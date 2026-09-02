# RCR adversarial specialist gate

**Gate date:** 2026-09-02  
**Role:** author-isolated specialist review of the frozen focused package  
**Decision:** `KILL_AMBER`  
**External status:** `HOLD_EXTERNAL`  
**Scope:** the present uniform two-dimensional random anchored-rectangle
contraction package only; no paper number is assigned

## 1. Required answer

**No.**  After assigning zero contribution credit to the Ross--Durrett strict
skeleton, geometric residence times, maxima of independent clocks, and tensor
transition factorization, the literal two-dimensional anchored-rectangle
carrier plus its every-target potential does **not** retain enough independent
mathematical content for a 4--6 page internal short paper.

The formulas remain exact and useful.  The failure is a contribution failure,
not a correctness failure.  Once the mandated deductions are made, the
spatial axis is obtained by summing the already-zero-credit tensor transition
over time, evaluating at `z=1`, and dividing out the already-zero-credit
one-block geometric residence.  The anchored-rectangle language adds no
coupling, geometric obstruction, new boundary phenomenon, or non-product
invariant to those operations.

## 2. Materials reread and owner subtraction

The gate reread in full:

- `DERIVATION_PACKAGE.md`;
- `PROOF_PACKAGE.md`;
- `THEOREM_CONTRACT.md`;
- `OWNER_FOCUSED_AUDIT.md`;
- `verify_rcr_focused.py`; and
- the frozen `CANONICAL.txt` transcript.

The decisive primary/authoritative owner facts were checked again rather than
accepted from the candidate narrative:

1. Sheldon Ross's 1982 paper, [“A Simple Heuristic Approach to Simplex
   Efficiency”](https://www.sciencedirect.com/science/article/pii/0377221782901771),
   takes the next rank uniformly among the `j-1` better ranks.  This is exactly
   the RCR coordinate chain after deleting self-loops.
2. Richard Durrett's official *Essentials of Stochastic Processes*, Version
   3.9, [Exercise 1.69](https://services.math.duke.edu/~rtd/EOSP/EOSP2021.pdf),
   prints the same strict kernel, its harmonic mean, the conditional level-hit
   probability `1/j`, and independence of the level-visit indicators.

Thus the strict descent and its visit mechanism are direct hits, not merely
nearby analogies.  Adding the self-loop at level `k` gives an elementary
geometric residence block; multiplying those owned visit mixtures gives the
lazy-coordinate product transform.  No contribution is restored by calling
the Cartesian product state an anchored rectangle.  The bounded failure to
find a paper with that literal title or carrier remains only a non-hit and is
not novelty evidence.

## 3. Formula-by-formula adversarial audit

The following audit deliberately probes the degenerate starts, unit sides,
time-zero convention, alternating coefficient signs, convergence disks, and
possible pole cancellation.  “Correct” means correct under the theorem
contract's stated conventions; it does not award contribution credit.

| formula | boundary/sign/radius attack | verdict |
|---|---|---|
| **B4** | The tail identity `G_T(z)=1+(z-1)sum_(t>=0)P(T>t)z^t` gives the two positive coordinate sums and the negative product sum.  At `(1,1)` all sums are empty and the value is one; with one unit side it reduces to the other coordinate PGF.  At `z=0` and `z=1` it gives the correct mass and normalization.  For every nonabsorbing start the uncancelled `r=2` coordinate residue has total tail coefficient `a+b-2>0`; every product pole has `rs>=4`. | **Correct.** Exact PGF radius two; no sign or unit-side error. |
| **B5** | Summing a term `q^t` gives `(1-q)^(-1)`: hence `q=1/r` gives `r/(r-1)` and `q=1/(rs)` gives `rs/(rs-1)`.  The product term retains the minus sign.  Empty sums give zero at `(1,1)` and the one-coordinate mean on a unit-side boundary. | **Correct.** |
| **B6** | The raw-second-moment tail factor is `(1+q)/(1-q)^2`; substitution gives exactly `r(r+1)/(r-1)^2` and `rs(rs+1)/(rs-1)^2`.  This is explicitly a raw second moment, not a variance. | **Correct.** |
| **B7** | A nonabsorbing rectangle hits in one step only by selecting `(1,1)`, of probability `1/(ab)`.  At least one nontrivial coordinate clock has positive mass at every positive integer, so the maximum has full positive support.  The `2^(-t)` product contribution cannot occur because `rs>=4`; the surviving coefficient is `(a-1)+(b-1)`. | **Correct.** The absorbing start is separately and correctly excluded from the atom/support clauses. |
| **B8** | For `a,b>=2`, independence and full positive support make each event `H_a>H_b` and `H_b>H_a` positive, so the lower inequality is strict.  Also `min(H_a,H_b)>=1`, making the upper inequality strict.  If a side is one, its clock is zero and equality with the other clock is mandatory. | **Correct.** |
| **C2** | At `t=0`, the alternating sums satisfy `sum_(r=k)^m C_(m,k;r)=1_{m=k}`, so the double sum is the correct Kronecker delta.  For target `(1,1)` the `(r,s)=(1,1)` coefficient is one and all other modes decay.  The sign is the product `(-1)^(r-i+s-j)`, as printed. | **Correct.** Inaccessible targets must remain outside the displayed accessible range and are correctly assigned zero later. |
| **C3** | For an accessible transient target, the smallest product is uniquely `ij`, with positive coefficient `C_(a,i;i)C_(b,j;j)`, so the occupation-series radius is exactly `ij`; for `(1,1)` it is exactly one.  The finite rational expression is its continuation beyond that disk. | **Correct, with a precision debt only.** The derivation says “in its disk,” but a future statement should print `|z|<ij` for transient targets and `|z|<1` for the absorbing target explicitly.  No contrary radius is presently claimed. |
| **C4** | Evaluation at `z=1` is legal exactly when `ij>1`; then every denominator has `rs>1`.  It is not legal for the absorbing target, which is separated in C7.  A transient target with one coordinate equal to one still has `ij>1`. | **Correct.** |
| **C5** | Conditional on reaching `(i,j)`, one visit block has continuation probability `1/(ij)` and mean length `ij/(ij-1)`.  Therefore hit probability is `(ij-1)K/(ij)`.  Starting at the target gives `K=ij/(ij-1)` and probability one; inaccessible targets give zero. | **Correct.** |
| **C6** | Strong Markov factorization gives `U_start,target(z)=F_start,target(z)/(1-z/(ij))`, including the time-zero atom when start equals target.  Multiplication gives the printed defective first-hit transform.  The equality first holds on the occupation disk and then rationally; cancellation may enlarge the first-hit transform's own disk, but no exact radius for it is asserted. | **Correct.** No boundary, sign, or stated-radius error. |
| **C7** | Since `(1,1)` is permanently occupied from time `T` onward, `sum_(t>=0)z^t P(T<=t)=E[z^T]/(1-z)` for `|z|<1`.  This includes `T=0` at the absorbing start and correctly diverges at `z=1`. | **Correct.** |

No theorem-breaking boundary, sign, or radius error was found in B4--B8 or
C2--C7.  The sole precision debt is that C3's exact power-series disk is
implicit in the theorem contract rather than printed numerically; the
derivation supplies the necessary qualification.

## 4. Independent cold replay

Two new interpreter processes were run with bytecode generation disabled:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers157_161_sequence/phase1/rcr/verify_rcr_focused.py
```

Both exits were zero, their stdout was byte-for-byte identical, and each was
byte-for-byte identical to `CANONICAL.txt`.  No `__pycache__` directory was
created.

```text
A lane:  3,062 assertions PASS
B lane: 26,880 assertions PASS
C lane: 20,131 assertions PASS
TOTAL:  50,073 assertions PASS

CANONICAL/stdout SHA256:
2d79daddd9369286f8713100a5ff9688f67b5c3775e2c84604c7000963d6164d

verifier SHA256:
258143e457e1674c612e85e8b5f8b4861a5b2ac91d289a400c973227cd1654c2
```

This is finite exact falsification pressure only.  It neither repairs the
contribution deficit nor upgrades a bounded owner non-hit.

## 5. Owner-subtracted contribution ledger

| candidate content | mathematical status | contribution after the required subtraction |
|---|---|---|
| B4--B8 | exact finite formulas and consequences | zero: tail summation and elementary consequences of an independent maximum |
| C2 | exact every-time/every-target transition | zero by the gate premise: literal tensor transition |
| C3 | exact synchronized potential | zero: termwise geometric summation of C2, i.e. the standard resolvent of the product chain |
| C4 | transient Green kernel | zero: evaluation of C3 at `z=1` |
| C5 | visit probability | zero: C4 divided by the elementary geometric residence block |
| C6 | first-hit transform | zero: standard strong-Markov factorization by the same residence block |
| C7 | absorbing-target potential | zero: universal occupation-after-hitting identity |
| “anchored rectangle” carrier | a valid literal realization | descriptive packaging only; no interaction between axes and no residual spatial theorem |

The every-target law is not recoverable from the scalar absorption-time
distribution alone, but that logical distinction is insufficient.  It is
recoverable immediately from the zero-credit tensor transition together with
standard resolvent and one-block identities.  “A second observable” is
therefore not, by itself, a second contribution axis.

## 6. Gate decision

```text
KILL_AMBER
```

Minimal reason: the package is mathematically sound, but after the required
owner and method deductions no independent theorem remains; the only residual
is a literal name plus a routine product-chain potential.  That residual does
not support a 4--6 page internal short paper under the present portfolio
standard.

Accordingly, no `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, or
`CLAIMS_EVIDENCE.md` is generated.  A future non-product update, genuinely
coupled spatial statistic, or owner-distinct qualitative theorem would be a
new candidate rather than a continuation of this gate.  Numbering, TeX
drafting, Git synchronization, posting, circulation, and external claims all
remain prohibited under `HOLD_EXTERNAL`.
