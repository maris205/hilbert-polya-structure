# Independent Formal Paper-Source R1 Review — Paper 24

Date scope: 2026-08-25 UTC.

## 1. Reviewer role, authority, and method

I am the fresh independent formal source reviewer for
`papers/24-hamiltonian-period-two-selector-exchange`. I authored none of the
Paper 24 source trio, none of its repair regions, none of the 19 predecessor
project records, neither live root ledger, and none of the four immutable
candidate review/correction records.

Before auditing the source I read the complete local `paper-write` skill. I
then read through EOF:

1. all 22 regular files in the live Paper 24 project;
2. the current Paper 24 lifecycle tails in `BATCH_06_STATUS.md` and
   `BATCH_06_IDEA_REPORT.md`;
3. both immutable candidate reviews and both append-only correction records;
4. the source and publication locks and all prior independent review records;
5. `paper/main.tex`, `paper/math_commands.tex`, and
   `paper/references.bib` in full.

The audit was source-static and proof-adversarial. I used local hashing,
inventory checks, text extraction, and hand algebra only. I did not invoke a
TeX engine, BibTeX, a PDF tool, a scientific CAS, a network service, or any
path under `/tmp`. No source or predecessor file was modified. This review is
the sole conditional write.

The live gate occurred exactly once as
`PAPER24_FORMAL_SOURCE_R1_REVIEW_OPEN`. Immediately before this write the
review path was absent and the project contained exactly 22 regular files,
four child directories, zero symlinks, and zero other objects, with no TeX,
BibTeX, PDF, log, or auxiliary build artifact.

## 2. Exact prewrite identity and inventory binding

The two live governance roots matched the identities supplied for this gate:

| Record | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `BATCH_06_STATUS.md` | `907f9abe96c9dd666f805a690118d763204816c414d6f6ebc2ab74c8e70f1f2c` | 137,619 | 2,008 |
| `BATCH_06_IDEA_REPORT.md` | `19b55af7f0a1fb3d4104de3f2a904b3c29ce06bc5fc479a5f5202dadc5867d86` | 239,465 | 4,672 |

The four candidate records also remained exact:

| Record | SHA-256 | Bytes | LF | Terminal |
|---|---|---:|---:|---|
| R1 | `b2802f24ca5de3d91b7ea5a1726a0cf12d6f36053055e24e3759124bfc8709c1` | 30,703 | 878 | `PAPER24_CANDIDATE_GATE_PASS_R1` |
| R1 correction | `dabf9fa2873aa0124e2d510dc20b581b51a5648e0828f33bc2b7a41b2172730d` | 2,583 | 112 | `PAPER24_CANDIDATE_GATE_PASS_R1_CORRECTED` |
| R2 | `914b92255cd9aae2b8be4707484ebf63a72d1b40e1cf1fc356dd365676ed25bd` | 19,672 | 769 | `PAPER24_CANDIDATE_GATE_PASS_R2` |
| R2 correction | `1c311a979b3c8fc396734bbd851f1a6c8ed5738a2f3005048688f623a6bcaf6b` | 2,500 | 115 | `PAPER24_CANDIDATE_GATE_PASS_R2_CORRECTED` |

The exact 22-file prewrite project universe was:

