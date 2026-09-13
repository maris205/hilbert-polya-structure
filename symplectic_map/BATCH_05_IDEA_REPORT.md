# Batch 05 Idea Discovery Report

## Decision

- Decision date: 2026-08-19 UTC
- Gate verdict: `BATCH05_PAPER19_CANDIDATE_GATE_PASS_CORRECTED`
- Selected project: `papers/19-shiftlike-translate-gcd-obstruction`
- Safe title: **Maximum-Dimensional Torus Translates in Sparse Shift-Like
  Recurrences: Coefficientwise Moduli and a Support-One GCD Obstruction**
- Authorized stage: proof/citation/novelty source design only
- External effect: none

Three independent zero-write audits passed the corrected Paper-19 package.
Their reported scores were

| Audit | Novelty | Standalone size | Proof confidence |
|---|---:|---:|---:|
| bounded independent novelty search | 8.2 / 10 | 8.4 / 10 | not scored |
| independent candidate gate | 7.9 / 10 | 8.2 / 10 | 9.1 / 10 |
| arbitrary-rank character adversary | not scored | not scored | 9.7 / 10 |

The conservative scored triple `7.9 / 8.2 / 9.1` clears the Batch-05
conjunctive thresholds `7.5 / 7.5 / 9.0`, and the independent adversary found
no arbitrary-rank or boundary-index counterexample. The unified article has a
credible `26--29` substantive-page proof architecture. A later plan must
realize that range without spacing, font, appendix, or background inflation;
failure stops the project rather than lowering the batch standard.

The detailed current decision is recorded in the Paper-19 section at the end
of this append-only report. The following older sections preserve the exact
Paper-17 and Paper-18 discovery history and must not be read as the current
gate.

## Paper-17 Historical Candidate Record

## Problem anchor

The common object is a finite scalar recurrence cut out inside a torus. A
positive-dimensional family of finite-rank torus survivors forces the
corresponding survivor variety to contain a translate of a positive-dimensional
subtorus. The selected package determines exactly how many torus directions
survive each recurrence when a nonzero constant term is present, and then
classifies the precise two-dimensional failure when that constant anchor is
removed.

The standard character-partition principle is not itself a novelty claim.
The proposed contribution is its recurrence-specific consequence: an exact
dimension profile in all dimensions and all intermediate windows, together
with the unique zero-constant support and coefficient phase that delays
rigidity.

## Part A: constant-anchor dimension decay

Let (F) be a characteristic-zero field, let (k\ge2), and let
(1\le\nu\le k-1). Fix

\[
P(X)=c+\sum_{j=1}^{s}b_jX^{e_j},
\qquad
0<e_1<\cdots<e_s,
\qquad
a,c,b_j\in F^\times,
\qquad s\ge2,
\]

where (s) is the actual nonconstant support after collecting equal powers.
The type-(\nu) shift-like automorphism is

\[
S(z_1,\ldots,z_k)
=
(z_2,\ldots,z_k,P(z_{k-\nu+1})+az_1).
\]

With zero-based scalar coordinates, its recurrence is

\[
x_{n+k}=P(x_{n+k-\nu})+a x_n.
\]

For (0\le m\le k), define the (m)-transition survivor variety over
(\overline F) by

\[
V_m=
\left\{
(x_0,\ldots,x_{k+m-1})\in\mathbb G_m^{k+m}:
x_{n+k}=P(x_{n+k-\nu})+a x_n\ (0\le n<m)
\right\}.
\]

The dominant geometric theorem is:

> If a translate (\xi H\) of a connected embedded subtorus is contained in
> (V_m), then
> \[
> \boxed{\dim H\le k-m.}
> \]
> The same dimension conclusion holds for a translate of a disconnected
> algebraic subgroup after passing to a connected component.

The theorem is sharp at every intermediate window. If (a=1) and
(P(1)=0), then

\[
H_m=
\left\{
x_{k+n-\nu}=1,
\quad x_{k+n}=x_n
\quad(0\le n<m)
\right\}
\]

is a connected subtorus of (V_m) with

\[
H_m\simeq\mathbb G_m^{k-m}.
\]

This is a sufficient equality construction, not a classification of all
parameters or all maximal cosets.

## Part A proof spine

On a translate (\xi H), restrict each ambient coordinate as

\[
x_i=\xi_i\chi_i,
\qquad \chi_i\in X^*(H).
\]

For the (n)-th recurrence put (t=k+n-\nu). If
(\chi_t\ne1), then

\[
1,\chi_t^{e_1},\ldots,\chi_t^{e_s}
\]

are at least three distinct characters because the character lattice of a
connected torus is torsion free. The old and output terms provide only two
additional character classes, so at least one polynomial term is an
uncancellable singleton with nonzero coefficient. Hence

\[
\chi_{k+n-\nu}=1.
\]

After aggregating the polynomial terms, two scalar cases must be kept
separate:

- if (P(\xi_t)\ne0), character independence forces
  (\chi_n=\chi_{k+n}=1);
- if (P(\xi_t)=0), the two endpoint terms force
  (\chi_{k+n}=\chi_n) and (\xi_{k+n}=a\xi_n).

In both cases the kernel of the ambient character map contains

\[
\varepsilon_{k+n-\nu},
\qquad
\varepsilon_{k+n}-\varepsilon_n,
\qquad 0\le n<m.
\]

These (2m) relations are independent. The pivot indices form a consecutive
length-(m) interval, the endpoint pairs are disjoint, and no endpoint pair
lies wholly in that interval when (m\le k). Therefore

\[
\operatorname{rk}X^*(H)
\le(k+m)-2m=k-m.
\]

Equivalently, the killed initial residues are

\[
R_m=\{n-\nu\pmod k:0\le n<m\}.
\]

This is a translation of (m) distinct residues, not the orbit
(-j\nu\pmod k). No hypothesis (\gcd(k,\nu)=1) is needed.

## Arithmetic transfer and the sharp clock

Let (\Gamma\le\overline F^\times) have finite rank, with arbitrary torsion
and without a finite-generation assumption. The (m)-transition initial
states are naturally identified with

\[
V_m(\overline F)\cap\Gamma^{k+m}.
\]

Laurent's torus Mordell--Lang theorem applies after placing (\Gamma) in the
division hull of a finitely generated subgroup. Since (V_k) contains no
positive-dimensional torus translate, it follows that

\[
\boxed{T_k(S,\Gamma)\text{ is finite}.}
\]

For (a=1,P(1)=0), the one-dimensional (H_{k-1}) construction has
infinitely many points in a suitable rank-one subgroup such as
(\langle2\rangle). Thus (T_{k-1}) can be infinite and the uniform clock
(k) is sharp. This is a qualitative finiteness theorem; no effective
cardinality bound is claimed.

## Part B: exact loss-of-anchor phase in dimension two

Set (k=2,\nu=1,c=0), and write

\[
x_{n+2}=P(x_{n+1})+a x_n,
\qquad
P(X)=\sum_{e\in E}b_eX^e,
\qquad a,b_e\ne0,
\]

where (E\subset\mathbb Z_{\ge1}) is the actual support. Let

\[
V_m^0=
\left\{
(x_0,\ldots,x_{m+1})\in\mathbb G_m^{m+2}:
x_{n+2}=P(x_{n+1})+a x_n\ (0\le n<m)
\right\}.
\]

