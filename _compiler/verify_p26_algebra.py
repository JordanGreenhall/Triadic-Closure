#!/usr/bin/env python3
"""Reproduce P26's bounded Hermitian/holonomy algebra with exact rationals."""

from fractions import Fraction as Q

Vector = tuple[tuple[Q, Q], ...]


def inner(x: Vector, y: Vector) -> tuple[Q, Q]:
    real = Q(0)
    imag = Q(0)
    assert len(x) == len(y)
    for (a, b), (c, d) in zip(x, y):
        real += a * c + b * d
        imag += a * d - b * c
    return real, imag


def main() -> None:
    x: Vector = ((Q(1), Q(0)), (Q(0), Q(0)), (Q(0), Q(0)))
    y: Vector = ((Q(0), Q(1)), (Q(0), Q(0)), (Q(0), Q(0)))
    xy = inner(x, y)
    yx = inner(y, x)
    assert xy == (Q(0), Q(1))
    assert yx == (Q(0), Q(-1))
    assert xy[1] == -yx[1]
    assert inner(x, x)[1] == 0

    potential = {"b": Q(2), "x": Q(5), "y": Q(-1), "xy": Q(7)}

    def coboundary(u: str, v: str) -> Q:
        return potential[v] - potential[u]

    exact_loop = (
        coboundary("b", "x")
        + coboundary("x", "xy")
        - coboundary("b", "y")
        - coboundary("y", "xy")
    )
    assert exact_loop == 0

    phase = {
        ("b", "x"): Q(1),
        ("x", "xy"): Q(2),
        ("b", "y"): Q(0),
        ("y", "xy"): Q(0),
    }
    nonzero_loop = (
        phase["b", "x"]
        + phase["x", "xy"]
        - phase["b", "y"]
        - phase["y", "xy"]
    )
    assert nonzero_loop == 3

    print("P26 exact algebra: PASS")
    print("imaginary-part antisymmetry: PASS")
    print("complex-carrier nonvanishing countermodel: PASS")
    print("exact-connection telescoping: PASS")
    print("nonzero-loop obstruction to exactness: PASS")


if __name__ == "__main__":
    main()
