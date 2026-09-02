# Test report

The final release gate records exact command outputs.  Required lanes are:

- deterministic producer and semantic evidence self-hash;
- independent checker with exact recomputation and strict JSON/YAML trees;
- independent SymPy identities;
- two isolated, byte-identical replays;
- repaired-hash and stale-hash hostile mutations;
- explicit rejection under `python -O`;
- fresh double LuaLaTeX builds for three substantive rounds and final alias;
- embedded/subset fonts, text sentinels, visual page inspection, warning scan, exact file ledger, and manifest stability.

Final closure passed: producer 123 rows; checker 1070 assertions; SymPy 259 exact symbolic checks; replay byte identity; and 43/43 hostile mutations rejected.  The checker failed explicitly under `python -O`.  The three archived PDF rounds contain 1, 2, and 3 pages with 15, 16, and 17 embedded/subset font rows; each matched two fresh builds byte for byte and had a warning-free settled log.  The release ledger contains exactly 28 physical files and 27 self-excluding manifest payloads.

Frozen hashes:

- evidence: `01ab53a54c00ec80c3dc6ccefbd827b35c001ebbd38a4cf1ce6ccefad9eb261c`;
- semantic evidence payload: `b1769b06886aa9443e8ac7922a52e41c7a3a10c1fbe42681f2f219783508d605`;
- final PDF: `0ddd3fad510c184a999ad785ab7ac1af170b66169f15b54bda92b9fcb5e1e8bd`.
