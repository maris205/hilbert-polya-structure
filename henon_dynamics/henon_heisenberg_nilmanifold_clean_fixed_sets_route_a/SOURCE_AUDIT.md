# C146 source audit

## Source class

C146 is an exact internally constructed nilmanifold example.  It uses no
downloaded data, fitted parameter, external numerical table, or paper-derived
constant.  The only inputs are the upper-triangular Heisenberg group, its
integer lattice, and `A=[[2,1],[1,1]]`.

## Frozen coordinate and quotient conventions

- `H=R^3` has product
  `(x,y,z)*(X,Y,Z)=(x+X,y+Y,z+Z+xY)`.
- `Gamma=Z^3`; the compact nilmanifold is the left quotient `Gamma\H`.
- `q(x,y)=x(x-1)+xy+y(y-1)/2`.
- `Phi_A(x,y,z)=(2x+y,x+y,z+q(x,y))`.
- The clock is the positive iterate number `n`.
- The ordinary stability expression is tested only as an obstruction.
- The iterate-20 ledger is finite evidence for exact formulas proved for all
  positive iterates.

The correction `q` is essential: its polarization is the difference between
the transformed and original Heisenberg cocycles, and it is integer-valued on
`Z^2`.  Thus `Phi_A` preserves the lattice and descends to the quotient.

## Evidence independence

The producer constructs the exact matrix/Lucas ledger and the period-two
cocycle witness.  The standard-library checker imports no producer code and
recomputes the group identity, lattice integrality, all 20 matrix powers,
cohomological receipts, and the counterexample.  SymPy separately reconstructs
the polynomial identities and derivatives.  Replay demands byte identity.
Hostile tests repair each semantic payload hash before demanding rejection,
plus a stale-hash control.

## Corrected claim boundary

An initial design inference lifted the toral count directly to the nontrivial
circle bundle.  Internal audit found this invalid: at `n=2`, the horizontal
class `(1/5,2/5)` is fixed by `A^2` modulo `Z^2`, but its fibre rotation is
`-4/5` modulo one.  The release therefore does not claim that every horizontal
fixed class lifts, and does not state an exact full nilmanifold component
count.

## Firewall

No target table, prime table, arithmetic local datum, Euler factor, root
number, automorphy datum, target divisor, Hilbert--Polya operator, or Route-B
input is used.  Literal scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
