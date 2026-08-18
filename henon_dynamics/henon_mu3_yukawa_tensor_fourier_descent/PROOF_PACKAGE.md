# HCS-C61 proof package

## Claim

The locked C61 claim is conditional:

> If C61-EXACT-0 through C61-EXACT-7 are independently reconstructed and
> pass exactly as specified in THEOREM_PACKAGE.md, then the three tensor
> algebras attached to the released \(W(E_6)\) Gassmann twins have the
> stated complete decompositions, are pairwise nonisomorphic despite equal
> rational linearizations and zeta products, the mixed tensor has the stated
> twelve factors and eight \(\mathbf Q\)-isomorphism types, and the
> normalized Fourier carrier identifies the distinct P6 degree-\(40\) mixed
> base with the stated fixed-field diamond, global arithmetic, both retained
> \(D_3\) branches, and local ideal complementarity.

This file supplies a proof-obligation map and the conditional mathematical
bridges. It does not assert that the antecedent has been discharged.

Scope literal: **NO_BAD_EULER_OR_ROOT_NUMBER**.

## Status

**TARGET_LOCKED / IMPLEMENTATION_PENDING / PAPER_PENDING / NOT_RELEASED**

Proof completion is pending. G0--G7 have no C61 machine PASS, there is no
C61 certificate or independent checker report, and no hostile formal audit
has accepted the theorem. The claim is therefore not currently available as
an unconditional theorem.

Root-authoritative target-selection report SHA-256:
**eb0a70f62427cd8b70fa35dc4153bd93d57d9ddef5ab7a349d439be3a8257026**.
It identifies the final 59,956-byte, 1,096-line report. This proof binds no
earlier report digest and no self-atlas aggregate hash. The report is
target-lock authority only; it cannot discharge a theorem premise.

All selection scans, tensor tables, arithmetic calculations, bridge
experiments, and novelty searches supplied before implementation are
nonauthoritative pilots.

## Assumptions

The conditional proof uses exactly these pending assumptions.

1. **G0.** The future evidence byte-rebinds released P60 commit
   \(fe1217810b72840619efdf40a2af31b8b80d96f6\), the released C60/C59
   authority, target report, group action, roots, split prime, filtrations,
   manifests, Route, Batch, guard, schemas, and scope.
2. **G1.** Independent lanes reconstruct every row of all three
   double-coset atlases, their complete intersection and join groups,
   conjugators, cores, normalizers, automorphism orders, multiplicities,
   unified \(\mathbf Q\)-types, degree sums, and permutation characters.
3. **G2.** The lanes reconstruct the \(160\) mixed positions, \(12\)
   factors, and \(8\) field types, prove the fixed-field dictionary and
   core-free common-normal-closure criterion, and identify only the mixed
   minimum \(L/M\) and maximum \(K\).
4. **G3.** Source-owned integral carriers, product-form resolvents, formal
   stabilizers, and complete split-prime noncollision establish the
   advertised characteristic-zero fields and degrees.
5. **G4.** Exact sparse identities establish \(R_0=0\), the normalized
   Fourier decomposition, rank \(3\), the Kummer product, the carrier
   stabilizers, the seed-\(149\) embedded equality, and every subgroup
   identity in the \(A/B/M/F_+\) diamond.
6. **G5.** Independent orbit/conductor lanes establish every global
   signature, signed discriminant, support, and relative norm vector in the
   theorem target.
7. **G6.** Independent double-coset/local lanes establish every uncollected
   row, degree total, factor total, different total, relative tower check,
   ideal valuation, tame flag, and archimedean type in both ToM \(140\) and
   ToM \(206\).
8. **G7.** Producer/checker mathematical code is independent, strict I/O and
   schemas are fail-closed, deterministic replay and all hostile mutations
   pass, source positioning is refreshed, and all scope and lifecycle leaves
   remain false.

No target value from a pilot is an additional assumption. Each must be
reconstructed under the appropriate gate.

## Notation

- \(K/\mathbf Q\) is the released common normal extension and
  \(G=\operatorname{Gal}(K/\mathbf Q)=W(E_6)\).
- \(H_+,H_-\leq G\) are the released nonconjugate, order-\(162\),
  index-\(320\) Gassmann subgroups.
- \(F_\pm=K^{H_\pm}\),
  \(x=[G/H_+]\), and \(y=[G/H_-]\).
