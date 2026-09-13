# Independent Paper 25 R2 Publication-Lock Supplement Review

## Verdict

PASS. I found no blocker, major issue, minor issue, or unresolved ambiguity in the Paper 25 R2 publication-lock supplement. The strict-canonical supplement, its chained overlay, the repaired source binding, the complete predecessor inventory, the candidate-local log grammar, the historical-root firewall, and the inherited publication contract are mutually consistent and independently reproducible.

This review is limited to the R2 publication-lock supplement. It does not authorize or perform a build, PDF inspection, release, repository operation, cleanup, network action, Paper 26 action, or access to any retained or proposed build root.

## Authority and read boundary

I acted as a fresh independent supplement reviewer under the exact gate `PAPER25_R2_PUBLICATION_LOCK_SUPPLEMENT_REVIEW_OPEN`. Before testing, I read both controlling ledgers and every file in the L27 project universe through physical EOF.

The current ledger measurements were:

| Ledger | SHA-256 | Bytes | LF | Gate count |
|---|---:|---:|---:|---:|
| `BATCH_06_STATUS.md` | `4c111cacb1de717512c35910f9e43794d710cdd7215b1c7bc182dac92ea8fe88` | 265336 | 3764 | 1 |
| `BATCH_06_IDEA_REPORT.md` | `c32b959d3c8123f6f989a5351c42da8a21ee2593a0cd975c2682e4a26336e154` | 432956 | 8002 | 1 |

The predecessor universe contained exactly 27 regular files and four directories, with no symlink or other node, totaling 691125 bytes and 10443 LF. Every file was mode 0644 with link count one, every directory was mode 0755, and every file satisfied its UTF-8, terminal-LF, BOM/CR/NUL, byte-count, LF-count, and SHA-256 binding. I did not list or glob a project parent; the audit visited only the exact bound paths.

I performed zero filesystem operation of any kind on every retained Paper 23, Paper 24, Paper 25 R0, and Paper 25 R1 root and on both proposed R2 root strings. I did not list their parents. I did not compile the manuscript, execute a PDF inspection command, use the network, or touch Paper 26. The only successful write in this review is the creation of this review file after all tests passed.

## Externally measured inputs

| Object | Measured identity |
|---|---|
| R2 supplement | `72506bff83d86a693f131185c611616d9d9649fa8cb5c90fc8cafb6eb7adf60e`; 44496 bytes; 1 LF |
| Repaired `paper/main.tex` | `cd149cfaa4881857629f130ccfe69733a199c79881394ae7d595108096792883`; 69850 bytes; 1174 LF |
| `paper/math_commands.tex` | `c748e0cde8aadef85c5de9e1fa20efb7770d07fb3fde58dfe0f4fe738720edf0`; 393 bytes; 11 LF |
| `paper/references.bib` | `159acd5633b19f3f91c203d4f85375cfe5ddaaee6337fd5297c673ac1b9ad99d`; 3450 bytes; 118 LF |
| Base publication lock | `414f7665ef2216c8e147e1a89ba3f01e64cd9823f651b341a0691983a7955081`; 69835 bytes; 1 LF |
| R1 supplement | `d88fa75747247e5fe9553a0a71d05fddeccb7aad0e2fc3ed77bc1ec3401f1728`; 32374 bytes; 1 LF |
| R1 supplement review | `65b183cf328fb10bb8281a65d3a3a37b9023448bc431230589b4ffdd20f9f231`; 21855 bytes; 348 LF |
| Repaired L26 frame | `88746eda95fc096a19c00d51295e3a680879599e74727e42c4e8c01ca188b9f8`; 647939 bytes |

The repaired L26 frame independently reconstructed as 26 files, four directories, 646629 content bytes, 10442 LF, and 850 UTF-8 path bytes. Its 44-byte NUL-terminated header and every `uint64_be(path length) || path || uint64_be(content length) || content` record were regenerated directly from the 26 exact files. The result matched the bound frame byte count and digest. Adding only the self-excluded supplement produced the measured L27 totals above.

