# Experiment Plan: Closed-World Exact Audit of the Hénon Period-Three Residue Law

**Problem:** On the normalized Hénon family

\[
f_{m,a}(x,y)=\bigl(y+(x^m-a)^2,x\bigr),\qquad m\ge 2,
\]

certify the sharp normalized quartic fiber whose formal fixed-point trace
multiset is \(0^4\), together with its first separating period-three trace
moment, and certify the degree-uniform two-term formal
period-three residue law and its finite nested-binomial coefficient formula.

**Method thesis:** Two implementation-independent exact tracks—a quotient-
algebra/standard-monomial track and a global-residue/combinatorial track—
should agree on every frozen quartic identity.  For the two isolated finite
coefficient diagnostics, Track Q evaluates the pre-collapse certificates
(9.9) and (9.13) and inserts their result into (9.8), whereas Track R
evaluates only the collapsed formulas (9.27)–(9.28).  They share no
\(H\), \(A\), generalized-binomial, arithmetic-helper, or scientific-
intermediate implementation.  The sole preregistered tuple is
\(T_{\mathrm{reg}}=(8,9)\); agreement there can falsify an implementation
but is inadmissible as evidence for an all-\(m\) claim.  The symbolic theorem
is already source-proved, and no machine record may self-certify that proof.

**Date:** 2026-08-16 UTC

**Candidate ID:** `henon_period3_residue_v1`

**Authorization:** `SOURCE_DESIGN_ONLY / NO_CODE / NO_REGISTERED_EXECUTION`.

A fresh independent, final-hash-bound `SOURCE_LOCK_PASS` is required before
any executable candidate code is created.  A later independently reviewed
execution tree must receive `DEPLOYMENT_PASS` before the sole registered exact
audit.  This document schedules work; it reports no run result.

## Claim Map

| Claim | Why it matters | Minimum convincing evidence | Linked blocks |
|---|---|---|---|
| PC1. In the full normalized monic-centered quartic fiber whose formal fixed-point trace multiset is \(0^4\), every map is \(f_L=(y+(x^2-L)^2,x)\); period-one and period-two trace multisets are constant, while the formal exact-period-three second trace moment is \(-384(3375+4096L^3)\), so period three is the first separating period and gives an affine coordinate on this normalized conjugacy fiber. | This is the sharp, concrete theorem and prevents the family from being presented as an arbitrary example. | Two independent exact derivations of the fiber classification, normalized conjugacy criterion \(L^3=M^3\), formal-period lengths, low-period trace multisets, Step-10 zero fixed moment, Step-13 local fixed multiplicity, and the period-three polynomial, including a direct quartic slope ledger independent of the all-degree collapse. | B1–B3, B5 |
| PC2. For every symbolic integer \(m\ge2\), the formal period-three moment has the two-term shape \(S_m(a,\varepsilon)=C_m\varepsilon^{3m}+D_ma^{2m-1}\varepsilon^{2m}\), with the frozen finite nested-binomial formula for \(D_m\), and \(C_m=0\) for odd \(m\). | This is the uniform mechanism that makes the quartic theorem more than an isolated elimination. | A complete all-\(m\) source proof; two independent exact checks of the symbolic weight/support/range/sign contracts; and two independent finite certificate evaluators agreeing at the diagnostic-only tuple \((8,9)\), never a table-based proof. | B1, B4, B5 |

The `PC` prefix denotes a paper-level aggregate claim and cannot be confused
with the atomic IDs in `CLAIMS_EVIDENCE_MATRIX.md`. PC1 maps principally to
atomic C1--C7 and C14--C18; its Step-12 derivation is independent of C8--C13,
which provide a cross-check. PC2 maps to atomic C1--C14.

### Anti-claims that the audit must reject

- `UNIVERSAL_D_M_NONVANISHING`: the assertion \(D_m\ne0\) for every
  \(m\ge2\) is an open conjecture/nonclaim.
- `PERIOD3_SEPARATES_EVERY_M`: PC2 does not show that period three recovers
  \(a^{2m-1}\) at every degree.
- `NEW_QUARTIC_FAMILY` or `NEW_PERIOD12_BLINDNESS`: the quartic family and
  its period-one/two blindness are prior context, not the novelty claim.
- `ALL_QUARTIC_HENON_MAPS`: PC1 is about the normalized monic-centered fiber
  whose formal fixed-point trace multiset is \(0^4\), not every quartic Hénon
  map.
- `GLOBAL_P4_EQUALS_3`: no global period bound for all degree-four maps is
  claimed.
- `GLOBAL_CONJUGACY_CLASSIFICATION`: the criterion is for normalized
  polynomial conjugacy in the frozen family.
- Any global multiplier-rigidity, unstable/saddle multiplier, arithmetic
  height/finiteness, prime/zero, transfer/Fredholm, or Euler-product claim.
- Any inference from the historical development checks \(m=2,\ldots,7\) to
  an all-\(m\) theorem or to universal nonvanishing.

### Source-stage diagnostic disclosure

During repair of the source proof, before the proof subagent received the
instruction not to generate further finite values, it incidentally reran an
exact recurrence check at the already historical indices
\(m=2,\ldots,7\).  It reported no counterexample, retained no numerical
values, and checked no new degree.  This was a pre-lock, non-evidentiary
development diagnostic: it is not a tracker run, is not an input to either
future engine, and supports no theorem or nonvanishing claim.

