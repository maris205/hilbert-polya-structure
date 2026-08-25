# C139 source audit

## Source class

C139 is an exact, internally constructed symbolic-dynamical candidate.  It
uses no observational data, downloaded tables, numerical fitting, or external
paper result.  The frozen base is the two-sided full binary shift.  The edge
roof `(1,sqrt(2),sqrt(3),sqrt(6))` is retained as the C135 control, and the
single new modeling choice is the forward cyclic marker `0011` with coefficient
`sqrt(5)`.

## Frozen conventions

- States are the ordered three-blocks `000,001,010,011,100,101,110,111`.
- The transition `abc -> bcd` has weight
  `x_ab*y^(1_[abcd=0011])`.
- A length-`n` periodic word has exactly `n` forward starting coordinates;
  wraparound marker occurrences are included.
- `Delta_139=det(I-M_139)` and the specialized zeta is its reciprocal.
- `x_ab=z*exp(-s*tau_ab)` and `y=exp(-sqrt(5)*s)`.
- The finite period-12 enumeration is a replay sentinel, not a theorem cutoff.

## Provenance and independence

The producer constructs the finite evidence from the frozen definition.  The
checker imports no producer code and recomputes cyclic block counts, primitive
necklaces, an eight-state path trace, all schemas, and all boundaries.  SymPy
separately reconstructs the determinant and twelve symbolic traces.  The byte
replay invokes the producer in a temporary directory.  Hostile tests repair
the payload hash after each semantic mutation before expecting rejection, plus
one stale-hash control.

## Firewall

No prime table, zero table, arithmetic/local factor, Euler factor, root number,
automorphy datum, target divisor, Hilbert--Polya operator, or Route-B input is
used.  Literal scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
