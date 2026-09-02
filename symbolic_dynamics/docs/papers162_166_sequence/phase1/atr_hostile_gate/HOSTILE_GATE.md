# ATR independent hostile gate

**Candidate:** alternating tropical row-normalization (`ATR`)  
**Literal map:** `T(A)=R(A)^T`, where
`R(A)_ij=A_ij-min_k A_ik` on `{0,...,q-1}^{n x n}`  
**Gate decision:** `KILL`  
**Mathematical audit:** `PASS`  
**External status:** `HOLD_EXTERNAL`  
**Severity ledger:** `0 Critical / 2 Major / 3 minor`

## Outcome first

The displayed ATR formulas survive a genuinely independent derivation and
1,602,435 exact assertions.  In particular, the two-step zero-cover formula
is not missing a compatibility condition, its potential parametrization is
bijective, the inclusion--exclusion signs are correct, and the claimed sharp
depth is correct for every `n,q>=2`.  No Critical mathematical error was
found.

The candidate nevertheless fails this batch's paper-selection threshold.
After mandatory subtraction of the Hungarian row/column-potential reduction,
the entire temporal spine is a two-pass normalization identity followed by
transpose.  Its paper architecture then repeats the already occupied P143
pattern: a full matrix carrier projects in constant depth to a core, the map
is transpose on that core, periods and zeta follow, and an every-target inverse
atlas supplies the second axis.  ATR's bounded-potential zero-cover sum is
correct and genuinely sensitive to zero placement, but it is too narrow to
carry a new short paper after both subtractions.  This is therefore a
value/allocation `KILL`, not a proof-failure kill.

## Frozen input

The four author files were read but not edited or imported by the hostile
verifier.

| author artifact | SHA-256 |
|---|---|
| `SCOUT.md` | `bde8b45b6a5adb8ebe2eedb2010e4521d2ebdfefd690f1910dd353068b45ce29` |
| `OWNER_SEARCH_LOG.md` | `6e284561a464f21064293416489a5fa8a4dd72dd8f73eb60cf89253b22d476b6` |
| `verify_atr.py` | `a38cd29feb6dd6396f186186d7992845eceb759479b03675ee05ac5fa8f85fa0` |
| `CANONICAL.txt` | `e7b73348dfdcf039e8f8ecd16a9d6514abf2520cc6b16499fc5e58c4778ed43d` |

## 1. Cold derivation of the forward dynamics

Let `B=R(A)` and put `s_j=min_i B_ij`.  Applying the literal update twice,
with both transposes written out, gives

```text
T^2(A)_ij = B_ij-s_j.                                   (H1)
```

Every column of the right side has a zero.  Every row of `B` already has a
zero; if `B_ij=0`, then necessarily `s_j=0`, so that zero survives (H1).
Thus `T^2(A)` belongs to the core `C_nq` of matrices having a zero in every
row and every column.  Conversely `T^2(C)=C` for every `C in C_nq`, so the
second image is exactly the core.  On the core row normalization is the
identity and

```text
T(C)=C^T,              T^2(C)=C,              T^4=T^2.  (H2)
```

Consequences checked independently:

- recurrent states are exactly the core;
- fixed states are exactly symmetric core matrices;
- non-symmetric core states pair into strict two-cycles, so the number of
  strict cycles is `(R_nq-F_nq)/2`, not `R_nq-F_nq`;
- the matrix whose first column is zero and whose other entries are one has
  exact depth two for every `n,q>=2`.

The hostile verifier also counted fixed points of `T^k` directly for
`1<=k<=6`: the answer is `F_nq` for odd `k` and `R_nq` for even `k`.

## 2. Inclusion--exclusion audit

For the recurrent count, choose `i` rows and `j` columns that are forbidden
to contain zero.  Their union contains `n(i+j)-ij` forced-nonzero entries and
the complement has `(n-i)(n-j)` free entries.  This rederives

```text
R_nq = sum_i,j (-1)^(i+j) C(n,i) C(n,j)
          (q-1)^(n(i+j)-ij) q^((n-i)(n-j)).             (H3)
```

