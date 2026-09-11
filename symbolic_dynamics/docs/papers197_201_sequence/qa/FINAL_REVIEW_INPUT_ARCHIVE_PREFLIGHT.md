# Final review-input archive preflight

Date: 2026-09-05 UTC; final local checks at 09:13:43 UTC.
Status: **ALL_REFERENCED_INPUT_BYTES_ALREADY_ARCHIVED**.

This is a bounded read-only Git-object dependency check, not a mathematical
review, manuscript acceptance, verifier replay or complete final-release audit.
The checking process authored P202 and co-contributed P203; this task does not
claim independent scientific review of either manuscript.

## Fixed baseline and actual method

- Git commit: `9a394ee2c3ab171ba4341d77c439ba145e247a85`.
- Mirror: `/root/autodl-tmp/hilbert-polya-structure`.
- Workspace: `/root/autodl-tmp/symbolic_dynamics`.
- Inputs: the ten `reviews/p{197,199,200,202,203}_{a,b}/PINNED_INPUTS.sha256` files.

A fresh read-only process parsed each actual pin list, normalized the ten
absolute workspace paths in P200 B back to their workspace-relative paths,
and computed the actual workspace file hashes. It enumerated the fixed Git
tree and read raw blobs with `git cat-file --batch`; archived bytes were
compared directly with workspace bytes and the pinned SHA-256.

The established split mirror layout was applied explicitly: papers numbered
at most186 and the referenced older batch-doc directories are stored under
`symbolic_dynamics/` in Git; current papers/docs remain at the repository
root. This was a path mapping, not a content-search substitution or pin edit.

## Actual outcome

| Review | Referenced inputs | Exact workspace / pin / Git match |
|---|---:|---:|
| p197_a | 18 | 18 |
| p197_b | 19 | 19 |
| p199_a | 16 | 16 |
| p199_b | 13 | 13 |
| p200_a | 13 | 13 |
| p200_b | 10 | 10 |
| p202_a | 13 | 13 |
| p202_b | 13 | 13 |
| p203_a | 28 | 28 |
| p203_b | 52 | 52 |
| **Total references** | **195** | **195** |

There are **150 distinct referenced paths**. All are physically present,
match their pinned version, and are already represented by equal raw bytes
in the fixed commit. Conflicting pins for the same path: **0**.

- Missing old/historical archived dependency: **0**.
- Old/historical Git-version mismatch: **0**.
- Workspace missing or pin-version mismatch: **0**.
- Referenced current P203 input not yet in the fixed commit: **0**.
- Direct-root mappings: **164 reference rows**.
- Historical-prefix mappings: **31 reference rows, 16 distinct paths**.

Thus this dependency preflight identifies **no additional old evidence file
that must be rescued or backfilled for the final ten review input lists**.

## What still needs the next backup

The first nine pin-list files themselves match their fixed Git blobs.
P203 B's newly frozen pin-list file is absent from this baseline, as expected:

- B `PINNED_INPUTS.sha256`:
  `ae80421d6ce5c31ac73334fea74ed787ac663f9fe76089dfe4e1f49133f6c061`.
- Observed B top `SHA256SUMS`:
  `e54fa5e086c7e2f79c495cb2c3591cca311c6dbe59d0a1d99d9090f3fc18a888`.

B's **52 referenced input files are all already archived**; that does not
mean B's own new report, verifier, canonical output, QA or manifest is
already committed. The complete new B package and later P203 Round2/terminal
artifacts still belong in root's subsequent scoped backup. This preflight
does not enumerate or certify future terminal files, repeat the full B
package audit, or establish five-paper completion.

## Historical pin-list boundary

One referenced input is
`papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/HISTORICAL_TEMPORAL_INPUT_PINS.sha256`.
It was hashed as a literal document only; its internal targets were **not**
recursively executed. Its document bytes matching Git do not repair or
reclassify the preserved historical temporal **3 PASS / 1 failed old-code
pin**. No unavailable program was reconstructed or substituted.

## Non-mutation and scope

Before and after the actual process, HEAD and local `origin/main` remained
9a394. The sole dirty mirror path was root-owned
`symbolic_dynamics/README.md`, unchanged at SHA-256
`d2c8d1604fc177322066cee7d486db659cba5475a4ca185500871a338eb5245a`.
No Git state, accepted research file, frozen pin, manuscript, review,
manifest, central index or earlier audit receipt was changed. Only this new
preflight record was written. No fetch or push was performed; local tracking
refs are not an independent remote-server check.

The result is limited to the union of these 195 review input references.
It is not a claim that every historical paper or transitive old dependency
has been synchronized.

## Explicit historical path mappings

| Workspace-root-relative path | Actual fixed Git path |
|---|---|
| `docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md` | `symbolic_dynamics/docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md` |
| `docs/papers147_151_sequence/scouting/combinatorial/verify_combinatorial_scout.py` | `symbolic_dynamics/docs/papers147_151_sequence/scouting/combinatorial/verify_combinatorial_scout.py` |
| `docs/papers157_161_sequence/scouting/replacement_probabilistic_geometric/SCOUT.md` | `symbolic_dynamics/docs/papers157_161_sequence/scouting/replacement_probabilistic_geometric/SCOUT.md` |
| `docs/papers182_186_sequence/scouting/root_coordinator/SCOUT_AND_KILL_LEDGER.md` | `symbolic_dynamics/docs/papers182_186_sequence/scouting/root_coordinator/SCOUT_AND_KILL_LEDGER.md` |
| `papers/112-tournament-score-upset-reversal/main.tex` | `symbolic_dynamics/papers/112-tournament-score-upset-reversal/main.tex` |
| `papers/117-odd-run-reversal-cyclic-words/main.tex` | `symbolic_dynamics/papers/117-odd-run-reversal-cyclic-words/main.tex` |
| `papers/123-odd-component-complementation/main.tex` | `symbolic_dynamics/papers/123-odd-component-complementation/main.tex` |
| `papers/148-even-level-plane-tree-contraction/main.tex` | `symbolic_dynamics/papers/148-even-level-plane-tree-contraction/main.tex` |
| `papers/149-iterated-endpoint-peak-extraction/main.tex` | `symbolic_dynamics/papers/149-iterated-endpoint-peak-extraction/main.tex` |
| `papers/152-triad-dynamics-triangular-books/main.tex` | `symbolic_dynamics/papers/152-triad-dynamics-triangular-books/main.tex` |
| `papers/164-cyclic-equality-feedback/main.tex` | `symbolic_dynamics/papers/164-cyclic-equality-feedback/main.tex` |
| `papers/169-successor-transfer-set-partitions/main.tex` | `symbolic_dynamics/papers/169-successor-transfer-set-partitions/main.tex` |
| `papers/179-random-singleton-isolation/main.tex` | `symbolic_dynamics/papers/179-random-singleton-isolation/main.tex` |
| `papers/181-first-descent-prefix-reversal/main.tex` | `symbolic_dynamics/papers/181-first-descent-prefix-reversal/main.tex` |
| `papers/182-cyclic-subspace-lattice-comparator/main.tex` | `symbolic_dynamics/papers/182-cyclic-subspace-lattice-comparator/main.tex` |
| `papers/90-rule184-particle-periodic-zeta/main.tex` | `symbolic_dynamics/papers/90-rule184-particle-periodic-zeta/main.tex` |

## Pin-list file observations

