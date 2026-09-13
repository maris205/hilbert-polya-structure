# Candidate brief: local arithmetic of internal Lindstedt cancellation polynomials

Date: 2026-09-08. Version: V2.
Packet status: FROZEN_COMMON_CANDIDATE_INPUT_V2.
This is a selection document, not a manuscript, publication lock, page measurement,
formal Paper30 project or acceptance of a paper.
Route applicability: NOT_APPLICABLE: no Riemann determinant, arithmetic prime-orbit
clock, Hilbert–Pólya operator or target-zero claim is proposed.

## 1. A single stand-alone question

For the weighted two-harmonic twist map, consider the actual positive-frequency
diagonal jet in the uniquely normalized local periodic elimination problem.
At a prime-power rotation denominator, what is the local arithmetic decomposition
of the cancellation-parameter polynomial at the third internal small-divisor
position? Can its cancellation parameters coincide with those at either of the
first two internal positions?

The position is \(3p\), not perturbation order three and not the third full-system
resonance. The polynomial degree and the required recurrence length grow without
bound with the prime \(p\). The proposed contribution is an exact two-branch
arithmetic classification and pairwise disjointness for this specified polynomial
family. It is not a new general Newton-polygon method, and it does not claim a
classification of the final periodic resonance coefficients.

## 2. Actual object, normalization and coordinate dependence

Use momentum \(y\) here to avoid confusing it with the prime:
\[
 y'=y+\epsilon\sin q+2\lambda\epsilon^2\sin(2q),\qquad q'=q+y'.
\]
The action is the sum, not the average,
\[
 \mathcal A(q)=\sum_{j=0}^{s-1}
 \left\{\frac12(q_{j+1}-q_j)^2-\epsilon\cos q_j
                         -\lambda\epsilon^2\cos(2q_j)\right\}.
\]
For fixed coprime \(r,s\), impose
\(q_j=\theta+2\pi rj/s+u_j\) and \(\sum_j u_j=0\).
The transverse unperturbed Hessian is invertible. Its small analytic elimination
branch is unique for each fixed denominator and fixed parameter compact set;
no denominator-uniform analytic neighborhood is claimed.

Let \(t=\epsilon\exp(i(\theta+2\pi rj/s))\).
The part of \(iu_j\) whose perturbation degree equals its positive Fourier
frequency is \(v(t)\). Degree-frequency filtering of the actual equations gives
\[
 v_n=-\frac{[t^{n-1}]e^v/2+\lambda[t^{n-2}]e^{2v}}{D_n},
 \quad D_n=2-\zeta^n-\zeta^{-n},\qquad 1\le n<s.
\]
This is a unique triangular recurrence, not a polynomial manufactured from
desired roots. Source A01, Notation and Proof Steps 1–2, proves the identity.

Fix any prime \(p\ge5\), integer \(a\ge2\), and primitive \(p^a\)-th root \(\zeta\).
Work at the corresponding \(p\)-adic completion with
\[
 s=p^a,\quad h=2-\zeta-\zeta^{-1},\quad \rho=-h,\quad L=\rho\lambda,
 \quad K^+=\mathbb Q_p(h),\quad \mathcal O^+=\mathbb Z_p[h].
\]
Normalize \(v_h(h)=1\). Put
\[
 m=(p-1)/2,\quad M=p^{a-1}m=v_h(p),\quad D=3m+1=p+m,\quad
 \chi=(-1)^{m+1}.
\]
The residue field of \(\mathcal O^+\) is \(\mathbb F_p\).
Define the finite actual prefix by
\[
 V_n(L)=\rho^n v_n(L/\rho),\quad d_n=-D_n/h,\qquad
 d_nV_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V}.
