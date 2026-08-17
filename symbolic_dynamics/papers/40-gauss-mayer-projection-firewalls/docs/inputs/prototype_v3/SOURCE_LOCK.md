# Paper 40 corrective source lock — SD-C42

## Status and authority boundary

- Candidate ID: `SD-C42`.
- Working title: **Trace, Order-Discriminant, and Norm Firewalls for the
  Two-Digit/Even-Iterate Gauss--Mayer Determinant**.
- Freeze status: `FINAL_CORRECTED_INPUT_SET_FROZEN_BEFORE_CANONICAL_M1_M20_RERUN`.
- This lock supersedes the source lock with SHA-256
  `2041dec0aebe85b773febc5c8ef7a61cc5dc4e2b8c6a8cd81a5ce0d413387362`.
  The supersession is forced by the DA M1--M20 findings recorded in
  `SOURCE_LOCK_SUPERSESSION_V2.md`.
- The earlier v1 prototype/control outputs and multiple in-flight corrective
  smoke-test outputs were already known while DA M1--M20 was still changing
  the contract and evaluators. This final corrective lock is therefore a
  disclosed retrospective correction, not an untouched prospective
  preregistration and not a claim that Paper-40 outcomes were unknown.
- The only timing claim is narrow and auditable: `CONTROL_LOCK.md` enumerates
  the exact corrected input set frozen before one empty-results canonical
  replacement rerun: `SOURCE_LOCK.md`, `MAYER_SOURCE_BOUNDARY.md`,
  `SELECTION_AUDIT.md`, the six control/prototype/test programs, the six local
  Route-card snapshots, and the listed seed/grid literals. No other package
  file is included in this prospective input set.
- Proof, ownership, Route, counterexample, literature, plan, report, result,
  summary, and manifest files are post-run dependent renderings. They receive
  hash/provenance binding but no prospective status. No novelty or priority
  credit is assigned to the corrective cycle or its witnesses.
- Paper 39 neither selected nor ranked this candidate. Its terminal-clean
  registry return is only a promotion-gate fact.
- Route A is evaluated under the literal authority evaluator v0.2.0. Route B
  is locked.

## 1. Independent selection rule

The selection universe is exactly the six source-locked, non-affine Session-4
registry candidates `SD-C01` through `SD-C06`. Apply this deterministic rule
to their own immutable Route cards.

1. Keep a card exactly when it proves a nonempty intrinsic primitive/repetition
   ledger and records `A2_ANALYTIC_DETERMINANT` with proved same-object
   determinant ownership. A ledger is nonempty even if it consists of one
   trivial primitive orbit; no unannounced nontriviality or Route-worthiness
   condition is allowed.
2. Among survivors, maximize the recorded A3 rung and then the A4 rung in the
   literal order of Route-A evaluator v0.2.0. Use the smaller candidate ID only
   as a final tie breaker.

The first filter leaves `SD-C01`, `SD-C02`, and `SD-C04`. In particular,
`SD-C02` survives because its card proves one period-one zero primitive orbit
and the same-object identities
`zeta_AM(z)=1/(1-z)` and `D_AM(z)=1-z`. It is not removed merely because that
ledger is trivial. `SD-C04` uniquely wins A3 and then A4:
`A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT`, versus
`A3_FAIL, A4_FAIL` for `SD-C01` and `SD-C02`.

The inherited `SD-C04` parent object is the one-digit Gauss shift with
`SigmaPrimitiveDigit` words, the branches $\phi_a$, the operator
$\mathcal L_s$, and the analytic determinant $\det(I-\mathcal L_s^2)$. It
does not supply a `RhoPrimitivePair` ledger or inherited A1 credit. Paper 40
newly freezes the re-indexed even iterate $K_s=\mathcal L_s^2$ on the pair
space, conjugate to the digit return $\sigma^2$, and must prove its pair primitivity, splitting,
orientation, completeness, repetition, branch order, and determinant
ownership from scratch. This is a typed refinement of a known operator, not a
claim of a new transfer-operator mechanism.

