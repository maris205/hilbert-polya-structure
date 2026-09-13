# Paper 28 claims--evidence matrix

Status: source-design author stop pending independent review  
Claim family: exact proof; no empirical support  
Public quantifier: one map \(F_{\mathsf w}\) per rooted primitive word

## Conjunctive evidence table

| ID | Public claim | Required hypotheses and side information | Exact evidence | Negative control / boundary | Planned main-body location |
|---|---|---|---|---|---|
| C01 | \(F_{\mathsf w}=\Pi_P\circ T_W\circ S_V\) is a polynomial symplectomorphism with polynomial inverse. | Characteristic-zero field for the later degree theorem; polynomial V and W; simultaneous permutation. | Symmetric-Hessian block computation and explicit reverse-order inverse in Proof P1. | Permuting q and p differently need not preserve the standard form. | Construction, Proposition 2.1. |
| C02 | A uniquely selected V monomial transports q weights by \(A_\alpha=\mathbf1\alpha^{\mathsf T}-I\), and a W monomial by \(B_\beta\). | Positive weights; collected support; unique selector; nonzero relevant derivative scalar. | Rowwise derivative degree calculation, Proof P2. | Positive characteristic can annihilate an exponent scalar. | Degree transport, Lemma 2.3. |
| C03 | \(B_\beta A_\alpha=I+\mathbf1((D-1)\alpha-\beta)^{\mathsf T}\) in the equal-total construction. | \(|\alpha|=|\beta|=D\). | Literal rank-one multiplication, Proof P3. | Unequal totals change the diagonal eigenvalue and selector reduction. | Degree transport, Lemma 2.4. |
| C04 | The strict selector word is feasible iff the seed lies in the pulled-back V-max/W-min normal-fan intersection. | Positive equal-total supports; fixed P; strict unique comparisons; selector statement only. | Diagonal-translation cancellation and W sign reversal, Proof P4. | Equality-wall seed produces a tie; unequal totals reintroduce \(t_n\). | Normal-fan theorem, Theorem 3.2. |
| C05 | Every rooted primitive pair word of length \(\ell\ge3\) has an explicit nonempty incidence realization. | \(r=\ell+1\), moving cycle plus fixed star, \(H\ge2,\rho\ge2,K\ge1\). | Exact incidence score table, Proof P5. | \(H=1\) collapses all score gaps and quotient phases. | Realization theorem, Theorem 4.1. |
| C06 | Every existing selector competitor is separated by exactly \(g=K(H-1)\). | Competitor set nonempty. | Two-valued score table, Proof P5. | Singleton side has vacuous uniqueness, full cone, and no finite gap. | Theorem 4.1 plus singleton remark. |
| C07 | The strict actual-degree lift holds exactly in the first-carry chamber \(0<m_0<A_{\alpha_{a_0}}u_0\). | \(r\ge2\); positive weights; all exponent coordinates at least two; strict selector seed. | Coordinate inequality, first-step necessity/sufficiency, and induction, Proof P6. | \(m_0\le u_0\) is sufficient but not necessary; dimension-one cancellation fixture. | Carry theorem, Theorem 5.1. |
| C08 | Selected leading forms survive for every nonzero coefficient tuple. | Characteristic zero; polynomial domain; positive exponent coordinates; unique selected monomials; strict carries. | Nonzero derivative scalars, product-domain argument, and lower-degree carried terms, Proof P7. | A zero coefficient changes support; a zero exponent or positive characteristic can delete a derivative term. | Leading-form proposition, Proposition 5.3. |
| C09 | \(u_n=P^nu_0+t_n\mathbf1\) and \(t_{n+1}=\lambda t_n+\mu\), with constant \(\mu>0\). | Explicit incidence realization and selected word. | Substitute the rank-one matrix; selected score is phase-independent, Proof P8. | General equal-total supports need not have constant forcing. | Cocycle setup, Lemma 6.1. |
| C10 | Prefix products and the period monodromy have the exact rank-one formulas. | Ordered matrix word; \(P\mathbf1=\mathbf1\); \(c_j^{\mathsf T}\mathbf1=\lambda-1\); \(P^\ell=I\). | Induction on \(Q_s\), Proof P9. | Reversing product order changes every rotated digit. | Monodromy theorem, Theorem 6.2. |
| C11 | \(0<(c_{a,b})_i<\lambda\) in every coordinate. | Incidence exponents; \(D=\rho(\ell+1)+K\ell\), \(\ell\ge3\), \(\rho\ge2\), \(K\ge1\). | Uniform lower and upper integer bounds, Proof P10(a). | Allowing smaller/negative support coordinates can violate the digit interval. | Decoder lemma, Lemma 7.1. |
| C12 | The pair-support map \((a,b)\mapsto c_{a,b}\) is injective. | Distinct used labels have distinct nonempty occurrence sets; \(D-1>1\). | Compare moving-coordinate differences of magnitude \(K(D-1)\) with at most \(K\), Proof P10(b). | Literal human names remain extrinsic to the vector table. | Decoder lemma, Lemma 7.2. |
| C13 | Marked monodromy decodes the rooted support-vector word without carry. | \(M\), P, \(\lambda\), \(\ell\), marked phase; labelled dictionary only for literal labels. | Coordinatewise base-\(\lambda\) uniqueness and inverse rotations, Proof P10(c). | Unmarked data yield only a cyclic class; scalar growth does not decode the word. | Decoder theorem, Theorem 7.3. |
| C14 | Selector and quotient least periods are both \(\ell\). | Pair word primitive; spike seed; fixed star; moving \(\ell\)-cycle. | Pair-word definition plus diagonal-quotient obstruction, Proof P11. | Nonprimitive word or shorter quotient orbit gives a divisor. | Period theorem, Theorem 8.1. |
| C15 | Position, coordinate, phase-subsequence, and complete-state recurrences have the stated starting indices. | Exact affine scalar recurrence; moving/star domains distinguished; first-carry domination from \(n\ge1\). | Closed forms and shift-operator substitution, Proof P12. | Momentum maximum above \(q_0\) creates defect \(\lambda(d_0-q_0)\) at \(n=0\). | Scalar consequences, Proposition 8.3. |
| C16 | The scalar recurrences are annihilators only. | None beyond C15. | Direct declaration and examples with shared scalar curves across different words. | No minimality or word-decoding inference. | Proposition 8.3 and limitations. |
| C17 | The theorem is not a collision with the closest established theories. | Bounded primary-source comparison through 2026-08-29. | Claim-by-claim citation table and local portfolio matrix. | Search misses cannot establish absolute priority. | Introduction and related work. |
| C18 | The theorem supports a 22--30 page proof-first article. | All C01--C17 proved in the main body; no empirical appendix. | Section mass budget totaling 26.5 pages. | Governance history, hashes, and internal scores do not count. | Internal planning only. |

