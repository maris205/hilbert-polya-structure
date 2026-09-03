# Hostile Review B — P176 First-Frequency Rotation

**Review date:** 2026-09-03 UTC  
**Reviewer role:** independent non-author reviewer B; neither P176 author nor
Review A  
**Mathematical triage:** `PROVABLE AS STATED`  
**Verdict:** `PASS_MATHEMATICS_WITH_TWO_MINOR_REPAIRS`  
**Lifecycle:** `AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL` (unchanged)  
**Edit boundary:** this review did not modify `main.tex`, `references.bib`, the
author verifier, or any PDF.

## 1. Outcome

I re-derived the literal map and all five advertised outputs before opening
Review A. The pointed-necklace component theorem, possible-period set, sharp
clock and deepest two, every-target inverse atlas and histogram, image formula,
and Möbius fixed census are correct as stated. The `n=1`, `n=2`, constant-word,
half-weight, and zero-residue component boundaries are all covered correctly.

The internal distance from P166 survives this audit but remains only an amber
residual. There are two independent obstructions to a direct proof transfer:
mixed `+/-1` generator components violate P166's weak-composition mass
constraint, and one P176 necklace may contain several nontrivial recurrent
components whereas P166 permits at most one. This does not exclude a contrived
embedding into a union of subsystems, so the existing kill switch must remain.

Two package defects require repair. First, the external owner boundary omits a
closer primary owner for fixed-weight binary rotation classes, while the
scouting owner log still conflates Høyer--Špalek's quantum **phase** rotation
with a coordinate rotation. Second, Review A's verifier-provenance repair did
not reach the author program, its canonical header, or all support documents.
Neither defect changes a theorem, but both must close before the package can be
called Review-B complete.

| Severity | Count |
|---|---:|
| Critical | 0 |
| Major | 0 |
| Minor | 2 |

## 2. Frozen review inputs

| Artifact | SHA-256 |
|---|---|
| `main.tex` | `a1ecbcc78809d9bb87d03902dd87ae0e6402d4b7e7992a4023ec64ac417d0877` |
| `main.pdf` | `5a8977524f5f7f5f654442bb3ac98cf74872de297277e9ffb0ff5c23878e69ba` |
| `references.bib` | `43ca1a1a260ea77ee3bdbbbf8d04140167ffce156a428d2e5c0c482fb54a5223` |
| author `code/verify_p176.py` | `c4a499855a50bc0ba64a78d69d3842a15375edcacdd9fad0e8dab39654956491` |
| author `code/CANONICAL.txt` | `71720878a3498347661bad83838c3dbbc47c5c64c76ad7b70f6d5f02e7029190` |
| P166 `main.tex` | `a709e1b8dc6f50059cf85c8a2c922455b7812b24f4e38ebab88c77123f279ce8` |

The reviewed PDF has four A4 pages and 395,769 bytes.

## 3. Independent derivation

### B-T01 — exact pointed reduction and every generator component: accepted

Let `u` be a length-`n` word of least rotational period `d|n`, and put
`k=wt(u)`. Its distinct pointed states are `R^j u`, `j in Z/dZ`. At phase
`j`, the first bit is `u_j`; therefore the literal rule is

```text
j -> j+k       when u_j=1,
j -> j+n-k     when u_j=0.
```

Since `d|n`, the second increment is `-k modulo d`. This proves the exact
`+/-k` phase map without quotient loss.

Let `h=gcd(k,d)` and `L=d/h`. The undirected generator graph of `+k` has
exactly `h` cosets, each of size `L`. Number one coset in generator order by
`q in Z/LZ` and write its labels as `b_q`. Its functional graph has successor

```text
q -> q+1 if b_q=1,
q -> q-1 if b_q=0.
```

- If `L=1`, the sole vertex is fixed.
- If `L=2`, `+1=-1`, so both vertices point to the other, independently of
  their labels.
- If `L>=3` and the labels are constant, every arrow is coherent and the
  component is one `L`-cycle.
- If `L>=3` and both labels occur, every cyclic `10` edge is bidirected and
  hence a two-cycle. Starting at a `1` moves forward to the terminal `1` of
  its run; starting at a `0` moves backward to the initial `0` of its run.
  Thus every vertex reaches one of those edges. A directed cycle that changes
  direction must immediately reuse an undirected edge, while a longer cycle
  without a change of direction would require every label to agree. Hence no
  other recurrent component exists.

