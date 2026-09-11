# P213 independent SOURCE/PARAMETER audit 01

2026-09-09 UTC. Reviewer: /root/round211_finite_matching_scout.
Disposition: SOURCE_PARAMETER_ACCEPTABLE / RUNTIME_HOLD.
This is not manuscript review A/B, runtime acceptance, execution authority,
canonical adoption, a source-only build, or paper completion.

## Exact scope and independence

The selected paper is papers/213-receiver-limited-cyclic-transfer, exactly
29 payloads plus its nonself SOURCE_MANIFEST.sha256, 30 files / 556,560 bytes.
The whole manifest SHA256 is
e232b73013c3d6d1828e778f800f981bf00921a4a6f56f979aaec6e044ebdc09.
The verifier is 451 lines / 17,539 ASCII bytes, SHA256
a01d3d93619cea90adfc2e5be1bdfd8089d7eae6fcaae153b4fb4af398fc1812.
Acceptance is restricted to these exact bytes and the 48 INPUT_PINS inputs.

I did not contribute fresh07 or P213 proof, pilot, verifier, prose or
bibliography. Before fresh07 selected this rule I supplied only navigation
to previously closed matching candidates/controls, not receiver-limited
cyclic-transfer content. AUTHORSHIP records FRESH as sole mathematical/code
author. I read the current complete proof and verifier as an auditor and
authored no repair, new scientific code or new mathematical result here.
This source familiarity must be disclosed if root later selects me as a
manuscript reviewer; no such assignment or independent scientific lane is
created by this report. The prior candidate gate is also not A or B.

## Literal, parameters and algorithm consistency

The full carrier is all labelled nonnegative integer cyclic compositions
of mass N, with fixed orientation and no rotation quotient. The current is
min(a_i,a_(i+1)), computed wholly from the old state. It is receiver mass,
not receiver vacancy. No scheduler or hidden state is introduced.

The six size values 1..6 and five masses 0..4 give 30 complete carriers.
Summing stars-and-bars cardinalities over the five masses gives respectively
5, 15, 35, 70, 126 and 210 states by size, total 461. This is independent
parameter arithmetic, not a scientific run or a list of observed states.
All six code constants, parameter declarations and printed PARAM literals
agree. Mass zero, sizes one/two, all-zero and uniform states remain included.

The following is a source audit against the submitted deductions, not a
new proof or an empirical pass. Line anchors refer to the exact verify.py.

| Source anchor | Received obligation | Source-level assessment |
|---|---|---|
| 30, 40, 293 | Full labelled carrier | Recursive weak compositions preserve lexicographic order; cardinality, uniqueness, membership and closure checks cover each full carrier. |
| 48, 303 | Literal forward graph | All currents are built before any successor coordinate; predecessor lists are accumulated from all states, not imported tables. |
| 55, 62, 78 | Fixed classification, terminal map, strict-cycle exclusion | Residual minimum normalization matches the proof. Endpoint walks stop at an original zero; direct trajectories include the first fixed state and reject an earlier nonfixed repeat. Depth is path length minus one. |
| 221, 229, 239 | Sharp worst clocks and n=3 pointwise formula | Zero/small-mass and n=1,2 branches are guarded; bit_length implements the n=3 ceiling-log branch without floating point. Witnesses separate N=0,1,2. The doubled endpoint is compared through saturation and one extra fixed step. |
| 92, 101, 117 | Unique words and cyclic blocks | Equality belongs only to bit one. Only mixed masks enter the block routine; all valleys are assigned before descending recursions, including wraparound and empty descent interiors. |
| 132, 147 | Forced dyadic descents and short ascents | Divisibility precedes integer division; nonnegativity and strict descent are checked. A one-edge ascent forces its peak and both boundary inequalities. |
| 157, 162, 164 | Long ascents and interval bounds | The shifted equality/order tests include r=2. The upper bound uses the peak target minus integer one, not the preceding target coordinate. Assigned interiors and interval pairs occupy the submitted disjoint roles. |
| 174, 189, 359 | All sources and multiplicities | Free intervals are enumerated independently. Missing/negative coordinates, mass or exact-word failures raise assertions rather than filtering a bad reconstruction. Per-word complete source lists, within-word uniqueness, product counts and the full disjoint union are checked against graph predecessors. |
| 338, 341 | Constant words and short cycles | n<=2 uses the identity fibre. The all-ascent contribution is exactly a uniform target; the impossible all-descent word is omitted. |
| 201, 377 | Fixed-target product | Called only for the fixed classification. Uniform targets return one; residual preceding gaps include a sole spike and give factors only for at least two zeros. |
| 390 | Largest-fibre bounds | Finite maxima/maximizer rows are observational certificates for this box, not new all-parameter extremizer claims. The degree, threshold, spaced-spike construction and exact rational lower-bound comparison match the proof. |
| 428 | Coverage requirements | First-failure status order and accepted-shape counters are explicit. NEGATIVE_DESCENT is correctly required to be zero for nonnegative forced data, not falsely advertised as an exercised positive branch. Other positive counts are pending assertions, not measured results. |

