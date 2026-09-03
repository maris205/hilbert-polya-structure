# Theorem pressure tests for A01, A03, and A16

These are independent derivations for the three cleanest signals in the
algebra/arithmetic lane.  They are not paper allocations or novelty claims.
In fact, all three fail the present collision gate.

## A01: Frobenius meet on the subspace lattice

Let `V=F_{q^m}`, viewed as an `m`-dimensional vector space over `F_q`, and let
`F(x)=x^q`.  On the complete subspace lattice define

\[
  M(U)=U\cap F(U).
\]

### Exact forward theorem

For every `t>=0`,

\[
  M^t(U)=\bigcap_{i=0}^{t}F^i(U).                 \tag{1}
\]

This follows immediately by induction, using that `F` preserves
intersections.  Since `F^m=1`, the orbit stabilizes by time `m-1` at

\[
  C(U)=\bigcap_{i=0}^{m-1}F^i(U),
\]

the largest Frobenius-invariant subspace contained in `U`.  Inclusion can
only decrease, so every directed cycle is a fixed point.

The upper bound `m-1` is sharp.  In a normal basis
`e_0,...,e_{m-1}` with `F(e_i)=e_{i+1}`, take the coordinate hyperplane
`U={x:[e_0]x=0}`.  The intersections in (1) impose one new independent
coordinate equation at each of the first `m-1` updates and end at zero.

The Frobenius module is cyclic:

\[
  V\simeq F_q[X]/(X^m-1).
\]

If `X^m-1=prod_j phi_j(X)^{e_j}` is its monic irreducible factorization,
then invariant subspaces correspond to ideals of this quotient.  Hence

\[
  \#\operatorname{Fix}(M)=\prod_j(e_j+1),\qquad
  \zeta_M(z)=(1-z)^{-\prod_j(e_j+1)}.             \tag{2}
\]

The multiplicities in (2) matter when the characteristic divides `m`; no
semisimplicity assumption is hidden.

### Every-target, every-time fibre theorem

Let

\[
  G_d(q)=\sum_{j=0}^{d}{d\brack j}_q
\]

be the number of subspaces of `F_q^d`, and for a target `W` put

\[
  L_t(W)=\sum_{i=0}^{t}F^{-i}(W).
\]

For any subspace `W`, the number of `U` satisfying
`W <= M^t(U)` is exactly `G_{m-dim L_t(W)}(q)`: the containment is equivalent
to `L_t(W)<=U`.  Möbius inversion on the full subspace lattice therefore
gives

\[
 \boxed{
 \#\{U:M^t(U)=W\}
 =\sum_{K\ge W}
   (-1)^r q^{\binom r2}
   G_{m-\dim L_t(K)}(q),\quad r=\dim K-\dim W .}
                                                            \tag{3}
\]

Thus the inverse axis is not merely a total basin count.  Formula (3) handles
every target, including targets outside the image, at every time.

For invariant `W` and `t>=m-1`, (3) specializes to the terminal-basin
formula.  Equivalently, if `B_W` counts states whose terminal core is exactly
`W`, then

\[
  B_W=\sum_{K\ge W,\,F(K)=K}
       \mu_{\mathrm{Inv}(F)}(W,K)G_{m-\dim K}(q).            \tag{4}
\]

Equation (4) is inversion on the invariant-subspace poset, whereas (3) is
inversion on the full subspace lattice.

### Boundary and machine pressure

- `m=1` has height zero; `m=2` has height one.  The hyperplane construction
  above covers all `m>=2`.
- The tempting false formula “the fixed count depends only on `m`” is killed
  by `m=4`: the verifier sees 5 fixed spaces over `F_2` and 8 over `F_3`.
  Factorization (2) explains the difference.
- Full graphs were enumerated for `(q,m)=(2,3..6),(3,3),(3,4),(5,3)`.
  Formula (3) was checked for every target and all `0<=t<m` for binary
  `m<=5` and all three odd-prime controls.  The largest full graph has 2,825
  states.

### Collision verdict

The literal finite-field carrier was not found in the local paper list, but
the proof is not independent.  Equation (1) is precisely the meet-dual of the
semilattice orbit-join identity used by P110.  P128 explicitly treats its
translation--GCD map as the order-dual semilattice orbit fold and retains an
orbit Euler product/fibre refinement only after subtracting that engine.
Equations (3)--(4) are ordinary lattice Möbius inversion, also central to the
P110 basin argument.  Consequently the whole two-axis package transfers:
`KILL_INTERNAL_P110_P128`.

