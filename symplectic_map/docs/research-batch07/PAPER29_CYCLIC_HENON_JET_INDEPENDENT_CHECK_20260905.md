# Paper29 cyclic Hénon jet theorem: independent mathematical check

Date: 2026-09-05.

## 1. Input, ownership and scope

This is an independent mathematical audit of the actual complete author
package, not a reuse of the earlier two-factor or first-order checks.
The second reviewer's messages and report were not read.

The complete V1 input was read and its hash verified:

- PAPER29_CYCLIC_HENON_JET_PROOF_V1_20260905.md, 683 lines;
  SHA256 d6da24f8aa6ada330612a10cf8974925450a3250c598b58cb405f12cef79c683.

Two missing-addition display errors were reported to the author. The
author preserved V1 and supplied a successor. The complete V1-to-V2
diff was checked:

- PAPER29_CYCLIC_HENON_JET_PROOF_V2_20260905.md, 688 lines;
  SHA256 f488e8a7cd5a2c71a4975b2f004b21c87d20f4afb29c967318781963fb2955f0.

The diff contains only the version explanation and the three restored
plus signs. In particular it changes no theorem, orbit selection,
coefficient domain, derivative convention, remainder claim or proof
argument. The mathematical decision below binds the V2 theorem and
proof, with the V1 display defects recorded in Section 12.

Only this independently owned file is written. Neither author version
nor any other project file is changed.

## 2. Claim and status

**Status: PROVABLE AS STATED for the complete V2 theorem.**

No additional hypothesis, weakening of the stated parameter region, or
restriction on the prescribed positive macro periods is required.
No unresolved mathematical counterexample was found.

This status is not a candidate PASS, novelty assessment, publication
recommendation, Route evaluation, or acceptance of a long-paper page
budget. No novelty score is assigned here.

The checked object is
$$
F_{\epsilon,u}=H_{c_k}\circ\cdots\circ H_{c_1},\qquad
H_c(x,y)=(x^2+c-y,x),\qquad
c_j=\epsilon^{-2}(u_j-1),\quad k\ge2.
$$
For a selected exact cycle of macro period $n$, the checked row is
$$
\kappa=\frac{1}{n\rho}\,d_u\rho,\qquad
\rho=\operatorname{tr}DF^n.
$$
All derivatives hold $\epsilon$ fixed. The claims checked jointly are:

1. A single small-parameter construction, uniform over every prescribed
   period vector, gives the explicit disjoint simple cycle tuple.
2. At $u=0$, its determinant has exact order $k-1$ when $6\nmid k$,
   and exact order $k+1$ when $6\mid k$, with the stated prefactor.
3. No tuple of actual periodic branches can have a smaller finite
   determinant order in this normalization at $u=0$.
4. The entire singular-value profile is attained, not just the
   determinant order.
5. These determinant and singular-value estimates hold on one common
   fixed $u$-neighborhood in the nonresonant case, and on the stated
   shrinking region $u=\epsilon v$ in the resonant case.
6. At least one labeled-cycle incidence component for each period
   vector has a dominant, generically étale trace map.

## 3. Assumptions, notation and dependencies

The ground field is $\mathbb C$. The integer $k$ is fixed; constants may
depend on $k$, but not on any period, symbol word or occupation vector.
The coefficient directions are the $k$ ordered factors, not solely the
one-dimensional direction along their common power locus.

Exactness and disjointness concern $F$, not an elementary Hénon factor.
The cycle labels are retained in the algebraic statement. Simplicity
means $\det(DF^n-I)\ne0$.

Write $s_j(u)=\sqrt{1-u_j}$ for the branch near $1$,
$\sigma_t\in\{1,-1\}$ for an elementary sign, and
$L_0(u)=\sum_j\log(2s_j(u))$.

