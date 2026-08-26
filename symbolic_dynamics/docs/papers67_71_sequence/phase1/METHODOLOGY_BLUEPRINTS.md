# Methodology blueprints and theorem contracts

## P67 theorem contract: arithmetic and `(a,b)`-exponent complexity

Fix coprime integers `a,b>=2` and a prime `p`.  Define

\[
X_{a,b,p}=\{x\in\mathbb F_p^{\mathbb N}:
x_n-x_{an}-x_{bn}+x_{abn}=0\text{ for every }n\ge1\}.
\]

For every `c>=1`, multiplicative decimation
`(M_cx)_n=x_(cn)` preserves `X`.  The local rule can be solved in increasing
order:

\[
x_{abn}=x_{an}+x_{bn}-x_n.
\]

Every coordinate divisible by `ab` has a strictly smaller predecessor `n`;
therefore arbitrary values on

\[
B=\{m\ge1:ab\nmid m\}
\]

extend uniquely to `X`.  On `[1,N]` the constraints with
`n<=floor(N/(ab))` have distinct largest pivots `abn`, yielding

\[
\dim_{\mathbb F_p}\pi_{[1,N]}X=N-\lfloor N/(ab)\rfloor.
\]

Because `gcd(a,b)=1`, each integer has a unique form `r a^i b^j` with neither
`a` nor `b` dividing `r`.  On a fixed `(a,b)`-root component, put
`y_(i,j)=x_(r a^i b^j)`.  Then

\[
y_{i,j}-y_{i+1,j}-y_{i,j+1}+y_{i+1,j+1}=0,
\]

and hence

\[
y_{i,j}=u_i+v_j
\]

with a one-dimensional gauge `(u,v)~(u+c,v-c)`.  Thus an `M x N` exponent
box has dimension `M+N-1` and exactly `p^(M+N-1)` patterns.  Its area-normalized
logarithmic complexity tends to zero when `min(M,N)->infinity`; no such claim
is made along a strip of fixed width.  Conversely, arbitrary finite choices
of the two boundary sequences `u_i` and `v_j` extend those sequences
arbitrarily and then define a global component by `y_(i,j)=u_i+v_j`; hence the
count is a projection count, not merely the nullity of internal equations.

**Stage-2 gates.**  Formalize the global extension homeomorphism and the
product over root components; keep the two normalizations distinct; search the
exact equation and finite-rank formula inside the 2026 prime-valuation source
and its citations.  If the exact pair of laws is already stated, subtract or
replace P67.

## P68 theorem contract: subgroup finite-dependence dichotomy

Let `A` and `B` be disjoint sets of sizes `m,n>=2`, and let `K_(m,n)` be
the complete bipartite graph with parts `A,B`.  For `d>=2`, set

\[
X_{m,n}^{(d)}=\operatorname{Hom}(\mathbb Z^d,K_{m,n}).
\]

The domain graph is connected and bipartite.  Every configuration has a
unique orientation `omega(x) in {+1,-1}` specifying which parity class maps
to `A`; translations obey

\[
\omega(\sigma^v x)=(-1)^{\sum_i v_i}\omega(x).
\]

Let `E=ker(v -> sum_i v_i mod 2)` and `L<=Z^d`.

- If `L<=E`, fix an orientation and choose every site independently and
  uniformly from its prescribed target part.  This is an `L`-invariant,
  full-support-on-that-component, 0-dependent process.
- If `L` contains an odd vector `v`, `L`-invariance forces the orientation to
  be fair.  The events revealing orientation at `0` and `2kv` are identical
  for arbitrarily large `k`, with covariance `1/4`; no `L`-invariant finitely
  dependent probability exists.

For every finite connected `F`, conditional freedom inside an orientation
gives

\[
|\mathcal L_F|=m^{e(F)}n^{o(F)}+n^{e(F)}m^{o(F)}.
\]

