# AS3-H independent mathematical, source, and materiality review

2026-09-08 UTC. Internal current-team nonauthor review, not an external
peer review, a formal Route-A evaluation, or a contract admission.

## Decision

**Mathematics: approved as stated for the complete frozen question.**
The all-iterate fixed-set classification and all four local count formulas
are proved. No required mathematical correction or counterexample was
found. There is no remaining index-five, dyadic, or all-iterate exhaustion
gap to preserve artificially.

**Local increment: real, but accurately delimited.** C156's completed
Smith/denominator/primary-decomposition theorem was not incomplete.
AS3-H closes the stronger exact-evaluation question that C161 explicitly
abandoned before changing models. The actual norm-coordinate bridge was
not supplied by the final C156 or C161 texts read in this review.

**Independent-paper materiality: not recommended as a new batch slot.**
The result is a useful complete addendum to the existing C146/C151/C156
Heisenberg chain. After deducting that chain and standard norm-congruence
arithmetic, the new content is a compact coordinate/lattice/parity bridge
for the same single automorphism and observable. The full answer is worth
retaining, but this package does not establish the independent substance
required for another paper in this batch. This is a materiality judgment,
not a mathematical rejection or a claim that an external source already
contains the exact answer.

Only the coordinator may make the final admission decision.

## 1. Frozen object and review record

The reviewer first read the current R3 plan, the complete
[frozen question](../arithmetic_spectral/FROZEN_QUESTION.md), and all
263 lines of the [author proof](../arithmetic_spectral/PROOF_PACKAGE.md).
The completed [source audit](../arithmetic_spectral/SOURCE_AUDIT.md) and
[scout report](../arithmetic_spectral/SCOUT_REPORT.md) were then read in full.
The proof hash was independently checked as

```
3ddcb662101fee7a1304c5c2c1f795afa3f33ffe21e2dd3bba943cf88b54e332
```

The object is the left quotient of the real Heisenberg group

$$
(x,y,z)(X,Y,Z)=(x+X,y+Y,z+Z+xY)
$$

by its integer lattice, with

$$
\Phi(v,z)=(Av,z+q(v)),\qquad
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
q(x,y)=x(x-1)+xy+\frac{y(y-1)}2.
$$

The quantified claim covers every integer iterate $n\geq1$ and every
point of this compact quotient. Its observable is the complete fixed set,
or equivalently the number of its central-circle components. It is not
an isolated-point count, a Nielsen number, a count after perturbation,
or a trace. This object and clock are unchanged in the proof.

The review used `research-review` and `proof-writer` checking, with the
batch's current-team replacement for legacy model examples. ARS-Codex
remained confined to source fact-checking. No empirical pilot or formal
evaluation was inferred from those skills. Their effect here was to
separate proof correctness, source applicability, and paper materiality.

## 2. Independent proof audit

### 2.1 The lift and the true lattice action

The coordinate $t=z-xy/2+(x+y)/2$ is exactly invariant under the lifted
$\Phi$: the change in $z-xy/2$ is $-x-y/2$, and the added linear term
changes by $x+y/2$. Left multiplication by $(m_1,m_2,k)$ changes $t$ by

$$
k+\frac{m_1y-xm_2-m_1m_2+m_1+m_2}{2}.
$$

Consequently, if $M=A^n-I$ and $m=Mv\in\mathbb Z^2$, the fixed-point
condition is precisely

$$
\rho_n(m)=\frac{\det(v,m)+m_1m_2-m_1-m_2}{2}\in\mathbb Z.
$$

The sign and the left-quotient convention agree with C151's actual
$q_n(v)-m_1v_2$. The action was not replaced by a product-torus action.
Its central-coordinate independence means an entire fibre is fixed or
none of it is. The nonzero horizontal determinant makes these finitely
many fibres isolated from one another horizontally, and the derivative
kernel at a fixed point is exactly their central tangent. Thus the
components really are clean circles.

### 2.2 Cofactors and uniform divisibility

The displayed factorization $M=gU$, with $g=L_n$ for odd $n$ and $g=F_n$
for even $n$, agrees with the full C156 theorem. For
$U=\left(\begin{smallmatrix}r&s\\s&t\end{smallmatrix}\right)$, the
recurrence gives $r-t=s$, and direct coefficient comparison gives
$Q(Uw)=(\det U)Q(w)$ for $Q(x,y)=x^2-xy-y^2$.
The determinants are $-1$ and $-5$ as claimed.

