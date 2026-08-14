# FIGURE SPECIFICATION — SD-C21

## Figure 1: semiring sieve and recurrent-core collapse

**Purpose.** Show both halves of the theorem in one diagram: the full-shift
semiring genuinely executes explicit quotient search on the same graph that
supports the determinant, but periodic traces retain only accepted loops and
the mechanism generalizes to every total decider.

**Format.** Native TikZ vector graphic, no external raster or generated
image.  Designed for full-width A4 placement and grayscale legibility.

**Layout.**

1. Top source node: full-shift semiring operations and entropy.
2. Program layer: (I_n\to T_{n,d}\to Q_{n,d,q}), with separate accept and
   equality branches.
3. Recurrent/transient layer: prime self-loop versus acyclic cemetery ray.
4. Whole-operator node: one (\mathcal S_1) weighted vertex adjacency.
5. Analytic branch: exact traces and Euler determinant.
6. Obstruction branch: transient pruning and universal-decider compiler.
7. Bottom verdict: selector-tautological, pruning-equivalent, Route A
   rejected.

**Color semantics.** Blue is frozen source structure, green is an exact
analytic pass, amber is a modeling/invisibility boundary, and red is a strict
route stop.  Every meaning is written in text so color is not required.

**Caption discipline.** The caption must say that the whole adjacency is
legitimate, that the determinant forgets the computation, and that no
critical-zero or RH claim is represented.
