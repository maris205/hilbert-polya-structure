# Independent Review of the Corrected R4 Publication-Lock Supplement

Date: 2026-08-26

## Verdict and authority

I performed a fresh, from-scratch, zero-write-first review under the controlling parent gate `PAPER25_R4_PUBLICATION_LOCK_SUPPLEMENT_SUBSTITUTE_REREVIEW_OPEN`. I am distinct from every Paper 25 source author, lock architect, correction role, prior R4 reviewer, and future builder. I found zero blocker, zero major issue, zero minor issue, and zero ambiguity.

The review was confined to the project tree, the two governing ledgers, frozen installed tool binaries, and frozen system TeX resources. I did not compile, run pdfLaTeX or BibTeX, inspect or mutate a PDF, use the network, touch Paper 26, or open a build, finalization, release, or submission gate. I performed no filesystem operation of any kind on a Paper 23 or Paper 24 temporary root, any retained Paper 25 R0--R3 root, or either reserved R4 root. Reserved and firewalled roots were treated only as inert strings.

## Opening universe and closing stability

The opening governing records were exact mode-0644, one-link, terminal-LF regular files:

- `BATCH_06_STATUS.md`: 319,831 bytes, 4,501 LF, SHA-256 `cc796787b29fdfbfddbbf9141f39be4437854fc389934f5101a16d976b699a4b`;
- `BATCH_06_IDEA_REPORT.md`: 477,451 bytes, 8,695 LF, SHA-256 `96bf96740ad008722c435f121ba1b452f8cccc3d80e88f53c2951323edcf063e`.

Before this review file was created, its exact path was ENOENT and not a symlink. The project was exactly L31: 31 regular files, four subdirectories, zero symlinks, zero other nodes, 843,117 content bytes, 10,697 LF, and 1,107 UTF-8 bytes across regular-file relative paths. I read all 31 files through physical EOF. Every one of the 30 L30 predecessor descriptors matched path, type, mode 0644, link count one, byte count, LF count, SHA-256, UTF-8 and terminal-LF state, and BOM/CR/NUL exclusions. The corrected supplement was the sole additional L31 node.

Immediately before the sole review-file patch, I repeated the two ledger identities, every one of the 31 predecessor identities and node properties, the complete L31 aggregate, and review-path absence. Every closing value was byte-identical to the opening value.

## Strict JSON and exact correction provenance

I parsed the base lock and the R1, R2, corrected R3, and corrected R4 supplements with a duplicate-rejecting parser that separately rejects floating-point tokens, `NaN`, and all infinities. Each file contains only the permitted JSON types, is UTF-8 without BOM/CR/NUL, consists of one physical JSON line and one terminal LF, and round-trips byte-for-byte under recursive Unicode-code-point key sorting, `ensure_ascii=false`, compact separators, and no nonfinite values. In-memory hostile inputs with duplicate keys, float tokens, nonfinite tokens, unsorted keys, reordered arrays, and line-contract drift were rejected.

The corrected R4 supplement is schema `paper25.publication_lock_r4_supplement.v1`, 66,018 bytes and one LF, SHA-256 `7ddb5dd5a9428008672feb4b12698a67f2a0c9db9bf502328c19aa2c4c184e9e`, mode 0644, and one link. It deliberately excludes a self-identity field.

I restored the six authorized correction locations in memory: the removed delta-6 `main.out` array member at its former position immediately before `main.pdf`; delta 8's `twelve` back to `thirteen`; the two former value hashes; and the former effective-R4 byte-count and SHA metadata. The resulting strict-canonical bytes are exactly the rejected preimage: 66,031 bytes, SHA-256 `5ab5576c2a68d43ef9df418ab01b252f5b315de6c426968cdf0184104f96bb3a`. Its former delta-6 and delta-8 value hashes are respectively `7919289a42e30a6810571f760ac3173a34a976f54af640b7b1953af788696e97` and `a9fa7661c03064d1bf303818142506fcfb080a12f665de65e08fe61db384e34c`; replay of that rejected overlay gives 94,452 canonical bytes and SHA-256 `060e305bf0bca0c3e113ad359ab7f51a66ffba0384fffcd8301a9edb0c4e5748`.

