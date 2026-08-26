# Paper 16 shared-`iota` / independent-lift factorization precheck

Status: **COMPLETE — FAIL-FAST STOP**  
Version: `P16-SHARED-IOTA-FACTORIZATION-PRECHECK-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Scope: source-level change-of-choice groupoid, owner typing, and standalone
nonredundancy only

```text
SOURCE_TRANSITION_CALCULUS       = COMPLETE_DERIVATION
SOURCE_UNDERDETERMINED           = false
FIXED_PRIME_TRANSITIONS          = ALL_B_r_TRANSLATIONS_X_ID_TIME
PAIRED_FULL_TRANSITION_IMAGE     = B_p_X_B_q
PAIRED_IMAGE_PROPER_SUBDIRECT    = false
COMMON_IOTA_ONLY_IMAGE           = PROPER_SUBDIRECT_BUT_NOT_FULL
FACTOR_INVISIBLE_INTRINSIC_DATA  = NONE
FINDINGS                         = C1/M1/m0
STANDALONE_PASS                  = false
FULL_PAPER                       = false
TECHNICAL_NOTE                   = false
FINAL_DISPOSITION                = STOP_SLOT16 / MERGE_FOUNDATION
GO_TO_PROTOCOL                   = false
```

The decisive calculation is short but not optional.  A common change of the
global root-of-unity injection produces the proper common-choice image already
computed in the Slot-14 common-quotient report.  However, Deninger's coordinate
construction chooses a geometric point separately above each closed point.
Once the independently permitted changes of `x_p` and `x_q` are included, even
with the injection `iota` held fixed, their cyclotomic characters independently
realize every translation in `B_p` and every translation in `B_q`.  Hence the
full paired image is the product `B_p x B_q`, not a proper subdirect product.

The common-choice mismatch is therefore not invariant under the full source
choice groupoid.  If the lift changes are artificially frozen, the surviving
cokernel is exactly the already-audited Slot-14/P15 common-quotient and
Smith--Ulm package.  It is not a new Paper-16 invariant.

## 1. Exact authorization and frozen-byte gate

This is the one source fail-fast authorized by the exact batch amendment v3.
The target path did not exist before this report was written.  The following
six required records were rehashed and read in full before the calculation.

| Required authority | Lines | Bytes | SHA-256 | Result |
|---|---:|---:|---|---|
| Papers 14--18 batch amendment v3 | 273 | 11320 | `09d7f23b8a20b2d1bfd45a32f7ef695772f7cec2b9c251b7dd217c6a0b37a4e8` | MATCH |
| P16 owner-sensitive salvage precheck | 504 | 26821 | `9f50124a7c89b5164fdbf63fcea6f14f28187fb4cb559e975039a4cbab0a1bda` | MATCH |
| replacement-P14 coordinate-transition precheck | 474 | 20136 | `037dd140f53dcc8384a0d4b71bd7f3f3358b55ab6dff284fa81d63940cf5d6df` | MATCH |
| Slot-14 rank-two common-quotient precheck | 735 | 28188 | `63dcace23ac620b7cc5d41ac78f4c6adbdafecd77f3cec11d0a6f66401634332` | MATCH |
| replacement-P15 symbolic proof ledger | 1127 | 44868 | `7804e73863e271402b4c1331843a0cf9a1f4a06e6944b4cbb35257c0aa7d8355` | MATCH |
| replacement-P15 exact-byte peer review | 712 | 32599 | `2b889ba09b95b3d97be62780f026e4a9e3de58379eb9abb8c720c8b6cd792cc7` | MATCH |

The current P16 protocol/lock records were also read on their complete bytes:

| P16 record | SHA-256 | Authority retained |
|---|---|---|
| `research_protocol.md` | `7af9853e1c44b87a14e7310a94a8de321857bcf3ed51d453b6b153776f4739d1` | historical Arveson candidate and standardized-owner boundary |
| `phase1_amendment_v1.md` | `65684892f52219ee50b9c809d3b69b56c2d5295ee430514ab6831ba731655af6` | strict/scaled/unmarked categories and merge trigger |
| `candidate_lock.md` | `398b3e6e083f9ece90ccd7b47e195f5cc694b8fdb481290769093efeb16736c7` | historical dependency lock |
| `candidate_lock_v2.md` | `46f723cccfedcf4d9bd72a4b35017b125a9e56de5eda8480a670b8f03a328658` | current generic ideal/spectrum candidate, already `NO_GO` under the salvage report |

No mutable pipeline state, proof conversation, control output, Route record,
or manuscript text is evidence for this precheck.

## 2. ARS method and review discipline

The complete ARS router, deep-research workflow, academic-paper-reviewer
workflow, methodology reviewer, domain reviewer, reviewer devil's advocate,
source-verification agent, and source-quality hierarchy were read before task
work.  Their exact roles here were:

- **methodology:** derive a typed groupoid with arrows, identity, inverse,
  composition, and flow covariance before asking for an invariant;
- **domain/owner:** keep the compact chart, the marked common-choice record,
  and the actual inherited packet topology distinct;
- **devil's advocate:** test the strongest favourable restriction—forcing the
  same transporter or freezing both lifts—and then restore every source-allowed
  arrow;
- **source verification:** use the local primary PDF and primary/official
  mathematical sources; treat earlier audit prose as a locator and ceiling,
  never as a replacement for the primary formulas; and state the web-search
  ceiling explicitly; and
- **nonredundancy:** subtract the final P15 proof and the Slot-14 rank-two
  result on exact bytes before assigning standalone weight.

The ARS singleton-Critical rule is applied.  The product-image theorem below
is the one Critical finding because it alone defeats a necessary registered
pass condition.  The Major finding is a separate maximum-subtraction failure
under the artificial favourable restriction; it is not a second count of the
same image calculation.

## 3. Primary source and owner corpus

### 3.1 Deninger primary bytes

The load-bearing primary file is

```text
papers/12-marked-time-cohomology/notes/sources/
  coh-deninger-dynamical-arithmetic-schemes-v4.pdf
