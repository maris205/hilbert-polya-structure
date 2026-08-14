# Phase 2 — Deninger packet/groupoid literature and source-update search

Status: **COMPLETE — SEARCH, SCREENING, AND SOURCE VERIFICATION ONLY**  
Search date and evidence cutoff: **2026-08-14**  
Frozen source candidate: `DEN-WITT-Z-FIN`  
Protocol input: `research_protocol.md`, `candidate_lock.md`  
Proof construction, manuscript synthesis, Route verdict, and Paper 8 work: **not performed**

## 1. Scoped source-audit finding

This search found one material post-Paper-2 update, but it does **not** supply
the missing packet trace.

- Morishita, arXiv:2508.15971v5, constructs a continuous map from an
  **unrefined** Deninger system for an abelian number field to the corresponding
  Connes--Consani adelic space.  The map is Galois-equivariant and
  flow-anti-equivariant.  In Theorem 3.6, every orbit circle `gamma_p` in the
  Deninger packet over `p` is sent onto the one adelic circle `C_p`.
- This is a genuine, source-verified **topological collapse bridge**.  Any older
  wording that says there is no relation at all between the two frameworks is
  now too broad.
- As printed, it is formulated on an unrefined larger character space:
  Morishita's Remark 2.1.13 explicitly omits the admissibility refinement
  required in Deninger Section 4.  A subsequent source audit nevertheless
  proves that the continuous map itself restricts to Deninger's finite-kernel
  subsystem, yielding a same-object topological intertwiner.  This corrected
  restriction is still not an analytic bridge: no measure, disintegration,
  Haar system, groupoid, representation, von Neumann algebra, trace domain,
  return distribution, or determinant is transported.
- The paired Connes--Consani source has an adelic crossed-product viewpoint,
  a semilocal `C*`-algebra/K-theory calculation, and an introductory local
  Schwartz-kernel trace expression.  It does not define a Deninger-packet
  groupoid, packet trace, normal semifinite trace, or Fuglede--Kadison
  determinant.  Morishita does not pull those target-side structures back.
- Deninger's 2025 *Rational Witt vectors and associated sheaves* studies
  sheafification and finite correspondences and explicitly treats improvement
  of the earlier spaces as motivation.  It does not replace the packet theorem
  or add a packet measure/trace construction.

Accordingly, within the dated and indexed corpus below, **no primary work was
found that explicitly connects Deninger's rational-Witt prime packets to a
groupoid/von Neumann/normal-semifinite trace determinant**.  This is a
reproducible search result, not a universal theorem that no future or unindexed
construction can exist.

## 2. Eligibility and evidence rules

### 2.1 Inclusion criteria

A work was included if its primary text did at least one of the following:

1. owns the rational-Witt flow or its closed-point packets;
2. is a later Deninger update that could change the construction or its
   admissibility/source-ownership boundary;
3. gives an explicit map involving those Deninger systems or packet orbits; or
4. is the primary target source needed to type such a map against adelic
   noncommutative/operator-algebra structures.

### 2.2 Exclusion criteria

A work was excluded from the retained corpus if `Deninger`, `Witt`, `packet`,
`trace`, or `groupoid` was only a semantic collision, citation, historical
motivation, or theorem about a different object.  In particular, the following
do not satisfy the source-to-packet bridge criterion by themselves:

- Fuglede--Kadison determinants for algebraic actions or group von Neumann
  algebras;
- trace/regularized-determinant formulas for smooth 3-dimensional foliated
  flows with simple isolated closed orbits;
- etale fundamental groupoids for parallel transport on p-adic curves;
- KMS states on unrelated number-field Toeplitz/groupoid `C*`-algebras; and
- unrelated uses of “packets” in homogeneous dynamics or representation
  theory.

### 2.3 Evidence policy

- Primary papers/preprints carry all mathematical content claims.
- arXiv, publisher, Crossref, and institutional pages are used only for
  existence, version, and bibliographic verification.
- OpenAlex and general web search are discovery aids only.  No theorem claim
  below depends on their summaries or citation counts.
- Absence statements are limited to the stated query fields, records, and
  inspected full texts.

