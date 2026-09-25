# Evidence — ASFS-20260915-SDC01

**Date:** 2026-09-15  
**Status:** PRIME-ONLY HYPERBOLIC PACKETS AND ORDINARY ZETA ESTABLISHED; TARGET CLOCK AND OPERATOR OPEN.

## Inputs and methods

The [version-1 card](../candidate-card.md) fixes all integers n>=2, the exact
binary phase count, local divisor tests, tanh coefficient 1/2, gain K_n,
full plane carrier, cotangent update and unit roof before results.
No prime table, Riemann-zero data, orbit fit or parameter sweep was used.

The [paper](../paper.md) is the complete evidence:

1. Proposition 1 checks monotonicity, onto behavior, the full inverse and
   exact preservation of the canonical one-form.
2. Proposition 2 constructs the mapping torus and checks both time directions.
3. Propositions 3--4 quantify over every real position and momentum, every
   integer fibre and every possible positive period.
4. Proposition 5 differentiates the same map on its derived full periodic set.
5. Proposition 6 proves convergence bounds and the exact absolute abscissa
   using an included elementary prime-harmonic divergence argument.
6. Section 6 proves the three arithmetic comparator outcomes, retains the
   empty n=2 block, and discloses gain, clock and PROVES_TOO_MUCH limits.

No numerical computation is part of the mathematical evidence. Accordingly
there is no numerical precision, orbit cutoff, trajectory output or claim
that a finite run proves a global result. The proofs can be checked from
the displayed equations alone.

## Verification and review

The first completed-package check used Node.js via an inline shell heredoc
from the workspace root. It recursively read the five Markdown files under
papers/147-saturated-drift-cotangent-sieve; extracted Markdown destinations
with /\[[^\]]*\]\(([^\s)]+)\)/g; skipped HTTP, mail and fragment-only
destinations; resolved all local paths from their referring file; checked
the candidate ID and exact status in each file; and rejected trailing
whitespace other than conventional two-space Markdown hard breaks.

Recorded output:

~~~text
{
  "files": 5,
  "localLinks": 15,
  "errors": []
}
~~~

The command git diff --check -- papers/147-saturated-drift-cotangent-sieve
also returned successfully. The filesystem pass, not this Git command,
covers new untracked files. These checks establish file consistency, not
mathematical correctness. Independent model review, when linked here, is
not human peer review or an external publication verdict.

The completed [independent model review](review.md) checks Propositions
1--6 and all three arithmetic controls and reports no mathematical blocker.
Its minor scope clarification about integer-valued constraints was applied
to the claim ledger; the abstract also states that the present exact
prime-log identity fails rather than leaving that identity undecided.
The reviewer verified both clarifications. No map, roof, proof or analytic
normalization changed.

After including that review and its navigation link, the same filesystem
checks returned: 6 Markdown files, 20 local links, zero errors. Candidate
identity, exact status and whitespace checks passed across all six files.
