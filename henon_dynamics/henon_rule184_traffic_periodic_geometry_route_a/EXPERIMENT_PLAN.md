# C175 verification plan

This is a theorem package, so no GPU or statistical experiment is appropriate.

1. Freeze cyclic labelled sites, the simultaneous Rule-184 clock, every `N>=1`, every conserved sector, and the Artin--Mazur convention.
2. Prove the low-density no-`11` and high-density no-`00` periodic-core classification.
3. Prove finite attraction with the gap zero-count Lyapunov mechanism and an explicit `m^2` bound.
4. Derive the cyclic-independent-set formula, every-iterate fixed count, Möbius primitive cycles, and sector zeta product.
5. Prove that the full sector is bijective exactly for `m<=1`; separate its Koopman operator from the canonical periodic-core unitary.
6. Exhaust every binary word through `N=12`, every sector, and iterates through `2N+2`; check with a particle-move implementation independent of the producer.
7. Cross-check independent-set, fixed-count, Möbius and gap identities in SymPy; byte-replay the producer and reject repaired-hash and stale-hash mutations.
8. Compile three materially distinct manuscript rounds; require deterministic final PDF bytes, embedded fonts, clean logs, visual snapshots, and a self-excluded manifest over exactly 27 payload files.

Falsifier: a periodic non-core word, a core word whose period does not divide `N`, one violation of the fixed-count formula, attraction slower than `m^2`, a bijective `m>=2` sector, a positive arithmetic claim, or any scope flag set true rejects the package.
