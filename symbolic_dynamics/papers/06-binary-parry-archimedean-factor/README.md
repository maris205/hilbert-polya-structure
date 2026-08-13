# Paper 06 — Binary Parry Archimedean Factor

Status: **GO A3 ARCHIMEDEAN FACTOR / STOP GLOBAL COMPLETION / ROUTE B LOCKED**

Candidate: **SD-C08**, the minimal-binary Parry/Hellinger extension of
SD-C07.

Research index: [Ra-1: Arithmetic Symbolic Dynamics](../../README.md)

Shared rules: [proposal](../../propose-symbolic-dynamics.md),
[Route A](../../skills/route-a-evaluator.md), and
[Route B](../../skills/route-b-evaluator.md).

Paper06 uses one source only: the symmetric monoidal family of finite full
shifts. Its unique least nonunit tensor atom is the binary full shift
\(F_2\). The maximal-entropy Parry kernel

\[
K_2=J_2/2
\]

has an intrinsic, multiplicity-one decomposition under symbol permutations:
the trivial line supplies the exact tensor-prime Euler ledger, while the sign
line supplies a canonical centered observable. Consequently

\[
\det(I-\mathcal A_s)=\prod_p(1-p^{-s})=\zeta(s)^{-1}
\quad (\Re s>1),
\]

and, for odd \(N\),

\[
\mathbb E\left|\frac{S_N}{\sqrt{2\pi N}}\right|^{s-1}
\longrightarrow \pi^{-s/2}\Gamma(s/2)
\quad (\Re s>0).
\]

Both are specializations of one tilted Parry trace. For
\(Q=\operatorname{diag}(1,-1)\),

\[
H(z)=e^{zQ/2}K_2e^{zQ/2},\qquad
\operatorname{tr}H(z)^r=(\cosh z)^r.
\]

At \(z=0\) this is the Euler ledger; at \(z=iu/\sqrt r\) it converges to
the Gaussian characteristic function.

This gives the same-source Mellin–Fredholm factorization

\[
\mathfrak Z_{\rm SD}(s)
=\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad \Re s>1.
\]

It is not claimed to be one dynamical determinant. No meromorphic
continuation, pole removal, functional equation, or Riemann-zero divisor is
derived. That boundary is essential: multiplying unrelated favorable
coordinates remains forbidden.

The accompanying no-motion theorem is equally decisive. Every
block-preserving Hellinger chiral completion commuting with the tensor-mass
operator is unitarily conjugate along \(s=1/2+it\). Its spectrum cannot move
with \(t\). For the frozen block, the first common regularization is
\(\det_3\); it deletes the divergent quadratic trace and is independent of
\(s\). Thus a vertical divisor would require intrinsic cross-atom coupling,
but naive coupling creates forbidden mixed primitive cycles.

The CPU prototype verifies the finite identities and separates the controls.
Uniform \(K_3,K_4\) and biased rank-one kernels preserve the Euler ledger, so
rank one alone proves too much. Canonical radial \(q\)-symbol fluctuations
have a dimension-shifted Gamma factor and select \(q=2\), but one-dimensional
CLT universality remains an explicit limitation. No Riemann-zero data are
loaded or fitted.

## Shareable paper and artifacts

- [main.pdf](main.pdf) — compiled paper.
- main.tex, sections/, figures/, math_commands.tex, references.bib — modular
  LaTeX source.
- [SOURCE_LOCK.md](SOURCE_LOCK.md) and
  [PREREGISTRATION.md](PREREGISTRATION.md) — frozen object, controls, and
  promotion gates.
- [PROOF_PACKAGE.md](PROOF_PACKAGE.md) — exact derivations and claim boundary.
- [NARRATIVE_REPORT.md](NARRATIVE_REPORT.md) and
  [PAPER_PLAN.md](PAPER_PLAN.md) — compact research story and manuscript map.
- [LITERATURE_AUDIT.md](LITERATURE_AUDIT.md) — primary-source boundary and
  finite-search synthesis claim.
- [EXPERIMENT_REPORT.md](EXPERIMENT_REPORT.md), code/, experiments/, and
  results/ — executable falsification package.
- [Route-A evaluation](evaluations/route_a/SD-C08/20260813T235000Z.yaml) —
  frozen SD-C08 tuple and Route-B lock.
- [COMPILATION_REPORT.md](COMPILATION_REPORT.md) and
  [PAPER_MANIFEST.sha256](PAPER_MANIFEST.sha256) — build and integrity record.

## Reproduce

From this Paper06 project root:

~~~bash
PYTHONDONTWRITEBYTECODE=1 \
  python code/symbolic_archimedean_experiment.py --out results

PYTHONDONTWRITEBYTECODE=1 \
  python code/test_symbolic_archimedean_experiment.py

pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

Route B remains locked.
