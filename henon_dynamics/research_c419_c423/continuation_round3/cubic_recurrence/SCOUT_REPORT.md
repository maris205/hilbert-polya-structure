# Round 3 arithmetic scouting: two candidates, no new admission

Date: 2026-09-07 UTC. This report concerns only the current
[third-pass lane](../SCOUT_PLAN.md), not the already completed round-2
documentation task. It does not change the coordinator's admission
state or reopen M1, AS2, IR1, or any sealed package.

## Outcome

| Candidate | Full frozen question | Result |
| --- | --- | --- |
| CR1, integral Duffing | Classify all ordinary integral cycles of $(y,y^3-Ay-x)$ for every integer $A$. | Rejected: literal subfamily of C417's completed all-monic-integral-cubic theorem on all $\mathbb Q^2$. No new computation. |
| CR2, rational McMillan | For every integer $A$, classify the entire ordinary periodic locus of $(y,Ay/(1+y^2)-x)$ on all $\mathbb Q^2$, including singular fibres and exact least periods. | Not closed: a rigorous infinite three-periodic fibre is obtained, but the all-parameter rational torsion-fibre atlas is not. No admission. |

The two-candidate limit is exhausted. No third candidate, coefficient
sweep, enlarged rational-height sample, manuscript, formal evaluation,
or C-number has been introduced. These outcomes do not supply either
of the two missing independent contracts.

## 1. The candidate comparison and source gate were real

The [frozen contracts](FROZEN_CONTRACTS.md) state the exact maps,
parameter fields, ordinary unit clock, domain, observable, closest
ownership, falsifier, and stop boundary before computation. CR1 was
rejected after reading the actual C417 theorem and its complete
template classification, not by a filename match. Substitution
$a=b=0$, $c=-A$ into $t^3+bt^2+ct+a$ contains CR1 verbatim.

CR2 was the only replacement and the only numerical diagnostic target.
The [source audit](SOURCE_AUDIT.md) records nineteen selected actual
fresh query formulations, exact access to relevant original theorem
sections, recent 2025/2026 McMillan work, inaccessible endpoints, and
the difference between a theorem read and metadata. C115 covers one
low-period example, not this full atlas. McMillan/QRT invariants,
elliptic translation, Mazur torsion, and division-polynomial order
tests are deducted as classical inputs, not counted as the increment.

The source-first skills influenced both decisions: literal containment
stopped CR1 without an experiment, and the known torsion machinery
prevented a short CR2 reconstruction from being promoted to a paper.
`proof-writer` required retaining the original all-parameter claim as
unproved while stating the partial theorem separately. No external
named-model review or independent source panel is claimed.

## 2. Exact partial result for CR2

The complete argument and execution receipt are in
[PARTIAL_PROOF.md](PARTIAL_PROOF.md). For $A=-5$, every rational point of

$$
C:\quad x^2y^2+x^2+y^2+5xy=4
$$

has ordinary least period three, and $C(\mathbb Q)$ is infinite. The
map $M_{-5}$ itself is not globally finite-order.

The three-coordinate seed is $(1,1/2,-3)$, so integrality already fails.
More substantially, the identity

$$
(1-xy)w+x+y
=\frac{y\bigl(I_A(x,y)+A+1\bigr)}{1+y^2},
\qquad w=\frac{Ay}{1+y^2}-x,
$$

proves the whole-fibre three-step return when $A=-5$, $I_A=4$.
There are no rational fixed points on that fibre. Explicit birational
charts take it to

$$
E:\quad Y^2=X^3-74X^2+1625X,
$$

with $P=(125,1000)$. Mazur's torsion-element order bound and the
frozen twelve-multiple certificate prove that $P$ has infinite order.
Its distinct multiples give infinitely many rational three-periodic
points. The denominator exclusions and curve nonsingularity are proved,
not assumed from the finite list.

The partial proof also locates the geometric singular levels exactly:

$$
K=0,\qquad K=-\frac{(A-2)^2}{4},\qquad
K=-\frac{(A+2)^2}{4}.
$$

