# Complete source proof: exponential wall and a bounded-remainder obstruction

Fix a>0. On L²(0,∞) define H_a by the closed form
q_a[u]=∫(|u'|²+a²e^(2x)|u|²)dx, with domain
H¹_0(0,∞)∩L²(e^(2x)dx). The associated operator has u(0)=0,
locally absolutely continuous u,u', and −u''+a²e^(2x)u∈L².
There is no boundary condition at the limit-point endpoint infinity.
The spectral variable is E, and the positive frequency is k=sqrt(E).

## 1. Classical source and self-adjoint complete spectrum

For H_cl=p²+a²e^(2x), x≥0, specular reflection at zero, every energy
E=k²>a² is one bouncing periodic orbit. With x*=log(k/a), its full action is
J(E)=2∫_0^x* sqrt(E−a²e^(2x))dx
=2[k arcosh(k/a)−sqrt(k²−a²)], and its physical Hamiltonian period is
T(E)=J'(E)=arcosh(k/a)/k. This follows by y=ae^x/k and differentiating
the vanishing-endpoint integral; dot x=2p fixes the time factor.
Reversal is (x,p)↦(x,−p). E<a² has no trajectory, and E=a² is a
degenerate wall threshold, not a nontrivial orbit. The continuum of
energy-indexed cycles is not a prime-indexed orbit list.

The form is densely defined, closed and bounded below by a². On its unit
ball the L² tail beyond R is at most a⁻²e^(−2R); compactness of the H¹
embedding on [0,R] therefore gives compact form embedding and compact
resolvent. The spectrum consists of simple eigenvalues
a²<E₁<E₂<...→∞ and a complete orthogonal eigenbasis. Strictness follows
because q_a[u]−a²||u||²>0 for every nonzero form-domain vector. Simplicity
will also follow from the decaying solution below.

Put ν²=−E and z=ae^x. The equation becomes
z²y_zz+zy_z−(z²+ν²)y=0. Its unique square-integrable solution at infinity
is a multiple of y_E(x)=K_ν(ae^x). It decays as exp(−ae^x)/sqrt(ae^x);
an independent I solution grows. K is entire and even in ν, so y_E is
an entire function of E independent of the square-root branch. Hence

E is an eigenvalue if and only if K_sqrt(−E)(a)=0.

All such zeros are positive real spectral values, not just the numerically
found zeros. In particular K_ik(a) has exactly the two order zeros ±ik_n
for each E_n=k_n² and none off the imaginary order axis.

Define f_E(x)=K_ν(a)I_ν(ae^x)−I_ν(a)K_ν(ae^x).
The Bessel Wronskian gives f_E(0)=0 and f_E'(0)=1. The resolvent kernel is
G_E(x,y)=f_E(min(x,y))K_ν(ae^max(x,y))/K_ν(a), E∉spectrum.
It has derivative jump −1, obeys the Dirichlet condition, and has the
decaying tail; these properties verify the operator inverse, first on
compactly supported functions and then by the self-adjoint resolvent bound.
Apparent choices of ν in f cancel by uniqueness of its initial conditions.

Differentiate (H_a−E)y_E=0. For W=y_E(∂_E y_E)'−y_E'(∂_E y_E),
W'=−y_E² and W(∞)=0. At an eigenvalue this gives
||y_En||²=−a K'_ikn(a) [∂_E K_sqrt(−E)(a)]_(E=En)>0.
The first factor is nonzero by ODE uniqueness. Thus the boundary entire
function has a simple energy zero, with the correct positive norm; dividing
by this norm gives the full orthonormal basis. Prime denotes argument,
not order, differentiation.

## 2. A self-contained bounded-remainder Weyl proof

For real k>0, the exact I-series and connection formula give
I_−ik(a)=(a/2)^−ik Γ(1−ik)^−1 S_a(k),
S_a(k)=Σ_{j≥0}(a²/4)^j/[j!(1−ik)_j],
and K_ik(a)=π Im(I_−ik(a))/sinh(πk).
For k≥1, |(1−ik)_j|≥k^j, whence
|S_a(k)−1|≤exp(a²/(4k))−1=O_a(k⁻¹).
Termwise differentiation adds a factor at most j/k, giving
S_a'(k)=O_a(k⁻²). These bounds justify differentiation by uniformly
convergent majorants. For sufficiently large k, S_a has no zero and has
a continuous small argument.

Choose a continuous log Γ(1+ik) on k>0 and set
Ψ_a(k)=k log(2/a)+Im log Γ(1+ik)+arg S_a(k).
Stirling's formula and its differentiated expansion, with remainder in a
sector around the positive imaginary axis, give
Ψ_a(k)=k log(2k/a)−k+π/4+O_a(k⁻¹),
Ψ_a'(k)=log(2k/a)+O_a(k⁻²)>0 eventually.
The exact K formula is a nonzero real amplitude times sin Ψ_a(k).
It therefore has exactly one zero for each successive integer multiple
of π reached by Ψ, with no extra zeros. The finitely many low roots change
the count by O_a(1). Thus, with N_a(E)=#{n:E_n≤E},

N_a(k²)=[k arcosh(k/a)−sqrt(k²−a²)]/π+O_a(1)
=k log k/π+[log(2/a)−1]k/π+O_a(1).

The first equality follows since the exact action half differs from
k log(2k/a)−k by O_a(k⁻¹). Constants here may depend on fixed a;
there is no uniform claim as a→0. The argument uses exact zeros and an
eventually monotone phase, not a leading oscillatory approximation alone.

## 3. Fredholm determinant, heat trace and Schatten threshold

The Weyl law implies k_n~πn/log n, so Σ E_n^−p converges exactly for
p>1/2. In particular H_a⁻¹ is trace class and the ordinary determinant
D_a(E)=det(I−EH_a⁻¹)=∏(1−E/E_n) exists as a genus-zero entire product.

The integral K_ν(a)=∫_0^∞exp(−a cosh t)cosh(νt)dt shows both evenness
and the estimate log|K_sqrt(−E)(a)|≤C_a sqrt(|E|)log(|E|+2)+C_a.
Indeed |cosh(νt)|≤exp(|ν|t), cosh t≥e^t/2, and the substitution
v=ae^t/2 bounds the resulting integral by a gamma integral for |ν|≥1;
bounded ν is handled by continuity. Thus its order in E is at most 1/2,
and the Weyl zero count makes the order exactly 1/2. Hadamard factorization
for an entire function of order less than one has only a constant
zero-free exponential factor. Since K_0(a)>0, normalization at E=0 yields

D_a(E)=K_sqrt(−E)(a)/K_0(a).

This identity is an ordinary Fredholm determinant in energy, not a
regularized determinant chosen after fitting zeros. The resolvent is in
S_p exactly for p>1/2; using E_n−z instead of E_n leaves that threshold.

Write A=1/(2π), B=(log(2/a)−1)/π so N_a(E)=A sqrt(E)log E+B sqrt(E)+O_a(1).
Stieltjes integration gives Tr(exp(−tH_a))=t∫_0^∞e^−tE N_a(E)dE.
The bounded remainder contributes O_a(1), including the integrable low-energy
extension of the displayed main terms. Differentiate the gamma integral:
Γ(3/2)=sqrt(π)/2 and ψ(3/2)=2−γ−2log2. Consequently

Tr(exp(−tH_a))=[log(1/t)−γ−2log a]/[4sqrt(πt)]+O_a(1), t↓0.

The spectral zeta ΣE_n^−s initially converges for Re s>1/2. Its Mellin
heat formula continues it to Re s>0, with a double pole at s=1/2 and
leading coefficient 1/(4π). The bounded heat remainder gives a holomorphic
integral for Re s>0; exponential decay handles large t. No continuation
beyond that half-plane is asserted.

## 4. All-parameter residual obstruction after the allowed normalizations

The only external number-theoretic inputs in this section are the classical
Riemann–von Mangoldt formula and unbounded positive/negative values of S(T).
Dobner, arXiv:2101.01747v2, equation (1) and Theorem 1, supplies verified
unconditional statements of both; the Ω mechanism is classically due to
Selberg/Tsang. We do not reprove that number-theoretic theorem.

For every fixed a,c>0, fixed b∈R and fixed integer m, it is impossible that
N_a(c²T²+b)=N_R(T)+m for all sufficiently large T away from jumps.
Here N_R counts all nontrivial Riemann zeros with positive ordinate up to T,
with multiplicity, not merely the critical-line zeros. The left side equals
(c/π)T log T+(c/π)[log(2c/a)−1]T+O_(a,c,b)(1).
Riemann–von Mangoldt has main terms
T log T/(2π)−[log(2π)+1]T/(2π) and remainder S(T)+O(1), where
S(T)=O(log T) and is unbounded in both signs. Equality first forces
c=1/2 and then a=2π. At those values it would force S(T)=O(1), a
contradiction. The fixed energy shift b changes the main expression by
O(log T/T) and cannot alter this conclusion. A finite modification of the
spectrum changes only m and is also excluded.

This is a theorem about fixed positive frequency scaling, fixed energy
shift and finitely many levels. It does not cover arbitrary nonlinear
spectral reparametrizations, a parameter depending on T, or different
potentials. No target table is used; a=2π is a forced obstruction case,
not a fitted successful candidate. Merely matching the two leading terms
cannot repair the bounded residual.

## 5. Degeneration, ownership and scope

At a=0 the form becomes the free Dirichlet half-line Laplacian, with
continuous spectrum [0,∞), no compact resolvent and no inverse trace-class
determinant of this convention. For a↓0 the forms decrease on their common
core; closure gives strong-resolvent convergence to that free operator.
This also explains why the Weyl constants cannot be uniform in a.

Pólya's K-order zero result and Lagarias's more general half-line Morse
analysis are classical owners. DLMF supplies the Bessel/Stirling identities
used above. The present full source reconstruction, consequences and audit
do not establish new literature priority. In particular a natural positive
self-adjoint quantization and a true T log T law are not a target operator.
A0/A2/A3 fail; all target flags remain false. NO_BAD_EULER_OR_ROOT_NUMBER.
