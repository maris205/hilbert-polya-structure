# Hostile Review B: Odd-Component Complementation

**Reviewer role:** second independent, nonauthor hostile reviewer. I did not
author this paper, its verifier, or Hostile Review A.

**Audit date:** 2026-08-30 UTC.

**Review target:** the repaired round-1 freeze: `main.tex`, `references.bib`,
`main.pdf`, `main_round1.pdf`, the retained `main_round0_original.pdf`, every
paper-local support document, and the strengthened verifier plus canonical
output. Round 0 was used only to verify the repair delta; it was not the review
target.

## Verdict

**GO_INTERNAL / NOT STOP. External release remains HOLD.**

The two Review-A repairs are substantively closed. I found no false theorem,
invalid converse, omitted mathematical boundary, coefficient error, verifier
miscount, build mismatch, rendered-page defect, or anonymity leak. The
surviving contribution is narrow after classical-owner and internal-collision
subtraction, but the scheduler-specific conjunction is mathematically coherent
for internal use.

Three nonblocking MINOR cleanup findings remain in support/control reporting.
None changes a theorem, proof, equation, PDF, census, or allowed claim ceiling.

## Severity and release summary

| Severity | Count | Consequence |
|---|---:|---|
| CRITICAL | 0 | No false theorem, invalid proof, corrupt artifact, or identity leak found. |
| MAJOR | 0 | No issue requiring STOP, a manuscript rewrite, or a verifier redesign found. |
| MINOR | 3 | Freeze labelling, collision-register completeness, and verifier-reporting precision should be cleaned up. |

| Decision axis | Result |
|---|---|
| GO/STOP | **GO_INTERNAL** |
| External circulation | **HOLD_EXTERNAL** |
| Novelty/priority clearance | **Not granted** |

## Actionable MINOR findings

### B-M1. `README.md` still identifies the package as round 0

`README.md:3` says “Anonymous internal round-0 freeze,” although the current
source, verifier, `main.pdf`, and `main_round1.pdf` are the repaired round-1
freeze. `BUILD.md` and `IMPROVEMENT_LOG.md` correctly describe round 1.

**Action:** change only the freeze label in `README.md` from round 0 to round 1
at the next support-document freeze. This is provenance hygiene, not a
mathematical defect.

### B-M2. The support collision register omits P122

Review A explicitly compared P123 with P122, even record-block reversal, because
both use a parity-selected block update and a sharp transient clock.
`CONTROL_RESULTS.md:26` and `PAPER_PLAN.md:22` list P75, P117, and P118 but omit
P122. The omission does not create a literal collision: P122 acts on
permutations, reparses record blocks, and terminates by lexicographic descent;
it has neither graph complementation nor a component-refinement tree.

**Action:** add P122 to the support collision register and state that generic
“parity-selected blocks plus a sharp transient” language receives no credit.
The residual P123 claim remains unchanged.

### B-M3. Two verifier-reporting details should be made literal

The strengthened verifier is correct for every claimed comparison, but two
presentation details are looser than the code.

1. `CLAIMS_EVIDENCE.md` C3 says that both iff criteria and both literal
   censuses are asserted “state by state.” The iff criteria are statewise; the
   code accumulates literal state counts and compares the two censuses once per
   order at lines 216--218. The census check is exhaustive but aggregate.
2. The canonical line `connected [1, 1, 1, 4, ...]` reports
   `connected[0] = 1`, because line 151 treats `n == 0` as connected for this
   local array. Standard connected-graph species use `c_0=0`. This entry is
   never consumed: `assemblies` starts at component size one, and
   `C_e` starts at size two. All printed and proved coefficients are therefore
   unaffected.

**Action:** say “criteria state by state and censuses by exhaustive aggregate
comparison”; and either report `connected[0]=0`, rename the array to document
the empty-state sentinel, or explicitly state the convention. If the canonical
stdout is changed, refreeze its hash. No theorem or assertion-count change is
needed.

## 1. Review-A repair closure

