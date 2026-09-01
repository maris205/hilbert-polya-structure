# Independent hostile review B — P139 Round 1

**Review date:** 2026-09-01 UTC  
**Reviewer posture:** second independent internal reviewer; separate from the author and review A  
**Scope:** frozen P137–P141 theorem contract check, full package read, adversarial reconstruction of the ordered-tail comparison with equal/prefix-related Lyndon factors and of the unique-depth proof from the forced mask, canonical verifier replay, independent spot controls, isolated build, P134 collision audit, and `main_round1.pdf` page/font/metadata/anonymity audit  
**Disposition:** **PASS**  
**External status:** **HOLD_EXTERNAL**

No manuscript, bibliography, verifier, frozen PDF, or build artifact was edited
during this review. The only paper-local output is this file.

## 1. Severity-indexed findings

### Critical

**C-B-01 — suffix-record characterization and ordered-tail descent under equal/prefix-related factors: PASS.**
I re-derived the static comparison lemma from the CFL factorization itself
rather than relying on the paper's prose. If

```text
w = u_1 ... u_k,   u_1 >= ... >= u_k
```

is the nonincreasing Lyndon factorization and `S_h = u_h ... u_k`, then for
adjacent tails one can write

```text
S_(h+1) = u^m z,   S_h = u^(m+1) z,
```

where `u=u_h`, `m>=0`, and either `z` is empty or its first CFL factor is a
Lyndon word `v<u`. If `z` is empty, then `S_(h+1)` is a proper prefix of `S_h`
and is therefore strictly smaller. If `z` is nonempty, then after deleting the
common prefix `u^m` the comparison reduces to `uz > z`, which holds because the
right-hand word begins with a strictly smaller Lyndon factor `v<u`. This is the
only delicate point when factors are equal or when the next factor is
prefix-related to `u`, and it survives the attack.

For a position strictly inside a factor `u_h`, write `v` for the proper suffix
of `u_h` beginning there. Since `u_h` is Lyndon, `u_h < v`. Also `v` cannot be
a prefix of `u_h`, because that would create a border, and `u_h` cannot be a
prefix of `v` because `v` is shorter. Appending the same later factor tail
preserves the strict inequality, so the suffix starting inside a factor is
always larger than the suffix at that factor start. Together these two facts
recover the exact equivalence

```text
factor starts = left-to-right strict new suffix minima.
```

I specifically attacked the equal-factor and proper-prefix boundaries:
`00 = 0|0`, `(01)(01)`, `(01)(0)`, `(001)(01)`, and `(0001)(001)`. No
counterexample appeared; the strict record convention is the correct one.

**C-B-02 — sharp depth `n` and uniqueness from the forced mask: PASS.**
The alternating source `a_n=0101...` is correctly identified as sharp. Its CFL
factorization is `(01)^m` for even `n=2m` and `(01)^m0` for odd `n=2m+1`, so

```text
L_n(a_n) = 1 a_(n-1).
```

Because `L_(m+1)(1v)=1L_m(v)` for every `v`, prefixing by `1` preserves depth
under iteration. Induction therefore gives `depth(a_n)=1+depth(a_(n-1))=n`,
which matches the amplifier upper bound.

The reviewer-specific fragile point was the uniqueness argument after forcing

```text
L_n(w) = 1 a_(n-1).
```

That step survives. The one-positions of the forced mask determine factor
lengths `(2,2,...,2)` when `n` is even and `(2,2,...,2,1)` when `n` is odd.
The only binary Lyndon word of length `2` is `01`. In the odd case the final
singleton cannot be `1`, because the required nonincrease would demand
`01 >= 1`, which is false in lexicographic order with `0<1`. So the last
factor is forced to be `0`, and all earlier factors are forced to be `01`. This
leaves exactly one source:

```text
w = (01)^(n/2)         if n is even,
w = (01)^((n-1)/2) 0   if n is odd.
```

Thus the unique depth-`n` state is indeed `a_n`, with no missing boundary case
at the final factor.

**C-B-03 — ordered-Lyndon inverse atlas and hostile outside-image masks: PASS.**
If a target mask starts with zero, its fibre is empty because every CFL
factorization has a first factor start. If it starts with one, its one-positions
fix a composition `(\ell_1,...,\ell_k)`, and any preimage must be exactly a
nonincreasing chain of binary Lyndon words of those lengths. Concatenation and
CFL uniqueness give the inverse map, so the fibre formula is exact.

The matrix formula is also dimensionally and combinatorially correct:
`M_(a,b)(u,v)=1{u>=v}` counts adjacent lex constraints, and the product

