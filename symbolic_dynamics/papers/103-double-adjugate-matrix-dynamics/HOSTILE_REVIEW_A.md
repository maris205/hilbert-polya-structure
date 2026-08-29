# Independent cross-hostile review A — P103

Audit date: 2026-08-29 UTC.  This is a second team-internal review of the
then-current repaired manuscript, independent of its author derivation and of
review B.  It is not an external referee report and confers no novelty,
priority, or release endorsement.

Verdict: **GO for internal Stage 2 use / HOLD for external release**.  Fatal
mathematical findings: 0.  Major mathematical findings: 0.  Major evidence
findings: 1, repaired.  Minor findings: 2, repaired.  The direct-owner gate
remains open.

## Theorem reconstruction

1. For invertible `A`, applying
   `adj(A)=det(A)A^(-1)` twice gives
   `Psi(A)=det(A)^(d-2)A`.  If `rank(A)<=d-2`, the first adjugate is zero;
   if `rank(A)=d-1`, it has rank one, whose adjugate is zero for `d>=3`.
   Thus every nonzero singular state has depth exactly one, with no missing
   rank endpoint or characteristic restriction.
2. If `delta=det(A)`, one step sends the determinant to
   `delta^alpha`, `alpha=(d-1)^2`.  The accumulated scalar exponent obeys
   `E_(k+1)=E_k+(d-2)alpha^k`, `E_1=d-2`.  Since
   `alpha-1=d(d-2)`, this gives exactly
   `E_k=(alpha^k-1)/d`; integrality follows from `alpha=1 mod d`.
3. Positive-iterate fixed singular matrices reduce to zero.  On `GL_d(q)`,
   fixedness is `delta^E_k=1`.  The determinant is onto and every fiber has
   `|SL_d(q)|` points, yielding
   `1+|SL_d(q)|gcd(E_k,q-1)`.  Finite-map Möbius inversion and one Euler
   factor per cycle give the cycle and zeta displays with the stated signs.
4. On a projective line through `A`, parameterized by `c`, direct substitution
   gives
   `Psi^k(cA)=delta^E_k c^(d E_k+1)A=delta^E_k c^(alpha^k)A`.
   Hence every line image has index `gcd(alpha^k,q-1)` and the full image has
   the displayed size plus the common singular image zero.
5. Prime by prime,
   `v_ell(gcd(alpha^k,q-1))=min(k v_ell(alpha),v_ell(q-1))`.
   The first saturated time is therefore the maximum of the displayed
   ceilings.  Starting the nested chain at
   `I_0=GL_d(q)` is essential: its first stable index is the maximum
   invertible tail depth.  If `t_*=0`, the restriction is already a
   permutation; the whole-space maximum remains one because of the singular
   basin.

## Findings and implemented repairs

### MAJOR EVIDENCE — the original controls never exercised `t_*>1`

The exhaustive matrix spaces had image stabilization time at most one, while
the four arithmetic signal lanes checked fixed points but did not check image
staircases.  Thus the universal valuation formula was analytically proved but
the advertised “registered gcd staircases” did not include a multi-step
example.  This was an evidence-chain overstatement, not a theorem error.

The exact verifier now has independent scalar-line image lanes at
`(q,d)=(5,4),(7,3),(17,3),(257,3),(19,4)`, realizing
`t_*=0,1,2,4,1`.  They literally iterate all nonzero scalars on the identity
line, compare every image size to the gcd formula, require strict loss before
`t_*`, equality from `t_*`, and check the saturated prime-power divisor.
These lanes add 82 substantive assertions.  The determinant signal lanes now
also compare the full matrix iterate and determinant exponents, adding 768
assertions.  The total rises from 140,340 to **141,190**.

### MINOR 1 — stabilization time had no explicit time-zero convention

The formula was right, but “the invertible image chain stabilizes first at
`t_*`” was ambiguous at the coprime endpoint.  The theorem now defines
`I_k=Psi^k(GL_d(q))` for `k>=0`, explicitly sets `I_0=GL_d(q)`, and the proof
separately handles `t_*=0`.

### MINOR 2 — internal collision boundary was too generic

The manuscript now names the closest internal mechanisms.  P99 has a
valuation staircase for a bijective unipotent action on fixed-index
sublattices, with no singular collapse or shrinking line.  P97 has a power
map on finite subsets of a prime cyclic group, not a full matrix-space map.
The shared valuation and power-map primitives are disclosed and receive no
separate contribution credit.

## Owner and scope audit

Publisher records confirm Lawrence's Jacobi/hyperadjugate source
(`10.4153/CMB-1964-045-0`), Dolgachev's Cremona treatment
(`10.1017/CBO9781139084437`), and Qureshi--Reis's general finite-group
power-map functional graphs (`10.1016/j.disc.2023.113393`).  Review B already
repaired the missing in-text Dolgachev citation.  These sources own the
ingredients, not merely related terminology.  A bounded direct search did not
locate the exact full-matrix temporal conjunction, but absence from a bounded
search is not a novelty certificate.  External release therefore remains
HOLD pending specialist owner review.

The paper correctly excludes `d=2`; it covers all prime powers symbolically,
while the literal-minor control remains prime-field only.  The latter is a
declared finite-control limitation, not evidence for an omitted field
assumption in the polynomial proof.

## Post-repair control and build

The canonical stored output is byte-identical to a fresh run:

```text
double-adjugate exact controls: PASS
assertions: 141190
staircase (5, 4, 0, [4, 4, 4, 4, 4, 4, 4])
staircase (7, 3, 1, [6, 3, 3, 3, 3, 3, 3])
staircase (17, 3, 2, [16, 4, 1, 1, 1, 1, 1])
staircase (257, 3, 4, [256, 64, 16, 4, 1, 1, 1, 1])
staircase (19, 4, 1, [18, 2, 2, 2, 2, 2, 2])
```

The post-repair four-stage build
`pdflatex -> bibtex -> pdflatex -> pdflatex` passed.  `main.pdf` has 4 A4
pages and 296,320 bytes.  `pdftotext -layout` recovered 13,815 bytes.  The
final logs contain no LaTeX/package warning, undefined citation/reference,
multiply-defined label, overfull/underfull box, or error.  All 23 fonts are
embedded, subsetted, and Unicode mapped.  The two modified pages were rendered
and inspected without clipping or malformed mathematics.

## Disposition

- Theorems and proofs: **GO internally**.
- Exact evidence: **GO after the staircase repair**.
- External posting, submission, contact, novelty, and priority claims:
  **HOLD** pending the direct-owner gate and final artifact QA.
