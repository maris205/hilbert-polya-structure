# Paper 15 replacement research protocol

Status: **PHASE-1 REPLACEMENT PROTOCOL / INDEPENDENT REVIEW REQUIRED**  
Version: `P15R-P1-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Working title: **Wieferich--Ulm Invariants of the Compact Rational-Witt Packet Bases**  
Proof, controls, Route A/B, manuscript, release, Git, and public
synchronization: `false`

## 1. Exact authority and replacement status

This protocol is authorized by, and binds, the following records:

```text
Papers 14--18 historical batch design lock
  sha256:2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
Papers 14--18 batch amendment v1
  sha256:afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802
old Paper-15 mathematical precheck
  sha256:1598569c48d4382408bb3df933a1c5443984daf36b12e6377bae4590356a75f8
replacement transverse Pontryagin/Ulm precheck
  sha256:02bfac76eeeeb8ac81524c5230b4033de8aec43522d0b74bbc9c635c502732eb
```

The old project *Mixed Prime-Clock Standardization and Global Scaling
Rigidity* is `NO_GO` as a standalone manuscript.  Its valid categorical
content is merged into Paper 16.  The historical directory
`papers/15-mixed-clock-rigidity/` remains an audit record; this directory is
the current replacement Paper-15 project.

The transverse precheck is feasibility evidence, not a proof.  Every theorem
below is `SPECIFIED / UNPROVED` until a later exact proof and independent
review close it.

## 2. Research question and exact owner

For a rational prime `p`, define the candidate source presentation

```text
U_p = product_{ell != p} Z_ell^x,
e_p : Zhat -> U_p,       n |-> p^n,
H_p = image(e_p),
B_p = U_p/H_p.
```

The first proof obligation is that `e_p` is a continuous closed embedding,
so that `H_p` is canonically isomorphic to `Zhat` and `B_p` is a countably
based compact abelian group.

The central question is:

> Can the bare compact topological groups `B_p` be classified intrinsically
> by the torsion sequences of their characteristic pro-primary Sylow
> subgroups, and which primes can be distinguished by the resulting
> Wieferich--Ulm signature?

The owner is the **bare compact group** `B_p`.  It is not Paper 9's actual
indiscrete quotient `Q_p`, a coordinate-labelled presentation, a measured
enhancement, or Paper 16's mixed standardized flow.

## 3. Primary decomposition and signature

For every rational prime `r`, let `B_{p,(r)}` be the characteristic pro-`r`
Sylow subgroup of `B_p`, and put

```text
P_r = product_{n>=1} (C_{r^n})^{aleph_0},
S_r = dual(P_r) = direct_sum_{n>=1} (C_{r^n})^{(aleph_0)},
K_{p,r} = dual(B_{p,(r)}).
```

The exact candidate defect is

```text
kappa_r(p) = 0                                      if r=p,
kappa_r(p) = v_r(p^(r-1)-1)-1                      if r!=p and r is odd,
kappa_2(p) = v_2(p^2-1)-3                          if r=2 and p is odd.
```

The `r=p` clause is not obtained by substituting into the Fermat-quotient
formula: the local `p`-coordinate is absent.  The `r=2` branch must retain
the sign factor of `Z_2^x=C_2 x (1+4Z_2)` throughout the proof.

Write `kappa(p)=(kappa_r(p))_r`.  This signature is a proposed intrinsic
invariant only after the compact-side torsion-closure formula in Section 5
is proved.

## 4. Arithmetic and dual-group proof obligations

The symbolic proof must establish the following chain without circular use
of the desired classification.

### 4.1 Exponent embedding

Prove `H_p ~= Zhat`.  For the `r!=p` part, an exact local-unit/logarithm
argument must detect the `Z_r` component.  For the missing `r=p` coordinate,
state and audit the precise Bang--Zsigmondy input, including its exceptional
cases, and show that away primes detect every finite `p`-power quotient.

### 4.2 Ambient Sylow structure

Prove

```text
U_{p,(r)} ~= P_r                 if r=p,
U_{p,(r)} ~= Z_r x P_r           if r!=p.
```

For `r=2!=p`, the literal local factor is `C_2 x Z_2`; only its abstract
extra `C_2` may be absorbed into the already infinite `C_2` multiplicity.
The proof must justify, rather than merely count, the occurrence of
countably infinitely many factors of every order `r^n`.

### 4.3 Exact restriction map

Pontryagin duality must be applied to the exact compact sequence and give

```text
0 -> K_{p,r} -> dual(U_{p,(r)}) -> C_{r^infty} -> 0.
```

For `r!=p`, identify the local Prüfer-summand map up to a unit as
multiplication by `r^{kappa_r(p)}`.  The proof must state the normalized
odd-`r` and `r=2` logarithm conventions and keep the finite sign character in
the reduced side.

### 4.4 Off-local height saturation

Prove directly, for the away-coordinate restriction `g:S_r->C_{r^infty}`,

```text
g(S_r[r^m]) = C_{r^infty}[r^m]       for every m>=1.
```

The proposed Kummer--Chebotarev witness is the existence of infinitely many
primes `ell != p,r` with

```text
v_r(ell-1)=m,
v_r(ord_ell(p))=m.
```

The final proof must construct a compatible Frobenius element in the exact
finite Kummer--cyclotomic compositum, treat `r=2` separately, and audit every
ramification/intersection assertion.  A density theorem that proves only
`r^m | ord_ell(p)` is insufficient unless the exact valuation of `ell-1` is
also forced.  GRH is not permitted as an unstated hypothesis.

### 4.5 Kernel and Ulm calculation

Prove

```text
u_n(K_{p,r}) = aleph_0                         for every finite n,
r^omega K_{p,r} ~= C_{r^{kappa_r(p)}}.
```

If `kappa_r(p)>0`, verify the exact sole transfinite index
`omega+kappa_r(p)-1`; if it is zero, verify that all transfinite invariants
vanish.  Kulikov/Pruefer/Ulm results may be cited only at exact domains and
locators.  Countability, reducedness, and the absence of a hidden divisible
summand must be checked before invoking classification.

## 5. Intrinsic compact-side theorem

The central compact-group theorem candidate is

```text
closure(Tor(B_{p,(r)})) ~= P_r,
B_{p,(r)}/closure(Tor(B_{p,(r)})) ~= C_{r^{kappa_r(p)}}.
```

The proof must derive the annihilator identity

```text
ann(closure(Tor(B_{p,(r)}))) = r^omega K_{p,r}
```

and show that both the Sylow subgroup and the torsion closure are
characteristic.  Only then may it call

```text
kappa_r(p) = log_r [B_{p,(r)}:closure(Tor(B_{p,(r)}))]
```

an invariant of the bare compact group.

The proposed complete classification is

```text
B_p ~=_top B_q
  iff
