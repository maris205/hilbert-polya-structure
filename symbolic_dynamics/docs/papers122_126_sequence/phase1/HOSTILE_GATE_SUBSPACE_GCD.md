# Independent hostile gate: C3 nilpotent subspace--Fibonacci and A01 proper-residue gcd descent

**Review posture:** independent, fail-closed correctness/owner/value gate.  I
did not write either proof dossier.  A finite verifier pass is treated only as
falsification evidence; it cannot repair owner subtraction or a thin residual.

**Files read:** both proof dossiers, both verifier sources and canonical
outputs, the relevant P1--P121 manuscripts/support files (especially P108 and
P109), and the current stage/scouting records.  External searches were run on
30 August 2026 with literal, algebraically translated, and owner-neighborhood
formulations.  Search misses below are bounded non-hits, never novelty
certificates.

**External status:** `HOLD_EXTERNAL` for both candidates.

## Executive gate

| candidate | formula audit | direct/structural owner subtraction | P1--P121 collision | paper-scale residual | decision |
|---|---|---|---|---|---|
| **C3**, `T(U,W)=(W,U+NW)` on `L(V)^2` | all five corrected claims survive; the `d=1` exception is necessary | fixed points are the classical invariant-subspace chain of a cyclic nilpotent; recurrent pairs are exactly subrepresentations of a nilpotent two-cycle quiver; the iterate is a generic idempotent-semiring truncation | **severe double squeeze:** P108 already owns the finite second-order Fibonacci-map silhouette and P109 already owns the regular-nilpotent subspace-lattice temporal silhouette | one short identity gives the iterate, period ceiling, and depth bound; no recurrent census, depth layers, fibres, or second theorem engine | **KILL / RESERVE AS A LEMMA** |
| **A01**, repeatedly replace `m` by `gcd(m,A)` for uniform `1<=A<m` | kernel, history law, support, prime-power product, endpoints, and limit law survive | Alexeev et al. (2026) own the downward-divisibility Markov-chain framework; Minami owns the one-step gcd law, of which this kernel is a conditioning; the prime-power product is a normalized/scaled q-Stirling rising factorial | no literal internal map collision; P21/P107/P99 are adjacent arithmetic silhouettes only | the prime-power identification is real but is currently the only nonmechanical residual; the general path sum is generic | **REWRITE; NO PAPER FREEZE** |

The decisions separate correctness from value.  C3 is not killed because its
displayed theorem is false; it is killed because the correct theorem is almost
entirely a recombination of already occupied mechanisms.  A01 is not GO
because, after compulsory 2026/Minami/q-Stirling subtraction, it has only one
clearly substantive family theorem.

## Fresh mechanical record

I reran both standard-library programs from the workspace root and compared
fresh stdout byte-for-byte with the stored canonical output.

```text
$ python3 docs/papers122_126_sequence/proof_spikes/verify_alg_subspace_fibonacci.py
ALG_SUBSPACE_FIBONACCI VERIFIER: PASS
assertions=3188520
exhaustive_lanes=12 witness_lanes=48
fresh-vs-canonical cmp: PASS

$ PYTHONDONTWRITEBYTECODE=1 python3 \
    docs/papers122_126_sequence/proof_spikes/verify_stoch_gcd_descent.py
proper-residue gcd descent proof verifier: PASS
exact assertions: 5,637
fresh-vs-canonical cmp: PASS
```

These totals are accurately reported by the dossiers.  The C3 exhaustive
lanes are over prime fields only; its proof, not its computation, supplies the
extension-field quantifier.  The A01 arithmetic is exact `Fraction` arithmetic
with no sampling.

## 1. C3: nilpotent subspace--Fibonacci

### 1.1 Literal normalization

To avoid the dossier's collision between the ambient vector space `V` and
the second state coordinate also called `V`, write the ambient space as
`E`, the state as `(U,W)`, and

```text
T(U,W) = (W, U + N W),
X_0=U, X_1=W, X_{t+2}=X_t+N X_{t+1}.
```

Here `+` is subspace join.  This renaming is not cosmetic in a manuscript:
phrases such as “on `L(V)^2`, define `T(U,V)`” use the same symbol for two
different quantified objects.

### 1.2 Formula-by-formula audit

#### C3.1 Closed terms: PASS

For `r>=1`,

```text
X_(2r)   = sum_(j=0)^(r-1) N^(2j) U
           + sum_(j=0)^(r-1) N^(2j+1) W,

X_(2r+1) = sum_(j=0)^(r-1) N^(2j+1) U
           + sum_(j=0)^r N^(2j) W.
```

The simultaneous induction is correct.  The apparent Fibonacci
multiplicities collapse because subspace join is idempotent.  In particular,
the actual coefficient support is only the parity support of ordinary
Fibonacci walks; no numerical Fibonacci coefficient remains.

#### C3.2 Two-step increment and period ceiling: PASS

Both parities give the single identity

```text
X_(t+2) = X_t + N^t U + N^(t+1) W.                 (C3.1)
```

Hence `N^d=0` gives `X_(t+2)=X_t` for `t>=d`, and applying this at `t` and
`t+1` proves `T^(t+2)=T^t`.  Every orbit is recurrent by time `d` and every
cycle has length one or two.  No hidden invertibility assumption is used.

