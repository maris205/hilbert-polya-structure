# HCS-C61 exact experiment plan

Status: **`TARGET_LOCKED / IMPLEMENTATION_PENDING / PAPER_PENDING /
NOT_RELEASED`.**

Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Target-report binding:
`eb0a70f62427cd8b70fa35dc4153bd93d57d9ddef5ab7a349d439be3a8257026`.

This is a design for future implementation, not executable evidence.  All
G0--G7 gates are `PENDING`.  Pilot values below are expected targets that must
be reconstructed project-locally from released P60/C60 authority.

## 1. Objective and decision rule

Build one exact producer/checker package that either certifies the complete
integrated tensor/Fourier target or kills it.  Passing only a subset does not
authorize an atlas-only, Fourier-only, local-only, or one-self-product paper.

The future decision rule is:

```text
GO only if G0=...=G7=PASS and every scope leaf remains false.
KILL on the first failed central identity, missing inventory, independence
failure, source overclaim, or scope/release violation.
```

No target-selection pilot counts as an official gate run.

## 2. Frozen inputs and conventions

### Released authority to rebind

- P60: `fe1217810b72840619efdf40a2af31b8b80d96f6`;
- P60 parent/tree:
  `f3b3726c40519cdd8ac7832f9f22df16d451b890` /
  `22b67a5ad27cc0e447bd63ecd2d9ac13ad2a595a`;
- C60 full manifest:
  `37c1f227aee6c0bfff233ffc1a7f1f8d2a8a27657faad353af711f2e503ed0a4`;
- C60 live/archive Route:
  `8ff624d1fa3d598c4f6aeddea8a9274619f2f21b468054281dda4169480c5872`;
- C60 certificate/payload:
  `d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518` /
  `dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead`;
- C60 group/resolvent evidence:
  `dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2` /
  `f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da`;
- C60 frozen permutation arrays:
  `0fc281590b635eed046cc4a8d38036895e2b1bc56284a0948b1576303de1c2f5`;
- C60 `L` carrier:
  `fae69eb91d414d8241bbbee51f4a3fcc91c4f8691090adc5cbb575079d2ea1f5`;
- C59 resolvent evidence:
  `667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6`;
- released Batch:
  `d1a9ebd06f125b1b4236f974e9e4b179f0cf2a57584f1ba180debf3591f2e3f5`;
- C59's exact labelled roots and split witness `p=692717`;
- protected guard as an external input, not a C61-owned artifact.

### Locked conventions

Group arrays are one-based; sparse monomials are zero-based; composition is
left after right; `p(X_i)=X_{p(i)}`; canonical sparse carriers have exact
integer coefficients and lexicographically sorted terms; duplicate JSON keys,
floats, integer-slot booleans, noncanonical integers, symlinks, stale reads,
and optimized-Python bypasses are rejected.

## 3. Planned artifact boundary

Suggested producer APIs are:

```text
build_tensor_products(authority, Hplus, Hminus) -> TensorEvidence
build_mixed_dictionary(tensor_evidence) -> MixedFieldEvidence
build_resolvents(authority, subgroup_targets) -> ResolventEvidence
build_fourier(authority, lambda, quotient_reps) -> FourierEvidence
build_diamond(groups, carriers) -> DiamondEvidence
build_global_arithmetic(groups, filtrations) -> GlobalEvidence
build_local_arithmetic(groups, filtrations, branches) -> LocalEvidence
```

Independent Python, GAP/TomLib, and arithmetic checkers must not import
producer mathematics.  The only shared code may implement strict neutral I/O,
canonical JSON, hashing, stable snapshot reads, and path safety.

## 4. G0 — released authority, object, and scope

G0 shall:

1. verify every released path by bytes and digest before parsing;
2. prove live/archive C60 Route equality and full/scoped manifest contracts;
3. rebind the owner-supplied final target-report digest
   `eb0a70f62427cd8b70fa35dc4153bd93d57d9ddef5ab7a349d439be3a8257026`
   and its exact 59,956-byte/1,096-line shape;
4. verify all 13 formal roots, live Route, and Batch are the exact integrated
   inputs expected by the implementation commit;
5. bind action/index conventions, the integrated title and object, and the
   prior-art boundary; and
6. verify exactly 30 named scope leaves, each Boolean `false`, plus the exact
   scope literal.

