# Variable multiplication collapses Haar image and defeats a countable inverse atlas

**Paper:** `362-variable-multiplier-admission`; screen `ANG-SCREEN-20260921-VMA01`.
**Date/status:** 2026-09-21; **NONSINGULARITY AND COUNTABLE ATLAS FAIL — SCOPED STOP / FORK**.
Pre-P0 measured admission only; no completed clock or flow candidate.
T2/T3 NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## 1. Abstract and exact owner

On the full X=K², K=Z-hat, with additive product Haar mu, the total update
T(x,y)=(y,xy+1) has a compact Haar-null image. Hence its pushforward
probability is singular to mu, contradicting the frozen forward-nonsingularity
question F. Its fibre over (0,1) is uncountable, already excluding a countable
full injective inverse atlas A; the IMAGE condition also independently blocks
such a measured atlas. Three full-source controls pass F and A on their own
maps. These conclusions stop only the two specified admission requirements,
not arbitrary non-etale/uncountable or differently measured constructions.

The [card](candidate-card.md) retains all states, null fibres and predecessors.
There is no defined clock, physical time, operator, trace, symplectic form or
mapping torus to borrow. Current divisibility enters the actual inverse:
at (a,b) every predecessor is (u,a) with au=b-1. For integer a=d>=1,
b-1=n, this has a K solution iff n lies in dK, equivalently d|n; if so
division is unique. For arbitrary nonunits, all annihilator translates remain.

## 2. Full fibres and the countability obstruction

The equation au=b-1 is solvable exactly when b-1 belongs to the compact
ideal aK. If u_0 is one solution, its ENTIRE solution set is
u_0+Ann(a), where Ann(a)={v:av=0}. This statement selects no representative
in the owner and requires no arbitrary cancellation. In the product of Z_p,
Ann(a) has unrestricted p-components where a_p=0 and zero components where
a_p is nonzero, since each Z_p is an integral domain. In particular

```text
T^-1{(0,1)}={(u,0):u in K}.                            (1)
```

K is uncountable: its Z_2 factor already contains distinct infinite binary
digit strings. Any source set on which T is injective meets (1) in at most
one point. Countably many such sets cannot cover (1), hence cannot cover X.
Thus A fails even without asking Borel regularity or a density. The fibre
itself is null; this argument alone does NOT prove failure of F.

## 3. The complete image is Haar null: a separate proof of F failure

Let S=T(X)={(a,b):b-1 in aK}. T is continuous and X compact, so S is
compact and Borel. For every prime p, membership in S implies
a=0 mod p => b=1 mod p. There are p(p-1)+1 admitted pairs modulo p out
of p². For any finite set P of primes, CRT and product Haar give

```text
mu(S) <= product_(p in P) (1-1/p+1/p²).                (2)
```

This is an exact necessary-condition bound on the FULL image, not an
existence argument or finite simulation. To see the right side tends to
zero, here is the needed elementary infinite argument. If sum_p 1/p were
finite, the finite Euler products product_(p<=N)(1-1/p)^-1 would be bounded:
for p>=2, -log(1-1/p)<=2/p. Expanding each finite geometric product with
nonnegative terms and using unique factorization shows it is at least
sum_(n<=N)1/n, which is unbounded (group integers in dyadic blocks).
This contradiction proves sum_p1/p diverges. Meanwhile sum_p1/p² converges,
bounded by the integer square series. Since log(1-t)<=-t for 0<t<1,
(2) is at most exp(-sum_(p in P)(1/p-1/p²)), tending to zero.

Therefore mu(S)=0 but T^-1 S=X has measure one. More strongly T_*mu is
supported on S and is singular to mu. F FAILS. The product limit, not one
chosen modulus or finite precision, is essential to this conclusion.

There is also a separate measured-atlas contradiction: any proposed V_i
lies in S. The EVERY-Borel IMAGE law with E=V_i would imply
mu(U_i)=integral_(V_i) J_i dmu=0. Countably many U_i cannot cover X, or
even a conull part. This uses exactly the frozen countable measured atlas,
not an assertion about arbitrary uncountable groupoid Haar systems.

## 4. Three independently owned controls

FIXED. Integer multiplication by 2 is injective on K: 2x=0 modulo 2m
forces x=0 modulo m for every m. Its image is 2K of Haar mass 1/2,
and normalized Haar there is the pushforward of h. Thus T_F(x,y)=(y,2x+1)
is a bijection from X onto V_F={b-1 in 2K}; theta_F=((b-1)/2,a) is its
continuous inverse. For EVERY Borel E subset V_F,
mu(theta_F E)=2 mu(E). Hence J_F=2 is a positive finite all-point atlas
version, A passes, and (T_F)_*mu=2 1_(V_F) mu proves F. Points outside
V_F have no predecessor, but still have their own forward step under T_F.

UNIT-FEEDBACK. Parity is continuous, and epsilon(a)=±1 equals its inverse.
The displayed theta_j in the card is the entire inverse on V_j; substitution
gives both identities and the two branches cover all X. On each a-fibre,
b->epsilon(a)(b-1) preserves additive Haar. Fubini and the coordinate swap
give mu(theta_j E)=mu(E) for EVERY Borel E subset V_j. Thus J_j=1 on all
points, the combined total map preserves mu, and both F and A pass. No
restriction to a unit subset of MAIN was used.

ADDITIVE. The map (x,y)->(y,x+y+1) has total inverse (b-a-1,a).
Fibrewise translation and swap preserve product Haar on all Borel sets.
Its single branch has J_A=1 everywhere; the total map preserves mu and
passes F and A. This is its own proof, not a transferred matrix clock.

## 5. Gate, integrity and next decision

| Owner | F: T_*mu << mu | A: full countable measured inverse atlas |
| --- | --- | --- |
| MAIN variable multiplier | FAIL: singular pushforward | FAIL: uncountable fibre; independently null image |
| FIXED integer coefficient | PASS, density 2 on its image | PASS, one full-source branch with J=2 |
| UNIT-FEEDBACK | PASS, invariant mu | PASS, both branches J=1 |
| ADDITIVE | PASS, invariant mu | PASS, full inverse J=1 |

Portfolio **SCOPED STOP / FORK**. The same T, mu and full predecessor
relation remained intact. No physical prime-period or general non-etale
no-go is asserted; other carriers/measures/clocks remain untested, not
refuted. In particular null saturation under an uncountable action alone
would NOT justify our countable-atlas conclusion. Strong naturalness OPEN.

Inputs: original93-line [card](candidate-card.md), SHA256
0755f26b9b18287cca9f0a0c6ab4ad42e0e3c56703e4011389abe43d8bb9cba8.
Methods: exact fibre equations, compactness, CRT, an unbounded finite-product
argument and own Haar identities. No scientific numerical code or cutoff.
Root's later collision read of283 card1–130/paper157–208 concerned its
different reversible Hénon owner, and supplied no theorem used here.
[Scope](evidence/scope-review.md), [independent proof](evidence/independent-proof.md)
and [analysis review](evidence/review.md) are internal shared-history
NOT_CALIBRATED, not external peer review or novelty certification.

EOF — failed specified admissions; no borrowed clock or universal carrier claim.
