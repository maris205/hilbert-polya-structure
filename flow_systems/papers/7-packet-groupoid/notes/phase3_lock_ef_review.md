# Paper 7 Phase-3 independent lock and `E_f` repair review

Review status: **COMPLETE — ACTIVE HASHES RE-LOCKED; ONE NON-RETROACTIVE
PREREGISTRATION AMENDMENT RECORDED; `E_f` REPAIR PASS**  
Review date: 2026-08-14 (Asia/Shanghai)  
Role: independent methodology/domain/integrity reviewer  
Write scope: this review only; all submitted protocol, candidate, source,
proof, code, manuscript, and Route files were treated as read-only

> **Post-review byte-drift note (12:08:03 +08:00).**  The Gate-A content
> review below was completed against the assigned protocol hash
> `0029ea437f9318ff4962830ed4d197cdad0d355968364a52bbeefc63a9db96c4`
> and candidate hash
> `0a5712af3f1e9ad83db5191f588e43631510b066e2128cdf77b6b94802da62fa`.
> During the final checksum check, the workspace paths had moved to protocol
> `8b8c6bdfb5546068d0fe8e5f971b771b1e7b4ae16cf3e0c41ce0fc9a6fc41ecf`
> and candidate
> `d5bc8643d7d41a58dbb632381c311e04bd3ae01de684b192b67540cf01f45ba0`.
> Those 12:08 amended bytes were **not reviewed in this pass**.  The 8/8
> content PASS and re-lock block below attach only to the two assigned old
> hashes and do not inherit forward; the amended files correctly remain
> exact-byte re-lock pending until a separate post-fix review.

## 1. Executive verdict

### Gate A — active Phase-1 files

```text
research_protocol.md
SHA-256: 0029ea437f9318ff4962830ed4d197cdad0d355968364a52bbeefc63a9db96c4

candidate_lock.md
SHA-256: 0a5712af3f1e9ad83db5191f588e43631510b066e2128cdf77b6b94802da62fa
```

**Formal independent re-lock verdict: PASS, 8/8 original closure conditions.**

This is a new content-based verdict attached directly to the two active
hashes.  It does not claim that their drift from the last historical
Phase-1 hashes was mechanical, and it does not inherit the old PASS merely
because the filenames are unchanged.

One post-lock theorem-domain correction is mandatory.  The general P7-4
target omitted the condition that `K_s` must first be a bounded element of
the frozen von Neumann product.  This review records that correction as
`P7-DEV-01` below.  The correction does not change the unit-mass half-plane,
the operator, trace, candidate ID, or determinant branch.  It therefore does
not undo any of the eight design-gate passes and does not require a new
candidate.  It must, however, be disclosed as a preregistration deviation and
must replace the unqualified general-mass formula in all result/manuscript
prose.

### Gate B — Morishita/Deninger `E_f` repair

**Exact verdict: PASS.**  The restricted repair is mathematically strict
provided it is stated as a new derivation, with `N_0=N`, rather than attributed
to Morishita's printed full-character theorem.

The verified result is stronger than the conservative wording in
`source_audit.md`: the restricted map is not merely “not known to be globally
onto”; it is **provably not globally onto** the Connes--Consani target.  Its
finite-adele image has at most one finite zero coordinate, whereas the target
contains classes with two finite zero coordinates.  This strengthening gives
no measure, algebra, trace, or determinant transport.

### Severity accounting

| Band | Count | Disposition |
|---|---:|---|
| Critical | 0 | no core-collapse defect found |
| Major | 1 | `LR-M1`, closed for release by the explicit `P7-DEV-01` amendment in this review |
| Minor | 1 | `EF-m1`, a non-blocking strengthening/wording correction |

There are **zero open required defects** after applying the downstream wording
rules in Sections 4 and 8.  This review authorizes manuscript theorem prose
for these two gates; it grants no Route score and performs no Route-B audit.

## 2. Materials and integrity anchors

### 2.1 Active research files

| File | SHA-256 | Review use |
|---|---|---|
| `research_protocol.md` | `0029ea437f9318ff4962830ed4d197cdad0d355968364a52bbeefc63a9db96c4` | eight-condition re-lock and original P7-4 target |
| `candidate_lock.md` | `0a5712af3f1e9ad83db5191f588e43631510b066e2128cdf77b6b94802da62fa` | record ownership and unit-mass scope |
| `phase1_devils_advocate.md` | read in full | original eight amendments and historical closure trail |
| `phase1_route_audit.md` | read in full | original typed release conditions and historical re-lock trail |
| `source_audit.md` | `a6a0e75aa2a5f38e8c60a5ce34ffb536438f93828501e282a2d0ecb530847d53` | submitted Sections 7.2--7.3 |
| `operator_source_audit.md` | `69a76991c94cab24652c8d7d9f71c47a8eba70fcd7d1d4148689d47ff56e8b04` | bounded trace-ideal terminology and bridge cross-check |
| `proof_audit.md` | read at active state | independent mathematical derivation of the P7-4 correction |
| `composition_blueprint.md` | `8071cb4d710ddd25ffae975fbd898c2373bb7f298989d170bb12ad141404ee44` | release-gate formulation only, not proof evidence |

### 2.2 Primary local manifestations

