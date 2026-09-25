# Exact CPU/GPU computation — ANG-20260918-GNS02

## Frozen command and limits

The candidate card was written before execution.  From the repository root,
the exact command was:

```bash
python papers/227-gated-neighbor-period8-extension/evidence/run_extension.py --backend both
```

The script uses `T=8`, coordinates `2,...,16`, `CAP=2_000_000`,
`CHUNK=8192`, unsigned 8-bit temporal words, and no floating-point or
probabilistic operation.  A stage stops before storing extension `CAP+1`;
the first such extension is reported as `extensions_seen=CAP+1`.  The higher
spatial boundary is free.  The pre-existing 139 command and cap 100000 were
not modified.

Runtime environment recorded during the run:

```text
Python 3.12.3
NumPy 2.4.4
PyTorch 2.8.0+cu128; CUDA 12.8
NVIDIA GeForce RTX 4080 SUPER; driver 580.95.05; 32760 MiB total
```

The executed script has SHA-256
`8da180c6240e0f38973cf9212ee601cf88dff2633aa4edc320bebc0a991fd406`.

## Full output

```text
python 3.12.3 platform Linux-5.15.0-78-generic-x86_64-with-glibc2.35
backend CPU-numpy numpy 2.4.4
T 8 CAP 2000000 CHUNK 8192 u2_words [51, 102, 153, 204] initial_prefixes_2_to_3 1024
equation_n 3 input_prefixes 1024 admissible 192 extensions_seen 2052 stored_extensions 2052 max_free_bits 8 capped False free_boundary_existential False
equation_n 4 input_prefixes 2052 admissible 216 extensions_seen 2340 stored_extensions 2340 max_free_bits 5 capped False free_boundary_existential False
equation_n 5 input_prefixes 2340 admissible 336 extensions_seen 5356 stored_extensions 5356 max_free_bits 5 capped False free_boundary_existential False
equation_n 6 input_prefixes 5356 admissible 796 extensions_seen 11892 stored_extensions 11892 max_free_bits 5 capped False free_boundary_existential False
equation_n 7 input_prefixes 11892 admissible 1996 extensions_seen 28000 stored_extensions 28000 max_free_bits 5 capped False free_boundary_existential False
equation_n 8 input_prefixes 28000 admissible 4928 extensions_seen 69664 stored_extensions 69664 max_free_bits 5 capped False free_boundary_existential False
equation_n 9 input_prefixes 69664 admissible 10280 extensions_seen 198064 stored_extensions 198064 max_free_bits 8 capped False free_boundary_existential False
equation_n 10 input_prefixes 198064 admissible 34416 extensions_seen 501520 stored_extensions 501520 max_free_bits 8 capped False free_boundary_existential False
equation_n 11 input_prefixes 501520 admissible 49384 extensions_seen 540304 stored_extensions 540304 max_free_bits 5 capped False free_boundary_existential False
equation_n 12 input_prefixes 540304 admissible 74072 extensions_seen 1122552 stored_extensions 1122552 max_free_bits 5 capped False free_boundary_existential False
equation_n 13 input_prefixes 1122552 admissible 138760 extensions_seen 2000001 stored_extensions 2000000 max_free_bits 5 capped True free_boundary_existential False
backend GPU-torch torch 2.8.0+cu128 cuda 12.8 device NVIDIA GeForce RTX 4080 SUPER
T 8 CAP 2000000 CHUNK 8192 u2_words [51, 102, 153, 204] initial_prefixes_2_to_3 1024
equation_n 3 input_prefixes 1024 admissible 192 extensions_seen 2052 stored_extensions 2052 max_free_bits 8 capped False free_boundary_existential False
equation_n 4 input_prefixes 2052 admissible 216 extensions_seen 2340 stored_extensions 2340 max_free_bits 5 capped False free_boundary_existential False
equation_n 5 input_prefixes 2340 admissible 336 extensions_seen 5356 stored_extensions 5356 max_free_bits 5 capped False free_boundary_existential False
equation_n 6 input_prefixes 5356 admissible 796 extensions_seen 11892 stored_extensions 11892 max_free_bits 5 capped False free_boundary_existential False
equation_n 7 input_prefixes 11892 admissible 1996 extensions_seen 28000 stored_extensions 28000 max_free_bits 5 capped False free_boundary_existential False
equation_n 8 input_prefixes 28000 admissible 4928 extensions_seen 69664 stored_extensions 69664 max_free_bits 5 capped False free_boundary_existential False
equation_n 9 input_prefixes 69664 admissible 10280 extensions_seen 198064 stored_extensions 198064 max_free_bits 8 capped False free_boundary_existential False
equation_n 10 input_prefixes 198064 admissible 34416 extensions_seen 501520 stored_extensions 501520 max_free_bits 8 capped False free_boundary_existential False
equation_n 11 input_prefixes 501520 admissible 49384 extensions_seen 540304 stored_extensions 540304 max_free_bits 5 capped False free_boundary_existential False
equation_n 12 input_prefixes 540304 admissible 74072 extensions_seen 1122552 stored_extensions 1122552 max_free_bits 5 capped False free_boundary_existential False
equation_n 13 input_prefixes 1122552 admissible 138760 extensions_seen 2000001 stored_extensions 2000000 max_free_bits 5 capped True free_boundary_existential False
BACKEND_AGREEMENT exact_stage_records 11
```

## Interpretation

The uncapped lines are exhaustive for their finite prefix levels.  The final
line is intentionally partial: it records a cap stop, not all equation-13
extensions.  A nonempty finite prefix is compatible only with the tested
finite equations and says nothing about an infinite fixed point of `R^8`.
Accordingly, this computation leaves period eight `OPEN` and does not change
139's T0/T1/T2 or Route labels.
