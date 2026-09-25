# Frozen same-object topology audit — version 1

Date: 2026-09-20. Audit ID: `ASFS-AUDIT-20260920-HQT01`.
Candidate ID: `ANG-20260919-HWS01` (unchanged candidate 278).
Initial workflow state: `FROZEN — TOPOLOGY QUESTIONS OPEN`.

This is a bounded follow-up audit, not a new dynamical candidate or a
replacement for the [278 card](../278-haar-seeded-witness-flow/candidate-card.md)
and [278 paper](../278-haar-seeded-witness-flow/paper.md). Outcomes, if obtained,
will be appended after this frozen prefix. No outcome is asserted here.

## 1. Source locks and authority

The authoritative unchanged source files have SHA-256:

- 278 candidate-card.md: `b5f1451a57afcbf7150c9f6afe1febf7c6c5673cbb3968d1c5485022be906a4a`.
- 278 paper.md: `9a53b0b5b0fa0648547d7a9d74404de16a5db82406ddec097ea97259e6d5605c`.

The current continuing research authorization covers this bounded audit.
Neither this card nor an existing workflow authorizes external publication,
numerical experiments, a new operator, or formal Route evaluation. Packages
241/242 remain paused. All 278 source and evidence files remain read-only.

## 2. Complete unchanged owner

Let K be the full profinite integers with their usual topology and normalized
additive Haar measure h. The source Y is the disjoint topological union of
copies of K at ALL roots H_n (n >= 2), S_(n,d) (n >= 3, 2 <= d <= n-1),
and E_k (k >= 0). Every root has mass one. Late scan roots, nonreturning
seeds, and escape states are retained without exception.

At (H_n,x), write j=x mod n in {0,...,n-1}, y=(x-j)/n. The actual map T is:

- n=2,j=0: (H_2,y).
- n>=3,j=0: (S_(n,2),y).
- j>=1,gcd(n,j)=d>=2: (H_d,y).
- j>=1,gcd(n,j)=1: (E_0,y).

At (S_(n,d),x), the seed is unchanged: go to H_d if d divides n, to
S_(n,d+1) if d does not divide n and d<n-1, and to H_n otherwise.
At (E_k,x), go to (E_(k+1),x).

The owner is the full retained-lag local-homeomorphism groupoid
G={(z,m-k,w): T^m z=T^k w}, with source w and target z. Its topology is
the full finite inverse-branch-pair topology on clopen terminal arithmetic
sets, not an orbit representative or a restricted germ owner. A finite
inverse branch is theta_alpha(t)=b_alpha+D_alpha t, where D_alpha is the
product of hub moduli actually consumed along that prefix. The unchanged
continuous clock on a beta-to-alpha branch pair is

    c = log D_alpha - log D_beta,
    Haar IMAGE Jacobian = D_beta / D_alpha.

This clock is defined on all actual arrows, including null seeds, by the
278 continuous full-point construction. It is not reselected a.e. here.
On M=Y x R the real extension G_c has arrows
(w,u) -> (z,u+c(g)). Real translation (z,u) -> (z,u+t) commutes with it.

The full coarse quotient Q=M/G_c is given its quotient topology. Only
G_c arrows are quotiented; real translation is NOT additionally quotiented.
No source, arrow, root, weight, clock, or topology is changed by this audit.
Classical symplectic base, positive roof, mapping torus, Hamiltonian and
contact owners: `NOT APPLICABLE`.

## 3. Existing ledger and lineage

278 supplies the same-object prime-symbolic witness/admissibility lineage:
the arithmetic seed consumes actual residues; gcd descent and exhaustive
divisor scanning deform the witness-symbolic source. It is not a generic
geometric or operator proposal. The scan choice still leaves naturalness
OPEN; this audit does not make it inevitable or establish natural A0.

The established 278 ledger may be used as a dependency: the only primitive
periodic source cycles are the zero-seed prime cycles C_p, of discrete
length ell_p=p-1. Write z_p=(H_p,0). Let B_p contain ALL source states
eventually hitting this cycle. B_p is one full G orbit. At its states the
clock isotropy image is (log p)Z; elsewhere it is {0}. Thus there is exactly
one abstract cyclic-time packet per prime with least time log p and repeats
r log p. Nonzero seeds in D_p=intersection_(r>=0) p^r K can follow the
same periodic root word without actual returns. Escape states also remain.
These distinctions, multiplicity one, and repetition conventions are fixed.

