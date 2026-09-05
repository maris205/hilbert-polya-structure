# Proof package: boundary-corrected reversible multibaker transport

## Claim and status

**PROVABLE AFTER AN EXPLICIT BOUNDARY CORRECTION.** The unqualified proposal
that every binary periodic word is a geometric periodic orbit is false on the
usual half-open square: the all-one word projects to an excluded corner.
Keeping both corners instead does not give the same single-valued baker
convention. We work on the invariant full-measure set below. Every mixed
periodic word, and only such a word, gives a geometric periodic point. The
transport determinant retains both homogeneous symbolic cycles; their exact
removal is part of the theorem, not an unreported convention change.

For every integer $L\geq1$, the reversible multibaker on a ring of $L$ cells
has a complete mixed-word primitive orbit classification, winding and
repetition law, reciprocal multipliers, and a boundary-corrected weighted
orbit product. The associated finite transport determinant has an exact
Chebyshev formula, hydrodynamic branch and parity-sensitive relaxation law.

## Assumptions and notation

Let $\mathcal D$ be the dyadic rationals in $[0,1]$, let
$X=(0,1)\setminus\mathcal D$, and put
$M_L=(\mathbb Z/L\mathbb Z)\times X\times X$. With $s=\lfloor2x\rfloor$ and
$d_s=2s-1$, define
$$
B(j,x,y)=(j+d_s\pmod L,\ 2x-s,\ (y+s)/2).
$$
Time and cell length are both one. Write $I(j,x,y)=(j,1-y,1-x)$.
For a binary word $w=s_0\cdots s_{n-1}$, let $a(w)$ be its binary integer,
$w^{\rm rev}=s_{n-1}\cdots s_0$, and $S(w)=\sum_t d_{s_t}$.
A mixed word contains both symbols. A binary necklace is a word modulo
cyclic rotation. Its least word period is denoted $d$.
For a closed geometric orbit, $W=S/L$ is winding. A real twist $\phi$ weights
it by $e^{i\phi W}$. Signed phases are retained throughout.

The finite transport operator is the backward tilted Markov operator
$$
(P_\phi f)_j=\tfrac12e^{i\phi/L}f_{j+1}
             +\tfrac12e^{-i\phi/L}f_{j-1}.
$$
Both summands are retained when their destination cells coincide, including
$L=1,2$. It is a finite-dimensional source transport operator; it is not the
full Perron operator on phase-space functions. Put
$D_L(z,\phi)=\det(I-zP_\phi)$.

## Strategy and dependency map

1. Unique non-dyadic binary expansions give the symbolic conjugacy and
   reversibility, with an explicit account of missing homogeneous words.
2. Affine iteration reconstructs all periodic points. The cell cocycle gives
   the least geometric period and multiplicity over each primitive necklace.
3. Fourier diagonalization and a Chebyshev polynomial identity give the
   finite determinant. A closed-word trace counts its coefficients.
4. Grouping closed points into powers of primitive cycles gives the geometric
   weighted product; the two removed symbolic cycles yield its correction.
5. The Fourier spectrum and Bernoulli increments give exact relaxation and
   diffusion. No unbounded theorem is inferred from the finite evidence.

## Proof

### 1. Domain, conjugacy and reversal

Every point of $X$ has a unique infinite binary expansion which is not
eventually constant. Encode
$x=.s_0s_1s_2\ldots$ and $y=.s_{-1}s_{-2}s_{-3}\ldots$.
The allowed bi-infinite sequences have neither tail eventually constant.
The map $B$ shifts this sequence left and adds $d_{s_0}$ to the cell. Conversely,
the two expansions reconstruct the point. Thus this coding is a bijective
conjugacy, not a finite-to-one coding with an ignored endpoint ambiguity.
Doubling, inverse doubling and complement preserve non-dyadic coordinates,
so the domain is invariant under $B$, $B^{-1}$ and $I$.

If $t=\lfloor2y\rfloor$, the inverse is
$$
B^{-1}(j,x,y)=(j-d_t,\ (x+t)/2,\ 2y-t).
$$
Since $y\neq1/2$, the first symbol of $1-y$ is $1-t$. Substitution in
$IBI$ gives this inverse formula and $I^2=\mathrm{id}$. Each smooth branch
has derivative $\operatorname{diag}(2,1/2)$ and determinant one. Since branch
images partition the full-measure domain, normalized cell counting measure
times Lebesgue area is invariant. The reversal $I$ is anti-symplectic on each
cell, because it sends $dx\wedge dy$ to $-dx\wedge dy$.

