# Independent hostile gate: replacement combinatorial candidates

**Scope:** exactly three candidates were reviewed: replacement-scout `FM1`,
replacement-scout `FM2`, and synchronous prefix-majority.  No fourth system
was considered or promoted here.

**Evidence cutoff:** 2026-08-31 UTC.  **External status:** `HOLD_EXTERNAL`.
The searches below are bounded non-hits, never novelty or priority evidence.

## 1. Verdict

| candidate | correctness gate | owner/value gate | P1--P131 gate | verdict |
|---|---|---|---|---|
| Synchronous prefix-majority | The displayed formulas survive.  The sharp clock and full fibre data replay exactly.  The report's proof of *strict* uniqueness of the maximal fibre is incomplete as written, but has a short valid repair below. | No exact literal-map owner was located.  Random-walk excursion factorisation, Catalan/meander counts, sign-change theory, and general majority-network language are zero credit.  The residual is the literal iteration, its fixed-prefix amplifier, and the resulting sharp logarithmic clock; the inverse atlas remains a useful classification, not a new Catalan method. | Literal separation from P117/P122/P126/P111 holds, but P80, P108, and P130 also have to be subtracted explicitly. | **REPAIR**.  The theorem survives, but the current report is not gate-clean until the strictness proof and owner/internal subtraction are inserted. |
| `FM1`, least-cycle opening | The depth, endpoint, pointwise polynomial, integer-break maximum, and layer EGF are correct and replay. | Joyal/Pitman/Heilman/Duchi and Cayley/species machinery remove essentially all of the mechanism.  The residual product is the immediate independent choice of closing zero or one admissible root path in each target component. | Directly crowded by P105's minimum-labelled cycle surgery, P114's rooted-forest endpoint/fibre package, and P130's product-fibre/maximum packaging. | **KILL**.  Correct lemma bank, not a paper-scale system. |
| `FM2`, least indegree-zero leaf to loop | The cyclic-core endpoint, exact clock, every-permutation depth polynomial, aggregate layers, and unique maximum are correct and replay. | After cyclic-core decomposition and Cayley's fixed-root forest formula are credited, every displayed coefficient is a one-line choice of noncyclic fixed points followed by a forest count. | P114 is a direct pruning-engine collision; P105 and the current functional-graph pruning lane further crowd the carrier. | **KILL**.  This is the thinner of the two finite-map candidates and may not be paired with or substituted for `FM1`. |

There is therefore **one repairable survivor and no clean PASS in the current
artifacts**.  The two endofunction candidates are both killed; the instruction
never to allow both is satisfied more strongly than by choosing between two
near-duplicates.

## 2. Material inspected and exact replay

The following four files were read in full before the decisions:

- `replacement_scout/root/PREFIX_MAJORITY_REPORT.md` (159 lines);
- `replacement_scout/root/verify_prefix_majority.py` (193 lines);
- `replacement_scout/combinatorial/SCOUT.md` (457 lines); and
- `replacement_scout/combinatorial/verify_combinatorial_scout.py` (967 lines).

Neither report nor verifier was edited.  Fresh isolated replays gave byte
matches against both frozen canonical transcripts:

```text
prefix-majority: lengths 1..19
states=1,048,574
assertions=5,894,725
signature_sha256=0941adf80ac62d37d57a5e380b999069b932e946d6ee857bf4f443774ea9969a
canonical comparison=IDENTICAL

replacement combinatorial scout: 20 literal systems
parameter-labelled states=426,937
assertions=1,812,761
canonical comparison=IDENTICAL
FM1 states through n=6=50,069
FM2 states through n=6=50,069
```

The source hashes at review time were:

```text
b88e04cf3b55d0bf1a3d68dd480e978376b6363d496ddb695b8941ef2d7becb7  combinatorial/SCOUT.md
0caf257635f1fd508e2a1f809093d1616b9febf45c6d283fcf01d7098548c92f  combinatorial/verify_combinatorial_scout.py
9c3f5334814e4e3cfbf1f1a15befdfd079f0762bc6ba6ae82ee45cd318176201  root/PREFIX_MAJORITY_REPORT.md
5df5558b3c68e222eb49b1cfc2f3d57c560e83014bac9b789b28dce7cb94fd98  root/verify_prefix_majority.py
```

This establishes faithful implementation and extensive finite
falsification only.  It does not decide ownership or replace an all-parameter
proof.

## 3. Prefix-majority: hostile proof audit

For `w in {0,1}^n`, put `x_i=2w_i-1`, `S_i=sum_{j<=i}x_j`, and

