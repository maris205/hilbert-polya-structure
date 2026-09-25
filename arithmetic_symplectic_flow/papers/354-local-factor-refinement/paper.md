# Local factor refinement with the entire work-state carrier

**Candidate:** `ANG-20260921-LFR01`.  
**Batch:** `RCF01-BATCH-20260921-A`, round5/5.  
**Status:** `FULL LOCAL EXECUTOR AND PRIME PACKETS ESTABLISHED; NATURALNESS OPEN`.

## 1. Result and frozen scope

The [card](candidate-card.md) replaces the one-step fct source operation
by an autonomous divisor-testing program, keeping ALL typed work states.
The resulting full quotient owns a complete Reeb flow with exactly one
primitive orbit of least length log p per prime, all repetitions and no
other closed orbit. Its quotient contact flow is explicitly conjugate to
RCF01's, but its specified integer source lags have changed. This is a
source refinement, not a genuinely different physical-flow architecture
or a proof that the chosen geometric clock is canonical.

The lineage is proper-divisor symbols -> local arithmetic execution ->
factor-word refinement -> full contact quotient. No prime list, test for
primality, complete-factorization call or successful-execution subspace
is built into the transition. Gcd remains a declared integer operation;
the program, launch scaling and contact geometry remain declared designs.
The preceding clock counter-control353 is not repaired by this result.

This is the final authorized round. No sixth candidate is frozen here.
Classical A0/A1/A2 NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED;
B NOT INVOKED. No spectral, determinant or zero-location result is claimed.

## 2. Full source and local termination

The discrete states are N(w), w ANY finite ordered positive-integer word,
and T(d,r,a), d>=2,r>=1,a ANY such word. The types are disjoint. Units,
empty, unsorted/invalid accumulators and states not reached by a proper
launch all remain. The exact rules are

```text
N(empty): terminal, no successor;
N((a,b,tail)) -> N((gcd(a,b),tail));
N((n)) -> T(2,n,empty);
T(d,1,a) -> N(a);
T(d,r,a), r>1,d^2>r -> N(a appended r);
T(d,r,a), r>1,d^2<=r,d|r -> T(d,r/d,a appended d);
T(d,r,a), r>1,d^2<=r,d does not divide r -> T(d+1,r,a).
```

**Lemma W: ALL work segments terminate.** Fix ANY initial T(d,r,a).
During a work segment r never increases, and each division decreases it
by at least a factor2. There are finitely many such divisions. The trial
integer d never decreases. A non-exit state has d^2<=r<=r_initial;
there are only finitely many increments before that inequality fails.
The remaining rules exit to N(a) or N(a appended r) in one step. This
proves finite termination for every initial accumulator, without assuming
it is a factorization or imposing a validity predicate. QED.

**Lemma P: proper launches compute the full sorted factor word.** Starting
at T(2,n,empty), every trial state with residual r>1 has no divisor e
with2<=e<d. Initially this is vacuous. Incrementing d after a failed test
preserves it; dividing r by d cannot introduce a divisor of r absent
before. Hence a dividing d is the smallest nonunit divisor of the current
r and is prime. If d^2>r, a composite r would have a divisor between2
and sqrt(r)<d, a contradiction; this final residual is prime. Emitted
entries are nondecreasing, since d never decreases and a final r>1 must
be at least d. The product of the emitted entries times residual r stays
n. Lemma W gives termination. Thus the output is exactly the complete
sorted prime-factor word, including multiplicity; n=1 yields empty.
This is a theorem about the rules, not an fct instruction within them.
It does NOT claim that arbitrary malformed work accumulators have this
factorization meaning. QED.

