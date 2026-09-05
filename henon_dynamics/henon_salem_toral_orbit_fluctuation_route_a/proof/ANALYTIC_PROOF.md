# Complete source proof: quartic Salem toral dynamics

Fix an integer a≥1 and put
P_a(X)=X⁴−aX³−X²−aX+1. Let A have rows
(0,0,0,−1), (1,0,0,a), (0,1,0,1), (0,0,1,a), acting on R⁴/Z⁴.
The native clock is one iterate. Unless explicitly discussing the boundary,
assume a≠2. All vector spaces below are real unless a field is specified.

## 1. Algebra, measure, reversal and nonexpansiveness

The companion identity gives det(XI−A)=P_a and det A=1. Substitution
Z=X+X⁻¹ gives P_a(X)/X²=Z²−aZ−3. Its roots are
z±=(a±sqrt(a²+12))/2, with z+>2 and −2<z−<0.
Thus A has four distinct eigenvalues λ,λ⁻¹,ζ,ζ⁻¹, where λ>1,
ζ=exp(iθ), 0<θ<π, and 2cosθ=z−.

P_a has no rational root: the only possibilities ±1 give 1−2a and 1+2a.
If it factors over Q, Gauss's lemma gives two monic integer quadratics.
Their constant terms are either both +1 or both −1. In the first case write
(X²+bX+1)(X²+cX+1); b+c=−a and bc=−3 force a=2 for positive a.
In the second case the X and X³ coefficients have opposite signs, forcing
a=0, excluded. Therefore P_a is irreducible for every permitted a.
No eigenvalue is a root of unity: otherwise irreducibility would make P_a
cyclotomic and force λ onto the unit circle. In particular θ/(2π) is irrational.

Set
Ω=[[0,0,1,a],[0,0,0,1],[−1,0,0,0],[−a,−1,0,0]].
It has determinant one and AᵀΩA=Ω, so this is an integral symplectic map.
In Q[X]/(P_a), inversion X↦X⁻¹ is a well-defined integral involution
because the reciprocal polynomial is P_a and X is a unit. In the basis
1,X,X²,X³ its matrix is R=[e₁,A⁻¹e₁,A⁻²e₁,A⁻³e₁]. Hence
R²=I, RAR=A⁻¹, and direct multiplication gives RᵀΩR=−Ω.
It defines a same-clock antisymplectic reversor on the torus.

A preserves normalized Haar measure. Its Fourier characters transform by
the integer matrix Aᵀ. For every nonzero integer vector m the vectors
(Aᵀ)^n m never repeat, since a repetition would give a root of unity on
the rational cyclic subspace of m. Every bounded set contains finitely many
integer vectors, so each such orbit eventually leaves any bounded set.
The character correlations therefore tend to zero except for constants.
Density of trigonometric polynomials and the unitary bound prove mixing
on L²; in particular the system is ergodic. This is not expansiveness:
choose a nonzero vector v in the central plane E_c with arbitrarily small
norm. Diagonalizability bounds sup_{n∈Z}||Aⁿv|| by C||v||. Its projection
is a nonzero torus point remaining arbitrarily close to zero for all time.

## 2. Every fixed group, primitive orbit, stability and zeta

For n≥1 the integer matrix B_n=Aⁿ−I is nonsingular. Thus
Fix(Aⁿ)=B_n⁻¹Z⁴/Z⁴ ≅ Z⁴/B_n Z⁴. If d₁|d₂|d₃|d₄ are its positive
Smith factors (the k-th determinantal divisor is the gcd of all k-minors),
the group is the direct sum of Z/d_jZ. This is the full group, not just its
order, and proves that no fixed point is missing. Its order is

F_n=|det(Aⁿ−I)|=(λⁿ+λ⁻ⁿ−2)(2−2cos(nθ)).

The determinant before the absolute value is negative for every n, because
the positive real expanding/contracting factors have opposite signs and the
complex conjugate pair has positive product. Every finite fixed point has
a least period dividing n. Hence the number O_n of primitive oriented
cycles of least period n is
nO_n=Σ_{d|n} μ(n/d)F_d. All O_n are nonnegative integers by this orbit
partition. Repetition contributes one cycle with n marked points to F_{rn}.
There is no independent complex phase in this unweighted counting convention;
the signed Lefschetz index is −F_n, not F_n. The derivative at any n-return
is Aⁿ, with multipliers λⁿ,λ⁻ⁿ,ζⁿ,ζ⁻ⁿ. Reversal sends each oriented
cycle to its inverse-time cycle, of the same length and reciprocal multipliers;
cycles fixed by this involution are not divided by two in O_n.

