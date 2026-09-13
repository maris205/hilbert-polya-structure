# Paper 22 — Publication-Stage Scope

Date: 2026-08-24 UTC  
Project root: `papers/22-hamiltonian-cubic-spectral-collapse`  
Artifact role: human-readable publication-governance contract, not manuscript prose  
Authoring status: scope-only author stop; no publication lock or public source is authorized

## Authority and upstream gate

This file is the sole project write of a fresh publication-scope author. The
author read the canonical R2 paper plan, its independent PASS review, the
source lock and its independent PASS review, the proof package, the citation
verification ledger, the claims--evidence matrix, the latest Batch 06
lifecycle addenda, and the Paper 21 publication scope used only as a
structural warning. No upstream file was edited.

The controlling upstream identities are:

- `paper/PAPER_PLAN.md`: SHA-256
  `2fdfc4eab1bd60e361b144eb8c3c9d0d7c71d37c63ce54145e7e6cca3888e224`,
  34,692 bytes, 952 LF;
- `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md`: SHA-256
  `20c7e7b49a2f698b509026bd025e5dd3ebf000ff6d3fa343466867e755d3951c`,
  10,683 bytes, 248 LF, terminal `PAPER_PLAN_PASS`;
- `experiments/source_lock.json`: SHA-256
  `6f79231121f78e1c6b55da148c5710c2005e0ae36f92b0771740d127a253ad88`,
  32,258 bytes, one LF; and
- `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`: SHA-256
  `1fa152bdf1cf83a852b7e585e1e3aac402d06534c447a881e7506f082594846f`,
  16,605 bytes, 521 LF, terminal `SOURCE_LOCK_PASS`.

The two immutable root-level plan histories remain outside the project tree
and were not modified:

- `BATCH_06_PAPER22_PAPER_PLAN_FAILED_R0.md`: SHA-256
  `7758ce22918de8ee2511611884f861a58d36b37873e114ebbe5534a83a9301f2`,
  32,169 bytes, 795 LF;
- `BATCH_06_PAPER22_PAPER_PLAN_BLOCKED_R1.md`: SHA-256
  `6a5ae037c6351291132ff1ea22ade36d851b1f861e5d1e88e4501a8fb498f785`,
  34,008 bytes, 939 LF.

This scope freezes what a later publication lock may authorize. It does not
itself authorize that lock, a manuscript, TeX, BibTeX, compilation, PDF, or
external action.

## Exact anonymous public and metadata identity

The following title string is exact and immutable across the public article,
the source `\title{...}` field, the rendered title, and the decoded PDF title
metadata:

`Cubic Spectral Collapse for Endpoint-Spiked Hamiltonian Product Shears: Sharp Selector Thresholds in Arbitrary Mode Number`

No shortened title, running-title substitute, subtitle split, project number,
or alternate punctuation may replace that string in any of those four
locations.

The identity and date fields are frozen as follows:

- visible author text: exactly `Anonymous`;
- source author field: exactly `Anonymous`;
- PDF author metadata: exactly empty;
- source date field: exactly empty, implemented as `\date{}` with no visible
  date; and
- no author footnote, thanks mark, corresponding-author marker, or hidden
  identity field.

No real name, pseudonymous personal identifier, affiliation, postal address,
email, ORCID, acknowledgment, funding statement, grant number, sponsor,
contribution statement, reviewer identity, agent identity, model name, local
path, hash, byte count, PASS token, dashboard state, scope/lock history,
submission venue, or private provenance may enter `paper/main.tex`,
`paper/math_commands.tex`, `paper/references.bib`, any generated auxiliary
source, the rendered article, or PDF metadata. This prohibition includes TeX
comments, BibTeX comments and unused metadata fields, PDF bookmarks, headers,
footers, document properties, and embedded-file metadata.

## Frozen mathematical object

Let `K` be an arbitrary field of characteristic zero. Let `r` and `g` be
integers satisfying

