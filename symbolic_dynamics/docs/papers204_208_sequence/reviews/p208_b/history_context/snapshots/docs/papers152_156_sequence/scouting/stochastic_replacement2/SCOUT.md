# Stochastic replacement-2 breadth scout — P152–P156 intake

**Audit date:** 2026-09-02 UTC  
**External status:** `HOLD_EXTERNAL`  
**Scope:** ten literal finite stochastic dynamical systems, all distinct from
one another and from the HTM/BTB pair.  This is an internal falsification and
owner-subtraction record.  It makes no novelty, priority, or release claim.

## Outcome first

The replacement pool is deliberately **empty**:

```text
systems tested = 10
paper-sized survivors = 0
kills = 10
verifier = PASS, 38,026 exact assertions
```

This is the correct high-threshold outcome.  Six candidates have a direct or
nearly direct primary owner of the literal object; two reduce to generic
group/Markov machinery; and two show a real finite anomaly but do not yet have
an all-parameter transform plus a genuinely independent inverse or extremal
axis.  None is promoted merely to replace BTB.

The strongest *experimental* signals were:

1. **RNC:** compatible-diagonal insertion is uniform for quadrilaterals and
   pentagons but becomes nonuniform first at the hexagon, with endpoint masses
   `1/15` and `13/180`.  This is a crisp anomaly, but only a finite dynamic
   program is currently available; its polygon carrier also collides with the
   established P146 lane.
2. **MCA:** random digit-position addition has a complete Fourier convolution
   transform, literal one-layer recovery of its position weights, and universal
   stationary carry tails.  The transform and inverse, however, are immediate
   character theory for a cyclic-group walk, and the inverse is only support
   reading.  The remaining carry statement is a uniform-digit fact, not an
   independent paper-sized axis.
3. **RGE:** every nonzero Schur pivot lowers binary rank by exactly one, while
   same-rank matrices already have different pivot-history counts.  Thus rank
   gives a sharp deterministic clock but not the history law.  No closed
   full-parameter history transform emerged.

Those signals are recorded for future search, but all three remain `KILL` in
this gate.  A bounded source-search non-hit is never used as novelty evidence.

## Collision firewall

- No candidate is a generic first-passage walk, urn/Johnson chain, random-scan
  wrapper, meet process on a tree, signed-book system, graph deletion process,
  or vertex/edge peeling rule.
- ATF and RNC keep a polygon and modify/add diagonals; neither deletes graph
  vertices or edges.  RNC is nevertheless killed for theorem thinness and the
  occupied internal polygon carrier.
- RAN is growth, not deletion, but its literal process and ternary-tree encoding
  are already externally owned.
- MCA is kept distinct from the classical carries chain: its state is a single
  cyclic counter and its update chooses a digit-position increment.  The
  Diaconis--Fulman carries chain is only a nearest thematic owner; the decisive
  subtraction is generic abelian-group convolution.
- RGE chooses a nonzero algebraic pivot and takes a Schur complement.  It is not
  graph deletion and is not the numerical randomized-pivot rule of the nearest
  sources cited below.

## Breadth table

