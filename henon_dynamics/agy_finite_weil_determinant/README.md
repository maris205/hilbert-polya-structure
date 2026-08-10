# HCS-C27 — AGY finite-Weil chronology determinant

HCS-C27 opens the finite-fibre door proposed by C26. For every fixed odd
prime p, the source-locked genus-two Rauzy–AGY cocycle is reduced to
Sp(4,F_p) and twisted by its genuine p²-dimensional Weil representation.

The main positive result is exact: for each fixed p, the twisted operator is
trace class on the C26 Bergman domain and has an ordinary Fredholm
determinant. A periodic word contributes its scalar Perron atom multiplied by
the exact finite Weil character Theta_p(g_word). At primes that do not divide
det(g-I), this character is the Legendre symbol of det(g-I) modulo p.

## What the large gate found

- The C26 three-return forward and noncyclic reverse finite-fibre
  polynomials differ at p = 3, 5, 7.
- Across odd p ≤ 97 and powers 1 ≤ r ≤ 24, 328 of 576 exact Weil
  characters differ.
- At p = 43, both matrices have order 925 and their characters agree for
  the complete period. Their degree-1849 **finite-fibre** polynomials are
  equal even though the base characteristic polynomials differ. Their scalar
  AGY atoms do not coincide.
- C24-P076 and P082 are distinct symbolic cycles but are explicitly
  conjugate in Sp(J24,Z), where J24 is the frozen C24 symplectic form. Every
  class-function fibre collapses their full
  repetition towers at every prime.
- All 150 source-locked branches in the bridge-length-at-most-12 census have
  different discriminants, characteristic polynomials, and Legendre
  signatures over the odd primes below 100.

Thus the finite Weil fibre repairs the ordinary-determinant obstruction and
adds genuine arithmetic chronology signals, but it does not provide a
separating invariant or a common global conductor. The modulus remains an
external parameter; no adelic product, self-adjoint Hilbert–Pólya operator,
functional equation, or Riemann-zero correspondence is claimed.

## Reproduce

```bash
cd henon_dynamics/agy_finite_weil_determinant
python -m pip install -r requirements.txt
bash code/run_c27.sh
```

The producer and checker are independent. Both use exact finite-field and
rational arithmetic; numerical phases are not used for decisions.

## Project map

- `RESEARCH_QUESTION.md` — the frozen mathematical question;
- `EXPERIMENT_PLAN.md` — pass/fail gates and scope;
- `THEOREM_PACKAGE.md` — proofs and exact theorem boundary;
- `SOURCE_AUDIT.md` — C24–C26 provenance and chronology conventions;
- `PAPER_PLAN.md`, `NARRATIVE_REPORT.md` — paper story and evidence map;
- `paper/main.pdf` — compiled manuscript;
- `code/` — producer, independent checker, tests, and release runner;
- `results/` — complete certificates, reports, and hashes;
- `route_a_evaluation.yaml` — conservative Route-A decision.

## Decision

The Route-A tuple is:

```text
(A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_NATURAL_QUANTIZATION)
```

with overall status `ROUTE_A_EXPLORATORY`. Route B is not authorized. The
next step is a large gate only: derive an intrinsic global prime/adelic trace
from the dynamics, or pivot to a different dynamical form.
