# F8, Done Properly: The Coherence-Participation Functional, Constructed and Derived

### Replaces the earlier prose F8. The next-configuration space is constructed explicitly from N's intrinsic data; the functional C(k) is **derived** from the properties it must satisfy (not asserted), and its **uniqueness** is established via the frame-function (Gleason) argument, with the exact dimensional condition stated. All non-trivial claims were checked by direct computation; the scripts and their outputs are recorded inline. Honesty note: where a step is a cited theorem rather than something computed here, it is marked **[cited]**; where it is verified numerically, **[checked]**; where it is a structural definition, **[def]**.

---

## 1. The objects (from N's intrinsic data, F1.2-admissible)

A content P stands at a node of the conditioning-network N. Construct the space of P's next-coupling-configurations:

- **[def] The elementary couplings.** P has finitely many admissible elementary next-couplings — one per neighbor/aspect P can condition at the next succession count. (Finiteness: F2 atomicity + finite conditioning-degree per step.) Label them $e_1, \dots, e_n$. They are the basis directions of the configuration space.
- **[def] The configuration space** $V = \mathbb{C}^n$, over rule-given $\mathbb{C}$ (0.9). A **next-configuration** is a vector $k = \sum_i k_i e_i \in V$ — a coherent superposition of elementary couplings (coherent because the standing is a ρ-coherent structure and realizability carries all forks with amplitudes, 0.5).
- **[conditional input] The pairing** $h$: M5 constructs a perfect `J`-invariant rational bilinear form, and M6 may extend it to a non-degenerate Hermitian form over rule-given $\mathbb C$. Neither step supplies positive definiteness. This F8 construction therefore assumes a separately licensed positive-definite physics pairing (probability-readability); conditional on that input, $(V,h)$ is a finite-dimensional inner-product space and may be written $h(x,y)=x^\dagger H y$ for Hermitian positive-definite $H$. M5 is not the warrant for this positivity.
- **[def] The standing vector** $\sigma \in V$: the accumulated standing, projected onto P's coupling-options — i.e. how the coherence the standing has already established constrains which of P's next-couplings cohere. It lives in the same space $V$ (the standing constrains P's couplings *through the pairing*, so its bearing on P is a vector paired against P's configurations).

Every object is built from N's intrinsic data plus the explicitly conditional positive-definite physics pairing — couplings (edges), the licensed pairing, ρ-coherence and conservation (0.5, 0.6) in the standing vector. No background metric or measure enters after that pairing is licensed. Admissible by F1.2 (P2) only under the stated pairing condition.

## 2. The requirements C(k) must satisfy

Coherence-participation $C(k)$ — the degree to which configuration $k$ coheres with the standing — must satisfy:

