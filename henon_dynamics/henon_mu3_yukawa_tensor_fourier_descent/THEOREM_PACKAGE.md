# HCS-C61 theorem package

Status: **TARGET_LOCKED / IMPLEMENTATION_PENDING / PAPER_PENDING / NOT_RELEASED**

This file locks a theorem target. It does not state a proved C61 theorem.
Every machine gate G0--G7 is pending, no C61 certificate or independent
checker report exists, and no formal proof completion is claimed. The
selection scans, arithmetic experiments, subgroup replays, and source audit
used to choose the target are pilots and are not theorem authority.

Root-authoritative target-selection report SHA-256:
**eb0a70f62427cd8b70fa35dc4153bd93d57d9ddef5ab7a349d439be3a8257026**.
This is the digest of the final 59,956-byte, 1,096-line target report. No
earlier report digest and no self-atlas aggregate hash is bound here. The
report is authority for target selection and lifecycle only; its pilot
tables do not discharge G1--G6.

Scope literal: **NO_BAD_EULER_OR_ROOT_NUMBER**.

Locked prospective paper title:
**Zeta-Equivalent Tensor Algebras of the Hénon Gassmann Twins and an
Explicit Fourier Descent**.

## 1. Released authority and exact conventions

The sole released repository authority is P60 commit

**fe1217810b72840619efdf40a2af31b8b80d96f6**.

Any future G0 evidence must byte-rebind at least:

| released object | SHA-256 |
|---|---|
| C60 certificate | d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518 |
| C60 canonical payload | dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead |
| C60 group evidence | dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2 |
| C60 resolvent evidence | f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da |
| C60 frozen permutation arrays | 0fc281590b635eed046cc4a8d38036895e2b1bc56284a0948b1576303de1c2f5 |
| C60 primitive carrier for \(L\) | fae69eb91d414d8241bbbee51f4a3fcc91c4f8691090adc5cbb575079d2ea1f5 |
| C59 resolvent evidence | 667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6 |

The future implementation must additionally rebind the released
self-excluding manifest, live/archive Route identity, Batch file, labelled
integral roots, split prime, local filtrations, source contract, and protected
guard. Nothing in a pilot may replace one of those released inputs.

The immutable conventions are:

- group arrays are one-based images on 27 labels;
- sparse-carrier monomials are zero-based;
- multiplication of label maps means left-after-right composition;
- the polynomial action is \(p(X_i)=X_{p(i)}\);
- sparse monomials and canonical group element lists are lexicographically
  sorted;
- coefficients and all evidence counters are exact integers;
- the common split-prime witness is \(p=692717\), using C59's labelled
  integral roots \(\alpha_i=L_0d_i\);
- ToM positions and serialized hashes are checks, never definitions of
  subgroups or fields.

## 2. Locked object and notation

Let \(K/\mathbf Q\) be the released common normal closure and put

$$
G=\operatorname{Gal}(K/\mathbf Q)=W(E_6),\qquad |G|=51840.
$$

Let \(H_+,H_-\leq G\) be the released nonconjugate order-\(162\),
index-\(320\) Gassmann pair, and define

$$
F_+=K^{H_+},\qquad F_-=K^{H_-},
$$

$$
X=G/H_+,\qquad Y=G/H_-,\qquad
x=[X],\quad y=[Y]\in B(G).
$$

The C61 object is the ordered triple of dimension-\(102400\) finite étale
algebras

$$
\mathscr T_{++}=F_+\otimes_{\mathbf Q}F_+,\qquad
\mathscr T_{+-}=F_+\otimes_{\mathbf Q}F_-,\qquad
\mathscr T_{--}=F_-\otimes_{\mathbf Q}F_-,
$$

together with the complete self/mixed relative-position atlas and the exact
Fourier descent selecting one degree-\(40\) mixed intersection field.
C60's biquadratic envelope is released input, not a fourth C61 tensor object.

For \(a,b\in\{+,-\}\) and a chosen double-coset representative \(g\), put

$$
I_{ab,g}=H_a\cap gH_bg^{-1},\qquad
J_{ab,g}=\langle H_a,gH_bg^{-1}\rangle,
$$