## 3. Reproducible search strategy

### 3.1 Counted arXiv channel

Endpoint template:

```text
https://export.arxiv.org/api/query
  ?search_query=<URL-encoded query>
  &start=0
  &max_results=100
  &sortBy=submittedDate
  &sortOrder=descending
```

The table reports the API's exact `opensearch:totalResults` value observed on
2026-08-14.  Query results overlap and **must not be summed**.

| ID | Exact `search_query` value | Hits | Screening consequence |
|---|---|---:|---|
| A1 | `au:"Christopher Deninger"` | 44 | Complete Deninger arXiv author set screened by title/abstract; all post-v4 records separately checked. |
| A2 | `all:"prime packets"` | 0 | No metadata/abstract exact-phrase hit. |
| A3 | `all:Deninger AND all:groupoid` | 2 | arXiv:1106.5912 and arXiv:0706.0925; both full texts excluded as different objects. |
| A4 | `all:Deninger AND all:"von Neumann"` | 7 | Algebraic-action, entropy, and group/crossed-product von Neumann literature; no rational-Witt packet record. |
| A5 | `all:Deninger AND all:"semifinite trace"` | 0 | No metadata/abstract hit. |
| A6 | `all:Deninger AND all:"Fuglede-Kadison"` | 8 | General algebraic/group-action determinant literature; no rational-Witt packet record. |
| A7 | `all:Deninger AND all:determinant` | 24 | One adjacent 3D foliated-flow theorem, arXiv:2410.20758; remaining hits are different determinant/Witt/entropy/cohomology objects or false positives. |
| A8 | `all:"rational Witt" AND all:trace` | 0 | No metadata/abstract hit. |
| A9 | `all:"packet of periodic orbits" AND all:groupoid` | 0 | No metadata/abstract exact-phrase hit. |
| A10 | `all:Deninger AND all:"Connes-Consani"` | 1 | Morishita arXiv:2508.15971v5; included and inspected in full. |
| A11 | `all:Deninger AND all:"Haar system"` | 0 | No metadata/abstract hit. |

The two A3 records were:

```text
1106.5912v3  KMS states on the C*-algebras of non-principal groupoids
0706.0925v1  Principal bundles on p-adic curves and parallel transport
```

The seven A4 records were:

```text
1911.00793v3  Partition functions as C*-dynamical invariants and actions of congruence monoids
1202.1213v2  Entropy, Determinants, and L2-Torsion
1111.1548v1  Regulators, entropy and infinite determinants
0905.0604v1  Mahler measures and Fuglede--Kadison determinants
0712.0667v2  Determinants on von Neumann algebras, Mahler measures and Ljapunov exponents
0608539v2     p-adic entropy and a p-adic Fuglede-Kadison determinant
0502233v1     Fuglede-Kadison determinants and entropy for actions of discrete amenable groups
```

The sole A10 record was Morishita arXiv:2508.15971v5.

### 3.2 Author-update screen

The most recent records in A1 were checked explicitly:

| arXiv ID | First submission | Title | Decision |
|---|---|---|---|
| `2608.11943v1` | 2026-08-12 | *Invariant Functions on p-divisible Groups and the p-adic Corona Problem II* | Exclude: different p-divisible-group problem. |
| `2508.13685v3` | 2025-08-19 | *A remark on the vanishing of Higgs fields in the p-adic Simpson correspondence* | Exclude: different p-adic Simpson problem. |
| `2508.05329v1` | 2025-08-07 | *Rational Witt vectors and associated sheaves* | Include: direct later update to the rational-Witt foundations. |
| `2504.15767v3` | 2025-04-22 | *Is there a Birch and Swinnerton-Dyer conjecture for Dedekind zeta functions?* | Exclude: no packet/groupoid trace construction. |
| `2301.11643v1` | 2023-01-27 | *Primes, knots and periodic orbits* | Include: primary author overview of the packet theorem. |
| `1807.06400v4` | 2018-07-17; v4 2024-02-07 | *Dynamical systems for arithmetic schemes* | Include: construction/theorem owner. |

