# Test report

Date: 2026-08-14

## Normal mode

- producer: PASS;
- independent checker: PASS;
- dependency hashes: 4/4;
- packet rows: 70/70;
- Abel rows: 5/5;
- unit/adversarial tests: 12/12;
- checker mutations rejected: 7/7.

## Optimized mode

- `python -B -O` producer: PASS;
- `python -B -O` independent checker: PASS;
- `python -B -O` tests: 12/12;
- optimized certificate core SHA equals normal core SHA:
  `069728ffb997068f5b7aff4cb2daad9f8faa2d6ef8f13f99703624fe993585be`.

## Document and format checks

- JSON parse: PASS;
- YAML parse: PASS;
- source UTF-8/control-byte scan: PASS;
- source trailing-whitespace scan: PASS;
- placeholder scan: PASS;
- `git diff --check`: PASS;
- LaTeX unresolved citations/references: 0;
- overfull/underfull boxes: 0;
- PDF fonts embedded: PASS;
- PDF metadata author: Liang Wang;
- PDF pages: 7.
