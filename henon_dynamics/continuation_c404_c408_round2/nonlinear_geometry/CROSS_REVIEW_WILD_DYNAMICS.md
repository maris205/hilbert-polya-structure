# Independent internal review: logarithmic wild-polynomial weights

2026-09-06. Non-author review by the nonlinear-geometry lane, at the
coordinator's request. This is current-team mathematical/source review, not
external or human peer review. No author file was modified.

**Verdict: mathematical pass for the explicitly weighted theorem;
do not admit it as a standalone paper under this batch's substantive-novelty
threshold. Preserve it as a research note / attributed corollary.**

I found no fatal mathematical error in the claimed all-period weighted
formula, its Euler product, the stated analytic conclusions, or the
non-dynamically-affine example. Those conclusions do not settle ordinary
periodic-point counting. The exact weighting counterexample is essential.
The remaining author-owned argument is short after the two ramification
theorems are credited; correctness alone does not clear the paper gate.

## 1. Audited snapshot and methods

The four requested files were read in full, including the complete JSON:

| File in `../wild_dynamics/` | SHA-256 at review |
|---|---|
| PROOF_PACKAGE.md | `f2a4ffee200827f1cd8f09eb870ab9d8900d0b0a6c14062df9a1dfe522e27661` |
| SOURCE_AUDIT.md | `f2bfdaa0e4f3ed4240d73ee745f746324fb16da62de7aeca39d7e61aa6c96c84` |
| EXACT_RESULTS.json | `26894055c9e2011df5e16d3ac4eaa5e80ab1dfb0fd990e9a07363f60c58984c5` |
| BOUNDED_RECEIPTS.md | `2816bbe11fd00b30aedb87b95e44a507add0bbea9796e975480f8d1e38701f16` |

I also read `exact_probe.py`; checked the local theorem statements directly
in the primary originals below; rederived the convolution and pole residues;
and independently recomposed the p=3 degree-seven map through period two to
verify the displayed squarefree-factor counterexample. That independent
check passed. No census enlargement, GPU work or external model was used.

## 2. First-return weight and local growth: pass

For `f=xH^p`, differentiation and composition genuinely give
`f'=f/x` and `f^n-x=x(K_n-1)^p`. Every nonzero periodic orbit avoids zero
and the zeros of H, so f is étale there. Conjugating adjacent first-return
germs by the local inverse of f proves cycle constancy of the multiplicity.
Consequently `w(a)=ord_a(f^l-id)/p` is a positive integer, invariant along
the cycle. It is not a reduced-scheme count.

Writing `g(u)-u=(a+u)T(u)^p` with `T=c u^m+...` gives `i_0=mp-1`.
The numerator exponent `(m-1)p` in the second-residue calculation is
exactly `q-ell`, where `ell=p-1`. The coefficient of `u^-1` is
`-(ac)^(-p)`: the p-th-power tail cannot contribute before degree p, and
the coefficient of degree p-1 in `(a+u)^(-1)` is `a^(-p)` for odd p.
There is no missing contribution from higher coefficients of H.

The matching to the original local theorems is correct:

- For m=1, q=p-1 lies in the permitted interval 1 through p-1. The
  iterative residue is nonzero, so the small-multiplicity theorem applies.
  The primary paper's Definition 1, Section 1.2 and Theorem 2 were checked.
  [Nordqvist–Rivera-Letelier, primary original](https://arxiv.org/pdf/1904.04494).
- For m>=2, q=mp-1>p and p does not divide q. Definition 2.2 uses precisely
  the numerator `u^(q-ell)`, and Theorem A gives the sequence used in the
  package when this residue is nonzero. Both passages were checked directly.
  [Nordqvist, primary original](https://arxiv.org/pdf/1909.10782).
- At zero, i_0=p*m0 is divisible by p. The Sen identity is expressly
  recorded in both of those sources. The review does not claim to have read
  Sen's original paper. Iteration by a positive integer prime to p preserves
  the leading nonzero degree by the elementary germ-composition argument.

Thus equations (8)–(10) are supported over the declared arbitrary
algebraically closed field. Finite-order identity germs do not create an
exception: a positive iterate of a polynomial of degree d>1 cannot equal
the identity polynomial.

## 3. Global inversion and data: pass, only for the stated observable

Total affine intersection length is d^n. Removing the special origin term
and dividing by p yields exactly the convolution in equation (11).
For n=s*p^r, the triangular inversion `E_j=B_{s*p^j}-p*B_{s*p^(j-1)}`
is valid. Its telescope produces equation (1), including the constant -m0.
The primitive-cycle Euler product follows from positive integral cycle
weights; it is a dynamical product, not an arithmetic prime product.

The code obtains first-return factors through gcd removal of earlier
exact-period factors, independently of the W_n formula. Its reconstruction
and multiplicity checks are relevant. The nineteen bounded rows do not
justify universal absence of extra weights, and the package does not use
them that way.

I independently verified in characteristic three that, for
`f=x+x^4+x^7`, the stated factorization of `f^2-x` is exact, the factors
are squarefree and coprime, and the multiplicity-six quadratic factor is
coprime to `f-x`. It gives a genuine two-cycle of first-return weight two:
ordinary nonzero fixed count 13, weighted count 15. Retain this distinction
in any later summary. Removing the adjectives “first-return weighted” would
make the principal claim false.

## 4. Analytic claims: pass with the existing boundaries

Coefficientwise substitution yields equation (3). Its logarithmic
derivative (12) has normally convergent tails on compact sets of the unit
disk avoiding its locally finite pole set. At `a^(p^j)=1/d`, j>=1, the
residue of `L/t` is `(p-1)/p^(j+1)`; only one summand has a pole at that
modulus. At a=1/d the residue is -1/p. These nonintegral residues imply
genuine branch points of continuations of Z_w.

The first branch point fixes the Taylor radius at 1/d. Infinitely many
distinct branch points exclude algebraicity and a linear differential
equation over C(t). The accumulation of the poles of L at every point of
the unit circle prevents meromorphic extension across that circle.

The distinction in the package is correct: the unit circle is a natural
boundary of the **meromorphic continuation of L**, not a claim that Z_w is
holomorphic on the unit disk. No pole cancellation or unlicensed branch
normalization was found.

The analytic mechanism is established precedent, not a new technique.
The primary Byszewski–Cornelissen–Houben paper's tame/full definitions,
Theorem A and Proposition 2.1 were checked. Their ordinary/tame zeta
theorems concern different observables and cannot simply be invoked for
Z_w, but their p-primary decompositions and non-holonomicity framework
must remain credited. [Primary original](https://arxiv.org/pdf/1904.04942).

## 5. Non-dynamically-affine specialization: pass

Bridy's Definition 2.2, the five-family classification discussion, and the
G_m/G_a cases were checked in the original. The package uses that
classification as an input, not a new classification theorem.
[Bridy, primary original](https://arxiv.org/pdf/1306.5267).

For `f=x+x^(p+1)`, degree p+1 excludes additive/subadditive quotient maps,
whose degree is a p-power. At -1 the local degree is p; at infinity it is
p+1. This excludes power maps of degree p+1. The Chebyshev computation
correctly yields p distinct finite critical points in odd characteristic,
not the one finite critical point of f. Finally a separable elliptic
isogeny of degree p+1 has `(p+1)^n` preimages of each point; a finite fibre
over a totally invariant point of a Lattès quotient would contradict that
growth. The Lattès exclusion is valid. The p=2 Chebyshev exception is real.

This proves a genuinely non-affine underlying map. It does **not** turn
the weighted theorem into the ordinary-count result asked about in Bridy's
conjecture, nor prove that every H in the larger family is non-affine.

## 6. Standalone-paper gate: fail at the present substantive threshold

After subtracting the credited inputs, the author-owned package is:

1. One coefficient computation forcing the relevant residue to be nonzero.
2. A standard triangular divisor-convolution inversion of degree counts.
3. An explicit generating function and its straightforward pole analysis.
4. A useful small counterexample to confusing first-return weights with
   ordinary counting, plus an elementary exclusion using a known
   classification.

The full H-family and all-period scope are real strengths; I do not call
the theorem false or assert that its exact formula was already published.
However, those strengths currently produce a compact attributed corollary,
not a new general ramification result, ordinary periodic-orbit census,
classification of first-return weights, or new analytic method. In fact
the aggregate W_n depends only on d and m0; it deliberately bypasses the
hard distribution of weights among actual cycles. Non-affineness of f is
not, by itself, sufficient novelty for this changed observable.

Recommendation: retain one research note with the 13/15 example and all
source boundaries intact; assign no C-number and count no completed paper
from this package now. Do not obtain a paper count by splitting the local
residue, inversion and analytic corollaries into separate manuscripts.
Any later admission needs a genuinely additional theorem, such as a
nontrivial all-period classification of actual first-return weights or
ordinary counts; this is an example of a meaningful increment, not an
instruction to expand the current authorized task.

Final status: `MATH_PASS_WEIGHTED_ONLY / RESEARCH_NOTE_RECOMMENDED /
STANDALONE_ADMISSION_NOT_SUPPORTED`. The coordinator retains final
editorial authority, but a mathematical pass must not be recorded as an
independent-paper acceptance.
