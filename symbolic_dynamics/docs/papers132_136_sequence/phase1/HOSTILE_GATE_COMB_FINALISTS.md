# Hostile gate for the two combinatorial finalists

**Audit cutoff:** 2026-08-31.  
**External status:** `HOLD_EXTERNAL`.  
**Scope:** synchronous prefix-majority and repeated Morris--Pratt border-array
dynamics.  This is an independent theorem, owner, boundary, and collision audit;
it is not a novelty certificate.

## 1. Gate result

| candidate | mathematical audit | owner/collision audit | verdict |
|---|---|---|---|
| Synchronous prefix-majority | The fixed language, absence of nontrivial recurrence, sharp `ceil(log_2 n)` depth, every-target fibre formula, Fibonacci image count, and unique maximum fibre all survive an independent all-parameter rederivation.  No counterexample was found. | Husfeldt--Rauhe already use the exact prefix-majority threshold predicate as a dynamic partial-sums query.  They do not iterate the resulting word, but the present report omits this direct one-step adjacency and therefore overstates what remains unowned. | **REPAIR** |
| Repeated Morris--Pratt border array on `E_n` | Exact one-step image, all `n-1` two-cycles, exclusion of all other recurrent points, sharp depth `2n-4`, and the two unique factorial-maximal fibres survive rederivation and independent testing.  No counterexample was found. | No direct owner of *whole-array recomputation* was located in the bounded search.  The report nevertheless needs precise border-array census/validation attribution, a semantic firewall against ordinary failure-link iteration, and a publication-grade indexed mismatch lemma. | **REPAIR** |

Neither candidate is `KILL`: the audit found no false theorem and no source
printing the same iterative finite dynamical system.  Neither candidate is
`PASS` yet: both repairs below are mandatory and are substantive gate repairs,
not a lowering of the standard.  No paper number should be allocated before a
fresh review of the repaired reports.

## 2. Frozen artifacts and byte-exact replay

The reviewed bytes were frozen at `2026-08-31T14:05:58Z`:

```text
c6ceef77593181560cc75d539cbbf004f9d5e5144991c90c62e4e2f12c19d31b  replacement_scout/root/PREFIX_MAJORITY_REPORT.md
5df5558b3c68e222eb49b1cfc2f3d57c560e83014bac9b789b28dce7cb94fd98  replacement_scout/root/verify_prefix_majority.py
9ec3b30dae3e72579320d388ed16158ac9baaa387bf231d1a7dfdf9ffc148dea  replacement_scout/root/PREFIX_MAJORITY_CANONICAL.txt
624790f689f2b82dd2e7ff935d711be90c9d2d05f6ac7281d52755d2062a8faa  replacement_scout/prefix_function/REPORT.md
fa3bab8aa874765bcc12671adc51db44abc3017126dbe4e8f3702d7406f54f22  replacement_scout/prefix_function/verify_prefix_function_dynamics.py
4f125f26d98cf4574869d2ec356710ab6414d2e6fb1a0ebb3a531cc7f6f3be51  replacement_scout/prefix_function/CANONICAL.txt
84cc6a291c9a858a69e9d0e7dbfe4a748f4d0aa80edc29e04ed7067253f36bf1  phase1/verify_comb_finalists_hostile.py
```

Both candidate programs were run afresh with bytecode writing disabled.  The
comparison was against raw stdout, with no stripping, parsing, sorting,
normalization, or reserialization:

```bash
cd docs/papers132_136_sequence/replacement_scout/root
cmp -s <(PYTHONDONTWRITEBYTECODE=1 python3 verify_prefix_majority.py) \
  PREFIX_MAJORITY_CANONICAL.txt
# exit 0

cd ../prefix_function
cmp -s <(PYTHONDONTWRITEBYTECODE=1 python3 verify_prefix_function_dynamics.py) \
  CANONICAL.txt
# exit 0
```

Thus `CANONICAL` means the original stdout bytes exactly.  In particular, this
gate does not treat a reconstructed summary as a canonical match.

An independent verifier was also written without importing either candidate
verifier.  It uses literal prefix sums for the first map and literal
prefix/suffix comparison for the second.  Its fresh output is:

```text
INDEPENDENT HOSTILE AUDIT: PASS
prefix_majority_exhaustive_states=32766
prefix_majority_random_cases=1250
border_array_exhaustive_states=46233
border_array_large_witness_cases=54
checks=147768
scope=independent falsification only; all-n claims require proof
```

