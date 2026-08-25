# Theorem package

## Target and status

Target: prove exact unitarity, antiunitary time reversal, signed primitive
path ownership, and coin-order sensitivity for the frozen inhomogeneous
coined walk.

Status: `PROVABLE AS STATED` and `COHERENT AS STATED`.

## Invariant object

The invariant object is `U_w=S C_w` on `H=C^5 tensor C^2`.  The same operator
owns the one-step clock, trace moments, path amplitudes, secular determinant,
and antiunitary.  A population-averaged coin is a negative control and never
replaces `U_w`.

## Definition

At every site use one of the real reflection coins

```text
C0=(1/5)[[3,4],[4,-3]],
C1=(1/13)[[5,12],[12,-5]].
```

The flip-flop shift sends `|x,+>` to `|x+1,->` and `|x,->` to
`|x-1,+>`, with positions modulo five.  For a word `w`, let `C_w` be the
block-diagonal coin and freeze `U_w=S C_w`.

## Theorem 1: source-derived unitary and reversal

For every five-site word `w`, `U_w` is real orthogonal.  The antiunitary

```text
Theta_w=C_w K
```

satisfies

```text
Theta_w^2=I,
Theta_w U_w Theta_w^(-1)=U_w^(-1).
```

The matrix `P_w=|U_w|^2` is a doubly stochastic classical shadow with the
same support and one-step clock.

### Proof

Direct multiplication gives `C0^2=C1^2=I`; both coins are real symmetric.
Thus `C_w^2=I`.  The flip-flop shift is a real symmetric permutation and
`S^2=I`.  Hence

```text
U_w^* U_w=C_w S S C_w=I.
```

Because complex conjugation `K` fixes the real matrices,

```text
(C_w K)^2=C_w^2=I,
(C_w K)(S C_w)(K C_w)=C_w S=U_w^(-1).
```

Squaring the moduli of a unitary matrix gives unit row and column sums,
which proves the shadow statement.

## Theorem 2: signed primitive paths

Let `p` be a primitive directed state cycle in the support graph of `U_w`,
let `ell_p` be its number of walk steps, and let `A_p` be the product of its
signed transition amplitudes.  Then

```text
det(I-zU_w)=product_[p](1-A_p z^(ell_p))
```

as an absolutely convergent raw product for `|z|<5/7` and by analytic
continuation as the degree-ten determinant polynomial.

### Proof

The standard determinant logarithm gives

```text
-log det(I-zU_w)=sum_{n>=1} Tr(U_w^n)z^n/n.
```

Expanding the matrix trace gives the signed amplitude of every rooted closed
state path.  Primitive-root decomposition is unique, and cyclic rotation
preserves the amplitude product.  Each column of `|U_w|` has sum at most
`7/5`, so the absolute rooted-path majorant is at most
`10(7/5)^n`.  Therefore the logarithmic regrouping is absolute for
`|z|<5/7`.  Signed cancellations are retained in the identity itself.

## Theorem 3: arrangement order is visible

The words `00011` and `00101` both contain three coins of type zero and two
of type one, but they are neither rotations nor reflection-rotations of one
another.  Their secular polynomials are

```text
D_00011(z)=1+(5617/4225)z^2+(6798/4225)z^4
             -(18432/21125)z^5+(6798/4225)z^6
             +(5617/4225)z^8+z^10,

D_00101(z)=1+(417/325)z^2+(538/325)z^4
             -(18432/21125)z^5+(538/325)z^6
             +(417/325)z^8+z^10.
```

In particular,

```text
D_00011-D_00101
 =(196/4225)z^2(z-1)^2(z+1)^2(z^2+1),
```

so coin population does not determine the walk determinant.

### Proof

The displayed formulas follow by exact elimination, or equivalently by
Newton identities from the ten-dimensional trace sequence.  Their
difference factors as stated.  Both polynomials are palindromic: `det U_w=1`
and real orthogonality give
`D_w(z)=z^10D_w(1/z)`.  This symmetry is internal and is not promoted to a
target functional equation.

## Proposition 4: population averaging is not a walk

The population average is

```text
Cbar=(3C0+2C1)/5=(1/325)[[167,276],[276,-167]].
```

It obeys

```text
Cbar^T Cbar-I=-(24/1625)I,
det Cbar=-1601/1625.
```

It is not unitary and erases spatial order.  Therefore it cannot replace
either exact walk in the source-locked comparison.

## Boundaries and open risks

- The matrix dimension is fixed at ten; no growing-level or semiclassical
  theorem is claimed.
- The primitive paths are intrinsic but have no prime-like correspondence.
- Palindromicity is a finite unitary symmetry, not target analytic structure.
- No target divisor, target counting law, arithmetic local data, Euler
  factor, root number, automorphy object, self-adjoint Hilbert--Polya operator,
  or Route-B authorization is supplied.
