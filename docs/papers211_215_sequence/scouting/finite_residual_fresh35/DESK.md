# Fresh35 — three-site minimum current

2026-09-11 UTC. `AUTHOR_NEGATIVE / NO_PROMOTION`.
One root-suggested literal; root and this scout are contributors, not
independent reviewers. No execution, pilot, reserve, number or count change.

## Claim and status

For $n\ge1,N\ge0$, let $X_{n,N}=\{a\in\mathbb Z_{\ge0}^n:
\sum_i a_i=N\}$, with labelled cyclic indices. The literal is

$$c_i=\min(a_i,a_{i+1},a_{i+2}),\qquad
T(a)_i=a_i-c_i+c_{i-1}.$$

All currents use the old state. The proposed research claim is that this
provides temporal and evaluated inverse mechanisms materially beyond P213.
Status: `NOT CURRENTLY JUSTIFIED`; the temporal mechanism transfers directly
from P213 and no evaluated all-target inverse mechanism has been obtained.
The narrower temporal statements below are deductively proved, but have
zero residual credit in this desk.

## Collision and primary-source check, before proof extension

Read P213's full bounded contract; its original fresh07 proof lines 1–180;
its complete SOURCE_AUDIT.md; and the complete original
`scouting/transport_lane/PROOF_PACKAGE.md` (UUC). P213 already owns this
proof architecture: minimum subtraction, immutable zero barriers, original
positive runs, endpoint collection, integer-increment sharp clocks, and
then an evaluated comparison-chamber inverse. UUC explicitly subtracts
generic current-word reconstruction as an inverse theorem.

The literal is not equal to P213: on $(1,1,0)$, this rule is identity,
whereas P213 gives $(0,2,0)$. Nor is it equal to UUC. This distinction is
not a nonconjugacy theorem or a contribution by itself.

Local discovery covered current scouting and old scouting by UUC,
lookahead/anticipation, three-site and current/minimum expressions, then
all paper Markdown/TeX for lookahead/anticipation. The latter returned
only the unrelated P63 coding-anticipation usage. No exact old lookahead
literal was resolved by those searches. This is a source/collision gap,
not absence evidence or clearance. No old traffic theorem is imported.

Direct primary body read: Nishinari and Takahashi,
[Analytical Properties of Ultradiscrete Burgers Equation and Rule–184
Cellular Automaton](https://hakotama.jp/laboratory/works/public/98nt.pdf),
Section II, equation (16), browser-decoded lines 215–264. Its current is
$\min(M,U_j,L-U_{j+1})$, with receiver vacancy and a fixed cap, not the
three-site receiver-mass minimum here. The published 1998 record and
the author-file's 2001 front date are distinguished in P213's source audit.
This desk reads the equation, not the whole source's solution proof.
Additional anticipation-traffic search hits are navigation only. No exact
external owner or general lookahead exclusion was established.

## Assumptions, strategy and dependency map

Only nonnegative integer coordinates, fixed total and synchronous cyclic
updating are assumed. Set $m=\min_i a_i$ and $r=a-m\mathbf1$.
Dependency chain: closure and translation covariance imply minimum
invariance; permanent zeros split runs; an unchanging last site and a
strictly growing penultimate site imply termination and the sharp bound.
This is precisely the P213 barrier/collector strategy with one frozen
lookahead site, not a new temporal strategy. The proof-writer skill is
used to make that negative mechanism transfer explicit.

## Proof of the transferred temporal statements

1. Since $0\le c_i\le a_i$, the update is nonnegative; summing telescopes.
   Also $T(a+h\mathbf1)=T(a)+h\mathbf1$ for $h\ge0$.
   If $r_i=0$, then $c_i=c_{i-1}=0$, so that zero persists. Consequently
   the residual stays nonnegative and has a zero, proving minimum invariance.

2. Consider an original positive residual run with last site $e$. No mass
   crosses its zero boundaries. The last site is frozen because both
   $c_e$ and $c_{e-1}$ contain $r_{e+1}=0$. An interior site $i<e$ with
   positive predecessor cannot vanish: its incoming current
   $\min(r_{i-1},r_i,r_{i+1})$ is positive. The endpoint also cannot vanish.
   Thus a run can shorten only from its left, at most one site per step;
   it cannot split. A run of length one or two is already fixed.

3. For a run of length at least three, $e-1$ receives
   $\min(r_{e-2},r_{e-1},r_e)\ge1$ and has zero outgoing current.
   Write $M$ for original run mass, $b=r_e(0)$ and $d=r_{e-1}(0)$.
   Its nonfixed rounds are therefore at most $M-b-d$, since $r_e=b$
   stays frozen and $r_{e-1}\le M-b$. The run ends with mass $b$ at $e$
   and mass $M-b$ at $e-1$, with all earlier sites zero. Singletons stay
   unchanged. This explicitly describes the terminal state after adding
   $m$ back. Fixed and recurrent states are precisely residuals with no
   three consecutive positive sites.

4. For $n\le3$ all three-site currents agree around the cycle, so $T$ is
   identity. For $N\le2$ no residual positive triple exists. Otherwise,
   at $n\ge4,N\ge3$, step 3 bounds the entrance time by $N-2$.
   The state $(N-2,1,1,0,\ldots,0)$ attains it: for $0\le t\le N-2$
   its first three entries are $(N-2-t,1+t,1)$. Until the first vanishes,
   the only nonzero current equals one. Thus the sharp full-carrier height is

   $$H(n,N)=\begin{cases}0,&n\le3\text{ or }N\le2,\\
   N-2,&n\ge4,N\ge3.\end{cases}$$

   The example also proves noninjectivity in the nontrivial branch: the
   final transition and the terminal fixed state share an image. The
   parameter family includes identity boundary cases, which are not
   mislabelled individually nonbijective. No finite run underlies this proof.

## Independent inverse assessment and stopping point

For a target $y$, a current vector $u$ would reconstruct
$a_i=y_i+u_i-u_{i-1}$. Requiring nonnegativity and
$u_i=\min(a_i,a_{i+1},a_{i+2})$ is merely UUC's generic feasibility
reconstruction with another predicate. It is not an evaluated fibre formula.
Choosing a tie-broken minimum position from each triple converts these
conditions into linear equations and inequalities; without their elimination,
this is only the same chamber setup already subtracted in P213. This desk
does not claim that P213's interval atlas transfers unchanged, nor that it
has proved a matching sharp fibre exponent. Both are unproved here.

The changed terminal shape (two-site remnants instead of isolated spikes)
and $N-2$ clock do not create a different proof mechanism. A hypothetical
new inverse theorem would still need to overcome the explicitly required
distinct temporal-axis boundary. Therefore stop now: no pilot source or
parameter contract is proposed and no larger neighborhood is substituted.

## Evidence and open risks

Native local reads: 5d5cd6 (P213 contract), e40df1 (original temporal proof
and inverse setup), 40f0f4 (source audit), 8076fc (complete UUC proof).
Discovery receipts 9f08cc,5481db,57c26b are search returns, not full-corpus
proof audits. Primary body return: turn10941view0. These are conversation
receipts, not a frozen source capsule. The exact old lookahead-traffic
comparison remains unresolved; no global originality claim follows.

Authored proof, not independent acceptance. Research skill, research-lit
local-first/source boundaries and proof-writer claim triage were applied.
No scientific program, imports, host/process inspection, child, build,
Git, central edit or external upload. Only this new owned desk is written.
