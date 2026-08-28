# Experiment plan

## Claim-bearing proof work

1. Integrate the endpoint constraints and reduce every admissible transfer to
   two moments of a bounded control.
2. Apply the sharp one-dimensional rearrangement inequality at fixed control
   mean to obtain the exact reachable interval for the first moment.
3. Solve the active endpoint of that interval on the two sides of
   `F_a=x+v|v|/(2a)=0`; derive the arc lengths and switch state.
4. Prove the terminal identities, nonnegative durations and symmetry/scaling
   laws.  Verify the value equation classically off the curve and in the
   viscosity sense globally.
5. Use the affine Pontryagin switching function as an independent structural
   certificate, not as the sole sufficiency argument.

## Executable evidence

The producer serializes 105 exact rational states across three acceleration
bounds, including origin, direct-braking and both one-switch sides.  The
checker imports no producer code and reconstructs every branch, radical,
time, switch state, terminal state and HJB residual at 100 digits.  SymPy
rebuilds the generic identities.  A clean subprocess must reproduce the JSON
byte for byte.  Repaired-hash semantic/schema, unknown-key and stale-hash
mutations must all fail.

## Paper and release

Compile three content-distinct revisions at `SOURCE_DATE_EPOCH=1787875200`
with LuaLaTeX.  Require byte-identical fresh final builds, embedded/subset
fonts, clean log, extractable text and page-by-page visual inspection.  Freeze
exactly 27 payload files plus the self-excluded manifest.
