# HCS-C56 exact experiment plan

Status: **DOCS_FINAL_NO_MORE_EDITS; PHASES 0--7 PASS FOR THE PROJECT
RELEASE_FROZEN.**

## Objective

Produce a compact, independently replayable certificate proving the exact
premises in THEOREM_PACKAGE.md for the frozen HCS-C55 cubic.

## Phase 0: source rebind

1. Resolve the authoritative C55 theorem, certificate, checker, Route, and
   scoped manifest from committed objects.
2. Verify live bytes against the committed objects.
3. Accept the intentional stratified status contract.
4. Run the C55 checker before reading coefficients.
5. Reconstruct the ordered 20-term map, verify degree three, unique exponent
   rows, content one, and fixed positive sign.

**Kill:** any byte, status-contract, checker, coefficient, ordering, or
normalization mismatch.

## Phase 1: surface and Grassmann systems

1. Rebuild \(F\) sparsely.
2. Recheck projective smoothness over \(\mathbf Q\).
3. Generate all six standard Plücker chart parameterizations.
4. On \(U_{01}\), generate \(f_0,\ldots,f_3\).
5. Compute a degree-compatible Gröbner basis and FGLM shape.
6. If \(d\) is not separating, choose the first primitive linear form in a
   fixed height order that is.

**Go:** rank/degree 27 and three nonzero shape constants.

**Branch:** change separating linear form and regenerate all witnesses.

## Phase 2: direct scheme certificate

1. Primitive-normalize \(g,h_a,h_b,h_c\).
2. Store every coefficient and normalization constant.
3. Substitute the three back-solutions into all four \(f_i\).
4. Clear denominators and store/recompute zero remainders.
5. Verify the five complementary-chart ideals with \(p_{01}=0\) are unit.

**Kill:** any nonzero remainder, zero shape constant, degree loss, or uncovered
complement.

## Phase 3: irreducibility

For \(p=7,19,29,37\), or deterministic replacement primes if the imported
surface changes:

1. require good surface reduction and surviving leading coefficient;
2. factor \(g\bmod p\);
3. store complete monic factors with multiplicities;
4. multiply factors back;
5. check derivative gcd one;
6. derive factor degrees and subset sums.

Require the intersection of subset sums to be exactly \(\{0,27\}\).

**Kill:** a proper common degree, repeated factor, bad reduction, leading
coefficient loss, or factor multiplication failure.

## Phase 4: Weyl group and Picard lattice

1. Construct the rank-seven lattice and six reflections.
2. Generate all 27 line classes.
3. Verify each generator preserves the form, canonical class, line set, and
   incidence.
4. Enumerate the group and index-two determinant kernel.
5. Require orders \(51840/25920\).
6. Require one orbit of size 27.
7. Count elements of cycle type \((2,5,5,5,10)\): require 5184 total,
   zero inside \(U\), 5184 outside.
8. Stack \(s_\alpha-I\) and require fixed-space rank one.

**Kill:** any ordinary-\(S_{27}\)-sign substitution, wrong group/order/orbit,
target element inside \(U\), or fixed rank other than one.

## Phase 5: independent checker

The checker independently:

- repeats source import and chart generation;
- repeats direct remainder arithmetic;
- repeats complement ideals;
- repeats modular factors and subset sums;
- reconstructs the Weyl/Picard model;
- derives every terminal claim;
- compares the canonical payload.

No producer import is permitted.

## Phase 6: semantic and runner tests

1. schema rejection tests;
2. all-leaf rebound mutations;
3. at least one cold-process mutation per semantic subtree;
4. source-drift and status-contract mutations;
5. rollback injection after every promotion move for existing and absent
   target sets;
6. default live checker after promotion;
7. byte/mtime nonmutation audit for read-only check mode.

## Phase 7: documentation and paper

After the exact handoff, the documentation lane:

1. has promoted the formal statements to exact prefreeze statements;
2. has filled the exact coefficient/eliminant/modular/group tables;
3. has backfilled the prefreeze payload/schema/certificate/check/manifest
   identifiers;
4. has drafted the paper from the formal package;
5. has completed source-level semantic review and a clean fresh isolated
   compile audit;
6. has completed the controlled bootstrap and official final build;
7. has filled compilation and frozen-release Route/provenance records.

## Planned payload subtrees

1. material_passport;
2. c55_source_lock;
3. surface;
4. grassmann_main_chart;
5. grassmann_complement;
6. irreducibility;
7. we6;
8. theorem_gates.

All arrays have fixed semantic order; narrative strings that are not checked
should be omitted.

## Resource envelope

- normal exact run: at most 10 CPU minutes;
- all-leaf mutation suite: at most 20 CPU minutes;
- memory: at most 4 GB;
- temporary/output disk: at most 50 MB;
- certificate target: below 2 MB.

These remain resource envelopes, not promoted release measurements.

## Current artifact fields

| artifact | current value |
|---|---|
| payload | `5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661` |
| canonical schema | `ef26d7204a38e28aaf00eed8188b31d34d590c9c8a19924f1d0798e40b052d5f` |
| schema file | `adab34998a944c8a4af8db774e511f0453839ea6a6e14e9437ffc259be3da504` |
| certificate | `26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4` |
| independent report | `4ccfb09139a4bfa812ea9c57ff8b65a6a8e603dbdb00e245355a4563386489a9` |
| scoped 12-entry manifest | `20d29af97128e766bb5e59bf6f82f8401c6ed62f279371b031febcefd5d99b4a` |
| semantic gates / rebound / tests | `10/10`; `2684/2684`; `15/15` |
| producer/checker/tests direct fields | bound by scoped manifest; otherwise `null` |
| implementation commit | `b32402f1dd276a2684d3e849dae26150ebb595e1` |
| provenance commit | null; external/not separately promoted |
| full-project manifest successor | root `FULL_PROJECT_HASHES.sha256`; 46 entries, self-excluding, verified separately; digest external-only |
| paper source | `b284a2f17a53b979374a5525a0642472bd7a14cb72f8260de87bea9a15628a29` |
| paper PDF | `ae8f422e3183455206f3459f0952d7e5175633bc534c318bfb7326b08c6c604e` |
| paper log/text | `afd4dc0323cc3139d6a1e8c441210d453c4c51ab4c5b14aa68d2197a7033af60`; `7c1722fa8286b4dcbb03a3acbe1fcec09a3a26890638599168e8844c9c3ae718` |
| compilation report | `e0b39488e2f3f589f6332db7cd09300d10614044763b7fced6c2bd505c698cb5` |
