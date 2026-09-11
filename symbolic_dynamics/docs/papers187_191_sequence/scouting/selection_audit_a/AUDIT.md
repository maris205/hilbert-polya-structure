# Process-separated preselection hostile audit A

Date: 2026-09-04 UTC  
Scope: unnumbered candidates `A01`, `A02`, `RC01`, `RC03`, and `RC05` only.  
Terminal boundary: `OWNER_AMBER / HOLD_EXTERNAL / UNNUMBERED`.

## Verdict first

This audit found no counterexample to the displayed all-parameter formulas of
`A01`, `A02`, `RC01`, or `RC03`.  That statement combines written
re-derivation with bounded exact falsification; the exact controls alone are
not proofs.  The selection verdicts are:

| qualitative order | candidate | verdict | decision-bearing reason |
|---|---|---|---|
| first | `RC01` cyclic divisor quotient | **PROVISIONAL_PASS** | The literal divisor update is natural, the height-layer induction closes for all exponent caps, and the temporal clock/fixed-locus theorem is genuinely distinct from the target-indexed local-constraint trace. |
| second | `RC03` self-cardinality truncation | **PROVISIONAL_PASS** | The rank iterate gives a closed all-time theorem and unique extremal tail, while source-size decomposition separately gives every labelled one-step fibre.  The order-labelled carrier is less natural than `RC01`, but no mechanical P185/P186 transfer was found. |
| third | `A02` class-size power on dihedral groups | **PROVISIONAL_PASS** | The conjugacy-equivariant update has three genuine parity regimes and a closed all-parameter atlas.  It ranks below `RC01/RC03` because both axes ultimately reuse the same exceptional-doubling congruence and because ordinary power-map/class-size ownership risk is high. |
| fourth | `A01` nilpotent last-nonzero selector | **DOWNGRADE** | The fibre polynomial is correct and nontrivial, but the entire temporal/spectral axis is the generic idempotence of a deliberately terminalizing map.  After Jordan theory is assigned zero credit, only one substantial axis remains. |
| fifth | `RC05` left-stabilizer subset map | **KILL** | The literal stabilizer mechanism already occurs in the P172--P176 scout, and the nonabelian extension uses the same idempotence and subgroup-poset inversion.  It also contains a left/right-coset wording error exposed by a nonnormal subgroup of `S_3`. |

This is a non-numeric ordering under the requested considerations:
naturality, independence of the two axes, closure of the all-parameter proof,
separation from P1--P186, and owner risk.  It is not a weighted score or a
paper-number allocation.  `PROVISIONAL_PASS` means “retain for the next
selection gate,” not “proved,” “novel,” “owned,” or “submission-ready.”

## Audit provenance and frozen inputs

This reviewer process did not write any lane file.  It read the two lanes as
untrusted review material, rebuilt the five updates from their definitions,
and wrote only this `selection_audit_a` package.  Representation/process
separation is recorded; it is not statistical or logical independence of
errors.  The attack program contains and hard-fails the following SHA-256
bindings before running any mathematical check:

| frozen input | SHA-256 |
|---|---|
| `algebra_lane/CANDIDATES.md` | `9a556b2eeb0dbcf3d7ce97200dddfd920127b0edb977c2e49e33b7af14c01fb1` |
| `algebra_lane/KILL_LEDGER.md` | `8bbca099fab07c941092a6411fb6c0f03cab27ce30081d72747b83bd82e8665b` |
| `algebra_lane/OWNER_SEARCH_LOG.md` | `7f67238603b0d15f3eccea2c9fd31cec3fd24e195e61128c926fc62404235b6f` |
| `algebra_lane/THEOREM_SPIKES.md` | `ad922463c85e0bfb87db143d6ade7ddba58363d46168fbdf16caca91169451b8` |
| `root_coordinator/CANDIDATES.md` | `2e42d9c6122dbd130ff004d8ac5277dda197288f973dec429060009cb6b05768` |
| `root_coordinator/KILL_LEDGER.md` | `e2e471f4f42e8340754b4971119cb59ba480433643b8b75443539dc44d6b30cf` |
| `root_coordinator/OWNER_SEARCH.md` | `ae30d5ac50e485046233034efe021850e983c7227506ae02259217f425ada34d` |
| `root_coordinator/THEOREM_SPIKES.md` | `cfcd47f804ea41a72aa048b4d2e1093395400ad25014e84a40eb6fb2eeae8dcf` |
| P172--P176 algebra scout/kill ledger | `2a8e024e6f6c8c6029b74387e4634141ed547d13cbfaf85bf50becab60a060a8` |

