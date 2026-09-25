# Frozen candidate — divisibility-permitted LU-to-UL reassembly

Candidate ID: `ANG-20260920-LUR01`.
Paper ID: `336-divisibility-lu-reassembly`. Date: 2026-09-20.
Version:1. Initial status: `OPEN — REAL REASSEMBLY AND OWN IMAGE CLOCK`.

## 1. Full carrier, source permission and actual matrix update

Take Y=M2(R), M=[[x,y],[z,w]], usual topology/Borel structure and mu=Leb4.
Retain ALL real matrices, signs, zero entries, singular matrices, floor faces and
null fibres. No extra integer root, scale, atom, spectral/similarity quotient or
change of coordinates is substituted for this carrier or measure.

Read a=floor(x), c=floor(z). For x!=0 put ell=z/x, s=w-zy/x.
The exact legal source and action are

    D={x!=0, a!=0, a divides c, s!=0};
    L(M)=[[1,0],[z/x,1]], U(M)=[[x,y],[0,s]];
    T(M)=U(M)L(M)=[[x+yz/x,y],[sz/x,s]].

The DISPLAYED formula defines T; matrix-factorization terminology supplies no theorem.
The successor rereads its own pivot, lower-left entry, floors, permission and
factors. Old a,c,ell,s are not extra retained labels. The actual real
pivot is used in division and multiplication, not an integer label in
a fixed affine kick. All identities/invariants/periods remain to be audited.

Every M outside D remains terminal with T^0 and ALL actual incoming
histories, but no reset, absorbing self-loop, waiting time or infinity object.
In particular0<=x<1 has a=0 and is terminal; x=0 is never
divided; s=0 is never continued by a limit. a=+/-1,c=0,z=0,y=0,w=0
and all negative values follow ONLY the same rule. No det(M)!=0
restriction is imposed on the entire carrier and no conull carrier replaces it.

## 2. Every target inverse and its actual source tests

For arbitrary target N=[[xi,eta],[zeta,omega]], if omega=0 generate NO predecessor;
N remains an object with its OWN forward permission. For omega!=0 set

    lambda=zeta/omega; u=xi-eta lambda;
    I(N)=[[u,eta],[lambda u,omega+lambda eta]].

This SINGLE candidate is admitted iff u!=0, a*=floor(u)!=0, a* divides
floor(lambda u), I(N) belongs to its own D including Schur condition,
and T(I(N))=N. Source checks are not target-forward checks. No limiting
inverse, arbitrary matrix-group action or additional inverse-label cutoff is allowed.

For EVERY integer pair a,c with a!=0,a divides c specify

    U_(a,c)={M in D:a<=x<a+1,c<=z<c+1};
    V_(a,c)={N:omega!=0,a<=u<a+1,c<=lambda u<c+1,
                  I(N) in D,T(I(N))=N};
    I_(a,c)=I restricted to V_(a,c).

Prove both inverse identities, exact image, exhaustive candidate count, boundary assignment
and distinction of source/target permissions. The formulas are frozen specifications,
not already verified statements. Do not evaluate undefined lambda,u at omega=0.

## 3. Full-point native-volume IMAGE and retained-lag clock

On EACH actual V_(a,c), prescribe J_I(N)=abs det D_N I, using
the displayed rational inverse's same analytic four-real-variable derivative version. It
applies at EVERY admitted floor face, axis and null point. No determinant
value, sign, potential or return-time result is pre-supplied. Prove finite positivity,

    mu(I E)=integral_E J_I dmu

for EVERY Borel E in its own domain, plus inverse and all
legal finite-composition compatibility. Do not alter null/periodic values by a.e.
equivalence or extend J to undefined/illegal inverse points. No density or
atomic part is inserted into Leb4.

Let G={(Z,m-n,W):T^m Z=T^n W,m,n>=0}, both histories ENTIRELY
legal, source W, target Z; take inherited Borel structure in Y x Z
x Y. Same actual triples are the same arrow, without free factorization-word
isotropy. For every legal step and its ACTUAL inverse B_Z:TZ->Z set

    kappa(Z)=-log J_(B_Z)(TZ);
    S_m(Z)=sum_(0<=i<m) kappa(T^i Z), S_0=0;
    C(Z,m-n,W)=S_m(Z)-S_n(W).

