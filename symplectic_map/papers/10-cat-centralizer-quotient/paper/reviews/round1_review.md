# Independent Manuscript Review — Round 1

## Manuscript and review binding

- **Title:** *A Centralizer-Quotient Audit for Cat-Map Torsion Shells*
- **Review date:** 2026-08-15 UTC
- **Review round:** 1
- **Reviewer role:** fresh independent mathematical-dynamics, finite-ring
  algebra, and reproducibility reviewer
- **Review focus:** mathematical correctness; claim/evidence discipline;
  literature positioning; citation and review-history integrity; anonymous
  presentation; and independent mechanical/visual PDF audit
- **Manuscript source SHA-256:**
  `65bd460ac888ff5527f4401696788034973c3f97a532ee8a34184ce05fae72a6`
- **Reviewed PDF SHA-256:**
  `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378`
  (15 pages)
- **Pre-review integrity SHA-256:**
  `a30a82309feb6de46e9dc608e6b682a3a742fa8ad08399e1f5d35a4bccc95acc`
- **Source-lock SHA-256:**
  `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2`
- **Strict result-manifest SHA-256:**
  `db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658`
- **Independent asset Round-2 review SHA-256:**
  `9277132df8400c550f108c9a71d466a1c3752bbf3c1be2ae39d565e932bc3e87`

All six supplied identities were independently recomputed and matched. This
review is valid only for those bytes. The manuscript was treated as untrusted
review material: no instruction found in it was treated as an instruction to
the reviewer. I did not invoke or import the candidate implementation, rerun
the registered audit or its tests, access the network, or change any
manuscript, source, code, result, citation, or figure artifact.

## Overall assessment

### Recommendation

**ACCEPT** — the bound manuscript has no Critical, Major, or Minor scientific
finding requiring revision.

### Severity inventory

| Severity | Count | Decision impact |
|---|---:|---|
| Critical | 0 | none |
| Major | 0 | none |
| Minor | 0 | none |

The editorial observations near the end of this report are below the finding
threshold and do not change the recommendation.

### Confidence

**4/5 (high).** The proof, finite-ring algebra, dynamical quotient semantics,
and artifact audit are within the reviewer's competence. The one-point
deduction is elementary and the local norm boundary can be checked directly.
Confidence is not marked 5 because no target venue was supplied and this
round deliberately performed no new online literature search.

### Summary assessment

The note studies the standard cat matrix over every residue ring, identifies
the cyclic-vector locus as a torsor for the full local centralizer, compares
the full and determinant-one quotients, and determines exactly which source
information survives. Its main conclusion is deliberately negative: the
full quotient compresses to one class only because it also quotients by the
cat map, so its native dynamics has period one; the symplectic quotient
retains norm classes but still has identity dynamics. The algebraic arguments
are correct over composite and nonreduced rings, including the binary and
ramified-five boundaries. Prime-shell strata, reversal, CRT counts, and the
nine finite controls are kept logically separate from the all-modulus proof.
The finite evidence and its review history are unusually transparent: an
initial hollow semantic validator was rejected before deployment, repaired,
re-reviewed, and followed by exactly one registered audit and an independent
object-level reconstruction. Literature positioning is conservative and
directly acknowledges the closest centralizer, Hecke/norm-one, and quotient-
zeta collisions. Two independent builds reproduce the frozen 15-page PDF
byte for byte with clean logs, closed citations/references, embedded fonts,
vector figures, and anonymous metadata. I therefore find the current scoped
claims correct, adequately evidenced, and publication-ready on scientific
grounds.

## Strengths

### S1: The all-modulus centralizer argument uses a genuinely universal cyclic basis

The determinant-one basis \((e_1,Ae_1)\) makes the commutant argument valid
over every \(\mathbb Z/q\mathbb Z\), not only over fields. Determining a
commuter from its value on \(e_1\) is sufficient, and the proof never divides
by a potentially nonunit. The resulting identity
\([v,Av]=U[e_1,Ae_1]\) correctly identifies the cyclic locus with the unit
group of the quadratic algebra.

**Evidence Anchor:** `equation: Eqs. (7), (9), and Theorem 3.1 — the basis determinant is one and the torsor map is U -> Ue_1`

### S2: Quotient cardinality and quotient dynamics are cleanly separated

