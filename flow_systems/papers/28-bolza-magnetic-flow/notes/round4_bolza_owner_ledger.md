# P28 Round-4 inverse-paired Bolza axis/signed-`k` ledger

Date: **2026-08-27**

ARS scope: **Stage 1 RESEARCH / Route A A0--A1**.  This note instantiates the
first genuine Bolza conjugacy/magnetic-orbit owner ledger inside the frozen
Round-3 signed-field even-subsequence subtype.  It does not enumerate the full
Bolza length spectrum, assign rational-prime labels, instantiate the zero-field
or non-arithmetic metric controls, or transfer any result to fixed `Delta^L`.

## 1. Result

`[PROVED under the frozen even subtype]`: four explicit opposite-side pairing
elements of the regular Bolza octagon define four primitive inverse-paired
axis owners per field.  The deterministic ledger instantiates the signed
`k != 0` sum displayed in Kordyukov--Taimanov equation (19), truncated to
`k=+-1,+-2,+-3`, together with the `b=+1/2 <-> -1/2` field-sign partner:

```text
INVERSE_PAIRED_AXIS_OWNERS_PER_FIELD=4
FIELD_AXIS_OWNER_PAIRS=8
SIGNED_K_PRIMITIVE_BRANCHES_PER_FIELD=8
SIGNED_TRACE_BRANCHES_PER_FIELD=24
SIGNED_K_PRIMITIVE_BRANCH_ROWS=16
SIGNED_K_REPETITION_BRANCH_ROWS=32
TOTAL_LEDGER_ROWS=48
MAXIMUM_ABSOLUTE_REPETITION=3
ORIENTED_OWNER_CREDIT_ROWS=0
TARGET_DATA_ROWS=0
ARITHMETIC_LABEL_ROWS=0
```

The 16 `|k|=1` rows are signed trace branches, not 16 primitive owners.  This
is a certified seed ledger, not a completeness claim.  In particular, the
source-backed four side pairings are not asserted to exhaust all systolic or
all primitive Bolza conjugacy classes.

## 2. Bolza group source lock

Ebbens, Iordanov, Teillaud, and Vegter give the opposite-side pairing matrices
of the generalized Bolza polygon in equation (5), the polygon relation in
equation (6), and the Bolza systole in Theorem 2.  At genus two, set

```text
a   = cot(pi/8) = 1+sqrt(2),
rho = sqrt(a^2-1) = sqrt(2+2sqrt(2)),

A_j = [[a, exp(i j pi/4) rho],
       [exp(-i j pi/4) rho, a]],       j=0,1,2,3.
```

The associated isometries `f_0,...,f_3` pair opposite sides of the regular
octagon and generate the Bolza Fuchsian group.  Their inverses are
`f_{j+4}=f_j^-1`.  The polygon relator is

```text
f0 f1^-1 f2 f3^-1 f0^-1 f1 f2^-1 f3 = identity.
```

The source and Poincare polygon theorem certify the group representation.  The
code independently replays the transcription at 120-decimal precision:

```text
max determinant residual = 5e-119
max trace residual       = 0e-119
polygon-relator residual = 1.5339252852327487e-117
```

These residuals check the encoded matrices; they are not presented as a new
numerical proof of Poincare's theorem.

## 3. Primitive certificate and inverse-pair counting boundary

Every generator has

```text
tr(A_j) = 2(1+sqrt(2)),
ell_B   = 2 acosh(1+sqrt(2))
        = 3.0571418389619963225449123695873467865... .
```

The same source proves that `ell_B` is the Bolza systole.  Therefore `f_j` is
primitive: if `f_j=u^q` with `q>=2`, translation length would give
`ell(u)=ell_B/q<ell_B`, contradicting systolic minimality.

The polygon presentation has one length-eight relator whose exponent sum in
each `f_j` is zero.  Its abelianization is therefore `Z^4`; `f_j` and
`f_j^-1` carry `+e_j` and `-e_j`, respectively, and are not conjugate in
`Gamma`.  That group-theoretic fact is retained, but it is not converted into
two owner credits in this trace schema.  For each `j` the ledger fixes

```text
primitive_axis_owner_id = BOLZA_AXIS_INVERSE_PAIR_j
inverse_pair_definition = {f_j,f_j^-1}
canonical representative = f_j.
```

Equation (19) is then instantiated once for the axis owner with signed
`k`.  The `k<0` row may carry the branch word `f_j^-1` and the group element
`f_j^k`, but it remains a branch of the same inverse-paired owner.  This is a
project no-double-counting convention; it does not assert that the source's
notation silently identifies two nonconjugate elements.  Branch class and
owner count therefore remain separate:

```text
|k|=1       -> SIGNED_K_PRIMITIVE_BRANCH
|k|=2 or 3  -> SIGNED_K_REPETITION_BRANCH
all six k rows for fixed (field,j) -> one primitive_axis_owner_id
```

## 4. Magnetic periods, action, and stability

Let

```text
N_B = (1+sqrt(2)+sqrt(2+2sqrt(2)))^2 = exp(ell_B).
```

Kordyukov--Taimanov Theorem 3 identifies every primitive hyperbolic conjugacy
class with a unique primitive closed magnetic trajectory above the critical
level.  Equations (22)--(23) give its period, Poincare multipliers, stability
denominator, and Maslov index.  After the exact Round-3 reindexing
`N=2m`, `E=sqrt(5)`, each seed owner has