$$
E_{ab,g}=K^{I_{ab,g}},\qquad C_{ab,g}=K^{J_{ab,g}}.
$$

The intended field dictionary is

$$
E_{ab,g}=F_aF_b^g,\qquad C_{ab,g}=F_a\cap F_b^g.
$$

It is a G2 proof obligation, not an identity inferred from subgroup orders.

## 3. C61-EXACT-0 through C61-EXACT-7

All eight gates in this section are **PENDING**. Their names lock the
required future evidence; they do not record passes.

### C61-EXACT-0 / G0: released authority and conventions

Rebind the complete released P60/C60/C59 authority, the owner-bound final
target-selection report, the action and
serialization conventions, the split-prime roots, the literal title and
object boundary, and every false scope leaf. Reject arbitrary paths,
certificate-selected dependencies, stale snapshots, and pilot substitution.

### C61-EXACT-1 / G1: three tensor products

Independently enumerate the twelve double cosets for each of
\(H_+\backslash G/H_+\), \(H_+\backslash G/H_-\), and
\(H_-\backslash G/H_-\). Reconstruct every intersection and join from
released arrays, certify representatives, conjugators, complete element
sets, cores, normalizers, automorphism groups, multiplicities, all three
degree sums, and the unified \(\mathbf Q\)-isomorphism grouping. Verify the
three full permutation characters and the Burnside/linearization conclusions.

### C61-EXACT-2 / G2: mixed \(160/12/8\) atlas

Keep distinct the \(160\) conjugate positions, the \(12\) mixed double
cosets/simple factors, and the \(8\) mixed \(\mathbf Q\)-isomorphism types.
Prove the compositum/intersection dictionary, core-freeness, the
common-normal-closure extension criterion, all conjugacy/nonconjugacy
decisions, and the narrowly scoped unique minimum \(L/M\) and maximum \(K\).

### C61-EXACT-3 / G3: product-form resolvents and noncollision

Construct source-owned integral carriers for every advertised new mixed
factor/base type and for the Fourier fields \(A,B\). Certify formal
stabilizers, complete orbits, product-form orbit polynomials, contents, and
complete evaluated noncollision at \(p=692717\). A formal stabilizer, modular
sample, ToM locator, or hash alone does not establish a characteristic-zero
field degree.

### C61-EXACT-4 / G4: Fourier bridge and fixed-field diamond

Reconstruct all Fourier carriers, prove the vanishing component and exact
divisions, establish the three-dimensional orbit span, certify
primitive-but-nonnormal status, rebuild the exact stabilizers, and prove the
seed-\(149\) mixed join equals the Fourier sign stabilizer as an embedded
element set. Prove the entire \(A/B/M/F_+\) lattice, normalizers, cores,
normal closures, automorphism groups, and square-class identities.

### C61-EXACT-5 / G5: complete global arithmetic

Independently compute signatures, discriminant signs, exact eight-prime
support, absolute exponent vectors, and relative discriminant-norm vectors
for all eight mixed types, all four mixed bases, \(A\), and \(B\). Reconcile
both routes around the fixed-field diamond and distinguish field,
resolvent-polynomial, and order discriminants.

### C61-EXACT-6 / G6: both complete local branches

Retain both \(D_3=\mathrm{ToM}\ 140\) and \(D_3=\mathrm{ToM}\ 206\).
Store and check every uncollected base and factor row for the mixed fields,
their bases, \(B\), and the released C60 envelope. Verify degree, factor, and
different totals, relative tower identities, tame rows, the prime-by-prime
ideal laws, and the archimedean complementarity. Neither branch may be
selected.

### C61-EXACT-7 / G7: independent authority and scope

Require mathematically independent producer/checker call graphs, a separate
GAP/TomLib group reconstruction, a separate arithmetic projection,
deterministic two-run replay, strict schemas, hostile mutations including
self-consistent rebounds, atomic manifests, a refreshed primary-source
ledger, a hostile formal audit, and explicit false scope leaves. Passing
G0--G7 would create a theorem candidate; release would still require a later
explicit promotion.

## 4. Conditional tensor and Burnside theorem target

