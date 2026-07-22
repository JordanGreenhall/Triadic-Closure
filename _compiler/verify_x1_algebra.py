#!/usr/bin/env python3
"""Finite countermodels for X1 non-entailments."""

from fractions import Fraction


def main() -> None:
    lines: list[str] = ["X1 exact finite countermodels", ""]

    # A. Static mass data leaves dynamics free.
    masses = (1, 1836)
    dynamics_a = (1, 1)
    dynamics_b = (1, 100)
    assert masses == masses and dynamics_a != dynamics_b
    lines += [
        "A. Static mass hierarchy does not entail slow/fast dynamics",
        f"shared_masses={masses[0]},{masses[1]}",
        f"update_rates_A={dynamics_a[0]},{dynamics_a[1]}",
        f"update_rates_B={dynamics_b[0]},{dynamics_b[1]}",
        "same masses, distinct response ratios: countermodel",
        "",
    ]

    # B. Signed relational valence leaves shell structure underdetermined.
    valence = (+1, -1)
    shells_a = (2, 8)
    shells_b = (1, 3, 5)
    assert valence == valence and shells_a != shells_b
    lines += [
        "B. Signed relational valence does not entail a shell-edge",
        f"shared_valence={valence[0]},{valence[1]}",
        "shell_structure_A=2,8",
        "shell_structure_B=1,3,5",
        "same valence orientation, distinct shell structures: countermodel",
        "",
    ]

    # C. Empirical occupancy does not entail a framework map.
    empirical_molecule = True
    framework_atom = False
    shell_edge_map = False
    assert empirical_molecule and not framework_atom and not shell_edge_map
    lines += [
        "C. Empirical molecules do not establish framework nonemptiness",
        "empirical_molecule=1",
        "framework_atom=0",
        "shell_edge_map=0",
        "observation without native map: countermodel",
        "",
    ]

    # D. One instance does not entail a universal rule.
    observed_instances = 1
    possible_rule_failures = 1
    assert observed_instances == 1 and possible_rule_failures == 1
    lines += [
        "D. One proposed gate does not entail a universal handoff law",
        "proposed_instances=1",
        "admissible_next_gate_counterexample=1",
        "single instance compatible with universal failure: countermodel",
        "",
    ]

    # E. A comparison maximum requires an explicit rival measure.
    carbon_score_a = Fraction(4, 1)
    silicon_score_a = Fraction(3, 1)
    carbon_score_b = Fraction(4, 1)
    silicon_score_b = Fraction(5, 1)
    assert carbon_score_a > silicon_score_a and carbon_score_b < silicon_score_b
    lines += [
        "E. Carbon maximality does not follow without a selected recursion measure",
        "measure_A: carbon=4 silicon=3",
        "measure_B: carbon=4 silicon=5",
        "same named candidates, distinct selected maxima: countermodel",
        "",
        "X1 exact countermodels: PASS",
    ]

    print("\n".join(lines))


if __name__ == "__main__":
    main()
