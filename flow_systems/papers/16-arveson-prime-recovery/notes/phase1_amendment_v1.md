# Paper 16 Phase-1 amendment v1 — mixed foundation and Arveson classification

Status: **ACTIVE / INDEPENDENT EXACT-BYTE REVIEW REQUIRED**  
Version: `P16-P1-AMENDMENT-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Proof, controls, Route A/B, manuscript, release, Git, and public
synchronization: `false`

## 1. Exact authority and precedence

This amendment binds:

```text
Papers 14--18 historical batch design lock
  sha256:2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
Papers 14--18 batch amendment v1
  sha256:afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802
Paper-16 base research protocol
  sha256:7af9853e1c44b87a14e7310a94a8de321857bcf3ed51d453b6b153776f4739d1
Paper-16 base candidate lock
  sha256:398b3e6e083f9ece90ccd7b47e195f5cc694b8fdb481290769093efeb16736c7
old Paper-15 research protocol
  sha256:53e023e427616e5bd98852181495c6598940e2eb238f100482f3abc7011ca59c
old Paper-15 mathematical precheck
  sha256:1598569c48d4382408bb3df933a1c5443984daf36b12e6377bae4590356a75f8
```

The batch amendment supersedes the base protocol's dependency on a separate
Paper-15 proof.  The mathematically valid old-P15 mixed-standardization
package is now an internal Paper-16 foundation; the failed minimum lemma is
only a control.  The replacement Wieferich--Ulm Paper 15 is independent and
is not a prerequisite.

The base protocol remains binding except where this amendment changes the
dependency, expands the foundation ledger, or strengthens the classification
and standalone gates.

## 2. Mixed marked foundation

Let `X` be a nonempty right-real set whose every orbit `q in Q=X/R` has

```text
Stab(q)=H_q=L_q Z,       L_q>0.
```

The same fixed real time line is part of the owner.  Define `Std_mix(X)`
section-freely by giving each orbit the quotient topology of any orbit map
`R->q` and taking the topological coproduct over `Q`.

The proof package must establish:

1. basepoint independence, Hausdorffness, joint action continuity, open
   components, and uniqueness among compatible Hausdorff topologies with
   open orbits;
2. an exact equivalence with nonempty coproducts of the marked torsors
   `R/(L_q Z)` and global indiscretization as the correctly typed inverse;
3. strict morphisms separately from globally `c`-scaled morphisms
   `F(x.t)=F(x).(ct)`;
4. the exact existence criterion

   ```text
   L_Y(sigma(q))=c L_X(q)
   ```

   with composition, inverse, ZFC choice, and origin-choice boundaries;
5. the canonical extensions by
   `product_q R/(L_q Z)` over the strict length-preserving permutation group
   and over

   ```text
   W_L={(sigma,c):L(sigma(q))=cL(q)};
   ```

6. the noncanonical nature of every origin-based split.

These statements are direct mathematical obligations inside Paper 16.  The
old precheck derived them, but no final proof may cite the precheck as if it
were a peer-reviewed theorem.

## 3. Analytic owner and arbitrary-index continuity

For the standardized owner put

```text
O_q=R/(L_q Z),
A=C_0(Std_mix X)=direct_sum_q^{c0} C(O_q),
(alpha_t f)(x)=f(x.t)
```

with one frozen sign convention.  The proof must establish strong
continuity for arbitrary, possibly uncountable, `Q`.  A permitted direct
proof first truncates a `c0` element to finitely many coordinates and then
uses uniform continuity on the corresponding compact circles.  No
separability or sigma-unital hypothesis may be imported silently.

The displayed direct-sum labels are construction data, not the definition
of the reconstructed answer.

## 4. Intrinsic invariant-ideal reconstruction

The central owner-free formulation is in terms of the dynamical system
`(A,alpha)`.  Prove:

1. every nonzero closed `alpha`-invariant ideal contains a minimal nonzero
   invariant ideal;
2. the set `Min_alpha(A)` of minimal nonzero invariant ideals is intrinsic;
3. under the constructed presentation, `Min_alpha(A)={A_q}_q`, where
   `A_q=C(O_q)` is extended by zero;
4. every strict equivariant C*-isomorphism induces a bijection of
   `Min_alpha`;
5. for a space map `F:X->Y` satisfying
   `F(x.t)=F(x).(ct)`, its contravariant algebra isomorphism
   `Phi=F^*:A_Y->A_X` is typed by

   ```text
   alpha^X_t o Phi = Phi o alpha^Y_{ct};
   ```

   and likewise permutes the minimal invariant ideals; and
6. repeated periods are recovered with their full cardinal multiplicities,
   not by selecting one representative per length class.

The proof must derive the component ideals from intrinsic invariant-ideal
minimality before reading any period label.

## 5. Exact restricted Arveson spectrum

Select one exact Arveson spectrum convention for a strongly continuous
real action on a C*-algebra and state the Fourier-transform sign.  For every
intrinsic minimal invariant ideal `I`, define `Sp(alpha|I)` in that convention.

Under the mixed-circle presentation, prove directly from Fourier modes that

```text
Sp(alpha|A_q)=(2 pi/L_q) Z.
```

The lattice is symmetric, so the final length formula is sign-independent:

```text
L(I)=2 pi/min(Sp(alpha|I) intersect R_{>0}).
```

The existence of the positive minimum and the zero-spectrum branch must be
checked.  Full, strong, point, Connes, and Borchers spectra are not
interchangeable names; only the frozen convention may appear in the theorem.

## 6. Complete strict/scaled/unmarked classification

Define the intrinsic length-multiplicity record

```text
M_{A,alpha}(lambda)
 = card{I in Min_alpha(A):L(I)=lambda}.
