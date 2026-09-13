# Publication-Stage Scope

Date: 2026-08-18 UTC

Candidate: marked_henon_scalar_boundary_v1

Canonical project: papers/18-marked-henon-scalar-boundary

Exact public title:

**Marked Trace Coordinates and Scheme-Theoretic Ramification at the
Polynomial Boundary of Generalized Hénon Maps**

Status after the paired publication lock is written:

**PUBLICATION_STAGE_LOCKED / PENDING_INDEPENDENT_PUBLICATION_REVIEW /
NO_DRAFT / NO_SOURCE_REVIEW / NO_BUILD / NO_FINALIZATION / NO_RELEASE**

## Purpose, authority, and present limit

This document is the human-readable publication-stage contract for one
anonymous, proof-first algebraic-dynamics article. It translates the passed
source design and paper plan into exact content, source, review, build,
universe, role, and closure rules. Its paired canonical authority is
experiments/publication_lock.json.

The present publication-stage author may create exactly two project files, in
this dependency order:

1. notes/PUBLICATION_STAGE_SCOPE.md;
2. experiments/publication_lock.json.

This scope must be stable, read to EOF, and hashed before the lock is written.
After the lock, the author may perform read-only validation and must stop. The
current stage authorizes no bibliography, TeX manuscript, code, scientific or
computational execution, data, result, figure, image, asset, compilation,
build, finalization, release, repository action, submission, upload, external
message, or identity disclosure.

The sole possible immediate successor is a fresh independent publication-stage
review at:

notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md

That path is absent at the publication-author stop. It may be written only
after the exact PUBLICATION AUTHOR STOP and only if every conjunctive check
passes. Its last nonempty line must be exactly:

**PUBLICATION_STAGE_PASS**

A blocker has disposition **WRITE NOTHING**. The reviewer may not repair,
draft, compile, build, self-sign, or expand its own universe. Even an exact
publication pass makes the project eligible only for a separately invoked
anonymous authoring episode for the two public source paths. It does not
activate source review or a build.

## Exact frozen input universe U_G15

The current project universe \(U_{G15}\) consists of exactly the following
fifteen regular non-symlink files. Every path, byte count, LF count, SHA-256,
and role is normative and is rebound by the canonical publication lock.

| Path | Bytes | LF | SHA-256 | Frozen role |
|---|---:|---:|---|---|
| experiments/EXPERIMENT_PLAN.md | 12,898 | 154 | 53a38842ca36ad57d84516dcc4761119a6db411ff998000dc53a6d890d2978a4 | Zero-science proof and editorial validation plan |
| experiments/EXPERIMENT_TRACKER.md | 8,938 | 118 | 2f82dc00aef040ae38c182d9460c278a87731c28a940b3bc79a659ec1ddbb998 | Closed zero-run validation tracker |
| experiments/source_lock.json | 32,589 | 1 | b29378068f5da669f6b9c15d4d4a3e81daa6a2ca345fd86481c403f86771fac3 | Final strict-canonical theorem, proof, citation, and authority lock |
| notes/CITATION_VERIFICATION.md | 14,139 | 236 | 16bb886a6d4fc72e71e58127b8d2ab01c695930f29c42ecf771f8c63830e9fb6 | Verified primary-source roles and anti-misquotation limits |
| notes/CLAIMS_EVIDENCE_MATRIX.md | 13,447 | 113 | bd323341293ebdcb139029c725b3f8432ba46bc627824aad7e7e911ce7d27bcc | Exact claims, evidence classes, dependencies, and guards |
| notes/INDEPENDENT_PAPER_PLAN_REVIEW.md | 18,794 | 356 | c0f09b1ce163d23e327fa6db93d9fcc1e4df41bc18b93b8875fbb748ffb62a88 | Fresh paper-plan review ending PAPER_PLAN_PASS |
| notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md | 19,199 | 366 | b5112a412bf52d504b856e4652023ed41e682f35c566903df2da0fbbc58947e4 | Fresh repaired source-design review |
| notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md | 17,222 | 319 | 970a3f3ccaa55390b6242b46bdf4776bcd404f53a5dcf5753ce99917cb4f1ae1 | Fresh review of the final source lock |
| notes/NOVELTY_ASSESSMENT.md | 14,490 | 182 | 4edf1d891fd033f30a2754c80e0d88288577fe77030fe2e2c88440c6747f0240 | Bounded primary-source novelty and collision ledger |
| notes/PROOF_PACKAGE.md | 30,538 | 611 | 99be46a2b242f99585b2f1692dd69facb87aca4674dab00eec79f76d0e9b4231 | Complete twelve-bridge proof package and exact theorem |
| notes/RESEARCH_QUESTION.md | 10,473 | 185 | cc04ee1db562f04f2291779481b52c2902020a8853bf1fdf186432560c892f24 | Exact setup, questions, scope, and architecture |
| paper/PAPER_PLAN.md | 39,127 | 633 | 33dad14ad5af5a022e99ce7ca573ab1c23b4984b5f37b9da26e04257015ce168 | Passed eight-section, Appendix-A, 23-page proof-first plan |
| refine-logs/FINAL_PROPOSAL.md | 15,731 | 249 | d94c162ee19e8cf621e6599fbab3ab90589f7b0ec0daf9f34479a186bbe67c0f | Final corrected proposal and proof spine |
| refine-logs/INITIAL_PROPOSAL.md | 8,336 | 163 | bfdd03291955d040594a4dd8cf8cfcb3198adb43d90b8b34a210deca96861a1b | Auditable initial proposal and repair history |
| refine-logs/REVIEW_SUMMARY.md | 11,953 | 177 | 7f514ac64a00acba1debb6d70c9f174bfe342c8afb2cfaf7ab72272e00d9c565 | Final refinement synthesis and claim freeze |

