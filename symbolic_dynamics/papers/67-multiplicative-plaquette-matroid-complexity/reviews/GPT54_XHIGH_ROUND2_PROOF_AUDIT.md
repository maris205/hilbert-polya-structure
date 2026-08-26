# GPT-5.4 XHigh Round 2 Proof Audit

## Provenance

- Reviewer role: official second-round hostile mathematical reviewer
- Paper: `P67`
- Scope: `papers/67-multiplicative-plaquette-matroid-complexity`
- Model provenance: `gpt-5.4 xhigh`
- Date: `2026-08-25 UTC`

I read the complete package in this directory, with special attention to `main.tex`, all manuscript section files, `PROOF_PACKAGE.md`, `CONTROL_RESULTS.md`, `reviews/GPT54_XHIGH_ROUND1_HOSTILE_REVIEW.md`, and `reviews/GPT54_XHIGH_ROUND1_RESOLUTION.md`. I also checked the supporting ledgers and QA artifacts, including `CLAIMS_EVIDENCE.md`, `ARGUMENT_BLUEPRINT.md`, `NARRATIVE_REPORT.md`, `PAPER_IMPROVEMENT_LOG.md`, `FINAL_QA.md`, `PAPER_IMPROVEMENT_STATE.json`, `SHA256SUMS`, `qa/final_text.txt`, `qa/final_pdfinfo.txt`, `code/verify_plaquette_matroid.py`, and the frozen control outputs.

I independently rederived the theorem package from the current manuscript and proof package rather than trusting Round 1.

I also ran the non-writing checks

```sh
python3 papers/67-multiplicative-plaquette-matroid-complexity/code/verify_plaquette_matroid.py
sha256sum papers/67-multiplicative-plaquette-matroid-complexity/main*.pdf
pdftotext papers/67-multiplicative-plaquette-matroid-complexity/main.pdf -
pdfinfo papers/67-multiplicative-plaquette-matroid-complexity/main.pdf
```

The deterministic control script still ends in `ALL CHECKS PASS`. The code and frozen control-output hashes match the values claimed in `CONTROL_RESULTS.md`.

## Verdict

**Theorem package: PASS.**

**Current release-package integrity: FAIL.**

I found no open theorem-level mathematical defect after hostile rederivation. The revised claims on root uniqueness, global parametrization, arbitrary finite projection rank, cycle completeness in all characteristics, graphic-matroid equivalence, Haar total correlation and joint-independence, prefix and rectangle laws, and one-edge updates all survive.

However, the current package is not internally synchronized as a frozen release artifact. The present `main.pdf` is the post-fix official Round-1 PDF, while several package files still claim that the final artifact is the older `main_round2.pdf`. That is a real release-blocking integrity defect.

**EXTERNAL RELEASE HOLD.**

## Severity-Ranked Issue List

### CRITICAL

None.

### MAJOR

#### M1. The frozen final-PDF / hash / QA trail is false for the current package.

Direct verification gives the following PDF identities and hashes:

- `main_round2.pdf` = `7bf54d3b56530decc051f56cfedc38684d432fca8c73474347d2ab33546bda7d`
- `main_pre_gpt54_round1.pdf` = `7bf54d3b56530decc051f56cfedc38684d432fca8c73474347d2ab33546bda7d`
- `main.pdf` = `48c3688f29062934ceb81f0b2077555b24ea23716e5224bd28ef5af7ae84729e`
- `main_gpt54_round1.pdf` = `48c3688f29062934ceb81f0b2077555b24ea23716e5224bd28ef5af7ae84729e`

So `main.pdf` is **not** byte-identical to `main_round2.pdf`; it is byte-identical to `main_gpt54_round1.pdf`.

But the package still asserts the obsolete round-2-final identity:

- `FINAL_QA.md:87-90` says Round 2 and final both hash to `7bf54...` and that `main.pdf` is byte-identical to `main_round2.pdf`.
- `PAPER_IMPROVEMENT_LOG.md:95-98` records the same obsolete final identity and hash.
- `SHA256SUMS:35-38` still assigns `7bf54...` to both `./main.pdf` and `./main_round2.pdf`.

The stored QA receipts are also stale relative to the actual current `main.pdf`:

- `qa/final_text.txt:95` still contains the old leaked token `qquadn`, while a live `pdftotext main.pdf -` no longer does.
- `qa/final_pdfinfo.txt:18` still reports file size `405467 bytes`, while live `pdfinfo main.pdf` reports `405543 bytes`.
- `FINAL_QA.md:73` repeats the stale `405,467 bytes` size.

