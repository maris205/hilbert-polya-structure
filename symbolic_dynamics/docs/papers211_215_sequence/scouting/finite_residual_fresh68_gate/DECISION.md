# Fresh68 A — independent candidate gate

2026-09-11 UTC. Reviewer: `/root/p213_manuscript_review_a`.

**GO_NARROW, candidate mathematics only.** The literal prefix-drawdown map
and its author-proved exact pointwise extinction clock survive this bounded
independent gate. The every-target record-height reconstruction supplies a
separate inverse axis; its subsequent barrier enumeration receives no new
mechanism credit. This is not a manuscript review, admission, paper number,
global novelty certificate or authorization to execute anything. Root must
receive this gate before taking the next lifecycle step. `HOLD_EXTERNAL`.

I had no authorship of A's map, proofs or verifier before this assignment.
I have not supplied a replacement proof or new theorem to the author. This
report checks the complete existing DESK proof and its subtraction boundary.
Prior P212/P213 review roles and familiarity with other finite-map scouts
make this process-separated, not blind or external specialist review.
No scientific program, import, pilot, build, host probe, child agent, central
edit or Git action occurred. Only this gate directory is written.

## Accepted scope and mathematical attacks

The checked input is the complete author `finite_residual_fresh68/DESK.md`,
SHA256 `14e7112b4b61d86534fe9c70db73d60798134dc63d9c76e756132bd8e03d11e9`.
B is not a candidate in this gate. On the labelled, ordered carrier
`{0,...,q}^n`, A is exactly

\[
 F(x)_i=\max_{j\le i}x_j-x_i.
\]

There is no sorting, circular boundary, extra threshold or outside driving
word. The nonnegative bounded carrier is closed. With an initial coordinate
zero, let R be the number of maximal sign blocks in the nonzero consecutive
differences. These are the checked conclusions, with no open mathematical
finding:

- For every nonzero x, `R(Fx)=R(x)-1`; zero is the sole recurrent state and
  the pointwise entrance time is exactly R(x).
- For n,q positive the height is n, attained exactly when all n initial-zero
  differences are nonzero and alternate signs. For n=0 or q=0 the height is 0.
- Every target starting with zero has the full record-height inverse
  described below; all other targets have no source. The image cardinality
  for n positive is `(q+1)^(n-1)`.
- The displayed first-violation binomial recurrence evaluates every fibre.
  For positive n,q the unique maximum is the zero target, with
  `binom(q+n,n)` sources. Singleton boundaries have fibre size 1.

**Clock proof attack.** The author identity
`y_i=max(y_(i-1)-(x_i-x_(i-1)),0)` is exact, including a new record,
non-record increases, and equal coordinates. An input plateau leaves y
unchanged, so removing zero differences does not create a missing transition.
The first positive run starts at y=0 and produces no nonzero output
difference. Every negative input run strictly increases y. A later positive
run starts after such an increase, hence its first difference strictly
decreases y even when it immediately hits zero. Subsequent differences in
that run decrease or leave zero. Thus each later run contributes exactly
one nonempty opposite-sign run; adjacent surviving runs cannot merge.
The terminal run need not be completed or return to zero. These observations
verify precisely the author's deletion-and-sign-flip step, including the
most vulnerable saturation and plateau cases.

R=0 forces every original difference to vanish, not merely a constant
nonzero word: the first coordinate is compared with the adjoined zero.
Consequently the decrement proves the exact clock rather than just a bound.
The n-difference upper bound and its complete equality condition are valid;
the alternating q,0,q,0,... word attains n. When n=1 each positive input maps
directly to zero. Empty words and q=0 need and receive separate treatment.

**Inverse attack.** For an image target y, write its zero positions
`1=z_1<...<z_k`, with `z_(k+1)=n+1`. On the block from z_j to just before
z_(j+1), let b_j be the largest target coordinate. A source's prefix maximum
cannot increase at a positive target coordinate; its value is therefore a
constant L_j throughout that block. The necessary conditions are exactly
`0<=L_1<=...<=L_k<=q` and `L_j>=b_j`. Conversely the formula
`x_i=L_j-y_i` attains L_j at the initial zero of each block, never exceeds
it within the block, and reconstructs the genuine running maxima. No
strict record increase is required between consecutive zeros: equality of
adjacent L_j is allowed and introduces neither duplicates nor missing
sources. This verifies both directions and injectivity of the author map.

