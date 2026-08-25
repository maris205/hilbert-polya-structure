# Paper improvement log

The external review transport specified by the generic paper workflow was not
available.  Two genuine internal theorem-and-scope reviews were performed;
no external independence, acceptance score, or reviewer score is claimed.

## Round 0

The original three-page paper proved the unitary/antiunitary identities,
signed primitive product, exact arrangement separation, and averaging
control.  It compiled without warnings.

## Round 1

Review finding: the two arrangements were asserted non-dihedral without an
immediate invariant, and the exact determinant calculation appeared as a
black box.

Fixes:

- added adjacency of the two `1` sites as a dihedral invariant;
- added the exact Newton recurrence
  `k d_k=-sum_(j=1)^k d_(k-j) Tr(U^j)`;
- retained the full polynomial factorization as an independently checked
  consequence.

The result is preserved as `paper/main_round1.pdf`.

## Round 2

Review finding: the A4 wording needed to distinguish temporal antiunitary
reversal from spatial word reflection and to prevent the unistochastic shadow
from being read as a unique classical quantization.

Fixes:

- stated that `Theta_w` reverses time on the same arrangement;
- stated that it does not map the word to its spatial reflection;
- denied uniqueness of the classical antecedent, a canonical logarithm, a
  growing-level limit, and a self-adjoint spectral realization.
- the rendered-page audit repaired two lost LaTeX spacing commands and one
  malformed transpose superscript before the round-two snapshot was sealed.

The result is preserved as `paper/main_round2.pdf`, byte-identical to the
final `paper/main.pdf`.

## Remaining boundary

The finite unitary structure is exact, but no target divisor, prime-like
semantics, growing family, or Route-B bridge is available.
