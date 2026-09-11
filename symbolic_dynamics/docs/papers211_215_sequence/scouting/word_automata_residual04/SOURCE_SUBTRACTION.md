# Source-first subtraction and entrance triage

Date: 2026-09-09 UTC. Author: /root/round211_fresh_residual_scout.
One attempted literal; zero promotion and zero pilot. Bounded negative check,
not global novelty certification.

## Selected primary sources

| Source | Actual read scope | Use |
|---|---|---|
| Štěpán Holub, Martin Raška, Štěpán Starosta, Combinatorics on Words Basics, Archive of Formal Proofs, entry dated 2021-05-24 and history updated 2025-11-19 | Entry metadata plus actual CoWBasic border/shortest-period sections, through the complete short proof of min_per_len_diff; not the full 6,974-line theory | Ordinary least period and longest proper-border length are complementary; this credited primitive is not the feedback theorem |
| Frédérique Bassino, Julien David, Cyril Nicaud, On the Average Complexity of Moore's State Minimization Algorithm, STACS 2009, pp. 123–134; arXiv:0902.1048v1 | Metadata and HTML §§2.1–2.3, Proposition 2.1, Theorem 2.2, algorithm discussion and Lemma 2.3/proof | Bounded-word-behavior refinement and the minimal quotient are standard automaton mechanisms |

The period relation is exactly min_per_len_diff, following
min_per_max_border, in the
[CoWBasic primary source](https://raw.githubusercontent.com/isabelle-prover/mirror-afp-devel/master/thys/Combinatorics_Words/CoWBasic.thy).
The [AFP entry](https://isa-afp.org/entries/Combinatorics_Words.html)
supplies attribution and version history. The least ordinary period equals
word length minus longest proper-border length. Step 1 independently spells
out its elementary proof. No Isabelle execution or whole-theory audit occurred.

[Bassino–David–Nicaud's primary article](https://arxiv.org/html/0902.1048v1)
states the successive equivalence refinement and canonical minimal quotient.
Only its deterministic preliminary mechanism is used for exclusion, not the
average-case theorem or its proof. The nontrivial two-block start and the
all-final/no-final cases must be distinguished. No blanket n−2 bound is
imported for arbitrary partitions or one-state boundary cases.

Other searches returned author/publisher snippets on borders and repeated
suffixes. Several Lecroq PDF and Cambridge excerpt body requests failed with
gateway/timeouts. The AFP outline supplied front matter but a requested
later section timed out. The full CoWBasic HTML exceeded the tool content
limit; the raw official-project mirror then supplied the relevant source.
These failures are recorded in PRIMARY_REQUESTS.json, not represented as
successful body reads. Snippets did not establish a new literal or complete
owner-theorem coverage.

## Actual old originals

INPUT_PINS.sha256 pins these eight files. Paths are workspace-relative.
NATIVE_READS.json preserves selected real command arguments and returned
outputs. Partial read extents below are deliberate.

| Original | Read extent | Subtraction |
|---|---|---|
| papers/134-recomputed-border-array-dynamics/main.tex | Entire main.tex in two contiguous reads | Border feedback on the exact carrier; full two-cycle atlas and factorial-fibre proof/equality cases |
| docs/papers204_208_sequence/scouting/word_local/SCOUT_REPORT.md | Entire report | Earlier previous-gap, distinct-suffix, palindrome-suffix, border-count and equal-run entrances; old Z-array status is not silently promoted |
| docs/papers211_215_sequence/scouting/parallel_run_erasure_lane/PROOF_AND_DISPOSITION.md | Entire proof/disposition | Parallel maximal-run deletion already has a sharp maximum and exact run-gap inverse decomposition |
| docs/papers204_208_sequence/scouting/finite_systems_thirty_ninth/PROOF_PACKAGE.md | Lines 1–160; the used §1 proof is complete | Next-equal-gap feedback on its suffix-bounded carrier is old previous-gap feedback reflected, not a whole alphabet-cube conjugacy |
| docs/papers204_208_sequence/scouting/finite_systems_eighteenth/PROOF_AND_ADAPTERS.md and INTAKE.md | Entire proof and intake | Brzozowski minimization, Moore refinement, trace normal form and leftmost free cancellation were explicitly evaluated already |
| docs/papers112_116_sequence/scouting/COMBINATORIAL_SCOUT.md | Focused C6 table row and C6 explanation; broader initial discovery not needed | Scalar longest-border descent is the old fixed-table KMP failure-link chain |
| docs/papers211_215_sequence/scouting/finite_compression_recoding_fresh_desk/HANDOFF.md | Entire handoff, as contextual disposition | Earlier uninstantiated compression hints did not justify two axes; no Lyndon/compression variant is instantiated here |

The actual P134 proof is decisive, not a title match. It defines B(x)_i=β_i(x)
on the same E_n. The attempted feedback is F=C∘B with C(y)_i=i−y_i.
Hence F⁻¹(y)=B⁻¹(Cy) as sets for every target. P134's extremal argument
and both unique maxima transfer without new inverse reasoning.
This is NOT conjugacy: fixed-point counts differ for all n≥2.
The new two-step time formula is directly derived, not borrowed from
P134's mismatch-amplifier clock.

## Other entrances: old comparisons or uninstantiated ideas

1. Scalar border descent is excluded by old C6's KMP match; recomputed
   borders are P134. Next-equal gaps are the actual old reversal adapter.
2. DFA minimization and partition refinement are excluded by the eighteenth
   scout's literal definitions/proofs and the independent primary source
   preliminaries above. No canonical language representative or arbitrary
   partition refinement is freshly proposed.
3. Deletion and normal-form entrances are covered by old free cancellation,
   trace and parallel-run-erasure evidence. A schedule/encoding/name change
   is not used to fill a seat.
4. A longest-repeated-suffix feedback hint lacked an all-parameter time
   spine plus materially independent inverse mechanism in this bounded
   check. It was NOT instantiated. In particular the factor-oracle
   statistic sometimes called lrs is not assumed to equal the true
   longest repeated suffix. Failed full-text access is a source limitation,
   not a reason to guess that contract.

Only the shortest-prefix-period feedback in PROOF_AND_DISPOSITION.md is
counted as an attempted new literal. Its structural difference from P134
does not cure the inverse-axis collision. It is not admitted as a standard
primitive rebrand. No second literal is needed.

## Limits and authority

The search was targeted, not exhaustive; empty rg output is not novelty
evidence. Broad discovery included irrelevant hits and truncated displays.
No PDF download or private upload occurred. Optional Zotero/Obsidian tools
were unavailable. Project workflow, research-lit, ARS source-verification
discipline and proof-writer directed original-source subtraction,
access-status accounting and self-contained deduction. No generic pipeline,
separate reviewer or API verifier is asserted. All four agent slots were
occupied when checked.

No manuscript, accepted evidence, central state, CSS packet, completed Git
consultation or Git repository was edited. HOLD_EXTERNAL remains unchanged.
