# Paper 37 proof package — SD-C39

## 1. Definitions and scope

For `r>=2`, let `X_r^H` be the full cyclically nonbacktracking oriented-edge
shift on the formal-reverse right Cayley graph of
`M_r=<u,v | vu=u^r v>+`. Let `P` be a finite-rank edge connection with
invertible transports and `P_bar(e)=P_e^(-1)`. The marker counts one original
Hashimoto transition, and `T_(P,theta)` uses the frozen source-coordinate
damping from `SOURCE_LOCK.md`.

The theorem concerns complete primitive matrix Euler factors. In the graded
branch, the object is explicitly a ratio of two independently owned ordinary
Fredholm determinants, never an ordinary positive determinant.

## 2. Main theorem

### Theorem — finite-coefficient relation-saturation trilemma

For every `r>=2` and `0<theta<1`:

1. the matrix-weighted damped Hashimoto operator on the full uninduced edge
   space is trace class and owns its complete primitive factorization;
2. an ordinary primitive factor with invertible holonomy cannot be deleted;
3. a flat graded connection cancels relation factors only at balanced parity,
   when it cancels every closed factor;
4. a non-flat graded pair may cancel the defining relator, every conjugate,
   and every repetition while leaking on mixed products; the frozen shear
   pair leaks on `M_r` with supertrace `-4r^4(r-1)`;
5. imposing cancellation on every mixed product in the relator's normal
   closure cancels every closed Cayley word and gives `Z_gr(z)=1`.

Consequently no finite-rank inverse-edge coefficient mechanism under the
complete mixed-relation obligation both erases the affine relation ledger and
retains a nonzero source-proved primitive arithmetic sector.

## 3. Proof of determinant ownership (`SD-C39-C1`)

At most four oriented edges originate at an affine vertex, so the positive
diagonal damping satisfies

```text
Tr(D_theta)<=4theta/(1-theta)^2.
```

Tensoring with a finite fiber preserves trace class. The four generator and
inverse transports have finite maximum norm `M`; every matrix Hashimoto row
and column has at most three blocks. The block Schur estimate gives
`||H_P||<=3M`. The two-sided trace ideal property makes
`T_(P,theta)` trace class.

The Fredholm trace-log is therefore defined near zero. Expanding diagonal
blocks and grouping by primitive roots gives each primitive orbit `gamma` the
factor

```text
det(I-q_theta(gamma) z^|gamma| W_gamma)^(-1).
```

Every repetition appears through `Tr(W_gamma^m)`. The same derivation in each
parity gives the explicitly graded determinant ratio. Marker powers remain
the original path lengths throughout.

## 4. Proof of ordinary obstruction (`SD-C39-C2`)

If `det(I-tW)=1`, every elementary symmetric polynomial in the eigenvalues of
`W` vanishes, so its characteristic polynomial is `x^d`. Cayley--Hamilton
gives `W^d=0`. Conversely, a nilpotent matrix has determinant polynomial one.
The formal logarithm gives the equivalent vanishing of every power trace.

A product of invertible edge transports is invertible and cannot be
nilpotent. Hence an ordinary finite-rank local system cannot delete even one
complete primitive factor. A zero first trace does not alter this conclusion.

## 5. Proof of graded and flat forks

The graded factor is one precisely when the even and odd determinant
polynomials agree. Newton identities make this equivalent to equality of all
power traces, without assuming diagonalizability.

If the connection descends to the filled Cayley `2`-complex, it is flat. Paper
36 verifies that the complex is contractible, so all closed holonomies are
identity after gauge. An ordinary rank `d` retains `(1-t)^(-d)`. Graded ranks
`d_+,d_-` give `(1-t)^(d_--d_+)`: unequal ranks retain the relation, while
equal ranks cancel all closed paths. Thus flat coefficients do not select a
proper primitive sector.

## 6. Proof of explicit mixed leakage (`SD-C39-C3`)

Let

```text
A=[[1,1],[0,1]],  B_c=[[1,0],[c,1]].
```

With `u -> A` and `v -> B_c`, direct multiplication gives

```text
Tr(B_c A B_c^(-1) A^(-r))=2+c^2r,
det(B_c A B_c^(-1) A^(-r))=1.
```

The choices `c=r` and `c=-r` have equal `2x2` characteristic polynomials.
Conjugacy invariance and equality of all power traces cancel every conjugate
and repetition of the defining relator.

The word

```text
M_r=bar(u)^r v bar(u)^(r-1) v u bar(v)^2
```

traces a closed path based at `(r^2,0)`. Adjacent generator types are never
inverse, including at the cyclic join. Its unique lowercase `u` rules out a
proper word power. Exact multiplication gives

```text
Tr W_c(M_r)
=-2c^3r^2+2c^3r-c^2r^2+6c^2r-c^2+2.
```

Substituting `c=r` and `c=-r` yields `-4r^4(r-1)`, nonzero for every `r>=2`.
The direct-pass graded connection therefore fails the first mixed relation
consequence.

## 7. Proof of saturation (`SD-C39-C4`)

Let `F=F(u,v)` and `N_r=<<R_r>>`. Every closed path label maps to the identity
in `F/N_r` and hence is a finite product of conjugates of `R_r` and its
inverse. Free and cyclic reduction preserve membership in `N_r`.

Direct-cell cancellation alone does not propagate through products because
matrix holonomy is noncommutative; Section 6 gives an explicit counterexample.
If the frozen obligation is strengthened to every finite mixed product,
however, it includes every primitive closed path label. All super-power-trace
terms in the graded primitive expansion vanish. Therefore

```text
log Z_gr(z)=0,  Z_gr(z)=1.
```

The saturation is exact but retains no recurrent sector. This proves the
leakage-versus-erasure fork.

## 8. Controls and non-claims

The balanced, exponent-mutated, fixed-relator, random one-relator, and paired
two-relator controls show that direct factor matching is not arithmetic
recognition. The nilpotent control changes the transport category. Hashimoto
backtrack deletion precedes coefficient application.

The theorem does not cover every infinite-dimensional coefficient algebra,
groupoid cocycle, or different symbolic object. It constructs no target
divisor, functional equation, critical-line carrier, or Route-B result.
