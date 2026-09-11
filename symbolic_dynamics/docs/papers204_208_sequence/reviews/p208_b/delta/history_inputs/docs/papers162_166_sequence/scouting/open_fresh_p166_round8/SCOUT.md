# P166 open discovery Round 8 — exact scout

**Decision:** `GREEN_OWNER_THIN_MIP`  
**Killed controls:** 5  
**External state:** `HOLD_EXTERNAL`  
**Paper/Git actions:** none

## Outcome first

Six fresh literal systems were exact-tested after a repository-wide duplicate
screen.  Five fail a direct-owner, second-axis, or internal-collision gate.
`MIP`, minimum inverse-position feedback on labelled endofunctions, survives
as one owner-thin theorem contract.  It has:

1. a componentwise all-time law with sharp height `2n-2` and only periods one
   and two;
2. exact recurrent and fixed exponential generating functions, hence the
   zeta function; and
3. a nonuniform every-target one-step fibre formula whose maximum is the Bell
   number.

This is a scout promotion only.  It requires an independent hostile gate and
remains `HOLD_EXTERNAL`.

## Frozen intake evidence

The duplicate screen included the prior Round-2--6 ledgers, the broad
cross-class and matching/incidence scouts, the current endofunction DFJ
negative control, the P122 `(xy,yx)` hostile gate, and the TDS independent
kill.  Representative pinned hashes were:

```text
d059a3f3f3a7dcdd3b562ec96009add54dff2d8cc313a811129f4b813ef89bc4  Round-2 idea ledger
b2f314f4e7ad99cdfa241b8e33ca0de65c7a24467379d91032903a8c32d370ed  Round-3 idea ledger
62de8c7e51511787c8a4c874ff60f7160ee3d783df179766128e19f2c53a1689  Round-4 idea ledger
914e4750f3ced91e3ad23f6cc72438c424f5bfc2ae2eccf1d10ef0e43d37f6cc  Round-5 idea ledger
9e37b9b97b42e84740660f39699113eaa3d5319b553b5f198fb8baf9b5e67520  Round-6 idea ledger
5afabf3a59797d712aee0991321f79b4eabf74b6c25c677740847e380a59eee6  replacement_crossclass scout
cfa1f5924e6d3404c8766e27ab02dec7a473edf8d5298d9e710d6099a25db0fd  replacement_matchings_incidence scout
5e91c7ef6eb88454a444195aa893753502d57bd2055e0ac7b43a748062d1783c  P122 group-product-exchange gate
b8cbadb72667310dbe7d517a880233e836df91a33822248ec8c1113226e20494  DFJ scout
6893e531a4b4cce3a54a9145399f4dea93d0a3e1a4857e2f652e147fc9281696  TDS independent gate
```

Two initially implemented ideas were discarded rather than counted after
the wider string search exposed exact prior occurrences: the canonical
kernel representative was `KRR`, and alternating projective exact-one
incidence was `FTA/PTA/I01/I03`.  The verifier was rewritten to remove both.

## `BFR`: cyclic Tits refinement — KILL

Let a face of the braid arrangement be an ordered set partition `P` of
`[n]`.  Let `rho` cyclically relabel the ground set, and let `*` be the Tits
product: list all nonempty intersections of a block of the left factor with a
block of the right factor, in lexicographic block order.  The update is

```text
T(P)=P*rho(P).
```

Because the face semigroup is a left regular band (`xyx=xy`),

```text
T^t(P)=P*rho(P)*...*rho^t(P).
```

The support partition therefore refines by consecutive cyclic translates.
After at most `n-2` steps it is invariant under `rho`; this is sharp.  A fixed
support is the coset partition for a subgroup of the cyclic regular action.
If it has `d` blocks, those blocks may be ordered in `d!` ways.  Hence

```text
#Fix(T)=sum_(d|n) d!.
```

The exact rows `(n,states,image,fixed,max_tail,max_fibre)` are

```text
2 3 3 3 0 1
3 13 7 7 1 2
4 75 35 27 2 4
5 541 201 121 3 6
6 4683 1245 729 4 11
7 47293 9227 5041 5 23
```

