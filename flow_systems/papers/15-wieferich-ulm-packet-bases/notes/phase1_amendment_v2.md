# Paper 15 replacement Phase-1 amendment v2 — exceptional-primary kernel absorption

Status: **ACTIVE / EXACT-BYTE RE-LOCK REQUIRED**  
Version: `P15R-P1-AMENDMENT-v2.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Proof, controls, Route A/B, manuscript, release, Git, and public
synchronization: `false`

## 1. Exact authority and supersession

This amendment binds:

```text
Papers 14--18 batch amendment v1
  sha256:afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802
replacement Paper-15 research protocol
  sha256:02693989ad616752c3f6f9e26ad0430a8f5942d0c8449cebe38b7105a2ab3d5a
replacement Paper-15 candidate lock
  sha256:811b4b515dd3f3c45cc96390a139e1d5e3a361d4fea566f0a473d91b8a73d722
transverse Pontryagin/Ulm precheck
  sha256:02bfac76eeeeb8ac81524c5230b4033de8aec43522d0b74bbc9c635c502732eb
Phase-1 amendment v1
  sha256:2fba2e4f163dbe223ee9eec5ea2d00848e97d2a78fe56ca57b54021837ec0bcc
final primary-source/precedent audit with v1 re-lock
  sha256:728e65f096aada4e52f1fb4a498ce8bf381b38b23418ebb53e93c4407b2c0916
```

Amendment v1 Section 2.1, the branch `r != p`, remains unchanged and still
requires its later exact proof.  Amendment v1 Section 2.2 is superseded in
full.  The assertions

```text
g_p(S_p[p^m]) = C_{p^infty}[p^m]
primitive divisor => bounded surjectivity at the same character order
```

are withdrawn and may not be used downstream.

The source audit's counterexample remains binding against amendment v1:
`ord_17(2)=8` while `v_2(17-1)=4`.  Extension of all characters from a
subgroup does not imply extension inside the same bounded-order subgroup.

## 2. Arrow and bounded-order correction

Let

```text
G=C_{p^a},
H=<h> subset G,
|H|=p^m,
h=u^(c p^(a-m)), p not dividing c.
```

The exponent coordinate and its dual are

```text
q_l: Z_p ->> H,             1 |-> h,
i:   H -> G,

