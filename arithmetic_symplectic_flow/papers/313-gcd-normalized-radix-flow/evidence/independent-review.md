# Internal three-checkpoint review — gcd-normalized radix flow

Candidate: `ANG-20260920-GNR01`.
Paper: `313-gcd-normalized-radix-flow`.
Status reviewed: `OWNED NORMALIZED-RADIX CLOCK; COMPOSITE AND MULTIPLE PRIME FIXED PACKETS — STOP / FORK`.
Verdict: the bounded mathematical claims and stop decision are supported;
no manuscript correction requested. Venue calibration: `NOT_CALIBRATED`.
This is inherited-model, shared-context internal scrutiny, not external
peer review, cross-model verification or evidence of independent errors.

## 1. Inputs, method and actual access order

The research inputs actually read were:

| Input | Read scope | Measured SHA-256 |
| --- | --- | --- |
| [Frozen card](../candidate-card.md) | Original complete 178 lines, before any manuscript access | `f1df9cb172c404e0f27bfacd1fe8f81baeba545de35104c71217af1ea30a8656` |
| [Manuscript](../paper.md) | Complete 382 lines, after the complete raw submission | `c234026d5cdd6eb0ede28e514b8f398119f898864460c106360ce0cc4d9ac646` |

The card was still exactly 178 lines when first read and hashed.
After the author's administrative append, `head -n 178 ... | sha256sum`
verified the same frozen prefix. The appended outcome was not read or
used as original evidence. The manuscript hash was measured before the
full read and checked again afterward. No alternative draft was reviewed.

The applicable ARS skill, deep-research workflow, DA role, runtime policy,
logical-fallacies reference, failure paths, quality definitions and
argumentation reference were read before the raw-card audit. The method
was the requested bounded three-checkpoint mathematical DA process, not a
full editorial panel or literature review. No issue quota was imposed.

Actual sequence:

1. **Checkpoint 1:** read and hash only the original card; derive the
   main owner, complete fixed census and all three controls locally.
   Send the decisive fixed-packet finding, then the complete owner and
   controls findings to the author before manuscript access.
2. **Checkpoint 2:** after explicit author permission and the paper hash,
   read all 382 manuscript lines and compare every proof with the raw
   findings. Separately verify the manuscript's additional origin-basin
   formula (13); it was not a theorem previously submitted in this raw review.
3. **Checkpoint 3:** challenge the primitive/repetition interpretation,
   full-tail nonmerging, null-point clock, changed-control ownership and
   inference scope. No unresolved mathematical or scope correction resulted.

One existing same-model auxiliary, `atomic_clock_scope`, was assigned only
the original card and its three frozen controls. It tool-verified the
178-line hash and acknowledged that read. It was instructed to withhold
all mathematics until this reviewer's own complete raw submission; the
release was sent only after that submission. Its single mathematical
reply arrived after this reviewer's full manuscript read and initial
report write, but before final hashing. Its exact three-control results
were then compared with the already-submitted local raw calculations and
agreed, including the zero-layer phase `h-log a`. This is a bounded
controls cross-check, not a second main-proof or manuscript review.
It read no manuscript, scout, peer result or historical proof, and used
no write, numerical script, external source or further delegation.

Separately, the author disclosed a manuscript-informed control/basin
check by `/root/gnr_control_basin_check`: original card lines 1–178 and
paper section 5, with the next heading incidentally visible. This
reviewer did not read that agent's answer or use it as proof evidence.
The author reported that its initial direction wording was corrected:
predecessor-to-core has `c=-log D_r`, the inverse has `+log D_r`.
That error was not in the reviewed manuscript and required no paper edit.

The author reports that the bound manuscript was completed before receipt
of the complete raw submission and was not amended using these findings.
This does not establish author blindness or independent error mechanisms:
the agents inherit extensive common history and the same model/runtime.
No scout, prior paper or historical proof was read for this review.
The main raw derivation and own controls were completed before any
auxiliary mathematical answer became visible. No external search,
scientific program, numerical census or model override was used.

## 2. Checkpoint 1 — main owner and clock

Write the source digit as `q=d*k`, with `a=C*d` and `b=B/d`.
The exact inverse at `(B,C,s)` is

    I_(d,k)(B,C,s)=(C*d,B/d,(s+k)/C),
    d|B, 0<=k<C, gcd(C,k)=1, 0<=s<1/d.

Indeed `floor(d*(s+k))=d*k` on precisely that interval, and
`gcd(C*d,d*k)=d`. Conversely every actual source gives these parameters.
Different d give different first roots and different k give different
seeds, so the list counts actual predecessors without duplicate labels.
The convention `gcd(1,0)=1` is essential and was retained.

