# Hostile Review A — Random-Permutation Fixed-Point Sieve

**Role:** independent theorem, source, boundary, executable, and PDF attack on
the immutable author Round-0 package.  
**Decision:** `ACCEPT_INTERNAL`.  
**Findings:** `0 Critical / 0 Major / 0 Minor`.  
**Theorem verdict:** `PROVABLE AS STATED`.  
**Lifecycle:** `HOLD_EXTERNAL`.

## Pinned Round-0 input

```text
5ca548eeecf686c16599bebe85b2e18c94f93ada2d577b6e8f5771b390711e74  main.tex
2ce60b1638579e340e5e77eb970603f29e050b207c4ede1649cf38ad475cd839  references.bib
b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034  main.pdf
b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034  main_round0_original.pdf
2a9b9167d0ba8cf36dcf76cd93e6f58f5c2bb0002f21bd2a8c6d25d13427aed8  verify_p170.py
985941e0a8b363fcf954d503cf825867e54548dd8fcf416ee105a4cbbac2ba13  verification_output.txt
```

The review reconstructed the unmarked and marked laws from the literal
independent-permutation process before reading the frozen transcript.  The
re-entry gate is selection evidence and is not counted as a manuscript
review.

## Independent mathematical attack

### Pathwise reduction and every endpoint

Because each update is an intersection, a length-`t` history satisfies

```text
A_t = A intersect Fix(pi_1) intersect ... intersect Fix(pi_t).
```

For a prescribed `B subseteq A`, every point of `B` must be fixed at every
epoch and every point of `D=A\B` must fail to be fixed at least once.  If a
chosen `j`-subset of `D` is additionally forced to survive, each epoch has
exactly `(n-b-j)!` permutations.  Inclusion--exclusion therefore gives

```text
K_t(A,B)=sum_(j=0)^d (-1)^j C(d,j)(n-b-j)!^t.
```

For `t=0`, the alternating sum is the Kronecker delta.  A noncontained target
is impossible pathwise.  At positive time, a full source cannot lose exactly
one label because fixing `n-1` labels forces the last one.  This is the only
obstruction: derange `D` when `d>=2`; when `d=1` transpose the lost point
with a label outside `A`; when `d=0` use the identity.  Identities at all
remaining epochs preserve the realized endpoint.  Thus the printed support
criterion is necessary and sufficient, including the delicate one-lost-
label case.

### Containment spectrum and absorption

For `phi_S(A)=1[S subseteq A]`, survival of `S` requires both `S subseteq A`
and pointwise fixation of `S`, an event realized by `(n-|S|)!` permutations.
Thus the transition operator has eigenvalue
`lambda_|S|=(n-|S|)!/n!` on `phi_S`.  The matrix of these functions is the
Boolean zeta matrix and has the displayed Möbius inverse, so they form a full
`2^n`-element basis.  The factorial sequence is strictly decreasing except
for `1!=0!`; hence `lambda_(n-1)=lambda_n` is the sole cross-rank collision
(also correctly covering `n=1`).

Setting `B` empty in the endpoint formula and dividing by `(n!)^t` proves
the absorption CDF.  Removing the `j=0` term gives the survival tail.  For
`n>=2`, every nonconstant eigenvalue has modulus below one, and the standard
integer-tail identities

```text
E[T]   = sum_(t>=0) P(T>t),
E[T^2] = sum_(t>=0) (2t+1)P(T>t)
```

give the printed first two moments term by term.  The same tail identity
gives the probability generating function on `|s|<n`; its displayed finite
rational expression is its continuation.

The low-dimensional split is correct.  At `n=1` the nonempty state is
immortal.  At `n=2`, the equal rank-one/rank-two scales combine to `2^-t`
for every nonempty source.  At `n=3`, the rank-two and rank-three terms both
use `1/6`, producing

```text
a 3^-t - (C(a,2)-C(a,3))6^-t.
```

Only at `n>=4` are `lambda_1>lambda_2>lambda_3`, so the stated two-distinct-
scale expansion and `O(lambda_3^t)` remainder begin at exactly the claimed
boundary.  The re-entry repair is therefore present and mathematically
complete.

### Cycle-marked endpoint histories

If `s` specified labels are fixed, they contribute `u^s` singleton-cycle
weight.  The remaining `n-s` labels form an arbitrary permutation, whose
ordinary cycle enumerator is the rising factorial.  Hence

```text
R_(n,s)(u)=u^s product_(q=0)^(n-s-1)(u+q).
```

Applying the same inclusion--exclusion before discarding the cycle mark gives

```text
M_t(A,B;u)=sum_(j=0)^d (-1)^j C(d,j)R_(n,b+j)(u)^t.
```