The distance from a run vertex to its boundary edge is exactly the formula
displayed in the manuscript. A constant run of length `s` contributes maximum
tail `s-1`, so the component maximum is longest cyclic constant run minus one.
No hypothesis is missing.

### B-T02 — complete possible-period set: accepted

A period greater than two can occur only on a constant generator component,
so it equals `L=d/gcd(k,d)` and divides `n`. If `L=n`, then `d=n` and
`gcd(k,n)=1`, leaving one generator component. Constancy of that component
would make the entire primitive word constant, impossible for `n>1`.
Consequently every long period is a proper divisor of `n`.

Constants realize period one. A necklace with exactly one `1` realizes period
two for every `n>=2`. For a proper divisor `L>=3`, write `n=gL`, `g>=2`, and
use the weight-`g` support

```text
{0,1,...,g-2,g}.
```

Its wraparound zero gap has length `n-g-1=g(L-1)-1>=3`, while its only other
nonempty zero gap has length one. The unique longest gap forces any preserving
rotation to be trivial, so the word has least period `n`. The generator coset
`g-1 modulo g` is all zero and has length `L`; it is the required `L`-cycle.
Thus the manuscript's set is exact:

```text
n=1:       {1},
n>=2:      {1,2} union {L : L|n and 3<=L<n}.
```

### B-T03 — sharp `n-2` clock and deepest states: accepted

In a nonconstant component of length `L`, every constant run has length at
most `L-1`, so every tail is at most `L-2<=n-2`. Constant components have no
tail. The pointed word `010^(n-2)` has weight one, a cyclic zero run of length
`n-1`, and the displayed pointer has tail `n-2`; complement equivariance gives
the second witness.

Equality forces `L=n` and a run of length `n-1`, hence exactly one minority
bit. There are two such rotation necklaces and one farthest pointer in each.
Therefore exactly the displayed word and its complement are deepest for
`n>=3`.

The small boundaries are not being inferred from that equality argument:

- for `n=1`, both one-letter words are fixed and deepest at depth zero;
- for `n=2`, the constants are fixed and `01 <-> 10`, so all four words are
  periodic and deepest at depth `n-2=0`.

### B-T04 — every target, tie layer, histogram, and image: accepted

Fix a nonconstant target `y` of weight `k`. Weight preservation confines every
source to the same layer. A source beginning in `1` must undo the `R^k` branch,
so its only candidate is

```text
x_1=R^(-k)y, valid exactly when y_(-k)=1.
```

A source beginning in `0` must undo `R^(n-k)=R^(-k)`, so its only candidate is

```text
x_0=R^k y, valid exactly when y_k=0.
```

When both exist, their first bits differ, so they are distinct. Constants have
only their constant source.

The two inspected target coordinates coincide exactly when `n|2k`. For an
internal layer this is precisely the even-`n`, half-weight case `k=n/2`.
Then `R^k=R^(-k)` and the update is the same rotation on both first-bit
branches. Exactly one label condition holds at every target, so the layer is a
permutation (indeed an involution) with fibre one everywhere. This resolves
both the frequency-tie and candidate-coalescence boundary.

Outside the tie layer, the inspected coordinates are distinct. Fibre zero
prescribes `(y_(-k),y_k)=(0,1)` and fibre two prescribes `(1,0)`. Each choice
leaves `k-1` ones among `n-2` free coordinates, proving

```text
N_0(n,k)=N_2(n,k)=C(n-2,k-1),
N_1(n,k)=C(n,k)-2 C(n-2,k-1).
```

Summing `N_1+N_2` over internal layers and adding the constants yields exactly
the manuscript's image formula. Both layer mass identities
`N_0+N_1+N_2=C(n,k)` and `N_1+2N_2=C(n,k)` hold.

### B-T05 — primitive-block Möbius fixed census: accepted

Let `A(d,j)` count length-`d` linear binary words of least period `d` and
weight `j`. Repetition-factor Möbius inversion gives

```text
A(d,j)=sum_{e|gcd(d,j)} mu(e) C(d/e,j/e).
```