This covers every binary word through length 14, 1,250 additional deterministic
large/random prefix-majority cases, all inversion sequences through length 8,
and 54 enlarged sharp-witness cases.  It is independent falsification evidence;
the all-`n` conclusions below come from proofs.

## 3. Synchronous prefix-majority: all-parameter proof audit

For `w in {0,1}^n`, put `x_i=2w_i-1`, `S_i=sum_(j<=i)x_j`, and

```text
P_n(w)_i = 1[S_i >= 0].
```

The weak tie convention is essential.  Replacing `>=` by `>` changes the fixed
language, so it must remain visible in the title theorem and code.

### 3.1 Fixed points

Let `h=S_(i-1)` be the balance immediately before the next letter.  The fixed
condition gives the following complete local table:

| previous balance | letters that can agree with the output |
|---|---|
| `h>=1` | only `1` |
| `h=0` | `0` or `1` |
| `h=-1` | `0` or `1` |
| `h<=-2` | only `0` |

Starting at height zero, the only way not to lock into a constant tail is to
traverse `01`, returning from height `-1` to height zero.  Therefore the fixed
words are exactly

```text
(01)^r 0^(n-2r),  0<=r<=floor(n/2),
(01)^r 1^(n-2r),  0<=r<=floor((n-1)/2).
```

The asymmetric upper limit prevents double-counting the empty tail when `n` is
even.  The two families are otherwise disjoint and total `n+1`.  At `n=1`,
both words are fixed, as required.

### 3.2 Fixed-prefix amplifier and complete recurrence

Prefix compatibility is literal: the first `q` coordinates of `P_n(w)` depend
only on the first `q` coordinates of `w`.  Hence the maximal agreement prefix
of a nonfixed `w` is itself fixed and has a unique expression
`(01)^r b^ell`, with a fixed alternating core and `ell>=1`.

There is a boundary point that must not be skipped: the maximal agreement
prefix cannot end at the pure alternating core.  At balance zero, either next
input bit agrees with its threshold output.  Thus it always contains at least
one tail bit.

- In the positive branch its terminal balance is `ell`.  Even an all-zero
  continuation remains nonnegative for the next `ell` positions, so one
  application locks at least `2ell` ones.
- In the negative branch maximality forces `ell>=2`: after only one terminal
  zero the balance is `-1`, and either possible next input again agrees.  From
  balance `-ell`, even an all-one continuation remains negative for the next
  `ell-1` positions, so one application locks at least `2ell-1` zeros.

The alternating core cannot restart after a locked one or after the two locked
zeros in the negative branch.  Inductively,

```text
ell_t >= 2^t ell_0                    (positive),
ell_t - 1 >= 2^t(ell_0 - 1)          (negative).
```

Thus every orbit is fixed after at most `ceil(log_2 n)` steps; in particular,
there is no nontrivial cycle.  For `W_a=1^a0^(n-a)`, direct balance calculation
gives

```text
P_n(W_a)=W_min(2a,n).
```

`W_1` therefore has exact depth `ceil(log_2 n)`.  This also handles `n=1`,
where the depth is zero.  The resulting recurrent set and zeta function are
consequences, not separate assumptions.

### 3.3 Every target fibre

Write a target in maximal sign runs as

```text
y=b_1^(l_1)...b_s^(l_s),  b_j != b_(j+1),
C_m=binom(2m,m)/(m+1),     M_m=binom(m,floor(m/2)).
```

Every sign change of the source walk crosses the edge between `-1` and zero.
Cutting at these forced crossings gives a bijection, not merely a product of
known generating functions.

- For a constant target, reflection gives
  `|P_n^(-1)(1^n)|=M_n` and `|P_n^(-1)(0^n)|=M_(n-1)`.
- For `s>=2`, the first positive run must be even, the first negative run must
  be odd, and every internal run must be odd.  Failure of any parity condition
  makes the fibre empty.
- When the parities hold, the first excursion has factor
  `C_(l_1/2)` if `b_1=1` and `C_((l_1-1)/2)` if `b_1=0`; every internal run has
  factor `C_((l_j-1)/2)`; the uncapped terminal portion has factor
  `M_(l_s-1)`.

