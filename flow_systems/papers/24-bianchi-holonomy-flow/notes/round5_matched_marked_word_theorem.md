# P24 Round-5 theorem and method note — matched marked-word census

## Scope and pre-result freeze

Round 5 executes the smallest comparison authorized by the Round-4 conclusion:
the Bianchi candidate and the finite-volume `5_2=m015` control are passed
through one executable **marked cyclic-word** rule.  The complete rule and the
phase statistic were written before the result builder was run and are
hash-pinned in
[`../experiments/round5_freeze_contract.json`](../experiments/round5_freeze_contract.json):

```text
freeze SHA-256 = 210cff78b8af54847baae1c7ef21572dd697d70004f50723f6b1bac4e19a85b7
marked length  = 1,...,5
linear words   = freely reduced and cyclically reduced
owner          = minimum over rotations and rotations of the inverse
primitivity    = exact shortest symbolic word root
multiplicity   = number of linear words mapped to the canonical owner
comparison set = symbolically primitive loxodromic rows
```

The frozen contract consumes no Gaussian-prime, rational-prime, prime-ideal,
Riemann-zero, or Dedekind-zero data.  It also freezes the known asymmetry:
the candidate marking has four positive generator symbols whereas the pinned
SnapPy control presentation has two.  Here “rank 4 versus rank 2” is shorthand
for **marked positive-generator count**, not a theorem about minimal group rank
or freeness.  Results therefore cannot be used to tune the cutoff, statistic,
or interpretation.

## Exact marked-word theorem

Let

```text
A_r = {g_1,G_1,...,g_r,G_r},  G_j = g_j^(-1),
```

with token order `g_1,G_1,g_2,G_2,...`.  Let `W_(r,N)` be the nonempty freely
and cyclically reduced words of length at most `N`.  On `W_(r,N)`, identify a
word with all cyclic rotations of itself and of its inverse.

**Proposition `[PROVED]`.**  The Round-5 canonicalization emits exactly one row
for each resulting unoriented marked cyclic class.  Its
`marked_orbit_multiplicity` is the number of linear words in that class.
Furthermore, the shortest-prefix root test uniquely decomposes each emitted
word as `u^k`, where `u` is not a proper word power; hence the symbolic
primitive/repetition label is exact for this marked-word quotient.

**Proof.**  Every finite rotation/inversion orbit has a unique lexicographic
minimum, so canonicalization is constant on an orbit and two distinct orbits
cannot share a representative.  Enumeration visits every word in `W_(r,N)`
once, and the counter therefore records the exact orbit cardinality.  For a
finite word, the least period dividing its length is unique; testing divisors
in increasing order returns its unique shortest root.  Rotation and inversion
canonicalization of that root supplies the corresponding unoriented root
owner.  These are finite combinatorial claims and are replayed by the unit
tests.  ∎

This proposition is deliberately about a **marked symbolic quotient**.  A
group presentation can identify additional words, and group conjugacy can
identify elements not related by free-word rotation.  Thus the proposition
does not prove full-group conjugacy or group-theoretic primitivity.

## Holonomy evaluation layers

### Bianchi candidate

The four Round-2 positive matrices `U1, Ui, L1, Li` and their inverses are
evaluated exactly over `Z[i]`.  All 2,074 owner representatives have determinant
one and are exactly congruent to `I mod 3`.  The exact matrix classification
finds two identity rows, 132 parabolic rows, and 1,940 loxodromic rows.  The two
identity rows are not removed: they visibly record short relations in the
chosen elementary marking.  Complex lengths of loxodromic rows are floating
reconstructions from exact traces and retain their numerical status.

### Finite-volume control

The inherited Round-4 source chain proves the control's finite-volume,
one-cusped, non-arithmetic geometry; Round 5 does not re-prove it.  The pinned
SnapPy 3.3.2 presentation is

```text
positive generators = a,b
relator             = aBBBabbAAbb
```

