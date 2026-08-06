# Experiment Tracker

| Run ID | Milestone | Purpose | System / variant | Split | Metrics | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| R000 | M0 | freeze protocol | all | all | source-lock completeness | MUST | DONE | frozen before periods 13--20 were generated |
| R001 | M0 | exact clock triage | unit/action/instability clocks | analytic | positivity, lattice status | MUST | DONE | exact action witness and multiplier-degree proof |
| R002 | M0 | implementation sanity | primitive product vs trace recursion | development | coefficient discrepancy | MUST | DONE | two implementations plus seven unit tests |
| R010 | M1 | development catalogue | \(H_6\) | periods 1--8 | counts, residuals, multipliers | MUST | DONE | 17 primitive cycles; exact symbolic counts |
| R011 | M1 | training root census | \(\kappa=0,1\) | cutoffs 7,8 | roots, numerical winding | MUST | DONE | 39 untwisted and 43 twisted tracked roots frozen |
| R020 | M2 | validation catalogue | \(H_6\) | periods 9--12 | prior bridge, residuals | MUST | DONE | 79/79 prior words matched |
| R021 | M2 | validation roots | \(\kappa=0,1\) | cutoffs 10,12 | drift, retention, counts | MUST | DONE | both sectors retain 100%; frozen gates pass |
| R030 | M3 | sealed catalogue | \(H_6\) | periods 13--16 | counts, residuals | MUST | DONE | 402 total primitive cycles |
| R031 | M3 | sealed roots | \(\kappa=0,1\) | cutoffs 14,16 | drift, retention, counts | MUST | DONE | both sectors retain 100%; frozen gates pass |
| R040 | M4 | high-cutoff robustness | \(H_6\) | periods 17--20 | drift, counts | MUST | DONE | 2,170 cycles; 43 roots per sector at cutoff 20 |
| R041 | M4 | clock/control panel | shuffled/random/constant | through 16 | control margins | MUST | DONE | valid controls and sampler failures all retained |
| R042 | M4 | neighbor controls | \(a=5.9,6.1\) | through 16 | word convergence, root drift | MUST | DONE | parameter-correct contraction bounds; numerical only |
| R050 | M5 | independent checker | persisted artifacts | all | hashes, schema, recomputation | MUST | DONE | 38/38 standalone checks pass |
| R060 | M5 | Route-A evaluation | final candidate | all | A1--A4 tuple | MUST | DONE | exploratory; Route B unauthorized |
| R070 | M5 | documentation | note, README, manifest | all | compile and handoff | MUST | DONE | 14-page PDF; repository handoff prepared |
