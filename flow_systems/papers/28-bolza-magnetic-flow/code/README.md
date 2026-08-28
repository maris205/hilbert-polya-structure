# P28 code status

## Round 8

`build_round8_control_systole_certificate.py` implements the finite theorem
frozen before computation.  It represents every traversed control element as
a Gaussian-integer polynomial `PSU(1,1)` matrix divided by
`Delta^q*sqrt(Delta)^p`, cancels common `Delta` factors, and canonicalizes the
projective sign.  Four generator/inverse pairs and the published relator reduce
to the exact identity.  Group equality never uses rounded matrix hashes.

Exact `Fraction` Taylor intervals prove the polygon-radius, cutoff, and center
guards and decide every nonzero trace-comparison polynomial.  Breadth-first
side-neighbor expansion closes the identity-connected
`|alpha|^2<=20000` component with 18,533 included states and 108,616 distinct
rejected boundary states.  The compact-polygon lemma then makes the result
complete for conjugacy classes of length at most `21/10`; the trace signs prove
the exact systole and `g0*g3` equality witness.

`test_round8_control_systole_certificate.py` has twenty-four tests covering
source/upstream locks, exact inverses and relator, all rational guards, frozen
state counts/digests, systole signs and primitivity, cutoff authorization, and
the census/comparison/A2/Route-B firewalls.  Canonical reproduction is:

```bash
./experiments/reproduce_round8.sh
```

Default mode is verify-only; `--refresh` is explicit.  The builder freezes
`Lambda=21/10` only after the theorem passes.  It does not run either surface
census, classify the 144 equality group elements into conjugacy owners, or
generate a magnetic comparison.

## Round 7

`build_round7_nonarithmetic_control_gate.py` digest-binds the pre-computation
freeze and four claim-bounded sources, specializes Nazarenko's exact octagon
formulas at `(a,alpha)=(exp(-1/10),pi/4)`, and emits the source matrix, analytic
and high-precision matrix package, six-item gate, and validation record.  It
checks admissibility, determinant one, `SU(1,1)`, hyperbolicity, angle sum, and
the published surface relator at 140 decimal digits.  Exact logic separately
certifies a transcendental square-subgroup trace and four primitive generator
classes.

`test_round7_nonarithmetic_control_gate.py` has twenty-two tests covering the
freeze and remote-source locks, claim boundaries, parameter admissibility,
matrix and relation replay, the square-subgroup Takeuchi obstruction,
per-owner abelianization primitivity, all six gates, mutation failure, and the
cutoff/census/comparison/target/A2/Route-B firewalls.  Canonical reproduction
is:

```bash
./experiments/reproduce_round7.sh
```

The default mode is verify-only and `--refresh` is explicit.  The builder does
not claim a control systole or run a census/comparison; its next authorized
input is a rigorous lower-bound/completeness certificate sufficient to freeze
one common geometric cutoff.

## Round 6

`build_round6_bolza_conjugacy_certificate.py` digest-binds the immutable
Round-5 builders and five result artifacts, then evaluates eight frozen
conjugacy witnesses in the same exact number field.  For each credited source
`g`, historically withheld target `h`, and short group word `x`, it verifies
`x^-1*g*x=h` exactly in `SL(2)`.  All eight use projective sign `+`; none uses
an inverse fallback.  The emitted resolution ledger classifies the targets as
`CERTIFIED_CONJUGATE_DUPLICATE_NO_NEW_OWNER`.

The builder does not rewrite the Round-5 census or magnetic branch ledger.
Its validation independently requires 36 owner IDs per field, the exact
576-row branch-ledger SHA-256, 322 still-open primitivity cases, zero new owner
credits, zero target-data rows, an unassigned formal tuple, and Route B
disabled.  It also emits `round6_nonarithmetic_source_package_gate.json`, which
fails closed because the six required control-source components are absent;
it creates no geometry or comparison result.

`test_round6_bolza_conjugacy_certificate.py` has seventeen tests covering all
source digests, exact determinant/relator replay, the frozen pair set and
conjugators, direct `SL(2)` equalities, absence of inverse fallback, peer
invariants, owner/branch conservation, the fail-closed control gate, and route
firewalls.  Canonical reproduction is:

```bash
./experiments/reproduce_round6.sh
```

The certificate closes only the frozen eight ambiguities.  It is not a full
surface-group conjugacy normal form and does not evaluate A2 or A4.

## Round 5

