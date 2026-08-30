# Narrative and derivation report — P121 owner rewrite

Status: **MATHEMATICALLY COHERENT / DIRECT OWNER SUBTRACTED / EXTERNAL HOLD**.

## The correction that changes the paper

The adjacent merger does not define an unrecognized random-tree statistic.
For an ordered history `T`, let `R(T)` be its number of root ancestral
configurations and let `X(T)` be the product-plus-one evaluation.  The
direct owner's recurrence is

```text
R(leaf)=0,
R(T)=(R(T_L)+1)(R(T_R)+1).
```

The merger evaluation satisfies

```text
X(leaf)=1,
X(T)=1+X(T_L)X(T_R).
```

Induction gives `X(T)=R(T)+1` for every ordered history.  Consequently the
split law, complete finite distribution, unmarked antichain count, mean,
and second-moment neighborhood are owned by Disanto et al. (2022) and are
used only as an interface.

## Marked refinement

For the internal-node ancestry poset, set

```text
P_T(s)=sum_B s^|B|,
```

including the empty antichain.  Root inclusion contributes `s`; root
exclusion independently chooses antichains in the two subtrees, so
`P_T=s+P_L P_R`.  At `s=1`, this is exactly the owned statistic plus its
empty antichain.  Andriantiana--Wagner--Wang already own fixed-tree
antichains of specified cardinality and the equivalent root-subtree leaf
statistic.  Averaging this owned marker under the Yule split yields the
residual refinement

```text
A_z=A^2+s/(1-z)^2,  A(0,s)=1.
```

With `w=1-z`, `delta=sqrt(1-4s)`, and
`beta_±=(1±delta)/2`, the Euler solution

```text
Y=(beta_+ w^beta_+ - beta_- w^beta_-)/delta
```

gives `A=Y_w/Y`.  Thus `[z^(n-1)s^k]A` is the exact expected number of
cardinality-`k` antichains.

## Higher-moment continuation

For `F_r=sum_(n>=1) E[X_n^r]z^(n-1)`, binomial expansion gives

```text
F_r'=sum_(k=0)^r binom(r,k)F_k^2.
```

This identity is a mechanical binomial expansion of the direct owner's exact
law and receives zero contribution credit; orders one and two are also
analyzed explicitly there.  At any later level write
`F_r'=F_r^2+G_r` and `F_r=-U_r'/U_r`.  If the preceding level has the
unit-residue pole at `rho_(r-1)`, then

```text
G_r(z)=r/(rho_(r-1)-z)^2+O((rho_(r-1)-z)^(-1)).
```

Because `r>1/4`, comparison with an oscillatory Euler equation forces a
zero of `U_r` before `rho_(r-1)`.  ODE uniqueness makes the first zero
simple, hence the new pole has residue one.  Positive coefficients and
Pringsheim exclude a smaller convergence radius.  This yields the strict
ladder and the exact limsup for every `r>=3`; it does not exclude other
singularities on the same circle.

## Endpoint atom

Both the caterpillar minimizer and its probability are owned background:
Chang--Fuchs print the same Yule--Harding formula, after Rosenberg's earlier
caterpillar analysis.  In the literal encoding,
`xy+1>=x+y`, with equality only if one factor is one, forces an endpoint
split at each stage.  There are `2^(n-2)` such planar deletion orders among
`(n-1)!`, reproducing the exact minimum mass.  This is retained solely as a
fully owned extremal normalization.

## Evidence boundary

The verifier independently evaluates literal histories and split-law
dynamic programs, then checks marked polynomials, raw-moment equations,
and the coefficient artifact.  Those finite tests cannot prove an infinite
pole ladder or an owner statement.  The focused residual search is a bounded
non-hit, not a clearance certificate.  External release remains **HOLD**.
