# Candidate brief: two-scale Ruelle resonances of the sine-perturbed cat map

Date: 2026-09-07. Status: `SAME_COMPLETE_FROZEN_INPUT_FOR_BLIND_CANDIDATE_REVIEWS`.
This is a selection brief, not a manuscript, a formal Paper30 project,
a page-measurement exception or a physical PDF acceptance.
Route applicability: `NOT_APPLICABLE`.

## 1. The single scientific question

What is the actual weak-coupling Ruelle spectrum of the classical
sine-perturbed cat map, beyond its known single-mode decay mechanism?
In particular, does the spectrum below the leading pair follow the
integer powers of a first-order tangent, explicitly solvable Blaschke
family, or does the pure sine perturbation produce a different scale?

The model is not new. Fix the exact area-preserving family
$$
F_\kappa=A\circ S_\kappa,\qquad
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
S_\kappa(q,p)=(q,p+\kappa\sin(2\pi q)),\qquad t=\pi\kappa.
$$
The question concerns the Ruelle–Pollicott resonances for invariant
area correlations, in the forward pullback convention. It is not an
$L^2$ eigenvalue problem, an arithmetic prime-orbit determinant, a
Riemann-zero model, a noisy finite matrix experiment or a maximum-entropy
measure spectrum.

The checked result is a complete two-scale small-parameter theorem for
this exact family: two simple leading resonances with different even/odd
quadratic corrections, eight simple resonances of order $|t|^{3/2}$,
and a uniform smaller bound on every remaining resonance.
The possible contribution is this explicit, rigorously controlled
branching structure, not the model, nuclearity or the general existence
of fractional eigenvalue perturbations.

## 2. Exact claims and nonclaims

There is $\tau_R>0$ such that for every real $0<|t|<\tau_R$,
the constant resonance $1$ is algebraically simple. After removing it,
the resonance multiset has the following structure.

**Leading pair.** There are two distinct simple branches, holomorphic
in $t$ and real for real $t$, in the even and odd sectors of frequency
inversion:
$$
\lambda_{\rm ev}(t)=-t+\frac{11}{12}t^2+O(t^3),\qquad
\lambda_{\rm od}(t)=-t+\frac5{12}t^2+O(t^3).
\tag{1}
$$

**Second cluster.** On the cover $t=s^2$ there are eight simple branches
$$
\lambda_j(s^2)=s^3\bigl(\nu_j+O(s)\bigr),\qquad j=1,\ldots,8,
\tag{2}
$$
holomorphic in $s$. Their eight different nonzero leading constants are
the two square roots of each of
$$
\frac{9+\sqrt{145}}{24},\quad \frac{9-\sqrt{145}}{24},\quad
\frac{7+i\sqrt{15}}{24},\quad \frac{7-i\sqrt{15}}{24}.
\tag{3}
$$
For positive $t$, one may take $s=\sqrt t$; for negative $t$, take
$s=i\sqrt{|t|}$. Changing the square root only relabels the cluster.
The leading constants occur in opposite pairs; the finite-parameter
eigenvalues are not claimed to occur in exact opposite pairs.

**Uniform remainder.** After deleting these ten eigenvalues with
algebraic multiplicity, the supremum of the moduli of all remaining
resonances is
$$
o(|t|^{3/2}).
\tag{4}
$$
Consequently, the entire nontrivial spectrum is $O(|t|)$, and its
spectral radius is $|t|+O(|t|^2)$. These are consequences of the same
theorem, not additional independent large theorem blocks.

The proof does not determine every smaller resonance, the optimal
remainder exponent, a largest valid parameter interval, global
finite-parameter spectra or a quantitative noise/coupling joint limit.
It does not prove analogous formulas for arbitrary analytic shears,
other cat matrices, higher dimensions or the previously open torus
cohomology problem. Complex parameters are allowed for the fixed-space
analytic matrix family, not claimed to describe this real area dynamics.

## 3. Complete common input package

Both reviewers receive this same frozen brief and all nine complete
files below. They must read the complete mathematical and prior inputs,
not just the synthesis, summaries or an author's desired conclusion.
All are under `docs/research-batch07/`; all have been fully read by root.

