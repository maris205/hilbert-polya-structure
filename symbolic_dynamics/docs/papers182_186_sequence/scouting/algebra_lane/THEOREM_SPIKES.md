# Frozen theorem spikes

These are proof packages, not conjectures inferred from a finite box.  The
finite boxes in `CANONICAL.txt` independently test every displayed formula on
the listed instances.

## A01 / cyclic lattice comparator

Let `L` be any lattice and define

\[
T(a,b,c)=(c,a\wedge b,a\vee b)\qquad(a,b,c\in L).
\]

### Universal temporal theorem

For every lattice,

\[
T^2(a,b,c)=(a\vee b,\ c\wedge a\wedge b,\ c\vee(a\wedge b)),
\qquad T^4=T^2.
\]

Consequently every orbit enters a cycle of length one or two by time two.  A
state is recurrent exactly when `b<=a` and `b<=c`; on this recurrent set,
`T(a,b,c)=(c,b,a)`.  It is fixed exactly when additionally `a=c`.

**Proof.** Put `m=a meet b` and `j=a join b`.  Then
`T^2(a,b,c)=(j,c meet m,c join m)`.  Applying `T` twice more and using
`c meet m <= m <= j` returns this same triple.  Equality with the original
triple is equivalent to `a=j`, `b=c meet m`, and `c=c join m`, which reduces
to `b<=a,c`.  The swap and fixed-point statements follow immediately.  No
distributive or modular law is used.  QED.

Now specialize to the lattice `L_d(q)` of subspaces of `F_q^d`, where `q` is
any prime power.  Write

\[
{n\brack r}_q=\prod_{i=0}^{r-1}\frac{q^{n-i}-1}{q^{r-i}-1},\qquad
G_n(q)=\sum_{r=0}^n {n\brack r}_q.
\]

Define four explicit quantities:

\[
\begin{aligned}
F_d(q)&=\sum_{b=0}^d {d\brack b}_qG_{d-b}(q),\\
R_d(q)&=\sum_{b=0}^d {d\brack b}_qG_{d-b}(q)^2,\\
Q_n(q)&=\sum_{a=0}^n\sum_{s=0}^{n-a}
 {n\brack a}_q{n-a\brack s}_q q^{as},\\
H_d(q)&=\sum_{m=0}^d {d\brack m}_qQ_{d-m}(q)G_{d-m}(q).
\end{aligned}
\]

Here `F_d` counts intervals `B<=A`, `R_d` counts triples `B<=A,C`,
`Q_n` counts ordered pairs of disjoint subspaces in an `n`-space, and `H_d`
counts triples satisfying `A cap B <= C`.

### Full graph census on `L_d(q)^3`

For every prime power `q` and every `d>=1`:

- carrier size: `G_d(q)^3`;
- image size: `G_d(q) F_d(q)`;
- fixed points: `F_d(q)`;
- strict two-cycles: `(R_d(q)-F_d(q))/2`;
- depth-zero vertices: `R_d(q)`;
- depth-one vertices: `H_d(q)-R_d(q)`;
- depth-two vertices: `G_d(q)^3-H_d(q)`.

In particular the height is sharply two.  The depth predicate itself is
especially simple: a nonrecurrent `(A,B,C)` has depth one iff `A cap B <= C`,
and depth two otherwise.

**Proof.** The universal theorem gives the cycles and depth predicates.
Choose `B` first and pass to `F_q^d/B` to obtain `F_d` and `R_d`.  For fixed
`M=A cap B`, the quotients `A/M,B/M` are disjoint.  If their dimensions are
`a,s`, choose the first subspace, then the second by the standard graph-of-a-
linear-map count `{n-a bracket s}_q q^{as}`.  Finally choose `C/M`; this gives
`H_d`.  The image consists exactly of triples `(C,M,J)` with `M<=J`, proving
its count.  Taking `A=B` a nonzero line and `C=0` proves sharpness.  QED.

### Every-target fibre atlas

For a target `(C,M,J)`, the first coordinate is immaterial and

\[
|T^{-1}(C,M,J)|=
\begin{cases}
K_k(q),&M\le J,\quad k=\dim(J/M),\\
0,&M\not\le J,
\end{cases}
\]

