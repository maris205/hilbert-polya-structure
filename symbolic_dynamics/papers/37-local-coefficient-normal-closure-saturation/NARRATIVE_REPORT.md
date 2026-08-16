# Paper 37 narrative report — SD-C39

## 1. The obligation left by Paper 36

Paper 36 showed that filling every affine Cayley relation cell is too strong:
the filled complex is contractible, and the original unit edge marker does not
descend. The only eligible repair was to keep the full paths and marker and
move cancellation into finite-rank coefficients on the same damped Hashimoto
operator.

Paper 37 tests that repair at the complete primitive matrix Euler factor, not
at one trace or after a scalar specialization.

## 2. The ordinary obstruction

An ordinary local system has invertible parallel transport. Its holonomy
around a primitive orbit is therefore invertible. For the analytic operator,
the edge transports are uniformly bounded; the frozen generator-role fixture
has this property automatically. Yet

```text
det(I-tW)=1  iff  W is nilpotent.
```

An invertible ordinary holonomy cannot delete even one factor. The analytic
operator is sound—the damping gives a trace-class matrix Hashimoto operator on
the original shift—but the desired cancellation cannot occur in the ordinary
branch.

## 3. The graded near miss

A graded pair can match characteristic polynomials without trivial holonomy.
The frozen shear connection uses

```text
A=[[1,1],[0,1]],  B_+(r)=[[1,0],[r,1]],
B_-(r)=[[1,0],[-r,1]].
```

It cancels the defining affine relator, every conjugate, and every repetition
at all orders. This is the strongest positive result in the paper and earns
`A2_ANALYTIC_DETERMINANT`: one same-object matrix Fredholm trace-log exists on
the unchanged graph-step marker.

The success is incomplete. The primitive closed word

```text
M_r=bar(u)^r v bar(u)^(r-1) v u bar(v)^2
```

has graded first trace `-4r^4(r-1)`. It leaks for every `r>=2`, including the
composite baseline.

## 4. The saturation fork

Every closed Cayley label lies in the normal closure of the defining relator.
Cancelling individual conjugates does not cancel arbitrary products—the shear
witness proves this. Requiring every mixed product to cancel, however, covers
every closed path. Then every primitive term vanishes and `Z_gr(z)=1`.

The paper's central visual is therefore

```text
ordinary invertible transport  -> no direct factor deletion
graded direct-cell matching    -> explicit mixed relation leakage
full normal-closure saturation -> every closed factor erased
```

There is no selective point that both removes the complete relation ledger and
retains a nonzero source-proved arithmetic primitive factor.

## 5. Object and language firewalls

Three objects remain distinct throughout:

1. an ordinary trace-class matrix Hashimoto determinant;
2. the explicit ratio of independently owned even and odd determinants;
3. a flat local system on the filled contractible Cayley `2`-complex.

A non-flat coefficient rule on the unfilled graph is an edge connection, not
a local system on the filled complex. Backtracks are excluded by the
Hashimoto rule before coefficients act. A nilpotent endomorphism is a useful
control but not invertible parallel transport.

## 6. Exact evidence

The canonical source/evaluator integration reproduces `131/131` exact checks
and passes `32/32` integration tests. All `8/8` affine direct factors cancel
and all `8/8` rows have a mixed primitive leak in the bounded census. The six
fixed mutations are retained. Random one-relator controls produce `9/48`
direct matches and `9/9` subsequent leaks. In `2/24` paired two-relator
controls both direct factors match, and both presentations still leak.

Fresh A/B and isolated cold C reproduce scientific, source-packet, and Route
bytes exactly; the cold copy is removed. Absent, null, empty, and populated
metadata and both simulated manifest states preserve scientific and Route
bytes. The second primary materialization is byte-identical. The exact result
set has `26` files, the full audit passes `82/82`, and all `39/39` immutable
ledger entries verify. The scientific SHA-256 is
`b17967f294da018e2e045ae70ac7731f5612f4bd4693115ea33dbaebb7fc0d6e`;
the ledger SHA-256 is
`8f47abf523451e1fdb84363d7a1b85b1009bc6e619700389959f4b39f01b8b6e`.

These finite rows test formulas, source/evaluator separation, and generic
controls. The trace-class, nilpotence, arbitrary-rank, and normal-closure
statements remain independently proved.

## 7. Decision and successor

The affine exponent is structural (`A0`). Partial cancellation does not
isolate recurrence and full saturation erases it (`A1`); generic controls
confirm that the partial residue is not an arithmetic recognition rule. The
same-object matrix determinant exists (`A2`) but supplies no target analytic
structure (`A3`), and no fixed self-adjoint carrier, target divisor, or
critical-line mechanism is constructed (`A4`). Hence Route A is rejected and
Route B stays locked.

Paper 38 may change the symbolic object only to the presentation-canonical
Bass--Serre tree geodesic shift of the original ascending HNN splitting, with
its canonical modular cocycle and no auxiliary representation. Another matrix
fixture on the Cayley relation ledger would repeat the closed branch.
