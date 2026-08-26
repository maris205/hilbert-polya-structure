# Paper 17 Phase-1 exact-byte proof gate

Status: **PASS TO ONE SYMBOLIC PROOF — C0/M0/m0**  
Version: `P17-P1-GATE-v1.0`  
Date: 2026-08-16 (Asia/Shanghai)  
Publication ceiling: `TECHNICAL_NOTE_CANDIDATE`  
Standalone status: `HOLD`  
Controls, Route A/B, manuscript, release, Git, and public synchronization:
`false`

## 1. Exact authority tuple

```text
Papers 14--18 historical batch design lock
  sha256:2d38bb69024aa91eb683e89f808568565439f2d82fcdf81bd661b4749eed7ad8
Papers 14--18 batch amendment v1
  sha256:afd933440abed3eff4872d6ffe671213d531cb6ceb4c08ebd87c3048d37b1802
Paper-17 base research protocol
  sha256:5ca581cff6f2fe088744a522646466ef2f5ce124ad3cdf50367cc5ed33347cea
Paper-17 candidate lock
  sha256:2db53e92961cdfa7e43e4e06b7cdd81a2d87d97d15957d793b720bd86c71a604
Paper-17 amendment v1
  sha256:3ada0e70a0d3f53bd68e1a44e63c24870215987176d538c513400dc99ef95f3d
Paper-17 amendment v2
  sha256:2ce675880b171ee598f8a796edf55f9c695e2e6d0973620371d3ba460c7d1957
final framework/source precheck and re-lock
  sha256:9991dc5e27ea8577d4236d38feeb63bfc110e3a3b242b3c17be8607da01f9e64
methodology/devil/nonredundancy review
  sha256:811e51fc96baedf81a3e4185fa49519ff6c15bad37d866d8186054a24c25653e
independent mathematical/devil/domain review
  sha256:bdf89476d49ab8a5b3bb7deff9f8738079bd185fd38a00bc1c9ba175677ad6d4
```

All inputs were rehashed before this gate was frozen.  Amendments v1 and v2
supersede only the conflicting base claims identified in their precedence
clauses.  The batch amendment assigns Paper 17 the sole possible Technical
Note slot but does not pre-approve a final note or manuscript.

## 2. Closed Phase-1 design

Let `X` be a nonempty globally indiscrete space and let a locally compact
topological group `H` act continuously on the right.  The joint theorem uses

```text
G(X,H)=X_ind rtimes H.
```

The exact target is:

```text
B(G(X,H)) ~= B_cont(H),
O(G(X,H)) ~= O(H),
base frame ~= 2,
```

where the first equivalence uses the selected open-groupoid equivariant-
sheaf convention and the second is first a direct bare open-set involutive
quantale calculation.  Multiplicative open-quantal-frame/localic
reconstruction additionally requires the explicit comparison

```text
q_H:O(H) tensor O(H) -> O(H x H)
```

in the exact locale convention; local compactness is the frozen sufficient
domain.

Required examples and comparisons are:

- actual time `H=R`: connectedness forces every continuous action on a
  discrete sheet set to be trivial, hence the classifying topos is `Set`;
- negative time `H=Z`: nontrivial discrete `Z`-sets prevent the same
  conclusion;
- actual real-time groupoid: open, non-etale, and its open quantal frame is
  nonunital;
- standard circle `S_L=R/(LZ)`: classifying topos `B(LZ)~=BZ` and base frame
  `O(S_L)`;
- unmarked dilation erases numerical `L`, while a separately registered
  strict real-time marker forbids that dilation; and
- point-set information loss occurs in the nonsober `Top -> Loc` reflection,
  not through failure of Protin--Resende reconstruction of the localic
  groupoid it receives.

## 3. Authorized proof artifact

This gate authorizes exactly one symbolic ledger:

```text
papers/17-open-groupoid-interfaces/notes/phase2_topos_quantale_proofs.md
```

It must prove, in order:

1. continuity, openness, composable-pair topology, and non-etaleness of the
   actual real-time action groupoid;
2. the full classification of etale objects over `X_ind` as whole-`X`
   sheets and explicit quasi-inverse functors for
   `B(G(X,H)) ~= B_cont(H)`;
3. the connected-`R` result and the disconnected-`Z` falsifier;
4. the arrow-open, product, involution, joins, right-sided/base-frame, and
   unit/nonunit calculations;
5. the exact `q_H` input before invoking localic reconstruction;
6. the actual-versus-standard topos and quantale comparison;
7. the unmarked dilation and strict-marker obstruction; and
8. the fixed-prime application only after the generic theorem.

The proof must state handedness and action conventions, must not invoke an
etale-only inverse-quantal-frame equivalence, and must fail closed if a
selected theorem requires an unregistered Hausdorff or second-countability
hypothesis.

## 4. Owner and source firewall

- Paper 9 supplies actual fixed-prime indiscreteness and the literal
  stabilizer only.
- Paper 10's separated/measurable collapse is not a topos theorem.
- Paper 11's arrow and composable-pair formulas may be inherited but carry
  no new credit.
- Moerdijk/Forssell own the open-groupoid equivariant-sheaf framework.
- Protin--Resende own open quantal-frame/localic reconstruction at their
  exact domain; Paper 17 must not attribute the preceding spatial-to-localic
  loss to failure of their theorem.
- Neither output is a C*-algebra, measure, trace, standard topology, or
  strict time marker unless separately registered.

## 5. Downstream and publication rule

Independent proof review remains mandatory.  Paper 17 is not a standalone
paper candidate at this gate.  It may proceed later only as the batch's sole
Technical Note if both topos and quantale branches, the standard comparison,
and the strict/unmarked boundary survive exact proof and source review.
Omitting one branch forces `NOTE_OR_MERGE`; it does not create a second note.

## 6. Authorization boundary

This gate authorizes the single symbolic proof ledger and read-only review
preparation.  It does not authorize deterministic-control design or
implementation, Route evaluation, manuscript or figure construction,
release, Git operations, archive creation, or public synchronization.

```text
PHASE1_GATE=PASS
CRITICAL_FINDINGS=0
MAJOR_FINDINGS=0
MINOR_FINDINGS=0
SYMBOLIC_PROOF_AUTHORIZED=true
AUTHORIZED_PROOF_PATH=papers/17-open-groupoid-interfaces/notes/phase2_topos_quantale_proofs.md
TECHNICAL_NOTE_CANDIDATE=true
STANDALONE_PASS=false
CONTROLS_AUTHORIZED=false
ROUTE_A_AUTHORIZED=false
ROUTE_B_AUTHORIZED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_PUBLIC_SYNC_AUTHORIZED=false
```
