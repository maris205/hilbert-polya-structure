# R8 X2 — bounded-multiplier source audit

## Disposition and unchanged interface

**No applicable classification theorem was obtained in this bounded source
audit.** In particular, this report does not exclude the critical-two-cycle
residual, prove its cofinite product condition, close MS6, or create a contract.
Failure to locate a source is not a theorem that no such source exists.

The input is the frozen R7 A1 report
[`a1_balanced_divisor_detection/REPORT.md`](../../continuation_round7/a1_balanced_divisor_detection/REPORT.md),
379 lines, SHA-256
`59f79d718d85e0c2b4bbaea2e8d78416b5cb48e52927fe044605fb5847bc6e8f`.
Its entire proof was read; the critical residual was reread and its full hash
checked before writing this report. The input is not a new X2 result.

Keep exactly

\[
k=\overline{\mathbb F}_p,\quad p\text{ odd},\qquad
f(x)=x^2-1,\quad g(x)=\frac{x-1}{x+1}.
\]

For a primitive ordinary cycle \(O\) of native length \(n\), disjoint from
\(\{0,1,-1\}\), write \(A_O=\prod_{x\in O}x\). The owned identities are

\[
\prod_{x\in O}g(x)=A_O^{-3},\qquad
\lambda_O=(f^n)'(x)=2^n A_O\ne0.
\]

Consequently the cofinite cycle-product hypothesis gives

\[
\forall\text{ but finitely many }O:\qquad
A_O^3=1,\qquad \lambda_O^{3(p-1)}=1. \tag{BM}
\]

The latter condition is only a necessary consequence, not asserted equivalent
to the product hypothesis. For \(p=3\), its geometric roots have order dividing
two, while the stronger owned product identity gives \(A_O=1\).

The target source must concern a **single** positive-characteristic map and a
fixed finite set of its noncritical native-cycle multipliers, with no dependence
of that set on the native period. A family having a fixed spectrum at each
period, membership in \(\overline{\mathbb F}_p\), and bounded spectra of a fixed
period are different statements.

## Quantifier controls — elementary checks

For nonzero elements of \(k\), the following are equivalent after the same
finite set of exceptional cycles is removed:

1. all remaining multipliers belong to one finite set;
2. one positive integer \(M\), prime to \(p\), satisfies \(\lambda_O^M=1\)
   for all remaining cycles;
3. one finite field \(\mathbb F_{p^r}\) contains all remaining multipliers.

Indeed, take the least common multiple of the orders in a finite set; conversely,
\(X^M-1\) has finitely many roots. Every finite subset of \(k\) lies in one
finite extension, and \(\mathbb F_{p^r}^{\times}\) has order \(p^r-1\).
The finite exceptional multipliers can also be absorbed into a larger \(M\)
or \(r\), without preserving the particular exponent in (BM). This absorption
does not provide a classification theorem.

By contrast, a separate root-of-unity order for each multiplier is automatic
for every map over \(k\). Tensoring their multiplicative group with
\(\mathbb Q\) gives zero, regardless of whether their orders are uniformly
bounded. Thus a positive-characteristic substitute for a characteristic-zero
rank theorem would need genuinely different information.

Here is an in-degree positive control. For \(h(x)=x^2\) over every odd
characteristic, a nonzero point of exact period \(n\) satisfies

\[
a^{2^n-1}=1,\qquad (h^n)'(a)=2^n a^{2^n-1}=2^n
\in\mathbb F_p^{\times}.
\]

So one finite set contains every noncritical multiplier. This defeats a generic
impossibility assertion, not an exceptional-map classification, and is not a
counterexample involving the target \(x^2-1\).

There is also a symmetric-function trap. Frobenius permutes the geometric
primitive cycles of any \(f\in\mathbb F_p[x]\) at each fixed period and sends
their multipliers to their \(p\)-th powers. Therefore the corresponding
cycle-multiplier polynomial has coefficients in \(\mathbb F_p\).
That fact alone does not put every individual multiplier, over all periods,
in one finite field. Abstractly, the polynomials \(X^{p^r}-X\) all have
coefficients in \(\mathbb F_p\), while the union of their root sets is infinite.
This last family is a logical control, not a claim about dynatomic factors.

## Closest complex source: Huguin

