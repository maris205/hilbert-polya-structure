# HCS-C220 narrative report

Open TASEP supplies a genuinely non-equilibrium owner: particles are
injected, move through a hard-core chain, and are removed.  The paper freezes
one physical clock and one normalized bulk rate, then gives a single theorem
chain rather than splitting the model into unrelated calculations.

The first layer is finite and exact.  The generator has \(2^L\) states, and
the DEHP relation \(DE=D+E\) reduces every configuration word to a rational
function of the two boundary rates.  Summing those words gives the
ballot-number normalization \(Z_L\).  An independent rational generator check
then verifies \(\pi Q=0\), the nullspace dimension, and equality of all bond
currents.  The closed formula is tested both away from and on the
\(\alpha=\beta\) divided-difference diagonal.

The second layer records the analytic thermodynamic atlas: left-density,
right-density, maximal-current, shock/coexistence, the two critical faces,
and their multicritical corner \(\alpha=\beta=1/2\).  The coexistence row is
restricted to the positive-rate line \(0<\alpha=\beta<1/2\); its endpoint
\((0,0)\) belongs only to the zero-rate boundary theorem.  The JSON rows deliberately say that finite observations are
regression sentinels, not a numerical proof of an \(L\to\infty\) statement.
Zero-rate faces are not hidden in a limiting denominator: they are separate
absorbing-chain theorems, including the \(L=0\) and \(L=1\) controls.

On the double-zero face there are \(L+1\) absorbing extreme points.  The
normalized stationary family is the simplex on these absorbers and therefore
has affine dimension \(L\); the separate linear nullspace field records
\(L+1\) basis directions.

The result is a substantial source theorem but not an arithmetic bridge.  Site
indices, rates, and matrix words have no intrinsic primitive-orbit or target
divisor semantics.  The honest Route-A tuple is
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT), and Route B remains
unauthorized.  No priority or novelty claim is made for TASEP or its phase
diagram.
