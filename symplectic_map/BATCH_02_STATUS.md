# Five-Paper Autonomous Batch 02

## Material Passport

- Batch start: 2026-08-14
- Scope authority: the user's `继续` instruction after Batch 01 completed,
  preserving the current Session's research family, directory convention,
  Route-A/Route-B gates, forbidden-data policy, independent-review rules, and
  GitHub synchronization procedure
- Checkpoint policy: per-paper and ordinary stage confirmations remain
  pre-authorized by the standing five-paper instruction; integrity failures,
  hard blockers, and genuine major breakthroughs are surfaced immediately
- Cross-model upload: disabled
- External prime/zero data: forbidden unless a future frozen candidate first
  passes its arithmetic entry gates
- Batch status: `COMPLETE_SYNCED`

## Paper Queue

| Batch paper | Project directory | Current stage | Status | Route outcome |
|---:|---|---|---|---|
| 1 | `papers/7-base2-exponent-clock` | final manuscript frozen after independent Round-2 PASS | COMPLETE_LOCAL | exact 2-adic valuation proved; no \(\pm2^n\) hit for development-seen \(2\le n\le7\); equality OPEN for \(n\ge4\) |
| 2 | `papers/8-cat-torsion-capacity` | final manuscript frozen after independent Round-2 PASS | COMPLETE_LOCAL | `INTRINSIC_TORSION_CAPACITY_CERTIFIED / A0_FAIL_PROVES_TOO_MUCH`; prime-order carriers are abundant but the order clock over-generates all integers and is nonlocal |
| 3 | `papers/9-cat-prime-shell-multiplicity` | final manuscript frozen after independent Round-2 PASS | COMPLETE_LOCAL | `PRIME_SHELL_MULTIPLICITY_OBSTRUCTION_CERTIFIED / A0_FAIL_GLOBAL_NORMALIZATION_ONLY`; unweighted prime-shell factors have multiplicity (m_p), while the exact repair is shell-global and tautological |
| 4 | `papers/10-cat-centralizer-quotient` | final manuscript frozen after independent Round-2 PASS | COMPLETE_LOCAL | `CENTRALIZER_CYCLIC_TORSOR_CERTIFIED / A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC`; one-class full-centralizer compression kills the native period and requires a modulus-dependent external label |
| 5 | `papers/11-cat-equivariant-clock` | final manuscript frozen after independent Round-2 PASS | COMPLETE_LOCAL | `EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED / A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC`; equivariant refinements trade compression for labelled group data but yield no family-uniform intrinsic modulus clock |

## Paper 7 Starting Question

For the frozen PCF quadratic

\[
g(z)=z^2-u,\qquad u^3-2u^2+2u-2=0,
\]

can an exact period-\(n\) orbit with rational multiplier satisfy
\(\lvert\lambda\rvert=2^n\) for any \(n\ge2\)?  Equivalently, since
\(\lambda=2^n\prod_{j=0}^{n-1}z_j\), can a primitive cycle product be
\(\pm1\)?  The raw-prime theorem from Batch 01 does not decide this case.

## Standing Scientific Rules

- The target `2` is inherited from the previous all-period theorem, not chosen
  after a scan.
- Formal dynatomic period and least period must be separated exactly.
- A finite cutoff audits implementation only; an all-period conclusion must
  come from a proof.
- Rational multiplier, rational modulus, and characteristic exponent are
  distinct predicates and may not be interchanged.
- No prime table, Riemann-zero data, fitted target list, or post-hoc parameter
  choice is permitted.
- If Paper 7 closes the remaining finite/algebraic boundary, Paper 8 moves to
  the closest same-family escape mechanism: a point-dependent, non-locally
  constant cocycle whose periodic readouts are not contained in a fixed
  finite-dimensional rational span.

## Batch Log

- 2026-08-14: Batch 02 opened after Batch 01 reached `COMPLETE_SYNCED` at
  GitHub commit `e38ebee`.  Paper 7 was selected from the sole explicit
  exponent-prime boundary retained by the independently reviewed Batch-01
  Paper 2; current-literature search, theorem attack, and exact source-lock
  design began in parallel before any registered candidate execution.
- 2026-08-14: Before the Paper-7 source lock was written, one explicitly
  exploratory exact gcd scratch check reused the prior paper's code for
  periods 1--8.  It tested the equivalent cycle-product targets `+1` and
  `-1` and found no common exact-period factor.  These periods are therefore
  development-seen and cannot be presented as confirmatory evidence; no
  prime table, zero data, parameter search, or approximate target was used.
