# Independent internal review — central-carry flow

Candidate: `ANG-20260920-CCF01`.
Package: `317-noncommutative-central-carry-flow`.
Reviewed status: `OWNED CENTRAL-CARRY CLOCK; PRIME TIMES EXCLUDED — STOP / FORK`.
Review calibration: `NOT_CALIBRATED`.

## 1. Inputs, access order and review ownership

The original frozen input was the complete first 197 lines of
`candidate-card.md`, measured SHA-256:

`301ff3423c91673e6baae9e2287579059465b7b46eaee5e2a97a0cd7c5af1054`.

The only manuscript read was the complete 431-line `paper.md`,
measured SHA-256:

`baa3ad2bdae85533156952561bc9b590b3c5b9e9a26166c89063e0c87a3eb4dd`.

Actual access order was: original card in full; independent main
derivation and first raw message; complete inverse/basin and three-control
raw messages; explicit completion of checkpoint 1; author's manuscript
unlock; measured manuscript hash and full reading; checkpoints 2 and 3.
The original 197-line prefix was rechecked without reading any appended
outcome. No other 317 research file, scout, companion record or peer
answer was read. There was no auxiliary reviewer or delegation.

The author reports that this complete manuscript was written and locked
before receiving my first raw result and was unchanged at release.
That chronology is author-reported, not a second manuscript I inspected.
No raw-influenced manuscript revision or reviewer-requested revision occurred
in this review. Agreement does not establish independent error probabilities.

The ARS original-card, synthesis and final-adverse checkpoints were used
within the requested bounded contract. This reviewer inherited extensive
programme history and the same model/runtime context. The raw calculation
preceded access to this manuscript, but neither ideation blindness,
cross-model validation, external peer review nor formal verification is claimed.
No venue-specific calibration was supplied. No scientific numerical run,
external lookup, high-period census or old-owner theorem transfer was used.
This report is the reviewer's only write path.

## 2. Checkpoint 1 — independent raw-card findings

### Complete source, actual inverses and clock

Direct expansion verifies the stated associative multiplication, its inverse
and the dilation automorphism. Signed floors give the unique half-open
factorization `g=gamma*f`; the central borrow gives exactly
`gamma=d*delta_m(eta)`. In particular the pre-feedback point is

    (a+r/m, b+s/m, c+t/m^2+a*s/m).

This is the actual current-cell quotient, not a carried symbolic label.
The divisor observable `j1=0 iff m divides A` holds on the full
specified cells. It does not select admissible states or supply a clock.
The multiplication, dilation weights, feedback and measure remain design
choices; this interface alone does not establish stronger naturalness.

Undoing the three actual factors gives the card's `theta_gamma`.
Its exact domain is the inverse's membership in its original cell.
These branches exhaust all predecessors, with different cell indices
giving distinct actual preimages. All target objects remain, including
those outside the union image; no ambient group arrows are added.

My raw target enumeration used `p=F_inverse(w)` in its own cell,

    p=(a+xi,b+eta,c+zeta+a*eta),  xi,eta,zeta in [0,1).

A candidate scale must satisfy `m*xi<1`, `m*eta<1`,
`m^2*zeta<1`. At `m=1`, the central integer is zero.
At `m>=2`, use `C=+(m-1)` or `-(m-1)`, all
`j1,j2=0,...,m-1`, and retain precisely

    j3=C-j1*m*b-m^2*c in {0,...,m^2-1}.

This is an exact untruncated countable enumeration. A noninteger target
has a bounded scale. Origin has infinitely many immediate predecessors
`(j1,j2,m-1)` for all allowed scales and horizontal digits.
The raw nonimage test used `p=(3/4,0,2)`; the manuscript's
different, simpler nonimage test is checked in checkpoint 2 below.
The map is total Borel, countable-to-one, nononto and not globally
finite-to-one. A raw cut example also showed noncontinuity; this example
was not added to, or needed as a new assertion in, the manuscript.

The actual inverse is a composition of determinant-one left translation,
determinant-one `F_inverse`, and dilation with determinant `m^4`.
Thus its IMAGE identity holds on every Borel subset of its actual
domain, with `J=m^4` and `kappa=-4 log m`. This is not
only a whole-cell mass ratio. The frozen analytic branch formula
specifies values at null cuts; the a.e. measure identity alone does not.

For a source-to-range branch pair, the IMAGE ratio is the range
inverse-history factor divided by the source inverse-history factor.
Consequently the card's cocycle has the displayed sign; an actual
forward arrow has lag `-1` and time `+4 log m`.
Common future extensions cancel pointwise, and synchronized histories prove
composition on actual arrows. No extra lag multiplicities or free words
are introduced. The full object is Borel/set-level, not asserted etale.

