# Paper 9 research protocol — separation of Deninger prime packets

Protocol date: 2026-08-14 (Asia/Shanghai)  
Status: **PHASE 1 AMENDED v1 — EXACT-BYTE RE-LOCK PENDING**  
Primary candidate: `DEN-EF-PACKET-QUOTIENT-TOPOLOGY-P`  
Parent object: Deninger's rational-Witt `Spec Z`, finite-kernel subsystem `E_f`

## 1. Research question

For a fixed rational prime `p`, give the actual inherited topology—not a
retopologized model—on Deninger's periodic packet `Gamma_p` and answer:

> Is the restricted diagonal equivalence relation defining `Gamma_p` closed,
> or does simultaneous real/profinite approximation force the packet (and
> possibly each inherited periodic orbit) to fail `T0`, `T1`, and Hausdorff
> separation?

This is the next theorem obligation left by Paper 8.  The paper succeeds with
either a positive separation theorem or a rigorous separation obstruction.

## 2. Frozen source object

Set

```text
X_0 = Spec Z,
C = the complex number field,
E = E_f (finite-kernel characters),
Xcheck = Xcheck_0(C)_{E_f}.
```

The source suspension is

```text
X_flow = (Xcheck x R_{>0}) / Q_{>0}
```

with Deninger's right diagonal action

```text
(P,u) q = (F_q P, q^{-1}u).
```

The topology on `X_flow` is the quotient topology, and `Gamma_p` has the
subspace topology inherited from `X_flow`.  No product topology, standard
circle topology, `B_p` topology, Borel replacement, or groupoid completion may
be substituted for this topology.

Let `x_p=(p)` be the closed point and let

```text
C_p^{E_f} subset Xcheck_0(C)_{E_f}
```

be Deninger's `Q_{>0}`-invariant packet fibre over `x_p` (his `C_{x_p}`
restricted to `E_f`; for `E_f` the restriction loses no packet point).  Freeze

```text
Z_p = C_p^{E_f} x R_{>0},
R_p = { ((P,u),(F_q P,q^{-1}u)) : P in C_p^{E_f}, u>0,
                                      q in Q_{>0} },
Gamma_p = Z_p/R_p.
```

This is the restriction of the global diagonal relation, not a relation
transported through a coordinate bijection.  Because the global quotient map
is open and `Z_p` is saturated, its restriction to `Z_p` is an open quotient
onto the subspace `Gamma_p`.  Consequently the quotient topology on `Z_p/R_p`
is exactly the inherited subspace topology.  This saturated-open-quotient
lemma is a theorem obligation and must be proved before P9-3 is used.

Fix a geometric point above `(p)` and an injective residue-field character
`chi`.  The exponent endomorphism ring of `Fbar_p^x` is
`Zhat_(p)=prod_{ell != p} Z_ell`.  Galois quotienting identifies unit exponents
along the closed procyclic subgroup `p^{Zhat}`.  These coordinates are proof
devices; source ownership remains with the character space and its quotient.

Object levels are frozen separately:

```text
Ptilde_a = (x,chi^a)              raw character point in the initial p-fibre,
P_a      = pi_G(Ptilde_a)         Galois-orbit point,
j(P_a)                            its point in the N-colimit Xcheck_0(C)_{E_f}.
```

For `q=m/p^k`, the expression `chi^{a q}` is interpreted elementwise on
`Fbar_p^x`; `p` is invertible on every finite cyclic subgroup.  Equality
`F_q(P_a)=F_m(P_a)` is allowed only after the Galois/packet quotient, where the
exact `p^Z` stabilizer acts.  It is never asserted as equality of raw
characters.

## 3. Frozen comparison objects

The following objects remain distinct.

1. `DEN-EF-PACKET-QUOTIENT-TOPOLOGY-P`: the actual inherited packet.
2. `DEN-EF-ORBIT-INHERITED-TOPOLOGY-P`: one actual `R_{>0}` orbit with its
   subspace topology inside the actual packet.
3. `DEN-EF-ORBIT-STD-CIRCLE-PROXY`: the separately imposed compact-Hausdorff
   circle `R/(log p)Z`; this is a control and may not borrow source topology.