The statements in this section are conditional targets: they may be promoted
to theorem statements only after G0--G7 all pass.

The released Gassmann relation gives

$$
\operatorname{lin}(x)=\operatorname{lin}(y)
$$

in the rational representation ring. The proposed C61 conclusion is

$$
x^2,\ xy,\ y^2\ \text{are pairwise distinct in }B(G),
$$

while

$$
\operatorname{lin}(x^2)=\operatorname{lin}(xy)
=\operatorname{lin}(y^2).
$$

Thus \(x(x-y)\), \(y(x-y)\), and
\((x+y)(x-y)\) are proposed explicit nonzero elements of the kernel of
rational linearization. On the finite étale side the three tensor algebras
are proposed to be pairwise nonisomorphic, while their permutation
characters and products of Dedekind zeta functions agree. This does not
assert an isomorphism of finite \(G\)-sets, fields, rings of integers, or
integral permutation modules.

The locked degree spectra are:

| algebra | simple-factor degree multiset |
|---|---|
| \(\mathscr T_{++}\) | \(320^2,960^2,1920,5760^2,8640^2,17280,25920^2\) |
| \(\mathscr T_{+-}\) | \(640,960^2,1920,2880^4,8640^2,17280,51840\) |
| \(\mathscr T_{--}\) | \(320^2,960^2,1920,5760^2,8640^2,17280,25920^2\) |

Here a superscript denotes multiplicity, not exponentiation of a degree.
Each row has twelve factors and total dimension \(102400\).

The unified factor-type targets are

$$
\mathscr T_{++}=Q_1^2Q_2^2Q_3Q_4^2Q_5^2Q_6Q_7^2,
$$

$$
\mathscr T_{+-}=Q_8Q_9^2Q_{10}Q_{11}^2Q_{12}^2Q_{13}^2Q_{14}Q_{15},
$$

$$
\mathscr T_{--}=Q_{16}^2Q_{17}^2Q_3Q_4^2Q_{18}^2Q_6Q_7^2.
$$

The diagonal types \(Q_1=K^{H_+}\) and \(Q_{16}=K^{H_-}\) are
nonisomorphic because their core-free stabilizers are nonconjugate. The
equal self degree spectra therefore do not collapse the two self tensor
algebras.

The canonical row/type inventory is:

| lane | canonical seed grouping |
|---|---|
| \(++\) | \(0,201:Q_1/P1;\ 2,196:Q_2/P2;\ 69:Q_3/P3;\ 59,68:Q_4/P4;\ 1,16:Q_5/P4;\ 52:Q_6/P4;\ 3,13:Q_7/P4\) |
| \(+-\) | \(148:Q_8/P5;\ 24,178:Q_9/P3;\ 149:Q_{10}/P6;\ 2,3:Q_{11}/P4;\ 12,169:Q_{12}/P4;\ 0,1:Q_{13}/P4;\ 7:Q_{14}/P4;\ 4:Q_{15}/P4\) |
| \(--\) | \(0,298:Q_{16}/P7;\ 1,13:Q_{17}/P8;\ 86:Q_3/P3;\ 46,62:Q_4/P4;\ 2,18:Q_{18}/P4;\ 32:Q_6/P4;\ 3,6:Q_7/P4\) |

G1 must rebuild the canonical representatives, intersection/join arrays,
and conjugators for every listed seed from the released group arrays. This
compact inventory is not permission to identify a row from its labels.

### 4.1 Complete mixed type target

The mixed factorization target is

$$
\begin{aligned}
F_+\otimes_{\mathbf Q}F_-\cong{}&
L_{640}\times E_{960}^{\,2}\times E_{1920}
\times E_{2880,a}^{\,2}\times E_{2880,b}^{\,2}\\
&\times E_{8640}^{\,2}\times E_{17280}\times K.
\end{aligned}
$$

The exact mixed type inventory is:

| type | multiplicity | raw positions | \(|I|\) | \([E:\mathbf Q]\) | \(|J|\) | \([C:\mathbf Q]\) | base class |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 81 | 640 | 324 | 160 | \(C_1=M\) |
| 2 | 2 | 3 | 54 | 960 | 1296 | 40 | \(C_2=P3\) |
| 3 | 1 | 3 | 27 | 1920 | 1296 | 40 | \(C_3=A=P6\) |
| 4 | 2 | 9 | 18 | 2880 | 51840 | 1 | \(\mathbf Q\) |
| 5 | 2 | 9 | 18 | 2880 | 51840 | 1 | \(\mathbf Q\) |
| 6 | 2 | 27 | 6 | 8640 | 51840 | 1 | \(\mathbf Q\) |
| 7 | 1 | 27 | 3 | 17280 | 51840 | 1 | \(\mathbf Q\) |
| 8 | 1 | 81 | 1 | 51840 | 51840 | 1 | \(\mathbf Q\) |

Every \(I\) is required to be core-free. The normalizer orders of the eight
representative \(I\)-types are respectively

$$
324,\ 108,\ 1296,\ 36,\ 108,\ 36,\ 216,\ 51840,
$$

so the proposed automorphism orders are

$$
4,\ 2,\ 48,\ 2,\ 6,\ 6,\ 72,\ 51840.
$$

Type \(1\) is required to be the unique minimum-degree mixed factor and to
equal the released C60 field \(L\), with base \(M\). Type \(8\) is required
to be the unique maximum mixed factor and to equal \(K\). Both uniqueness
statements are restricted to these twelve mixed factors.

### 4.2 Correct P3 class and the distinct Fourier class

The plus-self degree-\(1920\) join has embedded complete-group SHA-256

**263f31237e6f5111f76fd3470b6936a1a314020255c22eab55cece395c2adeb5**.

The minus-self degree-\(1920\) join has embedded complete-group SHA-256

**a426d516c4806c70f334acc004dc0dc4515e0caafe8ca1c06cde69596d2d2de1**.

These two embedded element sets are not different conjugacy classes. The
one-based permutation

$$
w=[25,22,23,27,24,26,9,13,20,16,19,7,11,8,10,15,12,14,18,21,17,4,1,2,6,3,5]
$$

must be checked to satisfy

$$
wJ_{--,86}w^{-1}=J_{++,69}
$$

as equality of complete element sets. After conjugation the minus-self image
has the plus-self hash \(263f\ldots\). These joins, together with the mixed
type-\(2\) joins, form the single P3 conjugacy class.

The P3 class is nonconjugate to the seed-\(149\) mixed type-\(3\) Fourier
join

$$
T_+,\qquad
\operatorname{SHA256}(T_+)
=\mathtt{55d7f2df8abc6709489e9bf632c45d620b9b570e6a295a82ee6f941c24c2c6bc}.
$$

This distinct mixed class is P6. Equal order \(1296\), equal field degree
\(40\), or an embedded serialization hash is not a conjugacy proof.

## 5. Conditional Fourier and fixed-field theorem target

Let \(J\triangleleft N\) be C60's order-\(81\) subgroup and
\(N/J\cong V_4\). For the released primitive carrier \(\lambda\), let
\(\operatorname{Tr}\) denote its \(V_4\)-trace and let
\(R_+,R_0,R_3\) be its three nontrivial character sums, labelled by their
order-two kernels. The exact target identities are

$$
R_0=0,\qquad
4\lambda=\operatorname{Tr}+R_++R_3,
$$

$$
r_+=R_+/2,\qquad r_3=R_3/4,\qquad r_0=r_+r_3,
$$

$$
4\lambda=\operatorname{Tr}+2r_++4r_3,
\qquad
\delta_i=r_i^2,\qquad
\delta_0=\delta_+\delta_3.
$$

The coefficientwise divisions by \(2\) and \(4\) must be proved before the
normalized carriers are formed. The direct \(H_0\)-component is the vanished
\(R_0\); the constructed Kummer carrier \(r_0=r_+r_3\) is a different
object and must never be replaced by a sum.

The proposed exact sparse-carrier fingerprints are:

