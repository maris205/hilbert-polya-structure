# Paper 23 — Claims and Evidence Matrix

## Evidence classes

- **L**: literal support or matrix identity.
- **I**: symbolic inequality valid on the declared cone.
- **D**: degree/carry induction.
- **C**: positive-coefficient characteristic-zero survival.
- **A**: exact arithmetic or algebra.
- **P**: standard named theorem with assumptions checked.
- **N**: bounded novelty/portfolio evidence.

Numerical samples and computer algebra are not evidence classes for this
project.

## Formal theorem ledger

| ID | Exact claim | Evidence class | Local certificate | Scope limiter |
|---|---|---|---|---|
| C1 | $S_g^+$ and $T_g^+$ are polynomial symplectic automorphisms | L | subtraction inverses and symmetric-Hessian block calculation | positive signs fixed only for the theorem family |
| C2 | exactly four gradient rows are competitive | L | complete eight-row support ledger | no arbitrary added supports |
| C3 | the selected phase matrices are $A_g,B_g$ and $C_g=B_gA_g$ | L | row reading and displayed multiplication | phase order cannot be reversed |
| C4 | all four pure branches are strict on $\mathcal K_g$ | I | four normalized gap formulas and lower bounds | integer $g\ge10$ |
| C5 | $\mathbf1\in\mathcal K_g$ | I | $(x,y,z)=(1,1,1)$ and $2<(g-5)/2$ | fails as strict height at $g=9$ |
| C6 | $C_g\mathcal K_g\subseteq\mathcal K_g$ | I | six target-face numerators, including strict height bound | cone is sufficient, not maximal |
| C7 | fresh rows beat carried rows in both phases | D | $A_g\mathbf1>\mathbf1$, $C_g-I_4>0$, and $A_g(u_n-u_{n-1})>0$ | relies on established phase indices |
| C8 | selected leading forms never cancel | C | forward iterates lie in the nonnegative integer coefficient semiring | no arbitrary signs or positive characteristic |
| C9 | $u_n=C_g^n\mathbf1$ and $v_n=A_gC_g^{n-1}\mathbf1$ | L/I/D/C | simultaneous phase induction | $v_n$ statement starts at $n=1$ |
| C10 | $q_4$ is uniquely visible for $n\ge1$ | I/D | three fourth-row differences and $C_g-A_g>0$ | all eight coordinates tie at $n=0$ |
| C11 | $\deg(F_g^n)=e_4^{\mathsf T}C_g^n\mathbf1$ | D/C | C9 and C10, with tied identity case separate | ordinary total degree only |
| C12 | the displayed $R_g(t)$ equals $\chi_{C_g}(t)$ | A | trace, six second-order minors, four third-order minors, determinant | no interpolation in $g$ |
| C13 | the visible degree sequence obeys the displayed order-four recurrence | A/P | Cayley–Hamilton applied to C11 and C12 | no lower-order minimality claim for every $g$ |
| C14 | $\lambda_1(F_g)=\rho(C_g)$ | P | exact visible sequence and primitive positive-matrix asymptotics | not an entropy statement |
| C15 | $R_g$ is irreducible for $g\equiv3\pmod5$ | A | five root evaluations and all monic quadratic constant cases | no other residue class certified |
| C16 | the certified spectral radii are distinct quartic Perron numbers | A/P | irreducibility, Perron–Frobenius, and the $t^3$ coefficient | subfamily $g=13,18,23,\ldots$ only |
| C17 | the common-kernel support profile forces unit eigenvectors in the abstract setup | L | one-line action on the common kernel plus dimension bound | explanatory and nonnovel |
| C18 | the displayed four-spike profile has no such common kernel and $1$ is not an eigenvalue | L/A | exact kernels/profile span and $R_g(1)\ne0$ | does not imply every full-rank profile is quartic |

## Exact evidence dependencies

1. C3 depends on C2 and the fixed composition order.
2. C4 must be proved before C6 is used as an iterated recurrence.
3. C7 separates support selection from temporal carry; neither implies the
   other.
