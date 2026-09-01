# Independent hostile review B - P140 Round 1 freeze

**Review date:** 2026-09-01 UTC  
**Reviewer role:** independent hostile reviewer; the reviewer did not author the manuscript  
**Scope:** frozen-contract alignment, Round-A closure audit of `M-A-01`, independent theorem reconstruction, independent exact controls, canonical verifier byte replay, isolated rebuild, source/owner/collision audit, and all-page/font/metadata/anonymity audit  
**Round-A delta:** `main.pdf` and `main_round1.pdf` are byte-identical; `main_round0_original.pdf` is different because it preserves the pre-repair scope statement  
**Disposition:** **PASS** at the internal theorem/artifact gate  
**External status:** **HOLD_EXTERNAL**

No manuscript source, bibliography, verifier, canonical stdout, or PDF artifact
was edited during this review. The only paper-local output of Round B is this
file.

## 1. Severity-indexed findings

### Critical

**C-B-01 - `M-A-01` closure is real and does not create a new scope clash:
PASS.** The repaired source now states the length-one boundary in the theorem
itself (`main.tex:237-246`), then isolates the degenerate clock before the
nondegenerate corollary (`main.tex:262-266`), and restricts the Beta identity
to `n=2m+1>=3`, `m>=1` (`main.tex:268-287`). The Gamma limit is explicitly
along odd lengths as `m -> infinity` (`main.tex:304-323`). Reattacking the
boundary from the empty history gives exactly the repaired statement: at `n=1`
there are no active windows, both embedded vectors are empty, `tau_1=0` almost
surely, the empty product in the Laplace formula is `1`, and the empty sums in
the mean/variance formulas are `0`. `pdftotext` on `main_round1.pdf` shows the
scoped corollary and no printed `Beta(1/2,0)` law. I found no new
inconsistency between Theorem 4.1, Corollary 4.2, Theorem 4.3, the abstract,
the paper ledger files, or the Round-A closure note.

**C-B-02 - two-run kernel, endpoint/history laws, and marked crossing law
survive independent hostile reconstruction: PASS.** Re-deriving the literal
update on `0^a1^b` again yields exactly the three successor classes in
`main.tex:83-104`, with the common complete-history denominator `(n-2)!!` from
the deterministic window counts `n-2,n-4,...,1` (`main.tex:138-141`). The
cross-count recurrence, support, and exactly-one-cross law in
`main.tex:153-227` also remain coherent on the sharp boundaries `a=1`, `b=1`,
`a=0`, and `b=0`: a terminal-one history must satisfy
`1<=C<=min(a,b-1)` and `C congruent a mod 2` when `b>=2`, while
`H^1_{a,1}=0` and `H^1_{0,b}=(b-2)!!` on the reachable odd one-run boundary.
An independently written script that did not import `code/verify.py` checked
818 exact conditions, including literal history enumeration for every two-run
input of odd length at most `13`; it reproduced the endpoint law, history
counts, support sets, and the `Pr(final 1, C=1)=1/a` atom with no
counterexample.

**C-B-03 - whole-history clock separation, Beta moments, and the
continuous/discrete firewall survive reattack: PASS.** The proof in
`main.tex:231-323` keeps the deterministic discrete contraction count
`(n-1)/2` separate from the random elapsed time `tau_n`. Reconstructing the
continuous-time law from equal-rate races again gives an `Exp(ell-2)` holding
time at current length `ell`, independent of the winning window index, so
strong Markov memorylessness separates the entire holding-time vector from the
entire embedded history, not merely from the endpoint. The same independent
script checked the joint Laplace factorization on every odd binary word of
length at most `9`, the two-run clock factorization on every odd two-run input
of length at most `13`, and the `e^{-2 tau_n}` moment identity against the
`Beta(1/2,m)` moment formula for `1<=m<=8`, `0<=q<=5`. No counterexample to
the nondegenerate Beta law or the centered Gamma-limit statement appeared.

### Major

**M-B-01 - canonical verifier byte replay: PASS.** A fresh replay of
`PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py` compared byte for byte with
`code/verification_output.txt` (`cmp=0`). The replay exited zero and the frozen
transcript still reports `exact_assertions=190740` and `status=PASS`. The
Round-A scope repair did not silently alter the executable control record.

**M-B-02 - isolated rebuild and frozen-byte identity: PASS.** A fresh
four-stage isolated build from only `main.tex` and `references.bib` in a
temporary directory exited zero on all stages and reproduced the current PDF
byte for byte. The current artifact hashes are:

| artifact | SHA-256 |
|---|---|
| `main.tex` | `1e10db2a0bedadc9c35df6265867264813bf165298b83c16cc60434dcb158473` |
| `references.bib` | `ac64e59d8708acc0c757a7a2f6c49420c983a886dc3bf6672c70d1cae99b27a7` |
| `code/verify.py` | `3b66cd33bca07d3ea7ac2739eb226adb3b50204755596c561aa2885cd282a331` |
| `code/verification_output.txt` | `c23afcaf89ee9bf9ac5c2cd43ee72d6599155b9930215bf0dba0b4c328087ec8` |
| `main.pdf` | `a04683cd14c2ac0ecea73ae6baf98f17ef1a0c947ba712f25529b0087d839c18` |
| `main_round1.pdf` | `a04683cd14c2ac0ecea73ae6baf98f17ef1a0c947ba712f25529b0087d839c18` |
| `main_round0_original.pdf` | `2b151d0916d8d43d26988f3f70a25885fdf8e71255657dc1486bc300e070aa99` |

So Round B is auditing the repaired Round-1 bytes, not the preserved Round-0
freeze.

**M-B-03 - source ownership and collision firewall: PASS.** The current
manuscript still gives Krapivsky--Redner and Goles et al. ownership of
fixed-carrier majority background (`main.tex:61-66`) and keeps the residual at
the shrinking two-run kernel, marked crossing law, and exact clock package
(`main.tex:352-357`). The batch owner audit explicitly clears P140 for
continued internal drafting while keeping `HOLD_EXTERNAL` and treating the
source search only as a bounded non-hit
(`docs/papers137_141_sequence/phase1/FINAL_OWNER_AUDIT.md:191-220`). I also
found no local collision with the nearby majority or stochastic-contraction
papers identified there; the carrier, update rule, and claimed laws remain
distinct.

### Minor

**N-B-01 - page, font, metadata, and anonymity audit: PASS.** `pdfinfo` on
`main_round1.pdf` reports four A4 pages, PDF 1.5, no encryption, no forms, and
no JavaScript. `Title`, `Author`, `Subject`, and `Keywords` metadata are
blank. `pdffonts` lists 22 rows, all embedded and subsetted. A raw `strings`
scan found no local path, workspace name, hostname, or machine identifier. All
four pages were rasterized at 150 dpi and visually inspected; the boundary
paragraph, Corollary 4.2 scope, Gamma-limit statement, table, and references
are legible, the only visible author string is `Anonymous`, and no clipping,
overlap, or anonymity leak appeared.

## 2. Final gate

There are **zero critical REPAIR items, zero major REPAIR items, and zero minor
REPAIR items**. The repaired Round-1 P140 package passes this independent
hostile review B. The external gate does not change: novelty, priority,
authorship, posting, specialist contact, and submission remain
**HOLD_EXTERNAL**.
