# Proof Package — Paper 33 / SD-C35

## Claim

Let `X_n=P^1(Z/nZ)` carry the Paper 32 projective permutations `S,R` with
`S^2=R^3=I`, and define over `Q`

$$
M_n=\mathbb Q[X_n]/\left(
\operatorname{im}(I+S)+\operatorname{im}(I+R+R^2)\right).
$$

Retain the Paper 32 cusp edges `n<->2n` and `n<->3n`, reduce inverse pairs to
oriented one-cells, and attach every cusp diamond as a two-cell.  Then:

1. `dim M_n=|X_n|-o_S(n)-o_R(n)+1`, where `o_S,o_R` count generator orbits;
2. `M_n` is nonzero for every `n>=2`, with a universal primitive cusp witness
   `c_n -> R c_n -> S R c_n=c_n`;
3. after all diamonds are attached, cross-modulus first homology vanishes and
   global first homology is the direct sum of the block cycle spaces
   `M_n^*` (equivalently, the finite-support block cohomology ledger is
   `direct_sum M_n`);
4. cycle-word traces and Manin norm-polynomial evaluations have distinct
   exact one-dimensional censuses, but every cancellation regime leaves the
   universal cusp word;
5. the inherited graph-step adjacency `S+R` does not descend to the quotient,
   already for `n=2`;
6. therefore the mandated quotient is not prime-selective, does not own a
   same-marker quotient determinant, and triggers
   `CLOSE_SEMIRING_RESIDUE_FAMILY`.

## Status

PROVABLE AS STATED

The stronger positive assertion that relation homology yields a prime-only
primitive ledger is false.  The six-part negative statement above is proved.

## Assumptions

- Coefficients have characteristic zero.
- The same state spaces, actions, cusp edges, roofs, and marker as Paper 32 are
  retained.
- The `S,R` action on every `X_n` is transitive.
- No field, prime, factorization, or target predicate occurs in the quotient.
- A quotient determinant requires an induced operator, not merely an
  orthogonal compression or a scalar comparison.
- Presentation characters act only on `S,R` and extend trivially over the
  inherited cross multipliers, as fixed in the source lock.

## Notation

- `V_n=Q[X_n]`.
- `U_S` and `U_R` are the two relation-image subspaces.
- `D_n` is the bipartite multigraph of generator orbits.
- `K` is the cross graph on the moduli.
- `t` is a primitive sixth root of unity.
- `L_fs=direct_sum_{n>=2} M_n` is the restricted block ledger, not a claim
  about compactly supported cohomology.

## Proof Strategy

Compute the relation rank through the connected orbit-incidence graph, use a
universal parallel-edge cusp circuit for nonvanishing, contract the filled
cross grid, enumerate the abelianized character twists, and give an explicit
three-state counterexample to operator descent.

## Dependency Map

1. The dimension theorem depends on Lemmas 1–3.
2. Universal nonvanishing depends on Lemma 4.
3. Global splitting depends on Lemmas 5–6.
4. The twist no-go depends on Lemma 7.
5. Operator non-descent depends on Lemma 8.
6. The Route-A conclusion combines Theorems 9–11.

## Proof

### Lemma 1 — relation images

Let `p` be a permutation whose cycles have length dividing `d`, and suppose
`d` is invertible in the coefficient field.  The image of
`I+p+...+p^(d-1)` is the span of the indicator vectors of the `p`-orbits.

**Proof.**  On an orbit of exact length `e|d`, the displayed norm sends every
basis vector to `(d/e)` times the orbit indicator.  This scalar is nonzero.
Images belonging to distinct orbits have disjoint support.  They therefore
span exactly one line per orbit.  ∎

Applied with `(p,d)=(S,2)` and `(R,3)`, Lemma 1 gives

$$
\dim U_S=o_S(n),\qquad \dim U_R=o_R(n).
$$

### Lemma 2 — connected incidence graph

The bipartite multigraph `D_n` whose left vertices are `S`-orbits, right
vertices are `R`-orbits, and edges are states in `X_n` is connected.

**Proof.**  A path alternating between left and right incidence vertices
corresponds to applying a word in `S` and `R` to a state.  Conversely, every
application of `S` or `R` moves between states incident to a common orbit
vertex.  The inherited action of the two generators is transitive on `X_n`,
so all state edges lie in one incidence component.  ∎

### Lemma 3 — intersection of relation images

$$
U_S\cap U_R=\mathbb Q\mathbf1_{X_n}.
$$

**Proof.**  If `v in U_S`, its coefficient on a state depends only on the
state's `S`-orbit.  If `v in U_R`, it depends only on the `R`-orbit.  Equality
of the two descriptions propagates equal coefficients along every edge of
`D_n`.  Lemma 2 makes this graph connected, hence all coefficients are one
common scalar.  The all-ones vector belongs to both subspaces, so the
intersection is exactly the displayed line.  ∎

### Theorem 4 — exact block quotient and universal survivor

