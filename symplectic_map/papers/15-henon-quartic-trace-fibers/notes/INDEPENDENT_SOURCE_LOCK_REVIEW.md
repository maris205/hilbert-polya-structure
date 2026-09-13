# Independent Source-Lock Review

Date: 2026-08-17 UTC

Candidate: `henon_quartic_trace_fibers_v1`

Canonical project: `papers/15-henon-quartic-trace-fibers`

## Review identity and authority

I am the fresh source-lock reviewer. I authored none of the nineteen bound
inputs and did not author the lock. Before the explicit `LOCK AUTHOR STOP`, I
reviewed only the nineteen intended inputs and did not open, stat, list, or
inventory `experiments/source_lock.json`. After the stop, the author supplied
the stable lock identity and authorized exactly one fail-closed review.

The only project write made by this review is this report. No code, CAS,
symbolic engine, numerical calculation, parameter scan, experiment, result,
figure, paper plan, manuscript, compilation, submission, upload, or external
release was performed or authorized.

## Binary verdict

All source-lock gates pass with zero mismatch and zero unresolved blocker.

- Verdict: `SOURCE_LOCK_PASS`
- Lock SHA-256:
  `802fc883cde85cd6312e8a31e0728dc01b493c640c8918d9eacc497f44cac7be`
- Lock bytes: `26920`
- Bound inputs excluding the lock: `19`
- Prewrite project inventory: `12` regular files, `3` subdirectories,
  `0` symlinks, and `0` other entry types
- Prewrite twenty-object identity-ledger SHA-256:
  `f2cc02917036cd1512311d752b7ea40ff90d3e86c29617ced64035d6a954aa28`

The passing effect is deliberately narrow: it permits only a separately
invoked proof-only `paper/PAPER_PLAN.md` authoring stage and a fresh independent
paper-plan review. It does not itself start that stage. Every later permission,
including code, scientific execution, results, figures, manuscript drafting,
compilation, finalization, release, submission, and upload, remains false.

## Strict lock and inventory audit

The stable lock matched the author's handoff byte for byte. It has exactly
twenty-two top-level keys, UTF-8 encoding, compact JSON separators, recursively
lexicographic Unicode object-key order, no carriage return, and exactly one
terminal LF. A strict parse rejected duplicate keys and `NaN`, `Infinity`, and
`-Infinity`; four synthetic rejection probes passed. Serializing the parsed
object with the declared recursive ordering and compact separators reproduced
the original 26,920 bytes exactly.

The lock contains neither its own SHA-256 nor its own byte count. Its path is
present only in the inventory and authority fields, never among the nineteen
content bindings. All binding paths are unique, relative, nonempty, free of
`.` and `..` segments, and resolve inside their declared project or workspace
base.

The prewrite tree contained exactly these three subdirectories:

- `experiments`
- `notes`
- `refine-logs`

The twelve regular files were exactly the eleven local bound inputs plus
`experiments/source_lock.json`. There was no unbound regular file. The future
review path was absent. The forbidden `code`, `data`, `figures`, `manuscript`,
`output`, `paper`, `results`, and `source` directories were absent.

## Binding closure

All eleven local and eight upstream bindings matched both their declared byte
counts and SHA-256 identities. The local identities are:

| Path | Bytes | SHA-256 |
|---|---:|---|
| `experiments/EXPERIMENT_PLAN.md` | 8354 | `c30436a0389c88df8f51fe6e226347bfe108aa84b5032841ec0033ffa7a987fb` |
| `experiments/EXPERIMENT_TRACKER.md` | 2955 | `d0e46a2c9a691c33e6f6e523f85367f00e8060c124044e2f011016c0a68f9efb` |
| `notes/CITATION_VERIFICATION.md` | 13630 | `d84f4b523a7fee3e8f5fa8f2c4c898dbf62e3fd9528154fdd991d82c150c3609` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 9343 | `928f0923bbfddd9294508a427bfcbcbd259591cac4c136bd4effb15bd86ed109` |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 12529 | `55789c4a7c62e4577b655399e7fe8247fe641381e50876d6ebad9bce1f0e8b6e` |
| `notes/NOVELTY_ASSESSMENT.md` | 9878 | `c0b7a102d0d63dcb71d58bdbe460e59988fbf303a10f540a0221275fd34c5eb2` |
| `notes/PROOF_PACKAGE.md` | 29436 | `f99d14bc18bd160e5d55e6254e4a2957dda40adbc2a680970506a6ecca5a42ed` |
| `notes/RESEARCH_QUESTION.md` | 8641 | `a287da2bebfa89b02dd7a83d13129e442b51d5780ccbc01c90eca93ad169e082` |
| `refine-logs/FINAL_PROPOSAL.md` | 9331 | `97daded29a79a1b19b828c4704187fa9c70bdac7448382a72b1df8c0f773ab21` |
| `refine-logs/INITIAL_PROPOSAL.md` | 4842 | `043ca69894386ab5040099138780cc6801ba39ff0b088a2ba3f274ef263cb1a0` |
| `refine-logs/REVIEW_SUMMARY.md` | 7112 | `ab479b99e6fbf1b8f66b719df01d8abfbc97da30a8feb1c0fb1b77bab16ac0bb` |

