# Paper 24 — Final Proof-First Proposal

## Title

**Forced Period-Two Selector Exchange in Two-Mode Hamiltonian Product
Shears**

## Lifecycle status

Source-design author proposal only. The corrected candidate gate passed before
this package, but the ten source-design files still require a fresh
independent audit. This proposal is not a source lock, paper plan, manuscript,
build, or release authorization.

## Headline theorem

Let $K$ be a characteristic-zero field and let $m\ge2$, $s\ge1$ be integers.
Let $A,B,C,D\in K^\times$. Put

$$
V_m(q)=Aq_1^m q_2^2+Bq_1q_2^{2m},
\qquad
W_{m,s}(p)=Cp_1^{s(2m+1)+1}+Dp_2^{sm+1},
$$

and define

$$
S(q,p)=(q,p+\nabla V_m(q)),
\qquad
T(q,p)=(q+\nabla W_{m,s}(p),p),
\qquad
F_{m,s}=T\circ S.
$$

Then $F_{m,s}$ is a polynomial symplectomorphism. For the standard total-degree
seed $u_0=(1,1)^{\mathsf T}$, the first-phase selector wall is exactly
$r=u_1/u_2=2$, the ordinary degree orbit alternates strictly between the two
open chambers, and the selected matrices are

$$
A_-=
\begin{pmatrix}
0&2m\\
1&2m-1
\end{pmatrix},
\qquad
A_+=
\begin{pmatrix}
m-1&2\\
m&1
\end{pmatrix},
\qquad
B_m=\operatorname{diag}(2m+1,m).
$$

Writing

$$
P=(B_mA_+)(B_mA_-),
$$

the exact parity laws are

$$
u_{2j}=(s^2P)^j(1,1)^{\mathsf T},
\qquad
u_{2j+1}=sB_mA_-(s^2P)^j(1,1)^{\mathsf T}.
$$

Arbitrary nonzero coefficients survive because the selected top homogeneous
part is unique and nonzero in a polynomial domain. For every $n\ge1$, the
first position coordinate is strictly maximal among all four coordinate
degrees, so

$$
d_n:=\deg(F_{m,s}^n)=u_{n,1}.
$$

The monodromy eigenvalues are

$$
H=m^2(2m+1)^2,
\qquad
L=2m(m+1),
$$

hence

$$
\lambda_1(F_{m,s})=sm(2m+1),
$$

and the visible degree sequence satisfies

$$
d_{n+4}=s^2(H+L)d_{n+2}-s^4HL\,d_n.
$$

The exact wall-gap laws are

$$
u_{2j,1}-2u_{2j,2}=-(s^2L)^j,
\qquad
u_{2j+1,1}-2u_{2j+1,2}=2ms(s^2L)^j.
$$

## Public contribution boundary

The contribution is the concrete conjunction of:

1. one explicit two-mode family;
2. forced wall fixing at $r=2$ inside the ansatz;
3. strict period-two selector exchange of the actual polynomial degree orbit;
4. a true carry/no-cancellation/visibility proof;
5. one exact two-step monodromy and parity degree law.

The bounded structural lemma and the conditional period-$k$ monodromy lemma
are supporting technique, not the novelty headline.

## Proof architecture

1. Differentiate the potentials and verify exact polynomial symplecticity.
2. Write the competitive support rows and derive $A_-,A_+,B_m$.
3. Derive the corrected branch formulas $h_m,\ell_m$ and prove strict
   chamber exchange.
4. Prove first-step and later-step carry in both phases.
5. Prove arbitrary-nonzero-coefficient leading-form survival in a domain.
6. Prove $q_1$ visibility against $q_2,p_1,p_2$.
7. Multiply the monodromy and derive its spectrum.
8. Derive the recurrence, wall gaps, and parity closed forms.
9. State the bounded wall-fixing lemma in the crossed-binomial /
   two-pure-power ansatz.
10. State the conditional period-$k$ selector-to-monodromy lemma only with its
    full hypotheses and nonnovel status.

## Planned 22--30 content pages

| Section | Target pages |
|---|---:|
| introduction and bounded related work | 3 |
| exact family, symplecticity, and support rows | 4 |
| wall algebra and strict selector exchange | 4 |
| carry, leading forms, and visibility | 6 |
| monodromy, recurrence, wall gaps, and parity formulas | 6 |
| structural lemma, conditional period-$k$ lemma, and boundaries | 3 |
| **target** | **26** |

## Citation and novelty boundary

The citation ledger may use only the candidate-review records and their
recorded access levels until a later citation stage is separately authorized.
The safe novelty sentence is only that no direct collision with the complete
frozen package was located in the bounded candidate-gate search through
2026-08-25 UTC.

## Hard exclusions

- theorem on the wall $r=2$;
- anything beyond the crossed-binomial / diagonal-pure-power ansatz;
- maximal or necessary selector-fan claims;
- period $>2$, automaton, or arbitrary-period realization;
- positive-characteristic validity;
- inverse-degree, entropy-equality, integrability, genericity,
  periodic-point, or nonconjugacy claims;
- novelty of the abstract period-$k$ lemma itself;
- first Perron realization or absolute literature priority.

## Permission boundary

This proposal completes no lifecycle gate by itself. Only a fresh independent
reviewer may decide whether the exact ten-file source-design package passes.
Until then, no lock, plan, manuscript, bibliography, figure, code, build, PDF,
release, registry edit, submission, upload, transport, message, identity
disclosure, or other external effect is authorized.
