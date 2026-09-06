# Source and ownership ledger: nonlinear geometry scout

Audit date: 2026-09-06. This is a bounded primary-source audit, not a global
priority certificate. Sources were read through available author, publisher,
institutional, or arXiv pages. No unpublished material was uploaded; no
external-model review was performed. Search-result summaries were discovery
leads, not substitutes for the theorem locations recorded below.

## 1. Decision on the retained claim

The candidate is **all integral periodic points of one Fibonacci trace map**,
across every level, with ordinary time. No exact owner of that complete
integer-lattice classification was located in this audit. This is weaker
than asserting that none exists. The author has supplied an independent
complete proof; the residual significance and ownership decision belongs to
the non-author reviewer.

Known existence of all displayed periodic curves, classical escape regions,
sign symmetries, the trace-map construction, the Markoff invariant, and
finite-cycle-to-zeta conversion are fully subtracted. The only proposed
principal contribution is the exhaustiveness argument in proof §§4–5.

### Internal same-object collision check

The existing [Fibonacci trace-map clock-obstruction project](../../fibonacci_trace_map_clock_obstruction/README.md)
and [candidate registry](../../docs/candidate_registry.md) (Fibonacci pivot
section beginning at line 1787) were read, not rerun or edited. They study
the same trace-map object up to normalization/reversal, but different
contracts: spectral-section incidence versus returns (C13), marked-band
boundary versus closed counts (C13B), bounded-polynomial short-clock degree
obstruction (C13P), zero-radius growth at fixed escape energies (C13G), and
an undefined general operator proposal (C13R). None of those registered
contracts is an all-integral periodic-point classification. Their negative
Route-A outcomes and clock boundaries remain unchanged; the new arithmetic
theorem is not a reversal of those decisions or a claimed spectral bridge.

## 2. Closest primary sources and the precise subtraction

### N1. Roberts–Baake: the map and periodic families

