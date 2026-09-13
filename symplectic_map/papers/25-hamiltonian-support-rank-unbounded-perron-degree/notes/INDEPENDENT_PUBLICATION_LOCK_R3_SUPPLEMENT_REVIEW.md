# Independent Paper 25 R3 Publication-Lock Supplement Rereview

## Role, authority, and disposition

I am the fresh full rereviewer of the corrected R3 publication-lock supplement. I designed and authored neither the supplement nor either bounded correction. I previously found the Paper35 namespace defect, wrote nothing at that failed review, and began this rereview again from the canonical base rather than treating the corrections as sufficient evidence.

This review was conducted locally under the research-review discipline. Every build-root path was treated only as an inert JSON string. I performed no filesystem operation on a retained, proposed, Paper23, Paper24, R0, R1, R2, or R3 build root; compiled nothing; browsed nowhere; edited no existing byte; and did not touch Paper26 or open a build, finalization, or release gate.

Finding census: zero blocker, zero major, zero minor, and zero ambiguity.

## Opening identities and L29 universe

The rereview opened on the following exact immutable inputs:

- `BATCH_06_STATUS.md`: SHA-256 `e318494175d94b6561387f995d7c6d00d25ccd4786f791bc1a344201a9005469`, 294,804 bytes, 4,162 LF.
- `BATCH_06_IDEA_REPORT.md`: SHA-256 `b147211f991572cf03c1a1d85415eeb7e1be2be832eb1dc96814a00bf2fc6f4a`, 458,672 bytes, 8,404 LF.
- `experiments/publication_lock_r3_supplement.json`: SHA-256 `7867e5b6df855e4ff3fe8723a10bdb1746ed984acf76543ad167a3a6a24aa640`, 51,894 bytes, one LF, mode 0644, one link.

The controlling rereview gate occurred exactly once in each ledger. Before this sole review write, the project contained exactly 29 regular files and four child directories, 765,882 content bytes, 10,609 LF, and 1,002 UTF-8 path bytes across the regular-file paths, with zero symlinks and zero other nodes. The review path was absent and was not a symlink.

## Independent strict-JSON and chain replay

I used two independent duplicate-rejecting implementations: a Python parser with an object-pair duplicate hook and nonfinite rejection, and a separate recursive-descent JavaScript parser with its own duplicate detection and canonical serializer. Both consumed the base lock and all three supplements through physical EOF. Each input was valid UTF-8, had no BOM, CR, or NUL, consisted of one canonical JSON line plus one terminal LF, used recursively sorted keys and compact separators, contained no duplicate key or forbidden numeric value, and round-tripped byte-for-byte.

The exact layer identities were:

- base lock: `414f7665ef2216c8e147e1a89ba3f01e64cd9823f651b341a0691983a7955081`, 69,835 bytes;
- R1 supplement: `d88fa75747247e5fe9553a0a71d05fddeccb7aad0e2fc3ed77bc1ec3401f1728`, 32,374 bytes;
- R2 supplement: `72506bff83d86a693f131185c611616d9d9649fa8cb5c90fc8cafb6eb7adf60e`, 44,496 bytes; and
- corrected R3 supplement: `7867e5b6df855e4ff3fe8723a10bdb1746ed984acf76543ad167a3a6a24aa640`, 51,894 bytes.

Mechanical JSON-Pointer application, with no copied effective object, reproduced:

- R1 effective: 75,264 canonical bytes / `8c92a2469a415736de6658ebed4710a19b8f59cedfa1c4dbd60f9a3f9ca15aaa`;
- R2 effective: 81,582 canonical bytes / `341c9fdb89602befa7dc02c4185d68452e8e6e8d076f8324e6fe9a81dee54d98`; and
- corrected R3 effective: 84,176 canonical bytes / `6b5265809ad32f8e3dabd9aa51f42ce76a9f9aa7f6635061b7d7aa3e64112d96`.

The R3 supplement's effective byte-count and SHA-256 metadata equal that independently replayed object exactly. The design-only 84,279-byte prototype remains expressly superseded provenance and is not used as an acceptance oracle.

