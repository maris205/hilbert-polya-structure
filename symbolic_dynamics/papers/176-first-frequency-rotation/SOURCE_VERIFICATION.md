# Source verification

**Checked:** 2026-09-03 UTC  
**Lifecycle:** `AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL`

## Verified primary sources

### Høyer and Špalek (2005)

- Publisher page: <https://theoryofcomputing.org/articles/v001a005/>
- Publisher BibTeX: <https://theoryofcomputing.org/articles/v001a005/bibtex.txt>
- DOI: <https://doi.org/10.4086/toc.2005.v001a005>
- Verified metadata: Peter Høyer and Robert Špalek, *Quantum Fan-out is
  Powerful*, **Theory of Computing** 1(5), 81--103 (2005).
- Content check: Section 3.2 is titled “Rotation by Hamming weight and
  value” and constructs `R_z(phi |x|)`.  This is a quantum phase rotation,
  not the cyclic coordinate shift used by FCR.  The manuscript therefore
  assigns only the broad Hamming-weight-controlled rotation phrase to this
  source and gives it zero contribution credit.  The ordinary coordinate
  branches are separately subtracted through the coordinate-rotation sources
  below.  Høyer--Špalek is not described as their literal owner or as an owner
  of the adaptive word map.

### Heckenberger and Sawada (2018)

- arXiv record: <https://arxiv.org/abs/1801.09516>
- Verified arXiv API metadata: I. Heckenberger and J. Sawada,
  *A Pascal-like Bound for the Number of Necklaces with Fixed Density*,
  arXiv:1801.09516 [math.CO], submitted 2018-01-29.
- Content check: the paper defines binary necklaces and Lyndon words of
  fixed density and records fixed-content enumeration formulas involving
  the Möbius function.  Those background ingredients receive zero credit.

### Meštrović (2018)

- arXiv record: <https://arxiv.org/abs/1804.00992>
- Verified arXiv API metadata: Romeo Meštrović, *Different classes of
  binary necklaces and a combinatorial method for their enumerations*,
  arXiv:1804.00992 [math.CO], submitted 2018-03-31.
- Content check: the paper discusses primitive binary necklaces and derives
  the Moreau/MacMahon--Witt enumeration formulas.  Primitive-word counting
  and Möbius inversion receive zero credit.

### Grošek and Hromada (2016)

- DOI: <https://doi.org/10.1515/tmmp-2016-0033>
- Verified metadata: Otokar Grošek and Viliam Hromada,
  *Rotation-Equivalence Classes of Binary Vectors*, **Tatra Mountains
  Mathematical Publications** 67, 93--98 (2016).
- Content check: the paper studies actual coordinate-rotation classes on
  fixed-weight binary vectors, including feasible class sizes and their
  enumeration.  Those necklace and fixed-weight census ingredients receive
  zero credit.  It does not define the adaptive first-symbol gluing or its
  functional graph.

### Gupta et al. (2022)

- DOI: <https://doi.org/10.3390/appliedmath2010005>
- Verified metadata: Anant Gupta, Idriss J. Aberkane, Sourangshu Ghosh,
  Adrian Abold, Alexander Rahn, and Eldar Sultanow, *Rotating Binaries*,
  **AppliedMath** 2(1), 104--117 (2022).
- Content check: the paper treats literal circular coordinate shifts,
  rotation distance and equivalence, Hamming weight, and complement symmetry.
  Those ordinary coordinate-rotation ingredients receive zero credit.  It
  does not define the adaptive first-symbol gluing or its functional graph.

## Internal source boundary

The internal primary comparison is
`papers/166-hamming-weight-translation-dynamics/main.tex`.  P166 acts on
`(Z/nZ)^n` by `x -> x + wt(x) 1` and reduces each diagonal orbit to
`j -> j+c_j`, where `c` is a weak composition of `n`.  FCR reduces a
coordinate-rotation necklace to the same generic phase syntax but with
increments restricted to `+k` and `-k`.  The shared syntax, P166's existing
`n-2` clock, and its target-indicator presentation are all subtracted.
P166's mass-exhaustion theorem does not by itself give the disjoint
generator-cycle orientation used here; this is the current amber residual,
not external clearance.

## Search ceiling

The bounded owner log is preserved at
`docs/papers172_176_sequence/scouting/combinatorial_crossdomain/`\
`focused_nonextractive/OWNER_SEARCH_LOG.md`.  A terminology-dependent
non-hit is not treated as positive mathematical or circulation evidence.
The direct-owner kill switch remains active.
