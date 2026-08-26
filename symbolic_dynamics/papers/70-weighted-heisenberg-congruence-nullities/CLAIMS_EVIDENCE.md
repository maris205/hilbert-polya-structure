# Claims and evidence ledger

| ID | Claim | Evidence | Status |
|---|---|---|---|
| C1 | `N_ell`-fixed configurations identify with functions on `Heis(F_ell)`. | Normality and the frozen left-shift convention; Section 2. | PROVED |
| C2 | Scalar extension preserves the required nullity. | Exactness of field extension; Section 3. | PROVED |
| C3 | The regular module has `ell^2` character blocks and `ell-1` degree-`ell` families with regular multiplicity `ell`. | Explicit cross-characteristic clock--shift modules, irreducibility, squared-degree completeness, and matrix-coefficient right-action audit; Section 3. | PROVED |
| C4 | Singular character blocks are counted by the stated gcd degree. | Root-by-root elimination of the second character; Section 4. | PROVED |
| C5 | Every nonlinear determinant is `alpha^ell+beta^ell+gamma^ell`. | Clock--shift determinant and cyclotomic product; Section 5. | PROVED |
| C6 | A singular nonlinear block has nullity exactly one. | Cyclic first-order recurrence with `gamma != 0`; Section 5. | PROVED |
| C7 | The full fixed-space formula follows with jump `ell(ell-1)`. | C3--C6; main theorem. | PROVED |
| C8 | The original `1+a+b` shift jumps in characteristic three. | Main theorem with unit coefficients. | PROVED |
| C9 | Ten full quotient matrices exercise the displayed group law and selected finite operator and agree with the formula; four direct clock--shift blocks satisfy the determinant/nullity lemmas. | `code/verify_weighted_heisenberg.py`. | CONTROL PASS |
| C10 | Priority over all equivalent finite-quotient formulas. | A bounded search cannot establish this. | NOT CLAIMED |

## Evidence policy

Formal proofs carry C1--C8.  Computation can catch many transcription and
implementation errors, including an omitted regular multiplicity.  Comparing
only the total nullity cannot distinguish the right-translation convention
from the dual left convention, because the proved formula is invariant under
that change.  External sources establish context and ownership; no cited
theorem is silently used as a missing proof step.
