# Nonauthor hand review of the round-nine AS1 spectral probe

2026-09-08 UTC. The coordinator fully read [PROOF_PACKAGE.md](PROOF_PACKAGE.md)
and its frozen scope. This is substantive internal nonauthor review, not
human peer review. The coordinator independently developed the separate
spectral-measure route and discussed the memory-versus-spectrum distinction
with the author; this review is therefore not blind. The exact inequalities
and their proofs were checked from the actual author document.

## Verdict

**PASS for the stated auxiliary inequalities (A), (B), exact memory lemma,
and untwisted nonzero-spectrum claim. No remaining required mathematical
correction in that scope.**

**NOT CLOSED** for nonreal spectral accumulation, uniform nonzero-spectrum
exclusion, or the original AS1 whole-circle continuation question. None
of these is proved by the author or inferred in this review. No admission.

## Checked reasoning

1. Backward decoding uses parity for the last label and exactly three
   lost binary digits for each predecessor comparison. The endpoint
   condition for the last recovered label is
   \(k-3(m-1)\ge1\), valid at \(m=\lceil k/3\rceil\), including
   \(k=1,2,3\). Incoming paths exist in the closed component. Starting
   at its even B-fixed state realizes every linear no-AA block; it does
   not require cyclic admissibility at the block ends.
2. The identities \(P h_0=\tau h_0\), \(P h_j=h_{j-1}\) use the
   normalized transition probabilities. At an even state,
   \(\tau/\varphi+\varphi^{-2}=\tau^2\) with
   \(\tau=-\varphi^{-2}\). Telescoping the phase sum gives exactly
   \(\zeta^m h_{m-1}-\tau h_0\), including \(m=1\).
3. The averaged positive real projection supplies a nonadjacent subset
   with phase-sum modulus at least \(M/\pi\). Subtracting the all-B
   baseline is essential and is done correctly. Thus the norm ratio
   is at least \(m/(4\pi)\), without assuming absence of cancellation.
   Restriction to a closed component intertwines the resolvents and
   admits norm-preserving extensions, so the full-space lower bound
   follows.
4. Untwisted word probabilities telescope, and terminal states become
   constant after m steps. Consequently the range of \(P^m\) is in
   the parity subspace. The quotient is nilpotent; the two nonzero
   eigenvalues are exactly \(1,\tau\), algebraically simple. The
   stationary projection on the parity subspace is norm one and its
   complementary projection has norm at most two. The finite resolvent
   identity then gives the displayed upper bound. It does not assert
   that a long approximate eigenvector gives a nearby true eigenvalue.
5. Modulus transport selects one actual positive-probability path in
   the expansion of \(L^t\). For B^m its probability is at least
   \(\varphi^{-m}\). For B(AB)^ell the first B has probability at
   least \(\varphi^{-1}\), and each AB pair has probability
   \(\varphi^{-2}\), since B from an odd state has probability one.
   Hence the claimed \(\varphi^{-s}\) bound is valid for this word;
   it is not the false claim that every length-s word has that bound.
6. The variance identity holds with complex unit character weights.
   Each selected edge has probability at least \(\varphi^{-2}\).
   The small-defect case makes all relevant eigenvector values at
   least 1/2; eliminating the intermediate value gives the two-cycle
   discrepancy at most 4E. Together with the B loop the generator
   discrepancy is at most 8E, yielding the constant
   \(128\varphi^2(1+K_k)\). The complementary defect case follows
   from the trivial squared-distance bound 4. Zero eigenvalues and
   small conductors are included.
7. The final finite-cycle approximation discussion is used only to
   disprove a fixed-two-cycle uniform frustration test. It does not
   supply near-peripheral eigenvalues. The earlier full peripheral
   theorem and finite-character approximation are explicit accepted
   inputs, not independently reproved here.

## Scope and receipts

The failure of a depth-uniform full-state weighted-supremum resolvent
bound is a genuine theorem about these exact matrices. Its reason can
be entirely nilpotent memory, invisible to positive-power traces.
Trace-level estimates or a depth-growing bound are not ruled out.
This is useful method discrimination, not the missing full AS1 result
and not new general operator theory.

No new outside source or theorem is needed for these elementary
deductions conditional on the accepted round-seven inputs. The author
claims zero new external searches and programs; no such activity is
added by this hand review. No old check, matrix computation, build or
Git mutation was run for this review. Document-integrity checks, if
performed at final handoff, remain separate from this mathematics.
