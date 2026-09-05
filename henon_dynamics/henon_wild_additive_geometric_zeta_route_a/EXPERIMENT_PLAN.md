# Frozen exact-validation plan

The source equation and clocks are frozen before evidence generation. No training, validation or test target-zero regions exist because target matching is STOP_SCOPED.

Producer: dense modular polynomial Euclid, direct finite-field arithmetic, integer Möbius inversion, rational residue and interior-tail bounds. Checker: independent sparse Euclid, modular matrix rank over explicit small-field bases and strict recursive typed schema comparison; it imports no producer.

Coverage: 1344 prime-iterate rows, 5760 extension rows, 896 coefficient controls, 9 direct field recounts, 9 residue intervals and 18 tail bounds. Symbolic checks use exact SymPy arithmetic. Two-directory replay must reproduce the evidence bytes. Hostile mutations repair evidence hashes before semantic checking and attack raw YAML separately. Smoke tests and all optimized-mode refusal gates are compulsory.
