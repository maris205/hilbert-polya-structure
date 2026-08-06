# HCS-C02B complex-polydisc results

## Outcome

The complex sequence-space orbit-coordinate bridge closes, in the precise
restricted sense of the signed-square-root solver.  For every admissible
finite cyclic or bi-infinite sign sequence, the explicit source-locked
polydisc

\[
 K_\varepsilon=
 \prod_i\overline D\left(\varepsilon_i\frac{23}{48},\frac7{48}\right)
\]

is a strict invariant domain for the principal-branch map

\[
 (T_\varepsilon q)_i
 =\varepsilon_i\sqrt{\frac{1-q_{i-1}-q_{i+1}}6}.
\]

The map is holomorphic on a neighborhood of this polydisc and contracts in
the sup norm by at most

\[
 \frac2{\sqrt{17}}\approx0.48507125.
\]

This is a theorem-level positive result, not a fitted-domain observation.

## Certified geometry

The no-two-positive-neighbors rule produces exactly two radicand disks:

| Neighbor case | Radicand disk | Left real edge |
|---|---|---:|
| one positive, one negative | \(\overline D(1/6,7/144)\) | \(17/144\) |
| two negative | \(\overline D(47/144,7/144)\) | \(5/18\) |

Both lie strictly inside the right half-plane, which supplies a common
principal square-root branch.

The square-root images lie inside
\(D(23/48,7/48)\) with the explicit lower margins

\[
 \mu_{\rm mix}=\frac{\sqrt{17}-4}{12}
 \approx0.0102588021,
\]

\[
 \mu_{--}=\frac58+\frac{\sqrt{10}-\sqrt{47}}6
 \approx0.0094371766.
\]

The producer encloses all required radicals by exact 192-bit dyadic
intervals. Its minimum certified margin is \(0.0094371766\), and its certified
upper contraction bound is \(0.4850712501<1\).

## Short-cycle chronology

Cyclic sign words through length 12 were exhaustively checked. In particular:

- at length 1, only the negative word is admissible, and its two neighbor
  occurrences both refer to that same coordinate;
- at length 2, only the double-negative word is admissible, and each
  coordinate sees the other coordinate twice;
- both derivative contributions are retained, so the bound remains
  \(2/\sqrt{17}\), not \(1/\sqrt{17}\).

The independent checker reproduces all cyclic counts and reports
`all_checks_pass=true`. Boundary sampling at 16,384 points per radicand disk
is included only as a regression diagnostic; the proof relies on exact
inequalities, not sampling.

## Research gate

| Gate | Result |
|---|---|
| complex signed-root self-map | `PASS` |
| complex sequence-space bridge | `PASS_FOR_SIGNED_ROOT_POLYDISC_ONLY` |
| finite-dimensional holomorphic Markov branches | `NOT_ESTABLISHED` |
| finite Schottky generators | `NOT_ESTABLISHED` |
| nuclearity | `NOT_ESTABLISHED` |
| Fredholm determinant | `NOT_ESTABLISHED` |
| Route-A A2 | `DO_NOT_PROMOTE` |

The result complexifies the genuine implicit Hénon orbit solver. It does not
complexify the symbolic alphabet into an analytic variable, nor does it turn
the itinerary-dependent dynamics into finitely many constant Möbius maps.

## Next theorem

First audit these statements against Rugh's pinning coordinates and the
iterated analytic pinning maps of Baladi--Pujals--Sambarino.  Continue only if
explicit \(H_6\) constants, a trace-Jacobian identity, or another quantitative
certificate remains genuinely new.

The sequence-polydisc problem is closed; finite-dimensional pinning/Markov
domains remain open.  The immediate lemma is deliberately smaller than an
operator construction:

> For every admissible finite sign block with two endpoint variables in
> frozen complex disks, construct the unique holomorphic internal solution;
> prove explicit exponential boundary-influence bounds and consistency under
> block extension and chronological two-coordinate gluing; then prove that
> endpoint-diagonal closure agrees with the already-established cyclic
> solution and recovers its derivative/monodromy bookkeeping.

The endpoint fixed-point statement is expected to be close to a
parameter-dependent consequence of the present contraction theorem.  The
paper-level gate is therefore stronger: prove the exact crossed-map identity,
two-coordinate interface composition, cyclic-diagonal equivalence, monodromy
recovery, and a frozen flat-trace weight.  Graph-directed convergence,
nuclearity, and a periodic-orbit Fredholm determinant are later gates.

## Reproduction

From the repository root:

```bash
python next_paper_henon_candidate_search/code/c02b_complex_polydisc.py
python next_paper_henon_candidate_search/code/c02b_complex_polydisc_check.py
```

Artifacts:

- `complex_polydisc.json`: exact/dyadic certificates and cyclic audit;
- `independent_check.json`: independent algebraic and chronology check;
- `paper/c02b_complex_polydisc_theorem.md`: theorem and proof.

Final SHA-256 values for the executable certificate package:

```text
501759df9acbdebb2a29945f04569deb1a9029642c592a7d7df5379be36d4882  c02b_complex_polydisc.py
e39de5e79de39bd12c7cac36dd8d745af5d688d7ba4ed685272f02727c3a8dd8  c02b_complex_polydisc_check.py
4f5ddb72618250a9fb525e2819b93d360bfe46ed37cab5745eb9d0cebd756f59  complex_polydisc.json
3bd69c9279c6bf4a2971de1d59f706b654e9abd1e44b4eb6873cc1ad71fabd8d  independent_check.json
```