For |z|<λ⁻¹, F_n≤4λⁿ, so the absolutely convergent Artin–Mazur zeta is
exp(Σ F_n zⁿ/n)=∏_{n≥1}(1−zⁿ)^(−O_n). Put
Q_a(z)=1+3z+(a²+4)z²+3z³+z⁴. The exterior-square determinant is
det(I−z∧²A)=(1−z)²Q_a(z); the first and third exterior determinants
both equal P_a(z), while degrees zero and four give 1−z.
The signed exterior-trace identity det(I−Aⁿ)=Σ(−1)^j tr((∧^jA)ⁿ)
and the negative sign above yield the complete rational continuation

Z_a(z)=(1−z)⁴ Q_a(z)/P_a(z)².

This is a native rational dynamical zeta, not a trace-class Koopman
determinant. The Koopman operator is unitary on an infinite-dimensional
space, hence is not compact and cannot itself be trace class.

## 3. Primitive and cumulative fluctuations at every period

For a fixed permitted a, 0≤F_d≤4λ^d. Every proper divisor d of n satisfies
d≤n/2. Möbius inversion therefore gives

nO_n/λⁿ = 2−2cos(nθ)+O_a(nλ^(−n/2)).

The term omitted from F_n/λⁿ itself is O_a(λ⁻ⁿ), uniformly in θn.
By the elementary geometric sum, the Cesàro average of exp(iknθ)
tends to zero for every nonzero integer k. Trigonometric approximation
then proves equidistribution of nθ modulo 2π. Thus the normalized primitive
counts have cluster set [0,4] and limiting probability density
1/[πsqrt(x(4−x))] on (0,4). The same proof gives all limiting moments;
the mean is 2 and the variance is 2. These are distributional asymptotics,
not a claim that the relative error is small when 2−2cos(nθ) is tiny.

Let Π(N)=Σ_{n≤N}O_n, r=λ⁻¹ and
C=2/(1−r), B=2/|1−r exp(−iθ)|. Then

NΠ(N)/λ^N = C−2Re(exp(iNθ)/(1−r exp(−iθ)))+O_a(1/N).

Indeed insert the preceding estimate and write n=N−j. For 0≤j≤N/2,
N/(N−j)=1+O(j/N), whose r^j-weighted error is O(1/N).
The n<N/2 terms contribute O_a(N²λ^(−N/2)); the tail of the geometric
series is exponentially small. Summing r^j and (r exp(−iθ))^j gives
the formula. Since θ is not zero modulo 2π, |1−r exp(−iθ)|>1−r,
so C>B>0. The cluster set is [C−B,C+B] and the limiting density is
1/[πsqrt(B²−(x−C)²)]. Consequently no constant-prefactor asymptotic
Π(N)~Kλ^N/N holds. An exponential orbit rate alone loses essential
oscillatory information; no lower bound on |ζⁿ−1| is used here.

## 4. Trivial homoclinic group and the exceptional cyclotomic member

Suppose Aⁿx→0 as n→±∞ on the torus. Choose lifts v_n→0 at each tail.
The integral vectors Av_n−v_{n+1} vanish for all sufficiently large |n|.
At the positive tail this forces v_n to lie in the stable eigenspace E_s;
at the negative tail it forces membership in the unstable eigenspace E_u.
Since A and A⁻¹ preserve the lattice, x belongs to both π(E_s) and π(E_u).
Write x=π(s)=π(u) with s∈E_s,u∈E_u. Then k=s−u is integral and belongs
to E_s⊕E_u. If k≠0 its rational cyclic span under A is a nonzero rational
invariant subspace. Irreducibility of P_a forces that span to have dimension
four, impossible inside a real two-plane. Hence k=0, and E_s∩E_u={0}
gives x=0. This supplies the complete elementary proof of the classical
nonexpansive homoclinic obstruction in this family, not a finite search.

At a=2, P_2=(X²−3X+1)(X²+X+1). If 3 divides n, Aⁿ−I has a rational
two-dimensional kernel, so its torus fixed set has a two-torus identity
component (possibly more components). Its cardinality is infinite. The
ordinary cardinality zeta is undefined for this boundary member; plugging
a=2 into a rational signed determinant expression does not repair that
definition. When 3 does not divide n the fixed group remains finite.

## 5. Ownership and Route-A boundary

Quasihyperbolic toral dynamics and its nonconstant prime-orbit asymptotics
are classical (Lind; Waddington). The trivial homoclinic theorem is also
classical (Lindenstrauss–Schmidt, Theorem 4.1/Corollary 4.2). The proofs
above specialize these mechanisms with explicit family constants and an
independent audit; they do not certify literature novelty.

The native arithmetic is an integral Salem unit, not a rational-prime
primitive carrier. The clock remains n, not an inserted log p roof. All
target flags are false, A2/A3 fail and Route B is not invoked.
NO_BAD_EULER_OR_ROOT_NUMBER.
