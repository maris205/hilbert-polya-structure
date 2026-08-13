# Paper06 binary Parry / symbolic-Archimedean experiment

## Scope lock

- Primary family: symbolic dynamics only.
- Source candidate: SD-C07 tensor-atom shift from Papers 04--05; the frozen
  binary Parry extension evaluated here is SD-C08.
- No Riemann-zero data are loaded or scored.
- Arithmetic atoms are recovered as nonunit indecomposables of the finite
  multiplication table; no prime list is read.
- This is the falsification record supporting the scoped SD-C08 promotion.
  It is not a Route-B object.

## Unified K2 hypothesis

Let

\[
K_2=J_2/2=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

Test whether this one symbolic rank-one Bernoulli block can simultaneously
carry:

1. the prime-power trace ledger through
   \(A_s=\bigoplus_p p^{-s}K_2\);
2. a centered chiral block
   \(B_p(s)=\left(\begin{smallmatrix}0&p^{-s}\\
   p^{-(1-s)}&0\end{smallmatrix}\right)\);
3. an archimedean Gamma skeleton through the absolute Mellin transform of
   odd-length K2 Birkhoff sums
   \(Y_N=S_N/\sqrt{2\pi N}\).

The three identities to verify before interpretation are

\[
\operatorname{tr}K_2^r=1,
\qquad
\det(I_2-p^{-s}K_2)=1-p^{-s},
\qquad
B_p(s)^2=p^{-1}I_2.
\]

The Euler and fluctuation tests are also joined at finite cutoff by the
tilted cyclic representative

\[
H_{\rm cyc}(u)=K_2\operatorname{diag}(e^{-iu},e^{iu}),\qquad
\operatorname{tr}H_{\rm cyc}(u)^N=\cos(u)^N.
\]

Thus \(H_{\rm cyc}(0)=K_2\) gives the stationary Euler power trace, while
\(u=t/\sqrt N\) gives the exact characteristic function of the standardized
sign Birkhoff sum. This is a genuine same-trace identity; the later Mellin
transform and the atom Fredholm determinant remain different transforms.

The manuscript uses the symmetric representative
\[
H_{\rm sym}(z)=e^{zQ/2}K_2e^{zQ/2},
\qquad Q=\operatorname{diag}(-1,1).
\]
With \(z=iu\), up to the frozen sign convention, \(H_{\rm sym}\) and
\(H_{\rm cyc}\) are cyclic/similar representatives of the same tilted
transfer. They have identical power traces and characteristic determinants;
they are not separate candidate objects.

On \(s=1/2+it\), the diagonal conjugator

\[
D_p(t)=\operatorname{diag}(p^{-it/2},p^{it/2})
\]

is unitary and

\[
B_p(1/2+it)=D_p(t)\frac{X}{\sqrt p}D_p(t)^{-1},
\qquad
X=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Thus the chiral spectrum is exactly \(\{\pm p^{-1/2}\}\); its \(t\)-phase
is a gauge, not a spectral parameter.

## Frozen numerical protocol

### Prime/K2 blocks

- recovered tensor atoms: all atoms up to 512 (97 atoms);
- complex test point: \(s=1/2+7i\);
- powers: \(r=1,\ldots,12\);
- report determinant, square, gauge, eigenvalue, and unitarity residuals;
- controls:
  - \(K_q=J_q/q\), \(q=3,4\);
  - biased rank-one K2 with stationary vector \((0.3,0.7)\);
  - reversible K2 with nontrivial eigenvalue \(\lambda=0.4\).

### K2 Gamma sector

- odd cutoffs \(N=31,127,511,2047,8191,32767\);
- exact binomial probabilities;
- grid
  \(\Re s\in\{0.25,0.5,1,1.5,2,3\}\),
  \(\Im s\in\{0,2,6,12\}\);
- target

  \[
  M(s)=\pi^{-s/2}\Gamma(s/2),\qquad \Re s>0;
  \]

- exact characteristic function
  \(\phi_N(t)=\cos(t/\sqrt N)^N\), tested at
  \(t=0.5,1,2,4\);
- local CLT scored on \(|z|\le3\).

Controls are biased K2 after centering/variance normalization, a
noncanonical scalar observable on uniform F3, uniform \(K_3,K_4\) represented
by the vertices of a centered regular simplex in dimensions two and three,
and 64 random binary relabel/scale transformations.  The K3/K4 statistic is
the radial norm of the Birkhoff sum, not a selected scalar projection.

### Parry/Hellinger auxiliary branch

For inventory \(\mathcal A\), solve

\[
\sum_{a\in\mathcal A}a^{-h}=1,
\qquad g_a=a^{-h}.
\]

Then test \(g_a^s g_a^{1-s}=g_a\), critical-axis conjugacy, chiral spectrum,
Schatten thresholds, and the trace term deleted by \(\det_2\). Controls use
shifted atoms, the additive singleton, and 32 matched random inventories.

## Decisive results

### 1. K2 gives the exact Euler ledger, but rank one is the real cause

All K2 block identities pass to binary64 precision:

- max determinant residual: \(4.44\times10^{-16}\);
- max chiral-square residual: \(1.11\times10^{-16}\);
- max unitary gauge residual: \(1.19\times10^{-16}\);
- max chiral eigenvalue residual: \(5.55\times10^{-16}\).

The finite tilted identity
\(\operatorname{tr}H_{\rm cyc}(t/\sqrt N)^N=\cos(t/\sqrt N)^N\) also passes on the
frozen grid to binary64 precision. It makes the two channels evaluations of
one source-locked trace family, although it does not turn their Mellin and
Fredholm outputs into one determinant.

However, uniform K3, uniform K4, and biased rank-one K2 also satisfy
\(\operatorname{tr}K^r=1\) for every tested power. The reversible control
with eigenvalues \(1,0.4\) gives

\[
\operatorname{tr}K^r=1+0.4^r,
\]

and immediately fails: the first eight traces begin
\(1.4,1.16,1.064,1.0256,\ldots\).

**Diagnosis:** the Euler ledger selects rank-one idempotence, not K2 or an
arithmetic half-density. This part **PROVES_TOO_MUCH** across all rank-one
finite Bernoulli kernels.

### 2. The chiral center is exact but spectrally sterile

The centered block has exactly \(s\)-independent eigenvalues
\(\pm p^{-1/2}\), and all critical-axis \(t\)-dependence is removed by a
unitary gauge. It therefore cannot create a vertical spectral divisor.

**Diagnosis:** exact \(s\leftrightarrow1-s\) centering alone is not enough;
the current chiral doubling is **PHASE_GAUGE_TRIVIAL**. The finite experiment
checks the frozen block-preserving instance; the analytic identity
\(A_t=G^{it}A_0\) proves the same no-motion result for every bounded \(K\) in
the one-sided ansatz, including \([G,K]\ne0\).

### 3. K2 yields the real Archimedean Gamma factor on \(\Re s>0\);
dimension controls partially select it, but scalar CLT universality remains

For a fair K2 chain,

\[
M_N(s)=2^{-N}\sum_{k=0}^{N}{N\choose k}
\left|\frac{2k-N}{\sqrt{2\pi N}}\right|^{s-1}
\longrightarrow \pi^{-s/2}\Gamma(s/2)
\]

pointwise for \(\Re s>0\). Across the frozen 24-point complex grid, the
median relative error falls from 2.269 at \(N=31\) to 0.04576 at
\(N=32767\), an improvement factor 49.6. The extreme high-frequency,
negative-moment corner \(s=0.25+12i\) converges extremely slowly, so the
maximum relative error remains \(1.56\times10^4\); this is reported rather
than hidden.

The characteristic-function error on \(|t|\le4\) falls from
\(5.90\times10^{-3}\) to \(5.51\times10^{-6}\). The max local-CLT relative
error on \(|z|\le3\) falls from 0.0342 to \(7.62\times10^{-5}\).

But the controls also approach the same target after centering and variance
normalization:

- biased K2 median grid error: 0.03573 at \(N=32767\);
- noncanonical F3 median error: 0.01598 at \(N=511\);
- every nonconstant binary relabel/scale is exactly identical after
  standardization.

The canonical radial Kq controls behave differently. Put the q states at
the vertices of a centered unit regular simplex in
\(d=q-1\) dimensions. Their radial limiting Mellin transform is

\[
 M_d(s)=(\pi d)^{-(s-1)/2}
 \frac{\Gamma((d+s-1)/2)}{\Gamma(d/2)}.
\]

Only \(d=1\), hence q=2, gives
\(\pi^{-s/2}\Gamma(s/2)\). At the last cutoffs:

- K3 radial median error against the K2 target is 1.5793, but only 0.00996
  against its native two-dimensional target;
- K4 radial median error against the K2 target is 2.5506, but only 0.01009
  against its native three-dimensional target.

Thus the exact Gamma shape does select a one-dimensional binary radial
sector among the canonical Kq controls. It still does not select fair K2
against biased binary rank-one kernels or against arbitrary scalar
observables in other alphabets.

**Diagnosis:** the positive-real Gamma skeleton is real and useful. Its
dimension shift rejects canonical radial K3/K4, while one-dimensional CLT
mechanisms still **PROVE_TOO_MUCH**. Finite symbolic moments do not provide
the meromorphic continuation of Gamma.

### 4. Global atom-inventory Parry/Hellinger normalization proves too much
and is not the SD-C08 binary fiber

For the infinite recovered prime inventory, the pressure root is

\[
h=1.3994333287263303,
\qquad \sum_p p^{-h}=1.
\]

The first common integer Schatten class for \(U_s\) and \(U_{1-s}\) is
\(q=2\), on

\[
0.35728747<\Re s<0.64271253.
\]

At the 512 cutoff \(\|U_{1/2}\|_{S_2}^2=1\), while its S1 partial norm is
5.01376 and grows with cutoff. A paired \(\det_2\) reaches the critical
line, but deletes the \(r=1\) trace term; at \(s=1/2+5i\) the deleted finite
term is \(-0.6569601903\).

All shifted/random positive inventories satisfy the Hellinger product,
conjugacy, and chiral identities to machine precision. More importantly,
the SD-C07 atom-loop base has identity adjacency, hence no canonical
nontrivial Parry probability across its atom inventory. Adding full mixing
there would manufacture the measure while also creating mixed temporal
cycles forbidden by the exact prime-power ledger. SD-C08 instead uses the
canonical Parry kernel internal to the distinguished finite full shift
\(F_2\); the two constructions are not identified.

## Route-A / Route-B consequence

The experiments support three exact same-family lemmas and the scoped
promotion from SD-C07 to SD-C08:

1. rank-one K2 reproduces the SD-C07 Euler trace ledger, and the tilted
   family \(H(u)\) gives both that ledger and the binary characteristic
   function as cyclic traces;
2. K2 fluctuations generate \(\pi^{-s/2}\Gamma(s/2)\) on \(\Re s>0\);
3. the naive chiral half-density doubling is gauge-trivial.

The unique least-entropy tensor atom \(F_2\), its canonical Parry kernel, and
the one-dimensional sign sector provide the source-internal selection used
by SD-C08. The experiment does **not** establish that the fluctuation Mellin
transform and prime Fredholm determinant are one operator determinant.
Their product is credited only as a same-source Mellin--Fredholm
factorization. Route B remains locked.

Stage verdict:

```text
SD-C08
GO_A3_ARCHIMEDEAN_FACTOR
STOP_GLOBAL_COMPLETION
ROUTE_B_LOCKED
```

The next falsification gate is a single determinant or trace formula whose
fixed, non-asymptotic object contains both transforms and retains the exact
prime-power ledger. It must distinguish the canonical binary sector from
biased one-dimensional controls and must not create uncancelled mixed atom
cycles.

## Reproduction

```bash
python code/symbolic_archimedean_experiment.py --out results
python code/test_symbolic_archimedean_experiment.py
```

Artifacts:

- `code/symbolic_archimedean_experiment.py`: executable experiment;
- `code/test_symbolic_archimedean_experiment.py`: six deterministic tests;
- `results/summary.json`: frozen headline result;
- `results/k2_prime_blocks.csv`: all 97 atom-block residuals;
- `results/mellin_grid.csv`: full complex-grid ledger;
- `results/mellin_cutoffs.csv`: cutoff summaries;
- `results/characteristic_local_clt.csv`: CLT diagnostics;
- `results/parry_cutoffs.csv`, `parry_controls.csv`: auxiliary branch.
