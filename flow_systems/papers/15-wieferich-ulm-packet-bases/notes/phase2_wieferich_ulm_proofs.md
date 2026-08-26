# Replacement Paper 15 Phase-2 Wieferich--Ulm symbolic proof ledger

Status: **COMPLETE — AUTHORIZED SYMBOLIC PROOF ONLY**  
Version: `P15R-P2-PROOF-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Proof self-verdict: **PASS — C0/M0/m0**  
Standalone disposition: **STANDALONE_PASS=HOLD**  
Publication ceiling: **FULL PAPER PLAUSIBLE; INDEPENDENT EXACT-BYTE PROOF AND NONREDUNDANCY REVIEW REQUIRED**  
Controls, Route A/B, composition, manuscript, release, archive, Git, and
public synchronization: **not authorized / false**

## 1. Exact authorization, precedence, and proof boundary

The sole Phase-1 authorization is the exact-byte gate
`P15R-P1-GATE-v1.0`.  Immediately before proof work, that gate and every
artifact in its authority tuple were re-hashed on their complete current
bytes:

| Artifact | SHA-256 | Receipt and use |
|---|---|---|
| `notes/phase1_final_gate.md` | `949839c27f2af87dd9097807f2a5218e4df5de470e235145739bd95919a900cd` | exact gate match; sole proof authorization |
| Papers 14--18 historical batch design lock | `2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8` | historical slot and owner firewall |
| Papers 14--18 batch amendment v1 | `afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802` | replacement-P15 registration |
| Papers 14--18 batch amendment v2 | `3aa08c2cc2e38b02c83316d188f418d157abd43cf881e447cc28bf083ed3684b` | current batch and sole-note ceiling |
| `notes/research_protocol.md` | `02693989ad616752c3f6f9e26ad0430a8f5942d0c8449cebe38b7105a2ab3d5a` | theorem, owner, and stop obligations |
| `notes/candidate_lock.md` | `811b4b515dd3f3c45cc96390a139e1d5e3a361d4fea566f0a473d91b8a73d722` | exact bare-group candidate |
| transverse Pontryagin/Ulm feasibility precheck | `02bfac76eeeeb8ac81524c5230b4033de8aec43522d0b74bbc9c635c502732eb` | feasibility architecture only |
| `notes/phase1_amendment_v1.md` | `2fba2e4f163dbe223ee9eec5ea2d00848e97d2a78fe56ca57b54021837ec0bcc` | historical branch split; diagonal route later withdrawn |
| `notes/phase1_amendment_v2.md` | `386ee5775c30ac263f4f72983fb7555b16ade8e72b4597f73fd11460445fcb80` | active exceptional-primary absorption |
| `notes/phase1_source_precedent_audit.md` | `287bba68fa191a1971c6c060b7eae43bf2ca2f02cbf64f6dfb8959d5c546de97` | final source/domain feasibility, exact locators, and ceilings |
| `notes/phase1_methodology_devils_review.md` | `5af721d6a0ba05731ce2e18397e006b87ef90f327a9edd931c171ad6b889f1ae` | final methodology/domain/devil/nonredundancy gate |

The active precedence is literal:

```text
batch amendment v2 > batch amendment v1 > historical batch lock;
P15R amendment v2 > amendment-v1 Section 2.2;
the final source addendum v2 > the earlier source-report prefixes.
```

Consequently the following implication is false, withdrawn, and not used
anywhere in this proof:

```text
ord_ell(p)=p^m from a primitive divisor
  => surjectivity of characters of order at most p^m.
```

Bang--Zsigmondy is used on the diagonal only to detect the finite quotients
of the exponent embedding.  It supplies no bounded-order character lift.
The active `r=p` proof is the homogeneous triangular split and
Kulikov/Hill absorption in Section 5.  The exact-order
Kummer--Chebotarev argument is confined to `r!=p` in Section 6.

The owner throughout is the unmarked compact topological group

```text
U_p=product_{ell!=p} Z_ell^x,
e_p:Zhat -> U_p,                 a |-> p^a,
H_p=e_p(Zhat),
B_p=U_p/H_p.                                            (1.1)
```

It is not the actual indiscrete packet quotient `Q_p`, the marked sequence
with labelled coordinates, a measured enhancement, a standardized flow, or
a trace/operator owner.

## 2. Conventions, exact arrows, and source theorem ceilings

All groups are abelian.  Compact groups are Hausdorff.  Discrete primary
groups are written additively; unit groups are written multiplicatively.
Write `C_(r^n)` for the cyclic group of order `r^n`, set `C_(r^0)=1`, and
write `C_(r^infty)` for the Prüfer `r`-group.  For a compact group `G`, its
Pontryagin dual is `G^*`.  For a discrete `r`-group `K`, put

```text
r^0 K=K,
r^(alpha+1)K=r(r^alpha K),
r^lambda K=intersection_{alpha<lambda} r^alpha K
  for a limit ordinal lambda.                              (2.1)
