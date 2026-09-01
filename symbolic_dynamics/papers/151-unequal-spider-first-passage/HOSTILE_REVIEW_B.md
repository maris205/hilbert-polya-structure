# HOSTILE REVIEW B — P151

**Manuscript:** *First-Passage Dynamics on an Unequal Finite Spider*  
**Reviewer status:** independent of both the P151 authoring pass and
`HOSTILE_REVIEW_A.md`  
**Review basis:** the repaired current source, complete support package,
frozen verifier transcript, primary-source records, an isolated rebuild, and
inspection of every rendered page  
**External status:** `HOLD_EXTERNAL`

## Verdict

**ACCEPT**

| Severity | Count |
|---|---:|
| Critical | 0 |
| Major | 0 |
| Minor | 0 |

All four findings from Review A are closed.  I also reattacked the repaired
theorem from the killed-arm recurrences, renewal equations, extremal transfers,
and inverse map rather than treating the package verifier as a proof.  I found
no false theorem interface, missing admissible boundary case, owner collision,
source-metadata defect, transcript mismatch, or visible PDF defect.

## 1. Closure of Review A

| Review-A item | Status | Review-B finding |
|---|---|---|
| M1: omitted Sericola generic time/place owner and Chen tree-PGF neighbour | **CLOSED** | Both primary records are now in the bibliography, source ledger, ownership table, prose subtraction, and limitations.  Generic joint time/place laws and matrix moments, generic tree hitting-time PGFs, and the background endpoint/mean formulas receive zero credit.  The residual claim is narrowed to the explicit unequal-spider continuant product, its compact scalar variance specialization, the sharp fixed-total extremizers with equality classes, and the exact coarse-data inverse boundary. |
| m1: de la Iglesia--Juarez cited only as a preprint | **CLOSED** | The bibliography and source ledger now give the journal version of record: *Journal of Mathematical Analysis and Applications* **517**(2), 126624 (2023), DOI `10.1016/j.jmaa.2022.126624`; the arXiv identifier is retained only as an access route. |
| m2: “independent” overstated for the one-attempt moment checks | **CLOSED** | The abstract and manuscript now say “exact-arithmetic” or “additional exact routes.”  `CONTROL_RESULTS.md` expressly records that the 400 one-attempt assertions share the continuant-derivative engine and are not an independent implementation.  The remaining verifier phrase “independently assembled” applies only to the genuinely separate literal vertex-state recursion versus rational-series construction. |
| m3: formal/analytic bridge at zero and one omitted | **CLOSED** | The proof now states `Q(0)=0`, `Q(1)=1-H/r<1`, and `D(1)=H product_j ell_j>0`, and it identifies separately what each fact licenses: formal-series inversion at zero and regular endpoint/moment evaluation at one. |

The repairs are substantive rather than cosmetic: they change the ownership
ceiling and contribution wording while preserving the valid mathematics.

## 2. Fresh direct-owner and source audit

### 2.1 Sericola and Chen subtraction

I checked the primary Sericola article rather than relying on title-level
metadata.  Its finite-chain formula gives the generic joint law of hitting
time and hitting place through the killed transition matrix, with endpoint
and first/second-moment matrix consequences.  Those results encompass the
generic existence and computability of the P151 distribution and moments.
The repaired manuscript now says exactly that and assigns them no
contribution credit.

Chen's primary record is correctly identified as the general-tree
hitting-time generating-function algorithm.  The repaired table and prose
subtract this generic tree-PGF axis.  They do not try to recover novelty by
renaming a generating function as a transform.

After those deductions, the manuscript claims only the model-specific
closed continuant factorization

`F_i(z) = z^{ell_i} product_{j != i} P_{ell_j}(z) / D(z)`,

the explicit unequal-spider scalar variance and its derivation, fixed-total
integer equality classes, and the endpoint-ray/mean-scale inverse statement.
Neither inspected primary owner states that residual package.  This is the
correct subtraction boundary; it is not an assertion that generic
first-passage, continuant, gambler's-ruin, or tree-PGF theory is new.

### 2.2 Metadata and neighbouring spider literature

The current source metadata agree with the primary/journal records:

- Bruno Sericola, *Stochastic Models* **40**(4), 685--727 (2024), DOI
  `10.1080/15326349.2024.2319201`;
