# Stochastic Phase-2b breadth scout

> **HISTORICAL SCREENING RECORD.**  The later direct-owner gate found that
> B03/P121 is the Disanto--Fuchs--Paningbatan--Rosenberg Yule
> root-configuration statistic after `X_n=R_n+1`.  It also assigned the
> fixed-tree marker to Andriantiana--Wagner--Wang and the caterpillar
> probability to Chang--Fuchs/Rosenberg.  Therefore the ranking language and
> B03 residual package below are superseded.  The final residual is only the
> Yule-averaged marked transform and the strict `r>=3` pole/radius
> continuation; external status remains HOLD.

**Status:** exactly twelve new literal systems screened; one conditional
promotion, one reserve, ten kills; no paper number frozen  
**External status:** `HOLD_EXTERNAL`  
**Date of bounded search:** 2026-08-30  
**Write boundary:** this report and the three unique
`proof_spikes/stoch_phase2b_*.py` pilots only. No shared ledger or Git state was
changed.

This lane replaces the killed S01/S02/S07/S10 package. It is an intake and
falsification record, not a novelty, priority, or ownership certificate.
Failure to find a direct owner below means only a bounded no-hit.

## Executive decision

The hard intake filter removed reset/regeneration, hidden finite-state
wrappers, random-walk or word-statistic relabelings, generic “make a rewrite
random” constructions, tandem/RSK, affine or valuation recodings, and every
P1--P116 engine. Exact finite-time formulas, not PF pressure or LLN/CLT, were
required before a system could survive even provisionally.

The ranking is:

| rank | ID | literal system | early infinite-family signal | decision |
|---:|---|---|---|---|
| 1 | B03 | adjacent coalescence under `x star y=xy+1` | marked antichain OGF, strict moment-radius cascade, tangent mean, minimum atom | **CONDITIONAL PROMOTE** |
| 2 | B02 | random greedy matching on the staircase Ferrers graph | perfect atom `2^n/(n+1)!` | **RESERVE** |
| 3 | B01 | parallel uncrossing of a maximally crossing chord matching | exact parity interval; owner-subtracted staircase extreme atom | **KILL AT PRECOMMITTED WHOLE-LAW GATE** |
| 4 | B04 | uniform Tamari-cover climb between the combs | exact classical chain-length interval; weighted edge atoms | **KILL** |
| 5 | B05 | uniform vertex elimination with fill on `K_{a,b}` | complete fill law from the first monochromatic run | **KILL** |
| 6 | B06 | Karger contraction on the cycle `C_n` | fixed-cut survival `2/[n(n-1)]` | **KILL** |
| 7 | B07 | Rémy growth of plane full binary trees | uniform Catalan terminal law | **KILL** |
| 8 | B08 | random Apollonian face subdivision | exact corner-face expectation product | **KILL** |
| 9 | B09 | uniform-attachment recursive-tree growth | root-degree PGF `(z)_(n-1)/(n-1)!` | **KILL** |
| 10 | B10 | opposite-colour Friedman urn | exact first- and second-moment recurrences | **KILL** |
| 11 | B11 | random greedy dimer matching on a path | exact all-`n` perfect-coverage Riccati recurrence | **KILL** |
| 12 | B12 | adjacent interval coalescence with reward `uv` | pathwise reward `binom(n,2)` | **KILL** |

Only B03 is conditionally promoted, and only to a second-route proof plus
direct-owner gate after a separate hostile score of `8.5/10`. B02 is kept as a
fallback, not promoted. B01 is killed by its own precommitted rule: its whole
absorption law did not compress beyond exponential state DP, and the only
closed extreme atom is classical reduced-word/tableau territory. Familiar
engines exposed by B03 and B07--B11 receive no credit merely because their
literal carrier looks different.

## Firewall and intake method

The following were rejected before numbering and therefore are not among the
twelve systems: random transposition fragmentation, random inversion sorting,
Bernoulli deletion--contraction, random Kauffman smoothing, sandpile/chip
firing, gcd--lcm smoothing, finite semigroup walks, and iid matrix-word
statistics. They respectively violate the random-walk, generic probabilistic
rewrite, occupied sandpile, semilattice/P100, finite-memory, or P99/P111/P116
firewalls.

For each admitted system below the record fixes:

1. the literal phase and update, including orientation;
2. a size family and an exact infinite-family signal;
3. the nearest external owner and internal subtraction;
4. two proof routes that do not merely rename the same DP; and
5. a precommitted kill condition.