John A. G. Roberts and Michael Baake, *Trace maps as 3D reversible dynamical
systems with an invariant*, Journal of Statistical Physics 74 (1994), 829–888.
[Publisher and DOI metadata](https://link.springer.com/article/10.1007/BF02188581);
[author-hosted published PDF](https://web.maths.unsw.edu.au/~jagr/RB94.pdf).

Read: abstract; §§3–4, including Props. 3–6, Eq. (29), and printed pp. 849–852;
relevant later statements and conclusion; keyword searches across the PDF.
Eq. (29) owns the axis cycle; Table I and pp. 851–852 own the 4/12 families
and sign relation. Table I's image was not legible in web extraction, so no
claim of visual table transcription is made. The surrounding text is explicit.
No whole-integer exhaustiveness theorem was located there.

Normalization: their half-trace coordinates are ours divided by 2; their
invariant \(I\) satisfies \(I=K/4-1\). This scaling changes the lattice to
\((\tfrac12\mathbb Z)^3\); integer coefficients of a map must not be
confused with a theorem about all integral points.

### N2. Roberts: classical necessary and sufficient escape criteria

John A. G. Roberts, *Escaping orbits in trace maps*, Physica A 228 (1996),
295–325, DOI `10.1016/0378-4371(95)00428-9`.
[Author-hosted published PDF](https://web.maths.unsw.edu.au/~jagr/R96.pdf).

Read: introduction; Thm. 3.1; §4 propositions/theorems and their displayed
escape regions; Remarks 4.1–4.2; Cor. 4.1; Extensions 5.1–5.2 and conclusion.
Printed pp. 318–319 characterize escape by eventual entrance into particular
regions. Thm. 4.2 and Cor. 4.1 exclude periodic points in those regions;
Thm. 4.3 covers negative-invariant noncompact cones. Section 5 includes
orientation-reversing maps such as Fibonacci.

These results own general real/complex escape and growth claims. They do not
state the lattice intersection classified here. The surviving step is the
uniform arithmetic treatment of its boundary/complement: maximum neighbours,
equality at modulus 2, the single-zero obstruction, signed 4/12 alternatives,
and the unit cube. The present proof does not claim a new escape criterion.
DOI/publisher endpoints were attempted but returned tool-safety/403 errors;
the full article identity is independently present in the author PDF header.

### N3. Humphries: whole-group finite orbits, not one-map periodicity

Stephen Humphries, *Points with finite orbits for trace maps*,
[arXiv:1611.02743v1](https://arxiv.org/abs/1611.02743v1), submitted
8 November 2016; the available arXiv history has a single version.
[Versioned full PDF](https://arxiv.org/pdf/1611.02743v1);
[full HTML](https://arxiv.org/html/1611.02743v1).

Exact anchors: definitions of \(\mathcal F_2,\mathcal P_2\) at printed
pp. 1–2; Theorem 1 at printed p. 2 (PDF page 2); explanation at p. 3;
proof of Theorem 1 at p. 16; finite-orbit half-trace values at pp. 5–6.
The quantifier is a finite orbit under the entire \(\operatorname{Aut}(F_2)\)
action, equivalently periodicity under each group element. Axes are an
explicit separate case and need not come from finite matrix groups.

Our \((-1,3,-1)\) is single-map periodic, but after dividing by 2 has
invariant level 2 and is non-axis, excluded by the source's whole-group
classification. Thus this source cannot prove the candidate by substituting
the single-map hypothesis. Any 2026 date appearing on dynamically generated
HTML is not a new submission or a publication date.

### N4. Ghosh–Sarnak: all integral points modulo the Markoff group

Amit Ghosh and Peter Sarnak, *Integral points on Markoff type cubic surfaces*,
[arXiv:1706.06712v3](https://arxiv.org/abs/1706.06712v3), final arXiv version
30 May 2022; Inventiones Mathematicae, DOI `10.1007/s00222-022-01114-z`.
[Full text](https://arxiv.org/html/1706.06712v3).

Read: abstract, the introduction's descent/fundamental-set discussion, and
full-text searches for periodic/Fibonacci. The central arithmetic objects are
integral points, local obstructions, and group-orbit representatives. A finite
number of group orbits does not mean that those orbits are finite; it does not
classify cycles of the specific word \(T\). The paper's arithmetic context is
subtracted, not used as a new source-orbit construction here.

### N5. Vishkautsan: the two-reflection map and residual periodicity

Solomon Vishkautsan, *Residual periodicity on the Markoff Surface*,
Rendiconti Lincei 27 (2016), 25–35, DOI `10.4171/RLM/720`.
[Publisher metadata](https://ems.press/journals/rlm/articles/13708);
[full preprint v2](https://arxiv.org/pdf/1504.07099v2).

Read: abstract and introduction, §§1.1–1.2. The map is a composition of two
coordinate reflections on the zero Markoff surface; periodic conics explain
residual periodicity. This differs in map, domain, and local/global question.
The introduction also credits earlier nonexistence of nonzero real periodic
points on the zero level; the candidate's \(k=0\) specialization is therefore
not proposed as a new result in isolation.

## 3. Remaining landscape sources actually inspected

The broader screen read abstract/introduction-level evidence from the following
additional primary items. These are not claimed to provide missing proofs.

| ID | Primary source and reading scope | What it changes in the screen |
|---|---|---|
| L1 | Gasull–Mañosa–Xarles, *Rational periodic sequences for the Lyness recurrence*, DCDS 32 (2012), 587–604; [publisher](https://www.aimsciences.org/article/doi/10.3934/dcds.2012.32.587), [full preprint](https://arxiv.org/pdf/1004.5511); abstract, introduction and Thm. 1 | Owns the full rational prime-period list \(1,2,3,5,6,7,8,9,10,12\). “Prime period” there means least period, not prime number. Candidate rejected. |
| L2 | Patrick Ingram, *Canonical heights for Henon maps*; [arXiv:1111.3609](https://arxiv.org/abs/1111.3609), related DOI `10.1112/plms/pdt026`; abstract and metadata | A rational-period conjecture for the orientation-reversing quadratic family remains a conjecture in this source; bounded numerical tests are not a proof of arbitrary rational parameters. |
| L3 | *Hénon maps: a list of open problems*; [journal-hosted full text](https://armj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html), arithmetic section, Conjectures 3–4 | Confirms the difficulty and exact parameter/sign conventions of neighbouring rational uniformity questions. Does not justify transferring the sealed integral-parameter result. |
| L4 | H. Kim, H. Krieger, M.-I. Postolache, V. Szeto, *Hénon maps with many rational periodic points*; [arXiv:2412.01668v2](https://arxiv.org/html/2412.01668v2), version date 8 July 2025; abstract, introduction, theorem setting | High-degree constructions already provide many integral points and long cycles. A cubic scout must not claim that small observed periods extend to all degrees. |
| L5 | Cima–Gasull–Mañosa, *Global periodicity conditions for maps and recurrences via Normal Forms*; [arXiv:1205.0923](https://arxiv.org/abs/1205.0923), abstract | Global finite order of an entire rational map is a different quantifier from classifying its rational periodic points. Renaming a known globally periodic recurrence is not a new contract. |
| L6 | Fuchs–Litman–Silverman–Tran, *Orbits on K3 Surfaces of Markoff Type*; [arXiv:2201.12588](https://arxiv.org/abs/2201.12588), [author-hosted full paper](https://www.math.ucdavis.edu/~efuchs/K3Markoff1.pdf); abstract and introductory related-work discussion | The tri-involutive K3 group-orbit problem and finite-field connectivity have real prior ownership, but are not the single affine cubic map being proved here. No K3 claim retained. |
| L7 | Gaétan Leclerc, *Fourier decay of equilibrium states and the Fibonacci Hamiltonian*; [arXiv:2507.23731](https://arxiv.org/abs/2507.23731), abstract and metadata | Recent trace-map research concerns equilibrium/density-of-states measures; it is not an integral-cycle theorem and supplies no Hilbert–Pólya bridge. |

This is twelve primary landscape items in total. Read depth is intentionally
different: near-owner statements were inspected in full context; rejected
or peripheral questions received abstract/introduction screening. The ledger
does not claim twelve papers were each read from first to last page.

## 4. Query record and negative-evidence boundary

Representative actually executed formulations, including synonym and
normalization changes:

```text
Lyness recurrence rational periodic points periods 7 9 10 12 Cima Gasull Mañosa
cubic Henon map integer periodic points x y y cubic a y rational classification
rational Henon map periodic points rational parameters denominator uniform bounds
Markoff surface integral periodic points automorphism three involutions
Markoff trace map integer periodic points Fibonacci recurrence
"trace map" "integer" "periodic points"
"Fibonacci trace map" "rational" "periodic"
"trace maps" "rational points" periodic
"Fibonacci trace map" "integral"
"Fibonacci trace map" "integer" cycles
"trace map" "period" "12" "integer"
"Fibonacci trace map" "integer points"
"Markoff" "periodic integral"
"trace map" "periodic" "lattice" classification
"Fibonacci trace map" "integer" "periodic points" 2024 2025 2026
"trace map" "integral periodic points"
"Fibonacci" "trace" "periods" "integers"
"Fibonacci trace map" "periodic" "rational points"
"Fibonacci trace map" "integer" -lattice -matrix -matrices -Hamiltonian -quasicrystal
"x_{n+3}=x_{n+2}x_{n+1}-x_n"
"Markoff" "integral" "12" "periodic points"
"Markoff" "periodic" "square"
"Markoff" "m^2-m+2"
"Fibonacci trace map" "zeta" "integral"
"Fibonacci trace map" "periodic" "integer" [recency filter: 183 days]
```

The exact-coordinate and arithmetic-support searches did not locate an exact
whole-lattice owner. Some searches returned unrelated or secondary pages;
these are not cited as mathematical support. A recency-filter result can
still be an old article crawled recently, so dates above come from version
history or publisher metadata, not relative “published/crawled” snippets.

The date-bounded and formula-specific searches do **not** exclude unpublished
work, unindexed books, exercise literature, alternative terminology, or a
short corollary known informally. The candidate must be rejected if a direct
earlier exhaustiveness theorem is found. It must also be rejected if the
reviewer judges the residual arithmetic completion insufficiently substantive,
even when no exact title match is found.

## 5. Source-integrity disposition

All mathematical attributions used in the retained contract have a retrieved
primary full-text witness. RB94 publication/DOI metadata and Vishkautsan
metadata were checked on publisher pages. Humphries is labelled by its actual
arXiv version, with no invented journal venue. R96 full text is available,
but its publisher endpoint was blocked; that limitation is recorded above.
No fabricated source, placeholder citation, external peer-review label, or
numeric novelty score is used.

Author-side source decision: `NO_EXACT_WHOLE_INTEGER_OWNER_LOCATED_IN_BOUNDED_AUDIT`.
This is ready for independent adjudication, not a declaration of global
novelty. The complete mathematics, all query failures, known antecedents, and
scope counterexamples remain separate from that decision.
