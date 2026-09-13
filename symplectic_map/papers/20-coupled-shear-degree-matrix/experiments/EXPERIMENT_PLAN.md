# Paper20 — Experiment and Verification Plan

## Authorization state

**No scientific experiments are authorized for this source-design package.**
The proposed result is a symbolic theorem about one explicit family. Numerical
orbits, random coefficient sweeps, CAS enumeration, benchmarking, and plots
would not prove the selector induction and are intentionally excluded.

## Proof-only verification sequence

The following are hand-checkable proof tasks, not experiments:

1. Expand \(\nabla V_g\) and \(\nabla W_g\) exactly.
2. Match each selected monomial to its row in \(A_g\) or \(B_g\).
3. Verify the strict inequalities for the ratio interval
   \([1,(g-2)/2)\) symbolically.
4. Verify carried-coordinate domination at the initial phase and under the
   nonnegative recurrence.
5. Multiply \(B_gA_g\), compute its characteristic polynomial, and factor its
   two eigenvalues.
6. Prove that \(q_2\) observes the Perron class and is the maximum coordinate
   degree.
7. Check the support graph has a mixed edge and record the exact meaning of
   “non-product.”

Each item belongs in a formal proof ledger. A future author may use a
transparent symbolic algebra tool as a convenience only after a human-readable
derivation exists; no hidden tool output can be cited as evidence.

## Explicitly forbidden actions

- creating `main.tex`, a manuscript, or a build directory;
- running numerical orbit iterations or coefficient randomization;
- searching for examples by brute force and presenting one as a theorem;
- writing source locks, transport bytes, or publication metadata;
- uploading source text to an external API;
- treating a finite sample of \(g\) as evidence for all \(g\ge5\);
- importing a generic tropical/toric theorem without checking its hypotheses.

## Future conditional unlock

A later parent-authorized stage could request a proof-audit script or a small
symbolic sanity check. That stage would require a new permission message,
separate evidence labels, and an explicit decision about whether such a check
is scientific experimentation or merely formal verification. Until then the
experiment count remains zero.
