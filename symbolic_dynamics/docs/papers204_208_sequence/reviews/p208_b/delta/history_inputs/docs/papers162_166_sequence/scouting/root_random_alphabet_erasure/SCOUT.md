# Random alphabet-erasure dynamics on finite words

**Handle:** `RAE`  
**Date:** 2026-09-03 UTC  
**Author decision:** `GREEN_PENDING_INDEPENDENT_HOSTILE_GATE`  
**External:** `HOLD_EXTERNAL`

## Literal system and early signal

Fix an alphabet (A) of size (q\ge2).  For (a\in A), let (E_a(w))
delete every occurrence of (a) from the finite word (w), preserving the
order of all other letters.  At each epoch choose (a\in A) independently
and uniformly and apply (E_a).  On words of length at most a fixed cap
(L), this is a finite random dynamical system with the empty word as its
unique common absorbing state.

The generators commute and are idempotent.  A history
\(h=(h_1,\ldots,h_t)\) therefore acts only through its support:

\[
 E_{h_t}\cdots E_{h_1}(w)=\pi_{A\setminus\operatorname{supp}(h)}(w), \tag{1}
\]

where \(\pi_B\) is the standard alphabet projection.  Coupon collection owns
the clock hidden in (1) and receives zero credit.  The residual candidate is
the exact word-sensitive transition kernel together with a closed
all-source/every-target history-fibre spectrum across every source length.

## Theorem A — arbitrary-source transition kernel and absorption law

Let (u,v\) be finite words.  Put (B=\operatorname{supp}(v)) and
\(D=\operatorname{supp}(u)\setminus B).  The number of histories
\(h\in A^t\) sending (u) to (v) is zero unless

\[
 B\subseteq\operatorname{supp}(u),\qquad \pi_B(u)=v.       \tag{2}
\]

When (2) holds, it is exactly

\[
 K_t(u,v)=\sum_{j=0}^{|D|}(-1)^j\binom{|D|}{j}
                    (q-|B|-j)^t.                           \tag{3}
\]

Indeed, a valid history avoids every retained letter in (B), hits every
deleted letter in (D), and may freely use letters absent from (u);
inclusion--exclusion gives (3).  Thus (3)/(q^t) is the complete (t)-step
Markov kernel, including zero-probability targets and holding histories.

If (w) uses (b) distinct letters and \(\tau_w\) is its absorption time,
then

\[
 \Pr(\tau_w\le t)=q^{-t}\sum_{j=0}^b(-1)^j\binom bj(q-j)^t,
 \qquad \mathbb E\tau_w=qH_b.                              \tag{4}
\]

The largest mean among words of length at most (L) is
\(qH_{\min(q,L)}\), attained exactly when the support is maximal.  Conditional
on the initial support, every letter is equally likely to be the last one
remaining, so the last nonempty word is each monochromatic projection with
probability (1/b).

At operator level, the probability that a length-(t) history has exactly
(s) distinct erasers is

\[
 \frac{(q)_s\,\left\{\begin{smallmatrix}t\\s\end{smallmatrix}\right\}}
      {q^t}.                                                \tag{5}
\]

Its image on words of length at most (L) has exactly
\(\sum_{m=0}^L(q-s)^m\) elements.  Equation (5) is consequently the complete
random-map image-size distribution.

## Theorem B — all-source/every-target history fibres

Fix a target word (v) of length (m) using (b) letters.  For every source
length (n\ge m), let \(A_{q,t,n}(v)\) count pairs
\((u,h)\in A^n\times A^t\) with (E_h(u)=v).  Then

\[
 A_{q,t,n}(v)=\binom nm
 \sum_{s=0}^{\min(q-b,t)}(q-b)_s
 \left\{\begin{matrix}t\\s\end{matrix}\right\}s^{n-m},  \tag{6}
\]

with (0^0=1).  Equivalently, the complete source-length series is

\[
 \sum_{n\ge m}A_{q,t,n}(v)z^n
 =z^m\sum_{s=0}^{\min(q-b,t)}
 \frac{(q-b)_s\left\{\begin{smallmatrix}t\\s\end{smallmatrix}\right\}}
      {(1-sz)^{m+1}}.                                      \tag{7}
\]

**Proof.**  Fix a history support (H\subseteq A\setminus B) of size (s).
There are (s!\left\{\begin{smallmatrix}t\\s\end{smallmatrix}\right\})
histories with that support.  A source is formed by choosing the (m)
ordered positions occupied by (v), then filling the other (n-m) positions
arbitrarily from (H), giving \(\binom nm s^{n-m}\).  Choose (H) and sum.
The binomial-series identity yields (7).

This is also a complete target spectrum: among length-(m) targets, exactly

\[
 (q)_b\left\{\begin{matrix}m\\b\end{matrix}\right\}       \tag{8}
\]

have support size (b), and all have the value (6).  Summing (6) over every
target of every length (0\le m\le n) gives the global mass (q^{n+t}), as
each source/history pair has one output.

The proof mechanisms of (3)--(5) and (6)--(8) are separated: the first fixes
a source and resolves required/forbidden coupons; the second fixes a target
and reconstructs every source by ordered-position insertion before summing
history supports.

## Evidence and claim boundary

`verify_scout.py` independently checks the commuting idempotent action,
history-support distribution, all feasible and infeasible transitions,
absorption CDF, every target class, (6), (8), and all mass identities.  The
frozen output is `CANONICAL.txt`; enumeration is counterexample pressure, not
proof.

Alphabet projection, Stirling surjection counts, binomial insertion, and the
classical coupon collector all receive zero contribution credit.  A bounded
search found ordinary position-deletion/erasure channels and static formal-
language projection, but no inspected record for this random all-occurrences
erasure action with (3) and the source/history spectrum (6)--(8).  A non-hit
is not a novelty, priority, or circulation claim.  Independent hostile owner
and P1--P161 review is required before allocation.

