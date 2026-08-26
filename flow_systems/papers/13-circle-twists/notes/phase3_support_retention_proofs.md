# Paper 13 Phase-3 support and retention proof record

Status: **FINAL — PASS TO INTEGRATED PHASE-3 PROOF REVIEW**  
Lane: P13-6--P13-8 retention/support proof and integrity audit  
Date: 2026-08-15 (Asia/Shanghai)  
`route_b_invocation_allowed: false`  
Standalone, Route, controls, manuscript, release, and public-sync authorization: **false**

This record proves the retention consequences P13-6/P13-7 from the exact
P13-3--P13-5 core conclusions bound and independently checked in Section 2,
and independently proves P13-8 from the frozen Paper-11/Paper-12 premises.
It does not enlarge the core claims, grant standalone status, or replace the
later integrated Phase-3 review.

## 1. Exact authority, scope, and owner firewall

The following controlling records were independently rehashed before this
proof was drafted:

| artifact | SHA-256 | use in this record |
|---|---|---|
| `notes/phase1_amendment_v1.md` | `ea5242ba6a8a1f2f867e8b258abc802fdeaace54db76629f0a9f0629e3e90d27` | exact objects, signs, named records, P13-6--P13-8 statements, and fail-closed branches |
| `notes/phase2_novelty_search.md` | `444507f623a998152fdc8e427ee8a3f917c11d5823278b110d431dbcacac6eea` | bounded precedent ceiling only |
| `notes/phase2_convention_owner_audit.md` | `498830945b10a9213da945710d21b7ea74d9e0747864e23ca6223efc9bb74f52` | signs, owners, restriction boundary, and corrected Austad locator |
| `notes/phase2_framework_source_audit.md` | `b47b1d6319c8419d96ca8679e3ff13b531a58f06a8b14afd95ec11f773345592` | source/companion ceilings and named-framework boundary |
| `notes/phase2_final_review.md` | `ffcfbac5768fc409b3fa9e5df4f3b46a2366f553373664c78f4364d456854cd9` | Phase-3 authorization, C0/M0/m0 |
| `notes/phase3_core_twist_proofs.md` | `62dac0782ba74fea9e8318e0835f7f20eede4cc9963c67471797a006b00decbd` | frozen P13-1--P13-5 proof dependency; 861 lines / 29,777 bytes |

The inherited companion bytes remain those rehashed by the final Phase-2
gate: Paper 9 manuscript `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb`,
Paper 11 manuscript
`eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002`,
and Paper 12 manuscript
`c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163`.

The proof uses only the strict category `Act_indisc(R)`: an object is a
nonempty globally indiscrete right `R`-set `X`, and a morphism is a strict
`R`-equivariant bijection. Its actual range-first groupoid is

```text
G_actual(X)=X x R,
r(x,t)=x,  s(x,t)=x.t,
(x,t)(x.t,u)=(x,t+u).
```

No conclusion below asserts that two nonisomorphic actions are isomorphic,
that this category is connected, or that every conceivable invariant is
constant. “Universal constancy” means only that, after the expressly
registered owner/provenance tags are forgotten, each of the named outputs in
Section 3 takes one common isomorphism-class value on every registered input.
Strict morphisms provide naturality where they exist; they are not used to
manufacture morphisms between unrelated actions.

## 2. Exact core-proof dependency bind for P13-6/P13-7

For an object `X`, Paper 12 gives the unique time factorization

```text
sigma(x;t,u)=sigma_0(t,u)
```

for every globally continuous normalized circle cocycle on `G_actual(X)`.
I independently rehashed and read the complete frozen core proof. The
load-bearing conclusions for P13-6/P13-7 are:

1. **Continuous triviality and uniqueness.** For every normalized continuous
   `sigma_0:R^2->T`, there is a normalized continuous `alpha:R->T` with
   `sigma_0=delta alpha`, where

   ```text
   (delta alpha)(t,u)=alpha(t)alpha(u)overline{alpha(t+u)}.
   ```

   If `beta` is another such trivializer, then `beta/alpha` is a continuous
   character of `R`.
2. **Author test-algebra gauge map.** With the frozen orientation
   `sigma overline{tau}=delta a`, multiplication by time,
   `(U_a^X F)(x,t)=a(t)F(x,t)`, is a star-isomorphism
   `A_sigma(X)->A_tau(X)` on the Paper-11 author global-QC domain.
