# Hostile replacement gate: `A02`, `D01`, and `CPG`

**Status:** independent owner/value review; **HOLD EXTERNAL**.  The labels in
this report are audit handles, not manuscript assignments.  Review snapshot:
**2026-08-31 UTC**.

## Outcome first

| candidate | verdict | decisive fact |
|---|---|---|
| `A02` | **PASS, CONDITIONAL** | It is the only candidate here whose coordinates remain genuinely coupled across distinct primes.  Its literal arithmetic reduction, recurrent census, and every-target fibre law survive the historical firewall, but the source-phase decoder and the advertised DAG-height entry bound still need a complete written induction. |
| `D01` | **KILL -- EXACT INTERNAL DUPLICATE** | It is word-for-word the complementary-divisor tent map already proved and killed in `proof_spikes/X01_DIVISOR_TENT_REPORT.md`, itself a resurrection of the older balanced-divisor tent candidate.  The old killed dossier proves a strictly stronger package, including pointwise periods and every iterated fibre. |
| `CPG` | **KILL -- EXACT CONJUGATE OF AN OCCUPIED SYSTEM** | Divisor complementation conjugates it exactly to the existing annihilator--power ideal map.  Its resonance, parity clock, depth CDF, recurrent product, and cycle census are therefore translations of the occupied clipped-reflection theorem.  Its target-fibre formula is a one-line inversion and does not clear the value floor. |

**Portfolio decision:** keep at most one divisor-lattice slot, and let that
slot be `A02` only after the proof repairs below.  If `A02` fails those repairs,
leave the slot empty.  Do **not** resurrect `D01` or `CPG` as fallbacks.

This is an internal value decision, not a novelty or priority claim.  A bounded
search non-hit never certifies absence of an owner.

## 1. Audit and source boundary

The audit read the three scouts, all three relevant verifiers, the completed
annihilator--power manuscript/control, the archived divisor-tent proof dossier,
and the historical collision files.  It searched the literal maps and the
equivalent scalar maps

```text
d -> lcm(d,n/d)/gcd(d,n/d),
d -> n/gcd(n,d^k),
a -> |2a-e|,
a -> max(e-ka,0),
```

as well as `Z(d,n/d)`, complementary-divisor iteration, tent/doubling
quotients, annihilator powers, and gcd/lcm divisor dynamics.  Exact-string and
structural searches were repeated against current 2025--2026 records.  No
primary source located in this bounded pass states either fixed-complement
self-map with the proposed complete atlas.  That non-hit has no positive
weight because both replacement candidates fail harder internal gates.

The primary controls used for subtraction are:

