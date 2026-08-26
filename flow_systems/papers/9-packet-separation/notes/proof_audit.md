# Paper 9 Phase-3 rigorous topology proof audit

Audit date: 2026-08-14 (Asia/Shanghai)  
Proof object: `DEN-EF-PACKET-QUOTIENT-TOPOLOGY-P`  
Primary verdict: **CONFIRM_STRONG**  
Proof findings: **0 Critical / 0 Major / 0 Minor**  
Route-B invocation: **false**

## 1. Exact lock and evidence binding

This proof audit is bound to the following exact Phase-1 tuple:

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `895b2357d4815d295a8a63f1b6a0c412aaf5afdc34e715b2607d5d25945ad49e` |
| `notes/candidate_lock.md` | `0e0e2f5e7a557baaf91cf6ca1abf4d17e0743a56d2d30f1364188d853f8f3ded` |
| `notes/phase1_design_amendment.md` | `b3a7143b6b213501869467ac78090a6d8ae433f6137185fc6537d99698120cbb` |
| `notes/phase1_amended_relock.md` | `0e18c1de19a56c988ae17a88859493a238291a2264c012dc09d4e77db688e346` |
| `notes/phase1_methodology_relock.md` | `936b17eb465697414371dd95b691ee9179d2706496e6303b868e366ab97cb88b` |

The exact Phase-2 evidence packet is:

| Artifact | SHA-256 |
|---|---|
| `notes/source_audit.md` | `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` |
| `notes/sources/paper9_source_manifest.md` | `8dd678dc33fa7396484c8c8d63a91943f6755da24eedefa0471860fa94e42906` |
| `notes/sources/paper9_sources.sha256` | `6413af8f2d0afec7158aec123f32a641776edcef0a9a9e747fd0ebc5c5f697e4` |

The checksum ledger verifies **14/14** retained PDFs and preflight sidecars.
No source PDF is modified or licensed for public redistribution by this audit.

### Source-owned inputs and their ceiling

The proof uses the following Deninger inputs from `P9-DEN-DYN-v4`:

- physical p. 32, equation (35): finite-kernel fixed-`p` characters have a
  unit exponent and positive-integer factor;
- physical p. 32, equation (38), and physical p. 33, equation (39): exact
  `Q_{>0}`-equivariant **set bijections** and set-level packet fibration;
- physical pp. 38--39, Section 6 and Theorem 6.1: suspension, right action,
  packet, and exact stabilizer `p^Z`;
- physical p. 43, Proposition 7.4: the initial colimit stage is open and the
  pre-suspension Frobenius maps are homeomorphisms;
- physical pp. 44--45, Propositions 7.6--7.7 and Corollaries 7.8--7.9:
  pointwise/quotient/colimit topology and pre-suspension Hausdorffness;
- physical pp. 46--47, Theorem 7.10, its Remark 2, and the following
  admissible-`E` paragraph: the topology applies to `E_f`, while the displayed
  suspension coordinates are not homeomorphisms in general.

The proof does **not** import topology through equations (38)--(39). Deninger's
survey `P9-DEN-SUR-v1`, physical pp. 11--13, calls packets/orbits compact but
does not add Hausdorffness and again warns that the continuous bijection need
not be a homeomorphism.

For the comparison audit, Morishita `P9-MOR-v5`, physical p. 5 equation
(1.1.5), physical pp. 23--25 Lemmas 3.4--3.5 and Theorem 3.6, supplies the
adelic target and continuous anti-equivariant map subject to the exact `E_f`
repair below. It does not supply an inherited-to-standard-circle
homeomorphism. Connes--Consani's intrinsic scaling-topos circle
`CC-SCALING-Cp` and the naive adelic quotient subspace are kept distinct, as
required by `source_audit.md:177-202`.

## 2. Frozen object and notation

Fix one rational prime `p`. Put

```text
A_p = product_{ell != p} Z_ell,
U_p = A_p^x,
H_p = p^{Zhat} subset U_p,
D_p = Z[1/p]_{>0}.
```

Let `G_p=Fbar_p^x`. Fix an injective character `chi:G_p -> C^x`. For
`a in A_p`, exponentiation is interpreted elementwise: on an element of order
`N` it uses the residue of `a` modulo `N`. Every such `N` is prime to `p`.

The three source levels remain distinct:

```text
Ptilde_a = (x_p,chi^a)       raw character point,
P_a      = pi_G(Ptilde_a)    Galois-orbit point,
j(P_a)                       point in Xcheck=Xcheck_0(C)_{E_f}.
```

Write

```text
Y       = Xcheck x R_{>0},
Z_p     = C_p^{E_f} x R_{>0} subset Y,
(P,u)q  = (F_qP,q^{-1}u),
rho     : Y -> Y/Q_{>0},
rho_p   : Z_p -> Gamma_p.
```

The relation `R_p` is the orbit relation of this exact right action on `Z_p`.
No claim below concerns the full-character Morishita source, the standard
circle proxy, the intrinsic scaling-topos circle, the generic adelic
suspension, or the full global Deninger suspension unless named explicitly.

## 3. The inherited packet topology is the restricted quotient topology

### Lemma 3.1 — openness of the global orbit quotient

The map `rho:Y -> Y/Q_{>0}` is open.

**Proof.** Proposition 7.4 and the admissible-`E` extension make each `F_q` a
homeomorphism on `Xcheck`; multiplication by `q^{-1}` is a homeomorphism on
`R_{>0}`. Hence every right translation on `Y` is a homeomorphism. For an open
set `V subset Y`,

```text
rho^{-1}(rho(V)) = union_{q in Q_{>0}} Vq,
```

which is open. By the definition of quotient topology, `rho(V)` is open.
QED.

### Lemma 3.2 — saturated restriction

`Z_p` is saturated, `rho_p` is open, and the canonical bijection

```text
Z_p/R_p -> rho(Z_p)=Gamma_p
```

is a homeomorphism. Thus `Z_p/R_p` has exactly the topology inherited by
`Gamma_p` from the global suspension.

**Proof.** Deninger's equation (38) is `Q_{>0}`-equivariant and identifies the
fixed-prime packet fibre set; equivalently `C_p^{E_f}` is invariant under every
`F_q`. Invariance under the group and its inverses makes `Z_p` saturated.

If `O subset Z_p` is relatively open, write `O=V intersect Z_p` with `V` open
in `Y`. Saturation gives

```text
rho_p(O)=rho(V) intersect rho(Z_p).
```

Lemma 3.1 makes the right side open in the subspace `rho(Z_p)`. Therefore
`rho_p` is an open quotient map. Its fibres are exactly the `R_p` classes, so
the induced continuous bijection from `Z_p/R_p` is open and hence a
homeomorphism. QED.

This closes the formerly conditional topology arrow before any exponent
coordinate is used.

## 4. P9-1: constructive simultaneous real/profinite density

### Theorem 4.1 — exact density theorem

The diagonal embedding

```text
D_p -> R_{>0} x A_p,
q   |-> (q,q)
```

has dense image. More precisely, for every `c>0` and `a in A_p` there is a
sequence `q_j=m_j/p^{k_j}` with `m_j in N`, `k_j>=0`, such that

```text
q_j -> c in R_{>0},
q_j -> a in A_p.
```

**Proof.** Enumerate the primes different from `p` as
`ell_1,ell_2,...` and set

```text
M_j = product_{i=1}^j ell_i^j.
```

Then `(M_j)` is cofinal among positive moduli prime to `p`: every prime power
`ell^r`, `ell!=p`, divides all sufficiently late `M_j`. Let `a_j` be the image
of `a` in `Z/M_jZ`.

Choose `k_j` so large that

```text
M_j/(2p^{k_j}) < 1/j,
cp^{k_j} > M_j.
```

Because `p` is invertible modulo `M_j`, impose the congruence on the rational
number itself by choosing

```text
m_j = a_j p^{k_j} (mod M_j).
```

Among the integers in this residue class choose one nearest to `cp^{k_j}`.
The second inequality ensures it is positive, and the spacing of the
arithmetic progression gives

```text
|m_j-cp^{k_j}| <= M_j/2,
|m_j/p^{k_j}-c| < 1/j.
```

Thus the real convergence holds. In `Z/M_jZ`,

```text
q_j=m_j p^{-k_j}=a_j.
```

For every `ell!=p` and `r>=1`, eventual divisibility `ell^r | M_j` gives
`q_j=a (mod ell^r)`. Hence `q_j->a` in every `Z_ell`, and therefore in the
product `A_p`. QED.

The argument uses additive CRT on the exact rational residue. It neither
asserts multiplicative strong approximation in finite ideles nor infers
`q_j->a` from `m_j->a`.

