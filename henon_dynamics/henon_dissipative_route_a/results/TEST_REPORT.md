# Test report

- producer: `PASS`;
- independent exact checker: `C109_CHECK_PASS`;
- separate SymPy elimination/determinant check: `C109_SYMPY_PASS`;
- deterministic replay: `C109_REPLAY_PASS`;
- hostile mutations: `8/8` rejected and original bytes restored;
- fixed-date double PDF build: byte-identical;
- font/layout audit: embedded fonts and no overfull/underfull/undefined or
  duplicate-label warnings;
- forbidden-claim scan: only explicit scope/nonclaim language.

Evidence SHA-256: `aecb4f5d72dd1b515560719b30d148958ba295e72c1e07ce944e4fbb50b38156`.
Final PDF SHA-256: `e11f42c611072eb363603968e8d6ef4c60bcb0a299d02ed8418e03deee15a479`.
