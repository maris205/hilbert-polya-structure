# HCS-C27 source audit: finite Weil fibres over the chronological AGY cocycle

**Audit date:** 2026-08-10

**Status:** `SOURCE_LOCKED; INTERNAL_C24_C25_C26_INPUTS_VERIFIED; TARGET_CLAIMS_SCOPED`
**Candidate:** exact odd-characteristic Weil fibres over the source-locked
four-letter `H(2)` AGY first-return system

## 1. Purpose and claim boundary

C27 changes the quantum fibre used in C24--C26.  It does not change the
underlying Rauzy graph, the AGY return section, the chronological matrix
convention, the scalar holomorphic base space, or the scalar roof/Jacobian
weight.  For an odd prime `p`, the intended new fibre is the genuine finite
Weil representation

\[
\rho_p:\operatorname{Sp}(4,\mathbb F_p)\longrightarrow
U(\mathcal H_p),
\qquad \dim \mathcal H_p=p^2,
\]

formed only after the exact integer cocycle has been placed in one fixed
symplectic lattice and reduced modulo `p`.

This audit freezes four logically distinct layers:

1. C24 supplies the literal seven-state Rauzy graph, exact edge transport,
   primitive labeled-cycle controls, and regular/singular homological
   witnesses.
2. C25 supplies the state-4 AGY section, its fixed-fibre integral
   trivialization, and the all-length word decoder.
3. C26 supplies the common holomorphic domain, the scalar trace-class
   determinant, the exact scalar periodic trace atom, and three explicit AGY
   chronology witnesses.
4. Thomas and Gurevich--Hadani supply the external Weil-character and finite
   quantization theory.  They do not supply the C27 dynamical conclusions.

C27 is not authorized to infer a prime-orbit law, the divisor or functional
equation of `xi`, a self-adjoint Hilbert--Polya operator, or an `p -> infinity`
limit to the infinite oscillator representation.  A finite character table
is an arithmetic fibre invariant, not a Riemann-zero fit.

## 2. Immutable internal inputs

Paths below are relative to `henon_dynamics/`.

### 2.1 C24: literal Rauzy chronology

- Project: `rauzy_metaplectic_obstruction/`
- Source commit:
  `0cbd599dcf6d52190b5ac2fb7d68807f1e25fbaa`
- Exact certificate:
  `rauzy_metaplectic_obstruction/results/c24_certificate.json`
- Certificate SHA-256:
  `4b4fe5943262137eeeb3eda4de887725a0663402a1f39f8cc43e089bcc91e778`
- Producer:
  `rauzy_metaplectic_obstruction/code/c24_producer.py`
- Producer SHA-256:
  `ad89bbd9001daca5fa805fbd9112739385d82fe3533b401cb48149792a18ffdd`

Authorized reuse:

- the seven labeled permutations and fourteen labeled directed edges;
- the elementary convention `B_e=I+E_(loser,winner)`;
- later-on-the-left chronological multiplication;
- the changing crossing-form transport identity;
- the 146 phase-invariant eventually-positive primitive labeled-cycle
  controls through elementary length twelve, including the 21
  fixed-vector/singular controls.

The 146 objects are primitive directed edge-token cycles modulo cyclic phase.
They are not asserted to be pairwise distinct primitive unmarked
Teichmuller geodesics.

### 2.2 C25: AGY section and fixed integral fibre

- Project: `agy_metaplectic_transfer_obstruction/`
- Source commit:
  `1903e35a81a1f00243a2acde5ad4753edf6e5bb4`
- Exact certificate:
  `agy_metaplectic_transfer_obstruction/results/c25_certificate.json`
- Certificate SHA-256:
  `a35cee22714abbb9dc9aadcc165720d1ff77aff3b7f29071f53a1b451760bd12`
- Producer:
  `agy_metaplectic_transfer_obstruction/code/c25_producer.py`
- Producer SHA-256:
  `6d5bebb6ac27c26691691cd92a2c4149c9093eb3a3ee91d6a678a5fc02b54ee8`

