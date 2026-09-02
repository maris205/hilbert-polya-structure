# Dubins six-word global synthesis theorem

Normalize the turning radius to one and the initial pose to `(0,0,0)`.  For
target `(x,y,phi)`, let `d=hypot(x,y)`, `theta=atan2(y,x)`,
`alpha=(-theta) mod 2pi`, and `beta=(phi-theta) mod 2pi`.

## Theorem

Every shortest forward curve satisfying

`xdot=cos(theta), ydot=sin(theta), |thetadot|<=1`

belongs to `LSL`, `RSR`, `LSR`, `RSL`, `RLR`, or `LRL`, with zero-length
pieces allowed.  The six explicit triples in the paper are complete:

- `LSL` and `RSR` use external-tangent square-root tests;
- `LSR` and `RSL` use internal-tangent square-root tests;
- `RLR` and `LRL` exist exactly when their three-circle cosine argument lies
  in `[-1,1]`.

For every feasible word, direct primitive integration reaches the target.
The global distance is the minimum of `t+p+q`; all words attaining that
minimum are retained.  At discriminant zero, a straight piece may collapse;
at cosine argument `+1` or `-1`, a middle arc collapses or becomes a half
turn.  The convention `atan2(0,0)=0` and `2pi mod 2pi=0` makes every boundary
receipt deterministic without changing its geometric curve.

For radius `R>0`, normalize positions by `R` and multiply every length by
`R`.  Rigid motions preserve the distance, and reflection
`(x,y,phi)->(x,-y,-phi)` exchanges `L` and `R`.

## Route-A result

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and
`ROUTE_A_REJECTED`.  The source control Hamiltonian is an exact extremal
device only; it carries no target spectral meaning.
