# Review Summary

## Review identity and limit

This is the author-side convergence record for the Paper 19 source design. It
summarizes three zero-write candidate-stage audits:

1. an independent combined novelty and standalone-value scout;
2. an independent candidate-gate proof and portfolio reviewer; and
3. an adversarial support-one character-theorem reviewer.

It is not the future independent source-design review and does not authorize a
source lock or manuscript stage.

## Overall verdict

The corrected combined package is accepted at candidate stage.

| Axis | Conservative result | Gate |
|---|---:|---:|
| Novelty | 7.9/10 | 7.5 |
| Standalone value | 8.2/10 | 7.5 |
| Proof readiness | 9.1/10 | 9.0 |

The novelty scout independently returned `8.2/8.4`. The adversarial character
review returned

`PROVABLE AS STATED`, confidence `0.97`.

No waiver is used.

## Source intake audit

The author package consumes only:

- the exact recurrence setup and group-algebra framework;
- Paper 16's terminal boundary for planar support one;
- Paper 17's terminal anchored dimension theorem and relation lattice;
- Paper 18's terminal artifact for a no-collision check;
- Laurent's qualitative torus theorem; and
- bounded primary-source closest-work comparisons.

It consumes no code, data, experiment, CAS transcript, figure, or unverified
secondary-source theorem.

## Part A obligation audit

### Equality subgroup rigidity

The reviewer reproduced the logic:

1. Paper 17's `2m` relation vectors generate a quotient freely based on the
   initial indices outside `R_m`.
2. The relation lattice is therefore saturated, not only independent.
3. Equality `dim H=k-m` gives an equal-rank saturated kernel containing that
   lattice.
4. The two lattices coincide.
5. A connected embedded torus is determined by this kernel, so `H=H_m`.

**Result:** PASS.

### Normalization and `E_m`

The unique normalization fixes every free initial scalar to one. The reviewer
checked every coordinate role in the reconstruction:

- initial killed middle coordinates for `n<nu`;
- previous outputs for `n>=nu`;
- solved killed initial scalars;
- copied future coordinates already represented by later `y`; and
- tail outputs requiring the second open inequality.

The activity interval

`[max(0,m-nu),min(m,k-nu))`

and its length

`min(m,k-m,nu,k-nu)`

were independently checked against residue membership.

**Result:** PASS.

### Nonemptiness

An early proposed construction using one repeated root `rho` was rejected as
unnecessarily fragile at tail steps. The repaired proof works root assignment
by root assignment. An inequality involving indices separated by `nu` or
`k-nu` always contains a free variable because the active interval has length
at most each separation. Each forbidden set is proper, possibly empty. A
finite union cannot cover the remaining irreducible torus. If every variable
is active, no inequality index exists.

**Result:** PASS, with the generic-open proof mandatory.

### Fixed and universal geometry

The reviewers confirmed:

- squarefree `P` gives `delta^alpha` disjoint smooth open-torus branches;
- arbitrary `P` gives `r^alpha` branches after reduction;
- active multiple roots yield local factors `z^mu`;
- fixing actual support and keeping the leading/constant coefficients
  invertible makes the root scheme finite locally free of degree `delta`;
- the universal `E_m` is an open product of root schemes and free tori, hence
  flat relative lci; and
- the completed formula is a **fiber** local ring statement.

The package was corrected not to call `E_m` a Hilbert or Fano scheme and not
to overstate the discriminant.

**Result:** PASS.

### Coefficientwise arithmetic

At `m=k-1`, nonempty `E_m` supplies a one-dimensional saturated translate for
every coefficient tuple. A finite algebraic extension contains its translate
scalars; adjoining the non-torsion parameter `2` gives a finitely generated
compatible group. This proves infinite `T_(k-1)`. Paper 17 plus Laurent gives
finite `T_k` for every finite-rank group.

**Result:** PASS with compatible-field/compatible-group quantifiers.

## Part B obligation audit

### Exclusive labels

