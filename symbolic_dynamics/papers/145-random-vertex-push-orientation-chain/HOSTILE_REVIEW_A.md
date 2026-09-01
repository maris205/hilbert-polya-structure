# Hostile review A — round 1

## Decision

**REVISE.** I found no counterexample to the orbit-size, spectrum, return-law,
period, or known-\(n\) component-order inverse statements.  The present paper is
nevertheless not acceptable in its current ownership and reproducibility form.
The connected-component chain is a folded-hypercube walk in an unexposed
coordinate system, and prior folded-hypercube sources already contain the
corresponding character spectrum and bipartiteness boundary.  This is a direct
owner hit on most of the advertised package, not merely adjacent background.
In addition, the inverse verifier chooses factors from the ground-truth
partition instead of recovering them from the spectral polynomial, while two
advertised root controls reduce to assertions of their own hypotheses.

The component-order inverse may remain as the residual theorem after an honest
folded-hypercube subtraction and a repaired owner search.  A bounded search did
not locate a direct prior source for that inverse; this non-hit is **not**
novelty, priority, or clearance evidence.  `HOLD_EXTERNAL` must remain.

## Severity-ranked findings

### S1 — blocking ownership omission: the component walk is a folded hypercube

For a connected component \(C\) of order \(s\), choose a pivot vertex and use
the representative whose pivot coordinate is zero.  There is then an explicit
quotient identification

\[
 \mathbb F_2^C/\langle\mathbf 1_C\rangle
 \cong \mathbb F_2^{s-1},\qquad
 [e_i]\mapsto e_i\ (i\ne *),\qquad
 [e_*]\mapsto \mathbf 1_{s-1}.
\]

Thus the generator set is the \(s-1\) coordinate vectors together with the
all-ones vector: this is exactly the standard Cayley presentation of the
folded hypercube \(FQ_{s-1}\).  If a character of
\(\mathbb F_2^{s-1}\) has Hamming weight \(r\), the unnormalised component
eigenvalue is

\[
 (s-1)-2r+(-1)^r.
\]

For even \(r=k\) this is \(s-2k\); for odd \(r=k-1\) it is again
\(s-2k\).  Pascal's identity combines the two multiplicities as
\(\binom{s-1}{k}+\binom{s-1}{k-1}=\binom{s}{k}\), for even \(k\).
This is precisely the connected factor \(B_s\) in `main.tex:80-86` and
`main.tex:181-196`, not a new graph family or a merely generic application of
finite-group Fourier analysis.

The following primary/official records were missing from both
`SOURCE_VERIFICATION.md` and `references.bib`:

