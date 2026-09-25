# Global coprime memory excludes source returns and invariant probability

**Paper ID:** `367-global-coprime-memory`  
**Candidate:** `ANG-SCREEN-20260921-GCM01`; batch `LONG-MEMORY-20260921-D`, round 3/5.  
**Date / status:** 2026-09-21; `FULL-HISTORY SOURCE FREE; NO INVARIANT PROBABILITY — PRE-P0 STOP / FORK`.  
**Scope:** exact source theorems; no supplied measure, clock or flow. Formal coordinates `UNASSIGNED`; Route B `NOT INVOKED`.

## Abstract

The complete two-sided language of integers at least two with pairwise coprime entries is nonempty, closed and shift-invariant, and its shift is a homeomorphism. Every finite admissible assignment extends to this full source without restricting the alphabet to primes. Nevertheless every coordinate value can occur only once: the entire integer action is free, and an independent wandering-cylinder argument excludes every invariant Borel probability. Finite-window coprimality controls have explicitly characterized periodic words and invariant probabilities on their own periodic orbits. The global language does not permit repetition of even one nonempty admissible word, so a full-path return-word splicing assumption cannot be imported from a local transition presentation. These are source-level results, not the construction or failure of an unspecified IMAGE law. The frozen screen stops before P0.

## 1. Identity and same-object ledger

| Item | Exact owner or boundary |
| --- | --- |
| Source | Entire \(X=\{x\in\{2,3,\ldots\}^{\mathbb Z}:\gcd(x_i,x_j)=1\text{ for }i\ne j\}\) |
| Evolution | Left shift \((Tx)_i=x_{i+1}\), with full inverse right shift |
| Topology / Borel | Subspace of the product of discrete alphabets; its Borel sigma-algebra |
| Source arrows | Every \((k,x):x\to T^kx\), \(k\in\mathbb Z\); labels retained |
| Controls | Entire ADJACENT, WINDOW-TWO and FREE sources in Section 7 |
| Measure / IMAGE / roof / flow | Not supplied; no normalization or time selected |
| Symplectic / Hamiltonian / operator owner | Not supplied; classical fields not applicable |

The [frozen card](candidate-card.md) is the contract. All proofs below concern that source or one explicitly named control, never a selected recurrent subset.

## 2. Arithmetic interface and allowed data

Write \(A=\{2,3,\ldots\}\). For every ordinary integer \(d\ge2\), the divisor readout at coordinate \(i\) is \(e_{d,i}(x)=1_{d\mid x_i}\). Membership in \(X\) means that, for each \(d\), at most one coordinate has \(e_{d,i}=1\). Indeed a common divisor greater than one violates coprimality, and a gcd greater than one is itself such a witness. Under \(T\), these readouts obey \(e_{d,i}(Tx)=e_{d,i+1}(x)\).

This realizes the [prior-work lineage](../../docs/prior_work/README.md) as divisor-witness exclusion extended from adjacent coordinates to the whole history. It is a stated deformation of admissibility, not a prime-sieve theorem, prime-labelled alphabet, or Logistic/Hénon conjugacy. Composite symbols remain allowed. No external prime table, per-prime parameter or logarithmic roof is used.

## 3. The complete source exists and owns both time directions

**Proposition 1 (extension and topology).** Every finite assignment of mutually coprime values in \(A\) to distinct integer coordinates extends to an element of \(X\). The space \(X\) is nonempty, closed and Borel in \(A^{\mathbb Z}\), and is noncompact.

**Proof.** Enumerate the unassigned coordinates. At each stage let \(P\) be the product of the finitely many assigned values, using \(P=1\) if there are none, and assign \(P+1\) to the next coordinate. This value is at least two and is coprime to every earlier value. Induction fills all coordinates and proves the extension assertion; starting with no assignment proves nonemptiness. This is an existence witness, not a selected source orbit or measure.

For fixed \(i\ne j\), the condition \(\gcd(x_i,x_j)=1\) is clopen because \(A^2\) is discrete. Their countable intersection is \(X\), so \(X\) is closed and Borel. The coordinate projection \(x\mapsto x_0\) is continuous and, by the extension assertion, maps \(X\) onto the infinite discrete set \(A\). A compact space cannot have that continuous image, proving noncompactness. The product topology is metrizable and second-countable: finite-coordinate cylinders form a countable base. QED.

In particular the finite block language consists exactly of words whose distinct positions have pairwise coprime values. This is a consequence of extension, not a substitution of a finite-window language or another closure for \(X\).

**Proposition 2 (full inverse and arrows).** \(T:X\to X\) is a homeomorphism with \((T^{-1}x)_i=x_{i-1}\). The full action groupoid has composition

\[
(k,T^\ell x)\circ(\ell,x)=(k+\ell,x),\qquad
(k,x)^{-1}=(-k,T^kx).
\]

