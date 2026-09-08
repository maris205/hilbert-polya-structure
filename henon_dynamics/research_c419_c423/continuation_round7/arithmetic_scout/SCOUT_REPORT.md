# Seventh continuation: three arithmetic-dynamics contract screens

Date: 2026-09-08 UTC. These are **AI-generated research proposals**, not
user-authored claims, proved theorems, or admissions. This bounded lane screens
three complete questions, makes **zero deep proof attempts**, runs **zero
mathematical programs**, and recommends **zero immediate admissions**. The
batch remains 3/5 unless the coordinator independently changes it on other
evidence. No C number or manuscript is assigned here.

The initial local-attractor favorite was down-ranked after classical ownership
checking. TR7 has the strongest possible arithmetic increment but no bounded
closure mechanism. FC7 is an exact, substantive cancellation question, with an
unresolved source comparison as well as a mathematical gap. None justifies
starting a large census.

## 1. Frozen comparison

| Label | Full object and question | Residual increment after deduction | Screen outcome |
| --- | --- | --- | --- |
| AP7 | Effective complete minimal-component and basin classification for every rational integral parameter of a dissipative quadratic map over every odd local prime | Effective two-dimensional stable-graph construction, global gluing, and certified exhaustive component templates, **only if not already a short transfer of one-dimensional theory** | `HOLD_CLASSICAL_TRANSFER_RISK`; not a proof-ready survivor |
| TR7 | Classify the strong, degree-uniform nonperiodic canonical-height gap over the field of all totally real numbers for every rational parameter | A uniform lower bound including points on algebraic curves, or explicit nonperiodic small-height witnesses; neither periodic-point finiteness nor generic equidistribution suffices | `HOLD_NO_FULL_MECHANISM` |
| FC7 | Power cancellation for every sufficiently long ordinary orbit of a fixed integral Hénon map reduced modulo every odd prime | Deterministic nonlinear orbit correlation at the stated length scale, beyond finite-permutation and random-involution facts | `HOLD_SOURCE_AND_FEASIBILITY_GAP` |

All three retain native iteration time. AP7's residue depth and FC7's prime
are arithmetic parameters, not replacements for the iterate clock. All
ordinary affine points, including zero coordinates, are retained. There is
no scheme-multiplicity count or deletion of inconvenient cycles.

## 2. AP7 — effective dissipative local component classification

### Exact contract

For **every odd prime** \(p\) and **every** \(a\in\mathbb Q\cap\mathbb Z_p\),
set

\[
 T_{a,p}(x,y)=(a+p y-x^2,x),\qquad
 J_{a,p}=\{P\in\mathbb Q_p^2:\{T_{a,p}^{n}P:n\in\mathbb Z\}
                   \text{ is bounded}\}.
\]

The object is an automorphism over \(\mathbb Q_p\), but its inverse is **not**
an integral automorphism of \(\mathbb Z_p^2\). The full parameter input is the
prime and the numerator/denominator of \(a\), with denominator prime to \(p\).
There is no arbitrary, possibly noncomputable, \(p\)-adic coefficient oracle.
The clock is \(n\in\mathbb Z\); forward empirical distributions use the
unmodified time averages \(N^{-1}\sum_{n=0}^{N-1}\delta_{T^nP}\).

**Question.** Is there a terminating exact algorithm, uniform in these inputs,
which gives an exhaustive finite-template description of:

1. every periodic point in \(J_{a,p}\), with exact least period and a
   \(p\)-adic algebraic root-isolation description;
2. every infinite minimal component, as a nested intersection of explicitly
   specified residue-ball cycles, with its complete successor-period sequence
   and adding-machine conjugacy;
3. the attracting basin of each component inside \(\mathbb Z_p^2\), its
   normalized two-dimensional Haar measure, and the corresponding limit of
   forward empirical measures?

Here a *finite-template description* must be a finite list of explicit
formulas, allowed to use an integer shell index \(k\ge k_0\), together with a
proved rule for **every** index, a proved disjoint/exhaustive partition, and
effective parameter bounds. An algorithm that merely enumerates the next
finite quotient is not such an output. If this prescribed form fails for
some parameter, a rigorous obstruction and the necessary broader component
type answer the structural part negatively; they do not silently redefine
the output requirement.

