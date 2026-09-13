# Paper 24 — Claims and Evidence Matrix

## Evidence classes

- **L**: literal support, matrix, or inverse identity.
- **I**: symbolic inequality on one of the two open chambers.
- **D**: degree/carry induction.
- **T**: top-homogeneous-part argument in a domain.
- **A**: exact arithmetic or algebra.
- **P**: standard named theorem with assumptions checked.
- **N**: bounded novelty/portfolio evidence.

Numerical samples and computer algebra are not evidence classes for this
project.

## Formal theorem ledger

| ID | Exact claim | Evidence class | Local certificate | Scope limiter |
|---|---|---|---|---|
| C1 | $S$ and $T$ are polynomial symplectomorphisms | L | subtraction inverses and symmetric-Hessian block calculation | characteristic zero and nonzero coefficients only |
| C2 | the two competitive $V$-rows switch synchronously at $r=2$ | L | both differences equal $(m-1)(u_1-2u_2)$ | $m\ge2$ |
| C3 | the selected branch matrices are exactly $A_-,A_+$ | L | literal gradient-support rows | no alternative support profile |
| C4 | $h_m(r)$ and $\ell_m(r)$ are the exact projective maps | A | direct multiplication by $sB_mA_\pm$ | phase order fixed |
| C5 | $0<r<2\Rightarrow h_m(r)>2$ and $r>2\Rightarrow1<\ell_m(r)<2$ | I | corrected formulas for $h_m-2$, $\ell_m-1$, and $2-\ell_m$ | wall excluded |
| C6 | the ordinary seed follows the strict itinerary $-,+,-,+,\dots$ | I | $r_0=1$ and C5 | seed-specific theorem |
| C7 | fresh first-phase rows beat carried momentum coordinates | D | base step plus chamberwise inequalities | selector choice alone is insufficient |
| C8 | fresh second-phase rows beat carried position coordinates | D | chamberwise inequalities after $u_{n+1}=sB_mv_{n+1}$ | no asymptotic-in-$s$ shortcut |
| C9 | selected leading forms survive for arbitrary nonzero $A,B,C,D$ | T | unique top-homogeneous source in a domain | positivity is not used as theorem evidence |
| C10 | $q_1$ is visible for every $n\ge1$ | I/D | branch ratios $>1$ plus chamberwise comparison with both momentum coordinates | seed $n=0$ remains tied |
| C11 | $d_n=\deg(F_{m,s}^n)=u_{n,1}$ for $n\ge1$ | D/T | exact degree transport plus C10 | ordinary total degree only |
| C12 | $P=(B_mA_+)(B_mA_-)$ has the displayed entries | A | direct multiplication | reversed product is different |
| C13 | $H=m^2(2m+1)^2$ and $L=2m(m+1)$ are the eigenvalues of $P$ | A | right Perron eigenvector $(2,1)^{\mathsf T}$, trace, and determinant | $m\ge2$ |
| C14 | $\lambda_1(F_{m,s})=sm(2m+1)$ | P | $u_{2j}=(s^2P)^j\mathbf1$ and Perron asymptotics | not an entropy statement |
| C15 | the visible degree sequence satisfies $d_{n+4}=s^2(H+L)d_{n+2}-s^4HLd_n$ | A/P | Cayley–Hamilton on $s^2P$ plus visibility | no lower-order minimality claim |
| C16 | the even and odd wall gaps are exact powers of $s^2L$ | A | left eigenvector $[1,-2]$ for $C_-$ and $C_+$ | applies to the strict off-wall orbit only |
| C17 | both parity subsequences admit explicit spectral closed forms | A | diagonalization/decomposition of $P$ | closed forms are downstream from the matrix law |
| C18 | the crossed-binomial / diagonal-pure-power lemma forces the wall-fixing ratio | A | monotonic branch maps and wall-value matching | ansatz only |
| C19 | the conditional period-$k$ selector-to-monodromy statement is correct as a technique lemma | P | explicit hypotheses: unique faces, carry, nonzero leading forms, linear maps, visible Perron class | not a novelty headline |

## Exact dependencies