| Review | Workspace SHA-256 | Pin-list itself in fixed commit? |
|---|---|---|
| p197_a | `bd1950d372a9542b4cf189b6eab4ebd7cb2db1396425b1e375753a7282e9c21c` | Yes, byte-identical |
| p197_b | `9c7424a8806f1c8d91ce8492576b1a6b789df88ccd8e5bd7153d24105827e362` | Yes, byte-identical |
| p199_a | `292d9732223291a3eb7ba3ebd4e4f8b31c43e41f668718b9c1aed2838585778d` | Yes, byte-identical |
| p199_b | `06bc8b28359e3f9ccdeb373f59bccffa36e2fe34b0d92e2a01b1dd95518166ef` | Yes, byte-identical |
| p200_a | `0c80f409f67af4c8d8d9adaae8396cb086cd3fb68ac87074e9e99932599d8e28` | Yes, byte-identical |
| p200_b | `da398c8318737e8b4bea7156575be07b2e355d15fa2bbe92d4650daa1a59612b` | Yes, byte-identical |
| p202_a | `5852bb6a4ca969f02e7775e384b1056627f3f56d31a4156e0954c106c9d6dc47` | Yes, byte-identical |
| p202_b | `079bd772b09fb5b4a818a5d8498cd385618e0679d7b1906e67503c7f0e638027` | Yes, byte-identical |
| p203_a | `0c68645e0cff44f20b269c826041169eca243a85a8c3a1600585aed80fe18e66` | Yes, byte-identical |
| p203_b | `ae80421d6ce5c31ac73334fea74ed787ac663f9fe76089dfe4e1f49133f6c061` | No, expected new B package |

## Per-input evidence (150 unique files)

Every row below has independently observed workspace SHA = pinned SHA =
raw Git-blob SHA and exact byte equality. `References` gives review and
one-based row in its pin list. The Git OID is the actual fixed-tree blob OID.

