# SD-C11 Derivation Package

## Outcome

The holomorphic reflection double removes the adjoint backtracking of
SD-C10, but it also removes every vertical frequency from the surviving pure
atom sector:

\[
\Phi_2(C_s^{2r+1})=0,\qquad
\Phi_2(C_s^{2r})=2\sum_p p^{-r}.
\]

This is an all-order identity-sector theorem. At infinite atom count, the
quadratic case r=1 is a divergent formal/cutoff trace; the honest retained
trace terms for det_3 begin at r=2.

Any elementary two-step escape that moves with height replaces a pure atom
by a mixed ordered pair (p,q). Thus the finite-channel monomial class has
an exact dichotomy:

    pure reflected word   -> s-independent
    moving reflected word -> mixed generalized ledger

Status: **GO REFLECTION RIGIDITY / STOP VERTICAL DIVISOR / ROUTE B LOCKED**.

## Frozen object

Let the atoms be the tensor-indecomposable full shifts F_p, ordered by
topological entropy log(p). The base graph is the recurrent
nearest-neighbor chain with an identity loop at each atom. Give the plus and
minus cross edges disjoint directed-positive cocycle alphabets and define

\[
C_s=
\begin{pmatrix}
0&T_s^+\\
T_{1-s}^-&0
\end{pmatrix}.
\]

The minus block is holomorphic in 1-s; it is not an adjoint. The channel
swap J and alphabet exchange implement

\[
J C_s J=C_{1-s}.
\]

The invariant is the channel/atom matrix trace followed by the canonical
identity-coefficient trace on both cocycle factors. All atoms are generated
internally. No target-zero data, scale, offset, phase, or pairing is fitted.

## 1. Exact alternating trace

Odd powers of C_s are off diagonal in channel space, hence have zero
finite-prefix trace. For an even closed word, the channel grammar uses
exactly r plus steps and r minus steps.

Every word containing a cross-atom edge has a nonempty positive projection
to at least one cocycle factor. Its identity coefficient vanishes. The
only surviving word stays at one atom p, and its weight is

\[
\bigl(p^{-s}p^{-(1-s)}\bigr)^r=p^{-r}.
\]

There are two starting channels, so

\[
\boxed{\Phi_2(C_s^{2r})=2\sum_p p^{-r}}.
\]

The exact three-atom audit enumerated powers 1 through 12. It contained
94,652 closed paths, of which 94,616 were mixed; all mixed identity
survivors were zero. Each even power had exactly six identity-visible pure
words, one for each atom and starting channel.

The same result holds when both layers share a positive alphabet. Disjoint
free alphabets are therefore convenient universal bookkeeping, not the
source of rigidity.

## 2. Common Schatten strip

For the finite-band endpoint transfer, the diagonal and the two weighted
shifts have the same p^{-Re(s)} summability threshold. Therefore

\[
T_s^+\in S_q\iff q\Re s>1,
\qquad
T_{1-s}^-\in S_q\iff q(1-\Re s)>1.
\]

The common strip is exactly

\[
\boxed{\frac1q<\Re s<1-\frac1q}.
\]

It is empty for q=1 and q=2; q=3 is the first integer regularization
order with a nonempty strip:

\[
\frac13<\Re s<\frac23.
\]

In particular, the naive direct sum T_s direct-sum T_(1-s) has no common
trace-class domain: its two S_1 conditions are respectively Re(s)>1 and
Re(s)<0.

## 3. The regularized determinant is vertically sterile

For a finite atom prefix,

\[
\det(I-zC_s)=\prod_p(1-z^2/p).
\]

The quadratic prime-harmonic term diverges at infinite atom count. On the
common S_3 strip, the canonical third regularization removes precisely
that term:

\[
\boxed{
\det{}_3(I-zC_s)
=\prod_p(1-z^2/p)e^{z^2/p}.}
\]

Indeed,

\[
\log\det{}_3(I-zC_s)
=-\sum_{r\ge2}\frac{z^{2r}}r\sum_p p^{-r}.
\]

The product is locally convergent in z, reflection symmetric, and exactly
independent of s. Across atom cutoffs N=2,3,8,16,32, complex s samples,
and a frozen complex z, the largest finite-prefix product residual was
2.36e-16; the largest apparent vertical range was 2.37e-16.
Reflection residual was exactly zero in binary64.

This determinant is not the original Euler determinant and has no moving
vertical divisor.

## 4. Cross-atom escape and the cosh dichotomy

Pairing different atoms produces

\[
\begin{aligned}
&p^{-s}q^{-(1-s)}+q^{-s}p^{-(1-s)}\\
&\qquad=\frac{2}{\sqrt{pq}}
\cosh\!\left((s-\tfrac12)\log(q/p)\right).
\end{aligned}
\]

For a two-oriented-block channel trace, this expression has an additional
factor two. On the critical line the cosh becomes a cosine and moves with
frequency log(q/p) whenever p differs from q.

But its exponent support is the mixed ordered pair (p,q), not a repetition
of one primitive atom. Constant phases cannot change that support.
Thirty-two frozen random perfect pairings of eight atoms all showed motion;
all 32 also contained mixed ledger terms. Hence generic pairing motion is
PROVES_TOO_MUCH, not an arithmetic selector.

## 5. Label relations

- Independent positive alphabets: no mixed identity through length 10 and
  all-order positive-word proof.
- Shared positive alphabet: same result; alphabet independence is refuted as
  essential.
- Inverse reflected labels: eight mixed identity backtracks already at
  length two for the three-atom prefix.
- Finite C5 labels: the first mixed identity occurs at length ten. A
  closed path in the atom chain has an even cross count, while the group
  relation requires a multiple of five, hence lcm(2,5)=10.

Finite relations and inverse identifications restore identity-visible mixed
words; they do not restore a pure moving prime ledger.

## 6. Random-DAG and inventory controls

For an arbitrary upper-DAG endpoint transfer, both T_s and T_(1-s) are
upper triangular. Their product has diagonal p^{-1}. Thus every cyclic
trace and finite det_3 is the same pure reflected product regardless of the
DAG radical.

All 24 frozen random complex DAGs passed the power 2,4,6,8 trace ledger to
maximum residual 8.88e-16, and all 24 had nonzero Schatten-fourth motion.
The largest determinant vertical range was 1.39e-17, while singular-motion
ranges ran from 1.462 to 33.392. This is a direct PROVES_TOO_MUCH control.

Tensor atoms, a shuffled copy, composites, and matched random integers all
obey the same pure reflection sterility. The arithmetic origin remains in
the tensor source, not in the reflection mechanism.

## Claim boundary

    finite/all-order identity-sector trace algebra: PROVED
    infinite even trace at r>=2:                     PROVED
    quadratic r=1 trace:                             FORMAL / DIVERGENT
    common S_q strip and q=3 threshold:              PROVED
    det_3 canonical product:                         PROVED
    reflection symmetry:                             PROVED
    pure-prime vertical motion:                      REFUTED
    cross-atom cosh motion:                          PROVED, mixed ledger
    finite-label leakage:                            PROVED
    global target divisor / RH claim:                NOT MADE
    fixed self-adjoint generator:                    ABSENT

No zero crossing census was performed, and no Riemann-zero or target-spectrum
data were loaded.