The eight upstream identities are:

| Path | Bytes | SHA-256 |
|---|---:|---|
| `BATCH_04_IDEA_REPORT.md` | 22478 | `9fbf4ce1d5cb2704d5fe392ca50cc84bdb3a182c9ed1138d50670e32871eae3d` |
| `BATCH_04_STATUS.md` | 16762 | `be8de4f088e436722f701eae89a364e72633bc12fc0af9f3bf28b2c9cf52c4d6` |
| `README.md` | 4753 | `0f2a5cdf14e77ad4a9da9beffffaffd6bab790ee12a7f4688321c115a7b9207e` |
| `docs/candidate_registry.md` | 8421 | `39cefe7f8dba897a4ec9ceeec7b78b54d1b926fc33b50dc86f9357d73ae89519` |
| `papers/12-henon-period3-residue/experiments/source_lock.json` | 13816 | `2fa930f697f6040cb16916d2b4dba7ec591a712882c108848e9eecf53608e1c2` |
| `papers/12-henon-period3-residue/notes/PROOF_PACKAGE.md` | 41134 | `36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9` |
| `papers/12-henon-period3-residue/paper/reviews/final_integrity_review.md` | 12597 | `adb2012367a71662d0054424cfed999988b480b919977f0595a6768c526d5aff` |
| `papers/14-henon-four-step-torus-escape/paper/reviews/final_integrity_review.md` | 7429 | `9cfb8b2cb492dc6bea84231a81c8f7b7c698eea5299a357d066339180b14260d` |

## Theorem and formal-cycle audit

The lock accurately freezes one indivisible three-part theorem package.

