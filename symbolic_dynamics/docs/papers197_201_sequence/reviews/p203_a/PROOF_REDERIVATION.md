# P203 A: full-parameter proof audit

2026-09-05 UTC. Root independently checked the entire frozen Round0 main,
not only its abstract or finite table. The A-M1 proposed repair inserts
only a release-scope paragraph; the following proof audit applies unchanged
to the original and proposed revised mathematical text. No bearing lemma
was supplied by this reviewer. The optional Stage1 root-zero observation
is not used to repair the author's original argument.

## Literal and entrance convention

The carrier is every0/1 edge assignment to all pairs of ordered labels,
including the empty cases n=0,1. A monochromatic triple has all three bits
equal; it is not a cyclic tournament predicate or a signed product test.
The least sorted triple is flipped simultaneously, or the state holds.
The chosen triple survives its own flip. Any later selector is therefore
no larger; equality reverses the preceding move. A newly earlier triple
must share a changed edge, and two distinct triples share at most one
edge. Its unflipped edges have the opposite colour, so strict selectors
alternate colour and replace one vertex by a smaller label. Finite descent
ends in a two-cycle. No moving state reaches a holding state because its
last flipped triple survives. Thus entrance time is exactly the number of
strict transitions, not that number plus one. This generic argument is
fully deducted from the contribution evaluation.

## Two-step geometry and no return

For successive strict selectors abc,abd,abe, replacement gives e<d<c.
The last two new edges were untouched, while ab was flipped twice.
Consequently abe already had the first triple's colour initially and was
earlier than abc. This proves that consecutive strict transitions cannot
reuse the same shared edge; distinct labels and untouched-edge assumptions
are justified by strict replacement rather than implicitly assumed.

For a later drop of the minimum, put T0=abc,T1=dab,d<c. After exchanging
a,b if needed the second shared edge must be da, so T2=eda with e<minT1.
Then e is below allT0. Its untouched ea edge has T0's colour q. Old least
priority excludes eab and eac, forcing eb=ec=1-q. The first flip makes
ebc colour1-q, earlier than T1. Applying this obstruction at every strict
pair stabilizes the minimum after at most the first change.

In an anchored segment, the non-repeated shared edge forces a sliding
pair Tt={a,vt,v(t+1)} with v(t+2)<vt. Both parity subsequences decrease.
A first repeated vertex has opposite-parity indices. An interior vertex's
anchor edge receives exactly its entry and departure flips, restoring its
entry colour during its absence. A return at opposite parity requires the
opposite colour. The initial nonanchor vertex has only its departure flip;
an odd return index instead requires its initial colour. Both are impossible.
Zero or one strict change respects the same endpoint conventions.

The proof must separately exclude the one vertex retired before anchor
stabilization. Write T0={r,u,v} colourq,T1={a,u,v},a<minT0, and gamma=1-q.
In G1, au,av,uv,ru,rv all have colourgamma, while ar is unchanged. Initially
every triple containing a precedes T0, so each a-spoke colour class k has
only rim edges1-k. If ar=gamma, the candidates aru and arv force r>u,v;
neither decreasing parity subsequence can reintroduce r. If ar=q, first
re-entry at relative anchored time k requires oddk. Its partner w is an
odd-position vertex, w<=v. For w=u orv, rw=gamma already blocks the return.
Otherwise w<v first entered at even time k-1, so its initially untouched
anchor spoke had colourgamma. The initial class rule gives wu=wv=q.
If rw=q then ruw was an earlier original monochromatic triple, replacing
v by w<v; hence rw=gamma. It remains untouched while r is absent and
again blocks re-entry. This is a global no-return proof, not an unjustified
extension of the anchored-only statement.

Every strict transition therefore spends a genuinely new vertex after
the initial three. The upper bound n-3 follows on the full carrier.

## All-size sharpness

The witness labels the nonanchor vertices n-1,n-2,...,1. Initial spokes
are0,0,1,0,1,..., with consecutive rim colour i mod2 and the displayed
nonconsecutive equal/different-spoke rules. Initially only the first pair
is eligible with anchor0. At step t, the carry spoke has flipped once;
retired interior spokes twice; the exceptional first spoke once; all future
spokes are unchanged. Future/future and retired/future pairs are blocked
by their rim colours, including the exceptional first spoke. Retired pairs
are later in label order. Among future spokes matching the carry, only
the immediately next one has the needed rim colour; later matching ones
have the opposite rim colour. Hence the exact selectors slide through
the descending sequence until012. That least possible triple immediately
repeats. There are n-3 strict transitions for every n>=3. At n=3 this is
already a two-cycle; n<3 has no triple and is the identity. No extrapolation
from a finite maximum is needed.

