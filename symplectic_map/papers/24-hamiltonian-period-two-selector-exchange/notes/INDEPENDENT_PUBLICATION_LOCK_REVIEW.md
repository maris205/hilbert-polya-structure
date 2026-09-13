# Independent Publication-Lock Review — Paper 24

Date: 2026-08-25 UTC  
Reviewer role: fresh independent publication-lock reviewer

## 1. Scope, independence, and method

I authored none of `experiments/publication_lock.json`, its seventeen bound
predecessor files, the four candidate review/correction records, either live
Batch 06 root ledger, the frozen R0 scope snapshot, or any upstream review.
Before writing this artifact I read through EOF the complete eighteen-file
Paper 24 author-stop universe, both live root ledgers, the frozen R0 snapshot,
all four candidate records, and every upstream artifact named by the lock.

The audit was conjunctive. It covered exact bytes and filesystem types,
strict-canonical JSON under two independent implementations, both aggregate
commitments, historical and live governance, correction precedence, the full
written proof, citation metadata and access limits, article architecture,
anonymity, the public/private firewall, anti-claims, scientific-execution
counters, lifecycle state, and permissions. Arithmetic replay was used only
to attack the already written proof; it did not substitute for reading that
proof.

No scientific run, CAS or symbolic certificate, code or data artifact,
networked scientific action, source authoring, build, PDF, release, external
message, or other external effect occurred. This file is the sole project
write made by this reviewer.

## 2. Opening lock identity and exact author-stop universe

