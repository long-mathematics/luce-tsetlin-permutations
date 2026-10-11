#!/usr/bin/env python3
"""Finite checks for the total-cycle Poisson smoothing proof.

Exact checks: discrete Taylor identity, Poisson Charlier moment identity,
and passivity of the omitted-cycle count under every eligible finite split.
Numerical checks: the second-difference norm and convolution inequality.
These are consistency checks, not a substitute for the analytic proof.

Requires Python 3.10+, NumPy and SciPy for the numerical portion.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


def shift(a: list[Fraction], amount: int, size: int) -> list[Fraction]:
    return [Fraction(0)] * amount + a[: size - amount] + [Fraction(0)] * max(0, size - amount - len(a))


def exact_taylor_checks() -> int:
    count = 0
    for size in range(1, 9):
        p = [Fraction(i + 1, size * (size + 1) // 2) for i in range(size)]
        for r in range(13):
            length = size + r + 3
            p0 = shift(p, 0, length)
            p1 = shift(p, 1, length)
            p2 = shift(p, 2, length)
            d1 = [y - x for x, y in zip(p0, p1)]
            d2 = [z - 2 * y + x for x, y, z in zip(p0, p1, p2)]
            rhs = [x + r * y for x, y in zip(p0, d1)]
            for j in range(max(0, r - 1)):
                term = shift(d2, j, length)
                rhs = [x + (r - 1 - j) * y for x, y in zip(rhs, term)]
            assert rhs == shift(p, r, length), (size, r)
            count += 1
    return count


def exact_charlier_checks() -> int:
    values = [Fraction(1, 100), Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(3), Fraction(17, 3), Fraction(100), Fraction(1000)]
    for lam in values:
        m1 = lam
        m2 = lam**2 + lam
        m3 = lam**3 + 3 * lam**2 + lam
        m4 = lam**4 + 6 * lam**3 + 7 * lam**2 + lam
        a = 2 * lam + 1
        eh2 = m4 - 2 * a * m3 + (a*a + 2 * lam*lam) * m2 - 2 * a * lam*lam * m1 + lam**4
        assert eh2 == 2 * lam*lam, lam
    return len(values)


def cycle_lengths(p: tuple[int, ...] | list[int]) -> tuple[list[int], list[int]]:
    n = len(p)
    seen = [False] * n
    lengths: list[int] = []
    by_vertex = [0] * n
    for i in range(n):
        if seen[i]:
            continue
        cyc = []
        j = i
        while not seen[j]:
            seen[j] = True
            cyc.append(j)
            j = p[j]
        lengths.append(len(cyc))
        for j in cyc:
            by_vertex[j] = len(cyc)
    return lengths, by_vertex


def exact_passivity_checks(max_n: int = 7) -> dict[str, int]:
    permutations = checks = 0
    for n in range(3, max_n + 1):
        for p in itertools.permutations(range(n)):
            permutations += 1
            lengths, by_vertex = cycle_lengths(p)
            for b, upper in [(0, 1), (0, 2), (1, 2)]:
                if upper >= n:
                    continue
                boundary = sum(r <= b or r > upper for r in lengths)
                core = [lengths.count(r) for r in range(b + 1, upper + 1)]
                for i in range(n):
                    j = i
                    for r in range(1, upper + 1):
                        j = p[j]
                        if r <= b or by_vertex[i] <= r + upper:
                            continue
                        q = list(p)
                        q[i], q[j] = q[j], q[i]  # right composition by (i,j)
                        qlens, _ = cycle_lengths(q)
                        qbound = sum(s <= b or s > upper for s in qlens)
                        qcore = [qlens.count(s) for s in range(b + 1, upper + 1)]
                        expected = list(core)
                        expected[r - b - 1] += 1
                        assert qbound == boundary and qcore == expected
                        assert len(qlens) == len(lengths) + 1
                        checks += 1
    return {"permutations": permutations, "good_splits": checks, "max_n": max_n}


def numerical_checks() -> list[dict[str, float | str]]:
    import numpy as np
    from scipy.stats import binom, poisson

    residues = {
        "zero": [(0, 1.0)],
        "deterministic_one": [(1, 1.0)],
        "deterministic_eight": [(8, 1.0)],
        "bernoulli": [(0, 0.63), (1, 0.37)],
        "uniform_0_12": [(i, 1.0 / 13) for i in range(13)],
        "rare_forty": [(0, 0.98), (40, 0.02)],
        "rare_two_hundred": [(0, 0.999), (200, 0.001)],
        "binomial": [(i, float(binom.pmf(i, 40, 0.12))) for i in range(41)],
    }
    rows = []
    for lam in [0.25, 1.0, 3.0, 10.0, 30.0, 100.0, 1000.0, 10000.0]:
        for name, law in residues.items():
            nu = sum(r * p for r, p in law)
            f2 = sum(r * (r - 1) * p for r, p in law)
            maximum = max(r for r, _ in law)
            end = int(math.ceil(lam + maximum + 20 * math.sqrt(lam + maximum + 1) + 100))
            k = np.arange(end + 1)
            base = poisson.pmf(k, lam)
            d2 = poisson.pmf(k - 2, lam) - 2 * poisson.pmf(k - 1, lam) + base
            norm = float(np.abs(d2).sum())
            norm_bound = math.sqrt(2) / lam
            mixture = sum(p * poisson.pmf(k - r, lam) for r, p in law)
            target = poisson.pmf(k, lam + nu)
            tv = float(np.abs(mixture - target).sum()) / 2
            bound = (f2 + nu * nu) / (2 * math.sqrt(2) * lam)
            assert norm <= norm_bound + 1e-9, (lam, name, norm, norm_bound)
            assert tv <= bound + 1e-9, (lam, name, tv, bound)
            assert abs(float(mixture.sum()) - 1) < 1e-8
            assert abs(float(target.sum()) - 1) < 1e-8
            rows.append({"lambda": lam, "residual": name, "total_variation": tv, "bound": bound, "second_difference_norm": norm, "norm_bound": norm_bound})
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("smoothing_checks.json"))
    parser.add_argument("--max-n", type=int, default=7)
    args = parser.parse_args()
    if not 3 <= args.max_n <= 8:
        parser.error("--max-n must be between 3 and 8; enumeration is factorial.")
    result = {
        "status": "all checks passed",
        "exact_discrete_taylor_cases": exact_taylor_checks(),
        "exact_charlier_moment_cases": exact_charlier_checks(),
        "exact_passivity": exact_passivity_checks(args.max_n),
        "numerical_cases": numerical_checks(),
        "scope": "Finite consistency checks only; not an asymptotic proof or formal verification.",
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: (len(v) if k == "numerical_cases" else v) for k, v in result.items()}, indent=2))


if __name__ == "__main__":
    main()