## Strict canonical JSON and chained replay

I used two genuinely independent implementations.

The first was a Python validator with a duplicate-rejecting object-pair hook, explicit rejection of floating-point and nonfinite tokens, recursive Unicode-code-point key-order validation, UTF-8 compact serialization with `ensure_ascii=false`, and an exact one-terminal-LF byte round trip. The second was a Node program with its own recursive-descent JSON parser, integer lexer, duplicate-key rejection, Unicode-code-point comparator, and canonical serializer; it did not call `JSON.parse`.

Both implementations accepted the exact base, R1 supplement, and R2 supplement and produced the same chain:

1. Replay the exact seven ordered R1 operations against the verified base: 75264 canonical bytes, SHA-256 `8c92a2469a415736de6658ebed4710a19b8f59cedfa1c4dbd60f9a3f9ca15aaa`.
2. Deep-copy that verified R1-effective object and apply the exact six ordered R2 replacements: 81582 canonical bytes, SHA-256 `341c9fdb89602befa7dc02c4185d68452e8e6e8d076f8324e6fe9a81dee54d98`.

A direct base-to-R2 shortcut produced a different byte count and digest and was rejected. A target-aware recursive comparison, stopping only at authorized targets, found exactly these six differences and no seventh difference:

1. `/build_contract/clean_dual_build/build_A_root`
2. `/build_contract/clean_dual_build/build_B_root`
3. `/build_contract/clean_dual_build/freshness_rule`
4. `/build_contract/clean_dual_build/historical_root_firewall`
5. `/build_contract/inspection/cross_build_command`
6. `/build_contract/failure_and_warning_policy/earlier_pass_only_allowlist`

The supplement contains no self digest or self octet count, and its L27 aggregate excludes its own content as required. It also assigns no future review digest, size, LF count, mode, link count, or terminal-count placeholder. These exclusions were checked structurally as well as by hostile mutations.

## Overlay, root controls, and lifecycle

The two proposed R2 roots occur only as unaccessed strings. Root A and root B are distinct, correctly ordered, and embedded only where authorized; the sole root-qualified inherited command compares the two direct pass-three PDFs using the exact new R2 paths.

The freshness rule is closed and stateful. It requires the parent-controlled dual-build gate before any root operation, then one non-following exact-path probe of A followed by one of B, with ENOENT required for both. Any successful metadata result, including a live or broken symlink or any file, directory, or other node, is presence and a hard stop. Only after both ENOENT results may A and then B each be created once as empty mode-0700 directories. `mkdir -p`, following probes, retries, recreation, cleanup, deletion, renaming, continuation, and reuse are forbidden. Once the first probe sequence begins, neither path can ever again be a freshness candidate, and any created evidence remains retained after success or failure.

The historical firewall preserves every exact Paper 23 and Paper 24 prohibition, the rule covering all other Paper 24 temporary roots, both Paper 25 R0 roots, and both Paper 25 R1 roots. Its exact forbidden-operation list remains `access`, `list`, `stat`, `lstat`, `glob`, `touch`, `read`, `hash`, `copy`, `continue`, `retry`, `rename`, `clean`, `delete`, and `reuse`. In-memory deletion of either an R0 or R1 root or any forbidden operation was rejected.

The source-stage binding is exact: only repaired `main.tex` plus unchanged `math_commands.tex` and `references.bib`, in that order, are staged as independent mode-0644 copies. The source static census also matched the supplement: 26 citation commands, 32 citation mentions, 12 citation keys, nine labels, 12 reference uses, eight sections, 39 subsections, one table, zero figures, no appendix, and the three protected headings.

The lifecycle remains closed after this review. No build, release, archive, submission, repository action, PDF finalization, cleanup, upload, external message, or Paper 26 work is authorized. A later build still requires an explicit parent transition and its own gate; this review does not self-open it.

## Candidate-local event parser review

I implemented the R2 byte grammar from the supplement rather than treating it as prose. Logs were split only on LF. Width counted every preceding octet other than LF, including HT, SP, and CR. Candidate classification ignored only leading HT/SP while retaining those bytes. Post-dewrap normalization collapsed only ASCII HT/LF/VT/FF/CR/SP runs, trimmed boundary spaces, and performed no case folding.

