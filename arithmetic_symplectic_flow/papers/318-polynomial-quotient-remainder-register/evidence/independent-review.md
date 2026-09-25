# Independent internal review — quotient/remainder register

Candidate: `ANG-20260920-PQR01`.
Package: `318-polynomial-quotient-remainder-register`.
Status: `OWNED REGISTER CLOCK; ONE/TWO-STEP RETURNS ABSENT — STOP / FORK`.
Calibration: `NOT_CALIBRATED`; internal AI review, not external peer review.

## 1. Exact inputs and actual review chronology

The original frozen card was read completely through its original EOF,
164 lines, with measured SHA-256:

`ab764785594498f289f04c026d3ee38de66a1ba3a6585236f8fe41389d4ce099`.

The same first-164-line prefix was rechecked after the author appended
an outcome. No appended outcome, scout, ledger, companion record, historical
research file or peer answer was read for this audit.

The manuscript versions and their distinct provenance are:

| Version | SHA-256 | Actual review access |
| --- | --- | --- |
| Author's first 331-line draft | `071663ac6be658a63e9734243fafbf979cd201347dd3175c53549c682ea3c34b` | Author-reported only; not read by this reviewer |
| Released 353-line manuscript | `b882c0576887515cd7ff8a4676e0a78fffd8187920b8e2d17bdb7456933d83d2` | Hash measured; all 353 lines read after explicit unlock |
| Final 356-line manuscript | `164b06bdaf48aa462f207d764f34639502fcccf124498bf9614b8e255b95f123` | Hash and line count measured; changed sections read back |

Actual order: full original card and required ARS instructions; independent
main proof; first raw message; all three controls and terminal-basin
proofs; complete raw checkpoint-1 commitment; author's explicit manuscript
unlock; full 353-line comparison; two bounded scope findings; author's
revision; targeted final readback and checkpoint 3; this report.

The author reports that the first draft was locked before my first
raw message. After the complete raw submission, the author adopted my
DIVISOR-CONSTANT-OFF cycle-product argument and terminal-basin/phase paragraph,
producing the released 353-line version. That manuscript was therefore
raw-influenced, not a blind draft. Its later unit-boundary example and
scope wording were added after checkpoint 2 as documented below.
The unread first version is not retrospectively treated as inspected evidence.

The ARS router, deep-research workflow, Devil's Advocate role, runtime policy
and logical-fallacy reference were read for the three-checkpoint method;
the interrupted router display was recovered with an overlapping read.
No issue quota, model override or external-dispatch instruction enlarged
the task. No auxiliary agent was delegated or consulted. This reviewer
inherits the same model/runtime and substantial historical context: raw-before-
manuscript access does not establish ideation blindness, cross-model verification
or independent error probabilities. No venue calibration was supplied.
Only this report is reviewer-written; the manuscript remains author-owned.

## 2. Checkpoint 1 — independent original-card audit

### Full source, exact inverses and IMAGE

For every legal current cell, polynomial division over the real
coefficients gives exactly

    x*xi+y=(x/b)*(b*xi+1)+(y-x/b),  b!=0.

The remainder is a constant polynomial, without an integer-remainder interval
restriction. The permission is genuine current signed integer divisibility;
it does not say that the real quotient is necessarily an integer.
The stated integer-seed divisor interface follows directly, without importing
an earlier clock or return theorem. Stronger naturalness remains open.

For a target `(s,t)`, the only possible source branch is
`B=floor(s+t)`. If `B!=0` and `B|floor(B*t)`, the unique
predecessor is `(B*t,s+t)`; otherwise none exists. The cellwise
inverse and the target floor recover both source indices uniquely.
Thus the main source is a partial Borel bijection from its
legal domain to its exact image, not a bijection on all of `Y`.

Lack of incoming history is distinct from terminality. My raw example
was `(-1,1)`: it has no predecessor but a legal next step.
Conversely `(1,0)` is terminal yet has predecessor `(0,1)`.
Every terminal object and actual incoming history remains; no terminal
step is fabricated from its length-zero identity.

The inverse derivative is `[[0,b],[1,1]]`, of determinant `-b`.
Consequently `J=|b|` is the actual IMAGE density on every Borel
subset of the branch's full domain. This is not a whole-cell
mass ratio. Its analytic determinant supplies the frozen all-point version
on retained cuts, not uniqueness from an a.e. density class.
The legal-source clock is `kappa=-log|b|`, including negative branches.

For legal histories let `D_k(z)=product_{i<k}|b(T^i z)|`,
with `D_0=1`. The source-to-range branch-pair IMAGE and clock are

    J(z,k-l,w)=D_k(z)/D_l(w),
    c(z,k-l,w)=-log D_k(z)+log D_l(w).

