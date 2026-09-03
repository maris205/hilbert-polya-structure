# P175 final Round-2 self-QA

**Disposition:** Review-B owner reframe implemented and accepted;
`HOLD_EXTERNAL`.  
**Hostile review:** both reviews present; no open finding.

## Scientific claim audit

- [x] The literal carrier (M_n(\mathbb F_q)), fixed standard basis, diagonal
  extraction, and update (\Phi(A)=[\Delta(A),A]) are stated before any
  theorem.
- [x] The entry formula is derived with the commutator sign convention
  (\Delta A-A\Delta).
- [x] (\Phi^2=0) is proved from the vanishing diagonal of the first image,
  rather than inferred only from computation.
- [x] The reachability criterion includes both necessary conditions: zero
  target diagonal and (q)-colourability of the undirected support.
- [x] The support graph uses an edge when either directed target entry is
  nonzero; this matches both scalar equations.
- [x] The every-target fibre counts ordered off-diagonal variables and uses
  (m(c)=\sum_\alpha n_\alpha(n_\alpha-1)), not the unordered equal-pair
  count.
- [x] The occupation-marked coefficient statement preserves field-element
  labels; it is stronger than an unlabelled partition count.
- [x] The image formula uses (q^2-1) choices per undirected support edge,
  because the ordered pair of directed entries may be anything except
  ((0,0)).
- [x] The zero-fibre composition formula includes the multinomial factor and
  all weak (q)-part compositions of (n).
- [x] The unique-maximum proof treats unreachable targets and uses strict
  exclusion of positive colouring summands for every nonzero reachable
  target.
- [x] The complete tree distinguishes root, depth-one leaves, depth-one
  branch vertices, and depth-two leaves; all counts sum to (q^{n^2}).
- [x] The boundary (n=1) has height one and no depth-two states; (n\ge2)
  has an explicit nonzero-image witness and height two.
- [x] All-time fibres, the image tower, fixed points, recurrent points, and
  the zeta function follow from the literal two-step collapse.

## Exact-verification audit

- [x] The verifier is independent and standard-library only.
- [x] Every literal arrow, output diagonal, and second iterate is checked.
- [x] Every codomain target is checked, including targets outside the image.
- [x] Aggregate fibre and labelled occupation-refined fibre are checked
  independently.
- [x] Image membership and support-only dependence are checked per target.
- [x] Image size is checked by an independent simple-graph support census.
- [x] Kernel weak-composition formula, unique maximum, depth layers, fixed
  points, second image, and depth-two mass are checked.
- [x] Eleven boxes include (q=2,3,4,5), (n\le4), and the nonprime field
  (\mathbb F_4=\mathbb F_2[x]/(x^2+x+1)).
- [x] Two fresh runs are byte-identical: 2,111,465 assertions, deterministic
  edge digest, and `RESULT=PASS`.
- [x] The manuscript labels computation as falsification evidence, not proof.

## Ownership and citation audit

- [x] Young and Kadyrsizova–Yerlanov delimit arbitrary-pair additive matrix
  commutator work.
- [x] Baddeley and Larsen–Lu delimit ordinary commutator-map image/fibre work.
- [x] Bier is credited for the fixed-regular triangular Engel mechanism
  underlying P119; P119's fixed-element update, centralizer-coset fibres, and
  filtration tree receive zero contribution credit.
- [x] Sokal's spin formula is used to display the exact complete-graph Potts
  specialization rather than only a “Potts-type” analogy; the identity is
  zero credit.
- [x] Stanley is credited for the proper-colouring occupation enumerator;
  the marked `X` exponent is explicitly a deterministic coefficientwise
  transform and zero credit.
- [x] Artin–Mazur is credited for zeta bookkeeping.
- [x] All eight bibliography entries have verified DOI or primary manuscript
  records, all eight are cited, and there are no uncited padding references.
- [x] The source ledger says explicitly that a bounded search miss does not
  prove novelty or priority.

## Manuscript and visual audit

- [x] Anonymous `amsart`, A4, 10pt, 24 mm margins.
- [x] Abstract states literal map, temporal result, inverse result, and owner
  boundary without citations.
- [x] Main theorem/proof order is definition → fibre → counts → complete graph
  → controls/limits.
- [x] Figure is documented as N/A in `PAPER_PLAN.md` and `README.md`; the
  branching formula carries all structural information.
- [x] Final Round-2 PDF is 4 pages with no build warnings or bad boxes.
- [x] All fonts are embedded and the full text extracts correctly.
- [x] All four final Round-2 pages passed the batch closeout visual audit.
- [x] PDF metadata fields that could leak authorship or tool identity are
  empty; visible author is only “Anonymous.”
- [x] `main.pdf` and `main_round2.pdf` are byte-identical; Round 0 and Round 1
  remain preserved.
- [x] Two final source-only cold builds reproduce `main.pdf` byte for byte;
      all retained settled/BibTeX logs are clean.

## Lifecycle guard

- [x] Both hostile-review files are present; Review A found no issue and
  Review B's one owner-reframe finding is implemented and delta-accepted.
- [x] No release, upload, submission, or external-message action was taken.
- [x] The manuscript, ledgers, transcript, and README all retain
  `HOLD_EXTERNAL`.
