# P24 Round-6 conclusion — exhaustive elementary-Nielsen sensitivity

Date: **2026-08-28**

## Material Passport

- Origin skill: `ars-codex:academic-research-suite`
- Workflow: ARS Stage-1 research plus deterministic validation
- Freeze SHA-256:
  `ea2ac26dfab2ff05f7ea4f179d76c96130559d94013d0f0f5b4689a44f730f89`
- Core-output SHA-256:
  `f5d31071c7174d84322c352b9028e334bf30e89a2368a751fbe58f6ab83ed660`
- Target data: none

## Exact panel theorem

Let `x=(x_1,x_2,x_3,x_4)`.  Round 6 uses the identity marking and all
elementary right Nielsen moves

```text
x_i -> x_i x_j^epsilon,
i != j,
epsilon in {+1,-1}.
```

There are exactly `1+4*3*2=25` such markings.  Each move has the explicit
inverse `x_i -> x_i x_j^(-epsilon)` and therefore preserves the generated
subgroup.  This is `[PROVED]` finite free-word algebra.  The Bianchi base is
`(U1,Ui,L1,Li)`.  The control base is the explicitly redundant Tietze
four-marking `(a,b,ab,aB)`, which generates the pinned two-generator control
because its first two entries are `a,b`.  Redundancy is disclosed; it is not
called a presentation match.

Each of the 50 system-marking pairs uses the same alphabet size eight, the same
19,624 freely and cyclically reduced linear words through marked length five,
the same 2,074 dihedral marked owners, and the same exact symbolic root rule.
Every candidate matrix has determinant one and lies in level `(3)` exactly.
The maximum 212-bit control determinant residual is
`6.3282339877999745e-58`, computed after subtracting one at SnapPy's native
212-bit precision and only then projecting to binary64.

## Exploratory result

The phase statistic and 64 permutations per system-marking pair are those in
the frozen contract.  A provisional eight-marking implementation pilot was
disclosed before the canonical run.  Its values are not consumed or reported
as evidence.  Consequently this is an exhaustive exploratory decision audit,
not a blind confirmatory experiment.

```text
candidate z range          [-2.00184797173, -1.08554792773]
candidate range width       0.916300044002       PASS (<=1)
control z range            [-0.747750608375, 16.1675419980]
control range width         16.9152926064         FAIL (<=1)
signed contrast direction  25 negative / 0 positive PASS
minimum |contrast|          0.808035900150        PASS (>=0.5)
```

The conjunction therefore fails.  Under the frozen exploratory rule:

```text
PAPER_DECISION=STOP_SCOPED_CURRENT_PHASE_STATISTIC_AS_MARKING_SENSITIVE
CURRENT_PHASE_STATISTIC=RETAIN_FOR_DESCRIPTIVE_METHODS_HISTORY_ONLY
METRIC_BIANCHI_PREFIX_AUTHORIZED=false
```

The result is about the present finite-cutoff statistic.  It does not prove
that every Bianchi invariant is marking-dependent, and the control's large
spread may be driven partly by its deliberately redundant stabilization.
That is precisely why the result cannot support an arithmetic comparison.

## Formal typed Route record

The conservative tuple

```text
(A0_WEAK_ARITHMETIC_RELATION,
 A1_WEAK,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)
overall = ROUTE_A_EXPLORATORY
```

is assigned only to `P24-BIANCHI-MARKED-WORD-PROXY`.  `A2_FAIL` means that
this finite marked-word proxy owns no determinant; it is not a theorem against
the cusp-aware analytic determinant of the full Bianchi flow.  The full-flow
tuple remains `UNASSIGNED`, its Gaussian-prime-ideal owner map remains open,
and Route B remains closed.

The next lawful positive step must start from a source-derived owner theorem
or from a different invariant under a separately frozen falsification
contract.  The stopped phase statistic does not authorize a metric prefix.
