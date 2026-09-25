# Divisor-gated product radix: an owned clock and square-time fixed packets

Paper ID: `308-divisor-product-radix-flow`.
Candidate ID: `ANG-20260920-DPR01`. Date: 2026-09-20.
Status: `OWNED PRODUCT-RADIX CLOCK; SQUARE-TIME FIXED PACKETS — STOP / FORK`.
Evidence class: exact ownership and complete fixed-root theorem;
negative direct-prime-time gate. Formal coordinates UNASSIGNED;
classical A0/A1/A2 NOT APPLICABLE; Route B NOT INVOKED.

## Abstract

On all positive-integer pairs with full real interval fibres,
the current product N=a*b sets a geometric radix. Real
position selects q=1+floor(N*x); precisely when q divides N,
the quotient changes the next roots and the affine remainder
changes the real position. We prove all inverse branches, the
partial Borel owner and its own IMAGE clock. Every n>=2
has exactly one fixed state (n,n,1/(n+1)), with least
positive time 2*log(n); the unit root retains a whole
zero-time fixed interval. These are also the entire fixed-root
staying sets. Distinct fixed cores cannot merge through full
tails. Already n=2 therefore supplies a primitive log(4)
packet, not a repetition of a shorter packet. Three changed
owners separately test radix transport, arithmetic feedback and digit
reflection. The first target gate decides STOP / FORK without
a higher-period census. Strong naturalness remains OPEN.

## 1. Identity, question and lineage

The original [card](candidate-card.md) is the sole frozen definition.
Its definition-only input is the [307 frontier record](../307-euclidean-cell-content-flow/evidence/scout-record.md);
hashes and exact access scopes are in [evidence](evidence/README.md).
No previous source, clock, return theorem or Route credit transfers.

| Item | Same-object owner | Scope |
| --- | --- | --- |
| Carrier/measure | Y=positive-integer pairs x [0,1], counting x Lebesgue | Full Borel carrier, including terminals |
| Source | Current product radix, divisor permission and quotient-root feedback | Exact formulas below |
| Coding | q=1+floor(a*b*x) from this real state | Not an independent shift |
| Clock | IMAGE derivative of actual inverse/branch pairs | Frozen affine all-point version |
| Time | Full retained-lag real extension, all Y x R | Complete Borel translation; set-level quotient |
| Packets | Full time orbits, actual isotropy and least positive generator | No equal-time or chosen-seed quotient |
| Classical geometry | Symplectic base/roof/mapping torus | NOT APPLICABLE |
| Analytic/quantum object | No operator, zeta, determinant or trace supplied | T3 NOT PURSUED |
| Controls | RADIX-OFF, ARITHMETIC-OFF, DIGIT-REFLECT | Each owns its changed branches and clock |

The [prior-work lineage](../../docs/prior_work/README.md) is used through
divisor-symbolic admissibility: d|n becomes q|a*b, with a*b=q*c.
An integer n can be inspected at root (n,1), but no
such slice is selected as Y. Integer roots set the
real partition; real position selects a factor; its quotient
changes the next partition. This is autonomous feedback, not
passive real scaling or a word-length factorization schedule.
It is not a proved Logistic/Henon conjugacy or conservative lift.

Question: does this full object own its clock and a compatible
primitive ledger at the first fixed-root gate? All roots and
seeds must remain during that test. Strong naturalness of the
product radix, offset digit, update and measure is OPEN. No
prime predicate, factor table, zero data, fitted parameter or roof
is used. A correct engineered arithmetic interface is not natural A0.

## 2. Complete partial source and inverse branches

At z=(a,b,x), set N=a*b and q=1+floor(N*x).
If q|N, put c=N/q and

    T(a,b,x)=(b,c,N*x-(q-1));

otherwise retain z as terminal. In particular x=1 has q=N+1
and is terminal; x=0 uses q=1. A cut k/N belongs
to q=k+1 and undergoes the same divisibility test. Unit
factors remain; N=1 has one, not two, unit branches.

