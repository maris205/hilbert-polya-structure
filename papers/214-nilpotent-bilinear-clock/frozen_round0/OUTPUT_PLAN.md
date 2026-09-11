# P214 author output plan — source only

Status: `SOURCE_ONLY / NOT_EXECUTED / NO_CANONICAL / HOLD_RUNTIME`.
This is an author implementation contribution, not an independent manuscript
review or a review-eligibility claim. No execution, import, compile, science
result, canonical output, runtime binding or build is supplied by this plan.

## Authority and scope

The accepted [theorem contract](../../docs/papers211_215_sequence/qa/fresh55_root_reception01/THEOREM_CONTRACT.md)
and original [Fresh55 proof](../../docs/papers211_215_sequence/scouting/finite_residual_fresh55/PROOF_PACKAGE.md)
control the mathematics. [PARAMETERS.json](PARAMETERS.json) freezes exactly
the Cartesian box `q=(2,3,4)`, `m=(2,3,4)`, ordered by increasing q and then m.
There is no command-line selector or enlargement. The embedded constants
in [verify.py](verify.py) implement this box;
PARAMETERS.json is a documentary mirror and is not opened by the program.

Deductively expected state/target counts are 4, 16, 64, 9, 81, 729, 16, 256,
4096, totaling 5271. These numbers are arithmetic predictions, not observed
results. Finite checks pressure the all-parameter proofs; they do not prove
those theorems or establish priority, nonlinear-factor absence, or a general
functional-graph classification. The inverse mechanism and linear clock
shape remain explicitly deducted as in the contract.

## Dependencies and I/O boundary

The source is standalone Python 3.8-or-later code with the sole explicit
`import sys`, plus Python builtins. Its local `wire`/`wire_string` helpers
encode the proved P214 value domain without importing json or another codec.
It imports no local project module, third-party package, optional accelerator,
or data file. sys retains the existing argv/stdout/exit behavior unchanged.
The interpreter, startup machinery, sys implementation, stdout configuration
and other selected runtime dependencies still require separate binding.
Removing the json dependency is not a claim that the current runtime or
any prior 19-role dependency key has already been accepted for this source.

The program does not call open, inspect cwd, read stdin, query environment
variables, load PARAMETERS.json/schema, create directories, start subprocesses,
use the network, or write application files. `sys.argv` is read only to reject
all supplied arguments; `sys.stdout` is the sole intentional application
output destination. The source contains the usual `__main__` guard, but no
import or compile action is authorized by its existence. Import-time Python
behavior, bytecode/cache effects and stdout capture are host/runtime-policy
questions, not application-level closure demonstrated here. A later receiver
must separately settle interpreter identity, startup/site/environment policy,
working directory, imports, bytecode policy, exact source/parameter/schema
pins, stdout/stderr capture, exit status and output destination. No proposed
shell invocation in this package doubles as a runtime grant.

## Exact arithmetic and independent observation route

Field elements for q=2,3 are residues. For q=4 the code labels 0,1,2,3 mean
0,1,alpha,1+alpha in F2[alpha]/(alpha^2+alpha+1): addition is bitwise XOR,
and multiplication is binary polynomial multiplication reduced by `0b111`.
It is not integer arithmetic modulo 4. Complete tables, inverse tables,
field-axiom checks and the alpha-square/characteristic-two anchors are emitted.

A ring element has integer code `sum(c_i*q**i)` with coefficient degree
ascending. Ring multiplication is direct coefficient convolution truncated
at degree m. I consists of the codes divisible by q. Put nI=q^(m-1); the
state ID of (x,y) is `(x_code//q)*nI+(y_code//q)`. IDs enumerate x first and y
second in ascending integer order. The complete ring code/coefficient/valuation
dictionary and ideal code list are included in each carrier record.

The program builds literal F, L=(y,tx), and M=(y,xy) transition arrays by ring
arithmetic over every state. Each F/L orbit is then independently walked
through its transition array until a state repeats. Neither valuation nor
the proposed 2m-2 bound is used for orbit stopping or for the observed depth.
Depth is the first index of state ID zero if present; its absence fails the
claim checks. The stored path includes the final repeated state. The detected
cycle is the nonrepeated cycle segment, with its starting index and period.

F predecessor buckets are built only by inverting the complete literal
transition array. Independently, every target obtains d=min(v(t+u),m-1),
reachability, the kernel ideal and a constructed representative. In the
nonsaturated reachable case, canonical coefficient shifts form e=(t+u)/t^d
and w0=w/t^(d+1); a coefficient-recursion inverse of e gives x0=t e^-1 w0.
No literal predecessor is selected to construct x0. Saturated reachable
targets use x0=0 and the entire ideal I; unreachable targets have no x0 or
coset. The whole sorted coset list, including its multiplicities, must equal
the exhaustive predecessor bucket. This detects duplicates as well as missing
or extra predecessors. All target records, including empty fibres, are kept.

