# Actual different-invocation mathematical review

**Paper ID:** 196-face-cotangent-conservative-lift  
**Candidate ID:** ASC-20260916-FCL01  
**Reviewed status:** ADVANCE — COMPLETE SYMPLECTIC COPRODUCT WITH FULL LOG-PRIME PACKETS; NEW TOPOLOGY; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.  
**Reviewer invocation:** `/root/research_controller/face_lift_reviewer_round19`  
**Core-byte observation:** 2026-09-16 05:55:53 UTC.  
**Disposition:** No required mathematical correction identified within this frozen contract.  
**Calibration:** NOT_CALIBRATED; no venue criteria or publication-readiness assessment.

## Actual reading and provenance

The reviewer first completely read the frozen version-1
[card](../candidate-card.md) before reading the author's new proof, and
independently derived the all-state cotangent iterate, singleton packet
equation, time-preserving projection and non-quotient boundary for h.
That preliminary feedback was sent to the controller and shared nonblind.
The original [193 card](../../193-indecomposable-radial-quotient/candidate-card.md)
and [193 paper](../../193-indecomposable-radial-quotient/paper.md) were
actually read in full as mathematical dependencies, including their
weighted topology, radial quotient, section, actual roof and full packets.
An old review verdict was not used as a substitute for those arguments.

After the controller reported author stop and core readiness, the reviewer
actually read all five current files completely: [README](../README.md),
[candidate card](../candidate-card.md), [paper](../paper.md),
[claim ledger](../claim-ledger.md), and [evidence index](README.md).
Their observed line counts were respectively 29, 175, 390, 31 and 73.
The final pass checked the whole deck-strip/endpoint proof, all-time
return equations, the full-flow non-quotient boundary, controls and scope,
not merely agreement with the earlier card-derived expectation.

This is one actual separate invocation, using the current inherited model
and reasoning setting with shared context. The final review is nonblind;
the early card-derived feedback is explicitly disclosed above. No helper
reviewer, different-model call, external API upload or model override was
used. This is not human peer review, a calibrated review or evidence of
independent error processes. ARS informed only bounded domain accuracy,
claim/evidence/reasoning and counterargument discipline; no full reviewer
panel, publication pipeline or external-literature novelty claim was run.

## Independent mathematical checks

### 1. Entire geometry and exact inverse

For a finite face J, fix a reference atom b. Coordinates
w_a=log(u_a/u_b), a different from b, identify its whole strict simplex
with real affine space. The frozen return sends w_a to
w_a+log(b/a). In the corresponding tautological cotangent coordinates,
its full lift fixes every momentum eta, so the complete map and inverse
are exactly

    G(w,eta,Q,P) = (w+ell,eta,2Q,P/2),
    G^(-1)(w,eta,Q,P) = (w-ell,eta,Q/2,2P).

This verifies both global domain and preservation of
sum_a dw_a wedge d eta_a + dQ wedge dP, not only preservation on a zero
section. For singleton faces the absent cotangent coordinates leave the
entire symplectic real plane. Countably many open invariant components
give the asserted Hausdorff coproduct, with dimensions 2 times the
support cardinality. The componentwise claim does not create a globally
fixed-dimensional carrier. **Anchor:** equation: paper (2)--(5), Proposition 1.

### 2. Whole-source projection and its actual topology

Each fixed face has the usual finite-dimensional topology under every
restricted weighted norm; its inclusion into S is continuous. The
coproduct property therefore proves continuity of h globally, while
the full zero-covector lifts prove surjectivity. The equations hG=Fh
and rho=tau h are exact.

The sequence (1-1/k)q_2+(1/k)q_3 tends to q_2 in every old weighted
norm. But h inverse of {q_2} is the open singleton component, whereas
{q_2} is not open in S. Thus h is not a quotient map. This verifies,
rather than suppresses, the topology change. **Anchor:** equation: paper
(6) and Section 3's explicit weighted-norm sequence.

### 3. Deck quotient, endpoint charts and complete actual time

For every integer r the finite sum c_r(u)=sum_a u_a a^(-r) is positive.
Direct iteration gives F^r u=D^(-r)u/c_r(u) and
T_r=-log c_r. The identity
T_(r+1)-T_r=rho(G^r z)>=log 2 holds also for negative r. It supplies
both-time divergence independently of covector size.

Every nonidentity deck power changes the real coordinate by at least
log 2 in absolute value. Hence a horizontal strip narrower than log 2
is disjoint from its nontrivial translates, and the open quotient map
is injective on that strip. Bounded time neighborhoods have only
finitely many potentially intersecting translates, so the manuscript's
finite shrinking argument separates inequivalent points. Around a seam,
the short negative-time piece is represented in the preceding roof
interval using the smooth inverse deck map; the positive piece lies in
the current interval. These are precisely the stated endpoint gluing
charts. Thus the endpoint model has the same quotient topology, not
only the same points.

Time translation commutes with the deck map and is defined for every
real time. The open quotient and its product with the real line give
joint continuity; the same charts give componentwise smoothness. The
section at zero is embedded, and its positive crossings are exactly
T_r for r>=1. Its first return is therefore G with actual time rho.
**Anchor:** equation: paper (7)--(10), Proposition 2.

### 4. Full-flow projection, including the non-quotient boundary

The proposed cover map (z,t) to [exp(t)h(z)] satisfies

    exp(t-rho(z)) h(Gz) = D^(-1) exp(t) h(z).

