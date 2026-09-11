# P215 current02 initial artifact reception

2026-09-11 UTC. Root's complete receiver passed 216 checks over the actual
run02 tree. The controller and all 14 supervised commands exited zero; all 25
captured stderr-role files are empty. The exact inventory is 160 files across
eight pass snapshots and final artifacts. Runtime, live-source and cold-source
before/after reports are raw-equal.

The final FLS has 249 lines: 245 ordered INPUT events, three ordered OUTPUT
events and the exact cold PWD. Its 67 unique absolute inputs are all present
in the freshly bound 227-row runtime manifest. Relative inputs are exactly the
eight source roles plus generated AUX/BBL roles. The four TFM resources absent
from run01 are explicitly present in current02's binding; no further current
FLS input is uncovered.

All snapshot PRESENT manifests match their complete bytes. The final six
products match FINAL_PRODUCTS.sha256. BibTeX used two entries with zero
warnings; 16 listed fonts are embedded, subset and Unicode mapped. The only
diagnostic match is the informational main.log line enabling file:line:error
messages. Extracted text contains the title, principal results and both
bibliography authors.

The accepted PDF is six A4 pages, 200910 bytes, SHA256
68b00073dda65e211dfb1ff518729df81b5631b0a75301b37cf6d7465e9f6784.
It and all six page PNGs are raw-equal to the already viewed run01 rendering,
so every current02 final page is actually inspected. run01's resource HOLD and
failed root receiver attempts remain historical evidence. Independent artifact
audit is still required before PDF adoption and Round0; this receipt alone
does not freeze the paper.
