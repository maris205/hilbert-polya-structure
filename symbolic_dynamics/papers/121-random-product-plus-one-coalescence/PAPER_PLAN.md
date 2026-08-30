# P121 paper plan — post-owner rewrite

Status: **RESIDUAL CLAIM LOCK / ANONYMOUS REVIEW / EXTERNAL HOLD**.

## One-sentence contribution

For the product-plus-one encoding of the Yule root-configuration statistic,
average an owned fixed-tree cardinality marker in closed form and propagate
the owned first-/second-moment base through a strict unit-residue pole ladder
at every moment order `r>=3`.

## Direct owner and mandatory subtraction

Disanto--Fuchs--Paningbatan--Rosenberg (2022) own the same variable after
the shift `X_n=R_n+1`.  The paper assigns them zero-credit ownership of:

- the Yule/uniform-history split law and exact distribution recursion;
- the root-configuration/nonempty-antichain correspondence;
- the first-moment Riccati equation, closed form, dominant pole, and
  exponential asymptotic;
- the second-moment/variance Riccati and singularity neighborhood; and
- the fact that caterpillars minimize the root-configuration count.

Andriantiana--Wagner--Wang own antichains of specified cardinality on a
fixed rooted-tree poset.  Chang--Fuchs print the same Yule--Harding
`n`-caterpillar probability `2^(n-2)/(n-1)!`, with Rosenberg as the earlier
caterpillar-pattern owner.  The fixed marker, minimum shape, and probability
all receive zero credit.

Generic random-BST, Cartesian-tree, forest-poset, Riccati, Sturm,
Pringsheim, and singularity-analysis machinery also receives zero credit.

## Frozen theorem and ownership contract

1. Under the common boundary-order/ordered-history coupling,
   `X(T)=R(T)+1` objectwise.  This is an identification and subtraction
   lemma, not a contribution claim.
2. For the owned fixed-tree marker `P_T(s)=sum_B s^|B|` over all
   internal-node antichains,
   `A_z=A^2+s/(1-z)^2` and `A=Y_w/Y` with the displayed Euler solution.
   The residual is only the Yule-averaged bivariate transform and its closed
   form; both the fixed marker and specialization `s=1` are owned.
3. For every raw moment,
   `F_r'=sum_(k=0)^r binom(r,k)F_k^2`.  Orders one and two are owned; the
   arbitrary-order triangular interface is a mechanical consequence of the
   owned exact law and receives zero credit.
4. There are radii `1=rho_0>rho_1>rho_2>...` and unit-residue positive
   simple poles.  The residual assertion starts at `r=3`, where Sturm
   comparison gives `rho_r<rho_(r-1)` and Cauchy--Hadamard gives the exact
   exponential limsup.
5. The minimum `X_n=n` and exact mass `2^(n-2)/(n-1)!` for `n>=2` are
   reproduced only as fully owned normalizations.

No full coefficient asymptotic or unique dominant singularity is claimed
for `r>=3`.  No novelty, priority, exhaustive equivalence-class search, or
external-clearance statement is permitted.

## Proof dependencies

1. Boundary survival couples the literal dynamics to a uniform ordered
   history.
2. The owner recurrence `R(T)=(R_L+1)(R_R+1)` and literal recursion
   `X(T)=1+X_L X_R` give `X=R+1` by induction.
3. Averaging the owned fixed-tree marker under the Yule split gives the
   marked Riccati equation; Euler linearization gives the closed form.
4. Binomial expansion gives the zero-credit all-order moment interface.
5. At level `r`, the pole of `F_(r-1)` contributes
   `r/(rho_(r-1)-z)^2`; Sturm comparison forces the next zero earlier.
6. ODE uniqueness gives a simple zero and unit residue; positivity and
   Pringsheim identify the convergence radius; Cauchy--Hadamard gives only
   the limsup.
7. Equality in `xy+1>=x+y` translates the fully owned caterpillar minimum
   and probability into the adjacent-deletion coordinates.

## Evidence and owner gate

The exact verifier checks finite laws, marked coefficients, moment ODEs,
minimum masses, and the owner shift numerically through its stated finite
horizons.  It cannot prove Sturm comparison or ownership.  A bounded search
of the direct owner's citation neighborhood and 2025--2026
root-configuration formulations produced no direct hit for the
Yule-averaged marked transform or a strict `r>=3` continuation of the owned
low-order pole ladder.  This is a search record only; external circulation
remains **HOLD**.