The registered runtime counter
`historical_m2_m7_result_access_count = 0` has a deliberately narrower and
auditable meaning: the future candidate process must not read, import,
recompute, or receive those historical results.  The disclosed source-stage
event occurred before that candidate runtime exists and therefore does not
change the required runtime value; it is recorded here so that the provenance
statement does not imply that no development diagnostic ever occurred.

## Frozen Mathematical Objects

Work over characteristic zero.  Put

\[
q_i=2m x_i^{m-1}(x_i^m-a),
\qquad
F_i=(x_i^m-a)^2+\varepsilon(x_{i-1}-x_{i+1}),
\]

with indices in \(\mathbb Z/3\mathbb Z\), and define

\[
t_\varepsilon=
\det\!\left(\frac{\partial(F_0,F_1,F_2)}
{\partial(x_0,x_1,x_2)}\right)
=q_0q_1q_2+\varepsilon^2(q_0+q_1+q_2).
\]

The quotient by \((F_0,F_1,F_2)\) has the frozen monic standard basis
\(x_0^{e_0}x_1^{e_1}x_2^{e_2}\), \(0\le e_i<2m\), and formal rank
\((2m)^3\).  The registered trace/residue convention is

\[
S_m(a,\varepsilon)
=\operatorname{Tr}\bigl(M_{t_\varepsilon^m}\bigr)
=\operatorname{Res}_{F_0,F_1,F_2}(t_\varepsilon^{m+1}).
\]

At \(\varepsilon=1\), \(t_1\) is the trace of \(Df_{m,a}^3\) on the
formal period-dividing-three scheme.  Two different facts must remain
separate.  Step 10 proves zero **moment contribution**: on the fixed algebra
\(q^2=0\), \(t_\varepsilon=q^3+3\varepsilon^2q\), and
\(t_\varepsilon^m=0\) for \(m\ge2\).  Step 13 proves correct **cycle
multiplicity subtraction**: at a root \(\alpha\) of multiplicity \(r\),
formal elimination gives a remaining equation
\(3p(\alpha+\delta)+O(\delta^{2r-1})\), of order exactly \(r\).
Consequently the fixed locus has the same local length inside
\(\operatorname{Fix}(f^3)\), so no residual fixed support remains after
formal prime-period subtraction.  Neither statement substitutes for the
other, and no numerical root splitting is allowed or needed.

The coefficient certificate is frozen as

\[
H(r,k)=
\sum_{\substack{u+v=k\\2u\le r,\;2v\le r}}
\binom{k}{u}\binom{r}{2u}\binom{r}{2v},
\]

\[
A_{m,r}=\sum_{k=\lceil m/2\rceil}^{\min(m-1,r)}
(-1)^{r+k}\binom{m-1}{2(m-k)-1}H(r,k),
\]

and

\[
D_m=3\sum_{j=0}^{\lfloor m/2\rfloor}
\binom{m+1}{j}(2m)^{3m+3-2j}A_{m,m-j}.
\]

The equivalent factored record, used as an internal exact consistency check,
is

\[
E_m=\sum_{j=0}^{q}\binom{m+1}{j}(2m)^{2(q-j)}A_{m,m-j},
\qquad
D_m=3(2m)^{3m+3-2q}E_m,
\quad q=\lfloor m/2\rfloor.
\]

Every empty sum is zero.  For an arbitrary integer upper argument and
\(s\ge0\), the generalized convention used in (9.14) is

\[
\binom zs=\frac{z(z-1)\cdots(z-s+1)}{s!},\qquad \binom z0=1,
\]

and \(\binom zs=0\) for \(s<0\).  In particular, if \(z=n\ge0\), this is
zero for \(s\notin\{0,\ldots,n\}\).  The identity
\((-1)^s\binom{s-M}{s}=\binom{M-1}{s}\) is interpreted with this
generalized convention.  The exact local fiber identity to be anchored in P7
is

\[
\sum_{\substack{\ell,A,B\ge0\\\ell+A+2B=\alpha}}
(-1)^{\ell+B}2^A\binom N\ell
\frac{(n+A+B)!}{n!A!B!}
=(-1)^\alpha\binom{N-2n-2}{\alpha}.
\tag{9.14}
\]

Neither track may replace these rules or an empty range with implementation-
dependent truncation.

For \(m=2\), write \(a=L\).  The frozen expected identities are

\[
\operatorname{Trace}_1=0^{\times4},\qquad
\operatorname{Trace}_2=2^{\times12},
\]

\[
S_2(L,1)=-1296000-1572864L^3
=-384(3375+4096L^3).
\]

The latter is the pointwise formal exact-period-three moment (formal length
\(4^3-4=60\)); the optional cyclewise display is exactly one third of it.

### Frozen finite diagnostic tuple

The unique registered coefficient-check tuple is

\[
T_{\mathrm{reg}}=(8,9).
\]

It was frozen before candidate implementation and is disjoint from the
historical development tuple \((2,3,4,5,6,7)\).  Its sole purpose is to
falsify a transcription or implementation mismatch between the exact
pre-collapse coefficient ledger and its proved collapsed form at two
isolated, previously unused indices.  The pair exercises one even and one
odd \(m\), the same value \(\lfloor m/2\rfloor=4\) but adjacent values
\(\lceil m/2\rceil=4,5\), the \(j=0\) exceptional branch, and nontrivial
guarded ranges, without constituting or authorizing a scan.

