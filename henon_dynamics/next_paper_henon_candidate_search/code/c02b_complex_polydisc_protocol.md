# HCS-C02B frozen complex-polydisc protocol

## Frozen question

Does the exact R059 signed-square-root map admit a canonical complex
extension on the polydiscs obtained by complexifying the real sign intervals
without changing their centers or radii?

For an admissible sign sequence $\varepsilon_i\in\{-1,+1\}$, define

\[
 (T_\varepsilon q)_i
 =\varepsilon_i\sqrt{\frac{1-q_{i-1}-q_{i+1}}6},
\]

where the square root must be the principal analytic branch.  Admissibility
means that $\varepsilon_{i-1}$ and $\varepsilon_{i+1}$ are not both positive,
with cyclic indices counted with multiplicity for a finite cyclic word.

## Frozen domains and constants

No radius is optimized:

\[
 c=\frac{23}{48},\qquad \rho=\frac7{48},\qquad
 K_\varepsilon=\prod_i
 \overline D(\varepsilon_i c,\rho).
\]

These disks are the canonical complexifications of
$X_-=[-5/8,-1/3]$ and $X_+=[1/3,5/8]$.

## Source lock

- `docs/related_programs/henon_weighted_zeta/research/refine-logs/R059_SYMBOLIC_CONTRACTION_PROOF.md`
  (`b2d2c46c198e20b40b042cf5bc02cbdcfe9835c1a7c193cd88476eebc3e3f315`);
- `docs/related_programs/henon_weighted_zeta/paper/sections/B_contraction_proof.tex`
  (`0ef59712ee231aac3023d15d3ec857cbedfea884b18be7ec1ac30459757e28a8`).

No target spectrum, primes, fitted Möbius maps, or optimized complex domain
may be read or introduced.

## Prespecified claims

1. The neighbor radicand lies in exactly one of the enclosing disks

   \[
   \overline D(1/6,7/144),\qquad
   \overline D(47/144,7/144),
   \]

   for mixed and two-negative neighbors respectively.
2. Both radicand disks lie strictly in the right half-plane, so the principal
   square root is analytic on a common neighborhood.
3. Their square-root images lie strictly in
   $\overline D(c,\rho)$, with explicit positive radical margins.
4. $T_\varepsilon$ is a sup-norm contraction with constant at most
   $2/\sqrt{17}<1$.
5. Cyclic lengths one and two count the two chronological neighbor
   occurrences even when they refer to the same coordinate; no occurrence
   may be silently dropped.

## Gate semantics

A successful run closes only `COMPLEX_SIGNED_ROOT_SELF_MAP`.  It does not
establish finite Schottky generators, a finite-dimensional holomorphic
Markov branch system, operator nuclearity, a Fredholm determinant, Route-A
A2, or any Hilbert--Pólya statement.

## Reproduction

From the repository root:

```bash
python next_paper_henon_candidate_search/code/c02b_complex_polydisc.py
python next_paper_henon_candidate_search/code/c02b_complex_polydisc_check.py
```

