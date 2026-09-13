# Independent Paper 27 source-design review (R2)

## Authorization and scope

This is the fresh independent review authorized by B07-E0062.  I inspected
only the ten frozen source-design files in this project and the physical
true-EOF chain of `BATCH_07_STATUS.md` through E0062, including the E0060
reconciliation and E0061 canonical adoption.  Earlier candidate
reviews, the failed source-design review, predecessor project files,
temporary/closed/future roots, PDFs, and builds were not used.  No network
query, code, CAS, numerical run, build, or external effect was used.
The status true-EOF bytes checked here are 229111 with SHA-256
`68a427d342d7c56341ce5755cc6a7f1ba33b43caf8ff7b4c42e32981ebc8bffa`.

The target inventory is exactly the ten files listed below; the review file
itself is the sole newly authorized path and is excluded from the frozen
22-row aggregate manifest.

## Exact file and manifest census

The ten files are regular, non-symlink, mode 0644, link-one, UTF-8/LF-only
files with no BOM, CR, NUL, hidden or backup file.  There is no `paper`
directory, manuscript, bibliography, code, data, figure, build, cache, PDF,
or standalone `PAPER_PLAN.md`.  The ten source rows and their frozen hashes
are:

| Path | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `papers/27-positive-newton-translation-reciprocity/experiments/EXPERIMENT_PLAN.md` | 4928 | 108 | `1b9628e18703fd2332c90799c71abaaa42467b7080cb35a59ab3617b1c4c9a9d` |
| `papers/27-positive-newton-translation-reciprocity/experiments/EXPERIMENT_TRACKER.md` | 3116 | 52 | `bbd8ec0ebdd866fb09174b65dd87075623fae78eba48e96aaccc4625deb45e8e` |
| `papers/27-positive-newton-translation-reciprocity/notes/CITATION_VERIFICATION.md` | 9366 | 61 | `1a54b62d83cd6861679f851ec509854d6ed83eb046d5b6db7343b6e96aa9c26b` |
| `papers/27-positive-newton-translation-reciprocity/notes/CLAIMS_EVIDENCE_MATRIX.md` | 6022 | 43 | `b0415cf8118b6e33352d513e170f5c2ad854e54a3ba854d683faca3eb6425b14` |
| `papers/27-positive-newton-translation-reciprocity/notes/NOVELTY_ASSESSMENT.md` | 6040 | 81 | `16b97ac1e7df048e1eb2d05f69980064f8201cf56a878bbd496831d20eec647c` |
| `papers/27-positive-newton-translation-reciprocity/notes/PROOF_PACKAGE.md` | 19921 | 527 | `c583d2cedcd97bef8410172bed967dfe99bcaf9caa69595c305bbf36ccd51fd1` |
| `papers/27-positive-newton-translation-reciprocity/notes/RESEARCH_QUESTION.md` | 4908 | 126 | `73b094e1905f4a5af49c82f3b3bfa7a242125e56ff724dcf00c1c8bb1a0ea4cc` |
| `papers/27-positive-newton-translation-reciprocity/refine-logs/FINAL_PROPOSAL.md` | 5446 | 131 | `d2bd1a47959907efa35364e408ede645353059a47cb3641226f5d022605a71ae` |
| `papers/27-positive-newton-translation-reciprocity/refine-logs/INITIAL_PROPOSAL.md` | 3525 | 75 | `af290d3d3587d6824cbe1c892d3b11c8551113d63c5fe03c1f641967af75e3e6` |
| `papers/27-positive-newton-translation-reciprocity/refine-logs/REVIEW_SUMMARY.md` | 4064 | 76 | `3805351516268043f6a3a91c35dc6568428849ad8fbdde33fc9872eef06e7836` |

The aggregate is the exact bytewise-path 22-row manifest (the inherited
twelve rows plus these ten rows), with framing
`path<TAB>bytes<TAB>LF<TAB>mode<TAB>nlink<TAB>sha256<LF>`, 2906 framing bytes,
22 LF, and post-aggregate SHA-256
`32d0f68dfb95ab2339607a0a3a2a91fd9e648ce1fb004294e688869801e36e2f`.
The proof-package row is the only changed row from the pre-correction
aggregate and has the hash shown above.  E0061 adopts those append-only
Section 14 bytes at true EOF and E0062 reauthorizes this review without any
source-byte change.  Thus the E0060--E0062 chain and live ten-file census
agree exactly with the current aggregate.

## Independent theorem and algebra rederivation

