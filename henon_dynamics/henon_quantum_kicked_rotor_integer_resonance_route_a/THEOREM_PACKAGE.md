# Proof Package

## Claim

Let $\mathcal H=L^2(\mathbb T,d\theta/(2\pi))$, $|n\rangle(\theta)=e^{in\theta}$, $\widehat n=-i\partial_\theta$, $K_\kappa=\exp(-i\kappa\cos\theta)$ and

$$
U_{2\pi\ell}=\exp(-i\pi\ell\widehat n^2)K_\kappa,
\qquad \ell\in\mathbb Z_{>0},\quad \kappa\in\mathbb R.
$$

For every $m\in\mathbb Z$ and $t\in\mathbb Z_{\geq0}$:

1. If $\ell$ is even, then
   $$
   \langle n|U_{2\pi\ell}^t|m\rangle=(-i)^{n-m}J_{n-m}(\kappa t).
   $$
   Thus $P_t(n)=J_{n-m}(x)^2$, $x=\kappa t$, and
   $$
   \mathbb E[e^{iu(n-m)}]=J_0(2x\sin(u/2)).
   $$
   The centered odd moments through order six vanish, while
   $$
   \mu_2=x^2/2,\quad
   \mu_4=x^2/2+3x^4/8,\quad
   \mu_6=x^2/2+15x^4/8+5x^6/16.
   $$
   In particular $\operatorname{Var}(n)=\kappa^2t^2/2$ and
   $\langle\widehat n^2/2\rangle=m^2/2+\kappa^2t^2/4$.
2. If $\ell$ is odd, the free factor is the half-turn $R$, $(Rf)(\theta)=f(\theta+\pi)$, and $U_{2\pi\ell}=RK_\kappa$ satisfies $U_{2\pi\ell}^2=I$. At even $t$ the state is exactly $|m\rangle$; at odd $t$,
   $$
   \langle n|U_{2\pi\ell}^t|m\rangle=(-1)^n(-i)^{n-m}J_{n-m}(\kappa).
   $$

## Status

PROVABLE AS STATED.

## Assumptions and notation

The Floquet ordering is free-after-kick exactly as displayed.  Momentum moments refer to projective measurement in the basis $|n\rangle$.  $J_q$ is the Bessel function of the first kind with integer order $q$.  General rational resonance and detuning are excluded.

## Proof strategy and dependency map

1. Spectral calculus for $\widehat n^2$ and bounded multiplication prove unitarity.
2. The congruence $n^2\equiv n\pmod2$ reduces the free factor to $I$ or $R$.
3. The even sheet uses kick commutation and the Jacobi--Anger Fourier coefficient.
4. Parseval gives the characteristic function; differentiation gives moments.
5. The odd sheet uses $RK_\kappa R=K_\kappa^{-1}$.

## Proof

### Step 1: operator ownership

$\widehat n$ is self-adjoint on periodic $H^1(\mathbb T)$, hence $\widehat n^2$ is self-adjoint on periodic $H^2(\mathbb T)$.  Its exponential is unitary by spectral calculus.  Since $|e^{-i\kappa\cos\theta}|=1$, $K_\kappa$ is a bounded unitary multiplication operator.  Their displayed product is therefore a unitary on all of $\mathcal H$.

### Step 2: parity reduction

On $|n\rangle$ the free factor has eigenvalue $e^{-i\pi\ell n^2}$.  Because $n^2-n=n(n-1)$ is even, this eigenvalue is $e^{-i\pi\ell n}$.  It equals $1$ for even $\ell$ and $(-1)^n$ for odd $\ell$.  The latter is exactly $R$, since $e^{in(\theta+\pi)}=(-1)^ne^{in\theta}$.

### Step 3: even sheet

When $\ell$ is even, $U=K_\kappa$, so $U^t=K_{t\kappa}$.  Jacobi--Anger Fourier expansion gives

$$
e^{-ix\cos\theta}=\sum_{q\in\mathbb Z}(-i)^qJ_q(x)e^{iq\theta}.
$$

Multiplication by $e^{im\theta}$ and extraction of the $n$th coefficient, with $q=n-m$, proves the kernel.  Parseval gives normalization.

### Step 4: characteristic function and moments

Let $c_q=(-i)^qJ_q(x)$ be the Fourier coefficients of $f(\theta)=e^{-ix\cos\theta}$.  Fourier orthogonality yields

$$
\sum_q|c_q|^2e^{iqu}
=\frac1{2\pi}\int_0^{2\pi}f(\theta+u)\overline{f(\theta)}\,d\theta
=J_0(2x\sin(u/2)),
$$

where the last equality follows after shifting $\theta$ and using the integral representation of $J_0$.  Differentiating at $u=0$ gives the stated centered moments.  Translation by $m$ gives the mean and kinetic-energy formula.  Since the variance is exactly quadratic in $t$ for $\kappa\ne0$, the transport is ballistic in this stated moment sense.

### Step 5: odd sheet

For odd $\ell$, $U=RK_\kappa$.  The half-turn reverses the cosine, so

$$
RK_\kappa R=K_{-\kappa}=K_\kappa^{-1}.
$$

Consequently $U^2=RK_\kappa RK_\kappa=I$.  Even powers are $I$ and odd powers are $U$.  Applying $R$ to each momentum coefficient after the kick multiplies it by $(-1)^n$, giving the asserted odd-time kernel.

### Step 6: boundaries

For $\kappa=0$, even $\ell$ gives $U=I$ and odd $\ell$ gives $U=R$; every momentum probability is stationary, although odd-momentum vectors acquire a sign under one odd-sheet kick.  The formula at $t=0$ uses $J_q(0)=\delta_{q0}$.  Negative $m$ requires no change.  Reversing the Floquet order is a different convention and is not silently identified with this theorem.

Therefore the claim follows. ∎

## Corrections or missing assumptions

None.  The positive-integer domain for $\ell$ and the free-after-kick ordering are essential frozen conventions.

## Open risks

Finite evidence cannot prove the infinite Bessel identities; the analytic Fourier proof does.  No statement is made about detuning or noninteger resonance sheets.
