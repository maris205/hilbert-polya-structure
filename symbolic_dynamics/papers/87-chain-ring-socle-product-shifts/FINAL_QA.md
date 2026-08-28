# Final QA

Release audit date: 2026-08-28 UTC.

## Result

- Decision: **GO; INTERNAL FREEZE; EXTERNAL HOLD**
- Proof status: **PROVABLE IN THE CORRECTED MANUSCRIPT**
- Independent hostile audit: **2/2 rounds complete**
- Exact control: `ALL EXACT CONTROLS PASSED: 700,499 assertions`
- Build: four-stage `pdflatex / bibtex / pdflatex / pdflatex` completed
- `latexmk`: unavailable; fallback is documented in `BUILD.md`
- PDF: `main.pdf`, 5 pages, 313,957 bytes, A4, PDF 1.5
- Undefined references: 0
- Undefined citations: 0
- LaTeX warnings on final pass: 0
- Package warnings on final pass: 0
- Overfull boxes: 0
- Underfull boxes: 0
- Fonts: 24/24 embedded; all are subsetted and Unicode-mapped
- Source markers: no unresolved `TODO`, `FIXME`, `XXX`, or verification marker
- Bibliography: 7 cited keys and exactly 7 entries
- PDF text extraction: nonempty and complete through the references
- Visual inspection: all five pages checked; no clipping, collision, broken
  equation, or stray text
- SHA-256: `c642f7ac4f95d5181b01b852a4550e2c88cbc9193fd38497a97fa05c82aebfd0`

## Mathematical release checks

- The socle is explicitly defined as `Ann_R(m)` and proved equal to `m^a`.
- The product rule handles every valuation pair and distinguishes a nonzero
  socle product from the zero-product threshold.
- The rank proof accounts for the full zero eigenspace, not only the
  `(a+1) x (a+1)` quotient.
- All SCCs have the same Perron value; no component is silently discarded in
  the entropy or MME count.
- The parity statement is correctly scoped: the full SFT is reducible for
  `a>=2`, while `a=1` is irreducible of period two; the existence of a mixing
  maximal component changes with parity.
- Fixed counts include all odd and even periods; zeta and least-period orbit
  counts follow from the same spectrum.
- Four-period recovery treats even and odd `a` separately and proves
  uniqueness of `q`.
- Ring collapse is an explicit layerwise one-block conjugacy; nonisomorphism
  is witnessed by different characteristics in the concrete family.

## Ownership and release scope

The manuscript positively cites the classical finite-chain-ring sources,
Anderson--Livingston for zero-divisor graphs,
Rattanakangwanwong--Meemark for the closest chain-ring zero-product spectral
work, Dolžan for fixed-product matrices over finite local rings,
Bowen--Lanford for the finite-type zeta determinant, and Parry for the
intrinsic Markov measure.  The boundary relation, vertex set, loop convention,
and sum over nonzero socle product fibres are explicitly distinguished.  The
bounded negative search is dated and does not claim absolute priority.
External release remains `HOLD` pending specialist clearance.
