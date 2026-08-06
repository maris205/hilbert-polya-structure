# R401-VAL-L1-V2 contiguous local branch

Milestone status: **PASS_CONTIGUOUS_LOCAL_BRANCH**.

The run evaluated 51 primary parameter slabs and 50 bridge hulls at both
128-bit and 256-bit MPFR precision.  The union of the primary slabs is
`epsilon in [0,0.101]`; the bridge certificates identify all adjacent local
solutions as one branch.

- smallest strict Krawczyk interior margin: `0.000009323437289176983550817013627`;
- largest certified infinity-norm contraction bound: `0.0339894097664427162455372693363021517663097132`;
- smallest certified `dK/dQ_plus` lower bound on the phase interval:
  `8.95504096447634587468922402392622771998519928`;
- total validated jobs: `202`
  of `202`;
- wall time with `20` workers: `420.594` seconds.

The phase gate and exact energy conservation recover the omitted `Q_plus`
return equation, and the existing short-period exclusion makes the certified
returns primitive.  The result proves uniqueness only inside the frozen
local boxes.  It does not exclude other roots, close the global covers,
promote `delta_tr`, or imply any Hilbert--Polya/RH statement.
