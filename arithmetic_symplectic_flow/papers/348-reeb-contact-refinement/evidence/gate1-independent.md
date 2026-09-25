# Independent Gate1 derivation — 348 Reeb/contact refinement

**Candidate:** `ANG-20260921-RCF01`  
**Gate1 verdict:** PASS for the frozen MAIN contact/quotient/complete-flow owner.  
**Gate2:** NOT AUDITED here; no physical-return or primitive-packet verdict.  
**Review standing:** Internal, inherited model/shared history, `NOT_CALIBRATED`.

## 1. Authorization, inputs and limits

This is a new mathematical audit authorized after the earlier definition-only
scope review. That earlier report is preserved and has not been edited.
The sole scientific input for this derivation was the complete 187-line
`candidate-card.md`, personally reread through its clarification EOF, with
measured SHA-256
`9fd564c3a42a09fb38463c860daa4cc451887015e3334485108b1537cba8622a`.

The ARS router, DA role and logical-fallacy guidance were reread; previously
completed workflow/runtime reads were retained. An initially truncated
combined instruction-tool response was followed by a complete untruncated
read of the affected router portion. No scientific input was truncated.

No root proof, manuscript, paper344, other scientific package, peer conclusion,
web source, auxiliary agent or experiment was consulted. No external theorem
lookup was necessary: the arithmetic and geometric arguments below are given
directly. Tool use was limited to instructions/card reads, hashes and writing
this assigned report. There was no model change, external upload or Git work.

Shared historical context, including related older constructions, was already
inherited. The proofs below are reconstructed from the present card, not
claimed to be blind rediscovery or evidence of independent model errors.
No old candidate theorem, clock or Route credit is transferred.

The scope is MAIN Gate1 only. Word basins are derived because the FULL quotient
cannot be owned merely by selecting convenient charts. The three controls,
physical return groups, full periodic locus, primitive multiplicity and Gate3
naturalness are deliberately not classified in this report.

The earlier ARS scope checkpoint remains separate. This document supplies
independent Gate1 analysis and a bounded adverse check, not a claim that a
later full manuscript/packet-review cycle has already been completed.

## 2. Arithmetic source needed for the entire quotient

### 2.1 Factorization and word dynamics

The card's cover atoms are exactly positive integers greater than one with
no proper integer divisor. Factorization into such atoms exists by induction:
a non-atom n splits into two smaller positive integers greater than one,
to which the induction applies. For uniqueness, an atom p dividing ab
divides a or b: if it does not divide a, the Euclidean algorithm gives
integers s,t with sp+ta=1, and multiplication by b gives p dividing b.
The Euclidean algorithm terminates because positive remainders decrease;
back-substitution supplies this identity. Cancelling one atom at a time
proves uniqueness of the multiset, and increasing order fixes its word.
No prime table or external arithmetic result is an input.

For a nonempty word w, successive leading-pair coalescences reduce it to
the singleton (g), where g is the gcd of every original entry. A singleton
1 then reaches empty. If g is an atom p, its word is fixed. If g is not
an atom, its factor word coalesces to the gcd of its atom entries. That
gcd is p when all factors are one atom p, and is 1 when at least two
distinct atoms occur. In the latter case one further step reaches empty.

Thus every word has finite first entrance into exactly one core label:

```text
b(w)=(p)  if gcd(w)=p^e for one cover atom p and an integer e>=1;
b(w)=empty otherwise, including w=empty.
```

The empty word is terminal, not fixed by an added map. The only repeated
word cores are the singleton atoms. This is a proof for all words, including
units and arbitrary order, rather than a finite word experiment.

Let h(w) be the first entrance time into that core word, with h=0 on a
core itself. Let D(w) be the product of the leading entries along the first
h(w) steps, with D=1 for h=0. These are finite positive integers. They
record actual defined steps, not an inserted physical time or roof.

### 2.2 All actual source inverses and full domains

On a nonempty source chart whose first entry is a,

```text
S(w,q,xi,z)=(C(w),q/a,a xi,z).
```

For a singleton source, the target word must equal fct(n), and its unique
geometric restoration is (nQ,X/n,Z). For a source with at least two entries,
the target word must be (g,tail) with gcd(a,b)=g, and restoration is
(aQ,X/a,Z) in the chart (a,b,tail). These are precisely the two source-
length cases; both directions of each displayed inverse identity follow
by substitution. There are no other predecessor types or extra real tests.

Every listed inverse domain is the ENTIRE target chart Q>0, X,Z arbitrary.
Zeros, signs and the surface specified in the card introduce no exception.
Identical presentations of one source are deduplicated, not distinct words.
The empty target has the single immediate predecessor chart (1). Every
nonempty target (g,tail) has countably infinitely many pair predecessors,
for example (g,kg,tail), k>=1, as well as any allowed singleton predecessor.
Consequently S is onto Y although its own domain excludes the empty chart.
All terminal incoming is retained.

