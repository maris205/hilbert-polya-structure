# Paper 45 result-free experiment plan

## Status and binding

Status: PREREGISTERED_NOT_RUN.

This plan is bound to:

- the final unique Phase-2 self-excluding parent seal with SHA-256
  d035310ac046981abe7a37a033b1354e3d8da3f53f33d631786ed80f40b90181,
  which supersedes every earlier Phase-2 manifest candidate;
- the corrected theorem audit with SHA-256
  12187d0bdb8671e5daf4893aac995b6e33ff87355df4d84778680306b17fbc5a;
- the independent hostile audit with SHA-256
  926aad2a27ef88fdb82e8cdca487d34c75d44141c9827d9863bf5a3eae8e1326;
- the exact definitions and domains in SOURCE_LOCK.md;
- the two claims and independence boundary in METHODOLOGY_BLUEPRINT.md;
- the typed case/evidence/transaction contract in EXPERIMENT_CONTRACT.json;
- its strict Draft-2020-12 schema in EXPERIMENT_CONTRACT_SCHEMA.json;
- the executable atomic mutation/consumer registry in
  MUTATION_REGISTRY.json and its strict schema in
  MUTATION_REGISTRY_SCHEMA.json.

No evaluator has been implemented or run by this package. No numbers below
are observations. Execution requires a later explicit authority decision and
a newly sealed implementation manifest.

## Primary claims

The run may evaluate exactly two primary claims.

### C1: isospectral but geometrically inequivalent retractions

For every \(h\ge2\), the pair has the exact separate existence and
power-Schatten domains, common simple nonzero eigenvalues and legal traces,
and the similarity split

\[
S_{h,s}\sim_{\mathrm{bd}}\text{ normal}\iff\sigma>1,
\qquad
M_{h,s}\sim_{\mathrm{bd}}\text{ normal}\iff\sigma>1/h.
\]

### C2: exact arithmetic distortion phase laws

The saturated primorial maximal order, both singular Weyl constants and the
\(\sigma=1\) crossover, and both self-commutator ideal laws hold with every
strict endpoint and the separate \(h=2\) witness.

The determinant equality, finite matrices, and free-UFD clone are controls,
not additional primary claims.

## Anti-claims

The experiment is designed to reject, not support, the following:

- finite truncations prove infinite convergence or a Tauberian theorem;
- equal eigenvalues or determinants imply bounded similarity;
- \(C_{h,\sigma}\) and \(D_{h,\sigma}\) are always different;
- a formal \(M^k\) exists below the \(M\) boundedness wall;
- the \(h=2\) radical case alone is paper-sized;
- the construction selects rational primes rather than normed formal atoms;
- generic weighted-composition, oblique, Gram, Schatten, or determinant
  methods are new here;
- ROUTE_EXPECTATION.yaml is an evaluated Route outcome.

## Experimental units

The mathematical unit is one tuple

\[
(h,s,\sigma,k,q,r,m,u,z,\text{retraction},\text{evidence type},
 \text{cutoff},\text{precision}),
\]

with exact types retained. Here \(r\) is a positive integer determinant
order, \(u\) is the typed complex analytic variable for generalized
Dirichlet/Tauberian certificates, and \(z\) is the typed complex Fredholm
variable. A finite block unit and an analytic Euler unit are distinct
evidence types even if they project to the same scientific field.

The required semantic strata are:

- \(h=2\), at least two values \(h\ge3\), and one larger-\(h\) stress case;
- real and genuinely nonreal \(s\) with the same \(\sigma\);
- parameters strictly below, exactly at, and strictly above every relevant
  wall \(0,1/h,1/q,2/(kq),2/k,1\);
- saturated sets empty, singleton, and containing at least two primes;
- the mandatory \(\sigma=1\) row for every tested \(h\);
- \(h=2\) commutator blocks with two saturated primes;
- nested fiber, prime, block-label, and precision cutoffs.

EXPERIMENT_CONTRACT.json freezes the concrete case IDs, exact raw values,
cutoffs, precision ladder, finite/infinite evidence tags, required and
forbidden fields, and the common finite case set. In particular,
FIN-H2-M6-REAL and FIN-H2-M6-COMPLEX have the same \(h,m,\Re s\) and differ
only in \(\Im s\); the registry also contains modulo similarity, the three
primorial regimes, a noncrossover Weyl row, \(h\ge3\) commutator necessity,
and the separate \(h=2\) Euler-commutator identity. The three finite
cutoffs in each compression case are zipped, in order, with 128, 256, and
512 bits. Both implementations must independently parse and expand those
neutral cases. There is no shared generated fixture, seed, intermediate,
or expected-value file.

