# Browser transport provenance

These are the actual requests whose complete returned text strings are
preserved alongside this file. Stored citation/ref tokens are transport
metadata, not standalone source identities. No browser result is a native
shell receipt, and no unreturned image or full-text body is invented.

1. `sowing_search.txt`: search queries `mancala solitaire finite dynamical
   systems recurrent configurations austrian sowing` and `periodic orbits
   deterministic sowing game mancala cycle dynamics`; long response.
2. `source_open_and_403.txt`: direct opens of
   `https://www.sciencedirect.com/science/article/pii/S0012365X15001466` and
   `https://arxiv.org/html/2304.10917`; long response. First returned 403;
   second returned Austrian-solitaire text used only as a discovery boundary.
3. `mancala_search.txt`: queries `"An optimal bound on the number of moves for
   open mancala" arxiv` and `"open mancala" "Theorem 1" Musesti Paolini Reale`;
   long response.
4. `mancala_primary_and_404.txt`: direct opens of
   `https://arxiv.org/html/1310.8088` and `https://arxiv.org/pdf/1310.8088`;
   long response. First returned 404; PDF extraction returned 23 pages and
   identifies arXiv 1310.8088v2. Only the returned text span is preserved,
   not a claim that all 23 pages were read.
5. `mancala_theorem_locations.txt`: find in the prior PDF response for
   `Theorem 5.9`, `D∗(n) =`, and `Definition 3.2`; long response. Exact
   returned line spans are retained, including adjacent material.
6. `screenshot_placeholders.txt`: screenshots requested for zero-based PDF
   pages 1 and 20; short response. Transport returned two reference-only
   placeholders and no image bytes. This is not a visual-reading record.

Earlier broad discovery searches for parallel carrying and generic queue
sorting were conversational-only and are not represented as complete
source-capture records. They support no asserted OM collision or novelty
boundary. No external model/API client was used. Bibliographic dates are
bounded to the identified publisher/author records; generated PDF title
dates are not treated as new publication dates.
