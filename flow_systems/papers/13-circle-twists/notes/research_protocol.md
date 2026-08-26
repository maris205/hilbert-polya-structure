# Paper 13 research protocol — amended Phase-1 active lock

Status: AMENDED / INDEPENDENT EXACT-BYTE RE-LOCK REQUIRED  
Version: P13-P1-v0.1 + P13-P1-AMENDMENT-v1.0  
Date: 2026-08-15  
Route B: false  
Proof, controls, Route, manuscript, and release authorization: false

Active amendment: `phase1_amendment_v1.md`.  Its final digest is recorded in
`pipeline_state.md`.  On conflict, that amendment has precedence over the
initial sections below; all unmodified firewalls and release boundaries
remain binding.

## 1. Research question

For a precisely registered actual globally indiscrete right-real action
groupoid, classify globally continuous normalized circle-valued
two-cocycles, define the corresponding scalar-twisted version of the
Paper-11 author global-QC convolution, and determine whether its
gauge class, test-function algebra, or rigorously transported completion
retains the action or the marked period.

The inherited factorization premise is not fresh; only the amended typed
twist/support-transfer conjunction is a candidate contribution.  This lock
does not assume that every multiplier is a
coboundary, that a twisted completion exists, or that a theorem on a
Hausdorff proxy applies to the actual owner.

## 2. Registered owners and inherited premises

### 2.1 Generic actual owner

Let X be a nonempty set with the global indiscrete topology and a right
action of the additive group R.  The range-first action groupoid is

    G_actual = X x R,
    r(x,t)=x,
    s(x,t)=x.t,
    (x,t)(x.t,u)=(x,t+u),
    (x,t)^(-1)=(x.t,-t).

The arrow topology is the product of the global indiscrete topology on X
and the usual topology on R.  Composable pairs use the chart
X x R^2.

Owner id:

    GEN-INDISC-R-ACTION-CONT-TWIST

### 2.2 Fixed-prime actual owner

For a rational prime p, the registered actual packet owner is

    G_p_actual = Gamma_p_actual ⋊ R.

Inherited source facts are only the fixed-prime packet, right flow,
every-unit multiplicative stabilizer p^Z, and logarithmic clock.  The
additive stabilizer is (log p)Z.  The globally indiscrete packet topology
is companion-owned by Paper 9.  The author action-groupoid and global-QC
records are Paper-11-owned.  Paper 12 owns the marked-period and
actual-versus-standard comparison.  No source supplies a twist.

Owner ids:

    DEN-EF-ACTUAL-PACKET-CONT-TWIST-P
    DEN-EF-ACTUAL-PACKET-TWISTED-GLOB-QC-P

### 2.3 Exact inherited byte locks

- Paper 9 manuscript: 24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb
- Paper 9 PDF: c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02
- Paper 11 integrated proof audit: 03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28
- Paper 11 final manuscript: eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002
- Paper 11 PDF: 15d207568a61590852697511df2faf4cb06fd06047574c3dc3413e352c14840d
- Paper 12 integrated proof audit: c2b0fc4ce4764b476de8623c7a1b37e33d51da4a1c318c133313956abf4af6ab
- Paper 12 final manuscript: c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163
- Paper 12 PDF: 3fda5ae01fd3b7a78ddbefb11a62befa4d2ab50906b112b39e3c48e89901a294
- Paper 12 citation audit: f599dfbf67026b0985ee0e09b4e41bb24e3fe94709a1cd5e03ba657fb2a4fcaf
- Paper 12 peer review: e1f1558e170831457685a4a5c8c4d77f061b405d6c499867b6ce4f91bea6dc2b
- Paper 12 release audit: 53403b3ea8c44f30b6941653e2809432ad0e6b99f5cf983f0d929aa9d5c2760d

These are premise locks, not citation substitutes and not permission to
copy conclusions across owners.

## 3. Cochain, normalization, and gauge conventions

The coefficient group is

    T = {z in C : |z|=1}

with multiplication, the usual Hausdorff topology, and the trivial
G-action.

A normalized continuous one-cochain is a globally continuous map

    a : G_actual -> T,       a(x,0)=1.

A normalized continuous two-cochain is a globally continuous map

    sigma : G_actual^(2) -> T,

with sigma(x;t,0)=sigma(x;0,u)=1.  It is a multiplier precisely when

    sigma(x;t,u) sigma(x;t+u,v)
      = sigma(x.t;u,v) sigma(x;t,u+v).

The normalized coboundary convention is

    (delta a)(x;t,u)
      = a(x,t) a(x.t,u) overline{a(x,t+u)}.

Two multipliers are gauge equivalent when their quotient is delta a for a
normalized globally continuous one-cochain.  H^2_tw(G_actual;T) denotes
this author-defined normalized continuous gauge quotient.  It must not be
renamed as an unqualified standard topological-groupoid cohomology theory
until a same-domain source audit permits that name.

