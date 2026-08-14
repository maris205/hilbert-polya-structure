# Figure Specification — SD-C23

All figures are pure TikZ vector sources.  They use no external raster image,
no target zeros, and no numerical interpolation.

## Figure 1 — successor–divisor anatomy

**File:** figures/successor_divisor_anatomy.tex
**Placement:** recurrent topology section
**Width:** approximately \(0.96\) text width

### Content

Two aligned panels:

1. an induced prefix on vertices \(2,\ldots,11\);
2. a schematic quotient-spine panel.

Use:

- dark blue arrows for successor edges \(q=1\);
- amber curved arrows for \(q=2\) returns;
- light gray arrows for other divisor returns;
- colored outlines around \(C_2,C_3,C_5\).

The panel must make visible:

\[
 2\to3\to2,
\qquad
 3\to4\to5\to3,
\qquad
 5\to6\to7\to8\to9\to5.
\]

### Caption

The induced prefix illustrates the two mechanisms behind the primitive-cycle
flood.  Successor edges move from \(n\) to \(n+1\), while the quotient-two
edge \(2k-1\to k\) closes \(C_k\).  The right panel emphasizes that the
pruned \(q\in\{1,2\}\) spine already retains every canonical cycle.  Gray
edges belong to the full graph but are unnecessary for this obstruction.

### Accessibility

Line style and arrow curvature must distinguish edge types without color.
Labels \(q=1,q=2,q\ge3\) remain readable in grayscale.

## Figure 2 — finite confinement mechanism

**File:** figures/confinement_geometry.tex
**Placement:** finite-confinement section
**Width:** approximately \(0.88\) text width

### Content

Show:

1. a maximal vertex \(M\);
2. the forced drop \(M\to d\) with
   \(d\le(M+1)/2\);
3. a staircase of \(r-1\) edges, each increasing by at most one, returning to
   \(M\);
4. the inequality chain

   \[
   M\le d+r-1
    \le\frac{M+1}{2}+r-1
   \]

   and conclusion \(M\le2r-1\);
5. the equality path
   \(2r-1\to r\to r+1\to\cdots\to2r-1\).

### Caption

At the maximum of a length-\(r\) closed walk, the next vertex is a proper
divisor of \(M+1\), forcing a drop by at least half.  Each remaining edge can
increase the current vertex by at most one.  Closing the walk therefore gives
\(M\le2r-1\); equality forces the canonical cycle \(C_r\).

## Figure exclusions

No near-threshold convergence plot is included.  At
\(\operatorname{Re}s=0.51\), finite nuclear prefixes grow for a long range
despite theorem-level convergence.  A plot would be less informative than the
exact row-decomposition and Fourier-extraction proof.