At \(m=8,9\), Track Q evaluates \(\mathcal C_{m,j}\) before the local fiber
collapse by its private implementations of (9.9) and (9.13), checks those two
pre-collapse records against each other, and then applies (9.8).  Track R
independently evaluates only the collapsed guarded formulas (9.27)–(9.28),
including its own \(H/A/D/E\) and generalized-binomial primitives.  Neither
track runs the full high-degree quotient/residue engine.  Track Q must not
parse or call \(H\), \(A\), (9.27), or (9.28); Track R must not parse or call
\(\mathscr R_m\), the admissible tuples, \(\mathcal C_{m,j}\), (9.9),
(9.13), or (9.8).  No expected \(D_8\), \(D_9\), \(E_8\), or \(E_9\) value
may be stored in the source, schema, code, fixtures, or adjudicator-visible
input.

Only the final canonical \(D_m\) values, together with non-value structural
fields, cross the engine boundary for adjudication.  Agreement at
\(T_{\mathrm{reg}}\) can falsify an implementation mismatch but cannot prove
PC2, re-prove the Step-9 collapse, establish \(D_m\ne0\), estimate a trend,
validate \(C_m\), or authorize a neighboring index.  The all-\(m\) law and
coefficient identity remain proof-derived.

## Closed-World and Engine-Independence Policy

The audit has no dataset, split, random seed, fitted tolerance, floating-
point stage, GPU stage, or human scoring stage.  The bootstrap gate and
independent reviewers may bind or inspect the complete final source-lock
package.  A scientific engine may read only the definitions-only schema and
its own immutable private subtree; at runtime it may not read a source
document.  All scientific arithmetic is exact characteristic-zero
integer/rational/polynomial arithmetic.

The only schema shared by the scientific engines is definitions-only.  It
contains the candidate ID, characteristic-zero category, symbol names,
cyclic orientation, family and \(F_i/q_i/t_\varepsilon\) definitions, formal
period convention, allowed task IDs, \(T_{\mathrm{reg}}=(8,9)\), canonical
integer/polynomial serialization types, output field names, and nonclaim
tags.  It contains no expected quartic coefficient vector; no \(D_8,D_9\) or
\(E_8,E_9\); no \(H/A\) table; no recurrence, binomial, reduction, residue,
or coefficient-selection routine; no proof verdict; and no acceptance
predicate beyond data types.  Each track must transcribe its private
scientific route independently from the proof bound by the eventual source
lock.

The acceptance ledger is held by a noncomputing adjudicator and is opened
only after both tracks seal their canonical outputs.  Neither engine may read
it.  Echoing or parsing an expected output is a terminal hollow-validator
failure.  A machine may emit source-anchor presence, exact witness, and
consistency records for P1–P10, but it may not set a source theorem status,
issue `PROVED`, or replace the independent human/source review.  The only
authority for the symbolic proof is the final source package plus its
independent final-hash-bound review.

Forbidden inputs and operations include:

- network access and external prime, zero, orbit, multiplier, or modulus
  tables;
- a generated prime list, a new modulus, or any prime/zero/modulus scan;
- a loop over a selected range of \(m\), any index outside
  \(T_{\mathrm{reg}}\), or use of the registered tuple as evidence for PC2;
- loading the historical \(m=2,\ldots,7\) development outputs;
- numerical root finding, interpolation from sampled \(a\), approximate
  rational reconstruction, randomness, or tolerance-based equality;
- post-result formula, normalization, family, term, sign, or range changes;
  and
- use of one exact engine's intermediate output by the other.

Two exact tracks are mandatory:

1. **Track Q (quotient algebra / pre-collapse certificate):** monic leading-term/standard-monomial
   certificates; multiplication matrices and exact traces; Gröbner or
   border-basis normal forms for the quartic identity; subresultant/coefficient
   elimination for the fixed fiber; and direct affine-normal-form coefficient
   comparison for conjugacy.  Its finite PC2 diagnostic evaluates (9.9) by the
   terminating four-branch recurrence and (9.13) by a separate admissible-
   tuple enumerator, requires exact internal agreement, and combines the
   resulting \(\mathcal C_{m,j}\) through (9.8) at \(m=8,9\).  It does not
   implement or consume \(H\), \(A\), (9.27), or (9.28), and it does not run
   a full high-degree quotient computation.
2. **Track R (residue/combinatorics / collapsed certificate):** iterated global-residue/top-coefficient
   extraction with no multiplication matrix; root-multiplicity partitions for
   the quartic fiber; an explicit scaling conjugator and invariant argument;
   and a private direct guarded evaluation of (9.27)–(9.28), including its
   own \(H/A/D/E\) and binomial code, at \(m=8,9\).  It does not implement or
   consume Track Q's recurrence states, admissible tuples,
   \(\mathcal C_{m,j}\), or pre-collapse outputs.

Tracks Q and R may share only the definitions-only input schema and a
types-only final envelope schema.  They must not share arithmetic helpers,
generalized-binomial code, \(H/A\) logic, polynomial reduction, monomial or
tuple enumeration, coefficient selection, conjugacy logic, formula
rendering, caches, or scientific intermediates.  The schema parser may
validate types and fixed identifiers only; it provides no arithmetic.  Their
code-subtree hashes and dependency graphs must otherwise be disjoint.  The
adjudicator compares sealed canonical exact outputs but cannot repair either
output.

### Future candidate filesystem allowlist

No path below exists as authorized candidate code yet.  Before deployment,
the implementation review must bind exact files under these logical roots
and reject every path not enumerated in the deployment manifest:

