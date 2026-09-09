# X2 primary-source check: PC424-L stabilization and finite detection

2026-09-09 UTC. Bounded nonauthor source check, not a mathematical
acceptance, universal novelty guarantee, or paper-admission decision.

## Outcome

No exact collision for the two claims below was located in the inspected
primary-source passages. Substantial method overlap was located and must
be subtracted: residue extraction of normal-form coefficients, Jacobian
trace formulas, and finite binomial matrices for quadratic dynamics are
classical. The candidate contribution is the specific across-period
stabilization identity and the resulting exact finite test, not that
infrastructure.

Recommendation: **PROCEED WITH CAUTION to the coordinator's source and
substantiality gate.** A numerical novelty score would suggest more
certainty than this bounded search supports, so none is assigned.
The unrestricted equality theorem is being searched separately by the
coordinator; this report covers only claims 2 and 3.

## Exact claims being compared

Input: [A1 proof package](../../a1_periodic_normal_form/PROOF_PACKAGE.md),
Sections 1–5, read in its 444-line version. Put
$k=\overline{\mathbb F}_p$, with $p$ odd, and $f=x^2+c$, with arbitrary
$c\in k$. These quantifiers are not replaced by a hyperbolicity,
separability, generic-parameter, or prime-to-$p$ assumption.

**Claim 2 — exact carry-coefficient stabilization.** In

$$A_n=k[X_0,\ldots,X_{n-1}]/(X_i^2+c-X_{i+1}:i\bmod n),$$

let $P_E=\prod_{i\in E}X_i$, $P_{\rm all}=\prod_iX_i$ and
$H_n(v)=\sum_i v(X_i)$. For an odd degree cap $D$, put
$m=\lfloor\log_2D\rfloor$ and let $E_D$ be the support of its binary
digits. For $v\in k\oplus xk[x^2]$ of degree at most $D$, the claim is

$$C_{n+1}(v;E_D)=C_n(v;E_D),\qquad n\ge3m+4,$$

where $C_j(v;E_D)=[P_{E_D}](P_{{\rm all},j}H_j(v))$ is computed
in $A_j$ and $P_{{\rm all},j}=\prod_{i=0}^{j-1}X_i$.
The proof uses a weight-preserving insertion/deletion of a forced
$1\to1$ carry transition. It is not an asymptotic estimate.

**Claim 3 — exact logarithmic-degree finite detection.** If $\deg h\le M$,
$M\ge1$, set $n=3\lfloor\log_2M\rfloor+4$,
$F_j=f^{\circ j}-x$, and
$\widetilde H_j(h)=\sum_{s=0}^{j-1}h\circ f^{\circ s}$. Membership
$h\in\{Q\circ f-Q:Q\in k[x]\}$ is equivalent to

$$F_j\mid F_j'\widetilde H_j(h)\quad\text{for both }j=n,n+1,$$

and to vanishing of $\widetilde H_j(h)$ on all ordinary roots at both
levels. This is a two-level equivalence, not a claimed single-level
converse to Jacobian annihilation. A noncoboundary has a detecting
ordinary primitive period dividing $n$ or $n+1$, hence at most
$3\lfloor\log_2M\rfloor+5$. The iterate degrees are at most $32M^3$.
The tests use full return sums on all roots, not only cycles of exact
primitive length $n$ and $n+1$.

## Closest primary sources and exact interfaces

### S1. Normal forms, residues, and Jacobian traces