The University of Münster's current author page was also checked as an
identity/publication cross-check.  It corroborated the 2025 Deninger preprints
but was not treated as a complete counted bibliography.

### 3.3 Citation and reference chasing

The exact OpenAlex calls were:

```text
GET https://api.openalex.org/works/https://doi.org/10.1016/j.indag.2024.05.007
GET https://api.openalex.org/works?filter=cites:W2884984338&per-page=100
```

Observed result: `cited_by_count = 2`, with exactly two returned citing records:

1. Deninger, *There is no "Weil-"cohomology theory with real coefficients for
   arithmetic curves*;
2. *Introduction*, DOI `10.1007/978-3-032-15413-2_1` (2026).

The first was full-text screened and excluded below.  The second was not
promoted beyond citation metadata because the retrievable primary metadata did
not identify a packet/groupoid/trace result.  The failure of this index to
return Morishita, despite the direct citation in Morishita's full text, is an
observed indexing-coverage warning.

Backward reference chasing from Morishita added one indispensable target
source:

- Connes and Consani, *Knots, primes and class field theory*,
  arXiv:2501.06560v1; published metadata verified as Contemporary Mathematics
  842 (2026), 105--132, DOI `10.1090/conm/842/16852`.

### 3.4 Supplementary exact web queries

The following exact strings were run to catch records not yet joined in
citation indexes:

```text
site:arxiv.org Deninger rational Witt vectors dynamical systems arithmetic schemes trace groupoid
site:arxiv.org Deninger prime packets groupoid von Neumann trace determinant
site:uni-muenster.de Christopher Deninger publications arithmetic dynamical systems Witt vectors
"On a relation between Deninger's foliated dynamical systems and Connes-Consani's adelic spaces"
site:arxiv.org Morishita Deninger Connes Consani adelic spaces
"Knots, primes and class field theory" Connes Consani PDF
"packet of periodic orbits" Deninger trace groupoid
"packet of R+ orbits" groupoid trace
"rational Witt" "von Neumann" Deninger
"rational Witt" groupoid determinant
```

The web interface did not expose stable corpus-level totals, so these queries
are intentionally excluded from numerical flow counts.  They located
Morishita and Connes--Consani, whose existence and content were then verified
from arXiv/full text and, where available, DOI metadata.  They also produced
semantic collisions involving rational Witt groups of knots and packets of
periodic torus orbits; those were excluded.

## 4. Screening flow and candidate ledger

Because the counted arXiv queries overlap, a naive PRISMA sum would be false.
The transparent work-level audit ledger is:

- 44 Deninger author records title/abstract screened;
- all records in the narrow A2--A11 intersections screened;
- 16 potentially material work records promoted to the explicit candidate
  ledger below;
- 13 of those inspected in full text and 3 recent author records excluded at
  title/abstract level;
- 5 primary works retained; 11 excluded from the retained corpus.

