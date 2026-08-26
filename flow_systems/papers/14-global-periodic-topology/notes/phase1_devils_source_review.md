# Paper 14 amended Phase-1 devil/domain/source re-lock

Status: **COMPLETE — EXACT-BYTE REVIEW ONLY**  
Role: **independent devil's-advocate, domain, and source-topology reviewer**  
Date: 2026-08-16 (Asia/Shanghai)  
Verdict: **PASS — C0 / M0 / m0**  
Amended devil/domain/source gate: **GO**  
Standalone status: **HOLD pending a proved infinity-sensitive or ambient-owner delta**  
Proof implementation, controls, Route A/B, manuscript, release, Git, and public
synchronization: **not authorized by this report**

## 1. Exact-byte basis and review boundary

The following inputs were hashed immediately before this review.  Every digest
matches the active tuple supplied by the review owner.

| Artifact | SHA-256 | Result |
|---|---|---|
| `notes/papers14_18_batch_design_lock.md` | `2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8` | exact match |
| `notes/research_protocol.md` | `a3ee049f27d29bb276553edcee8fbb019125b96c3e90b82f800a9706a106d7ab` | exact match |
| `notes/candidate_lock.md` | `8cbbd9e63f53c8f821f940405c6f5a41f34a5242ab9ea24be1fb87b47ae9b096` | exact match |
| `notes/phase1_amendment_v1.md` | `931d0c83528d1e05b467cf8f378b8798d2e14170c9505bcaeb5566de0a8cae16` | exact match |
| `notes/phase1_source_topology_precheck.md` | `05fb9f622c348839514d4d69760e491e7d2afdf4eb9f14687d5e0ce05d1229cb` | exact match; evidence, not authority |
| `notes/phase1_methodology_review.md` | `581e2ad01156d80f6b91febaa431d81352c47431de8a0fd865d9c71993861bf4` | exact match; final addendum included |

The retained Deninger technical source was also independently checked:

```text
papers/2-flow-zeta/notes/sources/
  deninger-dynamical-systems-arithmetic-schemes-v4.pdf
sha256:edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09
```

The ARS structural PDF preflight was rerun to stdout and returned `PASS` with
119 declared, enumerated, and reader pages and no warnings.  The source is the
exact arXiv `1807.06400v4` technical manifestation of the subsequently
peer-reviewed article.  It is Grade A, discipline-relative primary
mathematical evidence for definitions and theorem locators.  The source does
not uniquely select `E_f`; the batch explicitly freezes that source-permitted
class.

Paper 9 and Paper 10 manuscript/proof-audit hashes were independently checked
and match the batch lock.  They are internal proved-owner records, not external
novelty evidence.  No sibling verdict was inherited.  This report re-derives
only enough mathematics to decide the amended theorem signature, owner typing,
and source feasibility.  It does not execute `P14-G1`--`P14-G4`, construct
controls, or write a proof.

## 2. Executive finding

The amended tuple survives the independent attack.

1. `P14-0` is exactly source-typed.  Deninger's `C_{x_0}` is the full fibre of
   the checked base map over a finite-residue-field point, and the `E_f`
   restriction retains that full fibre.  The invariant base map therefore
   descends through the suspension and has `Gamma_p` as its full `(p)`-fibre.
2. The two-prime result is valid on the actual owner: the packets are disjoint
   ambient closed fibres; each is clopen in their finite union; Paper 9 makes
   each component indiscrete.  There are exactly four opens and no cross-prime
   specialization.
3. The infinite index topology is not forced to be the cofinite topology
   inherited from the closed-point subspace of `Spec Z`.  There is an exact
   source-level route to a finer relative separation: evaluation of the
   rational integer `p` is zero on the `p`-fibre and has complex modulus one on
   every other finite-field fibre.  The amendment correctly requires this
   route to be proved through the Galois quotient, Frobenius colimit, and
   suspension rather than inferred from finite restrictions.
4. Relative closure in `Per_Ef` and ambient closure in `X_susp` are genuinely
   different.  Deninger's Section 8 supplies a collective all-periodic closure
   precedent, but it does not classify closures for an arbitrary prescribed
   subset of rational primes.  That is the substantive source ceiling.
5. The amendment correctly prevents the likely relative coproduct/discrete
   quotient result from earning standalone status by itself.  A new ambient or
   otherwise non-substitution infinity-sensitive theorem remains mandatory.

Accordingly the amended Phase-1 devil/domain/source signature may proceed to
the separately authorized symbolic proof stage.  `STANDALONE_PASS` is not
prejudged.