The contract also freezes a 13-row raw serialization case grid. It contains
JSON-number spellings `6.0`, `6e0`, numerator/denominator `1.0`, a Boolean
numeric surrogate, plus/leading-zero/`-0` strings, a duplicate `base`, a
reordered-but-equivalent object, and a noncanonical stored-JCS envelope.
The parser must inspect duplicate members before constructing any mapping.

## Evaluator independence

### Evaluator A: direct map and finite matrix

Implementation family: a standalone Python program using its own
trial-division factorizer, exact rational/complex input parser, and direct
matrix construction. Numerical linear algebra may use NumPy/SciPy, but all
small integer and rational invariants are independently checked before a
floating calculation.

Allowed inputs:

- raw definitions of \(\tau_h\), \(\omega_h\), and \(n^{-s/2}\);
- type schema for inputs and final outputs;
- public runtime/library versions.

Forbidden inputs:

- closed fiber, Euler, Riesz, Weyl, or commutator formulas;
- Evaluator B source or output;
- project helper modules, expected tables, or generated shared cases.

Algorithm:

1. enumerate \(n\) at nested cutoffs and compute the two maps directly;
2. group basis indices by their computed image;
3. form finite block matrices without using a closed fiber description;
4. calculate matrix rank, singular values, eigenvalues, powers, Riesz
   idempotents, and self-commutators;
5. enumerate all \(h\)-free labels below independent cutoffs and find
   projection maxima;
6. emit exact fields and certified numerical intervals with a sealed method
   and coverage ledger;
7. refuse every infinite theorem field listed as forbidden for
   FINITE_COMPRESSION evidence. Nested trends are diagnostic only.

### Evaluator B: exponent states and Euler/Tauberian algebra

Implementation family: a physically separate standalone Python program
using its own prime sieve/factorizer and SymPy/mpmath only for independent
symbolic and high-precision arithmetic. It contains no import path to
Evaluator A.

Allowed inputs are the same raw definitions and final schema. Forbidden
inputs are all matrices, enumerated fibers, Evaluator A source/output,
shared helpers, fixtures, expected tables, and serialized intermediates.

Algorithm:

1. derive allowed local exponent states for each map;
2. derive fiber masses and power/Schatten Euler factors from those states;
3. independently derive eigenvalue and trace Euler products;
4. compute Riesz factors and the exact prime-set optimization;
5. expand the Tauberian local factor, derive both strip inequalities and the
   residue, and evaluate independent partial products;
6. derive \(h\)-free counts, modulo/eigenvalue constants, and the mandatory
   crossover;
7. derive self-commutator factors and the two different necessity families;
8. repeat the exponent calculation in a formal free-UFD atom namespace;
9. emit an independently sealed final projection.

Every infinite theorem certificate from Evaluator B is independently
checked by proof auditor P against PROOF_PACKAGE.md and the locked analytic
dependencies. B must emit exactly the 15 frozen INF cases in C-sort order,
with no missing, duplicate, extra, reordered, or `INF-UNDECLARED` row; A
must emit exactly zero infinite records. P must audit the identical ordered
15-case set and close certificate owner plus payload/proof/analytic hashes
case by case. The canonical LF-joined set hash is
6401b141f7b46b0f7275ec124ec571542655b9874cfa9aa5c7123108577e8a84.
Evaluator A and comparator X are forbidden consumers for those
certificates.

### Physical and chronological separation

- The two source trees have disjoint owners and no common production file.
- Each source manifest is sealed before either evaluator runs.
- Each evaluator runs in a directory from which the other source and output
  are unreadable.
- Neither output is exposed until both output manifests are sealed.
- Only a third comparator receives the two final projections.
- Method identities, dependency lists, logs, and internal check ledgers are
  never normalized into a shared artifact.

Failure of any clause is an automatic HOLD_INDEPENDENCE.

## Core block B1: raw maps to finite block invariants

Owner: Evaluator A.

Purpose: test C1's fiber geometry without importing the theorem formulas.

