# HCS-C58 theorem package

Status: **THEOREM_TARGET_LOCKED; EXACT PREMISES
PREFREEZE_CODE_RESULTS_PASS; POSTREFRESH_PASS; FORMAL-DOCUMENT HOSTILE AUDIT
PASS; PAPER_PENDING; NOT_RELEASED.**

This file states the C58 machine-prefreeze theorems and their exact finite
premises. G0--G7 and the independent post-refresh audit certify those premises;
PROOF_PACKAGE.md records the mathematical bridges. Paper and release are
separate pending layers.

## 1. Frozen object

Let \(Y/\mathbf Q\) be the frozen smooth cubic surface. Let \(E/\mathbf Q\)
be its degree-27 line field and \(K/\mathbf Q\) its normal closure:

\[
[E:\mathbf Q]=27,\qquad
\operatorname{Gal}(K/\mathbf Q)=W(E_6),\qquad |W(E_6)|=51840.
\tag{1.1}
\]

Let

\[
\mathbf Q[27]=\mathbf1\oplus V_6\oplus V_{20}.
\tag{1.2}
\]

Put

\[
q=14932047182473291995860108491583652133938007263719,
\tag{1.3}
\]

\[
A=181\cdot997\cdot2346241,\qquad B=283\cdot1801\cdot q.
\tag{1.4}
\]

## 2. C58-EXACT-0 through C58-EXACT-7

Every premise below is **PREFREEZE_CODE_RESULTS_PASS**.

### C58-EXACT-0: frozen import

- exact C55 surface identity;
- exact C56 line polynomial, field certificate, and 27-line action;
- exact C57 theta/delta identities and double-six action, with theta alone
  `KRASNER_CERTIFIED_AUTHORITY` and delta
  `BOUNDED_NON_RESULT_NONDEPENDENCY` (neither dependency nor corroboration);
- exact \(W(E_6)\) generators and Picard matrices;
- fresh upstream full-inventory binding with self-excluded counts 47/46/64.

### C58-EXACT-1: support and global order

- divided discriminant reproduced independently;
- surface divided-discriminant bad-prime envelope

  \[
  \{2,3,5,181,283,997,1801,2346241,q\};
  \]

- exact ramified support of both \(E\) and \(K\),
  \(\{3,5,181,283,997,1801,2346241,q\}\);
- exponent vector `(0,46,36,18,6,18,6,18,6)` for `Disc(E)` on the displayed
  nine-prime envelope;
- \(2\) absent from \(\operatorname{Disc}E\) and from ramification in \(K\);
- 27-element maximal order basis and positive field discriminant;
- unramifiedness outside the exact eight-prime support.

### C58-EXACT-2: local maximal orders

At \(3\):

\[
(e,f,d)=(3,1,3),(6,1,7),(9,1,18)^2.
\]

At \(5\):

\[
(e,f,d)=(1,1,0)^2,(5,1,7)^3,(10,1,15).
\]

At each \(181,997,2346241\):

\[
(e,f,d)=(3,1,2),(3,2,2),(3,6,2).
\]

Theta alone certifies degree-36 local partitions. At the tame primes it is
stable at `[20,30,40]`; precision 40 clears its global and twice-largest
factor-polynomial discriminant bounds 24/24 and certifies degrees
`(3,6,9,18)`. Delta's corresponding bounds are 840/408, so precision 40
clears neither. At p=3, theta is stable, simple, and multiplies back at
`[900,950,1000]`, clearing 886/538 and giving `(3,3,3,9,18)`; at p=5 the
same precisions clear 746/246 and give `(1,5,10,10,10)`. Delta remains a
bounded nonresult/nondependency at the wild primes too.

### C58-EXACT-3: dual-carrier subgroup classification

- exact 27-line and 36-double-six local orbit patterns over all 350
  `U4(2).2` Table-of-Marks classes;
- p=3 hits ToM 140/order 18, 142/order 18, 206/order 36 and exhaustive valid
  `(D,I,|D/I|)` triples `(140,140,1)`, `(142,142,1)`, `(206,140,2)`,
  `(206,142,2)`, with ToM 206 D-only;
- p=5 hits 147/247/295 and unique valid triple `(147,147,1)` after the
  Sylow-5 normality filter;
- complete deep p=3 inventory ToM 6 with multiplicity two, ToM 7 once, and
  ToM 8 once.

### C58-EXACT-4: filtered inertia

\[
p=3:\quad
I_0\cong(C_3^2):C_2,\quad I_1=C_3^2,\quad
I_2=\cdots=I_7=C_3,\quad I_8=1,
\tag{2.1}
\]

with deep subgroup ToM 7. Exact `Fraction` arithmetic uses base vector
`(2,5,8,8)`, one-layer \(C_3^2\) vector `(1,2,4,4)`, and deep vectors
`(1/3,2/3,1,1)`, `(0,0,1,1)`, `(1/3,2/3,1,1)`. Formal solutions are
`(7,-18)`, `(1,6)`, `(7,-18)`, so only ToM 7 is admissible. Serre IV.2
Proposition 9 selects inversion inertia ToM 140 and leaves exactly
`(D,I)=(140,140),(206,140)`, with

\[
|D_3|\in\{18,36\}.
\tag{2.2}
\]

\[
p=5:\quad
I_0\cong C_5:C_4,\quad
I_1=I_2=I_3=C_5,\quad I_4=1.
\tag{2.3}
\]

