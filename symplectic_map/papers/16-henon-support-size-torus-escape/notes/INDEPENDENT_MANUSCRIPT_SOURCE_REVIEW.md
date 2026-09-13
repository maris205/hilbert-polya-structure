# Independent Manuscript Source Review

## Status, independence, and review boundary

This is the fresh formal source-level compatibility re-review of the anonymous
Paper16 manuscript, **Support Size and Finite-Rank Torus Escape for Generalized
Hénon Maps**. I authored neither public source, the bounded compatibility
repair, nor the stale review that previously occupied this path. I began only
after the explicit `AUTHOR COMPATIBILITY STOP` and the stable identities stated
below.

The earlier review was bound to a superseded `main.tex` and therefore had no
positive effect after the compatibility repair. I read that stale review only
as required provenance, independently read all twenty non-review inputs to
EOF, reread both public sources line by line, and reconstructed the superseded
source byte for byte. This replacement report is my sole project write.

The review was source-only. I performed no compilation, PDF build, network
access, computer algebra, scientific computation, rasterization, experiment,
scan, parameter search, asset generation, or external communication. The
`research-review`, `proof-writer`, and `paper-writing` skills, together with the
shared writing principles, were used only as evidence, rigor, structure, and
prose checklists. Read-only hashing, counting, parsing, and source comparison
were not used as theorem evidence.

## Exact input and inventory gate

Immediately before this replacement, the project contained exactly twenty-one
regular files, exactly four real directories (`experiments`, `notes`, `paper`,
and `refine-logs`), zero symbolic links, and zero other entry types. The twenty
non-review files were exactly the frozen eighteen publication-stage inputs plus
`paper/main.tex` and `paper/references.bib`. The twenty-first file was the stale
review at this same path. Replacing it preserves the exact 21-file universe and
creates no new path.

All eighteen frozen inputs retained their locked SHA-256, byte, and LF-line
identities. In particular, the publication scope, publication lock,
publication-stage review, source lock, source-lock review, paper plan, and
paper-plan review remained byte-identical to their passed versions. Every
later build, PDF, manuscript-round, revision, finalization, release, and
submission path remained absent.

The two public sources matched the compatibility stop exactly:

| Source | SHA-256 | Bytes | LF lines |
|---|---|---:|---:|
| `paper/main.tex` | `2bd2dc0f3ddc2d9e75b48aef06b71bede5ecc5840ab1af7b0363a5c6c3f821d9` | 80,488 | 1,138 |
| `paper/references.bib` | `62e331e87056376d35a2181405cdd90bd1d8a9f5bc82f9334d40b9fbe2505b0f` | 2,019 | 64 |

Both decode strictly as UTF-8 and contain neither a BOM nor a carriage return.
`main.tex` has exactly one terminal LF. The bibliography is byte-identical to
the previously passed source, including its terminal whitespace.

## Byte-exact compatibility reconstruction

The complete source diff is exact and bounded. In a read-only stream I:

1. removed the sole `\allowbreak ` inserted in the inline scalar sequence at
   current line 271;
2. unwrapped every `\texorpdfstring{<TeX>}{<PDF>}` in the six repaired heading
   lines, retaining each TeX argument; and
3. restored the one terminal LF removed from the former double-LF ending.

The reconstructed stream has exactly 80,295 bytes and 1,139 LF lines and
SHA-256

`43963252424fb269cf82c68ce73a5a6300e555d555b432c1b595fc3255c09d67`.

This is the exact source identity bound by the stale review. The reverse
substitutions all occur at their intended sites and nowhere else, proving that
the repair introduced no additional drift. The byte arithmetic also closes:
the `\allowbreak ` insertion adds 12 bytes, the eight PDF-string wrappers add
182 bytes in total, and removal of one final LF subtracts one byte, for the
observed net increase of 193 bytes.

The precise heading count is six heading lines, eight mathematical spans, and
eight `\texorpdfstring` commands:

- Section 5, “Two-transition finiteness for support \(s\geq2\)”;
- Section 5.2, “The rank-\(3r\) nondegenerate locus”;
- Section 7.3, “Derivation of the \(A/B/C\) labels”;
- Section 7.5, “The \(BA\) continuation”;
- Section 7.6, “The \(CB\) and \(CBA\) continuations”; and
- the later Section 7 audit, “Why \(BA\) and \(CB\) are the only free pairs.”

