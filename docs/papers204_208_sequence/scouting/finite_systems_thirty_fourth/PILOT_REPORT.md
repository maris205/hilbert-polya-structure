# MPL original tiny complete pilot — actual output

One scientific pilot was predeclared in [SLATE](SLATE.md): every state of
$E_n$ for exactly $n=1,\ldots,6$, totaling873 states. No larger cutoff,
random sample, extra carrier or second original pilot occurred. PSL+ and
KSC were eliminated at the desk and were not numerically re-executed.

| n | states | image | fixed/recurrent | maximum depth | maximum fibre |
|---|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 0 | 1 |
| 2 | 2 | 2 | 2 | 0 | 1 |
| 3 | 6 | 5 | 5 | 1 | 2 |
| 4 | 24 | 11 | 11 | 1 | 4 |
| 5 | 120 | 27 | 26 | 2 | 14 |
| 6 | 720 | 63 | 58 | 2 | 54 |

Only period1 occurred in these finite boxes. The current proof independently
establishes that period restriction for every length, but the other numeric
columns are **not** extrapolated. Every image monotonicity-failure list was
empty. The length-five image contains the nonfixed arrow
`00110 -> 00111`, and length-six has five nonfixed image arrows. Thus
idempotence fails; all those arrows are preserved, not filtered away.

`pilot_mpl.py` is new, self-contained scientific code. It compares its
ordinary palindrome-cut DP with exhaustive cut-mask segmentations on every
source, checks closure/unit-step output/functional-graph transitions/fibre
mass, and emits every arrow, every state depth/period, and every target
fibre size, including zero. Its canonical has873 state rows, six summary
rows and one total row. Each execution reports3,504 checks. Numerical
finite maxima and deepest states are complete within each original box.

## Actual executions and exact byte comparisons

Commands10/11 are the first two full executions, each with67 pinned named
inputs including recorder, driver, pilot, predeclared slate, Python binary
and wrapper-observed import source origins. Commands12/13/14 are actual
`cmp` executions: raw1/raw2 and each raw against [CANONICAL.raw](CANONICAL.raw).
All five child commands exited0 and preserved every input before/after.

An append-only runtime follow-up explicitly adds present bytecode-cache
paths and records Python version/flags plus selected nonsensitive runtime
variables in `RUNTIME_CLOSURE.json`. Commands19/20 are two NEW executions
of the same unchanged scientific program and the same873 original states,
each with105 pinned inputs. Commands21/22/23 are three NEW actual raw
comparisons, with107 named inputs apiece. They all exit0 and match the
original canonical. These are provenance-strengthened replays, not a
second pilot or an enlarged scientific claim. The earlier source-only
runtime records remain unchanged; they were not relabelled retroactively.

Thus four actual producer executions each make3,504 checks; all six
actual raw comparisons exit0. Canonical SHA-256 is
`68586cf26e5b9a38941f5fe6a6ec5981ce1a39c3023b8682cc49c78f335b77e7`.
All raw stdout/stderr, exact argv/cwd/exit, pathsets and before/after pins
are preserved under `commands/`. Sorting is explicit; the program uses
`-I -B`, no random state and no imported prior research code. It is an
author pilot, not a process-separated verifier, candidate gate or review.

## Preserved correction and limits

The first proof draft misnamed which word in the correct three-arrow
example was palindromic. It was copied in full to `drafts/` before the
current explanation was corrected. No scientific code, canonical byte,
theorem inequality, accepted artifact or failed output was overwritten.
There was no failed numerical assertion. The unsuccessful arXiv helper
filename lookup is separately disclosed as a real documentary no-match.

The mathematical signal is insufficient after subtraction: finite
potential convergence, static DP target constraints and two elementary
special fibres do not make the requested two-axis contract. The exact
limits are in [PROOF_PACKAGE](PROOF_PACKAGE.md) and
[SOURCE_AND_COLLISION](SOURCE_AND_COLLISION.md). Final **NO_PROMOTION**.