**Lemma B: all eventual discrete cores.** From N(w), length>=2,
successive gcd operations lead to N(g), g=gcd(all entries). Its proper
launch then gives N(fct(g)) by Lemma P. If g=1 it reaches N(empty).
If g=p^a it reaches N(p) after gcd collapse. If g has distinct prime
factors it reaches N(1), then N(empty). Every arbitrary work state first
exits to some normal word by Lemma W and hence obeys this classification.
Thus there is just one terminal basin and one basin per prime, and no
other eventual cycle. The assignment of an arbitrary work state is its
actual eventual normal-word basin, not an assumed factorization label.

For prime p let b_p=floor(sqrt(p))+1. The cycle through N(p) consists of
N(p), T(2,p,empty), ..., T(b_p,p,empty), then N(p). None of the trial
integers before b_p divides p. Its least discrete length is
ell_p=b_p>=2; its states are all distinct. This is a microcycle of C_L,
not a periodic full geometric state or a physical time interval.

## 3. All inverse branches and branch measure law

Each typed state has its entire chart q>0,xi,z real; u=log q,v=q xi.
At every nonterminal normal state with head n the source geometry is
(q/n,n xi,z), equivalently u->u-log n with v,z unchanged. At EVERY
work-state step it is identity. This defines S_L without a runtime roof.

The following lists are exhaustive by splitting the preceding forward
rules. All conditions are discrete, so every branch domain is the WHOLE
geometric target chart, never a restricted transverse subset.

At N(w), all predecessors are:

1. N((a,b,tail)) when w=(gcd(a,b),tail), for every such ordered pair;
   inverse geometry (Q,X,Z)->(a Q,X/a,Z).
2. T(d,1,w) for every d>=2, inverse geometry identity.
3. T(d,r,a) when r>1,d^2>r and w=a appended r, geometry identity.

At T(d,r,a), all predecessors are:

1. N((r)) if d=2,a=empty, inverse geometry (r Q,X/r,Z).
2. T(d-1,r,a) if d>=3,r>1,(d-1)^2<=r and d-1 does not divide r,
   inverse geometry identity.
3. T(d,d r,b) if a=b appended d and r>=d, inverse geometry identity.

For the last line, the forward inequality d^2<=old residual=d r is
exactly r>=d; the old residual>1 and divisibility are then automatic.
Conversely every listed state satisfies its forward case and returns
exactly the target, including its real coordinates. Distinct cases have
different predecessor types or trial/residual data; identical triples
are not counted twice under different branch names. These observations
prove both inverse identities and completeness, including empty/units.
The map need not be onto: for example T(2,1,(1)) has no predecessor,
but it remains a full source chart and exits to N(1).

Each inverse has Jacobian1, pointwise throughout its domain. Consequently
mu(I(E))=mu(E) for EVERY Borel target set E, for
mu=counting typed states times dq dxi dz=du dv dz on each chart.
Finite branch compositions have the same law. This does not assert
global measure invariance of the many-to-one S_L; N(empty), for example,
has all the disjoint work predecessors T(d,1,empty).
The source IMAGE logarithmic cocycle is identically ZERO. It is NOT the
physical Reeb time or the log p translation accumulated around a cycle.

## 4. Actual lag, full quotient and topology

For any discrete state s define N_s as its first hit at the canonical
anchor N(empty) or N(p). It is finite by§2. Let A_s be the sum of log
heads over NORMAL steps before that first hit; work steps contribute0.
Anchors have N=A=0. One complete prime microcycle subtracts log p from u:
its only nonidentity geometry is its normal launch. Let L_p=log p.

The full actual groupoid consists of (y,k,x) with S_L^m y=S_L^n x,
k=m-n, legal m,n>=0. Put theta_x=u_x-A_(state x). Every actual arrow
requires the same basin, v_y=v_x,z_y=z_x, and exactly

```text
terminal: theta_y=theta_x, k=N_y-N_x;
prime p: theta_y-theta_x=j L_p,
         k=N_y-N_x+j ell_p, for some integer j.
```