\]
Negative coefficient indices mean zero; \(V_1=1/2\). Each coefficient extraction
uses only the necessary finite prefix. For \(k=1,2,3\), set
\[
 \mathcal B_k(L)=-[x^{kp-1}]e^V-2L[x^{kp-2}]e^{2V}
               =2d_{kp}V_{kp}.
\]
Since \(3p<p^a\), all these \(d_{kp}\) are nonzero. No actual internal mode has
been projected away or set to zero. The zero of \(\mathcal B_k\) therefore
cancels the specified diagonal jet coefficient, not the entire spatial harmonic,
the final resonant action term or an invariant under arbitrary symplectic
conjugacies.

The raw parameter polynomials obey
\[
 \mathcal B_k(L)=\rho^{kp-1}\mathcal B_{kp\mid p^a}(L/\rho),\qquad
 \mathcal B_{kp\mid p^a}=2D_{kp}v_{kp}.
\]
This invertible linear change preserves factor degrees, multiplicities,
splitting fields and common-root relations, whereas
\(v_h(\lambda)=v_h(L)-1\). “Positive” and “negative” clusters below refer
specifically to the declared \(L\) coordinate. A \(p\)-adic parameter root is
not being asserted to be an actual real bifurcation point.

## 3. Exact whole-package claims

Let \(S=h^{-D}p^2\mathcal B_3\). For every allowed \(p,a,\zeta\):

1. \(S\in\mathcal O^+[L]\) has actual degree \(D\) and a unique factorization
   \(S=P_{\rm cl}U_{\rm cl}\), where \(P_{\rm cl}\) is monic of degree \(m\),
   \(\overline P_{\rm cl}=L^m\), and \(U_{\rm cl}\) is of degree \(p\) with
   unit constant residue. The complete lower Newton polygon is
   \[
    (0,m-1)\longrightarrow(m,0)\longrightarrow(D,M-m).
   \]
   There are exactly two irreducible factors over \(K^+\), of degrees \(m,p\).
   Both are separable; thus the entire third polynomial is squarefree.

2. Each positive-cluster root \(\alpha_j\) has
   \[
    v_h(\alpha_j)=v_h(\alpha_i-\alpha_j)=(m-1)/m\quad(i\ne j).
   \]
   Let \(\kappa^m=-16\chi h^{m-1}\). Then
   \[
    E=K^+(\kappa)=K^+(\alpha_j)
      =\operatorname{Spl}_{K^+}(P_{\rm cl}),\qquad [E:K^+]=e=m,\quad f=1.
   \]
   This extension is cyclic and tamely totally ramified, and roots can be
   labeled \(\alpha_j=\omega_j\kappa+O(h)\), \(\omega_j\in\mu_m\subset K^+\).

3. Each of the \(p\) negative-cluster roots satisfies
   \[
    v_h(\beta)=-(M-m)/p,\qquad
    [K^+(\beta):K^+]=e=p,\quad f=1.
   \]
   These single-root extensions are wildly totally ramified. Their common
   identity, normality, full splitting field and Galois group are NOT determined.
   The compositum of \(E\) with any one of them has degree and ramification
   index \(mp\) and residue degree one; it is not identified as the full
   splitting field.

4. The three actual internal forcing polynomials are pairwise coprime:
   \[
    \gcd_{K^+[L]}(\mathcal B_i,\mathcal B_j)=1\qquad(1\le i<j\le3).
   \]
   This is stronger than merely excluding simultaneous vanishing of all three.
   The second polynomial has actual degree \(p\); a false smaller-degree
   argument is not part of this claim.

These are dependent conclusions of one structural theorem package.
They are not separate methods, independent research projects or grounds for
splitting the package into multiple papers.

## 4. Nonstandard coefficient inputs and standard consequences

