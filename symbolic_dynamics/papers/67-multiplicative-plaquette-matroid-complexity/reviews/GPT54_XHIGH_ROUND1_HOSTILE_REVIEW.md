# GPT-5.4 XHigh Round 1 Hostile Review

## Provenance

- Reviewer role: mandatory independent hostile mathematical reviewer
- Paper: `P67`
- Scope: `papers/67-multiplicative-plaquette-matroid-complexity`
- Baseline reviewed: current post-cross-review manuscript and package (`main.pdf`, byte-identical to `main_round2.pdf`)
- Model provenance: `gpt-5.4 xhigh`
- Date: `2026-08-25 UTC`

I read the substantive LaTeX source (`main.tex`, `sections/0_abstract.tex` through `sections/7_conclusion.tex`), `PROOF_PACKAGE.md`, `CLAIMS_EVIDENCE.md`, `CITATION_AUDIT.md`, `references.bib`, `main.bbl`, deterministic control code and frozen outputs, prior review and resolution records, build and QA records, and the compiled PDF text in `qa/final_text.txt`.

I also reran the non-writing control command

```sh
python3 code/verify_plaquette_matroid.py
```

and confirmed that its stdout is byte-identical to both frozen receipts:

- `code/verify_plaquette_matroid.out`
- `build/verify_plaquette_matroid.current.out`

I did not rerun the LaTeX build, because doing so would overwrite frozen build artifacts and PDFs, contrary to the review constraint.

## Verdict

**Verdict: INTERNAL HOLD DRAFT MATHEMATICALLY SURVIVES, BUT THE BASELINE IS NOT CLEAN ENOUGH TO CERTIFY AS ISSUE-FREE.**

I did **not** find a new mathematical counterexample to the theorem package. The core claims on root uniqueness, global free-axis coordinates, arbitrary finite projection rank, cycle completeness, graphic-matroid representation, Haar independence, prefix law, rectangle law, and one-edge rank updates survive hostile re-derivation.

I **did** find manuscript-integrity defects missed by the prior audit trail:

1. a visible TeX typo in the introductory definition of the evaluation maps;
2. an undefined symbol in the geometry summary table; and
3. a malformed row in the claims-evidence ledger.

None of these presently falsifies the mathematics, but they are real defects and mean the package should not be described as fully clean. External release remains **HOLD**.

## Theorem-by-Theorem Audit

1. **Root uniqueness for composite coprime multipliers: PASS.**
   For `n`, let `i` be maximal with `a^i | n` and `j` maximal with `b^j | n`. Coprimality gives `a^i b^j | n`, so `n = r a^i b^j`. If `a | r`, then `a^(i+1) | n`; likewise for `b`. Conversely, from `n = r a^i b^j` with `a \nmid r` and `b \nmid r`, Euclid's lemma forces `i` and `j` to be the maximal whole-power exponents. This works for composite coprime pairs, not just primes. The proof in [sections/2_coordinates.tex] is sound, and the control script exercises `(3,4)`, `(4,9)`, and `(6,35)`.

2. **Global free-axis homeomorphism: PASS.**
   On each root component, the plaquette rule becomes the vanishing mixed difference
   `y_{i,j} - y_{i+1,j} - y_{i,j+1} + y_{i+1,j+1} = 0`,
   which integrates to `y_{i,j} = y_{i,0} + y_{0,j} - y_{0,0}`. The equivalence
   `ab | r a^i b^j` iff `i,j >= 1` is valid under coprimality and the root exclusions. The inverse formula
   `x_{r a^i b^j} = x_{r a^i} + x_{r b^j} - x_r`
   uses only axis coordinates, and each output coordinate depends on only three input coordinates, so the product-topology continuity argument is complete. I found no hidden extension obstruction.

3. **Arbitrary finite projection rank: PASS.**
   For fixed root `r`, the finite image is exactly the image of the potential map
   `Phi_r(u,v)_(i,j) = u_i + v_j`.
   Extending used potentials to unused row/column indices gives surjectivity onto the finite restriction. On each connected component of `G_r(F)`, the kernel is one-dimensional, so
   `rank Phi_r = |I_r| + |J_r| - c_r`.
   Summing over roots yields the projection-dimension formula. This part is mathematically sound.

