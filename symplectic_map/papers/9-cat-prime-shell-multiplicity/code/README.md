# Paper 9 exact-audit implementation

This closed-world Python package implements only the fixed falsification
controls authorized for Paper 9.  Its scientific inputs are hard-coded as the
cat matrix `((2,1),(1,1))`, inherited primes `(2,3,5,7,11)`, and formal
repeats `(1,2,3)`.  There is no scientific command-line parameter.

The two finite-field engines are independent at the implementation level:
`analytic_case_certificate` uses the split/inert/Jordan case proof and matrix
order, while `direct_enumeration_certificate` constructs the full nonzero
vector permutation and its primitive cycles.  The registered candidate
requires both engines and the frozen source ledger to agree exactly.

Formal output keeps the point-potential/raw-return product separate from the
one-time orbit-label product.  It uses rational strings, never a floating
value of `s` or `log(p)`.  The mechanism ledger includes denominator degree,
the zero-weight boundary, equal weights at repeats 1--3, exact fractional
shell mass, selector discard cost, and a purely symbolic composite-`q`
identity.  Global convergence statements remain a proof-only schema.  The
centralizer is explicitly outside scope and is never computed.

The safe lifecycle is:

1. run pytest with bytecode/cache disabled and emit
   `results/PRE_EXECUTION_TESTS.xml`;
2. run `scripts/run_safe_preflight.py`;
3. have a fresh independent reviewer inspect the exact framed tree hash and
   write one canonical `DEPLOYMENT_PASS` authority to
   `results/CODE_REVIEW.md`;
4. rerun the safe preflight and only then invoke
   `scripts/run_registered_audit.py` once;
5. produce human reports, post-run tests, and an independent hash-bound
   `RESULT_PASS` before building the strict manifest.

The registered command writes a durable exclusive `STARTED` claim before it
imports the candidate.  Any orphan claim, result, terminal, extra result
file, stale review, source mismatch, code-tree change, or theorem-control
disagreement fails closed.  A passing run is development-seen finite
reproduction only; it cannot prove the all-prime or convergence theorems,
increase novelty, open Route B, or authorize Paper 10 centralizer work.