\[
r\ge 4,\qquad g\ge 2r+1,
\]

and put `h=g-1` and `m=r-2`. For
`q=(q_1,\ldots,q_r)` and `p=(p_1,\ldots,p_r)`, the article studies only

\[
V_{r,g}(q)=\prod_{i=1}^r q_i^2+q_1^g,
\qquad
W_{r,g}(p)=\prod_{i=1}^r p_i^2+p_r^g,
\]

\[
S(q,p)=(q,p+\nabla V_{r,g}(q)),\qquad
T(q,p)=(q+\nabla W_{r,g}(p),p),\qquad
F_{r,g}=T\circ S.
\]

The phase order `S` then `T`, hence `F=T\circ S`, is immutable. The article
must prove the subtraction inverses and preservation of
`\omega=\sum_i dq_i\wedge dp_i` from the symmetric Hessian blocks. Algebraic
closedness may not be added to the assumptions.

Set

\[
M=2\mathbf 1\mathbf 1^{\mathsf T}-I_r.
\]

The matrix `A` is `M` with its first row replaced by
`h e_1^{\mathsf T}`; `B` is `M` with its last row replaced by
`h e_r^{\mathsf T}`; and the complete-step matrix is exactly

\[
C=BA,
\]

never `AB`. Literal gradient supports must derive these matrices. The mixed
row score is `2\sum_j u_j-u_i`; exactly the first `V` row and last `W` row
are competitive. The complete entry ledger is frozen as

\[
\begin{aligned}
C_{11}&=h+4m+4,&
C_{1j}&=4m+2 &&(2\le j\le r),\\
C_{i1}&=2h+4m+2 &&(2\le i<r),&
C_{ij}&=4m+\mathbf1_{\{i=j\}}
&&(2\le i<r,\ 2\le j\le r),\\
C_{rj}&=2h &&(1\le j<r),&
C_{rr}&=h.
\end{aligned}
\]

## Selector, cone, carry, and leading-form contract

For `u>0`, the normalized variables exist only for `2\le i\le r`:

\[
x_i=\frac{u_i}{u_1},\qquad
\sigma=\sum_{i=2}^r x_i.
\]

The index `1` is excluded from `\sigma`. The region is always called the
**explicit sufficient invariant selector cone**

\[
\mathcal K_{r,g}=
\left\{u>0:x_i\ge1\ (2\le i\le r),\quad
\sigma<\frac{h-1}{2}=\frac{g-2}{2}\right\}.
\]

The public proof must retain all of the following main-body obligations:

1. The first pure-minus-mixed margin is
   `u_1(h-1-2\sigma)>0`.
2. For `v=Au`, and only after that first phase,
   `v_1/u_1=h` and `v_i/u_1=2+2\sigma-x_i`; the second margin is
   \[
   \frac{\Delta_T}{u_1}
   =(2h-4m)\sigma-(h+1)x_r-4m-2,
   \]
   with the two strict lower bounds
   `((h+1)(h-2m-3))/2` and
   `(2m+1)(h-2m-3)` in their proper sign cases.
3. The ordinary seed satisfies
   `\sigma(\mathbf1)=m+1<(h-1)/2`.
4. Every middle lower wall has output margin
   `(h-1-2\sigma)+(x_i-1)>0`; the last lower wall retains the two
   bounds `((h+2)(h-2m-3))/2` and
   `2(m+1)(h-2m-3)`; and the open height wall retains
   \[
   \frac{H_2}{u_1}\ge
   (h-2m-3)(h+4m^2+4m+2)>0.
   \]
5. At the least parameter `h=2m+4`, every decisive factor
   `h-2m-3` equals one. No threshold equality may be hidden.
6. Both carried-coordinate phases are proved in the actual word order from
   `C-I>0`, `A\mathbf1>\mathbf1`, and the nonnegative nonzero rows of `A`,
   yielding
   \[
   v_{n+1}=Au_n,\qquad u_{n+1}=Cu_n\qquad(n\ge0).
   \]