The target-report input is now fixed, but G0 remains `PENDING` until a future
implementation independently rebinds it with all other released inputs.

## 5. G1 — all three tensor products

Independently enumerate the twelve double cosets in each product.  For each of
the 36 rows store the canonical seed/conjugator, orbit multiplicity,
intersection `I`, join `J`, complete embedded arrays, orders, indices, cores,
normalizers, automorphism orders, conjugacy proofs, field degrees, and unified
`Q`/base type.

Required spectra are:

```text
T++ = [320x2,960x2,1920,5760x2,8640x2,17280,25920x2]
T+- = [640,960x2,1920,2880x4,8640x2,17280,51840]
T-- = [320x2,960x2,1920,5760x2,8640x2,17280,25920x2]
```

Check twelve factors and sum 102400 in each lane.  Compute complete
permutation characters and verify pointwise product equality.  Prove pairwise
Burnside/finite-étale nonisomorphism: mixed versus self by spectra; self versus
self by diagonal degree-320 types and the core-free normal-closure extension
argument.

The plus-self `263f...` and minus-self embedded `a426...` degree-1920 joins
must be proved G-conjugate using

```text
[25,22,23,27,24,26,9,13,20,16,19,7,11,8,10,15,12,14,18,21,17,4,1,2,6,3,5]
```

and the common P3 class must be proved nonconjugate to mixed Fourier
`55d7...`.  A claim of three nonconjugate order-1296 joins fails G1.

## 6. G2 — mixed 160/12/8 dictionary

Enumerate all 160 conjugates of `H_-`, their twelve `H_+` orbits, and eight
`Q`-isomorphism types without conflation.  For every representative `g`,
certify

\[
 I_g=H_+\cap gH_-g^{-1},\qquad
 J_g=\langle H_+,gH_-g^{-1}\rangle,
\]

\[
 E_g=F_+F_-^g=K^{I_g},\qquad
 C_g=F_+\cap F_-^g=K^{J_g}.
\]

Prove every `I_g` core-free and prove the extension-of-isomorphism criterion
used for grouping fields.  Rebound the unique degree-640 minimum to C60
`L/M` and the unique degree-51840 maximum to `K`.

## 7. G3 — product-form resolvents

Construct source-owned integral labelled-root carriers for every advertised
new mixed field/base and for `A,B`.  Reuse C60 carriers only after G0.  For
each carrier certify:

- canonical sparse serialization and exact content;
- formal stabilizer and complete orbit;
- product-form orbit polynomial with no claim of expanded
  characteristic-zero coefficients;
- complete evaluation of all orbit values at `p=692717`;
- noncollision equal to the formal orbit size; and
- the resulting evaluated fixed-field degree.

No mixed factor may be deferred to a later field-by-field paper.

## 8. G4 — Fourier, type-3 bridge, and diamond

Use source-owned quotient representatives and characters of `N/J=V4` to
rebuild `Trace,R_0,R_+,R_3`.  Prove coefficientwise

\[
 R_0=0,
 \quad r_+=R_+/2,
 \quad r_3=R_3/4,
 \quad 4\lambda=Trace+2r_++4r_3,
\]

\[
 r_0=r_+r_3,
 \qquad \delta_0=r_0^2=\delta_+\delta_3.
\]

The expected normalized carrier hashes are:

| object | terms | SHA-256 |
|---|---:|---|
| `r_+` | 54 | `2edfe1e8f952faf2ddbfae3af135da4509f3f40e4175e188e240a5f09b785a96` |
| `r_3` | 162 | `b9c21c9fc7060d4e52630a75d6ec0c10305ac33946f78c2c93e33fad68df8c7e` |
| `r_0` | 7560 | `a26813d1b2874ee700ececba786af55391dacc2a30a0d4da0390ecb871f63382` |
| `delta_+` | 1458 | `1b5927b4d213dfd5af490067a9a551ae0942791a5221e2fb2f9f826440b040c3` |
| `delta_3` | 10125 | `5f8baf7254f5c27478afce45b5667c62d13a35b205739bbf20ebd36651a144e7` |

The Trace carrier has 243 terms and SHA-256
`a7398d36cea0c83ace64466a579e21666731d1e3c8e8641df4ce036c79de2bd7`.
At the split prime, the identity values of `Trace,r_+,r_3` must be exactly
`581739,643771,119649`.  Their nonzero values in distinct eigenspaces are a
required rank-three certificate.

