# Phase-3 algebraic novelty/owner gate

**Role:** independent hostile owner review  
**Systems checked:** R1, A10, A1, A5 only  
**Search cutoff:** 2026-08-30  
**External status:** `HOLD_EXTERNAL`  
**Meaning of a no-hit:** bounded no-hit only; never a novelty or priority claim

## Executive gate

The current four-way gate is **one cautious reserve and three abandons**.  The
score is the strength of a theorem-level residual *after* owner subtraction,
not confidence that the computations are correct.

| system | exact closest owner | residual after subtraction | score | gate | selection action |
|---|---|---|---:|---|---|
| **R1**, ordered-DAG `A -> A+A^2` | Wadsanthat--Panraksa on the literal scalar polynomial `x^2+x`, plus standard linearized-polynomial composition | the literal ordered-DAG permutation and a possible **enumeration/structure theorem for exact period strata**; no such theorem is in the current contract | **6/10** | **CAUTION** | reserve for one focused census/structure spike; do not freeze from the present claims |
| **A10**, Young `UD` modulo `p` | Cai--Stanley, Smith form of `DU+xI` over `Z[x]` for Young's lattice | no non-mechanical temporal theorem located | **1/10** | **ABANDON** | kill the candidate as stated |
| **A1**, Boolean zeta modulo `p` | modular `C_p` tensor-product/Green-ring recurrence, already classical and restated explicitly by Elmer--Kadr (2026) | only the particular wording of the first `+1` threshold; it is an immediate recurrence corollary | **2/10** | **ABANDON** | kill the candidate as stated |
| **A5**, coupled shifted Cartier | Norman's complete prime-characteristic Kronecker-sum Jordan theory, plus internal P115 for the one-coordinate chains | coefficient-index bookkeeping only | **1/10** | **ABANDON** | kill the candidate as stated |

No 2025--2026 source located the exact ordered-DAG update in R1.  That is a
bounded no-hit, not evidence of novelty.  Conversely, the current-window
search strengthened the negative gate for A1: Elmer--Kadr, published June
2026, states the exact `V_i tensor V_2` recurrence that makes the advertised
threshold a short calculation.

## R1. Ordered-DAG parity two-path toggling

### Claims extracted

1. On strict upper-triangular `A in M_n(F_2)`, `T(A)=A+A^2` toggles `i -> j`
   exactly when the number of directed two-step witnesses from `i` to `j` is
   odd.
2. For every `t >= 0`,
   `T^t(A)=sum_(j binary-submask-of t) A^(2^j)`.
3. If `r(A)` is the nilpotency index, the point period is the least `2^s`
   with `2^(2^s) >= r(A)`; in particular every state is periodic from time
   zero.
4. The maximum period on size `n` is the least `2^s` with
   `2^(2^s) >= n`, attained by the single directed path/Jordan shift.

### Closest owners and subtraction