| Review-A request | Round-1 evidence | Review-B status |
|---|---|---|
| Replace “independent proof routes” by “complementary,” and state the enumerative route uses the proved pointwise recursion. | `NARRATIVE_REPORT.md:7--11` says exactly this and explicitly cites the already-proved depth recursion. | **CLOSED** |
| Correct theorem locations in the claims ledger. | C1--C9 now point to Lemma 1.1, Theorem 2.2, Corollary 2.3, Theorem 3.1, Theorem 4.1, Proposition 4.2, and Corollary 5.1, matching the final auxiliary labels and PDF. | **CLOSED** |
| Either narrow the mechanical-evidence language or strengthen the verifier with literal checks. | The verifier now checks one-step component refinement, literal orbit depth against a separately evaluated split clock, both iff criteria, literal fixed/recurrent censuses, period ceiling, and EGF cumulative layers. | **CLOSED**, subject only to B-M3 wording precision |
| Preserve the original and freeze the repaired PDF. | Round 0 is retained separately; current `main.pdf` and `main_round1.pdf` are byte-identical and differ from round 0 only in the verifier-description paragraph on extracted-text comparison. | **CLOSED** |

No Review-A repair silently weakened a theorem statement or widened the owner
ceiling.

## 2. Definition, theorem, proof, and equation audit

### 2.1 Equation (1) and Lemma 1.1

Equation (1) takes the connected components of the current labelled graph,
complements the induced graph on each odd block, copies each even block, and
forms their labelled disjoint union. Because no cross-component edge is ever
created, the next component partition refines the current one. An even current
component remains the same connected component forever. An odd connected block
is sent to its literal labelled complement; if that complement is connected it
returns in one more step, and if it is disconnected its new components can
never rejoin. The synchrony convention is unambiguous because the original
blocks are disjoint and their toggles commute.

**Result:** equation (1), all three clauses of Lemma 1.1, and its proof pass.

### 2.2 Equation (2), Theorem 2.2, and Corollary 2.3

For a connected odd block \(H\), a genuine split produces strict vertex
subsets. At least one child has odd order because the parent has odd total
order, so the recursive maximum in the split case is nonempty; the stated
empty-maximum convention is needed only for arbitrary graphs with no active
odd component and is harmless elsewhere. Thus equation (2) is well-founded.

After a split, even children have entrance time zero and odd children evolve as
independent components. A disjoint product reaches its recurrent set when the
last factor does, so the clock is

```text
0                                      if complement(H) is connected,
1 + max D(C) over odd complement-components C otherwise.
```

This is exactly equation (2), not merely an upper bound. Induction on vertex
order proves Theorem 2.2. There is no phase-synchronization gap: every recurrent
factor has period one or two, and entrance to the product recurrent set is
still the maximum factor entrance time.

A nontrivial odd component is recurrent precisely when it and its complement
are connected. On the same labelled vertex set a nontrivial graph cannot equal
its edge complement, so such a factor has exact period two. Singletons and all
even components are fixed. Products of period-one and period-two factors have
period at most two. These observations prove every direction of Corollary 2.3,
including the fixed iff and “genuine two-cycle” clauses.

**Result:** equation (2), Theorem 2.2, Corollary 2.3, and their boundary
conventions pass.

### 2.3 Equations (3)--(4) and Theorem 3.1

Along an active edge \(H\to C\), both orders are odd. Since the complement of
\(H\) has at least two components, the vertices outside \(C\) have positive
even total order and therefore number at least two. Each split loses at least
two active vertices, which proves equation (3). For an even ambient order, an
odd component has order at most \(n-1\), so taking the maximum over components
still gives exactly \(\lfloor(n-1)/2\rfloor\).

In equation (4), understood recursively for \(r\geq1\),

```text
H_1 = K_1,
H_{2r+1} = complement(H_{2r-1} disjoint-union K_2).
```

The graph inside the complement is disconnected, hence \(H_{2r+1}\) is
connected. Its complement has precisely the active odd child \(H_{2r-1}\) and
the frozen even child \(K_2\), giving depth \(r\). Adding a singleton preserves
that depth and supplies every even order.

The boundaries are all covered: \(n=0\) is separately zero; \(n=1\) uses
\(H_1\); \(n=2\) uses \(H_1\sqcup K_1\); odd and even \(n\geq3\) use the two
witness families above.

**Result:** equations (3)--(4), the upper bound, sharpness, and all order
boundaries pass.

### 2.4 Equations (5)--(11), Theorem 4.1, and Proposition 4.2

