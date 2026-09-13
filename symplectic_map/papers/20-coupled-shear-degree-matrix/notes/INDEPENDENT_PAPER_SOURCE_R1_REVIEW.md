# Paper20 — Independent Manuscript-Source R1 Review

**Review ID:** `PAPER_SOURCE_R1_2026_08_22`

**Scope:** repaired, author-stopped manuscript source only.  This is a
read-only review: I did not compile TeX, run BibTeX, run CAS or numerical
experiments, access transport, build downstream artifacts, or modify any
bound author file.  This note is reviewer-owned and is outside the locked
ten-file author aggregate.

## Reviewed identities and deterministic metadata

The current repaired source files were independently read and hashed:

| file | bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 37,423 | 981 | `2a27dc745bffa7c9efb2016edb416045216d9fcd8bad7beadf9143716eee2014` |
| `paper/math_commands.tex` | 702 | 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,331 | 73 | `5bd232714f5875a97c368342bbb978ee4cadda5893ce23c9af092c8895840774` |
| `paper/BUILD_METADATA_R0.json` | 3,588 | 1 | `1ac4fa5c1f3e575f5e09c4a3e311f4a59854a674585c92d80df4434a47605446` |

The upstream plan remains 22,064 bytes/LF397 with SHA
`4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3`.  The
source lock remains 11,847 bytes/LF1 with SHA
`57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581`.
All reviewed files are regular mode 0644, UTF-8, LF-only, and contain no CR,
BOM, or NUL bytes.  The metadata JSON and source lock each pass strict
duplicate-key-free, finite-number, recursively sorted-key, compact-JSON,
single-terminal-LF round-trip checks.  Their self-identity fields remain
explicitly null and excluded.  Every `source_files` row in the updated
`BUILD_METADATA_R0.json` matches the on-disk bytes, lengths, and hashes.

Reapplying the frozen ten-author-file framing (big-endian name/content lengths
over byte-sorted relative paths) independently gives 10 files, 45,416 total
bytes, 873 LF, and aggregate SHA
`3b27fe493832559e90ac5dcb059628492074574fe9492d12e500f7da107f7e90`.
The repaired manuscript and this review are downstream/out-of-band and do not
enter that aggregate.  No forbidden `aux`, `bbl`, `blg`, `log`, `pdf`, build,
transport, results, or figures output is present.  Metadata still reports
build, CAS, experiment, data, figure, publication, transport, and upload
permissions as false; build status is `NOT_RUN`.

## Equation-label repair and source-level cross-reference checks

The prior unnumbered-display defect is absent in this identity.  The four
displays referenced by proof text are now literal numbered `equation`
environments:

`eq:Sface`, `eq:Tfirstgap`, `eq:Tface`, and `eq:Tsecondgap`.

The unused `eq:ratiomap` label was removed rather than leaving an unnumbered
label.  A source parser finds 40 unique labels and 43 `ref`/`eqref` uses, with
zero missing targets and zero duplicate labels.  Each of the four selector-gap
labels is in an equation environment, and all seven citation keys used by
`main.tex` occur exactly once in the bibliography key set.  Environment and
brace nesting is balanced.  These are source checks only; no compilation was
performed.

## Theorem and proof replay

The manuscript agrees with the locked theorem over an algebraically closed
field (K) of characteristic zero, for every integer (g\ge5):

\[
 V=q_1^2q_2^2+q_1^g,\qquad W=p_1^2p_2^2+p_2^g,
 \qquad F_g=T\circ S,
\]

with (S(q,p)=(q,p+\nabla V(q))) and
(T(q,p)=(q+\nabla W(p),p)).  The displayed coordinate formulas have the
correct gradients and preserve the phase order.  The literal selector rows
are

\[
 A_g=\begin{pmatrix}g-1&0\\2&1\end{pmatrix},\qquad
 B_g=\begin{pmatrix}1&2\\0&g-1\end{pmatrix},\qquad
 C_g=B_gA_g=\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix}.
\]

The proof checks the required gates in the correct dependency order:

1. The triangular inverse formulas and symmetric-Hessian pullbacks establish
   polynomial automorphism and symplecticity.
