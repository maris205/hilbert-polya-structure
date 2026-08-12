# SD-C05 — Recursive Wheel-Sieve Level Shift

## Frozen construction

\[
Q_1=q_1=2,\qquad
q_{k+1}=\min\{n>q_k:\gcd(n,Q_k)=1\},\qquad
Q_{k+1}=Q_kq_{k+1}.
\]

The canonical residue Bratteli graph unpacks this recurrence.  At level \(k\)
its vertices are

\[
R_k=\{0\le r<Q_k:\gcd(r,Q_k)=1\}.
\]

If \(q=q_{k+1}\), a vertex \(r\in R_k\) has edges to

\[
r+jQ_k\in R_{k+1},\qquad 0\le j<q,
\]

except for the unique branch divisible by \(q\).  Every edge goes from level
\(k\) to \(k+1\).  Its scale roof is

\[
\tau_k=\log(Q_{k+1}/Q_k).
\]

No reset edge, prime-labelled component, potential, or cocycle is allowed.
The function space used for finite checks is the cylinder algebra on this
one-sided path space.  The periodic-point convention is Artin–Mazur:
the proved empty fixed sets give \(\zeta_{\rm AM}=1\) and
\(D_{\rm AM}=1\).

## Findings

- **PROVED:** \(q_k\) is exactly the \(k\)-th rational prime.
- **PROVED:** the scale roof is therefore \(\tau_k=\log q_{k+1}\), derived
  from the recursive primorial ratio rather than assigned to a prime symbol.
- **PROVED:** every path strictly increases its level, so
  \(\operatorname{Fix}(\sigma^n)=\varnothing\) for all \(n\ge1\).
- **A1_FAIL:** the strongest endogenous rational-prime generator found has no
  primitive periodic orbits and no canonical periodic-orbit determinant.

Adding a reset or splitting the system into prime-indexed components would
alter the frozen grammar precisely to manufacture cycles, so it is forbidden.
The candidate stops before Route B.

## Artifacts

- [Proof package](PROOF_PACKAGE.md)
- recursion checks under the session-level code/ and results/ directories