Necessity: extend any common future equally until it hits its anchor.
The terminal admits no extra steps. In a prime basin the subsequent
anchor visits occur exactly at multiples of ell_p, subtracting L_p per
visit. Sufficiency: the terminal uses the two first-hit times; the prime
case uses m=N_y+a ell_p,n=N_x+b ell_p with a,b>=0,a-b=j. Such a,b
always exist. This proves ALL actual triples, not merely a generated
equivalence relation. For y=x, positivity of L_p forces j=0 and then
k=0. Thus full-state source isotropy is trivial everywhere, despite the
discrete C_L microcycles. All terminals and incoming arrows remain.

For each fixed state pair and lag, a nonempty arrow piece is the graph
of a constant u translation. Under the frozen topology inherited from
Y_L x discrete Z x Y_L it is open and a source/range chart. These give
a countable Hausdorff locally compact etale groupoid with actual lags.

The phase map to (theta,v,z), reducing theta modulo L_p in prime basins,
has exactly the preceding orbit fibers. It is onto, continuous and OPEN:
each full atlas chart maps by translation and, when appropriate, a circle
covering. Therefore the FULL quotient is the Hausdorff smooth manifold

```text
Q_L = R^3_terminal disjoint-union
      coproduct_p ((R/(log p) Z) x R^2).
```

This proof retains every malformed/unreachable work chart. No validity
filter, core restriction, representative selection or extra quotient by
a guessed integer label has been used.

## 5. Contact/Reeb flow and entire physical ledger

Every transition and chart overlap translates u and fixes v,z. Therefore
the frozen beta descends. Directly, with alpha=dv-v du, eta=dz+z du,

```text
d beta=alpha wedge eta;
beta wedge d beta=du wedge dv wedge dz;
R=partial_u+v partial_v-z partial_z;
beta(R)=1, i_R d beta=0.
```

Thus beta is contact everywhere and the SAME frozen Phi^t is its complete
Reeb flow. Its formula (u+t,e^t v,e^-t z) commutes with all arrows and
exists for every real t on every full chart/component. It preserves beta
and the descended nu=beta wedge d beta for every Borel set. Nu is defined
locally on the quotient, NOT the pushforward of infinite counting-sheet
measure. As in the directly checkable v-expanding box, volume preservation
does not imply measure-theoretic conservativity or recurrence.

In the terminal component a physical return requires t=0. In a prime
component it requires t in L_p Z, e^t v=v and e^-t z=z. Hence the ENTIRE
physical return group is L_p Z on v=z=0 and {0} everywhere else.
The zero-transverse circle is one transitive physical orbit per prime,
least positive period L_p, with all positive repetitions k L_p. There
are no further closed orbits or incoming-sheet multiplicities. Notice
the three different quantities: discrete cycle length ell_p, source
return lag ell_p per anchor turn, and physical time L_p. None replaces
another in the primitive/repetition convention.

**Exact comparison with RCF01.** Map each quotient component by identity
on (theta,v,z) to RCF01's corresponding anchored component from348.
The inverse uses the LFR01 anchor chart N(empty) or N(p). Both directions
are well-defined smooth maps by the full orbit-fiber proofs, and preserve
beta and intertwine Phi^t. This proves a contact-flow conjugacy of the
FULL QUOTIENTS. It does not identify their source groupoids: at the named
prime anchor LFR01 uses lag ell_p for a log p translation, whereas RCF01
uses lag1. The specified anchor identification is not lag preserving.
No general theorem of non-isomorphism for arbitrary groupoid maps is
claimed. The physical model has been re-realized locally, not enlarged.

## 6. Three controls with all their work states

### F — FACTOR-OFF

Keep all work states/rules and normal gcd steps, but change every normal
singleton to N(n)->N(n) with scale n. Its OWN inverses at N(w) are all
three main normal-target families PLUS N(n) itself when w=(n), with
inverse (n Q,X/n,Z). At work targets DELETE the normal-launch family;
the increment/division families remain exactly as listed. Thus some work
charts have no predecessor, but none is removed. All branch Jacobians
are1 on their complete target domains.

