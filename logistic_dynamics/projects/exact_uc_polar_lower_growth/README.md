# Exact-\(U_c\) polar lower-growth stage

Stage ID: `LOG-0001-LOWER-GROWTH`.

This standalone stage keeps the exact-\(U_c\) polar map, intrinsic roof,
matching space, signed based-word trace ledger, and canonical Fredholm
determinant unchanged.  It extracts a cancellation-safe lower bound at the
safe real point \(s=2\).  With

\[
\alpha_0=\frac{U_c^2}{4},\qquad
\tau_*=-\log\alpha_0,\qquad
B_2=\frac{-\log(1-2\alpha_0^2)}{1-\alpha_0},
\]

the same determinant satisfies

\[
D_{\rm pol}'(2)\ge
e^{-B_2}\frac{\tau_*\alpha_0^2}{1-\alpha_0}
>0.0213.
\]

Cauchy's derivative estimate then gives, for
\(M_D(R)=\max_{|s|\le R}|D_{\rm pol}(s)|\),

\[
M_D(R)>0.0213(R-2)\quad(R>2),
\qquad
M_D(R)>0.01065R\quad(R\ge4).
\]

The trace logarithm also gives \(D_{\rm pol}(\sigma)\to1\) as
\(\sigma\to+\infty\).  Together with \(D_{\rm pol}'(2)>0\), this proves that
the entire determinant is transcendental and hence that its maximum modulus
grows faster than every fixed power, qualitatively.

The result does **not** prove positive or exact entire-function order, an
exponential lower bound, a zero-count lower bound, a \(T\log T\) law, a
completed-xi identity, or the Riemann hypothesis.

## Contents

- `PAPER_PLAN.md`: fixed claim--evidence map and manuscript outline.
- `NARRATIVE_REPORT.md`: theorem narrative and strict claim boundary.
- `source_lock.yaml` and `route_a_evaluation.yaml`: standalone decision
  records, mirrored byte-for-byte under `configs/` and `evaluations/`.
- `results/` and `formal/`: byte-identical copies of the formal theorem note.
- `paper/`: modular standalone manuscript.
- `src/`: self-contained certificate generator.
- `tests/`: eleven target-free regression and reproduction tests.
- `artifacts/`: canonical and convenience copies of the 1024-bit outward Arb
  certificate, plus a local copy of the inherited growth-order certificate
  used only for provenance.

The generator freezes the same 100-decimal-place rational bracket

```text
[1.5436890126920763615708559718017479865252032976509839352408040378311686739279738664851579145760591254,
 1.5436890126920763615708559718017479865252032976509839352408040378311686739279738664851579145760591255]
```

inside the project.  Exact rational arithmetic checks the two polynomial
signs, the width `10^-100`, and global positivity of
`3*u^2-4*u+2` through its discriminant `-8`.  No module outside this project,
including the legacy first-return support program, is imported.

## Reproduction

From this project directory, run:

```bash
PYTHONPATH=. python3 tests/test_log_0001_lower_growth.py
PYTHONPATH=. python3 src/log_0001_lower_growth.py \
  --quiet \
  --output artifacts/log_0001_lower_growth/lower_growth_certificate.json
```

The regression regenerates the artifact in a temporary directory and requires
byte-identical output.  It also verifies every provenance hash, the frozen
python-flint/FLINT versions, the data firewall, the source-lock and Route-A
copies, and restoration of the global Arb precision context.

Build the manuscript with:

```bash
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Validated environment: Python `3.12.3`, python-flint `0.9.0`, FLINT `3.6.0`,
and 1024-bit Arb arithmetic.
