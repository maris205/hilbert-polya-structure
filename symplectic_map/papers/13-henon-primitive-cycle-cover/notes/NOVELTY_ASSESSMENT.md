# Novelty Assessment

## Verdict

**Adjudicated disposition:** GO_SOURCE_DESIGN_ONLY_WITH_PRESERVED_DISSENT.

**Current lifecycle:** `SOURCE_LOCKED_V2 / PENDING_INDEPENDENT_R2 / NO_CODE /
NO_RESULTS`.

The positive case is not that any individual tool is new. It is the
strengthened five-layer theorem package:

1. a monic finite-flat full fixed algebra;
2. the generic actual-period block and its finite-flat relative
   normalization across \(a=0\);
3. the cyclic quotient with exact affine scalar fiber;
4. full symmetric monodromy on primitive cycles;
5. two natural observables, \(\tau\) and \(\rho\), proved separately to be
   primitive coordinates.

The internal adjudicator scored novelty \(6.8/10\), standalone size
\(7.4/10\), and proof confidence \(0.74\). A dissenting audit scored novelty
\(4.5/10\) and standalone size \(3.9/10\), a STOP recommendation. Both
records are normative. This file does not average them into a fictitious
consensus and does not relabel the dissent as resolved.

After the adjudication, the search located the Endler--Gallas period-four and
period-six orbit-sum carriers, Zhang's cyclic-polynomial computations through
period nine, Morton's direct scalar fixed-field generators, and
Cantat--Dujardin's formal-period trace-spectrum rigidity. In light of these
closer precedents and the Round-1 review, the corrected conservative
author-side ranges are **novelty \(4.8\)--\(5.5/10\)** and **standalone size
\(4.5\)--\(5.5/10\)**. These are risk estimates, not replacements for either
preserved gate record, not averages, and not a new independent verdict.

The conservative source-stage conclusion is:

> The combined deformation/normalization/monodromy/two-coordinate package
> appears distinguishable from located prior art, with PC1 carrying most of
> the residual contribution, but its standalone novelty remains disputed.
> Independent Round-2 review must verify the corrected collision map and exact
> scalar inputs before any implementation or manuscript.

## What is not novel

No novelty credit is assigned to:

- Gröbner bases or standard monomial bases;
- dynatomic polynomials or formal-period Möbius inversion;
- scalar \(Y_1(n)\) and \(Y_0(n)\)/\(X_0(n)\) constructions;
- smoothness and irreducibility of unicritical dynatomic curves;
- the scalar full-centralizer/wreath monodromy theorem;
- normalization, excellence, miracle flatness, or Reynolds averaging;
- orbit sums, trace coordinates, multiplier polynomials, or primitive-element
  arguments as general techniques;
- Morton's scalar fixed-field generation by the multiplier for all \(d,n\),
  or by the orbit sum for \(d=2\);
- reconstruction of Hénon parameters from formal-period trace-spectrum
  multisets over finitely many periods;
- low-period Hénon orbital carriers built from the sum of orbit points,
  their carrier polynomials, and stability equations;
- cyclic-polynomial computation of Hénon onset/bifurcation equations in
  bounded periods;
- Hénon normal forms or multiplier rigidity;
- specialization of a subgroup into global monodromy as a method.

The phrase “method novelty” is forbidden.

## Component-level collision map