Replacing b_j by its prefix maximum B_j is equivalent under monotonicity of
L. Reverse-complementing gives `a_i=q-L_(k+1-i)` and the nondecreasing upper
barrier `c_i=q-B_(k+1-i)`. This is exactly the classical static counting
problem, not an independent new enumeration method.

**Recurrence attack.** For each m the unrestricted monotone sequences in
`[0,c_m]` number `binom(c_m+m,m)`. An invalid sequence has a unique first
violation i<m. Its prefix has A_(i-1) choices; its suffix has length m-i+1
and values in `[c_i+1,c_m]`, hence
`binom(c_m-c_i+m-i,m-i+1)` choices. Because the prefix ends at most at
c_(i-1)<=c_i, concatenation is automatically monotone. The first-violation
classes are disjoint and exhaustive. This verifies the author's A4 formula,
including i=1, repeated barriers, c_m=c_i (zero suffix choices), m=1, and
zero barriers. A_0=1 is the correct empty-prefix convention.

Choosing all L_j=q proves the entire claimed image, even when the target
reaches q. At zero there are n unrestricted weakly increasing heights.
Any nonzero image target has k<n and at most `binom(q+k,k)` sources;
for q>0 this is strictly smaller than the zero fibre. No equality case is
lost at n=1 or q=0. These are proof checks, not executed finite tests.

## Actual source and collision subtraction

The following are direct primary-source or original-local-text checks,
not deductions from an index summary. Local whole-file hashes are recorded
in INPUT_PINS.sha256; the stated reading ranges delimit actual evidence use.

