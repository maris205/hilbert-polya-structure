# P177 author self-QA

**Decision:** `ROUND2_DUAL_REVIEW_FREEZE / OWNER_AMBER`  
**External state:** `HOLD_EXTERNAL`

## Mathematical closure

- The carrier is the set of all subsets of `E=F_2^d \ {0}`, represented by
  incidence words.  Every addition in the paper is over `F_2`, hence is
  symmetric difference on subsets.
- Only nonzero forms are sampled.  Their kernels contain exactly
  `2^(d-1)-1` points of `E`, so every move flips subset parity.
- Evaluation is injective, `1 notin C` for `d>=2`, and the manuscript gives
  an explicit nonzero-pair construction showing that the masks span all of
  `W`; no dimension count is assumed without proof.
- The class coordinates are unique and a step reaches every opposite-side
  coordinate except the matching one.  This proves the literal crown support,
  not merely a spectral coincidence.
- The history formula includes uniqueness of `L` and the exact support:
  only `L=0` at `t=0`, only `L!=0` at `t=1`, and every `L` from `t=2`.
  There is no missing factor of `q`, `N`, or number of starting states.
- The phase-compatible comparison space has `q` points.  It is distinguished
  from the `2q`-point stationary component, whose ordinary TV remains at
  least one half.  The manuscript never calls the chain ordinarily mixing.
- The spectral proof verifies the rank of the parity–vector-sum map by
  spanning all `(0,u)` and `(1,0)`.  The four multiplicities sum to `2^m`.
- Boolean characters form a full eigenbasis, so the statement “no Jordan
  blocks” is justified rather than inferred from symmetry alone.
- Parameter recovery is explicitly restricted to the promised family; it is
  not a characterization of arbitrary regular bipartite graphs.
- `d=1`, zero-form sampling, complement toggles, and nonbinary variants are
  excluded explicitly.

## Source and ownership closure

- All four cited entries were retrieved from DOI/Crossref metadata and
  checked against publisher or primary preprint surfaces.  Every entry is
  cited, and every citation has one entry.
- The projective-code source has three authors: Kwiatkowski, Pankov, and
  Pasini.  The bibliography does not repeat the earlier shorthand error.
- The canonical DOI for Diaconis–Saloff-Coste is `10.1007/BF01192214`.
- Diaconis–Saloff-Coste is cited only as broad generating-set-walk context,
  not as direct ownership of P177's fixed-generator character calculation.
- Brown's hyperplane-*chamber* walk is treated as a terminology and method
  control, not as the same dynamics.
- Simplex codes, incidence designs, symmetric difference, Cayley/Fourier
  calculus, crown graphs, crown spectra, and generic finite-chain facts all
  receive zero contribution credit.
- P145's Fourier/Cayley proof shell is subtracted.  P172 occupancy erosion,
  P173 quotient leakage, and P175 commutators are recorded as noncolliding
  literal systems, not used as novelty evidence.
- A bounded owner-search miss is never called novelty, priority, or freedom
  to operate.  `OWNER_AMBER / HOLD_EXTERNAL` appears in the abstract, status
  section, and paper-local documentation.

## Artifact closure

- The canonical verifier replay is byte-identical and ends with 1,095,999
  exact assertions, `status=PASS`, and `external_status=HOLD_EXTERNAL`.
- The settled PDF is four A4 pages and has no LaTeX/BibTeX warning, bad box,
  unresolved label/citation, rerun request, or fatal error.
- All 29 font rows are embedded, subsetted, and Unicode mapped.  The PDF is
  unencrypted and contains no form or JavaScript.
- PDF author, title, subject, keywords, creator, and producer metadata are
  blank; the visible author line is `Anonymous`.
- All four rendered pages were inspected.  There is no clipping, collision,
  illegible theorem continuation, malformed bibliography, or stray figure.
- `main_round0_original.pdf` preserves the original author PDF;
  `main_round1.pdf` is byte-identical to the live repaired PDF.
- Source files contain no control byte, TODO, FIXME, placeholder citation,
  email, ORCID, local path, or external-release instruction.
- Review A's support defect and traceability finding are repaired in source;
  both process-separated reviewers report zero open findings.
- `main.pdf` equals `main_round2.pdf`; two source-only cold builds reproduce
  those bytes and 4/4 final pages pass visual inspection.

## Remaining theorem concern

No mathematical defect is known in the frozen contracts.  The live concern
is ownership rather than proof: each ingredient is classical and the
residual conjunction may have an unlocated direct source.  That is why the
gate remains `OWNER_AMBER / HOLD_EXTERNAL`.