and words are evaluated with the 212-bit high-precision `SL2C`
representation.  The maximum determinant residual is
`1.5618132689045278e-62`.  These holonomy matrices and complex lengths are
high-precision **non-interval numerical observations**.  After the respective
exact/212-bit matrix evaluations, both systems use the same comparison
projection: complex lengths are serialized from binary64 to 17 significant
digits and reparsed before the frozen statistic is computed.  The numerical
parabolic classifier is also well separated at this cutoff: the maximum
parabolic `|tr^2-4|` residual is `2.2029717170162733e-63`, whereas the minimum
loxodromic gap is `1.8149626247513604` (threshold `1e-25`).

## Executed census

| Field | Bianchi candidate | `5_2=m015` control |
|---|---:|---:|
| marked positive-generator count / alphabet size | 4 / 8 | 2 / 4 |
| raw cyclically reduced linear words | 19,624 | 372 |
| canonical unoriented marked owners | 2,074 | 51 |
| symbolic primitive / repetition owners | 2,046 / 28 | 41 / 10 |
| loxodromic / parabolic / identity owners | 1,940 / 132 / 2 | 48 / 3 / 0 |
| primitive loxodromic rows used by the phase statistic | 1,932 | 39 |

The same algorithm, canonicalization, primitivity rule, multiplicity rule,
cutoff, precision contract, and comparison formula are executable on both
sides.  The alphabet cardinality and the underlying presentations are not the
same.  Therefore “matched” in Round 5 means **matched rule**, not matched group
presentation, matched sample size, or matched metric-length spectrum.

## Frozen phase-sensitive comparison

For primitive loxodromic rows, the predeclared complex statistic is

```text
q = corr(ell, cos(theta)) + i corr(ell, sin(theta)).
```

For each system, 64 target-free null permutations are obtained by sorting
source owner IDs with the frozen SHA-256 key.  The reported standardized value
is

```text
z = (|q| - mean_null |q|) / sample_sd_null |q|.
```

The observed values are:

| Quantity | Bianchi candidate | Control |
|---|---:|---:|
| `Re(q)` | 0.00322886827439 | 0.0761310902556 |
| `Im(q)` | -3.35688625065e-18 | 0.0823012747601 |
| `|q|` | 0.00322886827439 | 0.112113526082 |
| null mean `|q|` | 0.0288734503702 | 0.202137418192 |
| null sample SD | 0.0146805344620 | 0.110955366022 |
| `z` | -1.74684253916 | -0.811352306226 |

The absolute standardized contrast is `0.935490232934`.  Both observed
magnitudes lie below their respective frozen null means.  No inferential
threshold or p-value was preregistered, and the ledgers have very different
cardinalities and presentations.  These numbers are consequently a
`[NUMERICAL_OBSERVATION]`, not evidence for or against an arithmetic owner.

## Paper-level consequence and residual gap

Round 5 closes the Round-4 **enumeration data-type mismatch** at the algorithmic
level: the candidate word ball is no longer compared directly with a control
metric cutoff.  It also makes the next obstruction quantitative rather than
implicit: marked positive-generator counts 4/alphabet 8 versus 2/alphabet 4
produce 1,932 versus 39 comparison rows and retain presentation dependence.

Accordingly:

```text
CROSS_SYSTEM_COMPARISON=EXECUTED_DESCRIPTIVE_ONLY
ARITHMETIC_KILL_VERDICT=BLOCKED_BY_MARKING_AND_PRESENTATION_CONFOUND
FORMAL_ROUTE_A_TUPLE=UNASSIGNED
A2_A4_EVALUATION=NOT_EVALUATED
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
```

The smallest next artifact is a **preregistered same-marked-generator-count
Nielsen sensitivity panel**.  It must freeze all alternative markings before looking at
their phase results and must keep target tables prohibited.  Only a marking-
stable comparison could justify spending effort on a metric-cutoff Bianchi
ledger; it would still not create an orbit-to-prime-ideal map.
