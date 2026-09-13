# Optimal trace-differential jet orders near quadratic Hénon powers

Date: 2026-09-05. Author-side bounded Paper29 candidate proof.
This is a new multi-factor question, not an enlargement of the stopped
single-factor trace-coordinate note. No candidate PASS, formal project,
scientific/publication lock or manuscript is created.

## 1. Claim and exact normalization

Fix an integer $k\ge2$. Put
$$
H_c(x,y)=(x^2+c-y,x),\qquad
F_{\epsilon,u}=H_{c_k}\circ\cdots\circ H_{c_1},
\qquad c_j=\epsilon^{-2}(u_j-1),
$$
where $\epsilon\ne0$ and $u=(u_1,\ldots,u_k)\in\mathbb C^k$.
Every factor, and hence $F_{\epsilon,u}$, has Jacobian determinant one.
At $u=0$ this family lies on the power locus
$F_{\epsilon,0}=H_{-\epsilon^{-2}}^k$.
The coefficient directions are the $k$ separately variable factors,
not the one-dimensional direction along the power locus.

For a simple exact $F$-cycle of period $n$, let
$$
\rho=\operatorname{tr}DF^n,\qquad
\kappa=\frac1{n\rho}\,d_u\rho.
\tag{1}
$$
The periods here and throughout are periods of the composite map $F$.
One such period contains $k$ elementary Hénon steps.
All derivatives in this document are with respect to $u$, holding
$\epsilon$ fixed. Equation (1) is a logarithmic differential; it does
not require a global branch of $\log\rho$.

Define
$$
r_k=\begin{cases}k-1,&6\nmid k,\\k+1,&6\mid k,\end{cases}
\qquad
b_k=\begin{cases}
1-\cos(k\pi/3),&6\nmid k,\\
3k^2/32,&6\mid k.
\end{cases}
\tag{2}
$$
Thus $b_k>0$ in either case.

### Theorem

For every prescribed vector of positive macro periods
$\boldsymbol n=(n_1,\ldots,n_k)$, choose the following $k$ sign words.
The $i$th word has $n_i$ blocks of length $k$.

- If $n_i=1$, its sole block has a minus sign only in phase $i$.
- If $n_i\ge2$, exactly one block is all plus, and the other $n_i-1$
  blocks have a minus sign only in phase $i$.

The position of the all-plus block is immaterial up to macro cyclic
shift. Set
$$
a_i=\begin{cases}1,&n_i=1,\\1-1/n_i,&n_i\ge2,\end{cases}
\qquad
P(a)=\sum_{i=1}^k\prod_{j\ne i}a_j
     =\left(\prod_i a_i\right)\left(\sum_i a_i^{-1}\right).
\tag{3}
$$
In particular $1/2\le a_i\le1$ and $P(a)\ge k/2^{k-1}$.

There are positive constants $\epsilon_0,\eta,c,C$, depending only on
$k$, such that these words define pairwise-disjoint simple exact
$F_{\epsilon,u}$-cycles of periods $n_i$, with nonzero traces, throughout
the region
$$
0<|\epsilon|<\epsilon_0,\qquad
\begin{cases}
\|u\|_\infty<\eta,&6\nmid k,\\
u=\epsilon v,\quad \|v\|_\infty<\eta,&6\mid k.
\end{cases}
\tag{4}
$$
All cycle branches are holomorphic on the parent small-parameter domain
described in the proof. Let $K$ be the square matrix with rows (1) for
the chosen cycles. At the power locus $u=0$,
$$
\boxed{\det K(\epsilon,0)
=-b_kP(a)\epsilon^{r_k}+O_k(\epsilon^{r_k+1}).}
\tag{5}
$$
The error bound is uniform over all prescribed period vectors. On (4),
$$
|K_{ij}|\le C,\qquad
|\det K|\ge c|\epsilon|^{r_k}.
\tag{6}
$$
More precisely, if singular values are ordered decreasingly, their
orders on (4), with upper and lower comparison constants depending
only on $k$, are
$$
\begin{array}{c|c}
6\nmid k&1,\ \underbrace{|\epsilon|,\ldots,|\epsilon|}_{k-1}\\
6\mid k&1,\ \underbrace{|\epsilon|,\ldots,|\epsilon|}_{k-3},
             \ |\epsilon|^2,\ |\epsilon|^2.