SHA-256: edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09
pages: 119
preflight: PASS, 119/119/119, no warnings
```

Physical PDF pp. 30--34 and 37--39 were read directly.  The exact source
inputs are:

1. Section 5 fixes one global injection `iota:mu(K)->mu(C)` and, for a given
   closed point, one point `x` of the normalization above it.
2. Equation (32) supplies the reduction isomorphism on prime-to-residue-
   characteristic roots of unity.
3. Equations (34)--(39) supply the fixed-prime finite-kernel character and
   balanced-product set descriptions.
4. The paragraph after (39) says that the coordinate and fibration maps depend
   on `x` and `iota`.
5. Equation (40) makes the time quotient canonical.
6. Section 6 suspends the construction and makes the flow act in the time
   coordinate.

Deninger does not print the change-of-choice groupoid below.  It is derived
from those explicit formulas and standard Galois extension facts; it is not
attributed to the source.

### 3.2 Prior source and owner records actually used

| Record | SHA-256 | Use and ceiling |
|---|---|---|
| P2 Deninger source audit | `a4785e0fd56cb4e24211ea4d8f0e78a83ccdd6c942dc6572c87b2c1230ae521a` | source set/action facts and the historical absence of printed transition formulas |
| P7 Deninger ownership audit | `a6a0e75aa2a5f38e8c60a5ce34ffb536438f93828501e282a2d0ecb530847d53` | primary manifestations, chosen-chart ceiling, and no analytic-owner promotion |
| P7 ownership manifest | `ca28c2d24223d7031ca9a5ae0e20c50cbb57ff8b13f8f897efa262b916f4df68` | exact Deninger/Morishita source bytes |
| P7 canonical source manifest | `d99a0e9c9ddcfb4ab5ca3f7a57284dd1a405567664ce3dcc1d7abd1602fd4d0e` | retained primary-source union |
| P9 actual-owner candidate lock | `0e0e2f5e7a557baaf91cf6ca1abf4d17e0743a56d2d30f1364188d853f8f3ded` | actual/chart/quotient namespace |
| P9 actual-topology proof audit | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | the actual fixed-prime packet, each inherited orbit, and its orbit quotient are nontrivial indiscrete spaces |

The P2 and P7 source audits were read in full.  The P9 lock was read in full,
and the exact topology theorem, its owner proof, and final verdict were checked
in the P9 proof audit.  These records do not replace Deninger's formulas; they
prevent an owner reversal.

### 3.3 Bounded primary/official web verification

The external check was deliberately bounded to seven query strings in two
search calls.  Query families were:

```text
official extension of an automorphism of a normal subextension to an
  algebraic closure;
