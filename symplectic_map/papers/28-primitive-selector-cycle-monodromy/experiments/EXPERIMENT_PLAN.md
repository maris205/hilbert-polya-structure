# Paper 28 proof-only validation plan

Status: source-design author draft frozen for independent review  
Candidate: `primitive_selector_cycle_monodromy_v1`, controlling version V4  
Scientific execution budget: zero  
Empirical evidence supporting the headline: none

## Purpose

This project is a theorem paper.  Its headline must be established by exact
symbolic arguments, not by a search, numerical fit, computer algebra output,
or a finite collection of examples.  The word “experiment” in this file
means a predeclared adversarial check that can falsify a formula or expose a
missing hypothesis.  Passing such a check is never used to prove a universal
claim.

No script, notebook, CAS, solver, GPU job, parameter sweep, random test,
dataset, or generated certificate is authorized.  All checks below are
manual substitutions into displayed formulas.  Their public role is limited
to examples, counterexamples, and boundary illustrations.

## Frozen theorem under test

For every rooted primitive selector-pair word

\[
 \mathsf w=((a_0,b_0),\ldots,(a_{\ell-1},b_{\ell-1})),
 \qquad \ell\ge 3,
\]

the incidence construction gives one autonomous positive-support polynomial
symplectomorphism \(F_{\mathsf w}\) on \(2(\ell+1)\) coordinates.  It realizes
\(\mathsf w\) as a strict endogenous Newton-selector cycle, admits an exact
normal-fan feasibility iff, has a coefficient-uniform strict actual-degree
lift in the stated momentum chamber, has least selector and quotient periods
\(\ell\), and has a marked period monodromy that decodes the rooted
support-vector word.  Literal human labels require the labelled support
dictionary; without a marked root only the cyclic class is intrinsic.

The construction is one map per word.  It is not a universal map, a fixed-
dimension realization for arbitrary length, or one map per length.

## Registered exact fixture

The smallest nontrivial audit fixture uses

\[
 \ell=3,\quad r=4,\quad \rho=2,\quad K=1,\quad H=2,
\]

and the primitive word

\[
 ((A,X),(B,X),(A,Y)).
\]

Coordinates are \((0,1,2,\star)\), and

\[
 u_0=(2,1,1,1),\qquad D=\rho r+K\ell=11,
 \qquad \lambda=(D-1)^2=100.
\]

The literal incidence exponents are

\[
 \alpha_A=(3,2,3,3),\quad \alpha_B=(2,3,2,4),
\]

\[
 \beta_X=(2,2,3,4),\quad \beta_Y=(3,3,2,3).
\]

Every total is 11.  The common base score is
\(C_0=\rho(H+\ell)+K\ell=13\), the actual competitor gap is
\(g=K(H-1)=1\), and the affine forcing is

\[
 \mu=(D-1)(C_0+g)-C_0=127.
\]

The three selected digit vectors are

\[
 c_{A,X}=(28,18,27,26),\quad
 c_{B,X}=(18,28,17,36),\quad
 c_{A,Y}=(27,17,28,27).
\]

Every digit lies strictly between 0 and 100.  These values are a typeset
sanity fixture only; the general digit theorem is proved by inequalities.

## Adversarial check matrix

| ID | Exact check | Falsifying outcome | Proof obligation it audits |
|---|---|---|---|
| P28-X01 | Multiply the Jacobian blocks of the two gradient shears and the simultaneous permutation against the standard symplectic matrix. | Any nonsymmetric off-diagonal block or failure of \(J^{\mathsf T}\Omega J=\Omega\). | Polynomial symplecticity and inverse order. |
| P28-X02 | Differentiate one selected monomial row by row and derive \(A_\alpha=\mathbf1\alpha^{\mathsf T}-I\), then multiply \(B_\beta A_\alpha\). | A missing \(-I\), a transposition error, or any product other than \(I+\mathbf1((D-1)\alpha-\beta)^{\mathsf T}\). | Literal degree transport. |
| P28-X03 | At each phase substitute the spike vector into all incidence exponents. | Selected V score not \(C_0+g\), selected W score not \(C_0\), or an existing competitor not separated by exactly \(g\). | Arbitrary repeated-label realization. |
| P28-X04 | Repeat X03 when the V alphabet or W alphabet is a singleton. | A finite gap assigned to a nonexistent competitor, or a singleton normal cone not equal to the full positive weight space. | V4 empty-competitor convention. |
| P28-X05 | Use an arbitrary positive momentum seed \(m_0\) and compare it coordinatewise with \(A_{\alpha_{a_0}}u_0\). | Strict lift asserted outside \(0<m_0<A_{\alpha_{a_0}}u_0\), or \(m_0\le u_0\) called necessary. | V2 exact first-carry gate. |
| P28-X06 | Propagate source and target carries with \(r\ge2\) and every exponent coordinate at least two. | The dimension-one inequality is reused, or a later momentum condition is silently added. | Actual polynomial-degree lift. |
| P28-X07 | Expand \(Q_{s+1}=C_sQ_s\) with \(Q_s=P^s+\mathbf1R_s^{\mathsf T}\). | Wrong order of \(P^s\), \(c_s\), or \(\lambda\). | Ordered cocycle and monodromy. |
| P28-X08 | Bound every coordinate of \(c_{a,b}\) and compare two putatively equal pair digits. | A digit reaches 0 or \(\lambda\), or two distinct support pairs share a digit vector. | Carry-free base-\(\lambda\) decoding. |
| P28-X09 | Remove successively the marked root, the labelled dictionary, and the literal labels. | Rooted labels claimed from unmarked/unlabelled algebraic data. | Decoder side-information boundary. |
| P28-X10 | Compare \(P^du_0-u_0\) with the diagonal line for \(0<d<\ell\). | The fixed star coordinate fails to force diagonal displacement zero, or the moving spike does not obstruct equality. | Least quotient period. |
| P28-X11 | Separate \(q_n\), \(d_n\), moving-coordinate \(y_n^{(i)}\), star-coordinate \(y_n^{(\star)}\), and phase subsequence \(z_m^{(i,s)}\). | The complete-state recurrence is stated at \(n=0\) without its iff, or \(n\equiv\star\pmod\ell\) appears. | V3/V4 scalar-index repair. |
| P28-X12 | Set each structural hypothesis to its boundary value in turn. | A theorem survives merely because a finite fixture does not reveal the failure. | Sharp anti-claims and counterexamples. |

