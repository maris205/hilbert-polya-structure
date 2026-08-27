# Narrative report

C192 takes a deliberately broad but mathematically closed dynamical family.  A
probability distribution on the faces of any finite real hyperplane arrangement
drives a nonreversible chamber walk through the left-regular-band face product.
Brown and Diaconis proved that the resulting transition matrix is nevertheless
diagonalizable, with every eigenvalue and algebraic multiplicity read directly
from the intersection lattice.  This turns the characteristic polynomial,
finite determinant, and all power traces into exact flat sums.

The probabilistic half is equally complete.  Separation of every hyperplane is
exactly the unique-stationarity condition.  Weighted sampling without
replacement produces a perfect stationary chamber, while the equivalent
with-replacement chamber-hitting construction gives a coupling and an explicit
total-variation estimate.  When separation fails, the correct answer is not
just “nonunique”: the hyperplanes containing the weight support cut the chain
into closed components, each with one stationary law, and the full stationary
set is their simplex.

The largest conceptual correction introduced during writing concerned strong
stationarity.  A stationary output at a stopping time does not by itself imply
independence of output and stopping time.  The primary source proves the former
sampling/coupling statements, not the latter strict SST condition.  C192 makes
that boundary executable: a repaired-hash mutation that asserts strict SST is
rejected.

The finite evidence comprises eight coordinate and braid fixtures, including
two nonseparating boundaries.  Two algorithmically independent exact-rational
implementations and a separate SymPy oracle agree on all matrices, flats,
polynomials, traces, stationary probabilities, and mixing rows.  This is strong
regression evidence but remains logically subordinate to the cited theorem.

Route A is still rejected.  The walk supplies neither a target index nor target
arithmetic information, functional symmetry, or counting law.  Its exact
finite determinant is a genuine operator-theoretic object, but without a target
divisor it is only `A4_FORMAL_HINT`.  Route B remains false.
