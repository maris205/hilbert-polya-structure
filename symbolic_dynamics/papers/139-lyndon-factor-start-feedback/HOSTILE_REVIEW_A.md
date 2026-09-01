# Independent hostile review A — P139 Round 0

**Review date:** 2026-09-01 UTC  
**Reviewer posture:** independent internal reviewer; not an author of this manuscript  
**Scope:** frozen contract check, theorem reconstruction, adversarial spot enumeration, verifier replay, isolated build, P134 firewall, and `main_round0_original.pdf` artifact audit  
**Disposition:** **PASS**  
**External status:** **HOLD_EXTERNAL**

No manuscript, bibliography, verifier, frozen PDF, or build artifact was edited
during this review. The only paper-local output is this file.

## 1. Severity-indexed findings

### Critical

**C-A-01 — suffix-record characterization and leading-one stripping: PASS.**
The manuscript’s core static reduction reconstructs cleanly. In a nonincreasing
Chen--Fox--Lyndon factorization `w=u_1...u_k`, the suffixes beginning at factor
starts form a strict descending chain from left to right. If a position lies
strictly inside a factor `u_h`, then the suffix beginning there is larger than
the factor-start suffix because a Lyndon word is strictly smaller than each of
its nonempty proper suffixes. This gives the exact equivalence:

```text
factor starts = left-to-right strict new minima among suffixes.
```

The proper-prefix convention is essential and is handled correctly: it resolves
equal-factor cases such as `00 = 0|0` and repeated `01` blocks in the
alternating witness.

The leading-one rule also reconstructs literally. If `w=1^r0s`, every leading
`1` is forced to be a singleton Lyndon factor, so

```text
L_n(w) = 1^r L_(n-r)(0s).
```

Therefore every nonfixed update strictly increases the leading-one prefix. The
only fixed point, and hence the only recurrent state, is `1^n`.

**C-A-02 — sharp depth `n` and unique deepest source: PASS.**
For the alternating word `a_n=0101...`, the CFL factorization is `(01)^m` when
`n=2m` and `(01)^m0` when `n=2m+1`, so

```text
L_n(a_n) = 1 a_(n-1).
```

Since prefixing by `1` preserves depth under iteration, this gives
`depth(a_n)=1+depth(a_(n-1))=n`. The upper bound `depth<=n` follows from the
leading-one amplifier, so the clock is sharp.

The uniqueness proof also survives hostile reconstruction. If a word has depth
`n`, then its image has depth `n-1` and must equal the forced mask

```text
1 a_(n-1).
```

That mask prescribes factor lengths `(2,2,...,2)` for even `n` and
`(2,2,...,2,1)` for odd `n`. The only binary Lyndon word of length `2` is
`01`, and in the odd case the last singleton cannot be `1` because the
required nonincrease would read `01 >= 1`, which is false. Hence the unique
depth-`n` source is exactly `a_n`.

**C-A-03 — ordered-Lyndon fibre theorem, matrix formula, and special cells: PASS.**
If a target mask starts with `0`, its fibre is empty because every CFL
factorization has a first factor start. If `y_1=1`, its one-positions prescribe
a composition `(\ell_1,...,\ell_k)`, and every preimage corresponds bijectively
to a nonincreasing chain of binary Lyndon words of those lengths. Concatenation
and CFL uniqueness give the inverse map, so the fibre formula is exact.

The matrix form is dimensionally correct:

```text
M_(a,b) has size |L_a| x |L_b|,
1_(ell_1)^T M_(ell_1,ell_2) ... M_(ell_(k-1),ell_k) 1_(ell_k)
```

is a scalar, and its expansion counts exactly the adjacent lex inequalities.

The two special cells also check out:

- `|L_n^(-1)(10^(n-1))|` is the classical binary Lyndon census;
- `|L_n^(-1)(1^n)| = n+1` from the `n+1` nonincreasing one-letter chains
  `1^j 0^(n-j)`.

The `n=1` boundary is consistent: both displayed special-fibre formulas reduce
to `2`.

