# Final Proposal

## Title

**Maximum-Dimensional Torus Translates in Sparse Shift-Like Recurrences:
Coefficientwise Moduli and a Support-One GCD Obstruction**

## One-sentence contribution

For anchored shift-like recurrences with at least two nonconstant monomials,
we classify every maximum-dimensional torus translate and its fixed-support
coefficient family; at the support-one boundary, we prove exact gcd-reduced
character extinction and show that the unique penultimate character shadow is
universally scalar-incompatible when the reduced cycle length is at least
three.

## Exact setup

Let `Omega` be algebraically closed of characteristic zero. Fix

`k>=2`, `1<=nu<k`, `a in Omega*`,

and the recurrence

`x_(n+k)=P(x_(n+k-nu))+a x_n`.

Let `V_m subset (G_m)^(k+m)` encode the equations `0<=n<m`. For a
characteristic-zero field `K` and finite-rank `Gamma<=K*`, let `T_m` be the
initial states whose first `m+1` orbit states lie in `Gamma^k`. Projection
identifies `T_m` with `V_m intersect Gamma^(k+m)`.

The only indispensable external input is Laurent's qualitative torus
Mordell--Lang theorem. All recurrence geometry is internal.

## Main theorem A: maximum-dimensional translates

Assume

`P(X)=c+sum_(ell=1)^s b_ell X^(e_ell)`,

with actual support

`0<e_1<...<e_s`, `a,c,b_ell!=0`, `s>=2`.

Paper 17 proves that every connected translate in `V_m`, `0<=m<=k`, has
dimension at most `k-m`. Fix `1<=m<k` and put

`R_m={n-nu mod k:0<=n<m}`.

Let `H_m` be the saturated subgroup defined by killed initial coordinates in
`R_m` and copied futures `x_(k+n)=x_n`.

### TA1: subgroup rigidity

Every translate `xi H subset V_m` with `dim H=k-m` has

`H=H_m`.

### TA2: normalized translate classification

Normalize each coset uniquely by setting every free initial scalar to one.
Let

`y_n=xi_(k+n-nu)`, `0<=n<m`.

The active set and its size are

`A_m=[max(0,m-nu),min(m,k-nu))`,

`alpha_m=min(m,k-m,nu,k-nu)`.

The normalized translate scheme `E_m subset (G_m)^m` is defined by

- `P(y_n)=0` for `n in A_m`;
- `y_n!=P(y_(n-nu))` for `nu<=n<m`; and
- `P(y_j)+a y_(j+nu-k)!=0` for `k-nu<=j<m`.

The inverse reconstruction is explicit and gives a geometric-point
bijection between `E_m` and normalized maximum-dimensional translates.

### TA3: fixed-fiber geometry

`E_m` is nonempty for every permitted coefficient tuple and every
`1<=m<k`. If `P` is squarefree of degree `delta`, `E_m` has exactly
`delta^alpha_m` smooth geometric irreducible components, each of dimension
`m-alpha_m`. If `P` has `r` distinct roots, `E_m^red` has `r^alpha_m`
components, while multiple active roots retain their natural nilpotent
directions.

### TA4: universal coefficient family

Over the fixed-actual-support coefficient torus

`B=Spec Q[a^(+-1),c^(+-1),b_1^(+-1),...,b_s^(+-1)]`,

the universal `mathcal E_m` is an explicit open in

`Z(P)^(alpha_m) x_B G_(m,B)^(m-alpha_m)`.

It is flat and relative lci, and smooth over the discriminant complement. At
active root multiplicities `mu_i`, the completed fiber local ring is a power-
series ring in the free directions modulo the independent equations
`z_i^(mu_i)`.

### CA1: coefficientwise arithmetic sharpness

For every permitted coefficient tuple, after a finite algebraic extension
there is a compatible finitely generated group with infinite `T_(k-1)`.
Paper 17 gives finite `T_k` for every finite-rank group. Thus the terminal
window is coefficientwise sharp in this compatible-field, compatible-group
sense.

