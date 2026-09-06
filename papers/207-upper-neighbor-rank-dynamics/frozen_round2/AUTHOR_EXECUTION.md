# P207 author certificate: actual production and replay pair

2026-09-06 UTC. Author/proof contributor: `batch197_fosp_gate`.
Outcome: the paper-local [producer](verify.py) completed an initial
production and **two additional fresh executions**, each with
**1,384,012 passing assertions**. All three raw outputs are byte-identical
to the complete [canonical](CANONICAL.json). These are author executions,
not independent manuscript reviews, source clearance, a paper freeze,
PDF/build inspection, or completion of the five-paper batch.

## Exact executed input and output

| File / item | SHA-256 or value |
|---|---|
| `verify.py` | `5018b0fe6d6a032e0eadeb7cd53a6de47c789193580fa1707312b592cd4a3c93` |
| `record_author.py` | `6f84d70eebb562d63678623c362ea16b9ce7a284ddc04d2953252ad044e2c1e7` |
| Complete canonical, 288,808 bytes | `306d4e7dea07ad10234f06c69912561425792ed61fadeff3b165b09d1a106992` |
| Ordered checked-record SHA-256 | `9b10399f1754ca2728ed16c8bd3466ffcc54e9d6217a33c4e08fe5d3eaa5d172` |
| Python executable | `/root/miniconda3/bin/python3`, Python 3.12.3 |
| Executable SHA-256 | `9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101` |

The code imports only `collections`, `hashlib`, `itertools` and `json`.
It reads no file, canonical, repository module or external data and uses
no network, random choice or floating-point calculation. Each child ran
a byte-pinned copy of `verify.py` in a new standalone attempt directory,
not a repository-importing wrapper.

The [recorder](record_author.py) separately reads provenance files and
writes logs. It strips inherited Python import-location overrides without
printing their values and sets `LC_ALL=C`, `TZ=UTC`, `PYTHONHASHSEED=0`,
`PYTHONDONTWRITEBYTECODE=1`, and `PYTHONSAFEPATH=1`. Its complete command
arguments, working directories, interpreter/build version, UTC times,
durations, child exits and stream hashes are in the actual receipts.

## Three actual executions, followed by raw comparisons

Working directory for these recorder commands was the workspace root.
The commands were actually executed in the order shown; they are not a
suggested future procedure.

```sh
python3 -B papers/207-upper-neighbor-rank-dynamics/record_author.py --initial --tag initial_01
python3 -B papers/207-upper-neighbor-rank-dynamics/record_author.py --tag pair_01
```

| Producer | Actual UTC interval | Seconds | Assertions | Producer exit |
|---|---|---:|---:|---:|
| Initial run 0 | 07:02:06.144–07:02:19.827 | 13.683 | 1,384,012 | 0 |
| Fresh run 1 | 07:04:23.832–07:04:37.508 | 13.676 | 1,384,012 | 0 |
| Fresh run 2 | 07:04:37.513–07:04:51.144 | 13.631 | 1,384,012 | 0 |

The [initial receipt](author_replay/initial_01/RECEIPT.json) records its
actual stdout-to-canonical `cmp` and live-canonical-to-snapshot `cmp`, both
exit zero. The [pair receipt](author_replay/pair_01/RECEIPT.json) records
two actual stdout-to-canonical comparisons, the raw run-1/run-2 comparison,
and live-canonical-to-snapshot comparison; all four exited zero.
Every producer stderr and every comparator stream is empty. Each producer
stdout is the full 288,808-byte JSON; no normalized-text comparison or
summary replacement was used.

The complete original pair outputs are
[nested run 1](author_replay/pair_01/run1.stdout) and
[nested run 2](author_replay/pair_01/run2.stdout). For the existing freezer's
expected layout, [flat run 1](author_replay/run1.stdout) and
[flat run 2](author_replay/run2.stdout) are immutable byte copies of those
same two executions. The actual command

```sh
python3 -B papers/207-upper-neighbor-rank-dynamics/author_replay/export_pair.py
```

created them with exclusive writes at 07:05:54 UTC. Its
[export receipt](author_replay/export_pair_01/RECEIPT.json) records four
additional actual `cmp` calls, each alias against its original and against
the canonical; all four exited zero. The receipt explicitly says
`new_numerical_runs=0`. The aliases are not counted as a second pair.

## Provenance, pin coverage and authorship

This is an adaptation and combination of this same contributor's earlier
[UGR verifier](../../docs/papers204_208_sequence/scouting/word_local/UGR_PROOF_WORK/verify_ugr.py)
and [LNR inverse verifier](../../docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/verify_inverse.py).
The inherited local sign-cone, column compatibility, eight-role graph,
zero-run source lists and mixed-kernel code are disclosed reuse, not
independent reproduction. New integration checks the full UGR source sets,
their input-complement transport, run/role decoding, the complete functional
graphs, and all stated target maxima/equality cases in one standalone file.
Matrix-word products reuse prefix products for efficiency without changing
the predeclared complete word set.

