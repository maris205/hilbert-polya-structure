# Corank-two critical loci for the unbalanced single-phase selection

Date: 2026-09-06. Bounded author proof; not a formal Paper29, candidate
PASS, new singularity theory, or revision of any stopped result.

## Claim and mathematical status

**Author status: PROVABLE AS STATED with the fixed-period qualification
below.** The new all-period leading block is an explicit dependency whose
independent mathematical check is in progress. This note proves the
geometric consequence of that block and its established holomorphic
Schur realization; it does not claim that a truncated determinant alone
gives actual corank-two points.

Fix $6\mid k$, and a positive period vector $\boldsymbol n=(n_i)_{i=0}^{k-1}$.
Use the original single-negative-phase selection, not the new mixed-pattern
selection. As in [the all-period boundary calculation](PAPER29_ALL_PERIOD_BOUNDARY_PREFLIGHT_20260906.md),
put $a_i=1$ for $n_i=1$ and $a_i=1-1/n_i$ otherwise,
$w_i=a_i^{-1}$, $W=\sum_iw_i$, and
$$
\omega_\pm=\frac1W\sum_{j=0}^{k-1}w_j e^{\mp i\pi j/3}.
\tag{1}
$$
Assume $\omega_+\omega_-\ne0$. For these real positive weights this
is equivalent to $\omega_+\ne0$, since $\omega_-=\overline{\omega_+}$.
No condition is imposed on the remaining Fourier coefficients of $w$.

The map and normalized trace rows are
$$
F_{\epsilon,u}=H_{c_{k-1}}\circ\cdots\circ H_{c_0},\quad
H_c(x,y)=(x^2+c-y,x),\quad c_j=\epsilon^{-2}(u_j-1),
$$
$$
K_{ij}=\frac1{n_i\rho_i}\partial_{u_j}\rho_i,
\qquad \rho_i=\operatorname{tr}DF^{n_i}.
\tag{2}
$$
All derivatives hold $\epsilon$ fixed and are taken in $u$ before
evaluation at $u=\epsilon v$.

### Theorem

Define the four independent complex Fourier coordinates
$$
V_\pm=\frac1k\sum_jv_je^{\mp i\pi j/3},\qquad
Z_\pm=\frac1k\sum_jv_je^{\mp2\pi i j/3}.
\tag{3}
$$
Fix any values of the other $k-4$ Fourier coordinates, in a sufficiently
small neighborhood of a finite value. For all sufficiently small
$\epsilon$, there is a jointly holomorphic choice of the four coordinates
near
$$
V_+^*=-\frac1{2\omega_-},\quad
V_-^*=-\frac1{2\omega_+},\quad
Z_+^*=-\frac{\omega_+}{2\omega_-},\quad
Z_-^*=-\frac{\omega_-}{2\omega_+},
\tag{4}
$$
at which the actual Schur matrix of the normalized trace differential
is zero. At every corresponding point with $\epsilon\ne0$,
$$\operatorname{rank}K(\epsilon,\epsilon v)=k-2.\tag{5}$$
These points form a smooth codimension-four local submanifold of the
$v$-parameter space for each such $\epsilon$, and jointly a holomorphic
family across $\epsilon=0$ in the rescaled parameter space.

In local analytic coordinates $(x_{11},x_{12},x_{21},x_{22},z)$ centered
at one of these points, with $z\in\mathbb C^{k-4}$, the actual critical
hypersurface $\det K=0$ for fixed nonzero $\epsilon$ is exactly
$$x_{11}x_{22}-x_{12}x_{21}=0.\tag{6}$$
Its local singular locus is $x_{11}=x_{12}=x_{21}=x_{22}=0$, and
is precisely the corank-two locus in this neighborhood. Away from this
submanifold its critical points have corank one. The selected state
cycles remain exact, disjoint and simple, with nonzero traces.

The radii in this theorem may depend on the fixed period vector, in
particular on the nonzero $\omega_\pm$. No uniformity as
$\omega_\pm\to0$ is asserted.

## Dependency and strategy

The [all-period boundary preflight](PAPER29_ALL_PERIOD_BOUNDARY_PREFLIGHT_20260906.md),
SHA256 `f39d735da4ba02802e3baa570c043260f4424898e186f9d671696e81b345ffc9`,
provides the actual jointly holomorphic rescaled matrix and its leading
two-by-two block. Its orbit construction, coefficient normalization,
moving-column correction and oblique projection are retained intact.

The present argument uses only the invertible affine four-coordinate
map, the holomorphic inverse/implicit function theorem, the exact Schur
determinant identity and elementary rank calculations. Those classical
tools are not claimed as innovations.

## Proof

### 1. The actual Schur matrix, not merely its determinant