Locating these levels is not classifying their rational dynamics.
No complete genus-one or singular-fibre atlas is asserted.

## 3. What was actually computed

Exactly one newly frozen mathematical program was run:
[check_fixed_fibre.py](check_fixed_fibre.py), using stdlib `Fraction`
arithmetic, at `2026-09-07T10:51:19.517499+00:00`. It exited zero with
`PASS_FIXED_FIBRE_ONLY`, checked twelve nonidentity elliptic multiples,
and verified twelve inverse-chart points and exact three-step cycles.

Its SHA-256 is
`88be3d20b4eadecc2d14d6c919ee7801872b2a1fe9890f3c36fe77831fc46882`;
the canonical twelve-point-list digest is
`9ef47a8432efaef1f357984279d8d3ec7910f26abad04c7786f28f2a94e1c860`.
The complete recorded scope, environment, and first four multiples
are preserved in the partial proof. The source digest remains unchanged.
The program was **not rerun** during this handoff. A hash is an integrity
fact, not an independent mathematical check.

This is not a parameter census and cannot establish a quantified claim
about all integers $A$ or rational levels $K$. No old program, GPU job,
paid API, mathematical build, or prior finite-core certification was run.

## 4. The precise remaining gap and the stop-loss decision

The full CR2 question needs a uniform arithmetic classification of
the specialized torsion-translation fibres with rational points,
their exact ordinary periods and rational loci, plus all singular
and degenerate cases, over every integer $A$. This investigation
has not supplied those parameter/locus equations with complete
rational-point solutions or a theorem eliminating the remaining cases.

It is insufficient to import the classical genus-one translation and
then instruct the reader to solve finitely many torsion equations for
each input fibre. The full atlas was chosen precisely to require more
than that familiar bounded-order procedure. A finite sample would not
close the missing uniform Diophantine assertions either.

The infinite $A=-5$ fibre is valuable as a falsifier of finite-total-point
or finite-alphabet shortcuts. It is nevertheless a short explicit
classical application, not the substantial independent all-parameter
closure needed for admission. The result does not prove the full
question false, globally open, or permanently unproductive; it proves
that this bounded attempt has not met its frozen success condition.

**Decision: stop CR2 here without admission.** No replacement third
candidate is opened. No claim is made about target Euler factors, root
numbers, automorphy, target zero correspondence, or a Hilbert–Pólya
realization. `NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.

## 5. Disjoint-path and stray-directory check

The scout's research writes are confined to this directory: the frozen
contract, the one diagnostic program, this report, the source audit,
and the partial proof. Shared state, admissions, Git and other lanes
remain untouched. Round 2 has not been edited or rerun in this task.

At the coordinator's request, a read-only inspection of the accidentally
placed repository-root `research_c419_c423/` found only the empty
`continuation_round3/positive_charp_new/` directory. No file or
`cubic_recurrence/` directory was present there. The scout's two earlier
file-creation calls both used correct absolute paths containing
`henon_dynamics`; no directory-creation command was found in its current
round's execution record. This observation does not identify the actual
creator of an empty shared directory. Nothing was deleted or moved.

## 6. Handoff validation

At `2026-09-07T11:12:52.081890+00:00`, one stdlib-only static check
read the four Markdown documents in this directory. Outside fenced
code blocks it checked inline local Markdown-link target existence:
22 local-link occurrences, 13 unique local targets, and zero broken
links. Twelve remote-link occurrences were counted but not requested
by this check. This is a local existence check, not validation of
remote content, anchors, arbitrary Markdown syntax, or linked proofs.

The same diagnostic parsed the one 124-line Python source to an AST
and compiled that AST in memory with `dont_inherit=True, optimize=0`.
Both passed. It did not import or execute that source, write bytecode,
or perform a mathematical rerun. Its SHA-256 exactly matched the
single-execution digest in Section 3. Exit status was zero.

The receipt paragraph was then added without adding or changing any
link target or modifying the Python source. These checks do not
substitute for independent proof review. No claim of such review is made.
