# Paper 8: isotropy averaging and return traces

This project tests whether isotropy-character return traces can survive a fixed regular representation on an actual Deninger prime orbit, while keeping packet topology and scalar closed-point counting as separate mathematical types.

The final hierarchy is deliberately asymmetric:

- **Packet route — `NOT_TESTABLE`:** packet Hausdorff/local-compactness and a same-map packet restriction, disintegration, or compression bridge are not established.
- **Fixed chosen one-orbit route — `REFUTED`:** the character trace preserves the phase-weighted return comb, whereas the regular FNS trace gives only `Lf(0)`; a full finite rank-one corner rules out a normal extended-positive extension along that fixed map.
- **Positive-time scalar route — `PASS`:** rational closed-point counting yields a locally finite Radon ledger with coefficient one.

These verdicts do not define a determinant or prove A3/A4, Route B, a global all-prime operator, analytic continuation, or a Hilbert--Pólya statement.

## Project layout

- `paper/` — formal English manuscript, independent Simplified-Chinese abstract, native TikZ sources, bibliography, release PDF, and release audit;
- `notes/` — source manifests, proof handoffs, integrity records, review records, and composition blueprint;
- `code/` — deterministic control implementation;
- `experiments/` — reproduction entry point;
- `results/` — nine control ledgers and their deterministic manifest.

The release manuscript is [`paper/paper.pdf`](paper/paper.pdf); build and checksum details are in [`paper/README.md`](paper/README.md).

## Reproduce the controls

From `papers/8-isotropy-trace/` run:

```sh
./experiments/reproduce.sh
```

The locked run passed 18/18 tests, produced nine CSV files with 129 rows, and reproduced all artifacts byte-for-byte in two fresh generations. The SHA-256 of `results/isotropy_trace_manifest.json` is `20801ebe4c927f939c462842e38569555f96f5fef78859755b6caa8cbcf38b07`.

## Release lock

The 19-page PDF was built by XeLaTeX/BibTeX/XeLaTeX twice and audited with `pdfinfo`, `pdftotext`, `pdffonts`, log scans, citation-key comparison, and representative-page raster inspection. Its SHA-256 is `fad0f602edf4d2300b91bd7b356e363da3ab776c645288a14f39ae171aea262a`. All fonts are embedded. The only retained build notices are two harmless underfull boxes; there are no overfull boxes, unresolved citations/references, missing glyphs, or BibTeX warnings.

## Public-sync source policy

Do not include `notes/sources/*.pdf` in a public GitHub sync unless a redistribution licence is documented for the exact PDF manifestation. This repository's local research copies are left intact. Keep and synchronize the non-PDF audit material: source manifests, hashes, URLs, exact locators, and preflight sidecars.

