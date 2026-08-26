# Paper 12 standalone-strength amendment v3

Date: **2026-08-15**

Status: **SUBMITTED FOR EXACT-BYTE METHODOLOGY / DEVIL / SOURCE RE-LOCK**

## 1. Trigger and immutable history

The stable Phase-3 v2 mathematics passed its formal peer and controls reviews,
but the independent standalone reviewer triggered the protocol's semantic
routine-reduction stop. The exact disagreement is frozen in
`phase3_disposition_gate.md`. No v2 proof, control, source, or review artifact
is modified or reinterpreted.

The v3 repair addresses one exact weakness: the pointed quotient functor of
v2 intentionally sends every strict morphism at fixed period to the unique
basepoint-preserving target arrow and is not faithful. V3 adds a central
unpointed categorical reconstruction that retains those arrows.

## 2. New target category and canonical standardization

Let `Hom_R^std` be the category whose objects are standard Hausdorff
transitive right `R`-homogeneous spaces with stabilizer `LZ`, `L>0`, and whose
morphisms are continuous strictly `R`-equivariant homeomorphisms. No
basepoint is part of an object or morphism.

For an existing strict marked object `(G=X rtimes R,c)` define, for a chosen
unit `x`,

```text
q_x:R -> X,      q_x(t)=x dot t.
```

Put the quotient topology transported by `q_x` on the same underlying set
`X`; denote that retopologized space by `Std(G,c)`. The v3 proof must show:

1. if `x'=x dot u`, then `q_(x')=q_x o T_u`, where `T_u(t)=u+t`; therefore
   the transported topology is independent of `x`;
2. `Std(G,c)` is a standard Hausdorff transitive `R`-homogeneous space and is
   (noncanonically pointed) isomorphic to `R/H`, `H=Per_x([c])=LZ`;
3. the identity on the underlying set
   `Std(G,c) -> X_actual` is continuous, while its inverse is not for a
   nontrivial owner;
4. a strict marked groupoid isomorphism is uniquely
   `F(x,t)=(F_0(x),t)`, and `F_0` is an equivariant homeomorphism between the
   standardizations;
5. conversely every equivariant homeomorphism between the standardizations
   uniquely lifts by that formula to a strict marked groupoid isomorphism.

Thus

```text
Std:C_str -> Hom_R^std,       Std(F)=F_0
```

must be proved full and faithful. The inverse construction `Indisc` puts the
indiscrete topology on a standard homogeneous-space unit set and forms its
range-first action groupoid with `c(x,t)=t`. V3 must prove `Std` and `Indisc`
are inverse up to the explicitly displayed natural isomorphisms (and are
strict inverses under the frozen concrete-object convention). This is the
new standalone centre.

## 3. Automorphisms and relation to the v2 pointed shadow

For `H=LZ`, v3 must prove

```text
Aut_Cstr(G,c) ~= Aut_R(Std(G,c)) ~= R/H,
```

where `[u]` acts by unit translation `x |-> x dot u` and lifts to
`(x,t)|->(x dot u,t)`. Composition corresponds to addition in `R/H`, and
distinct classes give distinct strict automorphisms.

The existing pointed functor `S` remains correct but is explicitly demoted to
a basepointed shadow of `Std`: choosing `x` identifies `Std(G,c)` with
`(R/H,[0])`, while changing `x` rotates that basepoint. Forgetting all unit
translations is exactly why `S` is nonfaithful. V3 may not call `S` an
equivalence.

## 4. Scope and ownership

- The theorem is generic for the already frozen normalized transitive strict
  lattice objects; arithmetic credit remains absent there.
- The rational-Witt orbit/packet application may instantiate the theorem at
  `H=(log p)Z`, but Deninger still owns the source clock/stabilizer and Paper 9
  owns the actual inherited topology.
- `Std` is a Paper-12 marked-action reconstruction, not the Hausdorff or
  completely-regular reflection of the actual topology; those reflections
  remain singletons by Paper 10.
- The target topology is never transported back as the actual topology.
- No result concerns the global suspension, a cross-prime union, traces,
  completions, determinants, or Route B.

## 5. New deterministic controls

Add the frozen control `STD-EQUIV-L` for every `L` in the existing `PER-L`
set. It must verify, on deterministic finite cyclic quotient models:

- basepoint independence of the transported quotient topology;
- all unit translations are distinct, equivariant, and closed under
  composition/inverse;
- every tested equivariant standard homeomorphism lifts uniquely to a strict
  marked groupoid automorphism and every strict automorphism descends;
- the pointed shadow maps all translations to its unique pointed identity;
- `Std(Indisc(Y))=Y` and `Indisc(Std(G))=G` at the frozen typed fields; and
- label permutation leaves the equivalence signature unchanged.

The existing stdlib, exact/symbolic, strict-verification, two-fresh byte
identity, no-cache, no-target-data, and source-proof-separation contracts
remain unchanged. Controls are finite witnesses, not proofs.

## 6. Source, novelty, and standalone gates

Before the v3 proof may be counted, a bounded primary/authoritative audit must
check standard transitive topological-group homogeneous spaces, action-groupoid
equivalences induced by equivariant homeomorphisms, and any direct precedent
for canonical retopologization of an indiscrete marked action groupoid. The
only allowed negative wording remains `SUPPORTED_WITHIN_SEARCH`.

`STANDALONE_PASS` now requires the already proved v2 package **and** the v3
full-and-faithful/equivalence theorem with automorphism classification,
updated controls, and independent closure of the prior M1. If the new theorem
collapses to a cited standard result with no owner-specific categorical
content, or if the prior reviewer does not close M1, the result remains
`NOTE_OR_MERGE`.

## 7. Route and release boundary

No new Route owner is added. The existing
`DEN-EF-STANDARD-PERIOD-QUOTIENT-P` record must describe both the canonical
unpointed standardization and its pointed shadow, with arithmetic origin still
only a copied source period relation. A0/A1 ceilings, A2/A3/A4 failures,
`Route_B_invocation=false`, and all forbidden-data fields remain unchanged.

Route, manuscript, and release remain blocked until exact-byte v3 re-locks,
the targeted source/novelty audit, the v3 proof/control addendum, and
independent mathematical plus standalone reviews all pass.

## 8. Exact amended tuple

The final protocol, candidate, pipeline, disposition-gate, and this amendment
hashes are recorded in the three independent v3 re-lock reports after all
status bytes are frozen. No reviewer may bind an intermediate tuple.
