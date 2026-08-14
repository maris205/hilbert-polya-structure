# Narrative Report — SD-C24

## The question that survived Paper21

Paper21 obtained something genuinely nontrivial from the full-shift semiring:
a recurrent successor–divisor countable Markov shift with a sharp
trace-class determinant.  Its failure was not analytic weakness.  It was a
primitive-cycle flood.  The next honest question was therefore whether the
factorization witness already present on every edge contained a finer
arithmetic coordinate.

It does.  If \(n\to d\), the relation \(d\mid n+1\) exposes the unique
cofactor

\[
 q(n,d)=\frac{n+1}{d}.
\]

This is not a post-hoc prime label.  It is exactly the missing tensor factor
in \(F_{n+1}\cong F_d\boxtimes F_q\).  SD-C24 asks the strongest version of
the resulting question: can multiplicative holonomy, group extension, or
character-resolved Fredholm theory turn that intrinsic label into the
desired prime ledger?

## The positive surprise

The cofactor product on a closed path telescopes:

\[
 Q(\gamma)=\prod_jq(n_j,n_{j+1})
 =\prod_j\left(1+\frac1{n_j}\right).
\]

The right side is strictly larger than one, while the left side is a positive
integer.  This proves at once that every cycle has nontrivial holonomy.  It
also makes the first holonomy class rigid.  A product of positive integers is
two only when one factor is two and all the others are one.  Cofactor-one
edges are precisely successor edges.  Therefore every \(Q=2\) orbit is

\[
 C_k=(k,k+1,\ldots,2k-1),
\]

and there is exactly one primitive rotation class at every length \(k\ge2\).
The same argument classifies every atomic holonomy \(p\) as
\(C_{k,p}=(k,\ldots,pk-1)\).

This is a real advance over an undifferentiated cycle flood.  The character
family of the source label group resolves the connected trace ledger exactly,
and the holonomy-two coefficient has the closed formula

\[
 \mathcal H_2(s,z)=
 \sum_{k\ge2}z^k
 \left(\frac{(2k-1)!}{(k-1)!}\right)^{-2s}.
\]

No repetition enters this class.  No prime table or zero table is needed.

## The analytic phase diagram

The natural two-parameter operator combines the inherited endpoint roof and
the new cofactor roof:

\[
 L_{s,u}e_n=
 \sum_{d\mid n+1,\ d\ge2}(nd)^{-s}q(n,d)^{-u}e_d.
\]

Its trace-class domain is not merely sufficient; it is exact:

\[
 L_{s,u}\in\mathcal S_1
 \iff
 \Re s>\frac12,
 \quad
 \Re(s+u)>\frac12.
\]

The two inequalities arise from different pieces of the same graph.  The
tails in a fixed output row force the combined exponent
\(\Re(s+u)>1/2\).  The cofactor-one successor spine ignores \(u\) entirely
and forces \(\Re s>1/2\).  This independence is the analytic heart of the
paper: the cofactor twist cannot regularize the part of the graph on which
the cofactor equals the multiplicative identity.

## Why the group extension does not rescue the ledger

The regular group extension separates base cycles by their cofactor product.
Its neutral trace extracts \(Q=1\).  But \(Q=1\) never occurs, so every
neutral trace vanishes and the normalized local semifinite determinant is
one.  This is total trace blindness, not arithmetic selectivity.

A second distinction is essential.  The lift is \(L^1\) relative to the
semifinite group trace for \(\Re s>1/2\).  It is nevertheless not an
ordinary compact operator on the lifted Hilbert space: right translations in
the infinite deck coordinate reproduce any nonzero image with infinite
multiplicity.  These statements live in different operator ideals and are
reported separately throughout the project.

Character fibers behave differently but do not help enough.  A unitary
character changes only phases.  Every canonical cycle receives the same
phase \(\chi(2)\), so every \(C_k\) remains visible.  Exact Fourier
resolution prevents cancellation between different holonomy classes from
being misread as orbit deletion.

## The Fredholm trilemma

The source object offers three natural choices.

1. **Pure cofactor roof.**  Setting \(s=0\) gives a cycle of holonomy \(p\)
   the attractive weight \(p^{-u}\).  But the cofactor-one spine is the
   unweighted unilateral shift.  The whole operator is never trace class and
   is noncompact whenever bounded.  In the \(Q=2\) class, the formal series
   is \(2^{-u}z^2/(1-z)\), divergent at \(z=1\).
2. **Endpoint regularization.**  Taking \(\Re s>1/2\) produces an honest
   Fredholm determinant, but a canonical orbit receives the factorial weight
   \([ (2k-1)!/(k-1)!]^{-2s}\).  The analytic repair changes the arithmetic
   species.
3. **Unitary characters.**  They retain the sharp base half-plane and attach
   phases, but all canonical lengths survive.

First-return induction does not evade this choice.  It collapses every
\(C_k\) to a separate fixed return branch.  With pure cofactor roof and
\(z=1\), those branches have a constant nonzero diagonal entry.  With the
endpoint roof, they become summable only because the factorial dependence on
\(k\) remains.

## Route meaning

SD-C24 earns structural and analytic credit.  The cofactor is intrinsic, the
class ledger is exact, and the scalar character fibers have honest
trace-class Fredholm determinants.  It does not earn target completion.
For every atom \(p\), the candidate produces an infinite grid
\((p,k)\), not one primitive orbit per prime, and its natural endpoint roofs
are not \(\log p\).

The strict tuple is

\[
(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
 \mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_FAIL},
 \mathrm{A4\_FAIL}),
\]

so \(\mathrm{ROUTE\_A\_REJECTED}\).  Route B remains locked.

## What has been closed

Any statistic depending only on the abelian product \(Q(\gamma)\) is
constant on all \(C_k\), because \(Q(C_k)=2\).  No new scalar character,
Fourier combination, or positive inventory can recover the missing run
length from that product.  This closes the abelian product-holonomy branch
for the successor–divisor graph.

The smallest possible successor would have to retain the ordered cofactor
word \(1^{k-1}2\) and first confront the eventual-periodicity barrier for
finite-state readers.  That is recorded only as a next obligation; it is not
part of SD-C24 and is not started here.