This counts every labelled history exactly once.  Nonnegativity follows from
the literal history definition rather than from the alternating expression,
and `R_(n,s)(1)=(n-s)!` recovers the unmarked kernel.

Every epoch fixes the `b` endpoint labels.  If `b<n`, its complement contains
at least one permutation cycle, so the total cycle count is at least
`t(b+1)`; when `b=n` it is exactly `tn`.  A single cycle on the complement at
every epoch attains this minimum.  If that complement is a singleton, the
support criterion forces `A=B`, so the identity is the required witness.

For the maximum, put `delta(pi)=n-cyc(pi)`.  Each nontrivial `ell`-cycle moves
`ell` labels and contributes `ell-1` to the deficit, giving
`|supp(pi)|<=2 delta(pi)`.  Every one of the `d` lost labels appears in the
union of moved supports, hence the total deficit is at least `ceil(d/2)` and
the cycle count is at most `tn-ceil(d/2)`.  Equality is achieved by
transposition pairs when `d` is even, one 3-cycle plus transposition pairs
when odd `d>=3`, an outside-helper transposition when `d=1`, and identities
when `d=0`.  These constructions fix `B`, remove every lost label, and use
identities at other epochs.  Both marked-degree endpoints are therefore
sharp for every supported endpoint.

Finally,

```text
R'_(n,s)(1)/R_(n,s)(1) = s + H_(n-s).
```

Differentiating the exact marked polynomial, multiplying by the power-rule
factor `t`, and dividing by its positive value at one yields precisely the
conditional expectation in the theorem.  All histories have equal
probability before conditioning, so the logarithmic derivative is the
claimed uniform conditional mean.

## Boundary and counterexample pressure

The cold proof attack separately tested the zero-time Kronecker delta,
noncontained targets, empty source, full source, the impossible
`n-1` endpoint, `d=0`, even `d`, odd `d>=3`, `d=1`, `b=n-1`, `b=n`, and
`n=1,2,3,4`.  None requires a theorem restriction beyond those already
printed.  In particular, no asymptotic remainder hides the `n=3` eigenvalue
collision, and no marked sharpness witness silently assumes an unused label
when the support criterion does not provide one.

## Exact-control replay

A fresh standard-library process reran the unchanged author verifier and
matched the frozen 501-byte transcript exactly:

```text
assertions: 481,935
payload SHA-256:    e8f7f38c9e8bf14c2a35aba8b3eb9280127ec71374253056927290a65a5cdb8e
verifier SHA-256:   2a9b9167d0ba8cf36dcf76cd93e6f58f5c2bb0002f21bd2a8c6d25d13427aed8
transcript SHA-256: 985941e0a8b363fcf954d503cf825867e54548dd8fcf416ee105a4cbbac2ba13
decision: AUTHOR_ROUND0_PASS
```

The program enumerates literal permutation histories through `n=7`, marked
histories through `n=6`, checks uniform size formulas through `n=18`, and
constructs all parity-split sharp witnesses through `n=64`.  It also solves a
size-projected absorbing chain over exact rationals.  This is finite
falsification evidence, not the proof.  Review B must additionally use a
separately implemented carrier.

## Source, ownership, build, and PDF audit

The Hanany--Puder and Diaconis--Evans--Graham records justify treating common
fixed-point and fixed-set laws as background.  Brown and
Ayyer--Schilling--Steinberg--Thiéry own generic semigroup/semilattice spectral
machinery, while Cameron--Semeraro supplies the ordinary permutation-group
cycle-polynomial context.  The paper assigns all these ingredients, ordinary
inclusion--exclusion, and standard absorption transforms zero contribution
credit.  Its bounded non-hit for the complete endpoint-conditioned marked
conjunction is not presented as novelty, priority, or clearance.

Two new review-side source-only directories, each initially containing only
`main.tex` and `references.bib`, produced the same SHA-256
`b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034`.
Both match the canonical and preserved Round-0 PDFs byte for byte, and their
settled logs have zero genuine diagnostic.

All four A4 pages were independently rendered at 144 dpi and inspected.  The
theorem split across pages 1--2, absorption formulas, marked conditional
expectation, support-deficit proof, bibliography, headers, and page numbers
are legible and inside the page box.  All 23 font rows are embedded,
subsetted, and Unicode mapped.  Identifying metadata fields are blank; there
is no encryption, form, or JavaScript; the visible byline is anonymous; and
the hold status is explicit.

## Findings

### Critical

None.

### Major

None.

### Minor

None.

## Recommendation

Accept every formula without repair or weakening.  Preserve the Round-0
source and PDF, obtain the required independent Review B, and then freeze
byte-identical Round-1/Round-2 artifacts if no later finding arises.  The
package remains intentionally owner-thin, and this decision grants no
posting, circulation, contact, or submission permission.  External status
remains `HOLD_EXTERNAL`.