The declared family is over a characteristic-zero field (K), with finite
nonempty collected supports (E_V,E_W\subset\mathbb Z_{\ge2}^r), (r\ge3),
and nonzero coefficients.  Real positive degree vectors are kept separate
from coefficient-field elements.  For
\[
 S_V(q,p)=(q,p+\nabla V(q)),\qquad
 T_W(q,p)=(q+\nabla W(p),p),
\]
the composition is (F=T_W\circ S_V), while
\(F^{-1}=S_V^{-1}\circ T_W^{-1}\): inverse phase order is W first and V
second, with subtraction signs.

For a unique exposed α and β,
\[
 A_\alpha=\mathbf1\alpha^{\mathsf T}-I,
 \quad B_\beta=\mathbf1\beta^{\mathsf T}-I,
 \quad v=A_\alpha u,
 \quad u'=B_\beta v.
\]
Indeed the (i)-th gradient row has degree
\(\alpha\cdot u-u_i\), and the W half-step has degree
\(\beta\cdot v-v_i\).  The strict source and target carries separate each
fresh block from its old block, so the displayed matrix map is the actual
leading-form map on a certified edge.

For an exposed face (E_0), grouping the Hessian determinant by row-labelled
tuples gives the coefficient of the uniquely lowest secondary-weight group
\((\alpha_0,\ldots,\alpha_0)):
\[
 c_{\alpha_0}^{,r}(-1)^r(1-|\alpha_0|)\prod_i\alpha_{0i}\ne0.
\]
This follows from
\([\alpha_i(\alpha_j-\delta_{ij})]
=\operatorname{diag}(\alpha_0)(\mathbf1\alpha_0^{\mathsf T}-I)
\) and the matrix determinant lemma.  Characteristic zero, nonzero
coefficients, and coordinates at least two make the witness nonzero.  The
Jacobian criterion gives algebraic independence of face-gradient components;
injective substitution into algebraically independent incoming leading tuples
preserves visibility.  Fresh/carry separation and nonzero inverse signs then
give simultaneous forward and reflected-inverse survival.  This is a wall
certificate and does not select a tied vertex.

Let (s=h_V(u)=\alpha\cdot u).  Then
\[
 v=s\mathbf1-u,
 \qquad
 \beta\cdot v=|\beta|s-\beta\cdot u,
\]
so
\[
 u'=u+\delta(u)\mathbf1,\qquad
 \delta(u)=h_W(v)-h_V(u)
 =((|\beta|-1)\alpha-\beta)\cdot u.
\]
The second strict carry is exactly δ>0.  For an integer seed, all entries
and carries are integral, hence each strict δ is at least one and
\(u_n=u_0+t_n\mathbf1\), (t_0=0), with strictly increasing (t_n).

Put (g(t)=h_V(u_0+t\mathbf1)-t).  Since every support total exceeds one,
\(g\) is strictly increasing, and
\[
 v(t)=g(t)\mathbf1-u_0,
 \quad
 \beta\cdot v(t)-\eta\cdot v(t)
 =(|\beta|-|\eta|)g(t)- (\beta-\eta)\cdot u_0.
\]
Within each total-degree class the winner is fixed (or tied on an invariant
wall); unequal-total walls cross once because (g) is increasing.  Therefore
V and W contribute at most (d_V-1) and (d_W-1) changes respectively,
giving the claimed global (d_V+d_W-2) bound.  A strict infinite branch is
eventually stationary.  On pair ((\alpha,\beta)), with
\(c=(|\beta|-1)\alpha-\beta\),
\[
 t_{n+1}=\lambda t_n+\mu,
 \quad \lambda=1+c\cdot\mathbf1=(|\alpha|-1)(|\beta|-1)>1,
 \quad \mu=c\cdot u_0.
\]
The origin is global (t_0=0), including through selector changes.

For coordinate reversal (R), (R_{\rm state}(u,w)=(Rw,Ru)), and
\[
 B_{R\alpha}R=RA_\alpha,
 \qquad A_{R\beta}R=RB_\beta.
\]
The first identity is used by the inverse W phase and the second by its V
phase.  Equality of phase-resolved vectors on all integer seeds forces these
restrictions on (U_e) and (V_e); conversely, the restrictions plus the
reflected score, carry, and target certificates induct over the finite
seed-indexed word.  Full-matrix equality is asserted only at full spans;
scalar totals or an unfixed same numerical seed do not suffice.