Write $S$ for the cyclic shift on phase space. Its two occurrences in
$S+S^{-1}$ must both be kept when $k=2$. Let
$$
L_1=I-S-S^{-1},\qquad
D_a=\operatorname{diag}(a_1,\ldots,a_k),\qquad
P(a)=\sum_i\prod_{j\ne i}a_j.
$$

The proof dependency chain checked here is:

1. Uniform orbit contraction and exhaustion.
2. Uniform Riccati contraction and an actual normalized spectral
   differential, including the stable-eigenvalue correction.
3. Universal first-order jet and two Fourier obstructions.
4. Second-order correlation calculation and occupation-scaled recovery.
5. Exact prefactor, rescaled-column remainder, and full singular profile.
6. Parameter-dependent column elimination and common coefficient region.
7. Local simple incidence and labeled-cycle descent.

## 4. Actual orbit construction, exhaustion and normalized jets

For $N=kn$ the cyclic equations are
$$
z_t^2-(1-u_{j(t)})=\epsilon(z_{t-1}+z_{t+1}).
$$
The two roots of $1-u_j$ remain separated on a fixed small coefficient
polydisc. On the product of the corresponding root discs, the signed
square-root map has sup-norm Lipschitz constant at most $C|\epsilon|$.
Each component sees only two neighbors, so the estimate is independent
of $N$. Coincident neighbors for $N=2$ are counted twice.

The map preserves the chosen product discs and is a contraction for
one common radius. It therefore gives one holomorphic scaled branch
for every word. Cauchy estimates are taken on a larger coefficient
polydisc before restricting to a smaller one. Coordinate-wise
sup-norm bounds then provide period-independent coefficient derivatives
and Taylor remainders.

The author's analytic exhaustion argument is sufficient. Every complex
solution, with $M=\max_t|z_t|$ and $R=\max_j|1-u_j|$, satisfies
$$
M^2\le R+2|\epsilon|M.
$$
Thus $M$ is uniformly bounded, and
$$
|(z_t-s_j)(z_t+s_j)|\le2|\epsilon|M
$$
forces each coordinate into exactly one of the two root discs.
Contraction uniqueness excludes every additional affine periodic root.
This is a proof of exhaustion, not an extrapolation from local branches.

An independent algebraic check gives the same result: under a graded
monomial order, the cyclic quadrics have pairwise-coprime leading
monomials $z_t^2$, so they form a Gröbner basis. The quotient has the
$2^N$ square-free monomials as a basis. Hence the $2^N$ constructed
simple roots exhaust its length. This check is not an additional
dependency of the author's shorter analytic argument.

The cyclic Riccati equation
$$
w_t=2z_t-\frac{\epsilon^2}{w_{t-1}}
$$
has a uniform contraction near $2\sigma_t\sqrt{1-u_{j(t)}}$.
The exact invariant-line identity gives
$$
\lambda=\epsilon^{-N}\prod_t w_t,\qquad
\rho=\lambda+\lambda^{-1}.
$$
Choosing the common radius so that $|\lambda|>2^N$ proves both
simplicity and nonvanishing of the trace for every constructed branch.

With $\theta=\lambda^{-2}$,
$$
\kappa=\frac{1-\theta}{1+\theta}\,
       \frac1n\sum_t d_u\log w_t.
$$
The factor $1/n$ is essential for the uniform derivative bounds.
The corrected V2 scalar potential is a sum of three terms:
$$
\mathcal L_\sigma
=\sum_j\log(2s_j)
 +\frac1n\sum_t\operatorname{Log}
       \frac{w_t}{2\sigma_t s_{j(t)}}
 +\frac1n\operatorname{Log}(1+\theta).
$$
Its differential is exactly $\kappa$. The final summand starts at
order $\epsilon^{2kn}$; for $k\ge2$ this is uniformly at least order
four. Thus it does not alter either jet used in the theorem.

## 5. Universal necessary orders