## 5. P9-2: fixed-stage finite-kernel character convergence

### Lemma 5.1 — every approximant remains in `E_f`

Let `b in U_p` and `q=m/p^k in D_p`. Then `chi^{bq}` has finite kernel.

**Proof.** Write `m=p^s m'` with `(m',p)=1`. Multiplication by `b`, by
`p^s`, and by `p^{-k}` are automorphisms of `G_p`. Multiplication by `m'` has
kernel the finite group of `m'`-torsion elements. Hence the exponent map
`bq` and the character `chi^{bq}` have finite kernel. QED.

### Lemma 5.2 — pointwise convergence in one fixed raw fibre

Let `b,d in U_p` and let `q_j in D_p` converge to `d` in `A_p`. Then

```text
chi^{bq_j} -> chi^{bd}
```

pointwise on `G_p`, with all source and limit characters in the same initial
fixed-`p`, `E_f` raw-character fibre.

**Proof.** For `zeta in G_p`, put `N=ord(zeta)`. Since `p` does not divide
`N`, convergence in `A_p` implies `q_j=d (mod N)` eventually. Multiplication
by the fixed `b` preserves that congruence, so

```text
chi(zeta)^{bq_j}=chi(zeta)^{bd}
```

eventually. This is pointwise convergence. Lemma 5.1 puts every approximant in
`E_f`; `bd` is a unit, so the limit is injective and also lies in `E_f`.
No colimit stage varies: rational powers of `p` act as inverse Frobenius on
the same residue group. QED.

### Proposition 5.3 — legal source-topology passage

Under the same hypotheses,

```text
P_{bq_j} -> P_{bd},
j(P_{bq_j}) -> j(P_{bd}) in Xcheck.
```

Moreover `j(P_{bq_j})=F_{q_j}j(P_b)` at the source-action level.

**Proof.** First use Lemma 5.2 in the pointwise topology of the one raw fibre.
Then apply, in order, the continuous Galois quotient and the continuous open
initial-stage inclusion supplied by Deninger Proposition 7.4 and the Section-7
`E_f` extension. Equivariance gives the displayed action identity. QED.

The equality

```text
F_{m/p^k}(P_b)=F_m(P_b)
```

is also valid at the Galois/packet point because `p^Z` is the exact stabilizer,
but it was not used to prove convergence. The generally false raw equality
`chi^{bmp^{-k}}=chi^{bm}` is nowhere asserted.

For `d outside U_p`, Theorem 4.1 remains true but Proposition 5.3 earns no
`E_f` endpoint credit unless `chi^{bd}` independently has finite kernel.

## 6. Unit-exponent exhaustiveness and exact set equivalence

### Lemma 6.1 — unit normalization

Every point of `Gamma_p` has a representative `[j(P_a),u]` with
`a in U_p` and `u>0`.

**Proof.** Deninger equation (35) represents every finite-kernel character in
the fixed fibre by an exponent `a nu`, with `a in U_p` and `nu in N`. Powers
of `p` may be absorbed into the unit `a`, so `nu` may be taken prime to `p`.
At the exact source-action level `P_{a nu}=F_nu(P_a)`, and

```text
(j(P_a),nu u) nu = (j(P_{a nu}),u).
```

Thus `[j(P_{a nu}),u]=[j(P_a),nu u]`. Equations (38)--(39) and the suspension
set bijection show that these normalized representatives exhaust the packet.
No topology is transported through those set bijections. QED.

### Lemma 6.2 — equivalence of normalized representatives

For `a,b in U_p` and `u,v>0`,

```text
[j(P_a),u]=[j(P_b),v]
```

if and only if

```text
b a^{-1} in H_p,
u/v in p^Z.
```

**Proof.** Equality of suspension classes gives `q in Q_{>0}` with
`v=q^{-1}u` and `F_q(P_a)=P_b`. Since both endpoint characters are injective,
the image of `q` in every `Z_ell`, `ell!=p`, must be a unit. A positive
rational number with zero valuation at every `ell!=p` is `p^n` for some
`n in Z`. The Galois quotient identifies the remaining exponent precisely
modulo `H_p=p^{Zhat}`. Hence the two displayed conditions are necessary.
Equivalently, this is exactly the class relation in Deninger's
`Q_{>0}`-equivariant balanced-product bijection (38), rewritten as (39); that
set theorem is the decisive colimit-level check. The conditions are sufficient
by the same Galois identification and exact `p^Z` time stabilizer. QED.

