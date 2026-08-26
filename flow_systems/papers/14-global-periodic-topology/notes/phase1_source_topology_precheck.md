# Paper 14 Phase-1 source-topology precheck

Status: **COMPLETE — EXACT-BYTE REVIEW / REPORT ONLY**  
Role: independent devil/domain and source-topology fail-fast  
Date: 2026-08-16 (Asia/Shanghai)  
Verdict: **PASS — C0 / M0 / m0**  
Fail-fast decision: **GO_TO_FULL_PROOF**  
Standalone decision: **HOLD pending the global periodic-locus theorem**  
Route B, controls, proof implementation, manuscript, release, Git, and public
synchronization: **not authorized**

## 1. Exact-byte audit

The mathematical derivation in Sections 3--6 below was completed independently
before the frozen Phase-1 files were inspected.  The following byte audit was
then performed; the frozen files agree with the hashes supplied by the parent
review owner.

| Artifact | SHA-256 | Result |
|---|---|---|
| `notes/papers14_18_batch_design_lock.md` | `2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8` | exact match |
| `notes/research_protocol.md` | `a3ee049f27d29bb276553edcee8fbb019125b96c3e90b82f800a9706a106d7ab` | exact match |
| Paper-9 manuscript | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` | exact match to batch lock |
| Paper-9 proof audit | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | exact match to batch lock |
| Paper-10 manuscript | `27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315` | exact match to batch lock |
| Paper-10 proof audit | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` | exact match to batch lock |
| retained Deninger arXiv-v4 source | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | exact local primary-source bytes |

This report does not alter any frozen protocol, pipeline-state, source,
control, or upstream paper file.

## 2. Executive finding

The two-prime topology is **source-decidable**.  It is not necessary to impose
a coproduct topology or choose packet coordinates.

Let

```text
X_susp = (check_X_0(C)_{E_f} x R_{>0}) / Q_{>0}
```

be the exact frozen suspension.  The source/base map descends to a continuous
map

```text
pi : X_susp -> Spec Z.
```

For every rational prime `r`, the actual packet is the full fibre

```text
Gamma_r = pi^{-1}((r)).
```

It follows that every `Gamma_r` is closed in the full suspension.  Combining
this source-level fact with Paper 9's indiscreteness theorem gives, for
`p != q`,

```text
Gamma_p union Gamma_q  ~=  Gamma_p coproduct Gamma_q
```

as an actual homeomorphism, not as a declared control topology.  The union has
exactly four open sets:

```text
empty, Gamma_p, Gamma_q, Gamma_p union Gamma_q.
```

There is no cross-prime specialization.  For `x in Gamma_p`, its closure in
the full suspension is exactly `Gamma_p`; the analogous statement holds for
`q`.  Thus the two-prime Kolmogorov quotient is the discrete two-point space.

This closes the protocol's fail-fast gate with `GO_TO_FULL_PROOF`.  It does
**not** yet close the standalone gate.  The two-prime result is an elementary
actual-owner consequence of the source projection plus Paper 9.  If Paper 14
stops there, the protocol's `NOTE_OR_MERGE` rule applies.  A standalone paper
still requires the all-prime inherited topology, its global `T0` quotient, or
an equally substantive ambient-closure theorem.

## 3. Exact source and owner chain

### 3.1 Deninger primary source

The retained primary source is Christopher Deninger, *Dynamical systems for
arithmetic schemes*, arXiv `1807.06400v4`, identified above by SHA-256.
The relevant source chain is:

1. Definition 4.1 and Proposition 4.2, physical p. 27: `E_f` is an admissible
   finite-kernel class; the base projection is invariant under the Frobenius
   action, with the rational action trivial on the scheme point.
2. Section 5, physical pp. 31--37, especially equations (37)--(39) and
   Theorem 5.2: `C_{x_0}` is the checked pre-suspension fibre/packet over the
   finite-residue-field point `x_0`; for `E_f` the full packet occurs.
3. Section 6, physical pp. 38--39 and Theorem 6.1: the suspension and
   `Gamma_{x_0}` are defined, the packets are pairwise disjoint, and they
   exhaust the nontrivial-isotropy locus.
4. Section 7, Lemma 7.1, physical p. 40, followed by the quotient and
   inductive-limit topology results on physical pp. 43--47: the scheme/support
   map is continuous, the admissible `E` spaces carry the inherited
   topologies, and the source explicitly warns that its global continuous
   decomposition bijections need not be homeomorphisms.
5. Section 8, especially Theorem 8.2, physical pp. 49--52: the source already
   studies the collective closure of periodic points in the larger unitary
   subsystem.  This is a precedent and boundary for any later ambient-closure
   claim; it is not a new Paper-14 theorem merely by restatement.