The corrected executable audit must parse all six cards from the exact local
byte snapshots under `inputs/route_cards/`, reproduce the
three-survivor set and winner, verify every card hash, and reject mutations
that delete a card, duplicate an ID, erase the `SD-C02` orbit, change its A2
verdict, or change the winning A3/A4 coordinates. These tests verify the rule;
they do not authorize the candidate.

## 1.1 Prior-result and claimed-delta boundary

Paper 1 already states that trace, discriminant, norm, or parity collisions do
not create a canonical rational-prime ledger. Its `SD-C04` Route card records
7,018 non-reversal trace-collision groups and requests the next
trace/composite-discriminant audit. Therefore Paper 40 does not claim discovery
of the qualitative mismatch, first trace collisions, a new Gauss/Mayer
mechanism, or a new two-variable zeta mechanism.

The claimed delta is only theorem-grade exact formalization and closure of
that pre-existing next-test request. The v1 attempt was source-locked before
its provisional run. The present final statement is a retrospective DA-driven
correction assembled with both v1 and in-flight corrective smoke outputs
known, then its exact corrected input set frozen before the single declared
canonical replacement rerun:

1. exactly three projections, with no post-result fourth map;
2. explicit in-domain collision and composite-ledger witnesses under one fixed
   ordered matrix convention;
3. all-orders trace recurrence and exact clock incompatibility;
4. preservation of the original digit marker under the paired return; and
5. a typed, hash-backed absence-of-declared-owner conclusion for scalar
   postselection in the frozen untwisted operator contract; and
6. an exact branch-matrix bridge tying the ordered monodromy and derivative
   roof back to the same Gauss inverse branches used by the Mayer operator.

No minimal-witness claim is made. The trace-10 example is retained only
because it is an explicit non-reversal collision across different pair
lengths.

## 2. Source object and typed primitivity

Let

$$
A(a)=\begin{pmatrix}a&1\\1&0\end{pmatrix},\qquad a\in\mathbb N,
$$

and for an ordered even digit word $w=(a_1,\ldots,a_{2k})$ set

$$
M(w)=A(a_1)A(a_2)\cdots A(a_{2k}).
$$

Let $X=\mathbb N^{\mathbb N}$ carry the one-digit left shift $\sigma$, and let
$X_2=(\mathbb N\times\mathbb N)^{\mathbb N}$ carry the one-pair left shift
$\rho$. The grouping bijection is

$$
\iota:X\longrightarrow X_2,\qquad
\iota(a_1,a_2,a_3,a_4,\ldots)=((a_1,a_2),(a_3,a_4),\ldots),
$$

and the typed return identity is

$$
\rho\circ\iota=\iota\circ\sigma^2.
$$

Thus $\sigma^2$ acts on $X$, while $\rho$ acts on $X_2$; the notation never
applies the digit-space map directly to pair space. One $\rho$ step consumes
exactly two digits. Both evaluators must verify this conjugacy on a frozen
nonperiodic fixture and reject the wrong map that shifts $X_2$ by two pairs.

A source object is a cyclic word of ordered pairs. Flattening preserves pair
order. Reordering, transposing, inverting, changing cyclic representative
before multiplication, or switching matrix convention is forbidden.
The global raw-index reversal needed to express the stored composition order
is a bijection on finite even digit words. Grouped into ordered pairs it sends
pair rotations to pair rotations with reversed orientation, so it descends to
cyclic `RhoPrimitivePair` classes and preserves primitivity. It changes the
representative/order bookkeeping, not the primitive-necklace set. A frozen
non-palindromic mutation must reject a two-pair shift or an unreversed block
order.

`RhoPrimitivePair`, `SigmaPrimitiveDigit`, and
`GeodesicPrimitiveClass` are three distinct types. The theorem uses only the
first: a primitive cyclic necklace in the pair alphabet. A determinant or
zeta-function identity does not provide an objectwise bridge among the three
types. In particular, a one-pair word is pair-primitive even when its two
flattened digits agree.

The exact relation between the first two types is a splitting law, not an
identity. A least-period-$n$ orbit of $\sigma$ splits under $\sigma^2$ into
$\gcd(n,2)$ cycles, each of length $n/\gcd(n,2)$. Thus odd periods remain one
cycle and even periods split into two. If $N_D(n)$ counts primitive
$\sigma$-necklaces over a $D$-digit alphabet and $N_{D^2}(k)$ counts
primitive pair necklaces, then

