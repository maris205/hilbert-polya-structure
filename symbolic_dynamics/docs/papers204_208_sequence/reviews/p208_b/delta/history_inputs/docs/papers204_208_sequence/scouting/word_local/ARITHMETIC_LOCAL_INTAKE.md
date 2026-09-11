# Two cyclic arithmetic literals — fixed before pilot execution

2026-09-06 UTC. Root author scout; no candidate number or reserve.
These are new bounded literals, not permission to enlarge earlier failed
word/rank/contrast boxes. The two arithmetic rules can at most support one
seat if they prove to share a mechanism; no independence is presupposed.

| Code | Finite carrier and literal synchronous update | Fixed complete boxes |
|---|---|---|
| CPRM | $y\in\{1,\ldots,m\}^n$, $T(y)_i=1+((y_i-1)\bmod y_{i+1})$ | $n=2,\ldots,6$, $m=1,\ldots,6$ |
| CSGD | $x\in\{0,\ldots,m\}^n$, $D(x)_i=x_i-\gcd(x_i,x_{i+1})$, with $\gcd(0,0)=0$ | $n=2,\ldots,6$, $m=1,\ldots,5$ |

Coordinates are labelled modulo $n$; every right side uses the old word.
The positive remainder in CPRM is integral to the literal, not a
post-pilot failure completion. CSGD's zero value is a carrier element.
Only complete functional graphs at these boxes are planned. The inverse
histogram/maximizer list and transient distribution are observations, not
all-parameter proofs. No randomized or larger-cutoff rescue is authorized.

## Pre-pilot mathematical deductions, all zero-credit background

CPRM is coordinatewise nonincreasing. Equality in every coordinate forces
$y_i\le y_{i+1}$ all around the cycle, hence a uniform word. It therefore
converges by finite monotone descent. More precisely let
$q_i=\lfloor(y_i-1)/y_{i+1}\rfloor$. Some $q_i=0$ (take a minimum
coordinate), and $Ty=(I-\operatorname{diag}(q)S)y$, with $S$ the cyclic
next-coordinate matrix. The coefficient matrix has determinant
$1-\prod_iq_i=1$ and integer inverse. Thus the gcd of all coordinates is
preserved and the terminal uniform value is that original gcd. The
unimodular Euclidean reduction, termination argument and ordinary gcd-basin
Möbius inversion alone will not be treated as two residual axes.

For CSGD, each positive coordinate decreases by at least one at every
update and zero coordinates stay zero. Therefore $D^m=0$ on the whole
carrier. This elementary bound by itself is not a substantive temporal
advance. At $n=2$ the coordinate difference is invariant until one dies,
and the common gcd is $\gcd(x_0,x_0-x_1)$, so the trajectory reduces to
a scalar translation-by-gcd process; compare P128 and P184. Those two-site
claims cannot be presented as a new mechanism. No all-$n$ sharp clock or
all-target extremum has been proved for this scout.

Other arithmetic rules excluded without numerical-row credit: cyclic
lcm quotients have primewise truncated-difference dynamics already owned
by P187; simple quotient erosion and scalar divisor-count feedback supply
no established independent two-axis contract. P131's actual rational
quotient-queue definition was read: it rotates continued-fraction digits
and absorbs terminal ones, not CPRM's simultaneous least-positive remainders.
That literal difference is not a novelty certificate.

## Initial source scope

Internal searches covered parallel Euclidean, simultaneous remainder,
positive remainder, and cyclic quotient wording in scouting/proof ledgers.
Initial web queries were `"parallel Euclidean algorithm" cyclic remainder`,
`"cellular automata" "greatest common divisor" remainder`, and
`"cyclic Euclidean" algorithm simultaneous`. They supplied no exact
primary-body adapter; unrelated additive-CA/GCD and generic algorithm
search hits were not used as evidence of either novelty or ownership.
Any surviving signal still needs focused primary-body and internal
mechanism comparisons before a candidate gate. HOLD_EXTERNAL.

## Preserved first-execution failure and exact scope correction

The combined first execution completed all 30 CPRM rows, then exited one
at CSGD's first carrier-invariance assertion. The initial CSGD claim that
zero coordinates stay zero was **false**: $\gcd(0,b)=b$, so the declared
literal sends $(0,1)$ to $(-1,0)$ outside its proposed carrier. Its
pre-pilot convergence paragraph is therefore withdrawn in its entirety;
it is preserved above to expose the actual failed reasoning, not accepted
mathematics. This literal is **KILL_ILL_DEFINED_ON_DECLARED_CARRIER**.
No zero-guard, clipping rule or selectively frozen singular branch is added.

The exact failed program is `arithmetic_local_pilot.failed_v1.py`; all
30 completed CPRM rows and the complete traceback are preserved as
`ARITHMETIC_LOCAL_FAILED_V1.stdout` and `.stderr`. The files were renamed,
not deleted. The corrected runner executes only the unchanged CPRM rule
on the same 30 original boxes. It reports the existing profiler's image,
cycle census, height/witness and maximum fibre, not a full target-vector
or full depth histogram. Those richer prospective reports have not been
implemented and are not claimed as artifacts. The combined failed program
exit is not a successful canonical production.
