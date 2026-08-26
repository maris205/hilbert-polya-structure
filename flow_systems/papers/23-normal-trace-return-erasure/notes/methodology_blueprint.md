# Paper 23 methodology blueprint

Date: **2026-08-24**
Design: **von Neumann-algebraic classification with exact Fourier controls**

## Frozen inputs

- one standard circle `R/(LZ)`, `L>0`;
- Paper 8's fixed regular representation and
  `M_L^reg = L^infinity(T,m) bar-tensor B(L^2[0,L))`;
- the exact time-kernel domain on which the return expansion is valid;
- no actual packet owner or transfer map.

## Method

1. Use central decomposition to parameterize normal semifinite tracial
   weights by measurable center data, with precise faithfulness and
   semifiniteness hypotheses.
2. Evaluate such weights on the frozen regular time kernels, justifying every
   Tonelli/Fubini and trace-ideal step.
3. Freeze the dual-rotation/flow action on the center and classify invariant
   densities.
4. Compare invariance, constant density, and vanishing of all nonzero Fourier
   return coefficients in both directions.
5. Construct explicit nonconstant-density normal weights that retain selected
   returns when allowed by the domain.
6. Separate these weights from point-character `C*` traces and singular state
   extensions.

## Controls

- constant density reproduces Paper 8's Haar-averaged FNS trace `L f(0)`;
- a positive nonconstant trigonometric density tests return retention;
- a density with zero mean/nonzero Fourier mode tests sign and normalization;
- a point mass is rejected as nonnormal relative to Haar;
- scaling `L` changes the locked normalization coherently;
- a deliberately nonintegrable density tests the semifinite/domain boundary.

## Failure modes

- all normal traces are incorrectly called scalar multiples despite a
  nontrivial center;
- normal, faithful, finite, semifinite, and lower-semicontinuous are conflated;
- a Fourier formula is used beyond the trace ideal;
- invariance is not defined on the actual center action;
- proxy mathematics is attributed to the non-Hausdorff source packet;
- the result is entirely standard and lacks a standalone delta.

## Validation

- independent central-weight classification;
- exact Fourier calculations on finite trigonometric controls;
- domain audit for positive and complex elements;
- primary-source comparison for normal weights on type-I direct integrals;
- owner-firewall and Route review after the theorem shape is known.

## Expected output and effort

Phase-2 source and novelty auditing is complete.  The classification is
classical, while full translation invariance implies return erasure on the
frozen Paper-8 domain; the converse remains unproved without extra domain
hypotheses.  Queue only a technical note or Paper-8 amendment if separately
authorized; do not open a standalone Paper-23 manuscript.
