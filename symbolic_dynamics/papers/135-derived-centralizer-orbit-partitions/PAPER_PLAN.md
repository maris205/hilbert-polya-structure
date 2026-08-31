# Paper plan: derived-centralizer orbit partitions

**Working title:** Derived-Centralizer Orbit Partitions: Tagged Transients,
Recurrent Types, and Exact Fibres  
**Type:** rigorous mathematical short note  
**Status:** `GO_INTERNAL / HOLD_EXTERNAL`  
**Target length:** 5--8 A4 pages, including references  
**One-sentence contribution:** For the partition self-map obtained from the
orbits of the derived subgroup of a permutation centralizer, prove the exact
wreath-product local rule, an all-weight tagged transient theorem, the
complete recurrent classification and ordinary generating functions, and a
coefficient formula for every target fibre.

## Claims--evidence matrix

| Claim | Proof object | Paper-local control | Credit boundary |
|---|---|---|---|
| `j^m` maps to `1^j`, `j^2`, or `jm` according as `m=1,2,>=3`. | Derived subgroup and orbit calculation for `C_j wr S_m` | Literal commutator closure in 18 wreath products, 1,259 source group elements | Centralizer/wreath decomposition and commutator structure are zero credit. |
| Every orbit has eventual period at most two and tail at most `2 ell(lambda) <= 2n`. | Tag invariant, crossing potential, and two-clean-step lemma | 118,634 reachable tagged states and 56,961 clean pairs through weight 30 | The bound is safe and explicitly nonsharp. |
| `B`, `O1`, `O2=`, and `O2!=` are all recurrent objects. | Clean tagged normal form plus direct converse | Decoder agrees on all 540,634 partitions through weight 45 | A finite census is not the proof. |
| Fixed points and strict two-cycles have the two displayed OGFs. | Equations (8)--(9), Theorem 4.1, and the unnumbered generating-function proof in Section 4 | Coefficients through weight 30; at weight 30: `59,139,337` | Formal product extraction alone is zero credit. |
| Every target fibre is the stated multivariate coefficient. | Independent multiplicity-vector product | All 28,628 targets through weight 30, including zero fibres | The product is credited only as part of the package. |

## Structure

1. **Definition and main theorem.** Define the literal orbit-partition map
   and state all five contracts at once.
2. **Wreath-product reduction.** Prove the derived subgroup formula and its
   natural-point orbits for every `j,m`.
3. **Tagged transient theorem.** Establish whole/split tag form, strict
   coarsening on crossing merges, the reachable two-clean normal form, and
   the nonsharp `2 ell` bound.
4. **Complete recurrence and OGFs.** Prove the `B/O1/O2` list is exhaustive
   and derive fixed/cycle series.
5. **Every-target inverse coefficient.** Expand independent local source
   multiplicities and extract the target monomial.
6. **Owner subtraction and controls.** Separate prior group/partition
   machinery from the residual theorem, and distinguish P113 and P123.

## Display plan

No decorative figure.  A four-row recurrent-class table is the central
visual.  A compact verification table reports only falsification controls.

## Citation plan

- Britnell--Wildon for orbit partitions and permutation-centralizer context.
- Skuratovskii for commutator subgroups in wreath products.
- Eliahou--Erickson for neighboring multiplicity-description dynamics.
- Baalbaki et al. for recent weight-preserving partition dynamics.

All records were checked against publisher, institutional, or official
arXiv metadata.  Every bibliography entry is cited.

## Writing review applied

The short-note override replaces a conference template.  Complete proofs
stay in the main text; enumeration is isolated as control evidence.  The
Stage-2 instruction defers hostile Reviews A/B, so this package freezes only
round 0.