3. **Transported norm closure.** For `sigma_0=delta alpha`, `U_alpha^X`
   identifies the author full and reduced transported norms with the
   corresponding restrictions of the standard one-object time-group norms;
   a change `alpha->beta` acts by a continuous character and is isometric for
   both records. Their completions are therefore choice-independent author
   records. Equality of the full and reduced records is invoked only after
   this identification, from amenability of the standard group `R`.

The exact core locators are Theorem 5.1 for item 1; Lemma 6.4 together with
the actual-domain transport (6.10) for item 2; and Propositions 7.4--7.5 plus
Theorem 7.6 for item 3. I independently checked the phase lift, real-cocycle
splitting `q=delta(h-A)`, frozen sign, character quotient, gauge product/star
identities, actual `Phi` transport, regular intertwiner, standard-norm
restriction, and character isometries used by those conclusions. No gap or
owner transfer was found in this dependency slice.

These are typed proof inputs, not source substitutions: Sorkin is only the
prior-art sentinel for the first existence statement, and the standard group
sources own no actual non-Hausdorff action-groupoid completion. The stable
hash above therefore closes the dependency bind for Sections 3--5; the later
integrated Phase-3 review remains a separate pipeline gate.

## 3. P13-6 — universal constancy of exactly the named records

Fix any two registered pairs `(X,sigma)` and `(Y,tau)`. Write their unique
time factors as `sigma_0` and `tau_0`, and choose core-certified continuous
normalized trivializers

```text
sigma_0=delta alpha,    tau_0=delta beta.
```

### 3.1 `TIME-GAUGE`

By definition, `TIME-GAUGE(X,sigma)` is `[sigma_0]` in the one common
abstract group `H^2_tw(R;T)`. Since `sigma_0=delta alpha`,

```text
TIME-GAUGE(X,sigma)=[sigma_0]=0.
```

The same computation gives `TIME-GAUGE(Y,tau)=0`. Thus this registered output
is the constant zero element of the common abstract quotient. No quotient
topology is used or asserted.

### 3.2 `ACTUAL-TW-TEST`

Let

```text
Phi_X:C_c(R)->Cglob(G_actual(X)),   Phi_X(f)(x,t)=f(t)
```

be the Paper-11 time-function bijection, and define `Phi_Y` similarly. On the
untwisted author domains,

```text
I_XY = Phi_Y o Phi_X^{-1}:A_1(X)->A_1(Y)
```

is the time-only star-isomorphism. It does not identify the action
owners; it only identifies their registered author time-function algebras.
The composite

```text
Theta_XY
  = (U_beta^Y)^(-1) o I_XY o U_alpha^X
  : A_sigma(X) -> A_tau(Y)
```

is a star-isomorphism. Hence every registered author twisted global-QC test
algebra has the same `ACTUAL-TW-TEST` star-isomorphism class.

Different choices of `alpha` or `beta` can change the displayed representative
by a character automorphism; they do not change its star-isomorphism class.
The statement is therefore constancy of a class, not uniqueness of a
preferred inter-owner isomorphism.

### 3.3 `ACTUAL-TW-FULL` and `ACTUAL-TW-RED`

The core norm identifications make `U_alpha^X` isometric from the two
`sigma`-transported author normed algebras to the untwisted time records, and
similarly for `U_beta^Y`. Consequently `Theta_XY` extends by completion to
isometric star-isomorphisms

```text
TW-FULL-TRANSPORT_X(sigma)  ~=  TW-FULL-TRANSPORT_Y(tau),
TW-RED-TRANSPORT_X(sigma)   ~=  TW-RED-TRANSPORT_Y(tau).
```

If a trivializer is replaced, its ratio with the old one is a continuous
character, and the core package proves the induced character multiplier is
isometric for each norm. Thus neither completed class depends on the action,
the twist, or the trivializer. The full and reduced outputs remain separately
typed registered records even though, after the standard time-group
identification, amenability of `R` makes their norms equal. They are not
renamed as actual-groupoid C-star algebras.

### 3.4 Strict-morphism naturality and the exact constancy ceiling

If `b:X->Y` is a strict `R`-equivariant bijection, then