- [Atsanon Wadsanthat and Chatchawan Panraksa, *Distribution of cycle
  lengths of a quadratic map over finite fields of characteristic 2*,
  Fibonacci Quarterly 57 (2019), 35--44](https://murex.mahidol.ac.th/en/publications/distribution-of-cycle-lengths-of-a-quadratic-map-over-finite-fiel/)
  is the exact scalar-polynomial owner: its abstract explicitly studies
  `x -> x^2+x` as a dynamical system, its linearity, nilpotent points, and
  cycle lengths.
- [Wu and Liu, *Linearized polynomials over finite fields revisited*](https://arxiv.org/abs/1211.5475)
  owns the composition algebra of linearized polynomials.  The submask
  iterate is simply the binomial expansion of `(I+F)^t` in characteristic
  two, with `F^j(x)=x^(2^j)`.
- The adjacency interpretation of `A^2` as the number of two-walks is
  classical graph-matrix background.  Searches for the *iterated update*
  rather than merely graph squaring produced no direct hit.

The noncommutative phase space does not by itself rescue Claims 2--4.  Along
the orbit of a given `A`, every iterate lies in the one-generated commutative
algebra `F_2[A]`, so the scalar polynomial-composition identity transfers
verbatim.  The minimal polynomial of a nilpotent matrix is `x^r`; hence its
powers below `r` are independent, and the least positive submask immediately
gives the displayed period.  The path matrix then gives the maximum.  These
are correct specializations, but they are not yet a substantial second
engine.

### Residual delta and hostile objection

The bounded residual is the **literal labelled ordered-DAG permutation** and
the possibility of a nontrivial theorem describing or counting

`{A : period(A)=2^s}`

in graph language.  Such a result would amount to an exact distribution of
nilpotency indices of strict upper-triangular binary matrices, or an equally
strong parity-path characterization.  It is not present in the current four
claims.  Fibre claims cannot help: the displayed period theorem already makes
`T` a permutation, so every fibre is a singleton.

**Strongest reviewer objection.**  “The paper evaluates an already studied
additive polynomial at a nilpotent adjacency matrix; each orbit is contained
in `F_2[A]`, and the DAG paragraph merely visualizes matrix multiplication.”

**Gate:** **6/10, CAUTION.**  Reserve only for a focused exact-period-layer
census or a comparably nontrivial structural theorem.  If that spike reduces
again to nilpotency index plus a path witness, abandon.

Bibliographic caution: the DOI string carried in the scouting note did not
independently resolve in this audit.  The verified institutional record above
should be used until the DOI metadata is corrected.

## A10. Young up--down dynamics modulo `p`

### Claims extracted

1. The remove-then-add corner matrix on partitions of `n` is
   `UD_n=U_(n-1)D_n`, equivalently `Ind Res` on the characteristic-zero
   representation-ring basis.
2. In characteristic zero its eigenvalues and multiplicities are the
   classical differential-poset spectrum.
3. At `n=p`, zero is not semisimple; experimentally
   `nullity(T^2)=nullity(T)+1` for `p=2,3,5,7`.
4. A proposed paper would seek all power kernels, modular Jordan blocks, and
   the resulting finite-linear temporal census.

### Exact owner and decisive subtraction

[Cai and Stanley, *The Smith Normal Form of a Matrix Associated with Young's
Lattice*](https://arxiv.org/abs/1502.00922) (published as
[Proc. AMS 143 (2015), 4695--4703](https://doi.org/10.1090/proc/12642))
prove the Smith normal form of `DU_n+xI` **over `Z[x]`** for Young's lattice.
This is much stronger than an integer Smith form of one numerical matrix.
Because

`DU_n - UD_n = I`, 

substitution of the polynomial variable gives the characteristic Smith form
of the candidate `UD_n`.  The unimodular transformations over `Z[x]` remain
unimodular after reduction modulo `p`; over `F_p[x]` the resulting invariant
factors give the rational canonical form and, here, the complete split Jordan
form.  Consequently they determine every `nullity(T^k)`, including the
advertised length-two zero block at `n=p`.

[Shah, *Smith normal form of matrices associated with differential posets*
(2024; online 2025)](https://doi.org/10.5802/alco.393) explicitly connects
these Smith forms to integral canonical forms and extends the existence result
to a wider class of differential posets.  [Liu and Smith (2021)](https://doi.org/10.37236/10099)
also characterize the algebra generated by the local up/down operators; this
is background rather than the decisive owner.

### Residual delta and hostile objection

No theorem-grade delta remains.  Translating known invariant factors into
power-kernel formulas, fixed-point counts, cycle counts, or a zeta function is
finite-linear bookkeeping and is zero-credit under the internal firewall.
This is not merely “close to SNF”: the polynomial Smith form is precisely the
object that encodes the modular Jordan structure sought by the candidate.

**Strongest reviewer objection.**  “Your main modular resonance is already a
corollary of the published `Z[x]` Smith form of the same Young-lattice
operator, after the elementary shift `UD=DU-I`.”

**Gate:** **1/10, ABANDON.**

## A1. Boolean-lattice zeta transform modulo `p`

### Claims extracted

1. The Boolean zeta matrix is
   `Z_n=J_2(1)^(tensor n)` after ordering each subset coordinate by
   membership, and `(Z^m)_(S,A)=m^|S\A|` for `A subseteq S`.
2. `Z^p=I`; hence the only orbit lengths are `1` and `p`.
3. For odd `p`, `dim ker(Z-I)=binom(n,floor(n/2))` through `n=2p-2`.
4. At the first claimed modular threshold,
   `dim ker(Z-I)=binom(2p-1,p-1)+1`.

### Exact engine owner and subtraction

Regard `J_2(1)` as the generator action on the two-dimensional
indecomposable `C_p`-module `V_2`.  Then the candidate is exactly the diagonal
`C_p` action on `V_2^(tensor n)`, and fixed-space dimension is the number of
indecomposable summands.

The classical cyclic-`p` Green-ring calculation is already complete.  A
particularly explicit current primary source is [Jonathan Elmer and Kazal
Kadr, *Some formulae relating modular representations of elementary abelian
p-groups* (published 4 June 2026)](https://doi.org/10.1007/s13366-026-00855-9).
Its Section 2.3 states that each indecomposable `V_i` has a one-dimensional
fixed space and displays

`V_i tensor V_2 = V_(i-1) direct-sum V_(i+1)` for `i<p`,  
`V_p tensor V_2 = V_p direct-sum V_p`.

The paper identifies this as the classical cyclic-order-`p` result of
[Almkvist and Fossum](https://doi.org/10.1007/BFb0064842).  Iterating the two
displayed rules from `V_1` gives the ordinary Clebsch--Gordan walk until the
wall `V_p` is met and doubles at that wall.  Counting summands yields the
central binomial sequence through `2p-2` and the first excess `+1` at
`2p-1`.  Thus Claims 3--4 are not an independent Boolean-lattice mechanism;
they are a short specialization of the owned recurrence.  Claim 2 is the
standard fact that the cyclic generator has order `p`.

The bounded search did **not** locate a source printing the exact sentence
“central binomial through `2p-2`, then `+1` at `2p-1`.”  This is only a bounded
no-hit for that wording.  It does not create a defensible theorem delta when
the published recurrence proves it immediately.

### Residual delta and hostile objection

After subtraction, only the Boolean-zeta presentation and the convenient
first-threshold corollary remain.  All functional-graph conclusions follow
from the same Jordan decomposition and generic finite-linear dynamics.

**Strongest reviewer objection.**  “After the identity
`Z_n=J_2(1)^(tensor n)`, the paper is an example sheet for the cyclic
`p`-group Green ring; even the `+1` anomaly is the first boundary reflection
of the published `V_i tensor V_2` recurrence.”

**Gate:** **2/10, ABANDON.**  A different phase restriction might pose a new
problem, but that would be a new candidate rather than a repair of A1.

## A5. Coupled shifted-Cartier sum

### Claims extracted

1. Each shifted coordinate Cartier map decomposes the bounded exponent set
   into finite nilpotent index chains.
2. The maps commute, and powers of `T=C_x+C_y` have binomial coefficients
   as path weights.
3. The sharp nilpotency depth is one plus the last feasible carry-free
   binomial cell; for example the naive `17` becomes `15` at `(p,h)=(5,8)`.
4. A proposed paper would seek all power ranks/fibres, a closed depth law,
   and parameter recovery from the temporal data.

### Exact owner and decisive subtraction

After restriction of scalars from `F_q` to `F_p` and reordering coefficient
indices by their Cartier chains, the candidate has the form

`sigma^(-1) tensor (N_x tensor I + I tensor N_y)`,

where `sigma` is invertible and `N_x,N_y` are direct sums of nilpotent Jordan
blocks.  The invertible Frobenius factor does not change kernels or
nilpotency depth.  Every pair of index chains is therefore exactly a
prime-characteristic Kronecker sum.

[C. W. Norman, *On Jordan bases for the tensor product and Kronecker sum and
their elementary divisors over fields of prime characteristic*](https://doi.org/10.1080/03081080701395640),
Linear and Multilinear Algebra 56 (2008), 415--451, gives an inductive Jordan
basis and specifies all elementary divisors and their multiplicities from the
`p`-adic expansions of the two block sizes.  That result determines the
largest block, every power rank, every fibre size, and the whole nilpotent
functional graph of every chain pair.  Lucas carry language is an alternative
description of the same owned Jordan partition, not a second mechanism.

Multivariate coefficient-selection Cartier operators themselves are standard;
for a recent explicit bivariate definition see [Rowland, Stipulanti and
Yassawi, *Algebraic power series and their automatic complexity I: finite
fields*](https://arxiv.org/abs/2308.10977).  Internally, P115 already owns the
one-coordinate shifted-Cartier chain decomposition and its temporal census.

### Residual delta and hostile objection

Only the multiplicities with which the elementary index chains occur remain
to be tabulated.  Feeding those elementary digit counts into Norman's theorem
is mechanical substitution.  Parameter recovery from the resulting list is
also not an independent dynamical theorem unless a genuinely new inverse
problem survives the full Jordan partition, and none is presently stated.

**Strongest reviewer objection.**  “Once the coefficients are reordered,
Cartier terminology disappears: the operator is a direct sum of precisely
the modular Kronecker sums whose Jordan bases and elementary divisors Norman
already computed.”

**Gate:** **1/10, ABANDON.**

## Query-formulation audit

The following are representative literal queries actually used.  Each claim
group was attacked in at least three vocabularies: literal update, structural
algebra/representation theory, and owner/result language.  Year-qualified
queries were rerun for the 2025--2026 window.

| claim group | three representative formulations |
|---|---|
| R1-C1, literal graph update | `"A+A^2" "strictly upper triangular" iteration finite field`; `"A^2+A" strictly upper triangular matrix graph`; `graph transformation toggle edge odd number of directed two-paths parity` |
| R1-C2, iterate | `"x+x^2" additive polynomial iterates Lucas theorem`; `"linearized polynomial" "x^2+x" iteration finite field`; `"A -> A+A^2" nilpotent matrix` |
| R1-C3, point periods | `"x^2+x" functional graph finite field characteristic 2`; `"functional graph" "x^2+x" finite field`; `iteration of x+x^2 on nilpotent rings characteristic 2` |
| R1-C4, exact/recent owner | `2025 2026 "A+A^2" matrix finite field`; `2025 2026 polynomial matrix dynamics upper triangular finite field nilpotent`; `2025 2026 additive polynomial dynamics finite algebras characteristic 2` |
| A10-C1, literal `UD` | `"Young lattice" "up-down operator" characteristic p`; `"Ind Res" symmetric group Young lattice modulo p operator`; `"up-down operator" "Young's lattice" Smith normal form` |
| A10-C2, integral owner | `Cai Stanley Smith normal form matrix Young lattice up down`; `"Smith normal form" "Young's lattice" differential poset DU`; `Shah 2024 Smith normal form differential posets 10.5802/alco.393` |
| A10-C3, modular Jordan | `"p_1 d/dp_1" modular Jordan form symmetric functions`; `"UD" Young lattice modulo p kernel powers`; `"up-down" Young lattice "Jordan form"` |
| A10-C4, recent window | `2025 2026 Young lattice up down operator modular Jordan form`; `"Young lattice" "up-down" modulo p Jordan form`; `"Ind Res" Young lattice characteristic p canonical form` |
| A1-C1, literal zeta | `"Boolean lattice" zeta matrix Jordan form characteristic p`; `"Boolean algebra" incidence matrix modular Jordan canonical form`; `"zeta transform" Boolean lattice modulo p order p` |
| A1-C2, tensor identification | `tensor powers V_2 cyclic group order p decomposition indecomposable`; `"V_2" tensor power modular representation cyclic p-group`; `"tensor powers" "indecomposable" "cyclic p-group" Jordan block 2` |
| A1-C3, fixed dimension | `fixed space dimension tensor power V2 cyclic group p central binomial coefficient`; `"number of indecomposable summands" "V_2" tensor power`; `"tensor power" 2-dimensional indecomposable representation C_p fixed points` |
| A1-C4, threshold/recent owner | `"central binomial" "V_2" cyclic p group tensor`; `2025 2026 tensor powers cyclic p group indecomposable V2`; `2025 2026 Boolean lattice zeta operator characteristic p` |
| A5-C1, Cartier chains | `"Cartier operator" multivariate polynomials finite field`; `"Cartier operators" multivariate rational functions characteristic p`; `multivariate Cartier operator coefficient extraction several variables finite field` |
| A5-C2, coupled sum | `nilpotency index Kronecker sum Jordan blocks characteristic p binomial coefficients`; `"Kronecker sum" nilpotent Jordan blocks characteristic p`; `"Jordan canonical form" "Kronecker sum" modular` |
| A5-C3, exact Jordan owner | `C W Norman "On Jordan bases for the tensor product and Kronecker sum" PDF`; `"03081080701395640" Norman PDF`; `"S(m,n)" Kronecker sum Norman p-adic expansions` |
| A5-C4, recent/Cartier context | `2025 2026 Kronecker sum Jordan blocks positive characteristic`; `2025 2026 multivariate Cartier operator polynomial dynamics`; `"Algebraic power series and their automatic complexity I" finite fields authors` |

## Direct-neighbor reading record and limits

- Wadsanthat--Panraksa: verified bibliographic record and read the abstract.
- Cai--Stanley: read the abstract and introduction, including the statement
  that the result is the Smith form of `DU+xI` for Young's lattice.
- Shah: read the abstract and introduction through the integral-canonical-form
  interpretation.
- Liu--Smith: read the abstract and scope statement.
- Elmer--Kadr (2026): read the abstract, introduction, and Section 2.3 through
  the displayed cyclic-`p` tensor-product rules.
- Norman: read the publisher abstract, including the claims of a Jordan basis
  and all elementary divisors/multiplicities from `p`-adic expansions.
- Rowland--Stipulanti--Yassawi: read the abstract and the univariate/bivariate
  Cartier definitions used to assess terminology ownership.

This was a bounded web audit using primary papers, author/institutional
records, official publisher pages, and arXiv.  It was not a MathSciNet/zbMATH
exhaustive citation-chain review.  Search absence is recorded only for R1's
exact ordered-DAG update and A1's exact threshold wording; neither absence is
promoted to a novelty statement.  Novelty, priority, submission, and all
external dissemination remain **HOLD**.