The canonical aggregate of these path/hash pairs is
`7e2f6dc8aa5023dd17eed7d16bc114abfc43706c81bb72d539980bab736f9fdc`.
The owner-search documents are evidence about bounded searches, not absence
proofs.  No search non-hit is used below as novelty, priority, ownership, or
freedom-to-operate evidence.

## Candidate-by-candidate re-derivation

### RC01 — cyclic divisor quotient — PROVISIONAL_PASS

#### Literal reduction and closure

For one prime power `p^a`, write the exponent word as
`e=(e_0,...,e_{m-1})`.  The quotient update is exactly

```text
D(e)_i = max(e_i-e_{i+1},0),   indices modulo m.
```

Different primes do not interact, so state evolution, fixed-state counts, and
labelled fibres factor prime by prime.  This is an equality of literal
updates, not merely an analogy.

#### Temporal theorem and the claimed induction

Suppose the current exponent cap is `h`.  If `D(e)_i=h`, then necessarily
`e_i=h` and `e_{i+1}=0`.  Since every exponent is at most `h`, this forces

```text
D(e)_{i-1}=0,   D(e)_{i+1}=0,
```

and the height-`h` coordinate remains `h` at the next update.  Thus every
surviving top-layer peak after one step is isolated and frozen.  All other
coordinates are at most `h-1`; deleting the frozen peak and its adjacent
zeros leaves path segments governed by the same positive-difference rule at
cap at most `h-1`.  Induction on `h` therefore gives stabilization by time
`a` for `m>=3`.  The witness

```text
(0,a,1,0,...,0)
```

has tail `a`, so the bound is sharp.  For `m=2`, one update leaves at most one
positive coordinate and hence is already fixed.

The fixed equation
`e_i=max(e_i-e_{i+1},0)` says that every positive `e_i` has
`e_{i+1}=0`.  Hence positive support is an independent set of the cyclic
adjacency relation, and each occupied support vertex has exactly `a` possible
positive heights.  This proves the weighted independent-support census.  As
all orbits reach fixed points, recurrence equals the fixed locus.

#### Fibre matrix, independently reconstructed

For a labelled target `b`, define the local matrix by

```text
M_b(u,v) = 1[max(u-v,0)=b],   0<=u,v<=a.
```

Expanding `tr(M_{b_0}...M_{b_{m-1}})` chooses a cyclicly closed exponent
history `(u_0,...,u_{m-1})` and contributes one exactly when every local
positive-difference constraint produces the target.  It is therefore the
one-step fibre, including value zero for unreachable targets.  The attack
program did not multiply the lane matrices: it fixed the first exponent and
propagated the two constraint branches (`v=u-b` for `b>0`, and `v>=u` for
`b=0`), closing the last edge directly.  Agreement with brute source fibres
was exact.

#### Boundaries and hostile findings

- `N=1` has only the all-zero valuation word and is fixed.
- `m=1` is not covered by the headline `m>=2`: every exponent maps to zero,
  so the tail is one for a nonzero source, the only fixed state is zero, and
  the zero-target fibre is `a+1`.  The one-by-one trace formula remains valid.
- `m=2` has sharp tail one for `a>0`; equal positive exponents provide a
  witness by mapping to zero.
- Repeated maxima create no exception: only maxima surviving the first
  difference are isolated frozen peaks.
- Multi-prime target fibres were checked directly on joint exponent words
  and equal the product of prime-local fibres.

**Minor scope issue:** a promoted contract should state the `m=1` theorem
explicitly instead of listing `m=1` only as a boundary obligation.  No formula
counterexample was found within the stated `m>=2` range.

#### Separation and owner risk

The layer-freezing proof and cyclic local-constraint trace are not mechanical
instances of P184's one-coordinate co-gcd valuation ladder.  They also give
two different proof objects: an induction over transient height layers and a
target-indexed cyclic constraint partition.  The bounded owner log found
Ducci/cellular-automaton neighbors but no inspected direct literal owner.
That non-hit has no clearance force; status remains `OWNER_AMBER`.

### RC03 — self-cardinality truncation — PROVISIONAL_PASS

#### Closed iterate and endpoint

Fix the source `A` and let `r_A(k)=|A intersect [k]|`.  If `k_0=|A|` and
`k_{t+1}=r_A(k_t)`, induction gives

```text
T^t(A)=A intersect [k_{t-1}]   for t>=1.
```