There is an even simpler structural view that the dossier should not hide:
`T^2` is coordinatewise inflationary.  Thus the even-time orbit is a finite
closure iteration, and (C3.1) merely says that nilpotence truncates the
alternating-path closure after length `d`.  This makes the theorem reliable,
but also makes its mechanism very mature and mechanically reducible.

#### C3.3 Recurrent criterion: PASS

Directly,

```text
T^2(U,W) = (U+NW, W+NU+N^2W).
```

Equality with `(U,W)` is equivalent to

```text
N U <= W  and  N W <= U.                           (C3.2)
```

The reverse implication uses `N^2W<=NU<=W`.  Since the universal period
ceiling is two, recurrence is equivalent to being fixed by `T^2`.  The
dossier's argument transporting `T^2`-fixedness backward around a finite
cycle is valid.

#### C3.4 Fixed points and count: PASS / DIRECTLY OWNED

A fixed state must be `(Y,Y)` with `NY<=Y`.  A regular nilpotent is the
cyclic `F_q[z]`-module `F_q[z]/(z^d)`, whose submodules are the ideals
`(z^j)`.  Thus there are exactly `d+1` fixed points.  This count is correct
for every prime power, including `d=1`.

It is not residual contribution mass.  Invariant-subspace lattices of linear
transformations are classical; Brickman--Fillmore is the direct foundational
owner, and Aggarwal--Ram explicitly restate that a cyclic nilpotent has one
invariant subspace in each dimension.  The count `d+1` must receive zero
credit.

#### C3.5 Sharp maximum depth: PASS WITH THE STATED EXCEPTION

For `d=1`, `N=0` and `T(U,W)=(W,U)`, so every state is already recurrent and
the maximum depth is `0`, not `1`.  The dossier correctly repairs this.

For `d>=2`, the witness `(span(e_0),0)` has at time `t<d` alternating parity
spans.  In both parity cases `e_t` lies in `N X_(t+1)` but not in `X_t`, so
(C3.2) fails until time `d`.  The upper bound from (C3.1) is therefore sharp:

```text
D_1=0,   D_d=d for d>=2.
```

This proof is field-uniform and does not extrapolate from enumeration.

### 1.3 What the C3 verifier does and does not establish

The fresh run is useful and reproducible, but one advertised independence
point is overstated.  In the program, `is_recurrent(state)` is *defined* by
(C3.2); the subsequent comparison with `recurrence_conditions` is therefore
tautological.  The program does independently check equivalence with literal
`T^2(state)==state`, and the closed-term checks support the period ceiling,
but it never discovers literal cycles and then compares their vertices with
(C3.2).

If the dossier is archived for reuse, its control should compute the eventual
cycle of each pair independently, then compare period, entry time, and the
criterion.  The current pass supports the formulas; it does not turn the
recurrent characterization into an independently encoded check.

The more important absence is mathematical, not computational.  The report
does **not** give:

- a formula for the number of recurrent pairs (the canonical output merely
  prints small values);
- fixed-versus-genuine-two-cycle counts;
- an exact depth-layer census;
- one-step or iterated fibres; or
- any asymptotic/enumerative theorem independent of (C3.1).

Those omissions leave almost the entire package downstream of one identity.

### 1.4 External owner subtraction

#### Fixed and invariant subspaces

