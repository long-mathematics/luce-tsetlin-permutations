#!/usr/bin/env python3
"""Finite and numerical checks for the independence/peeling manuscript.

These checks do not certify asymptotic theorems or imported companion inputs.
Requires Python 3, NumPy and SciPy. Run from the repository root:
    python scripts/independence-peeling/check_consistency.py --output .build/verification/independence_peeling.json
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
from pathlib import Path
import random
import re
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.special import gamma

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "papers/independence-peeling/luce_independence_peeling.tex"


def cycles(perm: tuple[int, ...]) -> list[set[int]]:
    seen: set[int] = set()
    ans: list[set[int]] = []
    for start in range(len(perm)):
        if start in seen:
            continue
        block: set[int] = set()
        x = start
        while x not in seen:
            seen.add(x)
            block.add(x)
            x = perm[x]
        ans.append(block)
    return ans


def finite_deletion_check() -> dict:
    checked = 0
    for n in range(1, 7):
        universe = set(range(n))
        target_rows = [{i for i in range(n) if (3 * i) // n == a}
                       for a in range(3)]
        for perm in itertools.permutations(range(n)):
            cs = cycles(perm)
            source_rows = [{i for i in range(n) if perm[i] in row}
                           for row in target_rows]
            for mask in range(1 << len(cs)):
                deleted = set().union(*(cs[j] for j in range(len(cs))
                                        if mask & (1 << j)))
                remaining = universe - deleted
                v = len(deleted)
                for sr, tr in zip(source_rows, target_rows):
                    assert len(sr & deleted) == len(tr & deleted)
                    assert len(sr & remaining) == len(tr & remaining)
                    for other in source_rows:
                        initial = len(tr & other)
                        residual = len(tr & other & remaining)
                        assert 0 <= initial - residual <= v
                original = sorted((len(c) / n for c in cs), reverse=True)
                residual_parts = sorted((len(c) / len(remaining) for c in cs
                                         if c <= remaining), reverse=True) if remaining else []
                padded = residual_parts + [0.0] * (len(original) - len(residual_parts))
                assert sum(abs(x-y) for x, y in zip(original, padded)) <= 2*v/n + 1e-12
                checked += 1
    return {"conditional_cycle_deletion_cases": checked,
            "max_n": 6,
            "checks": "row balance, cell depletion, and 2v/n partition restoration"}


def annular_check() -> dict:
    count = 0
    cutoff_cases = 0
    rng = random.Random(20261020)
    families = [(40, list(itertools.combinations(range(1, 10), 4))),
                (64, list(itertools.combinations(range(1, 16), 4))),
                (100, sorted({tuple(sorted(rng.sample(range(1,25),4))) for _ in range(150)}))]
    for n, cutoffs in families:
        for small, b, u, large in cutoffs:
            assert small < b < u < large < n/4
            cutoff_cases += 1
            def contrib(length: int) -> tuple[int, int, int]:
                return (int(small < length <= b), int(u < length <= large),
                        int(length <= small or length > large))
            for r in range(small + 1, b + 1):
                exceptional = {l for l in range(r+1, n+1)
                               if l <= r+b or u < l <= u+r or large < l <= large+r}
                assert len(exceptional) <= 3*b
                assert not exceptional or max(exceptional) <= n//2
                for length in range(r+1,n+1):
                    before = contrib(length)
                    after1,after2 = contrib(r),contrib(length-r)
                    delta = tuple(x+y-z for x,y,z in zip(after1,after2,before))
                    if length not in exceptional:
                        assert delta == (1,0,0), (n,cutoffs,r,length,delta)
                    count += 1
            for r in range(u+1,large+1):
                for length in range(r+1,n+1):
                    before = contrib(length)
                    after1,after2 = contrib(r),contrib(length-r)
                    delta = tuple(x+y-z for x,y,z in zip(after1,after2,before))
                    if length > r+large:
                        assert delta == (0,1,0), (n,cutoffs,r,length,delta)
                    count += 1
    # The additional U' boundary is necessary for the stronger vector mark.
    small,b,u,large,r,length = 2,5,12,20,3,22
    assert not (r < length <= r+b or u < length <= u+r)
    assert large < length <= large+r
    return {"cutoff_configurations":cutoff_cases,"length_splittings":count,
            "additional_upper_boundary_witness":{"b_prime":small,"b":b,"U":u,"U_prime":large,
                                                 "r":r,"source_length":length}}


def pd_cutoff_check() -> dict:
    ws = np.array([-0.4, -0.2, 0.2, 0.4, 0.2j, -0.2+0.1j], dtype=complex)
    previous = lambda x: 1.0 + ws*np.log(x)
    y = previous(2.0)
    levels = {2:y.copy()}
    # F(x,w)=Phi(log x,w), F'=w F(x-1,w)/x, solved by method of steps.
    for k in range(2,128):
        old = previous
        result = solve_ivp(lambda x,y,old=old: ws*old(x-1)/x,
                           (float(k), float(k+1)), y, method="DOP853",
                           dense_output=True, rtol=2e-12, atol=2e-13)
        if not result.success:
            raise RuntimeError(result.message)
        previous = result.sol
        y = result.y[:,-1]
        if k+1 in (8,32,128):
            levels[k+1] = y.copy()
    target = np.exp(-np.euler_gamma*ws)/gamma(1+ws)
    errors = {}
    radius = 0.45
    for x, value in levels.items():
        actual = np.exp(-ws*np.log(x))*value
        error = np.abs(actual-target)
        bound = 2*radius**2/(1-2*radius)*x**(-(1-2*radius))
        assert float(error.max()) <= bound+2e-9
        errors[str(x)] = [float(a) for a in error]
    variance = []
    for eps in (0.6,0.4,0.25,0.1,1/128):
        x = 1/eps
        coefficient2 = quad(lambda u: math.log(u-1)/u, 2,x,epsabs=1e-12)[0] if x>2 else 0.0
        by_recurrence = 2*coefficient2-math.log(x)**2
        by_measure = -quad(lambda u: -math.log(max(eps,1-u))/u,
                           eps,1,points=[1-eps] if eps<0.5 else None,epsabs=1e-12)[0]
        assert abs(by_recurrence-by_measure)<1e-9
        defect = math.pi**2/6+by_measure
        assert -1e-10 <= defect <= 2*math.log(1/(1-eps))+1e-10
        variance.append({"epsilon":eps,"factorial_cumulant_2":by_measure,
                         "independent_formula_discrepancy":abs(by_recurrence-by_measure)})
    return {"complex_parameters":[[float(w.real),float(w.imag)] for w in ws],
            "residue_errors_at_inverse_cutoff":errors,
            "second_factorial_cumulant_checks":variance,
            "precision_note":"Floating-point consistency only; no certified quadrature or ODE enclosure."}


def source_check() -> dict:
    source = SOURCE.read_text()
    labels = re.findall(r"\\label\{([^}]+)\}",source)
    refs=[]
    for item in re.findall(r"\\(?:c|C|eq)?ref\{([^}]+)\}",source): refs.extend(item.split(","))
    assert len(labels)==len(set(labels))
    assert set(refs)<=set(labels)
    citations=[]
    for item in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}",source): citations.extend(item.split(","))
    bibliography=set(re.findall(r"\\bibitem\{([^}]+)\}",source))
    assert set(citations)<=bibliography
    for label in ("thm:mean-shift","thm:nuclear","thm:cumulants","conj:mod-poisson","cor:coefficientwise","lem:initial-peel"):
        assert label not in labels
    assert r"\cL(J^-,J^+,D_n(b',U'))" in source
    assert r"\cup(U',U'+r]" in source
    assert source.index(r"\appendix") < source.index(r"\begin{theorem}[Analytic cutoff")
    assert r"\label{eq:finite-deletion-recursion}" in source
    assert r"\texttt{eq:deletion-joint}" in source
    assert not any(ord(c)<32 and c not in "\n\r\t" for c in source)
    return {"labels":len(labels),"bibliography_entries":len(bibliography),
            "missing_or_duplicate_labels":0,"unresolved_citations":0,
            "duplicated_scalar_theorem_labels":0}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / ".build/verification/independence_peeling.json")
    args=parser.parse_args()
    result={"scope":"Finite and numerical consistency checks, not asymptotic or formal verification.",
            "finite_deletion":finite_deletion_check(),
            "annular_switching":annular_check(),
            "pd_cutoff":pd_cutoff_check(),
            "source_structure":source_check(),"all_checks_passed":True}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
