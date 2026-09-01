# P28 pipeline state

Date: **2026-09-01**

Current controlling state: **PIPELINE COMPLETED / STAGE 5 COMPLETE / STAGE 6
SKIPPED**.  The scholar's exact content response `确认` authorized the
final format-only build.  The accepted Stage-4.5 Round-2 integrity result
remains `PASS` at 6/6 references, 9/9 citation contexts, 95/95 registered
claims, and 104/104 evidence tuples.  Two independent fixed-environment builds
produced the byte-identical 14-page final PDF, SHA-256
`be156f76fcf3f31ecdc2d8be5dde5ccf7aaf7f0b530c7dc8efc9b889e3633cc9`;
its `pdftotext -layout` stream is byte-identical to the accepted proof, and all
14 pages passed visual review.  The advisory package report is fresh, with
A1--A7 not applicable, B1--B5 not checked because no venue profile exists,
and C1--C2 passed.  All 17 fonts are embedded; 12 legacy Type-1 math fonts
retain the accepted proof's `uni=no` profile, so complete per-font ToUnicode
coverage is not claimed.  Canonical manuscript/body, bibliography, PDF,
result tree, the frozen unit-speed Bolza magnetic flow at `b=1/2`, subtype,
and Route records remain unchanged.  On 2026-09-01 UTC the scholar declined
optional Stage 6 with the exact response `跳过，继续下一批`; Stage 6 is therefore
`skipped`, the pipeline global state is `completed`, no Process Record was
generated, and no further ARS event is required.