1. Goldberg and Mahmoud, [Drawdown: From Practice to Theory and Back Again](https://arxiv.org/pdf/1404.7493),
   printed p. 5, Definition 2.2, directly defines running maximum minus the
   current value. I read that definition and its surrounding setup. The
   one-step statistic is fully owned background; this finite restriction
   is not a new statistic. That inspected passage does not state the
   autonomous whole-word sign-run extinction theorem. I do not claim to
   have read every page or to have excluded every result on drawdown.
2. Pemantle and Wilf, [Counting nondecreasing integer sequences that lie below a barrier](https://arxiv.org/pdf/0905.0609),
   printed pp. 1–5, definition, Theorems 1–2 and their combinatorial proofs.
   These were directly read. The transformed fibre-counting problem is
   exactly their problem. Their explicit recurrence is differently indexed
   and written than A4; A4 is checked above by its own first-violation
   argument, not falsely attributed verbatim. Evaluated barrier counting,
   multiset coefficients and the elementary extremum receive zero new
   mechanism credit.
3. P93 main.tex, lines 121–212: the literal is a composition of externally
   driven push/pop operators on infinite words. Its reflected-walk lengths
   M_n-S_n and running maximum normal form own the reflection primitive;
   they do not autonomously replace the whole driving word by its drawdown.
   The original S2 in STOCHASTIC_SCOUT.md, lines 213–290, likewise uses
   driven clipped nearest-neighbour maps and a range-passage clock. No
   transporting factor from either theorem to A was found or asserted.
4. P117 main.tex, lines 55–160: odd cyclic constant-run flips and parity
   boundary survival. A is neither this literal nor a full-carrier
   conjugate; the length-one old map already has a two-cycle. The proof
   mechanism is parity coalescence, not A's ordered sign-block update.
5. P132 main.tex, lines 53–143: thresholded prefix sums and its actual fixed
   language. It has n+1 fixed words, versus A's one. Its triangular-prefix
   amplifier is not an exact sign-run decrement theorem.
6. P138 main.tex, lines 101–173: the actual normalized quotient is
   `Q(y)_i=y_i XOR 1 XOR p_i(y)` with a palindromic-prefix test. For n=3 it
   sends every normalized word to zero. A sends 010 to 001, which needs
   another step. Thus neither equality nor a same-length surjective factor
   from that one-step quotient to normalized A can hold. The original
   P138 recurrent class is a two-cycle; full-carrier conjugacy is excluded.
7. P185 main.tex, lines 58–164: strict-prefix distinct-symbol count;
   on its first image the rule is `d'_i=d_(i-1)+1`. The first image and
   exact clock are not A's. At q=n-1, n>=3, the same full carrier has old
   height n-1 but A height n, excluding a conjugacy and a surjective
   old-to-A factor. This does not claim to exclude all changed-parameter
   encodings.
8. The complete root_zigzag/INTAKE.md defines reversal of greedy alternating
   permutation factors, not sign-run erasure. The original parkization
   PROOF_AND_SUBTRACTION.md, lines 1–110, defines first-deficient-rank
   decrease and invariant parking terminal words. Its monotone record
   coordinates are a useful subtraction warning, but no full dynamic
   conjugacy or transported clock to A is supplied by those formulas.
9. The complete parallel_run_erasure_lane/PROOF_AND_DISPOSITION.md deletes
   all long constant runs simultaneously and keeps singletons. It has a
   different carrier and many fixed words. That original explicitly does
   not prove a pointwise entrance formula. Generic deletion-clock language
   alone cannot consume A's precise pointwise statistic.
10. The UPC original SCOUT_REPORT.md and PROOF_BOUNDARIES.md lines 1–120
    were read, including the actual closure adapter and its proof of
    `F^4=F^2`. With fixed reachability, UPC uses `N(S)=Q\up(S)`.
    Binary A uses **`up(S)\S`** on the ordered coordinate chain, equivalently
    `(prefix OR x) XOR x`. These differences are not interchangeable:
    N(empty)=Q, while A(empty)=empty. Further, a surjective factor of a
    map satisfying `T^4=T^2` must satisfy the same identity. Binary A for
    n>=3 does not: an alternating word of length n has time n, so at n=3
    its second iterate is nonzero and fourth is zero. UPC therefore cannot
    supply A as such a factor or consume its arbitrary-height clock.

Targeted archive searches included prefix-OR, prefix-XOR, drawdown,
running maximum and run-erasure formulations in manuscript originals and
scout text. Web discovery included iterated drawdown, drawdown operator
iteration, running maximum/sign changes and prefix-OR/XOR dynamics. Hits
about stochastic stopping times, groundwater iteration, prefix computations
and neural circuit implementation do not state the autonomous clock; their
snippets are discovery leads, not supporting primary evidence. Broad search
displays were sometimes truncated; no completeness claim is based on them.
Both primary PDFs above were opened directly. No external PDF was locally
frozen, and URL citation is not a byte pin of its future content.

In particular, identifying the binary rule does not itself identify an old
owner of its clock. Nor does mapping every state to its now-proved R value
show an *old* transporting theorem: using that factor already requires the
rule-specific decrement being evaluated. Conversely this gate makes no
universal assertion that no relevant old factor exists. A later exact
owner/factor hit would reopen the scope.

## Residual value, limits and next gate

The surviving advance is modest but concrete: repeated whole-path drawdown
has an exact height for every labelled bounded word, determined solely by
its initial monotonicity sign blocks even with plateaus and partial returns.
This is stronger than the generic triangular nilpotence bound and is not
deducted by the actually inspected older maps. The full inverse is a
separate record-height reconstruction, not a consequence of the sign-block
clock. Classical barrier evaluation then completes the fibre atlas without
being promoted to a new counting theory. The resulting tightly scoped
theorem note meets the candidate-level two-mechanism requirement; it does
not warrant an inflated novelty or venue-impact claim.

Any subsequent contract should retain only these proved conclusions,
attribute the statistic and static enumeration, and state the bounded
source-search limitation. An exact binary owner transporting the general
clock, an error in the sign-block step, or a missing inverse source would
be material grounds to reopen. This gate does not propose additional
claims, a larger cutoff or experiments to manufacture another axis.
There has been no verifier or canonical output here. Actual source,
execution, canonical, manuscript, two-review, build and terminal gates
remain for root to commission under the project workflow.

The project skill and the research-review skill's local-review fallback
guided this source/proof-only scope; the requested no-extra-agent boundary
was retained. Initial combined context/search displays were truncated and
are not represented as complete reads; the complete author desk, selected
instructions, proof sections and cited primary passages were subsequently
read in bounded displays. Current state/index headers were used only for
lifecycle navigation, not as mathematical premises or stable input pins.

## Package roles

INPUT_PINS.sha256 is workspace-root-relative and pins the exact author,
contracts and local originals used above. Hashing a whole original does not
enlarge its stated reading range. SHA256SUMS is directory-relative and
covers this decision plus that input-pin file, excluding itself. Nothing
outside this gate directory is changed; no final paper manifest is claimed.
