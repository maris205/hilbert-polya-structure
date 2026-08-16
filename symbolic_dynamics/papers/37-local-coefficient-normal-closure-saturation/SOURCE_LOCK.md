# Paper 37 source lock — SD-C39

Date: 2026-08-15
Family: Symbolic Dynamics only
Route: strict Route A v0.2
Route B: locked

## Candidate

On the formal-reverse right Cayley graph of

$$
M_r=\langle u,v\mid vu=u^rv\rangle^+,
\qquad r\ge2,
$$

retain the full cyclically nonbacktracking oriented-edge Hashimoto shift, one
free marker `z` per original transition, and source-coordinate damping
`d_theta(e)=theta^(1+b(e)+k(e))`.  Test finite-rank invertible matrix edge
connections, including an explicit even/odd grading, without quotienting or
inducing the path space.

## Frozen invariant

The accepted unit is the complete primitive matrix Euler factor

$$
\det(I-q_\theta(\gamma)z^{|\gamma|}W_\gamma)^{-1}
$$

or, only in the explicitly graded branch, the ratio of the independently
owned odd and even factors.  A first trace, scalar specialization, or
aggregate cancellation between distinct primitive orbits is insufficient.

## Frozen theorem target

Prove or refute the simultaneous existence of:

1. an honestly owned same-object matrix Fredholm trace-log;
2. the unchanged unit graph-step marker;
3. all-orders cancellation of every translated, conjugated, mixed, and
   repeated affine relation factor;
4. one nonzero source-proved arithmetic primitive factor; and
5. failure on matched generic presentations.

## Frozen coefficient fixture

For the exact counterexample audit, use rank two in each parity and

$$
A=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad
B_\pm(r)=\begin{pmatrix}1&0\\\pm r&1\end{pmatrix}.
$$

Both sectors map `u` to `A`; even maps `v` to `B_+(r)` and odd maps `v` to
`B_-(r)`.  Formal reverse letters receive exact inverses.  This fixture is
frozen from generator roles and the source exponent before evaluation.

## Parameters and controls

- theorem range: every integer `r>=2`, every `0<theta<1`;
- exact rows: `r=1,...,8`, with balanced `r=1` and composite baseline `r=4`;
- six fixed one-relator mutations;
- 48 deterministic random cyclically reduced one-relator controls, seed
  `370037`;
- 24 paired random two-relator presentations;
- flat balanced parity, traceless invertible, nilpotent, and inverse-edge
  backtrack boundaries;
- power supertraces through order twelve;
- two fresh subprocess runs with `PYTHONHASHSEED=0`.

## Source/evaluator firewall

- Source constructs presentations, words, and frozen matrices only.
- Evaluator independently implements word reduction, affine-group
  evaluation, exact matrix arithmetic, factor comparison, and decisions.
- No unbounded word enumeration is allowed.
- Scientific arithmetic is exact over integers and `fractions.Fraction`.

## Allowed inputs

- affine presentation and semidirect multiplication;
- formal reverse edges and Hashimoto transitions;
- source-coordinate damping;
- finite-rank matrices derived from the frozen source syntax;
- exact generic presentations generated before evaluation.

## Forbidden inputs and repairs

- prime/factor tables, accepted-support predicates, target coefficients, or
  target zeros;
- KMS, GNS, boundary, crystal, vacuum, Fock, or finite-quotient substitution;
- first return, acceleration, `z=1`, changed edge clock, or support projection;
- first-trace-only cancellation;
- an ordinary positive determinant silently replaced by a superdeterminant;
- another arbitrary representation after the frozen fixture fails;
- Route B.

## Frozen hard result

```text
ordinary invertible factor deletion -> impossible (requires nilpotence)
direct graded relation deletion      -> mixed primitive leakage
full normal-closure saturation       -> every closed Cayley factor deleted
```

Explicit mixed word for every `r>=2`:

$$
M_r=\bar u^r v\bar u^{r-1}vu\bar v^2,
$$

based at `(r^2,0)`, with graded first trace

$$
\operatorname{Tr}W_r(M_r)-\operatorname{Tr}W_{-r}(M_r)
=-4r^4(r-1)\ne0.
$$

## Frozen decision

```text
STOP_LOCAL_COEFFICIENT_SATURATION
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)
ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

## Frozen successor boundary

Paper 38 may test only the presentation-canonical Bass–Serre tree geodesic
shift of the original ascending HNN splitting, with the canonical modular
cocycle and no auxiliary representation.  It may not retry another matrix,
character, fiber rank, nilpotent automaton, or arbitrary infinite-dimensional
completion on the Cayley relation ledger.

## Frozen predecessor and exact aggregate

- Paper 36 research package SHA-256:
  `d29255f9eda598b780aa79165f0dcce6913880dcfa0b9ce5d370c1c43ffbd299`.
- Paper 36 scientific aggregate:
  `499b1a5b0647e9a9999dbfdfc881a8edc0877875102d91607c10e041f69f5221`.
- Paper 37 prototype scientific aggregate:
  `b17967f294da018e2e045ae70ac7731f5612f4bd4693115ea33dbaebb7fc0d6e`.

The final SHA-256 of this source lock is reported externally after freeze and
is not embedded recursively.
