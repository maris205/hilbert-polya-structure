# Paper 19 research-question brief

Date: **2026-08-24**
Status: **PHASE-2 RESOLVED — MERGE INTO PAPER 12**

## Primary question

For the Paper-12 standardized transformation groupoid
`G_std = Std(X) rtimes R`, where every orbit has the same stabilizer
`H=LZ`, what are the algebraic groups
`H_cnv^n(G_std;R)` for every `n>=2` in the exact continuous,
unnormalized, trivial-coefficient nerve complex fixed there? Can the answer be
realized by an explicit cochain normal form or natural homotopy over an
arbitrary nonempty bare orbit set `Q`, and what does the actual-to-standard
map `J*` do in those degrees?

No value, including vanishing, is assumed in advance.

## Subquestions

1. Reduce the one-orbit complex to a fully typed complex associated with the
   stabilizer without changing continuity or normalization conventions.
2. Compute degree two explicitly before making an all-degree claim.
3. Determine whether arbitrary coproducts assemble cohomology as a full
   Cartesian product and record every choice/naturality issue.
4. Construct an explicit chain homotopy or cocycle/coboundary normal form,
   rather than citing equivalence heuristically.
5. Compute `J*` from the globally indiscrete actual owner and identify any
   strict-automorphism invariant image.

## FINER screen

| Criterion | Score / 5 | Reason |
|---|---:|---|
| Feasible | 4 | the complex and owner are already exact; degree two can be checked first |
| Interesting | 3 | clarifies what standardization adds above Paper 12's `H^1` |
| Novel | 3 | the exact conjunction may be new, but the calculation may reduce to standard Morita/cohomological-dimension facts |
| Ethical | 5 | pure mathematics; only claim inflation and source attribution require control |
| Relevant | 4 | closes an explicit limitation in Paper 12 and tests whether the standardized owner carries higher information |

Mean score: **3.8/5**, conditional on the routine-reduction gate.

## Owner and nonclaims

- Coefficients are real and trivial; the complex is continuous,
  unnormalized, and algebraic after quotienting.
- The orbit set is bare; no count, topology, measure, boundedness, support, or
  summability is imposed on `Q`.
- No normalized cohomology, twisted coefficient, cohomology topology,
  `C*`-algebra, trace, determinant, analytic continuation, or operator is
  claimed.
- Paper 12's degree-one result is prior work.

## Decisions

- **Promote:** an explicit all-degree theorem with naturality and exact `J*`.
- **Technical note/merge:** only a routine one-line consequence of a standard
  equivalence remains after maximum prior subtraction.
- **Stop:** the exact complex cannot be matched to the proposed reduction or
  degree two contradicts the intended assembly.

## Phase-2 resolution

The [source/routine screen](phase2_source_routine_screen.md) found that
transitive reduction, `cd(Z)=1`, exact products, and the
normalized/unnormalized comparison conditionally determine the higher
groups.  The exact author-complex comparison, cup convention, and higher
`J*` remain local proof tasks.  The disposition is nevertheless resolved:
retain the theorem shape for a future Paper-12 amendment and do not authorize
a standalone Paper-19 manuscript.