The lower-ideal result is correctly quantified over one normalized compact
strict pair core, four normalized projections
\(\pi_u(C_e^+), A_\alpha u, Ru, RA_\alpha u\), typed pair margins, and
selected-minus-new row gaps bounded below by positive \(\Delta_{S,\pm}\).
Homogeneity gives positive unnormalized gaps.  The conclusion is exactly one
forward and one reflected-inverse leading step.  There is no assertion of
target-core inclusion, C1\(\to\)C2 perturbation stability, multi-edge, or
all-iterate stability.

## Exact fixture audit

The fixture supports and matrices are internally consistent:
\[
 a_1=(8,2,2),\ a_2=(2,5,6),\ \gamma=(2,8,2),\quad
 b_1=(2,2,8),\ b_2=(6,5,2).
\]
The displayed (A_i,B_i) equal \(\mathbf1\alpha^T-I\) and
\(\mathbf1\beta^T-I\), and direct outer-product
multiplication gives
\[
 B_2A_1=I+\mathbf1(90,19,22),\qquad
 B_2A_2=I+\mathbf1(18,55,70).
\]
The listed C1\(\to\)C2 selector, W-selector, reflected-selector, and carry
forms are respectively
\((84,22,26),(90,16,26),(1078,230,276),(1078,236,270)), and
\(\mathbf1(1074,231,268)\cdot u), all positive on the declared cone.
The C2 self-loop forms are
\((12,58,74),(18,52,74),(214,662,852),(214,668,846)), with carries
\(\mathbf1(216,660,840)\cdot u) and
\(\mathbf1(18,55,70)\cdot u\), again positive.  Reflected duplicates are
accounted for by the displayed permutation identities.

For the transient seed (u=(2,1,1),w=(1,1,1)), V scores are 20, 15, 14,
\(A_1u=(18,19,19)), (B_2A_1u=(223,222,222)), and the source W gap is
15.  The C2 baseline (u=w=(1,1,1)) gives (A_2u=(12,12,12)) and
\(B_2A_2u=(144,144,144)).  The three C1 seeds
\((2,1,1),(2,1,2),(3,1,1)\) and three C2 seeds
\((1,1,1),(1,1,2),(1,2,2)\) are linearly independent in their respective
sets (nonzero determinants), and (A_1,A_2) are nonsingular, so the stated
observable spans are full.  The omitted (R\gamma) and the explicit test
at (u=(1,10,1)) establish local rather than map-level reflection closure.

The cancellation fixture (V=(q_1+q_2+q_3)^3,
W=(p_1-p_2)^3) has zero/unit coordinates and cancellation of the leading
W difference at the first W half-step; it is outside the headline class.
Missing reflection certificates, ties, empty lattice cells, nonpositive
carries, positive characteristic, and proper-span complements are all stated
as failure or boundary cases.

## Collision, citation, page, and governance census

The citation ledger contains twenty first-party records with bounded query
families and source-role restrictions.  Citations are context/negative
controls only, not proof, priority, or exhaustiveness.  The predecessor
matrix charges P12--P26 collisions explicitly, and the reserved P28--P31
axes are separated by construction; no direct conjunction collision or
priority claim is made.  The safe wording remains a bounded public-index
observation through 2026-08-29 UTC.

The proof-only article allocation is 25.7 content pages in the declared
24--28 range, with theorem-critical derivations in the main text.  The
experiment plan and tracker explicitly record zero empirical/CAS/code/data
outputs and no computational dependency.  Anonymous manuscript safeguards
exclude identity, paths, hashes, event IDs, and provenance.  At this gate no
source lock, paper plan, manuscript, bibliography, build, upload, submission,
hosting, repository push, message, or identity disclosure is authorized.

## Finding census and disposition

| Finding class | Count |
|---|---:|
| Blocker | 0 |
| Major | 0 |
| Minor | 0 |
| Ambiguity | 0 |
| Threshold miss | 0 |
| Manifest/path mismatch | 0 |
| Scope or governance leak | 0 |
| Algebra, fixture, or boundary mismatch | 0 |

All theorem-critical algebra, phase order and carries, typed Section 14
definitions (\(\mathcal K_e^u\) is u-only and \(\mathcal C_e^+\) carries all pair-dependent
gaps), local lower-ideal limits, fixture arithmetic and spans, collision and
citation roles, page budget, and no-external-effect safeguards pass
independent rederivation.  The required all-zero condition is met.

BATCH07_PAPER27_SOURCE_DESIGN_PASS