The local source audit records the same owner chain at
`papers/2-flow-zeta/notes/phase2_deninger_source_audit.md:136`, with the
admissibility and packet statements at lines 159--207 and the topology ceiling
at lines 240--253.

### 3.2 Paper 9

Paper 9 fixes the actual owner and proves the fixed-prime input used here:

- `papers/9-packet-separation/paper/manuscript.tex:144` defines `check_X`,
  `Y`, `Z_p`, `Gamma_p`, and the inherited subspace topology through line 172;
- lines 194--216 prove that the global orbit map is open and that restriction
  to the saturated `Z_p` is the exact inherited quotient;
- lines 369--414 prove universal constant-class convergence and hence that
  `Gamma_p` is nontrivial indiscrete;
- lines 472--482 expressly stop at the fixed-prime boundary;
- lines 661--679 preserve the full-global problem as open.

### 3.3 Paper 10

Paper 10's copied coproduct remains a valid negative control:

- `papers/10-separated-reflection/paper/manuscript.tex:370`--418 proves the
  abstract tagged-coproduct classification;
- lines 420--450 specialize it to copied prime packets;
- lines 452--462 expressly deny source-global topology credit without a new
  continuous comparison;
- lines 527--540 identify the actual-global classification as unresolved.

Paper 14 may prove the missing comparison.  Doing so does not make Paper 10
incorrect: Paper 10 made no negative theorem saying that the comparison could
never be proved.

## 4. The two-prime theorem candidate

### Theorem (closed packet fibres and finite-packet coproduct)

Let `X_susp` be the actual `Spec Z`, `E_f` rational-Witt suspension.  Let
`p != q` be rational primes.

1. There is a canonical continuous map `pi:X_susp->Spec Z` and
   `Gamma_r=pi^{-1}((r))` for every rational prime `r`.
2. Every `Gamma_r` is closed in `X_susp`.
3. The actual inherited subspace `Gamma_pq=Gamma_p union Gamma_q` is the
   topological coproduct of its two actual packet subspaces.
4. For every `x in Gamma_r`,

   ```text
   closure_X_susp({x}) = Gamma_r.
   ```

5. Hence two points of `Gamma_pq` specialize to one another exactly when they
   lie in the same prime packet.  The specialization equivalence classes and
   topological-indistinguishability classes are `Gamma_p` and `Gamma_q`, and
   the `T0` quotient is discrete on `{p,q}`.
6. The same proof applies to every nonempty finite set of rational primes.

### Proof

The checked base map

```text
pr : check_X_0(C)_{E_f} -> Spec Z
```

is continuous and `Q_{>0}`-invariant because the rational Frobenius action is
trivial on the scheme point.  Therefore `(P,u) |-> pr(P)` is continuous and
constant on the diagonal `Q_{>0}` orbits.  By the universal property of the
quotient topology it descends to a continuous `pi` on `X_susp`.

The source definition of `C_{(r)}^{E_f}` as the full checked fibre over the
finite point `(r)`, followed by the Section-6 suspension definition, gives
`Gamma_r=pi^{-1}((r))`.  The point `(r)` is closed in `Spec Z`; hence
`Gamma_r` is closed in `X_susp`.

For `p != q`, the two packets are disjoint by Theorem 6.1.  In their finite
union, each packet is the complement of the other closed packet, hence is
relatively open as well as relatively closed.  Paper 9 says that the subspace
topology on each component is indiscrete.  It follows directly that a subset
of `Gamma_pq` is open exactly when it is a union of whole components.  This is
precisely the coproduct topology, and the canonical component-inclusion map
from `Gamma_p coproduct Gamma_q` is a homeomorphism.

Now fix `x in Gamma_r`.  Since `Gamma_r` is an ambient closed set containing
`x`,

```text
closure_X_susp({x}) subset Gamma_r.
```

Paper 9 proves that the constant sequence at `x` converges to every point of
`Gamma_r` in its actual subspace topology.  The inclusion into `X_susp` is
continuous, so every such point lies in the ambient closure of `{x}`.  The
reverse inclusion follows, proving equality.  The closure formula determines
the specialization relation without any first-countability assumption or
unlicensed replacement of nets by sequences.  The finite-set extension is
identical: a finite union of disjoint closed packets makes every component
clopen in that union.

## 5. Exact prequotient closure criterion

Paper 9 proves that

```text
rho:Y->X_susp
```

is an open continuous quotient map.  Any open continuous surjection satisfies
the exact identity

```text
rho^{-1}(closure_X_susp(A)) = closure_Y(rho^{-1}(A))
```

for every subset `A` of the quotient.

