# Independent Manuscript Review — Round 2

Review date: 2026-08-14 UTC  
Candidate: `cat_torsion_primitive_divisor_capacity_v1`  
Manuscript: *A Primitive-Divisor Audit of Prime-Order Torsion Periods for Hyperbolic Toral Automorphisms*  
Reviewer role: fresh independent revision verifier, mathematical reviewer, reproducibility auditor, and devil's advocate  
Decision: **PASS — MAY FINALIZE**  
Overall score: **92/100 (9.2/10)**  
Confidence: **5/5** for revision closure, internal mathematics, build, and artifact integrity; **4/5** for literature completeness because this round was intentionally offline

## Executive decision

All three bounded Round-1 findings are **FULLY ADDRESSED**.  The revised
source and PDF contain the requested sign-independent instability notation,
the two ordinary-period references are correctly delimited from the
prime-additive-order theorem, and the citation ledger now has an explicit,
hash-bound terminal state.  I found no mathematical, evidentiary,
bibliographic, typographic, or scope regression.

The uniform carrier theorem, its three negative-trace parity branches, the
primitive-kernel exact-period bridge, the sharp standard-cat exception set,
the modulo-five Jordan repair, and the torsion-order obstruction all pass a
fresh line-by-line review.  The one-shot result chain and the complete figure
package also remain closed.  There are **zero new Critical, Major, or Minor
findings**.

The manuscript may proceed to finalization without another scientific
revision round.  Finalization is limited to mechanical lifecycle changes:
replace the pre-review/awaiting-review wording, create and bind the final PDF,
and update the package state and hashes.  Any change to a theorem, proof,
citation role, figure, source lock, code, or result would reopen this gate.

## Verification order and immutable bindings

I fixed the acceptance criteria from the Round-1 report before inspecting
the revised manuscript and before reading the author's response.  I then
verified the revised source, PDF, bibliography, and citation ledger directly;
only afterward did I compare those observations with the response letter.
No author assertion was accepted without matching manuscript-side or
artifact-side evidence.

The four required dispatch bindings reproduce exactly:

| Object | SHA-256 | Verdict |
|---|---|---|
| Round-1 review | `bb64f75c96ca0b3d2e78a3b295a1d1b8321ea2143f4612e08b316594991e5ac5` | MATCH |
| Round-1 response | `85b618e7a0cbd28ac4bed4cea93e3cdc7a0593a1ba7357fc9f1944650c0950eb` | MATCH |
| revised `paper/manuscript.tex` | `95ebccff1eb5f2b939be92c9a8b7020b625d4b8056cc5b6bda3b3814fcae580c` | MATCH |
| revised `paper/manuscript.pdf` | `5ff37aca10905bd7fd84f25a81e47601ed9883259519b02e2809f77485770d98` | MATCH |

Additional revision bindings also reproduce:

| Object | SHA-256 |
|---|---|
| bibliography | `0fd74e7688739c8a3eb44ea995f950250c0a9afcfc99699824bd57e753e21ba9` |
| citation-verification ledger | `4d79e865326ae7209184f42a3a204e73b189d3a3f2d9ab71c25924ea72003805` |
| paper plan | `6d87e00c8cf5b21c021dfe38b572ec16d5551f576615fced4abdc72f6f70a885` |
| Round-1 revision integrity record | `2962317aa5028baf15478c105f86ac96adae5b6a9d3c381935cccc09b700f6d3` |
| immutable pre-review PDF | `9b7594015e3e6eb3db759ea1eea27a2249c513368ce9c063382be76e041357f8` |

This review was read-only apart from this report.  I did not run the
candidate or test suite, compute a new period, access a network service,
load an external prime table, inspect Riemann-zero data, or modify any
manuscript, bibliography, source-lock, code, result, or figure artifact.

## Round-1 revision traceability

| Item | Precommitted acceptance criterion | Independent evidence | Status |
|---|---|---|---|
| M1 | Every general negative-trace/native-instability statement uses the logarithm of the unstable multiplier's modulus, $n\log\rho(A)$, with no stale general $n\log\alpha$ claim. | `manuscript.tex:557--564` defines $\rho(A)$ as the spectral radius and uses $n\log\rho(A)$ in both the proof and comparison paragraph. `PAPER_PLAN.md:255--256` and Claim C6 in `CLAIM_MANIFEST.json` agree. | **FULLY ADDRESSED** |
| M2 | Add a bounded ordinary-period-set bridge using locally verified Kannan (2011) and Seibt (2003) metadata, and prevent either citation from supporting the prime-order carrier theorem. | `manuscript.tex:87--92` assigns Kannan only the ordinary hyperbolic two-torus period-set baseline and Seibt only rational-lattice period-formula context, then explicitly states that neither imposes prime additive order. Bibliography metadata and allowed roles match the local novelty and citation locks. | **FULLY ADDRESSED** |
| M3 | Reconcile the stale citation-ledger release item, state any verification not repeated, compile the expanded bibliography, and bind every affected hash. | `CITATION_VERIFICATION.md` records `ROUND-1 BOUNDED CITATION CLOSURE`, retains the 2026-08-14 cutoff, explicitly says URL re-resolution was not repeated, closes every checklist item, and records the revised bibliography hash. `INTEGRITY_ROUND1_REVISION.md` binds the revised source, plan, ledger, bibliography, response, configuration, claim, passport, figure, PDF, and pipeline artifacts. | **FULLY ADDRESSED** |

