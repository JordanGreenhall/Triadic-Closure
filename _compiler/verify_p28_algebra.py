#!/usr/bin/env python3
"""Exact finite checks for P28's combinatorics, identity, and countermodels."""

from fractions import Fraction as Q
from math import comb


def main() -> None:
    planes = [(d, comb(d, 2)) for d in range(1, 6)]
    assert planes == [(1, 0), (2, 1), (3, 3), (4, 6), (5, 10)]

    # Exact definitional identity at one rational witness.
    c, h0, lam = Q(5), Q(2), Q(7)
    omega = lam * c**2 / (Q(3) * h0**2)
    reach = c / h0
    reconstructed = Q(3) * omega / reach**2
    assert omega == Q(175, 12)
    assert reach == Q(5, 2)
    assert reconstructed == lam

    # Dimensional scaling leaves every dimensionless coefficient alpha available.
    radius = Q(11, 3)
    coefficient_rows = []
    for alpha in (Q(1), Q(2), Q(3), Q(7, 2)):
        value = alpha / radius**2
        assert value * radius**2 == alpha
        coefficient_rows.append((alpha, value))
    assert len({value for _, value in coefficient_rows}) == 4

    # Conditional flatness exclusion: conclusion follows only when both premises hold.
    flatness_rows = []
    for no_arena in (False, True):
        for exhaustive_two_mode in (False, True):
            excludes_unsourced_background = no_arena and exhaustive_two_mode
            flatness_rows.append((no_arena, exhaustive_two_mode, excludes_unsourced_background))
    assert flatness_rows.count((True, True, True)) == 1
    assert sum(int(row[2]) for row in flatness_rows) == 1

    print("P28 exact finite algebra")
    for dimension, count in planes:
        print(f"spatial_dimension={dimension} unordered_two_planes={count}")
    print(
        "definitional_witness="
        f"c={c} H0={h0} Lambda={lam} Omega_Lambda={omega} R_H={reach} reconstructed_Lambda={reconstructed}"
    )
    for alpha, value in coefficient_rows:
        print(f"scaling_countermodel_alpha={alpha} R_H={radius} Lambda_alpha={value}")
    for no_arena, exhaustive, excluded in flatness_rows:
        print(
            "flatness_conditional="
            f"no_arena={str(no_arena).lower()} exhaustive_two_mode={str(exhaustive).lower()} "
            f"unsourced_background_excluded={str(excluded).lower()}"
        )
    print("interpretation=plane count does not select a coefficient; the present expression is definitional; flatness is conditional")
    print("P28 exact finite algebra: PASS")


if __name__ == "__main__":
    main()