Equation (5) correctly counts unrestricted connected even components and has
neither a constant nor singleton term. For \(n\geq2\), a graph and its
complement cannot both be disconnected: vertices in distinct components of
one are adjacent in the other. Complementation is a label-preserving
involution, so inclusion--exclusion gives
\(q_n=2c_n-2^{\binom n2}\). Equation (6) correctly restricts this identity to
odd \(n\geq3\) and supplies the necessary convention \(q_1=1\).

Equation (7) is exact because a connected odd graph has depth zero exactly when
it is co-connected. For equation (8), complementation bijects a positive-depth
connected odd graph of depth at most \(t\) with a disconnected labelled SET of
unrestricted connected even components and connected odd components of depth
at most \(t-1\). The exponential formula counts that SET;
\(1+C_e+O_{t-1}\) removes the empty and every one-component SET; odd extraction
imposes odd total order; and the \(Q\) base class is disjoint because its
complement is connected. No symmetry factor is missing in labelled SET
calculus.

Equation (9) assembles arbitrary graphs from even connected components and the
allowed odd connected components. These cumulative classes are nested, so
equation (10) gives every exact positive-depth layer and \(F_0\) gives the
recurrent layer. Finally, the fixed-component classification permits exactly
singletons and arbitrary connected even graphs, proving equation (11) and
Proposition 4.2.

All statements are formal-power-series identities; no convergence assumption
is hidden.

**Result:** equations (5)--(11), Theorem 4.1, Proposition 4.2, all \(t=0\),
\(t\geq1\), \(n=0\), and \(q_1\) boundaries pass.

### 2.5 Equation (12) and Corollary 5.1

The recurrent set contains \(f_n\) fixed states and \(r_n-f_n\) states paired
into genuine two-cycles. A transient point cannot be fixed by a positive
iterate, because any such equality would put it on a cycle. Therefore odd
iterates fix exactly the one-cycles and even iterates fix the full recurrent
set. Splitting the Artin--Mazur series into one- and two-cycle factors gives

```text
(1-z)^(-f_n) (1-z^2)^(-(r_n-f_n)/2),
```

exactly as in equation (12).

**Result:** the two-cycle count, fixed-iterate count, equation (12), and
Corollary 5.1 pass, including \(n=0\).

## 3. Independent computational stress checks

In addition to reading the paper-local program, I ran review-side checks that
did not modify or import it.

- A separate set-of-edges implementation sampled 1,000 deterministic random
  labelled graphs at each of orders 7, 8, 9, and 10. It made 20,000 checks of
  literal orbit depth versus recursively computed split depth, recurrent iff,
  fixed iff, period ceiling, and global depth ceiling. Result: **PASS**.
- The sharp witnesses were built directly through odd order 13, with singleton
  extensions through even order 14. Their literal orbit depths were
  \(0,1,2,3,4,5,6\), exactly as claimed. Result: **PASS**.
- I independently generated connected labelled-graph counts and evaluated the
  labelled recurrence through order 12. Every depth layer summed to
  \(2^{\binom n2}\), and stabilization first occurred at
  \(\lfloor(n-1)/2\rfloor\). The recurrent counts for \(n=7,\ldots,12\) were
  `1,845,984`, `266,301,568`, `66,266,955,904`,
  `35,158,965,365,120`, `35,641,205,953,446,784`, and
  `73,782,267,413,628,108,288`, agreeing with Review A. Result: **PASS**.

These checks are corroboration only; the all-order conclusions rest on the
proofs audited above.

## 4. Strengthened verifier and canonical-byte audit

Fresh command, with stdout redirected outside the paper directory:

```text
python3 code/verify_odd_component_complementation.py
```

Result: **PASS**, `assertions=203244`.

The assertion count is not a decorative print; it reconstructs exactly:

| Assertion source | Count |
|---|---:|
| 33,868 labelled graphs through order six times six statewise checks (refinement, split clock, recurrent iff, fixed iff, period, depth ceiling) | 203,208 |
| Odd co-connected identities at orders 3 and 5 | 2 |
| Exhaustive cumulative-depth coefficient comparisons | 13 |
| Fixed-subset, literal-fixed-census, and literal-recurrent-census comparisons at seven orders | 21 |
| **Total** | **203,244** |

Code inspection confirms that:

- `step` computes the components once and toggles precisely the induced edges
  of each original odd component, so it is the literal synchronous map;
