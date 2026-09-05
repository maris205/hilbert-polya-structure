# Reproducibility

Run every command with Python bytecode disabled. The release script executes producer, independent checker, SymPy, two-directory replay, repaired-hash and parser mutations, three smoke tests and all six scripts in both optimized modes (twelve refusals). It builds each of three papers twice in fresh directories; each build uses two LuaLaTeX passes at SOURCE_DATE_EPOCH=1788566400. Final PDF must equal round2 bytes. Embedded/subset fonts, settled warning-free logs, text checks and page rasterization are verified.

The manifest declares exact payload and physical membership and every file SHA256, together with raw and semantic YAML hashes. Nonwrite release repeats all checks and compares the complete manifest. Raw compiler logs are never edited. Mathematical proof and prose are not claimed to have deterministic generative provenance; only frozen artifact reconstruction is byte deterministic.
