# P27 Round-4 theorem — finite-level `g`-loop closing times escape every residual tower

Date: **2026-08-27**

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite`
- Origin Workflow: Stage-1 theorem development plus experiment-agent validation
- Mathematical owner: descending normal finite-index tower and one
  infinite-order element
- Frozen specialization: `Gamma(3 n!)` in `PSL_2(Z)`
- Verification Status: theorem `PROVED`; 24-row finite audit
  `NUMERICALLY_CERTIFIED / REPRODUCIBLE`

## Theorem — quotient-order and period escape

Let `Gamma_1` be a group and

```text
Gamma_1 >= Gamma_2 >= Gamma_3 >= ...
```

a descending sequence of normal finite-index subgroups with
`intersection_n Gamma_n={e}`.  For an infinite-order element
`g in Gamma_1`, let

```text
o_n = order of g Gamma_n in Gamma_1/Gamma_n.
```

Then:

1. `o_n` divides `o_(n+1)` for every `n`; and
2. `o_n -> infinity`.

If the tower consists of normal finite covers of a hyperbolic surface and `g`
is hyperbolic with translation length `ell(g)`, the lift of the closed
`g`-loop based on the coset of `g` requires exactly `o_n` whole traversals
before returning.  Its corresponding closing time is

```text
T_n(g)=o_n ell(g) -> infinity.
```

Here `o_n` is minimal **among whole traversals of the chosen `g`-loop**.  If
`g` is known to represent a primitive conjugacy class, this closing time is the
minimal period of its lifted flow orbit.  Without that primitivity input, no
claim is made that `T_n(g)` is the underlying flow orbit's minimal period.

Normality makes `o_n` independent of the chosen conjugate/lift owner at level
`n`.

### Proof

Because `Gamma_(n+1)` is contained in `Gamma_n`, the quotient map
`Gamma_1/Gamma_(n+1) -> Gamma_1/Gamma_n` sends the class of `g` to the class of
`g`.  The order of an image divides the order of its preimage; hence
`o_n | o_(n+1)`.

Suppose the positive integers `o_n` did not tend to infinity.  A bounded
divisibility sequence is eventually constant, say `o_n=r` for all `n>=N`.
Then `g^r` lies in every `Gamma_n` with `n>=N`.  It also lies in `Gamma_N`, and
`Gamma_N` is contained in each earlier `Gamma_n`, so

```text
g^r in intersection_n Gamma_n={e}.
```

This contradicts that `g` has infinite order.  Therefore `o_n -> infinity`.
For a hyperbolic deck transformation, a lift closes after `k` base traversals
exactly when `g^k in Gamma_n`; the least such `k` is `o_n`.  Multiplying by the
chosen `g`-loop translation length proves the closing-time statement.  QED.

## Factorial-tower corollary

The Stage-1 proof already establishes

```text
intersection_n Gamma(3 n!)={e} in PSL_2(Z).
```

Each `Gamma(3 n!)` is a normal finite-index kernel.  Every hyperbolic element
has infinite order.  The theorem therefore gives `[PROVED]`:

```text
for every fixed hyperbolic g in Gamma(3),
ord(g mod Gamma(3 n!)) -> infinity,
and its finite-level whole-g-loop closing times escape to infinity.
```

This sharpens the owner firewall behind `Per(M_infinity)=empty`.  The finite
levels do not merely use different closing multiples: for each fixed
hyperbolic owner, those multiples eventually leave every bounded set.

## Executed finite-prefix audit

The Round-4 executable reuses the frozen Round-2 ledger, whose SHA-256 is
`811c53a24e34def2b7fbb9353ccd568dd638a9c57706443626091bc4c23e09de`.
It verifies all 21 divisibility transitions and the three exact sequences:

```text
G3-A: 1, 3, 3, 6, 6, 36, 72, 288
G3-B: 1, 1, 3, 12, 60, 360, 360, 2880
G3-C: 1, 2, 6, 12, 12, 72, 72, 576
```

The last-to-first growth factors are respectively `288`, `2880`, and `576`.
These 24 rows illustrate a finite prefix; they do not prove divergence.  The
general group-theoretic argument above is the proof.

The frozen positive words are primitive necklaces, but their full
`Gamma(3)`-conjugacy-class primitivity remains `OPEN`.  The quotient-order
escape statement applies to the recorded infinite-order elements and does not
require that stronger primitivity claim.  Consequently, the theorem certifies
their chosen-loop closing times, not an unproved primitive minimal-period
interpretation.

## Prior-work and novelty boundary

The theorem is presented as an elementary owner criterion and an explicit
factorial-tower specialization, not as a priority claim for the general
aperiodicity phenomenon.  The Round-3 closest-prior audit remains controlling:
the proposed paper is a transparent case study combining the sign-sensitive
residual proof, escape lemma, finite ledger, and same-owner firewall.

## Route correspondence

```text
PROPOSAL_STAGE=1
ROUTE_A_SCOPE=A0-A1
PERIOD_ESCAPE_THEOREM=PROVED
FINITE_PREFIX_AUDIT=NUMERICALLY_CERTIFIED
LOCAL_A1_PROGRESS_TAG=PROVED_A1_OBSTRUCTION
FORMAL_A0_A4_TUPLE=UNASSIGNED
A2_A4=NOT_EVALUATED
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
```

The theorem supplies no rational-prime owner, dynamical zeta, determinant, or
Route-B input.  Finite-level periods remain owned by the tower plus the chosen
element; inverse-limit periodic-orbit credit remains forbidden.