## Correction provenance and exact R3 overlay

Starting from the current supplement bytes, replacing only the effective-identity metadata value with the prior replay hash reconstructs namespace-corrected preimage SHA-256 `cdd07bd54a48e8ac4388b15a20b0fd8a3ebee0df1fafcc3ae4b6fd1b1a64c309`. Replacing the six namespace digits at zero-based byte offsets 28,771, 28,877, 28,985, 29,379, 29,707, and 29,749 then reconstructs the original defective supplement SHA-256 `3ff00159fc3b6a924d08bdc7e20ce056d0cf35c0a14c08459a70f8373f50e3f2`. Those six bytes are the complete first correction; the sole later change lies inside the declared 64-byte effective-identity metadata leaf. The current supplement contains zero `Paper35`, `PAPER35`, or `paper35` residue.

R2-to-R3 target-aware comparison gives exactly six ordered `replace` targets and no seventh change:

1. `/build_contract/clean_dual_build/build_A_root`, value hash `f3e3d313e4a966ead5cfa4b503ed50f4983dcb207084b3261fa2d4944cd8902d`;
2. `/build_contract/clean_dual_build/build_B_root`, value hash `80504fb884c963bf47ea17e1518185f3b641b19bb07a09554b27dd2f992cd619`;
3. `/build_contract/clean_dual_build/freshness_rule`, corrected value hash `3395be572d7b52b785a470076856fdf7f05f8c1b082f3f54e20d5346d6dbd39a`;
4. `/build_contract/clean_dual_build/historical_root_firewall`, value hash `fa262f3ef26f34608d020f2c095db49b13fe53cf4855ef2c2d15b215c3771904`;
5. `/build_contract/inspection/cross_build_command`, value hash `5fd44176ab892c8b2ba7d3b5696d6352b875a847e28c7f7dfab1986e627b3bbf`; and
6. `/build_contract/failure_and_warning_policy/earlier_pass_only_allowlist`, value hash `129f60bc71e2fa64a8408cdabfd9778206d24dbabc5efd7bbb2c7d980c8f15f7`.

The corrected freshness gate and both embedded freshness roots agree with the adjacent Paper25 R3 A/B roots, the future parent gate, and the cross-build command. The inherited R1 hard-failure exception is unchanged and has canonical SHA-256 `00a011644f44a6adbcc1235df27a263ac36770db9f42544bf5b0748d3886e729`.

## Source, review, ledger, evidence, and inventory bindings

Every one of the 28 pre-supplement manifest records matched its current regular file in path order for path, type, mode 0644, one link, byte count, LF count, SHA-256, UTF-8 and terminal-LF state, and BOM/CR/NUL exclusions. The prescribed frame grammar independently produced 715,435 bytes and SHA-256 `501928619ff924f6e14f6bcb936e64ce277ab65c0b547746fccb74b96818c2be`, from 713,988 content bytes, 10,608 LF, and 955 path bytes. Adding only the self-excluded supplement gives the exact L29 universe above.

The repaired source trio matched its three bound identities. Removing the nine exact LF-framed main-source insertions in memory reproduced predecessor `paper/main.tex` at 69,850 bytes, 1,174 LF, and SHA-256 `cd149cfaa4881857629f130ccfe69733a199c79881394ae7d595108096792883`; the repair is exactly 6,193 bytes and 18 LF.

The base, R1, and R2 independent lock-review files and the final source-review precedent matched their bound hashes, sizes, modes, one-link states, and unique final terminals. The author-time STATUS ledger is its exact current-file prefix at 284,689 bytes / 4,026 LF / `6bc9bea2f0c1a80474d22726df183a54f0c2fc694c3fd415a3ef6a2581bbed43`. Removing the two later bounded IDEA insertion regions in memory reproduced the author-time IDEA ledger at 450,462 bytes / 8,278 LF / `fe7928e4f3aefc13d4b5792c0605c5fb81c5f6def656cfba60d7b8da46a83a7e`.