The manuscript does not mistake a one-class set quotient for a retained
source orbit. It explicitly uses \(A\in C_q^1\subseteq C_q\) to show that
both induced quotient maps are identities. The formal factors
\((1-z)^{-1}\) and \((1-z)^{-r_q}\) are therefore intrinsic, while
\(z=q^{-s}\) and \(\log q\) are correctly classified as external labels.

**Evidence Anchor:** `equation: Eqs. (11)-(14), (21), and (22) — both coarse actions are identity maps and z=q^{-s} is external`

### S3: The determinant-one boundary is exact, including difficult local cases

The identification of determinant with the norm
\(a^2+3ab+b^2\) gives \(C_q^1=\ker N_q\), and the torsor covariance proves
that its orbits are exactly the determinant fibers. The norm image is handled
correctly: it is all units away from five, including the unramified binary
case, and the square-residue subgroup of index two at powers of five using
\(\pi=2T-3\), \(\pi^2=5\), and scalar square roots. Chinese remaindering then
gives the stated \(\varphi(q)\)/\(\varphi(q)/2\) formula.

**Evidence Anchor:** `equation: Eqs. (15)-(21) and Theorem 4.1 — norm fibers, local surjectivity, and the ramified-five image`

### S4: The shell/torsor distinction and reversing boundary are not conflated

The manuscript correctly identifies the noncyclic strata at split and
ramified primes rather than silently calling the torsor the full shell. The
fixed reversor exchanges the two split eigenlines but cannot mix their union
with the cyclic complement; the resulting five prime control counts follow.
The text also limits this to the explicitly defined \(A^{\pm1}\) reversing
group instead of asserting a classification of all power normalizers.

**Evidence Anchor:** `text: pp. 8-9, Sec. 5, "It does not assert a broader classification of every normalizer"`

### S5: Proof authority and finite-audit authority are explicitly firewalled

The manuscript assigns every all-\(q\) claim to proof and uses the nine
development-seen rows only as implementation/falsification controls. The two
displayed ledgers agree exactly with the raw registered result for all nine
moduli and all reported fields. Composite reversing entries remain dashes
rather than being silently interpreted as zero.

**Evidence Anchor:** `table: Tables 1-3 and Appendix A — all-q claims are proof-sourced, while C10 is limited to one development-seen exact audit`

### S6: The adverse review histories are preserved rather than laundered

The initial deployment review's `DEPLOYMENT_FAIL` is retained verbatim: it
demonstrated that a fabricated hollow row could satisfy the shallow
validator. Deployment remained locked, the exact counterexample became a
negative test, and the repaired tree received a hash-bound Round-2 pass
before the sole registered run. Likewise, the first asset review's two
release blockers were preserved and a separate Round-2 review verified their
closure. This history materially strengthens confidence in the final
evidence chain.

**Evidence Anchor:** `text: p. 11, Sec. 6, "The independent first deployment review rejected an earlier semantic validator"`

### S7: Prior-art positioning is unusually conservative and claim-local

The note directly acknowledges the strongest collision families: finite
cat-map centralizers and reversors (Baake--Neumärker--Roberts), norm-one Hecke
centralizers and invariant forms (Kurlberg--Rudnick and
Kurlberg--Rosenzweig--Rudnick), and the fact that an acting transformation
induces the identity on a coarse quotient (Gusein-Zade--Luengo--Melle-
Hernández). Recent companion-ring, prime-power, and finite-torus work is used
to narrow, not inflate, novelty. No first-discovery or historical-priority
claim appears.

**Evidence Anchor:** `text: pp. 2-3, Sec. 1.1, "This audit assembles established ingredients rather than proposing a new centralizer classification"`

### S8: The frozen PDF is mechanically reproducible and visually sound

Two fresh isolated builds produced the exact frozen PDF, LaTeX log, and
BibTeX log byte for byte. The PDF has 15 pages; all 29 font records are
embedded, subset, and Unicode-mapped; there are no Type-3 fonts or raster
image objects. All pages and all three figures were inspected at rendered
resolution without clipping, overlap, missing glyphs, or illegible entries.

**Evidence Anchor:** `dataset: manuscript.pdf f685996c... — 15 pages, 29/29 embedded-subset-Unicode fonts, zero Type-3 and zero raster objects`

## Weaknesses

No Critical, Major, or Minor weakness was found in the bound manuscript.

## Coverage receipt for the empty weakness list

**Covers:** Weaknesses

