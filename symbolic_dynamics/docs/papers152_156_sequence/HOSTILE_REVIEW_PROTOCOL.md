# Internal hostile-review protocol — P152--P156

**External state:** `HOLD_EXTERNAL`.  Manuscripts must not be transmitted to
an external or cross-model service.  The two reviews are independent internal
cold reads by agents that did not author the assigned paper.

## Review A — theorem, owner, and reproducibility attack

For each paper, the reviewer must read the frozen contract, `main.tex`, all
paper-local ledgers, references, verifier, frozen transcript, and round-0 PDF.
The raw report goes in `HOSTILE_REVIEW_A.md` and must contain:

1. a verdict and explicit Critical/Major/Minor counts;
2. a claim-by-claim theorem-ceiling comparison;
3. proof attacks at every quantifier, division, boundary, equality case, and
   inverse “if and only if” direction;
4. an owner attack separating direct ownership, nearby ownership, standard
   tools, and bounded non-hits;
5. a portfolio-collision attack against P1--P151 and the other four new notes;
6. an independent verifier/transcript replay and a statement of what the
   computation does **not** prove;
7. a source/PDF build check, anonymity scan, and list of precise repairs.

Severity means:

- **Critical:** false central theorem, direct owner collapsing the residual,
  irreproducible evidence, or anonymity/integrity failure.
- **Major:** proof gap, exceeded claim ceiling, missing decisive boundary,
  materially misleading ownership, or paper-value failure.
- **Minor:** local clarity, citation metadata, artifact provenance, or
  noncentral presentation defect.

The author must record every disposition and concrete edit in
`IMPROVEMENT_LOG.md`, preserve the pre-repair PDF as
`main_round0_original.pdf`, and compile `main_round1.pdf`.

## Review B — fresh post-repair falsification

Review B must be performed by a different internal reader or, at minimum, a
reader cold to Review A's prose.  It starts from the frozen contract and the
round-1 package rather than trusting the first report.  The raw report goes in
`HOSTILE_REVIEW_B.md` and must:

- re-derive the main formulas independently;
- check that every Review-A item was fixed in source, not merely marked fixed;
- attack all exceptional parameters and counterexamples again;
- replay the verifier in a fresh process and rebuild from a source-only copy;
- inspect every rendered page and PDF metadata;
- return explicit severity counts and a final `ACCEPT_INTERNAL` or `REVISE`.

Any finding is implemented and documented before `main_round2.pdf` is frozen.
Internal acceptance requires zero unresolved Critical, Major, **and Minor**
items.

## Final artifact invariant

At closure, `main.pdf` and `main_round2.pdf` must be byte-identical.  Round-0,
round-1, and round-2 PDFs remain distinct historical artifacts and become
read-only.  `SHA256SUMS` excludes itself, lists every other paper-local file,
and passes a cold `sha256sum -c`.  Acceptance is internal only and never
authorizes novelty, priority, posting, circulation, specialist contact, or
submission.