Required outputs:

- direct \(\tau_h(n)\) and \(\omega_h(n)\) images;
- independently grouped finite fibers;
- finite block rank and unique nonzero singular value;
- nonzero eigenvalue as a canonical `DIRICHLET_POWER` AST and its algebraic
  multiplicity; `complexExact` is forbidden because \(m^{-s/2}\) is
  generally transcendental. The real \(m=6\) row uses base string `"6"`,
  real rational strings `("-3","4")`, and imaginary rational strings
  `("0","1")`; the nonreal row changes the latter to `("-1","6")`.
  Both use `REAL_LOG_POSITIVE_BASE` and store exact RFC8785 JCS plus SHA-256;
- an optional independently certified complex interval enclosing the AST's
  numerical evaluation;
- exact power relation residual;
- Riesz-idempotent norm;
- two self-commutator singular values.

Positive controls:

- \(m=1\), where the saturated fiber is a singleton;
- \(h=2,m=6\);
- \(h=3,m=12\);
- real/nonreal \(s\) pairs sharing \(\sigma\), whose singular values agree
  while eigenvalue phases differ.

Failure criteria:

- wrong map image, block rank, phase behavior, or power relation;
- more than one nonzero singular value in a block;
- disagreement between direct matrix and direct coefficient square sum;
- any finite cutoff labeled as the infinite block.

## Core block B2: exponent/Euler phase diagram

Owner: Evaluator B.

Purpose: independently test both claims at the symbolic and convergence-wall
level.

Required outputs:

- exact saturated and modulo fiber descriptions;
- block mass formulas and existence walls;
- exact Euler factors for \(T^k\in\mathcal S_q\);
- common eigenvalue and legal trace product;
- Riesz factors and both similarity iff verdicts;
- commutator block factor and ideal walls;
- distinct \(h=2\) and \(h\ge3\) necessity certificates.

Success criteria:

- every strict comparison operator agrees with the frozen contract;
- leading local prime terms give exactly the walls two and one;
- \(M\)'s existence wall appears in every power, trace, determinant, and
  commutator consumer;
- all exact symbolic fields are well typed.

Failure criteria:

- any nonstrict endpoint accepted;
- an \(h=2\) endpoint derived from a nonsaturated exponent-one prime;
- any trace or determinant emitted outside its legal ideal;
- any source formula copied from Evaluator A.

## Core block B3: maximal order and Weyl asymptotics

Owners: Evaluator A for exhaustive finite optimization/counting;
Evaluator B for prime/Euler/Tauberian derivation. They work independently.

Required Evaluator A evidence:

- exhaustive finite maximizer over all \(h\)-free \(m\le x\);
- comparison of the maximizing label with the independently generated
  largest admissible saturated primorial;
- nested empirical singular counts from raw finite fibers;
- monotone cutoff and precision ledgers.

Required Evaluator B evidence:

- the exact coefficient
  \((h-1)^{\sigma-1}/[2(1-\sigma)]\) in the subcritical logarithm;
- the \(\sigma=1\) Mertens regime and \(\sigma>1\) Euler limit;
- \(F_{h,\sigma}=\zeta G\);
- local uniform remainder orders;
- the exact strip
  \(\Re z>\max(1/h,(1-\sigma)/(h-1))\);
- the positive residue \(C_{h,\sigma}\);
- \(D_{h,\sigma}\) and the eigenvalue constant \(1/\zeta(h)\);
- \(C_{h,1}=D_{h,1}=1\) for every tested \(h\).

Numerical policy:

- precision levels and interval-width targets are frozen before outputs:
  widths are at most (10^{-30},10^{-60},10^{-120}) at 128, 256, and 512
  bits respectively;
- a ratio trend is diagnostic only and never replaces the proof;
- exact symbolic crossover fields must agree byte for byte;
- approximate constants pass only when independently certified intervals
  overlap within the preregistered width.

Failure criteria:

- a nonprimorial finite maximizer not explained by a tie;
- a missing \(h-1\) factor in maximal order;
- a Tauberian conclusion without the strip, positivity, pole, and residue;
- any universal strict ordering of \(C\) and \(D\);
- finite-data extrapolation reported as theorem evidence.

## Core block B4: dual comparison and hostile mutations

Owner: a third comparator with no scientific formula implementation.