| Relative path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `bfd644a19d15f51a4c7eca6323909852d38e7477afac73aea77b02642ffb6f94` | 7,098 | 186 |
| `experiments/EXPERIMENT_TRACKER.md` | `61e34652fdea217b0da4f7774478f243ca806fb88a97e18f09d767e24fbe8db0` | 3,459 | 59 |
| `experiments/publication_lock.json` | `a2f3a4e0a005972b60f8c5b2241889ec5fffc1841b83ada69d5b8b7582fcdb6a` | 57,325 | 1 |
| `experiments/source_lock.json` | `45ce6527917d7172ff10e87db1e716b6e7caa2de3fa3cfbd54cd73b034003232` | 45,607 | 1 |
| `notes/CITATION_VERIFICATION.md` | `66558b974ebdcc0fd7627c52c4caee0c80b404514d06f622ededd9b9a8900fb9` | 6,694 | 93 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `28f8f3dd6add8617a63c16b5d6956d5a1214dc453a2416721dca824faba00dc5` | 7,040 | 114 |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | `4d642580cad2dec337249cb0a11acbb662ae640a8d5faf44077f6ec2be354d68` | 20,521 | 483 |
| `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md` | `e91bcda341469dfbb877d70fe0daeace876570b3696ef6fc0b881851fe7c9075` | 21,751 | 435 |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `c11b139759e7951ee5e13617537f60caaad04124638c9c64b95e5071af334972` | 10,735 | 240 |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | `1c733058483cb28370e4c6f283126c14305ce45de43010e7753a4d92a5f8ece8` | 16,630 | 490 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `a420a26fbf3a535aedafdfd701969db8084b932e2ae9e6d806570c460090abea` | 24,533 | 754 |
| `notes/NOVELTY_ASSESSMENT.md` | `e873bcdc57c0f39e04b950bf9221c894993370c1accd313cbcb05495fa92fb2c` | 5,532 | 119 |
| `notes/PROOF_PACKAGE.md` | `b6df4be9e9a00a5ae71e48505b007a59fea70bcff3046661af804714378963bf` | 18,290 | 1,048 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `c0354c4621afcdfe79d5bddad035b378f6a4917e4c69a570971419ef5e80f762` | 46,832 | 1,331 |
| `notes/RESEARCH_QUESTION.md` | `5dc091d3500800610360512f464a877adb51c1f83857c8335a28dccebd35ef7d` | 5,052 | 132 |
| `paper/PAPER_PLAN.md` | `ee5c320f800919543411b147b5d1484d33c577a56519121b9b4883fdff8122ad` | 36,690 | 586 |
| `paper/main.tex` | `1008cfa8c691d06645b79f33de00044df45e97a18b6d5a0f6ded2431f1df8f4e` | 67,011 | 1,707 |
| `paper/math_commands.tex` | `8c3f90e67d48b1773f5582b21e8bd6f805a22e40ea23a5bbeffb40ab7da7298e` | 605 | 20 |
| `paper/references.bib` | `4acd9cad4609fabfea4c8b4504a6fde11ff7de8b0a2952b6723678f10093af0b` | 3,556 | 118 |
| `refine-logs/FINAL_PROPOSAL.md` | `bf04aa95c67b19bc876c594b8162534c7000f12a92fc696017d36bf9cf7e96bf` | 4,773 | 175 |
| `refine-logs/INITIAL_PROPOSAL.md` | `7e5d64d5c4d3029d8d9d10f82c5dee41e66c5c2fb9cc3271e203657eeb74a8dc` | 3,971 | 148 |
| `refine-logs/REVIEW_SUMMARY.md` | `b2357b00fb2a9e05dbc96db775be9ef6a243e164b5b720525ecef9b3bd220c82` | 4,233 | 102 |

The byte-sorted text manifest consisting of
`SHA256 bytes LF relative-path` rows had SHA-256
`c25438718e4b33550929873f8d5691becb895016ef122a98dc68c318aebe2e9c`.

## 3. Direct read-only adversary clearance

The parent clarified that the distinct zero-write adversary ran under the
authorized canonical role `/root/syntax_python_author` because the originally
requested canonical name was unavailable under the thread limit. I received
its direct `READONLY_ADVERSARY_CLEAR` message before writing.

That direct message bound the same source trio:

| Source | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `paper/main.tex` | `1008cfa8c691d06645b79f33de00044df45e97a18b6d5a0f6ded2431f1df8f4e` | 67,011 | 1,707 |
| `paper/math_commands.tex` | `8c3f90e67d48b1773f5582b21e8bd6f805a22e40ea23a5bbeffb40ab7da7298e` | 605 | 20 |
| `paper/references.bib` | `4acd9cad4609fabfea4c8b4504a6fde11ff7de8b0a2952b6723678f10093af0b` | 3,556 | 118 |

