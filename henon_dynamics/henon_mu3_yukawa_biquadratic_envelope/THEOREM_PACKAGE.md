# HCS-C60 theorem package

Status: **PREFREEZE_CODE_RESULTS_PASS / POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

This file states the integrated theorem and locks its exact premises.
Statements labelled `C60-EXACT-*` have project-local prefreeze machine PASS
and the promoted bytes have an independent `POSTREFRESH_PASS`. Released C59
facts are used only through G0; target-selection pilots are chronology, never
theorem authority. The updated theorem roots and Route semantics also have an
independent `FORMAL_DOCS_PASS`, without authorizing paper or release status.

## 1. Released input and action convention

Let $K/\mathbf Q$ be the C59 normal closure with

$$
G=\operatorname{Gal}(K/\mathbf Q)=W(E_6),\qquad |G|=51840.
$$

Let $H_+$ and $H_-$ be C59's exact embedded order-$162$, index-$320$
subgroups. Their durable arrays are inherited from and byte-rebound to the
released C59 group evidence; their ToM locators $301$ and $303$ do not define
them.

All C60 transport equations use ordinary left composition of label maps on
the $27$ labels. The exact transport target is

```text
x = [1,15,14,13,22,12,27,26,25,7,24,16,17,6,19,18,5,20,4,21,3,2,11,10,9,23,8]
```

Thus $H_3=xH_-x^{-1}$. In GAP's right-labelled permutation syntax the same
carrier is written `Hminus^x`. G1 and G2 must bind this convention and prove

$$
\operatorname{Stab}(x\cdot\operatorname{supp}\eta_-)=H_3\subset N.
$$

## 2. Exact subgroup target

The following one-based image arrays lock the target carriers. The passing
group lane reconstructed them independently, verified them inside the
released $G$, and certified every machine invariant below.

```text
N generators:
[1,18,22,16,17,12,27,8,25,26,23,6,14,13,19,4,5,2,15,21,20,3,11,24,9,10,7]
[15,12,4,14,25,7,10,27,8,6,17,24,11,3,21,26,13,22,5,18,1,20,16,2,19,23,9]
[1,2,19,21,20,3,24,11,9,10,23,15,13,14,22,5,4,18,6,16,17,12,8,27,25,26,7]
[14,10,3,7,4,6,5,8,2,9,11,12,1,13,15,17,27,25,19,21,24,22,23,20,26,18,16]
[18,1,15,4,5,12,7,6,13,14,3,8,26,25,11,16,17,2,22,20,21,23,19,24,10,9,27]
[1,13,16,12,6,5,8,7,9,26,27,4,2,18,17,3,15,14,20,19,22,21,24,23,25,10,11]

H0 generators:
[2,18,23,21,20,11,24,15,26,25,22,3,9,10,19,5,4,1,8,16,17,6,12,27,14,13,7]
[13,9,6,16,27,19,17,23,10,2,8,22,14,1,12,24,20,26,3,7,5,15,11,4,18,25,21]
[15,12,4,14,25,7,10,27,8,6,17,24,11,3,21,26,13,22,5,18,1,20,16,2,19,23,9]
[1,2,19,21,20,3,24,11,9,10,23,15,13,14,22,5,4,18,6,16,17,12,8,27,25,26,7]
[20,5,3,2,9,11,10,8,7,4,6,23,24,21,19,26,18,16,15,13,1,22,12,14,17,27,25]

J generators:
[1,2,6,17,16,19,27,23,9,10,8,22,13,14,12,20,21,18,3,5,4,15,11,7,25,26,24]
[2,18,11,4,5,8,7,12,26,25,15,6,9,10,3,16,17,1,23,20,21,19,22,24,14,13,27]
[3,6,5,2,1,4,18,17,12,8,16,21,15,11,20,14,10,19,7,13,9,24,27,26,23,22,25]
```

The locked invariant table is:

| group | order | index in $G$ | SmallGroup | ToM | core | global normalizer |
|---|---:|---:|---:|---:|---:|---:|
| $N$ | 324 | 160 | `[324,39]` | 327 | 1 | $N$ |
| $H_+$ | 162 | 320 | `[162,11]` | 301 | 1 | $N$ |
| $H_0$ | 162 | 320 | `[162,10]` | 302 | 1 | $N$ |
| $H_3$ | 162 | 320 | `[162,19]` | 303 | 1 | $N$ |
| $J$ | 81 | 640 | not used as a defining locator | 266 | 1 | $N$ |

