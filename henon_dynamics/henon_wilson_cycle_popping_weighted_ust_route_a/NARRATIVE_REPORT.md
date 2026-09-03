# Narrative report

The substantive step in C338 is not another small graph formula.  It is the
closure of an entire logical chain under one set of conventions.

First, the cycle-popping dynamics is deterministic once the infinite stacks
are fixed.  Visible cycles either coincide or are disjoint, which yields a local
diamond.  A strip argument moves any proposed first pop to the front of one
known terminating list; induction then proves strong termination, identical
pop counts, and one terminal tree for every legal rule.  Wilson's exploration
supplies that terminating list almost surely because each conductance random
walk hits the current finite tree almost surely.

Second, the output law is derived rather than asserted.  A labelled
loop-erased path has a product of retained transition probabilities and
diagonal killed Green functions.  Cramer's rule turns each Green factor into a
ratio of successive determinants; every ratio telescopes across the full
Wilson construction.  The remaining denominator is a reduced Laplacian
determinant.  Since the algorithm outputs exactly one tree, normalization gives
the weighted matrix-tree identity.

Third, scaling each conductance by \(1+t_e\) turns the normalized tree
partition into a joint inclusion generating polynomial.  The matrix
determinant lemma turns the same expression into
\(\det(I+\operatorname{diag}(t)H)\).  Coefficient comparison proves every
(k)-edge transfer-current determinant simultaneously.  This also makes
orientation, root, and parallel-edge behavior transparent.

The evidence exhausts all connected labelled simple graphs through five
vertices and every edge subset, then adds weighted labelled multigraphs and an
all-schedule finite-stack audit.  No finite run is presented as the proof.
Route A is rejected because the source dynamics has no intrinsic arithmetic
prime structure; its projection kernel earns only a formal source-side A4 hint.
