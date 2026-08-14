# SD-C22 Implementation Notes

## Endpoint convention

The authority code follows the exact prototype: after the final square test,
the former terminal acceptance edge is redirected directly to the input,
\(T_{p,m+1}\to I_p\). There is no separate \(A_p\) vertex on the recurrent
cycle. Consequently

\[
\ell(p)=2+\sum_{d=2}^{m}\left\lceil p/d\right\rceil.
\]

Retaining a separate accept vertex would add one edge but would not change
the asymptotic or compactness theorem. It is not the frozen convention.

## No-oracle representation

The verifier-forward-path routine materializes actual input, trial, quotient,
and reject states. Its transition branch uses successor, multiplication, and
order comparison only. The independent Eratosthenes sieve is confined to
validation. Reject paths terminate in the first recorded cemetery state; the
mathematical graph continues as a one-way ray and never adds a reject loop.

## Analytic boundary

For any accepted cycle, the code stores the exact cycle product rather than
pretending that a finite matrix establishes an infinite Fredholm theorem.
The proof gives

\[
B_{p,s}^{\ell(p)}=p^{-s}I,\qquad
\|L_s\|_{\mathrm{ess}}=1.
\]

The uniform roof minimizes the maximum edge weight and is therefore the most
favorable allocation for compactness. Concentrating the roof makes some edge
weights exactly one.

## Marker firewall

The raw graph-step block factor is \(1-z^{\ell(p)}p^{-s}\); first return gives
\(1-zp^{-s}\). Exact rational products through 31 agree at \(z=1\) and differ
at \(z=1/3\). The induced return operator is the Paper 04 diagonal loop system
and is not relabeled as the whole recurrent operator.

## Provenance

The Route-A YAML initially contains PENDING_FIRST_ARTIFACT_COMMIT for both
source and code commits. A later authority commit must replace all three
paired placeholders, including source_lock.code_commit, with the same
40-character lowercase commit hash. This integration performs no Git
operation.
