# Independent Paper17 Repaired Source-Lock Review

Date: 2026-08-17 UTC

Candidate: `shiftlike_torus_coset_decay_v1`

Final repaired lock: `experiments/source_lock.json`

Article: **Sharp Torus-Coset Decay for Sparse Shift-Like Recurrences:
Constant Anchors and the Exact Zero-Constant Boundary**

## Review identity, temporal fences, and sole-write rule

This is the fresh independent review of the final governance-repaired and
verifiability-clarified Paper17 source lock. I authored none of the 23 bound
inputs and authored no version of the source lock. I began the first repair
audit only after `LOCK REPAIR AUTHOR STOP`. That audit correctly stopped with
zero writes when the synthetic `permission_bundle` digest lacked a
machine-readable construction. I did not inspect the subsequent lock while
its author was working. I crossed the second fence only after the explicit
`LOCK VERIFIABILITY REPAIR STOP` and stable final identity were supplied.

The existing review at this path was independently verified as the declared
stale artifact: SHA-256
`fee84669b07bde73a01b96bb3dfa8edd924798d68688782feb77720d43293356`,
`22540` bytes, `427` LF characters, ending in `SOURCE_LOCK_PASS`. Its effect
was explicitly false because it reviewed a superseded lock and an overbroad
global-immutability rule. This report replaces that stale file at the same
path. It is the sole project-file write made by the repaired-lock review.

I fully reread the applicable `research-review` and `proof-writer`
instructions. No web access, compilation, TeX or bibliography work, CAS,
symbolic engine, scientific computation, code, experiment, parameter scan,
data, result, figure, manuscript, paper plan, release, submission, upload,
external message, or identity action was performed. The only automated work
was read-only strict parsing, canonical serialization, RFC 6901 selection,
hashing, byte/LF counting, path checks, and the required bounded Paper17
inventory.

## Final stable identity and canonical JSON

The final repaired lock independently rehashed to exactly:

- SHA-256:
  `31b7e8d156bfe46f48bbe0fd38fc6d0f7cbd50da1d78eced8eb0d2b9d7ab0c9f`;
- bytes: `53476`; and
- LF count: `1`.

Strict UTF-8 decoding and JSON parsing succeeded with duplicate-object-key and
nonfinite-number rejection. Recursive ascending Unicode-code-point key
sorting, compact separators, `ensure_ascii=false`, `allow_nan=false`, and one
terminal LF reproduced all `53476` bytes exactly. The lock has no BOM, CR,
insignificant whitespace, or second terminal LF. Independent probes rejected
`{"x":1,"x":2}`, `{"x":NaN}`, `{"x":Infinity}`, and
`{"x":-Infinity}`.

The lock does not bind itself. Its self record excludes exactly `bytes` and
`sha256`; the final externally supplied byte count and digest do not occur as
a self identity. Every binding is a unique safe relative path resolving
inside the workspace, and every bound object is a regular non-symlink file
with strict UTF-8 and a terminal LF.

## Exact two-step repair reconstruction

The repair chain was reconstructed in memory rather than trusted from its
narrative.

First, reversing exactly the five declared verifiability-clarification
changes—removing the permission-bundle definition, removing the clarification
ledger, and restoring `closed_repair_ledger.author_state`, `lock_status`, and
`lock_version`—produced byte-for-byte the first repaired lock:

- SHA-256:
  `9933e31b0d7e4677630ee1831bb136eeeec65bf18c30ee06855014a64847e13a`;
- bytes: `51470`; and
- LF count: `1`.

No field outside those five declared clarification/status/version changes was
needed to obtain that identity.

Second, reversing only the first repair's declared governance allowlist
produced byte-for-byte the original lock:

- SHA-256:
  `d72f7381c5b8f7e9513d08d328f1d2f9cef3a9a8978b14e62e2c9c72bc8ce68b`;
- bytes: `40615`; and
- LF count: `1`.

The reverse operation removed only `batch_control_transition_policy`,
`closed_repair_ledger`, and `source_lock_review_state`; removed the declared
21/2 binding-count additions and restored the original mutation sentence;
removed the repair inventory additions; restored the original independent-
review contract; restored the original lifecycle status and author-stop
fields; and restored the original lock status/version. The exact original
identity proves that every theorem, proof obligation, scalar orientation,
citation, score, page gate, anti-claim, permission, zero-science rule,
binding record, and other non-allowlisted byte survived both repairs.