- Haiyan Chen, *Statistics & Probability Letters* **77**(15), 1574--1579
  (2007), DOI `10.1016/j.spl.2007.03.044`;
- Manuel D. de la Iglesia and Claudia Juarez, *Journal of Mathematical
  Analysis and Applications* **517**(2), 126624 (2023), DOI
  `10.1016/j.jmaa.2022.126624`.

The de la Iglesia--Juarez article studies a different spider-process
framework (spectral/QBD and reflecting--absorbing factorization), not the
finite unequal-leaf absorption law proved here.  Castella--Sericola remains
correctly subtracted as the equal-arm star-distribution owner.  A fresh
boundary search through tree first-passage moment and spider-chain literature
did not locate the repaired residual formulas.  As the manuscript itself
notes, this bounded search is evidence for the stated owner boundary, not a
global novelty guarantee.

## 3. Independent theorem re-derivation

### 3.1 Continuants and the killed-arm interface

The recurrence

`P_0=0, P_1=1, P_2=2, P_m=2P_{m-1}-z^2 P_{m-2}`

gives

`P_m(z)=sum_k (-1)^k binom(m-1-k,k) 2^{m-1-2k} z^{2k}`.

Thus `P_m` is even, `P_m(0)=2^{m-1}` for `m>=1`, and `P_m(1)=m`.
Solving the two boundary recurrences on a killed path of length `m`, started
at vertex one, gives

- success transform `z^{m-1}/P_m(z)`;
- return transform `z P_{m-1}(z)/P_m(z)`.

The formulas remain correct at `m=1`: `P_0=0` suppresses the impossible
return, while the subsequently restored centre step produces immediate
leaf success.  No hidden assumption `ell_i>=2` enters the theorem.

### 3.2 Renewal, the zero/one bridge, support, and atoms

Restoring the centre step and uniform arm choice yields

`S_i(z)=z^{ell_i}/(r P_{ell_i}(z))`

and

`Q(z)=z^2/r sum_j P_{ell_j-1}(z)/P_{ell_j}(z)`.

Summing over failed attempts gives `F_i=S_i/(1-Q)`, and clearing the
continuants gives the displayed common-denominator formula.  The repaired
bridge is exact:

- `Q(0)=0`, so `(1-Q)^{-1}` exists as a formal power series;
- `Q(1)=1-H/r<1`, so the renewal succeeds almost surely and the transform is
  regular at one;
- `D(1)=H product_j ell_j>0`, so the cleared rational presentation is also
  regular there.

Indeed `Q` is a defective PGF, so `|Q(z)|<=Q(|z|)<=Q(1)<1` on the closed unit
disk.  Each `P_m` has only even powers.  Therefore the marked support begins
at `ell_i` and remains in `ell_i+2 Z_{≥0}`.  The unique monotone path gives
the first atom `1/(r 2^{ell_i-1})`.  At one,
`F_i(1)=1/(ell_i H)` and the marked masses sum to one; there is no omitted
atom at infinity.

### 3.3 Mean and variance without a false independence step

For one centre-to-boundary attempt on an arm of length `m`, a direct
finite-difference calculation gives

- success probability `1/m`;
- `E A_m=m`;
- `E A_m^2=m(m^2+2)/3`;
- `E[A_m 1_{return}]=2(m^2-1)/(3m)`.

Averaging over arms gives

`p=H/r`, `mu=L/r`, `nu=(C+2L)/(3r)`, and
`rho=2(L-H)/(3r)`.

With a fresh strong-Markov restart `T'` only after failure,
`T=A+(1-B)T'`.  Consequently

`p E T=mu`, and `p E T^2=nu+2 rho E T`.

The `rho` term correctly retains the dependence between attempt duration and
failure; the manuscript does not factor dependent variables.  Simplification
gives

`E T=L/H`,

`Var(T)=(C-2L)/(3H)+L^2/(3H^2)`.

An independent exact absorbing-linear-system calculation on the profiles
`(1,1)`, `(1,5)`, `(2,3)`, `(3,7,10)`, `(1,4,9,13)`, and
`(2,2,2,2,2)` reproduced every endpoint probability, mean, and variance.
This check did not import the manuscript's quotient-derivative code.

### 3.4 Fixed-total extrema and inverse boundary

For `2<=a<=b`, the outward transfer `(a,b)->(a-1,b+1)` changes the reciprocal
sum by

`1/[a(a-1)] - 1/[b(b+1)] > 0`.