| Process | Read allowlist | Write allowlist |
|---|---|---|
| bootstrap/hash gate | bound source files plus future `candidate_v1/manifest.json`, `candidate_v1/durable_claim.json`, deployment review, and `candidate_v1/shared/definitions.json` | abort/status channel only; no scientific result |
| Track Q | `candidate_v1/shared/definitions.json` and individually manifested leaves under `candidate_v1/track_q/` | fresh `candidate_v1/staging/track_q/` namespace only |
| Track R | `candidate_v1/shared/definitions.json` and individually manifested leaves under `candidate_v1/track_r/` | fresh `candidate_v1/staging/track_r/` namespace only |
| noncomputing adjudicator | `candidate_v1/shared/result_envelope.schema.json`, private `candidate_v1/adjudicator/acceptance_ledger.json`, and the two sealed canonical envelopes | `candidate_v1/staging/final/` namespace only |
| read-only result reviewer | sealed R100 artifact and bound manifests/reviews | append-only independent review artifact only |

The directory notation in the table describes future logical roots; R020
must expand them to a closed list of leaf paths and hashes, and runtime code
may not resolve an unmanifested wildcard.  The allowlist excludes repository-wide globbing, historical result
directories, scratch notebooks, caches, environment-derived data paths,
network resources, the other track's subtree or staging namespace, and the
adjudicator ledger from either scientific engine.  Every attempted read or
write is logged by canonical path before access; a disallowed attempt aborts
before a scientific field is emitted.

## Structural Proof Contract

Every item below is a MUST-RUN exact consistency check.  The source proof has
already discharged the mathematical obligations; machine calculations may
only witness that the frozen implementation follows them.  An engine cannot
self-certify the source proof, turn a missing source argument into a PASS, or
issue the source-level verdict.

| Contract ID | Required obligation | Terminal failure condition |
|---|---|---|
| P1 | State characteristic zero, the normalized family, Jacobian sign, cyclic orientation, and formal-scheme convention. | Any implicit change of category, sign, or period notion. |
| P2 | Prove the three \(F_i\) are monic in distinct leading variables and the quotient is free of rank \((2m)^3\); justify trace under specialization. | Rank inferred from generic numerical roots or a missing flatness argument. |
| P3 | Derive the displayed Jacobian formula for \(t_\varepsilon\) and the trace–residue identity with the exponent \(m+1\). | A sign mismatch, omitted \(\varepsilon^2\)-term, or use of \(t^m\) inside the residue. |
| P4 | With weights \(\mathrm{wt}(x)=1\), \(\mathrm{wt}(a)=m\), \(\mathrm{wt}(\varepsilon)=2m-1\), derive exactly the four a priori admissible monomials. | Monomial support obtained by interpolation or a degree scan. |
| P5 | At \(\varepsilon=0\), use the separated double-root algebra to remove the \(a^{3(2m-1)}\) term; then audit the complete Puiseux branch partition and valuation bounds that remove the \(a^{2(2m-1)}\varepsilon^m\) term. | A missing diagonal/non-diagonal branch, an unproved trace descent under ramified base change, or a finite-\(m\) substitute. |
| P6 | Derive reversal symmetry and \(C_m=0\) for odd \(m\), with the action on \(\varepsilon\), orientation, trace, and residue explicit. | Parity asserted only from examples. |
| P7 | Audit the complete Step-9 chain: reduction state (9.1); every base case in (9.2); all four signed branches in (9.3); strict termination and reduction-order independence via unique normal form/Laurent expansion; the pre-collapse recurrence sum (9.9); admissible tuples, constraints, weights, finiteness, exhaustiveness, and no-double-counting in (9.10)–(9.13); the generalized-binomial fiber identity (9.14) with its negative-upper-index convention; integrality congruence; the unique distinguished coordinate (9.17)–(9.19); the transfer-flow bijection, ranges, signs, and local factors (9.20)–(9.23); the empty-range case; both \(j=0\) incoming patterns and the vanishing exceptional pattern (9.25)–(9.26); and the final collapse (9.27)–(9.28).  Separately, at \(T_{\mathrm{reg}}\), Q must compute (9.9)/(9.13)\(\to\)(9.8), R must compute (9.27)–(9.28), with no shared \(H/A\), binomial, arithmetic, or intermediate code. | Any omitted base/branch/sign/range; nonterminating or order-dependent recurrence; unproved tuple exhaustiveness; ordinary-binomial treatment of a negative upper index; missing distinguished-coordinate/flow or \(j=0\) case; a machine claiming to prove the source theorem; assigned-degree substitution for symbolic \(m\); or shared scientific logic between finite evaluators. |
| P8 | Keep two obligations distinct.  **P8a / Step 10:** prove the fixed **moment** is zero because \(t_\varepsilon=q^3+3\varepsilon^2q\), \(q^2=0\), and \(t_\varepsilon^m=0\).  **P8b / Step 13:** prove the fixed support has the correct **local multiplicity** inside \(\operatorname{Fix}(f^3)\) by formal \((u,v)\)-elimination and the order-\(r\) equation \(3p(\alpha+\delta)+O(\delta^{2r-1})\).  Only then subtract lengths, obtain quartic exact length \(60\), and divide the pointwise sum by three for the optional cyclewise moment. | Treating zero moment as a proof of length, subtracting only reduced support, omitting the local order argument, or dividing by three before fixed subtraction and the pointwise identity. |
| P9 | Restrict conjugacy to the frozen normalized polynomial category; prove necessity and sufficiency of \(a^{2m-1}=b^{2m-1}\). | An appeal to an unstated global classification or necessity without an explicit sufficient conjugator. |
| P10 | Preserve \(D_m\ne0\) for all \(m\) as a nonclaim and tag all finite-degree development observations as non-evidentiary. | Any universal GO decision based on \(m=2,\ldots,7\) or another finite list. |