7. Noncancellation is proved in the polynomial domain from strict uniqueness
   and
   `\operatorname{LH}(fg)=\operatorname{LH}(f)\operatorname{LH}(g)\ne0`.
   Degree arithmetic or positive coefficients alone are not a proof.

The normalized rows of `C`, every selector, every cone wall, carried terms,
and leading-form survival are theorem-critical and remain in the main body.

## Visibility, exact degree, and spectral-collapse contract

The public proof must show `C-A` is entrywise positive, prove the strict last
versus first and last versus middle row differences, and distinguish the two
time ranges exactly:

- the last `q`-coordinate is strictly visible only for `n\ge1`;
- at `n=0`, all `2r` coordinate degrees tie at one; and
- nevertheless
  \[
  \deg(F_{r,g}^n)=e_r^{\mathsf T}C^n\mathbf1
  \qquad(n\ge0),
  \qquad
  \lambda_1(F_{r,g})=\rho(C).
  \]

The Perron statement is an algebraic-degree statement. It may not be renamed
or promoted to a topological, metric, arithmetic, or measure-theoretic
entropy theorem.

Freeze the invariant spaces

\[
U=\left\{z\in K^r:z_1=z_r=0,\quad
\sum_{i=2}^{r-1}z_i=0\right\},
\]

\[
E=\left\{(a,b,\ldots,b,c)^{\mathsf T}:a,b,c\in K\right\}.
\]

The article must prove

\[
\dim U=r-3,\qquad A|_U=B|_U=-I_U,\qquad C|_U=I_U,
\qquad K^r=U\oplus E.
\]

In the exact convention
`(a,b,c)\mapsto(a,b,\ldots,b,c)`, with `m` equal middle coordinates, the
restriction is

\[
Q_{m,h}=
\begin{pmatrix}
h+4m+4 & 2m(2m+1) & 2(2m+1)\\
2h+4m+2 & 4m^2+1 & 4m\\
2h & 2mh & h
\end{pmatrix}.
\]

The cubic transcription lock is

\[
\begin{aligned}
P_{m,h}(t)
={}&t^3-(2h+4m^2+4m+5)t^2\\
&+(h^2-8hm(m+1)+2h+4)t\\
&-h^2(2m+1)^2,
\end{aligned}
\]

with

\[
\chi_C(t)=(t-1)^{r-3}P_{m,h}(t),
\qquad
P_{m,h}(1)=-4m(m+1)(h+1)^2\ne0.
\]

Therefore the eigenvalue one has algebraic and geometric multiplicity exactly
`r-3`, with no quotient unit eigenvalue or hidden unit Jordan block. For
`d_n=e_r^{\mathsf T}C^n\mathbf1`, the article must derive the exact cubic
annihilator

\[
d_{n+3}=T_0d_{n+2}-S_0d_{n+1}+D_0d_n,
\]

where

\[
T_0=2h+4m^2+4m+5,\quad
S_0=h^2-8hm(m+1)+2h+4,\quad
D_0=h^2(2m+1)^2,
\]

and `d_0=1`, `d_1=h(2m+3)`. The cubic is an annihilator. It is not claimed
minimal or irreducible for every parameter, and `\rho(C)` is not claimed to
have algebraic degree exactly three for every parameter.

## Boundary and fixed-support coefficient contract

At the ordinary seed, the first score difference is exactly

\[
(g-1)-\bigl(1+2(r-1)\bigr)=g-2r.
\]

At `g=2r`, the first selector ties and
`\sigma(\mathbf1)=r-1=(g-2)/2` lies on the open height boundary. This is
sharpness only for the ordinary seed and the chosen strict selected face. It
is not a global failure or optimality theorem. The headline remains
`r\ge4`; the formal `r=3`, `m=1` substitution is a low-mode consistency
calculation only, not a new theorem or a correction.

