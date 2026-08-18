# Methodology blueprint

## Workflow contract

This temporary package applies two explicit constraints:

1. the proof-writer contract: normalize every claim, state every assumption,
   classify proof status, isolate substantial lemmas, and downgrade rather
   than hide a gap;
2. the experiment-plan contract: at most two central claims, a compact set of
   claim-linked validation blocks, explicit success/failure criteria, and no
   fabricated result.

The concrete workflow is:

1. verify the sealed Phase-2 bytes;
2. freeze $q,A,N$, cutoff, logarithm, and $q$-adic conventions;
3. return all leading multiplicative-SFT results to primary owners;
4. derive the exact finite-$N$ increment before taking any limit;
5. prove Perron decay and the exact residue series;
6. prove both inclusions in the complete accumulation-set equality;
7. prove golden separation with an exact algebraic bound, not sampled data;
8. prove dimension by cylinder separation and a Frostman measure;
9. prove radial singularities with a dominated Abelian limit;
10. specify two independent evaluators and literal hostile mutations;
11. freeze self-excluding hashes before independent review.

No cross-model or external-review result is represented in this candidate.
Independent DA remains required.

## Claim map

| ID | Claim | Evidence type | Status |
|---|---|---|---|
| C1 | exact finite-size remainder extends to $\mathbb Z_q$ and has image equal to all accumulation values | direct proof plus two planned exact evaluators | `PROVED_CANDIDATE` |
| C2 | golden image is a Cantor set of exact dimension and $G$ has dense radial singularities | Binet/algebra, Frostman, Abelian limit | `PROVED_CANDIDATE` |
| A1 | chain product, entropy, and leading dimensions are candidate novelty | primary-source audit | `REFUTED / ZERO_CREDIT` |
| X1 | ordinary Minkowski content fails to exist | no continuous-scale proof | `EXCLUDED` |

## Proof architecture

```text
q-adic chain partition
  -> exact product and one-site increment
  -> primitive Perron decay of d_v
  -> exact valuation summation by parts
  -> uniformly convergent residue series on Z_q
  -> complete accumulation image

golden Binet formula
  -> exact positive a_m expansion of gamma_k
  -> one algebraic infinite-tail bound
  -> alternating sign + strong separation + ratio
  -> Cantor topology + Hausdorff/box dimension
  -> nonzero dyadic radial coefficient tails
  -> unit-circle natural boundary
```

Each arrow has a named lemma and a decisive falsifier.

## Evidence labels

- `PROVED_CANDIDATE`: complete local proof, not yet independently accepted.
- `KNOWN_PRIMARY_SOURCE`: explicit prior ownership, zero novelty credit.
- `DIRECT_COROLLARY`: locally proved but not a novelty anchor.
- `CERTIFIED_EVALUATOR`: exact integer or outward-rounded interval evidence.
- `MUTATION_EXPECTATION`: a prediction to be run, not a claimed result.
- `NOT_CURRENTLY_JUSTIFIED`: missing proof; must not enter theorem text.
- `STOP_DUPLICATE`: exact primary collision removes standalone status.
- `STOP_SCOPED`: mutation changes the frozen object or quantifier.

## Two-evaluator independence contract

### Evaluator A: direct finite-prefix route

- enumerate alphabet assignments for small $N$;
- check each edge $n\to qn$ directly;
- output only exact integers $Z(N)$ and exact rational increment pairs;
- derive residue-class observations directly from the integer cutoff.

### Evaluator B: chain/Perron/Binet route

- compute $W_\ell$ by exact matrix powers;
- compute chain-length histograms and their product independently;
- evaluate boundary coefficients from a separately implemented Binet series
  with certified algebraic/interval tails;
- evaluate radial coefficients in cyclotomic arithmetic from the residue
  generating functions.

Both evaluators may read the immutable `RAW_INPUT_MANIFEST.json`. It contains
only source configurations, exact scalar budgets, precision levels, and
deterministic digit-stream formulas; it contains no expected output or
expanded fixture. Each evaluator must parse and expand it independently.

The evaluators may agree only after canonical projection to:

```text
(q, serialized A, N, exact Z(N), exact increment numerator/denominator)
```

or to certified intervals carrying their precision and tail certificate.
They may not share source files, helper functions, expanded/generated
fixtures, expected values, serialized intermediates, or random seeds.

## Controls

### Positive controls

- one-symbol $A=[1]$: $Z(N)=1$, $h=0$, and $E\equiv0$;
- full $d$-shift $A=J_d$: $Z(N)=d^N$, $h=\log d$, and $E\equiv0$;
- golden small-$N$ integer ledger in `EXACT_WITNESS_LEDGER.md`;
- two independent formulas for every $\gamma_k$;
- exact relation between $\gamma_{v-1}$ and the level-$v$ radial tail.

### Assumption and type controls

- $q=1$, zero adjacency, reducible adjacency, and periodic adjacency;
- additive edge $n\to n+q$ substituted for $n\to qn$;
- prefix indexing shifted from $[1,N]$ to $[0,N)$;
- Perron subtraction removed;
- `mod` replaced by floor or fractional part;
- representatives that fail to tend to infinity;
- golden sign $r=-t$ mutated to $r=+t$;
- boundary-image dimension confused with original-shift dimension;
- radial singularity retyped as an isolated pole;
- ordinary Minkowski content inserted without a scale proof.

Literal mutation IDs and expected failures are in
`THEOREM_FALSIFIERS.md` and `EXPERIMENT_PLAN.md`.

## Literature protocol

Primary sources are assigned component ownership before any novelty
assessment. General method neighbors are separated from exact same-object
collisions. Search-result absence is never converted into a priority claim.
An exact later-discovered source triggers `STOP_DUPLICATE` without changing
the correctness of the local proof.

## Governance protocol

- Phase 2 freezes a scientific position only.
- This directory is outside the authority and repository paper trees.
- The provisional candidate label is not a registry claim.
- `ROUTE_EXPECTATION.yaml` is a conservative expectation, not a Route run.
- Only root governance may authorize copying, integration, paper writing, or
  Git operations.