Brickman--Fillmore's invariant-subspace-lattice paper is relevant background
for (2), not evidence that this exact self-map is unowned.  A bounded literal
search non-hit does not change the internal verdict.

## A03: derivative--GCD erosion in characteristic p

Let `q` be a prime power of characteristic `p`, let `X_n` be all monic
polynomials of degree at most `n`, and define

\[
  D(f)=\gcd(f,f'),
\]

with monic GCD and `D(1)=1`.

### Factor-exponent theorem

Write `f=prod_P P^{e_P}` over monic irreducibles.  Finite fields are perfect,
so `P'` is nonzero.  Reducing the product rule modulo `P` gives

\[
 v_P(D(f))=
 \begin{cases}
 e_P-1,&p\nmid e_P,\\
 e_P,&p\mid e_P.
 \end{cases}                                               \tag{5}
\]

If `r_P` is the least residue of `e_P` modulo `p`, induction on (5) yields

\[
  v_P(D^t(f))=e_P-\min(t,r_P).                              \tag{6}
\]

Hence

\[
 \operatorname{depth}(f)=\max_P(e_P\bmod p),\qquad
 H_{p,n}=\min(n,p-1).                                      \tag{7}
\]

The fixed polynomials are exactly `F_q[x^p]`, so their number in `X_n` is
`sum_{d=0}^{floor(n/p)}q^d`.  All cycles are fixed.

### Factor-degree depth and fibre series

Let `I_q` be the set of monic irreducibles and write `d(P)=deg P`.  The
cumulative number of states of depth at most `r`, for `0<=r<p`, is

\[
 [z^{\le n}]\prod_{P\in I_q}
 \frac{1+z^{d(P)}+\cdots+z^{r d(P)}}{1-z^{p d(P)}}.         \tag{8}
\]

For a time `t`, define

\[
 \phi_t(e)=e-\min(t,e\bmod p),\qquad
 E_t(b)=\{e\ge0:\phi_t(e)=b\}.
\]

For a target `g`, every prime coordinate is independent, and its complete
time-`t` fibre is

\[
 \boxed{
 |(D^t)^{-1}(g)|=[z^{\le n}]
 \prod_{P\mid g}\left(\sum_{e\in E_t(v_P(g))}z^{e d(P)}\right)
 \prod_{P\nmid g}\left(1+\sum_{e=1}^{\min(t,p-1)}z^{e d(P)}\right).} \tag{9}
\]

The degree truncation makes both formal products finite coefficientwise.
Formula (9) also returns zero for targets outside the time-`t` image.

### Boundary and machine pressure

- The naive characteristic-zero rule “every positive exponent drops by one”
  is false at multiples of `p`; (5) is the corrected rule.
- At `p=2` every orbit stabilizes after one step.  When `p>n`, (7) reduces to
  the usual largest-multiplicity clock capped by the degree.
- The verifier factors every polynomial in `(p,n)=(2,8),(3,6),(5,4)` and
  checks (6) statewise.  It compares (8) with every depth CDF and (9) with
  every target for every `1<=t<p`.  Representative cumulative rows are
  `13,823,1093` for `(3,6)` and `1,626,751,776,781` for `(5,4)`.

### Explicit comparison with P142

P142 reduces one prime-power divisor coordinate to the tent-like update
`a -> min(2a,e-a)`, with a recurrent band, two inverse branches, and an
odd-prime equal-valuation boundary.  A03 instead has monotone coordinate rule
`e -> e-1_{p does not divide e}`, a fixed multiple-of-`p` floor, and a product
over irreducible degrees.  The two literal maps are not conjugate.  They do,
however, share the generic valuation-product and every-target-fibre toolkit,
which supplies no separation credit.

The decisive obstruction is stronger than P142 similarity: A03 is the exact
`PDG/SFE/DGD` derivative--GCD map already recorded, with essentially (6),
(8), and target Euler products, in the P127, P152, P157, and P162 scouting
artifacts.  Yun's square-free-decomposition work owns the algebraic primitive.
Verdict: `KILL_DIRECT_OWNER_REPEAT`.

## A16: commutator with a fixed transposition

Fix `a=(1 2)` in `S_n` and define

\[
  T(g)=g^{-1}ag\,a.
\]

For `b=g^{-1}ag`, let `r=|supp(a) cap supp(b)|`.  Every `b` is a
transposition, and every transposition has exactly `2(n-2)!` conjugators.

### Complete functional graph

The image consists of `ba` over all transpositions `b`, so it has
`binom(n,2)` states.  Its three support types are:

| `r` | number of image targets | target type | next state |
|---:|---:|---|---|
| 2 | 1 | identity | identity |
| 1 | `2(n-2)` | 3-cycle supported on `{1,2}` and one new point | itself |
| 0 | `binom(n-2,2)` | product of two disjoint transpositions | identity |

Thus, for `n>=4`, all cycles are fixed, the sharp height is two, and

\[
 \begin{aligned}
 D_0&=2n-3,\\
 D_2&=2(n-2)!\binom{n-2}{2},\\
 D_1&=n!-D_0-D_2,\\
 \zeta_T(z)&=(1-z)^{-(2n-3)}.                              \tag{10}
 \end{aligned}
\]

At time one, each image target has fibre size `c_n=2(n-2)!`.  At every
`t>=2`,

\[
 |(T^t)^{-1}(h)|=
 \begin{cases}
 (1+\binom{n-2}{2})c_n,&h=1,\\
 c_n,&h\text{ is one of the }2(n-2)\text{ fixed 3-cycles},\\
 0,&\text{otherwise}.
 \end{cases}                                               \tag{11}
\]

For `n=2,3`, the disjoint-support row is absent and the sharp height is one;
the count formulas otherwise specialize correctly.

### Fixed-point-marked conjugator fibres

The possible nontransferable axis was not the uniform fibre size, but the
number of fixed points of the conjugator itself.  For a target `ba`, define

\[
  \mathcal F_{n,r}(u)=
  \sum_{g:\,g^{-1}ag=b}u^{\operatorname{fix}(g)}.
\]

Put `N=n-2`, `s=n-4+r`, and

\[
 Q_{N,s}(u)=\sum_{j=0}^{s}\binom{s}{j}(u-1)^j(N-j)!.
\]

This is the partial-rencontres polynomial for a bijection between two
`N`-sets whose intersection contains `s` labels eligible to be fixed.  The
two endpoint bijections contribute

\[
 P_0(u)=2,\qquad P_1(u)=1+u,\qquad P_2(u)=1+u^2.
\]

Consequently

\[
  \boxed{\mathcal F_{n,r}(u)=P_r(u)Q_{n-2,n-4+r}(u).}       \tag{12}
\]

Indeed, a conjugator maps `supp(b)` bijectively to `supp(a)`.  The endpoint
part has the three polynomials `P_r`; its complement is an arbitrary
bijection between two `(n-2)`-sets with exactly `n-4+r` common labels.
Ordinary marked inclusion--exclusion gives `Q`, and the choices are
independent.

The verifier enumerates all of `S_4,S_5,S_6`, checks (10)--(11), and compares
(12) coefficient by coefficient for every target.  For example, the `S_6`
rows for `r=0,1,2` are respectively

```text
(28,16,4)
(11,20,12,4,1)
(9,8,15,8,7,0,1)
```

where entry `k` counts conjugators with `k` fixed points.

### Owner and collision verdict

Brandl's *The commutator map* is broad direct background.  More closely,
Fulman (2024) studies fixed-point distributions of `g^{-1}x^{-1}gx` for
uniform `g` and fixed `x`.  Fulman's statistic marks the commutator output,
whereas (12) marks the conjugator conditional on a specified output, so no
claim is made that Fulman literally states (12).

That residual distinction is still insufficient internally.  P119 already
uses the same fixed-second-variable twisted coboundary
`g -> g^{-1}phi(g)` and proves its fibres by centralizer cosets.  Here the
entire forward graph follows after classifying the overlap of two
transpositions, and the extra mark factors into a two-point polynomial and a
standard partial-rencontres polynomial.  Neither proof engine is
nontransferable at paper scale.  Verdict: `KILL_INTERNAL_P119_TRANSFER`.

## Final pressure decision

All three conjectural theorem spines survived mathematical pressure, but none
survived collision/ownership pressure.  The correct recommendation is an
empty green pool, not a weakened novelty claim.