The sole coefficient extension keeps the same fixed supports:

\[
\alpha\prod_{i=1}^r q_i^2+\beta q_1^g,
\qquad
\gamma\prod_{i=1}^r p_i^2+\delta p_r^g,
\qquad
\alpha,\beta,\gamma,\delta\in K^\times.
\]

The proof must use that `2\alpha`, `g\beta`, `2\gamma`, and `g\delta` are
nonzero in characteristic zero and that the uniquely selected leading source
survives in a polynomial domain. A zero coefficient, extra monomial, altered
support, different shear word, or positive-characteristic specialization is
outside the theorem.

## Public article, page, section, and table contract

The article has §0 Abstract followed by exactly eight numbered main sections:

1. Introduction and bounded positioning;
2. the family, polynomial inverses, and symplectic geometry;
3. gradient supports and the two strict selectors;
4. seed containment and strict cone invariance;
5. carried coordinates and leading-form survival;
6. last-coordinate visibility, exact degrees, and Perron growth;
7. unit modes, the equal-middle quotient, and cubic recurrence; and
8. sharp boundary, low-mode consistency, fixed-support coefficients,
   limitations, and conclusion.

The substantive page target is exactly `26.5` pages, with preferred band
`24--28` and hard band `22--30`, measured from the Abstract through the end
of the Conclusion and excluding references. Every theorem-critical proof
listed above must be in §§2--8. No appendix may supply or repair a missing
selector, cone wall, carry step, noncancellation argument, visibility bound,
invariant splitting, quotient calculation, cubic coefficient, multiplicity
argument, boundary audit, or coefficient proof.

Generated figures, plots, diagrams, images, assets, empirical tables,
experiments, datasets, numerical spectra, parameter scans, and CAS or symbolic
certificates are exactly zero. The public article may use at most three
hand-typeset mathematical tables, and only for these roles:

1. a gradient support-row ledger;
2. a selector/cone proof ledger; and
3. a three-dimensional invariant ledger for the trace, principal-minor sum,
   determinant, and cubic coefficients.

Any of those three may be omitted if the proof remains complete. No fourth
table is permitted. Internal claims--evidence matrices, source screens,
collision ledgers, file inventories, hashes, review histories, permission
ledgers, dashboards, or governance artifacts may not become public tables or
public prose.

## Exact citation and bibliography allowlist

The future bibliography pool is exactly the six verified records `S01`--`S06`
below. The recommended and frozen BibTeX keys are exact. Their roles are
context-only; none may prove or replace a theorem-critical calculation.

1. `S01` / `BlancVanSanten2021`: Jérémy Blanc and Immanuel van Santen,
   “Dynamical degrees of affine-triangular automorphisms of affine spaces,”
   arXiv:1912.01324, DOI `10.1017/etds.2021.90`. Permitted only for broader
   arbitrary-dimensional affine-triangular degree calculations and weak-
   Perron realization context.
2. `S02` / `ShaoSun2025`: Enbo Shao and Xiaosong Sun, “Dynamical degrees of
   affine-triangular automorphisms in dimension four,” arXiv:2509.14584.
   Permitted only for current dimension-four affine-triangular algebraic-
   degree context.
3. `S03` / `Deserti2016`: Julie Déserti, “Degree growth of polynomial
   automorphisms and birational maps: some examples,” arXiv:1602.04642.
   Permitted only for varied higher-dimensional polynomial-automorphism
   degree-growth context.
4. `S04` / `DangFavre2021`: Nguyen-Bac Dang and Charles Favre, “Spectral
   interpretations of dynamical degrees and applications,” *Annals of
   Mathematics* 194 (2021), DOI `10.4007/annals.2021.194.1.5`. Permitted only
   for general spectral context motivating an explicit visibility proof.
