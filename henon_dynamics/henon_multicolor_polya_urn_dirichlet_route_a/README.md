# HCS-C263 — multicolor Pólya urn and Dirichlet limit (Route A)

This package freezes the classical `K`-color Eggenberger--Pólya urn with
nonnegative initial masses, positive total mass, and nonnegative reinforcement.
For positive reinforcement it closes the ordered-word law, the complete
Dirichlet--multinomial count vector, beta--binomial marginals, every
multi-index factorial moment, the proportion martingale, and its almost-sure
and finite-`Lp` Dirichlet limit.  The finite-time law and the Dirichlet de
Finetti mixture are proved in both directions.  The zero-reinforcement iid
face, zero-mass dimensional reductions, and the deterministic one-color face
are separate.

The exact receipt enumerates twelve parameter cases, 10,860 ordered words,
and all declared finite count/moment rows.  A producer, independent checker,
SymPy reconstruction, byte replay, and repaired-hash mutation suite validate
the artifact.  The final paper is `paper/main.pdf`.

This is source-local reinforced probability.  It uses no target arithmetic
local data, Euler factor, root number, automorphy statement, target divisor,
functional equation, or Hilbert--Pólya operator.  Scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is disabled.
