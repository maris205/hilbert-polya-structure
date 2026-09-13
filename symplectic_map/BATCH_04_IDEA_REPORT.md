# Batch 04 Idea Discovery Report

## Decision

- Decision date: 2026-08-16 UTC
- Gate verdict: BATCH04_PAPER12_CANDIDATE_GATE_PASS
- Selected project: papers/12-henon-period3-residue
- Safe title: **A Uniform Period-Three Residue Law on Exceptional Henon Families**
- Final post-proof novelty estimate: 6.2/10
- Final post-proof standalone-size estimate: 5.8/10
- Earlier candidate-stage estimates: novelty 6.1/10 and 6.5/10;
  standalone size 5.7/10 and 5.5/10
- Terminal state: `COMPLETE_LOCAL_FINAL_REVIEW_PASS`

## Terminal Addendum

The source lock
`2fa930f697f6040cb16916d2b4dba7ec591a712882c108848e9eecf53608e1c2`
received `SOURCE_LOCK_PASS` at
`5e66edcd7f33769f748c8b6bd6582aa7e05b3325329839c46bf3627945803d11`.
After the sole registered R100 transaction closed with no rerun, raw result,
or result pass, Paper 12 moved to the proof-only lifecycle
`henon_period3_residue_proof_note_v1`: lock
`2c7f056b7f9566f754a06c30417105c0b1cefb2d0081f4bca8bb3a00adbf8eeb`,
independent handoff
`407cec5bf295c29330c24ae461dca86ad1bf54d77f44d477d83a821bf7e41711`,
and asset R2 `ASSET_PASS`
`7b633dd001f1ae086863826612a15d74325406f1eaf2b95fc49e49eddd7ae404`.

The failed predecessor is bound only as non-scientific provenance by durable
claim
`3b7075f7d5b1b3199c213ae34327f2c80c9f03396b5a792c086416ce99d581c0`
and terminal
`1e0896af17907e41f7028a71c056e02d5f8fb4ddf63d3d033063979e0b1d802d`.
Its deterministic Track-Q endpoint diagnosis is a forensic inference, not a
recorded traceback or theorem input. Manuscript Round 1 had one Minor
typesetting repair; Round 2 returned `PASS / MAY_FINALIZE` at
`f56ff399b120e5fb9729e51b4d52dcde64df954fb064f32319998d678c3c0577`.
The byte-identical final PDF is
`9541a3ad0ffae34cc5c7a17cfd524de73a6685d1a3f7ba2b472061186b721375`;
terminal integrity is
`7dc99f6024d7ab6f53949290ebbd4b57dec8c9d255dc8c94ab86abf7b72856be`,
and independent terminal review is
`adb2012367a71662d0054424cfed999988b480b919977f0595a6768c526d5aff`
with `FINAL_INTEGRITY_PASS / RELEASE_CONFIRMED`. At the time of this Paper-12
terminal addendum, Paper 13 remained at pre-gate active discovery and no
Paper-13 project directory existed. That dated state is historical and is
superseded by the Paper-13 terminal addendum below.

The candidate clears the Batch-04 threshold only in an asymmetric form. The
quartic theorem is the sharp headline result. The all-degree theorem supplies a
uniform residue law and an explicit coefficient certificate. Universal
nonvanishing of that coefficient remains an open problem.

## Paper-13 Terminal Addendum

Paper 13 opened as `papers/13-henon-primitive-cycle-cover` after its own
independent candidate gate. Its proof-first package treats the normalized
primitive exact-period cover for
\(H_{a,c}(x,y)=(a y+x^d+c,x)\), the cyclic orbit quotient, and the orbit-sum
and derivative-trace coordinates. The final source assessment deliberately
retained the direct Morton and Cantat--Dujardin proximity: independent novelty
and standalone-size scores were `5.2/10` and `5.1/10`, rather than the earlier
optimistic candidate-stage estimates.