| carrier | degree | terms | SHA-256 |
|---|---:|---:|---|
| \(r_+\) | 2 | 54 | 2edfe1e8f952faf2ddbfae3af135da4509f3f40e4175e188e240a5f09b785a96 |
| \(r_3\) | 2 | 162 | b9c21c9fc7060d4e52630a75d6ec0c10305ac33946f78c2c93e33fad68df8c7e |
| \(r_0\) | 4 | 7560 | a26813d1b2874ee700ececba786af55391dacc2a30a0d4da0390ecb871f63382 |
| \(\delta_+\) | 4 | 1458 | 1b5927b4d213dfd5af490067a9a551ae0942791a5221e2fb2f9f826440b040c3 |
| \(\delta_3\) | 4 | 10125 | 5f8baf7254f5c27478afce45b5667c62d13a35b205739bbf20ebd36651a144e7 |

The trace carrier has degree \(2\), \(243\) terms, and SHA-256

**a7398d36cea0c83ace64466a579e21666731d1e3c8e8641df4ce036c79de2bd7**.

The factorized \(\delta_0=\delta_+\delta_3\) expression DAG has target
SHA-256
**ed8974824f48cc65299443609c94db5ceab06efb8bed36f44b99ead311d28a66**.
An expanded \(\delta_0\) is not an authority requirement.

At the split prime, the identity values of the three Fourier eigenspace
components

$$
\operatorname{Tr},\qquad r_+,\qquad r_3
$$

are respectively

$$
581739,\qquad 643771,\qquad 119649.
$$

All three are nonzero. The separate product carrier \(r_0\) has identity
value \(582281\). Together with the exact eigenspace identities, the three
nonzero values are the evaluated rank gate: the \(V_4\)-orbit of
\(\lambda\) has span dimension \(3\) over \(M=K^N\). The intended
conclusion is that \(\lambda\) is primitive for \(L/M\) but is not a
normal-basis generator. No normal integral basis statement is included.

The required formal and evaluated orbit data are:

| object | orbit | stabilizer order | sign orbit | sign stabilizer order |
|---|---:|---:|---:|---:|
| \(r_+\) | 80 | 648 | 40 | 1296 |
| \(r_3\) | 320 | 162 | 160 | 324 |
| \(r_0\) | 320 | 162 | 160 | 324 |

Complete evaluated noncollision at \(p=692717\) must give distinct counts
\(80,40,320,160,320,160\) for
\(r_+,\delta_+,r_3,\delta_3,r_0,\delta_0\), respectively.

Put

$$
S_+=\operatorname{Stab}_G(r_+),\qquad
T_+=\operatorname{Stab}_G(\delta_+).
$$

Their proposed complete-group hashes are

$$
\operatorname{SHA256}(S_+)
=\mathtt{1df969ee447989751850d36d7af50ce219daff3dbc830c56df04d93e9c512871},
$$

$$
\operatorname{SHA256}(T_+)
=\mathtt{55d7f2df8abc6709489e9bf632c45d620b9b570e6a295a82ee6f941c24c2c6bc}.
$$

For the canonical mixed seed

$$
g_{149}=[1,3,13,14,19,6,27,10,9,7,24,17,16,12,22,2,4,21,5,20,15,18,11,26,25,23,8],
$$

the future proof must establish the embedded equality

$$
T_+=\langle H_+,g_{149}H_-g_{149}^{-1}\rangle.
$$

This is stronger than equality of order, degree, hash, ToM position, or
abstract isomorphism.

Define

$$
A=\mathbf Q(\delta_+)=K^{T_+},\qquad
B=\mathbf Q(r_+)=K^{S_+},\qquad
M=K^N,\qquad F_+=K^{H_+}.
$$

The locked subgroup target is

$$
H_+<S_+<T_+,\qquad N<T_+,\qquad
S_+\cap N=H_+,\qquad \langle S_+,N\rangle=T_+,
$$

with orders \(162,648,1296\) for \(H_+,S_+,T_+\) and \(|N|=324\).
The conditional fixed-field conclusion is

$$
[A:\mathbf Q],[B:\mathbf Q],[M:\mathbf Q],[F_+:\mathbf Q]
=40,80,160,320,
$$

$$
B\cap M=A,\qquad BM=F_+,
$$

$$
\operatorname{Aut}_{\mathbf Q}(A)=1,\qquad
\operatorname{Aut}_{\mathbf Q}(B)\cong C_2,
$$

