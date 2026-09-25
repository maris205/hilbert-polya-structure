# Independent all-state local-executor audit

**Candidate:** `ANG-20260921-LFR01`; authorized batch round5/5.
**Finding:** MAIN retains the complete one-per-atom physical ledger through
a new full source; source microcycle length is not physical period.
**Standing:** Internal inherited-model/shared-history; `NOT_CALIBRATED`.

## 1. Input and scope

After explicit release I personally read original354 card lines1–146 through
EOF and measured SHA-256
`df82f1b6ba5562606b8aac1a2177783c4e29f5fda5d01ace0eae529462411e3a`.
This was the sole new scientific input, with retained raw348 source context.
I did not open root354 paper, scope/peer reports, old scientific files or
new surfaces. No network, numerical experiment or auxiliary agent was used.
The already-read ARS/stream instructions remain applicable. Only this report
was written; no sixth-round candidate or further research is proposed.

I completed MAIN and all F/U/D derivations and sent their summary before
writing. The card's microcycle expectation and inherited context prevent
blindness or error-independence claims. This is not external peer review.
No analytic operator, determinant, quantum owner or formal Route is audited.

## 2. Termination of EVERY work state; proper versus arbitrary inputs

Fix any T(d_0,r_0,a_0), without a validity or reachability condition.
At division r strictly decreases (indeed at least halves); at a scan r
stays fixed and d increases. A nonexit scan requires d^2<=r<=r_0, so d
never exceeds max(d_0,floor(sqrt(r_0))+1) before exit. There can therefore
be only finitely many divisions and scans. The r=1 rule exits immediately.
This proves termination for EVERY work state, including arbitrary a_0.

Write E(T) for its exact finite exit word. The original accumulator remains
an unchanged prefix, and product(a)*r is preserved during work and at exit.
This is not a primality claim about arbitrary output entries. For example
T(5,4,empty) exits to N((4)); it is not an honest factorization of4.

For the proper launch T(2,n,empty), maintain the invariant that the residual
has no prime divisor below d and that all accumulated entries are primes
in nondecreasing order. A dividing d must then be prime, since a proper
prime divisor of composite d would already divide the residual. Scanning
past a nondividing d preserves the invariant. At d^2>r>1 the residual is
prime, since any composite residual has a prime divisor below d. Product
preservation proves the exit is EXACTLY the full sorted factorization of n.
For n=1 it is empty. This verifies the program without a source prime test
and does not extend its correctness invariant to malformed launches.

## 3. All terminals, cycles and incoming basins

A nonempty normal word of length>=2 reduces by gcd to its singleton gcd g.
A proper singleton launch then returns its factor word. For g=p^e this
subsequently reaches N((p)); for g=1 or g with distinct prime factors it
reaches N(empty). Every arbitrary work state first exits to N(E(T)), so
these alternatives exhaust ALL states. N(empty) is the only terminal.

Let b_p=floor(sqrt(p))+1. The only typed source cycles are

```text
N((p)), then T(d,p,empty) for d=2,...,b_p in order,
then back to N((p));  q_p=b_p states/steps.                (1)
```

Primality makes every tested d nondividing, and the first exit is at b_p.
All these typed states are distinct; the displayed period is least.
No cycle can remain forever in work, and any other normal state eventually
reaches a terminal or one of(1), so there are no other source cycles.
For normal words the p basin is precisely gcd(word)=p^e, e>=1.
For T states apply this criterion to the ACTUAL E(T); empty and all remaining
exit words enter the terminal basin. This is a finite, exhaustive basin
test for every invalid/unreachable state, not a selected successful subset.

On(1) only the launch transports geometry, by u->u-log p. The other q_p-1
steps transport identically. Thus q_p is a source period, log p is its
geometric translation, and neither is yet a declared physical-time roof.

## 4. Exhaustive inverses and EVERY-Borel IMAGE