The model-specific inputs include the exact normalization
\[
 \overline S=-3\chi L^m/64,\qquad
 S(0)=-3h^{m-1}/4+O(h^m),\qquad
 [L^j]S\in h^{m-j}\mathcal O^+\quad(1\le j<m),
\]
and the high-coefficient bounds
\[
 p[L^j]\mathcal B_3\in h^m\mathcal O^+\quad(j>m),\qquad
 p[L^j]\mathcal B_3\in h^{2m}\mathcal O^+\quad(p\le j\le D).
\]
The decisive high endpoint is
\[
 p[L^D]\mathcal B_3=-\frac3{16}h^p+O(h^{p+1}).
\]
Writing \(U_{\rm cl}=\sum_{r=0}^p u_rL^r\), these inputs yield
\[
 u_0=-3\chi/64+O(h),\quad
 v_h(u_r)\ge M-p\ (1\le r\le m),\quad
 v_h(u_r)\ge M-m-1\ (m+1\le r<p),\quad
 v_h(u_p)=M-m.
\]
The strict inequalities placing the intermediate points above the chord,
and the coprime horizontal/vertical lengths, then permit standard Newton
and ramification arguments. Those general arguments are not new.

The necessary earlier internal identities are
\[
 \overline{h^{-m}\mathcal B_1}=\chi(2-L^m),\qquad
 \overline{h^{-2m}p\mathcal B_2}=2,\qquad
 [L^p]\mathcal B_2=4\chi h^m+O(h^{m+1}).
\]
The highest-to-constant coefficient ratios of \(\mathcal B_2\) and
\(U_{\rm cl}\), after the common scale \(\chi ph^{-m}\), have residues \(2,4\).
This distinguishes two degree-\(p\) polynomials; irreducibility then excludes
their sharing a root. Irreducibility plus nonproportionality is standard;
the actual coefficient comparison is the object-specific input.

The exact valuation of \(S\) away from the two critical circles follows from
the Newton polygon, and at them from factorization. A23 Step 5 records it.
On the negative critical circle the full sum of distances to all negative
roots remains necessary. This short consequence does not solve their
unknown pairwise distances or add a new main proof block.

## 5. Current proof selection and complete author inputs

Sections 1–4 retain the exact original scientific claims. V2 selects nine
same-object proof replacements with their independently checked interfaces;
it does not add a theorem, relax a quantifier or change an error window.

The [current proof map](PAPER30_TWIST_INTERNAL_ARITHMETIC_CURRENT_PROOF_MAP_V2_20260908.md)
identifies each forward module, necessary author sections, shared lemmas and
superseded evaluations. The common manifest preserves A01–A23 and A01s and
provides exact author/report paths, hashes and permitted reading intervals.
The new source labels are:

| ID | Current author proof | Mathematical role |
| --- | --- | --- |
| F2 | Finite moments, typesetting V2 | Finite even-space construction, parameter-preserving translation and double-exponential interface; strict precritical moments. |
| O2 | Unified critical operator, typesetting V2 | Full formal averaged-weight identity, derivative elimination and true odd reflection defect. |
| R | Finite terminal recurrence V1 | The required critical scalar, replacing the selected use of O2 Step 7. |
| N | Factorial normal form V1 | One finite characteristic-zero algebra for both factorial bands, integral products, ordered actual entrances and original comparison precision. |
| T | Third first-layer operator V1 | Full-parameter reduction modulo \(H^2\), both top parameter moments and the complete third first-layer coefficient. |
| I4 | Minimal fourth-shift interface V1 | Full-parameter polynomial existence and coefficientwise remainder, with a direct proof of the required constant. |
| P | Parametric cross-adjoint V1 | Finite even/odd reflection and pairing with changing weights, transferring the complete quadratic endpoint to direct drivers. |
| E | Direct quadratic evaluation V1 | Both orders of the direct sources, zero term, two kernels and a legal finite single sum giving \(0,-1/2\). |
| M | First-forcing moment reuse V1 | Same-object amplitude identification and difference of two weights, using T's proved top moment for the first-forcing next layer. |

