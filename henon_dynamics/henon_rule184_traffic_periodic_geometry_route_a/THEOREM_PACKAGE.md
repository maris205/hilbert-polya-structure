# C175 theorem package

## Assumptions and conventions

For `N>=1` and `0<=k<=N`, let
\[
X_{N,k}=\{x\in\{0,1\}^{\mathbb Z/N\mathbb Z}:\sum_i x_i=k\}.
\]
The simultaneous Rule-184 update is
\[
F(x)_i=x_{i-1}(1-x_i)+x_ix_{i+1},
\]
equivalently every cyclic `10` moves to `01`. One application of `F` is the clock. The right rotation is `(rho x)_i=x_{i-1}`. Put `m=min(k,N-k)`.

## Classification and attraction theorem

For every `N`, `k`, and state `x`:

1. If `k<=N/2`, then `x` is periodic exactly when it contains no cyclic `11`; on this core `F=rho`.
2. If `k>=N/2`, then `x` is periodic exactly when it contains no cyclic `00`; on this core `F=rho^{-1}`.
3. If `N` is even and `k=N/2`, the core is exactly the two alternating states and both have period two. At `k=0,N`, the unique uniform state is fixed.
4. Every temporal least period divides `N` and is the least cyclic-rotation period of the word.
5. Every state reaches the applicable isolated-minority core in at most `m^2` updates.

### Gap-Lyapunov proof

Assume first `0<k<=N/2` and label the `m=k` particles in cyclic order. Let `g_i>=0` be the number of holes between particle `i` and the next particle, and let `u_i=1_(g_i>0)`. Particle `i` moves precisely when `u_i=1`, so
\[
g_i'=g_i-u_i+u_{i+1}.
\]
A new zero at index `i` occurs exactly when the old `g_(i+1)=0` and `g_i<=1`. Thus each old zero-gap marker shifts one index backward unless the predecessor is at least two, in which case that marker is absorbed. The number `Z(g)=#{i:g_i=0}` never increases.

If `Z(g)>0`, then `sum_i g_i=N-k>=k=m`; hence some gap is at least two. Such an excess gap stays at the same index until a zero marker arrives immediately after it, while every unabsorbed zero moves backward by one index per update. Within at most `m` updates a zero meets an excess and `Z` strictly decreases. Since initially `Z<=m`, after at most `m^2` steps every gap is positive. This is exactly the no-`11` core. There every particle moves, so `F` is right rotation.

For `k>=N/2`, exchange particles with holes and reverse the cyclic orientation. Holes move left by the same gap law, proving attraction to the no-`00` core and left rotation there. The two descriptions agree at half filling. Conversely every core word is periodic because a rotation of an `N`-word has order dividing `N`. If a periodic word entered the forward-invariant core after positive time, a sufficiently large multiple of its period would put the original word in the core; hence no non-core word is periodic.

## Fixed counts and primitive cycles

Define the number of cyclic length-`g` words with `r` isolated marked sites by
\[
I(g,r)=
\begin{cases}
1,&r=0,\\
\dfrac{g}{g-r}\binom{g-r}{r},&1\le r\le\lfloor g/2\rfloor,\\
0,&\text{otherwise}.
\end{cases}
\]
The formula follows by counting linear nonadjacent words and subtracting those with both endpoints marked.

For every `n>=1`, put `g=gcd(N,n)` and `q=N/g`. Then
\[
#\operatorname{Fix}(F^n|X_{N,k})=
\begin{cases}
I(g,m/q),&q\mid m,\\
0,&q\nmid m.
\end{cases}
\]
Indeed an `F^n`-fixed word is periodic, hence lies in the isolated-minority core. On that core `F^n` is rotation by `+n` or `-n`. Rotation invariance makes the word `q` repetitions of a cyclic block of length `g`; its minority count is `m/q`, and isolation is exactly cyclic independence in that block.

For `d|N`, Möbius inversion gives exact-period points and primitive geometric cycles:
\[
E_{N,k}(d)=\sum_{e\mid d}\mu(d/e)\,#\operatorname{Fix}(F^e),
\qquad P_{N,k}(d)=E_{N,k}(d)/d.
\]
Consequently
\[
\zeta_{N,k}(z)=\prod_{d\mid N}(1-z^d)^{-P_{N,k}(d)}.
\]
For the uniform Koopman permutation `U_core` on the periodic core,
\[
\det(I-zU_{\rm core})=\prod_{d\mid N}(1-z^d)^{P_{N,k}(d)}
=\zeta_{N,k}(z)^{-1}.
\]
At half filling the fixed count is two exactly for even `n`; at `k=0,N` it is one for every `n`.

## Whole-sector versus core Koopman boundary

Every word in `X_(N,k)` has isolated minority symbols exactly when `m<=1`. Hence the whole-sector map is a rotation permutation, and its uniform finite Koopman operator is unitary, exactly in those sectors. When `m>=2`, a word with adjacent minority symbols exists and is transient by the theorem. A finite map with a transient state is not bijective, so the uniform whole-sector composition operator is not unitary.

The periodic core is canonical and `F` restricts there to a finite rotation permutation. Its uniform Koopman operator is unitary, and spatial reflection reverses the rotation. This restriction discards the full-system transient geometry, so it earns only `A4_FORMAL_HINT` for the all-sector family.

## Evidence status and Route-A decision

Every theorem statement above is `PROVED`. Exhaustive enumeration through `N=12` and `n=2N+2` is only a deterministic regression sentinel.

The v0.2 tuple is `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`, overall `ROUTE_A_REJECTED`, Route B false. The primitive cycles are intrinsic and completely classified but contain no arithmetic information. The exact source zeta is not a target divisor comparison, and no target global analytic structure is obtained.