## Seven protected semantic digests

The six direct protected subtrees were compactly serialized with recursive
Unicode key sorting, UTF-8, `ensure_ascii=false`, `allow_nan=false`, and no
terminal LF. Every digest matched:

| Protected object | SHA-256 |
|---|---|
| `anti_claim_lock` | `c6b4badf084c9627d6c70fd0119d93900284f8b87e98bb3b652becec39413694` |
| `binding_ledger` | `83a175746c451feba00e357e21a8d81233085caeb68268a3a924d24d2be892af` |
| `citation_identity_lock` | `11ad0d411c09ce4e23d6ad4a4c9e053ec5a11a4fd3b8a28c4217337aa13afe7d` |
| `proof_obligation_lock` | `76a89591aa21d0cf392023e5de24cd18dfbbfbb5503bea07e104db519a759133` |
| `score_and_page_lock` | `0644c632b2eabb84c03148c1b23b743dba935ebe62f74e5426389530bd6deeb2` |
| `theorem_lock` | `42ee3a53149f9cf17ffb2f387285d34c3fd71635bca919c466349184c6110f12` |

The final clarification makes the seventh digest independently reproducible.
I implemented its RFC 6901 recipe exactly. The output object has precisely
four keys and takes each entire selected subtree:

- `authorization` from `/authorization`;
- `conditional_next_stage` from
  `/lifecycle_authority/after_fresh_source_lock_pass_and_separate_explicit_invocation`;
- `permanently_false_permissions` from
  `/lifecycle_authority/always_false_under_this_lock`; and
- `scientific_execution_lock` from `/scientific_execution_lock`.

Serialization with the embedded options produced exactly `3548` bytes,
`0` LF characters, and SHA-256
`976e109498e162bc23aea465757e6f0eb38f6073a92f558faa5b70392db3a7f1`.
This matches both the definition and protected-digest ledger. All seven
protected semantics pass without an external construction assumption.

## Exact 23 current bindings

Before this replacement write, every binding matched path, bytes, LF,
SHA-256, regular-file status, non-symlink status, strict UTF-8, and terminal
LF. The exact ledger is:

| Category | Path | Bytes | LF | SHA-256 |
|---|---|---:|---:|---|
| Batch | `BATCH_05_IDEA_REPORT.md` | 16273 | 403 | `700ce1a86f0fc1790a7d9aa8f84585ec1032a00ed844bb478c156e63f5ac78b2` |
| Batch | `BATCH_05_STATUS.md` | 9163 | 169 | `00b889c71b1fcbd60ad7831f6b705c6f5c33e109cecf01bb7036aaec7728d092` |
| Paper16 | `papers/16-henon-support-size-torus-escape/experiments/source_lock.json` | 31945 | 1 | `86205b1f4dc12ab71302e9b283021c8085afc16f0cf6b479d9a91738c03041fd` |
| Paper16 | `papers/16-henon-support-size-torus-escape/notes/CITATION_VERIFICATION.md` | 10733 | 205 | `6ec31651060c148d3110856d8709206f60c36ea990b6c433fa9ab0e0944bab24` |
| Paper16 | `papers/16-henon-support-size-torus-escape/notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md` | 23550 | 492 | `f2ede84a5b19ad275b8b396f4f355c86c6b93a69e515ec29691eb29ac0e0172c` |
| Paper16 | `papers/16-henon-support-size-torus-escape/notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 13903 | 360 | `046e2ec16b46e8de903eac950c1df922725c5b16e359f5ed6c45bd28e737dd61` |
| Paper16 | `papers/16-henon-support-size-torus-escape/notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | 14929 | 298 | `f1c55a810008ef920cd421c4578a98c1d91f8feb800d478e285d2807602cd72c` |
| Paper16 | `papers/16-henon-support-size-torus-escape/notes/NOVELTY_ASSESSMENT.md` | 7309 | 117 | `83c9ab497211c7b5cd5d11b7061a292aba4fb258976a01ec8b9216b11226b96b` |
| Paper16 | `papers/16-henon-support-size-torus-escape/notes/PROOF_PACKAGE.md` | 16808 | 704 | `b44c1f164c97fb5d383cbef941fdef88be4e702066e40efcfb18543be0c4bdf8` |
| Paper16 | `papers/16-henon-support-size-torus-escape/notes/RESEARCH_QUESTION.md` | 8319 | 318 | `43b7f965dc04db33c1f00e45880466730d7ee2a25d84f117e91cace71b26a928` |
| Paper16 | `papers/16-henon-support-size-torus-escape/paper/FINAL_RELEASE_MANIFEST.json` | 37020 | 1 | `4bea0b67fff9c547ddc7f19f9147d8e743deac8a5cbe7a6fdc68c33c370b397b` |
| Paper16 | `papers/16-henon-support-size-torus-escape/paper/reviews/final_integrity_review.md` | 25462 | 234 | `e355172b4533011d549453d02ee9939fb2dabc16fef035206ad4911fdf18eb76` |
| Paper17 | `papers/17-shiftlike-torus-coset-decay/experiments/EXPERIMENT_PLAN.md` | 6234 | 140 | `6d3c765e8d9991ccaccbde358fa4c8119003c27201645ac08654d173a1d470f8` |
| Paper17 | `papers/17-shiftlike-torus-coset-decay/experiments/EXPERIMENT_TRACKER.md` | 2465 | 59 | `ef600f790719a402b294bb06229463a62450653f1f662ff635ebcd9ca82d9206` |
| Paper17 | `papers/17-shiftlike-torus-coset-decay/notes/CITATION_VERIFICATION.md` | 10066 | 173 | `28e6bc4d461a876e326c08e2a2481fd9f3b30ea3192ddc6c576185e88f317ddf` |
| Paper17 | `papers/17-shiftlike-torus-coset-decay/notes/CLAIMS_EVIDENCE_MATRIX.md` | 10963 | 83 | `becba75688dc6e77c18a301f37daa34a17328cf54968f3707a6b76ad1774fea9` |
| Paper17 | `papers/17-shiftlike-torus-coset-decay/notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 22043 | 390 | `aa67cb9c507e244095df86390bcfe5799c8919a1b32b99b84e94ee98b8538260` |
| Paper17 | `papers/17-shiftlike-torus-coset-decay/notes/NOVELTY_ASSESSMENT.md` | 10258 | 200 | `d67777768a84199c48170a8eada1c61af10652c81e080c7c341b90629b2c5e29` |
| Paper17 | `papers/17-shiftlike-torus-coset-decay/notes/PROOF_PACKAGE.md` | 30089 | 852 | `a5649bdc97d6853ddfe2716dc5531cf3d4a581fd9e55b4296c9cfe6ccadbcc77` |
| Paper17 | `papers/17-shiftlike-torus-coset-decay/notes/RESEARCH_QUESTION.md` | 13539 | 368 | `894259da46aa6e886af06741c8798503c5d7e8229295a1c76a8f53e399bdc82f` |
| Paper17 | `papers/17-shiftlike-torus-coset-decay/refine-logs/FINAL_PROPOSAL.md` | 8233 | 257 | `f91e41b0af9bf2ede85516f4362ae3880015b16080326d788e268d359c718bc4` |
| Paper17 | `papers/17-shiftlike-torus-coset-decay/refine-logs/INITIAL_PROPOSAL.md` | 6920 | 185 | `7cbf74c1db067b58184055dba18ff3fd0d467141bb3868005715612d108edf14` |
| Paper17 | `papers/17-shiftlike-torus-coset-decay/refine-logs/REVIEW_SUMMARY.md` | 10835 | 208 | `af07dea511210fa75f48db5d580106fd25d7984c3262d9a1f279b5baeab51aa9` |

The counts are exactly two Batch snapshots, ten Paper16 provenance inputs,
ten Paper17 author sources, and one Paper17 independent source-design review.
The 21 non-Batch records are the permanently byte-immutable set. The two Batch
files matched their restored source-lock-time snapshots before this PASS.

## Exact inventory and absent downstream paths

Before replacement, the Paper17 root contained exactly 13 regular files in
exactly three real directories, with zero symlinks and zero other entries:

- `experiments/EXPERIMENT_PLAN.md`;
- `experiments/EXPERIMENT_TRACKER.md`;
- `experiments/source_lock.json`;
- `notes/CITATION_VERIFICATION.md`;
- `notes/CLAIMS_EVIDENCE_MATRIX.md`;
- `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`;
- `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`;
- `notes/NOVELTY_ASSESSMENT.md`;
- `notes/PROOF_PACKAGE.md`;
- `notes/RESEARCH_QUESTION.md`;
- `refine-logs/FINAL_PROPOSAL.md`;
- `refine-logs/INITIAL_PROPOSAL.md`; and
- `refine-logs/REVIEW_SUMMARY.md`.

The directories were exactly `experiments`, `notes`, and `refine-logs`.
The pre-replacement 12 non-lock files totaled the declared `154185` bytes and
`3342` LF characters, including the exact stale-review identity. The `paper`
path was absent, as were every paper plan, bibliography, TeX source,
manuscript, code, data, result, figure, asset, build, and release artifact.
Replacing the review at the same path preserves the exact 13-path and
three-directory set.

## Controlled Batch transition policy

The repaired policy fixes an exact validation split.

Before this replacement PASS, the policy was inactive and required all 23
bindings to match exactly. They did. The prior review's effect was false.

After this PASS, the 21 non-Batch bindings remain permanently byte-identical
to their ledger records. Any drift invalidates the lock. The two Batch
controls may change only after a separate explicit stage invocation and only
under these exact rules:

- `BATCH_05_IDEA_REPORT.md` retains its exact first `16273` bytes and `403`
  LF characters, whose SHA-256 is
  `700ce1a86f0fc1790a7d9aa8f84585ec1032a00ed844bb478c156e63f5ac78b2`.
  Only complete stage addenda may be appended after that byte prefix.
- In `BATCH_05_STATUS.md`, the only replaceable regions are the values and
  continuation lines of the uniquely occurring Material Passport fields
  `Batch status`, `Current gate`, and `Permitted at the current gate`; the
  uniquely selected row whose first cell is `1 / Paper 17`; and complete new
  Activity Log bullets appended after the exact baseline log. All other
  bytes remain immutable.

The structural selectors are unambiguous in the frozen baseline: the three
permitted fields occur once at lines 11, 12, and 19; the Paper17 row occurs
once at line 28; and the Material Passport, Paper Queue, and Activity Log
headings each occur once. The restored status snapshot is exactly `9163`
bytes, `169` LF characters, and SHA-256
`00b889c71b1fcbd60ad7831f6b705c6f5c33e109cecf01bb7036aaec7728d092`.

Every permitted future transition must record the final repaired-lock
identity and this replacement review's postwrite identity and exact
`SOURCE_LOCK_PASS`; identify the separate invocation and stage transition;
remain local-only; and state the exact conditional next-stage authority and
that every other downstream or external permission remains false. A mutation
outside those regions, an incomplete append, a missing identity, or authority
beyond proof-only planning invalidates the lock.

The policy therefore repairs the dashboard deadlock without weakening any
scientific source binding or granting an automatic downstream transition.

## Preserved theorem, proof, citation, and portfolio gates

The exact reconstruction and protected digests establish byte preservation;
the substantive probes were also replayed.

Part A retains

`S(z_1,...,z_k)=(z_2,...,z_k,P(z_(k-nu+1))+a z_1)`

and

`x_(n+k)=P(x_(n+k-nu))+a x_n`.

For `0<=m<=k`, the `m` equations defining `V_m` correspond exactly to
states through time `m`, and every connected torus coset in `V_m` has
dimension at most `k-m`. The constant-plus-two-powers singleton forces the
middle character trivial. The `P(xi)!=0` branch kills endpoints; the zero
branch preserves both the endpoint-copy character relation and scalar
`xi_(n+k)=a xi_n`. The `A_n` pivots and disjoint `B_n` endpoint pairs give
`2m` integrally independent relations. Future generation yields the translated
set `{n-nu mod k:0<=n<m}`, not a rotation orbit, so there is no gcd phase.
The disconnected reduction, scheme sanity, saturated equality subtori for
`a=1,P(1)=0`, free residue `k-1-nu`, and rank-one sharp
`T_(k-1)` family all remain exact.

Part B retains `k=2`, `nu=1`, `c=0` and the full trivial-middle/root-copy
split. Nonlinear monomials close by `(d^2-1)u=0`; supports of size at least
three close by the singleton plus the next equation. For binomial support,
`A`, `B`, and `C` exhaust the partitions. The four nontrivial adjacent words
give `pq`, `q^2`, `p^2`, and `pq`; only `CB` survives and forces lower
exponent `1`. The scalar pairings retain their signs and force exactly
`a=-beta^2`, with the unique geometric coset

`C_d={((delta/beta^2)t^d,t,beta t,delta beta^d t^d):t in G_m}`.

The third label closes by `(d-1)u=0` or `(d^2-1)u=0`. The sharp tuples
remain exactly `(t^d,t,t,t^d)` at resonance, `(t^e,t,2t^e)` for the
nonlinear monomial, and `(t,1,t)` for a chosen multi-support with `P(1)=0`.
Geometric coset existence is not turned into universal arithmetic infinitude.

The Laurent identity remains Michel Laurent, *Inventiones mathematicae* 78
(1984), 299--327, DOI `10.1007/BF01388597`. EuDML `143175` is the journal
record; `182179` is the distinct Bordeaux seminar account. The project uses
only qualitative finite-union-of-cosets structure. The internal bridge still
places arbitrary finite-rank groups, with arbitrary infinite torsion, in the
division hull of a finitely generated subgroup and embeds only the finitely
generated coefficient/generator field into `C`. No effective bound or
embedding of the whole ground field is claimed.

The independent scores remain exactly novelty `8.0`, standalone value `7.6`,
and proof confidence `9.2`, all above `7.5/7.5/9.0`. The credible non-padded
range remains `19.5--22.5` substantive pages, targeting about `22` with
references excluded. All 15 anti-claims are byte-protected: no dimension
claim for `T_m`, universal resonance infinitude, necessary equality
conditions, gcd phase, rotation bookkeeping, monomial no-window claim,
effective Laurent output, standalone novelty for the standard partition,
scope extension, conjugacy-invariant support, finite-generation or bounded-
torsion substitution, Paper16 improvement, global priority, maximal-coset
classification, or height/periodic/effective enumeration claim can enter.

Paper16 remains non-absorbed. It owns the stronger explicit planar anchored
`T_2/T_1` theorem and fully absorbs Paper14's support-one `T_4/T_3` theorem.
Paper17's planar anchored endpoint is only a weaker qualitative shadow. Its
distinct scope is the all-`k,nu,m` dimension law with equality and the exact
zero-anchor planar phase.

## Zero-science and permission firewall

No scientific run, CAS, code, data, result, figure, or external job exists or
is authorized. No computational evidence enters the theorem.

At review time, the transition policy is inactive, the stale review effect is
false, and paper planning is unauthorized. This replacement PASS establishes
only eligibility for a later, separately invoked stage. It does not itself
mutate either Batch file, create `paper/PAPER_PLAN.md`, or authorize a paper
plan. After a separate invocation, the maximum conditional authority is
proof-only `paper/PAPER_PLAN.md` authorship and one fresh independent plan
review requiring `PAPER_PLAN_PASS`.

Bibliography, TeX, manuscript, code, science, data, results, figures, assets,
build, publication, finalization, release, repository push, submission,
upload, public hosting, external messaging, and identity disclosure remain
false. No stage inherits further authority from this verdict.

## Final conjunctive verdict

The final stable identity, strict canonical JSON, self-exclusion, exact
two-step reconstruction, machine-readable permission-bundle recipe, all seven
protected semantic digests, exact 23 current bindings, 21/2 transition split,
safe controlled Batch regions, stale-review replacement state, exact
inventory, absent paper path, theorem and scalar obligations, Laurent bridge,
scores, page range, anti-claims, Paper16 boundary, zero-science record, and
permission firewall all pass. No mathematical, citation, semantic,
canonicalization, binding, inventory, provenance, governance, temporal, or
lifecycle blocker remains.

SOURCE_LOCK_PASS
