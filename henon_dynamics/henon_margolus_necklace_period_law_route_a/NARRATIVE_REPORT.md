# C165 narrative report

C165 changes dynamical subtype rather than extending Rule 90 for a fourth
consecutive round.  The replacement is a binary Margolus partitioned cellular
automaton whose clock is a complete pair of staggered swap layers.

The central step is a relabelling that is easy to miss if adjacent sites are
paired naively.  Even cell labels advance by two while odd labels retreat by
two.  Pairing even site `2j` with reversed odd site `1-2j` makes both entries
advance under the same cyclic index.  The full configuration system is thus
exactly a four-letter necklace rotation.  That conjugacy, rather than a finite
table, owns the fixed-point law `4^gcd(m,n)` and the complete Moebius period
classification.

The same description yields a quantitative result: configurations of
non-full period occupy at most `m/2^m` of the state space.  This estimate is
uniform and transparent, though not promoted as sharp.  The smallest rings
are retained explicitly: the full tick at `m=1` is the identity, and at
`m=2` there are four fixed configurations and twelve configurations in six
two-cycles.

Reflection reverses the counterpropagating cell motion.  Consequently the
finite Koopman permutation is a source-natural same-clock unitary, its
ordinary determinant is the inverse source zeta, and reflection plus complex
conjugation supplies an antiunitary time reversal.

The exact solvability is also the principal obstruction.  This model is not
claimed to be chaotic or interacting, and its finite Koopman unitary is not a
uniform self-adjoint target operator.  A2 and A3 therefore remain failures, Route B
is disabled, and the result stays Route-A exploratory.
