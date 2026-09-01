# Compilation report

- Engine: LuaLaTeX
- Fixed environment: `SOURCE_DATE_EPOCH=1788134400`, `FORCE_SOURCE_DATE=1`,
  `TZ=UTC`
- Each revision round: two fresh build directories, two LuaLaTeX passes per
  build
- Fresh-build comparison: byte-identical within every round
- Final-pass warnings: none (`Warning`, `Overfull`, `Underfull`, `undefined`,
  and `Missing` scans are empty)
- Final pages: 3
- Final file size: 184,885 bytes
- Embedded/subset fonts: 25/25
- `main.pdf` equals `main_round2.pdf`: byte-identical

Round SHA-256 values:

- round 0: `802b6d4d4eefa87e5d47f48b937030cc25528b402e032d9623609e66a9a0d825`
- round 1: `0aa02262c71052c5765aa4ae2ad9b2acef5faeced00e0bb91071093eb264468f`
- round 2/final: `0f81c47565325f0a1fd296f8de0af7468638bc9981f197b9ed08d4cacda80b52`

All three round hashes are distinct.  Round 1 adds the positive-count cycle
law and scaling theorem; round 2 adds the atomic failure boundary and release
audit.