| Source | PDF SHA-256 | Preflight sidecar SHA-256 | Read integrity | Locators used |
|---|---|---|---|---|
| Deninger, *Dynamical systems for arithmetic schemes*, arXiv v4 | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | `e1d48da27567747dd880666d881ddd211021800cdde99c195e5434b114e42626` | `PASS`, 119/119/119 | Definition 4.1 and Proposition 4.2, physical p. 27; `E_f`, physical p. 28; equation (35), physical p. 32; Section 6, physical pp. 38--39; restricted topologies, physical p. 47; equations (62)--(68), physical pp. 48--49 |
| Morishita, *On a relation between Deninger's foliated dynamical systems and Connes--Consani's adelic spaces*, arXiv v5 | `3a5a34165a4bedfefb2c06f43f4e40e416882ae3406a9cd043f6ac12aebb21ae` | `1ca5ab980f477868a0600a8b53c2d04ea2a10e9702973c92e6c8177b8277d75f` | `PASS`, 26/26/26 | equations (2.1.5), (2.1.9)--(2.1.12), physical pp. 12--13; Remark 2.1.13, physical p. 13; suspension (2.2.1)--(2.2.2), physical p. 14; equation (2.2.7), physical p. 16; Lemmas 3.4--3.5, physical pp. 23--24; Theorem 3.6 and proof, physical pp. 24--25 |
| Connes--Consani, *Knots, primes and class field theory*, local v1 | `f200c41d6d772389528bb1de58ad7fe98fd8db807d72360d4311ecb3c44d2fe5` | `fb83d21739951aa78ff72f9009fc5875b1e8df6c2e437165d4d222146f0f1c4b` | `PASS`, 30/30/30 | `X_Q`, `C_p`, physical p. 9; zero-set invariant, equation (2), physical p. 10 |

The four ownership-manifest checksums were also rerun with
`sha256sum -c ownership_sources.sha256`; all eight PDF/sidecar entries returned
`OK`.  Page anchors above were used only after the `PASS` sidecars were read.

## 3. Gate A: eight-condition active-file re-lock

| # | Original Phase-1 closure condition | Evidence in the active hashes | Verdict |
|---:|---|---|---|
| 1 | component trace, global bounded `L1`, and componentwise positive-time return distribution remain distinct | Protocol Branch F requires the norm sum before `tau_m(C_f)` and defines `Theta_m` separately; candidate `RETURN-DIST-M` repeats the boundary | **PASS** |
| 2 | `K_s` has a separate analytic owner and a frozen determinant convention | Protocol Branch K and candidate `K0-M1` own the zero mode and trace-log direction separately from `C_f` | **PASS** |
| 3 | original, mass family, return distribution, and zero mode use four disjoint candidate records | Protocol Section 2 and the complete candidate lock list the same four IDs | **PASS** |
| 4 | no undefined groupoid or flow-generation claim remains | Both active files call `M_p` a selected decomposable type-I algebra and expressly deny groupoid-von-Neumann and flow-generation ownership | **PASS** |
| 5 | unit masses have a target-free, pre-result provenance obligation | Both active files retain the five-field `M1` gate and reject Euler equality/coefficient uniqueness as provenance | **PASS** |
| 6 | proxy-to-source promotion transports every classical and analytic owner field | Protocol Section 3 lists set, topology/Borel, flow/clock, measure/disintegration, algebra/representation, trace cone/domain, test class/return, zero mode/family, determinant/normalization | **PASS** |
| 7 | the proxy restarts A0, A3 receives no right-half-plane promotion, and A4/Route B remain closed | Protocol header and Section 7, plus the candidate Route boundary, impose exactly those caps | **PASS** |
| 8 | the original global-smearing Critical remains resolved before downstream work | Neither active file equates local finite Poisson sums with a normal semifinite trace value outside global `L1` | **PASS** |

The P7-4 amendment below changes an expected theorem boundary, not any owner
separation in this matrix.  The correct formal record is therefore:

```text
[P7-ACTIVE-RELOCK]
protocol_sha256: 0029ea437f9318ff4962830ed4d197cdad0d355968364a52bbeefc63a9db96c4
candidate_sha256: 0a5712af3f1e9ad83db5191f588e43631510b066e2128cdf77b6b94802da62fa
closure_conditions: 8/8 PASS
historical_pass_inherited_without_review: false
new_independent_verdict: PASS_WITH_REGISTERED_AMENDMENT
required_downstream_amendment: P7-DEV-01
candidate_version_change_required: false
```

## 4. `P7-DEV-01`: bounded-versus-affiliated preregistration amendment

### 4.1 Finding `LR-M1`

**Severity:** Major, because the uncorrected statement is false for the
general frozen mass family and would give the wrong analytic determinant
domain.  It does not invalidate the unit-mass theorem or the paper's central
negative ownership conclusion.

**Evidence anchor:** `equation: research_protocol.md, Branch K — the displayed
“exact target criterion” for K_s`; independently checked against
`equation: proof_audit.md (6.1)--(6.2)`.

**Confidence:** 5/5 — direct norm computation in the frozen atomic product.

The global algebra is

```text
M = {(A_p)_p : sup_p ||A_p|| < infinity}.
```

For `sigma=Re(s)`, the same frozen zero-mode block satisfies

```text
||K_s|| = sup_p p^(-sigma),
tau_m(|K_s|) = sum_p m_p p^(-sigma).
```