$$
N_{D^2}(k)=2N_D(2k)+\mathbf 1_{k\text{ odd}}N_D(k).
$$

For $D=2$ this gives pair counts $4,6,20$ at pair lengths $1,2,3$. The trace-4
words `((1,2))` and `((2,1))` are the two $\rho$ phases of one
$\sigma$-period-2 orbit, but they are distinct primitive factors of the frozen
$\rho$ ledger. Conversely, `((2,2))` is pair-primitive through the odd
$\sigma$-period-1 contribution although its flattened two-digit word is a
proper power. Both evaluators must reproduce this census and reject the
odd/even-swapped mutation.

## 3. Repetition, clock, and marker

For a pair word $w$ and $r\geq1$,

$$
M(w^r)=M(w)^r,\qquad T(w^r)=rT(w).
$$

Every pair contains two determinant-$-1$ digit matrices, so
$M(w)\in\mathrm{SL}_2(\mathbb Z)$. Write

$$
t(w)=\operatorname{tr}M(w),\qquad
\Delta(w):=\Delta_{\mathbb Z[M]}(w)=t(w)^2-4,
$$

$$
\lambda(w)=\frac{t(w)+\sqrt{\Delta(w)}}2,
\qquad T(w)=2\log\lambda(w)=\log\lambda(w)^2.
$$

Here $\Delta_{\mathbb Z[M]}$ is the order/characteristic-polynomial
discriminant, not a field fundamental discriminant or the discriminant of a
larger multiplier ring.

The sole free marker is $u$, counting one original Gauss digit. One $\rho$
step consumes two digits and carries $u^2$. A one-return marker, specialization
$u=1$, or a changed roof cannot earn same-marker or same-clock credit.

### 3.1 Exact Gauss branch--matrix bridge

For $\phi_a(z)=(a+z)^{-1}$ use the Möbius matrix

$$
B(a)=\begin{pmatrix}0&1\\1&a\end{pmatrix},\qquad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

With the standard column-vector Möbius convention, in which $B(a_1)B(a_2)$
represents $\phi_{a_1}\circ\phi_{a_2}$,

$$
\Phi_w=\phi_{a_1}\circ\cdots\circ\phi_{a_{2k}},\qquad
B_w=B(a_1)\cdots B(a_{2k}).
$$

The exact conjugacy is

$$
A(a)=JB(a)J,\qquad M(w)=JB_wJ.
$$

If $x_w$ is the attracting fixed point and
$B_w=\left(\begin{smallmatrix}\alpha&\beta\\\gamma&\delta\end{smallmatrix}\right)$,
then

$$
\gamma x_w^2+(\delta-\alpha)x_w-\beta=0,
\qquad \gamma x_w+\delta=\lambda_+(M(w)),
$$

and, because an even word has determinant one,

$$
-\log|\Phi_w'(x_w)|=2\log\lambda_+(M(w))=T(w).
$$

The expanding eigenvalue has polynomial $x^2-tx+1$. The derivative
multiplier $d_w=|\Phi_w'(x_w)|=\lambda_+^{-2}<1$ is a different algebraic
quantity and has polynomial

$$
x^2-(t^2-2)x+1.
$$

The norm label $P_N=\lambda_+^2$ is the root greater than one, whereas
$d_w=\lambda_+^{-2}$ is the root in $(0,1)$; their product is one. Neither
evaluator may conflate these root selectors or label the eigenvalue polynomial
as the derivative polynomial. Swapped-polynomial and swapped-root mutations
must fail. Each exact row records the two $\mathbb Q(\sqrt\Delta)$ values

$$
P_N=\frac{t^2-2+t\sqrt\Delta}{2},\qquad
d_w=\frac{t^2-2-t\sqrt\Delta}{2},
$$

and verifies their product is one; a decimal roof or a boolean stability flag
is not a substitute for this algebraic record.

Furthermore $B(w^r)=B_w^r$, so the branch derivative roof and matrix
repetition are the same-object repetition. The executable bridge witness is
the non-palindromic three-pair word
$(1,2,2,3,1,4)$, for which

