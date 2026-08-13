# SD-C13 Derivation Package

## Outcome

Finite positive unitary fibers cannot preserve the complete tensor-prime
repetition ledger and simultaneously create determinant-visible Bloch
motion. For a faithful normalized trace,

\[
\tau(U)=1\quad\Longrightarrow\quad U=I.
\]

The first moment removes every nontrivial positive visible fiber. Ordinary
trace exactness at all repetitions forces a one-dimensional trivial fiber.
Nonfaithful states may hide a moving sector, but then their moments do not
control its determinant. A graded matched sector restores the ledger only by
cancelling the same moving sector from the Berezinian. Roots-of-unity fibers
delay recurrent mixed words but never erase every repetition.

## Frozen object

The base consists of tensor-indecomposable full shifts \(F_p\), ordered by
entropy \(\log p\), with one primitive loop per atom. A frozen unitary
\(U_p\in U(d_p)\) is attached to the loop. Repetition \(r\) has coefficient

\[
p^{-rs}\tau_p(U_p^r),\qquad
\tau_p=d_p^{-1}\operatorname{Tr},
\]

and the finite-cutoff logarithmic determinant is

\[
\log D_N(s,z)
=-\sum_{p\le p_N}\sum_{r\ge1}
\frac{z^r p^{-rs}}r\tau_p(U_p^r).
\]

The direct sum has its honest trace-class interpretation on \(\Re s>1\).
No target zeros, fitted phases, or post-hoc fibers are used.

## Exact moment families

The executable audits \(r=1,\ldots,32\) for identity fibers, a scalar
phase, a conjugate phase pair, and cyclic permutations \(P_m\),
\(m=2,\ldots,8\). In particular,

\[
\boxed{\tau(P_m^r)=
\begin{cases}
1,&m\mid r,\\
0,&m\nmid r.
\end{cases}}
\]

The cycle formula has exact residual zero in every tested case.

## Faithful positive-state rigidity

For a unitary \(U\),

\[
\tau((U-I)^*(U-I))
=2-\tau(U)-\tau(U^*).
\]

If \(\tau(U)=1\), the positive left side is zero. Faithfulness gives
\(U=I\). Only the first moment is needed. Thirty-two random diagonal-unitary
controls in dimensions \(2,\ldots,8\) verify the identity with maximum
residual \(4.44\times10^{-16}\); every nontrivial control has
\(\tau(U)\ne1\).

## Ordinary-trace rigidity

Suppose a \(d\)-dimensional unitary has

\[
\operatorname{Tr}(U^r)=1,\qquad r=1,\ldots,d.
\]

Newton identities give \(e_1=1\) and \(e_2=\cdots=e_d=0\). For \(d>1\),
this forces \(\det U=0\), contradicting unitarity. Hence

\[
\boxed{\operatorname{Tr}(U^r)=1\ \forall r
\Longrightarrow d=1,\ U=1.}
\]

The exact recursion was checked for \(d=1,\ldots,8\).

## Nonfaithful and graded escapes

For \(U=1\oplus V\), a vector state supported on the first summand satisfies
\(\rho(U^r)=1\), but

\[
\det(I-zU)=(1-z)\det(I-zV).
\]

The hidden determinant factor is not controlled by the state. Across hidden
dimensions \(2,\ldots,8\) and four phases, state-ledger error is zero while
the ordinary determinant changes by up to \(8.883\times10^{-2}\).

For the graded choice

\[
\mathcal H_{\bar0}=1\oplus V,\qquad
\mathcal H_{\bar1}=V,
\]

one has \(\operatorname{Str}(U^r)=1\) for every repetition, but

\[
\operatorname{Ber}(I-zU)
=\frac{(1-z)\det(I-zV)}{\det(I-zV)}
=1-z.
\]

The moving sector cancels exactly. The largest numerical Berezinian
residual is \(2.22\times10^{-16}\).

## Recurrent mixed-cycle leakage

For a triangle with independent variables \(x,y,z\) and an \(m\)-cycle
fiber, the \(r\)-fold primitive contribution is

\[
3(xyz)^r\tau(P_m^r).
\]

It first survives at \(r=m\), hence at transfer power \(3m\). For
\(m=2,\ldots,8\), the first powers are
\(6,9,12,15,18,21,24\). Roots of unity delay leakage but never erase it.

Two independent return paths with monomials \(a,b\) and phases \(+1,-1\)
give

\[
a^r+(-1)^r b^r.
\]

This polynomial is nonzero for every \(r\). Under the nongeneric
specialization \(a=b\), odd repetitions cancel but even repetitions survive
as \(2a^r\).

## Entropy-block and clock controls

For cyclic fibers of dimensions \(d=2,3,4\),

\[
\det(I-aP_d(\phi))=1-e^{i\phi}a^d.
\]

The first ledger failure is repetition \(d\), exactly where the fiber first
becomes determinant-visible. The audit uses 32 seeds for each dimension and
each clock inventory.

| inventory | moving cases | motion range |
|---|---:|---:|
| tensor primes | 96/96 | 0.045893--0.704070 |
| composites | 96/96 | 0.004558--0.346647 |
| random increasing | 96/96 | 0.000465--0.064850 |

Every moving case fails the ledger at repetition \(2,3,\) or \(4\).
Bloch motion is generic and arithmetically nonselective.

## Claim boundary

    faithful normalized-trace rigidity:       PROVED
    ordinary all-moment rigidity:             PROVED
    nonfaithful state ledger:                 EXACT but determinant-uncontrolled
    graded ledger:                            EXACT but motion cancels
    roots-of-unity all-order cancellation:    REFUTED
    positive ledger plus nontrivial motion:   IMPOSSIBLE in frozen class
    matched-clock specificity:                REFUTED
    target divisor / RH claim:                NOT MADE
    fixed self-adjoint generator:             ABSENT
