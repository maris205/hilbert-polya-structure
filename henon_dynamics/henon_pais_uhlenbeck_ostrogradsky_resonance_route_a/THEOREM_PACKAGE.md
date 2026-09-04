# Proof package: Pais--Uhlenbeck resonance and difference spectrum

## Claim

Let
$$
L(x,\dot x,\ddot x)=\frac12\left[\ddot x^2-(\omega _1^2+\omega _2^2)\dot x^2+\omega _1^2\omega _2^2x^2\right].
$$
In the chamber (0<\omega _1<\omega _2), the associated Ostrogradsky flow is globally complete and canonically equivalent to the difference of harmonic oscillators of frequencies (\omega _1,\omega _2). If (\omega _1/\omega _2\in\mathbb Q), every trajectory is periodic. If the ratio is irrational, precisely the equilibrium and the single-mode trajectories are periodic, and every double-mode trajectory is dense in its invariant two-torus.

At coincident positive frequencies the Hamiltonian matrix has one size-two Jordan block at each of (+i\omega) and (-i\omega); at zero or negative squared frequencies the complete solution atlas is the factor-by-factor polynomial/hyperbolic atlas stated below.

For distinct positive frequencies and in units `hbar=1`, define the quantum operator as the Hermite-diagonal closure of
$$
\widehat H=-h_{\omega _1}\otimes I+I\otimes h_{\omega _2},
\qquad h_\omega=\frac12(-\partial_Q^2+\omega^2Q^2).
$$
It is self-adjoint and unbounded above and below. Rational frequency ratio gives an arithmetic lattice of eigenvalues, each of infinite multiplicity. Irrational ratio gives simple dense eigenvalues; the spectrum is all of (\mathbb R), while every spectral measure remains pure point.

## Status

PROVABLE AS STATED.

## Assumptions and notation

- The main classical and quantum chamber has (0<\omega _1<\omega _2) and (\Delta=\omega _2^2-\omega _1^2).
- The Ostrogradsky coordinates are (q_0=x,q_1=\dot x,p_1=\ddot x) and (p_0=-(\omega _1^2+\omega _2^2)\dot x-x^{(3)}), with ({q_j,p_k}=\delta_{jk}).
- A single-mode trajectory has exactly one nonzero normal-mode radius; a double-mode trajectory has both radii nonzero.
- For the boundary atlas, (\alpha,\beta\in\mathbb R) denote the two squared-frequency factors in ((D^2+\alpha)(D^2+\beta)x=0).
- “Pure point” describes spectral measures. “Discrete spectrum” is not used for the irrational chamber, whose eigenvalues are dense.

## Proof strategy and dependency map

1. The higher-order Euler--Lagrange equation and Legendre transform give the fourth-order equation and canonical Hamiltonian flow.
2. A displayed linear symplectic transform diagonalizes that Hamiltonian, yielding two rotations and invariant modal circles.
3. Elementary commensurability and Kronecker density classify every orbit closure.
4. Repeated, zero, and negative factors give the full degeneration atlas directly, without applying the singular distinct-frequency transform.
5. The Hermite transform identifies the quantum operator with a real diagonal multiplication operator on (\ell^2(\mathbb N_0^2)). Bézout and irrational rotation arguments then classify the spectrum.

## Proof

### 1. Ostrogradsky flow

The higher-order Euler--Lagrange equation is
$$
\frac{\partial L}{\partial x}-\frac{d}{dt}\frac{\partial L}{\partial\dot x}
+\frac{d^2}{dt^2}\frac{\partial L}{\partial\ddot x}=0.
$$
Substitution gives
$$
x^{(4)}+(\omega _1^2+\omega _2^2)\ddot x+\omega _1^2\omega _2^2x=0
=(D^2+\omega _1^2)(D^2+\omega _2^2)x. \tag{1}
$$
Since (p_1=\partial L/\partial\ddot x=\ddot x) and
$$
p_0=\frac{\partial L}{\partial\dot x}-\frac d{dt}\frac{\partial L}{\partial\ddot x}
=-(\omega _1^2+\omega _2^2)q_1-x^{(3)},
$$
the Legendre transform is
$$
H=p_0q_1+\frac12p_1^2+\frac12(\omega _1^2+\omega _2^2)q_1^2
-\frac12\omega _1^2\omega _2^2q_0^2. \tag{2}
$$
Hamilton's equations are
$$
\dot q_0=q_1,\quad \dot q_1=p_1,\quad
\dot p_0=\omega _1^2\omega _2^2q_0,\quad
\dot p_1=-p_0-(\omega _1^2+\omega _2^2)q_1. \tag{3}
$$
They reproduce (1). Their coefficient matrix is constant, so the flow exists for every real time.

