# Experiment Plan

## Status

PREREGISTERED / NOT RUN / NO RESULTS

The controlling machine inputs are EXPERIMENT_CONTRACT.json and
MUTATION_REGISTRY.json. Their typed cases, evidence domains, consumer sets,
serialization rules, and transaction policy supersede prose inference.

## Claims under test

### Claim C1 — exact ideal surface

For every tested radix \(b\ge2\) and finite \(q\ge1\), exact digit and shell
controls agree with

$$
B_{b,s}\in S_q
\iff
\sigma>\max\{1,\log_b\kappa_{b,q}\},
$$

with strict rejection at equality and adjacent paired shells used at
\(b=2\).

### Claim C2 — trace and temporal boundary

Positive-vertex controls agree with the digit-restricted trace, legal
\(\det_2\) power ledger for \(\sigma>1\), structural trace vanishing only
at \(b=2\), and least-period sets
\(\{r\ge2\}\) at \(b=2\) and \(\{r\ge1\}\) at \(b>2\).

## Core experiment blocks

### E1. Contract preflight

Validate scalar input types, positive-vertex convention, independent output
locations, exact parent seal, evaluator source separation, and the absence
of result or cache inputs. Reject composite-radix configurations that invoke
Kummer.

### E2. Evaluator A direct run

For preregistered small and medium cutoffs, build the positive-prefix matrix
directly, compute finite singular values and \(S_q\) summaries, multiply
matrices for selected trace powers, and scan graph witnesses. Record
precision and truncation metadata. Do not fit exponents or choose cases
after observing output.

### E3. Evaluator B factorized run

Independently construct digit matrices, exact Kronecker shell norms,
weighted interval bounds, digit-DP loop and closed-word controls, zero
deletion, and explicit period witnesses. Do not read any Evaluator A
artifact.

### E3P. Independent infinite theorem audit

Auditor P independently checks the infinite summations, equality witnesses,
trace/determinant domains, and temporal proofs from PROOF_PACKAGE.md and the
sealed exact identities. A and B are forbidden from emitting infinite
theorem certificates; neither finite cutoff nor finite tensor identity is an
infinite endpoint verdict.

### E4. Canonical comparison

Project native records independently to the frozen canonical schema.
Compare exact fields byte for byte and approximate fields only within their
predeclared enclosures. Produce a mismatch ledger; do not silently coerce a
type or drop a row.

### E5. Hostile mutation suite

Run every atomic source, type, endpoint, ownership, Route, integrity, and
provenance mutation in MUTATION_REGISTRY.json. THEOREM_FALSIFIERS.md is a
human-readable summary, not a second registry. The mandatory scientific
families include:

- \(\sigma=1\) changed from rejected to accepted;
- digit-wall equality changed from rejected to accepted;
- binary same-shell block changed from zero to nonzero;
- binary trace copied to \(b=3\);
- zero word retained in the positive source;
- composite radix labeled by Kummer;
- ordinary determinant enabled below \(\alpha_b\);
- finite cutoff agreement relabeled as proof of infinite membership.

## Preregistered coverage

Use exactly the neutral case IDs, radices, indices, cutoffs, trace powers,
and typed symbolic endpoint rows in EXPERIMENT_CONTRACT.json. This includes
radices \(2,3,4,5\), \(q=1,2,3\), same/adjacent/gapped shells, trace powers
\(r=1,2,3,4\) where legal, and the required deterministic randomized-digit-
mask control. Both implementations independently expand the same raw cases;
no generated case file is shared.

## Metrics

- maximum relative discrepancy in independently computed nonzero finite
  singular values;
- exact agreement of integer ranks, support counts, zero-deletion counts,
  and period labels;
- containment of direct weighted shell norms in the independently derived
  weighted intervals;
- exact agreement of trace-power support counts before weighting;
- overlap of certified trace-power intervals when an exact rational is not
  available;
- mutation kill rate, reported by mutation ID;
- missing, extra, duplicate, or type-invalid canonical rows.

## Success criteria

C1 passes its finite-control layer only if all exact shell identities agree,
all weighted direct norms lie in the predicted intervals, both equality
mutations are killed, and the binary paired-shell row is present.

C2 passes its finite-control layer only if binary and odd-radix trace rows
separate correctly, zero deletion is exact, every requested closed-walk
ledger agrees, period witnesses have certified least period, and
determinant-domain mutations are killed.

Both evaluators must have zero undeclared shared artifacts, and every
mandatory mutation must be killed. Passing remains validation, not proof or
authority.

The infinite C1/C2 statements pass only if auditor P accepts their exact
strict-domain certificates. A/B/X finite outputs cannot satisfy that gate.
Each mutation is killed only by the exact consumer set/code/exit contract in
MUTATION_REGISTRY.json; a crash or infrastructure error is a survivor.

## Failure criteria

Any unexplained scientific mismatch, missing equality row, failed mandatory
mutation, source/type coercion, shared scientific intermediate, result-based
case selection, or attempt to promote cutoff evidence to an infinite theorem
is a hard failure. Numerical instability requires a preregistered precision
escalation; it cannot be resolved by changing the expected value.

## Run order and stopping

Run E1, then E2 and E3 in isolated workspaces, then E3P, E4, and E5. Stop
immediately on contract or independence failure. Scientific mismatches are
preserved and investigated from original native outputs; neither evaluator
may be patched after seeing the other's result without invalidating and
restarting the complete run.

## Output boundary

Future results belong in a separately authorized result namespace. This
package contains specifications only and intentionally contains no matrix
dump, numerical table, plot, evaluator log, or claimed pass.

Future execution must use relative allowlisted paths; reject absolute paths,
parent segments, symlink components, and nonregular inputs before any read.
Stage the complete output set, recheck the target namespace, and install only
after all gates pass. A forced late failure must preserve target bytes and
metadata; a second complete run must make zero physical replacements. Cache,
auxiliary-build, bytecode, and host-path-token artifacts are forbidden.

GO/HOLD/STOP are external scientific/publication dispositions, not Route
terminals. Only strict Route validators own A0--A4, the overall Route verdict,
and Route-B fields.
