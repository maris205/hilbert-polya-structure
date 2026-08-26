# Replacement Paper 15 integrated Phase-1 exact-byte proof gate

Status: **PASS TO ONE SYMBOLIC PROOF — C0/M0/m0**  
Version: `P15R-P1-GATE-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Standalone status: **HOLD**  
Publication ceiling: **FULL PAPER PLAUSIBLE, NOT YET PASSED**

This gate authorizes one symbolic proof ledger and read-only independent
proof-review preparation.  It does not authorize deterministic-control
design or implementation, control execution, Route A/B, composition,
manuscript or figure work, release, archive, Git, or public synchronization.

## 1. Exact authority tuple and precedence

Every artifact below was re-hashed on its current complete bytes immediately
before this gate was written:

```text
Papers 14--18 historical batch design lock
  sha256:2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
Papers 14--18 batch amendment v1
  sha256:afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802
Papers 14--18 batch amendment v2
  sha256:3aa08c2cc2e38b02c83316d188f418d157abd43cf881e447cc28bf083ed3684b
replacement Paper-15 research protocol
  sha256:02693989ad616752c3f6f9e26ad0430a8f5942d0c8449cebe38b7105a2ab3d5a
replacement Paper-15 candidate lock
  sha256:811b4b515dd3f3c45cc96390a139e1d5e3a361d4fea566f0a473d91b8a73d722
transverse Pontryagin/Ulm feasibility precheck
  sha256:02bfac76eeeeb8ac81524c5230b4033de8aec43522d0b74bbc9c635c502732eb
Phase-1 amendment v1
  sha256:2fba2e4f163dbe223ee9eec5ea2d00848e97d2a78fe56ca57b54021837ec0bcc
Phase-1 amendment v2
  sha256:386ee5775c30ac263f4f72983fb7555b16ade8e72b4597f73fd11460445fcb80
final source/precedent report with v2 closure
  sha256:287bba68fa191a1971c6c060b7eae43bf2ca2f02cbf64f6dfb8959d5c546de97
independent methodology/domain/devil/nonredundancy review
  sha256:5af721d6a0ba05731ce2e18397e006b87ef90f327a9edd931c171ad6b889f1ae
```

Amendment v2 supersedes the `r=p` branch of amendment v1 in full.  The
following route is historical, false, and forbidden:

```text
primitive divisor with ord_ell(p)=p^m
  => bounded-order character extension at order p^m.
```

The active diagonal route is the exceptional-primary kernel-absorption
lemma.  Bang--Zsigmondy is used there only upstream to detect all finite
`p`-primary quotients of the exponent embedding.  The `r!=p` exact-order
Kummer--Chebotarev route remains active and separate.

Both final independent Phase-1 reports close at `C0/M0/m0`.  No proof gap is
being deferred into controls.

## 2. Exact owner and theorem ceiling

For a rational prime `p`, the proof owner is the bare compact group

```text
U_p = product_{ell!=p} Z_ell^x,
e_p:Zhat -> U_p,             a |-> p^a,
H_p=e_p(Zhat),
B_p=U_p/H_p.
```

It is not Paper-9's actual indiscrete quotient `Q_p`, a marked coordinate
presentation, a measured enhancement, a standardized flow, or a trace
owner.  All claims must remain invariant under unmarked topological-group
isomorphism of `B_p`.

For each rational prime `r`, write `B_{p,(r)}` for the characteristic
pro-`r` Sylow factor and `K_{p,r}=dual(B_{p,(r)})`.  The target signature is

```text
kappa_p(p)=0,
kappa_r(p)=v_r(p^(r-1)-1)-1       for odd r!=p,
kappa_2(p)=v_2(p^2-1)-3           for odd p.
```

The permitted central theorem is

```text
B_p ~=_top B_q
  iff