The current file differs from that rejected preimage only at the six authorized JSON locations. The remaining two raw `main.out` strings are the pass-1 and pass-2 rerunfilecheck diagnostic templates. They are neither inventory members nor an authorization to create a file.

## Five-layer replay and exact overlay

I replayed from a newly parsed deep copy of the base object, applying every operation with JSON-pointer unescaping, replace-target existence checks, add-target absence checks, exact order, and no cached expanded object. Compact canonical effective objects have no terminal LF and reproduce:

| Layer | Canonical bytes | SHA-256 |
|---|---:|---|
| R1 effective | 75,264 | `8c92a2469a415736de6658ebed4710a19b8f59cedfa1c4dbd60f9a3f9ca15aaa` |
| R2 effective | 81,582 | `341c9fdb89602befa7dc02c4185d68452e8e6e8d076f8324e6fe9a81dee54d98` |
| corrected R3 effective | 84,176 | `6b5265809ad32f8e3dabd9aa51f42ce76a9f9aa7f6635061b7d7aa3e64112d96` |
| corrected R4 effective | 94,439 | `5561c3506afb3a2495c07c6928beb64bc49a6c3cc8f1eba90ecaddefd9d6f86f` |

The R4 list has exactly ten operations, exactly the separately declared target list, no duplicate or unknown target, and operations `replace` for 1--7, `add` for 8, and `replace` for 9--10. The targets and independently recomputed value hashes are:

1. `/build_contract/clean_dual_build/build_A_root` — `62516de2356d2a5c4c0e3c04822e7bbd83d18e738fa4e102adea72f5b811137c`;
2. `/build_contract/clean_dual_build/build_B_root` — `d5dd0813a096630ff5d2aaedf738c783d587b12c90ed103dc6d123c3d859d764`;
3. `/build_contract/clean_dual_build/freshness_rule` — `0d475882ed5cf019ea8817070d8d8be622048908d8a24f5704389d9ded047a47`;
4. `/build_contract/clean_dual_build/historical_root_firewall` — `1338270e06e32fa3f95109f0a5dc04e2ad999592f080d5d6e135aaa3a9ab5927`;
5. `/build_contract/inspection/cross_build_command` — `5ad7b9269d6f6ee383ab92f360b3d09bd1b3329383dbd1b0cc6665ee7a27895b`;
6. `/build_contract/clean_dual_build/allowed_root_filenames` — `04f5df6f97ea69345a4568810a3a8d65adfc37030b04998b4fbd5696d3d970f4`;
7. `/build_contract/toolchain/tools/12/role` — `3ad80355b4349008b6cc809fb0fae974642be16a2250be4763e0127a5b8b00ad`;
8. `/build_contract/pass_boundary_raw_log_snapshots` — `acd06e706d91b6072595b89c21b302d8530d8088d1c753f02e6dd85932789577`;
9. `/build_contract/failure_and_warning_policy/underfull_box_rule` — `682cc7999afcbce612d77754edf628c71e8e04429809b6bbc01fc1489cade0ac`;
10. `/build_contract/failure_and_warning_policy/earlier_pass_only_allowlist` — `ef9beed4247e747228b69738f309ad20fafda8774e8d75a743a16b896a59628d`.

Every target changes at least one predecessor value. A recursive structural comparison assigns every raw difference to exactly one of these targets: the two roots; all freshness leaves; both R3-firewall additions; the cross-build command; the changed filename-array tail; the frozen Python role; the newly added snapshot subtree; the Underfull rule; and the complete pass allowlist. No difference lies outside those subtrees, and collapsing each replacement/addition subtree yields exactly the declared ten-target difference set. Missing, duplicate, reordered, unknown, eleventh, target-typo, operation-drift, add-collision, predecessor-drift, and Paper35-effective-namespace mutations all fail.

## Frozen source, predecessor reviews, and L30 frame

The staged universe remains exactly three independent mode-0644, one-link regular source copies:

