# Paper25 — Holomorphic Lefschetz Code Collapse

Candidate **SD-C27** tests the anisotropic/holomorphic function-space escape
left open by SD-C26.  It proves that the canonical zero-/one-form pullback
pair cancels an affine branch's fixed-point denominator at every repetition,
but that the resulting graded determinant retracts to degree-zero
cohomology.

The global dichotomy is exact:

- a shared renewal disk gives \(1-z\sum_n n^{-s}\) and retains every mixed
  primitive return necklace;
- disjoint disks give \(\prod_n(1-zn^{-s})\), but this is precisely the
  diagonal atom-loop determinant for the supplied inventory.

The result is a genuine analytic A2 advance and an arithmetic A1 failure.
It uses no target-zero data and makes no RH or Hilbert–Pólya claim.

## Frozen evaluation

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

## Artifact map

- `SOURCE_LOCK.md` — frozen code, branches, spaces, assemblies, markers,
  and route record;
- `PAPER_PLAN.md` — claims–evidence matrix and manuscript architecture;
- `PROOF_PACKAGE.md` — complete theorem chain;
- `DERIVATION_PACKAGE.md` — formula-by-formula derivation and ownership
  ledger;
- `LITERATURE_AUDIT.md` — primary-source and bounded-novelty audit;
- `NARRATIVE_REPORT.md` — concise research outcome and next obligation;
- `FIGURE_SPEC.md` — publication figure requirements;
- `ROUND2_CLUES.md` — quarantined analogies only;
- `sections/` and `figures/` — modular manuscript sources;
- `main.tex`, `math_commands.tex`, `references.bib` — LaTeX authority;
- `main.pdf` — compiled paper;
- `COMPILATION_REPORT.md` — final build and artifact audit.
- `EXPERIMENT_REPORT.md`, `code/`, `docs/`, `experiments/`, and `results/` —
  independently integrated exact evidence, maintained outside the authority
  writer's ownership.

Evaluation ledgers, manifests, root documentation, and Git synchronization
are maintained outside this authority-writer scope.

## Build

From this directory:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The manuscript explicitly preserves the ordinary/graded,
shared/disjoint, and digit/return ownership firewalls.
