# Derivation Package — Paper 33 / SD-C35

## Target

Determine whether a source-natural cycle quotient or twist of the exact Paper
32 projective-residue recurrent object can annihilate `S^2`, `R^3`, and all
cusp diamonds while retaining a prime-selective primitive ledger and an honest
quotient determinant.

## Status

COHERENT AFTER REFRAMING / EXTRA ASSUMPTION

The positive target fails.  The coherent result is a complete classification
of the frozen relation quotient: it is the classical Manin-symbol relation
module, every modulus retains a universal cusp class, diamond filling erases
all cross-modulus homology, and the original graph-step adjacency does not
descend.  The result is a negative paper and closes the semiring-residue
family.

## Invariant Object

The invariant algebraic object is

$$
M_n=\mathbb Q[X_n]/W_n,
\qquad
W_n=\operatorname{im}(I+P_{S,n})+
\operatorname{im}(I+P_{R,n}+P_{R,n}^2).
$$

The global object is obtained by joining the distinguished cusps with the
same `2`- and `3`-multiplication edges as Paper 32 and attaching every
commuting diamond as a two-cell.

## Assumptions

- The full Paper 32 source lock, graph, roofs, and edge marker are retained.
- Coefficients are rational, so `2` and `3` are invertible.
- No quotient coefficient consults a prime/composite label or static field
  defect.
- Presentation characters act only on `S,R` and extend trivially over the
  inherited cross multipliers.
- The `S,R` action on each `X_n` is transitive.
- Cross pairs are reduced to one oriented cellular edge before the diamond
  boundary is imposed; this is the chain-level version of removing immediate
  reverse traversal.
- A determinant is credited to the quotient only if the original graph-step
  action descends, or if an explicitly declared replacement is kept as a
  comparison rather than promoted to ownership.

## Notation

- `V_n=Q[X_n]`.
- `o_S(n)` and `o_R(n)` are the numbers of `S`- and `R`-orbits on `X_n`.
- `D_n` is the bipartite incidence multigraph with vertex classes the
  `S`-orbits and `R`-orbits and one edge for each `x in X_n`.
- `b_n=dim_Q M_n`.
- `K` is the cross-modulus graph with edges `n--2n` and `n--3n`.
- `A_n=P_{S,n}+P_{R,n}` is the inherited within-block graph-step adjacency.
- `L_fs=direct_sum_{n>=2} M_n` is the restricted block ledger; it is not
  asserted to be compactly supported cohomology.

## Derivation Strategy

Translate the presentation boundaries into orbit-indicator subspaces.  Use
the connected incidence dessin to compute the quotient dimension exactly.
Exhibit a two-edge cusp circuit that survives for every modulus.  Then fill
the `2x3` cross squares and prove that each cross component is contractible.
Finally test twists and operator descent before discussing any determinant.

## Derivation Map

1. `S^2` and `R^3` boundaries generate the two orbit-indicator subspaces.
2. Their intersection is one-dimensional because the incidence dessin is
   connected.
3. The dimension formula is the cycle rank of that dessin.
4. The cusp and its `R` image give parallel incidence edges, proving the rank
   is positive for every modulus.
5. Factoring each modulus as `m 2^a 3^b` makes every cross component a square
   grid (with the missing `n=1` corner when `m=1`); diamond cells make each
   component contractible.
6. Therefore global first homology is the direct sum of the duals of the
   nonzero block modules, not a cross-modulus prime family.
7. Cycle-word traces and Manin norm-polynomial evaluations are enumerated
   separately; every cancellation regime retains the universal cusp word.
8. The original adjacency fails the quotient invariance test already at
   `n=2`, so a same-marker quotient determinant is not owned.

## Main Derivation

### Step 1 — relation images are orbit indicators (identity)

For an `S`-orbit of length two, `(I+S)e_x=e_x+e_{Sx}`; for an `S`-fixed
point it equals `2e_x`.  Hence, over `Q`,

$$
\operatorname{im}(I+S)
=\operatorname{span}\{\mathbf 1_O:O\text{ is an }S\text{-orbit}\}.
$$

The same argument with `I+R+R^2` gives the span of the `R`-orbit indicators.
Thus their dimensions are `o_S(n)` and `o_R(n)`.

### Step 2 — exact relation rank (proposition)

If a vector belongs to both orbit-indicator spaces, then its coefficient on a
state `x` depends only on the `S`-orbit of `x` and only on the `R`-orbit of
`x`.  These coefficients propagate across the incidence graph `D_n`.
Transitivity of the `S,R` action makes `D_n` connected, so every coefficient
is equal.  Therefore