- `connected_odd_split_depth` follows complement-components recursively and is
  separate from functional-orbit detection;
- refinement and both iff criteria are checked for every state;
- literal fixed and recurrent counts are accumulated from map/orbit behavior,
  then compared with the formula assemblies;
- all \(2^{\binom n2}\) labelled states are exhausted for \(0\leq n\leq6\);
  and
- the EGF lane assembles labelled components independently of orbit traversal.

Fresh stdout was byte-for-byte identical to
`code/verify_odd_component_complementation.out`. The hashes were:

```text
verifier source  952f277e2f6955d51365e670888a1b706af82aedf064cb0c2a57f9063c64890c
canonical stdout 735c28b8c8b48c3308741840f1a6f92868a59076f276131ad59a3bfcccdb5c7e
fresh stdout     735c28b8c8b48c3308741840f1a6f92868a59076f276131ad59a3bfcccdb5c7e
```

The printed depth histograms and literal fixed/recurrent counts reproduce every
entry of the manuscript census. Subject only to B-M3's reporting cleanup, the
Review-A verifier strengthening is genuine and complete.

## 5. Isolated four-stage LaTeX build

I copied only `main.tex` and `references.bib` to a new temporary directory and
ran:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Stage statuses: **0 / 0 / 0 / 0**.

- Fresh PDF: 4 pages, A4, 281,582 bytes.
- Fresh SHA-256:
  `6c78410d7689a7e5f057413ef5256a26885a86a2b9653e3b2581ede30b46c9c1`.
- Fresh PDF, packaged `main.pdf`, and `main_round1.pdf` are byte-identical.
- Retained round-0 SHA-256 is
  `e7a5138e142ef89402668e4eca4e86ea804672b080bfdcce3fe33f7fa074f68d`,
  so the original is distinct and preserved.
- The final log has zero LaTeX/package/class warnings, undefined
  references/citations, overfull or underfull boxes, missing characters,
  rerun requests, or errors.
- BibTeX reports zero warnings and renders all eight cited entries.
- The source and bibliography hashes match `BUILD.md` exactly.

The first pass produced only the expected unresolved-reference diagnostics of a
clean auxiliary directory. BibTeX and the two resolving passes discharged all
of them.

## 6. Every-page visual audit

I rasterized the byte-frozen round-1 PDF at 180 dpi and inspected all four
pages, not just extracted text.

| Page | Material checked | Result |
|---:|---|---|
| 1 | Anonymous title block, abstract, equation (1), Lemma 1.1, Section 2 opening, Definition 2.1, equation (2), classification footer | Clean; no clipping, collision, malformed overline, or unreadable text. |
| 2 | Theorem 2.2, Corollary 2.3, Theorem 3.1, equations (3)--(10), Section 4 transition | Clean; displays, floors, complement bars, subscripts, and hyperlinks render correctly. |
| 3 | Completion of Theorem 4.1, Proposition 4.2, equations (11)--(12), census table, verifier paragraph, conclusion | Clean; table columns and large zeta display are legible and nonoverlapping. |
| 4 | Complete eight-entry bibliography with DOI text | Clean; no truncation, overlap, orphan, or blank-page defect. |

There are no malformed equations, clipped glyphs, float collisions, orphaned
headings, footer collisions, or unexplained blank pages. The page break after
equation (10) preserves a grammatical and visually clear continuation.

## 7. Fonts, metadata, structure, and anonymity

`pdffonts` lists 20 font resources. Every row reports `emb=yes`, `sub=yes`, and
`uni=yes`; therefore all fonts are embedded, subsetted, and carry Unicode maps.

`pdfinfo`, raw-object strings, `pdfdetach`, `pdfsig`, text extraction, and page
rendering give:

- title, subject, keywords, and author metadata fields blank;
- no creation or modification dates and no trailer identifier;
- only generic `Creator: LaTeX with hyperref` and
  `Producer: pdfTeX-1.40.22` fields;
- no metadata stream, user properties, forms, JavaScript, encryption,
  embedded files, or signatures;
- four unrotated A4 pages, PDF 1.5; and
- no `??`, `[?]`, `[VERIFY]`, TODO, FIXME, filesystem path, email, ORCID,
  affiliation, institution, or personal-author marker in the paper artifacts.

The visible byline and running heads say only “ANONYMOUS.” Personal names in
the bibliography are citations, not identity leakage. The anonymity audit
passes.