Direct expansion of the orbit equation gives
$$
z_t=\alpha_t+\epsilon t_t+\epsilon^2r_t+O_{C^1}(\epsilon^3),
$$
$$
t_t=\frac{\alpha_{t-1}+\alpha_{t+1}}{2\alpha_t},\qquad
r_t=\frac{t_{t-1}+t_{t+1}-t_t^2}{2\alpha_t},
\qquad \alpha_t=\sigma_t s_{j(t)}.
$$
After summing the first-order logarithmic term, the phase means $m_j$
give
$$
\mathcal L_\sigma=L_0+
\epsilon\sum_jm_j\frac{s_j}{2}
 (s_{j-1}^{-2}+s_{j+1}^{-2})+O_{C^1}(\epsilon^2).
$$
At $u=0$ this yields
$$
\kappa=-\frac12\mathbf1^T+
\epsilon m^T\frac{S+S^{-1}-I}{2}+O(\epsilon^2).
$$
This independently confirms the sign and the doubled-neighbor
convention for $k=2$.

The nonconstant Fourier columns have no zeroth-order term. Exactly
when $6\mid k$, the frequencies $k/6$ and $5k/6$ also have no
first-order term. Therefore every possible row tuple has determinant
order at least
$$
k-1\quad(6\nmid k),\qquad
(k-3)+2+2=k+1\quad(6\mid k).
$$
The row and remainder bounds used here are uniform over arbitrary
words. Section 4's exhaustion is what extends this statement from
constructed symbolic examples to every actual periodic branch in the
region. A determinant may vanish identically.

This necessary-order statement is at $u=0$ in the specified coefficient
normalization. It is not asserted at arbitrary coefficient points.

## 6. Independent check of the second-order calculation

The second-order logarithmic coefficient from the orbit and Riccati
equations is
$$
\frac{t_{t-1}+t_{t+1}}{2\alpha_t^2}
-\frac{(\alpha_{t-1}+\alpha_{t+1})^2}{4\alpha_t^4}
-\frac1{4\alpha_t\alpha_{t-1}}.
$$
In particular the last term is present. Removing it would change the
second-order resonant value.

Reindexing this expression gives exactly the V2 functions
$C_{\rm tot},D_j,E_j$ in equations (25)--(26).
For an explicit verification, the first fraction contributes
$$
\frac{\alpha_{t-2}}{4\alpha_t^2\alpha_{t-1}}
+\frac1{4\alpha_t\alpha_{t-1}}
+\frac1{4\alpha_t\alpha_{t+1}}
+\frac{\alpha_{t+2}}{4\alpha_t^2\alpha_{t+1}}.
$$
The Riccati term cancels the second summand. The three remaining
terms give the three adjacent-correlation coefficients in $E_j$.
The square in the second fraction gives the constant and
distance-two coefficients. This recovers (24) without assuming
temporal independence of the signs.

Differentiating these rational functions at $u=0$ gives
$$
dC_{\rm tot}=-\tfrac12\mathbf1^T,
$$
$$
dD_j=\tfrac14e_{j-1}^T-e_j^T+\tfrac14e_{j+1}^T,
$$
$$
dE_j=\tfrac14e_{j-1}^T+\tfrac18e_j^T+
      \tfrac18e_{j+1}^T+\tfrac14e_{j+2}^T.
$$
These are the actual gradients in the author package. Indices that
coincide for small $k$ add; they are not discarded.

For a minus sign confined to phase $i$, the correlation changes
produce the second-order row increment
$$
-\tfrac32e_i^T+\tfrac54(e_{i-1}^T+e_{i+1}^T)
-(e_{i-2}^T+e_{i+2}^T).
$$
Thus
$$
L_2=-\tfrac32I+\tfrac54(S+S^{-1})-(S^2+S^{-2})
$$
is correct. The all-plus second-order row is
$-\mathbf1^T/4$, giving the stated $\gamma(\epsilon)$.
The symbol of $L_2$ at either first-order zero mode is
$$
-\tfrac32+\tfrac52\cos(\pi/3)-2\cos(2\pi/3)=\tfrac34.
$$
The two missing directions therefore really recover at order two.

