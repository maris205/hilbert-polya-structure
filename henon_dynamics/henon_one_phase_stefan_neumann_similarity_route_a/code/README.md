# C226 verification code

`c226_stefan_producer.py` writes eight high-precision rational-Stefan rows
and three labelled singular boundaries. `c226_stefan_checker.py` does not
import the producer: it independently brackets the strictly monotone Neumann
root and checks flux, endpoint, and energy identities. The SymPy script checks
the PDE, boundary conditions, series reversion, and moving-domain ledger.
Replay checks canonical bytes; the mutation harness checks semantic fields,
repaired/stale hashes, unknown nested keys, route, and scope tampering.

The scope lock is `NO_BAD_EULER_OR_ROOT_NUMBER`. The erf/Lambert-W formulas
are source-local explicit solvability only: the source heat clock is not target
continuation/divisor/counting law and is not an A3 analytic match.
Citation records are checked exactly: Gupta is the single-author 2003 book
The Classical Stefan Problem: Basic Concepts, Modelling and Analysis, and
Rubinstein is the 1982 two-phase paper Global Stability of the Neumann
Solution of the Two-phase Stefan Problem.