## 3. Independent re-derivation of `P14-0`

### 3.1 The base map exists on the exact `E_f` owner

Deninger defines the source maps

```text
pr_X0 : check_X_0(C)_E -> X_0
```

and lets the Frobenius/rational action act trivially on `X_0`.  Proposition
4.2 gives invariance of admissible subsystems, including `E_f`.  Section 7,
Proposition 7.4 and the paragraph following Theorem 7.10 extend continuity and
the subspace/inductive-limit topology to the admissible `E` spaces.  Therefore
for `X_0=Spec Z` the map

```text
pr : check_X_0(C)_{E_f} -> Spec Z
```

is continuous and `Q_{>0}`-invariant on the frozen owner.

**Evidence Anchor:** `text: Deninger v4, physical pp. 27 and 43--47 — admissible-subsystem invariance, continuous checked projection, and E-subspace topology`

### 3.2 `C_p^{E_f}` is the full base fibre

Section 5, physical pp. 31--33, defines `C_{x_0}` as the full fibre of the
checked projection over `x_0` in the `E_tors` space, not merely as a selected
orbit inside that fibre.  It then defines

```text
C_{x_0}^E = C_{x_0} intersection check_X_0(C)_E.
```

For a finite residue field, every multiplicative character has torsion domain,
and Theorem 5.2 states that if `E` contains `E_f`, then the full `C_{x_0}`
occurs.  Taking `E=E_f` gives

```text
C_p^{E_f} = pr^{-1}((p)).
```

This directly answers the most dangerous possible source objection: the
packet is not a proper periodic subset of a larger `E_f` fibre.

**Evidence Anchor:** `text: Deninger v4, physical pp. 31--34 "The fibres ... C_x0 = pr_X0^{-1}(x0)" and Theorem 5.2`

### 3.3 Descent and suspended full-fibre identity

The diagonal action is

```text
(P,u)q=(F_qP,q^{-1}u),
```

and `pr(F_qP)=pr(P)`.  Hence `(P,u) -> pr(P)` is constant on quotient classes
and descends uniquely to a continuous map

```text
pi : X_susp -> Spec Z,
pi([P,u])=pr(P).
```

Because the preimage `pr^{-1}((p))` is invariant, taking the suspension fibre
commutes with the quotient:

```text
pi^{-1}((p))
  = (pr^{-1}((p)) x R_{>0})/Q_{>0}
  = C_p^{E_f} x_{Q_{>0}} R_{>0}
  = Gamma_p.
```

Thus the amendment's `P14-0` is feasible exactly as written.  The point `(p)`
is closed in `Spec Z`, so continuity makes `Gamma_p` closed in `X_susp`.

## 4. Independent two-prime attack

Fix distinct primes `p` and `q`.

- Theorem 6.1 makes `Gamma_p` and `Gamma_q` disjoint.
- `P14-0` makes both ambient closed.
- In `Gamma_p union Gamma_q`, each component is the complement of the other
  closed component and is therefore clopen.
- Paper 9 proves that each actual inherited component is nonempty
  indiscrete.

Consequently every open subset of the two-packet union is a union of whole
components, giving exactly

```text
empty, Gamma_p, Gamma_q, Gamma_p union Gamma_q.
```

The canonical map from the two-component topological sum is an actual-owner
homeomorphism.  For `x in Gamma_p`, indiscreteness gives
`closure_{Gamma_p}({x})=Gamma_p`, while ambient closedness gives the reverse
upper bound, hence

```text
closure_X_susp({x}) = Gamma_p.
```

The analogous equation holds for `q`.  There is no cross-prime
specialization, and the two-point Kolmogorov quotient is discrete.  This
argument uses closure and subspace identities; it does not assume first
countability or characterize ambient closure by sequences.

**Disposition:** `P14-2` is source-decidable and the finite fail-fast gate is
`GO`.  This remains feasibility evidence, not a standalone-bearing result.

## 5. Attack on `P14-G1`--`P14-G4`

### 5.1 `P14-G1`: cofinite index topology versus a finer topology

Continuity of `pi` alone supplies only the Zariski closed-point comparison.
The rational-prime subspace of `Spec Z` has the cofinite topology; therefore
closed fibres and finite-packet results alone cannot prove that `J` is open.
The amendment correctly records that limitation.

There is, however, a source-intrinsic route that can distinguish the all-prime
owner.  At the initial pointwise-convergence stage, extend a character by zero
as in Deninger's Section 7 and evaluate the rational integer `p`:

```text
ev_p(P)=P(p).
```

On a point over `(p)`, this value is zero.  On a point over `(q)` with
`q != p`, the residue of `p` is a nonzero element of the torsion group
`Fbar_q^times`; its image in `C^times` is a root of unity and therefore has
modulus one.  Thus the open condition

```text
|ev_p(P)| < 1/2
```

cuts out exactly the `p`-fibre after restriction to the finite-field fibre
union.  The zero/unit-modulus dichotomy is stable under Galois transport and
all permitted power maps.  Deninger's open Frobenius stages and quotient maps
therefore provide a concrete stagewise route to a relative neighborhood of
`Gamma_p` that misses every `Gamma_q`, `q != p`.

This is a feasibility route, not a completed `P14-G1` proof in this report.
The eventual proof must still write the saturation and subspace equalities at
the raw, Galois, colimit, and suspension levels.  If those equalities close,
each packet is relatively open and arbitrary unions are open, so `J` is open
and the index topology is discrete rather than merely cofinite.  No finite
control can establish that infinite conclusion.

**Gate result:** exact theorem signature and source route `PASS`; result
remains unproved.

### 5.2 `P14-G2`: arbitrary relative subfamilies

`P14-G2` is correctly formulated in the relative owner.  If the stagewise
separation route under `G1` closes, then for every `S` the union

```text
U_S = union_{p in S} Gamma_p
```

and its complement are arbitrary unions of relatively open packets.  Every
`U_S` would then be clopen and

```text
closure_Per(U_S)=U_S
```

for empty, finite, cofinite, and infinite coinfinite `S`.  The amendment does
not preinsert this answer and requires all branches, which is the correct
fail-fast design.

This relative result cannot be promoted to the ambient suspension.  In
particular, relative closedness says only

```text
closure_X_susp(U_S) intersection Per_Ef = U_S;
```

it says nothing by itself about nonperiodic or generic points in the ambient
closure.

**Gate result:** owner separation and exhaustive quantifiers `PASS`; result
remains unproved.

### 5.3 `P14-G3`: ambient closure and the exact source ceiling

The ambient problem has three source-supported strata.

1. For finite `S`, `U_S` is a finite union of ambient closed fibres and is
   ambient closed.
2. For every `S`, relative separation can exclude periodic packets with
   labels outside `S`, but it does not exclude nonperiodic ambient limit
   points.
3. For the union of all finite-field periodic points, Deninger's Section 8,
   Theorem 8.2 already identifies the collective closure in the larger
   source system with the unitary subsystem, subject to the theorem's stated
   hypotheses.  On the frozen `E_f` owner, any use requires the exact
   subspace/intersection and quotient argument; the source theorem itself is
   prior work, not a P14 contribution.

Theorem 8.2 proves density by satisfying finitely many character-value
constraints at suitable maximal ideals.  For number-ring strata, its cited
input gives infinitely many, indeed positive-density, eligible ideals.  It
does not say that an arbitrary prescribed infinite subset `S` meets every
eligible set.  An infinite coinfinite `S` may avoid a required congruence or
splitting class.  Therefore neither infinitude alone nor the cofinite-index
control decides the ambient closure.

This is precisely the high-risk but valid content of `P14-G3`: an exact
arbitrary-`S` classification needs an `S`-relative finite-approximation or
Chebotarev-incidence criterion, or sharp source-level bounds that expose the
missing incidence data.  A failure of a bounded search is not a mathematical
underdetermination theorem.  Under the unchanged base-protocol definition,
`SOURCE_UNDERDETERMINED` may be used only for a genuine missing source datum;
otherwise the honest disposition is unresolved/stop and carries no
standalone credit.

**Gate result:** exact owner and feasible fail-closed alternatives `PASS`;
full ambient classification and standalone weight remain `HOLD`.

### 5.4 `P14-G4`: quotient topology and universal `T0` property

The map `kappa` is well-defined because the packets are disjoint.  Its
quotient topology is an output:

```text
S is open in P  iff  union_{p in S} Gamma_p is open in Per_Ef.
```

Thus the amendment correctly distinguishes the discrete set, the cofinite
closed-point subspace, and a bare set until `G1`--`G2` are proved.  Paper 9's
indiscreteness implies that every continuous map from a packet to a `T0`
space is constant.  After the quotient topology is computed, the quotient
property of `kappa` supplies continuity of the unique factor map.  This is the
right universal-property order and does not import labels in advance.

**Gate result:** `PASS`; result remains conditional on `G1`--`G2`.