At target N(w), the complete list is: normal gcd predecessors when w is
nonempty; T(d,1,w) for every d>=2; and T(d,r,a) when r>1,d^2>r and
w=a appended r. The gcd inverse scales(Q,X,Z) to(aQ,X/a,Z); work inverses
are identity. Empty therefore has infinitely many incoming work branches.

At target T(d,r,a), the complete list is:

```text
N((r)) if d=2 and a=empty, inverse (rQ,X/r,Z);
T(d-1,r,a) if d>=3,r>1,(d-1)^2<=r and (d-1) does not divide r;
T(d,d*r,b) if a=b appended d and r>=d.                     (2)
```

The latter geometries are identity. The division condition r>=d is exactly
d^2<=d*r in its predecessor. Substitution proves both inverse identities;
the disjoint forward rules prove exhaustiveness, including terminal targets.
Launch cannot overlap either other predecessor type; scan and division may
both occur. All branches have the ENTIRE target geometric chart as domain.
S_L is NOT onto: T(2,1,(1)) is a legal state but has none of(2).
Keeping it is essential; lack of a predecessor does not exclude an object.

Every inverse branch has determinant1, including normal q/xi scalings.
Consequently mu(I(B))=mu(B) for every Borel target set, with the all-point
version J=1 on all null, unit and transverse states. Every finite branch-pair
map is a translation in u, so the IMAGE cocycle is zero on the full actual
groupoid; its kernel is the whole groupoid. This is NOT physical time or
global invariance of a many-to-one map with infinitely many incoming branches.

## 5. Exact retained lag, topology and full MAIN quotient

Choose N(empty) or N((p)) as the canonical core of each basin. Let d(e) be
the first time a typed state e reaches that chosen core and A(e) the sum of
log heads over NORMAL steps before that entrance; work steps add zero.
For a full state x put s_x=u_x-A(e_x). Completing a common tail to a
canonical core proves the exact arrow criterion

```text
(y,k,x): same core, v_y=v_x,z_y=z_x;
terminal: s_y=s_x, k=d(e_y)-d(e_x);
p: s_y-s_x=j log p, k=d(e_y)-d(e_x)+q_p*j, j in Z.         (3)
```

Conversely, post-entrance counts differing by j complete cycles realize
every arrow in(3); terminal arrows are realized at the two entrance depths.
Thus all actual triples and source phases are accounted for; different
common-tail witnesses of one triple are not added as extra arrows.
The lag is unique for related full-state pairs; source isotropy is trivial,
because a nonzero complete microcycle translates u by nonzero log p.

At fixed typed pair and integer lag, each nonempty arrow set is the full
graph of a constant u translation. These are open pieces in the frozen
inherited topology, proving Hausdorff, locally compact, second-countable
étale ownership. Map each chart to(s,v,z), reducing s modulo log p only
in a p basin. This is an open continuous surjection whose fibers are exactly
the actual orbits by(3). Hence the FULL quotient is the smooth Hausdorff space

```text
Q_L=R^3_terminal disjoint-union coproduct_p
                     (R/(log p)Z) x R^2.                 (4)
```

All chart/arrow transitions translate u and preserve beta. Directly
d beta=(dv-vdu) wedge(dz+zdu), beta wedge d beta=du wedge dv wedge dz,
beta(R)=1 and i_R d beta=0. Thus the contact form and its contact volume
descend everywhere, not as a multiple-counted pushforward of chart measure.
The complete Reeb flow is Phi^t(s,v,z)=(s+t,e^t v,e^(-t)z), with its
whole-domain inverse and every-Borel volume preservation. It commutes with
all actual arrows, so this is an owned flow on the entire quotient.

All physical return groups are(log p)Z on v=z=0 in each p component, and
zero elsewhere, including the terminal component. There is exactly ONE
primitive orbit per p, least period log p, and every kth repetition has
period k log p. No nonzero transverse state enters such an orbit in finite
physical time. Periodic phase is s modulo log p, with every predecessor
phase determined by A(e); the q_p source stages do not create extra packets.

## 6. Explicit reference comparison; no unproved groupoid isomorphism

