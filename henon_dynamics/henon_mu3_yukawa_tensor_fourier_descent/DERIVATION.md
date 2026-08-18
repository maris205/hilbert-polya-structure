# HCS-C61 derivation ledger

Status: **TARGET_LOCKED / IMPLEMENTATION_PENDING / PAPER_PENDING / NOT_RELEASED**

This ledger records the mathematical implications that would follow from
the locked C61-EXACT premises. It is not a transcript of completed
computations. G0--G7 are all pending, the numerical tables are target values
from nonauthoritative pilots, and no implication in this file discharges a
machine or proof obligation.

Root-authoritative target-selection report SHA-256:
**eb0a70f62427cd8b70fa35dc4153bd93d57d9ddef5ab7a349d439be3a8257026**.
It identifies the final 59,956-byte, 1,096-line report. No earlier report
digest or self-atlas aggregate hash is bound or inferred. The report binds
the target choice and lifecycle, not the truth of any G1--G6 premise.

Scope literal: **NO_BAD_EULER_OR_ROOT_NUMBER**.

## 1. Conditional-premise map

The derivations below have the following exact premise boundary:

1. G0 must bind the released P60/C60/C59 bytes, group action, roots,
   filtrations, target report, schemas, and scope.
2. G1 must reconstruct the complete three-product atlas, rather than read
   the pilot spectra.
3. G2 must establish every mixed subgroup and field dictionary entry.
4. G3 must turn formal carriers into evaluated characteristic-zero fields
   through integral product-form resolvents and complete noncollision.
5. G4 must establish the Fourier identities, stabilizers, exact seed-\(149\)
   bridge, and fixed-field diamond.
6. G5 must independently reconstruct the global arithmetic.
7. G6 must independently reconstruct every row in both retained local
   branches.
8. G7 must establish implementation independence, hostile robustness,
   sources, scope, manifests, and lifecycle discipline.

Until all eight premises pass, the formulas below are a derivation plan and
consistency audit only.

## 2. Burnside multiplication and tensor factors

For subgroups \(H,J\leq G\), the Cartesian product of transitive
\(G\)-sets decomposes as

$$
[G/H]\,[G/J]
=\sum_{HgJ\in H\backslash G/J}
\left[G/(H\cap gJg^{-1})\right].
$$

Indeed, the \(G\)-orbit through \((H,gJ)\) has stabilizer
\(H\cap gJg^{-1}\), and the orbits are indexed by the double cosets.
Consequently, for \(F_H=K^H\) and \(F_J=K^J\),

$$
F_H\otimes_{\mathbf Q}F_J
\cong\prod_{HgJ\in H\backslash G/J}
K^{H\cap gJg^{-1}}.
$$

The second formula is the finite étale/tensor version of the first and is a
classical double-coset correspondence. Its general form is not a C61
novelty claim.

For the C61 pair, every index is \(320\). Thus each product has dimension

$$
|G/H_a|\,|G/H_b|=320^2=102400.
$$

The locked self degree sum is

$$
2(320)+2(960)+1920+2(5760)+2(8640)
+17280+2(25920)=102400.
$$

The locked mixed degree sum is

$$
640+2(960)+1920+2(2880)+2(2880)+2(8640)
+17280+51840=102400.
$$

The mixed raw-position count and factor count are separately

$$
1+3+3+9+9+27+27+81=160,
$$

$$
1+2+1+2+2+2+1+1=12.
$$

Hence the numbers \(160\), \(12\), and \(8\) refer, respectively, to
conjugate positions, double-coset factors, and
\(\mathbf Q\)-isomorphism types. None can be substituted for another.

## 3. Linearization and the proposed Burnside defect

Let \(\ell:B(G)\to R_{\mathbf Q}(G)\) be rational linearization. It is a
ring homomorphism. The released Gassmann relation is

$$
\ell(x)=\ell(y).
$$

Multiplicativity therefore gives

