# Final Proposal

## Title

**Sharp Torus-Coset Decay for Sparse Shift-Like Recurrences**

**Subtitle:** *Constant Anchors and the Exact Zero-Constant Boundary*

## One-sentence contribution

A nonzero constant and two actual nonconstant monomials force an exact loss of
one torus direction per shift-like recurrence in every dimension, while
removing the constant produces a completely classified planar boundary with a
single nonlinear two-step resonance and mandatory third-step closure.

## Exact setup

Let `Omega` be algebraically closed of characteristic zero. Fix

`k>=2`, `1<=nu<=k-1`, `a!=0`,

and define

`S(z_1,...,z_k)=(z_2,...,z_k,P(z_{k-nu+1})+a z_1)`.

In zero-based scalar coordinates,

`x_{n+k}=P(x_{n+k-nu})+a x_n`.                                     (R)

For `m>=0`, the survivor variety `V_m subset G_m^(k+m)` has coordinates
`x_0,...,x_{k+m-1}` and the `m` equations (R) for `0<=n<m`.

For an arbitrary characteristic-zero field `K` and arbitrary finite-rank
`Gamma<=K*`, including infinite torsion, set

`T_m(S,Gamma)={z in Gamma^k:S^j(z) in Gamma^k for 0<=j<=m}`.

Projection from `V_m intersect Gamma^(k+m)` to the initial `k` coordinates is
a bijection onto `T_m`.

## Main theorem A: anchored decay

Assume

`P(X)=c+sum_{j=1}^s b_j X^(e_j)`,

where

`0<e_1<...<e_s`, `a,c,b_j!=0`, and actual collected support `s>=2`.

For every `0<=m<=k` and every connected torus coset

`xi H subset V_m`,

one has

`dim H<=k-m`.                                                        (A)

The theorem is independent of `gcd(k,nu)`.

If `a=1` and `P(1)=0`, equality is attained for every `m` by a connected
saturated subtorus `H_m`. Let

`R_m={n-nu mod k:0<=n<m}`.

Set initial coordinates `x_r=1` for `r in R_m`, impose
`x_{k+n}=x_n`, and leave every other initial coordinate free. This gives

`H_m isomorphic to G_m^(k-m)`.

Laurent's theorem then implies, for every arbitrary finite-rank `Gamma`, that

`T_k(S,Gamma)` is finite.                                            (A-finite)

The threshold is sharp. For every prescribed support, choose
`a=b_j=1,c=-s`, let `Gamma=<2>`, and use `H_{k-1}`. Its unique free initial
index is `q=k-1-nu`; varying `x_q=2^N` gives infinite `T_{k-1}`.

## Main theorem B: exact planar zero-anchor phase

Fix `k=2`, `nu=1`, and `c=0`. Write

`P(X)=sum_{e in E}b_e X^e`

with nonempty actual support `E subset Z_{>=1}`.

### Linear phase

If `E={1}` and `P(X)=beta X`, every `V_m^0` contains a one-dimensional torus
coset. For any root `r` of `r^2=beta r+a`, the coset is

`{(t,rt,...,r^(m+1)t):t in G_m}`.

There is no finite geometric window.

### Unique nonlinear exception

If

`P(X)=beta X+delta X^d`, `d>=2`,

then `V_2^0` has a positive-dimensional connected torus coset if and only if

`a=-beta^2`.

On this locus, the unique such coset is

`C_d={((delta/beta^2)t^d,t,beta t,delta beta^d t^d):t in G_m}`.       (C)

For every coefficient choice, including resonance, `V_3^0` has no
positive-dimensional torus coset.

### All other nonlinear supports

For every other nonlinear support, `V_2^0` has no positive-dimensional torus
coset. This includes nonlinear monomials, binomials whose lower exponent is at
least two, and supports of size at least three.

### Arithmetic corollary

For every arbitrary finite-rank `Gamma<=K*`:

- off the unique nonlinear resonance, `T_2` is finite;
- on the resonance, `T_3` is finite; and
- in the linear phase there is no coefficient-uniform finite geometric
  window.

Geometric resonance does not assert that every `Gamma` meets `C_d` infinitely.
A compatible sharp example is

`beta=delta=1`, `a=-1`, `Gamma=<2>`,

with

`(x_0,x_1,x_2,x_3)=(t^d,t,t,t^d)`, `t=2^N`.

For nonlinear monomial one-step sharpness, the scalar orientation is

`(x_0,x_1,x_2)=(t^e,t,2t^e)`,

not the transposed early candidate tuple.

## Proof architecture

### Common character framework

On a coset `xi H`, write `x_i=xi_i chi_i` with
`chi_i in X*(H)`. Characters are a basis of the group algebra, so a nonzero
singleton is impossible.