The dependency supplies bounded invertible row/column changes and
analytic column scales $1,\epsilon^{\times(k-3)},\epsilon^2,\epsilon^2$.
Call the resulting holomorphic matrix $\mathcal A(\epsilon,v)$.
In complementary/resonant blocks its value at $\epsilon=0$ is
$$
\mathcal A(0,v)=
\begin{pmatrix}D_U&B(v)\\0&R_a(v)\end{pmatrix},
\tag{7}
$$
where $D_U$ is invertible and
$$
R_a(v)=\frac34
\begin{pmatrix}
1+2\omega_+V_-&-2Z_++2\omega_+V_+\\
-2Z_-+2\omega_-V_-&1+2\omega_-V_+
\end{pmatrix}.
\tag{8}
$$
No zero assumption on the upper-right block $B(v)$ is used.
On a sufficiently small neighborhood of a finite $v$ and for small
$\epsilon$, the actual $UU$ block stays invertible. Therefore
$$
\mathcal S(\epsilon,v)=\mathcal A_{RR}
-\mathcal A_{RU}\mathcal A_{UU}^{-1}\mathcal A_{UR}
\tag{9}
$$
is jointly holomorphic and satisfies $\mathcal S(0,v)=R_a(v)$.
This identity is valid when $R_a$ or $\mathcal S$ is singular;
only the complementary block is inverted.

### 2. Four independent controls and an actual zero matrix

The four frequencies in (3) are distinct for every positive multiple
of six. Together with the other Fourier coordinates they are linear
coordinates on $\mathbb C^k$. The affine map from the four displayed
coordinates to the four entries of (8) is invertible:

- its diagonal entries independently determine $V_-$ and $V_+$,
  using $\omega_+\ne0$ and $\omega_-\ne0$;
- once these are known, its off-diagonal entries independently
  determine $Z_+$ and $Z_-$.

Solving $R_a=0$ gives exactly (4). Let $z$ denote the remaining
coordinates and choose one finite $z_0$. At $(\epsilon,v)=(0,v^*(z_0))$
the derivative of the four entries of $\mathcal S$ with respect to
$(V_+,V_-,Z_+,Z_-)$ is that same invertible linear map.
The holomorphic implicit function theorem gives a unique nearby
solution of $\mathcal S=0$, holomorphic in $(\epsilon,z)$.

The parameters in (4) are finite for the fixed nonzero imbalance.
Thus a bounded $v$-neighborhood can be chosen first and then
$|\epsilon|$ made small enough that $u=\epsilon v$ lies in the
parent orbit domain. This is why no uniformity in vanishing imbalance
is needed or inferred.

### 3. Rank and the exact critical hypersurface germ

Block elimination by invertible matrices gives
$$
\operatorname{rank}\mathcal A=(k-2)+\operatorname{rank}\mathcal S,
\qquad
\det\mathcal A=\det\mathcal A_{UU}\det\mathcal S.
\tag{10}
$$
For $\epsilon\ne0$, all row/column changes and column scales relating
$\mathcal A$ to $K$ are invertible. Hence $\mathcal S=0$ gives (5),
not merely $\det K=0$. Simplicity of the cycles is unaffected because
their parameters remain in the parent sign-disc domain.

The holomorphic inverse function theorem, with $\epsilon,z$ as
parameters, makes the four actual entries of $\mathcal S$ into local
coordinates $x_{11},x_{12},x_{21},x_{22}$. The factor
$\det\mathcal A_{UU}$ and all determinant factors returning to $K$
are nonzero for fixed $\epsilon\ne0$. Thus their product is a
nonvanishing analytic unit, and $\det K=0$ has exactly equation (6).

The four partial derivatives of that quadratic are
$x_{22},-x_{21},-x_{12},x_{11}$. They vanish simultaneously exactly
at the zero matrix. At a nonzero zero-determinant two-by-two matrix,
the rank is one. Equation (10) proves both the stated singular locus
and the corank-one assertion away from it. This completes the proof.

## Balanced case and scale boundary

If $\omega_+=\omega_-=0$, the leading block (8) has diagonal entries
$3/4$, so its trace is $3/2$ on every $v$. On each fixed compact
$v$-set, the actual $\mathcal S$ has trace $3/2+O(\epsilon)$ and
cannot be the zero matrix for sufficiently small $\epsilon$.
Thus no analogous corank-two point occurs on that bounded rescaled
set in the balanced case. This does not exclude other parameter
scales, other selections or higher-order critical phenomena elsewhere.

As imbalance tends to zero, the $V_\pm^*$ in (4) diverge. The new
corank-two centers leave every bounded $v$-set, consistent with the
balanced two-coordinate leading cylinder. No statement about a smooth
global compactification of this transition is being made.

## Relation to the new minimal selection and limits

The [new minimal-selection author proof](PAPER29_MINIMAL_TRACE_SELECTION_PROOF_V1_20260906.md)
would, after its separate independent verification, provide another
$k$-trace selection that is full rank on a fixed $u$-neighborhood for
the same prescribed periods. Its conclusion is not a dependency for
the corank-two calculation. Once both results are accepted, the points
above show that even a corank-two critical singularity of a selected
trace map need not be a common infinitesimal defect of the full marked
spectrum. This is a short comparison consequence, not an additional
proof of global spectral rigidity.

Equation (6) describes the critical hypersurface in coefficient
parameter space. It does not classify the full map germ from
coefficients to traces, prove a fold/cusp normal form for that map,
classify the whole critical scheme globally, or show a state-space
bifurcation. No new claim concerning thermodynamic metric lower bounds
is made.

The geometric step here is a short consequence of the four-coordinate
Schur block. Its genuine content must be counted together with that
block once, not as a new general singularity-theory chapter. Neither
its correctness nor the number of displayed consequences establishes
the long-paper gate.
