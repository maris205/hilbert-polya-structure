# Reversible conservative sieve simulation fails the non-arbitrariness test

**Record ID:** `ASFS-SCOUT-20260913-09`  
**Status:** `PRE-P0 REJECTED; Route B NOT INVOKED`

The prior-work lineage makes it tempting to embed the sieve's symbolic update in a reversible conservative system and then use that system as a symplectic lift. There are constructions of Turing-complete area-preserving diffeomorphisms of the disk, so such an embedding is not excluded by area preservation alone.

That observation rejects—not admits—the architecture. A universal reversible simulator can equally encode primes, composites, random labels, or any prescribed computable sequence through program/initial-condition choice. Thus the purported prime mechanism resides in external programming, and passes the `PROVES_TOO_MUCH` control. It also has no canonical single prime-orbit/repetition rule. `stop`: future lineage candidates must use intrinsic sieve admissibility or deformation constraints that distinguish prime structure from arbitrary computable output.