Consequently there is a chosen **set** bijection

```text
Gamma_p  <->  (U_p/H_p) x (R_{>0}/p^Z),
```

but no product topology has been used or obtained.

## 7. P9-3 and P9-4: universal constant-class convergence

### Theorem 7.1 — arbitrary specialization in the actual packet

For every ordered pair `x,y in Gamma_p`, the constant sequence

```text
x,x,x,...
```

converges to `y` in the actual inherited topology.

**Proof.** By Lemma 6.1 choose

```text
x=[j(P_b),u],
y=[j(P_a),v],
a,b in U_p, u,v>0.
```

Apply Theorem 4.1 to

```text
c=u/v in R_{>0},
d=a b^{-1} in U_p.
```

It yields `q_j=m_j/p^{k_j}` such that `q_j->u/v` in `R_{>0}` and
`q_j->ab^{-1}` in `A_p`. In the exact prequotient put

```text
z_j=(F_{q_j}j(P_b),q_j^{-1}u).
```

Proposition 5.3 and ordinary real convergence give

```text
z_j -> (j(P_a),v) in Z_p.
```

Every `z_j` is the right translate `(j(P_b),u)q_j`, so
`rho_p(z_j)=x` for all `j`. Continuity of `rho_p` gives the claimed convergence
of the constant quotient sequence to `y`. QED.

### Corollary 7.2 — packet indiscreteness

`Gamma_p` is indiscrete. It is non-`T0`, non-`T1`, and non-Hausdorff.

**Proof.** Theorem 7.1 says `y in closure({x})` for all ordered pairs `x,y`.
Thus every nonempty closed set is all of `Gamma_p`, equivalently the only open
sets are the empty set and `Gamma_p`.

The packet has more than one point: fix `a` and choose `u/v` outside `p^Z`;
Lemma 6.2 makes the corresponding points distinct. Therefore the indiscrete
space is not `T0`, and hence not `T1` or Hausdorff. QED.

### Corollary 7.3 — every actual inherited periodic orbit

Every actual periodic orbit in `Gamma_p`, with its inherited subspace
topology, is a nontrivial indiscrete space. In particular it is not a
Hausdorff standard circle.

**Proof.** Every subspace of an indiscrete space is indiscrete. The exact
stabilizer `p^Z` makes the orbit set `R_{>0}/p^Z`, which has more than one
point. QED.

The stronger direct orbit proof is obtained from Theorem 7.1 by taking
`a=b`; then the approximants have profinite target `1` and arbitrary positive
real target `u/v`.

### Corollary 7.4 — the intrinsic orbit quotient `Q_p`

Let `K_p=R_{>0}/p^Z` act through the source flow and let

```text
Q_p=Gamma_p/K_p
```

have the quotient topology. Then `Q_p` is indiscrete and nontrivial, hence
non-`T0`, non-`T1`, and non-Hausdorff. Set-theoretically it is the chosen
quotient `U_p/H_p`; it is not thereby the topological group `B_p`.

**Proof.** A surjective quotient of an indiscrete space is indiscrete. The
set statement follows from Lemma 6.2 by removing the time coordinate.

For nontriviality, `H_p` is procyclic because it is the continuous image of
`Zhat`; a procyclic profinite group has at most one element of order two.
Choose two distinct odd primes different from `p`. Independent sign choices
in their `Z_ell^x` coordinates give `U_p` at least three distinct nonidentity
elements of order two. Hence `H_p` is a proper subgroup of `U_p`, so
`U_p/H_p` has more than one point. QED.

### Topological property ledger

For each of `Gamma_p`, every inherited orbit, and `Q_p`:

- the space is quasi-compact and locally quasi-compact in the open-cover
  sense, because its only nonempty open set is the whole space;
- it is second countable, with basis consisting of the whole space;
- its Borel sigma-algebra is trivial;
- every continuous map to a `T0` space, in particular to a Hausdorff space,
  is constant; and
- it is not LCH in the project's frozen locally-compact-Hausdorff sense.

This does not assert failure of every convention for non-Hausdorff local
compactness.

## 8. P9-6: the restricted equivalence relation is not closed

### Theorem 8.1 — explicit nonclosed-relation sequence

The relation `R_p subset Z_p x Z_p` is not closed.

