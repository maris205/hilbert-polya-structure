# Replacement algebra/arithmetic scout

**Status:** internal discovery and hostile novelty gate only; **HOLD
EXTERNAL**.  The handles below are audit labels, not manuscript numbers.  No
novelty, priority, release, or submission claim is made.

**Search snapshot:** 2026-08-31 UTC.

## 1. Outcome

This replacement lane audited **24 new literal self-maps** not present in the
117-system breadth run.  It deliberately excluded ordinary linear and
unipotent actions, bare power maps, bounded-rank module functors, artificial
closure operators, and cosmetic copies of mechanisms already used in the
earlier portfolio.  The carrier mix is:

- divisors and complementary factorizations of an integer;
- binomial, factorial, and Catalan sections reduced back to a prime-power
  carrier;
- valuation-controlled maps on finite local rings; and
- monic divisors of split squarefree polynomials over finite fields.

The verdict is intentionally severe:

- **one internal promotion with an external novelty hold:** `D01`;
- **23 kills**; and
- no resurrection of the previously killed exterior-square or truncated
  Frobenius candidates.

`D01` is the complementary-factor disparity map

\[
   \Delta_n(d)=
   \frac{\operatorname{lcm}(d,n/d)}{\gcd(d,n/d)}
   =\frac{n}{\gcd(d,n/d)^2},\qquad d\mid n.
\]

Its signal is not a plot.  For arbitrary
\(n=\prod_i p_i^{e_i}\), it has an exact all-iterate formula, sharp depth and
depth layers, a complete recurrent census, every iterate-fixed count and hence
every exact-period count, and every one-step target fibre.  The hostile catch
is equally explicit: its binary operation is exactly the previously named
arithmetic \(Z\)-rule, and after prime-exponent coordinates the proposed
self-map is a product of finite full-tent maps.  Both ingredients receive zero
credit.  The residual is at most a focused arithmetic-dynamics note unless a
specialist owner search raises rather than lowers the ceiling.

## 2. Exact executable contract

[`verify_replacement_algebraic.py`](verify_replacement_algebraic.py) uses
Python integers only.  Every displayed finite carrier is completely
enumerated.  There is no floating point, sampling, random seed, network access,
third-party package, or timestamp in the executable.

Reproduce the frozen [`CANONICAL.txt`](CANONICAL.txt) with

```bash
cd docs/papers132_136_sequence/replacement_scout/algebraic
cmp -s CANONICAL.txt <(PYTHONDONTWRITEBYTECODE=1 python3 verify_replacement_algebraic.py)
```

The breadth ledger contains **13,762 parameter-labelled states**.  Focused
checks add four large `D01` divisor boxes and four binomial-section boxes.  The
run makes **1,539,136 exact assertions** and returns `STATUS=PASS`.  Enumeration
is falsification evidence, not proof and not novelty evidence.

Conventions used below are \(c=n/d\), \(s(d)=\sigma(d)-d\), and
\(v_p(0)=e\) when a valuation is clipped on \(\mathbb Z/p^e\mathbb Z\).  A
polynomial gcd is made monic.

## 3. Permanent 24-system ledger

### 3.1 Divisor and factorization carriers

The first ten maps were completely enumerated on
\(n=3^7,3^4 5^3,3^3 5^2 7^2\), for 64 divisor states per map.  The odd
parameters in `D02`--`D04` remove the exceptional extra factor of two when two
summands have the same valuation.