dual(G) --i*--> dual(H) --dual(q_l)--> dual(Z_p)=C_{p^infty}.
```

The full restriction `i*` is surjective.  Its restriction

```text
dual(G)[p^m] -> dual(H)
```

need not be surjective when `a>m`.  Indeed, a faithful character of the
subgroup `C_8 subset C_16` extends to a character of order `16`, not one of
order at most `8`; the image of `dual(C_16)[8]` on that `C_8` has order `4`.

No later argument may replace full character extension by bounded-order
extension.

## 3. The exceptional branch `r=p`

Put

```text
S_p = direct_sum_{n>=1} S_n,
S_n = (C_{p^n})^(aleph_0),
g_p:S_p -> C_{p^infty},
K_{p,p}=ker(g_p).
```

Bang--Zsigmondy is used only in the exponent-embedding argument.  For every
`m>=1`, a primitive prime divisor of `p^(p^m)-1` gives an away prime `ell`
with `ord_ell(p)=p^m`.  The resulting coordinate detects the quotient
`Z_p/p^m Z_p`; hence the pro-`p` exponent map is injective.  Compactness of
the domain and Hausdorffness of the ambient product make it a closed
embedding, and Pontryagin duality gives the full epimorphism `g_p` above.

No conclusion about `v_p(ell-1)` or the order of a character preimage is
drawn from this primitive divisor.

## 4. Kernel-absorption lemma

The `r=p` theorem must use the following purely algebraic lemma.

> For every prime `p` and every homomorphism
> 
> ```text
> g: direct_sum_{n>=1}(C_{p^n})^(aleph_0) -> C_{p^infty},
> ```
> 
> its kernel is isomorphic to
> `direct_sum_{n>=1}(C_{p^n})^(aleph_0)`.

The proof obligations are frozen as follows.

### 4.1 Homogeneous-block reduction

For each `n`, restrict `g` to

```text
g_n:S_n -> C_{p^infty}[p^n].
```

Choose a basis `(e_{n,j})_{j>=0}` for `S_n`.  Choose `e_{n,0}` whose image
has maximal order among the finitely many possible image orders; if `g_n=0`,
choose any basis element.  The subgroups of the finite cyclic target are
linearly ordered, so `g_n(e_{n,0})` generates `g_n(S_n)`.  For each `j>0`
choose `c_{n,j}` in `Z/p^n Z` with

```text
g_n(e_{n,j})=c_{n,j} g_n(e_{n,0}),
e'_{n,j}=e_{n,j}-c_{n,j}e_{n,0}.
```

This simultaneous triangular basis change and its inverse are well-defined
on the algebraic direct sum.  It gives

```text
S_n=T_n direct_sum R_n,
T_n=direct_sum_{j>0}<e'_{n,j}> ~= (C_{p^n})^(aleph_0),
g(T_n)=0,
R_n=<e_{n,0}> ~= C_{p^n}.
```

### 4.2 Global split and Kulikov domain

Taking the direct sum over all `n` gives

```text
S_p=T direct_sum R,
T=direct_sum_n T_n ~= S_p,
g(T)=0,
R=direct_sum_n R_n ~= direct_sum_{n>=1}C_{p^n}.
```

Consequently

```text
ker(g)=T direct_sum ker(g|R).
```

The second summand is a subgroup of a direct sum of cyclic `p`-groups.
Kulikov's subgroup theorem may be applied only after this domain statement;
it makes `ker(g|R)` a direct sum of cyclic `p`-groups.  Since `R` is
countable, every cyclic-order multiplicity in this remainder is at most
`aleph_0`.  The group `T` already contains `aleph_0` copies of every
`C_{p^n}`, so absorption gives

```text
ker(g) ~= T ~= S_p.
```

The exact accessible published carrier for the subgroup theorem remains
Paul Hill, *Primary groups whose subgroups of smaller cardinality are direct
sums of cyclic groups*, Pacific Journal of Mathematics 42 (1972), 63--67,
Corollary 2, as bound by the source audit.

## 5. Exceptional-primary consequences

Applying the lemma to `g_p` yields

```text
K_{p,p} ~= S_p,
u_n(K_{p,p})=aleph_0 for every finite n,
p^omega K_{p,p}=0,
all transfinite Ulm invariants vanish.
```

The height statement also follows directly from

```text
p^omega K_{p,p} subset p^omega S_p = 0,
```

but that inclusion alone is not a substitute for the kernel-isomorphism and
finite-Ulm calculation.

Pontryagin duality then gives

```text
B_{p,(p)} ~= P_p,
closure(Tor(B_{p,(p)}))=B_{p,(p)},
B_{p,(p)}/closure(Tor(B_{p,(p)}))=1=C_{p^0},
kappa_p(p)=0.
```

This branch is uniform for odd `p` and `p=2`.

## 6. The `p=2` firewall

No proof may require primes `ell` satisfying

```text
v_2(ord_ell(2))=v_2(ell-1)>=3.
```

For `ell=1 mod 8`, supplementary quadratic reciprocity makes `2` a square
modulo `ell`, so the displayed equality is impossible.  Equivalently,
`Q(sqrt(2))` already lies in the relevant `2`-power cyclotomic tower; the
two Frobenius conditions cannot be prescribed independently.

This firewall applies only to the withdrawn bounded-surjectivity route.  It
does not affect the exponent embedding or the kernel-absorption lemma.

## 7. Unchanged theorem and owner boundaries

Subject to later proof and independent review, the following candidates are
unchanged:

1. the `r != p` Kummer--Chebotarev height calculation;
2. the off-local formulas for `kappa_r(p)`, including the `r=2!=p` sign
   normalization;
3. the compact torsion-closure translation;
4. the complete iff classification by the full `kappa` signature;
5. the explicit bare-group separation `B_2 not~=B_3`; and
6. the stop `UNIVERSAL_RECOVER_P=OPEN`.

The amendment proves none of these by itself.  It changes no actual
indiscrete packet, marked conductor, measured enhancement, standardized
flow, or Paper-16 owner.

## 8. Re-lock and authorization

An independent exact-byte source/mathematical re-lock must verify the block
decomposition, triangular automorphism, Kulikov domain, absorption, dual
translation, `p=2` firewall, and absence of regression in the `r != p`
branch.  Only a later integrated zero-finding Phase-1 gate may authorize a
symbolic proof.

```text
AMENDMENT_V2_ACTIVE=true
AMENDMENT_V1_R_EQUAL_P_BRANCH=SUPERSEDED_FALSE
R_EQUAL_P_BOUNDED_SURJECTIVITY=WITHDRAWN
R_EQUAL_P_KERNEL_ABSORPTION=PROPOSED_FOR_EXACT_REVIEW
R_EQUAL_P_ZSIGMONDY_USE=EXPONENT_EMBEDDING_ONLY
R_EQUAL_P_ODD_AND_TWO_UNIFORM=true
R_NOT_EQUAL_P_BRANCH=UNCHANGED_PENDING_PROOF
UNIVERSAL_RECOVER_P=OPEN
PROOF_AUTHORIZED=false
CONTROLS_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
STANDALONE_PASS=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```
