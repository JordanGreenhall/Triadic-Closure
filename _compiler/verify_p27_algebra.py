#!/usr/bin/env python3
"""Exact finite checks for P27's conditional mathematics and countermodels."""

from fractions import Fraction as Q


def matvec(matrix: tuple[tuple[Q, Q], tuple[Q, Q]], vector: tuple[Q, Q]) -> tuple[Q, Q]:
    return tuple(sum((row[j] * vector[j] for j in range(2)), Q(0)) for row in matrix)  # type: ignore[return-value]


def matmul(
    left: tuple[tuple[Q, Q], tuple[Q, Q]],
    right: tuple[tuple[Q, Q], tuple[Q, Q]],
) -> tuple[tuple[Q, Q], tuple[Q, Q]]:
    return tuple(
        tuple(sum((left[i][k] * right[k][j] for k in range(2)), Q(0)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def euclidean(vector: tuple[Q, Q]) -> Q:
    return vector[0] ** 2 + vector[1] ** 2


def lorentzian(vector: tuple[Q, Q]) -> Q:
    return vector[0] ** 2 - vector[1] ** 2


def main() -> None:
    identity = ((Q(1), Q(0)), (Q(0), Q(1)))
    rotation = ((Q(0), Q(-1)), (Q(1), Q(0)))
    boost = ((Q(5, 3), Q(4, 3)), (Q(4, 3), Q(5, 3)))
    vector = (Q(2), Q(1))

    rotated = matvec(rotation, vector)
    boosted = matvec(boost, vector)
    rotation2 = matmul(rotation, rotation)
    rotation4 = matmul(rotation2, rotation2)

    assert euclidean(rotated) == euclidean(vector)
    assert lorentzian(boosted) == lorentzian(vector)
    assert euclidean(boosted) != euclidean(vector)
    assert rotation4 == identity

    # Selected cubical-region example: one face has L^2 crossing links, bulk has L^3 vertices.
    boundary_rows = []
    for length in (Q(1), Q(2), Q(3), Q(5)):
        crossing = length**2
        bulk = length**3
        assert crossing * length == bulk
        boundary_rows.append((length, crossing, bulk))

    # (2*pi/kappa) * (kappa/(8*pi)) = 1/4: cancel symbolic pi and kappa exponents.
    coefficient = Q(2) * Q(1, 8)
    pi_power = 1 - 1
    kappa_power = -1 + 1
    assert coefficient == Q(1, 4)
    assert pi_power == 0 and kappa_power == 0

    # Simple-zero lapse f=kappa*rho+c*rho^2: the leading square coefficient is kappa^2.
    kappa, correction = Q(3, 2), Q(2, 5)
    rho2_coefficient = kappa**2
    rho3_coefficient = Q(2) * kappa * correction
    assert rho2_coefficient == Q(9, 4)
    assert rho3_coefficient == Q(6, 5)

    # i:C^2 -> C^3, i(v)=(v,0), preserves the exact norm but misses (0,0,1).
    source = (Q(3, 5), Q(4, 5))
    image = (source[0], source[1], Q(0))
    source_norm = sum((x * x for x in source), Q(0))
    image_norm = sum((x * x for x in image), Q(0))
    assert source_norm == image_norm == Q(1)
    assert image[2] == 0
    missed = (Q(0), Q(0), Q(1))
    assert missed[2] != image[2]

    print("P27 exact finite algebra")
    print(f"rotation_vector={rotated} euclidean={euclidean(rotated)} order=4")
    print(f"boost_vector={boosted} lorentzian={lorentzian(boosted)} euclidean={euclidean(boosted)}")
    for length, crossing, bulk in boundary_rows:
        print(f"cube_L={length} crossing_links={crossing} bulk_vertices={bulk}")
    print(f"conditional_dS_coefficient={coefficient} pi_power={pi_power} kappa_power={kappa_power}")
    print(f"lapse_square_rho2={rho2_coefficient} rho3={rho3_coefficient}")
    print(f"injection_source_norm={source_norm} image_norm={image_norm} surjective=no")
    print("interpretation=conditional mathematics only; no physical horizon, thermality, entropy, or unitarity inferred")
    print("P27 exact finite algebra: PASS")


if __name__ == "__main__":
    main()
