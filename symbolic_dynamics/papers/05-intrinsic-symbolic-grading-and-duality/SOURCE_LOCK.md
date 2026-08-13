# Paper 05 Source Lock

## Stage identity

- Date frozen: 2026-08-13.
- Base candidate: SD-C07.
- New candidate ID: none; SD-C08 is forbidden unless G0--G4 all pass.
- Primary system family: Symbolic Dynamics.
- Final stage status:
  **GO_A2_GRADED_ORIENTATION / STOP_A3_COMPLETION**.
- Route B: locked.

## Shared object

The only arithmetic source is the symmetric monoidal skeleton of finite full
shifts:

\[
F_m\boxtimes F_n\cong F_{mn},
\qquad
h_{\rm top}(F_n)=\log n.
\]

The atom-loop transfer is

\[
L_s e_p=p^{-s}e_p
\]

on \(\ell^2(\operatorname{At}(\mathsf{FSh}))\). Every credited Paper05
construction is a functor on this source:

1. the reduced order complex of the open tensor-divisor interval;
2. the zero-differential exterior transfer module;
3. the standard equivariant Koszul resolution;
4. stable/unstable symbolic reversal;
5. the Grothendieck group completion of the tensor monoid.

## Frozen determinant data types

These objects must remain distinct:

- ordinary Fredholm determinant
  \(\det(I-L_s)=1/\zeta(s)\);
- exterior-Fock supertrace
  \(\operatorname{Str}\Gamma_-(L_s)=1/\zeta(s)\);
- odd one-particle Berezinian
  \(\operatorname{Ber}(I-L_s)=\zeta(s)\);
- full Koszul superdeterminant
  \(\operatorname{sdet}(I-zT_s)=1-z\);
- adversarial paired regularized determinant \(D_3\), which receives no
  source or G4 credit.

All infinite identities above are initially restricted to their proved
operator domains.

## Allowed inputs

- full-shift tensor product and tensor unit;
- topological entropy;
- tensor divisibility;
- reduced simplicial chain degree and standard signed boundary;
- finite atom cutoffs and predeclared complex cutoffs;
- random/global parity, shifted/additive monoid, and free-mixing controls.

## Forbidden inputs and moves

- rational-prime or Riemann-zero tables in the candidate definition;
- parity or simplex shifts selected after seeing \(\mu\);
- a hand-written half-density \(p^{-1/2}\) credited as intrinsic;
- a copied Gamma factor, zeta continuation, or functional equation;
- divergent trace subtraction without a relative determinant theorem;
- fitted regularization counterterms;
- interpreting homological degree as a new temporal primitive orbit;
- combining favorable coordinates from incompatible candidates or branches;
- Route B.

## Precision and cutoffs

- Exact integer boundary arithmetic and exact coefficient ledgers.
- Exact GF(2) rank computation with integral topology proved separately.
- Full object cutoffs \(N=64,128,256,512\).
- Binary64 is used only for finite dual-ratio and Schatten partial-norm
  diagnostics.
- No Riemann zero or target-root cutoff exists.

## Mechanical promotion rule

Paper05 may assign SD-C08 only if one frozen branch supplies, on the same
object, a nonempty new analytic domain, a canonical relative determinant,
an internally derived functional-equation factor, or a same-object
Weil/Lefschetz compression. None occurs. The exact grading theorem therefore
enhances SD-C07 without promoting a new candidate.
