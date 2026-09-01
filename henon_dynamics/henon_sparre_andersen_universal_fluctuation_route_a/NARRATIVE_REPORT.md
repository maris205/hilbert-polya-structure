# Narrative report

The decisive simplification is to start from the time of the maximum.  Under a
continuous increment law, the maximum is unique.  Conditioning on its location
separates the walk into two independent blocks: a reversed positive-survival
block before the maximum and, after symmetry, another positive-survival block
after it.  Since the maximum must occur somewhere, the survival probabilities
convolve to one.  This identity alone forces the square-root generating
function and the central-binomial coefficients.

The positive partial-sum count is not a second unrelated calculation.  The
Sparre–Andersen cycle transformation records the count through positive-total
cycles and produces a bivariate generating function.  Symmetry reduces it to
the product of two copies of the same square-root series, so the count and the
maximum time share the discrete-arcsine law.  Their common scaling limit is the
classical arcsine distribution.

The no-ties hypothesis controls the full theorem.  A two-step simple symmetric
walk already changes survival from `3/8` to `1/2` under a nonnegative
convention, changes the strict positive-count histogram, and creates a tied
maximum.  The paper therefore states one convention and one parameter class,
rather than silently treating lattice and continuous walks as identical.

Exact computation closes 41 survival rows, 561 arcsine cells, 695,482 complete
sign/permutation histories, eight atomic controls, and twelve scaling receipts.
The independent checker, symbolic check, byte replay, and repaired-hash
mutation suite test the certificate.  The proof remains analytic and
all-parameter.
