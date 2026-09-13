# Paper 24 — Proof-Obligation Verification Plan

## Authorization state

This project is opened only for a proof-first source-design package. The
directory name `experiments/` is a repository convention; no scientific
experiment, dataset, code, parameter sweep, floating-point computation,
computer algebra certificate, GPU run, or finite-iterate search is authorized
or needed for the headline theorem.

The frozen family is

$$
V_m(q)=Aq_1^m q_2^2+Bq_1q_2^{2m},
\qquad
W_{m,s}(p)=Cp_1^{s(2m+1)+1}+Dp_2^{sm+1},
$$

$$
S(q,p)=(q,p+\nabla V_m(q)),
\qquad
T(q,p)=(q+\nabla W_{m,s}(p),p),
\qquad
F_{m,s}=T\circ S,
$$

over a characteristic-zero field, with integers $m\ge2$, $s\ge1$, and
arbitrary nonzero coefficients $A,B,C,D$.

## Zero-science rule

The following are forbidden as theorem evidence:

- sampled degree orbits;
- floating-point eigenvalues, eigenvectors, or spectral radii;
- CAS matrix multiplication, factorization, recurrence fitting, or inequality
  solving;
- finite scans in $m$, $s$, coefficient signs, or primes;
- code, data, plots, timing tables, numerical certificates, or GPU work.

Arithmetic may be recomputed by a later reviewer as a private falsification
aid, but every accepted identity must have a written derivation in
`notes/PROOF_PACKAGE.md`.

## Proof-only verification sequence

| ID | Hand-check obligation | Acceptance condition | Failure action |
|---|---|---|---|
| P01 | Differentiate $V_m$ and $W_{m,s}$ literally | all four gradient coordinates and derivative scalars are written exactly | stop on any support or scalar mismatch |
| P02 | Check exact polynomial symplecticity | subtraction inverses and symmetric Hessian blocks are explicit | stop if the displayed family is not a polynomial symplectomorphism |
| P03 | Read the selector matrices | both $V$-coordinates switch at the common wall $r=2$ and yield exactly $A_-,A_+$ | stop on any altered row or wall |
| P04 | Derive both branch maps | $h_m(r)$ and $\ell_m(r)$ are exact and use the corrected formulas for $\ell_m(r)-1$ and $2-\ell_m(r)$ | stop on any dropped factor or sign error |
| P05 | Prove strict chamber exchange | $0<r<2\Rightarrow h_m(r)>2$ and $r>2\Rightarrow 1<\ell_m(r)<2$ | stop if the wall is treated as part of the theorem |
| P06 | Check base carry | the first selected $S$-rows beat the degree-one momentum seed and the first $T$-rows beat the carried position seed | stop if selector choice is conflated with temporal carry |
| P07 | Check later first-phase carry | in both chambers, the fresh $V$-rows beat the carried momentum coordinates | stop on any phase-index confusion |
| P08 | Check later second-phase carry | in both chambers, the pure $W$-rows beat the carried position coordinates | stop if a hidden asymptotic-in-$s$ argument is used |
| P09 | Prove top-homogeneous survival | arbitrary nonzero $A,B,C,D$ survive by a domain/top-homogeneous-part argument | stop if positivity of coefficients is used as theorem evidence |
| P10 | Prove visibility | $q_1$ beats $q_2$ and both momentum coordinates for every $n\ge1$ | stop if strict visibility is asserted at the tied seed |
| P11 | Multiply the monodromy | $P=(B_mA_+)(B_mA_-)$, not $(B_mA_-)(B_mA_+)$, and the displayed entries are exact | stop on a reversed product or altered entry |
| P12 | Close the spectrum | $H=m^2(2m+1)^2$, $L=2m(m+1)$, $\lambda_1=sm(2m+1)$, and the stride-two recurrence are all derived by hand | stop on interpolation or black-box factorization |
| P13 | Prove exact wall gaps and parity laws | even and odd gap formulas and parity subsequences are written exactly | stop if parity is described only qualitatively |
| P14 | Separate the bounded structural lemma | wall-fixing classification in the crossed-binomial / two-pure-power ansatz is proved separately from carry and visibility | stop on any overclaim beyond the ansatz |
| P15 | State the conditional period-$k$ lemma correctly | unique strict faces, strict carry, nonzero leading forms, linear face maps, and a visible Perron class are all explicit hypotheses | stop if the lemma is promoted as standalone novelty |

