# Round 10 Stage 4.5 Round 2 runtime compatibility repair

Recorded at UTC: 2026-09-05T03:51:58Z.

Result: PASS for the bounded runtime-path replacement. The three local audit tools now resolve the installed ARS runtime at cache version `0.1.28`. This result concerns runtime compatibility only; it does not constitute candidate promotion, a batch integrity verdict, or a Stage 5 authorization.

## Compared runtime roots

The formerly configured root `/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.26/` was absent at verification time. The original runtime remains available read-only at `/root/autodl-tmp/.codex/.tmp/marketplaces/.staging/marketplace-upgrade-0JRs4e/plugins/ars-codex/`. Its `.codex-plugin/plugin.json` declares version `0.1.26` and has SHA-256 `83df2e9c094559e35852cb3829befabbdb32e468c8c02bb4e8cf7897a8ceb16d`.

The active root is `/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/0.1.28/`. Its `.codex-plugin/plugin.json` declares version `0.1.28` and has SHA-256 `c2c872eed0a7b802c781a31207a997b6131b580f17fcf64e8162bc647e334bdf`.

Every runtime-relative path below is under `skills/academic-research-suite/ars/` in both roots. Direct byte comparisons passed for all seven files; each displayed digest and byte count is identical in the retained and active copy.

| Runtime-relative path | Bytes in each copy | SHA-256 of each copy |
| --- | ---: | --- |
| `scripts/evidence_rows.py` | 85359 | `eccfa0a5cfe9b438aac9c4ec85cd6c2ca07052de7eb521cfc1e7f799a971d7e3` |
| `scripts/claim_registry_coverage.py` | 18043 | `4a71dce80b8b600865a012b2672ee896a31f065423d4fd2e1fa8487a6174c9ea` |
| `scripts/check_compliance_report.py` | 3864 | `51ee2818aa36befdd86783d38143a7b4b523d48071d912fef8c4e2d114326f7b` |
| `scripts/_block_parser.py` | 14877 | `1ffdd0495af973312b4c19db3482512d7a582d7a98a4967e5e43159ee749369b` |
| `shared/contracts/evidence/claim_registry.schema.json` | 2324 | `4fac94d323855eff445e16528f7e1602e0bebd8d0d90805c224f710172c579bb` |
| `shared/contracts/evidence/claim_registry_coverage_report.schema.json` | 4940 | `69ffb0c8536a9a0864ed33b3735d41aed226b29d50077b8ef2641b732d69f142` |
| `shared/compliance_report.schema.json` | 8314 | `4e5d162f5ee64e52393720f0d47d204ea389d7d871649f234164329d4931caf2` |

## Dependency closure and execution checks

The builder directly imports `evidence_rows.py` and invokes the evidence, coverage, and compliance CLIs. The Ruby replay invokes those same three CLIs. The finalizer dynamically imports `_block_parser.py` through its `import_block_parser()` function.

The evidence and block-parser helpers use only the Python standard library. Coverage additionally imports `yaml`, `yaml.constructor`, and `jsonschema`; it loads the two listed coverage/registry schemas. Compliance additionally imports `jsonschema` and loads the listed compliance schema. There are no further plugin-local helper imports. All schema references in these three schemas are document-local `#/$defs/...` references; no external schema fetch is needed. This bounded comparison does not assert that the entire plugin versions are identical.

Both retained and active helper sets imported successfully in the same Python 3.12.3 process with bytecode writes disabled (`python3 -B`). The two coverage schemas and compliance schema from each root passed their official `Draft202012Validator.check_schema` checks. The actual local builder and finalizer imported successfully, including the finalizer's real block-parser loader. The imported builder evidence schema remained `evidence-row/1.0`.

External packages resolved in that process were PyYAML `6.0.2`, jsonschema `4.25.0`, attrs `25.3.0`, jsonschema-specifications `2025.4.1`, referencing `0.36.2`, and rpds-py `0.26.0`. No package or plugin content was installed or modified.

Ruby syntax check `ruby -w -c tools/audit_round10_stage4_5_round2.rb` returned `Syntax OK` with exit code 0. The Python import checks also established syntax validity without executing candidate generation or finalization.

## Exact local edits and frozen descriptors

Each local tool received exactly one literal substitution: the absolute plugin cache root ending in `/0.1.26/` became the same root ending in `/0.1.28/`. A reverse substitution on each post-edit byte stream reconstructed the corresponding recorded pre-edit SHA-256 exactly. No other behavior or content in these tools changed during this repair.

| Workspace-relative tool | Bytes before and after | Before SHA-256 | After SHA-256 |
| --- | ---: | --- | --- |
| `tools/rebuild_round10_stage4_5_p30_p31_dispatch.py` | 225888 | `0abf32c6b1c93a07db5d233d5edde4b16fffc1b8578eef2e1613c17efa7fba9e` | `c24f848afc99f10e6301b159c57cfa82e408dd45073a996a338c1d9cfd85fb8c` |
| `tools/audit_round10_stage4_5_round2.rb` | 62262 | `45816948d44caaefaf8d06b655c96b5e9b100a612826a7b1987ed0c49b080840` | `79ca4b364a0bbe7cdbd50b347ba8e7906476d5a00dba4f32fd590638b5d613a5` |
| `tools/finalize_round10_stage4_5_round2.py` | 72680 | `4d4af205a4ede3f8e71721c0bb5d6a0e3f60e3c594eac25a8b6e34fdb0e28b6a` | `783111115c18e3f35076cbe49dd8f98d8f7b4334f1954639530925aa633b5e08` |

This repair wrote only the three listed audit scripts and this audit-side compatibility note. It did not generate or promote a candidate, run network collection, change a protected/canonical/manuscript/Bib/science/result/Route/README/status artifact, modify either plugin root, or perform a Git operation. The enclosing task must rebuild stale candidates against these new tool descriptors and complete its independent evidence and batch replay checks before closeout.
