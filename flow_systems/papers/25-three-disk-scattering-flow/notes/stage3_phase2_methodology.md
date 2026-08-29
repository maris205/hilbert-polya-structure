contract_role: methodology
## Dimension Scores

### D1: methodology_rigor
score: warn
trigger: "The methods are broadly suitable, but important reporting, robustness, or reproducibility details are incomplete enough to reduce confidence without invalidating the core analysis."

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: pass

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

The methodology is appropriately split into an exact theoretical argument and a bounded computational replay. The noncohomology and scalar-nontransfer conclusions follow from two analytically derived periodic means, so they do not depend on the finite orbit solver. The numerical package then checks census completeness at the declared cutoff, retains difficult cases, and quantifies the scalar-clock mismatch. This supports D3. D1 is warned only because the reproducibility provenance is not yet fully self-contained; the identified gaps do not invalidate the analytic result or the frozen finite replay.

The symbolic control remains `(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)` with `ROUTE_A_REJECTED`. Those A1/A2 credits remain confined to the unit-roof symbolic object. The physical flow remains unassigned, no symbolic credit is transferred, and no Route B, operator construction, or spectral realization is supplied.

### S1: Exact two-witness design isolates the clock obstruction
The period-two and period-three mean-flight formulas yield a positive gap and are used only through the necessary periodic-sum implication for constant cohomology. The scalar-transfer theorem then preserves owner and repetition labels explicitly, while the minimax corollary states the exact scope of the approximation lower bound.

**Evidence Anchor**: equation: manuscript.tex, Propositions `prop:t2` and `prop:t3`, Corollary `cor:gap`, Theorems `thm:noncohom` and `thm:nontransfer`, and Corollary `cor:minimax`

### S2: Symbolic census and physical replay denominators are explicit
Exact Möbius counts establish 747 oriented primitive cyclic owners through length twelve for the three-symbol no-repeat convention. The locked physical ledger contains each owner once at each of three geometries, and the replay preserves all 2,241 rows with exactly three matches and 744 disagreements per geometry.

**Evidence Anchor**: dataset: results/round6_symbolic_owner_counts.csv and results/round8_roof_nontransfer_summary.json, complete declared populations

### S3: Numerical validation retains conditioned rows instead of selecting them away
All 2,241 rows pass the high-precision direct return-map checks; 2,202 use direct map refinement and 39 use the separately recorded stationarity fallback. The fallback rows remain subject to the same residual gates and remain in the replay, which closes a plausible selection-bias route at the finite cutoff while correctly stopping short of interval certification.

**Evidence Anchor**: dataset: results/round3_stability_metrics.json and results/round4_fallback_audit.csv, refinement-method and failure-tier records

### S4: Typed route ownership is preserved throughout the experiment chain
The frozen Round-8 contract and receipt keep the symbolic tuple owned by the unit-roof calibrator, leave the physical-flow tuple unassigned, forbid symbolic-to-physical credit transfer, and keep Route B closed. The manuscript repeats rather than enlarges that boundary.

**Evidence Anchor**: dataset: experiments/round8_roof_nontransfer_freeze.json, `route_boundary` and `forbidden_inputs` records

### W1: The computational environment is recorded but not reproducibly pinned
Round 2 records NumPy and SciPy versions, Round 3 records Python and mpmath versions, and the receipts establish byte identity only in the same environment. The supplied reproduction scripts rely on ambient installations and no paper-specific lockfile, container digest, or complete environment manifest is supplied. Add a machine-readable dependency lock or container specification and document the platform needed to reproduce the high-precision and compiled numerical paths.

**Severity**: Minor
**Evidence Anchor**: absence: Round-2--8 computational package — expected a pinned Python, NumPy, SciPy, mpmath, and platform environment; checked source programs, tests, validation notes, receipts, and reproduction scripts
**Confidence**: 5 — direct inspection of the complete named computational package

### W2: The manuscript points readers to a stale bibliography hash
The data-and-code statement says that artifact hashes are recorded in `paper/stage2_manuscript_audit.md`, but that audit lists `references.bib` as `acec8403...`, whereas the current frozen file and Stage-2.5 integrity report use `de776cc0...`. Update the named audit or point readers to the current integrity manifest so the advertised verification path does not fail on an unchanged frozen submission.

**Severity**: Minor
**Evidence Anchor**: dataset: paper/stage2_manuscript_audit.md, Deliverables and integrity table, compared with notes/stage2_5_integrity_report.md, Outcome table
**Confidence**: 5 — direct SHA-256 comparison of the allowed frozen files

### W3: Early-round receipts do not fully bind the source and tests they summarize
Rounds 6--8 bind source, tests, freezes, reproduction scripts, outputs, and validation records. By contrast, the Round-4 and Round-5 receipts report test counts and result hashes without source/test hashes, while the Round-2 and Round-3 receipts bind the main script but not the corresponding tests. Extend the receipt schema retrospectively or provide one frozen manifest that binds every Round-2--8 source, test, input, output, and command.

**Severity**: Minor
**Evidence Anchor**: dataset: experiments/round2_receipt.json through experiments/round5_reproducibility_receipt.json, source/test binding fields
**Confidence**: 5 — receipt-field and current-file hash audit

## Arithmetic Receipts
no_recomputable_statistics: The manuscript reports exact combinatorial and orbit counts, geometry ratios, deterministic replay tallies, and numerical residuals, but no t, z, F, chi-square/p, discrete-scale mean/SD, or invertible df-to-N statistic covered by the bounded procedures.
