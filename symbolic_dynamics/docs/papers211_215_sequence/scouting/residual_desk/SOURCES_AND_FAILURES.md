# Desk source observations and retained failures

2026-09-08 UTC. These are live browser text observations, not downloaded
source-byte capsules or page-visual certification. The evidence scopes and
mathematical deductions are in REPORT.md. No source body was copied locally.

Successful actual primary openings:

1. https://arxiv.org/pdf/1401.4250v4 — application/pdf, 71 pages, 3,571
   extracted lines. Definition actually read through find/open: 2215–2260
   (printed pages 44–45), (6.1) at 2228–2249. The initial extracted contents
   and introductory Toom–Tsetlin discussion also appeared; no full read claim.
2. https://link.springer.com/article/10.1007/s00373-024-02751-2 — publisher
   HTML, 668 extracted lines. Read 327–330 for joins and immediate theorem.
3. https://arxiv.org/html/1408.1886 — primary HTML, 595 extracted lines.
   Read 66–73 and 294–306 for parity-based alternating runs/compositions.

Public source search queries (no private manuscript text sent):

- `"pop-stack" "alternating" permutation`
- `"pop-stack" "consecutive patterns" "123" "321"`

The searches exposed the primary Defant–Zheng publisher page
https://www.sciencedirect.com/science/article/abs/pii/S0196885821000300,
with neighboring dynamics/fertility statements and Proposition 3.7 text.
Other returned leads were not promoted to theorem inputs or ownership proofs.

Actual failed primary retrieval:

    open({"ref_id":"https://par.nsf.gov/servlets/purl/10301360"})

Returned error text:

    Failed to fetch https://par.nsf.gov/servlets/purl/10301360: (400) Timeout fetching

This was one actual browser request failure. No locally read PDF, screenshot,
visual pass or full Defant–Zheng definition/proof read is asserted. Existing
author 404/screenshot/first-output limitations remain in their original files;
this desk does not rewrite them or count them as its own new executions.

The optional native jq lookup failure is preserved with its full mixed
read-only command/output in OPTIONAL_LOOKUP_NATIVE.json. The terminal exit
was 1 because `command -v jq` returned no path. Earlier two `nl|sed` displays
in that command succeeded; no scientific executable ran in that command.
