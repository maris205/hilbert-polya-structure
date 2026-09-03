# Hostile Review B — Quartic Inverse-Span Dynamics

**Role:** independent nonauthor Review B; the literal map, proof chain,
source boundary, target fibres, and edge cases were cold-read before the
author control was replayed.  Two reviewer-owned implementations, both
distinct from the author and Review A engines, were then used for targeted
falsification.  
**Decision:** `ACCEPT_INTERNAL`.  
**Findings:** `0 Critical / 0 Major / 0 Minor`.  
**Theorem verdict:** `PROVABLE AS STATED`.  
**Lifecycle:** `GREEN_OWNER_THIN / HOLD_EXTERNAL`.

## Pinned Round-0 input

```text
866951e658c3dd54c944e14c9d94b5690fa974e566d83bc35847663658571b8b  main.tex
aa6a1ec380d5a24114e4c1ce896afd668f2abaeb2fcf65ec14f36dc5849805e3  references.bib
c3c40bfc0e92c19fe3a6fe6b7b924c7d0cb6f2a518f6478363701ae4bab1f6f1  verify_p168.py
8c0b77d99e976e9666ae658f4af7525ccf185f927948e660e3323a0f6f7f3d74  verification_output.txt
846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e  main.pdf
846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e  main_round0_original.pdf
```

The paper-local manifest passed in full before and after the review.  Review B
changes no manuscript, bibliography, author verifier, frozen transcript,
build product, or author ledger.  Its only paper-directory addition is this
report; reviewer controls are isolated under the batch review directory.

## Independent mathematical attack

### Rank growth, equality, and the external-classification boundary

If `dim(A)=d`, pointwise inversion supplies exactly `p^d-1` distinct nonzero
points to the output span.  An output of dimension `r` contains only
`p^r-1` nonzero points, so `r>=d`.  Equality forces the inverse set to be the
entire nonzero part of the output subspace.  Inverting that set once more and
taking its span gives `J^2(A)=A`.  Conversely, dimension is nondecreasing
along every orbit, so a periodic state must attain equality at its first
edge.  Thus equality, recurrence, and period at most two are linked without
an omitted finite-map converse.

The cited Kolomeec--Bykov theorem is invoked only after equality has made the
patched pointwise inverse an actual subspace.  Its `|A|>2` hypothesis covers
every plane, hyperplane, and the full field in this quartic carrier.  Binary
lines are the sole relevant size-two exception, and the manuscript evaluates
them directly.  Consequently the use of the external classification has no
hidden boundary case.

### Plane rank and the binary depth jump

After scaling a plane to `<1,alpha>`, its projective points have inverse
representatives

```text
1, (alpha-t)^(-1),  t in F_p.
```

For distinct `t_i`, multiplying a relation among `1` and the corresponding
reciprocals by `prod(x-t_i)` produces a polynomial of degree below
`r=[F_p(alpha):F_p]`.  Minimality makes that polynomial zero, and evaluation
at each `t_i` kills every coefficient.  Since `r` divides four and exceeds
one, it is two or four.  The span dimension is therefore `min(p+1,r)`:
scalar quadratic-subfield planes retain dimension two, a degree-four plane
has rank three only at `p=2`, and it fills the field at every odd prime.

For a hyperplane, equality at rank three would make its patched inverse a
subspace.  Kolomeec--Bykov would then make it a scalar subfield of degree
three, impossible inside a degree-four extension.  Every hyperplane
therefore maps to the full field.  These two arguments exhaust every carrier
dimension and prove the sharp tail two at `p=2` versus tail one at odd `p`;
`P-Q=pL>0` proves that both displayed maxima are attained.

### Recurrent core, cycles, and temporal formulas

The recurrent set is exactly zero, the full field, all scalar lines, and all
scalar copies of the quadratic subfield.  Gaussian counts independently give

```text
L=p^3+p^2+p+1,
P=(p^2+1)(p^2+p+1),
Q=p^2+1,
S=2+2L+P,
R=2+L+Q.
```

On lines and recurrent planes the map is inversion on cyclic quotients of
orders `L` and `Q`.  Inversion fixes `gcd(2,L)` and `gcd(2,Q)` quotient
classes, respectively.  Adding zero and the full field gives `F=4` in the
binary case and `F=6` at odd primes; every other recurrent point belongs to a
two-cycle.  The fixed-iterate sequence and zeta factorization then follow
with no possible longer cycle.  The depth enumerator and image stabilization
are the direct disjoint counts of the recurrent, hyperplane, and
non-subfield-plane strata.