$$
\ell(x^2)=\ell(x)\ell(x)
=\ell(x)\ell(y)=\ell(y)\ell(y)=\ell(y^2).
$$

Equivalently,

$$
x(x-y),\qquad y(x-y),\qquad (x+y)(x-y)
$$

lie in \(\ker\ell\). To show that they are nonzero, G1 must establish that
\(x^2,xy,y^2\) are pairwise distinct in \(B(G)\).

The mixed spectrum differs from either self spectrum by degrees, so those
two separations follow once the decompositions are certified. The two self
spectra have identical degree multisets. Their separation instead uses the
degree-\(320\) diagonal factors \(K^{H_+}\) and \(K^{H_-}\): G1 must prove
that the core-free stabilizers \(H_+\) and \(H_-\) are nonconjugate, so the
fields and corresponding transitive \(G\)-sets are nonisomorphic. Equal
degree lists alone do not prove this step.

Applying Artin formalism to the equal permutation characters yields equality
of the products of Dedekind zeta functions of the simple factors. This
formal consequence neither identifies the finite étale algebras nor supplies
bad-prime Euler data.

## 4. Composita, intersections, and isomorphism types

Within a finite Galois extension \(K/\mathbf Q\), Galois correspondence gives
for \(H,J\leq G\)

$$
K^H K^J=K^{H\cap J},\qquad
K^H\cap K^J=K^{\langle H,J\rangle}.
$$

Substituting \(J=gH_bg^{-1}\) gives

$$
F_aF_b^g=K^{H_a\cap gH_bg^{-1}}=K^{I_{ab,g}},
$$

$$
F_a\cap F_b^g
=K^{\langle H_a,gH_bg^{-1}\rangle}=K^{J_{ab,g}}.
$$

These equalities explain both columns of the atlas, but G2 must still
reconstruct the embedded subgroups.

For \(I\leq G\), the normal closure of \(K^I/\mathbf Q\) inside \(K\) is
fixed by \(\operatorname{Core}_G(I)\). Thus core-freeness gives normal
closure \(K\). Suppose two core-free atlas fields \(K^{I_1}\) and
\(K^{I_2}\) are \(\mathbf Q\)-isomorphic. Extend the isomorphism to an
algebraic closure of \(\mathbf Q\). It sends the normal closure of the first
field to the normal closure of the second, hence restricts to an element of
\(G=\operatorname{Aut}_{\mathbf Q}(K)\). That element conjugates \(I_1\)
to \(I_2\). Therefore, among these core-free fields,

$$
K^{I_1}\cong_{\mathbf Q}K^{I_2}
\quad\Longleftrightarrow\quad
I_1\text{ and }I_2\text{ are }G\text{-conjugate}.
$$

The reverse implication follows directly by conjugating fixed fields.
This is the required bridge from subgroup conjugacy classes to the proposed
\(\mathbf Q\)-isomorphism grouping. Hashes and ToM rows are only checks.

For mixed type \(1\), the pending equality
\(I_{+-,148}=H_+\cap H_3=J\) gives \(E=L\), while its join is \(N\), giving
base \(M\). For mixed type \(8\), \(I=1\), so \(E=K\). The certified degree
list would make these uniquely minimal and maximal among the twelve mixed
factors, and nowhere else.

## 5. Correct P3 conjugacy calculation

Let \(J_{++,69}\) be the plus-self degree-\(1920\) join and
\(J_{--,86}\) the embedded minus-self degree-\(1920\) join. Their pilot
complete-element hashes are \(263f\ldots\) and \(a426\ldots\), respectively,
but different embedded hashes do not imply nonconjugacy.

The exact future calculation must use

$$
w=[25,22,23,27,24,26,9,13,20,16,19,7,11,8,10,15,12,14,18,21,17,4,1,2,6,3,5]
$$

and verify, element by element,

$$
wJ_{--,86}w^{-1}=J_{++,69}.
$$

The conjugated complete-element hash is then the plus-self hash

