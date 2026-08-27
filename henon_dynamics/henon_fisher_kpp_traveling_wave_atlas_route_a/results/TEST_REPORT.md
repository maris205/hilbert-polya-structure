# C202 test report

## Executable gates

All commands were run from the package directory on 2026-08-27.

- Producer: `C202_PRODUCER_PASS`; 17 speed cases, 340 phase rows and 25
  trapping rows; payload hash exactly reproduced.
- Independent checker: `C202_CHECKER_PASS`; 2,579 assertions.  It imports no
  producer code, reconstructs formulas with `Fraction` and high-precision
  `Decimal`, uses an independent bisection implementation for Hamiltonian
  turning points, and closes exact key sets plus hash-locked static sections.
- SymPy reconstruction: `C202_SYMPY_PASS`; 1,511 checks.
- Byte replay: `C202_REPLAY_PASS`; 110,686 bytes and SHA-256
  `605176e6653d796b6f86b1df8493a64d07ef8bca0fa308b256bf970d27110243`.
- Hostile mutations: `C202_MUTATION_PASS`; 101 repaired-payload-hash
  rejections, including 8 unknown-key injections, plus 1 stale-hash
  rejection, for 102 total rejections.

## Source and proof gates

The Fisher and Ablowitz--Zeppetella records are locked by their publisher DOI
metadata.  The KPP English translation is locked to *Selected Works of A. N.
Kolmogorov I*, pp. 242--270: the official table of contents starts the entry
at p. 242 and the following entry at p. 271.  The paper explicitly attributes
the classical theorem and exact special-speed solution.

The continuum existence statement is proved with the complete three-edge
inward check for the invariant triangle, the saddle unstable branch,
Poincare--Bendixson/Bendixson exclusion and the energy identity.  No sampled
speed grid or numerical shooting ledger is treated as that proof.

## Paper gates

The final 3-page PDF is LuaLaTeX-built at fixed epoch `1787788800`.  The three
substantive revision PDFs have distinct hashes; `main.pdf` is byte-identical
to round 2.  Two additional fresh builds reproduce the final hash exactly.
All fonts are embedded, text is extractable, the final log has no warnings,
undefined references, missing characters or bad boxes, and all three pages
were visually inspected.

## Failure-mode boundary

This is a theorem-and-exact-regression paper, not an empirical ML study.
There are no learned metrics, runs, clinical data or fabricated experimental
outcomes.  Producer/checker separation, symbolic reconstruction, replay and
hostile mutation tests address implementation-bug and result-drift risks
within their finite scope.  Classical source verification and explicit
nonclaims address citation, methodology and frame-lock risks.  These checks
do not establish independent error processes, global literature priority or
external peer review.
