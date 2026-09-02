# Internal hostile-review protocol — P162–P166

**External state:** `HOLD_EXTERNAL`.  Manuscripts, source packages, and
review material must not be transmitted to an external model, author, or
specialist.  Both paper reviews are process-separated internal cold reads;
candidate gates do not replace either manuscript review.

## Review A — theorem, provenance, and reproducibility attack

For each paper, the reviewer reads the frozen contract, source, local
ledgers, references, verifier, transcript, and immutable Round-0 PDF.  The
retained `HOSTILE_REVIEW_A.md` must include:

1. an explicit verdict and Critical/Major/Minor counts;
2. a claim-by-claim comparison with the frozen theorem ceiling;
3. fresh derivations attacking quantifiers, inverse directions, exceptional
   parameters, equality cases, and counting orientations;
4. owner and internal-collision audits that distinguish classical inputs
   from the residual conjunction;
5. a reviewer-owned exact verifier and frozen transcript, with computation
   labelled as falsification evidence rather than proof;
6. source-only builds plus PDF, metadata, fonts, references, anonymity,
   visible-hold, and all-page visual checks; and
7. exact repair requests for every finding.

Severity is fixed as follows:

- **Critical:** false central theorem, direct owner eliminating the residual,
  irreproducible evidence, or anonymity/integrity failure.
- **Major:** proof gap, claim-ceiling violation, missing decisive boundary,
  materially misleading provenance, or paper-scale failure after
  subtraction.
- **Minor:** local clarity, attribution, citation metadata, verifier
  coverage, artifact provenance, or noncentral presentation defect.

Every finding is mapped to a source/document repair in
`IMPROVEMENT_LOG.md`.  `main_round0_original.pdf` is immutable.  The revised
or explicitly unchanged artifact is frozen as `main_round1.pdf`.

## Paper-specific mandatory attacks

- **P162 / RTI:** history-span sufficiency; the full-rank sharp witness;
  Gaussian history orientation; target stabilizer containment; the saturated
  `r=s` and odd-target boundaries; source-size polynomial mass; and recovery
  of stabilizer dimension.
- **P163 / CSD:** even/odd atomic kernels; silent atom; central-rank parity;
  the singleton iff in the deepest shell; support-resolved product factors;
  the `n=2` exception; stable image and cover-inclusion–exclusion fibres.
- **P164 / CEF:** nonlinear change-mask multiplicity; dyadic powers of
  `I+S`; last-shell positivity; all-one endpoint; `t=0,1,n+1` conventions;
  affine-fibre signs; midpoint/time-two parameter multiplicities; and
  collisions between equal numerical fibre values.
- **P165 / SDS:** strict descent; minimum-distance doubling; zero-code and
  `n=0,t=0` boundaries; direct sums used for sharpness; necessity and
  sufficiency of both image inequalities; equality in both source lower
  bounds; and the explicit distinction between the extremal slice and a full
  fibre.
- **P166 / HWT:** sign/orientation in the diagonal phase conjugacy; composite
  moduli; cycle mass exhaustion and exact-period rather than dividing-period
  counts; the no-wrap step in every depth shell; sharp-tail equality
  structure; all-zero/no-zero branches in target fibres; marked EGF and
  maximum-fibre witness; the `n=2` Meyer–Pommersheim subtraction; siteswap
  ownership of the recurrent slice; and the supporting-only scope of the
  all-time phase oracle.

## Review B — fresh post-repair falsification

Review B is assigned to a different internal reader cold to Review A's
prose.  It starts from the Round-1 package and independently:

- rederives every principal formula and checks every Review-A repair;
- attacks exceptional parameters and searches for counterexamples;
- replays the author verifier and runs a separate implementation where
  useful;
- performs two source-only builds and inspects every rendered page, log,
  reference, font row, metadata field, anonymity token, and lifecycle token;
  and
- returns explicit severity counts and `ACCEPT_INTERNAL` or `REVISE`.

All Review-B findings must be closed before Round 2.  Internal acceptance
requires zero unresolved Critical, Major, and Minor findings.

## Final artifact invariant

At closure, `main.pdf` and `main_round2.pdf` are byte-identical.  Round-0,
Round-1, and Round-2 PDFs remain preserved.  Each paper-local `SHA256SUMS`
excludes itself and covers every other retained local file.  The batch
canonical-PDF manifest covers exactly P162–P166 and passes 5/5.  Internal
acceptance never authorizes public release, priority language, circulation,
contact, or submission.