Authorized reuse:

- base state `4`, with permutation
  `(1,3,4,2)/(4,3,2,1)`;
- the deterministic state-4-rooted spanning-tree frames `S_pi`;
- all fourteen fixed-fibre edge matrices;
- the source-locked neat strongly-positive word
  `gamma_star=t^64(tbttbtbb)^8`;
- the all-length fixed-start matrix decoder.

The finite length-22 stress enumeration remains a mutation sentinel.  It is
not the proof of the decoder theorem and is not a branch-completeness theorem
for C27.

### 2.3 C26: scalar holomorphic determinant and chronology witnesses

- Project: `agy_holomorphic_slice_obstruction/`
- Implementation commit:
  `6d8c40eed90fc6bd0cf5349069756c0045fb11bd`
- Release/provenance commit:
  `a952fc3487d2984d10e566a34b02fa2f7cccc34c`
- Release tag: `hcs-c26-agy-holomorphic-slice-obstruction-v1`
- Exact certificate:
  `agy_holomorphic_slice_obstruction/results/c26_certificate.json`
- Certificate SHA-256:
  `1c0289b9b47e65e0603ea001be7cce263aea13d58c66e4609eac88edf8f7ce4a`
- Producer:
  `agy_holomorphic_slice_obstruction/code/c26_producer.py`
- Producer SHA-256:
  `321cd3dcc63912e1aaa3824f00be8d6f372020887a2dae2633de636e20a89503`

Authorized reuse:

- the common bounded complex domain and compact containment for all AGY
  inverse branches;
- the scalar trace-class transfer operator on the source half-plane;
- the exact word trace atom
  `lambda_word^(-(s+1))/chi_word'(lambda_word)`;
- the one-, two-, and three-return exact chronological matrices.

The infinite unsmoothed oscillator fibre was proved noncompact on the C26
holomorphic space.  Finite Weil fibres are a new candidate, not a truncation,
regularization, or repair of that infinite unitary.

## 3. Exact symplectic conventions

### 3.1 State-4 crossing form and fixed form

At C25 base state `4`, the crossing form is

\[
\Omega_4=
\begin{pmatrix}
0&1&1&1\\
-1&0&0&0\\
-1&0&0&1\\
-1&0&-1&0
\end{pmatrix}.
\]

The fixed form used by C27 is

\[
\boxed{
J_0=\Omega_4^{-1}=
\begin{pmatrix}
0&-1&0&0\\
1&0&-1&1\\
0&1&0&-1\\
0&-1&1&0
\end{pmatrix}.}
\]

For every state `pi`, C25 supplies an integral unimodular frame satisfying

\[
S_\pi^T J_\pi S_\pi=J_0,
\qquad J_\pi=\Omega_\pi^{-1}.
\]

### 3.2 Integral passage to standard Schrödinger coordinates

Use the ordered symplectic basis

\[
a_1=e_1,\qquad a_2=e_1+e_3,\qquad
b_1=-e_2,\qquad b_2=e_1-e_4.
\]

With these vectors as columns,

\[
\boxed{
T=
\begin{pmatrix}
1&1&0&1\\
0&0&-1&0\\
0&1&0&0\\
0&0&0&-1
\end{pmatrix},
\qquad \det T=-1,}
\]

and direct multiplication gives

\[
\boxed{
T^T J_0T=J_{\rm std}=
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
-1&0&0&0\\
0&-1&0&0
\end{pmatrix}.}
\]

Both `T` and `T^(-1)` are integral.  Consequently this change of basis is
valid modulo every prime, with no exceptional denominator prime.

### 3.3 Edge and path telescope

For a labeled path

\[
\pi_0\xrightarrow{e_1}\pi_1\xrightarrow{e_2}\cdots
\xrightarrow{e_n}\pi_n,
\]

later edges multiply on the left:

\[
B_w=B_{e_n}\cdots B_{e_1}.
\]

