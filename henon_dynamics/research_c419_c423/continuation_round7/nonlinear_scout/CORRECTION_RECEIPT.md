# AY7 second-invariant correction

2026-09-08 UTC. The coordinator found this issue while independently
reading the completed nonlinear scout. This receipt corrects the invariant
and source-scope passage only. The frozen map, parameter, clock, domain,
classification question and `CHEAP_CHECKS.md` are unchanged.

## Error and exact countercheck

The initial report wrongly claimed that
$$
I_{2,\mathrm{old}}=pqrs+ps+qr+kpq
$$
is invariant for
$$
Y_k(p,q,r,s)=(r-kp/(1+ps),\ s,\ p,\ q+ks/(1+ps)).
$$
The coordinator's ordinary integral transition
$$
k=5,\qquad(1,2,3,4)\longmapsto(2,4,1,6)
$$
has forward denominator $5$ and reverses under the displayed inverse.
Here $I_{2,\mathrm{old}}$ changes from $44$ to $104$. This is a
one-step hand counterexample, not a periodic-orbit claim or a program run.

The correct invariant, now in the report, is
$$
J=pqrs+ps+qr+krs.
$$
It takes the value $94$ at both states. Equivalently one may use
$pqrs+ps+qr-kpq$, since $I_1=pq+rs$ is invariant and
$J-kI_1=pqrs+ps+qr-kpq$.

## General hand verification

Put $D=1+ps\ne0$, $h=k/D$, $K=pqrs+ps+qr=Dqr+ps$, and denote
the updated coordinates by primes. Directly from the frozen map,
$$
p'q'=(r-hp)s=rs-hps,\qquad
r's'=p(q+hs)=pq+hps.
$$
Writing $d=rs-pq-hps$ gives
$$
p'q'-pq=d,\qquad r's'-rs=-d,
$$
and therefore $I_1'=I_1$. Also
$$
K'=D(r-hp)(q+hs)+ps,
$$
so
$$
K'-K=Dh(rs-pq-hps)=kd.
$$
Hence $J'-J=kd+k(-d)=0$ for every ordinary input, whereas
$I_{2,\mathrm{old}}'-I_{2,\mathrm{old}}=2kd$, generally nonzero.
This verifies the correction without any external preservation claim.

## Primary-source discrepancy, not a silent reparametrization

[Kassotakis, SIGMA 15 (2019), 048, Example 2.4, printed p. 7](https://sigma-journal.com/2019/048/sigma19-048.pdf)
prints the base polynomial plus $a x_1x_2+b x_3x_4$ together with the
displayed map using $a-b$ in the signs frozen here. Those two printed
formulas are incompatible as an invariant/map pair with fixed parameters.
The initial report copied the coefficient assignment faithfully but
failed to verify preservation; responsibility for that unchecked claim
remains with this report. No source amendment or author intent is inferred.

A second primary source resolves the convention:
[Konstantinou-Rizos–Mikhailov, 1205.4910v3, Section 4.1.1, equations (28)–(31)](https://arxiv.org/pdf/1205.4910)
gives the same map and the invariant
$$
(a+pq)(b+rs)+ps+qr+1
=K+b pq+a rs+ab+1.
$$
With $(a,b)=(k,0)$, deleting the constant $1$ gives $J$ exactly.
Its canonical Poisson brackets and Liouville-integrability discussion
remain classical ownership, not a new claim of the scout.

Actual additional source access: the 2019 PDF's affected Example 2.4
was reopened; the arXiv PDF served version 1205.4910v3, whose abstract
and Section 4.1.1, equations (25)–(32), were read. No full-paper reading
or original 1994-paper access is claimed. Two fresh correction queries:

1. `"Adler-Yamilov" "invariants" "a" "b" "x_1"`
2. `"Darboux transformations, finite reduction groups and related Yang-Baxter maps"`

Search aggregators were discovery only. No mathematical program was
executed, no source PDF saved and no old check rerun.

## Dependency impact and disposition

The auxiliary AY height proof uses only the displayed update, its divisor
condition, the two scalar recurrences and periodic telescoping sums. It
never uses either invariant. `CHEAP_CHECKS.md` therefore remains unchanged.
Neither the original full AY atlas nor any new admission follows from
this correction. The AS1 proof-review task is separate and resumes after
this scoped repair.
