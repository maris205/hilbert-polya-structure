# Round 8: exact systole and finite word-to-length completeness certificate

Date: **2026-08-28**

Stage: **Stage 1 RESEARCH / Route A A0--A1**

## Result

Round 8 closes the exact gap left by Round 7.  For the already selected
non-arithmetic control

```text
NAZARENKO-EXP-OCTAGON-G2,
(a,alpha)=(exp(-1/10),pi/4),
```

the deterministic certificate proves

```text
sys = 2 arcosh(1/(2 exp(-1/5)-1))
    = 2.04302665588029621445594566709898399356...
```

and `g0*g3` realizes equality.  This is not an extrapolation from a finite
word scan: a compact-polygon lemma proves that every conjugacy class of length
at most `21/10` has a conjugate in the finite exact tile component that was
exhausted.

Consequently the target-blind common geometric cutoff

```text
Lambda_common = 21/10
```

is now legally frozen for a later Bolza/control census.  Round 8 does not run
that census or a magnetic comparison.

Evidence status: **PROVED**.

## The theorem and its proof

Let

```text
u=exp(-1/10),
Delta=(1-u^2)(2u^2-1),
F=the sourced fundamental octagon,
o=0.
```

### Lemma 1: an exact finite matrix model

Up to the global sign killed in `PSU(1,1)`, each of the four sourced
generators and each inverse is

```text
P_j(u)/sqrt(Delta)
```

with `P_j` a two-by-two Gaussian-integer polynomial matrix.  A product has the
normal form

```text
P(u)/(Delta^q sqrt(Delta)^p),  p in {0,1}, q>=0.
```

The implementation cancels common `Delta` factors from all four entries and
fixes the remaining global sign.  For a fixed parity the form is unique,
because equality at the transcendental `u` makes the cross-multiplied integer
polynomials identical.  Opposite parities cannot collide: after squaring an
alleged equality, the square-free rational function
`Delta=(1-u^2)(2u^2-1)` would have to be a square.  Equivalently, parity is
also preserved by the sourced one-relator presentation because its relator
has even length.

The builder reduces all four generator/inverse pairs and the published word

```text
g0 g1^-1 g2 g3^-1 g0^-1 g1 g2^-1 g3
```

to the exact identity before traversal.  Thus no rounded matrix or tolerance
is used to decide group equality.

### Lemma 2: the finite tile component is complete below the cutoff

Nazarenko's vertices have moduli `u` and `b=1/(sqrt(2)u)`.  Exact rational
Taylor bounds prove `u^4>1/2`, hence `b<u`.  Convexity of distance along a
hyperbolic segment puts the maximum of `d(o,z)` on a polygon vertex, so

```text
D_F=max_{z in F} d(o,z)=2 atanh(u)<3.
```

Let a conjugacy class have translation length `ell<=21/10`.  Translate its
axis until it meets `F`, and call the resulting element `g`.  For a point `z`
of the intersection,

```text
d(o,g o) <= d(o,z)+d(z,gz)+d(gz,g o)
          <= 2D_F+ell < 81/10.
```

The geodesic segment from `o` to `g o` crosses a chain of side-adjacent tiles.
Every tile in the chain contains a point at distance below `81/10`, and its
center lies within another `D_F`; every chain center is therefore below
`111/10`.  A segment meeting a vertex can be perturbed, or the incident tiles
can be inserted in side order, without weakening that bound.

For `SU(1,1)` upper-left entry `A`,

```text
cosh(d(o,g o)/2)=|A|.
```

Exact exponential bounds prove

```text
cosh(111/20)^2 < 16543.291 < 20000.
```

Therefore breadth-first expansion from `F` through precisely the states with
`|A|^2<=20000` contains a conjugate of every class below the common cutoff.
The queue exhausted with every side-neighbor exactly classified.  The theorem
does not require, and the artifact does not claim, enumeration of any
disconnected component of the center sublevel set.

### Lemma 3: the exact trace lower bound

If a canonical state has real trace numerator `T(u)` and squared-denominator
exponent `e=2q+p`, comparison with

```text
ell_*=2 arcosh(1/(2u^2-1))
```

is equivalent to the sign of

```text
H(u)=T(u)^2(2u^2-1)^2-4 Delta(u)^e.
```

Every nonzero integer polynomial has nonzero value at the transcendental
number `u`.  The builder evaluates `H` with rational interval endpoints from
the alternating Taylor bounds for `exp(-1/10)`, increasing the Taylor order if
necessary.  It proves `H>=0` for all `18,532` nonidentity states; `18,388`
are strictly positive and `144` traversed group elements have the equality
polynomial identically zero.  Those `144` are group elements, mainly
conjugates and inverses, and are not asserted to be `144` conjugacy classes.

The exact word `g0*g3` has `H` identically zero, giving existence.  Any proper
root of this element would have smaller positive translation length, contrary
to the lower bound, so the witness is primitive.