The comparator validates schema and types, verifies both sealed manifests,
then reads only the two final scientific projections. It must not
recalculate an expected value. Each projection contains a common namespace
and a method-specific namespace; absence of an analytically exclusive field
from the matrix route, or of a raw matrix field from the Euler route, is not
manufactured into false agreement.

Exact common-field agreement:

- integer, Boolean, rational, finite symbolic-expression,
  comparison-operator, and rejection-code fields in the common namespace
  must match byte for byte;
- no Python-style equality between Boolean and integer is accepted;
- missing, extra, reordered set-valued, or wrong-type common fields reject;
- method-specific fields must match their frozen per-evaluator schemas and
  coverage requirements, but are not compared to a nonexistent counterpart.

Numerical agreement:

- intervals must be finite, ordered, independently derived, and overlapping;
- interval widths must meet the predeclared precision ladder;
- NaN, infinity where not explicitly typed, or post hoc tolerance changes
  reject.

MUTATION_REGISTRY.json is the sole controlling mutation list. Each row has
an exact `target_artifact` and either a resolvable RFC6901 replacement
pointer or one of the three closed typed filesystem operations. Before a
replacement, the runner resolves the pointer in a fresh disposable copy and
requires exact JSON-type and value equality with `value_from`; failure
is HARNESS_ERROR:MUTATION_PRECONDITION_FAILED and therefore a survivor. The
registry atomizes the following summary families into stable IDs with exact
operations, domains, designated-consumer key sets, rejection codes, and
exit 2:

1. Type mutations:
   \(h=1\), noninteger \(h\), \(k=0\), \(q=0\), \(m\notin\mathcal F_h\),
   wrong \(J_h\), map swap, \(\sigma=s\) for nonreal \(s\), index zero,
   finite/infinite fiber confusion.
2. Endpoint mutations:
   change each strict wall to nonstrict, omit \(M\)'s existence wall, permit
   trace at \(k\sigma=2\), permit determinant at \(r\sigma=2\), admit
   saturated similarity at one, admit commutator equality, delete the
   mandatory \(C=D=1\) row.
3. Source mutations:
   alter a Phase-2 hash, substitute a wrong DOI, call the \(h\)-free part
   new, omit any P27--P30/P43 subtraction, restore the superseded universal
   \(C\ne D\) claim.
4. Firewall mutations:
   share an expected table, let one evaluator read the other, count the
   free-UFD clone as positive prime evidence, promote the \(h=2\) singleton
   to a paper, or relabel a Route expectation as an evaluated result.
5. Semantic-type mutations:
   retype a singular value as an eigenvalue or a Riesz-projection norm as a
   probability.
6. Symbolic-AST mutations:
   replace the Dirichlet-power eigenvalue by rational `complexExact`, or
   change the positive-real logarithm branch.
7. Infinite-coverage mutations:
   omit, add, reorder, or inject an undeclared B/P case; give A an infinite
   record; change B/P ownership; alter the canonical set hash; or break the
   per-case hash/verdict closure.
8. Raw-serialization mutations:
   admit `6.0`, `6e0`, Boolean or floating rational components; permit
   duplicate-member last-win; reject harmless key reordering; or trust
   noncanonical stored JCS/hash bytes.

The legal outcome union is ACCEPT, REJECT, or HARNESS_ERROR as typed in
EXPERIMENT_CONTRACT.json. A row is killed only if every and only its
designated consumers return REJECT with that row's exact code and exit 2.
Missing, extra, or duplicate consumers; ACCEPT or zero exit; a wrong code;
HARNESS_ERROR; parse/schema exceptions; timeouts; malformed payloads; and
unclassified nonzero exits are survivors and force HOLD.

## Core block B5: source, firewall, and result-free integrity

Owner: an independent read-only auditor.

Checks:

- verify the Phase-2 manifest and every P45 source hash;
- verify DOI/title/author/year bindings for Luan--Khoi, Carlson,
  de Weger--van de Woestijne, and Abanin--Mannanikov;
- verify explicit P27--P30/P43 ownership subtraction;
- rerun the delete-shared-method test;
- verify the free-UFD clone is classified as a negative control;
- verify both evaluator source manifests are disjoint;
- verify no result existed before both code seals;
- verify the output tree contains no undeclared path;
- verify the authority repository, mirror, registry, and Git state remain
  unchanged.