### M1 scope note: historical alpha labels are not a live overclaim

A repository-wide static scan does find `n log alpha` in immutable
source-lock, proof, code, and raw-result artifacts.  Those records belong to
the frozen standard trace-three cat map, where
\(\alpha=(3+\sqrt5)/2=\rho(A)>0\), or are historical schema labels from the
registered run.  They were correctly left unchanged.  The revised general
manuscript, current plan, caption/claim surfaces, and Claim C6 all use
\(n\log\rho(A)\).  Thus no stale signed-eigenvalue assertion remains on the
general negative-trace claim surface.

### M2 metadata and 14-of-14 closure

The two new entries reproduce the locally locked metadata and claim roles:

- V. Kannan, I. Subramania Pillai, K. Ali Akbar, and B. Sankararao,
  “The Set of Periods of Periodic Points of a Toral Automorphism,”
  *Topology Proceedings* **37**, 219--232 (2011), used only for the ordinary
  period-set baseline.
- Peter Seibt, “A Period Formula for Torus Automorphisms,” *Discrete and
  Continuous Dynamical Systems* **9**(4), 1029--1048 (2003), DOI
  `10.3934/dcds.2003.9.1029`, used only for rational-lattice/global period
  formula context.

The clean-build auxiliary file has 14 distinct cited keys.  The BibTeX file
has exactly the same 14 keys, the generated bibliography has 14 `bibitem`
records, and there are no missing or unused keys.  The terminal BibTeX log
reports `warning$ -- 0`.  This closes the requested bibliography expansion
without claiming that an offline Round-2 review performed a new live URL
resolution.

## Core mathematics and nonclaim regression

| Claim surface | Verdict | Independent check |
|---|---|---|
| Primitive divisor \(\Rightarrow\) exact prime-order carrier | PASS | Singularity gives a nonzero mod-\(p\) kernel; any smaller return would make \(p\) divide an earlier determinant.  The \((p^r-1)/n\) cycle count is taken only after exact period is proved. |
| Positive-trace uniform theorem | PASS | The determinant is the norm of \(\alpha^n-1\) for a positive norm-one quadratic unit, and Flatters is used only under those hypotheses. |
| Negative-trace uniform theorem | PASS | Odd \(n\) uses primitive index \(2n\); \(4\mid n\) uses index \(n\); \(n=2k\), \(k\) odd, uses index \(k=n/2\).  The half-index proof covers \(k=7,9,11\) and independently excludes \(p=2\).  The false all-even index-\(n\) shortcut remains explicitly rejected. |
| Standard-cat iff classification | PASS | The ledger, primitive cases, and complete support-prime profiles exclude exactly \(1,6,12\).  The proof never infers carrier absence merely from failure of primitive divisibility. |
| Modulo-five period-ten repair | PASS | With \(A=-I+N\), \(N^2=0\), rank \(N=1\), four nonzero kernel vectors have period two and the twenty nonkernel vectors have exact period ten, hence two ten-cycles. |
| Periodic points, torsion, and clock regularity | PASS | Both inclusions \(\operatorname{Per}=\operatorname{Tor}\), order invariance, all-order realization, the coprime-perturbation exact-order calculation, and relative local unboundedness are valid. |
| Orbit sum versus native instability | PASS | The sum is \(n\log p\), repeats give \(rn\log p\), and the absolute unstable log multiplier is \(n\log\rho(A)\), independent of carrier order. |
| Scope and novelty firewall | PASS | The paper uses low-novelty verbs, attributes the imported theorem, and claims no prime-orbit bijection, Euler product, transfer/Fredholm determinant, trace formula, quantization, canonical selector, or prime/zero matching. Route A stops at A0 and Route B remains unopened. |

Text extraction and comparison of the immutable pre-review PDF with the
revised PDF found exactly the expected substantive changes: the bounded
Kannan--Seibt paragraph and the two spectral-radius sentences.  The other
differences are bibliography insertion, numeric citation renumbering, and
page/equation reflow.  No theorem statement, proof branch, determinant,
finite-field profile, figure caption, result hash, classification, or
nonclaim was altered.

## Frozen source, result, and figure integrity

The scientific evidence package remains byte-closed:

- source lock:
  `87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce`;
- proof package:
  `ee02fe72071c0bbea26f5f34c28130374fe1a919195cfbe154f6f5a39ab420af`;
- immutable execution tree recorded by the one-shot chain:
  `b4441fb68ac42ab1649ee62037fb7cdf741aa9c09a0b0d5cffc4003697caa059`;
- live non-candidate analyzer tree, independently recomputed:
  `1aadef8597a641f2fd4e29ec63202942291a22d2552fa966bdb79d771f860f34`;
- raw registered result:
  `0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0`;
- final result manifest:
  `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f`;