| Proposed component | Closest located prior art | Collision strength | Safe residual delta |
|---|---|---:|---|
| Full cyclic algebra \(B_n\), rank \(d^n\) | standard complete-intersection/Gröbner algebra | method collision | an explicit integral entry point for this exact two-parameter family |
| Scalar fiber \(Y_1(n)\) | Gao–Ou; Morton; scalar dynatomic literature | direct on the \(a=0\) fiber | proving that this fiber is exactly the fiber of the **relative normalization**, including no nilpotents |
| Scalar orbit quotient | Doyle–Poonen and dynatomic modular-curve literature | direct on scalar quotient notation and geometry | Reynolds-compatible deformation to the Hénon parameter plane |
| Scalar wreath monodromy | Morton 1998, with Fakhruddin 2014's arbitrary characteristic-zero-field restatement | direct | correct restriction from the scalar line to the two-parameter normalized cover |
| Formal versus actual period | Hutz and dynatomic-curve literature | direct warning | using the warning to define the generic idempotent before normalization |
| Hénon family context | Friedland–Milnor | foundational | one tightly normalized two-parameter degeneration, not arbitrary Hénon maps |
| Hénon formal-period trace spectra | Cantat–Dujardin (2026), Section 3.2 and Theorems A/3.7 | direct observable adjacency, different reconstruction problem | one fixed actual-period cycle field, not parameter recovery from finitely many period multisets |
| Hénon hyperbolic-locus monodromy | Arai | adjacent use of “monodromy” | algebraic finite-cover monodromy over parameter space, not symbolic horseshoe monodromy |
| Orbit sum \(\tau\) | Morton 1996, Corollary 3 (p. 335) and fixed-field statement (p. 336), for \(d=2\); low-period Hénon carriers | direct scalar-generator collision in degree two | two-parameter lift, uniform \(d\ge3\) proof, and integral characteristic polynomial |
| Pointwise derivative trace \(\rho\) | Morton 1996, Corollary 1 and pp. 335--336 | direct scalar-generator collision for every \(d,n\) | two-parameter lift and integral characteristic polynomial, not invention of a multiplier generator |
| Quadratic Hénon period-four carrier | Endler--Gallas 2002 | direct low-period observable collision | all-\(d,n\) field generation and integral normalization, not invention of the orbit-sum carrier |
| Quadratic Hénon period-six carrier/stability | Endler--Gallas 2004 | direct low-period observable/stability collision | separate generic primitivity of \(\tau\) and \(\rho\), not a new low-period carrier calculation |
| Hénon cyclic polynomials through \(n\le9\) | Zhang 2014 | direct bounded-period computational collision | uniform proof for fixed arbitrary \(d,n\), exact normalization, and irreducibility |
| Top-wedge characteristic polynomial | standard norm/characteristic-polynomial algebra | method collision | integral basis-free packaging over \(A\) |

## Primary-source roles

### Gao–Ou

Yan Gao and Ya Fei Ou prove smoothness and irreducibility for the affine
periodic dynatomic curves of \(z^d+c\), \(d\ge2\). This is a theorem input for
the scalar normal domain \(D_n\); it is not novelty evidence.

### Morton, Fakhruddin, and the scalar monodromy line

Morton (1998), Theorem D/Theorem 10, gives the exact all-degree product of
wreath groups for \(f^b(z)-z\); Fakhruddin (2014), Theorem 3.2, restates it
over every characteristic-zero constant field, which makes the geometric
group explicit. Gao's periodic-group table (2016, p. 39) is a later
cross-check.

Morton's 1996 article is also direct primitive-generator prior art.
Corollary 1 and pp. 322--323 cover the required irreducibility for
\(x^d+c\). On p. 336, for the scalar point function field
\(K_0=\mathbb Q(c,z)\), Morton proves

\[
 K_0^{\langle\sigma\rangle}=\mathbb Q(c,w),\qquad
 w=\prod_{i=0}^{n-1}f'(f^i(z)).
\]

Here \(w=\rho|_{a=0}\), so scalar fixed-field generation by \(\rho\) is
occupied for every \(d,n\). In degree two, Corollary 3 on p. 335 proves the
orbit-sum trace polynomial irreducible, and p. 336 states that the same fixed
field is generated by \(t=\sum_i f^i(z)=\tau|_{a=0}\). The 2011 corrigendum
repairs a finite-characteristic lifting argument in Theorem 15 and does not
retract these characteristic-zero fixed-field statements.

Full marked-point wreath equality in the two-parameter family is used only
as an auxiliary restriction/centralizer consequence; the advertised PC1
statement is the \(S_r\) action on cycles.

These statements prevent both a general trace-coordinate novelty claim and a
claim that the named scalar generators themselves are new.