### 2. Canonical normal form and signs

Define
$$
\begin{aligned}
Q_1&=\frac{p_1+\omega _2^2q_0}{\sqrt\Delta},&
P_1&=\frac{p_0+\omega _1^2q_1}{\sqrt\Delta},\\
Q_2&=\frac{p_1+\omega _1^2q_0}{\sqrt\Delta},&
P_2&=-\frac{p_0+\omega _2^2q_1}{\sqrt\Delta}.
\end{aligned} \tag{4}
$$
Direct use of ({q_j,p_k}=\delta_{jk}) yields
({Q_1,P_1}={Q_2,P_2}=1), while all cross brackets vanish. Thus (4) is symplectic. Solving (4) for the old variables and inserting them into (2) gives
$$
H=-\frac12(P_1^2+\omega _1^2Q_1^2)
+\frac12(P_2^2+\omega _2^2Q_2^2). \tag{5}
$$
In particular, the low-frequency mode carries the negative sign in this convention. Hamilton's equations from (5) imply (\ddot Q_j+\omega_j^2Q_j=0). The quantities
$$
R_j^2=Q_j^2+P_j^2/\omega_j^2 \tag{6}
$$
are constant. Each (R_j>0) supplies a phase circle, and (R_1R_2>0) supplies an invariant two-torus.

### 3. Complete orbit-closure classification

Every solution of (1) in the distinct chamber is
$$
x(t)=a_1\cos(\omega _1t)+b_1\sin(\omega _1t)
+a_2\cos(\omega _2t)+b_2\sin(\omega _2t). \tag{7}
$$
Suppose (\omega _1/\omega _2=m/n) in lowest terms, with positive integers (m,n), and write (\omega _1=gm,\omega _2=gn). Then (T=2\pi/g) advances the two phases by (2\pi m) and (2\pi n). Hence every trajectory returns after (T). A collapsed single-mode orbit can have a smaller least period; (T) is the common period of the entire flow.

Conversely, assume the ratio is irrational. Equilibrium is periodic, and a single-mode circle has period (2\pi/\omega_j). If a double-mode orbit had a period (T>0), both nonzero phase coordinates would return, so (\omega_1T,\omega_2T\in2\pi\mathbb Z); their quotient would be rational, a contradiction. Kronecker's theorem for the linear flow with rationally independent frequencies shows that its phase orbit is dense in (S^1\times S^1). The invertible map (4) transfers this statement to the corresponding invariant torus in Ostrogradsky phase space. This proves every assertion about classical orbit closure.

### 4. Degenerate-factor atlas

The distinct transform (4) is not used when (\Delta=0). For (\alpha=\beta=\omega^2>0), equation (1) becomes ((D^2+\omega^2)^2x=0), hence
$$
x(t)=(a+bt)\cos(\omega t)+(c+dt)\sin(\omega t). \tag{8}
$$
The first-order matrix has characteristic polynomial ((\lambda^2+\omega^2)^2). At each of (\lambda=\pm i\omega) its nullity is one, so each eigenvalue has one length-two Jordan chain. Formula (8) is periodic exactly when (b=d=0); otherwise it is unbounded linearly.

If exactly one factor is zero and the other is (D^2+\omega^2), then
$$
x(t)=a+bt+c\cos(\omega t)+d\sin(\omega t), \tag{9}
$$
which is bounded and periodic exactly when (b=0). If both factors vanish, (D^4x=0) and
$$
x(t)=a+bt+ct^2+dt^3. \tag{10}
$$
Here boundedness and periodicity are both equivalent to `b=c=d=0`.
If a factor is (D^2-\nu^2), its basis is (e^{\nu t},e^{-\nu t}). Thus a mixed positive/negative face has those two hyperbolic solutions plus one sine/cosine pair; a negative/zero face has them plus (1,t); two distinct negative factors have four exponentials. On the repeated negative face ((D^2-\nu^2)^2), the basis is (e^{\nu t},te^{\nu t},e^{-\nu t},te^{-\nu t}). These mutually exclusive sign/equality cases exhaust all real ((\alpha,\beta)), up to relabelling.