\end{array}
\tag{7}
$$

The orders in (5) are optimal at $u=0$ in the following precise sense:
for **any** $k$ choices of periodic cycle branches, of any positive
periods, their matrix of normalized trace differentials satisfies
$$\det K_{\rm any}(\epsilon,0)=O_k(\epsilon^{r_k}).\tag{8}$$
Zero determinants are allowed in (8). The same normalized row and
remainder bounds apply to arbitrary words, so the upper bound can be
uniform in their periods. The explicit tuple above attains the smallest
possible finite order of vanishing. This is a statement about the
equal-scale power locus and this coefficient normalization, not an
intrinsic invariant under singular parameter changes.

For each prescribed period vector, the trace map on at least one
irreducible component of the simple exact disjoint cycle-marked
$k$-factor coefficient incidence is dominant and generically étale.
No all-component, global injectivity or reconstruction assertion is made.

### Derivative and neighborhood guards

The resonant condition $u=\epsilon v$ in (4) specifies a shrinking
region of evaluation points; $K$ is still differentiated in $u$.
If one uses $v$ as the differentiation coordinate, then
$K_v=\epsilon K_u$, and its determinant has $k$ additional powers of
$\epsilon$. For the original coefficients $c_j$,
$$
D_u\rho=\epsilon^{-2}D_c\rho.
\tag{9}
$$
Neither (5) nor (7) describes the unnormalized original trace Jacobian.
The orbit lengths and the traces themselves have also been divided out
in (1). No $\epsilon$-independent $u$-neighborhood is claimed for the
resonant estimate.

## 2. Status, assumptions and dependency map

**Author status: PROVABLE AS STATED. Independent general-theorem audit:
requested.** Separate bounded independent calculations already support
the two-factor first-order case, the general first-order obstruction,
and the six-factor second-order recovery. They do not replace a check
of this complete statement, its remainder control or its neighborhood.

Work is over $\mathbb C$ and all periods are positive integers.
Simple means $\det(DF^n-I)\ne0$. The cycle labels are retained.
The word “disjoint” always refers to orbits of $F$, not of an elementary
factor that coincides with other factors when $u=0$.

The proof chain is:

1. Uniform orbit and Riccati contractions produce all periodic branches
   and period-independent holomorphic normalized trace differentials.
2. First- and second-order jets are expressed by phase means and
   nearest/next-nearest sign correlations.
3. The universal first-order matrix has precisely two missing Fourier
   directions when $6\mid k$, proving the necessary jet order for
   every possible periodic selection.
4. Single-negative-phase words with a unique marker realize all
   prescribed macro periods and an occupation-scaled circulant
   second-order matrix.
5. Fourier column rescaling computes the exact determinant coefficient,
   controls the singular values, and proves uniform perturbation on
   the appropriate coefficient region.
6. A standard simple-incidence argument gives the stated algebraic
   consequence, without any claim about all components.

Uniform anti-integrable continuation, Fourier diagonalization and
incidence descent are established methods, not separate innovations.
The prospective core is the **unavoidable and attained** order
$k-1$ versus $k+1$ for actual spectral coefficient differentials,
including the second-order recovery and arbitrary-period selection.

## 3. Uniform periodic branches and their exhaustion

Let $s_j(u)=\sqrt{1-u_j}$ be the holomorphic branch near $1$.
Fix a small closed coefficient polydisc in a slightly larger one, so
that $s_j$ stays bounded away from zero. For a macro period $n$, put
$N=kn$, and give index $t\in\mathbb Z/N\mathbb Z$ the phase
$j(t)=1+(t\bmod k)$. The actual scaled recurrence is
$$
z_t^2-s_{j(t)}^2
=\epsilon(z_{t-1}+z_{t+1}).
\tag{10}
$$
Indeed, with $x_t=\epsilon^{-1}z_t$ the elementary update is
$x_{t+1}=x_t^2+c_{j(t)}-x_{t-1}$. The initial phase-space point is
$(x_0,x_{-1})$, and after $k$ steps the map is $F$ in the specified order.

