# AS1-R3 exact denominator diagnostic and unresolved whole-circle claim

2026-09-07 UTC. This is a bounded continuation of AS1, not a new paper.

## Claim and status

The [frozen contract](FROZEN_CONTRACT.md) asks for the full meromorphic
continuation behavior of the switching solenoid zeta on
$|z|=(8\varphi)^{-1}$, with the same based words and native clock as C14.

**Whole-contract status: NOT CURRENTLY JUSTIFIED / NOT ADMITTED.**
The already proved obstruction at the two real points is retained, not
reproved or counted as a new result. The new finite-layer calculation is
exact but supplies neither an all-layer recursion nor the necessary
analytic noncancellation argument.

## Assumptions, notation and dependency map

Use the integral matrices $A,B$, their chronological left products $M$,
and the active cyclic no-$aa$ words from the original contract. Let
$S_k$ be the adjacency matrix of the reachable residue states
$(M\bmod 2^k,\text{last letter})$, with identity sentinel $e$ at length
zero, and let $f_k(M)=1_{\operatorname{tr}M\equiv1\pmod{2^k}}$.
The new scalar sequence and its generating function are

$$c_{n,k}=eS_k^n f_k,\qquad C_k(t)=\sum_{n\ge0}c_{n,k}t^n.$$

1. The inherited graph constructor defines the exact finite $S_k$; its
   earlier `main` and SCC-period diagnostic are not called.
2. The graph terminal condition agrees with the required cyclic
   condition, as proved below. For general $k$, finitely many initial
   lengths need the determinant correction.
3. A rational recurrence inferred over $\mathbb Q$ is verified by a
   dimension-sufficient exact Cayley--Hamilton certificate.
4. Polynomial gcd reduction produces the actual scalar denominator,
   distinguishing it from the full graph characteristic polynomial.
5. No step here controls $k\to\infty$ outside the known interior disk.

## 1. Observable and clock verification

The graph excludes an internal $aa$. At modulus two,
$A^2=0$. If a linearly admissible word starts and ends in $a$, cyclic
rotation of the matrix trace brings these two $A$ factors together,
so its trace is zero modulo two. Thus the trace-one terminal condition
also excludes the wraparound $aa$. A single $a$ has even trace and is
excluded. Every accepted word therefore is cyclically active, and every
active word satisfying the congruence occurs once with its original
based starting location. No primitive-orbit or reversal quotient is
taken.

The inherited determinant identity is

$$\det(I-M)=8^n-\operatorname{tr}M+1.$$

Consequently $c_{n,k}=b_{n,k}$ for $3n\ge k$, where $b_{n,k}$ is the
valuation-tail count in the earlier proof. For the computed levels
$1\le k\le6$, the only possible positive-length discrepancy is $n=1$
at $k=4,5,6$. There the active word is $b$, its trace is $7$, and
$\det(I-B)=2$; both tests are false. Hence these six computed scalar
series are the actual $b_{n,k}$ series at every positive length.
At $n=0$, the sentinel has trace $2$ and is not accepted.

For higher $k$ this initial-length check must be done again or included
as a polynomial correction. The equality is not asserted at all $k,n$
without that qualification.

## 2. Exact recurrence certificate

Let $N$ be the state dimension. The program computes $3N+1$ integer
moments, uses the first $2N+1$ in the field Berlekamp--Massey algorithm,
and obtains an order $L\le N$ and coefficients $q_0=1,q_1,\ldots,q_L$.
It checks every available residual

$$r_n=\sum_{j=0}^L q_jc_{n-j,k}\quad(n\ge L)$$

exactly, requiring at least $N$ consecutive zero residuals. This is not
an assertion that a sampled recurrence alone proves an infinite one.
Indeed, put $v=\sum_{j=0}^Lq_j S_k^{L-j}f_k$. Then
$r_{L+m}=eS_k^mv$. The degree-$N$ characteristic identity of $S_k$
propagates the first $N$ zero values to every $m\ge0$. This proves the
recurrence for all subsequent lengths.