The one-object time multiplier convention is

    sigma(t,u) sigma(t+u,v)
      = sigma(u,v) sigma(t,u+v),
    (delta alpha)(t,u)
      = alpha(t) alpha(u) overline{alpha(t+u)}.

## 4. Twisted global-QC test algebra

Paper 11 supplies an author global-QC test algebra on the actual owner and
an exact time reduction to C_c(R).  For a normalized multiplier sigma, the
proposed twisted product on the frozen test domain is

    (f *_sigma g)(t)
      = integral_R f(u) g(t-u) sigma(u,t-u) du.

The proposed involution is

    f^{*sigma}(t)
      = overline{sigma(t,-t)} overline{f(-t)}.

The proof must establish closure in C_c(R), associativity, the involution
laws, support bounds, Fubini legitimacy, and compatibility with the actual
fibre formula.  These are author records:

    TW-GLOB-QC(sigma)
    TW-GLOB-QC-ACTUAL-PACKET-P(sigma).

They are not a standard groupoid C-star algebra on the actual
non-Hausdorff object.

If sigma=delta alpha, define the gauge map

    U_alpha f(t) = alpha(t) f(t).

The proposed equality

    U_alpha(f *_sigma g) = (U_alpha f) * (U_alpha g)

and the corresponding star identity are proof obligations, not frozen
facts.

## 5. Norm and completion boundary

No norm or completion is inherited from a standard actual-groupoid
framework.  Only after a proved gauge map may the paper define

    TW-FULL-TRANSPORT(sigma)
    TW-RED-TRANSPORT(sigma)

by transporting the full C*(R) norm and the left-regular norm through
U_alpha.  The proof must show:

1. existence of a continuous normalized alpha;
2. independence of the transported norm from the chosen alpha;
3. the exact unit-regular representation and sign convention;
4. full equals reduced only through amenability of the group R; and
5. no completion map is inferred from an actual-to-standard proxy.

If two trivializers differ, their quotient is required to be a continuous
character of R.  Character multiplication must be checked to act
isometrically on the transported full and reduced records.

## 6. Action and marked-period retention tests

The twist retains the action only if its gauge-class or completed
isomorphism invariant distinguishes at least two registered nonisomorphic
right-R actions on globally indiscrete carriers under the same typed
construction.

It retains a marked period only if a gauge-invariant restriction to
isotropy changes with the literal subgroup H_x and cannot be removed by an
allowed global gauge.  Merely evaluating a chosen representative on
H_x x H_x is not retention.

Mandatory controls include:

- trivial action;
- free translation action;
- transitive period-L action for arbitrary L>0;
- fixed-prime L=log p;
- composite-label and arbitrary-label period controls;
- a nontransitive action;
- a dense-stabilizer control where the registered topology permits it;
- coefficient targets that are not T0 as a factorization falsifier;
- measurable-only or discontinuous phases as excluded-domain controls.

The explicit quadratic family

    sigma_kappa(t,u)=exp(i kappa t u)

and proposed gauge

    alpha_kappa(t)=exp(-i kappa t^2/2)

must be checked with the frozen coboundary sign.  It is a control family,
not evidence that every multiplier has this form.

## 7. Claim targets

P13-1.  Every globally continuous normalized T-valued two-cochain on the
actual owner factors uniquely through the time-pair projection.

P13-2.  The multiplier equation and gauge relation reduce exactly to the
one-object continuous normalized multiplier complex of R.

P13-3.  Classify H^2_tw(R;T).  The candidate conclusion is zero: every
continuous normalized multiplier is a continuous normalized coboundary,
and two trivializers differ by a continuous character.  This conclusion
is unproved at Phase 1 and must survive an independent source/domain audit
and a direct proof.

P13-4.  Define and prove the twisted global-QC test algebra, including
product, involution, support, Fubini, and gauge-star isomorphism.

P13-5.  If P13-3 closes, define the transported full and reduced records,
prove choice independence, and prove their equality only from amenability
of R.

P13-6.  Prove the generic action-blind and period-blind conclusion under
the exact retention definitions.  Include trivial, free, periodic,
nontransitive, dense-period, and arbitrary-label controls.

P13-7.  Specialize to the actual fixed-prime packet without transporting a
standard topology or source theorem.  The candidate result is negative:
the scalar twist supplies no new invariant of (log p)Z.

P13-8.  Execute deterministic finite controls that are explicitly
witnesses and falsifiers, never proofs of the continuous classification.

P13-9.  Complete bounded primary-source and exact-package precedent audits.
Use only SUPPORTED_WITHIN_SEARCH if no exact precedent is found.

P13-10.  Evaluate every typed owner separately under Route A.  Route B is
false and cannot rescue a negative classical fit.

## 8. Direct proof obligations for the candidate H2 collapse

The proof must not cite the desired conclusion into existence.  At minimum
it must justify:

1. lifting a continuous circle multiplier on R^2 to a continuous real
   phase with a fixed base value;
2. why normalization lifts exactly rather than only modulo integers;
3. why the lifted cocycle defect is a constant integer and why it is zero;
4. why every resulting continuous real two-cocycle is a continuous
   coboundary in the frozen sign convention;