| ID | literal mechanism | exact pilot | theorem ceiling reached | owner/collision | decision |
|---|---|---|---|---|---|
| ATF | choose a triangulation diagonal uniformly and flip it | Catalan state counts through the octagon; uniform stationary; hexagon two-step return `1/3` | regular reversible chain only | direct triangulation-flip-walk literature | **KILL_DIRECT** |
| RBF | fixed pair/triple-slot commutation-or-braid update on a reduced word for `w_0` | `1,2,16,768` words for `S_2..S_5`; exact uniform stationarity and connectivity | symmetric move graph only | reduced-word move graph is directly owned | **KILL_DIRECT_OBJECT** |
| RAN | choose an active triangular face uniformly and subdivide it into three | ordered ternary states `1,3,12,55,273,1428`; exact hook probability | hook distribution plus pilot area range | literal Random Apollonian Network owner | **KILL_DIRECT** |
| GRS | iid `a`-labels on cards, then stable sort | complete distributions through `n=6`, `a=2,3,4`; `2` then `2` equals `4` | exact rising-sequence law and semigroup | Bayer--Diaconis directly owns law | **KILL_DIRECT** |
| SBS | independently remove one card from each pile with probability `1/2`; removed cards form a new pile | all partitions through `N=8`; exact stationary rational solve | finite stationary linear system only | Popov directly owns literal variant | **KILL_DIRECT** |
| RSK | append an iid uniform letter and row-insert; retain Young shape | hook-content endpoint and Schur transition through `q=4,t=7` | endpoint/transition already classical | O'Connell directly owns Markov shape process | **KILL_DIRECT** |
| MCA | choose digit position `i` with weight `w_i`; add `b^i mod b^h` | exact convolutions for `b<=5,h<=4,t<=5`; carry tails `b^{-ell}` | Fourier transform + trivial one-step inverse | generic cyclic walk; classical carries nearest | **KILL_GENERIC** |
| RGE | choose a nonzero entry of an `F_2` matrix uniformly; take its Schur complement | all square matrices through `3x3`; rank-3 history values `6,9,14,15,20` | deterministic rank clock; no closed history law | classical elimination/pivoting; recent random-pivot neighbours | **KILL_THIN** |
| RNC | add a uniformly chosen compatible polygon diagonal | every triangulation through heptagon; first nonuniformity at hexagon | exact finite path-sum only | static noncrossing owners; internal P146 carrier | **KILL_THIN_INTERNAL** |
| RMI | sample one uniform map `[n]->[n]`; iterate it from a marked point | full census through `n=6`; `(tail,cycle)=(2,2)` count `2160` | exact joint tail-cycle law | Flajolet--Odlyzko direct classical object | **KILL_DIRECT** |

## 1. ATF — associahedron triangulation-flip walk

### Literal update and exact signal

Fix a labelled convex `n`-gon, `n>=4`.  A state is a triangulation `T`.  Choose
one of its `n-3` diagonals uniformly.  The two triangles incident to that
diagonal form a quadrilateral; replace the chosen diagonal by the other
quadrilateral diagonal.

The verifier constructs all triangulations literally and obtains

```text
n                   3   4   5   6   7    8
number of states    1   2   5  14  42  132
```

Every flip has a unique reverse.  Consequently the transition matrix is
symmetric and the uniform law is stationary.  At `n=6`, the probability of
returning in two steps is exactly `1/(n-3)=1/3`.

### Theorem profile and kill

The full graph-resolvent `(I-zP)^{-1}` exists for every finite `n`, but no
carrier-specific closed spectrum, inverse boundary, or sharp observable
extremizer was found in this round.  More decisively, Molloy--Reed--Steiger and
the subsequent flip-walk literature study this literal chain.  Regularity,
uniform stationarity, reversibility, mixing language, and the associahedron
carrier therefore receive zero credit.

**Decision:** `KILL_DIRECT`.  A different observable on this chain would need
an owner audit before re-entry; the chain itself is not a candidate.

## 2. RBF — reduced-word commutation/braid slot walk

### Literal update and exact signal

Let `w_0` be the longest permutation in `S_n`, with reduced-word length
`L=binom(n,2)`.  A scheduler has the `L-1` adjacent pair slots followed by the
`L-2` consecutive triple slots.  Choose one of these `2L-3` slots uniformly.

- At a pair slot, swap `a,b` when `|a-b|>1`; otherwise hold.
- At a triple slot, replace `a,b,a` by `b,a,b` when `|a-b|=1`; otherwise hold.

The fixed scheduler is important: every legal local move has the same reverse
slot, so the kernel is symmetric despite the state-dependent number of legal
moves.  Exact enumeration gives `1,2,16,768` reduced words for `n=2,3,4,5`,
uniform stationarity, and a connected move graph in every nontrivial pilot.