The first expression is finite exactly when `sigma>=0`.  Consequently the
correct bounded-ideal statement is

```text
K_s in L^1_tau(M) := {A in M : tau_m(|A|)<infinity}
  iff sigma>=0 and sum_p m_p p^(-sigma)<infinity.            (A.1)
```

The summability condition alone characterizes the corresponding element of
the full affiliated-operator noncommutative `L1` space.  For `sigma<0`, such
an integrable block can be an unbounded affiliated operator and is not an
element of `M` or of the bounded relative determinant algebra.

A concrete counterexample to the preregistered general formula is

```text
sigma=-1,  m_p=p^(-3).
```

Then `sum_p m_p p^(-sigma)=sum_p p^(-2)<infinity`, but
`||K_s||=sup_p p=infinity`.  Thus the omitted boundedness condition cannot be
read as implicit in the summability test.

### 4.2 Amendment record

| Field | Record |
|---|---|
| Amendment ID | `P7-DEV-01` |
| Trigger | Phase-3 proof audit distinguished membership in the frozen bounded product from membership in affiliated noncommutative `L1` |
| Original locked target | summability alone was written as the general `K_s in L1(M,tau_m)` criterion |
| Corrected result | equation (A.1) for the bounded trace ideal; summability alone only for affiliated `L1` |
| Determinant consequence | use the open analytic domain `H_m={s: Re(s)>max(0,sigma_c(m))}` for the principal trace-log branch |
| Unit-mass consequence | none: `sum_p p^(-sigma)<infinity` iff `sigma>1`, so boundedness is automatic |
| Candidate consequence | none: same `K_s`, `M`, `tau_m`, `K0-M1` ID, and logarithm branch |
| Target-data involvement | none; the correction is an operator-domain check and uses no zeta values or zero data |
| Historical handling | do not alter or replace the locked protocol wording; cite this amendment and the proof audit downstream |

This is a permissible preregistration deviation because it narrows a theorem
to the actual frozen operator domain after a falsifying case was found.  It
would be impermissible to silently rewrite the old protocol and then describe
the corrected condition as originally preregistered.

### 4.3 Required manuscript wording

Permitted:

> The preregistered general-mass criterion omitted boundedness in the chosen
> von Neumann product.  The proof therefore corrects P7-4: the bounded trace
> ideal requires both `Re(s)>=0` and weighted summability; summability alone
> describes affiliated `L1`.  The unit-mass domain `Re(s)>1` is unchanged.

For the theorem itself:

> For the frozen bounded product, `K_s` belongs to the bounded
> `tau_m`-trace ideal if and only if `Re(s)>=0` and
> `sum_p m_p p^(-Re(s))<infinity`.  The principal trace-log determinant is
> holomorphic on `Re(s)>max(0,sigma_c(m))`.

Forbidden:

- “the exact preregistered criterion was proved unchanged”;
- summability alone as bounded membership for arbitrary masses;
- importing an affiliated unbounded operator into the relative bounded
  determinant theorem; or
- creating a new candidate ID merely to hide the deviation.

## 5. Gate B: equation (2.2.7) and the exact fixed-fibre image

### 5.1 The printed full-space surjection is false

Morishita equation (2.1.5) uses the unrefined full character space, and
Remark 2.1.13 confirms that Deninger's refinement is omitted.  Equation
(2.2.7) then prints a surjection

```text
Zhat_(p)^x x N -> Hom_Gr(Fbar_p^x,C^x),
(a,n) |-> chi_P o ( )^a o ( )^n.
```

Every displayed image has finite kernel: `a` is an automorphism of
`Fbar_p^x`, the `n`-power map has finite kernel, and `chi_P` is injective.
The trivial character belongs to the printed full Hom set but has kernel
`Fbar_p^x`, which is infinite.  It is therefore an explicit counterexample
to surjectivity as printed.

**Verdict:** the counterexample is valid and decisive.  It is not merely a
missing proof detail.

### 5.2 The exact repaired image is `E_f`

Deninger equation (35), for `N_0=N`, defines `S` to be the characters of
`Fbar_p^x` with finite cyclic kernel and proves the surjection

```text
Zhat_(p)^x x N -> S.
```

Because every finite subgroup of `Fbar_p^x` is cyclic, `S` is exactly the
fixed-fibre `E_f` class.  Equivalently, relative to the reference injection,
an exponent `b=(b_q)_(q!=p)` has finite kernel exactly when it can be written
`b=n a` with `n in N` and `a in Zhat_(p)^x`: no component `b_q` is zero and
only finitely many components have positive valuation.

Therefore:

```text
image of Morishita (2.2.7) = fixed-fibre E_f set,
not the full character set.                                  (B.1)
```

Equation (B.1) is fibrewise and set-theoretic.  It does not prove a global
chart, a homeomorphism, inverse continuity, a Borel transition, or Haar
transport.

## 6. `E_f` invariance, topology, restriction, and descent

The restriction/descent chain closes as follows.

1. Deninger Definition 4.1 makes admissibility invariant in both directions
   under Frobenius powers and invariant under residue-field automorphisms.
   The example immediately following Corollary 4.4 lists `E_f`; Proposition
   4.2 gives `G` invariance, forward/backward `N` invariance, and the induced
   `Q_+`-invariant colimit.
2. Morishita's unrefined object carries pointwise topology, then Galois
   quotient topology, inductive-limit topology, and suspension quotient
   topology in equations (2.1.5), (2.1.9)--(2.1.12), and (2.2.1).