On Følner boxes, this yields `h_top=1/2 log(mn)`.  Entropy is maximized within
each orientation only by the parity-wise uniform product.  An odd translation
swaps the two components, so their equal mixture is the unique full-action
MME.  It has a nontrivial parity eigenfactor and is neither mixing nor finitely
dependent.

**Stage-2 gates.**  State carefully what “full support” means for an even-
subgroup component; prove the MME uniqueness via conditional entropy; check
whether the current finite-dependence paper or hom-shift literature already
records the bipartite subgroup dichotomy.  If only the phase observation
survives, stop as too thin.

## P69 theorem contract: Rudin--Shapiro range and square-root slow entropy

Let `theta` be the constant-length substitution

\[
a\mapsto ab,\qquad b\mapsto ac,\qquad
c\mapsto db,\qquad d\mapsto dc,
\]

let `(Y,S)` be its two-sided subshift, and put

\[
\kappa(a)=\kappa(b)=1,
\qquad \kappa(c)=\kappa(d)=-1.
\]

For the full `q`-shift `(A^Z,sigma)`, `q>=2`, freeze the generalized
`[T,T^-1]` skew product

\[
F(y,x)=(Sy,\sigma^{\kappa(y_0)}x).
\]

For a factor `w=w_0...w_(n-1)` define partial sums `s_0=0` and
`s_j=sum_(i<j) kappa(w_i)`, and set

\[
r(w)=1+\max_{0\le j\le n}s_j-\min_{0\le j\le n}s_j,
\qquad
R(n)=\max_{w\in\mathcal L_n(Y)}r(w).
\]

Use the finite clopen edge partition that records `y_0` and the fibre symbols
at both endpoints `0` and `kappa(y_0)` of the current cocycle step.  During an
`n`-name it reads the fibre at `s_0,...,s_n`.  Because every increment is `+1`
or `-1`, these coordinates form the entire integer interval between the
extreme partial sums.  Thus a fixed base factor exposes exactly `q^(r(w))`
fibre names, and the exact edge-name count is

\[
C_q(n)=\sum_{w\in\mathcal L_n(Y)}q^{r(w)}.
\]

Let `M(m)` be the largest signed sum of a length-`m` Rudin--Shapiro factor and
let `rho(m)=M(m)+1`, the abelian-complexity sequence studied in the cited
owner papers.  The difference between the largest and smallest partial sums of
`w` is the absolute sum of a contiguous subfactor.  The Rudin--Shapiro language
is sign-symmetric, and every shorter factor extends inside a length-`n` factor.
These three observations give the central reduction

\[
R(n)=1+\max_{1\le m\le n}M(m)
=\max_{1\le m\le n}\rho(m).
\]

The primitive constant-length Rudin--Shapiro base has linear factor complexity,
`p_Y(n)=O(n)`.  The finite spike additionally finds `p_Y(n)=8n-8` for every
tested `2<=n<=256`, but that exact formula is not used without proof.  Therefore

\[
R(n)\log q\le \log C_q(n)
\le R(n)\log q+O(\log n).
\]

For `k>=2`, let `s(k)=min{n:rho(n)=k}`.  Lü--Han prove

\[
s(2k)=4s(k)-1,
\qquad
s(2k+1)=4s(k).
\]

Consequently

\[
R(n)=\max\{k:s(k)\le n\}.
\]

Iteration gives the exact dyadic identity

\[
R(2^j)=
\begin{cases}
3\,2^{j/2}-1,&j\text{ even},\\
2^{(j+3)/2}-1,&j\text{ odd}.
\end{cases}
\]

Finite enumeration independently confirms the identity for `1<=j<=8` and the
running-maximum formula for every `n<=256`.  For the lower envelope, induction
in the displayed owner recurrence gives

\[
27s(k)\le5k^2+9,
\]

with equality at `k=3*2^t`.  Thus for

\[
n_t=s(3\cdot2^t)-1=\frac{5\cdot4^t-2}{3}
\]

