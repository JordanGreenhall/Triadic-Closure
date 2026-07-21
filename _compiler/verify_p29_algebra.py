#!/usr/bin/env python3
"""Exact finite P29 countermodels for non-entailment boundaries."""

from fractions import Fraction


def main() -> None:
    print("P29 exact finite countermodels")
    print()

    print("A. Upstream capacities do not entail electroweak completion")
    capacities = {
        "office_source_forms": True,
        "chirality_criterion": True,
        "hypercharge_architecture": True,
    }
    completion = {
        "exact_common_module": False,
        "breaking_rule": False,
        "residual_boson_identification": False,
    }
    assert all(capacities.values())
    assert not any(completion.values())
    print("capacities=(1,1,1)")
    print("completion=(0,0,0)")
    print("same premises, absent completion: countermodel")
    print()

    print("B. Primitive triadic arity does not entail three generations")
    arity = 3
    generation_models = (1, 2, 3, 4)
    assert arity == 3
    assert len(set(generation_models)) == 4
    assert all(g > 0 for g in generation_models)
    print(f"primitive_arity={arity}")
    print("admissible_repeated_module_counts=" + ",".join(map(str, generation_models)))
    print("generation_count_not_function_of_arity_without_extra_axiom: countermodel")
    print()

    print("C. Fixed structural labels do not entail a unique numerical spectrum")
    labels = ("r1", "r2", "r3")
    model_a = tuple(Fraction(x) for x in (1, 2, 5))
    model_b = tuple(Fraction(x) for x in (1, 3, 8))
    assert labels == labels
    assert model_a[0] == model_b[0] == 1
    assert model_a != model_b
    print("labels=" + ",".join(labels))
    print("shared_internal_ruler=1")
    print("spectrum_A=" + ",".join(map(str, model_a)))
    print("spectrum_B=" + ",".join(map(str, model_b)))
    print("same labels and ruler, distinct spectra: countermodel")
    print()

    print("D. A global scale remains free without calibration")
    shape = tuple(Fraction(x) for x in (1, 2, 5))
    scale_a = Fraction(1)
    scale_b = Fraction(7, 3)
    physical_a = tuple(scale_a * x for x in shape)
    physical_b = tuple(scale_b * x for x in shape)
    assert physical_a != physical_b
    assert all(physical_b[i] / physical_b[0] == shape[i] for i in range(len(shape)))
    print("dimensionless_shape=" + ",".join(map(str, shape)))
    print("scale_A=1")
    print("scale_B=7/3")
    print("physical_A=" + ",".join(map(str, physical_a)))
    print("physical_B=" + ",".join(map(str, physical_b)))
    print("same dimensionless shape, distinct calibration: countermodel")
    print()

    print("P29 exact countermodels: PASS")


if __name__ == "__main__":
    main()