The adversary reported no critical or major finding after independently
checking the theorem chain, the repaired limit argument, source structure,
bibliography closure, syntax, metadata, and artifact absences. It performed
no write, compilation, network access, or `/tmp` access.

## 4. Public identity, abstract, article shape, and firewall

The public identity is exact:

- source and visible title are `Forced Period-Two Selector Exchange in
  Two-Mode Hamiltonian Product Shears`;
- source and visible author are exactly `Anonymous`;
- the source date is exactly empty through `\date{}`;
- `pdftitle` is the full exact title;
- `pdfauthor`, `pdfcreator`, and `pdfproducer` are explicitly empty;
- date/trailer suppression conditionals introduce no identity;
- no affiliation, email, ORCID, acknowledgment, funding text, venue marker,
  internal path, hash, review role, lifecycle token, predecessor number, or
  hidden public metadata field appears in the source trio.

The repaired abstract now contains exactly the four frozen categories:

1. the explicit characteristic-zero family and arbitrary-nonzero-coefficient
   scope;
2. strict period-two exchange between the open chambers, with no wall claim;
3. the exact dynamical degree and stride-two recurrence;
4. the bounded carry/visibility/parity contribution and explicit absence of a
   priority claim.

It does not promote the conditional period-(k) lemma, add a fifth
contribution, cite literature, expose governance, or claim priority.

There is one abstract and exactly eight numbered sections, with the locked
titles and order:

1. Introduction, theorem preview, and bounded positioning;
2. Family, inverses, symplecticity, and support rows;
3. Common wall, branch algebra, and strict selector exchange;
4. Temporal carry and arbitrary-nonzero top homogeneous survival;
5. (q_1) visibility, monodromy, determinant, and spectrum;
6. Recurrence, wall gaps, parity closed forms, and integrality;
7. Bounded structural lemma and conditional period-(k) lemma;
8. Boundaries, coefficient scope, limitations, and conclusion.

The source has exactly three hand-typeset mathematical tables: the selector
and branch ledger, the carry and visibility ledger, and the degree-law ledger.
There is no fourth table, figure environment, graphics inclusion, figure or
asset directory, appendix command, appendix environment, proof appendix,
empirical table, code listing, dataset, or computational certificate.

Static mass is credible for the locked proof-first article contract: the main
source has 1,707 LF and about 6.6 thousand visible words, with substantial
displayed derivations and three dense mathematical tables. That supports the
22--30 content-page band and the 26.0-page design target as a static source
assessment. Actual rendered pagination remains deliberately deferred to a
later separately authorized deterministic build.

## 5. Bibliography and bounded citation audit

I extracted all citation keys from the TeX and all entry keys/types from the
BibTeX. There are exactly nine cited keys, exactly nine defined keys, no
missing citation, no uncited entry, no duplicate entry, and no tenth key.
S01--S08 are `article` records and S09 is the sole `misc` record.