Define

\[
g_e=S_{\rm dst}^{-1}B_eS_{\rm src},
\qquad
\widehat g_e=T^{-1}g_eT.
\]

Then each `g_e` lies in `Sp(J0,Z)`, each `g_hat_e` lies in
`Sp(J_std,Z)`, and the state frames telescope without approximation:

\[
\boxed{
\widehat g_{e_n}\cdots\widehat g_{e_1}
=T^{-1}S_{\pi_n}^{-1}B_wS_{\pi_0}T.}
\]

For a closed state-4 AGY branch, `S_4=I`, so

\[
\widehat g_w=T^{-1}B_wT.
\]

Reduction modulo `p` may be performed edgewise or after the exact integer
product, but the independent implementation must show that both routes agree.
Identity tree edges and distinct labeled edges with equal matrices must remain
in the symbolic word; matrix coincidence does not authorize deletion of
dynamical tokens.

## 4. Source-locked C26 AGY branch chronology

Let

\[
G=t^{64}(tbttbtbb)^8,
\qquad |G|=128.
\]

In standard coordinates its exact matrix is

\[
Q_G=
\begin{pmatrix}
7110&11430&-464277&-3353\\
50233&81363&-3279928&-24020\\
-24020&-38803&1568410&11430\\
-38803&-62823&2533625&18540
\end{pmatrix}.
\]

The two return bridges used by C26 are

\[
u=bttbtbb,
\qquad
v=bbb,
\]

with standard matrices

\[
Q_u=
\begin{pmatrix}
1&0&0&0\\
1&3&0&-1\\
-1&-1&1&0\\
-1&-2&0&1
\end{pmatrix},
\qquad
Q_v=
\begin{pmatrix}
1&0&0&0\\
1&2&0&1\\
-1&-1&1&-1\\
-1&-1&0&0
\end{pmatrix}.
\]

Freeze the three branches as

\[
\gamma_1=G,
\qquad
\gamma_2=GuG,
\qquad
\gamma_3=GvG,
\]

so their matrices are

\[
Q_1=Q_G,
\qquad
Q_2=Q_GQ_uQ_G,
\qquad
Q_3=Q_GQ_vQ_G.
\]

For forward return order `(gamma_1,...,gamma_n)`, the forward cocycle matrix
is

\[
Q_{\rm fwd}=Q_n\cdots Q_1.
\]

The two-return pair `Q_2 Q_1` versus `Q_1 Q_2` is a matrix-order sentinel but
not a character separator: every genuine representation satisfies
`Tr rho(AB)=Tr rho(BA)`.

The C26 three-return forward/reversal pair is

\[
Q_3Q_2Q_1
\quad\hbox{versus}\quad
Q_1Q_2Q_3.
\]

Its two nontrivial reciprocal characteristic-polynomial coefficient
differences are

\[
229726517858224006251712
\]

and

\[
145433515145576882885026606972800.
\]

Their greatest common divisor is `64`; hence these two characteristic
polynomials remain different modulo every odd prime.  This is a universal
odd-prime chronology mutation sentinel, not evidence of a Riemann divisor.

## 5. C24 controls and exact conjugacy collapse

### 5.1 Canonical P076 and P082 paths

C24-P076 and C24-P082 are distinct primitive labeled free cycles.  The
canonical certificate representatives both start and end at state `0`; no
cyclic shift is used in the matrices below.

P076 has edge path

```text
s00:b:s03, s03:b:s00, s00:t:s01, s01:t:s02,
s02:b:s06, s06:b:s04, s04:b:s02, s02:t:s00,
s00:t:s01, s01:b:s01, s01:t:s02, s02:t:s00
```

and chronological matrix

\[
B_{76}=
\begin{pmatrix}
4&4&1&3\\
2&3&0&2\\
3&5&2&3\\
2&3&1&2
\end{pmatrix}.
\]

P082 has edge path