- \(\mathscr T_{ab}=F_a\otimes_{\mathbf Q}F_b\).
- For a double-coset representative \(g\),
  \(I_{ab,g}=H_a\cap gH_bg^{-1}\) and
  \(J_{ab,g}=\langle H_a,gH_bg^{-1}\rangle\).
- \(N,J,H_0,H_3,M,F_0,F_3,L,\lambda\) retain their released C60 meanings,
  with \(N/J\cong V_4\), \(M=K^N\), and \(L=K^J\).
- \(R_+,R_0,R_3\) are raw nontrivial Fourier components;
  \(r_+=R_+/2\), \(r_3=R_3/4\), and \(r_0=r_+r_3\).
- \(S_+=\operatorname{Stab}_G(r_+)\),
  \(T_+=\operatorname{Stab}_G(r_+^2)\),
  \(A=K^{T_+}\), and \(B=K^{S_+}\).

## Proof Strategy

First use the classical double-coset orbit formula to translate the pending
subgroup atlas into finite étale tensor factors. Use core-freeness and the
common normal closure to convert subgroup conjugacy into
\(\mathbf Q\)-field isomorphism classes. Then combine the released Gassmann
relation with multiplicativity of rational linearization and use the
certified transitive decompositions to show that the Burnside products are
nevertheless distinct.

For the bridge, use the four rational \(V_4\) idempotents on the released
primitive carrier, distinguish the vanished direct component from the
product Kummer carrier, and use complete noncollision to preserve formal
stabilizers after evaluation. Exact equality of the seed-\(149\) join and
the sign stabilizer then identifies the Fourier field with P6. Galois
correspondence proves the diamond.

Finally, derive signatures and discriminants from independently certified
orbit counts, use discriminant towers for relative norm vectors, and use
prime-by-prime valuations in both local branches for the ideal laws.

## Dependency Map

1. Tensor factorization depends on G0/G1 and the double-coset orbit lemma.
2. The mixed \(12\to8\) grouping depends on G1/G2, core-freeness, and the
   extension-of-isomorphism lemma.
3. Pairwise Burnside and finite étale nonisomorphism depends on the complete
   G1 type decomposition, not merely the degree spectra.
4. Zeta-product equality depends on the released Gassmann character equality
   and classical Artin formalism, not on any local bad-prime calculation.
5. The unique \(L\) and \(K\) identifications depend on G0/G2 and are
   restricted to the twelve mixed factors.
6. Fourier rank and primitive-but-nonnormal status depend on G0/G4 and
   nonvanishing of three distinct eigenspace projections.
7. The evaluated fields \(A,B,F_0,F_3\) depend on G3/G4 and complete
   split-prime noncollision.
8. The P6 identification depends on exact embedded equality at seed \(149\);
   order, degree, hash, ToM row, abstract isomorphism, or conjugacy alone is
   insufficient.
9. The fixed-field diamond depends on G4 subgroup intersections, joins,
   cores, and normalizers.
10. Global arithmetic depends on G5; relative vectors additionally use the
    discriminant tower formula.
11. The ideal complementarity depends on every prime row from both branches
    under G6; agreement of collected totals is insufficient.
12. Any theorem-level use of Steps 1--11 also depends on G7 and the literal
    scope firewall.

## Conditional Proof

### Step 1. Tensor products are controlled by double cosets

Let \(H,J\leq G\). The diagonal \(G\)-action on
\((G/H)\times(G/J)\) has an orbit through \((H,gJ)\) with stabilizer
\(H\cap gJg^{-1}\). Two such points lie in the same orbit exactly when
their representatives lie in the same double coset in \(H\backslash G/J\).
Therefore

$$
(G/H)\times(G/J)
\cong\bigsqcup_{HgJ\in H\backslash G/J}
G/(H\cap gJg^{-1}).
$$

Passing to the associated finite étale \(\mathbf Q\)-algebras gives

$$
K^H\otimes_{\mathbf Q}K^J
\cong\prod_{HgJ\in H\backslash G/J}
K^{H\cap gJg^{-1}}.
$$

Assumption G1 would instantiate this formula with exactly twelve factors in
each of the \(++,+-,--\) lanes and with the three degree multisets in
THEOREM_PACKAGE.md. Each certified sum is \(102400\), as required by the
dimension \(320^2\).

