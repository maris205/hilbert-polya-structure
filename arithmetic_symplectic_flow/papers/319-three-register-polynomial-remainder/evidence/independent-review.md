# Independent internal review — three-register polynomial remainder

Candidate: `ANG-20260920-PRF01`.
Package: `319-three-register-polynomial-remainder`.
Status: `OWNED POLYNOMIAL CLOCK; COMPOSITE FIXED PRIMITIVE — STOP / FORK`.
Review standing: `NOT_CALIBRATED`, internal inherited-model review.

## 1. Input locks, access order and limitations

The complete original card was read through its original EOF, 165 lines.
Its measured SHA-256 was

`8f7138b4f3478df3072c6fcf87f20620fcf72c7662505ec149fec042ed461d09`.

The first, released and reviewed manuscript is the same 366-line file,
with measured SHA-256

`86c27041705a952b7f344dbeea6f0d0d5117ca32a97eeca84300bd1382dae91c`.

Actual sequence was original-card reading; independent completion of the
entire main/control raw audit; a metadata-only `raw ready` message;
author-reported first-draft lock; explicit authorization to release the raw
findings; three complete raw messages and final commitment; explicit manuscript
unlock; measured manuscript hash and complete reading; synthesis and final
adverse checks; this report. No mathematical raw result was sent before
the author's draft-lock message. The author reports no subsequent change
to that manuscript from the raw results. The same bytes were actually
read only after the complete raw release and unlock.

No 319 scout, ledger, companion, appended outcome, peer answer, 318 source
record or other historical research material was read. No auxiliary agent
was delegated or consulted. There was no network call, scientific numerical
run, parameter change, higher-period search or other-file write.

The ARS router was reread in full for this round. The applicable
deep-research workflow, Devil's Advocate role, runtime policy and fallacy
reference had already been fully read in the continuing context. Their
three checkpoints and evidence-based severity discipline were applied; no issue
quota, model change or outside review was manufactured. The reviewer inherits
the current model/runtime and substantial programme history. The access isolation
above does not establish ideation blindness, cross-model validation, external
peer review, formal verification or independent error probabilities. No venue
calibration was supplied. Only this report is reviewer-written.

## 2. Checkpoint 1 — independently completed original-card results

### Full algebraic source, inverse and IMAGE

The Cardano expression is genuinely the inverse of `h(x)=x^3+x`.
If its two real cube-root terms are `p,r`, then `pr=-1/3`
and `p^3+r^3=a`, so their sum satisfies `h(p+r)=a`.
Since `h'=1+3x^2>0` and h is onto, the inverse is
unique and smooth with `sigma'=1/(1+3sigma^2)>0`. Positivity here
concerns the derivative/density, not sigma's value for every signed input.

Each integer cell has its own fixed q. Its unrestricted branch
map `(x,y,z)->(y,z,h(x)+z-q*y)` is a global smooth bijection.
Restriction to the actual half-open source cell gives exactly the card's
inverse and domain. Every signed cell and the explicit `B=0`
totalization remain. At integer states the third register is exactly
`N-qB=R`, including that declared totalization, rather than a label
standing in for the actual map.

For a target `(u,v,w)`, its source indices `B=floor(u)` and
`C=floor(v)` are forced. Enumerating every integer A, computing its
own q and retaining exactly

    A<=sigma(w-v+q_A*u)<A+1

enumerates all distinct predecessors. There is no independent cell-label
multiplicity or hidden index cutoff. In my raw notation, with
`alpha=u-B`, `beta=v-C`, `R_A=(h(A)+C) mod |B|`,
and `Delta_A=3A^2+3A+2`, the nonzero-B test is

    0<=w-beta-R_A+alpha*q_A<Delta_A.

If `B=0`, exactly one predecessor exists. If `B!=0` and
`alpha>0`, the nonzero cubic term dominates this quadratic window
in both tails, leaving only finitely many admissible A. At integer
`u=B!=0`, residue periodicity makes every nonempty predecessor fibre
countably infinite. The raw audit gave the full enumeration, the infinite
family over `(1,0,0)` and the missing target `(1,0,-1)`.
The manuscript's sharper explicit minimum-residue criterion is separately
verified in checkpoint 2, not retroactively attributed to the raw submission.

The actual forward determinant is `1+3x^2`, so the inverse
IMAGE density is its reciprocal, evaluated at the inverse source point.
Change of variables holds for every Borel subset of the actual
branch domain. In particular it is not a whole-cell volume ratio,
integer-divisor clock or branch count. The prescribed analytic formula gives
finite positive values at retained cuts; a.e. IMAGE alone does not
make arbitrary null values unique.

At the source, `kappa=log(1+3x^2)`. If `S_k` is its
actual k-step sum, a source-to-range branch pair has

    J(z,k-l,w)=exp(-S_k(z)+S_l(w)),
    c(z,k-l,w)=S_k(z)-S_l(w).