5. `S05` / `Rangarajan2002`: G. Rangarajan, “Polynomial map symplectic
   algorithm,” arXiv:physics/0212098. Permitted only for neighboring
   polynomial symplectic-map construction methodology.
6. `S06` / `FujiokaKogawaLiShudo2023`: Keisuke Fujioka, Ryota Kogawa, Jizhou
   Li, and Akira Shudo, “Coupled Hénon Map, Part I: Topological Horseshoes and
   Uniform Hyperbolicity,” arXiv:2303.05769. Permitted only for a neighboring
   coupled symplectic Hénon setting concerned with hyperbolicity.

There is no seventh citation record. No source may be used for proof transfer,
classification, firstness, uniqueness, priority, or an exhaustive-literature
claim. Context must be synthesized by mathematical question rather than by a
source-by-source novelty parade. As of this scope author stop, no stable public
identifier for a local low-mode predecessor is bound. Therefore the public
article must not cite, name, number, or bibliographically invent such an
object; the `r=3` calculation appears only as self-contained mathematical
consistency.

## Anti-claims and public-language firewall

The public source and PDF must not claim or imply:

1. that the selector cone is maximal, necessary, unique, exact, or a
   classification;
2. a theorem for arbitrary supports, added monomials, arbitrary potentials,
   arbitrary Hamiltonian or polynomial maps, or arbitrary shear words;
3. positive-characteristic validity;
4. universal irreducibility or minimality of `P_{m,h}`, or algebraic degree
   exactly three for every Perron root;
5. actual failure of degree dynamics at `g=2r`, or global optimality of
   `g\ge2r+1`;
6. a new `r=3` theorem, a correction to a predecessor, or novelty of the
   low-mode specialization;
7. topological, metric, arithmetic, or measure-theoretic entropy; periodic-
   point, trace, multiplier, torus, arithmetic-orbit, integrability, or
   invariant-variety conclusions;
8. genericity, non-conjugacy, classification, universality, or arbitrary
   Perron/weak-Perron realization;
9. absolute novelty, firstness, priority, uniqueness in the literature, or
   an exhaustive source screen; or
10. CAS, numerical iteration, a finite scan, an empirical table, an
    experiment, dataset, plot, or hidden computer certificate as evidence.

Public mathematical language must say “explicit sufficient invariant
selector cone,” “strict visibility for `n\ge1`,” “tied initial case at
`n=0`,” “seed/selected-face boundary,” “formal low-mode consistency,” and
“cubic annihilator” wherever the stronger but unproved alternatives could be
inferred.

## Current review gate: scope only

After stable author readback, the sole possible subsequent project write at
this gate is

`notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`.

It may be created only by a fresh independent reviewer who authored none of
this scope or its bound upstream inputs and who verifies the stable scope
bytes, exact metadata identity, mathematical formulas, section/page/table
contract, six-source boundary, anti-claims, public-source firewall, inventory,
and path permissions. The review file must be that reviewer's sole write.

If any conjunctive check fails, the instruction is exactly `WRITE NOTHING`:
create no review artifact and modify no path. If every check passes, the final
non-empty line of the sole review file must be exactly

`PUBLICATION_STAGE_PASS`.

`PUBLICATION_STAGE_PASS` has exactly one permission effect: it makes
`experiments/publication_lock.json` eligible for creation in a later,
separately authorized, lock-only author invocation. It does **not** directly
authorize `paper/main.tex`, `paper/math_commands.tex`,
`paper/references.bib`, manuscript prose, TeX, BibTeX, figures, assets, code,
science, a build, PDF, release, Paper 23, submission, upload, repository push,
messaging, identity disclosure, or any other external effect.

## Later publication-lock contract

Only after a valid independent `PUBLICATION_STAGE_PASS` may a distinct
publication-lock author be separately invoked. That author may write exactly
one path:

`experiments/publication_lock.json`.