R denotes the terminal recurrence; T denotes the third first-layer operator.
M in this table is a source label, not \(v_h(p)\). O2's full averaged identity
is proved once and used in two distinct quotients: T's full-parameter
\(H^2\) section and the critical total-degree section. Neither quotient
identity is extrapolated to the other.

Retain A04's actual second-forcing endpoint and constant \(2\), both nonunit
entrances, the full A06 coupled response, A07's actual action/four-term
endpoint/legal shifts, A09's full-\(H\) exact response, and A08's full
model-degree and monic-factor arguments. N does not replace the actual
second endpoint; I4 does not prove model degree. T's top moments are not
inferred backwards from its final unit.

Retain all A14–A16 negative coefficient windows, A17's raw integrality and
pollution support before A18's finite reference and \(w_0,a_0,w_1,a_1\),
A19's full formal Ward identities, the entire A21 actual ghost mechanism,
and A22's accurate quadratic shifts/direct drivers and actual precision.
P/E replace the explicit quadratic zero-layer solutions and old six-kernel
evaluations. M replaces the specified next-layer odd-response/double-sum
evaluation, not the complete first-forcing identity. No additional T/A18
low-solution sharing has been established or assumed.

All replacements use the same actual prefix, parameter, finite windows and
coefficientwise precision. The linear \(-1/4\), quadratic \(-1/2\) and net
ghost \(0\) occur at the same \(H^p\) level; \(4^D=4\) in \(\mathbb F_p\),
including \(p=5\), gives the unchanged actual endpoint \(-3/16\) for A23.
This is not a combination of favorable outputs from different constructions.

Read the actual proof of every lemma used by the selected chain, including
its finite ranges, integrality and error estimates. A source map, accepted
status or reported check count cannot substitute for this reading.
A reviewer who finds a retained consumer requiring a supposedly superseded
step should identify it; the author selection is open to that challenge.

A01 supplies its actual diagonal identity, not root scans; A01s Step 1
supplies fixed-compact analytic elimination, not later parity or orbit
counts. Detailed first-layer Frobenius factor types, the noncore three
next-layer second moments, \(p\ge7\) root translation and finite \(p=5,7\)
tables remain excluded. They neither pad the body nor prove universal
quantifiers. Every necessary proof belongs in the substantive body.

## 6. Mathematical checks, conditions and correction boundaries

The [historical binding roster](PAPER30_TWIST_INTERNAL_ARITHMETIC_REVIEW_BINDINGS_20260908.md)
identifies eighteen nonauthor mathematical reports for A01–A23, their twelve
scoped dispositions and the actual earlier failures/corrections. It is a
historical evidence roster, not the current selection of necessary
evaluations. Its old requirements to retain replaced rational kernels or
explicit quadratic solutions are interpreted through the current proof map,
not silently made into new scientific locks.

The nine current proofs have the following distinct nonauthor checks. Exact
paths and identities appear in the manifest; these labels do not rename the
historical R01–R18. Read the complete allowed report portions supporting each
currently used lemma, not only the binding table or an acceptance summary.

