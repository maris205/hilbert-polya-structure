# Research Question

## Source-design status

This document fixes the theorem package, proof obligations, predecessor
boundary, and nonclaims for

**Maximum-Dimensional Torus Translates in Sparse Shift-Like Recurrences:
Coefficientwise Moduli and a Support-One GCD Obstruction**.

The package is an author source design. It contains no scientific computation,
code, data, figure, bibliography, manuscript source, build, release, or
external effect. A separately authorized independent source-design review is
the sole permitted next scientific gate.

The internal claim identifiers are `TA1--TA4`, `CA1`, `TB1--TB9`, and `CB1`.
`EXT-L` denotes the only indispensable external proof theorem. `BG17` denotes
a predecessor result whose ownership is not transferred to this project.

## The unified question

Consider a type-`nu` shift-like recurrence inside a multiplicative torus.
There are two different ways in which a character configuration can be
extremal.

1. If the polynomial has a nonzero constant and at least two actual
   nonconstant monomials, the character relations already determine the
   unique subgroup underlying every maximum-dimensional translate. Which
   scalar translates of that subgroup actually lie in the recurrence
   variety, and how do those translates vary with the coefficients?
2. If the polynomial has only one nonconstant monomial, the local character
   identity has three exclusive pairings. How long can a nonzero character
   shadow survive after the recurrence is split by `gcd(k,nu)`, and can its
   last possible shadow be lifted to compatible nonzero scalars?

The common theme is **character equality versus scalar lift**. Part A
classifies every scalar lift of the maximum-dimensional anchored character
pattern. Part B proves that the unique penultimate support-one character
pattern has no scalar lift when the reduced cycle length is at least three.

## D1--D3: common conventions

Let `Omega` be an algebraically closed field of characteristic zero. Fix

`k>=2`, `1<=nu<=k-1`, and `a in Omega*`.

For `P in Omega[X]`, define

`S(z_1,...,z_k)=(z_2,...,z_k,P(z_{k-nu+1})+a z_1)`.

With zero-based scalar coordinates,

`S^n(x_0,...,x_{k-1})=(x_n,...,x_{n+k-1})`

and the recurrence is

`x_{n+k}=P(x_{n+k-nu})+a x_n`.                                    (R)

For `m>=0`, let `V_m=V_m(S)` be the closed subvariety of
`(G_m)^(k+m)` with coordinates `x_0,...,x_{k+m-1}` and equations (R)
for `0<=n<m`. Set `V_0=(G_m)^k`.

If the data are defined over a characteristic-zero field `K` and
`Gamma<=K*`, put

`T_m(S,Gamma)={z in Gamma^k:S^j(z) in Gamma^k for 0<=j<=m}`.

Projection to the first `k` coordinates is a bijection

`V_m intersect Gamma^(k+m) -> T_m(S,Gamma)`.

Thus `m` is the number of recurrence equations or transitions. The states run
from time zero through time `m`. Dimension is asserted for torus translates
inside `V_m`, never for the arithmetic set `T_m`.

A torus translate means `xi H`, where `H` is a connected closed subtorus of
the ambient torus. Ambient coordinate characters restrict surjectively onto
`X*(H)`; this actual-character-lattice quantifier is essential in Part B.

## EXT-L and the arithmetic bridge

`EXT-L` is Laurent's qualitative Mordell--Lang theorem for algebraic tori:
the intersection of a torus subvariety with the division group of a finitely
generated subgroup is covered by finitely many intersections with torus
translates contained in the subvariety. Consequently, absence of a
positive-dimensional torus translate implies finiteness of the intersection.

The finite-rank and arbitrary-field bridge is proved internally. An arbitrary
finite-rank group, including one with infinite torsion, lies in the division
hull of a finitely generated subgroup. The finitely generated field obtained
from the coefficients and those finitely many generators embeds into `C`;
one does not assert that the whole ground field embeds into `C`.

No effective cardinality follows from `EXT-L`.

## Part A: maximum-dimensional anchored translates

Assume in this part that

`P(X)=c+sum_{ell=1}^s b_ell X^(e_ell)`,

where

`0<e_1<...<e_s`, `a,c,b_ell in Omega*`, and `s>=2`.

The support is actual collected support. Fix `1<=m<k`.

### BG17: predecessor dimension law

Paper 17 proves that every connected torus translate `xi H subset V_m`
satisfies

`dim H<=k-m`.                                                       (A0)

Its proof supplies the saturated relation lattice

`L_m=<epsilon_(k+n-nu), epsilon_(k+n)-epsilon_n:0<=n<m>`            (A1)