The lock must be strict canonical UTF-8 JSON with one terminal LF, no
duplicate keys, no nonfinite values, recursively ordered object keys, compact
separators, and byte-exact canonical round trip. It must bind the complete
stable project universe present immediately before its write: absent any
drift, exactly 17 regular files, four child directories, and zero symlinks,
including this scope and the valid independent publication-stage review. It
must also enumerate the complete 18-regular-file author-stop universe after
its own creation. The publication lock is represented structurally in that
universe, but its self-referential byte count and SHA-256 must be `null` and
explicitly excluded. No upstream author or review artifact may be omitted,
rewritten, or absorbed silently.

The publication-lock author status must be exactly

`PUBLICATION_LOCK_AUTHOR_STOP / PENDING_FRESH_PUBLICATION_LOCK_REVIEW`.

At that author stop, the three future public source paths and every build/PDF
path remain absent and unauthorized. The fresh publication-lock reviewer's
sole possible write is

`notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md`.

A blocker again means exactly `WRITE NOTHING`. Only a fully passing reviewer
may create that sole file, and its final non-empty line must be exactly

`PUBLICATION_LOCK_PASS`.

`PUBLICATION_LOCK_PASS` may make only the following exact trio eligible for
one later, separately authorized, source-only author invocation:

- `paper/main.tex`;
- `paper/math_commands.tex`; and
- `paper/references.bib`.

Even that later PASS does not itself create or edit the trio, and it does not
authorize any fourth source path, figure, asset, code, experiment, dataset,
CAS run, build, PDF, release, Paper 23, submission, upload, repository push,
external message, identity disclosure, or other external effect.

## Zero-science and no-external-effect lock

This governance stage has exactly zero scientific experiments, numerical
runs, parameter scans, CAS or symbolic runs, datasets, plots, figures, GPU
actions, scientific network calls, external uploads, and results artifacts.
Read-only local validation of text, hashes, paths, and inventory is not
scientific evidence. No current or future reviewer may treat it as proof of a
headline theorem.

All transport, release, public hosting, submission, repository push, external
messaging, identity disclosure, and other external effects remain closed.
Nothing in this scope may be interpreted as publication, submission consent,
or communication authority.

## Exact scope-author-stop inventory

Immediately before this scope write, the Paper 22 project contained exactly
15 regular files, four child directories, and zero symlinks. After this sole
write it contains exactly 16 regular files, the same four child directories,
and zero symlinks.

The four child directories are exactly:

- `experiments`;
- `notes`;
- `paper`; and
- `refine-logs`.

The 16 regular files at scope-author stop are exactly:

- `experiments/EXPERIMENT_PLAN.md`;
- `experiments/EXPERIMENT_TRACKER.md`;
- `experiments/source_lock.json`;
- `notes/CITATION_VERIFICATION.md`;
- `notes/CLAIMS_EVIDENCE_MATRIX.md`;
- `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md`;
- `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`;
- `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`;
- `notes/NOVELTY_ASSESSMENT.md`;
- `notes/PROOF_PACKAGE.md`;
- `notes/PUBLICATION_STAGE_SCOPE.md`;
- `notes/RESEARCH_QUESTION.md`;
- `paper/PAPER_PLAN.md`;
- `refine-logs/FINAL_PROPOSAL.md`;
- `refine-logs/INITIAL_PROPOSAL.md`; and
- `refine-logs/REVIEW_SUMMARY.md`.

At this author stop, all of the following are absent and unauthorized:

- `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`;
- `experiments/publication_lock.json`;
- `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md`;
- `paper/main.tex`;
- `paper/math_commands.tex`;
- `paper/references.bib`; and
- every build, PDF, release, submission, transport, data, code, figure, asset,
  experiment, or external-action artifact.

The scope author performs stable readback, reports this file's external
SHA-256/byte/LF identity and the verified inventory to the governing role,
and then stops. No self-review PASS is claimed.

PUBLICATION SCOPE AUTHOR STOP