$$
\dim(W_n)=o_S(n)+o_R(n)-1
$$

and

$$
b_n=|X_n|-o_S(n)-o_R(n)+1=\beta_1(D_n).
$$

The last equality is the connected-graph cycle-rank formula.

### Step 3 — universal cusp survivor (proposition)

Let

$$
c=[1:0],\qquad y=Rc=[0:1].
$$

For every `n>=2`, `c` and `y` are distinct, while

$$
Sy=[-1:0]=[1:0]=c.
$$

Consequently the two state edges `c` and `y` have the same `R`-orbit endpoint
and the same `S`-orbit endpoint in `D_n`.  They form a parallel-edge circuit.
More explicitly, in the standard orthonormal state basis set

$$
z_n=e_c-e_y.
$$

Every `S`- or `R`-orbit indicator has zero pairing with `z_n`, so
`z_n in W_n^perp`.  Since `z_n` is nonzero and the standard rational pairing
is positive definite, `z_n` cannot belong to `W_n`; therefore its quotient
class `[z_n] in M_n` is nonzero.  With both dessin edges oriented from their
`S`-orbit vertex to their `R`-orbit vertex, `partial z_n=0`, so the same
vector is the two-parallel-edge first-homology cycle.  Hence

$$
b_n\ge1\qquad(n\ge2).
$$

In the original generator-labelled multigraph this circuit is the primitive
two-step word `R` then `S`.  Edge identities are retained: the inverse of the
first `R` transition has label `R^{-1}=R^2`, whereas the second transition is
labelled `S`.  Ihara/Hashimoto backtrack removal therefore does not delete it.

### Step 4 — arithmetic interpretation (identification, not novelty claim)

The quotient by the two displayed Manin relations is the classical relative
modular-symbol module for `Gamma_0(n)`.  Its rational dimension is also

$$
b_n=2g_0(n)+c_0(n)-1,
$$

where `g_0(n)` is the genus of `X_0(n)` and `c_0(n)` its cusp count.  Removing
the cusp-boundary part leaves dimension `2g_0(n)`.  This stronger quotient
still does not select fields: finite census gives nonzero cuspidal homology on
38 of 43 primes, 9 of 14 prime-power composites, and 130 of 134 mixed
composites through `n=192`; it also vanishes on five primes.

### Step 5 — diamond filling (theorem)

Write each modulus uniquely as

$$
n=m2^a3^b,\qquad \gcd(m,6)=1.
$$

Cross edges change exactly one of `a,b` by one.  For `m>1`, a component of
`K` is the square lattice on `N^2`; the `m=1` component is the same quadrant
with the nonexistent `n=1` corner removed.  Every available elementary
square is exactly

$$
n,2n,6n,3n,n.
$$

Attaching all such squares makes every infinite component contractible.  At
a cutoff `n<=N`, the exponent set for `m>1` is a finite down-set.  The union
of its cubes is coordinatewise lower-closed and contracts to `(0,0)`.  For
`m=1`, cover the corner-deleted complex by the subcomplexes `a>=1` and
`b>=1`.  Each is a translated down-set; when their intersection is nonempty
it is another translated down-set, and otherwise they are separate
components.  Hence every finite cross component is also contractible.

Subdivide the state edge `c_n` of `D_n` once and attach the inherited cross
edge at that midpoint.  This is only a cellular subdivision and leaves block
homology unchanged.  Each subdivided block complex then meets the cross
complex at exactly one vertex.  Collapsing every contractible cross component
to a point gives a wedge of the block dessins.  Since cellular one-chains have
finite support,

$$
H_1(\text{global filled complex};\mathbb Q)
\cong\bigoplus_{n\ge2}H_1(D_n;\mathbb Q)
\cong\bigoplus_{n\ge2}M_n^*.
$$

Blockwise, `M_n=H^1(D_n;Q)` and is the rational dual of its cycle space.  Thus
the restricted block ledger is `L_fs=direct_sum M_n`.  Ordinary unrestricted
global `H^1` would instead be the product `product M_n`; neither statement
identifies `L_fs` with compactly supported cohomology.

Diamond annihilation removes all cross-modulus recurrent information instead
of leaving a source-linked prime family.

### Step 6 — character and supercharacter test (exact algebra)

