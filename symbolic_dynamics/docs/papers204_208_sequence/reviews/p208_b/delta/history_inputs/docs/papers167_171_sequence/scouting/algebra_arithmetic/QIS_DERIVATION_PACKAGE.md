# Quartic inverse-span dynamics: derivation package

Provisional status: `GREEN_OWNER_THIN / HOLD_FOR_EXTERNAL_NOVELTY`.

## 1. Literal system

Let `p` be a prime, let `K = F_{p^4}`, and let `X_p` be the complete lattice
of `F_p`-linear subspaces of `K`.  For `A in X_p`, put

\[
 \mathcal J(A)=\operatorname{span}_{\mathbb F_p}
 \{a^{-1}:a\in A\setminus\{0\}\},\qquad \mathcal J(0)=0.
\]

This is a deterministic self-map on a finite, non-coordinate carrier.  The
degree four is structural: it has one proper intermediate field
`F_{p^2}`, planes are projective lines, and hyperplanes are one rank below the
full field.

## 2. Three counting constants

Write

\[
 L=L_p={4\brack1}_p=p^3+p^2+p+1,
\]

\[
 P=P_p={4\brack2}_p=(p^2+1)(p^2+p+1),
 \qquad Q=Q_p=p^2+1.
\]

Here `L` is both the number of lines and the number of hyperplanes, `P` is
the number of planes, and `Q` is the number of scalar copies of the quadratic
subfield:

\[
 \#\{\xi\mathbb F_{p^2}:\xi\in K^\times\}
   ={p^4-1\over p^2-1}=p^2+1.
\]

Consequently the state count is

\[
 S=|X_p|=2+2L+P.
\]

## 3. Rank engine

Inversion is a bijection on `K^x`.  If `dim(A)=d`, then
`A^{-1}` contains `p^d-1` distinct nonzero points.  An `r`-dimensional
subspace contains only `p^r-1` nonzero points, so

\[
 \dim\mathcal J(A)\geq \dim A. \tag{3.1}
\]

If equality holds, cardinality forces

\[
 \mathcal J(A)=A^{-1}\cup\{0\},
 \qquad \mathcal J^2(A)=A. \tag{3.2}
\]

The published classification of linear/affine subspaces whose patched inverse
image is again a subspace implies that, apart from zero and lines, equality in
(3.1) occurs exactly for scalar subfields `xi F_{p^k}`, `k|4`.  Thus the
only proper higher-dimensional equality cases are the `Q` planes
`xi F_{p^2}`.  No hyperplane is an equality case.

## 4. Why the binary plane takes one extra step

Normalize a plane as

\[
 A=\xi\langle1,\alpha\rangle_{\mathbb F_p}.
\]

The degree `r=[F_p(alpha):F_p]` is two or four.  Projective representatives
of the inverse line are

\[
 1,\quad (\alpha-t)^{-1}\quad(t\in\mathbb F_p).
\]

Any at most `r` of these representatives are linearly independent when they
include `1`: multiply a proposed relation by
`prod_i(alpha-t_i)` and use that no nonzero polynomial of degree below `r`
vanishes at `alpha`.  Hence

\[
 \dim\mathcal J(A)=\min\{p+1,r\}. \tag{4.1}
\]

If `r=2`, then `A=xi F_{p^2}` and its image is another such plane.  If
`r=4`, equation (4.1) gives

\[
 \dim\mathcal J(A)=
 \begin{cases}
 3,&p=2,\\
 4,&p>2.
 \end{cases} \tag{4.2}
\]

This is the early anomaly: a non-subfield projective line has only three
projective points over `F_2`, so its inverse spans a hyperplane; over every odd
prime it already supplies four independent inverse points and spans `K`.

## 5. Complete rank transition table

| Input `A` | Count | `J(A)` | Recurrent? |
|---|---:|---|---|
| `0` | 1 | `0` | yes, fixed |
| line `xi F_p` | `L` | `xi^{-1} F_p` | yes, period 1 or 2 |
| plane `xi F_{p^2}` | `Q` | `xi^{-1} F_{p^2}` | yes, period 1 or 2 |
| other plane, `p=2` | `P-Q=30` | a hyperplane | no, tail 2 |
| other plane, `p>2` | `P-Q` | `K` | no, tail 1 |
| hyperplane | `L` | `K` | no, tail 1 |
| `K` | 1 | `K` | yes, fixed |

Thus the recurrent-state count is

\[
 R=2+L+Q. \tag{5.1}
\]

The sharp maximum tail is

\[
 H_p=\begin{cases}2,&p=2,\\1,&p>2.\end{cases} \tag{5.2}
\]

A witness always exists because `P-Q>0`.

## 6. Depth enumerator and stabilization

