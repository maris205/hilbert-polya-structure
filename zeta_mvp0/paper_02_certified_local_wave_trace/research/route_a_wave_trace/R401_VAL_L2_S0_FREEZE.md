# R401-VAL-L2-S0 prospective production freeze

Freeze date: 2026-08-06 (UTC)  
Protocol ID: `R401-VAL-L2-S0`

## Licensed question

This run asks only whether the validated local-complement tree implementation
can exclude every point of

\[
B_{\rm loc}\setminus B_{\rm L1}(\epsilon),\qquad
B_{\rm loc}=[-.02,.02]\times[.12,.17]\times[-.08,.08]\times[.64,.69],
\]

for the three representative accepted L1 slabs `S000`, `S025`, and `S050`,
independently at 128 and 256 MPFR bits.  A pass is an implementation smoke,
not an all-51-slab complement theorem.  It licenses no phase/global cover,
trace-formula, prime, Hilbert--Polya, zeta-zero, or RH statement.

## Frozen production matrix and algorithm

- slabs: exactly `S000`, `S025`, `S050`;
- precision: exactly 128 and 256 MPFR bits;
- six trees in total, one per `(precision, slab)` pair;
- initial domain: the exact eight-shell decomposition in the protocol;
- split: exact midpoint of the coordinate of greatest normalized width;
- resource limits: depth 40 and at most 20,000 evaluated nodes per tree;
- acceptable terminal classes: `ENERGY_EXCLUDED` and `RETURN_EXCLUDED` only;
- `ROOT_CANDIDATE`, unresolved leaves, invalid leaves, missing evaluations, or
  any exclusion/Krawczyk conflict make the run non-licensing.

The frozen mathematical separation/gap thresholds are strictly
\(10^{-30}\) at 128 bits and \(10^{-60}\) at 256 bits.  The producer forms
an internal factor-two MPFR margin (`2e-30`, `2e-60`) so conversion cannot
fall below the mathematical threshold.  Archived Newton display enclosures
are expanded by `1e-40` and `1e-75`, respectively; these are representation
guards, not acceptance tolerances.

Both precisions must cover the same exact decimal input domains and reach the
same domain-level verdict.  Their adaptive tree shapes and leaf counts need
not coincide.

## Accepted L1 protected-box gates

Before production, the runner must replay the authoritative A4.12 L1 release,
show each exact planned protected box is contained in the actual outward
validated `X`, and show the Krawczyk image is strictly inside that planned
box.  The frozen minimum plan-box/image margins are:

| Precision | Slab | Minimum strict margin |
|---:|:---:|---:|
| 128 | S000 | `0.000010333845754599556392782729091294036756701` |
| 128 | S025 | `0.000009815914181266807272639303265980184121975` |
| 128 | S050 | `0.000009372525596175314418601393093868006164564` |
| 256 | S000 | `0.000010333856132628695223570103380616507381888475551992072495201970200431927439276098` |
| 256 | S025 | `0.000009816606490374309830935179078504884401695098140598734916905461457950045733041574` |
| 256 | S050 | `0.000009375348167466663689709330840147610189201765127021554240517428134304593237785806` |

## Frozen source and protocol hashes

| File | SHA-256 |
|---|---|
| `validated/capd_r401_local_complement_mp.cpp` | `8eabb022f92c712805c401fb07e2b741e4af4e927bc43702c95125b2a4338bd2` |
| `research/route_a_wave_trace/R401_VAL_L2_S0_LOCAL_COMPLEMENT_PROTOCOL.md` | `ced4df08866a6ed3a9fa140bd6ab7418fcc609881f5835172b662fd04d9b9767` |
| `scripts/run_r401_val_l2_s0_local_complement.py` | `2f2f4aed58405ad8dcaef929623f07e543013dbb627365623da1d3cf529dbbcf` |
| `scripts/check_r401_val_l2_s0_local_complement_independent.py` | `1227e5a5108fae23202ce26d462e4fef446117b594df5e4ec9f58c061a9defa8` |
| `research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json` | `a27ca53bee45ccf3bad2aff1fa93949376a522d1f54525c9be8aae9ecc297664` |
| `validated/CAPD_DEPENDENCY.md` | `74ace207ca6322004ee061fe7c47dcc96c34c421446a47b1c6c9f3d29e470d4b` |

## Frozen upstream L1 authority

| File | SHA-256 |
|---|---|
| `results/r401_val_l1_branch/RELEASE_PROVENANCE.json` | `141131916c3a23e38bf2bd3b66a152c1dc6590881bc52baf51818fd988d3200b` |
| `results/r401_val_l1_branch/summary.json` | `e9a71dfd61d26396d05b62a848f49577fdabdf3722101432455435d32bb7503c` |
| `results/r401_val_l1_branch/manifest.json` | `3c653e50042050e69a8928dd1fc7dac3464b6ae8e7ea8d47c70a03e970ece860` |
| `results/r401_val_l1_branch/independent_checker.json` | `a6c0db0fc2190013c221d0ecdd71ac6f86895fbaecad735e1f2814ea232280c2` |
| `results/r401_val_l1_branch/POSTCHECK_STATUS.json` | `83726312ea975ad9741bf2c802bb03fd0898c76646587c2012eb24401537aaf6` |

## External numerical dependency

CAPD 6.1.0 is pinned at commit
`731079217a9254ea2948d742df2b170895effe7f`.  Production must use its
MPFR-backed intervals with the MPFR/GMP and directed-rounding build flags
required by `validated/CAPD_DEPENDENCY.md`.

## Authority split

The producer may emit only `PASS_S0_PRODUCER`.  It must leave
`milestone_status` and `final_status` null.  Only a zero-failure run of the
frozen independent exact-decimal checker may assign
`PASS_IMPLEMENTATION_SMOKE`; `final_status` remains null even after that pass.
The release provenance is written only after the checker and postcheck exist.