```

Thus `r^omega K=intersection_m r^mK`; for any subgroup `J<=K`, write
`J[r]={x in J:rx=0}`.  The finite Ulm invariant is

```text
u_n(K)=dim_F_r ((r^nK)[r]/(r^(n+1)K)[r]),   n in omega.     (2.2)
```

The same formula at an ordinal `alpha` defines `u_alpha`.

### Lemma 2.1 — exact compact/discrete arrow reversal in the present domain

If `H` is a closed subgroup of an abelian profinite group `G`, then restriction
gives the exact discrete sequence

```text
0 -> (G/H)^* -> G^* -> H^* -> 0.                           (2.3)
```

**Proof.**  A character of `G/H` pulls back to exactly a character of `G`
that annihilates `H`, proving exactness at the first two terms.  Let
`chi:H->R/Z` be continuous.  Its image is finite in the profinite cases used
below, and its kernel is open in `H`.  Choose an open subgroup `V` of `G`
with `V intersection H` contained in `ker(chi)`.  Then `chi` factors through
the subgroup `H/(V intersection H)` of the finite abelian group `G/V`.
A character of a subgroup of a finite abelian group extends to the whole
finite group (decompose into cyclic primary factors, or use divisibility of
`R/Z`).  Pulling the extension back along `G->G/V` gives a continuous
extension of `chi`.  Restriction is therefore onto.  QED.

This proves the exact arrow used here rather than relying on a diagram with
an unstated reversal or continuity convention.  Pontryagin duality also
gives, for a closed `A<=G`,

```text
A^* ~= G^*/A^perp,             (G/A)^* ~= A^perp.           (2.4)
```

### Lemma 2.2 — canonical primary factors

Every abelian profinite group `G` is canonically the unrestricted product
of its unique pro-`r` Sylow factors:

```text
G ~= product_r G_(r).                                       (2.5)
```

Each `G_(r)` is characteristic.  A closed subgroup and a quotient respect
this decomposition.

**Proof.**  Every finite abelian quotient is the product of its unique
primary Sylows, compatibly with all transition maps.  Passing to the inverse
limit proves (2.5).  Uniqueness makes each factor characteristic.  If
`H<=G` is closed, the primary idempotents in every finite quotient give
`H=product_r(H intersection G_(r))`; applying the compact quotient map gives
the quotient assertion.  QED.

### 2.3 Exact external inputs and their ceilings

The proof uses the following source-owned inputs only in the stated domains.
Everything packet-specific, including the two arithmetic intersections,
restriction-map saturation, kernel-internal roots, and the joined
classification, is proved below.

| Source-owned input | Exact locator | Domain used here | Ceiling: what the source does **not** prove |
|---|---|---|---|
| Deninger's compact packet base | Deninger, *Dynamical systems for arithmetic schemes*, arXiv `1807.06400v4`, equations (38)--(40), paragraph immediately after (39), Section 6, Theorem 6.1 | provenance of the compact quotient and its choice-dependent packet fibration | no actual-packet topology identification; no Sylow/Ulm or iff calculation |
| Torsion closure and dual-reduced classification | Kiehlmann, arXiv `1101.3005v3`, Theorem 1.1; Definition 1.3 and Theorem 1.4; Remark 1.6 and Theorem 1.8; Proposition 2.3 | annihilator/infinite-height translation, duality between the full torsion and Ulm sequences, and classification of countably based **dual-reduced** abelian pro-`r` groups by that complete sequence | no packet kernel, arithmetic height, or reduction to one index without the full ledger |
| Kulikov subgroup theorem | Hill, *Pacific J. Math.* 42 (1972), Corollary 2, printed pp. 66--67 | a subgroup of a direct sum of cyclic primary groups is a direct sum of cyclic groups | no multiplicity computation or packet kernel identification |
| Prüfer cyclic-sum theorem | Hill, Theorem 1's cited Prüfer input; also Kiehlmann Proposition 2.3 | a countable primary group with no nonzero infinite-height element is a direct sum of cyclic groups | no arithmetic or Ulm multiplicities |
| Bang--Zsigmondy | Zsigmondy (1892), *Monatshefte* 3, pp. 265--284, with the exact classical three-exception list stated in Section 3.2 below | primitive divisors of `p^(p^m)-1` for exponent-embedding detection | no statement on `v_p(ell-1)` and no bounded character extension |
| Dirichlet | Sutherland, MIT 18.785 Lecture 18, Theorem 18.1; original theorem represented by arXiv `0808.1408` | infinitely many primes in the class `1+r^n mod r^(n+1)` | no multiplicative-order condition |
| Qualitative Chebotarev | Sutherland, MIT 18.785 Lecture 28, Theorem 28.9; Lagarias--Odlyzko (1977) stable bibliographic record on Lagarias's author page | nonempty conjugacy classes in a finite Galois extension occur for infinitely many unramified rational primes | no Kummer/cyclotomic intersection and no selected Frobenius construction |
| Local logarithms | Conrad, *Infinite series in p-adic fields*, Example 8.15; *p-adic interpolation*, Theorem 2.6 and Remark 2.8 | `log:1+rZ_r->rZ_r` for odd `r`, `log:1+4Z_2->4Z_2`, exact valuations, and `Z_2^x={+-1}x(1+4Z_2)` | no restriction-map or Ulm conclusion |
| Prescribed-order comparator | Moree, arXiv `math/0407421` | precedent subtraction only | divisibility of an order is not the simultaneous exact double-valuation lemma proved here |

The stale historical Lagarias--Odlyzko direct PDF URL is not used or
represented as inspected.  No GRH, effective density estimate, or
unverified priority claim occurs.  The novelty ceiling remains exactly

```text
NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH.          (2.6)
```

## 3. The exponent embedding and the ambient Sylow ledger

### Proposition 3.1 — construction and continuity of `e_p`

For every `ell!=p`, the map `Z->Z_ell^x`, `n|->p^n`, is continuous for the
profinite topology on `Z`: the inverse image of an open subgroup contains
`dZ`, where `d` is the order of `p` in the corresponding finite quotient.
It therefore extends uniquely from dense `Z` to a continuous homomorphism
`Zhat->Z_ell^x`.  Taking the product gives the map `e_p` in (1.1).

### Theorem 3.2 — every primary exponent coordinate is detected

The map `e_p` is injective.

**Proof.**  Write `Zhat=product_r Z_r`.  A continuous image of the pro-`r`
factor lies in the pro-`r` Sylow of every target coordinate.

First take `r!=p`.  Use the coordinate `ell=r`.

For odd `r`, write

```text
p=omega_r(p)<p>_r,
omega_r(p) in mu_(r-1),       <p>_r in 1+rZ_r.               (3.1)
```

Here `Z_r` means the canonical pro-`r` Sylow inside `Zhat`, rather than the
diagonal copy of the integer `1`.  Its idempotent exponent is `0` modulo
every prime-to-`r` finite order and `1` in `Z_r`.  The pro-`r` exponent
factor therefore kills `omega_r(p)` and sends its topological generator to
`<p>_r`.  This principal unit is not `1`: otherwise the nonzero rational
integer `p^(r-1)-1` would vanish in `Z_r`.  Its logarithm is consequently
nonzero, and under `log:1+rZ_r->rZ_r` the exponent map is multiplication by
a nonzero element of the integral domain `Z_r`.  Its kernel on `Z_r` is
zero.

For `r=2` (so `p` is odd), choose `epsilon_p in {+1,-1}` with
`u_p=epsilon_p p in 1+4Z_2`.  The principal component `u_p` is not `1`, and
`log(u_p)` is nonzero.  Again the principal-unit projection of the exponent
map has zero kernel on `Z_2`; the finite sign component is retained but is
not needed for injectivity.

It remains to detect `r=p`, because the coordinate `ell=p` is absent.  For
each `m>=1`, apply Bang--Zsigmondy to

```text
a=p, b=1, n=p^m.                                          (3.2)
```

The exact exceptions are: `n=1` and `a-b=1`; `n=2` and `a+b` a power of
`2`; and `(a,b,n)=(2,1,6)`.  Here `n=1` never occurs.  The case `n=2`
occurs only for `p=2,m=1`, but `a+b=3` is not a power of `2`.  Finally `6`
is not a prime power.  Hence there is a primitive prime divisor `ell!=p`
with

```text
ord_ell(p)=p^m.                                            (3.3)
```

If `p^a=1` in every away coordinate, then (3.3) forces the `Z_p` component
of `a` to vanish modulo `p^m` for every `m`, hence to be zero.  The preceding
local arguments do the same for every `Z_r`, `r!=p`.  Thus `a=0`.  QED.

Since `Zhat` is compact and `U_p` Hausdorff, a continuous injection is a
homeomorphism onto a closed image.  Therefore

```text
e_p is a closed embedding,
H_p ~= Zhat.                                                (3.4)
```

No conclusion about the order of a character extending from the subgroup
generated by `p mod ell` was used in this argument.

### Proposition 3.3 — exact ambient pro-`r` factors

Put

```text
P_r=product_{n>=1}(C_(r^n))^aleph_0,
S_r=P_r^*=direct_sum_{n>=1}(C_(r^n))^(aleph_0).             (3.5)
```

Then, as abstract compact groups,

```text
U_(p,(r)) ~= P_r                    if r=p,
U_(p,(r)) ~= Z_r x P_r              if r!=p.                (3.6)
```

**Proof.**  For an odd prime `ell!=r`, the pro-`r` Sylow of
`Z_ell^x` is the finite cyclic group

```text
C_(r^v_r(ell-1)).                                      (3.7)
```

For every `n>=1`, Dirichlet applied modulo `r^(n+1)` to the reduced class
`1+r^n` supplies infinitely many primes `ell` with

```text
v_r(ell-1)=n.                                             (3.8)
```

After deleting the finitely many forbidden coordinates `p,r`, infinitely
many remain.  Thus each `C_(r^n)` occurs at least `aleph_0` times and, since
there are only countably many rational primes, exactly `aleph_0` times.

For odd `r`, the local coordinate `ell=r`, when present, contributes the
principal-unit group `Z_r` and no finite pro-`r` torsion.  It is absent
exactly when `r=p`.

For `r=2`, the local coordinate is literally

```text
Z_2^x ~= C_2 x Z_2.                                      (3.9)
```

When `p` is odd, its extra `C_2` can be absorbed abstractly into the already
`aleph_0` copies of `C_2` in `P_2`, giving `Z_2 x P_2`.  When `p=2`, the
whole local factor is absent.  This proves (3.6).  The absorption in (3.9)
does not erase the sign restriction map; that map is registered in
Proposition 4.3.  QED.

### Corollary 3.4 — factorwise quotient and countability

Under the closed isomorphism (3.4), the pro-`r` Sylow of `H_p` is
`e_p(Z_r)`.  Lemma 2.2 gives

```text
B_p ~= product_r B_(p,(r)),
B_(p,(r))=U_(p,(r))/e_p(Z_r).                              (3.10)
```

The product defining `U_p` is countable, each factor is countably based,
and a closed quotient of a countably based compact group is countably
based.  Hence `B_p` and every `B_(p,(r))` are countably based.

## 4. Exact dual sequences and the off-local coefficient

### Proposition 4.1 — the arrows

Applying Lemma 2.1 to (3.10), with arrows reversed, gives

```text
0 -> K_(p,r) -> U_(p,(r))^* --res_(p,r)--> C_(r^infty) -> 0,
K_(p,r)=B_(p,(r))^*.                                      (4.1)
```

All terms are discrete in (4.1).  In particular,

```text
r=p:   0 -> K_(p,p) -> S_p --g_p--> C_(p^infty) -> 0;