The four nonzero group-algebra terms cannot contain a singleton. The only
possible partitions are `A`, `B`, `C`, and all-zero `Z`. The nonzero variable
`v` is explicit in `A/B/C`, preventing overlap with `Z`. The scalar table was
checked with signs from the fixed recurrence orientation.

**Result:** PASS.

### Gcd and original-window bookkeeping

Because the offsets are `gq` and `gL`, original indices split by residue
modulo `g`. At `m=gq^2`, every residue gets `q^2` equations. At
`m=gq^2-1`, residues `0,...,g-2` get `q^2`, while residue `g-1` gets
`q^2-1`.

The involved character endpoint at `m=kq` is

`u_(kq+k-1)`,

not `u_(2kq-1)`.

**Result:** PASS after endpoint correction.

### Arbitrary rank and colored components

This was the principal candidate-stage risk. A support-bit or rank-one
argument alone would not exclude a higher-rank torus.

The adversarial proof closes the gap:

1. Every active triple connects exactly its two nonzero coordinates.
2. A signed nonzero `d`-weight around a cycle would force `v=d^s v`,
   impossible in a torsion-free lattice.
3. Each graph component therefore has integer heights.
4. Components receive independent formal colors, so accidental equality of
   values in the actual lattice cannot merge disconnected graphs.
5. Each colored component separately obeys the Laurent recurrence.

**Result:** PASS. The use of colors is mandatory in the proof.

### `q^2` extinction

A minimum-height vertex traces backward only through `B` labels until an
initial residue `r`. Forward minimum-height persistence again forces `B`,
giving a column of nonzero old/output values and a parallel column of zero
middles. Triangular propagation yields zero at `r+qL`, while persistence gives
nonzero at `r+Lq`.

**Result:** PASS for every component and arbitrary character rank.

### Unique `q^2-1` shadow

If the minimum initial residue were at most `q-2`, the full contradiction
would still fit. Hence it is `q-1`. The shortened zero triangle covers the
central block except `N_*=(L+1)q-1`. The explicit congruence construction
and its two inequalities were checked. Every nonzero component must contain
`N_*`, so only one component exists.

Ambient coordinate restrictions generate the actual `X*(H)`. Since the
central minimum character itself appears, the actual lattice is `Z w` and
`w` is primitive. The package distinguishes this actual-torus conclusion
from the weaker statement for an abstract torsion-free lattice with an unused
direct summand.

**Result:** PASS.

### Generating functions

The central delta block determines the recurrence in both directions. The
reviewer checked

`G(z)=(1+Tz^L)/(1+Tz^L+z^q)`

and

`H(z)=z^(q-1)/(1+Tz^(q-L)+z^q)`.

The semigroup lemma says `alpha q+beta s=D<qs` has at most one nonnegative
solution when `gcd(q,s)=1`. The complete involved backward and forward ranges
remain below `Lq` and `(q-L)q`, respectively. Thus each coefficient is zero
or a monomial. The next degree equals `(q-L)q` and has exactly the two terms
producing `1+T^q`.

**Result:** PASS without computational evidence.

### Seven labels and scalar obstruction

The seven displayed triples and their index bounds were replayed. The special
zero at `z_*` was checked in the cases `2L<q` and `2L>q`; equality is excluded
by coprimality when `q>=3`. Possible coincidence of two `C` indices creates no
type conflict.

The scalar chain is:

1. first `C/B` overlap gives `bc^(d-1)=-1`;
2. later `C/A` overlap gives `a=-1`;
3. adjacent labels make the `Z` old/middle/future scalars all `c`; and
4. the recurrence gives `c=-c`, impossible in characteristic zero.

**Result:** PASS.

### `q=2` and general `g`

The unique core is `CBA`, with characters `(dw,w,0,w,dw)`. The scalar locus
`a=-1`, `bc^(d-1)=-1` is necessary and sufficient. The exponent vector
contains one and therefore defines a saturated one-torus.

For inactive residues, the map

`Phi(x,y)=(y,c+by^d-x)`

is a polynomial automorphism. The finitely many required coordinate
polynomials are nonzero; their zero hypersurfaces do not cover affine
two-space over an infinite field. Generic starting pairs fill every inactive
residue with nonzero scalars.

