# Derivation package

## 1. Chronological substitution cocycle

Let

\[
w_{-1}=b,\qquad w_0=a,\qquad w_{k+1}=w_kw_{k-1}.
\]

The lengths obey

\[
q_{-1}=q_0=1,\qquad q_{k+1}=q_k+q_{k-1},
\qquad q_k=F_{k+2}.
\]

Fix \(V(a)=\lambda,V(b)=0\) and define the one-site Schrödinger matrix

\[
A_v(E)=\begin{pmatrix}E-v&-1\\1&0\end{pmatrix}\in SL_2.
\]

For a chronological word \(w=c_1\cdots c_q\), use

\[
M(w;E)=A_{V(c_q)}(E)\cdots A_{V(c_1)}(E).
\]

The order is not averaged.  Word concatenation gives

\[
M_{k+1}=M_{k-1}M_k.
\]

Let \(d_k=\operatorname{tr}M_k\) and add the standard seed \(d_{-2}=2\).
The \(SL_2\) trace identity yields

\[
d_{k+1}=d_kd_{k-1}-d_{k-2},
\qquad (d_{-2},d_{-1},d_0)=(2,E,E-\lambda).
\]

The executable producer directly multiplies the chronological
matrices and checks this recursion through level five with symbolic
\((E,\lambda)\).

## 2. Trace map and invariant surface

Set \(x_k=d_k/2\).  Then

\[
x_{k+1}=2x_kx_{k-1}-x_{k-2}.
\]

With

\[
T(x,y,z)=(2xy-z,x,y),\qquad
\ell_\lambda(E)=\left(\frac{E-\lambda}{2},\frac E2,1\right),
\]

we have

\[
T^k\ell_\lambda(E)=(x_k,x_{k-1},x_{k-2}).
\]

The Fricke--Vogt invariant

\[
I(x,y,z)=x^2+y^2+z^2-2xyz-1
\]

satisfies

\[
I(\ell_\lambda(E))=\lambda^2/4.
\]

The polynomial degree records the physical word length:

\[
\deg_E d_k=q_k=F_{k+2}.
\]

This identity already displays two times: \(k\) is the number of
renormalization steps, while \(q_k\) is the number of lattice sites in the
periodic approximant.

## 3. Hitting and recurrence are different equations

The length-\(q_k\) Floquet discriminant is \(d_k(E)\).  If \(\theta\) is the
total Floquet phase accumulated across the entire \(q_k\)-site cell, then

\[
d_k(E)=2\cos\theta.
\]

Therefore

\[
d_k(E)=\pm2
\]

is a band-edge condition and \(d_k(E)=0\) is the discriminant-zero condition
\(\theta=\pi/2\pmod\pi\).  Here \(\theta\) is not the per-site
quasimomentum.
In trace-map language these equations say only

\[
T^k\ell_\lambda(E)\in\{x=\pm1\}
\quad\text{or}\quad
T^k\ell_\lambda(E)\in\{x=0\}.
\]

They are finite-time hits of one codimension-one section.  Periodicity with
return time \(m\) requires all three equations

\[
d_m=d_0,\qquad d_{m-1}=d_{-1},\qquad d_{m-2}=2.
\]

Neither \(m=k\) nor \(m=q_k\) is justified: the former confuses a section hit
with a return, and the latter identifies physical lattice length with
renormalization time.

## 4. Minimal exact counterexamples

At \(\lambda=1\),

\[
d_1(E)=E(E-1)-2.
\]

For the finite periodic approximant, \(E=0\) is a band edge with
\(d_1=-2\).  The half-trace sequence from indices \(-2\) upward is

\[
1,0,-\tfrac12,-1,1,-\tfrac32,-2,5,-\tfrac{37}{2},-183,\ldots.
\]

For \(E=-1\), \(d_1=0\), a finite-approximant discriminant-zero condition
(equivalently total cell Floquet phase
\(\theta=\pi/2\pmod\pi\)), and the sequence is

\[
1,-\tfrac12,-1,0,\tfrac12,1,1,\tfrac32,2,5,\ldots.
\]