```text
B:G_actual(X)->G_actual(Y),    B(x,t)=(b(x),t)
```

is an algebraic groupoid isomorphism and a homeomorphism. It commutes with
the time projections, and pullback satisfies

```text
B^*Phi_Y(f)=Phi_X(f),
B^*(tau_0 o pi_2)=tau_0 o pi_2.
```

Therefore the reductions and gauge maps above commute with every strict
morphism. For objects joined by no strict morphism, constancy follows from
the common time-algebra representatives, not from a false claim of action
equivalence.

The proof has now exhausted the registered action-blind outputs:

1. `TIME-GAUGE`;
2. `ACTUAL-TW-TEST`;
3. `ACTUAL-TW-FULL`; and
4. `ACTUAL-TW-RED`.

It says nothing about unnamed invariants, literal stabilizers, marked clocks,
orbit sets, action conjugacy, owner identity, or representations.

## 4. Typed isotropy restrictions — zero class without erasing `H_x`

For a fixed object, unit `x`, and its literal subgroup

```text
H_x=Stab_R(x)={h in R:x.h=x}
```

give `H_x` its literal subspace topology from `R`. The time factorization and
global trivializer give, for `h,k in H_x`,

```text
sigma(x;h,k)=sigma_0(h,k)
            =alpha(h)alpha(k)overline{alpha(h+k)}
            =delta_(H_x)(alpha|_(H_x))(h,k).
```

The restriction `alpha|_(H_x)` is continuous and normalized. It is one of
the allowed continuous normalized one-cochains in the definition of the
typed quotient. Therefore

```text
ISOTROPY-TWIST(x)
  = Res_x([sigma])
  = [sigma|_(H_x x H_x)]
  = 0 in H^2_tw(H_x;T).
```

This equality is internal to the quotient typed by the already supplied
literal subgroup. Zeros attached to different subgroups lie in differently
typed quotients and are not thereby identified. In particular, the equation
does not erase, reconstruct, or compare:

- the literal set/subgroup `H_x`;
- its embedding in `R` or its subspace topology;
- a marked generator, period, or clock;
- the orbit/action carrying it; or
- any representation or completion associated with it.

Nor does the argument prove `H^2_tw(H_x;T)=0` for every intrinsic cocycle on
`H_x`; it proves only that the restriction of a globally trivialized
Paper-13 cocycle represents zero.

### Dense-subgroup boundary

For the adversarial literal stabilizer `H_x=Q subset R`, the same restriction
calculation is valid: `alpha|_Q` is continuous for the subspace topology and
trivializes the restricted cocycle. That is the entire licensed conclusion.
This record invokes no locally compact group theorem, Haar measure, regular
representation, twisted `L^1` algebra, or C-star completion on the dense
nonclosed subgroup. In particular, no finite approximation or rational
window is allowed to promote this cochain calculation into an analytic
statement.

## 5. P13-7 — fixed-prime, same-owner negative conclusion

Fix one prime `p` and keep the registered owner
`G_p_actual=Gamma_p_actual semidirect R` fixed. The inherited premise supplies
the same literal stabilizer at every unit,

```text
H_x=(log p)Z,
```

and supplies no twist. Applying Sections 3--4 on this same owner gives:

- its `TIME-GAUGE` value is zero;
- every author twisted test algebra is in the same registered
  `ACTUAL-TW-TEST` class as the untwisted one;
- its two transported completion records are in the same respective
  isometric star-isomorphism classes; and
- for every unit, the restricted scalar cocycle is zero in the quotient
  typed by the already registered literal `(log p)Z`.

Thus, **conditional on the fixed registered owner and the literal stabilizer
`H=(log p)Z`, the scalar twist supplies no additional registered continuous
cohomology-class invariant.** This is a same-owner negative. It neither
compares different primes nor derives `p`, the period, the action, an orbit
count, or arithmetic structure from a twist. It also does not quantify over
every conceivable invariant.

## 6. P13-8 setup — actual global-QC support and the `J` pullback

Now let `X` have one common cocompact stabilizer

```text
H=LZ,    L>0,
```

and let `Q=X/R` be its nonempty **bare** orbit set. Paper 12 constructs

