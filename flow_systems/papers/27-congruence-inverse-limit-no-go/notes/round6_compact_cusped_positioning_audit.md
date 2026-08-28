# P27 Round-6 compact-versus-cusped technical and citation positioning audit

Date: **2026-08-28**

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite`
- Origin Workflow: ARS Stage-1 theorem synthesis, primary-source positioning,
  and deterministic claim/source validation
- Mathematical owner: two explicitly separated residual towers and their
  coordinatewise unit-speed geodesic flows
- Source verification: authoritative publisher/arXiv web records checked on
  2026-08-28; author reading status `HUMAN_CONFIRMATION_PENDING`
- Forbidden status: no source is marked `USER_ATTESTED_READ`

## Scope

Round 6 asks whether Rounds 1--5 support a technically useful
compact-versus-cusped comparison and whether that result is a viable paper
unit.  It does not claim a new general aperiodicity theorem.  It also does not
turn finite-level zeta functions or periods into primitive-orbit data owned by
the inverse-limit flow.

## Common-core proposition

Let `Gamma` be a torsion-free Fuchsian group and

```text
Gamma = Gamma_1 >= Gamma_2 >= ...
```

a descending sequence of normal finite-index subgroups with
`intersection_n Gamma_n={e}`.  Put

```text
Y_n = Gamma_n \ H,
M_infinity = inverse_limit_n T^1Y_n,
```

and give every level the same hyperbolic-arclength clock.

### Proposition

1. The coordinatewise geodesic flow on `M_infinity` has no periodic point.
2. For every infinite-order `g in Gamma`, its quotient orders
   `o_n(g)=ord(g Gamma_n)` satisfy

   ```text
   o_n(g) divides o_(n+1)(g),
   o_n(g) -> infinity.
   ```

Evidence token: `[PROVED]`.

### Proof

If a coherent inverse-limit point had period `T>0`, its first coordinate
would lie on a closed geodesic.  For a primitive hyperbolic owner `gamma`, one
has `T=m ell(gamma)` for one fixed integer `m>=1`.  At level `n`, normality
removes the coordinate-dependent conjugator, so return after the same `T`
forces `gamma^m in Gamma_n`.  This at every level gives
`gamma^m in intersection_n Gamma_n={e}`, contradicting infinite order.

The quotient maps give `o_n(g)|o_(n+1)(g)`.  A bounded divisibility sequence
would eventually stabilize at some `r`, placing `g^r` in every `Gamma_n` and
again contradicting the trivial intersection.

This common theorem is an elementary synthesis of the local P27 proofs.  Its
broad structural mechanism has direct prior art, so it is not presented as a
new general aperiodicity discovery.

## Exact comparison

| Feature | Cusped factorial congruence tower | Closed genus-2 control |
|---|---|---|
| Base | `Gamma(3)\H`, finite area with cusps | any marked closed genus-2 hyperbolic surface |
| Tower | `Gamma(3n!)` | `R_n intersection ker(H_1 -> H_1 mod n!)` |
| Arithmetic input | principal congruence in `PSL_2(Z)` | none required |
| Residual proof | explicit sign-sensitive congruence proof in `PSL_2(Z)` | bounded-index residual cores plus Malcev residual finiteness |
| Finite executable | exact projective quotient orders for three matrices at eight levels | exact homology-image order lower bounds for three owners at eight levels |
| Owner primitivity | positive-word primitive only; full `Gamma(3)` conjugacy primitivity remains open | primitive homology forbids proper powers |
| Period statement | whole-`g`-loop closing time `o_n(g)ell(g)` | exact minimal lifted-geodesic period `T_n=o_n(g)ell(g)` |
| Quantitative bound | divergence in general plus the computed finite prefix | `n!|o_n(g)` and `T_n>=n!ell(g)` |
| Uncomputed object | no claim beyond the exact frozen quotient orders | residual cores and full quotient orders are not enumerated |

The comparison isolates the causal mechanism:

```text
normal residuality + one common clock + same-owner compatibility.
```

Cusps, principal congruence, and arithmetic-lattice provenance are not needed
for period escape or inverse-limit aperiodicity.  Arithmetic structure remains
part of the cusped example's provenance, but it is not the cause of the
obstruction.

## Authoritative source verification

The deterministic claim matrix records thirteen rows, nine of them tied to
five authoritative source records: four research articles and one theorem
exposition.  All external rows are
`PRIMARY_SOURCE_WEB_VERIFIED` with access date 2026-08-28 and
`HUMAN_CONFIRMATION_PENDING`.

### S1 — Martínez, Matsumoto, and Verjovsky

- Publisher: https://www.aimsciences.org/article/doi/10.3934/jmd.2016.10.113
- DOI: https://doi.org/10.3934/jmd.2016.10.113
- Technical text: https://arxiv.org/pdf/0711.2307
- Locators:
  - pp. 2--3, Section 2.2 defines the laminated geodesic flow leafwise;
  - p. 12, Example 4 gives a compact hyperbolic-lamination example without
    periodic geodesic-flow orbits;
  - pp. 15--16, Example 6 presents the universal hyperbolic solenoid with
    simply connected leaves.
- Positioning effect: broad aperiodicity novelty and the simply-connected-leaf
  mechanism are directly prior.

### S2 — Penner and Šarić

- DOI: https://doi.org/10.1007/s10711-007-9226-9
- Technical text: https://arxiv.org/pdf/math/0508476
- Locators: Introduction pp. 1--2 and Section 2, Definition 2.1 with its
  following discussion.
- Verified content: the punctured solenoid is a noncompact inverse limit over
  finite-index modular covers; its dense leaves are unit disks.
- Domain difference: it uses the directed system of all finite covers, not the
  single factorial principal-congruence chain and not P27's owner audit.

### S3 — Alcalde Cuesta, Carballido Costas, Martínez, and Verjovsky

- Publisher: https://ems.press/journals/ggd/articles/14299725
- DOI: https://doi.org/10.4171/GGD/967
- Technical text: https://arxiv.org/pdf/2411.18418
- Locators in arXiv v2:
  - p. 7, Definition 4 defines the leafwise geodesic flow;
  - p. 8, Definition 5 defines hyperbolic solenoidal surfaces of finite type;
  - pp. 12--13, Section 3.3 and Definition 7 define inverse limits of regular
    covers as McCord solenoids;
  - pp. 13--14 set up decreasing finite-index subgroups of a nonuniform
    lattice and their inverse-limit unit tangent bundles.
- Positioning effect: P27's noncompact object class and terminology are prior.
  The source studies horocycle dynamics and does not supply P27's exact
  `Gamma(3n!)` no-geodesic-period proposition.

### S4 — Hurder and Lukina

- DOI: https://doi.org/10.1090/tran/7339
- Technical text: https://arxiv.org/pdf/1702.03032
- Locator: p. 17, Definition 5.5 and the following paragraph identify the
  group-chain intersection with the corresponding leaf fundamental group.
- Domain caveat: the weak-solenoid setup assumes a closed compact base.  It is
  structural comparison evidence, not a replacement for P27's noncompact
  proof.

### S5 — Nica

- Record: https://arxiv.org/abs/1306.2385
- PDF: https://arxiv.org/pdf/1306.2385
- Locator: arXiv v1, p. 1, Introduction, displayed Theorem (Malcev 1940),
  with the residual-finiteness definition immediately following.
- Scope: an exposition of Malcev's residual-finiteness theorem for finitely
  generated linear groups and Selberg's lemma.
- Use: only the standard residual-finiteness input for the closed Fuchsian
  surface group.  The residual/homology tower and factorial period bound are
  proved locally.

## Claim-by-claim positioning result

```text
DIRECT_STRUCTURAL_PRIOR_FOUND=true
BROAD_APERIODICITY_NOVELTY_CLAIM=REJECTED
SIMPLY_CONNECTED_LEAF_MECHANISM_IS_PRIOR=true
NONCOMPACT_FINITE_TYPE_OBJECT_TAXONOMY_IS_PRIOR=true
ABSOLUTE_NOVELTY_CLAIM_ALLOWED=false
EXACT_GAMMA_3_FACTORIAL_ROLE=SEARCH_BOUNDED_SPECIALIZATION_ONLY
COMPACT_FACTORIAL_ROLE=LOCAL_QUANTITATIVE_CONTROL
```

The defensible contribution is the combination of:

1. one exact cusped specialization with a sign-sensitive residual proof;
2. one exact cocompact control with a factorial minimal-period lower bound;
3. a common owner theorem explaining why every fixed finite-level owner
   escapes a bounded time window; and
4. a deterministic firewall preventing finite-level data from being credited
   to a limit flow whose periodic set is empty.

## Reproducibility and human-source boundary

The Round-6 builder checks source URLs, locators, domain caveats, novelty
labels, the owner firewall, and the three-way decision.  It cannot verify that
the author personally read the cited passages.  Therefore:

```text
PRIMARY_SOURCE_WEB_VERIFIED_ROWS=9
HUMAN_CONFIRMATION_PENDING_ROWS=9
USER_ATTESTED_READ_ROWS=0
```

Eleven tests pass.  Two builds are byte-identical with artifact-tree SHA-256:

```text
53b8b332c09f771f97ad45a1504491a7e542d014a9d6ce677d3dc86851efeb5a
```

## Route consequence

The formal same-owner Route-A evaluation now records

```text
(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)
OVERALL=ROUTE_A_REJECTED
```

`A1_FAIL` follows from the proved identity `Per(M_infinity)=empty`.  A2 is not
a determinant campaign with a negative numerical score; it is not testable on
primitive orbits of this owner because there are none.  Finite-level or
renormalized tower objects would be different candidates and cannot inherit
credit.  Route B remains disallowed.
