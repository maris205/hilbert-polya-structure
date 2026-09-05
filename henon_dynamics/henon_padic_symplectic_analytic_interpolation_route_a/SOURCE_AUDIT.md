# Source and collision audit

The frozen baseline is `697518b6db90458f86f7916fbf397b8ad5ef2372`. The authority is `flow_systems/skills/route-a-evaluator.md`, version 0.2.0, SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`. The source is not silently updated when another branch advances.

Repository-wide Markdown, TeX and Python searches used the mechanism terms `Poonen`, `Strassmann`, `dynamical.Mordell`, `analytic.arc`, `Mahler.*interpol`, `p.adic.*minimal`, and finite cycle-lift alternatives. The following nearest collisions were inspected or checked against their registry contracts:

| Existing package | Exact boundary relative to C394 |
|---|---|
| `henon_dynamics/henon_dyadic_pascal_skew_tower_route_a/` (C166) | Finite affine Pascal tower, not a nonlinear joint Tate action with radius-dependent orbit embeddings |
| `henon_dynamics/henon_dyadic_odd_affine_parity_renewal_route_a/` (C174) | Expanding parity/renewal dynamics; its accelerated and original clocks differ from this near-identity automorphism |
| `henon_dynamics/henon_mixed_lcg_hull_dobell_route_a/` (C258) | Finite affine single-cycle criterion, not the complete nonlinear minimal-component decomposition |
| `henon_dynamics/henon_padic_conductor_shell_heat_semigroup_route_a/` (C283) | A fixed-prime Hilbert multiplier, not interpolation of a nonlinear classical orbit |
| `symbolic_dynamics/papers/23-unary-holonomy-finite-fiber-rigidity/` | Its prior-boundary and proof files use classical linear-recurrence Skolem--Mahler--Lech; the generalized analytic-arc input is explicitly not used there |
| `flow_systems/papers/27-congruence-inverse-limit-no-go/` | Congruence-cover inverse limits, not this polynomial automorphism and its exact local analytic time |

Broader rejected directions included existing Markoff C193, full complex elliptic Lattès C180, finite linear rational-canonical C204, finite abelian power-map C264, and previously parked Bost--Connes/ax+b mechanisms. No code or theorem credit is claimed for increasing their parameters or cutoffs. The retained increment is the entire nonlinear analytic orbit structure and its simultaneous residue/hitting consequences.

Classical ownership is explicit in REFERENCES.md and the main text. The search was bounded and does not prove literature novelty. The recent effective Strassmann paper was found before drafting, so ordinary tails were framed as known tools rather than a new certificate algorithm.
