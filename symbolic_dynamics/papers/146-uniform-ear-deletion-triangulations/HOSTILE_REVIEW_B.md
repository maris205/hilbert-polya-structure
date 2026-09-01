# Hostile review B — round 2

Reviewer role: independent mathematical, ownership, and reproducibility
reviewer; the reviewer did not author this paper.  Reviewed 2026-09-01 UTC.

## Verdict and counts

**ACCEPT** for the internal round-2 gate.  External status remains
`HOLD_EXTERNAL`.

| Severity | Count |
|---|---:|
| Critical | 0 |
| Major | 0 |
| Minor | 2 |

I found no counterexample to the deletion-history probability, endpoint
triangulation construction, root-face bijection, rooted hook denominator,
unrooted leaf-order identity, recurrence, or sharp path equality class.  Every
required round-1 mathematical and artifact repair is present.  The two minor
findings below concern publication-facing source traceability and a stale plan;
neither changes a theorem, proof, verifier, canonical transcript, or PDF.

## Round-1 repair closure

| round-1 interface | round-2 result |
|---|---|
| current versus historical PDF | **PASS.** `main.pdf` is byte-identical to `main_round1.pdf`, while the defective round-0 PDF remains distinct and unchanged. |
| endpoint nonuniformity qualification | **PASS.** The abstract and narrative say that nonuniformity first occurs at $n=6$, consistent with the exact table. |
| connected dual / independent leaf recurrence / brute extensions | **PASS.** All three checks are implemented, exercised, and represented in the regenerated canonical transcript. |
| proof invariants | **PASS.** The triangulation invariant, descendant-closed-prefix invariant, and surviving-vertex partition are stated explicitly. |
| direct hook owner and source identifiers | **PASS.** The Björner--Wachs owner replaces the coarse book citation; full names, both journal DOIs, and Regev's arXiv identifier are correct and visible. |
| closest-owner subtraction | **PASS at packet level.** `SOURCE_VERIFICATION.md` distinguishes the Björner--Wachs forest hook formula and the Coronado--Pons--Riera reduction/linear-extension correspondence from the polygon-specific residual. |
| deterministic clean builds | **PASS.** Two isolated four-stage builds are mutually byte-identical and byte-identical to the distributed current PDF. |

The current PDF has SHA-256
`c84500da478cec5b6b29dd1542b865b711bdd7da83887412574984495c41029d`;
the same hash belongs to `main_round1.pdf`.  The preserved historical PDF has
SHA-256
`60d29efdca38b64fe8721a0e6d20fe9996b3da24f3d2e397628f64fc702595ca`.
Rendered page 2 of that historical artifact still contains the literal
`quad` and comma defects recorded by review A, so it is genuine provenance
rather than a silently replaced snapshot.

## Hostile mathematical reattack

### 1. Equiprobability and endpoint construction — pass

At current size $k\ge4$, convexity makes every current vertex an ear.  Hence
every ordered list of $n-3$ distinct original labels is legal, and its
probability is

\[
 \frac1n\frac1{n-1}\cdots\frac14=\frac{3!}{n!}.
\]

There are $n!/3!$ such lists.  The repaired construction invariant is the
right one: the current polygon together with the previously cut-off ear
triangles triangulates the original polygon.  Therefore the next neighbour
chord lies in the remaining region, is new, and cannot cross an earlier chord.
After $n-3$ steps the process has exactly the $n-3$ distinct diagonals of a
triangulation.  The empty $n=3$ case is covered without an exception.

The qualification “nonuniformity first occurs at $n=6$” is exact: the
endpoint multiplicities are constant at $1,2,4$ for $n=3,4,5$, whereas at
$n=6$ they range from $8$ to $12$.

### 2. Root-face bijection and hook denominator — pass