The factorized `delta_0` DAG target is
`ed8974824f48cc65299443609c94db5ceab06efb8bed36f44b99ead311d28a66`;
expansion is not required.

Prove orbit-span dimension three and primitive-but-nonnormal status.  Rebuild
`S_+,T_+` from the carriers; compare complete embedded element sets.  Rebuild
the canonical seed-149 mixed row and prove exact equality of its join with
`T_+`.  Then certify subgroup intersection/join, cores, normalizers, normal
closures, automorphism groups, and

\[
 [A,B,M,F_+:Q]=[40,80,160,320],\quad B\cap M=A,\quad BM=F_+.
\]

## 9. G5 — complete global arithmetic

Compute the eight mixed compositum types, four mixed bases, and Fourier fields
`A,B` by independent orbit/conductor lanes.  Required `A,B` targets are

```text
A: signature (6,17), Disc=-3^75*5^61*Pi_A^24*Pi_B^15
B: signature (4,38), Disc=+3^154*5^122*Pi_A^48*Pi_B^30
```

where `Pi_A=181*997*2346241` and
`Pi_B=283*1801*14932047182473291995860108491583652133938007263719`.

Required relative norm vectors in `(v3,v5,vPi_A,vPi_B)` order are

```text
Norm(d_B/A)  = (4,0,0,0)
Norm(d_M/A)  = (8,4,0,20)
Norm(d_F+/B) = (8,8,0,40)
Norm(d_F+/A) = (24,8,0,40)
Norm(d_F+/M) = (8,0,0,0)
```

Both routes from `A` to `F_+` must give `(24,8,0,40)`.  The evidence must
include all eight mixed absolute exponent vectors, not only these Fourier
rows.

## 10. G6 — both local branches

Retain complete uncollected rows for all eight compositum types, all four
bases, `B`, and the C60 envelope under both `D_3=ToM140` and `D_3=ToM206`.
Check degree totals, different totals, factor counts, relative tower identities,
and branch-independent global exponents.

For the C60 envelope verify primewise

\[
 \min(a_+,a_3)=0,\quad a_0=a_++a_3,\quad a_L=2a_0,
\]

and consequently

\[
 (\mathfrak d_{F_+/M},\mathfrak d_{F_3/M})=1,
 \quad \mathfrak d_{F_0/M}=\mathfrak d_{F_+/M}\mathfrak d_{F_3/M},
 \quad \mathfrak d_{L/M}=\mathfrak d_{F_0/M}^2.
\]

Neither branch may be selected.  Archimedean complementarity is proved
separately.

## 11. G7 — independent authority and hostile verification

Require deterministic two-run replay; strict evidence schemas; independent
Python, GAP/TomLib, and arithmetic computations; atomic self-excluding
manifests; source locators; formal proofs; hostile theorem and paper review;
and explicit later promotion.

Mutation families must cover:

1. released authority and stale snapshots;
2. carrier coefficients, content, action, and exact division;
3. expression-DAG structure and nonzero `R_0`;
4. subgroup arrays, seeds, conjugators, cores, and normalizers;
5. factor degrees, multiplicities, 160/12/8 counts, and Q-type grouping;
6. the P3 correction and substitution of self P3 for mixed `T_+`;
7. modular noncollision and field degrees;
8. diamond intersections/joins and relative norms;
9. global signs/exponents and both routes around the diamond;
10. both local branches, every row, tame flags, and no branch selection;
11. JSON types, duplicates, oversize/path/symlink inputs; and
12. self-consistent hostile rebounds of values and their hashes.

## 12. Execution and resource budget

Run G0 and schema tests first, then G1/G2, G4 formal identities, G3 evaluated
resolvents, G5/G6 arithmetic, and G7 integration.  Expected complete runtime is
10--25 minutes with a hard 45-minute ceiling and peak RSS below 2 GiB.
`delta_0` remains factorized.  Cache only independently reconstructed facts;
never cache a pilot as authority.

## 13. Present state

No implementation inventory, schema, payload, certificate, checker report,
manifest, implementation commit, paper source, PDF, or archive exists.  All
future artifact hashes are null/pending rather than guessed.