| ID | Exact key | Type | Frozen identity summary |
|---|---|---|---|
| S01 | `BellonVialletAlgebraicEntropy` | article | Bellon--Viallet, *Algebraic Entropy*, CMP 204(2), 425--437 (1999), DOI `10.1007/s002200050652`, `chao-dyn/9805006v3` |
| S02 | `HasselblattProppMonomialDegreeGrowth` | article | Hasselblatt--Propp, ETDS 27(5), 1375--1397 (2007), DOI `10.1017/S0143385707000168`, `math/0604521v5` |
| S03 | `FordyHoneSymplecticCluster` | article | Fordy--Hone, SIGMA 7, Paper 091 (2011), DOI `10.3842/SIGMA.2011.091`, `1105.2985v2` |
| S04 | `FordyHoneClusterPoisson` | article | Fordy--Hone, CMP 325(2), 527--584 (2014), DOI `10.1007/s00220-013-1867-y`, `1207.6072v2` |
| S05 | `IshibashiKanoSignStableEntropy` | article | Ishibashi--Kano, Geometriae Dedicata 214(1), 79--118 (2021), DOI `10.1007/s10711-021-00606-1`, `1911.07587v5` |
| S06 | `JaneczkoJelonekPolynomialSymplectomorphisms` | article | Stanisław Janeczko--Zbigniew Jelonek, BLMS 40(1), 108--116 (2008), DOI `10.1112/blms/bdm112` |
| S07 | `BlancVanSantenAffineTriangular` | article | Blanc--van Santen, ETDS 42(12), 3551--3592 (2022), DOI `10.1017/etds.2021.90`, `1912.01324v2` |
| S08 | `DangFavreSpectralInterpretations` | article | Dang--Favre, Annals 194(1), 299--359 (2021), DOI `10.4007/annals.2021.194.1.5`, `2006.10262v2` |
| S09 | `ShaoSunDimensionFour` | misc | Shao--Sun, `arXiv:2509.14584v1` (2025), arXiv DOI `10.48550/arXiv.2509.14584` |

The S09 treatment is correctly access-limited. The source records only the
frozen arXiv v1 identity and `misc` status. The manuscript uses it solely as
a nearby affine-triangular comparison and explicitly refuses to infer an
affine-triangular realization or noncollision statement. The governing fact
that no journal reference, version-of-record page, or non-arXiv publisher DOI
was verified as of 2026-08-25 is a bounded metadata result, not an absolute
claim that no publication exists.

All literature use is contextual. No source is used to prove a gradient,
symplecticity, selector, carry, no-cancellation, visibility, matrix,
eigenpair, recurrence, wall-gap, or structural-lemma identity. The prose
makes no firstness, priority, or exhaustive-noncollision claim.

## 6. Static source integrity

The three source files are ordinary mode-0644 regular non-symlinks, valid
UTF-8, BOM-free, CR-free, NUL-free, LF-only, and terminated by one LF.

Independent extraction gave:

- 75 labels, all 75 unique;
- 113 `ref`/`eqref` uses, with zero undefined target;
- 106 environment beginnings and 106 matching endings, with a clean nesting
  stack;
- 978 opening and 978 closing braces;
- 93 opening and 93 closing brackets;
- nine unique citation uses and nine matching BibTeX entries;
- zero TODO, FIXME, XXX, `[VERIFY]`, stale-input, or AI-watchword marker;
- no internal-governance or identity leakage.

Some equation labels are intentionally available as local proof anchors
without a later cross-reference; this is harmless. Every reference actually
used resolves uniquely. The source imports only `math_commands.tex` and ends
with the single `references` bibliography. No stale section file or hidden
fourth source path exists.

## 7. Independent theorem-chain audit

### 7.1 Maps, inverses, and symplecticity

Literal differentiation gives

\[
\partial_{q_1}V_m=mAq_1^{m-1}q_2^2+Bq_2^{2m},\qquad
\partial_{q_2}V_m=2Aq_1^mq_2+2mBq_1q_2^{2m-1},
\]

\[
\partial_{p_1}W_{m,s}=(s(2m+1)+1)Cp_1^{s(2m+1)},\qquad
\partial_{p_2}W_{m,s}=(sm+1)Dp_2^{sm}.
\]

The subtraction formulas for (S^{-1}) and (T^{-1}) are exact polynomial
inverses. In the coordinate order ((q_1,q_2,p_1,p_2)), their Jacobians have
the lower- and upper-Hessian shear blocks. Symmetry of both Hessians makes
(J_S^{\mathsf T}\Omega J_S=\Omega) and
(J_T^{\mathsf T}\Omega J_T=\Omega). Therefore (S,T,F_{m,s}) are
polynomial automorphisms preserving the stated standard symplectic form.