Before any filesystem read, the auditor rejects absolute paths, parent
segments, symlink components, and nonregular inputs. The exact output
whitelist is evaluator_a.json, evaluator_b.json, proof_auditor_p.json,
comparator_x.json, mutation_outcomes.json, integrity_audit.json,
evaluation_report.json, and the self-excluding results/SHA256SUMS.txt, all
under results/. A parent run stages that complete set, rechecks the target
namespace, and installs it by one same-filesystem atomic directory rename
only after every scientific and integrity gate passes. A forced late
failure must preserve for every target the exact identity tuple
(path,file_type,sha256,size_bytes,mode,mtime_ns); a second complete run must
perform zero physical replacements. Cache, auxiliary-build, bytecode, and
host-path-token artifacts are forbidden. Parse failure, timeout, consumer
exception, malformed payload, unclassified nonzero exit, schema failure,
and I/O failure totalize to the declared HARNESS_ERROR class instead of an
uncaught exception. These rules are exact in EXPERIMENT_CONTRACT.json and
EXPERIMENT_CONTRACT_SCHEMA.json.

Failure of source binding, independence, or repository immutability blocks
scientific release regardless of numerical agreement.

## Metrics and decision thresholds

### C1 passes only if

- all exact finite block identities pass both applicable routes;
- all finite shared fields pass A/B/X, while every strict infinite
  existence, ideal, trace, determinant, and similarity certificate passes
  B and the independent proof auditor P;
- A reports zero infinite records, B and P each report exactly the same
  frozen 15-case C-sorted ledger, and the evaluation report records PASS for
  the case-set hash plus per-case owner/hash closure;
- the entire band \(1/h<\sigma\le1\) is classified with the correct
  similarity split;
- every applicable type and endpoint mutation rejects.

### C2 passes only if

- the exact primorial maximizer and all three asymptotic regimes are present;
- the Tauberian strip, positivity, pole, residue, and inversion are present;
- both Weyl constants and the eigenvalue constant are distinguished;
- every mandatory \(\sigma=1\) row states \(C=D=1\);
- both commutator walls are strict and the \(h=2\) witness is correctly
  typed;
- source and firewall mutations reject.

Finite evidence from A never counts toward an infinite endpoint,
Tauberian, similarity, trace-domain, or determinant-domain acceptance.

### Overall decisions

- GO_EVALUATED: C1 and C2 pass, evaluators are independent, all mutations
  reject, and the source/integrity audit is clean.
- HOLD_REPAIR: a proof-consistent but repairable implementation, source,
  tolerance, coverage, or integrity defect remains.
- STOP_FALSE: a decisive mathematical falsifier is reproduced.
- STOP_DUPLICATE: exact primary prior art absorbs the residual theorem.
- STOP_GENERIC_SPECIALIZATION: only the \(h=2\) saturated case remains.

No GO code authorizes publication, Route B, or authority integration.
These GO/HOLD/STOP codes are external scientific/publication dispositions,
not Route terminals. Only the Route validators own A0--A4, the overall Route
expectation, and Route-B fields.

## Resource and reproducibility plan

- CPU-only execution is sufficient; no GPU is justified.
- Evaluator A uses nested integer cutoffs and moderate dense blocks, with
  exact small cases and high-precision numerical stress cases.
- Evaluator B uses symbolic local factors and arbitrary-precision partial
  products; it records precision and truncation bounds.
- Each run records runtime, OS, interpreter, library versions, source
  manifest, input-generation method, and deterministic ordering.
- A cold relocated rerun must reproduce every exact projection and
  overlapping certified intervals.

## Milestones

1. Seal this preauthority package and obtain root approval for implementation.
2. Assign independent owners and seal two disjoint evaluator source
   manifests before any run.
3. Run B1 and B2 separately; seal outputs without cross-exposure.
4. Run B3 independently on both sides and seal precision/cutoff ledgers.
5. Run the third comparator, all mutation suites, and the B5 read-only audit.
6. Issue an explicit GO/HOLD/STOP evaluation report.
7. Only after a separate root authorization may any authority integration be
   considered.

## Publication and no-result boundary

This file is a plan, not an experiment report. It contains no claimed
measurement, pass count, convergence fit, evaluator agreement, or mutation
outcome. Any later report must be a separately manifested artifact and must
preserve the chronology recorded here.
