# Compilation report

- Engine: LuaLaTeX
- Fixed environment: `SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`,
  `TZ=UTC`
- Each revision round: two fresh build directories, two LuaLaTeX passes per
  build
- Fresh-build comparison: byte-identical within every round
- Final-pass warnings: none (`Warning`, `Overfull`, `Underfull`, `undefined`,
  `Missing`, and duplicate-destination scans are empty)
- Final pages: 2
- Final file size: 188,099 bytes
- Embedded/subset fonts: 25/25
- `main.pdf` equals `main_round2.pdf`: byte-identical

Round SHA-256 values:

- round 0: `4116fb67e5f08c209884164f3e81750fc8bf9b968c7aab508db692d1c846c47d`
- round 1: `b26f021b96a12a822b637782e1ede34a3f7a3cc776eaa6daaa309fe40a35adcc`
- round 2/final: `ff5bee778af4d778c73ffdc1e38b457d64e1babe5050bb16588b72023d035972`

All three hashes are distinct.  Round 1 adds the complete marked-orbit law,
finite distributional identity, and Rayleigh limit.  Round 2 adds the joint
quadrant limit, independent executable certificate, and strict scope/Route-A
boundary.
