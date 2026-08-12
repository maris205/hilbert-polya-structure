# Paper 7 Round-2 Independent Review

## Mechanism

The configured external GPT review endpoint was unavailable, so no external
model score is reported.  Three independent read-only subagent audits were
used instead:

1. mathematical proof and operator-theory audit;
2. numerical, figure-source, and citation audit;
3. scope, provenance, and cross-document claim-drift audit.

## Findings before remediation

| Audit | Critical | Major | Minor | Main issue types |
|---|---:|---:|---:|---|
| Scope and provenance | 0 | 6 | 4 | post-hoc protocol language, R/C versus P/Z classification, zero-exposed parameter lineage, quantum \(+1\) drift in a support document |
| Mathematics | 0 | 0 | 9 | closability detail, parameter/measurability qualifiers, first-exit intermediate step, SSF normalization, propagator-trace terminology |
| Numerics and citations | 0 | 4 | 3 | stale R102 aggregates, hard-coded figure annotations, archive-field wording, unpublished-source locator |

A first numerical regression then exposed one additional major issue: the
historical R100--R104 summary JSON level-change aggregates did not use the
same 25/15 edge discard stated for the 140-level spacing window.

## Remediation

- The main theorem now states only the two growing quantum terms; the \(+1\)
  is retained only in the exact classical comparator.
- The quadratic form is explicitly proved closable, and the first-exit,
  fixed-parameter, measurable-vector-potential, SSF, and
  spectral-propagator details are written out.
- The authoritative taxonomy is Q/W/S/P/Z with R and C as side diagnostics:
  Q/W are proved, S is sampled, R is finite-window, C is admissible, P is
  open, and Z is untested and unauthorized before P.
- The \(a=1.02\) lineage is disclosed as RH-motivated and zero-exposed;
  present operator definitions and runs are zero-input, not statistically
  blinded in parameter provenance.
- Figure scripts now read frozen JSON/NPZ data, shared window code, and
  stored GOE/GUE references.  A unit test explicitly checks 140 levels and
  138 adjacent ratios.
- Raw NPZ spectra and historical summaries were preserved.  The version-2
  `QUANTUM_WINDOW_AUDIT.json` recomputes R100, R101, R102, and R104 on
  modes 25--164; `QUANTUM_WINDOW_CORRECTION.md` records the correction.
  No gate decision changed.
- The unpublished prior manuscript is identified by version, page count,
  affiliation, and SHA-256.  No public URL or DOI was invented.

## Regression outcome

All three independent auditors reported no residual issue after remediation.
The final local regression produced:

- 13/13 tests passing;
- all seven figures regenerated from archived results;
- version-2 window audit covering 5 R100, 5 R101, 2 R102, and 4 R104 cells;
- 35-page PDF with no undefined citation/reference and no overfull box;
- 59 distinct references printed from 69 audited database entries.

## Remaining external or research actions

These are not defects silently closed by the manuscript:

1. deposit the supplied unpublished prior manuscript in a public persistent
   repository before submission;
2. add a genuinely different magnetic finite-element or Galerkin
   discretization and several higher spectral windows;
3. expand the classical phase-space census;
4. execute R200 only after implementation review;
5. keep P open and Z unauthorized until an endogenous prime-power mechanism
   is derived.
