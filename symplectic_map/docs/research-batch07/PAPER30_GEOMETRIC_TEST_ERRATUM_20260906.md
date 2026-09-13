# Paper30 geometric probe: finite periods and a single period

Date: 2026-09-06. Status: AUTHOR_CORRECTION_TO_A_FROZEN_PREFLIGHT.
This explicit correction supplements, and does not overwrite, the author
[geometric probe](PAPER30_GEOMETRIC_TEST_PROBE_20260906.md), SHA256
`c2520f2651270b0fddc24a53ace06dca8c5486b9ab1180d7554f58670ce58f73`.
It implements the actual finding in §7 of the
[independent check](PAPER30_GEOMETRIC_INDEPENDENT_CHECK_20260906.md), SHA256
`55e74b146e1d53d2a0103bc1886bdc129fe83f6f85195a85b750c5d51c0674f3`.
Root has fully read that 329-line report. The original incorrect statements
remain visible in the frozen author input; this document takes precedence
for their mathematical interpretation. No other claim is changed.

## 1. Exact correction and assumptions

In the original §6.3, the assertion that finite-period detection does not
automatically become single-period detection is false under its actual
convention of testing all of $\operatorname{Fix}(F^n)$, including points
whose least period divides $n$. The corresponding final limitation in §8
must also be removed. The correction requires no additional assumption.

Fix the same complex Hénon map $F$, $\sigma=F^*$ and degree bound $D$.
Let $\mathcal H_D$ be the image of degree-at-most-$D$ polynomials in
$A/(\sigma-1)A$, and write $S_ng=\sum_{j=0}^{n-1}\sigma^jg$.
It is finite dimensional. Geometric periodic evaluation is well-defined on
$\mathcal H_D$ because a coboundary telescopes to zero at each periodic point.

**Corrected claim — PROVABLE AS STATED.** The following are equivalent:

1. The geometric periodic evaluation functionals for all periods have zero
   common kernel on $\mathcal H_D$.
2. The complete geometric tests for finitely many periods have zero common
   kernel on $\mathcal H_D$.
3. The complete geometric test for one period $M$ has zero common kernel on
   $\mathcal H_D$.

If such an $M$ exists, every positive integer multiple of $M$ also works.
This is not a statement that every sufficiently large integer period works.

## 2. Complete proof and dependency map

The only dependencies are finite-dimensional linear algebra, divisibility
of periods, and division by positive integers in characteristic zero.

Step 1. Suppose condition 1 holds. Starting with $\mathcal H_D$, if the
current intersection of selected kernels is nonzero, at least one further
periodic functional is nonzero on it. Intersecting with that kernel reduces
the dimension by at least one. At most $\dim\mathcal H_D$ selections give
zero kernel. Replace the selected points by the complete tests at their
periods $n_1,\ldots,n_s$; this only shrinks the kernel. Thus 2 holds.
If $\mathcal H_D=0$, every period already works and no selection is needed.

Step 2. Given a nonempty finite choice in 2, set
$$
M=\operatorname{lcm}(n_1,\ldots,n_s).
$$
For any $z\in\operatorname{Fix}(F^{n_i})(\mathbb C)$, one has
$z\in\operatorname{Fix}(F^M)(\mathbb C)$ and
$$
S_Mg(z)
=\sum_{r=0}^{M/n_i-1}\sum_{j=0}^{n_i-1}g(F^{rn_i+j}z)
=\frac{M}{n_i}S_{n_i}g(z).
$$
If the complete test at $M$ vanishes, each selected lower-period test
vanishes, since $M/n_i$ is nonzero and invertible in $\mathbb C$.
Condition 2 then forces $[g]=0$, proving 3. An empty choice only occurs
when the space is already zero, covered in Step 1.

Step 3. Condition 3 implies 1 because all-period testing contains the test
at $M$. Replacing $M$ by $tM$ in Step 2, with $n_i=M$, proves the assertion
about multiples for every integer $t\ge1$.

## 3. Replacement conclusions and remaining risks

The last paragraph of the original §6.3 should now be read as follows:

> Provided all-period sufficiency holds, finite-dimensional selection gives
> finitely many detecting periods, and their least common multiple gives
> one detecting period. The argument provides neither an effective upper
> bound for that period nor detection at every sufficiently large integer.

The final unresolved-obligation paragraph of the original §8 should be read
as follows:

> For each fixed map, the remaining main problem is to establish zero common
> kernel of all geometric periodic functionals, or to find a counterexample.
> If that sufficiency is established, non-effective single-period existence
> follows from the preceding lemma; effective bounds and an all-sufficiently-
> large-period assertion still require additional arguments.

No assertion that the common kernel is zero has been added. The conditional
Loewy mechanism, the separated-block power lemma, the explicit finite-period
counterexample, the scalar three-period result, and the across-maps resonance
family remain exactly as independently checked. In §6.1, an effective period
search from $b_F(n)=o(n)$ requires the already stated effective/explicitly
usable bound $b_F$; a bare non-effective asymptotic assertion is not an
effective numerical bound.

This correction strengthens a conditional finite-dimensional corollary;
it does not close the main geometric problem, establish novelty or long-paper
capacity, authorize a manuscript, or count Paper30 as completed. It is not
part of the separate quantum candidate's review package. Effects are local
only; Route applicability remains NOT_APPLICABLE.