official cyclotomic Galois group Gal(Q(zeta_n)/Q)=(Z/nZ)^times;
official definition/surjectivity basis of the global cyclotomic character;
official arXiv record for Deninger 1807.06400.
```

Admitted records were:

- Deninger's official arXiv record,
  <https://arxiv.org/abs/1807.06400>;
- Stacks Project, Tag `09HL`, Lemma 9.15.7, on extending a map inside a normal
  algebraic extension to an automorphism,
  <https://stacks.math.columbia.edu/tag/09HL>;
- MIT 18.785 Lecture 20, which records
  `Gal(Q(zeta_m)/Q) ~= (Z/mZ)^times`,
  <https://math.mit.edu/classes/18.785/2015fa/LectureNotes20.pdf>; and
- J. S. Milne's official notes for the cyclotomic-character convention and
  restriction to the maximal abelian extension,
  <https://www.jmilne.org/math/xnotes/AA.pdf>.

Together, the finite cyclotomic isomorphisms, inverse limits, and the normal-
extension lemma prove the only external fact needed below:

```text
chi_cyc:G_Q -> Zhat^times is surjective.                  (3.1)
```

The search stopped once (3.1) and the extension step were verified.  No
secondary technical source was admitted.  No novelty or priority claim is
inferred from search silence.

## 4. Three owners that must not be merged

Fix distinct rational primes `p` and `q`.  Put

```text
A   = Zhat^times,
U_r = product_(ell != r) Z_ell^times,
H_r = r^Zhat subset U_r,
B_r = U_r/H_r,
L_r = R_{>0}/r^Z,                                        (4.1)
```

for `r in {p,q}`.  There are three different records.

### 4.1 Compact chart owner

A chosen coordinate presentation has carrier

```text
Y_r=B_r x L_r.                                            (4.2)
```

It has the abstract compact topology on `B_r`, the ordinary compact-circle
topology on `L_r`, and, if later explicitly selected, normalized Haar.  The
transition calculation below is a calculation on these chart models.

### 4.2 Source-induced common-choice record

One global change of `iota` has one label in `A`.  With the lifts held fixed,
its two projections give the marked homomorphism

```text
beta_pq=(beta_p,beta_q):A -> B_p x B_q,                   (4.3)
```

where `beta_r` drops the `r` coordinate and quotients by `H_r`.  Slot 14
proves that this common-choice image is a proper subdirect product with a
nontrivial formal common quotient.  This is a marked subfamily of choice
causes.  It is not yet the full transition groupoid.

### 4.3 Actual packet owner

The source charts are set/equivariant bijections, not source-stated
homeomorphisms from (4.2) to the inherited packet.  P9 proves that the actual
fixed-prime packet, its inherited periodic orbits, and its intrinsic orbit
quotient are nontrivial indiscrete spaces.  Therefore:

```text
compact B_r chart topology != actual orbit-quotient topology;
common-iota marked image    != actual packet topology;
this precheck proves no topology transport in either direction.          (4.4)
```

There is no source-defined actual two-prime packet product whose topology may
be silently substituted for `Y_p x Y_q`.  The paired object below is a
source-choice/chart comparison record only.

## 5. Complete paired choice groupoid

Let `I` be the set of injections `mu(Qbar)->mu(C)`, and let `X_r` be the set
of points of the normalization of `Spec Z` in `Qbar` lying above `(r)`.
Define the raw paired choice groupoid `G_(p,q)` by

```text
Objects: c=(iota,x_p,x_q) in I x X_p x X_q.               (5.1)
```

For two objects `c` and `c'`, an arrow is represented by