Every length-`n` word is uniquely an `n/d`-fold repeat of one such aligned
primitive block and has total weight `k=(n/d)j`. On a least-period-`d` word, a
leading `1` is fixed iff `d|k`; a leading `0` is fixed iff `d|(n-k)`, which is
equivalent because `d|n`. The fixed condition is therefore independent of the
pointer, and summing the primitive blocks proves the displayed census.

The edge conventions are sound: `gcd(d,0)=d`; `A(1,0)=A(1,1)=1`; and constant
blocks of larger displayed length have least period one and cancel from
`A(d,0)` and `A(d,d)`. Primitive enumeration remains zero contribution credit.

## 4. Internal collision audit reopened: P166

P166 has literal carrier `(Z/NZ)^N`, diagonal alphabet translation, and phase
map `q -> q+c_q`, where `c_q>=0` and `sum c_q=N`. P176 has coordinate-rotation
necklaces and, in generator coordinates, increments `+1` and `-1`. The common
cyclic-phase shell, ordinary functional-graph language, numerical maximum
`n-2`, and indicator-style inverse notation are correctly assigned zero
credit.

The retained component mechanism is not a specialization of P166's mass
exhaustion. At a matched modulus `L>=3`, representing a mixed P176 generator
component as a P166 profile would require occupancy `1` at each `+1` arrow and
`L-1` at each `-1` arrow. If `z` of the `L` arrows are negative, the required
mass is

```text
(L-z) + z(L-1) = L + z(L-2) > L.
```

It cannot be a weak composition of `L`. Reversing generator orientation only
interchanges the label counts. The elementary `L=1`, `L=2`, and coherent
components may overlap P166 phase graphs and earn no residual credit.

There is a second, graph-invariant obstruction. P166's mass theorem permits at
most one nontrivial recurrent cycle on a diagonal orbit. The P176 necklace
`111000` has `d=6`, `k=3`, `h=3`, `L=2`; its six pointed states are three
disjoint two-cycles. Hence that whole necklace is not graph-conjugate to one
P166 diagonal orbit. P166 also permits all periods `1,...,N` and unbounded
one-step fibre size, unlike P176's proper-divisor period set and `0/1/2`
fibres.

These invariants block a direct theorem-engine transfer but do not prove that
no artificial union-of-subsystems embedding exists. The correct disposition
is unchanged amber, not a green separation claim and not an internal kill on
the current evidence.

## 5. External owner audit reopened

### 5.1 Høyer--Špalek: phase rotation, not coordinate rotation

The publisher PDF of Høyer and Špalek, *Quantum Fan-out is Powerful*,
Section 3.2 and Lemma 3.4, constructs the one-qubit operation
`R_z(phi |x|)`: Hamming weight controls a rotation angle in phase space. It
does not circularly permute the coordinates of the input word, select a sign
from its first bit, define an autonomous finite map, or study its functional
graph.

The live manuscript and `SOURCE_VERIFICATION.md` now state this distinction
correctly. Their conservative decision to give the generic
Hamming-weight-controlled-rotation phrase and both frozen P176 branches zero
credit is safe. Høyer--Špalek must not, however, be presented as a literal
owner of `R^k` on binary words.

Primary record checked:

- Peter Høyer and Robert Špalek, “Quantum Fan-out is Powerful,” *Theory of
  Computing* **1** (2005), 81--103,
  <https://doi.org/10.4086/toc.2005.v001a005>.

### 5.2 Closer coordinate-rotation owners omitted from the package

The following primary sources were independently opened and checked.

- Otokar Grošek and Viliam Hromada, “Rotation-Equivalence Classes of Binary
  Vectors,” *Tatra Mountains Mathematical Publications* **67** (2016),
  93--98, <https://doi.org/10.1515/tmmp-2016-0033>. They study the actual
  coordinate-rotation action on fixed-Hamming-weight binary vectors. Their
  Theorem 1 gives the feasibility of a rotation-class cardinality `d` by
  `d|n` and `n/d|k`, and their formulas give the sharp fixed-weight class-size
  distribution. This is a closer owner of P176's necklace/least-period input
  and a direct precursor for reorganizing the fixed census.
- Anant Gupta, Idriss J. Aberkane, Sourangshu Ghosh, Adrian Abold, Alexander
  Rahn, and Eldar Sultanow, “Rotating Binaries,” *AppliedMath* **2** (2022),
  104--117, <https://doi.org/10.3390/appliedmath2010005>. They define literal
  left circular coordinate shift and study rotation distance, Hamming weight,
  complement symmetry, and rotation equivalence classes. They cite and use
  the Grošek--Hromada class formula.

