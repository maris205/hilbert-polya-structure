# Evidence record — ASFS-20260918-SPK01

**Status:** `SCOPED ENGINEERING POSITIVE — CONNECTED EXACT SYMPLECTIC OWNER;
COMPLETE PRIME-ONLY LEDGER; A0 NATURALNESS OPEN; UNIT-ROOF TARGET CLOCK SCOPED FAIL`

## Exact inputs and methods

The [candidate card](../candidate-card.md) fixes all integer coefficients,
the explicit compact bump, smooth cutoff, complete real plane, kick/shear and
unit roof.  Its v1 clarification fixes the initially unnamed bump before any
proof output.  No theorem depends on sampled primes or an orbit cutoff.

The reproducible proof methods are in the [paper](../paper.md):

1. Restrict a compact real interval; only finitely many bump supports meet it.
   Differentiate the resulting finite smooth sum.  Classify its zeros by the
   nonnegative terms and the elementary small-divisor criterion.
2. Substitute equation (6) into (4) in both directions.  Pull back
   \(dx\wedge dp\) and \(\lambda=-p\,dx\) to verify the exact identities.
3. For arbitrary positive integer period \(m\), sum the momentum recurrence
   (9), use nonnegativity, then sum the position recurrence.  This proves the
   full ledger without enumeration.
4. Use height modulo one and the global inverse to classify suspension
   periods and establish forward/backward completeness.
5. Differentiate at a nonnegative zero to obtain the unipotent monodromy;
   inspect the \(r=1\) part of (15) for product divergence.

The adversarial controls are the full nonnegative-amplitude family (14), its
bump-free member, the shifted-divisor member, an arbitrary finite-block
permutation and a uniformly randomized choice of that permutation.  These are
exact conditional control statements; there was no random draw, numerical
experiment, finite search or statistical inference.

## Verification limits

Source naturalness remains OPEN.  The prime selector is encoded statically
in the coefficient sequence, so an operational owner theorem is not a
natural A0 result.  The target prime-log clock is a scoped FAIL, not OPEN:
this frozen candidate has unit lengths for all primes.  No non-unit roof,
regularization, new analytic owner, logarithmic insertion or per-prime weight
was used.  Parabolic monodromy blocks the usual nondegenerate denominator,
not every conceivable future trace theory.

No PDF, LaTeX, publication artifact, external upload or repository-wide
mutation is part of this package.  Formal Route-A coordinates are UNASSIGNED;
Route B is NOT INVOKED.

## Local handoff checks

The package has five Markdown files: this evidence record, the
[paper](../paper.md), [card](../candidate-card.md),
[claim ledger](../claim-ledger.md), and [summary](../README.md).  The exact
candidate ID is `ASFS-20260918-SPK01` throughout.  A separately dispatched
read-only model checker independently checked the frozen formulas, inverse,
exact primitive, all-state periodic proof, unit suspension, monodromy and
ordinary-product boundary; it reported no error in those claims.  This is
same-family model checking, not external peer review or a correctness
certificate.  The checker also emphasized that some complex partial products
may tend to zero, so the paper makes the narrower no-absolute-half-plane
claim instead of claiming failure of every complex partial-product limit.

On 2026-09-18 a local Perl check read exactly these five files, extracted
Markdown link destinations, resolved relative destinations against each
containing directory, and required the exact candidate ID in every file.
Its stdout was `link and ID errors=0` and its exit status was zero.  The
integration owner performs final cross-surface status checks after handoff.
These mechanical checks do not establish mathematical correctness or external
peer review.

The integration owner's separately dispatched read-only checker then read all
five final package surfaces and reported no mathematical or ownership mismatch.
The reviewed paper SHA-256 is
`48c8a2e525b61e622f246a5c95fa1636916b7411626e80d3db7d6532b00ede93`.
The 2026-09-18 final integration check used Node filesystem reads to require
the expected candidate ID and stop boundary in all five files of each of
packages 230 and 231 and resolve local Markdown links, excluding code
examples. It reported 10 files and 42 package links passing, with both IDs
registered and 433 local links resolving across the two root/index files.
The paper hashes matched the separate checkers' reviewed versions;
`git diff --check` also passed for the tracked integration changes.
These are consistency receipts, not Route or peer-review credentials.

**Portfolio:** stop / fork; preserve the connected symplectic owner and full
unit-roof ledger as an engineering control.
