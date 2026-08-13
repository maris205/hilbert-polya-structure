# Paper 05 — Intrinsic Symbolic Grading and Duality

Status: **GO A2 GRADED ORIENTATION / STOP A3 COMPLETION / ROUTE B LOCKED**

Research index: [Ra-1: Arithmetic Symbolic Dynamics](../../README.md)

Shared rules: [proposal](../../propose-symbolic-dynamics.md),
[Route A](../../skills/route-a-evaluator.md), and
[Route B](../../skills/route-b-evaluator.md).

Paper05 asks whether the tensor-prime full-shift candidate SD-C07 can acquire
an intrinsic grading and a genuine \(s\leftrightarrow1-s\) duality without
importing arithmetic signs or analytic continuation.

The grading branch succeeds. For the open tensor-divisor order complex
\(\Delta_n\),

\[
\widetilde H_j(\Delta_n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&n\text{ squarefree},\ j=\omega(n)-2,\\
0,&n\text{ nonsquarefree}.
\end{cases}
\]

Thus its supertrace is \(\mu(n)\), tensor atoms are odd, and in
\(\Re s>1\)

\[
\operatorname{Str}_{\Lambda^\bullet V}\Gamma_-(L_s)=\frac1{\zeta(s)},
\qquad
\operatorname{Ber}_{V_{\bar1}}(I-L_s)=\zeta(s).
\]

The completion branch stops. The honest equivariant Koszul resolution
cancels to supertrace \(1\); natural symbolic reversal gives \(s\mapsto s\);
tensor-group inversion gives \(s\mapsto-s\). Even after granting an external
\(s\leftrightarrow1-s\) pairing, the first shared regularization is a
paired \(\det_3\) on \(1/3<\Re s<2/3\). It is zero-free and deletes the
prime and prime-square traces \(r=1,2\).

The exact CPU experiment verifies all 511 complexes through \(N=512\):
zero \(\partial^2\), Euler, homology, or coefficient failures. Random,
global, Liouville, shifted-law, additive, and free-mixing controls separate
the canonical factorization degree from convenient signs.

The preregistered G4 gate fails, so this is a graded enhancement of SD-C07,
not a new SD-C08.

## Shareable paper and artifacts

- [main.pdf](main.pdf) — compiled paper.
- main.tex, sections/, figures/, math_commands.tex, references.bib — modular
  LaTeX source.
- [SOURCE_LOCK.md](SOURCE_LOCK.md) and
  [PREREGISTRATION.md](PREREGISTRATION.md) — frozen object and gates.
- [PROOF_PACKAGE.md](PROOF_PACKAGE.md) — theorem statements and derivations.
- [NARRATIVE_REPORT.md](NARRATIVE_REPORT.md),
  [PAPER_PLAN.md](PAPER_PLAN.md), and
  [LITERATURE_AUDIT.md](LITERATURE_AUDIT.md) — story and novelty boundary.
- [EXPERIMENT_REPORT.md](EXPERIMENT_REPORT.md), code/, experiments/, and
  results/ — exact computation and controls.
- [Route-A evaluation](evaluations/route_a/SD-C07/20260813T230000Z.yaml) —
  SD-C07 graded enhancement; no SD-C08.
- [PAPER_MANIFEST.sha256](PAPER_MANIFEST.sha256) — final checksums.

## Reproduce

From this Paper05 project root:

~~~bash
PYTHONDONTWRITEBYTECODE=1 \
  python code/intrinsic_grading_experiment.py --N 512 --output results

PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest discover -s code -p 'test_*.py' -v

pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

No Riemann zeros are read, fitted, or tested. Route B remains locked.