The hostile target `10110`, whose composition is `(2,1,2)`, is a clean
outside-image witness even though it starts with `1`. Both length-2 factors are
forced to be `01`, but there is no length-1 Lyndon word lying between `01` and
`01` in the order `u_1>=u_2>=u_3`. So the ordered-chain set and the matrix
product both vanish. This is the correct obstruction: not absent positive
Lyndon lengths, but impossible lex comparisons.

### Major

**M-A-01 — independent spot enumeration and equality-factor attacks: PASS.**
A separate brute-force program, written during this review and not importing the
paper-local verifier, checked two independent routes.

First, I enumerated all nonincreasing tuples of binary Lyndon words through
`n=8`. Each binary word occurred in exactly one such tuple, and the resulting
factor-start mask agreed with the strict suffix-record mask for every word.
Second, a separate ordered-chain counter matched literal fibre counts for every
target through `n=10`.

These checks specifically attacked:

- equal-factor cases such as `00` and `(01)(01)`;
- the proper-prefix lex convention;
- the `n=1` coincidence of the two special cells;
- target masks that begin with `1` but are still outside the image;
- the claimed unique deepest source.

No counterexample was found.

**M-A-02 — owner subtraction and P134 firewall: PASS.**
The credited background is properly bounded. Chen--Fox--Lyndon own the static
factorization theorem, Duval owns linear factorization/least-suffix machinery,
Franek--Islam--Rahman--Smyth and Badkobeh--Crochemore own Lyndon-array/tree
infrastructure, and the Möbius necklace formula owns the one-factor census.
What remains here is the iterated factor-start mask, its sharp unique clock,
and the complete ordered-Lyndon inverse atlas.

The internal firewall against P134 is adequate. P134 iterates integer border
arrays, has many exact two-cycles, and proves a mismatch-amplifier/factorial-
fibre package. P139 iterates binary factor-start masks, has one fixed recurrent
state `1^n`, and its inverse theorem is a lex-ordered Lyndon-chain census. The
two papers share string-theoretic background language, not the same dynamical
system or the same theorem.

### Minor

**N-A-01 — verifier replay, isolated build, PDF audit, and anonymity: PASS.**
The current package and frozen outputs are mechanically consistent.

```text
main.tex                7beded0c58ebfe439119a8c47c2e63119933b6bb4a7b3f75d2328146dbd8ffc5
references.bib          d6dfee797e92c74d431c06df9c7ecf7199e7cc8c8684b80980ccce52d75a4c9e
code/verify.py          01d10e3ffde5cfe675665e0cdfb1d2fc5e411c864ef83a82e93ca3d7d23e6b75
verification_output.txt 801b82a729adff63f35dc92306ad1044444d2cd0fc89b603306064fd7f6ec0fe
main.pdf                3d41d36820b33b2b4f9215dd55d8b9d620d7c39ae0f65c5512426c8d7b79acf0
main_round0_original.pdf
                        3d41d36820b33b2b4f9215dd55d8b9d620d7c39ae0f65c5512426c8d7b79acf0
```

Specific checks:

- a fresh verifier replay reproduced `code/verification_output.txt` byte for
  byte (`cmp=0`) and ended with `EXACT_ASSERTIONS=2654300` and `STATUS=PASS`;
- a fresh isolated four-stage build from only `main.tex` and `references.bib`
  exited zero and produced a PDF byte-identical to both `main.pdf` and
  `main_round0_original.pdf`;
- warning scans found no LaTeX warnings, bad boxes, undefined references,
  undefined citations, duplicate labels, or rerun requests;
- `pdfinfo` reports 4 A4 pages, no encryption, forms, JavaScript, or metadata
  stream, with blank title/author/subject/keywords metadata;
- `pdffonts` reports 25 font rows, all embedded, subsetted, and Unicode-mapped;
- all 4 pages were rasterized and visually inspected; I found no clipping,
  collision, truncation, overflow, or anonymity leak;
- `strings` scans found only the empty metadata fields plus the producer line,
  and no local path, username, or machine identifier.

## 2. Final gate

There are **zero critical REPAIR items, zero major REPAIR items, and zero
minor REPAIR items**. The theorem package, verifier replay, isolated build,
and frozen PDF all survive this independent Round-0 hostile review.

This is not an external novelty or priority clearance. The paper remains
**HOLD_EXTERNAL**.