Consequence: the current mathematical PDF appears to contain the official Round-1 integrity repairs, but the package's own freeze and QA story is no longer trustworthy as written. That blocks release certification.

### MINOR

No separate theorem-level minor issue remains beyond the stale-package-integrity problem above.

## Verification of the Three Round-1 Defects

I checked the three official Round-1 items directly rather than accepting the resolution file on trust.

1. **Evaluation-map display typo: repaired in source and current PDF.**
   - Source now reads correctly at `sections/1_introduction.tex:60`.
   - Live `pdftotext main.pdf -` no longer shows the leaked `qquad` token.
   - The stale `qa/final_text.txt` still shows it, but that is part of M1, not a live manuscript defect.

2. **Undefined `V_r` in the geometry table: repaired.**
   - `sections/5_rectangles.tex:116` now uses the defined expression `\sum_r(|I_r|+|J_r|-c_r)`.
   - The corresponding current PDF text matches the repaired formula.

3. **Malformed C9 row in the claims/evidence ledger: repaired.**
   - `CLAIMS_EVIDENCE.md:13` now uses a semantically valid evidence cell:
     `entropy additivity together with graphic-matroid acyclicity`.

Therefore, the three Round-1 defects are genuinely repaired in the live theorem package. The new open issue is the stale release trail created after those repairs.

## Theorem-by-Theorem Rederivation

### 1. Root uniqueness over all finite-field instances: PASS

This step is arithmetic, not field-dependent. For any `n`, let `i` be maximal with `a^i | n` and `j` maximal with `b^j | n`. Coprimality gives `a^i b^j | n`, so `n = r a^i b^j`. If `a | r`, then `a^(i+1) | n`; similarly for `b`. Conversely, in any representation with `a \nmid r` and `b \nmid r`, Euclid's lemma forces `i` and `j` to be the maximal whole-power exponents. This remains valid for composite coprime multipliers such as `(3,4)`, `(4,9)`, and `(6,35)`.

### 2. Global parametrization and free-axis homeomorphism: PASS

On each root component, writing `y_{i,j} = x_{r a^i b^j}` turns the rule into
`y_{i,j} - y_{i+1,j} - y_{i,j+1} + y_{i+1,j+1} = 0`. Rearranging gives horizontal increments independent of `j`; telescoping yields
`y_{i,j} = y_{i,0} + y_{0,j} - y_{0,0}`. Hence every component is determined by its two axes, with the origin counted once.

Under coprimality, `ab | r a^i b^j` iff `i,j >= 1`, so the arithmetic free coordinates are exactly `B = {n : ab \nmid n}`. The inverse
`x_{r a^i b^j} = z_{r a^i} + z_{r b^j} - z_r`
uses only axis coordinates and is coordinatewise finite, so the algebraic and topological inverse arguments are complete.

### 3. Arbitrary finite projection rank and global compatibility: PASS

For a fixed root `r`, a finite shape `E_r(F)` is represented by the potential map
`Phi_r(u,v)_{(i,j)} = u_i + v_j`.
Its image is exactly the finite restriction of global solutions because used potentials extend arbitrarily to unused row and column indices, after which the global formula `y_{i,j} = u_i + v_j` defines a full component solution.

On each connected component of `G_r(F)`, the kernel is one-dimensional: `u_i = t` on row vertices and `v_j = -t` on column vertices. Therefore
`rank Phi_r = |I_r| + |J_r| - c_r`.
Summing over roots gives the projection-dimension formula
`d(F) = sum_r (|I_r| + |J_r| - c_r)`.

### 4. Cycle completeness in every characteristic: PASS

After the sign change `v_j = -w_j`, the edge labels are the graph coboundary values `u_i - w_j`. Telescoping around a cycle gives the alternating relation
`sum_{ell=1}^k (z_{i_ell,j_ell} - z_{i_{ell+1},j_ell}) = 0`.
In characteristic two the minus signs collapse to plus signs, but the same field identity remains valid.

Sufficiency follows from spanning-forest integration: choose a base vertex in each tree, assign potential zero there, integrate along unique forest paths, then use each nonforest edge's fundamental-cycle equation to show the integrated endpoint values reproduce its label. No hidden higher-order compatibility survives beyond the cycle space.

### 5. Graphic-matroid equivalence: PASS

With edge rows and vertex-potential columns, the finite matrix representing the coordinate maps is the transpose of an oriented vertex-edge incidence matrix after a sign change on one vertex class. Its column matroid is therefore the graphic matroid of `G_r(F)`, and graphic matroids are representable over every field, including characteristic two. Distinct roots yield block-diagonal matrices, hence a direct sum of graphic matroids.
The manuscript's corresponding argument is correct; no field-dependent or graphic/cographic ambiguity remains.

