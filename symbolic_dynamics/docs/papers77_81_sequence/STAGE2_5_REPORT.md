# Stage 2.5 bounded hostile audit — Papers 77–81

Status: **mathematical audit complete; all five retained after corrections**.

## Independent verdicts

| Paper | Initial verdict | Required correction | Final gate |
|---|---|---|---|
| P77 | `KILL/REVISE` unqualified; `GO_SHORT_NOTE` after restriction | CB height `d+2`; absorbing zero beyond the bottom; precise `End`; exclude `d=0` rigidity | `GO` |
| P78 | replacement comparison and direct recomputation | credit Lorenzini as first bipartite-group owner; add current comparator; upgrade safely to arbitrary loading profiles | `GO_SHORT_NOTE_WITH_FIREWALL` |
| P79 | `GO_CONDITIONAL` | add Mohri collision; prove phase recovery/excess/nonmixing/infinite order; separate endpoints and `k=1,2` | `GO` |
| P80 | `GO` | none | `GO` |
| P81 | `REVISE` | close open-ball radius strictness; state invariant marginal/equivariant kernel and Markov-law existence precisely | `GO` |

Codex review MCP was unavailable in the environment.  Independent hostile
subagents therefore supplied the second-signature review fallback required by
the writing workflow.  P77/P80/P81 and P78/P79 were reviewed by agents other
than the final integrating author, and all requested mathematical corrections
were implemented before the final compile.

## Important audit findings retained in the papers

1. P77's lowering maps form truncated addition with an absorbing zero, not a
   saturation at the last layer.
2. P78's general period is the least common multiple of the actual coordinates
   of `Q^{-1}w`; its two-site specialization omits the nonexistent fourth
   coordinate when `n=2`.
3. P79's tensor-channel argument proves a norm onset, not persistence of one
   named noisy cylinder witness; the paper uses the correct statement.
4. P80's natural extension contains only recurrent cycles; transient trees
   cannot contribute a bi-infinite orbit.
5. P81's covering upper bound uses a fixed Voronoi name and equatorial-band
   successor count, avoiding recursive projection error.

## Final release-audit corrections

A second read-only release pass after manuscript generation found and closed
four wording/source issues without changing the mathematical contracts:

- P78 now gives Thomas Selig and Haoyue Zhu's formal WALCOM 2025 record and
  says explicitly that the two-site formula has three, not four, denominator
  classes when `n=2`.
- P79's abstract, introduction, and ownership boundary now distinguish fair
  noise (zero excess entropy and no phase recovery) from nonfair noise, and
  strict nonfair noise from deterministic endpoints for infinite Markov
  order.
- P80 calls the interaction rule symmetric rather than reversible, consistent
  with the proved noninvertibility of the global map.
- P81's open-ball and homogeneous-Markov wording corrections were confirmed in
  both source and final PDF.

Final independent verdicts are P77 `GO`, P78
`GO_SHORT_NOTE_WITH_FIREWALL`, and P79--P81 `GO`.

## Unresolved external gate

The bounded internal audit does not authorize public release or establish
worldwide novelty.  Specialist external review and venue-specific rewriting
remain future actions requiring separate authorization.
