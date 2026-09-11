# P200 Review A: independent deductive audit

Target: immutable Round0, all r,s>=2. No mathematical finding remains.
The verifier is a supplemental finite test, not the proof below. Root did
not author LFAS's candidate proof or manuscript; it had read the candidate
proof and replayed its earlier gate, so this is not blind review.

## Pivot geometry and cycles

An alternating rectangle exists for two rows exactly when their supports
are incomparable. In each incomparable pair its first columns are the two
exclusive minima. If a set C is comparable with both incomparable P,Q,
the only consistent containment choices put C below P intersection Q or
above P union Q: either mixed chain would compare P and Q. Since a switch
preserves that intersection and union, all earlier rows remain comparable
to both changed rows. The first active row i therefore persists, while
the least partner k cannot increase. No nonfixed input reaches a fixed
output, because its just-flipped rectangle is still alternating.

This surviving involution also implies q(F(A))<=q(A). Strict decrease
excludes a return forever. Equality means the next identical involution
undoes the first, so recurrence is exactly unchanged selector and every
nonfixed period is2. This generic least-involution argument gets zero
standalone contribution credit.

For the more specific iff, list all differing columns and mark their row
types. The first switch exchanges the initial type with its first opposite.
If that opposite is second, the same two columns remain first. Otherwise
the unchanged second type becomes the earlier opposite after one switch.
Thus column equality is exactly the opposite-first-two test. Earlier first
pivots were excluded above; earlier partner rows are excluded exactly by
containment of the reconstructed pivot with all intervening rows. This
proves both directions of the printed recurrence criterion.

## The two-visits bound and sharp witness

While a partner persists, its differing-column positions do not change.
Either the current first opposite already occupies the second position,
or a single switch makes that true. In the former case the starting state
is recurrent unless the next step produces an earlier partner. In the
latter case, if the partner survives both switches, the state just before
the second switch is already recurrent. A partner therefore occupies at
most two selector states up to AND INCLUDING the first recurrent state.
Departed partners cannot return. Counting those tau+1states gives
tau<=2p−1<=2(r−i−1)−1<=2r−3. Fixed states are separate; at2x2 the sharp
wide assertion does not apply, so its actual maximum0 is no contradiction.

The witness has initial pivot{r} and row k={0,k} union{k+2,...,r}.
At the start of partner k, the pivot is{k+1}. All earlier positive rows
contain it, while k is first missing it. The two switches send the pivot
through{0} to{k}; the changed row k passes through{k,...,r} to
{0,k+1,...,r}. For k>1 the next earlier missing partner is k−1.
At k=1 the second selector state is recurrent; every earlier selector
strictly decreases next. This verifies the FULL itinerary and first entry,
with tau2r−3. Extra zero columns do not affect any test. No transpose
argument is used;3x4 and4x3 have different image sizes3292/3290.

## Target inverse, completeness and equality cases

Any source and image share their first pivot. Reverse a target rectangle
whose exclusive columns are a in D and b in E. To select those same
columns in the source requires b<min(D without a) and a<min(E without b),
where an empty minimum is the legal sentinel s. If a<b this forces a to
be the first target difference and b to lie in the initial opposite run
before the next same-type difference; swapping the names handles b<a.
This is precisely the target prefix condition, not a full-source selector
test hidden in the inverse algorithm.

All target rows before i lie below the common intersection or above the
common union, so reversing the switch cannot create a smaller pivot.
Partners before k are excluded exactly by comparison with the changed
pivot. Thus the target prefix plus intervening containment is sufficient
as well as necessary. Distinct k or second columns change distinct cell
sets, so sources do not collide. Fixed targets have only themselves.

At most r−i−1partners contribute, each with at most s−1columns. Equality
above1 forces i0 and every partner to contribute all s−1choices. Since
those choices belong to the opposite exclusive set, that set has size
s−1; the initial-type set has size1 and no common/equal columns remain.
The first difference is therefore0 and the pivot is either{0} or its
complement. Its fixed choice forces every other row to be the opposite
support. Conversely every inverse pivot singleton (or co-singleton) in
these two targets is comparable with every intervening row. They attain
the product. At2x2 the fourteen fixed states and the lone alternating
pair give a bijection; every one of the sixteen targets maximizes.

## Independent computational pressure

The new code uses row-mask tuples, exclusive-minimum transitions and
direct forward-path functional graph decomposition. The author uses
column-major scalar encodings, entrywise rectangle scans and Kahn peeling.
An additional entrywise literal scan cross-checks the row-mask selector
on every tested box up to12cells. Every target, including impossible
targets, is compared with its entire graph-derived source SET, not merely
the claimed number. All19boxes with2<=r,s<=8 and rs<=16 are exhausted:
314512sources and targets. The code also tests116complete wide witness
orbits, r2..30 at widths r+1,r+4, with both complement orientations.
Each of two fresh final runs has3823696assertions and identical stdout.
The first development run also passed and is not counted as a review round.