It therefore descends continuously. Writing any old cone point as
exp(t)u and choosing a full-carrier lift of u proves surjectivity onto
the entire old flow. The unchanged time variable proves exact time
preservation. Support is preserved by all the actions involved, so
the inverse image of the old prime circle gamma_2 is precisely the
open singleton suspended component. The projected mixed sequence
converges to [q_2], showing gamma_2 is not open. Thus Pi too is not
a quotient map or conjugacy. **Anchor:** equation: paper (11) and the
following open-preimage counterexample.

### 5. Exhaustive packets, repetitions and monodromy

For every positive integer r and every state,

    G^r(w,eta,Q,P) = (w+r ell,eta,2^r Q,2^(-r) P).

A mixed support has a nonzero ell, so no momentum or transverse
coordinate can make its base point periodic. A singleton has no
w or eta and is fixed by an iterate exactly when Q=P=0; this point
is already fixed at the first iterate. The deck return equation then
shows that all positive flow periods over that point are exactly
r log a. The whole time circle is one oriented orbit, and the source
calculation identifies the atoms a with primes. No center or momentum
subset is substituted for the phase space in this argument.

The actual singleton Poincare map is the whole plane map B, with
derivative diag(2,1/2) and r-fold derivative diag(2^r,2^(-r)). The
neutral flow direction is separate. Noncentral singleton trajectories
are aperiodic even though their projections lie on an old closed
circle; the manuscript explicitly retains this distinction.
**Anchor:** equation: paper (12), Theorem 3 and its following paragraph.

## Findings, limits and empty-correction coverage

No required correction was identified after the complete final reading.
This is a bounded finding, not a correctness certificate. The following
coverage records why the absence of corrections is not a missing review:

| Examined claim surface | Checked evidence | Basis and retained limit |
| --- | --- | --- |
| Full symplectic geometry and inverse | Global coordinates and exact maps (3)--(5) | All covectors and real transverse states are covered; only componentwise geometry is claimed |
| Topology and old-source relation | Section 3 and (11), explicit convergent mixed sequence | Continuous onto maps are proved and their failure to be quotient maps is retained |
| Complete physical clock owner | All-integer telescoping, deck strips and endpoint charts (7)--(10) | Both directions and every state are covered; no change of roof or metric-completeness inference |
| Full intrinsic packet ledger | Complete iterate (12) plus the deck return equation | No hidden mixed or transverse periodic family; no selection of centers as carrier |
| Transverse stability | Exact singleton return derivative | Universal hyperbolic multipliers only; no arithmetic trace weight or Hamiltonian claim |
| Arithmetic origin and naturalness | Indecomposable source argument and Section 6 controls | Source design, positivity, scale and uniform plane remain engineering choices; naturalness stays OPEN |
| Status and same-object scope | All five current files and Section 7 | One new ASC owner, unchanged 193 dependency; no analytic result from another lane is attached |

The identity-plane, omitted-plane, changed-roof, omitted-quotient and
distinct generic-multiplier controls have the effects stated in Section 6.
In particular the same mechanism on another admissible generator alphabet
retains the PROVES_TOO_MUCH concern. The review does not settle arithmetic
naturalness, original-topology symplectification, fixed-dimensional or
infinite-support extensions, a lamination, a Hamiltonian/contact owner,
an analytic operator or any formal Route coordinate.

## Exact core-byte binding and handoff

The following current SHA-256 bindings were obtained by the read-only
`sha256sum` command after the complete final reading and the reported
author stop, with the ledger-only formatting delta recorded below:

| Core file | SHA-256 |
| --- | --- |
| [README.md](../README.md) | `2051634c94c0408d1f91a9c846591d91013da486383668dea97b64d12bbb0d02` |
| [candidate-card.md](../candidate-card.md) | `628166f9bdbe9c9f3b709c21084c174379470bd0205e80de4097941efce7733b` |
| [paper.md](../paper.md) | `b070053dfa54448d7e889088936fc3144e9bb9b4d694252bca9b14f53f6c2ad2` |
| [claim-ledger.md](../claim-ledger.md) | `26b4fad9885919ff996a84f79f97a7892a7411be1a96de0b80b62346f2c4a97d` |

**Actual formatting-delta receipt, 2026-09-16 06:20:29 UTC.** Root
reported changing only the cardinality token in the ledger's
"single fixed dimension" table row from `2|J|` to `2\|J\|`.
The reviewer actually read that current row and confirmed the escaped
Markdown preserves the expression and its varying-dimension claim,
then obtained the current ledger SHA-256 shown above. The initial
ledger digest `28e379bc1d012d043ff7708772efb10e81019a1abb25e99b145576d4918a3f50`
is superseded history, not a second current binding. The mathematical
disposition is unchanged. No whole-proof reread or batch check was run;
the other three core bindings remain unchanged. Only this review file
was updated, and this delta review is complete with writing stopped.

The evidence index is deliberately unbound for later actual closure and
root-verification receipts. These hashes identify reviewed bytes; they
are not mathematical evidence in themselves. No whole-batch mechanical
check, navigation update or publication operation was run by this reviewer.
Only this review file was written. The reviewer now stops writing and
returns integration authority to the controller/root. Any changed core
claim or byte requires its changed-input review; no future change is
silently covered by this receipt.
