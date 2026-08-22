# Experiment plan

1. Freeze the two maps, phase clock, representative samples, adjacency `Q`,
   product convention, and block cutoff `n=1,...,6` before generating data.
2. Enumerate admissible primitive necklaces and retain phase, orientation,
   rooted multiplicity, and cyclic-stabilizer fields.
3. Compute exact chronological, reversed, and same-phase block monodromies,
   repeated traces, transfer traces, determinant prefixes, and Newton data.
4. Reproduce the JSON with an independent checker and SymPy implementation;
   replay canonical bytes and apply semantic mutations.
5. Compile the paper twice in isolated directories with a fixed PDF trailer,
   verify byte identity, fonts, and layout diagnostics.
6. Report only the finite A1/A2 qualification.  A future phase must solve the
   actual non-autonomous periodic equations and supply a geometric coding
   argument before any A1 upgrade.

Controls are chronological `(0,1)`, reversed `(1,0)`, and same-parameter
`(0,0)`.  The control comparison is an internal structural diagnostic, not a
fit to external arithmetic or spectral data.
