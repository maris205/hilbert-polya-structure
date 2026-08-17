# HCS-C60: the biquadratic envelope of the cubic-surface Gassmann twins

Status: **`PREFREEZE_CODE_RESULTS_PASS`; `POSTREFRESH_PASS`;
`FORMAL_DOCS_PASS`; `PAPER_PENDING`; `NOT_RELEASED`.**

`NO_BAD_EULER_OR_ROOT_NUMBER`

This is a layered status. The official code/results tuple and its authorized
refresh plus mandatory nonmutating replay pass. The written theorem bridges
have passed their independent formal-documents audit; no paper or C60 release
is claimed.

## 1. Locked successor

HCS-C60 started from the released HCS-C59 normal extension

$$
K/\mathbf Q,\qquad G=\operatorname{Gal}(K/\mathbf Q)=W(E_6),
\qquad |G|=51840,
$$

and its exact core-free Gassmann subgroups $H_+$ and $H_-$ of order $162$
and index $320$. The target-lock stage specified a transport of $H_-$ into the
normalizer of $H_+$ and the unique collision-table case in which the
transported pair generates a common normalizer having index two over each
member. The official machine tuple now certifies that finite predicate.

With the frozen left action on the labelled $27$-line carrier, let $x$ be the
exact transport, and put

$$
H_3=xH_-x^{-1},\qquad
N=N_G(H_+)=N_G(H_3),\qquad
J=H_+\cap H_3.
$$

The third index-two subgroup of $N$ is denoted $H_0$. The locked target, now
certified at the machine layer, is

$$
|N|=324,\quad |J|=81,\quad J=[N,N],\quad N/J\cong C_2\times C_2,
$$

with ToM locators $301,302,303$ for $H_+,H_0,H_3$, locator $327$ for $N$,
and locator $266$ for $J$. These locators are frozen-version checks, never
definitions; exact one-based permutation arrays were locked in
`THEOREM_PACKAGE.md` and were independently reconstructed by G1. Their
written use has been accepted by the independent formal-documents audit.

## 2. Locked field tower

Define

$$
M=K^N,\qquad F_i=K^{H_i}\ (i\in\{+,0,3\}),\qquad L=K^J.
$$

The machine-certified lattice is

$$
M\subset F_+,F_0,F_3\subset L\subset K,
$$

where $L/M$ is biquadratic and $F_+,F_0,F_3$ are its three quadratic
subfields. The field $F_3=x(F_-)$ is a $\mathbf Q$-conjugate of the original
C59 minus field; the untransported $F_-$ is not asserted to be an embedded
subfield of this particular $L$.

The machine-certified normalizer data give the following automorphism results
accepted by the written formal audit:

$$
\operatorname{Aut}_{\mathbf Q}(M)=1,\qquad
\operatorname{Aut}_{\mathbf Q}(F_i)=C_2,\qquad
\operatorname{Aut}_{\mathbf Q}(L)=C_2\times C_2.
$$

## 3. Primitive integral carriers

Retain C59's integral labelled roots $\alpha_i=L_0d_i$, where $L_0$ is the
leading coefficient of the released line eliminant. C60 uses three new
primitive elements:

$$
\mu=\eta_+ + \tau(\eta_+)\quad (\tau\in N\setminus H_+),
$$

$$
\xi_0=\sum_{\{i,j,k\}\in\mathcal T_0}\alpha_i\alpha_j\alpha_k,
$$

$$
\lambda=\eta_+ +2\eta_3,\qquad \eta_3=x\cdot\eta_-.
$$

The intended exact stabilizers and degrees are

| carrier | stabilizer | field | degree | split-prime coefficient hash |
|---|---:|---:|---:|---|
| $\mu$ | $N$ | $M$ | 160 | `b8818888c1ceb83e05d2f2df045e9d6e418f1ea18a5f019d1398e4cd0a59ef6b` |
| $\xi_0$ | $H_0$ | $F_0$ | 320 | `ffe9439cd390729bbb0dd7ffa4c6a1045c7fbc9c645e0f37e75c71d1e786e10d` |
| $\lambda$ | $J$ | $L$ | 640 | `c82feda40496156b7d006de4e47a1b808b3cf3ffffe4a386652d3e3fa77861f1` |

