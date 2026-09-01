# Independent hostile review B — P138 Round 1

**Review date:** 2026-09-01 UTC  
**Reviewer posture:** second independent internal reviewer; separate from the author and review A  
**Scope:** frozen P137–P141 theorem contract check, full package read, adversarial reconstruction of the mod-4 sharp witness and decoder phase, canonical verifier replay, independent spot controls, isolated build, P134 collision audit, and `main_round1.pdf` page/font/metadata/anonymity audit  
**Disposition:** **PASS**  
**External status:** **HOLD_EXTERNAL**

No manuscript, bibliography, verifier, frozen PDF, or build artifact was edited
during this review. The only paper-local output is this file.

## 1. Severity-indexed findings

### Critical

**C-B-01 — complement quotient, unique recurrent class, and the sharp mod-4 witness: PASS.**
I re-derived the quotient map directly from

```text
T_n(x)_i = x_i xor 1{x_1...x_i is a palindrome}
```

and the normalization `N(x)_i=x_i xor x_1`. Because complement and
normalization preserve every equality test inside a prefix, the induced rule is

```text
Q_n(y)_i = y_i xor 1 xor 1{y_1...y_i is a palindrome},  y_1=0.
```

From this literal rule, one step always zeros the first `min(3,n)` normalized
coordinates, and any nonzero normalized state with leading zero run `0^k`
acquires at least `0^(k+1)` at the next step. Hence the quotient has the
single recurrent state `0^n`, while the original system has exactly the strict
two-cycle `0^n <-> 1^n`.

I then attacked the manuscript's sharp witness

```text
u_i = 1 exactly when i == 3 mod 4.
```

The vulnerable point is the claimed characterization of its palindromic
prefixes. Reconstructing it from scratch, the one-positions in a prefix of
length `i` are `3,7,11,...`, and reflection sends `3+4j` to `i-2-4j`. This
preserves the one-set exactly when `i == 1 mod 4`; lengths `3,4,6,7,8,...`
fail immediately because the reflection of position `3` is not itself a
`3 mod 4` position. Thus the palindromic prefixes are exactly lengths `1`, `2`,
and the lengths `i>=5` with `i == 1 mod 4`.

Substituting those indicators into `Q_n` gives `Q_n(u)=v_3`, where
`v_k = prefix_n(0^k1010...)`. For `k>=3`, every prefix of `v_k` longer than `k`
would have to end in `0^k`; if its length is `< 2k`, those last `k` positions
already contain the forced one at `k+1`, and if its length is `>= 2k`, the last
`k` positions lie inside an alternating tail and again contain a one. So no
longer prefix is palindromic, `Q_n` simply complements the tail, and
`Q_n(v_k)=v_(k+1)`. The chain

```text
u -> v_3 -> v_4 -> ... -> v_n = 0^n
```

therefore has exactly `n-2` arrows. I found no boundary failure at
`n=3,4,5`, no hidden earlier hit, and no alternative recurrent quotient state.

**C-B-02 — every-target decoder and phase recovery: PASS.**
I independently reconstructed the decoder rather than trusting the table in the
paper. For a normalized source prefix `y_1...y_i` with `y_1=0`, the full prefix
is palindromic iff `y_i=0` and the middle word `m=y_2...y_(i-1)` is
palindromic. This yields exactly three cases:

- if `m` is nonpalindromic, then the indicator is zero regardless of `y_i`, so
  `Q_n(y)_i=z_i` forces `y_i=1-z_i`;
- if `m` is palindromic and `z_i=0`, both `y_i=0` and `y_i=1` are allowed;
- if `m` is palindromic and `z_i=1`, no branch exists.

Because the `i`th quotient output depends only on the first `i` source bits,
induction on `i` shows that the surviving branches are exactly the normalized
fibre over `z=N(t)`. The decoder is therefore both an exact counting recursion
and the complete image criterion.

The reviewer-specific attack point was the manuscript's claim that the original
phase contributes no extra multiplicity. That claim survives: `t_1=x_1 xor 1`
forces `x_1=1-t_1`, and every normalized branch lifts to the unique original
source `x_i=y_i xor (1-t_1)`. I exhaustively checked that phase lift against
literal preimages for every target through `n<=10`; there was no double count,
missed source, or target outside the image that incorrectly lifted.

### Major

