# Paper 13 Phase-3 standalone amendment v2 — continuum orbit set and diagonal corona

Status: **CANDIDATE DESIGN — independent source/domain/methodology re-lock required**  
Date: **2026-08-15 (Asia/Shanghai)**  
Scope: versioned theorem and owner design only; no proof, controls, Route YAML,
manuscript, or release authorization

## 1. Authority, purpose, and narrow precedence

This amendment responds to the binding independent standalone disposition

```text
NOTE_OR_MERGE, C0/M1/m0
```

in `notes/phase3_standalone_review.md`.  The frozen P13-1--P13-8 proofs remain
mathematically valid.  The finding is not repaired by relabelling them: the
conditional compact-support statement is a direct Paper-11/Paper-12
corollary and does not by itself support a standalone article.

The exact reviewed inputs are:

| artifact | SHA-256 | role |
|---|---|---|
| `notes/research_protocol.md` | `519563a28c3f11e3b3853f6875a84191444a68cd2c032c4cfcf69ca4152d5064` | active base protocol |
| `notes/candidate_lock.md` | `8cc0d08971762aa784afe1c844215353f170a75a3c0ab892415458ab010d0266` | active base candidate |
| `notes/phase1_amendment_v1.md` | `ea5242ba6a8a1f2f867e8b258abc802fdeaace54db76629f0a9f0629e3e90d27` | signs, owners, and original P13-8 |
| `notes/phase2_final_review.md` | `ffcfbac5768fc409b3fa9e5df4f3b46a2366f553373664c78f4364d456854cd9` | original source/proof authorization |
| `notes/phase3_core_twist_proofs.md` | `62dac0782ba74fea9e8318e0835f7f20eede4cc9963c67471797a006b00decbd` | proved P13-1--P13-5 interface |
| `notes/phase3_core_peer_review.md` | `a96a91adb1474062656cbca4d677019f952b5fb84775bda952b6c996a700e665` | independent core PASS |
| `notes/phase3_support_retention_proofs.md` | `f8a0672026b2efaaf07af20d90a17e870e8d0e2f849af0eb78d6dcb1573fb811` | proved P13-6--P13-8 interface |
| `notes/phase3_support_peer_review.md` | `ded657fb7022114527e99a8c0bc12d9f70d9b4ca3f976a6335065190d0640bed` | independent support PASS |
| `notes/phase3_standalone_review.md` | `0397e1555a1ff07d30f06c3182b6cf570228ccd3e8db9e3c96666d118079c224` | binding M1 to repair |

This amendment supersedes only:

1. the unresolved finite/infinite fixed-prime branch of original P13-8;
2. the statement that test-function support is the terminal comparison;
3. the descriptions, but not the number, of Route owners 8 and 9; and
4. the sufficiency of the already reviewed v1 control design for the enlarged
   theorem package.

All earlier signs, gauge directions, actual-owner firewalls, source-credit
ceilings, and Route-B prohibition remain binding.  Arm A remains prior art in
substance and earns no standalone credit.

## 2. Four owner levels that must never be conflated

Fix a rational prime `p`.  Retain the Paper-9 bare-set identity

```text
Q_p  ~=_set  U_p/H_p,
U_p  = product_(ell != p) Z_ell^x,
H_p  = p^Zhat subset U_p.
```

The following are four different owners of related data.

1. `Q_p^actual` is the intrinsic actual time-orbit quotient with its Paper-9
   indiscrete topology.  It is nonempty, nontrivial, and second countable
   (the two-element family `{empty,Q_p}` is a base), despite the cardinality
   theorem proposed below.  It is not Hausdorff.
2. `Q_p^bare` is only the underlying orbit-index set.  Cardinality statements
   in this amendment are statements about this bare set.
3. `Std(Gamma_p)` is the Paper-12 same-carrier orbitwise standardization

   ```text
   Std(Gamma_p)=coproduct_(q in Q_p^bare) O_q,
   O_q ~= R/(log p)Z.
   ```

   Its orbit components are open compact Hausdorff torsors.
4. `Q_p^disc` is the discrete component/orbit quotient of `Std(Gamma_p)`.

No topology is transported from items 3--4 to items 1--2.  The proposed
non-second-countability and non-sigma-compactness conclusions apply only to
`Std(Gamma_p)`, its standard arrow space, and `Q_p^disc`; they do not apply to
the actual indiscrete quotient.

## 3. P13-8A — exact fixed-prime cardinality theorem

Let `I_p` be the countably infinite set of odd rational primes different from
`p`, and define the sign subgroup

```text
S_p=product_(ell in I_p) {+1,-1} subset U_p.
```

The direct proof obligation is:

1. `|S_p|=2^aleph_0`.
2. `H_p` is procyclic, as already proved on the Paper-9 owner, and therefore
   has at most one nonidentity element of order two.
3. Every element of `S_p` has order at most two, so

   ```text
   |S_p intersect H_p| <= 2.
   ```

4. The fibres of `S_p -> U_p/H_p` are cosets of `S_p intersect H_p`, hence
   have size at most two.  Therefore `|U_p/H_p|>=2^aleph_0`.
5. The countable product `U_p=product_(ell!=p)Z_ell^x` has cardinality at
   most `(2^aleph_0)^aleph_0=2^aleph_0`.

The exact candidate conclusion is

```text
|Q_p^bare|=|U_p/H_p|=2^aleph_0.                 (P13-8A)
```

This is a set theorem on the exact Paper-9 owner.  It uses no Haar measure,
quotient topology, separability inference, orbit enumeration, or continuum
hypothesis.

Consequently the already proved original P13-8 theorem specializes
unconditionally: for every nonzero `f in C_c(R)`,

```text
J_p^* Phi_actual(f) notin C_c(G_std(Gamma_p)),
T_p intersect C_c(G_std(Gamma_p))={0}.            (P13-8A-support)
```

The same cardinality gives:

- `Q_p^disc` is not second countable and not sigma-compact;
- `Std(Gamma_p)` is not second countable and not sigma-compact; and
- its arrow space `Std(Gamma_p) x R` has the same two failures.

The proofs must use the uncountable family of nonempty open components and
the fact that a compact subset of a coproduct meets only finitely many
components.  These topology facts are not framework-nonexistence claims.

## 4. Component twisted completions for an arbitrary common-lattice owner

Let `X` be a nonempty globally indiscrete right-`R` set whose every
stabilizer is the same cocompact lattice `H=LZ`, `L>0`.  Let

```text
Q=X/R,
Std(X)=coproduct_(q in Q) O_q,
O_q ~= R/H.
```

Let `sigma:R^2->T` be a continuous normalized multiplier.  The time test
algebra `A_sigma=C_c(R)` has exactly the product and star frozen in P13-4.
Its full and reduced completions are denoted

```text
C^*_(max)(R,sigma),    C^*_r(R,sigma).
```

They are standard one-object real-group completions.  P13-3--P13-5 prove
that each is gauge-isomorphic to its untwisted counterpart, that the two
norms agree, and that the actual author completions are isometrically the
same time records.

For each standard orbit `O_q`, use the exact standard transformation-groupoid
test algebra

```text
C_c(O_q semidirect R,sigma)
```

with Lebesgue range-fibre measure and the P13-4 product/star signs.  Define
the **component records**

```text
B_(q,sigma)^max = universal completion of C_c(O_q semidirect R,sigma),
B_(q,sigma)^r   = unit-regular completion of C_c(O_q semidirect R,sigma).
```

These are ordinary compact-orbit Hausdorff records.  No origin of the torsor
`O_q` is chosen in their definition.  Identifying all components with one
model `R/H` is noncanonical and is unnecessary.

For either `epsilon in {max,r}`, define the author componentwise standard
record

```text
A_(std,sigma)^epsilon
   := direct_sum_(q in Q)^c0 B_(q,sigma)^epsilon.   (4.1)
```

Equation (4.1), not a product, is the definition for arbitrary, possibly
uncountable `Q`.  It is deliberately owner-safe.  This amendment does not
claim that non-second-countability prevents a global groupoid construction:
Buss--Holkar--Meyer explicitly treats nonseparable groupoid C-star algebras
without a second-countability hypothesis in its audited untwisted setting.
The componentwise definition is retained because the exact global **twisted**
framework and its conventions have not yet been source-cleared, not because
such a framework is universally impossible.

## 5. P13-8B — faithful time diagonal and the finite/corona dichotomy

For `f in C_c(R)` define, on each component,

```text
d_(q,sigma)(f)(x,t)=f(t).
```

The proof must establish the following without assuming it from notation.

1. `d_(q,sigma)` is an injective star homomorphism at test level.
2. The component unit-regular representation restricts on its image to the
   intrinsic twisted left-regular representation `Lambda_sigma` of P13-5.
3. Every representation of the component full algebra restricts to a
   representation of `A_sigma`, while the regular representation supplies
   the reverse norm bound.  Since the time group `R` is amenable,

   ```text
   ||d_(q,sigma)(f)||_(B_q^max)
     =||d_(q,sigma)(f)||_(B_q^r)
     =||f||_(C^*(R,sigma)).                       (5.1)
   ```

4. Hence `d_(q,sigma)` extends to an isometric star homomorphism from the
   common time completion into each `B_(q,sigma)^epsilon`.

