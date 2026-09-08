# C421 evidence preparation: exact classification, not a new census

2026-09-08 UTC. Preparation for an anonymous English 11pt standalone
article. This document records inherited accepted evidence and its planned
presentation. No old enumerator, symbolic check, build or evaluation was
run. It does not relabel an internal model review as peer review.

## Accepted mathematical input and actual reading

The following were read in full during manuscript preparation:

| Input | Complete read scope | Role |
| --- | --- | --- |
| [Frozen IR1 contract](../../continuation_round2/integral_return/FROZEN_CONTRACTS.md) | 128 lines, including the stronger pre-computation difference gate | Defines all integer forcing parameters, levels, ordinary points and native time; the earlier tentative height mechanism was superseded, not combined with a new search |
| [Analytic proof](../../continuation_round2/integral_return/IR1_PROOF.md) | 260 lines | Parameter-free difference identity, five-center signed exhaustion, height channel, finite coverage and termination |
| [Classification](../../continuation_round2/integral_return/IR1_CLASSIFICATION.md) | 159 lines | Disjoint oriented cycle families, degeneracies, least periods, exact level counts and dynamical zeta |
| [Coordinator decision](../../continuation_round2/integral_return_review/COORDINATOR_REVIEW.md) | 179 lines | Final accepted complete-contract status; all identified corrections closed |
| [Analytic nonauthor review](../../continuation_round2/integral_return_review/REVIEW_LEMMAS.md) | 257 lines | Signed branches and explicit reversal closure independently checked; no execution in that review |
| [Finite-core nonauthor review](../../continuation_round2/integral_return_review/finite_core/REVIEW.md) | 292 lines | Independent inverse/two-sign reconstruction and complete semantic comparison |
| [Author certifier](../../continuation_round2/integral_return/certify_ir1_core.py) | All 139 lines | Positive-extremum forward enumeration, restoration of both orientations, symbolic-family recognition |
| [Author summary](../../continuation_round2/integral_return/IR1_CORE_SUMMARY.json) | All 59 lines | Recorded first run and complete seed/exit partition |
| [Independent certifier](../../continuation_round2/integral_return_review/finite_core/independent_ir1_core.py) | All 325 lines | Independently ordered interval seeds, both signs, inverse walking, forward reconstruction and full directed-state-set comparison |
| [Independent summary](../../continuation_round2/integral_return_review/finite_core/INDEPENDENT_SUMMARY.json) | All 706 lines, including all per-amplitude entries | Recorded independent run, complete comparison and input identifiers |
| [Independent pre-run plan](../../continuation_round2/integral_return_review/finite_core/REVIEW_PLAN.md) | Complete | Records the independence design before its historical execution |
| [Symbolic identity checker](../../continuation_round2/integral_return_review/check_symbolic_families.py) | Complete | Separate all-parameter recurrence, level, invariant and discriminant substitutions |

Both original source audits were also read in full. The earlier unforced
C413 proof was read selectively at its object/theorem/family verification
and ownership/verification sections, not falsely recorded as a new full
proof review. Its existing bibliography and title metadata were inspected.

The 25,851-record author and independent JSONL files have **not** been
manually reread line by line or re-enumerated in this preparation. Their
complete semantic agreement is an accepted historical result of the
independent program, explicitly documented in its report and summary.
The manuscript must state this evidence provenance accurately.

## Proof chain that must appear in the article itself

Use the map, inverse and invariant
$$
T_a(x,y,z)=(y,z,yz+a-x),\quad
T_a^{-1}(x,y,z)=(xy+a-z,x,y),
$$
$$
K_a=x^2+y^2+z^2-xyz-a(x+y+z).
$$
For the scalar encoding and its two-step differences,
$$
x_{i+3}=x_{i+1}x_{i+2}+a-x_i,\qquad
d_i=x_{i+2}-x_i,\qquad D=\max_i|d_i|,
$$
the forcing cancels exactly:
$$
d_{i-1}+d_{i+1}=(x_{i+1}+1)d_i.                            \tag{E1}
$$

Every arrow below is a mathematical claim to typeset and prove, not a
reference to an old Markdown file in place of proof:

1. $D=0$ gives the alternating family $a=u+v-uv$.
2. If $D>0$ and some $|x_i+1|>3D$, the exact four-step word is forced.
3. If $D>100$, an extremal difference has center
   $s\in\{-3,-2,-1,0,1\}$. All signed branches yield an explicit
   family or a contradiction. The entire case algebra must be printed.
4. Every remaining orbit has $1\le D\le100$ and
   $-3D-1\le x_i\le3D-1$, hence globally $-301\le x_i\le299$.
5. The finite seed conditions cover every remaining orbit. Parameter
   recovery is algebraic; no forcing range or period cutoff is guessed.
6. Exit-or-first-return iteration terminates by finiteness and
   injectivity. The actual completed certificate leaves exactly two
   sporadic words after complete symbolic-family subtraction.
7. The displayed words, proper-divisor tests and parameter
   identifications give a disjoint classification with the native clock.
8. Substitution of the invariant and finite square/parity tests give all
   per-level cycle counts and the finite dynamical zeta product.

## Complete independent finite seed algorithm, ready for typesetting

For each $1\le D\le100$, each $\delta\in\{-D,D\}$, each
$s\in\{-3,-2,-1,0,1\}$ and each integer $q\in[-D,D]$, put
$p=(s+1)\delta-q$ and discard $|p|>D$. Intersect the integer intervals
$$
[-3D-1,3D-1]\cap[-3D-1-\delta,3D-1-\delta]                 \tag{E2}
$$
with
$$
[-1-\lfloor2D/|p|\rfloor,-1+\lfloor2D/|p|\rfloor]
\quad\text{if }p\ne0,
$$
and
$$
[-1-\delta-\lfloor2D/|q|\rfloor,
 -1-\delta+\lfloor2D/|q|\rfloor]