### Step 2. The fixed fields are the stated composita and intersections

For subgroups \(H,J\leq G\), fixed-field Galois correspondence gives

$$
K^HK^J=K^{H\cap J},\qquad
K^H\cap K^J=K^{\langle H,J\rangle}.
$$

Applying this with \(J=gH_bg^{-1}\) yields

$$
K^{I_{ab,g}}=F_aF_b^g,\qquad
K^{J_{ab,g}}=F_a\cap F_b^g.
$$

Thus, conditional on G2's exact embedded subgroup reconstruction, every
factor and base in the atlas has the advertised field meaning.

### Step 3. Core-free subgroup classes determine the field types

The normal closure of \(K^I/\mathbf Q\) inside \(K\) is
\(K^{\operatorname{Core}_G(I)}\). G2 is required to give trivial core for
every mixed \(I\), so every mixed factor has normal closure \(K\).

If \(\varphi:K^{I_1}\to K^{I_2}\) is a \(\mathbf Q\)-isomorphism, extend it
to an automorphism of an algebraic closure. Since it sends normal closure to
normal closure, it restricts to an element \(g\in G\). For
\(\alpha\in K^{I_1}\) and \(h\in I_1\),

$$
(ghg^{-1})(g\alpha)=g(h\alpha)=g\alpha,
$$

so \(gI_1g^{-1}\) fixes \(K^{I_2}\); equality of degrees forces
\(gI_1g^{-1}=I_2\). Conversely, a conjugator sends one fixed field
isomorphically to the other.

Therefore G2's certified eight conjugacy classes are exactly the eight mixed
\(\mathbf Q\)-isomorphism types. Serialized subgroup hashes are not used as
the implication.

### Step 4. The three Burnside products are pairwise distinct

G1's mixed degree multiset contains degrees \(640,2880,51840\), which are
absent from either self degree multiset. Hence \(xy\ne x^2\) and
\(xy\ne y^2\) in \(B(G)\).

The two self degree multisets agree, so a different argument is required.
The \(++\) decomposition contains two diagonal degree-\(320\) factors of
\(H_+\)-type, whereas the \(--\) decomposition contains two of
\(H_-\)-type. The released pair is nonconjugate and core-free. By Step 3,
the two degree-\(320\) fields are not \(\mathbf Q\)-isomorphic and the
transitive \(G\)-sets are not isomorphic. G1's complete type multiplicities
then give \(x^2\ne y^2\).

Thus, conditional on G1, \(x^2,xy,y^2\) are pairwise distinct.

### Step 5. Linearizations and zeta products agree

Rational linearization

$$
\ell:B(G)\longrightarrow R_{\mathbf Q}(G)
$$

is a ring homomorphism. The released Gassmann equality
\(\ell(x)=\ell(y)\) gives

$$
\ell(x^2)=\ell(xy)=\ell(y^2).
$$

Combined with Step 4, this makes

$$
x(x-y),\qquad y(x-y),\qquad (x+y)(x-y)
$$

nonzero kernel elements.

For \(H\leq G\), the Dedekind zeta function of \(K^H\) is the Artin
\(L\)-function attached to \(\operatorname{Ind}_H^G\mathbf1\).
Multiplicativity on direct sums, applied to the transitive decompositions,
gives equality of the three products of Dedekind zeta functions. This is a
character-formal identity and does not assert finite étale algebra
isomorphism or compute forbidden bad Euler factors.

### Step 6. The mixed minimum and maximum have the stated identities

In mixed type \(1\), G2 must establish

$$
I_{+-,148}=J,\qquad J_{+-,148}=N.
$$

Step 2 then gives factor \(K^J=L\) and base \(K^N=M\). Its degree \(640\)
is strictly smaller than every other mixed factor degree. In type \(8\),
G2 must establish \(I=1\), giving factor \(K\) of degree \(51840\), strictly
larger than every other mixed factor. Hence these are unique only inside the
listed twelve-factor mixed decomposition.

### Step 7. The P3 correction is part of the proof, not metadata

Let the future G1 reconstruction form the plus-self and minus-self
degree-\(1920\) joins \(J_{++,69}\) and \(J_{--,86}\). It must verify with

$$
w=[25,22,23,27,24,26,9,13,20,16,19,7,11,8,10,15,12,14,18,21,17,4,1,2,6,3,5]
$$

