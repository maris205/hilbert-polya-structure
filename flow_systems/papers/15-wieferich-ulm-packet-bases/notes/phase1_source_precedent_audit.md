# Paper 15 replacement — independent primary-source and precedent audit

Status: **PHASE-1 SOURCE/PRECEDENT REVIEW — REVISE**  
Date: **2026-08-16 (Asia/Shanghai)**  
Mode: **ARS source verification + hostile domain/precedent audit**  
Findings: **C0 / M1 / m1**  
Exact-classification source feasibility: **GO, conditional on the branch repair in Finding M1**  
Proof authorization issued by this report: **false**  
Controls, Route A/B, manuscript, release, Git, archive, and public
synchronization authorized by this report: **false**

## 1. Scope and exact-byte lock

This report independently reviews source existence, source domain, theorem
locators, nearest precedent, and the feasibility of the proposed proof-source
chain.  It is not a symbolic proof and does not certify any candidate theorem
as proved.

The following files were read in full and re-hashed before this report was
written:

| Artifact | SHA-256 | Audit use |
|---|---|---|
| Papers 14--18 batch amendment v1 | `afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802` | replacement authority and owner firewall |
| replacement Paper-15 research protocol | `02693989ad616752c3f6f9e26ad0430a8f5942d0c8449cebe38b7105a2ab3d5a` | exact protocol under review |
| replacement Paper-15 candidate lock | `811b4b515dd3f3c45cc96390a139e1d5e3a361d4fea566f0a473d91b8a73d722` | exact candidate center and hard locks |
| transverse Pontryagin/Ulm precheck | `02bfac76eeeeb8ac81524c5230b4033de8aec43522d0b74bbc9c635c502732eb` | mathematical/source feasibility hypothesis under independent attack |
| adverse old-P15 precheck | `1598569c48d4382408bb3df933a1c5443984daf36b12e6377bae4590356a75f8` | binding reason the former standalone center is unavailable |

The directly relevant predecessor owner records were also read in full and
re-hashed:

| Owner record | SHA-256 | Binding boundary |
|---|---|---|
| Paper 2 Deninger source audit | `a4785e0fd56cb4e24211ea4d8f0e78a83ccdd6c942dc6572c87b2c1230ae521a` | `B_p` is an abstract compact Hausdorff quotient; the source packet projection is choice-dependent |
| Paper 2 mathematical proof audit | `aaab83c32eb9d6c172be192dbb14acc6ed927a972d61c24a90dbfe94ecd0dbae` | compact-group and cardinality owner; no packet-topology transport |
| Paper 9 source audit | `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` | exact source topology and no-topology-promotion boundary |
| Paper 9 Route-A owner audit | `f6e3c0ef065fb675d1f6408a411dba14de1581c5dfe4800dbddb532adaf8e730` | actual `Q_p` is a different, nontrivial indiscrete topology owner |
| Paper 9 final proof audit | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | `Q_p \cong U_p/H_p` only as the proved set model; not as compact `B_p` |

The old mixed-clock protocol is historical and was not treated as an owner or
proof source for the replacement project.

## 2. Review question and owner verdict

The exact source question is whether the literature supplies authoritative
inputs, at the right domains, for a new proof of

```text
B_p = (product_{ell != p} Z_ell^x) / p^Zhat
```

by characteristic pro-primary torsion-closure/Ulm invariants, without
identifying this compact group with Paper 9's actual quotient-topological
`Q_p`.

The owner split passes:

1. Deninger's source supplies the compact group
   `Zhat_(p)^x / p^Zhat` as the base of a choice-dependent packet
   fibration/set parametrization.
2. Paper 2 correctly owns this abstract compact Hausdorff quotient and its
   intrinsic compact-group facts.
3. Paper 9 owns the actual quotient `Q_p` with its inherited quotient topology,
   proves it nontrivial indiscrete, and expressly blocks a topological
   promotion from the common set model to compact `B_p`.
4. The replacement protocol stays on the Paper-2 compact-group owner.  No
   source reviewed here licenses transport to `Q_p`, a packet measure, a Haar
   system, a trace, or a determinant.

## 3. Retrieval and bounded-search record

Search and verification were performed on 2026-08-16.  Queries combined the
exact quotient notation, `p^Zhat`, `Wieferich`, `Ulm`, `torsion closure`,
`profinite`, `prescribed multiplicative order`, `Kummer`, and normalized
`p`-adic regulator terminology.  Searches covered arXiv, DOI/publisher pages,
author-hosted records, institutional repositories, and exact-title searches.

No new PDF was retained.  Source PDFs needed for exact locators were streamed
through text extraction and discarded; consequently this audit creates no PDF
manifest or redistribution claim.  The following negative statement is the
strongest licensed novelty language:

```text
NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH
```

It is a search-bounded result, not an absolute priority or nonexistence claim.

## 4. Primary and authoritative source matrix

### 4.1 Deninger owner

