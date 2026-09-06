# Independent review of the constant-Hénon canonical-height package

Review date: 2026-09-07. Reviewer: current-team agent
`/root/scout_henon_arithmetic`, not an author of the height proof. This is an
internal AI-assisted mathematical review, not journal peer review or a
worldwide-priority certificate. The coordinator retains admission ownership.

## Verdict and exact reviewed inputs

**Mathematics: PASS.** I found no counterexample, missing parameter case,
unjustified interchange, or pole cancellation in the complete eight-step
proof. The all-prime-power, all-degree, all-allowed-coefficient quantifiers
are supported by the argument, not merely by the reported finite tests.

**Substance: a coherent independent question is closed within the stated
polynomial-point domain.** The exact full distribution and aggregated pole
divisor/natural boundary are not supplied by the closest statements actually
read below. The canonical-height construction, escape mechanism, orbit
scaling, and generic rational-cone summation are classical inputs and should
remain deducted from novelty. I recommend the package for the coordinator's
bounded substantive-admission gate, with the two small source-provenance
corrections in Section 4 incorporated. This does not assign a C-number.

Inputs actually read in full:

- [HEIGHT_PROOF_PACKAGE.md](../spectral/HEIGHT_PROOF_PACKAGE.md), 379 lines;
  SHA256 `fc2fd3acdcbd1695997cecf02aaf6024e224fb89918777775ac95111a77d7ae7`.
- [HEIGHT_SOURCE_AUDIT.md](../spectral/HEIGHT_SOURCE_AUDIT.md), 101 lines;
  SHA256 `ee0f09dc3e49b61036c51dc8bf899db8bcfe74b480ab559719281ccd33418e81`.

These hashes identify the review baseline, not subsequent corrected versions.
No author input or frozen prior package was edited. I did not rerun the
author's 77,974-point check and do not claim independent reproduction of it.

## 1. Orbit exhaustion, heights, and uniform counts

The degree recursion only uses `deg f(y) = d deg y` when `deg y > 0` and
the nonvanishing of the leading coefficient and of `a`. It therefore works
in every characteristic, including inseparable `f` and characteristic
dividing `d`; no derivative or separability assumption is hidden.

Once two adjacent positive degrees are nondecreasing, the outward degrees
in that direction grow by exactly `d`. The reversed argument treats the
other direction. An indefinitely descending inward sequence is impossible
in the nonnegative integers. Two consecutive degree-zero coordinates would
put the entire orbit in the constant finite set. These observations exclude
additional valleys, nonconstant periodic orbits, and infinite tails missed
by the proposed representatives.

At a strict valley of degree `n`, unequal neighboring degrees have maximum
`dn`; their smaller neighbor gives exactly the open edge cone. Equal
neighboring degrees `M` instead satisfy `M >= dn` and give a turn. At a
positive plateau only the central adjacent pair can be the edge. The
displayed outward escape patterns prevent another representative of either
type. The turn orientation is essential: its reversed adjacent pair is an
iterate, but does not satisfy the turn's ordered degree condition.

I checked the normalization of both height limits. An edge has backward
and forward heights `(m,n)`. A turn has `(M,M/d)`, since the forward
geometric growth begins one step later. Consequently its two equal minimum
total heights occur at orbit indices `0,1`; this is not a double count of
representatives. Every nonconstant orbit is indexed injectively by all
integer shifts. Constant points contribute exactly `q^2` at height zero.

For `M=dk`, the strict turn portion contributes
`(q-1) q^((d+1)k)` and the equal-leading-degree portion contributes
`(q-1)(q-2) q^((d+1)k)`. Their sum is the stated
`(q-1)^2 q^((d+1)k)`. In particular, at `q=2` only the second portion
vanishes; no exceptional case has been divided out. When `M=dk+r`,
`1 <= r < d`, all `q^(k+1)` choices of the lower-degree coordinate are
admissible, giving the stated second formula. This establishes coefficient
uniformity without invoking a coefficient-blind computer experiment.

The orbit formulas also establish `h(P) <= hhat(P)` at every shift and
properness on `F_q[t]^2`. They do not imply a Northcott theorem over an
arbitrary constant field or on an enlarged rational-function domain.

## 2. Sector summation, continuation, and every pole

The closed tails removed from the positive quadrant in equation (2) are
disjoint for `d >= 2`. The open-cone parallelogram argument in equation (3)
is valid: write each positive cone coordinate uniquely as an integer
`>= 0` plus a number in `(0,1]`. The remainder is still an integer lattice
point and has positive coordinates. Thus equation (3) really removes the
spurious individual factors `1-A` and `1-B` away from cone poles.