```text
s00:b:s03, s03:b:s00, s00:t:s01, s01:t:s02,
s02:t:s00, s00:t:s01, s01:b:s01, s01:t:s02,
s02:b:s06, s06:b:s04, s04:b:s02, s02:t:s00
```

and chronological matrix

\[
B_{82}=
\begin{pmatrix}
2&5&1&4\\
1&4&0&3\\
1&6&2&4\\
1&4&1&3
\end{pmatrix}.
\]

The C25 state-4-rooted frame at state `0` is

\[
S_0=
\begin{pmatrix}
1&0&0&1\\
1&1&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}.
\]

Thus the canonical fixed-`J0` representatives are

\[
\boxed{
g_{76}=S_0^{-1}B_{76}S_0=
\begin{pmatrix}
3&1&0&3\\
2&2&0&1\\
8&5&2&6\\
5&3&1&4
\end{pmatrix},}
\]

\[
\boxed{
g_{82}=S_0^{-1}B_{82}S_0=
\begin{pmatrix}
2&1&0&2\\
3&3&0&2\\
7&6&2&5\\
5&4&1&4
\end{pmatrix}.}
\]

Both satisfy `g^T J0 g=J0` and have determinant one.

If the free cycles are instead rotated to the common central state `2`, their
first-return lists are respectively

\[
[bbb,ttbt,tbbtt]
\quad\hbox{and}\quad
[bbb,tbbtt,ttbt].
\]

This cyclic rebasing explains the noncyclic branch-order comparison, but it
is not used to define the canonical matrices above.

### 5.2 Explicit integral symplectic conjugator

Set

\[
\boxed{
Y=
\begin{pmatrix}
0&0&1&-1\\
1&0&-1&2\\
2&2&0&1\\
1&1&0&1
\end{pmatrix}.}
\]

Exact multiplication verifies

\[
\det Y=1,
\qquad
Y^TJ_0Y=J_0,
\qquad
\boxed{g_{82}=Yg_{76}Y^{-1}}.
\]

For independent replay,

\[
Y^{-1}=
\begin{pmatrix}
1&1&1&-2\\
-1&-1&0&1\\
1&0&-1&2\\
0&0&-1&2
\end{pmatrix}.
\]

Consequently P076 and P082 are conjugate already in `Sp(J0,Z)`, hence in
`Sp(J0,Q)` and, after reduction, in `Sp(J0,F_p)` for every prime `p`.
For every genuine finite Weil representation and every integer `r`,

\[
\boxed{
\Theta_p(g_{76}^r)=\Theta_p(g_{82}^r)
\quad\text{for every odd prime }p.}
\]

There is no distinguishing pair `(p,r)`.  This is an exact full-tower
conjugacy-collapse control: distinct symbolic Rauzy cycles can remain
indistinguishable to every group class-function fibre, not only to the
characteristic polynomial.

### 5.3 Regular and singular controls

The following C24 controls must remain available to an independent checker:

- P076/P082: integral-conjugacy null control; their common characteristic
  polynomial is `x^4-11x^3+18x^2-11x+1` and `det(I-g)=-2`, so they have no
  fixed vector modulo any odd prime.
- P009: `SNF(g-I)=diag(1,1,1,0)`; fixed-space dimension one modulo every
  prime.
- P073: `SNF(g-I)=diag(1,1,0,0)`; fixed-space dimension two modulo every
  prime.
- P065: `SNF(g-I)=diag(1,1,3,0)`; fixed-space dimension jumps at `p=3`.

The Smith-normal-form controls prevent an implementation from replacing
rank over `F_p` by rank over `Q`.  C24's real/infinite-dimensional regular
point obstruction is not transplanted into the finite model: a finite Weil
character is an honest finite trace even when `g-I` is singular.

## 6. Primary external sources

### 6.1 Thomas: character of the Weil representation

Teruji Thomas, *The Character of the Weil Representation*, Journal of the
London Mathematical Society (2) **77** (2008), 221--239.

- Preprint: <https://arxiv.org/abs/math/0610644>
- DOI: `10.1112/jlms/jdm098`