The temporal calculation is real but not residual: it is the defining Tits
product plus repeated support refinement under an automorphism.  Arbitrary
target fibres did not reduce beyond ordered common-refinement constraints.
This is precisely the left-regular-band/semilattice closure engine that the
intake firewall excludes.  **Decision:
`KILL_LRB_REFINEMENT_ENGINE`.**

## `QDP`: quiver detour pruning — KILL

Use all subgraphs of the complete acyclic orientation `1<...<n`.  Delete an
arrow `i->j` exactly when another directed path connects `i` to `j`.

For a DAG this is its unique transitive reduction, so the map is idempotent.
Its image is the class of transitively reduced ordered DAGs.  If `H` is in
the image, every source with target `H` is obtained by independently adding
any subset of comparable non-cover pairs.  Thus

```text
|T^(-1)(H)|=2^(|TC(H)|-|E(H)|),
```

and all other targets have empty fibre.  Exhaustion through order six checks
that formula over every target; at `n=6` there are `4,824` image objects among
`32,768` ordered DAGs and the largest fibre is `1,024`.

Aho--Garey--Ullman directly own the operation and its reachability-preserving
minimality.  Recasting the algorithm as a one-step finite dynamic adds no
temporal theorem.  **Decision:
`KILL_DIRECT_TRANSITIVE_REDUCTION_OWNER`.**

## `QTF`: unique-factorization arrow toggle — KILL

On the same ordered-DAG carrier, toggle `i->j` iff there is exactly one
factorization `i->k->j` in the old quiver.

The predicate for an edge of span `j-i` uses only shorter-span edges.  Reading
spans from one upward therefore reconstructs the source uniquely from the
target: the map is a triangular bijection and every target fibre is one.
The complete cycle spectra are

```text
n=2: 1^2
n=3: 1^6 2^2
n=4: 1^28 2^36
n=5: 1^194 2^754 4^76
n=6: 1^2056 2^22696 4^7376 8^640.
```

The growing power-of-two period is an interesting pilot, but no proved
all-`n` cycle census or sharp period formula emerged, while the inverse axis
is trivial.  The atomic exact-one two-walk predicate was already exhausted
and killed as `UWS`; XOR feedback does not create a second theorem axis.
**Decision: `KILL_NO_SECOND_AXIS_UWS`.**

## `BLM`: cyclic bargraph local-maximum transfer — KILL

For a weak composition `h=(h_0,...,h_(m-1))` of `N`, regard the columns as a
cyclic bargraph.  Every strict cyclic local maximum sends one unit to its
clockwise neighbour, simultaneously.

Mass is invariant.  For each firing pair,

```text
(h_i-1)^2+(h_(i+1)+1)^2-h_i^2-h_(i+1)^2
 =2(h_(i+1)-h_i+1)<=0,
```

and firing pairs are disjoint, so square energy never rises.  A state is
fixed exactly when it has no strict cyclic local maximum.  All twelve tested
boxes (`3<=m<=6`, `N in {m,2m,3m}`) absorbed, but their maximum tails were

```text
m=3: 3,4,6
m=4: 3,5,7
m=5: 5,6,9
m=6: 6,7,10.
```

These values do not expose a uniform two-parameter clock, and target fibres
remain scheduler-coupled.  Parallel chip-firing/diffusion and local load
balancing directly own the ambient mechanism; `CTB` already failed for the
same absence of a closed endpoint law.  **Decision:
`KILL_NO_PARAMETER_SPINE_LOAD_BALANCING`.**

## `DWS`: divisible-word span — KILL

For a binary linear code `C<=F_2^n`, define

```text
T(C)=span {c in C : wt(c)=0 mod 3}.
```

If `D=T(C)`, its displayed generators still belong to `D` and still have
weight divisible by three.  Hence `T(D)` contains those generators and is
contained in `D`, proving `T^2=T`.  Exact subspace-lattice exhaustion gives

```text
n             1  2   3   4    5     6
#codes        2  5  16  67  374  2825
#fixed/image  1  1   2  16  162  1475.
```