Representation independence, cocycle law, actual branch IMAGE meaning and measurable
ownership require audit. At undefined terminal steps no derivative or nonempty
sum is evaluated. Keep ALL Y x R_h with arrows(W,h)->(Z,h+C),
and proposed time translation h->h+t. This is an IMAGE-clock extension,
NOT physical Hamiltonian time, algorithmic runtime or a manually supplied roof.

Keep entire source G_Z^Z, clock kernel, extension fixed-object isotropy and
H_Z=C(G_Z^Z). Only ENTIRE H_Z=LZ with least L>0 defines
a positive primitive time; repetitions rL remain in that full packet. Retain
every ancestor, terminal, zero-time/nondiscrete case and full real matrix fibre.
Do not identify sources by eigenvalues, similarity, determinant, symbols or time.
Only actual extension arrows identify height phases. No coarse Hausdorff quotient,
smooth flow, conservative/symplectic realization or trace/operator is assumed.

## 4. Three controls with complete separate owners

Each retains full Y,mu but owns its legal map, complete inverse, all-point
IMAGE, lag/clock/kernel and whole incoming/packet/phase ledger.

A — DIVISIBILITY-OFF: D_A={x!=0,floor(x)!=0,s!=0}, deleting ONLY the
integer divisibility check. Use the same nonlinear displayed T. Generate I but
verify its OWN source conditions and forward equality, not main's divisibility.
Use all own floor cells, now every c in Z, for branch domains.

B — DIVISIBILITY-SHIFT: D_B={x!=0,a=floor(x)!=0,a divides(floor(z)+1),s!=0}.
Use the same T. Generate I and test floor(u) divides(floor(lambda u)+1)
with its own remaining source conditions and forward equality. Its own floor
cells require a divides(c+1), not a divides c.

C — REASSEMBLY-OFF: keep EXACTLY main D, but T_C(M)=M on D;
outside D stays terminal. Its complete inverse is identity on D, NOT
main's rational inverse or inherited IMAGE value. Preserve the full real fibre.

## 5. Exact symbolic-lineage interface and nonclaims

Native integer tests are M(n,d)=[[d,0],[n,1]], n>=2,d>=1.
Read pivot d and lower-left n; intended permission d divides n, with
proper-divisor observable1<d<n. Exact compatibility with all other domain conditions
must be proved. This interface is NOT the carrier or a selected recurrent core.

The proposed arrow is divisor-symbolic permission -> actual present real quotient
and triangular factors -> nonlinear multiplication-order reassembly LU to UL ->
new matrix's next divisibility permission. It replaces the sieve-symbolic transport
on the broadened track, not a completed Logistic/Henon conservative lift. Pivot,
floor coordinates, factor order and Lebesgue density are acknowledged design choices.
Strong arithmetic naturalness, prime selectivity and invariant/period claims stay OPEN.

No log p, von Mangoldt weight, prime table, Riemann-zero data or per-prime
choice is allowed. Classical symplectic form/base/positive roof/suspension and classical
A0/A1/A2 are NOT APPLICABLE; T0–T3 owner labels only. T3 NOT SUPPLIED;
formal UNASSIGNED; B NOT INVOKED. No later Hamiltonian/contact/quantum owner.

## 6. Prebounded decisive gate

First prove complete inverses, source/target permissions, boundary and terminal incoming,
then same-measure full-point IMAGE and retained-lag ownership. BEFORE a period
table ask whether the clock is a global endpoint difference, excluding target
return time. A potential cannot silently omit a retained zero or terminal fibre.

Only if this clock check does not decide, inspect the COMPLETE fixed
and legal T^2 sets of main and all controls, not positive/integer matrices
or a chosen spectrum/section. Decisive ownership, complete-time or multiplicity obstruction
stops the audit; otherwise retain bounded OPEN and stop/fork. No pivot/order/
measure/permission/clock change, high-period census or numerical fitting campaign.

Root clarifies before freeze: direct inverse/one-step identities may specify the full
incoming/source/kernel/phase ledger; unknown higher-period realizations remain OPEN. Do not
claim absence of source cycles from a failed clock. The complete fixed/T^2
window remains the precommitted next test if the clock check is not decisive.

## 7. Provenance, first lock and separated review