The domain is an open union of charts and each chart branch is a smooth
diffeomorphism onto its entire target chart. Hence S is a partial local
homeomorphism. Its inverse derivative diag(a,1/a,1) has determinant one.
For every Borel A in every actual target branch,

```text
mu(I A)=mu(A)=integral_A 1 dmu.
```

The inverse IMAGE version is exactly one at EVERY point, not only almost
everywhere, and all finite branch compositions have the same version.
This does not make the many-to-one S globally measure preserving: a positive
finite-measure set in a nonempty target chart has infinitely many disjoint
preimages of that same measure in different word charts.

## 3. Full contact form and exact Reeb normalization

Use the global chart coordinates u=log q, v=q xi, z=z. They cover all R^3;
their inverse is q=exp(u), xi=exp(-u)v. No transverse state is removed.
The frozen form and its derivative are

```text
beta=(1+vz) du +(v dz-z dv)/2;
d beta=(z dv+v dz) wedge du +dv wedge dz;
beta wedge d beta=du wedge dv wedge dz=dq wedge dxi wedge dz.
```

The last identity follows by direct expansion: the vz term in the first
contribution is cancelled by the two mixed half-terms. The volume is
nowhere zero and positive in the displayed original coordinate orientation.
In particular vz=-1 does not cause degeneracy; checking only its du
coefficient would give a false obstruction.

The prescribed physical action in these coordinates is

```text
Phi^t(u,v,z)=(u+t,exp(t)v,exp(-t)z);
R=partial_u +v partial_v -z partial_z.
```

Its normalization is beta(R)=1+vz−vz=1. For the contraction, the first
term of d beta contributes −z dv−v dz and dv wedge dz contributes
v dz+z dv. Thus contraction_R(d beta)=0 at every point. This is the
Reeb vector field of the frozen beta, with no time rescaling and no
division by a potentially vanishing function.

On every source branch, S is simply (u,v,z) to (u−log a,v,z).
Its constant chart translation preserves beta exactly. Every inverse and
actual finite composition also preserves beta and its volume. The source
branch IMAGE computation is separate from the physical action computation.

## 4. Actual retained-lag groupoid and FULL quotient

### 4.1 Normalization and every actual arrow

For a point in word chart w put

```text
s=u-log D(w),  v=q xi,  z=z.
```

Applying S for h(w) actual steps reaches the core chart with these real
coordinates. On an atom core (p), further source steps translate s by
−log p and leave v,z unchanged. On the empty core no further step exists.

Take y and x with word labels w_y,w_x, entrance times h_y,h_x and normalized
coordinates s_y,s_x,v_y,v_x,z_y,z_x. Complete arrow conditions are:

- Both endpoints must have the same core label and equal v and z.
- In the empty basin, s_y=s_x and the only possible lag is k=h_y−h_x.
- In the atom-p basin, s_y−s_x=j log p for an integer j, and the only
  possible lag is k=h_y−h_x+j.

For necessity, any common future can be advanced to its first core along
already valid histories. In an atom core it can then advance further by
nonnegative integer translations. For sufficiency in the atom case, choose
nonnegative i,l with i−l=j; then S^(h_y+i)y=S^(h_x+l)x. In the empty
case the first-core images already agree. This includes all finite incoming
charts and does not assume a chosen source section exhausts the orbit.

The conditions also prove that every source isotropy group is trivial:
equal endpoints force j=0 and k=0. A fixed singleton WORD is not a fixed
atlas point, since its nonunit q scaling is retained. This source-isotropy
statement is not a statement about physical-time returns on Q.

The common-future triples form a groupoid by the usual direct alignment:
compare the two middle history lengths and extend the shorter equality
only along the longer history already known to exist. This respects the
empty terminal chart. Inverse, identity and added lag follow immediately.

### 4.2 The prescribed topology, not a replacement topology

Fix w_y,w_x and k. The arrow set in this open component of
Y x discrete Z x Y is either empty or the whole graph of one constant
u translation with v,z fixed. Its source and target projections are chart
diffeomorphisms. The inherited groupoid topology is therefore a countable
disjoint union of such graphs: Hausdorff, second countable, locally compact
and étale. No discrete lag or incoming source is discarded to obtain this.

Consider the explicit space

```text
M = R^3_empty
    coproduct over cover atoms p of [(R/(log p)Z) x R^2_(v,z)].
```

