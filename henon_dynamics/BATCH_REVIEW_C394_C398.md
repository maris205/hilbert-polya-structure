# C394–C398 batch review and release receipts

Date2026-09-05. Five complete source-theorem papers; no sixth authorized.
Frozen evidence baseline: `697518b6db90458f86f7916fbf397b8ad5ef2372`.
Evaluatorv0.2.0, SHA256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
Epoch1788566400; scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Release state

All five complete proofs, final PDFs and final file/hash audits have passed.
Every package's final write and subsequent complete nonwrite actually exited
successfully, including C394/C396 after the necessary gate repairs. All five
packages are frozen. This is the completed five-way release checkpoint.

Root's independent final static audit rehashed every payload and verified
exact physical membership, live evaluator bytes, source baseline, epoch,
literal-false flags and Route-B permission, main==round2, actual page count,
all PASS lane flags and no ignored payload paths. Result:
**233 payload files + five self-excluding manifests = 238 physical files;
five final PDFs total22 pages.** No package symlink or extra cache file exists.

## One independent complete problem per paper

| Paper | Complete source increment | Final pages | Three revision pages | Payload + manifest |
|---|---|---:|---|---|
| C394 | Joint nonlinear p-adic analytic time, exact orbit-closure isometry, complete minimal decomposition, all finite-quotient periods and finite/all algebraic hitting sets | 4 | 2/3/4 | 47+1 |
| C395 | Every BCZ Farey periodic layer and irrational exclusion, totient period, exact physical roof, all parabolic return cocycles and floor-wall/continuous-family boundary | 5 | 3/4/5 | 48+1 |
| C396 | Full finite-impedance PDE semigroup and nontransparent spectrum/Riesz basis; transparent empty spectrum, exact extinction, pseudospectra and operator-ideal boundary | 5 | 3/4/5 | 44+1 |
| C397 | Full Salem fixed groups/zeta, primitive and cumulative arcsine laws, trivial homoclinic group, symplectic reversal and cyclotomic degeneration | 4 | 3/3/4 | 47+1 |
| C398 | Complete Bessel spectrum/resolvent/determinant, bounded Weyl residual, heat/Schatten laws and no target counting under any permitted fixed normalization | 4 | 2/4/4 | 47+1 |

Three revisions are substantive versions of the same paper, not additional
papers. Equal page counts in two revisions do not imply identical content:
the checked text lengths increase and the PDF hashes differ.

## Actual executable evidence and boundaries

| Paper | Mathematical regression | Hostile gate and release tests |
|---|---|---|
| C394 | 56 finite levels,109876 residue points,2880 displacement rows,512 polynomial coefficients,1024 tail rows; independent checker66481; exact symbolic4592 | 64/64:50 repaired-hash +3 strict JSON +10 actual YAML write refusals +1 actual symlink write refusal; smoke3 and optimized12 |
| C395 | N=1..64,27833 full-cycle points/return matrices,55666 two-scale controls,320 repetitions,16 walls and128 fixed iterates; symbolic14 general identities +256 exact layers +65 ninety-digit controls | 50/50 hostile, including6 actual YAML write refusals; smoke3 and optimized12 |
| C396 | Independent7+588 exact and126+27+21 numerical rows; symbolic11, Rayleigh27, Volterra81, complex gauge81, singular12 | 62 distinct hostile cases/73 refusals:45 semantic +4 serialization +10 YAML through both entries +1 authority through both entries +2 physical write attacks; smoke3 and optimized12 |
| C397 | 120 fixed groups,1920 matrix cells,12 cyclotomic controls;7 symbolic identities,120 seventy-digit root/primitive regressions,5 cumulative endpoint controls | 38/38 repaired-hash/JSON/YAML refusals +4 actual write attacks, including unlisted cache and symlink; smoke3 and optimized12 |
| C398 | 108 complex rational terms,16 action rows,12 tails;3 symbolic identities,9 series/ODE cases,3 integral representations,12 source roots,3 norms,1 full resolvent trace at70 digits | 38/38 repaired-hash/JSON/YAML refusals +4 actual write attacks, including unlisted cache and symlink; smoke3 and optimized12 |

