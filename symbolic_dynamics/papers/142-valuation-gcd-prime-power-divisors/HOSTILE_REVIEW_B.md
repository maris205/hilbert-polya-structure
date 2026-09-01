# Hostile review B — round 2

Reviewer role: independent mathematical, ownership, and reproducibility audit;
the reviewer did not author P142.  Reviewed 2026-09-01 UTC.

## Verdict and counts

**ACCEPT** for the internal round-2 gate, with external status unchanged at
`HOLD_EXTERNAL`.

| Severity | Count |
|---|---:|
| Critical | 0 |
| Major | 0 |
| Minor | 2 |

I found no counterexample to the literal odd-prime valuation identity, the
three-residue overshoot argument, the pointwise clock or sharp uniqueness, the
temporal coefficients, or any every-target inverse branch.  The single repair
requested in `HOSTILE_REVIEW_A.md` is present and correct: the current fibre
proof explicitly says that the doubling and reflection labels overlap at
\(3a=e\), where their values agree, and the set union handles the coincident
source.

The two minor findings below are local proof/provenance cleanups.  Neither
changes a theorem, formula, verifier, or ownership decision.

## Hostile mathematical audit

### 1. Odd-prime valuation and the binary boundary — pass

For \(d=p^a\), the integer inside the gcd is

\[
 p^{2a}+p^{e-a}.
\]

If \(3a\ne e\), factoring the smaller power \(p^q\), with
\(q=\min(2a,e-a)\), leaves \(1+p^{|3a-e|}\), which is a
\(p\)-adic unit.  If \(3a=e\), the remaining factor is \(2\), also a
unit exactly because \(p\) is odd.  Since \(0\le q\le e\), the outer gcd
does not truncate the valuation.  Thus
\(\mathsf F_{p,e}(p^a)=p^{\min(2a,e-a)}\) exactly.

For \(p=2\) and \(e=3a\), the valuation becomes \(2a+1\).  The
inequality \(2a+1\le3a=e\) for \(a\ge1\) shows that the gcd does not
erase this extra factor.  The displayed witness \((e,a)=(3,1)\) is therefore
sharp.  I found no omitted cancellation or endpoint case.

### 2. Branch threshold and residue-class overshoot — pass

The equality \(2a\le e-a\) is equivalent to \(3a\le e\), giving the
stated split at \(L=\lceil e/3\rceil\).  If \(1\le a<L\) and \(j\) is
the first doubling index with \(2^ja\ge L\), then
\(L\le2^ja<2L\).  The last upper-bound step survives all three residues:

- \(e=3q\): \((L,U)=(q,2q)\), so an integer below \(2L\) is at most
  \(U\);
- \(e=3q+2\): \(U=2L-1\), so the same strict inequality suffices;
- \(e=3q+1\): \(U=2L-2\).  Here \(j\ge1\), so \(2^ja\) is
  even and cannot be the only apparent overshoot \(2L-1\).

Thus the first crossing lands in \([L,U]\), not beyond it.

### 3. Recurrent set, entry times, and unique deepest state — pass

The band endpoint identities \(e-U=L\) and \(e-L=U\) make
\([L,U]\) invariant under \(a\mapsto e-a\).  A positive state below
\(L\) doubles to the band; a state above \(U\) first reflects to
\(e-a<L\), with \(a=e\) mapping directly to zero.  The recurrent set,
fixed states, complement two-cycles, and fixed-iterate parity census follow.

For a lower state, the least \(j\) with \(2^ja\ge L\) is exactly
\(\lceil\log_2(L/a)\rceil\); the overshoot lemma makes it an entry into
the recurrent band.  An upper state \(e-b\) adds one reflection step.  With
\(m=\lceil\log_2L\rceil\), \(b=1\) attains depth \(m+1\).  For
\(b\ge2\),

\[
 L/b\le L/2\le2^{m-1},
\]

so every other upper state has depth at most \(m\); lower states also have
depth at most \(m\), and \(e\) has depth one.  Hence \(e-1\) is the
unique deepest state for \(e\ge4\).  Direct inspection of \(L=1\) gives
the correctly separated \(e=2,3\) cases.

### 4. Temporal coefficients — pass

Depth \(j\) on the lower branch is equivalent to

\[
 \left\lceil\frac{L}{2^j}\right\rceil
 \le a\le
 \left\lceil\frac{L}{2^{j-1}}\right\rceil-1.
\]

This interval has exactly the displayed \(c_j\) elements, and the intervals
partition \(\{1,\ldots,L-1\}\).  Reflection is a bijection to
\(\{U+1,\ldots,e-1\}\) and adds one to depth.  Adding the \(R\)
recurrent states and the state \(e\) at depth one gives

\[
 D_e(z)=R+z+(1+z)\sum_{j=1}^{m}c_jz^j.
\]

The formula also handles \(L=1\) correctly through an empty sum.

### 5. Image and every-target fibres — pass

Solving the two branch equations gives \(a=b/2\) on the doubling branch
and \(a=e-b\) on the reflection branch.  Both domain conditions reduce to
\(3b\le2e\), equivalent for integer \(b\) to \(b\le U\).  The
doubling candidate exists exactly for even \(b\), whereas the reflection
candidate exists for every \(0\le b\le U\).  Their equality is exactly
\(e-b=b/2\), or \(3b=2e\).  The repaired overlap sentence at
`main.tex:374-375` removes the sole ambiguity identified in round 1.  The image
and every empty/singleton/doubleton fibre branch are correct, including
\(b=0\), \(b=U\), and \(b>U\).