4. **Cycle completeness and graphic-matroid equivalence in all characteristics: PASS.**
   After the sign change `v_j = -w_j`, the potential map becomes the graph coboundary `u_i - w_j`. Cycle equations are necessary by telescoping and sufficient by spanning-forest integration. The transposed incidence representation gives the graphic matroid of `G_r(F)`, not the cographic matroid. Characteristic two is not a problem: the incidence representation still captures the cycle matroid, and the alternating cycle law reduces to the corresponding plus-sum law. I found no characteristic-dependent failure.

5. **Haar entropy, total correlation, and forest independence: PASS.**
   Finite projections are finite quotients of the compact group `X_{a,b}`, so Haar pushes to uniform counting measure. Since singleton projections are all of `F_q`, every coordinate has entropy `log q`, and total correlation is exactly the cycle-rank defect. Forests are exactly the jointly independent finite families. Pairwise independence of distinct coordinates is correct because two distinct coordinates yield two distinct edges in a simple bipartite graph, hence a forest.

6. **Prefix law: PASS.**
   The clean proof is the global-axis proof, not the local pivot argument. For `n <= L`, the reconstruction formula uses only indices `r a^i`, `r b^j`, and `r`, all at most `n`, hence at most `L`. Conversely, any assignment on `B \cap [L]` extends by filling the remaining free-axis coordinates arbitrarily and applying the global inverse. Therefore
   `|proj_[L](X)| = q^(L-floor(L/(ab)))`.
   The triangular pivot lemma is correctly demoted to a local rank cross-check rather than a standalone extension theorem.

7. **Rectangle law: PASS.**
   For `Q_r(M,N)`, the graph is `K_{M,N}`. Its rank is `M+N-1` and its cycle rank is `(M-1)(N-1)`, so both the counting formula and the Haar total-correlation formula follow immediately. No issue found.

8. **One-edge rank updates: PASS.**
   The corrected deletion/addition dichotomy is now right. Deleting a cycle edge preserves rank and lowers cycle rank by one; deleting a bridge lowers rank by one and preserves cycle rank. On addition, an edge joining already connected endpoints preserves rank and raises cycle rank by one; otherwise it raises rank by one and preserves cycle rank. The control suite now checks representative transitions and the logic matches standard graphic-matroid rank.

## CRITICAL Issues

None.

## MAJOR Issues

None at the theorem level. I did not find a fresh mathematical defect that forces a theorem contraction.

## MINOR Issues

### M1. Visible introductory display typo in the matroid-definition setup

The displayed definition of the evaluation maps contains a missing backslash:

- `sections/1_introduction.tex:60`

Current source:

```tex
\qquad \epsilon_n(x)=x_n,qquad n\in F.
```

This leaks into the compiled PDF text as a malformed `qquad` token in the sentence that is supposed to define the matroid ground-set representation. The meaning is recoverable, but this is a real source-level error in a load-bearing definition paragraph.

### M2. Undefined notation `V_r` in Table 1

The geometry summary table introduces `V_r` without defining it anywhere in the manuscript:

- `sections/5_rectangles.tex:116`

Current entry:

```tex
\sum_r(|V_r|-c_r)
```

Everywhere else the paper uses the explicit formula `|I_r|+|J_r|-c_r`. If `V_r` is meant to be the vertex set of `G_r(F)`, define it; otherwise replace it by the already defined notation. As written, the table is not self-contained.

### M3. Claims-evidence ledger row C9 is malformed

The claims ledger row for forest independence misuses the evidence/dependency columns:

- `CLAIMS_EVIDENCE.md:13`

Current row:

```md
| C9 | finite coordinates are jointly independent iff every incidence graph is a forest | C7--C8 | C7, C8 | PROVED |
```