This is a generic span-of-selected-elements projection.  Divisible-code and
fixed-weight-generator theory owns the static objects, while P165 already
occupies low-weight selection followed by code shortening/span structure.
There is no temporal axis.  **Decision:
`KILL_ONE_STEP_CODE_PROJECTION`.**

## `MIP`: minimum inverse-position feedback — GREEN

For `f:[n]->[n]`, let

```text
M(f)(i)=min f^(-1)(i) when that fibre is nonempty,
        i             otherwise.
```

After one step, every nonloop target value is used at most once.  The
functional graph is consequently a disjoint union of directed cycles and
loop-rooted paths.  `M` reverses a directed cycle.  On a path listed
root-to-leaf as `(p_0,...,p_l)`, it reverses the whole path when `p_0>p_1`;
when `p_0<p_1`, it splits off `p_0` and reverses the rest.  A path is
recurrent iff both endpoints exceed their inward neighbours.  This proves
periods at most two and the sharp global tail `2n-2`; full details and the
explicit witness are in `MIP_THEOREM_CONTRACT.md`.

The labelled connected recurrent counts are a directed cycle plus an
endpoint-admissible path.  Thus

```text
R(x)=sum R_n x^n/n!
    =1/(1-x) exp(x^3/3+x^4/(4(1-x))),
I(x)=sum I_n x^n/n!=exp(x+x^2/2).
```

Here `R_n` counts all recurrent states and `I_n` counts fixed states.  Hence
`Fix(M^k)=I_n` for odd `k`, `R_n` for even `k`, and

```text
zeta_n(z)=(1-z)^(-I_n)(1-z^2)^(-(R_n-I_n)/2).
```

For every target, the fibre is an explicit sum over which fixed coordinates
mean “present first at itself” rather than “absent,” followed by a product of
the number of already opened symbols at each free word position.  The exact
formula is in the focused contract and is tested for all supported targets
through `n=7` and all supported or unsupported targets through `n=6`.
Every kernel partition contributes at most one source; equality over the
identity yields the sharp maximum fibre `B_n`.

The phase portrait is

```text
n  states  image  recurrent  fixed  max-tail  max-period  max-fibre
1       1      1          1      1         0           1          1
2       4      3          2      2         2           1          2
3      27     14          8      4         4           2          5
4     256     84         38     10         6           2         15
5    3125    612        220     26         8           2         52
6   46656   5220       1540     76        10           2        203
7  823543  50880      12460    232        12           2        877
```

The primary search found generic functional-digraph, full-transformation
semigroup, generalized-inverse/transversal, and restricted-growth owners,
but no source stating this literal self-map or its iteration.  Those generic
ingredients receive zero credit.  Internally, `KRR(f)(j)=M(f)(f(j))`, but
`KRR` is an idempotent kernel quotient whereas `MIP` has unbounded sharp
height, path reversal, a nontrivial recurrent species, and nonuniform
all-target fibres.  P143 has a depth-one Boolean-preorder image, and DFJ's
closed slices are classical power maps; neither supplies the MIP contract.

**Decision: `GREEN_OWNER_THIN / NEEDS_INDEPENDENT_HOSTILE_GATE`.**

## Verification

`verify_scout.py` imports no author/scout code and uses only the Python
standard library.  It checks:

- all ordered-partition BFR states through `n=7`, including every closed
  iterate cell, fixed count, and sharp tail;
- all ordered DAGs through `n=6` for QDP and QTF, including every QDP target
  fibre and every QTF cycle;
- all twelve BLM boxes and every local mass/energy/fixed-point assertion;
- all binary subspaces through length six for DWS; and
- all `873,612` cumulative endofunction states through `n=7` for MIP, including
  the fibre formula, unsupported targets through `n=6`, recurrent EGF,
  involution fixed count, Bell extremum, and sharp clock.

The exact assertion total is **1,119,007**.  `CANONICAL.txt` is the frozen
stdout.  Two fresh byte-for-byte replays are required at handoff.
