# Round 10 Papers 29--33 — Stage 2.5 pre-correction checkpoint

Date: **2026-09-03 UTC**

Decision: **FAIL-CLOSED pending one short scholar authorization.** Stage 2.5
has completed its frozen baseline, reference/context, originality, Phase-C,
and 294-claim semantic work, but three finding groups require exact scoped
repairs before the final integrity report can pass. Stage 3 is not authorized.

## Completed audit population

- Stage-2 deterministic replay: **543/543 PASS**, including five isolated
  builds and 66 fresh pages.
- References: **116/116 identities queried/replayed**. P30 and P31 are clean;
  P33 preserves one `PLAUSIBLE`, page-unpinned background source; P29 has one
  containing-volume editor defect; P32 has one stale live source-status label.
- Citation-context samples: P29 **7/22**, P30 **8/26**, P31 **7/22**, P32
  **8/26**, and P33 **18/48** citation uses, all accurate within their stated
  boundaries. Every canonical citation remains `anchor=none` and
  claim-to-passage support remains `INCONCLUSIVE`.
- Originality: **116/374 paragraphs (31.0%)**, covering every major section of
  every paper. Exact public-Web, local 26-manuscript, and known-author public-
  work checks found **0 substantive exact reuse**. Shared strings are workflow,
  Route-status, or declaration templates. No professional Turnitin/iThenticate
  detector was available; scientific novelty remains separately unassessed.
- Claim registry: **480 registered claims**, **382 selected distinct claims**,
  and **454 evidence tuples**. P29 (71), P30 (78), P31 (71), and P33 (74) now
  have claim-by-claim semantic tables: **292 VERIFIED, 1 MINOR_DISTORTION, 1
  MAJOR_DISTORTION**. P32's 88 selected claims are intentionally deferred to
  the post-repair bytes.
- Phase C/D7: **244/244 quantitative/data-tagged surfaces** checked
  (45/53/45/58/43). They are design constants, formal definitions,
  workflow/bibliography counts, or structural tags: **0 reported statistical
  results and 0 project-owned scientific experiment results**. P33's two
  longtables are prospective design tables and are traced 2/2.
- Scholar experiment declaration: `status=no_experiments_declared`,
  `declared_by=scholar`, `experiment_provenance=[]`; the exact C4 boundary is
  preserved in every Phase-C sidecar.

## Findings requiring authorization

1. **P29 / blocking MEDIUM — `P29-AB-MEDIUM-01`.** `P29-S15` correctly
   identifies Grunewald's chapter but lists only Graham Higman as editor of
   *Word Problems II*. The publisher/catalogue records list S. I. Adian,
   W. W. Boone, and Graham Higman. Only that BibTeX editor field may change.
2. **P31 / blocking MAJOR — `P31-E1-056`.** The manuscript says that any one
   of `G`, `I`, or `C` cannot reconstruct the other two. Its own definitions
   show that complete incidence relation `I` can project to `G` and `C`; only
   `G` or `C` alone loses occurrence-level information. The authorized text
   narrows this assertion without changing counts or the architecture.
3. **P31 / nonblocking MINOR — `P31-E1-078`.** The conclusion must distinguish
   the completed bounded textual-originality screen from scientific novelty,
   which remains unassessed.
4. **P32 / nonblocking MINOR — `P32-AB-MINOR-01`.** P32-S13 is now
   bibliographically verified by an authoritative journal record plus an
   independent catalogue, but five live current-status statements still say
   `PLAUSIBLE`. They may change to “bibliographically VERIFIED but
   background-only”; the historical Phase-2 25/1 statement, `anchor=none`,
   `INCONCLUSIVE`, and every scientific claim remain fixed.

The complete target and operation boundary is
`BATCH_ROUND10_STAGE2_5_CORRECTION_AUTHORIZATION_REQUEST.md`, SHA-256
`778c5ef44b3ef3790f0e34098923735edbd9a2af681c79d4f0fc8f83a69a7e16`.
The two earlier commentary hashes are superseded and must not authorize a
write.

## Roadmap and science boundary

The five papers remain on **Route A A0/A1 foundation/interface work**. They
have five distinct frozen continuous-time subtypes, but no scientific
execution and no formal Route result:

- formal Route-A tuples: **0/5**;
- positive arithmetic A2: **0/5**;
- A3/A4 completion: **0/5**;
- Route-B invocation: **0/5**.

The repair cannot change a dynamical subtype, clock, primitive-owner rule,
normalization, cutoff, scientific value, or Route state. Once authorized, the
workflow will apply only the named bytes, rebuild P29/P31/P32, regenerate the
affected sidecars, audit all 88 P32 selected claims and the affected P31/P29
surfaces, compile five passports/reports, validate, update README/state, and
SSH-push `flow_systems/`. It must then stop again at the mandatory Stage-3
confirmation boundary.