## Proof dependency DAG

The allowed logical flow is

\[
 \mathrm{C01}
 \longrightarrow (\mathrm{C02},\mathrm{C03})
 \longrightarrow \mathrm{C04}
 \longrightarrow (\mathrm{C05},\mathrm{C06})
 \longrightarrow (\mathrm{C07},\mathrm{C08})
 \longrightarrow \mathrm{C09}
 \longrightarrow \mathrm{C10}
 \longrightarrow (\mathrm{C11},\mathrm{C12})
 \longrightarrow \mathrm{C13}
 \longrightarrow (\mathrm{C14},\mathrm{C15},\mathrm{C16}).
\]

C17 is an independent positioning obligation; C18 is a mass check after the
proof chain closes.  No arrow originates in an experiment, computation, or
literature search miss.

## Quantifier firewall

The following separations are mandatory:

1. C04 is an iff for strict selectors, not by itself an iff for the actual
   polynomial-degree lift.
2. C07 adds the exact momentum-weight condition.
3. C05 gives one map per word; no cross-word universality is inferred.
4. C06 assigns \(g\) only when a competitor exists.
5. C13 recovers algebraic support data before it recovers dictionary labels.
6. C14 concerns selector and quotient periods, not a periodic polynomial
   state.
7. C15 distinguishes \(q_n\), \(d_n\), moving \(y_n^{(i)}\), fixed-star
   \(y_n^{(\star)}\), and \(z_m^{(i,s)}\).