Valentin Huguin,
[*Rational maps with rational multipliers*](https://jep.centre-mersenne.org/item/10.5802/jep.227.pdf),
J. Éc. polytech. Math. 10 (2023), 591–599;
also [arXiv:2210.17521v1](https://arxiv.org/pdf/2210.17521v1).

The main theorem, numbered Theorem 7 in that arXiv version, concerns a rational
map over \(\mathbb C\): if all periodic multipliers lie in one number field,
the map is a power, Chebyshev, or Lattès map. The proof reduces the field of
definition using multiplier-spectrum rigidity, then uses Galois-orbit
equidistribution and a complex Lyapunov-exponent characterization. The periodic
approximation lemma uses inverse branches and the Poincaré metric.

Reading record: published introduction and the approximation lemma with its
proof; arXiv Theorem 7 and its complete proof, printed pp. 6–7, through the final
Lyapunov contradiction. The publisher's later-page request timed out, so the
arXiv primary version supplied that last passage; numbering is not conflated.

This is not a theorem over \(k\). There is no field embedding of \(k\) in a
number field or \(\mathbb C\). No argument here transfers the algebraic
multiplier identities to characteristic zero.

## Newer closest source: Ji–Xie–Zhang

Zhuchao Ji, Junyi Xie, Geng-Rui Zhang,
[*Space spanned by characteristic exponents*, arXiv:2308.00289v3](https://arxiv.org/pdf/2308.00289v3),
25 March 2026.

Theorem 1.5 concerns \(f:\mathbb P^1(\mathbb C)\to\mathbb P^1(\mathbb C)\).
If one number field \(K\) contains a positive, point-dependent power of each
complex multiplier length \(|\rho_f(z)|\), then \(f\) is exceptional.
Remark 1.6 explicitly allows finitely many exceptional periodic points.
Thus finite exceptions are not the missing hypothesis in this source.

Reading record: Definitions 1.1, Theorems 1.4–1.5, Remarks 1.3 and 1.6,
Corollary 1.7, introduction proof sketch, and the complete proof of Theorem 1.5
in §4, printed pp. 22–25. That proof uses \(f\times\overline f\), a complex
Lyapunov gap, number-field Galois orbit measures and arithmetic
equidistribution. Theorem 1.4's multiplicative-rank consequence does not replace
the absent positive-characteristic bounded-order argument.

The domain \(\mathbb C\), complex length and number-field hypotheses are
essential unchecked interfaces for this task. A multiplicative lift of residue
elements supplies no preservation of addition, iteration and derivatives;
there is no proved lift of the required full spectrum here.

## Positive-characteristic source: Benedetto–Ingram–Jones–Levy

Robert Benedetto, Patrick Ingram, Rafe Jones, Alon Levy,
[*Attracting cycles in p-adic dynamics and height bounds for post-critically
finite maps*, arXiv:1201.1605v4](https://arxiv.org/pdf/1201.1605v4).

Theorem 1.5 is a non-archimedean attracting-cycle theorem when residue
characteristic is zero or exceeds the map's degree. Corollary 1.7 puts
PCF-map multipliers over a suitable function field in the algebraic closure of
the prime field. Corollary 6.3 makes quadratic PCF maps over global function
fields of odd characteristic isotrivial. Remark 6.2 concerns the symmetric
functions of the spectra in a fixed finite constant extension, not a uniform
finite set of the individual multipliers.

Reading record: exact Theorems 1.2 and 1.5, Corollaries 1.7 and 6.3,
Remark 6.2, and §6's Lemma 6.1 and complete displayed proofs of Theorem 1.5
and both corollaries, printed pp. 17–19. The constant-multiplier proof obtains
an attracting place from a nonconstant multiplier; the quadratic conclusion
uses the fixed-point multiplier coordinates on moduli.

For the target, \(0\leftrightarrow-1\) and \(\infty\) is fixed, so \(f\) is
already PCF and defined over \(\mathbb F_p\). Base change to \(\mathbb F_p(t)\)
does not improve this: isotriviality and algebraic-constant multipliers are
already true. Every absolute value on \(k\) is trivial, since each nonzero
element has finite order. Adjoining a valued transcendental variable does not
make these constant multipliers attracting. No classification from (BM) follows.

## Search and scope record

The research-lit and novelty-check workflow was used for a bounded primary
source comparison, and proof-writer for the quantifier controls. Repository
instructions and the batch workflow preserve this as an auxiliary bridge audit.
Their external-review defaults were not invoked: the explicit current task
forbids new agents and external model/API uploads.

Exactly two new search batches were used, four targeted queries each. Batch 1
tested finite multiplier sets, periodic multipliers over finite fields, bounded
multipliers in characteristic \(p\), and finite multiplier spectra. Batch 2
tested bounded order, quadratic finite-field classification, characteristic-\(p\)
Chebyshev exceptions, and recent Huguin/Ji/Xie multiplier work. Subsequent calls
only opened or located passages in identified primary sources. No third search
was performed, and no private manuscript text was submitted as a query.

Levy's arXiv:1304.2834 is an already-subtracted input, not a new find. This
report does not relabel its isospectral-family theorems as a single-map
bounded-spectrum classification, or reintroduce its excluded
\(\overline{\mathbb F}_p\)-spectrum case. The prior Bridy conjectural route is
not treated as a proved theorem. Unrelated search hits were not promoted.

The exact outstanding implication needed by this route is either a verified
positive-characteristic classification whose hypotheses cover (BM) and whose
conclusion excludes the actual map, or a direct proof that, for every odd
\(p\), infinitely many target cycles have
\(\lambda_O^{3(p-1)}\ne1\). The latter would suffice for infinitely many bad
products but is stronger than the original residual obligation; its failure
would not establish the product hypothesis.

No such implication was proved or imported here. The hand-proof lane retains
the sharper residual question \(A_O^3\ne1\) on infinitely many cycles.
No assertion of global literature completeness, priority, novelty, or full
MS6 impossibility is made.

Only this assigned new report was written. Mathematical programs, parameter
censuses, new agents, external model/API use, Git operations, configuration
changes, old/shared-file modifications, manuscript and PDF actions: zero.