## Paper Storyline

Main paper evidence must contain:

1. the full normalized quartic fiber classification under formal fixed-point
   trace multiset \(0^4\);
2. exact normalized conjugacy and period-one/two blindness;
3. the two-engine quartic period-three separator;
4. the complete symbolic two-term residue law and finite coefficient
   certificate; and
5. explicit proof and reporting boundaries, especially universal
   nonvanishing.

Appendix-only evidence may contain complete quartic normal forms,
multiplication matrices, residue extraction ledgers, coefficient-selection
witnesses, code/environment hashes, and the cyclewise normalization.

Intentionally cut are all degree scans, new Hénon families, external data,
numeric orbit ledgers, high-period exploration, and every analytic/arithmetic
extension named in the anti-claims.

The simplicity/elegance check is protocol-level: the symbolic proof contract
is compared against the tempting overbuilt alternatives—finite-degree scans,
numeric root ledgers, interpolation, and a third tie-breaking engine—and each
alternative must be rejected.  The project is intentionally non-frontier;
there is no LLM/VLM/diffusion/RL component and therefore no frontier-
necessity block.

## Exact Audit Blocks

### B1: Structural proof-contract and definition audit

- **Claims tested:** PC1 and PC2.
- **Why this block exists:** every later exact identity depends on flat formal
  quotients, a fixed orientation, the trace–residue normalization, and a
  careful distinction between formal and geometric periods.
- **Input / split:** the final frozen source package only; no dataset and no
  train/validation/test split.
- **Task:** independently check P1–P10 against the final source files; emit a
  stable-ID dependency graph from assumptions through lemmas to PC1/PC2.  The
  record says whether each required source anchor and implementation witness
  is present; it cannot assign a mathematical proof verdict.
- **Compared checks:** source proof line-by-line audit; Track-Q algebra
  contracts; Track-R residue/combinatorial contracts.
- **Metrics:** exact/categorical PASS per contract; no aggregate score.
- **Setup details:** characteristic-zero symbolic arithmetic and stable source
  anchors only; no candidate substitution.
- **Success criterion:** every contract has explicit source anchors and exact
  witnesses; both tracks implement the same frozen definitions independently;
  the machine proof-verdict field is absent and the independent source review
  remains authoritative.
- **Failure interpretation:** source lock or implementation is unsound; stop
  before the registered audit.
- **Paper target:** proof-dependency table and notation box.
- **Priority:** MUST-RUN.

### B2: Quartic fiber, conjugacy, and period-one/two blindness

- **Claim tested:** PC1.
- **Why this block exists:** it establishes that the quartic curve is the
  whole normalized exceptional fiber and that periods one and two cannot
  separate its conjugacy classes.
- **Input / split:** one symbolic general monic-centered quartic and symbolic
  \(L,M\); no sampled parameters or data split.
- **Task:** start from a general monic centered quartic \(p\) in
  \(f_p=(y+p(x),x)\).  Track Q uses subresultants and coefficient elimination;
  Track R uses root multiplicity partitions.  Both must derive
  \(p=(x^2-L)^2\).  Independently derive
  \(f_L\sim f_M\iff L^3=M^3\), and compute formal period-one and exact-
  period-two trace characteristic polynomials.
- **Compared systems:** Track Q versus Track R only; there is no numeric root
  list.
- **Metrics:** exact fiber normal form; conjugacy invariant and explicit
  conjugator; formal lengths \(4\) and \(12\); characteristic polynomials
  \(T^4\) and \((T-2)^{12}\).
- **Setup details:** Track Q works through exact subresultants/quotients;
  Track R works through multiplicity partitions, resultants, and the explicit
  scaling action without importing Q records.
- **Success criterion:** the two tracks agree exactly on every field and the
  simple-root negative fixture is rejected.
- **Failure interpretation:** PC1 is not reportable and B3 is not
  interpretable as a sharp fiber theorem.
- **Paper target:** main Proposition/Theorem 1 and low-period table.
- **Priority:** MUST-RUN.

### B3: Quartic period-three separator

- **Claim tested:** PC1.
- **Why this block exists:** this is the first nonconstant moment on the
  frozen fiber and the paper's decisive explicit identity.
- **Input / split:** the symbolic quartic quotient with \(m=2\), \(a=L\),
  and \(\varepsilon=1\); no numeric \(L\) values and no split.
- **Task:** Track Q computes the exact quotient-algebra trace of \(t_1^2\)
  from a standard-monomial basis.  Track R extracts the normalized global
  residue of \(t_1^3\) directly and exposes the Step-12 tensor-Laurent slope
  ledger
  \(\mathcal C_{2,0}=-6\),
  \(\mathcal C_{2,1}=\mathcal C_{2,2}=0\), hence
  \(D_2=4^9(-6)=-1572864\), without calling the all-degree collapse.
  Each track separately verifies Step 10's zero fixed moment and Step 13's
  local fixed multiplicity by its own exact local-algebra/elimination route.
- **Metrics:** quotient rank \(64\); fixed length \(4\); local fixed lengths
  preserved at every multiplicity-\(r\) branch; exact-period-three length
  \(60\); independent direct slope \(-1572864\); pointwise moment
  \(-1296000-1572864L^3\); optional cyclewise moment
  \(-432000-524288L^3\); zero floating fields.
