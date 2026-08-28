# P24 code status — Rounds 2–5

`round2_bianchi_ledger.py` uses exact pairs of Python integers for Gaussian
arithmetic.  It enumerates the reduced word ball of
`U(3), U(3i), L(3), L(3i)` and their inverses through frozen word length 5,
deduplicates exact matrices, checks determinant and level membership, identifies
power relations visible inside the sample, reconstructs PSL complex lengths,
and emits a deterministic holonomy shuffle without consulting prime or zero
tables.

Commands:

```bash
python3 code/test_round2_bianchi_ledger.py -v
python3 code/round2_bianchi_ledger.py
python3 code/round2_bianchi_ledger.py --verify-existing
```

The test suite covers exact generator and row membership, inverse closure,
projective trace reconstruction, target-free controls, and byte determinism.
The code intentionally does not assert full `Gamma((3))` generation or full
conjugacy/primitivity completeness.

## Round 3 — exact classical-Schottky control

`round3_schottky_control.py` uses exact Gaussian-rational arithmetic to define
four complex Möbius generators by

```text
h_j(z) = (z-a_j)/(z-r_j),
g_j = h_j^(-1) o (mu *) o h_j,
mu = (3+4i)/50000.
```

It verifies eight paired round disks, every one of the 28 pairwise separation
inequalities, the forward and inverse conjugacy identities, and the exact
boundary modulus relation.  It then enumerates the rank-4 free-group reduced
word ball and oriented cyclic classes through marked word length 5, records
primitive roots/repetitions, orientation, trace-invariant collisions, complex
length, holonomy, and stable/unstable multipliers, and runs a deterministic
intrinsic holonomy shuffle.

Commands:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/test_round3_schottky_control.py -v
PYTHONDONTWRITEBYTECODE=1 python3 code/round3_schottky_control.py
PYTHONDONTWRITEBYTECODE=1 python3 code/round3_schottky_control.py --verify-existing
```

The control matches only generator rank, oriented alphabet size, and word
cutoff.  It is convex-cocompact and infinite-volume, not a finite-volume
Bianchi substitute.  It has no arithmetic owner and consumes no target data.

## Round 4 — finite-volume cusped non-arithmetic control

`round4_finite_volume_control.py` freezes `5_2=m015`, checks the rigorous
positive SnapPy isometry identification and exact topology fields, records the
manually audited theorem-source chain, and builds a complex-length ledger with
pinned `snappy==3.3.2`.

The primary high-precision implementation emits grouped geodesics at real
length `<3.05`; the independent `length_spectrum_alt` implementation checks the
prefix at real length `<2.10` and 106-bit precision.  The program fails closed
if the pinned version, counts, multiplicity vector, or numerical residual bound
changes.

Commands:

```bash
python3 -m pip install 'snappy==3.3.2'
PYTHONDONTWRITEBYTECODE=1 python3 code/test_round4_finite_volume_control.py -v
PYTHONDONTWRITEBYTECODE=1 python3 code/round4_finite_volume_control.py
PYTHONDONTWRITEBYTECODE=1 python3 code/round4_finite_volume_control.py --verify-existing
bash experiments/reproduce_round4.sh
```

The theorem chain proves the finite-volume one-cusp non-arithmetic control;
the executable decimal invariants remain non-interval numerical observations.
No prime, zero, arithmetic label, or target-fitted cutoff is consumed.

## Round 5 — matched marked-word comparison

`round5_matched_marked_word.py` reads and hash-validates the pre-result contract
in `experiments/round5_freeze_contract.json`.  It runs one generic enumeration
function on inverse-paired alphabets with 4 and 2 positive marked symbols:

```text
freely reduced -> cyclically reduced -> rotations plus inverse rotations
-> lexicographic owner -> shortest symbolic root -> marked multiplicity.
```

The candidate reuses the exact Gaussian-integer Round-2 matrices.  The control
uses the pinned SnapPy 3.3.2 two-generator presentation and evaluates words in
its 212-bit high-precision `SL2C` representation.  The common phase statistic
uses the same binary64/17-significant-digit complex-length projection on both
sides.  It and the 64 target-free permutations are part of the executable
pre-result contract, not selected after the ledger is viewed.

Commands:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/test_round5_matched_marked_word.py -v
PYTHONDONTWRITEBYTECODE=1 python3 code/round5_matched_marked_word.py
PYTHONDONTWRITEBYTECODE=1 python3 code/round5_matched_marked_word.py --verify-existing
bash experiments/reproduce_round5.sh
```

The algorithm, canonicalization, symbolic primitivity, multiplicity and cutoff
match.  Marked generator count and presentation do not: count 4/alphabet 8
versus count 2/alphabet 4 is a frozen confound.  This is not a claim about
minimal group rank.  The outputs are marked symbolic censuses,
not complete group-conjugacy or metric-length spectra.  No prime/zero target
data are read, and no formal Route tuple or A2+ evaluation is emitted.