The aggregate identity is exactly 267,874 bytes and 3,863 LF characters.
Every input is UTF-8, has LF-only line endings and a terminal LF, and is
permanently byte-immutable under this publication-stage contract.

## One article and one coupled contribution

The manuscript tells one story. Its one-sentence contribution is:

> For every \(d\ge2\) and every positive period vector of length \(d-1\),
> the \(d-1\) traces of labelled, pairwise-disjoint, simple exact marked
> cycles, together with \(-b\), form a dominant generically étale map on the
> unique simple marked Hénon component issuing from the polynomial boundary,
> and its critical Fitting scheme restricts there exactly to the polynomial
> multiplier critical scheme.

The coordinate theorem and the boundary-ramification theorem remain coupled.
The work does not present the imported one-variable multiplier theorem as new,
does not turn generic étaleness into reconstruction, and uses no experiment,
calculation, or visual artifact as evidence.

## Exact mathematical setup

Work over \(\mathbf C\). For \(d\ge2\), let

\[
\mathcal P_d^{\mathrm{cm}}
=\left\{p(z)=z^d+\sum_{j=0}^{d-2}a_jz^j\right\}
\simeq\mathbf A^{d-1},
\qquad
\mathcal B_d=\mathbf A^1_b\times\mathcal P_d^{\mathrm{cm}},
\]

and consider the single generalized Hénon factor

\[
H_{b,p}(x,y)=(p(x)+by,x).
\]

Put \(r=d-1\) and fix an arbitrary positive period vector

\[
\mathbf n=(n_1,\ldots,n_r)\in\mathbf Z_{>0}^{r}.
\]

Repeated numerical periods are allowed. The \(r\) cycles are labelled,
pairwise disjoint, exact, and simple. First form the point-marked incidence.
Then quotient each exact point marking only by its own free cyclic shift

\[
G_{\mathbf n}=\prod_{i=1}^{r}\mathbf Z/n_i\mathbf Z.
\]

Equal-period labels are not permuted. This gives the cycle-marked incidence
\(\mathcal X_{\mathbf n}^{\circ}\), its scalar locus
\(\mathcal S_{\mathbf n}=(\mathcal X_{\mathbf n}^{\circ})_{b=0}\), and the
unique irreducible component \(\mathcal C_{\mathbf n}\) containing the full
scalar locus. The marked functions are

\[
\rho_i=\operatorname{tr}(DH_{b,p}^{n_i}),
\qquad
\Psi=(-b,\rho_1,\ldots,\rho_r):
\mathcal C_{\mathbf n}\longrightarrow
\mathbf A^1\times\mathbf A^r.
\]

The scalar value \(\lambda_i\) is the one-variable multiplier. The determinant
identity

\[
\det(DH_{b,p}^{n_i})=(-b)^{n_i}
\]

is explicit wherever traces are interpreted: trace plus the known
determinant records only an unordered eigenvalue pair, never a chosen
eigenvalue branch.

## Exact five-part main theorem

The manuscript states all five parts conjunctively and with the following
scope.

1. **Marked scalar component.** The scalar cycle-marked locus
   \(\mathcal S_{\mathbf n}\) is nonempty and irreducible and is contained
   in a unique irreducible component \(\mathcal C_{\mathbf n}\) of the
   simple exact disjoint incidence. The map
   \(\mathcal C_{\mathbf n}\to\mathcal B_d\) is étale and dominant, and
   \[
   (\mathcal C_{\mathbf n})_{b=0}=\mathcal S_{\mathbf n}
   \]
   scheme-theoretically inside that simple incidence. No full-incidence
   irreducibility is asserted.

2. **Coordinate map.** The map
   \(\Psi=(-b,\rho_1,\ldots,\rho_r)\) is étale at a scalar point and hence
   dominant and generically étale. Consequently
   \(\rho_1,\ldots,\rho_r\) are algebraically independent over
   \(\mathbf C(b)\) in the function field of the selected component.

3. **Safe fixed-\(b\) specialization.** There is an unspecified nonempty
   Zariski-open set \(U\subset\mathbf G_m\) such that the whole-fiber trace
   map is dominant for every \(b_0\in U\). For each such \(b_0\), at least
   one irreducible component of the reduced fiber is dominant and generically
   étale. The theorem includes no specialized-fiber irreducibility,
   all-component, every-nonzero-\(b\), or prescribed-\(b\) conclusion.

4. **Completed local form.** At every simple scalar point, with centered
   coefficient coordinates \(u=(u_0,\ldots,u_{d-2})\),
   \[
   \widehat{\mathcal O}_{\mathcal C_{\mathbf n},s}
   \simeq\mathbf C[[b,u_0,\ldots,u_{d-2}]],
   \qquad
   \widehat{\mathcal O}_{\mathcal S_{\mathbf n},s}
   \simeq\mathbf C[[u_0,\ldots,u_{d-2}]],
   \]
   and
   \[
   \rho_i=\lambda_i+bG_i
   \]
   for a unique \(G_i\in\mathbf C[[b,u]]\).