The exact geometric phase is:

1. If (E=\{1\}), every (V_m^0) contains a one-dimensional torus
   translate. Indeed, for (P(X)=\beta X), choose a nonzero root
   (r^2=\beta r+a) and use
   ((t,rt,\ldots,r^{m+1}t)). Hence no finite geometric rigidity window
   exists.
2. If (E=\{1,d\}), (d\ge2), and
   (P(X)=\beta X+\delta X^d), then (V_2^0) contains a
   positive-dimensional torus translate if and only if
   \[
   \boxed{a=-\beta^2.}
   \]
   At resonance the unique connected positive-dimensional coset is
   \[
   C_d=
   \left\{
   \left(
   \frac{\delta}{\beta^2}t^d,
   t,
   \beta t,
   \delta\beta^d t^d
   \right):t\in\mathbb G_m
   \right\}.
   \]
   For every coefficient choice, including resonance, (V_3^0) has no
   positive-dimensional torus translate.
3. For every other nonlinear actual support, (V_2^0) has no
   positive-dimensional torus translate. This includes nonlinear monomials,
   two-term supports (\{p,q\}) with (2\le p<q), and all supports of
   cardinality at least three.

Consequently (T_3(\Gamma)) is finite for every finite-rank (\Gamma) in
the exceptional (\{1,d\}) phase, while (T_2(\Gamma)) is finite outside
resonance and for every other nonlinear support. At resonance, existence of
the geometric coset does **not** imply infinite intersection with every fixed
(\Gamma); a separate compatible example supplies sharpness. With

\[
\beta=\delta=1,
\qquad a=-1,
\qquad \Gamma=\langle2\rangle,
\]

the points

\[
(x_0,x_1,x_2,x_3)=(t^d,t,t,t^d),
\qquad t\in\Gamma,
\]

give infinite (T_2). Every remaining nonlinear support has a suitable
positive-dimensional (V_1^0) coset and a compatible finite-rank sharpness
example.

## Part B proof spine

The zero constant term removes the trivial-character anchor. The local
character equation contains the two endpoint characters and the characters
(e\theta) for (e\in E).

- If the middle character is trivial, (P(\xi)=0) gives a root-copy branch
  and (P(\xi)\ne0) kills both endpoints. A second recurrence kills the
  apparently free root-copy branch.
- For a nonlinear monomial, two consecutive recurrences give
  ((d^2-1)\theta=0), hence (\theta=0).
- With two exponents (p<q), the two endpoint terms must pair bijectively
  with (p\theta,q\theta). The only two-step nonzero word forces (p=1);
  scalar compatibility then forces (a=-\beta^2).
- A third recurrence would require either (\theta=d\theta) or
  (\theta=d^2\theta), so the exceptional word cannot extend.
- Three or more current characters cannot be covered by two endpoint terms.

Thus the same character-deficit mechanism explains both parts. A nonzero
constant supplies an additional fixed character and pins one pivot at every
step; deleting it leaves exactly one critical low/high alternation in
dimension two.

## Collision matrix

The primary-source search was bounded through 2026-08-17. Its negative
result is provisional and is not an absolute priority statement.

