# P157 Hostile Review A — original report

**Review date:** 2026-09-02 UTC  
**Calibration:** `NOT_CALIBRATED`  
**Criteria binding:** `criteria_binding_unavailable`; no venue-fit claim is
made.  
**Execution boundary:** one role-separated adversarial review, not evidence of
independent error processes.  No P157 author file was modified during the
review; this report is the only new paper-local file.

## Verdict

**REVISE — 0 Critical / 0 Major / 2 Minor.**

The frozen A1–A3 and B1–B4 formulas survive independent derivation and
6,168,156 reviewer-owned exact checks.  The `N=1,2` branches, exact cubic
Taylor lift, `2^v` source-bit multiplicity, endpoint fibres, image census,
author-verifier transcript, references, and deterministic build all pass.
The requested revision is limited to attribution and scope wording; no
theorem, proof, verifier, transcript, or numerical result needs to change.

## Strongest counter-argument

The strongest objection is that the mathematical engine is classical and the
remaining calculation may be too thin to justify the manuscript's broadest
labels.  The polynomial, its approximate-idempotent role, and the quadratic
improvement are explicitly present in prior work.  After subtracting those
items, A1 is an immediate valuation consequence of the two factorizations,
and A2–A3 are divisibility counts.  The residual burden is therefore carried
almost entirely by the normalized-unit inverse atlas.  A skeptical reader can
also object that “complete finite dynamics” normally suggests a full
functional-graph or iterated-preimage classification, whereas the paper gives
endpoint/time data and complete **one-step** images and fibres.

That objection does not refute the paper.  The branchwise bit-lifting lemma is
correct, the boundary multiplicities are nontrivial and exact, and the
manuscript already assigns the classical engine zero contribution credit.  It
does, however, make neutral attribution and a precise definition of
“complete” important.  Without those wording repairs, the title and theorem
label invite a broader claim than the displayed formulas themselves make.

## Independent theorem audit

| Interface | Independent derivation / attack | Verdict |
|---|---|---|
| **A1** selected-error valuation | `F(x)=x^2(3-2x)` and `1-F(x)=(1-x)^2(1+2x)` have odd cofactors in the selected parity basin.  Therefore the truncated valuation doubles exactly. | PASS |
| **A2** pointwise entry | Parity is preserved, so the basin endpoint is `x mod 2`.  Entry occurs at the least `t` with `2^t v_2(e(x))>=n`; direct iteration through modulus `2^18` agrees. | PASS |
| **A3** temporal census | With `a=ceil(n/2^t)`, each basin contains `2^(n-a)` selected errors divisible by `2^a`; the basins are disjoint and reflection-bijective. | PASS |
| sharp height / recurrence | A valuation-one error realizes `ceil(log_2 n)` for `n>=2`; `n=1` has only the two endpoints.  Every state reaches `0` or `1`, both fixed. | PASS |
| **B1** normalized image | For odd `w`, `w^2=1 mod 8`; hence `h_1(w)=7 mod 8` and `h_v(w)=3 mod 8` for `v>=2`.  Direct quotient enumeration confirms the separate `N=1,2` reductions. | PASS |
| **B2** every-target fibre | Each modulo-four branch is two-to-one onto the prescribed class for `N>=3`; both branches give four reduced solutions.  Restoring high source bits multiplies this by exactly `2^v`. | PASS |
| **B3** endpoints | `F(x)=0 mod 2^n` iff `2v_2(x)>=n`, giving `2^floor(n/2)` sources.  Reflection gives the same count over one. | PASS |
| **B4** image size | A fixed low-three-bit class has `2^(N-3)` odd units for `N>=3`, while `N=1,2` each contribute one.  The valuation strata are disjoint; reflection and the two endpoints give the printed sum. | PASS |

The abstract and theorem agree on all seven interfaces.  In particular, the
abstract mentions the separate `N=1,2` boundaries immediately after its
modulo-eight synopsis, and the body does not silently extend the four-to-one
law to those quotients.

## Focused proof attacks

### `N=1,2` boundaries

For odd residues modulo two, the domain has one class and the unique image is
odd, so the reduced fibre is one.  Modulo four, every odd square is one and
the cubic term vanishes modulo four, so `h_v(w)=3 mod 4` for every `v>=1`;
both odd inputs hit that target.  These are genuinely one- and two-preimage
laws, not truncations of a four-preimage statement.  The theorem, proof,
author verifier, and reviewer verifier all preserve this distinction.

### Exact Taylor lift

For

```text
h_v(w)=w^2(3-2^(v+1)w)
```

the derivatives printed in the manuscript are correct.  With
`delta=4*2^j`, exact cubic Taylor expansion divided by eight gives term
valuations

```text
j,  2j+1,  and at least 3j+5.
```

The first normalized term is `2^j` times an odd integer and the other two
vanish modulo `2^(j+1)`.  Hence
`Phi(z+2^j)-Phi(z)=2^j mod 2^(j+1)`.  Induction makes each branch a
permutation at every truncated quotient.  The reviewer program checks the
exact Taylor identity, all divisibilities, and every bit toggle for
`v=1..8`, both residues modulo four, `j=0..11`, and every `z` modulo
`2^(j+1)`.

### Source-bit multiplicity

For output quotient size `N=n-2v`, an exact-valuation source is
`x=2^v w`, with `w` odd modulo `2^(n-v)`.  The target only sees `w mod 2^N`,
so the reduction kernel has size