The actual forward arrow has lag `-1` and clock `-kappa`;
the inverse arrow has `+kappa`. Common future factors cancel under
longer presentations of the same triple; middle histories can be aligned
for composition. These are full-point statements about actual histories,
not arbitrary polynomial arrows or germs. The resulting owner and quotient
are Borel/set-level; no smooth, etale or invariant-volume-times-height claim
is obtained from the branchwise IMAGE law.

### Complete signed fixed set and full fixed packets

Full fixedness first forces `x=y=z=t`; this is a consequence,
not a selected diagonal carrier. For `a=floor(t)=0`, q is
zero and `h(t)=0`, so only origin occurs. If `a!=0`,
the actual signed rule gives `R=0,q=a^2+2`, whence

    t*(t^2-a^2-1)=0.

For `a>=1`, exactly `t=sqrt(a^2+1)` lies in `[a,a+1)`.
For `a<=-1`, the negative root is strictly below a and
the positive root is outside the negative cell. Thus ALL fixed
states are origin and `g_a=(t_a,t_a,t_a)` for integers `a>=1`.
The three frozen test cells contain exactly origin, `diag(sqrt2)`
and `diag(sqrt5)`. The same short equation exhausts all other
signed fixed cells without an additional census.

Origin's only predecessor is origin, by its `B=C=0` inverse.
Its full basin is a singleton, source isotropy `Z`, time image
zero, extension isotropy `Z`, and phase the full real height.

At each positive fixed core the clock generator is

    a_a=log(3*a^2+4)>0.

Its full source isotropy is `Z`, entire H is `a_a Z`,
and extension kernel is trivial. Hence the first core gives primitive
`log7`, and the second gives primitive `log16`. The latter
is not a fourfold traversal of a smaller loop in this packet:
`log2` is absent from its entire H. This fixed primitive
already violates the frozen prime-only target. A prime example elsewhere
does not erase the composite example.

For every fixed core, the full basin is all legal finite inverse
chains from the exhaustive enumeration, with every index and depth retained.
Each basin is countable, but no finite cardinality or simple finite
list was claimed. It is exactly the core's full tail class;
different fixed futures cannot merge. With first entry depth `d_z`,
kappa prefix `S_z` and core clock a, all integer lags occur and

    c(z,ell,w)=S_z-S_w+(ell-d_z+d_w)*a.

Consequently every basin state has source isotropy `Z` and the same
H/kernel as its core. Phase is `h-S_z` modulo a for
positive a. Multiple predecessors cannot create a smaller clock generator
or identify distinct fixed cores. The countable/null nature of these
basins does not permit deletion under the frozen all-point owner.

For any actual eventual least-period-P cycle, the conditional loop generator
is `L=sum log(1+3x_i^2)`, not generally an integer logarithm.
Its entire time group is `L Z`; the extension kernel is
trivial when `L>0` and `P Z` when `L=0`. A zero
sum forces all first registers to vanish, and cyclic register shifting
then forces the core to be origin. This does not construct or
classify other source periods; the fixed composite witness already stops
the target, and no higher-period search followed.

### All three independently audited controls

DIVISION-OFF has the unique global inverse
`(sigma(w-v),u,v)`, with its own reciprocal cubic-derivative IMAGE.
It is onto and bijective; its cell decomposition adds no branch
copies. Its only fixed point solves `h(t)=0`, hence is origin,
with singleton full basin and source/extension `Z`, H zero.
Any nonzero cycle, if present, would have positive loop clock by
its own register-shift argument. Higher periods were not classified.

POLYNOMIAL-OFF changes both real h and integer N. Its target
indices B,C are forced, its own q is computed from `A+C`,
and each candidate inverse is `(w-v+q_A*u,u,v)` with its
actual cell test. In raw notation that test is

    0<=w-beta-R_A+alpha*q_A<1,
    R_A=(A+C) mod |B|.

The raw proof established B=0 uniqueness, finite fibres when
`B!=0,alpha>0`, and the integer-u image criterion
`0<=w-beta<|B|` with countably infinite fibres when satisfied.
Its inverse determinant is exactly one. Thus kappa and the entire
groupoid cocycle vanish; every H is zero, while extension isotropy
retains whatever source isotropy occurs. Only origin is fixed: q is
zero in the zero cell and 2 in every nonzero diagonal cell.
Its inverse basin is a singleton. Other source cycles are unclassified.
The manuscript's further result that every noninteger-u target has a
predecessor is a manuscript-stage verification below, not a raw claim.

THIRD-NUMERATOR-OFF recomputes q from `h(A)` and removes z
from the real numerator. Its actual inverse is
`(sigma(w+q_A*u),u,v)` on its own cell-membership domain.
Its own inverse enumeration has test

    0<=w-R_A+alpha*q_A<Delta_A,
    R_A=h(A) mod |B|.