| Source or predecessor | What it supplies | What remains in Paper 17 |
|---|---|---|
| [Laurent, *Equations diophantiennes exponentielles*, Invent. Math. 78 (1984)](https://doi.org/10.1007/BF01388597) | Finite-rank/division-group intersections with torus subvarieties are finite unions of cosets. | The recurrence-specific (k-m) dimension bound, sharp subtori, and support phase. |
| [Evertse--Schlickewei--Schmidt, Annals 155 (2002)](https://arxiv.org/abs/math/0409604) | Nondegenerate unit equations over characteristic-zero finite-rank groups. | The full torus-coset classification used here; ESS is an alternate boundary, not the headline proof. |
| [Bedford--Pambuccian (1998)](https://doi.org/10.1090/S1088-4173-98-00027-7) | Type-(\nu) shift-like maps, filtrations, Green functions, and currents. | Finite-rank torus survivors and exact intermediate-window dimension decay. |
| [Bera (2018)](https://arxiv.org/abs/1805.03142) | Degeneration and analytic dynamics of polynomial shift-like maps. | Arithmetic torus intersections and the zero-constant support phase. |
| [Bera--Verma (2013)](https://arxiv.org/abs/1309.3392) | Analytic and unstable-manifold properties of shift-like automorphisms. | The proposed algebraic and arithmetic survivor theorems. |
| Paper 16 | A stronger explicit cardinality bound for (k=2,c\ne0,s\ge2), plus the absorbed support-one theorem. | All (k,\nu,m) torus-coset dimensions and the entire (c=0) classification. The (k=2,m=2,c\ne0) shadow is only a consistency check and is not marketed as new. |

No checked source states the exact (k-m) profile, its all-(m) sharpness,
or the unique zero-constant resonance (a=-\beta^2).

## Candidate disposition table

| Candidate | Disposition | Reason |
|---|---|---|
| unified dimension-decay plus zero-constant phase | **SELECT / GO-CORRECTED** | Two independent proof audits close the theorem; scores clear all gates once geometric and arithmetic quantifiers are separated. |
| zero-constant two-dimensional phase alone | MERGE | Novel and proof-closed, but standalone score was only 6.9 and the natural article was about 14--18 pages. |
| high-dimensional (T_k/T_{k-1}) finiteness alone | MERGE | The exact all-(m) geometric profile is the real contribution; qualitative endpoint finiteness alone is too close to Paper 16. |
| all-degree unicritical multiplier ramification count | STOP | Morton's 1996 multiplier function-field, discriminant, infinity, and genus results reduce the proposed statement to a short Riemann--Hurwitz corollary. |
| quartic multiplier-image conductor and local singularities | HOLD | Potentially new local analytic data remain, but transversality, branch intersection, and conductor calculations are not proof-closed. |
| general-(d\) pure trace cutoff three | STOP FOR NOW | The arbitrary multiple-root (a=1) period-three separation is still open; Paper 15 covers only the closed quartic case. |
| dynatomic resonance-divisor normalization/inertia | HOLD | Known support and satellite-inertia results leave only a narrower local-model upgrade, whose normalization proof is incomplete. |
| higher-dimensional support-one (T_{2k}) clock | STOP | No complete character-chain classification; proof confidence is below the gate. |
| general Laurent or rational-support automaton | HOLD | Interesting extension, but endpoint partitions and denominator cancellations are not yet closed. |

## Locked anti-claims

The source-design package must explicitly exclude all of the following:

1. saying that (T_m) itself is positive dimensional;
2. saying resonance makes (T_2(\Gamma)) infinite for every (\Gamma);
3. treating (a=1,P(1)=0) as necessary for equality;
4. imposing or silently using (\gcd(k,\nu)=1);
5. using the incorrect rotation orbit (-j\nu\pmod k);
6. putting nonlinear monomials in the no-finite-window class;
7. claiming an effective cardinality bound from Laurent's qualitative theorem;
8. presenting the standard character-partition lemma as the novelty;
9. claiming positive-characteristic, zero-feedback (a=0), rational-support,
   or arbitrary-polynomial-automorphism extensions;
10. claiming that support is invariant under affine conjugacy;
11. claiming finite generation or bounded torsion for every finite-rank group;
12. claiming Paper 17 improves Paper 16's explicit two-dimensional bound;
13. claiming global priority from a bounded literature search;
14. claiming that every maximal/equality coset has been classified;
15. claiming heights, periodic-point classification, or effective enumeration.

## Source-design obligations

Paper 17 may now create exactly one ten-file source-design package under
`papers/17-shiftlike-torus-coset-decay`, using only `notes/`, `refine-logs/`,
and `experiments/`. It must contain:

1. a research question with exact geometric and arithmetic quantifiers;
2. a full proof package for both parts and their common character-deficit
   lemma;
3. a claims/evidence matrix;
4. theorem-level citation verification, with Laurent as the only indispensable
   imported proof engine unless a later reviewer requires otherwise;
5. a bounded-search novelty assessment and Paper-16 collision ledger;
6. initial/final proposal and review-summary records;
7. experiment plan/tracker records declaring that no scientific run is needed
   or authorized.

The package must plan a genuine 22-page mathematical manuscript, keep Part A
dominant, and make Part B the exact boundary theory rather than a detached
second note. A fresh independent review must return scores at least
`7.5 / 7.5 / 9.0` and `SOURCE_DESIGN_PASS` before any source lock. No paper
plan, bibliography, TeX source, code, scientific execution, figure, build,
release, upload, submission, external message, or identity disclosure is
authorized by this candidate decision.

## Paper-17 Source-Design Addendum

The exact ten-file source-design package has been completed under
`papers/17-shiftlike-torus-coset-decay`, confined to `notes/`,
`refine-logs/`, and `experiments/`. Its frozen author-package inventory is
10 regular files in three directories, totaling 109,602 bytes and 2,525 LF
lines; it contains no paper source, code, result, figure, asset, lock, build,
or release artifact.

A fresh independent line-by-line proof, citation, novelty, and portfolio audit
returned novelty `8.0`, standalone value `7.6`, and proof confidence `9.2`.
It independently closed the Part-A character-lattice dimension drop and
sharpness, the complete Part-B `A/B/C` and resonance classification, the
arbitrary-characteristic-zero and arbitrary-torsion finite-rank bridge to
Laurent, all 15 anti-claims, and the non-absorption boundary against Paper 16.
The reviewer found a credible non-padded range of `19.5--22.5` substantive
pages, so the article target is fixed at about 22 pages rather than padded to a
larger envelope.

The sole review artifact is
`notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`, SHA-256
`aa67cb9c507e244095df86390bcfe5799c8919a1b32b99b84e94ee98b8538260`,
22,043 bytes, 390 LF lines, with final exact line `SOURCE_DESIGN_PASS`. All ten
author files remained byte-identical after review. This pass authorizes only
one canonical source lock and one fresh independent source-lock review. It
does not authorize a paper plan, bibliography, TeX manuscript, code,
scientific execution, figures, compilation, release, submission, upload,
external messaging, or identity disclosure.

## Paper-17 Source-Lock and Plan-Stage Addendum

A separately invoked proof-only plan stage opened after a repaired canonical
source lock and a fresh replacement review passed. The final lock is
`experiments/source_lock.json`, SHA-256
`31b7e8d156bfe46f48bbe0fd38fc6d0f7cbd50da1d78eced8eb0d2b9d7ab0c9f`,
53,476 bytes and one LF. Its 23 source-lock-time bindings remain exact. The
lock makes 21 theorem, proof, citation, review, and predecessor-provenance
inputs permanently byte-immutable. It treats the two Batch controls as exact
historical snapshots and permits only closed lifecycle transitions: selected
status fields and the Paper-17 queue row, append-only status activity entries,
and complete idea-report addenda after the immutable 16,273-byte / 403-LF
prefix.

The governance repair resolved two fail-closed issues before any paper plan
was written. First, it replaced the overbroad rule under which any later Batch
status update would invalidate the lock. Second, it embedded an exact
four-pointer, machine-reproducible definition of the protected permission
bundle rather than relying on an external digest recipe. Exact reverse-diff
checks recover both superseded lock identities, while the theorem, proof,
citation, score/page, anti-claim, permission, and zero-science subtrees remain
unchanged.

The fresh same-path replacement review is
`notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`, SHA-256
`97dca62e01f1906c0a9a5042215badfc6db38b521aff8ba6e7ef996fb751b6b2`,
19,068 bytes, 332 LF lines, ending exactly `SOURCE_LOCK_PASS`. It independently
reproduced all seven protected semantic digests, both exact reverse chains,
all 23 live bindings, the 21/2 transition split, both theorem proofs and
scalar orientations, Laurent's field/torsion and record distinctions, all 15
anti-claims, the Paper-16 boundary, and the permission firewall.

This local-only transition authorizes exactly one proof-first
`paper/PAPER_PLAN.md` and one fresh independent paper-plan review. The plan
must target the verified `19.5--22.5` substantive-page range, approximately 22
pages without padding, keep Part A dominant, and present Part B as the exact
loss-of-anchor boundary. It authorizes no bibliography, TeX manuscript, code,
scientific execution, result, figure, build, finalization, release, repository
push, submission, upload, external message, or identity disclosure.

## Paper-17 Terminal Addendum and Paper-18 Transition

Paper 17 completed its full local anonymous proof-first lifecycle as **Sharp
Torus-Coset Decay for Sparse Shift-Like Recurrences: Constant Anchors and the
Exact Zero-Constant Boundary**. Independent Round 2 is
`notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md`, SHA-256
`b48628803c1cdb9fe0ec1f34b78ff0f9e33b47e935e24863288d817fc1009a4d`,
24,140 bytes and 431 LF, ending exactly `MANUSCRIPT_R2_PASS`. The independent
finalization-stage review is
`notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md`, SHA-256
`d31cdd9773234a3ff38f706b5bcc9491ba31d3380bf38dd81ba7b200de038abf`,
19,295 bytes and 337 LF, ending exactly `FINALIZATION_STAGE_PASS`.

The byte-identical 22-page local final PDF is `paper/main.pdf`, SHA-256
`080282e18b085cc87bb590db239c4c8f8f80fd86147ded1aa775e67504b17f2e`,
381,957 bytes and 2,066 LF. The strict-canonical release manifest is
`paper/FINAL_RELEASE_MANIFEST.json`, SHA-256
`7ddc2d3e9c92f47d447bc9688c4f0769e1d0b676e798cf56c428b8c83dc86c4e`,
42,216 bytes and one LF. The fresh terminal review is
`paper/reviews/final_integrity_review.md`, SHA-256
`941e8b47e4436fdd9bff6f48ebf6e8c1174d07f545a220ead9ad02d73b23ed9d`,
20,620 bytes and 339 LF, ending exactly, in order,
`FINAL_INTEGRITY_PASS` and `RELEASE_CONFIRMED`. Its 33-row binding table was
rechecked locally with zero identity mismatch, and exact `T34` remains
immutable.

The sole effect is `LOCAL_ANONYMOUS_RELEASE_ONLY`. No submission, upload,
public hosting, repository push, external messaging, camera-ready identity
insertion, or identity disclosure occurred or is authorized. Paper 17 is
`COMPLETE_LOCAL_FINAL_REVIEW_PASS`, and Batch 05 is complete at 1 / 5.
The batch dashboard advances only to `PAPER18_CANDIDATE_DISCOVERY`: no
Paper-18 candidate is selected, no Paper-18 project directory exists, and no
Paper-18 paper number is consumed before candidate PASS. This append-only
addendum leaves the protected 16,273-byte / 403-LF historical prefix and all
earlier addenda unchanged.

## Paper-18 Candidate Decision

Paper 18 is opened as `papers/18-marked-henon-scalar-boundary` under the
public-safe title **Marked Trace Coordinates and Scheme-Theoretic
Ramification at the Polynomial Boundary of Generalized Hénon Maps**. Two
independent, bounded primary-source and proof audits found no direct collision
through 2026-08-17. The first audit scored novelty / standalone value / proof
readiness at 8.1 / 7.9 / 9.4. A fresh adversarial gate identified necessary
component, fiber, Fitting-locus, and quotient qualifications; after those
repairs, its conservative scores are 8.0 / 7.7 / 9.3. All three Batch-05
thresholds therefore pass without waiver.

For `d >= 2`, put `r=d-1` and consider the monic-centered family
`H_{b,p}(x,y)=(p(x)+by,x)` together with `r` pairwise disjoint, simple,
exact cycles of arbitrary prescribed periods. After quotienting point
markings by cyclic rotation, let `C_n` be the unique irreducible component of
the simple cycle-marked incidence containing the full scalar fiber `b=0`.
The corrected theorem has five coupled assertions:

1. the scalar polynomial incidence is irreducible, and `C_n` is the unique
   component through it; the projection to the coefficient/Jacobian base is
   étale on this simple incidence and dominant;
2. `Psi=(-b,tr(DH^{n_1}),...,tr(DH^{n_r}))` is dominant and generically
   étale, and is étale at a scalar point, so the marked traces are
   algebraically independent over `C(b)`;
3. only after shrinking to a nonempty open `U` in `G_m` do these traces give
   dominant, generically étale coordinates on every fixed `b_0 in U`
   fiber;
4. along every simple scalar point the completed local ring is
   `C[[b,u_0,...,u_{d-2}]]` and each Hénon trace has expansion
   `rho_i(b,u)=lambda_i(u)+bG_i(b,u)`;
5. on the simple scalar locus, and only there, base change for K\u00e4hler
   differentials and zeroth Fitting ideals gives the scheme identity
   `R_H x_C S = R_poly`, equivalently `J_H mod b = +/- J_poly` in every
   completion.

The proof begins with the cyclic orbit equations
`x_{j+1}-p(x_j)-b x_{j-1}=0`. Simplicity makes the orbit-variable Jacobian
invertible and hence the marked incidence étale over the base. At `b=0`,
`H_0^n(x,y)=(p^n(x),p^{n-1}(x))`, the trace becomes the scalar multiplier,
and simplicity becomes `1-lambda != 0`. Gorbovickis's arbitrary-period
polynomial multiplier theorem and irreducibility lemma supply a scalar point
with nonsingular multiplier Jacobian. The differential of `Psi` is then block
triangular with diagonal blocks `-1` and the scalar multiplier Jacobian.
Dominance, spreading out in `b`, completed local coordinates, and Fitting
base change finish the five statements. Any finite-free orbit-algebra lemma
used in the package must remain separate from, and must not be inflated into,
irreducibility of the full Hénon incidence.

The mandatory limitations are part of the theorem package: general nonzero
`b` is not every `b` and not a prescribed value such as `-1`; only the
selected component through the scalar boundary is controlled; the Fitting
identity is not extended to nonsimple or singular closures; no reducedness,
normal crossings, transversality, or closed-point intersection number is
asserted; the result lives on the monic-centered normal-form cover with its
residual `mu_{d-1}` action; point markings also have cyclic-shift fibers;
trace plus the known determinant determines only the unordered multiplier
pair; `b=0` is a proof boundary, not an automorphism; and there is no positive
characteristic, multi-factor, all-fiber, global-injectivity, experiment, or
absolute-priority claim.

The closest sources are sharply separated. Gorbovickis (2013) is the sole
essential proof input and already owns the scalar arbitrary-period multiplier
independence. Gorbovickis--Taflin concern regular polynomial endomorphisms,
not Hénon automorphisms or this boundary Fitting identity. Huguin treats
complete unmarked period-one/two polynomial spectra. Cantat--Dujardin prove
full-spectrum and finite-cutoff Hénon rigidity, not arbitrary selected
marked-cycle local coordinates or the scalar boundary scheme. Bianchi--He
use the full marked unstable spectrum analytically on hyperbolic components.
Friedland--Milnor supply a low-degree fixed-point overlap only. Six weaker
packages were stopped: Morton already controls the multiplier-plane function
field/genus; global node and satellite singularity claims lack
transversality; the power-map and total-ramification variants are too small or
known; and the multi-factor extension is not proof-closed.

The current authority is exactly the ten proof-first source-design files in
`notes/`, `refine-logs/`, and `experiments/`, followed after a stable author
stop by one fresh independent source-design review. It authorizes no lock,
paper plan, bibliography, TeX, build, scientific execution, finalization,
release, submission, upload, external messaging, or identity disclosure.

## Paper-18 Source-Lock and Plan-Stage Addendum

Paper 18 has passed the repaired source-design and source-lock gates without
changing its theorem. The independent source-design review ends exactly
`SOURCE_DESIGN_PASS` and has SHA-256
`b5112a412bf52d504b856e4652023ed41e682f35c566903df2da0fbbc58947e4`.
The final strict-canonical source lock has SHA-256
`b29378068f5da669f6b9c15d4d4a3e81daa6a2ca345fd86481c403f86771fac3`,
32,589 bytes, and one LF. Its complete history records the original
Cartier-or-empty correction, exact write accounting, and removal of an
unbound optional citation record; all fifteen bindings and all theorem,
proof, score, universe, permission, and A1--A20 records remain exact.

A fresh independent source-lock reviewer, supported by separate binding and
proof/citation crosschecks, issued `SOURCE_LOCK_PASS`. The review has SHA-256
`970a3f3ccaa55390b6242b46bdf4776bcd404f53a5dcf5753ce99917cb4f1ae1`,
17,222 bytes, and 319 LF. A separate plan-stage invocation now authorizes
exactly one proof-first `paper/PAPER_PLAN.md` and, after its stable author
stop, exactly one fresh independent plan review. Bibliography, TeX,
manuscript drafting, code, science, figures, builds, publication governance,
finalization, release, repository push, submission, upload, external
messaging, and identity disclosure remain false. The effect remains local
only, and Papers 19--21 remain unopened.

## Paper-18 Plan PASS and Publication-Governance Addendum

Paper 18 now has a frozen proof-first plan at SHA-256
`33dad14ad5af5a022e99ce7ca573ab1c23b4984b5f37b9da26e04257015ce168`
(39,127 bytes, 633 LF). It assigns exactly 23.0 content pages to eight
numbered sections and one Appendix A, leaves references as the final
unnumbered part, and permits exactly one non-numerical proof-dependency table,
zero figures, and zero science. The five-part theorem, the finite-free cyclic
loop lemma and its `n=1,2` guards, the unique scalar component, the safe
general-`b` specialization, completed local coordinates, exact Fitting base
change, Cartier-or-empty alternative, residual normal-form action, and all
A1--A20 limitations remain explicit in the main-text architecture.

A fresh independent review passed the plan conjunctively and wrote
`PAPER_PLAN_PASS`; its SHA-256 is
`c0f09b1ce163d23e327fa6db93d9fcc1e4df41bc18b93b8875fbb748ffb62a88`
(18,794 bytes, 356 LF). A separate publication-governance invocation now
authorizes only a human-readable publication scope, its strict-canonical lock,
and one fresh independent publication-stage review. It does not yet authorize
`main.tex`, a bibliography, compilation, scientific execution, figures,
finalization, release, submission, upload, repository push, external
messaging, or identity disclosure. Papers 19--21 remain unopened.

## Paper-18 Publication PASS and Drafting Addendum

Paper 18 has passed its publication-stage governance review without changing
the theorem or plan. The human scope is SHA-256
`6802b5fb83657cff2a1b65c1e4c9f8bdc6f726df9d713a84ace09adcc87951a6`
(44,779 bytes, 932 LF), and the strict-canonical lock is SHA-256
`052ba1d2ed94055feaa7af53aa667019ec81481621d86fbe5775fd73eaf6d542`
(60,277 bytes, one LF). Their exact stage universes run from the fifteen-file
plan-pass baseline through formal source review, two deterministic build
rounds, one bounded revision window, and fresh R2 while keeping finalization,
release, and external actions closed.

The independent publication review is SHA-256
`65e900ae47c11b3a7ea47bfd17f9ef5331a2e9e27e1b6ef617700ca5f2dc8e1e`
(21,205 bytes, 378 LF) and ends `PUBLICATION_STAGE_PASS`. A separate drafting
invocation now permits only the anonymous monolithic `paper/main.tex` and the
exact seven-entry `paper/references.bib`, in that order. The manuscript must
retain eight numbered sections, Appendix A, 22--24 content pages targeting
23, a separate final References part, one non-numerical proof table, zero
figures, zero science, the five theorem parts, all proof bridges, and A1--A20.
No build or later-stage authority follows until a fresh formal source review
returns `MANUSCRIPT_SOURCE_PASS`. Papers 19--21 remain unopened.

## Paper-18 Source PASS and Round-0 Addendum

Paper 18 now has stable anonymous public sources. The repaired monolithic
`main.tex` is SHA-256
`f7e13264d0dbf3d4f1c11250c1f3e93263c9558fae825d33c8f13d19d0f9bf37`
(63,086 bytes, 1,500 LF), and the exact seven-entry bibliography is SHA-256
`51bb41341009caa22d9433440475761608e1d4af2343a974cfbd74447070ea21`
(1,577 bytes, 54 LF). The only bounded source repair changed two unsupported
`\mathscr` basis symbols to the already available `\mathcal` notation; it did
not alter the theorem, proof, citations, scope, or inventory.

A fresh reviewer reread the full repaired source universe and issued
`MANUSCRIPT_SOURCE_PASS`. Its review is SHA-256
`0f956315fe7ef17b20d7208f664fadc6681243ba360fe6fa3bee23da4da2ebd0`
(16,889 bytes, 293 LF). A separate Round-0 invocation now authorizes only two
fresh locked build roots, the exact two-by-four command ledger, complete
non-raster validation and explicit cleanup, followed by
`paper/main_round0.pdf` and strict-canonical `paper/BUILD_RECEIPT_R0.json`.
No source edit, revision, R1 verdict, finalization, release, or external action
is authorized. Papers 19--21 remain unopened.

## Paper-18 Terminal Closure Addendum

Paper 18 completed its full local anonymous lifecycle on 2026-08-19. Its
final anonymous PDF is
`e9044c2a9e6452b58b9e345a17c33a211feed909414798fa4696e169b24be06b`
(425,791 bytes, 2,220 LF), its current strict-canonical release manifest is
`4ecd941e55cf14d3e84e964a484fb6bd4a9af6a7f745f42948f5760f6350c43c`
(43,491 bytes, one LF), and its terminal integrity review is
`251d78d2989c0c76b6f1a3090c9aeccf9c66a7171829ca6b795c9ca97d359713`
(8,122 bytes, 65 LF). The review ends exactly `FINAL_INTEGRITY_PASS` followed
by `RELEASE_CONFIRMED`. The final universe has 34 regular files and five
descendant directories, with no symlink or other object. All build roots and
suffix-associated temporary residues are absent. The effect is
`LOCAL_ANONYMOUS_RELEASE_ONLY`; no submission, upload, public hosting,
repository push, external messaging, or identity disclosure occurred.

## Paper-19 Candidate Decision

Paper 19 is formally opened as
`papers/19-shiftlike-translate-gcd-obstruction` under the public-safe title
**Maximum-Dimensional Torus Translates in Sparse Shift-Like Recurrences:
Coefficientwise Moduli and a Support-One GCD Obstruction**. Its conservative
gate scores are:

| Audit | Novelty | Standalone size | Proof confidence |
|---|---:|---:|---:|
| bounded independent novelty search | 8.2 / 10 | 8.4 / 10 | not scored |
| independent candidate gate | 7.9 / 10 | 8.2 / 10 | 9.1 / 10 |
| arbitrary-rank character adversary | not scored | not scored | 9.7 / 10 |

The package has one unified mathematical contrast. In the anchored regime
with at least two collected nonconstant powers, the predecessor dimension
bound is upgraded to a classification of every maximum-dimensional connected
translate. The underlying subgroup is forced to be the canonical `H_m`, and
the normalized translates form an explicit locus `E_m` with active size
`alpha_m=min(m,k-m,nu,k-nu)`. This yields the exact geometric-fiber branches,
multiple-root local structure, a fixed-support universal flat lci family, and
coefficientwise sharpness after a compatible finite extension and choice of
finitely generated multiplicative group.

In the support-one regime, let `g=gcd(k,nu)`, `q=k/g`, and
`L=(k-nu)/g`. A component-height argument over the actual character lattice
proves extinction after `q^2` core equations and a unique rank-one character
shadow after `q^2-1`. The shadow is determined from a central delta block by
`F_{n+q}=F_n+T F_{n+L}`; explicit semigroup formulas show every involved term
is zero or a monomial, and identify seven forced local labels. For `q>=3`,
their scalar equations force `bc^(d-1)=-1`, then `a=-1`, and finally
`2c=0`, contradicting characteristic zero. Thus `V_{kq-1}` has no
positive-dimensional torus coset. This is a universal obstruction at the
penultimate character window, not an exact or minimal scalar threshold.

For `q=2`, the unique CBA shadow lifts exactly when
`a=-1` and `bc^(d-1)=-1`; general `g` is completed by choosing the inactive
residue scalar segments in a nonempty Zariski open set. This endpoint belongs
to Paper 16 and is included only for consistency. Paper 17 already owns the
`k-m` upper bound, its special equality family, and `T_k` finiteness; Paper 19
may claim only complete maximum-dimensional translate classification,
normalized-locus and coefficient-family geometry, coefficientwise sharpness,
and the new `q>=3` character-versus-scalar obstruction. Paper 18 has no
substantive theorem collision.

The original support-one conjecture that every `kq-1` character shadow lifts
was refuted first at `(k,nu,d)=(3,1,2)` and then by the universal seven-label
contradiction. It is permanently recorded as `STOP-S1` and may not be revived
by changing notation or weakening provenance. The project also makes no
classification of lower-dimensional or inclusion-maximal cosets, no
Hilbert/Fano fine-moduli claim, no assertion for every original field or
every fixed finite-rank group, no effective count, no positive-characteristic
claim, no exact `q>=3` escape threshold, and no absolute-priority claim.

A bounded primary-source search through 2026-08-19 found no direct collision.
Laurent's torus Mordell--Lang theorem is the only external proof theorem;
translated-subtorus, sparse-polynomial, Fano-scheme, shift-like-dynamics, and
orbit-arithmetic papers are cited only as neighboring context. The corrected
package supports approximately 26--29 genuine mathematical pages without
figures, experiments, code, appendix inflation, or hidden finite searches.
Exactly ten proof/citation/novelty source-design files are now authorized,
followed only after a stable author stop by one fresh independent review.
No source lock, paper plan, bibliography, TeX manuscript, scientific
execution, build, finalization, release, or external action is authorized.

## Paper-19 Source-Design PASS Addendum

The Paper-19 author package is now frozen as exactly ten Markdown files in
`notes/`, `refine-logs/`, and `experiments/`. It contains 127,846 bytes and
3,161 LF, and its sorted identity payload
`relative-path<TAB>sha256<TAB>bytes<TAB>LF<LF>` has SHA-256
`5d963e353fa915a0832adeb380cd69c1f8cc76becf8825a546bf243f83937fea`.
The author package records the corrected support-one history under
`STOP-S1`, the actual-character-lattice quantifier, colored scaling
components, explicit backward and forward generating functions, all seven
selected labels, the `q=2` general-`g` generic fill, and AC01--AC18.

A fresh independent reviewer then replayed all nine source-design audit
blocks without modifying any author file. It independently checked the
saturated equality subgroup and normalized locus, the fixed-fiber and
coefficient-family geometry, coefficientwise arithmetic, exclusive labels
and gcd bookkeeping, arbitrary-rank component-height extinction, the unique
Laurent shadow and first collision, the scalar obstruction and `q=2`
endpoint, the Paper16--18 boundary, and a bounded literature refresh through
2026-08-19. Its sole file is
`notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`, SHA-256
`4b2f309d6a84bf53bd6b28319fba2a47386e4d3c1ac96c86375a1a43a155c724`,
24,917 bytes and 469 LF, ending exactly `SOURCE_DESIGN_PASS`.

This pass authorizes only one strict-canonical source lock binding the frozen
author universe and independent review, followed by one fresh independent
source-lock review. It does not authorize a paper plan, bibliography, TeX,
scientific execution, figures, compilation, revision, finalization, release,
submission, upload, external messaging, or identity disclosure.

## Paper-19 Source-Lock PASS and Plan-Stage Addendum

Paper 19 now has a strict-canonical source lock at SHA-256
`bba41a3df39f41f367e8fbfaec3703c09c56f1f63af8904e908d262f41179aba`
(30,695 bytes, one LF). It binds the ten author files and independent
source-design review as an exact eleven-entry ledger; fixes the Part A
equality-rigidity and coefficient-family package, the Part B arbitrary-rank
colored-component argument, both generating functions, the seven-label
scalar contradiction, the `q=2` general-`g` fill, `STOP-S1`, AC01--AC18, and
all Paper16--18 boundaries; and keeps all scientific execution and external
effects false. Its own digest and byte count are correctly self-excluded.

A fresh reviewer who authored none of the twelve inputs independently
replayed the lock and full source universe. The review is SHA-256
`31a009eb64383eda501d37fd146a9a8456cdc427e951ec321c1b11108fc40b8b`,
25,379 bytes and 548 LF, and ends exactly `SOURCE_LOCK_PASS`. U13 now consists
of thirteen regular files and three directories, with no symlink or other
object. A new bounded stage authorizes only a proof-first
`paper/PAPER_PLAN.md`, followed after plan-author stop by one fresh
independent plan review. It still does not authorize bibliography, TeX,
experiments, figures, compilation, revision, finalization, release, or any
external action.

## Paper-19 Plan PASS and Publication-Governance Addendum

Paper 19 now has a proof-only plan at SHA-256
`8aac5856b1e480182cefe5796275fb9e8335efc161fd87e3782446716a74ff07`
(40,343 bytes, 428 LF). Its twelve content blocks sum exactly to 29.00 pages;
references are separate, and appendix padding, figures, numerical-result
tables, code, data, and scientific execution are all zero. The plan places
all TA1--TA4, CA1, TB1--TB9, and CB1 proofs in the main text; fixes a
31-item theorem/lemma numbering map and acyclic dependency graph; and binds
the exact hypotheses, two generating functions, semigroup ranges, selected
labels, scalar contradiction, `q=2` fill, citations, predecessor ownership,
`STOP-S1`, AC01--AC18, and source-writing checks.

A fresh independent reviewer replayed the complete U14 and issued
`PAPER_PLAN_PASS`. The review is SHA-256
`12664657e0c6c0e667ace509e1e174f0ab80ed9be9ea0fd435e8284ed09324b7`,
25,247 bytes and 466 LF. The current exact U15 contains fifteen regular files
and four directories, with no symlink or other object. The next separately
invoked gate authorizes only a human-readable publication-stage scope, a
strict-canonical publication lock, and one fresh independent review. It does
not authorize bibliography, TeX, manuscript drafting, compilation, release,
or any external action.

## Paper-19 Publication PASS and Anonymous-Drafting Addendum

Paper 19 has passed publication governance without changing the theorem or
plan. The human-readable scope is SHA-256
`fab52ee3553cf6ea14c8a098acdc28002d928b85f69a499652955b63a6ecd960`
(29,294 bytes, 300 LF), and the strict-canonical lock is SHA-256
`e82f40517dc08ccda3f8cd582b297f07e65cc546b879f8299a1891fc67a06969`
(58,406 bytes, one LF). Together they freeze the anonymous 29-page article,
all proof and citation obligations, source order, formal source-review gate,
deterministic R0/R1/R2 chain, bounded revision policy, finalization
reservations, local-only ceiling, and all external-effect prohibitions.

A fresh independent reviewer reread U17 and issued
`PUBLICATION_STAGE_PASS`. Its review is SHA-256
`045a3305c0bedf627076e21f2c51b69ec64bc560958e9a3261275b2545e5f438`,
24,647 bytes and 474 LF. U18 now contains eighteen regular files and four
directories, with no symlink or other object. A separate anonymous-drafting
stage permits only `paper/main.tex`, then the locked `paper/references.bib`,
followed after source-author stop by one fresh formal source review. It does
not authorize compilation, PDF creation, revision, finalization, release, or
any external action.

## Paper-20 Candidate Decision

Paper 20 passes the corrected candidate gate in a fixed, proof-first
four-dimensional family. The public-safe working title is **Asymmetric
Coupled Hamiltonian Shears: An Explicit Non-Product Dynamical-Degree Matrix**.
The theorem is intentionally not a claim about all polynomial automorphisms,
all sparse shears, arbitrary words, or all Hénon maps.

Fix an integer (g\ge5) and a characteristic-zero field, and set
\[
 V_g(q_1,q_2)=q_1^2q_2^2+q_1^g,
 \qquad W_g(p_1,p_2)=p_1^2p_2^2+p_2^g.
\]
The canonical shears are
\[
 S_V(q,p)=(q,p+\nabla V_g(q)),\qquad
 T_W(q,p)=(q+\nabla W_g(p),p),\qquad F_g=T_W\circ S_V.
\]
Their cross monomials make the support hypergraph connected and non-block
diagonal. For the two (q)-coordinate degrees (u_n) and the two
(p)-coordinate degrees (v_n), use the two-phase cones
\[
 C_q=\{u>0:1\le u_2/u_1<(g-2)/2\},
 \qquad C_p=A_gC_q,
\]
not a fictitious single strict cone across both half-steps. On these cones
the leading branches are exact, with
\[
 A_g=\begin{pmatrix}g-1&0\\2&1\end{pmatrix},
 \qquad B_g=\begin{pmatrix}1&2\\0&g-1\end{pmatrix},
 \qquad C_g=B_gA_g=\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix}.
\]
The ratio map is
\[
 f_g(r)=\frac{(g-1)(r+2)}{g+3+2r};
\]
the endpoint inequalities (f_g(1)\ge1) and
(f_g((g-2)/2-)<(g-2)/2) prove forward invariance. Strict branch
inequalities, positive integer coefficients, and characteristic zero exclude
later coefficient cancellation. The exact full-step recursion is
\[
 v_{n+1}=A_gu_n,\qquad u_{n+1}=C_gu_n,
\]
and the full one-step matrix is
\(\begin{psmallmatrix}C_g&0\\A_g&0\end{psmallmatrix}\), not the half-step
off-diagonal matrix. For (n\ge1), the second (q)-degree is the visible
maximum, so
\[
 \lambda_1(F_g)=\rho(C_g)=g+1+2\sqrt g=(\sqrt g+1)^2.
\]
This is strictly below the naive product ((g-1)^2) of the individual
shear degree maxima; (g=5) gives (6+2\sqrt5<16).

Three independent bounded candidate audits gave conservative scores:

| Audit | Novelty | Standalone size | Proof confidence |
|---|---:|---:|---:|
| candidate author | 8.1 | 8.0 | 9.3 |
| structural auditor | 8.1 | 8.0 | 9.3 |
| publication adversary | 8.1 | 8.0 | 9.2 |

The novelty claim is limited to this explicit asymmetric canonical-symplectic
family and its closed non-product degree matrix. Classical two-dimensional
degree-product results, dynamical tropicalisation, and higher-dimensional
polynomial-automorphism examples are neighboring context, not an absolute
priority claim. Papers 12--19 have no direct theorem collision: their scopes
are trace/ramification, primitive cycles, planar finite-rank torus survival,
fixed-lag torus translates, and support-one gcd obstructions rather than this
four-dimensional degree problem.

Frozen anti-claims and stops include (g\le4), characteristic (p), arbitrary
signs or coefficient specialisations, uncoupled/block-diagonal potentials,
arbitrary sparse shears or words, generic fan extensions, topological entropy,
periodic-point or arithmetic conclusions, and torus-survivor claims. A cone
tie or failed degree separation stops the project rather than being repaired
by an unregistered computation. Exactly ten proof/citation/novelty
source-design files are authorized next; no Paper-20 plan, manuscript,
source lock, experiment, build, release, or external action is authorized.

## Paper-21 Candidate Decision

Paper 21 passes its repaired candidate gate as
`papers/21-three-mode-hamiltonian-cubic-degree`. The public-safe working title
is **Three-Mode Hamiltonian Shears in \(\mathbb A^6\): Exact Degree Growth and
Cubic Perron Subfamilies**. The first proposed matrix package was rejected:
it differentiated the mixed monomial in \(W\) incorrectly. Both independent
PASS artifacts bind only the corrected package below; the superseded rows have
no authority.

Let \(K\) be algebraically closed of characteristic zero, let \(g\ge8\) be an
integer, and put
\[
 V_g(q)=q_1^2q_2^2q_3^2+q_1^g,
 \qquad
 W_g(p)=p_1^2p_2^2p_3^2+p_3^g.
\]
On \(\mathbb A^6_K\), with its standard symplectic form, define
\[
 S(q,p)=(q,p+\nabla V_g(q)),\qquad
 T(q,p)=(q+\nabla W_g(p),p),\qquad F_g=T\circ S.
\]
The exact selected half-step matrices are
\[
 A_g=\begin{pmatrix}g-1&0&0\\2&1&2\\2&2&1\end{pmatrix},
 \qquad
 B_g=\begin{pmatrix}1&2&2\\2&1&2\\0&0&g-1\end{pmatrix},
\]
and therefore
\[
 C_g=B_gA_g=
 \begin{pmatrix}
 g+7&6&6\\2g+4&5&4\\2(g-1)&2(g-1)&g-1
 \end{pmatrix}.
\]

For \(x=u_2/u_1\), \(y=u_3/u_1\), and
\(R=(g-3)/2\), the locked selector cone is
\[
 \mathcal K_g=\{u>0:x\ge1,\ y\ge1,\ x+y<R\}.
\]
The initial vector \((1,1,1)^\mathsf T\) belongs to this cone. The corrected
proof records the three projective invariance margins, including the separate
\(8\le g\le11\) endpoint calculation, and the exact third-coordinate
selector gap
\[
 (g-2)v_3-2v_1-2v_2
   =(2g-6)x+(g-6)y-6\ge6.
\]
Positive integer coefficients in characteristic zero and strict face gaps
give a semiring no-cancellation induction. Thus, with
\(u_0=(1,1,1)^\mathsf T\),
\[
 v_{n+1}=A_gu_n,\qquad u_{n+1}=C_gu_n.
\]
The third \(q\)-coordinate, not the second, is the visible maximum. Hence
\[
 \deg(F_g^n)=e_3^\mathsf T C_g^n(1,1,1)^\mathsf T,
 \qquad \lambda_1(F_g)=\rho(C_g).
\]
The Perron root is the largest real root of
\[
 P_g(t)=t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2,
\]
and the row-sum bound gives
\(\rho(C_g)<(g-1)^2\). For
\(g\equiv2,3,4\pmod5\), reduction modulo five gives one of three cubics with
no root in \(\mathbb F_5\); therefore \(P_g\) is irreducible and the
dynamical degree has algebraic degree three on these infinite subfamilies.

Two fresh corrected audits clear the strict candidate thresholds. R1 is
SHA-256
`d9362d3b07c38e2248494d2c0ec43209e7b0ce8fb089737326d61888b5d1d846`
(8,058 bytes, 237 LF), together with its immutable correction
`6f455d8b40c873b8fc18568d95ed3e3b97de7528eddae911e83a00fe5214c132`
(861 bytes, 32 LF); the corrected verdict scores novelty / standalone size /
proof confidence at `8.2 / 8.4 / 9.1`. R2 is SHA-256
`70592ffe85111cefde9e8fa872688958c22ad7cbe6bf4671151d9e5893aad387`
(6,569 bytes, 185 LF) and scores `8.4 / 8.8 / 9.3`. It independently binds
the corrected selector, \(e_3\)-visibility, no-cancellation induction,
Perron polynomial, mod-five irreducibility, and collision boundary.

The bounded literature check distinguishes this canonical two-shear family
from the affine-triangular classes studied by Blanc--van Santen
(https://arxiv.org/abs/1912.01324) and Shao--Sun
(https://arxiv.org/abs/2509.14584). It found no direct theorem collision in
the checked primary sources; this is not an absolute priority claim. Paper 20
is the direct internal predecessor, but it owns only a four-dimensional
two-mode quadratic Perron matrix. Paper 21's three-mode support, two-dimensional
selector cone, exact cubic matrix, third-coordinate visibility, and infinite
irreducible cubic subfamilies are the material new theorem package.

Frozen anti-claims exclude arbitrary dimensions, arbitrary Hamiltonian
potentials or shear words, generic fan or Newton-polytope classification,
positive characteristic, arbitrary coefficient signs or specialisations,
universal non-conjugacy, topological or measure entropy, arithmetic or
periodic-point conclusions, affine-triangular classification, and absolute
priority. The separated-window recurrence backup and all H\'{e}non
multiplier/ramification backups remain STOP. Exactly the usual ten-file
proof/citation/novelty source-design package is authorized next; no source
lock, plan, manuscript, bibliography, experiment, build, release, transport,
or external action is authorized.

## Batch-05 Terminal Disposition Addendum

Date: 2026-08-23 UTC

This append-only addendum supersedes only the lifecycle-state and permission
statements in the historical candidate decisions above. It alters no theorem,
score, collision boundary, anti-claim, or provenance record. In particular,
the Paper-20 discovery working title **Asymmetric Coupled Hamiltonian Shears:
An Explicit Non-Product Dynamical-Degree Matrix** and the historical
source-lock label with lowercase `asymmetric`/`family` are retained history;
the authoritative rendered title is the one in the table below.

| Paper | Exact project and title | Final disposition | Authoritative local closure evidence |
|---:|---|---|---|
| 17 | `papers/17-shiftlike-torus-coset-decay`; **Sharp Torus-Coset Decay for Sparse Shift-Like Recurrences: Constant Anchors and the Exact Zero-Constant Boundary** | `COMPLETE_LOCAL_FINAL_REVIEW_PASS`; 22-page local anonymous PDF `080282e18b085cc87bb590db239c4c8f8f80fd86147ded1aa775e67504b17f2e`; no external effect | finalization `d31cdd9773234a3ff38f706b5bcc9491ba31d3380bf38dd81ba7b200de038abf`; manifest `7ddc2d3e9c92f47d447bc9688c4f0769e1d0b676e798cf56c428b8c83dc86c4e`; terminal review `941e8b47e4436fdd9bff6f48ebf6e8c1174d07f545a220ead9ad02d73b23ed9d` |
| 18 | `papers/18-marked-henon-scalar-boundary`; **Marked Trace Coordinates and Scheme-Theoretic Ramification at the Polynomial Boundary of Generalized Hénon Maps** | `COMPLETE_LOCAL_FINAL_REVIEW_PASS`; 23-page local anonymous PDF `e9044c2a9e6452b58b9e345a17c33a211feed909414798fa4696e169b24be06b`; no external effect | finalization `a77211f190a87d434b4cb64b2bcac078c864a0660c1181292a2f85866f0dc6ad`; manifest `4ecd941e55cf14d3e84e964a484fb6bd4a9af6a7f745f42948f5760f6350c43c`; terminal review `251d78d2989c0c76b6f1a3090c9aeccf9c66a7171829ca6b795c9ca97d359713` |
| 19 | `papers/19-shiftlike-translate-gcd-obstruction`; **Maximum-Dimensional Torus Translates in Sparse Shift-Like Recurrences: Coefficientwise Moduli and a Support-One GCD Obstruction** | `COMPLETE_BOUNDED_INTERNAL_SCOPE`; all 15 external-source blocks remain; no PDF, build, candidate, finalization, transport, release, or external effect | bounded closure `5e3017024484bee1f922234127fc7ddf762baa716ecfce7a08a99a05ae3b1a49`; independent review `0f2d71c5048371d981e35a470c195358fce208d66b2ba98a104bfe0215ab9045`; historical R15/R16 hashes are non-persisted and non-authoritative |
| 20 | `papers/20-coupled-shear-degree-matrix`; **Coupled Hamiltonian Shear Degree Matrices in A4: An Asymmetric g>=5 Family** | `COMPLETE_LOCAL_FINAL_REVIEW_PASS`; authoritative 23-page candidate `paper/main_release_candidate.pdf` is SHA-256 `07426e1892fbbb85876a6f79401318c16f9d3aee96ae7d6ae2b087a25ca98e40`; 14-page `paper/main.pdf` remains historical; no external effect | finalization review `a09e620e3fb2cf215702db929017c109b78c6ca1dfd0bac70cbe003ac0b278fe`; manifest `422d278b72b606e4c3e0fb1463f1a6d24f78dc9dc5d449b05681ccb086bc4316`; terminal rebuild `3d9d5152f7cc970d27face326a87d9c17a0b34e6ccc8ecc95e82de643010c8e2`; terminal review `94ac571b504024e5472e280e06fe1c3ecd251c3994ac87fa0bf49bab8f917da5` |
| 21 | `papers/21-three-mode-hamiltonian-cubic-degree`; **Three-Mode Hamiltonian Shears in A6: Exact Degree Growth and Cubic Perron Subfamilies** | `COMPLETE_LOCAL_FINAL_REVIEW_PASS`; 27-page candidate `b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3`; no external effect | build R2 `69f0c560443edbf3f718e47507081525ddd1f2caa383f6bfbd1ec9378cf6070a`; finalization `d489295621cf42a1595d419bea33d63fe98c5d4a95078ffe2500165b12433fd3`; manifest `1acf1f482673e8f7e6ea64d98cccf205a11c153ef29d6fc9c4f029bb2708a661`; terminal rebuild `935e434e8329489fdb6edd2f27323200e0af42c6819dcbc227bba7041140896a`; terminal review `207a9c4eb668b28cfa9b3098ed250a7bc203805892f5d94104f07b4b3a0f5134` |

Batch 05 has consumed all five planned positions: four projects end in local
anonymous release state, while Paper 19 ends only in its explicitly bounded
internal/reference state. This is not a claim that five papers are publication
candidates. No submission, upload, public hosting, repository push, external
message, or identity disclosure occurred. The synchronized closure documents
now require a fresh independent cross-paper audit; after that audit passes the
workflow pauses at 5 / 5. Paper 22 is not authorized.

## Batch-05 Final Audit Confirmation

Date: 2026-08-23 UTC

The fresh independent cross-paper closure audit is persisted as
`BATCH_05_FINAL_AUDIT.md`, SHA-256
`3e583ac5a989a689b93da3a6a6a74ac42e37f2caaa2b6601c7ca14e37d46de3e`
(17,937 bytes, 325 LF), ending exactly `BATCH05_FINAL_AUDIT_PASS`. It
independently rehashed Papers 17--21, all authoritative manifest/receipt and
terminal or bounded-closure evidence, the four synchronized closure documents,
all 80 candidate-registry local links, PDF identities and page counts,
temporary-root cleanup, and the no-external-effect boundary.

Accordingly, Batch 05 is closed at 5 / 5 in the precise portfolio sense used
above: Papers 17, 18, 20, and 21 have local anonymous terminal integrity PASS,
while Paper 19 has only `COMPLETE_BOUNDED_INTERNAL_SCOPE`. No fifth publication
candidate is implied. The workflow is paused with read-only archival
permission only; Paper 22 and every further batch, build, release, scientific
execution, or external action require fresh explicit user authority.
