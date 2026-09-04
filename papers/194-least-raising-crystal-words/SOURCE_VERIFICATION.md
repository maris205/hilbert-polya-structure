# Source and collision verification — P194 Round 0 plus Review-B delta

**Checked:** 2026-09-04 UTC  
**Status:** `PASS_INTERNAL / OWNER_AMBER / HOLD_EXTERNAL`

## Bibliography scope

| key | verified record | manuscript scope | excluded inference |
|---|---|---|---|
| `Kashiwara1991` | Masaki Kashiwara, *On Crystal Bases of the Q-Analogue of Universal Enveloping Algebras*, *Duke Mathematical Journal* 63(2), 465–516 (1991), [DOI 10.1215/S0012-7094-91-06321-0](https://doi.org/10.1215/S0012-7094-91-06321-0) | crystal bases and Kashiwara-operator background | the least-colour scheduler or any P194 dynamical theorem |
| `BumpSchilling2017` | Daniel Bump and Anne Schilling, *Crystal Bases: Representations and Combinatorics*, World Scientific (2017), [DOI 10.1142/9876](https://doi.org/10.1142/9876) | finite type-A crystals, word signatures, highest-weight components | ownership of the literal priority rule or fibre atlas |
| `Fulton1997` | William Fulton, *Young Tableaux*, Cambridge University Press (1997), [DOI 10.1017/CBO9780511626241](https://doi.org/10.1017/CBO9780511626241) | Young tableaux and RSK background | the scheduled functional graph |
| `Stanley2023` | Richard P. Stanley, *Enumerative Combinatorics*, vol. 2, 2nd ed., Cambridge University Press (2023), [DOI 10.1017/9781009262538](https://doi.org/10.1017/9781009262538) | Schur specialization, hook formulas, symmetric-function enumeration | P194's inverse criterion or ownership |
| `Sagan2001` | Bruce E. Sagan, *The Symmetric Group*, 2nd ed., Springer (2001), [DOI 10.1007/978-1-4757-6804-6](https://doi.org/10.1007/978-1-4757-6804-6) | RSK, Schensted, standard tableaux, and involutions | the least-colour scheduler or a novelty conclusion |
| `DefantWilliams2022` | Colin Defant and Nathan Williams, *Crystal Pop-Stack Sorting and Type A Crystal Lattices*, *European Journal of Combinatorics* 103 (2022), 103514, [DOI 10.1016/j.ejc.2022.103514](https://doi.org/10.1016/j.ejc.2022.103514), [arXiv:2109.08251](https://arxiv.org/abs/2109.08251) | nearest deterministic crystal-dynamics owner: noninvertible crystal pop-stack sorting, convergence to the highest/minimal vertex, and sharp maximum orbit size | P194's one-edge least-current-colour scheduler, letter-sum clock, Schur depth layers, targetwise `f_i` atlas, or stable full-fibre threshold |

The citation-key set in `main.tex` equals the bibliography-key set.  Every
source is used only for named background or exact subtraction. The
Defant--Williams source is the nearest located dynamical owner, but is not
cited as a proof of a P194 scheduler theorem.

## Hostile Review-B source delta

Review B located Defant--Williams after the Round-0 bounded pass. Their
Definition 2.1 sends a crystal vertex `b` to the unique source of the
connected component of the crystal restricted to the whole starting descent
set `b_down`. Their operator is noninvertible, every forward orbit reaches
the highest/minimal crystal vertex, and their maximum orbit-size theorem is
sharp. This deterministic crystal sorting/orbit surface is therefore too
close to omit and now receives explicit zero contribution credit.

The literal maps remain different. A crystal pop-stack macrostep can traverse
multiple edges and colours selected from the starting descent set. P194 takes
exactly one `e_i` edge at the least currently usable colour and recomputes
availability after each edge. Defant--Williams do not give P194's word-level
letter-sum clock, Schur-specialized depth layers, target-resolved predecessor
set, or `n>=binom(k,2)` full-fibre threshold. This is an object-level
subtraction, not a novelty or clearance conclusion; `OWNER_AMBER /
HOLD_EXTERNAL` remains binding.

## Convention verification

Crystal conventions differ by tensor order, sign assignment, cancellation
direction, and selected unmatched occurrence.  P194 therefore does not cite
a source and silently inherit its typography.  It freezes all four choices in
the literal definition and checks them computationally.  With these choices,
reverse-word RSK—not ordinary left-to-right insertion of the displayed
word—gives the invariant shape used in the formulas.

Word reversal in the proof coordinate is not a conjugacy claim about the
dynamic.  Any external comparison must translate the full tuple

```text
(tensor order, sign encoding, cancellation, edited occurrence, colour order).
```

## Internal history subtraction

| occupied surface | proximity | binding treatment for P194 |
|---|---|---|
| P144, leftmost Dyck reassociation | deterministic leftmost available move; ballot/Catalan layers | all generic least/leftmost-scheduler and ballot-enumeration credit is subtracted; P144 changes Dyck factorization by reassociation, whereas P194 changes one word letter along a crystal edge |
| P181, first-descent prefix reversal | choose the first available defect; target-local inverse criterion | selector form alone earns no credit; P181 reverses a permutation prefix and has a depth-two two-cycle core, while P194 has many highest sinks and an unbounded weight-rank tail |
| P142–146 scout `P02`, RSK insertion-tableau projection | RSK carrier compression and hook-length fibres | permanent RSK-retraction kill is respected: P194 never applies RSK as its update and claims nothing for the classical decomposition |
| P166 open-fresh `D14_RDP`, RSK diagonal feedback | recording-tableau feedback and involution/hook census | the RSK/involution axis is explicitly zero-credit; P194's labelled update is a Kashiwara edge chosen from the current word |
| standing 0-Hecke/sorting firewall | ordered simple-colour moves, descent statistics, monotone rank | no claim is made for generic sorting or least descent; crystal components have shape-dependent sinks and the inverse criterion tests lower-colour availability after a specific `f_i` lowering |
| P192–P196 within-batch P192 | adjacent Coxeter/Hurwitz vocabulary and an adaptive first scheduler | P192 changes adjacent factors of a fixed product and its selected index advances; P194 changes one letter and uses crystal weight rank; their inverse atlases do not transfer |
| P192–P196 within-batch P193 | finite words/permutations and a deterministic scheduler | P193 performs simultaneous positional swaps and refines direct-sum blocks; P194 performs one value change determined by a global signature |

These comparisons establish local nonidentity against the inspected corpus.
They do not establish external novelty, independence from an uninspected
conjugate, or freedom to operate.

## Bounded external reconnaissance

Round 0 used targeted queries around the following combinations:

```text
"crystal graph" least color raising operator dynamics
"word crystal" priority scheduler Kashiwara operator
"highest weight word" repeated e_i least i
Kashiwara operators deterministic dynamics fibre predecessors
"crystal pop-stack sorting" deterministic crystal orbit highest weight
```

The records located in that bounded pass supported the classical background
above; no source was promoted to a direct owner of the full literal scheduler
plus targetwise inverse atlas.  That bounded non-hit is not evidence of
novelty, priority, completeness, or clearance.  Specialist terminology,
opposite tensor conventions, and related normal-form algorithms remain live
owner risks.

## Release rule

A source implementing the same priority rule up to word reversal and colour
reversal, or a theorem package from which both the exact schedule and the
labelled inverse atlas transfer mechanically, triggers withdrawal or a new
residual analysis.  Until a later owner search and hostile review are
completed, the binding state is

`OWNER_AMBER / HOLD_EXTERNAL / NOVELTY_CLAIM_NOT_AUTHORIZED`.