All four frozen R2 failure blocks independently matched their byte offsets, markers, byte/LF counts, and SHA-256 values: `551245456bd94fa339c1de66aace8a60fa73f54b9a7d7f914c45a5e567d8547c`, `bbacf28bde17820c8e8645aedd217919f490bb333b8ba821769626ff19c5337c`, `81fa494bcbe04dca9abfbba87508e0109816d7b4ba1756a7c2576e0d11caad25`, and `d1df2b208e527e683c4f0d377f99f477349b0f33405962b79cc23cddfbe01881`.

## Parser, pass-policy, and hostile suites

The event bindings have exact width arrays `[] / [] / [79] / [79] / [] / [] / [] / [77]`. An independently implemented byte-oriented reconstruction passed citation and reference joins only at width 79 and passed the zero-leading-space destination fixture only at the exact 77+28 split. Its joined 105-byte event has SHA-256 `9a92f52f157466f8a66ee498f748610bc537417911252567d639b9fb7eb78889`.

The executable negative fixtures rejected destination widths 78 and 79, citation/reference widths 77, 78, and 80, the historical two-leading-space synthetic fixture, changed destination fragments and continuations, joins for empty-width bindings, joining outside an open candidate, an incomplete candidate crossing a new diagnostic start, and consuming lookahead after a complete match. The rerunfilecheck semantic continuation preserved its boundaries and normalized to the exact allowed event. Ordinary prose containing warning-like terms opened no candidate and triggered no broad scan.

Pass one requires exactly one missing aux, missing bbl, undefined-references summary, and destination fallback; citation and reference ceilings remain 32 and 12 with the exact source multiplicity maps. Pass two permits only the two bounded rerun events. Pass three permits no diagnostic. Missing, duplicate, excessive, unclassified, wrong-pass, malformed, or independent merged events remain failures.

Separate in-memory canonical, chain, delta, root, firewall, lifecycle, and inventory mutations rejected duplicate or unknown deltas, reorderings, a seventh delta, changed targets, metadata mismatch, namespace typo, A/B swap, an R2 cross-build command, a weakened retained-root firewall, duplicate JSON keys, nonfinite or float tokens, noncanonical ordering/whitespace, broken line contracts, manifest drift, self identity, future-review placeholders, and unauthorized L29/L30 nodes.

## Inherited build and inspection obligations

Target-aware equality proves that every R2 effective subtree outside the six authorized targets is unchanged. In particular, the exact pass order, environment, source/input audit, allowed filenames, system resources, toolchain, deterministic-build rules, date rules, metadata suppression, direct-PDF rule, font/text checks, public firewall, and page/PDF inspection contracts remain inherited byte-for-byte. The pass-two and pass-three allowlist records are also unchanged inside the replaced allowlist.

The page contract still requires exactly 26 nonempty content pages through Conclusion, a standalone References heading first on physical page 27, and total PDF length at least 27. The PDF contract still requires the exact title; anonymous public metadata; empty private metadata fields; no dates, IDs, attachments, scripts, local/private links, hidden revision data, or build/governance leakage; embedded-font and structural validity; and exact public outline hierarchy. All tool and resource canonical hashes recorded by the supplement match the inherited effective subtrees.

The historical Paper23/Paper24 and retained Paper25 R0/R1/R2 firewall is complete and unconditional. The Paper25 R3 paths remain unaccessed strings until a later parent-controlled build gate, two ordered exact ENOENT probes, and one-time mode-0700 creation. Review success does not itself authorize those probes, a build, finalization, release, or any external effect.

## Final review conclusion

The corrected supplement is strict-canonical, mechanically replayable, internally self-consistent, complete over its declared source/evidence/inventory universe, and semantically faithful to every inherited build and inspection obligation. The two bounded corrections are exact and leave no namespace or metadata residue. All required positive and hostile suites pass with zero finding.

PUBLICATION_LOCK_R3_SUPPLEMENT_PASS
