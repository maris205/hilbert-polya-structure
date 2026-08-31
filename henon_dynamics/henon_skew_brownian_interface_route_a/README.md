# HCS-C266 — skew Brownian interface atlas (Route A)

This package freezes the zero-drift skew Brownian SDE

`X_t=x+B_t+(2p-1)L_t^0(X)`, `0<=p<=1`,

with **symmetric semimartingale local time**.  It closes the Lebesgue heat
kernel, the speed-measure symmetric kernel, the complete resolvent, every
two-sided exit probability and discounted side transform, the mean exit time,
and the generalized arcsine law for the positive occupation fraction.  The
ordinary Brownian and two one-sided reflected faces are retained.

The deterministic certificate contains 275 regression rows.  Its producer,
producer-independent checker, SymPy reconstruction, fresh byte replay, and
repaired-hash hostile mutation suite are in `code/`; the final paper is
`paper/main.pdf`.

The package is source-local stochastic interface dynamics.  It claims no
target arithmetic local data, Euler factor, root number, automorphy, target
divisor, functional equation, or Hilbert--Pólya operator.  Scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is disabled.