```tsv
workspace_path	actual_git_path	sha256_all_three_equal	git_blob_oid	references
docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md	symbolic_dynamics/docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md	371c740e6c2ab99db9aa2f3c429b0b32a4a4af94bd5b11255eba892c379d2cd3	cd21731dfb545b26bcbe97bfb9183f09e656724d	p203_a:23,p203_b:1
docs/papers147_151_sequence/scouting/combinatorial/verify_combinatorial_scout.py	symbolic_dynamics/docs/papers147_151_sequence/scouting/combinatorial/verify_combinatorial_scout.py	7cd3b3b4e91d3469c04131127ee81b7186f350c73cfbb5dacd5e7eb742412e5a	db97026756c7c972a7bfe4b2b72c49a9673c2aac	p203_b:2
docs/papers157_161_sequence/scouting/replacement_probabilistic_geometric/SCOUT.md	symbolic_dynamics/docs/papers157_161_sequence/scouting/replacement_probabilistic_geometric/SCOUT.md	287a397b484ff5eecce098a01114c50c0e0bd5ffb265100a3339c88ff125a8c1	2acdabf7e5a0654742e186106582d3e75dd8d738	p200_a:10
docs/papers182_186_sequence/scouting/root_coordinator/SCOUT_AND_KILL_LEDGER.md	symbolic_dynamics/docs/papers182_186_sequence/scouting/root_coordinator/SCOUT_AND_KILL_LEDGER.md	d54cbec0e9a8606ec646b5733467a7e4245e0951582c5dc06d78d2d43f3659f3	95a89b86595d22fcbb8620c9ac05a41786b0944b	p199_a:13
docs/papers197_201_sequence/FIVE_SEAT_FREEZE.md	docs/papers197_201_sequence/FIVE_SEAT_FREEZE.md	0bd658edf0aa9b2f38d117bfc8d0ff65c0459e674755c086d44fe2bc593f09b2	b4b31b32eadde74237795c831ea1cb8807ff8788	p197_a:8
docs/papers197_201_sequence/HOSTILE_REVIEW_PROTOCOL.md	docs/papers197_201_sequence/HOSTILE_REVIEW_PROTOCOL.md	60c1031ce5cfa5de988791e00c2d58496d82595c6f11183868de6fadb33314ed	ddac29ad9433b98bf238ae219749d22eacde4bd6	p197_a:7,p197_b:17,p199_a:15,p199_b:11,p200_a:6,p200_b:8,p202_a:6,p202_b:7,p203_a:14,p203_b:3
docs/papers197_201_sequence/LFCTR_HISTORY_COUNT_CORRECTION.md	docs/papers197_201_sequence/LFCTR_HISTORY_COUNT_CORRECTION.md	e07f6e7e110397033157ba409c548cc5bbfdbced7169b91042cba4d530215352	9bb339eecb7bc07128fd88d40fca7c99a376c467	p203_a:24
docs/papers197_201_sequence/OR_ROOT_ADJUDICATION.md	docs/papers197_201_sequence/OR_ROOT_ADJUDICATION.md	8589d0e372d24da641c96a193f5886069836531086e5d60f0926acb90739484d	cf3503240b8680d9d0d80652a6e29054b016498e	p202_a:8,p202_b:8
docs/papers197_201_sequence/PROBLEM_ANCHOR.md	docs/papers197_201_sequence/PROBLEM_ANCHOR.md	4c02a736cb9ebca544b05ca94a9bf621b244780f95a4f5651a0a62600003f91e	aad20f3517d5cfa095da4854059582bc539e6fe5	p197_b:18,p199_a:14,p199_b:12,p200_a:7,p200_b:9,p202_a:7,p202_b:6,p203_a:13
docs/papers197_201_sequence/qa/review_cold_build.sh	docs/papers197_201_sequence/qa/review_cold_build.sh	944e0efa5c4047d101f9e6d3797e601ca74114b3ee4015f284a01ea25d12aa97	a84e2c894de11439b3757139d99784e749c680bb	p200_b:10,p202_b:13,p203_a:12,p203_b:4
docs/papers197_201_sequence/reviews/mct_stage1_20260905/SHA256SUMS	docs/papers197_201_sequence/reviews/mct_stage1_20260905/SHA256SUMS	d018b994d4caa8cd5157a0ccdfe453b69baa160f05fa58eb1856e0361a85b4b5	5c0ae49f269db844f8b978ed75fe37d30943e9c7	p203_b:5
docs/papers197_201_sequence/reviews/mct_stage1_20260905/verify_independent.py	docs/papers197_201_sequence/reviews/mct_stage1_20260905/verify_independent.py	d2b69d2991681ff3105ccd90d9a5ed0930808ebe005e447a90de3ccce3f39013	12e78f840a68bc0c72ef2e23f3a53b010af0d360	p203_b:6
docs/papers197_201_sequence/reviews/p197_a/DELTA.md	docs/papers197_201_sequence/reviews/p197_a/DELTA.md	39c8a62095f4489377c4017ea51c3454eab18de9e42f056359cf3a96709c7e92	28dd599bd529308e1c93125de9d6a8d6da592993	p197_b:8
docs/papers197_201_sequence/reviews/p197_a/REVIEW_A.md	docs/papers197_201_sequence/reviews/p197_a/REVIEW_A.md	138d585412d6ccf241dd11510942b4860b06b175c83854e4923c738ece351220	e14e7c15d2f01595f09e6d288602c67b1ba46efd	p197_b:7
docs/papers197_201_sequence/reviews/p199_a/REVIEW_A.md	docs/papers197_201_sequence/reviews/p199_a/REVIEW_A.md	7eb59117ab53f83a57e022ff7dd21b1b9df8a221116a437f46ce1e7c3052b4bf	ad6e180a94ff8f0635267f37181eb9864c171e11	p199_b:7
docs/papers197_201_sequence/reviews/p199_a/SOURCE_OWNER_AUDIT.md	docs/papers197_201_sequence/reviews/p199_a/SOURCE_OWNER_AUDIT.md	6da4f79b70a8df04b996813a37df42dcfecee0d4d0a45fb6e4eeb7ccc2cb968f	dca805a575548c91fa08700a6480d4b48129f60c	p199_b:8
docs/papers197_201_sequence/reviews/p202_a/SHA256SUMS	docs/papers197_201_sequence/reviews/p202_a/SHA256SUMS	86b0fb8025912c12536b2fcb048729a430f98726a1ffa321f89b6d24cc7426f0	f181c1e285a2e0b5bc4d55ef6e56f4f0d54588d0	p202_b:5
docs/papers197_201_sequence/reviews/p203_a/DELTA.md	docs/papers197_201_sequence/reviews/p203_a/DELTA.md	4a672d4791010204f71597fac430c566c9b86e895540233f063e32ea73c33168	6c2df5405c56e4846d7ecc8bd9d717bf46bd0f46	p203_b:7
docs/papers197_201_sequence/reviews/p203_a/SHA256SUMS	docs/papers197_201_sequence/reviews/p203_a/SHA256SUMS	0299cf848039e58e1847a808c22362892d90e1eed88a1ae1becc761303789cfa	cf956d1b9327d4d6abc858685802a81892936648	p203_b:8
docs/papers197_201_sequence/scouting/lfas_reentry_20260905/SOURCE_AND_COLLISION.md	docs/papers197_201_sequence/scouting/lfas_reentry_20260905/SOURCE_AND_COLLISION.md	bd8efa8e4f64d9d136cc59fb3138f2fd05e6772383d5499f8d878cfcf1c3de0c	de73329bc78ee525e4f167861e774012ea9700ff	p200_a:9
docs/papers197_201_sequence/scouting/lfas_reentry_20260905/THEOREM_CONTRACT_AND_PROOF.md	docs/papers197_201_sequence/scouting/lfas_reentry_20260905/THEOREM_CONTRACT_AND_PROOF.md	86005efbe22159d5f1ae33b0636de1432bec66c9e7ef7732123fc56712772730	df0110e3488409eac92e8adb60c94a601fa93cea	p200_a:8
docs/papers197_201_sequence/scouting/replacement_lane/BREADTH_AND_KILL_LEDGER.md	docs/papers197_201_sequence/scouting/replacement_lane/BREADTH_AND_KILL_LEDGER.md	69945ad419514ee7eaa97a1db2b9100174f4c250f2341c569fc71998b6f67df0	021b135f01059f336995f78b91cee0df6217ac86	p203_b:9
docs/papers197_201_sequence/scouting/replacement_lane/verify_replacement_lane.py	docs/papers197_201_sequence/scouting/replacement_lane/verify_replacement_lane.py	e10b759ae5d1a755873bde7326b3f475029885ab138e43645c93495f7ee1187b	31a6811775755929b29cd66125377384c1382a99	p203_b:10
docs/papers197_201_sequence/scouting/word_poset_lane/TCSD_EXACT_GAP_PROOF.md	docs/papers197_201_sequence/scouting/word_poset_lane/TCSD_EXACT_GAP_PROOF.md	b7d72803db3638e6f8389a582cbf5b8562a4e8f411b2e8609e611929bea19180	82d390302aa1e6c527c19aba34ac3ebeb9862ef2	p197_a:10
docs/papers197_201_sequence/scouting/word_poset_lane/TCSD_SHARP_WITNESS_SUPPLEMENT.md	docs/papers197_201_sequence/scouting/word_poset_lane/TCSD_SHARP_WITNESS_SUPPLEMENT.md	f574d0260b1da8e7cea9687370f8c52574a3bba474e02a9e11dcd329f47cf6b4	f0625355278b032b919c619fc169545828d09b0d	p197_a:11
docs/papers197_201_sequence/scouting/word_poset_lane/TCSD_SMALL_WITNESS_ERRATUM.md	docs/papers197_201_sequence/scouting/word_poset_lane/TCSD_SMALL_WITNESS_ERRATUM.md	83f6ee2c6c1989dc204853e5216671a41477eff594f01e456749edefc8c08a85	5af43b7df4558f1ed90f97c78488ef66c17acce3	p197_a:9
docs/research_state/HISTORY_AND_CAVEATS.md	docs/research_state/HISTORY_AND_CAVEATS.md	ee6152b209cf6a655392f1f175aa7e9e63f9a8ab4fd8d9dba4a8991f5fc89d95	ad3db313b6fd04d5bdc7eccf61b87545933c8468	p197_b:19,p199_a:16,p199_b:13,p202_a:9,p203_a:15
papers/112-tournament-score-upset-reversal/main.tex	symbolic_dynamics/papers/112-tournament-score-upset-reversal/main.tex	ef4ac3d6efcc2dba4c40c39e0261b1c12d75906f6d035633cad01a52b40d301c	b5af87c604fe339744b5191802626d69400798d8	p203_a:25,p203_b:11
papers/117-odd-run-reversal-cyclic-words/main.tex	symbolic_dynamics/papers/117-odd-run-reversal-cyclic-words/main.tex	61e9d0ee7af6491a93e713dfa57707ec739609438ec8029d8115eb9e7a064053	974ca5648d558585300cb72c66070922eab70f0b	p197_a:14,p197_b:11
papers/123-odd-component-complementation/main.tex	symbolic_dynamics/papers/123-odd-component-complementation/main.tex	15e8193ad8568199aa3b08c13df1e2c61231b6b3ef13ef33fe804c4eb1d3ddb7	e3bada21cc25793c72cb04eb12943cb44ac89a6a	p203_a:26,p203_b:12
papers/148-even-level-plane-tree-contraction/main.tex	symbolic_dynamics/papers/148-even-level-plane-tree-contraction/main.tex	d48b8c37f66c16795474765c9fe328493c8c6888af9abe3a848512ea803ce3f6	a0c72ac4190ddf194f615aa32f52bfd61fb60e3f	p199_a:11,p199_b:9
papers/149-iterated-endpoint-peak-extraction/main.tex	symbolic_dynamics/papers/149-iterated-endpoint-peak-extraction/main.tex	a8e4699d6935c4ce086de311e9324da705fac709d10d9db27fcfa244194c7746	2cfef3efd4054935d35436aa723c552cf29d84e3	p197_a:18,p197_b:15
papers/152-triad-dynamics-triangular-books/main.tex	symbolic_dynamics/papers/152-triad-dynamics-triangular-books/main.tex	442d06a74281ce79f2e845ceb656035b5a1c7ae54c4ee2afe69927aa269f196e	9b65e10bfcbd3ed7944f68c3d76135c360bf0d43	p203_a:27,p203_b:13
papers/164-cyclic-equality-feedback/main.tex	symbolic_dynamics/papers/164-cyclic-equality-feedback/main.tex	6a589c778137cb6e039f7a01710e7264686c6952321f0494ee3c992bfcda4218	47a64c36b6275c3351aa6b77bb2733ab5d27e828	p197_a:12,p197_b:9,p202_a:12,p202_b:11
papers/169-successor-transfer-set-partitions/main.tex	symbolic_dynamics/papers/169-successor-transfer-set-partitions/main.tex	0344686ca5f9334f7dd72aaced7cd81b3380c55a5365f534696a47d9a93c3cbb	fd2e196a8d06faf8c8e89f6d0ad5403f79b16ad2	p202_a:11,p202_b:10
papers/179-random-singleton-isolation/main.tex	symbolic_dynamics/papers/179-random-singleton-isolation/main.tex	94ff9a5e84d50473b9c48afeb79098bd83cec1e848612e18b71b0b24ac03bbb6	810942958ef7abe81249b2e41a90dd16e3051c94	p199_a:12,p199_b:10
papers/181-first-descent-prefix-reversal/main.tex	symbolic_dynamics/papers/181-first-descent-prefix-reversal/main.tex	95909031cae2c75f09399452a472597e72a1bf3a91d10cf4286df54e54e2fb82	9f95357afe85bfb6ee1349222f80516c5cd61647	p200_a:11
papers/182-cyclic-subspace-lattice-comparator/main.tex	symbolic_dynamics/papers/182-cyclic-subspace-lattice-comparator/main.tex	9d496bf69fc3d7426c1f95bb7bacdaf0ea0cd6c7e3b36c5d3c55f64236f088c7	e78c0bd1a92146e971e6a0b386434aabcddcaf59	p197_b:16
papers/187-cyclic-divisor-quotient/main.tex	papers/187-cyclic-divisor-quotient/main.tex	e4dd2c5afb6381563476c6b6735f94c932403492165b8f21adeee6a448f7b83d	e5268d8e162b6b6538d9279334618663fd03a839	p197_a:15,p197_b:12
papers/190-brandt-sandwich-erosion/main.tex	papers/190-brandt-sandwich-erosion/main.tex	73cb3d23aa88247ecbc22a75651f48f94aaf94113ccb649b1f13d64f9c37d300	753981949de1a26ff6ae537c9368962592d23b00	p197_a:16,p197_b:13
papers/192-first-collision-hurwitz/main.tex	papers/192-first-collision-hurwitz/main.tex	30cd2c9bc853d9b195f89527db4794681e4d3dcacd8c45f5aea0b49a98ab12f9	a15ebc40e47a7d31908fa6df16ea8e7fd243463b	p200_a:12
papers/194-least-raising-crystal-words/main.tex	papers/194-least-raising-crystal-words/main.tex	d4c81d389dba055a3a232077e79058c09cae1be40b8822d49f976c4242d97ce9	e089a0f14ac966f26ba16c148db52237335951f6	p200_a:13
papers/196-cyclic-godel-implication/main.tex	papers/196-cyclic-godel-implication/main.tex	06cb66f5c784fe7521d4fe7a5777b8490e4f73f41ba968167f8ce58dbd54a97e	65fb518fb6bf6d8f0352070234b7a96e724a3eac	p197_a:17,p197_b:14,p202_a:13,p202_b:12
papers/197-ternary-cyclic-sign-difference/ROUND0_RECEIPT.md	papers/197-ternary-cyclic-sign-difference/ROUND0_RECEIPT.md	42d228553c614c1d763ac525d3c4ce7ef7560d452058f7cf5da7bead36134628	4a1643f6135fbbda93248de42b19f72d9899ec86	p197_a:6
papers/197-ternary-cyclic-sign-difference/ROUND1_RECEIPT.md	papers/197-ternary-cyclic-sign-difference/ROUND1_RECEIPT.md	e1ef35fda1b5bc467bbf67481cc3c9348c07d44a65179e01ba7ec7144589368d	268dbb8531a990b1452a4c5bc8ee011f6cccff32	p197_b:6
papers/197-ternary-cyclic-sign-difference/frozen_round0/code/CANONICAL.txt	papers/197-ternary-cyclic-sign-difference/frozen_round0/code/CANONICAL.txt	54d09ba740900f49fdd045c9aae3b3fbe4f0cf2bc6cbbee3fe92f7f98a77d5d1	69d8b462edeffa72fa6474c0d236f9a1ff056741	p197_a:4
papers/197-ternary-cyclic-sign-difference/frozen_round0/code/verify.py	papers/197-ternary-cyclic-sign-difference/frozen_round0/code/verify.py	2dde93e3e8c8b4c85f23ceb476d1cddd63a8f477c5c11d2cb59ee4f6e16b1e27	89724dca1ddaeecf0f01bac1fce25aac7b045205	p197_a:3
papers/197-ternary-cyclic-sign-difference/frozen_round0/main.tex	papers/197-ternary-cyclic-sign-difference/frozen_round0/main.tex	3958fd63a7a7487bceb9720fb140426651d27fb51bab79dc03a30286eb4deda0	1fb6fc0d75e4a01dd27c28afe610d4fa6a549389	p197_a:1
papers/197-ternary-cyclic-sign-difference/frozen_round0/references.bib	papers/197-ternary-cyclic-sign-difference/frozen_round0/references.bib	56fff92afda7b377cab2a340e5b41cb245c147e965d6e691102a2e25ae15937b	46f35c890e8f74f356217334bbc82d8d1e7b3a23	p197_a:2
papers/197-ternary-cyclic-sign-difference/frozen_round1/code/CANONICAL.txt	papers/197-ternary-cyclic-sign-difference/frozen_round1/code/CANONICAL.txt	54d09ba740900f49fdd045c9aae3b3fbe4f0cf2bc6cbbee3fe92f7f98a77d5d1	69d8b462edeffa72fa6474c0d236f9a1ff056741	p197_b:4
papers/197-ternary-cyclic-sign-difference/frozen_round1/code/verify.py	papers/197-ternary-cyclic-sign-difference/frozen_round1/code/verify.py	2dde93e3e8c8b4c85f23ceb476d1cddd63a8f477c5c11d2cb59ee4f6e16b1e27	89724dca1ddaeecf0f01bac1fce25aac7b045205	p197_b:3
papers/197-ternary-cyclic-sign-difference/frozen_round1/main.tex	papers/197-ternary-cyclic-sign-difference/frozen_round1/main.tex	3958fd63a7a7487bceb9720fb140426651d27fb51bab79dc03a30286eb4deda0	1fb6fc0d75e4a01dd27c28afe610d4fa6a549389	p197_b:1
papers/197-ternary-cyclic-sign-difference/frozen_round1/references.bib	papers/197-ternary-cyclic-sign-difference/frozen_round1/references.bib	56fff92afda7b377cab2a340e5b41cb245c147e965d6e691102a2e25ae15937b	46f35c890e8f74f356217334bbc82d8d1e7b3a23	p197_b:2
papers/197-ternary-cyclic-sign-difference/main_round0_original.pdf	papers/197-ternary-cyclic-sign-difference/main_round0_original.pdf	42cb9e1e7cd10858a7ecf98faf2d8ced79faeb31211f608fd20f4b75a01b792a	5b35e6650b12971bc963728b5056173cfd5b2c84	p197_a:5
papers/197-ternary-cyclic-sign-difference/main_round1.pdf	papers/197-ternary-cyclic-sign-difference/main_round1.pdf	42cb9e1e7cd10858a7ecf98faf2d8ced79faeb31211f608fd20f4b75a01b792a	5b35e6650b12971bc963728b5056173cfd5b2c84	p197_b:5
papers/199-first-one-stirling-splice/ROUND1_RECEIPT.md	papers/199-first-one-stirling-splice/ROUND1_RECEIPT.md	058cdb5df1d51b54332b97200961444b7e1ffef2b2824bcbbd1aac04aa8fcc9c	1c001bc76df8e001a36d062131294099ca6fe55c	p199_b:6
papers/199-first-one-stirling-splice/frozen_round1/code/CANONICAL.txt	papers/199-first-one-stirling-splice/frozen_round1/code/CANONICAL.txt	0b9a1f131984c427db95d8443470a280129b4863b4f92e817e484f99fc13c0ff	e2dd78bc60d5dc629cdd68e6bcf18dd9eec7babe	p199_b:4
papers/199-first-one-stirling-splice/frozen_round1/code/verify.py	papers/199-first-one-stirling-splice/frozen_round1/code/verify.py	d5eb32ce04fa9aef9acedda5a5f0bef5bcab4d3beb28e74cbb8a90ea265c0bb3	acdcc4385c719701b4826b6cec02af473c40dbf5	p199_b:3
papers/199-first-one-stirling-splice/frozen_round1/main.tex	papers/199-first-one-stirling-splice/frozen_round1/main.tex	33e5e27fe6c9cedef8490bc33628ce06dcef0416784ed4e2671c341cdbc80beb	dfc68d39e4f368b74db6bcdf53f07ce5dbf56817	p199_b:1
papers/199-first-one-stirling-splice/frozen_round1/references.bib	papers/199-first-one-stirling-splice/frozen_round1/references.bib	bea6c3a80631bd0a2450813d8b981214c852e0681cb4a33cdb7d2730a4b2bb28	ded90bac1fa85f5585b7d45bb69361b6fc8e5378	p199_b:2
papers/199-first-one-stirling-splice/main_round0_original.pdf	papers/199-first-one-stirling-splice/main_round0_original.pdf	b6ba18a10e83281c1dd491b47cf5d8513ab9914933c659411c8d5c24b72478a0	75830d2f67348ae60f3268614173277b5b73f358	p199_a:10
papers/199-first-one-stirling-splice/main_round1.pdf	papers/199-first-one-stirling-splice/main_round1.pdf	b6ba18a10e83281c1dd491b47cf5d8513ab9914933c659411c8d5c24b72478a0	75830d2f67348ae60f3268614173277b5b73f358	p199_b:5
papers/199-first-one-stirling-splice/round0_snapshot/CLAIMS_EVIDENCE.md	papers/199-first-one-stirling-splice/round0_snapshot/CLAIMS_EVIDENCE.md	1d217f508fe401e54423bfb8a9ad1d865c2793814a9d31bf10aa79928b3bcae9	b35ce7d9ef16aa4550403773c67de0b12f7bcd40	p199_a:8
papers/199-first-one-stirling-splice/round0_snapshot/CLAIM_INTENT.md	papers/199-first-one-stirling-splice/round0_snapshot/CLAIM_INTENT.md	97ab897fa9a2f250d2025894dc5ac4a55849f40de82bf8f12a352ff6d4fc3581	fdc22ef643f01d64e3d8f14f7a83b9fad9a54d25	p199_a:9
papers/199-first-one-stirling-splice/round0_snapshot/PROOF_PACKAGE.md	papers/199-first-one-stirling-splice/round0_snapshot/PROOF_PACKAGE.md	fe2057f6357c4030d9ab1af18cf4c9aa069613e81260f56b7acd05c4130ac061	8d0fefb2dd05118a5806085fe58c79c2401a1e01	p199_a:6
papers/199-first-one-stirling-splice/round0_snapshot/SOURCE_VERIFICATION.md	papers/199-first-one-stirling-splice/round0_snapshot/SOURCE_VERIFICATION.md	db4868603330e4231cf85cd02d768929b3499ed8d5026b2a93049fb3b6484410	0bb825865102730811a3a1a0b60c186203bb679a	p199_a:7
papers/199-first-one-stirling-splice/round0_snapshot/code/CANONICAL.txt	papers/199-first-one-stirling-splice/round0_snapshot/code/CANONICAL.txt	0b9a1f131984c427db95d8443470a280129b4863b4f92e817e484f99fc13c0ff	e2dd78bc60d5dc629cdd68e6bcf18dd9eec7babe	p199_a:5
papers/199-first-one-stirling-splice/round0_snapshot/code/verify.py	papers/199-first-one-stirling-splice/round0_snapshot/code/verify.py	d5eb32ce04fa9aef9acedda5a5f0bef5bcab4d3beb28e74cbb8a90ea265c0bb3	acdcc4385c719701b4826b6cec02af473c40dbf5	p199_a:4
papers/199-first-one-stirling-splice/round0_snapshot/main.pdf	papers/199-first-one-stirling-splice/round0_snapshot/main.pdf	b6ba18a10e83281c1dd491b47cf5d8513ab9914933c659411c8d5c24b72478a0	75830d2f67348ae60f3268614173277b5b73f358	p199_a:2
papers/199-first-one-stirling-splice/round0_snapshot/main.tex	papers/199-first-one-stirling-splice/round0_snapshot/main.tex	33e5e27fe6c9cedef8490bc33628ce06dcef0416784ed4e2671c341cdbc80beb	dfc68d39e4f368b74db6bcdf53f07ce5dbf56817	p199_a:1
papers/199-first-one-stirling-splice/round0_snapshot/references.bib	papers/199-first-one-stirling-splice/round0_snapshot/references.bib	bea6c3a80631bd0a2450813d8b981214c852e0681cb4a33cdb7d2730a4b2bb28	ded90bac1fa85f5585b7d45bb69361b6fc8e5378	p199_a:3
papers/200-lex-first-alternating-switch/ROUND1_RECEIPT.md	papers/200-lex-first-alternating-switch/ROUND1_RECEIPT.md	7bcd9c9c7bcad3459ff4dd0470ad50e8b936f53ba9b90905e72d8b0b7ab27752	0d92dc721fb9ae8fd21f229621df98f049b29d9f	p200_b:6
papers/200-lex-first-alternating-switch/SOURCE_VERIFICATION.md	papers/200-lex-first-alternating-switch/SOURCE_VERIFICATION.md	035094d40e94d26ae60ff80a25a5c58597187057ace720a385f039c11ea4ef43	c8fba3fbdc066a45864348d9d01039e51ab3733e	p200_b:7
papers/200-lex-first-alternating-switch/frozen_round1/code/CANONICAL.txt	papers/200-lex-first-alternating-switch/frozen_round1/code/CANONICAL.txt	9f1c320e2a79248ae2c9ba9b04bfee45540b3063e6d137f12996b898e9715f83	46614d9a8e27c9a754dcf9c78aaf748948010beb	p200_b:4
papers/200-lex-first-alternating-switch/frozen_round1/code/verify.py	papers/200-lex-first-alternating-switch/frozen_round1/code/verify.py	ba5d74cb537bca90a58619c0345333490a52e55bdd566d2a88303b9fda678feb	32e89d3ce9f207800578ea964a48f6f24337952b	p200_b:3
papers/200-lex-first-alternating-switch/frozen_round1/main.tex	papers/200-lex-first-alternating-switch/frozen_round1/main.tex	0827a2bf6d3162699074bbfbe5152108bd9bda897c8b1a08e924b514cc83e8ea	d2bd4823b854ad07df8a65bd5531caf3ac88fbe9	p200_b:1,p203_b:14
papers/200-lex-first-alternating-switch/frozen_round1/references.bib	papers/200-lex-first-alternating-switch/frozen_round1/references.bib	219606cad56fc4232e376271552b795f12cef63c538ebe3f657faa6833c47277	ed135bd9248612978dc7f4e888f8c52a65117782	p200_b:2
papers/200-lex-first-alternating-switch/frozen_round2/main.tex	papers/200-lex-first-alternating-switch/frozen_round2/main.tex	0827a2bf6d3162699074bbfbe5152108bd9bda897c8b1a08e924b514cc83e8ea	d2bd4823b854ad07df8a65bd5531caf3ac88fbe9	p203_a:28
papers/200-lex-first-alternating-switch/main_round0_original.pdf	papers/200-lex-first-alternating-switch/main_round0_original.pdf	7226b56257356fe3869a957983e0c92a7dbc79470f3e504f0f031c4b6248b3ea	a261be3683733508c03ea1e571ac4c502a540d48	p200_a:5
papers/200-lex-first-alternating-switch/main_round1.pdf	papers/200-lex-first-alternating-switch/main_round1.pdf	7226b56257356fe3869a957983e0c92a7dbc79470f3e504f0f031c4b6248b3ea	a261be3683733508c03ea1e571ac4c502a540d48	p200_b:5
papers/200-lex-first-alternating-switch/round0_snapshot/code/CANONICAL.txt	papers/200-lex-first-alternating-switch/round0_snapshot/code/CANONICAL.txt	9f1c320e2a79248ae2c9ba9b04bfee45540b3063e6d137f12996b898e9715f83	46614d9a8e27c9a754dcf9c78aaf748948010beb	p200_a:4
papers/200-lex-first-alternating-switch/round0_snapshot/code/verify.py	papers/200-lex-first-alternating-switch/round0_snapshot/code/verify.py	ba5d74cb537bca90a58619c0345333490a52e55bdd566d2a88303b9fda678feb	32e89d3ce9f207800578ea964a48f6f24337952b	p200_a:3
papers/200-lex-first-alternating-switch/round0_snapshot/main.tex	papers/200-lex-first-alternating-switch/round0_snapshot/main.tex	0827a2bf6d3162699074bbfbe5152108bd9bda897c8b1a08e924b514cc83e8ea	d2bd4823b854ad07df8a65bd5531caf3ac88fbe9	p200_a:1
papers/200-lex-first-alternating-switch/round0_snapshot/references.bib	papers/200-lex-first-alternating-switch/round0_snapshot/references.bib	219606cad56fc4232e376271552b795f12cef63c538ebe3f657faa6833c47277	ed135bd9248612978dc7f4e888f8c52a65117782	p200_a:2
papers/202-ternary-ordered-reset/ROUND0_RECEIPT.md	papers/202-ternary-ordered-reset/ROUND0_RECEIPT.md	f8e0e3aeb7b902c317f94f8a24657e805f88b5e7fe93a0a0ebea18346ccbdeeb	b2eea15e61c346df5b0a868a8d8c9b2ea8505661	p202_a:5
papers/202-ternary-ordered-reset/ROUND1_RECEIPT.md	papers/202-ternary-ordered-reset/ROUND1_RECEIPT.md	67ce417323890134d7d2ee16c2955a8860eec7f485bd357c7a51008255ffdfbb	e5ca6ac59bd9a1d9f6f26a5e80f7d7d6a54d9c9d	p202_b:4
papers/202-ternary-ordered-reset/frozen_round0/SOURCE_VERIFICATION.md	papers/202-ternary-ordered-reset/frozen_round0/SOURCE_VERIFICATION.md	850001668f54c4528c6dde2d28695c86bd10a16facb3997824334aa6ad7e58f0	5b3757b8b292db06e7fde5bf9261c2931ac4d199	p202_a:4
papers/202-ternary-ordered-reset/frozen_round0/main.pdf	papers/202-ternary-ordered-reset/frozen_round0/main.pdf	e1ca5021ff1ac74cff118d0d571fa0f3f74db32cc8b6ba5e7cd557fb69d88f8a	6cfc656c8e2b49a8876d7d839be336ff0881cbf1	p202_a:3
papers/202-ternary-ordered-reset/frozen_round0/main.tex	papers/202-ternary-ordered-reset/frozen_round0/main.tex	bcb24151784b52a27d846dd564ab6a0b438381e617575e6064c698f69683fa1a	19869263f455e0a9cc354665454b4cae3b3f6dd2	p202_a:1
papers/202-ternary-ordered-reset/frozen_round0/references.bib	papers/202-ternary-ordered-reset/frozen_round0/references.bib	56077d3271a58dc9ca3d22b4710c1790a52fbb242d1587da9a443b6455ad2fb0	e5326faea919d712d78d6aa7d8d2431c7727e9ac	p202_a:2
papers/202-ternary-ordered-reset/frozen_round1/main.tex	papers/202-ternary-ordered-reset/frozen_round1/main.tex	bcb24151784b52a27d846dd564ab6a0b438381e617575e6064c698f69683fa1a	19869263f455e0a9cc354665454b4cae3b3f6dd2	p202_b:1
papers/202-ternary-ordered-reset/frozen_round1/references.bib	papers/202-ternary-ordered-reset/frozen_round1/references.bib	56077d3271a58dc9ca3d22b4710c1790a52fbb242d1587da9a443b6455ad2fb0	e5326faea919d712d78d6aa7d8d2431c7727e9ac	p202_b:2
papers/202-ternary-ordered-reset/main_round1.pdf	papers/202-ternary-ordered-reset/main_round1.pdf	e1ca5021ff1ac74cff118d0d571fa0f3f74db32cc8b6ba5e7cd557fb69d88f8a	6cfc656c8e2b49a8876d7d839be336ff0881cbf1	p202_b:3
papers/203-monochromatic-triangle-complementation/A_RESPONSE.md	papers/203-monochromatic-triangle-complementation/A_RESPONSE.md	7fb21531352bafaf7e241fc67d26dc368bf77d42dc6006deb32c2bdb00fc27b6	250e681365d5e868e134b8a72dff633054b36033	p203_a:20
papers/203-monochromatic-triangle-complementation/ROUND0_RECEIPT.md	papers/203-monochromatic-triangle-complementation/ROUND0_RECEIPT.md	89b46ad4e130dbe78ca818e2dbffc94d6991e5b76590d31dd9f7683ad25bd265	22159686f00c14d1d54fb042006ba63cae1a0c8b	p203_a:11
papers/203-monochromatic-triangle-complementation/ROUND1_RECEIPT.md	papers/203-monochromatic-triangle-complementation/ROUND1_RECEIPT.md	ba2bb083dc236a93990c232955952e4faf6af30c559e452de783b9d097e8b487	8710b9761a6457b4d94e42bd0603e5f52282ece6	p203_b:15
papers/203-monochromatic-triangle-complementation/frozen_round0/CANONICAL.txt	papers/203-monochromatic-triangle-complementation/frozen_round0/CANONICAL.txt	6a672bcfa97f09c1575aa89bb4e2ca52aa8284315706ec90abbd6d35995dbf00	e9936277fdeca2d8ac534002d730dcb39dba0f94	p203_a:4
papers/203-monochromatic-triangle-complementation/frozen_round0/CURRENT_INPUTS_SHA256SUMS	papers/203-monochromatic-triangle-complementation/frozen_round0/CURRENT_INPUTS_SHA256SUMS	1327f9bd0177b5e20d29944bfa702b31a81ba481a37e068210fdaa1fdbbe8fdc	08acd44899ff647479cb2f007f438ad8d4d2c613	p203_a:10
papers/203-monochromatic-triangle-complementation/frozen_round0/PROOF_PACKAGE.md	papers/203-monochromatic-triangle-complementation/frozen_round0/PROOF_PACKAGE.md	04d28178f630a1b0c404bfc26c0d9cd561c2898e4f585f0168d43ef93d2ec9b7	7edefbc25b3bb084d97754e77e6c10b9cb6004d4	p203_a:8
papers/203-monochromatic-triangle-complementation/frozen_round0/PROVENANCE.md	papers/203-monochromatic-triangle-complementation/frozen_round0/PROVENANCE.md	002f4e08354829ef5c0f30eedc766b52b4968f1fbb5e85297ee0a962ff9ed83e	bc902ac43b6129b599d9d6cd82e99dd3e299d795	p203_a:7
papers/203-monochromatic-triangle-complementation/frozen_round0/SHA256SUMS	papers/203-monochromatic-triangle-complementation/frozen_round0/SHA256SUMS	4bd31b8f118d7508db30c99145c69aed508ef0efb33d815a37f8722b37ed1f8b	9348ee6858117228719680ab144dc59bd391af9e	p203_a:6
papers/203-monochromatic-triangle-complementation/frozen_round0/SOURCE_VERIFICATION.md	papers/203-monochromatic-triangle-complementation/frozen_round0/SOURCE_VERIFICATION.md	976c07220be31143843e5ca37a6448a33b40d4da67ab0463e4c6221da1a17ab9	18597ce8f3f34ef7fb0655ccc7129efab45ef5de	p203_a:9
papers/203-monochromatic-triangle-complementation/frozen_round0/main.pdf	papers/203-monochromatic-triangle-complementation/frozen_round0/main.pdf	617cea5d4f8b50a9946d05bafc2cfbf6fb01bbe45dab754813b07f4f12cc1167	89c923a76bc7709a0e4b968188fb8f3b1fa2b7fb	p203_a:5
papers/203-monochromatic-triangle-complementation/frozen_round0/main.tex	papers/203-monochromatic-triangle-complementation/frozen_round0/main.tex	a08983002caf08109c6a6406183149343aaa5ecd9a6d08af7f521f8ca85480b0	5a2a831c01135440cb3506a2949c1f63d49dcdf7	p203_a:1
papers/203-monochromatic-triangle-complementation/frozen_round0/references.bib	papers/203-monochromatic-triangle-complementation/frozen_round0/references.bib	2a7c888ff6158f11e00a45f6231f628e575515d1f1c0713f93f90592ea88f78a	2c390b0c5ef4586a7f3646cad4f406cb8c944564	p203_a:2
papers/203-monochromatic-triangle-complementation/frozen_round0/sources/fomin2020_primary.pdf	papers/203-monochromatic-triangle-complementation/frozen_round0/sources/fomin2020_primary.pdf	e38491e3f053535604fa616804fe269149812c97cddce50289111c21b4b74654	511b9c5f0bbb99bccbe71925967f7f2c6092c19e	p203_a:21
papers/203-monochromatic-triangle-complementation/frozen_round0/sources/shuldiner2022_v1.html	papers/203-monochromatic-triangle-complementation/frozen_round0/sources/shuldiner2022_v1.html	a46e824217751aec13658b14700985bbe7aebb326df5ca32dd20b0dad700a57c	9676c65da69a9585296d862f63d6aca568f07816	p203_a:22
papers/203-monochromatic-triangle-complementation/frozen_round0/verify_p203.py	papers/203-monochromatic-triangle-complementation/frozen_round0/verify_p203.py	77e7be9b6dc57a156010c6543ff41415415f833119e5a7116ffcef53cc5e1d7d	a993f5eda312ae27cc41ffb1f1bf4602540eabe4	p203_a:3
papers/203-monochromatic-triangle-complementation/frozen_round1/AUTHOR_RUN1.txt	papers/203-monochromatic-triangle-complementation/frozen_round1/AUTHOR_RUN1.txt	6a672bcfa97f09c1575aa89bb4e2ca52aa8284315706ec90abbd6d35995dbf00	e9936277fdeca2d8ac534002d730dcb39dba0f94	p203_b:16
papers/203-monochromatic-triangle-complementation/frozen_round1/AUTHOR_RUN2.txt	papers/203-monochromatic-triangle-complementation/frozen_round1/AUTHOR_RUN2.txt	6a672bcfa97f09c1575aa89bb4e2ca52aa8284315706ec90abbd6d35995dbf00	e9936277fdeca2d8ac534002d730dcb39dba0f94	p203_b:17
papers/203-monochromatic-triangle-complementation/frozen_round1/BUILD.md	papers/203-monochromatic-triangle-complementation/frozen_round1/BUILD.md	71ceb87bb7cfd268b770b89f2ed57805eef46bbc5926b2963d53d7058629e544	bd016db3d6b227e134ae5f76d5e85db82a921108	p203_b:18
papers/203-monochromatic-triangle-complementation/frozen_round1/BUILD.sh	papers/203-monochromatic-triangle-complementation/frozen_round1/BUILD.sh	09411256e146192c22debd9c68186327b54ccfd174b679bcaab58345c8cfd064	b228c91e8526628a79405949519a45d32e318c97	p203_b:19
papers/203-monochromatic-triangle-complementation/frozen_round1/CANONICAL.txt	papers/203-monochromatic-triangle-complementation/frozen_round1/CANONICAL.txt	6a672bcfa97f09c1575aa89bb4e2ca52aa8284315706ec90abbd6d35995dbf00	e9936277fdeca2d8ac534002d730dcb39dba0f94	p203_b:20
papers/203-monochromatic-triangle-complementation/frozen_round1/CLAIMS_EVIDENCE.md	papers/203-monochromatic-triangle-complementation/frozen_round1/CLAIMS_EVIDENCE.md	d50cde5489c896bfae1d39b2fb499c76890317288b79244553ea27cfcdb75726	f1d1e9cbc13b9459786f9f3de2d22fd018ad2333	p203_b:21
papers/203-monochromatic-triangle-complementation/frozen_round1/CURRENT_INPUTS_SHA256SUMS	papers/203-monochromatic-triangle-complementation/frozen_round1/CURRENT_INPUTS_SHA256SUMS	1327f9bd0177b5e20d29944bfa702b31a81ba481a37e068210fdaa1fdbbe8fdc	08acd44899ff647479cb2f007f438ad8d4d2c613	p203_b:22
papers/203-monochromatic-triangle-complementation/frozen_round1/FIGURE_PLAN.md	papers/203-monochromatic-triangle-complementation/frozen_round1/FIGURE_PLAN.md	456b2d278cf157993e5f84196c8bf42ce28b96e85aa7e78a105eea72c68ddfbe	e7a1628dc59fbd929204cfe05e473e2671639fb6	p203_b:23
papers/203-monochromatic-triangle-complementation/frozen_round1/IMPROVEMENT_LOG.md	papers/203-monochromatic-triangle-complementation/frozen_round1/IMPROVEMENT_LOG.md	cd963c86f0f5b249e81d55107aae4ae5b8d2c3a3c8ec0f9b78a3d32130a2e103	ac45ef65af451cd58e9d05478da3547e0b1c4737	p203_b:24
papers/203-monochromatic-triangle-complementation/frozen_round1/NARRATIVE_REPORT.md	papers/203-monochromatic-triangle-complementation/frozen_round1/NARRATIVE_REPORT.md	c054ffbe3cbb07a8d689f89b95220e944fd70f1a281de9bfcdaa20ae8b0f28f7	f3fb478180cb46dd8eb33412368aeee4f7d597bc	p203_b:25
papers/203-monochromatic-triangle-complementation/frozen_round1/PAPER_PLAN.md	papers/203-monochromatic-triangle-complementation/frozen_round1/PAPER_PLAN.md	377640667d9597da4217e38404a847409e732b59fa30bc483c61cc754cdd791b	fa83e82cb91d4f1c133821912c0346529ced0e0a	p203_b:26
papers/203-monochromatic-triangle-complementation/frozen_round1/PROOF_PACKAGE.md	papers/203-monochromatic-triangle-complementation/frozen_round1/PROOF_PACKAGE.md	04d28178f630a1b0c404bfc26c0d9cd561c2898e4f585f0168d43ef93d2ec9b7	7edefbc25b3bb084d97754e77e6c10b9cb6004d4	p203_b:27
papers/203-monochromatic-triangle-complementation/frozen_round1/PROVENANCE.md	papers/203-monochromatic-triangle-complementation/frozen_round1/PROVENANCE.md	002f4e08354829ef5c0f30eedc766b52b4968f1fbb5e85297ee0a962ff9ed83e	bc902ac43b6129b599d9d6cd82e99dd3e299d795	p203_b:28
papers/203-monochromatic-triangle-complementation/frozen_round1/README.md	papers/203-monochromatic-triangle-complementation/frozen_round1/README.md	fe9b3b9408ccdc83e7c69b2d95cf43d1a50f2c771ffd6d893e981f2833fd70dd	57ed7c9e889062cc87eb4f9cf721b76280d81411	p203_b:29
papers/203-monochromatic-triangle-complementation/frozen_round1/REPLAY_LOG.md	papers/203-monochromatic-triangle-complementation/frozen_round1/REPLAY_LOG.md	1f0d4e586a99ca533cbcfc15bd5e4bb7d985a5ed05b6e8cecd90b6418418c5a0	5304089725cb1cb3e800d061b08113a6603cc60d	p203_b:30
papers/203-monochromatic-triangle-complementation/frozen_round1/SELF_QA.md	papers/203-monochromatic-triangle-complementation/frozen_round1/SELF_QA.md	09cc4886ce5a2eca4ea9897de6b4922a54269037a9eed6be193d76e33b594356	1725a68c5eead5ac766cc74ebb8646e0ff9730d4	p203_b:31
papers/203-monochromatic-triangle-complementation/frozen_round1/SHA256SUMS	papers/203-monochromatic-triangle-complementation/frozen_round1/SHA256SUMS	e27427e2ce944382ba848a3e43d941ad3cfae2648eb24b21d0a106d88ad4c8b6	e8caeece8bc317a71ebeefe57a5f8dc10345979c	p203_b:32
papers/203-monochromatic-triangle-complementation/frozen_round1/SOURCE_VERIFICATION.md	papers/203-monochromatic-triangle-complementation/frozen_round1/SOURCE_VERIFICATION.md	976c07220be31143843e5ca37a6448a33b40d4da67ab0463e4c6221da1a17ab9	18597ce8f3f34ef7fb0655ccc7129efab45ef5de	p203_b:33
papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/CONTRACT.md	papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/CONTRACT.md	06e378c7e6086d326037e1bb01be4b4c603eb33ba44d3acddcec0c50b68fd500	ca2897ff88b298935e9998c81bde99d7304ddf2d	p203_b:34
papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/DELTA.md	papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/DELTA.md	45fe99e055654e13168a5e4dd137f0daaca3536b648b99d2ddb58c478f876d40	13437fac8fa093616690b51dcad49a7dea6d359b	p203_b:35
papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/HISTORICAL_TEMPORAL_INPUT_PINS.sha256	papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/HISTORICAL_TEMPORAL_INPUT_PINS.sha256	c987e124c592ff63f2eba5d121b1e105e1d1d71f5a27f3aeb74dfc1700900189	2fe4d3a3ffcc20d31c4f770afddbe95a756aa9d2	p203_b:36
papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/INVERSE_THEOREM.md	papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/INVERSE_THEOREM.md	845f386a6be557516229e657534496527adb1fffb2fe5f8bf0dc312ead24bd1a	66a177b05e6557b842f04a43981154d34408786d	p203_b:37
papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/LFCTR_HISTORY_COUNT_CORRECTION.md	papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/LFCTR_HISTORY_COUNT_CORRECTION.md	e07f6e7e110397033157ba409c548cc5bbfdbced7169b91042cba4d530215352	9bb339eecb7bc07128fd88d40fca7c99a376c467	p203_b:38
papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/MCT_ROOT_ADJUDICATION.md	papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/MCT_ROOT_ADJUDICATION.md	dc4cbddb4cf798d229cc4f5fbcfaf8b59131f39e893650b56a7ae6ec78a38268	8a026c16a0d3086614e523cf41d0d712f9bd1f5c	p203_b:39
papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/PROVENANCE_RECEIPT.md	papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/PROVENANCE_RECEIPT.md	6d1b1eaa25d18ce5ed0e036ab73f054476244117214da2ecacb37cd3332144af	735aa08a632ef1e425960da8b03f9be453a0fa1e	p203_b:40
papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/SOURCE_OWNER.md	papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/SOURCE_OWNER.md	c3f1f0d7063a1fa531d0b4d624bf6f5dfccb40dea79eee6fff525edc483e6b58	72e7280286ce6f0b9cb411c06a6591178b0d7f13	p203_b:41
papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/STAGE1_GATE.md	papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/STAGE1_GATE.md	4b2c8124144d14d2043928b8caeeb7fd83b8584683e57cc9e9538a857429cdc0	1d6d9bed5a5c68f271adaf4f8382c9dc2c7cefb6	p203_b:42
papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/TEMPORAL_PROOF.md	papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/TEMPORAL_PROOF.md	25ba4d29400ee7047fac588c3e8ba64cd55bf3782368a96bf4fb88dcbd5b85f8	9bd6ce1a57fcb239d057dc859617bf10c7833577	p203_b:43
papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/probe.py	papers/203-monochromatic-triangle-complementation/frozen_round1/current_inputs/probe.py	1e40d08722268ab476a8687d1f0204a5dd3f5b2dc6c7046eb0d887c63d36b937	d241826a1efbaf7bc72fab17e39cc9135366b550	p203_b:44
papers/203-monochromatic-triangle-complementation/frozen_round1/main.pdf	papers/203-monochromatic-triangle-complementation/frozen_round1/main.pdf	0738965406c046662618ec999474738c064c363fa66ba587e7b33a377f89b47d	a9997ae9c95a313bccfdccdc96ab7c12aa72e758	p203_b:45
papers/203-monochromatic-triangle-complementation/frozen_round1/main.tex	papers/203-monochromatic-triangle-complementation/frozen_round1/main.tex	70c22a62adc3b6218278a6fd91b08dfa8d02efddf03ba7cc115bd35a3ab6de54	0f5e7acd58426d84ce7c56d0eea1a6f02c7d9b06	p203_b:46
papers/203-monochromatic-triangle-complementation/frozen_round1/references.bib	papers/203-monochromatic-triangle-complementation/frozen_round1/references.bib	2a7c888ff6158f11e00a45f6231f628e575515d1f1c0713f93f90592ea88f78a	2c390b0c5ef4586a7f3646cad4f406cb8c944564	p203_b:47
papers/203-monochromatic-triangle-complementation/frozen_round1/sources/SHA256SUMS	papers/203-monochromatic-triangle-complementation/frozen_round1/sources/SHA256SUMS	7084b547be15e60998373ee19a42897cf9d1ab511cf1986f39673e53b08880fe	8c3aee45a36d4056146fe01274b8d8502345b303	p203_b:48
papers/203-monochromatic-triangle-complementation/frozen_round1/sources/fomin2020_primary.pdf	papers/203-monochromatic-triangle-complementation/frozen_round1/sources/fomin2020_primary.pdf	e38491e3f053535604fa616804fe269149812c97cddce50289111c21b4b74654	511b9c5f0bbb99bccbe71925967f7f2c6092c19e	p203_b:49
papers/203-monochromatic-triangle-complementation/frozen_round1/sources/shuldiner2022_v1.html	papers/203-monochromatic-triangle-complementation/frozen_round1/sources/shuldiner2022_v1.html	a46e824217751aec13658b14700985bbe7aebb326df5ca32dd20b0dad700a57c	9676c65da69a9585296d862f63d6aca568f07816	p203_b:50
papers/203-monochromatic-triangle-complementation/frozen_round1/temporal_author_audit.md	papers/203-monochromatic-triangle-complementation/frozen_round1/temporal_author_audit.md	f150027508bcdfcc0f22706754fee3b6e645e9027cda3e56eba0e6c0d5a91a56	e42aa097d513b5b4ef46c7162503cb35ee655d71	p203_b:51
papers/203-monochromatic-triangle-complementation/frozen_round1/verify_p203.py	papers/203-monochromatic-triangle-complementation/frozen_round1/verify_p203.py	77e7be9b6dc57a156010c6543ff41415415f833119e5a7116ffcef53cc5e1d7d	a993f5eda312ae27cc41ffb1f1bf4602540eabe4	p203_b:52
papers/203-monochromatic-triangle-complementation/revision_a/SHA256SUMS	papers/203-monochromatic-triangle-complementation/revision_a/SHA256SUMS	83c9b2650cdaa2324206c1d7d748c75fac119918cb91814a07557edfcb82ce1a	1ff865b7bbaf6c3bcdeba0a6d1b66047b4b41a8d	p203_a:19
papers/203-monochromatic-triangle-complementation/revision_a/main.pdf	papers/203-monochromatic-triangle-complementation/revision_a/main.pdf	0738965406c046662618ec999474738c064c363fa66ba587e7b33a377f89b47d	a9997ae9c95a313bccfdccdc96ab7c12aa72e758	p203_a:18
papers/203-monochromatic-triangle-complementation/revision_a/main.tex	papers/203-monochromatic-triangle-complementation/revision_a/main.tex	70c22a62adc3b6218278a6fd91b08dfa8d02efddf03ba7cc115bd35a3ab6de54	0f5e7acd58426d84ce7c56d0eea1a6f02c7d9b06	p203_a:16
papers/203-monochromatic-triangle-complementation/revision_a/references.bib	papers/203-monochromatic-triangle-complementation/revision_a/references.bib	2a7c888ff6158f11e00a45f6231f628e575515d1f1c0713f93f90592ea88f78a	2c390b0c5ef4586a7f3646cad4f406cb8c944564	p203_a:17
papers/90-rule184-particle-periodic-zeta/main.tex	symbolic_dynamics/papers/90-rule184-particle-periodic-zeta/main.tex	74adef800c0f6ff315746cc0bb8e74d975359653f488c998e822746933445f90	148ee3e0ad3aa9f20b6efb36af1b99a723f9796c	p197_a:13,p197_b:10,p202_a:10,p202_b:9
```

