# LITERATURE AUDIT — Paper 16

## Search boundary

The search was restricted to sources needed for SD-C18 inside Symbolic
Dynamics: symbolic zeta functions, equivariant dynamical zeta functions,
Burnside rings, combinatorial species and cycle indices, necklace/Witt rings,
\(\lambda\)- and Adams operations, twisted periodic-orbit factors, symmetric
group stability, infinite symmetric-group characters, and infinite Fredholm
determinants.  No general Hilbert--Pólya search and no independent geometric
or operator-family program was opened.

Publisher/Crossref metadata and DOI resolution were checked on 2026-08-14.
Only primary articles or primary monographs cited by the manuscript are
included in `references.bib`.

## Closest collisions

### 1. Burnside rings and species

Labelle and Yeh identify Burnside-ring data with virtual combinatorial
species and relate molecular cycle indices to permutation-group cycle
polynomials.  This is the closest formal collision with a Burnside/species
lift of the SD-C18 primitive ledger.

- Jacques Labelle and Yeong-Nan Yeh, “The relation between Burnside rings and
  combinatorial species,” *Journal of Combinatorial Theory, Series A* 50(2)
  (1989), 269--284.
- DOI: <https://doi.org/10.1016/0097-3165(89)90019-8>

**Boundary:** Burnside/species/cycle-index packaging is classical and is not
claimed as a contribution.

### 2. Equivariant dynamical zeta functions

Gusein-Zade, Luengo, and Melle-Hernández construct a Burnside-ring-valued
zeta function from equivariant Lefschetz data for a genuinely
\(G\)-equivariant transformation.  Their hypothesis clarifies the decisive
SD-C18 boundary: a character zeta requires a group action commuting with one
fixed dynamical map, not merely a relabeling that moves between differently
weighted maps.

- S. M. Gusein-Zade, I. Luengo, and A. Melle-Hernández, “On an Equivariant
  Version of the Zeta Function of a Transformation,” *Arnold Mathematical
  Journal* 1(2) (2015), 127--140.
- DOI: <https://doi.org/10.1007/s40598-015-0012-8>

**Boundary:** equivariant/Burnside-valued zeta functions are prior art.  The
paper contributes only the fixed-fiber audit of the specific tensor-subset
shift.

### 3. Necklace and Witt packaging

Dress and Siebeneicher identify the Burnside ring of the infinite cyclic
group with necklace, \(\lambda\)-ring, and big-Witt structures.  Metropolis
and Rota give the necklace-algebra model of Witt vectors.  These sources are
the closest collision with primitive-cycle Euler transforms and Adams ghost
coordinates.

- Andreas W. M. Dress and Christian Siebeneicher, “The Burnside ring of the
  infinite cyclic group and its relations to the necklace algebra,
  \(\lambda\)-rings, and the universal ring of Witt vectors,” *Advances in
  Mathematics* 78(1) (1989), 1--41.
- DOI: <https://doi.org/10.1016/0001-8708(89)90027-3>
- Nicholas Metropolis and Gian-Carlo Rota, “Witt Vectors and the Algebra of
  Necklaces,” *Advances in Mathematics* 50(2) (1983), 95--125.
- DOI: <https://doi.org/10.1016/0001-8708(83)90035-X>

**Boundary:** necklace/Witt Euler transforms and ghost-coordinate formalism
are not new.

## Foundational source ledger