4. `DEN-EF-PACKET-SET-PARAM`: Deninger's displayed set bijection using
   `Zhat_(p)^x/p^{Zhat}` and `R_{>0}/p^Z`; it is not frozen as a homeomorphism.
5. `DEN-EF-PACKET-ORBIT-QUOTIENT-Q-P`: the intrinsic topological quotient
   `Q_p=Gamma_p/K_p`, where `K_p=R_{>0}/p^Z` acts through the source flow.  It
   exists for every packet topology and is not identified with `B_p`.
6. `MOR-CC-Cp-INHERITED`: Morishita's adelic `C_p` with the subspace topology
   inherited from the exact adelic quotient; it must be audited directly.
7. `MOR-CC-Cp-STD-CIRCLE-PROXY`: `R_{>0}/p^Z` with its ordinary Hausdorff
   circle topology, imposed separately.  The word “isomorphic” does not by
   itself identify items 6 and 7 homeomorphically.

## 4. Pre-registered theorem targets

Labels `P9-1`--`P9-9` are Paper-9 theorem targets and must not be confused
with the Paper-3 `T0`--`T7` same-object certificate.

### P9-1 — simultaneous approximation lemma

Determine the closure of the diagonal image

```text
Z[1/p]_{>0} -> R_{>0} x Zhat_(p).
```

The strongest target is density.  A constructive CRT proof must specify an
increasing finite modulus, a positive numerator `m_j`, a denominator
`p^{k_j}`, real error, and profinite error.  No unproved appeal to “strong
approximation” is sufficient.

Full density in `R_{>0} x Zhat_(p)` is an independent arithmetic theorem.  It
does not imply convergence inside `E_f` when the profinite limit has infinite
kernel.

### P9-2 — character convergence and `E_f` domain

Split the claim.

1. For arbitrary `a in Zhat_(p)`, P9-1 is only an ambient approximation
   theorem; if `chi^a` has infinite kernel, the limit is outside `E_f` and
   supplies no source-topology credit.
2. For the packet proof, require `a in U_p=Zhat_(p)^x`.  For
   `q_j=m_j/p^{k_j}`, prove that every `chi^{b q_j}` has finite kernel in one
   fixed initial `p`-fibre and converges pointwise to `chi^{b a}`.  Then apply,
   in order, the continuous Galois quotient and the named open colimit-stage
   inclusion.  No convergence may be proved after silently discarding the
   denominator by a quotient-level stabilizer identity.

Every topology arrow and every object level must be named.

### P9-3 — closure of a suspension class

For source points represented by `(chi^b,u)` and `(chi^a,v)`, determine
whether representatives of the single diagonal class of `(chi^b,u)` can
converge to `(chi^a,v)`.  The proof must use the frozen right-action sign and
must separately prove that the two quotient points are distinct when needed.

Before universalizing this calculation, prove the **unit-exponent
exhaustiveness lemma**: Deninger's set theorem gives every point of `Gamma_p`
a representative `[P_a,u]` with `a in U_p`, and gives the exact equivalence
condition modulo `p^{Zhat}` and the time stabilizer `p^Z`.  The topology is not
transported through that parametrization.  Only after this set-level lemma may
P9-3 quantify over every ordered pair of packet points.

### P9-4 — separation classification

Classify the inherited topology of:

```text
one actual periodic orbit,
one actual prime packet Gamma_p,
the quotient Q_p = Gamma_p/(R/(log p)Z), with its quotient topology.
```

The result must distinguish `T0`, `T1`, Hausdorff, quasi-compact, and LCH.
“Compact” may not be silently read as compact Hausdorff.

`Q_p` is always a meaningful topological quotient of the continuous compact
flow-kernel action.  Under `CONFIRM_STRONG`, an indiscrete `Gamma_p` forces
`Q_p` to be indiscrete.  `CONFIRM_ORBIT` alone supplies no transverse
classification of `Q_p`.  In every case `Q_p` remains distinct from `B_p` and
earns no automatic T3--T7 or analytic Route credit.

