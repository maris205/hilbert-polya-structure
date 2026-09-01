# Independent hostile review A — P138 Round 0

**Review date:** 2026-09-01 UTC  
**Reviewer posture:** independent internal reviewer; not an author of this manuscript  
**Scope:** frozen contract check, theorem reconstruction, adversarial spot enumeration, verifier replay, isolated build, P134 firewall, and `main_round0_original.pdf` artifact audit  
**Disposition:** **PASS**  
**External status:** **HOLD_EXTERNAL**

No manuscript, bibliography, verifier, frozen PDF, or build artifact was edited
during this review. The only paper-local output is this file.

## 1. Severity-indexed findings

### Critical

**C-A-01 — complement quotient, reset/amplifier, and sole recurrent class: PASS.**
Complement preserves every coordinate equality, so the palindromic-prefix
indicator vector is complement-invariant. Writing `y_i=x_i xor x_1` gives the
exact normalized quotient

```text
Q_n(y)_i = y_i xor 1 xor 1{y_1...y_i is a palindrome},
```

with `y_1=0` and `Q_n(y)_1=0`. From this literal rule:

- one update always zeros the first `min(3,n)` normalized coordinates;
- if `y` begins with `0^k` and `k<n`, then `Q_n(y)` begins with `0^(k+1)`.

Hence the quotient dynamics has the unique recurrent state `0^n`. In the
original system the first bit flips on every step because the length-one prefix
is always palindromic, so the unique recurrent class upstairs is exactly the
strict two-cycle

```text
0^n <-> 1^n.
```

The boundary cases are consistent: for `n=1` both states are already on that
two-cycle, and for `n=2` the only nonrecurrent states are the two nonconstant
words.

**C-A-02 — exact clock, witness, and full palindrome-prefix characterization: PASS.**
The upper bound is forced by the amplifier: once the quotient is nonzero, the
leading-zero run strictly increases until it reaches length `n`. This yields
maximum depth `0` at `n=1`, `1` at `n=2`, and at most `n-2` for `n>=3`.

For sharpness, the manuscript’s witness

```text
u_i = 1 exactly when i == 3 mod 4
```

was reconstructed independently. Its palindromic prefixes are exactly of
lengths `1`, `2`, and all lengths `i>=5` with `i == 1 mod 4`. Therefore
`Q_n(u)` is `0001010...`, and for

```text
v_k = prefix_n(0^k 1010...)
```

one has `Q_n(v_k)=v_(k+1)` for `3<=k<n`. So the orbit is

```text
u -> v_3 -> v_4 -> ... -> v_n = 0^n,
```

with exactly `n-2` arrows and no earlier hit. I found no hidden shorter route,
including at the small boundaries `n=3,4,5`.

**C-A-03 — every-target decoder, no phase multiplicity, and target-outside-image cases: PASS.**
For a normalized target `z` and a constructed source prefix
`y_1...y_(i-1)` with `y_1=0`, the full prefix `y_1...y_i` is palindromic iff
`y_i=0` and the middle word `y_2...y_(i-1)` is palindromic. This gives the
exact left-to-right decoder:

- if the middle word is nonpalindromic, then `y_i=1-z_i` is forced;
- if the middle word is palindromic, then `z_i=0` is necessary and both
  `y_i=0,1` are allowed.

Induction on `i` shows that the surviving branches are exactly the normalized
one-step fibre. The original phase contributes no extra multiplicity because
`t_1 = x_1 xor 1` forces `x_1` uniquely.

The edge cases also check out:

- `n=1`: every target has exactly one preimage;
- `n=2`: only the constant targets appear, each with exactly two preimages;
- nontrivial outside-image targets exist even after the forced three-zero
  normalized prefix, e.g. `0001101` and its complement `1110010`, so the image
  criterion is genuinely target-wise and not merely the reset condition.

### Major

**M-A-01 — independent spot enumeration and sharpness attacks: PASS.**
A separate brute-force script, written during this review and not importing the
paper-local verifier, checked:

- full orbit structure and maximum depth through `n=10`;
- the witness chain `u -> v_3 -> ... -> 0^n` through `n=10`;
- the target decoder against literal fibres through `n=8`.

These checks reproduced the theorem package exactly: no recurrent state beyond
`0^n,1^n`, no source deeper than `n-2`, and no decoder mismatch. Deliberately
awkward targets such as `01`, `10`, `00100`, `11101`, and `0001101` behaved
exactly as the manuscript predicts.

**M-A-02 — owner subtraction and P134 firewall: PASS.**
The credited background is correctly subtracted. Galil, Rubinchik--Shur,
Harju--Huova--Zamboni, and Bathie--Ellert--Starikovskaya own static palindrome
recognition, storage, generation, and prefix encoding. What remains here is
not a new palindrome-recognition algorithm, but the repeated XOR feedback of
the complete palindromic-prefix indicator vector and the dynamical theorems
proved for that literal map.

The internal firewall against P134 is also adequate. P134 iterates whole border
arrays on an integer carrier, has `n-1` explicit two-cycles, a `2n-4` clock,
and factorial extremal fibres. P138 is a binary XOR system whose quotient has a
single amplifier into one fixed state, whose original dynamics has one strict
two-cycle, and whose inverse theorem is a target-wise palindrome decoder. The
shared prefix/border vocabulary is background only and does not collapse the
two theorem packages into the same claim.

### Minor

**N-A-01 — verifier replay, isolated build, PDF audit, and anonymity: PASS.**
The current package and frozen outputs are mechanically consistent.

```text
main.tex                e988fca92663c88d1d1f69498cfb54c57dbf4191a19f0c463d3e4558e706787b
references.bib          31353177649c793808e270070179b8de5016b0ca4b898f77bdc75ea0d42e3f57
code/verify.py          f7a12fdd55f0e7b5ca70f2df0089484282f2180d920ce0ea648683eb044c6443
verification_output.txt 551a61f69ba5bb09355bc99c95401bb89ee58ab5c732b81eaa24c6a016330675
main.pdf                6c2114456c77df71516e4d9b2573907a1633cedeb9e77890c3cdcca318828942
main_round0_original.pdf
                        6c2114456c77df71516e4d9b2573907a1633cedeb9e77890c3cdcca318828942
```

Specific checks:

- a fresh verifier replay reproduced `code/verification_output.txt` byte for
  byte (`cmp=0`) and ended with `EXACT_ASSERTIONS=3870590` and `STATUS=PASS`;
- a fresh isolated four-stage build from only `main.tex` and `references.bib`
  exited zero and produced a PDF byte-identical to both `main.pdf` and
  `main_round0_original.pdf`;
- warning scans found no LaTeX warnings, bad boxes, undefined references,
  undefined citations, duplicate labels, or rerun requests;
- `pdfinfo` reports 3 A4 pages, no encryption, forms, JavaScript, or metadata
  stream, with blank title/author/subject/keywords metadata;
- `pdffonts` reports 21 font rows, all embedded, subsetted, and Unicode-mapped;
- all 3 pages were rasterized and visually inspected; I found no clipping,
  collision, truncation, overflow, or anonymity leak;
- `strings` scans found only the empty metadata fields plus the producer line,
  and no local path, username, or machine identifier.

## 2. Final gate

There are **zero critical REPAIR items, zero major REPAIR items, and zero
minor REPAIR items**. The theorem package, verifier replay, isolated build,
and frozen PDF all survive this independent Round-0 hostile review.

This is not an external novelty or priority clearance. The paper remains
**HOLD_EXTERNAL**.