This calculation is needed only for resonant $k\ge6$. The author's
additive-index version also works for $k=3,4$, while $k=2$ is
deliberately covered only by the already sufficient first-order
argument. There is no unhandled small-$k$ case.

## 7. Arbitrary periods and occupation scaling

For $n_i\ge2$, the unique all-plus macro block prevents any smaller
macro repetition. For $n_i=1$ exactness is immediate. The $i$th word
has at least one negative sign in phase $i$; every other selected word
is positive in that phase. Hence no two selected words represent the
same $F$-cycle.

The means are $m^{(i)}=\mathbf1-2a_i e_i$, with $a_i\in[1/2,1]$.
For $k\ge3$, every adjacent or distance-two sign pair in the
second-order formula involves two distinct phases. At most one of
those phases can be negative in a selected word. Consequently the
change in its averaged product is exactly the corresponding
single-negative-block change times $a_i$. This remains valid across
macro boundaries and for $n_i=2$.

It follows that the complete selected matrix has the claimed form
$$
K=\gamma(\epsilon)J+
D_a(\epsilon L_1+\epsilon^2L_2)+O_k(\epsilon^3)
$$
with $J=\mathbf1\mathbf1^T$ and
$\gamma(\epsilon)=-1/2+\epsilon/2-\epsilon^2/4$,
whenever the second-order formula is used. The independent argument
does not replace the word by a constant word or ignore its marker.

## 8. Exact prefactor and the determinant remainder

The circulant product is
$$
\det L_1=-4\sin^2(k\pi/6).
$$
In the nonresonant case the nonconstant-mode product is therefore
$2(1-\cos(k\pi/3))$.

In the resonant case the two zero modes and the constant mode must
all be removed. Differentiating
$2[T_k(x/2)-1]$ twice at $x=1$ gives the coefficient
$-k^2/3$ of $(x-1)^2$. The constant-mode factor there is $-1$.
Hence the remaining nonconstant-mode product is $k^2/3$, as in (35).

Use $B=\epsilon L_1$ for the nonresonant leading term and
$B=\epsilon L_1+\epsilon^2L_2$ for the resonant leading term.
For $w=D_a^{-1}\mathbf1$, the correct determinant lemma is
$$
\det(B+\gamma w\mathbf1^T)
=\det B+\gamma\det B\,\mathbf1^TB^{-1}w.
$$
Because $B$ is circulant, its constant-mode inverse cancels exactly
the constant eigenvalue in the second term. The first term has one
higher order. Multiplication by $\det D_a$ thus leaves the occupation
factor $P(a)$, not a factor that presumes all $a_i$ are equal.

The result is
$$
\det K=-[1-\cos(k\pi/3)]P(a)\epsilon^{k-1}
       +O_k(\epsilon^k)
$$
when $6\nmid k$, and
$$
\det K=-\frac{3k^2}{32}P(a)\epsilon^{k+1}
       +O_k(\epsilon^{k+2})
$$
when $6\mid k$. The check $k=6$, $a_i=1$ gives the stated
$-81\epsilon^7/4$.

An entrywise determinant error estimate alone would not justify the
resonant remainder. The author instead divides Fourier columns by
$1$, $\epsilon$ or $\epsilon^2$ according to their actual order.
In the resonant columns the cubic row remainder becomes
$O_k(\epsilon)$; in other columns it is no larger.
Thus the rescaled determinant differs from its limiting nonzero
value by $O_k(\epsilon)$ uniformly over all periods. This establishes
the claimed remainder, including its quantifier order.

## 9. Full singular-value profile