For every `n>=2`,

$$
\dim M_n=|X_n|-o_S(n)-o_R(n)+1\ge1.
$$

**Proof.**  Lemmas 1 and 3 give

$$
\dim(U_S+U_R)=o_S(n)+o_R(n)-1,
$$

which proves the equality.

Let `c=[1:0]` and `y=Rc=[0:1]`.  They are distinct for `n>=2`, while
`Sy=[-1:0]=c` projectively.  Thus the two distinct state edges `c,y` join the
same pair of orbit vertices in `D_n`, forming a circuit of two parallel
edges.  A connected graph containing a circuit has first Betti number at
least one.  Since the equality above is also the cycle-rank formula for
`D_n`, `dim M_n>=1`.

The specific survivor is also explicit.  In the standard orthonormal basis
of `Q[X_n]`, let `z_n=e_c-e_y`.  Every `S`-orbit indicator and every `R`-orbit
indicator pairs to zero with `z_n`, because `c,y` lie in the same orbit of
each generator.  Hence `z_n in W_n^perp`.  It is nonzero, and positive
definiteness gives `W_n intersect W_n^perp={0}`; consequently
`[z_n]!=0 in M_n`.  If both state edges in `D_n` are oriented from the
`S`-orbit vertex to the `R`-orbit vertex, then `partial z_n=0`, so it is also
the concrete two-edge first-homology circuit.

In the original generator-labelled multigraph its transition word is `R`
followed by `S`.  Edge identities are retained: the inverse of the first
transition is labelled `R^{-1}=R^2`, not `S`.  It is therefore nonbacktracking.
Its cyclically reduced length in the free product `C2*C3` is two, so it cannot
be a proper power and is primitive.  ∎

### Lemma 5 — the filled cross components are contractible

Let `K` have vertices `n>=2` and undirected edges `n--2n`, `n--3n`.  Attach a
square along every circuit `n,2n,6n,3n,n`.  Every connected component of the
resulting square complex is contractible.

**Proof.**  Remove all factors of two and three from `n`; the remaining
integer `m` is constant along an edge and uniquely indexes each infinite
connected component.  For `m>1`, the map

$$
m2^a3^b\longmapsto(a,b)
$$

identifies that component with the standard cubical complex on `N^2`.  Every
elementary unit square is one attached diamond.  For `m=1`, the same statement
holds after deleting `(0,0)` and the cells incident only through that missing
vertex, because the source begins at `n=2`.

The full quadrant is contractible.  The corner-deleted quadrant is the union
of the two closed cubical half-quadrants `a>=1` and `b>=1`; both and their
nonempty intersection are contractible, so the CW gluing lemma (equivalently,
the two-set nerve lemma here) makes their union contractible.  At a finite
cutoff and `m>1`, the exponent pairs form a finite down-set.  Its
cubical realization is coordinatewise lower-closed: with every cube it
contains the rectangle from that cube to `(0,0)`.  Scalar contraction to the
origin stays inside it.  For `m=1`, the same two-subcomplex cover applies.
Each piece and every nonempty intersection is a translated finite down-set;
if the intersection is empty, its pieces are separate components.  Thus
every finite or infinite cross component is contractible, in particular it
has zero first homology.  ∎

### Lemma 6 — point-gluing splitting

After diamond filling, global first homology is

$$
H_1(\text{global filled complex};\mathbb Q)
\cong\bigoplus_{n\ge2}M_n^*.
$$

**Proof.**  In `D_n`, the state `c_n` is an edge.  Subdivide it once and attach
the inherited cross edge at the new midpoint.  Subdivision preserves
homology, and now each within-modulus complex intersects the cross square
complex in exactly one vertex.  Lemma 5 makes every cross component
contractible.  Collapsing such a contractible CW subcomplex to a point gives,
up to homotopy, the wedge of its attached block dessins.  Cellular chains are
finite sums, so first homology of this wedge is the direct sum of the block
first homologies.

Orient every edge of `D_n` from its `S`-orbit vertex to its `R`-orbit vertex.
The cellular coboundary image is `U_S+U_R` (changing the signs on one vertex
class does not change its span).  Thus
`M_n=coker(d^0)=H^1(D_n;Q)`.  Since `D_n` is finite, evaluation gives
`H_1(D_n;Q)=M_n^*`, proving the displayed formula.  Equivalently, the
restricted block ledger is `L_fs=direct_sum M_n`.  Ordinary global cohomology
is `product M_n`; no identification of `L_fs` with compactly supported
cohomology is asserted.  The midpoint subdivision is only an auxiliary CW
realization of the attachment and does not split or change a dynamical edge,
roof, or marker.  ∎

### Lemma 7 — complete one-dimensional twist census

No honest one-dimensional character of `C2*C3` has zero ordinary trace on
the cycle relator words `S^2`, `R^3`, or a commuting diamond word.  Exactly
two honest characters annihilate both Manin norm-polynomial evaluations.
All fifteen zero-superdimension differences annihilate the identity-word
supertraces, exactly two also annihilate both norm-polynomial evaluations,
and none annihilates `SR`.

