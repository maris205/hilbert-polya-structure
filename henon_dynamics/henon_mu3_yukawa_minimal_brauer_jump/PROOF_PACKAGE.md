# HCS-C57 proof package

Status: **PAPER_COMPILED; PAPER_HOSTILE_PASS; proof implication complete;
project-local exact premises PREFREEZE_CODE_RESULTS_PASS; NOT_RELEASED.**

## 1. Claim

For the frozen HCS-C55/HCS-C56 cubic surface \(Y/\mathbf Q\), prove:

1. nonzero 2-primary algebraic Brauer quotient after finite base change
   \(L/\mathbf Q\) forces

   \[
   36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q];
   \]

2. degree 36 is attained precisely by the conjugate double-six fields
   \(F_D=K^{U_1}\);
3. over \(F_D\), the quotient is \(\mathbf Z/2\);
4. its generator is the canonical quaternion
   \((\delta_D,Q_D/u_0^4)\).

## 2. Status and premise discipline

The argument below is a complete written implication from H0--H7. The exact
premises are bound by the project-local producer and independent checker at
`PREFREEZE_CODE_RESULTS_PASS`. The official paper compiled from this proof and
passed an independent hostile audit. Neither the machine handoff nor the paper
milestone is a project release, and no temporary computation is cited as
release authority.

The proof deliberately separates:

- H0, the frozen C56 theorem;
- the complete classical 2-primary classification, which applies to every
  subgroup arising after finite base change;
- H1--H7, exact instance premises for fields, cohomology, and the
  representative.

The finite natural-stabilizer audit in H2 cannot replace the complete
classification theorem.

## 3. Premises

- **H0 (frozen C56 object).** \(Y/\mathbf Q\) is smooth and geometrically
  irreducible; its common normal line field is \(K\), with
  \(\operatorname{Gal}(K/\mathbf Q)=W(E_6)\).
- **H1 (exact incidence).** The characteristic-zero gcd identities and
  modular all-and-only replay give 135 meeting pairs, 72 sixers, and 36
  double-sixes.
- **H2 (exact subgroup and cohomology).** For a double-six \(D\),

  \[
  U_1=\operatorname{Stab}(D)\cong S_6\times C_2
  \]

  has order 1440, index 36, line orbits \([12,15]\), trivial core, and
  self-normalizer. Its oriented subgroup \(U_1^+\cong S_6\) has index two.
  Exact integral cochains give

  \[
  H^1(W(E_6),\Lambda)=0,\qquad
  H^1(U_1,\Lambda)=\mathbf Z/2.
  \]
- **H3 (exact fields).** Degree-36 resolvers for \(\theta_D\) and
  \(\delta_D\) are exact, irreducible, separable, and bound
  Galois-equivariantly to all 36 double-sixes.
- **H4 (exact orientation).**

  \[
  \delta_D=\beta_D^2,\quad
  \operatorname{Stab}(\theta_D)=
  \operatorname{Stab}(\delta_D)=U_1,\quad
  \operatorname{Stab}(\beta_D)=U_1^+.
  \]
- **H5 (exact carrier).** Over \(\mathbf Q(\theta_D)\), the exact factor
  \(A_{12}\) cuts out precisely the twelve lines of \(D\), and
  \(g=A_{12}B_{15}\) with independent division and multiply-back checks.
- **H6 (canonical quartic).** The locked \(60\times31\) restriction matrix
  has rank 30; its locked pivot minor is nonzero; the normalized kernel vector
  defines \(Q_D\); and all 60 restrictions vanish for all 36 conjugates.
- **H7 (divisor and class matching).** The line and degree checks give

  \[
  \operatorname{div}(Q_D)=\mathcal E+\mathcal G,
  \]

  no carrier line lies in \(u_0=0\), and the norm-divisor identity holds.
  In the standard blow-up basis, the exact \(U_1\)-action includes

  \[
  \iota(h)=5h-2e_\Sigma,\qquad
  \iota(e_\Sigma)=12h-5e_\Sigma
  \]

  for the central involution exchanging the sixers. The written calculation
  below, not a machine label, proves that the resulting cyclic-algebra
  cocycle is nonzero.

## 4. External theorem used for the universal quantifier

