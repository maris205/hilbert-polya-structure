# Final internal QA — P151

**Verdict:** **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**  
**Surviving severity:** 0 Critical / 0 Major / 0 Minor

This is the consolidated internal QA record, not external clearance.

## Review closure

- Hostile Review A: REVISE, 0 Critical / 1 Major / 3 Minor.
- Sericola's generic time/place law and moments, Chen's tree-PGF algorithm,
  the de la Iglesia--Juarez journal VoR, exact-versus-independent wording,
  and the `Q(0)/Q(1)/D(1)` bridge were repaired.
- Independent Hostile Review B: ACCEPT, 0 / 0 / 0; every Review-A item CLOSED.

## Mathematical checks

- **Model:** the theorem consistently assumes a labelled finite spider,
  positive integer edge lengths, unweighted simple random walk, centre start,
  and absorbing leaves.
- **Killed-arm transform:** both boundary-value solutions satisfy
  \(u_k=(z/2)(u_{k-1}+u_{k+1})\), and the later-added centre step accounts for
  the powers \(z^{\ell_i}\) and \(z^2\).
- **Renewal:** the failed-attempt transform returns exactly to the centre, so
  the strong Markov restart and geometric series are legitimate.
- **Moments:** the second-moment equation keeps the dependence between attempt
  duration and failure through \(\rho=\mathbb E[A(1-B)]\); no false
  independence assumption is made.
- **Extrema:** both integer transfers are strict away from their stated
  terminal profiles, proving the equality classes as well as the bounds.
- **Inverse:** endpoint ratios recover only a primitive rational ray; common
  dilation is explicitly unidentifiable until the mean is added.  The claim
  excludes arbitrary noisy data, unknown topology, and unknown kernels.
- **Ceiling:** the statement matches the frozen P151 contract and does not
  claim generic gambler's ruin, continuants, spectral theory, generic
  time/place or tree-PGF machinery, endpoint/mean novelty, equal-arm laws, or
  general tomography.

## Exact-control checks

- Cold replay matches `verification_output.txt` byte for byte.
- All 1,446,432 assertions use only Python integers and `Fraction`.
- Literal state recursion is compared with a separately assembled rational
  transform; moment, extrema, inverse, and equal-arm controls use additional
  routes.
- The finite ranges are stated in both the manuscript and control record and
  are never substituted for the proofs.

## Source and writing checks

- All seven bibliography entries are verified primary/publisher records and
  all are cited in the ownership subtraction.
- Each direct or nearest owner is assigned explicit zero-credit material.
- The bounded non-hit is described only as a non-hit, never as a novelty or
  priority conclusion.
- The paper is anonymous and includes Data Availability, Ethics, Author
  Contributions, Conflict of Interest, Funding, Limitations, and the explicit
  `HOLD_EXTERNAL` statement.

## Build and visual checks

- The theorem's endpoint/mean display was inspected after restoring the
  missing backslash in `\qquad`.
- The killed-path proof was split into displays, eliminating the only
  overfull box from round 0.
- Citations and cross-references resolve; fonts are embedded; identifying PDF
  title/author/subject/keyword metadata are blank.
- Page rasterization confirms that the title, ownership table, theorem
  display, audit table, declarations, and bibliography remain inside the
  page bounds.

- The accepted current `main.pdf` and `main_round1.pdf` are byte-identical,
  6 A4 pages, 356,664 bytes, at SHA-256
  `24fddbfb896510cf2712a8ade2a3ac37d04712676f635e39f1170c4cc334e8d9`.
- Review B produced two isolated clean builds mutually and package
  byte-identical at that hash and inspected every current page at original
  detail without defect.

## Freeze boundary

`main_round2.pdf` is frozen read-only and byte-identical to the accepted
current PDF.  The final paper-local `SHA256SUMS` was regenerated after closure
and passes in full.  Nothing here authorizes public posting, circulation,
submission, author contact, or any other external action; status remains
`HOLD_EXTERNAL`.
