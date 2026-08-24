# Source audit — C122

- Source object: the displayed rational-coefficient polynomial map; no fitted
  table or imported orbit list.
- Clock: one application of `G`; the two-cycle uses chronological Jacobian
  order `J(-1)J(1)`.
- Number system: exact `Q(sqrt(5))`; no tolerance, seed, or floating point.
- Controls: gain `0` and neighboring gain `5/2` are evaluated without
  changing the named target states.
- Independent validation: the checker and SymPy reconstruction do not import
  the producer; replay compares canonical bytes; hostile mutations change
  conclusions and boundary fields.
- Literature novelty and priority are unverified.  No external citation or
  reviewer score is asserted.
- A monodromy determinant is not called a transfer/Fredholm determinant.  No
  prime-like target correspondence, target-divisor match, analytic bridge,
  arithmetic/local datum, Euler factor, root number, automorphy statement,
  Hilbert–Pólya operator, or Route-B authorization is imported or claimed.