**Proof.**  The abelianization is `C2 x C3`, hence cyclic of order six.  With
`t` a primitive sixth root, its six characters are

$$
\chi_k(S)=t^{3k},\qquad \chi_k(R)=t^{2k}.
$$

For an honest character, `chi_k(S^2)=chi_k(R^3)=1`, and a commuting diamond
is also an identity word.  Thus none has zero cycle-word trace.  In contrast,
the Manin chain polynomials evaluate as

$$
1+\chi_k(S),\qquad 1+\chi_k(R)+\chi_k(R)^2.
$$

The first is zero exactly when `k` is odd; the second is zero exactly when
`k` is not divisible by three.  Both vanish precisely for `k=1,5`.  Yet
`chi_k(SR)=t^{5k}` is a nonzero root of unity, so both chain-cancelling honest
characters retain the cusp word.

For `k!=l`, the virtual character `chi_k-chi_l` has value zero on the
identity, hence zero supertrace on the two cycle relator words and on the
commuting diamond word.  Its `S`-norm evaluation is zero exactly when `k,l`
have the same parity.  Its `R`-norm evaluation is zero exactly when either
both or neither are divisible by three.  Among unordered distinct pairs,
both conditions hold precisely for `{k,l}={1,5}` and `{2,4}`.  On the cusp
word, for every distinct pair,

$$
(\chi_k-\chi_l)(SR)=t^{5k}-t^{5l}.
$$

Since `gcd(5,6)=1`, the residues `5k` and `5l` are distinct modulo six.  The
two roots are distinct and their difference is nonzero.  There are
`binom(6,2)=15` such differences.  This proves both censuses while keeping
cycle-word cancellation distinct from chain-polynomial cancellation.  ∎

### Lemma 8 — explicit failure of adjacency descent

For `n=2`, the operator `A_2=S+R` does not preserve the relation subspace.

**Proof.**  In the ordered basis

$$
e_0=[0:1],\quad e_1=[1:0],\quad e_2=[1:1],
$$

the `S`-orbits are `{0,1}` and `{2}`, while the `R`-orbit is `{0,2,1}`.
The two relation-image spaces therefore sum to

$$
W_2=\operatorname{span}\{e_0+e_1,e_2\}.
$$

The actions give `Se_2=e_2` and `Re_2=e_1`; hence

$$
A_2e_2=e_2+e_1.
$$

Modulo `W_2`, this is congruent to `-e_0`, which is nonzero because `M_2` is
one-dimensional.  Thus an element of `W_2` has image outside `W_2`.  ∎

### Theorem 9 — primitive-ledger failure

The filled relation quotient is not prime-selective.

**Proof.**  Theorem 4 gives a nonzero primitive cusp survivor for every
modulus, including every prime power and mixed composite.  Lemma 6 shows that
diamond filling does not identify or cancel these block classes; it removes
the cross part and leaves their direct sum.  Lemma 7 shows that the complete
one-dimensional character/supercharacter family does not repair the cusp
survivor.  ∎

### Theorem 10 — analytic ownership failure for the quotient

The Paper 32 graph-step operator does not induce an operator on the global
relation quotient with the original marker.

**Proof.**  An induced map on a quotient `V/W` exists only when the original
map preserves `W`.  Lemma 8 disproves this condition on the `n=2` summand.
Therefore the direct-sum graph-step operator has no induced global quotient
operator.  Any orthogonal projection or scalar block action is a replacement,
not the induced graph-step map.  ∎

### Corollary 11 — branch closure

The candidate has strict Route-A record

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)
```

and the semiring-residue family must close.

**Proof.**  The quotient is built functorially from the source, so the scoped
structural A0 relation remains.  Theorem 9 proves A1 failure before roofs.
Theorem 10 proves failure of same-object quotient determinant ownership.  No
completion, Weil bridge, self-adjoint carrier, or zero correspondence is
present, so A3 and A4 fail.  The inherited stop rule requires closure once a
universal survivor, generic control cancellation, composite residual, or
operator non-descent occurs; all four occur.  ∎

Therefore the six-part claim follows.  ∎

## Corrections or Missing Assumptions

- Characteristic zero is essential for identifying relation images with
  orbit-indicator lines without characteristic-two or characteristic-three
  degeneration.
- The scalar comparison determinant on `direct_sum n^{-s} I_{M_n}` is honest
  as a determinant but is not the determinant of the inherited edge-step
  object.
- No universal assertion is made about every higher-dimensional or nonlocal
  superrepresentation.

## Open Risks

- A new family with a genuine chain endomorphism could evade the operator
  descent obstruction; it would not be a continuation of this frozen object.
- The proof closes the mandated semiring-residue branch, not every possible
  arithmetic groupoid or quantum statistical system.
