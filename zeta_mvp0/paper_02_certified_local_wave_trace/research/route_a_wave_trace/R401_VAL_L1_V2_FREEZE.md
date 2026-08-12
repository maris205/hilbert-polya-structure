# R401-VAL-L1-V2 production freeze

Frozen on 2026-08-06 after the guarded-hull 128-bit pilot and before the V2
two-precision production run.

## Proof inputs

| Component | SHA-256 |
|---|---|
| `validated/capd_r401_local_slab_grid_mp.cpp` | `9fb83e31937f8006e25cecbea818d74d90c107570f9369c9a03f7577894b1179` |
| `research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN_V2.json` | `a27ca53bee45ccf3bad2aff1fa93949376a522d1f54525c9be8aae9ecc297664` |
| `research/route_a_wave_trace/R401_VAL_L1_PROTOCOL_V2.md` | `fd41a010d94bd9c9305a3ac35f633e36675dd9acc7fd6ec61e5e54718f012699` |
| `research/route_a_wave_trace/R401_VAL_PROTOCOL_V2_FREEZE.md` | `f6f99e7c4bdd86da332848badf439eb3ed5882b8c3fd355b28b2289cf5e049a0` |
| `research/route_a_wave_trace/A411_RADIAL_PERIOD_BOUND.md` | `b991cf5ffce043db60ceaf2448f383364c66dca66812180fb996c19debcd11bb` |
| `research/route_a_wave_trace/A411_WARPED_PERIOD_FLOOR.md` | `71cc840cd6518ecb4672402fbe2517ae5096bb654872abce32ef21d02a7e26d8` |

## Execution and checking code

| Component | SHA-256 |
|---|---|
| `scripts/run_r401_val_l1_branch.py` | `63cc2638daeb056d3ae7ecd334a909da903299699e12177e44cb1681a5caba00` |
| `scripts/check_r401_val_l1_independent.py` | `3dd035d7cecdc2ea2a51690542c26267ce1e4af9cafe8f1795c8a8d00753de63` |
| `scripts/prepare_r401_val_l1_slab_plan.py` | `45e6b804983e7f16969cd48a7d99101277ea700e0173353710cbfd089e51f7bb` |

## Guarded-hull amendment

Each bridge root box is the exact Decimal coordinatewise hull of its two
adjacent primary boxes, padded by the pre-frozen rational amount `1e-18` on
each side and in each of the four coordinates.  The checker accepts no
comparison tolerance: it must verify ordinary exact containment of the
actual printed MPFR primary boxes in the actual printed bridge box.

The V2 128-bit pilot established:

- 101/101 validated jobs pass;
- 101/101 exact-rational Krawczyk replays pass;
- 50/50 actual printed bridge boxes contain both adjacent actual primary
  boxes;
- the pilot remains non-production because it omits 256-bit replication.

The external stack, Taylor order, tolerances, job counts, status namespace,
and claim boundary are unchanged from the L1 freeze.  Required success is
`PASS_CONTIGUOUS_LOCAL_BRANCH` with `final_status: null`.
