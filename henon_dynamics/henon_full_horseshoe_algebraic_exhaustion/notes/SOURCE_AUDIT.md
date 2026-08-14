# Source audit

## Primary imported theorems

1. **Zin Arai (2007), Theorem 1.2.** For the convention
   `H_(a,b)(x,y)=(a-x^2+b y,x)`, the chain recurrent set at `b=-1` is
   uniformly hyperbolic for
   `a>=5.699951171875=23347/4096`.  The paper also identifies hyperbolicity
   with R-stability on the plateau.  We use only this parameter range and
   stability role.
2. **Devaney--Nitecki (1979).** Their normalization is
   `(x,y)->(1+y-Ax^2,Bx)`. At `B=-1`, the scaling
   `(X,Y)=(Ax,-Ay)` gives Arai's `(X,Y)->(A-X^2-Y,X)` convention. Their
   threshold `(5+2sqrt(5))(1+|B|)^2/4` therefore becomes
   `A>5+2sqrt(5)`. We use `A=10` as an anchor, not `A=6` directly.
3. **Friedland--Milnor (1989), Theorem 3.1.** A cyclically reduced degree-`d`
   polynomial automorphism of the complex plane has algebraic fixed-point
   count `d`, with multiplicity.  Applied to `H6^n`, this gives `2^n`.

## New deductions in this project

- the explicit scaling `S(q,p)=(6q,6p)` between the repository map and the
  `a=6,b=-1` source convention;
- transport of the full-shift anchor along the connected certified plateau;
- exhaustion of the complete complex algebraic fixed-point scheme by the
  real full-shift points;
- all-period total reality and squarefreeness of the P60 mixed-axis closure;
- reduced exact-period effectivity of its Möbius primitive quotient.

## Context only

Sterling--Dullin--Meiss discuss the area-preserving horseshoe boundary and
numerical evidence near `a=5.699`.  Their numerical boundary is not used to
prove the `a=6` theorem.  Kang supplies reversible-map context, and Hutz
supplies general dynatomic-effectivity context; neither is used as a black
box for the main exhaustion theorem.

## Primary links

- Arai preprint: <https://www.math.kyoto-u.ac.jp/preprint/2005/8arai.pdf>
- Devaney--Nitecki DOI: <https://doi.org/10.1007/BF01221362>
- Friedland--Milnor DOI: <https://doi.org/10.1017/S014338570000482X>
- Friedland--Milnor PDF: <https://deserti.perso.math.cnrs.fr/biblio/FriedlandMilnor_dynamicalpropertiesofplanepolynomialautomorphisms.pdf>