```text
2^((n-v)-N)=2^v.
```

Every lift remains odd, hence every lifted source retains exact valuation
`v`; the lifts are distinct modulo `2^n` and produce the same target.  The
reviewer-owned lane checks the complete high-bit lift family for every
`3<=n<=18` and every `v` with `2v<n`.

## Exact-control and artifact audit

The author verifier was cold-replayed with bytecode disabled.  Its stdout is
byte-identical to `verification_output.txt`, containing 2,563,880 passing
assertions at SHA-256
`f5f1884f809110ca8ec3a954af1783c774896708495d626f694bbfb23f7876f1`.
Its windows include every state and target through `n=17`, and normalized
units for `v=1..6`, `N=1..11`.  The code checks zero fibres as well as positive
ones.  Finite enumeration is consistently described as counterexample
pressure, not proof.

An independently written reviewer verifier is stored outside the paper at
`docs/papers157_161_sequence/reviews/p157_a/verify_p157_review_a.py`.  It does
not import or call the author verifier.  It performs 6,168,156 exact checks,
extends the full atlas to `n=18`, extends normalized units to `v=1..8` and
`N=1..13`, and adds explicit Taylor and high-source-bit lanes.  Two cold runs
match `CANONICAL.txt` byte for byte.  Reviewer transcript SHA-256:
`8f7c8de7a7879deb4d044c4a73839a46692b722d06598f8febc84eaaed33e65d`.

Two fresh directories containing only `main.tex` and `references.bib` were
built by `pdflatex -> bibtex -> pdflatex -> pdflatex`.  Both PDFs are
byte-identical to each other, `main.pdf`, and `main_round0_original.pdf` at
SHA-256
`4188a459ad233e8a6a55d5706648617e833ea0f7771d324a368352182a2f9c0d`.
The PDF has four A4 pages; 25/25 fonts are embedded and subsetted; identifying
metadata is blank.  The settled log has no unresolved citation/reference,
rerun request, BibTeX warning, overfull box, underfull box, or build error.
All four pages were independently rasterized and inspected without finding
clipping, overlap, malformed formulae, or bad glyphs.

## Source and ownership audit

Crossref DOI metadata confirms the sole bibliography entry: Igor Burban and
Yuriy Drozd, “Derived categories of nodal algebras,” *Journal of Algebra*
272(1), 46–94 (2004), DOI `10.1016/j.jalgebra.2003.07.025`.  The author
manuscript at arXiv `math/0307060`, Appendix A, Lemma A.4, explicitly prints
`G_1(x)=3x^2-2x^3` and states its approximate-idempotent lifting property.
The polynomial, lifting role, and quadratic improvement are therefore
correctly subtracted.

The important attribution nuance is that the paragraph immediately before
Lemma A.4 calls this a known result and points to Jacobson's *Structure of
Rings* (1956), Section III.8.  The current paper never claims that
Burban–Drozd invented the polynomial, but the eponymic title can be read that
way.  A bounded OpenAlex/arXiv screen did not locate the complete B1–B4 finite
atlas.  That is only a non-hit, exactly as the manuscript states.

## Findings

### Critical

None.

### Major

None.

### Minor

#### M1 — Eponymic title overstates the established attribution

- **Evidence anchor:** text: title “Finite Dynamics of the Burban--Drozd Idempotent-Lifting Cubic”; source manuscript immediately before Lemma A.4 calls the result known.
- **Confidence:** 5/5 — directly checked against the primary author manuscript and its bibliography.
- **Why it matters:** the subtraction is conservative, but the title may imply
  that Burban and Drozd originated a polynomial that their own text presents
  as known.
- **Minimum repair:** use a neutral title such as “Finite Dynamics of the
  Idempotent-Lifting Cubic (3x^2-2x^3) Modulo Powers of Two,” and replace
  “direct owner” in author-side ledgers with “direct prior record” or “direct
  foundation record.”  If historical priority matters for external release,
  inspect Jacobson III.8 before assigning an eponym.

#### M2 — “Complete finite dynamics/atlas” needs an explicit scope qualifier

- **Evidence anchor:** text: abstract “determine its complete finite dynamics”; theorem label “complete finite atlas.”
- **Confidence:** 4/5 — finite-dynamics proof audit; terminology conventions vary.
- **Why it matters:** the paper proves a complete temporal census and complete
  one-step image/fibre atlas, but it does not state a target-resolved formula
  for every iterated fibre or classify full transient trees up to isomorphism.
- **Minimum repair:** replace “complete finite dynamics” by “complete temporal
  and one-step inverse atlas,” or add one sentence immediately after the first
  use defining “complete” as completeness only for A1–A3/B1–B4.  Do not add a
  new iterated-fibre claim.

## Required repair and re-review target

1. Neutralize the eponym or document the historical attribution more fully.
2. Qualify “complete” to the exact frozen interfaces.
3. Leave A1–A3, B1–B4, the Taylor proof, both verifiers, and both frozen
   transcripts unchanged unless a separate mathematical reason emerges.

After these two local wording repairs, Review A supports `ACCEPT_INTERNAL /
HOLD_EXTERNAL`, subject to an independent Review B and continued direct-owner
screening.  This report does not authorize external posting, circulation,
author contact, or submission.
