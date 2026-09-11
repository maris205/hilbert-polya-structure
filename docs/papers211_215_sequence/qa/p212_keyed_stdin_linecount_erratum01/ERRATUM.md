# P212 keyed-stdin source handoff: line-count erratum

2026-09-09 UTC. Root documentary correction only; same independent auditor's
exact delta and full root source reception are still pending. This is not
an observer, input-creation, live-application or runtime grant.

The frozen source handoff at
`qa/p212_keyed_stdin_source_delta01/HANDOFF.md` states:
“The seven programs are 2,779 lines / 148,546 bytes.”
The line count is a transcription error: the correct statement is
“The seven programs are 2,679 lines / 148,546 bytes.”
Only that count is corrected. The frozen handoff, its original seal and
all source, data, contracts, captured outputs and findings remain unchanged.

Root's actual `wc -l -c` returned exit 0 (native chunk `abb65c`):

| Program | LF lines | Bytes |
|---|---:|---:|
| observe.py | 436 | 22,106 |
| driver.js | 1,048 | 55,092 |
| outer_contract.py | 747 | 41,004 |
| python_runtime_probe.py | 146 | 8,600 |
| node_runtime_probe.js | 66 | 5,001 |
| node_preload.js | 147 | 10,913 |
| product_capture.js | 89 | 5,830 |
| Total | 2,679 | 148,546 |

`WC_NATIVE.json` contains that exact request and complete native return.
`check_delta01.cjs` independently counts LF bytes, verifies each full source digest
against the unchanged handoff, compares the entire source manifest and all
55 payloads, and checks the old/new program delta counts as documentary text.
It does not load, parse as programming-language source or execute any of
the seven programs. Its actual result is in `CHECK_DELTA_NATIVE.json`.
The first checker wrongly expected `./` in this package's bare-relative
manifest and exited 1 before inspecting its payloads. That unchanged
`check.cjs` and actual `CHECK_NATIVE.json` failure are retained. The new
checker changes only this package's exact path prefix and its diagnostic;
it does not accept an alternative path syntax or relax digest checks.

The arithmetic is 2,519 original program lines + 204 inserted − 44 deleted
= 2,679. This correction makes no fresh claim about the handoff's separate
19-derivative total or the validity of the program semantics; those remain
within the independently reviewed source package. It does not change any
mathematical claim, native-field policy, failure boundary or source hash.

The exact unchanged handoff SHA-256 is
`da09c9697133988256adec01aa4e5df66bc02aa99588edfef204a8471d9db9d8`;
its complete source-package nonself-manifest SHA-256 is
`f076522fc7e120c46be0c57b60168784c38c32339e07f65b74e0012694ca1ee8`.
The original independent audit must retain the open Minor at its original
endpoint. Only a later exact-combination delta may close it. Root authored
this documentary erratum and does not claim to be its independent reviewer.