| Work | Screening depth | Include? | Exact reason |
|---|---|---:|---|
| Deninger, arXiv:1807.06400v4 / DOI `10.1016/j.indag.2024.05.007` | Full text | Yes | Owns rational-Witt flow, admissibility classes, packets, topology, and Section 11's distinct convolution construction. |
| Deninger, arXiv:2301.11643v1 | Full text | Yes | Primary author restatement/overview of compact prime packets. |
| Deninger, arXiv:2508.05329v1 | Full text | Yes | Direct later rational-Witt update and improvement motivation. |
| Morishita, arXiv:2508.15971v5 | Full text | Yes | Explicit Deninger-to-Connes--Consani continuous map and packet-orbit image theorem. |
| Connes--Consani, arXiv:2501.06560v1 / DOI `10.1090/conm/842/16852` | Full text | Yes | Primary target-space/crossed-product context needed to type Morishita's bridge. |
| Deninger, arXiv:2608.11943v1 | Title/abstract | No | p-divisible groups/corona problem, not rational-Witt packets. |
| Deninger--Kamlesh, arXiv:2508.13685v3 | Title/abstract | No | p-adic Simpson correspondence, not packets. |
| Deninger, arXiv:2504.15767v3 | Title/abstract | No | Dedekind-zeta BSD question, no packet trace construction. |
| Deninger, arXiv:2204.02714v2 | Full text | No | Cohomological obstruction; its “trace isomorphism” is not a packet/operator trace. |
| Connes--Consani, arXiv:2209.08536 | Full text | No | Non-additive geometry; rational Witt and Haar-measure occurrences concern different constructions. |
| Alvarez Lopez--Kim--Morishita, arXiv:2410.20758v1 | Full text | No | Regularized determinant for certain smooth 3D Riemannian foliated systems with simple closed orbits; no rational-Witt packet/groupoid/von Neumann trace. |
| Alvarez Lopez--Kordyukov--Leichtnam, arXiv:2402.06671v2 | Full text | No | `b`-trace/Lefschetz distribution for simple foliated flows on smooth manifolds; no rational-Witt packet transport. |
| Deninger, arXiv:0712.0667v2 | Full text | No | Fuglede--Kadison determinant in `L-infinity(Omega) crossed-product Z` for an ergodic probability action; no arithmetic-scheme packet. |
| Deninger, arXiv:0905.0604v1 | Full text | No | Mahler measures and group von Neumann algebras; no rational-Witt packet. |
| Neshveyev, arXiv:1106.5912v3 | Full text | No | KMS states for etale groupoid `C*`-algebras and ax+b Toeplitz systems; “Deninger” enters through a different cited joint work. |
| Hackstein, arXiv:0706.0925v1 | Full text | No | Etale fundamental groupoid and p-adic parallel transport; no periodic packet or trace determinant. |

## 5. Annotated retained sources

### 5.1 `DEN-V4` — construction and ownership baseline

