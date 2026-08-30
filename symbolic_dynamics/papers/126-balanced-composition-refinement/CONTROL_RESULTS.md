# P126 exact-control results

Status: **FRESH PASS / CANONICAL BYTE MATCH / HOLD_EXTERNAL**.

Run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

The program uses only Python's standard library, exact integer arithmetic,
deterministic enumeration, and no network or random source.  Fresh stdout is
required to compare byte-for-byte with `code/verification_output.txt`.

```text
balanced composition refinement exact control: PASS
assertions=8756710
literal dynamics: all compositions n<=18
kernel/fibres: all sources and targets n<=15, t<=5
code/suffix decoder: source letters m<=256, t<=8
all-iterate image OGF recurrence: n<=90, t<=8
```

The exhaustive kernel lane records both maps `normal -> image` and
`image -> normal`, thereby checking both directions of the claimed
congruence without a quadratic pair loop.  For every target it compares the
literal fibre with two separately coded predictions: the canonical run
product and the original codeword-factorization DP.

Selected image rows are:

| `t` | `K` | `I_(n,t)` for `n=0..10` |
|---:|---:|---|
| 1 | 2 | `1,1,1,2,4,7,12,21,37,65,114` |
| 2 | 4 | `1,1,1,1,1,2,4,7,11,16,23` |
| 3 | 8 | `1,1,1,1,1,1,1,1,1,2,4` |

Finite agreement does not establish the symbolic theorems, a novelty claim,
or external safety.

## Internal collision firewall

- P094's morphism, marker, and recognizability package is prior internal
  vocabulary; P126 does not claim those general mechanisms.
- P108 already owns the Fibonacci-named clock/fibre silhouette.
- P113 already has an integer-sum carrier, absorption, sharp depth, and
  product-fibre transport.
- P115 already packages every iterate, image, fibre, and a logarithmic
  threshold.
- P122 already combines target-local fibre factorization/DP with image and
  Garden enumeration.
- P123 already centers a refinement engine.
- P125 already packages pointwise fibres, image layers, and functional
  components.
- P110 evolves set partitions of a cyclic group by shift and join; it is not
  a partwise map on integer compositions.
- P117 uses cyclic run compositions only to encode an odd-run reversal on
  binary words; it has no balanced split or iterate-kernel congruence.
- P121 is a stochastic product-plus-one coalescence, with fragmentation/BST
  facts used as controls; its direction and claims are different.
- P101 proves a chronological normal form for random cap/floor interval maps.
  The generic phrase “normal form” receives zero credit.  P126's invariant is
  the literal equality kernel of every balanced-refinement iterate and is
  coupled to its suffix code and fibre product.

The residual after all subtraction is only the all-iterate canonical kernel,
exact one-run fibre product, and temporal image bijection for this literal
infinite-alphabet balanced morphism.

## Gate-input provenance

The pre-paper gate pinned `BALANCED_COMPOSITION_REFINEMENT_REPORT.md`,
`verify_balanced_composition_refinement.py`, and
`BALANCED_COMPOSITION_REFINEMENT_CANONICAL.txt` at SHA-256 values
`fe4796bb730ac51c40e3ce2dd36f898ef13910da6ece50561b6a13eacc9f32b7`,
`fba237ac83d1a6f470f890824406a52b8a6eaa6189d02dca8f31bcfcd12999a2`, and
`c04de425fd715d549cdd2bfec5a4dc3a7eaf2c49719076059f2e9fc78b15c3f1`,
respectively.
Its fresh stdout comparison returned exit `0`.  These hashes record
historical gate inputs, not current paper artifacts.
