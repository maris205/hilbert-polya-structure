# Test report

- Producer: PASS, 2,046 blocks and 20,480 coefficients.
- Producer-independent checker: PASS, all coordinates and six full kernels.
- SymPy: PASS, 46 symbolic/exact checks.
- Replay: PASS, two isolated temporary directories, 773,961 identical bytes.
- Hostile mutation: PASS, 59/59 rejected.
- Optimized execution: every script explicitly rejects both -O and -OO; the
  release gate exercises these refusals.
- PDF revisions: 2/2/2 pages, each built twice from fresh directories with
  identical bytes; final PDF has 21 embedded and subset font rows.
- Settled LaTeX warnings, overfull/underfull boxes, undefined references,
  missing characters, extracted control bytes and text sentinels: zero.
- Route-B and every forbidden scope flag: false.