5. **Fitting-scheme restriction.** On the simple scalar locus,
   \[
   \mathcal R_H
   =V\!\left(\operatorname{Fitt}_0
   \Omega_{\mathcal C_{\mathbf n}/T}\right),
   \qquad
   \mathcal R_{\mathrm{poly}}
   =V\!\left(\operatorname{Fitt}_0
   \Omega_{\mathcal S_{\mathbf n}/\mathbf A^r}\right)
   \]
   satisfy
   \[
   \mathcal R_H\times_{\mathcal C_{\mathbf n}}\mathcal S_{\mathbf n}
   =\mathcal R_{\mathrm{poly}}
   \]
   as closed subschemes, and compatible local determinants satisfy
   \[
   J_H\bmod b=\pm J_{\mathrm{poly}}.
   \]
   Both determinant sections are nonzero. Their zero schemes are effective
   Cartier divisors when nonempty and may be empty. If the polynomial
   ramification scheme is empty, the multiplicity statement is vacuous.
   Otherwise, scheme restriction preserves generic multiplicity along each
   actual irreducible boundary component. For \(d>2\), no numerical
   intersection multiplicity at an arbitrary closed point follows without a
   separately justified proper transverse slice.

## Mandatory twelve-bridge proof chain

Every theorem-critical bridge below appears in the numbered main text. The
single appendix expands only cyclic-loop edge algebra and does not carry a
missing theorem step.

1. Prove the finite-free cyclic-loop algebra by a monic Gröbner basis,
   including the coincident-index relations for \(n=1\) and \(n=2\).
2. Apply the relative Jacobian criterion on the simple exact disjoint
   point-marked orbit equations.
3. Prove the product cyclic-shift action is free on the exact locus and
   descend étaleness to cycle markings.
4. Identify the scalar fiber scheme-theoretically and reduce trace and
   simplicity to the polynomial multiplier and polynomial simplicity.
5. Use Gorbovickis only for scalar marked-space irreducibility and a
   \(d\ge2\), arbitrary-positive-period, full-rank point on distinct simple
   cycles.
6. Use regular-component disjointness to obtain the unique component through
   the full scalar locus and the exact scheme-theoretic scalar fiber.
7. Compute the block-triangular differential of \(\Psi\), with first row
   \((-1,0,\ldots,0)\) and the polynomial multiplier Jacobian as the
   lower-right block.
8. Use the open image of the total étale locus to prove the
   reducible-fiber-safe fixed-\(b\) conclusion.
9. Apply formal étaleness and divisibility by the non-zero-divisor \(b\) to
   obtain both completed rings and \(\rho_i=\lambda_i+bG_i\).
10. Use the Cartesian boundary square, base change for relative Kähler
    differentials, and base change for zeroth Fitting ideals.
11. Prove the nonzero-determinant, Cartier-or-empty alternative and the
    generic component-length statement, including the vacuous empty case.
12. Identify the residual \(\mu_{d-1}\) normal-form action and its obstruction
    to global injectivity.

## Finite-free edge guards and degree-two guard

For the full ordered \(n\)-loop algebra, the main text states

\[
A_n=
\mathbf C[b,a_0,\ldots,a_{d-2}][x_0,\ldots,x_{n-1}]
\Big/
\left(p(x_j)+b x_{j-1}-x_{j+1}:j\in\mathbf Z/n\mathbf Z\right).
\]

The normalized relations have pairwise-coprime monic leading monomials
\(x_j^d\). The standard monomials give rank \(d^n\), and independent marked
products have rank \(d^{n_1+\cdots+n_r}\). The cyclic coincidences are
displayed exactly:

- \(n=1\): the single relation is \(p(x_0)+(b-1)x_0\);
- \(n=2\): the two relations are
  \(p(x_0)+(b-1)x_1\) and \(p(x_1)+(b-1)x_0\).

The full ordered-loop scheme contains lower periods, collisions, nonsimple
points, multiplicities, and possibly nonreduced fibers. Its rank is not an
exact-cycle count. Finite freeness implies neither irreducibility nor
finiteness or properness of the deleted simple exact open over every base
point.

The article begins at \(d=2\), not \(d=3\). For \(d=2\), one cycle is marked
and \(\mu_1\) is trivial. The arbitrary-period full-rank input is attributed
to Gorbovickis Theorem 1.6 and Lemma 2.1, not to Corollary 1.7. At the
\(z^d\) test point the selected exact cycles have multiplier \(d^{n_i}\ne1\)
and are simple.

## Residual normal-form symmetry

For \(\beta\in\mu_{d-1}\), the diagonal conjugacy

\[
L_\beta(x,y)=(\beta x,\beta y),
\qquad
p_\beta(z)=\beta^{-1}p(\beta z)
\]

satisfies

\[
L_\beta^{-1}\circ H_{b,p}\circ L_\beta=H_{b,p_\beta}.
\]

It preserves \(b\), transports every labelled cycle, preserves every trace,
and preserves the selected component by uniqueness. For \(d>2\) it is
generically free and obstructs generic injectivity and birationality on the
monic-centered normal-form cover. A coarse quotient can have stabilizer
singularities, so no naive coarse-quotient completed-local claim is made.

## Exact article architecture and page contract

The article has exactly two public source files:

- paper/main.tex;
- paper/references.bib.

The source is monolithic and pdfTeX-compatible. The class line is exactly
\(\backslash\)documentclass[11pt]\{article\}. The manuscript author and date
commands are exactly blank:

- \(\backslash\)author\{\};
- \(\backslash\)date\{\}.

There are exactly eight numbered main sections in this order:

1. Introduction;
2. Marked incidences and exact-cycle quotients;
3. Universal cyclic-loop algebra and simple incidence;
4. Scalar component and marked trace coordinates;
5. Completed local geometry at the polynomial boundary;
6. Scheme-theoretic ramification and multiplicities;
7. General nonzero fibers and residual normal-form symmetry;
8. Comparison, limitations, and conclusion.

There is exactly one appendix:

**Appendix A. Cyclic-loop algebra edge details**

It expands the \(n=1\), \(n=2\), and coefficient-ring monic-reduction details,
adds no new theorem, and proves no missing bridge. References follow Appendix
A after an explicit forced clear page, are unnumbered, occupy exactly one
nonempty final page, and are the last public content.