8. C16 forbids recurrence minimality and scalar word decoding.

## Reviewer falsification checklist

A source-design PASS requires independent answers of “yes” to all items:

- Does every formula use the ordered composition
  \(\Pi_P\circ T_W\circ S_V\)?
- Is the W selector a minimizer on the residual position weight?
- Are \(r\ge2\) and the headline \(r=\ell+1\ge4\) kept distinct?
- Is the phase-zero momentum gate strict and coordinatewise?
- Does the incidence table work with repeated labels and singleton sides?
- Are all coefficients quantified as nonzero, rather than generic?
- Are the rotated digits in the correct product order?
- Are digit bounds strict at both 0 and \(\lambda\)?
- Are marked phase and labelled dictionary listed among decoder inputs?
- Does the fixed-star argument prove least quotient period?
- Do all recurrence statements carry their literal start index?
- Is every negative boundary visible beside the affected claim?

Any “no” is a finding; finite fixtures or prior candidate PASS scores cannot
waive it.

## Public evidence policy

The eventual article may cite proofs, exact examples, counterexamples, and
primary literature.  It must omit batch identifiers, filesystem paths,
hashes, reviewer roles, internal scores, and lifecycle events.  No claim is
supported by a scientific run, CAS certificate, external message, upload, or
release action.

BATCH07_PAPER28_CLAIMS_EVIDENCE_MATRIX_FROZEN

## Controlling append-only traceability correction

Authority: `B07-E0174-P28-SOURCE-DESIGN-REVIEW-FAIL-CORRECTION-AUTHORIZATION`.
The original claims, hypotheses, negative controls, and public wording remain
unchanged.  Only their stale proof-location cells and the dependency display
are superseded by this packet.

### Canonical claim-to-proof map

| Claim | Controlling internal evidence |
|---|---|
| C01 | P1 |
| C02 | P2 |
| C03 | P2 |
| C04 | P6 |
| C05 | P7 |
| C06 | P7 |
| C07 | P3--P4 |
| C08 | P5 |
| C09 | P8 |
| C10 | P9 |
| C11 | P10 digit bounds |
| C12 | P10 pair injectivity |
| C13 | P11 |
| C14 | P12 |
| C15 | P13 |
| C16 | P13 plus its explicit anti-minimality statement |
| C17 | citation verification and novelty assessment; positioning branch independent of the mathematical proof |
| C18 | exact 26.5-page source-design allocation in `FINAL_PROPOSAL.md`; mass check only |

### Canonical dependency DAG

C01/P1 is an independent map-level branch establishing polynomial
symplecticity and inverse order.  The weighted-degree branch starts at
C02--C03/P2 and then splits:

\[
 \mathrm{C02,C03}/\mathrm{P2}
 \longrightarrow
 \begin{cases}
   \mathrm{C07}/\mathrm{P3--P4}
       \longrightarrow \mathrm{C08}/\mathrm{P5},\\
   \mathrm{C04}/\mathrm{P6}
       \longrightarrow \mathrm{C05,C06}/\mathrm{P7}.
 \end{cases}
\]

The branches rejoin in the explicit actual-degree realization.  Then

\[
 \mathrm{P7,P6}\to\mathrm{C09}/\mathrm{P8}
 \to\mathrm{C10}/\mathrm{P9}
 \to\mathrm{C11,C12}/\mathrm{P10}
 \to\mathrm{C13}/\mathrm{P11},
\]

while the period and recurrence consequences are

\[
 (\mathrm{P6,spike,primitivity})\to\mathrm{C14}/\mathrm{P12},
 \qquad
 (\mathrm{P8,P4})\to\mathrm{C15,C16}/\mathrm{P13}.
\]

C17 is an independent positioning obligation, and C18 is a mass audit after
all proof branches close.  No logical arrow originates in an experiment,
finite fixture, or literature search miss.

### Canonical page mass

The exact source-design allocation is 26.5 anonymous content pages.  The
formal candidate reviewers' 25.5- and 26.0-page estimates remain correctly
attributed historical estimates rather than the controlling source-design
sum.

BATCH07_PAPER28_CLAIMS_EVIDENCE_CORRECTION_FROZEN