For a `c0` direct sum of nonzero C-star algebras, use and prove or source the
canonical identity

```text
M(direct_sum_q^c0 B_q)=product_q^bounded M(B_q).   (5.2)
```

Define the time diagonal

```text
D_sigma^epsilon(a)
  =(d_(q,sigma)^epsilon(a))_(q in Q)
  in M(A_(std,sigma)^epsilon).                    (5.3)
```

No orbit origin or enumeration occurs in (5.3).  Equation (5.1) gives every
coordinate the same norm `||a||`, so (5.3) is isometric and faithful.  The
central candidate theorem is

```text
D_sigma^epsilon(a) in A_(std,sigma)^epsilon
  iff a=0 or Q is finite.                         (P13-8B-i)
```

If `Q` is infinite and `pi_cor` is the quotient onto the corona, then

```text
pi_cor o D_sigma^epsilon:
  C^*_(epsilon)(R,sigma)
    -> M(A_(std,sigma)^epsilon)/A_(std,sigma)^epsilon
```

is isometric and faithful, because its kernel is exactly the intersection in
`P13-8B-i`.  This is the **corona-survival theorem**:

```text
nonzero time completions leave the standard c0 algebra
but survive faithfully as diagonal corona elements.       (P13-8B-ii)
```

For finite `Q`, the diagonal lies in the finite direct sum itself.  For
infinite `Q`, no nonzero diagonal has coordinate norms tending to zero.
This completion theorem strictly strengthens, rather than merely restates,
the original compact-support calculation.

## 6. Actual-to-standard completion map and gauge covariance

Let `Sigma=pi_2^*sigma` be the actual multiplier.  The proved time
factorization and `Phi_actual` identify the actual author completion with the
time completion before (5.3) is applied.  The resulting map is denoted

```text
Delta_(X,Sigma)^epsilon:
  TW-epsilon-TRANSPORT_X(Sigma)
    -> M(A_(std,sigma)^epsilon).
```

It is a map between named author records, not a claim that the actual
non-Hausdorff groupoid has acquired a standard groupoid C-star algebra.

If `sigma overline(tau)=delta alpha`, the time gauge is
`U_alpha:A_sigma->A_tau`, and component multiplication by `alpha(t)` gives
`U_(alpha,q):B_(q,sigma)^epsilon->B_(q,tau)^epsilon`.  The exact commuting
square to prove is

```text
U_(alpha,q) d_(q,sigma) = d_(q,tau) U_alpha.       (6.1)
```

Taking `c0` sums, multipliers, and corona quotients preserves (6.1).  Thus
faithfulness, algebra membership, and corona survival are gauge invariant.
Changing a trivializer may conjugate a chosen untwisted presentation by a
character automorphism, but it does not change the intrinsic twisted
diagonal theorem.  No preferred trivializer or orbit origin is claimed.

## 7. Fixed-prime unconditional theorem

Combine P13-8A and P13-8B with `H=(log p)Z`.  Since
`|Q_p^bare|=2^aleph_0`, for every prime `p`, every normalized continuous time
multiplier `sigma`, both `epsilon=max,r`, and every nonzero completion element
`a`, the candidate fixed-prime conclusion is

```text
D_(p,sigma)^epsilon(a) notin A_(std,p,sigma)^epsilon,
pi_cor(D_(p,sigma)^epsilon(a)) != 0,
pi_cor o D_(p,sigma)^epsilon is isometric and faithful.    (P13-8C)
```

At test level, every nonzero time kernel fails standard compact support.  At
completion level, the same time record survives canonically in the corona.
The prime label supplies the exact packet owner, local-unit product, and
common period; it supplies no trace, determinant, orbit enumeration,
amplitude, analytic continuation, Weil structure, or quantization lift.

## 8. Sharp falsifiers and prohibited promotions

The strengthened package fails or narrows if any of the following occurs.

1. The sign subgroup does not embed in the exact `U_p`, or
   `|H_p intersect S_p|>2`.
2. The map `S_p->U_p/H_p` has a fibre not equal to a coset of the
   intersection.
3. The continuum upper bound for `U_p` fails under the exact countable prime
   product.
4. A topology is transported to actual `Q_p` from `Q_p^disc`, or actual
   `Q_p` is called non-second-countable.
5. A compact subset of the standard coproduct meets infinitely many open
   orbit components.
6. The component regular representation does not restrict to the frozen
   `Lambda_sigma`, or either inequality in (5.1) has the wrong direction.
7. A nonzero constant-norm diagonal belongs to an infinite `c0` sum.
8. The multiplier algebra in (5.2) is replaced by the `c0` algebra itself,
   or the corona kernel is larger than the intersection.
9. A noncanonical choice of orbit origins is described as canonical.
10. BHM's removal of second countability is ignored and
    non-second-countability is used as a universal C-star nonexistence claim.
