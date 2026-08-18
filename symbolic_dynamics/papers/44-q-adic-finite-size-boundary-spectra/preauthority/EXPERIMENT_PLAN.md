# Deterministic experiment and falsification plan

Plan date: `2026-08-18 UTC`

Status: `PLAN_ONLY / NO RUN RESULT CLAIMED`

## 1. Claims and anti-claims

### Primary claim C1: exact finite-size and q-adic boundary theorem

For every frozen integer $q\ge2$ and finite primitive zero-one $A$, the
one-site increment and residue formula are exact; the residue series extends
continuously to $\mathbb Z_q$ and its image is the complete subsequential
limit set.

### Primary claim C2: golden geometric and analytic closure

For the frozen binary golden adjacency, the boundary coefficients strongly
separate with scale $\varphi^{-2k}$, the image dimension is
$\log2/(2\log\varphi)$, and the same nonzero coefficient tails are the radial
singularity coefficients at primitive dyadic roots.

### Anti-claims

- `AC1`: finite numerical agreement proves neither uniform convergence nor a
  complete accumulation theorem.
- `AC2`: the chain product, entropy, Fibonacci counts, and leading dimensions
  are not new candidate contributions.
- `AC3`: no ordinary Minkowski-content conclusion follows from the dyadic
  boundary theorem.
- `AC4`: $G$ is not a dynamical zeta or determinant, and its dense boundary
  singularities are not isolated meromorphic poles.

## 2. Deterministic fixture universe

There is no train/validation/test split and no fitted parameter. The analogue
is a predeclared fixture partition:

| Partition | Fixtures | Purpose |
|---|---|---|
| positive controls | $A=[1]$; $A=J_2,J_3$; golden $A$ with $q=2$ | exact known outputs |
| theorem-domain probes | primitive binary matrices; selected primitive $3\times3$ matrices; $q\in\{2,3,4,6\}$ | composite-radix and non-golden checks |
| scope controls | zero, reducible, and periodic matrices; $q=1$ | validator must reject theorem label |
| formula mutations | named `MUT-*` transformations | verify that distinct proof dependencies are observable |

`RAW_INPUT_MANIFEST.json` is the sole neutral shared input. It serializes
only raw row-major matrices or deterministic matrix-generation rules,
scalar budgets, precision levels, and digit-stream formulas. It contains no
expected value or generated fixture. Evaluator A and Evaluator B must parse
and expand it independently and may not read one another's expansions,
outputs, or expected tables.

The result-free expansion rule is normative: expand each configuration's
generated matrices across every listed $q$ and every integer
$1\le N\le\texttt{resolved\_max\_N}$, deduplicate exact
$(q,\dim A,\operatorname{rowmajor}(A),N)$ tuples, and sort them by the key
frozen in the manifest. Duplicate configuration IDs/scopes are provenance
only. Digit streams use every $q\in\{2,3,4,6\}$ and every depth
$j\in\{1,\ldots,10\}$, with depth $j$ meaning digits
$a_0,\ldots,a_{j-1}$.

## 3. Core evidence blocks

The plan contains five core blocks. No later optional analysis may replace a
failed `MUST` block.

### B1 — exact prefix and increment census (`MUST`, supports C1)

Evaluator A directly enumerates all alphabet assignments on $[1,N]$ and
tests every edge $n\to qn\le N$. Evaluator B computes exact $W_\ell$ by
integer matrix powers, independently constructs $C_\ell(N)$, and multiplies
$W_\ell^{C_\ell(N)}$.

Initial budget:

- dedicated golden configuration through $N=20$; its appearances in the
  all-primitive binary census are deduplicated canonically;
- all primitive binary matrices through the largest $N$ for which direct
  enumeration uses at most $2^{24}$ assignments, hence through $N=24$;
- selected $3\times3$ fixtures through a predeclared assignment cap;
- $q=2,3,4,6$ to exercise composite $q$.

Canonical comparison is exact integer $Z(N)$ and the reduced rational ratio
$Z(N)/Z(N-1)$. No logarithms are used.

Success: every valid fixture agrees, W0--W5 reproduce exactly, and each
source-changing mutation is rejected or produces its predicted mismatch.

Failure: any valid exact mismatch is F1 and stops C1. Resource exhaustion is
`INCONCLUSIVE`, not failure or success.

### B2 — residue formula and complete-image mechanism (`MUST`, supports C1)

Route A converts the direct increment list into the coefficient sequence
$A_j(N)-N(q-1)/q^{j+1}$. Route B independently expands the residue
summation-by-parts expression into the coefficient sequence stated in W6.
Compare every predeclared initial coefficient exactly and separately have
both implementations verify the symbolic all-$j$ rule. For numerical values
of the full remainder, each evaluator must supply its own certified Perron
tail enclosure; the infinite entropy tail may not be replaced by a finite
formal-log basis.

Separately, predeclare q-adic cylinders $x\bmod q^j=a_j$ and check the
representatives

$$
N_j=a_j+q^j
$$

for monotone lower bound, residue compatibility at every $v\le j$, and exact
agreement of all level-$v$ truncated boundary sums. Include ordinary integer,
$-1$, alternating-digit, and the deterministic polynomial digit stream
frozen in `RAW_INPUT_MANIFEST.json`. No random or shared generated seed is
used.

Success: exact coefficient agreement, overlapping independently certified
full-remainder enclosures, and every representative invariant holds.
Failure: a valid mismatch is F2 or F4. Finite cylinders cannot by themselves
establish surjectivity; the proof of uniform convergence remains mandatory.