These are finite-approximant section energies, not points being asserted to
belong to the spectrum of the infinite Fibonacci Hamiltonian.  Both sequences
contain three consecutive absolute values

\[
1<\tfrac32<2<5.
\]

Once \(1<|x_{n-2}|<|x_{n-1}|<|x_n|\), the recurrence gives

\[
|x_{n+1}|\ge2|x_n||x_{n-1}|-|x_{n-2}|
>|x_n||x_{n-1}|,
\]

and the strict inequalities propagate.  If
\(a_r=\log|x_{n+r}|\), then \(a_{r+1}>a_r+a_{r-1}\); consequently
\(a_r\ge cF_{r+2}\) for some \(c>0\).  Both orbits are unbounded, hence
cannot be periodic for any return time, and their values grow
super-exponentially in the renormalization clock.

## 5. Exact modular factor gate

For \(k=1,\ldots,8\), set

\[
f_{k,c}(E)=d_k(E)-c,\qquad c\in\{0,2,-2\}.
\]

For each of \(m=k\) and \(m=q_k\), the code computes in
\(\mathbb F_{1000003}[E]\)

\[
\gcd\bigl(f_{k,c},d_m-d_0,d_{m-1}-d_{-1},d_{m-2}-2\bigr).
\]

All 48 gcds are 1.  Computation up to \(m=55\) is done in the quotient ring
modulo \(f_{k,c}\), so polynomial degrees never exceed \(q_k-1\).

Every \(f_{k,c}\) is monic over \(\mathbb Z\).  A nonconstant common factor
over \(\mathbb Q[E]\) would have a monic primitive representative over
\(\mathbb Z[E]\), whose reduction modulo any prime preserves its positive
degree and divides all reductions.  A degree-zero modular gcd therefore
certifies the absence of a common factor over \(\mathbb Q[E]\).

For the four frozen univariate polynomials, gcd \(1\) rules out every common
root in \(\overline{\mathbb Q}\), not merely a common factor of positive
degree as a geometric component.  The scope is nevertheless finite and
precise: the gate does not address a different return equation, a different
clock, or a newly defined energy-dependent operator whose determinant zeros
arise through global trace cancellations rather than through periodicity of
\(\ell_\lambda(E)\).

## 6. Casdagli band boundaries versus closed traces

Casdagli's theorem is used only in its source regime
\(V_{\rm C}\ge8\).  Centering the project potentials gives

\[
E_{\rm C}=E-\lambda/2,\qquad V_{\rm C}=\lambda/2,
\]

so this means \(\lambda\ge16\), not the \(\lambda=1\) regime of the exact
incidence witnesses.  Casdagli's endpoint-constrained spectral-band language
uses a ten-state graph with outgoing edges

\[
\begin{aligned}
1&\to\{3,7,10\},&2&\to\{4,8,9\},&3&\to6,&4&\to5,\\
5&\to1,&6&\to2,&7&\to1,&8&\to1,&9&\to2,&10&\to2.
\end{aligned}
\]

Let \(A_{10}\) be its row-current/column-next adjacency matrix and set

\[
u_{10}=e_1+e_6,\qquad v_{10}=e_1+e_2+e_3+e_4.
\]

Casdagli's admissible band words of \(n\) symbols have \(n-1\) edges.  His
Fibonacci convention is shifted by one from the standard convention here;
putting \(n=k+1\) gives

\[
u_{10}^{\top}A_{10}^kv_{10}=F_{k+2},\qquad
u_{10}^{\top}(I-zA_{10})^{-1}v_{10}
=\frac{1+z}{1-z-z^2}.
\]

Closed paths instead give

\[
\zeta_{A_{10}}(z)
=\exp\left(\sum_{k\ge1}\frac{z^k}{k}\operatorname{tr}A_{10}^k\right)
=\det(I-zA_{10})^{-1},
\]
\[
\det(I-zA_{10})
=(1+z)^2(1-z+z^2)(1-z-z^2).
\]