## Complete inverse and its algebraic independent control

Every moving predecessor ofY must undo a monochromatic target tripleQ.
Different Q reverse different edge sets, producing distinct sources. An
earlier target-monochromatic triple must share an edge withQ to be destroyed
(D). An earlier mixed triple becomes monochromatic only when its two
unchanged colours both equal the opposite ofQ's colour (C). Triples sharing
no edge are unchanged. These alternatives are exhaustive, proving both
directions and allowing empty fibres. A holding target has only itself.
For the least target tripleD is vacuous andC is exactly the recurrent test.

The separate control represents edge colours by signs s_e in{-1,1}.
For a triple with signs a,b,c its monochromatic indicator is
(1+ab+ac+bc)/4. Reversal multiplies exactlyQ's signs by-1. The sum of
these nonnegative indicators over triples earlier thanQ is zero exactly
when every earlier triple is mixed. This gives an independent correlation
implementation of inverse feasibility, without calling a source selector
or importing an author program. Every entire reconstructed source set is
compared to incoming arrows in the full finite graph. Generic undo/priority
filtering and the quadratic identity themselves receive zero novelty credit.

## Classical cap, literal realization and every equality case

Two admissible triplesP<Q share an edge byD. The rank-three Johnson clique
classification therefore applies: relative toabc,abd, another triple either
containsab or isacd/bcd. In the latter case all further triples remain in
that four-set; otherwise all shareab. Capacitiesn-2 and4, including their
crossover, are classical and are explicitly credited. Empty or singleton
families and n<=3 are separately harmless.

Attainment is not inferred from the static cap. In the star construction
all edges incident to0 or1 have colourc and all outer edges1-c. Every01v
destroys earlier star triples, creates none earlier, and leaves outer
triples later. For the four-face construction, every edge has colourc
except0v,v>=4. Other faces are destroyed. A triple with0 and one outside
vertex has opposite colours on its two edges to that vertex; with two
outside vertices it is also mixed. A non-S triple without0 is later than123
and every face containing0. Thus all four faces really are admissible.

For a general star, S1 makes all its triples monochromatic. UnderS1 no
new monochromatic competitor is created by reversal because an unchanged
incident edge has colourc. Existing competitorsaxy,bxy with rim colourc
survive exactly when their outside pair avoids the reversed third vertex.
Sinceaxy<bxy, the needed exclusions are preciselyS2. Outer triples are
unchanged and must follow the last star triple, preciselyS3. Thus the
conditions are an iff for the whole star, not just sufficient witnesses.

For a four-set, K1 makes its faces monochromatic and mutually destructive.
Triples meetingS in at most one vertex are unchanged, givingK2. A triple
uxy with two vertices inside is eligible before or after reversingxy
according as its two outside edges both have colourc or both1-c; unequal
outside colours always block it. Requiring absence before each pertinent
face is exactlyK3. This proves the full-top iff. Equality in the static
bound fills one largest containing family: tops atn4,5; either atn6;
stars atn>=7. At n<=3 every target has one source. All-target certificates
are distinct from any unclaimed formula counting the maximizing targets.

## Independent finite scope and residual assessment

The final separate implementation discovers a high even composition power
on the entire finite mapping, checks its idempotence and identifies its
fixed image as the recurrent core, then computes first entry by binary
jumps. The power bound uses carrier size, not the theorem n-3. It verifies
the fixed-F-squared iff independently. This is not author orbit-path tracing,
temporal-coauthor peeling or Stage1 Kosaraju discovery. Signed correlation
inverses and every possible star/top certificate are checked for all33868
states,n0..6; uniform time witnesses extend through80 and inverse witnesses
through24. All finite assertions passed in two actual formal fresh runs.
These support, but do not prove, the all-parameter arguments audited above.

The non-generic retained axes are the alternating-colour global no-return
clock with uniform attainment, and ordered-colour feasibility/equality for
actual targets. Neither follows from the other. This is internal amber
correctness/value acceptance subject to the separate source and provenance
audit, not a claim of universal originality.
