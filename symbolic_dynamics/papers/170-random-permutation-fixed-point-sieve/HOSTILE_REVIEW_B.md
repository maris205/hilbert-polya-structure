# Hostile Review B — Random-Permutation Fixed-Point Sieve

**Role:** nonauthor independent Review B of the frozen Round-0 source and
artifact; the literal map, all endpoint and absorption laws, and the complete
cycle-marked statement were rederived before either executable transcript was
consulted.  
**Decision:** `ACCEPT_INTERNAL`.  
**Findings:** `0 Critical / 0 Major / 0 Minor`.  
**Theorem verdict:** `PROVABLE AS STATED`.  
**Lifecycle:** `HOLD_EXTERNAL`.

## Pinned input

```text
5ca548eeecf686c16599bebe85b2e18c94f93ada2d577b6e8f5771b390711e74  main.tex
2ce60b1638579e340e5e77eb970603f29e050b207c4ede1649cf38ad475cd839  references.bib
b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034  main.pdf
b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034  main_round0_original.pdf
2a9b9167d0ba8cf36dcf76cd93e6f58f5c2bb0002f21bd2a8c6d25d13427aed8  verify_p170.py
985941e0a8b363fcf954d503cf825867e54548dd8fcf416ee105a4cbbac2ba13  verification_output.txt
```

The later convenience copy `main_round1.pdf` is also byte-identical at
`b900ad...2034`; it does not change the pinned source or Round-0 artifact.
The frozen author manifest passes in full.

## Independent mathematical attack

### Literal endpoint kernel and exact support

Iteration of the map gives the pathwise identity

```text
A_t = A intersect Fix(pi_1) intersect ... intersect Fix(pi_t).
```

Fix `B subseteq A`, write `b=|B|` and `d=|A\B|`, and force every label of
`B` to be fixed at every epoch.  Every label of `A\B` must instead be moved
at least once.  If a chosen `j`-subset of those lost labels is also forced to
remain fixed, each epoch has `(n-b-j)!` choices.  Inclusion--exclusion on the
lost labels therefore gives, including time zero,

```text
K_t(A,B) = sum_(j=0)^d (-1)^j C(d,j)(n-b-j)!^t.
```

The time-zero alternating sum is exactly the Kronecker delta, while a
noncontained target is impossible pathwise.  At positive time, fixing
`n-1` labels forces the last label, so `A=[n]` cannot reach a target of size
`n-1`.  This is the only missing edge.  For `d>=2`, derange the lost set at
one epoch; for `d=1`, the support condition supplies a helper outside `A`
and a transposition with that helper loses the desired label; for `d=0`, use
the identity.  Identities in all other epochs preserve the endpoint.  Thus
both necessity and sufficiency, including the empty source, full source,
one-lost-label boundary, and `t=0`, agree with the theorem.

### Containment eigenbasis and absorption transforms

For `phi_S(A)=1[S subseteq A]`, survival of `S` through one update requires
`S subseteq A` and pointwise fixation of all `|S|` labels.  Hence

```text
P phi_S = ((n-|S|)!/n!) phi_S.
```

The `2^n` containment functions form the Boolean zeta matrix, whose inverse
is Boolean Möbius inversion.  They are therefore a full eigenbasis, not only
a collection of eigenfunctions.  The factorial sequence is strictly
decreasing except at `1!=0!`; consequently the sole collision between
different ranks is `lambda_(n-1)=lambda_n`, also correctly covering `n=1`.

Putting `B` empty in the endpoint kernel and dividing by `(n!)^t` proves the
printed absorption CDF.  Removing its `j=0` term gives the survival tail.
For `n>=2`, termwise use of

```text
E[T]   = sum_(t>=0) P(T>t),
E[T^2] = sum_(t>=0) (2t+1)P(T>t)
```

gives the displayed first and second moments.  Likewise

```text
E[s^T] = 1-(1-s)sum_(t>=0) s^t P(T>t)
```

gives the PGF for `|s|<lambda_1^(-1)=n`, followed by the stated rational
continuation.  No interchange occurs outside the claimed convergence disk.

The low-dimensional cases are separated at the necessary boundaries.  At
`n=1` the nonempty state is immortal.  At `n=2`, the rank-one and rank-two
scales both equal `1/2`, and their coefficients combine to `2^-t` for every
nonempty source.  At `n=3`, `lambda_2=lambda_3=1/6`, giving exactly

```text
a 3^-t - (C(a,2)-C(a,3))6^-t.
```