that

$$
wJ_{--,86}w^{-1}=J_{++,69}
$$

as equality of complete element sets. Thus the embedded hashes
\(263f\ldots\) and \(a426\ldots\) represent conjugate copies of the same P3
class.

G1/G4 must also prove that P3 is nonconjugate to the mixed seed-\(149\)
Fourier join \(T_+\), whose complete embedded hash target is

$$
\mathtt{55d7f2df8abc6709489e9bf632c45d620b9b570e6a295a82ee6f941c24c2c6bc}.
$$

This latter class is P6. Hence the Fourier base is not the self-product P3
base.

### Step 8. Fourier inversion gives a rank-three orbit

Let \(V=N/J\cong V_4\). For each rational character \(\chi\), put

$$
R_\chi=\sum_{q\in V}\chi(q)\,q(\lambda).
$$

The character orthogonality relations give Fourier inversion

$$
4\lambda=\operatorname{Tr}+R_++R_0+R_3.
$$

Assumption G4 supplies the coefficientwise sparse identity \(R_0=0\) and
the exact divisions

$$
R_+=2r_+,\qquad R_3=4r_3.
$$

Hence

$$
4\lambda=\operatorname{Tr}+2r_++4r_3.
$$

The trace, \(r_+\), and \(r_3\) lie in three distinct rational character
eigenspaces. The trace carrier has \(243\) terms and target SHA-256

$$
\mathtt{a7398d36cea0c83ace64466a579e21666731d1e3c8e8641df4ce036c79de2bd7}.
$$

G4 must reproduce the split-prime identity values

$$
\operatorname{Tr}=581739,\qquad
r_+=643771,\qquad r_3=119649.
$$

They are all nonzero modulo \(692717\), so the corresponding
characteristic-zero components are nonzero. The three idempotent projections
are therefore linearly independent over \(M\). The fourth projection
vanishes. Hence the \(M\)-span of the four \(V\)-conjugates of
\(\lambda\) has dimension exactly \(3\).

C60 gives \(\operatorname{Stab}_G(\lambda)=J\); thus \(\lambda\) has four
conjugates over \(M\) and generates \(L/M\). Rank \(3<4\) means those
conjugates are not a basis of \(L\) over \(M\), so \(\lambda\) is not a
normal-basis generator.

### Step 9. The Kummer product is distinct from the vanished component

G4 defines

$$
r_0=r_+r_3,\qquad \delta_i=r_i^2.
$$

Then, in the formal polynomial domain,

$$
\delta_0=(r_+r_3)^2=\delta_+\delta_3.
$$

Since the product character is \(\chi_0\), the constructed \(r_0\) lies in
the \(H_0\)-character eigenspace. It is not the direct projection
\(R_0\), which is zero. After G3 establishes evaluated degrees, the identity
gives

$$
[\delta_0]=[\delta_+][\delta_3]
\quad\text{in }M^\times/M^{\times2},
$$

and

$$
F_3=M(r_3),\qquad F_0=M(r_0).
$$

No expansion of \(\delta_0\) is needed.

### Step 10. Complete noncollision preserves evaluated stabilizers

Let \(\theta\) be an integral formal carrier fixed by \(H\). It has at most
\([G:H]\) characteristic-zero conjugates. If G3 supplies
\([G:H]\) pairwise distinct reductions of the formal orbit at a common good
prime, no two characteristic-zero conjugates can coincide. Hence it has
exactly \([G:H]\) conjugates and

$$
\operatorname{Stab}_G(\theta)=H,\qquad
\mathbf Q(\theta)=K^H.
$$

Applying this to \(r_+,\delta_+,r_3,\delta_3,r_0,\delta_0\), with the exact
distinct counts \(80,40,320,160,320,160\), gives the advertised evaluated
fields. Formal stabilizer hashes without G3 do not justify this step.

### Step 11. Exact seed-\(149\) equality identifies the Fourier base

G4 must construct the canonical representative

$$
g_{149}=[1,3,13,14,19,6,27,10,9,7,24,17,16,12,22,2,4,21,5,20,15,18,11,26,25,23,8]
$$

and verify

$$
T_+=\langle H_+,g_{149}H_-g_{149}^{-1}\rangle
$$

as equality of complete embedded element sets. By Step 2, the mixed base is