Reset time, regeneration, a finite transfer matrix, stationary laws, PF
pressure, and generic LLN/CLT/LDP remain supporting machinery only. None is
proposed as a contribution.

## Exact pilots for the top three

All probabilities were computed with `fractions.Fraction`; there is no Monte
Carlo and no floating-point comparison.

| script | exact assertions | cached states | scope and killed guess |
|---|---:|---:|---|
| `stoch_phase2b_chord_uncrossing.py` | 215,862 | 18,775 joint-law + 625 unit-drop | `n<=7`; full parity support and extreme atom; uniform terminal law killed |
| `stoch_phase2b_ferrers_greedy.py` | 463,277 | 33,657 | `n<=10`; full size support and perfect atom; uniform size law killed |
| `stoch_phase2b_product_plus_one.py` | 1,694 | 8,113 literal states | boundary permutations/marked polynomials `n<=9`; literal moments `r<=6,n<=12`; both hierarchies through `n<=60`; deterministic output killed |

Total: **680,833 exact assertions**. Representative exact sentinels are

```text
B01, n=4: P(T=2,4,6) = 8/15, 4/9, 1/45.
B02, n=4: P(|M|=2,3,4) = 31/300, 229/300, 2/15.
B03, n=4: P(V=4,5) = 2/3, 1/3; E[V_10] = 9491/270.
```

The computations certify the displayed bounds only. Every unproved
all-parameter identification is explicitly labelled a theorem contract or a
conjecture below.

## The twelve literal systems

### B01. Parallel chord uncrossing — KILL AT WHOLE-LAW GATE

- **Phase and update.** Put endpoints `0,1,...,2n-1` clockwise on a circle.
  A state is a perfect matching. For crossing chords `(a,c),(b,d)` with
  `a<b<c<d`, choose one crossing occurrence uniformly and replace those two
  chords by the *parallel* smoothing `(a,b),(c,d)`. Start from
  `M_n={(i,i+n):0<=i<n}` and stop when no chords cross. This orientation is
  fixed; the nested smoothing `(a,d),(b,c)` is not allowed.
- **Exact infinite-family signal.** Let `C_n=binom(n,2)`. Every move lowers the
  crossing number by a positive odd integer. At most one original diameter
  can remain unchanged in a noncrossing terminal matching, while a move
  changes two chords. Hence

  ```text
  floor(n/2) <= T_n <= C_n,       T_n == C_n (mod 2).
  ```

  Pairing the first two remaining diameters at each short step realizes the
  lower endpoint; the explicit “bubble” smoothing in the pilot realizes the
  upper endpoint. Recursive splicing gives the theorem contract

  ```text
  supp(T_n)={floor(n/2), floor(n/2)+2, ..., C_n}.
  ```

  It is verified through `n=7`. Unit-drop histories have the exact checked
  count

  ```text
  # longest histories = C_n! / product_{j=2}^{n-1}(2j-1)!!,
  P(T_n=C_n) = 1 / product_{j=2}^{n-1}(2j-1)!!.
  ```

  The pilot independently counts unit-drop histories and checks the
  staircase hook product. It also finds `1,1,3,5,18,37,143` reachable terminal
  matchings for `n=1,...,7`; their probabilities are not uniform.
