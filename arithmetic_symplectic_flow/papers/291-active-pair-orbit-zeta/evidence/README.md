# Evidence — same-owner ordinary orbit zeta

Audit ID: `ASFS-AUDIT-20260920-APZ01`.
Candidate ID: `ANG-20260920-APR01` (unchanged 288/289).
Status: `ORDINARY ORBIT ZETA ESTABLISHED; TRACE/FREDHOLM OWNER OPEN — SCOPED ADVANCE / FORK`.

## Exact inputs and reproducible proof method

The original [analytic card](../candidate-card.md), before the appended
outcome, has SHA-256

    76830495c7e32a08de4dc270d620e6144ce307da3d8360b67954e5332464f413

Unchanged mathematical dependencies:

| Input | SHA-256 | Use |
|---|---|---|
| [288 card](../../288-active-pair-residue-flow/candidate-card.md) | cb48100913138d23d66b89e91c0502e5920337cc0c9969f31d33d9cf441fdc78 | Exact owner and separate controls |
| [288 paper](../../288-active-pair-residue-flow/paper.md) | b20fa7e047eabcb036e95b60a6a2255f60bb11419ef9d588df7c5d86d86c78b8 | Complete packets/repeats, countable null basins, root bound |
| [289 card](../../289-active-pair-packet-topology/candidate-card.md) | a7bcac69bc0552bc91f137dfe4739a58c8056140aa6dc3cda4e2c9640206015b | Same-candidate topological scope |
| [289 paper](../../289-active-pair-packet-topology/paper.md) | 857e2a8b5ec91aaddfe759a9a068c0e1de616a37eb763efc692d8b9180181826 | Full-quotient circles and non-Hausdorff result |

The exact proof inputs are ALL primitive circles and repetitions from
those dependencies, not a cutoff list of primes. Reproduction means
following [paper.md](../paper.md): finite positive-time pair bounds;
uniform all-integer majorants on compact subsets of Re s>1;
finite-product unique factorization followed by uniform tails;
harmonic-partial-sum divergence at the absolute boundary; justified
termwise differentiation; and the exact OFF/ON/SHIFTED coefficients.
No scientific code, numerical output, fitted parameter or finite
precision is involved. The variable N in the proof is an arbitrary
integer cutoff with a proved limiting tail, not a sampled experiment.

The [single primary-source topic](source-record.md) supplies only
the standard Dirichlet-series name and classical continuation after
the same-owner identity is proved. It supplies no new source dynamics,
operator, zero evidence or independent justification of our packet list.

## Ownership, controls and review order

Every state, domain, actual arrow, clock and packet remains unchanged.
The unit counting weights and 1/r convention are newly declared scalar
normalizations. Differentiation derives primitive-length coefficients;
these are not asserted to be trace weights. Composite primitives in
the controls retain their own multiplicities, even when their lengths
equal repeats of other circles.

The null returning locus gives a zero indicator on Haar equivalence
classes, not a universal obstruction to analytic or distributional
models. The full quotient stays non-Hausdorff. Stronger naturalness
stays OPEN, including generic zero-set encoding risk. The parallel
[definition-only scout](breadth-note.md) supplied no new rule; its
fixed-source-block question is not a retroactive hard gate.

The [internal review](independent-review.md) records three checkpoints:
raw frozen card and sources before manuscript access; comparison with
the manuscript; and an adverse scope/overclaim audit. Root owns the
manuscript, card, ledgers and integration. The reviewer owns only its
review file. An auxiliary bounded control check is disclosed there.
ARS influenced this freeze and evidence order, not the mathematical
truth of a result. Same-model/shared-context review is not external
peer review, formal verification or independent-error evidence.

The final manuscript has SHA-256

    7dd25c66e30d80a454f0a375c29caacf993280fa85231e82ec5358054ad3f366

The final review has SHA-256

    a1976c01b47231cfc109cd464164edf89d8b1125a80cbdf62d0e3b443640f5c6

The review first compared manuscript hash
044d83beb21fd8b616b2a021f55ad36e9d9253523f3aa213344026199f9a73d3.
Its only requested expansion was the explicit first-nonzero-Dirichlet-term
tail bound in Section 5, now included and checked against the final hash.
This closes the analytic-distinction justification without introducing
new control theorems or rerunning unchanged proof inputs. No outstanding
blocking issue remains in the internal review's stated scope.

Only this new Markdown package and concise registry entries are written.
Old sources/mirrors untouched; 241/242 paused; programme active.
Ordinary scalar T3 alone advances; operator/domain/trace/Fredholm OPEN.
Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
No PDF/LaTeX, commit, upload or publication.

## Verification receipt — 2026-09-20

Root ran a read-only Python check over all eight package Markdown
files and the two new registry entries. Result: **46 package-local
links + 2 new registry links resolved; 7 primary identity/status
records matched; 7 hash locks matched; 0 issues**. Every new Markdown
file decoded as UTF-8, ended in a newline, contained no NUL/tab and
had trailing spaces of only zero or two characters.

The primary identity/status records were paper.md, candidate-card.md,
claim-ledger.md, package README.md, evidence/README.md and both registries.
The expected values were ASFS-AUDIT-20260920-APZ01, ANG-20260920-APR01,
and ORDINARY ORBIT ZETA ESTABLISHED; TRACE/FREDHOLM OWNER OPEN —
SCOPED ADVANCE / FORK. Local inline Markdown targets were resolved
against each file's parent directory; external source reading is
documented separately, not simulated by a filesystem existence check.

The seven byte-level SHA-256 checks bound the original 291 card prefix,
final manuscript, final review and all four 288/289 dependencies above.
The prefix was obtained by splitting at the first newline followed by
`## Appended audit outcome`; the original freeze remains intact.

| Final artifact | Lines | SHA-256 |
|---|---:|---|
| paper.md | 295 | 7dd25c66e30d80a454f0a375c29caacf993280fa85231e82ec5358054ad3f366 |
| candidate-card.md with outcome | 164 | 84e7abac8515301102e7df48f7ed80bcc57ef0a6f14fe4a3ee6ed10f0674ed35 |
| evidence/independent-review.md | 150 | a1976c01b47231cfc109cd464164edf89d8b1125a80cbdf62d0e3b443640f5c6 |

Exact whitespace command, run from the workspace root:

```sh
git diff --check -- readme.md papers/README.md papers/291-active-pair-orbit-zeta
```

Exit zero, no output. The Python check separately covered untracked
Markdown files, which Git diff alone does not inspect. The session
outputs are summarized here; no scientific output file or standalone
validator was created. After this receipt was appended, only its
changed content/whitespace and the scoped Git diff were checked.
These integrity checks do not constitute proof or external peer review.