inside `Z^(k+m)`. Paper 17 also constructs one special coefficient family
attaining equality and proves qualitative finiteness of `T_k`.

These are predecessor facts, not Paper 19 novelty claims.

Put

`R_m={n-nu mod k:0<=n<m}`.

Define the canonical saturated subtorus `H_m` by

- `x_r=1` for `r in R_m` among the initial coordinates; and
- `x_(k+n)=x_n` for `0<=n<m`.

Then `H_m` has dimension `k-m`.

### TA1: maximum-subgroup rigidity

If

`xi H subset V_m` and `dim H=k-m`,

then

`H=H_m`.                                                           (TA1)

Indeed, equality of ranks forces the kernel of the ambient character map to
equal the saturated lattice `L_m`. Thus Paper 19 classifies the subgroup
under every maximum-dimensional translate. It does not classify lower-
dimensional or inclusion-maximal translates.

### D6: normalized representatives

Every coset `xi H_m` has a unique representative satisfying

`xi_i=1` for every free initial index `i notin R_m`.

For such a representative put

`y_n=xi_(k+n-nu)`, `0<=n<m`.

Define the active set

`A_m={n in [0,m-1]:n notin R_m}`

`   =[max(0,m-nu),min(m,k-nu))`,                                  (A2)

and

`alpha_m=|A_m|=min(m,k-m,nu,k-nu)`.                               (A3)

### TA2: normalized translate scheme `E_m`

Let `E_m` be the locally closed subscheme of `(G_m)^m` with coordinates
`y_0,...,y_(m-1)` defined by

1. `P(y_n)=0` for `n in A_m`;
2. `y_n!=P(y_(n-nu))` for `nu<=n<m`; and
3. `P(y_j)+a y_(j+nu-k)!=0` for `k-nu<=j<m`.

Its geometric points are in bijection with normalized maximum-dimensional
translates contained in `V_m`.

The inverse reconstruction is

- `xi_i=1` for initial `i notin R_m`;
- `xi_(k+n-nu)=y_n` for `0<=n<nu`;
- `xi_(n-nu)=a^(-1)(y_n-P(y_(n-nu)))` for `nu<=n<m`; and
- `xi_(k+j)=P(y_j)+a xi_j` for `0<=j<m`.

Whenever an output in the last line is already a later `y` coordinate, the
displayed formulas agree by construction. The two open conditions are
exactly the nonvanishing conditions not automatic from the active-root
equations.

The term **normalized translate scheme** refers to this explicit scheme and
its geometric-point classification. No Hilbert- or Fano-scheme functorial
claim is made.

### TA3: fixed-fiber geometry and nonemptiness

Let `delta=deg P=e_s`, and let `r` be the number of distinct roots of `P`.
Since `c!=0`, every root lies in `G_m`.

For every permitted coefficient tuple, `E_m` is nonempty. More precisely,
after choosing a root of `P` independently at each active coordinate, the
remaining conditions remove a finite union of proper closed subsets from an
irreducible torus. Active indices and the relevant shifted active indices are
disjoint. If `alpha_m=m`, neither family of inequalities occurs.

If `P` is squarefree, `E_m` is smooth and has exactly

`delta^(alpha_m)`

geometric irreducible components, each of dimension `m-alpha_m`.

For arbitrary `P`, the reduction of `E_m` has exactly

`r^(alpha_m)`

geometric irreducible components. Multiple active roots retain their natural
nilpotent directions in the unreduced scheme.

### TA4: the fixed-support coefficient family

Fix the exponent support `e_1<...<e_s` and put

`B=Spec Q[a^(+-1),c^(+-1),b_1^(+-1),...,b_s^(+-1)]`.

Let `P_univ=c+sum b_ell X^(e_ell)` and let

`Z(P_univ) subset G_(m,B)`

be its root scheme. It is finite flat of degree `delta` over `B`. The
universal normalized translate scheme `mathcal E_m` is an explicit open
subscheme of

`Z(P_univ)^(alpha_m) x_B G_(m,B)^(m-alpha_m)`.                      (A4)

Hence `mathcal E_m -> B` is flat and a relative local complete
intersection. It is smooth over the discriminant complement.

At a fixed coefficient fiber and a point whose active roots have
multiplicities `mu_1,...,mu_(alpha_m)`, the completed fiber local ring is

`Omega[[t_1,...,t_(m-alpha_m),z_1,...,z_(alpha_m)]]`

` /(z_1^(mu_1),...,z_(alpha_m)^(mu_(alpha_m)))`,                   (A5)