Writing $Q(t)=\sum_{j=0}^Lq_jt^j$, the initial convolution gives
$P(t)=\sum_{n<L}(\sum_{j\le n}q_jc_{n-j,k})t^n$, so
$C_k=P/Q$. The program divides $P,Q$ by their exact gcd over
$\mathbb Q[t]$ and normalizes $Q(0)=1$. Coprimality proves that the
result is the minimal scalar denominator. A transient may make the
recurrence order exceed the denominator degree; that is not an error.

All failure tests in the new program use explicit exceptions, not
optimization-sensitive assertions. A state cap is a failure, not PASS.

## 3. Actual finite result

The [program](exact_denominators.py) ran once as
`python -B henon_dynamics/research_c419_c423/continuation_round3/spectral_recursion/exact_denominators.py`
from the repository root. Python 3.12.3, SymPy 1.14.0; exit 0. The six
layer runtimes summed to approximately 0.513 seconds; the full command
took approximately 0.797 seconds. No floating eigenvalues, expanded
precision, old `main`, or output file writes were used.

| $k$ | $N$ | recurrence order | minimal denominator degree | exact consecutive zero residuals |
| --- | ---: | ---: | ---: | ---: |
| 1 | 5 | 3 | 2 | 13 |
| 2 | 9 | 5 | 4 | 23 |
| 3 | 9 | 5 | 4 | 23 |
| 4 | 39 | 11 | 10 | 107 |
| 5 | 75 | 19 | 18 | 207 |
| 6 | 147 | 43 | 42 | 399 |

For compact exact recording, define

$$\begin{aligned}
D(t)&=(1-t-t^2)(1+t-t^2)=1-3t^2+t^4,\\
E(t)&=-(2t^3-t^2+t-1)(2t^3+t^2+t+1),\\
F(t)&=(2t^2-2t+1)(2t^2+2t+1)(t^4-t^2+1),\\
R_\pm(t)&=1+2t^2\pm4t^3+t^4\pm4t^5+6t^6
          +7t^8\pm4t^9+6t^{10}\pm4t^{11}+2t^{12}.
\end{aligned}$$

The six normalized minimal denominators are, respectively,

$$1-t-t^2,\quad D,\quad D,\quad DE,\quad DEF,\quad DEFR_+R_-.$$

At $k=5$, each closed component's characteristic polynomial contains
$(x^4-x^2+1)^2$, while the scalar denominator contains only one copy
of its reciprocal. The three closed components' repeated factors are
also not repeated three times in the scalar denominator. Thus full
matrix multiplicities cannot simply be copied into the observed pole
structure. At $k=6$ the new scalar factors have degree twelve each;
they do not establish a simple all-depth parity-only denominator.

Program SHA-256:
`0e3f71a4b18a1db39617a6dcce37c32295da750df7743fe38b9963db8e48c255`.
Imported graph source SHA-256:
`96a8ddbde573c95ad70f99e5a0fccab7ed9775e825da0733e74b274804660357`.
The latter is an integrity receipt for reused construction code, not
an independent re-verification of the previous graph theorem.

## 4. Exact missing argument and disposition

These six factorizations yield no proved inductive factor construction
for every $k$, no uniform separation of all observable nonperipheral
roots, and no estimate on a complex annulus crossing the secondary
circle. Such finite denominators cannot certify that their poles
survive the entire weighted layer sum, its logarithmic integration,
or exponentiation. The existing inside-disk tail bounds are unchanged.

The gap is mathematical, not a shortage of precision. Under the frozen
stop rule, this exact-recursion attempt ends here. The whole AS1
contract remains unclosed, with **zero added admissions**, no short
companion paper, no formal evaluator change, and no target-arithmetic
promotion. A new attempt needs a specified uniform analytic mechanism;
increasing the six-layer bound alone is not that mechanism.