3. Deninger Section 7, physical p. 47, gives `E_f` the corresponding subspace
   topology, identifies the quotient by `G` topologically, and states that
   its inductive-limit topology agrees with the ambient subspace topology.
   Thus the genuine `E_f` system is a topological invariant subsystem of the
   unrefined one, not a newly imposed ad hoc topology.
4. Morishita Lemma 3.4 proves that root-of-unity restriction `psi` is
   continuous and `N`/Galois equivariant.  Restriction to the invariant
   `E_f` subspace remains continuous.  Equivariance permits passage to the
   colimit and Galois quotient; the quotient universal property gives the
   descended continuous map.
5. Morishita Lemma 3.5 supplies the suspension map and the inversion of the
   real coordinate.  Hence the restricted map satisfies, for `u>0`,

   ```text
   Psi_Ef(phi_u x) = u^(-1) . Psi_Ef(x).                      (B.2)
   ```

**Verdict:** restriction and descent are valid.  The resulting domain is the
genuine Deninger finite-kernel subsystem.  This does not validate the
homeomorphism claims of Theorems 2.2.8/2.2.9 on Morishita's enlarged object.

## 7. Away-from-`p` normalization and packetwise image

Fix one source circle in the packet over `p`.  Deninger equation (35) writes
its fixed-fibre character, after absorbing any reference-injection change
into the unit, with

```text
a in Zhat_(p)^x,  n in N.
```

Under the root-of-unity exponent map used by `psi`, the finite adele
`alpha=(alpha_q)` satisfies

```text
alpha_p = 0,
alpha_q = n a_q != 0  for every q != p.                       (B.3)
```

Only primes dividing `n` give nonunit away coordinates.  Multiplication by
`n^(-1) in Q^x` changes the away coordinates to `a_q`.  Then choose
`u in Zhat^x` with `u_q=a_q^(-1)` for `q!=p` and, for example, `u_p=1`.
In the double quotient, (B.3) is therefore represented by

```text
finite coordinate p: 0;
every finite coordinate q!=p: 1;
archimedean coordinate: positive.
```

This is precisely a point of the standard prime orbit `C_p`.  The printed
proof of Morishita Theorem 3.6(2) checks only `alpha_p=0`; equation (B.3) is
the missing finite-kernel supplement.

Once one point of a source circle maps into `C_p`, anti-equivariance (B.2)
shows that the image of the whole circle is the entire `R_+` orbit `C_p`.
Thus

```text
for every periodic source circle gamma contained in Gamma_p,
Psi_Ef(gamma) = C_p.                                          (B.4)
```

The same target orbit occurs for every transverse circle label over `p`.
Accordingly, the induced map on the set of orbit labels in one packet is
constant.  This is the exact sense in which transverse labels collapse.  It
does not assert that a transverse measure has been pushed forward or that a
packet has been identified pointwise with `C_p`.

## 8. Strict global non-surjectivity

### 8.1 Finding `EF-m1`

**Severity:** Minor.  `source_audit.md` safely says that global surjectivity
is not established, but the local sources permit the stronger negative
theorem below.  This is a scope/wording improvement, not a flaw in the
restricted construction.

**Evidence anchor:** `equation: Deninger (62)--(68), physical pp. 48--49`,
cross-checked with `equation: Connes--Consani (2), physical p. 10`.

**Confidence:** 5/5 — the zero-coordinate set is invariant under every
element used in the quotient.

Deninger's equations (62)--(64), and the induced adelic map (66)--(68), put
the root-of-unity exponent of any admissible source point in the disjoint
union

```text
Q_+ Zhat^x
  disjoint-union over p of Q_+ (Zhat_(p)^x x {0 at p}).        (B.5)
```

The `E_f` image is a subset of (B.5).  Hence every image point has either no
finite zero coordinate or exactly one finite zero coordinate.

On the other hand, choose distinct primes `p` and `q` and the adele

```text
a_p=a_q=0,  a_l=1 for l notin {p,q},  a_infinity=1.
```

It defines a point of the Connes--Consani target.  Its two-element finite
zero set cannot change under multiplication by `Q^x` or `Zhat^x`, because
all such multipliers have nonzero coordinates.  Connes--Consani equation (2)
records the same quotient-invariant zero set.  The class therefore has no
preimage under `Psi_Ef`.

The strict result is

```text
Psi_Ef is not globally surjective onto X_Q.                    (B.6)
```

Calling it a “factor onto its invariant image” is permissible only after
explicitly reversing the target time convention; the least ambiguous term is
“continuous flow-anti-equivariant intertwining map, surjective onto its own
image and packetwise onto `C_p`.”

## 9. Exact manuscript-safe theorem statement

The following is allowed:

> **Restricted adelic intertwiner.**  Let `X_Den^(E_f)` be Deninger's
> finite-kernel system for `Spec Z`, with `N_0=N`.  Restricting Morishita's
> root-of-unity map gives a continuous map to the Connes--Consani adelic
> system satisfying `Psi_Ef(phi_u x)=u^(-1)Psi_Ef(x)`.  For every prime `p`
> and every periodic orbit `gamma` in the source packet `Gamma_p`, one has
> `Psi_Ef(gamma)=C_p`.  The map is not globally onto: its image has at most
> one finite zero coordinate, while the adelic target contains classes with
> two.  All source orbit labels over `p` therefore have the same target-orbit
> image.