- `paper/main.tex`: 76,043 bytes, 1,192 LF, SHA-256 `4d8ac64803ecae76809461e183c72349e7bcab1ad1fac3e4167fe9735860eea2`;
- `paper/math_commands.tex`: 393 bytes, 11 LF, SHA-256 `c748e0cde8aadef85c5de9e1fa20efb7770d07fb3fde58dfe0f4fe738720edf0`;
- `paper/references.bib`: 3,450 bytes, 118 LF, SHA-256 `159acd5633b19f3f91c203d4f85375cfe5ddaaee6337fd5297c673ac1b9ad99d`.

The source has the exact class/package/load order, imports only `math_commands.tex` plus the bibliography basename, contains the sole `\clearpage` immediately before the sole bibliography, has no appendix, supplement, figure input, shell escape, local path, governance datum, or `[VERIFY]` marker, and ends at the bibliography insertion. It has eight sections, 39 subsections, one table, zero figures, nine labels, and twelve source-closed reference mentions.

Rebuilding the prescribed L30 binary frame in bytewise UTF-8 path order produced exactly 778,683 bytes and SHA-256 `a9fa9fffec8b138d2b16e4e1838faaf0913085620fba56b8873490f38c4c385e`, from 777,099 content bytes, 10,696 LF, and 1,060 path bytes. Adding only the self-excluded supplement produces the exact L31 universe above.

The base, R1, R2, and corrected R3 lock files match their bound identities. The four chained independent lock reviews match their bound identities and unique EOF terminals: base review `599640710e5064226c4c390ad78265d100ce0fb8c01d8f9f0eaf6d527f9fec44`, R1 review `65b183cf328fb10bb8281a65d3a3a37b9023448bc431230589b4ffdd20f9f231`, R2 review `690c5ea82656597d1bee99824f642d7356b8be22d059dbee1b4194c1e86ba447`, and corrected R3 review `3ea729e80498e4aa8fcdfa9f094a9887d8e4926d568bf0e6d66d2956dfaeca50`. The other five independent predecessor reviews also match their inventory identities and unique EOF terminals for plan, source design, source lock, publication stage, and R2 notation repair.

## Historical ledgers and frozen evidence

I independently inverted the later bounded ledger insertions in memory. Removing three exact STATUS insertion regions of 2,997, 2,842, and 2,259 bytes and then taking the bound author-time prefix reproduces 309,553 bytes, 4,360 LF, SHA-256 `d7f1ee1c90341ff534affeaada99531064e3a592509645a907ea58e9e4bb7432`. Removing the one exact 3,633-byte IDEA insertion and taking its bound prefix reproduces 469,662 bytes, 8,575 LF, SHA-256 `40291acbfac952ed828273783d7c18069dfb6ea9fdd3cdde4f5c94295e259e81`.

At their author-time offsets, the six R3 failure/review slices reproduce their exact byte/LF counts, start markers, and SHA-256 values in semantic chronology order:

1. `07611328942ba7f8f1bc1b9a067e0f26bf0f17288268b3e925117c1cd95cbc51`;
2. `13f150fb448475a009a7bf2d8afa7d4b2ffe0eaa2570bcbb5e4612161349a81a`;
3. `8b183f635568772e30bb5638fd5afb8d1233e25f4888f0b70d7b77c6670b6f92`;
4. `d6cffe021ab486918eee82ccd5803ed81a2a35afda7d9ab5ce3581e77609ee86`;
5. `585e3b8c54227709c7c2b7e730adb80a72e8818f961f52a419caf20dcc5bc7ca`;
6. `8be57ab11f42fea81a94c87909d2a0740f2ad2753e653ad839fc3bbfb5d1dbaa`.

The chronology ordinals are authoritative: IDEA ordinal 4 has author-time offset 461,362, while ordinals 5 and 6 have offsets 450,219 and 452,140 because later gate sections were physically inserted earlier. The two R4 design/author-gate slices also reproduce `7a6f81f2f440e116f8d6c6cb28392eea97052e9fa09e0d91ad4dd84a8703ff8c` and `1ae344a8070c9d5ffa0e895c5234211d9cbaeda11017e71a42c56370b29c3745`. In the current ledgers all eight unique start markers relocate cleanly, and slicing the declared byte counts from those markers reproduces the same hashes.

