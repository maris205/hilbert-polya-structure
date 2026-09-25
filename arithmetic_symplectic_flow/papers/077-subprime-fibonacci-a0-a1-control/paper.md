# Conway's subprime-Fibonacci map is an endogenous prime-recognition recurrence with actual cycles, but not yet a symplectic carrier

**Paper ID:** 077-subprime-fibonacci-a0-a1-control  
**Record ID:** ASFS-SCOUT-20260914-52  
**Date / status:** 2026-09-14; A0 SYMBOLIC POSITIVE CONTROL; A1 PROVES_TOO_MUCH / PRE-P0 STOP  
**Route state:** No classical ASFS Route-A coordinate; Route B NOT INVOKED.

## Frozen arithmetic object

For positive integers define

\[
s(n)=
\begin{cases}
n,& n\text{ is prime},\\
n/\operatorname{lpf}(n),& n\text{ is composite},
\end{cases}
\qquad
T(x,y)=(y,s(x+y)),
\]

where lpf(n) is the least prime factor. This is precisely the second-order
subprime-Fibonacci update expressed as one autonomous map on ordered pairs.

Unlike a prime-labelled horseshoe or a finite wheel, the primality/compositeness
branch is evaluated by T's own defining arithmetic rule at every state. No list
of primes, chosen modulus, finite prime word, or temporal parameter schedule is
an input. This gives a direct, though non-Eratosthenes, realization of the
prior-work arrow

prime/composite observable -> symbolic/arithmetic sequential deformation.

## Same-object source control and periodic-ledger failure

The cited study describes subprime-Fibonacci sequences as generally terminating
in a handful of cycles and investigates their cycle structure. Thus actual
recurrence is present in the same state update that evaluates the arithmetic
rule. For any concrete period-r state cycle

\[
z,Tz,\ldots,T^{r-1}z,\qquad T^r z=z,
\]

repetition is unambiguous: iterating r times again returns to z, and the orbit
repeats by concatenation. No roof, prime-log clock, complete cycle
classification, or zeta product is inferred.

However the exact full ledger immediately supplies an adverse control. For every
integer n >= 2, the number 2n is composite and has least prime factor 2. Hence

\[
T(n,n)=(n,s(2n))=(n,n).
\]

There are therefore infinitely many fixed states, including all diagonal
composite states such as (4,4), (6,6), and (9,9). The same map that internally
recognizes primes does **not** make periodicity a prime-selective feature. This
is stronger than merely observing extra cycles in finite data: it is an exact
infinite family in the complete state space.

| Required feature | Status |
| --- | --- |
| endogenous arithmetic source | established at the discrete-rule level |
| one fixed action | established: T |
| actual state recurrence | exact diagonal fixed family plus source-backed nontrivial cycles |
| primitive/repetition convention | exact for any verified T-cycle; global ledger PROVES_TOO_MUCH |
| prior-work Hénon/conservative lift | not supplied |
| symplectic map / positive roof / suspension | not supplied |
| transfer operator / determinant | not supplied |

## Decisive A1 and geometric boundaries

The exact carrier is N_{>0}^2, a discrete set rather than a positive-dimensional
smooth symplectic manifold. Moreover T is not injective:

\[
T(2,1)=(1,s(3))=(1,3)
\quad\text{and}\quad
T(5,1)=(1,s(6))=(1,3).
\]

Therefore T is not a diffeomorphism or an area-preserving Hénon-type map on this
carrier. A natural extension, reversible computation, cotangent construction,
or a geometric embedding would be a new object and must independently preserve
the internal s rule **and** the adverse diagonal fixed family. Existing generic
reversible-simulation and post-selected-lift controls prevent claiming that
such an owner is automatic.

| Gate | Result | Reason |
| --- | --- | --- |
| lineage/A0 source precheck | endogenous symbolic positive control | fixed prime/composite and lpf rule |
| A1 precheck | scoped FAIL / PROVES_TOO_MUCH | every diagonal n >= 2, prime or composite, is fixed |
| classical P0 geometry | STOP | discrete, noninjective T; no symplectic owner |
| A2 | NOT EVALUATED | no same-object roof/determinant |
| Route B | NOT INVOKED | no Route-A-ready classical candidate |

## Decision

**Portfolio position: stop/fork.** The s rule remains a useful endogenous
arithmetic-source control, but its exact periodic ledger is not prime-selective.
Do not seek a geometric lift merely to retain selected nontrivial cycles while
discarding the diagonal family. Any future related candidate must alter the
arithmetic state rule itself, then be frozen independently and audited for both
internal prime selection and its *complete* periodic ledger.

## Evidence index

- Guy, Khovanova, Salazar, [*Conway's subprime Fibonacci sequences*](https://arxiv.org/abs/1207.5099)
- Caragiu, Vicol, Zaki, [*On Conway's subprime function, a covering of N and an unexpected appearance of the golden ratio*](https://fq.math.ca/Papers1/55-4/CaragiuVicolZaki03162017.pdf)
- [011 reversible sieve simulation control](../011-reversible-sieve-simulation-control/paper.md)
- [050 causal binary-sieve fixed-point control](../050-causal-binary-sieve-fixed-point-screen/paper.md)
- [076 direct-lineage breadth frontier](../076-breadth-frontier-cycle-08/paper.md)
