# P166 Round-6 open scout

Decision: **KILL_ALL**  
Lifecycle: **HOLD_EXTERNAL**  
Artifact type: exact breadth scout only; no paper number is assigned.

## 1. Gate and method

Six literal maps were written down before inspecting their data.  Each was
then generated exhaustively in a deterministic standard-library verifier.
Promotion required both of the following after source and internal
subtraction:

1. an all-parameter temporal theorem (a closed iterate, sharp clock, or exact
   period/hitting law); and
2. an independent target-resolved inverse, endpoint, image, or structural
   census, not merely a finite dynamic program.

The verifier contains no random choices and does not import any previous
scout.  It closes **405,148 assertions**.  Its complete stdout is frozen in
`CANONICAL.txt`; two fresh runs agreed byte for byte at SHA-256
`aa2093a8298e20dc3f2ad461985b10c6dd099fea700133ca3b9cef9923e47a46`.

## 2. `MPS`: simultaneous maximum-peak shaving

### Literal map

For a Dyck word `w` of semilength `n`, let `H(w)` be its maximum height.  If
`H(w)=1`, fix `w`.  Otherwise simultaneously replace every factor `UD` whose
middle vertex is at height `H(w)` by `DU`.  Distinct highest peaks cannot
overlap, so the update is unambiguous and remains Dyck.

### Exact signal and full raw theorem

For `1<=n<=9` the verifier exhausts all 6,917 paths.  The last three
state/image/maximum-depth triples are

```text
n=7: 429 / 152 / 6
n=8: 1430 / 503 / 7
n=9: 4862 / 1699 / 8.
```

The following raw theorem was independently derived and checked for every
state and every `0<=t<=n` in those boxes.  Put `H=H(w)` and
`L=max(1,H-t)`.  If `h_j` is the original vertex-height sequence, then the
height after `t` updates is

```text
c_L(h_j) = h_j                         if h_j <= L,
           L                           if h_j > L and h_j == L (mod 2),
           L-1                         otherwise.
```

Consequently the unique recurrent state is `(UD)^n`, every orbit is fixed,
the point clock is `H(w)-1`, and the sharp maximum is `n-1`, attained by
`U^nD^n`.

There is also a true every-target all-time inverse formula.  Write
`A_s(r)` for the number of Dyck paths of semilength `s` and height at most
`r`.  Let a nonfixed target `y` have height `L>1`.  Its maximal excursions
above level `L-2` that actually touch level `L` have the unique forms

```text
U (UD)^{s_1} D, ..., U (UD)^{s_k} D.
```

Then, for every `t>=0`,

```text
|{x : MPS^t(x)=y}|
  = product_i A_{s_i}(t+1) - product_i A_{s_i}(t).
```

For the fixed target `y=(UD)^n` the separate formula is `A_n(t+1)`.  The
formula includes `t=0`; when `t` exceeds the possible height of every local
Dyck replacement the difference is zero.  The proof expands each displayed
top band to `U Q_i D`, with `height(Q_i)<=t+1`, and requires at least one
`Q_i` to have height exactly `t+1`.

### Decisive kill

This is a mathematically complete two-axis signal, but it fails the internal
independence gate.  P144 already occupies a Dyck-path clock plus exact
target-fibre conjunction.  More decisively, the current batch's killed `DAE`
and `MHE` candidates already use global height truncation, a maximum-height
clock, all-time images, and every-target bounded-walk enumeration; `DAE` was
killed against P160's truncation atlas.  `MPS` changes the cap to a parity cap
and factors the inverse over top bands, but its core proof remains global
height capping followed by bounded-height path enumeration.

Verdict: **`KILL_INTERNAL_DAE_P144_P160`**.  The bounded external search did
not find this exact simultaneous scheduler, but that non-hit supplies no
positive credit.

## 3. `XSD`: exact-two-secant duality

### Literal map

Normalize nonzero vectors of `F_p^3` by their first nonzero coordinate, using
the same list both for points and for line coefficient vectors.  For a point
subset `S` of `PG(2,p)`, let `XSD(S)` contain coefficient point `a` exactly
when the line `a dot x=0` contains exactly two points of `S`.

### Exact signal

```text
p=2: 7 points, 128 states, image 57, maximum tail 4, periods 1 or 2
p=3: 13 points, 8192 states, image 950, maximum tail 3, periods 1 or 2
```

At `p=2`, 21 states have tail four, while at `p=3` no state has tail four and
4,256 states eventually enter a two-cycle.  The complete tail/period census
is in the canonical transcript.

### Kill

Finite-geometry work on `i`-secants, arcs, and self-duality directly owns the
atomic incidence predicate.  More importantly, the two complete planes do
not expose a stable clock statistic, an all-prime iterate, or an arbitrary
target inverse condition.  Continuing would amount to classifying a large
functional graph separately for each `p`.

Verdict: **`KILL_NO_PARAMETER_SPINE`**.  Its finite-field geometry carrier is
also too close to P161 to tolerate a merely computational residual.

## 4. `MEG`: mutual-eccentric transform of a `{1,2}` metric

### Literal map and elementary rewrite

A labelled simple graph `G` encodes a metric by distance one on edges and
distance two on nonedges.  Join `i,j` in `MEG(G)` iff `j` is farthest from
`i` and `i` is farthest from `j`.  If `U(G)` is the set of universal vertices,
the literal metric definition gives

```text
MEG(G) = complement(G) union K_{U(G)}.
```

The verifier checks this identity pair by pair, rather than using it to
define the map.

### Exact signal and inverse description