For every q|N the exact source and image are

    U_(a,b,q)={(a,b)} x [(q-1)/N,q/N),
    V_(a,b,q)={(b,N/q)} x [0,1).

Indeed the affine output maps the stated half-open interval
bijectively onto [0,1). Conversely its inverse belongs to that
same digit interval. At a target (B,C,y), ALL predecessors
are indexed by A>=1 satisfying C|A*B, with

    q=A*B/C, I_A(B,C,y)=(A,B,(q-1+y)/(A*B)), 0<=y<1.

Here q is a positive divisor of A*B because C is
a positive integer; q<=A*B. Conversely any predecessor has first
root A, second root B and quotient C, forcing this q
and seed. Thus the enumeration is exhaustive, including every
overlap. Distinct A give distinct predecessor roots.

Every target with y<1 has a predecessor: choose A=C and
q=B. No y=1 target has one. Thus the FULL image
is all positive roots x [0,1), not Y. Some image
states are terminal: (2,2,1/2) has digit 3, not dividing
4, yet is the image of (2,2,3/8). These incoming
arrows remain; being terminal does not remove a state from G.

The domain is Borel, T is partial Borel and countable-to-one.
No ordinary-topology continuity is available across all digit cuts:
at root (1,2), x approaches 1/2 from below within
the domain, with output root (2,2); at x=1/2 the
output root is (2,1). Discrete roots prevent convergence.
We do not declare an etale or local-homeomorphism owner.

## 3. Same-measure IMAGE, full owner and time

### 3.1 Branches and all-point prescription

The affine inverse has derivative 1/(A*B). Counting-root density
is one on each fibre, so change of variables proves

    mu(I_A(E))=mu(E)/(A*B), EVERY Borel E subset V.

Thus its IMAGE J=1/N, and inverse-arrow clock is log N.
The branch source/image masses 1/N and 1 check this result
but are not the all-Borel proof. The derivative of the
actual forward branch is N. Frozen analytic affine continuation
assigns these same derivatives at retained endpoints/null states.
This is an explicit pointwise version, not a consequence of
a.e. Radon–Nikodym uniqueness, nor a derivative for terminal steps.

### 3.2 Actual retained-lag composition

Use G={(z,m-k,w):T^m z=T^k w} with every iterate
defined, T^0 everywhere, source w and range z. This is
a countable Borel groupoid: for each m,k the defined-iterate
sets and equalities are Borel; all finite fibres are countable;
the countable union keeps all actual triples and no extra histories.
Composition aligns the two finite histories at their common middle
state. If one history is longer, that already existing history
supplies the needed extension; no terminal step is invented.

Let D_m(z) be the product of the m actual positive
forward slopes N_i, with D_0=1. On the corresponding branch
pair from w to z, the affine IMAGE and clock are

    J(z,m-k,w)=D_k(w)/D_m(z),
    c_time(z,m-k,w)=log D_m(z)-log D_k(w).

For two presentations of one triple with the same lag,
the larger m,k adds the SAME actual future factors to
both products, so they cancel, including at retained boundaries.
Aligning histories similarly proves multiplicativity of J and additivity
of c_time. These constants agree with IMAGE on every Borel
restriction of each affine branch pair; null intersections do not
undo the declared pointwise version. This is not global T-invariance
of mu, and no free affine-group action has been introduced.

The full extension has object set Y x R and arrows
(w,h)->(z,h+c_time). Translation h->h+t is complete and jointly
Borel for all real t and commutes with arrows. We use
only its induced set-level quotient action. Coarse quotient topology,
locally compact realization and analytic trace objects are not claimed.

At each z, distinguish source isotropy, its time image H_z,
and the extension isotropy ker c_time. If H_z=L Z for
L>0, the time orbit has least positive period L. Its
repetitions r*L traverse that SAME packet. Full tails and time
translation determine packet identity, not equality of numerical clocks.

## 4. ALL fixed states and complete fixed-root staying fibres

### 4.1 Root equations and all real seeds

