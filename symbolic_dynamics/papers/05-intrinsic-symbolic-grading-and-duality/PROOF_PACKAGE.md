# Paper 05 Proof Package

## Status and claim boundary

**Status: COHERENT AS SCOPED.**

This package proves an exact graded enhancement of the Paper-04 symbolic
Euler object and a same-family analytic obstruction. The positive statement
is that tensor-factorization topology canonically supplies the Möbius parity
and therefore fixes the Euler determinant orientation once the exterior
transfer functor is chosen. The negative statement is that none of the three
frozen symbolic dualities produces a trace-class
\(s\leftrightarrow1-s\) completion, a Gamma factor, or a completed-\(\xi\)
divisor.

The standard Koszul resolution, the zero-differential exterior transfer
module, and the odd one-particle Berezinian are three different objects.
They are never identified below.

No new candidate ID is assigned: the preregistered G4 gate fails. The result
is a graded theorem about SD-C07, not SD-C08.

## 1. Source-locked symbolic monoid

Let \(F_n=\{1,\ldots,n\}^{\mathbb Z}\) be the two-sided full \(n\)-shift.
Cartesian product and topological entropy give

\[
 F_m\boxtimes F_n\cong F_{mn},
 \qquad
 h(F_n)=\log n.
\]

Hence the isomorphism-class monoid

\[
 M=\operatorname{Iso}(\mathsf{FSh})
\]

is canonically isomorphic to
\((\mathbb N_{\ge1},\times)\), and its nonunit tensor atoms are \(F_p\).
Let

\[
 V=\bigoplus_{P\in\operatorname{At}(M)}\mathbb C e_P
\]

and let the Paper-04 atom transfer act by

\[
 L_s e_{F_p}=e^{-s h(F_p)}e_{F_p}=p^{-s}e_{F_p}.
\]

On \(\ell^2(\operatorname{At}(M))\), \(L_s\) is trace class precisely when
\(\Re s>1\).

## 2. Factorization topology fixes Möbius parity

For \(n>1\), let \(P_n=(F_1,F_n)\) be the open interval in the tensor-divisor
poset and let \(\Delta_n=\Delta(P_n)\) be its order complex. We use the
augmented reduced simplicial complex, so an empty interval has one generator
in degree \(-1\).

### Theorem 2.1 — tensor-divisor homology

For every \(n>1\),