```text
Std(X) = coproduct_(q in Q) O_q,    O_q ~= R/H,
G_std(X)=Std(X) semidirect R,
J:G_std(X)->G_actual(X),
```

where every `O_q` is a nonempty compact Hausdorff torsor and `J` is the
continuous identity on the underlying arrows. The direction is essential:
pullback is

```text
J^*:C(G_actual(X))->C(G_std(X)),    J^*F=F o J.
```

For `f in C_c(R)`, let `K=supp_R(f)` and set

```text
Phi_actual(f)(x,t)=f(t).
```

Paper 11 gives the exact actual support

```text
supp_actual(Phi_actual(f))=X x K
```

and its quasi-compactness by the actual projection criterion. Thus
`Phi_actual(f)` belongs to the author global-QC test space for every
`f in C_c(R)`, including `f=0` (empty support).
This is the actual owner's quasi-compact-support statement; it is not
silently upgraded to Hausdorff compact support.

Since `J` is identity-on-carrier,

```text
Psi_X(f):=J^*Phi_actual(f),    Psi_X(f)(x,t)=f(t).
```

This function is continuous on the standard arrow space. Its nonzero locus
is `Std(X) x {t:f(t)!=0}`. For any space `Z` and nonempty `Z`, the closure of
`Z x A` in `Z x R` is `Z x closure(A)`: the forward inclusion is immediate,
and every basic neighborhood of `(z,t)` with `t in closure(A)` meets
`Z x A`. Hence

```text
supp_std(Psi_X(f))=Std(X) x K
  = coproduct_(q in Q) (O_q x K).                 (6.1)
```

The equality also holds for `f=0`, when both sides are empty.

## 7. P13-8 compact-support equivalence

### 7.1 Zero function

If `f=0`, then `K` and the support in (6.1) are empty. The empty set is
compact for every orbit set `Q`, finite or infinite. Therefore
`Psi_X(0) in C_c(G_std(X))` without an orbit-count hypothesis.

### 7.2 Nonzero function and finite `Q`

Suppose `f!=0`. Then `K` is nonempty compact Hausdorff. If `Q` is finite,
every `O_q x K` is compact Hausdorff, and (6.1) is a finite union of such
sets. It is compact. Therefore `Psi_X(f)` is continuous and compactly
supported, hence belongs to `C_c(G_std(X))`.

### 7.3 Nonzero function and infinite `Q`

Suppose again that `f!=0`, so `K` is nonempty, and now let `Q` be infinite.
Inside the support `S=Std(X) x K`, set

```text
V_q = S intersect (O_q x R) = O_q x K.
```

Every `V_q` is open in `S`, because each coproduct summand `O_q` is open in
`Std(X)`. Every `V_q` is nonempty, and `{V_q:q in Q}` covers `S`. A finite
subfamily indexed by `q_1,...,q_n` misses `V_q` for any
`q outside {q_1,...,q_n}`. Thus the cover has no finite subcover. The support
is not quasi-compact and therefore is not compact. Consequently
`Psi_X(f)` does not belong to `C_c(G_std(X))`.

This is an actual infinite-coproduct proof; it uses no finite diagnostic,
enumeration, countability assumption, or limit heuristic.

### 7.4 Exact theorem and strongest image/intersection form

The preceding three cases prove

```text
Psi_X(f) in C_c(G_std(X))  iff  f=0 or Q is finite.          (7.1)
```

Let

```text
T_X := J^*Phi_actual(C_c(R)) subset C(G_std(X)).
```

Because `Std(X)` is nonempty, `Psi_X` is injective. Therefore (7.1) is
equivalent to the stronger exact statement, inside `C(G_std(X))`,

```text
T_X intersect C_c(G_std(X))
  = T_X,    if Q is finite,
  = {0},    if Q is infinite.                               (7.2)
```

In particular, for infinite `Q` the cochain/function pullback remains a
well-defined continuous time-only function, but no nonzero author global-QC
time function lands in the standard compact-support test space.

## 8. Gauge invariance of support and of the intersection

Let `a:R->T` be any allowed continuous circle-valued time gauge. It is
nowhere zero. Hence, for every `f in C_c(R)`,

```text
{t:a(t)f(t)!=0}={t:f(t)!=0},
supp_R(af)=supp_R(f).
```