Only for `n>=4` are `lambda_1>lambda_2>lambda_3`; all remaining finitely
many scales are then bounded by `lambda_3`, proving the two-scale expansion
with the stated `O(lambda_3^t)` remainder.  The `n=4` terminal collision
`lambda_3=lambda_4` is harmless because both terms lie in that remainder.

### Cycle-marked polynomial and both sharp degrees

If `s` prescribed labels are fixed, their singleton cycles contribute
`u^s`; the remaining `n-s` labels contribute the ordinary symmetric-group
cycle enumerator.  Thus

```text
R_(n,s)(u) = u^s product_(q=0)^(n-s-1)(u+q).
```

Applying the endpoint inclusion--exclusion before forgetting cycle weight,
and using independence across epochs, proves

```text
M_t(A,B;u) = sum_(j=0)^d (-1)^j C(d,j)R_(n,b+j)(u)^t.
```

The literal history definition proves coefficientwise nonnegativity despite
the alternating closed form, and evaluation at `u=1` recovers `K_t`.

For the lowest degree, every epoch has the `b` fixed singleton cycles of
`B`; if `b<n`, the complement supplies at least one more cycle.  Hence the
minimum is `t(b+1)` when `b<n` and `tn` when `b=n`.  A single cycle on the
complement at each epoch realizes the former.  If the complement is a
singleton, support forces `A=B`, and the identity is exactly that witness.

For the highest degree, put `delta(pi)=n-cyc(pi)`.  A nontrivial `ell`-cycle
moves `ell` labels and contributes `ell-1` to the deficit, so
`|supp(pi)|<=2 delta(pi)`.  Every one of the `d` lost labels occurs in the
union of the moved supports over all epochs.  Therefore total deficit is at
least `ceil(d/2)`, and the total cycle count is at most
`tn-ceil(d/2)`.  Equality is realized separately in every required class:
identities for `d=0`; disjoint transposition pairs for even `d`; one
3-cycle and the remaining transposition pairs for odd `d>=3`; and, for
`d=1`, one transposition with a helper outside `A` guaranteed by endpoint
support.  The remaining epochs are identities.  Each witness fixes `B` and
moves every lost label, so both degree endpoints are genuinely attained.

Finally,

```text
R'_(n,s)(1)/R_(n,s)(1) = s + H_(n-s).
```

Differentiating the exact marked formula, using the power rule and
`R_(n,s)(1)=(n-s)!`, and dividing by the positive supported value
`M_t(A,B;1)=K_t(A,B)` gives the printed conditional expectation.  All
length-`t` permutation histories have the same probability `(n!)^-t`, so
this logarithmic derivative is exactly the uniform conditional mean.

No support leak, repeated-eigenvalue error, low-dimensional asymptotic leak,
negative marked coefficient, degree-endpoint gap, parity exception, missing
helper, or conditioning-denominator problem was found.

## Exact-control attacks

### Reviewer-owned independent control

Review B supplies `docs/papers167_171_sequence/reviews/p170_b/verify_review_b.py`
and its frozen transcript.  It imports no author, scouting, or Review-A
module.  Its representation is deliberately different from the author
program: labelled states are `frozenset` objects rather than bit masks;
polynomials are sparse degree/coefficient maps rather than dense tuples; and
it never constructs literal permutation tuples.  Instead it builds the
one-epoch exact-fixed-set cycle inventories from the recurrence obtained by
placing the smallest active label in a nontrivial cycle,

```text
D_m(u) = u sum_(ell=2)^m C(m-1,ell-1)(ell-1)! D_(m-ell)(u).
```

It then propagates the independently constructed marked transition atoms.
Two fresh processes matched each other and `CANONICAL.txt` byte for byte:

```text
assertions:          3,001,398
verifier SHA-256:    bf1245ae0068decddea02e43bd72ec2cb351af8aec9687435490a0ab4cb8c144
canonical SHA-256:   c8b8402f3421685562d1a02cd80e425053eeeeb9762bb98adadbb18b2ff40e6b
dynamic payload:     d0b0adab36ebf96669ae1a49a76d8c32c46cae519f1d6b6449b87c1db9d80a9e
decision:            REVIEW_B_INDEPENDENT_CONTROL_PASS
author/Review-A imports: 0
```

