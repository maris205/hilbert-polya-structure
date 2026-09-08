# Single AY8 falsification diagnostic

Frozen before execution, 2026-09-08 UTC.

**Purpose.** Test the tentative claim that for nonzero integer $k$ the
origin is the only ordinary integral periodic state. A nonzero cycle
would refute this particular rigidity route immediately; absence of such
a cycle for these inputs proves no all-parameter theorem.

**Exact inputs.** Parameters, in order,
$(-6,-5,-4,-3,-2,-1,1,2,3,4,5,6)$. For each, enumerate exactly the
integer box $[-C_k,C_k]^4$ with $C_k=\max(|k|+1,4)$, using the
seventh-pass proved bound. There is no period cutoff. Retain vertices
with both current-state displayed denominators nonzero and exact forward
edges that stay in the box and in that domain. Extract all directed
cycles by graph traversal. This is new code, not an old-program rerun.

**Expected output.** For each parameter: candidate-vertex and retained-edge
counts, cycle counts by native least period, and one explicit nonzero
cycle if present. Integer arithmetic only; no floating-point decision.
The output is a falsification aid, not independent certification.

**Failure interpretation.** A nonzero cycle rejects the origin-only
conjecture and must be hand replayed before being used. All-origin
output leaves the infinite-parameter claim unproved. A timeout or memory
failure establishes neither outcome; no parameter enlargement is allowed.

**Hard cap.** One mathematical diagnostic, at most 60 seconds CPU and
256 MiB address space, imposed by process resource limits. No GPU,
external model, background launch, optional extension or old rerun.
Execution count starts at zero; each actual execution must be recorded.

**Implementation.** `diagnostic.py` emits JSON to standard output. A
text receipt will record the actual command and result after execution;
the script does not write data files.