| Current proof | Mathematical report | Exact scope and condition closure |
| --- | --- | --- |
| F2 | RF: POSITIVE_FINITE_MOMENT_INDEPENDENT_CHECK V1 | Checks F1's finite construction and parameter interface; V2 is the narrow typesetting successor described below. |
| O2 | RO: POSITIVE_UNIFIED_CRITICAL_OPERATOR_INDEPENDENT_CHECK V1 | Checks O1's averaged operator, derivatives and critical defect; the valid old Step 7 is not needed in the selected path. |
| R | RR: POSITIVE_TERMINAL_RECURRENCE_INDEPENDENT_CHECK V1 | Independently checks the terminal replacement; its operator and strict-precritical inputs are closed by RO and RF. |
| N | RN: FACTORIAL_BLOCK_NORMAL_FORM_INDEPENDENT_CHECK V1 | Checks both normal-form bands and prefix comparisons with the explicitly retained actual second-endpoint and coupled-response inputs. |
| T | RT: THIRD_FIRST_LAYER_OPERATOR_INDEPENDENT_CHECK V1 | Checks the \(H^2\) section and both top moments, with accepted F2, the full averaged identity and actual bridges. |
| I4 | RI4: FOURTH_SHIFT_MINIMAL_INTERFACE_INDEPENDENT_CHECK V1 | Checks full-parameter existence/precision and the scalar pairing, using its stated third-endpoint and bridge inputs. |
| P | RP: NEGATIVE_PARAMETRIC_ADJOINT_INDEPENDENT_CHECK V1 | Checks the general finite pairing and actual-driver interface, not E's subsequent evaluation. |
| E | RE: NEGATIVE_PARAMETRIC_ADJOINT_EVALUATION_INDEPENDENT_CHECK V1 | Checks both direct orders, kernels, finite sum and \(p=5\); its P condition is closed by RP. |
| M | RM: FIRST_FORCING_NEXT_LAYER_MOMENT_REUSE_INDEPENDENT_CHECK V1 | Checks identification, weighted-moment difference and actual transfer; T's top-moment input remains separately proved through RT. |

Three conditional consumer reports have narrower roles:

- D+ (POSITIVE_REPLACEMENT_DEPENDENCY_CHECK) checks the positive substitutions
  and raw-integrality-before-reference interface; RF and RR close its F and
  terminal conditions.
- DI4 (FOURTH_SHIFT_MINIMAL_INTERFACE_DEPENDENCY) checks that the selected
  consumers need only I4's stated interface; RI4 closes its mathematics.
- D− (NEGATIVE_ADJOINT_REPLACEMENT_DEPENDENCY_CHECK) checks the unchanged
  endpoint consumers and complete claims. RE and RM close \(C_E,C_M\), with
  RP and RT as separately checked upstream inputs.

The manifest provides precise permitted mathematical/binding portions of
the three replacement dispositions. No interface report is counted as an
extra mathematical vote, and none is claimed to recheck every upstream
proof. Historical conditional wording is retained, with its actual closure.
A permitted source's outgoing link does not authorize excluded evaluations.

F2 and O2 are typesetting successors, not versions directly audited by RF
and RO. F1 lines 90, 183 and 319 recover the command `\qquad`, line 198
recovers `\quad`; O1 lines 39 and 224 replace U+000C followed by `rac` with
`\frac`. Apart from version headings/explanations and those six repairs, the
dated body was verified unchanged. RO's literal typesetting FAIL remains
visible and is not retrospectively made PASS. The F1/O1 identities and the
accepted successor boundary are in the common input.

Accepted reading clarifications remain part of the proof:

1. For F2, a positive \(N\)-derivative of an ordinary polynomial carries
   \(G^2-1\), while \(q_0\) begins this property at its second derivative;
   \(Nq_0=G\) is the explicit exception and the relevant \(D_a\) have at least
   two derivatives.
2. Parameter-exponential differentiation uses \(N,\partial_G\), which
   preserve the parameter ideal. Auxiliary translations are proved
   coefficientwise before truncation as in RF Step 3. Arbitrary
   \(\partial_H,\partial_\tau\) are not asserted to descend to the quotients.
3. R's final positive-\(L\) disappearance refers to the adjacent total-degree
   range at most \(m\), not to every order.
4. P identifies a residual coefficient module with \(H^{2m}\mathscr R\);
   it does not invert the nonunit \(H^{2m}\) in the larger quotient. Its
   even constants and unneeded odd index \(m\) obey the finite restrictions.
   Ward remains a formal-\(H\) identity.
5. A19's first-forcing formal identity is A02 equation (15); A23's pure-even
   double-angle input is A16 Step 5, equations (20)–(21).

