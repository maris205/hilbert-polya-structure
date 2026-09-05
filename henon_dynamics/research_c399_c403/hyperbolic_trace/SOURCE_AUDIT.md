# Source and collision audit: hyperbolic ordinary-trace obstruction

Date: 2026-09-05. Status: pre-admission; independent significance review pending.

## Directly inspected repository inputs

- `henon_time_ordered_ruelle_cocycle/T4_T5_DERIVATION.md`, HCS-C22:
  orbitwise scalar failure, with the nonscalar/graded alternatives distinguished.
- `symbolic_dynamics/papers/25-holomorphic-lefschetz-code-collapse/DERIVATION_PACKAGE.md`,
  section 3: the exact trace-class tensor obstruction for one contracting affine
  branch, with target moments $1-q^r$. The rational-pole argument is already here.
- Targeted theorem/proof/derivation searches for Schatten, ordinary tensor,
  stability cancellation and hyperbolic traces: other packages establish
  noncompactness of particular source operators, not this universal search over
  all ordinary Schatten fibers having a given repeat sequence.

These are different claims. This note must not call scalar-to-trace-class a new
repository mechanism or claim to solve the analytic global graded complex.

## Primary operator source actually opened

Thomas Britz, Alan Carey, Fritz Gesztesy, Roger Nichols, Fedor Sukochev and
Dmitriy Zanin, *The product formula for regularized Fredholm determinants*,
arXiv:2007.12834v2 (2020), subsequently Proc. Amer. Math. Soc. Ser. B 8 (2021).
[Full primary HTML](https://arxiv.org/html/2007.12834v2), introduction,
equations (1.1)–(1.3).

Equation (1.3) fixes the integer-order canonical product used here. The source's
main product-formula result is not this note's contribution. Standard trace
and exterior-algebra identities retain their classical ownership.
The HTML rendering displays a 2026 conversion date as well as the 2020 arXiv
version stamp; the conversion date is not treated as the publication date.

An Evans-function/Fredholm primary article was located but its PMC full-text
open returned a browser challenge in this run; it is not counted as read.
Search results on third-party upload sites were not used as proof authority.

## Bounded search and proposed increment

Queries included regularized determinants/Schatten trace powers;
stability determinants/supertrace; power sums/trace class/multiplicities; and
minimal graded dimension/hyperbolic exterior products. No direct full-contract
match was identified in that bounded search. This is not global novelty proof.

The proposed repository increment is the combined complete classification:

1. Every real invertible hyperbolic monodromy, without sign, Jordan or
   multiplicative-independence restrictions.
2. Every finite Schatten exponent and every tail after finitely many free
   moments, not just trace class at the first repetition.
3. Exact least graded dimension after resonant products merge.
4. The contrasting theorem that every finite prefix can be realized by a real
   normal finite matrix of unrestricted dimension. Normality is not a finite
   escape restriction; self-adjointness is materially different.
5. For real-spectrum monodromy, the exact inertia of every even-shifted finite
   Hankel matrix and a Lagrange polynomial giving a negative trace certificate
   against self-adjoint realizations. This extra hypothesis distinguishes the
   finite-testable positive-trace problem from the unrestricted problem.

The basic proof tools are classical, and P25 already supplies the pole idea.
If independent review finds the above remaining classification too incremental
for the user's large-step paper criterion, this candidate is not admitted.
No arithmetic label, target divisor, Euler factor or Hilbert–Pólya operator
is inferred from this local obstruction.