```text
P_n(w)_i = 1[S_i >= 0].
```

### 3.1 Fixed language: PASS

At balance `h>=1`, a zero cannot be fixed, since the new balance remains
nonnegative.  At `h<=-2`, a one cannot be fixed.  At height zero a fixed word
may write `1` and lock into ones, or write `0` and move to height `-1`; at
height `-1` it may write `0` and lock into zeros, or write `1` and return to
zero.  Hence the fixed words are exactly

```text
(01)^r 0^(n-2r),  0<=r<=floor(n/2),
(01)^r 1^(n-2r),  0<=r<=floor((n-1)/2).
```

They are disjoint and number `n+1`.  This part of the report is correct.

### 3.2 Sharp `ceil(log_2 n)` clock: PASS, but expand the proof

Because a prefix-majority output through position `q` depends only on the
length-`q` prefix, the fixed-language classification applies to every prefix
on which `w` already agrees with `P_n(w)`.  Write the maximal such prefix as

```text
(01)^r b^ell,
```

with alternating-core length `c=2r` and `ell>=1`.  If `b=0` and the word is
not fixed, then in fact `ell>=2`: after a lone zero at height zero, either
possible next input bit also agrees with its prefix-majority output, contrary
to maximality.

- On the positive branch, the balance after the locked prefix is `ell`.
  Even an all-zero continuation remains nonnegative for the next `ell`
  positions.  Thus the next fixed prefix has the same core and at least
  `2ell` locked ones.
- On the negative branch, the balance is `-ell`.  Even an all-one
  continuation stays negative for the next `ell-1` positions.  Thus the next
  fixed prefix has the same core and at least `2ell-1` locked zeros.

The same-core assertion is important and should not be left implicit.  A
locked `1` immediately after `(01)^r` cannot extend the alternating core.  A
locked zero branch has at least two zeros, so it cannot extend the core
either.  Iteration therefore gives

```text
positive branch: ell_t >= 2^t ell_0,
negative branch: ell_t-1 >= 2^t(ell_0-1).
```

This proves the upper bound `ceil(log_2 n)`.  For the lower bound, if
`W_a=1^a0^(n-a)`, then

```text
P_n(W_a)=W_min(2a,n).
```

Starting with `a=1` proves that `10^(n-1)` has depth exactly
`ceil(log_2 n)`, including the `n=1` boundary.  Hence all recurrent points
are fixed.  This is the strongest residual theorem after owner subtraction.

### 3.3 Every-target fibre: formulas PASS, contribution must be narrowed

Let the target have sign runs `b_1^l_1 ... b_s^l_s`, let

```text
C_m = binom(2m,m)/(m+1),
M_m = binom(m,floor(m/2)).
```

For a constant target the counts are `M_n` for `1^n` and `M_(n-1)` for
`0^n`.  For `s>=2`, feasibility requires

```text
l_1 even if b_1=1,
l_1 odd  if b_1=0,
l_2,...,l_(s-1) odd.
```

When feasible, the reported formula

```text
A(b_1,l_1) * product_(j=2)^(s-1) C_((l_j-1)/2) * M_(l_s-1),
A(1,l)=C_(l/2),  A(0,l)=C_((l-1)/2),
```

is correct.  Crossings can occur only across the edge `{-1,0}`; cutting at
successive crossings gives an initial excursion, odd-length interior
excursions, and a final meander.  Concatenation is the inverse.

