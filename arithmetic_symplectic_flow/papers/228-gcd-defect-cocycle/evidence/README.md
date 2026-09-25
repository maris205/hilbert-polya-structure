# Evidence record — ASFS-20260918-GDC01

## Scope and provenance

This is a symbolic proof audit of a freshly frozen candidate. The candidate
card was written before the paper proof. No prime table, Riemann-zero data,
fitted parameter, numerical search, GPU run, or finite-cutoff extrapolation was
used. The only arithmetic input is the gcd of the frozen integer state
(n,d). The roof is the unit function belonging to the displayed map.

## Exact checks

1. **Carrier and inverse.** The phase successor is a bijection on every D_n;
   the integer inverse subtracts the predecessor defect; and (7) is the
   integral inverse of every A_δ. Since det A_δ=1, each component preserves
   dq∧dp.
2. **Suspension completeness.** Every crossing costs one unit, so inf τ=1 and
   no trajectory has finite-time forward or backward accumulation.
3. **Periodic ledger.** A return must use m=r(n−1) steps. The defect sum
   D_n is positive for every composite n, forcing positive k drift. For a prime
   p the defect is identically zero; hyperbolicity of A_0 leaves z=0 as the
   only geometric return.
4. **Packet and repetition convention.** Each pair (p,k) owns exactly one
   primitive phase packet of p−1 states, and the unit-roof flow period is p−1.
   Repetitions are r(p−1), not new primitive packets.
5. **A1 stops.** The clock is not logarithmic. The full ledger has infinitely
   many k-labelled packets at each prime, so the ordinary repetition product
   diverges for every possible half-plane.

## Controls

The paper records four candidate-specific controls: replacing gcd−1 by an
indicator divisor defect; using a fixed single-cycle shuffled phase order;
projecting away k; and setting all geometry matrices to A_0. The first two
preserve the zero/positive drift result, while projection destroys composite
exclusion and the A_0-decoupled control isolates the source in the k register.

## Verification commands

The package was checked after writing with:

    find papers/228-gcd-defect-cocycle -maxdepth 2 -type f -print
    rg -n 'ASFS-20260918-GDC01|SCOPED FAIL|NOT INVOKED' papers/228-gcd-defect-cocycle
    for p in papers/228-gcd-defect-cocycle/README.md papers/228-gcd-defect-cocycle/paper.md; do rg -o '\]\([^)]*\)' "$p" | sed 's/^](//' | sed 's/)$//' | while IFS= read -r target; do case "$target" in http*|'#'*) continue;; esac; test -f "$(dirname "$p")/$target" || exit 1; done; done
    git diff --check -- papers/228-gcd-defect-cocycle

The first command lists exactly the five Markdown files in this package
(including evidence/README.md). The second confirms candidate-ID and status
strings in every package record. The third exits successfully only when every
local link in README.md and paper.md resolves. The fourth reports no
whitespace errors. No external link or root-file edit is required by this
package.

## Ownership and limits

During the neighboring 231 proof audit on 2026-09-18, a separately dispatched
checker identified repeated-orbit double counting in the original display of
paper equation (14). Integration corrected it to one Euler factor per
primitive (p,k), with repetitions and their 1/r factor only in the logarithm.
The infinite-k divergence already follows from r=1 and is unchanged. This is
a formula correction, not a new analytic object or a changed candidate.

The same-object ledger remains intact from gcd source through map, unit roof,
flow, primitive convention, and repetition law. This evidence does not supply
an analytic owner, a transfer operator, a determinant, a trace, a target
divisor, or a formal Route coordinate. The result is an exact infinite-family
theorem with a scoped A1 failure, not a finite computation and not a Route
pass.
