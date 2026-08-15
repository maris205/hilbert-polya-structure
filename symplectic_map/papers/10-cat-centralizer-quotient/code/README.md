# Paper 10 exact centralizer audit

This package implements only the source-locked, nine-modulus exact audit for
`cat_centralizer_cyclic_torsor_v1`.  Its scientific inputs are literal
constants: the cat matrix `((2,1),(1,1))`, moduli
`(2,3,5,7,11,4,6,9,10)`, and the prime-only reversing controls
`(2,3,5,7,11)`.  No command accepts a scientific argument.

The direct engine enumerates matrices, vectors, and group orbits in each
finite module.  The algebra engine independently constructs `aI+bA`, its
units, determinant/norm image, torsor map, and norm fibers.  A registered row
is accepted only when both engines and the proof-derived frozen ledger agree
exactly.

The execution package is closed-world: strict JSON rejects duplicate and
non-finite values; all evidence uses stable regular-file reads; the code-tree
hash is framed; an AST scanner rejects unreviewed executable changes,
network/process/data-loader/dynamic-import capabilities, float literals, and
hidden modulus literals.  The registered command writes an exclusive durable
claim before importing the candidate and may run only after a hash-bound
independent `DEPLOYMENT_PASS`.

The sole run reports exact integers, booleans, sets, and rational strings.  It
does not evaluate `s`, `log(q)`, or `q^(-s)`, access prime/zero data, scan a
modulus, use randomness, or construct an equivariant, stacky, Hecke,
transfer, Fredholm, or quantum mechanism.