### Doyle–Poonen

Doyle and Poonen treat dynatomic curves, including \(X_0(n)\), their
geometric irreducibility, and gonality in the unicritical setting. Their work
fixes the surrounding scalar modular-curve language. It does not supply the
two-parameter Hénon normalization theorem.

### Hutz

Hutz proves effectivity and multiplicity results for formal dynatomic cycles
for morphisms of projective varieties. This is background for the
formal/actual distinction. It cannot be cited as an exact-period Hénon cover
theorem.

### Friedland–Milnor

Friedland and Milnor supply the foundational classification and dynamics of
plane polynomial automorphisms. The present family is a narrow normalized
family within that world. Their work forbids positioning the project as a
general Hénon classification.

### Cantat–Dujardin (2026)

Section 3.2 defines \(\operatorname{Trace}_n(f)\) as the length-\(p_n\)
multiset of \(\operatorname{tr}(D_zf^n)\) over formal-period-\(n\) points,
with their scheme-theoretic multiplicities. Theorem A says that a complex
Hénon map of fixed degree is determined up to finitely many choices by its
trace spectrum (or unstable-multiplier spectrum). Theorem 3.7 strengthens the
trace statement uniformly: there are \(P,N\), depending only on the degree
(or multidegree), such that equality of \(\operatorname{Trace}_n\) for all
\(n\le P\) leaves at most \(N\) maps; the statement holds over every
algebraically closed characteristic-zero field. For compositions, the
multi-Jacobian is fixed as specified in their parameter space.

This is direct adjacency to \(\rho\), but not a theorem collision. Their
target is reconstruction of the map parameters from whole formal-period
trace multisets across finitely many periods. PC2 fixes one actual period,
chooses the corresponding generic cycle field over the parameter base, and
asks whether the value of \(\rho\) at one cycle generates that degree-\(r\)
field. Neither statement supplies the other. Their paper also does not state
the finite-flat normalization or exact \(a=0\) fiber in PC1.

### Ji–Xie (2026) and Arai

Ji and Xie prove broad 2026 genus/gonality results for dynatomic curves of
one-parameter endomorphism families, with higher-dimensional analogues under
hypotheses. This is a frontier geometry neighbor, not the present
two-parameter affine normalization theorem.

Arai studies symbolic monodromy of the complex Hénon hyperbolic horseshoe
locus. The object, base locus, and permutation representation differ from the
finite algebraic cycle cover here.

### Endler--Gallas and Zhang: direct low-period Hénon carriers

Endler and Gallas (2002) parameterize every period-four orbit of the
quadratic Hénon map by the sum of its four orbit points and derive the cubic
equation satisfied by that sum. Their 2004 paper uses the period-six orbit
sum as a carrier and writes both the carrier and stability equations. Zhang
(2014) develops cyclic-polynomial equations for onset and bifurcation
parameters, including Hénon periods through \(n\le9\).

These are direct precedents for using \(\tau\)-type carriers and low-period
stability/trace information. Together with Morton, they mean the project does
not claim invention of \(\tau\), \(\rho\), their scalar fixed-field roles,
carrier polynomials, or cyclic-polynomial elimination. The residual claim is
the relative normalization/monodromy package, the two-parameter lift, uniform
\(\tau\) treatment in all degrees, and integral characteristic-polynomial
packaging.

## The five-layer delta

### Layer 1. Integral full fixed algebra

This layer is technically useful but has little independent novelty. Its role
is to make all later ranks and specializations integral rather than
set-theoretic.

### Layer 2. Generic actual block and relative normalization

This is the first plausible contribution. The generic actual-period
idempotent is normalized back over the full \(a,c\)-plane, and the proof
crosses the noninvertible \(a=0\) divisor without claiming an embedded
actual-period family.

### Layer 3. Exact affine scalar fiber and cyclic quotient

The scalar curves themselves are prior art. The proposed delta is the exact
scheme-theoretic identification

\[
S/aS=D_n,\qquad S_0/aS_0=D_n^{C_n},
\]

