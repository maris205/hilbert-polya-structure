# Figure Specification — SD-C25

All manuscript figures are pure TikZ vector sources.  They use no raster
assets, numerical fits, target-zero data, or decorative chart elements.
Colors are paired with shapes, line styles, and explicit text so the figures
remain legible in grayscale.

## Figure 1 — ordered-word rigidity hierarchy

**File:** figures/ordered_word_rigidity.tex  
**Placement:** Introduction  
**Width:** approximately \(0.98\) text width  
**Role:** hero figure

### Content

The top row shows

\[
 C_k:k\to k+1\to\cdots\to2k-1\to k
\]

with \(q=1\) along the successor run and \(q=2\) on the return.  A central
box records

\[
        W(C_k)=1^{k-1}2.
\]

Four branches show:

1. fixed finite semigroup/DFA:
   \(a^{k-1}b\), ultimately periodic;
2. fixed complex/rational linear fiber:
   \(u^{\mathsf T}A^{k-1}Bv\) or
   \(\operatorname{tr}(A^{k-1}B)\), LRS and SML support;
3. growing \(N\)-dimensional nilpotent fiber:
   arbitrary \(N\)-term memorization, PROVES_TOO_MUCH;
4. countable decider:
   transient pruning or recurrent clock dilution.

Every branch points to the unchanged base ledger

\[
        z^kM_k^{-2s},
\qquad
        M_k=(2k-1)!/(k-1)!.
\]

### Caption

The unique-minimum marking turns the canonical holonomy-two orbit into the
word \(1^{k-1}2\).  Fixed finite readers are eventually periodic; fixed
linear readers have SML-rigid exact support; growing finite readers memorize
arbitrary prefixes; countable total deciders prune or clock-dilute.
Independently, the base cycle keeps marker \(z^k\) and factorial weight
\(M_k^{-2s}\).

### Accessibility

- quotient-one and quotient-two edges differ in both color and stroke;
- branch outcomes use distinct border shapes;
- stop/control labels are text, not color alone;
- no title is drawn inside the figure.

## Figure 2 — memory/roof decision tree

**File:** figures/memory_roof_decision.tex  
**Placement:** Countable-wrapper section  
**Width:** approximately \(0.97\) text width

### Content

A root asks whether the reader is fixed finite, growing finite, or
countable.

- Fixed finite:
  eventual periodicity or SML; no prime-only support.
- Growing finite:
  exact finite prefix, but target vector is stored.
- Countable transient:
  computation lies in a DAG; traces see accepted loops only.
- Countable recurrent:
  total roof \(\log n\) over
  \(\ell(n)\gg\log n\); maximum edge weight tends to one; noncompact.
- First return:
  recovers a diagonal weight only by
  \(z^{\ell(n)}\mapsto z\).

The bottom row records that the natural \(C_k\) roof is factorial, whereas
forcing \(\log k\) creates clock dilution.

### Caption

Every immediate enlargement of memory has a different failure certificate:
prime nonselection, arbitrary-prefix universality, determinant-invisible
transient computation, noncompact recurrent clocks, or a changed
first-return marker.  The natural endpoint roof remains factorial; forcing
\(\log k\) on a length-\(k\) orbit activates the recurrent obstruction.

### Accessibility

Solid, dashed, and dotted connectors distinguish model changes.  Green is
reserved for an honest analytic property, amber for modeling choices, and
red for route stops; every semantic distinction also appears in text.

## Figure exclusions

- No finite-prefix plot is presented as evidence for infinite prime
  selection.
- No near-boundary numerical sum proves the \(\mathcal S_1\) threshold.
- No Riemann zero or critical-line plot appears.
- No transient computation is drawn as a recurrent mechanism.
- No induced return is drawn as the unchanged vertex adjacency.
- No prime table enters figure generation.
