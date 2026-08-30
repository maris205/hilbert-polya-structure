# P122 hostile review A — even record-block reversal

**Review status:** first independent nonauthor review, round 0  
**Manuscript examined:** `main.tex` and the frozen `main_round0_original.pdf`  
**Decision:** **MAJOR — STOP/REWRITE**  
**External status:** **HOLD**, irrespective of the internal decision

I did not inspect, solicit, or wait for a second-review report. I made no
change to the manuscript, bibliography, verifier, or supporting documents.
The recommendation is not a rejection of the mathematical core: the three
principal all-size statements survive reconstruction, and the exact controls
pass. The stop is required because (a) a current reference is misattributed,
(b) the five-bit automaton is a central residual claim but its invariant and
initialization are underdefined in the paper, and (c) the manuscript does not
perform the necessary explicit subtraction against the closest papers in the
P1--P121 internal portfolio.

## 1. Scope and claim ceiling

I checked the literal operator, every displayed recurrence and inverse
construction, the paper-local support documents, all three Python files and
their stored transcript, all four bibliography records, and every page of the
frozen PDF. The contribution ceiling I used is deliberately severe:

* Foata's record-block/cycle transfer and the all-odd-cycle fixed-point count
  earn zero credit;
* relative-rank/record-indicator weights earn zero credit;
* lexicographic termination by the first changed block earns essentially zero
  credit;
* a bounded literature non-hit is not evidence of novelty or priority;
* the residual value must therefore come from the exact target-fibre
  bijection, the all-size image/Garden recurrence, and (secondarily) the sharp
  clock for this literal synchronous operator.

Under that ceiling, the residual is potentially sufficient for a short note,
but only if its two principal mechanisms are written so that a reader can
audit them without reverse-engineering the code, and only if the internal and
external owner firewalls are corrected.

## 2. Reconstruction of the dynamics and clock

Let a record factorization be
\(\pi=B_1\cdots B_k\), where each block begins at a left-to-right maximum.
The first entry of each \(B_i\) is its maximum, and these first entries
increase strictly. The claimed lexicographic descent is correct: if \(B_i\)
is the first even block, all preceding blocks are unchanged and reversal
replaces the maximum at the first changed position by the strictly smaller
last entry of \(B_i\). Thus \(\Phi(\pi)<_{\mathrm{lex}}\pi\), and a finite
state space has no nontrivial directed cycle.

The depth induction in Theorem 2.1 is also sound. Write
\(\pi=\alpha n\beta\).

* If \(|\beta|\) is even, the last block \(n\beta\) has odd length. It is
  unchanged, remains the final record block under every subsequent update,
  and the prefix evolves independently as \(\alpha\). Its depth is therefore
  at most \(|\alpha|-1\le n-2\) when nonempty.
* If \(|\beta|\) is odd, the last block is even and
  \[
  \Phi(\pi)=\Phi(\alpha)\operatorname{rev}(\beta)n.
  \]
  The final \(n\) is thereafter an inert singleton. The preceding \(n-1\)
  letters are an arbitrary distinct-letter word, so standardization and the
  induction hypothesis give at most another \(n-2\) steps. Hence the total is
  at most \(n-1\).

For \(\omega_n=(2,3,\ldots,n,1)\), only \((n,1)\) is even, and
\(\Phi(\omega_n)=\omega_{n-1}n\). Therefore its depth is exactly \(n-1\).
I found no missing parity case or exceptional small \(n\). The fixed-point
formulas in (2.4) are consistent with all-odd cycles, but, as the manuscript
acknowledges, are controls rather than contribution.

## 3. Admissible-cut fibre theorem: hostile inverse audit

For a target \(\sigma\), write \(M_j=\max(\sigma_1,\ldots,\sigma_j)\).
The necessity of (3.2) is correct. An odd source block is retained, so its
maximum is the first target entry of the corresponding segment. An even
source block is reversed, so its maximum is the last target entry. Since
source block maxima increase, that endpoint is the maximum of the whole
target prefix ending at the segment.

The more vulnerable direction is the inverse. Given an admissible sequence
\(0=i_0<i_1<\cdots<i_k=n\), retain odd target segments and reverse even target
segments. For segment \(r\), condition (3.2) puts \(M_{i_r}\) first in the
reconstructed **source** segment. This really yields the claimed record
factorization:

1. the occurrence carrying \(M_{i_r}\) lies in
   \((i_{r-1},i_r]\), whereas \(M_{i_{r-1}}\) occurs in the earlier prefix;
