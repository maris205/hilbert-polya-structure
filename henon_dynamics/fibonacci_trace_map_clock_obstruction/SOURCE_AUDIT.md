# Primary-source audit

## Core trace-map/spectral bridge

[Damanik, Gorodetski, and Yessen, *The Fibonacci Hamiltonian*, Inventiones
Mathematicae 206 (2016)](https://doi.org/10.1007/s00222-016-0660-x)
gives a modern, all-coupling account of the exact relation between the
Fibonacci Hamiltonian and the trace map.  The [author preprint](https://arxiv.org/abs/1403.7823)
states that the spectrum is a dynamically defined Cantor set and proves exact
identities connecting spectral characteristics with pressure, equilibrium
measures, and periodic-orbit multipliers.

In the convention frozen here,

\[
T^k\ell_\lambda(E)=(x_k(E),x_{k-1}(E),x_{k-2}(E)),
\qquad d_k(E)=2x_k(E),
\]

where \(d_k\) is the Floquet discriminant of the length-\(q_k\) periodic
approximant.  Index shifts in the literature depend on the seed words; the two
clocks and the hitting/return distinction are invariant under those shifts.

## Hyperbolic coding and closed-orbit zeta

[Casdagli, *Symbolic dynamics for the renormalization map of a quasiperiodic
Schrödinger equation*, CMP 107 (1986)](https://doi.org/10.1007/BF01209396)
proves in its \(V_{\rm C}\ge8\) convention that the nonwandering set on the
invariant cubic surface is hyperbolic and conjugate to a subshift on six
symbols.  It is not used to assert a \(\lambda=1\) theorem outside that scope;
the all-coupling hyperbolic/spectral framework used here is supplied by
Damanik--Gorodetski--Yessen.  Centering the two project potentials gives

\[
E_{\rm C}=E-\lambda/2,\qquad V_{\rm C}=\lambda/2,
\]

with an exchange of the first two seed coordinates.  Thus Casdagli's proved
regime corresponds to \(\lambda\ge16\).  This large-coupling source statement
is separate from the exact \(\lambda=1\) escape and gcd audits.  Periodic
trace-map points in a Markov coding are coded by closed symbolic paths.

The expanded source presentation gives the ten-state graph on printed page
18, the conjugacy in Theorem 2.1/Corollary 2.2 on page 20, and the reduction
to six symbols on page 21.  Section 3.1, equations (3.1)--(3.2) and Lemma 3.1
on pages 26--27, gives initial states \(\{1,6\}\), terminal states
\(\{1,2,3,4\}\), and the marked spectral-band path count.  Consequently the
ten-state presentation, not its six-state quotient, is the primary spectral
language.  The project extracts \(A_{10},u_{10},v_{10}\) and proves

\[
u_{10}^\top A_{10}^kv_{10}=F_{k+2},\qquad
u_{10}^\top(I-zA_{10})^{-1}v_{10}=\frac{1+z}{1-z-z^2}.
\]

The source identification
\(\{5,7,8\}\mapsto5\), \(\{6,9,10\}\mapsto6\) gives a six-state
unweighted quotient.  The certificate verifies

\[
A_{10}Q=QA_6,\qquad
u_{10}^\top Q=u_6^\top,\qquad Qv_6=v_{10}.
\]

For the endpoint-constrained band language, an initial quotient symbol \(6\)
is decorated with its lift to old geometric state \(R_6\), rather than
\(R_9\) or \(R_{10}\).  General energy-dependent weights descend only after
the additional intertwining \(L_{10}(E)Q=QL_6(E)\) is proved; the unweighted
quotient does not supply that identity automatically.

For a subshift with adjacency matrix \(A\), the standard closed-orbit identity
is

\[
\zeta_{\mathrm{AM}}(z)
=\exp\left(\sum_{k\ge1}\frac{z^k}{k}\operatorname{tr}(A^k)\right)
=\det(I-zA)^{-1}.
\]

This is classical Bowen--Lanford theory; see [the primary proceedings
article](https://doi.org/10.1090/pspum/014/9985).  It is categorically a closed
path trace, unlike a boundary matrix element \(u^\top A^kv\).

## Periodic orbits and thermodynamic formalism are not new

- [Roberts--Baake 1994](https://doi.org/10.1007/BF02188581) studies
  reversibility, periodic orbits, and multipliers of the Fibonacci trace map.
- [Cantat 2009](https://doi.org/10.1215/00127094-2009-042), with
  [preprint](https://arxiv.org/abs/0711.1727), places trace maps in a broader
  character-surface and Hénon-type polynomial-dynamics framework.
- Damanik--Gorodetski--Yessen already connect thermodynamic pressure and
  periodic multipliers to spectral dimensions and transport.  Consequently,
  merely building a Ruelle operator or computing its spectrum is not a paper
  contribution.

## Natural self-adjoint operator boundary

[Damanik--Lenz, *Uniform spectral properties of one-dimensional
quasicrystals, I. Absence of eigenvalues*](https://arxiv.org/abs/math-ph/9903011),
[CMP DOI](https://doi.org/10.1007/s002200050742), proves absence of eigenvalues
for every element of the Fibonacci hull.  Together with the zero-measure
Cantor spectrum proved in
[S{\"u}t{\H{o}} 1989](https://doi.org/10.1007/BF01044450), this gives purely
singular-continuous spectral type.  The
infinite Hamiltonian is canonical and self-adjoint, but it does not provide a
discrete eigenvalue sequence for Hilbert--Pólya.

Finite periodic approximants do have ordinary Bloch discriminants.  Their
zeros and band edges converge toward a Cantor spectral set rather than an
entire discrete divisor.  This operator-theoretic fact is independent of the
open/closed incidence obstruction.

## Degree/clock theorem boundary

The project's all-level result is elementary but structurally stronger than
the finite audit.  At each level let
\(B_k(E)\in\operatorname{Mat}_{N_k}(\mathbb C[E])\), where \(N_k<\infty\)
is arbitrary, every entry has degree at most a uniform \(D\), and boundary
entry-degrees are uniformly bounded.  Path expansion gives

\[
\deg_E\operatorname{tr}B_k(E)^k\le kD,
\qquad
\deg_Eu_k(E)^\top B_k(E)^kv_k(E)\le D_u+kD+D_v.
\]

The comparison with \(\deg_Ed_k=F_{k+2}\) rules out uniformly bounded
polynomial-energy weights in renormalization time even when the finite state
dimension and the coefficient matrices vary with \(k\).  Energy is a passive
parameter: iteration is ordinary matrix multiplication, not substitution
\(E\mapsto P(E)\).  Standard Bowen--Lanford weighted-adjacency algebra
supplies the fixed-graph closed-path special case;
the degree comparison and its application to the Fibonacci discriminants are
proved directly in this project.  No novelty claim is made against general
Ruelle operators with nonlocal, unbounded-degree, or infinite-dimensional
energy dependence.  Physical-time \(q_k\)-step cocycles, composition
operators, moving evaluation at \(\ell_\lambda(E)\), and unbounded
level-dependent weight degree are explicit escape routes.  State-dimension
growth alone is not: it adds summands but does not raise the degree of a
\(k\)-step trace or boundary coefficient.  A growing-order full
characteristic determinant changes the observable and must be assessed
separately.

## Zero-radius theorem boundary

At the two exact \(\lambda=1\) witnesses, a strict escape triple implies

\[
|x_{j+1}|>|x_j||x_{j-1}|,
\qquad \log|d_j(E_*)|\ge cF_j.
\]

Consequently

\[
|d_k(E_*)|^{1/k}\longrightarrow\infty,
\]

and both \(\sum_kd_k(E_*)z^k\) and
\(\sum_{k\ge1}d_k(E_*)z^k/k\) have radius of convergence zero.  This gives a
dimension-free local-analytic obstruction: no scalar germ analytic at
\(z=0\) can have the \(d_k(E_*)\) as its literal coefficients, and no analytic
\(\Delta\), normalized by \(\Delta(0)=1\), can satisfy a literal signed
logarithmic-trace matching

\[
\pm k[z^k]\log\Delta(z)=d_k(E_*)
\]

for all sufficiently large \(k\).  Fixed bounded-operator resolvent matrix
elements and standard analytic Fredholm determinants are included whenever
the claimed identification is of this literal coefficient or logarithmic
form.  Finite matrices are only a special case.

Here \(E_*=0,-1\) are finite-periodic-approximant section energies whose
trace-map orbits escape; they are not being asserted to be spectral points of
the infinite Fibonacci Hamiltonian.  C13G does not cover physical-clock
indexing by \(q_k\), \(k\)-dependent or nonanalytic constructions, operators
singular or undefined at a witness, composition/moving-evaluation models, or
indirect maps in which \(d_k(E)\) enters a divisor without being the literal
\(z^k\) coefficient or logarithmic trace.

## Novelty-safe claim boundary

The project claims only:

1. an exact minimal counterexample to the naive identification of spectral
   section hits with trace-map periodic points;
2. a 48-case exact modular factor audit for the two most tempting clock
   identifications;
3. the source-faithful ten-state marked-band generating function and its
   explicitly decorated unweighted six-state quotient in Casdagli's
   large-coupling regime;
4. an all-level dimension-independent no-go theorem for uniformly
   bounded-polynomial passive weights, covering closed traces, boundary
   coefficients, and coefficientwise finite determinants; and
5. a zero-radius analytic-germ no-go for literal coefficient and
   logarithmic-trace matching at two exact finite-approximant section
   energies.

It does **not** claim that the Fibonacci trace map has not previously been
used in spectral theory, that no sophisticated energy-dependent relative
transfer operator can exist, or that a single modular audit excludes every
possible weighted determinant identity.  In particular, C13G does not address
an indirect energy-divisor map merely because it uses a Fredholm determinant.
A general energy-dependent Fredholm proposal remains `NOT_TESTABLE` until its
operator and the claimed coefficient/divisor identification are explicitly
defined.