| Key | Primary contribution used here | Verified locator |
|---|---|---|
| `Joyal1981Species` | species, cycle indices, substitution/plethystic calculus | <https://doi.org/10.1016/0001-8708(81)90052-9> |
| `DressSiebeneicher1988ProfiniteWitt` | Witt--Burnside functors for profinite groups | <https://doi.org/10.1016/0001-8708(88)90052-7> |
| `Siebeneicher1976LambdaBurnside` | \(\lambda\)-ring operations on Burnside rings of finite groups | <https://doi.org/10.1007/BF01181882> |
| `Brun2005WittTambara` | Witt vectors and Tambara-functor compatibility | <https://doi.org/10.1016/j.aim.2004.05.002> |
| `Knutson1973LambdaRings` | symmetric-group representation rings, symmetric functions, and Adams operations | <https://doi.org/10.1007/BFb0069217> |
| `BowenLanford1970ShiftZeta` | zeta functions and determinants for shift transformations | <https://doi.org/10.1090/pspum/014/9985> |
| `Pollicott1994TwistedOrbits` | factorization of Lefschetz zeta functions by twisted periodic orbits | <https://doi.org/10.1007/BF02571937> |
| `ChurchEllenbergFarb2015FI` | finite generation and representation stability for FI-modules | <https://doi.org/10.1215/00127094-3120274> |
| `Thoma1964InfiniteSymmetric` | positive-definite characters of the infinite symmetric group | <https://doi.org/10.1007/BF01114877> |
| `Simon1977InfiniteDeterminants` | trace ideals and infinite determinants of Hilbert-space operators | <https://doi.org/10.1016/0001-8708(77)90057-3> |

## Classical facts used without novelty claim

1. Species and cycle-index calculus are classical.  Functoriality under
   finite-set bijections does not by itself supply a fixed arithmetically
   specialized \(S_\infty\) operator.
2. Burnside marks and permutation linearization are classical.  The
   \(S_3\) residual is a calculation for SD-C18, not a new theory of Burnside
   rings.
3. \(\lambda\)-rings, Adams operations, necklace rings, Witt vectors, and
   Tambara compatibility are classical.  The \(C_2\) sign carrier is an
   application of these operations to the scalar-power firewall.
4. Character-twisted zeta factors are classical when a genuine group
   extension or equivariant map has been fixed.  SD-C18 does not meet that
   hypothesis after distinct prime weights are substituted.
5. Fredholm determinants of trace-class operators and Schatten ideals are
   classical.  The calculation \(D_s\in\mathcal S_q\iff
   q\operatorname{Re}s>1\) is elementary for the frozen diagonal spectrum.
6. FI-module representation stability is classical.  The full subset
   functor is not finitely generated because injections preserve subset size;
   this paper uses the fact only to deny an automatic stable analytic limit.

## Bounded contribution

The defensible project-specific contribution is:

> Apply the classical Burnside/species/Witt formalism to the frozen
> Koszul-subset tensor-atom shift; calculate its first nonzero squarefree
> Burnside and representation residual; and prove, for its canonical
> rank-one and diagonal realizations, that distinct arithmetic weights break
> fixed-fiber label symmetry, symmetry restoration erases nontrivial modes,
> and representation-preserving diagonalization introduces mixed determinant
> factors.

The targeted search located no primary source containing this exact
source-locked combination.  The search was not exhaustive, so the manuscript
makes no “first,” “only,” or universal priority claim.

## Required wording

Use:

- “for SD-C18”;
- “within this model”;
- “for the canonical rank-one and diagonal lifts studied here”;
- “the targeted search located no direct instance.”

Do not claim:

- a new equivariant zeta formalism;
- a new Burnside/species correspondence;
- new cycle-index, plethystic, necklace, Witt, or \(\lambda\)-ring theory;
- a universal obstruction to all equivariant symbolic extensions;
- an analytic \(S_\infty\) character determinant;
- a Hilbert--Pólya operator or any consequence for Riemann zeros.

## Positioning consequence

The correct publication stance is asymmetric:

```text
GO_FORMAL_EQUIVARIANT_LEDGER
STOP_CHARACTER_FREDHOLM_FIBERS
```

The formal lift is useful because it exposes recurrent label motion hidden by
scalar dimension.  The same refinement fails as an arithmetic fixed-operator
character determinant.  This separation, rather than the classical
formalism itself, is the content of Paper 16.