```text
(epsilon,sigma_p,sigma_q):c -> c',                        (5.2)
```

where

```text
iota' = iota o ( )^epsilon,       epsilon in A,
sigma_r x_r = x'_r,               sigma_r in G_Q.          (5.3)
```

The exponent `epsilon` is unique.  Existence and uniqueness follow because
the root-of-unity groups are copies of `Q/Z`, and an injective endomorphism
on every Pruefer primary component is multiplication by a local unit.
Transporters `sigma_r` exist because `G_Q` acts transitively on the geometric
points over a fixed closed point, as used explicitly in Deninger's Section 5.

The two transporters are independent.  Deninger fixes `x` separately for the
closed point whose packet is being described.  A pair of charts therefore
chooses one point in `X_p` and one point in `X_q`; the source supplies no
global section and no requirement that one `sigma` move both points.

### 5.1 Raw laws

For arrows `a:c->c'` and `b:c'->c''`, write their representatives as
`(epsilon_a,sigma_(a,p),sigma_(a,q))` and similarly for `b`.  Then

```text
1_c=(1,1,1),                                               (5.4)

b o a=(epsilon_a epsilon_b,
       sigma_(b,p)sigma_(a,p),
       sigma_(b,q)sigma_(a,q)),                            (5.5)

a^(-1)=(epsilon_a^(-1),
        sigma_(a,p)^(-1),
        sigma_(a,q)^(-1)).                                 (5.6)
```

These are the identity, composition, and inverse laws of the transporter
groupoid.  The apparent order difference in (5.5) is harmless for the
cyclotomic labels because `A` is abelian.

### 5.2 Effective coordinate label

Let `chi_cyc:G_Q->A` be the cyclotomic character.  For an arrow `a`, define

```text
d_r(a)=pr_r(epsilon_a chi_cyc(sigma_(a,r))) in U_r,
bar_d_r(a)=d_r(a) H_r in B_r,
tau_r(a)=bar_d_r(a)^(-1).                                  (5.7)
```

If two transporters take `x_r` to the same `x'_r`, their ratio stabilizes
`x_r`.  Deninger's equation (34) identifies the prime-to-`r` cyclotomic image
of that stabilizer with `r^Zhat=H_r`.  Thus `bar_d_r(a)` is independent of
the transporter representative.

The P14 fixed-prime derivation from equations (32), (34)--(39) gives the
complete effective transition:

```text
T_a:Y_p x Y_q -> Y_p x Y_q,

T_a((b_p,[s_p]),(b_q,[s_q]))
 =((tau_p(a)b_p,[s_p]),
   (tau_q(a)b_q,[s_q])).                                   (5.8)
```

No time translation, dilation, inversion, or mixing occurs.  Equation (40)
is the canonical-time firewall.

### 5.3 Effective laws and flow covariance

The cyclotomic character is multiplicative, so modulo `H_r`,

```text
bar_d_r(b o a)=bar_d_r(a)bar_d_r(b),
tau_r(1_c)=1,
tau_r(a^(-1))=tau_r(a)^(-1),
T_(b o a)=T_b o T_a.                                      (5.9)
```

For the diagonal literal flow

```text
phi^t((b_p,[s_p]),(b_q,[s_q]))
 =((b_p,[e^t s_p]),(b_q,[e^t s_q])),                      (5.10)
```

equation (5.8) gives

```text
T_a phi^t=phi^t T_a.                                      (5.11)
```

The same calculation commutes with the larger independent `R^2` flow on the
two time factors.  Hence the groupoid is complete at the exact scope required
by the batch gate.

## 6. Full-image theorem

Define the effective full paired transition image

