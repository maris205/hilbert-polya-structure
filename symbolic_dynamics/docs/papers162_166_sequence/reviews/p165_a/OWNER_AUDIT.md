# P165 independent owner and internal-collision audit

**Audit date:** 2026-09-03  
**Scope:** Round0, bounded primary-source search, P1--P164 internal corpus  
**Decision:** `OWNER_THIN PASS / HOLD_EXTERNAL`

## Direct one-step owner subtraction

The strongest direct background source is Jibril, Tomlinson, Tjhai, Ahmed,
and Bezzateev, *Some new codes from binary Goppa codes and a method of
shortening linear codes*, IET Communications 7 (2013), 270--277,
[publisher full text](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/iet-com.2011.0693).
The publisher text explicitly develops shortening on hitting sets of
low-weight codewords and a generalized distance-increasing version.  Taking
the protected weight range through `2d-1` supplies the one-step mechanism
needed here: hit/remove all sub-double-weight words and the survivor has
distance at least `2d`.

Grassl and White's *New Good Linear Codes by Special Puncturings* is the
nearby low-weight-support puncturing source.  Its title, authors, venue,
year, and page are confirmed by the
[KIT institutional record](https://publikationen.bibliothek.kit.edu/1000001944)
and DOI `10.1109/ISIT.2004.1365491`.  It owns neighboring use of support
information for code modification, not the residual dynamics claimed here.

Accordingly, P165 correctly assigns **zero contribution credit** to:

- ordinary shortening and puncturing;
- choosing hitting coordinates for low-weight words;
- the entire one-step argument that all words below `2d` are removed and
  the surviving distance is at least `2d`;
- Hamming support, direct sums, repetition/full-support lines, finite-map
  termination, and the geometric-series identity.

This is a conservative subtraction: the literal P165 operation shortens on
the whole union of the relevant supports and keeps padded coordinates,
whereas hitting-set work may choose a smaller coordinate set.  Giving the
larger one-step principle zero credit prevents the manuscript from gaining
value from that distinction.

## Bounded direct-owner search

Primary/publisher searches included the exact and near-exact combinations:

```text
"iterated shortening" linear code minimum distance low weight support
"autonomous" shortening linear code low-weight codewords
"union of supports" low-weight codewords shortening linear code
"less than twice" minimum distance shortening linear code support
target preimages shortening linear codes minimum distance
```

The searches recovered conventional iterated shortening/projection,
minimum-distance/list-decoding work, and the one-step Jibril/Grassl--White
lane.  No inspected primary record stated the literal state-dependent
iteration together with its sharp dyadic clock, every-time nonzero-target
image equivalence, or simultaneous extremal inverse classification/count.
This is a bounded non-hit only; it is not evidence of novelty, priority, or
publication readiness.

Vardy's complexity citation resolves at IEEE DOI `10.1109/18.641542` and
supports only the explicit non-claim that general minimum-distance
computation is efficient.  All three bibliography entries agree with the
publisher/institutional metadata inspected.

## P1--P164 collision subtraction

The complete directory-name occupancy through P164 was reviewed, followed
by theorem-level inspection of the nearest carriers and proof engines.

| internal work | nearest overlap | decisive separation |
|---|---|---|
| P98, equal-block-sum torsion shifts | finite linear/coding objects and iterated kernels | fixed cyclic linear constraints; no state-dependent minimum-distance support kernel or dyadic code-extension atlas |
| P100/P115, digit erasure and bounded Cartier dynamics | coordinate/coefficient loss and finite-field linear algebra | fixed arithmetic/linear operator; P165 recomputes a nonlinear coordinate kernel from the full current code |
| P103/P109, matrix/subspace image dynamics | descending finite subspaces, exact images, clocks | iteration of a fixed matrix/operator and Gaussian incidence fibres; P165 uses multiplicative distance growth and target zero-coordinate capacity |
| P126, balanced refinement | geometric resource levels | composition refinement, not code shortening; no theorem or construction transfers |
| P137, rank-feedback p-group splitting | state-dependent statistic, resource budget, inverse language | unordered p-group types with additive/triangular resources and recurrent two-cycles; P165 has labelled coordinate supports, multiplicative doubling, a logarithmic nilpotent clock, and dyadic line extensions |
| P143, Boolean row-inclusion residual | support-driven finite algebra | Boolean row deletion/residual engine, not a subspace restriction kernel or Hamming-distance threshold |
| P158/P159/P160, intersection/pruning/cropping | rank-changing deletion and sharp clocks | set/graph/partition carriers and different inverse grammars; P165 preserves ambient labels and takes a code subspace kernel |
| P162, random translation intersection | subspaces appear in the history span | stochastic set intersection and stabilizer-weighted source polynomials, not deterministic code shortening |
| P163, complemented shadows | set-family ranks and period products | recurrent rank-support complement dynamics, not a descending subspace system |
| P164, cyclic equality feedback | q-ary words, affine-code target fibres | fixed cellular difference operator behind a nonlinear word front; P165 evolves whole linear codes via their current distance spectrum and does not reuse the affine-kernel fibre formulas |

No P1--P164 literal duplicate or occupied internal proof transfer was found.
The closest carrier collision is P109, but its fixed nilpotent operator does
not yield the state-dependent purge sets, distance-doubling support budget,
or dyadic equality-source classification.  The closest same-batch coding
paper is P164, whose word-state affine fibres are structurally different.

## Residual contribution after subtraction

Only the following conjunction remains eligible for internal credit:

1. autonomous recomputation of the full low-weight support union;
2. the sharp all-parameter absorption height with dyadic witnesses;
3. the every-time image criterion for every nonzero target;
4. the two universal inverse lower bounds; and
5. the iff classification and prime-power count of sources attaining both
   lower bounds simultaneously.

The manuscript expressly does not claim a complete fibre count, algorithmic
efficiency, priority, or absolute novelty.

## Gate decision

**OWNER_THIN PASS.**  The direct one-step owner is accurately exposed and
fully subtracted.  No direct owner of the residual conjunction or internal
P1--P164 duplicate was found in the bounded audit.  Maintain
`HOLD_EXTERNAL`; any later direct hit on the literal map or targetwise
inverse atlas reopens this gate.
