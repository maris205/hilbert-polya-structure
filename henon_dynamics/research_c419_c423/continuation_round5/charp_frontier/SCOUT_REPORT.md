# Round 5 characteristic-p frontier: no proposed new admission

2026-09-08 UTC. Three frozen mechanisms compared, two deepened, no
mathematical program executed. Author-stage recommendation: **0 new
substantial independent contracts**. The batch remains at M1, AS2 and IR1;
this lane does not modify that registry or claim a fourth/fifth slot.

| Contract | Full question | Mathematical result | Slot recommendation |
| --- | --- | --- | --- |
| CF1: Kummer-trivialized semi-linear skew | Every polynomial $a\in\mathbb F_p[x]$, every prime, every native ordinary return, and the full zeta dichotomy | Complete proof, including $a=0$, constants, $p=2$, zero fibers, disconnected covers and all characteristic-divisible times | `RETAIN_COMPLETE_RECONSTRUCTION; NO_INDEPENDENT_SLOT` |
| CF2: Laurent-series Hénon horseshoe | All square/nonsquare parameters in the entire frozen local-field horseshoe region; ordinary points of $K^2$ and all times | Direct source theorem plus the elementary fact that a periodic orbit is two-sided bounded | `REJECT_DIRECT_SOURCE_COVERAGE` |
| CF3: compact Wehler ordinary zeta | Rational/nonrational classification over the whole frozen confined finite-field class | Only an all-point nonreduced-iterate obstruction; the global multiplicity correction and zeta classification remain unproved | `HOLD_FULL_QUESTION_UNCLOSED; NO_ADMISSION` |

This is not a claim that these areas have no research value. The gate is
whether this round produced a full and substantial independent contract,
after known formulas and mechanisms are deducted.

## CF1: a complete result with a narrow increment

For $F_a(x,y)=(x^p,y^p+a(x)y)$ on all geometric affine points, let
$r=p^{v_p(n)}$ and let $R_a(n)$ count norm-one nonzero values $a(x)$ for
$x\in\mathbb F_{p^n}$. The proof establishes

$$
N_a(n)=p^{2n}-(p^n-p^{n-r})R_a(n),\qquad
(p-1)R_a(n)=\#\{t^{p-1}=a(x),\ t\ne0\}(\mathbb F_{p^n}).
$$

It also proves that $a=0$ has rational zeta $(1-p^2t)^{-1}$ and every
$a\ne0$ has a natural boundary at $|t|=p^{-2}$ even after taking any
positive integer power. Thus the classification, not merely a counting
helper, survives exactly as frozen.

The reason for the no-slot recommendation is concrete. On the Kummer
cover $y=tz$, the lifted system is
$(x,t,z)\mapsto(x^p,t^p,z^p+z)$. The only return twist is the elementary
norm of $a(x)$. Linearized root counting closes the ordinary count.
Frobenius permutes at most $p-1$ geometric components; the classical Weil
error is holomorphic beyond the dominant boundary. The remaining
characteristic-divisibility product and fractional radial orders are
the [owned C404 mechanism](../../../continuation_c404_c408_round2/henon_resonance/PROOF_PACKAGE.md).
The present component-cycle factors do not constitute a new hard
all-tower lemma. This is an increment judgment, not a claim that the
literal CF1 formula has been found verbatim in a primary publication.

Bridy's [additive-map theorem](https://arxiv.org/pdf/1202.0362v2) and
classical Kummer/Weil point counting are explicitly credited with their
actual hypotheses in the [source audit](SOURCE_AUDIT.md). In particular
Bridy's displayed Theorem 2 in that version is not used to skip $p=2$.

## CF2: full-domain coverage is already available

For $H_{A,b}(x,y)=(A+by-x^2,x)$ with
$|A|>\max(1,|b|^2)$ over the frozen odd-residue-characteristic local
fields, Allen–DeMark–Petsche's Theorem 1(a) says the full two-sided
filled Julia set is empty exactly when $A$ is nonsquare. When $A$ is
square, Theorem 28 gives a conjugacy of that full set to the two-sided
binary shift. Every periodic point of $K^2$ belongs to that filled
Julia set, because its entire forward and backward orbit is finite.
Thus the distinct ordinary fixed count is $0$ or $2^n$, respectively,
with zeta $1$ or $(1-2t)^{-1}$.
[Primary source, Theorems 1 and 28](https://arxiv.org/pdf/1610.04271v3).

There is no uncounted periodic point outside the coded set, no field
extension silently replacing the original $K$, and no claim about the
other parameter regions or residue characteristic two. This fully
settles the frozen observable by direct source coverage, so the branch
was not developed into a new proof or experiment.

## CF3: why cohomology does not close ordinary counting

The frozen map is one two-involution automorphism of a compact Wehler
surface, not the whole automorphism group, the earlier affine rational
$W_k$ question, or an automorphism composed with Frobenius.

For every geometric point, some finite extension contains it. The
automorphism permutes that finite point set; the derivative of a return
has finite order in a finite general linear group. An iterate therefore
has identity tangent map. Its fixed ideal lies in the square of a
two-dimensional maximal ideal, and confinement makes its local length
finite but at least three. Consequently ordinary count is smaller than
fixed-scheme length along infinitely many native times.

The short proof applies to every point, but does not compute those
higher lengths. [Hutz's primary dynatomic work](https://nyjm.albany.edu/j/2010/16-8p.pdf)
already supplies relevant formal-period and multiplicity restrictions.
Neither that source scope nor the helper supplies the missing sum of
local excess multiplicities over all periodic orbits and all
characteristic-power returns. Strict inequality from a cohomological
count does not by itself imply a nonrational ordinary zeta.

The full CF3 question remains exactly unclosed. A sufficient reopening
condition is a uniform all-orbit correction theorem or another complete
ordinary-count mechanism that actually determines the rationality
classification. A finite census, more local leading terms, or a
characteristic-zero trace formula is not that condition.

## What ran, what changed, and review status

- Executed: read-only repository inspection; directed web searches;
  primary/authoritative source opening; four markdown files written via
  `apply_patch`; line-count/hash/readback checks.
- Mathematical executions: **0**. No symbolic script, finite field
  census, old proof check, old counterexample, numerical root calculation,
  GPU, paid API or legacy model override was run.
- This author wrote only this lane's `FROZEN_CONTRACTS.md`,
  `PROOF_PACKAGE.md`, `SOURCE_AUDIT.md`, and `SCOUT_REPORT.md`.
- No global state, admission registry, old proof, paper, evaluator,
  C-number, Git state, or external publication was changed.
- The source-first skills enforced exact contracts and ownership
  subtraction; proof-writer enforced CF1 completeness versus CF3's
  unresolved original question. No skill-driven manuscript pipeline was
  triggered for a rejected/unclosed scout.
- The coordinator has requested a separate non-author CF1 proof review.
  This report records the author-stage result and does not preempt that
  review or describe it as peer review. The no-slot recommendation is
  independent of whether the short reconstruction passes that check.

NO_BAD_EULER_OR_ROOT_NUMBER is unchanged. The explicit curve point count
in CF1 belongs to that source curve; no target Euler factor, functional
equation, root number, zero correspondence, automorphy or Hilbert–Pólya
realization follows from this scout.