and all four normal closures equal \(K\). In particular
\(\mathbf Q(r_+)\ne F_+\) and \(\mathbf Q(\delta_+)\ne M\).
The degree-\(40\) field \(A\) is the P6 mixed type-\(3\) intersection field,
not the P3 field.

The other two quadratic arms must satisfy

$$
F_3=M(r_3)=M(\sqrt{\delta_3}),\qquad
F_0=M(r_0)=M(\sqrt{\delta_0}),
$$

$$
[\delta_0]=[\delta_+][\delta_3]\quad
\text{in }M^\times/M^{\times2}.
$$

## 6. Conditional global arithmetic target

Put

$$
\Pi_A=181\cdot997\cdot2346241,
$$

$$
\Pi_B=283\cdot1801\cdot
14932047182473291995860108491583652133938007263719.
$$

Exponent vectors below are ordered as
\((v_3,v_5,v_{\Pi_A},v_{\Pi_B})\).

| mixed type | degree | signature | sign | absolute exponent vector | base | relative norm vector |
|---:|---:|---:|:---:|---|---|---|
| 1 | 640 | \((0,320)\) | \(+\) | \((1264,992,384,320)\) | \(M\) | \((32,0,0,0)\) |
| 2 | 960 | \((16,472)\) | \(+\) | \((1944,1488,624,480)\) | \(C_2\) | \((312,0,192,0)\) |
| 3 | 1920 | \((0,960)\) | \(+\) | \((3808,2976,1152,960)\) | \(A\) | \((208,48,0,240)\) |
| 4 | 2880 | \((16,1432)\) | \(+\) | \((5872,4464,1872,1440)\) | \(\mathbf Q\) | same as absolute |
| 5 | 2880 | \((48,1416)\) | \(+\) | \((5856,4464,1872,1440)\) | \(\mathbf Q\) | same as absolute |
| 6 | 8640 | \((48,4296)\) | \(+\) | \((17640,13392,5616,4320)\) | \(\mathbf Q\) | same as absolute |
| 7 | 17280 | \((0,8640)\) | \(+\) | \((35504,26784,11520,8640)\) | \(\mathbf Q\) | same as absolute |
| 8 | 51840 | \((0,25920)\) | \(+\) | \((106560,80352,34560,25920)\) | \(\mathbf Q\) | same as absolute |

The four mixed base classes have targets:

| base | degree | signature | signed exponent data |
|---|---:|---:|---|
| \(M\) | 160 | \((16,72)\) | \(+(308,248,96,80)\) |
| \(C_2=P3\) | 40 | \((8,16)\) | \(+(68,62,18,20)\) |
| \(A=P6\) | 40 | \((6,17)\) | \(-(75,61,24,15)\) |
| \(\mathbf Q\) | 1 | \((1,0)\) | \(+(0,0,0,0)\) |

The Fourier fields have target formulas

$$
\operatorname{Disc}(A)
=-3^{75}5^{61}\Pi_A^{24}\Pi_B^{15},
\qquad \operatorname{sig}(A)=(6,17),
$$

$$
\operatorname{Disc}(B)
=+3^{154}5^{122}\Pi_A^{48}\Pi_B^{30},
\qquad \operatorname{sig}(B)=(4,38).
$$

The target relative discriminant-norm vectors are

| extension | vector |
|---|---|
| \(B/A\) | \((4,0,0,0)\) |
| \(M/A\) | \((8,4,0,20)\) |
| \(F_+/B\) | \((8,8,0,40)\) |
| \(F_+/A\) | \((24,8,0,40)\) |
| \(F_+/M\) | \((8,0,0,0)\) |

Both routes from \(A\) to \(F_+\) must yield \((24,8,0,40)\).
These are norms of relative discriminant ideals, not prime-ideal
factorizations, maximal-order computations, or local-field classifications.

## 7. Conditional two-branch local target

No \(D_3\) branch is selected. Complete uncollected rows remain mandatory;
the compact targets below are checks, not substitutes for G6 evidence.

For the eight mixed factor types, the exact
\((\text{degree},\text{different},\text{factor count})\) triples are:

