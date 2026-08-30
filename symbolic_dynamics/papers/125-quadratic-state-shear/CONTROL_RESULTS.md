# P125 exact-control results

Status: **ROUND-TWO PAPER-LOCAL PASS / ALL-SIZE CLAIMS PROVED SYMBOLICALLY /
GO_INTERNAL / EXTERNAL HOLD**.

Run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

The verifier uses only the Python standard library.  It makes no network
call, floating-point comparison, random draw, or computer-algebra call.  The
canonical transcript is `code/verification_output.txt`.

## Frozen result

```text
P125 quadratic-state shear exact audit
literal_im2_equals_recurrent PASS
literal_six_component_shapes PASS
ASSERTIONS 27405887
PASS
```

## Coverage

For the zero-dimensional plus boundary and both Witt signs for `1<=m<=5`,
the audit checks:

- the two canonical nonsingular forms and their singular/nonsingular census;
- polarization, the literal update, polar invariance, and all quotient
  transitions;
- every pointwise transient depth and eventual period;
- every inverse candidate and the complete fibre of every target;
- all eight type counts, all three depth layers, fibre mass, image sizes, and
  all cycle counts;
- literal pointwise equality between `im(Phi^2)` and the recurrent set;
- traversal of every functional component, canonicalization of its directed
  cycle decoration up to cyclic rotation only, an asymmetric sentinel that
  forbids reflection identification, exclusion of any seventh shape, and the
  six exact component counts.

The largest lane has `|V|=1024` and `|V|^2=1,048,576` states.  The canonical
transcript records all eleven form/sign lanes.

## Interpretation

The original paper-local run repaired the two coverage gaps identified at the
proof-spike gate: second-image equality is setwise, and component shapes are
literally traversed rather than inferred only from formula mass.  The
round-one repair additionally makes the directed-cycle convention exact by
removing reflection from canonicalization.  The run remains falsification
evidence; it proves no all-dimension identity or owner, novelty, or priority
statement.