proved through a unique unramified height-one prime and normality, rather than
declared by notation.

### Layer 4. Full \(S_r\) cycle monodromy

The scalar wreath theorem is prior art. The proposed delta is its transfer to
the normalized two-parameter cover with the restriction direction and
time-shift centralizer both explicit.

### Layer 5. Two primitive coordinates

Neither observable nor scalar fixed-field generation is new: Morton gives
\(\rho|_{a=0}\) for every \(d,n\), and \(\tau|_{a=0}\) for \(d=2\). The
proposed delta is narrower: lift each observable to the two-parameter generic
cycle field, prove \(\tau\) uniformly for every \(d\) (with genuinely needed
\(d\ge3\) work), and package both multiplication laws as monic, integral,
basis-free characteristic polynomials in \(A[T]\). The \((2,2)\) case is
only a degree-one boundary.

## Why the package may be standalone

The historical adjudicator's \(7.4/10\) size score treats PC1 as the dominant
theorem and PC2 as one supporting theorem. The corrected author-side size
range is \(4.5\)--\(5.5/10\), because much of PC2 is now recognized as a
two-parameter lift of direct scalar prior art. The paper would still have a
complete progression:

\[
\text{fixed algebra}\to
\text{actual field}\to
\text{normalization}\to
\text{scalar fiber}\to
\text{quotient}\to
\text{monodromy}\to
\text{coordinates}.
\]

The dissenting \(3.9/10\) score instead treats most layers as standard
consequences once the scalar theorem is imported. That objection remains
live. The safe response is a proof-complete specialist paper, not broader
claims, more observables, numerical tables, or an arbitrary-Hénon extension.

## Search protocol

### Phase A — direct and component search

The search used exact-family and component queries across:

- Hénon dynatomic/periodic-cycle covers;
- quadratic Hénon period-four and period-six orbit-sum carriers;
- cyclic-polynomial Hénon computations through bounded period;
- relative normalization at the scalar degeneration \(a=0\);
- exact-period and formal-period dynatomic schemes;
- unicritical wreath/centralizer monodromy;
- \(Y_1(n)\), \(Y_0(n)\), and \(X_0(n)\);
- orbit sums, scalar fixed-field generators, trace spectra, multipliers, and
  derivative traces;
- 2024–2026 Hénon trace-spectrum and dynatomic-geometry frontiers.

Queries included variants of:

- “Hénon dynatomic curve primitive cycle cover monodromy normalization”;
- “primitive cycle Hénon algebraic cover monodromy”;
- “derivative trace Hénon cycles primitive element”;
- “Morton fixed field multiplier orbit trace dynatomic”;
- “Hénon formal period trace spectrum finite determination”;
- “Hénon orbit sum period 4 carrier cubic”;
- “Hénon period 6 orbit sum stability polynomial”;
- “Hénon cyclic polynomials period 9”;
- “\(x^d+c\) dynatomic Galois group centralizer wreath product”;
- “relative normalization dynatomic special fiber Hénon”;
- “2026 Hénon multiplier rigidity dynatomic”.

Primary or authoritative records were opened wherever available. Exact
source metadata and claim-safe roles are recorded in
CITATION_VERIFICATION.md.

### Phase B — adversarial novelty audit

The audit explicitly challenged:

- whether scalar irreducibility already makes the two-parameter result
  automatic;
- whether full monodromy is only a restatement of the scalar theorem;
- whether \(\tau\) is an established trace coordinate;
- whether \(\rho\) adds a genuine theorem or only a routine primitive-element
  consequence;
- whether Morton's scalar fixed-field theorem already occupies the advertised
  generator claim;
- whether Cantat--Dujardin's formal-period trace-spectrum reconstruction was
  being blurred with single-cycle-field primitivity;
- whether the package is large enough without new asymptotic, arithmetic, or
  compactification results.