### Part A

For the `n`th equation, let `t=k+n-nu`. If `chi_t` is nontrivial, then

`1,chi_t^(e_1),...,chi_t^(e_s)`

are at least three distinct characters, while the two endpoints can cover at
most two. Hence `chi_t=1`. Then:

- `P(xi_t)!=0` forces both endpoints trivial;
- `P(xi_t)=0` forces `chi_{n+k}=chi_n` and
  `xi_{n+k}=a xi_n`.

Every equation therefore contributes

`A_n=epsilon_{k+n-nu}` and `B_n=epsilon_{k+n}-epsilon_n`

to the kernel of the ambient-character map. The `A_n` pivots occupy an
interval of length `m`; each disjoint endpoint pair of `B_n` has an endpoint
outside that interval. This proves all `2m` relations integrally independent
and gives dimension `k+m-2m=k-m`.

The future-copy relations also show that the killed initial residues are the
translation `{n-nu mod k}`, which removes every gcd concern.

### Part B

With no constant, a trivial middle character has two scalar subcases:
nonroot killing and root-copy. A nonlinear monomial gives a two-step relation
`u_1=d^2u_1`, so it closes. At least three powers leave a singleton.

For a binomial `{p,q}`, the complete nontrivial local orientations are

`B: u_n=p u, u_{n+2}=q u`,

`C: u_n=q u, u_{n+2}=p u`.

Together with the trivial-middle label `A`, these exhaust every partition.
All adjacent words containing `A` close. The four nontrivial words require

`pq=1`, `q^2=1`, `p^2=1`, `pq=1`,

respectively. Only `CB` survives, forcing `p=1`. Its two scalar orientations
force `a=-beta^2` and formula (C). A third label would force either `d=1` or
`d^2=1`, so the resonance closes in `V_3^0`.

## Laurent scope

The sole external proof input is Laurent's qualitative torus theorem over
`C`. An arbitrary finite-rank group `Gamma`, even with `mu_infinity`, lies in
the division hull of a finitely generated `Gamma_0`. The field generated by the
coefficients and generators of `Gamma_0` is finitely generated over `Q` and
embeds in `C`; all of `Gamma` is algebraic over it. This proves the
arbitrary-characteristic-zero-field corollary without assuming finite
generation, bounded torsion, or an embedding of the whole ground field.

No effective count is claimed.

## Relation to Paper16

Paper16, `papers/16-henon-support-size-torus-escape`, is terminal and remains a
separate project. It owns the explicit planar anchored bounds:

- `c!=0,s>=2`: finite explicit `T_2`, sharp `T_1`;
- `c!=0,s=1`: absorbed finite explicit `T_4`, sharp `T_3`.

Paper17's anchored `k=2` consequence is weaker and qualitative. Paper17 does
not absorb Paper16. Its standalone mass comes from all-dimensional exact coset
decay and the exact zero-constant boundary. Paper14's support-one result is
already fully absorbed by Paper16 and is neither revived nor reabsorbed here.

## About-22-page article plan

| Section | Substantive pages |
|---|---:|
| 1. Introduction and anchor-loss question | 1.75 |
| 2. Shift-like recurrences, `V_m`, and Laurent bridge | 2.25 |
| 3. Group-algebra and character preliminaries | 2.00 |
| 4. Anchored decay theorem | 4.00 |
| 5. Equality subtori and arithmetic sharpness | 2.00 |
| 6. Zero-anchor local partition calculus | 3.50 |
| 7. Exact resonance and third-step closure | 4.00 |
| 8. Paper16 boundary and examples | 1.50 |
| 9. Related work and limitations | 1.00 |
| **Total** | **22.00** |

This is a content budget, not a demand to stretch typesetting. References are
outside the count; no appendix, code, data, or computational supplement is
needed.

## Locked exclusions

There is no claim about positive characteristic, `a=0`, rational/Laurent
support, arbitrary polynomial automorphisms, affine-conjugacy invariance of
support, all maximal cosets, effective cardinalities, heights, periodic points,
or global priority. `T_m` is never called positive-dimensional, and resonance
is never asserted to meet every fixed `Gamma` infinitely.

## Lifecycle decision

Portfolio-adjusted scores are novelty `8.0/10`, standalone value `8.2/10`, and
proof confidence `9.3/10`. The proposal passes the `7.5/7.5/9.0` gate.

**FINAL PROPOSAL STATUS: AUTHOR COMPLETE / PENDING INDEPENDENT SOURCE REVIEW.**

This status does not authorize manuscript creation, a source lock, a review
artifact, a build, an experiment, or submission.