- **Setup details:** exact rational polynomial coefficients; Track Q uses
  standard-monomial trace and Track R uses normalized residue extraction.
- **Success criterion:** canonical coefficients, normalization, Step-10 zero
  moment, Step-13 local multiplicity, and all lengths agree across tracks;
  the Track-R slope ledger is independent of (9.27); and the nonzero \(L^3\)
  coefficient, combined with B2, proves exact minimal separation in the
  normalized fiber.
- **Failure interpretation:** any coefficient/sign/normalization mismatch is
  terminal for the registered candidate; no interpolation or third engine
  breaks the tie.
- **Paper target:** main Theorem 2 and one coefficient-extraction appendix
  table.
- **Priority:** MUST-RUN.

### B4: Symbolic general-\(m\) law and coefficient certificate

- **Claim tested:** PC2.
- **Why this block exists:** the uniform symbolic mechanism is the paper-size
  contribution beyond the quartic calculation.
- **Input / split:** a formal integer \(m\ge2\) and symbolic \(a,\varepsilon\)
  for the proof contract, plus the sole diagnostic tuple
  \(T_{\mathrm{reg}}=(8,9)\) for finite certificate evaluators; no data split.
- **Task:** the final source proof establishes the free quotient, trace
  identity, weighted support, separated-algebra degeneration, Puiseux
  valuation exclusions, reversal parity, and the complete Step-9 coefficient
  extraction listed in P7.  The machine only audits anchors and
  implementation consistency.  Track Q privately evaluates (9.9) and (9.13),
  requires their exact agreement, and combines the pre-collapse
  \(\mathcal C_{m,j}\) through (9.8) at \(m=8,9\).  Track R privately
  evaluates the collapsed guarded sums (9.27)–(9.28) at exactly the same two
  indices.  Neither runs a high-degree quotient.
- **Metrics:** categorical presence of every P7 source anchor; exact
  recurrence/admissible-tuple agreement inside Q; exact \(D/E\) consistency
  inside R; exact Q/R equality only at the final canonical \(D_m\) boundary
  for \(m=8,9\); parity and support consistency records; explicit empty-sum
  and generalized-binomial conventions; zero shared arithmetic/scientific
  helpers; and no stored expected integers.  There is no degree-range
  accuracy or source-proof score.
- **Setup details:** definitions-only shared schema; private Q and R
  scientific subtrees; guarded affine-in-\(m\) exponents; frozen generalized-
  binomial/empty-sum conventions; a runtime index allowlist containing only
  \(8,9\); and the filesystem allowlist above.  Q cannot resolve
  \(H/A/(9.27)/(9.28)\); R cannot resolve recurrence/admissible-tuple/
  \(\mathcal C/(9.8)\) symbols.  Full quotient/residue engines are disabled
  for these indices.
- **Success criterion:** the already closed source proof remains independently
  source-reviewed; both private finite routes agree at exactly \(8,9\);
  schema/allowlist/independence counters pass; no engine claims it proved the
  theorem; and neither finite record is cited as proof or as evidence for
  universal nonvanishing.
- **Failure interpretation:** retain only the portions proved by both tracks;
  a finite table cannot repair or promote PC2.
- **Paper target:** main uniform theorem and coefficient-certificate appendix.
- **Priority:** MUST-RUN.

### B5: Adversarial scope, independence, and lifecycle controls

- **Claims tested:** PC1 and PC2 plus every anti-claim.
- **Why this block exists:** a plausible-looking exact output can still arise
  from a sign error, period-convention error, shared engine path, or finite-
  sample overclaim.
- **Input / split:** exactly the eight frozen malformed request classes below;
  no generated fuzz cases and no data split.
- **Frozen negative controls:**
  1. omit \(\varepsilon^2(q_0+q_1+q_2)\) or use the wrong cyclic sign;
  2. request \(\operatorname{Res}(t^m)\) instead of
     \(\operatorname{Res}(t^{m+1})\);
  3. divide the pointwise moment by three before fixed subtraction;
  4. present \(p=x^4-x\) as having formal fixed-point trace multiset \(0^4\);
  5. replace normalized conjugacy by an unrestricted global claim;
  6. mark \(D_m\ne0\) universal because stored values at
     \(m=2,\ldots,7\) are nonzero;
  7. route a Track-Q intermediate, recurrence state, admissible tuple,
     \(\mathcal C_{m,j}\), arithmetic helper, or binomial helper into Track R;
     route Track-R \(H/A/E\), collapsed-form, or arithmetic output into Q;
     expose the adjudicator ledger to either engine; and
  8. request an index outside \(T_{\mathrm{reg}}\), a neighboring-degree or
     modulus list, an external prime/zero table, network access, numerical
     root solve, interpolation, or tolerance.
- **Metrics:** all eight fixtures rejected with the frozen reason code;
  independent subtree/dependency hashes; definitions-only schema inspection;
  canonical-path allowlist logs; machine-self-certification count zero; and
  all forbidden/shared-helper counters zero.
- **Setup details:** fixtures run before any registered scientific output is
  opened; rejection paths cannot call either scientific engine on a target.
- **Success criterion:** no negative fixture reaches a scientific result and
  no anti-claim is promoted.
- **Failure interpretation:** implementation or protocol failure; no
  registered execution.
- **Paper target:** limitations/provenance appendix.
- **Priority:** MUST-RUN.

## Exact Run Order and Stop/Go Gates

