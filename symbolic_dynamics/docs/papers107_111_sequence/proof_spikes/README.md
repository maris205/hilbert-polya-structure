# Proof-spike register — P107–P111

## Surviving spikes

| prospective paper | spike | frozen early result |
|---:|---|---|
| P107 | `../scouting/code/root_annihilator_power_spike.py` | 38,850 initial assertions; exact resonance/depth and literal moduli through 500 |
| P108 | `../scouting/code/root_capped_fibonacci_spike.py` | 89,764,177 initial assertions; every state for caps through 250 |
| P109 | `../scouting/code/algebraic_nilpotent_image.py` | 136,487 assertions; 14 `(q,d)` lanes and every rank-transition cell |
| P110 | `../scouting/code/combinatorial_partition_shift_join.py` | 164,113 assertions; all Bell states through `n=9`, including statewise deepest classification |
| P111 | `../scouting/code/stochastic_heisenberg_area.py` | 72,361 assertions; every word through length 15 and independent Gaussian-polynomial slices |

Paper-local verifiers are stronger canonical descendants and receive fresh
stored-output runs after manuscript freeze.

## Adversarial negative spikes

- `root_nilpotent_subspace_spike.py` falsified the proposed pivot-gap depth
  for `U -> U+N(U)` over `F_2^4`; the system was killed rather than patched
  around the counterexample.
- `algebraic_subspace_sweep.py` passed 1,442,212 assertions but was demoted by
  a direct lattice-sorting neighbor and the internal sorting firewall.
- `combinatorial_degree_parity_cut.py` passed a strong parity dichotomy but
  the odd-order projection is Seidel-owned.
- `stochastic_clipped_span.py` passed 226,603 assertions but collided with a
  direct random-walk-span owner and P93/P101.

Exact computation here is a falsification layer.  It neither proves the
infinite-family statements nor establishes novelty.