The p=5 decomposition and inertia subgroup is ToM 147. At each reflection
prime, the complete four-chart ODP/Hensel/regularity/Picard--Lefschetz bridge
selects tame root-reflection subgroup ToM 2 and makes no local \(e/f\) row
claim.

### C58-EXACT-5: fixed spaces and conductors

- exact fixed dimensions for every filtration subgroup;
- exact local Swan and Artin pairs;
- every branchwise permutation conductor integral and equal to the direct
  different.

### C58-EXACT-6: global and archimedean closure

- exact \(N(V_6),N(V_{20}),\operatorname{Disc}E,\operatorname{Disc}K\);
- exact signature `(3,12)` and `polsturm(theta36)=4`;
- separate subgroup ToM 5 and `CharacterTable("U4(2).2")` element-class
  index 17 (class size 540, centralizer 96), under CTblLib 1.3.1;
- parity \((3,3)\) and \((11,9)\).

### C58-EXACT-7: hostile independence and scope

- independent checker from primitive inputs, strict schema, and complete
  mutation suite (1149 payload leaves, 1199 rejected rebounds, 45 tests);
- exact 14-code/8-result/22-live/21-scoped inventory and self-excluding
  manifest `a1874229...`;
- four-chart singular uniqueness, unit Hessian, unique critical Hensel lift,
  critical-value congruence, valuation-one smoothing, regularity, and
  Picard--Lefschetz reflection bridge;
- exact leaf `NO_BAD_EULER_OR_ROOT_NUMBER` and all arithmetic-point
  nonclaims;
- certificate `456a4813...`, payload `fba2df...`, schema `ccbc20eb...`,
  check `64454700...`, and evidence `e374d3...`/`0e0b3f...`.

## 3. Theorem A: finite ramification support

The surface divided-discriminant bad-prime envelope is
\(\{2,3,5,181,283,997,1801,2346241,q\}\), and the `Disc(E)` exponent vector
on that envelope is \((0,46,36,18,6,18,6,18,6)\).

The prime \(2\) is unramified in \(E\) and \(K\): the zero degree-27
permutation conductor forces inertia to fix every coset of the line
stabilizer, and that stabilizer is core-free because the 27-line action is
faithful. The finite ramification support is exactly

\[
\{3,5,181,283,997,1801,2346241,q\}.
\]

## 4. Theorem B: filtered inertia

Up to \(W(E_6)\)-conjugacy, the inertia filtrations at \(3\) and \(5\) are
exactly (2.1) and (2.3). The deep p=3 subgroup is ToM 7 and inertia is ToM
140; the surviving pairs are `(D,I)=(140,140),(206,140)`. At
\(181,997,2346241\), inertia is the size-80 tame \(C_3\) subgroup ToM 6. At
\(283,1801,q\), inertia is tame root-reflection subgroup ToM 2.

The theorem identifies filtered inertia at \(3\), while leaving the
decomposition-group alternative (2.2) explicit.

## 5. Theorem C: local and global Artin conductors

The nonzero local conductor pairs are

\[
a_3(V_6,V_{20})=(11,35),
\qquad
\operatorname{Sw}_3(V_6,V_{20})=(5,18),
\]

\[
a_5(V_6,V_{20})=(7,29),
\qquad
\operatorname{Sw}_5(V_6,V_{20})=(3,12),
\]

\[
a_p(V_6,V_{20})=(6,12)
\quad(p=181,997,2346241),
\]

\[
a_p(V_6,V_{20})=(1,5)
\quad(p=283,1801,q).
\]

Consequently

\[
N(V_6)=3^{11}5^7A^6B,
\qquad
N(V_{20})=3^{35}5^{29}A^{12}B^5.
\]

## 6. Theorem D: field discriminants

\[
\operatorname{Disc}E=3^{46}5^{36}A^{18}B^6,
\]

\[
\operatorname{Disc}K
=3^{106560}5^{80352}A^{34560}B^{25920}.
\]

In particular,

\[
N(V_6)N(V_{20})=\operatorname{Disc}E.
\]

## 7. Theorem E: archimedean parity

The line field has signature

\[
(r_1,r_2)=(3,12).
\]

Complex conjugation is subgroup ToM 5. Separately, in
`CharacterTable("U4(2).2")` under CTblLib 1.3.1, it is element-class index
17 of size 540 and centralizer size 96. Moreover,

\[
V_6:(d^+,d^-)=(3,3),\qquad
V_{20}:(d^+,d^-)=(11,9).
\]

## 8. Exact proof boundary

Theorem A uses C58-EXACT-0--2. Theorem B additionally uses
C58-EXACT-3--4 and the written Serre/Picard--Lefschetz bridges. Theorem C uses
C58-EXACT-5. Theorems D--E use C58-EXACT-6. Every theorem remains subject to
C58-EXACT-7.

Theorems A--E are machine-certified at
`PREFREEZE_CODE_RESULTS_PASS`/`POSTREFRESH_PASS`. This is not a paper or
release claim.

## 9. Nonclaims

`NO_BAD_EULER_OR_ROOT_NUMBER`: C58 proves no decomposition Frobenius, bad
Euler polynomial/factor, local epsilon factor, local or global root number,
Artin holomorphy, automorphy, analytic continuation, or functional equation.
Even later resolution of \(D_3\) would not authorize those independent
claims. C58 also proves no rational-point, weak-approximation, Hasse-principle,
or Brauer--Manin statement.

## 10. Current status

Theorem statements, proof dependencies, machine tuple, independent
formal-document hostile audit, and external formal aggregate are locked.
Paper, compilation, release commit/full manifest, archive, and promotion are
pending.