For a sign word $\sigma_t\in\{1,-1\}$, solve
$$
z_t=\sigma_t\sqrt{s_{j(t)}^2+
                 \epsilon(z_{t-1}+z_{t+1})}.
\tag{11}
$$
Each square root in (11) is the local branch near $s_{j(t)}$.
Choose fixed disjoint discs about $\pm s_j$, of a small radius $h$.
On their product, the right side preserves the product when
$|\epsilon|$ is small and has sup-norm Lipschitz constant at most
$C|\epsilon|<1/2$. Both facts follow from bounded square-root
derivatives and the bound on two neighbors; neither contains $N$.
Repeated neighbors, when $k=2,n=1$, are counted twice and obey the
same bound. Banach's contraction theorem gives a unique branch with
$$z_t=\sigma_t s_{j(t)}+O(\epsilon)\tag{12}$$
uniformly in signs, position and period.

Iteration of (11) gives holomorphic dependence on $(\epsilon,u)$,
including $\epsilon=0$. All estimates are first made on larger
parameter discs. Cauchy's formula, applied to each scalar coordinate
on smaller discs with fixed radii, gives the corresponding bounds for
coefficient derivatives and Taylor remainders. In particular the
constants remain independent of $N$.

There are no other periodic branches hidden outside these root discs.
For any complex solution of (10), put $M=\max_t|z_t|$ and
$R=\max_j|1-u_j|$. At an index attaining $M$,
$$M^2\le R+2|\epsilon|M,\qquad
M\le|\epsilon|+\sqrt{|\epsilon|^2+R}.\tag{13}$$
This is a uniform bound. Equation (10) then implies
$|(z_t-s_j)(z_t+s_j)|\le2|\epsilon|M$.
For sufficiently small $|\epsilon|$, a coordinate outside both discs
would make this product at least $h^2$, a contradiction. The discs
are disjoint, so each solution has one unique sign word, and
contraction uniqueness applies. Thus the construction exhausts all
complex points of $\operatorname{Fix}(F^n)$.

Macro shift means shifting the word by $k$ elementary positions.
A primitive macro word yields exact $F$-period $n$: a shorter actual
period would impose the same shorter period on its root-disc labels.
Two primitive macro words can yield the same $F$-cycle only if their
lengths agree and they differ by a macro cyclic shift. This formulation
does not make the false disjointness assertion for arbitrary
nonprimitive words of different lengths.

## 4. Exact spectral differential and uniform Taylor jets

The elementary derivative is
$$M_t=\begin{pmatrix}2\epsilon^{-1}z_t&-1\\1&0\end{pmatrix}.$$
Solve the cyclic Riccati equations
$$w_t=2z_t-\frac{\epsilon^2}{w_{t-1}}.\tag{14}$$
On fixed small discs about $2\sigma_t s_{j(t)}$, denominators have
a common positive lower bound. The map preserves these discs and
has sup-norm Lipschitz constant at most $C|\epsilon|^2<1/2$.
Consequently its unique solution is holomorphic and
$$w_t=2\sigma_t s_{j(t)}+O(\epsilon),\qquad |w_t|\ge\mu>0.\tag{15}$$
The same larger-domain/Cauchy argument supplies uniform coefficient
derivatives and higher Taylor remainders.

The line identity
$$
M_t\binom{1}{\epsilon/w_{t-1}}
=\epsilon^{-1}w_t\binom{1}{\epsilon/w_t}
$$
gives a return eigenvalue
$$\lambda=\epsilon^{-N}\prod_{t=0}^{N-1}w_t.$$
The other eigenvalue is $\lambda^{-1}$ because the determinant is one.
After decreasing the common radius, $|\lambda|>2^N$ and
$|\lambda^{-1}|<2^{-N}$. All constructed cycles are simple, and
$$\rho=\lambda+\lambda^{-1}\ne0.\tag{16}$$