### Every-target fibres and components

The twisted law `J(lambda A)=lambda^(-1)J(A)` is exact at the point-set level.
Nondegeneracy of the trace pairing parametrizes every hyperplane as
`H_c={x:Tr(cx)=0}`, and scalar multiplication is transitive on these kernels.
At `p=2`, the 30 non-subfield planes therefore distribute uniformly over the
15 hyperplanes, so each target has exactly two such predecessors.  Both
reviewer controls reconstruct the 15 individual fibres rather than checking
only the quotient `30/15`.

Rank growth excludes incoming edges to a transient plane.  The complete rank
transition table excludes every transient predecessor of a non-full
recurrent target and, at odd primes, every hyperplane target.  The recurrent
restriction is an involutive bijection.  These facts leave precisely the
cases printed in the all-time fibre display:

- one predecessor for every non-full recurrent target;
- at binary time one, two predecessors for each hyperplane and `1+L` for the
  full field;
- at binary times at least two, `1+L+P-Q` for the full field and zero for all
  transient targets;
- at every positive odd-prime time, `1+L+P-Q` for the full field and zero for
  all transient targets.

Thus every transient vertex belongs to the full-field component, all other
recurrent components are bare, and the component count `(R+F)/2` is correct.

### Boundary checklist

The cold proof attack separately covered `A=0`, `A=K`, scalar lines,
the binary size-two line exception, scalar and non-subfield planes,
hyperplanes, `p=2`, the smallest odd prime, time one versus stabilized later
times, targets outside the image, fixed versus two-cycle recurrent states,
and the cyclic-quotient wrap.  The theorem intentionally starts its fibre
atlas at `t>=1`; its separate `t=0` image statement is consistent.  No
missing carrier stratum, overlapping fibre case, false period divisor, or
unstated predecessor was found.

## Independent exact controls

### Author-control double replay

Two fresh standard-library processes reran the unchanged paper-local
verifier.  Both outputs matched one another and the 827-byte frozen
`verification_output.txt` exactly:

```text
assertions: 32,754
verifier SHA-256:  c3c40bfc0e92c19fe3a6fe6b7b924c7d0cb6f2a518f6478363701ae4bab1f6f1
transcript SHA-256: 8c0b77d99e976e9666ae658f4af7525ccf185f927948e660e3323a0f6f7f3d74
decision: AUTHOR_ROUND0_PASS
```

### B1: primitive-companion/projective-point control

The first B-side implementation is retained at
`docs/papers167_171_sequence/reviews/p168_b/`.  It imports no author,
scouting, or Review-A code.  Field multiplication is reconstructed from a
primitive companion orbit and exponent table; subspaces are projective-point
sets; planes come from projective joins; and hyperplanes come independently
from trace kernels.  It rebuilds complete graphs for `p=2,3,5,7`, checks
every target fibre through time six and fixed iterates through time eight,
then checks every normalized degree-two/four plane parameter at `p=11`.

Two fresh Review-B processes matched the frozen canonical transcript byte
for byte:

```text
assertions: 1,493,371
verifier SHA-256:  922c91cd813bbf7eb786cf2f10ffffd18470129e3bf7d74309e2553959ab5ea4
canonical SHA-256: 6f690b57e7d500de5f92b65d268f90cec25f870285808689451d441e96440ddc
decision: REVIEW_B_INDEPENDENT_CONTROL_PASS
```

The extra full graph at `p=7` has 3,652 states, recurrent count 452, fixed
count 6, depth census `452,3200`, and full-field fibres `3201` at times one
through six.  The `p=11` sweep checks all 14,630 normalized nonbase-field
values of `alpha`, separating 110 quadratic cases from 14,520 degree-four
cases with the predicted inverse-span ranks.

### B2: coordinate-incidence join/kernel control

A second independently written control is retained at
`docs/papers167_171_sequence/reviews/p168_b_incidence/`.  Unlike B1, field
elements are normalized coordinate tuples in different quotient models;
hyperplanes are kernels of ordinary coordinate functionals; trace kernels
are reconstructed only afterward as an independent equality check.  States
are never represented by RREF bases and are not discovered by BFS.  The
engine builds the complete incidence carrier and graph for `p=2` and `p=5`,
checks all target fibres through time six, all 15 binary two-predecessor
fibres individually, trace/scalar transitivity, recurrent scalar-subfield
classification, and components.  It also sweeps the closed count identities
over all 25 primes through 97.