**M-B-01 — independent controls and canonical verifier replay: PASS.**
I used two independent checks that did not import the paper-local verifier.

- A standalone literal-word script verified the mod-4 palindrome-prefix
  characterization and the exact witness chain through `n<=20`.
- A separate standalone fibre script checked the decoder against literal
  one-step fibres for every target through `n<=10`, including the original
  phase lift.

Both checks passed exactly.

I also replayed the canonical verifier:

```text
python3 code/verify.py > /tmp/p138_verify_roundB.txt
cmp -s /tmp/p138_verify_roundB.txt code/verification_output.txt
```

The replay reproduced the frozen transcript byte for byte and ended with
`TOTAL_EXHAUSTIVE_STATES=524286`, `EXACT_ASSERTIONS=3870590`, and `STATUS=PASS`.

**M-B-02 — owner subtraction and P134 collision firewall: PASS.**
The credit boundary remains correctly stated. Classical palindrome
recognition/data-structure work and generic border machinery are background
only. The residual claim is the repeated palindromic-prefix indicator vector
fed back by XOR, its quotient amplifier, the sharp `n-2` witness, and the
target-wise inverse decoder.

I re-checked the internal P134 boundary directly against `papers/134-*` as well
as the batch firewall. P134 studies whole-array recomputation of integer border
arrays on the carrier `E_n`, has `n-1` explicit period-two cycles, a
`2n-4` mismatch amplifier, and factorial extremal fibres. P138 is a binary
length-preserving XOR map whose quotient has one absorbing fixed state and whose
original dynamics has exactly one strict two-cycle. The inverse theorem is a
palindrome-prefix branch decoder, not a border-array validity/factorial-fibre
atlas. The overlap is vocabulary, not mechanism.

### Minor

**N-B-01 — isolated build, Round-1 PDF equality, and anonymity audit: PASS.**
The artifact package is mechanically stable.

```text
main.tex                e988fca92663c88d1d1f69498cfb54c57dbf4191a19f0c463d3e4558e706787b
references.bib          31353177649c793808e270070179b8de5016b0ca4b898f77bdc75ea0d42e3f57
code/verify.py          f7a12fdd55f0e7b5ca70f2df0089484282f2180d920ce0ea648683eb044c6443
verification_output.txt 551a61f69ba5bb09355bc99c95401bb89ee58ab5c732b81eaa24c6a016330675
main.pdf                6c2114456c77df71516e4d9b2573907a1633cedeb9e77890c3cdcca318828942
main_round0_original.pdf
                        6c2114456c77df71516e4d9b2573907a1633cedeb9e77890c3cdcca318828942
main_round1.pdf         6c2114456c77df71516e4d9b2573907a1633cedeb9e77890c3cdcca318828942
```

Specific checks:

- a clean-room four-stage build from only `main.tex` and `references.bib`
  (`pdflatex -> bibtex -> pdflatex -> pdflatex`) exited zero and produced a
  PDF byte-identical to `main.pdf`, `main_round0_original.pdf`, and
  `main_round1.pdf`;
- the first two LaTeX passes showed the expected transient unresolved-citation
  and rerun notices, while the settled final pass showed no warning,
  undefined-reference, undefined-citation, bad-box, or multiply-defined-label
  output;
- `pdfinfo` on the isolated build reports 3 A4 pages, no encryption, forms,
  JavaScript, custom metadata, or metadata stream; title/author/subject/
  keywords are blank and the creator/producer lines are generic LaTeX/pdfTeX;
- `pdffonts` reports 21 font rows, all embedded, subsetted, and Unicode-mapped;
- extracted-text scans found no `??`, `[?]`, `TODO`, `FIXME`, local path,
  username, email address, or affiliation leak;
- all 3 rendered pages of `main_round1.pdf` were visually inspected; I found
  no clipping, collision, overflow, malformed display, broken bibliography, or
  anonymity failure beyond the intended `Anonymous` author line.

## 2. Final gate

There are **zero critical REPAIR items, zero major REPAIR items, and zero
minor REPAIR items**. The theorem package, targeted mod-4 witness attack,
decoder-phase attack, verifier replay, isolated build, and Round-1 PDF audit
all survive this independent Round-B hostile review.

This is not an external novelty or priority clearance. The paper remains
**HOLD_EXTERNAL**.