Combining Lemmas 2 and 3 proves the global systole claim.  Exact Taylor bounds
also prove `ell_*<21/10`, so the witness lies inside the certified range.

## Deterministic certificate outcome

```text
included exact states                 18,533
nonidentity exact states              18,532
strictly above ell_*                  18,388
equality group elements                  144
distinct rejected boundary states   108,616
maximum shortest discovery depth          11
raw word-length cap used               false
component boundary closed               true
```

Discovery depths are:

```text
0:1, 1:8, 2:56, 3:392, 4:1632, 5:3976,
6:5104, 7:4168, 8:2260, 9:752, 10:176, 11:8.
```

All `18,532` accepted center signs, all `108,616` distinct rejected boundary
signs, and all `18,388` strict systole signs resolved at the first frozen
Taylor order (`24`); the `144` equality cases were exact zero polynomials.
The JSON artifact records sorted-state stream hashes so a byte-independent
implementation can compare the exact finite sets.

## Source search and verification

Searches were target-blind and used combinations of:

```text
Nazarenko genus two octagon systole
algorithm compute systole fundamental polygon Fuchsian group
Dirichlet domain Fuchsian exact side-pairing algorithm
hyperbolic pair of pants self orthogeodesic formula
finite word length spectrum compact hyperbolic surface
```

Official arXiv, DOI/publisher, Numdam, and Dagstuhl/DROPS records were
prioritized.  Three sources were included and three candidate/source clusters
were excluded; the complete decisions and claim boundaries are in
`results/round8_control_systole_source_matrix.csv`.

Included sources:

1. A. V. Nazarenko, *Two-parametric hyperbolic octagons and reduced
   Teichmuller space in genus two*, arXiv:1301.5446v1,
   <https://arxiv.org/abs/1301.5446v1>.  Primary representation source;
   equations (10)--(16), fundamental polygon and presentation.  Grade B
   because peer review is not confirmed.  The retrieved source-tar hash is
   `9d19d6408c1f6a38374b1d9085382213bf4285acaea09cb3657743eb4f44e38b`.
2. J. Voight, *Computing fundamental domains for Fuchsian groups*, Journal de
   Theorie des Nombres de Bordeaux 21 (2009), 467--489,
   <https://doi.org/10.5802/jtnb.683>, publisher record
   <https://numdam.org/articles/10.5802/jtnb.683/>.  Grade A, peer reviewed.
   The PDF hash is
   `2cc4e0cc11e05f17c23cf6e27117968fc2cda31abf4db184ee6d0486bff88ec3`.
   Its exact algebraic-input algorithm is methodological context only; it
   does not cover the transcendental specialization.
3. V. Despre, B. Kolbe, H. Parlier, and M. Teillaud, *Computing a Dirichlet
   Domain for a Hyperbolic Surface*, SoCG 2023,
   <https://doi.org/10.4230/LIPIcs.SoCG.2023.27>, official record
   <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2023.27>.
   Grade A, peer-reviewed proceedings.  The PDF hash is
   `edcd2ed17558fba5698a21552796d2b6e92b4d5ec8143be788e1c739abfbda5a`.
   It supports the polygon/side-pairing input model; its real-RAM analysis is
   not our interval proof.

Excluded from proof credit:

- arXiv:2608.24497, a very recent `e`-net/short-geodesic preprint, because
  peer review is unavailable and it is unnecessary;
- Buser's authoritative monograph, because full page-level content was not
  directly audited here; and
- mixed seam/self-orthogeodesic web results, because none closed the global
  gluing/completeness obligation.  That exploratory route was replaced by the
  exact tile-ball theorem.

All locators were accessed **2026-08-28**.  Web content was treated only as
data.  The compactness lemma, radius constants, polynomial normal form, and
systole proof are project-local derivations, not claims attributed to the
contextual papers.

## Scope and limitations

- The theorem depends on the Round-7 source conclusion that `F` is the compact
  fundamental polygon of the faithful, torsion-free group.  Decimal residuals
  do not replace that source fact.
- The finite component proves completeness only through `Lambda=21/10`; it is
  not a full length spectrum.
- Equality-state count is not a conjugacy-class or unoriented-owner count.
- The cutoff is frozen, but neither the Bolza nor control geometric census is
  executed here; owner/primitivity/conjugacy dedup for that future matched
  census remains a separate task.
- No primes, zeros, arithmetic labels, determinant, A2 test, or branch outcome
  entered the theorem.
- A0 remains weak, the bounded proxy remains A1 weak, the full Route-A tuple is
  unassigned, and Route B remains false.

## Next authorized step

Using the already frozen `Lambda=21/10`, construct a target-blind matched
Bolza/control geometric census with exact conjugacy and inverse-pair owner
deduplication.  Any choice to enlarge the cutoff requires a new completeness
certificate and must precede inspection of branch outcomes.