A nonzero hyperbolic component is unbounded in at least one time direction.
Consequently the all-time bounded and periodic subspaces are respectively
`span(cos,sin)` on a positive/negative face, `span(1)` on a zero/negative
face, and `{0}` on both distinct and repeated double-negative faces.  At the
positive collision both subspaces are `span(cos,sin)`; on the double-zero
face both are `span(1)`.  This completes the dynamical, not merely algebraic,
boundary classification.

### 5. Self-adjoint quantum difference spectrum

Let (phi_n^{(\omega)}) be the normalized Hermite eigenbasis of (h_\omega), with eigenvalue (\omega(n+1/2)). On the tensor basis
$$
e_{n_1,n_2}=\phi_{n_1}^{(\omega_1)}\otimes\phi_{n_2}^{(\omega_2)},
$$
define
$$
\lambda_{n_1,n_2}=\omega_2(n_2+1/2)-\omega_1(n_1+1/2) \tag{11}
$$
and
$$
\mathcal D(\widehat H)=\left\{\sum c_{n_1,n_2}e_{n_1,n_2}:
 (c_{n_1,n_2})\in\ell^2(\mathbb N_0^2),
\sum |\lambda_{n_1,n_2}|^2|c_{n_1,n_2}|^2<\infty\right\}. \tag{12}
$$
The Hermite transform is unitary from (L^2(\mathbb R^2)) to (\ell^2(\mathbb N_0^2)), and (12) becomes multiplication by the real sequence (\lambda_{n_1,n_2}). Real maximal multiplication operators are self-adjoint. Truncating coefficient arrays proves that the finite Hermite span is a core, so this is precisely the closure of the formal oscillator difference. Taking (n_1\to\infty) or (n_2\to\infty) proves that it is unbounded below and above.

For a rational ratio, write (\omega_1=gm,\omega_2=gn) with (gcd(m,n)=1). Then
$$
\lambda_{n_1,n_2}=g\left(nn_2-mn_1+\frac{n-m}{2}\right). \tag{13}
$$
Bézout's identity supplies integer solutions of (nv-mu=k) for every (k\in\mathbb Z). Adding ((n,m)L) to ((u,v)) preserves the equation and makes both coordinates nonnegative for all sufficiently large (L). Thus
$$
\sigma(\widehat H)=g\left(\mathbb Z+\frac{n-m}{2}\right), \tag{14}
$$
and every point in (14) has infinitely many basis eigenvectors.

For an irrational ratio, equality of two values in (11) would give
$$
\omega_2(n_2-n_2')=\omega_1(n_1-n_1'),
$$
so both differences vanish; all eigenvalues are simple. Irrational rotation makes the fractional parts of (n_1\omega_1/\omega_2) dense modulo one. Given any real target, choose arbitrarily large (n_1) whose fractional part permits an integer (n_2\ge0) to approximate that target in (11). Hence the eigenvalues are dense in (\mathbb R), and the spectrum, which is the closure of the diagonal values, is (\mathbb R). Finally, for (f=\sum c_{n_1,n_2}e_{n_1,n_2}), its spectral measure is
$$
\mu_f=\sum_{n_1,n_2}|c_{n_1,n_2}|^2\delta_{\lambda_{n_1,n_2}}, \tag{15}
$$
so every spectral measure is pure point even though the eigenvalue set is dense. This completes the proof. ∎

## Corrections and scope locks

- “All trajectories are periodic” is asserted only for rational frequency ratio. At irrational ratio, genuine two-mode trajectories are nonperiodic and dense on two-tori.
- The rational common time need not be the least period of a collapsed one-mode orbit.
- Equal-frequency quantization is not obtained by taking the singular limit of (4).
- The quantum difference spectrum is not semibounded and is not a Hilbert--Pólya operator.
- Finite grids verify conventions only; Kronecker, Bézout, and the diagonal-operator proof carry the infinite statements.

## Open risks

No theorem-internal gap remains under the frozen linear model. Alternative Hamiltonian structures or interacting higher-derivative theories lie outside this package.
