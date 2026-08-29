# Independent cross-hostile review B — P102

Audit date: 2026-08-29 UTC.  This is a team-internal closure ledger, not an
external referee report; no reviewer identity, endorsement, novelty
certificate, or priority conclusion is implied.

Verdict: **RELEASE HOLD**.  The theorem package is **GO for internal use after
the repairs below**, with 0 fatal mathematical findings, 0 unrepaired major
mathematical findings, 2 repaired minor findings, and 1 unresolved major
literature/release gate.

## From-scratch proof attack

The review reconstructed the map before consulting the control output.

1. Commutativity gives `(aa*)*=aa*`; hence the first image is involution
   fixed and every later step is squaring.  With the stated DFT sign,
   `widehat(a*)_j=widehat(a)_{-j}`.  Self-inverse characters therefore carry
   `z -> z^2`, while a two-character orbit carries
   `(u,v) -> (uv,uv)`.  This independently recovers the iterate formula.
2. A positive-iterate fixed pair must be diagonal.  Both block types then
   reduce to `z^(2^k)=z`, with one zero root and
   `gcd(2^k-1,q-1)` nonzero roots.  Independence over the `o=(n+s)/2`
   inversion orbits gives the displayed fixed sequence with the correct
   exponent and no missing first-image factor.
3. Writing `q-1=2^alpha m`, scalar squaring removes exactly one factor of two
   from the multiplicative order per step.  The pointwise distinction that
   controls the depth is

   ```text
   self z:       depth = d_q(z)
   pair (u,u):   depth = d_q(u)
   pair (u,v), u != v: depth = 1 + d_q(uv).
   ```

   Thus only a genuinely nondiagonal pair contributes the synchronization
   level.  A primitive scalar attains `alpha`; `(1,gamma)` attains
   `alpha+1` when a pair exists.  This includes `n=1,2`, `alpha=0`, and the
   characteristic-two split cases.
4. On `{0} union mu_m`, squaring is a permutation of order `ord_m(2)` (with
   the declared `m=1` convention).  Möbius inversion therefore gives the
   least-period ledger, and multiplying one `(1-z^k)^(-1)` factor per cycle
   gives the finite zeta product with the stated signs.
5. The recovery proof survives both ambiguous branches.  `F_1=2^o`, the
   maximum root count recovers `m`, and `2o=n+gcd(n,2)` leaves only
   `2o-1` and `2o-2`.  For `o=2`, simultaneous survival would force
   `q_2=r^3`, `q_3=r^2`, and
   `(r-1)(r^2-r-1)=0`, impossible for an integer `r>=2`.  For `o>=3`, both
   candidates have the same synchronization correction and distinct positive
   exponents of the same field size, so the phase-size equality separates
   them.

## Findings and implemented repairs

### MINOR 1 — self/pair depth distinction was only implicit

The maximum-depth proof was correct, but the sentence “a paired block becomes
diagonal after one step” could be read as charging an extra step even to a
pair that was already diagonal and periodic.  The proof now states the exact
pointwise piecewise depth formula above and explains why the extra level is
exclusive to nondiagonal pairs.  No theorem value changed.

### MINOR 2 — missing internal collision firewall against P86

P86 uses the same elementary adjacent-product primitive.  The manuscript,
README, and claim ledger now disclose the boundary: P86 is a spatial
two-block factor of an iid process and studies support entropy and prediction
memory; P102 is a finite deterministic group-algebra map whose Fourier pair
synchronizes once and then squares.  The shared multiplication primitive is
not counted as a contribution.

### MAJOR RELEASE GATE — direct-owner coverage remains incomplete

Publisher records confirm the cited DOI metadata and the scope of the nearby
owners: Bovdi--Grishkov (`10.1017/S0013091518000500`) treat unitary and
symmetric units for a substantially narrower involution setting;
Qureshi--Reis (`10.1016/j.disc.2023.113393`) own general power-map functional
graphs; Terras owns finite-group Fourier analysis; and Artin--Mazur own the
periodic-point zeta construction.  A bounded exact-phrase and mechanism search
did not identify the whole-algebra map's exact temporal package, but search
absence is not novelty evidence.  A specialist direct-owner search is still
mandatory, so external release remains HOLD.

## Evidence and build replay

The post-repair verifier was rerun without numerical tolerances or random
seeds:

```text
cyclic group-algebra involution norm verification: PASS
literal_lanes=9
rigidity_lanes=85
assertions=116278
```

The literal coefficient lanes include all advertised prime and extension
fields and independently reconstruct the full functional graphs.  They agree
with Fourier reversal, iterate, fixed, recurrent, depth, cycle, and recovery
formulas.  These finite checks are falsifiers; the universal statements rest
on the proofs above.

The post-repair four-stage build
`pdflatex -> bibtex -> pdflatex -> pdflatex` passed.  The artifact is a
6-page A4 PDF of 328,565 bytes.  The final log and BibTeX log contain no
LaTeX/package warning, undefined citation/reference, multiply-defined label,
overfull/underfull box, or error.  All 24 font entries are embedded, subsetted,
and Unicode mapped.  `HOSTILE_REVIEW_B.md` is deliberately not a final QA or
hash manifest.

## Final disposition

- Mathematical package: **GO for internal Stage 2 use**.
- Control/reproducibility: **GO** within the declared finite lanes.
- Public posting, submission, specialist contact, novelty, or priority
  language: **HOLD** pending the direct-owner gate.