we have `R(n_t)=3*2^t-1`.  Together with the owner bound
`rho(n)<=3sqrt(n)`, this yields the lower equality as follows: whenever
`R(n)=m`, one has `n<s(m+1)`, and the displayed inequality bounds
`m/sqrt(n)` from below asymptotically; the sequence `n_t` attains that bound.
For the upper equality, `R(n)<=3sqrt(n)` for every `n`, while the power-of-four
values approach `3`.  Hence

\[
\liminf_{n\to\infty}\frac{R(n)}{\sqrt n}=3\sqrt{3/5},
\qquad
\limsup_{n\to\infty}\frac{R(n)}{\sqrt n}=3.
\]

The owner recurrence also gives `rho(n+1)-rho(n) in {-1,1}`, hence
`R(n+1)-R(n) in {0,1}`.  The adjacent differences of `R(n)/sqrt(n)` therefore
tend to zero, so its accumulation set is the whole interval
`[3sqrt(3/5),3]`.

For the upper and lower edge-name growth constants this proves

\[
\overline h_{\sqrt{\cdot}}
=\limsup_{n\to\infty}\frac{\log C_q(n)}{\sqrt n},
\qquad
\underline h_{\sqrt{\cdot}}
=\liminf_{n\to\infty}\frac{\log C_q(n)}{\sqrt n},
\]

\[
\overline h_{\sqrt{\cdot}}=3\log q,
\qquad
\underline h_{\sqrt{\cdot}}=3\sqrt{3/5}\log q,
\]

and, more strongly,

\[
\operatorname{Acc}\left\{\frac{\log C_q(n)}{\sqrt n}:n\ge1\right\}
=\left[3\sqrt{3/5}\log q,\,3\log q\right].
\]

These are owner-derived Stage-1 mathematical conclusions, not novelty claims.
The displayed induction and endpoint conventions must be written as a formal
proof memo with exact theorem citations before they can appear in a manuscript.

**Stage-2 gates.**  First write the 2--3 page owner-subtracted proof memo and
verify that this atom/name count computes the intended topological slow
entropy: Carrasco--Vargas already uses essentially the same exponential range
sum, and a finite-window comparison with the usual product cover must be made
explicit.  The specialization alone does not pass paper mass.  Continue only
if a new layer such as a measure/topological gap or a broader cocycle-family
theorem survives exact source review; otherwise replace P69.  P54 and P62
already occupy uniform-morphism and substitution-combinatorics territory, so
no language/frequency padding is allowed.

## P70 theorem contract: finite-Heisenberg block decomposition

Let

\[
\Gamma=\langle a,b,c\mid[a,b]=c,\ [a,c]=[b,c]=1\rangle
\]

and, for a prime `p`, define

\[
X_p=\{x\in\mathbb F_p^\Gamma:
x_g+x_{ga}+x_{gb}=0\text{ for all }g\in\Gamma\}.
\]

For an odd prime `ell!=p`, let `N_ell` be the normal kernel of reduction
`Gamma -> Heis(F_ell)=Q`.  An `N_ell`-fixed configuration is a function on
`Q`, and the defining operator in the chosen convention is
`(Tx)(q)=x(q)+x(qa)+x(qb)`.  Over `k=overline(F_p)`, Maschke's theorem
decomposes this right-regular module.  Passing to the opposite left/right
convention replaces irreducibles by their duals (equivalently `f` by `f*`),
which permutes the one-dimensional roots and sends a central character
`zeta` to `zeta^-1`; the block nullities below are unchanged.

The `ell^2` one-dimensional blocks are singular precisely when
`1+alpha+beta=0` with `alpha^ell=beta^ell=1`.  Since `ell!=p`, the roots are
simple and their number is

\[
D_{p,\ell}=\deg\gcd_{\mathbb F_p}
(t^\ell-1,(-1-t)^\ell-1).
\]

For a nontrivial central character, the unique `ell`-dimensional irreducible
has clock/shift matrices `U,V`.  Direct expansion of the cyclic
diagonal-plus-shift determinant gives, in every characteristic with
`p!=ell`,

