# Internal hostile-review protocol — P157–P161

**External state:** `HOLD_EXTERNAL`.  Manuscripts, source packages, and
review material must not be transmitted to an external model, author, or
specialist.  Both reviews are internal cold reads by agents independent of
the assigned manuscript's authoring pass.

## Review A — theorem, provenance, and reproducibility attack

For each paper, the reviewer reads the frozen contract, `main.tex`, every
paper-local ledger, references, verifier, frozen transcript, and immutable
Round-0 PDF.  The raw report is retained as `HOSTILE_REVIEW_A.md` and must
contain:

1. a verdict with explicit Critical/Major/Minor counts;
2. a claim-by-claim comparison against the frozen theorem ceiling;
3. fresh derivations attacking all quantifiers, inverse directions,
   exceptional parameters, equality cases, and counting orientations;
4. a provenance attack distinguishing prior ownership, nearby mechanisms,
   standard tools, and bounded non-hits;
5. a collision attack against P1–P156 and the other four new systems;
6. an independently written reviewer verifier, a frozen reviewer transcript,
   and a clear statement that computation is falsification pressure only;
7. source-only rebuild, PDF/metadata/font/visual inspection, anonymity scan,
   and exact repair requests.

Severity has the following fixed meaning:

- **Critical:** false central theorem, direct prior result eliminating the
  residual, irreproducible evidence, or anonymity/integrity failure.
- **Major:** proof gap, claim-ceiling violation, missing decisive boundary,
  materially misleading provenance, or failure to support a paper-sized
  theorem package.
- **Minor:** local clarity, attribution wording, citation metadata, artifact
  provenance, verifier coverage, or noncentral presentation defect.

The author-side pass records every finding and repair in
`IMPROVEMENT_LOG.md`, preserves `main_round0_original.pdf`, and freezes the
post-repair source as `main_round1.pdf`.  A Review-A `PASS` with no findings
still requires an explicit no-change Round-1 freeze.

## Paper-specific mandatory attacks

- **P157 NHI:** the `N=1,2` quotient boundaries, the `v=1` versus `v>=2`
  unit classes, endpoint fibres, temporal CDF, and the distinction between a
  direct prior record and an origination attribution.
- **P158 CIC:** history-word surjectivity, the `r=R,z>0` obstruction, the
  `n=5,t=2` two-edge-plus-isolate sentinel, inclusion–exclusion signs,
  labelled fibres, and the truncated image EGF.
- **P159 OVP:** strict `d>0` transfer versus the fixed diagonal, target-row /
  source-column orientation, `s=0,d=2`, `n=0,1`, `t=0`, and the different
  matrix expressions for even and non-even targets.
- **P160 RCS:** the all-`a,b,t` coordinate iterate, `N=0` and `t=0`, the
  sharp rectangle height, disjoint empty-target slices, the nonempty
  two-boundary bijection, positivity at every weight above threshold, the
  global mass identity, conjugation, three-probe recovery, and direct-owner
  pressure from classical Durfee-square/rectangle decompositions.  The
  retired BST package remains negative owner evidence and is not reviewed as
  a live paper.
- **P161 ORT:** the nondegenerate carrier plus sink, all three oriented-right
  depths, four-window identity, sink fibre, one-step and stable images,
  `p=3` empty recurrent core, and subtraction of the classical orthocentric
  quartet.

## Review B — fresh post-repair falsification

Review B is assigned to a different internal reader cold to Review A's prose.
It begins from the theorem contract and Round-1 package rather than trusting
the first report.  Its `HOSTILE_REVIEW_B.md` must:

- rederive every principal formula independently;
- verify each Review-A repair in source and rendered PDF;
- attack all exceptional parameters and search for small counterexamples;
- rerun the author verifier and, where useful, a reviewer-owned independent
  implementation;
- rebuild twice from source-only copies and inspect every rendered page,
  identifying metadata, fonts, references, and warning logs;
- return explicit severity counts and `ACCEPT_INTERNAL` or `REVISE`.

Every Review-B finding is repaired and documented before Round 2.  Internal
acceptance requires zero unresolved Critical, Major, and Minor findings.

## Final artifact invariant

At closure, `main.pdf` and `main_round2.pdf` are byte-identical.  Round-0,
Round-1, and Round-2 PDFs remain separate historical artifacts.  Each
paper-local `SHA256SUMS` excludes itself, covers every other retained local
file, and passes a cold `sha256sum -c`.  The batch canonical-PDF manifest
covers exactly P157–P161 and passes 5/5.  Acceptance is internal only and
does not authorize novelty or priority claims, posting, circulation, author
contact, specialist contact, or submission.
