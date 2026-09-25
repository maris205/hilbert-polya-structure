# Broadened carrier card — ANG-20260915-CDC01

**Version:** 1, 2026-09-15; frozen before theorem claims or computations.  
**Initial status:** BROADENED HYPOTHESIS — T0--T3 OPEN.

For every integer n>=2 put L_n=max(1,n-2), J_n=Z/L_n Z with representatives
0,...,L_n-1, and C_n=Z/n Z. Freeze the entire discrete carrier

\[
Y=\coprod_{n\geq2}\{n\}\times J_n\times C_n.
\]

There is no preselected prime or chosen subset of n. Define the local test

\[
h(n,j)=
\begin{cases}
1,&j+2<n\ \hbox{and}\ j+2\mid n,\\
0,&\hbox{otherwise},
\end{cases}
\quad
F(n,j,c)=(n,j+1\bmod L_n,c+h(n,j)\bmod n).
\]

In particular n=2 uses the same guarded test, not an added prime exception.
The updated counter and scan phase are part of the complete state.

| Field | Frozen specification |
| --- | --- |
| Lineage | Divisor-exclusion prime/composite observable of 050 -> sequential local witness tests -> reversible cyclic scan retaining its whole phase and counter |
| Source change | Proper divisors rather than only divisors up to sqrt(n) are scanned; equivalence of the zero-witness test to the sieve observable must be proved |
| Broadened owner | The full uniform F action on Y and its transformation groupoid by Z, if invertibility is established |
| Permitted data | Integer arithmetic, divisibility, natural order, L_n and modulus n chosen by the displayed uniform formulas; no prime table, supplied mask, per-prime parameter or zero data |
| Distinguished observable | n, j and counter c; complete-counter displacement after the intrinsic first scan-phase return |
| Source seed | No single orbit is declared to enumerate all primes; all states retained and no n-specific initial-state selection supplies the packet ledger |
| Roof / flow | Unit roof, ((n,j,c),1) identified with (F(n,j,c),0); no logarithmic replacement permitted |
| Primitive packets | All least-period full F-orbits, modulo cyclic phase; retain every counter-derived multiplicity; reversing orientation is not an additional quotient |
| Arithmetic question | Does zero scan-return counter displacement characterize primes, and does the resulting full primitive ledger differ from nonarithmetic controls? |
| Analytic proposal | Ordinary unweighted product Z(s)=product_gamma(1-exp(-s T_gamma))^(-1), only if complete packet counting and convergence are established; operator/domain/trace OPEN |
| Controls | Suppress h; replace local h by constant one; compare counter modulus two as a separate aliasing control; full multiplicity; conserved-label versus external selected-fibre ownership |
| Classical fields | Finite-dimensional symplectic phase space and geometric realization NOT APPLICABLE; no geometric credit inherited from a nearby paper |
| Earliest tests | Inverse and complete return; prime/composite scan displacement; primitive periods and multiplicity; actual clock growth, not a manually assigned prime clock |
| Stop / advance | Stop on owner loss, nonselective return or unknown arithmetic after the early tests. If credible return selectivity survives, advance only the same frozen ordinary product; no deep unrelated operator construction |
| Route | Broadened T0--T3 labels only, formal Route coordinates UNASSIGNED; Route B NOT INVOKED |

This is not a universal simulation of an unspecified program. Whether the
particular fixed local rule supplies sufficient arithmetic naturalness remains
an explicit audit question, not assumed from the absence of a prime table.
The conserved all-integer coordinate must not be confused with a separately
chosen prime carrier or an omitted construction history.

## Audit addendum — 2026-09-15, no object change

**Current status:** ADVANCE — EXACT MARKED RETURN SELECTOR, COMPLETE PACKETS, LOCAL ORDINARY ZETA.

The [paper](paper.md) proves that a(n), the complete proper-divisor count,
is the counter displacement at first phase return, and 0<=a(n)<n. Thus the
marked scan return detects primes with no modular aliasing. With
g(n)=gcd(n,a(n)), the full n-fibre has g(n) cycles, each of length
L_n n/g(n). All counters and all composite fibres remain.

T0 and T2 are established. T1 is established for the marked arithmetic return
selector, with an explicit clock/naturalness limitation: prime p has p
cycles of length max(1,p-2), not one log-p packet. T3 is established only
for the same complete ordinary product on Re(s)>0. Its operator/trace and
global continuation remain OPEN. The bounded ordinary-product advance is
complete; no classical or formal Route coordinate is assigned.

See the [claim ledger](claim-ledger.md), [summary](README.md) and
[evidence](evidence/README.md). Route B remains NOT INVOKED.
