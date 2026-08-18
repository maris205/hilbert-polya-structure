# Paper Improvement Log

## Score progression

| Manuscript state | Review round | Score | Verdict |
|---|---:|---:|---|
| Round 0 original | GPT-5.4 xhigh Round 1 | 6/10 | Almost |
| After Round 1 fixes | GPT-5.4 xhigh Round 2 | 7/10 | Ready |
| Round 2 final | Last external score retained | 7/10 | Ready; no Critical or Major findings |

The final row records the last external score rather than inventing a third review. Round 2 requested no acceptance-blocking fixes; its remaining minor presentation points and the independent visual-QA nits were nevertheless implemented before the final compilation.

## Round 1 review and fixes

<details>
<summary>GPT-5.4 xhigh raw review (verbatim text)</summary>

**OVERALL SCORE (1-10; 6=weak accept, 7=accept)**

6/10

**VERDICT (Ready / Almost / No)**

Almost

**SUMMARY**

This is a mathematically interesting and mostly careful paper. The main operator-theoretic claims look correct on the stated domains: bounded realization iff `Re s>0`, compactness throughout that half-plane, sharp `S_2` and `S_1` walls at `1/2` and `1`, exact `v_2`-block decomposition `W^*H_sW=\bigoplus_{k\ge0}2^{-ks}A_s`, and the resulting trace/determinant formulas in the legal ideal regimes. The paper is also commendably explicit about two delicate points that are often mishandled: `H_s=U_t H_\sigma U_t` is not unitary conjugacy, and the finite replay is reproducibility evidence only, not proof.

I did not find a fatal false theorem. The main reason I am at “Almost” rather than “Ready” is that one important bridge is still too compressed for referee-level self-containedness: the passage from finite compressions to absolute closed-walk trace sums in Section 7. A second issue is presentation/typing: the block-space unitary `W` should be typed more explicitly, and the replay material currently takes too much space relative to the mathematics.

**STRENGTHS (ranked)**

- The threshold proofs are well chosen and genuinely sharp. The three walls are detected by three different mechanisms, and the endpoint obstructions are analytically appropriate: row `m=1` for boundedness, central anti-diagonal mass for `S_2`, and disjoint trace-dual matchings for `S_1`.
- The complex-parameter handling is unusually disciplined. The bounded-realization typing for `Re s<=0` is correct, and the left-right phase factorization is correctly separated from spectral conjugacy.
- The `2`-adic decomposition is the structural heart of the paper and is used effectively. The direct sum for complex `s`, the trace-power factors, and the `det_2` block product fit together coherently.
- Appendix B is stronger than many papers would provide: it addresses the combined-eigenvalue product for nonnormal Hilbert-Schmidt blocks, compact-uniform convergence, and the local logarithm domain.
- The odd/even cycle solver is cleanly stated, including the positivity interval, parity filter for the odd block, and the distinction between based words, cyclic rotations, and primitive period.
- Claims-versus-evidence alignment is good. The finite replay never substitutes for proof, and the ownership/priority language is narrow rather than inflated.
- Figures and tables are mostly faithful to the mathematics; in particular the phase-domain table matches the legal determinant regimes.

**CRITICAL WEAKNESSES**

- None that currently look theorem-fatal. My objections are to proof presentation and mathematical typing, not to a detected false statement.

**MAJOR WEAKNESSES**

- Section 7’s justification of the absolute closed-walk trace formula is too compressed. The sentence “finite compressions ... converge in Hilbert-Schmidt norm, so their `r`th powers converge in trace norm” is plausible but not proved. This is the key bridge from operator theory to the label-solver evaluator, so it should not be left implicit.
- The typing of the block reordering is slightly sloppy. `W=\bigoplus_{k\ge0}W_k` is a unitary from `\bigoplus_{k\ge0}\ell^2(\N_{\rm odd})` onto `\ell^2(\N)`, not literally an endomorphism of a single already-named space. Theorem 6 is mathematically clear, but the Hilbert spaces should be declared explicitly once.
- Section 8 is oversized relative to the theorem content. The replay/mutation/integrity material is carefully fenced off, but it occupies too much argumentative weight in what is presented as a self-contained operator-theory article.

**MINOR WEAKNESSES**

- The word “Hankel” in the title is potentially misleading for `s\neq0`, since the matrix is not Hankel in the strict sense of depending only on `m+n`; the paper acknowledges this, but the title still overstates it.
- Proposition 6 in the main text is only a “proof sketch”. Since the appendix does contain the needed argument, the main text should point more sharply to the exact lemma that resolves the nonnormal block-product issue.
- The ownership/priority disclaimers are repeated more often than needed. One carefully written paragraph in the introduction plus one in the related-work section would suffice.
- Figure 1 is mathematically correct, but the valuation encoding may be hard to parse in grayscale despite the shape coding.

**ACTIONABLE FIXES (one per Critical/Major)**