Source-lock v2
`11d51aae93f4230a06046de7c3c8331a7e00169b69295d335435f470f9ff9469`
received `SOURCE_LOCK_PASS` at
`83b380d5fa1d5e2161281052ea69b447f6c26831f0cf0d818eced8affecd6c8e`.
The sole registered R100 transaction closed sealed at count one. Its accepted
effect is only `BOUNDED_IMPLEMENTATION_CONSISTENCY_ONLY`; it is not proof,
theorem validation, or novelty evidence and may not be rerun. Independent
result review is
`a5d1d3df1ed5e6e34d16aa50b86f5028c4ea86a655492794f0c58d8febcae23a`.

After one bounded manuscript revision, fresh R2 returned
`MANUSCRIPT_REVIEW_PASS` at
`10e7e5ef1ca92a348c70495bb9c631e02af055c27c017d219e46736d35a028fd`.
The byte-identical deterministic-build PDF is
`4f69c395ffc06c3d3282c09127a520385ff741428cea7083cb1a7618e347df09`.
The canonical final-release manifest is
`9db30f7bb715fa0d8faf06636d01580960304a571f02c5576735989c57526082`,
and the fresh terminal reviewer returned
`FINAL_INTEGRITY_PASS / RELEASE_CONFIRMED` at
`5896285e99d7ac551c44f8e0215e1202193535a70603a87b531180a97a138748`.
The terminal effect is strictly `LOCAL_ANONYMOUS_RELEASE_ONLY`; no submission,
upload, external distribution, or identity release is authorized. Paper 13 is
therefore `COMPLETE_LOCAL_FINAL_REVIEW_PASS`. Paper 14 is now limited to a new
pre-project candidate-discovery gate; no Paper-14 candidate or directory is
yet authorized.

## Paper-14 Candidate Gate Addendum

Paper 14 passed its candidate gate with the proof-first project
`papers/14-henon-four-step-torus-escape` and the safe title **Four-Step Escape
from Finite-Rank Tori for Monomial Henon Maps**. For a characteristic-zero
field, \(d\ge2\), nonzero \(a,b,c\), and a rank-\(r\) subgroup
\(\Gamma\le K^\ast\), set

\[
H_{a,b,c}(x,y)=(b x^d+a y+c,x),
\qquad
T_m=\{P\in\Gamma^2:H^j(P)\in\Gamma^2\ (0\le j\le m)\}.
\]

The selected headline is the explicit uniform bound

\[
\#T_4\le 4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2,
\]

together with the sharp statement that, for every \(d\ge2\), a rank-one
example can have infinite \(T_3\). The proof uses the
Evertse--Schlickewei--Schmidt three-term unit-equation bound for the
nondegenerate local recurrences and a complete three-state degeneracy
transition analysis for the remaining four-letter words. The coefficients are
fixed coefficients in the unit equation and need not belong to \(\Gamma\); the
rank remains \(3r\). A periodic-point corollary applies only to cycles whose
entire orbit lies in \(\Gamma^2\), not merely to a periodic point with one
representative in \(\Gamma^2\).

Two independent final audits returned GO. Both scored result novelty
`7.0/10`; standalone size was `6.0--6.3/10` and `6--6.5/10`; proof confidence
was `9.7/10` and `9.5/10`. Targeted primary-source checks through 2026-08-16
found no direct four-step finite-rank H\'enon collision. The classical unit
equation theorem remains the main imported arithmetic input, so method novelty
is deliberately scored lower than theorem novelty.

The rejected multiperiod-monodromy route is true at field level but reduces to
Paper 13 plus Morton/Fakhruddin and Bridy--Garton; its integral refinement is at
most a short addendum. The competing quartic sharp trace cutoff
\(P_{\mathcal H^1}(4)=3\) also passed its proof audit, but depends directly on
Paper 12, Cantat--Dujardin, and Sugiyama and has the narrower standalone-size
estimate `5.7/10`; it is preserved as the leading Paper-15 reserve rather than
mixed into Paper 14.