Thomas treats symplectic vector spaces over finite or local fields and gives
choice-free character formulas in terms of a Weil index/Maslov-type quadratic
form.  C27 uses this source to justify the character-theoretic invariant and
its dependence on genuine metaplectic/Weil normalization.  It does not use a
real distributional regular-point value as the finite-field trace, and it
does not infer that a character depends only on a characteristic polynomial.

### 6.2 Gurevich--Hadani: canonical finite quantization

Shamgar Gurevich and Ronny Hadani, *Quantization of Symplectic Vector Spaces
over Finite Fields*, Journal of Symplectic Geometry **7** (2009), 475--502.

- Preprint: <https://arxiv.org/abs/0705.4556>
- DOI: `10.4310/JSG.2009.v7.n4.a4`

For a finite-dimensional symplectic vector space over a finite field of odd
characteristic, Gurevich--Hadani construct a canonical quantization functor
and hence a canonical model of the Weil representation.  In the present
four-dimensional symplectic space the Schrödinger fibre has dimension `p^2`.
C27 uses this source for the existence and functorial/conjugacy-compatible
finite representation, not for any AGY orbit theorem or arithmetic match.

### 6.3 Required normalization

Every released computation must freeze the nontrivial additive character,
for example

\[
\psi_p(x)=\exp(2\pi i x/p),
\]

and one consistent Fourier/Gauss normalization.  The same normalization must
be used for all branches and all powers at fixed `p`.  Edgewise arbitrary
phases define neither a genuine representation nor a character.  Conjugate
matrices must have identical computed characters; the P076/P082 tower is the
mandatory normalization sentinel.

## 7. Precise scope firewall

### Proved before C27

- literal seven-state Rauzy dynamics and exact chronological edge matrices;
- statewise integral symplectic trivialization and all-length AGY decoder;
- common C26 holomorphic domain and scalar trace-class determinant;
- exact scalar periodic trace atom;
- P076/P082 integral symplectic conjugacy and consequent full finite-character
  tower equality.

### Permitted C27 claims after exact verification

- exact reductions of chronological matrices in `Sp(4,F_p)` for stated odd
  primes;
- exact finite Weil characters under the frozen normalization;
- exact character collisions or separations for explicitly released words;
- a finite-dimensional vector-valued trace-class determinant obtained by
  tensoring the already-proved scalar branch operators with bounded
  `p^2`-dimensional matrices, provided branchwise and wordwise chronology is
  retained;
- scoped arithmetic fragmentation or collapse statements for the released
  branch set and prime window.

### Not permitted without new proof

- quotienting symbolic branches by matrix, characteristic polynomial, or
  character equality;
- replacing chronological products by averaged transition matrices;
- treating a finite branch window as completeness for the countable AGY
  section;
- identifying labeled Rauzy cycles with pairwise distinct unmarked
  Teichmuller geodesics;
- passing from a finite Weil determinant to the infinite oscillator
  determinant or to an `p -> infinity` limit;
- claiming a prime number theorem, Riemann explicit formula, `xi` divisor,
  functional equation, critical-line theorem, or Hilbert--Polya operator;
- using prime tables or Riemann-zero tables to choose the dynamics,
  normalization, branches, or weights.

## 8. Audit decision

The source chain is coherent and noncircular:

\[
\text{C24 exact Rauzy chronology}
\longrightarrow
\text{C25 fixed integral AGY fibre}
\longrightarrow
\text{C26 scalar holomorphic determinant}
\longrightarrow
\text{odd-prime finite Weil twist}.
\]

The large positive gate is that the finite fibre has an honest trace and does
not inherit C26's infinite-dimensional noncompactness obstruction.  The
large negative gate is equally exact: finite Weil characters are class
functions, and the distinct P076/P082 symbolic chronology collapses for every
prime and every repetition because its cocycles are integrally symplectically
conjugate.  C27 must measure both phenomena without hiding either one.