Indeed, the displayed set has size `k_t`, so applying `T` once more
intersects it with `[k_t]`; because `k_t<=k_{t-1}`, this is exactly
`A intersect [k_t]`.  The nonincreasing integer sequence stops at the largest
`rho` for which `[rho] subseteq A`; the endpoint is `[rho]`.  Thus every
recurrent state is one of the fixed initial segments.

To have tail `n-1`, a source must decrease in size by exactly one at every
step from `n-1` to zero.  The first source therefore has size `n-1` and cannot
contain `1`; hence it is uniquely `{2,...,n}`.  This source realizes the
chain, proving both sharpness and uniqueness for `n>=2`.

#### Terminal and one-step fibres

Endpoint `[r]` means precisely that `A` contains `1,...,r` and, when `r<n`,
omits `r+1`; all later labels are free.  Its terminal fibre is therefore
`2^(n-r-1)` for `r<n`, and the full endpoint has the single source `[n]`.

For a labelled one-step target `B`, let `b=|B|` and `M=max(B)`, with `M=0`
for the empty target.  A source of size `k` must contain exactly `B` below or
at `k`, and choose its other `k-b` points strictly above `k`.  Thus its
contribution is `binom(n-k,k-b)`.  Feasibility is exactly

```text
max(b,M) <= k <= floor((n+b)/2),
```

which proves both the displayed sum and the exact first-image criterion.

#### Boundaries and hostile findings

- At `n=0`, the empty set is the unique fixed state and source.
- At `n=1`, both the empty and full sets are fixed; maximum tail is zero, so
  deepest-state uniqueness is deliberately not asserted.
- The empty-target one-step fibre is
  `sum_{k=0}^{floor(n/2)} binom(n-k,k)`; this was checked separately rather
  than inferred from a generic target loop.
- The full target has its unique full-set predecessor.
- The unique maximum-tail state and every labelled target formula survived
  all exact boxes.

No quantifier or formula defect was found.  The main selection risk is
conceptual: the update depends on the chosen total order, and both temporal
and inverse arguments use cardinality ranks.  Nevertheless, the inverse
source-size partition is not the temporal monotone-rank induction, and the
literal map is not P185's word-diversity delay or P186's rank-compression
support update.  The existing bounded search is too narrow to lower
`OWNER_AMBER`.

### A02 — conjugacy-class-size power on dihedral groups — PROVISIONAL_PASS

#### Literal map

In `D_{2n}`, noncentral rotations have conjugacy-class size two.  The identity
and, for even `n`, `r^(n/2)` are central and have class size one.  Reflection
classes have size `n` for odd `n` and `n/2` for even `n`.  Since reflections
have order two, this gives exactly:

```text
noncentral r^k -> r^(2k);
central rotations -> themselves;
reflections -> themselves when 4 does not divide n;
reflections -> 1 when 4 divides n.
```

No conjugacy-class table was assumed in the attack program: class sizes were
recomputed by conjugating every element under the defining multiplication
law, and exponentiation was then performed literally.

#### Cycles, tails, images, and pure two-power tails

For odd `n`, doubling is a permutation of `Z/nZ`; elements of exact order `d`
split into `phi(d)/ord_d(2)` cycles.  Reflections are fixed.

For `n=2^a m` with `a>=1`, CRT separates an eventually vanishing `2^a`
coordinate from a permuted odd coordinate.  Rotational recurrence therefore
consists of the `m`-element odd-order subgroup plus the exceptional central
rotation.  If a noncentral exponent is not divisible by `m`, its tail is the
number of doublings required to annihilate its `2`-primary coordinate,
`a-min(a,nu_2(k))`.  If `k=m u` is a nonzero pure `2`-primary exponent and is
not central, the exceptional central state arrests the last doubling, giving
`a-1-nu_2(u)`.  For `m=1`, this yields sharp depths `1,2,3` at
`n=4,8,16`, respectively.  When `a=1`, every reflection is fixed; when
`a>=2`, every reflection has tail one.

The image counts follow directly from the even rotation targets, with the
central exception and reflection branch added separately.  They are `2n`,
`3n/2+1`, and `n/2` in the odd, `2 mod 4`, and `0 mod 4` regimes.

#### Exact fibres

For each rotation target, direct solution of `2k=j (mod n)` after removing
the exceptional central sources, then adding back each source governed by a
special branch, gives exactly the displayed predecessor set.  Reflection
targets are singleton fibres when `4` does not divide `n` and empty otherwise.
The maximum fibres are consequently `1`, `2`, and `n+1` in the three stated
regimes.