Moreover `af in C_c(R)`, and multiplication has inverse multiplication by
`overline a`. On the time-only standard image,

```text
M_a Psi_X(f)=Psi_X(af).
```

Thus `M_a(T_X)=T_X` and

```text
M_a(T_X intersect C_c(G_std(X)))
  = T_X intersect C_c(G_std(X)).                            (8.1)
```

The finite-orbit criterion, the full-image branch for finite `Q`, and the
zero-intersection branch for infinite `Q` are all gauge invariant. This is a
support statement for a proved circle-valued gauge; it would be false for a
general multiplier allowed to vanish, which is outside the registered
cochain domain.

## 9. Finite-`Q` test-function star map — and no completion claim

This optional strengthening is licensed only at test-function level. Assume
`Q` is finite and let the time cocycle be `sigma_0`. Pull it back to the
standard action groupoid through the time composable-pair projection. The
standard range fibres carry Lebesgue measure, and the direct twisted
test-function formulas are

```text
(F *_sigma^std G)(x,t)
  = integral_R F(x,u)G(x.u,t-u)sigma_0(u,t-u) du,

F^{*sigma,std}(x,t)
  = overline{sigma_0(t,-t)} overline{F(x.t,-t)}.
```

For `f,g in C_c(R)`, direct substitution gives

```text
Psi_X(f) *_sigma^std Psi_X(g)=Psi_X(f *_sigma_0 g),
Psi_X(f)^{*sigma,std}=Psi_X(f^{*sigma_0}).                   (9.1)
```

The core P13-4 closure theorem puts the two scalar right-hand sides back in
`C_c(R)`. Because `Q` is finite, Section 7 then puts every term in the
standard compact-support test space. Hence

```text
Psi_X:A_sigma -> C_c(G_std(X),sigma)
```

is an injective star-homomorphism onto the **time-only
(unit-coordinate-constant) subalgebra** `T_X`; it is not asserted to be onto
the full standard groupoid test algebra. Equation (9.1) is the end of the
licensed analytic statement.
It yields no norm comparison, completion homomorphism, full/reduced theorem,
or actual-to-standard groupoid C-star identification.

When `Q` is infinite, (7.2) shows that the analogous continuous pullback has
zero intersection with the standard compact-support space. Thus there is no
nonzero test-space map of this form to extend; cochain pullback and pointwise
gauge multiplication nevertheless remain continuous.

## 10. Fixed-prime P13-8 specialization

For the fixed-prime packet, substitute only the registered data

```text
H=(log p)Z,    Q=Q_p,
```

where `Q_p` is a nonempty bare orbit set. Since `log p>0`, the stabilizer is
of the common cocompact-lattice form required above. Therefore

```text
J^*Phi_actual(f) in C_c(G_std(Gamma_p))
  iff f=0 or Q_p is finite,                                 (10.1)
```

and, for nonzero `f`, transfer holds iff `Q_p` is finite. Equivalently, its
time-only image/intersection has the two conditional branches in (7.2).

This proof assigns no truth value to “`Q_p` is finite,” assigns no cardinality
or enumeration to `Q_p`, equips it with no actual quotient topology or
measure, and imports no arithmetic conclusion. Equation (10.1) is a
conditional substitution into a generic owner theorem, nothing more.

## 11. Adversarial proof controls

