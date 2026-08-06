# Repository update

Priority note (2026-08-05): the former N+1/N+2 ordering is superseded by the
breadth-first tournament in `../next_paper_henon_candidate_search/`.

Date: 2026-08-05

## Added

A new planning-only project, `next_paper_henon_foundations`, has been added for
the proposed Paper-5-centered follow-up.

Files:

- `README.md`: executive thesis, exact formulas, Route-A position, and primary
  references.
- `SOURCE_AUDIT.md`: legacy claim audit, exact low-parameter obstructions, and
  duplication firewall.
- `PAPER_ROADMAP.md`: manuscript architecture, theorem ladder, timeline,
  decision gates, and fallback ladder.
- `refine-logs/FINAL_PROPOSAL.md`: frozen problem anchor and dominant
  contribution.
- `refine-logs/EXPERIMENT_PLAN.md`: reproducible, target-free trace experiment.
- `refine-logs/EXPERIMENT_TRACKER.md`: theorem/run ledger and stop conditions.
- `code/README.md`: planned package and implementation rules.
- `results/README.md`: future artifact contract; no scientific result is
  currently stored.
- `paper/README.md`: manuscript claim contract.

## Scientific decision

The planned paper will not continue the legacy zero-fitting program. It will:

1. prove the quartic Weyl-law obstruction;
2. use, with attribution, one specified natural unitary quantization of the
   discrete Hénon map while recording its gauge/subprincipal ambiguity;
3. derive and test a localized periodic-orbit trace formula on the certified
   local \(H_6\) survivor;
4. identify action as phase and instability time as amplitude;
5. retain an explicit negative Hilbert--Pólya verdict unless a separate
   arithmetic/operator mechanism is later proved.

## Current status

No experiment code or result has been added, and no theorem is marked proved.
After an expanded external literature audit, this quantum route is deferred:
Weickert's spectral work and Shudo--Ikeda's horseshoe-regime quantum Hénon
analysis create a serious novelty risk. The only authorized next action here is
the G0 full-text comparison. R000 and all later runs remain blocked.

Historical scheduling assigned `next_paper_henon_ruelle_operator/` to N+1 and
this package to N+2. That ordering is superseded. This package is now HCS-C09
and can compete only after G0 and the operator/cutoff gates pass.