2. entries are distinct, so \(M_{i_r}>M_{i_{r-1}}\);
3. every other entry of the reconstructed segment is less than its first
   entry \(M_{i_r}\), so no interior left-to-right maximum is introduced;
4. consequently the selected boundaries, and no others, are the source's
   record cuts;
5. reversing precisely its even blocks restores the target segments.

Uniqueness follows because a source permutation has a unique record
factorization. Thus the proposed cut-to-source construction is injective as
well as surjective. The last-cut decomposition then gives (3.3) and
\(|\Phi^{-1}(\sigma)|=h_n\). I found no counterexample to the theorem or DP.

There are two presentational weaknesses. Line 190 calls a reconstructed
source segment a “new target segment,” which points the inverse proof in the
wrong semantic direction. More importantly, the paper supplies no worked
target showing all admissible cut sequences and their reconstructed sources.
For the principal residual theorem, one complete example is required, not
cosmetic.

## 4. Five-bit state: derivation and missing invariant

The automaton is mathematically recoverable, but the manuscript makes the
reader reconstruct several definitions. The clean invariant is as follows.
Set \(d_0=1\). After position \(j\), define
\[
E_j=\bigvee_{0\le i\le j,\ i\text{ even}}d_i,
\qquad
O_j=\bigvee_{0\le i\le j,\ i\text{ odd}}d_i.
\]
Let \(\ell_j\) be the most recent record position, set
\(Q_j=d_{\ell_j-1}\), \(L_j=\ell_j\bmod2\), and \(D_j=d_j\).
Then \(s_1=(1,1,1,1,1)\) follows from \(d_0=d_1=1\).

For an odd final segment ending at \(j\), its first target entry must be
\(M_j\). It must therefore begin at the latest record \(\ell_j\), and it is
admissible exactly when
\[
d_{\ell_j-1}=1,
\qquad j\equiv \ell_j\pmod2.
\]
For an even final segment, the last target entry must be \(M_j\); hence
\(j\) must itself be a record, and there must be a reachable preceding cut
of the same parity as \(j\). At a record \(j\), the odd candidate is the
length-one segment and contributes \(D_{j-1}\); the even candidate contributes
\(E_{j-1}\) for even \(j\), or \(O_{j-1}\) for odd \(j\). At a nonrecord only
the odd candidate exists. These observations produce (4.3)--(4.4), after
which \(D_j\) is ORed into the corresponding parity accumulator.

So the recurrence is correct, including the base state. However, the paper
never explicitly states \(d_0=1\), never specifies the quantifier ranges in
the definitions of \(E_j,O_j\), and compresses the inductive preservation of
all five coordinates into a few sentences. Since the automaton is one of only
two main residual contributions, this is a **major proof-completeness issue**,
even though it is readily repairable. A short Boolean transition table or a
fully explicit invariant-and-induction paragraph is required. A single bit
trace on a nontrivial record word should accompany it.

The transfer weights themselves are correct. The relative-rank code is a
bijection
\(\mathfrak S_n\longleftrightarrow[1]\times[2]\times\cdots\times[n]\).
At position \(j\), rank \(j\) is the unique record choice and the other
\(j-1\) ranks are nonrecords. Hence a record set \(S\ni1\) has weight
\(\prod_{j\notin S}(j-1)\), and the matrices in (4.5) count all targets of
each record word exactly once. “These ranks range independently” should be
replaced by this explicit bijection, but there is no mathematical error.

## 5. Exact controls and reproducible build

I reran the paper-local verifier from the paper directory:

```text
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
record-block reversal fibre verifier: PASS
assertions=1636476
record-block image automaton: PASS
assertions=551
combined_assertions=1637027
```

The literal lane exhausts sources and targets through \(n=9\); the independent
record-word transfer agrees through \(n=9\) and continues through \(n=30\).
The image sequence through \(n=9\) is
\[
1,1,1,4,12,60,320,2160,15960,138880.
\]
The stored transcript has SHA-256
`f696fb468ff4de65f82d755079634da55271853310ca442736d51f43e085f5dc`.
The verifier hashes at review time were:

```text
verify.py           75f04bc6e5ebe6d0c807d131af3873bd7df98fb582628d69b8e2a8f351aa07b4
fibre_verify.py     ffbedd6caeea5b09e4ac905c06651348ec87463ee127d73807ad8c93b1dd6e46
image_automaton.py  e9fb3c83d23bfdcb5e92232d0226453fd7bf68dff041412afb18f20f7b158f11
```