## Exact recurrence boundary fixture

For the registered fixture,

\[
 A_{\alpha_A}u_0=(12,13,13,13).
\]

The canonical momentum seed \(m_0=(1,1,1,1)\) lies in the exact carry chamber
and has the same maximum bound needed for the \(n=0\) complete-state scalar
recurrence.  In contrast,

\[
 m_0=(10,10,10,10)
\]

still satisfies the strict first-carry gate but gives \(q_0=2\), \(d_0=10\).
The exact defect is

\[
 d_4-100d_3-d_1+100d_0=100(d_0-q_0)=800.
\]

This is a counterexample to the removed \(n=0\) statement, not evidence for
the corrected general theorem.  The corrected complete-state recurrence
starts at \(n\ge1\), and it extends to \(n=0\) exactly when \(d_0=q_0\).

## Structural failure fixtures

The article may use the following hand-derived failures:

1. \(H=1\): all spike distinctions disappear, selector ties appear, and the
   quotient period collapses.
2. A permutation with shorter quotient orbit: the realized phase period can
   divide that shorter order.
3. Unequal support totals: diagonal drift returns to selector comparisons and
   can destroy the prescribed word.
4. A zero support coordinate: a gradient row can lose the expected monomial;
   the coefficient-uniform leading-form argument no longer applies.
5. Positive characteristic dividing an exponent: a derivative scalar can
   vanish.
6. A zero displayed coefficient: the collected support changes.
7. A nonprimitive pair word: an \(\ell\)-step product exists, but the least
   selector period is a proper divisor.
8. Dimension one: the strict matrix lift can fail by cancellation; for
   \(V(q)=q^2\), \(W(p)=-p^2/4\), the formal matrices do not certify the
   actual target degree.

## Execution and evidence policy

All twelve registered checks are discharged in the proof package by manual
algebra and are independently rechecked at the source-design review.  The
tracker may record only `MANUAL_DERIVATION`, `COUNTEREXAMPLE`, `NOT_RUN`, or
`REVIEW_PENDING`.  It must not contain a fabricated runtime, seed, log,
hardware identifier, sample count, or success rate.

If a later author notices a formula that would benefit from computation, the
default disposition is to prove it manually or narrow the claim.  A new
scientific run would require a distinct explicit authorization and could not
retroactively support this frozen source-design gate.

BATCH07_PAPER28_EXPERIMENT_PLAN_FROZEN

## Controlling append-only correction after the first source-design review

Authority: `B07-E0174-P28-SOURCE-DESIGN-REVIEW-FAIL-CORRECTION-AUTHORIZATION`.
All earlier bytes and the original freeze marker remain historical.  This
packet supersedes only the proof-location cells and tracker-state vocabulary
identified by that event; every check, fixture, falsifier, zero-execution
rule, and theorem boundary is unchanged.

### Canonical proof-location map

| Check | Controlling proof location |
|---|---|
| P28-X01 | P1 |
| P28-X02 | P2 |
| P28-X03 | P7 |
| P28-X04 | P6--P7 |
| P28-X05 | P3--P4 |
| P28-X06 | P3--P5 |
| P28-X07 | P9 |
| P28-X08 | P10 |
| P28-X09 | P11 |
| P28-X10 | P12 |
| P28-X11 | P13 |
| P28-X12 | exact failure fixtures and boundary register following P13 |

P1 is the independent map-level symplecticity/inverse branch.  It is not a
logical predecessor of the weighted-degree branch beginning at P2.

### Canonical tracker states

The exact permitted tracker states are now
`MANUAL_DERIVATION_COMPLETE`, `COUNTEREXAMPLE`, `NOT_RUN`, and
`REVIEW_PENDING`.  The earlier token `MANUAL_DERIVATION` is superseded only
as a vocabulary entry.  Existing `MANUAL_DERIVATION_COMPLETE` rows are
therefore valid and mean that a written author derivation exists but still
requires independent review.

BATCH07_PAPER28_EXPERIMENT_PLAN_CORRECTION_FROZEN
