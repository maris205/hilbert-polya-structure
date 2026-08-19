# C75 experiment plan

## Source binding

Read the C72 coordinate evidence and C72 manifest byte-for-byte, then bind
the C74 evidence and C74 manifest. The producer refuses to run if an authority
hash differs.

## Exact enumeration

1. Enumerate all 54 points of `Q` and all 108 automorphisms by direct
   bijectivity testing of the displayed matrix form.
2. Enumerate the complete 20-subgroup lattice by cyclic-subgroup closure.
3. Partition the sixteen labels by their cyclic subgroup and record the nine
   nonempty fibers.
4. Retain exactly the ambient maps preserving the weight function on all
   twenty subgroups.
5. Enumerate all compatible label lifts in every target closure fiber.
6. Compare the direct 11,520-pair enumeration with the group generated from
   explicit label-fiber generators and ambient lifts.

## Independent checks

The checker reimplements the finite operations; GAP receives a faithful
70-point representation; clean replay starts a new interpreter; hostile
mutations alter authorities, definitions, fibers, orders, and the nonfaithful
lattice warning.

## Claims firewall

This is a finite named-presentation symmetry result only. It does not assert a
canonical basis, full table of marks, Burnside-ring identity, or arithmetic
local interpretation.