\[
\det(I+U+V)=\prod_{j=0}^{\ell-1}(1+\zeta^j)+1=2+1=3.
\]

Thus the block is invertible unless `p=3`; in characteristic three its cyclic
first-order recurrence has nullity exactly one.  Indeed, only in this singular
case do we need to divide by the diagonal entries `1+zeta^j`; they are nonzero
because `-1` has order two whereas `ell` is odd.  Every such irreducible
occurs with multiplicity `ell`, and there are `ell-1` nontrivial central
characters.  Extension of scalars preserves nullity, proving

\[
\dim_{\mathbb F_p}\operatorname{Fix}_{N_\ell}X_p
=D_{p,\ell}+\ell(\ell-1)\mathbf1_{p=3}.
\]

**Stage-2 gates.**  Fix the group multiplication and left/right convolution
once; prove the determinant sign and characteristic-three nullity lemma;
explain why dualizing conventions do not change nullity; compare the exact
formula against every finite-quotient discussion in the principal-action
owner and its citing neighborhood.

## P71 theorem contract: natural extension versus fibre profile

Let `tau:S->Z` be a surjection of finite sets whose fibre sizes are not all
equal (hence at least one fibre has size greater than one), and let

\[
\Sigma_{Z,S}=Z^{\mathbb Z_{<0}}\times S^{\mathbb Z_{\ge0}}.
\]

The full zip map is

\[
(\sigma_\tau x)_i=
\begin{cases}
\tau(x_0),&i=-1,\\
x_{i+1},&i\ne-1.
\end{cases}
\]

The factor map from the full two-sided `S`-shift is

\[
\Phi(t)_i=\begin{cases}\tau(t_i),&i<0,\\t_i,&i\ge0.\end{cases}
\]

and satisfies `Phi o sigma = sigma_tau o Phi`.  An inverse history of the zip
map records exactly the previously hidden interface symbols, so the natural
extension is conjugate to the full two-sided `S`-shift.  Standard natural-
extension theory then gives an affine entropy-preserving bijection of
invariant-measure simplexes and the unique MME.  Intrinsic ergodicity for the
uniform `n`-to-one full-zip subclass is prior work; here this is a supporting
natural-extension consequence for variable-degree maps, not the headline.

Put `k_z=|tau^-1(z)|`.  Local degree is

\[
d_\tau(x)=|\sigma_\tau^{-1}(x)|=k_{x_{-1}}.
\]

Fixed points correspond to `s in S`; the fixed point associated with `s` has
degree `k_(tau(s))`.  Therefore the number of fixed points of degree `k` is
`k m_k`, where `m_k` is the number of fibres of size `k`, and conjugacy
recovers every `m_k`.  Conversely equal fibre profiles admit bijections of `S`
and `Z` commuting with `tau`, producing a coordinatewise conjugacy.  Hence
fibre profile is a complete invariant.

For every test function `g`, periodic words give the degree-decorated identity

\[
\sum_{x\in\operatorname{Fix}(\sigma_\tau^n)}
\prod_{j=0}^{n-1}g(d_\tau(\sigma_\tau^j x))
=\left(\sum_{z\in Z}k_zg(k_z)\right)^n.
\]

Unweighted specialization gives `|Fix(sigma_tau^n)|=|S|^n`, the least-period
Möbius formula and zeta `1/(1-|S|z)`; these are supporting corollaries, not the
novelty headline.  The decorated identity is the `n`th power of its fixed-point
specialization, so it is a convenient conjugacy diagnostic rather than an
additional complete invariant.

**Stage-2 gates.**  Write the inverse-limit conjugacy explicitly and prove its
continuity; cite the invariant-measure/entropy correspondence; search all zip
papers for classification or natural-extension statements; distinguish fixed
points from points of least period; test whether arbitrary conjugacies really
preserve the local-degree histogram in the required form.  Pass a paper-mass
gate after subtracting the uniform-fibre entropy paper; otherwise replace P71.