### Sources and classical ownership deduction

[Allen–DeMark–Petsche](https://arxiv.org/pdf/1610.04271) supplies the global
bounded-set/attractor setup. In the accessed version, Theorem 18 equates
finiteness of \(J\) with bounded periods of periodic balls over **all** depths.
Theorems 20 and 22 treat two specified \(\mathbb Q_3\) parameter families;
§4.4 presents additional finite-level observations, not a general
classification. These statements and their example mechanisms are prior
ownership, not AP7's increment.

[Fan–Fan–Liao–Wang, §3.2, Propositions 3.3–3.4 and Theorems 3.7–3.8](https://arxiv.org/pdf/1511.04856)
records one-variable analytic cycle-lifting, minimal decomposition, and
odometer classification, explicitly citing earlier Fan–Liao results. All of
that is also deducted. The proposed stable-graph reduction from AP7 to this
class is an **unproved scout inference**, not a theorem read in either source.

The internal [C409–C413 scout, §D](../../../research_c409_c413/arithmetic/SCOUT_REPORT.md)
already rejected the general one-variable decomposition question. [C394](../../../henon_padic_symplectic_analytic_interpolation_route_a/RESEARCH_QUESTION.md)
owns the earlier near-identity symplectic interpolation/closure direction.
The retired [CT1 contract](../../continuation_round2/congruence_towers/FROZEN_CONTRACT.md)
is a further warning against claiming general \(p\)-adic counting rationality.
AP7's nonunit Jacobian distinguishes its setting from integral-automorphism
interpolation, but that distinction alone does not establish novelty.

### Cheap decisive test and replacement boundary

**Next diagnostic, not executed:** analyze a single general noncritical
residual cycle of \(x\mapsto a-x^2\pmod p\), with its length and unit
multiplier left symbolic. Determine whether the attracting inverse-limit
set admits an effectively computable one-variable analytic graph and return
map to which the complete cited decomposition theorem directly applies.
Treat residual cycles containing the critical point separately. This is an
ownership/graph-reduction test, not a \(p\le P\) or depth-\(K\) census.

If effective graph reduction plus the cited scalar theory supplies the full
output in a short argument, **reject AP7 as a classical transfer**. In
particular, a finite-versus-infinite criterion alone, one new \(\mathbb Q_5\)
example, or a list of residue periods cannot be promoted. Continue only if a
precisely identified effective gluing/termination problem survives the full
deduction. No such surviving problem has yet been proved to be substantial.

## 3. TR7 — strong totally-real height-gap classification

### Exact contract

For **every** \(c\in\mathbb Q\), let

\[
 F_c(x,y)=(y,y^2+c-x),\qquad
 \widehat h_c^{\pm}(P)=\lim_{n\to\infty}2^{-n}h(F_c^{\pm n}P),\qquad
 \widehat h_c=\widehat h_c^++\widehat h_c^-.
\]

Here \(h\) is the absolute logarithmic projective Weil height of
\([x:y:1]\); the normalization is fixed. Let \(\mathbb Q^{\rm tr}\) be the
field of algebraic numbers all of whose conjugates are real, and define

\[
 b(c)=\inf\{\widehat h_c(P):
       P\in(\mathbb Q^{\rm tr})^2,\ P\notin\operatorname{Per}(F_c)\}.
\]

The degree of \(P\), its field, denominator, and orbit period are **not**
bounded. The clock is the original forward/backward iterate index in the
height limits. No replacement by coordinate house or a periodic-divisor
pressure is permitted.

**Question.** Determine the entire rational-parameter zero locus
\(\{c\in\mathbb Q:b(c)=0\}\), with a terminating input-\(c\) decision and
the following exact witnesses:

- if \(b(c)>0\), output a positive rational \(\epsilon(c)\) and prove
  \(\widehat h_c(P)\ge\epsilon(c)\) for **every** nonperiodic
  \(P\in(\mathbb Q^{\rm tr})^2\);
- if \(b(c)=0\), give an explicit algorithm producing distinct nonperiodic
  algebraic points \(P_j\in(\mathbb Q^{\rm tr})^2\), with certified
  \(\widehat h_c(P_j)\le2^{-j}\).

This is a classification question, **not a conjectured identification of the
zero locus with a real horseshoe or maximal-entropy locus**. Such an
identification would itself require proof in both directions. Exact root
polynomials, real embeddings, and height-error certificates are required for
the zero-gap witnesses.

### Sources and classical ownership deduction

[Lee, Theorems A–B and Corollary 7.5](https://arxiv.org/pdf/1203.1224) gives
arithmetic equidistribution for generic small sequences associated to
strongly regular pairs; the accessed §7 identifies the archimedean measure.
This supplies a classical obstruction to a **generic** sequence of totally
real small points when the relevant measure is not supported in the real
plane. It does not by itself exclude a sequence contained in an algebraic
curve. The height normalization must also be compared before importing the
statement; no equality of differently defined heights is presumed here.

[Smillie–Buzzard, Theorem 14.2 and its cited BLS source](https://library.slmath.org/books/Book31/files/smillie.pdf)
relates maximal real entropy, real support of the equilibrium measure, the
bounded set, and reality of all periodic points. This is dynamical ownership,
not a construction of nonperiodic arithmetic small points. A separate
primary Bedford–Smillie PDF was located, but a targeted body fetch timed out;
the theorem locator actually read for this equivalence is the author survey.

Internally, [P62](../../../henon_full_horseshoe_algebraic_exhaustion/README.md)
already gives all-period totally-real periodic-point exhaustion for its
fixed horseshoe, and [primitive coordinate-height pressure](../../../henon_primitive_coordinate_height_flat_pressure/RESEARCH_QUESTION.md)
already separates bounded coordinate height from period entropy. Those
results are deducted. AF5-C is retired and is not reopened: changing
cyclotomic to totally-real **periodic points** would not be TR7. The proposed
increment is the strong nonperiodic height gap with unbounded degree.

### Cheap decisive test and replacement boundary

**Next diagnostic, not executed:** separate (i) a genuinely generic small
sequence, (ii) a sequence contained in one fixed irreducible algebraic
curve, and (iii) a proposed zero-gap construction near totally-real periodic
divisors. Test the diagonal first because reversibility makes it a natural
exceptional curve. Write the exact height comparison needed for case (i),
and identify an actual curve-level argument for case (ii). Merely observing
infinitely many totally-real periodic points does not establish case (iii):
the definition expressly removes them.

If the only new statement is the generic equidistribution corollary, **reject
that smaller statement**. If no curve-level uniform gap or explicit
nonperiodic zero-gap construction is available, stop with the full TR7
contract unclosed. Do not replace it with a finite-degree Northcott search,
one parameter, qualitative periodic-point finiteness, or a conductor bound.
This screen finds no mechanism closing all three cases.

## 4. FC7 — additive cancellation on actual nonlinear finite-field orbits

### Exact contract

Keep the **single integral map**

\[
 F_1(x,y)=(y,y^2+1-x).
\]

For every odd prime \(p\), reduce it on all of \(\mathbb F_p^2\). Let
\(\mathcal O=\{F_1^nP:0\le n<L\}\) be any ordinary cycle of exact least
length \(L\). For \(\xi=(r,s)\in\mathbb F_p^2\setminus\{(0,0)\}\), set

\[
 S_p(\mathcal O;\xi)=
 \sum_{(x,y)\in\mathcal O}\exp\!\left(\frac{2\pi i}{p}(rx+sy)\right).
\]

The clock is one map iterate and the sum contains one complete ordinary
cycle. There is no randomization, orbit weighting, selected prime subset,
extension-field limit, or replacement by a quantum trace.

**Question.** For every real \(0<\eta<1/2\), do there exist explicit
\(\delta(\eta)>0\) and \(C(\eta)>0\) such that, simultaneously for
every odd \(p\), every cycle with \(L\ge p^{1/2+\eta}\), and every nonzero
\(\xi\),

\[
 |S_p(\mathcal O;\xi)|\le C(\eta)Lp^{-\delta(\eta)}\ ?
\]

A full negative answer must exhibit an unbounded-prime obstruction to power
saving at some fixed \(\eta\), not a small-prime counterexample absorbed by
\(C(\eta)\). The square-root length scale is a **proposed research target**,
not a known threshold inferred from the sources. Existence or positive
density of cycles meeting the threshold is not asserted by the contract.

### Sources and classical ownership deduction

[Ostafe–Shparlinski, §2.1 and Theorem 4](https://arxiv.org/pdf/0902.3884)
proves orbit exponential-sum estimates for a specified triangular,
slow-degree-growth class. The hypothesis is substantive; \(F_1\) is not that
triangular construction. Their introduction also explains the loss incurred
by exponential degree growth in earlier methods. These general methods are
prior ownership, not an FC7 result.

The broader [Ostafe–Pelican–Shparlinski 2010 article](https://doi.org/10.1016/j.ffa.2010.05.002)
was verified by publisher metadata/abstract and the author's publication
list, but its exact theorem and length threshold were **not body-verified**.
Consequently this report does **not** certify that FC7 lies beyond every
existing general estimate. That comparison is a hard source gate.

[Roberts–Vivaldi, Theorem A and §3 discussion](https://arxiv.org/pdf/0905.4135)
is a theorem about a random-involution ensemble. Its period scale for the
two-involution Hénon model is not a deterministic correlation theorem for
each orbit of \(F_1\). The internal [C03 protocol](../../../next_paper_henon_candidate_search/code/c03_PROTOCOL.md)
already treats matched-reversibility statistics as a null model. No cycle
census or reidentification of that model would be a new increment. The
older Artin–Schreier quantum-trace stream also has a different observable;
FC7's proposal is ordinary-orbit Fourier cancellation, not a reused trace
construction.

### Cheap decisive test and replacement boundary

**Next diagnostic, not executed:** first obtain and compare the exact theorem
in the broader 2010 paper, including its dependence on orbit length, field
size, dimension and degree. If it already yields the displayed bound, reject
FC7 as a specialization. Otherwise write the shifted-phase moment argument
for the first four consecutive iterates with \(r,s\) symbolic, listing all
phase degeneracies and showing exactly where the standard argument stops.
No large-prime orbit enumeration is needed for that diagnostic.

A credible continuation requires either a new invariant-set incidence or
additive-energy estimate with the displayed power saving, or a genuine
unbounded-prime obstruction. Ordinary Weil bounds for a bounded number of
iterates, an unexplained random-model analogy, or a numerical cancellation
plot do not suffice. If the only accessible theorem needs much longer
cycles, do not quietly enlarge \(p^{1/2+\eta}\) or promote a finite-period
result; retain the full question as unclosed.

## 5. Limits, sources, and handoff

The [source audit](SOURCE_AUDIT.md) records actual sections and all 38 query
strings in 12 search-bearing calls, including two 190-day recency-filtered
queries. Search volume is a receipt, not evidence of exhaustive novelty.
Zotero/Obsidian and the named local literature/helper fallbacks were
unavailable. No source PDF was saved; no human-read attestation was created.

The governing batch workflow and the selected research-lit, idea-creator,
novelty-check and bounded ARS source-verification instructions were read and
used. They changed the outcome by enforcing full questions, local ownership
deduction, separate source/feasibility gaps, and a no-census stop rule.
`SOCRATIC-NON-GENERATION-EXIT: explicit_user_request` applies to the
coordinator's explicit request for three AI-generated proposals; no extra
full Socratic research pipeline was started.

Mathematical executions, old reruns, GPU jobs, paid API calls, and proof
packages: **0**. Shell reads/searches and document validation are
administrative only. Writes are confined to this directory, via
`apply_patch`; global state, admissions, prior packages and Git are unchanged.
All team slots were already occupied by disjoint assigned tasks, so no
conflicting subtask was spawned or assigned to the child reserved by the
coordinator.

Recommended handoff: retain these as bounded screens, **not** as three
survivors. AP7's short-transfer risk comes first if any follow-up is chosen;
TR7 needs a genuinely new strong-height mechanism; FC7 first needs the exact
general-source comparison. No further authority is needed merely to read
or adjudicate this report. None establishes Euler factors, root numbers,
automorphy, a target zeta identity, or a Hilbert–Pólya realization.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