- 2026-08-14: A second pre-lock development benchmark re-ran periods 4--7
  using the inherited exact engine; target gcds were trivial and target
  resultants nonzero.  It was recorded as development-seen, not validation.
  Source lock v1 was then frozen and independently audited.  The audit's
  exact-period semantic repairs were incorporated into source lock v2 at
  SHA-256
  `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1`.
  The all-period result is now an exact local theorem: higher-period points
  are 2-adic units and rational multipliers are \(2^n\) times odd integers.
  The equality \(\Lambda=\pm2^n\) is proved absent for periods 2 and 3, is
  only finitely audited thereafter, and remains OPEN for arbitrary
  \(n\ge4\).
- 2026-08-14: The first independent pre-execution code review bound source
  lock v2 and code-tree SHA-256
  `bb648aa54d98b27df71ab849b7515312003d45898aefe9186f114739c1f3eb07`
  and returned `DEPLOYMENT_FAIL`.  The mathematical exact-set, local-field,
  finite-field, and control implementations passed, but three fail-closed
  engineering defects were reproduced: alias/dynamic/symlink escapes in the
  isolation scanner, an inconsistent zero representation for a genuine
  target hit over `Q(u)`, and a vacuous post-run manifest/lifecycle validator.
  The registered candidate remains unexecuted (`P4=0`).  Repairs are being
  made under the same source lock and must receive a fresh independent review
  before periods 2--7 can run.
- 2026-08-14: The repaired tree
  `8716715b9449e2943bfbe1e0566c61d2271260cada2f23c6aa70c6b44d4e5b37`
  passed 34 safe tests and independently closed the algebraic zero,
  manifest/lifecycle, symlink, path-swap, wrapper, and serialization defects.
  Round 2 nevertheless returned `DEPLOYMENT_FAIL` after reproducing one
  narrower scanner bypass: a forbidden callable stored in a named tuple or
  dictionary could be recovered by subscript and invoked without a finding.
  No registered period was executed.  The next repair is restricted to this
  callable-provenance path and requires a fresh Round-3 tree binding.
- 2026-08-14: Round 3 bound tree
  `dd346942647bdd74f2c435d5396a720950d6bed246e88686d15f898e18afe3f4`
  and failed closed on one still narrower capability-flow gap: forbidden
  callables transported through a conditional expression, a lambda return,
  or a function default argument were not tracked.  The three paths were
  repaired without changing the mathematical candidate.  Round 4 then bound
  tree `7a5ea42ea52d35bf4d6608b1175a43ab81ceaa9ed8fbfd0e35e183920dbdd27a`
  and returned `DEPLOYMENT_PASS`; 38 safe tests passed and the registered-run
  counter was still zero at authorization.
- 2026-08-14: The sole registered Paper-7 execution then ran the frozen exact
  periods 2--7 once.  Both cycle-product targets `+1` and `-1` had exact gcd
  degree zero in every period, so no `TARGET_HIT_HALT` occurred.  The run is
  classified `BASE2_EQUALITY_ABSENT_N2_TO_N7_DEVELOPMENT_SEEN`, because every
  registered period had been inspected before source lock; it supplies no
  blind confirmatory evidence and does not close the all-period question for
  `n >= 4`.  The strict result manifest passed with no missing, extra, unsafe,
  or semantically inconsistent artifact; external prime/zero access and
  numerical candidate runs remained zero.
- 2026-08-14: Paper 7 passed an independent result-integrity gate, an
  independent plan/figure gate, and two manuscript-review rounds.  Round 1
  required four proof-wording clarifications and no major revision; Round 2
  closed all four and returned `PASS / MAY_FINALIZE` at 9.2/10.  The approved
  11-page final PDF is byte-identical to the reviewed revision at SHA-256
  `fac4b7a3a5f19f515ebd982a3eef0e3c63e1c025616fbaeb62a94621d19632bf`;
  the project terminal state is `COMPLETE_LOCAL_FINAL_REVIEW_PASS`.
- 2026-08-14: Paper 8 formally opened only after Paper 7 reached that terminal
  state.  Its frozen-object candidate is the standard hyperbolic cat map
  `[[2,1],[1,1]]` on the two-torus.  The planned positive theorem concerns
  exact-period prime-order torsion obtained from primitive divisors of
  `|det(A^n-I)|`; the planned negative audit asks whether the invariant clock
  `log ord(x)` has enough locality or specificity to support the arithmetic
  mechanism, rather than treating mere availability of every integer order as
  prime emergence.
