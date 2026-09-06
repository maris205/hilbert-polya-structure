# Owner and portfolio audit: open P166 finite-algebra lane

**Search date:** 3 September 2026  
**Decision:** `KILL_ALL / HOLD_EXTERNAL`

This was a bounded primary-source audit.  Search-engine snippets were used only
to route to author manuscripts, journal PDFs, DOI/publisher records, and arXiv
records.  A query non-hit is not evidence of novelty or priority.

## 1. Search lanes

The recorded query families included:

```text
"X^2+X=A" matrices characteristic 2 Artin-Schreier
Artin-Schreier map triangular matrix algebra finite field
upper triangular idempotent matrices finite field enumeration
square-zero upper triangular matrices finite field

Cartan embedding g inverse theta(g) symmetric space
"g^{-1} theta(g)" iteration dynamics
perfect matching association scheme coset type hyperoctahedral
perfect matching power map union alternating cycles

Galois invariant linear codes subfield subcode scalar extension
Galois interior operator linear codes
Delsarte trace code subfield subcode dual
rational-point-free subspaces quadratic extension Mobius
```

The literal iterate packages were not located as a single printed theorem in
these bounded searches.  That fact gives no positive novelty evidence and is
irrelevant to the final kills, which already follow from direct ingredients
and internal collisions.

## 2. UTAS owner boundary

### Verified primary records

1. Shalosh B. Ekhad and Doron Zeilberger, *An Explicit Formula for the Number
   of Solutions of `X^2=0` in Triangular Matrices over a Finite Field*,
   [arXiv:math/9512224](https://arxiv.org/abs/math/9512224).  The primary record
   explicitly supplies an all-order formula for the square-zero upper
   triangular matrices.  These are exactly the UTAS fixed points.
2. Xin Hou, *Idempotents in triangular matrix rings*, *Linear and Multilinear
   Algebra* 69 (2021), 296--304,
   [doi:10.1080/03081087.2019.1596223](https://doi.org/10.1080/03081087.2019.1596223).
   The publisher record says that it describes triangular idempotents and,
   over a finite ring, calculates their number.  UTAS's zero fibre is therefore
   direct static background.

### Subtraction

- zero credit: Artin--Schreier polynomial notation, nilpotent functional
  calculus, triangular idempotent enumeration, and square-zero fixed census;
- residual: the elementary iterate identity and the bijection from a target
  fibre to idempotents in its triangular centralizer;
- fatal defect: the latter is not an evaluated all-target count, while every
  non-core point has tail one.

The internal nearest neighbours are P102 (power dynamics after one algebraic
collapse), P103 (matrix polynomial/adjugate strata), P119 (upper-unitriangular
word dynamics), and the permanent matrix-word/power kills.  No literal equality
with those maps is claimed; the combined theorem value remains below them.

**Owner gate:** `KILL_OWNER_DENSE_WEAK_INVERSE`.

## 3. RTCD owner boundary

### Verified primary records

1. Amanda K. Sutherland, *Generalizations of the Cartan and Iwasawa
   Decompositions for `SL_2(k)`*, *Journal of Lie Theory* 27 (2017), 155--176,
   [journal PDF](https://jolt.centre-mersenne.org/item/10.5802/jolt.938.pdf).
   Definition 2.6 writes the symmetric-space image as
   `{g theta(g)^(-1)}` and the extended locus as
   `{x:theta(x)=x^(-1)}`; Remark 2.7 identifies the quotient by the fixed-point
   group.  RTCD uses the inverse orientation of the same Cartan embedding.
2. Murali K. Srinivasan, *The perfect matching association scheme*,
   *Algebraic Combinatorics* 3 (2020), 559--591,
   [doi:10.5802/alco.104](https://doi.org/10.5802/alco.104).  The paper treats
   the `S_(2r)` action on perfect matchings and identifies its Bose--Mesner
   algebra with the double-coset algebra for the Gelfand pair `(S_(2r),H_r)`.
   The partition/coset-type organization used by RTCD is therefore classical.
3. Márton Hablicsek and Guillermo Mantilla-Soler, *Power map permutations and
   symmetric differences in finite groups*,
   [arXiv:1109.2256](https://arxiv.org/abs/1109.2256).  This is a primary
   boundary source for permutation actions induced by power maps on finite
   groups; it does not state RTCD's matching-restricted census.

### Subtraction and decisive internal collision

- zero credit: Cartan image, quotient/fibre by `C(w_0)`, perfect matching
  carrier, hyperoctahedral stabilizer, matching coset types, and ordinary power
  maps;
- possible residual in isolation: the explicit `-2` iteration on this Cartan
  image and the resulting matching-partition fixed sequence;
- decisive subtraction: P102 already develops the same complete architecture
  for an involution norm: one step into the involution-defined locus, later
  power iteration, exact fixed sequence, Mobius cycle census, sharp depth, and
  parameter recovery.  Replacing split Fourier blocks by matching coset types
  does not pass the present proof-engine firewall.

The unresolved positive-time target quantity

```text
#{y in Omega_n : y^((-2)^(t-1))=z}
```

is also not a closed every-target theorem in the scout.

**Owner/portfolio gate:** `KILL_INTERNAL_P102_PROOF_ENGINE`.

## 4. SCD owner boundary

### Verified primary records

1. Philippe Delsarte, *On subfield subcodes of modified Reed--Solomon codes*,
   *IEEE Transactions on Information Theory* 21 (1975), 575--576,
   [doi:10.1109/TIT.1975.1055435](https://doi.org/10.1109/TIT.1975.1055435).
   This is the controlling trace/subfield-duality source.
2. Marta Giorgetti and Andrea Previtali, *Galois invariance, trace codes and
   subfield subcodes*, *Finite Fields and Their Applications* 16 (2010),
   96--99,
   [doi:10.1016/j.ffa.2010.01.002](https://doi.org/10.1016/j.ffa.2010.01.002).
   The primary paper relates Galois invariance, restriction, and trace and
   characterizes invariant codes through these constructions.
3. A. Fotue Tabue, E. Martínez-Moro, and C. Mouaha, *Galois Correspondence on
   Linear Codes over Finite Chain Rings*,
   [arXiv:1602.01242](https://arxiv.org/abs/1602.01242).  The abstract and text
   explicitly define Galois closure and interior operators on the lattice of
   linear codes; fields are a special case of that framework.

### Subtraction

- zero credit: subfield subcodes, scalar extension, Galois-stable codes,
  Galois interior, duality, Gaussian coefficients, and subspace-lattice Mobius
  inversion;
- residual: packaging the one-step fibre as the number `A_k(q)` of
  rational-point-free extension-field subspaces;
- fatal defect: `T=perp o I` exposes an idempotent interior projection followed
  by an involution, exactly the one-step projection form barred at intake.

P109's finite-subspace image/fibre work and the current closure/semilattice
kills further reduce portfolio value, although they are not literal copies of
SCD.

**Owner gate:** `KILL_ONE_STEP_GALOIS_INTERIOR`.

## 5. Final owner/value ruling

There is no direct-owner claim based on silence.  The decisions instead use
positive ownership of each main background mechanism plus a decisive internal
architecture collision for the strongest system.

| candidate | direct background burden | internal burden | result |
|---|---|---|---|
| UTAS | square-zero and idempotent triangular matrices | P102/P103/P119 neighbourhood | kill |
| RTCD | Cartan embedding and matching Gelfand pair | **P102 full proof engine** | kill |
| SCD | Delsarte/Galois interior and duality | one-step closure/subspace engines | kill |

**Final: `KILL_ALL`.  `HOLD_EXTERNAL`.**