$$
\mathtt{263f31237e6f5111f76fd3470b6936a1a314020255c22eab55cece395c2adeb5}.
$$

Thus both self joins are in P3. The mixed type-\(2\) joins are also in P3.
G1 must separately prove that this class is nonconjugate to the mixed
type-\(3\) Fourier join

$$
T_+,\qquad
\operatorname{SHA256}(T_+)
=\mathtt{55d7f2df8abc6709489e9bf632c45d620b9b570e6a295a82ee6f941c24c2c6bc}.
$$

The latter is P6. In particular, the minus embedded hash
\(a426\ldots\) is not evidence for a third order-\(1296\) conjugacy class.

## 6. Fourier decomposition and orbit rank

Write \(V=N/J\cong V_4\). Its four rational characters are the trivial
character and \(\chi_+,\chi_0,\chi_3\), whose kernels are the three
order-two subgroups \(H_+/J,H_0/J,H_3/J\).

For a fixed canonical representative \(q\) of each coset in \(V\), define

$$
R_\chi=\sum_{q\in V}\chi(q)\,q(\lambda).
$$

The trivial component is

$$
\operatorname{Tr}=\sum_{q\in V}q(\lambda).
$$

Fourier inversion in the group algebra \(\mathbf Q[V]\) gives

$$
4\lambda=\operatorname{Tr}+R_++R_0+R_3.
$$

The pending sparse identity \(R_0=0\), followed by the pending exact
coefficient divisions

$$
r_+=R_+/2,\qquad r_3=R_3/4,
$$

would give

$$
4\lambda=\operatorname{Tr}+2r_++4r_3.
$$

The three surviving terms lie in pairwise distinct character eigenspaces.
The trace carrier has \(243\) terms and target SHA-256

$$
\mathtt{a7398d36cea0c83ace64466a579e21666731d1e3c8e8641df4ce036c79de2bd7}.
$$

At the split-prime identity embedding, the pending evaluated witnesses are

$$
\operatorname{Tr}=581739,\qquad
r_+=643771,\qquad r_3=119649.
$$

All are nonzero modulo \(692717\), hence their characteristic-zero
evaluations are nonzero. The three rational idempotents then show that the
\(M\)-span of the \(V\)-orbit of \(\lambda\) has dimension exactly \(3\).

C60 gives \(\operatorname{Stab}_G(\lambda)=J\). Hence the orbit under
\(N/J\) has four elements and \(\lambda\) is primitive for \(L/M\).
A normal-basis generator for the degree-\(4\) Galois extension would have
four linearly independent conjugates. Rank \(3\) therefore excludes
normal-basis status. It says nothing about normal integral bases.

## 7. Kummer carriers

Define

$$
r_0=r_+r_3,\qquad \delta_i=r_i^2.
$$

Because \(\chi_+\chi_3=\chi_0\), \(r_0\) lies in the third nontrivial
eigenspace even though the direct Fourier projection \(R_0\) vanishes. The
two objects are not interchangeable.

The polynomial-ring identity is

$$
\delta_0=r_0^2=(r_+r_3)^2
=r_+^2r_3^2=\delta_+\delta_3.
$$

Consequently, after G3 proves that the evaluated carriers have the expected
degrees,

$$
[\delta_0]=[\delta_+][\delta_3]
\quad\text{in }M^\times/M^{\times2}.
$$

The equality can be certified by a factorized expression DAG; expanding
\(r_0^2\) is mathematically unnecessary.

## 8. From formal stabilizers to fields

Let \(\theta\) be an integral carrier with formal stabilizer \(H\).
If its \([G:H]\) formal conjugates have pairwise distinct reductions at one
common good prime, equality of two characteristic-zero conjugates would
force equality after reduction, a contradiction. Thus the evaluated
stabilizer remains \(H\), and

$$
\mathbf Q(\theta)=K^H.
$$

This lemma is the required passage from sparse formal carriers to fields.
It explains why the complete distinct counts

$$
80,40,320,160,320,160
$$