2. For (r=u_2/u_1\in[1,(g-2)/2)), the (S)-phase gap
   (u_1+2u_2<(g-1)u_1) selects the (q_1^g) face, while the second row is
   (2u_1+u_2).
3. With (v=A_gu), the (T)-phase uses
   (v_2/v_1=(2+r)/(g-1)\ge3/(g-1)>2/(g-2)), so the (p_2^g) face is
   strict; both carried (q)-coordinate gaps are displayed.
4. The complete-step ratio map
   (f_g(r)=(g-1)(2+r)/(g+3+2r)) is increasing,
   (f_g(1)>1), and its upper-endpoint gap is (g(g-4)>0).  The manuscript
   also proves (C_gu>u) componentwise and keeps the phase-return equality
   (v_{n+1}=A_gu_n) explicit rather than using a false single strict cone.
5. All carried (p)- and (q)-terms are covered at the base step and by the
   induction.  Coefficients remain nonnegative integers, selected terms have
   positive coefficients, and characteristic zero plus strict gaps gives the
   claimed no-cancellation result without asserting unique monomial paths.
6. The exact phase recurrence is
   (v_{n+1}=A_gu_n, u_{n+1}=C_gu_n).  Since
   (C_g-A_g=\bigl(\begin{smallmatrix}4&2\\2g-4&g-2\end{smallmatrix}\bigr)>0)
   and the cone gives (u_{n,2}>u_{n,1}) for (n\ge1), (q_2) is the
   maximal coordinate degree and
   \(\deg(F_g^n)=e_2^{\mathsf T}C_g^n(1,1)^{\mathsf T}\).
7. Trace (2g+2), determinant ((g-1)^2), and discriminant (16g) give
   eigenvalues ((\sqrt g\pm1)^2).  Positivity of (C_g), together with the
   positive initial vector and visible (e_2), justifies the Perron limit
   \(\lambda_1(F_g)=\rho(C_g)=(\sqrt g+1)^2\).

The scalar Cayley–Hamilton recurrence and the factorization
\((g-1)^2-(\sqrt g+1)^2=\sqrt g(\sqrt g-2)(\sqrt g+1)^2>0\) are consistent.
The (g=5) matrix audit is also correct.  No half-step matrix is promoted to
the complete-step theorem matrix.

## Citations, collision boundary, and anti-claims

All seven bibliography keys resolve: Friedland–Milnor, Déserti,
Guedj–Sibony, Favre–Jonsson, Dang–Favre, Fujioka et al., and the explicitly
secondary Hénon survey.  Their uses remain bounded to planar degree-product
background, higher-dimensional degree-growth context, dynamical-degree
spectral terminology, historical valuation context, and a neighboring
four-dimensional coupled-Hénon hyperbolicity object.  No citation is used as
proof of the displayed recurrence, symplecticity, selectors, no-cancellation,
Perron root, or priority.

The P12–P19 table is explicitly a bounded collision ledger rather than an
exhaustive priority search.  The manuscript retains all locked anti-claims:
no arbitrary supports/words/coefficients, no positive-characteristic result,
no generic finite-Newton-fan or all-symplectic-map theorem, no topological or
arithmetic entropy equality, no periodic/trace/centralizer/torus theorem, no
universal product non-conjugacy, no numerical/CAS proof certificate, and no
firstness or absolute novelty claim.  The “non-product” wording is restricted
to the displayed support split and strict degree comparison.

## Non-blocking editorial notes

For a later polish pass, define (e_2=(0,1)^{\mathsf T}) explicitly near its
first use and standardize component notation (`u_{n,1}` versus `u_{1,n}`) in
the old-term proposition and visibility lemma.  The broad introductory
citation bundle could also move the Favre–Jonsson citation to its explicitly
historical paragraph, but the current text already states that role and does
not make it proof authority.  None of these observations changes the locked
theorem or blocks this source-only review.

The repaired source is therefore internally consistent and eligible for the
next authorized review/build gate only; this review does not authorize
compilation, publication, transport, upload, or release.

PAPER_SOURCE_R1_PASS
