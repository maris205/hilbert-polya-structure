# Independent hostile review A — P140 Round 0

**Review date:** 2026-09-01 UTC  
**Reviewer role:** independent; the reviewer did not author the manuscript  
**Scope:** frozen-contract hostile reconstruction, counterexample search,
canonical verifier replay, isolated rebuild, primary-source/owner subtraction,
current-vs-original PDF audit, and anonymity/metadata/font/page checks  
**Disposition:** **REPAIR** before internal pass  
**External status:** **HOLD_EXTERNAL**

No manuscript source, bibliography, verifier, canonical transcript, or PDF was
changed during this review. The only paper-local output of the review is this
file.

## 1. Severity-indexed findings

### Critical

**C-A-01 — two-run kernel, endpoint law, and exact history counts: PASS.**
Reconstructing the literal adjacent-window dynamics on `0^a1^b` gives exactly
three successor types:

```text
(a,b)->(a-2,b)  with multiplicity (a-2)_+,
(a,b)->(a,b-2)  with multiplicity (b-2)_+,
(a,b)->(a-1,b-1) with multiplicity 1_{a>=2}+1_{b>=2}.
```

This matches `main.tex:82-140`. The common complete-history denominator is
`(n-2)!!` because the available window counts are deterministically
`n-2,n-4,...,1`, so history probabilities depend only on length, not on the
embedded path. An independently written literal-history expansion over all
two-run inputs with odd `n<=13` reproduced

```text
#(final 1)=(b-1)(n-4)!!,   #(final 0)=(a-1)(n-4)!!,
Pr(final 1)=(b-1)/(n-2),   Pr(final 0)=(a-1)/(n-2).
```

No tree/history conflation was found: the manuscript explicitly defines a
history as the sequence of current window positions (`main.tex:71-73`).

**C-A-02 — marked support, all `a=1` / `b=1` boundaries, and one-cross law:
PASS.** The marked recurrence in `main.tex:152-226` is the literal
endpoint-marked history recurrence. The boundary behavior is correct:

- `H^1_{0,b}(u)=(b-2)!!` on the reachable odd one-run boundary.
- `H^1_{a,0}(u)=0`.
- If `b=1`, then `H^1_{a,1}(u)=0`.
- If `a=1` and `b` is even, every terminal-one history has exactly one cross,
  so the support is `{1}`.

For terminal one, every crossing removes one zero and one one, whereas every
homogeneous-zero contraction removes two zeros, so
`C equiv a (mod 2)` and `1<=C<=min(a,b-1)` whenever `b>=2`. The inductive
positivity argument closes. The exact one-cross law

```text
Pr(final 1,C=1)=1/a   for odd a,   0 for even a
```

and its symmetric terminal-zero counterpart survive direct hostile probes.
Independent literal-history enumeration reproduced the stated support and
linear coefficient on every two-run input with odd `n<=13`.

**C-A-03 — whole-history clock independence and the odd-rate transform:
PASS modulo the boundary repair below.** The continuous-time proof in
`main.tex:228-315` correctly separates the holding-time vector from the entire
embedded winner history. At any current length `ell`, the minimum of the
`ell-2` unit-rate clocks is `Exp(ell-2)`, the winner index is uniform on the
current windows, and the two are independent. Strong Markov plus
memorylessness restarts the same statement after each contraction, so the full
history factorization is correct and does not collapse only to the endpoint.

An independently written recursion over all odd words with `n<=9` confirmed
that for `s=2`

```text
E[e^{-s tau_n}] = product_(k=1,3,...,n-2) k/(k+s)
```

on every word, not only on two-run words. For `n>=3`, the Gamma-ratio
representation, the exact `e^{-2 tau_n}` moment formula, and the scaling-limit
argument are mathematically sound.

### Major

**M-A-01 — Corollary 4.2 overstates the `n=1` boundary (`main.tex:258-279`):
REPAIR REQUIRED.** Theorem 4.1 is explicitly stated for *every* odd initial
word (`main.tex:236-245`), so it includes `n=1`. In that boundary case there
are no contractions and `tau_1=0` almost surely. The empty-product and
empty-sum versions of the Laplace transform and moment formulas remain valid:

```text
E[e^{-s tau_1}] = 1,   E[tau_1]=0,   Var(tau_1)=0.
```

