# Narrative report

The finite structure is rigid once the cyclic labels are exposed.  Their
induced map is a permutation, whose number of cycles is the component count.
Every other vertex lies in a rooted in-tree directed toward those labels.  A
single complete-graph Laplacian minor counts that forest, so choosing labels,
choosing a permutation, and choosing the forest gives the full joint count.
Summing unsigned Stirling numbers immediately yields the cyclic-vertex law.

A marked orbit offers a second, apparently unrelated view.  Before its first
repeat, the orbit is an ordered list of distinct labels; its closing edge is
then forced.  Thus every admissible pair `(mu,lambda)` with fixed sum has the
same mass.  Summing those cells gives exactly the cyclic-vertex distribution,
so global cyclic mass and one-orbit collision length agree in law for every
finite `n`.

The no-collision survival probability is a birthday-product.  Under square-root
scaling its logarithm tends to `-x^2/2`, producing the Rayleigh law.  Conditional
on a collision length, the tail position is discrete uniform; combining this
with the Rayleigh radial limit gives joint density
`exp(-(x+y)^2/2)` on the nonnegative quadrant.

Executable evidence exhausts 873,612 maps, 196 finite enumeration cells, and
1,616 formula-atlas cells, with independent reconstruction, symbolic checks,
byte replay, and repaired-hash mutation.  These receipts close implementation
risk while the proof supplies the all-size theorem.  The synthesis is
workspace-new but its ingredients and laws are classical; no priority claim is
made.
