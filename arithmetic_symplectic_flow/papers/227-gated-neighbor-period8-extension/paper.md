# Gated-neighbor period-8 finite extension

**Paper ID:** 227-gated-neighbor-period8-extension  
**Candidate:** `ANG-20260918-GNS02`  
**Date / status:** 2026-09-18; FINITE TEST COMPLETE — CAP HIT, PERIOD 8 OPEN.  
**Parent object:** `ANG-20260914-GNS01` (139), unchanged.

## Abstract

We reran the exact period-eight temporal-prefix test for candidate 139 under a
new, separately frozen storage cap of 2,000,000 extensions.  The full Boolean
constraint is evaluated with integer/Boolean operations only over the configured
coordinates 2 through 16, with an existential higher boundary.  The cap stops
the run at equation 13 before coordinates 14--16 are reached.  A chunked NumPy CPU path
and a chunked PyTorch CUDA path agree on all eleven reported stage records.
Equations 3 through 12 complete without a cap and leave nonzero prefixes;
equation 13 reaches the declared cap after 2,000,000 stored prefixes, with
the 2,000,001st extension used only as the stop event.  Thus this extension
does not decide existence or nonexistence of an infinite period-eight state.

## 1. Object and finite question

The map, divisor source `G`, gated feedback `L`, full product carrier, unit
roof, and temporal equation are exactly those frozen in [139](../139-gated-neighbor-sieve/paper.md).
This package changes no rule or boundary convention.  It only versions a
larger finite evidence cap and two exact implementations.  A temporal word
is an 8-bit integer, and each spatial extension tests

\[
 A_n=u_{n-1}+u_n,\qquad E_n=D u_n+G(u)_n,
\]

with the bitwise solvability condition `E_n & (255 xor A_n)=0`; forced bits
are fixed and the remaining bits are enumerated in the same descending
submask order as the parent 139 computation.
The coordinates 2--16 are the only tested columns, and no value at a higher
coordinate is inserted.

## 2. Exact finite result

The four coordinate-2 words are `[51, 102, 153, 204]`; the initial
2--3 prefix count is 1024.  The complete uncapped prefix counts are:

| Equation | Input | Admissible | Extensions / stored | Max free bits |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 1024 | 192 | 2052 | 8 |
| 4 | 2052 | 216 | 2340 | 5 |
| 5 | 2340 | 336 | 5356 | 5 |
| 6 | 5356 | 796 | 11892 | 5 |
| 7 | 11892 | 1996 | 28000 | 5 |
| 8 | 28000 | 4928 | 69664 | 5 |
| 9 | 69664 | 10280 | 198064 | 8 |
| 10 | 198064 | 34416 | 501520 | 8 |
| 11 | 501520 | 49384 | 540304 | 5 |
| 12 | 540304 | 74072 | 1122552 | 5 |

At equation 13, 1,122,552 input prefixes are available.  The run processes
138,760 admissible inputs before the first extension beyond the cap, stores
2,000,000 prefixes, reports `extensions_seen=2,000,001`, and stops.  This is
an exact bounded computation, not an emptiness certificate.

## 3. Backend and safety checks

The NumPy CPU and PyTorch CUDA implementations use unsigned 8-bit words,
fixed row-major submask order, chunk size 8192, and identical cap semantics.
CUDA is guarded at 1 GiB of reported free memory per chunk.  The recorded
device is an NVIDIA GeForce RTX 4080 SUPER (32,760 MiB), with PyTorch 2.8.0
and CUDA 12.8.  The two paths agree on all stage records; no tolerance,
randomness, prime table, or external solver is involved.

## 4. Claim boundary and decision

The nonzero finite survivors through equation 13 do not prove an infinite
periodic state, and the cap does not prove its absence.  Periods 12 and above,
Boolean-rule variants, a new roof, and any operator/Route claim were not run.
The same-object ledger is preserved, while 139's period-eight status remains
`OPEN`.  Decision: **bounded extension complete; stop/fork rather than infer
an orbit from open finite prefixes**.  See the [claim ledger](claim-ledger.md)
and [exact computation record](evidence/computation.md).