1. Part A is pure trace: over an algebraically closed characteristic-zero
   field, fixed traces determine
   \(C_f(T)=\det(T-M_{p'}\mid k[x]/(p-(1-a)x))\), the identity
   \(C_f'(1-a)=0\) leaves at most \(d-1\) Jacobian candidates, and the
   quartic count is at most three, never seven. The Jacobian is an output
   candidate and is not supplied to the trace map.
2. Parts B and C are only over \(\mathbb C\), on the single-factor
   monic-centered \(\mathcal H^1_4\) and its finite residual quotient. The
   five root partitions are all bound, and the exact lower non-quasi-finite
   locus is
   \(E=\{a=1,\ p=(x^2-L)^2\}\), with lower trace fiber
   \((0^{\times4},2^{\times12})\) and quotient coordinate \(L^3\).
3. Formal traces through period three have finite geometric fibers and hence
   give a quasi-finite map; period two remains non-quasi-finite. The sharp
   cutoff is three. This is not an injectivity or exact-degree theorem.

The formal-cycle convention is consistent throughout. The period degrees are
4, 12, and 60. On \(a=1\), the full period-two algebra has length 16 and the
embedded formal fixed cycle has length 4. On \(E\), the full
\(f^3\)-fixed algebra has length 64, the formal fixed contribution has length
4 and zero second moment, and formal subtraction leaves pointwise length 60.
Only then is division by three allowed. The locked pointwise and cyclewise
moments are respectively

\[
-1296000-1572864L^3
\quad\text{and}\quad
-432000-524288L^3.
\]

Equality of the full period-three multiset is used only to force equality of
this moment on \(E\); the moment is not promoted to a global classifier.

## P1--P17 conjunctive review

Every proof obligation was present exactly once, in order, with a nonempty
obligation and acceptance rule.

| Gate | Finding | Verdict |
|---|---|---|
| P1 | Field, single-factor source, formal symmetric-product target, and quasi-finite semantics are exact. | PASS |
| P2 | The fixed algebra, \(s=1-a\), \(q=p-sx\), and pure fixed-trace characteristic polynomial are bound. | PASS |
| P3 | Both the squarefree residue and nonreduced local-factor proofs of \(C_f'(s)=0\) are preserved. | PASS |
| P4 | Characteristic zero gives degree \(d-1\); the quartic candidate bound is three. | PASS |
| P5 | Cantat--Dujardin is used only over \(\mathbb C\), at fixed \(a\ne1\), after Jacobian enumeration. | PASS |
| P6 | The length-16 tensor algebra and length-4 formal subtraction give formal period-two length 12. | PASS |
| P7 | Sugiyama is confined to the simple-root \([1111]\) stratum and its \(V_4\) domain. | PASS |
| P8 | The \([31]\) and \([211]\) formulas and finite recovery, including orderings, are preserved. | PASS |
| P9 | Every boundary and the exact \([22]\cup[4]=E\) classification are present. | PASS |
| P10 | The pointwise finite-type criterion gives exactly \(E\) as the lower non-quasi-finite locus. | PASS |
| P11 | Rank 64, cyclic signs, derivative trace, and \(\operatorname{Tr}(M_{t^2})=\operatorname{Res}(t^3)\) are exact. | PASS |
| P12 | The four weight candidates and the two eliminations leave only \(\varepsilon^6\) and \(L^3\varepsilon^4\). | PASS |
| P13 | Both slope ledgers give \(-1572864\), and the constant ledger gives \(-1296000\). | PASS |
| P14 | Fixed-algebra nilpotence, local lengths 2 and 4, length 60, and delayed division by three are separated correctly. | PASS |
| P15 | The \(\mu_3\) quotient, finite geometric fibers, finite type, and sharpness argument are closed. | PASS |
| P16 | Primary-source identities, controlling versions, theorem roles, and bounded-search language match the reviewed source ledger. | PASS |
| P17 | Paper 12 absorption, publication policy, scope limits, and all anti-claims remain closed. | PASS |

## Citation, novelty, and score gates

The controlling citation ledger has eight primary records. The later
Cantat--Dujardin author PDF dated May 10, 2026, with 51 pages, controls over
arXiv v1. Theorem 3.7 supplies no explicit quartic cutoff; Theorem 4.2 retains
its fixed-Jacobian, complex, \(a\ne1\) scope; Example 4.3 is credited for the
known exceptional family and lower-period blindness. Sugiyama I and II remain
restricted to the no-multiple-fixed-point domain. Friedland--Milnor,
Cattani--Dickenstein--Sturmfels, Hutz, Huguin, and the Stacks Project retain
only their stated background or method roles. Mutable web bytes are not bound.

The collision statement is correctly date-bounded to 2026-08-17 and does not
claim priority or absence of unpublished work. The naked cutoff remains
`STOP`; only the strengthened unified package is `GO`. The fresh source-design
scores are novelty 6.8, standalone size 6.4, and proof confidence 9.3, clearing
the frozen thresholds 6.5, 6.0, and 9.0. Scores are lifecycle evidence, not
theorem evidence.

## Anti-claims and Paper 12 absorption

All fourteen anti-claims occur exactly once as A1--A14. They exclude a supplied
Jacobian, injectivity, exact map degree, multifactored or arbitrary-loxodromic
scope, wider field scope for Parts B--C, positive characteristic, reduced-only
periodic data, method or family novelty, all-degree cutoff or universal
nonvanishing, global classification by one moment, computation as evidence,
and absolute priority.

Paper 12 is frozen internal provenance, not a black-box theorem dependency.
Its exceptional-curve classification, formal subtraction, two slope ledgers,
constant ledger, and local-length proof are reproduced inside Paper 15 and
receive no new novelty credit. Any external publication must use the unified
Paper 15 treatment or withdraw the overlapping Paper 12 claim; parallel
overlapping submission is forbidden.

## Lifecycle closure

Before this verdict, every implementation, code, scientific-execution,
result, figure, paper-plan, manuscript, compilation, finalization, release,
submission, and upload permission was false. This report changes only the
next-gate eligibility stated in the lock: under a separate stage invocation,
a proof-only paper plan may be authored and then independently reviewed.

No hidden experiment authority is created by `EXPERIMENT_PLAN.md`; it is a
no-scientific-run proof-audit protocol. No source-design header overrides the
frozen lock; those earlier headers are bound provenance. This review does not
authorize any scientific run, manuscript text, build, release action, or
external communication.

SOURCE_LOCK_PASS