Content pages run from the first PDF page, including the abstract, through the
end of Appendix A. The allowed content range is exactly 22--24 nonempty
pages, with target 23. References are excluded from that content count.
Consequently the total PDF has 23--25 nonempty pages, exactly one of which is
the final References page. No blank page is allowed.

The abstract is result-first, citation-free, history-free, self-contained,
anonymous, and has 180--220 words under this robust rule: strip TeX comments;
isolate the abstract environment; replace every maximal inline, display,
delimiter, or named mathematics span by one MATH token; preserve ordinary
text in command arguments while removing formatting commands and braces;
normalize ties and whitespace; then count maximal word tokens allowing
internal apostrophes and hyphens, plus each MATH token as one word. The source
review and each build receipt record the integer and the exact counter-snippet
source identity.

The manuscript contains exactly one table environment:

**Table 1. Dependency of the five theorem parts on the twelve proof bridges.**

Its rows are the five theorem parts and the auxiliary finite-free lemma. Its
columns identify bridge numbers and distinguish direct, imported, and formal
corollary evidence. It is non-numerical proof structure, every row is derived
in prose, and it is not scientific data.

There are exactly zero other tables, figures, figure environments, included
graphics, illustrations, image files, raster or vector assets, scans,
external inputs, code files, datasets, experiments, numerical examples,
numerical-result tables, empirical results, or computational evidence.

## Exact seven-entry bibliography lock

The bibliography contains exactly seven entries, all actually cited. The
exact sorted key set is:

\[
\{
\mathrm{BH26},
\mathrm{CD26},
\mathrm{FM89},
\mathrm{GT24},
\mathrm{Gor13},
\mathrm{Hug24},
\mathrm{StacksProject}
\}.
\]

The citation keys used by paper/main.tex, the entry keys in
paper/references.bib, and the generated main.bbl bibitem keys are exactly
equal to this set. Wildcard nocite, duplicate keys, missing entries, and
uncited entries are forbidden.

| Key | Locked verified identity | Permitted role |
|---|---|---|
| BH26 | Fabrizio Bianchi and Yan Mary He, “A thermodynamic path metric for complex Hénon maps,” arXiv:2606.29363v1, submitted 2026-06-28 | Analytic full marked unstable-spectrum and thermodynamic comparison only |
| CD26 | Serge Cantat and Romain Dujardin, “Multiplier rigidity for complex Hénon maps,” arXiv:2603.09445v1, submitted 2026-03-10 | Full-spectrum and finite low-period Hénon rigidity comparison only |
| FM89 | Shmuel Friedland and John Milnor, “Dynamical properties of plane polynomial automorphisms,” Ergodic Theory and Dynamical Systems 9 (1989), 67--99, DOI 10.1017/S014338570000482X | Generalized Hénon normal forms and low-degree fixed-point overlap only |
| GT24 | Igors Gorbovickis and Johan Taflin, “Independence of multipliers in several variables complex dynamics,” arXiv:2411.12856v2, 2025 source version | Regular polynomial-endomorphism multiplier-independence comparison only |
| Gor13 | Igors Gorbovickis, “Algebraic independence of multipliers of periodic orbits in the space of polynomial maps of one variable,” arXiv:1305.0867v1 (2013), later ETDS 36 (2016), DOI 10.1017/etds.2014.103 | Sole indispensable dynamics input: marked-space irreducibility and the \(d\ge2\) arbitrary-period full-rank point |
| Hug24 | Valentin Huguin, “Moduli spaces of polynomial maps and multipliers at small cycles,” arXiv:2412.19335v1 (2024) | Complete unmarked period-one/two polynomial-spectrum comparison only |
| StacksProject | The Stacks Project, Tags 02GH, 0257, 07Z6, and 0C3I | Formal/completed-local étale support and Fitting base change on the proved Cartesian simple-boundary square only |

Gorbovickis is the sole indispensable dynamics theorem. The Stacks entry is
foundational support for the two exact algebraic-geometric operations. The
other five dynamics papers are comparison or context only. No source supplies
a stronger conclusion than its recorded role, and no metadata may be
generated from memory or a secondary summary.

Names of cited authors, public paper titles, publication years, public
submission dates, journal data, DOI data, arXiv identifiers, and Stacks tags
are required neutral bibliography. They are not manuscript-author identity
or manuscript-date metadata and do not relax the blank author/date rule.

## Exact A1--A20 public mathematical boundaries

The manuscript preserves the following twenty statements exactly and does
not contradict them elsewhere.

- **A1.** No irreducibility claim for the full marked Hénon incidence.
- **A2.** No irreducibility claim for any or every specialized fixed-\(b\) fiber.
- **A3.** No local-coordinate claim for every nonzero \(b\).
- **A4.** No conclusion at any prescribed nonzero fiber, including \(b=-1\).
- **A5.** No global injectivity, birationality, or reconstruction claim on the monic-centered normal-form cover.
- **A6.** No claim that every irreducible component of a general fixed-\(b\) fiber dominates or is generically étale.
- **A7.** No reducedness or smoothness claim for either critical/Fitting scheme.
- **A8.** No transversality or normal-crossings claim for the boundary intersection.
- **A9.** No global, nonsimple, or compactified Fitting-scheme equality beyond the simple scalar locus.
- **A10.** No closed-point numerical intersection multiplicity without a separately justified proper transverse slice; the theorem preserves generic multiplicities along boundary components.
- **A11.** No individual eigenvalue branch is a coordinate: \(\det(DH_{b,p}^{n_i})=(-b)^{n_i}\), so trace records only the unordered eigenvalue pair once the determinant is known.
- **A12.** No interpretation of finite-free rank \(d^n\) as an exact-cycle count.
- **A13.** The fiber \(b=0\) is only the polynomial/proof boundary; \(H_{0,p}\) is not a Hénon automorphism.
- **A14.** No positive-characteristic extension.
- **A15.** No extension to multi-factor or composed generalized Hénon maps.
- **A16.** Point-marked fibers contain cyclic-shift copies; passage to cycle markings removes only those shifts, not residual \(\mu_{d-1}\) ambiguity.
- **A17.** No naive coarse \(\mu_{d-1}\)-quotient completed-local claim near stabilizers; stack or quotient-singularity analysis is required.
- **A18.** No claim that the simple exact open is finite or proper over all of \(\mathcal B_d\), no uniform all-fiber degree, and no all-fiber reconstruction.
- **A19.** No absolute-priority or “first ever” claim.
- **A20.** No computational, CAS, numerical, empirical, or experimental evidence or result.

