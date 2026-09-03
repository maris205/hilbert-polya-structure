# P167 narrative report

## Outcome

Minimum inverse positions produce a finite feedback system with two
independent exact axes.  Temporally, the first image reduces to labelled
cycles and loop-rooted paths whose endpoint comparisons control reversal
and irreversible splitting.  Inversely, every target is resolved by forced
first positions, optional fixed symbols, and a product over positions whose
symbols have already opened.  The intersection of those two axes is the
paper's theorem ceiling.

The candidate passed an independent hostile gate as
`GREEN_OWNER_THIN / HOLD_EXTERNAL`.  The formulas survived unchanged, but
the ownership margin remains thin because the first update is a least
kernel-transversal inner inverse and the maximal identity fibre is the
classical block-minimum encoding of set partitions.

## Literal object

On `X_n=[n]^[n]`, a state `f` is replaced by the vector of first positions of
its present symbols.  A missing symbol `i` is assigned the coordinate value
`i`.  This identity default is essential: it closes an absent path leaf as a
loop and thereby decides whether the next step reverses the path or splits
off an endpoint.  Results for arbitrary section extensions do not determine
this feedback dynamics.

The map satisfies the one-sided identity `f M(f) f=f`.  The related map
`M(f) f` retracts each kernel block to its least position and is idempotent.
Those facts explain the transformation-semigroup neighbourhood but are not
the main dynamics; `M` is not generally a mutual inverse selection.

## Temporal story

Distinct symbols have distinct first positions, so the nonloop indegrees of
a first image are at most one.  Every component is consequently a bare
directed cycle or a loop-rooted path.  Cycles invert.  A path in root-to-leaf
order reverses when its root exceeds its child; otherwise the root becomes a
singleton and the remaining path reverses.  Components do not merge, so a
split is permanent.

Two endpoint descents characterize recurrent paths.  Deleting the endpoint
created by a two-step reverse/split event yields an induction with path tail
at most `2s-2`, uniquely attained by the decreasing order.  A first-position
vector always contains value zero, whereas the full decreasing path does
not.  This removes the sole `2n-2` path from the first image and leaves the
sharp image clock `2n-3`.  The source `(1,2,...,n-1,1)` realizes the global
clock `2n-2` by mapping to the increasing full path.

Recurrent connected components can then be counted locally.  Cycles give
`(s-1)!`; recurrent paths give two at size three and `s!/4` from size four
onward.  Labelled set assembly gives the EGF.  Fixed components are only
singletons and two-cycles, so fixed states are involutions; every recurrent
state has period one or two, which determines all positive-iterate counts
and the zeta function.

## Inverse story

For a target `g`, every off-diagonal coordinate forces that symbol to be
present at its prescribed first position.  Repeated forced positions make
the fibre empty.  A fixed coordinate can describe either an absent symbol
or a symbol first appearing at itself, except when that position has already
been occupied by another forced first occurrence.  After selecting the
optional fixed symbols, every other position may carry precisely a symbol
whose first occurrence has already opened.  Multiplication over those
positions and summation over optional subsets gives an exact formula for
every target, including a membership test for the first image.

For a fixed target and a fixed kernel partition, each block label is forced
by the target and the block minimum.  Thus a fibre has at most one source per
set partition.  The identity attains this Bell bound because labelling every
block by its minimum produces exactly that target.  The argument makes no
claim that the identity is the unique maximizer.

## Evidence and risk boundary

The paper-local verifier uses only the Python standard library.  It checks
all states and targets through `n=7`, all path orders and canonical cycles
through size nine, EGF coefficients through order fourteen, and the complete
small graphs at `n=1,2,3`.  Two fresh executions are byte-identical and each
records `12,603,676` assertions.  Enumeration is a hostile control rather
than a premise of the proofs.

The direct-owner search was bounded.  It located primary owners for least
kernel transversals, inverse matching, first-occurrence encodings, generic
functional graphs, and periodic-point zeta functions, but no inspected
source iterated the same identity-on-missing map.  This non-hit is
novelty-neutral.  External posting, submission, priority, and release remain
on hold pending specialist owner review.

