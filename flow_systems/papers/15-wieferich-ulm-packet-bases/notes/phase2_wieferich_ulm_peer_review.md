# Replacement Paper 15: independent exact-byte Phase-2 proof review

Status: **COMPLETE — INDEPENDENT FINAL-FROZEN-BYTE REVIEW**  
Review ID: `P15R-P2-EXACT-BYTE-PEER-REVIEW-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Mathematical/source-domain/devil verdict: **PASS — C0/M0/m0**  
Standalone disposition: **STANDALONE_PASS=PASS**  
Post-subtraction disposition: **FULL_PAPER_PLAUSIBLE=YES; MERGE_OR_STOP not triggered**  
Universal recovery disposition: **OPEN_NOT_AUTHORIZED**

## 1. Review object, independence, and authority

I reviewed the complete current bytes of

```text
papers/15-wieferich-ulm-packet-bases/notes/phase2_wieferich_ulm_proofs.md
```

with the following receipt:

```text
SHA-256: 7804e73863e271402b4c1331843a0cf9a1f4a06e6944b4cbb35257c0aa7d8355
lines:   1127
bytes:   44868
```

The sole Phase-1 gate was also read in full and re-hashed:

```text
papers/15-wieferich-ulm-packet-bases/notes/phase1_final_gate.md
SHA-256: 949839c27f2af87dd9097807f2a5218e4df5de470e235145739bd95919a900cd
lines:   312
bytes:   11102
```

Both receipts match the hashes named in the review instruction.  I did not
read proof-author conversations.  I independently rederived the proof rather
than treating the proof ledger's self-verdict as evidence.  Before starting
the review I read the complete ARS academic-research-suite instructions and
the complete academic-paper-reviewer, methodology-reviewer, domain-reviewer,
devil's-advocate, and source-verification methods.  This review applies their
mathematical/theoretical logic, source-domain, strongest-counterargument, and
maximum-prior-subtraction standards.

No project control was run.  No proof, lock, pipeline, source audit, control,
Route, manuscript, release, archive, or Git artifact was edited.  This peer
review is the only file written by this review.

### 1.1 Complete gate-authority tuple receipt

Every authority artifact was read in full and independently re-hashed on its
current bytes.  All hashes match the frozen tuple.

| Authority artifact | Lines | Recomputed SHA-256 | Result |
|---|---:|---|---|
| `papers/14-global-periodic-topology/notes/papers14_18_batch_design_lock.md` | 196 | `2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8` | MATCH |
| `papers/14-global-periodic-topology/notes/papers14_18_batch_amendment_v1.md` | 325 | `afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802` | MATCH |
| `papers/14-global-periodic-topology/notes/papers14_18_batch_amendment_v2.md` | 239 | `3aa08c2cc2e38b02c83316d188f418d157abd43cf881e447cc28bf083ed3684b` | MATCH |
| `papers/15-mixed-clock-rigidity/notes/phase1_transverse_ulm_precheck.md` | 643 | `02bfac76eeeeb8ac81524c5230b4033de8aec43522d0b74bbc9c635c502732eb` | MATCH |
| `papers/15-wieferich-ulm-packet-bases/notes/research_protocol.md` | 339 | `02693989ad616752c3f6f9e26ad0430a8f5942d0c8449cebe38b7105a2ab3d5a` | MATCH |
| `papers/15-wieferich-ulm-packet-bases/notes/candidate_lock.md` | 47 | `811b4b515dd3f3c45cc96390a139e1d5e3a361d4fea566f0a473d91b8a73d722` | MATCH |
| `papers/15-wieferich-ulm-packet-bases/notes/phase1_amendment_v1.md` | 152 | `2fba2e4f163dbe223ee9eec5ea2d00848e97d2a78fe56ca57b54021837ec0bcc` | MATCH |
| `papers/15-wieferich-ulm-packet-bases/notes/phase1_amendment_v2.md` | 263 | `386ee5775c30ac263f4f72983fb7555b16ade8e72b4597f73fd11460445fcb80` | MATCH |
| `papers/15-wieferich-ulm-packet-bases/notes/phase1_source_precedent_audit.md` | 994 | `287bba68fa191a1971c6c060b7eae43bf2ca2f02cbf64f6dfb8959d5c546de97` | MATCH |
| `papers/15-wieferich-ulm-packet-bases/notes/phase1_methodology_devils_review.md` | 698 | `5af721d6a0ba05731ce2e18397e006b87ef90f327a9edd931c171ad6b889f1ae` | MATCH |

The active precedence and owner restrictions in that tuple are mutually
consistent.  In particular, amendment v2 withdraws the diagonal bounded-
character-extension route, Paper 17 retains the sole Technical Note slot,
and the object under review is the unmarked compact group `B_p`, not an
actual packet, a marked exact sequence, or a measured/flow/operator owner.

## 2. Binding verdict

The frozen proof establishes the authorized theorem

```text
B_p ~=_top B_q
  iff