Consequently the formula in the candidate report covers every target,
including the empty-fibre cases and both constant targets.  Concatenating the
excursions and terminal meander is the inverse construction, so no compatibility
condition has been lost between factors.  Counting the admissible run patterns
obeys the Fibonacci recurrence and gives `|im P_n|=F_(n+2)`.

The maximum-fibre proof also survives the strictness attack.  On a fixed fibre,
`S -> |S|` injects into nonnegative meanders because `y_i` recovers whether
`S_i>=0` or `S_i<0`.  A nonconstant target forces a positive-time return of
`|S|` to zero, so the all-up meander is absent and the injection is strict.
The all-zero target has only `M_(n-1)<M_n` preimages for `n>=2`.  Absolute value
is a bijection from the fibre of `1^n` onto all `M_n` meanders.  Hence

```text
max_y |P_n^(-1)(y)| = binom(n,floor(n/2)),
```

uniquely at `1^n` for `n>=2`; the two length-one targets tie at one.  The
candidate verifier checks the formula for every target through length 19, not
only aggregate fibre histograms.

### 3.4 Counterexample and boundary attacks

The hostile implementation separately attacked weak ties, `n=1`, an alternating
prefix ending at height zero, the negative `ell=1` possibility, both constant
targets, all inadmissible run parities, nonconstant targets with several sign
changes, and the sharp family at powers and nonpowers of two.  No failure was
found.  The proof above closes these cases for all `n`.

## 4. Prefix-majority: owner and collision gate

### 4.1 Direct one-step adjacency that must be added

