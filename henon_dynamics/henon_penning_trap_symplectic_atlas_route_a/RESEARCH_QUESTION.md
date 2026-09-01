# Research question

## Primary question

For the ideal axially symmetric Penning Hamiltonian in a fixed symmetric-gauge
canonical convention, can one prove one closed theorem that covers the exact
six-dimensional flow, every stable/critical/unstable parameter chamber, every
degenerate boundary, the signed stable-mode normal form, and all periodic and
stroboscopic fixed-space cases?

## Frozen model

The state order is `(x,y,z,p_x,p_y,p_z)`.  With signed cyclotron frequency
`c` and `zeta >= 0`,

```text
H = ((p_x+c y/2)^2+(p_y-c x/2)^2+p_z^2)/2
    + zeta^2 (z^2-(x^2+y^2)/2)/2.
```

Writing `u=x+i y` and `v=u'` gives

```text
u'' + i c u' - zeta^2 u/2 = 0,
z'' + zeta^2 z = 0.
```

## Answer sought

The desired result must be global in `(c,zeta)` and must not infer a continuum
statement from sampled numerics.  It must prove:

1. an entire-in-`Delta` exact flow and canonical symplecticity;
2. bounded, critical-Jordan, unstable, zero-axial, zero-field, and free cases;
3. the stable frequencies, actions, Krein signs, and signed energy normal form;
4. active-mode commensurability, true minimal periods, and strobe fixed-space
   dimensions; and
5. the exact field-sign conjugacy.

## Route-A hypothesis

The model is expected to be mathematically complete but Route-A negative.  Its
resonant orbits form clean positive-dimensional families, and natural trap
quantization remains candidate-local.  The strict evaluation is therefore
frozen before computation as

```text
(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)
overall = ROUTE_A_REJECTED; route_b_invocation_allowed = false.
```