Christopher Deninger, *Dynamical systems for arithmetic schemes*,
arXiv:1807.06400v4; final publication *Indagationes Mathematicae* 37(1)
(January 2026), 25--136, DOI `10.1016/j.indag.2024.05.007`.
[arXiv record](https://arxiv.org/abs/1807.06400) |
[publisher record](https://www.sciencedirect.com/science/article/pii/S0019357724000491)

Relevant source locators:

- Section 4, Definition 4.1 and the examples following it: admissible classes,
  including finite-kernel `E_f`; the source says the resulting topology depends
  strongly on `E`.
- Section 5, equations (37)--(40), Theorem 5.2: the choice-dependent packet
  coordinates and exhaustion of nontrivial isotropy.
- Section 6 and Theorem 6.1: suspension flow, compact packets, periods, and the
  statement that `Gamma^E_x = Gamma_x` when `E_f` is contained in `E`.
- Section 7: pointwise/inductive-limit/quotient topologies and the warning that
  relevant continuous bijections need not be homeomorphisms in general.
- Section 11, equations (104)--(112): Haar measure and convolution on the
  inverse-limit group `inverse-limit K^x`; this is not a packet groupoid or
  packet return trace.

Full-text term audit found no occurrence of `groupoid`, `von Neumann`,
`semifinite`, `Fuglede`, or `Haar system`.  `Haar` occurs in Section 11 on the
different inverse-limit group just identified.  This source remains the owner
of packet indexing and clocks, not of the missing analytic trace fields.

### 5.2 `DEN-SURVEY` — corroborating packet overview

Christopher Deninger, *Primes, knots and periodic orbits*,
arXiv:2301.11643v1; published in *Colloquium De Giorgi 2021--2022* (2024).
[arXiv record](https://arxiv.org/abs/2301.11643)

The survey restates the compact packet picture and prime/period analogy.  Its
full text contains no `groupoid`, `von Neumann`, `semifinite`, `Fuglede`, or
`Haar system` occurrence.  It is by the constructor and is corroborative, not
an independent trace construction.

### 5.3 `DEN-RW-SHEAVES` — later rational-Witt update

Christopher Deninger, *Rational Witt vectors and associated sheaves*,
arXiv:2508.05329v1, submitted 2025-08-07.
[arXiv record](https://arxiv.org/abs/2508.05329)

The introduction explicitly says the spaces of Kucharczyk--Scholze and
Deninger have useful features and shortcomings and that the paper seeks to
understand and possibly improve their rational-Witt foundations.  The paper's
results concern sheaf conditions, the ind-scheme `W_J`, finite cycles and
correspondences, and a geometric interpretation of Almkvist's theorem.

Full-text checks found:

- no `packet`, `groupoid`, `von Neumann`, `semifinite`, `Haar`, or flow-trace
  construction;
- `determinant` occurrences concern Hankel determinants in rational-Witt
  algebra, not a dynamical or Fuglede--Kadison determinant; and
- the earlier dynamical system is cited as motivation rather than rebuilt with
  a packet measure/trace.

It is therefore an important source update, but not a source-ownership update
for the missing packet analytic structures.

### 5.4 `MORISHITA-BRIDGE` — explicit but collapsing typed bridge

Masanori Morishita, *On a relation between Deninger's foliated dynamical
systems and Connes-Consani's adelic spaces*, arXiv:2508.15971v5.  Submitted
2025-08-21, revised through 2026-01-21; the arXiv record says “to appear in
Muenster Journal of Mathematics.”
[arXiv record](https://arxiv.org/abs/2508.15971)

Exact typed findings:

1. **Object mismatch is explicit.** Remark 2.1.13 says Deninger imposes
   conditions on the characters in Section 4 to make a smaller, more suitable
   space, and Morishita omits that refinement for this paper.  Section 2.2
   repeats that the refinement is ignored.  The ambient source object is
   therefore not licensed as identical to frozen `DEN-WITT-Z-FIN`.
2. **Packet statements are imported, not a new measured construction.**
   Theorems 2.2.8 and 2.2.9 attribute their packet mapping-torus/homeomorphism
   descriptions to Deninger Sections 5--7.  No separate proof block or
   measure/disintegration statement accompanies either theorem.  Theorem
   2.2.9 gives circle orbits of length `log Np` for the finite number-field
   case; Theorem 2.2.8 concerns the algebraically closed-residue-field case and
   has different orbit fibres.  The two must not be conflated.
3. **Map type is limited.** Lemma 3.5 and Theorem 3.6 construct a continuous,
   Galois-equivariant, `R_+`-anti-equivariant map.  They do not assert a global
   homeomorphism, measurable-flow equivalence, algebra homomorphism, or
   trace-preserving map.
4. **Packet label is collapsed after finite-kernel repair.** Equation (2.2.7)
   is not surjective onto the printed full character space: the trivial
   character is an explicit counterexample, and the printed proof of Theorem
   3.6(2) checks only the vanishing of the `p`-coordinate.  Deninger's equation
   (35) repairs the statement on the finite-kernel class `E_f`: every
   away-from-`p` coordinate is then nonzero and can be normalized, so each
   source circle maps onto the fixed adelic circle `C_p`.  Distinct transverse
   circles therefore have the same target orbit.  This many-to-one behaviour
   does not by itself choose or transport a transverse measure; a separate
   disintegration/trace theorem would be required.
5. **No analytic transport fields occur.** Full-text occurrence counts were:
   `groupoid 0`, `von Neumann 0`, `semifinite 0`, `Haar 0`, `measure 0`,
   `disintegrat* 0`, `Fuglede 0`.  The five `trace` and two `determinant`
   occurrences are introductory historical remarks or bibliography titles,
   not constructions in the theorem.

Deninger Section 6 states that the finite-kernel subsystem contains the full
finite-prime packet.  Morishita's continuous equivariant map can be restricted
and descended on that invariant subsystem, producing a newly derived
same-object, time-reversing intertwining map.  Global surjectivity onto the
adelic space is neither stated nor true in general, so this is not called a
global factor map.  The restriction fills continuity, flow, prime-label, and
absolute-clock fields only; it does not fill product topology/Borel,
transverse measure, algebra, representation, trace-domain, return, zero-mode,
analytic-family, or determinant fields.  See `source_audit.md`, Section 7,
for the repaired proof and exact boundary.

### 5.5 `CC-CLASS-FIELD` — target-side adelic/operator context

Alain Connes and Caterina Consani, *Knots, primes and class field theory*,
arXiv:2501.06560v1.  Crossref verifies the final DOI metadata as Contemporary
Mathematics 842 (2026), 105--132, DOI `10.1090/conm/842/16852`.  The local
full text is the 30-page arXiv v1, not a claim of byte identity with the final
28-page publication.
[arXiv record](https://arxiv.org/abs/2501.06560) |
[publisher DOI](https://doi.org/10.1090/conm/842/16852)

Relevant contents:

- the adelic space has one periodic circle `C_p` of length `log p` per rational
  prime and finite covers whose monodromy encodes Frobenius;
- the introduction recalls the noncommutative crossed product
  `C_0(A_K) crossed-product K^x` and writes a local Schwartz-kernel trace
  contribution to explicit formulas;
- Section 5.4 computes K-theory for a semilocal `C*`-algebra associated with
  the generic orbit and finitely many periodic orbits.

Full-text checks found no `packet`, `groupoid`, `von Neumann`, `semifinite`,
`Fuglede`, or `determinant` occurrence.  The source does not construct a
normal semifinite trace or determinant on a Deninger packet.  In combination
with Morishita, it provides a target-side topological/`C*` lead, but the
many-to-one circle map is not an algebraic, measured, or trace-preserving
transport theorem.

## 6. Direct packet-to-operator-algebra intersection audit

| Required connection | Located primary source? | Source-verification result |
|---|---:|---|
| Deninger rational-Witt packet -> selected locally compact groupoid | No | Deninger does not select one; Morishita does not define one; A3 hits are unrelated groupoids. |
| Packet groupoid -> Haar system | No | A11 returned zero; neither included bridge source uses `Haar system`. |
| Packet/transverse base -> invariant or quasi-invariant measure | No | Morishita has zero `measure` occurrences and collapses all packet orbit circles to `C_p`. |
| Packet observable algebra -> von Neumann completion | No | A4 hits concern different probability/group actions; Morishita has zero `von Neumann` occurrences. |
| Packet algebra -> normal faithful semifinite trace/domain | No | A5 returned zero; no included source defines a trace ideal/domain for a packet. |
| Packet trace -> Fuglede--Kadison or analytic trace determinant | No | A6 hits are different group/action algebras; the adjacent regularized-determinant theorem concerns smooth 3D foliated flows, not rational-Witt packets. |
| Deninger source -> Connes--Consani topological orbit | Yes, limited and corrected | Restricting Morishita's map to Deninger's invariant `E_f` subsystem gives a continuous anti-equivariant intertwiner; Deninger (35) repairs the packetwise image proof.  It is not globally onto and collapses all transverse circles over `p` to the same `C_p`. |
| Connes--Consani target -> crossed-product/semilocal `C*` objects | Yes, target only | Connes--Consani supplies target-side NCG/`C*` context; no pullback to a packet trace is proved. |

This table is a source-coverage statement only.  It neither constructs the
missing objects nor rules out a future enrichment.

## 7. Source quality, independence, and contamination advisory

### 7.1 Discipline-relative quality

| Source | Manifestation used | Quality/independence caveat |
|---|---|---|
| Deninger v4 | arXiv author version; final journal metadata verified | Primary construction and published theorem source.  Author self-audit; not independent replication. |
| Deninger survey | arXiv/published chapter | Primary author overview, intellectually non-independent of v4. |
| Deninger rational-Witt sheaves | arXiv v1 | Primary 2025 preprint; no final journal record located in this search. |
| Morishita bridge | arXiv v5; “to appear” note | Primary theorem text and source-verified existence.  The paper acknowledges substantive discussions with Deninger, Connes, and Consani, so it is not an independent replication of either program. |
| Connes--Consani class-field paper | arXiv v1; 2026 DOI metadata verified | Primary target source; local arXiv text may differ from the final AMS chapter. |

Mathematical theorem papers sit low in a generic empirical evidence hierarchy,
but they are discipline-relative Grade-A primary evidence for what objects and
maps they themselves define.  They are not empirical replications.

### 7.2 Post-LLM contamination flag

The three 2025 arXiv texts are post-LLM-inflection publications.  They were not
accepted from search snippets: title, author, version history, complete PDF,
internal theorem statements, references, and SHA-256 were checked.  This
reduces identity and hallucinated-citation risk but cannot establish anything
about undisclosed writing assistance.  No mathematical claim here relies on
AI-generated summaries.

### 7.3 Terminology contamination

The query vocabulary is unusually collision-prone:

- “packet of periodic orbits” also denotes finite packets of homogeneous torus
  orbits with invariant measures;
- “rational Witt” also appears in knot-concordance Witt groups and
  noncommutative characteristic-polynomial theory; and
- `Deninger + groupoid` retrieves number-field Toeplitz/KMS work or p-adic
  fundamental groupoids in which Deninger's role is unrelated to the
  rational-Witt flow.

All such hits were excluded unless a primary full text named the relevant
Deninger rational-Witt system or packet map.

### 7.4 Coverage limits

- arXiv metadata search does not index every journal/book text or every term in
  a PDF; backward reference chasing and exact-title web searches partly
  mitigate, but do not eliminate, that limitation.
- OpenAlex visibly lagged the direct citation from Morishita.
- No claim is made about private manuscripts, unindexed proceedings, or work
  appearing after 2026-08-14.
- Keyword zero counts support screening but are not substitutes for full-text
  reading; all five retained works were read at their relevant sections.

## 8. Retained local-source manifest

Only full texts retained by the eligibility criteria are listed.  Other files
in `notes/sources/` belong to parallel Phase-2 analytic-source work and are not
part of this subsearch manifest.

| Local file | Version/extent | SHA-256 | Integrity and locator policy |
|---|---|---|---|
| `sources/deninger-dynamical-systems-arithmetic-schemes-v4.pdf` | arXiv v4; 119 pages | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | Parallel ownership audit preflight `PASS`, 119/119/119 pages; use section/theorem/equation locators. |
| `sources/deninger-primes-knots-periodic-orbits.pdf` | arXiv v1; 16 pages | `453c19e9daa20e2d6976b8eb7ee6725f2b5f666e95a16e265b45d9121ac67269` | Parallel ownership audit preflight `PASS`, 16/16/16 pages; use theorem/section locators. |
| `sources/deninger-rational-witt-vectors-associated-sheaves-v1.pdf` | arXiv v1; 31 pages | `19870cbdddbde82526939eb801c2ce14707dc7b48e54a7bc81f4a84400505002` | Parallel ownership audit preflight `PASS`, 31/31/31 pages; use theorem/section locators. |
| `sources/morishita_2025_dynamical_systems_arithmetic_topology_v5.pdf` | arXiv v5; 26 pages | `3a5a34165a4bedfefb2c06f43f4e40e416882ae3406a9cd043f6ac12aebb21ae` | ARS preflight `PASS`, 26/26/26 pages; theorem/remark locators also used. |
| `sources/connes_consani_2025_knots_primes_class_field_v1.pdf` | arXiv v1; 30 pages | `f200c41d6d772389528bb1de58ad7fe98fd8db807d72360d4311ecb3c44d2fe5` | Preflight `PASS`, 30/30/30 pages; use section/theorem locators. |

The downloaded Morishita file is the current arXiv v5, not v1.  The
Connes--Consani file is arXiv v1; the final AMS metadata was verified
separately, and byte/text identity with the final typesetting was not assumed.

## 9. Phase-2 handoff boundary

The literature stage, combined with the independent ownership audit, hands
forward exactly three source facts:

1. the broad “no Deninger--Connes relation” statement must be narrowed because
   `MORISHITA-BRIDGE` exists; and
2. Morishita's printed full-character parametrization and packet-image proof
   need the finite-kernel repair, after which a genuine continuous
   time-reversing intertwiner exists on `DEN-WITT-Z-FIN`, packetwise onto but
   not globally onto the adelic target; and
3. the narrower Paper-2 finding remains source-supported: the searched primary
   literature still does not provide the measured/operator-algebra transport
   required to make a packet groupoid trace or determinant belong to
   `DEN-WITT-Z-FIN`.

Whether a new enrichment can be built, whether any proxy theorem is true, and
what Route status follows are deliberately left to later protocol phases.