```text
Lambda_(p,q)
 ={(tau_p(a),tau_q(a)):a is an arrow of G_(p,q)}
 subset B_p x B_q.                                        (6.1)
```

### Theorem 6.1

```text
Lambda_(p,q)=B_p x B_q.                                   (6.2)
```

**Proof.**  Each map

```text
beta_r:A -> B_r                                           (6.3)
```

is onto: coordinate deletion `A->U_r` is onto, followed by the quotient
`U_r->B_r`.  By (3.1), `chi_cyc:G_Q->A` is onto.

Take arbitrary `(g_p,g_q) in B_p x B_q`.  Choose `a_p,a_q in A` with

```text
beta_p(a_p)=g_p^(-1),
beta_q(a_q)=g_q^(-1).                                     (6.4)
```

Choose independent `sigma_p,sigma_q in G_Q` satisfying
`chi_cyc(sigma_r)=a_r`, and set `x'_r=sigma_r x_r`.  Hold the global injection
fixed, so `epsilon=1`.  Equations (5.7)--(5.8) then give the transition label
`(g_p,g_q)`.  Thus the full product is contained in the image; the reverse
containment is tautological.  QED.

The conclusion is stronger than saying that a common-`iota` restriction is
eventually enlarged.  **Lift changes alone, with `iota` unchanged, already
give the full product.**

### 6.2 Exact reparameterization that removes the apparent coupling

At the effective cyclotomic-label level, the raw parameters are

```text
(epsilon,a_p,a_q) in A^3,
F(epsilon,a_p,a_q)
 =(beta_p(epsilon a_p),beta_q(epsilon a_q)).               (6.5)
```

The automorphism

```text
Theta:A^3 -> A^3,
Theta(epsilon,a_p,a_q)
 =(epsilon,u_p=epsilon a_p,u_q=epsilon a_q)                (6.6)
```

has inverse `(epsilon,u_p,u_q)->(epsilon,epsilon^(-1)u_p,
epsilon^(-1)u_q)`.  In the new coordinates,

```text
F Theta^(-1)(epsilon,u_p,u_q)
 =(beta_p(u_p),beta_q(u_q)).                               (6.7)
```

The shared `epsilon` is a silent kernel coordinate.  If
`N_r=ker(beta_r)`, then the kernel becomes

```text
A x N_p x N_q.                                            (6.8)
```

Thus even the marked cause-parameter homomorphism is a split product after an
explicit automorphism.  There is no hidden extension class produced by the
common injection.

## 7. Why the common-choice proper subdirect is not the full answer

With both lifts frozen, or if one artificially requires
`sigma_p=sigma_q`, equations (5.7) reduce to the common map

```text
Delta_(p,q)=im(beta_p,beta_q) subset B_p x B_q.            (7.1)
```

Slot 14 proves the exact sequence

```text
0 -> A/(N_p cap N_q)
  -> B_p x B_q
  -> C_pq=A/(N_pN_q)
  -> 0,                                                    (7.2)

Delta_(p,q)=B_p x_(C_pq) B_q.                             (7.3)
```

This is the strongest counterargument to the stop verdict: a single global
`iota`, or a single forced Galois transporter, does produce a proper
overlap-compatible subdirect image.

It is not the source's full transition groupoid.  The choice of `x_p` and the
choice of `x_q` are separate inputs.  Restoring their independent changes adds

```text
beta_p(A) x beta_q(A)=B_p x B_q,                           (7.4)
```

so (7.1) is swallowed by the product.  Requiring a single transporter would
add a new global marking not printed by Deninger and would delete legitimate
source choices.  It is therefore not an admissible Paper-16 owner.

## 8. Factor-invisible invariant attacks

### 8.1 Object invariant on the compact chart

The product `B_p x B_q` acts by all translations on the transverse chart
`B_p x B_q`.  This action is simply transitive.  Therefore every invariant
function, partition, or isomorphism class of a transverse chart point that is
unchanged under every full transition is constant.  No nonconstant pair-only
invariant survives.

