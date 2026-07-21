# Task: Scaling Exponent of a Laplacian Residual on a Network

**P28 disposition.** This is an **Open / Unexecuted**, underdetermined research specification, not a result report. [P28 Lambda, Cosmological Closure, Magnitude, and Dynamics](p28-lambda-cosmological-closure-magnitude-and-dynamics.md) governs all Lambda claims and grades. No tracked dataset, graph-family selection, output, or reproducer currently turns the candidate residuals below into P28 warrant.

Determine a single number: the exponent **p** in **Λ(N) ∝ N^(−p)** for large N, where Λ(N) is defined below. Show your work. If the problem is underdetermined — if p depends on a modeling choice — report each value and the choice it depends on. Report what the construction yields.

## Graphs

Let **G_N** be a connected graph on **N** nodes. Compute p for each of:

1. a **d-dimensional cubic lattice** region with N nodes (linear size L ~ N^(1/d)); give p as a function of d, then specialize to d = 1, 2, 3;
2. a **random d-regular graph** on N nodes;
3. an **Erdős–Rényi** graph G(N, q) above the connectivity threshold;
4. (optional) any graph with a stated finite spectral dimension d_s.

## Definitions

Let **L = D − A** be the graph Laplacian (D the degree-diagonal matrix, A the adjacency matrix). Let **λ₁(G_N)** be the smallest nonzero eigenvalue of L (the spectral gap / algebraic connectivity).

Define

  **Λ(N) := λ₁(G_N) / N.**

## Compute

**(a)** The exponent p in Λ(N) ∝ N^(−p), for each graph family above, with derivation. (The spectral gap has known closed-form or asymptotic expressions for these families.)

**(b)** Sensitivity. Recompute p when Λ(N) is instead defined as each of:
- λ₁
- √(λ₁) / N
- 1 / (diam(G_N)² · N), where diam is the graph diameter
- λ₁ / N²

Report p for each, so the dependence on the definition is explicit.

**(c)** State plainly whether p is robust across the graph families and across the definitions in (b), or whether it is sensitive to those choices, and if sensitive, to which.

## Output

For each graph family and each definition: the value of p, the derivation, and any point at which the problem is underdetermined. A flat report of what the construction gives.