$$
M_A=\begin{pmatrix}148&31\\105&22\end{pmatrix},\quad
B_w=\begin{pmatrix}22&105\\31&148\end{pmatrix},\quad t=170,
$$

and $x_w$ satisfies $31x^2+126x-105=0$, with
$\gamma x_w+\delta=85+2\sqrt{1806}=\lambda_+$. Reference and independent
evaluators must reject order and reversal mutations of this witness.

## 4. Operator, space, determinant, and ownership

Let

$$
(\mathcal L_s f)(z)=\sum_{a\ge1}(a+z)^{-2s}
f\!\left((a+z)^{-1}\right)
$$

be the Mayer Gauss transfer operator on the exact source-supported holomorphic
Banach space stated in `MAYER_SOURCE_BOUNDARY.md`. Define

$$
K_s=\mathcal L_s^2,\qquad
D_{42}(s,u)=\det(I-u^2K_s).
$$

In the declared nuclear domain, determinant multiplication gives

$$
D_{42}(s,u)=\det(I-u\mathcal L_s)\det(I+u\mathcal L_s).
$$

Only at $u=1$, and only with the domain/continuation qualifications in
`MAYER_SOURCE_BOUNDARY.md`, is the modular Selberg-zeta/Fredholm-determinant
identity invoked. This is a functional identity, not an objectwise primitive
pair/geodesic bijection. The bookkeeping marker $u$ does not create a new
arbitrary-$u$ Selberg identity.

The ownership conclusion is contract-relative: the frozen untwisted $K_s$
schema declares no projector for rational-prime scalar postselection. It is
not a universal nonexistence claim across prospectively defined twists.

### 4.1 Exact raw-iteration order for $K_s^k$

Write $j_{a,s}(z)=(a+z)^{-2s}$. Raw operator composition gives

$$
\mathcal L_s(\mathcal L_s f)(z)
=\sum_{a,b\ge1}j_{a,s}(z)j_{b,s}(\phi_a z)
f(\phi_b\circ\phi_a(z)).
$$

Therefore the stored pair in composition order is $(b,a)$, not the raw index
tuple $(a,b)$. More generally, for a stored flattened word
$w=(a_1,\ldots,a_{2k})$, globally reverse the raw indices and define

$$
G_{w,s}(z)=j_{a_{2k},s}(z)
j_{a_{2k-1},s}(\phi_{a_{2k}}z)\cdots
j_{a_1,s}(\phi_{a_2}\circ\cdots\circ\phi_{a_{2k}}z).
$$

Then the unrestricted dummy-index reversal is bijective and

$$
K_s^k f(z)=\mathcal L_s^{2k}f(z)
=\sum_{w\in\mathbb N^{2k}}G_{w,s}(z)f(\Phi_w(z)),
\qquad
G_{w,s}(z)=|\Phi_w'(z)|^s
$$

on the positive real branch (and with the source's holomorphic branch
convention on its complex domain). Hence the stored $B_w$, derivative roof,
and $K_s^k$ summand belong to the same ordered word.

For the non-palindromic witness $w=(1,2,2,3,1,4)$ at $z=1/4$ and $s=1$,

$$
\Phi_w(1/4)=\frac{442}{623},\qquad
G_{w,1}(1/4)=\frac{16}{388129}.
$$

Using the same raw index order without reversal instead gives the wrong values
$146/697$ and $16/485809$. Reference and independent evaluators must recover
the stored values by raw-index reversal and reject the same-index mutation.
They must compute the raw nested product recursively from
$x_i=\phi_{r_i}(x_{i-1})$ and
$\prod_i j_{r_i,1}(x_{i-1})$, then separately compare it with the stored
Möbius branch and derivative. Merely evaluating the derivative of a
pre-reversed product matrix does not test the $K_s^k$ expansion.

## 5. Exactly three projections

The complete projection family is

1. $P_t(w)=t(w)$;
2. $P_\Delta(w)=\Delta_{\mathbb Z[M(w)]}=t(w)^2-4$;
3. $P_N(w)=\lambda(w)^2$.

No fourth word-to-integer map, prime lookup, orbitwise accepted list, fitted
projector, selected direct sum, changed roof, or changed function space may be
introduced after results. Diagnostic primality testing of a computed exact
integer is allowed.

