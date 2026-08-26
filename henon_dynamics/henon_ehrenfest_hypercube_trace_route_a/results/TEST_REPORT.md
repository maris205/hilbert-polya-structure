# C171 exact test report

All mandatory validation layers pass:

- deterministic producer: pass;
- independent exact checker: 2,990 assertions, pass;
- brute closed-walk enumeration on \(d\leq7,n\leq8\): pass;
- SymPy characteristic/eigenvector reconstruction: 914 checks, pass;
- byte replay: pass;
- repaired-hash semantic mutations: 38 rejected of 38;
- stale-hash mutation: 1 rejected of 1.

The final release additionally requires deterministic double PDF compilation,
embedded fonts, zero layout/reference/glyph warnings and manifest closure;
these values are recorded in `paper/COMPILE_REPORT.md` and the release
manifest.  No network, citation database or target table participates.