Husfeldt and Rauhe, [*New Lower Bound Techniques for Dynamic Partial Sums and
Related Problems*](https://doi.org/10.1137/S0097539701391592), SIAM Journal on
Computing 32(3), 2003, explicitly study maintaining the majority of prefixes of
a bit string.  Their threshold query at position `i` asks whether the first `i`
bits have sum at least `ceil(i/2)`, which is exactly the coordinate predicate
`P_n(w)_i=1` above.  Batched evaluation over all `i` is therefore not an
unowned definition.

That paper is a dynamic-data-structure lower-bound paper.  It does not, in the
material inspected, replace the bit string by the full answer vector and repeat
that replacement; nor does it state the fixed language, amplifier, sharp clock,
or inverse atlas.  It is therefore a mandatory subtraction, not a direct kill.

The existing report already correctly gives zero credit to classical
walk/excursion and sign-change tools, including Wallner, Sparre Andersen, and
Erdos--Hunt, and to generic majority-network language.  Those deductions remain.

### 4.2 Bounded direct-owner search

Primary-source/owner-directed searches were frozen at the audit cutoff after
queries for exact and semantic variants of:

```text
"iterated prefix majority" binary word
"prefix majority" transform dynamics
"running majority" / "cumulative majority" iteration
sign-of-partial-sums transform iterate
nested-prefix threshold network fixed points
prefix-majority ceil(log_2 n) convergence
```

No source was located that studies the repeated full-vector self-map and states
the present residual theorems.  This is only a bounded non-hit.  It must be
reported exactly that way; it is neither novelty nor priority evidence.

### 4.3 P1--P131 and current-batch collision firewall

- **P80** already owns a synchronous majority functional-graph paper.  Its
  cocktail-party rule has fixed points/two-cycles and one-step consensus outside
  its recurrent region; the present nested directed prefix thresholds are
  fixed-only with an unbounded logarithmic clock.  Only the literal amplifier is
  residual; generic majority/zeta packaging is zero credit.
- **P108** occupies Fibonacci dynamics rhetoric.  The Fibonacci image count here
  is a classification corollary, not a headline.
- **P111** occupies binary-word/lattice-path enumeration through inversion area.
  The present statistic is a partial-sum sign trace; it claims no area or
  `q`-polynomial.
- **P117**, **P122**, and **P126** occupy binary-run, sharp-depth/fibre, and
  logarithmic binary-refinement silhouettes.  This map neither reverses record
  blocks nor flips runs nor splits composition parts.
- **P130** demonstrates that a product fibre and unique maximum alone are not a
  paper contribution.  The inverse atlas must remain secondary to the literal
  fixed-prefix amplifier.
- Current finalists `A02`, `CT1`, and `SF1` act respectively on a divisor/Pratt
  network, centralizer-derived partition types, and stochastic sunflower
  transversals.  There is no literal carrier or update collision.  Repeated
  border arrays below also use a different carrier and proof engine.  The common
  short-paper silhouette “sharp clock plus fibres” receives zero portfolio
  credit.

### 4.4 Exact repair contract

The prefix-majority candidate becomes eligible for a new gate only after all of
the following edits are made:

1. Add Husfeldt--Rauhe with the exact threshold-query equivalence and say
   explicitly that the coordinate predicate/batched one-step operator receives
   zero originality credit.
2. Replace any implication from search miss to ownership by: “A bounded search
   did not locate an owner of the repeated full-vector dynamics; this is not
   novelty or priority evidence.”
3. Lead the proposed paper only with the residual conjunction: repeated
   full-vector iteration, exact fixed language, fixed-prefix amplifier, and
   sharp `ceil(log_2 n)` clock.  Keep Catalan factors, Fibonacci image, and
   general majority language as credited completion results.
4. Retain the strict maximum-fibre argument in full: injectivity of `S -> |S|`,
   the missing all-up meander for nonconstant targets, the `0^n` inequality, and
   the `n=1` tie.  Do not compress it to “by reflection.”
5. Rerun the verifier and require raw-stdout `cmp -s` against a deliberately
   regenerated canonical only if theorem-bearing bytes changed; record the new
   hashes and obtain a fresh hostile sign-off.

## 5. Repeated border-array dynamics: all-parameter proof audit

Let

```text
E_n={(e_0,...,e_(n-1)): 0<=e_i<=i}
```

and let `Pi_n(e)` be the ordinary longest-proper-border table of the integer
word `e`.  This is a self-map because its `i`th entry lies in `[0,i]`.

### 5.1 Exact one-step image

Every output is a valid border array by definition.  Conversely, take any word
realizing a valid border array and standardize its letters by order of first
occurrence.  The standardized value at position `i` is at most `i`, so the word
lies in `E_n`; standardization preserves the equality pattern and therefore all
borders.  The image is exactly the set of valid border arrays, for every `n`.

### 5.2 Recurrent atlas

For `1<=r<n`, define

```text
A_r=(0,1,...,r,0,...,0),
B_(r+1)=(0^(r+1),1,...,1).
```

Direct prefix/suffix inspection gives `Pi_n(A_r)=B_(r+1)` and
`Pi_n(B_(r+1))=A_r`.  These are distinct for all allowed `r`; hence there are
`n-1` exact two-cycles when `n>=2`.  At `n=1`, `(0)` is fixed.

To exclude additional recurrence, classify any valid table by its longest
agreement with the unique template selected by its second entry.  If `p_1=1`,
the initial slope is `0,1,...,r`; if it breaks, the next entry is zero.  A
realizing word has begun with `r+1` equal letters, and the next letter either
continues the slope or destroys every nonempty border.  If `p_1=0`, the maximal
initial zero run has length `k`; if it breaks, unit growth
`p_i<=p_(i-1)+1` forces the next entry to be one.  Thus a noncanonical valid
table agrees with its template through at least three coordinates.

At the first mismatch, the ordinary border recursion has the following complete
state machine:

```text
A1 -> B2 -> extension,
B0 -> A1 -> B2 -> extension.
```

Here the letter names record template type and the actual mismatch value, and
“extension” means strictly longer agreement with the partner template.  After
an `A` prefix, validity and unit growth force mismatch value one and its new
border is two.  After a `B` prefix, only mismatch values zero and two remain:
zero creates border one without extension, whereas two creates border zero and
resolves the mismatch.  Once resolved, a later first mismatch follows a zero
table value, so the next unresolved case is again `A1`.  The first mismatch
costs at most three iterates and each subsequent coordinate costs at most two.

Strict template-prefix growth rules out recurrence off the displayed templates.
It also yields, for `n>=4`, valid-state depth at most `2n-5` and arbitrary
carrier depth at most `2n-4`, because one application enters the valid image.

### 5.3 Sharp clock and small boundaries

The report's witnesses

```text
p_n=(0,0,1,0^(n-3)),
e_n=(0,1,0,2,1^(n-4))
```

obey `Pi_n(e_n)=p_n`.  Literal border recursion gives the alternating formulas
in equations (3.5)--(3.6) of the candidate report; every two steps advances one
canonical coordinate, and the last displayed state maps into `A_1`.  Hence
`p_n` has exact depth `2n-5` and `e_n` exact depth `2n-4` for `n>=4`.

The complete boundary table is

```text
n=1: 0,
n=2: 0,
n=3: 1,
n>=4: 2n-4.
```

The independent verifier additionally evaluates the witness formulas well
beyond the exhaustive range.  No off-by-one failure was found at `n=4`, at the
transition to the final two-cycle, or in the distinction between valid-state
and whole-carrier depth.

### 5.4 Every target fibre and unique maxima

Fix an arbitrary target table `p`, including invalid targets.  Expose a source
`e in E_n` from left to right.

- `p_0=0` is forced.  At position one, either target value zero or one uniquely
  fixes `e_1` relative to `e_0=0`.
- At position `i>=2`, a prescribed positive border value forces `e_i` to equal
  the already specified letter at the matching prefix position: at most one
  choice.
- A prescribed zero border must at least avoid the initial letter zero, leaving
  at most `i` choices from `0,...,i`.

Multiplication gives `|Pi_n^(-1)(p)|<=(n-1)!` for every target; invalid targets
simply have fibre zero.  Equality forces every coordinate from index two onward
to be zero, so only `0^n` and `A_1=(0,1,0^(n-2))` can qualify.  For either target,
the first two source entries are fixed and every later source entry may be any
nonzero value.  The sufficiency needs a little more care than the candidate
report gives it.  A nonzero *last* letter alone does not rule out a longer
border, so that sentence in the report is not a valid general argument.

For the `0^n` fibre, position zero is the only zero in the source.  Every proper
suffix therefore starts with a nonzero letter and cannot equal a prefix, which
starts with zero.  For the `A_1` fibre, positions zero and one are zero and all
later positions are nonzero.  A proper suffix starting at position at least two
again fails in its first letter; the only remaining possible suffix starts at
position one, and it fails in its second letter (`e_2!=0=e_1`).  Hence no prefix
after position one has a nonempty border.  Therefore both fibres have exactly
`product_(i=2)^(n-1)i=(n-1)!` elements and, for `n>=2`, they are the only
maximizers.  At `n=1`, there is one target and one source.

The candidate verifier checks the exact fibre of every target through `n=9`,
not merely the two candidate maxima.  The proof above supplies the all-`n`
upper bound and equality classification.

## 6. Border-array owner and collision gate

### 6.1 Owned background and missing attribution

Knuth--Morris--Pratt own the prefix/failure-function mechanism and its linear
computation ([primary DOI](https://doi.org/10.1137/0206024)).  Franek et al.,
[*Verifying a Border Array in Linear Time*](https://www.cas.mcmaster.ca/~franek/proceedings/border.pdf),
give a linear validation route.  Duval--Lecroq--Lefebvre,
[*Efficient Validation and Construction of Border Arrays and Validation of
String Matching Automata*](https://doi.org/10.1051/ita:2008030), treat validation,
generation, construction, and counts of distinct border arrays.  Gawrychowski,
Jez, and Jez, [*Validating the Knuth-Morris-Pratt Failure Function, Fast and
Online*](https://doi.org/10.1007/s00224-013-9522-8), treat validation and
minimum-alphabet realization.  The image census
`1,2,4,9,20,47,110,263,630`, validation, realization, and generation are all
owned background and receive zero contribution credit.

The current report names KMP and Gawrychowski--Jez--Jez but does not attach a
precise owner to its “classical valid-border-array census.”  That omission is
repairable but not acceptable at the final gate.

### 6.2 The semantic firewall required by the owner search

The border literature repeatedly “iterates” a failure function in the sense

```text
beta^j[i] = beta(beta^(j-1)[i]),
```

which follows failure links inside the fixed border table of one fixed word.
That is not the candidate map.  The candidate treats the entire integer array
`beta(w)` as a new word and recomputes its complete border table:

```text
w -> beta(w) -> beta(beta(w)) -> ... .
```

The distinction is mathematically decisive.  P112's killed scout C6 is exactly
failure-link descent to successive longest borders and is classically owned;
the present synchronous whole-table recomputation is different.  A manuscript
that merely says “iterate the prefix function” is ambiguous and risks claiming
an owned operation.

### 6.3 Bounded direct-owner search

Owner-directed searches were frozen after exact and semantic variants of:

```text
"iterated prefix function" / "iteration of prefix function"
"prefix function of the prefix-function array"
"border array of a border array"
"repeated border array" dynamics
"border array" two-cycle / dynamical system
recomputing KMP table on its own integer array
```

The KMP, Franek et al., Duval--Lecroq--Lefebvre, and
Gawrychowski--Jez--Jez primary texts inspected did not state the whole-table
self-map or its two-cycle/clock/fibre package.  Searches also targeted recent
arXiv records through the 2026-08-31 cutoff.  No direct iterative owner was
located.  This is a bounded non-hit only, never a novelty inference.  A
secondary cross-model novelty check was unavailable in this runtime, which is
an additional reason to retain `HOLD_EXTERNAL`.

### 6.4 P1--P131 and current-batch collision firewall

- **P112 scout C6** is the closest semantic collision: it follows the KMP
  failure-link chain of one word and was killed as directly owned.  Whole-table
  recomputation must be displayed next to that distinction in any paper.
- The carrier `E_n` is an inversion-sequence carrier and is bijective with
  permutations.  Carrier choice alone is zero credit.  **P105** already occupies
  permutation cycle-type pruning and a factorial/depth silhouette; here the
  recurrence is `n-1` two-cycles and the factorial occurs as a maximum fibre,
  not a deepest layer.
- **P122** already owns a permutation sharp-depth/image/fibre package.  Its proof
  uses left-to-right records and admissible cuts; this proof uses equality
  patterns, valid border tables, and KMP fallback.
- The same-batch inversion-rank candidate `PR1` has an exact owner
  (Allagan--Gao--Testart, arXiv:2608.24476) and is killed.  If the border map
  survives repair, it must be the sole inversion-sequence candidate; retaining
  both would be cosmetic carrier duplication.
- `A02`, `CT1`, and `SF1` have distinct carriers and updates.  Prefix-majority
  and the border map also have distinct literal maps and proof engines.  The
  repeated package “recurrent atlas, sharp clock, maximal fibre” is portfolio
  scaffolding, not an independent advance.

### 6.5 Exact repair contract

The border-array candidate becomes eligible for a new gate only after all of
the following edits are made:

1. Add Franek et al. and Duval--Lecroq--Lefebvre as precise owners for border
   validation/generation/census; retain KMP and Gawrychowski--Jez--Jez.  Mark the
   entire one-step image census and all standard validation/realization facts as
   zero-credit background.
2. Put the two notions of iteration side by side: failure-link composition
   `beta^j[i]` versus whole-array recomputation `beta(beta(w))`.  Cite P112-C6
   as the internal killed control and never use an unqualified title such as
   “iterating the prefix function.”
3. Replace the prose-only mismatch paragraph by an indexed lemma.  It must
   define the first mismatch position and partner template, prove the exhaustive
   transitions `A1 -> B2 -> extension` and
   `B0 -> A1 -> B2 -> extension`, and state why later mismatches cost at most two
   iterations.  Then derive `3+2(n-4)=2n-5` for valid arrays and add the one-step
   entry into the valid image.
4. Keep the boundary table `n=1,2,3,n>=4` and explicitly distinguish entry depth
   from period.  Show the witness trajectory through its first and final steps;
   do not delegate sharpness to enumeration.
5. Add the fibre proof for arbitrary targets, including invalid targets, explain
   why a positive prescribed border leaves at most one letter, and state the
   `n=1` boundary.  Replace the false general sentence “a nonzero last letter
   rules out every nonempty border” by the proper-suffix-start argument given in
   Section 5.4 above.  Do not state only the two maximal fibres.
6. Add the P105/P112-C6/P122/PR1 collision firewall and the one-inversion-carrier
   portfolio rule.  Rerun raw-stdout `cmp -s`, record fresh hashes after any
   theorem-bearing code/report changes, and obtain a fresh hostile sign-off.

## 7. Final disposition

The proof audit does **not** authorize either candidate for external release.
It establishes a narrower conclusion:

```text
synchronous prefix-majority:  REPAIR, no counterexample, direct one-step owner adjacency
repeated border-array map:     REPAIR, no counterexample, bounded direct-iteration non-hit
external status:              HOLD_EXTERNAL
```

After the exact repairs, prefix-majority has the cleaner residual headline: a
familiar coordinate predicate acquires a nontrivial fixed language and sharp
logarithmic convergence under repeated synchronous feedback.  The border-array
map has the stronger recurrent/clock/fibre package but carries a denser classical
owner neighborhood and an inversion-sequence portfolio constraint.  That is a
portfolio ranking, not a novelty judgment.

No Git operation was performed by this hostile gate.