The common-odd-prime exclusion follows from
$L_n^2-5F_n^2=4(-1)^n$. The dyadic assertions are justified for every
$n$, not by extrapolating samples: $Q_0^{12}\equiv I\pmod8$ gives the
needed recurrence period, and the residues at $n=0,3,6,9$ give exactly
the cases stated. In particular, if $g$ is even then $4\mid g$,
$s=2u$ with $u$ odd, and $(u,g)=1$.

### 2.3 The even-iterate index-five selection

The inverse-matrix calculation yields

$$
\det(M^{-1}m,m)=\frac{sQ(m)}{g\det U}.
$$

For even $n$, integrality of $\rho_n(m)$ forces $5\mid sQ(m)$.
Since $s=L_n$ is a unit modulo $5$, this gives $Q(m)\equiv0\pmod5$.
The latter is the single line $m_1+2m_2=0$ over $\mathbb F_5$.
The lattice $U\mathbb Z^2$ lies over this line by the norm identity,
and both it and the full inverse image of the line have index five.
They are therefore equal.

This proves the needed inclusion for every zero-rotation class, even
when $5\mid g$. It does not falsely identify all $5g^2$ horizontal
classes with a square module. Once $m=Uw$, quotienting by
$M\mathbb Z^2=gU\mathbb Z^2$ is exactly quotienting $w$ by
$g\mathbb Z^2$, with no extra factor five. The base point is $w/g$.
The odd case follows immediately from unimodularity of $U$.

### 2.4 Affine parity: an independent compact check

The author's two-way dyadic argument is correct. The following additional
hand check makes its full scope particularly transparent. Since
$P(a,b)=ab-a-b\equiv Q(a,b)\pmod2$ and $\det U$ is odd,

$$
\rho_n(Uw)\equiv\frac{sQ(w)}{2g}+\frac{Q(w)}2
=\frac{a_nQ(w)}g\pmod1,
\qquad a_n=\frac{s+g}{2}.\tag{R1}
$$

Here $a_n$ is an integer because $s,g$ have the same parity. If $g$ is
odd, $(a_n,g)=1$ follows from $(s,g)=1$. If $g$ is even, write
$a_n=u+g/2$; it is odd, and no odd prime divisor of $g$ divides it
because $(u,g)=1$. Thus $(a_n,g)=1$ in every case, including $g=1$.
Equation (R1) proves

$$
\rho_n(Uw)=0\quad\Longleftrightarrow\quad Q(w)=0\pmod g.
$$

This is an optional simplification, not a required repair. In particular,
there is no concealed division by two in an even residue ring.

### 2.5 All local counts, including repeated prime powers

For $p=2$ and the odd inert primes, anisotropy modulo $p$ shows that
$v_p(Q(x,y))=2\min(v_p(x),v_p(y))$ whenever the divided vector is
nonzero modulo $p$. The zero vector and coordinates divisible by the
whole modulus are included by the same divisibility criterion. This
gives $p^{2\lfloor e/2\rfloor}$.

For odd split primes distinct from five, the two distinct roots of
$T^2-T-1$ lift digit by digit; the resulting invertible linear change
turns $Q$ into a product. Counting valuations $j=0,\ldots,e-1$, plus
the zero first coordinate, gives
$p^e+e(p^e-p^{e-1})$. No primitive-vector restriction was introduced.

For $p=5$, the invertible change $(a,b)=(2x-y,y)$ gives
$4Q=a^2-5b^2$. The two valuations have different parity, so divisibility
by $5^e$ requires $5^{\lceil e/2\rceil}\mid a$ and
$5^{\lfloor e/2\rfloor}\mid b$, giving $5^e$ pairs. This includes
every ramified exponent. CRT supplies the complete product over $g$.

These are standard local norm counts, and the proof correctly presents
them as such. Their validity is not contingent on an unchecked Weil
representation or nondegenerate finite-quadratic-module hypothesis.

### 2.6 Least periods and what is being counted

