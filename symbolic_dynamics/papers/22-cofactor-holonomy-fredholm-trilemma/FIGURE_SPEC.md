# Figure Specification — SD-C24

All manuscript figures are pure TikZ vector sources.  They use no raster
assets, target-zero data, fitted coordinates, or numerical interpolation.

## Figure 1 — cocycle and extension anatomy

**File:** `figures/cofactor_extension_anatomy.tex`  
**Placement:** positive-holonomy and gauge section  
**Width:** approximately \(0.96\) text width

### Content

Three linked panels show:

1. a base edge \(n\to d\) with
   \(n+1=dq\) and voltage \(q\);
2. its regular lift
   \((n,g)\to(d,qg)\), with a closed base path ending at
   \((n,Qg)\ne(n,g)\);
3. character fibers \(L_{s,\chi}\) and Haar extraction of the
   \(Q=m\) connected coefficient.

The lower annotation must distinguish:

- ordinary lift: infinite deck multiplicity, noncompact;
- semifinite trace: \(L^1\) for \(\Re s>1/2\);
- neutral trace: every periodic coefficient vanishes.

### Caption

The factor witness on a successor–divisor edge supplies the voltage
\(q=(n+1)/d\).  A closed base path accumulates
\(Q=\prod q=\prod(1+1/n)>1\), so it never closes in the regular deck
coordinate.  Character fibers retain every base cycle and permit exact
Fourier extraction of non-neutral connected coefficients.  Ordinary
noncompactness of the lift and semifinite \(L^1\)-integrability are separate
operator statements.

### Accessibility

Solid, dashed, and dotted edges distinguish the base, deck, and Fourier
maps without color.  Text labels carry every semantic distinction.  The
palette is colorblind-safe and remains legible in grayscale.

## Figure 2 — canonical spine and Fredholm trilemma

**File:** `figures/canonical_spine_trilemma.tex`  
**Placement:** exact-class or Fredholm-trilemma section  
**Width:** approximately \(0.98\) text width

### Content

The upper panel depicts

\[
 C_k:k\to k+1\to\cdots\to2k-1\to k,
\]

with \(q=1\) on the successor run and \(q=2\) on the closing edge.  It
labels

\[
 \ell(C_k)=k,
 \qquad
 Q(C_k)=2,
 \qquad
 M_k=(2k-1)!/(k-1)!.
\]

The lower panel branches into:

1. pure cofactor \(s=0\): desired \(2^{-u}\), noncompact successor spine;
2. endpoint regularized: honest \(\mathcal S_1\), factorial
   \(M_k^{-2s}\);
3. unitary character: common phase \(\chi(2)\), every \(C_k\) retained.

### Caption

Holonomy two forces one cofactor-two closing edge and otherwise only
cofactor-one successors, hence exactly the canonical orbit \(C_k\) at every
length \(k\ge2\).  The three natural analytic choices expose the Fredholm
trilemma: pure cofactor weights lose compactness, endpoint weights restore an
honest determinant through factorial damping, and unitary characters change
only a common phase.

### Accessibility

The three outcomes use distinct node shapes and border styles in addition to
color.  The stop conclusion is textually labeled; it is not encoded only by
red.

## Figure exclusions

- No near-boundary finite prefix is plotted as evidence for the exact
  \(\mathcal S_1\) threshold.
- No Riemann zero, critical-line plot, or spectral fit is shown.
- No diagram may depict the neutral determinant \(1\) as a successful Euler
  factor.
- No ordinary Fredholm symbol is attached to the regular lifted operator.
