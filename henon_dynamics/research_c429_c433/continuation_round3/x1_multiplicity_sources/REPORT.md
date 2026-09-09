# R3 X1 — primary-source multiplicity bridge scout

2026-09-09 UTC. Bounded source lookup and proof reading; no mathematical
program, finite census, source-package edit, or external-model upload.

## Frozen target

For every odd prime $p$, every $c\in k=\overline{\mathbb F}_p$, and
$f_c(x)=x^2+c$, define
$$
M_n(c)=\max_{f_c^{\circ n}(\alpha)=\alpha}
       \operatorname{ord}_{x=\alpha}(f_c^{\circ n}(x)-x).
$$
The source target is a theorem implying
$$
\liminf_{n\to\infty}M_n(c)/2^{n/2}=0
$$
for every allowed $p,c$. A stronger uniform bound would suffice, but is not
silently assumed. One iterate of $f_c$ is the native clock; $M_n$ measures
nonreduced multiplicity, not the number of ordinary periodic points.

The imported sufficiency argument is
[R2 positive characteristic, Step 4](../../../research_c424_c428/continuation_round2/positive_characteristic/PROOF_PACKAGE.md).
It already proves that this condition implies the original ordinary-cycle
coboundary equality. Reproving that implication, the normal form, or an
author's current partial theorem is outside this scout.

Success is an applicable primary theorem with its exact domain and proof
mechanism. A negative source outcome must identify the precise absent
hypothesis or quantifier, especially when a result only treats dynamically
affine maps, a fixed return germ, or minimally ramified germs. A source not
covering this target is not a counterexample to the target.

## Multiplicity-source outcome

No applicable all-$c$ maximum-multiplicity theorem was located in this
bounded primary-source check. The two closest mechanisms have explicit
domain gaps. This is a statement about the sources checked, not a claim
that the target is false or that no such theorem exists. No source below
can presently replace the missing all-$c$ bridge in PC424-L.

### 1. Dynamically affine maps: exact group-quotient restriction