- 2026-08-14: Paper 8 source lock v1 froze the standard trace-three cat map,
  the Flatters primitive-divisor bridge, the repaired three-case negative-trace
  parity argument, the exact standard-cat exception set `{1,6,12}`, and the
  torsion-order clock audit.  An independent source-lock review passed.  The
  first pre-execution code review found a `sys.modules` capability-laundering
  path; a minimal repair received a fresh `DEPLOYMENT_PASS` at execution-tree
  SHA-256
  `b4441fb68ac42ab1649ee62037fb7cdf741aa9c09a0b0d5cffc4003697caa059`,
  with 21 safe tests passing and no registered artifact yet present.
- 2026-08-14: The sole Paper-8 registered exact audit then executed periods
  1--12 exactly once.  It certified the fixed determinant ledger, the
  prime-torsion period profiles, the mod-5 Jordan repair at period 10, and the
  clock/monodromy contracts.  The raw result classification is
  `INTRINSIC_TORSION_CAPACITY_CERTIFIED_A0_FAIL_PROVES_TOO_MUCH`; no period
  above 12, numerical candidate, external prime table, or Riemann-zero data
  was used.  The post-run test suite passed 21/21.
- 2026-08-14: The first post-run manifest attempt failed closed because the
  original validator compared a claim-bound pre-run JUnit snapshot with the
  deliberately refreshed post-run JUnit.  A dual-tree repair now preserves
  the immutable execution tree and records a separate non-executing analyzer
  tree.  Independent review then found one further lifecycle defect: the
  pre-write builder had no read-only validator for the final directory after
  `result_manifest.json` was added.  No candidate rerun occurred and all raw
  execution hashes remained unchanged.  A bounded final-inventory closure
  repair and fresh independent review are in progress.
- 2026-08-14: The bounded final-inventory repair introduced separate exact
  pre-write and final inventories plus a read-only validator for an existing
  manifest.  A fresh independent Round-2 analyzer review reproduced the full
  one-shot lifecycle and tamper matrix and returned `POSTRUN_ANALYZER_PASS`.
  The live V2 dual-tree manifest was then written exactly once and its
  read-only closure passed with no errors at SHA-256
  `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f`.
  An independent final result-integrity audit subsequently rechecked the
  exact 11-file result inventory, 14 non-self hashes, determinant and finite-
  field ledgers, single-run lifecycle, proof-only tail, forbidden-access
  flags, and Route labels and returned `PAPER8_RESULT_INTEGRITY_PASS`.
- 2026-08-14: Paper 8 then passed an independent plan/figure/citation gate
  and two fresh manuscript-review rounds.  Round 1 found no mathematical or
  evidentiary blocker and requested only three local repairs: use
  `n log rho(A)` for the negative-trace instability clock, add a direct
  ordinary-period-set baseline, and close the citation-ledger release state.
  Round 2 verified all three, returned `PASS / MAY_FINALIZE` at 9.2/10, and
  found no residual issue.  The approved 12-page final PDF is byte-identical
  to the reviewed revision at SHA-256
  `5ff37aca10905bd7fd84f25a81e47601ed9883259519b02e2809f77485770d98`;
  the project terminal state is `COMPLETE_LOCAL_FINAL_REVIEW_PASS`.
- 2026-08-14: Paper 9 formally opened only after Paper 8 reached that terminal
  state.  It audits the prime-shell orbit multiplicity left unresolved by the
  capacity theorem: whether an unweighted primitive-orbit product on the
  standard cat map can have one Euler factor per rational prime, or whether
  the finite-field orbit decomposition forces a multiplicity obstruction.
- 2026-08-15: Paper 9 proved that the standard cat map's (p)-torsion shell
  has one primitive orbit only at (p=2), whereas every odd prime has
  (m_p\ge p-1).  Its sole registered exact audit reproduced the frozen
  shells (p=2,3,5,7,11), 203 nonzero points, and 37 primitive cycles; the
  raw-return and one-time orbit-label products were separated exactly.  A
  fixed nonzero scalar denominator cannot collapse degree (m_p) to one;
  the exact fractional repair succeeds only by global shell normalization
  and works just as mechanically for composite-order shells.  Four rounds of
  fail-closed code review preceded the one-shot run; independent result and
  asset gates passed.