5. why exponentiation returns a normalized continuous circle trivializer;
6. uniqueness modulo continuous characters; and
7. why none of these steps sees X, the action, an orbit label, or H_x.

If a direct contracting argument cannot be completed, the candidate
conclusion remains open even if a nearby theorem is found.

## 9. Sharp falsifiers

Any one of the following blocks the corresponding claim:

- a globally continuous T-valued two-cochain on X_indisc x R^2 that is not
  time-only;
- a continuous normalized multiplier of R not continuously gauge trivial;
- a sign-correct multiplier for which the proposed twisted product is not
  associative;
- failure of the proposed involution or gauge-star identity;
- a gauge-independent norm that cannot be shown independent of the chosen
  trivializer;
- action or period retention that disappears under an allowed gauge;
- a fixed-prime claim using a standard proxy topology on the actual packet;
- any standard actual-groupoid C-star claim whose hypotheses fail;
- a finite control presented as proof of the universal theorem;
- an exact same-domain, same-package precedent that invalidates the bounded
  novelty or standalone narrative.

## 10. Source and novelty protocol

Phase 2 must separately audit:

- definitions of normalized continuous multipliers and gauge equivalence;
- classification of continuous multipliers on the one-dimensional vector
  group R;
- twisted convolution, involution, projective regular representation, and
  twisted group C-star completion on the Hausdorff group R;
- amenability and full/reduced equality for R;
- the applicability failure of standard groupoid frameworks on the actual
  non-Hausdorff owner;
- Deninger and companion owner facts already bound above; and
- an exact conjunction search for the rational-Witt actual packet,
  globally indiscrete arrow topology, continuous circle multiplier
  classification, author global-QC twist, gauge collapse, and marked-period
  nonretention.

Sources may own definitions and applicable group-R theorems.  They do not
own the Paper-13 actual-object factorization, typed transfer, or
fixed-prime negative conclusion unless they explicitly study that object.

## 11. Deterministic-control freeze boundary

Before implementation, a versioned amendment must freeze exact schemas,
row formulas, and expected counts for these ten output CSVs:

1. nerve_factorization_controls.csv
2. circle_multiplier_cocycle_controls.csv
3. lift_integer_defect_controls.csv
4. gauge_coboundary_controls.csv
5. twisted_convolution_controls.csv
6. twisted_involution_controls.csv
7. completion_gauge_controls.csv
8. action_period_nonretention_controls.csv
9. negative_domain_controls.csv
10. target_summary.csv

The package must use deterministic standard-library code, strict
verify-only mode, two fresh generations, byte identity, tamper/extra/missing
and lock/gate/implementation/manifest fail-closed tests, an explicit
recursive-entry guard, and no cache residue.  No proof hash may be bound
until the proof is stable; the controls manifest should instead bind the
active design/source gates and its own implementation/artifacts.

## 12. Nonredundancy and standalone gate

Paper 11 owns the untwisted global-QC collapse and author transported
C*(R) records.  Paper 12 owns marked degree-one cohomology and orbitwise
standardization.  Paper 13 must add all of the following to qualify as a
standalone manuscript:

- a direct, exact, normalized continuous H2 classification;
- a fully typed twisted test algebra and involution;
- gauge-star isomorphism and choice-independent transported completions;
- a precise action/period retention theorem with adversarial controls;
- a fixed-prime same-owner application;
- a bounded exact-package novelty audit; and
- independent proof, controls, standalone, citation, peer, and release
  reviews.

If the result is only the formal composition of Paper-12 factorization with
a standard H2(R;T)=0 fact, or only a quadratic example, the disposition is
NOTE_OR_MERGE.  The status STANDALONE_PASS is withheld until an independent
post-proof reviewer closes this gate.

## 13. Route ceiling

The generic factorization and gauge-collapse owners are expected to have
A0_FAIL and no positive A1-A4 coordinate.  A fixed-prime actual owner may
retain source-origin arithmetic relevance only on its own object; generic
or quadratic controls cannot donate that credit.  Gauge equivalence to
untwisted C*(R) supplies no determinant, primitive-orbit amplitude, analytic
continuation, Weil compression, or natural quantization.  A2, A3, and A4
are expected to fail for every registered owner.  These are priors, not
prejudged Route records.

No Stage-13 Route YAML or Route audit may exist before final proof,
controls, source, peer, and integrated gates.  Later Route provenance must
use the acyclic pattern:

    upstream stable tuple -> Stage-13 YAMLs -> route_audit -> composition.

No YAML or Route audit may embed its own hash.

## 14. Release boundary

No Git or public sync occurs during Papers 9-13 construction.  All retained
research-source PDFs are local verification bytes and must be absent from
every public index, staged delta, tree, archive, attachment list, and fresh
clone.  Human authorship, institution, correspondence, CRediT, funding,
conflicts, acknowledgments, venue, AI policy, repository, archive, licence,
DOI, and release authorization remain AUTHOR TO CONFIRM.