`build_round5_bolza_marked_cyclic_census.py` exhaustively enumerates all
freely/cyclically reduced marked words at `L<=4`, canonicalizes them modulo
cyclic rotation and inversion, separates proper marked powers, and evaluates
the source-locked matrices exactly in
`Q(s,t,i)`, `s^2=2`, `t^2=1+s`, `i^2=-1`.  It audits literal PSL equality and
equality-or-inverse collisions, computes exact trace-squared isospectral
groups, and replays numerical lengths with the Round-4 120-decimal model.

The exact systolic gate `abs(trace)<10+8sqrt(2)` proves `Gamma` primitivity for
44 of 366 marked-primitive candidates.  A second conservative gate credits at
most one proved primitive per abelianized homology vector modulo sign.  This
emits 36 mutually distinguished inverse-paired owners per field, withholds
eight same-axis proved records, and leaves 322 primitivity candidates open.
Only the 36 credited axes receive theorem-derived branches at
`k=+-1,+-2,+-3,+-4`, giving 576 rows and no orientation or signed-branch owner
credit.  The builder also emits a design-only non-arithmetic control contract;
it does not invent control matrices or a comparison result.

`test_round5_bolza_marked_cyclic_census.py` has fourteen tests covering exact
group replay, exhaustive counts, normal-form invariance, proper-power laws,
matrix equality/inverse collisions, primitivity, homology-axis deduplication,
signed-`k`/field involutions, periods, actions, stability, Round-4 compatibility,
target-data absence, and route firewalls.  Canonical reproduction is:

```bash
./experiments/reproduce_round5.sh
```

The complete claim applies to the declared marked-cyclic equivalence only.
Full `Gamma`-conjugacy completeness is `NOT_ESTABLISHED`.

## Round 4

`build_round4_bolza_owner_ledger.py` transcribes the published genus-two
opposite-side-pairing matrices, replays their determinants, common trace, and
polygon relator at 120-decimal precision, and emits the first target-free
Bolza magnetic-owner seed ledger.  Its declared scope is four systolic
inverse-paired primitive axis owners per field, equation-(19) signed branches
`k=+-1,+-2,+-3`, and fields `b=+1/2,-1/2` under the frozen Round-3 even
subtype: 24 branches per field and 48 rows total.  The negative-`k` branch may
store `f_j^-1`, but it shares the same `primitive_axis_owner_id` and receives no
second owner credit.

`test_round4_bolza_owner_ledger.py` has twelve tests covering the group source
lock, inverse-paired primitive certificate, four-owner-per-field grid, absence
of orientation owner credit, signed-`k` laws, `(b,k)->(-b,-k)` field reversal,
action, both clocks, signed/absolute stability, Maslov index, target-data
absence, and route firewalls.  Canonical reproduction is:

```bash
./experiments/reproduce_round4.sh
```

The matrix residuals validate the source transcription; they do not replace
the source's Poincare-polygon theorem.  The generator list is not promoted to a
complete primitive spectrum.

## Round 3

`build_round3_trace_contract.py` generates and validates the 12-row
source-bound contract for `N=2,4,8,16` and fields `0,+1/2,-1/2`.
`test_round3_trace_contract.py` has eight independent standard-library tests,
including the fixed-`k` positive/negative action-sign pairing.
Canonical reproduction is:

```bash
./experiments/reproduce_round3.sh
```

The generated contract does not contain eigenvalue or orbit samples.  It
authorizes the source-compatible signed-field even-subsequence owner theorem,
while retaining an open zero-field owner and all fixed-operator firewalls.

## Round 2

`EXECUTION_STATUS=ROUND2_OWNER_LEDGER_COMPLETED`. The owner lemma now freezes
the connection/dual connection, sign convention, named Hilbert spaces,
operators, domains, bundle degrees, field-reversal partners, and holonomy
repetition. `build_owner_ledger.py` generated a 12-row target-free ledger for
`N=1,2,4,8`; `test_owner_ledger.py` passed 7/7 tests and replayed
byte-identically.

Those `UNASSIGNED`/`OPEN` fields are the immutable Round-2 state.  Round 3 adds
a separate, narrower source-compatible even-subsequence contract rather than
rewriting historical artifacts.

The implementation must key all spectral outputs by `tensor_power_N` and must
reject pooling with the separate fixed candidate `Δ^L`.  A `PROVED` same-owner
token is permitted only for the verified source-compatible signed-field even
subsequence.  All other regimes remain `[OPEN]` / `NOT_ESTABLISHED` until a
separate trace theorem is verified.