after multiplying the equations by local units. The open inequalities become
units in the completion.

This is a relative and fiberwise statement. It does not assert that the
discriminant is reduced or irreducible, or identify all singularities of the
total space.

### CA1: coefficientwise arithmetic sharpness

For every permitted anchored coefficient tuple, `E_(k-1)` is nonempty and
parametrizes a one-dimensional translate. After a finite algebraic extension
containing one translating point, let `Gamma` be generated by its finitely
many coordinates and by `2`. Varying the free parameter through `2^N` gives
infinitely many points of `T_(k-1)`.

Together with BG17, which gives finiteness of `T_k` for every finite-rank
`Gamma`, the terminal window `k` is sharp coefficient by coefficient in this
compatible-field, compatible-group sense.

This is not a statement about every fixed group or about remaining in the
original ground field.

## Part B: support-one character extinction and scalar obstruction

Assume in this part that

`P(X)=c+b X^d`, `a,b,c in Omega*`, and `d>=2`.

Put

`g=gcd(k,nu)`, `q=k/g`, and `L=(k-nu)/g`.

Then `q>=2`, `1<=L<q`, and `gcd(q,L)=1`.

For an original index `i=r+gj` in residue class `r mod g`, write its
restricted character additively as `v_j`. The local character triple is

`(v_j,v_(j+L),v_(j+q))`.

### TB1: exclusive labels

Every local character identity has exactly one of the following types:

| label | old | middle | future |
|---|---|---|---|
| `A` | `0` | `v` | `d v` |
| `B` | `v` | `0` | `v` |
| `C` | `d v` | `v` | `0` |
| `Z` | `0` | `0` | `0` |

In rows `A`, `B`, and `C`, `v!=0`; the labels are exclusive. Their scalar
conditions, using core translation scalars `eta_j`, are

| label | scalar conditions |
|---|---|
| `A` | `eta_(j+q)=b eta_(j+L)^d`, `a eta_j=-c` |
| `B` | `eta_(j+q)=a eta_j`, `b eta_(j+L)^d=-c` |
| `C` | `eta_(j+q)=c`, `a eta_j=-b eta_(j+L)^d` |
| `Z` | `eta_(j+q)=c+b eta_(j+L)^d+a eta_j` |

The support bits satisfy

`s_(j+q)=s_j+s_(j+L)` over `F_2`.                                 (B1)

### TB2--TB3: residues, colored components, and heights

The recurrence splits into `g` core residue classes. For a character word in
an arbitrary torsion-free lattice, connect the two nonzero positions in every
`A`, `B`, or `C` triple, with multiplicative edge weight `d` or `1`.

Every connected component has a well-defined integer height: a nonzero
height change around a cycle would give `v=d^s v`, impossible in a
torsion-free group for `d>=2`.

Give different components different colors `e_C` and set

`F_i=T^(h_i)e_C` on component `C`, and `F_i=0` at a zero character.

Then, in the free colored module

`direct_sum_C F_2[T,T^(-1)] e_C`,

every core equation satisfies

`F_(j+q)=F_j+T F_(j+L)`.                                           (B2)

Colors prevent accidental equality of values carried by disconnected
components from being treated as a graph connection.

### TB4: `q^2` core extinction

Any torsion-free-lattice-valued character word satisfying `q^2` consecutive
core equations is zero on every involved coordinate.

The proof takes a minimum-height vertex in one component, traces it backward
to a residue `r in [0,q-1]`, and forces a `B` persistence chain. Its middle
zeros propagate in a triangle to make `v_(r+qL)=0`, while the same persistence
chain makes `v_(r+Lq)!=0`. Since `qL=Lq`, this is a contradiction.

### TB5: the unique `q^2-1` character shadow

For `q^2-1` core equations, every nonzero component has minimum-height
residue `q-1`. Put

`A_*=Lq`, `N_*=(L+1)q-1`.

The triangular zero set fills the central block `[A_*,N_*]` except for its
last coordinate. Every nonzero component must contain `N_*`; disjointness of
components therefore leaves exactly one component.

After normalizing `F_(N_*)=1`,

`(F_(A_*),...,F_(N_*))=(0,...,0,1)`.                               (B3)

Recurrence (B2) determines the whole involved word forward and backward. If
`p=q-L`, the two generating functions are

`G(z)=sum_(t>=0) F_(N_*-t) z^t=(1+Tz^L)/(1+Tz^L+z^q)`,             (B4)

