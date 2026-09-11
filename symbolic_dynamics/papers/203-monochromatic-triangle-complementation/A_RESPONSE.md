# P203 author response to formal Review A finding A-M1

2026-09-05 UTC. **AUTHOR_REPAIR_SUPPLIED / REVIEWER_ACCEPTANCE_PENDING /
HOLD_EXTERNAL**. No Round1 is created or accepted by this response.

## Finding and exact change

Review A identified Minor A-M1: the original main.tex/PDF did not visibly
display the project external-release hold, although the companions did.
The only manuscript edit adds the following paragraph immediately before
the bibliography, after the existing limitations paragraph:

```latex
\paragraph{Scope and release status.}
\texttt{HOLD\_EXTERNAL}. The ownership comparison is bounded to the
inspected literature and internal history. No global novelty or priority
claim is made, and external release is not authorized.
```

The actual unified diff against frozen_round0/main.tex has exactly that
one addition and no removals (tool receipt7e0849). All definitions,
theorem statements, proofs, witnesses, equations, table entries and cited
keys are unchanged. references.bib, verify_p203.py and CANONICAL.txt were
byte-compared with their frozen Round0 originals and are unchanged
(receipt e55270). No verifier run is invented for this text-only repair.

## Exact old/new identities

| Artifact | Round0 | Proposed A revision |
|---|---|---|
| main.tex | a08983002caf08109c6a6406183149343aaa5ecd9a6d08af7f521f8ca85480b0 | 70c22a62adc3b6218278a6fd91b08dfa8d02efddf03ba7cc115bd35a3ab6de54 |
| main.pdf | 617cea5d4f8b50a9946d05bafc2cfbf6fb01bbe45dab754813b07f4f12cc1167 | 0738965406c046662618ec999474738c064c363fa66ba587e7b33a377f89b47d |
| references.bib | 2a7c888ff6158f11e00a45f6231f628e575515d1f1c0713f93f90592ea88f78a | unchanged |
| verify_p203.py | 77e7be9b6dc57a156010c6543ff41415415f833119e5a7116ffcef53cc5e1d7d | unchanged |
| canonical stdout | 6a672bcfa97f09c1575aa89bb4e2ca52aa8284315706ec90abbd6d35995dbf00 | unchanged |

The proposed source/bibliography/PDF are physically supplied in revision_a/.
Live main.tex and main.pdf byte-match that revision. Its21 nonself files
include the new cold build and page renders, covered by revision_a/SHA256SUMS
with digest
`83c9b2650cdaa2324206c1d7d748c75fac119918cb91814a07557edfcb82ce1a`.
This is a versioned author repair, not frozen_round1 or a reviewer verdict.

## Actual new build and all-page visual QA

The unchanged executable BUILD.sh copied only revised main.tex and unchanged
references.bib into the previously nonexistent revision_a/cold_build,
then ran the deterministic pdflatex/BibTeX/pdflatex/pdflatex chain.
Launch receipt0e0772/session48806, completion01b831/exit0. No original
build cache was copied. The new PDF has4 pages,309,156 bytes and22 embedded
font entries. The extra embedded monospaced font renders the hold marker.
No warning, error, undefined-reference/citation or bad-box match occurs in
the final build log (receipt215464, expected rg exit1 for no matches).

All4 revised pages were rendered at120dpi and actually viewed. Pages1–3
retain the same legible setup, complete proofs and certificate layout.
Page4 retains the equality proof, data table, limitations and bibliography;
the new HOLD_EXTERNAL paragraph is visibly readable above the references,
with no clipping or overflow. PDF text extraction independently finds the
literal HOLD_EXTERNAL marker and the complete scope statement
(receipt c29351). This is author-side build/visual QA, not Review A acceptance.

## Preservation and pending judgement

The full36-file frozen_round0 manifest still passes (receipt d6f401).
ROUND0_RECEIPT.md remains
`89b46ad4e130dbe78ca818e2dbffc94d6991e5b76590d31dd9f7683ad25bd265`;
main_round0_original.pdf is still the original PDF. The original full
author-tree manifest is physically preserved as
revision_a/ORIGINAL_AUTHOR_TREE.sha256, digest
`d186ac63932a9332e0da75ab849cc6a5f065f39ea359d56f50e6923f0c348615`.
It is an old-version record, not a promise that revised live paths match
the old version. The top current manifest is refreshed for the new files.

The untouched Round0 companion identity/build statements remain records
of Round0. This response identifies the current live repair while reviewer
acceptance is pending; it does not retroactively revise the old receipt.

The historical Stage1 missing-intermediate-probe Minor1 remains unrepaired
and distinct from paper finding A-M1. Adding the hold paragraph does not
recover those missing bytes, repair the old failed pin, or change the
mathematics. Root must accept this proposed delta and finish its actual
formal review before any Round1 freeze. No central edit, Git mutation,
external notification or release is performed here.