This corrects a potentially confusing shorthand in the compatibility stop:
there are nine hyperref warning events, not nine wrapper commands. The eight
mathematical spans account for eight math-shift events, and the support heading
contains the additional disallowed `\geq` token. Every hazardous span is
wrapped, and no mathematical heading span remains unwrapped.

The TeX arguments of all eight wrappers are byte-identical to the old heading
text. Replacing each wrapper by its first argument gives exactly the old full
heading stream, so printed headings are unchanged. The PDF-string alternatives
are plain and faithful (`s at least 2`, `3r`, `A/B/C`, `BA`, `CB`, and `CBA`).
The `\allowbreak` is a zero-width permitted break point immediately before
`x_4`; it changes no scalar, punctuation, order, or mathematical assertion.
The terminal-LF normalization has no TeX semantics.

These edits are correctly targeted at the recorded source causes: the single
inline scalar sequence that produced the overfull diagnostic and the nine
unsafe PDF-string token events. This is a static compatibility judgment, not a
claim about an unperformed build. The separately governed Round-0 build must
still confirm the emitted log has zero overfull boxes and zero hyperref
warnings.

## Abstract and front matter

The abstract byte slice is identical before and after the compatibility diff;
both slices have SHA-256
`c5694f7db6fc03c48ec3f0e60d5a6cb73efc1240935cdc21b9afbba387fd772d`.
It has thirteen mathematical spans. Replacing each span by one word and
discarding punctuation-only tokens gives the conservative count 180; direct
source-whitespace counting gives 190. Both independently satisfy the locked
180--220 interval. The earlier author's separate math-atom metric was 216;
because the abstract has zero changed bytes, that inherited metric is also
unchanged, but this verdict does not rely on its undocumented tokenizer.

The abstract states PC1 first and gives its exact bound. It identifies
vanishing proper subsums as the obstacle, summarizes the graph/root-fiber and
second-recurrence closure, includes arbitrary torsion and vertical
cancellation, and closes with PC2 and the support-one \(T_4/T_3\) contrast. It
contains no citation, predecessor provenance, publication history, priority
language, or excluded generalization.

The visible title is exact, the author presentation is `Anonymous`, and the
manuscript date is empty. The pdfTeX controls suppress dates and the trailer
identifier; all identity-bearing `hyperref` fields are empty. The
compatibility repair changes none of these controls.

## Structure, tables, appendices, and zero-figure gate

The source has exactly eight numbered main sections in the locked order,
followed by Appendices A--C and then final References. A single `\clearpage`
immediately precedes the bibliography commands. No essential proof is deferred
to an appendix.

There are exactly four `table` environments and no `figure` environment,
`\includegraphics`, external asset, `\input`, or `\include`. The four proof
tables are at the exact logical locations:

| Table | Current source start | Logical location | Verified content |
|---|---:|---:|---|
| 1 | line 452 | Section 5.3 | GZ/GU/R0/R1 membership, equations, \(J\)-convention, and budgets |
| 2 | line 715 | Section 7.4 | all nine adjacent \(A/B/C\) words |
| 3 | line 759 | Section 7.5 | BAA/BAB/BAC continuations |
| 4 | line 786 | Section 7.6 | CBB/CBC/CBA and CBAA/CBAB/CBAC closure |

Every row is derived in the main text. The appendices repeat rank,
component-count, and continuation calculations only. The source remains
feasible for the locked 24--26-page mathematical-content target; actual page
count is correctly left to the prohibited-here Round-0 build.

## Sole external proof input and field bridge

Amoroso--Viada Theorem 6.2 remains the sole external theorem used in a proof,
with

\[
\mathcal A(q,R)=(8q)^{4q^4(q+R+1)}.
\]

The manuscript states its algebraically closed characteristic-zero domain,
embeds the arbitrary characteristic-zero field into an algebraic closure,
preserves the rank of \(\Gamma\), and uses homomorphic images of
\(\Gamma^2\) or \(\Gamma^3\) with ranks at most \(2r\) or \(3r\). Original
solutions inject into the larger solution sets. There is no descent or
solution-set equality claim. Fixed coefficients remain coefficients of the
linear equation and never enlarge a variable group.

## Sparse-image lemma

For a \(q\)-term polynomial with distinct exponents from zero through \(d\),
the tuple

