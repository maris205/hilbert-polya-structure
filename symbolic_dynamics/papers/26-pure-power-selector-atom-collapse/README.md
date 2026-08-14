# Paper26 — Pure-Power Selector and Atom Collapse

Candidate **SD-C28** asks whether the mixed return necklaces left by Paper25
can be removed by a source-derived cyclic incidence selector without first
splitting the renewal system into one recurrent component per supplied atom.

The coefficient problem has an exact positive answer: a support-dependent
exterior coefficient and the stationary projector character both assign
coefficient one to every nonempty monochromatic word and zero to every mixed
word, at all repetitions.  The structural answer is negative.  Every
finite-dimensional stationary wordwise trace realization has observable
semisimple content equal to one character per supplied color; radicals,
dormant sectors, and matched even/odd sectors are trace-invisible.  Tensoring
with the Paper25 holomorphic de Rham sector therefore gives the disjoint
color/atom product rather than a new shared-renewal mechanism.

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

The A2 object is a graded/relative determinant assembled from separately
honest trace-class operators on `Re(s)>1`.  It is not an ordinary determinant
of an ungraded block sum.  Prime labels are only one specialization of an
arbitrary supplied inventory; no target-zero data are used.

## Artifact map

- `SOURCE_LOCK.md` — frozen alphabet, coefficient, trace and analytic scope;
- `PREREGISTRATION.md` — theorem gates, adversaries, and exact audit protocol;
- `PAPER_PLAN.md` — claims–evidence matrix and manuscript architecture;
- `PROOF_PACKAGE.md` and `DERIVATION_PACKAGE.md` — theorem chain and formulas;
- `LITERATURE_AUDIT.md` — primary-source boundary and novelty calibration;
- `NARRATIVE_REPORT.md` and `ROUND2_CLUES.md` — outcome and next obligation;
- `FIGURE_SPEC.md`, `figures/`, and `sections/` — publication sources;
- `main.tex`, `math_commands.tex`, `references.bib`, and `main.pdf` — paper;
- `COMPILATION_REPORT.md` — final build and artifact audit.

The independent exact integrator owns `code/`, `results/`, `experiments/`,
`EXPERIMENT_REPORT.md`, `docs/`, and `evaluations/route_a/SD-C28/`.  Manifests,
root documentation, Git synchronization, and route-registry edits are outside
the authority writer's scope.

## Build

From this directory:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The manuscript preserves the wordwise/abelianized, ordinary/graded,
stationary/support-dependent, empty-word, and digit/return-marker firewalls.
