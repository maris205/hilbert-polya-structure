# Proof Package: complete-graph quantum search

## Claim

Let `N>=2`, `0<M<N`, `a=M/N`, and `g>=0`.  On `C^N` set

\[
H_g=-g|s\rangle\langle s|-P_W.
\]

The marked and unmarked dark spaces have eigenvalues `-1` and `0`, with
dimensions `M-1` and `N-M-1`.  On the bright space the two eigenvalues are

\[
\lambda_\pm=-\frac{g+1}{2}\pm\frac12
\sqrt{(g-1)^2+4ga}.
\]

Writing `Omega^2=(g-1)^2+4ga`, evolution from `|s>` has success probability

\[
p_W(t)=a+\frac{4ga(1-a)}{\Omega^2}
\sin^2(\Omega t/2).
\]

It reaches one if and only if `g=1`; its first hitting time is
`pi/(2 sqrt(a))`.  Off resonance its maximum is

\[
p_{\max}=a+\frac{4ga(1-a)}{(g-1)^2+4ga},\qquad
1-p_{\max}=\frac{(1-a)(g-1)^2}{(g-1)^2+4ga}.
\]

If `k` is a positive integer, `M=1`, `N=k^2` (hence `a=k^{-2}`), and
`g=1+c/k`, then, for fixed real `c` and large enough `k`,

\[
p_{\max}\longrightarrow\frac4{c^2+4},\qquad
\sqrt a\,t_{\rm peak}\longrightarrow\frac\pi{\sqrt{c^2+4}}.
\]

For complete-graph adjacency `A(K_N)=N|s><s|-I` and `g=gamma N`,
`-gamma A(K_N)-P_W=H_g+gamma I`, so the two propagators differ only by
`exp(-i gamma t)`.  The faces `M=0`, `M=N`, `N=1`, and `g=0` have the spectra
and constant success laws stated below.

## Status

PROVABLE AS STATED

## Assumptions and notation

- `P_W` is the orthogonal projector onto the span of the marked computational
  basis states.
- For `0<M<N`, `|w>` and `|r>` are the normalized uniform marked and unmarked
  vectors; `|s>=sqrt(a)|w>+sqrt(1-a)|r>`.
- Success probability is `||P_W exp(-itH_g)|s>||^2`, not one selected marked
  amplitude.
- The oracle coefficient is fixed to one, so `g` is dimensionless.

## Dependency map

1. Permutation symmetry supplies the orthogonal dark/bright decomposition.
2. The bright matrix, after removing its scalar trace, squares to
   `(Omega^2/4)I`; this gives both eigenvalues and the propagator.
3. The success formula follows by applying that propagator to `|s>`.
4. Positivity of the exact maximum defect proves the resonance iff theorem.
5. Direct substitution proves the critical-window limits and adjacency
   equivalence.
6. Missing bright vectors on boundary faces are handled directly rather than
   by negative multiplicities.

## Proof

### Step 1: invariant orthogonal sum

Let `D_W` be the marked vectors whose marked coordinates sum to zero and let
`D_R` be the analogous unmarked space.  Both are orthogonal to `|s>`.  Hence
`H_g=-I` on `D_W` and `H_g=0` on `D_R`.  Their dimensions are `M-1` and
`N-M-1`.  Their orthogonal complement is spanned by `|w>,|r>`.

### Step 2: bright spectrum

In the ordered basis `(|w>,|r>)`,

\[
H_B=-\begin{pmatrix}
1+ga&g\sqrt{a(1-a)}\\
g\sqrt{a(1-a)}&g(1-a)
\end{pmatrix}.
\]

Its trace is `-(g+1)` and determinant is `g(1-a)`.  Therefore the
discriminant is

\[
(g+1)^2-4g(1-a)=(g-1)^2+4ga=\Omega^2,
\]

which proves the eigenvalue formula and all multiplicities.

### Step 3: exact search law

Put `B=H_B+(g+1)I/2`.  Cayley--Hamilton gives `B^2=Omega^2 I/4`, hence

\[
e^{-itH_B}=e^{it(g+1)/2}
\left(\cos\frac{\Omega t}{2}I-
\frac{2i}{\Omega}\sin\frac{\Omega t}{2}B\right).
\]

Furthermore

\[
\langle w|B|s\rangle=-\frac{g+1}{2}\sqrt a.
\]

The marked dark component of the initial state is zero, so

\[
|\langle w|e^{-itH_g}|s\rangle|^2
=a\cos^2(\Omega t/2)+
\frac{a(g+1)^2}{\Omega^2}\sin^2(\Omega t/2).
\]

Since `(g+1)^2-Omega^2=4g(1-a)`, this is the claimed success law.

### Step 4: resonance is necessary and sufficient

For `0<a<1`, the first peak occurs at `t=pi/Omega`.  Algebra gives

\[
1-p_{\max}=
\frac{(1-a)(g-1)^2}{\Omega^2}.
\]

The denominator is positive throughout the interior domain.  The defect
vanishes exactly at `g=1`, where `Omega=2sqrt(a)` and the first peak is
`pi/(2sqrt(a))`.  This proves both directions; no continuity argument is
needed.

### Step 5: detuning window

For positive integer `k`, take `M=1`, `N=k^2`, so that `a=k^{-2}`, and set
`g=1+c/k`.  Then

\[
\Omega^2=\frac{c^2+4+4c/k}{k^2}.
\]

Substitution in the exact maximum and `t_peak=pi/Omega` gives the two limits.
This also shows why fixed nonzero detuning fails as `a` tends to zero.

### Step 6: graph normalization

The complete-graph adjacency satisfies `A(K_N)=J-I=N|s><s|-I`.
Consequently

\[
-\gamma A(K_N)-P_W=H_{\gamma N}+\gamma I.
\]

Exponentiating the commuting scalar term proves global-phase equivalence and
identical probabilities.

### Step 7: boundary faces

If `M=0`, then `P_W=0`; the eigenvalues are `-g` once and `0` with
multiplicity `N-1`, while success is zero.  If `M=N`, then `P_W=I`; the
eigenvalues are `-(g+1)` once and `-1` with multiplicity `N-1`, while success
is one.  These formulas include `N=1`.  If `g=0` and `0<M<N`, then
`H=-P_W`, with eigenvalues `-1` of multiplicity `M` and `0` of multiplicity
`N-M`; because no marked/unmarked mixing occurs, success remains `a`.

Thus every claim follows. ∎

## Open risks

- The source paper owns the continuous-time analog search principle.  This
  package must describe the arbitrary-`M`, arbitrary-detuning closure as a
  source-local reconstruction, not as a literature-priority claim.
- The source Hamiltonian is naturally quantum, but it has no target arithmetic
  payload.  `A4_NATURAL_QUANTIZATION` cannot be promoted to Route-B readiness.
