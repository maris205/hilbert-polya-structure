# Round-two integral-return contracts

2026-09-07. Continuation of the same C419–C423 batch after its 2/5
research checkpoint. The admitted M1 and AS2 contracts are preserved;
neither is re-reviewed or recomputed. This lane writes only this directory.
AI-assisted internal research, not a manuscript or an admission decision.

## IR1: close the original NG1 question, or identify the exact remaining gap

**Object and quantifiers.** For every integer $a$, use
$$
T_a(x,y,z)=(y,z,yz+a-x),\qquad (x,y,z)\in\mathbb Z^3.
$$
All integer levels of
$K_a=x^2+y^2+z^2-xyz-a(x+y+z)$ and singular ordinary points are included.
One $T_a$ iterate is one clock step. Classify every ordinary integral
periodic point with no coordinate, period, parameter, or level cutoff.

**Inherited gap, not a new question.** The first pass proved only entrance
to a small-coordinate section and exhibited the already known four-step
word $(-1,t,-1,a+1-t)$. It did not classify the full return dynamics on
that section. C413 owns the complete $a=0$ case. General trace-map escape,
whole-group cubic-surface orbits and known finite periodic words are
deducted; none is silently substituted for this single-map all-$a$ answer.

### Decisive new structural lemma to test

Let $M$ be the maximum absolute scalar coordinate of an integral cycle,
and set $A=|a|$. Try to prove the following uniform extremal-channel
statement, with the explicit tentative bound $B(A)=2(A+2)^2$:

> If $M>B(A)$, a cyclic phase has the form $(b,v,c)$ with $|v|=M$
> and $b,c\in\{-1,0,1\}$. Every such periodic phase belongs to a
> finite explicit list of affine channels, obtained by a complete
> nine-case calculation (six cases after the actual time reversor).

The proposed argument uses maximality twice: first to bound both
neighbors by $2+A/M$, and then to exclude neighbor values $\pm2$.
The remaining recurrences are affine until a provably escaping quadratic
term appears. This is a symbolic all-parameter lemma, not a larger box.
The exact channel list, exceptional parameters, first-return times and
transitions must be proved, not inferred from sampled periods.

The tentative channel lengths emerging from preliminary hand inspection
are $4$ for general $a$, and possible additional $2,5,6,8,12$ channels
at exceptional parameters. These are hypotheses to verify; this document
does not assert their exhaustiveness or least-period claims.

### Completion and stop boundary

### Stronger difference-amplitude gate (frozen before any computation)

A subsequent hand-derived identity suggests a parameter-independent
closure, stronger than the height lemma above. For a periodic scalar
sequence define $d_i=x_{i+2}-x_i$. Direct subtraction gives
$$d_{i+1}+d_{i-1}=(x_{i+1}+1)d_i.$$
If $D=\max_i|d_i|>0$, an extremal difference is centered at
$s\in\{-3,-2,-1,0,1\}$. Test the following bounded proof program:

1. Resolve all five centered cases symbolically. The tentative universal
   cutoff is $D>100$; increasing a census box is not an allowed substitute.
2. For any center whose coordinate has magnitude $>3D+2$, use integrality
   and the identity at the two neighboring centers to force the general
   four-cycle channel. Thus, outside that channel, bounded $D$ gives a
   genuinely universal bounded coordinate core.
3. The $s=-1$ case already reduces by hand to the four-cycle channel or
   parameters $-6\le a\le2$. Check this deduction rigorously and close
   the finite exceptional parameters using the already frozen height
   lemma, not an unbounded parameter search.
4. If a universal finite core follows, enumerate its *entire* directed
   recurrent graph once, certify every excluded state, and publish its
   explicit terminal cycle words and parameter guards. The enumeration
   must be logically downstream of the symbolic exhaustion proof.

Before computation, the exceptional-parameter branch was also closed
by hand: its two subcases have words beginning $(u,-1,v,0)$ and
$(u,-1,v,1)$ respectively; a quadratic difference in the first and
an affine difference in the second exclude all unlisted parameters
when $D>100$. Consequently the proposed finite certification now uses
only $1\le D\le100$, not the earlier parameter-dependent height bound.
The precise inequalities are recorded in `IR1_PROOF.md`. That earlier
height lemma is no longer needed and must not become an additional
computation task.

The $D=0$ case is period dividing two and has the direct factorization
$a=1-(x_0-1)(x_1-1)$. This gate is a new proof strategy for IR1, not a
different question. Failure to prove the universal reduction remains an
IR1 failure, regardless of any promising finite sample.

After the extremal lemma, a successful complete result must resolve the
remaining parameter-dependent recurrent core and its exact interaction
with the affine channels. A finite ambient box with an unspecified
instruction to search for cycles is not a closed core classification.
An exact finite first-return description qualifies only if its exhaustive
states, transitions, exclusions, terminal cycles and parameter conditions
are actually proved for every $a$.

If the extremal lemma fails, record its counterexample or missing case.
If it succeeds but leaves the recurrent core essentially unclassified,
record that precise limitation and do not relabel the same gap as a new
question. No expanding coordinate census, period table, extra four-cycle
note or positive-word variation is allowed.

## IR2: one replacement slot, conditional and not yet instantiated

Only if IR1 cannot meet its complete-question gate, choose at most one
materially different nonlinear/integral arithmetic-return subtype.
Freeze its actual family, domain, native clock, complete observable,
closest-source deductions and decisive test before calculations.
Do not use a positive-word extension, the classical rank-two cluster conic,
or bare McMillan elliptic parametrization. This reserved slot is not a
second claimed research question until a concrete contract is written.

## Sources and execution boundaries

Fresh primary applicability checks will distinguish Roberts' Fricke–Vogt
escape setting, Cantat–Loray's parameter-dependent cubic maps and group
statements, and Baragar/Markoff–Hurwitz descent or counting results.
The source register will state exactly what was read. Current papers will
be checked where relevant, without attributing unseen theorems.

At the initial freeze, no mathematical computation had yet been executed
for this round-two lane. Any later finite symbolic check must test a specifically frozen
identity or unresolved case, not repeat old PASS evidence. No paid model,
GPU, manuscript, C-number assignment, formal evaluation, Git mutation,
external upload, or edit to the first-pass/accepted/sealed artifacts.
Source arithmetic remains distinct from target arithmetic;
NO_BAD_EULER_OR_ROOT_NUMBER remains unconditional.