### 7.2 Common wall, selectors, branches, and strict itinerary

The mixed-minus-pure differences in both gradient coordinates are exactly

\[
(m-1)(u_1-2u_2).
\]

Thus the common tie wall is (r=u_1/u_2=2), with

\[
A_-=
\begin{pmatrix}0&2m\\1&2m-1\end{pmatrix},\qquad
A_+=
\begin{pmatrix}m-1&2\\m&1\end{pmatrix},\qquad
B_m=\operatorname{diag}(2m+1,m).
\]

The branch maps are

\[
h_m(r)=\frac{2(2m+1)}{r+2m-1},\qquad
\ell_m(r)=\frac{(2m+1)((m-1)r+2)}{m(mr+1)}.
\]

Direct subtraction reproduces all corrected differences:

\[
h_m(r)-2=\frac{2(2-r)}{r+2m-1},
\]

\[
\ell_m(r)-1=\frac{(m^2-m-1)r+3m+2}{m(mr+1)},\qquad
2-\ell_m(r)=\frac{(m+1)(r-2)}{m(mr+1)}.
\]

Hence (0<r<2) maps strictly above two, while (r>2) maps strictly
into ((1,2)). The ordinary seed has (r_0=1), so the itinerary is
strictly (A_-,A_+,A_-,A_+,\ldots), and no wall convention is used.

### 7.3 Both temporal carry phases

At the seed,

\[
A_-(1,1)^{\mathsf T}=(2m,2m)^{\mathsf T}>(1,1)^{\mathsf T},
\]

and the following pure-power phase also beats the position seed.

For later steps, the carried momentum degrees are

\[
\left(\frac{u_{n,1}}{s(2m+1)},\frac{u_{n,2}}{sm}\right).
\]

In the negative chamber the selected vector is

\[
(2mu_{n,2},\ u_{n,1}+(2m-1)u_{n,2})^{\mathsf T};
\]

in the positive chamber it is

\[
((m-1)u_{n,1}+2u_{n,2},\ mu_{n,1}+u_{n,2})^{\mathsf T}.
\]

Each entry strictly beats its carried momentum entry, and multiplication by
(s(2m+1)) and (sm) then strictly beats the carried position entry. All
four chamberwise comparisons hold already at (s=1). Selector choice is
therefore promoted to actual temporal degree transport without an asymptotic
shortcut.

### 7.4 Arbitrary-nonzero top-form survival

Off the wall each derivative coordinate has one unique highest-degree support
source. After substitution its top homogeneous part is a nonzero derivative
scalar times (A) or (B) and powers of already nonzero position top forms.
The pure-power phase similarly uses a nonzero scalar times (C) or (D) and
a positive power of a nonzero momentum top form. The polynomial ring over a
field is a domain, and strict carry keeps every older coordinate at lower
degree. Characteristic zero keeps all derivative scalars nonzero. This proves
survival for every (A,B,C,D\in K^\times), not merely generic or positive
coefficients.

### 7.5 (q_1) visibility and true total degree

Every positive-step branch image is greater than one, so (u_{n,1}>u_{n,2}).
In the negative chamber the controlling relation is the corrected equality

\[
u_{n+1,1}=sm\,h_m(r_n)v_{n+1,2}>v_{n+1,2},
\]

not a substituted strict sign. In the positive chamber,

\[
u_{n+1,1}-v_{n+1,2}
=s(2m+1)((m-1)u_{n,1}+2u_{n,2})-(mu_{n,1}+u_{n,2})>0.
\]

Also (u_{n+1,1}=s(2m+1)v_{n+1,1}>v_{n+1,1}) in both chambers.
Therefore (q_1) is strictly maximal among all four coordinates for every
positive iterate, while (d_0=1) is correctly retained as a tied seed.

### 7.6 Monodromy, eigenpairs, trace, determinant, and spectral order