r!=p:  0 -> K_(p,r) -> S_r direct_sum C_(r^infty)
              --Phi_(p,r)--> C_(r^infty) -> 0.             (4.2)
```

The direction `U^*->H^*` is restriction.  Its surjectivity is the continuous
character-extension statement proved in Lemma 2.1, not a bounded-order
extension assertion.

### Proposition 4.2 — odd off-local coefficient

Let `r` be odd and `r!=p`.  After automorphisms by `r`-adic units on the
local source and the target, the local Prüfer summand in (4.2) maps by

```text
z |-> r^kappa z,
kappa=kappa_r(p)=v_r(p^(r-1)-1)-1.                         (4.3)
```

**Proof.**  Use (3.1).  Since `<p>_r^(r-1)=p^(r-1)` and `r-1` is an
`r`-adic unit,

```text
v_r(log <p>_r)=v_r(p^(r-1)-1).                            (4.4)
```

Normalize `1+rZ_r` by a logarithmic generator whose logarithm has valuation
`1`.  The primal map `Z_r->Z_r` is then multiplication by an element of
valuation (4.3).  Its Pontryagin dual has the same multiplication
coefficient on `C_(r^infty)`.  Removing its unit factor gives `r^kappa`.
Fermat's congruence makes `kappa>=0`.  QED.

### Proposition 4.3 — the off-local `2` coefficient and sign ledger

Let `r=2` and `p` be odd.  With `u_p=epsilon_p p in 1+4Z_2` as in
Theorem 3.2, normalize the principal units by `log(5)`.  Then

```text
v_2(log(u_p)/log(5))
 =v_2(u_p-1)-2
 =v_2(p^2-1)-3
 =kappa_2(p).                                               (4.5)
