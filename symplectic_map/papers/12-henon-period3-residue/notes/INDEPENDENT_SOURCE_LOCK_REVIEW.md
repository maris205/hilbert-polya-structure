# Independent Source-Lock Review — R1

- Candidate: `henon_period3_residue_v1`
- Review date: 2026-08-16 UTC
- Reviewer relation: fresh independent reviewer; I did not author any bound file
- Bound lock: `experiments/source_lock.json`
- Required lock SHA-256: `fc6277812d937bc07fc855145a6360b628dced34e1a3689c92ed40d351cce29f`
- Recomputed lock SHA-256: `fc6277812d937bc07fc855145a6360b628dced34e1a3689c92ed40d351cce29f`

## Canonical verdict

`REPAIR_REQUIRED`

The mathematical, literature, and package-integrity checks below pass. The
frozen package nevertheless fails closed because four normative protocol or
cross-file inconsistencies remain. No implementation, registered execution,
result, figure, or manuscript is authorized by this review.

## 1. Mechanical source-lock audit

Strict JSON parsing with duplicate-key rejection passed. The lock contains 14
distinct bound paths, declares 14, excludes its own path and self-hash, and all
14 recomputed SHA-256 values agree byte-for-byte:

| Binding | Recomputed SHA-256 | Result |
|---|---|---|
| `notes/RESEARCH_QUESTION.md` | `c4d7c734af6dfd534a5019e3073ed08e3327491f43f841bd2c006a269adb7cb1` | PASS |
| `notes/NOVELTY_ASSESSMENT.md` | `c497dc4e2c404fbbfc3c89450991964d1049f06288a051bc647a15005a66146a` | PASS |
| `notes/PROOF_PACKAGE.md` | `36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9` | PASS |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `dd9de5be94dfb115b1bc547307b90622a639673870413e1c26fa899c0b36860f` | PASS |
| `notes/CITATION_VERIFICATION.md` | `eb99e7ab59e5d2947b6d5dab0d23dd471c05d090280f7915f010210b021e39ee` | PASS |
| `experiments/EXPERIMENT_PLAN.md` | `39d87e1ef3606f2cf85cb2a76ed957e9e16bd534f0f899a035ff5db46e3d7c8a` | PASS |
| `experiments/EXPERIMENT_TRACKER.md` | `763ed28cb579cb80af97779c863a300c39cbb533807030987244ca2df0fc9b10` | PASS |
| `refine-logs/FINAL_PROPOSAL.md` | `3793d8fc8210999d27b528f1aa3d42af88b6adc7d7f7afd9ccc4ea1cb32af950` | PASS |
| `refine-logs/REFINEMENT_REPORT.md` | `974a7d9509b4e2653359d20fa6b04752617303a015d15032f1c8da41ee483998` | PASS |
| `refine-logs/REVIEW_SUMMARY.md` | `9de75aa92ff47528fed649623a210a736541ec04c22d0bd9caf82619fc3783bb` | PASS |
| `refine-logs/INITIAL_PROPOSAL.md` | `46984d6028e52842602f5a1d5a4f41b13aa9a840528c21328af3f4eb5ea5c8d6` | PASS |
| `refine-logs/round-1-review.md` | `757279f1b7274f20f619db78f4ae38214927d8ce04161c63d5da89b919ae86ba` | PASS |
| `refine-logs/round-2-review.md` | `7a35bd1feb2283e6934032a489c648e116e712ccbb14d5377c5d9575a7620277` | PASS |
| `refine-logs/score-history.md` | `edd13b5ce88132f6ec08f571885ecb6b6501b2eafacb57c9d4f9df561dd04b28` | PASS |

The pre-review Paper-12 inventory contained exactly the 14 bound documents
plus the self-excluded lock. No code, registered-run, result, figure, or
manuscript artifact was present. This review is the sole permitted post-lock
write.

## 2. Independent mathematical audit

The complete 1,639-line proof package was reviewed. No theorem-level blocker
was found.

- **C10, Steps 7 and 10 — PASS.** The all-distinct, exactly-two-equal, and
  all-equal root patterns give the claimed strict local valuation bounds. On
  the diagonal, (t_\epsilon=q^3+3\epsilon^2q) together with (q^2=0)
  closes the previously delicate branch and eliminates the forbidden term.
- **C13, Step 9 — PASS.** The terminating four-branch recurrence, Laurent and
  admissible-tuple extractions, and exponent/sign shifts agree. Equation
  (9.14) follows from coefficient extraction in
  ((1-z)^N(1-2z+z^2)^{-n-1}). The distinguished-coordinate rule for
  (j\ge1), transfer-flow count, guarded range, orientation multiplicity, and
  separate (j=0) incoming patterns reproduce the stated finite (H/A/D)
  certificate.
- **C16, Step 12 — PASS.** The independent quartic tensor ledger gives
  (D_2=4^9(-6)=-1572864). The constant ledger
  (R_{999}=-6, R_{966}=2, R_{933}=0, R_{663}=-1) reproduces
  (-1296000), independently of the all-
  (m) collapse.