for \(r_+,\delta_+,r_3,\delta_3,r_0,\delta_0\) cannot be replaced by a
formal-orbit calculation.

In the formal polynomial domain,

$$
g(r)^2=r^2\Longrightarrow(g(r)-r)(g(r)+r)=0
\Longrightarrow g(r)=\pm r.
$$

Therefore the formal stabilizer of \(r^2\) is the sign stabilizer of \(r\).
Evaluation still requires the preceding noncollision lemma.

## 9. Seed-\(149\) bridge and fixed-field diamond

The canonical mixed representative is

$$
g_{149}=[1,3,13,14,19,6,27,10,9,7,24,17,16,12,22,2,4,21,5,20,15,18,11,26,25,23,8].
$$

G4 must reconstruct

$$
T_{\mathrm{mix}}
=\langle H_+,g_{149}H_-g_{149}^{-1}\rangle
$$

and prove exact embedded equality \(T_{\mathrm{mix}}=T_+\), where
\(T_+=\operatorname{Stab}_G(\delta_+)\). The equality identifies the
Fourier field with the P6 mixed base; it cannot be derived from the common
order \(1296\).

Assume the pending subgroup identities

$$
S_+\cap N=H_+,\qquad
\langle S_+,N\rangle=T_+.
$$

Set

$$
A=K^{T_+},\qquad B=K^{S_+},\qquad
M=K^N,\qquad F_+=K^{H_+}.
$$

Orders give degrees \(40,80,160,320\). The fixed-field formulas of section
4 give

$$
B\cap M
=K^{\langle S_+,N\rangle}=K^{T_+}=A,
$$

$$
BM=K^{S_+\cap N}=K^{H_+}=F_+.
$$

Thus \(F_+/M\) is the base change of \(B/A\). If
\(N_G(S_+)=T_+\), then \(S_+\triangleleft T_+\) and

$$
\operatorname{Gal}(B/A)=T_+/S_+\cong C_2.
$$

The normalizer formulas

$$
\operatorname{Aut}_{\mathbf Q}(K^H)\cong N_G(H)/H
$$

give \(\operatorname{Aut}_{\mathbf Q}(A)=1\) from
\(N_G(T_+)=T_+\), and
\(\operatorname{Aut}_{\mathbf Q}(B)\cong C_2\) from
\(N_G(S_+)=T_+\). Trivial cores give normal closure \(K\).

## 10. Signatures and conductor-discriminant exponents

For a degree-\(n\) coset action and complex-conjugation orbit count
\(o_\infty\),

$$
r_1+2r_2=n,\qquad r_1+r_2=o_\infty,
$$

so

$$
r_1=2o_\infty-n,\qquad r_2=n-o_\infty.
$$

For orbit counts ordered as
\((I_3,P_3,Q_3,I_5,P_5,C_3,C_2,C_\infty)\), the inherited conductor
formulas are

$$
v_3=(n-o_{I_3})+\frac{n-o_{P_3}}2+(n-o_{Q_3}),
$$

$$
v_5=(n-o_{I_5})+\frac34(n-o_{P_5}),\qquad
v_{\Pi_A}=n-o_{C_3},\qquad
v_{\Pi_B}=n-o_{C_2}.
$$

For \(A\), the target orbit vector

$$
(7,8,14,3,8,16,25,23)
$$

gives

$$
(v_3,v_5,v_{\Pi_A},v_{\Pi_B})=(75,61,24,15),
$$

$$
(r_1,r_2)=(6,17).
$$

Because \(r_2=17\), its discriminant sign is negative.

For \(B\), the target vector

$$
(10,16,28,6,16,32,50,42)
$$

gives

$$
(154,122,48,30),\qquad (r_1,r_2)=(4,38),
$$

and a positive sign. G5 must reconstruct these orbit vectors independently;
this substitution is not evidence.

## 11. Relative discriminant vectors

For \(E/C\),