The source correction should be introduced with:

> Morishita's equation (2.2.7) is not surjective on the printed full
> character space; the trivial character is a counterexample.  Deninger's
> equation (35) identifies its exact fixed-fibre image with `E_f`.  The
> packet statement below is therefore a new restricted derivation, not the
> unmodified printed theorem.

The following remain forbidden:

- “Morishita proves (2.2.7) on the full character space”;
- a homeomorphism or conjugacy between a Deninger packet and `C_p`;
- a globally onto factor map to all of `X_Q`;
- preservation of transverse multiplicity, a transverse measure, or Haar
  disintegration;
- a map from the source to the Paper-7 proxy `Y_p` or algebra `M_p`; or
- transport of `m_p`, `tau_m`, its `L1` ideal, `P_0`, `K_s`, the return
  distribution, or any determinant.

## 10. Release decision

Both requested publication gates are closed:

```text
Gate A: PASS
  active hashes re-locked independently
  eight original Phase-1 conditions: 8/8 PASS
  P7-DEV-01: recorded, non-retroactive, mandatory downstream

Gate B: PASS
  MOR-EF-IMAGE: proved as a fixed-fibre set statement
  MOR-PSI-RESTRICT-EF: restriction/topology/descent proved
  away-from-p normalization: proved
  packetwise onto C_p: proved
  global non-surjectivity: proved
  transverse orbit-label collapse: proved
  measured/operator/determinant transport: not supplied
```

**Final decision: RELEASE THESE TWO GATES TO MANUSCRIPT DRAFTING.**  This
decision is conditional only on using the corrected P7-4 domain and the exact
restricted-map wording above.  It is not a Route-A promotion and it gives no
permission to invoke Route B.

## 11. Post-fix exact-byte re-lock addendum — 2026-08-14

Addendum status: **COMPLETE — CONTENT RE-LOCK PASS; OVERALL M5 GATE REVISE
FOR ONE DOWNSTREAM-PROPAGATION DEFECT**  
Review mode: independent post-fix verification; no prior PASS inherited  
Write scope: this addendum only; every protocol, candidate, proof, amendment,
source, code, result, blueprint, manuscript, and Route file remained read-only

This addendum supersedes the prospective part of the byte-drift note at the
top of this review, but does not erase it.  The earlier note accurately records
that the 12:08 bytes had not then been reviewed.  The determinations below are
a fresh content review of a later, explicitly supplied five-record tuple.

### 11.1 Exact input tuple and anti-inheritance check

Every supplied hash was recomputed immediately before substantive review and
again after the read-only verification run:

| Record | Required and observed SHA-256 | Byte verdict |
|---|---|---|
| `research_protocol.md` | `2f8dc9a802cfcf8b578db24419909de710563ece62cf026e9848fac437ba1581` | **MATCH** |
| `candidate_lock.md` | `73314bb031f663e8532a922821e66b20f31bd6f20b06a801a25147d6e55a17a0` | **MATCH** |
| `proof_audit.md` | `febcd43e5d23daf893816b815c81f19ee4da5bac42a554d553262784660f00b5` | **MATCH** |
| `phase3_protocol_amendment.md` | `b8c55c5a2ebd4f22f6990671d03b2e1d997ce180e7638ed933b20471374eb03c` | **MATCH** |
| `packet_trace_manifest.json` | `fe12ec4c6b0a950d35d267c830119945652acafb9a5ddae2aa6b86db92943b26` | **MATCH** |

The old `0029ea.../0a5712...` PASS was used only as historical review input.
It was not treated as evidence that the five records above pass.  The current
protocol, candidate, proof, amendment crosswalk, and manifest were read and
tested on their own bytes.

The unchanged supporting source records were also checked at
`source_audit.md` SHA-256
`a6a0e75aa2a5f38e8c60a5ce34ffb536438f93828501e282a2d0ecb530847d53`
and `operator_source_audit.md` SHA-256
`69a76991c94cab24652c8d7d9f71c47a8eba70fcd7d1d4148689d47ff56e8b04`.
They are bridge/terminology evidence, not members of the new five-record lock.

### 11.2 `P7-DEV-01` to authorial-amendment crosswalk

The two identifiers have different audit roles but the same load-bearing
mathematical correction:

```text
P7-DEV-01                         independent review deviation record
  -> phase3_peer_review M1        independently rediscovered release defect
  -> P7-PH3-AMEND-2026-08-14-v1  authorial normative amendment
```

The crosswalk is complete because:

1. the historical one-domain formula remains quoted and expressly marked
   superseded; history was not silently rewritten;
2. the affiliated criterion is weighted summability alone;
3. the bounded relative trace-ideal criterion adds `Re(s)>=0`;
4. the determinant branch is restricted to the open domain
   `H_m={Re(s)>max(0,sigma_c(m))}`, where summability and `||K_s||<1` hold;
5. the scalar is named `D_tau^pr`, with the principal logarithm fixed at the
   identity, rather than an unqualified complex semifinite determinant;
6. the unit-mass conclusion remains exactly `Re(s)>1`; and
7. the candidate ID, operator, trace, mass status, and same-object boundary do
   not change merely to conceal the deviation.