### B3 — golden coefficient separation and dimension scales (`MUST`, supports C2)

Evaluator A computes $d_v$ from Fibonacci ratios and evaluates

$$
-\sum_{v\ge k+1}(d_v-d_{v-1})2^{k-v}
$$

using outward-rounded intervals plus an analytic Fibonacci/Perron tail.
Evaluator B independently evaluates the positive-$a_m$ Binet series, using a
separate arbitrary-precision library or exact rational bounds in
$\mathbb Q(\sqrt5)$.

Both must independently certify W7 and W8. The exact algebraic checker must
reproduce $99044>0$. At increasing depths, report cylinder count, maximum
diameter, and minimum gap only as diagnostics; the dimension remains a proof
consequence of uniform constants.

Success: disjoint-code certified intervals overlap for every tested
$\gamma_k$, both prove the prescribed tail enclosures, and the exact W8
certificate passes.

Failure: disjoint certified intervals trigger F5/F6 investigation. A
floating-point-only mismatch is `INCONCLUSIVE`.

### B4 — cyclotomic radial coefficient (`MUST`, supports C2)

Evaluator A obtains the coefficient from the certified $\gamma_{v-1}$ tail.
Evaluator B works in an exact cyclotomic representation, evaluates
$P_{2^w}(\xi)=-2^w/(1-\xi)$ for all contributing $w\ge v$, and bounds the
remaining $\Delta_w$ tail independently.

Predeclare $1\le v\le10$ and at least one primitive root per level. Radial
samples $r_0\uparrow1$ are diagnostic only; the canonical output is the
certified coefficient interval or exact cyclotomic expression.

Success: the two routes agree after projection to the same cyclotomic basis,
`MUT-POLELEVEL` is detected for a level at which the omitted tail is nonzero,
and `MUT-RADIALXI` fails exactly at $Q=4$, $\xi=i$.

Failure: a certified mismatch is F8 and stops the analytic corollary.

### B5 — mutation, ownership, and independence audit (`MUST` gate)

Run every literal mutation in `THEOREM_FALSIFIERS.md`. Record whether it is
rejected by typing, disagrees with an exact control, invalidates a proof
certificate, or survives. A surviving mutation is acceptable only if the
ledger predicted survival and it does not alter the claim.

The falsifier ledger freezes the exact designated-consumer key set and exact
nonzero rejection code for every mutation. Every and only those keys must be
present in the observed record. A mutation survives if a designated consumer
is missing, an unlisted key is present, a consumer accepts/returns zero, the
code differs, or the consumer raises an uncaught exception instead of
returning its typed envelope.

Independence is audited by file/module hashes, import graphs, fixture-access
logs, and separate expected-output embargoes. Search all prose for forbidden
ownership and scope transfers.

Success: every high-risk mutation is detected at the stated layer; no shared
implementation or expected table crosses the evaluator boundary; all
prior-owned components remain zero-credit.

Failure: `MUT-EVAL` invalidates the entire two-evaluator comparison;
`MUT-OWNER`, `MUT-CONTENT`, or `MUT-MERO` blocks package freeze until repaired.

## 4. Run order and first-run matrix

| Run | Blocks | Purpose | May proceed if failed? |
|---|---|---|---|
| M0 | B5 contract-only | input/type/ownership lint before computation | no |
| M1 | B1 | exact object and increment | no for C1/C2 |
| M2 | B2 | residue and q-adic representative mechanism | no for C1 |
| M3 | B3 | golden separation and scale | no for C2 |
| M4 | B4 then B5 full | radial tail and adversarial closeout | no for C2/freeze |

The actual state of each run is recorded only in `EXPERIMENT_TRACKER.md`.

## 5. Resource and reproducibility budget

- hardware: ordinary CPU; no GPU required;
- exact enumeration cap: predeclared by assignment count, never changed in
  response to agreement or disagreement;
- arithmetic: integers, rationals, exact $\mathbb Q(\sqrt5)$, cyclotomic
  arithmetic, and outward-rounded arbitrary precision;
- precision ladder: predeclare at least 128, 256, and 512 bits for interval
  overlap diagnostics;
- randomness: none for inference; if fixed digit streams use a PRNG, record
  generator, version, and seed before outputs are exposed;
- artifacts: source, command, environment lock, stdout/stderr, canonical
  results, and SHA-256 manifest for each evaluator separately.

No benchmark number, execution time, agreement rate, or mutation score is
claimed by this plan.

## 6. Decision rules

`VALIDATION_GO` requires all of B1--B5, evaluator independence, exact source
ownership subtraction, and no decisive falsifier.

`VALIDATION_HOLD` is the current execution state and applies to missing
evaluator implementation/independence, missing certified tails, unimplemented
mutations, or resource-limited direct enumeration. A positive preauthority
theory/source DA does not change this execution state.

`THEOREM_STOP` applies to an exact valid-domain counterexample. `STOP_DUPLICATE`
applies to an external same-object theorem and affects standalone positioning,
not the mathematical truth of the local derivation.

Ordinary Minkowski content remains excluded under every validation outcome.

## 7. Minimal publication-facing evidence set

If later authorized, the smallest adequate evidence package is:

1. the formal proof and source subtraction;
2. B1 exact integer cross-checks;
3. B3 exact algebraic certificate and independent interval check;
4. B4 exact cyclotomic-tail cross-check;
5. a complete mutation and evaluator-independence ledger.

Plots and large cutoff tables are optional diagnostics, not central evidence.
