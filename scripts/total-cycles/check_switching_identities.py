#!/usr/bin/env python3
"""Exact finite checks accompanying the functional Luce manuscript audit.

These check permutation identities and residual-set algebra, not asymptotics.
No random simulation, floating-point arithmetic, or external package is used.

Run: python3 check_switching_identities.py
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path
from typing import NamedTuple


class Data(NamedTuple):
    counts: tuple[int, ...]
    lengths: tuple[int, ...]
    cycle_ids: tuple[int, ...]
    powers: tuple[tuple[int, ...], ...]


def data(sigma: tuple[int, ...]) -> Data:
    n = len(sigma)
    counts = [0] * (n + 1)
    lengths = [0] * n
    ids = [-1] * n
    cid = 0
    for root in range(n):
        if ids[root] >= 0:
            continue
        cycle = []
        x = root
        while ids[x] < 0:
            ids[x] = cid
            cycle.append(x)
            x = sigma[x]
        assert x == root
        counts[len(cycle)] += 1
        for x in cycle:
            lengths[x] = len(cycle)
        cid += 1
    powers = []
    for root in range(n):
        orbit = [root]
        for _ in range(n):
            orbit.append(sigma[orbit[-1]])
        powers.append(tuple(orbit))
    return Data(tuple(counts), tuple(lengths), tuple(ids), tuple(powers))


def swap(sigma: tuple[int, ...], i: int, j: int) -> tuple[int, ...]:
    out = list(sigma)
    out[i], out[j] = out[j], out[i]
    return tuple(out)


def three(sigma: tuple[int, ...], i: int, j: int, k: int) -> tuple[int, ...]:
    """Right composition by the cycle (i j k)."""
    out = list(sigma)
    out[i], out[j], out[k] = sigma[j], sigma[k], sigma[i]
    return tuple(out)


def orientation(i: int, j: int, k: int, rates: tuple[int, ...]) -> tuple[int, int, int]:
    order = sorted((i, j, k), key=lambda x: (-rates[x], x))
    pos = order.index(i)
    return tuple(order[pos:] + order[:pos])


def check_two(max_n: int = 8) -> dict[str, int]:
    stats = dict(permutations=0, switches=0, marked_coefficients=0, good_split_cutoffs=0)
    for n in range(2, max_n + 1):
        cache = {sigma: data(sigma) for sigma in permutations(range(n))}
        incoming = [defaultdict(int) for _ in range(n)]
        for sigma, d in cache.items():
            stats['permutations'] += 1
            for i in range(n):
                ell = d.lengths[i]
                for r in range(1, ell):
                    j = d.powers[i][r]
                    target = swap(sigma, i, j)
                    td = cache[target]
                    assert td.lengths[j] == r
                    assert td.cycle_ids[i] != td.cycle_ids[j]
                    expected = list(d.counts)
                    expected[ell] -= 1
                    expected[r] += 1
                    expected[ell-r] += 1
                    assert tuple(expected) == td.counts
                    incoming[r][target] += 1
                    stats['switches'] += 1
                    for upper in range(r, ell-r):
                        # All lower cutoffs b<r follow by restricting this vector.
                        assert all(td.counts[s] - d.counts[s] == int(s == r)
                                   for s in range(1, upper + 1))
                        stats['good_split_cutoffs'] += 1
        for r in range(1, n):
            for target, td in cache.items():
                assert incoming[r][target] == r*(n-r)*td.counts[r]
                stats['marked_coefficients'] += 1
    return stats


def check_three(max_n: int = 7) -> dict[str, int]:
    stats = dict(profile_permutations=0, selected_summands=0, marked_coefficients=0)
    for n in range(3, max_n + 1):
        cache = {sigma: data(sigma) for sigma in permutations(range(n))}
        profiles = (tuple([1]*n), tuple(1 + (2*i+1) % 3 for i in range(n)))
        for rates in profiles:
            stats['profile_permutations'] += len(cache)
            for r in range(1, n-1):
                for s in range(1, n-r):
                    incoming: dict[tuple[int, ...], int] = defaultdict(int)
                    for sigma, d in cache.items():
                        for i in range(n):
                            if d.lengths[i] <= r+s:
                                continue
                            j, k = d.powers[i][r], d.powers[i][r+s]
                            if orientation(i, j, k, rates) == (i, k, j):
                                target = three(sigma, i, k, j)
                                td = cache[target]
                                assert td.lengths[j] == r and td.lengths[k] == s
                                assert len({td.cycle_ids[i], td.cycle_ids[j], td.cycle_ids[k]}) == 3
                                incoming[target] += 1
                                stats['selected_summands'] += 1
                            k, j = d.powers[i][s], d.powers[i][r+s]
                            if orientation(i, j, k, rates) == (i, j, k):
                                target = three(sigma, i, j, k)
                                td = cache[target]
                                assert td.lengths[j] == r and td.lengths[k] == s
                                assert len({td.cycle_ids[i], td.cycle_ids[j], td.cycle_ids[k]}) == 3
                                incoming[target] += 1
                                stats['selected_summands'] += 1
                    for target, td in cache.items():
                        expected = r*s*(n-r-s)*td.counts[r]*(td.counts[s] - int(r == s))
                        assert incoming[target] == expected
                        stats['marked_coefficients'] += 1
    return stats


def check_residual(max_n: int = 6) -> dict[str, int]:
    stats = dict(prefix_histories=0, invariance_coordinates=0)
    for n in range(2, max_n + 1):
        universe = set(range(n))
        # Three rank blocks, including a terminal block, possibly empty.
        blocks = [{y for y in range(n) if min(2, 3*y//n) == a} for a in range(3)]
        nu = (Fraction(1), Fraction(0), Fraction(0))
        for sigma in permutations(range(n)):
            d = data(sigma)
            H = [{x for x in range(n) if sigma[x] in blocks[a]} for a in range(3)]
            for root in range(n):
                for k in range(1, d.lengths[root]):
                    path = d.powers[root][:k+1]
                    S = universe - set(path[:-1])
                    T = universe - set(path[1:])
                    assert T-S == {root}
                    assert S-T == {path[-1]}
                    Ss = [S & row for row in H]
                    Ts = [T & row for row in blocks]
                    sizes = [len(row) for row in Ss]
                    assert sizes == [len(row) for row in Ts]
                    N = len(S)
                    # Check the exact pre-reset stationarity-defect formula.
                    for b in range(3):
                        lhs = Fraction(0)
                        for a in range(3):
                            if sizes[a]:
                                kernel = Fraction(len(Ts[a] & Ss[b]), sizes[a])
                                kernel += Fraction(len(Ts[a]-S), sizes[a])*nu[b]
                                lhs += Fraction(sizes[a], N)*kernel
                        lhs -= Fraction(sizes[b], N)
                        rhs = (nu[b] - len(Ss[b]-T))/N
                        assert lhs == rhs
                        stats['invariance_coordinates'] += 1
                    stats['prefix_histories'] += 1
    return stats


def main() -> None:
    result = {
        'scope': 'Exact finite identities only; not a proof of probabilistic asymptotics.',
        'two_clock_n_max': 8,
        'two_clock': check_two(),
        'three_clock_n_max': 7,
        'three_clock': check_three(),
        'residual_n_max': 6,
        'residual': check_residual(),
        'status': 'All assertions passed',
    }
    out = Path(__file__).resolve().parents[2] / '.build/verification/finite_checks.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