- Brickman and Fillmore, *The invariant subspace lattice of a linear
  transformation*, Canadian Journal of Mathematics 19 (1967), 810--822,
  [DOI 10.4153/CJM-1967-075-4](https://doi.org/10.4153/CJM-1967-075-4), own
  the classical invariant-lattice setting.
- Aggarwal and Ram, *Splitting Subspaces of Linear Operators over Finite
  Fields*, [arXiv:2012.08411](https://arxiv.org/abs/2012.08411), published as
  [Finite Fields and Their Applications 76 (2021), 101982](https://doi.org/10.1016/j.ffa.2021.101982),
  explicitly use the cyclic-nilpotent invariant chain.  Splitting/Krylov
  counts are not C3's map, but the `d+1` fixed count is owned background.

#### Recurrent locus as a cyclic-quiver subrepresentation locus

Condition (C3.2) is exactly the definition of a subrepresentation of the
two-vertex equioriented cycle representation

```text
E --N--> E --N--> E.
```

Thus the recurrent pairs, stratified by `(dim U,dim W)`, are cyclic-quiver
Grassmannians.  Quiver Grassmannians and nilpotent cyclic representations are
an active, already named theory; see, for example:

- Feigin et al., *Generalized juggling patterns, quiver Grassmannians and
  affine flag varieties*,
  [Mathematische Zeitschrift (2025), DOI 10.1007/s00209-024-03614-5](https://doi.org/10.1007/s00209-024-03614-5),
  Definition 2.1 and its cyclic-quiver specialization; and
- Lowiel, *Quiver Grassmannians associated to nilpotent cyclic
  representations defined by single matrix*,
  [arXiv:2406.03970](https://arxiv.org/abs/2406.03970).

These papers do not state the literal temporal map `T`, so this is a closest
structural owner, not a claimed exact temporal owner.  It nevertheless means
that merely identifying or eventually counting (C3.2) cannot be marketed as
a new class of recurrent subspace pairs without a quiver-level subtraction.

#### Idempotent linear recurrence

The closed form is ordinary companion-matrix/linear-recurrence algebra in an
additively idempotent setting.  Generic idempotent semiring linearization and
matrix iteration are established machinery; see Gunawardena's
[*An Introduction to Idempotency*](https://www.cambridge.org/core/books/idempotency/an-introduction-to-idempotency/9F6B9CCD54C8D7461C5DACAEFDBE82D1).
No direct source was located for the exact pair map after searches for
“subspace Fibonacci,” `X_(t+2)=X_t+N X_(t+1)`, nilpotent join recurrences,
and cyclic-quiver temporal variants through 2026.  This is only
`BOUNDED_NO_EXACT_MAP_HIT`.

### 1.5 The P108/P109 double squeeze

This is the decisive internal gate.

| C3 feature | P108 already occupies | P109 already occupies | residual after subtraction |
|---|---|---|---|
| finite second-order map `(x,y)->(y,x+y-like)` | exact capped Fibonacci iterates, recurrence, depth clock, sharp witness, fibres | -- | C3 changes scalar cap to subspace join, whose idempotence actually collapses the Fibonacci coefficients to parity |
| nilpotent operator on the full finite subspace lattice | -- | exact `U->NU`, all iterated pointed fibres, joint rank transitions, indegrees, exact depth layers, sharp depth, zeta, rigidity | C3 uses two copies of the same lattice but gives fewer enumerative outputs |
| regular Jordan chain and depth `d` | P108 has an exact uniform sharp family in its own cap parameter | P109 already has the regular-nilpotent kernel flag and sharp depth `d` | no independent clock mechanism remains |
| fixed/recurrent structure | P108 supplies complete recurrence for its map | P109 supplies full nilpotent functional graph and classical invariant-subspace background | C3 fixed points are owned; recurrent pairs are quiver subrepresentations but are not counted |

P108 is not literally the same map, and P109 is not a second-order recurrence.
That literal distinction is insufficient.  C3's advertised value is precisely
the conjunction of the two already frozen silhouettes, while its theorem
surface is strictly thinner than their union.  A new paper would read as an
internal recombination rather than a new lane.

### 1.6 C3 verdict, claim ceiling, and required action

**Decision: `KILL / RESERVE AS A CORRECT LEMMA`.**  Do not assign a paper
number from the current dossier.

Permitted archival ceiling:

> For a nilpotent endomorphism `N`, the join-linear second-order recurrence
> has the displayed parity-support normal form, reaches period at most two by
> the nilpotency index, and has recurrent locus `NU<=W, NW<=U`; for a regular
> nilpotent the maximum depth is `d` for `d>=2`, with `d=1` exceptional.

The following receive zero contribution credit: generic Fibonacci companion
recurrences, idempotent-semiring matrix iteration, nilpotence truncation,
cyclic-nilpotent invariant subspaces and their count, cyclic-quiver
subrepresentation language, finite-map period/zeta bookkeeping, and brute
force enumeration.

If C3 is ever reconsidered, all of the following are required:

1. obtain a genuine recurrent/depth/fibre enumeration not mechanically
   implied by (C3.1), preferably a closed `q,d` formula;
2. formulate and subtract the two-cycle quiver Grassmannian/Hall-polynomial
   owner neighborhood explicitly;
3. explain, theorem by theorem, why the result is not a P108-plus-P109
   recombination;
4. add a second proof engine (for example, a quiver-module/Hall route) that
   yields an enumerative theorem, not merely another proof of (C3.1); and
5. replace the verifier's criterion-defined recurrence test by literal cycle
   discovery, and add at least one extension-field lane if extension-field
   computation is advertised.

Without all five, the correct disposition is archive, not rewrite-to-paper.

## 2. A01: proper-residue gcd descent

### 2.1 Terminology and boundary normalization

At state `m>1`, sample uniformly from the **nonzero residue
representatives** `1,...,m-1` and move to `gcd(m,A)`; state `1` is absorbing.
The phrase “proper residue” is not standard enough to carry the definition by
itself and is a poor owner-search key.  Any manuscript must display
`1<=A<m` in the abstract/introduction and search under “nonzero residue,”
“conditioned random gcd,” “random divisor chain,” and “cyclic-group element
order” formulations as well.

The boundary conventions are correct:

```text
T_1=0, G_1(z)=1;
T_p=1, G_p(z)=z for prime p;
empty products at k=1 equal 1.
```

### 2.2 Formula-by-formula audit

#### A01.1 One-step kernel: PASS / ZERO CREDIT

For a proper divisor `d|n`, writing `a=db` gives

```text
# {1<=a<n : gcd(n,a)=d} = phi(n/d),
P(n,d)=phi(n/d)/(n-1).
```

The fibres partition `1,...,n-1`, so
`sum_(d|n,d<n) phi(n/d)=n-1`.  Every transition strictly lowers the integer,
and absorption is certain.  This is correct.

It is also exactly the `r=1` Minami gcd distribution conditioned not to draw
the representative `n`: under uniform `K in {1,...,n}`, `gcd(n,K)=n` occurs
only for `K=n`; conditioning it away yields A01's kernel.  The one-step
totient law therefore receives zero novelty credit, not merely “nearby”
credit.

#### A01.2 History law and divisor PGF: PASS / GENERIC

Multiplying edge probabilities along a strict divisor history and summing
over histories gives the stated distribution.  Conditioning on the first
step gives

```text
G_n(z) = z/(n-1) * sum_(d|n,d<n) phi(n/d) G_d(z).
```

The literal residue-history fibre is the product of the corresponding
totients.  All formulas are correct.  Once the transition kernel is known,
however, these are the standard path formula and first-step recursion for an
absorbing DAG Markov chain.  They are proof infrastructure, not a second
headline theorem.

#### A01.3 Support and endpoint coefficients: PASS

Every step reduces `Omega` by at least one, so the degree is at most
`Omega(n)`.  For every `1<=t<=Omega(n)`, jump first to a divisor with
`Omega=t-1` and then remove one prime at a time; every edge has positive
probability.  Thus the support is exactly `1,...,Omega(n)`.

The first coefficient `phi(n)/(n-1)` and the maximal-history sum over distinct
orders of the prime multiset are correct.  The maximal-history recurrence

```text
[z^r]G_n = 1/(n-1) * sum_(p|n) (p-1)[z^(r-1)]G_(n/p)
```

correctly sums over distinct prime divisors, not prime occurrences.

#### A01.4 Prime-power product: PASS

For `F_k=G_(p^k)`, subtracting `p` times the `k-1` divisor recurrence from
the `k` recurrence cancels all old terms and gives

```text
(p^k-1)F_k = [p(p^(k-1)-1)+(p-1)z]F_(k-1).
```

Consequently, with `c_(p,j)=p(p^j-1)/(p-1)`, the dossier's formula

```text
G_(p^k)(z)=z product_(j=1)^(k-1) (z+c_(p,j))/(1+c_(p,j))
```

is correct, as is

```text
T_(p^k) =_d 1 + sum_(j=1)^(k-1) Bernoulli((p-1)/(p^(j+1)-1)).
```

#### A01.5 Moments, endpoint atoms, and fixed-p asymptotic: PASS

The mean and variance are the sums of Bernoulli means and variances.  The
shortest atom telescopes to

```text
P(T_(p^k)=1)=p^(k-1)(p-1)/(p^k-1),
```

and its exact error from `(p-1)/p` is correct.  The longest atom is

```text
P(T_(p^k)=k)=product_(r=2)^k (p-1)/(p^r-1),
```

with the displayed fixed-`p`, `k->infinity` asymptotic and convergent constant
`C_p`.  One wording needs repair: the dossier's opening says “sharp
asymptotic of the maximum duration.”  The maximum duration itself is exactly
`k`; what has an asymptotic is the **probability mass at that maximum**.

#### A01.6 Infinite-exponent limit and tails: PASS

The bound

```text
q_(p,j)=(p-1)/(p^(j+1)-1) < p^(-j)
```

makes the infinite Bernoulli sum almost surely finite.  The common product
space gives almost-sure and distributional convergence.  The total-variation
and mean truncation bounds follow from the tail coupling, and the factorial-
moment bound gives

```text
P(T_(p,infinity)>=r+1) < 1/(r!(p-1)^r).
```

The proof handles `p=2` and `r=1`; no missing exceptional case was found.

### 2.3 A01 owner subtraction

#### Direct 2026 framework owner

Alexeev, Barreto, Li, Lichtman, Price, Shah, Tang, and Tao,
[*Primitive sets and von Mangoldt chains: Erdős Problem #1196 and beyond*](https://arxiv.org/abs/2605.00301)
(arXiv:2605.00301, submitted 1 May 2026), Definition 2.1, define downward
Markov chains on the divisibility poset with absorbing states.  Examples
2.2--2.4 give random-prime, Mertens, and von Mangoldt downward chains.  The
paper also uses path/hitting probabilities in the same divisibility-chain
framework.

It does **not** state A01's totient kernel, its absorption-time PGF, or the
prime-power product; searches within the primary text found no `totient`,
`absorption time`, or generating-function version of this process.  It is
therefore a direct **framework owner**, not an exact-kernel owner.

Mandatory zero-credit subtraction:

- the idea and terminology of a downward divisibility Markov chain;
- strict divisor histories and the absorbing state `1`;
- a generic first-step recursion, path multiplication, and flow language;
- `Omega` as the natural divisibility-poset level; and
- claims that merely insert a new kernel into Definition 2.1.

Any manuscript that presents the chain framework itself as new would collide
directly with a paper posted four months earlier.

#### Direct one-step gcd owner

Minami, *On the random variable
`{1,...,n}^r -> gcd(n,k_1...k_r)`*, Journal of Number Theory 133 (2013),
2635--2647,
[DOI 10.1016/j.jnt.2013.01.012](https://doi.org/10.1016/j.jnt.2013.01.012)
([publisher page](https://www.sciencedirect.com/science/article/pii/S0022314X13000620)),
studies the fixed-modulus random gcd distribution, its moments, and
convolutions.  At `r=1`, conditioning away its unique self-value `K=n`
produces A01's one-step law exactly.

Thus totient fibres, the one-step distribution, fixed-modulus gcd moments,
and convolution language all receive zero credit.  The genuine distinction
is temporal resampling at the new modulus and the resulting absorption time.

#### q-Stirling owner/mechanism hidden in the product

Put `[j]_p=(p^j-1)/(p-1)`.  Then

```text
c_(p,j)=p[j]_p,       1+c_(p,j)=[j+1]_p,

G_(p^k)(z)
 = z product_(j=1)^(k-1) (z+p[j]_p)/[j+1]_p
 = z p^(k-1)/product_(j=1)^(k-1)[j+1]_p
     * product_(j=1)^(k-1)(z/p+[j]_p).              (A01.1)
```

The last product is a scaled q-rising factorial, so its coefficients are a
normalization of classical q-Stirling numbers of the first kind.  Carlitz's
q-Stirling generating polynomials are established background; a modern
primary treatment is Cai and Readdy, *q-Stirling numbers: A new view*,
[Advances in Applied Mathematics 86 (2017), 50--80, DOI
10.1016/j.aam.2016.11.007](https://doi.org/10.1016/j.aam.2016.11.007).

This does not own the identification of A01's absorption time with (A01.1),
which is the best remaining theorem.  It does own the polynomial family and
linear-factor technology.  After the factorization, real negative zeros,
Poisson-binomial representation, coefficient log-concavity, and generic
Bernoulli moment/convergence arguments cannot be counted as separate novel
engines.

#### Bounded exact-process search

Queries covered “iterated random gcd,” “conditioned/nonzero random residue
gcd,” `phi(n/d)/(n-1)` transition probabilities, random cyclic-group element
orders, divisor-chain absorption PGFs, prime-power exponent descent, and the
explicit Bernoulli parameters through 2026.  No primary source was found that
states this literal adaptive process or its prime-power law.  The result is
`BOUNDED_NO_EXACT_PROCESS_HIT`, not a priority conclusion.

### 2.4 P1--P121 collision audit

No literal map, conjugacy, or identical theorem package was found among
P1--P121.

- **P21** uses a successor--divisor relation to build a countable symbolic
  shift and trace-class determinant.  It occupies divisor-chain language but
  not a finite absorbing arithmetic Markov chain.
- **P107** is the closest deterministic carrier: ideals of `Z/NZ`, CRT,
  prime-power valuations, and a literal gcd generator.  Its update is
  `I -> Ann(I)^r`, with clipped-reflection cycles and deterministic depths,
  not random resampling.  Static divisor/valuation decomposition and CRT
  receive zero internal credit.
- **P99** already uses prime-power valuation staircases for a deterministic
  sublattice shear.  It does not own A01's law, but “prime-power valuation
  simplification” alone cannot be the residual narrative.
- **P50/P59** use divisibility posets in symbolic/finite-ideal constructions,
  not this transition kernel.

The internal risk is therefore **adjacent silhouette**, not exact collision.
Unlike C3, A01 is not killed by P1--P121.

### 2.5 Paper-value audit

After strict subtraction, the current package has the following value:

1. the one-step kernel: correct, but Minami-conditioned and zero credit;
2. the general history/PGF recursion: exact, but generic downward-chain DAG
   machinery and zero/low credit;
3. support `1,...,Omega(n)` and endpoint histories: useful low-credit
   consequences;
4. the prime-power q-Stirling/Bernoulli product: the one genuine residual;
5. means, variance, endpoints, limit law, and tails: valid corollaries, mostly
   standard once item 4 is known.

This is a coherent short theorem note, but it does not yet clear this
project's paper-value gate.  All substantive statements are consequences of
one adjacent-recurrence subtraction on the one-dimensional prime-power
chain.  The dossier itself correctly identifies the missing increment: a
second non-prime-power infinite family or a genuinely general transform.

### 2.6 A01 verdict, allowed ceiling, and mandatory repairs

**Decision: `REWRITE / NO PAPER FREEZE`.**  This is not `KILL_FALSE`, and no
exact temporal owner was found.  It is also not `GO`: the 2026 owner and the
conditional-Minami/q-Stirling reductions must be made central, and another
paper-scale output is required.

Current allowed claim ceiling:

> Iterating the conditioned one-step gcd kernel produces a finite downward
> chain.  For prime-power starts, its absorption-time PGF is the normalized
> scaled q-Stirling rising factorial (A01.1), equivalently a specific
> Poisson-binomial law; the exact endpoint and fixed-prime limit formulas
> follow.

Not allowed from the current dossier:

- novelty or priority claims for downward divisibility chains;
- treating the totient kernel, divisor-DAG recursion, or one-step gcd law as
  residual;
- counting each Bernoulli corollary as an independent theorem engine;
- presenting (A01.1)'s q-Stirling polynomial as a newly created polynomial
  family;
- claiming a multiplicative factorization for general `n`; or
- public release before a specialist owner check.  External status remains
  `HOLD_EXTERNAL`.

Mandatory repairs before re-review:

1. **Owner-first rewrite.** Lead with Alexeev et al. 2026, state that A01 is a
   new kernel inside their Definition 2.1 framework, and assign the framework,
   path law, and `Omega` layers zero credit.
2. **Minami conditioning lemma.** State explicitly that the one-step kernel is
   the `r=1` Minami law conditioned on `K<n`; remove the present suggestion
   that Minami is merely adjacent.
3. **q-Stirling identification.** Add (A01.1), cite Carlitz/Cai--Readdy, and
   zero-credit the polynomial family and generic linear-factor consequences.
4. **Contribution compression.** Promote only the adaptive prime-power
   absorption identification; demote history sums, moments, endpoints, and
   tail inequalities to lemmas/corollaries.
5. **Value increment.** Prove one genuinely different infinite-family theorem
   beyond prime powers--for example an exact two-prime/squarefree transform,
   a nontrivial factor/interlacing criterion for a broad class of `n`, or an
   aggregate law not obtained by restating the divisor DP.  If this fails,
   downgrade to `KILL_VALUE / RESERVE AS A NOTE`.
6. **Wording/boundaries.** Replace the nonstandard bare term “proper
   residues” by the literal sample set, specify fixed `p` in the longest-atom
   asymptotic, and say “mass at the maximum duration,” not “asymptotic of the
   maximum duration.”
7. **Control scope.** Keep the exact 5,637-assertion verifier, but add a direct
   coefficient comparison with the normalized q-Stirling polynomial if that
   identity becomes the main theorem.

## 3. Replacement recommendation after the C3 kill

The already proved **odd-component complementation on labelled graphs** is a
materially stronger replacement candidate than C3, subject to its own hostile
owner gate.  Its dossier currently supplies:

- a literal graph self-map: synchronously complement each odd connected
  component;
- recurrence iff every nontrivial odd component is co-connected, with all
  periods at most two;
- a pointwise alternating component/co-component recursion for depth;
- the sharp global depth `floor((n-1)/2)` with an infinite witness family;
- exact all-depth labelled EGF recursions, plus fixed and recurrent census;
  and
- an exhaustive `n<=6` control reporting 67,758 assertions.

This clears the missing “all-depth recursion” and second-output gate that C3
does not.  However, the owner subtraction must be uncompromising:

- graph complementation and connected/co-connected decomposition: zero
  credit;
- cographs, cotrees, and canonical alternating component/co-component trees:
  **zero credit**, beginning with Corneil--Lerchs--Stewart Burlingham's
  complement-reducible graph theory;
- labelled `SET` assembly, connected-graph recurrence, EGF parity extraction,
  and zeta conversion: zero credit.

Only the parity-triggered component update, its exact temporal recursion,
sharp witness, and the resulting new all-depth census can remain.  The report
also contains a source-encoding defect where `\rm` appears as a carriage-return
character in two displayed EGF definitions; that must be repaired before any
reuse.  Subject to a direct-map/cograph owner search, this replacement is
`PROMOTE_TO_OWNER_GATE`, not yet a paper freeze.

## Final decision ledger

- **C3 nilpotent subspace--Fibonacci:** formulas correct; **`KILL / RESERVE AS
  A LEMMA`** because of direct classical/quiver subtraction and the P108/P109
  double internal squeeze.
- **A01 proper-residue gcd descent:** formulas correct; **`REWRITE / NO PAPER
  FREEZE`**.  Preserve only the adaptive prime-power q-Stirling identification
  as the current main residual, and require a distinct non-prime-power theorem
  before GO.
- **Replacement:** send odd-component complementation to hostile owner/value
  review, with all cograph/cotree machinery explicitly zero-credited.
- **External circulation:** `HOLD_EXTERNAL` throughout.

## 4. A01 re-entry audit after the all-integer zeta-mixture repair

**Re-entry date:** 30 August 2026.  
**New files audited:** the appended section “Post-gate value repair: an
all-integer zeta-mixture law” in `STOCH_GCD_DESCENT_REPORT.md`, together with
`verify_stoch_gcd_zeta_transform.py` and its canonical output.  
**Final A01 decision:** `KILL_DIRECT_2026_ZETA_PROCESS / RESERVE AS AN
OWNER-ADJACENT COROLLARY NOTE`.  
**External status:** `HOLD_EXTERNAL`.

The second output is mathematically correct.  It does **not** clear the owner
gate.  A relation missed in the first audit is decisive: the proper-residue
gcd chain is exactly the strict-change chain of the unit-spaced skeleton of
the zeta process explicitly constructed in Section 10.2 of Alexeev et al.
(2026).  The new independent-Bernoulli mixture is then the interval-change
count of that owned process.

### 4.1 Fresh control record

I reran both A01 programs and compared fresh stdout byte-for-byte with their
stored canonical outputs:

```text
$ PYTHONDONTWRITEBYTECODE=1 python3 \
    docs/papers122_126_sequence/proof_spikes/verify_stoch_gcd_descent.py
proper-residue gcd descent proof verifier: PASS
exact assertions: 5,637
fresh-vs-canonical cmp: PASS

$ PYTHONDONTWRITEBYTECODE=1 python3 \
    docs/papers122_126_sequence/proof_spikes/verify_stoch_gcd_zeta_transform.py
proper-residue gcd zeta-transform verifier: PASS
assertions=1199
bivariate coefficient equation: 1 <= n <= 600
exact arithmetic: Fraction only
fresh-vs-canonical cmp: PASS
```

The new total is exactly `1+2(600-1)=1199`: one coefficient-equation check
at `n=1`, and for each `2<=n<=600` one coefficient-equation check plus one
literal-residue reconstruction.  Despite its filename, this program does
**not** numerically evaluate zeta ratios, truncate the infinite product, or
encode Bernoulli independence.  It checks (A01.3), and it checks the original
finite PGFs independently from literal residues.  The analytic proof, not
the 1,199 assertions, carries (A01.4)--(A01.9).

### 4.2 Formula-by-formula re-entry audit

#### (A01.2)--(A01.3): PASS

For `n>1`, the first-step recursion is

```text
(n-1) G_n(z)
  = z sum_(d|n,d<n) phi(n/d) G_d(z).
```

Adding the `d=n` term and collecting `G_n` gives

```text
n G_n(z)
  = z sum_(d|n) phi(n/d) G_d(z) + (1-z)G_n(z).
```

At `n=1`, both sides equal `G_1=1`, so the stated boundary extension is
valid.  Since each `G_n` is a probability generating polynomial,
`|G_n(z)|<=1` for `|z|<=1`, and the Dirichlet series in (A01.2) converges
absolutely for real `s>1` (and, with the natural definition, for complex
`Re(s)>1`).

#### (A01.4): PASS

Multiply (A01.3) by `n^(-s-1)` and sum.  The divisor convolution factors as

```text
sum_n n^(-s-1) sum_(d|n) phi(n/d)G_d
 = [sum_m phi(m)/m^(s+1)] [sum_d G_d/d^(s+1)]
 = zeta(s)/zeta(s+1) * mathcal G(s+1,z).
```

This gives exactly

```text
mathcal G(s,z)
 = (1-z+z*zeta(s)/zeta(s+1)) mathcal G(s+1,z).
```

No exponent shift or missing `n=1` atom was found.

#### (A01.5): PASS

Iteration is legitimate.  Uniformly on a compact subset of `Re(s)>1`,

```text
mathcal G(s+J,z) = 1 + O(2^(-J)),
zeta(s+J)/zeta(s+J+1) = 1 + O(2^(-J)),
```

for `|z|<=1`.  Hence the terminal series tends to `G_1=1` and the product
converges normally.  At `z=1`, its partial products telescope to
`zeta(s)/zeta(s+J)`, whose limit is `zeta(s)`.

A wording repair would be needed only if this were retained: define the
complex-`s` extension before invoking normal convergence on `Re(s)>1`, or
keep every assertion on the real half-line.  This is not a mathematical
defect.

#### (A01.6)--(A01.8): PASS, BUT DIRECTLY OWNER-DERIVED

For real `s>1`, division by `mathcal G(s,1)=zeta(s)` produces factors

```text
q_(s,j) + (1-q_(s,j))z,
q_(s,j)=zeta(s+j+1)/zeta(s+j).
```

The zeta function is strictly decreasing on the real half-line `s>1`, so
`0<q_(s,j)<1`.  The complementary probabilities are `O(2^(-j))` and are
summable.  The infinite product is therefore the PGF of an almost surely
finite sum of independent Bernoulli variables.  Equations (A01.7) and
(A01.8) are correct.

The phrase “independent Bernoulli variables” is a distributional
factorization.  It does not claim that the original residue draws are
independent across times, and no such false claim appears in the dossier.

#### (A01.9): PASS / GENERIC CONSEQUENCE

Summability justifies termwise expectation.  Since the Bernoulli variables
are independent and have summable variances, the displayed mean and variance
are correct.  They receive no separate contribution credit once (A01.8) is
known.

### 4.3 The decisive owner equivalence

Alexeev, Barreto, Li, Lichtman, Price, Shah, Tang, and Tao,
[*Primitive sets and von Mangoldt chains: Erdős Problem #1196 and beyond*](https://arxiv.org/abs/2605.00301),
Section 10.2, explicitly construct the **zeta process**.  For every prime
`p` and positive integer `k`, they take independent exponential variables
`E_(p,k)` of rate `log p`, set

```text
e_(p,u) = max{k: E_(p,1),...,E_(p,k) >= u},
Z_u = product_p p^(e_(p,u)),
```

and prove

```text
P(Z_u=n)=1/(zeta(u)n^u),        Z_v | Z_u for u<v.
```

Thus they own not only a generic divisibility-chain framework but the exact
continuous zeta-distributed superprocess used by the new A01 repair.

The following unit-skeleton calculation is immediate from their definition.
Fix `u>1`, condition on

```text
Z_u=n=product_p p^(a_p),
```

and let `d=product_p p^(b_p)` divide `n`.  By exponential memorylessness,
each already present `p`-level survives from `u` to `u+1` with probability
`1/p`.  Hence, at one prime,

```text
P(e_(p,u+1)=b | e_(p,u)=a)
 = p^(-b)(1-p^(-1)),    0<=b<a,
 = p^(-a),              b=a.
```

Multiplying over primes yields the exact unit-skeleton kernel

```text
P(Z_(u+1)=d | Z_u=n) = phi(n/d)/n,       d|n.             (R1)
```

Indeed, for a prime whose exponent drops, its local factor is

```text
phi(p^(a-b))/p^a = p^(-b)(1-p^(-1));
```

for an unchanged exponent it is `phi(1)/p^a=p^(-a)`.  In particular,

```text
P(Z_(u+1)=n | Z_u=n)=1/n.                                  (R2)
```

Delete repeated states from the discrete sequence

```text
Z_u, Z_(u+1), Z_(u+2), ... .
```

Conditioning (R1) on a strict change gives

```text
P(Z_(u+1)=d | Z_u=n, Z_(u+1)<n)
 = [phi(n/d)/n]/[1-1/n]
 = phi(n/d)/(n-1),        d|n, d<n.                       (R3)
```

This is **literally A01's transition kernel**.  The kernel does not depend
on `u`, so deleting every self-loop from the unit-spaced zeta-process
skeleton produces the proper-residue gcd chain.

This must not be confused with the embedded chain of the continuous jump
times.  The continuous process can jump within a unit interval, whereas
A01 compresses the unit-spaced discrete skeleton.  Equation (R3) is the
exact and relevant relation.

### 4.4 The new Bernoulli theorem is the owned process's interval-change count

Let

```text
I_j = 1_{Z_(s+j+1) < Z_(s+j)}.
```

Because `Z_(s+j)` has the zeta distribution, (R2) gives

```text
P(I_j=0)
 = sum_n [1/(zeta(s+j)n^(s+j))] * 1/n
 = zeta(s+j+1)/zeta(s+j).                                  (R4)
```

There is also an exact independence argument.  Conditional on `I_j=0`,

```text
P(Z_(s+j+1)=n | I_j=0)
 = [n^(-(s+j))/zeta(s+j)](1/n)
   / [zeta(s+j+1)/zeta(s+j)]
 = n^(-(s+j+1))/zeta(s+j+1).
```

This is the unconditional law of `Z_(s+j+1)`.  Thus `I_j` is independent of
the next state.  The Markov property and induction make the entire sequence
`I_0,I_1,...` independent, with success probabilities

```text
1-zeta(s+j+1)/zeta(s+j).
```

Finally, the number of strict changes before the skeleton reaches `1` is the
absorption time of its self-loop-deleted chain (R3).

The skeleton does reach `1` almost surely: its states decrease with `j`, and
`P(Z_(s+j)>1)=1-1/zeta(s+j)` tends to zero.  Continuity from above rules out
a positive limiting state.  Therefore

```text
T_(N_s) =_d sum_(j>=0) I_j,
```

which is exactly (A01.8).  This proof is shorter than the Dirichlet-transform
proof and exposes the owner relation: the “second output” is the strict-unit-
interval count of Alexeev et al.'s explicit zeta process.

The unnormalized product (A01.5) is the same observation after multiplying
each Bernoulli factor by
`zeta(s+j)/zeta(s+j+1)` and telescoping.  It is not an owner-independent
second theorem engine.

### 4.5 Bounded direct-statement search

Additional searches used the exact and translated formulations
`phi(n/d)/n zeta process`, `totient zeta distribution Markov kernel`,
`embedded/strict jump chain zeta process`, the ratio
`zeta(s+j+1)/zeta(s+j)`, and the complete Bernoulli parameter through 2026.
No primary source was located that prints (R1)--(R4) or (A01.8) verbatim.

That bounded non-hit does not rescue the candidate.  Owner subtraction is
not limited to text-string identity: (R1)--(R4) are immediate conditional
laws of the explicit primary-source process, and (R3) is the literal A01
kernel.  The closest owner must therefore be upgraded from “framework owner”
to **direct temporal superprocess owner**.

### 4.6 Re-entry value decision

The repair satisfies the earlier mathematical request for a second
all-integer formula, but fails the reason that request was imposed.  After
correct subtraction, the package is:

1. a one-step law equal to conditioned Minami and also to the strict-change
   kernel (R3) of the 2026 zeta process;
2. generic history and divisor-DAG recursion;
3. a prime-power q-Stirling product, followed by generic Poisson-binomial
   consequences; and
4. an all-integer mixture product equal to the unit-interval change count of
   the same 2026 owner process.

Items 1, 2, and the process behind item 4 are directly owned or generic.
Item 3 remains a correct narrow identification, but no longer supports a
standalone paper after the direct temporal relation is registered.  Calling
the new theorem “genuinely aggregate” is mathematically fair; calling it a
genuinely independent residual is not.

**Final verdict: `KILL_DIRECT_2026_ZETA_PROCESS / RESERVE AS AN
OWNER-ADJACENT COROLLARY NOTE`.**  Do not freeze A01 as a P122--P126 paper.

Permitted archival ceiling:

> The conditioned random-gcd chain is the self-loop-deleted unit-spaced
> skeleton of the Alexeev et al. zeta process.  Fixed prime-power starts give
> the displayed normalized q-Stirling/Poisson-binomial absorption law, and a
> zeta-distributed start makes the number of strict unit-interval changes an
> independent Bernoulli sum with parameters
> `1-zeta(s+j+1)/zeta(s+j)`.

Mandatory language if the result is ever reused:

- lead with Alexeev et al. Section 10.2, not only their Definition 2.1;
- display (R1)--(R3) before presenting the gcd formulation;
- assign the zeta distribution, zeta process, unit skeleton, self-loop
  deletion, generic Dirichlet convolution, and Bernoulli-product conversion
  zero contribution credit;
- describe (A01.8) as a new corollary/identification of the owned process,
  not as an independent stochastic model; and
- retain `HOLD_EXTERNAL`; a bounded missing verbatim formula is not owner
  clearance.

The C3 decision remains `KILL / RESERVE AS A LEMMA`.  For a replacement
paper lane, the already proved odd-component graph recursion remains the
stronger option, with cograph/cotree structure fully zero-credited.