| Input | Lines | SHA-256 |
| --- | ---: | --- |
| [Trace-class author proof](PAPER30_TORUS_REWEIGHTED_NUCLEAR_OPERATOR_PROBE_20260906.md) | 320 | `c85dfa0ed29f1c6eb7d29d0898984bf9e2536da5ec89868c4582db9ea7381826` |
| [Two-scale matrix author proof V1](PAPER30_TORUS_TWO_SCALE_MATRIX_PROOF_V1_20260906.md) | 363 | `a5cc67aad167207330a98f88ff45c26e4977285df1e14c8aaabf727eb2483d2c` |
| [Dynamical-spectrum identification author proof](PAPER30_TORUS_WEIGHTED_TRACE_IDENTIFICATION_20260906.md) | 395 | `ccdcb4bb0cd1ebaabfd65c6069cd47b1bcab7e94c2e524aa77c22dcdea209cd6` |
| [Independent low-order algebra check](PAPER30_TORUS_SECOND_STRATUM_ALGEBRA_CHECK_20260906.md) | 430 | `88b045f78a3e3fe9f57c868a62d26ea29dc003380d35547c3825c95dc04953ec` |
| [Independent full operator check](PAPER30_TORUS_TWO_SCALE_OPERATOR_INDEPENDENT_CHECK_20260906.md) | 388 | `a47442b6721d005590bbbf368165c86da6f4360279fc34881913af03b3cd57e6` |
| [Independent dynamical identification check](PAPER30_TORUS_TRACE_IDENTIFICATION_INDEPENDENT_CHECK_20260906.md) | 401 | `519b4e997b04dac1226f5ac80bdec30f6276460f0de8fb9a971a8e12ad446762` |
| [Primary-source small-coupling screen](PAPER30_TORUS_SMALL_COUPLING_RESONANCE_PRIOR_PROBE_20260906.md) | 271 | `d80892c27c79fbbfdcabee116e6aeb17dd2832048fb2cac5dd01b9b035871694` |
| [Three late-source checks](PAPER30_TORUS_RESONANCE_LATE_PRIOR_CHECK_20260907.md) | 69 | `4e61cd20dfe19619638cef09957c26a8e45720f60c7946cb62892d4da38aabca` |
| [Proof-stage synthesis and acceptance](PAPER30_TORUS_TWO_SCALE_PROOF_ACCEPTANCE_20260907.md) | 149 | `772246b8e7caaec519b3e5e6373ab9d82e30dd19762cd46369098225490eae09` |

The three independent checks are PROVABLE AS STATED in their stated
scopes. No theorem-level correction is needed for these final inputs.
The corrected zero-order sign and the inclusion of zero coordinates
already appear in the final trace-class proof. The old three-frequency
$\sqrt{2/3}$ suggestion in the prior search is superseded by (3);
it is neither a theorem nor an additional claim in this package.
The independent checks and the synthesis are evidence records, not
extra manuscript content to be copied as repeated proofs.

## 4. Mathematical architecture, credited once

**Uniform infinite-frequency control.** For $m=(r,s)$, use states
$(a,b)=(s,r+s)$ and edge $(a,b)\to(b,c)$, with $k=a+c-3b$.
The Fourier coefficient is $[z^k]e^{tb(z-z^{-1})}$. A parameter-dependent
weight with exponent $\omega(m)=|a|-|b|$ leads to
$$
B(t)_{(b,c),(a,b)}
=t^{|a|-2|b|+|c|-1}[z^k]e^{tb(z-z^{-1})}.
\tag{5}
$$
The integer cost, factorial coefficients and geometric summation give
a whole-complex-disk bound
$$
\sum_{m,n}\sup_{|t|\le1/256}|B(t)_{n,m}|
\le23040+512/65535<23041.
\tag{6}
$$
This proves trace-norm holomorphy at zero on a fixed Hilbert space.
The radius and constant are explicit sufficient bounds, not optimizers.

**Degenerate leading operator and parity.** The complete zero- and
first-order supports have respectively 20 and 58 nonzero edges.
The exact zero-order operator is $B_0=-P+N$, where $P$ has rank two,
$N$ has rank six, $PN=NP=0$ and $N^2=0$.
Frequency inversion commutes with the full family. It gives a simple
$-1$ branch in each parity sector; the left-right derivative calculation
gives (1). The low-order proof is not independent of the operator
proof's same calculation and must not be counted twice.