A full fixed state must satisfy a=b=c=n, hence N=n^2
and q=n. A single root-preserving step is therefore permitted
precisely on the full interval

    I_n=[(n-1)/n^2,1/n).

For n=1 this is [0,1), and the action is identity.
The endpoint 1 remains terminal. For n>=2 the real fixed
equation is (n^2-1)*x=n-1, with unique solution

    z_n=(n,n,x_n), x_n=1/(n+1).

It genuinely lies in the required digit interval:

    x_n-(n-1)/n^2=1/(n^2*(n+1))>0,
    1/n-x_n=1/(n*(n+1))>0.

Consequently these z_n and ALL (1,1,x), 0<=x<1,
are the COMPLETE fixed locus, with no selected prime restriction.

Now require the integer roots to remain unchanged for EVERY
forward iterate. This forces the same n,n and q=n
at every step, so the whole trajectory must stay in I_n.
For n>=2, writing f_n(x)=n^2*x-(n-1) gives

    f_n^k(x)-x_n=n^(2*k)*(x-x_n).

Since I_n is bounded, all these iterates can remain there
only when x=x_n. Conversely x_n stays. For n=1 the
entire [0,1) stays. Thus the fixed-root staying sets have
been classified from COMPLETE fibres, not presumed from fixed seeds.
This does not classify periods with changing integer roots.

### 4.2 Literal isotropy and no full-tail merger

Every fixed state has source isotropy the literal lag group Z.
At z_n, n>=2, one forward return has D_1=n^2;
the time image and extension kernel are therefore

    H_(z_n)=2*log(n) Z, ker c_time={0}.

The least positive time is 2*log(n), not log(n): every
source lag is an integer, and its clock is exactly that
integer times 2*log(n). At all unit fixed states H=0
and the extension isotropy is Z. Zero time is not absence
of source recurrence. Different unit seeds remain different fixed cores.

If two fixed states were tail-equivalent, equality of any
defined forward iterates would equal their constant tails, forcing
the states identical. Finite inverse excursions cannot help because
their composite is still an arrow of the actual full-tail owner.
Time translation cannot connect different source-tail classes. Thus
every z_n gives its own positive packet, with repeats r*2*log(n).
All finite predecessors of that core are retained, not extra
core packets; their clock-isotropy image is preserved by conjugation.

### 4.3 First decisive target obstruction

For EVERY n>=2 this fixed packet has exp(L_n)=n^2,
a composite integer. Already z_2=(2,2,1/3) has primitive
time log 4. Calling it a second traversal would require
a shorter positive time in its SAME full isotropy image;
none exists. A different packet at another root cannot supply
that missing half-lag. Deleting composite roots or rescaling time
would change the frozen owner or normalization, not repair this result.

Therefore the direct prime-time target fails at the complete
fixed-root gate. This is not a full main periodic census,
nor a theorem against all asymptotic clock comparisons or nonlinear
arithmetic carriers. Higher main periods are NOT PURSUED after
the precommitted stop; stronger naturalness remains OPEN.

## 5. Three controls with their own IMAGE and returns

### 5.1 RADIX-OFF

Keep the main domain and roots but real output x. At
target (B,C,y), each A with C|A*B has q=A*B/C
and inverse (A,B,y), ONLY on

    (q-1)/(A*B)<=y<q/(A*B).

These are its exact images, not the main [0,1) targets.
Every inverse IMAGE is 1 on Borel subsets, so the entire
cocycle and ALL H vanish. ALL fixed states, and also all
fixed-root staying states, are (n,n,x) with x in I_n,
including n=1. Their source and extension isotropy are Z,
and distinct fixed cores do not tail-merge. No broader source
period classification is claimed for this control.

### 5.2 ARITHMETIC-OFF

For x<1 use all q=1,...,N and map to (b,N,N*x-(q-1));
x=1 remains terminal. A target (B,C,y) has predecessors
only if B|C, with A=C/B, and then ALL q=1,...,C:

    (A,B,(q-1+y)/C), 0<=y<1.