where

\[
K_k(q)=\sum_{a=0}^k {k\brack a}_q q^{a(k-a)}.
\]

Indeed a preimage is uniquely an ordered pair `(A,B)` satisfying
`A cap B=M` and `A+B=J`; after quotienting by `M`, choose `A/M` and then a
complement.  This is a targetwise statement, not merely a histogram.

**Deep spike.** The same three-register law has a universal lattice temporal
identity, while finite-field modularity supplies an independent complement-
pair fibre law.  Thus neither theorem is a corollary of the other.

## A02 / Lie-derived subspaces of a central thickening

Let `q` be an odd prime power, let `Z=F_q^z`, and put

\[
\mathfrak l_{z,q}=Z\oplus\mathfrak {sl}_2(F_q),\qquad
D(U)=[U,U]=\operatorname{span}\{[x,y]:x,y\in U\}
\]

on the full subspace lattice of `l_{z,q}`.  Let `pi` be projection onto
`S=sl_2(F_q)`, let `L=q^2+q+1`, and define

\[
E_{z,r}(q)=\sum_{k=0}^z {z\brack k}_q q^{r(z-k)}.
\]

### Projection and lift lemmas

1. `D(U)=[pi U,pi U]` because `Z` is central.
2. The bracket map `Lambda^2 S -> S` is an isomorphism.  In the usual basis
   `(H,E,F)`, its images are `2E,-2F,H`; odd characteristic is exactly what
   makes this invertible.
3. For a fixed `r`-subspace `P<=S`, precisely `E_{z,r}(q)` subspaces `U` have
   `pi U=P`.

For (3), choose `K=U cap Z` of dimension `k`.  Then `U/K` is the graph of an
arbitrary linear map `P -> Z/K`, giving `q^{r(z-k)}` choices.

### Full two-axis dynamical and fibre theorem

For every odd prime power `q` and every `z>=0`, `D^3=D^2`.  Its image consists
of exactly

\[
0,\quad\text{the }L\text{ lines in }S,\quad S,
\]

so has size `L+2`.  The only recurrent states are the fixed points `0` and
`S`; there are no nontrivial cycles.  On the carrier of size `G_{z+3}(q)`,
the depth census is

\[
N_0=2,\qquad N_2=L E_{z,2}(q),\qquad
N_1=G_{z+3}(q)-2-L E_{z,2}(q).
\]

Every target has the following exact fibre:

\[
|D^{-1}(W)|=
\begin{cases}
E_{z,0}(q)+L E_{z,1}(q),&W=0,\\
E_{z,2}(q),&W\text{ is a line contained in }S,\\
E_{z,3}(q),&W=S,\\
0,&\text{otherwise.}
\end{cases}
\]

**Proof.** If `r=dim(pi U)` is zero or one, alternation forces `D(U)=0`.
If `r=2`, the bracket isomorphism sends `Lambda^2(pi U)` to one nonzero line;
as planes range over `S`, these lines do so bijectively.  If `r=3`, the image
is `S`.  Lines derive to zero and `S` derives to itself.  The lift lemma then
gives each fibre and every depth count.  QED.

**Deep spike.** The parameter `z` does not merely duplicate states: it changes
each of the three positive fibre sizes by a different Gaussian-binomial lift
polynomial `E_{z,r}`, while the temporal skeleton stays rigid.  This cleanly
separates geometry from transient multiplicity.

## A03 / exact theorem retained only as a kill-control

For odd `q`, set `C(A)=AA^t-A^tA` on `M_2(F_q)`.  Writing
`u=b-c`, `v=b+c`, `w=d-a` gives

\[
C\!\begin{pmatrix}a&b\\c&d\end{pmatrix}
=\begin{pmatrix}uv&uw\\uw&-uv\end{pmatrix}.
\]

Thus `C^2=0`, the image is the `q^2`-element trace-zero symmetric plane, the
zero fibre has size `q^3+q(q-1)`, and each nonzero image point has fibre
`q(q-1)`.  This is fully closed, but it is **not a survivor**: P175 already
establishes the project-local square-zero commutator mechanism, so this theorem
is evidence for a collision kill, not a third recommendation.

