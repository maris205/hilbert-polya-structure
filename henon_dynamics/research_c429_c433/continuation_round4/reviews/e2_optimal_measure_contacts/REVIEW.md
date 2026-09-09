# R4 E2 independent review: optimal-cycle contacts and measures

2026-09-09 UTC. Final nonauthor actual-file review.

## Verdict and exact scope

**PASS: PROVABLE AS STATED. Zero open mathematical or
source-applicability must-fixes.**

The reviewed proof establishes convergence for every odd prime \(p\),
every complete algebraically closed ultrametric field \(K\) of
characteristic \(p\), and every \(\lambda\in K\) with
\(0<|\lambda-1|<1\). For \(P(z)=\lambda z+z^2\), let \(\Pi_e\) be the
source-supplied unique small cycle of ordinary least period \(p^e\).
Then the real probability measures
\[
\mu_e=p^{-e}\sum_{\alpha\in\Pi_e}\delta_\alpha
\]
converge weakly on \(\mathbb P^{1,\mathrm{an}}_K\). Indeed, their supports
lie in a single compact metric subset of the classical field \(K\).

The exact all-anchor contact formula and its divergent lower bound
are proved, rather than inferred from top-\(p\) matching. The author
also supplies a complete compactness and measure argument, so this
verdict does not depend on D1's separate abstract criterion.

This is a mathematical/source-applicability verdict for the stated
theorem. It does not certify publication priority, worldwide current
open status, a new paper count, an odometer identification, or any
global Galois claim. The independent X1 priority audit is separate.

## Frozen files and review method

Both author files were read completely:

- [PROOF_PACKAGE.md](../../a1_optimal_cycle_measures/PROOF_PACKAGE.md),
  470 lines, SHA-256
  038cdb412d1b83b94c1ebcfb742090e3937251225077a0f6842d7933c458174e.
- [REPORT.md](../../a1_optimal_cycle_measures/REPORT.md), SHA-256
  dda8616930868403898a1b6f3ba1c09a3800488175494a095723b3229cfaa80d.

The contact and specialization steps were independently derived while
the author proof was still being completed, and then checked against
the frozen complete text. The earlier B4 displacement proof and its
nonauthor review were read as dependency checks; the present proof
re-establishes the needed bound over arbitrary \(K\).

The proof-writing and research-review checklists were used to separate
imported dynamical facts, new derivations, general-field hypotheses,
and the final measure-theoretic interface. No mathematical program was
executed, no author file was edited, and no external model, child agent,
Git operation, manuscript build, or shared-file write was used.

## 1. Primary-source scope and imported geometry