### 6. Haar total correlation and joint-independence characterization: PASS

For finite `F`, the projection `X_{a,b} -> proj_F(X_{a,b})` is a continuous surjective homomorphism from a compact group onto a finite group, so Haar measure pushes forward to normalized counting measure. Hence
`H(Z_F) = d(F) log q`.

Every singleton coordinate projection is all of `F_q`, so each marginal entropy is `log q`. Therefore
`TC(Z_F) = (|F| - d(F)) log q = beta(F) log q`.
Joint independence is equivalent to equality between joint entropy and the sum of marginals, hence to `beta(F) = 0`, i.e. every root-wise incidence graph is a forest.

For pairwise independence, two distinct arithmetic coordinates correspond to two distinct edges in simple bipartite graphs, possibly on different roots. A two-edge simple graph is always a forest, so every distinct pair is independent.

### 7. Prefix law: PASS

For `F = [L]`, the free coordinates in the prefix are exactly `B cap [L]`, of cardinality `L - floor(L/(ab))`. If `n = r a^i b^j <= L`, then the inverse formula uses only `r a^i`, `r b^j`, and `r`, each at most `n`, hence at most `L`. So the prefix is determined by `B cap [L]`.

Conversely, any assignment on `B cap [L]` extends to all of `B`, then globally to a point of `X_{a,b}`. This gives the exact count
`|proj_[L](X_{a,b})| = q^(L - floor(L/(ab)))`.

The triangular pivot lemma is now correctly only a local row-rank cross-check. I found no surviving logical overreach there.

### 8. Rectangle law: PASS

For `Q_r(M,N) = {r a^i b^j : 0 <= i < M, 0 <= j < N}`, the incidence graph is `K_{M,N}`. Its graphic rank is `M + N - 1`, and its cycle rank is
`MN - (M + N) + 1 = (M - 1)(N - 1)`.
So the counting and Haar formulas follow immediately:

- `|proj_{Q_r(M,N)}(X_{a,b})| = q^(M + N - 1)`
- `TC(Z_{Q_r(M,N)}) = (M - 1)(N - 1) log q`

No hidden dependence or characteristic issue appears here.

### 9. One-edge update statements: PASS

Deleting a cycle edge in a graphic matroid preserves rank and lowers nullity by one. Deleting a bridge lowers rank by one and preserves nullity. Since `beta(F) = |F| - d(F)`, the manuscript's deletion formulas follow exactly.

For addition, an edge whose endpoints are already connected is dependent, so rank is preserved and nullity rises by one. Any other new edge raises rank by one and preserves nullity. This includes the cases where the new edge introduces a new vertex or an entirely new root component.

The corrected Round-1 defect is genuinely repaired.

## Explicit Pass / Fail Disposition

- **Root uniqueness:** PASS
- **Global free-axis parametrization:** PASS
- **Arbitrary finite projection rank:** PASS
- **Cycle completeness:** PASS
- **Graphic-matroid equivalence:** PASS
- **Haar entropy / total correlation / forest independence:** PASS
- **Prefix law:** PASS
- **Rectangle law:** PASS
- **One-edge update law:** PASS
- **Three Round-1 defects:** PASS
- **Current frozen release-package consistency:** FAIL

No substantive open mathematical issue remains in the theorem package. The open issue is release-package integrity, not proof correctness.

## Remaining Release Gates

1. Decide which PDF is the actual frozen final artifact.
   - Either the package final is `main_round2.pdf` / `main_pre_gpt54_round1.pdf` with hash `7bf54...`,
   - or it is `main.pdf` / `main_gpt54_round1.pdf` with hash `48c368...`.
   The package currently asserts both incompatible stories.

2. Regenerate or synchronize all release metadata against the chosen final PDF.
   - At minimum: `SHA256SUMS`, `FINAL_QA.md`, `PAPER_IMPROVEMENT_LOG.md`, `qa/final_text.txt`, and `qa/final_pdfinfo.txt`.

3. Recheck the artifact trail after synchronization.
   - Hash equality claims
   - extracted-text receipt
   - `pdfinfo` receipt
   - any "byte-identical" statements across round artifacts

4. Keep the already declared specialist exact-neighbor search gate.
   - The bounded-search posture remains correct, but it is still a release gate.

## Final Status

Mathematics: **PASS**.

Current package freeze integrity: **FAIL**.

**EXTERNAL RELEASE HOLD.**
