# Round 1 independent review

Manuscript: *Raw Rational-Prime Multipliers at a Frozen PCF Quadratic: Divisibility Obstruction and Exact Audit*  
Date of review: August 13, 2026  
Reviewer mode: full local read of manuscript/PDF/artifacts/code + independent test/build checks + spot-check of key literature claims against primary sources

Score: 7.1/10  
Verdict: MINOR

## Executive assessment

This is a careful, unusually well-audited negative-result note. The core mathematical statement is correct as written: the derivative-content divisibility lemma is elementary but sound, the specialization to \(g(z)=z^2-u\) is valid, the \(n=1\) residue \(\lambda=\pm2\) is closed exactly, the conjugacy transfer to \(f_u(x)=1-ux^2\) is correct, the distinction between raw-prime / exponent-prime / modulus-only targets is consistently enforced, and the cotangent discussion is responsibly scoped to the regular branchwise setting.

The software side is also strong. I found the exact low-period audit, the formal-versus-exact period saturation, the controls, and the independent coordinate duplication all technically credible. I also independently reran the local test suite and a clean LaTeX build in a copied temporary paper directory; both passed cleanly.

My main reservation is not theorem-level correctness. It is package readiness and framing. Two issues need fixing before I would call the package review-ready:

1. the manuscript repeatedly calls the parameter/map “PCF,” but this standalone paper never actually proves or cites the postcritical-finiteness relation in the manuscript itself; and
2. the published “VERIFIED” artifact manifest is not fully consistent with the current on-disk files: I found one concrete hash mismatch.

These are fixable. Because the mathematical core looks right and the claims are mostly scoped responsibly, I land at MINOR rather than MAJOR.

## What I checked

- Read `paper/manuscript.tex` and the rendered PDF content.
- Read the lock / proof / derivation / novelty / citation / integrity documents:
  `experiments/source_lock.json`, `notes/PROOF_PACKAGE.md`, `notes/DERIVATION_PACKAGE.md`,
  `notes/NOVELTY_AUDIT.md`, `notes/CITATION_VERIFICATION.md`,
  `paper/CLAIM_MANIFEST.json`, `paper/EXPERIMENT_PASSPORT.json`,
  `paper/FIGURE_PACKAGE.json`, `paper/INTEGRITY_PRE_REVIEW.md`.
- Inspected the machine-readable outputs, especially:
  `results/candidate_multiplier_audit.json`, `results/control_audit.json`,
  `results/conjugacy_audit.json`, `results/symplectic_bridge_audit.json`,
  `results/proof_audit.json`, `results/final_result_manifest.json`.
- Read the implementation in `code/prime_multiplier/*.py` and the tests in `code/tests/*.py`.
- Independently ran:
  - `python -m pytest -q -p no:cacheprovider` in `code/` → `37 passed in 34.88s`.
  - a copied-temp-directory LaTeX build (`pdflatex -> bibtex -> pdflatex -> pdflatex`) → no warnings; PDF built successfully.
- Checked PDF metadata via `pdfinfo` → title/author/subject/keywords populated; 11 pages.
- Spot-checked key prior-work / novelty boundaries against primary sources (Huguin 2021/2022/2023, Ji–Xie 2023, Ji–Xie–Zhang 2026 / arXiv 2308.00289, Murakami–Sano–Takehira 2024, Fogedby–Jensen 2005, Demaeyer–Gaspard 2009).
- Verified the final hash manifest against on-disk files.

## Scientific assessment

### 1. Theorem/proof chain

I do not see a theorem-level flaw in Theorem 3.1 or Corollaries 3.2–3.3.

