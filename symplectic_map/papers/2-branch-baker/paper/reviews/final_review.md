# Final Independent Technical Review

Manuscript: *Finite-Rank Obstructions for Locally Constant Multiplier Clocks:
An Audited PCF Markov--Baker Note*

Artifacts reviewed: `paper_round2.pdf`, `manuscript.tex`,
`references.bib`, both prior review reports, the citation-verification record,
the frozen result manifest, and the implementation tests.

Overall score: **7.5/10**

Verdict: **PASS_WITH_MINORS**

Venue calibration: **technically ready as a specialist note**. The remaining
comments below concern proof exposition and citation pinpointing, not the
validity of the all-period quotient or any headline conclusion.

Confidence: **4.5/5**

## Executive verdict

The localized major issue identified in round 2 has been repaired.  The new
nested-cylinder/homterval argument supplies the previously missing generating
property, preserves least periods away from partition endpoints, and reduces
all periodic coding ambiguity to the single symbolic two-cycle over the fixed
point \(d\).  I found no counterexample or unproved mathematical step that
would require weakening the all-period parent quotient to the period-20 audit
cutoff.

The proof is concise enough that two elementary intermediate facts are left
implicit: every finite named cylinder is a compact **interval**, and singleton
intersection implies its diameter tends to zero.  Both facts follow directly
in this full-branch Markov case and do not constitute a gap.  Making the first
one explicit, and adding theorem/chapter pinpoints for the three interval-
dynamics results, would improve publication polish.

The finite-rank theorem, affine carrier, determinant conventions, multiplier
corollary, exact counts, and frozen numerical evidence show no regression.
The PDF compiles cleanly, all fonts are embedded, the corrected Bowen--Lanford
name renders properly, the audit figure is now in the appendix, and the key
proof pages are readable.

## Decisive check: generating partition and sole boundary ghost

### 1. Nested cylinders exist and are intervals -- **PASS**

The graph is a genuine full-branch Markov graph for the displayed partition:

\[
 f(I_0)=I_2,\qquad f(I_1)=I_2,\qquad
 f(I_2)=I_0\cup I_1.
\]

On each \(I_i\), the restriction is monotone (strictly on its interior), and
for every allowed edge \(i\to j\) the corresponding restriction contains all
of \(I_j\).  Backward induction along a finite admissible word therefore gives
a unique nonempty compact interval in the initial branch.  Thus the sets

\[
 K_N(\omega)=\bigcap_{j=0}^N f^{-j}(I_{\omega_j})
\]

are nested nonempty compact intervals, not merely arbitrary compact sets.
Compactness of the core gives nonemptiness of their infinite intersection.
The manuscript states this as “nonempty compact cylinder”; the interval
property is immediate from its preceding Markov/monotonicity calculation but
would be worth naming explicitly.

### 2. A nontrivial fibre is a homterval -- **PASS**

If \(K(\omega)\) contained a nondegenerate interval \(J\), then for every
\(j\geq0\), \(f^j(J)\) would remain inside the named branch
\(I_{\omega_j}\).  After coarsening \(I_1,I_2\) to the right monotonicity
branch, no iterate can cross the critical point \(0\).  A first critical
encounter in the interior would force the preceding locally monotone image to
cross the two sides of \(0\), contradicting its single named branch.  Hence
every iterate is monotone on the interior of \(J\), so this interior is a
homterval for the two-branch unimodal partition.

This is the correct bridge from a nontrivial itinerary fibre to the standard
homterval lemma.  The artificial split at \(d\) causes no problem because
coarsening states 1 and 2 removes that split before the lemma is applied.

### 3. Smooth-dynamics hypotheses -- **PASS**

All hypotheses needed by the invoked interval-dynamics results are checked:

- \(f_u\) is \(C^\infty\) on the invariant compact core and has a single
  quadratic, hence nonflat, critical point at \(0\).
- Its Schwarzian derivative is
  \(Sf_u(x)=-3/(2x^2)<0\) away from that critical point.
- The exact lower bound
  \[
  |f'_u(d)|=2u(u-1)>
  5244381/3125000>1
  \]
  correctly proves that \(d\) is repelling.
- The critical point and both core endpoints eventually land on \(d\):
  \(0\to1\to-d\to d\), \(-d\to d\), and
  \(1\to-d\to d\).

The negative-Schwarzian basin theorem therefore excludes a periodic attractor
with an open basin: its immediate basin would have to contain the critical
point or a core endpoint, while all such distinguished points land on the
repelling \(d\).  A neutral periodic orbit with an attracting side is excluded
by the same basin argument.  The no-wandering-interval theorem applies to this
smooth nonflat unimodal map.  The homterval lemma then leaves only a wandering
interval or a periodic attracting basin, both already excluded.

Consequently \(K(\omega)\) is a singleton.  Since the \(K_N\) are nested
compact intervals, singleton intersection also implies
\(\operatorname{diam}K_N\to0\).  The closed-endpoint convention can give a
point more than one symbolic name, but each **named** fibre is still a
singleton, exactly as stated.

### 4. Periodic realization and least-period preservation -- **PASS**

For an \(n\)-periodic word, \(K(\omega)=K(\sigma^n\omega)\); singleton fibres
give \(f^n(x)=x\).  Conversely, every parent periodic orbit has at least one
admissible named itinerary.  Away from endpoints that itinerary is unique.
If a primitive symbolic word of period \(n\) represented an off-endpoint point
of smaller period \(r<n\), uniqueness would force
\(\sigma^r\omega=\omega\), contradicting primitivity.  This is the missing
least-period argument requested in round 2, and it is correct.

### 5. Boundary enumeration -- **PASS**

