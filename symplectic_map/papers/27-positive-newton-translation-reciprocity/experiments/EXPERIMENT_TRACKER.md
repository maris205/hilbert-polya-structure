# Paper 27 proof-audit tracker

This tracker is an immutable source-design ledger.  “Closed” means that the
mathematical obligation has an explicit proof location or an exact declared
fixture; it does not mean that a numerical experiment was run.  Every run,
code artifact, dataset, plot, CAS transcript, and build is `NOT_AUTHORIZED` at
this gate.

| ID | Obligation | Evidence anchor | State | Run/output |
|---|---|---|---|---|
| T01 | Support/field/rank scope | E0052; RESEARCH_QUESTION §1 | CLOSED | NOT_RUN |
| T02 | Positive integer seed realization | E0033/E0039; PROOF_PACKAGE §2 | CLOSED | NOT_RUN |
| T03 | Exposed-face grouped Hessian determinant | E0052; PROOF_PACKAGE §4 | CLOSED | NOT_RUN |
| T04 | Jacobian independence and injective substitution | E0052; PROOF_PACKAGE §5 | CLOSED | NOT_RUN |
| T05 | Forward and inverse phase order/signs | E0052; PROOF_PACKAGE §3, §5 | CLOSED | NOT_RUN |
| T06 | Exact all-ones translation | E0050; PROOF_PACKAGE §6 | CLOSED | NOT_RUN |
| T07 | (d_V+d_W-2) wall count | E0050; PROOF_PACKAGE §7 | CLOSED | NOT_RUN |
| T08 | Stationary affine ((\lambda,\mu)) tail | E0050; PROOF_PACKAGE §8 | CLOSED | NOT_RUN |
| T09 | Reflected observable-span iff | E0033/E0039; PROOF_PACKAGE §9 | CLOSED | NOT_RUN |
| T10 | One-edge/four-section lower-ideal lemma | E0051; PROOF_PACKAGE §10 | CLOSED | NOT_RUN |
| T11 | C1-to-C2-to-C2 fixture arithmetic | E0025/E0027; PROOF_PACKAGE §11 | CLOSED | NOT_RUN |
| T12 | Hessian cancellation boundary | E0027/E0052; PROOF_PACKAGE §12 | CLOSED | NOT_RUN |
| T13 | P12--P26 claim-level collision screen | E0052; NOVELTY_ASSESSMENT | CLOSED | NOT_RUN |
| T14 | P28--P31 portfolio separation | E0043; NOVELTY_ASSESSMENT | CLOSED | NOT_RUN |
| T15 | Citation metadata and role checks | CITATION_VERIFICATION | CLOSED | NOT_RUN |
| T16 | Anonymous/no-external-effect compliance | E0053; FINAL_PROPOSAL §8 | CLOSED | NOT_RUN |

## Gate ledger

| Gate | Required artifact/action | State at source-design stop |
|---|---|---|
| G0 | Candidate dual PASS and number consumption | PASS (E0052) |
| G1 | Exact source-design authorization | PASS (E0053) |
| G2 | Exactly ten source-design files | PENDING author manifest |
| G3 | Fresh independent source-design review | PENDING |
| G4 | Canonical source lock | NOT_OPEN |
| G5 | Paper-plan artifact | NOT_OPEN; standalone file forbidden here |
| G6 | Publication scope/anonymous source trio | NOT_OPEN |
| G7 | Deterministic build/review gates | NOT_OPEN |
| G8 | Final integrity and cross-paper audit | NOT_OPEN |

## Non-results and stop rules

No empirical result, parameter sweep, random seed, runtime, accuracy,
statistical interval, numerical eigenvalue, or hidden computer certificate is
part of Paper 27.  If a later check disagrees with a displayed proof, the
proof is reopened and the discrepancy is recorded before any manuscript gate;
the check cannot be used to “average away” a counterexample.  A source-design
review finding leaves this tracker unchanged until an append-only disposition
and fresh review close it.

BATCH07_PAPER27_SOURCE_DESIGN_TRACKER_FROZEN