Taking d=1 and k=0 for C=1, or k=1 for C>1, proves
surjectivity. The predecessor count is exactly
`phi(C)*#{d|B: s<1/d}`, with `phi(1)=1`. It is finite
also at s=0. Product `a*b` is invariant on the entire carrier.
Neither fact licenses restriction to a chosen product component.

The source is total and Borel but not ordinarily continuous: at roots
(2,1), crossing x=1/2 changes the output roots. Countable actual finite
branch pairs cover the retained-lag groupoid. Equality sets of Borel
iterates give its Borel arrow set; its fibres are countable. No étale
or local-homeomorphism conclusion follows from these facts.

For every Borel E in an inverse domain, affine substitution gives
`mu(I E)=mu(E)/C`, not merely an interval-mass ratio. Thus the frozen
all-point derivative version is `J_I=1/C`, and `kappa=log e`.
On an arrow `(z,m-n,w)` the exact density and cocycle are

    J=D_n(w)/D_m(z),
    c=log D_m(z)-log D_n(w),   D_m=product_(i<m)e(T^i z).

Two presentations with the same lag differ by a common number of
forward steps. Their extra factors are evaluated on the same future
and cancel, including at zero seeds and cuts. Aligning the middle
histories also proves composition. These are pointwise arguments, not
an unproved extension of an almost-everywhere identity to null cycles.

The all-point version is nevertheless a frozen affine-derivative
prescription; the Radon–Nikodym law alone is only almost-everywhere unique.
The nonatomic measure does not assign an atomic Jacobian to a fixed point.
With arrows `(w,h)->(z,h+c)`, the actual forward step subtracts
kappa. All real translations exist on the whole extension. The quotient
time action is asserted set-theoretically, not as a Hausdorff suspension.

## 3. Checkpoint 1 — complete fixed census and packets

The root equations require `a=b*d`, `e=b`; the real equation is
`(b-1)*x=k`, together with `gcd(b,k)=1` and `0<=x<1/d`.
These conditions are necessary and sufficient, including the original
floor cell. They give exactly:

* `(a,1,x)`, for every a>=1 and `0<=x<1/a`;
* `(b*d,b,k/(b-1))`, with b>=3, d,k>=1,
  `gcd(b,k)=1` and `d*k<b-1`.

The strict inequality cannot be replaced by equality: the upper point
belongs to the next floor cell. There is no positive b=2 fixed case.
The unit-root intervals have source isotropy Z, time image {0} and
extension fixed-object isotropy Z. Their recurrence has not disappeared.
For every positive fixed core the corresponding groups are Z,
`(log b)Z`, and {0}; the least positive time is exactly log b.

Two fixed states can be tail-equivalent only if they are identical.
For a fixed core u its full source class is
`B_u=union_r (T^r)^(-1){u}`. All these predecessors remain.
If `T^r z=u`, its core-height phase is

    h - sum_(i<r)kappa(T^i z)  modulo H_u.

Different choices of r differ by a core return and give the same
phase. Consequently each full basin's time packet is, set-theoretically,
`R/H_u`; neither adding predecessors nor translating height merges
distinct cores. Source isotropy and H at eventual fixed states agree
with the core after finite-prefix cancellation.

In particular `(4,4,1/3)` is an actual fixed state with least time
log 4. The number log 4 equals twice log 2 arithmetically, but
the object's H contains no log 2. It is not a repeated traversal
of a smaller packet. This already stops promotion of the target.
The three cores `(5,5,k/4)`, k=1,2,3, and the two additional
cores `(10,5,1/4)`, `(15,5,1/4)` also establish distinct same-time
prime packets. The manuscript's fixed count
`sum_(1<=k<=b-2,gcd(b,k)=1) floor((b-2)/k)` follows directly.
It is not a total count including higher source cycles.

The positive witnesses lie inside their actual cells, not on ambiguous
cuts. They are still measure-null points: their inclusion and the
affine all-point clock are part of the full frozen owner.
No further fixed-root staying classification was needed for nonmerging,
and no higher-period census was performed after this decisive gate.

## 4. Checkpoint 1 — separately owned controls