- **C17, Step 13 — PASS.** The transverse Jacobian is invertible, the local
  fixed branch has multiplicity equal to the root multiplicity of (p), and
  the length subtraction (64-4=60), followed by division by three for the
  cyclewise display, is justified.

The low-period scheme interpretation, normalized conjugacy quotient,
two-term weight support, parity statement, quartic full-fiber classification,
and scoped minimality chain were also checked without finding a mathematical
blocker.

## 3. Protocol audit apart from the blockers below

- P7 binds the full recurrence/Laurent/(9.14)/distinguished-coordinate/flow/
  (j=0) chain; P8 keeps the Step-10 zero moment distinct from the Step-13
  local fixed multiplicity. PASS.
- Track Q is genuinely pre-collapse and Track R genuinely collapsed; their
  prohibited-access lists prevent shared scientific or arithmetic code.
  Definitions-only input and the acceptance ledger are isolated from both
  engines. PASS.
- The intended scope of (T_{\mathrm{reg}}=(8,9)) is two isolated
  implementation-falsification indices, not a scan, parity proof, trend, or
  nonvanishing witness. PASS subject to blocker 1's incorrect rationale text.
- The incidental development recheck at (m=2,\ldots,7) is disclosed as
  unregistered, non-evidentiary, value-free, and quarantined with historical
  runtime access counter zero. PASS.
- Universal (D_m\ne0), all-
  (m) separation, global quartic separation, global (P(4)=3), method or
  family priority, and other listed overclaims remain explicit nonclaims.
  PASS.

## 4. Primary-source and novelty gate

The eleven primary-source records were independently spot-checked for
bibliographic identity, status, and claim-safe role: Cantat--Dujardin;
Friedland--Milnor; Cattani--Dickenstein--Sturmfels;
Cvitanovic--Hansen--Rolf--Vattay; Dullin--Meiss; Huguin; Hutz (2010); Hutz
(2020); Guillot--Ramirez; Ueda; and Bianchi--He. Direct-precedent, method-prior,
adjacent-result, and background roles are correctly separated. In particular,
the Cantat--Dujardin family and period-one/two blindness are not claimed as
new, and global-residue machinery is credited as prior art.

The bounded primary-source search through the 2026-08-16 cutoff found no
direct collision for the exact quartic period-three moment, full-fiber scoped
separator, or all-
(m) finite coefficient certificate. This remains a bounded no-hit result,
not a priority or universal-absence claim. The post-proof novelty score
(6.2/10\ge5) and standalone-size score (5.8/10\ge5) are supportable for a
borderline specialist note. PASS.

## 5. Blocking repairs

1. **False (T_{\mathrm{reg}}) rationale.**
   `experiments/EXPERIMENT_PLAN.md` says (m=8,9) exercise “the two adjacent
   values of \(\lfloor m/2\rfloor\).” In fact both floors equal 4. The intended
   distinction is the same floor while the ceiling changes from 4 to 5 (with
   adjacent even/odd and guarded-range handling), which the lock's tuple role
   already states more accurately. Correct the normative plan. The same old
   wording may remain in the hash-preserved historical round-2 record, but a
   normative synthesis must explicitly supersede it.
2. **Claim-ID namespace collision.**
   `experiments/EXPERIMENT_PLAN.md` uses aggregate `C1` for the quartic package
   and `C2` for the all-
   (m) package, while `notes/CLAIMS_EVIDENCE_MATRIX.md` uses atomic `C1` for
   the category assumption and atomic `C2` for fixed-scheme nilpotence.
   `experiments/EXPERIMENT_TRACKER.md`, B1--B5, and the lock's claim count then
   refer to `C1`/`C2` ambiguously. Give the aggregates a distinct stable
   namespace such as `PC1`/`PC2`, provide an explicit aggregate-to-atomic map,
   and propagate it through every normative reference and the lock.
3. **Decision-string drift.**
   `notes/CLAIMS_EVIDENCE_MATRIX.md` records
   `GO_BORDERLINE_STANDALONE_EXACT_DYNAMICS_NOTE`, whereas the novelty ledger
   and lock record `GO_BORDERLINE_STANDALONE_SPECIALIST_NOTE`. Canonicalize one
   decision enum throughout the normative package.
4. **Stale normative lock state.**
   `notes/RESEARCH_QUESTION.md` and `notes/CLAIMS_EVIDENCE_MATRIX.md` still say
   source-package synchronization is pending, and
   `refine-logs/REFINEMENT_REPORT.md` still instructs the project to synchronize
   the package and build `source_lock.json`. Those steps had already completed
   when v1 declared `source_design_frozen=true`. Update the normative state to
   say the v1 package is frozen and only fresh independent review is pending.

Because each correction changes bound bytes, remediation requires a new lock
version with all hashes recomputed, followed by a fresh independent review.