- Add a short lemma in Section 7 or Appendix C: if `T_N=P_NH_\sigma P_N -> H_\sigma` in `S_2`, then `T_N^r -> H_\sigma^r` in `S_1` for every `r>=2`, with an explicit telescoping estimate using `S_2 \cdot S_2 \subset S_1` and boundedness of intermediate powers. Then deduce the absolute closed-walk sum formula for `Tr(H_s^r)` by comparison with `H_\sigma`.
- Retype the decomposition formally: define the source Hilbert space `\mathcal K := \bigoplus_{k\ge0}\ell^2(\N_{\rm odd})`, set `W:\mathcal K\to\ell^2(\N)`, and interpret `\bigoplus_{k\ge0}2^{-ks}A_s` as an operator on `\mathcal K`. This removes a persistent notational ambiguity at essentially no cost.
- Compress Section 8. Keep the one replay table and a short statement that the replay validates implementations only; move the mutation-count and hash-binding details entirely to the appendix/supplement.

**MISSING OR MISUSED REFERENCES**

- I do not see a seriously misused reference.
- The paper would benefit from more precise pin-point attribution to Simon for two standard facts used repeatedly: `S_1`–`B(H)` trace duality and the determinant conventions/eigenvalue-product formula for `\det_2`.
- If the authors want to keep “Hankel” in the title, it may help to add one sentence with a reference clarifying that this is a Hankel-supported or weighted Hankel-type matrix rather than a classical Hankel matrix in the strict `a_{m+n}` sense.

</details>

### Fixes implemented after Round 1

1. Added Lemma 7.2 with an explicit Hilbert--Schmidt compression argument, Schatten-product square estimate, bounded-power telescoping estimate, and trace-norm convergence for every integer power r >= 2.
2. Used that lemma twice to justify the nonnegative H_sigma walk-sum limit, absolute convergence for complex s, and equality with Tr(H_s^r).
3. Defined K as the Hilbert direct sum of odd-coordinate spaces and typed W: K -> ell^2(N); every block sum is explicitly an operator on K.
4. Reduced the main replay discussion to one table and its evidence boundary, moving source independence, mutation, clone-audit, and hash metadata to Appendix D.
5. Retitled the object as a weighted Hankel operator, defined that usage precisely, consolidated ownership wording, added a direct pointer to the exact determinant lemma, and retained only claim-level verified references.
6. Made Figure 1 independently legible in grayscale by redundant marker shape and fill encoding.

## Round 2 review and fixes

<details>
<summary>GPT-5.4 xhigh raw review (verbatim text)</summary>

**OVERALL SCORE (1-10; 6=weak accept, 7=accept)**

7/10

**VERDICT (Ready / Almost / No)**

Ready

**SUMMARY**

This now reads as a mathematically sound, self-contained paper on a specific dyadic-sum weighted Hankel operator. The core operator-theoretic claims appear correct on their stated domains: bounded realization iff `\Re s>0`, compactness throughout that half-plane, sharp `\mathcal S_2` and `\mathcal S_1` thresholds at `1/2` and `1`, the exact `2`-adic block decomposition on the explicitly typed Hilbert sum `\mathcal K`, and the resulting trace and determinant identities in the legal ideal regimes. The complex-parameter firewall is handled correctly: `H_s=U_tH_\sigma U_t` is used only for singular-value/ideal information, while powers, traces, and determinants are derived from the genuine block direct sum rather than from a false conjugacy principle.

The most important bridge that needed care is now in place. The finite-compression lemma gives `\mathcal S_2` convergence of `T_N` and `\mathcal S_1` convergence of `T_N^r` for every `r\ge2`, and Section 7 uses it correctly to pass from finite matrix traces to an absolutely convergent closed-walk expansion, first via the nonnegative `H_\sigma` comparison and then back to `H_s`. The determinant section is also in good order: the paper now cleanly separates the block-product identity for `\det_2`, the nonnormal combined-eigenvalue issue, compact-uniform convergence, and the local logarithm domain. Claims remain narrower than evidence, and the replay is correctly kept on the reproducibility side rather than the proof side.

**STRENGTHS (ranked)**

- The theorem domains and operator typing are clean and internally consistent. In particular, the bounded-realization language for `\Re s\le0` avoids illicit use of an undefined unbounded operator, and the valuation unitary is now correctly typed as `W:\mathcal K\to\ell^2(\mathbb N)`.
- The complex-parameter handling is rigorous. The paper explicitly distinguishes left-right phase factorization from unitary conjugacy, and all spectral/trace/determinant identities are derived only from the actual `2`-adic block decomposition.
- The compression-to-walk bridge is now self-contained and correct. The `\mathcal S_2\to\mathcal S_1` power-convergence lemma is enough to justify absolute closed-walk summability and the trace identification for `H_s`.
- The sharp endpoints are proved by the right mechanisms, not by extrapolation: row `m=1` for boundedness, central anti-diagonal mass for `\mathcal S_2`, and phase-normalized trace-dual matchings for `\mathcal S_1`, including the complex case.
- Appendix B handles the delicate determinant point properly: nonnormal Hilbert--Schmidt blocks, combined eigenvalue square summability, compact-uniform convergence of the canonical product, and the restriction of the logarithm to a local zero-free disk.
- The cycle solver is precise and well typed: odd/even separation, positivity interval, parity filter for the odd block, and the distinction between based walks, cyclic rotations, and primitive period are all correctly kept separate.
- Claims and evidence are well aligned. The finite replay is explicitly fenced off as implementation validation only, and neither novelty nor infinite endpoint statements are attributed to it.
- The figure/table claims visible from the text are faithful to the mathematics: the domain table matches the legal determinant regimes, and the figure captions do not overclaim beyond the proved statements.