Every point of a fixed fibre has the same return times because the
return rotation is independent of its central coordinate. The divisor
subtraction and Möbius formula therefore count circle fibres with
pointwise least period $n$. They do not count isolated primitive orbits.
The text appropriately does not divide the fibre count by $n$ and call
the result an orbit count. No further return-time assumption is missing.

## 3. Required corrections, counterexamples, and optional changes

- Required mathematical corrections: **none found**.
- Counterexamples to the frozen theorem: **none found**.
- Required source corrections to justify the actual proof: **none found**;
  the new derivation does not invoke an unverified external theorem.
- Optional exposition: (R1) can replace part of the longer parity
  discussion if a future authorized revision is made. It need not be
  inserted into the frozen author proof to close this review.
- Scope wording to preserve: call this a solution of the stronger
  Heisenberg continuation left open at the C161 pivot, not completion
  of an allegedly unfinished C156 structural theorem.

The author proof was not edited. One frozen-snapshot review was conducted;
no second review round or author correction cycle is invented when no
required correction was identified.

## 4. Local ownership independently checked

The reviewer read the complete theorem packages for
[C146](../../../henon_heisenberg_nilmanifold_clean_fixed_sets_route_a/THEOREM_PACKAGE.md),
[C151](../../../henon_heisenberg_character_resolved_fibre_route_a/THEOREM_PACKAGE.md),
[C156](../../../henon_heisenberg_primary_quadratic_module_route_a/THEOREM_PACKAGE.md),
and [C161](../../../henon_finite_cyclic_quadratic_birkhoff_route_a/THEOREM_PACKAGE.md).
The complete C156/C161 final `paper/main.tex`, source audits and improvement
logs were also read, together with their research questions and C161's
narrative. This is actual mathematical-body comparison, not a favorable
summary adopted from the author.

| Prior ownership | Deduction from AS3-H's increment |
| --- | --- |
| C146 | The map/lattice, central clean geometry, singular stability and toral count are already owned. |
| C151 | The actual affine rotation, representative invariance, exact zero criterion and finite projector are already owned. |
| C156 | Both all-n Smith types, exponent denominator and primary zero-product framework are already proved. Final equation (8) leaves the local sums unevaluated, and the subsequent table is finite. |
| C161 | The source audit expressly records failure of the Heisenberg quotient/affine/2-/5-primary step. The final theorem is the different odd cyclic Birkhoff model; it contains no replacement proof of the Heisenberg formula. |
| Standard arithmetic | Norm anisotropy, split-product counting, the ramified valuation calculation, CRT and Möbius inversion are not new general results. |

What remains new relative to these actual texts is the all-n realization
of the zero-rotation locus by $Q(w)=0\pmod{g_n}$, through the invariant
central coordinate, forced index-five lattice, and parity unit. This is
genuine mathematical progress and resolves a real earlier missing step.

## 5. Independent primary-source checks and their limits

### Finite quadratic modules

