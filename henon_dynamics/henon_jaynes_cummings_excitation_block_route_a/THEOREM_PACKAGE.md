# Theorem package

With `hbar=1`, let

\[
 H=\omega_c a^\dagger a+\frac{\omega_q}{2}\sigma_z
   +g(a^\dagger\sigma_-+a\sigma_+),
 \qquad
 N=a^\dagger a+\sigma_+\sigma_- .
\]

The atomic convention is `sigma_z|e>=|e>` and
`sigma_z|g>=-|g>`.

## Main theorem (conserved-excitation block atlas)

The commutator `[H,N]` vanishes.  The vacuum `|g,0>` is an eigenstate with
energy `-omega_q/2`.  For every `n>=1`, the excitation-`n` space with ordered
basis `{|e,n-1>,|g,n>}` is invariant and

\[
 H_n=c_n I+\frac{\Delta}{2}\sigma_z+g\sqrt n\,\sigma_x,
 \quad c_n=(n-\tfrac12)\omega_c,
 \quad \Delta=\omega_q-\omega_c.
\]

Writing

\[
 \Omega_n=\sqrt{\Delta^2+4g^2n},
\]

the dressed pair and propagator are

\[
 E_{n,\pm}=c_n\pm\frac{\Omega_n}{2},
\]

\[
 U_n(t)=e^{-ic_nt}\left[
 \cos\frac{\Omega_nt}{2}I
 -i\frac{\sin(\Omega_nt/2)}{\Omega_n}
   (\Delta\sigma_z+2g\sqrt n\,\sigma_x)\right],
\]

with its continuous identity limit when `Omega_n=0`.  Consequently

\[
 P_{|e,n-1\rangle\to|g,n\rangle}(t)
 =\frac{4g^2n}{\Omega_n^2}\sin^2\frac{\Omega_nt}{2},
\]

interpreted as zero on the simultaneous `g=Delta=0` face.  Each block is
unitary and

\[
 \operatorname{tr}U_n=2e^{-ic_nt}\cos(\Omega_nt/2),\qquad
 \det U_n=e^{-2ic_nt}.
\]

## Proof

Every interaction monomial destroys one atomic excitation while creating one
photon, or performs the reverse operation; hence it commutes with `N`.
Applying `H` to the two ordered bare states gives the displayed matrix.  Its
traceless part `B_n` satisfies `B_n^2=(Omega_n^2/4)I`.  The characteristic
polynomial and the even/odd power series of `exp(-itB_n)` give the dressed
energies and propagator.  The off-diagonal entry gives the transition law;
`B_n` self-adjoint and the Pauli-square identity give unitarity, trace and
determinant.

## Revival and boundary theorem

For a finite set `S` of active coupled bare blocks (`g sqrt(n)` nonzero), a
single positive time `T` restores every bare population for all initial bare
states in those blocks if and only if

\[
 \Omega_nT\in2\pi\mathbb Z\qquad(n\in S).
\]

Equivalently, the positive frequencies in `S` are rationally commensurate.
At such a time, `U_n(T)=e^{-ic_nT}(-1)^{k_n}I`; a common state-vector revival
therefore also requires these block phases, and any occupied vacuum phase, to
agree up to one global phase.  Population revival alone does not imply that
extra condition.

At `g=0` the bare states decouple.  At resonance,
`Omega_n=2|g|sqrt(n)` and the exchange amplitude is one.  The `n=0` vacuum is
not inserted into an `n>=1` square-root block.  Conjugation by a diagonal
atomic phase changes `g` to `-g`, leaving energies and probabilities fixed.
A finite Fock compression preserves all blocks below its dangling top state.
On the full infinite Fock space, every unitary has infinitely many singular
values equal to one; this propagator is noncompact and not Schatten.  Thus no
ordinary full-space trace or Fredholm determinant is asserted.
