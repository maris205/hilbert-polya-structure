# The canonical profinite completion of primorial wheels has no compatible successor

**Paper ID:** `039-profinite-wheel-successor-compatibility`  
**Record ID:** `ASFS-SCOUT-20260914-28`  
**Date / status:** `2026-09-14; PRE-P0 STOP — WHEEL SUCCESSORS DO NOT DESCEND TO THE NATURAL INVERSE LIMIT`  
**Route state:** `No classical candidate; Route A not evaluated; Route B NOT INVOKED`

## Abstract

The primorial wheel recursion is a direct prime-symbolic A0 control. This
screen tests a different repair of its sequential character: the canonical
inverse limit of all reduced-residue wheels under modular reduction. Although
this carrier is compact and retains all finite wheel states, successor maps
are incompatible with its bonding maps. The explicit `30 -> 6` counterexample
proves there is no autonomous map on the natural inverse limit that projects to
all finite sieve successors. No base map, roof, primitive-orbit ledger, or
analytic owner exists, and the screen stops before P0.

## 1. Lineage and carrier

```text
prime/composite sieve constraint
  -> primorial reduced-residue admissibility and gap word (019)
  -> finite wheel successor R_k (028)
  -> canonical inverse-limit recurrence test (this screen).
```

Let `P_k=p_k#`, `W_k=(Z/P_k Z)^×`, and let `R_k` take a survivor to the next
survivor in cyclic residue order. Canonical reduction gives surjections
`rho_(ell,k):W_ell -> W_k` for `ell>k`; hence the compact carrier
`W_infty=lim<- (W_k,rho_(ell,k))` exists. A projected successor `R_infty`
would require every square

`rho_(ell,k) o R_ell = R_k o rho_(ell,k)`.

This is not optional: without it, a point's “next state” depends on which
finite sieve stage observes it.

## 2. Decisive test

At stages two and three,

```text
P_2=6,   W_2={1,5},                        R_2(1)=5;
P_3=30,  W_3={1,7,11,13,17,19,23,29},      R_3(1)=7.
```

Reduction modulo six yields

```text
rho_(3,2)(R_3(1)) = 7 mod 6 = 1,
R_2(rho_(3,2)(1)) = R_2(1) = 5.
```

The required square does not commute. A hypothetical `R_infty` projected to
levels three and two would imply this false equality. Passing from 6 to 30
inserts new survivors between old ones, so a fine-level successor need not be
the coarse-level successor after reduction. Compactification has therefore not
made the sequential sieve update stationary.

## 3. Same-object audit

| Item | Owner in this screen | Status |
| --- | --- | --- |
| Arithmetic mechanism | finite primorial wheel recurrence | retained as source only |
| Autonomous base map | no compatible inverse-limit successor | `FAIL-CLOSED` |
| Symplectic structure | profinite set, not specified smooth `(M,omega)` | absent |
| Roof / suspension | no base map to suspend | absent |
| Primitive orbits / repetitions | no same-object autonomous dynamics | absent |
| Operator / zeta | none | absent |

The 032 circles and zeta are not imported: they belong to a disjoint-packet
carrier with a different base and roof. Nor may arbitrary bonding maps, a
stage counter, or an external time change be silently added; each would define
a new candidate and needs its own P0 card.

## 4. Controls and nonclaims

| Test | Result | Consequence |
| --- | --- | --- |
| Canonical `30 -> 6` reduction | successor square fails | decisive stop |
| Inverse-system construction | compact state carrier exists | does not provide dynamics |
| 026 natural-extension audit | chronology cannot be made bi-infinite on same owner | no repair borrowed |
| 032 suspension | finite packets can be roofed separately | no transfer |

This does not show that every inverse-limit or Bratteli construction fails. It
only proves failure of the canonical reduced-residue inverse system to carry
the exact finite-stage successors. No manually supplied prime logarithms,
prime tables, zero data, or parameter fit is used.

## 5. Gate decision

| Gate | Evidence | Status |
| --- | --- | --- |
| A0 | finite-stage sieve source retained, but no autonomous same-object carrier | `NOT EVALUATED` |
| A1 | no base map or primitive-orbit convention | `scoped FAIL` |
| A2 | no roofed object or analytic owner | `NOT EVALUATED` |
| Route B | no Route-A candidate | `NOT INVOKED` |

**Portfolio position: stop/fork.** Stop the canonical profinite completion.
Fork only to a new carrier with bonding maps and autonomous action compatible
by construction, while still deriving rather than importing the sieve-symbolic
mechanism.
