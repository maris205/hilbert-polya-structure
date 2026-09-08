# Round 4 DH1/DH2: bounded non-author proof review

Date: 2026-09-08 UTC. Reviewer: current-team agent
`/root/scout_charp_c414`, not the author of the two reviewed proofs.
This is AI-assisted internal cross-review, not human peer review, an
external referee certificate, evidence of independent model errors, a
priority determination, or a formal Route A evaluation.

## Outcome and actual scope

**Both frozen mathematical claims are PROVED AS STATED by the elementary
arguments in Sections 1 and 2. No must-fix mathematical issue was found.**
No additional assumptions, period cutoff, parameter cutoff, selected
subsequence, or clock change are required. This does **not** admit either
candidate as a substantial independent paper. The author's separate
no-admission disposition is consistent with the short residual proofs.

The reviewer actually read, in full:

| Artifact | Actual coverage | SHA256 at review |
| --- | --- | --- |
| [COMPLETE_SHORT_PROOFS.md](COMPLETE_SHORT_PROOFS.md) | Lines 1–390 after D1 closure: initial full read plus targeted supplemental read of current lines 300–390; includes all five lemmas, both classifications/limits, the source cross-check, and the scope/target disclaimers | `ed5b16b86d5bece35da20c0953f779809570f71d2ce12b32b0a35deb6a0da9a0` |
| [FROZEN_CONTRACTS.md](FROZEN_CONTRACTS.md) | Lines 1–145, including the exact domains, native clocks, observables, and mathematical-versus-substantial success gates | `e996c1e2a2c96023f9679126d9b27a104944ff22eee10c8cb836908bc8164da4` |

The hashes identify the local text checked, not a signature or a proof of
mathematical correctness. The reviewer also read the repository guidance
and the relevant current-state entry. No author proof, source audit, scout
report, global state, manuscript, or historical package was modified.
This report is the sole new file written by this review.

The reviewer did not run or import a mathematical script, perform a
numerical census, search new literature, reopen a primary paper, or check
the author's external source-access receipts. Section 3 was read as part
of the submitted proof, but its quoted external theorem statements and
publication/version claims were **not independently source-verified here**.
The judgments below therefore do not recertify that separate source audit.

Review method: the scoped `research-review` workflow, with `proof-writer`
claim/assumption/quantifier checks. These skills led to the explicit
dependency separation and evidence-anchored report, not a five-seat
simulated panel, external upload, or manuscript revision.

Calibration status: `NOT_CALIBRATED`.

`criteria_binding_unavailable`

No venue-alignment, numerical quality score, or acceptance probability is
asserted. Confidence in the two elementary proof checks: 5/5, based on
direct verification of their finite algebraic and limiting steps; this
is a scope disclosure, not a calibrated reliability measure.

## Exact claims and criterion-bound judgments

DH1 fixes every integer $c$, the map
$H_c(x,y)=(y,y^2+c-2x)$ on all $\mathbb Q^2$, and ordinary forward least
periods. DH2 fixes $c=0$, $P=(0,1)$, and
$D_n=\gcd(|u_n|,|u_{n+1}-1|)$ at every native time $n\geq1$.

| Criterion | Source of criterion | Judgment | Evidence anchor | Reason and scope limit | Decision bearing |
| --- | --- | --- | --- | --- | --- |
| DH1 all-rational, all-parameter necessity and sufficiency | Frozen DH1 contract, lines 24–66 | MEETS | equation: proof Section 1, (1)–(2) and both discriminants | Every rational periodic point is integral; the entire periodic locus injects modulo two; both parameter lists have verified converses | Yes: supports DH1 PROVED |
| DH2 unconditional full-time limit | Frozen DH2 contract, lines 68–126 | MEETS | equation: proof Section 2, (4)–(7) | Parity licenses the inverse modulus; escape licenses a nonzero divisor bound; the order of limits is valid | Yes: supports DH2 PROVED |
| Assumptions, bad prime, and native clock | Frozen contracts, lines 8–11, 36–39, 86–93 | MEETS | equation: proof Lemmas 1, 4, 5 | Integrality includes two; every return gcd is odd; backward comparison does not replace the forward observable | Yes: excludes hidden restrictions |
| Elementary-proof dependency separation | Proof dependency map, lines 26–37 | MEETS | text: proof lines 360–361, "It would remain a complete proof if this cross-check were removed." | Sections 1–2 do not use density, dynamical Mordell–Lang, or a gcd-height theorem | Yes: source-cross-check uncertainty does not create a gap in those proofs |
| Independent substantive increment | Frozen contracts, lines 50–66 and 101–126 | DOES_NOT_MEET | equation: proof Sections 1–2, contraction argument and (6)–(7) | After the classical local/modular tools are deducted, each residual argument is short; this is a bounded internal gate judgment, not a universal publication verdict | Yes: no new admission |
| External-source accuracy, priority, and completeness | Explicit bounded review assignment | NOT_ASSESSED | — | No primary sources or source-access receipts were reopened in this review | No: separate source audit remains the source authority |

