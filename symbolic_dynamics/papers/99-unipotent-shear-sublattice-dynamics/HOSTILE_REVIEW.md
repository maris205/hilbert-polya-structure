# Internal hostile review — P99

Audit date: 2026-08-29 UTC
Disposition: **internal GO after repair / external HOLD**

Round 1 was a from-scratch reconstruction by the drafting agent.  Round 2 was
a separate, strictly read-only audit by the stochastic candidate scout,
followed by an integrating repair pass.  Both are team-internal review, not
external peer review.  No worldwide novelty or Hecke-priority conclusion is
licensed.

## Round 1 — proof reconstruction from the lattice action

This pass ignored the displayed theorem chain and rebuilt it from the
definition of an index-`N` subgroup.

- Projection to the second coordinate gives `c Z`; horizontal intersection
  gives `a Z x {0}`.  Choosing a vector above `c` and reducing its first
  coordinate modulo `a` proves existence and uniqueness of
  `L(a,b,c)`, while its determinant gives `ac=N`.
- Left multiplication by `U` sends the basis columns to `(a,0)` and
  `(b+c,c)`.  Thus the invariant `a`-layer is literally translation by
  `c=N/a` on `Z/aZ`; there is no row/column or left/right orientation swap.
- A translation by `c` on `Z/aZ` has `g=gcd(a,c)` cycles of length `a/g`.
  The fixed condition after time `n` is `a | nc`; after dividing by `g`,
  coprimality makes it equivalent to `a/g | n`.
- The finite-permutation identity
  `F(n)=sum_{m|n} m C(m)` gives the stated Möbius inversion.  Summing one
  geometric logarithm per cycle gives every Artin--Mazur zeta factor with
  the recorded sign and exponent.
- For `N=p^r`, direct substitution at layer `j` gives
  `g_j=p^min(j,r-j)` and periods `1` or `p^(2j-r)`.  The fixed condition is
  exactly `2j<=r+v_p(n)`, including `p=2`, `r=1`, coprime times, and
  saturation when `v_p(n)>=r`.
- The `a=N,c=1` layer is one `N`-cycle.  Since every layer period is at most
  `a<=N`, equality forces that same layer, proving both maximality and
  uniqueness.  The `N=1` endpoint survives unchanged.

### Round 1 findings and repairs

1. **MAJOR — zeta recovery was correct but too compressed.** The proof now
   displays `z (d/dz) log zeta_N(z)=sum_n F_N(n) z^n`, so recovery from the
   formal series is coefficientwise and does not depend on a chosen rational
   factorization.
2. **MINOR — permutation status was implicit.** The introduction now states
   `U in SL_2(Z)` before calling `T_N` a permutation.
3. **MINOR — bibliographic precision.** The subgroup-zeta owner is recorded
   as `G. C. Smith`, matching the publisher/archive metadata.

No formula or theorem conclusion was withdrawn in Round 1.

## Round 2 — quantifier, evidence, owner, and presentation attack

The independent second reviewer reread the frozen package, reran the control,
and checked every universal quantifier while separating what the program
actually tests from what the proof establishes.

- General formulas quantify over `N,n,m>=1`; empty cycle sums are allowed.
  The prime-power theorem separately assumes prime `p` and `r>=1`.
- Möbius reconstruction is integral because it reconstructs actual cycle
  counts; the program also checks the numerator's divisibility before every
  division.
- The valuation staircase changes at parity-matched thresholds: nontrivial
  period exponents are `1,3,...,r` for odd `r` and `2,4,...,r` for even `r`.
  Direct checks use two times with the same valuation, preventing a hidden
  dependence on the coprime unit.
- The recovery theorem uses the complete temporal data.  It makes no claim
  that the state count `sigma_1(N)` alone is injective.
- The script's cycle walk is independent of the gcd inventory, and its fixed
  walk enumerates every phase rather than reusing the divisor sum.  The zeta
  evidence is the exact equality between literal cycle exponents and all
  tested logarithmic fixed coefficients.
- The initial PDF was inspected page by page.  The table fits the text block,
  theorem continuations are readable, proof terminators are present, and no
  display or reference is clipped.

### Round 2 findings and repairs

1. **MAJOR — one control sentence outran the artifact.** The abstract
   originally said that the program independently enumerated “all lattices.”
   It now says that it enumerates every canonical phase and independently
   traces its orbit.  Exhaustiveness of HNF is proved analytically, not
   delegated to the program.
2. **MINOR — the evidence ledger still over-attributed uniqueness to the
   program.** `CLAIMS_EVIDENCE.md` now says explicitly that the program checks
   coordinate constraints and basis containment, whereas HNF uniqueness is
   analytic.
3. **MINOR — HNF convention could be misread.** The paper now displays
   `H(a,b,c)=[[a,b],[0,c]]` and states that `(a,0),(b,c)` are its columns.
   The proof also displays the left product `U H`; Section 6 now describes
   raw-column action, residue reduction, and mutual containment rather than
   saying that canonicalization is independent.
4. **MINOR — parity jumps were only described implicitly.** The final text
   lists the staircase jumps at `s=1,3,...,r` for odd `r` and
   `s=2,4,...,r` for even `r`.
5. **MINOR — endpoint regression coverage.** The frozen controls explicitly
   include `N=1`, `p=2`, `r=1`, six hand-entered inventories, and the first
   eight fixed counts at `N=8`.
6. **MINOR — page-1 theorem continuation.** The abstract and owner paragraph
   were tightened so Proposition 2.1's full statement stays together; no
   mathematical content or ownership caveat was removed.
7. **MAJOR RELEASE GATE — direct-owner coverage remains incomplete.** The
   three positive references own the general HNF, subgroup-zeta, and
   periodic-zeta mechanisms, but they are not a recent direct owner for this
   unipotent Hecke-coset temporal census.  The existing external HOLD is
   therefore retained without dilution.

No critical or major mathematical error remained after Round 2.

## Bounded owner audit

Publisher or institutional records were checked for all three cited owners:

- Cohen, *A Course in Computational Algebraic Number Theory*, GTM 138,
  DOI `10.1007/978-3-662-02945-9`, for lattice/HNF background;
- Grunewald--Segal--Smith, *Inventiones Mathematicae* 93 (1988), 185--223,
  DOI `10.1007/BF01393692`, for finite-index subgroup counting and subgroup
  zeta functions; and
- Artin--Mazur, *Annals of Mathematics* 81 (1965), 82--99,
  DOI `10.2307/1970384`, for periodic-point zeta terminology.

A bounded search through 2026-08-29 found standard HNF enumeration and the
classical modular/Hecke coset action on determinant-`N` matrices, but did not
identify a primary source packaging this exact shear's divisor-layer cycle
census, valuation staircase, finite zeta, and recovery theorem together.
Search absence is not proof of novelty or priority.

## Residual risks and verdict

- **Mathematics:** low after two complete derivations and exhaustive finite
  controls in the declared range.
- **Reproducibility:** low; all theorem-facing probes use deterministic exact
  integer arithmetic and the stored output is byte-comparable.
- **Scope:** low after explicitly excluding higher rank, random walks,
  asymptotic orbit statistics, and Hecke-algebraic organization.
- **Literature/priority:** medium because the action is natural in the
  classical Hecke-coset setting and an older computation may use different
  language.
- **Verdict:** GO for internal Stage 2 use; HOLD for public release,
  submission, contact, or priority language pending specialist review.