## 6. Net, quotient, and source-level stress tests

| Attack | Result | Reason |
|---|---|---|
| Is `Gamma_p=pi^{-1}((p))` only an isotropy subset? | **REFUTED** | Section 5 defines `C_x0` as the full checked fibre, and `E_f` retains it. |
| Does continuity to `Spec Z` make the all-prime index discrete? | **NO** | It supplies at most the cofinite closed-point comparison; the evaluation gap is the needed finer input. |
| Do finite subfamily homeomorphisms decide `G1`? | **NO** | Cofinite and discrete index controls have identical finite restrictions. |
| Is a sequence-only closure characterization licensed? | **NO** | The protocol's net requirement remains binding; the feasibility arguments above use explicit opens and closure identities. |
| Can relative closure be promoted to ambient closure? | **NO** | Generic/nonperiodic limits are invisible in the relative owner. |
| Does Deninger Theorem 8.2 settle arbitrary `S`? | **NO** | Its approximation chooses eligible primes; it does not force them to lie in an arbitrary prescribed subset. |
| Can a search-negative source gap become a theorem? | **NO** | It is at most `NO_DIRECT_EXACT_PACKAGE_FOUND_WITHIN_BOUNDED_SEARCH` or an unresolved stop. |

The specialization-order convention should be stated by an explicit closure
formula in the proof because both orientations occur in the literature.  This
is a proof-writing observation already recorded by the frozen precheck, not a
Phase-1 defect requiring another amendment.

## 7. Domain contribution and standalone ceiling

The strongest hostile-review objection is:

> The likely relative theorem is an evaluation-separation lemma followed by
> Paper 9's fixed-packet indiscreteness and Paper 10's complete abstract
> coproduct classification.  Deninger already owns the collective closure of
> all periodic points.  Unless Paper 14 proves a genuinely new theorem for
> prescribed infinite prime subfamilies or another non-substitution ambient
> owner, it is not a standalone paper.

The amendment answers this objection at protocol level:

- `G1`, the discrete quotient, and direct Paper-10 consequences are expressly
  insufficient for `STANDALONE_PASS`;
- the claim-delta matrix separates P9, P10, Deninger, new P14 work, direct
  substitution, infinity sensitivity, and ambient content;
- a post-proof nonredundancy review and bounded precedent search remain
  mandatory; and
- absence of a qualifying delta forces `TECHNICAL_NOTE_OR_MERGE`, without
  automatically consuming the batch's sole Technical Note slot.

The objection therefore does not require a further Phase-1 amendment, but it
remains decisive at the post-proof gate.

## 8. Severity record

### Critical findings

None.

### Major findings

None.  The amended tuple no longer conflates finite and infinite topology,
relative and ambient closure, or internal claim novelty and standalone weight.

### Minor findings

None requiring amendment.  The specialization-orientation note and the narrow
meaning of `SOURCE_UNDERDETERMINED` are already enforced by the unchanged base
protocol and are carried forward as proof-audit checks.

### Strongest counter-argument disposition

The strongest counter-argument is **VALID AS A LATER STANDALONE TEST** and
**NOT A PHASE-1 OWNER OR FEASIBILITY BLOCK**.  The amendment does not claim to
have defeated it with an unproved theorem.

## 9. Final gate matrix

| Gate | Result |
|---|---|
| six supplied exact-byte identities | PASS |
| retained Deninger PDF identity and structural preflight | PASS |
| actual `Spec Z`, `E_f`, suspension owner | PASS |
| `P14-0` source map, descent, and full-fibre feasibility | PASS |
| arbitrary two-prime topology | PASS / finite fail-fast GO |
| `P14-G1` all-prime canonical comparison signature | PASS / unproved |
| cofinite-versus-finer index attack | PASS / exact evaluation route identified |
| `P14-G2` arbitrary relative subfamilies | PASS / unproved |
| `P14-G3` ambient-owner separation and source ceiling | PASS / high-risk / unproved |
| `P14-G4` quotient and universal-property order | PASS / conditional on G1--G2 |
| net/sequence and raw/Galois/colimit/suspension firewall | PASS |
| P9/P10/Deninger nonredundancy firewall | PASS at protocol level |
| amended devil/domain/source re-lock | **GO** |
| standalone paper | **HOLD** |
| proof, controls, Route, manuscript, release, Git/public sync | not authorized by this report |

Final exact-byte verdict:
**PASS — C0 / M0 / m0; amended devil/domain/source re-lock GO, standalone HOLD.**