Here `LCH-Hausdorff` denotes the frozen standard groupoid hypothesis.  If a
non-Hausdorff space is locally quasi-compact under another convention, report
that property separately; failure of Hausdorffness alone is not called
failure of every notion of local compactness.

### P9-5 — set model versus topological model

Audit the continuous/set bijections used by Deninger and Morishita.  If an
actual inherited orbit or packet is not Hausdorff, prove exactly why the
standard-circle or product parametrization is not a homeomorphism.  If it is
Hausdorff, prove continuity of the inverse rather than invoking compactness
without a Hausdorff target.

### P9-6 — equivalence-relation theorem

State the result directly for the restricted diagonal orbit relation in
`Xcheck x R_{>0}`: closed, non-closed, or not testable.  Give an explicit
convergent sequence/net of related pairs if non-closedness is claimed.

### P9-7 — groupoid/completion consequence

Determine only the consequences licensed by P9-4/P9-6 for the standard
second-countable LCH-Hausdorff action-groupoid framework.  A non-Hausdorff
result may refute that framework but does not by itself define a replacement
non-Hausdorff C*-algebra, Haar system, trace, or determinant.

### P9-8 — deterministic controls

Implement target-free finite witnesses for the approximation lemma, character
values on finite cyclic groups, the action-sign identity, distinctness modulo
`p^{Zhat}`, and the following controls:

- retain only the stabilizer subgroup `p^Z`;
- impose the standard circle topology by definition;
- truncate the CRT modulus;
- vary `p` without changing the theorem statement;
- use a deliberately wrong time-action sign;
- replace the finite-kernel domain by an illegal infinite-kernel limit.

Finite controls illustrate the exact proof and catch sign/domain bugs; they do
not prove an infinite topological theorem.

### P9-9 — ownership and Route correction

Issue new versioned Route-A records for every object whose topology/ownership
changes.  Historical Paper-8 records remain immutable.  Local proxy formulas
may survive on `DEN-EF-ORBIT-STD-CIRCLE-PROXY`, but no coordinate from that
proxy may be spliced into the actual packet or orbit.

## 5. Two-sided decision rule

The primary topology verdict is assigned before any downstream analytic
claim:

```text
CONFIRM_STRONG:
  every singleton closure in Gamma_p is all of Gamma_p, hence the packet is
  indiscrete and non-T0;

CONFIRM_MINIMAL:
  an explicit singleton is not closed, hence Gamma_p is not T1/Hausdorff and
  the frozen LCH-Hausdorff packet framework is refuted;

CONFIRM_ORBIT:
  every inherited periodic orbit is indiscrete, but the transverse
  unit-exponent exhaustiveness or universal two-point step for Gamma_p remains
  open;

REFUTE_OBSTRUCTION:
  the proposed approximation/convergence mechanism fails at a named arrow and
  a closed-relation or Hausdorff theorem is proved instead;

NOT_TESTABLE:
  the source topology or action cannot be reconstructed sufficiently to decide
  either side.
```

The protocol must not move from `CONFIRM_MINIMAL` to `CONFIRM_STRONG` merely
because the stronger statement is aesthetically attractive.

## 6. Same-object certificate boundary

`T0`--`T7` retain their Paper-3 meanings.

| Field | Phase-1 status | Required closure |
|---|---|---|
| `T0` object identity | PASS | exact Deninger `Spec Z`, `E_f`, fixed `p`, inherited quotient |
| `T1` topology/Borel | PRIMARY TARGET | exact quotient/subspace topology; no proxy |
| `T2` flow/clock | PASS set-theoretically | right action and `log p` stabilizer; topological consequences open |
| `T3` groupoid/Haar | WITHHELD | depends on the separation theorem |
| `T4` measure | NOT INVOKED | no transverse probability selected |
| `T5` representation/trace | NOT INVOKED | Paper-8 local proxy cannot lend ownership |
| `T6` test algebra/formula | NOT INVOKED | only finite topology controls in this paper |
| `T7` arithmetic promotion | PASS only for source label/clock | no trace, weight, determinant, or spectral promotion |

## 7. Route ceiling

This is a topology/primitive-orbit obstruction paper.

