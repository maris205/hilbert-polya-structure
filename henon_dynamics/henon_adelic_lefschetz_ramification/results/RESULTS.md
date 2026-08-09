# HCS-C23 first-gate results

## Main result

Full Galois packet norm preserves chronology for both hard controls:

- at \(\ell=11\), the period-seven same-bigram pair has norm-divisibility
  vector \([1,0]\);
- at \(\ell=3\), the period-eight same-trigram pair has vector \([0,1]\).

The exact multiplication-kernel dimensions are respectively

\[
[1,0],\qquad[0,1].
\]

The event sides have explicit residue-degree-one fixed points, while the
zero-dimensional multiplication kernel on the paired side proves absence
over the full algebraic closure.

## Frozen prime scan through 43

Nonzero \(r=1\) rows are:

| Pair | Prime | Kernel dimensions |
|---|---:|---:|
| \(n=8\) | 3 | \([0,1]\) |
| \(n=7\) | 7 | \([2,4]\) |
| \(n=7\) | 11 | \([1,0]\) |
| \(n=7\) | 13 | \([0,1]\) |
| \(n=8\) | 13 | \([0,3]\) |
| \(n=8\) | 17 | \([0,1]\) |
| \(n=8\) | 29 | \([0,1]\) |

All other degree-good prime rows through 43 are explicitly present with
zero kernel dimensions.  Prime 7 divides both period-seven packet norms; its
different kernel dimensions are **not** called different norm valuations.

## Repetition fingerprints

At \((w,\ell)=(0001001,11)\), the event repetitions through twelve are

\[
3,6,9,12.
\]

At the period-seven event word \(0000101\), and at the period-eight event word
\(00101101\) over \(\mathbb F_3\), every repetition through twelve is an
event because a multiplier one is already present at \(r=1\).  The paired
word \(00101011\) has no event through twelve at \(\ell=3\).

These divisor-closed patterns are required cyclotomic controls, not a new
Zsigmondy signal. More strongly, with

\[
P_w(X)=\operatorname{Norm}_{A_w/R}(X^2-t_wX+1),
\]

the complete fixed-word tower satisfies

\[
\Delta_{w,r}=\operatorname{Res}_X(P_w(X),X^r-1).
\]

It is therefore a classical cyclic-resultant sequence.

## Verification

- producer release checks: pass;
- independent checks: 12/12 pass;
- mutation tests: 11/11 pass;
- cyclic rotations: invariant;
- reversal: equal and retained, not quotiented;
- averaged dynamics: absent.

## Decision

`CLOSED_AT_CYCLIC_RESULTANT_BASELINE`.

The fast kill “chronology vanishes after Galois packetization” is refuted,
but that finite separation does not create a new arithmetic mechanism. No
explicit all-period cross-word law was frozen before the proposed extended
ledger, so the broad scan is cancelled. The exact chronology certificate and
finite-flat implementation are retained; an Euler product remains forbidden.