## 8. Owner subtraction and external non-clearance

The paper correctly gives zero contribution credit to:

- Gallai component/co-component and modular-decomposition structure;
- cographs, union/join recursion, cotrees, and recognition;
- modern labelled cograph/cotree enumeration;
- labelled SET and odd-part operators;
- classical connected labelled-graph enumeration and the elementary
  co-connected count; and
- generic one-cycle/two-cycle/Artin--Mazur bookkeeping.

The primary owner anchors are appropriate: [Gallai
1967](https://doi.org/10.1007/BF02020961), [Corneil--Lerchs--Stewart
Burlingham 1981](https://doi.org/10.1016/0166-218X(81)90013-5), and
[Corneil--Perl--Stewart 1985](https://doi.org/10.1137/0214065). The manuscript
calls its object a “parity-pruned component/co-component split tree,” expressly
denies that it is a new cotree or modular decomposition, and uses the classical
machinery only as an interface.

I repeated bounded exact-phrase and concept searches for odd-component
complementation, complementing each odd connected component, iterative
component/co-component dynamics, and parity-scheduled graph complementation.
They returned adjacent cograph, local-complementation, parity-component, and
cograph-editing/community-detection literature, but no primary source defining
this literal scheduler or its full clock-and-census package. One superficially
close hit, [Jia et al. 2015](https://doi.org/10.1088/1367-2630/17/1/013044),
deletes high-\(P_4\)-centrality edges until a cograph is obtained; it is not this
self-map.

This remains only a bounded non-hit. The proof package becomes short once the
classical decomposition is recognized, so direct-owner risk remains
**medium-high**. Nothing in this review converts the non-hit into novelty,
priority, or external-release evidence.

## 9. Internal P1--P122 collision ceiling

| Internal item | Shared silhouette | Why it does not own the P123 residual |
|---|---|---|
| P75, RACG geodesic join components | Complement components organize recurrent automaton pieces; zeta language. | It has no graph self-map, parity scheduler, refinement clock, or labelled graph-depth census. |
| P117, odd-run reversal | Synchronous parity-selected blocks, periods at most two, sharp transients, finite zeta. | The carrier is a cyclic binary word; its run-boundary erosion and extremal proof are unrelated to graph component/co-component splitting. |
| P118, synchronous multipartite mex | Pointwise depths, every depth layer, recurrent census, and zeta. | Its mechanism is a mex quotient/lift on graph colourings, not graph complementation or component refinement. |
| P122, even record-block reversal | Parity-selected blocks and a sharp transient clock. | The carrier is a permutation; blocks are reparsed and descend lexicographically. There is no graph split tree or period-two complement atom. |

A repository-wide term audit found no second literal odd-component
complementation map. Generic parity scheduling, block independence, finite
depth, labelled EGF assembly, and zeta packaging are already-spent motifs and
must continue to receive zero credit. B-M2 concerns only keeping this ceiling
explicit in the support register.

## 10. Allowed claim ceiling

The following survive for internal mathematical use:

- the literal odd-component complementation self-map on labelled simple
  graphs;
- its exact scheduler-specific split-tree entrance clock;
- the recurrent/fixed classification and period-one/two ceiling;
- the sharp all-order maximum depth with witnesses at every order; and
- the scheduler-specific all-depth labelled EGF and its recurrent, fixed,
  two-cycle, and zeta consequences.

The following remain zero-credit or forbidden:

- a new cotree, modular decomposition, complement operation, or general
  cograph theorem;
- a new connected-graph or cograph enumeration method;
- logical independence of the enumerative proof from equation (2);
- proof of any all-order statement by the order-six verifier;
- contribution credit for generic parity-block, EGF, or zeta motifs;
- novelty or priority inferred from exact-string or bounded-search non-hits;
  and
- external posting, circulation, submission, or release before a broader
  direct-owner audit.

## Final recommendation

**GO_INTERNAL / HOLD_EXTERNAL.**

The repaired round-1 theorem package, strengthened verifier, canonical output,
isolated build, frozen PDF, rendered pages, fonts, metadata, and anonymity all
pass hostile reconstruction. Resolve B-M1--B-M3 in a later support-only freeze,
retain the classical and internal subtraction ceiling, and do not treat this
review as novelty, priority, or release clearance.