The time coordinates are fixed by every transition.  They retain only the
two separate clocks `log p` and `log q`, each visible on a projection and
already part of the standard marked-time foundation.  They are not a
factor-invisible paired invariant.

### 8.2 Arrow invariant

An effective paired arrow is exactly the ordered pair of its two projected
translation arrows because the image is the product.  Hence no effective
arrow relation is lost by both projections.  The raw nonabelian kernels of
the two cyclotomic characters act trivially on their respective charts and
occur independently; (6.6)--(6.8) show that the common injection adds only a
split silent factor.  A label remembering whether a translation was called an
`iota` change or a point change is a decomposition of a cause, not an
intrinsic coordinate invariant.

### 8.3 Common-quotient mismatch

Let `delta:B_p x B_q->C_pq` be the quotient map in (7.2).  Under a full
translation `(g_p,g_q)`, in additive notation,

```text
delta((g_p,g_q)+(b_p,b_q))
 =delta(g_p,g_q)+delta(b_p,b_q).                           (8.1)
```

Because `delta` is onto and `(g_p,g_q)` ranges over the full product, the
common-quotient value can be moved to any element of `C_pq`.  It is not
invariant.

If independent lift changes are forbidden, `C_pq` survives, but the final
Slot-14 report already proves that its primary signature is

```text
h_r(p,q)=0                                      for r in {p,q},
h_r(p,q)=min(kappa_r(p),kappa_r(q))             otherwise, (8.2)
```

and that finite owner sets give the corresponding incidence-matrix Smith
invariants.  The Slot-14 standalone verdict is `MERGE_P15R / STOP_SLOT14`.
Thus the favourable restricted invariant is exactly the generic P15
common-quotient/Smith--Ulm material prohibited by the P16 gate.

### 8.4 Actual topology cannot rescue the invariant

The actual fixed-prime packets and their orbit quotients are indiscrete, and
the compact charts are not homeomorphic owners.  The paired source-choice
calculation cannot be transported to the actual topology.  Conversely, an
actual-topology continuous invariant with a `T0` or Hausdorff target is
constant already on each factor.  This supplies no pair-only rescue and does
not turn the actual packet into a compact common-quotient owner.

### 8.5 Result

```text
FULL_IMAGE_PRODUCT                       = true
TRANSVERSE_FULL_ACTION_TRANSITIVE        = true
EFFECTIVE_ARROW_DETERMINED_BY_PROJECTIONS= true
COMMON_IOTA_PARAMETER_SPLITS_OFF         = true
COMMON_QUOTIENT_INVARIANT_UNDER_FULL_ARROWS=false
NON_GENERIC_FACTOR_INVISIBLE_INVARIANT   = false.          (8.3)
```

## 9. Maximum P15/Slot-14 subtraction

| Candidate residue | Exact prior owner | What remains for P16 |
|---|---|---|
| fixed-prime source transitions | replacement P14 precheck | input only: all `B_r` translations times identity on time |
| common `iota` image | Slot-14 rank-two report | formal proper subdirect before lifts are restored |
| common quotient `C_pq` | Slot 14 plus P15R | no invariant under the full groupoid |
| off-owner height `min(kappa_r(p),kappa_r(q))` | P15R and Slot 14 | no new height or relative tail |
| finite-set generalization | Slot-14 incidence-matrix Smith form | no nonformal functorial theorem |
| minimal ideals and component Arveson spectra | old P16 candidate | valid generic `c_0` circle lemma only; merge foundation |
| actual packet topology | P9 | indiscrete owner; no compact-chart promotion |

After exact subtraction there is no source-specific theorem center.  The only
positive Paper-16 mathematics left is the already-recognized generic
minimal-ideal/Arveson-spectrum lemma for a `c_0` sum of circle flows.  It may be
retained as shared foundation but not as a standalone paper or a second
Technical Note.

## 10. Findings

### C1 — independent lift changes make the full image a product