## Anonymous and public-text contract

The public article is anonymous. Its author and date source fields are blank,
and the corresponding PDF metadata values are empty. It contains no
affiliation, email address, self-identifying link, acknowledgment, grant,
repository identity, submission identifier, manuscript date, identity-bearing
timestamp, local filesystem path, hash, internal candidate identifier,
internal paper number, governance term, gate or review verdict, agent or model
name, operational instruction, discovery history, hidden prompt, release
claim, or unsupported priority statement.

The article may and must name cited authors and state verified public
publication or submission dates when mathematically relevant. That neutral
bibliographic use is distinct from manuscript authorship and manuscript date
and does not authorize any identity-bearing metadata.

The source includes deterministic pdfTeX controls that suppress creation and
modification dates, the trailer identifier, author, subject, keywords, and
local-path metadata. An unavoidable generic identity-free creator or producer
string may remain only if it is recorded by both build receipts. No governance
text may be exposed in extracted public prose.

## Exact monotone stage universes

Every universe is an exact sorted set of safe project-relative regular-file
paths. At every stage the only four directories excluding the project root
are experiments, notes, paper, and refine-logs. There are zero symbolic links
and zero other entry types.

\(U_{G15}\), count 15, is exactly the frozen-input table above.

\(U_{L17}=U_{G15}\cup\{\)

- experiments/publication_lock.json;
- notes/PUBLICATION_STAGE_SCOPE.md

\(\}\), count 17.

\(U_{P18}=U_{L17}\cup\{\)

- notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md

\(\}\), count 18.

\(U_{D20}=U_{P18}\cup\{\)

- paper/main.tex;
- paper/references.bib

\(\}\), count 20.

\(U_{S21}=U_{D20}\cup\{\)

- notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md

\(\}\), count 21.

\(U_{R0}=U_{S21}\cup\{\)

- paper/BUILD_RECEIPT_R0.json;
- paper/main_round0.pdf

\(\}\), count 23.

\(U_{V1}=U_{R0}\cup\{\)

- notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md

\(\}\), count 24.

\(U_{S1}=U_{V1}\cup\{\)

- paper/SOURCE_REVISION_RECEIPT_R1.json

\(\}\), count 25.

\(U_{R1}=U_{S1}\cup\{\)

- paper/BUILD_RECEIPT_R1.json;
- paper/main_round1.pdf

\(\}\), count 27.

\(U_{V2}=U_{R1}\cup\{\)

- notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md

\(\}\), count 28.

No stage skips a predecessor, removes a path, pre-creates a later path, or
retains a build intermediate. The sole additions are exactly those displayed.
A bounded source revision may change the bytes of the two existing public
sources but adds only its required receipt path.

## Disjoint temporal roles and exact read/write universes

Roles are substantively and temporally disjoint. No role may author an object
that it reviews, read a later-stage artifact, expand its own allowlist, or
convert conditional authority into present authority.

| Role | Activation | Exact project read universe | Exact project write universe |
|---|---|---|---|
| Publication-stage author | This task only | \(U_{G15}\) | scope, then lock |
| Independent publication reviewer | Stable PUBLICATION AUTHOR STOP | \(U_{L17}\) | notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md only, all-pass only |
| Anonymous manuscript author | Exact PUBLICATION_STAGE_PASS and separate invocation | \(U_{P18}\) | paper/main.tex, then paper/references.bib |
| Formal manuscript-source reviewer | Stable manuscript AUTHOR STOP with both exact source identities | \(U_{D20}\) | notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md only, all-pass only |
| Bounded pre-source repair author | Separate explicit instruction after a zero-write source-review blocker | \(U_{D20}\) | may edit only paper/main.tex and paper/references.bib |
| Round-0 builder | Exact MANUSCRIPT_SOURCE_PASS plus separate explicit build GO | \(U_{S21}\) | paper/main_round0.pdf and paper/BUILD_RECEIPT_R0.json only |
| Round-1 manuscript reviewer | Stable Round-0 builder stop | \(U_{R0}\) | notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md only |
| Sole bounded revision author | Stable R1 review | \(U_{V1}\) | may edit the two sources and must add paper/SOURCE_REVISION_RECEIPT_R1.json |
| Round-1 builder | Stable revision stop | \(U_{S1}\) | paper/main_round1.pdf and paper/BUILD_RECEIPT_R1.json only |
| Fresh Round-2 manuscript reviewer | Stable Round-1 builder stop | \(U_{R1}\) | notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md only |

The publication reviewer authored none of the fifteen inputs or governance
pair. The source reviewer authored neither public source. The R1 reviewer is
distinct from every source author and builder. The R2 reviewer is fresh and
distinct from every author, builder, and prior reviewer.

## Anonymous drafting contract

