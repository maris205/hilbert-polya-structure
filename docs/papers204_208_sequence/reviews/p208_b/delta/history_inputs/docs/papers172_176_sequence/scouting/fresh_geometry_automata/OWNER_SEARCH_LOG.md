# Bounded primary-source owner search

**Search date:** 2026-09-03 UTC  
**Lifecycle:** `HOLD_EXTERNAL`  
**Rule:** a query non-hit is never novelty, priority, ownership, freedom to
operate, or release evidence.

## 1. Strong-signal search vocabulary

The following literal and structural queries were run in multiple variants:

```text
"minimum pivot" Mobius transformation subset projective line finite field
"1/(x-a)" subset projective line finite field
state-dependent Mobius transformation finite field dynamical system subset
projective line subset normalization Mobius smallest point
PGL(2,q) action k-subsets projective line
"(S-a)^-1" finite field subset
adaptive Mobius transformation finite field subsets dynamics
set partition occurrence rank tableau columns fibre
set partitions tableaux subspace profiles Prasad Ram
```

Additional owner queries covered prescribed-outcome parking, BFS-canonical
accessible automata, doubly lexical matrices, RSK involutions, Schubert pivot
cells, and matching/Dyck signatures.

After Hostile Review B, the bounded audit was reopened with the additional
query vocabulary

```text
minimal canonical image permutation group subset
canonizing element ordered finite set group action
dynamic ordering canonical image finite group
```

This located Christopher Jefferson, Eliza Jonauskyte, Markus Pfeiffer, and
Rebecca Waldecker, *Minimal and Canonical Images*, Journal of Algebra 521
(2019), 481--506, DOI `10.1016/j.jalgebra.2018.11.009` (also
arXiv:1703.00197).  That work owns minimal/canonical images and canonizing
elements for ordered group actions.  Those notions receive zero credit in
P174.  The P174 map is not a canonical-image construction: it applies one
state-selected translation followed by inversion, is not constant on group
orbits, and is analysed through a two-step containment tower and a
target-dependent pivot interval.  This subtraction closes the Review-B
query-vocabulary gap; it is not positive novelty evidence.

## 2. Decisive direct owner for `D01_ORT`

Amritanshu Prasad and Samrith Ram,
[*Set partitions, tableaux, and subspace profiles under regular diagonal
matrices*](https://doi.org/10.1016/j.ejc.2024.104060), European Journal of
Combinatorics 124 (2025), 104060; accessible
[FPSAC text](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2022/35.pdf).

The source was checked at the theorem level:

- Definition 2.1: list old blocks as increasing rows, sort and top-justify
  columns -- exactly the tableau whose columns are the `D01` output blocks;
- Theorem 2.8: complete product formula `c(T)` for every tableau fibre;
- Theorem 3.4: interlacing-marked `q`-enumerator of that fibre;
- Theorem 4.4: the fixed-pivot RREF/Schubert-cell count also used by `D07`.

Disposition: all static image/fibre/marked content receives zero credit.
Tableau transposition supplies only a shallow temporal wrapper.  `D01` is a
hard direct-owner kill, and `D07` is independently a direct Schubert-cell
kill.

## 3. `D02_MPM`: adjacent owners and literal non-hit

The bounded search found no source stating the state-dependent rule

```text
S -> {1/(x-min(S intersect F_p)) : x in S}
```

on fixed-size projective-line subsets, nor its threshold fibre polynomial.
That sentence is a search report only, not evidence of novelty.

Adjacent primary sources were subtracted:

- E. H. El Abdalaoui and I. E. Shparlinski,
  [*Disjointness of the Möbius Transformation and Möbius
  Function*](https://arxiv.org/abs/1711.11062), studies trajectories of one
  **fixed** fractional-linear map over `F_p`.  Fixed-map period/spectral
  language is zero credit here.
- P. Tricot,
  [*On 3-designs from PGL(2,q)*](https://arxiv.org/abs/2408.14714), starts
  from the 3-transitive action of `PGL(2,q)` on projective-line `k`-subsets
  and analyses block orbits/stabilisers.  Ordinary group-action and subset
  orbit facts are zero credit.
- P. Aluffi and C. Faber,
  [*Linear orbits of d-tuples of points in
  P^1*](https://arxiv.org/abs/alg-geom/9205005), owns the general
  projective-configuration orbit setting.  Configuration normalisation and
  orbit-closure vocabulary are zero credit.
- Internal P132 scouts already kill a fixed order-three `PGL_2` action, and
  P168 owns inverse-span subspace dynamics after inverse-subspace
  classification.  More importantly, the P166 `AQN` hostile gate kills an
  adaptive quotient-normalisation map even though it has an exact recurrent
  action and marked fibres: the state-selected section plus classical group
  action was theorem-thin after owner subtraction.  Thus the generic facts
  that inversion is projective and involutive, and that a state-selected
  normalisation can expose it, are all zero credit here.

Residual under test: the current subset chooses its own translation pivot;
the containment flag `infinity`, then `{0,infinity}`, gives the sharp clock;
and modular wraparound makes the possible pivots an exact target-dependent
initial interval.  AQN's constant-size translation-orbit fibres do not prove
that interval law, so this conjunction did not completely transfer from the
sources or internal engines inspected.  Because the clock is only two, the
coordinate order is artificial, and the architecture is close to AQN, the
status is the lane's unique `PROVISIONAL_AMBER`, not green or owner-cleared.

## 4. Direct/static owners for killed controls

| rows | primary or authoritative source | subtraction |
|---|---|---|
| `D05_CPA` | A. G. Konheim and B. Weiss, [*An Occupancy Discipline and Applications*](https://doi.org/10.1137/0114101), SIAM J. Appl. Math. 14 (1966), 1266--1274; modern parking outcome-map work includes [Harris et al.](https://arxiv.org/abs/2207.13041) | linear/cyclic probing and prescribed parking outcomes are direct owner territory; the one-step retraction is not retained |
| `D10_BCA` | M. Almeida, N. Moreira, R. Reis, [*Enumeration and Generation of Initially Connected Deterministic Finite Automata*](https://web.fc.up.pt/dcc/Pubs/TReports/TR06/dcc-2006-07.pdf) | defines the unique alphabet-ordered BFS state labelling/canonical string used literally by `D10` |
| `D11_DLX` | A. Lubiw, [*Doubly Lexical Orderings of Matrices*](https://doi.org/10.1137/0216057), SIAM J. Comput. 16 (1987), 854--879 | doubly lexical matrix ordering and its algorithms are direct; our alternating-sort functional graph has no retained all-size residual |
| `D14_RDP` | C. Schensted, [*Longest Increasing and Decreasing Subsequences*](https://doi.org/10.4153/CJM-1961-015-3), Canad. J. Math. 13 (1961); J. S. Frame, G. de B. Robinson, R. M. Thrall, [*The Hook Graphs of the Symmetric Group*](https://doi.org/10.4153/CJM-1954-030-1) | RSK sends involutions to equal tableau pairs and the hook formula supplies the displayed fibre; P166 already pre-killed recording-tableau feedback |

The remaining controls are killed by definition-level normal forms,
incomplete theorem silhouettes, or explicit internal transfer; they do not
need a speculative novelty search to be rejected.

## 5. Owner conclusion

- `D01_ORT`: `DIRECT_OWNER_KILL`.
- `D02_MPM`: no literal hit in this bounded vocabulary; adjacent owners
  subtracted; `PROVISIONAL_AMBER / HOLD_EXTERNAL`.
- all other rows: killed before a novelty claim.

No search result authorises circulation or paper allocation.