kappa_r(p)=kappa_r(q) for every rational prime r.
```

Necessity and sufficiency must both be proved.  The sufficiency direction
must assemble all characteristic pro-primary factors and may not retain
coordinate labels from `U_p`.

## 6. Explicit theorem and controls

At minimum, the proof must include the intrinsic separation

```text
kappa_11(2)=0,
kappa_11(3)=1,
B_2 not~ B_3.
```

The witness must be stated on the bare group:

```text
Tor(B_{2,(11)}) is dense,
[B_{3,(11)}:closure(Tor(B_{3,(11)}))]=11.
```

Future deterministic controls must include:

- direct valuations for several ordinary and higher-Wieferich branches;
- the exceptional `r=p` and `r=2` branches;
- model pro-`r` groups with prescribed finite torsion-closure quotient;
- a wrong-local-coordinate negative;
- a wrong `-1` or `-3` normalization negative;
- equality of finitely many signature coordinates without promotion to a
  full-group collision; and
- marked-conductor data that changes under bare automorphisms.

Finite controls support bookkeeping only and cannot prove the infinite
Chebotarev or Ulm theorems.

## 7. Marked presentation and universal-recovery firewall

The conductor/support filtration on `H_p^perp subset dual(U_p)` is natural
for the marked exact sequence

```text
H_p -> U_p -> B_p
```

with labelled local coordinates.  It is not supplied by the bare group
`B_p`: equal-order summands can be mixed, and the missing `p`-coordinate
already carries the sought label.  The proof must include this distinction
and the negative control that the **ambient** group `U_p` does recover the
omitted prime, while the quotient loses that simple marker.

The universal statement

```text
the topological isomorphism type of B_p determines p for every p
```

is **OPEN / NOT A CANDIDATE THEOREM**.  Under the proposed complete
classification it is equivalent to injectivity of `p |-> kappa(p)` on
rational primes.  Explicit pairwise separations do not establish that
injectivity.  No manuscript may use “recover the prime from `B_p`” without a
later versioned proof and independent audit.

## 8. Source and novelty gate

Before proof authorization, an independent source audit must freeze exact
primary or authoritative manifestations and locators for:

1. Deninger's compact packet-base presentation and choice boundary;
2. Pontryagin duality and primary decomposition in the required compact and
   countable-discrete categories;
3. Kiehlmann's torsion-sequence/Ulm classification and torsion-closure
   translation;
4. the exact Kulikov/Pruefer subgroup theorem used in the kernel;
5. Bang--Zsigmondy with all exceptions;
6. Dirichlet for exact `r`-adic valuation classes;
7. qualitative Chebotarev and the exact Kummer independence lemma;
8. normalized local-unit logarithms, especially at `2`; and
9. nearest exact precedent for the complete package.

Moree's prescribed-order work is a comparator, not a substitute for the
paper's exact height-saturation proof.  Search-negative language is limited
to `NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH`; no priority claim
is authorized.

## 9. Candidate claim ledger

| ID | Candidate claim | Phase-1 status |
|---|---|---|
| P15R-1 | `H_p ~= Zhat`, including the missing-`p` detection. | SPECIFIED / UNPROVED |
| P15R-2 | Exact `U_{p,(r)}` Sylow structure with `r=2` guard. | SPECIFIED / UNPROVED |
| P15R-3 | Local restriction coefficient and full off-local height saturation. | HIGH-RISK / UNPROVED |
| P15R-4 | Finite and transfinite Ulm invariants of `K_{p,r}`. | HIGH-RISK / UNPROVED |
| P15R-5 | Intrinsic torsion-closure quotient formula. | CENTRAL / UNPROVED |
| P15R-6 | Complete iff classification and `B_2 not~ B_3`. | CENTRAL / UNPROVED |
| P15R-7 | Marked-conductor/bare-owner nonintrinsicity boundary. | SPECIFIED / UNPROVED |
| P15R-8 | Universal recover-`p` remains open; exact precedent audit. | HARD STOP / REVIEW REQUIRED |

## 10. Nonredundancy and standalone gate

The following do not clear standalone review:

- the standard annihilator formula `H_p^perp`;
- the single calculation `B_2 not~ B_3`;
- a conductor grading on the marked presentation;
- a list of finite Wieferich valuations;
- an abstract invocation of Ulm without the exact packet-base kernel; or
- any inference about the actual indiscrete `Q_p`.

Standalone eligibility requires the full intrinsic torsion-closure theorem,
the complete iff classification, the height-saturation proof, explicit
arithmetic separations, and a post-proof source/nonredundancy finding that the
exact package is not routine prior art.  At this protocol:

```text
CURRENT_STANDALONE_PASS=false
STANDALONE_CEILING=FULL_PAPER_PLAUSIBLE
```

If only a special pair or marked formula survives, the project is merged or
stopped; Paper 17 remains the batch's sole Technical Note candidate.

## 11. Phase gates

Independent methodology/nonredundancy, mathematical devil/domain, and
primary-source/precedent reviews must all pass this exact protocol and its
candidate lock before a proof gate may be frozen.  The Kummer--Chebotarev
and `2`-primary branches each require explicit hostile review.  Symbolic
proof, controls, Route A/B, manuscript, release, Git, archive, and public
synchronization remain false.

Machine-readable status:

```text
REPLACEMENT_P15_PROTOCOL_FROZEN=true
PROOF_AUTHORIZED=false
CONTROLS_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
STANDALONE_PASS=false
UNIVERSAL_RECOVER_P=OPEN
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```