Paper 14 is authorized only for source design. No code, experiment, result,
figure, or manuscript may be created before a fresh independent source-lock
review returns PASS.

The source-design package subsequently passed a citation-precision repair
cycle without changing its theorem or proof. The controlling citation audit
is `7e625c593267545088320459b65e990fdea5e347ed779416a6ce334d5a131f17`,
and the repaired 13-file package received independent `SOURCE_DESIGN_PASS` at
`8bde838d4bd18426f291eb793f5c822fbd6d70d604fc7097c5761c02bb309ef0`.
The project is now at source-lock authoring only; code, experiments, results,
figures, and manuscript drafting remain closed pending a fresh
`SOURCE_LOCK_PASS`.

The canonical source lock subsequently froze at
`f2077d20262f6a068da58a2227c405573dd34fa8b844461b3d057da94e9eaa0c`,
and a fresh reviewer with no authorship overlap returned `SOURCE_LOCK_PASS` at
`ea6d13c1ec74bbad0ac8c6cd850d0f0b8c33992d05b5e428308eef3347a18308`.
This authorizes a proof-only paper plan and its independent review, not code,
experiments, results, figures, manuscript drafting, compilation, or release.

## Paper-14 Terminal Addendum

Paper 14 subsequently completed the reviewed proof-first publication
lifecycle without code, scientific experiments, or result claims. The final
source remained the characteristic-zero finite-rank theorem stated above.
Independent manuscript R2 returned `MANUSCRIPT_R2_PASS` at
`03499cc92c6a5a6b7010f75ba5fd879082dcd4abb61709722fab081bc709fe1b`.
The deterministic R0 and R1 builds and a fresh terminal double build all
produced the same 17-page anonymous PDF,
`4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414`.
The canonical final-release manifest is
`e832be91a990d1d1caf7e2b4aba40fa8d9a1196524c815e03b30309df6226e68`,
and the independent terminal reviewer returned
`FINAL_INTEGRITY_PASS / RELEASE_CONFIRMED` at
`9cfb8b2cb492dc6bea84231a81c8f7b7c698eea5299a357d066339180b14260d`.
The effect is only `LOCAL_ANONYMOUS_RELEASE_ONLY`; no submission, upload,
external distribution, or identity disclosure is authorized. Paper 14 is
therefore `COMPLETE_LOCAL_FINAL_REVIEW_PASS`. Batch 04 has completed three of
five papers, and Paper 15 may now enter only a fresh pre-project candidate
gate. The quartic sharp trace cutoff remains a reserve, not a preselected
Paper-15 theorem.

## Paper-15 Candidate and Source-Design Gate Addendum

The fresh Paper-15 gate rejected a standalone claim that the quartic formal
trace cutoff is merely \(3\): that conclusion alone is too close to the known
Cantat--Dujardin exceptional family and the local Paper-12 calculation to
support another paper. The project opened only after the contribution was
strengthened into one dependent three-part theorem on the single-factor
monic-centered generalized Henon space:

1. for every degree \(d\ge2\), the formal fixed-trace characteristic
   polynomial \(C_f\) satisfies \(C_f'(1-a)=0\), so pure fixed traces leave at
   most \(d-1\) Jacobian candidates;
2. in degree four over \(\mathbb C\), the exact non-quasi-finite locus of the
   period-one/two trace morphism is
   \(E=\{a=1,\ p=(x^2-L)^2\}\), with quotient coordinate \(L^3\);
3. adding formal period three makes the global quartic trace morphism
   quasi-finite, while period two remains insufficient.

The proof package uses Cantat--Dujardin only after the pure-trace Jacobian
enumeration and only at fixed \(a\ne1\). Sugiyama is confined to the simple
fixed-point stratum; the four singular root partitions are handled directly.
The nonreduced period-three subtraction, coefficient ledger, local branch
lengths, pointwise/cyclewise normalization, and residual \(\mu_3\) quotient are
fully absorbed from the frozen Paper-12 proof rather than cited as an opaque
internal result. Consequently Paper 15 is a unified strengthening of Paper 12
for any external publication, not a parallel overlapping sequel.

The bounded candidate audits gave the strengthened package novelty
`6.6--6.9/10`, standalone size `6.0--7.4/10`, and no known mathematical
counterexample. The author-side transcription score initially remained
`8.7/10`, so the project was opened only for source design. A fresh reviewer
then replayed the complete P1--P17 proof and primary-source scopes, assigning
novelty `6.8/10`, standalone size `6.4/10`, and proof confidence `9.3/10`, and
wrote `SOURCE_DESIGN_PASS` at
`55789c4a7c62e4577b655399e7fe8247fe641381e50876d6ebad9bce1f0e8b6e`.
This authorizes only source-lock authoring and a fresh source-lock review. No
code, scientific experiment, result, paper plan, manuscript, figure, build, or
release is authorized.

The canonical source lock subsequently froze at
`802fc883cde85cd6312e8a31e0728dc01b493c640c8918d9eacc497f44cac7be`.
It binds all 11 local source-design records together with eight upstream
governance and absorbed-proof provenance records. A fresh reviewer with no
authorship overlap returned `SOURCE_LOCK_PASS` at
`39ef31d1dac337fe9856fd9d8f40f756b30730a683db43c1d9b7e183236c6f63`.
The exact effect is eligibility only for a proof-only paper plan and its
independent review; every manuscript, computation, build, and release stage
remains closed.

The proof-only paper plan then froze at
`1b70ec0c37d9d587aa56b97b175c6da2f44e114d9414bf31c9f70534dd209e08`
with a 25-page, eight-section main-text budget and five proof appendices. It
keeps the fixed-algebra lemma, Jacobian-first use of Cantat--Dujardin, all five
quartic strata, formal period-two and period-three scheme bridges, and global
quasi-finiteness in the main narrative; only the long exact coefficient and
local-length ledgers move to appendices. A fresh reviewer returned
`PAPER_PLAN_PASS` at
`ce2f6ba64b971d26b2ed472d2417c018461632cb1d54d6db53004f25b2d435ac`.
The next permissible action is publication-stage governance authoring and
review, not manuscript writing.

Publication governance then froze at scope
`23ec6c825aaccd157b20b018e7e77c014ce8f94a841996850b22f586d685ea31`
and canonical lock
`3de5a4c14af5846bcb05998303f8928c9f0500b28c720a961dd7a70b8088d063`.
A fresh review returned `PUBLICATION_STAGE_PASS` at
`21aaf6cac736851a2ace894cc617e4d6b1367e292e4fe8eb8084c17685422abc`.
That gate activates only anonymous two-file source drafting. Every build,
review, revision, finalization, release, and external action remains
temporally gated or closed.

## Paper-15 Terminal Addendum

Paper 15 subsequently completed the reviewed proof-first publication
lifecycle without code, scientific experiments, or empirical evidence. The
final article keeps the dependent three-part theorem intact: pure fixed traces
first restrict the Jacobian, the quartic period-one/two non-quasi-finite locus
is exactly (E), and formal period three gives the sharp global quasi-finite
cutoff. The overlapping exceptional-fiber theorem and its nonreduced
period-three ledger are fully absorbed from Paper 12; the two manuscripts are
not parallel external submissions.

Independent R1 returned `MANUSCRIPT_R1_PASS` with no required repair, so the
single revision window was consumed by a canonical no-op receipt. The
byte-identical R1 rebuild then led to `MANUSCRIPT_R2_PASS` at
`82c2c6151b627f738f126fa80c5825e924db7841f2da83a5ad017876814842b4`.
The anonymous PDF has 24 main-content pages and 35 total pages; R0, R1, and
both terminal rebuilds have the same SHA-256
`278263a4b10e617ab18fddfb2457cccc5477e89e135341a958f379dad8f081ca`.
The canonical release manifest is
`9d7033a6912a31bfc65a5637d070654e0b3f75b303371629ac585678bba97d47`,
and the independent terminal review returned
`FINAL_INTEGRITY_PASS / RELEASE_CONFIRMED` at
`c3f333debdff6e2d3271a8857e2b93a9264ea9f50a86e813941c2572dec3079b`.

The terminal effect is only `LOCAL_ANONYMOUS_RELEASE_ONLY`; no submission,
upload, public hosting, repository push, external distribution, or identity
disclosure is authorized. Paper 15 is therefore
`COMPLETE_LOCAL_FINAL_REVIEW_PASS`. Batch 04 has completed four of five papers,
and Paper 16 may now enter only a fresh pre-project candidate-discovery gate;
no Paper-16 project or theorem is preselected.

## Paper-16 Terminal Addendum

Paper 16 opened as `papers/16-henon-support-size-torus-escape` with candidate
`henon_support_size_torus_escape_v1` and the anonymous title **Support Size and
Finite-Rank Torus Escape for Generalized Hénon Maps**. It completed the
reviewed proof-first lifecycle without code, scientific experiments, data,
results, figures, or empirical theorem evidence. The source-design gate
assigned conservative scores 7.8/10 for novelty, 8.0/10 for standalone size,
and 9.3/10 for proof confidence.

For actual collected nonconstant support \(s\ge2\), the dominant theorem gives
the coefficient-uniform bound
\[
\#T_2\le dA(s+2,3r)+M(e)S^\ast,
\]
and every prescribed such support admits a rational rank-one example with
infinite \(T_1\). The article also reproduces and fully absorbs Paper 14's
support-one theorem and proof: \(T_4\) is uniformly finite with bound
\(4dA(3,3r)+81d^2\), while \(T_3\) can be infinite in rank one. Paper 14 and
Paper 16 are not parallel external submissions.

Independent R2 returned `MANUSCRIPT_R2_PASS` at
`f2ede84a5b19ad275b8b396f4f355c86c6b93a69e515ec29691eb29ac0e0172c`.
R0, R1, both terminal rebuilds, and the final 27-page anonymous PDF are
byte-identical at
`b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f`.
The canonical release manifest is
`4bea0b67fff9c547ddc7f19f9147d8e743deac8a5cbe7a6fdc68c33c370b397b`,
and the independent terminal review returned
`FINAL_INTEGRITY_PASS / RELEASE_CONFIRMED` at
`e355172b4533011d549453d02ee9939fb2dabc16fef035206ad4911fdf18eb76`.

The effect is strictly `LOCAL_ANONYMOUS_RELEASE_ONLY`; no submission, upload,
public hosting, repository push, external messaging, or identity disclosure
occurred or is authorized. Paper 16 is
`COMPLETE_LOCAL_FINAL_REVIEW_PASS`, and Batch 04 is locally complete at
5 / 5. No Paper 17 or next batch is opened; any next transition requires fresh
explicit user authority. This Paper-16 addendum is the current batch dashboard
authority; all earlier dated stage statements and numbered addenda remain
historical provenance.

## Problem Anchor

Cantat--Dujardin prove that finitely many multiplier traces determine a complex
Henon map up to finitely many choices in fixed degree, but their Noetherian
argument does not compute an effective period cutoff. Their quartic
Jacobian-minus-one example also shows that periods one and two may be completely
blind along a positive-dimensional normalized family.

The anchored question is:

> On the complete normalized quartic fiber whose formal fixed-point trace
> multiset is \(0^4\), what is the first
> formal period whose trace data recover the conjugacy coordinate, and is there
> a degree-uniform algebraic mechanism explaining that recovery?

This question is narrower than a global theorem for all quartic Henon maps and
narrower than a formula for the unknown cutoff in every degree.

## Selected Family

For every integer \(m\ge2\), set

\[
f_{m,a}(x,y)=\bigl(y+(x^m-a)^2,x\bigr).
\]

The formal-period-three calculation uses cyclic coordinates and an auxiliary
coupling parameter:

\[
F_i=(x_i^m-a)^2+\varepsilon(x_{i-1}-x_{i+1}),
\qquad
q_i=2m x_i^{m-1}(x_i^m-a),
\]

\[
t_\varepsilon
=\det\left(\frac{\partial F_i}{\partial x_j}\right)
=q_0q_1q_2+\varepsilon^2(q_0+q_1+q_2).
\]

At \(\varepsilon=1\), this is the trace of \(Df_{m,a}^3\) on the cyclic
complete intersection.

## Frozen Safe Theorem Package

### T1. Low-period blindness

With scheme multiplicity,

\[
\operatorname{Trace}_1(f_{m,a})=0^{\times 2m},
\qquad
\operatorname{Trace}_2(f_{m,a})
=2^{\times((2m)^2-2m)}.
\]

Both are independent of \(a\).

### T2. Normalized conjugacy coordinate

Within the normalized monic-centered Henon moduli problem,

\[
f_{m,a}\sim f_{m,b}
\quad\Longleftrightarrow\quad
a^{2m-1}=b^{2m-1}.
\]

The source lock must state this category explicitly and may not silently
enlarge the result to arbitrary plane polynomial automorphisms.

### T3. Uniform period-three residue law

The cyclic quotient is monic free of rank \((2m)^3\), and the
complete-intersection trace-residue identity gives

\[
S_m(a,\varepsilon)
:=\operatorname{Tr}(t_\varepsilon^m)
=\operatorname{Res}(t_\varepsilon^{m+1}).
\]

Weighted homogeneity with

\[
\mathrm{wt}(x_i)=1,\quad
\mathrm{wt}(a)=m,\quad
\mathrm{wt}(\varepsilon)=2m-1
\]

first permits four monomials. The separated double-root algebra at
\(\varepsilon=0\), together with a local Puiseux trace analysis at the
non-diagonal degeneration, eliminates the two higher invariant powers. Hence

\[
S_m(a,\varepsilon)
=C_m\varepsilon^{3m}
 +D_m a^{2m-1}\varepsilon^{2m},
\qquad
S_m(a)=C_m+D_m a^{2m-1}.
\]

Reversing cyclic coordinates gives \(C_m=0\) for odd \(m\).

### T4. Exact finite certificate

Define

\[
H(r,k)=
\sum_{\substack{u+v=k\\2u\le r,\;2v\le r}}
\binom{k}{u}\binom{r}{2u}\binom{r}{2v},
\]

\[
A_{m,r}=
\sum_{k=\lceil m/2\rceil}^{\min(m-1,r)}
(-1)^{r+k}\binom{m-1}{2(m-k)-1}H(r,k).
\]

Then

\[
D_m=3\sum_{j=0}^{\lfloor m/2\rfloor}
\binom{m+1}{j}(2m)^{3m+3-2j}A_{m,m-j}.
\]

Equivalently, with \(q=\lfloor m/2\rfloor\),

\[
E_m=\sum_{j=0}^{q}\binom{m+1}{j}
(2m)^{2(q-j)}A_{m,m-j},
\qquad
D_m=3(2m)^{3m+3-2q}E_m.
\]

This coefficient formula is proved in the bound `PROOF_PACKAGE.md`, Step 9.
The derivation uses the terminating recurrence, the order-independent
Laurent/admissible-tuple sum, the local binomial identity (9.14), and the
distinguished-coordinate/transfer-flow classification including its \(j=0\)
case. The assertion \(D_m\ne0\) for all \(m\) is not proved and remains an
explicit nonclaim.

### T5. Sharp quartic theorem

Let \(f_p(x,y)=(y+p(x),x)\), with \(p\) monic and centered of degree four.
If its formal fixed-point trace multiset is \(0^4\), then

\[
p(x)=(x^2-L)^2.
\]

Thus the selected \(m=2\) family is the entire normalized quartic fiber whose
formal fixed-point trace multiset is \(0^4\). On it,

\[
S_2^{(3)}(L)
=-1296000-1572864L^3
=-384(3375+4096L^3).
\]

Step 12 independently derives the quartic slope without using the collapsed
all-\(m\) formula. Step 10 proves that the fixed-point contribution to this
second trace moment is zero, while Step 13 separately proves that fixed
support enters \(\operatorname{Fix}(f^3)\) with exactly its fixed-scheme
multiplicity. The exact-period-three pointwise formal length is therefore 60,
and the cyclewise sum is

\[
-432000-524288L^3.
\]

Periods one and two are constant, whereas normalized conjugacy is classified by
\(L^3\). Therefore period three is the minimal separating period on this
complete fiber.

## Bounded Development Evidence

Before opening Paper 12, exact symbolic checks established only the following
development facts:

- for \(m=2\), the cyclic ideal has leading monomials
  \(x_0^4,x_1^4,x_2^4\);
- the normal form of \(t^3\) has 44 terms and the exact socle coefficient above;
- the fixed-component remainder of \((q^3+3q)^2\) modulo
  \((x^2-L)^2\) is zero;
- a separate exact check reproduced the \(m=4\) coefficient.

These are not registered results. Any checks at \(m=2,\ldots,7\) cannot prove
universal nonvanishing.

During source-proof repair, a proof subagent incidentally rechecked the
already-designated local recurrence at \(m=2,\ldots,7\). This was an
unregistered, non-evidentiary source-stage diagnostic. It is not a tracker
run, is not an input or witness for the coefficient theorem or universal
nonvanishing, does not alter the sole possible future tuple
\(T_{\mathrm{reg}}=(8,9)\), and may not be loaded by either future engine. No
table of \(D_3,\ldots,D_9\) is stored in the source package.

## Candidate Ranking

| Rank | Candidate | Novelty | Proof confidence | Decision |
|---:|---|---:|---:|---|
| 1 | Exceptional Henon period-three law and quartic cutoff | 6.1--6.5 | high in safe scope | GO |
| 2 | Determinant-specific finite-rank noisy recovery | 5--6 | medium | backup; Prony risk |
| 3 | General effective exceptional-fiber cutoff | 5.5--6.5 | about 40% | stop until proof closes |
| 4 | Trace-class Fredholm stability/minimax | about 6 | about 40% | stop until stability theorem |
| 5 | Subexponential Henon return-gcd height | about 8 | 15--20% | stop; no global estimate |
| 6 | Period-uniform multiplier S-unit finiteness | 6.5--7 | about 20% | stop; incomplete |
| 7 | Fixed-map rational unstable multiplier rigidity | 7--8 | about 10% | stop; conjectural |
| 8 | Henon return ideals and local lifting | 3.5 | high | stop; general etale result |
| 9 | Generic multiplier rigidity | below gate | direct collision | stop |
| 10 | Symplectic/zeta repackaging | below gate | formal | stop; exhausted |
| 11 | Fredholm tail moment rigidity | 2--4 | high | stop as flagship |

The selected candidate is the only one with a complete safe theorem package,
an intrinsic moduli coordinate, bounded exact development checks and a frozen
audit plan, independent above-threshold novelty assessments, and standalone
mathematical mass.

## Primary-Source Collision Map

1. Cantat--Dujardin (2026) is the direct collision. It already contains the
   quartic obstruction family and period-one/two blindness and proves existence
   of some finite cutoff. It does not give the period-three calculation,
   effective separator, uniform law, or coefficient certificate.
2. Cattani--Dickenstein--Sturmfels supplies mature multidimensional residue
   machinery. Weighted global residues are not a novelty claim.
3. Cvitanovic--Hansen--Rolf--Vattay derive exact periodic-orbit contour sum
   rules, including Henon-type settings. Their transfer/Fredholm weights differ
   from the raw formal-period-three moment here.
4. Dullin--Meiss gives explicit low-period calculations for cubic generalized
   Henon maps, not this even-degree family.
5. Friedland--Milnor, Huguin, Hutz, Guillot--Ramirez, and Ueda supply
   normal-form, small-cycle, dynatomic, invariant, and fixed-point background.

The search was bounded. No-hit evidence is not a priority or universal-absence
proof.

## Independent Gate Record

| Audit | Novelty | Standalone size | Verdict | Qualification |
|---|---:|---:|---|---|
| Final theorem/novelty audit | 6.5/10 | 5.5/10 | GO | lead with quartic theorem |
| Updated primary-source landscape | 6.1/10 | 5.7/10 | GO | method itself is mature |
| Final post-proof audit | 6.2/10 | 5.8/10 | GO, borderline | transparent Step-9 certificate is essential; opaque appendix would fall below gate |

Their agreement closes only the candidate gate. A fresh reviewer must still
bind the complete source package and return SOURCE_LOCK_PASS.

## Mandatory Nonclaims

Paper 12 must not claim:

1. \(D_m\ne0\) for every \(m\ge2\);
2. period three recovers conjugacy for every even-degree family;
3. the quartic family or its period-one/two blindness is new;
4. a theorem about all quartic Henon maps;
5. a global equality \(P(4)=3\) outside this normalized fiber;
6. classification of all positive-dimensional low-period fibers;
7. invention of global-residue or dynatomic machinery;
8. unstable-spectrum, height, arithmetic-finiteness, prime-zero, or global
   multiplier-rigidity conclusions;
9. a universal theorem inferred from finitely many exact \(m\)-checks.

## Validation Boundary

Any later registered audit must be closed-world and exact:

- no GPU, stochastic seed, external dataset, or human evaluation;
- no new prime, Riemann-zero, modulus, or exploratory parameter scan;
- two independent exact engines for the quartic identity and finite
  certificate cases;
- proof-contract checks for the general theorem;
- negative controls for fixed-point subtraction, conjugacy exponent, cyclic
  signs, formal-period counts, and false universal promotion;
- a one-shot lifecycle only after independent deployment review.

## Source-Lock Transition

The design-only package consists of the following scientific and protocol
sources. `source_lock.json` binds them but does not hash itself; its SHA is
bound by the subsequent independent review.

1. notes/RESEARCH_QUESTION.md;
2. notes/NOVELTY_ASSESSMENT.md;
3. notes/PROOF_PACKAGE.md;
4. notes/CLAIMS_EVIDENCE_MATRIX.md;
5. notes/CITATION_VERIFICATION.md;
6. experiments/EXPERIMENT_PLAN.md;
7. experiments/EXPERIMENT_TRACKER.md;
8. refine-logs/FINAL_PROPOSAL.md;
9. refine-logs/REFINEMENT_REPORT.md;
10. refine-logs/REVIEW_SUMMARY.md;
11. refine-logs/INITIAL_PROPOSAL.md (historical, non-normative);
12. refine-logs/round-1-review.md (historical, non-normative);
13. refine-logs/round-2-review.md (historical, non-normative);
14. refine-logs/score-history.md (historical, non-normative);
15. experiments/source_lock.json (self-excluded from its own hash table).

No author may sign the independent source review. No code or result directory
may be created before the full frozen hash set receives SOURCE_LOCK_PASS.

The frozen v2 source lock is
`2fa930f697f6040cb16916d2b4dba7ec591a712882c108848e9eecf53608e1c2`.
It binds 14 design sources plus the immutable R1 review, preserves the v1 lock
hash, and explicitly excludes the mutable batch dashboards from its immutable
scientific hash table.

Fresh independent Round 2 returned `SOURCE_LOCK_PASS` at review SHA-256
`5e66edcd7f33769f748c8b6bd6582aa7e05b3325329839c46bf3627945803d11`.
At that source-stage transition this authorized implementation only; the
subsequent deployment, consumed registered failure, proof-only redisposition,
manuscript reviews, and terminal release are recorded in the Paper-12 Terminal
Addendum above. That Paper-12-local statement is historical and is superseded
for current batch status by the Paper-16 Terminal Addendum.