## Findings

### Minor 1 — one recurrence sentence is mildly circular in wording

At `main.tex:259-261`, after proving the displayed band invariant, the proof
says that every outside state “has strictly positive entry time, so it cannot
be recurrent.”  Entry time was defined as first entrance into the recurrent
set, whose exact identity is the conclusion currently being proved.  The
preceding orbit geometry already contains a complete noncircular argument, so
the theorem is not in doubt; only this sentence is backwards as written.

**Exact fix:** replace that sentence by the direct argument: once an outside
orbit first enters the invariant set \(\{0\}\cup[L,U]\), it never leaves,
and therefore can never return to its outside starting state; hence the
starting state is not recurrent.

### Minor 2 — package provenance text is stale after the round-1 repair

The current source and PDFs have the following actual relations:

```text
main.tex                    0cfd6cd1e02dee63efef17fde703ef4c90702633d30f97273dabaa78232076ed
main.pdf                    205059fecbbf17fd89bb0f957bd7bcb13b186265e65fa7e550acd4331f1db512
main_round1.pdf             205059fecbbf17fd89bb0f957bd7bcb13b186265e65fa7e550acd4331f1db512
main_round0_original.pdf    88198d07e2aed9e7cd1c46262808507ba25af54d2a7764b9933fa40ccd78a0a8
```

Thus `main.pdf` is byte-identical to `main_round1.pdf`, not to
`main_round0_original.pdf`.  The PDF text diff confirms that the substantive
change is the requested equality-overlap clarification, plus the induced page
flow.  `README.md` still calls the package round 0 and says the current and
round-0 PDFs are byte-identical; `BUILD.md` is a valid historical round-0
record but can now be misread as a current build record.  The statement that
no review files belong to the package is also no longer current.

**Exact fix:** update the current README/package map to distinguish the
preserved round-0 PDF from the current/round-1 PDF; retain `BUILD.md` explicitly
as a frozen historical record or append a labelled current-build section with
the hashes above.  Update round-status labels in current-facing ledgers without
rewriting the historical round-0 facts.

## Ownership audit

The ownership framing passes this round.  The paper assigns elementary
valuation algebra, ceiling/logarithm manipulations, functional-graph and zeta
bookkeeping, interval-map theory, and tent-map silhouettes zero contribution
credit.  It explicitly observes that normalisation exposes
\(x\mapsto\min(2x,1-x)\), makes no novelty or priority claim, treats a
direct owner or a specialist cosmetic-lift judgment as a kill condition, and
keeps `HOLD_EXTERNAL`.

The cited records accurately delimit background rather than claim ownership:

- Milnor and Thurston's [interval-map work](https://doi.org/10.1007/BFb0082847)
  is used only for general piecewise-monotone theory;
- Kuzovlev's [primary arXiv record](https://arxiv.org/abs/cond-mat/0412366)
  concerns reversible discrete tent maps and periodic-orbit statistics;
- Choi et al.'s [publisher article](https://www.mdpi.com/1099-4300/28/1/131)
  concerns a different bijective discrete skew-tent construction.

A fresh bounded search used the literal gcd expression, the exponent formula,
the slopes/turning point, and prime-power divisor dynamics.  It did not locate
a source stating this literal map or its full temporal/inverse atlas.  That is
only a bounded non-hit, not novelty, ownership, priority, or release evidence.
The cosmetic-lift risk remains real because all dynamics after the valuation
lemma is the elementary scalar map; the manuscript describes that risk
honestly enough for the internal gate.

## Reproducibility audit

- Canonical replay:
  `PYTHONDONTWRITEBYTECODE=1 python3 verify_p142.py | cmp - verification_output.txt`
  exited zero.  The transcript remains byte-identical and ends with
  `TOTAL_ASSERTIONS=319074` and `STATUS=PASS`.
- In addition to the canonical verifier, I ran an independent exact sweep of
  every \(2\le e\le2048\) for the recurrent set, entry clock, deepest
  state, temporal histogram, image, and all fibres, plus literal gcd checks for
  \(p\in\{3,5,7,11,13\}\) and \(2\le e\le256\).  It passed
  10,666,860 integer assertions.  This supplementary sweep is counterexample
  pressure only and is not part of the frozen canonical artifact.
- An isolated `/tmp` build containing only current `main.tex` and
  `references.bib` completed the documented `pdflatex`/`bibtex`/two-pass
  sequence.  Its PDF compared byte for byte with current `main.pdf` and had
  SHA-256 `205059fecbbf17fd89bb0f957bd7bcb13b186265e65fa7e550acd4331f1db512`.
- The settled log has no undefined citation/reference, bad box, rerun request,
  or BibTeX warning.  The current PDF is five A4 pages, has blank identifying
  metadata, has all 28 font rows embedded, and is visually free of clipping,
  collisions, malformed displays, or illegible text.

## Final disposition

The repaired manuscript clears the internal mathematical and reproducibility
gate.  The two minor fixes should be made as local wording and provenance
maintenance; they do not warrant another theorem-level review.  This
**ACCEPT** is not external clearance: no novelty, priority, posting,
submission, or release conclusion follows, and `HOLD_EXTERNAL` remains.