But Corollary 4.2 then writes `n=2m+1` and states
`e^{-2 tau_n} ~ Beta(1/2,m)`. At `n=1` this forces `m=0`, and
`Beta(1/2,0)` is not a valid probability law. So the corollary, as written,
has an allowed-boundary scope defect even though the preceding theorem is
correct.

This is a **major scope issue**, not a collapse of the main two-run package:
the kernel, endpoint law, marked law, independence theorem, and the
`n>=3` Beta/Gamma statements remain intact. Still, a hostile reader can point
to an invalid displayed distribution on a theorem-admissible boundary, so the
paper should not clear the internal gate unchanged.

**Required repair scope:** local statement repair only.

- Add an explicit boundary sentence before Corollary 4.2:
  `For n=1, tau_1=0 almost surely.`
- Restrict the Beta identity to `n=2m+1>=3` or equivalently `m>=1`.
- Keep the Laplace and moment formulas either under the same `n>=3` scope or
  separately note that they also hold at `n=1` by empty products/sums.
- The scaling theorem already concerns `m->infinity`; it needs no substantive
  change.

No verifier change is forced by this finding; the defect is in the theorem
statement, not in the finite exact replay.

**M-A-02 — owner subtraction and collision firewall: PASS.** The cited owner
boundary is internally coherent. Krapivsky--Redner and Goles et al. own
fixed-carrier majority dynamics; they do not supply the shrinking
adjacent-triple two-run kernel, endpoint history atlas, marked cross-count
recurrence, or whole-history clock theorem. The manuscript also correctly
declines any claim to generic majority logic, generic exponential-race facts,
or generic Beta/Gamma identities.

I also found no internal collision with the surrounding batch contracts: this
paper is about a shrinking current-window process with position histories,
whereas the nearby majority papers in the batch use fixed-carrier or different
feedback objects. A bounded exact-title/keyword search returned no direct
owner of the full theorem package, but that is only a bounded non-hit and does
not justify changing `HOLD_EXTERNAL`.

### Minor

**N-A-01 — verifier/build/PDF/anonymity audit: PASS.**

- Fresh canonical replay: `cmp=0` against
  `code/verification_output.txt`; the replay again ended in `status=PASS` with
  `exact_assertions=190740`.
- Fresh isolated four-stage build from only `main.tex` and `references.bib`:
  all stages exited zero; the isolated PDF was byte-identical to both the
  working `main.pdf` and `main_round0_original.pdf`.
- Frozen artifact hashes audited during this review:
  - `main.tex`: `0479c29f34d7ab4362074df3ab71719ac81041a6068fd3f0a498545b25e947c9`
  - `references.bib`: `ac64e59d8708acc0c757a7a2f6c49420c983a886dc3bf6672c70d1cae99b27a7`
  - `code/verify.py`: `3b66cd33bca07d3ea7ac2739eb226adb3b50204755596c561aa2885cd282a331`
  - `code/verification_output.txt`: `c23afcaf89ee9bf9ac5c2cd43ee72d6599155b9930215bf0dba0b4c328087ec8`
  - `main.pdf`: `2b151d0916d8d43d26988f3f70a25885fdf8e71255657dc1486bc300e070aa99`
  - `main_round0_original.pdf`: `2b151d0916d8d43d26988f3f70a25885fdf8e71255657dc1486bc300e070aa99`
- `pdfinfo`/`pdffonts` audit: four A4 pages, PDF 1.5, unencrypted, no forms,
  JavaScript, custom metadata, or metadata stream; title/author/subject/
  keywords metadata are blank; all 22 font rows are embedded, subsetted, and
  Unicode-mapped.
- `pdftotext` succeeded (`368` lines, `2037` words, `11525` bytes).
- All four pages were rasterized and inspected at 150 dpi. Equations, table,
  references, and proof endings are legible; no clipping or overlap was found.
- Current and frozen round-0 PDFs are byte-identical, so this review found no
  silent drift in the artifact.

## 2. Final gate

There is **one major REPAIR item** and **no critical REPAIR items**. After
the local `n=1` scope repair above, this manuscript should clear the internal
Round-0 hostile theorem/artifact gate. Until then the correct disposition is
**REPAIR / HOLD_EXTERNAL**.
