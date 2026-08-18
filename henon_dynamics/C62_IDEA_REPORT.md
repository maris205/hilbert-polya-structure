# HCS-C62 adaptive idea report

Date: 2026-08-18

This is the first successor-selection record after the frozen C57--C61
batch.  It uses only the released C61 theorem as authority; no pilot or
uncommitted computation is a theorem premise.

## Direction

Continue the arithmetic-equivalence program for the released nonconjugate
order-162 Gassmann pair in (W(E_6)), while changing the Burnside operation
so that the next paper is not a repetition of C61's tensor products.

## Candidates

| rank | candidate | verdict |
|---|---|---|
| 1 | Exterior/symmetric-square lambda shadows of the two 320-point G-sets | **SELECT** |
| 2 | Cubic tensor products (x^3,x^2y,xy^2,y^3) | defer: same tensor mechanism and much larger atlas |
| 3 | Integral-order/discriminant separation of the C61 factors | defer: requires an unprovided maximal-order/integral-basis authority layer |

## Selected C62 target

Let (G=W(E_6)), (X_+=G/H_+), (X_-=G/H_-), and let
(Lambda^2X_pm) and (operatorname{Sym}^2X_pm) denote the G-sets of
2-subsets and size-two multisets.  The selected paper will determine their
complete orbit/stabilizer atlases and prove, conditional on exact gates, that

\[
\operatorname{lin}(\Lambda^2X_+)=\operatorname{lin}(\Lambda^2X_-),\qquad
\operatorname{lin}(\operatorname{Sym}^2X_+)=
\operatorname{lin}(\operatorname{Sym}^2X_-),
\]

while the corresponding finite G-sets and finite-etale algebras are not
isomorphic.  The equality is forced by the character identities

\[
\chi_{\Lambda^2X}(g)=\frac{\chi_X(g)^2-\chi_X(g^2)}2,
\qquad
\chi_{\operatorname{Sym}^2X}(g)=
\frac{\chi_X(g)^2+\chi_X(g^2)}2,
\]

and the C61 Gassmann equality; the nonisomorphism must come from a complete
finite-group orbit computation, not from character data.

## Why this is the right successor

It is a new lambda-ring operation on the exact C61 object, not another
tensor-power table.  It gives a positive theorem if the two shadows differ
and a sharp obstruction if either pair unexpectedly collapses.  Its ambient
sizes are fixed at \(|\Lambda^2X|=51,040\) and
\(|\operatorname{Sym}^2X|=51,360\), so the first exact pilot is finite-group
only and does not require a GPU.

## Scope firewall

`NO_BAD_EULER_OR_ROOT_NUMBER` remains literal.  No automorphy, Artin
holomorphy, root number, maximal-order, integral-basis, monogenicity,
Brauer--Manin, RH, or Hilbert--Polya claim is selected.