```

Indeed, if `p=1 mod 4`, then `u_p=p` and `v_2(p+1)=1`; if `p=3 mod 4`,
then `u_p=-p` and `v_2(p-1)=1`.  Equation (4.5) follows in either case.

The actual local dual before abstract absorption is

```text
C_2 direct_sum C_(2^infty).                               (4.6)
```

If `p=3 mod 4`, the nontrivial generator of the `C_2` sign character
restricts to the unique element of order `2` in the target; if `p=1 mod 4`
it restricts trivially.  We absorb the **group** `C_2` into the countable
order-`2` part of `S_2`, but place its actual restriction contribution inside
the map called `g` below.  Only the principal Prüfer summand is normalized
to multiplication by `2^kappa`.  Thus for every `r!=p`, including `r=2`,
we may and do write

```text
Phi(s,z)=g(s)+r^kappa z,
S_r direct_sum C_(r^infty) -> C_(r^infty),                 (4.7)
```

where the sign in (4.6) has been registered, not discarded.

## 5. The exceptional-primary branch `r=p`

This section is valid for every prime `p`, including `p=2`.  It does not use
off-local exact-order saturation.

### Lemma 5.1 — homogeneous triangular split

Let

```text
S=direct_sum_{n>=1} S_n,
S_n=(C_(p^n))^(aleph_0),
g:S->C_(p^infty)                                           (5.1)
```

be any homomorphism.  For each `n`, fix a basis
`(e_(n,j))_(j>=0)` of `S_n`.  Among the finitely many possible orders
`1,p,...,p^n` of the basis images under `g_n=g|S_n`, choose
`e_(n,0)` with maximal image order; if `g_n=0`, choose any basis vector.
Subgroups of the cyclic target `C_(p^infty)[p^n]` are linearly ordered, so
`g(e_(n,0))` generates `g_n(S_n)`.  For every `j>0`, choose
`c_(n,j) in Z/p^nZ` with

```text
g(e_(n,j))=c_(n,j)g(e_(n,0)),
e'_(n,j)=e_(n,j)-c_(n,j)e_(n,0).                           (5.2)
```

The simultaneous change of basis

```text
e_(n,0) |-> e_(n,0),
e_(n,j) |-> e'_(n,j),                                     (5.3)
```

is an automorphism of the algebraic direct sum.  Each input has finite
support, so both (5.3) and the inverse
`e_(n,j)=e'_(n,j)+c_(n,j)e_(n,0)` contain only finite sums.  The coefficient
`1` in the old `e_(n,j)` coordinate shows that `e'_(n,j)` still has exact
order `p^n` and that the new family is a basis.  Consequently

```text
S_n=T_n direct_sum R_n,
T_n=direct_sum_{j>0}<e'_(n,j)> ~= (C_(p^n))^(aleph_0),
R_n=<e_(n,0)> ~= C_(p^n),
g(T_n)=0.                                                   (5.4)
```

### Lemma 5.2 — literal kernel split and Kulikov absorption

Taking algebraic direct sums in (5.4) gives

```text
S=T direct_sum R,
T=direct_sum_n T_n ~= S,
R=direct_sum_n R_n ~= direct_sum_{n>=1}C_(p^n),
g(T)=0.                                                     (5.5)
```

Writing an element uniquely as `t+x`, the equation `g(t+x)=0` is exactly
`g(x)=0`.  Hence there is a literal internal equality

```text
ker(g)=T direct_sum ker(g|R).                               (5.6)
```

Now, and only now, the Kulikov/Hill theorem is in domain:
`R` is a direct sum of cyclic primary groups and `ker(g|R)` is a subgroup
of it.  Hill, Corollary 2, printed pp. 66--67, makes `ker(g|R)` a direct sum
of finite cyclic `p`-groups.  It is countable because `R` is countable, so
the multiplicity `mu_n` of each `C_(p^n)` is at most `aleph_0`.  The summand
`T` already has `aleph_0` copies of every such order.  Since
`aleph_0+mu_n=aleph_0`, a bijection of cyclic summands gives

```text
ker(g) ~= T ~= S.                                          (5.7)
```

This uses Kulikov at its exact subgroup domain and countability only for the
subsequent multiplicity absorption.

### Theorem 5.3 — complete exceptional ledger

Apply Lemmas 5.1--5.2 to the epimorphism `g_p` in (4.2).  Then

```text
K_(p,p)=ker(g_p) ~= S_p.                                   (5.8)
```

Every element of `S_p` has finite support.  A nonzero coordinate in a
finite cyclic summand prevents the element from lying in `p^mS_p` for all
large `m`; hence `p^omega S_p=0`.  Also, the countably many summands
`C_(p^(n+1))` give

```text
u_n(K_(p,p))=aleph_0                  for every n<omega,
p^omega K_(p,p)=0,
u_alpha(K_(p,p))=0                    for every alpha>=omega. (5.9)
```

Thus `K_(p,p)` is countable and reduced.  Dualizing (5.8) gives

```text
B_(p,(p)) ~= P_p,
closure(Tor(B_(p,(p))))=B_(p,(p)),
B_(p,(p))/closure(Tor(B_(p,(p))))=1=C_(p^0),
kappa_p(p)=0.                                               (5.10)
```

The density in (5.10) is also direct: finite-support torsion points are
dense in the product `P_p`.

### 5.4 Withdrawn-route and `p=r=2` firewall

The proof of (5.8)--(5.10) never asserts
`g_p(S_p[p^m])=C_(p^infty)[p^m]`.  Full character restriction in (4.1)
does not imply that bounded-order restriction.  The concrete obstruction

```text
ord_17(2)=8,             v_2(17-1)=4                       (5.11)
```

is retained as a regression witness: a faithful character of the order-`8`
subgroup of `C_16` may require an extension of order `16`.

Moreover, if `ell=1 mod 8`, supplementary quadratic reciprocity gives

```text
(2/ell)=(-1)^((ell^2-1)/8)=1.                              (5.12)
```

Thus `2` is a square modulo `ell` and one cannot require

```text
v_2(ord_ell(2))=v_2(ell-1)>=3.                             (5.13)
```

The case `p=r=2` belongs only to Theorem 5.3.  Equations (5.11)--(5.13)
are not used to weaken the valid off-local branch `r=2!=p` below.

## 6. Off-local exact-order saturation (`r!=p` only)

Fix `r!=p`, and let `g:S_r->C_(r^infty)` be the away/sign part of (4.7).

### Lemma 6.1 — one exact coordinate gives bounded saturation

Suppose `ell!=p,r` satisfies

```text
v_r(ell-1)=m,
v_r(ord_ell(p))=m.                                         (6.1)
```