The direct proof is present in `proof_audit.md` equations (6.1)--(6.3) and
(7.1)--(7.11).  The concrete counterexample from the first review therefore no
longer refutes the normative theorem; it refutes only the visibly retained
historical target.

**Verdict on `P7-DEV-01` / M1:** **PASS, CLOSED NON-RETROACTIVELY.**

### 11.3 Original Phase-1 eight-condition re-audit

This matrix uses the original eight amendments in
`phase1_devils_advocate.md`, rather than deriving a more convenient new list.

| # | Original condition | Evidence in the post-fix tuple | Verdict |
|---:|---|---|---|
| 1 | separate component trace, global `L1(tau_m)`, and distributional return | protocol Branch F and proof Sections 3--5 distinguish all three and permit `tau_m(C_f)` only under the global norm sum | **PASS** |
| 2 | preregister the trace-norm asymptotic and unit-mass divergence | protocol Branch F/P7-2 and proof equations (4.1)--(4.3) give the exact criterion and nonzero-test asymptotic | **PASS** |
| 3 | add a separate `K_s` owner, determinant gate, and base/clock controls | protocol Branch K, candidate `K0-M1`, proof Sections 6--7 and 10, and the control manifest preserve the separation | **PASS** |
| 4 | define a groupoid or remove the claim | protocol and candidate call `M_p` a selected decomposable type-I algebra and deny flow-generated/groupoid-algebra ownership | **PASS** |
| 5 | make the mass family primary and gate unit-mass provenance | the mass-family record remains primary; `K0-M1` remains `MODELING_CHOICE` behind the same five target-free fields | **PASS** |
| 6 | separate trace existence, operator-domain membership, local finiteness, and Dirichlet convergence | protocol now types affiliated versus bounded `L1`; proof Section 2.1 proves FNS independently, Section 5 proves local finiteness, and Sections 6--7 handle convergence | **PASS** |
| 7 | restart proxy A0 and retain the non-redundancy/proves-too-much controls | protocol Route scope is A0--A3, P7-8 proves base/clock blindness, and A4/Route B remain closed | **PASS** |
| 8 | preserve full same-object ownership before source promotion | protocol lists every classical and analytic transport field; candidate and proof deny transfer to `DEN-WITT-Z-FIN` | **PASS** |

**Phase-1 compatibility verdict on these new bytes: 8/8 PASS.**  The M1
amendment narrows and types a theorem domain; it does not reopen any of the
eight object-design closures.

### 11.4 M2--M4 mathematical repair check

| Finding | Post-fix evidence | Verdict |
|---|---|---|
| M2, concrete FNS trace | proof Section 2.1 proves local direct-integral faithfulness/normality, uses the increasing congruence cutdowns `A_p^(1/2)E_(p,N)A_p^(1/2)`, builds the finite-prime/finite-mode global net, and proves arbitrary-net normality in (2.6) | **PASS** |
| M3, relative-norm holomorphy | proof Section 7.1 supplies derivative domination, operator-norm tails, trace-norm tails, and locally uniform logarithm/derivative convergence in `||.||+||.||_1` | **PASS** |
| M4, actual-base multiplicity | proof Sections 7.3--7.4 prove the frozen `B_p` infinite using the sign subgroup modulo the procyclic image, then construct arbitrarily large orthogonal Haar-`L2` families and exclude ordinary trace class | **PASS** |

No mathematical Critical or residual M1--M4 Major was found.  The proof also
keeps P7-9 outside its authority and repeatedly denies analytic transfer to
the published source flow.

### 11.5 `E_f` bridge scope after the amendment

The post-fix operator/protocol work does not enlarge the already reviewed
bridge.  The exact permitted result remains:

```text
domain: genuine Deninger E_f subsystem
target: Connes--Consani adelic system
map: continuous and flow-anti-equivariant
prime packet: every source circle maps onto C_p
global target: not surjective
transverse labels: collapse to the same target orbit
```

The strict negative global statement follows from the invariant finite-zero
set: the source image has at most one finite zero coordinate, while the target
contains classes with two.  This does not turn the map into a source-to-proxy
bridge.  No packet Haar measure/disintegration, representation, algebra,
normal trace, `L1` ideal, return distribution, zero mode, analytic family, or
determinant is transported.

**Bridge verdict: PASS WITH THE PREVIOUS STRICT SCOPE UNCHANGED.**  In
particular, the amendment does not revive Morishita's printed full-character
surjection or homeomorphism claim and does not make the map globally onto.

### 11.6 Same-object and operator-ownership audit

The following ownership separations survive byte-for-byte:

- `DEN-WITT-Z-FIN` owns the source packet, prime labels, repetitions, and
  clocks, but none of the selected proxy's measured/operator fields;
- `DEN-WITT-PACKET-DECOMP-MASS-FAM` owns the chosen bases, representation,
  algebra, positive-cone trace family, and general masses;
- `DEN-WITT-PACKET-DECOMP-RETURN-DIST-M` owns the componentwise positive-time
  distribution and cannot borrow the zero-mode determinant;
- `DEN-WITT-PACKET-DECOMP-K0-M1` owns the conditional unit-mass zero-mode
  family and `D_tau^pr`, but remains `MODELING_CHOICE` on provenance; and
- the Morishita target is a third adelic object, not the Paper-7 proxy.

