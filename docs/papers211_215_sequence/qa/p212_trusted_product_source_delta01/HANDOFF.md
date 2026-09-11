# Proposed P212 trusted-product source delta

Status: SOURCE_PREPARED_FOR_INDEPENDENT_REVIEW / HOLD_OPERATIONAL.

This new-only proposal explicitly selects ordinary trusted product/root-
observer/Bash/env and initial interpreter/import bootstrap, not independent
startup attestation. The original strict product_startup obligation remains
unsatisfied and immutable. The proposed evidence is conditional: independently
received finite file/configuration keys and discrete downstream observations.
The fixed provenance object always says product_startup_attested=false.

## Exact changed bodies

| Derivative | Lines | Bytes | SHA256 |
|---|---:|---:|---|
| outer_contract.py | 674 | 37210 | d4723b4405a96f7023df143ae5c7687b46f7fa933a731572fed26faf1549d266 |
| node_preload.js | 147 | 10925 | 93a68f29408b42c2f56d8fdc5cf5b5688af8bbffd78789a6e8fd27587b24d586 |
| product_capture.js | 86 | 5591 | 48e76a1ef2fdaadbb6d5f7addf706655eb876682d9b7d78f9dc5d0fd29005c99 |
| python_runtime_probe.py | 142 | 8373 | 15c9af65ba9923256a5b77bea0ceb3da16a6f63c72d4c2dd003d6d92803074c7 |
| node_runtime_probe.js | 66 | 5005 | ed79a360ce7fa4eb4daa23d63369180edd2ab5019b69ac2b55c6decd1e093ca8 |
| SOURCE_CONTRACT.md | 271 | 17023 | 45646957cdc74bba585aa8810ed5efa6ba0dfd8c9cf5f93a0f77fc9865d00f5a |
| RUNTIME_PREPARATION.md | 140 | 8844 | e832d553f7b9a1128b86ebaefab0e544cbc5b19e1715d3426f8bc153b2e0c8fd |
| SOURCE_ORIGIN.json | 141 | 9106 | 767f5c5966759b099ce67cb93e4c4f28804db533819f54bca6c556ee82f28961 |
| INTERFACE.disabled.json | 45 | 1163 | 0193d52a342a1c2db7086866f72f2b2b4548018c62e3cc145acff30113065de0 |
| READ_ENTRY_COVERAGE.md | 61 | 6501 | e49b0a45bcfe2554a40c962a077e8585574009b3eea3cbc1fa8fdc55a5479f70 |

The five source files total 67104 bytes. The ten derivatives total
109741 bytes and have ten complete actual diffs under diffs/. The coverage
baseline is the accepted corrected file, not the original PCE-D1 overclaim.
SOURCE_INPUTS.sha256 / INPUT_ROLES.json identify 48 finite external workspace
inputs and their read scope; eight live sources still match 20092 bytes.

The outer binding uses p212-contract-outer-trusted-product-binding-v1 and
ROOT_BOUND_TRUSTED_PRODUCT_CONTRACT_ONLY; the collector and probes also use
distinct trusted-product authorization schemas. The outer receipt role is
trusted_product_boundary, never a disguised satisfied product_startup.
Each probe now requires named source/bootstrap_key/trusted_product_boundary
references with distinct physical pathnames. No enabled argument is included.

Trust cannot replace the independent finite key before either author probe
or the complete fourteen-field pre-Node/tool key before operation. Source
relocation invalidates source/argv/__main__/preload/cache/request/binding pins;
TYPED_INVALIDATION_MAP states exact affected and preserved dependencies.
The accepted amended driver/four companions remain unchanged, as do ENV8,
interpreter flags/cache policy, DQD-O1 nonself ordering, actual frame/session
retention, no-signal lifecycle and all separate query/body/science/build gates.

## What was actually checked

All ten derivative bodies and actual diffs were fully read. Documentary
orchestration reconstructs all ten complete baseline/current texts through
68 literal edits and through actual diff hunks, and checks seven protected
source slices plus the five unchanged import surfaces. Whole ordinary byte
keys, actual requests/returns and final integrity checks are preserved.
This is author source inspection only: no runtime/syntax/import/AST or new
helper file was executed, and no independent verdict is claimed.

The original composite's accepted zero current source findings do not apply
automatically to this derivative. The old source audit, its OPEN PCE-D1,
actual correction and root acceptance keep their original scope. Collector
catch remains normalized name/message only; its Date.now budget remains
between returned calls; all candidate handles must be read from full frames.

## Required handoff

The next authorized step is independent nonauthor review of this sealed exact
source/provenance delta, then separate root original-source reception. Even
acceptance would not itself authorize an operation. Root must separately
receive the explicit trust decision, independent pre-probe bootstrap key,
authorized fresh runtime-only originals, full operational runtime/ABI/tool
key, exact new contract-only bindings and eventual actual capture originals.

Successful future help/version would still need separate option semantics
reception before lookup; lookup and body phases and first-build/manuscript
review/completion gates remain distinct. No host runtime/configuration/env
read, settings change, enabled binding, query, science, build, Git or external
action occurred here. Old packets and live sources remain untouched.
