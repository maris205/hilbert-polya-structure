# Experiment Tracker

All rows are `TODO_NOT_AUTHORIZED`.  This tracker records a prospective exact
audit only.  No Paper-10 code, candidate execution, result, or deployment
authority exists at source-design time.

| Run ID | Milestone | Purpose | System / variant | Frozen input | Exact metrics | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| R000 | M0 | strict source-lock parse | final seven-file package | six bound design files plus lock | JSON parse, duplicate keys, hashes | MUST | TODO_NOT_AUTHORIZED | independent review must bind final lock SHA |
| R001 | M0 | upstream Paper-9 terminal binding | read-only upstream | named Paper-9 terminal artifacts | all hashes reproduce | MUST | TODO_NOT_AUTHORIZED | no upstream edit or rerun |
| R002 | M0 | fixed-object schema check | candidate configuration | one matrix; ordered tuple `(2,3,5,7,11,4,6,9,10)` | exact equality; no alternate list | MUST | TODO_NOT_AUTHORIZED | reject hidden scan/generator |
| R003 | M0 | independent code review | future immutable code tree | source lock plus code-tree hash | tests, policy, deterministic serialization | MUST | TODO_NOT_AUTHORIZED | explicit `DEPLOYMENT_PASS` required |
| R010 | M1 | cyclic basis check | direct matrix algebra | all nine fixed moduli | `det[e1,Ae1]=1` | MUST | TODO_NOT_AUTHORIZED | exact integer residues only |
| R011 | M1 | commutant equality | brute matrices vs `aI+bA` | all nine fixed moduli | exact set equality | MUST | TODO_NOT_AUTHORIZED | max ambient size $11^4$ |
| R012 | M1 | algebra-unit equality | `R_q[A]^times` vs GL commutant | all nine fixed moduli | exact set equality, sizes | MUST | TODO_NOT_AUTHORIZED | determinant-unit criterion |
| R013 | M1 | cyclic-locus equality | vector determinant test | all nine fixed moduli | exact vector set and size | MUST | TODO_NOT_AUTHORIZED | no shell omission |
| R014 | M1 | torsor axioms | action `U*v` | all nine fixed moduli | closure, free, transitive, bijective | MUST | TODO_NOT_AUTHORIZED | four booleans per modulus |
| R015 | M1 | exact additive-order inclusion | independent order routine | `CV_q` at all fixed moduli | every order equals $q$ | MUST | TODO_NOT_AUTHORIZED | validates `CV_q subset E_q` |
| R016 | M1 | determinant/norm equality | matrix det vs quadratic polynomial | every $a,b$ at fixed moduli | exact equality | MUST | TODO_NOT_AUTHORIZED | `a^2+3ab+b^2` |
| R017 | M1 | expected-ledger unit tests | development-only assertions | frozen table | all integers match | MUST | TODO_NOT_AUTHORIZED | cannot change table after failure |
| R018 | M1 | determinism test | two isolated development invocations | same exact inputs | byte-identical outputs | MUST | TODO_NOT_AUTHORIZED | not the registered science run |
| R019 | M1 | forbidden API static audit | future code tree | no inputs | no network, RNG, float, prime/zero API | MUST | TODO_NOT_AUTHORIZED | code reviewer owns decision |
| R020 | M2 | freeze execution tree | implementation package | reviewed code | explicit tree hash | MUST | TODO_NOT_AUTHORIZED | no later code drift |
| R021 | M2 | freeze registered claim | claim manifest | source/code/review hashes | exact bindings and one-run policy | MUST | TODO_NOT_AUTHORIZED | signed by future pipeline only |
| R022 | M2 | clean environment preflight | isolated local runtime | network disabled | dependency and policy PASS | MUST | TODO_NOT_AUTHORIZED | no external data mount |
| R023 | M2 | pre-execution full tests | reviewed code tree | fixed inputs only | all tests pass | MUST | TODO_NOT_AUTHORIZED | JUnit/provenance artifact |
| R024 | M2 | deployment gate | independent reviewer | all M0--M2 artifacts | `DEPLOYMENT_PASS` | MUST | TODO_NOT_AUTHORIZED | only authorization for R100 |
| R100 | M3 | sole registered exact audit | frozen candidate | exactly nine moduli | all blocks B2--B5 and artifact contract | MUST | TODO_NOT_AUTHORIZED | run exactly once; seedless |
| R110 | M4 | raw result schema/hash review | read-only result | R100 artifact | parse, hashes, inventory | MUST | TODO_NOT_AUTHORIZED | no candidate rerun |
| R111 | M4 | torsor result review | independent recomputation from records | nine rows | all C1 booleans and counts | MUST | TODO_NOT_AUTHORIZED | finite control only |
| R112 | M4 | GL/Sp quotient review | independent set/profile check | nine rows | quotient counts, norm fibers | MUST | TODO_NOT_AUTHORIZED | check $2$/$5$ boundaries |
| R113 | M4 | quotient-dynamics review | transition records | all quotient sets | every induced action identity | MUST | TODO_NOT_AUTHORIZED | native period is one |
| R114 | M4 | full-shell/reversing review | shell records | nine shells; five prime reversing groups | strata, discard, no mixing | MUST | TODO_NOT_AUTHORIZED | three symmetry layers kept distinct; no new modulus |
| R115 | M4 | composite proves-too-much review | composite rows only | `(4,6,9,10)` | every full quotient one; external label true | MUST | TODO_NOT_AUTHORIZED | cannot infer prime specificity |
| R116 | M4 | forbidden-data review | provenance counters | complete run record | every counter zero | MUST | TODO_NOT_AUTHORIZED | any nonzero value is integrity FAIL |
| R117 | M4 | terminal decision review | machine classification | full result | exact certificate and Route-B closure | MUST | TODO_NOT_AUTHORIZED | no novelty upgrade |
| R118 | M4 | independent result manifest | read-only artifact tree | hashes and inventory | strict manifest PASS | MUST | TODO_NOT_AUTHORIZED | no scientific write |
| R119 | M4 | human validation report | theorem/result comparison | final reviewed result | scoped PASS/FAIL | MUST | TODO_NOT_AUTHORIZED | must say finite run is not proof |
| R120 | M5 | manuscript handoff gate | reviewed source and result | all terminal hashes | writing authorization only | MUST | TODO_NOT_AUTHORIZED | no new experiment |