4. C8 is necessary before a formal weighted-degree maximum becomes an actual
   polynomial degree.
5. C9 depends jointly on C4--C8.
6. C11 depends on both the phase recurrence and the visibility comparison;
   the characteristic polynomial cannot establish visibility retroactively.
7. C14 depends on C11, positivity of $C_g$, and Perron–Frobenius; it does not
   follow from the matrix spectrum alone.
8. C16 depends on C15 and on every conjugate of the irreducible quartic being
   an eigenvalue of the primitive matrix.
9. C17 explains the predecessor collapse but supplies no positive quartic
   theorem without C1--C16.

## Exact inequality ledger

With

$$
a_g=\frac{g-1}{g-2},\qquad H_g=\frac{g-5}{2},
$$

the declared cone is

$$
1\le x\le a_g,qquad 1\le y\le z\le a_gy,qquad y+z<H_g.
$$

The independent reviewer must check all of the following, not a subset:

| Item | Required sign |
|---|---|
| $\Delta_{S,1}=(g-2)-2(x+y+z)$ | $>0$ |
| $\Delta_{S,2}=(g-3)x-2(1+y+z)$ | $>0$ |
| $\Delta_{T,3}=-8-6x+(g-7)y+(2g-8)z$ | $>0$ |
| $\Delta_{T,4}=-6-4x+(2g-6)y+(g-6)z$ | $>0$ |
| $X'-1$ | $\ge0$ |
| $a_g-X'$ | $>0$ |
| $Y'-1$ | $>0$ |
| $Z'-Y'$ | $>0$ |
| $a_gY'-Z'$ | $\ge0$ |
| $H_g-Y'-Z'$ | $>0$ |

Closed ratio/order faces are intentional; selector gaps and the height face
remain strict, so no selected support tie is introduced.

## Anti-claim ledger

| Forbidden enlargement | Correct replacement |
|---|---|
| all four-mode Hamiltonian shears | one displayed positive-sign family |
| all $g$, or globally sharp $g=10$ | $g\ge10$ for this seed and four-face itinerary |
| maximal or necessary cone | one explicit sufficient invariant ratio cone |
| sign-invariant degree growth | positive integer coefficients and characteristic-zero no-cancellation |
| quartic algebraic degree for every $g$ | certified subfamily $g\equiv3\pmod5$ |
| support-profile rank as a new theorem | reused explanatory linear algebra |
| every full-rank support profile is quartic | this exact profile has the proved quartic matrix/subfamily |
| first Perron realization | restricted symplectic explicit-family result, positioned against general realization work |
| entropy, integrability, conjugacy, periodicity, or genericity | no such conclusion |
| computational certificate | hand-written support, inequality, minor, and factor ledgers |
| absolute priority | no direct collision within a bounded search |

## Counterexample and assumption-failure ledger

| Changed assumption | Exact proof failure |
|---|---|
| $g=9$ | $\Delta_{S,2}(\mathbf1)=0$ and $\Delta_{T,3}(\mathbf1)=-2$ |
| subtraction or arbitrary signs | positive-semiring no-cancellation no longer applies |
| positive characteristic | derivative or accumulated positive integer coefficients can vanish |
| reversed order $S_g^+\circ T_g^+$ | the complete matrix is not the certified $B_gA_g$ |
| added monomial | support ledger and selector chamber can change |
| arbitrary nonzero coefficients | signs and cancellation can change actual degrees |
| omitted visibility proof | $e_4^{\mathsf T}C_g^n\mathbf1$ is only a candidate observable |
| mod-five root/quadratic case omitted | irreducibility is not certified |

## Manuscript completeness gate

A future manuscript is incomplete unless it locally contains C1--C18, the
inequality ledger, the principal-minor table, the $g=9$ audit, and the modular
linear/quadratic factor exclusions.  References to Papers 20--22 may explain
lineage but may not replace any theorem-critical proof.