These witnesses close the R3 failure census, ordinary BibTeX convergence, retained source and generated-bibliography identity, deterministic AX spacing event, missing pass-1 raw log, 27-page nonfinal layout, and the causal need for the R4 snapshot contract without accessing a retained root.

## Parser, pass policy, and AX conjunction

The source contains 26 citation commands and exactly 32 citation mentions. Its canonical multiplicity object is 192 bytes, SHA-256 `2de243d572e002ed4df314f7c2dad7fabad1cbca44ab454826409edc395f508c`: `AX`, `BT`, `BvS`, `DF`, `Des`, `HS`, `KL`, and `SS` occur three times each; `StdDummit2004AbstractAlgebra` once; `StdIreland1990ModernNumberTheory` twice; `StdKailath1980LinearSystems` four times; and `StdMeyer2000MatrixAnalysis` once. The twelve bibliography keys equal that key set. The twelve reference mentions have exactly the declared eight-label multiplicities.

The byte-oriented event reconstruction has candidate width arrays `[] / [] / [79] / [79] / [] / [] / [] / [77] / []`. Independent executable fixtures admitted citation and reference in-word joins only at width 79 and the destination fallback only at the exact zero-leading-space 77+28 split. Its 105-byte joined destination event hashes to `9a92f52f157466f8a66ee498f748610bc537417911252567d639b9fb7eb78889`. Widths 77, 78, and 80 for ordinary candidates, destination width 78, the historical two-leading-space destination, changed fragments, empty-width joins, joining outside an open candidate, crossing a new diagnostic, consuming lookahead after closure, and broad scanning of ordinary warning-like prose all fail. The rerunfilecheck semantic continuation alone retains LF boundaries and normalizes to its exact template.

Pass 1 admits only its source-closed grammar and forbids every box; the frozen complete positive census has 49 events. Pass 2 requires exactly the 32-citation vector, exactly one plural undefined-reference summary, zero singular undefined references, optionally zero or one label-rerun and zero or one rerunfilecheck event, and exactly one AX-bound Underfull. The frozen observed form has 35 complete events. Pass 3 requires exactly one AX-bound Underfull and zero of every other warning, rerun diagnostic, destination, citation, reference, box, missing-character, multiply-defined, error, and fatal class. Count, key, label, pass, summary, unexpected-event, and extra-box mutations fail.

The AX project slice `references.bib[1887,2068)` is exactly 181 bytes and six LF, begins `@misc{AX,`, and hashes to `359fcd6a061689e9c652641e4df10862818fc1a020a6e3d38e3f8c19b1e7b929`. The frozen generated `main.bbl` witness is 2,908 bytes and 79 LF, SHA-256 `a3d83191db0fc3c7f77656c685c215255140db72eea0746bf51e5696f8eb6fe0`. The exact 57-byte normalized header `Underfull \hbox (badness 1215) in paragraph at lines 4--7` hashes to `f012678404387c656e8579aa632c85820f5f0c1281b5a3966c6abf04c0e111bc`. Authorization requires all of header, bbl identity, reported lines 4--7, unique nearest `\bibitem{AX}` ownership, source slice, allowed pass, and count. Leading whitespace, hbox/vbox class drift, badness or line drift, width joining, detail-line consumption, bbl/owner/source/pass/count drift, and any other box fail.

## Raw-log snapshots and reachable inventory

The embedded capture program is ASCII, 1,507 bytes and 38 LF with terminal LF, SHA-256 `b15f1871efe580e1d6ce93534ec6b4a8f105bd719266c1c5e3c58c1a2a453a99`. It parses and compiles as Python. Its AST and exact source establish three imports only; exact two-argument validation; source `lstat`; regular, one-link, same-inode checks; `O_RDONLY|O_CLOEXEC|O_NOFOLLOW`; destination `O_WRONLY|O_CREAT|O_EXCL|O_CLOEXEC|O_NOFOLLOW`; umask 022 and verified mode 0644; source/destination inode inequality; full read and short-write-safe write loops; source device/inode/mode/link/size/mtime stability; final-size equality; `fsync`; and nested `finally` closure.

