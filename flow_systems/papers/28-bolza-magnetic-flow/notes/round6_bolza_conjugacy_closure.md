# P28 Round-6 exact Bolza conjugacy closure

Date: **2026-08-28**

ARS scope: **Stage 1 RESEARCH / Route A A0--A1**.  This round closes exactly
the eight homology-axis ambiguities deliberately retained by Round 5.  It does
not extend the marked-word cutoff, prove primitivity for the other 322 marked
candidates, instantiate the non-arithmetic control, define a dynamical Zeta
function, assign a formal Route-A tuple, or invoke Route B.

## 1. Result at a glance

```text
HISTORICALLY_WITHHELD_PROVED_RECORDS=8
EXACT_DIRECT_SL2_CONJUGACIES=8
INVERSE_FALLBACKS=0
CERTIFIED_CONJUGATE_DUPLICATES=8
UNRESOLVED_INSIDE_FROZEN_EIGHT=0
NEW_OWNER_CREDITS=0
PRIMITIVE_AXIS_OWNERS_PER_FIELD=36
FIELD_AXIS_OWNER_PAIRS=72
ROUND5_BRANCH_ROWS_REUSED_BYTE_FOR_BYTE=576
GAMMA_PRIMITIVITY_OPEN=322
FULL_GAMMA_CONJUGACY_COMPLETENESS=NOT_ESTABLISHED_OUTSIDE_FROZEN_EIGHT
NONARITHMETIC_CONTROL=DESIGN_ONLY_NOT_INSTANTIATED
FORMAL_ROUTE_A_TUPLE=UNASSIGNED
A2_EVALUATION=NOT_RUN
A4_CREDIT=NONE
ROUTE_B_INVOCATION_ALLOWED=false
```

All eight Round-5 withheld records are conjugate to their already credited
representatives.  They are not eight additional primitive-axis owners.  The
finite certified population therefore has 44 primitive records partitioned as

```text
36 credited inverse-paired Gamma-conjugacy classes
+ 8 exact conjugate duplicate records
= 44 exactly primitivity-certified records.
```

## 2. Source lock and exact model

The builder refuses execution unless the Round-5 builder, Round-4 exact group
builder, 390-row census, 576-row branch ledger, group certificate, validation,
and non-arithmetic control contract have their frozen SHA-256 digests.  In
particular, the source census and branch ledger are bound to

```text
round5 census SHA-256:
d3d3fab9a62de100247d76141f0fb96cfe988c5fedb4bfe14dea262a64f88b27

round5 branch ledger SHA-256:
5f9cc50dfba3bb257a8a4f32c8bc5bd322a683788da4c9b900e9f8a5a62ee493
```

Every equality is evaluated in the existing exact model

```text
Q(s,t,i),   s^2=2,   t^2=1+s,   i^2=-1,
```

after exact determinant-one and polygon-relator replay.  No decimal length,
tolerance, numerical conjugator search, or equality of trace alone enters the
certificate.

## 3. Exact conjugacy witnesses

For each row, `g` is the already credited representative, `h` is the
historically withheld record, and the displayed `x` satisfies the direct
matrix identity

```text
x^-1 g x = h
```

exactly in `SL(2)`.  The projective sign is `+` for every row; no equality to
`h^-1` is used.

| Credited `g` | Historically withheld `h` | Exact conjugator `x` |
|---|---|---|
| `C0034: f0*f1^-1*f2` | `C0039: f0*f2*f1^-1` | `f3^-1*f0^-1` |
| `C0036: f0*f1^-1*f3` | `C0049: f0*f3*f1^-1` | `f3^-1*f2*f1^-1` |
| `C0046: f0*f2^-1*f3` | `C0051: f0*f3*f2^-1` | `f0*f1^-1` |
| `C0067: f1*f2^-1*f3` | `C0070: f1*f3*f2^-1` | `f0*f1^-1` |
| `C0168: f0*f1^-1*f2*f3` | `C0267: f0*f3*f2*f1^-1` | `f3^-1*f2*f1^-1` |
| `C0143: f0*f1*f2^-1*f3` | `C0271: f0*f3*f2^-1*f1` | `f0` |
| `C0173: f0*f1^-1*f2^-1*f3` | `C0272: f0*f3*f2^-1*f1^-1` | `f0*f1^-1*f1^-1` |
| `C0169: f0*f1^-1*f2*f3^-1` | `C0293: f0*f3^-1*f2*f1^-1` | `f0^-1` |

