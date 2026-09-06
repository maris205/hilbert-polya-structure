# LNR — complete temporal proof, candidate not admitted

2026-09-06 UTC. Proof author: root. The inverse contributor works separately
in LNR_INVERSE_WORK/. No paper number, candidate PASS or new gate is implied.

## Claim, assumptions and status

**PROVABLE AS STATED.** For $n\ge3$, the carrier is $\{0,1,2\}^n$
with cyclic labelled positions. Define
$$F(x)_i=\mathbf1_{\{x_{i-1}<x_i\}}+\mathbf1_{\{x_{i+1}<x_i\}},$$
using synchronous old-state comparisons and subscripts modulo $n$.
We prove $F^4=F^3$; all recurrent states are fixed; and the sharp global
entrance is one at $n=3$ and three at every $n\ge4$. The following is
deductive, not inferred from the finite pilot. The standalone temporal
verifier is `verify_lnr_temporal.py`; actual execution is recorded separately.

## Strategy and dependency map

1. Local strict-comparison contradiction excludes adjacent twos in every
   image. A cycle orientation argument excludes the all-one image.
2. Image zeros/twos persist. All remaining coordinates split into one-runs
   with fixed bounds. The complete run cases stabilize in two further steps.
3. Fixed triples give the exact positive-block language. The three-vertex
   case is separate; explicit all-length witnesses attain the larger bound.

No external theorem is invoked for these deductions. The ternary alphabet,
strict comparison and two distinct cycle neighbors are used; $n<3$ and
larger alphabets are not silently included. The inverse theorem is not a
premise of any temporal conclusion.

## Fixed states

A zero is always unchanged. A one is fixed iff exactly one of its neighbors
is zero. A two is fixed iff neither neighbor is two. Thus a fixed nonzero
run between zero runs must be one of

    2, 11, 12, 21, 121.

Conversely each cyclic concatenation of these positive runs separated by
one or more zeros is fixed, as is the all-zero word. There is no fixed word
without a zero: a one could not be fixed, and the constant two word is not
fixed. The triple tests also give a precise cyclic-language description
without choosing an artificial first zero.

## Stabilization by three

Let y=F(x). No two adjacent coordinates of y equal two: that would require
each of the two adjacent original letters to be strictly larger than the
other. This contradiction applies to every image, at every time.

Every zero persists. In a word without adjacent twos, a two has two
strictly smaller neighbors and therefore persists as well. Hence in y
all zeros and twos are permanently fixed; only runs of ones can change.

First exclude the all-one image. If every output equals one, every vertex
has exactly one incident strict-down edge. Summing counts gives n strict
edges, so no edge is a tie; an orientation of a cycle with outdegree one
at every vertex is directed cyclically. Strictly decreasing values around
a full cycle are impossible. Therefore y has at least one zero or two,
and all its one runs have bounding symbols in {0,2}. A run may wrap around
the labelled origin; its bounding symbols are still the same actual sites.

Consider one such run of length m. If m=1, neighbors 00 turn its one into
two, neighbors 22 turn it into zero, and mixed 02/20 keep it one. All three
results are permanently fixed against their fixed bounding symbols.

If m>=2, each internal one becomes zero. A boundary one stays one exactly
when its outside bound is zero; with outside two it becomes zero. For
m=2, both outside bounds zero yield the stable run 11. If precisely one
outside bound is zero, the survivor has two zero neighbors and becomes two
at the next update. If neither is zero, no one survives. For m>=3 every
surviving endpoint likewise has outside zero and an inside zero, so becomes
two at the next update; all other positions are already zero.

These cases cover all one runs and their possibly shared fixed bounds.
Thus two further updates from y produce a fixed state. This proves
F^4=F^3 on every carrier. Every recurrent state lies in the image of F^3,
so every recurrent state is fixed, with the exact language above.

## Sharpness and small length

For n=3 the graph is the complete graph on three vertices. Three distinct
source values yield a permutation of 012, a fixed word. Two equal smaller
values and a larger value yield a permutation of 002, also fixed; two
equal larger values and one smaller yield a permutation of 011, fixed.
All equal values yield 000. Thus every first image is fixed, and 111 is
not initially fixed, giving sharp entrance one.

For every n>=4 use x=0^(n-3)122. Its first image is 0^(n-3)111.
The next image replaces the middle one by zero, giving 0^(n-3)101.
Both remaining ones then become two, giving 0^(n-3)202, which is fixed.
The first and second images are not fixed, so this source has entrance
three. Combined with the upper bound this proves the claimed sharp law.

## Value and ownership limits

The proof uses permanent local symbols and a finite run classification;
those are not claimed as new general techniques. A generic de Bruijn
matrix for all target fibres alone would not supply a distinct contribution.
The inverse/maximum/equality contract is still being investigated, including
complete classical crown-poset/independent-set adapters. No source nonhit
is treated as proof of originality. P112's tournament update retains tie
edges and lives on complete orientations, unlike this strict-comparison
ternary word update; its exact formulas must be compared, not its title.
HOLD_EXTERNAL remains.