E. Cattani, A. Dickenstein, B. Sturmfels, *Computing Multidimensional
Residues*, arXiv:alg-geom/9404011 (1994 preprint; MEGA-94 proceedings,
1996). [Primary text](https://arxiv.org/pdf/alg-geom/9404011).

Read selected passages in §§0–2 and §4, especially (2.1), Lemma (4.2), Theorem
(4.3), and Algorithm (4.8), PDF pp. 13 and 19–21. For a zero-dimensional
system with monic pure-power initial forms $x_i^{r_i+1}$, (4.2) identifies
the global residue with the top normal-form coefficient. Theorem (4.3)
recovers every coefficient through the invertible residue-pairing matrix;
(4.8) computes $\operatorname{tr}(h)$ as the top coefficient of
$\operatorname{NF}(hJ)$.

Their initial setup is $K\subset\mathbb C$; Remark (1.6)(iii) discusses
extension to other fields. The cyclic quadratic leading forms satisfy
the same structural hypothesis. This does not license characteristic-$p$
specialization of every analytic formula. It is strong method overlap, not a
reason to claim the residue infrastructure is new. The inspected
statements do not compare different numbers of cyclic variables, prove
the forced carry insertion, or give the two-period certificate. Their
note added in proof also attributes earlier Euler–Jacobi vanishing to
Kreuzer–Kunz (1987); that attribution is not an independently read
Kreuzer–Kunz theorem here.

### S2. Quadratic finite matrices and weighted periodic traces

P. Cvitanović, K. Hansen, J. Rolf, G. Vattay, *Beyond the periodic orbit
theory*, Nonlinearity 11 (1998), 1209–1232; arXiv:chao-dyn/9712002.
[Author-hosted primary text](https://cns.gatech.edu/~predrag/papers/contourNonl.pdf).

Read the introduction, relevant passages of §§2–4 and the opening of §6. Section 3 uses
complex contour residues, initially taking fixed roots to be simple.
For quadratic $f$, the periodic traces involve
$\sum_{\operatorname{Fix}(f^n)}\Lambda^k/(\Lambda-1)$, where
$\Lambda=(f^n)'$. Section 4, printed pp. 1215–1216, equations (25)–(28),
gives finite matrices with binomial/power-of-$c$ entries, an iterate
matrix recurrence, and finite determinants. The paper explicitly
credits Levin–Sodin–Yuditskii for the finite-matrix construction.

This is a serious algebraic-method antecedent. It does not, in the
passages inspected, state stabilization of A1's short-support
coefficient across $n,n+1$, or exact testing of individual additive
ordinary-cycle obstructions over $\overline{\mathbb F}_p$. An implication
from those trace identities to A1's conclusion would require a separate
argument; it has not been established by this search.

### S3. The credited 1994 antecedent: access limitation

G. Levin, M. Sodin, P. Yuditskii, *Ruelle operators with rational weights
for Julia sets*, J. Analyse Math. 63 (1994), 303–331,
DOI 10.1007/BF03008428.
[Publisher abstract](https://link.springer.com/article/10.1007/BF03008428).

The readable abstract assumes a rational map with nonempty normality
set consisting only of attracting basins and rational weight $Q$.
It studies $L_Qg(z)=\sum_{R(w)=z}Q(w)g(w)$ on locally analytic Julia-set
functions, eigenvalue equations and eigenfunctions. Do not silently
replace this condition by a different hyperbolicity hypothesis.

Full theorem text was inaccessible: the publisher page is subscription
only, its PDF endpoint failed, and the author-uploaded ResearchGate
copy did not provide a readable preview/download. An institutional
publication list confirms the bibliography but supplies no theorem
text. Thus no original LSY finite-matrix theorem number or complete
hypothesis list is certified here. S2, equations (25)–(28), is the
directly read source for the matrix formulas; S3 is its credited
antecedent. This unresolved access is an explicit search limitation.

### S4. A 2025 finite approximate Livšic theorem

R. Zou, H. Wei, *A finite approximate Livšic theorem for Anosov
diffeomorphisms*, J. Applied Analysis and Computation 15(4) (August
2025), 2185–2194, DOI 10.11948/20240420.
[Publisher primary text](https://www.jaac-online.com/data/article/jaac/preview/pdf/jaac-15-4-2185.pdf).

Read abstract, introduction, Theorem 1.1 and Proposition 1.1, printed
pp. 2185–2186, plus the opening of the proof in §3. Theorem 1.1 assumes
a transitive Anosov diffeomorphism of a compact manifold and a real
Hölder observable with bounded Hölder norm. Small periodic data through
a cutoff $\varepsilon^{-1/2}$ imply
$\varphi=u\circ f-u+h$, with controlled Hölder norms and
$\|h\|\le C\varepsilon^\tau$.

Overlap: finite periodic information quantitatively constrains a
cohomological equation. Difference: the conclusion is approximate,
the setting smooth/hyperbolic, and the cutoff depends on error. It is
not an exact finite-dimensional polynomial criterion in characteristic
$p$, does not have a polynomial degree parameter $M$, and supplies
neither adjacent-return tests nor A1's logarithmic bound.

### S5. O'Hare's 2025 finite periodic-data rigidity

T. A. O'Hare, *Finite Periodic Data Rigidity for Low-Dimensional
Hyperbolic Systems*, Ohio State University PhD dissertation (2025).
[Institutional primary text](https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1750628245070562&disposition=inline).

Read abstract, introduction, Theorems 1.1.1–1.1.2 (printed pp. 4–5),
and the circle-map proof strategy. Theorem 1.1.1 assumes a bounded
family of $C^2$ expanding circle maps with a fixed expansion lower
bound, a conjugate pair, and matching multipliers on
$\operatorname{Fix}(f^N)$. It constructs a smooth approximant to the
conjugacy with exponentially small $C^0$ error and nearby conjugate
maps in $C^1$. Theorem 1.1.2 is the corresponding result for a closed,
bounded family of area-preserving Anosov maps on $\mathbb T^2$, with
fixed homotopy class and stable/unstable data matching.

This is finite-data approximate rigidity, not exact additive
polynomial coboundary membership. The differentiability, family and
hyperbolicity assumptions cannot be dropped when comparing it with
A1's every-$p$, every-$c$ theorem.

### S6. Nearby non-Archimedean transfer-operator work

Y. Jiang, C. Wu, *Ruelle's Zeta Function for non-Archimedean Rational
Maps*, arXiv:2508.19374v1, 26 August 2025.
[Primary text](https://arxiv.org/html/2508.19374v1).

Read abstract, §§1–3, and Theorem 1.1. The displayed theorem is over
$\mathbb C_p$, assumes nondegenerate critical points with disjoint
critical orbits, and relates an inverse-multiplier-weighted periodic
series to a critical-orbit determinant. Section 3 proves the identity
by comparing rational coefficient functions with the complex result.
This is a characteristic-zero theorem as stated over $\mathbb C_p$;
the abstract's local-field extension is also explicitly
characteristic zero. No every-parameter ordinary additive cycle
criterion over $\overline{\mathbb F}_p$, or logarithmic-degree finite
certificate, occurs in these inspected statements. Non-Archimedean
terminology alone does not make it an applicable positive-characteristic
source.

### S7. Recent six-month discovery, abstract only

O'Hare's Georgia Tech seminar of 16 April 2026 advertises joint work
with J. DeWitt, S. Durham and J. M. Reber on finite Livšic for transitive
Anosov flows, with approximation error exponentially small in the
period cutoff. [Institutional seminar abstract](https://math.gatech.edu/seminars-colloquia/series/cdsns-colloquium/thomas-ohare-20260416).
This verifies a recent nearby announcement, not a full theorem or its
proof; no corresponding primary preprint was located in this check.
It should not be cited as proving or excluding an exact arithmetic
finite-detection theorem.

## Search ledger and coverage boundary

Search date: 2026-09-09. Recent-six-month interval: 2026-03-09 through
2026-09-09. The following literal formulations were among those run;
each claim had more than three technical formulations.

| Claim / scope | Query formulation | Outcome relevant to this report |
| --- | --- | --- |
| 2 | `"cyclic complete intersection" residue polynomial dynamics` | Mostly unrelated complete-intersection uses; no exact stabilization located. |
| 2 | `"quadratic map" "residue" "normal form"` | Many unrelated symplectic-map residue hits; not treated as Grothendieck residues. |
| 2 | `"cyclic" "binary carries" polynomial periodic points` | No matching theorem located. |
| 2 | `"cyclic" "residue" "quadratic map" stabilization` | No exact match located. |
| 2, arXiv 2024–2026 | `site:arxiv.org residue periodic points polynomial 2024 2025 2026` | Nearby complex-dynamics records; primary candidates screened by hypotheses. |
| 2, arXiv 2024–2026 | `site:arxiv.org "Grothendieck residue" "dynamics" "2024" "2025" "2026"` | No matching record returned. |
| 2, recent arXiv | `site:arxiv.org "cyclic" "residue" "periodic" after:2026-03-09 before:2026-09-10` | No matching record returned. |
| 3 | `"finite Livsic" "polynomial" "degree"` | No exact arithmetic finite-test theorem located. |
| 3 | `"Livsic" "positive characteristic" periodic polynomial` | No applicable theorem located. |
| 3 | `finite periodic tests polynomial coboundaries positive characteristic` | Mostly unrelated testing/finite-field topics. |
| 3 | `effective Livsic polynomial degree finite period bound` | Classical/analytic Livšic and unrelated period bounds; no exact match located. |
| 3, arXiv 2024–2026 | `site:arxiv.org "polynomial" "coboundary" "2024" "2025" "2026"` | No matching record returned in this batch. |
| 3, recent arXiv | `site:arxiv.org "finite Livsic" after:2026-03-09 before:2026-09-10` | No primary preprint located; S7 was found through the broader recent search. |
| 3, recent arXiv | `site:arxiv.org Livsic finite periodic polynomial`, with 183-day recency | Returned older or unrelated records too; dates were checked instead of trusting the filter. |
| 2, Scholar discoverability | `site:scholar.google.com "Computing Multidimensional Residues"` | Did not obtain a useful native theorem record. |
| 2, Semantic Scholar discoverability | `site:semanticscholar.org "Computing Multidimensional Residues"` | No useful exact record returned by the available index. |
| 2, Semantic Scholar discoverability | `site:semanticscholar.org "Beyond the periodic orbit theory"` | No useful exact record returned by the available index. |
| 3, Scholar discoverability | `site:scholar.google.com "finite Livsic"` | No useful native theorem record returned. |
| 3, Semantic Scholar discoverability | `site:semanticscholar.org "finite approximate Livsic"` | No useful exact theorem record returned. |

These were available-web-index searches, not exhaustive authenticated
Google Scholar or Semantic Scholar database searches. arXiv primary
texts were opened when located. Search results sometimes labeled old
papers as recently crawled/published, so actual paper dates controlled
the assessment. An empty query result is a retrieval limitation, not
evidence that a theorem does not exist.

The novelty-check skill's ML-venue checklist (ICLR/NeurIPS/ICML) has no
identified relevant arithmetic-dynamics target here; no blanket
conference coverage is claimed. Its cross-model API step was not run,
as that action is excluded by the current task contract. All substantive
comparisons above use primary theorem text, except the explicitly
marked publisher/seminar abstracts. No mathematical code, external
model call, Git action, manuscript/PDF edit, or shared-file change was
performed.

## Suggested source subtraction and admission language

1. Describe the general residue/trace and finite-matrix machinery as
   inherited. Cite S1 and S2, with S3 credited through its actual
   accessible interface. A new characteristic or notation is not,
   by itself, a new method.
2. State the narrow candidate delta precisely: the forced
   weight-one transition gives exact short-support stabilization
   between different full cyclic algebras; two adjacent Jacobian
   identities then separate the normal defect without dividing by a
   period or assuming reduced periodic schemes.
3. Treat the finite certificate as a same-theorem consequence. Do not
   turn the two-level equivalence into a false single-level claim, or
   turn an upper bound into an optimality claim.
4. Do not present smooth finite approximate Livšic results as either a
   direct collision or irrelevant background. Their problem template
   overlaps, while their hypotheses, error conclusions and degree
   dependence differ.
5. Safe conclusion: “The checked primary passages contain substantial
   antecedent machinery but no exact instance of the stated
   stabilization and logarithmic-degree two-return certificate.”
   Unsafe conclusion: “This is the first finite Livšic theorem,” or
   “No prior result can imply it.” Global source priority and
   substantiality remain separate coordinator decisions.