For a nonzero holomorphic function, use $d\log h$ to mean $dh/h$.
Define
$$\theta=\lambda^{-2}
=\epsilon^{2N}\left(\prod_t w_t\right)^{-2}.$$
It extends holomorphically across $\epsilon=0$, and
$|\theta|\le(C|\epsilon|^2)^N$.
The exact differential is
$$
\kappa
=\frac{1-\theta}{1+\theta}\,
  \frac1n\sum_t d_u\log w_t.
\tag{17}
$$
This identity removes the apparent period factor in differentiating
the stable-eigenvalue correction.

For Taylor expansions there is a bounded holomorphic scalar
$\mathcal L_\sigma(u,\epsilon)$ with $d_u\mathcal L_\sigma=\kappa$:
$$
\mathcal L_\sigma
=\sum_{j=1}^k\log(2s_j)
 \frac1n\sum_t
  \operatorname{Log}\frac{w_t}{2\sigma_t s_{j(t)}}
 \frac1n\operatorname{Log}(1+\theta).
\tag{18}
$$
The logarithms in the sum use the branch near $1$; the first logarithms
use branches near $2$. Sign products and powers of $\epsilon$ drop out
of the $u$ differential. The summands have uniform bounds and there
are exactly $kn$ of them. Hence (18), its coefficient derivatives,
and its Taylor remainders are uniformly bounded with constants
depending on $k$, not on $n$ or the signs. Since $k\ge2$, the last
term is $O_{C^1}(\epsilon^4)$ uniformly, including $n=1$.

Writing $\alpha_t=\sigma_t s_{j(t)}$, the orbit expansion is
$$
z_t=\alpha_t+\epsilon t_t+\epsilon^2r_t+O_{C^1}(\epsilon^3),
\quad
t_t=\frac{\alpha_{t-1}+\alpha_{t+1}}{2\alpha_t},
\quad
r_t=\frac{t_{t-1}+t_{t+1}-t_t^2}{2\alpha_t}.
\tag{19}
$$
Substitution in (14) and then in the logarithm gives
$$
\log w_t=\log(2\alpha_t)
+\epsilon\frac{t_t}{\alpha_t}
+\epsilon^2\left(
 \frac{t_{t-1}+t_{t+1}}{2\alpha_t^2}
 -\frac{(\alpha_{t-1}+\alpha_{t+1})^2}{4\alpha_t^4}
 -\frac1{4\alpha_t\alpha_{t-1}}\right)
+O_{C^1}(\epsilon^3).
\tag{20}
$$
The last displayed rational term is the Riccati contribution. Omitting
it changes the resonant second-order answer. The constant logarithm
in (20) is used only through its differential, consistent with (18).

## 5. The universal first-order obstruction

Let $m_j$ be the mean of the signs in phase $j$ over the $n$ macro
blocks. Reindexing the first-order sum in (20) yields
$$
\mathcal L_\sigma
=L_0(u)+\epsilon\sum_jm_jh_j(u)
 +O_{C^1}(\epsilon^2),
$$
$$
L_0(u)=\sum_j\log(2s_j),\qquad
h_j(u)=\frac{s_j}{2}
       \left(s_{j-1}^{-2}+s_{j+1}^{-2}\right).
\tag{21}
$$
The phase indices in (21) are modulo $k$. When $k=2$, the same
neighbor appears in both terms and must not be deleted.

Let $S$ be the cyclic shift on $\mathbb C^k$, and define
$$
\mathcal C=\frac12(S+S^{-1}-I),\qquad
L_1=-2\mathcal C=I-S-S^{-1}.
\tag{22}
$$
At $u=0$, $d_uL_0=-\frac12\mathbf1^T$, and the row matrix of the
$d_uh_j$ is $\mathcal C$. Thus every normalized trace row has
$$
\kappa(\epsilon,0)
=-\frac12\mathbf1^T+\epsilon m^T\mathcal C
 +O(\epsilon^2).