**Proof.** Translating coordinate indices preserves every pairwise gcd condition. Both coordinate shifts are continuous and mutually inverse on the entire source. The displayed formulas are the integer-action identities. Give the groupoid the product topology on \(\mathbb Z_{\mathrm{discrete}}\times X\) and its Borel structure. For every target \(y\), all incoming arrows are exactly \((k,T^{-k}y)\), for every integer \(k\). Thus there is no missing predecessor, terminal, finite-history cutoff or omitted negative-time history. QED.

## 4. Free action and the separate invariant-probability obstruction

**Theorem 3 (all source isotropy).** For every \(x\in X\), \(\{k\in\mathbb Z:T^kx=x\}=\{0\}\). Moreover no point returns at a nonzero iterate to its own one-coordinate cylinder.

**Proof.** If \(T^kx=x\) with \(k\ne0\), then \(x_k=x_0\), contradicting \(\gcd(x_0,x_k)=1\), since \(x_0\ge2\). More generally the cylinder \(C_a=\{x\in X:x_0=a\}\) cannot contain both \(x\) and \(T^kx\) for \(k\ne0\): the value \(a\) would occur at two coordinates. All integer labels remain in the groupoid; the assertion classifies its actual isotropy rather than removing it. QED.

**Theorem 4 (no invariant Borel probability).** There is no \(T\)-invariant Borel probability measure on \(X\).

**Proof.** Suppose \(\mu\) were such a probability. Fix \(a\ge2\). The Borel sets

\[
T^{-k}C_a=\{x\in X:x_k=a\},\qquad k=0,1,2,\ldots,
\]

are pairwise disjoint by the gcd constraint. Invariance assigns all of them the same mass \(\mu(C_a)\). Their first \(N\) members have total mass \(N\mu(C_a)\le1\) for every positive integer \(N\), hence \(\mu(C_a)=0\). But \(X=\bigsqcup_{a\ge2}C_a\), so countable additivity gives \(\mu(X)=0\), a contradiction. QED.

The second theorem is not inferred merely from the absence of periodic points: it uses the disjoint translates of a countable Borel cover. Both arguments depend on the lower bound two. Allowing a reusable unit would invalidate the repeated-value contradiction; that altered alphabet is not silently substituted here. No assertion is made that all nonsingular or sigma-finite measures are impossible.

## 5. Infinite memory and the precise splicing boundary

**Proposition 5 (no bounded-window replacement).** No fixed finite window length determines this language. If a nonempty finite word \(w\) occurs in \(X\), the concatenation \(ww\) does not occur in \(X\).

**Proof.** For a window length \(L\ge1\), choose \(L\) pairwise coprime values by the construction of Proposition 1 and periodically repeat that length-\(L\) word. Every window of length at most \(L\) has pairwise coprime entries, hence extends to \(X\), but the periodic sequence repeats each entry and is not in \(X\). Therefore no rule checking only those windows can characterize \(X\). For the second assertion, the first entry of \(w\) occurs twice in \(ww\), contradicting the full-history gcd condition. QED.

The relevant full-Markov-path splicing premise of the 364 comparison is that an actual closed edge word at a vertex may be concatenated with itself and periodically extended while remaining in the complete path source. Here an admissible segment \(w\) is not an actual closed return word: \(ww\) is forbidden. Identifying only local endpoints would forget the already-used divisor witnesses. For example the adjacent cycle \(2,3,2,3,\ldots\) satisfies local adjacent coprimality but is not a point of \(X\).

This does not assert that no enlarged graph presentation of any kind exists. A faithful presentation must retain the global constraint and cannot manufacture a closed return from that local cycle. No theorem or clock from 364 is transferred; the word-level failure is proved directly above.

## 6. Conditional cocycle consequence, not a clock construction

If a real additive cocycle \(c\) were supplied on this exact full action groupoid, then \(c(0,x)=0\) by the cocycle identity. Theorem 3 would therefore imply

\[
c(G_x^x)=\{0\}\quad\text{for every }x\in X.
\]

This is conditional on that owner and cocycle. It does not assert that \(c\) vanishes on non-isotropy arrows, provide a measure or IMAGE derivative, or construct a real extension. Under a packet convention based on the image of full source isotropy, such a supplied cocycle could not produce a positive cyclic-return packet. A different arrow relation or physical flow would require a different definition, not inheritance of this statement.

## 7. Three complete source-level controls

For \(R=1,2\), let \(X_R=\{x\in A^{\mathbb Z}:\gcd(x_i,x_j)=1\text{ whenever }0<|i-j|\le R\}\). Set \(X_{\rm free}=A^{\mathbb Z}\). These are respectively ADJACENT, WINDOW-TWO and FREE, each with its own product-subspace topology/Borel, left shift \(T_Y\) and inverse right shift.

