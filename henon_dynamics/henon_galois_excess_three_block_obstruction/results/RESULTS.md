# Results

## Exact finite outputs

- Primitive symbolic cycle counts through period five: `1,0,1,2,2`.
- Width-three relation:
  `N3(gamma3)+N3(gamma5)=N3(gamma4a)+N3(gamma4b)`.
- Width-four selected interpolation determinant: `-1`.
- Period-four-a trace: `-574-192*sqrt(6)`.
- Period-four-a excess: `4.641389525467404250...`.
- Period-five trace degree: `6`.
- Period-five multiplier degree: `12`.
- Physical coordinate root count: `1`; derivative-root counts for
  `(b,c,trace)` are `(0,0,0)` with midpoint signs `(+,+,-)`.
- Period-five excess: `34.497616030977493114...`.
- Strict theorem witness: `E3+E5>E4a+E4b`.

## Validation

- dependency locks: 8/8;
- producer mutations: 17/17 rejected;
- unit tests: 14/14 passed;
- independent symbolic/algebraic reconstruction: passed;
- producer certificate SHA-256:
  `d21cdcdfcce7cb279fab02ee3222c5d5a10e4fc6efa63e2e611d135e2ff27f1c`;
- independent certificate SHA-256:
  `4ee5634c159d62b8b75429f55557090044a8a55a3165b564e9b9202a2dfb6d0b`.
- deterministic final PDF SHA-256:
  `6d7385f9ad6d6b87a56b095b020faa6dbb8289b7e538378aeb7c7655dd19b627`.

## Claim boundary

These results prove a width-at-most-three local-potential obstruction.  They
do not refute a general Hölder or asymptotically additive realization and do
not construct a full weighted determinant or arithmetic trace.