The entire `n=2 mod 4` branch was checked at `n=6,10,14,18,22`.  The literal
presentation at excluded `n=2` is the Klein four group, every class has size
one, and the map is the identity with maximum fibre one.  Thus the stated
`n>=3` hypothesis is essential and must remain visible in every promoted
theorem.

#### Hostile findings and risk

No counterexample was found for `n>=3`.  One wording defect should be cleaned
before promotion: “the same divisor/order formula over `d|m` gives the
noncentral rotational cycles” includes the `d=1` identity cycle, which is
central.  The formula is correct; “odd-order subgroup cycles” is the accurate
scope.

This update is natural under group isomorphisms because conjugacy-class size
and powering are preserved.  Its weakness is contribution independence:
cycle/tail/image and predecessor results all descend from the same exceptional
doubling description.  Ordinary power maps, CRT, multiplicative orders,
dihedral conjugacy classes, and class-size arithmetic receive zero credit.
The bounded direct-owner non-hits do not offset this generic ingredient risk,
so `OWNER_AMBER / HOLD_EXTERNAL` remains strict.

### A01 — nilpotent last-nonzero selector — DOWNGRADE

#### Fibre theorem

Use Jordan chains with level zero at the bottom.  A source of height exactly
`h` mapping to nonzero `y=sum y_i e_i` must satisfy:

- its level `h-1` coefficient in every block of length at least `h` is the
  prescribed `y_i`;
- every higher level is zero;
- every lower level is free;
- every block shorter than `h` is entirely free.

Such a stratum exists exactly when `h<=L(y)`, and the number of free
coordinates is

```text
D(h)=sum_i min(h-1,lambda_i).
```

The strata are disjoint, so summing gives the displayed fibre formula.  At
`h=1`, there are zero free coordinates and the contribution is exactly one:
the target itself.  This explicitly disposes of the dangerous omitted-
constant possibility.  For unequal blocks, short blocks become wholly free
once `h` exceeds their lengths, while a target coefficient in such a block
would forbid that height; this is precisely why the upper limit is the
minimum supported block length.

The `L`-histogram follows by allowing arbitrary coefficients only on blocks
of length at least `ell`, and subtracting those supported only above `ell`.
Maximum fibres occur exactly when every supported block has maximum length.
The zero fibre is one because minimality of `h(v)` makes the last nonzero
iterate nonzero for every nonzero source.

#### Temporal/spectral theorem

Every nonzero source is sent by definition to its last nonzero iterate, which
lies in `ker N`; every kernel vector is fixed.  Hence `T^2=T`, image and fixed
locus are `ker N`, and all tails are zero or one.  The transition matrix is
idempotent of rank `|ker N|=q^b`, giving the displayed `0/1` characteristic
polynomial.  These statements are correct also for `N=0`.

#### Why the candidate is downgraded

There is no formula defect in the audited contract.  The downgrade is about
paper-scale contribution.  The temporal map was defined to jump directly to
the terminal nonzero state, so idempotence, the depth bound, recurrence, and
the transition spectrum are generic consequences of terminalization rather
than a second nilpotent-dynamics theorem.  The Jordan height-stratum fibre
polynomial is the sole substantial residual after classical Jordan theory is
subtracted.  Similarity equivariance makes the construction well-defined but
does not cure that one-axis concentration.  The P109 carrier differs, yet the
remaining proof engine is still classical Jordan-coordinate counting.  This
candidate should be reserve material unless a genuinely independent second
axis is found.  Owner status remains amber; bounded non-hits are not novelty.

### RC05 — left-stabilizer subset dynamics — KILL

#### Correct portion of the theorem

For every subset `A` of a finite group `G`, the left setwise stabilizer

```text
S(A)={g in G:gA=A}
```

is a subgroup.  A subgroup `H`, regarded as a subset, satisfies `S(H)=H`, so
the map is idempotent and its image/fixed locus is the subgroup lattice.  If
`f(H)` is the number of subsets with exact stabilizer `H`, then the number
invariant under `H` is `2^[G:H]`, and

```text
2^[G:H] = sum_{K>=H} f(K).
```

Möbius inversion on the full subgroup poset gives the displayed fibre
formula without any normality assumption.  The attack used the actual
subgroup posets of `C_1`, `C_4`, `S_3`, and `D_8`; every exact fibre agreed.
The empty target set has no predecessors because every stabilizer contains
the identity.  The full target `G` has exactly two predecessors, the empty
and full source sets.

