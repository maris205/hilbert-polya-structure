# R401-VAL-L1 production freeze

Frozen on 2026-08-06 before the two-precision production run.

## Proof inputs

| Component | SHA-256 |
|---|---|
| `validated/capd_r401_local_slab_grid_mp.cpp` | `9fb83e31937f8006e25cecbea818d74d90c107570f9369c9a03f7577894b1179` |
| `research/route_a_wave_trace/R401_VAL_L1_FINAL_PLAN.json` | `3d9698bd15f2d6f0d8632c364c9f2d26180b59f731da17d90fbd1d618227ca50` |
| `research/route_a_wave_trace/R401_VAL_L1_PROTOCOL.md` | `3942d7ebcfbf4cb1b91962785869d11476745d2777c3169b1bca048218a8ff18` |
| `research/route_a_wave_trace/R401_VAL_PROTOCOL_V2_FREEZE.md` | `f6f99e7c4bdd86da332848badf439eb3ed5882b8c3fd355b28b2289cf5e049a0` |
| `research/route_a_wave_trace/A411_RADIAL_PERIOD_BOUND.md` | `b991cf5ffce043db60ceaf2448f383364c66dca66812180fb996c19debcd11bb` |
| `research/route_a_wave_trace/A411_WARPED_PERIOD_FLOOR.md` | `71cc840cd6518ecb4672402fbe2517ae5096bb654872abce32ef21d02a7e26d8` |

## Execution and postcheck code

| Component | SHA-256 |
|---|---|
| `scripts/run_r401_val_l1_branch.py` | `f2bdddb6ce8c66e19e819c6fb7d4f8d9413a16f9fc27c17db2a295c7a34a3d93` |
| `scripts/check_r401_val_l1_independent.py` | `8026eb46040a5b14da3bbd167e0683f77bd8490113cbf3aa193b7a691228a505` |
| `scripts/prepare_r401_val_l1_slab_plan.py` | `261127ad8ef95491ef83c828a98d418871de180dcbf21a624ec0783d837d699d` |

The old `R401_VAL_L1_SLAB_PLAN.json` is an exploratory artifact and is not a
proof input.  The final plan contains 51 primary slabs and 50 exact Decimal
bridge hulls.

## External stack and numerical contract

- CAPD commit: `731079217a9254ea2948d742df2b170895effe7f`;
- CAPD multiprecision build with MPFR, GMP, and directed rounding;
- Taylor order 24;
- 128-bit tolerance `1e-30`;
- 256-bit tolerance `1e-60`;
- 101 tasks at each precision;
- 202 strict validated-flow/Krawczyk jobs in total;
- 51 primary boxes plus 50 bridge hulls;
- required independent exact-rational replay of every printed Krawczyk
  operator.

The 128-bit freeze-candidate pilot passed all 101 jobs and all 101 independent
arithmetic replays.  It is not a production result because it intentionally
omitted 256-bit replication.

Production command:

```bash
python scripts/run_r401_val_l1_branch.py \
  --workers 20 \
  --output results/r401_val_l1_branch

python scripts/check_r401_val_l1_independent.py \
  --result results/r401_val_l1_branch
```

The only authorized success milestone is
`PASS_CONTIGUOUS_LOCAL_BRANCH` with `final_status: null`.