### Theorem profile and kill

Matsumoto connectivity plus symmetry gives an irreducible reversible chain
with uniform stationary law.  That is only one generic axis.  Elder defines
the graph whose vertices are reduced words and whose edges are exactly these
commutation/braid moves; Schilling--Thiéry--White--Williams analyze braid moves
and promotion statistics on the same reduced-word structures.  Adding a lazy
fixed-slot Markov scheduler does not create an independent theorem package.

**Decision:** `KILL_DIRECT_OBJECT`.

## 3. RAN — Random Apollonian face subdivision

### Literal update and exact signal

Start with one active triangular face.  At each step choose an active face
uniformly, insert a new vertex in it, connect the new vertex to the three
corners, retire the chosen face, and declare the three child faces active.
Equivalently, choose one leaf of an ordered full ternary tree uniformly and
replace it by an internal node with three ordered leaf children.

After `m` subdivisions there are `2m+1` active faces.  If `T` is the ordered
ternary tree, let `s(v)` be the number of internal nodes in the subtree rooted
at an internal vertex `v`.  Then the exact pilot verifies

```text
P_m(T) = [m! / product_v s(v)]
         / product_{j=0}^{m-1}(2j+1).
```

The numbers of reachable ordered shapes for `m=1,...,6` are
`1,3,12,55,273,1428`.  At `m=6`, external path length ranges from `32` to `48`.

### Theorem profile and kill

The hook probability gives an exact endpoint axis, and balanced-versus-comb
trees suggest an area extremal axis.  Neither rescues the system: Zhou et al.
introduce the literal Random Apollonian Network rule, and the ordered ternary
increasing-tree history formula is standard growth-tree machinery.  The pilot
area range was not promoted to a new all-parameter theorem after that direct
subtraction.

**Decision:** `KILL_DIRECT`.

## 4. GRS — global Gilbert--Shannon--Reeds inverse riffle

### Literal update and exact signal

For a deck of `n` distinct cards, assign each card an independent uniform label
in `{0,...,a-1}` and stable-sort the deck by label.  If `r(pi)` is the number of
rising sequences of the output permutation, the exact enumeration verifies

```text
P_a(pi) = binom(a+n-r(pi),n) / a^n,
```

and verifies that an `a`-shuffle followed by a `c`-shuffle has the law of an
`ac`-shuffle.  In particular, two binary shuffles equal one `4`-shuffle.  For
`n=6`, a binary shuffle has support size `58`.

### Theorem profile and kill

Bayer and Diaconis give the probability of every arrangement after any number
of riffle shuffles.  Thus the literal update, rising-sequence law, convolution
semigroup, all-time distribution, and mixing consequences are direct-owner
material.

**Decision:** `KILL_DIRECT`.

## 5. SBS — pile-wise stochastic Bulgarian solitaire

### Literal update and exact signal

A state is an integer partition of a fixed number `N` of cards.  Independently
for each nonempty pile, mark its candidate top card with probability `1/2`.
Remove all marked cards, discard empty piles, make the removed cards into one
new pile if nonempty, and sort pile sizes.  The empty choice is a self-loop.

For every partition through `N=8`, the verifier constructs the exact rational
transition row, proves mass conservation, solves the stationary equations over
`Fraction`, checks every stationary equation, and verifies irreducibility and
positive self-loops.  There are 22 states at `N=8`; its largest stationary atom
is

```text
847348748555804736 / 3762626879624873491.
```

### Theorem profile and kill

The finite stationary law has no evident product form in the pilot.  More
importantly, Popov's *Random Bulgarian solitaire* is precisely the process in
which one candidate card per pile is independently selected with fixed
probability.  Finite-state ergodicity and the limit-shape program are therefore
owned.  Eriksson--Jonsson--Sjöstrand provide related card-wise and generalized
variants, reinforcing the crowded owner boundary.

**Decision:** `KILL_DIRECT`.

## 6. RSK — iid-word RSK shape growth

### Literal update and exact signal

