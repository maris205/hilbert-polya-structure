# R4 D1: the isometric-cycle measure bridge

2026-09-09 UTC. Companion to A1's single full Lindahl–Rivera-Letelier measure question, not a second proposed paper for the same result. Exclusive write ownership: this directory. Proof-first investigation; no mathematical executions, external models, manuscript changes, shared-index writes or Git actions.

## Outcome

**Complete general criterion, with independent E1 internal review passed and zero must-fixes.** For finite single cycles of one isometry, a nearest pair yields an equal-distance coupling of all orbit points, and

$$
\min_{x\in C_d,y\in C_e}d(x,y)
=d_H(C_d,C_e)=W_1(\mu_d,\mu_e)=W_\infty(\mu_d,\mu_e).
$$

Therefore the uniform all-higher-level condition

$$
\sup_{e>d}\min_{x\in C_d,y\in C_e}d(x,y)\longrightarrow0
$$

proves, in a complete ultrametric space, compactness of the classical closure of the entire union, Hausdorff convergence of the cycles, and weak convergence of their uniform measures. It does not assume local compactness of the ambient field or metrizability of the ambient Berkovich line. The compact limit system is minimal and uniquely ergodic. If the cycle lengths are $p^e$, it is a finite $p$-power cycle or the $p$-adic adding machine.

The criterion is necessary and sufficient for Hausdorff-Cauchyness of the cycle sets. It is only sufficient, not claimed necessary, for weak convergence in a compactification.

Full proofs and exact hypothesis lists are in [PROOF_PACKAGE.md](PROOF_PACKAGE.md), Steps 1–8. Step 9 separately proves that the Berkovich closure of any bounded countable classical set is compact metrizable; this optional fallback also handles subsequential compactness correctly over very large ground fields.

## Exact quadratic interface

Retain every parameter of the public question: every odd prime $p$, every complete algebraically closed ultrametric field $K$ of characteristic $p$, and every $s=\lambda-1$ with $0<|s|<1$. Let $r=(p-1)/p$ and $v(x)=\log|x|/\log|s|$. The single cycles $S_e$ have length $p^e$ and lie on $|z|=|s|^r$. On the containing closed disk,

$$
P(x)-P(y)=(x-y)(1+s+x+y),\qquad |1+s+x+y|=1,
$$

so the complete-space isometry hypothesis is fulfilled.

The [A1 proof](../a1_optimal_cycle_measures/PROOF_PACKAGE.md), read in full after its author freeze, asserts and derives

$$
\frac1{p^e}\sum_{\alpha\in S_e}v(\beta-\alpha)
=c_d\ge d r^3+r^2(1+1/p)\longrightarrow+\infty,
\qquad \beta\in S_d,\ e>d.
$$

Taking a maximum at least equal to the average gives one pair at distance at most $|s|^{c_d}$, uniformly for all $e>d$. The general criterion then proves convergence on compact classical support and hence on the Berkovich projective line, quantitatively:

$$
d_H(S_d,A)\le |s|^{c_d},\qquad
W_\infty(\mu_d,\mu)\le |s|^{c_d}.
$$

This interface does not require nested higher splitting fields, an exact higher contact tree or chosen compatible orbit representatives. A1's separate E2 review is the arithmetic gate; this report does not preempt it.

The finite equality also proves aperiodicity. For a fixed pair $\beta\in S_d,\alpha\in S_e$, a fraction $p^{-d}$ of $S_e$ has the same contact $h=v(\beta-\alpha)$ with $\beta$, by iteration through multiples of $p^d$. Every other contact is at least $r$. Thus

$$
h\le p^dc_d-(p^d-1)r<\infty,
$$

uniformly in $e>d$. The limit stays a positive distance from each fixed old cycle. Its finite-cycle alternative would have to be one of those cycles or a fixed point; uniqueness excludes the former, while the fixed points $0,-s$ lie off the limiting sphere. Conditional on the same A1 identity, the limit is therefore the $p$-adic adding machine with nonatomic Haar probability. This refinement is proved explicitly in the companion proof, not inferred from a slogan about invariant measures.

## Boundary and source subtraction

An explicit compact ultrametric counterexample in the proof retains exactly one cycle of each period $p^e$, canonical top-$p$ cluster matching, and internal displacement distances $q^{(p^j+1)r}$, yet its measures have two distinct alternating limits. Consequently those previously available generic inputs alone do not establish convergence. The missing ingredient is cross-level contact or an equivalent occupancy/unique-ergodicity theorem. This is an abstract counterexample to that inference, not a counterexample for the actual quadratic polynomial.

| Primary source actually opened | Exact role and subtraction |
| --- | --- |
| Lindahl–Rivera-Letelier, [arXiv:1311.4478v3](https://arxiv.org/html/1311.4478v3), 26 May 2015, Problem 1.3; Theorem C and its $q=1$ discussion | Supplies the precise public question, cycles and sphere. Its periodic isolation corollary is recorded only as an unused alternative for aperiodicity. |
| Matthew Baker, [Berkovich lecture notes](https://swc-math.github.io/aws/2007/BakerNotesMarch21.pdf), Section 1 and Theorem 2.3.2 | Supplies established seminorm/topological background. Compactness of the specific classical support is proved here, not imported from Berkovich compactness. |
| Hurder–Lukina, [Essential holonomy of Cantor actions](https://homepages.math.uic.edu/~hurder/papers/93manuscript.pdf), Sections 2.2–2.3 | Records the classical inverse-limit and unique-Haar mechanism in a broader setting. D1 includes its own elementary cyclic-quotient proof; the generic mechanism is not asserted novel. |

Source priority for a solution to Problem 1.3 is a separate coordinator-assigned investigation. This report makes no assertion that the source problem remains open as of today, or that the combined author proof has passed admission.

## Handoff and exact remaining gates

1. [E1's completed independent review](../reviews/e1_isometric_cycle_limit/REVIEW.md) accepts the full general theorem and conditional quadratic interfaces, including the optional countable-closure lemma, abstract counterexample and direct aperiodicity refinement, with zero mathematical or source-applicability must-fixes. The unchanged reviewed proof SHA256 is `e2daa9770024c62e7b7fb09855d4c23eaa0c4cd0aa5416ad268288dbe569aedd`. This report received only the resulting review-status/link update after the review.
2. E2 is independently checking A1's polynomial argument, especially its all-field transport, nonzero derivative denominators and the all-$e>d$ quantifier. The A1 version read by D1 has SHA256 `038cdb412d1b83b94c1ebcfb742090e3937251225077a0f6842d7933c458174e`.
3. The coordinator owns proof adjudication, priority assessment, any paper admission and integration. A1 and D1 address one source measure question; the general criterion and optional strengthening are not separate paper slots.

The proof-writer skill drove the explicit hypothesis/status separation and complete dependency proof; research-lit drove primary-source subtraction; the Hénon batch workflow kept this work in the assigned proof lane and pending independent internal review. No target Euler factor, root number, automorphy or Hilbert–Pólya claim follows from these source-system measure results.