kappa_r(p)=kappa_r(q) for every rational prime r,
```

with the disjoint-domain signature

```text
kappa_p(p)=0,
kappa_r(p)=v_r(p^(r-1)-1)-1       for odd r!=p,
kappa_2(p)=v_2(p^2-1)-3           for p odd.
```

It supplies the exceptional `r=p` absorption branch, exact off-local
double-valuation saturation, roots internal to the kernel, every finite and
transfinite Ulm invariant, the compact torsion-closure quotient, both
directions of the global classification, the intrinsic `B_2` versus `B_3`
separation, and all required owner firewalls.  None of the mandatory fail-
closed conditions in Phase-1 Section 10 occurs.

```text
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=0
OVERALL_REVIEW_VERDICT=PASS
STANDALONE_PASS=PASS
FULL_PAPER_PLAUSIBLE=YES
MERGE_OR_STOP_TRIGGERED=false
```

The rest of this report records the independent derivation and the hostile
tests supporting that verdict.

## 3. Independent mathematical rederivation

### 3.1 Closed exponent embedding and the Zsigmondy exceptions

For each `ell!=p`, the homomorphism `n |-> p^n` from `Z` to
`Z_ell^x` is continuous for the profinite topology, because its reduction
through any finite unit quotient has finite order.  It therefore extends
uniquely to `Zhat`, and the coordinate extensions give the product map
`e_p`.  This verifies proof Proposition 3.1 (lines 168--174).

To prove injectivity, take a nonzero primary exponent component `a_r`.

* If `r!=p` and `r` is odd, restrict to the `ell=r` principal-unit
  coordinate.  The Teichmueller factor is killed by a pro-`r` exponent and
  the `r`-adic logarithm turns the restriction into multiplication by the
  nonzero element `log(<p>_r)` of the domain `Z_r`.  Hence it detects
  `a_r`.
* If `r=2` and `p` is odd, multiply `p` by its sign to obtain
  `u_p in 1+4Z_2`.  It cannot equal `1`, and the logarithm on `1+4Z_2`
  again gives multiplication by a nonzero element of `Z_2`.
* If `r=p`, suppose `a_p` is nonzero modulo `p^m`.  Apply Bang--Zsigmondy
  to the exponent `n=p^m`.  The `n=1` exception is absent because `m>=1`.
  The `n=2` exception could occur here only at `p=2,m=1`, but then
  `p+1=3` is not a power of two.  The exceptional exponent `n=6` is not a
  prime power.  A primitive divisor `ell` therefore exists, and
  `ord_ell(p)=p^m`, so the `ell` coordinate detects `a_p mod p^m`.

Thus every primary component is detected.  A continuous injection from the
compact group `Zhat` into the Hausdorff group `U_p` is a homeomorphism onto a
closed image.  The proof's closed embedding, not merely algebraic
injectivity, is valid (Theorem 3.2, lines 176--238).

### 3.2 Ambient Sylow factors and the `2`-sign

For `ell!=r`, the pro-`r` Sylow of `Z_ell^x` is the cyclic group of order
`r^{v_r(ell-1)}`.  Dirichlet applied to

```text
ell = 1+r^n mod r^(n+1)
```

gives infinitely many coordinates of exact order `r^n`, for every `n>=1`.
The local `ell=r` factor, when it is present, contributes a `Z_r` principal-
unit factor, dual to `C_(r^infty)`.  For `r=2`, the actual local factor is
`C_2 x Z_2`; its sign is kept until its restriction has been registered and
only then is the abstract `C_2` absorbed into the already countably infinite
order-two part.  If `r=p`, the local coordinate is missing, so there is no
Pruefer summand.  These observations reproduce Proposition 3.3 exactly:

```text
S_r = direct_sum_(n>=1) (C_(r^n))^(aleph_0),
U_(p,(r))^* = S_r                  if r=p,
U_(p,(r))^* = S_r + C_(r^infty)   if r!=p.
```

No abstract absorption loses the `2`-sign contribution to the restriction
map (proof lines 240--288 and 351--385).

### 3.3 Pontryagin arrows and local coefficients

A continuous character of a closed subgroup of a profinite abelian group
factors through a finite quotient.  Its finite character extends because
`R/Z` is divisible.  Therefore restriction is surjective and the exact
sequence really is

```text
0 -> (G/H)^* -> G^* -> H^* -> 0,
```

with the arrows in the direction used in proof Lemma 2.1 and Proposition
4.1.  There is no hidden reversal or unsupported bounded-order lifting.

For odd `r!=p`, logarithmic normalization identifies the local primal map
with multiplication by an element of valuation

```text
v_r(log <p>_r)-1 = v_r(p^(r-1)-1)-1.
```

Dualization retains that coefficient up to units.  At `r=2`, with
`u_p=epsilon_p p in 1+4Z_2`, exact logarithmic valuation gives

```text
v_2(log(u_p)/log 5)
  = v_2(u_p-1)-2
  = v_2(p^2-1)-3.