The original failed TOP_COEFFICIENT V1, the separate accepted A17 and the
noncore root-bound V1/V2 wording correction retain the distinct histories
specified by the old roster; none may be hidden or conflated.
For the superseded A22 six-kernel calculation, its adjoint-domain
clarification remains true: characteristic-zero convolution computes a
\(p\)-integral representative of a residue identity, not an exact
characteristic-zero identity for the original response endpoint. Current
P/E stays in its stated finite residue rings; changing the evaluation method
does not grant a stronger domain identity.

Existing reports support their exact mathematical portions, not candidate
novelty, value or body capacity. The fresh reviewers assess the complete
stated package with its selected proof. Auxiliary symbolic computations are
not substitutes for general proofs, and no old candidate assessment is an
input or a vote here.

## 7. Prior-art deductions and internal noncollision

The identical external sources for the reviewers are the
[bounded novelty preflight](PAPER30_TWIST_INTERNAL_ARITHMETIC_NOVELTY_PREFLIGHT_20260908.md)
and its
[independent boundary check](PAPER30_TWIST_INTERNAL_ARITHMETIC_NOVELTY_INDEPENDENT_CHECK_20260908.md).
Their conclusion is only NO_DIRECT_MATCH_IN_READ_SCOPE; GLOBAL_NOVELTY_UNCERTAIN.
Read the stated actual source-access limits, not just the conclusion.

Mandatory deductions include:

- Olvera's weighted Fourier setting, homological recursion and continuation
  after a leading resonant coefficient vanishes. Merely using different
  \(\epsilon\) weights or advancing beyond a cancellation is not new.
- Berretti–Gentile's Lindstedt/tree recursions, resonance cancellation and
  minimal-tree mechanisms. The presence of the same classical map is not
  novelty, and “use \(p\)-adic methods on this model” alone is not a contribution.
- General Newton/Hensel/Kummer and ramification theory, including the
  coprime-length single-edge irreducibility criterion.
- The existing two-harmonic standard-map literature on island chains,
  isochronous and shearless bifurcations.
- Djakov–Mityagin's double-harmonic Hill gap formulas and the Suris background.
  No parameter-preserving identity has been proved from their linear
  spectral/path objects or full integrable potential to the nonlinear
  internal forcing here. Neither transfer of their best result nor a
  categorical proof that no bridge can exist is claimed.

The bibliography distinguishes the EPJST article's 2025 online publication from
its 2026 volume assignment. Recent source queries and access limits are already
logged. A focused primary-source check is permitted if a reviewer identifies a
specific uncertainty; there is no need to repeat an unaltered broad search.

The same
[local noncollision report](PAPER30_TWIST_INTERNAL_ARITHMETIC_NONCOLLISION_CHECK_20260908.md)
is provided to both reviewers. Its six closest-paper matrix and supplementary
comparisons distinguish coefficient valuation from the support/degree Newton
polygons in Papers20–28 and from polynomial cohomology in Paper29.
It also records the actual earlier local-resonance and jet packages.
It is a bounded comparison of read statements, not an exhaustive theorem
search through all files.

The earlier \(p,2p\) final-forcing results and the \(B_1,B_2\) and positive-cluster
stages in this same twist research chain are genuine prior work within the
program. Necessary earlier lemmas enter this one proof package once.
No publication or extra contribution is manufactured by counting research
dates, repeated derivations, increasingly sharp old root bounds or checks.

## 8. Nonclaims and forbidden extensions

The package does NOT solve the final prime-power \(C,Q\), all denominators,
all real roots, every internal layer, the full negative splitting field,
negative pair distances or the second forcing's full polygon and simplicity.
None is secretly assumed by the stated central theorem.

The internal coefficients are not claimed to be arbitrary-coordinate
dynamical invariants, physical bifurcation parameters, integrability
obstructions or a classification of actual periodic-orbit splitting.
A future dynamical application would require a separate bridge controlling
all intervening contributions, not merely an observation that the recurrence
eventually reaches \(s\).