## Reproducibility worksheets

### W1 — Selector wall ledger

Record, for each competitive $V$-row:

1. the mixed exponent vector;
2. the pure exponent vector;
3. the mixed-minus-pure weighted score;
4. the common factor $(m-1)(u_1-2u_2)$;
5. the selected matrix row in the chambers $r<2$ and $r>2$.

The branch calculations must visibly preserve the corrected identities

$$
\ell_m(r)-1=
\frac{(m^2-m-1)r+3m+2}{m(mr+1)},
$$

$$
2-\ell_m(r)=
\frac{(m+1)(r-2)}{m(mr+1)}.
$$

### W2 — Carry ledger

Use the exact phase indexing

$$
u_n=\deg_q(F_{m,s}^n),
\qquad
v_{n+1}=\deg_p\bigl(S(F_{m,s}^n)\bigr),
$$

and check:

1. the base step $A_-(1,1)^{\mathsf T}>(1,1)^{\mathsf T}$;
2. the chamber-$-$ inequalities
   $$
   2mu_2>\frac{u_1}{s(2m+1)},
   \qquad
   u_1+(2m-1)u_2>\frac{u_2}{sm};
   $$
3. the chamber-$+$ inequalities
   $$
   (m-1)u_1+2u_2>\frac{u_1}{s(2m+1)},
   \qquad
   mu_1+u_2>\frac{u_2}{sm};
   $$
4. the corresponding second-phase inequalities
   $$
   s(2m+1)v_1>u_1,
   \qquad
   smv_2>u_2.
   $$

### W3 — Visibility and gap ledger

Check:

1. $h_m(r)>2$ and $1<\ell_m(r)<2$, hence $u_{n,1}>u_{n,2}$ for every
   $n\ge1$;
2. in the negative chamber, the exact identity
   $$
   u_{n+1,1}=sm\,h_m(r_n)\,v_{n+1,2}>v_{n+1,2};
   $$
3. in the positive chamber,
   $$
   u_{n+1,1}-v_{n+1,2}
   =s(2m+1)\bigl((m-1)u_{n,1}+2u_{n,2}\bigr)-(mu_{n,1}+u_{n,2})>0;
   $$
4. the left-eigenvector identities
   $$
   [1,-2]C_-=-2ms[1,-2],
   \qquad
   [1,-2]C_+=-(m+1)s[1,-2].
   $$

### W4 — Spectral and integrality ledger

Record:

1. the explicit product
   $$
   P=(B_mA_+)(B_mA_-);
   $$
2. the right Perron eigenvector $(2,1)^{\mathsf T}$ for $H$;
3. the trace and determinant giving the companion eigenvalue $L$;
4. the even/odd formulas
   $$
   u_{2j}=(s^2P)^j(1,1)^{\mathsf T},
   \qquad
   u_{2j+1}=sB_mA_-(s^2P)^j(1,1)^{\mathsf T};
   $$
5. the stride-two recurrence and parity closed forms for $d_{2j}$ and
   $d_{2j+1}$;
6. the integrality explanation from the matrix formula and integer-coefficient
   recurrence, not from denominator divisibility folklore.

## Credible manuscript mass

A proof-first article of roughly 24--28 content pages is credible:

| Component | Pages |
|---|---:|
| motivation, theorem, bounded related work | 3 |
| family, symplecticity, supports, selectors, and branch algebra | 5 |
| strict chamber exchange and both carry phases | 5 |
| arbitrary-coefficient survival and visibility | 4 |
| monodromy, recurrence, wall gaps, and parity closed forms | 5 |
| structural lemma, conditional period-$k$ lemma, and boundaries | 4 |
| total target | 26 |

References, governance records, hashes, internal paths, and discovery history
do not count toward article content.

## Failure policy

Any failed item P01--P15 blocks the corresponding headline. It may not be
repaired by sampled computation or by silently changing the family. The
permitted responses are a written correction, a narrower theorem, or a
candidate block followed by a new review.