\tag{23}
$$

In a unitary Fourier basis $q_\ell$,
$S$ has eigenvalues $e^{2\pi i\ell/k}$ and $\mathcal C$ has eigenvalues
$\cos(2\pi\ell/k)-1/2$.
The constant Fourier column has order zero. Every nonconstant column
of (23) has order at least one. Exactly when $6\mid k$, the two
nonconstant columns $\ell=k/6,5k/6$ have order at least two.
Expanding a determinant by its columns proves (8):
$$
0+(k-1)\cdot1=k-1
$$
in the nonresonant case, and
$$
0+(k-3)\cdot1+2\cdot2=k+1
$$
in the resonant case. These conclusions hold for all sign selections;
Section 3 shows that they therefore hold for every periodic branch
in this region, not just a conveniently chosen subset.

## 6. The second-order correlation formula

This section is needed only for $6\mid k$, so $k\ge6$. The formulas
also hold for $k\ge3$ with coincident phase indices interpreted by
addition. No use of them is required for $k=2$.

Let $e_j$ be the mean of the product of adjacent signs in phases
$j,j+1$, and let $f_j$ be the mean of the product of the two signs
adjacent to phase $j$. At the wraparound these are signs in the
appropriate neighboring macro block. Direct reindexing of (20) gives
$$
\mathcal L_\sigma=L_0+\epsilon\sum_jm_jh_j
+\epsilon^2\left(C_{\rm tot}+\sum_je_jE_j+\sum_jf_jD_j\right)
+O_{C^1}(\epsilon^3),
\tag{24}
$$
where
$$
C_{\rm tot}=-\sum_j\frac{s_{j-1}^2+s_{j+1}^2}{4s_j^4},
\qquad
D_j=-\frac{s_{j-1}s_{j+1}}{2s_j^4},
\tag{25}
$$
$$
E_j=\frac1{4s_js_{j+1}}
 +\frac{s_{j+1}}{4s_js_{j-1}^2}
 +\frac{s_j}{4s_{j+1}s_{j+2}^2}.
\tag{26}
$$
For verification, the two contributions involving $t_{t\pm1}$ in
(20) supply adjacent sign products; the square term supplies the
constant and distance-two products; and the Riccati term subtracts
one adjacent-product contribution. Their combined adjacent coefficient
is precisely (26).

At $u=0$, the gradients are
$$
d_uC_{\rm tot}=-\frac12\mathbf1^T,
\qquad
d_uD_j=\tfrac14e_{j-1}^T-e_j^T+\tfrac14e_{j+1}^T,
\tag{27}
$$
$$
d_uE_j=\tfrac14e_{j-1}^T+\tfrac18e_j^T
       +\tfrac18e_{j+1}^T+\tfrac14e_{j+2}^T.
\tag{28}
$$
Here $e_j^T$ in (27)--(28) denotes a coordinate row vector, not the
sign-correlation scalar $e_j$ in (24). The different uses are confined
to these displayed gradient identities.

For an additional check, if $v_{j-1}+v_{j+1}=v_j$ is one of the two
resonant directions, then $\sum_jv_j=0$ and (27)--(28) reduce (24)'s
second-order directional derivative to
$$
\frac18\sum_j(v_j+v_{j+1})e_j-\frac34\sum_jv_jf_j.
\tag{29}
$$
For a word with a minus sign only in phase $i$, relative to the
all-plus word the adjacent correlations at $i-1,i$ change by $-2$,
and the distance-two correlations centered at $i-1,i+1$ change by
$-2$. Inserting these changes in (29), and using the resonant
recurrence twice, gives exactly $3v_i/4$.

## 7. Arbitrary macro periods and the occupation-scaled matrix