Root read335's COMPLETE204-line frontier. The definition author read ONLY316
original1–110 and318 original1–98, neither EOF; totals unreported. Heading scans
exposed outcome TITLES188/166, not bodies. The316 prefix itself mentioned other
historical negative statuses; no referenced cards/results were opened. No current335
or334 science/peer, third card, old paper/review, web, scientific computation,
auxiliary or write entered initial delivery. These are definition comparisons, not
global novelty/nonconjugacy proofs. Root did not reopen316/318 or borrow their outcomes.

Later author QA read335 frontier25–187 only, NOT EOF, no headings/other
files/SHA/length measurement. It confirmed substantive transcription and requested explicit
=0 notation, which root restored. The existence-only current335 clock-verdict mention
was NEW QA exposure, not original definition input or its mathematical content.

Root's §6 full-ledger clarification is pre-freeze scope wording, not changed action
or clock. Reviewer reads ONLY this ORIGINAL card, personally derives main and
ALL controls, then sends metadata ALL RAW READY while withholding ALL math.
Root FIRST-paper hash lock plus explicit RAW RELEASE precedes every raw result;
ALL RAW FINAL precedes a SEPARATE PAPER UNLOCK and manuscript/adverse review.
Root owns all package paths except evidence/independent-review.md. No auxiliary/web/
scientific numerics in review. Shared model/history NOT_CALIBRATED, not external peer
review or independent-error evidence. Markdown only, no PDF/LaTeX/publication/upload,
staging/commit, model or old-package changes.241/242 paused; programme goal active.
Preserve this complete original prefix before appending any outcome.

## 8. Appended outcome — original175-line definition unchanged

Final status: `OWNED REASSEMBLY CLOCK; CONTINUUM PRIMITIVES — STOP / FORK`.
Read [paper](paper.md), [claim ledger](claim-ledger.md) and [evidence](evidence/README.md).

The full rational inverse is exact and unique on its OWN source-checked
image. Main/A/B own full-point J_I=abs(u/omega) and every-Borel image laws;
their step clock is log(abs(s/x)). C owns identity J=1 and clock0.
The retained-lag groupoid and extension use those same actual branches, not a
physical flow or transplanted determinant. All cuts, singular/terminal matrices and
actual incoming remain. Singular matrices have no incoming; other terminals may.

On ENTIRE z!=0, F=log(abs(z)) gives kappa=F(T M)-F(M),
so every source there has ENTIRE H0, including all native n>=2 divisor
test seeds. General source periods are not thereby excluded. Complete actual
inverse chains remain, with phase h+F(M) and source/kernel dZ on a
least-d cycle,0 otherwise. Injectivity precludes extra transient ancestors of a cycle.

This potential is NOT global. Every legal z=0 state is fixed with
alpha=log(abs(w/x)); its complete orbit is singleton, source groupZ and H=alphaZ.
If alpha!=0 the positive primitive is abs(alpha), kernel/extension isotropy0 and
phases R/abs(alpha)Z. Otherwise source/kernel/extensionZ, H0 and real phase.
Illegal z=0 states are isolated terminals. All positive-time sources are exactly
this legal z=0,abs(w/x)!=1 family; C has none anywhere.

For every L>0, [[1,y],[0,exp(L)]] is legal for main/A/B and
owns least primitive L for EVERY real y. These are continuum DISTINCT
packets at each length, not repetitions or selected representatives. The explicit
w=3/2 source gives non-log-prime length log(3/2). The entire positive-time
family is Leb4-null but retained; deleting it would change the object.

Complete fixed sets are D_own intersect({z=0} union{y=0,w=x}). Complete
least-two sets are {M in D_own:T M in D_own,z!=0,x+w=0},
with all OWN floor checks on both states. Those two-cycles have H0,
source/kernel/extension2Z, possibly nonzero opposite step clocks. C fixes all D,
with H0; every outside-D C terminal is isolated. Higher nonlinear source
period realizations remain UNCLASSIFIED, without leaving their time groups undetermined.

Same-object ledger intact. T0/full IMAGE clock ownership established; prime-only
time and finite-multiplicity T2 target FAILS. Strong naturalness remains OPEN,
not rescued by generic transverse fixed-source clocks. T3 NOT SUPPLIED / NOT
PURSUED; classical ASFS A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT
INVOKED. Portfolio stop / fork, not a zero-clock or no-positive-period theorem.
No measure/roof/permission repair or further local census. Earlier packages unchanged;
241/242 paused; programme goal active.