In addition,

$$
N^{\mathrm{ab}}\cong C_2\times C_2,\qquad [N,N]=J,
\qquad N/J\cong V_4.
$$

Every pair among $H_+,H_0,H_3$ must intersect in $J$ and generate $N$.

## 3. Exact primitive-carrier target

Retain C59's integral roots $\alpha_i$. The implementation must emit exact
carriers for

$$
\mu=\eta_+ + \tau(\eta_+),\qquad
\lambda=\eta_+ +2x(\eta_-),
$$

and the cubic

$$
\xi_0=\sum_{T\in\mathcal T_0}\prod_{i\in T}\alpha_i,
$$

where the locked one-based triple orbit is

```text
{1,2,9}, {1,13,18}, {1,14,25}, {2,10,14}, {2,18,26},
{3,6,12}, {3,11,23}, {3,15,19}, {4,5,21}, {4,7,24},
{4,16,17}, {5,7,20}, {5,16,27}, {6,8,11}, {6,19,22},
{7,17,27}, {8,12,15}, {8,19,23}, {9,10,13}, {9,25,26},
{10,18,25}, {11,15,22}, {12,22,23}, {13,14,26},
{16,20,24}, {17,20,21}, {21,24,27}.
```

The exact target fingerprints at $p=692717$ are:

The formal carrier hashes below use the pilot's declared canonical compact
JSON serialization with zero-based monomial labels; the human-readable arrays
and triples in this document are one-based. A project-local schema must state
the conversion explicitly before comparing hashes.

| object | formal carrier hash | terms / degree | stabilizer / orbit | modular polynomial hash |
|---|---|---|---|---|
| $M$ | `0beb2791f4df4bb56214b6a35384517083f5909004219cc988b6de70f494d17c` | 81 / 2 | 324 / 160 | `b8818888c1ceb83e05d2f2df045e9d6e418f1ea18a5f019d1398e4cd0a59ef6b` |
| $F_0$ | `83f014bb3087708ad6e65c4f61bc92a73172aa649ef573358164c1ae7d9efbc5` | 27 / 3 | 162 / 320 | `ffe9439cd390729bbb0dd7ffa4c6a1045c7fbc9c645e0f37e75c71d1e786e10d` |
| $L$ | `fae69eb91d414d8241bbbee51f4a3fcc91c4f8691090adc5cbb575079d2ea1f5` | 135 / 2 | 81 / 640 | `c82feda40496156b7d006de4e47a1b808b3cf3ffffe4a386652d3e3fa77861f1` |

These locked values are rebound by the passing primitive-resolvent evidence
and the independent integrated checker.

## 4. C60-EXACT-0 through C60-EXACT-7

At the official machine layer, every gate below has status
`PREFREEZE_CODE_RESULTS_PASS`.

### C60-EXACT-0: released-authority rebind

Bind the exact I59/P59 release tuple, complete C59 project inventory, scoped
and full manifests, live/archive Route identity, labelled group and root
carriers, both C58 local filtrations, current Batch target, and protected
guard. Reject arbitrary or certificate-selected paths.

### C60-EXACT-1: common-normalizer lattice and uniqueness

Reconstruct the exact arrays in section 2; prove every group invariant,
transport equality, normalizer, core, intersection, quotient, and generated
group. Replay all $350$ subgroup classes and all eleven C59 collision buckets.
The precise uniqueness claim is: $301/303$ is the only collision whose two
normalizers are conjugate and have index two over both members. No broader
“unique $V_4$” claim is allowed.

### C60-EXACT-2: primitive integral carriers

Reconstruct all three carriers, their exact stabilizers, 160/320/640 formal
orbits, integrality, squarefree split witness, distinct modular values, full
modular coefficient vectors and hashes, and the transported-support equality
$\operatorname{Stab}(x\operatorname{supp}\eta_-)=H_3\subset N$.

### C60-EXACT-3: invariant-degree obstruction

Exhaust the $H_0$ and $N$ point and unordered-pair orbit partitions and prove
that both are equal:

```text
points: 27
unordered pairs: 27, 27, 54, 81, 162
```

Supply the coefficient-orbit argument for every commutative
$\mathbf Q$-coefficient formal polynomial of total degree at most two, then
certify the exact cubic carrier and its stabilizer. This is a formal
coordinate statement, not a claim after quotienting by every relation among
the actual roots.

### C60-EXACT-4: tower, automorphisms, characters, and zeta

Prove the fixed-field lattice, normal closures, automorphism groups, full
permutation-character equality/inequality, rational Brauer relation, and zeta
identity. The bracket relation is an equality in the rational permutation
representation ring, not an isomorphism of finite $G$-sets.

### C60-EXACT-5: absolute and relative arithmetic

Recompute all orbit counts, signatures, signed discriminants, exact absolute
support, and relative discriminant norms. Rebind the C59 twins rather than
re-proving them from a pilot.

### C60-EXACT-6: both complete relative local towers

For both $D_3=140$ and $D_3=206$, enumerate every prime of $M$ and every
factor above it in $F_+,F_0,F_3,L$. Verify all $(g,e,f,d)$ rows, degree,
factor, and different totals, local tower formulas, tame relative ramification,
and branch independence. The branch-selection leaf remains false.

### C60-EXACT-7: independence, sources, scope, and release

Require disjoint producer/checker theorem call graphs, strict schemas and
exact key sets, scalar/structural/type-confusion mutations, independent
evidence rebound, deterministic replay, rollback-atomic promotion,
self-excluding manifests, primary-source and hostile non-salami audits, and
explicit false scope leaves.

## 5. Formally audited integrated theorem

C60-EXACT-0 through C60-EXACT-7 have project-local machine PASS, and this
changed formal package has an independent `FORMAL_DOCS_PASS`. Their written
consequences are:

### Theorem A: biquadratic fixed-field envelope

The fields

$$
M=K^N,\qquad F_i=K^{H_i},\qquad L=K^J
$$

have degrees $160,320,640$ as appropriate, $L/M$ is biquadratic, and
$F_+,F_0,F_3$ are its three quadratic subfields. Their normal closures are
$K$; $F_3$ is $\mathbf Q$-conjugate to the original C59 $F_-$; and

$$
\operatorname{Aut}_{\mathbf Q}(M)=1,\quad
\operatorname{Aut}_{\mathbf Q}(F_i)=C_2,\quad
\operatorname{Aut}_{\mathbf Q}(L)=V_4.
$$

Moreover,

$$
M=\mathbf Q(\mu),\qquad F_0=\mathbf Q(\xi_0),\qquad
L=\mathbf Q(\lambda).
$$

### Theorem B: formal invariant gap and zeta relation

No commutative $\mathbf Q$-coefficient formal polynomial of total degree at
most two in the labelled root variables has stabilizer exactly $H_0$, while
the displayed cubic carrier does. In the rational representation ring,

$$
[G/J]+2[G/N]=[G/H_+]+[G/H_0]+[G/H_3].
$$

Consequently,

$$
\zeta_L(s)\zeta_M(s)^2
=\zeta_{F_+}(s)\zeta_{F_0}(s)\zeta_{F_3}(s)
=\zeta_{F_+}(s)^2\zeta_{F_0}(s).
$$

### Theorem C: exact absolute and relative arithmetic

With C59's definitions of $A$ and $B$:

| field | signature | signed discriminant |
|---|---:|---|
| $M$ | $(16,72)$ | $+3^{308}5^{248}A^{96}B^{80}$ |
| $F_+,F_3$ | $(16,152)$ | $+3^{624}5^{496}A^{192}B^{160}$ |
| $F_0$ | $(0,160)$ | $+3^{632}5^{496}A^{192}B^{160}$ |
| $L$ | $(0,320)$ | $+3^{1264}5^{992}A^{384}B^{320}$ |

All have the inherited exact eight-prime absolute support, and

$$
N_{M/\mathbf Q}\mathfrak d_{F_+/M}=3^8,\quad
N_{M/\mathbf Q}\mathfrak d_{F_0/M}=3^{16},\quad
N_{M/\mathbf Q}\mathfrak d_{F_3/M}=3^8,
$$