```

Fix the same variance: `Phi:A_Y->A_X` is `c`-scaled when
`alpha^X_t Phi=Phi alpha^Y_{ct}`.  The proposed classification package is:

```text
strict equivariant isomorphism
  iff M_A(lambda)=M_B(lambda) for every lambda>0;

globally c-scaled conjugacy
  iff M_A(lambda)=M_B(c lambda) for every lambda>0;

unmarked algebra isomorphism
  does not recover the numerical lengths.
```

Necessity and sufficiency, arbitrary cardinal multiplicities, composition
and inverse laws, and the choice of component bijections must be explicit.
The unmarked loss control must construct circle/algebra isomorphisms for
different positive lengths without smuggling in the time action.

This theorem is the analytic center.  The section-free construction and the
one-circle Fourier calculation alone do not clear standalone review.

## 7. Prime-clock application and minimum control

For the actual periodic-orbit set, use the bare partition

```text
Q_Per=disjoint_union_p Q_p,
L_q=log(p) for every q in Q_p,
```

where every `Q_p` is nonempty and no singleton simplification is allowed.
After intrinsic reconstruction of the minimal ideals and periods, the marked
action recovers the length multiset and hence identifies each numerical
`p=exp(L)` that occurs.  This is a theorem about the standardized marked
real-time owner; it does not imply that replacement Paper 15's bare compact
group `B_p` universally determines `p`.

If one global scale preserves the entire supplied prime-length set, its
scale is one because the set has minimum `log 2`.  This minimum lemma is a
sharp control and contributes no standalone arithmetic credit.  No PNT is
load-bearing unless a separate optional proof actually uses it.

## 8. Claim ledger

| ID | Candidate claim | Phase-1 status |
|---|---|---|
| P16-F1 | Section-free mixed standardization, uniqueness, and equivalence. | MERGED FOUNDATION / UNPROVED |
| P16-F2 | Strict and global-scale isomorphism classification with `W_L`. | MERGED FOUNDATION / UNPROVED |
| P16-A1 | Strong continuity for arbitrary `Q`. | SPECIFIED / UNPROVED |
| P16-A2 | Intrinsic minimal nonzero invariant ideals recover components. | CENTRAL / UNPROVED |
| P16-A3 | Exact restricted Arveson spectrum and period formula. | CENTRAL / UNPROVED |
| P16-A4 | Complete strict/scaled length-multiplicity classification. | CENTRAL / UNPROVED |
| P16-A5 | Unmarked action-forgetting loss theorem. | SPECIFIED / UNPROVED |
| P16-A6 | All-orbit fixed-prime application and minimum control. | SPECIFIED / UNPROVED |

## 9. Source and hostile-review gate

Before proof authorization, independent reviews must audit:

- the exact Arveson primary definition and every cited restriction result;
- arbitrary-index `c0` and strong-continuity domains;
- invariant ideals of arbitrary coproducts and the transitivity argument on
  each component;
- global `c`-scaled variance and its Fourier-spectral scaling direction;
- repeated cardinal multiplicities and Choice;
- comparison with Paper 12's stabilizer reconstruction and Paper 13's
  generic diagonal/corona lemma; and
- nearest precedent for the combined intrinsic classification.

The review must attack the possibility that the full package is only Paper
12 plus elementary Fourier series.  If no substantive analytic conjunction
survives that subtraction, Paper 16 is merged/stopped; it does not consume
the Technical Note slot.

## 10. Controls and nonredundancy

Future controls must include common/heterogeneous/repeated clocks, empty
objects as an excluded type, uncountable-index `c0` finite-tail witnesses,
strict versus global-scale sign/direction negatives, an unmarked dilation,
arbitrary nonprime length sets, and the minimum-lemma control.

Standalone eligibility requires `P16-A1`--`P16-A6` plus the mixed foundation,
a complete source audit, and an independent post-proof finding that the
intrinsic ideal-spectrum classification is not a routine companion
substitution.  Current status:

```text
STANDALONE_PASS=false
STANDALONE_CEILING=FULL_PAPER_PLAUSIBLE
```

## 11. Authorization boundary

This amendment authorizes only independent Phase-1 reviews of the exact
base-plus-amendment tuple.  Proof, deterministic controls, Route A/B,
manuscript, release, Git, archive, and public synchronization remain false.

```text
P16_AMENDED_PROTOCOL_ACTIVE=true
P15_REPLACEMENT_DEPENDENCY=false
OLD_P15_FOUNDATION_MERGED=true
PROOF_AUTHORIZED=false
CONTROLS_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
STANDALONE_PASS=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```
