# HCS-C212: affine-impact bouncing ball with a physical Zeno ledger

This release freezes a gravity-driven ball on the half-line,
`q'=v, v'=-g`, with `g>0`, guard `q=0,v^-<0`, and affine reset
`v^+=r(-v^-)+J`, where `0<=r<=1` and `J>=0`. The outgoing-speed event
map is `P(u)=r u+J`, while the physical flight time is `2u/g`.

The theorem package separates positive-duration hybrid flights from the
adjoined rest state at `u=0`. It gives exact iterates, cumulative event times,
the Zeno/non-Zeno split (`J=0,0<r<1`), the unique forced cycle when `J>0,r<1`, neutral
elastic families, the accelerating `r=1,J>0` boundary, and the transverse
multiplier `P'(u)=r`. An event-map fixed-point series is recorded only as a
formal discrete object and is never identified with a physical-flow zeta.

Reproduce with:

```bash
python3 code/c212_bouncing_producer.py
python3 code/c212_bouncing_checker.py
python3 code/c212_bouncing_sympy_crosscheck.py
python3 code/c212_bouncing_replay.py
python3 code/c212_bouncing_mutation.py
python3 code/c212_release_manifest.py
```

The scope guard is `NO_BAD_EULER_OR_ROOT_NUMBER`. The registered Route-A
record is `overall=ROUTE_A_REJECTED` and
`route_b_invocation_allowed=false`.
