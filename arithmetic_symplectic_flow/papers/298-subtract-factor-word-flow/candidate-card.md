# Frozen candidate — subtract-and-factor full word flow

Candidate ID: `ANG-20260920-SFW01`.
Paper ID: `298-subtract-factor-word-flow`. Date: 2026-09-20.
Version: 1. Initial status: `OPEN — FULL WORD OWNER, IMAGE CLOCK AND FIRST FIXED PACKETS`.

## 1. Exact carrier, arithmetic rule and all branches

Freeze X={2,3,...}^(N_0), with discrete integer alphabet and the FULL
product topology. All infinite words remain, including every composite
symbol, unbounded tail, repeated factor and nonperiodic word. Do not
replace the carrier by prime words, a finite alphabet or a recurrent set.

For d>=2 let fct(d) be the complete ascending factor word of d,
with atoms defined as integers covering 1 in the divisibility order,
and with every multiplicity retained. Set fct(1) to the empty word.
Its arithmetic existence and properties must be justified from integer
divisibility, not a supplied prime list. On the current first pair put

    q(a,b)=a if a=b; q(a,b)=abs(a-b) if a!=b,
    T(a,b,x_2,x_3,...)=fct(q(a,b)) concatenated with (x_2,x_3,...).

The equality convention q(a,a)=a is an explicit design. All q=1
empty outputs are retained; no symbol 1 is inserted in X. The
infinite remainder remains after removing the two input symbols.
This is an autonomous variable-length prefix rule, not a word graph
with an unspecified next edge, port priority or stopping completion.

For each a,b>=2 let w=fct(q(a,b)). The proposed restriction
T:C(a,b)->C(w) has inverse

    h_(a,b)(w concatenated with eta)=(a,b) concatenated with eta.

C(empty)=X. Verify these complete images and actual local inverses,
the full image of T, and the local-compactness boundary before using
a topological groupoid. Do not drop equal-input or empty-output charts.

## 2. Full measure, IMAGE prescription and actual time owner

The fixed source measure is the full product law

    nu(n)=1/[n(n-1)] for EVERY n>=2,
    mu=nu^(N_0).

Normalization, existence, full support and singleton masses are
obligations. These all-integer weights and the factor ordering are
declared designs, not established necessities. No prime-dependent
measure, invariant probability or local compactness is assumed.

Freeze the ENTIRE retained-lag tail groupoid

    G_T={(x,m-k,y):T^m x=T^k y, m,k>=0},
    source y, range x.

Topology uses all actual finite inverse-branch pairs on common open
terminal domains and every finite-cylinder refinement. Keep the lag;
do not add swaps, unrestricted prefix replacements, free word labels
or a germ quotient. Derive the Borel IMAGE law on all these charts.

For a single INVERSE branch h_(a,b), the proposed formula is

    J_h=nu(a)*nu(b)/product_(d in fct(q(a,b)))nu(d),
    empty product=1.

This formula is UNPROVED at freeze; it is not the forward derivative.
Only after deriving the full branch-pair IMAGE law set c=-log J
on actual arrows. Require presentation independence, additivity and
a continuous full-point version determined by full support, including
all null returning words. Do not choose a version only at fixed words.

The extension has objects X x R and arrows
(y,u)->(x,u+c(x,l,y)); physical time is u->u+t for ALL real t.
Prove complete jointly continuous time using this owner. No independent
roof, assigned log-prime length or borrowed symbolic clock is supplied.
Classical finite-dimensional symplectic/mapping-torus fields are NOT
APPLICABLE, even if a useful positive branch-clock bound is established.

## 3. Packet convention and decisive bounded first test

For every tested x use the COMPLETE H_x=c(G_x^x), not a chosen
return arrow. A primitive cyclic time packet requires H_x=T_x Z
with least T_x>0. Repeated traversals have times ell*T_x within
the SAME packet. Different fixed cores, identical lengths or equal
arithmetic products are not extra identifications. Packet equivalence
uses actual tail arrows and real-time translation. Keep source
isotropy, fixed-object extension isotropy and time groups separate.
No Hausdorff quotient or embedded-circle conclusion is presumed.

After full owner/measure/clock checks, classify the FIXED members
of x_(a,b)=(a,b,b,...) for all a,b>=2, including constant words
and the b=2a boundary. This is an exact fixed-core family audit,
not a commitment to classify every eventual or higher-period member
of that head/constant-tail family. For every fixed member compute
the entire lag/clock group and actual packet equivalence, including
whether excursions through finite preimages can identify two cores.

One composite primitive time, wrong prime clock or extra packet is
enough to STOP target promotion. Then finish only the following
precommitted controls, not a full mixed-word/returning-locus census,
parameter tuning, new measure fitting or T3 construction.

## 4. Separately owned controls

1. FACTORIZATION-OFF: on the SAME full X and measure mu, replace
   fct(q) by the one-symbol word (q) when q>=2 and by the empty
   word when q=1. Rebuild its own branch derivatives and tail-clock
   owner. Classify only its fixed head/constant-tail family and actual
   packet identities. Do not use the main clock on this changed map.