- **Owner and internal subtraction.** Crossing resolution itself is directly
  owned by Kim--Rhoades, whose projection repeatedly resolves chord/set-
  partition crossings ([IMRN 2023, DOI 10.1093/imrn/rnac110](https://doi.org/10.1093/imrn/rnac110)).
  The longest-history count is also zero credit: it is the classical count of
  reduced words of the longest permutation by staircase tableaux, owned by
  Stanley ([European J. Combin. 1984, DOI 10.1016/S0195-6698(84)80039-6](https://doi.org/10.1016/S0195-6698(84)80039-6))
  and the Edelman--Greene bijection. Acan owns random chord diagrams and their
  growth models ([Discrete Math. 2017, DOI 10.1016/j.disc.2016.11.004](https://doi.org/10.1016/j.disc.2016.11.004)).
  A current direct neighbor is Gross--Šarković's genus-preserving chord-swap
  chain ([arXiv:2607.02410](https://arxiv.org/abs/2607.02410)), but that chain
  is nonabsorbing and does not use this one-sided smoothing. The residual is
  only the **full absorbing-time/terminal law for this fixed maximally
  crossing family**, beyond the classical extreme subclass. No reset,
  finite-memory, sorting-network, or generic skein statement may be claimed.
- **Two materially distinct routes.** (A) Encode arbitrary smoothings by a
  laminar interval forest and derive a recursive PGF by its first outer split;
  this route must handle large odd crossing drops. (B) Use the crossing-number
  filtration and a Temperley--Lieb/skein projection with a time marker, then
  extract coefficients by triangular algebra. The reduced-word/tableau route
  proves only the longest atom and is owner subtraction, not one of the two
  residual routes.
- **Kill condition.** Met. The pilot did not give a polynomial-size recurrence
  or coefficient formula for the *whole* `T_n` law (or a comparably strong
  terminal statistic). The double-factorial atom is already a classical
  staircase reduced-word/tableau count and cannot support a paper. The checked
  parity interval remains a useful conjectural signal, not a substitute for the
  precommitted whole-law requirement.

### B02. Staircase-Ferrers random greedy matching — RESERVE

- **Phase and update.** The bipartite graph has rows and columns
  `0,...,n-1` and edge set `E_n={(i,j):j<=i}`. Choose a current edge uniformly,
  put it in the matching, and delete its row, its column, and all incident
  edges. Stop when the board is empty.
- **Exact infinite-family signal.** The terminal size has support

  ```text
  {ceil(n/2), ceil(n/2)+1, ..., n}.
  ```

  The staircase graph has a unique perfect matching, its diagonal. Conditional
  on having selected diagonals only, `r` surviving indices induce exactly
  `r(r+1)/2` active edges, of which `r` are safe. Therefore

  ```text
  P(perfect) = product_{r=n,...,1} 2/(r+1) = 2^n/(n+1)!.
  ```

  This identity and the full support are verified exactly through `n=10`.
- **Owner and internal subtraction.** Choosing a uniform surviving edge is
  precisely randomized greedy matching as studied by Dyer--Frieze
  ([Random Structures & Algorithms 1991, DOI 10.1002/rsa.3240020104](https://doi.org/10.1002/rsa.3240020104))
  and in graph-RSA form by Pippenger
  ([SIAM J. Discrete Math. 2005, DOI 10.1137/0402034](https://doi.org/10.1137/0402034)).
  The 2025--2026 search also reached the random greedy process in
  *Counting Perfect Matchings in Dirac Hypergraphs*
  ([Combinatorica 2026, DOI 10.1007/s00493-025-00194-8](https://doi.org/10.1007/s00493-025-00194-8)).
  No direct exact staircase-board law was found, but this is only a bounded
  no-hit. The generic algorithm, maximal-matching bounds, unique diagonal, and
  the single perfect atom are all zero credit.
- **Two materially distinct routes.** (A) Ferrers-board deletion and rook-
  polynomial/continued-fraction recurrences for the entire terminal-size PGF.
  (B) Assign iid exponential priorities to edges and analyze the induced
  diagonal hazard through order statistics and inclusion--exclusion.
- **Kill condition.** Promote only if the whole size PGF, or at least a new
  two-parameter `a x b` staircase/trapezoid law, compresses beyond exponential
  board DP. Kill if only `2^n/(n+1)!` survives. B11 below is the same generic
  engine and cannot advance alongside B02.

### B03. Adjacent `xy+1` coalescence — CONDITIONAL PROMOTE

- **Phase and update.** Start with the composition `(1,...,1)` of length `n`.
  At each step choose one of the current adjacent boundaries uniformly and
  replace adjacent values `x,y` by `x star y=xy+1`. Stop at the scalar `V_n`.
- **Exact infinite-family signal.** Every current boundary is an original
  boundary that has not yet been deleted, so the deletion order is a uniform
  permutation. Its max-Cartesian tree has the random-BST root-split law

  ```text
  V_1=1,
  V_n =d 1 + V_I V'_(n-I),   I uniform on {1,...,n-1}.
  ```

  Thus the complete finite law satisfies

  ```text
  p_n(v)=(1/(n-1))*sum_i sum_(1+ab=v) p_i(a)p_(n-i)(b).
  ```

  There is also a closed marked ideal theorem. If
  `P_T(u)=sum_C u^|C|` over antichains of internal nodes, including the empty
  antichain, then `P_T=u+P_LP_R`. For
  `a_n(u)=E[P_T(u)]` and `A(z,u)=sum_(n>=1)a_n(u)z^(n-1)`,

  ```text
  A_z=A^2+u/(1-z)^2,  A(0,u)=1.
  ```

  With `w=1-z`, `Delta=sqrt(1-4u)`, and
  `alpha_+=(1+Delta)/2`, `alpha_-=(1-Delta)/2`, set

  ```text
  y=(alpha_+ w^alpha_+ - alpha_- w^alpha_-)/Delta.
  ```

  Then `A=y_w/y`; the apparent singularity at `u=1/4` is removable, with
  `y=sqrt(w)(1+(1/2)log w)`. Thus every expected `k`-antichain count is
  encoded exactly, and `u=1` gives `E[V_n]`. This marked formula is still
  derived by the root-split route and is not counted as an independent proof.

  Put `m_(r,n)=E[V_n^r]` and
  `M_r(z)=sum_(n>=1)m_(r,n)z^(n-1)`. Binomial expansion gives the closed
  triangular hierarchy

  ```text
  M_0=(1-z)^(-1),
  M_r'=sum_(k=0)^r binom(r,k) M_k^2,  M_r(0)=1.
  ```

  This hierarchy has a genuine all-order consequence. Set `rho_0=1`,
  `G_r=sum_(k<r)binom(r,k)M_k^2`, and `M_r=-u_r'/u_r`, so

  ```text
  u_r''+G_r u_r=0,  u_r(0)=1, u_r'(0)=-1.
  ```

  If `rho_r` is the first positive zero of `u_r`, then

  ```text
  1=rho_0>rho_1>rho_2>...>0,
  radius(M_r)=rho_r,
  M_r(z)=1/(rho_r-z)+O(1),
  limsup_n E[V_n^r]^(1/n)=rho_r^(-1).
  ```

  Indeed, inductively
  `G_r(x)=r/(rho_(r-1)-x)^2+O((rho_(r-1)-x)^(-1))`.
  Euler/Sturm comparison forces a zero strictly before `rho_(r-1)`; it is
  simple by ODE uniqueness. Nonnegative coefficients and Pringsheim's theorem
  then identify that first positive pole with the complex convergence radius.
  No uniqueness of the dominant complex singularity or full coefficient
  asymptotic is claimed for `r>=2`.

  In particular, if `M=M_1`, then

  ```text
  m_1=1,
  m_n=1+(1/(n-1))*sum_{k=1}^{n-1} m_k m_{n-k}.
  ```

  With `M(z)=sum_{n>=1}m_n z^(n-1)`, this is exactly

  ```text
  M'=M^2+(1-z)^(-2),  M(0)=1.
  ```

  Setting `M=-u'/u` gives `u''+u/(1-z)^2=0`, with

  ```text
  u=sqrt(1-z)*[
      cos((sqrt(3)/2)log(1-z))
      +(1/sqrt(3))sin((sqrt(3)/2)log(1-z))].
  ```

  The elementary solution is

  ```text
  M=(1/w)[1/2-(sqrt(3)/2)*tan((sqrt(3)/2)log(w)-pi/6)], w=1-z.
  ```

  In `|z|<1`, `Re(w)>0`; every cosine zero forces `log(w)` real. The zeros
  are

  ```text
  w_k=exp((2/sqrt(3))*(2*pi/3+k*pi)).
  ```

  Therefore `k=-1` gives the unique dominant simple pole
  `rho=1-exp(-2*pi/(3*sqrt(3)))`; all `k<=-2` yield larger positive
  singularities, all `k>=0` have modulus greater than one, and the logarithmic
  branch point is at `z=1`. Locally `M=1/(rho-z)+O(1)`, so

  ```text
  E[V_n] ~ rho^(-n)
  ```

  with leading constant exactly one. Also `xy+1>=x+y`, with equality exactly
  when one factor is one. Hence `V_n>=n`, equality occurs exactly on planar
  comb evaluation trees, and

  ```text
  P(V_n=n)=2^(n-2)/(n-1)!  (n>=2).
  ```

  Literal laws and moments through `n=12`, original-boundary permutations and
  marked antichain polynomials through `n=9`, and both coefficient hierarchies
  through `n=60` agree exactly.
- **Owner and internal subtraction.** The evaluation-tree statistic is the
  number of antichains of internal nodes (including the empty antichain), since
  `A(T)=1+A(T_L)A(T_R)`. Deterministic subtree/ideal enumeration is classical:
  Ruskey
  ([SIAM J. Comput. 1981](https://doi.org/10.1137/0210011)) and Koda--Ruskey
  ([J. Algorithms 1993](https://doi.org/10.1006/jagm.1993.1044)) receive full
  credit. Klazar studies average antichains on rooted plane trees
  ([EJC 1997](https://doi.org/10.1006/eujc.1995.0095)); Janson studies ideals
  for the uniform/Catalan random-tree model
  ([2002 chapter](https://doi.org/10.1007/978-3-0348-8211-8_24)); and
  Flajolet--Gourdon--Martinez own the random-BST split, Riccati-linearization,
  and analytic framework
  ([RSA 1997](https://doi.org/10.1002/%28SICI%291098-2418%28199710%2911%3A3%3C223%3A%3AAID-RSA2%3E3.0.CO%3B2-2)).
  Martinez--Panholzer--Prodinger already use differential generating functions
  for all moments of classical BST parameters
  ([EJC 1998](https://doi.org/10.37236/1358)).
  All of those objects and engines are zero credit. Exact-formula, sequence,
  antichain/pruning, random-BST, and 2025--2026 searches found no source giving
  this tangent OGF, growth constant, all-moment hierarchy, or minimum atom in
  the random-permutation BST model; this is only a bounded no-hit. The separate
  hostile gate scores the remaining pair-specific package `8.5/10`.
- **Two materially distinct routes.** (A) Temporal/analytic: uniform deletion
  order, random-BST splitting, moment Riccati hierarchy, Euler linearization,
  and zero analysis. (B) Combinatorial: regard boundary permutations as heap
  labelings of Cartesian trees and enumerate pairs `(heap labeling, forest
  ideal)` directly; the comb labelings already give the minimum atom. Route B
  must recover the mean OGF or coefficients without simply restating the root-
  split conditioning before a paper can freeze.
- **Kill condition.** Conditional survival only. Kill on a direct random-BST
  antichain/ideal source containing the tangent OGF or equivalent constant.
  Also kill if the heap-labeling/ideal route collapses to the same root-split
  recurrence and no additional marked or higher-moment theorem appears.

### B04. Uniform Tamari-cover climb — KILL

- **Phase and update.** On plane binary trees with `n` leaves, start at the
  left comb. At every step choose uniformly one available right rotation
  `(xy)z -> x(yz)`, and stop at the right comb.
- **Exact infinite-family signal.** The absorption time is the length of a
  maximal chain and ranges from `n-2` to `binom(n-1,2)`. A small exact DP
  through `n=10` suggested endpoint weights `1/(n-2)!` and
  `2^(-binom(n-2,2))` for the chosen orientation.
- **Owner and internal subtraction.** Nelson directly owns the chain-length
  interval, tableau encoding, and recursions for fixed excess length
  ([arXiv:1709.02987](https://arxiv.org/abs/1709.02987)); Dahlberg--Fishel
  extend maximal-chain methods to graph-associahedral lattices
  ([arXiv:2409.13898](https://arxiv.org/abs/2409.13898)). Defant--Li already
  study stochastic Tamari-lattice absorption under the different Ungarian
  transition rule ([arXiv:2301.08206](https://arxiv.org/abs/2301.08206)). The
  remaining uniform-one-cover weights are too narrow.
- **Two materially distinct routes.** Tamari tableaux/rotation posets; or a
  recursive decomposition at the root edge with harmonic hitting weights.
- **Kill condition.** Met: the phase object, temporal observable, support,
  and both proof routes are already owner-dense; two endpoint probabilities
  do not clear the owner subtraction.

### B05. Random fill under elimination of `K_{a,b}` — KILL

- **Phase and update.** Start from `K_{a,b}`. Uniformly choose a remaining
  vertex, make its current neighbors a clique, record the number of new fill
  edges, and delete the vertex. Continue until empty.
- **Exact infinite-family signal.** If the elimination order begins with
  exactly `r<a` vertices of side `A` and then a `B`, then

  ```text
  F=binom(b,2)+binom(a-r,2),
  P(initial run A^r B)=(a)_r b/(a+b)_(r+1).
  ```

  If all `A` vertices occur first, `F=binom(b,2)` with probability
  `1/binom(a+b,a)`; the symmetric `B` formulas complete the exact law.
- **Owner and internal subtraction.** Graph elimination/fill is classical
  sparse-Cholesky machinery; see Heggernes--Eisenstat--Kumfert--Pothen
  ([DOI 10.2172/15002765](https://doi.org/10.2172/15002765)). Here the whole
  stochastic statistic collapses to the first monochromatic run of a uniform
  permutation. The graph carrier contributes no new dynamics.
- **Two materially distinct routes.** Elimination-graph clique completion;
  or negative-hypergeometric enumeration of the first colour run.
- **Kill condition.** Met: exact solvability is precisely the collapse to a
  one-run permutation statistic.

### B06. Karger contraction on a cycle — KILL

- **Phase and update.** On the cycle multigraph `C_n`, select a current edge
  uniformly with multiplicity and contract it; remove loops and stop at two
  supervertices. Fix in advance a two-edge minimum cut.
- **Exact infinite-family signal.** Conditional on its survival at `m`
  vertices, `m-2` of the `m` edges are safe, so

  ```text
  P(the fixed cut survives)=product_{m=3}^n (m-2)/m=2/[n(n-1)].
  ```

- **Owner and internal subtraction.** This is the original random contraction
  algorithm, not a new cocycle; Karger's thesis gives the contraction method
  and its `Omega(n^-2)` fixed-min-cut survival analysis
  ([official MIT PDF](https://people.csail.mit.edu/karger/Papers/thesis.pdf)).
  The clock is deterministically `n-2`.
- **Two materially distinct routes.** The conditional hazard telescopes; or
  expose a uniform order of the original cycle edges and require the two cut
  edges to be the last two relevant edges.
- **Kill condition.** Met by exact direct ownership and deterministic time.

### B07. Rémy binary-tree growth — KILL

- **Phase and update.** Start from one leaf. With `m` leaves, choose uniformly
  one of the `2m-1` vertices, replace its rooted subtree by a new parent whose
  children are that subtree and a new leaf, and choose left/right orientation
  fairly.
- **Exact infinite-family signal.** After `n-1` steps every plane full binary
  tree with `n` leaves has probability `1/Catalan_{n-1}`.
- **Owner and internal subtraction.** This is Rémy's algorithm verbatim, with
  uniformity as its principal theorem
  ([RAIRO 19 (1985), EuDML full record](https://eudml.org/doc/92229)). Its
  reverse deletion also sits too near the internal tree/leaf-peeling terrain,
  though the direct external owner already kills it.
- **Two materially distinct routes.** Reverse-pruning double counting of
  histories; or a Catalan-species/generating-tree argument.
- **Kill condition.** Met: both system and exact law have a direct owner, and
  elapsed time is deterministic.

### B08. Random Apollonian face subdivision — KILL

- **Phase and update.** Start from one bounded triangular face. At step `m`,
  choose one of the `2m+1` bounded faces uniformly, insert a vertex in it, and
  join the new vertex to its three corners.
- **Exact infinite-family signal.** For a fixed original corner, let `I_m` be
  its incident active-face count. Then `I_0=1` and

  ```text
  E[I_(m+1)|I_m]=I_m*(1+1/(2m+1)),
  E[I_m]=(2m)!!/(2m-1)!!.
  ```

  The corner degree is `I_m+1`.
- **Owner and internal subtraction.** The literal random Apollonian network
  and its degree laws are established objects; see Zhou--Yan--Wang
  ([Phys. Rev. E 71, DOI 10.1103/PhysRevE.71.046141](https://doi.org/10.1103/PhysRevE.71.046141))
  and the ternary-tree analysis of Darrasse--Soria
  ([DOI 10.46298/dmtcs.3521](https://doi.org/10.46298/dmtcs.3521)). The product
  above is a one-colour projection of their urn structure.
- **Two materially distinct routes.** A triangular Pólya-urn martingale; or
  the dual recursive ternary tree and marked-subtree enumeration.
- **Kill condition.** Met by literal process ownership; neither an exact mean
  nor a repackaged urn limit is residual.

### B09. Uniform-attachment recursive tree — KILL

- **Phase and update.** Begin with root `1`. For `k=2,...,n`, attach vertex
  `k` to a uniformly chosen existing vertex. Observe the final root outdegree
  `D_n`.
- **Exact infinite-family signal.** Root attachments are independent
  Bernoulli variables of parameters `1,1/2,...,1/(n-1)`, hence

  ```text
  E[z^D_n]=product_{j=1}^{n-1}(1+(z-1)/j)
          =z(z+1)...(z+n-2)/(n-1)!,
  P(D_n=r)=|s(n-1,r)|/(n-1)!.
  ```

- **Owner and internal subtraction.** The exact node-outdegree distribution,
  including its Stirling formula, is directly in Javanian--Vahidi-Asl
  ([DOI 10.1007/BF02936077](https://doi.org/10.1007/BF02936077)). A current
  August-2026 neighbor studies new rank/layer statistics rather than this law
  ([arXiv:2608.04303](https://arxiv.org/abs/2608.04303)).
- **Two materially distinct routes.** Independent attachment indicators; or
  the classical permutation-cycle/record bijection for Stirling numbers.
- **Kill condition.** Met: exact law and both interpretations are classical.

### B10. Opposite-colour Friedman urn — KILL

- **Phase and update.** Start with `X_0=a`, `Y_0=b`. Draw a ball uniformly,
  replace it, and add one ball of the opposite colour. Let
  `D_t=X_t-Y_t` and `N=a+b`.
- **Exact infinite-family signal.** Direct conditioning gives

  ```text
  E[D_(t+1)|D_t]=(1-1/(N+t))*D_t,
  E[D_t]=(a-b)(N-1)/(N+t-1),
  E[D_(t+1)^2]=(1-2/(N+t))*E[D_t^2]+1.
  ```

- **Owner and internal subtraction.** This is Bernard Friedman's symmetric
  opposite-reinforcement urn. The literature already gives functional
  equations, moments, martingale limits, and generalizations; a recent
  2026 mixed-model paper explicitly places the Friedman replacement matrix in
  that lineage ([arXiv:2605.26669](https://arxiv.org/abs/2605.26669)). The
  two displayed recurrences are elementary specializations, not residuals.
- **Two materially distinct routes.** Diagonalize the balanced replacement
  matrix and form a martingale; or derive the exact bivariate urn generating
  PDE and differentiate it.
- **Kill condition.** Met by direct model ownership and absence of a
  pair-specific temporal anomaly.

### B11. Random greedy dimers on a path — KILL

- **Phase and update.** On `P_n`, choose a surviving edge uniformly, accept it
  into the matching, delete its endpoints, and recurse on the two remaining
  path intervals.
- **Exact infinite-family signal.** Let `p_m` be the probability of a perfect
  matching on `P_{2m}`. First-edge decomposition gives

  ```text
  p_0=1,
  (2m-1)p_m=sum_{j=0}^{m-1}p_j p_(m-1-j).
  ```

  Thus for `P(x)=sum_{m>=0}p_m x^m`,
  `2xP'=P-1+xP^2`; the first values are
  `1,1,2/3,7/15,34/105`.
- **Owner and internal subtraction.** This is one-dimensional dimer random
  sequential adsorption/random greedy matching, with exact one-dimensional
  kinetics predating and surveyed by Pippenger
  ([DOI 10.1137/0402034](https://doi.org/10.1137/0402034)). It is also the
  same generic random-edge engine as B02, so at most B02 can remain.
- **Two materially distinct routes.** Recursive splitting at the first chosen
  edge; or iid exponential edge priorities and interval RSA.
- **Kill condition.** Met by direct owner and internal B02 engine collision.

### B12. Adjacent interval coalescence with pair reward — KILL

- **Phase and update.** Start from block sizes `(1,...,1)`. Uniformly choose a
  current adjacent boundary, merge blocks of sizes `u,v` into `u+v`, and add
  `uv` to a cumulative reward `R`.
- **Exact infinite-family signal.** Pathwise, for every merge history,

  ```text
  R=binom(n,2).
  ```

  Indeed `Phi=sum_i binom(s_i,2)` increases by exactly `uv` and runs from
  zero to `binom(n,2)`.
- **Owner and internal subtraction.** The same uniform boundary-priority/random
  BST genealogy appears in B03, but here even the observable is a telescoping
  potential. Generic coalescent or additive-functional theory would be
  unnecessary overkill.
- **Two materially distinct routes.** Telescope `Phi`; or charge each
  unordered pair of original atoms at the unique merge where the pair first
  enters one block.
- **Kill condition.** Met: all randomness disappears from both time (`n-1`)
  and reward.

## Bounded primary-owner audit

The search was deliberately current but bounded. Query families included
literal update formulas, synonyms (`parallel smoothing`, `uncrossing`,
`crossing resolution`, `staircase/Ferrers/chain graph greedy matching`,
`xy+1 parenthesization`, `nonassociative adjacent coalescence`), and the same
queries restricted to 2025--2026. Direct neighbors were opened rather than
inferred from snippets.

The strongest owner findings are:

| system | closest direct owner | subtraction consequence |
|---|---|---|
| B01 | Kim--Rhoades crossing resolution; Stanley reduced words; Gross--Šarković 2026 chord chain | smoothing and longest atom are fully subtracted; the required full absorbing-law compression was not obtained, so the candidate is killed |
| B02/B11 | Dyer--Frieze randomized greedy matching; Pippenger graph RSA; 2026 Dirac-hypergraph greedy process | generic process and asymptotics are fully subtracted; only a staircase-specific full exact law could survive |
| B03 | Ruskey and Koda--Ruskey on rooted subtrees/forest ideals; Klazar and Janson on random-tree antichains/ideals; Flajolet--Gourdon--Martinez and Martinez--Panholzer--Prodinger on BST analytic/moment schemes | every carrier and generic engine is subtracted; only this parameter's marked transform, moment-radius cascade, tangent mean, exact pole/residue, and comb atom survive conditionally |
| B12 | random-BST root splitting plus a pathwise telescoping potential | no stochastic residual survives |
| B04 | Nelson maximal Tamari chains; Defant--Li stochastic Tamari chain | chain support/tableaux and lattice absorption are owner-dense |
| B05 | sparse elimination/fill literature | law collapses to a negative-hypergeometric first run |
| B06 | Karger random contraction | literal process and survival product directly owned |
| B07 | Rémy | literal process and uniform law directly owned |
| B08 | random Apollonian-network literature | literal growth and urn/tree routes directly owned |
| B09 | Javanian--Vahidi-Asl | exact Stirling outdegree law directly owned |
| B10 | Friedman urn literature, including 2026 mixed extensions | literal replacement rule and moment machinery directly owned |

No query establishes exhaustiveness or priority. In particular, neither the
B01 nor B03 bounded no-hit is evidence of novelty. Equivalence classes under
chord reflection, endpoint rotation, alternative smoothing conventions,
matching skein modules, and sorting-network encodings have not been exhausted;
nor have all vocabularies around BST prunings, cuts, initial subtrees, ideals,
and heap-labelled Cartesian trees.

## Falsification and collision ledger

1. **B01 uniform terminal measure:** false already at `n=4`.
2. **B02 uniform matching-size law:** false at `n=4`.
3. **B03 deterministic evaluation:** false at `n=4`, with masses `2/3,1/3`;
   this falsification led to the exact distribution and moment hierarchy.
4. **B01 longest atom as residual novelty:** killed by the
   Stanley/Edelman--Greene reduced-word owner.
5. **B04 chain-support novelty:** killed by Nelson's maximal-chain work.
6. **B05 nonlocal fill dynamics:** killed; all fill is decided by the first
   colour run.
7. **B06/B07/B08/B09/B10 literal novelty:** each killed by a direct named
   process owner.
8. **B11 as a second greedy lane:** killed by both RSA ownership and collision
   with B02.
9. **B12 random reward law:** killed by a pathwise potential identity.

## Handoff contracts

### Conditional promotion: B03 only

Proceed to one hard combinatorial/owner pilot, not a paper assignment. It must
deliver all of the following before any freeze:

1. a direct heap-labeling/forest-ideal enumeration that recovers the mean OGF
   or its coefficients without merely repeating conditional root splitting;
2. a citation-neighborhood audit around Ruskey, Koda--Ruskey, Klazar, Janson,
   and random-BST parameter analyses;
3. an explicit zero-credit subtraction of the random-BST genealogy,
   deterministic antichain/ideal interpretation, and generic Riccati method;
4. retention of the strict moment-radius/unit-pole theorem at exactly its
   proved strength--only an exact `limsup` for `r>=2`, unless a uniqueness
   theorem justifies full coefficient asymptotics; and
5. a direct combinatorial coefficient interpretation of the proved marked
   antichain transform; the transform itself does not count as Route B.

Kill on a direct random-BST antichain formula owner, or if the second route
collapses to the same split recurrence without an additional structural
output.

### Reserve: B02 only

Do not promote on the perfect atom. Reopen only if a two-parameter
staircase/trapezoid PGF or a coefficient formula for the whole terminal-size
law appears, together with a direct Ferrers-board owner clearance. Otherwise
kill behind B03.

### Closed lane: B01

Do not reopen on the parity support or longest atom. Its precommitted
whole-absorption-law gate failed, while the extreme atom is classical
Stanley/Edelman--Greene territory. Reopening requires a genuinely compressed
whole law and a fresh owner gate, not additional finite-state data.

### Final Phase-2b disposition

```text
PROMOTE (conditional hard proof/owner gate): B03
RESERVE:                                  B02
KILL:                                     B01, B04--B12
EXTERNAL:                                 HOLD
```