The partition endpoint set is \(E=\{-d,0,d,1\}\).  If a periodic parent
orbit meets \(E\), the endpoint met is periodic; the exact endpoint dynamics
shows that only \(d\) is periodic.  At \(d\in I_1\cap I_2\), the restricted
adjacency graph has only \(1\to2\) and \(2\to1\), so it supplies exactly one
primitive symbolic period-two orbit, represented by the two phase shifts of
\(1212\ldots\).  There are no additional endpoint names or period changes.

It follows rigorously for all periods that the parent-minus-symbolic primitive
count correction is \((+1,-1,0,\ldots)\), and therefore

\[
 \frac{1-z^2}{1-z}=1+z,\qquad
 \zeta_f(z)=\frac{1+z}{1-2z^2}.
\]

The corresponding parent fixed-point counts, \(1\) for odd \(n\) and
\(2^{k+1}-1\) for \(n=2k\), are consistent with this replacement.  The
period-20 parent audit is correctly described as an implementation check, not
as the proof of the all-period statement.

## Other mathematical claims

### Finite-rank theorem -- **PASS**

Higher-block recoding preserves cyclic block multiplicities, every orbit
length is an integer combination of finitely many local log-moduli, and
\(V_{\rm cyc}\subseteq V\).  Rational independence of distinct rational-prime
logarithms follows from unique factorization.  The cardinality bound by
\(\dim_{\mathbb Q}V_{\rm cyc}\), the finite-rank sharpness example, and all
listed exclusions are correct and honestly scoped.

### Markov--baker carrier -- **PASS**

The PCF identities, adjacency and factor-orientation matrices, PF vectors and
areas, strip tilings, and affine branch maps are mutually consistent.  Each
allowed derivative is

\[
 \operatorname{diag}(\sigma\sqrt2,\sigma/\sqrt2),
\]

with determinant \(+1\).  The Liouville calculation
\(B^*(x\,dy)-x\,dy=d((b/a)y)\) proves branchwise exactness, not merely area
preservation.  The manuscript properly restricts the claim to branch
interiors and almost-everywhere invertibility.

### Cycle, sign, and multiplier ledgers -- **PASS**

The eigenvalues \(0,\sqrt2,-\sqrt2\), primitive vector through period 20,
total 226, and \(\det(I-zA)=1-2z^2\) agree.  Direct multiplication confirms
\(W^3=0\) and \(\det(I-zW)=1\).  The unsigned SFT zeta, parent quotient,
factor-orientation object \(1-z\), and Lefschetz convention \(1/(1-z)\) remain
clearly separated.

Bipartiteness forces period \(2k\); the source-locked constant edge multiplier
gives \(|\Lambda_u|=2^k\) and \(L=k\log2\).  Therefore the only
rational-prime hit is \(p=2\), and

\[
 Z_u(s)=\det(I-2^{-s/2}A)^{-1}
       =(1-2^{1-s})^{-1},\qquad \operatorname{Re}s>1,
\]

with the stated meromorphic continuation.  The paper consistently excludes
the nonlinear parent derivative cocycle from this result.

## Compilation, presentation, citations, and artifact integrity

- `paper_round2.pdf` is byte-identical to the current `manuscript.pdf`:
  SHA-256 `3cc1f56d8bc82ff3776b7b6578fcd689aaa0c1d2e4a532397fad66b4774655b7`.
- Independent `pdflatex` compilation completed without an error.  The retained
  production log has no undefined citation/reference, overfull/underfull box,
  or multiply-defined-label warning.
- The PDF has 17 letter-size pages.  All listed fonts are embedded; there is no
  encryption, suspicious form, or JavaScript content.
- Visual inspection of the title/abstract, both pages of Lemma 3, the moved
  audit figure, and the bibliography found no clipping, collision, or
  unreadable element.  Figure 3 now sits with the reproducibility passport and
  no longer interrupts the discussion.
- The previous dangling `period- 2k` and `length- m` renderings are gone.
- The Bowen--Lanford entry now renders as “R. Bowen and O. E. Lanford, III.”
- The bibliography contains the 17 audited entries, including de Melo--van
  Strien.  The citation supports the proof class used here, although more
  precise chapter/theorem pointers would help readers audit the proof quickly.
- All 89 unit/integration tests pass independently (`89 passed`).
- `sha256sum -c results/REPORT.sha256` reports **OK for every listed frozen
  artifact**, including the source lock, exact ledger, parent audit, all three
  floating splits, analyses, reports, and final manifest.
- The manuscript numbers remain consistent with the frozen artifacts: six
  exact gates, three sets of \(16{,}777{,}216\) roundtrip checks, maximum error
  \(1.388\times10^{-16}\), 100-digit parent audit, maximum residual
  \(9.706\times10^{-98}\), primitive vector through 20, and total 226.

## Minor revisions recommended

1. **Name the interval property in the cylinder proof.**  In the sentence
   following equation (17), change “nonempty compact cylinder” to “nonempty
   compact interval,” optionally adding that it is obtained by the unique
   monotone inverse branch along the word.  This makes the later invocation of
   a nondegenerate interval completely explicit.

2. **Add precise source pinpoints for the proof chain.**  The generic book
   citation is substantively appropriate, but the key all-period lemma would
   be easier to verify if it identified the homterval lemma (Chapter II,
   Lemma 3.1 in the checked edition) and the relevant no-wandering and
   negative-Schwarzian basin results by chapter/theorem or page.  This is a
   citation-quality improvement, not a missing hypothesis.

No new experiment, weakened claim, or third review round is required for
technical correctness.

## Final recommendation

**PASS_WITH_MINORS.**  The manuscript now contains a valid all-period proof of
the sole boundary quotient.  It is technically ready for circulation or
submission as the narrow specialist note it claims to be.  Its venue ceiling
remains driven by theorem depth and scope, as the previous reviews noted, not
by a correctness defect.
