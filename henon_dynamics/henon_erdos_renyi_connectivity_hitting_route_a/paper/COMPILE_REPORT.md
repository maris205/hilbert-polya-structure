# Compile report

- Engine: LuaHBTeX/LuaLaTeX; fixed epoch `1788393600`, UTC.
- Every round is built twice in each of two fresh temporary directories.
- Round 0 contains the all-finite theorem but not the Gumbel section.
- Round 1 adds both the Poisson and non-isolated-component lemmas.
- Round 2 adds boundary/evidence/scope/source/AI-use material.
- Round 2 also contains the registry-checked C301/C291/C276 collision
  boundary added by the final cross-red-team hardening pass.
- Final `main.pdf` equals round 2 byte for byte.
- Second-pass logs contain no LaTeX/package warnings, overfull/underfull boxes,
  undefined references/citations, rerun requests, or missing characters.
- Every font row is embedded and subset; every page renders nonempty.
- The final raster was visually inspected for clipping, blank space failures,
  malformed equations, and control-character artifacts.

Exact archived outputs are:

| Round | Pages | Embedded/subset font rows | SHA-256 |
|---|---:|---:|---|
| 0 | 2 | 21 | `48422f1fd9f9a03a777f2ff7487d3e2a6d0c75f9b173b882ce52749bb4e0abf7` |
| 1 | 3 | 25 | `57adea30caf75026d6672365fc0eaae5bb4805be6dfb562d3cad408e5dd35953` |
| 2/final | 3 | 26 | `2d0b722327df4079b63dbe72cb1c757c176e59ff01cb1b953a8045ca63412916` |

The release manifest machine-checks these values and owns the final ledger.
