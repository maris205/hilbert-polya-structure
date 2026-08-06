# R101 — Third-Grid Quantum Refinement

## Trigger

The historical R100 summary reported \(h=0.04\) versus \(h=0.03\) median
level changes of 1.14--1.65%.  A later unified-window audit of the unchanged
NPZ spectra gives 1.20--1.67% on modes 25--164.  Both versions fail the
frozen 1% gate, so the trigger and chronology are unchanged.  R101 was
specified only after that failure and therefore cannot be presented as
preregistered R100 evidence.

## Frozen repair

- Recompute all five R100 physical cells at nominal spacing \(h=0.0225\).
- Compare modes 25 through 164 against the existing \(h=0.03\) spectra, the
  same level window used by the 25/15 spacing discard.
- Gate: median relative change below 1%; report p90 and maximum without
  suppressing failures.
- Form a two-grid second-order extrapolation
  \[
    E_j(0)=\frac{h_c^2E_j(h_f)-h_f^2E_j(h_c)}{h_c^2-h_f^2},
    \qquad h_c=0.03,\ h_f=0.0225.
  \]
- Report spacing ratios for the fine and extrapolated spectra.  A difference
  between these remains a discretization warning.

No zero or prime data are loaded.
