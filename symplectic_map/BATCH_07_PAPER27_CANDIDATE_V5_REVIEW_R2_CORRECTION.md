# Paper 27 candidate v5 — fresh blind R2 correction review

**Disposition:** PASS (fresh R2; all finding classes zero)

**Reviewer role:** independent Batch 07 Paper 27 v5 proof/adversarial reviewer

**Review point:** current \`BATCH_07_STATUS.md\` physical EOF through E0051

**Candidate:** \`positive_newton_translation_reciprocity_v5\`

## Restricted reading and action boundary

This review was restarted from the current EOF after E0051. I read only:

1. \`BATCH_07_STATUS.md\`, including its governing charter sections and the
   authoritative v5 packet through E0051;
2. \`BATCH_07_CHARTER_REVIEW.md\`;
3. \`papers/12-henon-period3-residue/notes/RESEARCH_QUESTION.md\`;
4. \`papers/12-henon-period3-residue/notes/CLAIMS_EVIDENCE_MATRIX.md\`;
5. \`papers/12-henon-period3-residue/notes/PROOF_PACKAGE.md\`;
6. \`papers/26-hamiltonian-newton-envelope-contraction/notes/RESEARCH_QUESTION.md\`;
7. \`papers/26-hamiltonian-newton-envelope-contraction/notes/CLAIMS_EVIDENCE_MATRIX.md\`;
8. \`papers/26-hamiltonian-newton-envelope-contraction/notes/PROOF_PACKAGE.md\`.

I did not read, probe, or wait on any earlier candidate-review file (including
any earlier v5 review), Paper 27 project or source tree, PDF, idea report,
temporary/closed/future root, or any other project file. I performed no build,
compile, network lookup, numerical/CAS/scientific run, cache-producing
operation, copy, cleanup, or external action. Before the single authorized
write below, no file was modified.

The live status file is a regular mode-0644, link-one, strict-UTF-8, LF-only
file of 195,902 bytes and 4,154 LF (terminal LF present; no CR, NUL, or BOM).
Its E0051 parent prefix was independently checked:

| logical event | physical prefix bytes | independently recomputed SHA-256 |
|---|---:|---|
| E0046 predecessor | 185,006 | \`0ba32a7350a34cc5e81fca4699f40c0b9b18434aaf716957fc56cc99f4c2de08\` |
| E0048 physical block | 187,122 | \`7ac9477bface4790fa83aea224686021adb42f99bd20cd5baa8e0a459d43093a\` |
| E0049 physical block | 188,940 | \`a476b46996a635b73a4a6e81b73a5ed62b1bcf79af2e51bd405508d624d6dac4\` |
| E0050 physical block | 190,831 | \`0f5a00ed54bbd3e0fff0306350df201ae782cdf81c183d31c3053ca217e8a19\` |
| E0051 parent prefix | 193,300 | \`95bb3c5276c7690476f6d710331cf54ac73d8e6a29f7a4fc4a1da8e81168e55b\` |

These values agree with the machine fields. E0048 is explicitly disposed as
the premature physical \`seq:48\`; E0049 is the authoritative logical \`seq:47\`
correction, E0050 is logical \`seq:48\`, and E0051 is logical \`seq:49\`. Thus the
authoritative chain is 46 -> 47 -> 48 -> 49 even though the immutable invalid
E0048 bytes remain in the physical ledger. E0051 has unchanged pre/post
manifest \`845a62b44598b8b24378ed8ec0e8aca4345cb8fc206e9ab3cf4590a6f2fb2ad2\`,
\`created_paths: []\`, \`paper_number_consumed: false\`, and the required v5 dual
review gate. No sequence, parent-hash, manifest, or append finding remains.

## Controlling scope and governance

The charter's broad discovery label is subordinate to the active
\`BATCH07_PAPER27_CANDIDATE_V5_DUAL_REVIEW_REQUIRED\` subgate. The candidate is
not a project, does not consume Paper 27, and has no external effect. Its
family is explicitly nonempty finite collected supports

\[
 E_V,E_W\subset\mathbb Z_{\ge 2}^{\,r},\qquad r\ge3,
\]

over a characteristic-zero coefficient field, with ordered real degree space
separate from that field. A weighted polynomial seed uses positive integer
degree vectors and algebraically independent leading tuples (fresh variable
blocks realize every declared pair). A strict branch requires a unique
exposed maximizer at each visited half-step and strict fresh-gradient carries;
ties, failed carries, and uncertified walls are terminal boundaries. The
positive-support face-Hessian lemma is an auxiliary wall certificate and does
not silently turn a wall into a strict selector.

E0033/E0039 are controlling for selector scope: “canonical automaton” means a
seed-indexed finite selector-word certificate unless a separate closure and
target-inclusion certificate is printed. The support set alone is not claimed
to supply a universal automaton. E0051 further controls the lower-ideal claim:
it is one declared strict pair core and one step only. The prior
multi-edge/all-iterate wording is explicitly conditional and outside the v5
headline; no C1-to-C2-to-C2 perturbation stability or F-CORE-1 obligation is
being smuggled back in.

## Independent proof and adversarial checks

### 1. Leading transport and noncancellation

For an exposed support exponent \(\alpha\), the gradient degree map is

\[
A_\alpha u=(\alpha\!\cdot u)\mathbf1-u,
\qquad
B_\beta v=(\beta\!\cdot v)\mathbf1-v.
\]

For a face \(F\), the Hessian coefficient matrix of one monomial is
\(\alpha\alpha^{\mathsf T}-\operatorname{diag}(\alpha)\), and hence

\[
\det(\alpha\alpha^{\mathsf T}-\operatorname{diag}\alpha)
 =(-1)^r(1-|\alpha|)\prod_i\alpha_i\ne0.
\]

Choosing a generic secondary weight with a unique minimizing
\(\alpha_0\in F\) makes the all-\(\alpha_0\) tuple the unique lowest group in
the grouped determinant expansion. Its coefficient is
\(c_{\alpha_0}^{\,r}(-1)^r(1-|\alpha_0|)\prod_i\alpha_{0i}\), nonzero for the
declared nonzero coefficients and characteristic zero. The Jacobian
criterion therefore gives algebraic independence of the full face-gradient
tuple; injective substitution into the independent leading tuple, component
pure powers, nonzero scalars, and inverse signs preserve that independence.
Thus the face result is coefficient-uniform and applies to every exposed face,
while strict carries keep old blocks from cancelling fresh blocks.

The map convention is checked as

\[
H(q,p)=V(q)+W(p),\quad S_V(q,p)=(q,p+\nabla V(q)),\quad
T_W(q,p)=(q+\nabla W(p),p),\quad F=T_W\circ S_V,
\]

with \(F^{-1}=S_V^{-1}\circ T_W^{-1}\) and subtraction in both inverse
phases. The forward order is \(A_\alpha\) then \(B_\beta\), and the inverse
reflected order is W then V. Since every support coordinate is at least two,
the displayed fresh vectors dominate the old coordinate blocks whenever the
declared pair carries are strict.

### 2. Translation, recurrence, and finite selector changes

Writing \(h_V(u)=\max_{\alpha\in E_V}\alpha\cdot u\), one step has

\[
v=h_V(u)\mathbf1-u,
\qquad
u'=h_W(v)\mathbf1-v=u+\delta\mathbf1,
\qquad
\delta=h_W(v)-h_V(u).
\]

Thus \(u_n=u_0+t_n\mathbf1\), \(t_0=0\), and strict carry is exactly
\(\delta_n>0\). On a stationary pair \((\alpha,\beta)\),

\[
t_{n+1}=\lambda t_n+\mu,
\quad
\lambda=(|\alpha|-1)(|\beta|-1)>1,
\quad
\mu=((|\beta|-1)\alpha-\beta)\cdot u_0.
\]

The global wall argument is sound. Put
\(g(t)=h_V(u_0+t\mathbf1)-t\). Every support total \(|\alpha|-1\) is
positive, so \(g\) is strictly increasing. For W exponents \(\beta,\eta\),

\[
(\beta-\eta)\cdot v(t)
=(|\beta|-|\eta|)g(t)-(\beta-\eta)\cdot u_0.
\]

Unequal-total W walls therefore cross at most once globally; equal-total
differences are invariant. V total-degree classes similarly form an upper
envelope in \(t\). If \(d_V,d_W\) are the numbers of distinct total degrees,
the controlling E0050 bound is

\[
\#\{\text{selector changes}\}\le d_V+d_W-2.
\]

The older \(d_Vd_W-1\) and pair-count bounds are valid conservative historical
estimates, not competing headline claims. An orbit that reaches a tie or
failed carry stops; an infinite strict continuation has a stationary pair and
the displayed affine tail. Consequently there is no hidden infinite or
nontrivial periodic strict selector word.

### 3. Reflected phase identities and the converse

With coordinate reversal \(R\) and phase-state swap
\(R_{\rm state}(u,w)=(Rw,Ru)\), the literal reflected identities are

\[
B_{R\alpha}R=RA_\alpha,
\qquad
A_{R\beta}R=RB_\beta.
\]

They give the reflected W-then-V inverse state transition. For an edge \(e\),
the integer seed spans

\[
U_e=\operatorname{span}_{\mathbb R}\{u:(u,w)\in C_e^\mathbb Z\},
\qquad
V_e=\operatorname{span}_{\mathbb R}\{A_\alpha u:(u,w)\in C_e^\mathbb Z\}.
\]

Equality of both phase-resolved degree vectors for all integer seeds forces the
two linear restrictions at \(n=1\) on \(U_e\) and \(V_e\). Full matrix
identities are asserted only when the corresponding spans are all of
\(\mathbb R^r\); on proper spans a different face label inducing the same
action is expressly allowed. Conversely, the restrictions on every edge of
the seed-indexed word, with reflected score/carry checks, induct by phase
state. Scalar total-degree equality alone is not used and cannot identify the
selector matrices.

### 4. E0051 lower-ideal lemma

For one strict pair core, the four score projections are the V-plus input,
W-plus fresh output, reflected W-minus input, and reflected V-minus fresh
output:

\[
\pi_u(C_e^+),\quad \{A_\alpha u\},\quad \{Ru\},\quad
\{RA_\alpha u\}.
\]

On each normalized compact strict core, every retained/selected row \(\ell\)
and lower/new row \(\rho\) satisfies the sign-correct margin

\[
\min_x(\ell-\rho)\cdot x\ge\Delta>0.
\]

The typed pair core separately carries the source \((u,w)\), all carry and
target gaps, and its reflected swap. These conditions preserve the selected
leading forms for exactly one forward step and one reflected inverse step.
No image-to-next-core or all-iterate inference is made, so E0051 removes the
former unsupported stability obligation.

## Exact fixture audit

The canonical positive r=3 supports are

\[
E_V=\{(8,2,2),(2,5,6),(2,8,2)\},\qquad
E_W=\{(2,2,8),(6,5,2)\}.
\]

With \(R(1,2,3)=(3,2,1)\), the displayed matrices are

\[
A_1=\begin{pmatrix}7&2&2\\8&1&2\\8&2&1\end{pmatrix},\quad
A_2=\begin{pmatrix}1&5&6\\2&4&6\\2&5&5\end{pmatrix},
\]
\[
B_1=\begin{pmatrix}1&2&8\\2&1&8\\2&2&7\end{pmatrix},\quad
B_2=\begin{pmatrix}5&5&2\\6&4&2\\6&5&1\end{pmatrix}.
\]

Direct multiplication gives

\[
C_{21}=B_2A_1=I+\mathbf1(90,19,22),\qquad
C_{22}=B_2A_2=I+\mathbf1(18,55,70).
\]

The C1-to-C2 target gaps are
\((84,22,26)\cdot u\), \((90,16,26)\cdot u\), and
\((1074,231,268)\cdot u\) (the last as an all-rows carry vector), with
reflected gamma form \((4,5,2)\cdot u\). The C2 self-loop gaps are
\((12,58,74)\cdot u\), \((18,52,74)\cdot u\),
\((214,662,852)\cdot u\), and \((214,668,846)\cdot u\); its target
carry increment is the all-rows vector \(\mathbf1(216,660,840)\cdot u\).
All are positive on the declared K1/K2 cones. The pair cells are the open
sets \(w>0\), \(A_i u-w>0\), and are full-dimensional.

The integer pair \(((2,1,1),(1,1,1))\) lies in C1 and maps to the C2 cell;
\(((1,1,1),(1,1,1))\) lies in C2. The listed C1 seeds
\((2,1,1),(2,1,2),(3,1,1)\) and C2 seeds
\((1,1,1),(1,1,2),(1,2,2)\) have nonzero determinants, so the required
observable spans are genuinely full in the fixture. The reflected products
satisfy

\[
B_1Ru=RA_1u,\quad A_2B_1Ru=RC_{21}u,\qquad
B_2Ru=RA_2u,\quad A_2B_2Ru=RC_{22}u.
\]

The exponent \(\gamma=(2,8,2)\) is active on an off-component open cone but is
absent from the W support after reflection, proving local rather than global
map-level symmetry. The ordinary equal seed has unique exposed \(a_2,b_2\)
selectors (inactive submaximal ties do not count); it is a stationary baseline,
not a claimed transient strict-cell witness. No perturbation-preserved
C1-to-C2-to-C2 claim is made after E0051.

## Collision, source, portfolio, and anti-claim audit

The status ledger contains a complete P12--P26 matrix and a v5-specific
augmentation. The allowed P12 notes identify a period-three Hénon trace/residue
and quartic-fiber observable, not a support-derived Hamiltonian degree theorem.
The allowed P26 notes identify a planar (r=2), pure-power-momentum
Newton-envelope contraction, separate forward/inverse recurrences, and a
rate bridge. V5 is r>=3 with arbitrary finite positive supports in both
potentials, derives the diagonal translation and global finite wall bound, and
adds reflected phase-state observable-span reciprocity; it neither claims
P26's planar theorem as new nor borrows its scalar bridge as a recurrence proof.
The status matrix separately charges P20--P25 and records their distinct
stationary, endpoint, wall-monodromy, support-rank, and spectral ownership.

The bounded source screen gives query families, named primary sources, date,
limitations, and explicitly avoids a priority claim. The provisional novelty
screen is not treated as proof; after charging P12--P26, my independent scores
are recorded below. E0043's provisional P28--P31 axes are disjoint: length-
at-least-three primitive cycles, toric cohomological spectra, signed transfer
reciprocity, and zero-coordinate cancellation respectively. None is a
relabelled v5 appendix.

Permanent anti-claims are present and respected: no arbitrary or
zero-coordinate support extension; no positive-characteristic, empty-support,
zero-coefficient, or uncollected-support extension; no unconditional field
algorithm; no map-level reversor/global classification; no entropy, higher
dynamical degree, or minimal-recurrence claim; no same-seed assertion for a
non-\`Rstate\`-fixed pair; no scalar-only converse; no claim beyond listed strict
walls/carries; no global priority; and no external effect. The Hessian
cancellation fixture is explicitly a boundary counterexample, not evidence for
the headline.

## Numerical gate assessment

| Gate | Independent assessment | Result |
|---|---:|---|
| novelty | 8.0 / 10 | PASS (>=7.5) |
| standalone value after predecessor absorption | 7.8 / 10 | PASS (>=7.5) |
| proof readiness | 9.2 / 10 | PASS (>=9.0) |
| anonymous proof-only content | 24--28 pages | PASS (credible 22--30) |
| P12--P26 absorption and source/collision lock | complete, bounded, non-priority | PASS |
| exact noncollision with P28--P31 | all four reserved axes disjoint | PASS |

The page estimate counts substantive setup/seed semantics, the all-face
Hessian and induction proof, translation and global wall lemma, reflected
observable-span converse, the local one-edge margin lemma, the exact fixture,
boundaries, and collision analysis. Governance prose, paths, hashes, and
discovery history are excluded. Removing the former multi-edge obligation
does not make the article a short corollary: the four remaining proof objects
still support the stated range.

## Finding census

Every category was checked against the authoritative E0030--E0051 chain and
the restricted notes above. No issue is being deferred to a later project
stage.

| Finding category | Count |
|---|---:|
| authorization and Papers 27--31 scope | 0 |
| controlling subgate and serial authority | 0 |
| E0048/E0049 sequence correction and E0051 parent/EOF append | 0 |
| current status identity, UTF-8/LF, manifest, and no created paths | 0 |
| nonempty positive-support/collected coefficient assumptions | 0 |
| weighted integer-seed and ordered degree-space semantics | 0 |
| phase order, carries, leading-form survival, and inverse signs | 0 |
| translation law, lambda/mu recurrence, and finite-change bound | 0 |
| strict unique-selector scope and no universal automaton overclaim | 0 |
| reflected phase identities, pair-state swap, and span converse | 0 |
| four-section lower-ideal quantifiers and E0051 one-edge limitation | 0 |
| exact C1/C2 fixture arithmetic, spans, and asymmetry | 0 |
| P12/P26 absorption and P12--P26 collision matrix | 0 |
| P28--P31 portfolio noncollision lock | 0 |
| anti-claims, boundaries, and no external effect | 0 |
| novelty, standalone, proof-readiness, and page thresholds | 0 |
| forbidden reads, mutation, cache/build/network action | 0 |

Severity census: **Blocker 0; Major 0; Minor 0; Ambiguity 0.** The terminal
marker for this review is counted only as the final complete line of this
artifact; no event-field value is counted as an additional exact-line marker.

## Conclusion

The E0051 packet is a coherent, nonempty, positive-support v5 theorem with a
valid coefficient-uniform face certificate, exact all-ones translation, global
finite wall bound, correctly typed reflected phase-state converse, and a
properly narrowed one-edge lower-ideal lemma. The canonical r=3 fixture and
all displayed carries/reflected gaps check exactly. Earlier invalid physical
ledger bytes have an explicit authoritative-chain disposition, and the
candidate remains unconsumed with no project or downstream effect. All finding
classes are zero and every numerical gate passes.

BATCH07_PAPER27_CANDIDATE_V5_REVIEW_R2_CORRECTION_PASS