Neither source defines P176's first-symbol-glued autonomous update or proves
its generator-component, tail, inverse-fibre, or complete period theorem.
Thus this audit located a missing subtraction neighbor, not a direct owner and
not a kill trigger. Exact-phrase and structural searches for “rotate by the
multiplicity/frequency of the first symbol,” plus the literal formula and
`+/-k` pointed walk, produced no direct primary hit in this bounded pass. That
non-hit is not novelty, priority, freedom-to-operate, or circulation evidence.

## 6. Review-A provenance delta

I kept Review A closed until after the independent derivation and first
canonical execution above. Once opened, its mathematical derivations agreed
with the independent results. Its one finding correctly established that the
author verifier is scout-derived, and the revised `README.md`,
`NARRATIVE_REPORT.md`, and `CLAIMS_EVIDENCE.md` now say so.

The repair is nevertheless incomplete across the live package:

- `code/verify_p176.py` still calls itself a “paper-local independent exact
  verifier” in its docstring and prints `INDEPENDENT EXACT CONTROL`;
- the frozen `code/CANONICAL.txt` repeats that header;
- `PAPER_PLAN.md` still directs the author to “record independent exhaustive
  verification through n=18”;
- `README.md` first records Review A as complete but later says Reviews A/B
  “are intentionally deferred”; and
- `SELF_QA.md` records the Review-A independent control and later says no
  hostile Review A/B was produced.

The last two sentences can be preserved only if explicitly scoped as an
immutable historical Round-0 statement. As currently written in documents
that were otherwise revised after Review A, they are internally inconsistent.

## 7. Finding ledger and mandatory repairs

### P176-B-m01 — coordinate-rotation ownership boundary is incomplete

**Severity:** Minor while `HOLD_EXTERNAL` remains in force.  
**Status:** mandatory source-package repair; no theorem failure.

The live manuscript correctly types Høyer--Špalek as quantum phase rotation,
but the owner log cited by `SOURCE_VERIFICATION.md` still says their Section
3.2 treats “rotation by Hamming weight” and immediately equates a P176 branch
with that rotation without the phase/coordinate qualifier. The same package
omits the closer coordinate-rotation source Grošek--Hromada and the adjacent
Hamming-weight/rotation treatment of Gupta et al.

**Mandatory repair:** before any later circulation decision:

1. correct the scouting owner-log row so Høyer--Špalek owns only a
   Hamming-weight-controlled **phase** rotation, never a coordinate branch;
2. add and verify Grošek--Hromada in `references.bib`, cite it in the
   coordinate-necklace/fixed-census background, and assign fixed-weight
   rotation-class structure and enumeration zero contribution credit;
3. record Gupta et al. in `SOURCE_VERIFICATION.md` and the owner log as the
   adjacent literal-coordinate/Hamming-weight source (it may also be cited in
   the manuscript if the owner paragraph is expanded);
4. state explicitly that neither source owns the adaptive first-symbol gluing
   or its functional graph; and
5. preserve the direct-owner kill switch and `HOLD_EXTERNAL` after the repair.

**Why Minor:** the manuscript's present Høyer--Špalek sentence is factually
correct, all relevant classical rotation ingredients already receive zero
credit, and no newly checked source proves a retained dynamical theorem. The
defect is still mandatory because the source ledger is part of the external
gate.

### P176-B-m02 — Review-A provenance labels remain contradictory

**Severity:** Minor.  
**Status:** mandatory evidence-package repair; no mathematical or executable
failure.

Review A showed that the author verifier is a lightly relabelled descendant of
the scouting program. Several high-level documents were repaired, but the
program and canonical transcript still self-label as independent, and the
plan/QA/README contain stale statements listed in Section 6.

**Mandatory repair:** use one consistent provenance policy throughout the
package:

1. relabel the author program's docstring and printed header as a standalone
   author/scout-derived regression control;
2. regenerate its canonical transcript and cascade every changed verifier or
   transcript digest through `main.tex`, package documents, manifests, and a
   fresh PDF build; alternatively, if the Round-0 bytes must remain frozen,
   preserve them under an explicitly historical filename and add a
   non-ambiguous provenance correction adjacent to every live reproduction
   instruction;