Two fresh processes again matched the canonical transcript exactly:

```text
assertions: 73,983
verifier SHA-256:  440c4f33a22962fc0ab686360ca2b91ccd58ef265bfe243ae233127615061a4e
canonical SHA-256: 640b7a1ff476d694e466a05f5cc1f63d0c02bb88e3f37831856a9a552d311a61
decision: HOSTILE_REVIEW_B_TARGETED_PASS
```

B1 and B2 use different field models, projective labels, hyperplane
construction routes, and state canonicalizations.  Their edge hashes are
therefore not expected to coincide, but their invariant graph profiles and
target-resolved fibres do.  Together they contribute 1,567,354 reviewer
assertions beyond the author and Review-A controls.  These bounded programs
are falsification evidence; the all-prime verdict rests on the derivation
above.

## Primary-source and ownership attack

The direct owner statements were reopened rather than inferred from the
bibliography.

- Kolomeec--Bykov, arXiv `2206.14980`, Theorem 2, states exactly that for
  patched inversion and an affine `F_p`-subspace of size greater than two,
  affine image occurs exactly for a nonzero scalar copy of a subfield.  This
  matches Proposition 3 and its hypotheses.
- Lavrauw--Zanella, arXiv `1311.4309`, Theorem 5, identifies the inverse of a
  projective line with the image of an `(m-1)`-uple embedding where `m` is the
  generated extension degree.  Its small-field discussion explicitly gives
  independent `(q+1)`-tuples.  This supports the manuscript's zero-credit
  inverse-line ceiling; the manuscript also supplies its own short rank
  calculation.
- DOI content negotiation independently matched all six cited records.  The
  Kolomeec--Bykov and Lavrauw--Zanella years in the bibliography are their
  print-volume years (2024 and 2014), while their primary records also expose
  the 2023 online-first dates.  The remaining authors, titles, venues,
  volumes, issues, pages, and DOI strings agree with the frozen ledger.

The bounded literal search also reopened Mattarei's closely adjacent
`1311.3644` and `1312.1293`.  They concern sizes and geometry of intersections
`A^{-1} cap B`, including three-dimensional cases, but do not state the
quartic span-of-inverses iterate, its functional graph, sharp tail, image
stabilization, or every-target fibre atlas.  They therefore create no hidden
direct-owner collision and do not change the existing zero-credit boundary.
No inspected primary source owned the residual conjunction.

This is only a bounded owner check.  It supplies no novelty, priority,
freedom-to-operate, or external-release conclusion.  The manuscript's
`HOLD_EXTERNAL` status remains necessary.

## Double cold build and PDF audit

Two fresh Review-B directories began with only `main.tex` and
`references.bib`.  Each ran `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
Both settled logs have zero actual warnings, bad boxes, unresolved citations
or references, rerun requests, or fatal errors.  Both PDFs are byte-identical
to one another, the live canonical, and the preserved Round-0 copy:

```text
cold build 1: 846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e
cold build 2: 846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e
live main.pdf: 846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e
Round-0 copy:  846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e
```

The artifact has five A4 pages and 322,829 bytes.  All 23 font rows are
embedded, subsetted, and Unicode mapped.  Standard title, subject, keywords,
author, creator, and producer metadata fields are blank; the file is
unencrypted and has no form or JavaScript.  Extracted text has no email,
filesystem path, affiliation, acknowledgment, unresolved marker, or visible
nonauthor identity.

All five pages were independently rendered at 144 dpi and inspected.  The
theorem transition table, long fibre display, denominator-clearing proof,
trace-fibre argument, control table, lifecycle line, and bibliography are
legible.  A bounding-box scan found all 2,918 text boxes within the A4 page
rectangle.  No clipping, collision, overflow, malformed glyph, broken link
text, orphaned heading, or unreadable cell was found.  The visible byline and
running heads remain anonymous.

## Findings

### Critical

None.

### Major

None.

### Minor

None.

## Recommendation

Accept P168 Round 0 internally without source repair.  Preserve the explicit
zero-credit assignment to the patched-inverse classification and
inverse-line geometry, and preserve `GREEN_OWNER_THIN / HOLD_EXTERNAL`.
Neither this review nor its bounded source non-hit authorizes posting or
submission.