| Milestone | Goal | Runs | Stop/go gate | Cost | Principal risk |
|---|---|---|---|---|---|
| M0 | Freeze the source package | R000–R004 | final-hash-bound independent `SOURCE_LOCK_PASS`; otherwise no code | exact file/JSON checks, CPU seconds | source drift or hidden nonclaim promotion |
| M1 | Build and challenge two independent engines | R010–R019 | all proof contracts and adversarial unit fixtures pass; tracks have disjoint scientific dependencies | exact CPU, target under 30 minutes | nominally independent engines sharing logic |
| M2 | Freeze deployment | R020–R024 | independent code/tree review issues `DEPLOYMENT_PASS` tied to immutable hashes and the durable one-shot claim | review plus exact tests | hollow validators or post-lock mutation |
| M3 | Sole registered audit | R100 only | one atomic seedless execution of B1–B5; exact agreement yields provisional GO; any mismatch is terminal | exact CPU, target under 30 minutes | expression swell or normalization mismatch |
| M4 | Read-only result integrity | R110–R119 | certificates, hashes, counters, and scope pass without a scientific rerun | CPU seconds/minutes | unbound artifact or result-scope expansion |
| M5 | Manuscript handoff | R120 | only after independent `RESULT_PASS` and strict manifest closure | no new run | prose outgrowing certified claims |

The internal order of the atomic R100 transaction is frozen:

1. verify source, code, deployment-review, and durable-claim hashes;
2. run frozen negative controls before opening scientific output fields;
3. execute B1 proof-contract anchor/witness checks without a machine proof
   verdict;
4. execute Track Q for B2 and B3, then its private B4
   (9.9)/(9.13)\(\to\)(9.8) route at exactly \(8,9\);
5. clear Track-Q memory/output handles except its signed canonical result;
6. execute Track R for B2 and B3, including the direct Step-12 quartic slope
   ledger, then its private B4 (9.27)–(9.28) route at exactly \(8,9\);
7. compare canonical exact records without repair or fallback;
8. seal raw witnesses, counters, logs, and the one-shot transaction record.

If R100 fails, the candidate disposition is
`REGISTERED_AUDIT_TERMINAL_FAIL`.  The same registered claim may not be
rerun, patched, reparameterized, or adjudicated by exploratory calculation.
A materially new attempt would require a new candidate ID, new source lock,
and a new lifecycle outside this protocol.

## Must-Run versus Nice-to-Have

**MUST-RUN:** B1–B5; both independent tracks; all P1–P10 anchor/witness
contracts; the quartic pointwise identity; independent direct \(D_2\) and
local fixed-multiplicity records; the general symbolic coefficient
certificate; Q-pre-collapse/R-collapsed separation; negative controls;
source/deployment/result review gates; provenance, filesystem-allowlist,
machine-verdict, and forbidden-operation counters.

**NICE-TO-HAVE (appendix only, never a GO gate):** a compact human-readable
quartic multiplication-matrix ledger; a term-by-term residue witness; a
formally checked rendering of the already-proved binomial identity; the
cyclewise one-third display; exact time and peak-memory diagnostics.

**CUT:** any \(m\)-range scan (including rerunning \(m=2,\ldots,7\)), any
index beyond the isolated registered checks \(8,9\), any degree-based
nonvanishing conjecture score, extra Hénon parameters, high periods,
numerical plots, or external data.

## Compute and Data Budget

- GPU/accelerator hours: **0**.
- External data preparation: **none**.
- Network calls during development tests or R100: **0**.
- Random seeds and stochastic repetitions: **0**.
- Registered scientific executions: **exactly 1**.
- Registered finite certificate indices: **exactly \((8,9)\)** inside that
  one execution; no full quotient/residue calculation at either index.
- Expected exact CPU budget for R100: **under 30 minutes**; this is an
  engineering cap, not a mathematical threshold.
- Human evaluation: independent source, deployment, and result-scope review
  only; no subjective score enters a theorem gate.
- Biggest bottleneck: maintaining genuine independence between the quotient
  and residue/combinatorial derivations, not compute.

## Required Registered Counters

The raw result must assert and substantiate:

- `registered_audit_count = 1`;
- `registered_candidate_id_count = 1`;
- `exact_engine_count = 2`;
- `definitions_only_shared_schema_count = 1`;
- `shared_schema_scientific_field_count = 0`;
- `shared_scientific_implementation_count = 0`;
- `shared_arithmetic_helper_count = 0`;
- `shared_binomial_implementation_count = 0`;
- `shared_generalized_binomial_implementation_count = 0`;
- `shared_H_A_implementation_count = 0`;
- `cross_track_scientific_read_count = 0`;
- `track_q_collapsed_formula_access_count = 0`;
- `track_r_precollapse_formula_access_count = 0`;
- `engine_acceptance_ledger_access_count = 0`;
- `engine_source_document_access_count = 0`;
- `filesystem_read_outside_allowlist_count = 0`;
- `filesystem_write_outside_allowlist_count = 0`;
- `machine_source_proof_verdict_count = 0`;
- `floating_field_count = 0`;
- `random_seed_count = 0`;
- `network_access_count = 0`;
- `external_prime_data_access_count = 0`;
- `external_zero_data_access_count = 0`;
- `external_modulus_data_access_count = 0`;
- `new_modulus_scan_count = 0`;
- `degree_parameter_scan_count = 0`;
- `registered_coefficient_check_count = 2`;
- `registered_coefficient_check_order = [8,9]`;
- `registered_engine_index_evaluation_count = 4`;
- `full_quotient_residue_at_registered_tuple_count = 0`;
- `coefficient_check_outside_registered_tuple_count = 0`;
- `stored_D8_D9_expected_value_count = 0`;
- `stored_expected_E8_E9_count = 0`;
- `historical_m2_m7_result_access_count = 0`;
- `historical_source_stage_diagnostic_used_as_evidence_count = 0`;
- `numerical_root_solve_count = 0`;
- `interpolation_count = 0`;
- `post_result_retune_count = 0`;
- `universal_Dm_nonvanishing_claim_count = 0`;
- `period3_all_m_separation_claim_count = 0`;
- `global_quartic_or_conjugacy_claim_count = 0`.

