# Reserve theorem package LFS — random linear-form sieve

**Lane status:** `THEOREM_COMPLETE_RESERVE / R7_AND_MEET_WALK_RISK /
HOLD_EXTERNAL`.

## Literal chain

Let (X\subseteq V\setminus\{0\}) be a fixed finite represented point
configuration in (V=\mathbb F_q^d), with proportional copies removed if a
projective carrier is desired.  A state is (A\subseteq X).  Independently
sample a uniform linear form (ell\in V^*), including zero, and set

\[
 A\longmapsto A\cap\ker\ell.                         \tag{1}
\]

The carrier is the full subset lattice of a vector configuration, not the
subspace lattice used by the historical `R7` reserve.

## Exact theorem

Let (r(S)=\dim\langle S\rangle).  For (B\subseteq A\) and (t\ge1), the
ordered form-history count for endpoint (B) is

\[
 N_t(A,B)=\sum_{C\subseteq A\setminus B}
 (-1)^{|C|}q^{t\{d-r(B\cup C)\}}.                   \tag{2}
\]

It is zero automatically when the target is not closed relative to the
intersection (A\cap\langle B\rangle).  Consequently:

1. (P^t(A,B)=N_t(A,B)/q^{dt}) is an every-source, every-target,
   every-time kernel.
2. For absorption of a nonempty (A) at the empty set,

   \[
   \Pr_A(T\le t)=\sum_{C\subseteq A}(-1)^{|C|}q^{-t r(C)},
   \quad
   \mathbb E_A T=\sum_{\varnothing\ne C\subseteq A}
   {(-1)^{|C|+1}\over1-q^{-r(C)}}.                  \tag{3}
   \]

3. The zeta functions (g_C(A)=\mathbf1_{C\subseteq A}) form an eigenbasis
   with eigenvalue (q^{-r(C)}).  The chain is diagonalizable, and the
   multiplicity of (q^{-j}) is the number of subsets of (X) having rank
   (j).

Indeed, after (t) steps the survivor condition for (x) is
((\ell_1(x),\ldots,\ell_t(x))=0).  Requiring this on (B) and excluding it
for every (x\in A\setminus B) gives (2) by inclusion--exclusion.  Summing
the absorption tail gives (3).  Finally

\[
 \mathbb E[g_C(A\cap\ker\ell)]
 =\mathbf1_{C\subseteq A}\Pr(\ell|_{\langle C\rangle}=0)
 =q^{-r(C)}g_C(A),
\]

and Boolean zeta functions are a basis.

## Gate

The all-time formula is a characteristic/Tutte-polynomial evaluation of a
represented matroid, and generic meet-walk diagonalization is direct
semilattice background.  More importantly, `R7` already records iid ambient
hyperplane intersection, albeit only on the subspace lattice and only at the
dimension-chain level.  The configuration-level every-target lift is exact
progress, but it remains a reserve behind RHT unless a hostile audit proves
that it is more than the natural matroid completion of `R7`.