The coordinate pro-`r` Sylow is then `G_ell=C_(r^m)`, and the pro-`r`
exponent map `Z_r->G_ell` is onto because the `r`-primary part of `p mod
ell` has exact order `r^m`.  Its dual restriction embeds
`G_ell^*=C_(r^m)` onto `C_(r^infty)[r^m]`.  Since that coordinate dual lies
inside `S_r[r^m]`, (6.1) implies

```text
g(S_r[r^m])=C_(r^infty)[r^m].                              (6.2)
```

The reverse containment in (6.2) is automatic because a homomorphism sends
`r^m`-torsion to `r^m`-torsion.

### Lemma 6.2 — odd Kummer--cyclotomic intersection and Frobenius

Let `r` be odd, `r!=p`, and `m>=1`.  Put

```text
F=Q(zeta_r),
L=F(p^(1/r)),
C_m=Q(zeta_(r^(m+1))).                                    (6.3)
```

Then `L intersection C_m=F`.

**Proof of the intersection.**  The prime `p` is unramified in `F/Q`
because `p!=r`.  At every prime `P` of `F` above `p`, `v_P(p)=1`; hence
`X^r-p` is Eisenstein at `P`.  Thus `L/F` is a nontrivial cyclic Kummer
extension of prime degree `r` and is ramified above `p`.  The cyclotomic
extension `C_m/F` is ramified only above `r`.  Since `[L:F]=r`, its
intersection with `C_m` is either `F` or `L`; the latter would make `L/F`
unramified above `p`, a contradiction.  QED.

Choose the exact cyclotomic and Kummer automorphisms

```text
sigma_C in Gal(C_m/F):
sigma_C(zeta_(r^(m+1)))=zeta_(r^(m+1))^(1+r^m),
so sigma_C fixes zeta_(r^m) but moves zeta_(r^(m+1));

sigma_L in Gal(L/F):
sigma_L(p^(1/r))=zeta_r p^(1/r).                            (6.4)
```

The intersection just proved makes these restrictions compatible, so they
define `sigma in Gal(LC_m/F)`.  The compositum `LC_m/Q` is finite Galois.
Apply unconditional qualitative Chebotarev to the conjugacy class of
`sigma`.  It gives infinitely many unramified rational primes `ell`, and we
discard the finitely many `p,r`, such that:

1. the cyclotomic Frobenius fixes `zeta_(r^m)` but not
   `zeta_(r^(m+1))`, so `v_r(ell-1)=m`;
2. the Frobenius fixes `F`, so `ell` splits there and the residue field is
   `F_ell`; and
3. its nontrivial Kummer restriction says that `p` is not an `r`th power
   in `F_ell^x`.

If a cyclic group has order with `r`-valuation `m`, an element is not an
`r`th power exactly when its exponent relative to a generator is prime to
`r`, equivalently when the `r`-part of its order is `r^m`.  Hence these
primes satisfy both equalities in (6.1).

The use of a conjugacy class causes no loss: the cyclotomic Galois group is
abelian, and conjugation sends the nontrivial Kummer element to another
nontrivial element while preserving its restriction to `F`.

### Lemma 6.3 — the separate quadratic/cyclotomic branch at `r=2`

Let `r=2`, so `p` is odd, and put

```text
L=Q(sqrt(p)),
C_m=Q(zeta_(2^(m+1))).                                    (6.5)
```

The quadratic field `L` is ramified at the odd prime `p`, whereas `C_m` is
ramified only at `2`; therefore

```text
L intersection C_m=Q.                                     (6.6)
```

Choose the unique compatible automorphism that is nontrivial on `sqrt(p)`
and whose cyclotomic restriction is

```text
zeta_(2^(m+1)) |-> zeta_(2^(m+1))^(1+2^m).                 (6.7)
```

It fixes `zeta_(2^m)` and moves `zeta_(2^(m+1))`.  Chebotarev in the finite
abelian compositum gives infinitely many odd primes `ell!=p` with

```text
v_2(ell-1)=m,
(p/ell)=-1.                                                (6.8)
```

Nonsquareness in the cyclic group `F_ell^x`, whose `2`-part has order
`2^m`, is equivalent to `v_2(ord_ell(p))=m`.  The case `m=1` is included:
the cyclotomic condition is `ell=3 mod 4`, independently combined with
`(p/ell)=-1`.  This argument applies only to odd `p`; it neither uses nor
contradicts the diagonal firewall (5.13).

### Theorem 6.4 — exact double-valuation saturation

For every `r!=p` and every `m>=1`, Lemma 6.2 or 6.3 supplies infinitely many
primes `ell!=p,r` satisfying

```text
v_r(ell-1)=m,
v_r(ord_ell(p))=m.                                         (6.9)
```

Lemma 6.1 therefore proves the exact equality

```text
g(S_r[r^m])=C_(r^infty)[r^m]       for every m>=1.          (6.10)
```

Both valuations, not mere divisibility of the order, are load-bearing.
The proof is unconditional and qualitative; no density computation and no
GRH hypothesis is used.

## 7. Off-local kernel, internal roots, and the complete Ulm ledger

Continue with `r!=p`, put `kappa=kappa_r(p)`, and normalize (4.7) as

```text
Phi(s,z)=g(s)+r^kappa z,
K=K_(p,r)=ker(Phi).                                        (7.1)
```

### Lemma 7.1 — a homogeneous killed summand

Apply the triangular construction of Lemma 5.1, with `r` in place of `p`,
to the map `g:S_r->C_(r^infty)`.  It gives

```text
S_r=T direct_sum R,
T~=S_r,
R~=direct_sum_{n>=1}C_(r^n),
g(T)=0.                                                     (7.2)
```

Consequently there is a literal internal split

```text
K=T direct_sum K^0,
K^0=ker(Phi|_(R direct_sum C_(r^infty))).                  (7.3)
```

This split will provide all finite multiplicities and will make the compact
torsion-closure type explicit; it is not used as a substitute for the
infinite-height calculation.

### Theorem 7.2 — literal equality at infinite height

Inside the displayed ambient group of (7.1),

```text
r^omega K = 0 direct_sum C_(r^kappa).                       (7.4)
```

**Upper inclusion.**  If `(s,z)` lies in `r^mK` for every `m`, then its
`S_r` projection lies in every `r^mS_r`.  The algebraic direct sum `S_r`
has `r^omega S_r=0`, so `s=0`.  The kernel equation is then
`r^kappa z=0`, proving