| control | exact result | false inference blocked |
|---|---|---|
| singleton `X={*}` in P13-6 | exactly the Hausdorff one-object time group; all four named records have the common value | no universal claim that every actual owner is non-Hausdorff |
| two actions with no strict isomorphism | named output classes still share the common time representative | constancy is not action equivalence or connectedness of `Act_indisc(R)` |
| heterogeneous stabilizers `{0}`, `LZ`, `R`, and dense `Q` | each globally restricted cocycle is zero in its own typed quotient | zeros do not identify literal subgroups or prove a common-period theorem |
| dense literal `H=Q` | restriction-cochain calculation only | no Haar, regular, `L^1`, or C-star promotion |
| `f=0`, arbitrary orbit set | standard support is empty and compact | prevents the false converse “compact pullback implies `Q` finite” without the nonzero qualifier |
| `f!=0`, one orbit | one compact component, so transfer succeeds | validates the singleton orbit-set edge of the finite branch |
| `f!=0`, finite `Q` | finite union of compact nonempty components | no dependence on an enumeration or equal component size |
| `f!=0`, infinite `Q` | explicit open-component cover has no finite subcover | no finite computation is substituted for the infinite proof |
| noncocompact `H={0}` with `f!=0` | `R/H=R` is noncompact; finite `Q` alone does not prove compact support | shows the common cocompact lattice hypothesis is load-bearing |
| dense nonclosed `H=Q` in P13-8 position | excluded from the `H=LZ` standard compact-orbit theorem | no conflation of dense-isotropy cochains with support transfer |
| heterogeneous action in P13-8 position | excluded: no common `H=LZ` owner is registered | no mixing of orbitwise types under one coproduct formula |
| nowhere-zero circle gauge | support is exactly invariant | no extension to scalar multipliers with zeros |
| excluded `R^2` multiplier | outside the one-dimensional P13-3 dependency | no dimension-free cohomology-collapse claim |
| fixed-prime substitution | conditional on bare `Q_p` only | no cardinality, topology, measure, or arithmetic promotion |

### Post-core P13-8 regression receipt

The frozen core proof does not alter the support theorem's domain or
topological calculation. Its equations (6.1)--(6.2) use the same time
product/star as Section 9 above; its actual transport (6.10) uses the same
`Phi_actual`; and Lemma 6.4 proves that every allowed gauge is
support-preserving because it is circle-valued. Re-substitution into (9.1)
reproduces both test-function identities without a sign or owner change.
The compactness proof in Sections 6--8 still depends only on the closure of
the nonzero locus, the bare-set finite/infinite split for `Q`, and the
Paper-12 coproduct topology. Thus the core bind introduces no regression in
the zero, finite, infinite, gauge, intersection, or fixed-prime branches.

## 12. Claim delta, nonredundancy ceiling, and disposition

| claim | inherited/source-owned part | author-owned proof in this record | strongest licensed conclusion |
|---|---|---|---|
| P13-6 | Paper-12 time factorization plus the exact P13-3--P13-5 core closure | explicit inter-owner star/isometric maps; strict-morphism naturality; typed isotropy restriction | only the four named action-blind records are constant; literal stabilizers remain typed |
| P13-7 | Paper-9 fixed-prime owner and literal `(log p)Z`; generic P13-6 proof | same-owner restriction and negative conclusion | scalar twist adds no registered cohomology-class invariant, conditional on owner and literal `H` |
| P13-8 | Paper-11 actual QC support; Paper-12 same-carrier standardization and `J` direction; elementary compactness | zero/finite/infinite iff, infinite coproduct cover, exact image/intersection, gauge invariance, finite-`Q` test star map, conditional packet branch | a proved cross-topology support obstruction at ordinary/test-function level only |

The bounded search result remains exactly
`SUPPORTED_WITHIN_SEARCH / NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH`.
It is not an absence proof, novelty certificate, or priority claim. Arm A is
prior art in substance. P13-8 combines inherited facts across two differently
typed topology owners, but the compactness step is elementary. This proof
record does not decide whether that dependency break has enough substantive
weight for a standalone paper.

Accordingly:

```text
STANDALONE_PASS=false
ROUTE_B_INVOCATION_ALLOWED=false
```

An independent post-proof nonredundancy/standalone reviewer must decide
whether P13-8 is nonformal and central. If it is judged a routine/direct
restatement of the inherited Paper-11/Paper-12 facts, if a direct package
precedent is later found, or if any required proof dependency fails, the
binding disposition remains `NOTE_OR_MERGE`.

## 13. Lane verdict and remaining gate

- **P13-8 mathematical verdict:** PASS; the exact theorem, image/intersection
  strengthening, gauge invariance, finite-`Q` test-level star map, infinite
  zero intersection, and fixed-prime conditional are proved above.
- **P13-6/P13-7 verdict:** PASS, bound to the frozen core proof SHA-256 in
  Section 1 and the independently checked dependency slice in Section 2.
- **Final lane binding:** FROZEN for integrated Phase-3 proof review.
- **Final finding count:** C0 / M0 / m0.

No controls were run, no Route or manuscript artifact was created, and no
standalone, completion, release, Git, or public-synchronization authorization
is granted by this record.