Map every word chart to its core component by (s,v,z), reducing s modulo
log p only in an atom basin. On EACH entire chart this map is continuous,
open and onto the corresponding whole component. The core charts make
the total map onto M. Its fibers are exactly the actual G-orbits by4.1.
An open continuous surjection is a quotient map, so it induces a homeomorphism
from the card's FULL orbit quotient Q to M. This proves the actual quotient
topology, rather than merely exhibiting a set bijection or preferred section.

The terminal component is R^3. Each other component has the standard smooth
circle coordinate s modulo the positive number log p and the ENTIRE v,z
plane. These countably many components give a Hausdorff second-countable
smooth three-manifold. The quotient map is locally a diffeomorphism.
The circumference here is a source-translation identification; no physical
primitive period or multiplicity is inferred in Gate1.

In these quotient coordinates the descended form is

```text
bar beta=(1+vz) ds +(v dz-z dv)/2;
bar beta wedge d bar beta=ds wedge dv wedge dz.
```

The differential ds is a global one-form on each circle, although s is not
a global real-valued function there. Translation overlap maps preserve
the form; its pullback is the original beta on every incoming chart.
This supplies the full smooth contact quotient and positive contact volume.

## 5. Complete physical flow, descent and its own IMAGE

For every real t, Phi preserves q>0 and finite real xi,z and has inverse
Phi^(-t). Its exponential formulas satisfy the action law and give a smooth
complete flow on Y. It commutes with S on every nonempty chart, leaves the
empty word chart intact, and preserves all legal word histories. Hence
(y,k,x) maps to (Phi^t y,k,Phi^t x), an actual arrow with the same lag.
This proves compatibility with every arrow, not only generators at one core.

On the full quotient model its action is

```text
(s,v,z) -> (s+t,exp(t)v,exp(-t)z),
```

with the existing circle interpretation of s when appropriate. This is a
complete smooth flow on Q. It preserves bar beta exactly: vz and the
two terms v dz and z dv are unchanged under pullback, as is ds. Its
generator is the descended normalized Reeb field proved in section3.

On the original atlas coordinates, the physical derivative is
diag(exp(t),1,exp(-t)), of determinant one. The actual physical inverse
IMAGE is therefore one everywhere and satisfies the EVERY-Borel law on
the whole chart; counting the unchanged word labels gives global physical
mu invariance. This uses Phi's own bijective flow, not source-S invariance.
The descended contact volume is invariant as well, by the explicit pullback
or the quotient-coordinate determinant one. All zero states and vz=-1 remain.

The quotient volume must NOT be identified with the atlas measure pushforward.
Already one atom core chart covers its circle component in infinitely many
u strips, giving infinite atlas mass above a positive finite-volume local
quotient box. In the empty component, the infinitely many all-unit word
charts have D=1 and each maps onto the same R^3 component; their contributions
also make such a pushforward infinite. The locally finite contact volume
is instead the descended differential form just proved to exist.

## 6. Gate1 adverse tests and bounded conclusion

The attempted failure mechanisms were concrete:

- A vanishing du coefficient at vz=-1 does not kill contactness: the full
  wedge is the positive volume form, with no omitted states.
- Syntactically fixed atom words do not license source isotropy: the whole
  geometric scaling makes the actual retained-lag owner principal.
- Source inverses cannot be reduced to a chosen refinement history: every
  gcd-pair and allowed singleton branch is included, with full real domains.
- A section-level circle model would not establish the quotient. The open
  surjection and exact fiber proof above identify the full orbit topology.
- Branchwise unit Jacobian does not imply global S invariance; this failure
  is explicitly separated from Phi's actual global physical invariance.
- Infinite-sheet pushforward volume is not a substitute for descended
  contact volume. Both constructions were distinguished explicitly.

No substantive Gate1 identity or owner failure was found. The strongest
remaining objection is about significance and later arithmetic selectivity,
not this contact/flow construction: an exact Reeb owner does not establish
one primitive per atom, exclude additional periodic fibers, prove naturalness
or supply an operator. Those questions require the separately scoped Gate2
and later analysis. No packet is selected or counted here to answer them.

The exact conclusion is MAIN Gate1 PASS: full contact/Reeb normalization,
complete source inverse and every-point/every-Borel IMAGE, actual retained-
lag groupoid, full smooth Hausdorff contact quotient, and complete descending
physical flow with its own invariant volume are established above.

Gate2 physical return groups/periodic locus/primitive ledger and all three
controls remain NOT AUDITED BY THIS REPORT. No T2 promotion, strong naturalness,
classical ASFS pass, T3 result or formal Route-B standing is issued. The
frozen scope-review file and all other candidate files remain untouched.

EOF — completed MAIN Gate1 derivation and adverse check, pending only report readback/hash freeze.
