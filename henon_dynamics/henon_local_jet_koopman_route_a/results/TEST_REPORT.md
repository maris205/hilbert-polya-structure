# Test report — C114

- producer: `C114_PREFREEZE_G3_PASS`;
- independent checker: `C114_CHECK_PASS` for all 225 matrix cells;
- separate SymPy reconstruction: `C114_SYMPY_PASS`;
- canonical replay: `C114_REPLAY_PASS`;
- hostile mutation audit: `C114_MUTATION_PASS 13 / 13`;
- paper: fixed-date isolated double build is byte-identical;
- PDF: two pages, all fonts embedded, no unresolved references, citations,
  overfull boxes, underfull boxes, or material TeX warnings;
- release manifest: content ledger closed after the final paper build.

The checker imports no producer code.  Mutation rejection is performed by
actually invoking the independent validation function on each altered
in-memory ledger.