1. C4 depends on C2 and C3.
2. C6 uses only the seed and C5; it does not yet certify actual polynomial
   degrees.
3. C7, C8, and C9 are independent obligations. None can replace another.
4. C11 requires exact actual degree transport and visibility; the matrix law
   alone does not prove observability.
5. C14 uses C11, the parity matrix formulas, and Perron–Frobenius.
6. C15 is a scalar consequence of the matrix law and C11, not a primary
   definition.
7. C18 is strictly weaker than the explicit family theorem because it does not
   prove carry or visibility.
8. C19 is downstream technique, not a source of Paper-24 novelty.

## Inequality ledger

The reviewer must check every displayed sign, not merely the qualitative
conclusion.

| Item | Required sign |
|---|---|
| $(m-1)u_1+2u_2-2mu_2$ | same sign as $u_1-2u_2$ |
| $mu_1+u_2-(u_1+(2m-1)u_2)$ | same sign as $u_1-2u_2$ |
| $h_m(r)-2$ on $0<r<2$ | $>0$ |
| $\ell_m(r)-1$ on $r>2$ | $>0$ |
| $2-\ell_m(r)$ on $r>2$ | $>0$ |
| $2mu_2-\dfrac{u_1}{s(2m+1)}$ in the $-$ chamber | $>0$ |
| $u_1+(2m-1)u_2-\dfrac{u_2}{sm}$ in the $-$ chamber | $>0$ |
| $(m-1)u_1+2u_2-\dfrac{u_1}{s(2m+1)}$ in the $+$ chamber | $>0$ |
| $mu_1+u_2-\dfrac{u_2}{sm}$ in the $+$ chamber | $>0$ |
| $u_{n+1,1}-u_{n+1,2}$ | $>0$ for $n\ge0$ after one complete step |
| $u_{n+1,1}-v_{n+1,2}$ in the $-$ chamber | $>0$ via the exact equality $u_{n+1,1}=smh_m(r_n)v_{n+1,2}$ |
| $u_{n+1,1}-v_{n+1,2}$ in the $+$ chamber | $>0$ by direct expansion |

## Anti-claim ledger

| Forbidden enlargement | Correct replacement |
|---|---|
| theorem on the wall $r=2$ | wall is an excluded tie boundary |
| all two-binomial support profiles | one explicit $m,s$ family plus one bounded ansatz lemma |
| arbitrary period or automaton realization | strict period two only |
| positivity-only coefficient theorem | arbitrary nonzero coefficients via domain/top homogeneous parts |
| positive-characteristic validity | characteristic zero only |
| novelty of the period-$k$ monodromy lemma | technical downstream proposition |
| maximal or necessary selector fan | one explicit sufficient switching mechanism |
| first Perron realization or first tropical switching result | bounded explicit-family contribution only |

## Counterexample and assumption-failure ledger

| Changed assumption | Exact proof failure |
|---|---|
| $r=2$ | both competitive $V$-rows tie exactly |
| $m=1$ | the common factor $(m-1)(u_1-2u_2)$ vanishes and the switching story collapses |
| zero coefficient in $A,B,C,D$ | support profile changes, so the theorem changes |
| positive characteristic | derivative scalars can vanish |
| omitted carry proof | weighted support no longer certifies actual polynomial degrees |
| omitted visibility proof | $u_{n,1}$ is only a candidate observable, not the certified total degree |
| $R=1$ in the structural lemma | the ordinary seed lies on the wall, so no strict seed theorem follows |

## Manuscript completeness gate

A future manuscript is incomplete unless it locally contains:

1. the literal gradients and inverses;
2. the corrected branch algebra for both chambers;
3. both temporal carry phases;
4. the arbitrary-nonzero-coefficient top-homogeneous survival proof;
5. $q_1$ visibility against all four coordinates;
6. the matrix product, spectral derivation, recurrence, wall gaps, and parity
   closed forms;
7. the bounded structural lemma and the conditional period-$k$ lemma with
   their scope warnings;
8. the wall, $m=1$, $R=1$, positive-characteristic, and zero-coefficient
   failure boundaries.