Only an exact PUBLICATION_STAGE_PASS, followed by a separate manuscript-author
invocation, activates drafting. The author reads exactly \(U_{P18}\) and
writes exactly, in dependency order:

1. paper/main.tex;
2. paper/references.bib.

All eight numbered sections, Appendix A, all definitions, five theorem parts,
twelve proof bridges, exact limitations, the single proof-dependency table,
and deterministic controls are in paper/main.tex. There is no sections
directory, macro file, style file, class file, second appendix, supplement,
figure, image, asset, code, data, result, or build artifact.

The source author does not compile, use the network, install software, invoke
CAS, run a scientific calculation, generate data or assets, or read a future
review or build artifact. Static source checks are allowed. The author reports
stable SHA-256, bytes, LF counts, robust abstract count, exact seven-key set
equality, and exact \(U_{D20}\), then stops. Drafting does not self-authorize
formal source review.

## Formal manuscript-source review gate

There is exactly one formal source-review path:

notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md

It is temporally after a stable manuscript AUTHOR STOP that binds both public
sources by exact SHA-256 and byte count. A fresh reviewer who authored neither
source reads exactly \(U_{D20}\) and independently checks:

- exact title, 11pt standard article, blank author and date, anonymous front
  matter, robust 180--220-word abstract, eight sections, Appendix A, and
  final References;
- the complete \(d\ge2\), repeated-labelled-period setup and all five theorem
  parts;
- all twelve proof bridges, including the block differential and the exact
  scalar fiber;
- the \(n=1,2\) finite-free relations and every rank/irreducibility/finiteness
  guard;
- the unique component argument and the Theorem 1.6/Lemma 2.1 quadratic
  guard;
- the unspecified-open, reducible-fiber-safe fixed-\(b\) proof;
- both completed local rings, the unique trace expansion, the Cartesian
  differential and Fitting base change, the sign-unit determinant
  congruence, and the Cartier-or-empty/vacuous-empty multiplicity guard;
- the determinant identity, unordered eigenvalue pair, residual
  \(\mu_{d-1}\) action, trivial quadratic action, and coarse-stabilizer
  warning;
- exactly one non-numerical proof table and zero figures, images, assets,
  numerical tables, experiments, computations, or empirical claims;
- all twenty exact A1--A20 boundaries;
- exact equality of the seven citation-key sets and the precise proof versus
  comparison roles;
- static pdfTeX compatibility, deterministic controls, public-text hygiene,
  blank identity/date metadata, and absence of drafting markers.

If any item fails, the reviewer writes nothing and emits no pass token. A
repair requires a separate explicit instruction, may edit only the two public
sources without expanding theorem, bibliography, evidence, or scope, and is
followed by a fresh full review at the same still-absent review path. Only an
all-pass reviewer may create the review, bind both exact source hashes and
bytes, and end with:

**MANUSCRIPT_SOURCE_PASS**

That pass alone does not authorize compilation. Round 0 also requires a
separate explicit build GO.

## Frozen deterministic toolchain and environment

No build is performed in this governance stage. A future authorized builder
must use the following exact invocation paths, resolved targets, executable
SHA-256 identities, and version leads. Any mismatch is a blocker and
authorizes no build.

| Purpose | Invocation path | Resolved target | Executable SHA-256 | Frozen version lead |
|---|---|---|---|---|
| Strict static and decoded-PDF validation | /root/miniconda3/bin/python3.12 | /root/miniconda3/bin/python3.12 | 9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101 | Python 3.12.3 |
| BibTeX | /usr/bin/bibtex | /usr/bin/bibtex.original | c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f | BibTeX 0.99d (TeX Live 2022/dev/Debian) |
| Byte comparison | /usr/bin/cmp | /usr/bin/cmp | b355472d3c90ea94d11ebb8b750e6946ccd348edc6fca4aefc1235c3994ef791 | GNU diffutils 3.8 |
| MIME identity | /usr/bin/file | /usr/bin/file | ffa64f607f77d57cb3e2b650825868367a06eb91cdc5959c4e2f62ceb885b18a | file-5.41 |
| PDF attachments | /usr/bin/pdfdetach | /usr/bin/pdfdetach | e0c04f35fc5b0c4096199ff11d70e49db2b1952b4110f96f5f9ef0a3a4135b2d | pdfdetach version 22.02.0 |
| PDF fonts | /usr/bin/pdffonts | /usr/bin/pdffonts | 257a74fde0c3c36040504ff9068ee4b896c1cc2f19a9fae5a5b3dda55637ba5e | pdffonts version 22.02.0 |
| PDF images | /usr/bin/pdfimages | /usr/bin/pdfimages | cdac55daf2eaacbaf9f80cf8371e935c8686cb4fd7e84c42bba9706c1f10c87d | pdfimages version 22.02.0 |
| PDF metadata and pages | /usr/bin/pdfinfo | /usr/bin/pdfinfo | 8ca6e6d0b2e6b3f135a82feb07b3d5750498eb77e6f66412803f425eb8471a8e | pdfinfo version 22.02.0 |
| pdfLaTeX | /usr/bin/pdflatex | /usr/bin/pdftex | 01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9 | pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian) |
| PDF signatures | /usr/bin/pdfsig | /usr/bin/pdfsig | 0c50615f466e45cc0309a68bdb8c4ad53778529ec77ab14e521e9c8d765eff09 | pdfsig version 22.02.0 |
| PDF text | /usr/bin/pdftotext | /usr/bin/pdftotext | 7de929ce0686af5dbf76975ad08bbff93526b3d9028035176a4ca89d9d19c27d | pdftotext version 22.02.0 |
| SHA-256 | /usr/bin/sha256sum | /usr/bin/sha256sum | 7645c8e76d75515ccb75c9086bdcf0d4071f2985f380f249253ead7d7c6810b3 | GNU coreutils 8.32 |
| Decoded PDF token scan | /usr/bin/x86_64-linux-gnu-strings | /usr/bin/x86_64-linux-gnu-strings | 6ff5cfaddaf8dbc67614f535530465c890e83498509a6c8ffacc3798b6f1126f | GNU strings 2.38 |