\[
\widetilde H_j(\Delta_n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,
  & n\text{ squarefree and }j=\omega(n)-2,\\
0,
  & n\text{ not squarefree}.
\end{cases}
\]

Consequently,

\[
\widetilde\chi(\Delta_n)
=\sum_j(-1)^j\operatorname{rank}\widetilde H_j(\Delta_n)
=\mu(n).
\]

#### Proof

Write \(n=\prod_{i=1}^k p_i^{a_i}\). The closed divisor interval is the
product of chains

\[
[F_1,F_n]\cong\prod_{i=1}^k[0,a_i].
\]

Use the atoms \(F_{p_i}\) as a crosscut. A subset of these atoms spans the
crosscut complex exactly when its tensor join is strictly below \(F_n\).
If every \(a_i=1\), the only forbidden subset is the full set, so the
crosscut complex is the boundary of a \((k-1)\)-simplex and has the homotopy
type of \(S^{k-2}\). If some \(a_i>1\), even the join of all atoms is
\(F_{\operatorname{rad}(n)}<F_n\); every subset is allowed and the crosscut
complex is a full simplex. It is contractible. The crosscut theorem gives
the stated homotopy types. For \(k=1\) and \(n=p\), the boundary of the
zero-simplex is the empty complex and
\(\widetilde H_{-1}=\mathbb Z\). The Euler formula follows. \(\square\)

### Corollary 2.2 — canonical atom parity

In the standard reduced chain grading, an atom \(F_p\) contributes in degree
\(-1\), hence in odd parity. More generally, a squarefree tensor product of
\(k\) distinct atoms contributes in degree \(k-2\), whose parity is \(k\).
Thus the homological sign is \((-1)^k=\mu(n)\).

This parity is independent of the ordering and orientation of the simplex
basis. Reorienting chains conjugates the boundary matrices by diagonal sign
matrices and leaves homology and supertrace invariant.

### Corollary 2.3 — homological Dirichlet supertrace

Adjoin the tensor unit in even degree. On

\[
\mathcal H_{\mathrm{fac}}
=\mathbb C\mathbf1\oplus
 \bigoplus_{n\ge2}\widetilde H_\bullet(\Delta_n;\mathbb C),
\]

let \(W_s\) act by \(n^{-s}\) on the \(n\)-summand. For \(\Re s>1\),

\[
\operatorname{Str}(W_s)
=\sum_{n\ge1}\mu(n)n^{-s}
=\frac1{\zeta(s)}.
\]

This is a homological explanation of the Möbius coefficient ledger. It is
not an analytic continuation theorem.

## 3. Exterior transfer and determinant orientation

Put the atom space \(V\) in odd degree and form the zero-differential exterior
transfer module \(\Lambda^\bullet V\). This construction is functorial under
permutations of tensor atoms and uses no assigned atom signs.

### Theorem 3.1 — exterior and Berezinian identities

For \(\Re s>1\),

\[
\operatorname{Str}_{\Lambda^\bullet V}\Gamma_-(L_s)
=\det(I-L_s)
=\prod_p(1-p^{-s})
=\frac1{\zeta(s)}.
\]

On the purely odd one-particle space \(V_{\bar1}\), with the fixed convention
\(\operatorname{Ber}(A)=\det(A_{\bar0})/\det(A_{\bar1})\),

\[
\operatorname{Ber}_{V_{\bar1}}(I-L_s)
=\det(I-L_s)^{-1}
=\zeta(s).
\]

#### Proof

At a finite atom cutoff, exterior occupation permits each atom zero or one
time. The graded trace therefore factorizes as

\[
\prod_p(1-p^{-s}).
\]

Absolute convergence for \(\Re s>1\) permits the infinite product and
identifies it with the Fredholm determinant. A purely odd one-particle
operator contributes in the denominator of the Berezinian, giving the
reciprocal identity. \(\square\)

### Interpretation

The two formulas solve the Paper-04 determinant-orientation question only at
A2:

- exterior/Fock supertrace gives \(1/\zeta(s)\);
- the odd one-particle Berezinian gives \(\zeta(s)\);
- both remain confined to \(\Re s>1\).

The selection of the exterior/Koszul functor is a modeling choice on the
bare tensor monoid. Once that functor is frozen, however, its vacuum is even,
its atoms are odd, and its internal determinant orientation is canonical.

The factor-count character is different:

\[
\sum_{n\ge1}\frac{(-1)^{\Omega(n)}}{n^s}
=\frac{\zeta(2s)}{\zeta(s)}.
\]

It is Liouville parity and does not implement fermionic exclusion. It must
not be confused with the Möbius/exterior ledger.

## 4. Honest Koszul resolution cancels the Euler data

Let \(A=\mathbb C[M]\cong\mathbb C[x_p:p\in\mathbb P]\), let
\(I=(x_p)\), and identify \(I/I^2\) with \(V\). The standard Koszul
resolution is

\[
K=A\otimes\Lambda^\bullet V
\]

with

\[
d(x^\alpha\otimes e_{p_1}\wedge\cdots\wedge e_{p_k})
=\sum_{j=1}^k(-1)^{j-1}
x^{\alpha+e_{p_j}}\otimes
e_{p_1}\wedge\cdots\widehat e_{p_j}\cdots\wedge e_{p_k}.
\]

Weight a basis vector by its total tensor mass:

\[
T_s(x^\alpha\otimes e_S)
=\bigl(N(\alpha)N(S)\bigr)^{-s}x^\alpha\otimes e_S .
\]

The total mass is preserved by \(d\), so \(dT_s=T_sd\).

### Theorem 4.1 — Lefschetz/Koszul cancellation

For \(\Re s>1\),

\[
\operatorname{Tr}(T_s)
=\zeta(s)\prod_p(1+p^{-s})
=\frac{\zeta(s)^2}{\zeta(2s)},
\qquad
\operatorname{Str}(T_s)=1.
\]

More generally, \(\operatorname{Str}(T_s^r)=1\) for every \(r\ge1\), and

\[
\operatorname{sdet}(I-zT_s)=1-z.
\]

#### Proof

The symmetric algebra contributes the bosonic trace
\(\prod_p(1-p^{-s})^{-1}\), while the exterior factor contributes the
supertrace \(\prod_p(1-p^{-s})\). They cancel. The ordinary exterior trace
is \(\prod_p(1+p^{-s})\), giving the stated ordinary trace. Replacing
\(s\) by \(rs\) proves the power-supertrace identity, and the logarithmic
definition of the superdeterminant yields

\[
\log\operatorname{sdet}(I-zT_s)
=-\sum_{r\ge1}\frac{z^r}{r}
\operatorname{Str}(T_s^r)
=\log(1-z).
\]

\(\square\)

### Consequence

The honest equivariant Koszul resolution has only its vacuum homology and
cannot itself carry the Riemann Euler product. The Möbius factor belongs to
the exterior transfer module or to factorization homology. Calling the
zero-differential exterior object “the Koszul complex” would erase this
obstruction and is forbidden in the paper.

## 5. Symbolic reversal gives \(s\mapsto s\)

Let \(V^s\) and \(V^u\) be stable and unstable copies of the atom space, and
let \(J:V^s\to V^u\) be induced by reversal of the two-sided full shift. The
entropy of \(F_p\) is unchanged by reversal.

### Proposition 5.1 — natural reversal complex

The source-compatible chain transfer is

\[
L_s\oplus L_s,
\qquad
J L_s=L_s J.
\]

Its ordinary determinant is \(\zeta(s)^{-2}\) and its superdeterminant is
\(1\) in \(\Re s>1\).

Replacing the unstable block by \(L_{1-s}\) breaks the chain identity:

\[
J L_s=L_{1-s}J
\]

holds for all tensor atoms only at the isolated line center \(s=\tfrac12\).
Moreover, \(L_s\) is trace class for \(\Re s>1\), while \(L_{1-s}\) is trace
class for \(\Re s<0\); the two domains do not overlap.

Thus symbolic time reversal explains transpose/reversal invariance of a
shift zeta, but does not generate the Riemann involution.

## 6. Group completion gives \(s\mapsto-s\)

The Grothendieck group of \(M\) is

\[
G=M^{\mathrm{gp}}\cong\mathbb Q_{>0}^{\times}
\cong\bigoplus_p\mathbb Z.
\]

Inversion sends the entropy character \(q^{-s}\) to \(q^s=q^{-(-s)}\).

### Proposition 6.1 — inversion is parity-even

For every monoidal grading
\(\varepsilon:G\to\mathbb Z/2\mathbb Z\),

\[
\varepsilon(g^{-1})=-\varepsilon(g)=\varepsilon(g).
\]

Hence inversion cannot functorially switch determinant parity. It naturally
implements \(s\mapsto-s\), not \(s\mapsto1-s\).

To write

\[
p^{-s}=p^{-1/2}p^{-(s-1/2)},
\qquad
p^{-(1-s)}=p^{-1/2}p^{s-1/2},
\]

one must add a half-density factor \(p^{-1/2}\). The bare full-shift tensor
skeleton contains no rule that selects this center. In this stage it is a
target-centered modeling choice, not an intrinsic symbolic invariant.

The signed blocks \(\operatorname{diag}(p^{-s},p^s)\) have no common
trace-class domain. Replacing signed entropy by absolute entropy makes the
two blocks identical and their superdeterminant trivial.

## 7. Strongest adversarial regularization

The next result deliberately grants the missing
\(s\leftrightarrow1-s\) pairing. It is an obstruction test and receives no
G4 credit.

For \(q\ge1\), diagonal singular values give

\[
L_s\in\mathcal S_q
\iff q\Re s>1,
\qquad
L_{1-s}\in\mathcal S_q
\iff q(1-\Re s)>1.
\]

### Theorem 7.1 — first critical-strip overlap deletes low traces

There is no common \(\mathcal S_1\) or \(\mathcal S_2\) domain. The first
integer regularization order with a nonempty overlap is \(q=3\), on

\[
\frac13<\Re s<\frac23.
\]

On this strip define the adversarial paired determinant

\[
D_3(s)
=\det\nolimits_3(I-L_s)
 \det\nolimits_3(I-L_{1-s}).
\]

Then \(D_3(s)=D_3(1-s)\), but \(D_3\) is zero-free throughout the strip and

\[
\log D_3(s)
=-\sum_{r\ge3}\frac1r
\sum_p\left(p^{-rs}+p^{-r(1-s)}\right).
\]

Thus the first regularization that reaches the critical line removes exactly
the \(r=1\) prime trace and the \(r=2\) prime-square trace.

#### Proof

The Schatten criterion is the convergence of
\(\sum_p p^{-q\Re s}\). A common strip exists exactly when
\(1/q<\Re s<1-1/q\), which first occurs for \(q=3\). The standard
regularized determinant satisfies

\[
\log\det\nolimits_3(I-A)
=-\sum_{r\ge3}\frac{\operatorname{Tr}(A^r)}r.
\]

Both \(L_s\) and \(L_{1-s}\) have spectral radius strictly below one on the
open strip, so none of their regularized factors vanishes there. Exchanging
\(s\) and \(1-s\) swaps the factors. \(\square\)

### Corollary 7.2 — no completion credit

Restoring the \(r=1,2\) terms requires counterterms that have no common
nuclear definition on an open neighborhood of the critical line. The
paired \(\det_3\) therefore cannot be the desired completed determinant.
It has the visible symmetry but loses the decisive arithmetic divisor.

## 8. Final gate decision

The exact results mechanically imply:

~~~text
G0  definition/source lock          PASS
G1  intrinsic factorization parity  PASS
G2  exact graded ledger             PASS
G3  analytic domain                 Euler half-plane only
G4  new A3 structure                FAIL

stage outcome: GO_A2_GRADED_ORIENTATION / STOP_A3_COMPLETION
candidate outcome: SD-C07 retained; no SD-C08
Route B: locked
~~~

The stage does not derive a Gamma factor, trivial-zero sector, scalar
functional equation, operator continuation, Riemann--von Mangoldt law, Weil
compression, or self-adjoint zero correspondence.

## 9. Smallest live next question

Within Symbolic Dynamics, the missing datum can be stated sharply:

> Does a natural symbolic Jacobian or normalized stable/unstable transfer
> functor supply a source-derived half-density character, rather than the
> target-selected factor \(p^{-1/2}\), while retaining the exact tensor-atom
> orbit ledger?

This question must be preregistered as a new symbolic object. It cannot
inherit G4 credit from the adversarial \(\det_3\) calculation.