This phase produced the preserved STOP scores \(4.5/10\) and \(3.9/10\).
The adjudicator's GO scores \(6.8/10\) and \(7.4/10\) came only after the
five-layer theorem and all proof bridges were added. The later Round-1 source
review located the stronger Morton and Cantat--Dujardin comparisons, leading
to the current author-side \(4.8\)--\(5.5/10\) novelty and
\(4.5\)--\(5.5/10\) size ranges without rewriting either historical record.

### Phase C — independent cross-model novelty

BATCH_04_STATUS.md records cross-model upload as disabled for this batch.
No independent cross-model Phase C was run, and none is simulated in this
file. The preserved blind/dissenting and adjudicator records are the available
independent-family checks. Independent Round-2 source review remains required.

## Family coverage and criteria binding

- Literature families covered: unicritical polynomial dynamics and scalar
  fixed-field generators, general dynatomic/formal-period theory, plane
  polynomial automorphisms, low-period Hénon orbit carriers and cyclic
  polynomials, complex Hénon monodromy, and current Hénon trace-spectrum
  rigidity.
- Retrieval/model coverage: one search stack plus the preserved internal
  audits; cross-model coverage unavailable.
- Venue criteria: no target venue or formal acceptance rubric was supplied.
  Therefore criteria_binding_unavailable is the only valid criteria status.
- Literature cutoff: 2026-08-16.

## Bounded absence statement

Within the recorded searches through 2026-08-16, no source was located that
states the exact conjunction:

> for \(H_{a,c}(x,y)=(a y+x^d+c,x)\), the generic actual exact-\(n\) block
> has a finite-locally-free geometrically integral normalization over
> \(\mathbb Q[a,c]\) with exact scalar dynatomic fiber, affine cyclic quotient
> of rank \(r\), full \(S_r\) cycle monodromy, and both \(\tau\) and
> pointwise derivative trace \(\rho\) separately primitive.

This is a bounded no-hit statement. It is not proof of absence, novelty, or
priority.

## Safe positioning

Use formulations such as:

- “We prove, for the normalized two-parameter family …”
- “The contribution is the combined relative-normalization package …”
- “The scalar dynatomic and wreath theorems are imported inputs …”
- “Morton's scalar generator theorems are prior art; the remaining PC2 claim
  is their two-parameter lift, uniform \(\tau\) treatment, and integral
  characteristic-polynomial package …”
- “The two observables are separately primitive on the two-parameter generic
  cycle field …”
- “Low-period Hénon orbit-sum carriers are prior art; the claim here is
  uniform field generation on the normalized cover …”
- “The exact scalar-fiber identification requires an \(a\)-adic divisor
  argument …”

## Forbidden positioning

Do not use:

- “first” or “previously unknown” without a new independent priority audit;
- “new dynatomic curve,” “new wreath monodromy,” or “new trace method”;
- “first Hénon orbit-sum carrier,” “first cyclic Hénon polynomial,” or
  “invention of the \(\tau\)/\(\rho\) carrier”;
- “first scalar primitive multiplier/orbit-sum generator”;
- “first trace-spectrum reconstruction of a Hénon map”;
- “all Hénon maps” or “arbitrary generalized Hénon family”;
- “actual-period scheme over every parameter”;
- “every fiber is smooth/reduced”;
- “free cyclic action everywhere”;
- “methodological novelty”;
- “no prior work”;
- “the dissent was resolved.”

## Gate conclusion

The corrected v2 package may proceed only to independent Round-2 source
review. That review must:

1. verify the all-\(d\) scalar monodromy attribution;
2. verify Morton's scalar fixed-field generators and distinguish them from
   the residual two-parameter PC2 claim;
3. verify Cantat--Dujardin's formal-period multiset/finite-period
   reconstruction statement and the noncollision boundary;
4. compare the exact five-layer conjunction against the primary sources;
5. retain both historical score pairs and the corrected ranges in its report;
6. decide whether the strengthened package clears the desired standalone
   threshold;
7. bind the v2 source-lock hashes and immutable Round-1 review.

Until that review returns SOURCE_LOCK_PASS, the novelty status is
**adjudicated GO with unresolved conservative dissent and a conservative v2
rescore**, not an unqualified novelty pass.
