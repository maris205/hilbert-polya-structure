# Hostile algebraic/root gate: `A02`, `M01`, and `X01`

Status: **INDEPENDENT HOSTILE REVIEW / NO PAPER NUMBERS / HOLD EXTERNAL**  
Review date: **2026-08-31 UTC**

## Outcome first

| candidate | decision | decisive reason |
|---|---|---|
| `A02` | **PASS -- INTERNAL STAGE-2 CONTRACT ONLY** | After full subtraction, the literal divisor self-map still carries one coherent residual package: an arithmetic-to-signed-Boolean conjugacy, the complete recurrent census, a DAG-height entry bound, and an all-target one-step fibre formula.  No exact literal/equivalent owner was located in the bounded primary-source search. |
| `M01` | **KILL** | The map and every advertised formula are elementary consequences of the published invariant-factor formula for `Lambda^2 G`.  The rank-three carrier is an artificial closure accident, not a natural invariant family beyond rank three. |
| root `X01` | **KILL** | This is exactly a unipotent finite linear permutation `I+F` with `F` nilpotent.  Its fixed strata, `p`-power periods, cycles, and zeta follow immediately from standard finite-linear/Jordan machinery, and the same Frobenius-chain proof engine is already explicitly fenced by the P1--P131 portfolio. |

These decisions concern internal theorem value only.  They establish neither
novelty nor priority and authorize no release, posting, submission, or owner
contact.

## Review method and search boundary

The review read the literal definitions and proposed contracts in
`scouting/algebraic/SCOUT.md`, `scouting/root/SCOUT.md`, and
`proof_spikes/FROBENIUS_SHEAR_REPORT.md`, then searched both the displayed
maps and their structural normal forms.  Queries included quoted forms of
`gcd(n,(n/d)phi(d))`, totient-complement divisor maps, negative-self-loop
triangular Boolean networks, iterated exterior squares of finite abelian
groups, `Lambda^2(Lambda^2 G)`, unipotent `I+N` cycle structure, and
Frobenius/linearized-polynomial functional graphs.  Recent 2025--2026 primary
records were included.  Search non-hits below are bounded observations, never
owner-absence certificates.

The main primary controls are:

- Ford--Konyagin--Luca study the relation `p_j | p_(j+1)-1` and Pratt-tree
  height, so prime-chain geometry is fully background
  ([author preprint](https://arxiv.org/abs/0904.0473)).
- Veliz-Cuba et al. formalize AND-NOT (signed conjunctive) networks and the
  signed-wiring-diagram representation used by the Boolean reduction
  ([author preprint](https://arxiv.org/abs/1211.5633)); Chen--Gao--Basar give
  broad periodic-orbit/system-reduction theory for conjunctive networks over
  weakly connected digraphs
  ([author preprint](https://arxiv.org/abs/1708.01975)).
- Frei--Loughran--Newton, Lemma 6.5, state the complete invariant-factor
  formula for the exterior square of a finite abelian group
  ([current author version, Lemma 6.5](https://arxiv.org/html/1508.02518v4#S6.SS3)).
- Finite-linear functional graphs and periodic points are mature: see
  Hernandez-Toledo
  ([publisher DOI](https://doi.org/10.1081/AGB-200066211)),
  Mullen--Vaughan on linearized permutations
  ([publisher DOI](https://doi.org/10.1016/0024-3795(88)90179-6)),
  Li on periodic points of a linear transformation
  ([publisher DOI](https://doi.org/10.1016/j.laa.2012.06.022)), and Reis on
  functional graphs of linear finite dynamical systems
  ([publisher DOI](https://doi.org/10.1016/j.laa.2022.10.011)).

The Cohen--Hachenberger paper cited in the root scout is only an adjacent
control: its advertised dynamical system is the map induced on monic
irreducible polynomials, not the present truncated-ideal state map
([publisher abstract](https://doi.org/10.1017/S0013091500020733)).  Likewise,
Reis's 2025 paper concerns splitting fields of iterated additive polynomials
and extension-field periodic statistics, not this literal truncation
([author preprint](https://arxiv.org/abs/2502.19141)).  Neither should be
mislabelled a direct owner; the decisive subtraction for `X01` is generic
finite-linear theory plus the internal firewall.

## `A02`: pass only after aggressive subtraction

### Literal reduction

Let `P` be a nonempty finite set of primes, `n=product_(p in P) p`, and let a
divisor `d|n` correspond to its support `S`.  For

```text
F_n(d)=gcd(n,(n/d) phi(d)),
```

squarefreeness gives

```text
F(S)=(P\S) union N(S),
N(S)={p : some q in S satisfies p | q-1}.
```

With edges `q -> p` when `p | q-1`, all nonloop edges strictly decrease the
prime and hence form a DAG.  In complemented coordinates `y_p=1-x_p`, the
update is the signed-conjunctive rule

```text
y'_p = (not y_p) AND product_(q -> p) y_q.       (A)
```

This explicit form makes the hostile objection precise: the temporal proof is
a feed-forward phase induction in an AND-NOT network.  The arithmetic
factorization, the DAG, the source language, and generic phase propagation
receive zero credit.

### Exact zero-credit subtraction

The following may appear in exposition but cannot be counted as
contributions:

1. Euler's product formula for `phi(d)` and squarefree support encoding;
2. the prime-chain/Pratt relation and any use of Pratt height;
3. the AND-NOT/signed-interaction representation (A);
4. the generic fact that a finite feed-forward network is handled in
   topological order;
5. inclusion--exclusion as a method, and generic finite-map conversion from
   periodic points to cycles or zeta factors; and
6. a claim of novelty inferred from the failure of the quoted searches to
   find the exact string.

### Residual theorem contract that clears the internal value floor

`A02` passes only as the conjunction below, for every nonempty finite prime
set `P`, with all edge orientations and empty-parent conventions explicit.

1. **Literal conjugacy.**  Prove the divisor-support identity state by state,
   not merely the Boolean model in isolation.
2. **Complete recurrent set.**  If `s` is the number of vertices with no
   incoming Pratt edge, prove that there are no fixed states, exactly `2^s`
   recurrent states, and hence exactly `2^(s-1)` cycles, all of exact period
   two.  Give the explicit topological phase decoder from the `s` source
   phases; do not count the generic induction separately.
3. **Entry control.**  Prove the advertised entry-time bound in terms of the
   longest directed path `h`, including `|P|=1` and disconnected induced Pratt
   DAGs.  The current report sketches but does not yet fully write this
   induction.  Call it a bound, not an exact clock, unless a sharpness theorem
   and extremizers are actually proved.
4. **Every-target fibres.**  For every `B subseteq P`, prove the stated
   inclusion--exclusion formula, including targets outside the image, and
   separately check that the forced-one set and forced-zero parent set are
   disjoint in every surviving summand.  This is the strongest residual
   output because it is target-wise rather than only a total image count.
5. **Independent control.**  Retain the integer-divisor versus Boolean-DAG
   statewise verifier.  Enumeration is falsification evidence only.

The value judgment is narrow but positive: the complete recurrent decoder
and the all-target fibre law coexist for one literal arithmetic self-map and
are enough for one short internal theorem paper.  The arithmetic dressing
alone would not pass.  Failure of either items 2 or 4 sends the candidate to
`RESERVE`, and failure of the literal identity sends it to `KILL`.

### P1--P131 firewall

No direct carrier/update collision was found.  `A02` is not P84's unitary
Cayley SFT and Ramanujan periodic-spectrum package, P97's sumset squaring, P100's valuation absorber,
P128's translation--GCD polynomial map, or P131's Euclidean quotient queue.
Its separating fingerprint is a deterministic divisor-lattice map whose
negative self-coordinate and prime-divisibility DAG force source-parametrized
two-cycles and whose inverse problem has a target-wise formula.  This is a
literal separation, not an external novelty finding.

## `M01`: kill as an elementary corollary on an artificial closure

For

```text
G = direct_sum_i Z/p^(a_i)Z,
```

Frei--Loughran--Newton's Lemma 6.5 gives the complete type formula for
`Lambda^2 G`.  On partitions of length at most three it immediately becomes

```text
()        -> ()
(a)       -> ()
(a,b)     -> (b)
(a,b,c)   -> (b,c,c).
```

Everything proposed in the scout follows by inspecting these four lines:
`W^3=W^2`, the fixed types, image size, and all one-step and terminal fibres.
Partition counting and the classification of finite abelian groups also
receive zero credit.  There is no residual dynamical mechanism after this
subtraction.

The carrier makes the value problem worse.  Rank at most three is closed only
because `binom(3,2)=3`; at rank four the exterior square can have six
generators.  Thus the cutoff is selected to manufacture a finite self-map,
not inherited from a natural all-rank invariant family.  Bounding the exponent
does not repair that artificial rank boundary.

The P1--P131 registry has no literal exterior-square paper, but literal
distinctness is insufficient.  Generic functor-on-isomorphism-types
packaging, a depth-two finite graph, and elementary fibres are below the
nonnegotiable contribution floor and sit near P109's functorial
image/filtration territory.  Decision: **KILL**, retain only as a negative
control or an example in the kill ledger.  There is no Stage-2 theorem
contract to freeze.

## Root `X01`: kill by direct normal form and historical firewall

Let `I_N=x F_q[x]/(x^N)`, let `F(f)=f^p`, and set `T=I+F`.  After restriction
of scalars, `I_N` is a finite-dimensional `F_p`-vector space, `F` is a
nilpotent `F_p`-linear operator, and `T` is an ordinary unipotent linear
permutation.  The proposed proof is precisely the standard calculation

```text
T^t-I = F^(p^r) U(F),
r=v_p(t),  U(0) != 0,
```

followed by kernel dimension, consecutive fixed-stratum subtraction, and
division by the exact period.  The truncated-polynomial basis only makes the
kernel dimensions easy to write down.

### Exact zero-credit subtraction

All of the advertised package is zero credit:

1. Frobenius additivity and nilpotence on the truncated ideal;
2. restriction of scalars to an `F_p`-linear map;
3. `I+nilpotent` being a unipotent permutation;
4. the characteristic-`p` binomial identity and the `p`-power order bound;
5. fixed counts obtained from `ker F^s`;
6. exact-period and cycle counts by subtraction/division; and
7. the finite Artin--Mazur zeta product assembled from that cycle list.

No separate truncated-ring invariant survives: the formula merely inserts
the explicit Frobenius index chains into generic unipotent-linear theory.

### Decisive internal collisions

The historical collision is stronger than a keyword resemblance.

- `docs/papers97_101_sequence/phase1/CANDIDATE_POOL_AND_KILL_LEDGER.md`
  already records **"Frobenius--Jordan and linear CA candidates"** as
  `KILL_OWNER_AND_INTERNAL` because general finite-linear functional graphs
  own the engine.
- P99 already occupies a unipotent action with complete fixed/cycle/zeta and
  prime-power staircase outputs.  Changing the carrier from sublattices to a
  truncated polynomial vector space does not create a new proof engine.
- `docs/papers112_116_sequence/scouting/ROOT_SCOUT.md` already kills the bare
  truncated-ring Frobenius as a weaker same-family candidate, while P115
  occupies bounded coefficient-index chains, Frobenius coordinates,
  fixed/cycle/zeta data, and complete component language.

Adding the identity changes absorption into a permutation, but it does not
defeat these owner and mechanism exclusions.  Decision: **KILL** and preserve
the 145,716-assertion spike only as a verified negative result.  No paper
number, reserve slot, or replacement theorem contract is justified.

## Selector handoff

Only `A02` may enter the global finalist comparison, and even it enters with a
low novelty ceiling and mandatory proof repairs.  `M01` and `X01` must remain
in the permanent kill ledger so that their attractive closed formulas are not
reintroduced later under a changed carrier description.  The global selector
should prefer a different system if another lane offers comparable theorem
mass with a less elementary owner subtraction.