- Ying Xu and Jixiang Meng, “On the Folded Hypercube and Bi-folded
  Hypercube,” *Ars Combinatoria* 92 (2009), 3–9.  Its Cayley presentation and
  Theorem 2.3 give the folded-hypercube spectrum by character methods.  See the
  [publisher record](https://combinatorialpress.com/ars-articles/volume-092-ars-articles/on-the-folded-hypercube-and-bi-folded-hypercube/)
  and [publisher PDF](https://combinatorialpress.com/article/ars/Volume%20092/volume-92-paper-1.pdf).
- Jun-Ming Xu and Meijie Ma, “Cycles in Folded Hypercubes,” *Applied
  Mathematics Letters* 19(2) (2006), 140–145,
  DOI `10.1016/j.aml.2005.04.002`.  Its stated bipartiteness boundary for
  \(FQ_m\) is \(m\) odd, which becomes \(s\) even under \(m=s-1\).
  See the [publisher record](https://www.sciencedirect.com/science/article/pii/S0893965905002065).
- Hong Chen, Xiaoyan Li, and Cheng Kuan Lin, “Random Walks on the Folded
  Hypercube,” *Journal of Internet Technology* 20(6) (2019), 1987–1994,
  DOI `10.3966/160792642019102006027`.  This is direct prior random-walk
  literature on the same named factor family; it further defeats an
  owner-thin presentation.  See the [official institutional record](https://scholar.nycu.edu.tw/en/publications/random-walks-on-the-folded-hypercube/).

This does not show that any one of these papers owns the component-order
inverse.  It does show that the orbit/spectrum/period/return package cannot be
presented with only vertex-push and generic Fourier sources, as currently done
in `main.tex:64-72` and `SOURCE_VERIFICATION.md:7-23`.

**Required fix.** Add the displayed quotient-to-\(FQ_{s-1}\) identification as
an explicit proposition.  Describe the full disconnected chain as the
degree-weighted Cartesian-product kernel

\[
 P_G=\sum_{i:s_i\ge2}\frac{s_i}{n}
       (P_{FQ_{s_i-1}}\otimes I_{\ne i})
       +\frac{m_1}{n}I,
\]

where \(m_1\) is the number of isolated vertices.  State separately that
\(s=2\) has two labelled vertex choices producing the same nonzero quotient
generator (the normalised kernel agrees with the usual \(FQ_1\) walk), and
\(s=1\) contributes an identity move.  Cite and assign zero contribution
credit to the folded-hypercube spectrum, bipartiteness/cycle, and random-walk
literature.  Reframe the return formula as the spectral-moment consequence of
this known factor spectrum.  Restrict any residual emphasis to the
component-order inverse and its exact boundary.  Do not describe the bounded
inverse owner-search non-hit as evidence of novelty.

### S2 — major reproducibility defect: “factor peeling” uses the answer

`inverse_controls()` constructs `compressed` from the known partition and then
loops over

```python
for size in sorted((s for s in part if s >= 2), reverse=True):
    remainder = divide_exact_integer(remainder, even_factor(size))
```

(`verify_p145.py:288-318`).  This checks that factors used to construct a
product divide that product.  It does **not** implement the claimed inverse,
does not identify the largest component from \(Q\), and does not test that
factor multiplicity is recovered from the nearest root.  The fixed-total
signature-injectivity check through total 30 is useful independent pressure,
but it is a different control.  Consequently `CONTROL_RESULTS.md:33-40` and
`main.tex:348-350` overstate the evidence when they call these divisions
“factor peeling.”

The advertised root controls have the same problem.  “Strict nearest-root
order” is implemented only as `CHECK.true(smaller < size, ...)`, and the
“no-smaller-factor collision” loop checks only that
`smaller != size * (2*j+1)` (`verify_p145.py:321-341`).  Neither control
constructs a root, evaluates an \(E_r\) at an algebraic root of \(E_s\), or
recovers a factor from input data.  These are executable restatements of the
proof's already assumed integer inequalities, not independent tests of the
root argument.

**Required fix.** Choose one of the following, and make the manuscript and
control ledger agree exactly:

1. Implement a deterministic recovery routine whose only mathematical inputs
   are `(n, Q)`, which outputs the component-order multiset, including isolates;
   test that routine on every partition in the stated range.  The routine must
   not inspect `part` or an equivalent ground-truth factor list when deciding
   which factor to remove.  If roots are used, retain an exact algebraic
   comparison/certification rather than silently introducing floating point.
2. Or remove “factor peeling,” “strict nearest-root order,” and
   “no-smaller-factor collision” from the claimed computational coverage and
   relabel the present checks honestly as fixed-total signature enumeration,
   squarefreeness, exact known-factor division, and integer consistency checks.

The all-parameter proof in `main.tex:245-308` is logically sufficient and does
not depend on this finite control, so this defect requires evidence repair, not
withdrawal of the inverse theorem.

### S2 — major presentation defect: disconnected factors, loops, and labelled
generator multiplicities are hidden

The quotient proof itself is correct for disconnected graphs, but the current
presentation jumps from the abstract quotient to a product polynomial.  It
never states the actual product-kernel normal form.  This matters for both
ownership and edge cases:

- an isolated vertex gives \([e_v]=0\), hence a self-loop with probability
  \(1/n\);
- in a component of order two the two labelled vertex choices give the same
  quotient translation;
- for several components, the global chain is not an unweighted product of
  simple graphs but the weighted sum of component kernels displayed above.

The phrases “transition spectrum” and “folded-hypercube spectrum” can otherwise
be misread as ordinary simple-graph adjacency spectra, where low-dimensional
parallel-generator conventions differ.

**Required fix.** State the labelled-generator Markov kernel, the isolate loop
weight, the \(s=2\) degeneration, and the weighted-product formula before using
component spectra.  Explicitly distinguish transition-matrix eigenvalues from
unnormalised simple-graph adjacency eigenvalues.  Keep the known-\(n\)
hypothesis in every inverse statement.  Add the sharp necessity witness that
all-edgeless graphs, for all positive ambient orders, have the same one-state
transition spectrum \(\{1\}\) if \(n\) is not supplied.

### S3 — minor control overstatement: the \(P_4/K_4\) witness is tautological

`boundary_controls()` calls `component_product((4,))` twice and compares the
two returned tuples (`verify_p145.py:344-350`).  It does not construct \(P_4\)
or \(K_4\), derive either transition kernel, or compare two independently
computed spectra.  The mathematical witness in `main.tex:317-323` is valid,
but the count “Explicit nonidentifiability witnesses: 2” in
`CONTROL_RESULTS.md:30` is not fully supported by the implementation.

**Required fix.** Either construct both graphs and compare independently
derived labelled-generator transition spectra, or rename this assertion as a
formula-level adjacency-invariance sanity check and reduce the explicit-witness
claim accordingly.  The affine-orbit conjugacy check at
`verify_p145.py:352-378` is a genuine constructed witness and may remain.

### S3 — minor wording issue: starting orientation is not a spectral inverse
target

The claim that the transition spectrum does not determine the starting
orientation is true, and the affine translation argument is correct.  But a
transition matrix spectrum ordinarily contains no marked initial state at all.
As phrased in the abstract and main theorem (`main.tex:56-57`,
`main.tex:105-107`), this sounds like a substantive inverse boundary when it is
mostly a category distinction.

**Required fix.** Say explicitly that all push orbits carry conjugate
translation kernels, so neither the unmarked chain nor its spectrum records a
chosen orientation or affine orbit.  Keep internal adjacency as the substantive
nonidentifiability boundary.

## Hostile mathematical audit: claims that survived

I specifically attempted the failure modes named for this review and found no
mathematical counterexample.

1. **Orbit size on disconnected graphs.**  The cut map satisfies
   \(\ker\delta=\operatorname{span}\{\mathbf1_{C_i}\}\), including
   singleton components.  The component indicators are independent, so the
   image and every push orbit have size \(2^{n-c}\).  Isolates act trivially
   rather than creating extra orbit states.
2. **Fourier multiplicities and return law.**  Dual characters are exactly the
   sign assignments having an even number of minus signs in every component.
   Their weight enumerator is \(\prod_i B_{s_i}\), its coefficient sum is
   \(2^{n-c}\), and distinct \(k\) give distinct values
   \((n-2k)/n\).  Character orthogonality gives the stated diagonal return
   probability, with the labelled-generator multiplicities and isolate loops
   already included.
3. **Period.**  If every component order is even, coordinate parity descends to
   the quotient, every push flips it, and a two-step return exists.  If an odd
   component exists, its all-vertex relation is an odd closed walk; together
   with a two-step return it gives period one.  For an isolated vertex this odd
   walk is the one-step loop.  Hence “period two iff all component sizes are
   even” is correct.
4. **Known-\(n\) spectral inverse.**  The spectrum recovers \(M_G\) because
   the eigenvalue labels are distinct when \(n\) is known.  The cosine
   factorisation gives simple negative roots of \(E_s\); the nearest root
   \(-\tan^2(\pi/(2s))\) moves strictly toward zero with increasing
   \(s\), and no smaller factor shares it.  Therefore the nearest root of the
   remaining product identifies the largest remaining nontrivial component and
   its multiplicity.  Repetition recovers all orders at least two; because
   \(E_1=1\), the known total recovers the number of isolates.  The proof is
   correct, including the all-isolate case \(Q=1\).

These passes are mathematical findings only.  They do not cure the ownership
or evidence defects above.

## Reproducibility and artifact inspection

- From the paper directory I reran
  `PYTHONDONTWRITEBYTECODE=1 python3 verify_p145.py | cmp - verification_output.txt`.
  It exited with status 0 and reproduced `status=PASS` byte for byte.
- The frozen run reports 1,099 labelled graphs through order 5, 14,149 orbit
  states, 71,874 return-recurrence state cells through time 6, 28,628
  fixed-total component partitions through total 30, 144,024 known-factor
  divisions, and **473,328 exact assertions**.
- `main.pdf` is a clean four-page A4 build.  The log contains no undefined
  references/citations, LaTeX warnings, or overfull/underfull box reports.  The
  PDF has blank author/title metadata and embedded fonts.
- `main.pdf` and `main_round0_original.pdf` are byte-identical, both with SHA-256
  `abf75d832a1bd874ce31155d8c71e55e8cf3bb23f17029b82b6a88e645a49dea`.
- The current bibliography has only three items (Pretzel, Klostermeyer, Terras)
  and therefore does not cover the direct folded-hypercube owners above.

## Acceptance gate for the next round

I would change the decision to **ACCEPT** only after all of the following are
visible in the revised artifacts:

1. the folded-hypercube quotient and weighted-product normal form, including
   \(s=1\), \(s=2\), and transition-versus-adjacency conventions;
2. primary citations and zero-credit subtraction for the known folded-cube
   spectrum, bipartiteness/cycles, and random-walk lane;
3. residual positioning centered on the known-\(n\) component-order inverse,
   with `HOLD_EXTERNAL` and no novelty language;
4. either a genuine input-only exact inverse recovery control or a precise
   downgrade of the present control claims;
5. a repaired or honestly relabelled \(P_4/K_4\) computational witness; and
6. a fresh canonical transcript, assertion ledger, clean build, and preserved
   round-zero PDF after the textual/source changes.
