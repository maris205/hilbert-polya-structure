# HCS-C57 machine results

Status: `PREFREEZE_CODE_RESULTS_PASS` after the canonical producer/checker
replay; documentation and project status remain `PAPER_PENDING`.

The exact machine package binds the frozen HCS-C56 cubic and proves the
following machine gates: the degree-10 incidence carrier on all 27 lines; the
135-edge Schläfli graph with 72 sixers and 36 double-sixes; the exact
group/Picard and cohomology calculations; candidate-blind degree-36 theta and
delta CRT resolvents and their irreducibility certificates; the exact
degree-12 carrier identity; and the canonical rank-30 determinant quartic
minor with all restriction residuals zero.  The divisor/quaternion conclusion
also records the written Hilbert-90, norm-divisor, Picard coboundary and
Hochschild-Serre class-map bridges as written proof obligations rather than
mislabeling them as machine output.

The five deterministic gzip evidence objects are semantic inputs: the checker
decompresses them, enforces canonical JSON and deterministic recompression,
and independently replays their arithmetic.  Compression hashes alone are
not treated as proof.

The direct PARI characteristic-zero incidence factor lane timed out and is a
non-result.  The expanded quartic and delta-as-a-polynomial-in-theta lanes are
bounded non-results.  None is a theorem dependency.  No local evaluation,
Brauer-Manin obstruction, rational-point, paper-completion, or release claim is
made here.
