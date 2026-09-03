# Exact evidence plan

The proof is algebraic.  Computation is a regression and hostile-ownership
audit on the 13 prime powers
`5,9,13,17,25,29,37,41,49,53,61,73,81`.

For every field, the producer records the characteristic, extension degree,
canonical irreducible polynomial, all nonzero quadratic residues, graph
parameters, adjacency spectral factors, Bass factors, and trace/primitive
counts through power 12.  The independent checker reconstructs 25,901
adjacency cells, 12,704 directed edges, and 369,848 legal nonbacktracking
transitions.  SymPy separately expands the low-order trace logarithm and
checks prime-field characteristic polynomials.

Acceptance requires producer, independent checker, SymPy, isolated byte
replay, every hostile mutation, optimized-Python rejection, three fresh
deterministic LuaLaTeX round builds, embedded/subset fonts, raster/text gates,
and exact 27-payload manifest closure.
