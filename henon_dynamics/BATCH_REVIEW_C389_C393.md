# Batch review: HCS-C389--HCS-C393

## Frozen scope and release checkpoint

Date 2026-09-05; deterministic epoch 1788566400.
Frozen source baseline: `0c877206d202f732e21ea0b194f9c7fdf30467ee`.
Evaluator `flow_systems/skills/route-a-evaluator.md`, v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

All five complete packages passed their full write and subsequent full
nonwrite release gates. Every package contains one final paper, not a fragment
of a shared paper; three substantive versions record its own development.
Final PDFs total 22 pages. The packages contain 238 payload files plus five
self-excluding manifests, hence 243 physical files. All final pages were
actually viewed. Exact closure is recorded below and in the five manifests.

A separate team agent performed the final five-package static audit;
that auditor also authored C390, so this is not nonauthor review of all five.
Root separately recomputed all physical memberships, payload file hashes,
canonical evidence hashes, evaluator/baseline locks, literal scope flags,
actual PDF page/font data and settled-log checks. Cross-author mathematical
reviews are identified per package below. A final C393 prose-only
cross-package reference was corrected and its release gate rerun before
the last hash audit. This reaches the user checkpoint. C394--C398 is not
authorized or started.

## Five complete source-theorem increments

**C389 — Carlitz full ring-action torsion and ramified towers.**
For all prime powers q and monic conductors a, the complete A=F_q[theta]
action has cyclic torsion A/a and explicit annihilator strata. Every
multiplier has exact transient and periodic laws; a nonunit multiplier is
not treated as a permutation. The reduction identity C_P mod P = X^Q is
proved using the impossible Q-point orbit of a nonzero root of a
derivative-zero degree-Q polynomial. Every prime-power primitive
polynomial is P-Eisenstein, giving the full Galois group (A/P^k)^× and its
compatible inverse limit. Total P-ramification and absence of other finite
ramification prove linear disjointness of different-prime towers and the
full composite-conductor group. Distinct valuations give the integral
basis, every lower ramification group and different exponent
Q^(k−1)[k(Q−1)−1]. Infinity and maximal class-field theory are excluded.
Carlitz theory is a classical owner; function-field arithmetic does not
supply a rational-prime target clock merely by analogy.