## 6. Frozen theorem target and witnesses

For every `RhoPrimitivePair` word, prove the branch bridge above and universal
items 1--4 below. Items 5--7 are existential named witnesses. Items 8--9 are
global conclusions about the full ledger and frozen ownership contract.

1. **Order-discriminant firewall.** $t\ge3$ and
   $\Delta=(t-2)(t+2)$; hence $\Delta$ is a rational prime exactly at $t=3$,
   where $\Delta=5$.
2. **Norm firewall.** $(t-1)^2<\Delta<t^2$, so $\lambda^2$ is irrational and
   is not a rational prime or rational prime power.
3. **Trace clock firewall.** $\lambda^2>t$, so
   $T=\log\lambda^2\ne\log t$; no constant rescaling agrees for all realized
   integer traces $t\ge3$. Every such trace is realized by the one-pair family
   $w_t=((1,t-2))$, with
   $M(w_t)=\left(\begin{smallmatrix}t-1&1\\t-2&1\end{smallmatrix}\right)$.
   The proof must use this all-$t$ family and the asymptotic
   $\log\lambda(t)^2/\log t\to2$ (plus the exact characteristic equation),
   not a bounded census.
4. **Trace repetition firewall.** With $q_r=\operatorname{tr}(M^r)$,
   $q_0=2$, $q_1=t$, and $q_r=tq_{r-1}-q_{r-2}$; in particular
   $q_2=t^2-2\ne t^2$.
5. **One-pair reversal collision.** `((1,2))` and `((2,1))` are distinct
   one-pair primitive necklaces with matrices
   $\left(\begin{smallmatrix}3&1\\2&1\end{smallmatrix}\right)$ and
   $\left(\begin{smallmatrix}3&2\\1&1\end{smallmatrix}\right)$. Both have
   $t=4$, determinant $1$, $\Delta=12$, and the same roof. Digit reversal is
   metadata only; no reversal quotient is declared.
6. **One-pair non-reversal collision.** `((1,4))` and `((2,2))` have matrices
   $\left(\begin{smallmatrix}5&1\\4&1\end{smallmatrix}\right)$ and
   $\left(\begin{smallmatrix}5&2\\2&1\end{smallmatrix}\right)$. They are
   distinct one-pair primitive necklaces, are not digit reversals of one
   another, and both have $t=6$, determinant $1$, $\Delta=32$, and the same
   roof.
7. **Cross-pair-length non-reversal collision.** `((2,4))` and
   `((1,1),(1,2))` have matrices
   $\left(\begin{smallmatrix}9&2\\4&1\end{smallmatrix}\right)$ and
   $\left(\begin{smallmatrix}8&3\\5&2\end{smallmatrix}\right)$. They are
   primitive, non-reversal, have pair lengths one and two, and both have
   $t=10$, determinant $1$, $\Delta=96$, and the same roof.
8. **Full-ledger firewall.** `((1,2))` already has composite trace $4$, so
   the untwisted full determinant is not a trace-prime selected product.
9. **Ownership firewall.** None of the three scalar maps is a declared
   reducing projector or twisted operator in the hash-frozen untwisted
   schema. Scalar postselection therefore has no declared same-operator
   Fredholm owner in this contract.

The bounded corrected census must include all three collision classes above.
It may report earlier classes inside its frozen finite box, but no such census
can create a minimality claim.

## 7. Sharp STOP/GO rule and quantifier coverage

### 7.1 Exact comparison determinant, sign, and marker convention

The positive trace-series comparison object is the reciprocal determinant

$$
D_{42}(s,u)^{-1}=\det(I-u^2K_s)^{-1},
$$

because $-\log D_{42}$ has positive Fredholm trace coefficients. For a
primitive pair word $w$ of pair length $k$, let
$d_w=|\Phi_w'(x_w)|=\lambda(w)^{-2}$. Its same-object source contribution is

$$
\prod_{j\ge0}\left(1-u^{2k}d_w^{s+j}\right)^{-1},
$$

whose $r$th coefficient in $-\log D_{42}$ is

