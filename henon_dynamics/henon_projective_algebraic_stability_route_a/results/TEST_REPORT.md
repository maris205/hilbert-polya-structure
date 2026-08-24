# Test report — C121

- producer: `C121_PREFREEZE_G3_PASS`;
- independent checker: `C121_CHECK_PASS` for eight recursive iterates,
  projective geometry, orbit witnesses, and controls;
- separate SymPy reconstruction: `C121_SYMPY_PASS 97 exact symbolic checks`;
- canonical replay: `C121_REPLAY_PASS` through \(n=8\);
- hostile mutation audit: `C121_MUTATION_PASS 16 / 16`, including explicit
  rejection of A1 overpromotion and A3 softening;
- paper: fixed-date isolated double build is byte-identical;
- PDF: two pages, all fonts embedded, with no unresolved references,
  citations, overfull boxes, underfull boxes, or material TeX warnings;
- release manifest: content ledger closed after the final paper build.

The checker imports no producer code.  The degree-256 endpoint is replayed by
an exact recursive DAG, leading-term induction, and exact probes rather than
by trusting an expensive full expansion.