The categorical judgments are not averaged or converted into a score.

## Detailed verification: DH1

### 1. Integrality covers the whole rational domain

For a periodic coordinate sequence and any prime $p$, let
$m=\min_i v_p(a_i)$. If a negative minimum exists, the left side of
$a_i^2=a_{i+1}+2a_{i-1}-c$ has valuation $2m$, while the right side
has valuation at least $m$, since $c$ is integral and $v_p(2)\geq0$.
The contradiction includes $p=2$. If all coordinates are zero, they
are already integral; zero coordinates otherwise cause no problem under
the convention $v_p(0)=+\infty$. No invertibility modulo two is assumed.

### 2. Precision gain and global periodic injectivity are valid

For points congruent modulo $2^r$ with $r\geq1$, the one-step coordinate
differences have valuations at least $r$ and $r+1$: the factor $y+y'$
is even. At the second step, both differences have valuation at least
$r+1$. Repeating this establishes precisely the stated congruence gain.

An even common multiple $N$ of two periods makes both points fixed by
every $H_c^{jN}$. Their original difference is then divisible by
$2^{1+jN/2}$ for every $j$. This forces equality and proves injectivity
on **all** periodic points with a given residue, not only uniqueness of
a putative lift constructed in advance.

### 3. The residue classification controls the native period exactly

The reduced map is $(x,y)\mapsto(y,y+\bar c)$. For even $c$ its only
periodic states are the two diagonal fixed points; for odd $c$ they are
the anti-diagonal two-cycle. If an integral periodic point has residue
period $m$, it and its $m$th forward iterate are periodic with the same
residue, so they coincide by injectivity. Reduction also implies that
$m$ divides the upstairs period. Thus the least periods agree, excluding
every rational period greater than two.

### 4. Both parameter rows and every exceptional case are complete

The fixed-point equation $t^2-3t+c=0$ has integral roots exactly when
$9-4c=(2k+1)^2$, $k\geq0$. This gives
$c=2-k(k+1)$ and the distinct points $(1-k,1-k)$ and $(2+k,2+k)$.

For a genuine two-cycle, subtraction gives $x+y=-3$, and the remaining
equation is $x^2+3x+c+9=0$. Its discriminant condition is
$-4c-27=(2k+1)^2$, giving $c=-7-k(k+1)$ and the two displayed exchanged
points. They cannot coincide for integral $k\geq0$. Substitution proves
sufficiency, including $k=0$ in both rows. The parameter sets are
disjoint by parity, and $k(k+1)$ is strictly increasing on
$\mathbb Z_{\geq0}$. The empty row therefore accounts for every other
integer parameter. There is no missing bounded-height exception.

## Detailed verification: DH2

### 5. Positivity, nonperiodicity, and the growth constant are proved

The listed seven initial values follow directly from the recurrence.
Modulo two, $u_{j+2}\equiv u_{j+1}$, so every $u_j$ with $j\geq1$ is
odd and nonzero. Thus each $D_n$ is positive and odd. No later point
can equal $P$, and invertibility over $\mathbb Q$ turns any repetition
into such a return. This establishes nonperiodicity without numerical
escape evidence.

Starting from $u_6=11\geq2u_5$, the induction
$u_{j+1}\geq u_j^2-u_j\geq u_j^2/2\geq2u_j$ and the upper bound
$u_{j+1}\leq u_j^2$ have the correct directions and positive inputs.
Iteration gives (5). In particular,
$\log u_j\leq C2^j$ with the single constant
$C=2^{-6}\log11$, independent of every later backward shift $k$.
The lower bound proves $u_j\to+\infty$.

### 6. The inverse-modulus step is legitimate at every return prime

For fixed $k\geq1$, $H^{-k}$ is a polynomial over $\mathbb Z[1/2]$.
Since $D_n$ is odd, reduction of this ring modulo $D_n$ is defined.
Applying that polynomial to $H^n(P)\equiv P$ and using $n\geq k$
gives $D_n\mid A_k u_{n-k}-B_k$ in $\mathbb Z$, with $A_k$ a positive
power of two. This is not an unjustified use of inverse good reduction
at the bad prime. The trivial modulus $D_n=1$ is harmless.

For fixed $k$, escape makes $A_k u_{n-k}-B_k$ nonzero for all sufficiently
large $n$. Hence the divisibility does imply the absolute-value bound
in the proof. Its threshold may depend on $k$; no uniform threshold is
needed. The inequality using $A_k+|B_k|$ is valid since eventually
$u_{n-k}\geq1$.

### 7. The two limits prove the full original claim

For every fixed $k$, inequality (7) holds for all sufficiently large
$n$ and yields

$$
0\leq\liminf_{n\to\infty}2^{-n}\log D_n
\leq\limsup_{n\to\infty}2^{-n}\log D_n\leq C2^{-k}.
$$