There are two distinct operations and they must not be conflated.  First, for
an honest representation `rho` of `C2*C3`, the **cycle relator words** obey

$$
\rho(S)^2=I,\qquad \rho(R)^3=I.
$$

Their ordinary traces, and the trace of a commuting diamond word, are
therefore `dim rho`, not zero.  A cycle-character twist changes a primitive
cycle by a nonzero phase and does not annihilate it.

Second, the **Manin chain boundaries** use the norm polynomials `1+S` and
`1+R+R^2`.  Let `t` be a primitive sixth root and enumerate the six
one-dimensional characters by

$$
\chi_k(S)=t^{3k},\qquad \chi_k(R)=t^{2k},\qquad 0\le k<6.
$$

Exactly `k=1,5` make both norm-polynomial evaluations vanish:

$$
1+\chi_k(S)=0,\qquad
1+\chi_k(R)+\chi_k(R)^2=0.
$$

This legitimate chain-level cancellation does not cancel the cusp cycle:
`chi_k(SR)=t^{5k}` is a nonzero phase.  For virtual differences
`chi_k-chi_l`, all fifteen have superdimension zero and hence zero
supertrace on the identity relator words and commuting diamond word.  Only
the two pairs `{1,5}` and `{2,4}` also make both norm-polynomial evaluations
zero.  In every one of the fifteen cases,

$$
(\chi_k-\chi_l)(SR)=t^{5k}-t^{5l}\ne0,
$$

because multiplication by five permutes `Z/6Z`.  All fifteen distinct
differences therefore retain the same cusp circuit on every prime and every
composite block.  Thus the complete one-dimensional census covers both
semantics without claiming that honest characters cannot kill the chain
polynomials.

### Step 7 — operator descent fails (proposition)

An operator on `V_n` descends to `M_n=V_n/W_n` only if it preserves `W_n`.
For `n=2`, order the states as

$$
x_0=[0:1],\quad x_1=[1:0],\quad x_2=[1:1].
$$

The Manin relation space is

$$
W_2=\operatorname{span}\{e_0+e_1,e_2\}.
$$

The inherited adjacency `A_2=P_S+P_R` satisfies

$$
A_2e_2=e_2+e_1\equiv-e_0\pmod{W_2},
$$

which is nonzero.  Hence `A_2(W_2)` is not contained in `W_2`; the global
graph-step operator cannot descend to the direct-sum quotient.  The exact
census finds the same non-invariance for every `2<=n<=192`.

### Step 8 — analytic comparison and ownership boundary

The scalar comparison

$$
K_s=\bigoplus_{n\ge2}n^{-s}I_{M_n}
$$

is trace class for `Re(s)>2`, since `b_n<=|X_n|=psi(n)` and the Paper 32
Dedekind-psi majorant converges there.  Thus `det(I-zK_s)` exists.

This determinant is not owned by the original graph-step dynamics.  Its
`z` counts a blockwise identity action, not an original edge, and it exists
only after replacing the non-descending adjacency.  Orthogonal Hodge
compression has the same problem: it is a new nonlocal compression rather
than an induced quotient map with a surviving primitive ledger.  Hopf-trace
or graded-determinant identities require a chain map, which the inherited
adjacency is not.

## Remarks and Interpretation

- The required universal relations and diamonds can be killed exactly, but
  the operation is generic topology rather than arithmetic selectivity.
- The quotient lands directly in classical modular-symbol territory; the
  quotient mechanism itself is not novel.
- Relative homology retains every modulus.  Removing cusps still retains many
  composites and loses some primes.
- Same-object analytic ownership is weaker after quotienting than it was in
  Paper 32: the unquotiented operator owns a determinant, but the homological
  relation quotient does not inherit it.

## Boundaries and Non-Claims

- No theorem is claimed for every conceivable superrepresentation, cocycle,
  or nonlocal quotient.
- No claim is made that modular symbols, Ihara zeta, Hashimoto operators,
  Kac-Ward signs, or Hopf trace are new.
- The scalar comparison determinant is not promoted to Route-A ownership.
- No target-zero data, analytic continuation, functional equation, Weil
  compression, self-adjoint carrier, or Route B is used.

## Open Risks

- A genuinely different global arithmetic dynamical system may possess a
  chain map whose primitive ledger is selective.  It would be outside the
  frozen semiring-residue family.
- A general theorem classifying all nonlocal superrepresentations was not
  attempted; the branch closes because the exact mandated quotient already
  realizes four independent stop conditions.