### All main fixed points and the decisive whole-clock gate

My independent raw proof eliminated coordinates in each nonunit branch.
The inverse fixed equations are

    y=j2+m*x,
    z=j3+m^2*y+j1*m*x,
    x=j1+m*(z-x*y).

They imply

    m^2*x^2-H*x-D=0,
    H=m^4+j1*m^2-m*j2-1,
    D=m*j3+m^3*j2+j1.

The positive root is too large for the actual central cell
`C=+/- (m-1)`. A nonzero negative root lies in `(-1,0)`;
self-consistency then forces `A=B=-1`, `j1=j2=m-1` and
ultimately `m=2,C=-1,j3=1`. Its remaining candidate has
`r=x+1=(25-sqrt465)/8` in `(1/4,1/2)`, making its actual
central quantity `r*(2*r-1/2)` positive, contrary to `C=-1`.
The zero root belongs only to the unit case. At `m=1`,
fixedness is fixedness of `F`, hence only origin. This establishes
the full main fixed locus, including negative cells and cuts.

Every actual finite predecessor is retained in the origin basin.
The inverse maps integer targets to integer sources, so this basin
is contained in `Z^3`, but no claim that every integer enters
origin was made. Its source isotropy is `Z`, entire time image
is zero, and extension isotropy is `Z`; transient clock sums
do not create a positive primitive at the zero-clock core.

For any actual least source cycle of length `q`, put
`N=product m_i`. Its loop clock is `-4 log N`, so

    source isotropy = q Z;
    N=1: H={0}, extension kernel=q Z;
    N>=2: H=(4 log N) Z, extension kernel={0}.

Entry prefixes cancel. A non-eventually-periodic state has no nontrivial
source isotropy or time stabilizer. Thus any positive primitive of
the full main owner would have least time `log(N^4)`, never
`log p` for a prime. Repetitions are multiples of that same
least time, not new packets. This is the decisive stop gate.
It neither constructs nor rules out positive higher-period main cycles;
their existence and census remain OPEN / UNCLASSIFIED.

### Three independently derived changed-source controls

COMMUTATOR-OFF uses ordinary cubes and the inverse
`d+delta_m(F_inverse(w))`, with its own cube-domain tests.
In the coordinates `p=(U,V,W)=F_inverse(w)`, its total image is

    {0<=W<1}
      union {-1<=W<-3/4, frac(U)<1/2, frac(V)<1/2}.

Equivalently, its exhaustive scale/digit enumeration has central quotient
`c=0` or `-1`, with the required fractional tests retained.
It has its own determinant `m^4`, not a borrowed central-cell law.
All fixed points are origin and

    z*=(-1+r,-1+2r,-1+8r),
    r=(21-sqrt409)/8 in (0,1/8).

The raw coordinate elimination excludes the positive branch, and the
negative branch forces the ordinary cell `A=B=C=-1`, `m=2`,
digits `(1,1,3)` and `4r^2-21r+2=0`. Origin has zero time;
`z*` has source `Z`, time `log16 Z`, and trivial extension
kernel. Its entire fixed basin is one genuine positive packet.
No higher source-cycle classification was claimed.

FEEDBACK-OFF retains the noncommutative cells but has inverse
`d*delta_m(w)` on its own exact domain. The main target enumeration
applies with the target itself, rather than `F_inverse(w)`, because
this control's cell tests give that formula directly. Its own
Jacobian is `m^4`. Its complete fixed set is the entire
region `C(g)=0`, plus exactly

    (0,0,-1), (-1,0,-1), (0,-1,-1).

For nonunit fixed points, the horizontal integer/fraction equations force
`x,y` to be `0` or `-1`. The central range and its
actual residue then force `m=2,C=-1` and the three listed
possibilities. Every point in the full unit region is a different
zero-clock fixed core with source/extension `Z`. The three other cores
give three distinct `log16` packets with trivial extension kernel.
Their full inverse basins are not merged by equal clock values.

UNIT-DILATION is `F` on all of `R^3`, not a selected
unit-cell subsystem. Its global inverse has determinant one, so its
cocycle and all time groups vanish. Its only fixed point is
origin, with no additional inverse-basin points. Source isotropy outside
that fixed basin is not fully classified; extension isotropy equals
whatever source isotropy occurs. Zero time does not erase recurrence.

For the first two controls, and for the main fixed basin,
all actual finite inverse chains are included. If `d_z` is first
entry depth, `S_z` its own kappa prefix and `a` the core
kappa, the full basin arrow formula is

    c(z,ell,w)=S_z-S_w+(ell-d_z+d_w)*a.