The registered pass condition requires the complete paired transition image
to remain a proper subdirect product after all source-permitted changes of
`x_p` and `x_q`.  Theorem 6.1 proves the opposite: with `iota` fixed, the two
independent transporters already realize `B_p x B_q`.  This is a singleton
foundation-collapse finding.  It alone forces `STOP_SLOT16` under batch
amendment v3.

**Remedy threshold:** none inside the registered owner.  Forcing one
transporter, freezing a lift, or remembering the cause decomposition would
change the source choice groupoid.  A future replacement would need a
different source-defined global object that genuinely binds the two lifts.

### M1 — the favourable restricted invariant is already P15/Slot-14 data

If the legitimate independent lifts are removed, the common-choice image has
the formal quotient `C_pq`.  Its complete new-looking signature is the
minimum of two P15 `kappa` tails and, for finite sets, ordinary Smith factors.
The exact Slot-14 report already assigns it to a P15 corollary/appendix and
stops its standalone slot.  It cannot be relabelled as a factor-invisible P16
invariant.

**Remedy threshold:** a source-defined invariant that survives the full product
image and is not the common quotient, a projection combination, a generic
paired-group invariant, or the P15/Slot-14 Smith--Ulm signature.  No such
invariant exists in the audited groupoid.

### Minor findings

None.  Expository changes cannot alter the full-image theorem or the maximum-
subtraction result.

## 11. Standalone and publication disposition

The mathematical task is determined rather than source-underdetermined, but
the determination is negative for the candidate:

```text
MATHEMATICAL_GROUPOID_DERIVATION=PASS
SOURCE_OWNER_TYPING=PASS
DEVILS_ADVOCATE_FULL_ARROW_RESTORE=PASS
P16_CANDIDATE_GATE=FAIL
CRITICAL_FINDINGS=1
MAJOR_FINDINGS=1
MINOR_FINDINGS=0
STANDALONE_PASS=false
FULL_PAPER_PLAUSIBLE=false
FULL_PAPER=false
TECHNICAL_NOTE_PLAUSIBLE=false
TECHNICAL_NOTE=false
MERGE_TARGET=SHARED_FOUNDATION_ONLY
FINAL=STOP_SLOT16 / MERGE_FOUNDATION
```

This stop does not create a replacement slot, a new protocol, or a Note.  It
preserves the exact five-slot register by leaving Slot 16 visibly stopped.

## 12. Final authorization boundary

```text
P16_SHARED_IOTA_FAILFAST_COMPLETE=true
P16_SHARED_IOTA_FAILFAST_VERDICT=STOP_SLOT16_MERGE_FOUNDATION
ALL_DOWNSTREAM_AUTHORIZED=false

P16_PROTOCOL_AUTHORIZED=false
P16_CANDIDATE_LOCK_AUTHORIZED=false
P16_PROOF_AUTHORIZED=false
P16_CONTROL_DESIGN_AUTHORIZED=false
P16_CONTROL_IMPLEMENTATION_AUTHORIZED=false
P16_CONTROL_EXECUTION_AUTHORIZED=false
P16_ROUTE_A_AUTHORIZED=false
P16_ROUTE_B_AUTHORIZED=false
P16_COMPOSITION_AUTHORIZED=false
P16_MANUSCRIPT_AUTHORIZED=false
P16_FIGURE_WORK_AUTHORIZED=false
P16_RELEASE_AUTHORIZED=false
P16_ARCHIVE_AUTHORIZED=false
P16_GIT_AUTHORIZED=false
P16_GIT_PUBLIC_SYNC_AUTHORIZED=false

OTHER_SLOT_PROTOCOL_AUTHORIZED_BY_THIS_REPORT=false
OTHER_SLOT_PROOF_AUTHORIZED_BY_THIS_REPORT=false
OTHER_SLOT_CONTROL_AUTHORIZED_BY_THIS_REPORT=false
```

No protocol, candidate lock, proof ledger, control, Route record, composition,
manuscript, figure, release, archive, pipeline state, or Git state was created,
modified, or executed by this precheck.