| type | \(D_3=\mathrm{ToM}\ 140\) | \(D_3=\mathrm{ToM}\ 206\) |
|---:|---|---|
| 1 | \((640,1264,56)\) | \((640,1264,28)\) |
| 2 | \((960,1944,72)\) | \((960,1944,36)\) |
| 3 | \((1920,3808,160)\) | \((1920,3808,80)\) |
| 4 | \((2880,5872,188)\) | \((2880,5872,94)\) |
| 5 | \((2880,5856,204)\) | \((2880,5856,102)\) |
| 6 | \((8640,17640,552)\) | \((8640,17640,276)\) |
| 7 | \((17280,35504,968)\) | \((17280,35504,484)\) |
| 8 | \((51840,106560,2880)\) | \((51840,106560,1440)\) |

Writing \((n,e,f,d)^m\) for an absolute local row of multiplicity \(m\),
the collected mixed rows are:

| type | \(D_3=\mathrm{ToM}\ 140\) | \(D_3=\mathrm{ToM}\ 206\) |
|---:|---|---|
| 1 | \((2,2,1,1)^8,(6,6,1,11)^{20},(18,18,1,37)^{28}\) | \((4,2,2,1)^4,(12,6,2,11)^{10},(36,18,2,37)^{14}\) |
| 2 | \((3,3,1,5)^8,(6,6,1,11)^{12},(9,9,1,18)^8,(18,18,1,37)^{44}\) | \((6,3,2,5)^4,(12,6,2,11)^6,(18,9,2,18)^4,(36,18,2,37)^{22}\) |
| 3 | \((2,2,1,1)^{24},(6,6,1,11)^{48},(18,18,1,37)^{88}\) | \((4,2,2,1)^{12},(12,6,2,11)^{24},(36,18,2,37)^{44}\) |
| 4 | \((3,3,1,5)^4,(6,6,1,11)^{28},(9,9,1,18)^{12},(18,18,1,37)^{144}\) | \((6,3,2,5)^2,(12,6,2,11)^{14},(18,9,2,18)^6,(36,18,2,37)^{72}\) |
| 5 | \((3,3,1,5)^{24},(6,6,1,11)^{18},(9,9,1,18)^{24},(18,18,1,37)^{138}\) | \((6,3,2,5)^{12},(12,6,2,11)^9,(18,9,2,18)^{12},(36,18,2,37)^{69}\) |
| 6 | \((3,3,1,5)^{12},(6,6,1,11)^{66},(9,9,1,18)^{36},(18,18,1,37)^{438}\) | \((6,3,2,5)^6,(12,6,2,11)^{33},(18,9,2,18)^{18},(36,18,2,37)^{219}\) |
| 7 | \((6,6,1,11)^{12},(18,18,1,37)^{956}\) | \((12,6,2,11)^6,(36,18,2,37)^{478}\) |
| 8 | \((18,18,1,37)^{2880}\) | \((36,18,2,37)^{1440}\) |

The four base triples are:

| base | \(D_3=\mathrm{ToM}\ 140\) | \(D_3=\mathrm{ToM}\ 206\) |
|---|---|---|
| \(M\) | \((160,308,22)\) | \((160,308,11)\) |
| \(C_2=P3\) | \((40,68,10)\) | \((40,68,5)\) |
| \(A=P6\) | \((40,75,7)\) | \((40,75,5)\) |
| \(\mathbf Q\) | \((1,0,1)\) | \((1,0,1)\) |

The collected base rows are:

| base | \(D_3=\mathrm{ToM}\ 140\) | \(D_3=\mathrm{ToM}\ 206\) |
|---|---|---|
| \(M\) | \((1,1,1,0)^4,(3,3,1,5)^6,(6,6,1,11)^2,(9,9,1,18)^6,(18,18,1,37)^4\) | \((2,1,2,0)^2,(6,3,2,5)^3,(12,6,2,11),(18,9,2,18)^3,(36,18,2,37)^2\) |
| \(C_2=P3\) | \((1,1,1,0)^4,(3,3,1,5)^2,(6,6,1,11)^2,(9,9,1,18)^2\) | \((2,1,2,0)^2,(6,3,2,5),(12,6,2,11),(18,9,2,18)\) |
| \(A=P6\) | \((1,1,1,0),(3,3,1,5)^4,(9,9,1,18),(18,18,1,37)\) | \((1,1,1,0),(6,3,2,5)^2,(9,9,1,18),(18,18,1,37)\) |
| \(\mathbf Q\) | \((1,1,1,0)\) | \((1,1,1,0)\) |

