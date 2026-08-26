# C188 narrative report

C188 makes one substantial step: it moves from isolated tropical examples to
an exact all-parameter dynamical classification of every irreducible rational
max-plus matrix.  Critical cycles determine a single integer `gamma`; the
classical theorem says this is not merely a period bound but the minimal
ultimate period of the entire normalized matrix-power sequence.

That one statement propagates through the rest of the dynamics.  The first
equality one period apart is the exact transient.  The standard CSR product
recovers every late matrix power.  Every vector and projective orbit has a
period dividing `gamma`, and the divisor strata are two-sided max-plus linear
attraction cones.  The eigencone is the fixed stratum, while column images of
late powers form a periodic sequence of ultimate spans.

The boundary is equally sharp.  Primitive critical graphs make powers
eventually constant, but a complete two-node support already supports every
positive transient through `B_m`; therefore a weight-independent bound based
only on dimension and support is impossible.  Dropping irreducibility permits
multiple growth rates and multiple CSR terms.

The executable ledger is deliberately subordinate to the theorem.  It checks
177 matrices by an enumerative producer, an algorithmically independent
Karp/closure/Tarjan checker, and a SymPy path.  It does not infer an infinite
theorem from 177 cases.

Route A stops decisively.  Max-plus weights, support edges and critical cycles
do not intrinsically encode rational primes; CSR is a source decomposition,
not a target divisor; finite eventual periodicity supplies no target analytic
structure; and a max-plus semimodule is not a Hilbert-space quantization.