## 4. Precommitted bounded questions

Define P_p={pi(z_p,t):t in R} in the FULL quotient Q and the canonical map

    kappa_p: R/(log p)Z -> P_p, [t] -> pi(z_p,t).

Check separately, first at p=2 as an edge control and then uniformly:

1. Are the seed sets B_p at each individual root finite? Include every
   late scan root, every composite hub, and every escape root. A structural
   induction is permitted; a finite orbit table is not a proof.
2. Is kappa_p a homeomorphism onto the actual subspace P_p of the full Q?
   A quotient of a reduced returning subgroupoid alone is insufficient.
3. Is P_p closed in Q? This is different from both item 2 and global
   Hausdorffness.
4. Does the full Q satisfy Hausdorff separation? One fixed separating
   stress test is the pair of seeds 3^(k!) and 2*3^(k!) at H_3, at common
   real coordinate zero. Test their exact full-groupoid equivalence,
   profinite limits, and the equivalence of those limits. This sequence
   is a proof device, not a numerical experiment or an added trajectory.

For item 2 explicitly compare the quotient topology of B_p x R with the
subspace topology in Q before using a circle phase map. Retain full clock
signs and all finite preimages. Prove any limit using all finite moduli,
not decimal approximations or finite precision.

## 5. Stops and non-goals

A failure of global separation stops a Hausdorff-ambient promotion, not
automatically the separate circle question. A circle result does not imply
global Hausdorffness, local manifold structure, contact geometry, natural
arithmetic selection, or an explicit formula. Do not delete nonreturning
fibres or escape states to repair a negative result; that changes the owner
and requires a newly authorized architecture/card.

Do not classify every nonperiodic orbit closure or the global T1 property.
No T3 operator, trace, determinant, domain, or weights are supplied or pursued.
No new A0/A1/A2 coordinates: classical fields NOT APPLICABLE. Formal Route
coordinates UNASSIGNED; Route B NOT INVOKED. Model review is an internal
adverse check, not external peer review or formal verification.

The allowed handoff is scoped advance of an exact same-object topological
fact, or a precise stop/fork, with all remaining questions explicitly OPEN.

## Appended audit outcome — 2026-09-20

Audit `ASFS-AUDIT-20260920-HQT01`; unchanged candidate `ANG-20260919-HWS01`.
Status: `CLOSED EMBEDDED PRIME CIRCLES; FULL QUOTIENT NON-HAUSDORFF — SCOPED ADVANCE / STOP`.

The frozen prefix above is preserved. The [paper](paper.md) supplies the
structural all-root induction: each B_p is rootwise finite and therefore
closed and discrete in Y. B_p x R is a closed saturated part of the
UNCHANGED full extension. Its quotient topology agrees with the actual
subspace topology on P_p in Q. An explicit phase inverse proves the
canonical kappa_p is a closed embedding of the ordinary circle, for
every prime including p=2. Least times and all repeats are unchanged.

The precommitted H_3 pair is a decisive negative separation control:
3^(k!) and 2*3^(k!) have equal-clock arrows into the same escape state,
but converge to inequivalent nonreturning seeds. The full Q is therefore
non-Hausdorff. Global T1 and other nonperiodic orbit closures remain
unclassified. No sources, arrows, seeds, phases or clock values changed.

Portfolio: **scoped advance / stop**. Advance the same-owner T2 circle
topology; stop global Hausdorff/classical-ambient promotion. Naturalness
remains OPEN. T0/scoped T1 retain their prior scope. T3 NOT SUPPLIED /
NOT PURSUED; classical A0/A1/A2 NOT APPLICABLE, formal UNASSIGNED,
Route B NOT INVOKED. No new analytic owner is created.

The [claim ledger](claim-ledger.md) and [evidence](evidence/README.md)
record limits and internal-review provenance. The next authorized step
is continued architectural breadth with this exact result preserved,
not state deletion or clock retuning. 241/242 paused; programme active.