The selected words in the theorem are primitive in macro time: when
$n_i\ge2$, a unique all-plus block rules out a nontrivial repetition.
The $i$th word contains minus signs in phase $i$ and nowhere else,
whereas every other selected word is positive in that phase.
Consequently no two selected primitive words differ by a macro shift,
and Section 3 proves exactness and disjointness of the actual cycles.

The phase means of the $i$th word are
$m_j=1-2a_i\mathbf1_{j=i}$. Thus (23) gives
$$
K=\left(-\tfrac12+\tfrac12\epsilon\right)J
 +\epsilon\,\operatorname{diag}(a)L_1+O(\epsilon^2).
\tag{30}
$$
Here $J=\mathbf1\mathbf1^T$, and the error is uniform in every period.

For $k\ge3$, every adjacent or distance-two pair contains different
phases. In our selected word, at most one of these phases can carry
a negative sign. Hence all relevant correlation changes from the
all-plus word are also exactly $a_i$ times the single-negative-block
changes. This argument uses the mean number of negative blocks, not
an assumption that the whole word is constant. It remains true at
the boundary between macro blocks.

Equations (27)--(28) therefore give
$$
K=\gamma(\epsilon)J+
 D_a\bigl(\epsilon L_1+\epsilon^2L_2\bigr)+O_k(\epsilon^3),
\quad D_a=\operatorname{diag}(a_i),
\tag{31}
$$
$$
\gamma(\epsilon)=-\frac12+\frac12\epsilon-\frac14\epsilon^2,
\qquad
L_2=-\frac32I+\frac54(S+S^{-1})-(S^2+S^{-2}).
\tag{32}
$$
For example, the single-negative-phase change in the second-order
gradient is $-3/2$ in its own phase, $5/4$ in each neighbor, and $-1$
in each next-neighbor. Coincident indices contribute additively.
The all-plus second-order row equals $-\frac14\mathbf1^T$.
This proves (31), including its uniform error, directly from (24).

The symbol of $L_2$ is
$$\mu(\theta)=-\tfrac32+\tfrac52\cos\theta-2\cos2\theta.$$
At $\theta=\pm\pi/3$ this equals $3/4$, so the two universally missing
first-order directions recover at second order. The number $3/4$
is a spectral coefficient-differential calculation, not the
eigenvalue of the orbit-equation Jacobian.

## 8. Exact determinant coefficient and sharp singular-value orders

In the nonresonant case, all nonconstant Fourier modes of $L_1$
have nonzero eigenvalues
$$\ell_\nu=1-2\cos(2\pi\nu/k).$$
The constant eigenvalue is $-1$.
The characteristic polynomial identity
$$
\prod_{\nu=0}^{k-1}(x-2\cos(2\pi\nu/k))
=2\bigl(T_k(x/2)-1\bigr)
\tag{33}
$$
follows by writing $x=z+z^{-1}$ and comparing the roots and the
monic leading coefficient; $T_k(\cos\theta)=\cos(k\theta)$.
At $x=1$, it gives
$$
\prod_{\nu=1}^{k-1}\ell_\nu=2(1-\cos(k\pi/3)).
\tag{34}
$$

For $6\mid k$, remove the two zero factors as well as the constant
factor. The second derivative of the right side of (33) at $x=1$
gives
$$
\prod_{\substack{1\le\nu<k\\
          \nu\ne k/6,\,5k/6}}\ell_\nu=k^2/3.
\tag{35}
$$
For detail, $T_k'(1/2)=0$ and $T_k''(1/2)=-4k^2/3$.
The coefficient of $(x-1)^2$ in (33) is therefore $-k^2/3$;
the omitted constant-mode factor equals $-1$, yielding (35).

Let $w=D_a^{-1}\mathbf1$ and write
$B(\epsilon)=\epsilon L_1+\epsilon^2L_2$ when resonant.
For a nonresonant first-order calculation one can use
$B(\epsilon)=\epsilon L_1$.
In either case the leading determinant of
$D_a[B+\gamma w\mathbf1^T]$ is
$$
\det D_a\;\gamma\left(\sum_i a_i^{-1}\right)
 \prod_{\nu\ne0} \operatorname{eig}_\nu B.
