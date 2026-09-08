# IR1 coordinator classification and evidence review

2026-09-07 UTC. Coordinator: non-author of the IR1 proof and enumerator.
This is current-team AI-assisted internal review, not blind review,
human peer review, external GPT-5.4 review or a priority certificate.

Final verdict: **PASS — ADMIT ONE COMPLETE CONTRACT**. The analytic
proof, independent finite-core reconstruction, final classification/count
formulas and substantive source subtraction have all been reviewed.
The coordinator has read both complete nonauthor reports and the whole
independent program. There are no remaining required corrections.

## Actual inputs and independent checks

The coordinator has read the whole
[analytic proof](../integral_return/IR1_PROOF.md),
[classification](../integral_return/IR1_CLASSIFICATION.md),
[author enumerator](../integral_return/certify_ir1_core.py),
[original summary](../integral_return/IR1_CORE_SUMMARY.json), and both
author source/scout reports. The original 25,851-line output was not
manually inspected line by line. Its complete semantic comparison is
the independent finite-certificate task, not a reading claim here.

The complete [nonauthor lemma review](REVIEW_LEMMAS.md) was read,
including its signed branches and the directed closure of W1. Its
scope is §§1–4, not the output or source novelty. The coordinator's
own earlier derivation identified the Section 2 typo: both neighboring
values are `m+e`, not one `m-e`. The author repaired it, and the
separate lemma reviewer verified that actual correction. Neither
the enumerator nor its bounds depended on the mistaken sign.

The coordinator independently checked the five possible extremal
centers, the `k=1,2` channels at center `-1`, both signs after reversal
at centers `0,-2`, and all displayed strict inequalities at `D>100`.
The proof's bounded core is mathematical, parameter-independent and
period-independent. No positive-extremum assumption survives the
second reversal without its explicit sign variable.

Section 3.6 now expressly closes all channels under reversal; the
original reviewer checked this addition and closed its Minor W1.
In particular, a reversed F5 word belongs to parameter `-1-u`, which
usually denotes a different forward orbit. The finite core cannot merge
those orientations. No remaining analytic correction was identified.

## Classification table and native clocks

All scalar words are interpreted as periodic bi-infinite sequences.
Equality of consecutive triples after `j` forward steps implies equality
of the entire scalar sequence by deterministic invertible recurrence;
the least scalar period is therefore the actual map period.

The coordinator checked the following degeneracies and identifications:

| Entry | Complete identification / exclusion checked |
| --- | --- |
| F1/F2 | `D=0` gives exactly `a=u+v-uv`; `u=v` is fixed and `u<v` selects each genuine two-cycle once |
| F3 | Its prime length collapses only at `t=-2`, already fixed |
| F4 | A two-step rotation exchanges `t` and `a+1-t`; equality gives period two or one. `2t<a+1` selects precisely the period-four representatives |
| F5 | Prime length five never collapses. Generic `t` is unique by its unique `-1` entry; `t=0,-1` give the sole cyclic duplicate. Omitting `-1`, not quotienting `t` by `-1-t`, preserves distinct orientations |
| F6 | `t=0` is fixed; a three-step rotation sends `t` to `-t`, so `t>=1` is exact and has period six |
| F8 | Four-step rotation sends `t` to `-t-2`; only `t=-1` collapses, to F4. `t>=0` chooses each eight-cycle once |
| F12 | Proper divisors `1,2,3,4,6` are excluded by the printed comparisons, including `m=1`. For `m>=1` the level strictly increases, so representatives are distinct |
| E5/E9 | Direct least-period checks exclude the proper divisors; reversal is a cyclic rotation by one and six respectively. E5's forcing differs from F5's |

Different least periods cannot duplicate an orbit. The complete
possible period set is `{1,2,3,4,5,6,8,9,12}`, provided the full core
certificate agrees. Its least common multiple is 360; this says only
that `T_a^360` fixes the integral periodic locus, not that the polynomial
automorphism has finite order on its phase space.

## Every invariant-level count is finite and explicit

For F2, set `P=uv` and `S=u+v`. Then `a=S-P` and
`k=P(S-3)=P(P+a-3)`. Thus the distinct integer roots of
`P^2+(a-3)P-k=0`, followed by the strictly positive square/parity test
for `S^2-4P`, give exactly the unordered pairs `u<v`. This also covers
`a=1`; factoring `(u-1)(v-1)=0` alone would not give a finite list
without the level equation.

For F4 the discriminant is `(a+1)(a-7)+4k`; positivity removes the
period-two degeneration and parity selects integers. Its two roots are
one orbit, not two. F5 gives two roots of `t(t+1)=k` except that the
two roots at `k=0` give one orbit; no negative integer `k` can occur.
F8 and F12 are handled by their chosen representative ranges and the
positive-square tests for `k-1` and `4k-7`. Fixed, three-, six- and
nine-period cases are direct and consistent with their listed levels.