**C390 — full positive Lyness dynamics and real/rational period contrast.**
For a>0, strict convexity and properness in logarithmic coordinates give
the unique center and complete positive regular-oval foliation.
Normalized Abel time gives the exact circle rotation, all least periods,
dense irrational orbits, repetition laws and return shear
[[1,0],[n rho'(h),1]]. No everywhere-nonzero twist or global monotonicity
is assumed. Explicitly imported Bastien--Rogalski endpoint values and
continuity imply that each fixed a≠1 realizes every sufficiently large
prime integer as a real least period. The separately imported
Gasull--Mañosa--Xarles/Mazur rational-torsion classification restricts
positive rational periods to 1,5,9, with period 5 only at a=1.
An exact a=7 nine-cycle is verified. Translation-point torsion is not
starting-point torsion. Periodic real ovals are uncountable, preventing
the ordinary point-cardinality zeta. On each finite invariant annulus,
the Koopman spectrum is the full unit circle with point spectrum {1}
for a≠1; a=1 has five-root pure point spectrum. Singular fibers and
the center are separate boundaries; a=0 is not inside the contract.

**C391 — all supercritical inverse-square domains, spectrum and limit cycle.**
For sigma>0, every unit-modulus boundary parameter kappa specifies a
self-adjoint half-line realization of
−d²/dx²−(sigma²+1/4)/x². With
varsigma=kappa Gamma(−i sigma)/Gamma(i sigma)=exp(i theta), its entire
simple negative spectrum is
E_j=−4 exp[−(theta+2 pi j)/sigma], j in Z.
Normalized Bessel bound states, Green kernel, Stone jump and Hankel-type
continuous transform close the full spectral resolution: the positive
part is purely absolutely continuous of multiplicity one, with no
positive eigenvalue, zero mode or singular continuous part.
The incoming reflection convention is explicitly distinguished from
relative scattering. Domain dilation sends kappa to
kappa exp(−2i sigma tau); the log-momentum scattering period is pi/sigma.
No supercritical extension is continuously dilation invariant or
Friedrichs; every one is unbounded below. Classical fall to the center
does not choose the extra quantum boundary phase. Positive-time heat is
unbounded, the resolvent is noncompact, and the bilateral negative-ladder
zeta has no convergence half-plane. This rules out the specified ordinary
global constructions, not every possible relative renormalization.
The classical complete model is explicitly attributed to
Dereziński--Richard.

**C392 — Lüroth whole-plane operator continuation and determinant blindness.**
On H²(D_2), the native transfer family uses
h_n(z)=(z+n)/[n(n+1)] and a_n=1/[n(n+1)].
For Re s>1/2 it is trace class with an explicit norm tail, complete
algebraic spectrum A(s+j), and determinant
D(u,s)=product_(j≥0)(1−u A(s+j)), where A(s)=sum_n a_n^s.
The full primitive stability product is distinguished from the simpler
word product D(u,s+1)/D(u,s). Complex eigenvalue collisions do not justify
an unproved diagonalizability claim. A centered Hurwitz expansion
continues A, and a separate trace-norm coefficient estimate continues
the entire operator family meromorphically over the whole plane.
At s=(1−l)/2 the residue has rank floor(l/2)+1. At nonpositive integers
it is nonzero and square-zero, so the operator has a genuine pole although
the scalar determinant is holomorphic. At s=1/2−m, D(1,s) instead has
exact pole order m+1; no zero-free entire prefactor can turn this frozen
object into an entire target. The isolated endpoint zero is not silently
included in the positive-branch derivative product. Neither composite
slopes nor a Hurwitz rewriting inserts a prime carrier.

**C393 — full generic quadratic tree and zero periodic fraction over primes.**
For f(X)=X²+1 over Q(t), the distinct critical values give one new simple
quadratic branch at every height. Its inertia is a single sibling swap
in the previous restriction kernel; parent transitivity supplies every
independent swap. Thus both geometric and arithmetic groups are the full
binary-tree automorphism group at every height, with regular constant
field Q and full inverse limit. All finite branch inertia types, infinity
inertia, Galois-closure genera and cycle indices are explicit.
The fixed-leaf probability satisfies delta_0=1 and
delta_n=delta_(n−1)−delta_(n−1)^2/2, hence n delta_n→2.
For fixed n, primes avoiding
B_n=2 product_(0≤i<j≤n)(c_j−c_i) have the same full tame regular group.
Explicitly imported finite-field Chebotarev/Weil then gives image density
delta_n+O_n(p^(−1/2)). Periodic points lie in every iterated image:
taking the prime limsup first and then n→∞ proves that their fraction
tends to zero over primes. No uniform height cutoff, rate in p, or full
group for every rational specialization is asserted. Tree height,
map iteration and Frobenius iteration are distinct clocks. Odoni, Pink
and Juul--Kurlberg--Madhu--Tucker retain their source ownership.

## Strict route assessment

| ID | A0 | A1 | A2 | A3 | A4 | Overall |
|---|---|---|---|---|---|---|
| C389 | STRUCTURAL_ARITHMETIC_RELATION | WEAK | FAIL | FAIL | FAIL | EXPLORATORY |
| C390 | WEAK_ARITHMETIC_RELATION | WEAK | FAIL | FAIL | FORMAL_HINT | REJECTED |
| C391 | FAIL | FAIL | FAIL | FAIL | NATURAL_QUANTIZATION | REJECTED |
| C392 | FAIL | WEAK | FAIL | FAIL | FORMAL_HINT | REJECTED |
| C393 | STRUCTURAL_ARITHMETIC_RELATION | WEAK | FAIL | FAIL | FORMAL_HINT | EXPLORATORY |

These are candidate-local target judgments, not a rating of the whole
repository or a denial of source-theorem completeness. Evaluator §6
lists allowed overall judgments but does not define a unique automatic
tuple-to-overall function. Conservative reasoned grades are retained.
C391's A4 refers to the natural differential expression with an explicitly
chosen additional boundary domain, not a uniquely selected target operator.

All nine target/Route-B flags are literal false; separate
route_b_invocation_allowed is also false.
Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
No target local arithmetic, Euler factor, root number, automorphy,
target functional equation, target zeros/divisor/counting law,
Hilbert--Pólya operator or Route-B invocation is claimed.

## Executed evidence and release receipts

| ID | Actual independent audit population | Built-in hostile population | PDF rounds | Payload / physical |
|---|---|---|---|---|
| C389 | 107 conductors, 1,829 multiplier maps, 40,937 node/multiplier combinations, 21,948 fixed cells, 77 tower cases; 191,903 checker assertions and 22,782 exact symbolic checks | 63 distinct: 51 repaired-hash + 2 JSON + 10 YAML | 2 / 3 / 4 | 52 / 53 |
| C390 | 24 controls / 288 exact steps, 11 complete cycles / 59 points, 5 rational centers, 1,280 denominator controls, 690 reduced rotation witnesses; 35 exact identities, 11 high-precision enclosure controls and 24 quadratures at 90 digits | 38 distinct: 31 repaired-hash + 2 JSON + 5 YAML | 3 / 4 / 5 | 48 / 49 |
| C391 | Checker 45+27+15 exact and 60+36 numerical controls; 8 symbolic identities; at 100 digits 108 actual Stone-jump cells, 12 Wronskians, 12 Bessel ODE, 12 boundary matches, 3 normalization integrals and 36 log-period checks | 56 distinct mutations, 66 refusals: 42 repaired-hash + 4 JSON + 10 YAML, the YAML exercised through two gates | 3 / 4 / 5 | 44 / 45 |
| C392 | 12 branches, 16 degree-six matrices, 10 operator residues, 10 scalar residues, 340 words; 1,169 matrix cells, 220 exact identities; at 100 digits 6 dual Hurwitz comparisons, one s=1 value, 4 telescoping and 3 phase controls | 44 distinct: 32 repaired-hash + 3 JSON + 9 YAML | 3 / 3 / 4 | 47 / 48 |
| C393 | 8 tower rows, 6 cycle indices with 255 types, 13 probability rows, 25 fields / 150 levels; 32,907 direct tree permutations through height 4, next-height class convolution; 14 exact identities and 632 factored residue polynomials | 44 distinct: 32 repaired-hash + 3 JSON + 9 YAML | 2 / 3 / 4 | 47 / 48 |

Finite samples are regression evidence, not proofs of infinite quantifiers.
Working precision and agreement thresholds are distinguished from rigorous
interval certification; C390's quadrature is not an interval certificate.
Each package also ran three smoke tests, two unrelated-directory byte replays,
and actual rejection of six lane scripts under both -O and -OO.
All three versions in every package passed double fresh two-pass PDF builds.
Final embedded/subset font records are respectively 17,9,9,8,8.
Settled logs have no missing-glyph, layout, citation or reference warnings.
C392's first two versions both have three pages but add genuine theorems;
content markers and extracted-text growth, not blank padding, certify revision.

| ID | Evidence file SHA-256 | Final PDF SHA-256 | Manifest SHA-256 |
|---|---|---|---|
| C389 | `1ff01a9e016348903f4f7b6548953fc298967474c7ce3d6a54ed98db5d637c35` | `7ebe468e3a4730039ae63d3ae932ef4b88bbc85bb911c692e983b877ea7dd33e` | `c2c43fe1205b2ad9e9c6b320c74cb3f75ba9f959173be039b7eba561ac687149` |
| C390 | `6916995178818788172b5963b8c42b043c573be1acdf4a2635f5d7de6697d8f9` | `398163e43de109d0ff0f5f06534e6d78600562c5d978eb428cef76f0f7f7b2c4` | `e31b099501b29b6396d4ccdbc3aeb4be095e797f4c7d01f186e54f258f8fb1f9` |
| C391 | `069eabac801adf6c6ceabd14f8e9c0aa26ce5f79664f2d2365dc3e54671ae3a8` | `1c72bd8a6d6818f96cc40f211504f54d9144585efb2b2a05b8e0c185c8f1976a` | `c5d791fcefe6a42df48159a9438ed254c7a1547aefa92587b7412edaf7e3c4b1` |
| C392 | `3f36398866c1b8df65f19000454e5dd5f2cad72428c783eec37ad48d4b6283d0` | `8ee1aafbf1df90011f95757c8103678e2bb6fa1931ed060175fd1737dc8cb172` | `3431697b33973ba673dc13591f001e14a81b1a42b909d2e15da8a4cd2ee6a267` |
| C393 | `683b1866a4e7592afd483d82cf87145c11de32793538d75867c57c3930128b49` | `6b46c9c8fddd921ffa5b9518fedfe283da6eef581698c0ba4bdacb5af010b6bf` | `56e16665f474416823ac9c307fa2ce8b1ed5f11e32f9338e61d20e661827a4ee` |

## Internal review, actual failures and repairs

- Root and a second reader checked C389's reduction proof, full Galois
  kernel, ramification filtration and different; all-parameter claims
  were not inferred from the 107/77 finite cases. Its mutation runner
  initially used Python equality to decide whether a boolean-to-integer
  mutation changed data. That failed efficacy check was corrected to
  serialized comparison; the semantic checker already used exact types.
  An additional independent reader executed nine repaired-hash JSON and
  ten YAML attacks, all refused.
- Root read C390's full proof, including the positive domain, exceptional
  five-periodicity, external torsion ownership and annular Koopman claim.
  The evidence report was corrected to distinguish 35 exact identities
  from 11 numerical enclosure controls, rather than calling all 46 symbolic.
- C391's full proof and manuscript were independently read by root and
  the C390 author. Incoming reflection and relative scattering, all
  boundary phases, the signs in the bilateral ladder and the ordinary
  operator-class obstructions were retained. Root required actual
  Green-boundary-value versus spectral-kernel Stone comparisons and an
  explicit normalization derivation; both were implemented and checked.
- C392/C393 had independent full proof/manuscript and code review.
  Besides the built-in suites, a nonauthor executed ten repaired-hash
  JSON attacks per package and ten YAML variants per package through
  both the checker and actual writable-release entry: twenty YAML
  refusals per package, all before any write. These are separate
  cross-review populations, not silently added as disjoint built-in cases.
  Independent algorithms use affine-power/binomial reconstruction for
  C392 and direct tree permutations/function-graph periodic detection
  for C393, not merely producer self-comparison.
- A C392 complex-phase check initially included a real argument and
  incorrectly required a nonzero imaginary component. The failed run
  was not accepted; the control now targets the three actual complex
  inputs. No theorem or evidence hash changed.
- C393's SymPy/flint factor sorting raised “nmods cannot be ordered”.
  The separate symbolic lane now selects SYMPY_GROUND_TYPES=python
  before import; all 632 factorizations then completed. The final
  C393 improvement-log cross-reference to C392 was removed, followed
  by complete write/nonwrite resealing; PDF and evidence did not change.
- Actual visual inspection found Latin glyph boxes inside Chinese font
  spans. Explicit Latin spans and a missing-character hard gate repaired
  them; scope lines were restructured to remove overfull boxes.
  All affected versions were rebuilt and final pages actually viewed.
  No warning suppression or blank-page padding was used.
- The first root static-audit draft assumed one common manifest/evidence
  layout; it stopped on C391's absent redundant version field and
  C389's wrapped payload. The audit was adapted to their actual schemas,
  retaining version verification in frozen YAML and canonical payload
  recomputation. Only the final complete run is recorded as PASS.
  This required no package data change.
- Seven ARS failure modes and claim/reference boundaries are recorded
  in each package. Internal current-team review is not external,
  cross-model or human peer review, and not publication acceptance.

## Source verification and workflow limits

Primary source locations, actually read passages and inaccessible routes
are recorded in each SOURCE_AUDIT.md. Classical ownership is not inferred
from plausible citation strings. C392's Acta publisher PDF timed out:
bibliographic metadata were verified and the coding used here proved
locally; full-PDF inspection was not claimed. The actual Bandtlow--Jenkinson
preprint theorem/proof and NIST Hurwitz entry were read.
For C393, the JKMT arXiv theorem, branching lemma and finite-field argument
were inspected; the published author-PDF route failed. Online publication
in 2015 and the 2016 journal issue are distinguished. Odoni/Pink are
credited at the level actually verified, not assigned an unread numbered
theorem. Similar source/version limits are explicit in C389--C391.

Applied skills: ARS academic-research-suite and its academic pipeline /
integrity protocol, idea-creator, proof-writer, paper-write and paper-compile.
They enforce selection/collision control, complete proofs, source ownership,
independent evidence, substantive revisions and actual PDF inspection.
The user's five-complete-then-confirm instruction replaces repeated
within-batch permission stops. Standalone mathematics format replaces
irrelevant ML venue scaffolding. No GPU pilot, target fitting, numeric
novelty score, external GPT-5.4 call, formal full ARS runtime, optional
unavailable advisory check, submission or novelty certification is claimed.

## Repository integration and preservation

During this round, origin/main advanced by three symbolic-track commits
touching 467 paths: one symbolic state file, 203 docs paths and 263 papers
paths. Read-only overlap checks found no changes under henon_dynamics or
flow_systems/skills. A safe fast-forward reached
`908069ac646c281941788b49e09c0671bf8be0b8`; the frozen scientific baseline
remains `0c877206d202f732e21ea0b194f9c7fdf30467ee`.

Only the five exact package directories and eight related global files
belong to this release. Raw compiler logs have narrowly scoped whitespace
attributes; source, proof, JSON/YAML and prose files remain under normal
whitespace checks. Earlier author-created C389/C390 files at the wrong
root paths were moved into their proper package without data loss.
No current-batch root stray remains.

The actual staged audit passed: exactly 251 files, comprising 243 package
files and eight globals; every staged blob equals its worktree bytes, no
unstaged tracked change remains, and source/proof/data text passes strict
EOF, trailing-whitespace and control-byte checks. The actual
git diff --cached --check passed. All newly introduced global links resolve.
A second precommit fetch found HEAD and origin/main equal at 908069ac…;
there was no further remote advancement at that check.

The five old C99--C103 untracked packages and three old root directories
are preserved and excluded. Those root directories contain twelve legacy
files; therefore the entire worktree must not be described as empty.
The commit is identified by `Add Route-A papers C389-C393`; the actual
commit hash and final remote equality are reported after the push rather
than self-referenced inside their own commit.
