# Geometry/group/topology bounded owner-search log

**Status:** `HOLD_EXTERNAL`  
**Interpretation rule:** a missed query is not evidence of novelty; a direct
owner or an internal proof-engine transfer is sufficient to kill.

## Search discipline

The owner pass was deliberately early and bounded.  Queries were issued for
literal update terms and for the mathematical primitives exposed by the exact
pilots.  Only primary papers, publisher/DOI records, or author manuscripts were
used to make substantive technical subtractions.  Search snippets were not
used as theorem proofs.

Representative query strings:

```text
finite Grassmannian coordinate flag trace subspace fibre q-binomial Schubert
symplectic radical of subspace number totally isotropic subspaces finite field
U intersection (V+W) cyclic triple subspaces retraction modular lattice
P -> O_p(N_G(P)) iteration radical p-subgroups Bouc complex
ordered matroid contraction rank word target fibres
finite Alexandrov topology regular closed cl(int(S))
iterated Chebyshev center set graph subset finite metric
farthest point set iteration path cycle graph metric
projective point subset essential points coloops deletion lowers rank
affine plane line subset unique parallel class dynamics
Euler characteristic link vertex pruning simplicial complex
exactly one cofacet boundary derivative simplicial complex
```

## Primary records actually verified

1. Hansen, Johnsen, and Ranestad, *Schubert Unions in Grassmann Varieties*,
   arXiv:math/0503121.  This is a primary finite-field Schubert-union study and
   confirms that counting relative to a fixed flag is an established
   enumerative setting: <https://arxiv.org/abs/math/0503121>.
2. Maginnis and Onofrei, *Homotopy equivalences between p-subgroup
   categories*, Journal of Pure and Applied Algebra 219 (2015), 3030--3052,
   DOI 10.1016/j.jpaa.2014.10.002.  Its primary results explicitly use the
   radical collection and record the Bouc/Quillen ownership of radical
   `p`-subgroups: <https://doi.org/10.1016/j.jpaa.2014.10.002>.
3. Whitney, *On the Abstract Properties of Linear Dependence*, American
   Journal of Mathematics 57 (1935), 509--533, DOI 10.2307/2371182.  This is
   the primary matroid source used for the dependence/coloop/minor
   subtraction: <https://doi.org/10.2307/2371182>.
4. Hakimi, *Optimum Locations of Switching Centers and the Absolute Centers
   and Medians of a Graph*, Operations Research 12 (1964), 450--459, DOI
   10.1287/opre.12.3.450.  This directly owns the graph-center primitive:
   <https://doi.org/10.1287/opre.12.3.450>.
5. Kuratowski, *Sur l'opération A-bar de l'Analysis Situs*, Fundamenta
   Mathematicae 3 (1922), 182--199.  The EuDML primary record and full text
   directly establish the closure-operation algebra used by `RCR`:
   <https://eudml.org/doc/213290>.
6. Pierce, *The Boolean Algebra of Regular Open Sets*, Canadian Journal of
   Mathematics 5 (1953), 95--100, DOI 10.4153/CJM-1953-011-0.  The paper
   studies precisely the regular-open Boolean algebra adjacent to `RCR`:
   <https://doi.org/10.4153/CJM-1953-011-0>.
7. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134
   (1998), 90--145, DOI 10.1006/aima.1997.1650.  This is a primary owner for
   the elementary-collapse/free-face environment against which `ELP/BPD`
   were subtracted: <https://doi.org/10.1006/aima.1997.1650>.
8. Forman, *Witten--Morse Theory for Cell Complexes*, Topology 37 (1998),
   945--979, DOI 10.1016/S0040-9383(97)00071-2, gives a second direct primary
   record for the same cell-complex reduction environment:
   <https://doi.org/10.1016/S0040-9383(97)00071-2>.
