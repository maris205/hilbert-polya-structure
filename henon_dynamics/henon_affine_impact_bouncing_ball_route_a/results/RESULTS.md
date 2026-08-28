# C212 exact results

- Twelve rational (g,r,J,u0) controls cover five regimes and boundaries.
- Each control stores eight affine iterates, eight physical roof times, and
  cumulative times (96 event-time cells total), plus three exact interior
  impact reconstructions (36 cells).
- The independent checker passes 368 exact assertions. It explicitly fixes
  the regular section as S_+=(0,infinity), treats r=0,J=0 as one-flight
  sticking rather than infinite Zeno, and keeps the closed-section affine
  series separate.
- SymPy passes 11 identities and byte replay is exact.
- Hostile audit rejects 13 repaired-hash semantic mutations and one stale-hash
  mutation, including an attack that relabels the r=0,J=0 edge as Zeno.

The event-map series is formal and is never interpreted as a physical-flow
zeta or a target arithmetic object.