For a symmetric matrix there are `N=n(n+1)/2` upper-triangular variables.
If `i` rows are forbidden to contain zero, precisely the variables outside
the complementary `(n-i) x (n-i)` symmetric block are forced nonzero.  Hence

```text
F_nq = sum_i (-1)^i C(n,i)
          (q-1)^(N-C(n-i+1,2)) q^C(n-i+1,2).           (H4)
```

This establishes both the orientation and the signs of the two formulas.
Their numerical values agree with complete enumeration in seven boxes,
including the author-unseen box `(n,q)=(2,5)`.

## 3. One- and two-step fibres

### One step

If `T(A)=Y`, each source row is uniquely

```text
A_ij=Y_ji+r_i,     0<=r_i<=q-1-max_j Y_ji.             (H5)
```

Existence is equivalent to a zero in every column of `Y`.  Multiplying the
independent row choices proves both the unweighted product and its
source-sum polynomial.  This part is elementary and correct.

### Two steps: attempted break of the zero-cover condition

Fix a core target `C`.  The unique row-normalized intermediate matrix has
the form

```text
B_ij=C_ij+s_j.                                          (H6)
```

The alphabet cap is
`0<=s_j<=q-1-max_i C_ij`.  The missing compatibility condition one might
suspect is in fact exactly the author's condition:

```text
for every row i, some j has C_ij=0 and s_j=0.           (H7)
```

Necessity follows because `B` must have row minimum zero.  Sufficiency is
immediate from (H7), and column reduction of (H6) returns `C` because every
column of `C` has minimum zero.  Finally every source above `B` is uniquely

```text
A_ij=C_ij+s_j+r_i,
0<=r_i<=q-1-max_j(C_ij+s_j).                            (H8)
```

Equations (H6)--(H8) are a bijective coordinate system, not merely a
surjective construction.  They give the author's product-sum fibre count
and the weighted exponent
`|C|+n sum_j s_j+n sum_i r_i`.  The independent verifier reconstructed
every literal source from these coordinates and compared both weighted
polynomials coefficientwise in every exhaustive box.

The zero-incidence dependence is real.  At `n=q=3`, the two core targets

```text
C1 = [0 0 0; 0 0 1; 0 1 2],
C2 = [0 0 0; 0 1 0; 0 1 2]
```

have identical row maxima `(0,1,2)`, column maxima `(0,1,2)`, entry sum
`4`, and six zero entries.  Their two-step fibres nevertheless have sizes
`10` and `8`.  Thus the formula does encode placement rather than only
coarse margins.

## 4. Depth census and a stronger closed form

The author's

```text
L_nq = sum_(C in C_nq) product_i(q-M_i(C))              (H9)
```

correctly counts sources whose first iterate is already recurrent.  It is,
however, still a sum over every core target.  A direct source-side
inclusion--exclusion removes that target sum.  For `0<=k<=n`, put

```text
g_k(n,q) = sum_(r=0)^(q-1)
             ((r+1)^(n-k)-r^(n-k)) r^k.                (H10)
```

Here `g_k` counts one row in which none of a prescribed set of `k` columns
attains the row minimum.  The first iterate is in the core exactly when the
union of all row-minimum positions covers every column.  Therefore

```text
L_nq = sum_(k=0)^n (-1)^k C(n,k) g_k(n,q)^n.            (H11)
```

The exact depth shells are consequently
`(R_nq, L_nq-R_nq, q^(n^2)-L_nq)`.  Formula (H11) was checked against the
literal depth census in all seven exhaustive boxes and structurally for
`1<=n,q<=10`.

## 5. Boundary audit

- For `n=1`, `T(a)=0`.  If `q>=2`, zero has depth zero and the other `q-1`
  states have depth one.  Thus the sharp height-two statement must retain
  `n>=2`.
- For `q=1`, the all-zero matrix is the unique state for every `n`; its
  depth is zero.  Thus the sharp height-two statement must retain `q>=2`.
- At the overlap `n=q=1`, the singleton description controls; there is no
  depth-one state.

The verifier checks these boundary formulas through `q=8` and `n=8`, and
checks the exact-depth-two witness for all `2<=n,q<=12`.

## 6. Findings by severity

### Critical: none

No false theorem, missing branch, sign error, cycle/state confusion, or
boundary contradiction was found.