The manifest independently labels its calculations as finite proxy
convention checks and denies proof, source transport, trace provenance,
determinant provenance, or Route authority.  Thus neither shared clocks nor a
shared parent algebra permits cross-operator or cross-object credit.

**Same-object/operator verdict: PASS.**

### 11.7 Manifest and deterministic closure

Read-only validation produced all of the following:

- valid JSON with schema `paper7-packet-trace-controls/2`;
- all nine CSV SHA-256 values, byte counts, and data-row counts match;
- all six frozen implementation-file SHA-256 values match;
- the verifier rejects missing, extra, and tampered implementation entries;
- `21/21` unit tests pass with bytecode writing disabled; and
- `--verify-only` returns `regression_status: PASS` and `artifact_count: 9`.

These checks close the previous sign/quantity-label and implementation-hash
verification defects.  They remain regression and convention witnesses, not
proof of an infinite theorem or source ownership.

**Manifest verdict: PASS.**

### 11.8 Residual M5 defect

M5 has two separable parts.  Independent inspection of the exact amended
tuple is complete and passes.  Propagation of that lock and the repaired
theorem status into downstream authority records is not complete.

`composition_blueprint.md` remains a stale downstream consumer:

1. lines 7--8 still say P7-1--P7-8 and the `E_f` repair await an independent
   proof audit;
2. lines 18--19 still label `0029ea.../0a5712...` as the active protocol and
   candidate;
3. lines 23--33 still say a formal independent re-lock is required before
   drafting;
4. line 169 still compresses P7-4 to unqualified weighted summability instead
   of splitting affiliated and bounded domains; and
5. lines 210--239 and line 555 still type the `E_f` lemmas as expected/pending
   and say only that global surjectivity is unestablished, rather than
   recording the proved strict non-surjectivity.

This is a typed authority-chain defect, not a mathematical counterexample.
It nevertheless blocks **M5 as a whole**, because the finding that created M5
expressly required both an independent exact-byte lock and downstream hash/
status propagation.  This review was instructed not to modify that blueprint,
so the defect is reported rather than repaired here.

The `M5 pending` text inside the locked protocol, candidate, proof, and
authorial amendment is not itself a defect.  Those author-owned records must
not self-certify the independent check; this external addendum is the proper
certificate.  Editing those status lines merely to say PASS would create new
bytes and another lock cycle.

**Finding `M5-R1`: downstream lock/theorem propagation incomplete.**  
**Severity:** Major, because it is the sole remaining release condition in the
pre-existing M5 Major and can direct manuscript drafting to superseded hashes
and theorem domains.  
**Evidence anchor:** text: `composition_blueprint.md` lines 7--8, 18--33,
169, 210--239, and 555 — "formal independent hash re-lock: REQUIRED before
manuscript drafting".  
**Confidence:** 5/5 — direct hash/status and theorem-wording comparison.

Required repair, outside this review's write scope:

1. update the blueprint's active authority table to the post-fix locks while
   preserving every old hash as historical;
2. replace its proof-pending status with the exact proved/negative boundaries;
3. split P7-4 into affiliated and bounded criteria and name `H_m`/`D_tau^pr`;
4. state the proved `E_f` repair, including strict global non-surjectivity and
   the no-analytic-transport boundary; and
5. obtain a narrow read-only confirmation that those downstream edits point
   to this exact tuple and do not introduce a new ownership or Route claim.

### 11.9 Formal post-fix verdict

```text
[P7-M5-POSTFIX-RELOCK]
review_date: 2026-08-14 Asia/Shanghai
prior_pass_inherited: false

research_protocol_sha256: 2f8dc9a802cfcf8b578db24419909de710563ece62cf026e9848fac437ba1581
candidate_lock_sha256: 73314bb031f663e8532a922821e66b20f31bd6f20b06a801a25147d6e55a17a0
proof_audit_sha256: febcd43e5d23daf893816b815c81f19ee4da5bac42a554d553262784660f00b5
phase3_protocol_amendment_sha256: b8c55c5a2ebd4f22f6990671d03b2e1d997ce180e7638ed933b20471374eb03c
packet_trace_manifest_sha256: fe12ec4c6b0a950d35d267c830119945652acafb9a5ddae2aa6b86db92943b26

exact_tuple_content_relock: PASS
phase1_original_conditions: 8/8 PASS
P7-DEV-01_M1_crosswalk: PASS_CLOSED_NON_RETROACTIVELY
M2_M4_mathematics: PASS
E_f_bridge_scope: PASS_STRICT
same_object_operator_ownership: PASS
manifest_internal_and_regression_check: PASS

M5_independent_exact_byte_inspection: PASS
M5_downstream_propagation: FAIL
overall_M5_gate: REVISE

critical_open: 0
major_open: 1 (M5-R1, mechanical downstream propagation)
required_minor_open: 0
route_verdict: NOT_ISSUED
```

**Final addendum decision: REVISE.**  The five-record tuple is mathematically
and typologically eligible for re-lock, but M5 is not closed until the stale
blueprint authority/theorem references are updated and narrowly verified.
This decision grants no Route-A promotion, no Route-B entry, and no transfer
of proxy results to `DEN-WITT-Z-FIN`.

## 12. M5-R1 narrow closure addendum — 2026-08-14