No source-level contradiction, excluded boundary or identified algorithmic
blocker was found. This does not claim machine syntax acceptance or that a
future process will terminate successfully under an unresolved runtime.

## Proof, output and provenance boundaries

The complete 435-line paper proof, all eight TeX files and bibliography were
read, as were the original 391-line candidate proof and the selected gate,
source-check, erratum, delta and root-reception originals. The submitted
temporal argument, eliminated one-step inverse and degree proof have the
same scope as P213_THEOREM_CONTRACT. The manuscript keeps the distinction
between an arithmetic-operation count and bit complexity, and does not add
general pointwise clocks, all-time fibres, a basin census, exact finite-N
maxima/all maximizers, or a numerical proof of the growth exponent.

OUTPUT_SCHEMA and every output construction agree on record names, field
order, vector/interval formatting, tie word, first-failure certificates and
census order. Carriers and targets are lexicographic; masks are ascending.
Each target's mixed WORD records precede TARGET; CARRIER closes each carrier;
TOTAL and PASS close the output. All scientific records are buffered before
the sole print, with a final LF. As parameter arithmetic only, successful
completion would emit 17,990 WORD records, 461 TARGET records, 30 CARRIER
records and four framing records: 18,485 total lines. No byte size, CHECKS
value, branch census or successful stdout has been invented or adopted.

The author source has no imports, data/file/environment/argument reads,
subprocesses, floating-point calculations or randomness. The interval
reconstruction does not call forward; source-set comparisons are explicit.
This is an author verification lane, not an independent manuscript reviewer
implementation. The old candidate pilot tested only temporal claims in its
own 756-state/21-carrier box; the later independent candidate check remains
separate historical evidence. Neither is the new paper canonical or either
member of a new strict replay pair. I did not replay or independently
re-parse those archived scientific outputs here.

The old finite-field P211 label remains visible in its frozen original and
is corrected only by the named accepted erratum/delta. New P213 prose uses
the corrected finite-chain label. This audit follows the accepted bounded
source-history boundary; it is not a fresh global ownership, literature or
venue-quality review. No primary-source access was claimed without a new
actual access, and no whole-paper primary read is inferred from a hash.

## Documentary evidence and retained failures

Both inventory native returns passed 1,602 checks each. The complete 48
input keys agree byte-for-byte between them: whole SHA256/length plus dev,
ino, mode, nlink, uid, gid, rdev, size, mtimeNs and ctimeNs. The helpers use
bounded regular workspace reads and descriptor/path endpoint checks; atime
is excluded. This is an ordinary-trusted documentary boundary, not an
adversarial host attestation or Python/TeX runtime closure.

The 50 actual read records preserve 259,056 output bytes. The final
documentary closure matched 42 selected raw read returns, 229,972 bytes,
to their unchanged current originals and rechecked all 48 complete keys;
it exited zero with 1,437 checks. The other eight read records are preserved
but not falsely counted as raw-content comparisons of immutable inputs.
READ_SCOPE distinguishes complete manual reading from whole-key-only intake.

Two audit-tool failures are retained, not hidden: the first closure wrongly
expected the same command spelling for the absolute-path first inventory
and relative-path second inventory; an ensuing documentary diagnostic
one-liner had an extra closing brace. The failed closure source/native and
diagnostic return are unchanged. The separately saved closure_delta01
accepts those two exact actual request strings and passes. Neither failure
ran or modified a scientific source or invalidated its pinned bytes.

## Outstanding runtime and lifecycle gates

RUNTIME_PLAN explicitly leaves interpreter/startup/native identities,
controlled launch directory, flags, complete stdout/stderr/exit capture,
transport capacity, and wall-time/memory boundaries unresolved. Zero source
imports does not imply zero Python startup dependencies. Buffering output
does not guarantee complete transport or an accepted runtime limit. Those
are acknowledged later gate obligations, not defects concealed as passes.

Root must separately receive a finite runtime/observer/launcher contract
before any Python invocation, import, AST/syntax operation or execution.
Only a complete accepted initial result may supply a byte-identical canonical;
the separate strict author replay pair remains subsequent. TeX/BibTeX
runtime selection, initial build/all-page view/physical Round0, distinct
actual A/B reviews and their strict lanes/deltas, physical Round1/Round2,
and terminal builds/views remain outstanding.

Finding census in this SOURCE/PARAMETER scope: FATAL 0, MAJOR 0, MINOR 0
identified. No scientific operation, build, host/config/environment/private
check, Git/SSH operation, external manuscript upload or contact was performed.
Only this new audit directory was written. Root owns central state updates.
HOLD_EXTERNAL.