#### Concrete nonnormal counterexample to the wording

Under left multiplication by `H`, an orbit is

```text
H a = {h a:h in H},
```

which is a **right** coset under the standard convention; a left coset is
`aH`.  For a nonnormal order-two subgroup of `S_3`, the attack found a right
coset `Ha` that is not any left coset `a'H`, while its exact left stabilizer is
still `H`.  Thus the spike sentence saying an invariant subset is a union of
“left `H`-cosets” is false for the requested nonnormal boundary.  Replacing
“left” by “right” repairs the explanation but creates no new mathematics and
does not alter the fibre count.

#### Kill basis

Even after that wording repair, the same literal subset-to-stabilizer map was
already recorded as A13 in the P172--P176 algebra scout and killed as a
shallow static stabilizer invariant.  Passing from cyclic groups to
nonabelian groups changes the subgroup poset but not the proof engine:
idempotence plus exact-stabilizer Möbius inversion.  A nonabelian example is
therefore a generic extension, not a new independent axis.  The historical
collision is decisive; external non-hits cannot reopen it.

## Exact attack receipt

`attack.py` uses five representation routes different from the lane pilots:

| candidate | reviewer-owned route | finite pressure |
|---|---|---|
| `A01` | explicit height strata in bottom-to-top chain coordinates, with every `h` contribution counted separately | six boxes, 333 vectors; includes `h=1`, zero map, repeated and unequal block lengths |
| `A02` | literal Cayley multiplication, exhaustive conjugation, and direct modular predecessor solving | every `3<=n<=24`; all three parity regimes; pure powers `4,8,16`; excluded `n=2` |
| `RC01` | first-exponent-conditioned constraint propagation around the cycle, not matrix multiplication | caps `0..4`, lengths `1..6`, 26,214 valuation words; joint two-prime fibre factorization |
| `RC03` | one-based `frozenset` carrier and direct source-size partitions | all subsets through `n=11`, including `n=0,1`, empty/full targets, and unique deepest states |
| `RC05` | explicit Cayley tables and full subgroup-poset Möbius recursion | `C_1`, `C_4`, `S_3`, `D_8`; nonnormal subgroup and coset-handedness witness |

The program made **196,597** successful assertions.  Two fresh Python
processes produced byte-identical 1,061-byte, 10-line stdout streams with
SHA-256
`ce5124dcf3819b7c6a9246c5db10de11fa754e45bfd17e2393f8fc5f100e0c3b`.
The saved stream is `canonical_stdout.txt`.

Finite controls establish only that no counterexample occurred in those
boxes and that the coded definitions agree with the tested formulas.  They do
not prove the all-parameter theorems, validate novelty, estimate error
probability, certify owner clearance, or allocate any paper number.

## Finding ledger

| ID | candidate | class | finding | disposition |
|---|---|---|---|---|
| `SA-A-01` | `RC05` | theorem wording / nonnormal boundary | Left-action orbits are right cosets `Ha`, not left cosets `aH`; the phrases diverge for nonnormal `H`. | Valid finding; count formula unaffected; candidate already KILL. |
| `SA-A-02` | `RC05` | historical collision / low contribution | Nonabelian ambient groups retain the exact A13 stabilizer/idempotence/Möbius engine. | KILL; cannot be reopened by search non-hits. |
| `SA-A-03` | `A01` | axis independence / low contribution | Temporal and spectral claims are generic consequences of defining `T` as terminalization. | DOWNGRADE to reserve pending a genuinely independent axis. |
| `SA-A-04` | `A02` | wording precision | The `d|m` cycle sum includes the `d=1` identity, so “noncentral rotational cycles” is inaccurate. | Minor pre-promotion wording repair; formula unchanged. |
| `SA-A-05` | `A02` | quantified boundary | The sharp fibre cap does not extend to `n=2`; the explicit `n>=3` hypothesis is essential. | No defect in current scope; retain boundary prominently. |
| `SA-A-06` | `RC01` | boundary completeness | At `m=1` the map is one-step zeroing, with zero-target fibre `a+1`; this deserves an explicit separate clause. | Minor pre-promotion scope completion; no defect for `m>=2`. |

No other formula or quantifier finding remains open in this preselection
audit.  “No open formula finding” is not external readiness: all retained
candidates remain `OWNER_AMBER / HOLD_EXTERNAL / UNNUMBERED`.