The exact isolated argv uses the frozen Python binary with `-I -S -c` under only `LANG=C`, `LC_ALL=C`, `PATH=/usr/bin:/bin`, and `TZ=UTC`; HOME and CODEX_HOME remain unset. Exactly three captures occur immediately after `pdflatex(1)`, `pdflatex(2)`, and `pdflatex(3)`, each before return-code interpretation, the corresponding snapshot-only parser, and any command that can replace `main.log`. A nonzero TeX return code still requires capture and then stops all continuation.

Each snapshot is created once, is regular mode 0644 with one link, has a distinct inode from its source and every other retained snapshot, equals the just-produced log, and is thereafter immutable. The parser reads only the corresponding snapshot. No snapshot may occur as an INPUT or OUTPUT in `main.fls`; final `main.log` must equal but remain inode-distinct from `main.pass3.log.raw`; and corresponding A/B snapshots and their three explicit `cmp` commands must agree.

The only reachable successful root inventory is exactly twelve regular files: the three sources; `main.aux`, `main.bbl`, `main.blg`, `main.fls`, and `main.log`; the three raw-log snapshots; and direct `main.pdf`. There is no directory, symlink, other node, or `main.out`. Missing, extra, late, swapped, preexisting, short, mutable, renamed, recreated, same-inode, wrong-mode, multi-link, FLS-visible, parser-substituted, final-log-mismatched, or cross-build-unequal snapshots fail.

## Root, command, page, PDF, tool, and resource closure

The R4 namespace is internally Paper25 throughout every effective root and gate field. The sole `Paper35` text is an explicitly rejected hostile-case label; no `PAPER35` gate or `paper35` root occurs. The permanent firewall contains the complete five exact Paper 23 roots, seven exact Paper 24 roots plus the additional-temporary-root rule, and all eight Paper 25 R0--R3 retained roots. Its exact 15 prohibited operations and permanent scope are unchanged. The future A then B probes are permitted only after a later build gate, must be non-following exact-path probes returning ENOENT, and permit one mode-0700 creation each; presence, symlink, swap, typo, listing, globbing, cleanup, retry, recreation, or reuse fails.

The four inherited pass command strings, ordinals, and environment are byte-for-byte unchanged: three pdfLaTeX commands and one intervening BibTeX command. The three snapshot captures add no TeX pass. The final PDF remains the direct third-pdflatex output with no wrapper, retry, rewrite, normalization, optimizer, timestamp fixer, or postprocessor. The PDF and all three corresponding log snapshots must be byte-identical across independently staged A/B roots.

The combined page contract requires exactly 27 total pages: pages 1--26 are nonempty content pages from Abstract through Conclusion, page 26 contains the public Conclusion heading, and the first standalone References heading is on page 27 with none earlier. The retained R3 evidence records exactly that placement under the identical source and TeX stack. R4 changes only convergence-warning policy and raw-log retention, so it does not authorize layout drift. Total 28, Conclusion on 25, References on 26, or an empty content page all fail.

I independently hashed all 13 frozen command binaries plus the frozen Python binary and the installed `fitz` module; all 14 tool records match. Under the frozen isolated TeX search environment, all 19 direct class, package, bibliography-style, and engine resources resolve from the system installation and match their recorded SHA-256 values. The inherited environment, pass-order, inspection-command, source/input-audit, and system-resource canonical hashes equal their R4 bindings. Representative positive and hostile records also enforce exact staging, commands, captures, twelve-node inventory, FLS exclusion, log identity, PDF determinism, page placement, metadata suppression, embedded/subset non-Type-3 fonts, Unicode text, bookmarks, links, structure, public firewall, inspection completeness, and tool/resource identities; every single-field hostile mutation fails.

## Final assessment

The corrected supplement is strict-canonical, mechanically replayable, internally consistent, complete over its declared project and historical evidence universe, and sufficient to make a later retained dual build independently auditable without weakening any scientific, source, lifecycle, freshness, firewall, page, PDF, tool, or resource obligation. The twelve-file correction is exact, the rejected thirteen-file preimage is reproducible, and no residual inventory ambiguity remains. This PASS review creates only the authorized L32 node and does not itself authorize or open a build.

PUBLICATION_LOCK_R4_SUPPLEMENT_PASS