**Proposition 6 (control owners and all periodic admissibility).** All three are closed, nonempty sources with globally invertible shifts. Each owns the full groupoid \(\mathbb Z\ltimes Y\); incoming arrows at \(y\) are precisely \((k,T_Y^{-k}y)\). For every point its source-isotropy group is \(\{k:y_{i+k}=y_i\text{ for all }i\}\), which is either \(\{0\}\) or \(d\mathbb Z\), where \(d\) is its least positive period.

For a word \(w=(w_0,\ldots,w_{n-1})\), \(n\ge1\), let \(w^\infty\) denote its two-sided periodic repetition. The complete tests are:

| Source | Necessary and sufficient condition for \(w^\infty\) |
| --- | --- |
| ADJACENT | \(\gcd(w_i,w_{(i+1)\bmod n})=1\) for all \(0\le i<n\) |
| WINDOW-TWO | \(\gcd(w_i,w_{(i+s)\bmod n})=1\) for all \(0\le i<n\), \(s=1,2\) |
| FREE | Every word in \(A^n\) is allowed |

**Proof.** The local gcd conditions are intersections of clopen cylinder conditions, so their sources are closed. Shift and inverse preserve the distance between indices, hence preserve each source; the full-action and incoming formulas follow without discarding any state. The displayed periodic tests follow by reducing each tested index modulo \(n\), and conversely check every required pair of a repeated word. In particular they include the self-pair obstruction when a tested distance is a multiple of \(n\).

For any sequence its period set is a subgroup of \(\mathbb Z\). If nontrivial, its least positive member \(d\) generates that subgroup: division with remainder would otherwise produce a smaller positive period. For a displayed \(n\)-periodic word, \(d\mid n\) and is the least divisor satisfying \(w_{(i+d)\bmod n}=w_i\) for all \(i\). Thus a nonprimitive written word is not counted as a new primitive source orbit. Nonemptiness and the following existence claims are witnessed explicitly. QED.

| Source | Actual periodic point | Least discrete period |
| --- | --- | --- |
| ADJACENT | \((2,3)^\infty\) | 2 |
| WINDOW-TWO | \((2,3,5)^\infty\) | 3 |
| FREE | \(2^\infty\) | 1 |

The first two examples satisfy their own cyclic gcd tests; their displayed distinct entries prove the stated least periods. For each example \(y\) with least period \(d\), the measure \(\nu_y=d^{-1}\sum_{j=0}^{d-1}\delta_{T_Y^jy}\) is a Borel probability on that control, and is invariant because its shift cyclically permutes the summands. These are existence tests, not canonical or full-support laws. Every other periodic word is governed by the full rules above; no finite enumeration replaces them. The discrete periods are not physical times, and none of these controls supplies MAIN's missing clock or extension.

## 8. Gate assessment and decision

| Gate | Exact evidence / status |
| --- | --- |
| T0, source only | Nonempty closed source, complete inverse and full action established |
| T1 | `NOT TESTABLE`: no measure/IMAGE clock supplied |
| T2, source gate only | Every actual source-isotropy group trivial; no invariant Borel probability |
| T3 | `NOT AUDITED`; operator/trace/zeta not supplied |
| Classical A0/A1/A2 | `NOT APPLICABLE`; no classical geometric candidate |
| Formal Route / B | `UNASSIGNED` / `NOT INVOKED` |

**Decision: PRE-P0 STOP / FORK.** Full-history divisor exclusion is exact but removes the source returns sought here. The control sources show that this is not a conclusion about all coprimality constraints or all symbolic dynamics. No alphabet repair, selected orbit, substitute measure, roof or geometric lift is appended to preserve this candidate.

## Reproducibility, provenance and declarations

The mathematical input is the complete [67-line original contract](candidate-card.md); the source proofs and controls above are exact and contain no orbit computation, cutoff, precision choice or external theorem dependency. Root owns the other package records and independent review. This author read the complete original card and [paper template](../paper-template.md), not a peer proof or new independent result.

The same author previously returned a definition-reserve `NONE` because a complete measured inverse/IMAGE interface was missing. This source screen changes the immediate question and does not fill that gap. Historical 065/125 information in the card is root-reported provenance; those packages were not opened for this proof. Shared-history internal work remains `NOT_CALIBRATED`; there is no priority claim, external literature search or publication-readiness claim.

Data availability: all definitions and exact derivations are in this Markdown record; no experimental dataset exists. Ethics: no human subjects or private data are involved. Contributions: the task-scoped AI author derived and drafted this paper; root owns contract, integration and review coordination, without implying human CRediT attribution. Funding and conflicts: no declarations were supplied; none are inferred. AI use: this is an AI-assisted internal mathematical source screen, not independent external peer review.
