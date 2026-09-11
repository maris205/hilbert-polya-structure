# P214 Review B deductive and source audit

2026-09-11 UTC. SOURCE preparation by eligible nonauthor
`/root/p212_round2_terminal_finish`, from accepted physical Round1 only.
No scientific verifier, build or manuscript edit was executed.

## Independent clock proof

Write the orbit as consecutive registers `x_0=x`, `x_1=y`. After one update,
`x_2=x(t+y)` lies in `t^2R`. Hence every multiplier used from then on has the
form `t(1+r)` with `r in tR`; its parenthesized factor is a unit. Viewed on the
associated graded filtration, each later two-step update raises the surviving
coefficient order of its parity register by exactly one.

If `v(y)>=2`, this also holds at the initial even update, so the two filtered
registers vanish after respectively `2(m-v(x))-1` and `2(m-v(y))` state
steps. Their maximum is the first simultaneous zero. If `v(y)=1`, the first
even update may cancel, but every later odd-register multiplier is still
`t` times a unit because its neighboring even term is already in `t^2R`.
Thus the odd register survives through index `2m-3` and vanishes at the next
state, fixing depth `2m-2` regardless of acceleration in the even register.
This also covers `x=0`, `y=0`, cancellation at `y=-t`, and `m=2`.

The filtration rectangle for depth at most `h` is
`t^(m-ceil(h/2))R x t^(m-floor(h/2))R`, whose cardinality is `q^h`.
Subtracting adjacent rectangles gives the exact depth census. Since every
orbit reaches zero, zero is the only recurrent state. This proof is phrased
as a two-step associated-graded argument, rather than accepting finite data
or A's reverse-graph construction as proof.

## Independent fibre proof

For target `(u,w)`, the first output coordinate forces source `y=u`. Put
`a=t+u` and let `d=min(v(a),m-1)`. In coefficient coordinates, the equations
for `ax=w` below degree `d+1` force those target coefficients to vanish.
When `d<=m-2`, the coefficient of `t^(d+k)` has the triangular form

`a_d x_k + sum_{i=d+1}^{d+k-1} a_i x_(d+k-i) = w_(d+k)`.

Because `a_d` is nonzero, the field equation determines successively
`x_1,...,x_(m-d-1)`. The last `d` coefficients of `x` are free, so every
reachable target has exactly `q^d` predecessors and every unreachable target
has none. For `d=m-1`, all products with `x in I` vanish; exactly `w=0` is
reachable and all `q^(m-1)` values of `x` occur. This coefficient-triangular
derivation neither invokes a unit/coset constructor nor Gaussian elimination.

Translation by `t` partitions `u` by the first nonzero coefficient of `a`.
There are `(q-1)q^(m-d-1)` ordinary `u` and `q^(m-d-1)` compatible `w` for
each `1<=d<=m-2`, giving the stated target count. The saturated stratum has
the q values `u=-t+c t^(m-1)` and only `w=0`. Summation yields the image
formula and shows the q saturated targets uniquely maximize the fibre.

The two-sided identity `F=QMP` correctly deducts inverse-mechanism novelty but
is not an iterate conjugacy. The linear map has the same filtered two-step
clock. At `m=2`, `I^2=0` makes `F=L`. For `m>=3`, the verified formulas give
positive fibres of sizes q and `q^(m-1)`; a finite-group endomorphism has every
nonempty fibre a coset of one kernel, so conjugacy is impossible. This does
not exclude arbitrary nonlinear factors.

## Manuscript and source findings

The theorem statements match the proofs, including zero coordinates,
characteristic two, the saturated fibre, `m=2`, and the exact maximizers.
The finite protocol explicitly distinguishes F4 from integers modulo four.
The two citations are used only for finite-group endomorphism and complex
Fibonacci-map context; the needed algebra is proved locally. Classical
valuation growth, multiplication fibres, the linear clock shape and global
priority are not overclaimed.

The title phrase "bilinear dynamics" describes the bilinear feedback term;
unlike the pre-A abstract, it does not call the whole pair map bilinear. The
Round1 abstract correctly says "polynomial map". No Critical, Major or Minor
manuscript/source defect is found at SOURCE stage.

## Independent verifier representation

The proposed B source represents ideal elements as coefficient tuples. It
discovers each state depth by forward repeat detection, constructs the entire
literal predecessor relation, and separately solves every multiplication
equation by coefficient-triangular back substitution. It uses neither author
code/canonical nor A code/results, reverse BFS or Gaussian elimination. It
also checks the linear map, complete depth/fibre censuses, exact predecessor
sets, all boundary carriers and F4 arithmetic.

Finite checks remain controls, not proofs. SOURCE_READY is not execution,
canonical adoption, a final B verdict, accepted delta, Round2, build, page
view, paper completion or external endorsement.
