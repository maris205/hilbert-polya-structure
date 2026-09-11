# Sources and explicit old-mechanism subtraction

Date: 2026-09-08 UTC. Status: bounded negative source desk; no priority claim.
Scientific execution/import/pilot count: zero.

## Primary bindings actually read

| Source | Actual body location used | Deduction allowed |
|---|---|---|
| Holroyd, Levine, Mészáros, Peres, Propp and Wilson, Chip-Firing and Rotor-Routing on Directed Graphs | [arXiv primary PDF](https://arxiv.org/pdf/0801.3306), printed pp. 12–14: Definition 3.1, Lemmas 3.3–3.7, Theorem 3.8; the relevant proof bodies were read | Advance the visited rotor before moving; unicycle restriction is a permutation; strong connectivity yields the recurrent converse |
| Kaiser, Levine and Sava-Huss, Locally Markov walks on finite graphs | [versioned arXiv HTML](https://arxiv.org/html/2412.13766v3), Section 2, Remark 2.1, Definition 2.2 and Assumptions 2.1 | Hidden local state updates before choosing the next location; deterministic local transitions and jumps fit this definition. No later stochastic theorem is imported |
| Manna and Waldinger, The Deductive Synthesis of Imperative LISP Programs, AAAI 1987 | [primary proceedings PDF](https://cdn.aaai.org/AAAI/1987/AAAI87-028.pdf), printed pp. 157–159, especially the in-place reverse program and its listed preconditions on p. 159 | The right-pointer overwrite and two-register advance are an established kernel. The source's terminating-list correctness is not asserted for arbitrary cyclic pointer states |

The external deductions above are narrow. In particular, the rotor source
already supplies the local cyclic-order mechanism on graphs; hidden labels
and repeated outputs do not avoid it when labels are retained as parallel
arcs. The exact full-carrier conjugacy and local predecessor calculation are
spelled out independently in PROOF_PACKAGE.md, not inferred from a title.

For the LISP source, bind its current location to $v$, previous location to
$u$, and right-pointer store to $f$. One nonterminal recursion reads the
old $f(v)$, assigns $f(v):=u$, and advances the locations to $(v,f(v))$
in previous/current order. The desk drops the nil-stop to obtain $R$ on
all labelled pointer states. This distinction prevents attribution of an
unproved all-period theorem to the source.

The [publisher page](https://onlinelibrary.wiley.com/doi/10.1002/rsa.70045)
was also opened for the locally Markov paper. Its numbering differs from
the versioned arXiv rendering: publisher Remark 2.5 / Definition 2.7 /
Assumptions 2.9 correspond to arXiv Remark 2.1 / Definition 2.2 /
Assumptions 2.1. The proof cites the latter version consistently.
The arXiv version stamp is 1 December 2025, while that HTML body displays
24 August 2026. This rendering/version-date discrepancy is retained, not
silently converted into a publication-date or theorem-version assertion.
No exact month of journal publication is needed by this desk.

The 1967 Schorr–Waite pointer algorithm appeared during navigation, but no
controlling original proof body was acquired here; it supplies no premise.
Likewise, secondary aggregators and unrelated graph-walk search hits supply
no theorem or priority evidence.

## Internal literal subtraction from original files

The mirror path was recovered from
[HISTORY_AND_CAVEATS.md](../../../research_state/HISTORY_AND_CAVEATS.md),
not assumed to be the current working directory. No Git command followed.

| Original artifact and read boundary | Exact occupied mechanism | Consequence here |
|---|---|---|
| C181 mirror [THEOREM_PACKAGE.md](/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/henon_rotor_router_strong_digraph_route_a/THEOREM_PACKAGE.md), complete; producer lines 1–175 read as text | Finite strong directed multigraph, distinguished arcs, cyclic outgoing order, chip position; literal advance-then-move implementation | Exact old literal after the state-label/arc bijection. A new graph or repeated-output memory encoding does not create a fresh primitive |
| P117 batch [COMBINATORIAL_SCOUT.md](../../../papers117_121_sequence/scouting/COMBINATORIAL_SCOUT.md), lines 250–306 | C04 bidirected-lollipop rotor walk; C05 rotor-guided local complementation was also already written | Lollipop specialization and adaptive local-complementation variants were not reopened |
| P162 batch [replacement scout](../../../papers162_166_sequence/scouting/replacement_posets_languages/SCOUT.md), lines 1–112 | C04/RTR toggles the visited binary rotor on a four-cycle and moves; already killed as direct rotor routing | Historical finite counts are not a fresh test and cannot rescue the same primitive |
| P82 batch [candidate ledger](../../../papers82_86_sequence/phase1/CANDIDATE_POOL_AND_KILL_LEDGER.md), lines 1–55 | Cyclic single-chip rotor routing already marked internal collision with C181 | Independent historical signpost; the actual C181 literal, not this summary alone, controls |
| P167 [main.tex](../../../../papers/167-minimum-inverse-position-feedback/main.tex), lines 1–165 | Least-preimage selection with identity on missing values; first-image path reversal/splitting is part of its stated result | Ordered endpoint-filter/path reversal is occupied and was not resubmitted. No claim that $R$ is conjugate to P167 is made |
| P209 [setup](../../../../papers/209-ordered-fibre-threading/sections/01_setup.tex) and [recurrence proof](../../../../papers/209-ordered-fibre-threading/sections/02_recurrence.tex), both complete | Ordered fibres are threaded to chains; recurrent feeding-path attachments rotate backwards along vertex cycles | Sibling-to-path threading and its recurrence proof were read directly and not repackaged. This is a different map from the two-register kernel |

The C181 package's old HP Route-A rejection is unrelated to the present
finite-system gate. Its already-used finite map and imported rotor mechanism
remain occupied; that arithmetic verdict does not make the literal fresh.
Its full orbit-count claims were read as old-package claims, but were not
reproved, replayed or promoted as new primary-source deductions here.

### SHA-256 pins measured in the native old-read command

| File | SHA-256 |
|---|---|
| P167 main.tex | 500fdea81499204a92bd3b6e24c5f9fd7b758d29b5c5dcdbf60e5e3f8e861d73 |
| P209 sections/01_setup.tex | 005beb35da0a457bf6c085daf8e294dc8c567d88f3a35b04ca7e88da1dc8374a |
| P209 sections/02_recurrence.tex | f05481b35728034e432a0ace5431eed4a4722ab64377502ff06424fc26955032 |
| C181 THEOREM_PACKAGE.md | 30a4b2c31f6475d4eadeee42bc954992a4b55fec9566a3ef9a5de80ba3848e19 |
| C181 code/c181_rotor_router_producer.py | 584b386b31ad558853ee8a3567d01af00246ec8ab968a829c7e66080fd819a4b |
| P117 COMBINATORIAL_SCOUT.md | a6c82021d9f5c699ca666c1a2a2a54e56cf38d3fd910748ad295501953a91615 |
| P162 replacement_posets_languages/SCOUT.md | 05fe383935587bb71450334751d293bdd6259a07f2fdb60db1050295af85d24d |

These are original-file pins at read time, not a claim that all lines of each
pinned file were read. Ranges above are the actual read boundary.

## Why neither entry survives

For cyclic memory, the whole state and tick are rotor routing, while the
general inverse formula only solves the changed local coordinate. A source
recurrent theorem plus such an overwrite count does not constitute two new
independent mechanisms.

For unary pointer reversal, the source owns the operational kernel and the
autonomous completion is directly reversible by swapping back the overwritten
field. Its unit fibres, elementary fixed census and static edge invariant do
not provide a demonstrated paper-sized conjunction. No periodic-orbit census
beyond fixed states was derived or empirically inferred. This is a thin
remainder rejection, not a claim that the source already classifies all
autonomous pointer orbits.

General noncyclic local memory remains outside this negative statement.
A genuinely different specific update would need its own literal contract,
source subtraction and nontrivial temporal plus independent second mechanism.
No such extra candidate was generated to fill this desk's quota.

## Retrieval and read-record honesty

The six web calls and selected local native records are preserved in the
two JSON files linked from HANDOFF.md. These records distinguish navigation,
actual primary reads and historical claims. The web record contains requests,
native metadata and URLs, not a full primary-text redistribution. No source
PDF was downloaded into this desk, and no source-body file hash is claimed.

A local helper lookup and a guessed old firewall path returned errors.
They remain in the native records; existing original files and direct
primary web retrieval provided the stated fallback. A separate broad old
scout read produced a truncated output and is not used as a full-read premise
or included among the controlling complete native records.

Search coverage is bounded. Search hits or missing names are not treated as
novelty evidence. Root's pre-execution approval gate remains closed because
there is no proposed survivor to execute.

