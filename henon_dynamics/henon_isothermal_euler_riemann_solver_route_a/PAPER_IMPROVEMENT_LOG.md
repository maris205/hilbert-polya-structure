# Two-round substantive improvement log — HCS-C300

## Round 0 — complete solver and wave atlas

- Artifact: `paper/main_round0_original.pdf`
- SHA-256: `d494467b8163758a36e942a588982ab358a18d263be3236eeef0aa86755a9a69`
- Length: 2 pages
- Content: the common piecewise wave function, its unique positive root, all four branch combinations, two fan profiles, and two shock-speed identities.

The first hostile review found that existence formulas alone did not fully expose admissibility or uniqueness: signs needed strict Lax gaps, mechanical entropy needed a direct shock calculation, and no-vacuum needed its precise finite-data chamber.

## Round 1 — admissibility and uniqueness closure

- Artifact: `paper/main_round1.pdf`
- SHA-256: `32020b4388648121ae19fd60ece4ca076476c023190d8265566335017d79936a`
- Length: 3 pages
- Added: strict Lax inequalities for both shock families, ordered family sectors, the convex entropy pair, the exact formula
  \([q]-s[\eta]=a^3\rho_0\sqrt r[\log r-(r-r^{-1})/2]<0\), its derivative proof, exhaustion of both Lax wave curves, and finite-data no-vacuum.

The second hostile review targeted branch-point conventions, density rescaling, the \(a\downarrow0\) limit, collision with C195, and possible promotion of finite rows into an all-data proof or arithmetic claim.

## Round 2 — boundary and release closure

- Artifacts: `paper/main_round2.pdf` and byte-identical `paper/main.pdf`
- SHA-256: `051da17fe465f1314e40a00329bf06d677b598080f8609cd05f6b9af4790e90a`
- Length: 3 pages
- Added: zero-strength waves, constant data, common density scaling, vacuum-input exclusion, two explicit and opposite pressureless asymptotics, 437-cell evidence, independent checking lanes, C195 collision separation, the five-failure Route-A tuple, and scope/AI-use statements.

All hashes differ.  Final build and visual receipts are recorded in `paper/COMPILE_REPORT.md`.

## Final hostile-release hardening

A second machine red team found acceptance gaps in the first release checker rather than in the theorem or paper: selected prose leaves, unknown keys, noncanonical but equal rationals, integer substitutions, duplicate case identifiers, and five repaired-hash YAML edits could survive.  The checker now locks the full model, theorem, proof, nonclaim, collision, reference, boundary, and Route-A evaluation trees; every case/wave/receipt/scaling/probe row has an exact schema and primitive types; rational and decimal receipts have canonical syntax; case identifiers are exact, ordered, and unique; optimized Python is refused; and acceptance uses explicit exceptions rather than removable assertions.  The expanded hostile suite rejects 110/110 attacks.  Since this pass changed verification semantics but not manuscript content, all three archived PDF byte hashes remain unchanged and are rebuilt afresh during release closure.
