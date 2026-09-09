# C426 — second actual nonauthor manuscript review

2026-09-09 UTC. Coordinator review, nonauthor of GR5 and of this manuscript.
This pass inspects the actual first-round revision after the complete earlier
manuscript review; it is not that report relabelled or an external review.

## Decision

**PASS. Round-one P1, P2 and P3 are closed. Must-fix findings: 0.
New optional findings: 0. No further manuscript-source correction is needed.**
The coordinator accepts this second-pass disposition. Formal evaluation,
final fresh double build and release verification remain separate gates.

## Actual reviewed inputs

Revised `main.pdf`, `main_round1.pdf` and `builds/round1_revised/main.pdf`
are identical: 10 pages, 343725 bytes, SHA-256
`d0b4e14e8ed42002bf0ad454ee004c817403e9662ae92b25306a94adf4d582db`.
The revised source archive hash is
`816419cad52e4101a2922dde8e7c60626ee391be8da321b0918422daa8768638`.
The complete saved three-hunk diff has hash
`877eab155556f5385f377ccd3258e31494c43007800ffd9d6693bb347279b515`.

The reviewer read the actual diff, the full changed `main.tex`, introduction
and bibliography, the improvement record and the entire 10-page revised PDF
text. All ten revised page images were newly viewed. A fresh `pdftotext`
stream exactly matched the text used for reading, and the current PDF matched
the revised build PDF. All ten active TeX/Bib inputs matched their streamed
members from the revised archive. Comparing all ten with the preserved
baseline found exactly the three recorded changes and seven unchanged
inputs; no theorem, proof or table source changed.

The baseline remains the first reviewed 10-page PDF with hash
`85677da439f31f1c2faea804430c8f395a2aaa235a0d20696e0a97a8ca08ed38`.
The complete first-round report remains at
`manuscript_reviews/round1/C426_REVIEW.md`, hash
`e1be3cd670d5a5cc8536020c0b3352c133a3e4faa91fc0d9bea4b0b5eb07511c`.

## Closure and regression checks

| Check | Actual revised result |
| --- | --- |
| P1, abstract | It says the proof requires no computer-assisted certificate. This accurately permits its displayed hand calculations; Section 7 still records zero mathematical program executions. |
| P2, introduction | The prose now renders “statement for arbitrary class groups”; the spurious hyphen-space is gone. The comparison still concerns projective endomorphisms over a PID versus affine plane maps with indeterminacy, not an unqualified claim that ideal obstructions were unknown. |
| P3, bibliography | GR5 has a single year, rendered `8 September, 2026`; title, working-source path and unpublished AI-assisted status are unchanged. All five entries remain cited and resolved. |
| All-affine quantifier | Theorem 2.2 and Lemma 3.1 still begin with arbitrary affine matrices and independent translations. A primitive row's pure power has a unit coefficient in every residue characteristic. Both reduced indeterminacy directions, not merely lattice preservation, force the primitive matrix into `GL_2(O)`. |
| Wild and quadratic centre cases | `q=f-aY`, particularly `q_1=f_1-a` at degree two, remains explicit. The candidate radius comes from valuation `v(d)-k`; enumeration is over `O/dO`, not just the formal centre `r_0`. All coefficients including the constant term are tested. The dyadic half-centre example still shows why the extra classes matter. |
| Unique disc | Its proof uses the intrinsic bounded-forward-orbit set of the auxiliary polynomial `q`; it does not confuse that iteration with the original Hénon clock or classify periodic points. |
| Global patching | The denominator-clearing CRT includes new prime places introduced by the denominator, not only the original finite bad set. All selected centres remain in the stated ground field. |
| Principal square, not principal ideal | Necessity is `I^2=(det A)`. Sufficiency is the displayed two-generator basis with determinant gamma and the explicitly integral inverse on `I direct-sum I`; this covers nonprincipal two-torsion ideals. The global set remains one left coset with every allowed translation. |
| Complete converse and examples | `Cl(R)[d-1]` contained in `Cl(R)[2]` is derived in both directions, using `f=bY^d+Y` for the converse. Both number-field examples prove the needed ideal identities and nonprincipality without a claimed whole class-group computation. Degree-two/three and all-field limits remain correct. |

The new reading found no altered scope, omitted exceptional branch,
left/right coset error, new dependence on a field extension, or migration
regression. The unchanged public-source assertions were already checked
against primary sources in round one. No repeat search or new full external
paper read is claimed here. The bibliography's one internal source out of
five (20%) is necessary provenance, not a substitute for the displayed proof;
this concentration is flagged without asserting personal self-citation.

## Actual PDF and execution boundary

All ten newly viewed pages are readable, including the ownership table,
multi-page theorem, wild-centre calculation, explicit basis, both ideal
examples and bibliography. No clipping, collision, dropped symbol or broken
proof continuation was observed. All 20 font resources are embedded Type 1
with Unicode maps. The converged revised engine/BibTeX logs have no warning,
undefined reference/citation, over/underfull box or TeX error; a no-match
`rg` exit 1 is a successful diagnostic with no hits, not a failed build.

The author recorded one real revision build with three engine and two
BibTeX passes. This review launched neither a build nor a mathematical
program. It did not rerun old evidence or invent another source revision.
The earlier full mathematical/source reading and this actual revision
regression pass are both internal AI-assisted checks, not human peer review,
formal proof-assistant certification or worldwide-priority certification.

The author/coordinator may now record a no-change second-round PDF alias
and freeze these sources for formal evaluation and final identical-input
builds. This report closes the two manuscript-review rounds only.
