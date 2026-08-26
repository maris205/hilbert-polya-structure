# Theorem package

## Frozen family

Let \(E\) be any complex elliptic curve, \(\pi:E\to E/\{\pm1\}\cong\mathbb P^1\), and \(m\ge2\) an integer. Define \(f_m\) by \(f_m\circ\pi=\pi\circ[m]\). One application of \(f_m\) is one clock tick. Put \(a=m^n\) and

\[
h(a)=\#E[\gcd(a-1,a+1)]=\begin{cases}1,&a\text{ even},\\4,&a\text{ odd}.\end{cases}
\]

## Main theorem

For every \(E,m,n\) as above:

1. The fixed classes are
   \[
   \operatorname{Fix}(f_m^n)=\big(E[a-1]\cup E[a+1]\big)/\{\pm1\}.
   \]
2. They split disjointly into three channels:
   \[
   N_+=\frac{(a-1)^2-h(a)}2,\qquad
   N_-=\frac{(a+1)^2-h(a)}2,\qquad
   N_{\rm br}=h(a),
   \]
   with multipliers \(+a,-a,a^2\), respectively.
3. Consequently \(\#\operatorname{Fix}(f_m^n)=a^2+1\), and the holomorphic Lefschetz sum is exactly
   \[
   \frac{N_+}{1-a}+\frac{N_-}{1+a}+\frac{N_{\rm br}}{1-a^2}=1.
   \]
4. The Artin--Mazur zeta and exact-period counts are
   \[
   \zeta_{\rm AM}(z)=\frac1{(1-z)(1-m^2z)},\qquad
   P_m(n)=\sum_{d\mid n}\mu(n/d)(m^{2d}+1),
   \]
   and \(P_m(n)/n\) is the number of primitive cycles of length \(n\).
5. If \(\nu=\pi_*\mathrm{Haar}_E\), then the Koopman isometry \(U_mg=g\circ f_m\) on \(L^2(\mathbb P^1,\nu)\) has Wold model
   \[
   U_m\cong I_{\mathbb C}\oplus S^{(\aleph_0)}.
   \]
   In particular it is a proper, noncompact isometry outside every finite Schatten class; no ordinary Fredholm determinant \(\det(I-zU_m)\) exists.

## Proof

The equality \(f_m^n\pi(P)=\pi(P)\) holds exactly when \([a]P=P\) or \([a]P=-P\). Hence the fixed set is the stated torsion union. Its intersection is \(E[a-1]\cap E[a+1]=E[\gcd(a-1,a+1)]\). The gcd is one for even \(a\) and two for odd \(a\), giving one or four intersection points. These are precisely the quotient branch classes.

Away from the branch locus, \(\pi\) is locally biholomorphic. On \(E[a-1]\) the chain rule gives multiplier \(+a\). On \(E[a+1]\), use \(\pi(-P)=\pi(P)\) and \(D\pi_{-P}=-D\pi_P\) to get \(-a\). At a two-torsion point, a quotient coordinate is the square of a torus coordinate, so multiplication by \(a\) induces multiplier \(a^2\). Removing the intersection and dividing the remaining torsion points into sign pairs yields the three counts. Their sum and the displayed Lefschetz identity follow by direct algebra.

Exponentiating \(\sum_{n\ge1}(m^{2n}+1)z^n/n\) gives the zeta formula. Möbius inversion separates exact periods; partitioning exact-period points into cycles proves divisibility by \(n\).

Pullback by \(\pi\) identifies \(L^2(\mathbb P^1,\nu)\) with the even subspace of \(L^2(E)\). For a nonzero dual-lattice vector \(k\), let \(c_k=(e_k+e_{-k})/\sqrt2\), indexed modulo sign. Then \(U_mc_k=c_{mk}\). Every nonzero \(k\in\mathbb Z^2\) has a unique representation \(k=m^jr\) with \(r\notin m\mathbb Z^2\), modulo sign. Each primitive root therefore starts a unilateral shift chain, and there are countably infinitely many roots. Constants give the only unitary summand. The adjoint sends \(c_k\) to \(c_{k/m}\) exactly when both coordinates are divisible by \(m\), and to zero otherwise.

## Route-A consequence

The strict tuple is

\[
(\texttt{A0_FAIL},\texttt{A1_WEAK},\texttt{A2_FAIL},\texttt{A3_FAIL},\texttt{A4_FORMAL_HINT}).
\]

A0 fails because the torsion channels have no intrinsic rational-prime labels or prime-power repetition weights. A1 is weak despite a complete orbit formula because no arithmetic labels or target amplitudes arise. A2 and A3 fail because the zeta is the same elementary rational function for every elliptic modulus and supplies no target divisor or functional equation. A4 remains only a formal hint: the canonical observable lift is a proper non-Schatten isometry. Line-bundle quantization does not repair the frozen candidate because \([m]^*L\) changes degree by \(m^2\), so it does not act on one fixed quantization space.