The independent control covers every labelled source-target pair through
`n=8` and times `0..4`; full Boolean containment/Möbius bases through `n=9`;
full labelled absorption recursions, moments, and three exact-rational PGF
evaluations through `n=9`; derangement-cycle inventories through `n=32`;
uniform marked endpoints through `n=32` and times `1..5`; the `n=1,2,3`
boundaries through time 24; the exact two-scale envelope for `4<=n<=40`;
and every supported size pair through `n=100`.  The last axis constructs
176,750 cycle-block witnesses and separately covers `d=0`, `d=1`, positive
even `d`, and odd `d>=3`.

### Author control replay

One fresh process reran the unchanged paper-local verifier.  Its 501-byte
stdout matched `verification_output.txt` exactly:

```text
assertions:          481,935
payload SHA-256:     e8f7f38c9e8bf14c2a35aba8b3eb9280127ec71374253056927290a65a5cdb8e
verifier SHA-256:    2a9b9167d0ba8cf36dcf76cd93e6f58f5c2bb0002f21bd2a8c6d25d13427aed8
transcript SHA-256:  985941e0a8b363fcf954d503cf825867e54548dd8fcf416ee105a4cbbac2ba13
decision:            AUTHOR_ROUND0_PASS
```

These computations are finite hostile falsification evidence; the
all-parameter verdict rests on the independent derivations above.

## Primary-source and ownership audit

The five retained records were checked again against primary publisher or
author-posted surfaces.  Oxford Academic confirms Hanany--Puder,
*International Mathematics Research Notices* 2023(11), 9221--9297,
DOI `10.1093/imrn/rnac084`; ScienceDirect confirms
Diaconis--Evans--Graham, *Advances in Applied Mathematics* 61 (2014),
102--124, DOI `10.1016/j.aam.2014.05.006`; Springer confirms Brown,
*Journal of Theoretical Probability* 13, 871--938 (2000), DOI
`10.1023/A:1007822931408`; the primary arXiv record `1401.4250` confirms
the Ayyer--Schilling--Steinberg--Thiéry article and DOI
`10.1142/S0218196715400081`; and the Electronic Journal of Combinatorics
record confirms Cameron--Semeraro 25(1), P1.14 (2018), DOI
`10.37236/7299`.  Titles, authors, venues, dates, pagination, and identifiers
match `references.bib` and the rendered bibliography.  All five entries are
cited, and no placeholder source remains.

The subtraction boundary is strong and visible.  Common fixed-point and
fixed-set laws, inclusion--exclusion, generic semigroup/semilattice spectral
machinery, Boolean Möbius inversion, standard absorption transforms, and the
ordinary permutation-group cycle polynomial all receive zero contribution
credit.  The internal P158/P162 “random intersection plus absorption” shape
is also subtracted.  The bounded owner non-hit for the complete
endpoint-conditioned marked conjunction is not used as priority, clearance,
or release evidence.  This review supplies no ownership certificate.

## Source-only build, PDF, anonymity, and lifecycle audit

Two new Review-B directories began with only `main.tex` and
`references.bib`.  In each, the sequence `pdflatex`, `bibtex`, `pdflatex`,
`pdflatex` reproduced the frozen PDF byte for byte:

```text
cold build 1:   b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034
cold build 2:   b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034
live main.pdf:  b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034
```

Both settled logs have zero actual warnings, bad boxes, unresolved
citations/references, rerun requests, or errors.  The author `SHA256SUMS`
replay passes every listed entry.  The canonical PDF, preserved Round-0
copy, and post-review Round-1 convenience copy are mutually byte-identical.

The PDF has four A4 pages and 277,277 bytes.  All four pages were rendered
at 144 dpi and independently inspected: the theorem continuation, absorption
formulas, marked polynomial, conditional-mean fraction, support-deficit
argument, references, running heads, and page numbers are legible and inside
the page box.  No clipping, collision, malformed glyph, stranded heading, or
blank page was found.  All 23 font rows are embedded, subsetted, and Unicode
mapped.  The file is unencrypted and has no form, JavaScript, attachment,
custom metadata, or metadata stream.  Title, subject, keywords, author,
creator, and producer metadata fields are blank; the visible byline and
running heads are anonymous.  Extracted text has no email, affiliation,
filesystem path, unresolved token, TODO, or review verdict.  The external
hold appears in the abstract, body, and package ledgers.

## Findings

### Critical

None.

### Major

None.

### Minor

None.

## Recommendation

Accept the theorem package without repair, weakening, or source/PDF change.
The frozen input, two independent exact controls, cold builds, and artifact
audits agree.  External status remains `HOLD_EXTERNAL`; this review grants no
posting, circulation, contact, or submission permission.
