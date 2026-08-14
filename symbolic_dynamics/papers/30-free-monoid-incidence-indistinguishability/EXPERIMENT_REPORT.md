# Paper 30 exact report — Boolean joins and the free-commutative clone

Candidate: **SD-C32**
Strongest GO: **Boolean triple finite-fixture separation plus an auxiliary
trace-class Gram determinant**
Strongest STOP: **source specificity fails by an exact
free-commutative/UFD clone**
Overall: **rejected as an RH completion**

## Outcome

The frozen coherence selector is genuinely stronger than the SD-C31
pair-local counterterm, but it still cannot distinguish integer divisibility
from unique factorization itself.

At the finite-fixture level, the connected triple statistic succeeds:

\[
\Theta_3
=2\sum_{a<b<c}\chi_3(a,b,c)
\frac{G_{ab}G_{bc}G_{ca}}{\nu(a)\nu(b)\nu(c)}
\]

is nonzero at all three integer-divisibility active cutoffs and exactly zero
on the mutated-cover, composite-only, generic-DAG, and random-inventory
fixtures.

The pair statistic fails sooner. The mutated-cover source still contains the
three untouched fully coherent pairs

\[
(2,5),\qquad(2,7),\qquad(3,5).
\]

More decisively, every baseline pair and triple, every Gram coefficient,
every marker exponent, and every one of the 31 nonempty predicate-mask counts
is reproduced term by term by an abstract free-commutative monoid and by a
polynomial-UFD monomial factorization control with transported decorations.
The candidate therefore detects free unique factorization, not a structure
specific to the integer primes.

## Frozen coherence

Atoms are always bottom covers. For a pair or triple \(S\), the selector
\(\chi_k(S)\) requires:

1. a unique join \(j_S\);
2. a Boolean interval \([\bot,j_S]\cong B_k\);
3. \(\mu(\bot,j_S)=(-1)^k\);
4. \(\nu(j_S)=\prod_{a\in S}\nu(a)\);
5. associative ownership of the join by iterated binary lcm/tensor product.

All five predicates are computed from the pointed decorated source. Numeric
roof marks enter only after the cover predicate derives the atoms. The full
five-predicate conjunction was frozen before results; the 31-mask enumeration
is a robustness audit, not post-hoc selector choice.

At \(\eta=2\), in units of \(C_\eta\), the normalized divisibility Gram is

\[
g_{pp}=1+p^{-4},\qquad
g_{pq}=\frac{1}{(p^4+1)(q^4+1)}.
\]

The filtered zero-diagonal atom matrix is

\[
H_{pq}=\chi_2(p,q)\frac{G_{pq}}{\sqrt{pq}},
\qquad H_{pp}=0.
\]

Its first two nontrivial finite characteristic coefficients are

\[
[z^2]\det(I+zH)=-\sum_{p<q}H_{pq}^2,
\]

\[
[z^3]\det(I+zH)
=2\sum_{p<q<r}H_{pq}H_{qr}H_{pr}.
\]

The separately filtered \(\Theta_3\) uses the stronger triple predicate rather
than merely requiring the three pair edges.

## Exact census

| Ledger | Rows | Exact result |
|---|---:|---|
| baseline pair/triple subsets | 241 | every predicate true |
| finite-control subsets | 118 | pair survivors 3; triple survivors 0 |
| free/UFD controls | 45 | all pairs and triples coherent |
| predicate-mask audit | 186 | no pair mask separates; triple finite separators exist |
| marker ownership | 165 | every exponent exact at theorem value \(u=1\) |
| independent evaluator | 1616 | 1616/1616 PASS |
| regression tests | 28 | 28/28 PASS |

Two isolated authority fresh runs produced the same set of 17 generated
artifacts byte for byte. Their aggregate artifact-ledger SHA-256 is
`b2ea8f6c6803ef5a0a01999452f7e68ed099ccb04f2e24c8592b97b5e1fef316`,
which is exactly the preregistered prototype aggregate. The authority freeze
ledger contains 31 code/result hashes and passes strict verification together
with Route-A v0.2, source separation, LF/control-byte/cache, and terminal-
newline audits.