These values at $p=692717$ first appeared as bounded design-pilot targets.
The official G2 implementation and independent checker now reproduce them;
the pilots remain historical nonauthority input.

## 4. Machine-certified target; formal theorem bridge passed

C60-EXACT-0 through C60-EXACT-7 pass at the official prefreeze code/results
layer. The independent formal-documents audit has accepted the written
implications, so they support the following one theorem-sized result:

1. the unique index-two common-normalizer envelope inside all eleven frozen
   C59 Gassmann collisions;
2. the fixed-field lattice and the primitive identities
   $M=\mathbf Q(\mu)$, $F_0=\mathbf Q(\xi_0)$, and
   $L=\mathbf Q(\lambda)$;
3. the formal invariant-degree gap: every commutative
   $\mathbf Q$-coefficient polynomial of total degree at most two fixed by
   $H_0$ is fixed by $N$, while the selected cubic has stabilizer $H_0$;
4. the rational permutation-character relation

   $$
   [G/J]+2[G/N]=[G/H_+]+[G/H_0]+[G/H_3]
   $$

   and hence

   $$
   \zeta_L(s)\zeta_M(s)^2
   =\zeta_{F_+}(s)\zeta_{F_0}(s)\zeta_{F_3}(s)
   =\zeta_{F_+}(s)^2\zeta_{F_0}(s);
   $$

5. exact signatures, signed discriminants, eight-prime absolute support, and
   relative discriminant norms $3^8,3^{16},3^8,3^{32}$; and
6. complete relative local tables for both retained C59 branches, with no
   branch selection.

Nothing in this list is certified merely because a target-selection pilot
passed. The independent machine tuple now supplies the finite premises, but
the independent written audit supplies `FORMAL_DOCS_PASS`.

## 5. Canonical G0--G7 map

- G0: final C59 release, Batch, Route/archive, manifests, carriers, and guard
  rebind;
- G1: durable common-normalizer lattice and exhaustive eleven-bucket
  uniqueness;
- G2: primitive integral carriers, exact stabilizers, and split-prime
  noncollision;
- G3: formal quadratic obstruction and exact cubic escape;
- G4: fixed fields, automorphisms, characters, Brauer relation, and zeta
  identity;
- G5: signatures, absolute discriminants/support, and relative discriminant
  norms;
- G6: both complete relative local towers and branch independence;
- G7: independent implementation, strict schemas, mutations, manifests,
  sources, scope, hostile review, and atomic promotion.

All eight machine gates now have `PREFREEZE_CODE_RESULTS_PASS`; the authorized
refresh and mandatory live replay have `POSTREFRESH_PASS`. These statuses do
not substitute for the separate written formal audit, which has now passed.

## 6. Official inventories and historical target-lock input

The formal-root topology matches C59 and contains exactly these 13 Markdown
files:

```text
DERIVATION.md
EXPERIMENT_PLAN.md
EXPERIMENT_TRACKER.md
IMPLEMENTATION_CHECKLIST.md
INTEGRITY_REPORT.md
METHODOLOGY_BLUEPRINT.md
NARRATIVE_REPORT.md
PAPER_PLAN.md
PROOF_PACKAGE.md
README.md
RESEARCH_QUESTION.md
SOURCE_AUDIT.md
THEOREM_PACKAGE.md
```

The official machine inventory is exact. `code13` is:

```text
code/README.md
code/c60_atomic_promote.py
code/c60_checker.py
code/c60_checker_group.g
code/c60_checker_resolvent.py
code/c60_exact.py
code/c60_group.py
code/c60_hash_manifest.py
code/c60_pipeline.py
code/c60_producer.py
code/c60_resolvent.py
code/run_all.sh
code/test_c60.py
```

`results8` is:

```text
results/RESULTS.md
results/TEST_REPORT.md
results/c60_certificate.json
results/c60_check_report.json
results/c60_group_evidence.json
results/c60_resolvent_evidence.json
results/c60_schema.json
results/scoped_hash_manifest.json
```

The self-excluding manifest covers the exact other 20 files (`scoped20`), and
the complete live code/results inventory including that manifest is exactly
21 files (`live21`). Its SHA-256 is
`f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7`.

