# C87 experiment plan

1. Rebind the C73/C76/C78/C81/C82 evidence and manifests by raw-byte SHA-256.
2. Build `F(A)` from containment of one of C73's 25 minimal generating edges;
   require exactly 30400 true supports among all 65536 subsets.
3. For every label `i`, enumerate `Delta_i F(A)` over all `2^15` coalitions,
   retaining the complete 16-cell coalition-size swing vector, raw swing sum,
   exact uniform Banzhaf value, and exact factorial-weighted Shapley value.
4. For every unordered pair `{i,j}`, enumerate `Delta_ij F(A)` over all
   `2^14` coalitions.  Retain positive, negative, zero, signed, and
   coalition-size-resolved counts plus both exact interaction normalizations.
5. Reconstruct the faithful label group from C76's five permutations; require
   order 1920, seven label orbits, 27 pair orbits, orbit-invariant rows, and
   full coverage of 16 labels and 120 unordered pairs.
6. Independently rebuild the truth table from C78's pivot/block criterion.
   Separately use SymPy's multilinear Boolean polynomial to recover every
   first and second coalition-size enumerator.
7. Verify Shapley efficiency, the per-label pair endpoint identity, all C73
   first-order baseline rows, replay determinism, and hostile mutations.
8. Compile twice in isolated directories with `SOURCE_DATE_EPOCH=0`; require
   byte-identical PDFs, embedded fonts, no undefined references/citations,
   clean layout, and a complete prefreeze manifest.

All arithmetic is exact integer or rational arithmetic.  There is no Monte
Carlo stage and no external network dependency.
