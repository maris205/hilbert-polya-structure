# Compile report

Each conditional manuscript round was built twice in fresh directories with LuaLaTeX under `SOURCE_DATE_EPOCH=1788480000`; both bytes matched the stored artifact.  Settled logs have no warnings or layout defects, all fonts are embedded and subset, extracted text has no control garbage, and every page rasterizes.

| round | pages | font rows | SHA-256 | substantive addition |
|---|---:|---:|---|---|
| 0 | 1 | 12 | `d2a3b47c4a71f2701b8a2ce9961bb91c73304279979bf51e98b0680d584fbc14` | Skorokhod construction, embedded Lindley chain, sharp drift trichotomy, and stable law |
| 1 | 2 | 12 | `04e36c9bf5ec52957e5326938115d4867f98ee5b018b69c2fb9e32089dfe160b` | stationary mass, environmental marginals, all moments, and regulator rate |
| 2 | 2 | 16 | `522c7ef71180cd6ee2b1c31b86a0b7e9cc8845b7ea541fe6c04fc72a2566217a` | complete closed-class zero-rate atlas, source boundary, exact evidence, and route firewall |

`main.pdf` is byte-identical to round 2.
