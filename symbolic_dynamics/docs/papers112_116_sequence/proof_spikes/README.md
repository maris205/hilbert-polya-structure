# Proof-spike index

The executable scouting spikes live under `../scouting/code/`; this directory
records how their finite evidence maps to the frozen proof obligations.

| paper | scouting program | falsification / positive role |
|---|---|---|
| P112 | `combinatorial_tournament_score.py` | killed idempotence at `n=6`; retained strict energy, fixed classification and refinement bound |
| P113 | `combinatorial_diagonal_hooks.py` | killed a naive deepest-shell guess; retained exact gap growth, fibres and sharp maximum depth |
| P114 | `root_forest_peeling_spike.py` | checked every state through `n=6`, all endpoint/depth cells and every local fibre |
| P115 | `root_cartier_spike.py` | checked literal fields `F_2,F_3,F_4,F_8,F_9,F_16`, iterates, fibres, depths and core cycles |
| P116 | `stochastic_tropical_resonance.py` | discovered and verified the literal-gap lumping, PGF, cumulants, word extremes and cold-edge structure |

The manuscript directories contain separate canonical `code/verify.py`
programs.  Passing a spike is not cited as a proof and does not license a
claim absent from the frozen theorem contract.

