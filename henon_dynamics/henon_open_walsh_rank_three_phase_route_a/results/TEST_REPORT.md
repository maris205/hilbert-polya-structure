# C168 exact test report

- Producer: PASS.
- Producer-independent checker: PASS, 682 assertions.
- Independent SymPy reconstruction: PASS, 386 checks.
- Byte replay: PASS.
- Repaired-hash semantic mutations: 112/112 rejected.
- Stale-hash attack: 1/1 rejected.
- Spectral sentinels: all `1<=k<=24`.
- Fourier sentinels: all `1<=m<=24`, exact in `Q(i/sqrt(2))`.
- Hole-zero residue sentinels: all `1<=k<=24`.

The evidence file SHA-256 and PDF/build checks are recorded in the release
manifest and compilation report.  No finite cutoff is represented as the
proof of an all-`k` theorem.
