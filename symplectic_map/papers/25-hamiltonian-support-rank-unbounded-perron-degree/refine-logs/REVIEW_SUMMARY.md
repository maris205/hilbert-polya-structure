# Review Summary

## Inputs and independence boundary

This source-design reconciliation uses the two root-level candidate records
without copying them into the project:

- R1: 21,097 bytes, 603 LF, SHA-256
  c8044d3d41573df7d1cd356acaa1e78414e18b3608e76a50553157c556495d0f.
- R2: 17,460 bytes, 663 LF, SHA-256
  46724d7d3c764d95f8235e6ffc40b40d78c6130ccf9c85a5832bbc4b5ca6b408.

R1 was proof-first and included a bounded primary-source screen through
2026-08-26 UTC. R2 was mutually blind, offline, proof-first, and
computation-free. Both gave proof confidence 9.6/10 and passed the complete
candidate. R2 assigned no external novelty score because it used no network.
This document reconciles their formulations; it is not a third independent
review.

## Finding reconciliation

| Topic | R1 formulation | R2 formulation | Frozen source-design resolution |
|---|---|---|---|
| Support rank | Factor through a row basis of $\binom Q S$ and use Sylvester. | Equivalent factorization through the same row span. | Give one explicit factorization and retain both the determinant and common-kernel interpretations. |
| Unit eigenvalue | Multiplicity is at least $n-r$. | Reduced factor may contain more copies of $t-1$. | No exact unit multiplicity or exact profile claim. |
| Selector domain | Broad ratio cone, with weighted order proved along the seed orbit. | Coordinate ratio and weighted order combined in one chamber. | State two nested regions and prove the role of each. |
| Carries | Cross-phase domination plus componentwise temporal induction. | Phase-labelled old-versus-new comparisons. | Include a complete coordinate-polynomial induction with all carries. |
| Top forms | Positive-semiring survival. | Unique selected source and nonzero derivative coefficients. | Use both: strict degree separation and nonnegative integer coefficients embedded in characteristic zero. |
| Arithmetic | Full binomial criterion, with $d=2$ and $4\mid d$. | Same, independently derived. | State the named criterion, verify every hypothesis, and retain both boundary audits. |
| Scalar order | Perron asymptotics exclude a lower-order tail recurrence. | Reachability, observability, and Hankel rank give global minimality. | Prove Hankel rank $d$ and add the asymptotic argument for eventual recurrences. |
| Sharpness | The family has support-row rank $d$ and quotient degree $d$. | Same. | Claim existential sharpness for every rank $r=d\ge2$ covered by the family. |

## The two-level cone formulation

Let

$$
R=1+\frac{2M}{bS_a},\qquad 1<R<\sqrt2.
$$

The broad ratio cone is

$$
\mathcal K_{\rm ratio}(R)
=\{u\in\mathbb R_{>0}^d:\max_i u_i\le R\min_i u_i\}.
$$

It contains $\mathbf1$, all pure spikes are strictly selected on it, and
$C\mathcal K_{\rm ratio}(R)$ lies in its strict interior. It is also the
right domain for a uniform cross-phase domination estimate.

The fine visibility chamber is

$$
\mathcal K_{\rm vis}(R)
=\{u>0:u_i\le u_1<Ru_i\ \text{and}\
a_1u_1<a_i u_i\ \text{for every }i>1\}.
$$

It is contained in the broad cone. The seed has equality at the permitted
walls $u_i\le u_1$ and satisfies all strict upper-ratio and weighted
inequalities. The parameter inequalities imply
$C\mathcal K_{\rm vis}(R)\subset\mathcal K_{\rm vis}(R)$, with strict
coordinate ordering after one step. This chamber supplies a fixed visible
coordinate. Equivalently, the weighted order can be proved only along the
ordinary-seed orbit inside the broad cone, but the article will use the
nested-cone formulation because it makes dependencies auditable.

## Accepted corrections and wording controls

1. A primitive element $c$ always means an element of order exactly $p-1$,
   not merely a nonzero element.
2. The characteristic-zero restriction is explicit wherever positive
   derivative coefficients and no cancellation are used.
3. Visibility is unique only for positive iterates; at $n=0$ all coordinate
   degrees equal one.
4. The scalar recurrence claim is over rational constant coefficients and
   includes a precise definition of order.
5. Sharpness is stated for the nontrivial ranks $r=d\ge2$ constructed here.
   No assertion about ranks zero or one is smuggled into the all-$d$ theorem.
6. The support-rank theorem bounds nonunit characteristic degree but does
   not determine an exact spectral profile.
7. The $d=4$ and isolated $d=5$ cases are examples only; they do not carry
   the novelty statement.

## Refined theorem package

The accepted package consists of five inseparable outputs.

1. An explicit support-row factorization
   $\chi_C(t)=(t-1)^{n-r}Q_r(t)$ with $Q_r$ monic of degree $r$.
2. For every $d\ge2$, an explicit positive Hamiltonian product shear whose
   selected complete-step matrix is
   $C=b\mathbf1a^{\mathsf T}-D$.
3. A two-level strict selector, carry, and visibility proof giving
   $\deg(F^n)=e_1^{\mathsf T}C^n\mathbf1$.
4. A modular construction making $\chi_C$ irreducible of degree $d$, hence
   making the dynamical degree a Perron algebraic integer of degree $d$.
5. A reachability-observability proof that the visible scalar sequence has
   minimal rational recurrence order $d$, together with rank-$d$ sharpness.

Removing any one of selection, exact visibility, irreducibility, scalar
minimality, or support-rank sharpness materially weakens the paper and may
collapse it into established infrastructure or local predecessor territory.

## Remaining design-stage risks

No mathematical blocker remains in the supplied theorem package, but later
stages must independently rederive it. The most fragile presentation points
are the two cone roles, the direction of the visibility inequality, the
separate two phase carries, and the distinction between matrix recurrence
dimension and scalar minimal order. Bibliographic metadata and the bounded
noncollision conclusion must be reverified before any bibliography or source
lock. No such later action is authorized by this summary.

## Review-summary disposition

The proposal survives refinement without enlarging its scope. It proceeds as
a 22--30-page proof-first design, subject to an independent source-design
review. No manuscript or build is opened here.

SOURCE DESIGN AUTHOR STOP