$$
K^{T_+}=F_+\cap F_-^{g_{149}}.
$$

By Step 10, the same fixed field is

$$
K^{T_+}=\mathbf Q(\delta_+)=A.
$$

Thus the degree-\(40\) Fourier field is exactly the P6 base of the unique
mixed degree-\(1920\) factor. Neither order \(1296\) nor field degree \(40\)
would distinguish it from P3.

### Step 12. Galois correspondence proves the \(A/B/M/F_+\) diamond

Assumption G4 gives

$$
S_+\cap N=H_+,\qquad
\langle S_+,N\rangle=T_+.
$$

With \(A=K^{T_+}\), \(B=K^{S_+}\), \(M=K^N\), and
\(F_+=K^{H_+}\), Step 2 yields

$$
B\cap M=K^{\langle S_+,N\rangle}=A,
$$

$$
BM=K^{S_+\cap N}=F_+.
$$

The subgroup orders yield degrees \(40,80,160,320\). The pending normalizer
identities

$$
N_G(S_+)=T_+,\qquad N_G(T_+)=T_+
$$

give

$$
\operatorname{Aut}_{\mathbf Q}(B)\cong T_+/S_+\cong C_2,
\qquad
\operatorname{Aut}_{\mathbf Q}(A)=1.
$$

Trivial cores give common normal closure \(K\). This also proves the required
negative statements

$$
\mathbf Q(r_+)=B\ne F_+,\qquad
\mathbf Q(\delta_+)=A\ne M.
$$

### Step 13. Global arithmetic follows from orbit counts

For a degree-\(n\) coset action, if \(o_\infty\) is the complex-conjugation
orbit count, then

$$
r_1=2o_\infty-n,\qquad r_2=n-o_\infty.
$$

For the released inertia/filtration classes, G5 must independently supply
the orbit counts entering

$$
v_3=(n-o_{I_3})+\frac{n-o_{P_3}}2+(n-o_{Q_3}),
$$

$$
v_5=(n-o_{I_5})+\frac34(n-o_{P_5}),\qquad
v_{\Pi_A}=n-o_{C_3},\qquad v_{\Pi_B}=n-o_{C_2}.
$$

Direct substitution then gives every signature, discriminant sign, and
absolute exponent vector in THEOREM_PACKAGE.md. In particular, the pending
vectors for \(A\) and \(B\) give

$$
\operatorname{Disc}(A)
=-3^{75}5^{61}\Pi_A^{24}\Pi_B^{15},
$$

$$
\operatorname{Disc}(B)
=+3^{154}5^{122}\Pi_A^{48}\Pi_B^{30}.
$$

This step is conditional on the independently reconstructed orbit counts and
exact inherited support; the displayed formulas cannot verify themselves.

### Step 14. Relative discriminants and the two diamond routes

For \(E/C\),

$$
\operatorname{Disc}(E/\mathbf Q)
=\operatorname{Disc}(C/\mathbf Q)^{[E:C]}
N_{C/\mathbf Q}(\mathfrak d_{E/C}).
$$

Subtracting scaled base exponent vectors gives the mixed relative vectors and

$$
\begin{aligned}
N(\mathfrak d_{B/A})&=(4,0,0,0),\\
N(\mathfrak d_{M/A})&=(8,4,0,20),\\
N(\mathfrak d_{F_+/B})&=(8,8,0,40),\\
N(\mathfrak d_{F_+/A})&=(24,8,0,40),\\
N(\mathfrak d_{F_+/M})&=(8,0,0,0).
\end{aligned}
$$

The two tower calculations agree:

$$
2(8,4,0,20)+(8,0,0,0)=(24,8,0,40),
$$

$$
4(4,0,0,0)+(8,8,0,40)=(24,8,0,40).
$$

These equalities check G5 outputs but do not construct the underlying
relative ideals.

### Step 15. Both local branches imply the ideal complementarity

For each base prime and a relative row \((g,e,f,d)\), let \(a=gfd\).
Assumption G6 supplies every row under both ToM \(140\) and ToM \(206\) and
checks

$$
\min(a_+,a_3)=0,\qquad
a_0=a_++a_3,\qquad
a_L=2a_0.
$$

The first equality says that no prime of \(M\) divides both
\(\mathfrak d_{F_+/M}\) and \(\mathfrak d_{F_3/M}\). Equality of every
prime valuation in the second and third identities gives

