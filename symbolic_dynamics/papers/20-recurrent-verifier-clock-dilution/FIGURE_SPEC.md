# FIGURE SPECIFICATION — SD-C22

## Figure 1: Recurrent verification, clock dilution, and return collapse

**Format:** one pure-TikZ vector figure, three horizontal panels, no raster
assets.

### Panel A — Recurrent verifier

Show $I_p\to T_{p,2}\to Q_{p,2,2}\to\cdots\to T_{p,m+1}\to I_p$ as a
long directed cycle.  Add a side branch from a quotient equality to the
one-way cemetery ray for composite inputs.  Label

\[
\ell(p)=2+\sum_{d=2}^{\lfloor\sqrt p\rfloor}\lceil p/d\rceil
\sim\tfrac12p\log p.
\]

### Panel B — Clock dilution

Represent the exact total $\sum\tau_e=\log p$ spread over $\ell(p)$ edges.
Highlight one edge with

\[
\tau_e\le\log p/\ell(p),\qquad
|w_e|\ge p^{-\sigma/\ell(p)}\to1.
\]

Conclude `whole vertex adjacency: noncompact, essential norm 1`.

### Panel C — First-return collapse

Contract the full cycle to a single loop at $I_p$ with weight $p^{-s}$.
Display the marker firewall

\[
1-z^{\ell(p)}p^{-s}\quad\text{versus}\quad1-zp^{-s},
\]

and state `equal at $z=1$ only (without transporting the graph-step marker)`.

### Style

- muted navy for state/edge structure;
- amber for the diluted near-unit edge;
- red for the noncompactness stop;
- teal for the induced diagonal loop;
- line weights and text remain legible at one-column width;
- figure must compile under `pdflatex` with standard TikZ libraries only.
