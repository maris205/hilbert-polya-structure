# C156 source audit

## Frozen source

The source is the C151 Heisenberg lattice automorphism on the left quotient
`Z^3\H`, with

```text
A=((2,1),(1,1)),
q(x,y)=x(x-1)+xy+y(y-1)/2,
Phi(v,z)=(Av,z+q(v)).
```

The upstream evidence hash is
`5fe26d210e6c848789ee769f9f0fbaa0ba67baef06cb93cb3d2f2d403ef18419`.
No parameters are fitted and the only clock is the iterate number.

## Cocycle audit

For a general unimodular `B=((a,b),(c,d))`, the canonical lattice correction
is

```text
q_B=ac*x(x-1)/2+bc*xy+bd*y(y-1)/2.
```

The actual iterate correction is not silently identified with this canonical
choice: `q_n=q_(A^n)+ell_n`, with an integer linear drift `ell_n` recorded at
every certified iterate.  Local rotation residues remain modulo one, whereas
signed polynomial coefficients are serialized without modular reduction.

## Independence

The producer and checker share no imported implementation.  The checker uses
direct numerator iteration rather than the producer's coefficient evaluation.
SymPy derives the cocycle and rotation polarizations symbolically and rebuilds
the first ten primary ledgers.  Replay and mutations close byte and semantic
integrity separately.

## Firewall

“Primary” means the primary decomposition of a finite abelian group.  It does
not mean an arithmetic local factor.  No prime table, target table, Euler
factor, root number, automorphy datum, target divisor, Hilbert--Polya operator,
or Route-B input appears.  Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
