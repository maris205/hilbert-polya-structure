# FIGURE SPECIFICATION — SD-C20

## Figure 1: transition holonomy and the selectivity obstruction

**Purpose.** Show, in one visual, why the transition cocycle is a genuine
advance over a one-letter parity clock and why it still fails Route A.

**Format.** Native TikZ vector graphic, designed for one-page A4 use and
legible in grayscale.

**Layout.**

1. Top node: the unchanged tensor-subset full shift in its two-block edge
   presentation.
2. Second node: the intrinsic \(S_3\) rule, with refinement \(r=(12)\),
   coarsening \(t=(23)\), and identity otherwise.
3. Three middle branches:
   - one-dimensional blocks, both equal to \((1-x)(1-y)\);
   - primitive commutator cycle with \(H=(rt)^2\ne e\) and character gap 3;
   - the exact standard determinant and first mixed trace-log leak.
4. Merge node: the mixed subset inventory remains visible.
5. Bottom decision node: `STOP_ARITHMETIC_SELECTIVITY` and
   `ROUTE_A_REJECTED`.

**Color semantics.** Blue means exact symbolic construction; green means a
passed local certificate; amber means an analytic or evidentiary boundary;
red means a strict route stop.  Text labels duplicate the color meaning so
the figure remains accessible without color.

**Caption discipline.** The caption must say that the clean one-dimensional
blocks do not imply a clean nonabelian factor and that the figure concerns a
finite two-atom certificate, not an RH zero statement.