The primary statement of Lindahl–Rivera-Letelier's Problem 1.3 has the
same odd-prime, complete algebraically closed ultrametric-field and
multiplier quantifiers. Its measures are the uniform real measures on
the selected cycles, not crucial measures or averages over all
periodic points. The \(q=1\) case of Theorem C supplies the cycles and
their common radius; minimal ramification of \(z+z^2\) supplies the
reduction order used below. These are credited inputs, not new
conclusions. [LRL, Problem 1.3 and Theorem C](https://arxiv.org/html/1311.4478v3)

Write
\[
s=\lambda-1,\qquad v(s)=1,\qquad r=(p-1)/p.
\]
Every point of every \(\Pi_e\) has valuation \(r>0\). The proof uses
ordinary native least periods. In particular, two levels have disjoint
point sets. The source's \(p^e\) points are already distinct; no
separability or irreducibility claim is being silently assumed.

## 2. Arbitrary-\(K\) specialization is justified

The author does not simply transport a result proved only over
\(\overline{\mathbb F}_p((s))\).

Let \(k_0\subset K\) be the elements algebraic over \(\mathbb F_p\).
Algebraic closedness of \(K\) makes \(k_0\) an algebraic closure of its
prime field. Its nonzero elements have norm one, since each is in a
finite field. Evaluation
\[
\sum_{n\ge n_0}a_nt^n\longmapsto\sum_{n\ge n_0}a_ns^n
\]
converges in \(K\). A nonzero leading term strictly dominates the
remaining tail, so its norm is exactly
\(|s|^{\operatorname{ord}_t a}\). Continuity applied to finite Laurent
polynomials proves preservation of sums and products; the leading-term
calculation proves injectivity. Thus this is an isometric field
embedding of \(k_0((t))\), with no residue-field restriction on \(K\).

Set \(F_e=P^{\circ p^e}-z\) and \(Q_e=F_e/F_{e-1}\). Divisibility is a
polynomial identity over the coefficient ring. The reduction order
\[
\operatorname{ord}_z(g^{\circ p^e}-z)
=1+\frac{p^{e+1}-1}{p-1},\qquad g=z+z^2,
\]
has successive difference \(p^e\). Coprime Hensel factorization over
\(k_0[[t]]\) therefore yields \(Q_{e,t}=M_{e,t}V_{e,t}\), with
\(\deg M_{e,t}=p^e\), reduction \(z^{p^e}\), and
\(\overline V_{e,t}(0)\ne0\). All factors are monic.

After evaluation in \(K\), coefficients remain integral and the
constant term of \(V_e\) remains a unit. Every other term has positive
valuation at a positive-valuation input, hence
\[
v(V_e(x))=0\quad\text{for }v(x)>0.
\]
If \(\alpha\in\Pi_e\), least period gives \(F_{e-1}(\alpha)\ne0\);
therefore \(F_e=F_{e-1}M_eV_e\) forces \(M_e(\alpha)=0\). Its degree
and the \(p^e\) distinct source-supplied roots give exactly
\[
M_e(z)=\prod_{\alpha\in\Pi_e}(z-\alpha).
\]
This proves the required root identification and simplicity for every
allowed multiplier, without a generic-discriminant specialization
argument, full local inertia, or nested root fields.

## 3. Index-dependent contacts and exponential displacement

On \(D=\{x:v(x)\ge r\}\), the identity
\[
P(x)-P(y)=(x-y)(1+s+x+y)
\]
shows both invariance of \(D\) and isometry. For distinct \(x,y\in D\),
every iterated difference quotient has the form \(1+u\), \(v(u)\ge r\).
This stronger residue-one statement, not isometry alone, is what
justifies the contact classification.

Fix \(\beta\in\Pi_d\) and put
\(\delta_j=v(P^{\circ p^j}(\beta)-\beta)\), \(0\le j<d\). These are
finite. If \(a=kp^j\), \(p\nmid k\), a telescoping sum with
\(G=P^{\circ p^j}\), divided by \(G(\beta)-\beta\), has \(k\) summands
of residue one. Its residue is \(k\ne0\), so
\[
v(P^{\circ a}(\beta)-\beta)=\delta_{v_p(a)}
\quad(1\le a<p^d).
\]
There are \((p-1)p^{d-j-1}\) indices with \(v_p(a)=j\). No assertion
that distinct index classes have distinct contact values is needed.

For the exponential bound, define the weighted Gauss valuation
\(w_r(\sum h_i z^i)=\min_i(v(h_i)+ir)\). The \(K\)-linear substitution
operator \(U(H)=H\circ P\) satisfies
\[
(U-I)z^i=z^i((1+s+z)^i-1),\qquad
w_r((U-I)H)\ge w_r(H)+r.
\]
The bracket's constant term has valuation at least one and every
positive-degree term has weight at least \(r\). Constants map to
zero. Characteristic \(p\) gives
\((U-I)^{p^j}=U^{p^j}-I\). Evaluation at \(\beta\) now gives
\[
\boxed{\delta_j\ge(p^j+1)r}.
\]
This argument is valid for a real-valued nondiscrete valuation. The
weaker linear-in-\(j\) estimate is not being substituted for it.

## 4. All-anchor multiplier identity and denominator audit

Let \(m_d=(P^{\circ p^d})'(\beta)\). Differentiating
\(F_d=F_{d-1}M_dV_d\) at \(\beta\) gives
\[
m_d-1=F_{d-1}(\beta)M_d'(\beta)V_d(\beta).
\]
All three factors are nonzero: least period, the simple-root product,
and the unit calculation respectively. Thus \(m_d\ne1\) is proved
before any derivative quotient is divided. In particular
\[
\begin{aligned}
A_d:=v(m_d-1)
&=\delta_{d-1}
 +\sum_{j=0}^{d-1}(p-1)p^{d-j-1}\delta_j.
\end{aligned}
\]
The multiplier is a product of \(P'\) over the entire cycle, so it,
and hence \(A_d\), is independent of the chosen anchor.

For every \(e>d\), differentiating \(F_e=F_{e-1}Q_e\) at this same
anchor yields
\[
F_e'(\beta)=F_{e-1}'(\beta)Q_e(\beta),\qquad
F_{e-1}'(\beta)=(m_d-1)^{p^{e-d-1}}\ne0.
\]
The exponent is one at \(e=d+1\); the endpoint is not exceptional.
Consequently
\[
Q_e(\beta)=(m_d-1)^{(p-1)p^{e-d-1}}.
\]
Using the unit factor and the actual root product then gives
\[
\frac1{p^e}\sum_{\alpha\in\Pi_e}v(\beta-\alpha)
=c_d:=\frac{p-1}{p^{d+1}}A_d.
\]
The division here is of real valuation sums by the real number \(p^e\),
not division by zero inside \(K\). Distinct least periods make every
individual contact finite.

The lower bound can be checked without an asymptotic approximation:
\[
\begin{aligned}
A_d
&\ge r\left[p^{d-1}+1+
 \sum_{j=0}^{d-1}(p-1)p^{d-j-1}(p^j+1)\right]\\
&=r\,p^{d-1}\bigl(1+p+d(p-1)\bigr).
\end{aligned}
\]
It follows exactly that
\[
\boxed{c_d\ge b_d:=d r^3+r^2(1+1/p)\longrightarrow+\infty}.
\]
All quantifiers are uniform over \(e>d\). No exact higher displacement
pattern, discriminant bound, or higher-layer ramification formula is
used to obtain this divergence.

## 5. One close pair gives a coupling of the actual cycles

For any fixed anchor \(\beta\in\Pi_d\), the maximum of the finite
contact list is at least its average \(c_d\). Choose the corresponding
\(\alpha\in\Pi_e\). Native isometry gives
\[
|P^{\circ i}(\alpha)-P^{\circ i}(\beta)|
\le |s|^{c_d}\le\varepsilon_d:=|s|^{b_d}
\quad(i\ge0).
\]
The explicitly defined real probability measure
\[
\pi_{e,d}=p^{-e}\sum_{i=0}^{p^e-1}
\delta_{(P^{\circ i}(\alpha),P^{\circ i}(\beta))}
\]
has first marginal \(\mu_e\). Every point of \(\Pi_d\) occurs precisely
\(p^{e-d}\) times, so the second marginal is exactly \(\mu_d\). Thus
every support pair has distance at most \(\varepsilon_d\to0\).

This is a coupling of the original native-period measures, not merely
a correspondence between quotient clusters. No simultaneous global
choice of phases across all levels is required.

## 6. Compactness and weak convergence, including topology

Let \(S=\bigcup_e\Pi_e\). Given \(\eta>0\), choose \(d\) with
\(\varepsilon_d<\eta\). Every later cycle lies within
\(\varepsilon_d\) of the finite set \(\Pi_d\); there are only finitely
many earlier points. Hence \(S\) is totally bounded. Completeness of
\(K\) makes \(C=\overline S\) compact metric. Its points stay on the
same norm sphere. No ball of \(K\) is presumed compact.

For each continuous real \(\varphi\) on \(C\), uniform continuity and
the coupling give
\[
|\mu_e(\varphi)-\mu_d(\varphi)|
\le\omega_\varphi(\varepsilon_d)\quad(e>d).
\]
The integrals are Cauchy. Their limits define a positive bounded linear
functional with value one on the constant function one. Riesz
representation gives a unique probability measure \(\nu_C\), and
therefore weak convergence on \(C\).

This application needs only a compact metric space: it is in
particular second countable and locally compact Hausdorff. Thus the
positive-functional representation theorem in Baggett's Theorem 1.3
applies directly; finite Borel measures on a compact metric space are
regular. [Baggett, Chapter I, Theorem 1.3](https://spot.colorado.edu/~baggett/funcchap1.pdf)

Evaluation embeds \(K\) continuously into the Berkovich affine line,
because each polynomial seminorm \(a\mapsto|H(a)|\) is continuous.
The projective line is Hausdorff, so the compact image of \(C\) is
closed and homeomorphic to \(C\). These statements hold over arbitrary
complete non-Archimedean fields; no residue-countability or global
metrizability assumption is required. The general-field setup,
evaluation points, topology, and Hausdorff projective line were checked
in Poineau–Turchetti, Example I.1.2, §I.3 and Proposition II.1.6.
[Primary exposition](https://arxiv.org/pdf/2010.09043)

Pushing \(\nu_C\) forward gives \(\nu\) on
\(\mathbb P^{1,\mathrm{an}}_K\). Every continuous real function there
restricts continuously to \(C\), so the same inequality proves the
claimed weak convergence. Since \(P(C)\subset C\) and every \(\mu_e\)
is invariant, applying convergence to \(\varphi\circ P\) proves
invariance of the limit. This completes the measure claim without
using D1's pending work.

## Final disposition

The frozen proof is complete for the original convergence question's
mathematical quantifiers. No repair or additional hypothesis is
requested. The new uniform contact average is the essential arithmetic
interface; the source-supplied cycle geometry and the classical
functional-analysis/topology inputs remain explicitly subtracted.

The separate source-priority/admission decision remains with the
coordinator. This review neither upgrades a bounded search to a
worldwide novelty claim nor converts the result into a global
irreducibility, Witt-tower, or Hilbert–Pólya assertion.

**Final status: PASS; zero open mathematical must-fixes; zero open
source-applicability must-fixes; zero mathematical executions.**