Every complete version transcript, not only its displayed lead, is bound by
command, SHA-256, and byte count in each build receipt. Every non-raster
validation executable and every nonpersistent validation snippet whose output
enters a receipt is bound in the same way. The Python interpreter may run only
nonpersistent governance-validation snippets and no scientific calculation.

Every build command uses exactly this environment:

    TZ=UTC
    LC_ALL=C
    LANG=C
    SOURCE_DATE_EPOCH=1786924800
    FORCE_SOURCE_DATE=1

No additional variable may alter TeX, bibliography, locale, clock, metadata,
path lookup, or source discovery. Absolute frozen invocation paths are used;
PATH does not select an executable.

## Round-0 isolated deterministic build

Round 0 begins only after stable exact \(U_{S21}\), an exact
MANUSCRIPT_SOURCE_PASS, absence of every later path, and a separate explicit
build GO.

Create exactly two distinct, new, initially empty, builder-owned,
non-symlink temporary directories from the literal template:

/tmp/p18-paper18-r0-XXXXXXXX

Each resolved path must match:

^/tmp/p18-paper18-r0-[A-Za-z0-9]{8}$

and have resolved parent /tmp. The suffixes differ. A reused or preexisting
entry, symlink, different parent, or different path is a blocker. Copy into
each root only the exact bytes of paper/main.tex and paper/references.bib.

In each root run exactly, in order:

    /usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
    /usr/bin/bibtex main
    /usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex
    /usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex

All eight exit codes are zero. Capture exact combined stdout/stderr bytes for
each command without a root label, timestamp, or wrapper prefix. Run A and run
B must have byte-identical:

- main.pdf;
- main.bbl;
- final main.log;
- every corresponding command transcript;
- the combined four-command transcript; and
- the complete discovered font table.

Identity means equal SHA-256, equal bytes, and byte-for-byte comparison. A
mismatch fails the round; choosing one run is forbidden.

The only allowed root entries are regular non-symlink files named:

- main.tex;
- references.bib;
- main.aux;
- main.bbl;
- main.blg;
- main.log;
- optional main.out;
- optional main.toc;
- main.pdf.

Shell escape, network access, package installation, rasterization, source
editing, CAS, scientific execution, undeclared project reads, and project
intermediates are forbidden.

## Non-raster source and PDF validation

Both clean runs pass the same checks before persistence.

1. All TeX and BibTeX exits are zero. Final logs contain zero TeX, LaTeX,
   package, or BibTeX errors; zero warnings; zero undefined references or
   citations; zero multiply defined labels; zero missing characters, glyphs,
   or fonts; and zero overfull or underfull boxes.
2. Source and extracted text contain zero TODO, FIXME, XXX, VERIFY,
   placeholder, draft, repair, governance, review-verdict, internal path,
   hash, internal paper number, agent/model, identity, grant,
   acknowledgment, repository, submission, release, or operational marker.
3. The title is exact. The author and date fields and PDF metadata are blank.
   The abstract has 180--220 words under the locked robust counter. There are
   exactly Sections 1--8 in the locked order, exactly Appendix A, a forced
   clear page, and final References.
4. There are 22--24 nonempty content pages through the end of Appendix A,
   with target 23, exactly one final References page, and 23--25 total pages.
   Every page contains non-whitespace public mathematical or bibliographic
   text.
5. There is exactly one table environment in the locked location and no other
   table, figure environment, includegraphics command, image, or external
   asset.
6. The citation keys in main.tex, references.bib, and main.bbl have exact
   seven-key set equality. There is no wildcard nocite, duplicate, missing,
   or uncited key.
7. The font count is discovered from the actual PDF and recorded as an
   integer. Every font is embedded, subset, and has a Unicode map. The two
   runs have identical complete font tables.
8. The PDF contains zero image XObjects, attachments, embedded files,
   AcroForm, XFA, JavaScript or JS action, Launch action, RichMedia,
   FileAttachment annotation, signature, external-file action, or trailer
   identifier. PDF structure and inflated Flate streams are included in the
   frozen-tool token audit; raw-byte searching alone is insufficient.
9. PDF metadata contain no author identity, manuscript date, creation or
   modification date, subject, keywords, submission identifier, local path,
   or identity-bearing timestamp. Any generic identity-free creator or
   producer value is recorded exactly.
10. Extracted text contains every theorem assumption, all five theorem parts,
    all twelve proof bridges, the \(n=1,2\) guards, the exact fixed-\(b\),
    completion, Fitting, Cartier-or-empty, multiplicity, determinant, and
    residual-symmetry statements, all A1--A20 boundaries, and zero empirical
    claim.

The receipt records exact commands, snippet sources, exit codes,
stdout/stderr transcript identities, counts, set comparisons, and booleans.
No screenshot, OCR, visual inspection, or raster inspection is part of the
build gate.

## Persistence, canonical receipt, and safe cleanup

Only after both clean runs and every validation pass may Round 0 persist:

- paper/main_round0.pdf;
- paper/BUILD_RECEIPT_R0.json.

The PDF is the exact byte copy common to both runs. No paper/main.pdf,
auxiliary, log, transcript, cache, temporary path, or other project artifact
persists.