The official refresh and mandatory nonmutating replay each ran the identical
$53/53$ test suite, producer, independent checker, all eight G0--G7 gates,
and post-checker counter validation. Both runs report $9{,}310$ payload scalar
leaves; $9{,}339$ value, $9{,}339$ type, and $14$ structural mutations; actual
hostile rebound counts $6/4/10/2/12$ for group/resolver/self-consistent
evidence/additional artifact/total; and $39$ child snapshot rebind checks.
The official refresh transcript SHA-256 is
`5f5d788a1493c16a8eec86ec0cb40bfed2dea72fa2257bddf50eed1be2c43239`;
the transcript is an external execution record, not a `live21` member.

| bound object | SHA-256 |
|---|---|
| canonical payload | `dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead` |
| certificate | `d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518` |
| schema | `c7ddb4ff8fa890f9f801d615158c9038299487affa3808f25fe5d73c987791a5` |
| independent check report | `25bc9c1c656da742359814054b66c05e18a304ca85741776c055152a30a98e44` |
| scoped manifest | `f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7` |
| group evidence | `dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2` |
| resolver evidence | `f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da` |
| official refresh log | `5f5d788a1493c16a8eec86ec0cb40bfed2dea72fa2257bddf50eed1be2c43239` |

Before integrated assembly, two bounded component tuples were frozen under
`PROJECT_LOCAL_EVIDENCE_FROZEN_MACHINE_ASSEMBLY_PENDING`. They remain part of
the exact target-lock chronology; the official tuple now independently
reproduces their evidence hashes:

| component | files / bytes | aggregate | producer | independent checker | evidence |
|---|---:|---|---|---|---|
| group | 10 / 248,016 | `dfd7d16a0128eae7a64906a4449a3022772dbc277abaae8187b6208340302464` | `fd3e75913db3cf5d71f7fd95a3e260edae19bc53a748767f28773d008121536b` | `4338ad0e2af9a0fe096cbb6514de6c8d5227386a2ffadeac487a858fb160dde3` | `dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2` |
| primitive-resolvent | 12 / 140,873 | `9ceda190badd260008fcb37788afd5f2a3e3457ca9e1e452f3999df24c12fe97` | `61b157e8c3e5a68bf304f9499bc176f60fe16bf7c5e5f6d021fbec17d7d9465e` | `5f4070831d4734ba3be93ae578d7a2be893f46676ab40cdaa4a2de6b8d3fb672` | `f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da` |

Those preassembly component tuples were not a complete machine assembly or
theorem authority. Likewise, the external adaptive scan and Pilot A/B tuple
record target-selection chronology only and must never be promoted as C60
theorem authority. The 13 roots, live Route, and Batch update formed the
integrated `TARGET_LOCK_FORMAL_INPUT` layer used by the now-passing machine
tuple; their historical role does not make them theorem authority.

## 7. Hard scope firewall

C60 makes no bad Artin Euler-factor, decomposition Frobenius, local epsilon,
local/global root-number, Artin-holomorphy, automorphy, expanded
characteristic-zero coefficient, integral-basis, maximal-order, monogenicity,
class-number, regulator, rational-point, Hasse-principle, weak-approximation,
Brauer--Manin, motive, RH, or Hilbert--Polya claim. It does not select
$D_3=140$ or $D_3=206$, and it does not infer an individual high-degree
local field from an $(n,e,f,d)$ row.

## 8. Current boundary

C59 is `RELEASE_FROZEN` at I59
`6c806120f17dab2e7b0bca37fcc156dfc459a4b7` and P59
`961c45f4b0c66ec94d2f069fd9ecc9d4b529d03a`. C60 chronology is now:

1. adaptive target selection and Pilot A/B design evidence;
2. independent non-salami review and `TARGET_LOCK_FORMAL_INPUT` lock;
3. frozen group and primitive-resolvent component evidence;
4. source-stable integrated `PREFREEZE_CODE_RESULTS_PASS` tuple; and
5. authorized refresh plus mandatory live replay with `POSTREFRESH_PASS`; and
6. independent post-machine formal hostile audit with `FORMAL_DOCS_PASS`.

The next gate is separate paper authorization. A paper, paper audit,
implementation/release commits, Route archive, and C60 release do not yet
exist. The honest handoff is
`FORMAL_DOCS_PASS / PAPER_PENDING / NOT_RELEASED`.
