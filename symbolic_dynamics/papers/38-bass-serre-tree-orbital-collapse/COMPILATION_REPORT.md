# Paper 38 compilation report — SD-C40

Date: 2026-08-16 (UTC)
Manuscript: `main.tex`
Output: `main.pdf`
Writer-layer verdict: **PASS**

The repository root still owns the future Stage-2 manifest, metadata-only
seal, root registration, Git operations, and mirror synchronization.  This
report certifies the complete pre-artifact writer layer only.

## Clean build

`latexmk` is not installed in the environment.  The final build started with
no LaTeX auxiliaries or prior PDF in the authority directory and used:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final log and BibTeX log contain zero errors, LaTeX/package/BibTeX
warnings, unresolved citations or references, rerun requests, and overfull or
underfull boxes.

## Final PDF audit

- PDF: 17 pages, A4 (`595.276 x 841.89 pt`), PDF 1.5, 517,244 bytes.
- PDF SHA-256:
  `61e731540f3546c0d2b728edfe124f5885d4a424cbf542d970ed02985a3117e9`.
- `main.tex` SHA-256:
  `c8437cffa2dc9ec34900f1efb8db0ebd3fc778064c04e7e09686e62015f035ea`.
- Bibliography parity: 11 unique cited keys, 11 compiled keys, and 11 database
  entries, with empty set differences.  Every entry carries a DOI or an
  official journal URL.
- Fonts: 28/28 rows are Type 1, embedded, subset, and Unicode-mapped.
- Raster images: 0.  All three figures are vector TikZ.
- Modular inputs: 12/12 section files and 3/3 figure files resolve and are
  included.
- Extracted-text draft-marker scan: 0 matches.
- Direct visual inspection covered all 17 pages, all three TikZ figures, every
  table, the bibliography, both appendices, and the final disclosure.  There
  is no clipping, collision, blank page, illegible label, or widow/orphan.
  In particular, Appendix A's opening paragraph is complete on page 14 and
  page 15 begins cleanly at Section A.1.

## Frozen five-file research boundary

The final build preserves the corrected authority research files byte for
byte:

```text
febaeb0b1db1a0713bbb68cf99110d7ecf2df8b39caf3ee9f311598f45fa6a7a  SOURCE_LOCK.md
606541a6852e9953882ba07bcaaa12efe06ab7f2a5c25346486a48c19fdbed2f  PREREGISTRATION.md
18c07306c64297338d6b85b4f830ce0ccd15317ec0ee22f0e57823064171307a  DERIVATION_PACKAGE.md
fdb49515d5baafc2baa00e5e3d510d940c6af813f8a32ce56e3116171f7b6d73  PROOF_PACKAGE.md
dd3b0e2e0258a6423f7a43266ca19d9597e1b3353e8491f7d51a81ab70b302d7  LITERATURE_AUDIT.md
```

The scientific boundary is the corrected split: for `r>=2` the action is
faithful with non-discrete image; for `r=1` the image is a discrete
translation copy of `Z`, while the original `Z^2` action has kernel `<u>`, is
non-proper, and fails the finite-stabilizer tree-lattice hypotheses.  No
superseded seed result is promoted to authority evidence.

## Canonical integration certificate

- Corrected exact evaluator: 277/277 assertions; scientific SHA-256
  `a9ffa66d826bcaf8eef0b00991aafa46cdbeaca7014430c68aacf070446adf24`.
- Fresh A, fresh B, and isolated cold C reproduce the scientific payload,
  source packet, and Route evaluation byte for byte; the cold copy is absent
  after the check.
- Integration tests: 44/44; full integrity audit: 96/96.
- Exact result set: 28 files; canonical managed text set: 44 files.
- Immutable ledger: 42/42 entries independently pass `sha256sum -c`; ledger
  SHA-256
  `af2db7457808bcb956c284d28387bf74bfda59f329b688e9491b5ef38066d309`.
- Integrity audit SHA-256:
  `0bb80e4dd9aed33c704fd2ca7bf2f2b2444043f664d6ce728ed92dc6d0183305`.
- Independent Route evaluation SHA-256:
  `984187abd5fced5e42c334763127ced28329fc4d9fbefe4d06b31427f509a434`.
- Fixed Route-A v0.2 YAML SHA-256:
  `32b2288b1397b084e73b4dd01d0bcc973f7326f963396463d532976e56d36a0c`.
- Experiment report SHA-256:
  `174b2ddf05fa41b5ddc06130fec14de628b51f410ec59dc905179a71f9eeb380`.
- Research lock SHA-256:
  `b338e75410116890e11b6d2d09a9d11c5c8e41fecd00a9c438997dde80435be3`.
- Corrected prototype lock SHA-256:
  `7a25ecee27974aa1f593f4793c7f44b8a940ad1b13f824f0a5f3c11669290c5b`.
- Prototype bridge SHA-256:
  `25d95b5c0e06aac15bd673b1d6547cdef4e71277445b1e69356d05f7ebd6e657`.
- Independent evaluator SHA-256:
  `0934d99fa05329d8146467e903b57f36e23588ce977354f3e948777c8ec5da13`.
- Test-result, exact-set, canonical-count, reproducibility, idempotence, and
  dependency-lock SHA-256 values are, respectively,
  `718a9cb50be393d148faa54407ec5af947b5c9b11c15ea58e149f92381c5ce30`,
  `4233fb2d5e4af966e7496c69f39c258ea98e992753f8a64a040a72a289dfac2b`,
  `f56b5bb70054f3e38eacd15a4a65237755b2d31dafcc70140c224ebbc200d231`,
  `90691ef8c207b104b23f215852d9b51d95e514c7e9e2e0bae1095f687f0ad611`,
  `56a3058840a1176e2341447917014398f4f09a8bb34bc40f44183e49aa400fe2`,
  and
  `14c8df242aa8c17d107701329141903b43a19ff8e15ca6fc3328292a933b63ff`.
- Four transport-metadata states and both simulated future-manifest states
  preserve the scientific and Route bytes.  A second primary materialization
  reports `changed_paths=[]`.

No undocumented aggregate is treated as a canonical certificate.  The
source and evaluator processes remain physically separated and do not import
one another.

## Decision and ownership

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
stop: STOP_BASS_SERRE_TREE_BRANCH
branch: CLOSE_ENTIRE_AFFINE_BRANCH
```

The independent integration layer owns `code/`, `results/`, `experiments/`,
`evaluations/`, `docs/`, `EXPERIMENT_REPORT.md`, and the Route artifacts.  The
repository root alone owns the future Stage-2 manifest and metadata seal.  No
writer action touched those paths, the root README, Git state, or a mirror.
No review loop was run.

After inspection, all LaTeX build auxiliaries were moved out of the authority
directory.  The complete text tree is UTF-8/LF, has exactly one terminal
newline per file, and has no trailing whitespace, disallowed control byte,
symlink, cache, bytecode, or writer-created manifest.