kappa_r(p)=kappa_r(q) for every rational prime r.
```

The stronger statement `B_p determines p for every p` remains OPEN and is
not a candidate theorem.  The proof must not infer `p=q` from equality of
signatures or import a labelled conductor to force that conclusion.

## 3. Sole authorized proof artifact

Exactly one new proof file may be created:

```text
papers/15-wieferich-ulm-packet-bases/notes/phase2_wieferich_ulm_proofs.md
```

It must bind this gate and the complete authority tuple above, state all
source-owned inputs with exact domains, prove every item in Sections 4--9
below, give a claim-closure ledger, and retain `STANDALONE_PASS=HOLD` pending
an independent proof/nonredundancy review.

## 4. Exponent embedding and ambient primary structure

The proof must first establish:

1. `e_p` is a continuous injective map from compact `Zhat` to Hausdorff
   `U_p`, hence a closed embedding and `H_p~=Zhat`;
2. every primary component of `Zhat` is detected, with the omitted `p`
   coordinate handled by a correctly exception-checked primitive-divisor
   argument;
3. for every `r`, every finite cyclic order `r^n` occurs countably
   infinitely often in the away-coordinate pro-`r` Sylow; and
4. the exact abstract decompositions

   ```text
   U_{p,(r)} ~= P_r                  if r=p,
   U_{p,(r)} ~= Z_r x P_r            if r!=p,
   P_r=product_{n>=1}(C_{r^n})^aleph0.
   ```

At `r=2!=p`, the local sign factor `C_2` may be absorbed in an abstract
group isomorphism only after its actual restriction-map contribution has
been registered.

## 5. Exact dual sequences and exceptional branch

Pontryagin duality must reverse the compact exact sequence and yield the
correct discrete exact restriction maps.  Countability and reducedness are
proof obligations, not implicit conventions.

For `r=p`, put

```text
S_p=direct_sum_{n>=1}(C_{p^n})^aleph0,
g_p:S_p -> C_{p^infty},
K_{p,p}=ker(g_p).
```

The proof must display the amendment-v2 block calculation:

- one explicit maximal-image generator in every homogeneous block;
- the simultaneous triangular basis change and its finite-support inverse;
- `S_p=T direct_sum R`, with `T~=S_p`, `g_p(T)=0`, and
  `R~=direct_sum_n C_{p^n}`;
- the literal equality `ker(g_p)=T direct_sum ker(g_p|R)`;
- the exact Kulikov/Hill domain before invoking the subgroup theorem; and
- absorption of the at-most-countable cyclic remainder by the `aleph_0`
  copies of every order already in `T`.

It must conclude

```text
K_{p,p} ~= S_p,
u_n(K_{p,p})=aleph_0 for all finite n,
p^omega K_{p,p}=0,
all transfinite Ulm invariants vanish.
```

This branch applies equally to odd `p` and `p=2`; the withdrawn bounded
surjectivity route may not reappear in another notation.

## 6. Off-local exact-order saturation

For `r!=p`, the proof must identify the local Prüfer coefficient up to an
`r`-adic unit as multiplication by `r^kappa_r(p)`, retaining the normalized
odd logarithm and the `r=2` sign convention.

The away map `g:S_r->C_{r^infty}` must satisfy, by direct proof,

```text
g(S_r[r^m])=C_{r^infty}[r^m] for every m>=1.
```

The arithmetic witness must produce infinitely many primes `ell!=p,r` with

```text
v_r(ell-1)=m,
v_r(ord_ell(p))=m.
```

For odd `r`, the proof must construct the exact compatible Frobenius in the
Kummer--cyclotomic compositum, prove the required intersection using its
ramification domains, and then apply unconditional qualitative Chebotarev.
For `r=2` and odd `p`, it must separately prove the quadratic/cyclotomic
compatibility.  No GRH, density snippet, mere divisibility of the order, or
`r=p` reuse is permitted.

The `p=r=2` impossibility guard is explicit: high-level equality
`v_2(ord_ell(2))=v_2(ell-1)` cannot be demanded for `ell=1 mod 8` because
`2` is then a square.  That case belongs only to Section 5.

## 7. Infinite height and the complete Ulm ledger

For `r!=p`, after writing the restriction as

```text
Phi(s,z)=g(s)+r^kappa z,
S_r direct_sum C_{r^infty} -> C_{r^infty},
```

the proof must establish both inclusions in

```text
r^omega K_{p,r} ~= C_{r^kappa_r(p)}.
```

The reverse inclusion must construct roots **inside the kernel** by using
the exact-order saturation to cancel the image of each ambient Prüfer root.
Ambient divisibility alone is insufficient.

It must then prove, not merely assert:

```text
u_n(K_{p,r})=aleph_0 for every finite n;
if kappa>0, u_{omega+kappa-1}=1 and every other transfinite invariant is 0;
if kappa=0, every transfinite invariant is 0.
```

The countable/reduced guard must precede any Ulm or Kiehlmann classification
step.  A finite `r^omega K` contains no nonzero divisible subgroup; this and
the exceptional isomorphism must be used to rule out hidden Prüfer summands.

## 8. Compact translation, intrinsicity, and global iff

The proof must derive the annihilator identity, with closure,

```text
ann(closure(Tor(B_{p,(r)})))=r^omega K_{p,r},
```

and then prove

```text
closure(Tor(B_{p,(r)})) ~= P_r,
B_{p,(r)}/closure(Tor(B_{p,(r)})) ~= C_{r^kappa_r(p)}.
```

It must show that `B_{p,(r)}` and its torsion closure are characteristic,
so `kappa_r(p)` is intrinsic on the bare compact group.  Necessity of the
global iff follows factorwise.  Sufficiency must use the complete common
finite/transfinite ledger, obtain each factor isomorphism from the exact
countably based dual-reduced classification, and assemble the unrestricted
product over all rational primes.  Coordinate labels from `U_p` may not
survive this construction.

## 9. Mandatory arithmetic example and owner firewalls

The proof must include the bare-group separation

```text
kappa_11(2)=0,
kappa_11(3)=1,
B_2 not~=B_3,
```

using the intrinsic 11-primary torsion-closure quotient rather than a
marked missing coordinate.

It must also prove the boundary that the conductor/support filtration is
natural only for the marked exact sequence `H_p->U_p->B_p`; bare-group
automorphisms may mix equal-order summands.  The ambient `U_p` missing-local-
coordinate marker is a negative control, not an invariant of `B_p`.

No result may be promoted to the actual indiscrete packet, a Haar or measured
owner, a standardized flow, a trace, an operator, a determinant, Route B,
or universal prime recovery.

## 10. Review and publication gate after proof

The final proof bytes require an independent exact-byte mathematical,
source-domain, devil, and post-proof nonredundancy review.  That review must
rederive the two arithmetic branches and the full Ulm/compact/global chain.
It must again subtract Pontryagin duality, Kulikov, Kiehlmann/Ulm,
Kummer--Chebotarev, and ordinary local-unit structure before deciding whether
the executed conjunction carries full-paper weight.

The project fails closed to `MERGE_OR_STOP` if the proof supplies only one
separation, omits exact-order saturation or exceptional absorption, records
only the order of the infinite-height subgroup, or never proves both
directions of the global iff.  It cannot fall back to a second Technical
Note because Paper 17 holds the batch's sole note slot.

## 11. Authorization matrix

```text
PHASE1_INTEGRATED_GATE=PASS_C0_M0_m0
AUTHORIZED_PROOF_PATH=papers/15-wieferich-ulm-packet-bases/notes/phase2_wieferich_ulm_proofs.md
SYMBOLIC_PROOF_AUTHORIZED=true
INDEPENDENT_PROOF_REVIEW_REQUIRED=true
STANDALONE_PASS=HOLD
FULL_PAPER_PLAUSIBLE=true
UNIVERSAL_RECOVER_P=OPEN_NOT_AUTHORIZED
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

This gate is acyclic: it binds only stable upstream inputs and does not name
or predict the proof's future digest.  A later review may bind the final proof
hash; this gate may not be edited to back-fill it.
