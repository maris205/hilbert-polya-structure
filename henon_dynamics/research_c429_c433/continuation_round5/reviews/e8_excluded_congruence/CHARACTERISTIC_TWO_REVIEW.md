# E8 targeted review: the characteristic-two parameter domain

2026-09-10 UTC. Separately allocated nonauthor review of the new domain,
using proof-writer and research-review with the current selected model.
This file does not amend or enlarge the historical scope of the original
411-line E8 review. Only changed-domain implications and their relevant
proof dependencies were checked; no mathematical program was run.

## Decision and version pins

**PROVABLE AS STATED.** The characteristic-two addendum passes in full.
Mathematical must-fixes: **0**. Imported-source applicability must-fixes:
**0**. Required minor/textual repairs: **0**.

The actual [author addendum](../../a2_excluded_congruence/CHARACTERISTIC_TWO.md)
was read completely, all 322 lines, including the final notation and
verification material. Reviewed SHA256:
`0e7d600e2b35455aa5b93ffefef34c357d8a71e9fb3c20aa76dcf6f1be13d18a`.

The following frozen files remain unchanged and retain their original
statement/review scopes:

- [Original E8 review](REVIEW.md), 411 lines:
  `a88ab98256491744ff2d29a90685142720be552f4cf6a3dc8428c75a89b961e2`.
- [R5 proof](../../a2_excluded_congruence/PROOF_PACKAGE.md), 517 lines:
  `b703fde520e5405b6ab28833a40dcce324925bebbbeaefea6b9ca22de57445e3`.
- [R5 report](../../a2_excluded_congruence/REPORT.md), 203 lines:
  `2d99b82dc75d50d18b8e74eb20a12a97d9a1117e50a13f950c5dfb087b7f99a5`.
- [R4 proof](../../../continuation_round4/a2_unicritical_carry_extension/PROOF_PACKAGE.md):
  `766f8d95f3297fdfe2b803965bc217ed28ccc7934090c07c68f42c9624f0cd01`.

This is one same-PC424-L parameter completion, not a new contract or
paper count. Coordinator integration and any priority assessment are
separate from this mathematical review.

## Exact new-domain claim

For $k=\overline{\mathbf F}_2$, every integer $d\ge2$, every
$c\in k$, and $f(x)=x^d+c$, the reviewed conclusion is

$$
\left\{h\in k[x]:\sum_{a\in O}h(a)=0
\text{ for every ordinary primitive }f\text{-orbit }O\right\}
=\{Q\circ f-Q:Q\in k[x]\}.
$$

Coefficients are not restricted to the prime field. The native clock
remains one application of $f$. Each distinct ordinary orbit point
is counted once, including primitive periods divisible by two.

For $\deg h\le M$, $M\ge1$, including zero input, the addendum
also proves these finite tests equivalent to coboundary membership and
ordinary-root return-sum vanishing at the same two levels:

| Degree branch | Return levels | Polynomial test |
| --- | --- | --- |
| Odd $d$; $P=2^{v_2(d-1)}$ | $n=7\lfloor\log_d(PM)\rfloor+22$, $n+1$ | $F_j\mid D^{[P]}F_j\,\widetilde H_j(h)^P$ |
| Even $d$ | $n=3\lfloor\log_dM\rfloor+4$, $n+1$ | $F_j\mid\widetilde H_j(h)$ |

The primitive detection cutoff is $n+1$ in each row. The respective
iterate-polynomial degree bounds are $d^{23}(PM)^7$ and $d^5M^3$.

## 1. Common inputs and the scope of their reuse: PASS

The normal form uses only that $\Delta x^r$ is monic of degree $dr$.
Its triangular elimination and directness proof therefore remain valid
when two is zero, including when $d$ is even. The degree does not rise;
zero input is explicitly handled with $Q=v=0$.

The full cyclic quotient is still $k[x]/(F_j)$ of dimension $d^j$.
Digit reductions lower total degree, and the number of digit monomials
equals this dimension. These facts use neither separability nor an odd
characteristic. Telescoping remains an identity in that full quotient.

Thus the addendum legitimately reuses these algebraic proofs after
checking their actual hypotheses. It does not cite the odd-characteristic
R4 or R5 theorem statements as if those statements already included
characteristic two.