- figure manifest:
  `e292df2cd1d9d2c19675bc36cf30ed75e88e730fca17c7cd47420285be07fb2c`.

The read-only V2 existing-manifest validator returned stage
`R100_FINAL_POSTRUN_MANIFEST_CLOSURE`, `pass=true`, `errors=[]`, and the exact
11-file final `results/` inventory.  The execution evidence remains 21/21
tests at
`2a0844152eea6d9184d374a6e33c3c4be72fce8deb60296c77650027104348cc`,
and the post-run analyzer evidence remains 27/27 at
`fac25a2d332d68f6a2374b14f57d0f9dcacd5ea27c2c7581766b8c84d00499a0`.
The manifest still records one registered exact audit, zero candidate
numerical runs, no rerun, and an empty list of computed periods above twelve.

All eight figure-generator/scaffold hashes and all nine PDF/SVG/PNG output
hashes reproduce the figure manifest.  The three PDF masters retain their
bound hashes:

| Figure | SHA-256 |
|---|---|
| carrier bridge | `b6c0b975bc45e94da0c3e012498a507df9378239726adb2f654f6bb0225dc4ed` |
| standard-cat boundary | `9983862ebabd20ba783441fd121925950ffffc14a9f0c397b5c1ff379d2e1789` |
| capacity versus specificity | `b5205fbf59daf6f693318c8820419b79f2e5edc4824a0269f73d6675e0548f2f` |

No source, code, result, or figure file changed during this review, and no
Python bytecode/cache artifact was created in those trees.

## Independent build, typography, and visual QA

I created two separate clean temporary paper trees containing only the
bound manuscript source, macro file, bibliography, and three frozen PDF
figures.  Each tree was built from scratch with `pdflatex`, `bibtex`, and two
terminal `pdflatex` passes under the frozen source-date environment.  Both
builds produced

`5ff37aca10905bd7fd84f25a81e47601ed9883259519b02e2809f77485770d98`,

byte-identical to each other, to `paper/manuscript.pdf`, and to
`paper/paper_round1_revision.pdf`.

The terminal build state has 12 letter-size pages, 33/33 fonts embedded and
subset, zero raster image objects, 14 bibliography items, no unresolved
citation or cross-reference, and no LaTeX, package, overfull, underfull, or
BibTeX warning.  As expected for a clean multipass build, early passes emit
transient undefined-reference messages; none remains in the terminal log or
final pass.

All 12 rendered pages were inspected.  The new first-page literature
paragraph, the corrected page-7 instability notation, all equations,
theorem endings, tables, hashes, bibliography entries, and all three figures
are legible, uncropped, and free of collision or corrupt glyphs.  The figures
retain their intended semantics: imported theorem versus derived parity
conversion versus finite audit; primitive-divisor cases versus the Jordan
repair and exclusions; and all-order capacity versus prime specificity and
native monodromy.

## Findings and residual advisories

### Critical findings

None.

### Major findings

None.

### Minor findings

None.

### Nonblocking residual advisories

1. This Round-2 review intentionally performed no live network lookup.  The
   two added references are verified against the locally frozen primary
   metadata and claim-role records at the retained 2026-08-14 cutoff.  The
   ledger accurately discloses that URL re-resolution was not repeated.
2. The current source still says “Pre-review manuscript” and “awaiting a
   fresh independent manuscript review,” and `paper_final.pdf` is absent.
   Those are correct pre-decision lifecycle markers, not scientific defects;
   the finalizer should now update them mechanically and refresh downstream
   hashes.
3. The verification used a fresh independent agent and evidence-first
   procedure but not an external model family.  Hash, compilation, and
   exact-mathematics checks are independently reproducible; qualitative
   literature-completeness judgment may retain same-family correlation.

## Dimension scores

These uncalibrated scores are ordinal quality judgments, not venue
acceptance probabilities.

| Dimension | Score | Review note |
|---|---:|---|
| Originality | 72 | Deliberately scoped, useful synthesis and parity repair; low novelty is disclosed rather than inflated. |
| Methodological rigor | 97 | Complete proofs, edge-case handling, theorem/computation firewall, and immutable one-shot audit. |
| Evidence sufficiency | 96 | Claims, frozen exact artifacts, independent closures, and deterministic rebuild all align. |
| Argument coherence | 96 | The arithmetic bridge, sharp boundary, and specificity obstruction form a clean logical sequence. |
| Writing quality | 96 | Precise, restrained, warning-free, and visually polished after M1. |
| Literature integration | 88 | The direct ordinary-period bridge now closes the only identified positioning gap. |
| Significance and impact | 79 | A strong technical and obstruction note, not a broad new theory. |
| **Overall** | **92/100 (9.2/10)** | **PASS — MAY FINALIZE** |

## Final verdict

**PASS — MAY FINALIZE.**  The three Round-1 items are fully closed, no
regression or blocker remains, and no further manuscript-revision round is
required.  Finalization may make only the bounded lifecycle and hash updates
listed above.  It must not rerun the candidate, extend the period range,
alter frozen evidence, access prime/zero targets, or open a new Route-A or
Route-B claim.
