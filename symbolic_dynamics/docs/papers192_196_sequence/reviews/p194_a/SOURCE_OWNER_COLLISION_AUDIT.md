# P194 Review-A source and owner-collision audit

**Audit date:** 2026-09-04 UTC  
**Decision:** original A no-change plus post-B nearest-owner repair accepted;
no remaining actionable bibliography defect or literal-map collision found in
the bounded audit.  
**Gate:** `OWNER_AMBER / HOLD_EXTERNAL`.

## Bibliography verification

The six citation keys extracted from `main.tex` equal the six records in
`references.bib`; there is no uncited or unresolved entry.

| Record | Independently checked metadata and permitted scope | Result |
|---|---|---|
| Kashiwara, *On crystal bases of the Q-analogue of universal enveloping algebras* | *Duke Mathematical Journal* 63(2), 465--516 (1991), DOI [10.1215/S0012-7094-91-06321-0](https://doi.org/10.1215/S0012-7094-91-06321-0); the [author's KURIMS publication list](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/list.html) gives the same journal coordinates; crystal-base background only | PASS |
| Bump--Schilling, *Crystal Bases: Representations and Combinatorics* | World Scientific (2017), DOI [10.1142/9876](https://doi.org/10.1142/9876), paperback ISBN 978-981-4733-44-1; type-A crystals, tensor signatures, and highest components only | PASS |
| Defant--Williams, *Crystal Pop-Stack Sorting and Type A Crystal Lattices* | *European Journal of Combinatorics* 103 (2022), article 103514, DOI [10.1016/j.ejc.2022.103514](https://doi.org/10.1016/j.ejc.2022.103514), [arXiv:2109.08251](https://arxiv.org/abs/2109.08251); nearest deterministic crystal-dynamics surface, assigned zero contribution credit | PASS |
| Fulton, *Young Tableaux* | London Mathematical Society Student Texts 35, Cambridge University Press (1997), DOI [10.1017/CBO9780511626241](https://doi.org/10.1017/CBO9780511626241), ISBN 978-0-521-56724-4; tableaux and RSK only | PASS |
| Stanley, *Enumerative Combinatorics*, vol. 2, 2nd ed. | Cambridge University Press (2023), DOI [10.1017/9781009262538](https://doi.org/10.1017/9781009262538), ISBN 978-1-009-26253-8; Schur, principal-specialization, and hook enumeration only | PASS |
| Sagan, *The Symmetric Group*, 2nd ed. | Graduate Texts in Mathematics 203, Springer (2001), DOI [10.1007/978-1-4757-6804-6](https://doi.org/10.1007/978-1-4757-6804-6), hardcover ISBN 978-0-387-95067-9; RSK, Schensted, tableaux, and involutions only | PASS |

The publisher/DOI records support the bibliography fields used in the paper.
None is cited as an owner of the priority scheduler, clock, or labelled
inverse atlas.  The manuscript assigns all named classical machinery zero
contribution credit.

## Post-B nearest-owner repair

The original Review-A bounded search did not locate Defant--Williams.  Review B
correctly raised that omission, and Reviewer A independently checked the
primary arXiv record and paper definition before accepting the source-only
repair.  Their Definition 2.1 fixes the descent-colour set of the starting
vertex, restricts the crystal to those colours, and maps the vertex to the
unique source of its connected component.  Their Theorem 1.1 proves a sharp
maximum forward-orbit size equal to the Coxeter number; the abstract also
states convergence to the fixed highest/minimal vertex.

That is close enough that its entire deterministic crystal pop-stack surface
must receive zero contribution credit.  It is nevertheless not the exact P194
map.  A Defant--Williams macrostep resolves a whole restricted connected
component using the starting descent set.  P194 traverses one Kashiwara edge
of the least currently available colour and recomputes the availability set
after that edge.  The inspected source does not state P194's word-level
letter-sum clock, reverse-RSK Schur depth layers for this scheduler, or its
targetwise admissible-`f_i` inverse atlas and stable full-fibre threshold.

The repaired paragraph states precisely this distinction, explicitly assigns
zero credit, and ends with a no-novelty limitation.  It neither turns a source
non-hit into an originality claim nor strengthens the owner gate.

## Convention audit

The literature uses competing tensor orders, sign assignments, cancellation
directions, and edited unmatched occurrences.  P194 states all four choices
literally.  Reviewer reconstruction confirms that its invariant is the shape
of the reversed displayed word.  The smallest separating example is
`e_1(21)=11`: ordinary RSK shape changes, while reverse-word RSK shape does
not.  Therefore an external comparison must translate the entire tuple

```text
(tensor order, sign encoding, cancellation direction,
 edited occurrence, priority order),
```

not merely rename `e` and `f`.

## Bounded external-owner search

The independent query set included exact and convention-reversed variants of

```text
"least color" Kashiwara operator word crystal
"smallest i" e_i crystal highest weight algorithm
repeatedly apply e_i least usable colour
priority Kashiwara operators deterministic highest word
Kashiwara dynamics fibre predecessors
"fibre size" binom(k,2) crystal word
```

The inspected results covered the standard signature rule, mutual
`e_i/f_i` edges, unique highest vertices, algorithms that apply unspecified
raising sequences, and crystal-compatible rewriting.  In particular,
[Nazarov's crystal preliminaries](https://doi.org/10.1112/jlms.12813) state
the standard inverse/highest-weight structure, while
[Meha's K-string rewriting paper](https://www.lix.polytechnique.fr/iwc2021/papers/IWC_2021_paper_8.pdf)
uses crystal graphs to reduce confluence questions to highest-weight words.
Neither inspected source states the literal one-edge least-colour self-map,
its pointwise scheduled functional graph, or the targetwise admissible-`f_i`
atlas and sharp stable fibre threshold.

No direct owner of that full conjunction was located in this bounded search.
This non-hit is not evidence of novelty, priority, completeness, independence
from an unqueried conjugate, or freedom to operate.  Specialist terminology
and opposite conventions remain live owner risks.

## Internal P1--P191 subtraction

The live paper definitions and scouting/kill ledgers were searched for
crystal, ballot, RSK, Schur/hook, involution, least-scheduler, normalization,
and 0-Hecke surfaces.  The closest entries are:

| Prior surface | Shared material | Literal and proof separation after zero credit |
|---|---|---|
| P144 leftmost Dyck reassociation | deterministic least/leftmost available move, ballot/Catalan language, exact tail and target fibres | P144 moves a Dyck factor by a ground-level Tamari reassociation and its clock is the number of prime factors; P194 changes one letter on a coloured crystal edge and has shape-dependent sinks.  The generic scheduler and ballot enumeration receive zero credit. |
| P181 first-descent prefix reversal | first available defect and target-local inverse test | P181 reverses one permutation prefix and has a depth-two fixed/2-cycle core; P194 lowers a letter, has many highest sinks, and can have tail `n(k-1)`.  Selector form and generic inverse bookkeeping receive zero credit. |
| P142--P146 scout P02 | RSK insertion-tableau projection, recording-tableau fibres, hook counts | P02 applies RSK as an idempotent retraction and is permanently killed.  P194 never applies RSK in its update; all RSK decomposition and multiplicity facts are explicitly zero-credit. |
| P152--P156 RSK shape process | RSK/Schur endpoint laws and hook-content multiplicities | that random shape-growth process is a direct classical RSK object.  P194 is a deterministic word-level edge scheduler; its Schur layers earn no residual credit. |
| P166 open-fresh P04/D14_RDP | RSK diagonal/recording feedback and involution census | that proposal is killed as classical RSK feedback.  P194's update retains the word and follows a current Kashiwara edge; the involution census is background only. |
| P113 principal-hook partition dynamics | hook vocabulary, a monotone clock, and a fibre theorem | P113 regroups Ferrers cells into diagonal-hook lengths on integer partitions.  It neither has the word-crystal update nor the labelled `f_i` admissibility conditions. |
| standing sorting/0-Hecke firewall | ordered simple colours, a least defect, monotone rank | no credit is assigned to generic normalization or ordered descent.  Crystal components, the literal edited word position, and lower-colour tests after a specified lowering prevent a mechanical transfer of the target atlas. |

No inspected P1--P191 system has the same carrier/update, and no listed prior
proof mechanically transfers both the literal priority trajectory and the
labelled inverse criterion.  This is a bounded internal noncollision record,
not a novelty claim.  All RSK/Schur/hook/involution and generic scheduler
axes remain subtracted.

## Disposition

No further source amendment is requested after the accepted post-B repair.
The original Review-A no-change result remains tied to the preserved Round-0
snapshot; the current live source has separately passed this nonregression
audit.  Any later source implementing
the same priority rule up to a fully specified tensor/word/colour conjugacy,
or a theorem from which the exact labelled inverse atlas transfers, reopens
the gate.  Current state: `OWNER_AMBER / HOLD_EXTERNAL`.