$$
\frac{u^{2kr}d_w^{rs}}{r(1-d_w^r)}.
$$

Under a hypothetical bijection $w_p\leftrightarrow p$, the marked target is

$$
D_{\mathrm{prime}}(s,u)^{-1}
=\prod_p\left(1-u^{2k(w_p)}p^{-s}\right)^{-1},
$$

so its $r$th coefficient is exactly
$u^{2k(w_p)r}p^{-rs}/r$. At $u=1$ this is the ordinary rational-prime Euler
product $\zeta(s)$. The primitive-factor sign is minus inside each factor and
the coefficients of the logarithm of the reciprocal are positive. The marker
exponent is inherited from the source digit length; it is not silently changed
to $u^r$. The logarithmic derivative has target amplitude $\log p$.

For each $P\in\{P_t,P_\Delta,P_N\}$ define `ProjectionGO(P)` as the conjunction
of all conditions below on the full same-object primitive ledger and this
exact reciprocal-determinant convention.

- **integer-valued support:** every primitive label is a rational integer;
- **rational-prime support/selectivity:** every primitive label is a rational
  prime, there are infinitely many distinct labels, and no composite occurs;
- **one-to-one target multiplicity:** exactly one source primitive factor maps
  to each target rational prime, with no duplicate source species;
- **repetition:** the label of the $r$-fold temporal repetition is $p^r$ for
  every $r\ge1$;
- **clock and marker:** the unchanged derivative roof is $\log p$ and the
  original digit marker remains $u$;
- **weight/amplitude and sign:** the reciprocal-determinant coefficients are
  exactly $u^{2kr}p^{-rs}/r$ with positive logarithmic sign (equivalently
  logarithmic-derivative amplitude $\log p$); source orbit weights must match
  this normalization without an extra stability denominator or Selberg
  $k$-tower;
- **sign, orientation, and phase:** under the frozen target convention each
  rational prime has multiplicity one, Euler sign $+1$, one unoriented target
  species, and phase $0$ modulo $2\pi$; source multiplicity, reversal/orientation
  class, sign, and phase must map to those values at every repetition;
- **operator ownership:** a prospectively declared invariant/reducing operator
  sector owns exactly that selected trace, with the same multiplicities and
  marker at every repetition; and
- **control separation:** the claimed arithmetic signal separates from every
  mandatory A0/A1 control.

The source-derived stability amplitude, reciprocal-determinant sign, digit
marker $u^{2kr}$, and associated Selberg $k$-tower are recorded, not collapsed
into a scalar label. The source coefficient does not equal the target
coefficient even under the formal assignment $p=\lambda^2$, because
$1/(1-d_w^r)$ remains.

The untwisted real-$s$ source-control convention records Euler sign `+1` and
phase exponent `0 mod 97`; random-phase controls use nonzero exponents. Pair
necklaces are quotiented by cyclic pair rotation only. For
$w=((a_1,a_2),\ldots,(a_{2k-1},a_{2k}))$, digit reversal is the metadata map

$$
R(w)=((a_{2k},a_{2k-1}),\ldots,(a_2,a_1)).
$$

Each row records its canonical rotation representative, the canonical
representative of $R(w)$, whether the two coincide, and their unoriented
reversal-orbit ID. Reversal is never silently added to the object quotient.

The existential GO is then machine-literal:

$$
\mathrm{GO\_CANONICAL\_INTEGER\_PROJECTION}
\iff \bigvee_{P\in\{P_t,P_\Delta,P_N\}}\mathrm{ProjectionGO}(P).
$$

The decisive failure coverage is projection-specific:

| Projection | Integer-valued | Rational-prime support | One-to-one target multiplicity | Repetition | Clock | Reciprocal-determinant amplitude/sign/marker | Declared selected owner |
|---|---|---|---|---|---|---|---|
| $P_t$ | **pass** | fails: trace 4 is composite | fails: trace-4, trace-6, and trace-10 collisions | fails: $q_2=t^2-2$ | fails: $T>\log t$ | fails: source stability denominator remains | fails in frozen untwisted schema |
| $P_\Delta$ | **pass** | fails: prime only at $t=3$ | fails on every trace collision | fails: $\Delta(M^2)=t^2\Delta\ne\Delta^2$ | fails because $\lambda^2$ is irrational while $\Delta$ is integer | fails: source stability denominator remains | fails in frozen untwisted schema |
| $P_N$ | fails: labels are irrational | fails | fails on every trace collision | **pass:** $P_N(w^r)=P_N(w)^r$ | **pass:** $T=\log P_N$ | fails: $1/(1-P_N^{-r})$ remains | fails in frozen untwisted schema |