Start with the empty semistandard tableau.  At each step sample a uniform
letter from `{1,...,q}`, row-insert it, and retain only the Young shape
`lambda_t`.  For `|lambda|=t`, exact word enumeration verifies

```text
P(lambda_t=lambda)
  = f^lambda s_lambda(1^q) / q^t,

P(lambda -> lambda+box)
  = s_{lambda+box}(1^q) / [q s_lambda(1^q)].
```

Here `f^lambda` is computed by the hook-length formula and `s_lambda(1^q)` by
the hook-content formula.  The check covers `2<=q<=4`, `t<=7`; at `q=4,t=7`
there are 11 shapes.

### Theorem profile and kill

This is an exact endpoint law and exact Markov kernel, but both are classical.
O'Connell's path-transformation/RSK work identifies the shape evolution with a
conditioned walk in the type-A Weyl chamber and supplies the Markov framework.
Hook and Schur formulas receive zero credit; the alphabet is also visible from
the one-step support, so there is no nontrivial inverse axis here.

**Decision:** `KILL_DIRECT`.

## 7. MCA — random digit-position modular addition

### Literal update and exact signal

Fix base `b>=2`, height `h>=1`, and positive rational weights
`w_0,...,w_{h-1}` summing to one.  The state is `X_t in Z/(b^h)Z`.  Independently
choose `I_t=i` with probability `w_i` and set

```text
X_{t+1}=X_t+b^i mod b^h.
```

For a `b^h`-th root of unity `zeta`, character diagonalization gives

```text
E[zeta^(k X_t)]
 = zeta^(k X_0) (sum_i w_i zeta^(k b^i))^t.       (MCA.1)
```

The time-one law assigns mass `w_i` to the distinct increment `b^i`, so all
weights are literally recovered from one layer.  If `w_0>0`, the uniform law
is the unique stationary law.  Under it, the number `C_i` of consecutive
base-`b` digits equal to `b-1` beginning at position `i` satisfies

```text
P(C_i>=ell)=b^(-ell),  1<=ell<=h-i.               (MCA.2)
```

The verifier independently expands all update sequences for `b<=5,h<=4,t<=5`
and matches convolution exactly; it also checks (MCA.2) by a complete census.

### Theorem profile and kill

Despite satisfying the requested words “transform” and “inverse,” this is not
paper-sized.  Formula (MCA.1) is the standard Fourier transform of a random
walk on a finite cyclic group.  Its inverse is simply reading distinct
one-step support weights.  Formula (MCA.2) is the elementary suffix law of a
uniform base-`b` word and does not depend on the weights.  Diaconis--Fulman own
the nearby but different classical carries chain; no same-kernel claim is made
against them.

**Decision:** `KILL_GENERIC`.  Re-entry would require a genuinely coupled
carry observable whose transform and inverse are not immediate character
theory.

## 8. RGE — random nonzero Schur pivot over `F_2`

### Literal update and exact signal

Let `A` be an `m` by `n` binary matrix.  If `A` is nonzero, choose uniformly a
nonzero entry `A_ij=1`, use it as a pivot, and replace `A` by the binary Schur
complement obtained after deleting row `i` and column `j`:

```text
A'_{kl}=A_{kl}+A_{kj}A_{il}  (mod 2),  k!=i,l!=j.
```

Every legal pivot satisfies

```text
rank(A')=rank(A)-1.
```

Hence the absorption time is deterministically `rank(A)`.  If `H(A)` counts
all legal pivot histories, then

```text
H(0)=1,    H(A)=sum_{A_ij=1} H(A^(i,j)).
```

Complete enumeration through `3x3` finds full-rank history counts
`6,9,14,15,20`.  Thus the sharp rank clock does not determine history shape.

### Theorem profile and kill