## 2. Odd degree and the $P=2$ composition boundary: PASS

For odd $d$, $P=2^{v_2(d-1)}$ satisfies $2\le P<d$,
$A=(d-1)/P$ is odd, and $\alpha=[A]=1$. Also $\gcd(d,P)=1$,
so the normal exponent condition survives multiplication by $P$.
The coefficients of $v^P$ are the actual $P$th powers of the
coefficients of $v$, not assumed fixed by Frobenius.

The multiplicity-safe Hasse implication uses root orders and the Hasse
product rule only. It works in characteristic two, including zero Hasse
derivatives and arbitrarily large root multiplicities.

Expanding $(x+z)(x^P+z^P)^A+c$ gives the same linear coefficient
and first nonlinear coefficient as in R5, now with scalar one. For
$P=2$, the absent-order interval is empty, but the composition formula
is still exact: substituting $a z+b z^2+O(z^3)$ into the outer
Taylor expansion gives order-two coefficient

$$
f'(g)b+D^{[2]}f(g)a^2.
$$

No further cross term has order two. For higher powers $P$, the
previous absence of intermediate orders applies without change.
Consequently the one-mark background formula is valid for every odd
$d$ in characteristic two, including its $P=2$ boundary. The background
numbers are integer exponents, not coefficients reduced modulo two.

## 3. Cuts, source localization, and coincident anchor digits: PASS

The two numerical uses of odd characteristic in the original wording
can be weakened exactly as the addendum states:

$$
P\ge2\ \Longrightarrow\ d-P+1<d,
\qquad d\ge3\ \Longrightarrow\ d-1\ge2>1.
$$

The original adaptive-cut carry bound and its predecessor estimate
are integer inequalities. They still bound the final cut exponent by
$d$. An overflowing branch still leaves the cut digit at most one,
which is strictly below the target digit $d-1\ge2$. Its exclusion
therefore remains valid. Legal branches keep the same quotient and
binomial weight, including when $-c=c$.

The baseline values $P-1$ and zero, the nonpositive-excess recurrence,
and the two source-location exclusion intervals require $P<d$, not
$P\ge3$. The argument still excludes every outside source and
source-free marked background before adopting the common cut. At that
cut, the target forces final carry one and the closed convention
$t_0=t_j=1$ without changing the first quotient.

For $P=2$, the anchor digit equals the long-block digit for every
allowed odd $d$, not only $d=3$. This causes no aliasing in the
argument: no step identifies site zero by uniqueness of its digit or
requires the anchor to be smaller than the long block. The cut positions
are fixed by indices. The strict digit comparison needed later is
$(PD-1)\bmod d<d-1$, which still follows from $d\nmid PD$.

At the smallest case $d=3$, $P=2$, the backgrounds are $4,1,2$.
The target cut digit is two, overflowing outcomes have digit zero or
one, and the common-cut exponent is $2<3$. Thus the smallest strict
inequalities and the coincident-anchor boundary both pass.

## 4. Every mark, every weight, and the new contribution: PASS

The old-mark insertion and deletion use the same localized source
interval and the same baselines. An unmarked inserted site has incoming
and outgoing carry $P-1$ or zero, equal to its quotient. Its weight
is one in characteristic two as well. The inverse includes marks
immediately before and immediately after the inserted site; no sign
distinction between $c$ and $-c$ is used.

Every old binomial weight is preserved as an element of the actual
field, including weights that vanish modulo two. Thus any cancellation
among old terms occurs identically at the two levels. No nonzero weight
or cancellation-free expansion is assumed.

The new-mark isolation still uses the exact integer identity

$$
Pr=PDd^{S-i}+\sum_{u=i}^{N-1}\kappa_ud^{u-i+1},
\qquad r\le D,\quad i\le S,\quad \kappa_u\ge0.
$$

It forces $i=S$, $r=D$, and every suffix loss to vanish. Earlier
transitions retain their forced baselines. The unique surviving path
has all weights one, including all high-background reductions; no
positive power of $c$ is omitted. The coefficient difference is
$a_D^P\ne0$.