Let \(k\) be a number field and let \(H\subseteq W(E_6)\) be the image of
\(G_k\) on the Picard lattice of a smooth cubic surface. The complete
Swinnerton-Dyer--Elsenhans--Jahnel classification gives the following
2-primary alternatives:

\[
\begin{array}{c|c}
H^1(H,\Lambda)[2]&\text{forced containment}\\ \hline
\mathbf Z/2&H\subseteq gU_1g^{-1}\\
(\mathbf Z/2)^2&H\subseteq gU_3g^{-1}.
\end{array}
\tag{P.1}
\]

Here is the base-field bridge used in that sentence. Swinnerton-Dyer's
cohomological theorem is stated over an algebraic number field. The
Elsenhans--Jahnel containment and restriction assertions are propositions
about subgroups of \(W(E_6)\), their action on the integral Picard lattice,
and invariant line configurations. Thus, for any number field \(k\), they
apply verbatim to the finite image \(H=\operatorname{im}(G_k\to W(E_6))\);
no property special to \(\mathbf Q\) enters the subgroup statement. For the
explicit class over \(F_D\), we reproduce the quadratic norm-divisor and
cyclic-algebra construction directly over that number field, and then use
the same number-field Hochschild--Serre identification. We therefore do not
silently promote a literal \(\mathbf Q\)-model calculation into a
number-field theorem.

Here \(U_1\) has index 36 and \(U_3\) has index 720 in \(W(E_6)\). This
complete theorem, not H2 alone, is what makes the proof valid for every
finite \(L/\mathbf Q\).

## 5. Proof of divisibility

Let \(L/\mathbf Q\) be finite and assume

\[
\left(
\operatorname{Br}(Y_L)/\operatorname{im}\operatorname{Br}(L)
\right)[2]\ne0.
\tag{P.2}
\]

Write \(G_L=\operatorname{Gal}(\overline{\mathbf Q}/L)\), and let

\[
H_L=\operatorname{im}\!\left(
G_L\longrightarrow W(E_6)
\right).
\tag{P.3}
\]

Set

\[
N_L=\ker\!\left(G_L\longrightarrow H_L\right).
\tag{P.3a}
\]

The action of \(G_L\) on the discrete Picard lattice \(\Lambda\) factors
through \(H_L\), so \(N_L\) acts trivially. Every continuous homomorphism
from the profinite group \(N_L\) to the discrete group \(\Lambda\) has finite
image, and the torsion-free lattice \(\Lambda\) has no nonzero finite
subgroup. Hence

\[
H^1(N_L,\Lambda)
=\operatorname{Hom}_{\mathrm{cont}}(N_L,\Lambda)=0.
\tag{P.3b}
\]

The inflation--restriction sequence for
\(1\to N_L\to G_L\to H_L\to1\) therefore gives

\[
H^1(G_L,\Lambda)\cong H^1(H_L,\Lambda).
\tag{P.3c}
\]

Because \(Y_{\overline{\mathbf Q}}\) is rational,
\(\operatorname{Br}(Y_{\overline{\mathbf Q}})=0\). Moreover \(L\) is a
number field, so \(H^3(L,\mathbf G_m)=0\). The low-degree
Hochschild--Serre sequence and (P.3c) consequently identify

\[
\operatorname{Br}(Y_L)/\operatorname{im}\operatorname{Br}(L)
\cong H^1(G_L,\Lambda)
\cong H^1(H_L,\Lambda).
\tag{P.3d}
\]

Thus (P.2) gives nonzero \(H^1(H_L,\Lambda)[2]\), and (P.1) applies.

If the 2-primary quotient is \(\mathbf Z/2\), then
\(H_L\subseteq gU_1g^{-1}\), and the index formula gives

\[
[W(E_6):H_L]
=36[U_1:g^{-1}H_Lg].
\tag{P.4}
\]

If it is \((\mathbf Z/2)^2\), then
\(H_L\subseteq gU_3g^{-1}\), and

\[
[W(E_6):H_L]
=720[U_3:g^{-1}H_Lg].
\tag{P.5}
\]

Thus in both cases

\[
36\mid[W(E_6):H_L].
\tag{P.6}
\]

Since \(K/\mathbf Q\) is Galois, restriction to \(L\) has fixed field

\[
K^{H_L}=K\cap L.
\tag{P.7}
\]

The Galois correspondence and tower law now give

