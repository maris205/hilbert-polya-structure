# G05 theorem package — random quotient-leakage erosion

**Provisional gate:** `SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL`  
Let `V=F_q^n`, let `T_t` be independent uniform elements of `End(V)`, and
iterate on the full subspace lattice

```text
U_(t+1) = U_t intersect T_t^(-1)(U_t).                    (0)
```

The phrase “quotient leakage” is descriptive only.  No application or novelty
claim is attached to it.

## 1. Quotient reduction and every-target fibre

For a current `a`-space `U`, compose `T|U` with the quotient projection
`V -> V/U`.  This gives a uniform linear map

```text
L_T : U -> V/U,       U intersect T^(-1)(U)=ker L_T.      (1)
```

Fix `B<=U`, `dim B=b`, and put `d=a-b`.  A quotient map has kernel exactly
`B` precisely when the induced map `U/B -> V/U` is injective.  Consequently

```text
C_nq(a,b)
 = 1_(d<=n-a) product_(i=0)^(d-1)(q^(n-a)-q^i)           (2)
```

quotient maps give that endpoint, and

```text
P(U,B)=1_(B<=U) C_nq(a,b)/q^(a(n-a)).                    (3)
```

If full ambient endomorphisms are counted, the exact fibre is

```text
#{T in End(V): U intersect T^(-1)(U)=B}
 = q^(n^2-a(n-a)) C_nq(a,b).                             (4)
```

Thus (4), not a bounded enumeration, is the proposed every-target inverse
axis.  The verifier independently enumerates all subspaces and all binary
matrices through `n=3`.

## 2. Size quotient and all-time targets

Let `[r choose s]_q` denote the Gaussian coefficient.  The dimension chain is

```text
Q_ab = [a choose b]_q C_nq(a,b)/q^(a(n-a)).               (5)
```

The finite-field kernel-nullity identity makes every row sum one.  Since (0)
is nested and `GL(V)`-equivariant, for every `t>=0` and fixed `B<=U`,

```text
P^t(U,B)=(Q^t)_(a,b)/[a choose b]_q.                      (6)
```

No target outside `U` is reachable.  Equations (4)--(6) give the complete
finite transition/fibre interface.

## 3. Algebraic spectrum and complementary Jordan ladder

On every exact `a`-space, the self-loop probability is the probability that
`L_T=0`:

```text
lambda_a=q^(-a(n-a)).                                    (7)
```

Ordering all subspaces by dimension gives the complete algebraic spectrum

```text
{lambda_a with multiplicity [n choose a]_q: 0<=a<=n}.     (8)
```

The only equalities among the numbers in (7) are
`lambda_a=lambda_(n-a)`.  The size quotient has the following full Jordan
pattern:

- eigenvalue `1=lambda_0=lambda_n` has two one-dimensional blocks, because
  zero and `V` are separate absorbing states;
- if `n` is even, `lambda_(n/2)` has one one-dimensional block; and
- for every `1<=b<n/2`, the pair `b,n-b` contributes one `J_2` block at
  `q^(-b(n-b))`.

**Proof route for the nonzero coupling.**  Set `a=n-b`.  Between diagonal
positions `b` and `a`, strict concavity of `x(n-x)` gives
`lambda_k<lambda_b` for `b<k<a`.  In an eigenvector recursion starting at
position `b`, every intermediate coordinate is positive: denominators
`lambda_b-lambda_k` and adjacent transition entries `Q_(k,k-1)` are positive.
The compatibility equation at row `a` therefore has a strictly positive left
side and cannot be satisfied.  The eigenvector born at `b` is lost, leaving
geometric multiplicity one for algebraic multiplicity two.  A length-two
Jordan block follows.  The verifier checks the corresponding nullities
`(1,2)` for all complementary pairs at

```text
q=2, 1<=n<=8;     q=3,5, 1<=n<=7.                        (9)
```

This is a proof obligation worth preserving: the resonance is forced by
complementary dimensions, including indirect coupling when the one-step
`a -> b` transition itself is zero.

## 4. Absorption and boundaries

The subspaces `0` and `V` are fixed.  Every proper nonzero `U` has positive
probability of strict dimension loss, so it reaches zero almost surely.  For
`0<a<n`,

```text
Pr_a(tau_0<=t)=(Q^t)_(a,0),                              (10)
E_a tau_0=[1+sum_(b<a)Q_ab E_b]/(1-Q_aa).                (11)
```

The Jordan blocks above force polynomial-exponential terms in (10).

- `n=0`: one fixed zero space.
- `n=1`: exactly `0,V`, both fixed; there is no transient layer.
- `n=2`: the only transient dimension is one,
  `Q_(1,0)=(q-1)/q`, `Q_(1,1)=1/q`; there is no paired transient Jordan block.
- `n=3`: dimensions two and one give the first direct `J_2`, at eigenvalue
  `q^-2`.

## 5. Owner and internal subtraction

The following receive zero credit:

1. rank/nullity counts for uniform finite-field matrices, including Balakin
   and Fulman--Goldstein;
2. Gaussian subspace incidence and the count of injective maps;
3. generic triangular-chain absorption and Jordan linear algebra;
4. P109's full subspace-lattice carrier and Gaussian pointed fibres;
5. P162's random-intersection/absorption language, P165's code shortening,
   and P168's inverse-span carrier.

The residual under test is only the literal state-dependent quotient map (1),
its exact ambient fibres (4), every-time targets (6), and the complementary
Jordan ladder.  `G01` in the same scout uses `U intersect T(U)` instead; its
diagonal is `abs(GL_a(q))/q^(na)` and has no complementary resonance.  This
separates the literals but does not justify allocating both to one five-paper
batch.

The bounded exact-phrase search found no literal owner.  That result is
recorded only as a non-hit.  A direct quotient-kernel Markov-chain owner or a
hostile finding that the Jordan ladder is a routine repackaging must kill or
demote this candidate.