Christopher Deninger, *Dynamical systems for arithmetic schemes*, arXiv
`1807.06400v4`, especially equations (38)--(40), the paragraph immediately
after (39), Section 6, and Theorem 6.1; journal DOI
[`10.1016/j.indag.2024.05.007`](https://doi.org/10.1016/j.indag.2024.05.007).
The audited manifestation is
[`arXiv:1807.06400v4`](https://arxiv.org/abs/1807.06400v4).

Verified source scope:

- the compact group is
  `B_p = Zhat_(p)^x/p^Zhat = Aut(Fbar_p^x)/Aut(Fbar_p)`;
- the packet fibres over it after auxiliary choices;
- the fibration map depends on the choices named by Deninger; and
- this source statement does not identify the actual packet orbit-space
  topology with the compact topology on `B_p`.

This is the exact natural-owner source for the replacement.  It does not
contain the proposed Sylow, torsion-closure, Ulm, or iff-classification
calculation.

### 4.2 Kiehlmann, Pontryagin/Ulm, and torsion closure

Jonathan Kiehlmann, *Classifications of countably-based abelian profinite
groups*, *Journal of Group Theory* 16 (2013), 141--157, DOI
[`10.1515/jgt-2012-0024`](https://doi.org/10.1515/jgt-2012-0024); audited
author manuscript
[`arXiv:1101.3005v3`](https://arxiv.org/abs/1101.3005).

Exact relevant locators and domains are:

- **Theorem 1.1:** for an abelian profinite group `G`, the dual of the closure
  of its torsion is `G^*/ih(G^*)`.  Equivalently, the annihilator of the
  torsion closure is the infinite-height subgroup of the discrete dual.
- **Definition 1.3 and Theorem 1.4:** the dual-reduced condition is the absence
  of a nontrivial continuous torsion-free quotient, equivalently reducedness
  of the discrete dual; a general abelian pro-`r` group also has a possible
  `Z_r` product factor.
- **Theorem 1.8:** two countably based abelian **dual-reduced** pro-`r` groups
  with the same full torsion sequence are topologically isomorphic.
- **Proposition 2.3:** the closure of torsion in a countably based pro-`r`
  group is Cartesian; the proof invokes Prüfer's theorem for a countable
  `r`-group with no nonzero infinite-height elements.

These results make the proposed compact-side translation and final
topological classification source-feasible.  They do not reduce the full
torsion sequence to one integer automatically.  The new proof must first
establish countable basing, reducedness/no Prüfer divisible summand, every
finite Ulm invariant, the full transfinite tail, and the characteristic
primary product decomposition.  Only then can Theorem 1.8 be invoked.

### 4.3 Prüfer and Kulikov subgroup inputs

The exact accessible published source checked for the subgroup step is Paul
Hill, *Primary groups whose subgroups of smaller cardinality are direct sums
of cyclic groups*, *Pacific Journal of Mathematics* 42 (1972), 63--67,
[`publisher PDF`](https://msp.org/pjm/1972/42-1/pjm-v42-n1-p08-s.pdf).

- Hill's Theorem 1 explicitly uses Prüfer's theorem that a countable primary
  group without elements of infinite height is a direct sum of cyclic groups.
- Hill's Corollary 2 states Kulikov's subgroup theorem: a subgroup of a direct
  sum of cyclic primary groups is a direct sum of cyclic groups.

This source supports the proposed kernel decomposition after, but not before,
the kernel has been typed as a subgroup of a direct sum of cyclic `r`-groups.
It does not compute the packet-base kernel or its heights.

### 4.4 Bang--Zsigmondy and the omitted `p` coordinate

The primary historical source is K. Zsigmondy, *Zur Theorie der
Potenzreste*, *Monatshefte für Mathematik und Physik* 3 (1892), 265--284,
DOI [`10.1007/BF01692444`](https://doi.org/10.1007/BF01692444).  The exact
classical exception list was cross-checked against later peer-reviewed
statements of the theorem.

For coprime positive `a>b`, a primitive divisor of `a^n-b^n` exists except
for:

1. `n=1` and `a-b=1`;
2. `n=2` and `a+b` a power of `2`; and
3. `(a,b,n)=(2,1,6)`.

The replacement application takes `a=p`, `b=1`, and `n=p^m`, `m>=1`.
None of the exceptions applies:

- `n=1` never occurs;
- `n=2` occurs only for `p=2,m=1`, when `p+1=3` is not a power of `2`;
- `n=6` is not a prime power.

Thus a primitive prime divisor `ell` exists, `ell != p`, and
`ord_ell(p)=p^m`.  This makes detection of every finite `p`-power quotient of
the omitted `p`-Sylow exponent coordinate source-feasible.  The final proof
must state this exception check; citing “Zsigmondy” without it is
insufficient.

### 4.5 Dirichlet and exact valuation classes

Dirichlet's original 1837 theorem is available in English translation as
[`arXiv:0808.1408`](https://arxiv.org/abs/0808.1408).  A modern authoritative
statement and proof locator is Andrew V. Sutherland, MIT 18.785 Lecture 18,
Theorem 18.1,
[`Dirichlet L-functions, primes in arithmetic progressions`](https://math.mit.edu/classes/18.785/2021fa/LectureNotes18.pdf).

For every prime `r` and `n>=1`, apply Dirichlet with modulus `r^(n+1)` and
residue `1+r^n`.  The residue is coprime to the modulus, and every resulting
prime `ell` satisfies exactly

```text
v_r(ell-1)=n.
```

This includes `r=2,n=1`, where the class is `3 mod 4`.  Therefore the
countably infinite multiplicity of every cyclic order in `P_r` is directly
source-feasible; no prime number theorem or GRH is needed.

### 4.6 Chebotarev and prescribed-order comparators

The qualitative theorem needed is the ordinary finite-extension Chebotarev
density theorem.  The primary bibliographic record checked is J. C. Lagarias
and A. M. Odlyzko, *Effective versions of the Chebotarev density theorem*, in
*Algebraic Number Fields* (1977), pp. 409--464, as recorded on
[`Lagarias's author page`](https://websites.umich.edu/~lagarias/zeta.html).
For a stable theorem statement and proof, see Andrew V. Sutherland, MIT 18.785
Lecture 28, Theorem 28.9,
[`Global class field theory, the Chebotarev density theorem`](https://math.mit.edu/classes/18.785/2025/LectureNotes28.pdf).
It assigns positive density `#C/#G` to every nonempty conjugacy-stable
Frobenius condition in a finite Galois extension.

Pieter Moree, *On primes p for which d divides ord_p(g)*, *Functiones et
Approximatio* 33 (2005), 85--95,
[`arXiv:math/0407421`](https://arxiv.org/abs/math/0407421), is the nearest
verified multiplicative-order comparator.  Its `d | ord_ell(g)` density
theorems do not by themselves impose the simultaneous exact condition
`v_r(ell-1)=v_r(ord_ell(p))=m`; they cannot replace the paper's finite-field
and Kummer--Chebotarev argument.

### 4.7 Odd and 2-adic unit logarithms

Keith Conrad, *Infinite series in p-adic fields*, Example 8.15,
[`author-hosted PDF`](https://kconrad.math.uconn.edu/blurbs/gradnumthy/infseriespadic.pdf),
gives the isomorphisms

```text
log : 1+r Z_r  -> r Z_r       (r odd),
log : 1+4 Z_2  -> 4 Z_2.
```

Conrad, *p-adic interpolation*, Theorem 2.6 and Remark 2.8,
[`author-hosted PDF`](https://kconrad.math.uconn.edu/math5020f11/padicinterpolation.pdf),
gives the exact valuation behavior and

```text
Z_2^x = {+1,-1} x (1+4 Z_2).
```

These are sufficient authoritative sources for the local normalization,
provided the final proof performs the calculation in Section 6 below and
does not erase the finite sign coordinate.

## 5. Hostile audit of the full-height lemma (protocol 4.4; precheck 5.3--5.4)

### 5.1 Exact target

For the off-local restriction map

```text
g:S_r -> C_{r^infty},
```

the required claim is

```text
g(S_r[r^m]) = C_{r^infty}[r^m]       for every m>=1.
```

A prime `ell != p,r` with

```text
v_r(ell-1)=m,
v_r(ord_ell(p))=m
```

does supply a coordinate character whose restriction has full order `r^m`.
Thus the witness condition is exactly strong enough.  A source proving only
`r^m | ord_ell(p)` without controlling `v_r(ell-1)` would not be enough.

### 5.2 Odd `r != p`

Let

```text
F = Q(zeta_r),
C_m = Q(zeta_{r^(m+1)}),
L = F(p^(1/r)).
```

The source-feasible self-contained argument is:

1. `X^r-p` is Eisenstein at every prime of `F` above `p`, because `p != r`
   is unramified in `F`; hence `L/F` has degree `r` and is ramified above
   `p`.
2. `C_m/F` is ramified only above `r`.  Since `L/F` has prime degree,
   `L intersect C_m = F`; otherwise `L` would lie in `C_m`, contradicting
   ramification at `p`.
3. In the compositum, choose an automorphism that is identity on
   `Q(zeta_{r^m})`, nonidentity on `Q(zeta_{r^(m+1)})`, and nonidentity on
   `p^(1/r)` while fixing `zeta_r`.  Disjointness makes these restrictions
   compatible.
4. Qualitative Chebotarev gives infinitely many rational primes with that
   Frobenius conjugacy class.
5. The cyclotomic restrictions give `v_r(ell-1)=m`.  Since `ell=1 mod r`
   and the Kummer restriction is nontrivial, `p` is not an `r`th power in
   `F_ell^x`.  In the cyclic group `F_ell^x`, whose `r`-part has order
   `r^m`, this is equivalent to `v_r(ord_ell(p))=m`.

This closes source feasibility without GRH.  Moree is corroborative only;
the exact five-step lemma must be proved in the paper.

### 5.3 `r=2 != p`

Here `p` is odd.  Put

```text
C_m = Q(zeta_{2^(m+1)}),
L = Q(sqrt(p)).
```

The fields are linearly disjoint over `Q`: `L` is ramified at `p`, whereas
`C_m` is ramified only at `2`.  Choose a Frobenius automorphism that fixes
`zeta_{2^m}`, moves `zeta_{2^(m+1)}`, and acts nontrivially on `sqrt(p)`.
Chebotarev then gives infinitely many `ell` with

```text
v_2(ell-1)=m
```

and with `p` a nonsquare modulo `ell`.  In the cyclic group
`F_ell^x`, nonsquareness plus the exact `2`-part `2^m` is equivalent to

```text
v_2(ord_ell(p))=m.
```

The case `m=1` is included: the cyclotomic condition is `ell=3 mod 4`, and
the independent quadratic condition is `(p/ell)=-1`.  No unspoken
odd-prime Kummer argument is being used at `2`.

### 5.4 The `r=p` branch is different

The ramification-disjointness argument above requires `r != p`.  When
`r=p`, both the Kummer and `p`-power cyclotomic extensions ramify at `p`, so
the stated intersection proof cannot simply be reused.  The required
bounded-order witnesses are instead available directly from the
Bang--Zsigmondy application in Section 4.4, or the relevant bounded
surjectivity must be derived separately from the closed embedding and dual
map.

This distinction is the report's Major finding M1.  The precheck's Section
5.4 correctly says “for `r != p`,” but the replacement protocol's Section
4.4 states the off-local saturation obligation without an equally explicit
branch split and then immediately proposes the Kummer--Chebotarev witness.
Before a proof gate is frozen, the protocol must say:

```text
r != p: exact Kummer--Chebotarev proof above;
r  = p: Bang--Zsigmondy/bounded-surjectivity proof, with no disjointness claim.
```

The repair is local and source-feasible, but it is load-bearing because an
invalid field-intersection argument would infect the kernel-height theorem.

## 6. Hostile audit of the `r=2` normalization

For odd `p`, choose `epsilon_p in {+1,-1}` so that

```text
u_p = epsilon_p p in 1+4 Z_2.
```

The local exponent map into

```text
Z_2^x = C_2 x (1+4 Z_2)
```

has a finite sign component and a principal-unit component.  Under the
normalized logarithmic coordinate `log(5)` on `1+4Z_2`, the latter has
coefficient

```text
log(u_p)/log(5).
```

Conrad's exact valuation formula gives

```text
v_2(log(u_p)/log(5)) = v_2(u_p-1)-2.
```

If `p=1 mod 4`, then `u_p=p` and `v_2(p+1)=1`; if `p=3 mod 4`, then
`u_p=-p` and `v_2(p-1)=1`.  In both cases

```text
v_2(u_p-1)-2
  = v_2(p^2-1)-3
  = kappa_2(p).
```

Therefore the protocol's `-3` normalization is correct.  The result does
not license deletion of the sign summand:

- when `p=3 mod 4`, the sign character restricts nontrivially to the order-2
  part of the target;
- after the abstract extra `C_2` is absorbed into the countably infinite
  `C_2` multiplicity of `P_2`, that character belongs to the reduced
  `S_2` side of the restriction map; and
- the full-height proof must still use off-local saturation to cancel every
  bounded target value.

Thus the `r=2` formula and sign firewall are source-feasible as written.  A
proof using `log(p)` indiscriminately on all odd `p`, or replacing `-3` by
`-2`, would be wrong.

## 7. Exact-classification feasibility

The proposed iff classification is source-feasible, but no cited theorem
states it for these `B_p`.  The minimum legitimate chain is:

1. prove `e_p:Zhat -> U_p` is a closed embedding;
2. compute each characteristic pro-`r` Sylow ambient group;
3. dualize the exact compact sequence;
4. prove the local coefficient and the correct branch of full-height
   saturation;
5. compute all finite Ulm invariants and the entire transfinite tail;
6. prove the dual is reduced, so Kiehlmann Theorem 1.8 is in domain;
7. use Kiehlmann Theorem 1.1 to identify the annihilator of the compact
   torsion closure;
8. use Proposition 2.3/Prüfer to identify its Cartesian type; and
9. assemble the characteristic pro-primary factors without retaining
   presentation labels.

If those steps establish

```text
u_n(K_{p,r}) = aleph_0                 for all finite n,
r^omega K_{p,r} = C_{r^kappa_r(p)},
```

with the stated successor tail, then the full torsion sequence is determined
by `kappa_r(p)`, and Kiehlmann supplies necessity and sufficiency on each
dual-reduced pro-`r` factor.  Canonical primary decomposition then gives the
global iff criterion.

Conversely, merely proving the finite quotient

```text
B_{p,(r)}/closure(Tor(B_{p,(r)})) = C_{r^kappa_r(p)}
```

does not by itself prove the iff classification: distinct countable reduced
`r`-groups can share the same infinite-height subgroup.  The complete finite
and transfinite Ulm ledger remains load-bearing.

## 8. Nearest precedent and nonredundancy

No direct source located in the bounded search combines all of the following:

- Deninger's exact compact quotient `B_p`;
- its complete characteristic pro-primary decomposition;
- a Kummer--Chebotarev bounded-height saturation theorem;
- Wieferich valuations as the complete transfinite defect;
- compact torsion-closure indices; and
- an iff topological classification of the family.

The nearest verified precedents are complementary rather than duplicative:

| Source family | What it supplies | What it does not supply |
|---|---|---|
| Deninger | the exact natural compact owner `B_p` | no Ulm/torsion-closure classification |
| Kiehlmann | full countably based dual-reduced pro-primary classification via torsion/Ulm sequences | no arithmetic computation for `B_p` |
| Prüfer/Kulikov/Hill | cyclic-sum structure of the relevant reduced kernels | no packet-base or Wieferich calculation |
| Moree and prescribed-order literature | densities for divisibility constraints on multiplicative orders | not the simultaneous exact valuation lemma and not the compact-group classification |
| normalized `p`-adic regulator / `p`-rationality literature | close arithmetic analogy between local-unit quotients and Wieferich defects | a different fixed-prime/local-global owner; no classification of the all-away compact groups `B_p` by Ulm data |

Accordingly the candidate has a source-feasible nonroutine center if, and only
if, the complete theorem chain survives proof and independent review.  A
single `B_2 not~ B_3` calculation, the standard annihilator formula, or a
marked conductor grading remains below that threshold.

The universal statement that the bare topological group `B_p` determines
`p` is not supported by any verified source and remains outside the candidate
theorem.  This audit found no theorem proving injectivity of
`p |-> (kappa_r(p))_r`.

## 9. Findings

### Critical findings — C0

No critical source-integrity or theorem-domain failure was found.

### Major finding — M1

**The height-saturation source route must be split explicitly at `r=p`.**

The Kummer/cyclotomic linear-disjointness proof is valid for `r != p`, where
ramification at `p` separates the Kummer extension from the `r`-power
cyclotomic tower.  It is not the correct argument when `r=p`.  The precheck
contains the restriction; protocol Section 4.4 does not freeze it with equal
precision.  Amend that scope before proof authorization and route `r=p`
through Bang--Zsigmondy or an independently proved bounded-surjectivity
lemma.

### Minor finding — m1

**The precheck's direct Lagarias--Odlyzko PDF URL is stale.**

The URL `https://www.dtc.umn.edu/~odlyzko/doc/arch/cheb.density.pdf` returned
HTTP 404 during this audit.  The bibliographic work is real and verified on
Lagarias's author page, and an authoritative exact theorem statement is
available in Sutherland's MIT Lecture 28, Theorem 28.9.  A future source lock
must replace the stale direct URL with a stable manifestation/record and must
not claim that the unavailable URL was read.

## 10. Verdict and authorization firewall

```text
REPORT_ID=P15R-PHASE1-SOURCE-PRECEDENT-AUDIT-v1.0
VERDICT=REVISE
FINDINGS=C0/M1/m1
OWNER_BOUNDARY=PASS
DENINGER_OWNER_SOURCE=VERIFIED
KIEHLMANN_DOMAIN_SOURCE=VERIFIED_WITH_DUAL_REDUCED_GUARD
KULIKOV_PRUEFER_SOURCE=VERIFIED
ZSIGMONDY_EXCEPTION_APPLICATION=SOURCE_FEASIBLE
DIRICHLET_EXACT_VALUATION_CLASSES=SOURCE_FEASIBLE
FULL_HEIGHT_LEMMA_R_NE_P=SOURCE_FEASIBLE_SELF_CONTAINED_PROOF_REQUIRED
FULL_HEIGHT_LEMMA_R_EQ_P=SEPARATE_ZSIGMONDY_OR_BOUNDED_SURJECTIVITY_BRANCH_REQUIRED
R2_NORMALIZATION=VERIFIED_SOURCE_FEASIBLE
EXACT_IFF_CLASSIFICATION=SOURCE_FEASIBLE_UNPROVED
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
NOVELTY_LANGUAGE=NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH
NEW_PDF_RETAINED=false
PROOF_AUTHORIZED=false
CONTROLS_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```

The correct next action is a versioned Phase-1 protocol repair resolving M1
and m1, followed by an exact-byte re-review.  This report itself grants no
symbolic-proof authority.

---

## Closure addendum v1 — exact-byte source re-lock

Addendum date: **2026-08-16 (Asia/Shanghai)**  
Addendum scope: **narrow review of `P15R-P1-AMENDMENT-v1.0` only**  
Immutable report-prefix SHA-256 before this append:
`983644f24e76cc219b4966024bb5235963656ef1cd8a0555f1d38651efe4e83e`  
Amendment reviewed in full:
`papers/15-wieferich-ulm-packet-bases/notes/phase1_amendment_v1.md`  
Amendment SHA-256:
`2fba2e4f163dbe223ee9eec5ea2d00848e97d2a78fe56ca57b54021837ec0bcc`

### A. Exact source-record closure

The amendment withdraws the stale URL

```text
https://www.dtc.umn.edu/~odlyzko/doc/arch/cheb.density.pdf
```

and expressly prohibits representing it as an inspected manifestation.  The
withdrawn address still resolves to an HTTP-404 endpoint in this re-lock.

The two replacement records were independently reopened:

1. Lagarias's University of Michigan author page lists J. C. Lagarias and
   A. M. Odlyzko, *Effective versions of the Chebotarev density theorem*, in
   *Algebraic Number Fields*, Academic Press, 1977, pp. 409--464.
2. Sutherland's MIT 18.785 Lecture 28 PDF is available; Theorem 28.9 states
   the finite-Galois-extension Chebotarev density theorem for a
   conjugacy-stable subset `C`, with density `#C/#G`.

The amendment also correctly says that these records do not construct the
packet-specific Kummer compositum or its Frobenius element.  Effective result:

```text
old m1 = CLOSED
```

### B. `r != p` branch

Section 2.1 now explicitly limits the ramification-separation argument to
`r != p`, retains the required compatibility over `Q(zeta_r)`, separates the
quadratic `r=2` branch, includes `m=1`, and prohibits hidden GRH.  This is the
scope repair requested by the original audit and is source-feasible.

```text
R_NOT_EQUAL_P_BRANCH = RELOCK_PASS
```

### C. `r=p` branch does not establish bounded surjectivity

Section 2.2 correctly avoids a Kummer/cyclotomic disjointness claim at `p`,
but its Bang--Zsigmondy replacement does **not** prove the displayed bounded
surjectivity identity.

Let the pro-`p` Sylow of one away coordinate be cyclic of order `p^a`, and
suppose the coordinate image of the exponent generator has order `p^b`.
On duals, restriction has the form

```text
C_{p^a} -> C_{p^infty},
k         |-> k/p^b
```

up to a unit and the chosen cyclic coordinates.  Restricting the source to
characters of order at most `p^m` forces `v_p(k)>=a-m`.  Its image can contain
an element of exact order `p^m` only when the exponent image generates the
full pro-`p` Sylow at that coordinate (`a=b`); knowing only `b=m` is
insufficient when `a>m`.

Bang--Zsigmondy applied to `p^(p^m)-1` gives a primitive divisor `ell` with

```text
ord_ell(p)=p^m,
```

but it gives only `p^m | ell-1`, not
`v_p(ell-1)=m`.  The gap is realized by the smallest concrete branch:

```text
p=2, m=3, ell=17,
ord_17(2)=8,
v_2(17-1)=4.
```

Here the coordinate pro-2 Sylow is `C_16`, while `2` generates only its
order-8 subgroup.  A character of `C_16` of order at most `8` restricts to a
character of that subgroup of order at most `4`; it cannot reach an element
of order `8` in `C_{2^infty}[8]`.  Thus the amendment's inference

```text
primitive divisor of p^(p^m)-1
  => g_p(S_p[p^m])=C_{p^infty}[p^m]
```

is false as stated.

This does not prove that the desired `r=p` saturation theorem is false.  It
shows that the frozen source route does not prove it.  A further amendment
must supply one of the following and undergo a new exact-byte review:

1. primes `ell` for which the exponent image generates the full pro-`p`
   Sylow and that full order is at least `p^m`; or
2. an independent group-theoretic proof that the combined bounded
   restriction map is surjective.

Zsigmondy alone is not such a theorem.  Therefore the original M1 is not
closed.

### D. Effective verdict after amendment v1

```text
ADDENDUM_ID=P15R-PHASE1-SOURCE-RELOCK-v1.0
AMENDMENT_SHA256=2fba2e4f163dbe223ee9eec5ea2d00848e97d2a78fe56ca57b54021837ec0bcc
VERDICT=REVISE
EFFECTIVE_FINDINGS=C0/M1/m0
OLD_M1=OPEN_R_EQUAL_P_BOUNDED_SURJECTIVITY_NOT_PROVED
OLD_m1=CLOSED
R_NOT_EQUAL_P_HEIGHT_ROUTE=PASS
R_EQUAL_P_HEIGHT_ROUTE=FAIL_AS_STATED
STABLE_LAGARIAS_BIBLIOGRAPHIC_RECORD=VERIFIED
SUTHERLAND_THEOREM_28_9=VERIFIED
STALE_CHEBOTAREV_URL=WITHDRAWN_404
EXACT_CLASSIFICATION_SOURCE_FEASIBILITY=HOLD_AT_R_EQUAL_P_HEIGHT_BRANCH
PROOF_AUTHORIZED=false
CONTROLS_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```

This append preserves every byte of the original report prefix.  It does not
authorize proof or any downstream action.

---

## Closure addendum v2 — exceptional-primary kernel re-lock

Addendum date: **2026-08-16 (Asia/Shanghai)**  
Addendum scope: **independent exact-byte mathematical/source/domain review of
`P15R-P1-AMENDMENT-v2.0` only**  
Immutable report-prefix size before this append: **27342 bytes / 684 lines**  
Immutable report-prefix SHA-256 before this append:
`728e65f096aada4e52f1fb4a498ce8bf381b38b23418ebb53e93c4407b2c0916`  
Amendment reviewed in full:
`papers/15-wieferich-ulm-packet-bases/notes/phase1_amendment_v2.md`  
Amendment SHA-256:
`386ee5775c30ac263f4f72983fb7555b16ade8e72b4597f73fd11460445fcb80`

This addendum is a Phase-1 feasibility re-lock, not a symbolic proof.  It
does not certify the unchanged off-local theorem chain as proved and does not
issue any downstream authorization.

### A. Exact-byte scope and precedence

Before review, the following artifacts were read in full and independently
re-hashed:

| Artifact | SHA-256 | Re-lock use |
|---|---|---|
| replacement research protocol | `02693989ad616752c3f6f9e26ad0430a8f5942d0c8449cebe38b7105a2ab3d5a` | base obligations and authorization firewall |
| replacement candidate lock | `811b4b515dd3f3c45cc96390a139e1d5e3a361d4fea566f0a473d91b8a73d722` | bare owner and complete-signature candidate |
| transverse Pontryagin/Ulm precheck | `02bfac76eeeeb8ac81524c5230b4033de8aec43522d0b74bbc9c635c502732eb` | original mathematical architecture under hostile recheck |
| Phase-1 amendment v1 | `2fba2e4f163dbe223ee9eec5ea2d00848e97d2a78fe56ca57b54021837ec0bcc` | withdrawn exceptional-primary route |
| final source report plus v1 re-lock, exact prefix to this addendum | `728e65f096aada4e52f1fb4a498ce8bf381b38b23418ebb53e93c4407b2c0916` | binding v1 counterexample and source ledger |
| Phase-1 amendment v2 | `386ee5775c30ac263f4f72983fb7555b16ade8e72b4597f73fd11460445fcb80` | exact amendment under review |
| Papers 14--18 batch amendment v1 | `afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802` | replacement authority and owner firewall |
| Papers 14--18 batch amendment v2 | `3aa08c2cc2e38b02c83316d188f418d157abd43cf881e447cc28bf083ed3684b` | unchanged five-slot/downstream firewall context |

Amendment v2 correctly supersedes only amendment-v1 Section 2.2.  Amendment-
v1 Section 2.1 (`r != p`) and every base owner, marked/bare, universal-
recovery, standalone, and authorization boundary remain in force.

### B. Bounded-restriction counterexample and arrow audit

The v1 re-lock's objection is exact.  With

```text
G=C_{p^a}=<u>,
H=<u^(c p^(a-m))> ~= C_{p^m},
p not dividing c,
```

identify `dual(G)` with `Z/p^a Z`.  Restriction to `H` sends `k` to
`ck mod p^m`.  The subgroup `dual(G)[p^m]` consists of the residue classes
divisible by `p^(a-m)`, so its restriction image can be a proper subgroup of
`dual(H)`.  For `C_8 subset C_16`, characters of `C_16` of order at most
`8` restrict only to the even characters of `C_8`, an image of order `4`.

Thus full character extension does not imply bounded-order extension.
Amendment v2 withdraws precisely the invalid implication and does not use it
elsewhere.

```text
V1_BOUNDED_RESTRICTION_INFERENCE = CONFIRMED_FALSE
V2_ARROW_CORRECTION = PASS
```

### C. Homogeneous blocks and the infinite triangular change of basis

For

```text
S_n=(C_{p^n})^(aleph_0),
g_n:S_n -> C_{p^infty}[p^n],
```

the possible orders of the basis images form a finite set contained in
`{1,p,...,p^n}`.  A maximal order is therefore attained.  Since subgroups of
the finite cyclic target are linearly ordered, a basis vector `e_{n,0}` of
maximal image order generates `g_n(S_n)`.  Hence every other image is
`c_{n,j}g_n(e_{n,0})` for a lift `c_{n,j} in Z/p^n Z`.

Keeping `e_{n,0}` and replacing

```text
e_{n,j} by e'_{n,j}=e_{n,j}-c_{n,j}e_{n,0}  (j>0)
```

is an automorphism of the algebraic direct sum.  Both the displayed map and
its inverse `e_{n,j}=e'_{n,j}+c_{n,j}e_{n,0}` send every finite-support
element to a finite-support element; no infinite sum is introduced.  The
coefficient `1` in the `e_{n,j}` coordinate also shows that each
`e'_{n,j}` still has order `p^n` and that the new family is a basis.  It
follows exactly that

```text
S_n=T_n direct_sum R_n,
T_n ~= (C_{p^n})^(aleph_0),
R_n ~= C_{p^n},
g(T_n)=0.
```

```text
HOMOGENEOUS_BLOCK_REDUCTION = PASS
INFINITE_TRIANGULAR_AUTOMORPHISM = PASS
```

### D. Global split, Kulikov domain, and countable absorption

Taking algebraic direct sums over `n` preserves the block decompositions:

```text
S_p=T direct_sum R,
T=direct_sum_n T_n ~= S_p,
R=direct_sum_n R_n ~= direct_sum_{n>=1} C_{p^n}.
```

Because `g(T)=0`, uniqueness in this direct sum gives the equality, not just
an abstract extension,

```text
ker(g)=T direct_sum ker(g|R).
```

The source domain is now exact.  `R` is a primary abelian group that is a
direct sum of cyclic groups, and `ker(g|R)` is its subgroup.  Paul Hill,
*Primary groups whose subgroups of smaller cardinality are direct sums of
cyclic groups*, *Pacific Journal of Mathematics* 42 (1972), 63--67,
Corollary 2 (pp. 66--67), states Kulikov's theorem in exactly this domain:
a subgroup of a direct sum of cyclic primary groups is a direct sum of
cyclic groups.  The [publisher PDF](https://msp.org/pjm/1972/42-1/pjm-v42-n1-p08-p.pdf)
was independently reopened for this re-lock.

Moreover, `R` and its subgroup are countable.  In a cyclic-sum decomposition
of `ker(g|R)`, every order multiplicity is therefore at most `aleph_0`.
The summand `T` already has `aleph_0` copies of every `C_{p^n}`, and cardinal
addition gives `aleph_0+mu_n=aleph_0` for every `mu_n<=aleph_0`.  Therefore

```text
ker(g) ~= T ~= S_p.
```

No countability hypothesis is silently substituted for Kulikov's actual
domain; countability is used only in the subsequent multiplicity absorption.

```text
GLOBAL_KERNEL_SPLIT = PASS
KULIKOV_DOMAIN = PASS
COUNTABLE_CYCLIC_REMAINDER_ABSORPTION = PASS
```

### E. Infinite height and compact torsion closure

Every element of `S_p` has finite support.  For sufficiently large `m`, a
nonzero finite-support element cannot lie in `p^mS_p`; hence

```text
p^omega S_p=intersection_m p^mS_p=0.
```

The kernel is both a subgroup of `S_p` and isomorphic to `S_p`, so

```text
p^omega K_{p,p}=0,
u_n(K_{p,p})=aleph_0 for every finite n,
```

and there is no hidden divisible Prüfer summand or transfinite tail.

Jonathan Kiehlmann, *Classifications of countably-based abelian profinite
groups*, [arXiv:1101.3005v3](https://arxiv.org/html/1101.3005v3), Theorem
1.1 identifies the annihilator of the compact torsion closure with the
infinite-height subgroup of the discrete dual; for a discrete `p`-group this
is `p^omega K`.  Consequently the annihilator here is zero.  Equivalently,
dualizing the kernel isomorphism gives

```text
B_{p,(p)} ~= dual(S_p)=P_p,
closure(Tor(B_{p,(p)}))=B_{p,(p)},
B_{p,(p)}/closure(Tor(B_{p,(p)}))=1=C_{p^0}.
```

The density statement also has the direct check that finite-support elements
are torsion and dense in the Cartesian product `P_p`.

```text
P_OMEGA_EXCEPTIONAL_BRANCH = ZERO_PASS
PONTRYAGIN_TORSION_CLOSURE_TRANSLATION = PASS
KAPPA_P_OF_P = ZERO_PASS
```

### F. `p=2` firewall and the restricted Zsigmondy use

The quadratic firewall is correct.  If `ell=1 mod 8`, supplementary
quadratic reciprocity gives

```text
(2/ell)=(-1)^((ell^2-1)/8)=1.
```

Thus `2` is a square in the cyclic group `F_ell^x`, so the `2`-part of its
order is strictly smaller than the full `2`-part of `ell-1`.  The condition

```text
v_2(ord_ell(2))=v_2(ell-1)>=3
```

is impossible.  This confirms that the withdrawn same-order
bounded-surjectivity route cannot be repaired by imposing the old Frobenius
conditions at `p=r=2`.

Amendment v2 instead uses Bang--Zsigmondy only to obtain, for each `m`, an
away prime with `ord_ell(p)=p^m`.  That coordinate detects
`Z_p/p^mZ_p`, and all such quotients detect `Z_p`; compact-to-Hausdorff
injectivity then makes the exponent map a closed embedding.  No value of
`v_p(ell-1)` and no bounded order for a character preimage is inferred.
The exception audit already frozen in Section 4.4 of the report remains
valid for the exponents `p^m`.

```text
P2_QUADRATIC_FIREWALL = PASS
ZSIGMONDY_USE = EXPONENT_EMBEDDING_ONLY_PASS
ZSIGMONDY_BOUNDED_CHARACTER_EXTENSION = NOT_USED
```

### G. No regression in the `r != p` branch

Amendment v2 leaves amendment-v1 Section 2.1 unchanged.  The hostile recheck
found no regression:

1. for odd `r != p`, `Q(zeta_r,p^(1/r))/Q(zeta_r)` is ramified above `p`,
   while the added `r`-power cyclotomic layer is ramified only above `r`, so
   the required restrictions are compatible over `Q(zeta_r)`;
2. the chosen cyclotomic Frobenius gives exact `v_r(ell-1)=m`, and the
   nontrivial Kummer restriction makes `p` a non-`r`th-power, which in the
   cyclic residue group gives exact `v_r(ord_ell(p))=m`;
3. for `r=2 != p`, the base `p` is odd, `Q(sqrt(p))` is ramified at `p` and
   is disjoint from the `2`-power cyclotomic tower, including the separate
   `m=1` condition; and
4. this quadratic `r=2 != p` branch is disjoint from the firewall at
   `r=p=2`.  Neither branch licenses hidden GRH or deletion of the local
   sign character.

Therefore the previously re-locked off-local saturation and the
`kappa_2(p)=v_2(p^2-1)-3` normalization remain source-feasible and pending
their later exact proof.

```text
R_NOT_EQUAL_P_BRANCH = RELOCK_PASS_NO_REGRESSION
R2_NOT_EQUAL_P_SIGN_FIREWALL = UNCHANGED_PASS
```

### H. Complete iff source feasibility

The repair restores the source-feasible proof chain without claiming that
the chain has already been proved.  The exceptional characteristic factor
now has the fixed type `B_{p,(p)}~=P_p` and zero transfinite defect.  For
`r != p`, the unchanged proposed calculation supplies countable reduced
duals with all finite Ulm invariants `aleph_0` and the stated finite
`r^omega` tail.  Kiehlmann Theorem 1.8 applies only after those facts,
dual-reducedness, and the full torsion sequence are proved; its stated domain
is exactly countably based abelian dual-reduced pro-`r` groups.  Finally,
characteristic pro-primary decomposition permits the factorwise
isomorphisms to be assembled without retaining coordinate labels.

Accordingly, the candidate

```text
B_p ~=_top B_q
  iff
kappa_r(p)=kappa_r(q) for every rational prime r
```

is again **source-feasible / unproved**.  The finite torsion-closure index by
itself is still not a complete invariant; the full finite and transfinite
Ulm ledger remains load-bearing.  Nothing in this addendum changes
`UNIVERSAL_RECOVER_P=OPEN`.

### I. Findings and effective verdict after amendment v2

No critical, major, or minor defect was found in the exact amendment-v2
repair.

```text
ADDENDUM_ID=P15R-PHASE1-SOURCE-MATH-RELOCK-v2.0
AMENDMENT_SHA256=386ee5775c30ac263f4f72983fb7555b16ade8e72b4597f73fd11460445fcb80
VERDICT=PASS
FINDINGS=C0/M0/m0
OLD_M1=CLOSED_BY_EXCEPTIONAL_PRIMARY_KERNEL_ABSORPTION
OLD_m1=CLOSED_REMAINS_CLOSED
R_EQUAL_P_BOUNDED_SURJECTIVITY=WITHDRAWN
R_EQUAL_P_KERNEL_ABSORPTION=RELOCK_PASS
R_EQUAL_P_ZSIGMONDY_USE=EXPONENT_EMBEDDING_ONLY
R_NOT_EQUAL_P_HEIGHT_ROUTE=RELOCK_PASS_NO_REGRESSION
P2_QUADRATIC_FIREWALL=PASS
KULIKOV_DOMAIN=VERIFIED
PONTRYAGIN_TORSION_CLOSURE_TRANSLATION=PASS
EXACT_IFF_CLASSIFICATION=SOURCE_FEASIBLE_UNPROVED
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
NOVELTY_LANGUAGE=NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH
PROOF_AUTHORIZED=false
CONTROLS_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```

This append preserves every byte of the 27342-byte / 684-line report prefix.
It authorizes no proof, controls, Route, manuscript, release, Git operation,
archive, or public synchronization.