In characteristic two, subtraction equals addition, but subtracting
equal paired contributions still gives zero. The proof never divides
by two or cancels a scalar asserted to be a nonzero two. Thus the
coefficient comparison excludes a positive normal remainder exactly
as claimed, with every mark and source retained.

## 5. Odd-degree constants and finite bounds: PASS

One of two adjacent return levels is odd. At that level the leading
coefficient of $D^{[P]}F_j$ is $j\alpha=1$, so the derivative is
nonzero and has degree $d^j-P<d^j$. For constant normal remainder
$a_0$, the certificate becomes
$F_j\mid j a_0^P D^{[P]}F_j$ and forces $a_0=0$.
Here integer scalars are fixed by Frobenius; arbitrary coefficients
$a_0$ are not assumed fixed.

Coboundaries telescope, root vanishing gives the multiplicity-safe
certificate, and the two tests exclude both types of normal remainder.
The odd-degree equivalences therefore hold at exactly the declared
$n,n+1$, with the unchanged R5 period and iterate-degree bounds.

## 6. Even degree: direct squarefree and digit proof: PASS

For even $d$, direct differentiation gives $f'=0$ and
$F_j'=-1=1$. Hence every return polynomial is squarefree.
Ordinary-root vanishing is therefore equivalent to divisibility by
$F_j$ and to zero in the full periodic quotient. This is proved
directly in the new characteristic, not imported from an odd-prime
theorem statement.

The addendum supplies the complete relevant leading-digit argument.
For a positive normal degree $D$, its base-$d$ expansion has nonzero
first and last digits. In a forward window with weights
$1,d,\ldots,d^q$, where $q=\lfloor\log_dD\rfloor$, reductions
preserve weight on the variable branch and strictly lower it on a
constant branch. No branch leaves the window. At $j>2q$ only the
source-zero window can contain both target endpoints; the $q=0$
singleton case is included. The unique branch of weight $D$ has
coefficient one, so the target coefficient is exactly $a_D$.

This remains true for composite even $d$ and for $d=2$; it does
not require normal exponents themselves to be odd. Characteristic-two
signs or binomial cancellation cannot eliminate the isolated coefficient.
The two chosen levels exceed the required bound for every $D\le M$.
Thus the two divisibilities exclude a positive normal remainder.

For a constant remainder, the equations are $na_0=0$ and
$(n+1)a_0=0$; the odd level forces $a_0=0$. The reverse implications
follow by telescoping and squarefreeness. This establishes the even-degree
certificate at the stated bound $n=3\lfloor\log_dM\rfloor+4$,
with iterate-polynomial degrees at most $d^5M^3$.

## 7. Ordinary wild periods, combined coverage, and receipt

In both branches, the identity
$\widetilde H_j(h)(a)=(j/r)S_h(O_a)$ is repetition of an ordinary
sum, not division in the field. A nonzero return sum implies a nonzero
primitive sum even in characteristic two. If $j/r$ is even the
return sum is zero, so such a root cannot be the selected failed test;
this does not remove primitive even periods from the theorem.

The constants and zero polynomial are covered explicitly, $c$ and all
polynomial coefficients range over the full algebraic closure, and the
finite logarithms use a positive degree or the positive cap $M$.
The native clock and ordinary-root test convention remain unchanged.

The combination with the previously reviewed odd-prime ranges is
disjoint and exhaustive: $p\mid d$, $p\mid d-1$, or
$p\nmid d(d-1)$. The final range has no characteristic-two case.
Thus the addendum's combined all-prime/all-degree kernel statement is
supported by the actual verified dependencies. It does not retrospectively
change the old theorem files or their historical review scopes.

There is no new external theorem whose hypotheses require source
verification, and no root-multiplicity growth estimate is assumed.
Global novelty and formal integration remain coordinator decisions.
No extra contract, target Euler factor, root number, or Hilbert–Pólya
conclusion is asserted.

Work was limited to the new domain, relevant frozen proof passages,
direct hand reasoning, and read-only hashes. Mathematical executions,
external model/API calls, new agents, Git operations, old/shared-file
edits, and PDF work were zero. The only new workspace write is this
separate review file; the original 411-line review is preserved.