The parser closed a candidate immediately after exactly one complete fullmatch and before lookahead. An incomplete candidate could not cross a following diagnostic start. The rerunfilecheck exception applied only to its two exact semantic-continuation lines, retained one LF boundary per line, and was bounded to two physical continuation lines. Every other continuation required an open candidate and an exactly 79-octet preceding physical line, and removed exactly the one LF without stripping or inserting any byte.

The pass classifier then enforced exact pass scope, total counts, per-key or per-label ceilings, the separately scoped inherited hard-failure exception, and rejection of every unclassified diagnostic or marker.

## Hostile-test matrix

All hostile inputs were in memory; none was written to a project or build root.

| Area | Accepted witnesses | Required rejections observed |
|---|---|---|
| Canonical JSON | Exact base, R1, and R2 byte round trips in both implementations | Duplicate key, float, NaN, noncanonical key order, BOM, CRLF, missing LF, extra LF |
| Overlay shape | Exact seven-operation R1 replay followed by exact six-operation R2 replay | Missing, extra/seventh, duplicate, reordered, unknown-pointer, wrong-pointer, and wrong-verb R2 delta |
| Chain integrity | Exact R1 and R2 effective identities | Base drift, R1 replay drift, direct-base skip, altered target set, and unauthorized effective difference |
| Root values | Exact A/B R2 strings and exact new cross-build command | Root typo, A/B swap, stale R1-root cross-build command, R0 deletion, R1 deletion, firewall-operation deletion |
| Freshness state | Gate; A ENOENT; B ENOENT; create A once; create B once | Pre-gate probe, reversed or following probe, non-ENOENT, live/broken symlink, regular file, directory, other node, permission result, `mkdir -p`, retry, recreation, cleanup, delete, rename, hash, list, reuse |
| Hard-wrap width | Exact 79-octet candidate-local join | 78-octet join, 80-octet join, join outside an open candidate, empty continuation |
| Boundary discipline | Complete summary followed by independent missing-aux event yielded two events | Fullmatch swallowing lookahead; incomplete candidate crossing or consuming a new diagnostic; independent diagnostic merged into prior event |
| Regression shapes | `ex|ist`, `in|put`, and `word|.` reconstructed without inserted space | Literal-whitespace-style corruption and non-79 reconstruction |
| rerunfilecheck | Two short semantic lines normalized to the one exact allowed event | Short nonsemantic continuation, continuation after closure, extra semantic line, wrong-pass leakage |
| Pass-one counts | Missing aux exactly one, missing bbl exactly one, summary exactly one, references.1 exactly one | Zero or two for each required event; summary zero/two; references.1 zero/two |
| Citation policy | Totals through 32 and every declared key ceiling | Total 33, per-key overflow, unknown key |
| Reference policy | Totals through 12 and every declared label ceiling | Total 13, per-label overflow, unknown label |
| Pass scope | Pass two accepted only zero/one bounded label and rerunfilecheck events; pass three accepted an empty diagnostic set | references.1 on pass two/three, missing/citation/reference/summary leakage on pass two, duplicate bounded rerun, any pass-three diagnostic or unclassified marker |
| Inventory and bindings | Exact repaired source trio, every non-main file, L26 frame, and exact L27 universe | Repaired-source byte drift, non-main drift, frame drift, L27 extra node, premature review node, future placeholder, self identity |

The `ex|ist` witness used the contract's exact two leading spaces and split the references.1 event after physical byte 79. The `in|put` witness split a valid citation event inside `input`; the `word|.` witness split immediately before the final period. Each reconstructed the exact normalized event because the hard-wrap boundary contributed no byte. Corresponding 78- and 80-byte cases failed.

The fullmatch test placed the complete undefined-references summary immediately before an independent `No file main.aux.` diagnostic and recovered two events. The inverse hostile test placed an incomplete 79-byte citation candidate before a leading-space diagnostic start; it failed at the untouched next-line index, proving that the new diagnostic was neither consumed nor merged.