### 2. Exact periodic point and primitive classification

For an itinerary of length $n$, affine iteration yields
$x_n=2^nx-a(w)$ and
$y_n=2^{-n}y+2^{-n}a(w^{\rm rev})$.
Consequently the only possible fixed coordinates are
$$
x=\frac{a(w)}{2^n-1},\qquad
y=\frac{a(w^{\rm rev})}{2^n-1}.
$$
For a mixed word these are in $(0,1)$ with odd reduced denominators greater
than one, hence are non-dyadic. Their periodic expansions give exactly the
specified itinerary. The cell closes exactly when $L\mid S(w)$. Every
periodic point has a periodic allowed coding, so the construction is complete.
The two homogeneous words give $(0,0)$ and $(1,1)$ and are excluded.

Now let $w$ be a primitive mixed binary necklace of length $d$ and net
displacement $S$. After $d$ steps the internal coordinates first return,
while the cell translates by $S$. Its additive order in $\mathbb Z/L\mathbb Z$
is $h=L/g$, where $g=\gcd(L,S)$ and $\gcd(L,0)=L$. Therefore the geometric
least period, winding and number of geometric cycles over this necklace are
$$
q=dh,\qquad W=S/g,\qquad m=g.
$$
For the multiplicity, there are $Ld$ point/word-phase choices over the
necklace, partitioned into cycles of length $dh$; their number is $g$.
An $r$-fold repetition has time $rq$, displacement $rLW$, winding $rW$ and
weight $2^{-rq}e^{ir\phi W}$. Its multipliers are $2^{rq}$ and $2^{-rq}$,
both positive. The map is orientation preserving.

Time reversal transforms the itinerary to the complement of the reversed
word, up to cyclic rotation. Its net displacement is $-S$, its period and
multiplicity are unchanged, and its winding is $-W$. This assertion is about
the action on cycles and permits self-reversing cycles; it does not divide
the orbit count by two.

The exact unweighted fixed-point census is
$$
F_{L,n}=L\left[\sum_{\substack{0\leq k\leq n\\L\mid(2k-n)}}
{n\choose k}-2\mathbf1_{L\mid n}\right].
$$
All least-period counts also follow from
$\#\mathcal P_q=q^{-1}\sum_{r\mid q}\mu(r)F_{L,q/r}$.
This is Möbius inversion of the disjoint primitive-power decomposition.

### 3. Transport determinant and its complete trace

The Fourier vectors $f_j=e^{2\pi ikj/L}$ diagonalize $P_\phi$, giving
$$
\lambda_k(\phi)=\cos\frac{2\pi k+\phi}{L},\quad0\leq k<L,
\qquad D_L=\prod_{k=0}^{L-1}(1-z\lambda_k).
$$
The degree-$L$ polynomial $T_L(t)-\cos\phi$ has precisely these roots,
counting multiplicity. For generic $\phi$ this follows from
$T_L(\cos\theta)=\cos L\theta$ with distinct roots; continuity extends the
identity to all $\phi$. Its leading coefficient is $2^{L-1}$, also valid at
$L=1$. Hence, as a polynomial after cancellation of the displayed powers,
$$
D_L(z,\phi)=2^{1-L}z^L\bigl(T_L(1/z)-\cos\phi\bigr).
$$
This formula covers collisions of Fourier eigenvalues and eigenvalue zero;
the degree in $z$ can drop when eigenvalues vanish. The spectrum above is the
complete root/multiplicity ledger, with determinant roots $z=1/\lambda_k$
only for nonzero $\lambda_k$. Shifting $\phi$ by $2\pi$ permutes the spectrum.

Expanding $P_\phi^n$ as signed steps, a diagonal matrix element requires
$L\mid S(w)$. Its phase is $e^{i\phi S(w)/L}$. Thus
$$
\operatorname{tr}P_\phi^n=
L2^{-n}\sum_{\substack{w\in\{0,1\}^n\\L\mid S(w)}}
e^{i\phi S(w)/L}.
$$
The two homogeneous symbolic cycles have least symbolic-lattice period $L$,
windings $+1,-1$, and weights $2^{-L}e^{\pm i\phi}$. These remain two
distinct labelled cycles when $L=1$ or $L=2$, even if transitions coincide.

### 4. Exact geometric correction and the stability-weight boundary