The source and target matrices in every row are literally different before
conjugation.  Thus the certificate is not merely detecting a repeated CSV row
or a direct PSL equality.  The explicit witnesses are sufficient positive
certificates; no claim that a bounded search would decide arbitrary surface-
group nonconjugacy is made.

## 4. Owner and branch consequence

Each target already had exact `ell<2ell_B` primitivity, the same homology axis,
trace, trace squared, and geodesic length as its credited peer.  Round 6 changes
only the interpretation of the historical withheld status:

```text
WITHHELD_DUPLICATE_HOMOLOGY_AXIS_GAMMA_CONJUGACY_UNRESOLVED
  -> CERTIFIED_CONJUGATE_DUPLICATE_NO_NEW_OWNER.
```

The Round-5 census remains an immutable historical artifact.  The new eight-row
certificate is the resolution overlay.  No owner ID is added, no historical
owner ID is renamed, and the Round-5 576-row magnetic branch ledger is reused
byte for byte.  Signed `k`, field sign, and orientation continue to mint no
owner credit.

## 5. Non-arithmetic control gate

`round6_nonarithmetic_source_package_gate.json` evaluates only the current
source lock.  None of the six required items is present:

1. a named closed constant-curvature genus-two control surface;
2. explicit torsion-free cocompact Fuchsian matrices;
3. a presentation and checked relation;
4. a primary or peer-reviewed source locator;
5. an independent non-arithmeticity certificate; and
6. a rigorous systole or stronger per-owner primitivity certificate.

The gate therefore records `FAIL_CLOSED_NOT_READY`, leaves every execution
flag false, and gives no authorization to run a control census.  This is an
auditable missing-input result, not a negative experimental result.  No random
matrix perturbation, changed marking, synthetic systole, or genericity argument
is substituted for the missing geometry.

## 6. Reproducibility

```text
UNIT_TESTS=17/17_PASS
DETERMINISTIC_BUILDS=2
BYTE_IDENTICAL=PASS
ARTIFACT_TREE_SHA256=098bfcac59f7fd332ddc022d2f59745f4e91450ade251024e9d6a12a6c82126b
CORE_ARTIFACT_SHA256=9c593b41c3cb2b971a2f5e5bd38c23b786200e96a938f215225d0a1b7198f13a
CONJUGACY_PAYLOAD_SHA256=bb355c9765ef59c5f7e73b36b6e84d4e4bc6fb8aa2e4b166ca4a850fd234f4c3
```

The tests independently replay all source digests, exact generators and
relator, the frozen eight pair identities, conjugator words, direct `SL(2)`
equalities, absence of inverse fallback, shared peer invariants, zero owner
delta, the 36-owner/576-branch invariants, the 322 open primitivity cases, the
fail-closed control gate, target-data absence, and route firewalls.

## 7. Route boundary

This is `[PROVED]` bounded A1 evidence: within the exact short primitive subset,
the previous eight distinctness ambiguities are fully resolved and the owner
ledger now has an exact group-conjugacy explanation.  It is not a global A1
pass.  Full `Gamma`-conjugacy completeness outside the frozen eight and
primitivity for 322 records remain open; the arithmetic-prime dictionary and
mandatory arithmetic controls are absent.

A separate typed Route-A YAML is emitted only for the bounded
`L<=4` certified-owner proxy.  It conservatively records
`A0_WEAK_ARITHMETIC_RELATION`, `A1_WEAK`, and
`A2_FAIL/A3_FAIL/A4_FAIL` with `NOT_TESTABLE` evidence status, overall
`ROUTE_A_EXPLORATORY`.  This is an evaluation record, not a promotion of the
full Paper-28 candidate, whose tuple remains unassigned.  There is no explicit
dynamical Zeta/Fredholm determinant, frozen validation region, root count, or
cutoff/precision study.  The tensor-power host remains an architecture note
with no A4 credit, and Route B remains disallowed.

The next smallest lawful step is to acquire and source-lock a valid
non-arithmetic genus-two package satisfying all six gate requirements, then
freeze one common geometric cutoff before inspecting either surface's branch
outcomes.