The temporal product is correctly ordered:

\[
P_m=(B_mA_+)(B_mA_-)
=\begin{pmatrix}
2m(2m+1)&2m(2m+1)(2m^2+m-2)\\
m^2&m^2(4m^2+4m-1)
\end{pmatrix}.
\]

Direct multiplication verifies both right eigenpairs:

\[
P_m(2,1)^{\mathsf T}=H(2,1)^{\mathsf T},\qquad
H=m^2(2m+1)^2,
\]

and

\[
P_m(-(2m+1)(2m^2+m-2),m)^{\mathsf T}
=L(-(2m+1)(2m^2+m-2),m)^{\mathsf T},
\]

with (L=2m(m+1)). The trace is exactly (H+L). The manuscript does not
infer the determinant from the proposed eigenvalues; it expands (ad-bc):

\[
\det P_m
=2m^3(2m+1)((4m^2+4m-1)-(2m^2+m-2))
=2m^3(m+1)(2m+1)^2=HL.
\]

Finally,

\[
H-L=m(4m^3+4m^2-m-2)>0
\]

for (m\ge2). The two-step monodromy is (s^2P_m), and the nonzero
dominant seed component remains visible after the odd prefix. Thus

\[
\lambda_1(F_{m,s})=sm(2m+1).
\]

### 7.7 Recurrence, initials, wall gaps, parity laws, and integrality

Cayley--Hamilton for (P_m), with the powers of (s) restored on each
parity class, gives

\[
d_{n+4}=s^2(H+L)d_{n+2}-s^4HLd_n.
\]

Direct multiplication gives the exact initials

\[
d_0=1,\quad d_1=2m(2m+1)s,
\]

\[
d_2=2m(m+1)(2m-1)(2m+1)s^2,\quad
d_3=8m^4(m+1)(2m+1)s^3,
\]

and the corrected full third vector

\[
u_3=\begin{pmatrix}
8m^4(m+1)(2m+1)s^3\\
2m^2(m+1)(2m-1)(2m^2+2m+1)s^3
\end{pmatrix}.
\]

For the wall functional (w=(1,-2)),

\[
wC_-=-2ms\,w,\qquad wC_+=-(m+1)s\,w.
\]

Since (wu_0=-1), this gives exactly

\[
u_{2j,1}-2u_{2j,2}=-(s^2L)^j,\qquad
u_{2j+1,1}-2u_{2j+1,2}=2ms(s^2L)^j.
\]

The seed decomposition into the (H)- and (L)-eigenvectors reproduces the
full even-vector formula and both visible parity formulas. Applying (w)
cancels the (H)-component and recovers the wall laws. Integrality follows
from the integer matrices and integer seed, equivalently from the
integer-coefficient recurrence and integer initials; it is not inferred from
the rational-looking diagonalized denominators.

### 7.8 Bounded crossed-binomial criterion

For

\[
V=Aq_1^aq_2^b+Bq_1^cq_2^d,\qquad
a>c\ge1,\quad d>b\ge1,
\]

both derivative comparisons have wall

\[
R=\frac{d-b}{a-c}.
\]

For either selected exponent ((x,y)), the branch

\[
g_{x,y}(r)=\frac ef\frac{(x-1)r+y}{xr+y-1}
\]

is strictly decreasing, and both branches have the same wall value. The two
global open-chamber implications therefore hold if and only if

\[
\frac ef=\frac{R(L_{\mathrm{wall}}-1)}{L_{\mathrm{wall}}-R}.
\]

For ((a,b,c,d)=(m,2,1,2m)), this gives (R=2),
(L_{\mathrm{wall}}=2m+2), and (e/f=(2m+1)/m). The repaired coprimality
proof is exact: every common divisor of (m) and (2m+1) divides
((2m+1)-2m=1). Hence all positive integral realizations are precisely
((e,f)=s(2m+1,m)). Carry, top-form survival, and visibility remain separate
obligations and are not smuggled into this bounded selector criterion.