For `b>=a+2`, the inward transfer `(a,b)->(a+1,b-1)` changes the old reciprocal
sum minus the new one by

`1/[a(a+1)] - 1/[b(b-1)] > 0`.

Strictness proves both claimed equality classes: the one-long-arm profiles
and the balanced profiles.  The boundary `L=r` is not lost; both classes then
coincide at the all-one profile.

For the inverse statement,
`pi_i/pi_j=ell_j/ell_i` determines the unique primitive positive integer ray
`d`, while every common integer dilation `ell=cd` preserves the endpoint
vector.  Substituting into the owned mean identity gives

`E T = c^2 (sum_i d_i)/(sum_i d_i^{-1})`,

and hence the printed scale formula.  The theorem properly restricts this to
exact data generated by a labelled simple-random-walk spider; it does not
claim recovery from noisy data, unknown topology, or unknown transition
probabilities.

### 3.5 Boundary cases and interfaces

The following hostile cases all close correctly:

- a unit arm has immediate success probability `1/r` and zero return mass;
- all arms of length one give `F_i=z/r`, `T=1`, and variance zero;
- for `r=2` and arm lengths `a,b`, the formulas reduce to `E T=ab` and
  `Var(T)=ab(a^2+b^2-2)/3`, the absorbing-interval values;
- repeated arm lengths may cancel factors from the displayed `D`, but the
  manuscript calls it a common denominator, not a reduced denominator;
- `r=1` and zero-length arms are explicitly outside scope;
- the background endpoint and mean identities are visibly labelled as owned
  inputs, while the new extrema and inverse conclusions built from them are
  separately identified.

## 4. Frozen verifier and package manifest

I replayed the verifier cold with bytecode generation disabled.  Its output
matched `verification_output.txt` byte for byte and ended in `PASS`:

| Item | Frozen value |
|---|---:|
| Literal profiles | 1,360 |
| Fixed-mass profiles | 190,026 |
| Inverse profiles | 37,440 |
| Exact integer/Fraction assertions | **1,446,432** |

The replay covers literal-state coefficients, marked transforms, moments,
continuants, one-attempt identities, fixed-mass extrema, inverse recovery,
and the equal-arm owned control.  The transcript correctly says enumeration
is not proof.

`sha256sum -c SHA256SUMS` passed every listed pre-Review-B artifact.  In
particular:

- current `main.pdf` and `main_round1.pdf` are byte-identical at
  `24fddbfb896510cf2712a8ade2a3ac37d04712676f635e39f1170c4cc334e8d9`;
- preserved `main_round0_original.pdf` is
  `64ea74c13f5fedcd4d4280426224723a2b290f16ff6d53ceb860163b456215af`;
- `verification_output.txt` is
  `af9c4bba9094e149b5c070351cad0b48697eb3fd999fc4f8b60e155513242f7c`.

The manifest's omission of this newly created Review-B file is expected at
review time.  If the project freezes a post-review manifest, the author-side
freeze pass should add this report without altering the accepted theorem.

## 5. Isolated build and page inspection

I copied only the current `main.tex` and `references.bib` to an isolated
temporary directory and ran
`pdflatex -> bibtex -> pdflatex -> pdflatex` under fixed reproducibility
settings.  The result was byte-identical to the packaged current PDF.  A
second independent clean build was byte-identical to both the first isolated
build and the package PDF.

The current artifact is an unencrypted PDF 1.5 file, 6 A4 pages, 356,664
bytes.  The settled build has no undefined reference/citation, rerun request,
or bad box, and every reported font is embedded.

I rasterized and inspected all six pages at original detail.  The ownership
table, main theorem, continuant and renewal displays, the repaired
`Q(0)/Q(1)/D(1)` bridge, exact-audit table, limitations, mandatory
declarations, and all seven bibliography entries are legible and within the
page bounds.  There is no overlap, clipping, corrupted glyph, accidental
blank page, or visible anonymity breach.

## 6. Final decision

Review A's owner, metadata, evidence-wording, and regularity objections are
all closed.  The narrowed theorem is internally consistent, its proof
interfaces survive independent derivation and edge-case attack, and the
source/PDF/transcript package is coherent.  I therefore recommend
**ACCEPT**, with **0 Critical, 0 Major, and 0 Minor** findings.

External dissemination remains **`HOLD_EXTERNAL`**.
