---
title: Closure-Inherited Metric
type: physics-closure-mass
created: 2026-06-23
updated: 2026-06-23
status: current
confidence: medium-high
section: Closure, confinement, and mass/value machinery
sources:
  - mass-derivation-three-faces.md
  - gauge-structure-result.md
  - mathematization-F8-done.md
---

# Closure-Inherited Metric

A load-bearing metric result extracted from [mass-derivation-three-faces](mass-derivation-three-faces.md). It fixes which measure belongs to the color closure before that measure is used in the mass-ratio synthesis.

## Result

The measure of one seated color closure is the closure-inherited metric

> Vol(SU(3))_closure = Vol(S^5) x Vol(S^3) = pi^3 x 2 pi^2 = 2 pi^5.

Status: **Registered** for the metric forcing. This page does not by itself derive the proton/electron ratio; it supplies the color-closure measure used by [mass-derivation-three-faces](mass-derivation-three-faces.md).

## Place in the physics section

Section: **Closure, confinement, and mass/value machinery**.

Read this page in the sequence given by [physics-section-guide](physics-section-guide.md). Current claim grade is governed by [physics-domain-mature-status](physics-domain-mature-status.md). Source/provenance links are collected in [physics-source-map](physics-source-map.md).

## Why the metric is 2 pi^5, not sqrt(3) pi^5

The abstract trace metric on SU(3) gives sqrt(3) pi^5. That is not the metric the framework is allowed to use for the physical color closure.

The framework's metric source is the primitive pairing on standings. It measures the standing's closure, not the abstract operator group detached from the standing. The standing is a normalized color vector in C^3, so the free color-standing part is the round S^5. The determinant-preserving completion supplies the round S^3. Their product gives 2 pi^5.

The entire difference between sqrt(3) pi^5 and 2 pi^5 lives in the determinant-balancing direction lambda_8 = diag(1,1,-2)/sqrt(3). In the abstract trace metric lambda_8 is counted as a free operator direction. In the closure-inherited metric it is not free: det = 1 makes that direction the forced completion of the closure. The same condition that yields SU(3) also fixes the measure by making the determinant-balancing direction dependent.

## Why confinement matters

Confinement removes the possibility of measuring a free abstract color group. There is no physical free color standing whose independent trace metric could be used. What exists is the closure that preserves determinant and closes color into a singlet. Therefore the measure belongs to the closure, not to an abstract color freedom considered apart from confinement.

## Grade

**Registered:**
- the pairing, not the trace form, is the framework metric source;
- the color standing is measured as S^5 with determinant-preserving S^3 completion;
- the 2/sqrt(3) discrepancy is localized wholly in lambda_8;
- det = 1 makes lambda_8 dependent rather than independent for the closure;
- confinement forbids replacing the closure-inherited metric with a free abstract group metric.

**Boundary:** the factor-3 spatialization is Registered in [mass-derivation-three-faces](mass-derivation-three-faces.md) as an additive seating result. The From-With chiral face is theorem-bounded there by

> epsilon_FW = c(3 pi^4)^-2,  3/2 <= c <= 9/4.

Only the exact internal selection of c remains Open.

See also: [mass-as-self-closure](mass-as-self-closure.md), [gauge-structure-result](gauge-structure-result.md).