$$
(\mathfrak d_{F_+/M},\mathfrak d_{F_3/M})=1,
$$

$$
\mathfrak d_{F_0/M}
=\mathfrak d_{F_+/M}\mathfrak d_{F_3/M},
$$

$$
\mathfrak d_{L/M}
=\mathfrak d_{F_0/M}^{\,2}.
$$

G6 must obtain this separately in both branches. The branch populations are
\((8,8,6,0)\) and \((4,4,3,0)\) for
\((H_+,H_3,\mathrm{trivial},H_0)\), with common residue-degree masses
\((8,8,6,0)\). Every ramified relative row has \(e=2,d=1\), so it is tame.
No branch selection or converse local-field classification follows.

The infinity calculation is independent of the finite rows. Its
\(H_+:8,H_3:8,H_0:0\) types give complementary real splitting and
\(\mathbf C\times\mathbf C\) over every real place in \(L/M\).

### Step 16. Authority and scope prevent closure at the present stage

Steps 1--15 show that the written conclusions follow from the listed exact
premises. They do not show that the premises hold. G0--G7 are pending, and
G7 has not yet established the independent authority chain or hostile
formal audit. Therefore the conditional argument cannot be closed as an
unconditional C61 proof.

The argument uses no bad Euler factor, epsilon factor, root number,
decomposition Frobenius, branch selection, or local-field converse.
**NO_BAD_EULER_OR_ROOT_NUMBER** remains literal.

## Corrections or Missing Assumptions

- The target report is bound only to the root-authoritative SHA-256
  \(eb0a70f62427cd8b70fa35dc4153bd93d57d9ddef5ab7a349d439be3a8257026\);
  no earlier digest is admissible.
- No self-atlas aggregate hash is present. Future authority must reconstruct
  the self rows and may bind their resulting official evidence only after
  independent checking.
- The plus-self join \(263f\ldots\) and the embedded minus-self join
  \(a426\ldots\) are G-conjugate via the displayed \(w\). They are one P3
  class, not two.
- P3 is nonconjugate to the mixed seed-\(149\) Fourier group
  \(T_+=55d7\ldots\), which is P6.
- The vanished direct Fourier component is \(R_0\). The nonzero third
  Kummer carrier is the product \(r_0=r_+r_3\).
- The normalized reconstruction is
  \(4\lambda=\operatorname{Tr}+2r_++4r_3\), not a scalar-free shorthand.
- Formal stabilizers do not imply evaluated field degrees; G3's complete
  noncollision is indispensable.
- \(B=\mathbf Q(r_+)\) has target degree \(80\), not \(320\), and
  \(A=\mathbf Q(\delta_+)\) has target degree \(40\), not \(160\).
- The counts \(160\), \(12\), and \(8\) have distinct meanings.
- Uniqueness of \(L\) and \(K\) is confined to the twelve mixed factors.
- Generic Burnside, double-coset, tensor/compositum, Fourier, and zeta
  mechanisms are prior art; only the bounded exact instance is positioned as
  the proposed contribution.

## Open Risks

- Complete self-product row inventories and conjugators have not yet been
  produced by an official C61 implementation.
- The target carrier inventory for every advertised mixed factor and base
  has not yet passed product-form resolvent and noncollision checks.
- Exact divisibility by \(2\) and \(4\), \(R_0=0\), and orbit rank \(3\)
  remain pending machine obligations.
- Exact seed-\(149\) embedded equality and P3/P6 nonconjugacy remain pending
  independent reconstruction.
- Every global arithmetic row, both degree-\(2880\) distinctions, and both
  routes around the diamond remain pending G5.
- Both complete \(D_3\) branches, including the \(B\) rows and every
  uncollected factor row, remain pending G6.
- Producer/checker separation, self-consistent hostile mutations,
  deterministic replay, manifests, source refresh, and formal hostile audit
  remain pending G7.
- Any requirement for branch selection, expanded characteristic-zero
  coefficients, maximal orders, class numbers, regulators, bad Euler data,
  epsilon factors, or root numbers would exceed the locked target.

The lifecycle remains
**TARGET_LOCKED / IMPLEMENTATION_PENDING / PAPER_PENDING / NOT_RELEASED**.
No proof completion, paper completion, promotion, archive, or release is
claimed.
