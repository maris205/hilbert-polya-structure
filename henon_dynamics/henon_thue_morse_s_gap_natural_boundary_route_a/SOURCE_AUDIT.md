# C159 source audit

## Frozen source

The source is the binary S-gap shift with

```text
t_s = parity of the binary digit sum of s,
S = {s>=0:t_s=1},
C = {10^s:s in S}.
```

Successive ones are separated by a number of zeros in `S`; the all-zero
configuration is included as a limit.  One left shift is one clock tick.
Fixed points are counted as labeled configurations, exact-period points are
obtained by Möbius inversion, and geometric cycles are counted only after
division by their period.

## Candidate audit and pivot

The first candidate was a `q`-clock decoration of a Sturmian shift.  It would
have supplied a recurrent minimal system and an exact complexity law, but its
complete periodic vacuum and zeta `1` repeated the central C144 obstruction.
It was rejected before manuscript drafting.  The replacement passes the hard
gate: it is mixing, has dense nontrivial periodic points, has an exact renewal
zeta and entropy equation, and its source meromorphic continuation has a
proved unit-circle natural boundary.

## Evidence ownership

All finite data come from the Thue--Morse parity definition and exact binary
word enumeration.  No external bibliography is needed for a claim path: the
mixing, renewal identity, product identity, radial-zero argument, and natural-
boundary transfer are proved in the package.  The rational entropy bracket is
certified with an explicit geometric tail bound.

## Scope firewall

The ordinary word `prime` does not occur in the construction.  The package
reads no target zero or prime table and asserts no arithmetic/local factor,
Euler factor, root number, automorphy statement, target functional equation,
target counting law, natural self-adjoint lift, or Hilbert--Pólya operator.
Route B is unauthorized.  Literal scope:

```text
NO_BAD_EULER_OR_ROOT_NUMBER
```
