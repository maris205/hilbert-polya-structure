# Paper 12 Phase-1 design amendment v1

Amendment date: **2026-08-15 (Asia/Shanghai)**  
Status: **CONTENT AMENDED — INDEPENDENT EXACT-BYTE RE-LOCK PENDING**

## 1. Superseded initial tuple

The three independent initial reviews audited these exact bytes:

| Artifact | SHA-256 |
|---|---|
| `research_protocol.md` | `1ea7e67825d5f543f472e1f4e0b3ea57a986269b24ec8dad1bf533475cc860eb` |
| `candidate_lock.md` | `6a03983a76d34937f01ff03da4d074d1111b0722afff417a4532c5d7744f2975` |
| `pipeline_state.md` | `4fe89540fb743e757e45ce71569261659a0d780db0c79ee5867792fe8ac936c0` |

Their independent verdicts were:

| Review | Verdict | SHA-256 |
|---|---|---|
| methodology/nonredundancy | `REVISE C0/M6/m2` | `797e194f9b02f236c5c5b103cac09b63a55078f46b3a269ccea3ebfc61775008` |
| devil's advocate/domain | `REVISE C1/M5/m3` | `f861957d59ff63ccc1aa3328c3bcb2c8a293d2115f69f845f0ae4f77e3ab11cf` |
| source/scope feasibility | `REVISE C0/M4/m2` | `e7bc2e3dbf78f415bf57d59d66314ce338c24ac90993e99ab178cc128f30ec32` |

Those reports remain the immutable history of the initial design. This
amendment does not revise their findings or verdicts.

## 2. Core logical correction

The initial primary question incorrectly suggested an iff-like boundary:
that exact period preservation occurs precisely for strict marked morphisms
and is lost under every scaled or unmarked equivalence. Amendment v1 replaces
that false claim by the exact theorem signature

```text
c' o F=alpha c
  => Per_(F_0(x))([c'])=alpha Per_x([c]).
```

Strict marked maps are the `alpha=1` sufficient case. The weaker-category
claim is existential non-descent: explicit unequal-period objects are
isomorphic after scaling or forgetting the mark. It is not universal loss.
The frozen orientation-reversing control preserves `LZ` while sending
`c` to `-c`, and trivial/free/dense-period controls make the same distinction.

## 3. Typed cohomology repair

The coefficient datum is now the constant bundle

```text
underline(A)_X=X x A -> X,
gamma.(s(gamma),a)=(r(gamma),a).
```

The complex is named the **Paper-12 author-defined continuous unnormalized
nerve complex**. Degenerate simplices remain; all cochain groups use
pointwise addition. The face maps and alternating differential are explicit.
`Z=ker d`, `B=im d`, and `H=Z/B` are algebraic abelian groups, and real
vector spaces for `A=R`; no cochain-space or quotient topology is claimed.
The fail-closed notation `C_cnv/H_cnv` remains until Phase 2 proves exact
agreement with a named published theory at matching hypotheses.

Time projection is now correctly typed contravariantly:

```text
T_n=pi_n^*:C_cnv^n(R;A)->C_cnv^n(G;underline(A)).
```

Evaluation at a chosen unit is only the inverse after the all-degree `T0`
factorization theorem proves unit independence.

## 4. Owner and source-credit split

The amendment separates:

```text
G(X,alpha)                     generic indiscrete R-action;
G_(p,a)^orb=X_(p,a) rtimes R  actual fixed orbit;
G_p^pkt=Gamma_p rtimes R      actual fixed-prime packet;
G^global                      excluded full suspension.
```

Deninger owns the source flow, packet membership, `p^Z`, and logarithmic
clock at physical pp. 38--39, Section 6/Theorem 6.1. Paper 9 owns the actual
inherited orbit/packet topology. Paper 11/Paper 12 own the transformation-
groupoid definition. Paper 12 owns only the proposed cochain/category/period
constructions. The packet corollary must verify the same restricted action,
normalized clock, and common stabilizer at every packet unit or return
`ORBIT_ONLY`; no global/cross-prime theorem is allowed.

## 5. Class-dependent period and normalized quotient