**Proof.** Fix a unit exponent `b`, choose `u,v>0` with `u/v notin p^Z`, and
put

```text
w =(j(P_b),u),
w'=(j(P_b),v).
```

Lemma 6.2 says `rho_p(w)!=rho_p(w')`. Apply Theorem 4.1 with real target
`u/v` and profinite target `1`, and put `w_j=wq_j`. Then

```text
(w,w_j) in R_p for every j,
(w,w_j) -> (w,w') in Z_p x Z_p.
```

If `(w,w')` belonged to `R_p`, their quotient points would be equal, contrary
to the choice. Thus the limit is outside `R_p`. QED.

This is a relation theorem on the exact restricted prequotient, not an analogy
from Deninger's adelic target or from a different dense diagonal action.

## 9. P9-5: set models versus actual topological models

### 9.1 Deninger coordinates

The Deninger set bijection

```text
(U_p/H_p) x (R_{>0}/p^Z) -> Gamma_p
```

cannot be a homeomorphism when the left side has its standard compact-group
times Hausdorff-circle topology: that domain is Hausdorff and nontrivial,
whereas Corollary 7.2 makes the actual target indiscrete and non-`T0`.
Likewise, the standard circle parametrization of an individual orbit is a set
and flow parametrization only, not an inherited-topology homeomorphism.

This realizes, rather than contradicts, Deninger's Theorem 7.10 Remark 2 and
Section-10 warning that continuous bijective slices need not be inherited
homeomorphisms.

### 9.2 The naive adelic inherited prime orbit

Define this subsection's object exactly as

```text
X_Q^{naive}=Q^x\A_Q/Zhat^x
```

with the double-quotient topology, and let `C_p^{naive}` have the inherited
subspace topology. For `r>0`, let `e_p(r)` be the adele with component `0` at
`p`, component `1` at every finite `ell!=p`, and infinite component `r`.

### Theorem 9.1 — the naive inherited adelic `C_p` is indiscrete

For all `r,s>0`, the constant sequence represented by `[e_p(r)]` converges to
`[e_p(s)]` in `C_p^{naive}`. Hence this actual inherited subspace is
indiscrete.

**Proof.** Put `c=s/r` and apply Theorem 4.1 with any unit target
`a=(a_ell) in U_p` (target `a=1` suffices). For the resulting `q_j`,

```text
q_j e_p(r) -> alpha
```

in the adele ring, where

```text
alpha_p=0,
alpha_ell=a_ell for ell!=p,
alpha_infinity=s.
```

Every `q_j e_p(r)` represents exactly `[e_p(r)]`, because `q_j in Q^x` acts
on the left. Let `epsilon in Zhat^x` have `p`-component `1` and
`ell`-component `a_ell^{-1}` for `ell!=p`. Then

```text
alpha epsilon=e_p(s).
```

Continuity of the quotient map therefore makes the constant quotient sequence
`[e_p(r)]` converge to `[e_p(s)]`.

Finally, `[e_p(r)]=[e_p(s)]` holds exactly when `s/r in p^Z`: equality forces
a rational left multiplier to have valuation zero at every `ell!=p`, hence to
be `+p^n`, and the converse is immediate. The orbit is nontrivial. Applying
the arbitrary ordered-pair argument proves indiscreteness. QED.

This theorem applies to `MOR-CC-Cp-INHERITED` and
`CC-NAIVE-XQ-Cp-INHERITED` only insofar as those labels mean this exact naive
double quotient with its quotient-subspace topology.

It does **not** apply to:

- `MOR-CC-Cp-STD-CIRCLE-PROXY`, which is Hausdorff by definition; or
- `CC-SCALING-Cp`, the intrinsic scaling-topos point subspace proved
  topologically isomorphic to the ordinary circle by Connes--Consani Lemma
  6.3(i).

The canonical set bijection between scaling-topos points and the natural
adelic quotient is therefore not a topology-transport theorem. Connes--Consani
mapping-torus or proper replacement results retain their exact intrinsic or
replacement ownership.

### 9.3 Corrected Morishita bridge

On Deninger's exact `E_f` orbit, equation (35) gives exponent `a nu` with
`a in U_p`. Under Morishita's continuous character-to-adele map, its
away-`p` components are `nu a_ell`, hence nonzero. Diagonal multiplication by
`nu^{-1}` followed by the away-`p` unit normalization used in Theorem 9.1
places the class in `C_p^{naive}`. This repairs the missing nonvanishing check
in the printed full-character proof without enlarging the domain.

