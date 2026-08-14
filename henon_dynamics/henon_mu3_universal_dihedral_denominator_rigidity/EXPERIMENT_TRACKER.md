# HCS-C54 exact experiment tracker

| Run ID | Milestone | Purpose | Exact object | Priority | Status | Notes |
|---|---|---|---|---|---|---|
| C54-R001 | M0 | ideal-to-equation-line lemma | graded ideal | MUST | DONE-MATH | pure-cube comparison and domain argument |
| C54-R002 | M1 | symbolic closure parity | edge recurrence (A.1) | MUST | DONE-MATH | closing preimage must have odd index |
| C54-R003 | M1 | universal finite controls | rows \(2\le n\le64\) | MUST | RC-PASS | control only, not proof |
| C54-R004 | M1 | independent small-row brute force | rows \(2,3,4\) | MUST | RC-PASS | independent enumeration path passed |
| C54-R005 | M1 | generator presentation | \(r,s\), order \(3n\) | MUST | DONE-MATH | compare presentation bound with exhaustive count |
| C54-R006 | M2 | semilinear transport | \(\delta(r),\delta(s)\) | MUST | DONE-MATH | exact formulas frozen |
| C54-R007 | M2 | fixed rational elements | rows \(2\le n\le256\) | MUST | RC-PASS | immutable project-local replay |
| C54-R008 | M2 | Reynolds/transfer distinction | \(1/(6n)\) versus \(1/2\) | MUST | DONE-MATH | all geometric graphs included |
| C54-R009 | M3 | rank arithmetic | \(e_n,o_n\) and \(n\mid24\) | MUST | DONE-MATH | separate weights before ranks |
| C54-R010 | M3 | divisor table | divisors of 24 | MUST | RC-PASS | survivors exactly `[2,4]` |
| C54-R011 | M3 | range mutation guard | \(2\le n\le512\) | MUST | RC-PASS | immutable project-local replay |
| C54-R012 | M3 | total-rank negative control | \(n=3\), scaled rank 84 | MUST | RC-PASS | checker rejects this proof route |
| C54-R013 | M3 | complete-factor converse | direct copies for \(n=2,4\) | MUST | DONE-MATH | matches all power traces |
| C54-R014 | M4 | exact Cayley quotient | 27 monomials / 7 relations | MUST | RC-PASS | quotient dimension 20 |
| C54-R015 | M4 | group-action consistency | all \(G_3\) matrices | MUST | RC-PASS | relation images and group law pass |
| C54-R016 | M4 | residue orientation | \(\det M_g/\det A_g\) | MUST | RC-PASS | omission/inversion mutations rejected |
| C54-R017 | M4 | two-rail characters | \(\mathsf E_3,\mathsf O_3\) | MUST | RC-PASS | trace vectors and multiplicities pass |
| C54-R018 | M4 | coefficient orbit blocks | \(U_1,U_2,U_4\) | MUST | RC-PASS | block pair remains \((3,4)\) |
| C54-R019 | M4 | virtual kernel caveat | \(\mathbf1-\chi_{K/\mathbf Q}\) | MUST | DONE-MATH | nonzero over \(\mathbf Q\), restriction and rank zero |
| C54-R020 | M4 | scope assertions | exclusions | MUST | RC-PASS | no global/inert root or all-\(n\) motive |
| C54-R021 | M5 | mutation suite | semantic fields | MUST | RC-PASS | 93/93 unit tests; targeted mutations and 198-leaf rebound sweep included |
| C54-R022 | M5 | rollback-atomic local promotion | injected failure after stages 1, 2, 3, 4 | MUST | RC-PASS | rollback and exception safety; no power-loss claim |
| C54-R023 | M5 | duplicate/unknown JSON keys | certificate envelope | MUST | RC-PASS | fail closed |
| C54-R024 | M5 | deterministic default runner | canonical certificate | MUST | RC-PASS | byte-for-byte immutable replay |
| C54-R025 | M5 | code/results manifest | release-candidate artifacts | MUST | RC-PASS | persistent 11-entry manifest hash locked; both manifests excluded; 44-entry full inventory includes it |
| C54-R026 | M5 | manuscript compile audit | LaTeX/PDF | MUST | DOCS-FINAL-PASS | 14-page clean build; PDF and compilation-report digests frozen |
