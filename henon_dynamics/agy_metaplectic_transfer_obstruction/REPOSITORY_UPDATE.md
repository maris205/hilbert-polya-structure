# HCS-C25 repository update

**Release date:** 2026-08-10
**Release status:** independently validated

## Released update

HCS-C25 applies the C24 infinite-fibre obstruction to a source-standard
Avila--Gouëzel--Yoccoz countable Rauzy first-return transfer operator.  It
also adds an all-length row-subtraction decoder proving that, from a fixed
labeled starting permutation, the chronological Rauzy matrix uniquely
determines the path.

The release contains:

- a primary-source audit of the AGY section, inverse branches, Jacobian, roof,
  and `C_b^1` transfer family;
- exact construction of a neat, strongly-positive four-interval section;
- producer and independent-checker certificates for chronology and decoding;
- noncompactness theorems for the vector-valued AGY `C_b^1` transfer and the
  invariant-density normalized `L^2` transfer;
- a Route-A rejection of the ordinary Fredholm realization, with
  holomorphic/generalized-trace alternatives explicitly left open;
- a compiled technical note.

The independent implementation passes eleven source/chronology checks and all
fourteen mutation/regression tests.  It reconstructs the exact length-128
section word, its positive determinant-one matrix, the projective
`J=exp(-4r)` identity, seven integral state frames, fourteen fixed-fibre
symplectic edges, and every step of the all-length decoder witness.  A
separate non-proof sentinel decodes 35,420 central first returns through
elementary length 22 with zero collision.

The raw vector-valued `C_b^1` operator is noncompact throughout the AGY
half-plane `Re(s)>-sigma_0`.  The normalized `L^2` operator is noncompact for
`Re(s)>=0` and has essential norm one on `s=it`; the normalized scalar
operator is already noncompact on this half-plane.

No legacy result is deleted or weakened.  C25 closes the source-standard-space
application left open by C24 and redirects the next broad search away from
longer elementary periodic ledgers.