**Result:** PASS. A five-coordinate core alone would have been insufficient
for general `g`; the `Phi` fill is mandatory.

## STOP-S1 audit

The original universal support-one sharpness candidate is false. The package
does not conceal the failure. `STOP-S1` appears in the research question,
proof package, claims matrix, novelty assessment, initial/final proposals,
this review, and the no-run audit plan.

The surviving `q>=3` theorem is deliberately called a universal obstruction
at the penultimate character window, not an exact scalar threshold.

**Result:** NEGATIVE PROVENANCE PRESERVED.

## Citation and portfolio audit

- Laurent is the only external proof theorem and remains qualitative.
- General torus, sparse-polynomial, and shift-like sources are context only.
- Paper 16 ownership of planar `CBA` and effective `T_4/T_3` is hash-bound.
- Paper 17 ownership of the anchored dimension law and terminal arithmetic is
  hash-bound.
- Paper 18 has no theorem-level collision.

**Result:** PASS, subject to a search refresh at source lock.

## Unity and page audit

The article is unified by the scalar-lift problem for extremal character
patterns. The 29-page working plan allocates 14 pages to Part A proof geometry
and about 13 pages to Part B character/scalar proofs. The credible compressed
range is `26--29` pages. No padding, appendix, computation, or figure is
required.

**Result:** PASS.

## Repaired-issue ledger

| Issue | Repair | Locked consequence |
|---|---|---|
| False universal `kq` sharpness | Seven-label scalar obstruction | `STOP-S1`; no exact clock for `q>=3`. |
| Rank-one ansatz did not cover arbitrary `H` | Colored components plus actual `X*(H)` surjectivity | TB3--TB5 stated at correct quantifiers. |
| Wrong possible touched endpoint `u_(2kq-1)` | Direct residue inventory | Correct endpoint `u_(kq+k-1)`. |
| Five-coordinate `q=2` lift ignored inactive residues | Generic `Phi` orbit fill | Full original `V_(kq-1)` construction. |
| One-root Part A nonemptiness argument fragile | Root-tuple proper-closed avoidance | Nonemptiness for every root assignment. |
| `E_m` risked moduli overstatement | Explicit normalized-locus terminology | No Hilbert/Fano/fine-moduli claim. |
| Part A risked absorbing Paper 17 | Net-new ownership list | BG17 remains predecessor. |
| `CBA` risked duplicate novelty | Paper 16 provenance | Recovered endpoint only. |

## AC01--AC18 review

All eighteen anti-claims in `RESEARCH_QUESTION.md` are present and consistent
with the theorem statements. None is contradicted by the proof package or the
page plan.

## Residual risks for the independent source reviewer

1. Recheck every translation between core index `j` and original index
   `r+gj`; the mathematical theorem is closed but typography is fragile.
2. Re-derive the selected seven `F` triples from the generating-function
   formulas, including the two cases for `F_(z_*)=0`.
3. Verify every active/free index in the `E_m` reconstruction and confirm that
   no open condition is omitted or duplicated.
4. Check that every universal-family statement says fixed actual support and
   every local ring says completed fiber.
5. Recheck all predecessor hashes and the `q=2` novelty deduction.
6. Confirm that all ten author files preserve `STOP-S1` and AC01--AC18.

These are independent replay obligations, not known blockers.

## STOP list

- `STOP-S1`: universal scalar sharpness for `q>=3`.
- all-lower-dimensional translate classification.
- Hilbert/Fano fine-moduli language.
- effective Laurent counts.
- positive characteristic and zero-coefficient extensions.
- rational/Laurent support and arbitrary polynomial automorphisms.
- absolute priority and every-group sharpness.

## Final review decision

The corrected package is mathematically coherent, portfolio-distinct after
deductions, and large enough for a standalone proof-first article.

**AUTHOR REVIEW VERDICT: PASS / TEN-FILE SOURCE DESIGN MAY BE SUBMITTED TO A
FRESH INDEPENDENT SOURCE REVIEW.**

No later lifecycle stage is authorized by this author-side verdict.