No single theorem item is claimed to eliminate the existential GO by itself.
The collective table proves that each of the three projection conjunctions is
false, hence their disjunction is false. The executable evaluator must build
each conjunction field by field and mutation-test removal of the decisive
support/multiplicity/clock/repetition coverage; it may not hard-code the final
STOP.

Two STOP codes are deliberately distinct. `STOP_CANONICAL_INTEGER_PROJECTION`
means no projection satisfies the full rational-prime Euler-ledger
conjunction. `STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION` means no
projection that is rational-integer-valued also preserves both the exact
source clock and temporal powers: $P_t$ and $P_\Delta$ are integer-valued but
fail clock and repetition, while $P_N$ passes clock and repetition but is not
integer-valued. The latter code never asserts that every projection fails
clock or repetition.

If all nine theorem items are proved and the corrected controls are valid, the
terminal tuple is

```text
GO_MODULAR_PRIMITIVE_LEDGER
GO_SAME_OBJECT_MAYER_DETERMINANT
STOP_CANONICAL_INTEGER_PROJECTION
STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION
STOP_OPERATOR_VISIBLE_SELECTOR_NOT_OWNED
ROUTE_A_REJECTED
```

The GO codes refer only to the intrinsic `RhoPrimitivePair` modular object and
its same-space determinant. They grant no rational-prime or cross-primitivity
credit.

## 8. Literal strict Route-A control lock

All controls below are mandatory executable records, not names. The base
finite object is the complete set of primitive pair necklaces over
`{1,2} x {1,2}` at pair lengths one through three (30 rows). The neighboring
object uses `{2,3} x {2,3}` at the same lengths. The simpler parent is the
one-digit `sigma` shift over `{1,2}` at digit lengths one through three.
Integer generation and Fisher--Yates permutations use the platform-independent
LCG

$$
x_{n+1}=(1103515245x_n+12345)\bmod 2^{31}
$$

with the per-control seeds frozen in `CONTROL_LOCK.md`.

### A0 controls — all seven are required

1. an algorithmically generated prime inventory followed by a nonidentity
   shuffle;
2. an integer inventory with exactly the same row count and prime density as
   the base trace inventory;
3. a composites-only inventory;
4. an inventory of composite base-2 Fermat pseudoprimes;
5. a nonidentity randomized permutation of base arithmetic labels;
6. the neighboring digit object; and
7. the simpler one-digit parent object.

### A1 controls — all six are required

1. a nonidentity shuffle of source-derived period tokens;
2. deterministic random signed rational weights not equal to the canonical
   unit weights;
3. deterministic random phase exponents modulo 97, not all zero;
4. random positive lengths preserving the exact frozen two-unit-bin histogram
   of the source-derived derivative roofs;
5. the neighboring candidate parameters; and
6. the simpler parent candidate.

Every control has a source-provenance field, a computed predicate, and a
dedicated negative mutation that must fail. The independent evaluator must
rederive pair necklaces and monodromies without importing the reference
module and must recompute the control predicates from the emitted schema.

Every baseline pair row also records rotation-only orientation, digit-reversal
metadata, source multiplicity one, untwisted sign `+1`, untwisted real-$s$
phase exponent `0 mod 97`, derivative multiplier $\lambda^{-2}$, and the
presence of the exact stability denominator. Mutations must delete or corrupt
reversal metadata, silently quotient a distinct reverse class, change
multiplicity, flip sign, inject a canonical phase, and remove the stability
denominator. The A/B/J bridge and the non-palindromic witness must be
independently recomputed.

### Ownership controls

The positive finite-dimensional owner uses
$K=\operatorname{diag}(2,3)$ and
$P=\operatorname{diag}(1,0)$. The evaluator must compute, not trust strings or
booleans:

- $P^2=P$ and $PK=KP$;
- compatible dimensions;
- $\operatorname{Tr}(PK^r)=2^r$ for every frozen $r=1,\ldots,6$;
- multiplicity one; and
- marker support of $\det(I-u^2K|_{\operatorname{ran}P})$.

Mutations must independently break idempotence, commutation, dimension,
trace multiplicity, and marker support. For the infinite baseline, only the
hash-backed statement “no owner is declared in this frozen untwisted schema”
is allowed.

### Bounded exact prototype and independent replay

The replacement prototype grid is fixed to canonical digit alphabets
`{1,...,D}` and neighboring alphabets `{2,...,D+1}` for `D=2,3,4`, with pair
lengths one through four. It is an exact-integer theorem audit, not a finite
Fredholm determinant evaluation. Its independent implementation must use a
separate aperiodic-necklace/continuant path and rederive every scientific and
contract field: theorem-failure predicates, all three collision witnesses,
the odd determinant-minus-one boundary, the sigma-squared splitting census,
the direct raw-transfer branch and weight, aggregate totals/status,
chronology/source binding, and the finite claim boundary. It may not omit a
field from comparison. Canonical tests must reject a raw-field mutation in
each component and must produce byte-identical output after relocating the
package; serialized paths are package-relative basenames only.

## 9. Route-rung decision map

No corrected rung is inherited by assertion.

- A0 is `A0_WEAK_ARITHMETIC_RELATION` only if the intrinsic continued-fraction
  arithmetic is verified, the exact rational-prime GO conjunction fails, and
  all seven A0 controls plus their mutations execute; otherwise A0 is
  `A0_FAIL` or `NOT_TESTABLE` as required by the evaluator.
- A1 is `A1_PASS_ANALYTIC` only if intrinsic pair primitivity, reproducible
  enumeration, rotation-only orientation and digit-reversal metadata, exact
  powers, monodromy, multiplicities, stability weights, sign, phase
  convention, the A/B/J branch bridge, and derivative roofs are proved and all
  six literal A1 controls plus mutations execute. Otherwise the verdict must
  be downgraded.
- A2 is `A2_ANALYTIC_DETERMINANT` only on the exact hash-bound Mayer function
  space and nuclear domain; no finite determinant earns this rung.
- A3 is at most `A3_PARTIAL_ANALYTIC_STRUCTURE`: the Selberg-zeta identity is
  nontrivial global modular structure, while the completed Riemann divisor,
  Gamma/pole/trivial-zero ledger, Riemann--von Mangoldt target count, and
  same-ledger Weil compression are absent.
- A4 is at most `A4_FORMAL_HINT`: known modular geometry is context, but no new
  quantum operator, domain, phase/weight theorem, or same-clock rational-prime
  lift is defined.

The corrected executable result and `ROUTE_STATUS_AUDIT.md` must re-evaluate
all five coordinates from this map. `route_b_invocation_allowed: false`.

## 10. Allowed and forbidden data

Allowed: positive digit words; exact pair necklaces; exact integer matrix
products; exact traces, determinants, order discriminants, and recurrences;
source-derived high-precision roofs for controls; diagnostic primality tests
of computed/generated integers; the six immutable registry cards; verified
primary sources; and hash-bound predecessor contracts.

Forbidden: rational-prime or Riemann-zero tables; hand-assigned log-prime
roofs or von Mangoldt weights; fitted phases; orbitwise accept/reject tables;
selected Euler products called Fredholm determinants; first-return
atomization; hidden reversal quotients; post-hoc nontriviality filters;
marker specialization used as identity; function-space switching; finite
determinant promotion; affine-branch coordinate transfer; post-result
projection repair; and Route B.

## 11. Source provenance

`SELECTION_AUDIT.md` records the immutable registry-card hashes and the
terminal-clean P39 ancestry. `CONTROL_LOCK.md` freezes only its exact
enumerated corrected inputs, seeds, and bounded grids before canonical
execution; dependent proof/report/literature files are post-run renderings.
Literature claims require a new audit
seal bound to this replacement SHA-256; the earlier audit bound to
`2041dec0...` cannot validate these corrected bytes.
