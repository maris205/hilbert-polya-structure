# C77 code map

The C77 code is intentionally split into independent gates:

- the producer binds C76 and writes canonical Möbius/reliability evidence;
- the checker reconstructs the subgroup poset, `n_H`, Möbius inversion, and
  all 65536 direct support polynomials independently;
- the cross-check evaluates the incidence relation and top factorization;
- the replay checker runs in a clean interpreter;
- the mutation test changes semantic evidence fields and requires rejection.

Run the scripts from this directory with `python3`.  The producer must be run
before the checker.  All scripts must preserve the C73/C75/C76 authority hashes and
the literal scope firewall `NO_BAD_EULER_OR_ROOT_NUMBER`.

The central implementation identity is

```text
P_{<=H}(q) = q^(16-n_H)
P_{=H}(q)  = sum_{K<=H} mu(K,H) P_{<=K}(q)
           = sum_{A:Phi(A)=H} (1-q)^|A| q^(16-|A|).
```

No script is permitted to substitute an abstract subgroup lattice, numerical
floating-point probabilities, or the non-faithful 11520-element lift.