The actual forward arrow has lag `-1` and clock `+log|b|`.
Longer presentations of the same lag append a common legal future
and cancel. For composition, the two middle histories align at their
maximum available length. These arguments never evaluate a nonexistent
terminal step. Only actual retained-lag triples are arrows, not words,
arbitrary affine maps or additional branch multiplicities. The extension
and quotient remain Borel/set-level; no etale or invariant-measure assertion
is inferred from branchwise change of variables.

### Complete one/two-step test and the conditional higher-period rule

Fixedness gives `x/b=y` and `x=y-x/b=0`, hence `y=0`.
That point has `b=0` and is terminal. Thus there are no
legal fixed points, including on axes and cuts.

For a legal two-step return, put `q=x/b` and `d=floor(q)`.
Both divisors must be nonzero. The return equations imply

    x=-d*y, q=(1-d)*y, x=b*q,
    (b-1)*(d-1)=1.

Since `b!=0` implies `y!=0`, there is no lost zero case.
The integer solutions are `(b,d)=(2,2)` or `(0,0)`.
The latter is illegal. The former requires `q=-y`, while both
floors would be 2, which is impossible. This excludes every
full-real one/two-step return without a positivity restriction or cutoff.

It does not exclude higher periods. At any actual least-period-`P`
cycle, `N=product|b_i|` is a positive integer and the full
source isotropy is `P Z`. Its entire time image is zero
if `N=1`, with extension kernel `P Z`; if `N>=2`,
the time image is `log(N) Z` and the extension kernel is
trivial. The positive primitive, when present, is `log N`, and
its positive multiples are repetitions of the same packet. This
formula alone establishes neither occurrence nor exclusion of prime or
composite products. Main higher-period existence and multiplicity remain OPEN.

Partial injectivity also proves that a periodic core has no external
finite incoming tail: its cycle predecessor is already its unique
predecessor. Its full source class is exactly that cycle. Distinct
cycles cannot merge by equal labels, products or times.

For a terminal anchor `omega`, all incoming states are its unique
partial inverse iterated for every legal finite depth, with no cutoff.
If `d_z` is stopping depth and `S_z` its kappa prefix,
the only basin lag is `d_z-d_w`, its clock is `S_z-S_w`,
and the full height invariant is `h-S_z`. Source isotropy,
time image and extension kernel are all zero. These formulas do
not add absorbing loops or remove terminal incoming histories.

### Three separately owned controls

DIVISIBILITY-OFF has exact image `floor(s+t)!=0`, unique inverse
`(B*t,s+t)`, and its own inverse determinant `-B`.
There is no hidden integer-divisibility filter. Its clock and finite
branch composition follow from these actual domains. The preceding
one/two-step algebra uses only nonzero divisors and current floor
membership, so proves the complete short-return obstruction for this
control too. Higher cycles and their products remain unresolved.

DIVISIBILITY-SHIFT has exact image

    B=floor(s+t)!=0,  B|(floor(B*t)+1),

and the same unique inverse formula on that different domain.
Its own IMAGE is `|B|` and source kappa is `-log|b|`.
The same permission-independent equations exclude all of its one/two-step
returns. No main orbit or higher-period conclusion is transferred.

I explicitly checked the signed half-open filters in the raw audit.
For main positive `b`, quotient targets have `t in [k,k+1/b)`;
for `b=-m`, they have `t in (k-1/m,k]`. For SHIFT,
these become `[k-1/b,k)` and `(k,k+1/m]`, respectively.
The manuscript's exact floor tests already retain these endpoints and
need not reproduce these supplementary interval expressions.

DIVISOR-CONSTANT-OFF is genuinely the changed source `T_0=(y,x/b)`.
Its target branch is uniquely `B=floor(s)`, with image condition
`B!=0` and `B|floor(B*t)`, inverse `(B*t,s)`, determinant
`-B` and own kappa `-log|b|`. Main inverse domains cannot
be reused without replacing the target-floor coordinate.

All its fixed points are exactly `(u,u)` for `1<=u<2`.
For a two-step return the equations are `x/b=x`, `y/d=y`.
Since `y!=0`, first `d=1`; then `x/b in [1,2)` is
nonzero, so `b=1`. Hence its complete two-step locus is
`Q=[1,2)^2`, where the source swaps coordinates. The diagonal
has least period 1, and off-diagonal unordered pairs least period 2.

The unique inverse also swaps inside Q, so the complete basins
are precisely these singleton or two-point cores, without omitted tails.
Their kappa is zero, H is zero, source/extension isotropy is
`Z` or `2Z`, and phase is the full real height `h`.
Different unordered pairs are not identified by their equal zero clock.
They are not positive primitive time orbits.

The raw audit additionally supplied the short identity

    |x_(i+1)*y_(i+1)|=|x_i*y_i|/|b_i|.

