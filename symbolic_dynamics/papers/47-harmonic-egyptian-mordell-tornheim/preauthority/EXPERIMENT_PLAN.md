# Claim-Driven Experiment Plan — Paper 47

## Status

PREAUTHORITY / RESULTS UNSEEN / OUTPUT SET NOT YET FROZEN

## Claim matrix

| ID | Claim | Primary executable check |
|---|---|---|
| C1 | direct divisibility equals the coprime-scale parameterization | exhaustive ordered-edge equality |
| C2 | divisor-row coordinates equal the same support | exhaustive row equality |
| C3 | loops are exactly even vertices | exact cutoff equality |
| C4 | phase walls are \(0,1/2,1\) with strict endpoints | proof-backed endpoint certificates |
| C5 | first trace is \(2^{-s}\zeta(s)\) | exact diagonal equality |
| C6 | second trace is primitive MT times \(\zeta(2s)\) | direct matrix versus independent series |
| C7 | a mixed triangle exists and PSD is false | exact witnesses |
| C8 | every hostile mutation is rejected | exact designated-consumer outcomes |

## Frozen grids

- ordered vertex cutoffs \(N\in\{16,32,64,128\}\);
- full row audit for \(1\le m\le128\);
- coprime \(1\le a,b\le64\), with all \(t\) producing endpoints at most
  \(128\);
- closed-walk lengths \(1\le r\le5\) at \(N\in\{16,32\}\);
- exact rational trace parameters \(s\in\{2,4\}\);
- rectangular primitive/full MT cutoffs \(B\in\{16,32,64,128\}\);
- interval diagnostics at
  \(\sigma\in\{0,1/4,1/2,3/4,1,5/4,2\}\);
- divisor endpoint controls on squarefree products of the first
  \(1,\ldots,8\) primes.

## Evaluator independence

Evaluator D begins with ordered pairs and the remainder of \(mn\) modulo
\(m+n\). Evaluator P begins with coprime pairs and scale, plus a separate
divisor enumeration for rows. Neither may import the other's edge predicate,
fixtures, expected tables, trace routines, or mutation outcomes.

## Exact trace tests

Write \(A_N=P_NE_sP_N\), where \(P_N\) projects onto vertices
\(1,\ldots,N\), and write
\(H_M^{(u)}=\sum_{t=1}^{M}t^{-u}\). The exact finite identities are

$$
\operatorname{Tr}A_N
=2^{-s}H_{\lfloor N/2\rfloor}^{(s)},
$$

and

$$
\operatorname{Tr}(A_N^2)
=\sum_{\substack{a,b\ge1\\(a,b)=1}}
[ab(a+b)^2]^{-s}
H_{\left\lfloor N/((a+b)\max(a,b))\right\rfloor}^{(2s)},
$$

with terms having zero harmonic cutoff omitted. In particular, the finite
scale cutoff depends on \((a,b)\); no common \(\zeta(2s)\) may be extracted
from a finite matrix.

For \(s=2,4\):

1. form \(\operatorname{Tr}(A_N^2)\), with \(A_N=P_NE_sP_N\), by exact
   finite-matrix multiplication;
2. sum exact ordered edges directly;
3. generate the same edge set from \((t,a,b)\);
4. evaluate the displayed finite scale-sum with the same endpoint cutoff;
5. compare primitive and unrestricted MT truncations in an independent
   rectangular gcd-extraction control:

   $$
   \sum_{1\le p,q\le B}[pq(p+q)^2]^{-s}
   =\sum_{\substack{u,v\ge1\\(u,v)=1}}
   [uv(u+v)^2]^{-s}
   H_{\lfloor B/\max(u,v)\rfloor}^{(4s)}.
   $$

The first four projections must agree on the identical vertex endpoint
domain. The fifth is a separate rectangular-domain identity. The infinite
\(\zeta(2s)\) and \(\zeta(4s)\) formulas are analytic proof certificates
only; neither is inferred from a finite cutoff.

## Mutation consumer contract

`THEOREM_FALSIFIERS.md` freezes the exact designated-consumer key set and
exact rejection code for every F01--F15 row. A negative row survives if any
designated consumer is missing, any unlisted consumer key is present, any
consumer returns zero/acceptance, or any returned code differs from the
frozen code. Registry rows, emitted adversarial records, and the read-only
auditor must agree on this entire mapping byte-for-byte.

## Mutation families

- source relation, loops, weight, clock, and marker;
- gcd, scale, orientation, ordered/unordered multiplicity, and quotient;
- all three endpoint equalities and quantifiers;
- MT scale and primitive factors;
- trace and determinant domains;
- positive-semidefinite misclassification;
- missing mixed cycle;
- raw JSON key, order, duplicate, and scalar-type variants;
- result/report/ledger coordinated tampering;
- output deletion, rename, extra, unsafe path, and symlink;
- evaluator check-map add/delete/rename;
- mutation-registry omission;
- Route tuple, Route-B, and provenance states;
- cache, auxiliary, host-token, and hostile-environment controls.

## Acceptance

- ordered support mismatch: zero;
- row mismatch: zero;
- trace mismatch: zero;
- theorem failures: zero;
- mutation survivors: zero;
- designated consumer-key mismatch: zero, with exact key-set equality and
  the frozen rejection code from every designated consumer;
- all reports reconstruct exactly from the sealed science object;
- first install changes only the declared output paths;
- internal and external reruns replace zero paths;
- forced late failure leaves the target tree and metadata unchanged.

## Interpretation

Successful computation validates two implementations and frozen witnesses.
It does not establish the theorem, external novelty, or a Route-A target.