11. A global twisted groupoid completion is named without an exact audited
    framework and convention match.
12. Finite controls are used to prove the continuum, multiplier, or corona
    theorem.

Dense nonclosed stabilizers, heterogeneous stabilizers, noncocompact
`H={0}`, higher-dimensional multiplier counterexamples, and scalar gauges
with zeros remain outside the theorem exactly as in amendment v1.

## 9. Source, novelty, and standalone gates

Before proof authorization an independent v2 audit must bind:

- the exact Paper-9 set model and procyclic/order-two fact;
- cardinal arithmetic used in P13-8A;
- standard compact-orbit twisted test/completion conventions;
- the unit-regular restriction and full/reduced norm inequalities;
- `c0` direct sums and multiplier products for arbitrary index sets;
- the corona quotient and kernel/intersection step;
- the exact BHM nonseparable ceiling and the absence of a false framework
  exclusion; and
- a bounded exact-package precedent search for the conjunction
  `rational-Witt continuum orbit set + actual/standard time diagonal + c0
  membership + faithful corona survival`.

The strongest novelty language remains `SUPPORTED_WITHIN_SEARCH`.  P13-3--5
remain prior-covered in substance.  Neither this design nor a negative
search result grants standalone status.  A fresh independent post-proof
review must find that the combined unconditional fixed-prime cardinality and
corona-survival theorem closes the prior M1.  Otherwise `NOTE_OR_MERGE`
remains binding.

## 10. Claims, controls, Route, and phase status

The revised claim ledger is:

| claim | v2 status |
|---|---|
| P13-1--P13-7 | frozen proofs remain PASS; no new novelty credit |
| original P13-8 | frozen as a proved generic test-support lemma |
| P13-8A | fixed-prime continuum orbit-set theorem: CONJECTURED / MUST PROVE |
| P13-8B | generic component-completion diagonal and corona theorem: SPECIFIED / MUST PROVE |
| P13-8C | unconditional fixed-prime test and corona consequence: CONDITIONAL ON P13-8A/B / MUST PROVE |
| P13-9 v1 controls | design tuple reviewed PASS but unimplemented and insufficient for v2 |
| P13-9 v2 controls | a separate exact design amendment and independent review are mandatory before implementation |
| P13-10 v2 sources/novelty | NOT YET PASSED |
| P13-11 Route | BLOCKED; Route B false |

The exact Route-A registry remains **ten** owners.  Owners 1--7 and 10 are
unchanged.  Only the descriptions of owners 8--9 are expanded:

| no. | owner | v2 exact scope | ceiling |
|---:|---|---|---|
| 8 | `GEN-ACTUAL-STD-QC-SUPPORT-TRANSFER` | common-lattice generic test-support lemma plus component `c0` completion, faithful multiplier diagonal, finite/infinite membership, and corona theorem | generic topology/analytic relation; A0 fail; no arithmetic credit |
| 9 | `DEN-EF-ACTUAL-STD-QC-SUPPORT-TRANSFER-P` | exact continuum `Q_p` theorem, unconditional fixed-prime zero test intersection, non-second-countable standardization, and faithful diagonal corona survival | source-origin arithmetic relation only; no A2--A4 promotion |

No extra owner is created by splitting full and reduced rows inside owner 8
or 9; every eventual YAML must serialize both norms separately in its
claim/evidence fields without conflating them.  Route B remains false.

The already reviewed control tuple

```text
base design: 900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c
design amendment v1: 5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e
final review: bf56b96e19b682600ed5de43f7df51ef381fe82d4e12363f66cd1e7d2a5a5184
```

remains a valid unimplemented design for the v1 claims.  It does not cover
P13-8A--C.  A separately reviewed control-design amendment v2 must freeze
the additional cardinality/diagonal/corona diagnostics and revised package
aggregates before any code or result directory is created.  It must repeat
that finite projections do not prove a continuum or corona theorem and must
continue to bind no concurrent proof hash.

```text
P13_STANDALONE_AMENDMENT_V2=CANDIDATE
P13_8A_PROVED=false
P13_8B_PROVED=false
P13_8C_PROVED=false
V2_SOURCE_GATE_PASSED=false
V2_CONTROL_DESIGN_PASSED=false
V2_CONTROL_IMPLEMENTED=false
STANDALONE_PASS=false
NOTE_OR_MERGE_BINDING=true
ROUTE_A_AUTHORIZED=false
ROUTE_B_INVOCATION_ALLOWED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
```

Only independent zero-finding reviews of these exact bytes may open bounded
v2 proof and control-design work.  Route, composition, manuscript, citation,
release, Git, and public synchronization remain blocked.