Closure status: **COMPLETE — M5 PASS**  
Review mode: narrow read-only re-review of `M5-R1` only  
Submitted downstream record: `composition_blueprint.md`, SHA-256
`ec916a47cc77b7d6e731614d2f258f7c61ecb3317b405ad5fc0b094324a6cc7b`

This addendum does not inherit a result from Section 11 and does not re-open
the mathematical, source, ownership, or manifest gates that already passed.
It independently checks the one repair that Section 11 left open: whether the
composition blueprint now propagates the exact post-fix authority and theorem
boundaries without retaining a contradictory old active state.

### 12.1 Exact-byte and authority-table check

The submitted blueprint hash matched both before and after inspection.  Its
authority table now makes the required distinction:

| Record class | Blueprint treatment | Verdict |
|---|---|---|
| old protocol `0029ea...` and candidate `0a5712...` | lines 17--18 call them **pre-amendment**, **historical**, and visibly superseded | **PASS** |
| amended protocol | line 19 records `2f8dc9a802cfcf8b578db24419909de710563ece62cf026e9848fac437ba1581` as active and independently accepted | **PASS** |
| amended candidate | line 20 records `73314bb031f663e8532a922821e66b20f31bd6f20b06a801a25147d6e55a17a0` as active and independently accepted | **PASS** |
| repaired proof | line 21 records `febcd43e5d23daf893816b815c81f19ee4da5bac42a554d553262784660f00b5` as active and independently accepted | **PASS** |
| amendment crosswalk | line 22 records `b8c55c5a2ebd4f22f6990671d03b2e1d997ce180e7638ed933b20471374eb03c` | **PASS** |
| result manifest | line 25 records `fe12ec4c6b0a950d35d267c830119945652acafb9a5ddae2aa6b86db92943b26` with the verified schema/test scope | **PASS** |
| independent post-fix report | line 26 records `phase3_postfix_review.md` at its observed hash `8527d940ccac52279ac857a9db7739e8a4d4849035d6a6a371aeaac7beacb475` | **PASS** |

Lines 27--42 explicitly deny inheritance of the historical PASS, attach the
current authorization to independent post-fix review, identify this blueprint
revision as the `M5-R1` propagation, and mark M1--M5 closed.  No old hash is
still labeled active.

### 12.2 Theorem-status and wording check

| Former residual | Corrected blueprint evidence | Verdict |
|---|---|---|
| proof audit still pending | lines 7--9 now say P7-1--P7-8 and the `E_f` repair passed independent post-fix review; lines 603--621 record the resulting proof/re-lock authority | **PASS** |
| P7-4 compressed to one domain | owner table line 119 and theorem row 180 distinguish affiliated summability from bounded `L^1_tau` with `Re(s)>=0`; line 181 and the Branch-K plan bind the scalar to `H_m` and `D_tau^pr` | **PASS** |
| `MOR-EF-IMAGE` still expected | lines 221--226 state that Deninger equation (35) proves the exact restricted finite-kernel image | **PASS** |
| restricted descent still proof-pending | lines 229--245 state that independent source/post-fix audits verified invariance, topology, descent, normalization, and packetwise onto `C_p` | **PASS** |
| global surjectivity merely unestablished | lines 247--255 prove the strict negative using the one-zero image/two-zero target invariant; lines 507--510 and 573 require “strictly not globally onto” | **PASS** |
| analytic ownership could drift through the bridge | lines 256--261 and the owner table keep the map away from `Y_p`, `M_p`, measure, representation, trace, `L1`, zero mode, and determinant | **PASS** |

The full-file negative scan found no occurrence matching any of these forbidden
residual forms:

```text
Active ... 0029ea... / 0a5712...
formal re-lock REQUIRED or PENDING
P7-4 membership iff weighted summability without the bounded split
MOR-EF-IMAGE / MOR-PSI-RESTRICT-EF expected or pending
proof audit must verify / independent proof audit required
global surjectivity not established
```

The two old hashes remain present only as historical audit-trail data.  Their
presence is required provenance, not a residual active-lock defect.

### 12.3 Final closure decision

`M5-R1` is **FULLY ADDRESSED**.  The repair changes only the downstream
authority and theorem-status map; it introduces no new candidate, analytic
owner, source transport, determinant entitlement, or Route claim.

```text
[P7-M5-FINAL-CLOSURE]
review_date: 2026-08-14 Asia/Shanghai
review_scope: M5-R1 narrow downstream confirmation
composition_blueprint_sha256: ec916a47cc77b7d6e731614d2f258f7c61ecb3317b405ad5fc0b094324a6cc7b

old_active_hash_residual: NONE
relock_required_or_pending_residual: NONE
P7_4_single_domain_residual: NONE
E_f_proof_pending_residual: NONE
global_surjectivity_unestablished_residual: NONE
same_object_or_operator_regression: NONE

M5_R1: FULLY_ADDRESSED
M5_independent_exact_byte_inspection: PASS
M5_downstream_propagation: PASS
overall_M5_gate: PASS

critical_open: 0
major_open: 0
required_minor_open: 0
route_verdict: NOT_ISSUED
```

**Final closure verdict: M5 PASS.**  This supersedes the Section-11 `REVISE`
decision for `M5-R1` only.  It authorizes manuscript drafting under the exact
typed owners and theorem boundaries in the corrected blueprint.  Route-A
evaluation, manuscript review, citation integrity, final artifact audit, and
Route B remain separate gates exactly as listed in blueprint Section 17.