- Cobeli--Zaharescu define the arithmetic operation whose prime exponents are
  absolute differences in [*A game with divisors and absolute differences of
  exponents*](https://arxiv.org/abs/1411.1334), DOI
  [10.1080/10236198.2014.940337](https://doi.org/10.1080/10236198.2014.940337).
- Cobeli--Prunescu--Zaharescu explicitly define
  `Z(a,b)=ab/gcd(a,b)^2` and iterate it as an arithmetic growth rule in
  [*A growth model based on the arithmetic Z-game*](https://arxiv.org/abs/1511.04315),
  DOI [10.1016/j.chaos.2016.05.016](https://doi.org/10.1016/j.chaos.2016.05.016).
- Scheicher--Sirvent--Surer treat tent-map dynamics and periodicity transfer in
  [*Dynamical properties of the tent map*](https://doi.org/10.1112/jlms/jdv071).
  Qureshi--Reis give structural functional graphs for power maps on finite
  groups, including the abelian case, in
  [*On the functional graph of the power map over finite groups*](https://doi.org/10.1016/j.disc.2023.113393).
- Dacic's primary paper
  [*Properties of monotone mappings in partially ordered sets*](https://eudml.org/doc/257609)
  is background for antitone maps; generic order reversal and fixed/two-cycle
  reasoning receive no credit.
- For `A02`, Ford--Konyagin--Luca own prime chains and Pratt height
  ([author preprint](https://arxiv.org/abs/0904.0473)); Veliz-Cuba et al. own
  the AND-NOT/wiring-diagram framework
  ([author preprint](https://arxiv.org/abs/1211.5633)); and Chen--Gao--Basar
  give broad periodic-orbit reduction for conjunctive Boolean networks
  ([author preprint](https://arxiv.org/abs/1708.01975)).

The two arithmetic Z-game papers directly own the atomic rule and exponent
absolute difference.  Their searched text did not expose the fixed pair
`(d,n/d)` as this self-map.  Likewise, the bounded CPG search found no literal
external iteration owner.  Neither observation can overcome exact internal
duplication or conjugacy.

## 2. Mechanical replay and proof sufficiency

All supplied exact programs replayed successfully.

| control | replay result |
|---|---:|
| full algebraic scout containing `A02` | `531,206` assertions; `A02` itself has 224 states and 1,132 checks |
| replacement algebraic scout containing `D01` | `1,539,136` assertions; focused `D01` audit has 635 states |
| archived complementary-divisor tent pilot | `348,392` assertions |
| `CPG` verifier | 1,600 boxes, 215,855 states, `3,111,459` assertions |
| occupied annihilator--power verifier | `212,843` assertions |
| independent literal `CPG`/annihilator conjugacy audit | 49,476 state-parameter checks for `2<=n<=1000`, `2<=k<=8` |

An additional independent falsification pass exhausted all **33,867** ordered
DAGs on at most six vertices.  For the `A02` Boolean rule it found no violation
of: period exactly two on recurrence, recurrent count `2^s`, or maximum tail at
most `h+1`.  This strengthens the computational evidence but is not a proof.

The distinction between formula correctness and proof sufficiency is decisive:

- The `D01` formulas are correct, and the older killed dossier already contains
  proofs stronger than the replacement scout.
- The `CPG` formulas are correct, and the completed annihilator--power proof
  translates through an exact conjugacy.
- For `A02`, the integer/support identity and target inclusion--exclusion
  derivation are proof-ready.  The current source-phase recurrence argument is
  a credible outline, but the phase decoder and the `h+1` entry induction are
  not yet written at theorem-proof granularity.  Thus its pass remains
  conditional rather than automatic.

## 3. `D01`: correct mathematics, fatal exact duplication

The replacement map is

\[
 \Delta_n(d)=
 \frac{\operatorname{lcm}(d,n/d)}{\gcd(d,n/d)}.
\]

This is exactly equation (1) of the already killed complementary-divisor tent
dossier, with only notation changed from `Phi_N` to `Delta_n`.  It is also the
balanced-divisor tent candidate already recorded in the earlier historical
ledger.  There is no carrier, update, or schedule distinction.

### 3.1 Formula audit

Write `n=product p_i^(e_i)` and `d=product p_i^(a_i)`.  Then

\[
 v_{p_i}(\Delta_n(d))=|2a_i-e_i|.
\]

With `j_i=e_i-a_i`, this is folding multiplication by two on
`Z/(2e_i)Z` by `j~-j`.  Consequently all of the replacement formulas follow:

- the displayed all-iterate formula;
- depth `max_i max(0,v_2(2e_i)-v_2(e_i-a_i))`;
- the recurrent count and every cumulative depth layer;
- the gcd formula for every iterate-fixed count and hence exact periods; and
- the parity-controlled one-step target fibre.

The formulas agree with both verifiers.  The stray comma in the replacement
scout's typeset exponent `p_i^{,e_i-...}` is a presentation typo only; the
executable and intended formula are correct.

The older killed dossier is strictly stronger.  It additionally gives the
least eventual period of every state from the odd part of its cyclic order and
an explicit fibre formula for **every iterate**, not merely one step.  Thus the
replacement scout supplies no theorem increment over the archive.

### 3.2 Exact zero-credit subtraction

The following receive zero contribution credit:

1. gcd/lcm valuation coordinates and `gcd*lcm=product`;
2. the arithmetic `Z`-rule and absolute difference of prime exponents;
3. tent-map or doubling-map dynamics;
4. folding a cyclic group by sign;
5. finite-abelian power-map functional graphs;
6. primewise Cartesian products;
7. congruence counting, Burnside, Mobius inversion, and zeta packaging;
8. every formula already present in the killed divisor-tent dossier; and
9. all finite enumeration.

After external subtraction, a narrow fixed-complement realization might have
remained.  After the exact internal subtraction, even that realization is not
new to this project.  There is no residual theorem contract to advance.

**Verdict: KILL / PERMANENT ARCHIVE.**  The correct verifier may remain as a
negative control, but `D01` must not occupy a reserve or fallback slot.

## 4. `CPG`: exact complement conjugacy to annihilator--power ideals

The proposed map is

\[
 T_{n,k}(d)=\frac{n}{\gcd(n,d^k)},\qquad k\ge2.
\]

Let `C(d)=n/d`.  Represent an ideal of `Z/nZ` by its unique divisor generator
`d|n`.  The occupied annihilator--power map has literal divisor form

\[
 A_{n,k}(d)=\gcd\!\left(n,(n/d)^k\right).
\]

Then, as literal integers,

\[
 \boxed{T_{n,k}=C\circ A_{n,k}\circ C}.
\]

Indeed,

\[
 C\bigl(A_{n,k}(C(d))\bigr)
 =\frac{n}{\gcd(n,d^k)}.
\]

This is topological conjugacy of the entire finite functional graph, not a
shared motif.

### 4.1 Scalar translation and formula audit

On a prime-power exponent chain `0<=a<=e`, annihilator--power uses

\[
 g(a)=\min(e,k(e-a)).
\]

With `c(a)=e-a`,

\[
 c\,g\,c(a)=e-\min(e,ka)=\max(e-ka,0),
\]

which is exactly the CPG scalar map.  The advertised CPG package translates
term by term:

- the endpoint two-cycle is unchanged;
- the annihilator--power fixed exponent `ke/(k+1)` becomes `e/(k+1)`;
- its signed deviation becomes the negative of CPG's deviation, exchanging
  the two parity branches of the same depth clock;
- the cumulative depth formula is the same CDF after reflection;
- product recurrent/fixed/two-cycle counts are identical; and
- product depth is the same coordinate maximum.

The CPG verifier correctly checks these translations.  The completed occupied
proof already establishes the nontrivial temporal claims.  The only displayed
item not foregrounded in that earlier theorem contract is the one-step fibre

```text
b=0: e-ceil(e/k)+1;
b>0: one preimage iff k divides e-b;
otherwise: zero.
```

This is immediate from solving `max(e-ka,0)=b`; it is not enough to reopen an
exact conjugate of an occupied system.

### 4.2 Exact zero-credit subtraction

Zero credit includes:

1. divisor/ideal identification in `Z/nZ`;
2. annihilator and ideal-power valuation formulas;
3. divisor complementation and conjugacy by an involution;
4. antitone-chain fixed/two-cycle background;
5. the clipped affine deviation law and both parity threshold branches;
6. all depth CDF, CRT product, cycle, and zeta outputs already proved for the
   annihilator--power system;
7. the elementary one-step inverse equation; and
8. finite verification.

After this exact subtraction, the residual theorem value is empty.

**Verdict: KILL / EXACT CONJUGATE.**  Preserve the identity
`T=C A C` in the permanent kill ledger so the same system cannot return under
the phrase “complementary power--GCD.”

## 5. `A02`: sole conditional survivor

For squarefree `n=product_(p in P) p`, write a divisor as a support
`S subseteq P`.  The literal map

\[
 F_n(d)=\gcd(n,(n/d)\varphi(d))
\]

has support rule

\[
 F(S)=(P\setminus S)\cup N(S),
 \qquad N(S)=\{p:\exists q\in S,\ p\mid q-1\}.
\]

Unlike `D01` and `CPG`, this update is not a Cartesian product of independent
prime-power chains.  The edge relation `q->p` couples different primes and is
acyclic because `p|q-1` implies `p<q`.

### 5.1 What is already sufficient

The following parts are algebraically and combinatorially sound:

1. Euler's squarefree product formula proves the literal support identity
   state by state.
2. Target zeros force a source-state one-set and its parent set to zero; ordinary
   inclusion--exclusion over the remaining bad target-one events gives the
   stated every-target fibre formula, including targets outside the image.
3. The supplied verifier compares literal integer arithmetic with the Boolean
   rule and checks every target in all three boxes.
4. Independent ordered-DAG exhaustion supports the claimed recurrent census
   and entry bound far beyond the three arithmetic examples.

### 5.2 Mandatory proof repairs

Before the conditional pass becomes a frozen theorem contract, the write-up
must provide:

1. an explicit topological phase decoder showing that each choice of phases on
   the `s` source vertices extends uniquely to one recurrent state;
2. a proof that the resulting recurrent states all have exact period two and
   that there are no fixed states;
3. a level-by-level induction proving entry by time at most `h+1`, with the
   indexing convention for path length fixed and the one-vertex/disconnected
   cases included;
4. a complete proof of the every-target inclusion--exclusion formula, explicitly
   deleting every summand in which forced-one and forced-zero sets intersect;
5. a statement that `h+1` is only a bound unless sharpness and extremizers are
   separately proved; and
6. an explicit integer-to-support conjugacy theorem so that the arithmetic map,
   rather than a detached Boolean network, is the object of the result.

Failure of items 1--4 demotes the candidate below the value floor.  More
enumeration cannot substitute for them.

### 5.3 Exact zero-credit subtraction and residual

Zero credit includes Euler's totient identity, squarefree support coordinates,
prime chains, Pratt trees and height, generic AND-NOT/conjunctive-network
language, feed-forward topological induction as a method, ordinary
inclusion--exclusion, and generic finite-map cycle/zeta conversion.

The residual is the conjunction tied to one literal arithmetic map:

- the source-phase recurrent decoder and exact `2^s` census;
- the all-prime-set entry bound; and
- the every-target arithmetic fibre formula.

This is a focused, low-ceiling result, but it is structurally different from a
coordinatewise exponent product and remains the only candidate in this trio
with nonempty owner-subtracted value.

**Verdict: PASS, CONDITIONAL / SOLE ACTIVE DIVISOR SLOT.**

## 6. Historical firewall

| occupied mechanism | `A02` | `D01` | `CPG` |
|---|---|---|---|
| P97 sumset squaring | No map or proof transfer; only generic nonlinear finite dynamics. | Doubling/power language is adjacent, but the exact old divisor-tent duplicate already kills it. | No literal collision; irrelevant to the decisive conjugacy. |
| P100 valuation digit erasure | Squarefree cross-prime Boolean coupling, not a digit eroder. | Valuation coordinates are adjacent and receive no credit. | Valuation clocks are adjacent, but the stronger collision is exact P107 conjugacy. |
| P107 annihilator--power ideals | Different: cross-prime Pratt coupling versus primewise clipped reflection. | Adjacent coordinate-product arithmetic only. | **Exact conjugate by `d->n/d`; fatal.** |
| P124 cross-colon monomial ideals | Both reduce partly to coupled Boolean propagation, so generic OR/AND path machinery is zero credit; carriers, literal operators, upper-set geometry, and target formulas differ. | No literal overlap; both generic transfer and product bookkeeping are zero credit. | Same broad ideal-operator narrative, but exact P107 conjugacy is already decisive. |
| P128 translation--GCD polynomials | Different carrier and update; no meet-fold or irreducible-orbit exponent-minimum transfer. | Generic exponent minima/maxima and product fibres are zero credit; no rescue. | No literal overlap; the existing arithmetic ideal conjugacy is decisive. |
| archived divisor-tent candidate | No collision. | **Exact same literal map and a strictly weaker theorem package; fatal.** | No literal collision. |

The two kill decisions do not depend on arguing that every coordinatewise
divisor map is forbidden.  Each has its own exact fatal identity.  Conversely,
`A02` is not saved merely by being different: it survives only if its coupled
arithmetic theorem contract is fully proved.

## 7. Ranked portfolio recommendation

1. **`A02` -- conditional active choice.**  Freeze only after the phase-decoder,
   recurrence, entry-bound, and target-fibre proofs are complete.  Its value is
   the coupled arithmetic package, not Pratt or Boolean-network machinery.
2. **`D01` -- killed archive, not a reserve.**  Mathematically richer than CPG,
   but exactly identical to an older killed system whose dossier is stronger.
3. **`CPG` -- killed archive, not a reserve.**  Exact conjugacy to an occupied
   system leaves only an elementary target-fibre inversion.

Final selector rule: one divisor-lattice slot at most, occupied by `A02` only
after proof completion.  If a stronger non-divisor candidate exists, it should
still outrank this low-ceiling conditional pass.  If `A02` fails, select a new
system rather than carrying either cosmetic exponent-map replacement.
