# C228 code

The producer emits exact Cayley coefficients and high-precision pregel,
critical, Smoluchowski/Stockmayer and Flory rows.  The independent checker
reconstructs all coefficients, moments, branch roots and loss-term residuals
without importing the producer.  SymPy checks the generic tree and moment
identities; replay compares clean-process bytes; mutation tests repaired and
stale semantic/schema attacks.

Run from repository root:

```bash
python henon_dynamics/henon_smoluchowski_product_kernel_gelation_route_a/code/c228_coagulation_producer.py
python henon_dynamics/henon_smoluchowski_product_kernel_gelation_route_a/code/c228_coagulation_checker.py
python henon_dynamics/henon_smoluchowski_product_kernel_gelation_route_a/code/c228_coagulation_sympy_crosscheck.py
python henon_dynamics/henon_smoluchowski_product_kernel_gelation_route_a/code/c228_coagulation_replay.py
python henon_dynamics/henon_smoluchowski_product_kernel_gelation_route_a/code/c228_coagulation_mutation.py
python henon_dynamics/henon_smoluchowski_product_kernel_gelation_route_a/code/c228_release_manifest.py
```

The first 20 coefficients are regression controls.  Infinite-tail and moment
claims are proved analytically and reconstructed symbolically rather than
inferred from truncation.
