# HCS-C62 selection pilot

Status: **PILOT_NONAUTHORITY / TARGET_LOCK_SUPPORTING**

Date: 2026-08-18.  The pilot rebuilt the released C61 (W(E_6)) action from
the committed C61 group evidence and enumerated 2-subset orbits by generator
action.  It did not write theorem evidence and is not a G0--G7 result.

## Exterior-square signal

The plus and minus 2-subset G-sets each have ten orbits with the same size
multiset:

```text
[160, 480, 480, 960, 4320, 4320, 5760, 8640, 12960, 12960]
```

Matched stabilizers are not all conjugate.  In canonical orbit order, the
480-orbit at seed `(0,2)` has plus/minus stabilizer hashes

```text
f25eee5ff7f54c50996ed4a4d36dddb4be687855348799fc63d5a0bed219f5ee
c75d3b21b45736ccef5b7f0c4f9fcc09ef48411902e2f3e66be017db4adbc819
```

and an exhaustive conjugator search returned false.  The 4320-orbit at seed
`(0,1)` likewise returned false.  This is a positive feasibility signal for
the exterior branch, not a theorem: the final checker must reconstruct all
orbits, element sets, cores, normalizers, and field dictionaries.

## Symmetric-square status

The pilot enumerated eleven orbits on each size-two-multiset G-set with size
multiset

```text
[160, 320, 480, 480, 960, 4320, 4320, 5760, 8640, 12960, 12960]
```

The plus/minus stabilizer conjugacy audit remains pending and is an explicit
C62 gate.  No nonisomorphism is assumed from these equal sizes.

## Decision

The exterior branch clears the bounded feasibility gate; C62 remains locked
as the integrated exterior/symmetric-square target.  A collapse of the
symmetric branch is a certified result and does not authorize scope growth.