The complete height invariant is `h-S_z` modulo `a Z` when
`a!=0`, and the real value `h-S_z` when `a=0`.
Different fixed cores cannot merge, since their fixed futures differ.
The controls with nonunit dilation obey their own whole-clock law;
their positive examples are not existence evidence for the main owner.

## 3. Checkpoint 2 — full manuscript comparison

All 431 lines were read after the raw checkpoint was complete.
The measured manuscript matches the released hash; no other draft was
opened. The following proof details were specifically checked, rather than
inferred from agreement of final statements:

- Equations (5)–(7) give the complete cell-consistent target enumeration,
  including the singleton `S_1`, strict fractional bounds and all signs.
  The exact direct-predecessor set (8) agrees with the raw enumeration.
  The manuscript's target `(0,1,0)` is indeed outside the image:
  it requires `j3=C-m^2<0` at every allowed scale.
- Equations (9)–(10) have the correct Borel IMAGE direction and
  actual-forward lag/clock sign. Both pointwise presentation independence
  and branch-pair composition use legal common futures.
- The manuscript's four signed-`A` fixed-point cases are a different
  proof from my raw quadratic elimination. Each was verified directly.
  For `A<=-2`, its lower/upper bounds have positive gap at
  least `m-1-(m+1)/m^2`. For `A=-1`, `r>=1/(m+1)`
  puts the actual central quantity strictly in `(0,1/m^2)`.
  These exclude all negative cells without a numerical cutoff.
- The COMMUTATOR-OFF root and its half-open inequalities are exact;
  the rejected `t=0` branch is handled. FEEDBACK-OFF's integer/fraction
  equations also force the central fraction to zero, and (19)
  has precisely the stated three nonunit solutions.
- Formula (21) retains all lags and both signs, including transient
  prefixes. Its phase reduction and distinct-core nonmerging statements
  follow for the full fixed basins, not a selected section.
- Equations (11)–(13), the abstract and the conclusion consistently
  retain the conditional nature of the positive-period clock theorem.
  No control cycle is substituted for an unproved main cycle.

No mathematical or scope correction to this manuscript is requested.
The raw proof and manuscript proof are not presented as interchangeable
provenance: the signed-`A` argument and the particular nonimage witness
above were reviewed from the manuscript, not retroactively attributed to
my raw submission.

## 4. Checkpoint 3 — strongest adverse checks and final disposition

The strongest apparent counterarguments were tested against the full owner:

1. Extra lag presentations, finite incoming branches or repetitions cannot
   yield a smaller positive time: source isotropy is exactly the
   least-cycle subgroup and common prefixes cancel. The fourth-power
   obstruction concerns its entire clock image, not one selected loop.
2. Infinite incoming branches and null fixed states cannot be deleted.
   They remain in the inverse enumeration and all-point clock owner.
   Conversely their inclusion does not turn a transient clock sum into
   a new return at the origin. The full-point density is a
   frozen analytic version, not a uniqueness consequence of a.e. IMAGE.
3. Absence of positive fixed points does not prove absence of higher
   positive cycles. The paper explicitly leaves that existence question
   OPEN. The algebraic exclusion of prime least times is sufficient
   for this bounded target without resolving it.
4. The noncommutative borrow genuinely changes the fixed ledger relative
   to COMMUTATOR-OFF; the FEEDBACK-OFF and UNIT-DILATION sources also
   have their own clocks and basins. None supplies the main owner's
   missing prime packet or licenses cross-control packet identification.
5. Dividing times by four, changing the measure, selecting a prime
   subsystem or dropping cuts would change the contract. This scoped
   failure is not a universal impossibility theorem for central-carry
   sources, other dilation weights or other measures.

The local positive result is a complete owned Borel arithmetic source,
actual IMAGE cocycle, full main fixed-point theorem and exact specified
control results. The negative result is exclusion of prime primitive
times for this owner at every source period. Stronger naturalness and
positive higher-period existence remain OPEN; no complete higher-cycle
ledger, embedded phase circle, Hausdorff quotient, etale or classical
symplectic realization is supplied.

Final standing: **no blocking or nonblocking manuscript change requested**.
Retain `STOP / FORK` for the stated prime-time target. The same-object
ledger is intact; all controls remain separate. T3 is not supplied
or pursued, classical A0/A1/A2 are not applicable, formal Route coordinates
are unassigned and Route B is not invoked. This internal report
adds no publication, numerical, operator, zeta, trace or RH claim.

Only the original card prefix and the exact manuscript above were
bound here. Companion links, registries and administrative outcome records
were outside this read scope and remain the author's integration QA.
