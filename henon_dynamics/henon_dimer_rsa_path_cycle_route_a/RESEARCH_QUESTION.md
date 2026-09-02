# Research question

For the dimer random sequential adsorption process on the finite path `P_n`
and the simple cycle `C_n`, can one close in a single exact theorem:

1. the full probability generating function at every finite size;
2. one triangular differential system generating every factorial moment;
3. the exact mean and the leading and constant terms of the variance;
4. every attainable jammed matching size, including empty/singleton and cycle
   domain boundaries; and
5. the precise boundary effect between a path and a same-size cycle?

The process samples a uniform permutation of labeled edges (equivalently, iid
continuous priorities) and greedily accepts an edge iff both endpoints are
unmatched.  The question concerns a jammed **maximal** matching, not an
optimization algorithm guaranteed to return a maximum matching.

The package also asks whether this exact stochastic-combinatorial theorem can
meet Route A.  It cannot: the finite edge order has neither a rational-prime
carrier nor prime-power repetition, a logarithmic prime clock, an analytic
target bridge, or a source-native Hilbert–Pólya operator.  The frozen tuple is
therefore `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.
