# Paper 22 — Analytic Verification Plan

## Authorization state

This project has zero scientific experiments. The word “verification” below
means a deterministic, line-by-line human audit of a fixed symbolic proof.
No numerical orbit, finite parameter scan, CAS certificate, network lookup,
GPU run, benchmark, dataset, plot, or hidden computation is authorized.

The source-design author records the proof obligations but does not certify
their independent completion. Every item remains planned until a distinct
reviewer reads the frozen ten-file package and issues a disposition.

## Proof-only verification sequence

1. Expand every coordinate of $\nabla V_{r,g}$ and $\nabla W_{r,g}$, write the
   subtraction inverses, and check preservation of
   $\omega=\sum_i dq_i\wedge dp_i$ from Hessian symmetry.
2. Enumerate every gradient monomial and bind its exponent row to
   $M_r=2\mathbf 1\mathbf 1^{\mathsf T}-I_r$ or to one endpoint row
   $h e_1^{\mathsf T}$ or $h e_r^{\mathsf T}$, where $h=g-1$.
3. Derive $A_{r,g}$ and $B_{r,g}$ from those literal rows and multiply
   $C_{r,g}=B_{r,g}A_{r,g}$ entry by entry.
4. Normalize only by $u_1$ and verify that
   $x_i=u_i/u_1$ is defined for $2\le i\le r$ and that
   $\sigma=\sum_{i=2}^r x_i$ never includes $x_1$.
5. Check the first selector margin
   $h-1-2\sigma$ and the separately derived second selector margin on the
   full open cone, including the threshold $h=2m+4$ with $m=r-2$.
6. Check every invariant-cone boundary: each allowed lower face $x_i=1$, the
   limiting open height face, and the least parameters $m=2$ and
   $h=2m+4$.
7. Verify seed containment and the exact boundary failure at $g=2r$:
   the seed reaches the height boundary and the first selector has a tie.
8. Audit the phase-labelled carried-coordinate induction using $C-I>0$,
   nonzero nonnegative rows of $A$, and $C-A>0$.
9. Audit leading homogeneous forms in a polynomial domain. Repeat the argument
   for exactly four arbitrary nonzero coefficients
   $\alpha,\beta,\gamma,\delta$ on the displayed supports.
10. Prove that the last $q$-coordinate strictly dominates all other
    coordinates only for full iterates $n\ge1$; record the harmless tie at
    $n=0$ separately.
11. Verify the exact degree formula, the Perron–Frobenius root limit, and the
    absence of a visibility gap.
12. Verify $K^r=U\oplus E$, the actions $A|_U=B|_U=-I$, the displayed
    three-dimensional quotient, its determinant and principal minors, the
    cubic $P_{m,h}$, and $P_{m,h}(1)$.
13. Check that the eigenvalue $1$ has algebraic multiplicity exactly $r-3$
    and that the cubic is an annihilator, not necessarily a minimal or
    irreducible polynomial.
14. Substitute $m=1$ only as a predecessor-consistency check against Paper 21.
    Do not convert that calculation into a Paper 22 claim for $r=3$.
15. Audit the collision, anti-claim, coefficient, characteristic, and
    permission boundaries before any later source lock is considered.

## Reproducibility worksheets

### W1 — Gradient ledger

For each of the $2r$ derivative rows, record the source potential, target
coordinate, coefficient, and exponent row. There are exactly two competitive
derivative rows: the first row of $\nabla V$ and the last row of $\nabla W$.
Every other derivative has one monomial.

### W2 — Selector ledger

Use

$$
m=r-2,\qquad h=g-1,\qquad
x_i=\frac{u_i}{u_1}\ (2\le i\le r),\qquad
\sigma=\sum_{i=2}^r x_i.
$$

The cone is

$$
\mathcal K_{r,g}=
\left\{u>0:x_i\ge1,
\sigma<\frac{h-1}{2}\right\}.
$$

The audit must retain the open upper face, allow equality on every lower face,
and split each negative-coefficient estimate with the inequality direction
reversed correctly.

### W3 — Carry and leading-form ledger

Track $u_n$ as the $q$-degree vector after $F^n$ and $v_{n+1}$ as the
intermediate $p$-degree vector after the next first shear. The intended phase
identities are

$$
v_{n+1}=Au_n,\qquad u_{n+1}=Cu_n.
$$

Each identity requires both strict degree comparison and nonzero survival of
the selected leading homogeneous form.

### W4 — Spectral ledger

State the coordinate convention

$$
(a,b,c)\longmapsto(a,b,\ldots,b,c)
$$

before writing the quotient matrix. Compute its trace, three principal
$2\times2$ minors, and determinant without relying on sampled ranks.

### W5 — Boundary ledger

The three mandatory boundary statements are:

- $g=2r+1$ is inside the proof range and every decisive margin is strict;
- $g=2r$ gives a seed/selected-face tie and is not a global impossibility
  theorem for degree dynamics;
- $n=0$ has a coordinate tie, whereas strict $e_r$ visibility starts at
  $n\ge1$.

## Credible manuscript mass

A later proof-first article can occupy 24–28 substantive content pages without
governance padding:

| Content block | Planned pages |
|---|---:|
| Introduction, exact question, and predecessor disclosure | 2.5–3 |
| Family, gradients, inverses, symplecticity, support rows | 3–3.5 |
| Two selectors and sharp seed/face threshold | 3–3.5 |
| Full invariant-cone proof | 4–4.5 |
| Carry induction, leading forms, coefficient corollary | 3.5–4 |
| Visibility, exact degrees, Perron limit | 2.5–3 |
| Invariant space, quotient, cubic, exact multiplicity | 4–4.5 |
| Boundary examples, low-rank lineage, limitations | 1.5–2 |

The target is a content budget, not a page-count certificate. A later draft
outside 22–30 substantive pages requires an independent completeness review.

## Failure policy

Any failed selector, cone wall, carry comparison, leading-form argument,
visibility inequality, quotient identity, or predecessor boundary returns the
project to repair. A numerical example cannot cure a symbolic failure. This
plan grants no source lock, paper plan, manuscript, build, release, or external
effect.
