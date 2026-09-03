# Hostile Review A — Quartic Inverse-Span Dynamics

**Role:** coordinator-side independent Review A.  
**Frozen input:** anonymous author Round 0.  
**Decision:** `ACCEPT_INTERNAL`.  
**Findings:** `0 Critical / 0 Major / 0 Minor`.  
**Lifecycle:** `GREEN_OWNER_THIN / HOLD_EXTERNAL`.

## Pinned artifact

```text
866951e658c3dd54c944e14c9d94b5690fa974e566d83bc35847663658571b8b  main.tex
aa6a1ec380d5a24114e4c1ce896afd668f2abaeb2fcf65ec14f36dc5849805e3  references.bib
c3c40bfc0e92c19fe3a6fe6b7b924c7d0cb6f2a518f6478363701ae4bab1f6f1  verify_p168.py
8c0b77d99e976e9666ae658f4af7525ccf185f927948e660e3323a0f6f7f3d74  verification_output.txt
846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e  main_round0_original.pdf
```

The pinned Round-0 PDF and `main.pdf` are byte-identical.  This review adds
only this report and requests no source change.

## Independent proof attack

The literal map is the span of the pointwise inverses, with zero handled
separately.  The main structural steps survive rederivation.

- Inversion preserves the number of nonzero points.  Therefore the inverse
  span cannot have smaller dimension.  Equality forces the inverse set to
  fill the nonzero part of the image subspace and immediately gives
  `J^2(A)=A`; monotone dimension then makes equality equivalent to
  recurrence.
- The cited Kolomeec--Bykov classification is used at exactly the equality
  case and is openly declared a zero-credit theorem input.  Together with
  direct treatment of lines, it leaves precisely zero, the full field,
  lines, and scalar quadratic subfields recurrent.
- For a plane scaled to `<1,alpha>`, the inverse projective representatives
  are `1` and `(alpha-t)^(-1)`.  Denominator clearing shows that any at most
  `r=[F_p(alpha):F_p]` of these representatives are independent.  Since
  `r` is two or four, the image rank is `min(p+1,r)`.  This produces rank
  three only when `p=2` and `r=4`; the odd-prime plane goes directly to the
  full field.
- A hyperplane cannot retain rank three: equality would make its patched
  inverse a subspace, contradicting the cited scalar-subfield
  classification because three does not divide four.  Hence every
  hyperplane maps to the full field.
- Gaussian counts give the stated state strata.  On scalar lines and scalar
  quadratic subfields, the update is inversion on cyclic quotients of
  orders `L` and `Q`; this verifies the fixed counts, two-cycles,
  fixed-iterate counts, zeta function, and component count.
- Twisted scalar equivariance maps a fibre over one hyperplane bijectively
  to a fibre over any other.  Trace-pairing parametrization makes the scalar
  action transitive.  At `p=2`, the 30 transient planes therefore split
  uniformly over 15 hyperplanes, exactly two each.
- Rank monotonicity and the complete stratum transition table exclude every
  other predecessor.  This yields the displayed fibre for every target and
  every positive time, not just aggregate image sizes.

The special cases zero, binary lines of size two, the full field, and the
distinction between time one and later times were all attacked explicitly.
No unproved converse or missing carrier stratum was found.

## Findings

### Critical

None.

### Major

None.

### Minor

None.

## Exact and source controls

A fresh process replayed the author standard-library verifier and matched
the 827-byte frozen transcript byte for byte.  It reconstructs complete
subspace lattices and all directed edges for `p=2,3,5`, including every
target fibre through time four, and reports 32,754 assertions.

In addition, Review A wrote a separate implementation using coefficient-tuple
field elements and breadth-first discovery of the subspace lattice, rather
than the author's packed elements and RREF-template enumeration.  It rebuilt
the complete graphs for `p=2,3`, checked every target through time four,
tested the recurrent classification and twisted scalar action, and executed
82,955 reviewer assertions.  Two fresh processes matched its canonical
transcript byte for byte:

```text
390fdc7b0fc901daab61c95263538986adcd9aa3923a2389eee331e7b0104f24  verify_review.py
123a1eb97c4ce856eac61e78628e835b13a6178cd1356216ff20077abee1e65d  CANONICAL.txt
```

The independent evidence is retained under
`docs/papers167_171_sequence/reviews/p168_a/`.  Neither implementation
imports scouting or manuscript code, and no hidden sampling is used for its
advertised exhaustive primes.

The six bibliographic records and their print-issue years agree with the
listed DOI records.  Most importantly, the manuscript does not relabel the
published inverse-subspace classification or inverse-line geometry as a new
result.  The residual claim is only the degree-four dynamical integration:
the binary/odd depth jump, complete graph and stabilization, and all-time
fibre atlas.  That is a coherent internal result, but its direct dependence
on owner theorems makes `HOLD_EXTERNAL` essential.

## Build and presentation

The five-page A4 artifact is anonymous, has blank standard metadata, and
uses embedded/subsetted/Unicode-mapped fonts.  Review A repeated two
source-only builds in distinct fresh directories; both were byte-identical
to each other and to the pinned PDF with SHA-256
`846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e`.
The settled logs have no warning, bad box, unresolved reference, or citation.
The theorem tables and long fibre display remain within the page box.

## Recommendation

Accept Round 0 without repair for independent Review B.  Preserve the
owner-dependent theorem ceiling and external hold.
