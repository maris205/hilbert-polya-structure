# Exact control results

## Scope

`code/verify.py` is a standard-library exact verifier. It enumerates every
integer partition of every weight `1<=n<=40` and performs **10,110,035 exact
assertions**. The stored stdout transcript is
`code/verification_output.txt`.

The union of the enumerated lanes contains 215,307 partition states. The
largest lane is `n=40`, with 37,338 states and 374 one-step image states.

## Post-review fresh-run gate

The unchanged verifier was run with bytecode writes disabled after all
manuscript repairs:

```bash
python3 -B code/verify.py > /tmp/p113_verify_revision.txt
cmp -s /tmp/p113_verify_revision.txt code/verification_output.txt
```

- verifier exit: `0`;
- `cmp` exit: `0` (byte-for-byte match; no hash used);
- fresh stdout: 45 lines and 6,053 bytes;
- fresh result: `PASS: 10,110,035 exact assertions`;
- measured wall time: 11.438 s.

Because the mathematical contracts did not change, neither `verify.py` nor
the canonical transcript required an edit.

## Independently computed objects

- Principal-hook images from Ferrers row/column lengths.
- Principal-hook images from Frobenius arms and legs.
- Orbit depths by literal iteration and by cached recurrence.
- Fibre sizes by direct census.
- Fibre sizes by an independent strict arm/leg dynamic program.
- Fibre sizes by Goupil's owned product formula.

## Assertion families

For every enumerated state, the verifier checks:

- equality of the two hook constructions;
- weight preservation and Durfee-length agreement;
- adjacent image gaps of at least two;
- conjugation involution and `H(lambda)=H(lambda')`;
- strict nonnegative Frobenius arms and legs;
- Gutschwager's owned first-hook formula and strict first-part growth;
- literal termination without a nontrivial cycle;
- exact recursive/literal depth agreement;
- the pointwise and global depth bounds;
- both cases of the exact gap-increment theorem;
- positive-time conjugate orbit agreement and the sole depth exception.

For every target and lane, it additionally checks:

- exact equality of the observed and characterized image sets;
- observed fibre size = product formula = Frobenius DP count;
- `A_0=1`, `A_1=n-1`, total layer mass, and every weighted transport lane;
- the balanced two-row witness path for `n>=2` (`b-1` two-row updates plus one
  final hook step), the terminal `n=1` witness, and sharp maximum depth;
- for each lane, `#Fix(H_n^m)=1` for `1<=m<=8`;
- zeta coefficients equal to one through degree eight;
- dedicated `n=1` and `n=2` boundary assertions.

## Falsification controls

The program actively locates and freezes the first witnesses against three
stronger conjectures:

```text
first_nonprojection=(4, (2, 2), (3, 1), (4,))
first_depth_conjugacy_failure=(2, (2,), (1, 1), 0, 1)
first_boundary_shell_failure=(16, (4, 4, 4, 4), 7, 8)
```

Thus the manuscript does not claim idempotence, unconditional conjugacy of
depth, or a naive rectangular-boundary classification of deepest states.

## Representative exact lanes

| `n` | `p(n)` | image size | maximum depth | states at maximum |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 1 | 1 |
| 10 | 42 | 6 | 5 | 4 |
| 16 | 231 | 17 | 8 | 13 |
| 20 | 627 | 31 | 10 | 29 |
| 30 | 5,604 | 117 | 15 | 145 |
| 35 | 14,883 | 211 | 17 | 914 |
| 40 | 37,338 | 374 | 20 | 628 |

## Interpretation boundary

The computation is a regression and counterexample search, not a substitute
for proof or an ownership test. Every manuscript statement is proved
symbolically. The gap increment and sharp depth form the sole main theorem;
absorption, layer transport, conjugation timing, periodic census, and zeta are
explicit low-credit consequences. Gutschwager/Goupil/Chern--Yee owner material
remains zero credit, and external novelty, priority, and dissemination remain
**HOLD**.