2. MEASURE-CHANGE: retain the main T and full carrier but use
   nu_0(n)=2^(1-n), mu_0=nu_0^(N_0). Prove normalization/support
   and its OWN IMAGE law; test the SAME main fixed-core family.
   Equal or integer-related times must not merge distinct packets.
3. Empty-output chart (2,3), equal-input chart (2,2), composite
   input symbols, and the b=2a family are arithmetic/ownership
   controls. All singleton-null states remain. Clock continuity on
   a full-support measure, not positive atom mass, must own them.

Keep source/q/factor-order/measure naturalness OPEN unless separately
established. Identify PROVES_TOO_MUCH only at the scope actually
proved; no arbitrary-data universality or general no-go is presumed.
No scientific numerical run, prime cutoff, precision parameter,
external literature campaign or target-zero comparison is planned.

## 5. Lineage, provenance and nontransfer boundary

The [prior-work](../../docs/prior_work/README.md) arrow is integer
divisibility/factor observables -> current-pair subtraction -> actual
variable-length factor rewriting -> the same full word source's
measured time action. This is a stated symbolic deformation, not a
Logistic/Henon conjugacy or positive-dimensional conservative lift.

The definition is the untested proposal in
[297's scout record](../297-real-feedback-scale-flow/evidence/scout-record.md),
SHA-256 `95355d5764b98b70df6251237b48207d91a974bf634e69314534c8e5acc6ba58`.
It changes the source mechanism, not 296's min/max parameter:
[296](../296-factor-compare-remove-flow/candidate-card.md) has cover-atom
words, comparison/removal and declared scale without a measure.
[225](../225-euclid-edge-scattering/candidate-card.md) uses finite-word
Euclid graph ports with a componentwise geometric action and unit roof;
[269](../269-factor-redistribution-lattice/candidate-card.md) uses a
product-preserving lattice update and spatial quotient. None supplies
this measured infinite-word rule's clock, packet theorem or Route credit.

## 6. Review, ownership and stop/fork handoff

T0-T2 are broadened owner labels only. T3 / analytic / Hilbert /
contact / Hamiltonian / quantum owners NOT SUPPLIED / NOT PURSUED.
Classical A0/A1/A2 NOT APPLICABLE; formal coordinates UNASSIGNED;
Route B NOT INVOKED. Even an owned measured clock is not natural A0.

Root owns integration and all files except the native reviewer's
evidence/independent-review.md. ARS raw-card, evidence-comparison
and final adverse checks are inherited-model/shared-context internal
research, not external peer review or independent-error evidence.
Old packages/mirrors unchanged; 241/242 paused; programme goal active.
Markdown only; no PDF/LaTeX, staging, commit, upload or publication.

## Appended audit outcome — 2026-09-20

Final status: `OWNED WORD IMAGE CLOCK; COMPOSITE FIXED-CORE TIMES — STOP / FORK`.

The original 156-line version-1 bytes above remain unchanged, SHA-256
`10b23181087e28469c7490e4dc3ae5cc018eb274ed4684a7482d3d0add762ecd`.
The [paper](paper.md) proves the full source, surjective local map,
normalized full-support nonatomic product measure and exact Borel
inverse IMAGE factors. Its continuous all-point clock owns all null
fixed words and the complete real action; each inverse branch clock
is at least log 2. No classical suspension is inferred.

The fixed members of (a,b,b,...) are exactly p^infinity and
(p,2p,2p,...), p prime. Each has full source lag Z, trivial
fixed-object extension isotropy and H=log[b(b-1)]Z. Different
fixed cores remain different actual packets. Constant 3 has least
primitive time log 6; (2,4,4,...) has least time log 12.
This decisively fails the ordinary-prime-time target.

FACTORIZATION-OFF has integer-indexed fixed families with its own
clock; constant 4 and (2,4,4,...) are different log-12 primitives.
MEASURE-CHANGE keeps the main fixed cores but gives least times
(b-1)log 2, without identifying different cores as repetitions.
Empty-output and composite-input chart identities remain branch
statements, not unproved return claims.

Portfolio: **stop target promotion / fork**. All source words,
measure, arrows and clocks remain intact. Other fixed words,
nonfixed family members and higher/eventual returns remain OPEN /
NOT PURSUED. Strong naturalness and coarse topology are not settled.
T0/scoped measured T1 and the tested T2 family established; target
FAIL. T3 NOT SUPPLIED / NOT PURSUED, classical A0/A1/A2 NOT
APPLICABLE, formal UNASSIGNED, B NOT INVOKED.

[Claims](claim-ledger.md), [evidence](evidence/README.md),
[review](evidence/independent-review.md) and
[provenance](evidence/scout-record.md) preserve limits. A separate
finite-quotient transport lane has no complete new transition, not
a no-go result. Old packages unchanged; 241/242 paused; goal active.