At $u=0$, let $Q_0$ be a unitary Fourier matrix and let $\Delta$ have
entries $1$, $\epsilon$, or $\epsilon^2$ according to the asserted
column orders; the analytic scales here are not their absolute values.
The rescaled
matrix
$$
M=KQ_0\Delta^{-1}
$$
extends to $\epsilon=0$. Its limiting columns are the constant
column $-\sqrt{k}\,\mathbf1/2$, the columns $D_a L_1q_\nu$ for
nonresonant modes, and $D_a L_2q_\nu$ for the two resonant modes.

The determinant computed above is nonzero for every
$a\in[1/2,1]^k$, and $P(a)\ge k/2^{k-1}$. Uniform entry bounds and
the cofactor formula bound both $M$ and $M^{-1}$ on this compact
occupation cube and on one sufficiently small parameter domain.
Hence
$$
K=M\Delta Q_0^*
$$
has each singular value comparable, above and below, to the matching
ordered diagonal scale of $\Delta$. This proves all of (7), not
just a smallest-singular-value consequence of the determinant.

## 10. Parameter-column elimination and the shrinking region

The row
$$
v_0(u)=\left(-\frac1{2(1-u_j)}\right)_j
$$
is common to every cycle at order zero. The author's columns
$$
\widetilde q_\nu(u)=q_\nu-
q_0\frac{v_0(u)q_\nu}{v_0(u)q_0}
$$
annihilate this row exactly. The denominator stays nonzero near
$u=0$. The transformation is a triangular column shear relative
to the Fourier basis, so its determinant is unchanged and its
matrix and inverse are uniformly bounded.

It need not be the Jacobian of a parameter-coordinate map; it is
used only as a bounded holomorphic column operation. No derivative
of this column matrix is improperly inserted into $K$.

For the nonresonant estimate, these columns remove the whole
zeroth-order contribution before division by $\epsilon$. Uniform
Taylor bounds and the already invertible limiting matrix give
one coefficient polydisc for every occupation vector and period.

For a resonant column, set
$$
G_\nu(u)=(d_uh_j(u))_j\widetilde q_\nu(u).
$$
It is holomorphic and $G_\nu(0)=0$. Therefore
$$
\frac{G_\nu(\epsilon v)}{\epsilon}
=\int_0^1 DG_\nu(t\epsilon v)[v]\,dt
$$
extends holomorphically to $\epsilon=0$ and is $O_k(\|v\|)$.
After the exact zeroth-order elimination, this is precisely the
potential first-order contribution to a column divided by
$\epsilon^2$. The genuine second-order term has the required factor
already; the cubic remainder becomes $O_k(\epsilon)$.

The rescaled matrix at $(\epsilon,v)=(0,0)$ is the invertible matrix
of Section 9. On a common small $v$-polydisc, the new limiting term
is a uniformly small perturbation; then one common $\epsilon_0$
controls the remaining error. This validates the stated region
$u=\epsilon v$, including complex $\epsilon$ and complex $v$.

Multiplication back by the bounded nonunitary matrix $Q(u)^{-1}$
still preserves each singular-value comparison up to fixed
constants. Thus both (6) and the full (7) hold on (4).

There is no hidden fixed-$u$-radius resonant assertion: the proof
uses the shrinking region in an essential place. Differentiation
remains in $u$, not in $v$.

## 11. Algebraic consequence and exact boundaries

On the exact, disjoint, simple point-marked incidence, the
marked-point Jacobian consists of the invertible blocks
$DF^{n_i}-I$. The Jacobian criterion makes projection to the
coefficient base étale locally, so the constructed point lies on
one smooth local component of dimension $k$.

The product of the finite cyclic shift groups acts freely there:
a stabilizer would contradict one of the exact periods. The
characteristic-zero quotient gives labeled cycles and is étale on
this locus. Traces descend because the return derivatives at shifted
points are conjugate.

At fixed nonzero $\epsilon$,
$$
D_u\rho=\epsilon^{-2}D_c\rho,\qquad
D_u(\rho_1,\ldots,\rho_k)
=\operatorname{diag}(n_i\rho_i)K.
$$
Hence the ordinary coefficient trace differential is invertible.
On the irreducible component through this point, its image has
dimension $k$, proving dominance; the resulting function-field
extension is finite and separable, proving generic finiteness and
generic étaleness. No whole-incidence irreducibility assumption
is used.

