# HCS-C61 narrative report

Status: **`TARGET_LOCKED / IMPLEMENTATION_PENDING / PAPER_PENDING /
NOT_RELEASED`.**

Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Target-report binding:
`eb0a70f62427cd8b70fa35dc4153bd93d57d9ddef5ab7a349d439be3a8257026`.

This report explains why the target is one coherent theorem-sized successor.
It does not convert the selection pilots into proof.

## 1. What C60 leaves behind

C59 constructed two nonconjugate degree-320 fixed fields with the same
rational permutation character and Dedekind zeta function.  C60 then found a
specific `V4` envelope around them: a degree-160 core `M`, three quadratic
arms, and the degree-640 field `L`, with primitive carriers and complete
arithmetic in two retained local branches.

That theorem answers an additive/fixed-field question.  It does not say what
happens after multiplying the two Burnside classes or tensoring their fields.

## 2. The information rational characters forget

Write `x=[G/H_+]` and `y=[G/H_-]`.  The equality
`lin(x)=lin(y)` survives multiplication, so the rational characters of
`x^2`, `xy`, and `y^2` coincide automatically.  Their orbit structures need
not coincide.

The proposed C61 computation makes that loss visible.  Both self products
have factor degrees

```text
320,320,960,960,1920,5760,5760,8640,8640,17280,25920,25920,
```

whereas the mixed product has

```text
640,960,960,1920,2880,2880,2880,2880,8640,8640,17280,51840.
```

Each list has twelve entries and sum 102400.  The mixed product is therefore
visibly different.  The two self products require a subtler proof: their
equal spectra conceal distinct diagonal degree-320 subgroup types.  This is
the core mathematical point, not the production of a large table.

## 3. From twelve mixed factors to eight fields

The mixed algebra simultaneously supports three counts: 160 conjugate
positions of `H_-`, twelve double-coset factors, and eight `Q`-isomorphism
types.  C61 must prove the passage between them through exact embedded
intersection groups, core-freeness, and extension of field isomorphisms to the
common normal closure `K`.

The ends of this spectrum reconnect to released authority.  The unique
degree-640 mixed factor is C60's `L`, with base `M`; the unique degree-51840
factor is `K`.  These are internal checks and conceptual anchors, not a new
claim that C60 failed to prove its field tower.

## 4. Why Fourier descent belongs in the same paper

C60's primitive carrier `lambda` has a surprising Fourier profile under the
`V4` quotient: one direct character component vanishes, while the remaining
three components span dimension three.  After exact normalization, `r_+`
and its square define degree-80 and degree-40 fields `B` and `A`.

The future certificate must not infer this rank from formal labels alone.  At
the split prime, the 243-term Trace carrier and normalized `r_+,r_3` have
nonzero identity values `581739,643771,119649`; their three distinct character
eigenspaces give the exact rank-three bridge.

The decisive C61 bridge is not merely that an order-1296 subgroup appears in
both calculations.  The sign stabilizer of `r_+` must equal the canonical
seed-149 mixed join as the same embedded element set.  It then follows that
the degree-40 Fourier field is exactly one mixed intersection field, and the
quadratic extension `B/A` base-changes to `F_+/M`:

\[
 B\cap M=A,\qquad BM=F_+.
\]

This exact meeting point turns two computations into one theorem.  If the
equality fails, the Fourier material is an afterthought and C61 is killed.

## 5. The corrected order-1296 picture

The plus-self `263f...` and embedded minus-self `a426...` degree-1920 joins
are G-conjugate; they represent one self P3 class.  That class is
nonconjugate to the mixed Fourier join `55d7...`.  The implementation must
check the exact conjugator and the nonconjugacy.  Describing all three
embedded joins as mutually nonconjugate is stale and false.

## 6. Arithmetic as certificate, not headline inflation

Signatures, discriminants, relative norms, and both local branches make the
field dictionary testable and distinguish equal-degree types.  The degree-40
fields already have different arithmetic, and the two mixed degree-2880
types have different 3-adic different totals.  These facts strengthen the
certificate; they are not a replacement for the Burnside and Fourier proofs.

The ideal complementarity inside the C60 envelope is a subordinate structural
corollary.  Both ToM140 and ToM206 remain present, and neither is selected.

## 7. Why this remains conditional

The selection lanes agree on a feasible target, but complete project-local
self atlases, exact resolvents, split-prime noncollision, both branch tables
for `B`, and independent hostile checking do not yet exist.  Consequently all
G0--G7 gates remain pending.  There is no theorem, manuscript, or release.

## 8. Current state

The title, object, theorem skeleton, source boundary, experiment contract, and
KILL gates are locked.  Implementation and every downstream phase remain
pending, with promotion authorization false.
