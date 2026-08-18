# Paper Review Round 1 — Raw Referee Record

**Reviewer:** GPT-5.4, model_reasoning_effort=xhigh
**Invocation:** ephemeral, read-only sandbox; complete manuscript source,
bibliography, claims-evidence matrix, frozen proof/source records, and
canonical summary supplied through standard input
**Date:** 2026-08-18

The substantive reviewer agent message below is preserved verbatim.
Startup model-catalog and WebSocket fallback warnings were transport events,
not parts of the review.

---

ROUND
1

VERDICT
Revise. The mathematical core matches the frozen proof package: I found no correctness defect in the all-radix \(S_q\) classification, the binary paired-shell endpoint repair, the trace/determinant domain split, or the least-period support argument. The figure/table program and section organization are coherent at the manuscript level, and the main proofs are self-contained modulo standard cited trace-ideal facts. The remaining blocker is submission readiness: the validation/reproducibility material still exposes internal workflow state.

SCORE
8.8/10

CRITICAL_ISSUES
None.

MAJOR_ISSUES
1. Section 7 and Appendix d are not yet submission-ready because they expose internal pipeline state rather than reader-facing reproducibility evidence. Locations: “hostile-\texttt{PYTHONPATH}”, “Route B”, the table row “Protected-authority replay = \texttt{WAIT\_PROTECTED\_AUTHORITY}”, and the closing sentence “publication/closure state remains \texttt{WAIT\_PROTECTED\_AUTHORITY}”. This does not undercut the theorem, but it is a real readiness defect: it reads like unreconciled internal process metadata, not archival scientific prose. Minimal repair: move raw route/orchestration/status tokens and placeholder seals out of the manuscript into an artifact README or supplement; in the paper keep only the evidence boundary, the exact finite-control counts if desired, and a neutral statement that no external archival attestation is claimed here.

MINOR_ISSUES
1. Source-boundary wording is mostly disciplined, but the introduction phrase “On words of a fixed length this rule gives a finite Kronecker power” briefly blurs the zero-completed-control versus positive-vertex-source distinction. Minimal repair: say “As a zero-completed fixed-length control, this rule gives a finite Kronecker power.”
2. Table-caption notation in Section 3, unique phrase “The last column is \(\sigma_c(2)=\max\{1,\log_b\kappa_{b,2}\}\),” is ambiguous because \(b\) varies and the displayed argument “2” looks like the variable. Minimal repair: rename it to \(\sigma_c(q=2)\) or \(\sigma_{c,2}(b)\).
3. Validation prose is accurate about proof-versus-check separation, but phrases like “owned four audit records” and “did not authorize its invocation” are more process-internal than reader-facing. Minimal repair: recast them as neutral independence statements.

LINE_LEVEL_FIXES
1. Section 1, unique phrase “On words of a fixed length this rule gives a finite Kronecker power.” Replace with “As a zero-completed fixed-length control, this rule gives a finite Kronecker power.”
2. Section 3, table caption unique phrase “The last column is \(\sigma_c(2)=\max\{1,\log_b\kappa_{b,2}\}\).” Replace with “The last column is \(\sigma_c(q=2)=\max\{1,\log_b\kappa_{b,2}\}\).”
3. Section 7, unique phrase “A separate proof auditor, denoted \(P\) in the frozen ledger, owned four audit records...” Replace “owned four audit records” with “independently checked four dependency/domain claims”.
4. Section 7, unique phrase “hostile-\texttt{PYTHONPATH} environments.” Replace with “adversarial import-path environments” or move to supplement.
5. Appendix d table row “Protected-authority replay & \texttt{WAIT\_PROTECTED\_AUTHORITY}”. Delete the placeholder row, or replace it with a prose note outside the table: “No external archival attestation is claimed in this manuscript.”
6. Appendix d, final sentence “publication/closure state remains \texttt{WAIT\_PROTECTED\_AUTHORITY}...” Replace with a reader-facing sentence such as “No external publication-attestation artifact is claimed here.”

NONREGRESSION_AUDIT
1. Exact quantifiers are preserved. The main theorem and abstract consistently state “for every \(b\ge2\), every \(1\le q<\infty\), and \(s\in\C\)”.
2. Phase removal is handled correctly as two-sided unitary equivalence, not conjugation: Section 3 uses \(B_{b,s}=U_tB_{b,\sigma}U_t\) and explicitly warns against inferring positivity or self-adjointness for \(t\ne0\).
3. Shell factorization respects coordinate deletion and the positive-vertex boundary. Section 4 and Appendix b delete zero rows/columns explicitly and never reinsert vertex \(0\) into the infinite source.
4. Active versus hidden walls are distinguished correctly. The paper does not misdescribe \(\log_b\kappa_{b,q}\le1\) as a second active endpoint.
5. The binary exception is handled with the right necessity mechanism. Section 5.4 treats the full bad range \(\kappa_{2,q}2^{-\sigma}\ge1\), including equality, via paired adjacent shells; it does not reuse the \(b\ge3\) same-shell proof.
6. Trace-domain wording is controlled. Operator trace and ordinary determinant are asserted only for \(\sigma>\alpha_b\), while trace powers and \(\det_2\) start at \(\sigma>1\).
7. Finite-compression and absolute-convergence justifications for trace powers are present in the manuscript itself: finite-shell \(S_2\to S_1\) passage plus absolute majorization by \(B_{b,\sigma}\).
8. The \(\det_2\) claim separates “entire in \(z\)” from the local logarithm near \(z=0\) and does not overclaim global log convergence.
9. Positive-vertex zero deletion is maintained in the trace and least-period sections; the binary trace is correctly framed as an operator-trace statement only in the trace-class domain.
10. Least periods are proved from support witnesses, not inferred from possibly cancelling complex traces.
11. Citation ownership and novelty boundaries stay inside the frozen lock: Kummer/Lucas are historical comparators, finite tensor/spectral facts are not claimed as new, and the source search is explicitly bounded.
12. Main proofs remain self-contained modulo standard Simon trace-ideal facts. The appendices enlarge details rather than patch genuine proof gaps.

PRIORITIZED_ACTIONS
1. Strip internal workflow placeholders and route/orchestration jargon from Section 7 and Appendix d, or move that material to a supplement/artifact note.
2. Tighten the one place in the introduction where a fixed-length tensor could be misread as part of the infinite positive-vertex source.
3. Clean the remaining reader-facing notation/prose in the validation and table-caption material.