\[
[W(E_6):H_L]=[K\cap L:\mathbf Q],
\tag{P.8}
\]

\[
[K\cap L:\mathbf Q]\mid[L:\mathbf Q].
\tag{P.9}
\]

Combining (P.6)--(P.9) proves

\[
36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q].
\tag{P.10}
\]

This is stronger than the numerical inequality \([L:\mathbf Q]\ge36\).

## 6. Equality fields

Assume in addition that \([L:\mathbf Q]=36\). Then every divisibility in
(P.10) is equality:

\[
L=K\cap L,\qquad [W(E_6):H_L]=36.
\tag{P.11}
\]

Equation (P.5) excludes the \(U_3\) branch. Equation (P.4) then forces

\[
H_L=gU_1g^{-1}.
\tag{P.12}
\]

Therefore

\[
L=K^{gU_1g^{-1}}.
\tag{P.13}
\]

By H2, \(U_1\) is self-normalizing. Hence its 36 conjugates are in bijection
with the 36 double-sixes; the associated embedded fixed fields are distinct.
They are conjugate under \(W(E_6)\), so they form one Q-isomorphism type.

Conversely, for every double-six \(D\),

\[
F_D=K^{U_1},\qquad
[F_D:\mathbf Q]=[W(E_6):U_1]=36.
\tag{P.14}
\]

It remains to prove that the quotient is indeed nonzero over \(F_D\).

## 7. Brauer quotient over the attaining field

Let

\[
\Lambda=\operatorname{Pic}(Y_{\overline{\mathbf Q}}).
\]

The \(G_{F_D}\)-action on \(\Lambda\) factors through \(U_1\). If \(N\) is
the kernel, then \(N\) acts trivially. In the inflation--restriction
sequence, the term

\[
H^1(N,\Lambda)=\operatorname{Hom}_{\mathrm{cont}}(N,\Lambda)
\tag{P.15}
\]

vanishes: a continuous image of the profinite group \(N\) is finite, whereas
the free abelian lattice \(\Lambda\) has no nonzero finite subgroup. Thus

\[
H^1(F_D,\Lambda)\cong H^1(U_1,\Lambda).
\tag{P.16}
\]

For a smooth geometrically rational surface,

\[
\operatorname{Br}(Y_{\overline{\mathbf Q}})=0.
\tag{P.17}
\]

The low-degree Hochschild--Serre sequence gives

\[
\operatorname{Br}(Y_{F_D})/
\operatorname{im}\operatorname{Br}(F_D)
\longrightarrow H^1(F_D,\Lambda)
\longrightarrow H^3(F_D,\mathbf G_m).
\tag{P.18}
\]

For the number field \(F_D\), the last group vanishes in this standard
application. Therefore (P.18), (P.16), and H2 yield

\[
\operatorname{Br}(Y_{F_D})/
\operatorname{im}\operatorname{Br}(F_D)
\cong H^1(U_1,\Lambda)
\cong\mathbf Z/2.
\tag{P.19}
\]

The same argument over \(\mathbf Q\), using H2 for the full \(W(E_6)\)
action, gives

\[
\operatorname{Br}(Y)/\operatorname{im}\operatorname{Br}(\mathbf Q)=0.
\tag{P.20}
\]

This proves the jump and completes the converse required in Section 6.

## 8. Resolver and field identification

By H1, the 36 exact configurations form the transitive
\(W(E_6)\)-set \(W(E_6)/U_1\). By H3--H4,

\[
\operatorname{Stab}(\theta_D)=U_1,\qquad
\operatorname{Stab}(\delta_D)=U_1.
\tag{P.21}
\]

The orbit-stabilizer theorem gives 36 conjugates for each element, so its
minimal polynomial has degree 36. Since the exact orbit polynomials in H3
also have degree 36, they are those minimal polynomials and are irreducible:

\[
\mathbf Q(\theta_D)=K^{U_1}
=\mathbf Q(\delta_D)=F_D.
\tag{P.22}
\]

The core of \(U_1\) is trivial by H2, so the kernel of the 36-point coset
action is trivial. Hence the splitting field of either resolver is \(K\).

Finally H4 gives

\[
\operatorname{Stab}(\beta_D)=U_1^+,\qquad
\delta_D=\beta_D^2.
\tag{P.23}
\]

Since \(U_1^+\) has index two in \(U_1\),

