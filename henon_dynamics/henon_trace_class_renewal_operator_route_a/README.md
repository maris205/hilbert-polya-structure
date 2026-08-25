# HCS-C142: trace-class renewal operator

This package proves that a frozen countable renewal graph owns a genuine
infinite-rank trace-class operator with exact Fredholm determinant

```text
1-sum_{m>=1}2^{-m(m+1)/2}z^m.
```

It also proves that a closely matched constant-advance renewal control is
noncompact, despite its rational formal renewal expression.

## Entry points

- `THEOREM_PACKAGE.md` — complete derivation and proofs;
- `results/c142_renewal_evidence.json` — canonical exact receipt;
- `code/` — producer, independent checker, SymPy reconstruction, replay,
  mutations, and manifest builder;
- `paper/main.pdf` — final paper.

## Boundary

Strict tuple:
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`.

The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is not authorized.