- **R1.** Real, non-negative (a degree of coherence).
- **R2.** Ray-invariant: $C(\lambda k) = C(k)$ for $\lambda \in \mathbb{C}^\times$ (a configuration is a coherent direction; overall scale/phase is not content).
- **R3.** Determined by $h$ and $\sigma$ only (F1.2 — no other structure available).
- **R4.** Maximal when $k \parallel \sigma$, zero when $k \perp_h \sigma$, monotone in alignment.
- **R5.** Frame-independent normalization: across any $h$-orthonormal basis $\{k_a\}$ of $V$, $\sum_a C(k_a)$ is a constant independent of the basis — so that $P(k_a) = C(k_a)/\sum_b C(k_b)$ is a probability (the realizability-weighting law's requirement that actualization-frequencies be a frame-independent measure).

## 3. The functional, and verification of R1–R5

**The functional:**
$$ C(k) = \frac{|h(\sigma, k)|^2}{h(k,k)} \qquad (k \neq 0). $$
Equivalently $C(k) = |h(\sigma, \hat k)|^2$ with $\hat k = k/\sqrt{h(k,k)}$ the $h$-unit configuration.

**[checked]** R1, R2, R4 (script `f8_requirements.py`, n = 5, random Hermitian positive-definite $H$):
- R1: $C(k)$ real with zero imaginary part; $\geq 0$.
- R2: $|C(\lambda k) - C(k)| = 0$ for random complex $\lambda$.
- R4: $C(\sigma) = h(\sigma,\sigma)$ exactly (maximum); $C(k_\perp) \sim 10^{-30}$ for $k \perp_h \sigma$; over $10^4$ random $k$, $\max C(k) \le h(\sigma,\sigma)$ (Cauchy–Schwarz).

**[checked]** R5 (script `f8_R5.py`, n = 6): for an $h$-orthonormal basis (built by Cholesky $H = LL^\dagger$, columns of $(L^\dagger)^{-1}$), $\sum_a C(k_a) = h(\sigma,\sigma)$ exactly; rotating the basis by a random $h$-unitary leaves the sum unchanged ($|S_1 - S_2| < 10^{-9}$); the normalized $P(k_a)$ sum to 1, lie in $[0,1]$, and equal the Born form $|h(\sigma,k_a)|^2 / h(\sigma,\sigma)$. The mechanism is Parseval: for $h$-orthonormal $\{k_a\}$, $\sum_a |h(\sigma,k_a)|^2 = h(\sigma,\sigma)$.

So $C(k) = |h(\sigma,k)|^2/h(k,k)$ satisfies R1–R5, and the induced probability $P(k_a) = |h(\sigma,k_a)|^2/h(\sigma,\sigma)$ is exactly the **Born measure** — confirming F8's claim that gravity's coherence-participation weighting and quantum probability are the *same* functional (the realizability-weighting law's physics instance).

## 4. Uniqueness — the functional is forced, not guessed

Meeting R1–R5 is not enough; the question is whether $C$ is the **unique** such functional. It is, in dimension $\ge 3$, and this is the load-bearing result.

**Reduction.** By R2 and R3, $C(k)$ depends only on the $h$-unit ray $\hat k$ and on $\sigma$, through $h$-invariant scalars. The only $h$-unitary-invariant scalar built from a fixed $\sigma$ and a unit $\hat k$ is the overlap $t = |h(\hat\sigma, \hat k)|^2 \in [0,1]$ (with $\hat\sigma$ the unit standing). So $C(k) = |\sigma|^2 f(t)$ for some $f:[0,1]\to[0,\infty)$ with $f(0)=0$, $f$ increasing (R4). R5 demands: for every $h$-orthonormal basis $\{k_a\}$, with $t_a = |h(\hat\sigma,k_a)|^2$ (so $\sum_a t_a = 1$ by Parseval), the sum $\sum_a f(t_a)$ is basis-independent. A function $f$ with this property is a **frame function**.

**[checked]** Only the linear frame function survives (script `f8_uniqueness.py`, n = 4, $2000$ random $h$-orthonormal bases per candidate):

| $f(t)$ | mean $\sum_a f(t_a)$ | std (basis-dependence) | basis-independent? |
|---|---|---|---|
| $t$ (Born) | $1.000000$ | $3.6\times10^{-16}$ | **yes** |
| $t^2$ | $0.40$ | $1.1\times10^{-1}$ | no |
| $\sqrt t$ | $1.83$ | $1.1\times10^{-1}$ | no |
| $t^{1.5}$ | $0.61$ | $7.2\times10^{-2}$ | no |
| $t - t^2$ | $0.60$ | $1.1\times10^{-1}$ | no |

Only $f(t) = t$ gives a basis-independent sum; every nonlinear candidate's sum varies with the basis (std $\sim 0.1$), violating R5. Hence R5 forces $f$ linear, hence $C(k) = |h(\sigma,k)|^2/h(k,k)$ uniquely.

**[cited] This is Gleason's theorem.** The result "every frame function on a Hilbert space of dimension $\ge 3$ is linear" is Gleason (1957); the numerical check above is a verification, not a new proof. The reduction shows R1–R5 are exactly the frame-function hypotheses.

**[checked] The dimensional condition is real and necessary** (script `f8_dim2.py`): in dimension $n = 2$, an orthonormal basis is $\{k, k_\perp\}$ with $t_1 + t_2 = 1$, so $\sum f(t_a) = f(t) + f(1-t)$, which is constant for *many* nonlinear $f$ — e.g. the smoothstep $f(t) = 3t^2 - 2t^3$ satisfies $f(t)+f(1-t)=1$ identically. So $n=2$ does **not** force Born; both Born and the nonlinear smoothstep give constant sums. **Uniqueness of $C$ requires $\dim V \ge 3$.**

## 5. Status of F8 — stated exactly

**Established conditional on the licensed positive-definite physics pairing (constructed + derived + uniqueness):**
- The next-configuration space $(V = \mathbb{C}^n, h)$ is built from N's intrinsic data (elementary couplings, the pairing). [def, F1.2-admissible]
- $C(k) = |h(\sigma,k)|^2/h(k,k)$ satisfies the five required properties R1–R5. [checked]
- $C$ is the **unique** functional satisfying R1–R5 when $\dim V \ge 3$, by the frame-function/Gleason argument; the induced probability is the Born measure. [checked + cited]
- Gravity's coherence-participation weighting **is** the realizability-weighting law's physics instance (same functional as Born). [established]

**Honest conditions and gaps:**
- **Dimensional condition $\dim V \ge 3$** [open-conditional]: uniqueness requires P to have at least 3 admissible elementary next-couplings. Generic nodes plausibly satisfy this, but it is a genuine condition, not automatic — to be discharged by showing admissible conditioning-degree $\ge 3$ generically (likely from the three-fold spatial structure F3, but not proved here).
- **The standing vector $\sigma$** [def, partially open]: I defined $\sigma$ as "the standing projected onto P's coupling-options through the pairing." That it is *well-defined and unique* — that the accumulated standing determines a single such $\sigma \in V$ — is asserted at the level of definition; making it a construction (an explicit map from the accumulated standing to $\sigma \in V$) is owed. This is the next real piece, and it is the hinge for F9 (the degree-derivative needs $\sigma$ as an explicit function of the neighbours' conditioning-degrees).
- **Positive-definite pairing input** [open / separately owned]: M5 supplies a perfect rational form and, conditional on M6, a non-degenerate Hermitian extension; it does not supply positivity. The positive-definite form used for Hilbert-space structure, orthonormal frames, Cauchy–Schwarz, and Gleason must be constructed or selected in its physics owning unit. F8 is conditional until that dependency is discharged.

**What F8 now is, honestly:** conditional on a licensed positive-definite physics pairing, the functional is constructed from N's data and derived (uniqueness via Gleason, dimension $\ge 3$ stated), not asserted “in essence.” The owed pieces are that pairing construction, the dimensional condition, and the explicit construction of $\sigma$ from the standing — the last being exactly what F9 needs.

---

### Appendix: scripts (run, outputs recorded above)
- `f8_requirements.py` — R1, R2, R4 verification.
- `f8_R5.py` — R5 (Parseval normalization, basis-independence, Born form).
- `f8_uniqueness.py` — frame-function uniqueness: only $f(t)=t$ is basis-independent (n=4).
- `f8_dim2.py` — the $n=2$ exception: uniqueness needs $\dim \ge 3$.