This proves finiteness for each `a,k`. Ordinary fixed counts are
`sum_(l|n) l*c_l(a,k)`, hence the stated finite dynamical product for
the per-level zeta follows. Without fixing `k`, F4 produces infinitely
many periodic points for every `a`; no all-level finite-count zeta is
defined by this result. Singular ordinary points were not removed.

## Exact symbolic receipt — distinct from finite exhaustion

The coordinator wrote and ran once the independent
[symbolic checker](check_symbolic_families.py). It neither imports nor
executes a finite-core enumerator and writes no output files.

Actual command from the repository root:

`python -B henon_dynamics/research_c419_c423/continuation_round2/integral_return_review/check_symbolic_families.py`

Environment: Python 3.12.3, SymPy 1.14.0. Exit status 0. It verified
all wraparound recurrence identities and level identities for all ten
table rows: 55 phases per identity, with free symbolic parameters.
It also checked the full-space invariant identity and the four printed
count-reduction/discriminant identities. Source SHA-256:

`be9ca47f3b7c8f94b43b25d6857f823f35f004407eff71807770dadf6dac40bd`.

The code uses explicit failure exceptions, not removable assertions.
The least-period, disjointness and exhaustion proofs are not delegated
to these substitution identities. No old computation, author core or
arithmetic diagnostic was rerun by the coordinator.

## Independent finite-core receipt and adjudication

The coordinator has now read the complete
[finite-certificate review](finite_core/REVIEW.md), its pre-run plan,
the whole 325-line independent program and the actual summary's
result/identifier fields. The program's per-amplitude data are retained;
the coordinator does not claim a second enumeration or manual reading
of all raw cycle records.

The reviewer used both signs, chose `q` before `u` by exact interval
intersection, walked the inverse map and identified cycles by complete
directed triple-state sets. The coordinator checked that these intervals
are exactly the necessary height and neighbor inequalities, including
zero coefficients; the recovered `a` is not a guessed cutoff. A visited
set checks the injectivity-based first-repeat argument explicitly.
Forward reconstruction verifies every returned native first period.
The full output comparison is made only after independent discovery.

Its actual single run used Python 3.12.3 and exited 0 in 3.37218 seconds:
149,732 signed seeds, 51,814 returning seeds, 37,239 height exits,
60,679 difference exits and 25,851 distinct oriented cycles. Every
author cycle was individually compared by parameter, full state set,
period and independently generated family label. Only E5 and E9 remain
outside the symbolic families. The 25,753 self-reversing cycles and
49 genuinely distinct reverse pairs agree with the F5 orientation rule.
The backward maximum of 18 steps is observed, not imposed; its differing
exit-type partition from forward iteration is not a classification error.

The independent code/JSONL SHA-256 values are respectively
`8bd343b599f9ed6c605b255dfe60b544a81375975083fd5d7ffb2b18a1d6c7c3`
and `0432cd5d8c35fe3cf9fdc0027451bf2e85d04eb880da6da1c03457571fffe35b`.
The coordinator ran a read-only `sha256sum` check on these and the
author proof, code, two original outputs and the independent symbolic
checker; the recorded input identifiers agree. This establishes that
the inspected evidence is the reviewed input, not a second proof run.
The final classification statement read here has SHA-256
`e07855ea457056387c471677fffe0c0414bb6773e3583a3bfb1eb4a4f58a5336`.

The finite review's conditional global premise is now supplied by the
separately passed analytic review and the coordinator's own check.
Combining those results closes the computer-assisted all-parameter
classification, not merely a bounded experiment. Neither the reviewer
nor coordinator claims proof-assistant kernel verification.

## Source ownership and final decision

The separate coordinator [source audit](SOURCE_AUDIT.md) records actual
primary reading and seventeen fresh searches. It deducts the ambient
cubic, unforced C413/M1 content, classical escape/group theory and the
first-pass F4 channel. The uniform forcing-eliminating proof and exact
complete classification form one substantive residual question.

All scoped review gates are now closed. The coordinator admits IR1 as
**one** substantial independent classification contract. It promotes
the original unclosed NG1 question; it is not counted as an additional
new question besides NG1. Earlier authored drafts retaining their
then-pending review language are historical snapshots; this adjudication
is the current status and does not rewrite their frozen run identifiers.

Together with M1 and AS2 the same batch now has **3/5 admitted contracts,
0 new manuscripts**. Formal evaluations, paper numbers, manuscript
writing and PDFs remain later batch gates. Source arithmetic does not
establish target arithmetic; `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