For every compact set with `Re s >= epsilon > 0`, the finite numerator
in equation (3) has positive powers of the doubly-exponentially decaying
variable `B_k`; `A_k` remains bounded and both cone denominators tend to
one. The turn numerator has the analogous decay. This gives normal
convergence of the analytic tail, leaving only finitely many meromorphic
sectors locally. It justifies continuation and excludes unlisted poles.
For `Re s > 1` the same estimates and positive-sector convergence justify
the original sum. The central edge term gives divergence of the absolute
sum at every `Re s <= 1` through the exact coefficient
`b_j = j - 2 floor(j/(d+1)) - 1`.

For `k >= 2`, strictly distinct `L_k` ensure that only `C_(k-1)`, `C_k`,
and `E_k` meet the selected pole. Each has weight two in equation (5).
I independently combined their numerators. In the notation of the proof,

\[
\frac1{A-1}+\frac{A}{q/v-A}+1
=\frac{A(q-v)}{(A-1)(q-vA)},\qquad
\sum_{r=1}^{d-1}v^{-r}=\frac{q-v}{q(v-1)}.
\]

After these substitutions the remaining numerator is

\[
(q-1)A(v-1)+(A-1)(q-vA)=(q-A)(vA-1),
\]

which proves equation (8). Since
`q^(1-1/d) < |A| < q` for `k >= 2`, every factor asserted nonzero
really is nonzero, for every root-of-unity phase of `v`. The derivative of
`1-q^(d+1-s L_k)` at its zero is `L_k log q`, giving the residue sign
and scale in equation (9).

The `k=1` collision needs separate weight accounting. Set
`w=B_0(s_0)`. When `w != 1`, `C_0` has coefficient
`2(q-1)^2/(w-1)` because its two cone denominators coincide, even though
`C_0` itself has weight one. `C_1` and `E_1` each have weight two.
The total is therefore exactly `2R`, not `R` or `4R`. The only vanishing
denominator in (8) at this level is `q-vA`, and it vanishes precisely when
`w=1`, equivalently `(d+1) | ell`. At those points `C_0` has the stated
positive double-pole coefficient; both remaining sectors are at most
simple. Off those points the factored numerator cannot vanish. This closes
all small-`q`, small-`d`, and phase cases, including `d=q=2`.

As an auxiliary second check, agent `/root/scout_charp_c414` independently
read Steps 4–6 and returned the same algebra and `k=1` weight analysis.
That agent additionally reported two exact SymPy simplifications equal to
zero, exit 0. My verdict above rests on the displayed algebra and full
proof review; the auxiliary check covers only Step 6, not the entire proof.

Every point of the imaginary axis is approached by the genuine pole
lattices with distinct positive real parts. A meromorphic extension across
such a point would have an interior accumulation of poles. Thus the
natural-boundary argument is valid for meromorphic, not merely holomorphic,
continuation. It is a conclusion about the combined function, not about
unaggregated summands.

## 3. Counting asymptotic and its real-bound convention

The central edge sum gives the displayed leading term with
`alpha=(d-1)/(d+1)` and `N=floor(B)`. For the adjacent shifts, setting
`e=dn-m >= 1` gives height `(d+1)n-e/d` and weight proportional to
`q^((d+1)n-e)`. At each fixed `e`, summing over the height-bounded `n`
is at most a constant times `q^(B-(1-1/d)e)`. The remaining sum over
`e` is convergent, so these shifts contribute only `O(q^B)`.

For `|k| >= 2`, maximize
`(m+n)/(d^(-k)m+d^k n)` over the open cone. For `k>0` this ratio
increases with `m/n`, and its supremum occurs at `m/n=d`, giving
`(d+1)/L_k <= alpha_2 < 1`; negative indices follow by symmetry.
The first exterior turn shifts give the same `alpha_2`. Core degrees
are bounded by `B` and only `O(1+log(1+B))` indices contribute. The
polynomial/logarithmic number of terms is absorbed by the strict
exponential gap `1-alpha_2`. No unbounded multiplicity remains hidden in
the error estimate.

Replacing `N` by `B` only in the linear factor changes the answer by
`O(q^B)`, while the exponent retains `floor(B)+1`. Accordingly the
asymptotic is correct for arbitrary real `B`, not just integral subsequences.
Removing that floor from the exponential main term would be an invalid
strengthening. No Tauberian single-pole assumption is used.

## 4. Actual closest-source ownership and minor corrections

I independently opened the primary documents below, rather than accepting
the author's source table as evidence of their mathematical contents. My
reading was of the identified sections, not of every page or final version.