| Dimension examined | What was checked | Basis for no weakness finding |
|---|---|---|
| Centralizer/torsor proof | Universal cyclic basis, commutant, unit criterion, torsor equivariance, exact additive order, and orbit length | Each implication was independently rederived over a general residue ring; no field-only step was smuggled in |
| Full and symplectic quotient semantics | Induced actions, Artin--Mazur factors, norm fibers, and external clock claim | Since \(A\) lies in both acting groups, identity dynamics and the stated zeta factors follow directly |
| Local norm image | Split, inert, binary, ramified-five, prime-power, and CRT cases | Local images give all units except the one index-two ramified factor, exactly matching the theorem |
| Prime and reversing strata | Anisotropic, split, Jordan, and fixed-reversor orbit decompositions | The stated strata and counts follow from the quadratic-form zero locus and centralizer action; cyclic/noncyclic mixing is excluded correctly |
| Composite formulas and finite ledger | Jordan-totient shell, cyclic-locus lifts, nine table rows, quotient counts, and unaudited cells | Displayed values agree with the registered raw rows and elementary identities; finite controls are not used as proof |
| Claims/evidence and lifecycle | Claim firewall, source lock, code-review failure/repair, sole registered audit, result review, and result manifest | Hashes and sequence agree; adverse history is preserved; no rerun or finality claim is hidden |
| Literature and citations | Claim-local uses of all 14 cited works, metadata lock, missing/unused keys, and priority language | Positioning is bounded and conservative; 14/14 keys are used, with no missing or unused bibliography entry |
| Anonymity and declarations | Source, extracted PDF text, PDF metadata, URLs, paths, affiliations, email, ORCID, funding, and authorship fields | Author metadata is anonymous and no identifying URL or filesystem path appears; deferred release metadata is explicitly disclosed |
| Build and presentation | Two builds, warnings, references, fonts, vector status, and visual inspection of all 15 pages | Builds are byte-identical and clean; figures, tables, hashes, and references are legible and complete |

## Detailed mathematical audit

| Claim family | Independent check | Status |
|---|---|---|
| C1: matrix commutant | \((e_1,Ae_1)\) is a basis of determinant one; a commuter is determined by its first basis vector and equals \(aI+bA\) | PASS |
| C2: cyclic torsor and exact order | \([Ue_1,AUe_1]=UP\); determinant-unit iff invertible; a cyclic vector is unimodular and has additive order \(q\) | PASS |
| C3: cyclic \(A\)-orbits | The torsor converts the action to left multiplication by \(A\), giving uniform length \(\operatorname{ord}_q(A)\) and cosets \(C_q/\langle A\rangle\) | PASS |
| C4-C5: full quotient and clock | \(C_q\) acts transitively and contains \(A\); the quotient is one fixed point with zeta \((1-z)^{-1}\); no \(q\)-clock survives | PASS |
| C6: symplectic quotient | \(\Delta(Dv)=\det(D)\Delta(v)\); equal determinant values differ by a norm-one unit | PASS |
| C7: norm-image size | Étale local norms are onto, including the binary unramified case; at five the image is exactly the square-residue units; CRT yields the formula | PASS |
| C8: prime shell and reversal | Quadratic-form type gives 1/3/2 centralizer strata; \(J\) pairs split eigenlines and preserves the ramified eigenline, giving 1,1,2,1,2 | PASS |
| C9: composite formulas | Cyclicity is a prime-local unit condition; lift counts multiply and the full torsor quotient remains one class for every composite | PASS |
| C10: exact audit | Both tables reproduce all nine raw result rows; independent result review reconstructed objects rather than only counts | PASS |
| X1-X2: exclusions | Enriched equivariant/orbifold/groupoid/twisted and Hecke/transfer/Fredholm/quantum routes are expressly untested | PASS |

## Literature and citation audit

The literature boundary is appropriate for a low-novelty structural audit.
The manuscript does not claim a new general commutant theorem, a new Hecke
centralizer, a new equivariant zeta, or a general impossibility result. In
particular:

1. Baake--Neumärker--Roberts is presented as the closest algebraic collision
   and as direct prior for rational-lattice centralizers, normal types,
   reversal, and prime-power orbit structure.
2. Kurlberg--Rudnick and Kurlberg--Rosenzweig--Rudnick bound the norm-one and
   invariant-form claims; the manuscript uses the resulting subgroup only as
   a comparison layer and makes no new Hecke or quantum claim.