## Failure Matrix

| Failure | Interpretation | Required action |
|---|---|---|
| Source/proof contract fails before deployment | theorem package is incomplete or inconsistent | repair source, issue a new lock/version, and obtain a new independent source review before code |
| Track Q and Track R disagree in development | at least one derivation is not trustworthy | stop; no majority vote, interpolation, or third-engine tie-break |
| Engine-independence audit fails | the advertised replication is not independent | refactor before deployment freeze |
| Q can resolve \(H/A/(9.27)/(9.28)\), R can resolve pre-collapse objects, or either engine reads a shared arithmetic helper/intermediate | the two finite certificates are not independent | stop before R100 and replace the candidate implementation under a new deployment hash |
| A machine emits a source-level `PROVED`/proof verdict | computation is being substituted for the source proof | invalidate deployment; only the independent final-hash source review may certify the proof |
| Any process touches a path outside its frozen allowlist | closed-world provenance has failed | abort before scientific output; no R100 authorization or salvage |
| Negative fixture is accepted | scope or definition guard is ineffective | stop before R100 |
| R100 coefficient, sign, rank, length, or normalization mismatch | registered theorem audit failed | terminal failure; no rerun in this lifecycle |
| Symbolic PC2 proof closes only after assigning finitely many \(m\) | no all-\(m\) certificate exists | do not report PC2; finite rows remain non-evidence |
| \(D_m\ne0\) is inferred universally | explicit anti-claim violation | invalidate the scientific report |
| Time/memory cap is exceeded without a mathematical mismatch | engineering limitation only | terminal incomplete result for v1; no simplified fallback run |
| Post-run scope audit expands the claim | provenance/interpretation failure | withhold manuscript handoff |

## Result Artifact Contract

The future sole raw result must contain:

1. immutable source-lock, code-tree, deployment-review, and durable-claim
   hashes;
2. separate `track_q` and `track_r` namespaces and dependency manifests;
3. P1–P10 categorical records with stable source anchors;
4. the quartic fiber, conjugacy, length, trace-multiset, fixed-subtraction,
   pointwise-moment, and optional cyclewise records;
5. the symbolic support/Puiseux/parity source-anchor records; the complete P7
   recurrence/base/four-branch/termination/order-independence/admissible-tuple/
   (9.14)/distinguished-flow/\(j=0\) witness ledger; separate Step-10 zero-
   moment and Step-13 local-multiplicity records; and separately namespaced
   Track-Q pre-collapse and Track-R collapsed certificate values at exactly
   \(m=8,9\), exposing only the canonical comparison boundary;
6. all adversarial outcomes, canonical-path access logs, the source-stage
   diagnostic disclosure binding, and required counters;
7. canonical exact integers/rationals/polynomials only; and
8. an explicit nonclaim ledger copied into the sealed artifact.

The post-run reviewer may validate hashes and check the sealed proof
certificates.  It may not choose new \(m\), \(a\), \(L\), signs, terms,
normalizations, or formulas, and it may not perform a second registered
scientific computation.

## Final Checklist

- [x] At most two primary claims are frozen.
- [x] Five core blocks or fewer are used.
- [x] The proposal is explicitly non-frontier and uses no forced frontier
  component.
- [x] Two exact, implementation-independent tracks are specified.
- [x] The shared engine schema is definitions-only and the future filesystem
  allowlist is explicit.
- [x] Quartic fiber, conjugacy, period-one/two blindness, and period-three
  identity are all covered.
- [x] The general-\(m\) law and nested-binomial certificate are symbolic,
  not scan-based.
- [x] P7 binds the complete recurrence-to-collapse proof chain and the
  generalized-binomial convention.
- [x] Step-10 zero fixed moment and Step-13 local fixed multiplicity are
  independent obligations.
- [x] Track Q uses only the pre-collapse finite route and Track R uses only
  the collapsed finite route; no scientific/arithmetic helper is shared.
- [x] The sole registered finite tuple \((8,9)\) is diagnostic-only and
  isolated from the historical development tuple \((2,\ldots,7)\).
- [x] Structural proof contracts and adversarial negative controls are
  explicit.
- [x] Universal \(D_m\) nonvanishing and all-\(m\) period-three separation
  remain nonclaims.
- [x] Historical \(m=2,\ldots,7\) checks are quarantined from evidence.
- [x] The incidental pre-lock \(m=2,\ldots,7\) source-stage recheck is
  disclosed, retained no values, and is distinguished from the required
  runtime access counter of zero.
- [x] Must-run and nice-to-have work are separated.
- [x] Exact run order and one-shot stop/go gates are frozen.
- [x] No candidate code or registered execution is authorized or reported by
  this planning artifact; the disclosed source-stage diagnostic is not
  candidate evidence.