- Ingram's retrieved [arXiv PDF](https://arxiv.org/pdf/1111.3609v1):
  introduction, Section 2 definitions and Lemma 2.1's statement, including
  its initial nonarchimedean strict-domination calculation.
  This supports the classical forward/backward limits, scaling and escape
  formulas. Its local setup specifies monic `f`; the present direct degree
  proof handles arbitrary nonzero constant leading coefficient. The source
  does not supply this complete polynomial-point census or its pole divisor.
- Kawaguchi's [official journal PDF](https://msp.org/ant/2013/7-5/ant-v7-n5-p08-p.pdf):
  introduction, Theorem A, and the displayed Theorem B/Corollary D scopes.
  Theorem A supplies general nonarchimedean Green functions and scaling;
  the global result is formulated over number fields. Corollary D counts
  bounded-naive-height points in one fixed infinite orbit, not all polynomial
  points of all orbits. This is a genuine domain and observable distinction.
- Takehira's [arXiv v1 PDF](https://arxiv.org/pdf/2404.00955v1): introduction,
  Section 2.2, Condition 3.1 and its partition, Theorem 3.4, and the opening
  of Section 4. These are one-variable polynomial height-zeta results.
  The finite constant local-height-discrepancy partition used there cannot
  hold for this whole two-dimensional domain: at the edge `m=n`, the
  two-sided height is `2m` and the naive height is `m`. Takehira explicitly
  treats vertical-line poles as relevant to counting; retaining the present
  fractional-part oscillation is necessary. This does not independently
  verify his criticism of Hsia's original asymptotic, which I have not read.

The source-scope comparison is my inference from these actual statements.
The distribution theorem requires an all-orbit census absent from the
accessed local-height and fixed-orbit formulas. The combined residue and
the infinite family of surviving poles supply additional analytic work
beyond standard rational-cone summation. Thus the increment survives the
deduction of the classical tools. This is not a proof that no other source
contains it; Hsia's original article and final Ingram/Takehira versions
remain outside this review's actual text access.

Two corrections are requested in the source record before its release:

1. Takehira Section 2.2 attributes the height-zeta **definition** to
   Silverman's unpublished 1994 talk, via Hsia. Credit Hsia's published
   development, but do not state Hsia as the exclusive origin of the
   definition. The talk attribution is itself secondary evidence from
   Takehira, not an inspected talk or original Hsia text.
2. Distinguish arXiv labels/submission dates from manuscript-internal dates.
   The retrieved Ingram PDF bears `1111.3609v1 / 15 Nov 2011` in its arXiv
   header but `Date: August 21, 2017` in the article. The Takehira PDF bears
   `2404.00955v1 / 1 Apr 2024` but has internal date April 2, 2024. Record
   the observations without explaining away the discrepancy or claiming
   that a final published version has been inspected.

These are source precision fixes, not mathematical objections. The
coordinator was notified of both before this report was written.

## 5. Allowed conclusions and stopping point

The proof supports the stated fixed-domain coefficient-uniform height
distribution, exact abscissa, full simple/double pole divisor, meromorphic
natural boundary, and lattice-sensitive real-height asymptotic. It supports
one independent bounded research contract, subject to the coordinator's
source-corrected admission decision.

It does not support all rational-function points, nonconstant coefficients,
a periodic-orbit zeta identification, target Euler factors/root numbers,
automorphy, a Riemann-zero correspondence, or a Hilbert–Pólya realization.
No new GPU computation, external model/API review, or rerun of sealed
calculations is needed to settle the issues raised in this review.

Review dialogue summary: the initial request concerned proof quantifiers
and cancellation; full independent analysis found no blocker. The targeted
second review confirmed Step 6. The coordinator then requested closest-source
ownership, which was checked against primary texts and generated only the
two bounded source corrections above. Mathematical review is complete;
author source edits and formal admission remain with the coordinator.

## Source-fix confirmation — 2026-09-07

At the coordinator's request I reread only the affected primary-source
matrix rows. Both requested corrections are now accurately incorporated:
the definition's secondary Silverman attribution is separated from Hsia's
published development, and the Ingram/Takehira header dates are separated
from their manuscript-internal dates. Unaccessed original/final texts and
the unaccessed talk remain explicitly identified. The revised source audit
has SHA256
`32ded9aa931d95ccd5374b4df947b91c5b5a1a6efdd2495deab3883dfb9f13fc`.
The proof retains its original reviewed SHA256 stated above.

The source precision requests are closed. The mathematical PASS and bounded
substantive recommendation stand, with no new mathematics review or test
rerun. Formal admission and the five-contract batch gate remain the
coordinator's actions; this confirmation does not assert that five contracts
have been assembled or any manuscript has been written.