## Main theorem B: support-one gcd obstruction

Assume

`P(X)=c+bX^d`, `a,b,c!=0`, `d>=2`.

Put

`g=gcd(k,nu)`, `q=k/g`, `L=(k-nu)/g`.

Then `q>=2`, `1<=L<q`, and `gcd(q,L)=1`.

### TB1--TB3: exclusive labels and colored components

On every core residue, each local character triple has exactly one exclusive
type

`A=(0,v,dv)`, `B=(v,0,v)`, `C=(dv,v,0)`, or `Z=(0,0,0)`,

with `v!=0` in `A/B/C`. Connecting the two nonzero positions gives
`d`-scaling components. Signed cycle weights define an integer height on each
component. Giving components independent colors yields

`F_(j+q)=F_j+T F_(j+L)`

in a free colored Laurent module.

### TB4--TB5: exact character boundary

`q^2` consecutive core equations force every character to zero. With
`q^2-1` equations, every nonzero component must pass through the same central
coordinate

`N_*=(L+1)q-1`,

so there is exactly one component. The central block is `(0,...,0,1)`, and
the entire shadow is determined by

`G(z)=(1+Tz^L)/(1+Tz^L+z^q)`,

`H(z)=z^(q-1)/(1+Tz^(q-L)+z^q)`.

The explicit coefficient formulas prove that every involved term is zero or
one monomial. The next term is `1+T^q`, giving exact character extinction.

After the other original residue classes have been extinguished, ambient
coordinate characters generate the actual `X*(H)`. Hence the unique nonzero
pattern forces `X*(H)=Z w` and `dim H=1`; this is not a rank-one ansatz.

### TB6--TB8: original windows and scalar obstruction

At `m=kq`, each of the `g` residues has `q^2` core equations, so no positive-
dimensional translate exists. At `m=kq-1`, only residue `g-1` has the unique
penultimate shadow.

For `q>=3`, seven forced labels occur at explicit indices. Their scalar
conditions give

`bc^(d-1)=-1`, `a=-1`,

and then a `Z` equation with old, middle, and future scalar all equal to `c`
gives `c=-c`. Characteristic zero and `c!=0` yield a contradiction.

Thus

`V_(kq-1)` has no positive-dimensional torus translate for `q>=3`.

This is a universal obstruction one equation before character extinction. It
is not called an exact or optimal scalar threshold.

### TB9: the recovered `q=2` endpoint

For `q=2`, necessarily `L=1`, and the unique core is the `CBA` word

`(d w,w,0,w,d w)`.

It lifts if and only if

`a=-1`, `bc^(d-1)=-1`,

through scalars

`(b s^d,s,c,-s,b(-s)^d)`.

For general `g`, all inactive residue scalars are filled by choosing generic
nonzero orbit segments of the polynomial automorphism

`Phi(x,y)=(y,c+b y^d-x)`.

The exponent vector contains `1`, so the one-parameter subgroup is saturated.
At `m=kq` character extinction still closes the family.

The planar `g=1,k=2` instance is the Paper 16 endpoint and is recovered only
for consistency.

### CB1: arithmetic consequences

Laurent gives:

- finite `T_(kq)` for every finite-rank group and every `q>=2`;
- finite `T_(kq-1)` for every finite-rank group when `q>=3`;
- finite `T_(kq-1)` for nonresonant `q=2`; and
- compatible infinite `T_(kq-1)` on the resonant `q=2` locus, followed by
  finite `T_(kq)`.

All statements are qualitative. Paper 16 remains stronger and effective in
the plane.

## STOP-S1: corrected false conjecture

The initial conjecture that the `q^2-1` character shadow always has a scalar
lift is false. A first counterexample occurs at `(k,nu,d)=(3,1,2)`, and the
seven-label theorem proves universal failure for every `q>=3`.

The project preserves this negative history. It claims an exact character
boundary and a universal penultimate scalar obstruction, not a sharp scalar
clock for `q>=3`.