3. Gusein-Zade--Luengo--Melle-Hernández is cited exactly where the quotient
   clock collapses, and the manuscript distinguishes their finer
   Burnside/equivariant/orbifold constructions from the coarse set quotient.
4. The remaining general-ring, quotient-orbit, group-action, prime-lattice,
   recent prime-power, and finite-torus references are used as adjacent scope
   boundaries rather than as decorative citations.

The bibliography contains exactly 14 unique entries and the source cites all
14: missing 0, unused 0, BibTeX warnings 0. All 56 labels are unique, and all
40 `ref`/`eqref` uses resolve. The current review made no network call, so this
is a manuscript/source-lock positioning audit rather than a new exhaustive
2024-2026 search. Importantly, the manuscript itself makes no exhaustive-
absence or historical-priority claim that would require a stronger search
assertion.

## Evidence and review-history audit

The review chain is coherent and accurately described in the manuscript:

- the independent source-lock review passed the proof-controlled design;
- the first deployment review failed the initial tree because its semantic
  validator accepted a specifically constructed hollow row;
- the repair introduced recursive schemas/types, uniqueness and partition
  checks, exact proof/control keys, and canonical fresh recomputation;
- Round 2 preserved the original failure prefix and issued
  `DEPLOYMENT_PASS` for execution-tree digest
  `87b08f11fc67eae47bdf745f8286700376f3debc5ac3fd190075a5fa2632f436`;
- exactly one registered exact audit was claimed and terminalized, with zero
  candidate numerical runs or reruns;
- the independent result reviewer did not import or run the candidate and
  reconstructed every stored matrix, vector, orbit, norm/determinant fiber,
  quotient transition, and prime reversing record; and
- the strict result manifest binds that `RESULT_PASS` history and the
  official reports.

The plan/figure/citation Round-1 review separately found malformed umlaut
metadata and an overbroad figure phrase. Round 2 verified both bounded
repairs, regenerated assets, and deterministic rendering before the
manuscript was written. The manuscript's provenance appendix retains both
rounds rather than citing only the later pass. The author pre-review audit is
correctly labelled author-side and does not impersonate the present
independent verdict.

## Independent build, PDF, and visual audit

I copied the frozen paper package into two fresh temporary trees and ran its
declared build script independently in each. Results were:

| Check | Build A | Build B | Result |
|---|---|---|---|
| PDF SHA-256 | `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378` | same | exact frozen match |
| LaTeX-log SHA-256 | `f25ef2cac5202002df9dc4de99cf5c9f2ff8d9976ca5f2938f54e6c532746767` | same | byte-identical |
| BibTeX-log SHA-256 | `30b5b34d3dd350f820edce18b81e27d9d41a2c8642deaff7bc9c094907c856cb` | same | byte-identical |
| PDF size/pages | 516261 bytes / 15 | same | exact |
| stderr | 0 bytes | 0 bytes | clean |

The terminal log contains no LaTeX/package error, warning, undefined
citation/reference, overfull box, or underfull box. BibTeX reports
`warning$ -- 0`. PDF inspection found 29/29 embedded, subset, Unicode-mapped
font records, no Type-3 font, and no raster image object. Text extraction from
the two builds was identical. All 15 rendered pages were inspected, with
additional original-resolution checks of the three figures, the dense
tables, the provenance pages, declarations, and bibliography. No clipped
content, accidental overlap, unreadable symbol, broken glyph, missing figure,
or visual evidence mismatch was found.

## Anonymity and integrity audit

The source and PDF metadata identify only `Anonymous Authors`. Searches of
the source and extracted PDF found no affiliation, email, ORCID, grant
identifier, identifying repository URL, or local filesystem path. PDF
metadata contain no custom stream, user properties, form, JavaScript, or
hidden author field. The declarations correctly distinguish this anonymous
pre-review copy from a non-anonymous release and state that authorship,
conflict, and funding metadata must be completed before external submission.
The AI-assisted workflow disclosure is visible and does not transfer
responsibility away from the authors.

The long provenance digests do not themselves disclose an identity in this
package. As a release precaution, however, the authors should ensure that
the exact digests are not already indexed in an identity-bearing public
repository during a double-blind review; this is a venue/deployment question,
not a defect established in the reviewed bytes.

## Detailed comments by section

