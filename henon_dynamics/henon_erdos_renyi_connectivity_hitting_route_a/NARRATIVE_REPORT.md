# Narrative report

The finite law is simpler once the connected graph count is treated as the
primary object.  Every disconnected graph has exactly one component
containing vertex 1; choosing its labels, connected internal graph, and an
arbitrary graph on the remaining labels gives a triangular recurrence in
`n`.  Uniform edge-order prefixes then turn these counts into the entire
hitting distribution, not only its mean.

The asymptotic step stays in the same without-replacement model.  Fixed
factorial moments of isolated vertices converge to those of a
`Poisson(exp(-c))` law.  That alone does not prove connectivity: the paper
adds a spanning tree inside every candidate component and forbids all crossing
edges.  Splitting component sizes at `n/log n` makes both union-bound ranges
summable, proving all non-isolated obstructions vanish.

This produces the standard Gumbel CDF for `2 tau/n-log n`.  The result is a
distributional threshold statement.  No finite-n coupling identity with the
last isolated vertex and no unbounded-moment convergence are inferred.
