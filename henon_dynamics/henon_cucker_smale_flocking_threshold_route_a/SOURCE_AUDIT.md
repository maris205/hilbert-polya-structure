# Source audit

## Verified primary lineage

1. F. Cucker and S. Smale, *Emergent Behavior in Flocks*, IEEE Transactions on
   Automatic Control 52 (2007), 852--862.
   DOI: <https://doi.org/10.1109/TAC.2007.895842>.
2. S.-Y. Ha and J.-G. Liu, *A Simple Proof of the Cucker--Smale Flocking
   Dynamics and Mean-Field Limit*, Communications in Mathematical Sciences 7
   (2009), 297--325.
   DOI: <https://doi.org/10.4310/CMS.2009.v7.n2.a2>.

The first source introduces the model and its long-/short-range flocking
split.  The second supplies the Lyapunov-tail proof lineage.  Both DOI/title
records were checked against publisher or author-hosted bibliographic pages on
2026-09-04.

## Claim boundary

The package rederives every normalization used here.  Citations establish
lineage, not priority for this packaging, evidence format, or boundary atlas.
No mean-field limit, noisy flocking, singular communication, collision
avoidance, delayed interaction, or nonlinear stability beyond the frozen
system is claimed.  In particular, failure of the many-body sufficient
inequality is not labelled non-flocking.

## Nearest repository collisions

- C203: a fixed signed-Laplacian first-order consensus semigroup;
- C333: random edge gossip with a finite second-moment decomposition;
- C347: noisy mean-field Kuramoto phase synchronization.

C362 instead owns a deterministic second-order position--velocity system with
a coevolving distance-dependent complete graph, a tail barrier, and a sharp
two-body escape face.