P and Q and their inverses are emitted as complete permutations. The program
checks F=QMP pointwise and transports all M predecessor buckets through
P^-1 at Q^-1(target). Q differs from P^-1 already at zero; this is a warning
against reading the adapter as a conjugacy, not a claim that the inequality
alone rules out every other conjugacy.

## Complete claim coverage

Each emitted scientific record contains a `checks` object. A key is recorded
as true only after its exact comparison has succeeded. Repeated checks with
the same name (for example every coefficient-field triple) are counted in
the final `check_counts`; within a record the name appears once. Failed
comparisons emit a separate failure record and terminate nonzero, so partially
emitted scientific records never count as a complete accepted result.

- Every state: encoding, closure, product valuation, later t^2 containment,
  cancellation-safe valuation chains, actual full orbit, recurrent sink/period,
  clock equality, maximum-depth characterization, QMP identity, independently
  walked linear-control clock and, only for m=2, F=L=(y,0).
- Every target: literal predecessor list, reachability, kernel size/equation,
  full constructed coset equality, fibre size, representative validity and
  equation, nonsaturated unit inverse, saturated boundary, and full QMP fibre
  transport. Both v(t+u)=m-1 and t+u=0 use the saturated branch.
- Every h from zero through 2m-2: exact and cumulative state-ID lists, the
  valuation-ideal rectangle, exact count (including the h=0 special case),
  cumulative q^h, and exact equality to independently observed L depth sets.
- Every fibre size in the claimed support, including zero: complete target-ID
  lists, predicted lists and census counts. Empty fibres use d=0 as a census
  row label only; actual target d is always at least one.
- Every carrier: unique recurrent and fixed sets, zero sink, sharp depth and
  its full maximizing set, full image and its size, maximum-fibre target set
  exactly (-t+c*t^(m-1),0), q saturated targets, predecessor partition and
  mass, and the explicitly cancellation-challenging seed (t,-t).
- At m>=3 only: the full predecessor sets at (0,0) and (-t,0) witness unequal
  positive sizes q and q^(m-1); (t,t) additionally witnesses literal F != L.
  The deductive finite-group-endomorphism obstruction is not an enumeration
  over groups. At m=2 both witness fields are null and no such claim is tested.

## Deterministic JSONL protocol

[OUTPUT_SCHEMA.json](OUTPUT_SCHEMA.json) defines the record grammar and
[OUTPUT_SCHEMA.md](OUTPUT_SCHEMA.md) explains every field. On a
successful execution, the source is designed to emit this exact sequence:

1. One `run_start`.
2. For each q, one `field`, then for each m: one `carrier`, one `adapter`,
   all state records in ascending ID order, all target records in ascending
   ID order, all `depth_row` records in ascending h, all `fibre_row` records
   in ascending d, and one `carrier_complete`.
3. Exactly one `run_complete`, only after every check succeeds.

The expected counts are 1 run_start, 3 field, 9 carrier, 9 adapter, 5271 state,
5271 target, 45 depth_row, 27 fibre_row, 9 carrier_complete, 1 run_complete:
10646 records. These are unobserved protocol expectations. Every successful
record is serialized by the local builtin-only encoder using sorted string
keys, compact separators, exact ensure_ascii spelling and one newline. The
proved value domain has no floats or NaN/Infinity; outside-domain values are
rejected rather than assigned a new scientific encoding. All numeric scientific
values are integers; no floats, timestamps, PIDs, paths, host names or hash
summaries enter the successful stream. Lists follow the declared order.

`run_complete.preceding_record_counts` excludes the run_complete record itself;
`check_count` includes all comparisons, including final coverage checks.
Its `FINITE_BOX_CHECKS_PASSED` string is prospective executable behavior, not
a result asserted by this source handoff. Exit zero requires this final
record. A `verification_failure` has the failed scope/name/actual/expected
values and exits 1. A caught unexpected exception emits `runtime_error` and
exits 2. Either terminates without run_complete. Interpreter/import failures
or an unusable stdout can occur outside this application-level JSONL guarantee
and must still be captured as failed runtime evidence, never accepted output.

## Later output acceptance, not authorized now

No canonical is created in this source stage. The future `CANONICAL.json`
is a historical role filename containing JSONL, NOT one JSON object. A later
grant may select a complete raw JSONL transcript for that role, preserving every record above,
not a hash, a histogram alone or the final summary. Its receiver must validate
ordering, exact record multiplicities, all nested schemas, ID bounds,
cross-record correspondence, the final status, empty stderr as required by
the chosen runtime contract, successful exit and all frozen inputs. A second
separately authorized execution and complete raw-byte comparison may then
support deterministic replay. This plan provides neither run nor comparison.