**Second rescaling, including all other frequencies.** Analytic Riesz
trivialization fixes the zero spectral space and gives
$\mathcal A(t)=N+tM(t)$ with $M(0)=QB_1Q$.
On the square-root cover, scaling the six-dimensional source of $N$
gives a trace-norm holomorphic full operator $K(s)$. Its finite-rank
limit retains the infinite-complement-to-source coupling. Its nonzero
generalized spectrum nevertheless lies in the twelve-dimensional core.
The two parity effective matrices are
$$
D=\begin{pmatrix}1/12&-1/2&1\\-1/2&1&0\\1&0&0\end{pmatrix},\qquad
A_\eta=\operatorname{diag}(\eta,2/3,0),\quad\eta=\pm1.
$$
The nonzero roots of $DA_\eta$ solve
$\mu^2-(8+\eta)\mu/12-\eta/9=0$, giving (3).
Simple analytic spectral projections and a uniform resolvent argument
then prove (2) and (4) for the complete infinite operator.

**Identification with the actual dynamics.** The weighted completion
$H_t$, with orthonormal basis $t^{\omega(m)}E_m$, carries
$C_t=1\oplus tB(t)$. An invariant entire-periodic core proves equality
of every actual iterate with the matrix power. Self-adjoint heat
regularization converges in trace norm; the Poisson kernel localizes
each trace at all nondegenerate fixed points. Comparing every power
trace with Faure–Roy's resonance realization gives the entire identity
$$
\det(I-zR_t)=(1-z)\det(I-ztB(t)).
\tag{7}
$$
Thus all nonzero eigenvalues and algebraic multiplicities are identified.
No bounded similarity on ordinary $L^2$ is asserted. These trace and
spectral tools are classical; their necessary application to this
singularly weighted realization must be distinguished from novelty.

## 5. Mandatory prior deductions and remaining possible delta