The final term involving $A_k,B_k$ vanishes because $k$ is first held
fixed while $n\to\infty$. Since the resulting bound holds for every integer $k$,
letting $k\to\infty$ makes the limsup zero. This establishes the limit
along **all** native times. There is no exchange of limits and no need
to bound the rate at which the backward denominators grow.

## Jacobian, dynamical degrees, and source-dependency boundary

Direct differentiation gives

$$
DH_c(x,y)=\begin{pmatrix}0&1\\-2&2y\end{pmatrix},
\qquad \det DH_c=2.
$$

The forward map therefore expands real area. The inherited directory
name is not a dissipativity claim, and the inverse determinant $1/2$
does not change the frozen forward clock. The stated $d_1=2$ follows
from the monic degree-$2^n$ second coordinate; the birational topological
degree, hence $d_2$, is $1$, not the Jacobian determinant $2$.

The reviewer also checked the elementary geometry used in Section 3:
the displayed projective extension, affine inverse, reduced affine point
target, and height growth are consistent. Since the inverse iterates
are morphisms on the affine target, their graphs are closed there;
the projective graph closure restricted over that target cannot add
extra sources. This supports the map-specific graph observation.

The applications of the quoted Matsuzawa and Bell–Ghioca–Tucker results,
and the publication/version discussion, remain external-source assertions
outside this review's primary-source verification scope. Their correctness
is not required for the two elementary proofs: deleting all of Section 3,
including its density/genericity and height-ratio route, leaves (1)–(7)
and both conclusions intact. No source cross-check is being counted as
an additional independent mathematical result.

## Strengths, weaknesses, and disposition

### S1. DH1 closes necessity and sufficiency with no census cutoff

Evidence Anchor: equation: proof Section 1, (1)–(2), followed by the
fixed-point and two-cycle discriminant equations.

The global periodic-point injection is the key step that makes the
low-period table an exhaustive theorem on $\mathbb Q^2$.

### S2. DH2 makes both fragile arithmetic steps explicit

Evidence Anchor: equation: proof Section 2, (6)–(7).

The author explicitly excludes the bad prime from each modulus and
states the fixed-$k$ order of limits. Neither is supplied by experiments.

### Weaknesses and coverage receipt

No must-fix mathematical weakness was found in the two frozen elementary
claims. No repair or weakening is requested. This is not a claim that
unreviewed external-source statements have been certified.

| Dimension examined | Actual check | Basis for no mathematical weakness found |
| --- | --- | --- |
| Domain and parameter exhaustiveness | All primes in Lemma 1; both residue cycles; both discriminants and converses | No rational or integer-parameter cases are excluded without proof |
| Native periods | Congruence improvement for any shared residue and an even common multiple of periods | The reduction argument proves exact upstairs periods, not merely divisibility in the wrong direction |
| Bad-prime control and gcd positivity | Oddness at every $n\geq1$ and ring reduction of the polynomial inverse | Each inverse-modulus step is defined; the zero-gcd case cannot arise |
| Growth and quantifiers | Explicit escape, constant $C$, eventual nonzero divisor, fixed-$k$ limsup bound | Every bound is available for the needed tail and the final limit follows without uniform-in-$k$ assumptions |
| Definitions and dependency map | Jacobian versus $d_2$; removal of all Section 3 dependencies | No determinant/degree conflation or hidden sourced theorem enters Sections 1–2 |

There are no unanswered author questions needed to close these two
mathematical claims. No additional computation, parameter change,
literature program, or manuscript is requested by this review.

**Final disposition:** DH1 `PROVED`; DH2 `PROVED`; `NO_NEW_ADMISSION`.
The elementary closures and their short-proof provenance are worth
preserving, but they do not supply the missing substantial contracts.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unchanged: no target Euler factors,
root numbers, automorphy, target zeros, or Hilbert–Pólya realization follow.

## D1 directed documentation closure

On 2026-09-08 UTC, the documentation reviewer identified a mismatch
between the reported 382-line proof extent and the current file's
390 lines. A read-only `wc -l` check confirmed 390 proof lines and
145 frozen-contract lines. Both current SHA256 values equal the values
already recorded above. The earlier 382-line extent was inaccurate for
that recorded proof hash; it has been corrected rather than treated as
evidence of a different mathematical input.

The reviewer supplementally read current proof lines 300–390, including
the entire current Section 3, the codimension-power inequality, and the
Section 4 clarification that the displayed return gcd targets the point
$(0,1)$, not a diagonal subvariety. The dependency-separation quotation
was relocated to its actual current lines 360–361. All other explicit
line anchors in this report concern the unchanged early dependency map
or the 145-line frozen contract and required no relocation.

This was a directed range/anchor and tail-reading closure, not a second
full mathematical review, a new source verification, or a mathematical
program run. Only this review report was edited. The previous mathematical
verdicts, no-admission disposition, and primary-source verification limits
are unchanged. D1 is closed.