| Item | Status |
|---|---|
| ARS Stage 1 | **COMPLETE / RESEARCH SPINE FROZEN** |
| ARS Stage 2 | **DRAFT COMPLETE** — full manuscript, bibliography, compiled PDF and manuscript audit delivered |
| ARS Stage 2.5 | **PASS AT MANDATORY CHECKPOINT** — 0 serious blockers; one non-blocking replay-order minor retained |
| ARS Stage 3 | **COMPLETE / HISTORICAL MINOR REVISION** — five Phase-1 and five Phase-2 cards, synthesis, provenance, and four-item non-ranking roadmap validated |
| ARS Stage 4 | **COMPLETE** — authorized four-item revision, evidence bundle, direct tests and clean preview complete |
| ARS Stage 3′ | **ROUND 2 COMPLETE / HISTORICAL MAJOR REVISION ENTRY** — 3 fully + 1 cannot verify; B3; checker PASS; exact Stage-4′ authority was subsequently granted |
| ARS Stage 4′ | **COMPLETE WITHIN AUTHORIZED SCOPE** — `REV-02` resolved by 1 operation; 14/14 surfaces exact-once; 28/28 tests plus 24/24 replay; 14-page clean preview; canonical content/results/Route frozen |
| ARS Stage 4.5 | **PASS / MANDATORY CHECKPOINT COMPLETE** — fresh Mode-2 audit: refs 6/6; contexts 9/9; claims 95/95; evidence tuples 104/104 |
| ARS Stage 5 | **COMPLETE / FULL CHECKPOINT** — scholar-confirmed format-only finalization; 2/2 byte-identical builds; 14-page final PDF; fresh advisory package report |
| ARS Stage 6 | **SKIPPED / PIPELINE COMPLETED** — scholar declined the optional process summary; no Process Record generated; no next required event |
| Continuous-time object | **FROZEN** — unit-speed Bolza magnetic flow at `b=1/2` |
| Flux / base-bundle degrees | **`[PROVED]`** — `b=0,+1/2,-1/2` maps to `0,+1,-1`; negative field uses `L^*` |
| Global magnetic potential | **`[PROVED]`** — nonzero flux implies nonexact field |
| Phase owner | **`[PROVED]` / FROZEN** — line-bundle holonomy modulo `2 pi` |
| Semiclassical family | **FROZEN / NO ROUTE CREDIT** — `H_N=Δ^{L^N}` on `L²(Σ_B,L^N)`, `N→∞` |
| Operator dependence | **`[PROVED]`** — operator and Hilbert space change with `N` |
| Full all-`N` / arbitrary-twist trace regime | **`[OPEN]`** — no uniform energy-window theorem frozen |
| Full all-`N` / arbitrary-twist orbit ownership | **`[OPEN]` / `NOT_ESTABLISHED`** |
| Round-3 subtype | **`[MODELING_CHOICE]` / FROZEN** — source-compatible square root, even `N=2m` |
| Round-3 operator/window | **SOURCE BOUND** — `sqrt(Delta^(L^N)+N^2/4)`, center `(sqrt(5)/2)N`, `O(1)` transformed window |
| Round-3 classical shell | **`[PROVED]`** — principal Hamiltonian `sqrt(|p|^2+1/4)` at the frozen center gives `|p|=1` |
| Round-3 clock map | **`[PROVED]`** — `T_trace=(sqrt(5)/2)T_physical`; the physical clock remains unit speed |
| Round-3 source/project flow map | **`[PROVED]`** — `q=2p`, pullback `omega_source=2 omega_project`, pullback `H_source=2 H_project` |
| Round-3 signed-field orbit ownership | **`[PROVED]` under frozen subtype** — source Theorem 3 for `+1/2`; antiunitary dual for `-1/2` |
| Full all-`N` / arbitrary-twist ownership | **`[OPEN]` / `NOT_ESTABLISHED`** |
| Round-3 contract validation | **PASS / REPRODUCIBLE** — 12 rows, 8/8 tests, two byte-identical runs, tree SHA-256 `a28bf68d0da5c34350224031428f18f325af0d11619df95f2509741475275f3d` |
| Round-4 Bolza group lock | **SOURCE LOCKED / REPLAY PASS** — four published opposite-side-pairing generators, exact polygon relator, 120-decimal residual `1.534e-117` |
| Round-4 primitive seed | **`[PROVED]` under frozen subtype** — four systolic inverse-paired primitive axis owners per field; `f_j` and `f_j^-1` remain nonconjugate facts but receive one axis-owner ID in this schema |
| Round-4 signed-`k` ledger | **EXECUTED / REPRODUCIBLE** — equation-(19) branches `k=+-1,+-2,+-3`; 24 branches per field, 48 rows total, zero orientation owner credit, 12/12 tests, two byte-identical builds, tree SHA-256 `b2387be3d4acc6485cd7f0e2d89eeaae9a36dace1ddf2d451d7f51ed3680bfd4` |
| Round-4 completeness | **INCOMPLETE BY DESIGN** — four explicit side-pairing primitives only; not a complete Bolza primitive or systolic spectrum |
| Round-4 arithmetic labels | **NONE** — no target data and no rational-prime/prime-ideal assignment |
| Round-5 finite census | **EXECUTED / REPRODUCIBLE** — complete matched marked-cyclic census for freely/cyclically reduced words at `L<=4` modulo rotation and inversion: 390 classes = 366 marked-primitive candidates + 24 powers |
| Round-5 exact equality audit | **PASS** — exact `Q(s,t,i)` generator/relator replay; zero PSL matrix collisions and zero equality-or-inverse collisions among the 390 canonical records |
| Round-5 primitivity gate | **`[PROVED]` for 44 records** — exact `abs(trace)<10+8sqrt(2)` gives `ell<2ell_B`; 322 marked-primitive records remain `NOT_ESTABLISHED` |
| Round-5 owner distinctness | **36 CREDITS PER FIELD / 8 WITHHELD** — credit at most one proved primitive per homology vector modulo sign; eight same-axis proved records receive no duplicate owner credit |
| Round-5 signed-`k` ledger | **EXECUTED / REPRODUCIBLE** — 36 owners per field, `k=+-1,+-2,+-3,+-4`, 576 rows, 48/48 Round-4 compatibility checks, zero orientation-owner fields |
| Round-5 reproducibility | **PASS** — 14/14 tests, two byte-identical builds, tree SHA-256 `1c8665ea55826e73c6aeb5f8cd6386a8d1020976d23004e1216d05e2f1e8a138` |
| Round-5 completeness boundary | **MARKED-CYCLIC ONLY** — full `Gamma`-conjugacy completeness is `NOT_ESTABLISHED`; equal exact trace squared never mints conjugacy credit |
| Non-arithmetic genus-2 control | **`[PROVED] / SOURCE PACKAGE + SYSTOLE READY`** — `NAZARENKO-EXP-OCTAGON-G2`, `(a,alpha)=(exp(-1/10),pi/4)`, is source locked and independently proved non-arithmetic; four side-pairing owners are primitive; Round 8 proves its exact systole and finite cutoff completeness; no comparison is claimed |
| Round-6 frozen-eight conjugacy closure | **`[PROVED] / PASS`** — eight explicit short words satisfy `x^-1*g*x=h` exactly in source-locked `SL(2)`; all eight historically withheld records are conjugate duplicates, with zero inverse fallbacks and zero new owner credits |
| Round-6 owner consequence | **UNCHANGED** — 44 primitivity-certified records resolve to 36 credited inverse-paired classes plus eight exact duplicate records; 36 owners per field and 72 field-owner pairs |
| Round-6 branch consequence | **BYTE-IDENTICAL REUSE** — the Round-5 576-row branch ledger remains canonical, SHA-256 `5f9cc50dfba3bb257a8a4f32c8bc5bd322a683788da4c9b900e9f8a5a62ee493` |
| Round-6 control source-package gate | **FAIL-CLOSED / NOT READY** — 0/6 required locked inputs present; geometry, matrices, non-arithmeticity, systole, cutoff, census, and comparison all remain false/not run |
| Round-6 reproducibility | **PASS** — 17/17 tests, two byte-identical builds, artifact-tree SHA-256 `098bfcac59f7fd332ddc022d2f59745f4e91450ade251024e9d6a12a6c82126b` |
| Round-6 bounded-proxy Route record | **EVALUATION ONLY / NO PROMOTION** — separate `L<=4` certified-owner proxy is conservatively typed `A0_WEAK / A1_WEAK / A2--A4 FAIL-NOT_TESTABLE`, overall `ROUTE_A_EXPLORATORY`; the main P28 tuple remains unassigned |
| Round-7 source audit | **COMPLETE / CLAIM BOUNDED** — eight records screened, four included and four excluded; all included sources have exact locators, access date `2026-08-28`, claim ownership, grade, and boundary |
| Round-7 six-item source gate | **PASS / 6 OF 6** — named closed genus-two surface; exact torsion-free cocompact Fuchsian side pairings; published presentation plus checked relator; primary/peer-reviewed locator; independent non-arithmeticity; four per-owner primitivity certificates |
| Round-7 exact matrix replay | **PASS** — four analytic `SU(1,1)` generators; determinant residual `1.314e-140`, `SU(1,1)` residual `1.050e-140`, relator residual `7.191e-139` at 140 decimal digits; the angle-sum replay is a formula-consistency check rather than an independent geometry proof |
| Round-7 non-arithmeticity | **`[PROVED]`** — `tr(g0)^2` is transcendental by exact trace algebra and Lindemann--Weierstrass; hence the square-subgroup trace `tr(g0^2)` violates Takeuchi's necessary algebraic trace-field condition |
| Round-7 primitive control owners | **`[PROVED]` FOR FOUR GENERATORS** — abelianization `Z^4` maps `g_j` to primitive basis vector `e_j`, excluding a proper-power representation; no systole or other-word credit |
| Round-7 execution boundary | **NOT RUN BEYOND SOURCE PACKAGE** — no common cutoff, control census, branch comparison, target data, arithmetic labels, determinant, A2, or Route B |
| Round-7 reproducibility | **PASS** — 22/22 tests, two byte-identical builds, core artifact SHA-256 `f1fbcc162907622e8f521dc08d56032afec7553810a9bbbcf3ba752728540386`, tree SHA-256 `a11917f6e9eab3bc48f1920b9727b0ec96a9c43c1f7ac13ab69984c005cfccef` |
| Round-8 exact group engine | **PASS / NO DECIMAL EQUALITY KEYS** — Gaussian-integer polynomial matrices in `u=exp(-1/10)`, exact `PSU(1,1)` denominator normal forms, four inverse-pair identities, and the published relator all reduce exactly; every proof sign uses rational Taylor intervals |
| Round-8 finite completeness | **`[PROVED]` THROUGH `Lambda=21/10`** — compact-polygon radius `D_F<3` converts every short conjugacy class to the exact identity-connected center sublevel component at `|alpha|^2<=20000`; 18,533 states are included and 108,616 distinct boundary states are rejected exactly |
| Round-8 control systole | **`[PROVED]`** — `sys=2 acosh(1/(2exp(-1/5)-1))=2.043026655880296...`; all 18,532 nonidentity finite states meet the lower bound and `g0*g3` is an exact equality/primitive witness |
| Round-8 common cutoff | **FROZEN / TARGET BLIND** — `Lambda_common=21/10`; chosen before traversal and before any branch outcome; neither surface census nor a magnetic comparison is run |
| Round-8 source audit | **3 INCLUDED / 3 EXCLUDED** — exact locators, access date `2026-08-28`, source grade, claim support, and explicit boundaries; contextual algorithms are not credited with the project-local theorem |
| Round-8 reproducibility | **PASS** — 24/24 tests, two byte-identical builds, core artifact SHA-256 `0a0ae16bbba5ed66958bc3714e91e038a8f80f3efc70224bfa5d9f87e48e6512`, tree SHA-256 `c30beebdd2e832d9375f55f1eab700868b7b967dfb5ee43fcecc0ba5f60919ac` |
| Round-8 execution boundary | **NO CENSUS OR COMPARISON** — target/arithmetic labels remain zero; control/Bolza census, owner dedup, magnetic comparison, determinant, A2, and Route B remain not run/false |
| Fixed degree-one candidate | `Δ^L` tracked separately; `FIXED_OPERATOR_HIGH_ENERGY_TRACE=OPEN` |
| Fixed-candidate orbit ownership | `FIXED_OPERATOR_MAGNETIC_ORBIT_OWNERSHIP=NOT_ESTABLISHED` |
| Bold hypothesis | **`[HEURISTIC]`** — arithmetic-specific phase cancellation |
| First controls | **FROZEN DESIGN** — degree `0,+1,-1`, dual-bundle field reversal, and non-arithmetic metric |
| Round-2 owner lemma | **`[PROVED]`** — changing bundles, duality, antiunitary reversal, domain, repetition, and no fixed-owner credit transfer |
| Round-2 owner ledger | **EXECUTED / REPLAY PASS** — 12 rows, `N=1,2,4,8`, 7/7 tests |
| Magnetic-orbit ledger | **BOUNDED OWNER SUBSET EXECUTED** — 36 safely distinct inverse-paired axes per field and theorem-derived signed-`k` period/action/stability branches; no trajectory integration or complete `Gamma` spectrum |
| Evidence tokens | `[PROVED]|[HEURISTIC]|[MODELING_CHOICE]|[OPEN]` |
| Paper-delivery stage | ARS Stage 5 complete / Route A early control-infrastructure layer |
| Formal Route-A tuple | UNASSIGNED |
| Route-B evaluation | NOT RUN |
| Route-B invocation allowed | `false` |
| Manuscript | **FROZEN STAGE-3 REVIEW TARGET** — 5,127 body words, 14 pages, 6/6 citation closure; no Phase-0 mutation |

Historical workflow checkpoint: Stage 3 review outputs were complete, and the
author still had to adjudicate every source row and authorize exact revision
blocks before any Stage-4 edit. The mechanical decision was `MINOR_REVISION`;
the later Stage 4 and Stage 3′ Round 2 states are recorded in the current-state
table above. No Route-A or Route-B mutation was authorized by the review itself.

Next scientific gate: the contracted non-arithmetic control passes 6/6, its exact systole
is proved, and the target-blind common cutoff `Lambda=21/10` is frozen.  Build
the matched Bolza/control geometric census at that unchanged cutoff, with
exact quotient-conjugacy, inverse-pair ownership, and primitivity deduplication,
before generating any magnetic comparison outcome.  This progress applies
only to the frozen signed-field even
subsequence; zero field, odd `N`, full all-`N`, arbitrary twists, and fixed
`Delta^L` remain open or `NOT_ESTABLISHED`.  The bounded-proxy evaluation is
not a promotion of the main candidate: its formal Route-A tuple remains
unassigned, A2 is not run, A4 has no credit, and Route B remains disallowed.