3. replace `PAPER_PLAN.md`'s implementation-independence claim; and
4. update or explicitly historical-scope the stale Review-A/B deferral
   sentences in `README.md` and `SELF_QA.md`.

The independent Review-A bit-mask program and the independent Review-B string
program remain valid cross-checks, so no theorem depends on this wording.

## 8. Independent executable receipt

Fresh evidence lives in
`docs/papers172_176_sequence/reviews/p176_review_b/`. It imports no project
code, represents states as strings, uses literal slicing for rotation, obtains
orbit clocks by Brent detection, and reconstructs each local functional graph
before comparing it with the boundary/run theorem. This differs from the
author's tuple program and Review A's integer-bitmask program.

The canonical pass exhausts every binary word for `1<=n<=17` and every
pointed generator component in that box. It then constructs every advertised
proper-divisor period and checks all closed histogram mass identities through
`n=96`.

```text
assertions=19758014
transition_clock_digest=a3c10b5b7c7d35801ba595e56a91aa08e51b65545bbe9fa7426948359efcd455
RESULT: PASS
```

| Reviewer-B artifact | SHA-256 |
|---|---|
| `verify_p176_review_b.py` | `e6f2f90149b6c70a60783273cae4dce76cf36395aa5e9bf9b783fa6b848bdeb5` |
| `CANONICAL.txt` | `e79813f77b0dd7acfbce32eecda876f2a1b074aa5fe7220be57d9946f83ad128` |

Finite enumeration is only falsification evidence; the all-parameter
derivations in Sections 3--4 carry the acceptance.

## 9. Final disposition

No theorem, displayed formula, proof, or small-`n` boundary requires repair.
Do not weaken the complete component theorem, period inventory, sharp clock,
deepest-state census, inverse atlas, histogram, image formula, or fixed census.

Close `P176-B-m01` and `P176-B-m02`, rebuild any artifact whose recorded hash
changes, and append the author response to this file. The lifecycle must remain

```text
AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL
```

No external posting, circulation, contact, or submission is authorized by
this review.

## 10. Author response and Round-2 repair request

Both mandatory minors have been implemented without altering a theorem
statement, proof formula, or assertion count.

- For `P176-B-m01`, the owner ledger now types Høyer--Špalek only as a
  quantum phase-rotation source.  Grošek--Hromada (2016) and Gupta et al.
  (2022) were verified, added to the source boundary, cited in the manuscript,
  assigned zero contribution credit for fixed-weight coordinate-rotation
  structure, and explicitly denied ownership of the adaptive gluing or its
  functional graph.
- For `P176-B-m02`, the author program and canonical header now say
  `AUTHOR/SCOUT-DERIVED REGRESSION CONTROL`; the stale plan/README/self-QA
  deferral language was removed or explicitly historical-scoped.  The live
  verifier and transcript hashes are respectively
  `2dd56b882925c908565a9a213c42db7acccbf4fc214b54460619b71fe0587b50`
  and
  `3d0947a4df32f8e583e28d1964a52523602d61c64dde7b259bfdd15e71e4003b`.
- A fresh author replay matched that transcript at 2,828,503 assertions.
  The amended manuscript has source/PDF hashes
  `ff1f7d45c7ac7146a06f737a7187a9cedd451591ab9cbffeccf2d35eadc5874a`
  and
  `c13ca3f5e3673bb5dd9c01bdf7c8913f78425cdbfeb2a52e2d9b096a34122db4`.
  Two isolated source-only builds reproduce the four-page PDF byte for byte;
  settled logs are clean, all 31 font rows pass, and all-page visual,
  metadata, anonymity, and visible-hold checks pass.

The author requests Review-B delta acceptance.  Until that independent
acceptance is recorded, both findings remain repair-implemented/pending.
The lifecycle remains `AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL`.

## 11. Reviewer-B Round-2 delta acceptance

**Delta checked:** 2026-09-03 UTC  
**Verdict:** `ALL_REVIEW_B_FINDINGS_CLOSED`  
**Open findings:** `0 Critical / 0 Major / 0 Minor`  
**Lifecycle:** `AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL` (unchanged)

I re-read the live Round-2 manuscript and every repair surface named in
Section 7, rather than accepting the author's summary.  I also re-opened the
three primary source documents used at the disputed ownership boundary,
replayed both the author control and the independent Review-B control, checked
the settled PDF and build receipts, and verified the paper manifest against
the then-current directory.  The two findings close as follows.

