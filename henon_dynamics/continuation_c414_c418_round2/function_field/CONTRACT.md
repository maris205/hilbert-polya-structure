# Nonconstant quadratic Hénon maps over rational function fields

Status: **SCOUTING; NOT ADMITTED**. Coordinator-owned second entrance.
This replaces the already-owned point-count part of the Frobenius lane;
the C401 collision remains recorded in the batch plan. This is not a
separate authorized batch, a numbered paper or an A1/A2 verdict.

## Exact object and proposed complete question

Let $k$ be a field of characteristic different from two, let $t$ be
transcendental over $k$, and take

$$
a\in k^*,\qquad c\in k[t]\setminus k,\qquad
H_{a,c}(x,y)=(y,y^2+c-a x).
$$

The domain is all of $k(t)^2$ and the clock is ordinary positive iteration
of this single polynomial automorphism. The observable is its complete
set of rational periodic points, with exact point labels, minimal periods
and ordinary cycle multiplicities. It is not a geometric extension-field
count, scheme length, Frobenius clock or local completed-field horseshoe.

The proposed theorem is an exhaustive rigidity and finite-model result:
periodic rational points force $c=-P^2+C$ for a nonconstant $P\in k[t]$
and $C\in k$; if this representation exists, every point is recovered
from a field-uniform finite binary-word graph with at most 16 vertices.
The representation should be unique up to $P\mapsto-P$. The graph must
cover every constant determinant $a\ne0$, all positive-characteristic
collisions, every ordinary period and every actual point. Seek a sharp
total bound and full parameter atlas only if they follow from this same
complete graph and are independently checked.

## Decisive proof route and rejection boundary

1. At finite polynomial primes, a maximum pole order should contradict
   the monic quadratic recurrence, proving rational periodic coordinates
   are polynomials. This is a classical integrality argument, not an
   independent increment.
2. At infinity, a nonconstant parameter should force a common positive
   maximum degree $m$. Comparing squares of two periodic coordinates
   should give $y_i=\sigma_i P_0+b_i$, with $\sigma_i\in\{1,-1\}$ and
   $b_i\in k$, including coordinates from different cycles.
3. Completing the square should yield the necessary parameter form above.
   Comparing the coefficient of $P$ then forces
   $b_i=\sigma_i(\sigma_{i+1}+a\sigma_{i-1})/2$.
4. Comparing constants gives a five-sign local constraint, hence a
   four-sign state graph. It must be proved to be a partial permutation,
   with injective exact point reconstruction; a branching graph that
   merely encodes an unconstrained shift is not a uniform bound.

A single periodic point outside this reduction refutes the proposed
theorem. If the full result is already covered by an accessed theorem,
or if it reduces to a direct rephrasing of the local horseshoe theorem or
C412's integral quadratic encoding, retain it only as a companion. Do not
expand a finite parameter sample to replace a missing all-field argument.

## First cheap diagnostic, not the theorem

A one-off Python enumeration of the six coordinate symbols
$(\sigma,b)\in\{1,-1\}\times\{-1,0,1\}$ for $a=1$ and characteristics
$3,5,7,11$ yielded only the expected fixed, two-, three- and four-cycles.
Characteristic three joins the $C=0$ four-cycle with the $C=-3$ two-cycle.
This checks a small conservative specialization only. It does not prove
the general $a$ graph, the reduction, other fields or a sharp bound. No
source manuscript or old accepted check was rerun.

## Ownership and scope obligations

Read and subtract the relevant Ingram canonical-height/function-field
results, Allen–DeMark–Petsche local-field horseshoes, C412 integral
quadratic classification, and the accepted constant-coefficient
polynomial-point height contract. Verify exact hypotheses and actual
full-text access; broad search snippets do not settle priority.
Nonconstant $c$ and characteristic different from two are explicit
family choices, not hidden exclusions. Constant coefficients and
characteristic two require different statements and are not claimed.

All arithmetic is source-side. No rational-prime Euler factor, root
number, automorphy, target divisor or Hilbert–Pólya statement is implied.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
