# Actual P210 author replay

Author only; 2026-09-07 UTC. This is not independent manuscript review, root replay or terminal acceptance.

The standalone [verify.py](verify.py) imports only json, collections and functools. It accepts no arguments, reads no data/canonical/pilot/old/reviewer code, and fixes $N=1,\ldots,12$ in source. PARAMETERS.json mirrors the constants as documentary input. Dynamics uses accumulated run sums with OLD adjacent comparisons; an additional cumulative-cut expression is checked on every edge. Births use absolute interval endpoints. The inverse uses independently generated sorted refinements and a right-to-left endpoint-partition DP. Candidate-gate code instead used persistent-cell component unions and a left-to-right transfer. This is a new author implementation, not a new independent manuscript process or an independent derivation of the admitted proof.

## Actual runs and bytes

| Role | Native captured producer | Exact result |
|---|---|---|
| First fresh canonical production | `execution/produce01/` → `author_produce_01/` | Parent exit0; child exit0; 2,631 before/after known inputs identical; all observed extant files pre-pinned; empty stderr |
| Initial verified pair | `execution/pair01/` → `author_pair_01/` | Parent exit0; both child exits0; 2,633 before/after known inputs identical; all three native cmp exits0; empty stderr |

The complete initial producer stdout was copied unchanged to CANONICAL.json only after its actual success. The later pair compares each fresh stdout to the copied canonical and to the other stdout. Full raw stdout/stderr, exact argv/cwd/environment, native return codes and timing records are in every `commands/*/{ATTEMPT,RESULT}.json` with `stdout` and `stderr`. No normalized-text comparison substitutes for raw byte equality.

- Verifier SHA-256: `3a39b297b7140f6c63373ecd5434c8e631ed0d0da3dd41df2442f87c0c8a1c94`.
- Canonical size: **6,471,668 bytes**.
- Canonical SHA-256: `6804839eaff6983bcf363232ae71fecfac60b98c6c55814d75a3fc400c1d56fc`.
- Actual checks per run: **197,471**. Exactly **4,095 states/edges/targets**, **265 image objects**, **265 triangular objects**, **28 in-box surplus witnesses**.
- Full-orbit pressure includes17,215 deleted-cut left-mass checks,3,106 delayed right-birth checks,9,956 new-block mass checks, and24,576 actual suffix-minimum checks. The canonical contains all state rows, complete orbits/birth records, every target's fibre and explicit source list, endpoint coefficients, actual suffix first-part sets/counts/attaining witnesses, both coding directions and all twelve summaries.
- Image counts at masses1–12 are `1,1,2,3,4,7,11,16,25,40,61,94`; maximal depths are `0,1,1,2,2,2,3,3,3,3,4,4`.

The first production and two fresh pairs are five actual author science executions on the unchanged original box. There was no extra enlarged pilot, no scientific counterexample, and no failed author scientific attempt. This says nothing about the truth of unclaimed larger-box patterns or the historical candidate failures.

## Exact runtime key

The driver and children use `/usr/bin/python3.10 -I -S -B`, with explicit absolute absent `-X pycache_prefix` paths. Every dedicated cache prefix remained absent. In addition to live/copied verifier, parameters, proof, claim/source documents and canonical, the key includes helper sources, interpreter, stdlib sources/extensions, relevant binaries and library dependencies, conservative native-library coverage, all installed locale/gconv contexts, loader/configuration files, explicit child environment, flags, import/module inventories and before/after mapped-library snapshots. `INPUTS_BEFORE.json`, `INPUTS_AFTER.json`, `runtime_1.json`, `runtime_2.json` and the exact report expose these roles completely. No site package or bytecode input was observed; missing observed inputs are an empty list.

The child environment is explicit C locale/UTC with fixed source-date settings, a dedicated empty home and temporary directory, and a minimal system PATH. No caller credentials or external scientific data are required. A post-hook audit plus before/after `/proc/self/maps` is a bounded observed runtime inventory, NOT an OS syscall/startup trace or continuous observation. Many conservative pinned files were not consumed. Source-only means own sources are copied and the installed interpreter/stdlib are pinned, not copied wholesale.

## Reproduction

The exact selected complete command is in `execution/pair02/ATTEMPT.json`. For a later replay use the documented evidence.py `pair` invocation with an entirely absent output directory and absent cache prefix. Never point a producer back at `author_produce_01`, `author_pair_01` or `author_pair_02`; all evidence outputs are immutable. The report's internal PAYLOADS.json is a complete nonself inventory of its own directory, and the paper's outer SHA256SUMS covers both inventories and all raw artifacts.

Root must independently inspect these original sources/streams and execute its required strict author pair before adopting Round0. Independent manuscript A/B and all later lifecycle gates remain pending. Authors and author-evidence contributors cannot fill either review role.

## Selected final proof-document key

After the integer-domain clarification recorded in AUTHOR_REVISION_LOG.md, the distinct `execution/pair02/` → `author_pair_02/` pair passed with parent and both child exits 0, all three native raw comparisons 0, 2,633 unchanged known inputs and no unpinned observation. Both runs again produced exactly 197,471 checks and the identical canonical SHA-256 above. No verifier or scientific output changed. Initial producer/pair01 old live proof pins resolve through their exact physical source copies in HISTORICAL_INPUT_ROLES.actual.json; those original pin files are unchanged.
