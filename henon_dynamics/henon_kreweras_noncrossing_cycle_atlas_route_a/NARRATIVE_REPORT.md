# Narrative report

HCS-C209 freezes a genuinely different finite dynamical subtype from the
tableau-promotion lane: the ordinary Kreweras complement on noncrossing set
partitions.  The key step is to keep two clocks separate.  The actual map has
order 1, 2, or 2n at n=1, n=2, or n>=3, while the source CSP is naturally
indexed by the abstract order-2n cyclic group (with a kernel at n=2).  Once
this is explicit, the odd and even root rows agree exactly with direct integer
formulae.

The package closes more than a fixed-point table.  Mobius inversion gives every
least-period population and cycle count; each cycle contributes one elementary
factor to the finite Artin--Mazur zeta and the reciprocal Koopman determinant;
the same ledger gives every root-of-unity multiplicity.  Rank complementation
and all polygon reflections provide a concrete dihedral reversor.  These are
complete consequences for the frozen finite source, not fitted observations.

The independent checker constructs all set partitions through n=8, filters
crossings, computes p_pi^(-1)c, and verifies the map, orientation, rank, fixed
rows, cycles, and reflections.  SymPy independently reconstructs the
q-Catalan polynomials and their cyclotomic remainders.  Replay and mutation
tests close the reproducibility and tamper-detection gates.

The result intentionally stops at the source boundary.  Catalan size and
polygon time have no intrinsic rational-prime carrier, so the route verdict is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` and Route B is not
opened.
