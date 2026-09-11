# Proof Package

Gate: `OWNER_RED_AMBER/HOLD_EXTERNAL`.

This document expands the mathematical proofs in `main.tex`. It separates the proved four-axis package from the unproved history-set law.

## 1. Frozen definitions and assumptions

Fix (n\ge2).

- Permutation products act rightmost first.
- (c_n=(1\,2\,\cdots\,n)).
- \(\mathcal F_n\) consists of ordered ((n-1))-tuples of transpositions with product (c_n).
- Every transposition is written ((a,b)) with (a<b), and \(\ell((a,b))=a\).
- The right Hurwitz move is
  \[
  H_i(\ldots,x,y,\ldots)=(\ldots,y,yxy,\ldots).
  \]
- (T_n) applies (H_i) at the least adjacent lower-endpoint collision and fixes a state with no collision.
- The tail or depth of a state is the number of nontrivial (T_n)-updates before its first fixed state.

The orientation of (c_n), the right-Hurwitz convention, numeric endpoint ordering, and least-index scheduler are structural assumptions, not cosmetic choices.

## 2. Status table

| Item | Status | Main dependency |
|---|---|---|
| Hurwitz move preserves the product | Proved directly/classical | conjugation identity |
| Executed indices strictly increase | Proved | local collision lemma |
| All recurrent states are fixed | Proved | strict index increase |
| Maximum tail is (n-2) | Proved sharp | strict index increase + witness |
| Fixed count is ((n-1)^{n-2}) | Proved | classical parking bijection + Pollak count |
| Every-target one-step fibre formula | Proved | inverse Hurwitz lemma + scheduler test |
| Maximum indegree (n-1), unique maximizer | Proved | fibre formula + parking inequalities |
| History-set product law for all (n) | Conjecture only | missing all-(n) code/bijection |
| Binomial depth law for all (n) | Conjecture only | sum of history conjecture |
| Unique deepest state for all (n) | Conjecture only | full-history case of conjecture |

## 3. Elementary carrier facts

### Lemma 3.1: Hurwitz preservation

Replacing an adjacent pair ((x,y)) by ((y,yxy)) preserves its product because transpositions are involutions:

\[
y(yxy)=y^2xy=xy.
\]

Therefore every update remains in \(\mathcal F_n\).

### Lemma 3.2: adjacent factors cannot coincide

If two adjacent factors in a member of \(\mathcal F_n\) were the same transposition (x), then (xx=e) would cancel. The long cycle would be expressed using (n-3) transpositions. This is impossible because an (n)-cycle has transposition length (n-1): multiplying by one transposition changes the number of permutation cycles by exactly one, while the identity has (n) cycles and (c_n) has one.

This also covers the only possible degeneracy in the local collision calculation.

## 4. Strictly advancing scheduler

### Lemma 4.1: local collision resolution

Suppose the scheduler is active at (i). Write

\[
\tau_i=(a,b),\qquad \tau_{i+1}=(a,c),\qquad a<b,c.
\]

By Lemma 3.2, (b\ne c). Conjugation by ((a,c)) swaps (a) and (c), so

\[
H_i\big((a,b),(a,c)\big)=\big((a,c),(b,c)\big).
\]

After normalization, the lower endpoints at positions (i,i+1) are

\[
a,\min\{b,c\},
\]

and \(\min\{b,c\}>a\). Thus the collision at (i) disappears.

All positions before (i) are unchanged except that position (i) participates in the comparison at (i-1); its lower endpoint remains (a), so that comparison is unchanged as well. Since (i) was the least old collision, no collision exists at any position (<i) after the move.

### Theorem 4.2: strict histories and recurrence

By Lemma 4.1, after an update at (i), the next update, if it exists, has index (>i). Therefore every history satisfies

\[
1\le i_1<i_2<\cdots\le n-2.
\]

There can be at most (n-2) updates. Every orbit reaches a fixed state. Hence the only recurrent points are fixed points; no nontrivial periodic orbit exists.

### Proposition 4.3: sharp witness

Let

\[
w_n=((1,n),(1,2),(2,3),\ldots,(n-2,n-1)).
\]

The first update replaces ((1,n),(1,2)) with ((1,2),(2,n)). Inductively, at stage (j), the moving factor ((j,n)) meets ((j,j+1)) and becomes

\[
(j,n),(j,j+1)\longmapsto(j,j+1),(j+1,n).
\]

Thus the history is (1,2,\ldots,n-2), and the terminal state is

\[
q_n=((1,2),(2,3),\ldots,(n-1,n)).
\]

The canonical chain (q_n) has product (c_n); Hurwitz moves preserve product, so the backwards-related witness (w_n) also lies in \(\mathcal F_n\). Therefore the upper bound (n-2) is attained.

## 5. Fixed-state census

The classical lower-endpoint map is a bijection

\[
\mathcal F_n\longrightarrow \operatorname{PF}_{N},\qquad
(\tau_1,\ldots,\tau_N)\mapsto
(\ell(\tau_1),\ldots,\ell(\tau_N)),
\]

where (N=n-1) and \(\operatorname{PF}_{N}\) is the set of length-(N) parking functions. This is an external classical input, not a claim proved by the note.

A factorization is fixed exactly when its lower word has (a_i\ne a_{i+1}) for every (i<N). It remains to count adjacent-unequal parking functions.

In Pollak's circular model, preferences are words in \([N+1]^N\). There are