Morishita Lemmas 3.4--3.5 give continuity and flow anti-equivariance. Orbitwise
surjectivity plus the equal exact stabilizer `p^Z` gives a bijection from each
actual Deninger orbit to `C_p^{naive}`. Corollary 7.3 and Theorem 9.1 make both
sides nontrivial indiscrete spaces, so this actual-to-actual bijection is a
homeomorphism.

The Paper-8 contradiction is now exact: its compact-to-Hausdorff step typed
the target as the ordinary circle. The actual inherited-to-actual inherited
map may remain a homeomorphism, but it is a homeomorphism of indiscrete
spaces, not of Hausdorff circles.

## 10. P9-7: groupoid and completion consequence

### Proposition 10.1 — standard LCH-Hausdorff route is refuted

The actual packet and actual inherited-orbit transformation groupoids cannot
be Hausdorff groupoids in the frozen standard LCH-Hausdorff framework.

**Proof.** The unit space of a Hausdorff topological groupoid is a Hausdorff
subspace. Corollaries 7.2--7.3 show that the actual unit spaces are nontrivial
and non-Hausdorff. Thus the Hausdorff prerequisite fails before Haar,
completion, disintegration, representation, or trace transport. QED.

Jüstel's strongly proper lcH disintegration theorem is therefore inapplicable
to the actual packet under the proved topology. This result does not say that
no non-Hausdorff groupoid, Haar system, C*-algebra, or trace theory can ever be
defined. Constructing such a replacement is a separately locked project.

## 11. P9-8: adversarial controls

### 11.1 Exact deterministic execution binding

The finite control packet is bound to
`results/packet_separation_manifest.json`, SHA-256
`52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668`.
It records eight CSV artifacts with **240 data rows** total. Its implementation
ledger includes, among other files:

```text
code/packet_separation_controls.py
  6a2acfa84c3dbf1b3c8969dfcd2a8cca7fe1db956a80874715c7878ed1d6a6e7
code/test_packet_separation_controls.py
  aad1cd822aa2f9febb50794577f6cc71508ad81583601c5d2fe34c7792e29a55
experiments/reproduce.sh
  56520434a8fe450b1e7ea89bb2044a33cb05ba0f77a9545da8dec3b07dd9e14a
```

With `PYTHONDONTWRITEBYTECODE=1`, the unit suite passed **20/20** tests. The
documented `--verify-only` path then passed all CSV hashes, byte sizes, row
counts, metric recomputation, active-lock hashes, and implementation hashes,
reporting:

```text
PASS: 240 CSV rows;
max real error=6.5383536556262208e-06;
max character error=0;
max correct-time error=7.7964676432670538e-05
```

`--verify-only` rewrites no artifact. The generator and full reproduction
runner are implementation/reproducibility tools, while the verify-only result
is a tamper/regression check. Neither execution mode proves an infinite
density, source-topology, quotient-separation, Paper-8 supersession, or Route
claim; those conclusions are owned only by Sections 3--10 and 12--14 of this
audit.

### 11.2 Control adjudication

| Control | Exact result | What it prevents |
|---|---|---|
| rational residue | the proof enforces `m_j=a_jp^{k_j} (mod M_j)`, so it is `q_j`, not merely `m_j`, that has the target residue | numerator-gauge error |
| finite CRT truncation | one modulus proves one cylinder hit only; cofinal `(M_j)` is required | finite computation promoted to density |
| `E_f` domain | each approximant has explicitly finite kernel; arbitrary infinite-kernel `A_p` limits receive no endpoint credit | ambient/full-character splice |
| action sign | for `(P,u)q=(F_qP,q^{-1}u)`, the real target is `u/v`; under the deliberately wrong sign it would be `v/u` | orientation mistake; the wrong sign is not expected to restore separation |
| stabilizer level | `F_{m/p^k}(P)=F_m(P)` is quotient-only and unused in fixed-stage convergence | false raw-character equality |
| distinctness | `u/v notin p^Z` gives an explicit unequal pair; transverse equality is checked modulo `H_p` | multiple limits stated without distinct points |
| `p^Z`-only suspension | logarithmic time gives `R/(log p)Z`; the translation subgroup is discrete and the quotient is a Hausdorff circle | mechanism falsely applied without the dense real/profinite channel |
| standard circle proxy | remains Hausdorff by definition and is never used as the inherited orbit | actual/proxy conflation |
| Deninger generic adelic quotient | source physical pp. 64--65 gives a related irreducible but `T1` quotient because its orbits are closed | “dense diagonal always means indiscrete” |
| Le Bruyn formal topology | the peer-reviewed finite-adele-class quotient is coarse but non-indiscrete; the corrected old-arXiv claim is excluded | unrelated quotient promoted to this packet |
| intrinsic scaling `C_p` | remains the source-owned Hausdorff circle on its own object | naive quotient and scaling-topos topology splice |