The boundary function therefore has a simple zero at \(z=-1\), after rational
continuation, while the closed zeta has a double pole there.  The source
identifications \(\{5,7,8\}\mapsto5\) and \(\{6,9,10\}\mapsto6\) yield an
unweighted six-state quotient.  With class-incidence matrix \(Q\), the exact
certificate checks

\[
A_{10}Q=QA_6,\qquad u_{10}^{\top}Q=u_6^{\top},\qquad Qv_6=v_{10}.
\]

An initial quotient symbol \(6\) is decorated with the lift to old state
\(R_6\), not \(R_9\) or \(R_{10}\).  An arbitrary energy-dependent weighting
does not automatically descend; it must additionally satisfy
\(L_{10}(E)Q=QL_6(E)\).  Even the source-faithful unweighted identity counts
bands, not the coefficients of the energy polynomial \(d_k(E)\).

## 7. All-level polynomial-weight degree/clock obstruction

The finite audit suggests a stronger theorem that does not depend on low
periods.

**Theorem (dimension-independent local-weight obstruction).**  For each
\(k\), let
\(B_k(E)\in\operatorname{Mat}_{N_k}(\mathbb C[E])\), where \(N_k<\infty\)
is arbitrary and every entry has degree at most a constant \(D\) independent
of \(k\).  Let \(u_k(E),v_k(E)\in\mathbb C[E]^{N_k}\) have entry-degrees
bounded uniformly by \(D_u,D_v\).  Then

\[
\deg_E\operatorname{tr} B_k(E)^k\le kD,
\qquad
\deg_E\bigl(u_k(E)^\top B_k(E)^kv_k(E)\bigr)
\le D_u+kD+D_v.
\]

The bound is independent of \(N_k\) and of the level dependence of the
coefficient matrices.  A fixed finite graph with polynomial edge weights is a
special case.  Consequently neither the closed-path traces nor the marked
boundary coefficients can equal the Fibonacci discriminants \(d_k(E)\) for
all sufficiently large \(k\), because

\[
\deg_E d_k=q_k=F_{k+2}
\]

grows exponentially in the renormalization time \(k\).

**Proof.**  Every entry of \(B_k(E)^k\) is a sum of products of \(k\) entries
of \(B_k(E)\).  Each product has degree at most \(kD\), and addition cannot
increase the maximum polynomial degree.  Taking a trace preserves this bound;
left and right multiplication by the uniformly bounded-degree boundary
vectors add at most \(D_u+D_v\).  Finally,
\(q_{k+1}=q_k+q_{k-1}\), while the leading term of
\(d_{k+1}=d_kd_{k-1}-d_{k-2}\) is the product of two monic polynomials of
degrees \(q_k,q_{k-1}\); hence \(d_{k+1}\) is monic of degree \(q_{k+1}\).
No uniform linear bound can equal \(F_{k+2}\) for all sufficiently large
\(k\).  \(\square\)

This theorem covers locally constant polynomial energy weights on any fixed
finite Markov coding, and more generally arbitrary finite \(N_k\).  It also
covers the order-\(k\) coefficients of finite boundary resolvents.  More
generally, if \(a_j(E)\) has degree at most \(jD\), then every coefficient of

\[
\exp\left(\pm\sum_{j\ge1}\frac{a_j(E)}{j}z^j\right)
\]

has degree at most its \(z\)-order times \(D\).  Taking
\(a_j=\operatorname{tr}B_k(E)^j\) covers both
\(\det(I-zB_k(E))\) and its reciprocal coefficientwise.  For the finite
determinant

\[
\det(I-zB_k(E))=\sum_{j=0}^{N_k}c_{k,j}(E)z^j,
\]

the principal-minor expansion similarly gives
\(\deg_Ec_{k,j}\le jD\); coefficients vanish for \(j>N_k\).

The obstruction has explicit escape routes, and none should be hidden:

1. index the model by physical time \(q_k\), not renormalization time \(k\);
2. allow local weights whose degree grows on the order of \(q_k/k\);
3. change to a growing-order full characteristic determinant, such as the
   natural \(q_k\)-dimensional Bloch Hamiltonian determinant, rather than a
   \(k\)-step trace or order-\(k\) determinant coefficient;
4. use a nonlinear or composition renormalization operator; or
5. define an infinite-dimensional energy-dependent Fredholm operator outside
   the uniformly bounded polynomial local-weight class.

The first route changes the clock; the second injects exponentially growing
target complexity; the third changes the observable.  Merely increasing
\(N_k\) does not evade the trace/boundary/coefficient bounds.  Thus this is a
class no-go theorem, not a no-go theorem for every weighted determinant.

## 8. Zero-radius analytic-germ obstruction

The same escape witnesses yield a different all-level theorem with a
different scope.  At \(E_*=0\) or \(-1\), the product inequality above gives,
after an index shift,

\[
\log|d_k(E_*)|\ge cF_k.
\]

Since \(F_k/k\to\infty\),

\[
|d_k(E_*)|^{1/k}\longrightarrow\infty.
\]

The Cauchy--Hadamard formula, together with
\(k^{-1/k}\to1\), therefore gives

\[
R\!\left(\sum_{k\ge0}d_k(E_*)z^k\right)=0,
\qquad
R\!\left(\sum_{k\ge1}\frac{d_k(E_*)}{k}z^k\right)=0.
\]

This proves the following dimension-free statement.  No scalar germ
\(G(z)\) analytic at \(z=0\) can satisfy

\[
[z^k]G(z)=d_k(E_*)
\]

for all sufficiently large \(k\).  Likewise, if \(\Delta\) is analytic near
zero and \(\Delta(0)=1\), then after shrinking the neighborhood it has an
analytic logarithm, so it cannot satisfy

\[
\pm k[z^k]\log\Delta(z)=d_k(E_*)
\]

for all sufficiently large \(k\).  Changing finitely many initial
coefficients does not change either convergence radius.

For a fixed bounded operator \(L\), every scalar resolvent matrix element
formed with fixed vectors and a continuous boundary functional is analytic
for sufficiently small \(z\).  A standard analytic Fredholm determinant of a
fixed trace-class or nuclear operator is normalized by \(\Delta(0)=1\) and
has a local analytic logarithm.  Hence these fixed infinite-dimensional
models are covered whenever their claimed realization is the literal
coefficient or signed logarithmic-trace identity above; fixed finite matrices
are only a special case.

C13G does not exclude physical-time powers indexed by \(q_k\),
\(k\)-dependent or nonanalytic/zero-radius formal constructions, operators
singular or undefined at \(E_*\), composition or moving-evaluation operators,
or indirect energy-divisor maps that do not identify \(d_k(E_*)\) with a
\(z^k\) coefficient or logarithmic trace.

## 9. Operator obstruction and surviving question

The infinite Fibonacci Hamiltonian is self-adjoint but has no eigenvalues for
any phase in the Fibonacci hull.  Its spectrum is singular-continuous and
Cantor.  It therefore cannot itself supply a discrete Hilbert--Pólya
eigenvalue sequence, while the ordinary trace-map Ruelle operator is a
different, generally non-self-adjoint object using the \(k\)-clock.  This does
not exclude a new operator derived from the trace dynamics.

The surviving theorem-scale question is whether there exists a canonical
boundary Fredholm construction

\[
\langle u,(I-z\mathcal L_{E,\theta})^{-1}v\rangle
\]

whose finite-level energy divisor is exactly
\(d_k(E)-2\cos\theta\), whose operator retains chronological word products,
and whose limit respects both clocks.  It must evade the degree theorem by an
explicit mechanism or use the physical clock honestly.  At the registered
witnesses it also cannot make \(d_k(E_*)\) the literal coefficients or
logarithmic traces of a scalar germ analytic at \(z=0\); an indirect divisor
identity is a different claim and must be stated explicitly.  Until the
operator, function space, weights, variables, normalization, and exact
coefficient/divisor identity are frozen, this proposal is `NOT_TESTABLE`.