\[
(t^{m_1}u^{-1},\ldots,t^{m_q}u^{-1})
\]

is a homomorphic image of \(\Gamma^2\) of rank at most \(2r\). A coordinate
ratio recovers a nonzero power of \(t\) with at most \(d\) lifts; the original
equation then fixes \(u\). This gives \(d\mathcal A(q,2r)\) on the
nondegenerate locus.

On the degenerate locus, no singleton can vanish. The proper subsets of sizes
two through \(q-1\) number exactly \(2^q-q-2\), and every chosen subsum is a
nonzero polynomial of degree at most \(d\). The resulting bound is exactly

\[
\mathcal S_q(d,r)
=d\bigl(\mathcal A(q,2r)+2^q-q-2\bigr).
\]

Arbitrary, including infinite, torsion introduces no extra fiber: rank controls
the imported theorem and polynomial degree controls every remaining fiber. A
fixed output coefficient requires no coefficient membership in \(\Gamma\).

## PC1: complete two-transition proof

For \(Q=(v,u)\), \(H(Q)=(z,v)\), and \(H^2(Q)=(w,z)\), the first recurrence is
normalized as

\[
Z+U+\sum_{j=1}^sM_j=1,
\qquad Z=z/c,\quad U=-au/c,\quad M_j=-b_jv^{e_j}/c.
\]

The variable tuple \((z,u,v^{e_1},\ldots,v^{e_s})\) has rank at most \(3r\).
The nondegenerate contribution is \(d\mathcal A(s+2,3r)\), including the
degree-\(d\) power fiber and no second multiplicity.

The four degenerate types are exhaustive and retain their exact signs and
subset conventions:

- GZ: \(z=B_J(v)\), \(-au=c+B_{J^c}(v)\), with selected nonempty \(J\);
- GU: \(au=-B_J(v)\), \(z=c+B_{J^c}(v)\), with selected nonempty \(J\);
- R0: \(B_J(v)=0\), with \(|J|\geq2\); and
- R1: \(c+B_J(v)=0\), with nonempty complementary \(J\).

For GZ and GU, both \(J=[s]\) and \(|J|=1\) expose a polynomial with at least
\(s\geq2\) terms. Fixed output coefficients \(1,a,-a\) create no coefficient
rank. R0 has at most \(e_{\max J}-e_{\min J}\) nonzero roots, and R1 has at
most \(e_{\max J}\) roots.

At a root \(v=\rho\), the second recurrence is

\[
w=(c+a\rho)+\sum_{j=1}^s b_jz^{e_j}.
\]

It has \(s+1\) terms unless the constant cancels and exactly \(s\geq2\) terms
when it does. The sparse-image lemma closes every root fiber by
\(\mathcal S_*\), after which \(u=(z-P(\rho))/a\) is unique. No free vertical
chain remains.

Simultaneous zero subsums are covered by the full label union, with deliberate
overcount and no disjointness claim. The primary definition

\[
\mathcal M(\mathbf e)=2(2^s-1)
+\sum_{|J|\geq2}(e_{\max J}-e_{\min J})
+\sum_{\varnothing\neq J}e_{\max J}
\]

and both checksum derivations are unchanged and correct. These pieces prove
the exact PC1 bound with every locked hypothesis.

## PC2 and essential-hypothesis examples

For every prescribed support with \(s\geq2\), the rational choice
\(a=b_j=1\), \(c=-s\), and \(\Gamma=\langle2\rangle\) gives \(P(1)=0\) and

\[
(1,2^n)\longmapsto(2^n,1),
\]

so \(T_1\) is infinite in rank one. This proves exact transition depth, not
optimality of the displayed constants.

The two excluded-coefficient examples remain direct and correct. With
\(c=0\), \(P(X)=X^d+X\), and \(a=-1\),

\[
(t,t^d)\longmapsto(t,t)\longmapsto(t^d,t)
\]

gives infinite \(T_2\). With \(a=0\) and \(P(X)=-1+X+X^2\),

\[
(1,t)\longmapsto(1,1)\longmapsto(1,1)
\]

does the same. Both demonstrate essential hypotheses and make no extension
claim.

## PC3: complete support-one proof

At each of the four local indices for \(T_4\), the triple
\((x_{i+1},x_i^d,x_{i-1})\) has rank at most \(3r\). The four-index union of
nondegenerate local equations contributes \(4d\mathcal A(3,3r)\).