All labelled graphs through `n=6` were exhausted.  For `n>=3` every recurrent
state has period one or two and every tail has length at most two.  At `n=6`,
31,346 of 32,768 graphs are already in two-cycles, 710 have tail one into a
two-cycle, 710 have tail two, and the empty graph has tail one into the unique
fixed complete graph.

For a target `H`, a source with proper universal set `U` is unique once `U`
is chosen.  Such a choice is feasible exactly when

- there are no `H`-edges from `U` to its complement;
- `H[U]` is complete; and
- `H-U` has no isolated vertex.

The special source `K_n` maps to `K_n`.  Thus the one-step indegree is a
clique-component/isolated-vertex statistic; the observed positive indegrees
reach four at `n=6`.

### Kill

The notions of eccentric graph and mutually eccentric vertices are directly
owned.  After the displayed rewrite, the temporal and inverse statements are
only complementing plus isolated/universal component bookkeeping, with
depth at most two.  That is below the required temporal threshold even if the
precise mutual transform has no direct iteration paper.

Verdict: **`KILL_DIRECT_PRIMITIVE_AND_SHALLOW`**.

## 5. `CTB`: continuous-time unit balancing on a path

### Literal process

The state is a weak composition `(a_1,...,a_n)` of mass `M`.  Each path edge
with `|a_i-a_{i+1}|>=2` has an independent rate-one clock.  When it rings,
one chip moves from the larger load to the smaller.  The embedded jump chain
therefore chooses uniformly among currently active edges.

### Exact signal

The potential `sum_i a_i^2` strictly decreases at every jump.  Complete
rational endpoint laws and continuous-time mean absorption times were solved
recursively on four finite DAGs:

```text
(n,M)   states  edges  absorbing  max jumps  max endpoint support
(3,4)      15     16       3          3              3
(3,6)      28     36       3          4              3
(4,6)      84    132       8          5              5
(4,8)     165    300       7          9              5
```

For example, the all-mass-at-the-left initial states have exact mean
absorption times `3, 7/2, 7/2, 31/4` in the four boxes.

### Kill

Local load balancing and discrepancy-one terminal states are established
objects.  The pilot finds genuine random endpoint branching, but only a DAG
recursion, not an all-parameter hitting law or target formula.  The potential
proof alone is standard and the route is also close to the portfolio's chip
and first-passage systems (P129/P151).

Verdict: **`KILL_FINITE_DP_ONLY`**.

## 6. `DPF`: divisor-count fragmentation of integer partitions

### Literal map

For every part `m` of a partition of `N`, replace it by one part `tau(m)` and
`m-tau(m)` parts equal to one, where `tau` is the number-of-divisors function;
then sort.  Total mass is preserved because `tau(m)<=m`.

### Exact signal

Every partition in eight boxes through `N=24` was enumerated.  A partition is
fixed exactly when all its parts lie in `{1,2}`.  Its depth is the maximum,
over original parts, of the number of divisor-function iterations needed to
reach `{1,2}`.  The final box has 1,575 states, image size 138, 13 fixed
states, and depth distribution

```text
0:13, 1:304, 2:441, 3:723, 4:94.
```

### Kill

The temporal coordinate is exactly classical iterated-divisor-function
stopping.  Arbitrary target inversion asks for multiplicities of source parts
whose independent fragments assemble the target, an unrestricted coefficient
extraction rather than a new closed atlas.  P126/P147 already occupy much
stronger composition/partition rewriting mechanisms.

Verdict: **`KILL_OWNED_CLOCK_NO_INVERSE_ATLAS`**.

## 7. `GGT`: pairwise-GCD triangle

### Literal map and full exact formula

On triples of divisors of `N`, set

```text
GGT(a,b,c) = (gcd(a,b), gcd(b,c), gcd(c,a)).
```

Associativity gives

```text
GGT^2(a,b,c) = (g,g,g),  g=gcd(a,b,c),
```

so the only recurrent states are diagonal fixed points and the sharp depth is
two when `N>1`.

The inverse count is nevertheless exact.  For a prime power `p^e || N`, let
`(alpha,beta,gamma)` be the target valuations.  Its local one-step fibre is

```text
1 + 3(e-h),          if alpha=beta=gamma=h;
2(e-k) + 1,          if the minimum h occurs exactly twice and k is the maximum;
0,                    if the minimum occurs exactly once.
```

The full fibre is the product of these local factors.  At time two a target
must be diagonal, say `(d,d,d)`, and its fibre is

```text
product_{p^e || N} ((e-v_p(d)+1)^3 - (e-v_p(d))^3).
```

All formulae were checked on the full divisor cubes for
`N=2,6,12,36,72,180` (8,577 states in total).

### Kill

This is a coordinatewise minimum map on the divisor-product lattice.  Its
two-step collapse and local inverse cases are a small meet-semilattice
calculation.  The P128/P142 GCD machinery and the same-batch `CNG` adjacent
GCD/minimum system already occupy the proof silhouette at substantially
greater depth.

Verdict: **`KILL_INTERNAL_MEET_GCD`**.

## 8. Final gate

| candidate | nontrivial all-time/clock | target-resolved second axis | owner-thin and internally distinct | final |
|---|---:|---:|---:|---|
| `MPS` | yes | yes | **no** | kill |
| `XSD` | no | no | not reached | kill |
| `MEG` | shallow only | yes | no | kill |
| `CTB` | no closed law | DP only | no | kill |
| `DPF` | owned scalar stopping time | no | no | kill |
| `GGT` | depth two | yes | no | kill |

The correct Round-6 result is therefore **KILL_ALL**.  There is no theorem
contract to transmit and no paper drafting is authorized.  All results remain
**HOLD_EXTERNAL**.