\[
F_D'=K^{U_1^+}
=F_D(\beta_D)
=F_D(\sqrt{\delta_D}).
\tag{P.24}
\]

Nothing in (P.21)--(P.24) requires an expanded
\(\delta=P(\theta)\) calculation.

## 9. Construction and uniqueness of the quartic

By H5, the degree-12 carrier \(A_{12}\) cuts out exactly the lines in
\(D\). The coefficient of \(u_0^3\) in \(F\) is
\(c=75081586157\). Multiplication by the four coordinate linear forms,
followed by projection to the coefficients of

\[
u_0^4,\quad u_0^3u_1,\quad u_0^3u_2,\quad u_0^3u_3,
\]

has a triangular \(4\times4\) matrix with determinant

\[
c^4=
31778526453059635681033276764499400992765201\ne0.
\tag{P.25}
\]

Consequently each quartic class modulo \(F\) times a linear form has a unique
representative with those four coefficients zero. Restricting that fixed
31-dimensional gauge to the twelve lines in \(D\) gives H6's matrix

\[
M_D:F_D^{31}\longrightarrow F_D^{60}.
\tag{P.26}
\]

We first establish the upper rank bound geometrically. The class of the
double-six divisor is

\[
\mathcal E+\mathcal G\sim4H_Y.
\tag{P.27}
\]

This geometric equivalence must first be descended. Put \(k=F_D\) and
choose a \(k\)-rational hyperplane section
\(H_0=\operatorname{div}_Y(\ell)\). Both
\(\mathcal E+\mathcal G\) and \(4H_0\) are \(k\)-rational divisors. Over
\(\bar k\), choose \(r\in\bar k(Y)^*\) satisfying

\[
\operatorname{div}(r)=\mathcal E+\mathcal G-4H_0.
\]

For \(\sigma\in\operatorname{Gal}(\bar k/k)\), the rational function
\(c_\sigma=\sigma(r)/r\) has zero divisor and is therefore in
\(\bar k^*\). These scalars form a multiplicative 1-cocycle. By Hilbert
theorem 90 there is \(a\in\bar k^*\) with
\(c_\sigma=\sigma(a)/a\). It follows that \(r_0=r/a\) belongs to
\(k(Y)^*\). Hence

\[
s_D=r_0\ell^4\in H^0(Y_k,\mathcal O_Y(4))
\]

is a \(k\)-rational section with divisor
\(\mathcal E+\mathcal G\). This Hilbert--90 argument is the descent of
the line-bundle/section equality; no section over \(F_D\) is inferred from
geometric linear equivalence alone.

The hypersurface restriction sequence

\[
0\to\mathcal O_{\mathbf P^3}(1)
\xrightarrow{\cdot F}\mathcal O_{\mathbf P^3}(4)
\to\mathcal O_Y(4)\to0
\tag{P.28}
\]

is surjective on global sections over \(k\) because
\(H^1(\mathbf P^3_k,\mathcal O(1))=0\). Thus \(s_D\) lifts to an ambient
quartic over \(F_D\) with the prescribed double-six divisor, modulo \(F\)
times a linear form.
Therefore

\[
\operatorname{rank}M_D\le30.
\tag{P.29}
\]

H6 supplies a fixed \(30\times30\) minor that is nonzero in \(F_D\). A
nonzero reduction at one denominator-good prime proves the characteristic-zero
determinant is nonzero, so

\[
\operatorname{rank}M_D\ge30.
\tag{P.30}
\]

Together,

\[
\operatorname{rank}M_D=30,\qquad \dim\ker M_D=1.
\tag{P.31}
\]

The nonzero pivot minor also proves that the coordinate \(q_0\) is nonzero on
the kernel line. Normalize it to one. Cramer's rule for the locked minor
defines the remaining coefficients and hence the unique normalized
determinant-defined quartic \(Q_D\).

The construction is exact without an expanded coefficient table: basis,
gauge, row order, pivot rows, normalization, and determinants uniquely define
every coefficient.

## 10. Divisor equality

H6 verifies all 60 restrictions, so \(Q_D\) vanishes on the twelve distinct
lines in \(\mathcal E+\mathcal G\). It is not \(F\) times a linear form
because its gauge class is the nonzero vector spanning \(\ker M_D\).

The quartic divisor has degree