`H(z)=sum_(t>=0) F_(A_*+t) z^t=z^(q-1)/(1+Tz^p+z^q)`.              (B5)

Their coefficient formulas show that every involved `F_i` is zero or one
monomial. At the next equation the first collision is `1+T^q`. Thus the
`q^2-1` shadow exists and is unique, while `q^2` equations extinguish every
shadow.

After TB6 kills every other residue in the full original `m=kq-1` window,
ambient coordinate characters generate the actual `X*(H)`. The unique
nonzero shadow contains its minimum character `w` and all other characters
are `0` or `d^beta w`. Hence `X*(H)=Z w`, `w` is primitive, and `dim H=1`.
The primitive-rank conclusion would not follow for an isolated core word in
an arbitrary torsion-free over-lattice with an unused direct summand; the
full-window restriction-surjectivity hypothesis is explicit here.

### TB6: original-window bookkeeping

At `m=kq`, every residue class has `q^2` core equations. Hence all involved
characters

`u_0,...,u_(kq+k-1)`

are zero. The endpoint is not `u_(2kq-1)`.

At `m=kq-1`, residues `0,...,g-2` have `q^2` core equations, while residue
`g-1` has `q^2-1`. Therefore the only possible nonzero original character
word is the unique TB5 shadow in residue `g-1`.

### TB7--TB8: seven labels and the `q>=3` obstruction

For `q>=3`, put

`z_*=N_*-2L=(q-2)L+q-1`.

The unique shadow has

- `C` at `L-1` and `B` at `q-1`;
- `C` at `z_*-q` and `z_*+L-q`;
- `Z` at `z_*`; and
- `A` at `z_*+L` and `z_*+q`.

All indices lie in `[0,q^2-2]`; coincident `C` indices for small parameters
carry the same type.

The shared scalar at the first `C/B` pair gives

`b c^(d-1)=-1`.

The later `C/A` pair gives `a=-1`. The old, middle, and future scalars at the
`Z` equation `z_*` are all `c`, so the recurrence reads

`c=c+b c^d+a c=-c`.

This contradicts characteristic zero and `c!=0`. Consequently

`V_(kq-1)` contains no positive-dimensional torus translate when `q>=3`.
                                                                        (B6)

This is a universal obstruction at the penultimate character window, not an
exact or optimal scalar escape threshold: no shorter-window survivor theorem
is asserted.

### TB9: the recovered `q=2` endpoint and general `g`

If `q=2`, then `L=1`. The unique three-equation core word is

`(d w,w,0,w,d w)`

with labels `CBA`. It lifts to scalars if and only if

`a=-1` and `b c^(d-1)=-1`.                                        (B7)

For any `s in Omega*`, its active core translate is

`(b s^d,s,c,-s,b(-s)^d)`.                                         (B8)

When `g>1`, the other residue classes carry zero characters. Their scalar
coordinates are filled by generic orbit segments of

`Phi(x,y)=(y,c+b y^d-x)`,

which is a polynomial automorphism on affine two-space under `a=-1`.
Every finitely many required iterate coordinates is a nonzero polynomial;
over the infinite field `Omega`, one avoids their finite union of zero
hypersurfaces. This yields a genuine one-dimensional saturated subtorus
translate in the whole `V_(kq-1)`, not merely a five-coordinate core lift.

At `m=kq`, TB4 still excludes every positive-dimensional translate. The
case `g=1,k=2` is the `CBA` endpoint already owned by Paper 16 and is recovered
only for consistency.

### CB1: arithmetic consequences

By `EXT-L` and the finite-rank bridge:

- for every `q>=2`, `T_(kq)` is finite for every finite-rank group;
- for `q>=3`, `T_(kq-1)` is finite for every finite-rank group;
- for `q=2` off the locus (B7), `T_(kq-1)` is finite; and
- on (B7), a compatible finite extension and finitely generated group give
  infinitely many points in `T_(kq-1)`, while `T_(kq)` remains finite.

No effective count is claimed. Paper 16 has a stronger effective theorem in
the planar `k=2` case.

## STOP-S1: the refuted false-sharpness candidate

The initial support-one conjecture asserted that the unique `q^2-1`
character shadow always lifted to scalars and therefore made `kq` an exact
geometric clock. This is false.

Already `(k,nu,d)=(3,1,2)` has a unique maximal character word but no scalar
lift. TB7--TB8 strengthen that counterexample: every `q>=3` shadow is
universally scalar-incompatible. The false conjecture is permanently marked
`STOP-S1` and must not be revived, paraphrased as sharpness, or hidden behind
the true character-extinction theorem.