\[
(N+1)N^{N-1}
\]

such words with adjacent letters unequal: (N+1) choices for the first coordinate and (N) choices for each later coordinate. Adding a common residue modulo (N+1) preserves adjacent inequality and acts freely, so every translation orbit has (N+1) words. Circular parking leaves one spot empty, and exactly one translate puts that empty spot at the distinguished final location, producing an ordinary parking function. Therefore the desired count is

\[
\frac{(N+1)N^{N-1}}{N+1}=N^{N-1}=(n-1)^{n-2}.
\]

## 6. Complete one-step inverse atlas

Fix a target (y=(\sigma_1,\ldots,\sigma_{n-1})\). Let (j(y)) be its first collision index, with sentinel (j(y)=n-1) if it is fixed.

### Lemma 6.1: inverse Hurwitz pair

If the target pair is ((u,v)), then the unique inverse at (i) is

\[
H_i^{-1}(u,v)=(uvu,u).
\]

Indeed, applying (H_i) gives ((u,u(uvu)u)=(u,v)).

### Lemma 6.2: exact reverse-admissibility criterion

Write \(\sigma_i=(a,b)\) with (a<b). The two source factors in Lemma 6.1 have the same lower endpoint if and only if \(\sigma_{i+1}\) contains (b) and its other endpoint (c) satisfies (c>a).

To see necessity, conjugating \(\sigma_{i+1}\) by ((a,b)) must yield a transposition with lower endpoint (a), equal to that of \(\sigma_i\). Apart from the impossible coincident-transposition case, this forces \(\sigma_{i+1}=(b,c)\) as an unordered pair. The inverse source pair is then

\[
(a,c),(a,b),
\]

precisely when (c>a). Conversely, these conditions visibly give a lower-endpoint collision in the inverse source.

For this collision to be selected by the least-index scheduler, all earlier comparisons must be collision-free. The inverse changes no position before (i), and therefore this is equivalent to (i<j(y)).

### Theorem 6.3: labelled fibre formula

Each (i<j(y)) satisfying the criterion of Lemma 6.2 contributes the unique nonself predecessor (H_i^{-1}y), and no other nonself predecessor is possible. A self-predecessor exists exactly when (y) is fixed, which is equivalent to (j(y)=n-1). Hence

\[
\operatorname{indeg}(y)=
\mathbf 1_{\{j(y)=n-1\}}+
\#\{i<j(y):i\text{ is reverse-admissible}\}.
\]

This is target-resolved: it identifies each predecessor, not merely the size of an average fibre.

## 7. Maximum fibre and uniqueness

A fixed target has at most one self-predecessor and at most one inverse predecessor for each of the (n-2) indices, so its indegree is at most (n-1). A nonfixed target has no self-predecessor and only indices (i<j(y)\le n-2), hence cannot reach (n-1).

For the canonical chain

\[
q_n=((1,2),(2,3),\ldots,(n-1,n)),
\]

the target is fixed and every index is reverse-admissible: at (i), the next transposition contains the upper endpoint (i+1), and its other endpoint (i+2) exceeds (i). Thus \(\operatorname{indeg}(q_n)=n-1\).

Suppose equality holds for a target (y). Then (y) must be fixed and all (n-2) indices must be reverse-admissible. Write \(\sigma_i=(a_i,b_i)\) with (a_i<b_i). Reverse admissibility at (i) says both endpoints of \(\sigma_{i+1}\) exceed (a_i), so

\[
a_1<a_2<\cdots<a_{n-1}.
\]

This lower word is a parking function. Because it is strictly increasing, its sorted form is itself. Positivity gives (a_i\ge i), while the parking inequality gives (a_i\le i). Hence (a_i=i) for all (i). The classical lower-endpoint bijection has exactly one factorization above this word, namely (q_n). Therefore the maximum is (n-1) and the maximizer is unique.

## 8. Boundary case (n=2)

There is one factorization, (((1,2))), and no scheduler index. It is fixed, has tail zero, and has indegree one. The formulas give

\[
(n-1)^{n-2}=1^0=1,\qquad n-2=0,\qquad n-1=1.
\]

Thus the stated conventions include (n=2) without exception.

## 9. Conjecture quarantine

The unproved statement is

\[
\#\{f\in\mathcal F_n:\operatorname{Hist}(f)=I\}
=(n-1)^{n-2-|I|}
\quad(I\subseteq[n-2]).
\]

Its finite status is:

- exhaustive Python verification for every state and every mask at (2\le n\le8);
- independent C++ streaming verification over all (9^7) Prüfer words and all 128 masks at (n=9);
- no all-(n) Prüfer/history bijection;
- no theorem status for the binomial depth sum, unique deepest state, or derived basin counts.

The static occurrence-set count for a distinguished symbol in a Prüfer word has the same formula, but equality of two enumerators is not a scheduler-compatible bijection. This is the precise missing step.

## 10. Residual proof risks

- The classical lower-endpoint bijection is imported and must retain an accurate citation.
- The inverse atlas is orientation-sensitive; using the inverse cycle or inverse Hurwitz convention requires a new proof and may fail.
- The phrase "complete fibre" means complete for one-step labelled predecessors only. Higher fibres have a finite reverse dynamic program but no asserted uniform closed form.
- The computational history law must never be used as a lemma in the four proved axes.
- Owner clearance is a literature question, not a mathematical corollary. It remains unresolved under `HOLD_EXTERNAL`.