Fix an endpoint $T$ and final face $r$.  A deleted ear face is a leaf of
the current weak dual, and a nonroot dual leaf has one remaining internal edge
and therefore one current ear tip.  In the converse direction, a
child-before-parent prefix is descendant-closed.  Its complement is the
connected ancestor-closed subtree containing $r$, and its faces triangulate
the current convex polygon.  Thus the scheduled vertex is genuinely a current
dual leaf, not merely a leaf in the original tree.  This proves existence,
uniqueness, and mutual inverseness of the two constructions.

With $m=n-2$ and $q=m-1=n-3$, split the nonroot vertices into root branches
of sizes $q_1,\ldots,q_d$.  Interleaving their internal orders gives the
multinomial coefficient, and recursive cancellation yields

\[
 \binom{q}{q_1,\ldots,q_d}
 \prod_i\frac{q_i!}{\prod_{v\text{ in branch }i}s_v^{(r)}}
 =\frac{q!}{\prod_{v\ne r}s_v^{(r)}}.
\]

The root is correctly excluded.  For $m=1$, the empty product and $0!$
give one history.  Summing the mutually exclusive final-face classes and
multiplying by $6/n!$ proves the complete endpoint law.

### 3. The identity $H(T)=L(D_T)$ — pass

A complete leaf-deletion order has a unique surviving vertex $r$.  Orienting
the tree toward that survivor turns the order into a child-before-parent
linear extension, and every such extension is a legal leaf-deletion order by
the same ancestor-closed-complement argument.  Partitioning by the survivor,
not by a nonexistent final deletion, gives

\[
 L(D_T)=\sum_r H(T,r)=H(T).
\]

Partitioning instead by the first deleted leaf gives the exact recurrence

\[
 L(K_1)=1,
 \qquad L(D)=\sum_{v\in\operatorname{Leaf}(D)}L(D-v).
\]

Deleting a leaf preserves connectedness and acyclicity, so every term is a
tree of size one less.  There is no hidden forest case in the induction.

### 4. Sharp lower bound and equality — pass

Every tree of order $m\ge2$ has at least two leaves.  Induction in the
recurrence therefore gives

\[
 L(D)\ge |\operatorname{Leaf}(D)|2^{m-2}\ge2^{m-1}.
\]

If equality holds, the first inequality chain forces exactly two leaves; a
finite tree with exactly two leaves is a path.  Conversely, either endpoint
of a path can be removed and the remainder is a path, so the recurrence gives
equality at every order.  Substituting $m=n-2$ yields precisely
$H(T)\ge2^{n-3}$, including $m=1,2$.

## Exact-control audit

The documented replay

```text
PYTHONDONTWRITEBYTECODE=1 python3 verify_p146.py
```

compared byte for byte with `verification_output.txt`.  It again ended with

```text
assertions=9562
P146_THEOREM_INTERFACES_PASS
```

The verifier genuinely does what the manuscript now says:

- it enumerates all 68,185 histories for $3\le n\le9$, reaches all 625
  Catalan endpoints, and preserves final-face refinements;
- it checks that every reconstructed weak dual is connected and has the tree
  edge count;
- it compares every marked history count with the rooted hook quotient;
- it computes an independent bitmask leaf-deletion recurrence and compares it
  separately with observed histories and the sum of root hooks;
- it brute-forces child-before-parent permutations whenever the dual has at
  most six vertices; and
- it checks exact rational normalization, the minimum, and equality iff the
  dual is a path.

As extra pressure beyond the frozen packet, a direct $n=10$ run returned

```text
(histories, triangulations, min_H, max_H, path_dual_equalities)
=(604800, 1430, 128, 1504, 320)
```

and passed 21,454 exact assertions.  A second implementation, independent of
`verify_p146.py`, enumerated all 18,249 labelled trees through seven vertices
by Prüfer codes, compared memoized leaf orders with every rooted hook sum,
brute-forced rooted extensions through six vertices, and rechecked the sharp
equality class.  All 315,476 integer assertions passed.  These computations
are falsification pressure, not proof or novelty evidence.

## Ownership and source audit

The four primary records in `SOURCE_VERIFICATION.md` have correct bibliographic
data and appropriately narrow overlap decisions:

- [Eder--Held--Palfrader](https://doi.org/10.1016/j.comgeo.2018.01.004)
  supplies ear-clipping background, not the random endpoint law;
- [Regev](https://arxiv.org/abs/1311.1955) supplies a deterministic labelled
  ear-clipping bijection, not all histories or endpoint masses;
- [Björner--Wachs](https://doi.org/10.1016/0097-3165(89)90028-9) owns the
  rooted-forest linear-extension hook formula, not the polygon/root-face
  identification; and
- [Coronado--Pons--Riera](https://doi.org/10.1007/s11538-024-01374-1) gives a
  reduction-sequence/linear-extension correspondence for phylogenetic
  networks, not polygon ears or the sharp weak-dual minimum.

The paper and packet give zero contribution credit to ear clipping, Catalan
enumeration, weak-dual trees, generic reduction-order/linear-extension ideas,
and the generic hook formula.  The residual is expressly called elementary
and owner-thin.  The bounded search non-hit is expressly denied novelty,
priority, ownership, or release force.  This is the correct internal posture;
`HOLD_EXTERNAL` must remain.

## Reproducibility and three-page inspection

I made two fresh isolated directories containing only current `main.tex` and
`references.bib` and ran

```text
pdflatex -> bibtex -> pdflatex -> pdflatex
```

in each.  Both builds succeeded; both PDFs had the current hash above; and the
two PDFs and distributed `main.pdf` compared byte for byte.  Volatile PDF
dates and trailer identifiers are absent.  The settled log has no unresolved
citation/reference, bad box, or rerun request.  It retains one harmless
pdfTeX font-expansion ordering warning; that warning is reproducible and has
no visual or byte-stability consequence.

All three current pages were rasterized and inspected at high resolution.
Equation (6) displays `\qquad (|V(D)|\ge2)`, the induction line displays
$|\operatorname{Leaf}(D)|\,2^{m-2}$, and neither historical corruption is
present.  The theorem, proofs, exact table, and all three references are
legible, with no overlap or clipping.  Both journal DOIs and `arXiv:1311.1955`
are printed.  The PDF is three A4 pages, unencrypted, has blank identifying
metadata, and all font rows are embedded and subsetted.  No figure is needed
for a theorem whose complete interfaces are the displayed bijection, hook
formula, recurrence, and one exact table.

## Minor findings

### Minor 1 — the Coronado owner is packet-visible but not paper-visible

The closest modern reduction-history/linear-extension analogue is correctly
verified and subtracted in `SOURCE_VERIFICATION.md`, so the round-1 owner gate
is closed at packet level.  However, `references.bib` and `main.tex` contain
only the other three records.  A reader of the PDF sees the generic
zero-priority sentence for reduction-order/linear-extension correspondences
but cannot recover the Coronado--Pons--Riera analogue that supports that
sentence.

**Exact fix:** if the manuscript advances beyond internal hold, add the
verified Coronado--Pons--Riera entry to `references.bib` and cite it at the
scope sentence, explicitly as a different-carrier analogue rather than an
owner of the polygon endpoint law.  No theorem or ownership status changes.

### Minor 2 — `PAPER_PLAN.md` is stale relative to the accepted artifact

The plan promises five sections and “4--6 pages including references.”  The
current paper intentionally has four numbered sections and three pages, and
the task-specific all-page audit confirms that this compact form is complete.

**Exact fix:** change the plan to four sections (noting that theorem and
process share Section 1) and a three-page target, or label the old figures as
pre-draft estimates.  No paper rebuild is required.

## Final disposition

There are **0 critical, 0 major, and 2 minor findings**.  Every round-1
release-blocking defect is closed, the theorem package survives independent
reattack and exact pressure, and the artifact is deterministic and visually
correct.  The paper therefore receives **ACCEPT** at the internal round-2
gate.  This is not novelty, priority, posting, submission, or external-release
clearance; status remains **HOLD_EXTERNAL**.
