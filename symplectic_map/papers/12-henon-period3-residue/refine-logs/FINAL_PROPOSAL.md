# Research Proposal: A Uniform Period-Three Residue Law on Exceptional Henon Families

## Problem Anchor

Cantat--Dujardin's quartic Jacobian-minus-one family shows that formal
multiplier traces through period two can be constant on a
positive-dimensional normalized Henon family. Their general finite-cutoff
result is non-effective. This project asks for the first separating trace
period on the complete normalized quartic fiber whose formal fixed-point trace
multiset is \(0^4\), and for the
smallest degree-uniform algebraic mechanism that explains it.

## Dominant Contribution

For a monic-centered quartic

\[
f_p(x,y)=(y+p(x),x),
\]

formal fixed-point trace multiset \(0^4\) forces

\[
p(x)=(x^2-L)^2.
\]

Thus the known exceptional family is the complete normalized quartic
fiber with formal fixed-point trace multiset \(0^4\). On this fiber:

\[
\operatorname{Trace}_1=0^{\times4},
\qquad
\operatorname{Trace}_2=2^{\times12},
\]

and the formal exact-period-three second trace moment is

\[
S_2^{(3)}(L)
=-1296000-1572864L^3.
\]

Normalized conjugacy is classified by \(L^3\), so this affine moment separates
the fiber exactly. Because periods one and two are constant, period three is
minimal on this fiber.

## Supporting Uniform Mechanism

For every \(m\ge2\), consider

\[
f_{m,a}(x,y)=\bigl(y+(x^m-a)^2,x\bigr).
\]

The normalized quotient coordinate is \(a^{2m-1}\), while the formal
period-one and exact-period-two trace multisets remain constant. Introduce the
period-three cyclic complete intersection

\[
F_i=(x_i^m-a)^2+\varepsilon(x_{i-1}-x_{i+1})
\]

and its Jacobian/derivative-trace function

\[
t_\varepsilon
=q_0q_1q_2+\varepsilon^2(q_0+q_1+q_2),
\qquad
q_i=2m x_i^{m-1}(x_i^m-a).
\]

The quotient is monic free of rank \((2m)^3\), and

\[
\operatorname{Tr}(t_\varepsilon^m)
=\operatorname{Res}(t_\varepsilon^{m+1}).
\]

Weighted homogeneity first leaves four parameter monomials. The separated
double-root algebra and the complete root-triple Newton--Puiseux/trace-order
analysis in Step 7 remove the two higher invariant powers, yielding

\[
S_m(a,\varepsilon)
=C_m\varepsilon^{3m}
+D_ma^{2m-1}\varepsilon^{2m}.
\]

Cyclic reversal gives \(C_m=0\) for odd \(m\). The slope \(D_m\) has the
finite nested-binomial certificate

\[
D_m=3\sum_{j=0}^{\lfloor m/2\rfloor}
\binom{m+1}{j}(2m)^{3m+3-2j}A_{m,m-j},
\]

with \(A_{m,r}\) and its inner sum \(H(r,k)\) defined explicitly in the
research question and proof package. In the current bound proof-package
candidate (proof-package SHA-256
`36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9`),
Step 9 derives this certificate from the terminating normal-form recurrence,
its Laurent/admissible-tuple expansion, and the exact local binomial fiber
identity (9.14). The resulting congruence selects a distinguished coordinate,
the transfer-flow equations give the \((k,u,v)\) parameterization with its
sign and multiplicity, and the separate \(j=0\) analysis eliminates the
additional incoming-flow type. Thus the earlier recurrence-enumeration gap is
closed inside the candidate; independent source-lock review remains pending.

The quartic ledger has two further checks that do not merely respecialize the
uniform collapse. Step 12 independently obtains
\(D_2=4^9(-6)=-1572864\) by tensor Laurent residues and then computes
\(C_2=-1296000\). Step 13 proves, in local coordinates around every multiple
fixed root, that its length in \(\operatorname{Fix}(f^3)\) equals its fixed
scheme length. This validates the exact-period subtraction, length \(60\),
and division by three used for the cyclewise moment.

## Contribution Discipline

The paper has exactly one dominant result and one supporting mechanism:

1. dominant: the full quartic fiber and its minimal period-three conjugacy
   separator;
2. supporting: the uniform residue law and finite coefficient certificate
   explaining why the quartic identity is structural.

The project does not add a third route. In particular, it does not add height,
prime, zero, saddle-spectrum, thermodynamic, or global rigidity claims.

## Critical Open Boundary

The statement

\[
D_m\ne0\qquad\text{for every }m\ge2
\]

is open. The project does not claim all-degree period-three separation.
Finite exact checks cannot prove this conjecture.

## Claim-Driven Audit

If and only if a fresh source review and later deployment review authorize
execution, one exact CPU audit will contain:

1. two independent derivations of the quartic fiber, normalized conjugacy,
   low-period formal spectra, fixed-cycle subtraction, and period-three
   polynomial;
2. a proof-contract audit for the general theorem;
3. two genuinely independent finite evaluators of the coefficient certificate
   at the sole diagnostic tuple \(T_{\mathrm{reg}}=(8,9)\);
4. negative controls for cyclic signs, trace--residue exponent, formal-period
   normalization, scope expansion, finite-sample overclaim, shared engines,
   and external/scanning operations;
5. an atomic one-shot lifecycle with independent deployment and result
   reviews.

The tuple \((8,9)\) is disjoint from development checks \(m=2,\ldots,7\),
cannot be expanded, and serves only to falsify implementation disagreement.
The previously noted \(m=2,\ldots,7\) recurrence recheck is a pre-lock,
non-evidentiary development diagnostic; no values from it are retained or
admitted as registered evidence. The full quotient/residue engine runs only
for the decisive quartic case.

## Literature Position

The manuscript will:

- credit Cantat--Dujardin for the quartic family and period-one/two
  blindness;
- use Friedland--Milnor for normalized Henon structure;
- credit Cattani--Dickenstein--Sturmfels for multidimensional residue
  machinery;
- distinguish the raw formal trace moment from the exact Henon orbit sum
  rules of Cvitanovic--Hansen--Rolf--Vattay;
- position Dullin--Meiss, Huguin, Hutz, Guillot--Ramirez, and Ueda as
  low-period, moduli, dynatomic, and fixed-point background as needed.

The bounded 2026-08-16 search found no direct statement of the period-three
identity, the complete-fiber minimal separator, or the uniform two-term
certificate. This is not an absolute absence or priority claim.

## Success Condition

The source stage succeeds only if an independent reviewer verifies:

- the nonreduced formal-spectrum interpretation;
- normalized conjugacy necessity and sufficiency;
- monic freeness and absence of contributions at infinity;
- the Step-7 Puiseux branch coverage and trace descent already supplied by
  the bound proof-package candidate;
- the Step-9 recurrence/Laurent/admissible-tuple reduction, identity (9.14),
  distinguished-coordinate transfer flow, and \(j=0\) boundary case;
- the independent Step-12 quartic coefficient derivation and Step-13 local
  fixed-branch multiplicity argument;
- the quartic integer ledger;
- citation roles and every mandatory nonclaim.

The completed proof package is bound by source-lock v2 after the bounded R1
repair, but it is not yet independently approved. Only a fresh, hash-bound v2
`SOURCE_LOCK_PASS` authorizes implementation.