```text
r^omega K subset 0 direct_sum C_(r^kappa).                 (7.5)
```

**Reverse inclusion by roots inside the kernel.**  Let
`z in C_(r^infty)[r^kappa]`, and fix an arbitrary `m>=1`.  Choose an ambient
Prüfer root `w_m` with

```text
r^m w_m=z.                                                  (7.6)
```

Then `r^kappa w_m` belongs to `C_(r^infty)[r^m]` because
`r^m r^kappa w_m=r^kappa z=0`.  By the exact saturation (6.10), choose

```text
s_m in S_r[r^m],
g(s_m)=-r^kappa w_m.                                       (7.7)
```

Equations (7.1) and (7.7) show that `(s_m,w_m)` lies **inside `K`**, and

```text
r^m(s_m,w_m)=(0,z).                                        (7.8)
```

Since this construction works for every `m`, `(0,z) in r^omega K`.  This
proves the reverse inclusion and (7.4).  Ambient divisibility alone would
give (7.6) but not (7.7), and therefore would not prove the theorem.  QED.

### Proposition 7.3 — every finite Ulm invariant

For every `n<omega`, the direct summand `T~=S_r` in (7.3) contributes
`aleph_0` independent order-`r` classes at height `n`, coming from its
`aleph_0` copies of `C_(r^(n+1))`.  Thus `u_n(K)>=aleph_0`.  The group

```text
S_r direct_sum C_(r^infty)                                (7.9)
```

is countable, so `K` is countable and `u_n(K)<=aleph_0`.  Hence

```text
u_n(K_(p,r))=aleph_0              for every finite n.       (7.10)
```

No finite invariant is inferred merely from the order of (7.4).

### Proposition 7.4 — the entire transfinite tail

If `kappa=0`, (7.4) is zero, so every invariant at an ordinal
`alpha>=omega` vanishes.  If `kappa>0`, successor multiplication in the
finite cyclic group (7.4) gives

```text
r^(omega+j)K=r^j C_(r^kappa) ~= C_(r^(kappa-j))
       for 0<=j<=kappa,
r^(omega+kappa)K=0.                                        (7.11)
```

For `j<kappa-1`, the order-`r` subgroup of consecutive terms in (7.11) is
the same unique `C_r`, so the corresponding Ulm quotient is zero.  At
`j=kappa-1`, it is `C_r/0`.  All later terms vanish.  Therefore

```text
kappa>0:  u_(omega+kappa-1)(K_(p,r))=1,
          u_alpha(K_(p,r))=0 for every other alpha>=omega;

kappa=0:  u_alpha(K_(p,r))=0 for every alpha>=omega.        (7.12)
```

Together, (7.10) and (7.12) are the complete finite/transfinite Ulm ledger.

### Proposition 7.5 — countable and reduced before classification

Countability was established in Proposition 7.3.  If `D<=K` were divisible,
then each `x in D` would have roots of every finite `r`-power **inside `K`**;
therefore `D<=r^omega K`.  By (7.4), this last group is finite.  A finite
divisible group is zero, so `D=0`.  Thus `K_(p,r)` is reduced.

For `r=p`, Theorem 5.3 already gave the countable reduced group `S_p`.
Consequently every `B_(p,(r))` is countably based and dual-reduced before
any Kiehlmann/Ulm classification theorem is invoked.  There is no hidden
Prüfer summand.

## 8. Compact translation, intrinsicity, and the global iff

### Lemma 8.1 — the annihilator uses the closure of torsion

Let `K` be a discrete `r`-group and `B=K^*`.  Then

```text
ann(closure(Tor(B)))=r^omega K.                             (8.1)
```

**Proof.**  If `x in r^omega K` and `chi in B` has order dividing `r^m`,
write `x=r^m y`; then `chi(x)=r^m chi(y)=0`.  Thus `r^omega K` annihilates
`Tor(B)` and its closure.

Conversely, if `x notin r^omega K`, choose `m` with `x notin r^mK`.
The nonzero class of `x` in the bounded group `K/r^mK` is separated by a
homomorphism to `C_(r^m)<=R/Z`: define a nonzero character on its cyclic
subgroup and extend it using divisibility of `R/Z`.  Pulling back gives a
continuous point `chi in B` of finite order with `chi(x)!=0`.  Hence `x`
does not annihilate `Tor(B)`.  Finally annihilators of a subset and of its
closure agree because evaluation at `x` is continuous.  QED.

This is the direct proof of the identity recorded by Kiehlmann Theorem 1.1.
It expressly concerns `closure(Tor(B))`, not an unjustified quotient by the
possibly nonclosed raw torsion subgroup.

For reference, (4.3), (4.5), and (5.10) now give the complete piecewise
signature, with disjoint domains:

```text
kappa_r(p)=0                              if r=p;
kappa_r(p)=v_r(p^(r-1)-1)-1              if r is odd and r!=p;
kappa_2(p)=v_2(p^2-1)-3                   if r=2 and p is odd.
```

### Theorem 8.2 — exact compact factor type

For every prime pair `p,r`, put

```text
A_(p,r)=closure(Tor(B_(p,(r)))).                            (8.2)
```

Then

```text
A_(p,r) ~= P_r,
B_(p,(r))/A_(p,r) ~= C_(r^kappa_r(p)).                      (8.3)
```

**Proof.**  The exceptional case `r=p` is (5.10), so assume `r!=p` and put
`N=r^omega K_(p,r)`.  Lemma 8.1 and (2.4) give

```text
A_(p,r)^* ~= K_(p,r)/N,
(B_(p,(r))/A_(p,r))^* ~= N.                                (8.4)
```

Projection onto the first coordinate restricts to an exact sequence

```text
0 -> N -> K_(p,r) --pi_S--> S_r -> 0.                       (8.5)
```

Indeed, multiplication by `r^kappa` on the Prüfer group is surjective, so
for every `s in S_r` there is `z` with
`r^kappa z=-g(s)`; hence `(s,z) in K` and `pi_S` is onto.  Its kernel is
exactly the set of `(0,z)` with `r^kappa z=0`, which is `N` by (7.4).
The first isomorphism theorem therefore gives directly