The reviewer independently accessed Strömberg's
[arXiv:1108.0202v1 HTML](https://arxiv.org/html/1108.0202v1) and version
record, dated 31 July 2011. Actual reads include the definition and main
statement in Section 1.2, Section 2's opening/Jordan description and
Lemma 2.1, and the displayed Section 3 local-Gauss statements. A complete
25-page proof audit is not claimed.

The definition requires a homogeneous quadratic form and nondegenerate
polarization. It owns a general evaluation framework, not the identification
of this actual nilmanifold rotation with the stated norm congruence.
AS3-H does not import those hypotheses or claim a new general Gauss theory.

### Nielsen/Reidemeister counts are not these fixed circles

The reviewer read Sections 1--2 and Section 4's opening/4.1 in
[Dekimpe--Tertooy--Vargas, arXiv:1710.09662v3](https://arxiv.org/html/1710.09662v3).
The [version record](https://arxiv.org/abs/1710.09662v3) dates v3 to
21 October 2021 and records the 2020 journal article. An initial v2 read
was followed by the v3 check; the rendered body date was not substituted
for the version history.

Proposition 2.2 gives actual fixed-point cardinality only with nonzero
Nielsen number. The same section's determinant formula makes that number
zero for the present map because its central eigenvalue is one; Section
4's finite-Reidemeister restriction also excludes it. Thus this is not a
missing general theorem that automatically evaluates the present circles.
That application check is the reviewer's inference from the stated
hypotheses, not a statement that Nielsen theory is invalid.

### Density and perturbation sources

The reviewer also accessed the primary
[Ha--Kim--Lee 2010 article](https://link.springer.com/article/10.1155/2010/721736):
metadata, abstract, introduction, and displayed density conclusions
including Corollaries 3.9/3.11 and Theorem 4.2. Many formulas render as
images; no full technical-proof read is claimed. Those conclusions do
not give a fixed-iterate component count.

Yi Shi's 2014
[Numdam record](https://www.numdam.org/item/CRMATH_2014__352_9_743_0/)
was read for metadata and abstract: it concerns perturbations and
holonomy for the relevant Heisenberg object class. This reviewer's PDF
body requests timed out after an initial page-count response, so no own
full-PDF read is claimed. A separate read-only spot checker reported
reading the published Sections 1--3, with the same perturbation/holonomy
scope. That supplemental access is not silently counted as this reviewer's
own read or used as a mathematical dependency.

The spot checker also independently checked the accepted DTV manuscript;
its report was followed by this reviewer's own v3 statement checks above.
The task identity was
`/root/scout_henon_arithmetic/round5_doc_links/as3h_source_spotcheck`.
It did not inspect the new author formula, edit files, or make an admission
judgment. No second independent mathematical review is claimed from it.

A Wiley search lead at DOI `10.1002/cpa.70059` did not yield a reliable
requested body passage; no conclusion from it was imported. No local PDF
was saved or new local page anchor used. No full-bibliography, retraction,
COI, indexing or worldwide-novelty certificate is asserted.

### Exact reviewer search ledger

The reviewer submitted eight new search strings, in two four-query calls,
without recency or domain filters. Direct version opens and source finds
are not counted as queries; the spot checker's searches are separate.

1. `"Heisenberg" "automorphism" "fixed" "quadratic form"`
2. `"nilmanifold" "fixed point components" automorphism formula`
3. `"Heisenberg" "Fibonacci" "periodic"`
4. `"nilmanifold automorphisms" "fixed point sets"`
5. `nilmanifold automorphism non isolated fixed point sets connected components Heisenberg`
6. `Heisenberg nilmanifold periodic points quadratic congruence count`
7. `"fixed point classes" "nilmanifold" "automorphism"`
8. `"Heisenberg" "fixed circles"`

These bounded searches did not provide an accessed external statement of
the exact AS3-H answer. Source absence is not the reason for the mathematical
approval or evidence of worldwide novelty.

## 6. Independent materiality assessment

The complete all-n theorem must not be demoted to a finite table or called
unproved: the coordinate and local arguments really quantify over all
iterates, and the exceptional prime cases are closed. Its exact locus
also improves on knowing only the old component counts.

Nevertheless, after the ownership subtraction, its role is an exact
completion of the same fixed-map calculation already occupying several
local packages. The added bridge has content, but the evaluated formula
and least-period statement then follow by standard short deductions.
There is no independently developed new map family, return/trace
mechanism, analytic continuation result or other second structural
conclusion in the frozen package. None is required for the theorem's
correctness; their absence matters only to the batch's independent-paper
threshold.

Accordingly, the recommendation is **retain as a mathematically closed
Heisenberg addendum; do not count it as an additional independently
substantial paper contract in the current five-paper batch**. This is
not a blanket claim that a short theorem can never merit publication.
It is the judgment on this exact package after its nearest local owners
and routine arithmetic consequences are deducted.

Expanding tables, factor lists, exposition length or software checks
would not change this materiality assessment. No speculative extension
or changed parameter family is proposed or authorized by this review.

## 7. Execution and final disposition

Reviewer mathematical program executions: **0**. The proof was checked
algebraically; no finite diagnostic was needed or run. The author's four
inherited sentinels were not rerun and were not treated as an infinite
proof. Shell work was limited to scoped reading, path discovery, line
counts and the frozen hash. Only this review file was written.

No author proof, old payload, current-state file, Git state, manuscript,
PDF, release manifest or formal evaluation was changed. No external
model/API upload, human-read mark, target Euler data, root-number claim,
ordinary trace determinant or Hilbert--Pólya conclusion was introduced.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.

Final separation: **complete mathematics; genuine local increment;
no required correction; addendum-level materiality; coordinator admission
gate remains separate.**
