# Narrative report

The product kernel turns an infinite nonlinear kinetic system into an exact
tree calculation.  The rooted-tree identity closes the mass generating
function, while its unrooted companion closes the number density.  Before
gelation this yields every cluster concentration, not merely a few moments.
The second moment blows up at \(t=1\), and the same coefficient law becomes a
critical \(k^{-5/2}\) tail.

The main step beyond that familiar pregel calculation is a postgel firewall.
If the loss rate uses only finite-cluster mass, the explicit
Smoluchowski/Stockmayer continuation freezes the critical shape and scales it
by \(1/t\); its sol mass is \(1/t\) and its second moment remains infinite.
If finite clusters can react with the gel, the Flory loss stays equal to the
initial total mass.  The pregel coefficient formula then continues, but its
mass is the small Lambert-W branch
\(q=-W_0(-te^{-t})/t\), with an exponentially cut-off tail and finite higher
moments.  Both laws meet at the gel point, yet direct substitution proves they
solve different equations thereafter.

The evidence chain records 40 exact Cayley rows, 13 time/branch rows and five
tail controls.  The independent checker makes 696 assertions; SymPy
reconstructs 29 identities; replay is byte exact; all 28 hostile mutations
are rejected.  Finite rows are audit controls, never the proof of gelation.

Route A remains rejected on all five axes.  Cluster sizes and tree functions
do not create arithmetic primitives, a target orbit clock, target determinant,
target analytic structure or a natural unitary operator.