```text
K_(p,r)/N ~= S_r.                                          (8.6)
```

Dualizing (8.6) proves `A_(p,r)~=P_r`.  Theorem 7.2 identifies
`N~=C_(r^kappa)`, a finite self-dual cyclic group, so the second identity in
(8.3) follows from (8.4).  QED.

### Proposition 8.3 — bare-group intrinsicity

The factor `B_(p,(r))` is characteristic by Lemma 2.2.  Its algebraic
torsion subgroup is characteristic under every group automorphism, and its
topological closure is therefore characteristic.  Hence the finite quotient
in (8.3), including its order, is intrinsic to the unmarked compact group:

```text
kappa_r(p)
 =log_r [B_(p,(r)):closure(Tor(B_(p,(r))))].                (8.7)
```

No coordinate of `U_p` and no conductor label appears in (8.7).

### Theorem 8.4 — complete global classification

For rational primes `p,q`,

```text
B_p ~=_top B_q
  iff
kappa_r(p)=kappa_r(q) for every rational prime r.           (8.8)
```

**Necessity.**  A topological group isomorphism sends the unique
characteristic pro-`r` Sylow factor to the pro-`r` Sylow factor and sends
the closure of its torsion onto the closure of torsion.  The quotient orders
in (8.7) are therefore equal for every `r`, proving equality of every
`kappa` coordinate.

**Sufficiency.**  Suppose all coordinates agree.  For each `r`, the groups
`K_(p,r)` and `K_(q,r)` are countable and reduced by Proposition 7.5 and
Theorem 5.3.  Their finite invariants are all `aleph_0`; their complete
transfinite invariants agree by (5.9) or (7.12) because the corresponding
`kappa` values agree.  Each Ulm quotient in (2.2) is an `F_r`-vector space,
so equality of every displayed dimension is exactly isomorphism of the full
Ulm sequences.  Kiehlmann Remark 1.6 identifies those sequences as the
Pontryagin duals of the full compact torsion sequences.  Thus all hypotheses
of the countably based dual-reduced classification in Kiehlmann Theorem 1.8
have now been supplied, and it gives

```text
K_(p,r) ~= K_(q,r).                                        (8.9)
```

Dualizing gives a topological isomorphism
`phi_r:B_(p,(r))->B_(q,(r))`.  Finally use the canonical decompositions
(3.10) and take the **unrestricted** product

```text
product_r phi_r : product_r B_(p,(r))
                    -> product_r B_(q,(r)).                 (8.10)
```

The product of the homeomorphisms is a homeomorphism with inverse
`product_r phi_r^(-1)`.  This proves sufficiency.  The construction uses
only the intrinsic rational-prime Sylow types and arbitrary factor
isomorphisms; labelled away coordinates from `U_p` do not survive.  QED.

## 9. Arithmetic separation and owner firewalls

### Proposition 9.1 — the intrinsic separation `B_2 not~= B_3`

At `r=11`,

```text
2^10-1=1023=3*11*31,
kappa_11(2)=1-1=0;                                         (9.1)

3^10-1=59048=8*11^2*61,
kappa_11(3)=2-1=1.                                         (9.2)
```

Theorem 8.2 therefore gives the bare compact-group witnesses

```text
B_(2,(11))/closure(Tor(B_(2,(11))))=1,
B_(3,(11))/closure(Tor(B_(3,(11))))~=C_11.                 (9.3)
```

Equivalently, torsion is dense in the first `11`-primary factor and has
closure of index `11` in the second.  The characteristic quotients in (9.3)
cannot be carried to each other by an isomorphism, so

```text
B_2 not~=top B_3.                                          (9.4)
```

This argument does not inspect which ambient coordinate is missing.

### Proposition 9.2 — marked support is not a bare invariant

For the marked exact sequence

```text
H_p -> U_p -> B_p,                                         (9.5)
```

the dual `K_(p,r)<=U_(p,(r))^*` inherits labelled finite coordinate
supports and hence the source conductor/support filtration.  This filtration
is natural **for (9.5)**.

It is not characteristic on the bare group.  Indeed, in every homogeneous
order block the constructions (5.4) and (7.2) exhibit a direct summand

```text
T_n=(C_(r^n))^(aleph_0)<=K_(p,r).                          (9.6)
```

Its displayed basis elements arise from distinct away coordinates (after
the finite triangular correction by the chosen pivot).  There are infinitely
many such away coordinates in every order block by (3.8); when `r=2`, take
`n>=2` so the absorbed local sign is not involved.  Choose two such elements
whose labelled supports have different conductor bounds.  Swapping
them, and fixing the remaining basis of `T_n` and the complementary summand
of `K_(p,r)`, is an automorphism of the discrete bare dual.  It moves the
marked support/conductor filtration.  Pontryagin duality gives the
corresponding automorphism of `B_(p,(r))`.

Thus equal-order summands can be mixed by bare automorphisms, and neither the
embedding in `U_p^*` nor a labelled conductor is reconstructible from
`B_p` alone.

### Proposition 9.3 — the ambient missing-coordinate marker is only a control

The bare ambient group `U_p` does retain the omitted prime: by (3.6),

```text
U_(p,(r))^* has a divisible C_(r^infty) summand iff r!=p.    (9.7)
```

The unique Sylow prime with no such local divisible summand is `p`.  This is
an invariant of **`U_p`**, not of the quotient `B_p`; Theorem 5.3 and
Proposition 7.4
show how quotienting by `H_p` replaces that simple marker by the
`kappa`-ledger.  Equation (9.7) is therefore a negative control against
smuggling the ambient label into the quotient classification.

### 9.4 Exact owner firewall

| Record | What this ledger proves or uses | What is forbidden |
|---|---|---|
| marked sequence `H_p->U_p->B_p` | source-natural coordinate support and the exponent restriction map | treating its labels as bare invariants |
| bare compact group `B_p` | Theorems 8.2 and 8.4 and Proposition 9.1 | importing a missing-coordinate marker |
| actual packet quotient `Q_p` | nothing beyond the upstream statement that it is a different owner | transferring compact topology, separation, or (9.4) to `Q_p` |
| Haar/measured enhancement | no measured theorem | transporting normalized Haar to the actual packet or claiming descent/canonicity |
| standardized flow/time owner | no flow theorem | importing a clock, real-time marking, or Paper-16 recovery |
| trace/operator/determinant | no analytic theorem | any return trace, weight, spectrum, determinant, or Route-B claim |