**GEOMETRY-OFF.** Its inverse is `(C*d,B/d,s)`, with d|B,
coprime digit k and own domain `[k/C,k/C+1/(C*d))`.
Its full image consists exactly of targets satisfying
`gcd(C,floor(C*s))=1`: the inverse condition forces this, and d=1
is sufficient. Every inverse has J=1, hence the entire groupoid
has c=0 and every H is zero. Extension isotropy equals source
isotropy, rather than necessarily being trivial.
All fixed states are `(b*d,b,x)` in those same own intervals
with C=b. Each has source/extension Z and its distinct fixed
core class. No main normalized inverse domain was transplanted.

**CONTENT-OFF.** Its inverse is `(C,B,(s+q)/C)` for every
q=0,...,C-1 and all `0<=s<1`; no gcd filter is permitted.
It is onto, J=1/C and its own source kappa is log a.
All fixed states are the whole `(1,1,x)` interval, and
`(n,n,q/(n-1))`, n>=2, q=0,...,n-2. The former have
source/extension Z and H=0. Each latter core has source Z,
H=`(log n)Z`, extension isotropy {0}, and a distinct primitive
packet; all finite predecessors are included without merging cores.

**NORMALIZATION-OFF.** Its inverse is
`(C*d,B/d,(s+d*k)/(C*d))`, with d|B, coprime k and
the whole domain `0<=s<1`. It is onto, J=1/(C*d),
and its own source kappa is log a. Every zero-layer state
`(a,b,0)` reaches `(N,1,0)`, N=a*b, in one step.
Its source isotropy is Z, also for nonfixed initial factor pairs.
For N>1, H=`(log N)Z` and extension isotropy is {0};
for N=1 these are {0} and Z. Same-N zero states share
one packet; different N cannot merge because product is invariant.
At N=1 the full unit interval is fixed, and its different seeds
remain different zero-time cores. Other nonzero periodic fibres were
not classified in the raw review.

## 5. Checkpoint 2 — manuscript comparison and its additional basin proof

Every original-card definition and the above raw conclusion agrees with
the bound manuscript. Its signs, half-open boundaries, complete fixed
family and distinction between source, extension and time isotropy check.
The exact-image condition for GEOMETRY-OFF is implicit in its exhaustive
inverse domains; the paper does not assert that control is onto.

Formula (13), the FULL NORMALIZATION-OFF origin basin, was first
verified here at checkpoint 2, not submitted as a raw-card result.
For fixed product N, write `D_m=product_(i<m)a_i`. Since each
a_i divides N, `D_m|N^m`; repeated integer radix deletion gives
`x_m=fractional_part(D_m*x)`. Reaching zero therefore requires
`x in Z[1/N]`. Conversely

    a_i*a_(i+1)=N*d_i,
    D_(2m)=N^m * product_(j<m)d_(2j).

This clears every denominator dividing N^m by step 2m, after
which the next step reaches the fixed core. For N=1 the
intersection with [0,1) is only {0}, consistent with the other
unit seeds being separate fixed states. Formula (13) thus retains
all and only that core's predecessors; it is not a census of
the control's other periodic fibres. Prefix cancellation preserves H
and does not create a new primitive for each rational predecessor.

## 6. Checkpoint 3 — strongest counterarguments and limits

The strongest attempted rescue is to call log 4 a prime-power
repeat, or to merge equal-time fixed cores after adjoining predecessors.
Both fail by the actual isotropy and deterministic-tail calculations above.
Deleting the measure-null positive cores would change the frozen owner.
The negative gate is therefore substantive, not an absent-mechanism claim.

Conversely, this does not refute arithmetic feedback or geometric clocks:
the current gcd genuinely affects both roots and the remainder, and
the owned IMAGE clock is proved. The controls establish precisely their
own changed ledgers, not a universal arbitrary-predicate result or a
uniqueness theorem for the declared measure, radix convention or rule.
Stronger naturalness remains OPEN.

The missing positive b=2 fixed family does not exclude log 2
from every higher-period packet. Those packets remain unclassified.
No clock result is borrowed from a historical comparator; the directly
checked lineage is the current observable `gcd(a,q)=q iff q|a`
on 1<=q<a. Historical priority or source comparisons were not separately
audited. No classical symplectic, Hausdorff-circle, positive-roof, trace,
operator, zeta or formal Route claim is supplied by this review.

## 7. Disposition

No Critical, Major or Minor manuscript correction is requested; the
review does not manufacture objections to satisfy a quota. The same
full owner survives the audit, but its direct prime-time and one-per-prime
fixed-packet target is decisively **STOP / FORK**. Positive ownership
and control results are retained without promoting stronger naturalness.
T3 is not supplied/pursued; formal coordinates are UNASSIGNED and
Route B is NOT INVOKED. No old package or author-owned file was edited.
This report is the reviewer's sole written artifact for this round.
