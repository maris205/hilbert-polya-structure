# Paper 9 source-retention boundary

This directory contains exact local research copies used for page-level source
verification. Citation reproducibility and redistribution permission are
separate questions.

Public GitHub synchronization must exclude `*.pdf` unless a redistribution
licence has been documented for that exact PDF manifestation. The local files
are retained. Public audit material should keep:

- `paper9_source_manifest.md` and `paper9_sources.sha256`;
- exact titles, versions, canonical URLs, and page/theorem locators;
- the ARS preflight sidecars; and
- SHA-256 hashes of the locally retained bytes.

The adjacent `.gitignore` enforces this default. A later licence review may
whitelist one exact PDF without weakening the boundary for the rest of the
corpus.