Let `d(A)` be the distance of `A` to its eventual cycle and define
`D_p(u)=sum_A u^{d(A)}`.  The transition table gives

\[
 D_2(u)=R+Lu+(P-Q)u^2=22+15u+30u^2, \tag{6.1}
\]

and for every odd prime

\[
 D_p(u)=R+(S-R)u. \tag{6.2}
\]

The successive image sizes are

\[
 |\mathcal J^t(X_2)|=
 \begin{cases}S,&t=0,\\R+L,&t=1,\\R,&t\ge2,\end{cases} \tag{6.3}
\]

\[
 |\mathcal J^t(X_p)|=
 \begin{cases}S,&t=0,\\R,&t\ge1\end{cases}
 \quad(p>2). \tag{6.4}
\]

## 7. Periods and zeta function

On the line orbit set `K^x/F_p^x`, `J` is coset inversion.  On the recurrent
plane orbit set `K^x/F_{p^2}^x`, it is also coset inversion.  These cyclic
quotients have orders `L` and `Q`.  Therefore

\[
 F=\#\operatorname{Fix}(\mathcal J)
  =2+\gcd(2,L)+\gcd(2,Q)
  =\begin{cases}4,&p=2,\\6,&p>2.\end{cases} \tag{7.1}
\]

There are `(R-F)/2` two-cycles and no other periods.  Equivalently,

\[
 \#\operatorname{Fix}(\mathcal J^n)=
 \begin{cases}F,&n\text{ odd},\\R,&n\text{ even},\end{cases} \tag{7.2}
\]

and the Artin--Mazur zeta function is

\[
 \zeta_{\mathcal J}(z)
  =(1-z)^{-F}(1-z^2)^{-(R-F)/2}. \tag{7.3}
\]

## 8. Complete all-time fibre atlas

For `t>=1`, write

\[
 N_t(B)=\#\{A\in X_p:\mathcal J^t(A)=B\}.
\]

The answer for every target is:

- `N_t(0)=1`;
- if `B` is recurrent and `B != K`, then `N_t(B)=1`;
- if `B` is a non-subfield plane, then `N_t(B)=0`;
- for a hyperplane `H`,

  \[
  N_t(H)=
  \begin{cases}
  2,&p=2,\ t=1,\\
  0,&\text{otherwise};
  \end{cases} \tag{8.1}
  \]

- for the full field,

  \[
  N_t(K)=
  \begin{cases}
  1+L,&p=2,\ t=1,\\
  1+L+P-Q,&p=2,\ t\ge2,\\
  1+L+P-Q,&p>2,\ t\ge1.
  \end{cases} \tag{8.2}
  \]

The nontrivial value `N_1(H)=2` at `p=2` follows from twisted scalar symmetry

\[
 \mathcal J(\lambda A)=\lambda^{-1}\mathcal J(A), \tag{8.3}
\]

the transitive Singer action on hyperplanes, and the count
`(P-Q)/L=30/15=2`.

## 9. Full functional-graph shape

All recurrent fixed points and two-cycles other than `K` have no transient
vertices attached.  Every transient vertex belongs to the component rooted at
the fixed point `K`.

- For odd `p`, that component is a star: all `L` hyperplanes and all `P-Q`
  non-subfield planes point directly to `K`.
- For `p=2`, it is a uniform depth-two tree: 15 hyperplanes point to `K`, and
  each hyperplane has exactly two non-subfield plane children.

The number of weak components is `(R+F)/2`.

## 10. Checked instances

| `p` | `S` | one-step image | `R` | `F` | cycles | depth histogram | full fibre `(t=1,t=2)` |
|---:|---:|---:|---:|---:|---|---|---|
| 2 | 67 | 37 | 22 | 4 | 4 fixed, 9 two-cycles | `22,15,30` | `16,46` |
| 3 | 212 | 52 | 52 | 6 | 6 fixed, 23 two-cycles | `52,160` | `161,161` |
| 5 | 1120 | 184 | 184 | 6 | 6 fixed, 89 two-cycles | `184,936` | `937,937` |

The independent verifier reconstructs the finite fields, enumerates every
RREF subspace, computes every edge, verifies the classification counts and all
one-/two-step fibres, tests twisted scalar symmetry, and pins edge digests.

## 11. Honest claim budget

Potentially residual claims are the degree-four **iterated span dynamics**:
the binary/odd sharp-height dichotomy, exact functional graph, zeta synthesis,
and all-time target fibre atlas.  The inverse-image equality classification and
normal-rational-curve geometry are prior work and must appear as inputs, not
contributions.  If an external search finds the same self-map or graph
synthesis, this candidate should be killed immediately rather than narrowed to
a parameter variant.