The same asymptotic/residue reasoning applied to this formula gives its
own image/multiplicity results, missing/infinite examples and unique origin
predecessor. The derivative's last diagonal entry changes to zero, but
its determinant remains `1+3x^2`; this is a direct calculation,
not a transfer of main branch domains or basins.

Its fixed equations give q zero at a=0 and `q=a^2+1`
otherwise, again forcing the same complete signed fixed set. The fixed
clocks therefore coincide in value, including its own primitive `log16`.
All incoming histories and phases use this control's inverse branches
and prefix sums. Equality of these fixed data does not establish
equivalence of the full main/control sources or basin membership.

## 3. Checkpoint 2 — complete manuscript comparison

All 366 lines were read after raw completion, raw release and unlock.
The measured manuscript agrees with the author's lock. Its source,
signed arithmetic, full-point density, clock direction, complete fixed equations,
basin formula and three controls agree with the independently submitted
raw results. No revision was requested or incorporated at this stage.

Three more explicit manuscript claims were checked directly:

1. In Section 2.2, for integer `u=B!=0`, the finite residue
   minimum really gives the exact image threshold
   `w-epsilon*gamma0>=r_min`. Necessity follows from the lower bound
   in (5). Sufficiency follows within a minimizing congruence class,
   where `Delta_A` tends to infinity. This includes negative B and
   the exact lower endpoint; the strict upper endpoint is met by
   sufficiently large absolute A. Every nonempty fibre is infinite.
2. The complete predecessor set over `(1,0,0)` is exactly
   `(A,1,0)`, not merely a subset: B=1,C=0 fixes
   `q_A=h(A)`, and `sigma(h(A))=A` for every integer A.
   The target-wise enumeration permits no other branch or source point.
3. In POLYNOMIAL-OFF, write `A+C=B*q+R`, `0<=R<m`.
   For manuscript `beta>0`, the full test is
   `0<=delta+q*beta<m`. Its half-open q interval has length
   `m/beta>1`, so contains at least one integer and only finitely
   many. The residue R and source A are then uniquely determined;
   Euclidean decomposition prevents duplicate predecessors. Thus the stronger
   positive existence assertion for every such target is correct, including
   signed B, rather than inferred from finiteness alone.

The phase formula was checked with the stated source/range orientation.
Integer multiples of the fixed-core clock absorb the entry-depth terms
modulo that clock; no sign switch or smaller primitive is introduced.
The core recurrence and complete basins, not only the displayed diagonal
points, support the composite-primitive conclusion.

## 4. Checkpoint 3 — strongest adverse checks and final disposition

The main counterargument would reinterpret `log16` as a repetition,
or hope that incoming identifications replace it by a smaller primitive.
The full isotropy calculation rules this out: every fixed-basin loop
has integer lag and an integer multiple of its own core clock.
Additional source periods could add other packets, but cannot remove or
merge this established fixed packet. No higher-period classification is needed
to reach this specific stop.

Other scope checks were also satisfied:

- A.e. volume ownership does not force arbitrary clock values at null
  periodic points. The result uses the frozen analytic all-point version
  and retains all axes, cuts and incoming states.
- The B=0 convention is a declared totalization, not ordinary division.
  It has been verified rather than silently omitted from the fixed proof.
- Three preselected cells do not by sampling imply the global fixed
  theorem; the same exhaustive signed equation supplies that theorem.
- The loop product away from fixed cores is generally real-valued;
  no unproved integer clock or prime selection is inferred for all cycles.
- The third-numerator control retains the wrong-time family, but this
  does not prove full-source equivalence or general irrelevance of that
  numerator term. The other controls have separate inverse/image owners.
- Arithmetic participation and an owned clock do not prove canonical
  naturalness, a conservative lift or a formal Route condition. The
  paper leaves those limitations explicit.

Final standing: no unresolved blocking or nonblocking manuscript correction.
Retain `STOP / FORK` because a genuine fixed packet has least
positive time `log16`, not because no prime example exists or all
higher cycles have been excluded. The same-object ledger is intact.
All fixed results and specified controls are established within this
declared source; higher source-cycle classification and stronger naturalness remain
OPEN / UNCLASSIFIED. No new candidate, numerical campaign or source change
is supplied by this report.

T3 is not supplied/pursued; classical A0/A1/A2 are not applicable;
formal Route coordinates are unassigned and Route B is not invoked.
No embedded-circle, Hausdorff quotient, invariant product measure, symplectic,
operator, trace, zeta, RH or Hilbert--Polya result follows. This is
internal model review, not external peer review or an independent-error
certificate. Companion/registry links and appended administrative records were
outside this access scope and remain the author's integration QA.
