# Narrative and derivation report — P124

Status: **ROUND2 GO_INTERNAL / EXTERNAL HOLD**.

## Central story

The crossed-colon operator initially looks global on the lattice of monomial
ideals.  Total degree reveals the useful normal form: every diagonal evolves
independently by neighbor OR, with zero, one, or two wall sources.  That
component decomposition alone is established Boolean-network territory.
The residual step is to reimpose the fact that all diagonal words must be
traces of one upper set.

The first occupied diagonal captures this coupling.  If its support meets
both parity classes, its OR evolution fills and the ideal enters a fixed
power.  If its support lies in one parity class, it becomes the corresponding
checker phase and the ideal enters a two-cycle.  If all source-free diagonals
are empty, the sourced region fills and the terminal fixed power is reached.
Thus one diagonal trace determines the complete basin.

## Basin enumeration

A staircase is encoded by an east/south path from `(0,b)` to `(a,0)`.  Having
no occupied monomial below degree `r` is exactly the condition that the path
stay above `i+j=r`, while contacts with the barrier are precisely the
occupied positions on degree `r`.  Four transfer states record no contact,
even contacts only, odd contacts only, or both.  Their terminal counts give
the checker and fixed-power basins.  Reflection supplies the total
first-degree layer and the terminal fixed-basin ballot formula.

This transfer has polynomially many entries and does not iterate across the
exponential ideal state space.  It is the paper's main enumerative output,
not a computational restatement of the dynamics.

## Supporting dynamics

The established path lemma plus upper-set compatibility gives the complete
recurrent set: `m` fixed powers and `m-1` checker two-cycles.  Taking the
maximum of component entrance times yields maximum depth `m` off the square.
On the square the one-source band disappears, leaving `max(1,m-2)`.  These
facts orient the basin theorem but are not the contribution center.

## Evidence and ownership boundary

One paper-local verifier compares literal basis arithmetic, staircase
updates, diagonal networks, recurrent families, and sharp depth.  A second,
independent verifier follows every small-box orbit and compares actual basins
with the first-trace theorem and contact transfer.  Finite computation proves
neither the all-parameter results nor ownership.

All generic OR-network, lattice-path/reflection, staircase, and colon
ingredients receive zero credit.  The residual is their specific conjunction
with the literal map and the upper-set basin partition.  Novelty, priority,
and external release remain **HOLD**.

Internally, P107's annihilator-power dynamics on ideals of `Z/NZ` is separated
by both carrier and mechanism: it uses CRT valuations and clipped reflection,
not crossed colons or sourced diagonals.  P104 is a random contraction
cocycle and shares only the nonstructural words “monomial” and “toggle.”
Neither is a literal collision, while their generic vocabulary receives zero
credit in P124.

## Round-2 closure

Review A's two support-only findings were repaired without changing the
manuscript: the sharp-depth anchor is Theorem 3.2, the layer and terminal
ballot anchor is Theorem 5.1, and the P107/P104 firewall is explicit.
Independent nonauthor Review B then audited the theorem/proof package,
boundaries, both canonical controls, owner ceiling, isolated build, and all
five PDF pages.  It returned `0 CRITICAL / 0 MAJOR / 0 MINOR` and
`GO_INTERNAL`.

Round 2 therefore freezes the support record rather than changing the
mathematics.  The combined control count is `1,735,656`, all four PDF
snapshots are byte-identical, and the package checksum manifest passes.
External novelty, priority, posting, submission, and release remain `HOLD`.