That proof mechanism is not available as a contribution.  Michael Wallner's
primary dissertation explicitly decomposes signed lattice walks into an
alternating sequence of positive and negative excursions followed by a final
meander; the simple-walk formulas here are a particularly transparent
specialisation of that architecture: [Wallner, *Combinatorics of lattice
paths and tree-like structures*](https://doi.org/10.34726/hss.2016.38100).
Classical persistence and sign-change results are likewise prior background:
[Sparre Andersen, *On the fluctuations of sums of random variables
II*](https://doi.org/10.7146/math.scand.a-10407) and
[Erdos--Hunt, *Changes of sign of sums of random
variables*](https://msp.org/pjm/1953/3-4/pjm-v3-n4-p01-p.pdf).

The atlas may remain in a paper because it completely classifies the inverse
geometry of this literal map.  It must be phrased as an application of owned
excursion decomposition, not as a new Catalan/meander factorisation.

### 3.4 Fibonacci image: PASS as a corollary only

Let

```text
L=z/(1-z)       (arbitrary positive last run),
O=z/(1-z^2)     (positive odd run),
E=z^2/(1-z^2)   (positive even run).
```

The two constant targets contribute `2L`.  A nonconstant feasible target
contributes `(E+O)L/(1-O)`.  Therefore

```text
2L + (E+O)L/(1-O) = (2z+z^2)/(1-z-z^2),
```

and `|im P_n|=F_(n+2)`.  This is a clean system corollary, but it is not a
second independent proof engine and may not be advertised as a new
Fibonacci family.

### 3.5 Unique maximal fibre: REPAIR the written proof

The report currently says that reflection embeds every target fibre into the
all-positive meander fibre and then asserts uniqueness.  An injection proves
the upper bound, not strictness.  The missing strict argument is short.

For a source walk `S` with fixed sign target `y`, map it to

```text
R_i=|S_i|.
```

`R` is a nonnegative simple-walk meander.  The map is injective on a fixed
target fibre because `y_i` recovers the sign: `S_i=R_i` when `y_i=1` and
`S_i=-R_i` when `y_i=0`.

If `y` is nonconstant, a `1 -> 0` target change forces `S_t=0`, while a
`0 -> 1` change forces `S_(t+1)=0`.  Thus every image `R` returns to zero at
a positive time.  The all-up meander `R_i=i` is missing, so the injection is
strict.  If `y=0^n`, its fibre is `M_(n-1)<M_n` for every `n>=2`.  If
`y=1^n`, taking absolute values is a bijection onto all `M_n` nonnegative
meanders.  Hence

```text
max_y |P_n^(-1)(y)| = M_n,
```

with unique maximiser `1^n` for `n>=2` and the stated tie at `n=1`.

This replacement paragraph is mandatory.  Without it, the current report
does not prove its uniqueness sentence.

## 4. Prefix-majority owner gate

### 4.1 Exact and synonymous searches

The bounded primary-source search used all of the following description
families, with formula variants and 2025--2026 recency checks:

```text
"prefix majority" binary words iteration
"running majority" binary sequence transform
"cumulative majority" binary sequence map
iteration of the sign of cumulative/partial sums
lower-triangular all-ones threshold Boolean map
nested-prefix / Ferrers-neighbourhood majority dynamics
prescribed sign runs of a simple walk + Catalan product + Fibonacci image
```

No source was found defining this exact length-preserving map and proving its
iteration, fixed-prefix doubling, sharp `ceil(log_2 n)` clock, or the same
combined theorem package.  This is only a search non-hit.

### 4.2 Closest owners and zero-credit allocation

| source neighborhood | what it owns here | what it does not currently own |
|---|---|---|
| Wallner's signed-walk excursion decomposition | alternating positive/negative excursions, terminal meander, and therefore the structural route behind the run-by-run fibre product | the repeated prefix-majority map and fixed-prefix amplification |
| Sparre Andersen; Erdos--Hunt; ballot/reflection theory | persistence, meander/Catalan counts, signs and sign changes of partial sums | the literal finite dynamical system and its sharp iteration clock |
| Goles--Montealegre--Salo--Torma, [*PSPACE-completeness of majority automata networks*](https://doi.org/10.1016/j.tcs.2015.09.014) | general synchronous/sequential/block-sequential majority-network vocabulary and generic finite-state orbit questions | this directed nested-prefix threshold family or its formulas |
| P80 cocktail-party majority | internal portfolio ownership of a synchronous majority family, complete functional graph, basins, zeta, and probabilistic outcome laws | nested prefix neighborhoods, walk-sign inverse geometry, or logarithmic prefix amplification |

The correct residual is therefore not "a new majority rule," "a new Catalan
interpretation," or "a new Fibonacci enumeration."  It is the exact dynamics
of one specified triangular threshold map, led by the fixed language and
sharp clock, with a complete owner-credited inverse atlas.

## 5. Prefix-majority collision firewall through P131

| occupied item | collision | surviving distinction |
|---|---|---|
| **P80** cocktail-party majority | same broad synchronous-majority carrier language; P80 already owns complete-functional-graph, basin, recurrent, and zeta packaging | P80 acts on an undirected cocktail-party graph with a family-specific total-weight reduction.  Prefix-majority is a nested directed threshold map whose irreversible prefix amplifier gives unbounded `ceil(log_2 n)` depth.  All generic majority claims are nevertheless removed. |
| **P108** capped Fibonacci absorption | Fibonacci sequence and sharp hitting-clock rhetoric already occur internally | P108's Fibonacci recurrence is the literal state evolution on an integer square.  Here Fibonacci counts only the one-step image language; it is a corollary, not the clock mechanism. |
| **P111** positive Heisenberg word area | binary-word/lattice-path statistics and exact finite-word enumeration are occupied | P111's statistic is inversion area and its Gaussian polynomial; prefix-majority outputs the sign trace of partial sums.  No area, inversion, or `q`-polynomial survives as a claim. |
| **P117** odd cyclic run reversal | binary runs, recurrent classification, and parity-dependent clocks are occupied | P117 flips bits inside cyclic runs and can have two-cycles.  Prefix-majority neither reverses nor flips a current run; it is acyclic and amplifies a fixed prefix.  Run-composition bookkeeping alone receives no credit. |
| **P122** even record-block reversal | sharp depth plus every-target fibre/image packaging is occupied | P122 is a lexicographically descending permutation map with record-cut DP.  There is no record cut or permutation action here; packaging is not used as a separator. |
| **P126** balanced composition refinement | base-two logarithmic clocks, products over one-runs, image decoders, and Fibonacci/restricted-composition silhouettes are occupied | P126 changes composition length by synchronous part splitting.  Prefix-majority preserves word length and performs global prefix thresholding.  The survivor must be the fixed-prefix amplifier, not "another binary refinement clock." |
| **P130** crossing-component fibre geometry | pointwise product fibres and unique maximum are already an internal paper shape | the carriers and local inverses differ, but this confirms that "product fibre + unique maximum" alone cannot carry the new paper. |

No literal conjugacy to P1--P131 was found.  The table is nevertheless a
substantive narrowing: after these deductions, the sharp iteration theorem
must remain the lead result.

## 6. Precise repair contract for prefix-majority

The candidate may re-enter selection only with all four repairs below.

1. Replace the maximal-fibre paragraph by the strict absolute-value injection
   in Section 3.5, including the constant-zero comparison and `n=1` boundary.
2. Expand the fixed-prefix lemma to prove `ell>=2` on the negative branch,
   preservation of the same alternating core, both amplification recurrences,
   and the exact `W_a -> W_min(2a,n)` witness.
3. Add Wallner, Sparre Andersen, Erdos--Hunt, general majority networks, and
   internal P80 to the owner/collision section.  Assign all ballot,
   reflection, excursion, Catalan, meander, and general threshold-network
   machinery zero contribution credit.
4. State the Fibonacci OGF derivation explicitly and demote it, the zeta
   formula, and the unique-fibre corollary below the fixed-language/clock
   theorem.

After repair, the admissible two-theorem contract is exactly:

- **Theorem A (residual lead):** fixed language, convergence of every orbit,
  and sharp maximum depth `ceil(log_2 n)` via fixed-prefix amplification.
- **Theorem B (owner-credited system classification):** feasible target-run
  language and every-target one-step fibre, with Fibonacci image and unique
  maximum as corollaries.

Forbidden claims include novelty/priority, a new Catalan interpretation, a
new majority-network theorem in general, a new Fibonacci model, and any
statement that the literature search proves absence of an owner.

## 7. `FM1` hostile gate: correct but KILL

### 7.1 Formula audit

For an endofunction `f:[n]->[n]`, `FM1` redirects the least-labelled vertex
on any nontrivial cycle to itself.  Each step opens one nontrivial cyclic
component and cannot create another.  Therefore

```text
depth(f)=number of nontrivial cyclic components,
max depth=floor(n/2),
endpoint=open every original cycle at its minimum.
```

The fixed targets are loop-rooted forests, counted by `(n+1)^(n-1)`.  For a
target forest `F` and loop-root `r`, let `a_r(F)` count nonroot vertices `v`
whose path from `v` to `r`, excluding `r`, has all labels greater than `r`.
Then

```text
B_F(u)=product_r (1+a_r(F)u).
```

This is correct.  In a component rooted at `r`, a source either keeps the
loop or replaces it by `r -> v`; the latter closes the unique root path into
a cycle that reopens at `r` exactly under the displayed label condition.
Components are independent.  The integer-break maximum follows immediately
from `1+a_r<=|T_r|`, and

```text
exp((1-u)T(z)) (1-T(z))^(-u),  T=z exp(T),
```

is the standard cycle-of-rooted-trees EGF with nontrivial cyclic components
marked by `u`.

### 7.2 Owner search and subtraction

Exact searches for repeated least-cycle opening, minimum-cycle vertex to
self-loop, and the displayed pointwise polynomial found no direct literal
owner.  That non-hit does not rescue the candidate.

- [Pitman, *Random mappings, forests, and subsets associated with
  Abel--Cayley--Hurwitz multinomial
  expansions*](https://www.mat.univie.ac.at/~slc/wpapers/s46pitman.pdf)
  explicitly decomposes mappings into a cyclic permutation plus rooted
  forest and gives the fixed-root forest-volume formula.
- [Heilman, *Tree/Endofunction Bijections and Concentration
  Inequalities*](https://doi.org/10.37236/10560) removes one edge from every
  cycle and orders/reconnects cycles through their minima.
- The current 2026 paper of Duchi, Lillo, Puerto, Rosas, and Trandafir,
  [*The Genesis Sequence, Tree Records and
  Endofunctions*](https://arxiv.org/abs/2606.14393), cuts and inserts cycle
  edges to relate connected endofunction girth to labelled tree records and
  derives tree/forest record generating functions.
- [Joyal's mapping-species
  treatment](https://doi.org/10.1016/0001-8708(81)90052-9) and Cayley's
  forest formula own the ambient cycle-of-trees EGF and all aggregate forest
  counts.

After those sources receive zero credit, the product polynomial is exactly
the componentwise list of legal one-edge cycle closures.  Its proof is the
definition plus independence.  The integer-break extremum and species EGF do
not provide a second independent advance.

### 7.3 Internal collision and value ruling

P105 uses the same labelled permutation-cycle skeleton and the same minimum
label to drive cycle surgery; it already contains an exact iterate, depth
census, and target fibre theorem.  Extending that skeleton from permutations
to endofunctions by adding passive in-trees does not create a new cycle
mechanism.  P114 owns rooted-forest endpoint assembly, pruning
clocks, local fibres, and Cayley/species control.  P130 confirms that a
pointwise product plus an elementary extremum is not by itself a fresh paper
shape.

The literal maps are not identical: P105 peels every cycle over time, whereas
`FM1` opens one whole cyclic component.  That is enough for a lemma-level
noncollision, not enough for paper-scale residual value.  **`FM1` is KILL.**
Its formulas may remain in the scout as negative evidence or a future lemma;
changing the scheduler, opening cycles simultaneously, or adding zeta/layer
corollaries cannot trigger re-entry.

## 8. `FM2` hostile gate: correct and thinner, KILL

### 8.1 Formula audit

`FM2` redirects the least indegree-zero vertex to itself.  Original cyclic
vertices never become leaves; every original noncyclic vertex is processed
after its descendants.  Thus

```text
depth(f)=n-|Cyc(f)|,
endpoint=original cycles plus loops on every original noncyclic vertex,
fixed targets=permutations.
```

For a target permutation `sigma` with `m` fixed points,

```text
B_sigma(u)
 = 1 + sum_(k=1)^m binom(m,k)(n-k)n^(k-1)u^k.
```

Choose the `k` target fixed points that were noncyclic in the source.  The
remaining `n-k` vertices are the specified roots, and Cayley's fixed-root
forest formula gives `(n-k)n^(k-1)`.  Consequently

```text
|E^(-1)(sigma)|=(n+1-m)(n+1)^(m-1)       (m>0),
L(n,k)=binom(n,n-k)(n-k)!(n-k)n^(k-1),
```

with the stated conventions.  The identity is the unique largest target.
All of this is correct.

### 8.2 Owner, collision, and value ruling

Exact searches for leaf-to-loop endofunction dynamics, indegree-zero to
self-loop pruning, and asynchronous pruning to a permutation found no direct
literal owner.  But Pitman's cyclic-set/rooted-forest decomposition and
Cayley's fixed-root formula already give every coefficient once the endpoint
is observed.  The update order contributes no statistic: it only linearises
a standard bottom-up forest elimination.

P114 is the decisive internal collision.  It already owns parallel rooted-
forest leaf peeling, endpoint and clock, root-set basins, target-local fibre,
height layers, and Cayley/species enumeration.  Retaining deleted leaves as
loops and serialising by least label changes the presentation, not the proof
engine.  P105 and the killed current functional-graph restriction scout make
the endofunction carrier still more crowded.

Unlike `FM1`, the basin depends only on the number of fixed points of the
target, so there is not even a fine target geometry left after forest
subtraction.  **`FM2` is KILL.**  It may not be promoted alongside `FM1`, used
as an automatic fallback for it, or revived by a different leaf scheduler,
parallel update, or a restatement of the same Cayley sum.

## 9. Final selector instruction

- Send **only prefix-majority** forward, and only with status `REPAIR`, under
  the two-theorem narrowed contract in Section 6.
- Keep `FM1` and `FM2` as permanent owner/value kills for this round.
- Do not infer an external novelty decision from the exact-literal search
  non-hits.
- Do not assign a paper number until the prefix-majority repair is checked
  against this gate.