$$
\operatorname{Disc}(E/\mathbf Q)
=\operatorname{Disc}(C/\mathbf Q)^{[E:C]}
N_{C/\mathbf Q}(\mathfrak d_{E/C}).
$$

Subtracting \([E:C]\) times the base exponent vector gives the relative
norm vector.

For the nontrivial mixed bases this yields:

$$
\begin{aligned}
E_{640}/M:\;&
(1264,992,384,320)-4(308,248,96,80)\\
&=(32,0,0,0),\\
E_{960}/C_2:\;&
(1944,1488,624,480)-24(68,62,18,20)\\
&=(312,0,192,0),\\
E_{1920}/A:\;&
(3808,2976,1152,960)-48(75,61,24,15)\\
&=(208,48,0,240).
\end{aligned}
$$

For the Fourier diamond:

$$
\begin{aligned}
B/A:\;&(154,122,48,30)-2(75,61,24,15)
=(4,0,0,0),\\
M/A:\;&(308,248,96,80)-4(75,61,24,15)
=(8,4,0,20),\\
F_+/B:\;&(624,496,192,160)-4(154,122,48,30)
=(8,8,0,40),\\
F_+/A:\;&(624,496,192,160)-8(75,61,24,15)
=(24,8,0,40),\\
F_+/M:\;&(624,496,192,160)-2(308,248,96,80)
=(8,0,0,0).
\end{aligned}
$$

The two tower routes reconcile because

$$
2(8,4,0,20)+(8,0,0,0)=(24,8,0,40),
$$

$$
4(4,0,0,0)+(8,8,0,40)=(24,8,0,40).
$$

This arithmetic operates on norms of relative discriminant ideals. It does
not construct prime ideals in \(A\) or \(B\).

## 12. Both \(D_3\) branches and the ideal laws

For a relative local row \((g,e,f,d)\), put

$$
a=gfd.
$$

G6 must reconstruct the rows above each base prime in both ToM \(140\) and
ToM \(206\). If for every base prime

$$
\min(a_+,a_3)=0,\qquad
a_0=a_++a_3,\qquad
a_L=2a_0,
$$

then equality of valuations at every prime gives

$$
(\mathfrak d_{F_+/M},\mathfrak d_{F_3/M})=1,
$$

$$
\mathfrak d_{F_0/M}
=\mathfrak d_{F_+/M}\mathfrak d_{F_3/M},
$$

$$
\mathfrak d_{L/M}
=\mathfrak d_{F_+/M}\mathfrak d_{F_0/M}
\mathfrak d_{F_3/M}
=\mathfrak d_{F_0/M}^{\,2}.
$$

The branch populations

$$
(H_+,H_3,\mathrm{trivial},H_0)=(8,8,6,0)
$$

and

$$
(4,4,3,0)
$$

for ToM \(140\) and ToM \(206\) have the same residue-degree masses
\((8,8,6,0)\) and the same relative norm exponents
\((8,16,8,32)\). Agreement of totals does not identify the two
decomposition branches and does not authorize choosing one.

The archimedean calculation is separate: the pending \(H_+:8,H_3:8,H_0:0\)
type count gives complementary real splitting for \(F_+\) and \(F_3\).
It is not inferred from the finite-prime rows.

## 13. Derivation boundary

The displayed substitutions are internally consistent with the locked
targets, but they do not establish any target datum. No pilot script, pilot
JSON, target scan, source audit, or this ledger can substitute for G0--G7.

**NO_BAD_EULER_OR_ROOT_NUMBER**. The conductor and local formulas authorize
only the stated conditional signature, discriminant, relative-ideal, and
local-row conclusions. They authorize no decomposition Frobenius, bad Euler,
epsilon, root-number, holomorphy, automorphy, functional-equation, or branch
selection statement.

The lifecycle remains
**TARGET_LOCKED / IMPLEMENTATION_PENDING / PAPER_PENDING / NOT_RELEASED**.
No proof completion, paper completion, promotion, or release is claimed.