For real $\phi$ and $|z|<1$, the trace logarithm is absolutely convergent
because $|\operatorname{tr}P_\phi^n|\leq L$. Grouping terms into primitive
cycles in the finite labelled symbolic graph gives
$D_L^{-1}=\prod_{p\text{ symbolic}}(1-a_p)^{-1}$, with
$a_p=(z/2)^{q_p}e^{i\phi W_p}$. Removing exactly the two homogeneous cycles
therefore gives
$$
Z_L^{\rm geom}(z,\phi)
=\prod_{p\text{ geometric}}
\left(1-(z/2)^{q_p}e^{i\phi W_p}\right)^{-1}
=\frac{(1-(z/2)^Le^{i\phi})(1-(z/2)^Le^{-i\phi})}
{D_L(z,\phi)}.
$$
Absolute convergence can also be verified directly from
$F_{L,n}\leq L2^n$ in the logarithmic series. The rational expression supplies
meromorphic continuation in $z$; cancellations must be kept. It does not
certify any target divisor. Differentiating the logarithm gives all weighted
primitive-power trace identities, so the result is all-order, not a cutoff
extrapolation.

The unstable inverse multiplier is $2^{-n}$, the transport weight used here.
The two-dimensional fixed-point flat-trace denominator would instead be
$$
|\det(I-DB^n)|=\frac{(2^n-1)^2}{2^n}.
$$
Its inverse is not $2^{-n}$. We make no identification of $D_L$ with a full
phase-space Perron Fredholm determinant and no trace-class assertion for that
infinite-dimensional operator. This distinction is essential even though
both weights come from the same exact derivative matrix.

### 5. Diffusion, spectral gaps and degenerate rings

Under invariant Lebesgue measure the future symbols are independent fair
bits: each prescribed length-$n$ cylinder has width $2^{-n}$. On the
integer-cell lift, displacement $X_n=\sum_{t=0}^{n-1}d_{s_t}$ therefore has
$\mathbb E X_n=0$, $\operatorname{Var}X_n=n$ and
$\mathbb E e^{tX_n}=(\cosh t)^n$. With unit cell and time the diffusion
constant is $D=\lim_n\operatorname{Var}X_n/(2n)=1/2$.
The spatial Bloch branch is $\lambda(\kappa)=\cos\kappa$ and
$$
\log\lambda(\kappa)=-\kappa^2/2-\kappa^4/12+O(\kappa^6)
$$
near zero. On the ring the local branch is $\cos(\phi/L)$.

At $\phi=0$, $P_0$ is real symmetric, so its Fourier eigenvalues determine
the exact Euclidean operator norm on every invariant Fourier subspace.
For odd $L\geq3$, the norm on mean-zero vectors after $n$ steps is
$\cos(\pi/L)^n$, hence absolute gap $1-\cos(\pi/L)$.
The usual nonabsolute gap is $1-\cos(2\pi/L)$.
For even $L\geq2$, the parity mode $(-1)^j$ has eigenvalue $-1$, so there is
no convergence to the uniform distribution at every integer time.
For even $L\geq4$, after removing both uniform and parity modes, the exact
two-step norm is $\cos^2(2\pi/L)$; on the mean-zero subspace of each fixed
parity class this gives the two-step relaxation factor.

For $L=1$, $P_\phi=[\cos\phi]$, while the untilted chain has only its invariant
mode; a nontrivial relaxation gap is not defined. For $L=2$,
$P_\phi$ has off-diagonal entry $\cos(\phi/2)$ and
$D_2=1-z^2\cos^2(\phi/2)$; the untilted chain alternates deterministically and
has no internal parity-class relaxation mode. These facts coexist with
nontrivial internal baker dynamics and the geometric boundary correction.
For the explicitly different lazy control $Q=(I+P_0)/2$, all $L\geq2$ have
gap $\sin^2(\pi/L)$. This control is not silently substituted for $B$.

## Corrections and open risks

The boundary correction is compulsory, and the full-measure phase space is
part of the theorem. The analytic theorems above are proved without finite
cutoffs. Exact executable evidence only audits their formulas. The arithmetic
gate fails: cell size, binary symbols and winding contain no intrinsic
rational-prime data. Strict evaluation is $A0\_FAIL$, $A1\_WEAK$,
$A2\_FAIL$, $A3\_FAIL$, $A4\_FORMAL\_HINT$. The last grade records the
proved symplectic and reversible structure, not a constructed quantization.
No Route B or target arithmetic conclusion follows. Literature priority is
not claimed; the contribution is a self-contained, independently audited
assembly with its boundary and weight correction made explicit.
