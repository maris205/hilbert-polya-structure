# P28 experiment status

## Round 6

`EXECUTION_STATUS=ROUND6_EXACT_GAMMA_CONJUGACY_CLOSURE_COMPLETED`. Run:

```bash
./experiments/reproduce_round6.sh
```

Seventeen tests pass.  Two isolated builds of the eight-row exact conjugacy
certificate, validation, fail-closed non-arithmetic source-package gate, and
standard output are byte-identical.  The artifact-tree SHA-256 is
`098bfcac59f7fd332ddc022d2f59745f4e91450ade251024e9d6a12a6c82126b`;
the three core artifacts have combined SHA-256
`9c593b41c3cb2b971a2f5e5bd38c23b786200e96a938f215225d0a1b7198f13a`.

The default command verifies temporary outputs and the candidate receipt
against the checked-in canonical bytes with `cmp`; it does not overwrite them.
The explicit maintainer-only refresh path is
`./experiments/reproduce_round6.sh --refresh`.  The receipt additionally binds
the Round-6 builder, tests, and reproducer by SHA-256.

The run verifies all eight frozen identities `x^-1*g*x=h` directly in the
exact source-locked `SL(2)` model.  All eight formerly withheld records are
certified conjugate duplicates; none receives owner credit.  The owner count
therefore remains 36 per field, and the Round-5 branch ledger is reused byte
for byte at 576 rows.

This run does not decide arbitrary `Gamma` conjugacy, prove primitivity for the
322 open marked candidates, instantiate a non-arithmetic surface, or run a
dynamical Zeta/root experiment.  The source-package gate records 0/6 required
control inputs and `FAIL_CLOSED_NOT_READY`; all geometry and comparison flags
remain false.  The formal Route-A tuple is unassigned, A2 is not run, A4 has no
credit, and Route B is disabled.  A separate bounded-proxy Route-A record is
exploratory and does not promote the full candidate.

## Round 5

`EXECUTION_STATUS=ROUND5_MATCHED_MARKED_CYCLIC_CENSUS_COMPLETED`. Run:

```bash
./experiments/reproduce_round5.sh
```

Fourteen tests pass.  Two isolated builds of the 390-row census, 576-row
signed-field branch ledger, exact group/census certificate, non-arithmetic
control contract, validation report, and standard output are byte-identical.
The artifact tree SHA-256 is
`1c8665ea55826e73c6aeb5f8cd6386a8d1020976d23004e1216d05e2f1e8a138`.

The finite scope is all freely and cyclically reduced marked words at `L<=4`
modulo cyclic rotation and inversion.  It yields 366 marked-primitive
candidates and 24 powers.  Exact `ell<2ell_B` proves 44 `Gamma` primitives;
homology-axis deduplication credits 36 distinct inverse-paired owners per field
and withholds eight same-axis proved records.  The remaining 322 candidates
stay open.  Only credited owners receive `k=+-1,+-2,+-3,+-4` branches.  All
48 Round-4 seed rows replay compatibly, and no signed branch creates owner
credit.

This run is not a full quotient-group conjugacy census and not an arithmetic
discrimination experiment.  The non-arithmetic control artifact is a strict
design/source contract with `geometry_selected=false` and
`comparison_run=false`.  No target prime, prime ideal, zero, eigenvalue, or
fixed-operator spectrum is used.

## Round 4

`EXECUTION_STATUS=ROUND4_EXPLICIT_BOLZA_OWNER_LEDGER_COMPLETED`. Run:

```bash
./experiments/reproduce_round4.sh
```

Twelve tests pass; two isolated builds of the group certificate, 48-row CSV,
validation report, and standard output are byte-identical.  The artifact tree
SHA-256 is
`b2387be3d4acc6485cd7f0e2d89eeaae9a36dace1ddf2d451d7f51ed3680bfd4`.
This run validates a published matrix transcription and exact theorem-derived
owner ledger.  It does not numerically integrate magnetic trajectories,
enumerate the full Bolza spectrum, or test arithmetic discrimination.

The declared seed contains four inverse-paired primitive axis owners per field
and equation-(19) branches `k=+-1,+-2,+-3`: eight `|k|=1` branches and 24
total signed branches per field, 48 rows overall.  Signed branches do not
receive separate owner credit, and field reversal is `(b,k)->(-b,-k)` on the
same axis ID.  Zero field, odd `N`, full all-`N`, arbitrary twists, fixed
`Delta^L`, and the non-arithmetic metric control remain outside the run.

## Round 3

`EXECUTION_STATUS=ROUND3_SOURCE_CONTRACT_COMPLETED`. Run:

```bash
./experiments/reproduce_round3.sh
```

Eight tests pass; two isolated contract builds are byte-identical.  The
artifact tree SHA-256 is
`a28bf68d0da5c34350224031428f18f325af0d11619df95f2509741475275f3d`.
The run validates the deterministic schema/status contract and exact rational
scaling identities.  It does not independently prove or re-check every
hypothesis of the cited trace theorem, and it generates no eigenvalue or orbit
data.

## Round 2

`EXECUTION_STATUS=ROUND2_OWNER_BOOKKEEPING_COMPLETED`. The deterministic
owner-bookkeeping run and its byte-identical replay are recorded in
`round2_execution_receipt.md`. This is not a magnetic-orbit, spectral, or trace
experiment. Frozen controls are

- zero field `b=0` on a degree-zero trivial bundle with trivial connection;
- positive field `b=+1/2` on the degree-one bundle `L`;
- negative field `b=-1/2` on the degree-minus-one dual bundle `L^*`;
- symmetry-resolved versus unsymmetrized ledgers; and
- an area-, field-, base-degree-, tensor-power-, energy-window-, and
  trace-regime-matched non-arithmetic metric.

Every tensor-family comparison must use a common `N`.  A fixed-operator
high-energy control is a separate regime and cannot be used as evidence for the
`N→∞` family.

The non-arithmetic genus-2 metric is still not instantiated.  Round 5 completed
the finite Bolza marked-cyclic layer and froze the source/parameter contract;
Round 6 subsequently proves that all eight same-homology gaps are exact
conjugate duplicates.  The next experiment must source and instantiate the
matched control under a common geometric cutoff; other regimes remain open.