The baseline counts are:

| Active cutoff | Atoms | Pairs | Triples |
|---:|---:|---:|---:|
| 12 | 5 | 10 | 10 |
| 18 | 7 | 21 | 35 |
| 30 | 10 | 45 | 120 |

All baseline statistics are nonzero. Canonical relabelled ledgers agree
exactly, and the 12→18→30 active-cutoff restrictions preserve every old pair
and triple row.

The four finite controls have full-coherence counts:

| Source | Pairs | Triples |
|---|---:|---:|
| mutated cover promoting 6 | 3 | 0 |
| composite-only inventory | 0 | 0 |
| seeded generic DAG | 0 | 0 |
| seeded random inventory | 0 | 0 |

## First obstruction: unaffected generated intervals

Promoting 6 changes some joins, but it does not alter the generated interval
for (2,5):

\[
[1,10]=\{1,2,5,10\}\cong B_2,\qquad
\mu(1,10)=1,\qquad 10=2\cdot5.
\]

The same holds for (2,7) and (3,5). Their direct finite Gram coefficients are
nonzero. Since these pairs satisfy all five predicates, every nonempty subset
of the predicate family also retains them. The exhaustive 31-mask audit
therefore finds zero pair masks that are nonzero on the baseline and zero on
all four finite fixtures.

This gives a small theorem: any positive additive statistic supported on
generated pair intervals is blind to a source mutation disjoint from at least
one coherent interval. Calling a predicate “global” because it searches for a
join in the whole poset does not overcome support locality.

## Strong obstruction: the free-commutative clone theorem

Let \(F(X)\) be the free commutative monoid on abstract generators
\(X=\{x_p:p\in\mathbb P\}\). Define

\[
\Phi:\mathbb N_{>0}\longrightarrow F(X),\qquad
\Phi\!\left(\prod_p p^{e_p}\right)=\prod_p x_p^{e_p}.
\]

Unique factorization makes \(\Phi\) a monoid and pointed-poset isomorphism:
integer divisibility becomes coordinatewise exponent order. It preserves:

- the bottom and its covers;
- finite joins and lcm/tensor multiplication;
- Boolean intervals generated by distinct atoms;
- incidence Möbius values;
- exponent-box and finite-generator compatible cutoffs;
- the transported roof character \(\nu(x_p)=p\);
- the transported Gram kernel;
- gamma-code marker ownership.

The factorization monoid of any UFD modulo units is likewise free commutative
on its irreducibles. A polynomial-monomial control is therefore an explicit
UFD clone.

Consequently, for every invariant \(I\) natural in precisely the frozen data,

\[
I(\mathbb N_{>0},\mid,\nu,G)
=I(F(X),\mid,\nu\circ\Phi^{-1},\Phi_*G).
\]

This is not a numerical coincidence. It is an isomorphism obstruction. The
canonical ledgers at cutoffs 12, 18, and 30 are byte-for-byte equal for both
the free monoid and polynomial-UFD aliases. Ranks 2–6 and exponent caps 1–3
also retain every pair and triple, for transported as well as generic
generator weights.

Thus no source-natural statistic using only the frozen
incidence/join/Möbius/roof/Gram data can be nonzero on integer divisibility and
zero on all free-commutative/UFD controls.

## Why the triple finite success is still useful

The triple selector is not vacuous. It gives a clean zero on all four finite
non-UFD fixtures and shows that Boolean rank-three coherence can reject local
mutations and accidental joins that survive weaker filters. Twenty-eight of
the 31 predicate masks separate the baseline triples from those four fixtures.

But every such mask is copied by the transported clone. The correct
interpretation is:

- finite-fixture GO: rank-three coherence detects a strong unique-factorization
  pattern;
- arithmetic STOP: the pattern is shared by arbitrary free commutative
  factorization sources.

The mandatory clone prevents a hand-sized control suite from being mistaken
for arithmetic specificity.

## Summability and holomorphy

The filtered pair series is bounded by the unfiltered SD-C31 mixed series:

\[
\mathcal C_2(s)
=2\sum_{p<q}\chi_2(p,q)G_{pq}
\left(p^{-s}q^{s-1}+q^{-s}p^{s-1}\right).
\]

It is normally convergent on

\[
1-2\eta<\Re s<2\eta,
\]

which at \(\eta=2\) is \(-3<\Re s<4\), and it obeys
\(\mathcal C_2(1-s)=\mathcal C_2(s)\). The inherited det3 strip lies inside
this domain.

The exact rational pair tail certificate is

\[
\operatorname{tail}_{2}(N)\le\frac{5}{36N^3}.
\]

For the connected triangle, \(g_{pq}\le(pq)^{-4}\) gives

\[
\frac{2g_{pq}g_{qr}g_{pr}}{pqr}
\le2(pqr)^{-9},
\]

and the frozen rational tail bound is

\[
\operatorname{tail}_{3}(N)
\le\frac{25}{2^{24}N^8}.
\]

Both vanish with the active cutoff.

## Determinant and marker ownership

Absolute summability of the entries of \(H\) implies trace class through the
matrix-unit nuclear decomposition. Therefore the auxiliary determinant

\[
\det(I+zH)
\]

is an honest ordinary Fredholm determinant, entire in \(z\). This is a real
analytic gain. It is not the original chiral transfer determinant.

On the critical line the phase-decorated pair kernel is diagonally conjugate
at finite cutoff, so its characteristic cycles cancel the \(t\)-phase. The
auxiliary determinant therefore supplies no spectral motion. Its entire
coefficient ledger is also cloned by free commutative/UFD sources.

The original chiral \(\det_3\) remains the inherited honest determinant and
still deletes the complete quadratic trace term. Exponentiating
\(\mathcal C_2\) or \(\Theta_3\) separately creates a new declared functional;
it does not change original determinant ownership. The triangle monomial is
not claimed to equal the full \(\operatorname{Tr}B^6\).

Marker ownership is explicit:

\[
\text{pair exponent}=\ell(a)+\ell(b),
\]

\[
\text{triangle exponent}
=2(\ell(a)+\ell(b)+\ell(c)).
\]

All 165 baseline rows pass. The theorem is at \(u=1\); damping changes the
object.

## Findings in analysis form

**Observation.** Three fully coherent pairs survive the cover mutation.
**Interpretation.** Their generated intervals never meet the defect.
**Implication.** Pair-interval coherence cannot be a global source selector.
**Next step.** Reject any successor whose support can avoid a declared source
mutation.

**Observation.** Triple coherence vanishes on all four finite fixtures.
**Interpretation.** Rank-three Boolean/lcm coherence is a meaningful stronger
filter.
**Implication.** It earns a finite-fixture GO, not arithmetic specificity.
**Next step.** Keep mandatory isomorphic factorization clones in every future
control suite.

**Observation.** Free and polynomial-UFD clones reproduce every baseline
ledger.
**Interpretation.** The statistic measures free unique factorization.
**Implication.** A0 survives, but A1/A4 fail and Route A remains rejected.
**Next step.** Add a canonically derived source operation that the clone
cannot transport.

**Observation.** \(H\) owns an ordinary auxiliary Fredholm determinant, but
its phase cancels and its coefficients are cloned.
**Interpretation.** Honest analyticity is insufficient.
**Implication.** A2 can hold without A3 or A4.
**Next step.** Do not identify this auxiliary determinant with a Hilbert–Pólya
carrier.

## Route decision and Paper 31 obligation

Recommended tuple:

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL).

Overall: Route A rejected; Route B false.

Paper 31 has one minimum obligation: introduce a canonically source-derived
operation absent from the free-commutative/UFD clone and prove exact clone
separation before constructing another determinant. The most plausible
remaining datum is a coupling between integer addition and multiplicative or
archimedean size, derived uniformly from the source rather than from a prime
lookup. If no such operation can be made compatible with the symbolic
dynamics and analytic ownership, the source-incidence branch should close.

No target zero or RH claim is used anywhere in this package.
