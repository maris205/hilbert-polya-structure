# Test report

Run date: 2026-09-02 UTC.  Fixed epoch: `1788307200`.

| Lane | Result |
|---|---:|
| deterministic producer | PASS; 226 recorded audit cells |
| independent exact checker | PASS; 92,280 assertions |
| SymPy cross-check | PASS; 417 symbolic checks |
| canonical byte replay | PASS; two fresh JSON files equal archive |
| hostile JSON/YAML mutation | PASS; 58/58 rejected |
| manuscript revisions | PASS; three distinct PDF hashes |
| fresh builds | PASS; two fresh builds for each of three rounds |
| settled log scan | PASS; no warning/layout/reference/glyph matches |
| PDF fonts | PASS; 20/20/21 embedded and subset rows |
| visual inspection | PASS; all 10 archived pages inspected |
| scope firewall | PASS; all nine forbidden-claim flags false |

The direct word lane exhausts all `3^n` rooted words through `n=10` inside
the independent checker and records producer counts through the same bound.
Finite tests are regression checks only; the geometric theorem is proved by
compactness, no-eclipse, convexity, and strict convexity.
