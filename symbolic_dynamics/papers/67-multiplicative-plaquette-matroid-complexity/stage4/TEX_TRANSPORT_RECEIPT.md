# TeX transport receipt — Round 1

status: complete

paper: `67-multiplicative-plaquette-matroid-complexity`

mirror_root:
`/root/autodl-tmp/hilbert-polya-structure/symbolic_dynamics/papers/67-multiplicative-plaquette-matroid-complexity`

## Patch-to-source mapping

| Roadmap item | Markdown operation and actual revised block | TeX transport | Auxiliary code/control transport | Verification |
|---|---|---|---|---|
| `REV-P67-EIC-W1` | `replace_block B0005`; content remains in actual block `B0005` | `sections/1_introduction.tex`: definition of normalized-Haar total correlation immediately before the main theorem | none | Revised Markdown block `B0005` and the TeX paragraph display the same entropy-deficit definition before first theorem use. |
| `REV-P67-R1-W1` | `replace_block B0092`; content remains in actual block `B0092` | `sections/6_scope.tex`: deterministic-control paragraph now records exact nonprime `F_4` coverage and retains the regression-evidence limitation | `code/verify_plaquette_matroid.py`; `code/verify_plaquette_matroid.out`; `CONTROL_RESULTS.md`; Stage 4 control receipts | The control exits 0 and records 80 prefix ranks, 4096 projections, 36 rectangles, and three Haar enumerations over `F_4`. |

No operation was transported for `REV-P67-R2-W1` or `REV-P67-R3-W1`.
Their `change_block_ids` are empty. Existing HOLD/ownership blocks `B0089`
and `B0098`, and the optional-application location `B0086`, were not changed.

## Markdown patch and LaTeX transport relationship

`REVISION_PATCH.json` is the authorized patch against the frozen anchored
Markdown review draft. Its deterministic application produced
`REVISED_DRAFT.md` and the apply report; it did not write the LaTeX source.
The LaTeX edits are an explicit semantic transport of those two authorized
operations into the paper's compilable source tree. This receipt binds each
applied Markdown block to its TeX and, where applicable, executable-control
counterpart. The Markdown and TeX representations are not claimed to be
byte-identical because they use different citation and display syntaxes.

## Git-mirror source-surface verification

A SHA-256 comparison against the Git mirror covered `main.tex`,
`references.bib`, every `sections/*.tex` file, every regular `code/*` file,
and `CONTROL_RESULTS.md`.

The only differing source/control files are exactly:

- `sections/1_introduction.tex`
- `sections/6_scope.tex`
- `code/verify_plaquette_matroid.py`
- `code/verify_plaquette_matroid.out`
- `CONTROL_RESULTS.md`

The unchanged compared files are:

- `main.tex`
- `references.bib`
- `sections/0_abstract.tex`
- `sections/2_coordinates.tex`
- `sections/3_finite_projections.tex`
- `sections/4_prefixes.tex`
- `sections/5_rectangles.tex`
- `sections/7_conclusion.tex`

Generated `main.aux`, `main.log`, and `main.pdf` differ from the mirror as
expected after compilation; they are build outputs, not additional source
changes.

## Integrity and citation receipt

- `main.tex` is mirror-identical at SHA-256
  `940ceda23385c37a2c3f362640c8cd362807685b848329bbf4897b8f2b4984ae`.
- `references.bib` is mirror-identical at SHA-256
  `ff523453c6f1ddb518319d6d15c815071e449fd85f97f7115b3fdd24eda23628`.
- New references added: `0`.
- The frozen Stage 3 anchored draft remains SHA-256
  `9acf34f77b9a4c65ee7523322ee75388d6e241296675439b07f796a2be086ef8`.
- The frozen Stage 3 block manifest remains SHA-256
  `00c0888fbc5d7478147c2b41b0effecf6bb0b0b22a095ee441f45e14d5d541cf`.
- The frozen Stage 3 revision roadmap remains SHA-256
  `43d96486dbfd781d2c82d040e964f2d24c2a280339d68f581365922344e1edcd`.
- No Stage 3 frozen artifact was written during transport.