Byszewski–Cornelissen–Houben, *Dynamically affine maps in positive
characteristic*, Theorem A, §1.2, Lemma 3.1, and §3 hypotheses
([primary PDF](https://arxiv.org/pdf/1904.04942)).

Theorem A assumes a dynamically affine map on $\mathbb P^1$: a connected
commutative algebraic group $G$, an affine map $\sigma+h$ with $\sigma$ a
confined isogeny, a finite automorphism group $\Gamma$, and a compatible
dense-open identification $\Gamma\backslash G\hookrightarrow\mathbb P^1$.
It proves rationality versus non-holonomicity of the full zeta function
according to coseparability, and root-rationality of the tame zeta function.

The proof reduces ordinary fixed-point counts to a complement contribution
plus $|\Gamma|^{-1}\sum_{\gamma\in\Gamma}\#\ker(\sigma^n-\gamma)$.
Kernel sizes are degree divided by inseparable degree; hypothesis H2
encodes the latter by a valuation on an isogeny ring. Mahler-type arguments
then analyze the resulting generating functions.

**Gap:** no such group-quotient presentation is supplied for arbitrary
$x^2+c$. The introduction explicitly distinguishes $x^2+1$ in
characteristic other than $2,3$ from this class. Degree prime to $p$ is not
a replacement for dynamically affine. Tame ordinary counts also are not
an asserted bound for maximum nonreduced multiplicity.

### 2. Local parabolic germs: exact genericity and moving-cycle gaps

Lindahl–Rivera-Letelier, *Generic parabolic points are isolated in positive
characteristic*, Definitions 1.2–1.3, Theorems A and D, §3.1
([primary PDF](https://arxiv.org/pdf/1501.03965)).

For a germ $g$ whose multiplier has order $q$, write
$i_e(g^q)=\operatorname{ord}((g^{qp^e}(z)-z)/z)$.
The general inequality is a **lower** bound
$i_e(g^q)\ge q(p^{e+1}-1)/(p-1)$; equality for every $e$ defines minimal
ramification. For odd $p$, Theorem D characterizes it by
$i_0(g^q)=q$ and nonzero iterative residue. Theorem A expresses this as
nonvanishing of a polynomial in the first $2q$ coefficients.

The proof uses a formal resonant normal form (Lemma 3.3) and explicitly
computes first significant terms of iterates (Main Lemma, Corollary 3.1).
Theorems B/Corollary C give local periodic-point isolation under the stated
conditions, not an unconditional upper multiplicity estimate.

**Gap:** no cited result verifies minimal ramification for every quadratic
cycle-return germ. Moreover, estimates for one fixed germ do not control
the maximum over cycles whose periods and germs vary with $n$. A usable
bridge needs uniform control of those exceptional germs, not genericity
alone. Identifying this requirement does not assert it is true.

### 3. Earlier polynomial zeta theorem: a genuine but restricted special case

Bridy, *Transcendence of the Artin–Mazur Zeta Function for Polynomial Maps
of $\mathbb A^1(\overline{\mathbb F}_p)$*, Theorems 1–2, equation (3),
Proposition 6, and Question 2
([primary PDF](https://arxiv.org/pdf/1202.0362)).

Theorem 1 treats polynomials in $k[x^p]$ and power maps $x^m$; Theorem 2
treats $x^{p^m}+ax$, with $a\in\mathbb F_{p^m}^{\times}$ and odd $p$.
The proof explicitly factors power-map fixed-point polynomials to remove
$p$-power multiplicities, uses valuation identities, then applies
Christol–Cobham automatic-sequence results to establish transcendence.
Thus its power-map factorization directly supplies multiplicity data for
$c=0$, but not general $c$.

**Gap:** these are group-homomorphism special families. The paper ends by
asking whether the ordinary zeta function for $x^2+1$ in odd characteristic
is rational (Question 2). That historical question is not itself evidence
for or against the weaker maximum-multiplicity target; it confirms that
this paper does not provide the missing general theorem.

## Direct periodic-data source pass

The additional bounded pass found no new applicable theorem turning
ordinary periodic sums into a polynomial transfer for every $x^2+c$.
The earlier [R2 source exclusions](../../../research_c424_c428/continuation_round2/positive_characteristic/SOURCE_AUDIT.md)
and [R6 Mahler subtraction](../../../research_c424_c428/continuation_round6/positive_characteristic/SOURCE_AUDIT.md)
were checked and are not repackaged as new mathematical findings.

The nearest retrieved positive-characteristic regularity theorem remains
Julien Roques, *On the reduction modulo p of Mahler equations*, Theorem 2,
§3, printed pp. 57–60. It assumes an **already algebraic** Laurent-series
solution of a linear monomial-base Mahler equation with nonzero first and
last coefficients and $\gcd(\ell,p)=1$, and concludes rationality.
Proposition 4 classifies finite function-field extensions stable under
$z\mapsto z^\ell$; Corollary 5 and purely inseparable descent complete the
argument. This does not construct an algebraic transfer from ordinary
periodic sums or provide a native arbitrary-quadratic base theorem.
These are unchanged mathematical exclusions, not a new PC424-L proof.
The theorem and displayed proof were rechecked in the
[published PDF](https://www.jstage.jst.go.jp/article/tmj/69/1/69_1493172128/_pdf).

There is one bibliographic delta: the directly accessible
[publisher record](https://www.jstage.jst.go.jp/article/tmj/69/1/69_1493172128/_article/-char/ja)
now verifies *Tohoku Mathematical Journal* **69**(1), 55–65 (2017),
DOI `10.2748/tmj/1493172128`, published 2017-03-30. This resolves the
earlier unsuccessful publisher-access check only; it changes no theorem
scope and is not a publication-quality or novelty certificate.

## Closing boundary

Both bounded source passes are complete. The research-lit workflow kept
this report local-first and primary-source/hypothesis-led; no broad
literature review or author-mathematics rewrite was undertaken. Source
body access covered the displayed results, their stated reductions, and
the selected local/finite-extension proofs identified above, not every
technical proof in every paper. No mathematical programs, finite census,
external-model uploads, shared/source-package edits, Git operations, or
configuration changes were made. The only write was this lane report.

This source outcome does not decide any independently developing proof.
In particular, it neither establishes nor refutes an all-parameter
ordinary-cycle coboundary theorem, and it makes no inference from source
absence about the truth of the frozen multiplicity target.
