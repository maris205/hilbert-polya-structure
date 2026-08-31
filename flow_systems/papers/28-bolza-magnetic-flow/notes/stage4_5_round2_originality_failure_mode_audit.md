# Paper 28 — Stage 4.5 Round 2 originality and failure-mode audit

Audit mode/date: **ARS Integrity Mode 2, 2026-08-31**.

Fresh dual-lane coverage is **44/77 body paragraphs (57.1%)**. Every successful paragraph has both an 8–12-word quoted exact search and an unquoted supplementary/paraphrase search, with HTTP state and auditable top-result title/URL/snippet summaries. All ten major body sections are represented. All five Stage-4/4′ new or materially changed paragraphs are successful (**5/5, 100%**).

No returned top-result summary contained an unattributed exact match requiring action. One sampled generic passage was graded common knowledge; the remaining recorded checks found no exact match in their reviewed top results. Search access failures would be excluded from the numerator and could never be graded ORIGINAL; this run recorded none among the counted samples.

The same-author check covered Liang Wang's 2026 Taylor & Francis/Zenodo prime-distribution work and the Research Square/Zenodo Spectral Isomorphism work using author/email/institution/ORCID linkage. Full held-text 8-, 10-, and 12-token shingle comparisons found zero shared windows, and all five changed P28 passages received the dual-lane search. The conclusion is limited to that searchable subset.

No licensed professional similarity detector was available, so this is not a global plagiarism or self-plagiarism certificate.

All seven ARS failure modes were reviewed under the exact taxonomy: implementation bug passing AI self-review; hallucinated citation; hallucinated experimental result; shortcut reliance; implementation bug reframed as novel insight; methodology fabrication; frame-lock at early pipeline stage. Each is CLEAR on the recorded surface; the implementation-bug, experimental-result, bug-reframing, and methodology-fabrication classes are supported by actual logs/configuration/tests/provenance/receipts and would block if non-CLEAR.