The proof is therefore specific to the fixed-prime rational-Witt `E_f`
packet and the exact diagonal `D_p` channel. It does not prove every arithmetic
suspension, every adelic quotient, or the full global Deninger space
indiscrete.

## 12. P9-9: Paper-8 dependency correction

The following exact Paper-8 historical bytes were checked:

| Artifact | SHA-256 |
|---|---|
| `phase2_source_topology_audit.md` | `f76dc87df56bacc54ea420447b28cb37020fc2625fa97d2eca2f173278ee83a3` |
| `phase3_topology_ownership_proofs.md` | `209989444b48a625777c0c4626b92429ed08b58f3dc4c31b03f7d23b067dca14` |
| `proof_audit.md` | `1bbcc8f7faadb331ff0840c26472ee16722894b6dff2cae2687216e4638a5990` |
| `stage8_summary_zh.md` | `4aede4aaac2161350786a1c29991565c569d0d3bd41ad6769ba6ec5a2c618771` |

The failed premise first appears in Paper 8
`phase2_source_topology_audit.md:203-239`, especially `:232-239`: Morishita's
set-level `R_{>0}/p^Z` identification is silently given the Hausdorff standard
circle topology, and compact-to-Hausdorff is then used for inverse continuity.
It propagates to `phase3_topology_ownership_proofs.md:65-70,82-102` and to
`proof_audit.md:74-80,84-99,464-473`.

The versioned correction matrix is:

| Paper-8 branch | Paper-9 status | Preserved content |
|---|---|---|
| actual inherited orbit is a compact Hausdorff standard circle | **REFUTED** by Corollary 7.3 | source orbit set, exact `p^Z` stabilizer, flow sign, prime label, and `log p` clock |
| actual one-orbit standard LCH-Hausdorff groupoid | **REFUTED at T1/T3 prerequisite** | abstract action formulas after explicit standard-circle retopology |
| P8-2--P8-6 algebraic/Floquet/FNS/character/corner package owned by the actual orbit | **SUPERSEDED AS OWNER ATTRIBUTION**; actual completion questions become `NOT_TESTABLE` | internal theorems retyped to `DEN-EF-ORBIT-STD-CIRCLE-PROXY` after a new versioned owner record |
| proxy no-normal-extension theorem | **PRESERVED on the proxy** | its exact corner/representation statement; no actual-source transport |
| packet standard LCH-Hausdorff groupoid branch | **REFUTED at the topology gate** | no universal no-go for future non-Hausdorff theories |
| `Q_p` open/quasi-compact/second-countable quotient | **PRESERVED AND SHARPENED** to nontrivial indiscrete | intrinsic quotient definition; no `B_p`, Radon, bundle, or analytic credit |
| continuous functions/orbit averages on actual `Gamma_p,Q_p` | **TOPOLOGICALLY VACUOUS FOR SEPARATION** because all continuous Hausdorff-valued functions are constant | algebraic total-mass identity only |
| actual packet normal extension | **REMAINS `NOT_TESTABLE`** | no analytic refutation is inferred from a missing standard completion |
| coefficient-one positive-time scalar Radon ledger | **UNCHANGED** | its typed scalar A1 statement; it is not a packet trace |

Paper 8 and all Stage-8 records remain immutable historical artifacts. New
Stage-9 records must use explicit `supersedes` or `retypes` links; this proof
audit itself does not edit either generation of Route files.

## 13. Same-object and Route ceiling

### T0--T7

