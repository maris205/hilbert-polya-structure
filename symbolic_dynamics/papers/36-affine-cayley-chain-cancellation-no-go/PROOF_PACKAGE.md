# Paper 36 proof package — SD-C38

## 1. Definitions

For `r>=2`, let `M_r=<u,v | vu=u^r v>+` in its affine normal form. Let
`Gamma_r^<->` be its right Cayley graph after adjoining distinct formal
reverses. Let `X_r^H` be the cyclically nonbacktracking oriented-edge shift,
and let `K_r` be the Cayley `2`-complex obtained by attaching every translate
of the defining relation cell. The free marker counts each original oriented
edge once.

For `0<theta<1`, define `D_theta` and `T_(r,theta)=D_theta H_r D_theta` exactly
as in `SOURCE_LOCK.md`.

## 2. Main theorem

### Theorem — affine Cayley-chain cancellation quadrilemma

For every `r>=2`:

1. `K_r` is contractible, so all positive-dimensional homology and every
   reduced closed-path homotopy class vanish after complete relation filling.
2. Any torsion-free additive grading invariant under the relation has
   `deg(u)=0`; the unit generator-step marker does not descend.
3. `T_(r,theta)` is trace class and
   `Tr(T_(r,theta)^(r+3)) >= (r+3)theta^(2S_r)>0`, where
   `S_r=r(r+1)/2+2r+5`.
4. The diagonal scalar chain lift on the group completion has zero supertrace
   in every positive power and superdeterminant one, uniformly for every
   two-generator one-relator presentation.

Therefore complete cellular cancellation cannot simultaneously retain a
nonzero source-natural recurrent sector, preserve the original marker, own the
same prequotient Fredholm determinant, and fail matched generic controls.

## 3. Proof of total cancellation (`SD-C38-C1`)

The affine product embeds `M_r` injectively in affine transformations. If
`x=x^m`, `m>=2`, and `x=(b,k)`, then `k=mk`, hence `k=0`, and then `b=mb`,
hence `b=0`. Thus the relevant torsion-free hypothesis holds.

The words `vu` and `u^r v` share neither a nonempty prefix nor a nonempty
suffix: their first letters and last letters differ. The presentation is
therefore incompressible with empty compression word. The contractibility
theorem of Gray and Steinberg for torsion-free incompressible one-relator
monoids applies to the ordinary Cayley complex in this empty-compression case.
Thus `K_r` is contractible.

Contractibility implies `pi_1(K_r)=0` and `H_j(K_r;Z)=0` for `j>=1`.
Consequently every reduced closed edge path becomes null-homotopic after free
backtrack cancellation and relation-cell homotopies. The quotient does not
select relation cycles; it removes the entire primitive recurrent ledger.

For an explicit chain check, with edge basis `e_u,e_v`,

```text
partial_2(1)
 =(v-sum_(j=0)^(r-1)u^j)e_u+(1-u^r)e_v.
```

Applying `partial_1(e_u)=u-1`, `partial_1(e_v)=v-1` gives
`partial_1 partial_2(1)=vu-u^r v=0`. Exactness then follows from
contractibility. This chain identity is consistent with, but not substituted
for, path-level simple connectivity.

## 4. Proof of marker non-descent (`SD-C38-C2`)

Let `D` be torsion-free abelian and let an additive degree be invariant under
the cell. With `alpha=deg(u)` and `beta=deg(v)`, the relation implies

```text
beta+alpha=r alpha+beta,
(r-1)alpha=0.
```

Since `r>=2` and `D` is torsion-free, `alpha=0`. The original degree has
`alpha=beta=1`, a contradiction. Equivalently, the cell would identify the
free monomials `z^2` and `z^(r+1)`. Equality after a specialization of `z` is
not equality of free germs. This proves the claim independently of every
operator or finite audit.

## 5. Proof of Fredholm separation (`SD-C38-C3`)

At every vertex of the formal symmetrization there are at most four outgoing
oriented edges. After excluding the immediate reverse, every row and column of
`H_r` has at most three ones. The Schur test yields `||H_r||<=3`.

There are at most four oriented edges with any given origin. Therefore

```text
Tr(D_theta)
 <=4 sum_(b,k>=0)theta^(1+b+k)
 =4theta/(1-theta)^2.
```

So `D_theta` is trace class. As the trace class is a two-sided ideal,
`D_theta H_r D_theta` is trace class and its ordinary Fredholm determinant is
defined on the full oriented-edge Hilbert space.

The relation word based at `(0,0)` is cyclically nonbacktracking and primitive.
The sum of damping exponents over its edge origins equals

```text
S_r=1+2+(r+2)+sum_(j=1)^r(j+1)
   =r(r+1)/2+2r+5.
```

The corresponding `DHD` cycle has weight `theta^(2S_r)`. Its `r+3` cyclic
base states produce `r+3` diagonal terms in `T^(r+3)`. All entries are
nonnegative, hence

```text
Tr(T^(r+3)) >= (r+3)theta^(2S_r)>0.
```

The Fredholm trace-log therefore has a positive coefficient at the relation
length, whereas the complete chain quotient has an empty recurrent ledger.
They cannot be the same determinant-bearing object.

## 6. Proof of generic scalar cancellation (`SD-C38-C4`)

On the group-completed cellular complex, take one scalar convolution operator
`A` and lift it diagonally to one copy on `C_0`, two copies on `C_1`, and one
copy on `C_2`. Left convolution commutes with the right-module Fox boundary.
For every `n>=1`,

```text
Str(A_tilde^n)
 =tau(A^n)-2tau(A^n)+tau(A^n)
 =0.
```

Exponentiating the trace-log gives `SDet(I-zA_tilde)=1`. Only the cell-orbit
counts `(1,2,1)` enter. Replacing the affine relator with any other relator in
a two-generator one-relator presentation does not change the calculation.
Thus the mechanism passes all-orders cancellation only by cancelling every
sector generically; it has no source-selective arithmetic content.

## 7. Finite quotient corollary

Let `q` be coprime to `r` and `t=ord_q(r)`. In the finite semidirect group
`Z/qZ semidirect_r Z/tZ`, affine relation cells alone do not impose the finite
relations `u^q=1` and `v^t=1`; their cycles may survive in `H_1`. Adding cells
for the complete finite presentation kills those generators. Hence a residual
finite-block class is a quotient artifact, not evidence of a class descending
from the contractible infinite Cayley complex.

## 8. Balanced control corollary

At `r=1`, `vu=uv` is homogeneous of length two, so the unit marker descends.
The filled Cayley complex is the contractible square grid, so its positive
homology still vanishes. Thus marker descent is necessary for the proposed
same-clock quotient but not sufficient for nonzero recurrence.

## 9. Claim firewall

The theorem does not identify cellular homology with ordinary path
multiplicity, a Fuglede--Kadison determinant with an ordinary Fredholm
determinant, or a trivial superdeterminant with an arithmetic primitive ledger.
It does not extend to every coefficient system or derived symbolic object.
Its conclusion is exactly the failure of the frozen source-derived Cayley-cell
mechanism.