No fitted roots, parameter tuning with \(\epsilon\), post-hoc threshold changes,
combination of different constructions, new experiment or paid/external
operation is part of this candidate. The manuscript cannot be padded with
the excluded special cases, open directions, other stopped candidates,
source listings, audit histories or textbook treatments of standard tools.

## 9. Identical contract for two fresh, mutually blind candidate reviews

Each reviewer independently evaluates this exact entire package:

1. Novelty at least 7.5/10 after the mandatory prior deductions.
2. Stand-alone scientific value at least 7.5/10.
3. Complete-proof confidence at least 9/10 for the stated full quantifiers.
4. Credible natural capacity of 22–30 substantive English body pages.

Use anonymous single-column article, 11pt, letter paper, one-inch margins and
standard spacing for the capacity judgment. References start separately and
do not count. Give your own justified low/central/high table by necessary
mathematical block, remove duplication, and explain both insufficient and
excessive-length risks. Do not infer body capacity from Chinese source lines,
proof count, agent effort or the need to finish this batch.
If the complete result naturally belongs in a shorter article, fail this
locked capacity gate without denying its mathematical merits. If a complete
proof cannot credibly fit within the upper bound, report that failure too;
omitting necessary lemmas is not an acceptable compression.

Do not read the author-capacity file, author page allocation, earlier
candidate scores, the other current review, or communications reporting them.
The author value preflight and value/scope disposition are not needed for
your decision and are excluded from the common review input.
This brief contains no author's page estimate or desired score.
You may disagree with any prior bounded interpretation after examining the
actual evidence; report a concrete claim/source/quantifier mismatch if found.

The two reviewers must not be authors or previous mathematical auditors of
this package. Neither may read, discuss, infer or import the other's report.
Each owns one disjoint output file and discloses actual identity, tools and
read scope. Use xhigh reasoning as prescribed by research-review; the
specified GPT-5.4 MCP interface is not configured, so do not claim its use,
a human review or a cross-model certificate.
Progress messages may identify read scope and factual questions, but must not
circulate provisional scores or page estimates. Any substantive factual
clarification during the reviews must be supplied identically to both
reviewers. The released packet remains unchanged; a genuine correction
requires a separately identified successor and preservation of the original.

The final decision is the conjunction of all four gates in BOTH reports.
No averaging, best-component selection, construction mixing or repeated
submission of the same failed package is permitted.
The Paper29 special natural-draft measurement exception does not carry over.
A complete candidate PASS only opens the ordinary local manuscript workflow;
it is not a completed paper, PDF acceptance or authority for external effects.

## 10. Common input identity and reading boundary

The accompanying
[review-input manifest V2](PAPER30_TWIST_INTERNAL_ARITHMETIC_REVIEW_INPUT_MANIFEST_V2_20260908.md)
binds this brief, the current proof map, retained/replacement author sources,
their mathematical reports, consumer and acceptance boundaries, and the
unchanged bounded prior-art/noncollision evidence. Historical documents are
classified as current proof, scoped binding, or correction/background;
their presence does not make every historical result part of the theorem.

It records byte identity and exact reading intervals only, not scientific
truth, candidate acceptance or a manuscript source/publication lock.
Both reviewers receive the same manifest and its externally recorded digest.
The original files remain intact. A few administrative passages containing
prior candidate evaluations are excluded from permitted reading intervals;
no mathematical proof, failure, correction or condition is excluded for that
reason. The bounded prior-art deductions, source-access limitations and
scientific value risks remain visible, including unfavorable ones.

Neither this brief nor the current proof map supplies an author's page
allocation, target estimate, outline diagnostic or desired score.
No recursive permission follows from an outgoing link in a permitted file.
If a necessary scientific dependency is not covered by the allowed input,
request a factual clarification rather than importing excluded evaluations.
Any substantive clarification is sent identically to both reviewers and
recorded with the frozen input.