## Proof architecture

### Common layer

1. Fix recurrence orientation and window indexing.
2. Restrict ambient coordinates to characters on a connected torus.
3. Use group-algebra independence and actual-character surjectivity.
4. Apply Laurent only after geometric coset exclusion is complete.

### Part A

1. Replay the Paper 17 relation lattice and prove it is saturated.
2. Equality of ranks gives subgroup rigidity.
3. Normalize representatives and solve scalar recurrences through `y_n`.
4. Prove nonemptiness root tuple by root tuple using proper-closed avoidance.
5. Pass to fixed fibers and the universal coefficient torus.
6. Vary the saturated equality parameter inside a compatible group.

### Part B

1. Prove exclusive `A/B/C/Z` labels and scalar rules.
2. Split by `gcd(k,nu)`.
3. Use colored components and integer heights to handle arbitrary rank.
4. Prove the `q^2` and `q^2-1` theorems by minimum height and triangular
   zeros.
5. Derive the two generating functions and monomial uniqueness.
6. Read seven labels and close scalar compatibility for `q>=3`.
7. Prove the `q=2` iff statement and fill inactive residues generically.

## Relation to Papers 16--18

- Paper 16 owns planar `CBA`, exact `T_4/T_3`, and an effective bound. Paper
  19 does not claim those as new.
- Paper 17 owns `dim H<=k-m`, its special equality family, `T_k` finiteness,
  and special-coefficient sharpness. Paper 19 begins with equality
  classification and coefficientwise moduli.
- Paper 18 has no theorem-level overlap.

Neither predecessor is absorbed. Their ownership is hash-bound in the source
design.

## Twenty-nine-page article plan

| section | substantive pages |
|---|---:|
| 1. Introduction | 2.0 |
| 2. Recurrences, Laurent, and predecessor boundary | 2.5 |
| 3. Saturated equality rigidity | 2.5 |
| 4. Normalized translates and nonemptiness | 4.0 |
| 5. Fixed-fiber and universal geometry | 3.0 |
| 6. Coefficientwise arithmetic sharpness | 1.5 |
| 7. Exclusive labels and gcd cores | 2.5 |
| 8. Component heights and character extinction | 4.0 |
| 9. Laurent shadow and seven labels | 3.5 |
| 10. Scalar obstruction and the `q=2` fill | 2.5 |
| 11. Related work and limitations | 1.0 |
| **Total** | **29.0** |

Natural compression may produce 27--28 pages. The admissible range is
`26--29`. References are outside the count. No appendix, computation, code,
data, figure, or background padding is required.

## Locked exclusions

The project excludes:

- dimension language for `T_m`;
- lower-dimensional or inclusion-maximal coset classification;
- Hilbert/Fano/fine-moduli terminology for `E_m`;
- unqualified nonclosed-field component counts;
- smooth branch claims without squarefreeness;
- coefficient-zero or varying-support family claims;
- every-group coefficientwise infinitude;
- effective consequences of Laurent;
- exact/optimal/minimal clock language for `q>=3`;
- novelty credit for Paper 16's `CBA` or Paper 17's dimension theorem;
- positive characteristic, zero coefficients, `d=1`, rational/Laurent
  support, and arbitrary polynomial automorphisms;
- absolute priority; and
- heights, periodic-point classification, effective enumeration, or any
  external lifecycle effect.

## Lifecycle decision

Independent gate results are:

- combined novelty `8.2/10` and standalone value `8.4/10`;
- conservative gate scores `7.9/8.2/9.1`; and
- adversarial character verdict `PROVABLE AS STATED`, confidence `0.97`.

The corrected theorem package passes the candidate gate.

**FINAL PROPOSAL STATUS: AUTHOR COMPLETE / PENDING FRESH INDEPENDENT SOURCE
DESIGN REVIEW.**

This status authorizes no source lock, paper plan, bibliography, TeX,
computation, figure, build, release, upload, submission, external message, or
identity disclosure.