| Handle | Literal self-map | Exact pilot fingerprint | Hostile disposition |
|---|---|---|---|
| `D01` | \(d\mapsto\operatorname{lcm}(d,c)/\gcd(d,c)\). | Periods `1,3`, tail at most 3 in breadth; the focused 635-state theorem check verifies all iterates and all fibres. | **PROMOTE INTERNAL / OWNER-HEAVY NOVELTY HOLD.** The atomic \(Z\)-rule is directly owned; only the fixed-complement functional graph in Section 4 survives. |
| `D02` | \(d\mapsto\gcd(n,d+c)\). | Fixed-only, tail at most 2, four to nine image points. | **KILL.** Coordinatewise complementary meet/fold with shallow dynamics. |
| `D03` | \(d\mapsto\gcd(n,d^2+c)\). | Periods `1,2`, tail at most 5. | **KILL.** The exponent rule \(a\mapsto\min(2a,e-a)\) has no comparable all-iterate spine and is a weaker sibling of `D01`. |
| `D04` | \(d\mapsto\gcd(n,|d^2-c|)\). | Periods `1,2`, tail at most 3. | **KILL.** `D03` plus the isolated equality jump \(3a=e\); no independent theorem value. |
| `D05` | \(d\mapsto\gcd(n,d\varphi(c)+c\varphi(d))\). | At most two-cycles, image size at most 3 in the boxes. | **KILL.** Totient/Pratt relation engine already occupied; changing the Boolean gate is zero credit. |
| `D06` | \(d\mapsto\gcd(n,d\varphi(d)+c\varphi(c))\). | Periods `1,2`, tail at most 4. | **KILL.** Same totient-support engine, with no stable fibre law. |
| `D07` | \(d\mapsto\gcd(n,\varphi(d)+\varphi(c))\). | Fixed-only, image size 3--4. | **KILL.** Totient-value collapse and no recurrent residual. |
| `D08` | \(d\mapsto\gcd(n,|\varphi(d)-\varphi(c)|)\). | Fixed-only, tail at most 4. | **KILL.** Difference instead of sum does not escape the same owner/mechanism boundary. |
| `D09` | \(d\mapsto\gcd(n,s(d))\). | Periods `2,3,4`, tail at most 3; no fixed state in the boxes. | **KILL OWNER.** The apparent recurrence is a finite restriction of aliquot iteration and has no uniform formula. |
| `D10` | \(d\mapsto\gcd(n,\tau(d))\). | One recurrent fixed point; image size at most 5. | **KILL.** Divisor-count collapse. |

Four further arithmetic sections and one factorial map were checked separately.

| Handle | Literal self-map and carrier | Exact pilot fingerprint | Hostile disposition |
|---|---|---|---|
| `D11` | On divisors of \(p^e\), \(d\mapsto\gcd(p^e,d!)\). | 19 states across \(2^8,3^5,5^3\); three fixed points and tail at most 3. | **KILL.** A capped Legendre-valuation threshold calculation. |
| `D12` | On \(0\le k\le p^e\), \(k\mapsto\gcd(p^e,{p^e\choose k})\). | 337 states; every state reaches an \((e+1)\)-point involution in at most one step. | **KILL OWNER/THIN.** Kummer makes the whole graph a one-line corollary; see Section 5.2. |
| `D13` | Same interval, \(k\mapsto\gcd(p^e,{2k\choose k})\). | Fixed-only recurrence, tail at most 2; image sizes 4--8. | **KILL OWNER.** Base-\(p\) carry statistics own the signal. |
| `D14` | Same interval, \(k\mapsto\gcd(p^e,\frac1{k+1}{2k\choose k})\). | Fixed-only recurrence, tail at most 2; image sizes 4--7. | **KILL OWNER.** Catalan/binomial valuation theory owns the reduction. |

### 3.2 Valuation-controlled local-ring maps

Each map below was completely checked on
\((p,e)=(2,9),(3,6),(5,4)\), a total of 1,866 residues per map.

| Handle | Literal self-map on \(\mathbb Z/p^e\mathbb Z\) | Exact pilot fingerprint | Hostile disposition |
|---|---|---|---|
| `V01` | Fix 0; otherwise \(x\mapsto x+p^{v_p(x)}\). | Unique recurrent fixed point; sharp observed tail 16. | **KILL DIRECT/INTERNAL.** `lowbit` successor/Fenwick arithmetic and the prior valuation-erasure lane consume the mechanism. |
| `V02` | Fix 0; otherwise \(x\mapsto x-p^{v_p(x)}\). | Unique recurrent fixed point; sharp observed tail 16. | **KILL.** Base-\(p\) digit-sum descent, again inside the prior valuation lane. |
| `V03` | Fix 0; otherwise \(x\mapsto p^{v_p(x)}-x\). | Periods `1,2`, tails through 9. | **KILL THIN.** A valuation-gated reflection; each stable shell is an involution. |
| `V04` | Fix 0; otherwise \(x\mapsto x+p^{e-1-v_p(x)}\). | Periods `1,2,3,4,5,8,9,16,25,27`; at most two preimages per target. | **KILL DESPITE SIGNAL.** Shell translations give the complete explanation in Section 5.3. |
| `V05` | \(x\mapsto x+p^{v_p(x^2+1)}\), with valuation clipped at \(e\). | Periods include 256 and 729; tails through 15. | **KILL CONTROL.** For \(p=3\), \(x^2+1\) is always a unit and the map is just the full translation \(x\mapsto x+1\); the remaining parameters have no uniform residual. |
| `V06` | \(x\mapsto x+p^{v_p(x(x-1))}\), clipped at \(e\). | Exactly two recurrent fixed residues; tails through 15. | **KILL.** Hensel-defect erosion without a second theorem. |