9. The 1965 primary note *The Number of Isotropic Subspaces in a Finite
   Geometry* treats the symplectic/skew-symmetric isotropic-subspace census
   used in `SRE`: <https://www.bdim.eu/item?fmt=pdf&id=RLINA_1965_8_39_6_418_0>.

These records are subtraction evidence only.  They do not assert that every
literal conjunction in the scout has appeared in print.

## Candidate-by-candidate owner gate

| ID | external result | internal result | disposition |
|---|---|---|---|
| `GG01/FTR` | fixed-flag finite-field Grassmannian/Schubert enumeration is established | coordinate restriction plus P109-style subspace fibres; current graph/set scout independently kills the analogous trace clock | `KILL_FLAG_TRACE_OWNER_THIN` |
| `GG02/SRE` | direct finite symplectic isotropic-subspace enumeration | radical/hull is a one-step meet under orthogonality | `KILL_WITT_RETRACTION_SHALLOW` |
| `GG03/MTE` | no literal title located in the bounded pass | a three-line modular-lattice argument proves `T^2=T`; no external miss can restore dynamics | `KILL_MODULAR_RETRACTION_SHALLOW` |
| `GG04/PRC` | radical `p`-subgroups and their homotopy role are directly owned | P154 owns subgroup normalizer dynamics; adding `O_p` does not create an owner-thin residual | `KILL_DIRECT_P_RADICAL_OWNER` |
| `GG05/OMC` | matroid contraction/minors are foundational and direct | rank word is an imposed ordered deletion clock | `KILL_DIRECT_MATROID_MINOR_THIN` |
| `GG06/RCR` | closure algebra and regular-open/closed algebras are direct primary literature | `cl int` is idempotent, so there is no temporal residual | `KILL_CLASSICAL_REGULARIZATION` |
| `GG07/MCS` | graph centers are directly classical | paths reduce to midpoint extraction; cycles already introduce 2-cycles and remove the clean monotone theorem | `KILL_CENTER_OWNER_OR_UNSTABLE` |
| `GG08/MFS` | no precise literal iteration owner was needed after the theorem gate failed | exact pilots are dominated by antipodal 2-cycles and lack a stable all-family theorem | `KILL_ANTIPODAL_SHADOW_UNSTABLE` |
| `GG09/EPC` | dependence, independence, and matroid structure are directly owned | the retained points are exactly the coloops of the restriction; one-step retraction | `KILL_MATROID_COLOOP_RETRACTION` |
| `GG10/LPU` | affine parallel classes are classical; no literal dynamics paper was retrieved | exact product over independent direction classes proves both fibres and `T^2=T` | `KILL_PARTITION_EXTRACTOR_SHALLOW` |
| `GG11/ELP` | cell-complex local reduction has direct primary owners | generic simultaneous pruning plus occupied Euler/parity support, with no all-target theorem | `KILL_LOCAL_PRUNING_ENGINE` |
| `GG12/BPD` | boundary/free-face/cell-collapse environment is directly classical | strict dimension loss is the whole clock; close to P67 and recent topology kills | `KILL_BOUNDARY_OWNER_THIN` |

## Internal firewall receipts

The most important exact internal comparisons were:

- `FTR` versus P109's subspace image/fibre machinery and the current
  set-family coordinate-trace control;
- `PRC` versus P154's normalizer map;
- `OMC/EPC` versus the dense matroid/minor occupancy;
- `ELP/BPD` versus P67 and the recent simultaneous-collapse/free-face kills;
- every possible projective-polar, orthocenter, Lyness, Vieta, QNC, generic
  action/walk, involution, or finite-linear variant was rejected before the
  twelve-system count.

## Final owner disposition

```text
direct/classical owner kills: 6
internal/shallow proof-engine kills: 5
unstable theorem-gate kill: 1
conditional survivors: 0
paper-sized survivors: 0
status: EMPTY_POOL / HOLD_EXTERNAL
```

No paper number should be assigned from this lane without a new literal
mechanism and a fresh owner search.

