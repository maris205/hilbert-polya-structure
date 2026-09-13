# Paper 23 — Proof-Obligation Verification Plan

## Authorization state

This directory name is inherited from the repository convention.  Paper 23
requires no scientific experiment, dataset, code, parameter sweep, numerical
eigenvalue calculation, computer algebra certificate, or finite-iterate
validation.  The only authorized work at this stage is hand-checking the
finite symbolic proof obligations listed below.

The frozen family is

$$
S_g^+(q,p)=(q,p+\nabla V_g(q)),\qquad
T_g^+(q,p)=(q+\nabla W_g(p),p),\qquad
F_g=T_g^+\circ S_g^+,
$$

over a characteristic-zero field, with integer $g\ge 10$.  A minus sign,
reversed phase order, changed support, changed coefficient, or positive-
characteristic field is a different problem and must not be tested into the
present theorem.

## Zero-science rule

The following are forbidden as theorem evidence:

- sampled orbits of degree vectors;
- floating-point spectra or eigenvectors;
- CAS matrix products, determinants, factorizations, or inequality solvers;
- finite scans in $g$ or over prime moduli;
- code, data, plots, tables of experimental measurements, or GPU work.

Arithmetic may be recomputed by a later reviewer, but every accepted identity
must have a written derivation in `notes/PROOF_PACKAGE.md`.

## Proof-only verification sequence

| ID | Hand-check obligation | Acceptance condition | Failure action |
|---|---|---|---|
| P01 | Differentiate $V_g$ and $W_g$ | all eight gradient rows and coefficients are written literally | stop on any support or coefficient mismatch |
| P02 | Check canonicality | triangular inverses exist and both Hessians give symplectic Jacobian blocks | stop if the displayed positive-sign maps are not polynomial symplectic automorphisms |
| P03 | Read $A_g$ and $B_g$ from supports | phase one is $A_g$, phase two is $B_g$, and the full step is $C_g=B_gA_g$ | stop on reversed order or altered entry |
| P04 | Derive four selector gaps | both second-phase gaps are evaluated at $v=A_gu$ | stop on a tie anywhere in the declared cone |
| P05 | Check seed and threshold | $\mathbf1$ lies in the cone for $g\ge10$; the $g=9$ failure is displayed | weaken wording if any broader sharpness is suggested |
| P06 | Prove every cone face | all lower, ordering, ratio, and height faces return under $C_g$ | stop if even one face is supported only by samples |
| P07 | Prove both carries | fresh $p$ rows beat inherited $p$ rows and fresh $q$ rows beat inherited $q$ rows | stop if internal selection is confused with temporal carry |
| P08 | Prove leading-form survival | positive integer coefficient paths remain nonzero in characteristic zero | stop for arbitrary signs or positive characteristic |
| P09 | Prove $q_4$ visibility | $q_4$ beats the other three $q$ rows and all four $p$ rows for $n\ge1$ | stop if visibility is asserted at the tied seed |
| P10 | Derive the quartic | trace, six $2\times2$ principal minors, four $3\times3$ principal minors, and determinant reproduce $R_g$ | stop on any coefficient mismatch |
| P11 | Prove the modular certificate | all five roots and all four constant-term quadratic cases are excluded by hand | stop if a computer factorization is substituted |
| P12 | Audit the support-profile explanation | the common-kernel lemma is correct, nonnovel, and not promoted to a classification | stop on a general full-rank-implies-quartic claim |

## Reproducibility worksheets

### W1 — Support and phase ledger

Record, row by row:

1. the mixed exponent vector;
2. any pure exponent vector;
3. the pure-minus-mixed score;
4. whether the row is competitive or rigid;
5. the row of $A_g$ or $B_g$ selected by the proof.

The phase boundary must remain visible: $S_g^+$ reads $u$, whereas $T_g^+$
reads $v=A_gu$.

### W2 — Ratio-cone ledger

Normalize a positive vector by

$$
u=u_1(1,x,y,z)^{\mathsf T}
$$

and check the sufficient cone

$$
1\le x\le \frac{g-1}{g-2},\qquad
1\le y\le z\le \frac{g-1}{g-2}y,\qquad
y+z<\frac{g-5}{2}.
$$

The target ledger must contain separate expressions for $X'-1$,
$a_g-X'$, $Y'-1$, $Z'-Y'$, $a_gY'-Z'$, and
$H_g-Y'-Z'$.  No assertion of maximality or equivalence to every other
sufficient cone is allowed.

### W3 — Carry and coefficient ledger

Check

$$
A_g\mathbf1>\mathbf1,\qquad
(C_g-I_4)u>0,
$$

then use $u_n-u_{n-1}>0$ to prove

$$
A_g(u_n-u_{n-1})>0.
$$

Separately record that the positive-sign gradients use only positive integer
coefficients and that characteristic zero is needed to keep every positive
selected coefficient nonzero.

### W4 — Visibility ledger

Check $C_g-A_g>0$ entrywise.  Then subtract the fourth row of $C_g$ from
the first three rows in the correct direction and prove the resulting three
positive margins on the cone.  The output must distinguish the tied $n=0$
seed from strict visibility for $n\ge1$.

### W5 — Spectral and arithmetic ledger

List every principal minor used in the characteristic polynomial, factor
$\det C_g$ through $\det A_g\det B_g$, evaluate $R_g(1)$, and write the
complete coefficient comparison for a hypothetical factorization

$$
t^4-2t^3-t^2+1=(t^2+at+b)(t^2+ct+d)
$$

over $\mathbf F_5$.

## Credible manuscript mass

A proof-first article of approximately 24--28 content pages is credible:

| Component | Pages |
|---|---:|
| motivation, exact claim, and bounded related work | 3 |
| family, symplecticity, support profile, and matrices | 4 |
| four selectors and ratio cone | 5 |
| cone invariance, carry, and leading forms | 6 |
| visibility and exact degree | 3 |
| quartic spectrum and modular irreducibility | 4 |
| boundary and limitations | 2 |
| total target | 27 |

References, governance records, hashes, internal paths, and discovery history
do not count toward article content.

## Failure policy

Any failed item P01--P12 blocks the corresponding headline.  It may not be
repaired by finite computation or by silently changing the family.  The
permitted responses are a written correction, a narrower theorem, or a
candidate block followed by a new review.