On any actual `T_0` cycle both coordinates are nonzero. Multiplying
over that cycle forces `product|b_i|=1`. Therefore every actual
periodic core of this control has zero H; nonperiodic points also
have zero time image. This proves global zero return-time groups
without a full source-cycle classification, without asserting that every
step clock is zero, and without applying a logarithm to zero.
This control-only conclusion does not apply to the main source.

## 3. Checkpoint 2 — manuscript comparison and resolved findings

The complete 353-line manuscript was checked against the raw derivations.
The polynomial identity, exact domains, partial injectivity, all-Borel IMAGE,
absolute determinant, forward/inverse clock signs, partial-history alignment
and complete short-return equations agree. The manuscript's distinct no-
predecessor example `(1,-1)` was directly substituted: its source branch
is `-1`, its outgoing value is `(0,-1)`, and its incoming
test has `floor(s+t)=0`. The example is correct.

The conditional phase formula was also checked. With `z_j=T^j z_0`
and kappa prefix `S_j`, the arrow from `z_0` to `z_j`
has clock `-S_j`; therefore `h+S_j` modulo `log N` is
the correct cycle phase. For `N=1`, every absolute branch factor
is one, so this reduces to `h`. The terminal formula
uses the opposite entry-to-anchor orientation and correctly gives `h-S_z`.

The author-integrated raw additions, namely the terminal-basin paragraph and
the control cycle-product proof, were checked in their manuscript form.
Their legal-history and nonzero-coordinate hypotheses are explicit and sufficient.

Two nonblocking scope corrections were requested and accepted:

1. During manuscript-stage unit-boundary checking, I explicitly verified
   the exact control cycle `(1,-1)->(-1,-1)->(-1,1)->(1,-1)`.
   Its three points are distinct, its branch divisors are `-1,-1,1`,
   and all permissions hold. Thus the earlier sentence leaving
   higher control-cycle *existence* unclassified was unnecessarily broad.
   The final manuscript retains this single period-three boundary example
   and leaves the complete higher source classification unclassified.
   This explicitly verified example was not submitted in checkpoint-1
   raw results and is not retroactively attributed to that checkpoint.
2. The conclusion's phrase “not an all-period theorem” was narrowed
   to “not a complete all-period source classification,” avoiding a
   literal denial of the control's proved all-period time result.

These are precision/completeness changes, not changed definitions, new search
campaigns or alterations to the main stop conclusion. No other main
return or higher-period census was pursued. The final 356-line version's
changed passages were read back with the actual final hash; both
findings are closed. Unchanged proofs were not needlessly rerun.

## 4. Checkpoint 3 — strongest counterarguments and final standing

The strongest limitation is that absence of source periods 1 and 2
does not refute higher positive prime packets. The main conditional
integer-product clock also does not do so. The final manuscript
properly retains this OPEN scope and treats STOP / FORK as
the precommitted bounded decision, not a global impossibility theorem.

Other adverse checks retained the complete owner:

- Terminal identities cannot create fixed or periodic source points.
  All real terminal states and all legal incoming histories remain.
- The negative divisor sign must be removed only inside the absolute
  Jacobian, not by deleting negative branches. The paper does this.
- All-point endpoint clocks are a frozen version choice; a.e. IMAGE
  does not force those null values. No atomic replacement is used.
- Equal times, products or phase labels cannot merge distinct source
  cycles. Injectivity proves absence of external cycle tails rather than
  assuming a preferred section or erasing possible predecessors.
- The changed-permission controls show that the short-return obstruction
  does not need divisibility. This does not erase the main source's
  actual arithmetic permission or prove it irrelevant at every period.
- The divisor-constant control's global zero H, its continuum of
  short zero-time cores and its retained boundary three-cycle are
  control results only, not main source returns or a main no-go.

No further correction is requested. The final binding above has no
unresolved blocking or nonblocking reviewer finding. The original card and
same-object ledger remain intact. Established results are exact source and
clock ownership, the full main one/two-step exclusion, complete specified
control short-return loci and the control-only all-period zero-time result.
Main higher periods, prime/composite selectivity, multiplicity and stronger
naturalness remain OPEN; the full higher source-cycle census was not done.

No embedded circle, Hausdorff quotient, etale flow, invariant product measure,
classical symplectic realization, operator, trace, zeta, RH or Hilbert--Polya
claim follows. T3 is not supplied/pursued; classical A0/A1/A2 are not
applicable; formal Route coordinates are unassigned and Route B is not
invoked. No external lookup, scientific numerical run, auxiliary review or
cross-model call occurred. This is evidence-backed internal model review,
not an external peer-review or independent-error certificate.

Companion links, registration files and appended administrative outcomes were
outside the permitted read scope and remain the author's integration QA.