**CRITICAL WEAKNESSES**

- None detected.

**MAJOR WEAKNESSES**

- None that block acceptance.

**MINOR WEAKNESSES**

- The main text still presents the `\det_2` block product as a proof sketch rather than a full proof. This is acceptable because Appendix B contains the needed argument, but the presentation is slightly uneven relative to the rest of the paper.
- The ordinary Fredholm product in the trace-class overlap `\sigma>1` is treated more tersely than the `\det_2` case. It is standard, and I do not think it is wrong, but the exposition there is lighter than elsewhere.
- A small amount of defensive boundary prose remains in the conclusion (`Hilbert--Polya`, primes, functional equation, priority disclaimers). It no longer overwhelms the paper, but a few sentences still read more as overclaim prevention than as operator-theory exposition.
- The introduction still repeats the replay counts explicitly. This is harmless, but the mathematics is strong enough that those numbers need not be foregrounded twice.

**ACTIONABLE FIXES (one per Critical/Major)**

- None required for acceptance.

**MISSING OR MISUSED REFERENCES**

- I do not see a materially misused reference.
- The current citations are narrow and appropriately owned: Simon is used for standard trace-ideal background, not as a substitute for the paper’s specialized determinant argument.
- No essential missing reference is apparent from the mathematical claims actually made. If the authors want broader contextualization of the phrase “weighted Hankel,” that would be optional background expansion, not a correctness issue.

</details>

### Fixes implemented after Round 2

1. Replaced the main-text det2 proof sketch with a complete application of the self-contained square-summable direct-sum lemma.
2. Expanded the ordinary Fredholm product proof through finite block sums and trace-norm determinant continuity.
3. Removed duplicated replay counts from the introduction and compressed defensive boundary prose in the conclusion without weakening the mathematical firewalls.
4. Fixed Table 3 at its Section 8 insertion point so that it no longer floats above the section heading.
5. Rephrased the page-5 transition that visual QA identified as a one-word continuation.

## Compilation and visual QA

- Final PDF: `main.pdf`, identical to `main_round2.pdf`.
- Page format: 16 A4 pages; main text and conclusion end on page 12, followed by four appendix pages.
- Final LaTeX log: zero undefined citations, zero undefined references, zero package/LaTeX warnings, and zero overfull or underfull boxes.
- Fonts: embedded, subset, and Unicode mapped.
- Independent read-only visual QA: pass; no clipping, overlap, overflow, missing figure, or unreadable label. Figure 1 remains distinguishable in grayscale, Figure 2 retains line-style and endpoint redundancy, and Figure 3 remains legible.

## PDFs

- `main_round0_original.pdf` -- original generated manuscript.
- `main_round1.pdf` -- after Round 1 fixes.
- `main_round2.pdf` -- final manuscript after Round 2 fixes.

## Post-Round-2 ToUnicode repair and final QA

Independent extraction QA found eight illegal C0 bytes in the pre-repair PDF,
all emitted by unmapped extensible-delimiter glyph pieces.  The affected
partial-fraction, determinant-overlap, compression-square, cardinality, and
finite-block trace displays now use ordinary fixed parentheses.  No
mathematical expression or claim changed.

Two clean builds with `SOURCE_DATE_EPOCH=1787011200`, `TZ=UTC`, and
`LC_ALL=C` produced byte-identical PDFs.  The replacement `main.pdf` and
`main_round2.pdf` have SHA-256
`8772e8c9649bea045bace7b369d446ff51f5c9a7eb95c7e1bc957a9ff2f02d6e`.
The final log hash is
`e458745557941be7d04e4d9420a308d4eb6dcf0092cdba619007ca820a595cdd`,
and the bibliography hash is
`2bd8b051f978b0124a143c8cdc064218a7e9ff4740990dc16df302554439c6f7`.

Default, layout, and raw `pdftotext` extraction now each contain zero illegal
C0/DEL characters, zero C1 controls, and zero U+FFFD characters.  Both bbox
modes produce well-formed XML.  All fonts remain embedded, subset, and
Unicode mapped; the compile log is warning-free; and all 16 rendered pages
pass visual inspection.  Full counts and the permanent withdrawal of the old
PDF hash are recorded in `evidence/PDF_QA.md`.