The amendment first defines `res_x` on cocycles, then proves coboundaries
restrict to zero, and only afterward defines
`Per_x([b])=image(res_x(b))`. Every covariance formula uses the transported
unit `F_0(x)`.

The standard action-orbit quotient is restricted to normalized coordinate
marks `c(x,t)=t`, where `Per_x([c])=Stab_R(x)`. For arbitrary
`[b]=lambda[c]`, `R/Per_x([b])` is only a value-space quotient and is not used
to parametrize the action orbit.

## 6. Categories and functor

The strict, positive-scaled, and unmarked categories now have explicit
objects, topological groupoid isomorphisms, unit maps, scale labels,
identities, composition, and inverses. The strict normalized functor targets
pointed standard Hausdorff homogeneous spaces `(R/H,[0])`, sends
`F` to `[t]|->[t]`, and has explicit well-definedness, identity,
composition, naturality, and basepoint-rotation obligations. Positive
dilation is a separate semilinear map, not a strict target morphism.

## 7. Deterministic controls

The unfrozen random language is removed. Exact controls are `TRIV-2`,
`FREE-R`, `PER-L` with `L in {log 2, log 4, sqrt(2),37/29}`, `DENSE-Q`,
`NONTRANS-1-2`, `NON-T0-A2`, `SCALE-LM`, `REVERSE-L`, and `LABEL-SWAP`.
Carrier sets, actions, coefficient group, witnesses, expected outcomes,
paths, optional reserved seed `120012`, exact/`1e-12` tolerance boundary,
manifest fields, at least 30 tests, strict verify-only mode, two fresh
byte-identical generations, tamper/drift rejection, and cache hygiene are
frozen before Phase 3.

## 8. Standalone, source, and novelty gates

A preregistered Paper-9--11 delta matrix now assigns every Paper-12 target an
inherited premise and a distinct new obligation. `STANDALONE_PASS` requires
the all-degree natural chain theorem, typed covariance/non-descent theorem,
normalized strict quotient functor, packet decision, deterministic controls,
and nearest-precedent audit. `NOTE_OR_MERGE` is mandatory if the work reduces
to Paper-11 arrow factorization plus a routine bar-complex corollary and
Deninger's stabilizer, or if direct precedent absorbs the categorical result.

Phase 2 has a fixed comparator set, cutoff, endpoints, query families,
inclusion/exclusion rule, source-hypothesis ceilings, and
`SUPPORTED_WITHIN_SEARCH` vocabulary. It must not promote author-defined
cohomology to a standard theory or infer priority from an exact-string zero.

## 9. Route and release repairs

The later Route-A evaluation now has every mandatory input field, including
the present negative convention
`NONE_BY_DESIGN_NO_DETERMINANT_OBJECT`, exact cutoff/precision/data split,
forbidden data, and artifact paths. A period subgroup alone does not satisfy
the A1 primitive-orbit obligations. A2/A3/A4 remain negative ceilings; Route
B is false and no Route-B YAML is permitted.

The release boundary distinguishes the generated manuscript PDF from local
source evidence, forbids public `notes/sources/*.pdf`, requires canonical
bibliographic endpoints rather than local hashes, handles unpublished
companion dependencies honestly, and requires an enumerated zero-source-PDF
public-sync dry run.

## 10. Amended content tuple submitted for re-lock

| Active artifact | SHA-256 |
|---|---|
| `research_protocol.md` | `a923bfcf5fbae2d3136632794f0eb68ce4b7e48f217f0a071295e9fe4a85dda5` |
| `candidate_lock.md` | `0932d8a388ce732a3ad0702f3703cc91088d2fa73cc02f0a8063d240d70f5a42` |
| `pipeline_state.md` | `9cb7c51c534fd26f68fb66853312b022202c1d58b0ff2d74910c4deb3b32059b` |

The amendment file is the version ledger for this tuple. The three active
hashes must remain exact during independent re-lock. The reviewers must also
bind the final hash of this amendment itself.

## 11. Non-claim

Amendment v1 closes design ambiguity only. It proves no `P12-*` target,
certifies no source equivalence or novelty, creates no Route verdict, and
does not authorize Phase 2 until methodology, devil/domain, and source/scope
reviewers independently return `PASS C0/M0/m0` on the exact amended tuple.