I also built in a fresh temporary directory containing only `main.tex` and
`references.bib`, using the required four stages
`pdflatex -> bibtex -> pdflatex -> pdflatex`. All four commands exited zero;
the final stage had no LaTeX warnings or unresolved citations. The isolated
PDF SHA-256 was
`55fe14d1be59856d79924d16876f19c91c767ed88f5c25a8d4f7b5d71ba61991`,
identical to both `main.pdf` and `main_round0_original.pdf`.

I rendered and visually inspected all four A4 pages. There is no clipping,
overlap, missing glyph, broken reference, or unresolved citation marker. All
fonts are embedded/subsetted and carry Unicode mappings. Page 4 has generous
unused space, which is not a defect but removes any page-pressure excuse for
omitting the needed collision table, explicit automaton invariant, or example.

These controls are unusually strong falsification evidence. They do not
repair an underwritten all-size proof and do not establish ownership.

## 6. External owner subtraction

The bounded search found no source stating this literal even-record-block
reversal, the admissible-cut inverse, or the five-bit image state. That is only
a bounded non-hit. The present source control needs the following repairs.

1. **Huang metadata is wrong.** The current arXiv record for
   [2607.22767](https://arxiv.org/abs/2607.22767) lists **Pyuyi Chufeng
   Huang**, not “Jang Soo Huang.” A live 2026 neighbor cannot be cited under
   the wrong author. The title and author order should be copied from the
   current primary record and checked again at repair time.
2. **Bouvel--Cioni--Ferrari should use the published record.** *Preimages
   under the Bubblesort Operator* appeared in *Electronic Journal of
   Combinatorics* 29(4), P4.32 (2022),
   [DOI 10.37236/11390](https://doi.org/10.37236/11390). The manuscript's
   arXiv-only entry understates the direct neighboring owner. That paper owns
   left-to-right-maximum descriptions of bubblesort preimages and functional
   trees; it does not, from the material inspected, own this literal map.
3. **The Foata pointer is too diffuse for the exact deduction.** The cited
   Foata--Han paper exists, but the manuscript must point to the precise
   transformation/proposition that sends maximum-first cycles to
   left-to-right-maximum blocks, or use a more direct original/standard
   source for that exact correspondence. A generic “see, for example” is not
   adequate when the fixed-point count is explicitly being subtracted.
4. **Broaden the record-operator neighbor check.** At minimum the repair
   should inspect and, if relevant, discuss Cioni--Ferrari's queuesort
   preimage work ([arXiv:2102.07628](https://arxiv.org/abs/2102.07628)) and
   explain why its recursive left-to-right-maximum fibres do not contain the
   present admissible-cut mechanism. This is a firewall request, not an
   assertion of collision.
5. **Clarify Huang's relevance.** The inspected arXiv paper concerns greedy
   record statistics/order polynomials and record-set fibres, not the literal
   permutation self-map. The manuscript should say exactly which method is
   neighboring and which residual theorem remains after subtraction; merely
   calling it a “current record/fibre neighbor” is too vague.

Until these metadata and subtraction defects are repaired, no novelty or
priority language is supportable. The current explicit external HOLD is
correct and must remain.

## 7. P1--P121 internal collision audit

The support plan promises a collision firewall, but the manuscript contains
no explicit internal comparison. That omission is material because several
portfolio papers share its silhouette.

| Internal neighbor | Genuine overlap | Residual distinction that P122 must state |
|---|---|---|
| **P105, cycle-minimum pruning dynamics** | Same carrier \(\mathfrak S_n\); acyclic functional graph; sharp maximum depth \(n-1\); exact one-step fibres and Garden-of-Eden criterion. This is the highest-risk collision. | P105 has a cycle-minimum deletion/pruning mechanism and a stronger temporal package (iterate normal form/depth layers). P122's defensible residue is the adaptive record-block reversal, target-cut fibre bijection, and record-word finite-state image census. Generic “permutation dynamics + \(n-1\) + fibres/GOE” is already spent. |
| **P117, odd-run reversal on cyclic words** | Synchronous parity-selected reversal of maximal blocks and sharp linear transients. | Different carrier and boundary mechanism: binary cyclic run boundaries erode, whereas P122 reparses left-to-right record blocks after each update and terminates by lexicographic descent. |
| **P120, odd-fringe mirror on plane trees** | Simultaneous parity-triggered reversal/mirroring. | Plane-tree topology is invariant and the map is involutive with periods at most two; P122 is a terminating permutation map with adaptive record cuts. |
| **P112, tournament-score upset reversal** | Synchronous reversal language, termination, and an \(n-1\)-type recursive clock. | Edge-score energy and tournament structure are unrelated to the record-cut fibre and automaton. The overlap is architectural, not theorem identity. |

P108 and other papers with exact image/fibre/Garden packages supply a generic
portfolio template but not a literal carrier or mechanism collision. The
manuscript need not enumerate every such paper. It must, however, include at
least P105, P117, and P120 explicitly and limit its sales language to the
target-cut bijection and aggregate record-state recurrence. Without this
comparison, the internal originality claim has not been earned.

## 8. Contribution sufficiency

After all owner deductions, the clock alone is not paper-scale, and the fixed
enumeration has zero value credit. The combination of the following two
results is nevertheless plausibly sufficient for a concise paper:

* a pointwise, invertible description of every one-step fibre by admissible
  target cuts, including an exact target-local fibre DP; and
* a genuinely all-size finite-state aggregation of image membership and
  Garden-of-Eden counts over record words.

These are different results: the first retains fibre multiplicity for one
target, while the second discards multiplicity and aggregates nonempty-fibre
membership over all targets. The sentence after the residual list currently
says “The second and third items are distinct: the first ... whereas the
second ...”; this pronoun sequence is confusing and should explicitly say
“items (ii) and (iii)” and name each one.

The value verdict is therefore **not KILL**. It is **conditional short-paper
value**: sufficient after the central automaton proof is made self-contained,
the inverse is illustrated, and P105 is explicitly subtracted. Claims about
maximum indegree, all depth layers, iterated fibres, finite-state minimality,
asymptotics, first occurrence, novelty, or priority must remain outside the
paper unless separately proved and owner-checked.

## 9. Findings by severity

### CRITICAL

None. I found no false theorem, failed inverse, invalid transition, incorrect
boundary case, or reproducibility failure.

### MAJOR

**M1 — Bibliographic identity/source-integrity failure.** `Huang2026` names
the wrong author, Bouvel--Cioni--Ferrari is not represented by its published
record, and the exact Foata correspondence is not pinned to a precise source.

**M2 — Central five-bit lemma is underdefined.** The paper must define
\(d_0\), the exact domains summarized by \(E_j,O_j\), and prove preservation
of all five state coordinates. The current recurrence is correct but the
proof is too compressed for a principal all-size contribution.

**M3 — Internal collision firewall is absent.** P105 is a serious same-carrier,
same-clock, fibres/GOE silhouette collision, and P117/P120 are close reversal
mechanism neighbors. They must be explicitly subtracted in the manuscript,
not only alluded to in planning documents.

**M4 — Core mechanisms have no auditable example.** Add one compact example
that lists a target's admissible cuts, constructs every associated preimage,
checks the fibre DP, and traces the five-bit state on its record indicator.
This is necessary exposition for a four-page note whose novelty resides in
those two constructions.

### MINOR

**m1.** In the inverse proof, “new target segment” should be “reconstructed
source segment.”

**m2.** Replace “the second and third items ... the first ... the second” by
unambiguous references to items (ii) and (iii).

**m3.** State that relative ranks give a bijection to
\([1]\times\cdots\times[n]\), rather than only saying that they “range
independently.”

**m4.** The literature paragraph should distinguish a literal-map owner,
a method neighbor, and a record-statistic neighbor. Those are different
subtractions.

**m5.** Use the available page-4 space for a short conclusion/claim-ceiling
paragraph or the collision table; do not expand generic motivation.

## 10. Required repair set and re-entry gate

Before a round-one internal GO can be considered, all of the following are
required:

1. correct `Huang2026` against the live primary record; update the published
   Bouvel--Cioni--Ferrari citation; pin the exact Foata correspondence to a
   precise primary/standard source; and document the queuesort/record-operator
   neighbor check;
2. insert the complete five-coordinate invariant, \(d_0=1\), accumulator
   ranges, and an explicit induction proving (4.3)--(4.4);
3. insert a compact worked admissible-cut/preimage/DP/bit-state example;
4. add an explicit P105/P117/P120 internal-collision paragraph or table, with
   P105 identified as the closest same-carrier package and the residual claim
   narrowed accordingly;
5. repair the source/target wording, ambiguous item references, and
   relative-rank sentence;
6. rerun the exact verifier and isolated four-stage build, preserve the
   frozen round-0 artifact, and obtain an independent re-entry review;
7. keep all public posting, submission, novelty, and priority actions on
   **HOLD**.

**Final round-0 verdict: MAJOR — STOP/REWRITE.** The theorem package is not
killed: the admissible-cut bijection and weighted five-bit census appear
correct and likely form a viable short paper after the exact repairs above.
There is no authorization for external circulation.