### Title and abstract

The title accurately signals an audit rather than a new general theory. The
abstract contains the full positive/negative result, the symplectic boundary,
the prime/composite controls, and the enriched-scope exclusion without
inflating novelty.

### Introduction and prior-art boundary

The bounded research question is explicit. Direct prior collisions appear
at the claims they limit, and the contribution list matches theorems later
proved. The explicit statement that no historical-priority claim is made is
consistent with the prose throughout.

### Setup, torsor, and quotient sections

Definitions distinguish the exact-order shell, cyclic locus, full
centralizer, symplectic centralizer, and reversing group. The proof order is
effective: universal basis first, then torsor, then quotient semantics, then
the norm boundary. No circular reliance on finite rows was found.

### Prime, composite, and exact-audit sections

The shell/torsor distinction is visible before the finite tables. The
registered modulus order is preserved, composite controls are predeclared,
and prime-only reversing cells are not extrapolated. The failure-and-repair
account agrees with the preserved review records.

### Route decision and conclusion

The conclusion follows from the proved identity action and all-modulus CRT
statement. It closes only the coarse full-centralizer candidate and does not
generalize the negative result to enriched quotients, Hecke theory,
quantization, spectral constructions, prime-zero correspondences, or RH.

### Appendices, declarations, and references

The claim firewall is accurate and useful. Provenance bindings reproduce.
Declarations are sufficient for an anonymous pre-review artifact and clearly
identify the metadata still needed for release. References are complete,
legible, and citation-closed.

## Questions for the authors (release-stage only)

These questions do not alter the scientific recommendation.

1. For a double-blind external submission, will the exact provenance digests
   remain unindexed or be placed in an anonymous supplement until unblinding?
2. Which release gate will replace the pre-review date and complete the
   authorship/CRediT, conflict-of-interest, and funding metadata required by
   the target venue?

## Non-finding editorial observations

These items are below the Minor-finding threshold and require no re-review:

- In the reversor paragraph, “Every reversor differs from \(J\) by a
  commuter” is mathematically standard in context. “Every time-reversing
  element” would remove even the small possibility that a reader interprets
  “reversor” as including the commuting half of the reversing group.
- The prose spelling “etale” may be changed to “étale” if the venue's style
  supports UTF-8; this is purely typographic.
- Before external submission, replace “Pre-review manuscript” and complete
  the explicitly deferred release metadata. If a venue has a strict main-text
  limit, the hash ledger can move to an anonymous supplement without changing
  the scientific argument.

## Dimension scores

The scores are ordinal review aids, not calibrated acceptance probabilities.

| Dimension | Score | Descriptor | Basis |
|---|---:|---|---|
| Originality (20%) | 64 | Adequate | contribution is intentionally incremental and diagnostic, with direct collisions fully acknowledged |
| Methodological rigor (25%) | 98 | Exceptional | proof/audit authority is separated; adverse validator history is preserved; exact lifecycle is reproducible |
| Evidence sufficiency (25%) | 97 | Exceptional | all central claims have proof or object-level exact evidence, with explicit scope exclusions |
| Argument coherence (15%) | 96 | Exceptional | positive algebraic result leads directly to the clock-erasure and prime-nonspecificity decision |
| Writing quality (15%) | 94 | Exceptional | precise terminology, strong section flow, clean figures/tables, and no material language defect |
| Literature integration (optional) | 93 | Exceptional | closest direct collisions and recent boundary sources are integrated claim-locally |
| Significance and impact (optional) | 68 | Adequate | narrow but useful route-closing result; no broad theory or spectral consequence is claimed |
| **Weighted average** | **90.05** | **Accept** | \(0.20(64)+0.25(98)+0.25(97)+0.15(96)+0.15(94)=90.05\) |

## Round-1 disposition and non-finalization boundary

**Exact Round-1 verdict:** `ACCEPT`.

**Exact finding inventory:** `CRITICAL=0 / MAJOR=0 / MINOR=0`.

No bounded scientific revision or Round-2 manuscript re-review is requested
for the bytes reviewed here. This report is a manuscript-review verdict only.
It does **not** authorize creation of `paper_final.pdf`, mutation of pipeline
state, repository release, external submission, or any other finalization
action. Any change to the manuscript source, PDF, bibliography, figures, or
bound evidence invalidates the byte-specific verdict and must be handled by
the project's existing change-control rules.
