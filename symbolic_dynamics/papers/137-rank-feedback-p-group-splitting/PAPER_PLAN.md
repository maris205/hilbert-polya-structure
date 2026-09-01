# Paper plan: rank-feedback splitting of finite abelian p-groups

**Working title:** Rank-Feedback Splitting of Finite Abelian `p`-Groups: A
Sharp Triangular Clock and Exact Target Fibres  
**Type:** anonymous rigorous mathematical short note  
**Status:** `INTERNAL DRAFT / HOLD_EXTERNAL`  
**Target length:** 4--6 A4 pages, including references  
**Literal map:** `F(G)=p^d(G)G direct_sum G[p^d(G)]` on isomorphism classes
of finite abelian `p`-groups of fixed order  
**One-sentence contribution:** After subtracting all standard finite-abelian-
group and partition machinery, prove the complete state-dependent type rule,
fixed/recurrent set and OGF, a unique sharp triangular entry clock, and an
exact inverse decoder over every target.

## Claims--evidence matrix

| Claim | Proof object | Paper-local control | Credit boundary |
|---|---|---|---|
| The literal group map preserves order and acts on type `lambda=(a_i)`, `r=ell(lambda)`, by keeping `a_i<=r` and splitting `a_i>r` into `(r,a_i-r)`. | Proposition 2.1 and the multiplication-by-`p^r` exact sequence. | Literal cyclic kernels and images for `p=2,3`, exponents `1..8`, ranks `0..10`; factorwise type equality on all partitions through weight 50. | Finite abelian group classification, `d(G)=dim G/pG`, and cyclic kernel/image types are zero credit. |
| Recurrent types are exactly fixed types `lambda_1<=ell(lambda)`. | Proposition 3.1 and strict rank increase. | Complete functional graphs on all 1,295,970 partitions through weight 50. | Generic finite-map recurrence and monotone-potential reasoning are zero credit. |
| Fixed types have OGF `1+sum_r z^r [2r-1 choose r]_z`. | Ferrers rectangle bijection in Section 3. | Coefficients 0 through 50 from an independent q-Pascal recurrence. | Ferrers diagrams and Gaussian-binomial rectangle enumeration are zero credit. |
| Every type of initial rank `r0` and entry time `d` obeys `n>=r0(d+1)+binom(d,2)`; the global clock is `D(n)=ceil((sqrt(8n+1)-3)/2)`, uniquely attained by `(n)`. | Frozen-marker budget, explicit cyclic-type orbit, and rank-2 exclusion in Section 4. | Every state through weight 50 satisfies the pointwise budget; each weight has the predicted maximum and unique deepest source `(n)`. | Triangular-number algebra is zero credit; the residual is the sharp feedback-dynamics statement. |
| Every target has the displayed bounded-choice fibre formula and exact image criterion. | Marker-removal/reconstruction bijection in Section 5. | Every one of 81,155 targets through weight 35, including 30,923 zero-fibre targets. | Formal coefficient extraction is zero credit. |

## Structure

1. **Literal map and theorem.** Define the group operator, type carrier,
   entry time, fibre notation, and front-load the complete result.
2. **Group/type identity.** Derive the type split factor by factor and verify
   order preservation from the kernel/image exact sequence.
3. **Fixed and recurrent set.** Use strict length growth and enumerate fixed
   Ferrers rectangles.
4. **Sharp clock.** Tag initial parts, freeze every rank marker, prove the
   pointwise budget, construct the cyclic-type orbit, and prove uniqueness.
5. **Every-target inverse geometry.** Remove candidate marker copies, force
   all large residuals, and count the remaining bounded choices.
6. **Ownership and controls.** State zero-credit inputs, internal collision
   separation, bounded source-audit limits, and exact finite controls.

## Display plan

No decorative figure is needed.  The main theorem contains the literal type
map, fixed OGF, pointwise and global clocks, explicit deepest orbit, fibre
formula, and image criterion.  One compact terminal table reports only exact
falsification controls.

## Citation plan

- Fuchs: finite abelian group classification and cyclic direct sums.
- Andrews: partitions, Ferrers rectangles, and Gaussian polynomials.
- Delaunay--Jouhet: `p^ell`-torsion statistics on partition-indexed finite
  abelian groups.
- Eliahou--Erickson and Baalbaki et al.: different established iteration
  settings on integer partitions.

Publisher/DOI metadata are recorded in `SOURCE_VERIFICATION.md`.  All cited
background is subtracted.  No search non-hit is treated as priority evidence.

## Release gate

The package may be complete as an internal theorem draft, but it remains
`HOLD_EXTERNAL`.  No novelty, priority, authorship, posting, submission, or
specialist-contact decision is made here.
