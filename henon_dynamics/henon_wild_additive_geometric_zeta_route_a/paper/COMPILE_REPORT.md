# Compile report

Every round was built twice in fresh directories at epoch 1788566400, with two LuaLaTeX passes per build. Each pair is byte identical. All fonts are embedded/subset, all pages rasterize and settled logs contain no warning.

| round | pages | fonts | bytes | SHA256 |
|---|---:|---:|---:|---|
| 0 | 2 | 16 | 83707 | 97a84b7ed74f8aabbb6830479ad87900a36fb28f9c734739c51cfc18a078d195 |
| 1 | 3 | 16 | 96241 | 1c6b8189a951266ed239102e460c56ad8b897a66f9f9030ef3e677b3d15f171c |
| 2 | 5 | 16 | 116046 | 045a29475418bc1de741e5058f7d69f7e24bd25c2e01f6c3408473c2959e3481 |

main.pdf equals round2. Round0 establishes the geometric/length split; round1 adds every extension and both clocks; round2 adds the meromorphic natural boundary, tail certificates and source/target audit. Raw settled logs are retained as .txt files.