For \(B\), the target triples are

$$
(80,154,10)\quad\text{and}\quad(80,154,8)
$$

for ToM \(140\) and ToM \(206\), respectively.

The collected \(B\) rows are:

| branch | collected absolute rows |
|---|---|
| ToM \(140\) | \((1,1,1,0)^2,(6,6,1,11)^4,(9,9,1,18)^2,(18,18,1,37)^2\) |
| ToM \(206\) | \((1,1,1,0)^2,(9,9,1,18)^2,(12,6,2,11)^2,(18,18,1,37)^2\) |

For the released C60 \(V_4\) envelope, define
\(a=gfd\) for a relative row \((g,e,f,d)\). Prime by prime, both branches
must satisfy

$$
\min(a_+,a_3)=0,\qquad
a_0=a_++a_3,\qquad a_L=2a_0.
$$

The resulting ideal target is

$$
(\mathfrak d_{F_+/M},\mathfrak d_{F_3/M})=1,
$$

$$
\mathfrak d_{F_0/M}
=\mathfrak d_{F_+/M}\mathfrak d_{F_3/M},
\qquad
\mathfrak d_{L/M}=\mathfrak d_{F_0/M}^{\,2}.
$$

The \(p=3\) inertia-type populations are

| branch | \(H_+\) | \(H_3\) | trivial | \(H_0\) |
|---|---:|---:|---:|---:|
| ToM \(140\) | 8 | 8 | 6 | 0 |
| ToM \(206\) | 4 | 4 | 3 | 0 |

The residue-degree masses are \(8:8:6:0\) in both branches, and the relative
norm exponents for \((F_+,F_0,F_3,L)\) are \((8,16,8,32)\).
Every ramified relative row must have \(e=2,d=1\) and be tame.

At infinity the type counts are \(H_+:8,H_3:8,H_0:0\); the real-splitting
sets of \(F_+\) and \(F_3\) are complementary, and each real completion of
\(L\) is \(\mathbf C\times\mathbf C\).

## 8. Source boundary

The general mechanisms are prior art and must be cited as such:

- Gassmann and Perlis for arithmetic equivalence and the zeta bridge;
- Bartel--Dokchitser, Parzanchevski, and
  Lin--Shinder--Zimmermann for Burnside multiplication and linearization;
- Étienne for tensor-field quotients/composita indexed by double cosets;
- James for the \(350\to339\to11\) \(W(E_6)\) collision census;
- Kida as the closest audited compositum comparator;
- GAP and TomLib only for software provenance.

The bounded contribution language is: for this specified \(W(E_6)\)
Gassmann pair, determine and certify the three tensor decompositions, their
pairwise nonisomorphism despite equal linearization, the mixed \(12\)-factor
and \(8\)-type atlas, and the exact P6 Fourier field. No generic double-coset,
Burnside, Fourier, or absolute-priority claim is licensed.

## 9. Nonclaims and lifecycle boundary

**NO_BAD_EULER_OR_ROOT_NUMBER**.

This target does not claim decomposition Frobenius data, bad Artin Euler
factors, local epsilon factors, local or global root numbers, Artin
holomorphy, automorphy, analytic continuation, functional equations, branch
selection, converse classification of local fields by \((n,e,f,d)\),
expanded characteristic-zero orbit-polynomial coefficients, maximal orders,
integral bases, monogenicity, class numbers, regulators, trace forms, motives,
rational points, Brauer--Manin consequences, RH, or Hilbert--Pólya.

The exact lifecycle remains
**TARGET_LOCKED / IMPLEMENTATION_PENDING / PAPER_PENDING / NOT_RELEASED**.
Pilots remain nonauthority; G0--G7 remain pending; no proof, paper,
promotion, archive, or release is claimed.