The deterministic clock is exact but elementary.  The varying same-rank
history counts are a useful warning against an over-lumping theorem, not a
closed transform.  The bounded owner search found classical Gaussian
elimination/pivoting and recent uniformly random pivoting programs, but no
primary source was classified as the exact same finite-field Schur kernel.
That non-hit does not help: after one research round, no full-parameter history
law, inverse theorem, or sharp second-axis extremal was available.

**Decision:** `KILL_THIN`.

## 9. RNC — random compatible noncrossing-diagonal insertion

### Literal update and exact signal

Fix a labelled convex `n`-gon.  Start with no diagonals.  At each step choose
uniformly among all as-yet-unselected diagonals that cross none of the selected
diagonals, and add it.  After `n-3` steps the endpoint is a triangulation.

For a triangulation `T`, the exact endpoint law is the finite path sum

```text
P(T)=sum_{valid orders d_1,...,d_{n-3} of T}
       product_{j=0}^{n-4} 1/c({d_1,...,d_j}),
```

where `c(S)` is the number of diagonals compatible with the partial set `S`.
The verifier constructs the process literally and obtains

```text
n=4:  mass range 1/2 .. 1/2
n=5:  mass range 1/5 .. 1/5
n=6:  mass range 1/15 .. 13/180
n=7:  mass range 1/45 .. 31/1260.
```

Thus the first loss of uniformity is exactly the hexagon boundary.

### Theorem profile and kill

The finite path sum is not an all-parameter closed law.  The first asymmetry is
promising, but no sufficient triangulation statistic, transform, inverse
boundary, or extremizer theorem was found.  Uniform dissections and other
noncrossing configurations are already mature static objects, while the same
convex-polygon/triangulation carrier is occupied internally by P146.  A bounded
search did not locate a direct owner of this exact naïve insertion kernel, but
that non-hit is not positive evidence.

**Decision:** `KILL_THIN_INTERNAL`.

## 10. RMI — orbit of a uniformly random mapping

### Literal update and exact signal

Sample once a uniform function `F:[n]->[n]`, start at a fixed marked point
`X_0=0`, and iterate `X_{t+1}=F(X_t)`.  Let `mu` be the tail length before the
first repeated orbit vertex and `lambda` the eventual cycle length.  Complete
mapping enumeration verifies, for `0<=mu<n` and
`1<=lambda<=n-mu`,

```text
#{F:(tail,cycle)=(mu,lambda)}
  = (n-1)_(mu+lambda-1) n^(n-mu-lambda),          (RMI.1)
```

where `(x)_k` is the falling factorial.  For `n=6`, exactly `2160` of the
`46656` maps have `(mu,lambda)=(2,2)`.

### Theorem profile and kill

Formula (RMI.1) gives a complete joint endpoint/clock law, but random mapping
functional graphs are a classical direct object.  Flajolet--Odlyzko develop a
general framework for roughly twenty random-mapping parameters by generating
functions and singularity analysis.  Orbit-tail/cycle counting and the random
map model therefore receive zero credit.

**Decision:** `KILL_DIRECT`.

## Deterministic evidence and reproducibility

The verifier
[`verify_stochastic_replacement2.py`](verify_stochastic_replacement2.py)
uses only Python's standard library, integers, and `fractions.Fraction`.  It
does not import any earlier scout.  A cold run is

```bash
python3 docs/papers152_156_sequence/scouting/stochastic_replacement2/verify_stochastic_replacement2.py
```

The frozen output is in [`VERIFICATION.txt`](VERIFICATION.txt).  It records
**38,026 exact assertions**, ten systems, zero selected candidates, and a final
`PASS`.  These computations falsify formulas on finite instances; they are not
evidence of novelty and do not replace proofs or source ownership checks.

## Final freeze verdict

```text
STATUS = PASS_EMPTY_POOL
SELECTED = none
EXTERNAL = HOLD_EXTERNAL
```

No candidate in this replacement round clears the two-axis paper threshold.
The correct next action is to keep the stochastic slot empty or begin a new,
mechanistically disjoint breadth round—not to narrow BTB or promote one of the
finite anomalies without a theorem and owner breakthrough.
