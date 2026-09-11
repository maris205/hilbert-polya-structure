# Fresh63 — sandwich squaring has no residual time mechanism

2026-09-11 UTC. Author: current_round_independent_scout.
**ZERO_NEW_LITERALS / ZERO_NOMINATIONS / NO_PILOT**.
This is a bounded author exclusion of a known semigroup construction, not
a new candidate or an assertion that finite-semigroup dynamics is exhausted.

## 1. Exact old and primary-source boundary

The tempting update $x\mapsto xax$, with fixed $a$, is squaring in the
semigroup variant $x\star y=xay$. Associativity follows directly from
associativity of the original multiplication. This includes noninvertible
$a$; no cancellation or change-of-coordinates inverse is required.

The actual old S01 definition was read in
`docs/papers127_131_sequence/scouting/algebraic/SCOUT.md`, lines 78–108
(native `d60acc`): $f\mapsto f\circ g\circ f$ on the full transformation
semigroup, with a fixed cyclic permutation $g$. The actual C13 and C18
rows were read in
`docs/papers122_126_sequence/scouting/algebraic/SCOUT.md`, lines 52–72
(`36810b`): matrix and path-algebra sandwiches with a fixed shift/arrow
sum. Their old pilot observations are not newly executed evidence.

The primary source Igor Dolinka and James East, *Semigroups of rectangular
matrices under a sandwich operation*,
[arXiv:1503.03139v2 PDF](https://arxiv.org/pdf/1503.03139), directly defines
$X\star Y=XAY$ even for rectangular matrices and discusses variants and
fixed-intermediate-map transformation semigroups in its opening two pages.
Those passages were actually read. Thus changing square matrices to
rectangular matrices does not avoid the same associative squaring adapter.
This paper is cited for the construction, not as an uninspected owner of
the exact elementary temporal formula below.

## 2. Full time law is ordinary monogenic squaring

Status: **PROVABLE AS STATED** for the following generic exclusion lemma.
Let $(S,\star)$ be any finite semigroup and $T(x)=x\star x$. Fix $x\in S$.
Write $x^{\star k}$ for its positive powers. The sequence of powers has an
index $\mu\ge1$ and least period $\lambda\ge1$: its initial $\mu-1$ terms
are transient and all later terms repeat with exact period $\lambda$.
Equivalently, two distinct exponents have equal powers exactly when both
are at least $\mu$ and congruent modulo $\lambda$.

These parameters exist because successive powers follow the deterministic
map $z\mapsto z\star x$ on a finite set. Its first repetition separates
the nonrepeating prefix from its cycle. This is the entire dependency for
the power equality criterion.

Write $\lambda=2^v d$ with $d$ odd, and define
$\operatorname{ord}_1(2)=1$. Then the exact entrance time of $x$ under $T$
and its eventual least period are
$$
h_T(x)=\max\{\lceil\log_2\mu\rceil,v\},\qquad
\ell_T(x)=\operatorname{ord}_d(2).
$$

**Proof.** Induction using associativity gives
$T^t(x)=x^{\star 2^t}$. For any $r\ge1$, equality between times $t$ and
$t+r$ holds exactly when
$$2^t\ge\mu\quad\text{and}\quad\lambda\mid 2^t(2^r-1).$$
The second condition requires $t\ge v$, since $2^r-1$ is odd. Once
$t\ge v$, it reduces to $d\mid2^r-1$; multiplication by $2^t$ is
invertible modulo odd $d$. Such an $r$ exists, and the least is
$\operatorname{ord}_d(2)$. Taking the first permissible $t$ proves both
formulas, including $\mu=1$ and $d=1$.

Applying this lemma to the sandwich semigroup gives the **entire** time
axis of $x\mapsto xax$, not merely a bound from left multiplication or
a many-to-one factor. In original notation its iterates are alternating
words with $2^t$ copies of $x$ and $2^t-1$ copies of $a$. The correct
obstruction is associative power dynamics, not an assumption that the
fixed sandwich element is a unit.

## 3. Why this desk stops

The generic index and period may themselves be difficult to evaluate in
an arbitrary supplied semigroup, but that difficulty does not create a
new nonlinear temporal mechanism. No different natural finite semigroup
or ideal operator with a proved residual time law and evaluated inverse
was obtained in this bounded desk. An arbitrary-root equation or an
uncomputed sum over semigroup elements would not supply the missing
inverse/enumeration axis. No exceptional parameter, ideal restriction or
rectangular decoration was introduced to fill the seat.

The parent explicitly permits reuse of an ordinary inverse mechanism
when a substantive new nonlinear time theorem survives. Here no such
time residual survives the exact variant-semigroup identity. P214's
separate local-ring recurrence and the excluded rowmotion/blocker/QIS
families were not reopened.

## 4. Evidence and scope limits

The broad sandwich archive search (`0f9002`) was truncated and served only
navigation; the two specific original reads above supply the old literal
boundary. Initial arXiv HTML openings for 1503.03139 and 1803.00724 returned
406. The later 1503.03139 PDF opened successfully, with version stamp
15 August 2016 and title-page date 16 August 2016. No full 35-page source
audit, screenshot review, scientific replay or global novelty check is
claimed. Source snippets from secondary sites are not proof inputs.

Only this desk was written. No code, import, parser, scientific experiment,
pilot, nested agent, new paper number, central-index edit, Git operation
or external write occurred. There is no reserve or independent-gate claim.