The publication lock opened as an ordinary mode-`0644` non-symlink file with
the following external identity:

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/publication_lock.json` | `a2f3a4e0a005972b60f8c5b2241889ec5fffc1841b83ada69d5b8b7582fcdb6a` | 57,325 | 1 |

It declares schema `paper24.publication_lock.v1`, version `1`, status
`PUBLICATION_LOCK_AUTHOR_STOP`, and next state
`PENDING_FRESH_PUBLICATION_LOCK_REVIEW`. Its internal self-byte and
self-SHA-256 fields are both exactly `null`, as required to avoid
self-reference.

I independently recomputed every bound predecessor fact rather than accepting
the lock table:

| Relative path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `bfd644a19d15f51a4c7eca6323909852d38e7477afac73aea77b02642ffb6f94` | 7,098 | 186 |
| `experiments/EXPERIMENT_TRACKER.md` | `61e34652fdea217b0da4f7774478f243ca806fb88a97e18f09d767e24fbe8db0` | 3,459 | 59 |
| `experiments/source_lock.json` | `45ce6527917d7172ff10e87db1e716b6e7caa2de3fa3cfbd54cd73b034003232` | 45,607 | 1 |
| `notes/CITATION_VERIFICATION.md` | `66558b974ebdcc0fd7627c52c4caee0c80b404514d06f622ededd9b9a8900fb9` | 6,694 | 93 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `28f8f3dd6add8617a63c16b5d6956d5a1214dc453a2416721dca824faba00dc5` | 7,040 | 114 |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | `4d642580cad2dec337249cb0a11acbb662ae640a8d5faf44077f6ec2be354d68` | 20,521 | 483 |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `c11b139759e7951ee5e13617537f60caaad04124638c9c64b95e5071af334972` | 10,735 | 240 |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | `1c733058483cb28370e4c6f283126c14305ce45de43010e7753a4d92a5f8ece8` | 16,630 | 490 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `a420a26fbf3a535aedafdfd701969db8084b932e2ae9e6d806570c460090abea` | 24,533 | 754 |
| `notes/NOVELTY_ASSESSMENT.md` | `e873bcdc57c0f39e04b950bf9221c894993370c1accd313cbcb05495fa92fb2c` | 5,532 | 119 |
| `notes/PROOF_PACKAGE.md` | `b6df4be9e9a00a5ae71e48505b007a59fea70bcff3046661af804714378963bf` | 18,290 | 1,048 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `c0354c4621afcdfe79d5bddad035b378f6a4917e4c69a570971419ef5e80f762` | 46,832 | 1,331 |
| `notes/RESEARCH_QUESTION.md` | `5dc091d3500800610360512f464a877adb51c1f83857c8335a28dccebd35ef7d` | 5,052 | 132 |
| `paper/PAPER_PLAN.md` | `ee5c320f800919543411b147b5d1484d33c577a56519121b9b4883fdff8122ad` | 36,690 | 586 |
| `refine-logs/FINAL_PROPOSAL.md` | `bf04aa95c67b19bc876c594b8162534c7000f12a92fc696017d36bf9cf7e96bf` | 4,773 | 175 |
| `refine-logs/INITIAL_PROPOSAL.md` | `7e5d64d5c4d3029d8d9d10f82c5dee41e66c5c2fb9cc3271e203657eeb74a8dc` | 3,971 | 148 |
| `refine-logs/REVIEW_SUMMARY.md` | `b2357b00fb2a9e05dbc96db775be9ef6a243e164b5b720525ecef9b3bd220c82` | 4,233 | 102 |

Every predecessor was an ordinary mode-`0644` regular non-symlink, valid
UTF-8, BOM-free, CR-free, NUL-free, LF-only, and terminal-LF-terminated. The
seventeen byte-sorted relative paths independently yielded:

| Aggregate | Recomputed result |
|---|---|
| file count | `17` |
| total bytes / LF | `267690 / 6061` |
| sorted text ledger | `1811` bytes, SHA-256 `cc83a3e07802f61c9c2470405236fea53da2533d736fbb4fddfe1bd563a7edb2` |
| uint64-BE name/content-length-framed stream | `268492` bytes, SHA-256 `8f881199a9cb4a30937adf553e22ff3a619a01df29bc15ae964e101a9dfff8c7` |

I reproduced those totals, ledger bytes, framing bytes, and digests once in
Python and again in Node with independently written traversal, byte sorting,
line counting, hashing, and framing logic.

Before this review write the project contained exactly eighteen regular
files, the four child directories `experiments`, `notes`, `paper`, and
`refine-logs`, zero symlinks, and zero other objects. The review path, all
three future source paths, and every build/code/data/figure/result/release/
submission/transport artifact were absent.

## 3. Strict-canonical JSON audit

### 3.1 Independent Python implementation

The Python implementation began at raw bytes and enforced valid UTF-8, no
BOM/CR/NUL, exactly one physical JSON line, exactly one terminal LF, no lone
surrogate code point, and no leading or trailing record. It used a
duplicate-aware `object_pairs_hook`, rejected floating and nonfinite tokens,
walked every value recursively, required integer JSON numbers, required every
object's written keys already to be in Unicode code-point order, and then
re-encoded with compact separators, semantic array order, Unicode output, and
recursive sorted keys. The re-encoded bytes plus terminal LF matched all
57,325 original bytes exactly.

Adversarial cases rejected or detected by this implementation included a
duplicate key, decimal and exponent numbers, `NaN`, both infinities, a
trailing record, BOM, CRLF, NUL, missing or extra terminal LF, multiple JSON
records, a lone surrogate, and noncanonical object order.

### 3.2 Separately implemented custom Node parser and encoder

The Node implementation did not use `JSON.parse` or `JSON.stringify` for the
canonical decision. A recursive-descent parser manually handled objects,
arrays, literals, integer tokens, strings, escapes, surrogate pairs,
duplicate detection, and trailing-input rejection. A separate encoder
manually escaped strings, compared object keys by Unicode scalar values,
preserved array order, sorted only object keys, and emitted compact bytes.
Its encoded bytes plus terminal LF also matched the lock byte-for-byte.

Its adversarial suite independently rejected duplicate names, fractional and
exponent numbers, leading-zero integers, nonfinite tokens, trailing records,
lone high and low surrogates, BOM, CR, NUL, missing LF, and multiple records.
A supplementary-plane-versus-BMP key test confirmed true code-point ordering
rather than accidental UTF-16 ordering.

Both implementations therefore agree that the lock is one strict-canonical
UTF-8 JSON object, arrays retain declared semantic order, all object keys are
recursively canonical, and the self-null exclusion is genuine.

## 4. Root, candidate, correction, and upstream provenance

The live roots at review opening were ordinary stable mode-`0644` files:

| Root record | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `BATCH_06_STATUS.md` | `8f285465f24805d32c680d31b33dddb7e498f4b635107f92202a3054ed0eb561` | 132,220 | 1,931 |
| `BATCH_06_IDEA_REPORT.md` | `ed515b97c6476e56e1a92a825c3ce1b988c8f4cf06ea3918970733403615262e` | 231,063 | 4,521 |
| `BATCH_06_PAPER24_PUBLICATION_STAGE_SCOPE_BLOCKED_R0.md` | `c3a195d89b90fb8c4d17885b98e8f7a0592539fbfd266bddf4a8629a9e91dc8b` | 46,805 | 1,331 |

I proved the live status transition rather than accepting its description. I
removed the unique complete EOF author-stop suffix beginning with the
publication-lock-author activity entry, restored the current gate from review
to authoring, and restored the exact prior Paper 24 row whose stage was
“repaired publication scope passed fresh independent review; only a distinct
publication-lock author is open” and whose queue was
`PUBLICATION_STAGE_PASS_PUBLICATION_LOCK_OPEN`. The reconstructed predecessor
is exactly 130,639 bytes, 1,908 LF, SHA-256
`5b5d4276f8933016c3f64102145b07dc651fd08f054b5fb68c9b731b688750b9`.

I likewise removed the unique complete EOF addendum headed “Paper 24
Publication-Lock Author Stop and Review Gate” from the live Idea Report,
without adding a newline. The reconstructed predecessor is exactly 228,374
bytes, 4,470 LF, SHA-256
`d002698312ad27a62ad3ec32dc58979f6fd0bbf66fa3cb0b0afc19c6ec0629fd`.
The frozen rejected R0 scope snapshot remained byte-identical at the identity
shown above.

The four candidate provenance records also matched independently recomputed
identities and exact terminal lines:

| Record | SHA-256 | Bytes | LF | Terminal |
|---|---|---:|---:|---|
| R1 | `b2802f24ca5de3d91b7ea5a1726a0cf12d6f36053055e24e3759124bfc8709c1` | 30,703 | 878 | `PAPER24_CANDIDATE_GATE_PASS_R1` |
| R1 correction | `dabf9fa2873aa0124e2d510dc20b581b51a5648e0828f33bc2b7a41b2172730d` | 2,583 | 112 | `PAPER24_CANDIDATE_GATE_PASS_R1_CORRECTED` |
| R2 | `914b92255cd9aae2b8be4707484ebf63a72d1b40e1cf1fc356dd365676ed25bd` | 19,672 | 769 | `PAPER24_CANDIDATE_GATE_PASS_R2` |
| R2 correction | `1c311a979b3c8fc396734bbd851f1a6c8ed5738a2f3005048688f623a6bcaf6b` | 2,500 | 115 | `PAPER24_CANDIDATE_GATE_PASS_R2_CORRECTED` |

The exact local correction precedence is complete and contains no fifth
correction: the corrected numerator of \(\ell_m-1\), the equality before the
negative-chamber visibility inequality, the missing factor \(m+1\) in
\(2-\ell_m\), and the corrected second coordinate of \(u_3\). Separately,
the frozen R0-to-R1 scope diff contains exactly seven changed metadata lines:
three for S01, two for S04, one for S05, and one for S06. No other R0 scope
byte changed, and S09 remained unchanged.

The ten source-design author files independently reproduced 66,142 bytes and
2,176 LF, a 1,038-byte sorted ledger at SHA-256
`51364bd0e7c56055f17956248cc9f12bd10de6679638e8a90411394e89b51e88`,
and a 66,590-byte framed stream at SHA-256
`ca447f74449cee1f04c9f6181c2325b2350a975e59a8624aa8705b350f7e8e67`.
The source lock itself remained strict-canonical schema
`paper24.source_lock.v1`, with null self bytes and digest.

The paper plan, paper-plan review, publication scope, publication-stage
review, source-design review, source lock, and source-lock review all matched
the lock's exact bytes, LF, hashes, and terminal records. In particular, the
controlling upstream publication-stage review is 10,735 bytes / 240 LF /
SHA-256 `c11b139759e7951ee5e13617537f60caaad04124638c9c64b95e5071af334972`
and ends with its sole `PUBLICATION_STAGE_PASS`.

## 5. Independent theorem and written-proof audit

### 5.1 Family, phase order, and symplecticity

The lock freezes a characteristic-zero field \(K\), integers \(m\ge2\) and
\(s\ge1\), arbitrary nonzero \(A,B,C,D\in K\), and

\[
V_m=Aq_1^m q_2^2+Bq_1q_2^{2m},\qquad
W_{m,s}=Cp_1^{s(2m+1)+1}+Dp_2^{sm+1}.
\]

Literal differentiation gives the four frozen gradient coordinates. The
subtraction inverses are exact. The Hessian blocks in
\(J_S=\begin{psmallmatrix}I&0\\H_V&I\end{psmallmatrix}\) and
\(J_T=\begin{psmallmatrix}I&H_W\\0&I\end{psmallmatrix}\) are symmetric, so
both shears preserve the standard symplectic form. The forward phase order is
unambiguously \(F=T\circ S\), with \(T\) acting on the updated momenta.

### 5.2 Common wall, strict selector exchange, carry, and visibility

The two competitive first-phase differences both equal
\((m-1)(u_1-2u_2)\), giving the common excluded wall \(r=2\) and the exact
matrices

\[
A_- = \begin{pmatrix}0&2m\\1&2m-1\end{pmatrix},\quad
A_+ = \begin{pmatrix}m-1&2\\m&1\end{pmatrix},\quad
B_m=\operatorname{diag}(2m+1,m).
\]

The complete branch maps are

\[
h_m(r)=\frac{2(2m+1)}{r+2m-1},\qquad
\ell_m(r)=\frac{(2m+1)((m-1)r+2)}{m(mr+1)}.
\]

Direct subtraction reproduces all three corrected identities:

\[
h_m(r)-2=\frac{2(2-r)}{r+2m-1},
\]

\[
\ell_m(r)-1=
\frac{(m^2-m-1)r+3m+2}{m(mr+1)},\qquad
2-\ell_m(r)=\frac{(m+1)(r-2)}{m(mr+1)}.
\]

Thus the seed \((1,1)^\mathsf T\) has the unique strict itinerary
\(A_-,A_+,A_-,A_+,\ldots\), and neither branch maps an off-wall point onto
the wall.

I separately checked seed carry and all later first- and second-phase carry
inequalities in both chambers, already at \(s=1\). The selected source is
strictly unique at every phase. Its top homogeneous part is a nonzero scalar
times a product or power of earlier nonzero top parts in a polynomial domain;
nonzero coefficients and characteristic zero prevent its loss. This proves
actual degree transport without positivity assumptions.

The branch images make \(q_1\) dominate \(q_2\). In the negative chamber the
correct comparison is first the equality
\(u_{n+1,1}=smh_m(r_n)v_{n+1,2}\), then strict dominance. In the positive
chamber direct expansion makes \(u_{n+1,1}-v_{n+1,2}>0\). Together with the
first momentum comparison this makes \(q_1\) strictly visible among all four
coordinates for every positive iterate, while \(d_0=1\) remains the tied
seed.

### 5.3 Monodromy, determinant, spectrum, recurrence, and parity laws

The correct two-step product is

\[
P=(B_mA_+)(B_mA_-)=
\begin{pmatrix}
2m(2m+1)&2m(2m+1)(2m^2+m-2)\\
m^2&m^2(4m^2+4m-1)
\end{pmatrix}.
\]

I multiplied both factors and checked both right eigenpairs. They are

\[
H=m^2(2m+1)^2,\quad (2,1)^\mathsf T,
\]

and

\[
L=2m(m+1),\quad
(-(2m+1)(2m^2+m-2),m)^\mathsf T.
\]

The trace is \(H+L=4m^4+4m^3+3m^2+2m\). Expanding \(ad-bc\) for the displayed
matrix gives

\[
2m(2m+1)m^2(4m^2+4m-1)
-2m(2m+1)(2m^2+m-2)m^2
=2m^3(m+1)(2m+1)^2=HL.
\]

Hence \(C_+C_-=s^2P\), \(H>L>0\), and the visible growth gives
\(\lambda_1(F)=sm(2m+1)\).

Cayley--Hamilton yields exactly

\[
d_{n+4}=s^2(H+L)d_{n+2}-s^4HLd_n,
\]

with

\[
d_0=1,\quad d_1=2m(2m+1)s,\quad
d_2=2m(m+1)(2m-1)(2m+1)s^2,
\]

\[
d_3=8m^4(m+1)(2m+1)s^3.
\]

The full corrected third vector has second coordinate
\(2m^2(m+1)(2m-1)(2m^2+2m+1)s^3\). The left wall functional satisfies
\((1,-2)C_-=-2ms(1,-2)\) and
\((1,-2)C_+=-(m+1)s(1,-2)\), so the exact gaps are

\[
u_{2j,1}-2u_{2j,2}=-(s^2L)^j,\qquad
u_{2j+1,1}-2u_{2j+1,2}=2ms(s^2L)^j.
\]

I also checked the written full even-vector decomposition and both visible
parity closed forms against the two eigenvectors. Their apparent denominators
do not carry the integrality proof; integrality follows from the integer
matrix formulas, equivalently the integer recurrence and initials.

### 5.4 Bounded structural and conditional lemmas

Inside the stated crossed-binomial / diagonal-pure-power ansatz, both
competitive differences share the wall
\(R=(d-b)/(a-c)\). The branch

\[
g_{x,y}(r)=\frac ef\frac{(x-1)r+y}{xr+y-1}
\]

is strictly decreasing. Since both branches meet at the common wall weight
\(L_{\mathrm{wall}}\), global exchange of the two open chambers holds if and
only if

\[
\frac ef=\frac{R(L_{\mathrm{wall}}-1)}{L_{\mathrm{wall}}-R}.
\]

The explicit specialization is exactly \(R=2\),
\(L_{\mathrm{wall}}=2m+2\), and
\((e,f)=s(2m+1,m)\). This lemma proves no carry, top-form survival, actual
degree transport, or visibility by itself, and \(R=1\) places the ordinary
seed on the wall.

The conditional period-\(k\) lemma retains all six necessary hypotheses:
strict selected-face gaps, strict carry, nonzero selected top forms in a
domain, linear face maps, true-degree visibility, and Perron-class
visibility. Only then do the residue matrices, Cayley--Hamilton recurrences,
and \(\rho(M)^{1/k}\) conclusion follow. It remains technical and
nonheadline.

## 6. Public identity, article architecture, and citation lock

The exact title is *Forced Period-Two Selector Exchange in Two-Mode
Hamiltonian Product Shears*. Source, rendered, and visible author are exactly
`Anonymous`; source date is exactly `\date{}` and visible date is empty. PDF
title metadata is the full title, while PDF author, creator, and producer are
each empty. Venue and identity markers are forbidden.

The article contract is one abstract plus exactly eight numbered sections,
with all theorem-critical proofs in the numbered main body and no proof
appendix. The exact content-page arithmetic is
\(0.5+3.0+3.0+3.5+4.0+3.5+4.0+2.5+2.0=26.0\), references excluded, inside
the hard 22--30 band. Exactly three hand-typeset mathematical tables are
required: selector/branch, carry/visibility, and degree-law. A fourth table is
forbidden. Figures, images, plots, diagrams, assets, datasets, empirical
panels, code listings, and computational tables all remain zero.

The citation allowlist is exactly S01--S09 and no tenth source. I replayed the
exact repaired metadata and bounded access statements:

| ID | Exact frozen record |
|---|---|
| S01 | M. P. Bellon; C.-M. Viallet, “Algebraic Entropy,” *Communications in Mathematical Physics* 204(2), 425--437 (1999), DOI `10.1007/s002200050652`, `chao-dyn/9805006v3` |
| S02 | Boris Hasselblatt; James Propp, “Degree-growth of monomial maps,” *Ergodic Theory and Dynamical Systems* 27(5), 1375--1397 (2007), DOI `10.1017/S0143385707000168`, `math/0604521v5` |
| S03 | Allan P. Fordy; Andrew Hone, “Symplectic Maps from Cluster Algebras,” *SIGMA* 7, Paper 091, 12 pages (2011), DOI `10.3842/SIGMA.2011.091`, `1105.2985v2` |
| S04 | Allan P. Fordy; Andrew Hone, “Discrete Integrable Systems and Poisson Algebras From Cluster Maps,” *Communications in Mathematical Physics* 325(2), 527--584 (2014), DOI `10.1007/s00220-013-1867-y`, `1207.6072v2` |
| S05 | Tsukasa Ishibashi; Shunsuke Kano, “Algebraic entropy of sign-stable mutation loops,” *Geometriae Dedicata* 214(1), 79--118 (2021), DOI `10.1007/s10711-021-00606-1`, `1911.07587v5` |
| S06 | Stanisław Janeczko; Zbigniew Jelonek, “Polynomial symplectomorphisms,” *Bulletin of the London Mathematical Society* 40(1), 108--116 (2008), DOI `10.1112/blms/bdm112`; no verified arXiv record in the bounded check |
| S07 | Jérémy Blanc; Immanuel van Santen, “Dynamical degrees of affine-triangular automorphisms of affine spaces,” *Ergodic Theory and Dynamical Systems* 42(12), 3551--3592 (2022), DOI `10.1017/etds.2021.90`, `1912.01324v2` |
| S08 | Nguyen-Bac Dang; Charles Favre, “Spectral interpretations of dynamical degrees and applications,” *Annals of Mathematics* 194(1), 299--359 (2021), DOI `10.4007/annals.2021.194.1.5`, `2006.10262v2` |
| S09 | Enbo Shao; Xiaosong Sun, “Dynamical degrees of affine-triangular automorphisms in dimension four,” `arXiv:2509.14584v1`, dated 2025-09-18, arXiv DOI `10.48550/arXiv.2509.14584`; `misc`, preprint-only under the bounded 2026-08-25 status |

S01--S08 remain future `article` records and S09 remains a future `misc`
record. The S09 statement is expressly access-limited: no journal reference,
version-of-record page, or non-arXiv publisher DOI was verified as of the
cutoff; this is not an absolute nonpublication claim. No source transfers a
local proof, expands novelty, or supports firstness. A fresh final metadata
identity check is still mandatory before any later source authoring.

## 7. Firewall, anti-claims, lifecycle, and permissions

The public/private firewall is exact. Future public bytes may contain only the
anonymous theorem narrative, formulas, the three mathematical tables, and
the nine frozen bibliography entries. Real identity, venue, funding,
acknowledgment, local path, hash, byte/LF count, queue, review, lifecycle,
batch, predecessor numbering, comment, hidden BibTeX field, and PDF metadata
leaks are forbidden.

The lock preserves the complete anti-claim boundary: no theorem on the wall;
no classification outside the bounded ansatz; no maximal selector fan;
no period greater than two or arbitrary automaton; no positive-characteristic
theorem; no inverse-degree, entropy-equality, integrability, genericity,
periodic-point, arithmetic-orbit, or nonconjugacy theorem; no novelty claim
for the conditional period-\(k\) principle; no Perron/tropical/symplectic
firstness or absolute priority; no changed supports, vanishing coefficients,
or reversed phase order; and no proof by computation.

At author stop, all scientific counters are zero and theorem evidence is
noncomputational. Exactly one conditional project write was open: this review
artifact. Modification of the lock or any predecessor, source/BibTeX
authoring, figures/assets, code/data/experiments, build/PDF, release,
submission/upload/hosting/push, transport/messaging, identity disclosure,
Paper 25, and every external effect were closed. A blocker would have required
zero writes.

## 8. Sole delta and final disposition

All conjunctive checks passed. Immediately before this write, all eighteen
preexisting project files and all root/candidate records were stable, and the
future source trio was absent. This review is the sole delta. After this write
the required project universe is nineteen regular files, the same four child
directories, zero symlinks, and zero other objects.

The terminal verdict below does not directly authorize source, TeX, BibTeX,
build, PDF, release, or any external action. It only permits a separate later
root transition to consider opening one source-only author for exactly
`paper/main.tex`, `paper/math_commands.tex`, and `paper/references.bib`.

PUBLICATION_LOCK_PASS