- 2026-08-15: Paper 9 then passed two independent manuscript rounds.  Round 1
  requested four minor traceability and standalone-presentation repairs;
  Round 2 closed all four and returned `PASS / MAY_FINALIZE` at 8.5/10.  The
  approved 15-page final PDF is byte-identical to the reviewed revision at
  SHA-256
  `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6`;
  the project terminal state is `COMPLETE_LOCAL_FINAL_REVIEW_PASS`.
- 2026-08-15: Paper 10 formally opened only after Paper 9 reached that
  terminal state.  It examines the live escape explicitly left outside the
  scalar multiplicity theorem: quotienting prime-shell orbit families by the
  finite-field centralizer of the cat matrix, while auditing whether the
  resulting class compression is intrinsic dynamics or merely another
  shell-global arithmetic normalization.
- 2026-08-15: Paper 10 source lock v1 passed a fresh independent mathematical
  and novelty audit at SHA-256
  `aa99218099f2e2c3e14367bfe75f9da881d8b204689c07c6fa963f9582b696e2`.
  The cyclic locus is a torsor for the full local centralizer, but the coarse
  quotient contains the cat map in the quotienting group and therefore has
  identity dynamics and native period one.  The determinant-one/symplectic
  centralizer leaves exactly the norm-image strata, while the one-class full
  quotient uses modulus-dependent nonsymplectic pseudo-symmetries and works
  for composite moduli as well as primes.  The frozen outcome is
  `CENTRALIZER_CYCLIC_TORSOR_CERTIFIED / A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC /
  ROUTE_B_NOT_OPENED`; implementation is now authorized, but registered
  execution remains closed pending an independent deployment review.
- 2026-08-15: Paper 10 then passed a two-round independent deployment audit.
  Round 1 correctly rejected a hollow result-schema validator; the bounded
  repair changed every registered row to an exact fresh-engine canonical
  comparison, and Round 2 rejected the original attack plus 36 nested
  variants before authorizing execution tree
  `87b08f11fc67eae47bdf745f8286700376f3debc5ac3fd190075a5fa2632f436`.
  The sole registered audit evaluated exactly the nine frozen moduli
  `2,3,5,7,11,4,6,9,10`.  An independent result-integrity review recomputed
  every shell, cyclic locus, centralizer, norm fiber, and orbit partition and
  returned `RESULT_PASS`.  The one-shot result manifest closed at SHA-256
  `db1dda86ff8bf13fd307cbb1eb6ea6a8c3c0de531ea5b1cc28a58c7bb085b658`
  with 9/9 files and 10/10 gates; registered audits equal one, candidate
  numerical runs equal zero, and no rerun occurred.
- 2026-08-15: Paper 10 passed an independent plan/figure gate after a bounded
  bibliography-encoding and reversor-caption repair, followed by two fresh
  manuscript rounds.  Round 1 accepted the bound bytes with no findings;
  Round 2 independently rechecked the no-change provenance and returned
  `PASS / MAY_FINALIZE`, again with no findings.  The approved 15-page final
  PDF is byte-identical to both isolated clean builds and the reviewed
  revision at SHA-256
  `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378`;
  the project terminal state is `COMPLETE_LOCAL_FINAL_REVIEW_PASS`.
- 2026-08-15: Paper 11 formally opened only after Paper 10 reached terminal
  state.  It audits the exact boundary left outside the coarse quotient note:
  whether Burnside-ring, equivariant, orbifold, or stacky refinements retain
  source periods or stabilizer data, and whether any retained structure
  supplies an intrinsic prime/modulus clock rather than another externally
  labelled shell construction.
- 2026-08-15: Paper 11 source lock v2 passed a two-round independent audit at
  SHA-256
  `331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b`.
  The first review corrected one categorical overstatement: the orbifold
  reduction on exact-period Burnside exponents is additive, not a ring or
  power-structure homomorphism.  The frozen information-loss hierarchy now
  separates coarse/orbit-counting collapse, fixed-point Burnside recovery of
  only `<A>`, labelled effective `C x Z` recovery of `A` modulo the action
  kernel, and static inertia/stabilizer data.  The source package also fixes
  the effective `C6/C2 union C6/C3` counterexample with no period-six factor.
  Implementation is authorized, while registered execution remains closed
  pending an independent deployment review.