\[
(4H_Y)\cdot H_Y=4\deg(Y)=12.
\tag{P.32}
\]

The twelve distinct line components contribute total degree 12. Any residual
effective curve would have positive hyperplane degree, and any repeated
carrier line would increase the counted degree. Neither is possible.
Therefore

\[
\operatorname{div}_{Y_{F_D}}(Q_D)
=\mathcal E+\mathcal G.
\tag{P.33}
\]

This is the point where restriction vanishing becomes a global divisor
statement; it cannot be asserted before the degree comparison.

## 11. Quaternion and nontriviality

Let

\[
\ell=u_0,\qquad
\mathcal L_0=\operatorname{div}_Y(\ell),\qquad
f_D=Q_D/\ell^4.
\tag{P.34}
\]

H7 verifies that no carrier line lies in the hyperplane \(\ell=0\). Over
\(F_D'\), define

\[
\mathcal D=\mathcal E-2\mathcal L_0.
\tag{P.35}
\]

The nontrivial automorphism of \(F_D'/F_D\) exchanges
\(\mathcal E\) and \(\mathcal G\). Using (P.33),

\[
\begin{aligned}
\operatorname{Norm}_{F_D'/F_D}(\mathcal D)
&=\mathcal E+\mathcal G-4\mathcal L_0\\
&=\operatorname{div}(Q_D/u_0^4)\\
&=\operatorname{div}(f_D).
\end{aligned}
\tag{P.36}
\]

The cyclic-algebra divisor criterion shows that

\[
\mathcal A_D=(F_D'/F_D,f_D)
=(\delta_D,Q_D/u_0^4)
\tag{P.37}
\]

extends to an unramified class on \(Y_{F_D}\).

Unramifiedness alone would not prove nontriviality. We now identify the
cocycle explicitly. In the standard blow-up basis, let

\[
e_\Sigma=e_1+\cdots+e_6,\qquad
H_Y=3h-e_\Sigma,\qquad
d_0=e_\Sigma-2h.
\tag{P.38}
\]

The first sixer has class \(e_\Sigma\), and its opposite has class
\(12h-5e_\Sigma\). Therefore

\[
[\mathcal D]=e_\Sigma-2H_Y=3(e_\Sigma-2h)=3d_0.
\tag{P.39}
\]

Write \(U_1=S_6\times\langle\iota\rangle\), where \(\iota\) exchanges the
two sixers. H7 gives

\[
\iota(h)=5h-2e_\Sigma,\qquad
\iota(e_\Sigma)=12h-5e_\Sigma,\qquad
\iota(d_0)=-d_0.
\tag{P.40}
\]

Moreover \(\Lambda^{S_6}=\mathbf Zh\oplus\mathbf Ze_\Sigma\), and direct
calculation yields

\[
\ker(1+\iota\mid\Lambda^{S_6})=\mathbf Z d_0,\qquad
(\iota-1)\Lambda^{S_6}=2\mathbf Z d_0.
\tag{P.41}
\]

With the convention in (P.36), the Hochschild--Serre cocycle of (P.37)
vanishes on \(S_6\) and takes \(\iota\) to
\([\mathcal D]=3d_0\). If it were a \(U_1\)-coboundary, the vanishing on
\(S_6\) would force a cobounding class to lie in \(\Lambda^{S_6}\); its
value at \(\iota\) would then lie in \(2\mathbf Z d_0\) by (P.41). This is
impossible because \(3d_0\notin2\mathbf Z d_0\). Thus the cocycle is nonzero.
By H2 it is the unique nonzero element of \(H^1(U_1,\Lambda)\), and under
(P.19), \(\mathcal A_D\) generates the Brauer quotient. This proves the
explicit representative theorem.
\(\square\)

## 12. Scope locks

- The proof of (P.10) uses both \(U_1\) and \(U_3\) branches of the complete
  2-primary theorem.
- The machine natural-stabilizer table verifies H2 only; it is not the
  classification theorem.
- The field equality is a stabilizer argument, not
  \(\delta=P(\theta)\).
- The quartic is determinant-defined; a huge expanded table is optional.
- No local evaluation of \(\mathcal A_D\) is supplied.
- Therefore no rational-point, Hasse-principle, weak-approximation, or
  Brauer--Manin claim follows.
- Stable-rationality and local Picard--Artin statements are outside C57.