| Field | Actual packet/inherited orbit after this proof | Standard-circle proxy |
|---|---|---|
| `T0` object | PASS: exact `Spec Z`, `E_f`, fixed `p`, restricted inherited quotient | PASS only as an explicitly new modeling object |
| `T1` topology/Borel | PASS: indiscrete, non-`T0/T1`, trivial Borel sigma-algebra | Hausdorff circle by definition; no source topology credit |
| `T2` flow/clock | PASS: exact right sign, `p^Z`, and `log p`; not a topological circle | translation flow with copied clock under an explicit set/action comparison |
| `T3` groupoid/Haar | standard LCH-Hausdorff route REFUTED; replacement withheld | Paper-8 local groupoid results may be re-owned after versioning |
| `T4` measure | no source transverse probability; no Radon disintegration promotion | orbit Haar is a modeling measure only |
| `T5` representation/trace | actual standard completion/normal-extension question NOT_TESTABLE | proxy trace and no-normal theorems retain proxy ownership |
| `T6` test algebra/formula | no actual-source operator formula follows | local formulas survive only on their exact proxy maps |
| `T7` arithmetic promotion | `(p)` and `log p` only | at most a weak copied label/clock relation |

### Route-A/Route-B

- The actual packet topology theorem retains
  `A0_ANALYTIC_ARITHMETIC_ORIGIN`; its standard LCH-Hausdorff packet-groupoid
  candidate is `A1_FAIL` at the topology prerequisite.
- The actual inherited-orbit standard-LCH record is likewise `A1_FAIL` at
  `T1/T3`.
- A newly typed standard-circle bare groupoid is at most
  `A0_WEAK_ARITHMETIC_RELATION/A1_WEAK`; proxy trace records retain only their
  independently proved proxy-level A1 verdicts.
- The independent positive-time scalar record retains its prior typed status
  and lends no topology, completion, or trace coordinate.
- Every affected row remains `A2_FAIL`, `A3_FAIL`, and `A4_FAIL`: this paper
  proves no determinant, continuation, functional equation, completed
  divisor, self-adjoint quantization, or Hilbert--Polya realization.
- Route-B invocation is Boolean `false`; no Route-B YAML is licensed.

## 14. Integrated P9-1--P9-9 adjudication

| Target | Verdict | Exact proved content |
|---|---|---|
| P9-1 | **PROVED** | `Z[1/p]_{>0}` is dense in `R_{>0} x A_p` by an explicit positive CRT sequence |
| P9-2 | **PROVED on exact domain** | unit-target pointwise convergence occurs in one fixed `E_f` raw fibre and passes through named quotient/colimit maps |
| P9-3 | **PROVED universally** | for arbitrary `x,y in Gamma_p`, the constant sequence at `x` converges to `y` |
| P9-4 | **CONFIRM_STRONG** | `Gamma_p`, every inherited orbit, and nontrivial `Q_p` are indiscrete and non-`T0/T1`/Hausdorff |
| P9-5 | **PROVED with object split** | Deninger/product and inherited-orbit/standard-circle maps are not homeomorphisms; naive adelic inherited `C_p` is indiscrete; intrinsic scaling `C_p` remains separate |
| P9-6 | **PROVED NON-CLOSED** | an explicit sequence in `R_p` converges to a pair outside `R_p` |
| P9-7 | **REFUTED at prerequisite** | the standard LCH-Hausdorff actual packet/orbit groupoid route fails; no universal non-Hausdorff no-go |
| P9-8 | **PASS** | all domain, sign, residue, stabilizer, distinctness, proxy, and unrelated-object controls close analytically |
| P9-9 | **PASS as correction specification** | exact Paper-8 dependency and Stage-9 supersession/retyping boundary is fixed; no historical file is edited |

## 15. Final proof verdict and integrity disclosure

The exact theorem is:

> For every rational prime `p`, Deninger's genuine fixed-prime rational-Witt
> `E_f` packet `Gamma_p`, with the subspace topology inherited from the exact
> `Q_{>0}` suspension quotient, is a nontrivial indiscrete space. Every actual
> inherited periodic orbit and the intrinsic orbit quotient `Q_p` are likewise
> nontrivial indiscrete spaces, and the restricted diagonal orbit relation
> `R_p` is not closed.

This proves `CONFIRM_STRONG`. It does not classify the full global suspension,
transport topology to `B_p`, construct a non-Hausdorff operator algebra,
select a transverse measure, or establish any determinant/spectral claim.

AI-assisted proof disclosure: the audit used AI-assisted exact-byte source
comparison, constructive algebra/topology proofs, and adversarial checking. It
used no Riemann-zero data, fitted parameter, external model upload, or
modification of active locks, source artifacts, historical Paper-8 files, or
Route records.