\tag{36}
$$
One way to verify (36) is the determinant lemma
$\det(B+\gamma w\mathbf1^T)=\det B
( \gamma\det B)\mathbf1^TB^{-1}w$ for nonzero small $\epsilon$.
Since $B$ is circulant, $\mathbf1^TB^{-1}$ is its constant
eigenvalue inverse times $\mathbf1^T$. The term $\det B$ itself
has one higher power of $\epsilon$ than the displayed leading term.
This computation does not require $D_a$ to be scalar.

Combining $\gamma(0)=-1/2$, (34), and (36) gives the first case of
(5). Combining (35), the two recovered eigenvalues $3/4$, and (36)
gives
$$
-\frac12\cdot\frac{k^2}{3}\cdot\left(\frac34\right)^2P(a)
=-\frac{3k^2}{32}P(a),
$$
the resonant case of (5).

Remainder order in this calculation requires more than a naive
entrywise determinant bound. In a unitary Fourier column basis,
the constant column of (31) is $O(1)$, each nonresonant nonconstant
column is $O(\epsilon)$, and the two resonant columns are
$O(\epsilon^2)$. Divide these columns by their indicated powers.
The resulting matrix has a uniform finite limit; the remainder
in the resonant columns is $O(\epsilon)$ after division, and in
the other columns is no worse. In the nonresonant case (30)
suffices. Thus the determinant remainder in (5) is indeed
$O_k(\epsilon^{r_k+1})$, uniformly in all periods.

This same rescaling proves (7) at $u=0$. The limiting rescaled
matrix is invertible for every $a\in[1/2,1]^k$, by (36) and
$P(a)>0$. Its entries are bounded, and its determinant has a
uniform positive lower bound on that compact cube. Its inverse
is therefore uniformly bounded by the cofactor formula.
The Fourier matrix is unitary. Multiplication by bounded invertible
matrices changes each singular value by at most their condition
bounds, so the singular values of $K$ are comparable to the
diagonal column scales in (7).

As a check, for $k=6$ and all $n_i=1$, $P(a)=6$ and
$$\det K=-81\epsilon^7/4+O(\epsilon^8).$$
The six points are six different $F$-fixed points even though
at $u=0$ they are the six phases of one elementary Hénon cycle.
This does not identify their separately continued trace functions
under arbitrary factor perturbations.

## 9. Uniform coefficient regions without a false resonance claim

Write $v_0(u)=d_uL_0(u)$; its entries are
$-1/[2(1-u_j)]$ and $v_0(0)=-\frac12\mathbf1^T$.
Let $q_0=\mathbf1/\sqrt k$ be the constant Fourier column.
For nonconstant Fourier columns define
$$
\widetilde q_\nu(u)
=q_\nu-q_0\frac{v_0(u)q_\nu}{v_0(u)q_0}.
\tag{37}
$$
The denominator is nonzero on a small common coefficient polydisc.
These columns, together with $q_0$, form a holomorphic invertible
matrix $Q(u)$. It has the same determinant as the Fourier matrix
and uniformly bounded matrix and inverse norms. Crucially,
$v_0(u)\widetilde q_\nu(u)=0$ exactly, not merely at $u=0$.

For $6\nmid k$, multiply every row matrix $K$ by $Q(u)$ and
divide its nonconstant columns by $\epsilon$. Formula (21)
shows that this rescaled matrix extends holomorphically across
$\epsilon=0$ and has period-independent bounds. For the selected
words, its value at $(\epsilon,u)=(0,0)$ is the uniformly invertible
matrix of Section 8. Its dependence on the periods at that boundary
is only through $a\in[1/2,1]^k$. Uniform derivative and remainder
bounds now give a single $\eta,\epsilon_0$ for which it and its
inverse remain bounded. This proves (6)--(7) on the first region
in (4).