## Portfolio boundary

### Paper 16

Paper 16 owns the planar support-one `T_4/T_3` theorem, the `CBA` chain, and a
stronger effective finite-rank bound. Paper 19's `q=2,k=2` specialization is a
recovered endpoint, not a novelty bullet. The new support-one content begins
with the all-`k,nu` residue theorem and the `q>=3` scalar obstruction.

### Paper 17

Paper 17 owns the anchored dimension law, a special equality subtorus family,
qualitative `T_k` finiteness, and special-coefficient sharpness. Paper 19's
Part A contribution is limited to:

1. rigidity of the subgroup under every maximum-dimensional translate;
2. complete normalized translate parameterization;
3. fixed-fiber and universal coefficient-family geometry; and
4. coefficientwise compatible-group sharpness.

### Paper 18

Paper 18 concerns marked trace coordinates and scheme-theoretic ramification
at a polynomial boundary. It has no theorem-level overlap with this project.
The shared use of scheme language is not a scientific collision.

## Credible article size and unity gate

The intended proof-first article has a credible `26--29` substantive-page
range, with an exact working budget of 29 pages:

| section | pages |
|---|---:|
| Introduction | 2.0 |
| Setup, Laurent bridge, and predecessor boundary | 2.5 |
| Saturated equality rigidity | 2.5 |
| Normalized `E_m` classification and nonemptiness | 4.0 |
| Fixed-fiber and universal-family geometry | 3.0 |
| Coefficientwise arithmetic sharpness | 1.5 |
| Exclusive labels and gcd reduction | 2.5 |
| Component-height extinction and uniqueness | 4.0 |
| Laurent shadow, generating functions, and seven labels | 3.5 |
| Scalar obstruction and general-`g` `q=2` lift | 2.5 |
| Related work and limitations | 1.0 |
| **Total** | **29.0** |

This budget uses no appendix, oversized preliminaries, formatting inflation,
code, data, or computational supplement. The two parts are not adjacent
notes: both ask when a forced character pattern admits a scalar translate.

## AC01--AC18: locked anti-claims

1. `AC01`: `T_m` itself is never called positive-dimensional.
2. `AC02`: no classification of lower-dimensional or inclusion-maximal
   translates is claimed.
3. `AC03`: “maximum-dimensional” means exactly dimension `k-m` in Part A.
4. `AC04`: `E_m` is not called a Hilbert scheme, Fano scheme, or fine moduli
   functor.
5. `AC05`: component counts are geometric-fiber statements over an
   algebraically closed field.
6. `AC06`: squarefreeness is required for the smooth `delta^alpha` statement.
7. `AC07`: the universal family fixes actual support and keeps every displayed
   coefficient invertible.
8. `AC08`: no irreducibility, reducedness, or total-singularity theorem for
   the discriminant is claimed.
9. `AC09`: coefficientwise sharpness means existence after a compatible
   finite extension and for a compatible finite-rank group, not every group.
10. `AC10`: Laurent's theorem supplies no effective cardinality.
11. `AC11`: the `q>=3` window `kq-1` is not called exact, optimal, shortest,
    or minimal.
12. `AC12`: the planar `q=2` `CBA` endpoint is not claimed as new.
13. `AC13`: Paper 17's dimension law, special equality family, and `T_k`
    theorem are not re-marketed.
14. `AC14`: character independence, root schemes, discriminants, and lci
    facts are standard tools, not headline novelty.
15. `AC15`: there is no positive-characteristic, `a=0`, `b=0`, `c=0`, or
    `d=1` extension.
16. `AC16`: there is no rational/Laurent-support or arbitrary-polynomial-
    automorphism extension.
17. `AC17`: a bounded negative literature search is not an absolute priority
    claim.
18. `AC18`: there is no effective enumeration, height theorem, periodic-point
    classification, submission, upload, or other external effect.

## Source-stage decision

The corrected combined package has passed the internal candidate gate with
conservative scores `7.9 / 8.2 / 9.1` for novelty, standalone value, and proof
readiness. A separate novelty audit returned `8.2 / 8.4`, and the adversarial
character-theorem audit returned `PROVABLE AS STATED` with confidence `0.97`.

**STATUS: AUTHOR SOURCE DESIGN COMPLETE / PENDING FRESH INDEPENDENT SOURCE
REVIEW.**

Completion of this author package will authorize only a fresh independent
source-design review. It will not authorize a source lock, paper plan,
bibliography, TeX source, computation, build, release, submission, upload,
external message, or identity disclosure.
