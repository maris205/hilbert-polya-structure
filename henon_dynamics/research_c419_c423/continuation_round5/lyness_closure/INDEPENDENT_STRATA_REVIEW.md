# Non-author internal review of the fifth-pass LY4 strata

Date: 2026-09-08 UTC. Reviewer: coordinator, who did not author the reviewed
stratum package. The author is the separate `lyness_round5` agent. This is
current-team AI-assisted internal review, not human peer review, external
model review, or a priority certificate. The repository batch workflow's
current-team rule replaces the selected research-review skill's historical
GPT-5.4/MCP default. No external model call, thread ID or venue score is invented.

## Exact reviewed artifact and scope

The reviewer read all **481 lines** of [PROOF_PACKAGE.md](PROOF_PACKAGE.md),
in two consecutive reads covering lines 1–240 and 241–EOF.
SHA-256 at review:
`f6f00908b8ade99a08806ebe37744ed89acc3fc02bb1ab92733361d3c64aab10`.

The fourth-pass integrality and $a\ne1$ stratum meeting $-1$ are inherited
dependencies with their existing independent review. They were not rerun.
The present review checks the new complete small-period strata, the entire
$a=1$ integral atlas, and the eight-period exclusion. The coordinator's
separate rational-period bound is not reviewed by its own author here.

## Findings: no mandatory correction within the proved strata

### R1. Complete periods dividing six

The opposite-index equations give the three linear differences and the
parameterization $(p,q,r,p+t,q-t,r+t)$. Subtraction gives exactly the three
products in (6). The split $p=r$ versus $p\ne r$ and the two branches of
the second product cover all solutions; both nontrivial branches really are
rotations of $W(r,s)$. The displayed substitutions prove sufficiency, and
the exclusions $r,s\notin\{0,-1\}$ are precisely the nonzero-coordinate
conditions. The least-period labels at $s=r$ and $s=-r-1$ were checked and
cannot coincide for an integer parameter. No reversal quotient was used.

### R2. Unique five-cycle

The propagation of $-1$ and coprimality of four/five correctly exclude that
locus. The constant two-integral gives the stated scaled second-order
recurrence. I independently expanded its fifth-step numerator by hand:
after subtracting the initial coordinate, the residual is
$(c-1)[w^2+(c-1)w-cv-c]$, with the displayed outside factor and denominator.
The denominator factors are nonzero on the ordinary orbit. Applying the
identity to the reversed sequence is legitimate because the second-order
equation is symmetric in its outside indices. It forces period dividing two
unless $c=1$. The sign and product arguments then force positive transformed
integers and a coordinate one; the remaining divisor choices are exactly
$b=1,2$. The resulting original word has parameter 13 at every position.

### R3. Exceptional parameter $a=1$

The four-step identity divides only by nonzero original coordinates. It
proves the eight-step law even when a plus-factor is zero, which is important
for the exceptional stratum. The block split for the $-1$ locus treats the
$b_j=-1$ case separately and does not cancel a zero plus-factor. Nonzero-domain
restrictions and the period-four overlap at $b=-1$ in the eight-word were checked.

Off that locus the six-step sign law combined with the eight-step identity
really gives parity-constant signs. Both-negative and mixed-parity-negative
patterns are excluded by the displayed recurrence and strict cyclic increase,
respectively. The only period-at-most-two ordinary integer orbit is $(2,3)$.

For longer positive orbits, formula (16) reconstructs all odd terms. The two
displayed parity identities prove sufficiency for all eight positions. Choosing
the smaller members of the two opposite divisor pairs gives adjacent entries
in the cyclic even list, so the $K\le9$ bound in the no-coordinate-one case
is valid. Both divisor tables were checked by hand. In particular the
$K=9,q=3$ word is $(1,1,3,5,9,5,3,1)$, a rotation of the listed $K=5$
orbit; it is neither an omission nor a fifth positive orbit. The four distinct
listed multisets and their singleton entries justify distinctness and least
period eight.

### R4. No genuine eight-cycle at $a\ne1$

The even-subsequence identity (18) follows by the stated substitution and
does not divide by an excluded zero. Equating opposite products in a
four-periodic even list forces both opposite pairs equal because
$u(a-1)\ne0$. Reconstruction makes the odd entries constant, and the
earlier no-$-1$ four-period argument then forces period dividing two.
The separate $-1$ locus supplies the remaining case. This exclusion is not
an exclusion of arbitrary larger periods.

## Original-contract and source adjudication

The full LY4 contract remains **NOT CURRENTLY JUSTIFIED**. Lemma E is stated
precisely and is not hidden behind the proved strata. A coarse rational-period
bound, even if independently accepted, would leave higher-period integral
torsion strata to solve. The period-six sign law alone is not a period-six
law for the numerical coordinates.

The [coordinator source audit](../lyness_sources/SOURCE_AUDIT.md) records the
classical recurrence, two-integrals, QRT reduction and order-eight phenomenon.
This review makes no global ownership claim for the new elementary exhaustion
of the specified strata. Complete auxiliary results do not close the full
question, and this package is **not admitted as an independent slot**.

## Outcome and execution boundary

`PASS_AUXILIARY_STRATA; FULL_LY4_UNCLOSED; ZERO_ADMISSION`.
No mandatory issue was found in the reviewed proof scope; no author revision
or additional mathematical execution was necessary. This was a full textual
proof review plus independent hand algebra/divisor checks, not a program run,
finite census, source-system certification or target-arithmetic evaluation.
The old alphabet computation and IR1 were not rerun. The remaining task is
the original exhaustive period lemma, not additional repeats of these checks.
