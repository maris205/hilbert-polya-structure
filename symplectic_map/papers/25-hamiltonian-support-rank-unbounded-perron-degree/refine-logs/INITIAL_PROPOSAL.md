# Initial Proposal

## Identity and design boundary

- Candidate ID: support_rank_sharp_unbounded_perron_v1.
- Working title: **Sharp Support-Rank Bounds and Unbounded Perron Degree in Hamiltonian Product Shears**.
- Decision date and literature cutoff inherited from candidate review: 2026-08-26 UTC.
- Object: an explicit positive integer-coefficient Hamiltonian product shear on affine $2d$-space over a characteristic-zero field.
- Evidence mode: exact symbolic proof design only.

This proposal preserves the complete candidate conjunction. It does not treat
the support-kernel observation, a fixed-dimensional example, or a familiar
spectral theorem as a paper by itself.

## Initial problem statement

The local lineage contains two contrasting finite-dimensional outcomes.
Paper 22 obtains a common unit sector and cubic spectral collapse in an
arbitrary-mode endpoint-spike family. Paper 23 removes that unit sector in one
four-mode construction and obtains an irreducible quartic family. The open
structural question is whether selected support data impose a general bound
on the nonunit spectral complexity and, if so, whether Hamiltonian
gradient-compatible maps can attain that bound in unbounded rank while still
admitting an exact ordinary-degree calculation.

The initial thesis has two parts.

1. If selected half-step matrices have presentations
   $A=-I_n+\mathsf P\mathsf Q$ and
   $B=-I_n+\mathsf R\mathsf S$, then the row rank
   $r=\operatorname{rank}\binom{\mathsf Q}{\mathsf S}$ forces at least
   $n-r$ unit eigenvalues algebraically and bounds the remaining
   characteristic degree by $r$.
2. For every $d\ge2$, a positive Hamiltonian product shear realizes the
   bound at $r=d$, has exact visible degree sequence
   $e_1^{\mathsf T}C^n\mathbf1$, and has Perron degree and minimal rational
   scalar recurrence order exactly $d$.

## Proposed construction

After choosing integers $a_1<\cdots<a_d$ and $b\ge2$, set

$$
V(q)=\prod_{j=1}^d q_j^2+\sum_{i=1}^d q_i^{a_i+1},
\qquad
W(p)=\prod_{j=1}^d p_j^b.
$$

For

$$
S_V(q,p)=(q,p+\nabla V(q)),\qquad
T_W(q,p)=(q+\nabla W(p),p),
$$

take $F=T_W\circ S_V$. The intended selected matrices are

$$
D=\operatorname{diag}(a_1,\ldots,a_d),\qquad
B=bJ-I_d,\qquad
C=BD=b\mathbf1a^{\mathsf T}-D.
$$

The arithmetic choice is intended to force

$$
\chi_C(t)\equiv t^d-c\pmod p
$$

for a generator $c$ of $\mathbb F_p^\times$, while a strict cone is intended
to make the matrix recursion equal to the literal polynomial-degree
recursion.

## Initial proof obligations

The proposal is viable only if all of the following are proved rather than
suggested by a tropical calculation.

1. Derive the support-rank factorization with an explicit reduced
   determinant and state only a lower bound on unit multiplicity.
2. Choose parameters in the noncircular order
   $d\to p,c\to a_1,\ldots,a_d\to b,R$.
3. Separate the broad coordinate-ratio cone used for selection from the
   finer weighted chamber used for fixed-coordinate visibility.
4. Prove every selector inequality, cone wall, temporal carry, and
   cross-phase comparison strictly.
5. Prove top-form survival in the positive integer semiring over every
   characteristic-zero base field.
6. Derive the characteristic polynomial coefficient by coefficient.
7. Verify the exact finite-field binomial criterion, including $d=2$ and
   the extra clause when $4\mid d$.
8. Upgrade a $d$-dimensional matrix recurrence to minimal scalar order $d$
   by reachability and observability, not by Cayley--Hamilton alone.
9. Show that the family attains the support-row bound for every
   nontrivial rank $d\ge2$ covered by the theorem.

## Initial risk register

| Risk | Failure mode | Required repair |
|---|---|---|
| Unit-root overstatement | The reduced determinant may also vanish at $t=1$. | State algebraic multiplicity at least $n-r$, never exactly $n-r$. |
| Cone conflation | A coordinate-ratio band alone does not encode the weighted order needed for $q_1$ visibility. | Use a broad ratio cone and a finer visibility chamber explicitly. |
| Carry omission | A selected gradient monomial may lose to an old coordinate. | Label both half-steps and prove all old-versus-new inequalities. |
| Cancellation gap | Matrix degrees need not imply nonzero polynomial top forms. | Work in the positive integer coefficient semiring and use characteristic zero. |
| Arithmetic exception | A binomial test may omit the $4\mid d$ condition. | State the full criterion and audit $d=2$ and $4\mid d$. |
| Quantifier reversal | Choosing lifts after $b$ would make the large-$b$ argument circular. | Freeze the lifts before choosing $b$ in its residue class. |
| Scalar-order overclaim | A matrix of size $d$ only gives order at most $d$. | Prove cyclic reachability and observability and full Hankel rank. |
| Portfolio collision | The rank lemma or $d=4,5$ alone repeats local work. | Headline the all-$d$ sharp conjunction and subtract Papers 22--24. |

## Initial anti-claims

The proposal does not cover arbitrary signs, supports, coefficients, or
exponent profiles. It does not realize every weak Perron number and does not
claim minimal dimension or sparsity. It says nothing about inverse growth,
higher dynamical degrees, compactification, entropy equality, integrability,
periodic selectors, automata, genericity, classification, nonconjugacy, or
positive characteristic. It does not assert exact unit multiplicity or an
exact rank profile for arbitrary selected matrices. An isolated $d=5$ case
has no independent novelty role, and no absolute priority wording is
permitted.

## Initial disposition

The candidate is sufficiently coherent to enter proof-only refinement. No
manuscript, computation, build, source lock, or release action follows from
this initial proposal.
