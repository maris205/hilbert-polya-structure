# Methodology Blueprint

## Aim

Build falsification-first evidence for two claims without allowing finite
controls to substitute for the infinite proof:

1. the exact all-radix finite-\(q\) Schatten surface, including both
   equality mechanisms;
2. the positive-vertex trace, power, determinant-domain, and least-period
   boundaries.

No experiment is run at this preauthority stage.

## Evaluator A — direct positive-prefix operator

Evaluator A receives only a scalar configuration record
\((b,q,\sigma,N,r,\text{precision})\).

1. It represents the vertices \(1,\ldots,N\) as ordinary integers.
2. It decides carry freedom by repeated quotient and remainder during direct
   addition; it does not import \(C_b\), Kronecker factors, shell formulas,
   or a digit-DP table.
3. It builds the weighted positive-prefix matrix directly.
4. It computes singular values with an independently chosen dense or sparse
   numerical backend, and computes traces of powers by matrix
   multiplication.
5. It separately scans diagonal entries and graph cycles to record trace and
   least-period controls.

Evaluator A tests the actual finite restrictions of the frozen
positive-vertex operator. It is not permitted to infer an infinite theorem
from convergence plots or to emit infinite endpoint, ideal, determinant, or
least-period classifications.

## Evaluator B — shell tensor and digit automata

Evaluator B receives the same scalar configuration fields through a
separately parsed file, but no file created by Evaluator A.

1. It constructs \(C_d\) from the predicate \(a+c<d\).
2. It derives unweighted shell norms from repetition vectors and Kronecker
   factors, never materializing the full positive-prefix matrix.
3. It computes the uniform weighted upper and lower envelopes from the
   shell endpoints.
4. It uses an independently implemented digit automaton for loop and
   closed-walk controls, with explicit deletion of the all-zero word.
5. It constructs period witnesses from distinct digit positions rather than
   scanning Evaluator A's graph.

Evaluator B owns no fixture containing a predicted norm, trace, or period.
It recomputes every prediction from the mathematical specification.
Like Evaluator A, it owns finite controls only; its exact shell identities
may be evidence read by the proof auditor but do not themselves carry an
infinite theorem verdict.

## Independent infinite theorem auditor

Auditor P reads the frozen proof package, the exact finite identities sealed
by A and B, and the neutral typed contract. It independently checks the
infinite shell summations, strict endpoint divergence witnesses, trace and
determinant ideal domains, and least-period proof. Only P may emit an
INFINITE_THEOREM_CERTIFICATE. It imports neither evaluator implementation
and treats finite numerical behavior as a falsifier, never as proof.

## Independence firewall

The evaluator implementations must use different source trees, module
namespaces, dependency lockfiles, random-access conventions, and test
fixtures. They may not share:

- source code or helper libraries;
- serialized matrices, digit words, shell factors, expected tables, seeds,
  cache files, or intermediate results;
- generated configuration expansions;
- logs before the final comparison.

The only common inputs are the hand-audited EXPERIMENT_CONTRACT.json and
MUTATION_REGISTRY.json. Each evaluator independently parses and expands the
neutral scalar cases and writes its own native output. Generated expansions,
seeds, fixtures, and expected values may not be shared. A third,
non-scientific comparator projects both finite outputs to a versioned
canonical schema and compares canonical bytes. The comparator performs no
arithmetic beyond type validation, sorting, decimal normalization, and
stated tolerance checks.

## Canonical scientific projection

Each evaluator must independently emit:

- configuration identity and source-object type;
- zero-included or zero-deleted convention;
- ordered singular-value summaries for specified finite controls;
- shell indices and \(S_q\)-norm summaries;
- trace-power values for requested lengths;
- least-period witness or rejection status;
- precision and rounding metadata.

Infinite legal-domain and endpoint labels are excluded from the A/B common
projection and belong only to P's theorem-certificate namespace.

Exact integers and rational bounds are serialized as strings. Approximate
values include precision and an error enclosure. Records are ordered by the
complete tuple \((\text{case id},b,q,\sigma,N,r,\text{control},k,\ell,
\text{mask depth},\text{mask integer},\text{precision})\) under bytewise C
ordering. Non-shell and non-mask coordinates are explicit JSON nulls, so no
two expanded rows share an identity.

Finite trace powers are records with either an exact reduced rational and a
null interval, or a null exact value and a certified closed interval. This
includes odd-radix, nonintegral-\(\sigma\) traces containing radical terms.

## Required controls

- binary and odd-radix cases;
- a composite radix, ensuring the edge relation is direct and not Kummer
  derived;
- same-shell and adjacent-shell blocks;
- zero-included digit tensor and zero-deleted positive graph;
- the two equality surfaces;
- trace class versus Hilbert–Schmidt-only domains;
- ordinary determinant versus \(\det_2\);
- support periods versus complex trace values;
- deterministic randomized-digit-mask controls, with all finite mask/tensor
  behavior assigned zero novelty credit.

## Exact hostile-outcome contract

MUTATION_REGISTRY.json is exhaustive for this freeze. Each atomic row fixes
a stable ID, exact target and from/to payload, semantic domain, every and
only designated consumer, exact rejection code, and required exit 2. The
legal outcome union is ACCEPT, REJECT, or HARNESS_ERROR. A mutation is killed
only if each designated consumer and no other consumer returns REJECT with
the exact row code and exit 2. Missing, extra, or duplicate consumers;
ACCEPT/zero exit; wrong code; HARNESS_ERROR; exception; timeout; malformed
payload; or unclassified nonzero exit is a survivor and forces HOLD.

## Interpretation rule

Agreement supports only consistency of the finite controls with the exact
proof. Disagreement is informative and blocks progression. Agreement cannot
establish priority, replace endpoint proofs, or authorize repository
integration.