No gate C++ code, reviewer representation, old verifier import or canonical
reader was used. The nonauthor gate's direct enumeration of all 13-letter
words and its 81-state overlap graph remain a different verification route.
This author is a mathematical contributor and cannot review P207.

Each execution attempt physically snapshots and before/after-pins **17
files**: this producer and recorder; the accepted theorem/artifact contracts;
the two original proofs, two original verifiers, two original canonicals
and two historical manifests; the LNR source boundary; and the UGR gate
contract, source audit, input pins and manifest. See the exact
[pair before-pins](author_replay/pair_01/INPUT_PINS.before.sha256) and
[after-pins](author_replay/pair_01/INPUT_PINS.after.sha256), with complete
physical copies under each attempt's `source_inputs/`. All 17 were unchanged
within both attempts. Historical code/canonicals are provenance evidence,
not runtime inputs to `verify.py`. This does not purport to redo the gate's
source reading or the later manuscript's bibliography audit.

The initial, pair and alias-export directories have complete nonself
manifests of 30, 36 and 9 entries respectively. The final
`author_replay/OWNED_MANIFEST.sha256` seals only this contributor's named
top-level files and `author_replay/` evidence. It is **not** the whole-paper
or Round0 freeze manifest; root owns that distinct artifact gate.

## What the certificate actually checks

The complete canonical retains the explicit local proof dependency, not
just an aggregate success count. It exhausts all 177,147 inner eleven-letter
words: 158,643 have equal time-2/time-4 centers, 18,300 have a new-extremum
witness entirely inside the inner cone, and 204 need the two outside
letters. The canonical prints **each of all 1,836 outside-extension
witnesses** for those 204 exceptions. Witnesses are also tested by direct
height inequalities, including their allowed position/time domain.

Every thirteen-letter word has a unique inner word and one of the nine
outer pairs. Equality of the overlapping update cones preserves the two
center values and each inner witness. The exceptional class checks all
nine extensions explicitly. Thus the recorded certificate and the displayed
overlap argument cover all **1,594,323** thirteen-letter words; this author
program does not claim to have looped over that many full words directly.
The proof embeds every cyclic window, including repeated coordinates for
n<13. That coverage and embedding are necessary to use the finite lemma
for the nonsharp all-size bound.

| Section | Passing assertions | Exact finite scope |
|---|---:|---|
| Local growth certificate | 44,359 | All inner words, complete exceptional extensions, literal rule and permanence controls |
| Core columns and graph | 406 | All 125 five-type triples, all 3,125 five-column windows, 28 role paths, exact full determinant, traces 1–60 |
| Complete cyclic sources and targets | 1,154,612 | Every one of 88,560 sources and 88,560 targets across n=3,…,10 |
| Local inverse tables | 3,402 | Every positive source/target run of lengths 1–6 and all boundary heights |
| Mixed-kernel comparison | 177,854 | All A/J/B words of lengths 2–10; matrix identities 2–100; exact rational constants |
| Single-seed checks | 3,371 | Only the prescribed seed/source at each n=4,…,64 |
| Deducted classical attainer adapter | 8 | Full independent-set/source-set bijections at n=4,6,8,10 |
| Total | 1,384,012 | One actual execution |

The source/target boxes verify exact decoded source sets, including empty
fibres, rather than comparing only maximum numbers. The Kahn functional-
graph decomposition checks all depths and strict cycles independently of
the role decoder. Every nonzero core word has its labelled role sequence
recovered and its phase flip checked; the actual power identity is also
tested throughout each full box. The observed heights at n=3,…,10 are
`1,5,5,5,5,5,5,6`; these observations are **not** an all-size sharp formula.
The respective fibre maxima are `3,7,7,18,18,47,47,123`, and every labelled
maximizer is compared against the full stated equality list.

No complete cyclic box exceeds the already reviewed n=10 cutoff. The
longer seed checks, graph traces and matrix identities are separately
labelled and do not increase that full-carrier bound. Finite checks pressure
the all-parameter proof; they do not replace its mixed-kernel inequalities,
length budget, equality argument, core converse or wave induction.

## Preserved failures and limits

No paper-local producer or replay failed in these three attempts. The
earlier shorter-cone counterexamples and the erroneous center-only
weak-column test remain untouched in the original UGR author package;
this code retains the corrected requirement to check the neutral neighbor's
own equation. The gate's earlier compile failure also remains unchanged.
During readback, an optional `jq` summary command exited 127 because `jq`
was unavailable; subsequent standard-library JSON readback succeeded. This
was not a failed numerical producer or a suppressed mathematical finding.

The upper bound is `H(n)<=4n+2`, explicitly **nonsharp**. The exact seed
clock and H(3) do not establish the global sharp height for n>=4. The input
complement and static inverse decoder receive no extra contribution credit;
the global mixed-target extremal theorem is used once for the rank family.
The unread Mukherjee 2011 body remains the recorded source-access limitation
with LNR's separate finding untouched. This receipt does not claim new
source clearance, public release, independent manuscript acceptance,
Round0/1/2 or batch completion. `OWNER_AMBER / HOLD_EXTERNAL` remains.