All five have deterministic two-directory evidence replay and three
double-fresh PDF builds, each with two settled LuaLaTeX passes. Fonts are
embedded/subset; text, bilingual abstracts, six keywords in each language,
references, control characters and rendered pages are checked. Raw settled
logs retain compiler-emitted whitespace; only the fifteen named current
compiler-log paths receive whitespace-lint exemptions.

Finite arithmetic and numerical tests are regression, not infinite theorem
proofs or interval certificates. No target zero table, prime-table model
definition, GPU experiment, proof-assistant certificate or external-model
peer review is claimed.

## Internal cross-review and discovered failures

Root read all three agent-authored complete proofs. The C395 author reviewed
C397's irreducibility, index sign, fluctuation errors and homoclinic rational
span argument; the C396 author reviewed C398's exact phase, norm/Green signs,
Hadamard factor, heat constant and fixed-normalization obstruction.

The C394 author independently audited C397/C398: for each, four extra
repaired-hash JSON attacks, ten YAML attacks and three actual YAML write
attacks were rejected, with disposable file snapshots unchanged. Its final
94-payload/96-physical SHA audit agrees with root's final hashes below.
The C395 author audited C394/C396: six extra repaired-hash type attacks and,
after repair, two C396 actual-write cache/symlink attacks passed. Their
91-payload/93-physical hash audit agrees with root.
The C396 author additionally tested C394 with ten repaired-hash JSON attacks
and ten actual YAML write attacks. A no-op replacement in that review's
first test fixture stopped the fixture; after correcting it for the actual
JSON-compatible YAML, all ten attacks ran and were rejected. This was not
a candidate bug. These supplementary populations are reported separately,
not merged into an inflated unique-test total.

An independent temporary-copy test found that C396's former release ledger
ignored files under __pycache__. The final code checks every physical file,
rejects symlinks before writes and verifies live evaluator bytes; the repaired
actual write gate was independently retested. No real unlisted payload was
present and no user material was deleted. C394/C397/C398 also gained explicit
symlink early-refusal tests. Evidence and all final PDFs were unchanged by
these engineering repairs.

C397 had two typesetting overflows,2.40773pt and6.29105pt, resolved by rewriting
the offending paragraphs. C398's initial exact checker did not simplify a
hyperbolic function of a rational logarithm before Rational conversion; the
exponential rewrite fixed the representation without altering the data or
theorem. Its first full resolvent-trace quadrature passed but was slow;
the final same-operator regression uses the half-integer energy where the
kernel simplifies, avoiding expensive evaluation near infinity.

C397/C398 have a full semantic YAML hard lock and an exact raw-byte manifest
ledger, not a raw-format immutable gate. An authorized write may reseal
semantically identical formatting. C394/C396 use stricter raw/semantic locks.
Do not conflate those contracts or the independent mathematical derivations
with reused release-harness structure.

Every final page was actually opened: C394 author viewed all nine revision
pages, C395 author its five final pages, C396 author all twelve revision pages,
and root all four final pages of each C397/C398. Automated raster existence
is separately tested and is not presented as visual review.

## Strict Route-A judgments

| Candidate | A0 | A1 | A2 | A3 | A4 | Overall |
|---|---|---|---|---|---|---|
| C394 | WEAK_ARITHMETIC_RELATION | WEAK | FAIL | FAIL | FORMAL_HINT | EXPLORATORY |
| C395 | WEAK_ARITHMETIC_RELATION | WEAK | FAIL | FAIL | FORMAL_HINT | REJECTED |
| C396 | FAIL | FAIL | FAIL | FAIL | FORMAL_HINT | REJECTED |
| C397 | WEAK_ARITHMETIC_RELATION | WEAK | FAIL | FAIL | FORMAL_HINT | REJECTED |
| C398 | FAIL | FAIL | FAIL | FAIL | NATURAL_QUANTIZATION | REJECTED |

C394 is only locally exploratory, not a primary HP candidate. C398's negative
counting theorem explicitly imports the unconditional number-theoretic S(T)
oscillation input; the full source derivation and application are proved.
The other classical owners are credited in each paper and source audit.
No automatic tuple-to-overall algorithm or novelty certification is invented.
All nine target/Route-B flags plus separate route_b_invocation_allowed are false.

## Frozen SHA-256 receipts

### C394