- **Thiffeault–Childress (2003).** Their equation (2) is exactly this
  family with $K=2t$. Their Fourier–Bessel transfer matrix, vertical
  self-feedback mode and small-$K$ modulus $J_1(K)\sim K/2$ already
  identify the linear leading decay scale. Their cycle discussion also
  precedes the broad idea of organizing higher-order Fourier returns.
  The read section uses single-mode approximation and numerical
  agreement, not the present complete uniform two-scale theorem.
  The sign, multiplicity and remainders here are independently derived.
  [Primary text, §II and §IV](https://arxiv.org/pdf/nlin/0211036)
- **Faure–Roy (2006), Adam (2017).** Ordinary anisotropic nuclearity,
  real-dynamical resonance identification and periodic trace machinery
  are established theory. FR's exact example is linearly conjugate to
  this one. Adam's nonzero trace-derivative criterion directly proves
  nontrivial resonances for sufficiently small nonzero parameters here.
  None of these ingredients alone is a new contribution. Distinguish
  spectral-index or noise limits from the coupling limit.
  [FR §2.2](https://arxiv.org/pdf/nlin/0601010),
  [Adam Theorem 4.3](https://arxiv.org/pdf/1605.06493)
- **Slipantschuk–Bandtlow–Just (2017).** For real parameter $a$, their
  Blaschke shear is
  $$
  \psi_a(q)=\frac1\pi\arctan\frac{a\sin(2\pi q)}{1-a\cos(2\pi q)}.
  $$
  It has exact spectrum $\{1,0\}\cup\{(-a)^n:n\ge1\}$, counting
  each power twice. Setting $a=t$ makes the maps first-order tangent:
  $\psi_t=(t/\pi)\sin(2\pi q)+(t^2/(2\pi))\sin(4\pi q)+O(t^3)$.
  Thus the negative double leading scale has a very close exact
  precedent. But its spectrum below that pair has size $t^2$, whereas
  (2) has size $|t|^{3/2}$. This is a direct comparison of the two
  formulas, not a claim that merely changing the shear creates novelty.
  [Model and Theorem 1.1](https://arxiv.org/pdf/1605.02883)
- **Pollicott–Sewell (2023).** Their different orientation-reversing
  rational family already has rigorous half-integer spectral powers.
  Therefore neither fractional powers nor square-root splitting of
  Anosov resonances is new as a general phenomenon. Its base matrix,
  perturbation and location of the fractional cluster differ from this
  positive-determinant pure sine family.
  [Definition 3.1 and Lemma 3.7](https://arxiv.org/html/2204.01511v1)
- **Other analytic and numerical precedents.** Blum–Agam's variational
  four-root approximations, rational-map explicit spectra, modern
  resonance-counting and certified transfer-operator methods must not
  be ignored. The prior report distinguishes their maps and quantifiers.
  Keller uses a piecewise-linear cat perturbation, Ostruszka et al.
  coupled baker maps (including actual analytic resonances), and
  Nonnenmacher a noise/quantum-classical limit with a fixed double-
  harmonic numerical example. The late-source report gives precise
  model checks rather than dismissing those papers as purely numerical.
- **General operator theory.** Riesz projections, analytic simple
  eigenvalues, Fredholm determinants, nilpotent square-root splitting,
  elementary parity and finite-dimensional characteristic polynomials
  are standard. Re-presenting these tools is not independent novelty.

The main source report covers 2024–2026 and the then-current six-month
window, including actual June 2026 updates; the late report adds only
three model checks. Neither is an exhaustive proof of world priority.
Reviewers must decide whether the exact two-scale result and its
uniform infinite-dimensional realization constitute a substantial
scientific increment after all these deductions, or a correct but
insufficiently substantial specialized calculation.

## 6. Local noncollision and exclusions

The current README and the retained Papers1–29 portfolio baseline have
been checked. Papers8–11 concern deterministic finite-torsion orbit,
centralizer and clock constructions; their manuscript scope explicitly
does not enter Ruelle/transfer/Fredholm spectral claims. Papers14–19
concern algebraic multiplicative tori, not the present real hyperbolic
torus spectrum. Papers20–28 concern Hamiltonian degree-growth, Newton
and selector structures. Paper29 concerns polynomial cohomology,
periodic-scheme detection and fixed fields. No accepted theorem in that
portfolio supplies (1)–(7).

This is local noncollision, not external novelty. The earlier stopped
formal conjugacy, action reconstruction, quantum trace, finite-field
tuple mixing and open torus cohomology packages are all excluded.
They may not be merged into this candidate as extra body capacity.
No experiment, frozen numerical output or source-code appendix is part
of the scientific evidence; all results here are proof-derived.

## 7. Unchanged contract for two fresh mutually blind reviews

Each reviewer independently decides all four gates for this exact
whole package:

1. Novelty at least 7.5/10 after the mandatory prior deductions.
2. Stand-alone scientific value at least 7.5/10.
3. Complete-proof confidence at least 9/10 for the stated exact scope.
4. Credible natural capacity of 22–30 substantive English body pages.

Capacity geometry is anonymous English single-column `article`, 11pt,
letter paper, one-inch margins and standard spacing. References start
separately and do not count. No enlarged fonts, display inflation,
artificial breaks, blank pages, logs or source listings can count as
substantive body. No author page allocation or target is supplied.

Each reviewer supplies a justified low/central/high natural-body table
by necessary mathematical block, credits every argument once, and
deducts duplicate proof/audit records. A full textbook exposition of
FR, general spectral perturbation, the many unrelated prior models,
or open later resonance layers cannot fill a deficit. The leading
spectral-radius corollary and the tangent-Blaschke comparison are short
consequences, not extra large chapters. If the result naturally belongs
in a shorter article, fail this locked capacity gate while accurately
preserving its mathematical and scientific merits.

The selection decision is the conjunction of all four gates in both
complete reports. Scores are not averaged; best components are not
combined across constructions or reviewers. The two reviewers have
no authorship or prior mathematical-audit role in this package. They
must not read, discuss or infer the other review; each owns one
disjoint output file. They must not import scores from earlier
candidates. A failed gate stops selection of this unchanged package.
No inherited Paper29 natural-draft exception or automatic post-count
expansion is authorized.

The configured GPT-5.4 MCP reviewer interface is unavailable. The
actual independent secondary execution must be identified honestly;
do not claim that model, a human review or a cross-model test that did
not occur. A complete candidate PASS would only open the ordinary
local manuscript workflow; it would not itself count as a completed
paper, a PDF acceptance or permission for any external action.