## Locked expected row values

The order of rows is fixed as

`2, 3, 5, 7, 11, 4, 6, 9, 10`.

- `exact_shell_size`: `3, 8, 24, 48, 120, 12, 24, 72, 72`.
- `cyclic_locus_size`: `3, 8, 20, 48, 100, 12, 24, 72, 60`.
- `discard_size`: `0, 0, 4, 0, 20, 0, 0, 0, 12`.
- `full_centralizer_size`: `3, 8, 20, 48, 100, 12, 24, 72, 60`.
- `symplectic_centralizer_size`: `3, 4, 10, 8, 10, 6, 12, 12, 30`.
- `A_order`: `3, 4, 10, 8, 5, 3, 12, 12, 30`.
- `cyclic_A_orbit_count`: `1, 2, 2, 6, 20, 4, 2, 6, 2`.
- `full_centralizer_CV_quotient_count`: all nine values are `1`.
- `symplectic_centralizer_CV_quotient_count`:
  `1, 2, 2, 6, 10, 2, 2, 6, 2`.
- `full_centralizer_shell_orbit_count`:
  `1, 1, 2, 1, 3, 1, 1, 1, 2`.
- `symplectic_centralizer_shell_orbit_count`:
  `1, 2, 4, 6, 12, 2, 2, 6, 4`.
- `prime_reversing_group_shell_orbit_count` at `2,3,5,7,11`:
  `1, 1, 2, 1, 2`.
- `induced_A_action_on_full_quotient`: `IDENTITY` for every row.
- `induced_A_action_on_symplectic_quotient`: `IDENTITY` for every row.

## Stop rules

1. Any mismatch in R010--R024 blocks deployment; repair must occur before the
   code tree and registered claim are frozen.
2. Any mismatch in R100 is a registered scientific FAIL.  Do not add or
   replace a modulus, switch centralizer ambient groups, alter the cyclic
   criterion, or rerun the registered candidate.
3. Any forbidden-data or network counter above zero is a result-integrity
   FAIL regardless of mathematical counts.
4. A PASS cannot alter the low-novelty assessment or establish an all-$q$
   theorem; the proof package is the theorem authority.
5. A PASS cannot open A2--A4, Route B, a prime/zero comparison,
   transfer/Fredholm construction, quantization, Hecke spectral study, or
   equivariant/stacky/twisted-sector route.
6. The only terminal machine disposition after a full PASS is
   `CENTRALIZER_CYCLIC_TORSOR_CERTIFIED /`
   `A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.
