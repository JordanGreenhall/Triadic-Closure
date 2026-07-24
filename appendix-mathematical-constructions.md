---
title: "Appendix — Mathematical Constructions"
type: technical-appendix
status: canonical-appendix
updated: 2026-07-24
---

# Appendix — Mathematical Constructions

This appendix carries technical constructions that support documents 02, 04, 06, and 07 and would make those principal documents unwieldy if stated there in full. It contains current constructions and current open boundaries only.

## 1. Conditioning network and intrinsic quantities

Let \(N\) be the horizontal build of standings under one-way conditioning.

- **Nodes** are standings individuated by finite addresses of turn-overs.
- **Edges** are direct conditionings: \(A\triangleleft B\) when \(B\) is reached from \(A\) by one turn-over.
- Office-content, J, the two exchange sectors, the pairing, rho-coherence, and conservation are carried by the standings; they are not added as external graph structure.

The construction is background-free: an address is an internal location in the build, and address depth is internal succession. No spatial or temporal arena is presupposed.

A quantity on \(N\) is admissible only when it is definable from addresses, edge structure, node-content, rho-coherence, and conservation. Background rate and density are therefore inadmissible before the metric is built. Coherence-participation, depth, address-separation, sector-content, and edge-counts are intrinsic.

Two count structures are distinct:

- **Depth:** address length, an oriented From-count.
- **Address-separation:** minimal conditioning-chain length between standings, a relational With-count.

## 2. Step atomicity

One conditioning is one turn-over. A partial turn-over would be neither a completed standing at depth \(n+1\) nor the unaltered standing at depth \(n\); it supplies no address at which it can stand. A conditioning therefore either occurs or does not occur. Depth is discretely graded by oriented succession, and there is no finer step-arithmetic supplied by the inherited object.

This establishes atomic temporal substructure. It does not deny a rule-given continuum as a large-scale representation, and it does not by itself establish the full spatial manifold.

## 3. Flat metric construction

A unit of depth and a unit of separation are the same act — one conditioning — read under the From-count and With-count. Their metric conversion is therefore the identity, written \(c=1\). The numerical value assigned to \(c\) in external units is a unit conversion, not a framework particular.

On the three interchangeable spatial degrees, an additive sign-definite interval invariant under continuous spatial mixing is, up to scale,

\[
\delta_{ij}\,\Delta x^i\Delta x^j
=(\Delta x^1)^2+(\Delta x^2)^2+(\Delta x^3)^2.
\]

Direct conditioning at the propagation bound supplies the null relation \(|\Delta x|=\Delta t\). Combining the spatial form with the null relation yields

\[
\mathrm ds^2
=-(\Delta t)^2+(\Delta x^1)^2+(\Delta x^2)^2+(\Delta x^3)^2.
\]

At the scope of a given smooth Lorentzian manifold, the transformations preserving the causal and interval structure are the Lorentz transformations; preserving the one-way conditioning orientation selects the orthochronous component. The recovery of the smooth manifold and the exact continuous-symmetry limit retain the conditions stated in documents 04 and 07.

## 4. Realizability weighting

For a standing \(\sigma\) and an admissible next-configuration ray \(k\) in a finite-dimensional complex space with positive Hermitian form \(h\), define

\[
C_\sigma(k)
=
\frac{|h(\sigma,k)|^2}{h(k,k)},
\qquad k\ne0.
\]

This functional is non-negative, ray-invariant, maximal on alignment, and zero on \(h\)-orthogonality.

The frame condition is not a statement about observed frequencies. Orthogonal alternatives are registrably distinct; a complete orthonormal fork is a complete admissible decomposition; the standing of one candidate cannot depend on which merely-held co-alternatives are used to complete that fork. Therefore, for every complete \(h\)-orthonormal basis \(\{e_i\}\),

\[
\sum_i w_\sigma(e_i)=W_\sigma,
\]

with \(W_\sigma\) independent of the chosen held decomposition. In dimension at least three, the frame-function theorem gives a positive operator \(\rho_\sigma\) with

\[
w_\sigma(e)=\langle e,\rho_\sigma e\rangle.
\]

For a pure standing, \(\rho_\sigma=|\sigma\rangle\langle\sigma|\), so the weighting law is the Born form \(|h(\sigma,e)|^2\), after normalization. Dimension two does not by itself force the unique quadratic frame function.

This is a realizability weighting. It does not require, and must not be converted into, an identity between weight and empirical frequency.

## 5. Standing vector and local tilt

Let the elementary next-couplings of a content be the basis \(e_i\). A conserved coherence-flow on the conditioning network has stationary measure proportional to conditioning degree,

\[
\pi_i=\frac{d_i}{\sum_j d_j}.
\]

Taking the standing amplitude as the square root of this measure gives

\[
\sigma_i=\sqrt{\pi_i}=\frac{\sqrt{d_i}}{\sqrt{\sum_j d_j}}.
\]

For an elementary coupling,

\[
C_\sigma(e_i)=|\sigma_i|^2
=\frac{d_i}{\sum_j d_j}.
\]

The local coherence-participation tilt is therefore linear in conditioning degree. The selection of the conserved-flow standing rather than another global standing remains a stated selection unless and until uniqueness from rho-coherence is established.

## 6. Weak-field curvature bridge

With atomic depth and the conserved-flow tilt, the weak-field clock sector is represented by

\[
g_{00}=-\left(\frac{d_0}{d}\right)^2,
\qquad
\Phi=-\frac{d-d_0}{d_0}.
\]

At the tested weak-field static scope, the induced motion agrees with the geodesics of this metric and nearby free trajectories exhibit radial stretch and transverse squeeze: genuine tidal curvature rather than a uniform background force.

The long-range field is the perturbation of the conserved coherence-flow, not bare local degree. Its graph-Laplacian Green function on the three-dimensional spatial structure is harmonic outside a localized source, yielding the weak-field Poisson form

\[
\nabla^2\Phi=4\pi G\rho.
\]

An oriented conditioning carries a worldline tangent \(V^\mu\). Transport of that orientation gives a symmetric source

\[
T^{\mu\nu}=\sum_k a_k V_k^\mu V_k^\nu,
\]

with conservation inherited from the conserved conditioning flow. Given locality, metric second-order dependence, and this symmetric conserved source, the Lovelock rigidity theorem selects the Einstein tensor plus the metric term. The full nonlinear field equation remains conditional on the exact second-order and continuum premises stated in document 07; \(G\) is not internally fixed here, and the status and meaning of \(\Lambda\) are governed exclusively by document 07.

## 7. Exact boundaries

The appendix does not establish:

- an observed-frequency law from realizability weighting;
- a rule-free completed continuum;
- smooth-manifold recovery without G1's stated conditions;
- the exact strong-field nonlinear regime;
- a unique conserved-flow standing unless the remaining selection is discharged;
- the value of \(G\);
- any independent Lambda result.
