# P166 Round-6 owner and collision search log

Status: **bounded search completed / KILL_ALL / HOLD_EXTERNAL**  
Search date: 2026-09-03  
Rule: all cited classical machinery receives zero contribution credit.  A
bounded non-hit never establishes novelty, priority, or freedom to circulate.

## 1. Protocol

For each literal map the search proceeded in four passes:

1. exact update phrase and obvious synonyms;
2. carrier plus the strongest temporal statistic;
3. carrier plus inverse/preimage/endpoint terminology;
4. local P1--P165 and same-batch string/silhouette search.

The web pass prioritized primary papers, publisher records, and arXiv paper
records.  Search-result summaries were not treated as proofs.  Once a
candidate failed the theorem gate, the owner search remained bounded rather
than being inflated into a novelty review.

## 2. `MPS`: maximum-peak shaving

Representative queries:

```text
Dyck paths lower all highest peaks simultaneously dynamics
Dyck path peak lowering maximum height operation
Dyck path peak down move bounded-height preimages
parallel highest peaks Dyck path
```

External subtraction:

- T. Mansour, [*Counting peaks at height k in a Dyck path*](https://arxiv.org/abs/math/0203222),
  directly owns height-resolved peak enumeration.
- A. Bacher, [*Generalized Dyck paths of bounded height*](https://arxiv.org/abs/1303.2724),
  owns the transfer-matrix/rational-generating-function machinery for
  bounded-height excursions.
- M. Barnabei, F. Bonetti, and M. Silimbani,
  [*The Catalan matroid*](https://doi.org/10.1016/S0097-3165(03)00121-3),
  is representative background for Dyck height coordinates.

No source in this bounded pass stated the exact simultaneous global-maximum
update.  This non-hit is not used positively.  The internal collision is
already fatal:

- P144, `papers/144-leftmost-dyck-reassociation/`, occupies a literal Dyck
  dynamics with pointwise clock and exact target fibres.
- `docs/papers162_166_sequence/scouting/word_combinatorial/SCOUT.md` records
  `DAE`, coordinatewise Dyck-height truncation, and `MHE`, Motzkin-height
  truncation.  Both have the maximum-height clock and every-target
  bounded-walk enumeration; they were killed against P160/P144.
- `MPS` has a parity cap rather than a scalar cap, but the proof still reduces
  every iterate to global height capping and every inverse to bounded-height
  paths.

Decision: **KILL_INTERNAL_DAE_P144_P160**.

## 3. `XSD`: exact-two-secant duality

Representative queries:

```text
finite projective plane exact two secants point set dual
PG(2,q) 2-secants point set duality
finite projective plane secant transform iteration
every target set of 2-secants inverse
```

External subtraction:

- [*Avoiding secants of given size in finite projective planes*](https://arxiv.org/abs/2409.14213)
  studies point sets through exact prescribed line-intersection sizes.
- [*A new lower bound for the smallest complete (k,n)-arc in PG(2,q)*](https://doi.org/10.1007/s10623-018-00592-8)
  fixes the standard `i`-secant notation and counting identities.
- Projective point-line duality and exact secant counts are therefore zero
  credit even though the bounded pass found no direct iteration of the full
  line-set transform.

The exact `p=2,3` functional graphs do not extrapolate to an all-parameter
clock or inverse atlas.  P161 already occupies finite-field incidence
geometry, so a parameter-by-parameter census has no residual value.

Decision: **KILL_NO_PARAMETER_SPINE**.

## 4. `MEG`: mutual-eccentric metric graph

Representative queries:

```text
mutually eccentric vertices graph
mutual eccentric graph transform iteration
eccentric graph complement universal vertices
inverse eccentric graph labelled enumeration
```

Direct primitive owners:

- J. Akiyama, K. Ando, and D. Avis,
  [*Eccentric graphs*](https://doi.org/10.1016/0012-365X(85)90188-8),
  defines an eccentric-vertex graph transform and explicitly studies when it
  is the complement.
- [*Mutually Eccentric Vertices in Graphs*](https://combinatorialpress.com/ars-articles/volume-067-ars-articles/mutually-eccentric-vertices-in-graphs/)
  directly owns the mutual-farthest predicate used in the literal update.

The first paper uses the one-sided eccentric relation while `MEG` requires
both directions, so it is not asserted as an exact owner of the complete
map.  Still, the primitive is direct.  On a `{1,2}` metric the rewrite
`complement(G) union K_{U(G)}` makes all further dynamics an elementary
universal/isolated-vertex case split of depth at most two.  That residual is
too thin independently of any exact owner hit.

Decision: **KILL_DIRECT_PRIMITIVE_AND_SHALLOW**.

## 5. `CTB`: continuous-time path balancing

Representative queries:

```text
local load balancing path chips adjacent difference two
continuous-time discrete load balancing nearest-neighbor path
unit transfer larger load to smaller rate one
absorbing endpoint law local balancing path
```

External subtraction:

- L. Feuilloley, J. Hirvonen, and J. Suomela,
  [*Locally Optimal Load Balancing*](https://arxiv.org/abs/1502.04511),
  treats the same adjacent discrepancy-at-most-one terminal criterion and
  discrete load balancing on paths.
- P. Berenbrink et al.,
  [*Improved Analysis of Deterministic Load-Balancing Schemes*](https://arxiv.org/abs/1404.4344),
  treats discrete diffusion/load exchange and potential-style convergence
  analysis on graphs.

The bounded pass did not locate the exact independent rate-one edge-clock
chain.  The pilot nonetheless stops at finite rational DAG recursion: it
does not supply a target formula or a sharp all-parameter absorption law.
P129's pile dynamics and P151's path first-passage package reinforce the
internal crowding.

Decision: **KILL_FINITE_DP_ONLY**.

## 6. `DPF`: divisor-count partition fragmentation

Representative queries:

```text
integer partition replace each part by number of divisors
iterated divisor function stopping time
divisor-count fragmentation partition dynamics
inverse iterated divisor function partition fibre
```

External subtraction:

- Y. Buttkewitz, C. Elsholtz, K. Ford, and J.-C. Schlage-Puchta,
  [*A problem of Ramanujan, Erdos and Katai on the iterated divisor function*](https://arxiv.org/abs/1108.1815),
  directly owns iteration of `d(n)` as an arithmetic object.
- C. Soulé and A. Smati,
  [*Sur un problème de S. Ramanujan*](https://doi.org/10.1016/j.crma.2004.11.014),
  records the older Ramanujan/Erdos--Ivic iterated-divisor setting.

No literal partition-fragmentation source was found, but all of its temporal
content is the maximum of the owned scalar stopping times.  The target axis
is only coefficient extraction over independent part types.  P126 and P147
already have stronger natural refinement/consolidation dynamics.

Decision: **KILL_OWNED_CLOCK_NO_INVERSE_ATLAS**.

## 7. `GGT`: pairwise-GCD triangle

Representative queries:

```text
"pairwise gcd" triangle map iteration
"gcd(a,b)" "gcd(b,c)" "gcd(c,a)"
gcd dynamical system divisor triples
meet semilattice triangle map fibres
```

The bounded external pass found ordinary pairwise-GCD computation but no
source for this exact simultaneous triple update.  Again, that non-hit is not
positive evidence.  The literal map is a meet-polynomial operation and its
prime-valuation form is

```text
(a,b,c) -> (min(a,b), min(b,c), min(c,a)).
```

It reaches the diagonal minimum after the second step.  P128 and P142 occupy
the GCD/valuation product engine; the same-batch `CNG` ledger contains the
strictly richer cyclic adjacent-minimum window dynamics and every-target
fibres.  This is a direct proof-silhouette collision.

Decision: **KILL_INTERNAL_MEET_GCD**.

## 8. Consolidated gate

| ID | exact literal owner | classical primitive subtraction | internal collision | theorem gate | result |
|---|---|---|---|---|---|
| `MPS` | bounded non-hit | height peaks; bounded Dyck paths | P144, killed DAE/MHE, P160 | mathematically passes | **KILL** |
| `XSD` | bounded non-hit | exact secants; point-line duality | P161 carrier vicinity | fails | **KILL** |
| `MEG` | mutual primitive direct | eccentric graph/complement | graph-projection crowding | shallow | **KILL** |
| `CTB` | bounded non-hit | local load balancing | P129/P151 | finite DP only | **KILL** |
| `DPF` | scalar clock direct | iterated divisor function | P126/P147 | no inverse atlas | **KILL** |
| `GGT` | bounded non-hit | GCD as meet | P128/P142/CNG | shallow collision | **KILL** |

No row is `GREEN_OWNER_THIN`; no theorem contract is authorized.  External
status remains **HOLD_EXTERNAL**.