$$
N_{M/\mathbf Q}\mathfrak d_{L/M}=3^{32}.
$$

### Theorem D: branch-independent relative local tables

The complete tables in section 6 hold for both retained C59 branches. In
particular, all relative ramification occurs over primes above $3$, and every
relative ramified row has $e=2,d=1$ and is tame. Neither branch is selected.

Theorems A--D are one integrated target; no subset is a licensed fallback.

## 6. Complete relative local target tables

Each line gives a base-$M$ row $(n,e,f,d)$, the relative rows $(g,e,f,d)$ for
$(F_+,F_0,F_3,L)/M$, and its multiplicity.

```text
D3 = ToM 140
(1,1,1,0):    (2,1,1,0) (1,2,1,1) (1,2,1,1) (2,2,1,1)  x4
(3,3,1,5):    (1,2,1,1) (1,2,1,1) (2,1,1,0) (2,2,1,1)  x6
(6,6,1,11):   (2,1,1,0) (2,1,1,0) (2,1,1,0) (4,1,1,0)  x2
(9,9,1,18):   (1,2,1,1) (1,2,1,1) (2,1,1,0) (2,2,1,1)  x2
(9,9,1,18):   (2,1,1,0) (1,2,1,1) (1,2,1,1) (2,2,1,1)  x4
(18,18,1,37): (2,1,1,0) (2,1,1,0) (2,1,1,0) (4,1,1,0)  x4

D3 = ToM 206
(2,1,2,0):    (2,1,1,0) (1,2,1,1) (1,2,1,1) (2,2,1,1)  x2
(6,3,2,5):    (1,2,1,1) (1,2,1,1) (2,1,1,0) (2,2,1,1)  x3
(12,6,2,11):  (2,1,1,0) (2,1,1,0) (2,1,1,0) (4,1,1,0)  x1
(18,9,2,18):  (1,2,1,1) (1,2,1,1) (2,1,1,0) (2,2,1,1)  x1
(18,9,2,18):  (2,1,1,0) (1,2,1,1) (1,2,1,1) (2,2,1,1)  x2
(36,18,2,37): (2,1,1,0) (2,1,1,0) (2,1,1,0) (4,1,1,0)  x2
```

The relative factor totals are $(36,28,36,56)$ and $(18,14,18,28)$.

## 7. Nonclaims and current status

`NO_BAD_EULER_OR_ROOT_NUMBER`.

No decomposition Frobenius, bad Euler factor, epsilon/root number,
holomorphy, automorphy, branch selection, converse local classification,
expanded characteristic-zero coefficient vector, maximal order, class
number, regulator, rational point, motive, RH, or Hilbert--Polya claim is
made.

The exact machine status is
`PREFREEZE_CODE_RESULTS_PASS / POSTREFRESH_PASS`. The official tuple has
code/results/live/scoped counts `13/8/21/20`, two `53`-test cycles, `9310`
payload leaves, `9339/9339/14` value/type/structural mutations,
`6/4/10/2/12` hostile evidence counters, and `39` snapshot checks. It binds:

```text
payload              dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead
certificate          d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518
schema               c7ddb4ff8fa890f9f801d615158c9038299487affa3808f25fe5d73c987791a5
independent check    25bc9c1c656da742359814054b66c05e18a304ca85741776c055152a30a98e44
scoped manifest      f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7
group evidence       dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2
resolver evidence    f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da
source contract      4c484b3532c4604b028f45fc157c261149a7a49ca9631bbcf83f8d1efd1cdb90
G0                   0512db556004edde7c19176bbb35375beaeba89301da53902d5c5d98001cb8a8
official refresh log 5f5d788a1493c16a8eec86ec0cb40bfed2dea72fa2257bddf50eed1be2c43239
```

The historical machine-bound formal aggregate is
`fd76237963d385b79b10b7ea13477173b2cf17261fc47d5b43697379d9b012ca`.
It does not identify these changed post-machine roots. Their new aggregate and
Route semantics have passed independent hostile audit and are externally bound
by the live Route, so exact status is `FORMAL_DOCS_PASS`; paper and release
remain pending and `NOT_RELEASED`. Release promotion is false, and
implementation/provenance commits, the full-project manifest, Route archive,
paper source, and paper PDF remain null or pending.