These exact branches give inverse IMAGE 1/C and clock log C.
No original quotient-root domain is transferred. Along its root
recurrence (a,b)->(b,a*b), the root product P=a*b changes
to P*b>=P. A periodic root sequence forces EVERY b=1
and hence EVERY a=1. The only preimage root of (1,1)
is itself, so eventual periodic roots likewise must start at (1,1).
There the real map is identity on [0,1); the endpoint is terminal.

Thus ALL nontrivial source isotropy occurs exactly at (1,1,x<1),
where it and extension isotropy are Z. Everywhere else both
are zero; ALL H are zero. This global positive-packet absence
coexists with nonconstant branch clocks. It follows from actual
root dynamics, not a falsely asserted globally zero cocycle.

### 5.3 DIGIT-REFLECT

Keep q|N and quotient roots but real output q-N*x.
The exact inverse at target (B,C,y) is now

    (A,B,(q-y)/(A*B)), C|A*B, q=A*B/C, 0<y<=1.

Its IMAGE is 1/(A*B), by absolute affine derivative on
its OWN target. The full image includes y=1 but excludes
y=0; x=0 maps to a terminal endpoint. The branch clock
agrees in magnitude with the main one, not in future itinerary.

Fixed roots again require n,n and q=n. ALL full fixed
states have x'_n=n/(n^2+1), n>=1. For n>=2,

    x'_n-(n-1)/n^2=(n^2-n+1)/(n^2*(n^2+1))>0,
    1/n-x'_n=1/(n*(n^2+1))>0.

Deviation from x'_n multiplies by -n^2, so the ENTIRE
fixed-root staying set for n>=2 is that one seed. Its
source isotropy is Z, least time 2*log(n), extension zero.
These are separately owned square-time packets, not inherited main ones.

At n=1 the real action is 1-x on x<1. The
ENTIRE unit-root staying set is (0,1): zero reaches terminal
1, while 1 has no successor. The midpoint 1/2 is
fixed with source/extension Z; every other interior point has
least source period two and literal source/extension 2Z. ALL
these unit time groups are zero. No changing-root census follows.

## 6. Gate assessment, limitations and decision

| Gate | Result | Boundary |
| --- | --- | --- |
| T0 | Full partial Borel source, complete inverses and real extension established | No etale/coarse-topology or symplectic claim |
| T1 | Actual divisor/radix feedback owns its measured clock | Stronger arithmetic naturalness OPEN |
| T2 | ALL fixed states and entire fixed-root staying sets established; square-time primitives obstruct direct prime target | Higher main returns NOT PURSUED |
| T3 | NOT SUPPLIED / NOT PURSUED | No borrowed trace or operator |
| Classical/formal | A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED | No Route credit |

The controls distinguish real expansion, quotient feedback and orientation,
but do not force this particular radix, measure or endpoint version.
They do not establish arbitrary-data universality: no unconstructed
PROVES_TOO_MUCH theorem is asserted. All results are exact and
carry their stated domains; no finite numerical cutoff, precision
parameter, prime/zero dataset or external literature lemma is needed.

Portfolio: **stop direct prime-time promotion; retain the owned source
and fixed-root obstruction; fork a different architecture**. The same-object
ledger is intact. A future definition must receive its own card;
no result transfers merely because its formulas look similar.

## Evidence and AI-assisted review disclosure

See the [claim ledger](claim-ledger.md), [evidence and locks](evidence/README.md),
[internal review](evidence/independent-review.md), [source/frontier record](evidence/scout-record.md)
and [package index](README.md). The proofs above are the mathematical
evidence. ARS raw-card, synthesis and adverse checkpoints are native
inherited-model/shared-context AI-assisted scrutiny, not external peer review,
independent-error evidence or formal verification. No venue calibration.
Review provenance and any revisions are recorded with exact hashes.
Positive 304, old packages, mirrors and Phase-I material unchanged;
241/242 paused; goal active. Markdown only; no publication or upload.