For $6\mid k$, the same claim on a fixed $u$-polydisc has not been
proved and is not assumed. Substitute $u=\epsilon v$.
For a resonant column $q_\nu$, the first-order vector
$$
G_\nu(u)=(d_uh_j(u))_{j=1}^k\,\widetilde q_\nu(u)
$$
is holomorphic and vanishes at $u=0$, by (22).
Thus $G_\nu(\epsilon v)/\epsilon$ extends holomorphically and is
bounded by $C\|v\|$ on a common product domain. This follows, for
example, by integrating its derivative on the segment
$t\epsilon v$, $0\le t\le1$.

After multiplication by $Q(\epsilon v)$, divide the $k-3$
nonresonant nonconstant columns by $\epsilon$ and the two resonant
columns by $\epsilon^2$. The zeroth-order row contributes nothing
to these columns by (37). The first-order contribution in a
resonant column is divisible by $\epsilon^2$ by the preceding
paragraph, and the second-order contribution already has that
factor. Equations (18)--(24) give a uniformly bounded holomorphic
rescaled matrix on $(\epsilon,v)$, including $\epsilon=0$.
At $(0,0)$ it is precisely the uniformly invertible matrix
calculated in Section 8.

The additional limiting first-order contribution in the resonant
columns is bounded by $C\|v\|$, uniformly in all phase means.
All further errors tend to zero uniformly with $\epsilon$.
Choose $\eta$ and then $\epsilon_0$ small enough that the rescaled
matrix stays within a fixed inverse-norm perturbation radius
of its value at $(0,0)$. This is possible uniformly for all
$a\in[1/2,1]^k$ and every period vector. The determinant and
inverse remain bounded away from zero and infinity.
Multiplying back the columns proves (6)--(7) in the resonant
region of (4), with the derivative convention (9) unchanged.

This proves an actual common coefficient region for all period
vectors at each small $\epsilon$, not a countable intersection
of unrelated local-coordinate neighborhoods. The resonant region
is intentionally narrower in $u$ than the nonresonant region.

## 10. Algebraic consequence and limits of the result

For a fixed period vector, the point-marked incidence over the
coefficient space $\mathbb A^k_c$ is given by
$F_c^{n_i}(z_i)=z_i$. Restrict to the exact, pairwise-disjoint,
simple locus. At a constructed tuple the marked-point differential
has invertible blocks $DF_c^{n_i}-I$, so the incidence is étale over
the coefficient base locally. There is a unique smooth local
component of dimension $k$ through this tuple.

The product of cyclic shift groups acts freely on that open locus.
Its finite quotient in characteristic zero gives labeled cycles;
the quotient is étale there. Traces descend because cyclically
shifted return derivatives are conjugate. Equations (6) and (9),
together with $n_i\rho_i\ne0$, make the ordinary coefficient trace
differential invertible. The component through the tuple therefore
has dominant trace map, is generically finite over the target,
and is generically étale. This does not require irreducibility
of the whole marked incidence.

No new normal-form conjugacy classification is used. Finite
factor-rotation or diagonal symmetries may prevent global
injectivity, and reversible partner orbits may have equal traces.
The proof does not assert that every disjoint tuple works:
the explicit determinant calculation certifies this tuple despite
such possible redundancies elsewhere.

The determinant orders are not orders of the unnormalized trace
Jacobian, not orders under the $v$ coordinate substitution, and not
a statement for arbitrary coefficient points away from the equal
power locus. The estimates say nothing about individual multiplier
branches as global algebraic coordinates, a universal reconstruction
algorithm, entropy, arithmetic orbit determinants or Riemann zeros.

The full theorem has now been proved on the author side. Its exact
general-$k$ coefficient, period-uniform remainders, universal lower
order, selected-word attainability and resonant neighborhood require
independent review as one package. The primary-source novelty and
independent long-paper value/page-fit gates remain separate and
unpassed. All preceding stopped candidate files and accepted papers
are unchanged. No numerical experiment, fitting or manuscript build
is a dependency.