### 7.9 Repaired conditional period-(k) lemma and actual root limit

The lemma retains exactly six hypotheses: unique strict selection, strict
carry, nonzero top forms in a domain, linear degree transport in temporal
order, full-degree visibility on every residue class, and Perron-class
visibility.

The repaired sixth hypothesis is strong enough. For each residue (j), it
groups the spectral-circle Jordan terms at the maximal surviving polynomial
order (h_j) and requires their coefficient, after normalization by
(\rho^\ell\ell^{h_j}), to stay uniformly bounded away from zero for all
sufficiently large ℓ. This excludes both permanent and oscillatory
equal-modulus cancellation.

The Jordan expansion then supplies, on every residue class,

\[
|a_{\ell,j}|\le C_j\ell^{r-1}\rho^\ell
\]

and

\[
|a_{\ell,j}|\ge c_j\ell^{h_j}\rho^\ell
\]

for all sufficiently large ℓ. Consequently

\[
\lim_{\ell\to\infty}|a_{\ell,j}|^{1/\ell}=\rho,
\qquad
\lim_{\ell\to\infty}d_{k\ell+j}^{1/(k\ell+j)}=\rho^{1/k}.
\]

Because the finitely many residue limits agree, the full root limit exists;
the proof no longer establishes merely a limsup.

The exact (k=2) family satisfies the strengthened condition. The even seed
decomposition has a fixed positive, nonzero (H)-eigencomponent; the odd
prefix maps the dominant eigenvector to the same direction with positive
factor (sm(2m+1)); and (L<H), so there is no competing spectral-circle
class. Thus (h_0=h_1=0) and the normalized dominant coefficients are fixed
nonzero constants on both parities.

## 8. Boundaries, anti-claims, and repair containment

The source explicitly preserves every hard boundary:

- no theorem on the tie wall (r=2);
- no (m=1) or positive-characteristic extension;
- no zero coefficient, added support, or reversed phase order;
- no classification outside the crossed-binomial / diagonal-pure-power
  ansatz;
- no maximal selector fan, period greater than two realization, automaton, or
  arbitrary shear-word theorem;
- no inverse-degree, entropy-equality, integrability, genericity,
  periodic-point, arithmetic-orbit, or nonconjugacy theorem;
- no novelty claim for the conditional period-(k) implication;
- no first Perron, first weak-Perron, first tropical switching, first
  symplectic-shear, or absolute-priority claim;
- no theorem evidence from CAS, numerics, finite iterates, scans, code, or
  data.

The bounded R0 repair is contained exactly as recorded by the live roots:

1. the abstract was restricted to the four allowed categories;
2. the adjacent filler transition was replaced by direct proof-order prose;
3. the false “consecutive integers” explanation was replaced by the exact
   divisor subtraction;
4. hypothesis (6) was strengthened by the uniform spectral-circle lower
   bound; and
5. the Jordan proof was extended to matching residue-wise upper and lower
   bounds and the true full limit.

The current five source regions implement precisely those repairs and no
claim expansion. `paper/math_commands.tex` and `paper/references.bib` retain
their R0 identities. Every one of the 19 pre-source project files retains its
frozen publication-lock identity, and the other 21 project files match the
pre-repair stability record. No source path, metadata field, theorem formula,
citation key, section, table, asset, or downstream permission drifted.

## 9. Disposition and authority boundary

I found no critical or major source defect, no mathematical gap, no static
source blocker, no citation or metadata drift, and no permission leak. All
conjunctive source-review checks pass, including the independent direct
adversary condition.

This disposition does not authorize compilation, TeX/BibTeX execution, PDF
creation, source revision, release, submission, upload, hosting, repository
push, transport, messaging, identity disclosure, Paper 25 work, or any
external effect. It makes only a later separate parent transition eligible to
open the deterministic R0 build stage.

PAPER_SOURCE_R1_PASS
