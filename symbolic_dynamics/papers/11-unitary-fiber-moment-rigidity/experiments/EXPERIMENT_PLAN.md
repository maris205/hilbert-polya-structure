# SD-C13 Frozen Experiment Plan

## Object

Attach one frozen finite-dimensional unitary \(U_p\) to every tensor-prime
atom loop. The positive ledger uses normalized matrix trace
\(\tau_p=\operatorname{Tr}/d_p\), and repetition \(r\) carries
\(\tau_p(U_p^r)\). Ordinary trace is an explicit control.

No target-zero data, fitted phases, changed fibers, or crossing census is
allowed.

## Exact and numerical tests

1. Audit identity, scalar-phase, conjugate-phase, and cyclic permutation
   moment families through repetition 32.
2. Use cycle dimensions \(m=2,\ldots,8\).
3. Verify faithful normalized-trace rigidity from the positive
   Hilbert--Schmidt identity.
4. Verify ordinary-trace rigidity by exact Newton identities in dimensions
   \(1,\ldots,8\).
5. Test nonfaithful \(1\oplus V\) hidden sectors.
6. Test the graded even \(=1\oplus V\), odd \(=V\) construction in both
   supertraces and Berezinians.
7. Audit a formal-variable triangle and two independent return paths.
8. Test entropy/fiber dimensions 2, 3, 4 on tensor-prime, composite, and
   random increasing clocks with 32 frozen seeds.

## Stop gates

- Faithful \(\tau(U)=1\) forcing \(U=I\) stops positive Bloch escape.
- Any finite repetition with a mixed formal monomial stops recurrent escape.
- Graded preservation that cancels the moving determinant sector stops
  graded escape.
- Matched nonprime motion triggers STOP_SCOPED / PROVES_TOO_MUCH.
- Route B remains false without a fixed self-adjoint generator.