- The monicity/integrality step is correct.
- The chain-rule factorization \((F^n)'(\alpha)=m^n\prod_j H(F^j(\alpha))\) is exact.
- The rationality step \(\mathbb Q\cap\overline{\mathbb Z}=\mathbb Z\) is used correctly.
- The theorem is correctly stated for points fixed by \(F^n\), not necessarily of exact period \(n\).
- The modulus-only nonclaim is explicitly preserved and mathematically necessary.

For the frozen quadratic:

- \(g'(z)=2z\) gives the required derivative content with \(m=2\).
- The period-one residue is closed correctly: \(\lambda=2\Rightarrow u=0\), \(\lambda=-2\Rightarrow u=2\), both impossible for the chosen cubic.
- The odd exponent-prime exclusion is a correct \(2\)-adic corollary.
- The \(p=2\), \(n\ge2\) case is correctly left OPEN. The paper does not overclaim here.

### 2. Exact audit / formal vs exact period / controls

This part is well done.

- The repeated saturation in `dynatomic.py` is the right move for formal-period contamination.
- The `c=-3/4` control is genuinely informative: it shows the pipeline can detect an odd raw prime when the algebraic-integrality hypothesis is deliberately broken.
- The `z^2` and `z^2-2` controls are also well chosen. They recover the sharp \(2^n\) boundary and the Chebyshev signed residue.
- The independent \(f_u\) / \(g\) coordinate duplication is a real check, not a cosmetic one.

I am satisfied that the finite audit is being used as an implementation certificate rather than as illicit evidence for the all-period theorem.

### 3. Symplectic bridge

The paper is disciplined here. The bridge claim is branchwise, regular-locus only, and does not pretend to give a global compact symplectomorphism. The limitations at \(q=0\), branch-image overlap, noncompactness, and the failure for zero multipliers are all stated.

That is the right level of claim.

My only caveat is that the code-side “noncompactness check” is weaker than the prose suggests: the recorded witness is mathematically fine, but the computed Boolean is basically tautological rather than a deep verification. This does not affect the manuscript’s scientific claim, but it is worth knowing.

### 4. Citation and novelty boundary

This is mostly responsible.

- The paper does not falsely claim priority for the general lemma.
- The prior-work section correctly places the manuscript against stronger global rigidity results and existing multiplier-polynomial integrality work.
- The symplectic bridge is not sold as novel.

My read is that the literature positioning is credible **provided the paper is presented as a narrow exact obstruction note**. I would not support any reframing toward “new general arithmetic-dynamics theorem” or “new symplectic construction.”

### 5. Reproducibility / integrity

This is strong overall, but not flawless.

Strong points:

- Tests pass.
- Temp-directory rebuild is clean.
- The manuscript/log are warning-free.
- The artifact organization is unusually transparent.

But one concrete integrity issue remains:

- I verified all 43 entries in `results/final_result_manifest.json`.
  42 match the current files, but **1 does not**:
  `notes/NOVELTY_AUDIT.md`
  - expected SHA-256 in manifest:
    `1478aeb69907a4c628437d634e2ca1655576c0c15a7c92c68963db0743de8b84`
  - actual current SHA-256 on disk:
    `1b5bd5b0efb4b604aea69687489a27b5c5c1bed1bf54efbbe73e40a9504bb629`

This means the current working package is **not fully consistent** with the manifest that declares `verification_status: VERIFIED`.

That does not by itself invalidate the theorem or the low-period audit, but it does matter for a paper that emphasizes source locking and artifact integrity.

## Mandatory fixes

1. Prove or explicitly cite the PCF property inside this manuscript.

   The paper repeatedly uses “frozen PCF quadratic” in the title, abstract, Section 4 heading, discussion, and conclusion (e.g. `manuscript.tex` lines 38–39, 48–49, 234, 452–453, 503), but the standalone manuscript never actually establishes the postcritical-finite relation. The theorem itself does not need PCF, but the paper’s framing does.

   The clean fix is easy: add the exact orbit relation for the critical point, e.g.
   \(0\mapsto 1\mapsto -(u-1)\mapsto u-1\mapsto u-1\),
   or explicitly cite the source where that exact relation is proved. If you do neither, then “PCF” should be removed from the standalone framing.

2. Repair the manifest mismatch before calling the package verified/frozen.

   Either:

   - regenerate `results/final_result_manifest.json` from the actual current tree, or
   - restore `notes/NOVELTY_AUDIT.md` to the version whose hash is recorded in the manifest.

   As written, the paper’s reproducibility narrative overstates the current on-disk consistency.

3. Make the note-level contribution framing even more explicit.

   The manuscript is already better than most on this point, especially at lines 124–129, but I still recommend one more pass through the title/intro/conclusion so the reader cannot mistake this for a priority claim about a new general theorem. What is solid here is:

   - an elementary divisibility lemma,
   - a candidate-specific all-period obstruction at one frozen algebraic parameter,
   - and an unusually careful exact audit package.

   That is enough for a good note. It is not the same thing as a broad arithmetic-dynamics advance.

## Optional improvements

1. Improve Figure 2 typography.

   Panel (b) is readable, but the code-like polynomial formatting (`L**2`, etc.) looks like an internal artifact dump rather than publication typography. This is the one obvious presentation weakness in an otherwise clean figure set.

2. Add one sentence stating explicitly that the PCF property is not used in Theorem 3.1 or Corollaries 3.2–3.3, only in parameter provenance / broader program context.

3. If space matters, trim some of the artifact-map prose and move one layer of registry detail to supplementary material. The paper’s good discipline is already evident without repeating every registry role in the main text.

4. If you keep the symplectic section, consider citing the cotangent-lift formula itself at the proposition entry point, not only in the prior-work paragraph.

## Bottom line

I found no mathematical blocker in the main theorem/corollary chain, and the exact audit package is stronger than average for this kind of note. The paper’s main vulnerabilities are standalone framing and one concrete integrity mismatch in the final hash manifest.

So my recommendation is:

- scientifically: basically sound;
- editorially: needs small but real cleanup;
- final verdict: MINOR.

If the two mandatory factual issues above are fixed, I would be comfortable passing this to the next round as a narrow exact-obstruction note.