```text
primitive trace-clock period    = sqrt(5/3) ell_B
                                = 3.9467531430979095073061328696659781982...

primitive physical-clock period = 2/sqrt(3) ell_B
                                = 3.5300833273511522320487789598389271033...
```

For the signed source index `k in {+-1,+-2,+-3}` and `r=|k|`,

```text
absolute trace-clock period       = r sqrt(5/3) ell_B,
signed trace time                 = k sqrt(5/3) ell_B,
absolute physical-clock period    = r 2/sqrt(3) ell_B,
action/N                          = k sqrt(3)/2 ell_B,
phase                             = exp(-i N k sqrt(3)/2 ell_B),
Fourier factor                    = hat_phi(k sqrt(5/3) ell_B),
ordered Poincare multipliers      = (N_B^k,N_B^-k),
absolute determinant square root = N_B^(r/2)-N_B^(-r/2),
equation-(19) signed denominator  = N_B^(k/2)-N_B^(-k/2),
Maslov index                      = 0.
```

Thus the displayed trace denominator changes sign under `k -> -k`, while the
absolute determinant square root and unordered Poincare spectrum do not.  The
ledger stores both quantities instead of labeling `N_B^k` as “unstable” when
`k<0`.

Here `action/N` is the project even-subsequence phase coefficient obtained from
the source action after `m=N/2`; it is not a fixed-operator action.  The
individual square-root-connection holonomy is deliberately not lifted from the
source phase.  Only the total even-`N` action, for which `L^N=K^m`, is claimed.

## 5. Signed-`k` and field partners

For a fixed field, equation (19)'s two signed branches are recorded by

```text
(b, primitive_axis_owner_id, k)
  -> (b, same primitive_axis_owner_id, -k).
```

This reverses signed trace time, action, and the displayed signed stability
denominator without creating a second owner.  Round 2 proved antiunitary
bundle duality and classical time reversal.  In the inverse-paired schema its
field involution is

```text
(b, primitive_axis_owner_id, k)
  -> (-b, same primitive_axis_owner_id, -k).
```

It preserves `|k|`, both absolute clock periods, the axis-owner ID, the
absolute stability root, and the unordered multiplier spectrum; it reverses
signed trace time, action, and the signed equation-(19) denominator.  All 48
rows have both a signed-`k` partner and a field-sign partner, and both maps
replay as involutions.

## 6. Reproducibility result

```text
UNIT_TESTS=12/12_PASS
DETERMINISTIC_BUILDS=2
BYTE_IDENTICAL=PASS
ARTIFACT_TREE_SHA256=b2387be3d4acc6485cd7f0e2d89eeaae9a36dace1ddf2d451d7f51ed3680bfd4
ROW_PAYLOAD_SHA256=9421f17680281527792cbd551663ca2faf57263cbe154ccc792d775b9c42b88d
```

The tests cover the group transcription, relator, norm/systole identity,
inverse-paired owner count, absence of orientation owner credit, signed-`k`
branch classification, signed-`k` and field involutions, period/action laws,
the equation-(19) signed stability denominator, Maslov index, target-data
absence, and route firewalls.

## 7. Claim and route boundary

```text
PROPOSAL_STAGE=1
ROUTE_A_SCOPE=A0-A1
A0_SCREEN=ARITHMETIC_BOLZA_SUBSTRATE_PRESENT_PRIME_LINK_UNPROVED
A1_PROGRESS=4_INVERSE_PAIRED_AXIS_OWNERS_PER_FIELD_WITH_SIGNED_K_TRACE_ROWS
A1_COMPLETENESS=NOT_COMPLETE_PRIMITIVE_SPECTRUM
FORMAL_A0_A4_TUPLE=UNASSIGNED
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
```

Only the source-compatible signed-field even subsequence receives `[PROVED]`
same-owner credit.  The following remain `[OPEN]` / `NOT_ESTABLISHED`:

- zero field;
- odd `N`;
- arbitrary degree-one flat twists;
- the full all-`N` family;
- the fixed degree-one operator `Delta^L`;
- a complete primitive Bolza enumeration;
- any rational-prime or prime-ideal dictionary; and
- the metric-matched non-arithmetic control.

The next smallest test is to extend the exact ledger from the four side-pairing
generators to a source-locked bounded-length conjugacy census with a certified
normal-form/completeness rule, then run the same ledger schema on the
area/field/degree-matched non-arithmetic genus-two control.

## Primary sources checked

- Ebbens, Iordanov, Teillaud, and Vegter, *Delaunay triangulations of
  generalized Bolza surfaces*, Journal of Computational Geometry 13 (2022),
  https://doi.org/10.20382/jocg.v13i1a5 and
  https://arxiv.org/abs/2103.05960.
- Katz, Katz, Schein, and Vishne, *Bolza Quaternion Order and Asymptotics of
  Systoles Along Congruence Subgroups*,
  https://arxiv.org/abs/1405.5454.  Proposition 10.3 and Corollary 10.4 provide
  an independent arithmetic-group presentation and identify four generators as
  systolic loops.
- Kordyukov and Taimanov, *Trace formula for the magnetic Laplacian on a compact
  hyperbolic surface*, https://arxiv.org/abs/2202.06055, especially Theorem 3
  and equations (19), (22), and (23).