### Major M1 — the temporal spine is consumed by standard assignment reduction

Two literal iterations perform row-minimum reduction and then column-minimum
reduction; the transposes merely alternate which orientation is presented.
The core, height-two clock, recurrence, and transpose periods are immediate
after this preprocessing.  Under the batch rule that a renamed standard
algorithm or bare one-step identity is below threshold, this entire temporal
axis receives zero paper credit.

**Executable repair:** none within the present literal map.  A surviving
replacement needs a different update for which the temporal theorem is not
just a packaging of row/column cost reduction.  The present identities may
be retained only as internal lemmas or control results.

### Major M2 — P143 consumes the remaining paper architecture

P143 already has: full matrices; constant-depth projection onto a structural
core; transpose on that core; fixed/strict-two-cycle/zeta enumeration; and
an every-target inverse atlas as the independent theorem axis.  P127 further
occupies full finite matrices, transpose-driven cycles, fibres, and zeta
packaging.  ATR's ordered alphabet and zero-cover potentials make the literal
fibre proof different, but after M1 the only substantial residue is that one
finite cover sum.  Difference of local proof mechanism is insufficient when
the forward and inverse architecture is already occupied.

**Executable repair:** do not promote ATR.  A replacement must change the
literal mechanism and at least one of the projection/core/involution/inverse
roles, rather than adding refinements to the current fibre polynomial.

### minor m1 — the displayed depth census is less closed than advertised

Equation (H9) is exact but ranges over all recurrent targets.  If retained as
a control result, add the source-side closed inclusion--exclusion formula
(H10)--(H11) and call (H9) a target-sum identity rather than the terminal
closed evaluation.

### minor m2 — direct-owner wording needs historical precision

Kuhn's 1955 paper is a primary owner of the Hungarian assignment framework
and dual covers, but its displayed initial cover chooses row maxima or column
maxima according to their total; it is not itself an exact statement of the
modern sequential row-minimum-then-column-minimum preprocessing.  Munkres's
publisher record confirms the later algorithmic paper.  The correct wording
is that ATR's primitive lies in the Hungarian/Kuhn--Munkres reduction lineage
and is standard zero-credit preprocessing, not that Kuhn 1955 literally
states this exact endomorphism.

### minor m3 — parts of the author structural verifier are tautological

The author check assigning `i1=image_one_formula(n,q)` and then comparing it
to the same expanded expression cannot detect an implementation error.
Also, its larger `n,q` checks test inequalities and parity rather than the
literal formulas.  The hostile verifier adds a seventh exhaustive box,
source-coordinate reconstruction, all-target weighted comparisons in all
boxes, fixed-iterate counts, a distinct depth formula, and explicit lower
bound branches.

## 7. Independent executable evidence

Run twice from the repository root:

```bash
python3 -B docs/papers162_166_sequence/phase1/atr_hostile_gate/verify_hostile.py
```

The two fresh outputs are byte-identical to `CANONICAL.txt`.  The program
imports no author module and contains its own literal update, inverse
parametrization, counters, and inclusion--exclusion formulas.  It exhausts
86,709 matrices in seven boxes:

```text
(2,2), (2,3), (2,4), (2,5), (3,2), (3,3), (4,2).
```

The replay comparison returned `REPLAY_BYTE_MATCH=0` (shell success), and a
separate process-substitution comparison returned
`CANONICAL_BYTE_MATCH=PASS`.  The frozen stdout SHA-256 is
`eb72ea9bd5b69f618e32c968408dff96b8d1c6da272148b2bad1696ab9d25ee4`.

Frozen result: `1,602,435 assertions`, `MATHEMATICS PASS`, `DECISION KILL`,
`EXTERNAL HOLD_EXTERNAL`, `STATUS PASS`.

## Final ruling

`KILL_KUHN_MUNKRES_INITIALIZATION_AND_P143_CORE_TRANSPOSE_TEMPLATE`.

The verified zero-cover inverse formula is a useful exact observation, but
it does not leave two independent paper-scale axes after mandatory owner and
internal subtraction.  A bounded owner-search non-hit is not a novelty or
priority claim, and no external circulation is authorized.