- A0 may retain `A0_ANALYTIC_ARITHMETIC_ORIGIN` for the source packet.
- A1 is re-evaluated from the inherited topology and cannot exceed
  `A1_WEAK`; a nonseparation obstruction may force `A1_FAIL` for a frozen
  LCH-Hausdorff action-groupoid candidate while leaving set-theoretic
  closed-point/clock statements intact.
- A2, A3, and A4 are `A2_FAIL`, `A3_FAIL`, and `A4_FAIL` unless a separate
  theorem unexpectedly supplies their complete inputs.
- Route B is not invoked; no Route-B YAML is permitted.

No result in this paper is a determinant identity, analytic continuation,
functional equation, quantization, self-adjointness theorem, or
Hilbert--Polya realization.

## 8. Data and contamination lock

Allowed:

- retained Deninger/Morishita primary manifestations and authoritative later
  versions;
- general topology, profinite groups, CRT/approximation, and transformation
  groupoid references;
- exact deterministic integer arithmetic.

Forbidden:

- Riemann-zero tables;
- fitting to zeta zeros or prime statistics;
- redefining the topology after seeing the result;
- using a standard circle/product topology as if source-owned;
- borrowing Paper-8 trace credit before `T1`--`T5` transport is proved;
- treating a finite CRT grid as proof of density;
- calling a non-Hausdorff quotient a noncommutative space and then importing a
  trace without a theorem.

## 9. Paper-8 versioned correction matrix

Paper 8 and its Stage-8 YAMLs remain immutable historical records.  Paper 9
must adjudicate the following branches separately and create new Stage-9
records with explicit `supersedes` or `retypes` links.

| Paper-8 branch | If P9 topology obstruction is proved | What is preserved |
|---|---|---|
| actual inherited-orbit homeomorphism, Hausdorff/LCH, Haar/completion, and downstream actual-orbit ownership | superseded/refuted at the failed topology premise | source prime label, exact `log p` clock, and set-theoretic isotropy |
| algebraic Poisson/Floquet, regular FNS, and finite-corner calculations | retyped to `DEN-EF-ORBIT-STD-CIRCLE-PROXY` after explicit standard-circle retopology | internal proxy theorems and controls, but no actual-source T1--T6 transport |
| packet action-groupoid branch | frozen standard second-countable LCH-Hausdorff route refuted | no claim that every future non-Hausdorff completion, Haar theory, or trace is impossible |
| coefficient-one positive-time scalar Radon ledger | no topology dependency; preserved unless independently refuted | its typed A1 analytic statement only; no packet operator ownership |

The exact failed Paper-8 proof locator and the first downstream claims that use
it must be recorded in the proof audit and manuscript.  In particular,
actual-source normal-extension statements become `NOT_TESTABLE` when their
completion loses its topology gate; the proxy no-normal theorem remains a
separate valid calculation.

## 10. Adversarial controls and stop rules

Mandatory attacks:

1. test the inverse/right-action sign;
2. test whether `q_j` really remains in the `E_f` domain;
3. test Galois quotient distinctness modulo `p^{Zhat}`;
4. test whether convergence occurs in one fixed colimit stage;
5. test whether a source use of “circle” or “isomorphic” is topological;
6. test the same logic on the `p^Z`-only standard suspension, where an
   indiscrete conclusion must fail;
7. test whether the argument proves every unrelated suspension non-Hausdorff;
8. test whether a continuous map to Morishita's adelic orbit has been given a
   Hausdorff target without evidence.

Stop and revise the object if any map in P9-2/P9-3 is only set-theoretic.  Stop
the analytic branch after a negative separation result; do not improvise a
non-Hausdorff operator algebra in the same paper.

## 11. Planned artifacts

```text
notes/research_protocol.md
notes/candidate_lock.md
notes/phase1_*_review.md
notes/source_audit.md
notes/proof_audit.md
notes/composition_blueprint.md
code/packet_separation_controls.py
code/test_packet_separation_controls.py
experiments/reproduce.sh
results/*.csv
results/packet_separation_manifest.json
paper/manuscript.tex
paper/references.bib
paper/paper.pdf
```

All source PDFs require read-integrity preflight and remain local-only unless
the exact manifestation has a documented redistribution licence.