The usual continuity inclusion is one direction.  For the reverse direction,
if an open neighborhood `V` of `y` misses `rho^{-1}(A)`, then `rho(V)` is an
open neighborhood of `rho(y)` and also misses `A`; hence `rho(y)` is not in
`closure(A)`.  This proves the identity.

For `A=Gamma_r`, saturation gives `rho^{-1}(A)=Z_r`.  Thus the protocol's
P14-1 closure test can be carried out entirely before quotienting:

```text
rho^{-1}(closure(Gamma_r)) = closure(Z_r).
```

The continuous base projection already makes `Z_r` and `Gamma_r` closed, so
no cross-prime approximating net exists from one packet to another.  This is a
source theorem on the named owner, not a conclusion from the choice-dependent
`U_r/H_r` coordinates.

## 6. Tagged-coproduct adjudication

| Question | Verdict | Reason |
|---|---|---|
| Is `TAGGED-COPRODUCT-PQ` automatically the source owner by definition? | no | The protocol correctly treats it as a control. |
| Is the canonical map from that control to the actual two-packet union a homeomorphism? | yes | Closed source fibres plus Paper-9 indiscreteness prove it. |
| Is this comparison source-derived? | yes, for every finite packet set | It uses the actual ambient projection and inherited topology. |
| Does it prove that the all-prime periodic locus has the discrete coproduct topology? | not by the finite argument alone | An infinite union of closed components need not make each component relatively open. |
| Does it contradict Paper 10? | no | Paper 10 withheld the comparison; it did not prove a mismatch. |

There is a promising source-level route for the all-prime step.  On the
finite-field periodic locus, evaluation at the base integer `p` is `0` on the
`p`-fibre and has modulus `1` on every other prime fibre, because nonzero
finite-field elements map to roots of unity.  Pointwise convergence therefore
suggests a relative clopen separation of each checked prepacket before the
Galois quotient, colimit, and suspension quotient.  The full proof must track
that `0`/unit separation through each of those exact maps and through the
inductive-limit topology.  It may not replace this check with the label set or
with Deninger's non-homeomorphic global decomposition bijection.

If that stagewise argument closes, it yields the substantive candidate

```text
Per_Ef ~= coproduct_{p prime} Gamma_p,
K0(Per_Ef) ~= Primes_discrete,
```

on the actual owner.  That is the appropriate next proof target.  It is not
counted as proved by this two-prime precheck.

## 7. Source ceiling and standalone risk

The current source supplies enough topology to decide the finite-packet
question, but it does not state the resulting theorem.  It also does not hand
Paper 14 the following claims:

1. a classification of all subsets `S` of primes for which
   `union_{p in S} Gamma_p` is open or closed in `Per_Ef`;
2. an exact proof that the all-prime actual union is the tagged topological
   coproduct;
3. the topology of the global `T0` quotient of `Per_Ef`;
4. closures in the full suspension of arbitrary infinite packet subfamilies;
5. a new collective-closure theorem merely by restating Deninger's Theorem
   8.2.

The strongest hostile-review objection is therefore:

> The two-prime theorem is a short corollary of a continuous base projection,
> closed points of `Spec Z`, and Paper 9's fixed-prime result; Paper 10 already
> proves every generic consequence of a tagged coproduct.

That objection is decisive against a standalone paper whose center is only
the two-prime theorem.  It is not a reason to stop the proof pipeline, because
the fail-fast theorem validates the owner and opens a concrete all-prime
question.  Standalone status must remain `HOLD` until the actual global
comparison and its nonredundancy against Papers 9--10 receive independent
review.

## 8. Severity and gate record

### Critical findings

None.

### Major findings

None against the frozen protocol.  The protocol already contains the correct
`NOTE_OR_MERGE` fallback if the work stops at a formal finite coproduct.

### Minor findings

None requiring a protocol amendment.  In the full proof, specialization
notation should be defined by an explicit closure formula because the order
convention is reversed in parts of the literature.

### Gate matrix

| Gate | Result |
|---|---|
| exact-byte identity | PASS |
| source owner fixed to `Spec Z`, `E_f`, actual suspension | PASS |
| arbitrary `p != q` topology decidable | PASS |
| cross-prime closure/specialization | PASS: none |
| actual-vs-tagged two-prime comparison | PASS: canonical homeomorphism |
| source underdetermination | REFUTED for the finite-packet gate |
| authorization to begin full symbolic proof | **GO_TO_FULL_PROOF** |
| all-prime topology and global `T0` quotient | UNPROVED / next gate |
| standalone paper | HOLD |
| controls, Route A/B, manuscript, release, Git/public sync | BLOCKED / false |

Final Phase-1 verdict: **PASS — C0 / M0 / m0; GO_TO_FULL_PROOF.**