\quad\text{if }q\ne0.                                   \tag{E3}
$$
For every remaining integer $u$, set
$$
v=u+\delta,\qquad a=q-sv+u+s,
\qquad (x,y,z)=(u,s,v).                                  \tag{E4}
$$
Walk the inverse map until either a coordinate leaves the interval in
(E2)'s first factor, $|z-x|>D$, or the starting triple first repeats.
A visited set explicitly rejects a noninitial first repeat; the proof
shows it cannot occur. On return reconstruct the native forward word
from the least triple, checking every state and the first return.

Identify cycles by $(a,\min\{\text{native triples}\})$, but compare
their **complete triple-state sets**, periods and independently generated
family words. Do not merge a word with its reversal. The full author
data are read for comparison only after independent discovery. This
algorithm is sufficiently explicit to reproduce the finite claim without
access to a hidden mathematical lemma.

## Exact historical receipt to reproduce, not relabel as an experiment

| Traversal / signs | Seeds | First returns | Difference exits | Height exits |
| --- | ---: | ---: | ---: | ---: |
| Author, forward positive extremum | 74,866 | 25,907 | 30,335 | 18,624 |
| Independent, inverse negative extremum | 74,866 | 25,907 | 30,335 | 18,624 |
| Independent, inverse positive extremum | 74,866 | 25,907 | 30,344 | 18,615 |
| Independent total | 149,732 | 51,814 | 60,679 | 37,239 |

The nine-seed exchange between the inverse exit types is expected: a
forward and backward orbit can encounter different rejecting boundaries.
It is not an output mismatch. Every seed is assigned exactly one outcome.

Both implementations identify exactly 25,851 directed cycles in the
proved finite core. Their family partition is
$$
(F_3,F_4,F_5,F_6,F_8,F_{12},\mathrm{sporadic})
=(200,25350,99,100,50,50,2).                               \tag{E5}
$$
These are **finite-certificate counts only**, not counts of all members
of the infinite global families. There are 25,753 self-reversing cycles
and 49 pairs of genuinely distinct reversed cycles in this certificate.
The non-self-reversing cycles lie in $F_5$.

The observed longest traversals were 12 forward and 18 backward; neither
was an imposed limit. The observed seed forcing range $[-503,497]$ is
an output, not an input. Historical runtimes were 0.834775 seconds for
the author and 3.37218 seconds for the independent run; report these
only in provenance, not as a benchmark or an algorithmic complexity bound.
The independent run used Python 3.12.3. The separate symbolic receipt
used Python 3.12.3 and SymPy 1.14.0 and checked all ten rows at 55
wraparound phases for each recurrence/level identity, plus the full
invariant and four count-reduction identities.

## Historical byte identifiers and code caveat

| Artifact | Accepted SHA-256 |
| --- | --- |
| Author certifier | `750b4dbb54cacd1df11cc3929ed436cf8de9877048545f212cecc9bc03b75330` |
| Author core JSONL | `352ffd5b5b188e32c347a4083559680e5d1bad12c8e6c6d7cd3dad6324935805` |
| Author summary | `7000a021df6d38d82e14f6a22b3b764026e9545881aa4b7247cd041e5cf4af0b` |
| Independent certifier | `8bd343b599f9ed6c605b255dfe60b544a81375975083fd5d7ffb2b18a1d6c7c3` |
| Independent core JSONL | `0432cd5d8c35fe3cf9fdc0027451bf2e85d04eb880da6da1c03457571fffe35b` |
| Separate symbolic checker | `be9ca47f3b7c8f94b43b25d6857f823f35f004407eff71807770dadf6dac40bd` |

These identify the accepted runs; hashes are not proofs. The original
author code uses Python assertions and must be run without `-O` when
its historical checks are reproduced. The independent implementation
uses explicit exceptions and does not import the author code. The draft
must not silently replace either implementation or attach old receipts
to changed code. No new execution is authorized by this preparation.

## Planned self-contained computational supplement

The main text will print the complete finite seed/exit/return algorithm,
its coverage/termination proofs, family-matching rules and the outcome
tables. A typeset appendix will include the full 139-line primary
certifier, with its exact-input convention and assertion caveat. The
independently structured algorithm will also be specified completely
in mathematical pseudocode, including zero-coefficient intervals,
native forward reconstruction and full-state-set comparison.

Machine-readable supplements will preserve both full source files,
both complete cycle outputs, both summaries and the independent symbolic
checker with the recorded identifiers. They are computational witnesses,
not a substitute for printing the mathematical exhaustion proof. The
25,851 raw records need not be typeset; their generation and complete
comparison must be intelligible from the article itself. Release copying,
new package checks and builds are later coordinator-controlled steps,
not operations performed during this planning task.

## Baseline production checkpoint

After the coordinator's explicit drafting authorization, the author
created the full TeX/PDF and copied the accepted evidence into the
allocated package only. All 16 initial copies passed bytewise comparison.
Subsequently two navigation links in the copied coordinator source audit
were rebased to the unchanged repository context; its scientific text
was not changed. The other 15 artifacts, including every mathematical
proof, program, complete cycle output, execution summary and proof-review
report, remain byte-identical. The six listed historical hashes match.
No enumerator or symbolic checker was rerun. The full actual build and
inspection receipt is in [BASELINE_REPORT.md](BASELINE_REPORT.md).