| Finding | Delta verdict | Acceptance evidence |
|---|---|---|
| `P176-B-m01` | **CLOSED** | `main.tex` now identifies H\o yer--\v Spalek's operation as the phase gate $R_z(\varphi|x|)$ and explicitly denies that it is a cyclic coordinate shift.  It cites Gro\v sek--Hromada for fixed-weight coordinate-rotation classes and Gupta et al. for literal circular shifts, while assigning those ordinary ingredients zero contribution credit and denying either source ownership of the adaptive gluing or its functional graph.  The bibliography metadata agree with the publisher records.  `SOURCE_VERIFICATION.md` and the live focused owner ledger make the same phase-versus-coordinate distinction, retain the direct-owner kill switch, and retain the P166 subtraction and external hold. |
| `P176-B-m02` | **CLOSED** | The live author program docstring and printed header, its canonical transcript, `main.tex`, `README.md`, `PAPER_PLAN.md`, `CLAIMS_EVIDENCE.md`, `NARRATIVE_REPORT.md`, and `SELF_QA.md` consistently type that program as an author/scout-derived regression control.  Any Round-0 wording is explicitly historical.  The Review-A bit-mask and Review-B string-state implementations alone are described as independent cross-checks. |

The source checks supporting `P176-B-m01` were direct checks of the publisher
PDFs: H\o yer--\v Spalek, Section 3.2, uses ``rotation by Hamming weight'' for
a quantum phase rotation; Gro\v sek--Hromada studies coordinate-rotation
equivalence classes of fixed-weight binary vectors; and Gupta et al. studies
literal circular shifts, rotation equivalence/distance, weight, and
complementation.  This closes the attribution defect without changing the
paper's residual claim or granting contribution credit to standard necklace
facts.

Fresh executable receipts are likewise unchanged in substance:

```text
author/scout-derived control: 2,828,503 assertions, PASS
author transcript SHA-256:     3d0947a4df32f8e583e28d1964a52523602d61c64dde7b259bfdd15e71e4003b
Review-B independent control: 19,758,014 assertions, PASS
Review-B transcript SHA-256:   e79813f77b0dd7acfbce32eecda876f2a1b074aa5fe7220be57d9946f83ad128
transition-clock digest:       a3c10b5b7c7d35801ba595e56a91aa08e51b65545bbe9fa7426948359efcd455
```

The fresh author output was byte-identical to its checked-in transcript, and
the fresh Review-B output was byte-identical to its independently generated
transcript.  The live source and PDF hashes at acceptance were

```text
main.tex:        ff1f7d45c7ac7146a06f737a7187a9cedd451591ab9cbffeccf2d35eadc5874a
references.bib:  f47ccab745c702d4024276abb40d0fa5426df71cbab1e461749b9c609aab7307
main.pdf:        c13ca3f5e3673bb5dd9c01bdf7c8913f78425cdbfeb2a52e2d9b096a34122db4
main_round2.pdf: c13ca3f5e3673bb5dd9c01bdf7c8913f78425cdbfeb2a52e2d9b096a34122db4
```

The two PDF files are byte-identical, four pages long, and 397,525 bytes.
Settled logs have no LaTeX warning, undefined reference, rerun request, or bad
box; all 31 font rows are embedded and subsetted; all-page visual inspection,
metadata inspection, anonymity, and the visible hold pass.  Immediately before
this closure paragraph was appended, the paper-local `SHA256SUMS` had exactly
46 entries, exactly covered every paper-directory file other than itself, and
passed `46/46`.  Because appending this paragraph necessarily changes the
review-report bytes, the package maintainer must regenerate that aggregate
manifest after the purely mechanical pending-to-closed ledger synchronization.
That housekeeping step does not reopen either substantive finding.

No new mathematical, attribution, provenance, boundary, build, or packaging
finding arose in the delta audit.  Section 10's ``pending'' sentence records
the author's pre-acceptance state and is superseded by this section.  The final
Review-B disposition is therefore

```text
0 OPEN / ALL REVIEW-B FINDINGS CLOSED
AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL
```

The unresolved direct-owner search is a lifecycle gate, not an open Review-B
finding.  This acceptance authorizes neither external posting nor circulation,
contact, or submission.