```

The equality uses `v_2(p+1)=1` when `p=1 mod 4` and `v_2(p-1)=1` when
`p=3 mod 4`.  The sign character maps nontrivially precisely in the latter
case and is included in the bounded map `g`.  Hence the normalized off-local
map has the correctly typed form

```text
Phi(s,z)=g(s)+r^kappa z.
```

This rederives proof Section 4 without importing a source conclusion beyond
the stated local logarithm facts.

### 3.4 Exceptional branch `r=p`: triangular split and Kulikov absorption

Here the source is the direct sum `S_p`, with no Pruefer summand.  Split it
into its homogeneous order-`p^n` blocks.  The image of each block under
`g_p` is a subgroup of the finite cyclic target
`C_(p^infty)[p^n]`; choose one basis vector with maximal image order.
Every other basis vector's image is a scalar multiple of that pivot.  The
finite-support changes

```text
e_j' = e_j-c_j e_0
```

are invertible within the direct sum and kill all nonpivot vectors.  This
produces a literal split `S_p=T+R`, with `g_p(T)=0`, `T~=S_p`, and one
cyclic pivot per homogeneous block (proof Lemma 5.1).

Consequently

```text
K_(p,p)=T + ker(g_p|R).
```

Kulikov's theorem applies to `ker(g_p|R)<=R`, because `R` is a direct sum
of cyclic primary groups.  Its kernel is a countable direct sum of finite
cyclic groups.  Adding it to `T`, which already has `aleph_0` copies of
every finite cyclic order, changes no multiplicity.  Therefore

```text
K_(p,p) ~= S_p,
p^omega K_(p,p)=0,
u_n(K_(p,p))=aleph_0 for every n<omega,
u_alpha(K_(p,p))=0 for every alpha>=omega.
```

This argument includes `p=2`; it neither invokes off-local Kummer theory nor
the withdrawn claim that a primitive divisor gives bounded-character
surjectivity.  The exceptional branch is complete (proof lines 387--525).

### 3.5 Odd off-local Kummer--cyclotomic exact order

Fix odd `r!=p` and `m>=1`, and put

```text
F=Q(zeta_r),
L=F(p^(1/r)),
C_m=Q(zeta_(r^(m+1))).
```

At a prime of `F` over `p`, the polynomial `X^r-p` is Eisenstein; hence
`L/F` is cyclic of degree `r` and ramifies at `p`.  The extension `C_m/F`
is ramified only over `r`.  Since `[L:F]=r`, a nontrivial intersection would
force `L` into `C_m`, contradicting the distinct ramification.  Thus
`L intersection C_m=F`.

Choose on `C_m` the automorphism with cyclotomic exponent `1+r^m`; it fixes
`zeta_(r^m)` and moves `zeta_(r^(m+1))`.  Combine it, using the proved
intersection, with a nonidentity automorphism of `L/F`.  The compositum is
Galois over `Q`.  Chebotarev applied to the conjugacy class of this combined
element yields infinitely many rational primes `ell`.  Conjugation does not
alter the abelian cyclotomic restriction, and it cannot turn a nonidentity
element of the order-`r` Kummer kernel into the identity.  Therefore every
prime in the selected class has

```text
ell = 1+r^m mod r^(m+1),
p is not an r-th power mod ell.
```

The first condition gives `v_r(ell-1)=m`.  In the cyclic group
`F_ell^x`, the second says the exponent of `p` is prime to `r`, so the
`r`-part of its order is the full `r^m`.  Hence

```text
v_r(ord_ell(p))=m.
```

This checks the intersection, the Frobenius conjugacy issue, and both exact
valuations in proof Lemma 6.2.

### 3.6 Separate `r=2`, `p` odd branch, including `m=1`

Put `L=Q(sqrt(p))` and `C_m=Q(zeta_(2^(m+1)))`.  The field `L` ramifies at
the odd prime `p`, while `C_m` is ramified only at `2`; hence their
intersection is `Q`.  Combine the nontrivial quadratic automorphism with the
cyclotomic exponent `1+2^m`.  Chebotarev then supplies infinitely many
primes satisfying

```text
ell = 1+2^m mod 2^(m+1),
(p/ell)=-1.
```

Thus `v_2(ell-1)=m`, and nonsquareness in the cyclic group `F_ell^x`
forces `v_2(ord_ell(p))=m`.

This remains valid at the edge `m=1`: `C_1=Q(i)`, the exponent `3` is
complex conjugation, and the selected primes are `3 mod 4`.  The branch is
correctly restricted to odd `p`.  It is not used when `p=r=2` (proof Lemma
6.3, lines 606--641).

### 3.7 Exact bounded saturation

For a witness prime `ell`, the pro-`r` Sylow of its finite residue-unit
coordinate is `C_(r^m)`.  Because the `r`-part of `p mod ell` has exact
order `r^m`, restriction from the `Z_r` exponent is onto this coordinate.
Dual restriction from that coordinate is therefore onto the target
`r^m`-torsion.  The coordinate source itself is killed by `r^m`, proving

```text
g(S_r[r^m])=C_(r^infty)[r^m]
```

for every `m>=1`.  Merely knowing that the order is divisible by `r^m`, or
knowing only `v_r(ell-1)`, would not prove this equality.  Proof Lemma 6.1
and Theorem 6.4 use both exact valuations correctly.

### 3.8 Roots inside the kernel and infinite height

Let `K=ker(g(s)+r^kappa z)`.  If `(s,z)` lies in every `r^mK`, then its
`S_r` projection belongs to `r^omega S_r=0`; the kernel equation then gives
`z in C_(r^kappa)`.  This proves the upper inclusion

```text
r^omega K <= 0+C_(r^kappa).
```

For the reverse inclusion, take `z` killed by `r^kappa` and an arbitrary
`m`.  Choose a Pruefer root `w_m` with `r^m w_m=z`.  The element
`r^kappa w_m` is killed by `r^m`; exact bounded saturation therefore gives
`s_m in S_r[r^m]` with

```text
g(s_m)=-r^kappa w_m.
```

Now `(s_m,w_m)` is a root **in `K`**, and
`r^m(s_m,w_m)=(0,z)`.  Thus

```text
r^omega K=0+C_(r^kappa).
```

The proof does not substitute ambient Pruefer divisibility for
kernel-internal roots; equation (7.7) is precisely the missing correction
that such an invalid shortcut would omit (proof Theorem 7.2).

### 3.9 Complete finite and transfinite Ulm ledger

The same homogeneous triangular construction applied to the bounded map
`g:S_r->C_(r^infty)` gives an internal killed summand `T~=S_r` of `K`.
For every finite `n`, its `aleph_0` copies of `C_(r^(n+1))` give
`aleph_0` independent height-`n`, order-`r` classes.  Countability supplies
the reverse bound, so

```text
u_n(K)=aleph_0 for every n<omega.
```

At and beyond `omega`, the literal equality just proved gives

```text
r^(omega+j)K=r^j C_(r^kappa), 0<=j<=kappa.
```

If `kappa=0`, every transfinite invariant vanishes.  If `kappa>0`, the
unique nonzero tail invariant is

```text
u_(omega+kappa-1)(K)=1,
```

and every other `u_alpha` with `alpha>=omega` is zero.  This computes the
ordinal position, not merely the order of `r^omega K` (proof Propositions
7.3--7.4).

The group `K` is countable.  Any divisible subgroup would lie inside
`r^omega K`, which is finite; a finite divisible group is zero.  Thus `K`
is reduced before any Ulm/Kiehlmann classification is invoked.  Its compact
dual is countably based and dual-reduced, exactly the domain required by
Kiehlmann (proof Proposition 7.5).

### 3.10 Torsion closure, compact quotient, and exact sequence

For a discrete `r`-group `K` with compact dual `B`, an element of
`r^omega K` is killed by every finite-order character.  Conversely, if
`x notin r^mK`, its nonzero class in `K/r^mK` is separated by a character
of finite `r`-power order.  Therefore

```text
ann(closure(Tor(B)))=r^omega K.
```

The closure is essential; the proof never quotients by possibly nonclosed
raw torsion.

For off-local `K`, write `N=r^omega K`.  Projection to `S_r` is surjective
because multiplication by `r^kappa` on the Pruefer group is surjective, and
its kernel is exactly `N`.  Thus the relevant discrete exact sequence is

```text
0 -> N -> K -> S_r -> 0.
```

Dualizing, with
`A_(p,r)=closure(Tor(B_(p,(r))))`, gives

```text
A_(p,r) ~= P_r,
B_(p,(r))/A_(p,r) ~= C_(r^kappa_r(p)).
```

This also clarifies notation: the finite discrete kernel is `N`; `A_(p,r)`
is its compact annihilator-side torsion closure.  The proof's arrows and
compact quotient are correct (Lemma 8.1 and Theorem 8.2).

### 3.11 Both directions of the global iff

Necessity follows because each pro-`r` Sylow factor is characteristic, as is
the closure of its torsion.  Hence a topological isomorphism preserves the
order of the intrinsic finite quotient and therefore every `kappa_r`.

For sufficiency, equality of all `kappa_r` gives equality of all finite and
transfinite Ulm invariants factor by factor.  The discrete duals are
countable and reduced, so the complete Ulm classification, equivalently the
countably based dual-reduced Kiehlmann formulation, gives factor
isomorphisms.  Dualize and take their unrestricted product.  The product of
homeomorphisms has the product inverse, so it is a homeomorphism.  Neither
direction uses labelled away coordinates.  Proof Theorem 8.4 proves a true
global iff, not a one-way obstruction or a single separation.

### 3.12 `B_2` versus `B_3` and the recovery firewall

At `r=11`, direct factorization gives

```text
2^10-1 = 3*11*31,       kappa_11(2)=0,
3^10-1 = 8*11^2*61,    kappa_11(3)=1.
```

The intrinsic torsion-closure quotients are therefore trivial and `C_11`,
respectively, proving `B_2 not~= B_3` without inspecting the missing ambient
coordinate.

The marked conductor/support filtration is also kept on the correct side of
the owner boundary.  Each homogeneous killed summand contains countably many
equal-order basis elements arising from different labelled supports.
Swapping two with different conductor bounds, while fixing a complementary
summand, is a bare-dual automorphism and moves the marked filtration.  For
`r=2`, taking order at least four avoids the absorbed sign.  Consequently no
marked conductor is reconstructed from the bare group.

Finally, the proof stops at classification by the signature.  It never
infers `p=q` from equality of signatures and explicitly retains

```text
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED.
```

The ambient `U_p` missing-Pruefer-coordinate marker is used only as a
negative control and is never imported into `B_p`.

## 4. Targeted hostile regression matrix

| Required attack | Independent adversarial test | Result |
|---|---|---|
| Source theorem locator | Checked primary/stable records and the precise theorem locations.  Zsigmondy's existence theorem is on printed p. 283; the proof's article range and explicit exception statement resolve to that theorem.  Kiehlmann, Hill, Deninger, Conrad, Sutherland, Moree, and Lagarias--Odlyzko locators and domains all match. | PASS |
| `m=1` | Odd `r`: exponent `1+r` fixes `zeta_r` and moves `zeta_(r^2)`.  `r=2`: `C_1=Q(i)` and exponent `3` is nontrivial.  Exact congruence valuations remain one. | PASS |
| `p=r=2` regression | The diagonal triangular/Kulikov branch applies.  Zsigmondy at exponent two has primitive divisor three; the power-of-two exception does not occur.  The quadratic off-local argument is not used. | PASS |
| Ambient divisibility substitution | Ambient roots `w_m` are explicitly corrected by saturated `s_m`, producing roots inside `K`.  Without (7.7) the proof would fail; (7.7) is present. | PASS |
| Only the tail order is computed | All finite invariants are `aleph_0`; the entire transfinite sequence and unique ordinal `omega+kappa-1` are computed; reducedness is separately proved. | PASS |
| Marked conductor leak | The proof constructs bare automorphisms swapping equal-order killed summands with different labelled supports and prohibits transferring the ambient missing-coordinate marker. | PASS |
| Zsigmondy used for bounded saturation | It is used only for diagonal exponent detection.  Saturation is proved off-local by exact-order Kummer--Chebotarev witnesses. | PASS |
| `2`-sign silently absorbed | Its actual restriction is entered into `g` before the abstract `C_2` summand is absorbed. | PASS |
| Frobenius representative versus conjugacy class | The cyclotomic restriction is conjugacy-invariant and a nonidentity element of the order-`r` Kummer kernel remains nonidentity under conjugation. | PASS |
| One exact valuation only | Both `v_r(ell-1)=m` and `v_r(ord_ell(p))=m` are independently forced and used. | PASS |
| Raw torsion replaces torsion closure | The annihilator lemma and all finite quotients explicitly use `closure(Tor)`. | PASS |
| Kiehlmann domain mismatch | Countability and reducedness/dual-reducedness are proved before classification; the unrestricted product is taken only afterward. | PASS |
| One-way global statement | Necessity uses intrinsic characteristic quotients; sufficiency uses the full Ulm ledger and factorwise product. | PASS |
| Universal recovery smuggled in | Signature injectivity is neither assumed nor claimed; marked support and ambient labels are fenced out. | PASS |

No hostile test produces a finding.

## 5. Source and theorem-domain verification

The source check distinguished bibliographic existence, theorem location,
domain of application, and the ceiling not supplied by the source.  It did
not treat a search-result snippet or a stale direct PDF URL as a theorem.

| Input | Primary/stable verification and exact locator | Domain adjudication |
|---|---|---|
| Deninger compact packet base | [arXiv:1807.06400v4](https://arxiv.org/abs/1807.06400), equations (38)--(40), paragraph after (39), and Theorem 6.1 | Supports provenance and the choice-dependent fibration only; supplies no present Sylow/Ulm classification. |
| Kiehlmann torsion/Ulm classification | [arXiv:1101.3005](https://arxiv.org/abs/1101.3005), Theorem 1.1, Definition 1.3, Theorem 1.4, Remark 1.6, Theorem 1.8, Proposition 2.3 | Applies only after countably based and dual-reduced hypotheses; the proof supplies both before invocation. |
| Kulikov subgroup theorem | [Hill, Pacific J. Math. 42 (1972)](https://msp.org/pjm/1972/42-1/pjm-v42-n1-p08-p.pdf), Corollary 2, printed pp. 66--67 | Gives only that the subgroup is a cyclic direct sum; multiplicities and packet identification remain proof-owned. |
| Bang--Zsigmondy | [Zsigmondy 1892 record and scan](https://zenodo.org/records/2131326), DOI `10.1007/BF01692444`, especially printed p. 283 | Supplies primitive-divisor existence with exceptions.  It supplies neither `v_p(ell-1)` nor bounded restriction-map saturation. |
| Dirichlet | [MIT 18.785 Lecture 18](https://math.mit.edu/classes/18.785/2021fa/LectureNotes18.pdf), Theorem 18.1; [historical translation](https://arxiv.org/abs/0808.1408) | Supplies infinitely many primes in the prescribed reduced class, not a multiplicative-order condition. |
| Qualitative Chebotarev | [MIT 18.785 Lecture 28](https://math.mit.edu/classes/18.785/2025/LectureNotes28.pdf), Theorem 28.9; [Lagarias author bibliography](https://websites.umich.edu/~lagarias/zeta.html), first entry | Supplies primes for a nonempty conjugacy class.  The field intersections, selected Frobenius element, and exact valuations are proof-owned. |
| Local logarithms and `2`-units | [Conrad, Infinite series in p-adic fields](https://kconrad.math.uconn.edu/blurbs/gradnumthy/infseriespadic.pdf), Example 8.15; [Conrad, p-adic interpolation](https://kconrad.math.uconn.edu/math5020f11/padicinterpolation.pdf), Theorem 2.6 and Remark 2.8 | Supplies the logarithm domains, exact valuations, and `Z_2^x={+-1}x(1+4Z_2)`, not character saturation or Ulm conclusions. |
| Prescribed-order comparator | [Moree, arXiv:math/0407421](https://arxiv.org/abs/math/0407421), title/abstract and journal record | Treats primes for which a prescribed integer divides the order.  It does not give the simultaneous exact double valuation and kernel/Ulm package here. |

The Zsigmondy row in the proof cites the full original article range rather
than printing the sharper single page `283`, but it also states the exact
exception list and use-domain in the same row and in Section 3.2.  The
primary scan resolves the theorem unambiguously.  This is a possible future
manuscript citation sharpening, not a mathematical or source-domain defect
in the frozen proof ledger, and it is not counted as a minor finding.

The source domains are respected throughout.  No source is cited for a
stronger conclusion than it proves, and no GRH, effective density estimate,
direct package, or universal-recovery priority claim is silently imported.

## 6. Maximum prior subtraction and post-proof nonredundancy

The publication-weight decision must be made after removing every standard
or source-owned component, not from the impressive length of the proof.

### 6.1 What is fully subtracted

| Subtracted prior/standard input | What is removed from any novelty credit |
|---|---|
| Pontryagin duality | Exact compact/discrete reversal, annihilators, and formal factorwise dualization. |
| Primary structure and Ulm theory | Pro-primary decomposition, the definition of Ulm invariants, and completeness of the countable reduced classification. |
| Kulikov/Pruefer/Hill | Subgroups of cyclic primary direct sums are cyclic direct sums, and the no-infinite-height cyclic-sum input. |
| Kiehlmann | Torsion-closure/infinite-height translation and countably based dual-reduced compact classification. |
| Local units | Teichmueller/principal-unit decompositions, logarithm domains, the `2`-sign split, and standard exact logarithmic valuations. |
| Dirichlet and Bang--Zsigmondy | Arithmetic progressions and primitive-divisor existence with all classical exceptions. |
| Kummer theory and Chebotarev | The general construction of cyclic Kummer extensions and the qualitative occurrence of conjugacy classes. |
| Deninger | The compact quotient's provenance and choice-dependent packet-fibration context. |
| Moree and neighboring order literature | Existing divisibility/prescribed-order prime results and their density framing. |

None of these ingredients, alone or jointly as a generic toolbox, is counted
as the Paper-15 contribution.

### 6.2 What remains after subtraction

After that maximal subtraction, the executed proof still contains the
following connected proof-owned package:

1. The exact natural restriction problem for the arithmetic family
   `U_p/e_p(Zhat)`, including a closed exponent embedding at every primary
   coordinate and the correct split between missing-local and present-local
   branches.
2. A genuinely different exceptional-primary solution: homogeneous
   triangularization of the restriction map followed by literal kernel
   splitting and Kulikov absorption.  This replaces, rather than disguises,
   the tempting false bounded-character-extension route.
3. For every off-local pair and every bound, a simultaneous exact
   `v_r(ell-1)=v_r(ord_ell(p))=m` construction with two independently checked
   intersections, a conjugacy-stable Frobenius prescription, and a separate
   quadratic `r=2` edge case.
4. The nonformal bridge from those arithmetic witnesses to exact bounded
   restriction saturation, then to roots internal to the packet kernel.
5. The full finite/transfinite Ulm computation, with the arithmetic
   Wieferich depth appearing at the exact ordinal `omega+kappa-1`, followed
   by the intrinsic compact quotient by the closure of torsion.
6. The all-prime, both-direction topological classification and its concrete
   `B_2 not~=B_3` witness, together with a constructive proof that marked
   conductor data and the ambient missing-coordinate marker are not bare
   quotient invariants.

This is more than inserting a value into a standard classification theorem.
The arithmetic exact-order lemma is load-bearing for internal divisibility;
internal divisibility is load-bearing for the transfinite Ulm position; the
complete Ulm sequence is load-bearing for the reverse direction of the
global iff.  Removing any one of these bridges breaks the joined theorem.

### 6.3 Strongest routine-substitution objection

The strongest skeptical case is that every named tool is classical, the
off-local witness is a short Kummer--Chebotarev construction, and once the
kernel's infinite-height subgroup is known, Ulm classification is standard.
On that view the work could be folded into a larger paper rather than occupy
the batch's full-paper slot.

That objection is not sustained against the executed proof.  It discounts
the nonuniform diagonal branch, which requires a different algebraic
mechanism and explicitly repairs a false uniform route; it also treats exact
bounded saturation and kernel-internal roots as formal, although neither
follows from ordinary order divisibility or ambient Pruefer divisibility.
Finally, the result is not one separation: it identifies every pro-primary
factor, computes its complete invariant ledger, and proves the family-wide
iff while excluding marked and ambient shortcuts.

The bounded source search still supports only

```text
NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH,
```

not an absolute priority theorem.  Within that honest ceiling, the executed
conjunction retains a coherent theorem-level delta and sufficient
mathematical depth for a full paper.

```text
POST_PROOF_NONREDUNDANCY_VERDICT=PASS
ROUTINE_SUBSTITUTION_OBJECTION=NOT_SUSTAINED
FULL_PAPER_PLAUSIBLE=YES
STANDALONE_PASS=PASS
MERGE_OR_STOP_TRIGGERED=false
SECOND_TECHNICAL_NOTE_FALLBACK=false
```

## 7. Findings by severity

### Critical findings

None.

### Major findings

None.

### Minor findings

None.

The possible sharpening of the Zsigmondy page range to printed p. 283 is
already resolved by the primary-source verification above and does not
alter a theorem statement, hypothesis, inference, source ceiling, or owner
boundary.  It is therefore not elevated into a frozen-proof finding.

## 8. Exact next gate and authorization boundary

The next gate is:

```text
NEXT_GATE=OWNER_ORCHESTRATOR_INTEGRATED_ZERO_FINDING_EXACT_BYTE_POST_PROOF_GATE
```

That gate should bind, without back-editing, all of the following:

* the Phase-1 gate hash
  `949839c27f2af87dd9097807f2a5218e4df5de470e235145739bd95919a900cd`;
* the final proof hash
  `7804e73863e271402b4c1331843a0cf9a1f4a06e6944b4cbb35257c0aa7d8355`;
* this review's post-write SHA-256 and line count;
* the `PASS — C0/M0/m0`, `STANDALONE_PASS=PASS`, and
  `FULL_PAPER_PLAUSIBLE=YES` dispositions;
* the still-open universal-recovery and all owner/firewall restrictions.

This review does not itself authorize control design, control
implementation/execution, a Route, composition, manuscript work, release,
or Git/public synchronization.  A later owner/orchestrator gate must make
any such authorization explicitly.

## 9. Machine-readable disposition

```text
REVIEW_ID=P15R-P2-EXACT-BYTE-PEER-REVIEW-v1.0
REVIEW_SCOPE=MATHEMATICAL_SOURCE_DOMAIN_DEVIL_POST_PROOF_NONREDUNDANCY
REVIEW_INDEPENDENT_OF_PROOF_AUTHOR_DIALOGUE=true
ARS_METHODS_READ_IN_FULL=true
PHASE1_GATE_SHA256=949839c27f2af87dd9097807f2a5218e4df5de470e235145739bd95919a900cd
REVIEWED_PROOF_SHA256=7804e73863e271402b4c1331843a0cf9a1f4a06e6944b4cbb35257c0aa7d8355
AUTHORITY_TUPLE_REHASHED_IN_FULL=true
EXACT_BYTE_MATCH=true
MATHEMATICAL_VERDICT=PASS
SOURCE_DOMAIN_VERDICT=PASS
DEVILS_ADVOCATE_VERDICT=PASS
POST_PROOF_NONREDUNDANCY_VERDICT=PASS
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=0
OVERALL_REVIEW_VERDICT=PASS_C0_M0_m0
CLOSED_EXPONENT_EMBEDDING=PASS
ZSIGMONDY_EXCEPTIONS=PASS
AMBIENT_SYLOW_AND_2_SIGN=PASS
PONTRYAGIN_ARROWS=PASS
R_EQUAL_P_TRIANGULAR_KULIKOV_BRANCH=PASS
ODD_R_NOT_EQUAL_P_KUMMER_CYCLOTOMIC_BRANCH=PASS
R_EQUAL_2_QUADRATIC_CYCLOTOMIC_BRANCH=PASS
M_EQUAL_1_EDGE=PASS
P_R_EQUAL_2_REGRESSION=PASS
EXACT_DOUBLE_VALUATION=PASS
BOUNDED_SATURATION=PASS
KERNEL_INTERNAL_ROOTS=PASS
FINITE_TRANSFINITE_ULM_LEDGER=PASS
COUNTABLE_REDUCED_KIEHLMANN_DOMAIN=PASS
TORSION_CLOSURE_COMPACT_QUOTIENT=PASS
GLOBAL_IFF_BOTH_DIRECTIONS=PASS
B2_NOT_ISOMORPHIC_B3=PASS
MARKED_CONDUCTOR_FIREWALL=PASS
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
ROUTINE_SUBSTITUTION_OBJECTION=NOT_SUSTAINED
FULL_PAPER_PLAUSIBLE=YES
STANDALONE_PASS=PASS
MERGE_OR_STOP_TRIGGERED=false
SECOND_TECHNICAL_NOTE_FALLBACK=false
NEXT_GATE=OWNER_ORCHESTRATOR_INTEGRATED_ZERO_FINDING_EXACT_BYTE_POST_PROOF_GATE
CONTROL_DESIGN_AUTHORIZED=false
CONTROL_IMPLEMENTATION_AUTHORIZED=false
CONTROL_EXECUTION_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
COMPOSITION_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```

Final independent verdict on the specified frozen proof bytes:
**PASS — C0 / M0 / m0; STANDALONE_PASS=PASS; FULL_PAPER_PLAUSIBLE=YES**.