In particular, this proof neither creates nor analyzes controls, a Route,
composition, manuscript text, a measured owner, or a trace.

### 9.5 Universal prime recovery remains open

Theorem 8.4 classifies the family by the equivalence relation

```text
B_p~=B_q iff kappa(p)=kappa(q).                             (9.8)
```

It does **not** prove that `p|->kappa(p)` is injective.  Equality of all
signatures cannot be followed by `p=q` without a new arithmetic theorem,
and Proposition 9.2 forbids using marked support to manufacture one.

```text
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED.                    (9.9)
```

## 10. Full claim-closure ledger

| Claim | Gate obligation | Proof owner in this ledger | Closure |
|---|---|---|---|
| P15R-1 | `e_p` closed embedding, every Sylow, omitted-`p` exceptions | Propositions 3.1, Theorem 3.2 | **PROVED** |
| P15R-2 | every finite cyclic multiplicity and exact ambient Sylows, including `2` sign | Proposition 3.3; Proposition 4.3 | **PROVED** |
| P15R-3a | exact reversed dual arrows and local coefficient | Proposition 4.1--4.3 | **PROVED** |
| P15R-3b | off-local simultaneous exact valuations and saturation | Lemmas 6.1--6.3; Theorem 6.4 | **PROVED for `r!=p`** |
| P15R-3c | diagonal branch without bounded character extension | Section 5, especially Lemmas 5.1--5.2 | **PROVED; old route explicitly withdrawn** |
| P15R-4 | both inclusions in `r^omega`, all finite/transfinite Ulm data, reduced guard | Theorem 7.2; Propositions 7.3--7.5; Theorem 5.3 | **PROVED** |
| P15R-5 | annihilator with closure, `P_r` torsion closure, finite compact quotient | Lemma 8.1; Theorem 8.2 | **PROVED** |
| P15R-6 | global iff both ways, unrestricted product, `B_2 not~=B_3` | Theorem 8.4; Proposition 9.1 | **PROVED** |
| P15R-7 | marked/bare boundary and ambient marker control | Propositions 9.2--9.3; Section 9.4 | **PROVED** |
| P15R-8 | universal recovery and precedent ceiling | (2.6), (9.9), source table | **OPEN/CEILING RETAINED; not promoted** |

The exact gate Sections 4--9 are therefore closed without deferral to a
finite control.  Standard Pontryagin duality, local-unit structure,
Bang--Zsigmondy, Dirichlet, Chebotarev, Kulikov/Prüfer, and the
Kiehlmann/Ulm classification have been subtracted in the source table; the
new proof surface is the joined packet-specific calculation.

## 11. Hostile self-audit, findings, and frozen disposition

### 11.1 Regression and completeness audit

| Attack | Exact check | Result |
|---|---|---|
| wrong dual direction | compact quotient dualized as `0->B^*->U^*->H^*->0`; restriction surjectivity proved | PASS |
| revived bounded-character route | no diagonal saturation used; (5.11) retained as counterexample | PASS |
| `p=r=2` leakage | diagonal `2` handled only by Section 5; impossible condition (5.13) rejected | PASS |
| erased local sign | literal `C_2` restriction recorded in (4.6) before abstract absorption | PASS |
| divisibility instead of exact order | both valuations in (6.9) proved by compatible Frobenius | PASS |
| unjustified field intersection | ramification domains proved separately in Lemmas 6.2 and 6.3 | PASS |
| ambient roots substituted for kernel roots | cancellation (7.7) constructs an internal root at every depth | PASS |
| only order of `r^omega` recorded | both inclusions and the full ordinal filtration (7.11)--(7.12) written | PASS |
| hidden divisible summand | countability and reducedness proved before classification | PASS |
| `Tor` used without closure | annihilator identity and compact quotient use `closure(Tor)` throughout | PASS |
| one-way invariant only | necessity and sufficiency, then unrestricted product, proved in Theorem 8.4 | PASS |
| marked or actual-owner promotion | explicit automorphism falsifier and owner table retained | PASS |
| universal recovery smuggled in | (9.9) remains OPEN and no `p=q` conclusion appears | PASS |

### 11.2 C/M/m ledger

```text
Critical findings (C): 0
Major findings (M):    0
Minor findings (m):    0
```

No proof gap is delegated to controls.  The mandatory downstream independent
mathematical, source-domain, devil, and post-proof nonredundancy review of
the **final frozen bytes** has not yet occurred; that pending review is a
gate state, not a self-declared finding or authorization.

### 11.3 Machine-readable disposition

```text
PROOF_LEDGER_ID=P15R-P2-PROOF-v1.0
PHASE1_GATE_SHA256=949839c27f2af87dd9097807f2a5218e4df5de470e235145739bd95919a900cd
AUTHORIZED_SYMBOLIC_PROOF_COMPLETE=true
PROOF_SELF_VERDICT=PASS_C0_M0_m0
ACTIVE_R_EQUAL_P_ROUTE=HOMOGENEOUS_TRIANGULAR_SPLIT_AND_KULIKOV_ABSORPTION
WITHDRAWN_R_EQUAL_P_ROUTE=BOUNDED_ORDER_CHARACTER_SURJECTIVITY
R_NOT_EQUAL_P_ROUTE=EXACT_ORDER_KUMMER_CHEBOTAREV
P_R_EQUAL_2_FIREWALL=PASS
KERNEL_INTERNAL_ROOTS=PROVED
COMPLETE_FINITE_TRANSFINITE_ULM_LEDGER=PROVED
DUAL_REDUCED_GUARD=PROVED_BEFORE_CLASSIFICATION
TORSION_CLOSURE_QUOTIENT=PROVED
GLOBAL_IFF_BOTH_DIRECTIONS=PROVED
B2_NOT_ISOMORPHIC_B3=PROVED
MARKED_BARE_ACTUAL_MEASURE_TRACE_FIREWALL=PASS
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
INDEPENDENT_PROOF_REVIEW_REQUIRED=true
STANDALONE_PASS=HOLD
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

The file is to be frozen on its post-write SHA-256 and line count.  Those
external byte receipts do not authorize modification of this ledger or any
other pipeline artifact.
