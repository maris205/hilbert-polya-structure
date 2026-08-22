# Route-A dynamics-variant batch plan: C104--C108

Status: **five paper outputs complete; uniform prefreeze audit passed**

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This round deliberately broadens the frozen Hénon family by testing five
different dynamical subtypes.  Each package is source-locked, finite, and
reproducible.  A finite symbolic or monodromy prefix is never promoted to a
complete geometric coding, an analytic Fredholm theorem, arithmetic data, or
Route B.

## Research sequence

1. **C104 — polynomial multi-branch Hénon.**  For
   (H_{1/7}(x,y)=(x^3-3x+1/7-y,x)), enumerate the complete three-letter
   branch-word pilot through length six and certify its (6\times6) block
   transfer prefix.
2. **C105 — kneading/pruning and a Hofbauer gate.**  Freeze a finite
   lexicographic kneading pair, exclude unresolved comparisons, and derive the
   exact accepted rooted/primitive prefix through period twelve.
3. **C106 — coupled variational Hénon lattice.**  Use the exact two-site
   variational/symplectic map to compare a genuine synchronous period-two
   monodromy with its uncoupled control, while keeping operator ownership open.
4. **C107 — open-hole survivor dynamics.**  Delete the frozen H6 state 3 and
   certify the finite survivor transfer (B) and its escape determinant
   (det(I-zB)=1-z-z^3).
5. **C108 — complex holomorphic Hénon transfer.**  Solve the period-one/two
   equations exactly, compute the Jacobian-weight trace prefix, and test the
   obstruction from inverse-pullback degree growth.

## Authority and dependency boundary

C104, C106, and C108 are independent candidate-system pilots.  C105 is a
finite language certificate whose unresolved boundary comparisons remain
explicit.  C107 reads only the frozen four-state symbolic interface and the
specified hole state.  None of the five packages imports arithmetic labels,
Euler products, root numbers, automorphy, a full Hénon periodic-orbit atlas, or
a Hilbert--Pólya operator.

## Uniform release gate

Every package contains a research question, source audit, theorem/boundary
package, executable producer, independent checker, exact symbolic check where
appropriate, replay, hostile mutation audit, LaTeX source and PDF, compile
report, narrative/plan/improvement records, and a content-addressed manifest.
The final audit requires matching evidence/PDF hashes, complete manifest file
ledgers, two isolated builds with `SOURCE_DATE_EPOCH=0`, embedded fonts, and no
layout/reference warnings.

## Paper and artifact ledger

| paper | dynamical subtype | PDF pages | hostile mutations | evidence SHA-256 | manifest SHA-256 | PDF SHA-256 |
|---|---|---:|---:|---|---|---|
| C104 | cubic three-branch polynomial Hénon | 2 | 9/9 | `392b356265b1f4caaec9dd0b9f9ff1d5466acef3e25374c443d3e55c9e199205` | `38dd82b4edc6f94950608fd3bda109f2f95ecf0f3cbfd9508fbbc15c5c1a9661` | `b9d3a478e211cfe4856485c96e0045de0c95240354e3163768ddf09f57761efb` |
| C105 | finite kneading/pruning language | 2 | 5/5 | `904d95fdcbbeda9f4ac86603c37f84101db406c3a9c76db2f5fd73bb04d9c78a` | `f0d2ea2a494b81aecc7801c7793c5b36350ca825882318fabbf0d1f2fc68d932` | `ba3fdf0f1663571d0feb4a7f62a1097190a9c646f7b088974ed659655c5590bb` |
| C106 | exact two-site variational/symplectic lattice | 2 | 11/11 | `3c3c512f021a8bb4ba094ed8dc14a9635346f566ef404fd6f799dbf7340d1f9b` | `17243df8e1402388bb9efc6fff77b1fd49e08d94503b7fbe34e8a150ae23e662` | `73eccfff0ada7eafe1a96caac809faad1a70845bb719f2d558a76634ce9a0d2f` |
| C107 | finite open-hole survivor transfer | 1 | 6/6 | `433d8dbe9bb577932c85a7963aecf8af6e6151f727066a8f1e526d7ba1717ac8` | `a992f89d0333b577b74b030e330daf19841a4f6d54aea0c109e47198ecbbfb4b` | `32211c220aed2c6ba7ecc60d55158750c6d02eb00383f04525cf28cc824a6b04` |
| C108 | complex holomorphic polynomial Hénon | 2 | 5/5 | `e4609f071e144fd0a534ab028cbc40a00027b49db67dc20782ae3f49eb150b65` | `db82a4f0f85d099c2300990f5caca3bdd45f55e4903492d840386f3c31c2e0ec` | `5fa264e11c73b2b81e9c343280971e0db5beccd3b6c67ab86eae1efcacb416e0` |

## Route-A boundary after this round

| paper | A1 | A2 | A3 | A4 |
|---|---|---|---|---|
| C104 | `A1_OPEN` | `A2_CERTIFIED_PREFIX` | `A3_NOT_ADDRESSED` | `A4_FAIL` |
| C105 | `A1_OPEN` | `A2_CERTIFIED_PREFIX` | `A3_NOT_ADDRESSED` | `A4_FAIL` |
| C106 | `A1_WEAK` | `A2_FAIL` | `A3_NOT_ADDRESSED` | `A4_FAIL` |
| C107 | `A1_PARTIAL_CERTIFIED` | `A2_CERTIFIED_PREFIX` | `A3_NOT_ADDRESSED` | `A4_FAIL` |
| C108 | `A1_OPEN` | `A2_CERTIFIED_PREFIX` | `A3_NOT_ADDRESSED` | `A4_FAIL` |

The global evaluator tuple therefore remains

```text
(A0_NOT_ADDRESSED, A1_WEAK, A2_CERTIFIED_PREFIX,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
```

with overall status `ROUTE_A_EXPLORATORY`.  The round supplies several
candidate dynamical subtypes and exact finite witnesses, but no source-native
compact/nuclear operator or arithmetic ownership.  Route B remains
unauthorized.

## Reproduction commands

Run the package-specific commands in each linked README, then regenerate its
manifest.  The five paper PDFs are:

- [C104 paper](henon_polynomial_multibranch_route_a/paper/main.pdf)
- [C105 paper](henon_kneading_pruning_hofbauer/paper/main.pdf)
- [C106 paper](henon_variational_coupled_henon_lattice/paper/main.pdf)
- [C107 paper](henon_open_hole_route_a/paper/main.pdf)
- [C108 paper](henon_holomorphic_complex_transfer/paper/main.pdf)