Here `C7--C8` appears under `Evidence type`, where the rest of the table uses actual evidence classes such as proof method or source type. This is not mathematically fatal, but it means the ledger is not internally clean, despite the package repeatedly presenting itself as fully synchronized.

## Source and Ownership Audit

The subtraction discipline is substantially improved relative to the earlier baseline and is now mostly acceptable.

- The manuscript cites and delimits the established multiplicative-system context: Kenyon-Peres-Solomyak, Peres-Schmeling-Seuret-Solomyak, Ban-Hu-Lin, Ban-Hu-Lai, and Ban-Hu-Lai-Liao.
- It also correctly treats Whitney and Watanabe as standard ingredient sources rather than paper-specific contributions.
- The nearest valuation-coordinate/correlation neighbor, Mora Cuellar-Rojas Aravena-Yavicoli, is acknowledged and bounded away carefully.
- The bounded-search label `BOUNDED_NO_EXACT_COLLISION_LOCATED` is much more disciplined than a novelty claim, and the manuscript does not presently overstate priority.

I did not find source theft language or an illegitimate priority claim in the current baseline. The source/ownership posture is acceptable **provided** the paper continues to maintain external-release **HOLD** and does not upgrade bounded search into a novelty certificate.

## Reproducibility Audit

### What I verified directly

- The deterministic control code in `code/verify_plaquette_matroid.py` is non-writing and standard-library only.
- I reran it successfully.
- Its live stdout matches both frozen output files byte-for-byte.
- The live stdout SHA-256 matches the stated receipt:
  `a44506264017a8e6250e123df4477898def6c23f560c67b4e829948967c0bb26`.
- The script SHA-256 matches the stated receipt:
  `d0a2d3a1bd0c743b375eaf7e2dc98b100ff08f30cd741641cb1fcd81ab98a158`.
- `main.pdf` and `main_round2.pdf` are byte-identical at
  `7bf54d3b56530decc051f56cfedc38684d432fca8c73474347d2ab33546bda7d`.

### What I did not rerun

- I did not rerun `pdflatex`/`bibtex`, because doing so would overwrite the frozen PDF and log artifacts, which this task explicitly forbids.
- My build audit therefore relies on `BUILD.md`, `FINAL_QA.md`, `qa/final_log_findings.txt`, `qa/final_pdfinfo.txt`, `qa/final_pdffonts.txt`, and the extracted compiled text in `qa/final_text.txt`.

### Reproducibility limitations

- The control suite exercises prime fields of orders `2`, `3`, and `5`, not non-prime finite fields. This is acceptable because the manuscript's arbitrary-field structural claims are proved analytically, but the computational evidence is narrower than the theorem statement.
- The finite-projection brute-force check is exhaustive only for subsets of `[1,12]` in three `(a,b,q)` cases. Again, acceptable as regression evidence, not proof.

## Required Fixes

1. Fix the missing backslash in the introductory evaluation-map display at `sections/1_introduction.tex:60`.
2. Replace or define `V_r` in Table 1 at `sections/5_rectangles.tex:116`; using the already defined `|I_r|+|J_r|` would be safest.
3. Repair the malformed C9 row in `CLAIMS_EVIDENCE.md` so the evidence/dependency columns are semantically consistent.
4. After those edits, regenerate any synchronization artifacts that claim the package is fully clean and hash-frozen.

## External-Release Status

**HOLD.**

The mathematics survives, but the exact-neighbor search remains bounded and the package still contains correctable integrity defects that prior reviews missed. This is not external-release grade.

## Coordinator Summary

No new theorem-level failure was found. The root decomposition, global free-axis homeomorphism, arbitrary finite-shape rank theorem, cycle/matroid characterization, Haar independence formulas, prefix and rectangle laws, and one-edge update law all survive hostile reconstruction.

However, the current baseline is **not** issue-free. I found three concrete defects missed by the prior audit trail: a visible intro typo in the evaluation-map display, an undefined `V_r` in the geometry table, and a malformed row in the claims-evidence ledger. Keep the manuscript on **HOLD**, fix those items, and do not describe the package as fully clean until the metadata is resynchronized.