- [Manifest](henon_padic_symplectic_analytic_interpolation_route_a/C394_RELEASE_MANIFEST.json): `3146368faa567effd4df3a490cd143a29614e0727e9ec26cbbf79377a68418a0`.
- Evidence: `53df1f26a3ec5586fb3cce0b4d127659afc3ebcf912589714d10a23bc409f039`.
- [Final PDF](henon_padic_symplectic_analytic_interpolation_route_a/paper/main.pdf): `2ccb11a9fd06b146ec72de8ff50e20fe365627c65c03c462b23e83184459cd44`.

### C395

- [Manifest](henon_bcz_horocycle_farey_cycles_route_a/C395_RELEASE_MANIFEST.json): `8a0cfa5b0cae4fe8d46ee1df05ea000e62d35941a2bcbf79cf54cb1a4fef33b7`.
- Evidence: `bac2638210aa6d58c1d1f51ea295cf0ad262c7edc2c44b316c4c700820fc8169`.
- [Final PDF](henon_bcz_horocycle_farey_cycles_route_a/paper/main.pdf): `21ae04e9ec91e508ec4a3ac7cdccb058e70cb03c815047035786a93c103e0db2`.

### C396

- [Manifest](henon_impedance_string_empty_spectrum_route_a/C396_RELEASE_MANIFEST.json): `1509ceb585f57ae3db6f97b8b4c17f73d5a972d023d2787709393d69278463a7`.
- Evidence: `015000cea0cbb302ac272b6a935a7f1bcadad585af53f955f8883695854f9fa3`.
- [Final PDF](henon_impedance_string_empty_spectrum_route_a/paper/main.pdf): `a9b573b18382c8b4dcf346a955ca6f3cf1ce9e449de1293b0ea525c2676d5894`.

### C397

- [Manifest](henon_salem_toral_orbit_fluctuation_route_a/C397_RELEASE_MANIFEST.json): `1dbb5e3d6dbc3e3f37b57be75077e6ccb5cb0b1c0a2883aef136475a5cf32205`.
- Evidence: `cca119cb8e946657b8c0b7bdb19b2723dd7d912927ca7a27fac42e2683351711`.
- [Final PDF](henon_salem_toral_orbit_fluctuation_route_a/paper/main.pdf): `5a1507277f6b27e1e538a16df7358915e6dcb0fed196e71cf6b170e0f65462e4`.

### C398

- [Manifest](henon_exponential_wall_bessel_determinant_route_a/C398_RELEASE_MANIFEST.json): `d2fb4344af4bc703c4158f1e5b7dd56584ec0f2a0da5fc57aa58a79e5bfd186b`.
- Evidence: `ed76a339b3680f0a83918bc25fe2c0004c5d6ee805dc7a5c3fb327b35c541a13`.
- [Final PDF](henon_exponential_wall_bessel_determinant_route_a/paper/main.pdf): `cc3b31d93ac1a3f9d410db6d6c1ee026f44e304c2b6efa0e80c70a5bbd1be439`.


## Provenance, integration and user checkpoint

The remote advanced to9a394ee2c3ab171ba4341d77c439ba145e247a85 during work.
All421 changed paths belong to a disjoint symbolic-paper workflow
(SYMBOLIC_DYNAMICS_STATE.md, docs/, papers/), with no current-package or
evaluator overlap. A checked fast-forward preserved the frozen baseline.
The final pre-commit fetch found one further symbolic-workflow commit,
79e8729b5c25bbf3140482f7fd2ece7d32f09b79, with 130 changed paths confined to
SYMBOLIC_DYNAMICS_STATE.md, docs/, papers/, and symbolic_dynamics/.
An exact path-set check found no overlap with the 246 staged batch files or
the evaluator; a second safe fast-forward preserved all five manifests.
The final index contains exactly 238 package files and eight global files,
with every staged blob byte-identical to its working file.

The eight pre-existing untracked directories remain untouched and excluded.
Only these five packages and eight related global files may be staged.
The commit is to be identified by `Add Route-A papers C394-C398`; exact
commit and actual remote equality are checked at delivery, avoiding a
self-referential hash inside a file in that same commit.
After successful final release and push, report in Chinese and wait for
confirmation before C399–C403. No sixth paper has been started.
