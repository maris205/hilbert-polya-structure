# Exact web query ledger

The six first query strings are in SCOPE.md. The next request used:

```json
{"open":[{"ref_id":"https://www.sciencedirect.com/science/article/pii/S0304397504007923"},{"ref_id":"https://dl.acm.org/doi/10.1145/69558.69560"}],"search_query":[{"q":"\"Concurrency in Heavily\" \"pdf\" Barbosa Gafni"},{"q":"\"Resource-sharing system\" \"Yeh\" \"pdf\" Zhu site:math.ncu.edu.tw"},{"q":"site:arxiv.org \"scheduling by edge reversal\""}],"response_length":"long"}
```

The two opens returned Internal Error. This request and the first two search
batches have exact strings preserved here/SCOPE and their complete native web
tool results in the conversation, not copied as reconstructed raw JSON.
None is represented as acquired primary proof.

The fourth discovery batch is preserved as an actual request/result object in
`web_discovery_04.json`:

```json
{"search_query":[{"q":"\"A Dynamic View of Circular Colorings\" arxiv"},{"q":"\"Resource-sharing system scheduling\" filetype:pdf"},{"q":"\"Concurrency in heavily loaded\" site:cos.ufrj.br"},{"q":"\"Concurrency in heavily loaded\" site:cs.ucla.edu"}],"response_length":"long"}
```

The final metadata request/result is `web_arxiv_metadata.json`:

```json
{"open":[{"ref_id":"https://arxiv.org/abs/math/0604226"}],"response_length":"long"}
```

Only three native body acquisition URLs were attempted; see SOURCE_REPORT.
Searches are owner discovery, not additional body acquisition routes. Native
`curl`, `pdfinfo`, `pdftotext`, `rg` and source `sed` commands have complete
untruncated generated logs in commands/, independent of web snippets or tool
display truncation. No fourth source or new route is authorized by this file.