## Inherited publication contract

The R2 supplement's seven compatibility bindings independently matched the exact canonical base subtrees:

| Bound subtree | Canonical SHA-256 |
|---|---|
| Allowed root filenames | `d0dac127a6ed18ecfe9cb1cfcb644fe4ad22bd925d8e7e0576e7a378349db55a` |
| Environment | `9bc9f895741e8bbd50f3d5c9b8ebca982a627874c11a87740c138a4d3bb16d86` |
| Per-build inspection commands | `8f88615ed8d1c876fef9a0f9e442df01b18971d153582a5fa70ca01b4a8b338c` |
| Pass order and commands | `d21eb4297853423daf3fa35a5f66b02063f48363cd8b4e016228d32393402b72` |
| Source and input audit | `d6e91f8a9a0230a8d1bfffa6d51e7854399ebda410f18c1ba684b7f73d672967` |
| Direct system resources | `b902e5d3355a329cb65d630e1f1142d01abcd25f924f05b4ac3681c54e6a0a51` |
| Toolchain | `a76d23d183dc7eae936c533d159bad51f6d1bbe3689b753af85624328eddd959` |

The inherited R1 hard-failure exception array also matched `00a011644f44a6adbcc1235df27a263ac36770db9f42544bf5b0748d3886e729` and remained scoped only to the exact pass-one references.1 event.

I verified all 14 frozen tool binary or module byte identities. Under the exact clean environment, a read-only `kpsewhich` resolution of the 19 explicitly named direct TeX resources returned system paths and every resource matched its frozen SHA-256. This was resource verification only: no TeX engine, BibTeX pass, publication inspection command, or build-root command ran.

The four pass commands and their order are byte-for-byte inherited. The environment remains `env -i` with the exact declared map, unset HOME and CODEX_HOME, disabled shell escape, and administratively disabled network. The direct-PDF rule still permits only the third-pdflatex output and forbids a rewrite, normalizer, extra pass, retry, wrapper, or postprocessor.

The FLS and source-input audit remains unchanged: pdfLaTeX source-origin inputs are exactly `main.tex` and `math_commands.tex`; BibTeX alone reads `references.bib`; generated inputs are bounded; all other inputs must be frozen system transitive resources; and home, workspace, network, hidden, substitute, or unlisted project inputs fail.

The determinism requirements, A/B byte identity, inspection-output identity, source and return-code identity, metadata and XMP suppression, embedded/subset font and ToUnicode rules, raw/layout text integrity, zero-raster rule, outline hierarchy, public-surface firewall, absence of private paths and governance data, and ordinary-public-link rule are all inherited unchanged.

The page contract is likewise unchanged: exactly 26 nonempty content pages from Abstract through Conclusion, Conclusion on physical page 26, the first standalone References heading on physical page 27, no earlier standalone References heading, and references only from page 27 onward. The source still has the sole `clearpage` before the bibliography, no appendix or supplement, and an explicit public References bookmark.

## Read-only harness diagnostics

Three transient harness assertions occurred before the recorded passing reruns: an initial citation-census regex was mistyped, the first event-fixture invocation looked for the R1-added exception in the immutable base object, and the first resource-binding map selected the full source-basename object instead of `clean_dual_build/allowed_root_filenames`. Each stopped before producing a result, involved only already-authorized reads and in-memory state, and caused no write, build-root operation, compilation, inspection, or external effect. The corrected implementations were rerun from the exact inputs and all results above passed.

## Findings and stop state

| Severity | Count |
|---|---:|
| Blocker | 0 |
| Major | 0 |
| Minor | 0 |
| Ambiguity | 0 |

The supplement is internally complete for its stated role. This PASS consumes only the authorized review-file creation. It leaves both proposed R2 roots unaccessed, all retained roots firewalled, all existing project bytes unchanged, and every build/release authority closed pending an explicit parent transition.

PUBLICATION_LOCK_R2_SUPPLEMENT_PASS