The build receipt is strict compact canonical JSON: UTF-8; recursively
Unicode-code-point-sorted object keys; compact comma/colon separators; no
duplicate key, nonfinite number, BOM, carriage return, or insignificant
whitespace; and exactly one terminal LF. It excludes its own SHA-256 and byte
count. It binds:

- the publication scope and lock, publication review, both public sources,
  and formal source review;
- exact prebuild and postbuild source identities;
- both roots, regex, ownership, distinctness, initial emptiness, and
  non-symlink checks;
- every frozen executable path, resolved target, hash, complete version
  transcript, and validation snippet;
- exact environment, command sequence, eight exits, and every command
  transcript;
- per-run PDF, BBL, final-log, combined-transcript, and font-table identities;
- every within-round byte-identity result;
- every log, source, text, page, abstract, section, appendix, table, citation,
  theorem, proof, anti-claim, font, image, attachment, action, metadata,
  trailer, identity, and external-access check;
- the discovered font count and complete font table;
- the persisted PDF identity;
- exact prewrite and postwrite universes; and
- explicit cleanup operations and verified root absences.

After all facts are captured, revalidate each resolved root and its exact
regular-file allowlist. Unlink each allowed file individually by its explicit
resolved path, then remove the empty root with rmdir. Recursive deletion,
globs, unresolved variables, symlink traversal, broad directory targets, and
deletion outside the two validated roots are forbidden. Both roots must be
verified absent before the builder stop. A validation failure authorizes no
persistence. A cleanup failure after persistence is reported as a blocker
without creating another project path.

## Round-1 review, one bounded revision, rebuild, and Round-2 review

After a stable exact \(U_{R0}\) builder stop, a fresh reviewer may write only:

notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md

A precondition mismatch has disposition WRITE NOTHING. The reviewer rehashes
the complete chain and independently audits the receipt, PDF, sources, five
theorem parts, twelve proof bridges, finite-free guards, citation roles, page
boundaries, nonempty pages, sole proof table, A1--A20, fonts, metadata,
security, warnings, anonymity, public text, and cleanup without rasterization.

The final disposition is exactly one of:

- MANUSCRIPT_R1_PASS;
- MANUSCRIPT_R1_REPAIR_REQUIRED.

Each finding has a stable identifier, severity, exact source/PDF location,
required bounded repair, and theorem-scope impact. Neither disposition
authorizes finalization or release.

Exactly one bounded revision window follows, including a canonical no-op. The
revision author may edit only paper/main.tex and paper/references.bib and must
create:

paper/SOURCE_REVISION_RECEIPT_R1.json

Every change maps to an R1 finding and preserves theorem scope, all proof
dependencies, the exact seven-key bibliography, page/table/appendix contract,
anonymity, public-text hygiene, and zero-science envelope. If R1 requires no
repair, both sources remain byte-identical and the receipt records zero
changes. There is no second revision window.

The revision receipt is strict canonical JSON under the same rules, excludes
its own SHA-256 and bytes, and binds the R1 review, pre/post source identities,
an exact source-diff digest and bounded change ledger, or exact no-op
identities, plus the exact prewrite and postwrite universes.

Round 1 begins only after stable exact \(U_{S1}\). It repeats the entire
two-clean-build and validation protocol in two distinct roots from:

/tmp/p18-paper18-r1-XXXXXXXX

matching:

^/tmp/p18-paper18-r1-[A-Za-z0-9]{8}$

It persists only paper/main_round1.pdf and paper/BUILD_RECEIPT_R1.json. The
R1 receipt additionally binds the R0 PDF and receipt, R1 review, revision
receipt, and authorized source diff. If the revision is a no-op, the R1 PDF
must be byte-identical to the R0 PDF. If it is not a no-op, every difference
must arise from the exact authorized source diff. R0 artifacts remain
unchanged.

After stable exact \(U_{R1}\), a fresh reviewer may write only:

notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md

A precondition mismatch writes nothing. The reviewer replays every R1 finding
and repair and repeats the complete theorem, proof, citation, page, PDF,
anonymity, warning, public-text, inventory, receipt, and cleanup audit. Its
sole positive last nonempty line is:

**MANUSCRIPT_R2_PASS**

A failure creates no second revision authority.

Even an exact R2 pass leaves paper/main.pdf, camera-ready work, finalization,
identity disclosure, public or local release, repository publication,
submission, upload, venue communication, and every external message
unauthorized. Any finalization or release path requires a separate future
governance lock and a fresh independent review.

## Current inventory, future absences, and author stop

Immediately before these governance writes, the project contains exactly
\(U_{G15}\): 15 regular files, four directories excluding the project root
(experiments, notes, paper, refine-logs), zero symbolic links, and zero other
entry types.

After this scope and the canonical publication lock are written, the required
universe is exactly \(U_{L17}\): 17 regular files, the same four directories,
zero symbolic links, and zero other entry types.

At the publication-author stop, every future path in
\(U_{V2}\setminus U_{L17}\) is absent, as are:

- paper/main.pdf;
- paper/sections and paper/math_commands.tex;
- every additional appendix, supplement, style, class, figure, image, asset,
  code, data, result, build intermediate, cache, finalization, release,
  submission, upload, identity, or external-message artifact; and
- every forbidden directory named build, code, data, figures, manuscript,
  output, release, results, source, or submission.

The canonical lock binds this scope by safe relative path, SHA-256, byte
count, and LF count. It binds itself only by safe path and authority role; its
own SHA-256 and byte count are excluded.

After writing and validating exactly these two governance artifacts, the
author rehashes all fifteen frozen inputs, verifies strict canonical
round-trip, duplicate-key and nonfinite rejection, exact stage equations,
role disjointness, exact \(U_{L17}\), and all future absences, reports both
governance identities, and stops. No further project write is permitted in
this authoring turn.
