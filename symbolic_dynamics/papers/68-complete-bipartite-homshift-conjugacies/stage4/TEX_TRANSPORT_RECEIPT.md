# TeX transport receipt — Round 1

status: complete

paper: `68-complete-bipartite-homshift-conjugacies`

mirror_root:
`/root/autodl-tmp/hilbert-polya-structure/symbolic_dynamics/papers/68-complete-bipartite-homshift-conjugacies`

## Patch-to-source mapping

| Roadmap item | Markdown operation and actual revised block | TeX transport | Auxiliary code/control transport | Verification |
|---|---|---|---|---|
| `REV-P68-EIC-W1` | `replace_block B0005`; content remains in actual block `B0005` | `sections/1_introduction.tex`: explicit hierarchy before the four-contract list | none | Revised Markdown block `B0005` and the TeX paragraph both identify the product conjugacy/dimer code as central, the phase lemma as mechanism, and the remaining packages as complementary. |
| `REV-P68-R3-W1` | `insert_after B0041`; apply assigned the inserted paragraph fresh block `B0061` | `sections/5_pressure.tex`: statistical-mechanics dictionary after the one-site activity definitions | none | Actual block `B0061` and the TeX paragraph identify the spin system, sector variable, activities, equal mixture, conditional independence, and non-complete-target boundary. |
| `REV-P68-R1-W1` | `replace_block B0057`; content remains in actual block `B0057` | `sections/7_scope.tex`: control description now includes `(1,6)` to `(2,3)` and `(1,1)` | `code/verify_complete_bipartite.py`; `code/verify_complete_bipartite.out`; `CONTROL_RESULTS.md`; Stage 4 control receipts | The control exits 0 and records 72 singleton-boundary torus points, two minimal torus points, and expanded finite-shape cases. |

No operation was transported for `REV-P68-R2-W1`; its
`change_block_ids` is empty. Existing specialist-audit and external-release
HOLD block `B0056` was not changed.

## Markdown patch and LaTeX transport relationship

`REVISION_PATCH.json` is the authorized patch against the frozen anchored
Markdown review draft. Its deterministic application produced
`REVISED_DRAFT.md` and the apply report; it did not write the LaTeX source.
The LaTeX edits are an explicit semantic transport of the three authorized
operations into the paper's compilable source tree. This receipt binds each
applied Markdown block—including fresh inserted block `B0061`—to its TeX and,
where applicable, executable-control counterpart. The Markdown and TeX
representations are not claimed to be byte-identical because they use
different citation and display syntaxes.

## Git-mirror source-surface verification

A SHA-256 comparison against the Git mirror covered `main.tex`,
`references.bib`, every `sections/*.tex` file, every regular `code/*` file,
and `CONTROL_RESULTS.md`.

The only differing source/control files are exactly:

- `sections/1_introduction.tex`
- `sections/5_pressure.tex`
- `sections/7_scope.tex`
- `code/verify_complete_bipartite.py`
- `code/verify_complete_bipartite.out`
- `CONTROL_RESULTS.md`

The unchanged compared files are:

- `main.tex`
- `references.bib`
- `sections/0_abstract.tex`
- `sections/2_phase_counts.tex`
- `sections/3_conjugacy.tex`
- `sections/4_finite_dependence.tex`
- `sections/6_periodic_data.tex`
- `sections/8_conclusion.tex`

Generated `main.aux`, `main.log`, and `main.pdf` differ from the mirror as
expected after compilation; they are build outputs, not additional source
changes.

## Integrity and citation receipt

- `main.tex` is mirror-identical at SHA-256
  `60cca40aa4a91db684e0d628fa4799bf1ce4f98af806e4bcfbc09d6a32dddc83`.
- `references.bib` is mirror-identical at SHA-256
  `7c7658dee3452d9fd8616fc849c2073034113492b921d716dc218171de89df43`.
- New references added: `0`.
- The frozen Stage 3 anchored draft remains SHA-256
  `232b1b6b51d15a7a87d62266fe69ad5ba4a2cad09ed0ba154812b87126f1b412`.
- The frozen Stage 3 block manifest remains SHA-256
  `8ac140bcbbf0928c14208363feb2053709cd93f83ab43cb91f1f15deb5bab7b3`.
- The frozen Stage 3 revision roadmap remains SHA-256
  `9cc387fa9cca1178d83fc61358eee6a36fc22aeecdb884139f52c8ac34680eb2`.
- No Stage 3 frozen artifact was written during transport.
