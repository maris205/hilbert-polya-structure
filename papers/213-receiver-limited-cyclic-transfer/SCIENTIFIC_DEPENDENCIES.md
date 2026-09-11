# Scientific source/dependency declaration

Milestone: SOURCE_ONLY_GATE_REQUEST. No scientific execution or parse.

## Complete paper-local scientific source

The only executable scientific source is verify.py, written by the current
paper author. It contains zero import statements, uses no external modules
or data, and reads no file, environment variable, command-line argument,
clock, randomness, network, process list or subprocess. Its hard-coded
parameter constants are declared verbatim in VERIFICATION_PARAMETERS.json;
the JSON is documentary and is not imported or read by the verifier.

Scientific semantics required from a Python 3 implementation are arbitrary
precision integer arithmetic (including //, %, bit shifts and bit_length),
tuple/list/set/dictionary behavior, deterministic range and explicit sorted
order, recursion, generator/list comprehensions, builtin scalar conversion,
exceptions, function calls, __name__, and print with its ordinary stdout.
No floating point operation or non-builtin scientific package is used.

The forward implementation calculates simultaneous min currents literally.
The independent inverse implementation uses comparison-word valley/descent
forcing and long-ascent intervals. word_sources never calls forward and
has no source-carrier feasibility filter. It asserts nonnegative filling,
automatic mass and the precise comparison word before external equality
against graph predecessors. Direct trajectories are traced separately for
each initial state, not reconstructed from the inverse formula.

## Non-executable mathematical/documentary dependencies

The P213 theorem contract, admitted proof and candidate gate/label amendment
govern claim scope. Their exact input pins are in SOURCE_INPUTS.sha256.
PAPER_PLAN, NARRATIVE_REPORT, CLAIMS_EVIDENCE, PROOF_PACKAGE, OUTPUT_SCHEMA,
VERIFICATION_PARAMETERS, SOURCE_AUDIT and the LaTeX sources state proof
and reporting obligations but are not runtime inputs to verify.py.

No old author pilot, gate verifier, old stdout, old canonical or other
paper's scientific source is copied or imported. The gate's executable
was not read in this authoring task. Familiarity with its gate report is
declared; that report is not this author's independent review.

The bibliography's published data and equations are read-only evidence,
not a numerical dependency. No arbitrary-encoding nonconjugacy or global
originality test is encoded.

## Runtime is a separate gate, not implicitly closed

“No imports” is not “no runtime dependencies.” The interpreter, its actual
startup/native support and stdout transport remain a finite runtime-gate
obligation. RUNTIME_PLAN.md intentionally gives them unresolved identities;
no host probe, Python/Node execution, source import, syntax compilation,
AST parse, scientific test, build or Git operation is authorized or
represented as having occurred by this source-only handoff.

Source/parameter acceptance alone does not permit initial execution.
Only an independently accepted finite runtime/launch contract can fix the
actual command and receipt obligations. Do not borrow P212 operational
locks, treat a proposed interpreter name as resolved, or start a recursive
self-observer/bootstrap investigation. An ordinary bootstrap trust boundary
must be explicitly stated by the responsible root gate.