```text
1_(ell_1)^T M_(ell_1,ell_2) ... M_(ell_(k-1),ell_k) 1_(ell_k)
```

expands to one count per admissible ordered chain. I attacked the image
criterion with masks that begin with one but should still fail. The cleanest is
`10110`, whose composition is `(2,1,2)`: both length-2 factors are forced to be
`01`, but there is no one-letter Lyndon word `u_2` satisfying
`01 >= u_2 >= 01`. The fibre and matrix product both vanish, exactly as the
paper claims.

### Major

**M-B-01 — independent spot controls and canonical verifier replay: PASS.**
I used standalone brute-force controls that did not import `code/verify.py`.

- A brute-force CFL search over all words through `n<=9` produced a unique
  nonincreasing Lyndon tuple for each word and matched the strict suffix-record
  mask in every case.
- A standalone ordered-chain counter matched literal target fibres for every
  mask through `n<=9`.
- A targeted exhaustive check over every nonincreasing Lyndon tuple of total
  length `<=10` confirmed the ordered-tail descent
  `S_1 > S_2 > ... > S_k`, including equal-factor and prefix-related cases.

All three controls passed exactly.

I also replayed the canonical verifier:

```text
python3 code/verify.py > /tmp/p139_verify_roundB.txt
cmp -s /tmp/p139_verify_roundB.txt code/verification_output.txt
```

The replay reproduced the frozen transcript byte for byte and ended with
`TOTAL_EXHAUSTIVE_STATES=524286`, `EXACT_ASSERTIONS=2654300`, and `STATUS=PASS`.

**M-B-02 — owner subtraction and P134 collision firewall: PASS.**
The subtraction boundary is still appropriate. Chen–Fox–Lyndon factorization,
Duval's algorithm, Lyndon arrays/forests, the binary Lyndon census, Möbius
necklace inversion, and matrix multiplication are all correctly treated as
background owners. The residual claim is the iterated factor-start mask, its
unique sharp depth witness, and the complete ordered-Lyndon inverse atlas.

I also re-checked the internal P134 boundary directly. P134 iterates integer
border arrays and proves many period-two cycles, a mismatch amplifier, and
factorial fibre extremals on an inversion-sequence carrier. P139 iterates
binary start masks extracted from CFL factorizations, has one fixed recurrent
state `1^n`, and counts preimages by ordered Lyndon chains. The mechanisms,
temporal silhouettes, and inverse statements are different. Shared string
background does not collapse them into the same theorem package.

### Minor

**N-B-01 — isolated build, Round-1 PDF equality, and anonymity audit: PASS.**
The artifact package is mechanically stable.

```text
main.tex                7beded0c58ebfe439119a8c47c2e63119933b6bb4a7b3f75d2328146dbd8ffc5
references.bib          d6dfee797e92c74d431c06df9c7ecf7199e7cc8c8684b80980ccce52d75a4c9e
code/verify.py          01d10e3ffde5cfe675665e0cdfb1d2fc5e411c864ef83a82e93ca3d7d23e6b75
verification_output.txt 801b82a729adff63f35dc92306ad1044444d2cd0fc89b603306064fd7f6ec0fe
main.pdf                3d41d36820b33b2b4f9215dd55d8b9d620d7c39ae0f65c5512426c8d7b79acf0
main_round0_original.pdf
                        3d41d36820b33b2b4f9215dd55d8b9d620d7c39ae0f65c5512426c8d7b79acf0
main_round1.pdf         3d41d36820b33b2b4f9215dd55d8b9d620d7c39ae0f65c5512426c8d7b79acf0
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
- `pdfinfo` on the isolated build reports 4 A4 pages, no encryption, forms,
  JavaScript, custom metadata, or metadata stream; title/author/subject/
  keywords are blank and the creator/producer lines are generic LaTeX/pdfTeX;
- `pdffonts` reports 25 font rows, all embedded, subsetted, and Unicode-mapped;
- extracted-text scans found no `??`, `[?]`, `TODO`, `FIXME`, local path,
  username, email address, or affiliation leak;
- all 4 rendered pages of `main_round1.pdf` were visually inspected; I found
  no clipping, collision, overflow, malformed display, broken bibliography, or
  anonymity failure beyond the intended `Anonymous` author line.

## 2. Final gate

There are **zero critical REPAIR items, zero major REPAIR items, and zero
minor REPAIR items**. The theorem package, ordered-tail attack, forced-mask
uniqueness attack, verifier replay, isolated build, and Round-1 PDF audit all
survive this independent Round-B hostile review.

This is not an external novelty or priority clearance. The paper remains
**HOLD_EXTERNAL**.
