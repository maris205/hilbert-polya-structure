# Paper 37 preregistration — SD-C39

## 1. Frozen question and verdict rule

On the full unquotiented cyclically nonbacktracking affine edge shift, test
whether one finite-rank matrix coefficient mechanism can simultaneously:

1. own a same-object matrix Fredholm trace-log;
2. preserve one free `z` per original Hashimoto transition;
3. cancel every translated, conjugated, repeated, and mixed affine relation
   factor at the level of complete primitive matrix Euler factors;
4. retain one nonzero source-proved arithmetic primitive factor; and
5. fail matched generic presentations.

Failure of any item rejects the candidate. Cancellation of a first trace or
an aggregate of distinct primitive orbits earns no factor-deletion credit.

## 2. Frozen source and coefficient fixture

For `r>=2`, retain the formal-reverse right Cayley graph of

```text
M_r=<u,v | vu=u^r v>+
```

with immediate reversals forbidden and one unit marker per original
transition. For an oriented edge based at `(b,k)`, use

```text
d_theta(e)=theta^(1+b+k),  0<theta<1,
T_(P,theta)=(D_theta tensor I) H_P (D_theta tensor I).
```

Freeze rank two in each parity and

```text
A = [[1,1],[0,1]],
B_+(r) = [[1,0],[r,1]],
B_-(r) = [[1,0],[-r,1]].
```

Both sectors assign `u -> A`; even assigns `v -> B_+(r)` and odd assigns
`v -> B_-(r)`. Formal reverses receive exact inverses. No replacement fixture
may be selected after evaluation.

## 3. Frozen invariant and ownership firewall

For each primitive orbit `gamma`, the accepted ordinary unit is

```text
det(I-q_theta(gamma) z^|gamma| W_gamma)^(-1).
```

The explicitly graded branch owns the ratio of the independent odd and even
Fredholm determinants. It may not be reported as an ordinary positive
determinant. Complete factor deletion means equality of determinant
polynomials, equivalently equality of every power trace; first-trace
cancellation is insufficient.

Backtracks are absent by the Hashimoto transition rule. Inverse transport
would assign `P_bar(e) P_e=I`, so the coefficient mechanism receives no credit
for paths excluded before coefficients act.

## 4. Frozen parameters and controls

- theorem range: every integer `r>=2` and every `0<theta<1`;
- exact affine rows: `r=1,...,8`, with balanced `r=1` and composite baseline
  `r=4`;
- six fixed one-relator mutations;
- `48` deterministic random cyclically reduced one-relator controls, seed
  `370037`;
- `24` paired random two-relator presentations;
- flat balanced parity, traceless invertible, nilpotent, and inverse-edge
  backtrack boundary controls;
- power supertraces through order twelve;
- two fresh subprocess runs with `PYTHONHASHSEED=0` and canonical byte
  equality.

Bounded mixed candidates are products of two conjugated relators with freely
reduced conjugators of length at most three for affine rows and at most two for
random controls. “Shortest” means shortest only in this preregistered bounded
census.

## 5. Source/evaluator split

The source process constructs presentations, words, bounded normal-closure
products, and frozen matrices only. The evaluator must not import the source
module and must independently implement free and cyclic reduction, affine
group evaluation, exact matrix arithmetic, factor comparison, repetition
checks, and decisions.

Scientific arithmetic is exact over integers and `fractions.Fraction`. No
unbounded word enumeration, network access, floating tolerance, target label,
target coefficient, factorization predicate, or prime/zero datum is allowed.

## 6. Preregistered theorem checks

1. Prove trace-class ownership of `T_(P,theta)` from source-coordinate damping,
   bounded matrix Hashimoto transport, and the trace-ideal property.
2. Derive the complete primitive matrix Euler product and every-repetition
   trace-log on the same uninduced edge space.
3. Prove `det(I-tW)=1` iff finite-dimensional `W` is nilpotent; conclude that
   invertible ordinary holonomy cannot delete a primitive factor.
4. Prove graded all-orders deletion iff the even and odd determinant
   polynomials agree.
5. Use Paper 36 contractibility to prove the flat fork: unbalanced ranks retain
   relation factors, while balanced parity cancels every closed orbit.
6. Prove direct all-orders cancellation for the frozen shear fixture.
7. Verify that

   ```text
   M_r=bar(u)^r v bar(u)^(r-1) v u bar(v)^2
   ```

   is a primitive cyclically nonbacktracking closed path based at `(r^2,0)`
   and that its graded first trace is `-4r^4(r-1)` for every `r>=2`.
8. Prove that saturation over every finite mixed product of conjugated
   relators and inverses covers every closed Cayley word and gives
   `Z_gr(z)=1`.

Finite experiments audit formulas and controls but do not prove any infinite
or all-rank statement.

## 7. Frozen expected exact results

- prototype assertions: `131/131`;
- affine direct-factor cancellations: `8/8`;
- affine mixed primitive leaks in the frozen census: `8/8`;
- random one-relator direct cancellations: `9/48`;
- mixed leaks after those cancellations: `9/9`;
- paired two-relator cases with both direct factors cancelled: `2/24`, with a
  mixed leak in both;
- fresh subprocess scientific payloads: byte-identical;
- prototype scientific SHA-256:
  `b17967f294da018e2e045ae70ac7731f5612f4bd4693115ea33dbaebb7fc0d6e`.

## 8. Acceptance and stop rules

The candidate stops if ordinary deletion requires noninvertible holonomy,
direct graded cancellation leaks on a mixed relation consequence, full
normal-closure saturation cancels every closed orbit, a surviving residue is
generic across matched controls, or any forbidden repair is required.

The strict decision is frozen as

```text
STOP_LOCAL_COEFFICIENT_SATURATION
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

## 9. Forbidden repairs and claim boundary

Forbidden: prime/factor tables, accepted support, target coefficients or
zeros, KMS/GNS/boundary/crystal/vacuum/Fock substitution, first return,
acceleration, finite quotient, `z=1`, changed edge clock, support projection,
ordinary/graded determinant conflation, post-result fixture replacement, or
Route B.

The result is scoped to finite-rank inverse-edge coefficient mechanisms under
the complete mixed-relation obligation on this affine Cayley shift. It is not
a no-go for every cocycle, representation, groupoid, or infinite-dimensional
coefficient algebra, and it proves no arithmetic Euler product, functional
equation, target divisor, critical-line mechanism, or RH implication.

## 10. Frozen provenance and successor

- research package: `/tmp/paper37_research_package.md`, SHA-256
  `e39a8c89975670926461c46c9c82df58e886647e49fb77244fc530d3a060f3aa`;
- source lock: `/tmp/paper37_source_lock.md`, SHA-256
  `d725f03caffc6c5fab916314df25097b7383af7494287052496516deab0dcb4e`;
- prototype: `/tmp/paper37_exact_prototype/`, scientific SHA-256
  `b17967f294da018e2e045ae70ac7731f5612f4bd4693115ea33dbaebb7fc0d6e`.

No downstream experiment ledger, Route card, manifest, environment lock, or
Git hash is preregistered here.

Paper 38 may test only the presentation-canonical Bass–Serre tree geodesic
shift of the original ascending HNN splitting with its canonical modular
cocycle. It may not retry another arbitrary matrix, character, fiber rank,
nilpotent automaton, or completion on the same Cayley relation ledger.