On normal states, proper execution realizes each RCF01 factorization step
with the SAME single normal scaling and extra identity work steps. Thus its
normal-state entrance sum A(N(w)) equals the RCF01 sum. For a work state,
A(T)=A(N(E(T))). Sending a normal state to w and a work state to E(T), with
unchanged geometry, therefore induces the explicit identity in the canonical
coordinates(4) to RCF01's quotient. It is a bijective smooth strict-contact
flow conjugacy, including the entire terminal and transverse components.

It is NOT here asserted to be a lag-graded source-groupoid isomorphism.
For example, the arrow from u to u+log p in the canonical normal core chart
has lag q_p under(3), whereas the corresponding RCF01 arrow has lag1.
The natural comparison does not preserve that grading. No claim of abstract
global groupoid nonisomorphism is needed for this precise distinction.

## 7. FULL F, U and D controls

**F.** All work termination and exit words are unchanged. Every nonempty
normal word now enters fixed singleton n=gcd(word), including n=1.
Every T enters the singleton gcd(E(T)) if its exit is nonempty; otherwise
it enters N(empty). These are the full basins and all source cycles.
The terminal basin is exactly N(empty) plus T(d,1,empty), d>=2.

At N targets keep every main gcd/work predecessor and ADD the singleton
self predecessor when the target is N((n)), inverse(nQ,X/n,Z).
At T targets REMOVE main launch predecessors, keeping precisely scan and
division predecessors in(2). Thus all work states stay, including newly
unreachable T(2,r,empty). Every inverse domain remains whole and J=1.

The F quotient has terminal R^3, a separate unit-core R^3, and one
circle(log n)xR^2 for EVERY n>=2. The n>=2 arrow formula is(3) with
q=1 and log n, recomputing entrance depths and sums for F's OWN cores.
The unit basin has identical canonical geometric coordinates
and every integer lag, so source isotropy is Z there, zero in other basins.
All this ineffective source isotropy is retained. Physical periods exist
only on the zero-transverse n>=2 circles: exactly one primitive per INTEGER,
including composites. Terminal and unit components have no physical periods.
The same beta/Reeb/volume proof applies on this entire F quotient.

**U.** Keep every typed rule, inverse WORD and work state, with all geometric
inverse maps now identity. Formula(3) becomes identical geometric coordinates
and k congruent to d(e_y)-d(e_x) modulo q_p in a p basin; the terminal lag
is still exactly the depth difference. Source isotropy is q_p Z in a p basin,
NOT Z, and zero in the terminal basin. Its zero-IMAGE kernel retains all of it.
The full coarse quotient is R^3 for EVERY core, with real u. The same beta
and complete Phi descend, but real-u translation forces ALL physical return
groups to zero. Microcycle source returns are not physical closed orbits.

**D.** Keep the entire main source, G_L and quotient(4). The complete drift
Psi^t(s,v,z)=(s+t,v,z) descends and preserves beta and volume. However
beta(partial_s)=1+vz and i_(partial_s)d beta=-d(vz); it is not globally the
Reeb field (it agrees with R only at v=z=0). In EVERY p component all
(v,z) in R^2 label distinct primitive circles, each of least period log p.
Thus each p has continuum multiplicity, not the main's isolated orbit.
Terminal drift orbits are free. No center selection repairs this control.

## 8. Adverse check and fifth-round stop

The full executor supplies a scoped positive source-localization result:
proper launches perform local tests, while arbitrary work states remain and
are exhausted by the basin proof. Extra computational stages change actual
source lag but not the proved quotient clock/primitive ledger. Conversely,
the program, normal launch scale, gcd instruction and chosen contact geometry
are not thereby canonical, efficient or an endogenous real-feedback law.
F, U and D demonstrate separate arithmetic-selection, holonomy and transverse
isolation boundaries. Strong naturalness stays OPEN; T3 is not audited.
This report completes the assigned fifth-round proof only. No sixth round,
new architecture, quantum claim or formal Route coordinate is authorized here.

EOF — all-state MAIN and full F/U/D independent proof complete.