The following limits are necessary and already respected by V2:

- Actual phase-space coordinates $\epsilon^{-1}z_t$ are holomorphic
  on the punctured domain; the scaled coordinates and normalized
  differential extend across $\epsilon=0$. The actual orbit need
  not extend as a finite point at $\epsilon=0$.
- The universal optimal order is at the power locus and depends on
  the fixed normalization. It is not invariant under singular
  coefficient changes.
- Constants may depend on $k$; uniformity as $k\to\infty$ is not claimed.
- The theorem certifies this explicit tuple; it does not make every
  disjoint tuple a coordinate system.
- The algebraic statement concerns at least one component, not all
  components, global injectivity or reconstruction.
- No assertion is made about a fixed resonant $u$-neighborhood,
  unnormalized trace-Jacobian orders, or $v$-differential orders.

## 12. Specific defects found and their resolution

The two V1 display defects were genuine literal formula errors:

1. In (18), omission of the two plus signs turned a sum into a
   product. At $\epsilon=0$ the latter has zero differential,
   contradicting the required nonzero row
   $-\mathbf1^T/2$. V2 restores the two plus signs.
2. In the determinant-lemma sentence after (36), omission of the
   plus sign gave an incorrect product. For example, with
   $B=I$, $w=\mathbf1$ and $\gamma=1$, the correct left side is
   $k+1$, whereas the printed V1 right side gives $k$.
   V2 restores the exact determinant identity used in Section 8.

These corrections repair the displays without modifying the
underlying argument or theorem. The inspected V2 diff resolves
both. No additional mathematical defect remains open in this
independent check.

## 13. Genuine additional proof volume

This package has more mathematical content than the stopped
single-factor full-rank construction. The new content is not merely
another anti-integrable continuation:

- It identifies a universal loss of two first-order directions at
  precisely the multiples of six and proves the necessary order
  for every actual periodic selection.
- It computes the actual second-order spectral differential,
  including the Riccati term, and proves that one arbitrary-period
  selection recovers both missing directions.
- It obtains the exact occupation-dependent prefactor, sharp full
  singular profile, and a justified common shrinking parameter region.

These form one linked theorem, not three independent paper-sized
results. Uniform root continuation, Cauchy estimates, Fourier
diagonalization, compact-matrix perturbation and incidence descent
are established proof tools and are not counted again as new methods.
The two-factor case is a special case, not a separate additional
chapter required to prove the general theorem.

As a proof-volume estimate, the genuinely additional central
arguments in Sections 5--10 above support approximately 6--9
substantive English pages when presented coherently. A standalone
main text including the necessary analytic setup, precise theorem,
algebraic consequence and modest positioning is naturally around
16--20 substantive pages on the current mathematical input.
This is an editorial estimate, not a compiled page count.
The source V2 has 3,576 whitespace-delimited words, including
mathematical tokens, and 37
numbered displays; neither its 688 Markdown lines nor the length
of this audit should be converted directly into manuscript pages.

This audit does not certify 22--30 substantive pages. Conversely,
the estimate is not a proof that a carefully justified longer
presentation is impossible. The separate novelty, scientific value
and honest page-fit gates must judge the actual eventual content;
they must not inflate this theorem by repeating the inherited
continuation or the special cases.

## 14. Final disposition

The V2 theorem survives unchanged. Its general-$k$ prefactors,
all-period quantifiers, universal necessary orders, selected-word
attainment, full singular-value profile, parameter-column
elimination, resonant coefficient region, orbit exhaustion and
restricted algebraic consequence have all been independently checked
as one package.

Mathematical status: **PROVABLE AS STATED**.

Candidate, novelty and long-paper acceptance status: **not assigned
by this report**.