Every work segment still terminates, now into a word whose normal gcd
collapse reaches N(g), or into N(empty). Every N(n) is fixed discretely;
there are NO other cycles. For n>=2 the core shifts u by log n, giving
one circle(log n) x R^2 component per integer n. N(1) has zero geometric
shift and gives a whole R^3 component with source isotropy Z. N(empty)
is a distinct terminal R^3 component with trivial source isotropy. The
work inputs into these basins are included through their actual first-hit
phase maps, as in§4 with cycle length1. For n>=2 full-state source
isotropy is trivial; for ALL points in the unit basin it is Z.

These open phase maps prove the full quotient with TWO real components
and all integer cylinders. The same beta/Phi descend and remain complete
Reeb. Actual physical returns are log n Z exactly on the zero-transverse
circle in every n>=2 component and zero everywhere else. There is one
primitive per integer n>=2, so composites survive. Equal lengths of a
repeat and another primitive do not identify their different components.

### U — UNIT-HOLONOMY

Keep C_L but use identity geometry on EVERY step. The complete inverse
state lists of§3 remain, now with identity geometric inverses, all domains
whole charts and Jacobian1. Work termination and discrete basins/cycles
are literally unchanged. For related points geometrical coordinates must
be equal. Actual lags in a prime basin are N_y-N_x+j ell_p; in the
terminal basin only N_y-N_x. Therefore full source isotropy is ell_p Z
throughout a prime basin, and0 in the terminal basin. The full lag kernel
is retained; it is not compressed to Z by choosing a cycle representative.

The open quotient is one R^3 per basin, with REAL u, because no arrow
changes u. Beta and Phi descend as complete Reeb/contact-volume data.
The translating real u forbids every nonzero physical return. There is
NO positive primitive anywhere despite the nonzero source isotropy.

### D — DRIFT-ONLY

Keep the main S_L, its inverses, branch measures, lags and entire Q_L;
only change physical flow to Psi^t(u,v,z)=(u+t,v,z). It commutes with all
main arrows and preserves the contact form and volume, but is NOT its
normalized Reeb flow: beta(partial_u)=1+vz and
i_(partial_u)d beta=-z dv-v dz, not identically0. Every fixed pair(v,z)
on a prime cylinder now defines a distinct primitive circle of least
period log p. Thus there is an R^2 continuum per prime, with all their
repetitions. Actual arrows never change v,z, so none of that multiplicity
can be collapsed. The terminal component still has no nonzero return.

## 7. Decision, reproducibility and remaining design boundary

Portfolio **advance** only the full local-source refinement theorem.
All-state termination, inverse ownership, groupoid topology, contact time
and prime packets pass the frozen owner-level tests. **Stop** any promotion
of this into a new physical architecture, an endogenous IMAGE clock, or
canonical arithmetic naturalness. Strong naturalness remains OPEN.

The entire proof uses exact integer invariants, finite termination for
each arbitrary input, exact arrow equations and differential/return
identities. There is no scientific numerical cutoff, runtime test, hidden
prime table or precision-dependent output. Controls are all-state exact
calculations. The original146-line card is preserved, and original348/349
remain read-only; their clock/analytic results are not silently reassigned.

Internal independent raw-card derivation and ARS three checkpoints are
recorded in evidence/ after actual delivery. They use inherited-model
shared-history scrutiny, NOT_CALIBRATED, not external peer verification.
The same-object ledger is intact for main and each explicitly changed
control. Classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED;
T3 NOT AUDITED; B NOT INVOKED. No external release or publication artifact.

The next DECISION, subject to user confirmation of the five-round summary,
is whether to search for a genuinely coupled arithmetic/geometric rule
that constrains the clock, or to retain this family as an engineered
positive benchmark. Another implementation-equivalent source refinement
alone will not answer353's naturalness objection. No successor object or
sixth round is created in this batch.

EOF — LFR01 complete all-state local-source/contact-flow proof.