### 3.3 Polynomial-factorization carriers

Let \(M=\prod_{a=0}^{r-1}(x-a)\in\mathbb F_p[x]\), let \(f\) range over
the monic divisors of \(M\), and write \(c=M/f\).  The parameters
\((p,r)=(7,5),(11,6),(13,7)\) contribute 224 states per map.

| Handle | Literal self-map | Exact pilot fingerprint | Hostile disposition |
|---|---|---|---|
| `F01` | \(f\mapsto\gcd(M,f'+c)\). | Periods `1,2,3`, tails through 5. | **KILL.** Parameter-sensitive factor evaluation; no all-parameter clock, census, or fibre law. |
| `F02` | \(f\mapsto\gcd(M,ff'+c)\). | Only two-cycles, no fixed state; tails through 3. | **KILL.** Large fibres but no structural spine. |
| `F03` | \(f\mapsto\gcd(M,f'c-fc')\). | Constant image 1 in every box. | **KILL IDENTITY.** At a simple root of either complementary factor the Wronskian is nonzero, so the gcd is 1 immediately. |
| `F04` | \(f\mapsto\gcd(M,f^2+c')\). | Periods `1,4`, tails through 5. | **KILL.** A finite anomaly without an invariant or parameter-uniform census. |

## 4. Surviving theorem contract for `D01`

### 4.1 Coordinate reduction and all iterates

Write

\[
 n=\prod_{i=1}^r p_i^{e_i},\qquad
 d=\prod_{i=1}^r p_i^{a_i},\qquad 0\le a_i\le e_i.
\]

Then

\[
 v_{p_i}(\Delta_n(d))=|2a_i-e_i|.
\]

Put \(j_i=e_i-a_i\), and for \(0\le u\le 2e\) let

\[
 \|u\|_{2e}=\min(u\bmod 2e,\;2e-(u\bmod 2e)).
\]

The complementary coordinate follows the full finite tent map

\[
 j_i\longmapsto \|2j_i\|_{2e_i}.
\]

Consequently the complete iterate is

\[
 \boxed{
 \Delta_n^t(d)=
 \prod_i p_i^{,e_i-\|2^t(e_i-a_i)\|_{2e_i}}
 }
 \qquad(t\ge0).
\]

This is an equality of literal integers, not merely a semiconjugacy statement.
The verifier checks it for every state in four focused boxes and every
\(0\le t\le12\).

### 4.2 Sharp transients and complete recurrent census

Let \(s_i=v_2(2e_i)\), with the convention \(v_2(0)=+\infty\).  A state
is recurrent exactly when

\[
 2^{s_i}\mid(e_i-a_i)\quad\text{for every }i.
\]

Its exact preperiod is

\[
 \boxed{
 \operatorname{depth}(d)=
 \max_i\max\{0,\ s_i-v_2(e_i-a_i)\}
 }.
\]

Hence the sharp global depth is \(\max_i s_i\).  If
\(q_i=(2e_i)/2^{s_i}\) is odd, the recurrent-state count is

\[
 \boxed{\#\operatorname{Rec}(\Delta_n)=\prod_i\frac{q_i+1}{2}}.
\]

More strongly, the cumulative depth distribution is

\[
 \boxed{
 \#\{d:\operatorname{depth}(d)\le t\}
 =\prod_i\left(
 \left\lfloor\frac{e_i}{2^{\max(s_i-t,0)}}\right\rfloor+1
 \right)
 }.
\]

Subtracting the expression at \(t-1\) gives every exact depth layer.

### 4.3 Fixed iterates, exact periods, and cycles

For every \(t\ge1\), fixed points lift to the two congruences
\(2^t j_i\equiv \pm j_i\pmod{2e_i}\).  Taking the sign quotient gives

\[
 \boxed{
 \#\operatorname{Fix}(\Delta_n^t)
 =\prod_i
 \frac{gcd(2e_i,2^t-1)+\gcd(2e_i,2^t+1)}{2}
 }.
\]

Thus no separate orbit classification is needed to obtain the exact-period
point and cycle counts:

\[
 \#\operatorname{Per}_{=m}
 =\sum_{r\mid m}\mu(m/r)\#\operatorname{Fix}(\Delta_n^r),
 \qquad
 \#\operatorname{Cycles}_{m}=\frac1m\#\operatorname{Per}_{=m}.
\]

Generic Möbius inversion itself is zero credit; the admissible content is the
explicit arithmetic fixed-iterate input.

### 4.4 Every target fibre

For a target \(y=\prod_i p_i^{b_i}\mid n\), define

\[
 \kappa(e,b)=
 \begin{cases}
 0,&e\not\equiv b\pmod2,\\
 1,&e\equiv b\pmod2\text{ and }b=0,\\
 2,&e\equiv b\pmod2\text{ and }b>0.
 \end{cases}
\]

Solving \(|2a_i-e_i|=b_i\) independently gives

\[
 \boxed{\#\Delta_n^{-1}(y)=\prod_i\kappa(e_i,b_i)}.
\]

In particular,

\[
 |\operatorname{im}\Delta_n|
 =\prod_i(\lfloor e_i/2\rfloor+1),
 \qquad
 \max_y|\Delta_n^{-1}(y)|=2^{\omega(n)}.
\]

The maximum is attained at \(y=n\); its preimages choose exponent 0 or
\(e_i\) independently, i.e. they are the unitary divisors of \(n\).

### 4.5 Focused falsification boxes

The focused verifier exhausts

\[
 2^{12},\quad 3^9 5^6,\quad 2^8 3^7 5^5,
 \quad 2^5 7^4 11^3,
\]

for **635 divisor states**.  It checks the coordinate identity, all iterates
through time 12, every target fibre, fixed-iterate counts through time 12,
every exact state depth, the recurrent count, and all cumulative depth layers.
The sharp observed tail is 4 and the recurrent counts are `2,10,12,6`.

## 5. Hostile subtraction and kill certificates

### 5.1 What receives exactly zero contribution credit for `D01`

| Ingredient | Zero-credit owner/reason | Residual retained |
|---|---|---|
| \(\gcd(u,v)\operatorname{lcm}(u,v)=uv\) and prime-exponent coordinates | Elementary arithmetic. | None. |
| The atomic rule \(Z(a,b)=ab/\gcd(a,b)^2\), equivalently \(\operatorname{lcm}(a,b)/\gcd(a,b)\), and its absolute-difference action on prime exponents | Directly studied by Cobeli--Zaharescu in [*A game with divisors and absolute differences of exponents*](https://arxiv.org/abs/1411.1334) and by Cobeli--Prunescu--Zaharescu in [*A growth model based on the arithmetic Z-game*](https://arxiv.org/abs/1511.04315). | Neither the operation, its name, nor exponentwise absolute difference. |
| The full tent map, its symbolic dynamics, and its connection to radix expansions | Generic tent-map theory is mature; for example Scheicher--Sirvent--Surer study tent-map/beta-expansion dynamics in [*Dynamical properties of the tent map*](https://doi.org/10.1112/jlms/jdv071). | None of the generic interval dynamics. |
| Folding multiplication by 2 modulo \(2e\) by the sign involution | Elementary cyclic-group quotient. | None. |
| Product decomposition over prime powers | Standard valuation bookkeeping. | None. |
| Möbius inversion from fixed points to exact periods | Standard finite dynamics. | None. |
| The 635-state pilot | Falsification only. | None. |

After those subtractions, the proposed residual is precisely the conjunction
of: feeding the **fixed complementary pair** \((d,n/d)\) into the owned
\(Z\)-rule and iterating the resulting self-map on all divisors of arbitrary
\(n\); its literal all-iterate formula; sharp transient layers; explicit
iterate-fixed arithmetic; and every target fibre.  A paper that merely says
“this is the \(Z\)-rule” or “this is a tent map” has zero residual and must be
killed.

The main hostile risk is obvious: the whole proof becomes short once the
exponent coordinate is written down.  Therefore the value ceiling is a
focused short note, not a broad algebraic-dynamics claim.  External promotion
requires both (i) a specialist literal/equivalent-map owner search and (ii) a
written proof showing that all four theorem blocks survive unchanged.

### 5.2 Why the exact binomial graph is still killed

Kummer's carry theorem gives, for \(1\le k\le p^e\),

\[
 v_p{p^e\choose k}=e-v_p(k).
\]

Thus `D12` maps every state in one step to a prime power, and

\[
 p^a\longmapsto p^{e-a}.
\]

The recurrent graph is merely the involution \(a\leftrightarrow e-a\).  Its
pointwise fibres are

\[
 \#F^{-1}(1)=2,
 \qquad
 \#F^{-1}(p^b)=p^b-p^{b-1}\quad(1\le b\le e).
\]

The verifier checks all of these identities on 2,213 states, but they add no
new mathematics after Kummer.  Modern primary work already counts binomial
coefficients by their \(p\)-adic valuation via carry recurrences; see Rowland,
[*A matrix generalization of a theorem of Fine*](https://arxiv.org/abs/1704.05872).
Central-binomial and related valuations are likewise a direct subject of
Straub--Amdeberhan--Moll,
[*The p-adic valuation of k-central binomial coefficients*](https://arxiv.org/abs/0811.2028).
Exact dynamics does not override zero residual.

### 5.3 Why the richest valuation pilot is also killed

For `V04`, put

\[
 K_{p,e}(x)=x+p^{e-1-v_p(x)}\pmod{p^e},\qquad K_{p,e}(0)=0.
\]

If \(a=v_p(x)<(e-1)/2\), the valuation shell is invariant and division by
\(p^a\) turns the update into translation by \(p^{e-1-2a}\) modulo
\(p^{e-a}\).  Hence every point on that shell has period \(p^{a+1}\), and
the number of such cycles is

\[
 (p-1)p^{e-2a-2}.
\]

If \(a>(e-1)/2\), one step lands on the mirror low shell
\(e-1-a\).  When \(e\) is odd, the middle shell increments its unit part
until a carry exits the shell, in at most \(p\) steps.  This explains every
long period in the pilot without a new mechanism.  It is a deliberately
hostile kill: a beautiful period set is not a paper when valuation-shell
translations give it for free.

The broad theory of compatible and ergodic maps on \(p\)-adic integer spaces
is already substantial; see Anashin,
[*Ergodic Transformations of the Space of p-adic Integers*](https://arxiv.org/abs/math/0602083).
The binary `lowbit` arithmetic in `V01` is also the update geometry behind
Fenwick's original binary indexed tree
[*A new data structure for cumulative frequency tables*](https://doi.org/10.1002/spe.4380240306).

### 5.4 Other direct owner and identity kills

- `D09` inherits the mature and still active aliquot-iteration problem.  The
  current primary computational boundary includes Chum--Guy--Jacobson--Mosunov,
  [*Numerical and Statistical Analysis of Aliquot Sequences*](https://arxiv.org/abs/2110.14136).
  Adding a gcd with a fixed \(n\) is not automatically a residual theorem.
- `D13`--`D14` are carry/valuation projections.  Their short tails are caused
  by immediate image collapse, not hidden recurrence.
- `F03` is killed algebraically before any dynamics: squarefreeness makes its
  Wronskian coprime to \(M\).  More generally, polynomial gcd and finite-field
  factorization are standard machinery; see Brent--Zimmermann,
  [*A Multi-level Blocking Distinct Degree Factorization Algorithm*](https://arxiv.org/abs/0710.4410).
- `F01`, `F02`, and `F04` retain small-box cycles but fail the minimum contract:
  no parameter-uniform iterate, recurrent census, endpoint basin, or pointwise
  fibre theorem emerged.

## 6. Literal/equivalent-map owner search

The search was run against current web-visible primary literature through the
snapshot date.  Queries included exact strings and algebraically equivalent
forms, among them:

```text
"lcm(d,n/d)/gcd(d,n/d)" iteration dynamics
"n/gcd(d,n/d)^2" divisor map
"|2a-e|" finite tent map divisor dynamics
"Z(d,n/d)" arithmetic game
"ab/gcd(a,b)^2" functional graph divisors
"n/gcd(d,n/d)^2" unitary bi-unitary divisor
"gcd(p^e, binomial(p^e,k))" iteration
"x + p^{v_p(x)}" dynamical system
"gcd(M, f' + M/f)" polynomial dynamics
```

The equivalent-operation search did locate the direct arithmetic \(Z\)-game
owners.  No primary source was located for the further specialization
\(d\mapsto Z(d,n/d)\) as a self-map of the full divisor set, or for the
conjunction of theorem blocks in Section 4.  That is only a bounded non-hit,
never evidence of novelty or priority.  The primary owners found in the same
search force the following subtraction boundary:

| Search cluster | Primary source found | Consequence |
|---|---|---|
| Absolute differences of prime exponents | [Cobeli--Zaharescu 2014](https://arxiv.org/abs/1411.1334) | The exponentwise absolute-difference game is directly owned. |
| Arithmetic \(Z\)-rule | [Cobeli--Prunescu--Zaharescu 2015](https://arxiv.org/abs/1511.04315) | The operation \(ab/\gcd(a,b)^2\) and its name are directly owned; only the fixed-complement functional graph can be residual. |
| Tent and radix dynamics | [Scheicher--Sirvent--Surer 2016](https://doi.org/10.1112/jlms/jdv071) | All generic tent, symbolic, and radix facts are zero credit. |
| Binomial valuation distributions | [Rowland 2017](https://arxiv.org/abs/1704.05872) | Kummer/carry recurrences and valuation counts are zero credit. |
| Central-binomial valuations | [Straub--Amdeberhan--Moll 2008](https://arxiv.org/abs/0811.2028) | `D13`/`D14` cannot claim their valuation mechanism. |
| Finite/local \(p\)-adic maps | [Anashin 2006](https://arxiv.org/abs/math/0602083) | Generic shell, compatibility, and ergodicity language is zero credit. |
| `lowbit` binary arithmetic | [Fenwick 1994](https://doi.org/10.1002/spe.4380240306) | `V01` cannot claim the least-bit update geometry. |
| Aliquot iteration | [Chum et al. 2021](https://arxiv.org/abs/2110.14136) | `D09` is owner-heavy even before the fixed-gcd restriction. |
| Finite-field factorization | [Brent--Zimmermann 2007](https://arxiv.org/abs/0710.4410) | Polynomial gcd/factor algorithms themselves are zero credit. |

An external novelty decision would still require specialist databases and
citation chasing from tent-map arithmetic, divisor-map iteration, unitary and
bi-unitary divisor literature, and arithmetic-function dynamics.

## 7. Firewall against the earlier portfolio

| Earlier occupied mechanism | Affected replacements | Decision |
|---|---|---|
| Arithmetic-function/Pratt relation maps in the early arithmetic lane and the recent totient-complement scout | `D05`--`D08` | Killed.  New sums and differences do not create a new carrier mechanism. |
| Aliquot and generic iteration of number-theoretic functions | `D09`, `D10` | Killed by owner or collapse. |
| Valuation digit erasure and local Newton/Hensel defect squaring | `D11`--`D14`, `V01`--`V06` | The overlapping descent/defect content is subtracted; none survives. |
| Polynomial derivative/Euclidean and translation-gcd lanes | `F01`--`F04` | All four killed; no derivative-gcd result is promoted. |
| Arithmetic \(Z\)-games, ordinary power maps, finite linear maps, and group actions | reduction of `D01` | The \(Z\)-operation, absolute exponent difference, and multiplication by 2 on \(\mathbb Z/(2e)\) are explicitly zero credit.  The survivor is only the fixed-complement functional graph and its complete arithmetic theorem package. |
| Closure, pruning, bounded-rank functors, standard categorical identities | all candidates | None was admitted as a survivor; `F03` is killed precisely as an identity. |

`D01` is also separated from the squarefree totient-complement system in a
literal way: if \(n\) is squarefree, then \(\gcd(d,n/d)=1\) for every divisor
and `D01` is the constant map \(d\mapsto n\).  Its nontrivial dynamics begins
only with repeated prime exponents and contains no Pratt-edge interaction.

## 8. Gate recommendation

Advance only `D01` to an independent proof-and-specialist-collision gate, with
the following non-negotiable conditions:

1. prove all four boxed theorem blocks for arbitrary \(n\), including edge
   cases \(n=1\), even exponents, and zero target exponents;
2. lead related work with the two direct \(Z\)-game owners and keep the
   \(Z\)-operation, tent/doubling quotient, CRT product, and Möbius inversion
   in an explicit zero-credit paragraph;
3. search the literal map and the equivalent form
   \(n/\gcd(d,n/d)^2\) in specialist number-theory databases and through
   unitary/bi-unitary divisor references; and
4. kill the candidate immediately if a direct owner contains the arbitrary-
   \(n\) all-iterate/fixed/fibre package, or if specialist review judges the
   arithmetic wrapper itself to have no independent value.

All other handles remain permanent kills for this sequence.  They should not
be recycled by changing a sign, an exponent, a prime, or a finite parameter
box.