On the fully degenerate locus, the three labels are exactly

\[
\begin{array}{lll}
A_i:&x_{i-1}=-c/a,&x_{i+1}=bx_i^d,\\
B_i:&bx_i^d=-c,&x_{i+1}=ax_{i-1},\\
C_i:&bx_i^d=-ax_{i-1},&x_{i+1}=c.
\end{array}
\]

All nine adjacent words are derived with the displayed bounds. Only \(BA\)
and \(CB\) can remain free after two labels. BAA/BAB/BAC close every \(BA\)
branch. CBB/CBC close two \(CB\) continuations; only \(CBA\) remains free,
and only under \(a=-1\) and \(bc^{d-1}=-1\). CBAA/CBAB/CBAC then impose
nonzero equations of degree at most \(d^2\). The \(3^4=81\) word union covers
simultaneous labels and gives \(81d^2\).

For sharpness, \(c^{d-1}=-1\), \(b=1\), \(a=-1\),
\(K=\mathbb Q(c)\), and \(\Gamma=\langle2,c,-1\rangle\) give a rank-one
group. For \(t=2^n\), the exact scalar order is

\[
t^d,\ t,\ c,\ -t,\ (-t)^d,
\]

so infinitely many initial states lie in \(T_3\). PC3 is fully internal and
remains visibly subordinate to PC1.

## Citation and bibliography closure

The citation set equals the bibliography-entry set and contains exactly seven
keys:

- `amorosoViada2009`;
- `ess2002`;
- `kriegerEtAl2015`;
- `bellGhioca2024`;
- `jiXieZhang2026`;
- `melloYasufuku2026`; and
- `kimEtAl2025`.

There is no duplicate, missing or uncited entry, wildcard `\nocite`, or entry
for the absorbed predecessor. Amoroso--Viada is cited twice and is the only
proof source. ESS remains historical only. The three Krieger-et-al. result
roles remain distinct. Bell--Ghioca retains the fixed-orbit,
finite-generation, progression/residual, and regularity qualifications.
Ji--Xie--Zhang remains non-density; the incompatible Mello--Yasufuku epsilon
regimes remain unmerged; and the Kim-et-al. degree and congruence restrictions
remain explicit. All seven records match the frozen primary-source metadata.

## Static LaTeX, anonymity, anti-claims, and absorption

All 75 labels are unique, and all 108 `\ref`/`\eqref` occurrences target
defined labels. The begin/end environment stack is balanced. All four tables
have the declared structures. No unresolved `TODO`, `FIXME`, `XXX`, `VERIFY`,
placeholder, drafting, or repair marker remains.

The public source contains no manuscript-author identity, affiliation, email,
acknowledgment, grant, repository identity, submission identifier, internal
candidate or project number, local path, hash, governance verdict, agent name,
operational instruction, or unsupported priority claim. Neutral bibliography
authors and dates remain the required exemptions.

The twenty-one mandatory anti-claims occur as twenty-one explicit items at
current lines 921--941. They preserve characteristic, coefficient, collected
support, conjugacy, optimality, effectiveness, height, periodic-point,
coefficient-stratum, broader-map, subgroup, finite-generation,
coefficient-membership, additive-closure, literature, Bell--Ghioca,
Ji--Xie--Zhang, Mello--Yasufuku, Kim-et-al., computational-evidence, and PC3
novelty/black-box boundaries.

The exact public-safe absorption paragraph occurs verbatim exactly once, at
current line 948 under Section 8.3, and nowhere in the abstract, theorem
statements, proofs, literature positioning, tables, appendices, or
bibliography. It continues to make the present paper the sole intended
external version and forbids parallel submission of the predecessor.

## Final disposition

The bounded compatibility repair is byte-exact, correctly targeted, and
semantically inert. It preserves the abstract, printed headings, PC1--PC3,
proof dependencies, four proof tables, all seven citations, all twenty-one
anti-claims, anonymity, and the unique absorption paragraph. No source-level
mathematical, bibliographic, structural, anonymity, or static compatibility
blocker remains at the exact source identities recorded above.

This verdict authorizes no compilation, source edit, PDF, release, submission,
or external communication. It binds only the two reviewed source byte strings
and restores eligibility for the separately governed next stage.

MANUSCRIPT_SOURCE_PASS
