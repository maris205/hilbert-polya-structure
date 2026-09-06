# HVD primary-source scope, deductions, and reproduction contract

2026-09-06 UTC. This is an author-side source audit, not an independent
review or a proof of global novelty. The task uses the repository's
`symbolic-dynamics-research`, `proof-writer`, and `research-lit` workflows.
Optional Zotero/Obsidian tools and the local arXiv helper were unavailable;
the disclosed fallback was direct primary arXiv PDF-body access and
institutional primary copies. No specialist was contacted, no manuscript
was uploaded, and no external release was made. `HOLD_EXTERNAL` remains.

## Actual primary-body access and exact scope

| Source | Material actually read | Scope and deduction |
|---|---|---|
| Luque and Lacasa, *Canonical Horizontal Visibility Graphs are uniquely determined by their degree sequence*, arXiv:1605.05222; journal version EPJ ST 226, 383–389 (2017). [Primary PDF](https://arxiv.org/pdf/1605.05222) | Entire four-page preprint, including canonical definition, canonization limitations, Proposition 1, Theorem 1 and its full decimation proof. | Endpoint maxima and distinct inner heights are hypotheses. Graph reconstruction is static; its degree-decrement decimation is not HVD feedback. Deduct reconstruction completely, but do not transport it to arbitrary ties. |
| Juhnke-Kubitzke, Köhne and Schmidt, *Counting horizontal visibility graphs*, arXiv:2111.02723 (2021 preprint). [Primary PDF](https://arxiv.org/pdf/2111.02723) | Introduction; Section 2 definitions and structural lemmas; Theorem 3.1 and proof; Lemmas 3.3–3.6, Theorem 1.1 proof and Remark 3.7; Figure 6; Section 4 including Theorem 4.1 and the bracketing proof of Theorem 4.4; Section 5. | Distinct-data degree reconstruction does not extend to all tied data: Figure 6 gives the two checked words. At length 7 the paper reports 394 graphs but 391 ordered degree sequences. Its nesting-height realization and arbitrary-HVG enumeration are static, not all-height-word degree-target fibres or autonomous convergence. Deduct those mechanisms and never extrapolate the first-image counts as Schröder numbers. |
| Lacasa and Just, *Visibility graphs and symbolic dynamics*, arXiv:1704.06467; Physica D, DOI 10.1016/j.physd.2018.04.001 (2018). [Primary PDF](https://arxiv.org/pdf/1704.06467) | Introduction, Section II definitions, Section IV setup and its motif-counting limitations, and Section V discussion in the twelve-page preprint. Not a claim to have checked every intermediate motif calculation. | The underlying evolution is the logistic map; HVG degrees symbolize its trajectories. Out-degree partition results and entropy evidence concern that external map. They do not prove iteration of the degree sequence as the next whole input word. The discussion also distinguishes numerical entropy evidence from a generating-partition theorem. |
| Stephen, *Horizon Visibility Graphs and Time Series Merge Trees are Dual*, arXiv:1906.08825 (2019). [Primary PDF](https://arxiv.org/pdf/1906.08825) | Definitions 1–10, Lemmas 3 and 5, Corollary 6, full Theorem 11 proof, Definitions 12–13, Corollary 14 and canonical reconstruction discussion through Corollary 15, pages 1–4. | The edge-weighted path has a merge tree; adding two infinite horizon vertices gives its stated dual. Removing those vertices gives ordinary HVG weak duality. Therefore a proposed HVG/max-tree translation is already owned. This does not recover a unique tree from an arbitrary undirected degree target, nor establish feedback convergence. |
| Stephen, *A Scalable Linear-Time Algorithm for Horizontal Visibility Graph Construction Over Long Sequences*, IEEE Big Data, DOI 10.1109/BigData52589.2021.9671517. [Institutional publication record](https://pureportal.coventry.ac.uk/en/publications/a-scalable-linear-time-algorithm-for-horizontal-visibility-graph-/) and [primary author PDF](https://pure.coventry.ac.uk/ws/portalfiles/portal/53347588/Binder3.pdf) | Institutional metadata; indexed primary-PDF Section II-A discussion and its reference 35. Whole-PDF reopening timed out; no full-paper-read claim. The cited duality result was then checked directly in arXiv:1906.08825. | The dual-tree implementation and merge-tree explanation are additional static neighbors. They receive no new value here. The direct 2019 theorem, rather than an inaccessible proof in this copy, supports the deduction. |

The last two sources were added because max/merge-tree ownership was
explicitly in scope. No thesis or secondary aggregator is used as a
theorem-level substitute. The accessible PDF-body locations above were
read online on 2026-09-06; this directory does not contain frozen copies
of those remote PDFs, and the local manifests do not pretend to pin them.

## Source adapter versus unsupported transfer

The relevant known maps are height word → HVG, HVG → a canonical
realization, and, under the appropriate hypotheses, degree sequence →
HVG. The autonomous map here is their different composition height word
→ ordered undirected degree word, used repeatedly on its own output.
No checked primary theorem supplies that repeated-feedback behavior.
This limited audit is not an assertion that no other relevant paper exists.

The historical [LUB proof](../LUB_PROOF_WORK/PROOF_AND_DISPOSITION.md)
and [LUB source record](../LUB_PROOF_WORK/SOURCE_AND_REPLAY.md) were
read directly. Component-tree reconstruction and height order-polynomial
counting are deducted as generic mechanisms. The HVD path fibre is just
a weak-unimodal-word count, not a second independent novelty unit.
Neither an unevaluated sum over all compatible HVGs nor a sum over
height-order chambers satisfies the requested evaluated inverse gate.

## Reproduction and pin roles

All commands below run from the workspace root
`/root/autodl-tmp/symbolic_dynamics` unless a different cwd is recorded.
The two scientific entry points are
[verify_partial_theorems.py](verify_partial_theorems.py) and
[probe_sentinels.py](probe_sentinels.py).

```text
python -B docs/papers204_208_sequence/scouting/word_local/HVD_PROOF_WORK/verify_partial_theorems.py
python -B docs/papers204_208_sequence/scouting/word_local/HVD_PROOF_WORK/probe_sentinels.py
```

The first canonical is [PARTIAL_CANONICAL.json](PARTIAL_CANONICAL.json),
the complete stdout from the first successful partial-proof execution.
It checks 50,069 literal words at lengths 1–6, the endpoint propositions,
permanent twos, exact active reduction, the low-degree fixed family,
and 21 $(n,N)$ instances of the path-fibre formula with $1\le N\le n\le6$.
The separate [SENTINELS_CANONICAL.json](SENTINELS_CANONICAL.json)
contains the complete stdout from seven assertions on the four named
input sentinels. The partial verifier additionally checks the single
formula-derived length-seven embedding example. These are author tests,
not nonself reviews and not substitutes for deductive proofs.

Fresh second stdout files and actual exit/byte-comparison results are
listed in [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md). A byte-exact claim
there means an actual raw-file `cmp`, not parsed-JSON equivalence.
[INPUTS.sha256](INPUTS.sha256) is workspace-root-relative and pins the
literal module, its `pilot.py` import, inherited canonical, and the LUB
proof/source/verifier/canonical inputs. [SHA256SUMS](SHA256SUMS) is
package-directory-relative and covers every package file except itself.
See [ARTIFACT_AUDIT.md](ARTIFACT_AUDIT.md) for actual closure checks.

Only this `HVD_PROOF_WORK/` directory was edited for this task.
Central indexes, the inherited atlas, historical packages and Git were
not changed. Root may later record the author-side HOLD disposition;
this package does not itself perform that central mutation.
