# HCS-P54 results

## Unconditional analytic result

For every primitive orbit of the certified H6 survivor,

\[
\mathcal H_\gamma=\ell_\gamma+E_\gamma,
\qquad E_\gamma\ge0.
\]

The physical component of the P53 Mahler amplitude has a meromorphic germ
at the entropy-one pressure point:

\[
\mathcal A_{\rm phys}(s)
=\frac{3}{\pi^2h_*}\frac1{s-1}+G_{\rm phys}(s),
\]

where \(G_{\rm phys}\) is holomorphic near one and

\[
1.093445200412297389\ldots
<\frac3{\pi^2h_*}<
1.093472735186032499\ldots.
\]

The proof extracts the first repetition from the logarithmic derivative of
the normalized suspension zeta; the repetitions \(k\ge2\) form a normally
convergent tail on \(\Re s>1/2\).

## Exact Galois witnesses

| orbit | physical length \(\ell_\gamma\) | Mahler height \(\mathcal H_\gamma\) | excess \(E_\gamma\) |
|---|---:|---:|---:|
| period 1 | 1.9673466290942102 | 3.0501161905168336 | 1.0827695614226234 |
| period 3 | 4.8820992058291742 | 8.9056092910640769 | 4.0235100852349027 |
| period 4 | 6.3595708753997577 | 6.3595708753997577 | 0 |

The exact excesses are
\(E_1=\operatorname{arcosh}(\sqrt7-1)\),
\(E_3=\operatorname{arcosh}(21\sqrt5-19)\), and \(E_4=0\).
The period-four row forces a hypothetical scalar roof factor to be one;
period one then contradicts it.  Thus no constant pressure retuning modulo a
coboundary realizes the full Mahler height.

## Pressure gate

Let \(\sigma_{\rm Gal}\) be the absolute-convergence abscissa of the positive
excess series.  The inherited all-orbit majorant proves
\(\sigma_{\rm Gal}<3.125207\), and the defining full series has abscissa
\(\max\{1,\sigma_{\rm Gal}\}\).  The three cases
\(\sigma_{\rm Gal}<1\), \(=1\), and \(>1\) respectively give physical-pole
inheritance, an unresolved critical boundary, and loss of convergence before
the pressure line.  The last statement concerns the defining series and does
not rule out continuation by another theorem.

## Conditional completion

If one real Hölder observable \(\psi\) satisfies
\(E_\gamma=S_{m(\gamma)}\psi\) on every primitive orbit, then the full
Mahler amplitude has a simple-pole germ at one with residue

\[
\frac3{\pi^2}
\frac{\int(\tau+\psi)\,d\mu}
     {\int h_*\tau\,d\mu}.
\]

This statement is a `CONDITIONAL_THEOREM`; the Hölder realization is `OPEN`.

## Claim status

- physical pressure pole: **PROVED**;
- scalar-roof completion: **REFUTED**;
- excess-abscissa trichotomy: **PROVED**;
- Hölder-excess completion: **CONDITIONAL_THEOREM**;
- full Galois-weighted determinant: **OPEN**;
- rational-prime trace and Hilbert--Pólya operator: **OPEN**.
