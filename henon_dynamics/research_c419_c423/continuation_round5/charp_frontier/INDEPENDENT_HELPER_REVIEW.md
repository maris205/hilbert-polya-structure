# Independent internal review: CF1 full theorem and CF3 local helper

Date: 2026-09-08 UTC. Reviewer: current-team agent independent of the
characteristic-$p$ proof author.

**Verdict: `PASS_CF1_FULL_MATHEMATICS; PASS_CF3_HELPER_ONLY`.** No
mandatory mathematical correction was found in the complete CF1 count
and all-positive-powers natural-boundary theorem or in the stated CF3
nonreduced-iterate helper. CF3's ordinary-zeta classification remains
unclosed. CF1 is not admitted by this review: the recommendation to
retain it as a classical/owned reconstruction is supported below.

This is internal AI-assisted proof review, not human peer review,
global-priority verification, an external-model review, or a numerical
certificate. CF2's source-covered theorem is outside this review's
mathematical verdict.

## 1. Actual inspected artifacts and source scope

Read both local inputs completely:

| Input | SHA-256 at review |
| --- | --- |
| [FROZEN_CONTRACTS.md](FROZEN_CONTRACTS.md) | `ede179b5dd93d61d901eab676d28c79a92ca7641cafb847c8060d8121ed29e2b` |
| [PROOF_PACKAGE.md](PROOF_PACKAGE.md) | `e6a5a8f374daebc1546170b04a4941d474be0eeb535c1278a94c229b6eb240f0` |

The latter is the actual 347-line proof named in the review assignment,
not a summary supplied by its author. These hashes identify bytes;
they do not certify their mathematical content.

The review additionally read the following precise sources:

- [Poonen, author-hosted text](https://math.mit.edu/~poonen/papers/Qpoints.pdf),
  §7.2 and Corollary 7.2.1, and Theorem 7.7.1(ii): the smooth projective
  curve bound and its affine/geometrically irreducible point-count
  form have the hypotheses required by CF1. The whole book was not
  read, and none of its unrelated results is imported.
- [Hutz, publisher PDF](https://nyjm.albany.edu/j/2010/16-8p.pdf),
  Theorem 1.3 and Proposition 2.18(2), including the local-linear-term
  proof of the latter: the cited multiplicity-one criterion and the
  characteristic-power formal-period allowance match the limited use
  in the package. They do not provide the missing global multiplicity
  correction for CF3.
- The existing repository
  [C404 proof, §7](../../../continuation_c404_c408_round2/henon_resonance/PROOF_PACKAGE.md),
  for an ownership comparison only: its positive characteristic-tower
  weights, dominated radial-order limit and all-positive-powers
  meromorphic-boundary argument are already present there. No old
  program or independent mathematical reconstruction of C404 was run.

The author source/scout files were not present at the first directory
inspection and are not presumed reviewed here. This report does not
claim exhaustive literature access, literal published ownership of the
exact CF1 formula, or a new proof of the Hasse–Weil theorem.

## 2. CF1: the return twist and distinct-root count

Write $Q=p^n$, $r=p^{v_p(n)}$ and $n=rm$ with $p\nmid m$.
The first coordinate is fixed exactly at $x\in\mathbb F_Q$. Since the
coefficient polynomial is defined over $\mathbb F_p$, its value along
the base orbit is $a(x)^{p^j}$.

The zero-fiber branch is correct: if $a(x)=0$, every intervening
coefficient is zero, and $y^Q-y$ is separable with $Q$ roots. Thus zeros
and repeated zeros of $a$ are retained in the original ordinary domain.

On a nonzero fiber, the change $y=t z$ with $t^{p-1}=a(x)$ is a
bijection over the algebraic closure. Its moving-coordinate version
$t_j=t^{p^j}$ really gives $z\mapsto z^p+z$ at each step. The important
return multiplier is
$$t^Q/t=\operatorname{Norm}_{\mathbb F_Q/\mathbb F_p}(a(x))=\rho_x.$$
Consequently the fixed polynomial is
$$(\tau+1)^n(z)-\rho_x^{-1}z,$$
not the untwisted polynomial unless $\rho_x=1$. The proof does not
incorrectly require $t$ or $z$ to be $\mathbb F_Q$-rational.

For $\rho_x\ne1$ the derivative is the nonzero coefficient
$1-\rho_x^{-1}$, giving $Q$ distinct roots. For $\rho_x=1$, the first
nonzero operator power is $\tau^r$, because
$$(1+T)^n-1=(1+T^r)^m-1=mT^r+\cdots.$$
Thus the inseparability factor is $p^r$, not $r$ and not
$p^{v_p(n)}$ used directly as a root multiplicity. Removing that factor
leaves a separable polynomial of degree $p^{n-r}$. This verifies the
complete count
$$N_a(n)=p^{2n}-(p^n-p^{n-r})R_a(n).$$

The claimed scheme length $Q^2$ is also compatible with this
calculation: the base equation is reduced of degree $Q$, and each
monic fiber fixed polynomial has degree $Q$ counted with multiplicity.
It is not substituted for the distinct geometric count.

## 3. CF1: Kummer components and their exact clocks

The cyclic-group criterion for $t^{p-1}=b$ in $\mathbb F_Q^*$ gives
exactly $p-1$ roots if the norm is one and no roots otherwise. Therefore
$\#C_a^*(\mathbb F_Q)=(p-1)R_a(n)$ with no multiplicity or orbit-clock
factor missing.

When $a\ne0$, the cover over $U=\mathbb A^1\setminus\{a=0\}$ is finite
étale of degree $p-1$. It is smooth, and its geometric irreducible
components are disjoint. This remains true for polynomials with repeated
roots, since their zero fibers have been removed only in the auxiliary
cover and already restored in the original count.

There are at most $p-1$ geometric components, so each Frobenius cycle
length $h_j$ satisfies $1\le h_j\le p-1$ and is prime to $p$. This
simple inequality is sufficient for the later clock substitution;
no assertion that the cover is geometrically connected is required.
A component contributes rational points only if Frobenius to the
$n$-th power fixes it, since otherwise a putative rational point would
belong to two disjoint components. A cycle of length $h_j$ contributes
exactly $h_j$ fixed components when $h_j\mid n$.

Each component can be defined over its fixed finite field and then
base-changed at the relevant multiples of that field degree. Its
compactification genus and its finite missing-point set are fixed.
The Hasse–Weil estimate therefore has an implied constant independent
of $n$, although dependent on the fixed polynomial. This justifies
$$R_a(n)/p^n=
\frac1{p-1}\sum_jh_j\mathbf1_{h_j\mid n}+E_n,
\qquad |E_n|\le C p^{-n/2}.$$
No uniformity over unbounded polynomial degrees is used or needed.

## 4. CF1: analytic error, coefficients and cancellation test

After $u=p^2t$, the normalized coefficient is exactly
$$1+\frac{b_n-1}{p-1}\sum_jh_j\mathbf1_{h_j\mid n}+(b_n-1)E_n,
\qquad b_n=p^{-p^{v_p(n)}}.$$
The error series $H(u)$ is holomorphic for $|u|<\sqrt p$, since
$|b_n-1|\le1$ and $|E_n|\le Cp^{-n/2}$. In particular its exponential
is holomorphic and nonzero on an open neighborhood of the entire
unit circle. It cannot cancel a boundary zero order through a hidden
pole or branch singularity.

For a component cycle, substituting $n=h_jm$ cancels $h_j/n$ to $1/m$.
The prime-to-$p$ condition gives $b_{h_jm}=b_m$. Inserting the finite
telescoping decomposition of $b_m$ into this logarithmic series gives
the stated coefficient $1/p$ for $\log(1-u^{h_j})$ and
$$\gamma_k=
\frac{p^{-p^{k-1}}-p^{-p^k}}{(p-1)p^k}>0$$
for $\log(1-u^{h_jp^k})$. The signs and all clock denominators are
correct. Absolute convergence on smaller discs justifies the
interchanges and ties the formula to the original exponential germ.

At a primitive $p^e$-th root $\xi$, every finite term with $k<e$ and
the factors $1-u$, $1-u^{h_j}$ are nonzero. For $k\ge e$, all the
remaining factors vanish radially as $1-\rho^{h_jp^k}$. Their
logarithmic ratios lie in $[0,1]$ and converge to one for each fixed
exponent. Summability and positivity of the $\gamma_k$ therefore give
the exact radial order
$$\sigma_e=s\sum_{k\ge e}\gamma_k>0.$$

There is no cancellation between components: every component-cycle
term has the same positive coefficient. The factor $h_j$ changes the
fixed exponent inside a logarithm but not its limiting radial order.
The holomorphic error and the finitely many nonzero factors contribute
zero to that order. The bound
$$\sigma_e\le
\frac{s}{(p-1)p^e}p^{-p^{e-1}}\longrightarrow0$$
follows by replacing $p^{-k}$ by $p^{-e}$ and telescoping the remaining
positive differences.

## 5. CF1: every positive power and the edge cases

For each fixed positive integer $L$, choose $e$ sufficiently large
that $0<L\sigma_e<1$. A nonzero meromorphic extension at $\xi$ would
have an integral zero/pole order, contradicting this radial order of
$Z_a(u/p^2)^L$. Primitive $p^e$-th roots with such arbitrarily large
$e$ are dense. Any meromorphic continuation across an open boundary
arc would include one of them. This proves the full all-positive-powers
natural-boundary statement, not only a singularity at one point or
nonrationality of the original germ. Algebraicity would allow only
finitely many finite branch/pole locations, so it is also excluded.

The following analytic adversarial cases were checked separately by
hand, with no program:

- **Zero polynomial:** $R_a(n)=0$, so $N_a(n)=p^{2n}$ and the zeta is
  exactly $(1-p^2t)^{-1}$. The nonempty-cover argument starts only after
  this branch is removed.
- **Characteristic two:** $p-1=1$ gives a degree-one cover, one component
  cycle and $h_1=1$. The weights remain strictly positive; the error
  disc has radius $\sqrt2>1$. There is no lost small-prime case.
- **Nonzero constant $c$:** writing $h=\operatorname{ord}(c)$ gives
  $R_a(n)=p^n\mathbf1_{h\mid n}$. On the cover Frobenius multiplies a
  chosen $t$ by $c$, so there are $(p-1)/h$ component cycles of length
  $h$. This exactly matches the component formula and retains the
  nontrivial norm twist; the error term is zero in this example.
- **Pure $p$-power times:** $n=r$ makes the norm-one fixed polynomial
  a pure $p^n$-power, hence one distinct fiber root. The displayed
  formula gives $p^{n-r}=1$ as required. No claim of a full exponential
  growth limit is used to locate the proved natural boundary.
- **Zero/repeated-zero fibers:** each has $Q$ distinct roots by the
  separate derivative test and is not removed from $N_a(n)$.

Möbius inversion also uses the correct native clock. A fixed point of
an iterate belongs to a finite cyclic orbit even though the ambient
map need not be invertible. The least-period partition therefore
justifies $P_a(n)/n$ as the primitive orbit count.

## 6. CF3: the precise nonreduced-iterate helper

The local helper is valid for the stated general smooth surface
automorphism and hence for the confined Wehler class. Every geometric
point is defined over a finite extension of the finite base field.
The automorphism and its inverse preserve that finite rational-point
set, so the point is periodic. The derivative of its first return
belongs to a finite general linear group, including its possible
unipotent part, and has a finite order $e$.

For $b=me$, every multiple of $b$ fixes the point with identity
derivative. In completed geometric local coordinates, the fixed ideal
then lies in $\mathfrak m^2\subset\bar k[[u,v]]$. The quotient by that
ideal maps onto $\bar k[[u,v]]/\mathfrak m^2$, which has dimension three.
Confinement is exactly the assumption making the local fixed length
finite. Thus the fixed-point contribution is at least three, rather
than the ordinary contribution one, for every such multiple.

All remaining fixed-point lengths are at least one, so the strict
inequality between total fixed-scheme length and ordinary count holds
at infinitely many native times. This does not require excluding
ramification points of either deck involution: the composition is an
automorphism of the smooth surface, and its tangent map is invertible
at every point.

The proof gives neither a uniform $b$ across all geometric points nor
the sizes of their higher local lengths. In particular it gives no
formula, cancellation bound or recurrence for the total multiplicity
correction. Hutz's cited formal-period restrictions do not fill that
gap. The package correctly avoids deducing rationality or
nonrationality of CF3's ordinary zeta from the strict inequality alone.

## 7. Increment adjudication and execution boundary

Required mathematical fixes: **none found within CF1 and the stated
CF3 helper**.

CF1's literal all-polynomial theorem was not located in a publication
by this review. Nonetheless its mechanism is explicitly a Kummer
trivialization of the additive fiber, an elementary twisted root count,
a classical componentwise curve estimate, and the existing C404
positive-weight radial-order argument with finitely many prime-to-$p$
component factors. The source comparison supports retaining it as a
complete classical/owned reconstruction rather than treating this
proof PASS as automatic independent-paper admission. Final admission
authority remains with the coordinator under the batch contract.

CF3 remains `NOT CURRENTLY JUSTIFIED` for its full zeta classification.
CF2 is not given an independent PASS here; its claimed direct-source
coverage belongs to the separate source/scout adjudication.

No mathematical program, symbolic computation, finite census, GPU job
or external-model call was performed. Actual actions were complete
local proof/contract reads, selected source and repository ownership
reads, and read-only SHA-256 identification. The existing C404 proof
was consulted only for mechanism ownership; its old checks were not
rerun. Only this new review file was written, with `apply_patch`.

The research-review and proof-writer workflows governed the hypothesis,
counterexample, exceptional-case and claim-boundary checks. Under the
current batch instructions, the current team replaces the skill's
historical GPT-5.4/MCP default; no external thread or venue score is
invented. This review gives no C-number, manuscript, formal evaluation,
target Euler factor, root number, automorphy, zero correspondence or
Hilbert–Pólya conclusion. `NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
