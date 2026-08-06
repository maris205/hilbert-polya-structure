# R058 Hyperbolic Survivor and Filament Replication Manifest

**Frozen:** 2026-08-02, before R058 production  
**Protocol SHA-256:** `bdd851ac14fb5cbe89ce4592b4f0e9f6cbe4fa4b76778530a2e19e7e0f1dd6f3`  
**Primary object:** an exact four-h-set covering/cone certificate for \(H_6\)  
**Supporting object:** three locked exact true-positive 4x refinement lineages

## 1. Why this run exists

R056 supplied a filament-compatible finite-grid observation but no common orbit
witness. R057 supplied an exact local incidence criterion but also showed that
closed mutual filtering is not universal. R058 therefore separates two tasks:

1. build a small exact hyperbolic survivor whose orbit existence does not rely
   on an incidence path;
2. test the R056 true-positive lineage signature on a fully new locked batch.

The first task is the paper-relevant upgrade. The second is an independent
replication attempt and may fail without changing the first result.

## 2. Frozen h-sets and transition graph

For

\[
H_6(x,y)=(1-6x^2-y,x),
\]

freeze

\[
X_\pm=\pm[1/3,5/8],\qquad
Y_\pm=\pm[5/16,81/128],
\]

and \(N_{st}=X_s\times Y_t\). The \(X\)-interval is strictly inside the
same-sign \(Y\)-interval. With state order \(--,-+,+-,++\), the claimed
covering matrix is

\[
A=
\begin{pmatrix}
1&0&1&0\\
1&0&0&0\\
0&1&0&1\\
0&1&0&0
\end{pmatrix}.
\]

Its exact characteristic polynomial must be

\[
(\lambda^2-\lambda-1)(\lambda^2+1),
\]

so \(\rho(A)=\varphi\).

## 3. Frozen theory claim and downgrade rule

The strongest permitted claim, only if every B0--B2 gate passes, is:

> There exists a nonempty compact uniformly hyperbolic invariant survivor
> subset with a continuous surjective itinerary map onto the four-state
> subshift, and its topological entropy is at least \(\log\varphi\).

This wording requires both exact covering/cone inequalities and an audited
bi-infinite itinerary-realization theorem. If the last theorem gate remains
unresolved, R058 must downgrade to local exact covering/cone diagnostics and
delete invariant-set and entropy wording.

R058 does not claim conjugacy, entropy equality, a Markov partition, or that
the entire R056 SCC is the certified set.

## 4. Exact geometry and cone quantities

The smallest required exit-crossing margin is \(1/48\). The smallest margin
placing \(H_y=x\) strictly inside the target entry interval is \(1/128\).

In affinely normalized h-set coordinates, freeze cone width
\(\kappa=1/2\). The exact forward unstable and backward stable slope bounds
are

\[
\frac{25088}{95079}<\frac12,\qquad
\frac{15129}{45388}<\frac12.
\]

Both directions must also have a strict expansion factor greater than one.

## 5. Locked true-positive lineages

The nine configurations are produced as one batch:

- centered: \(112@0\to224@0\to448@0\);
- positive phase:
  \(113@1/12\to226@1/6\to452@1/3\);
- negative phase:
  \(113@-1/12\to226@-1/6\to452@-1/3\).

These are exact nested 2x steps. The pre-freeze uncapped adaptive maxima are
31 for centered and 37, 43, 62 across the shifted levels. Any cap activity is
a hard integrity failure.

The primary branch is always the canonical largest multi-node true-positive
SCC followed by the matched-support largest multi-node descendant. Closed
graphs cannot replace a failed positive lineage.

For each chain, if \(S_N\) is the level-zero lineage size and \(S_{4N}\) the
level-two size, freeze

\[
d_c=\frac{\log(S_{4N}/S_N)}{\log 4}.
\]

Success requires increasing lineage size, decreasing exact cell-union area,
\(d_c\in[0.85,1.20]\), a nontrivial descendant at both levels, and descendant
lifted-area coverage in \([0.35,0.65]\) at each step.

## 6. Failure-oriented controls

- Nine grids are inseparable as one locked batch.
- No grid, phase, threshold, or branch tie rule may change after production.
- R057 closed-margin status is recorded only as a sidecar.
- Every cap event, branch switch, exact projection failure, or negative
  replication remains reportable.
- The finest-grid h-set bridge is a finite diagnostic and cannot prove C1.

## 7. Scope boundary

R058 cannot establish graph-limit or transfer-operator convergence. It has no
zeta, prime, Riemann-zero, RH, or Hilbert--Pólya consequence. The exact
hyperbolic subset, if certified, is deliberately conservative and need not
exhaust the full \(a=6\) horseshoe.