- 2026-08-15: Paper 11 passed a two-round independent deployment audit and one
  registered exact run over the nine frozen arithmetic rows plus the separate
  structural `C6/C2 union C6/C3` control.  Its first manifest attempt failed
  before writing because a post-run analyzer compared JSON lists with Python
  tuples.  The immutable execution chain was preserved; a separate dual-tree
  analyzer reproduced the failure, repaired only the read-only semantic
  layer, passed an independent analyzer review, and wrote the V2 manifest
  exactly once.  Final read-only closure passed at SHA-256
  `a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c`
  with an exact 11-file inventory.  The registered run count is one, numerical
  candidate and rerun counts are zero, and the frozen classification is
  `EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED /
  A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.
- 2026-08-15: A fresh post-run scope audit caught and repaired a publication-
  level quantifier overstatement without changing the frozen execution chain.
  The point-cardinality reduction at `q=2` is the unique locked row/type with
  both source-period support and unit exponent; the certified obstruction is
  family-uniform rather than exception-free per row, and `r_2=r_4=3` still
  defeats modulus specificity.  The independent audit returned
  `PASS_WITH_SCOPE_CORRECTION` at SHA-256
  `f7b365c9e6c8933cf3cbcaf3c96692cbacdaabcc84400bdc629f1d482cb243e4`.
  The publication layer also corrected the Walton bibliography metadata to
  the DOI-authoritative JNT 192 (2018), 386--405 record; neither correction
  altered source, code, registered results, or the dual-tree manifest.
- 2026-08-15: Paper 11 passed the independent plan/figure/citation gate and
  two fresh manuscript rounds.  Round 1 requested only four reader-facing
  internal `Paper 10/11` labels be rewritten as standalone prose; the exact
  four-line repair preserved every scientific claim and the `q=2` scope.
  Round 2 returned `PASS / MAY_FINALIZE` with zero Critical, Major, Minor, or
  residual finding.  The approved 19-page final PDF is byte-identical to the
  reviewed revision and two new isolated clean builds at SHA-256
  `9f9a0a25ba82a56d10980ecafad3be8cc893523fc494e5dd66a9307dd831888b`;
  the project terminal state is `COMPLETE_LOCAL_FINAL_REVIEW_PASS`.
- 2026-08-15: The batch pre-audit found one non-scientific Paper-10 manifest
  self-description defect: the nested post-run JUnit record carried the
  correct POST hash but a stale PRE path because the frozen parser always
  emitted the pre-execution pathname.  The original execution tree, 9/9
  result inventory, two JUnit files, raw result, reviews, final paper, and all
  Paper-11 whole-hash bindings remain exact.  A notes-only immutable metadata
  erratum at SHA-256
  `c433451ef942f0e88af8441ed2117e2e9933dac097f48a4516e3bbf5f216833b`
  now supplies the authoritative path interpretation; a fresh independent
  review returned `ERRATUM_PASS / BATCH_METADATA_BLOCKER_CLOSED` at SHA-256
  `62838ef837a17b91414f1e8327d76a7dc114b7b52d6493e5fb88468901bf77ee`.
  No candidate, registered run, or test was rerun.
- 2026-08-15: All five papers are locally terminal.  The root README,
  candidate registry, and obstruction registry now index Papers 7--11 with
  their open boundaries and Route labels.  Independent five-paper batch
  audit and GitHub synchronization remain pending; no sixth paper is opened.
- 2026-08-15: The independent five-paper final audit returned
  `BATCH02_FINAL_AUDIT_PASS` with zero blocker and six explicitly bounded
  historical/schema advisories.  It independently reproduced all five final
  PDF identities, Round-2 dispositions, terminal integrity chains, exact
  result inventories, JUnit summaries, figure/citation closures, the Paper-10
  metadata erratum overlay, the Paper-11 `q=2` scope correction, and all
  Papers 7--11 registry links.  The audit authority is
  `BATCH_02_FINAL_AUDIT.md`, SHA-256
  `765eea5cb974d70f80d25deafaa6d711be9940f397a24439460058420767292c`.
  Local status is now `COMPLETE_LOCAL_PENDING_GITHUB_SYNC`; no sixth paper
  has been opened.
- 2026-08-15: The explicit Batch-02 allowlist was synchronized to GitHub in
  bulk commit `3b91eb95e1917bb73c81bbc58b1d813c1ef5ac7a`.  The commit added the
  five frozen paper packages, batch audit, dashboard, README, and two
  registries as 489 staged paths (486 additions and 3 modifications), with
  zero deletions, zero gitlinks, and no nested `.git`, cache, checkpoint, or
  build-intermediate payload.  The live `origin/main` identity was checked
  immediately before and after the push.  This final dashboard-only closure
  records `COMPLETE_SYNCED`; all scientific artifacts remain byte-identical,
  and no sixth paper has been opened.
