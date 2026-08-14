# Paper 8 Phase-2 typed-amendment independent DA re-lock

Review date: 2026-08-14  
Verdict: **PASS**  
Findings: **0 Critical / 0 Major / 0 Minor**  
Scope: exact-byte and reasoning review of the Phase-2 finite-corner,
local/packet-map, and character-sign amendment.  This review performs no
Phase-3 proof, grants no P8 or Route credit, and edits no active lock.

## 1. Exact reviewed tuple

| Artifact | Recomputed SHA-256 | Result |
|---|---|---|
| `research_protocol.md` | `e1fe94efb8451142264a73a7ce3093daa66589569c9238ba7719ab3736dccece` | MATCH |
| `candidate_lock.md` | `f890ad69e2b9c329b72daf2464b54728ebceac212f24aaa94020366d0a0c7057` | MATCH |
| `phase2_domain_amendment.md` | `0b6572a2d0ad99521bb934f9ef4f9599a4c6e0c338e6e6df4a600894b80b70bd` | MATCH |
| `phase2_groupoid_source_audit.md` | `39fcd460018a38a2b23107b0cb2f59195b7fa4110ad6742b66a334af0f4bad42` | MATCH |
| `phase2_trace_source_audit.md` | `101d447a238cbf9ec6ea33a78b3f6be7456a1be30fdc206e13db91697d75c5f0` | MATCH |

The retained Williams full text used for the independent convention check is
`sources/grp-williams-crossed-products-draft3.1.pdf`, SHA-256
`3dbc1fb9e96191a278e0d59feb4981d3bbea4faa4df609d1886c81125bffe9c2`.

## 2. Finite-corner proof-target sufficiency

**PASS, conditional exactly where the locks say it is conditional.**

The amendment now uses the correctly typed one-orbit algebra

```text
A_L ~= C(T) tensor K(H),       Z(A_L)=0,
p=1 tensor e,                  p A_L p ~= C(T),
tau_theta=delta_theta tensor Tr,  tau_theta(p)=1,
```

with `e` rank one.  The exact owners are stated at amendment lines 28--61,
protocol lines 351--403 and 478--488, and candidate lines 120--149.  The
argument is sufficient as a preregistered target for the following reason:

1. the still-unproved fixed-map theorem must identify the image of this same
   `p` in `M_L^reg` and prove `p M_L^reg p ~= L-infinity(T,Haar)`;
2. any normal extended-positive extension agreeing with `tau_theta` has value
   one on `p`;
3. compression is therefore a finite normal positive functional on the
   unital corner, hence a bounded normal functional there; and
4. its restriction to `p A_L p` is point evaluation, contradicted by a
   decreasing continuous peak sequence whose Haar-`L-infinity` infimum is
   zero.

The lock does not assume any of those Phase-3 steps.  In particular, an
abstract `C*`-isomorphism or Morita equivalence is not substituted for the
fixed represented closure.

The previous object-splice risk is also closed.  The local map

```text
A_L -> A_(L,r) -> M_L^reg
```

is separated from the conditional packet map

```text
C*(G_p) -> C*_r(G_p) -> M_(p,nu)^reg.
```

The rank-one projection belongs only to `A_L`.  Amendment lines 129--133,
protocol lines 398--403 and 487--488, and candidate lines 136--149 explicitly
forbid using the local obstruction to refute the packet question without a
packet restriction/disintegration same-map theorem.  Failure of that bridge
is `NOT_TESTABLE`, not `REFUTE`.

## 3. Ordinary, normal, singular, and extended-positive domains

**PASS.**  The active tuple keeps the four roles distinct:

- `Tr o pi_(L,theta)` is first an extended-positive lower-semicontinuous
  `C*`-weight on its positive pullback domain; dense definition,
  semifiniteness, traciality, compact image, and the `a_f` linear trace domain
  remain proof obligations (protocol 333--349 and 376--390; trace audit
  175--244).
- A hypothetical extension to `M_L^reg` is the same extended-positive
  functional along the same map.  Normality is tested only after the von
  Neumann owner is fixed.
- Finiteness on `p` converts the compressed normal weight into an ordinary
  bounded normal positive functional; the full character weight is not
  incorrectly declared finite.
- On the multiplier centre `C(T) tensor 1`, the uncompressed character weight
  is generally infinite.  The active tuple never uses it as the bounded
  witness.
- A singular positive state extension from `C(T)` to `L-infinity(T,Haar)` is
  kept separate from literal point evaluation on an `L-infinity` equivalence
  class and from the no-normal-extension theorem (amendment 57--61; protocol
  387--396 and controls 9/14).

Thus “ordinary trace,” “normal extension,” “singular extension,” and
“semifinite extended-positive weight” do not borrow one another's domains.

## 4. Choice dependence and source ownership

**PASS.**  The groupoid audit records that the concrete
`C(T) tensor K` trivialization is noncanonical and choice-dependent
(groupoid audit 146--151).  The active amendment correspondingly labels the
rank-one projection/trivialization as a proof device, demands projection-choice
independence of the conclusion, and does not promote `p` to source data
(amendment 57--61; protocol 385--390).

The trivial isotropy character remains distinguished algebraically before any
target comparison.  That distinction selects neither a transverse measure nor
a packet or cross-prime mass.  No choice-dependent trivialization, matrix unit,
or singular state is inserted into the source-owned fields.

## 5. Induced-character sign re-lock

**PASS.**  The retained Williams source defines induced functions by

```text
xi(u+rL)=chi_theta(rL)^(-1) xi(u)
```

and, in the present unimodular additive case, the induced unitary by
`(U_t xi)(u)=xi(u-t)` (printed p. 153, Proposition 5.4, equations (5.2)--(5.3);
Theorem 5.12 on printed p. 161 identifies this induced representation with the
Green-module construction).

For `chi_theta(rL)=exp(ir theta)`, a mode `exp(i k u)` therefore satisfies
`k=(2pi n-theta)/L`, and `U_t` contributes `exp(-ikt)`.  With the frozen
Fourier transform, the eigenvalue is
`fhat((2pi n-theta)/L)`.  Shifted Poisson summation then gives

```text
sum_n fhat((2pi n-theta)/L)
  = L sum_r f(rL) exp(+ir theta).
```

The protocol (88--103, 311--331, 531--535, 679--685), candidate
(179--203), and amendment (72, 79--103) apply the sign change simultaneously
to the Floquet frequency and return phase.  Dual-Haar cancellation and the
trivial-character value are unchanged.  The choice is source-convention-led
and target-free.  The older sign in the trace source audit is explicitly
conditional there on the later representation calculation; the typed
amendment activates its prescribed simultaneous `theta -> -theta` branch
rather than silently rewriting evidence.

## 6. Primary outcomes, controls, and Route drift

**PASS; no semantic drift detected.**

- The primary question and the mutually exclusive
  `CONFIRM`/`REFUTE`/`NOT_TESTABLE` meanings remain at protocol 58--81.
- Candidate IDs, local/finite/positive-time records, common length/probability
  normalization, target-free controls, and T0--T7 ownership gates remain
  separate.
- The finite-corner and sign corrections alter only the typed proof domain and
  the already-preregistered character-coordinate branch.  They do not fit a
  phase, mass, clock, or normalization to an Euler or zero target.
- A1 remains the maximum possible positive analytic credit; every record has
  `A2_FAIL` or `A2 NOT_TESTABLE`, A3 remains failed, and A4/Route B remain
  closed with `route_b_invocation_allowed=false` (protocol 600--617;
  candidate 225--245).

## 7. Residual Phase-3 obligations, not re-lock defects

The following remain open exactly as required and receive no credit here:

1. the represented decomposition of `M_L^reg`, the image of `p`, and the
   identification of `p M_L^reg p`;
2. compact-image factorization, dense semifinite pullback domains, and
   trace-class membership of each `a_f`;
3. the fixed-representation Floquet diagonalization, shifted Poisson identity,
   and dual-Haar sum/integral interchange;
4. the decreasing-peak no-normal-extension lemma and any separately claimed
   singular-state existence/nonuniqueness result; and
5. every packet restriction/disintegration/compression bridge and the full
   T0--T7 packet ownership audit.

## 8. Final decision

**PASS.**  The exact tuple closes the centre/corner error, freezes the
source-forced sign consistently, and prevents a one-orbit proof from being
spliced into the packet primary outcome.  No Critical, Major, or Minor
preregistration defect remains in the reviewed scope.  Phase 3 may begin only
after the mainline records this re-lock; this report itself proves none of
P8-1--P8-9.

## Final mechanical status-byte addendum

Check date: 2026-08-14  
Decision: **PASS**

Final active tuple:

| Artifact | SHA-256 |
|---|---|
| `research_protocol.md` | `e1149ebd9609de24e0df00dcaeafdbcd31ee973e8ebe04b15cf86541f8084535` |
| `candidate_lock.md` | `8a5a460bac51843e532c9894fcb99470247c7de7833449c3660813ccd183d64e` |
| `phase2_domain_amendment.md` | `412e6d24c43ab5a995d135c6ecb207f5225414fac223fcf63080486af6fc3de3` |

Each active file contains exactly one status transition from `RE-LOCK PENDING`
to `RE-LOCK PASS`.  Reversing only that transition reproduces the reviewed
content hashes `e1fe94ef...`, `f890ad69...`, and `0b6572a2...`, respectively;
there is no mathematical, outcome, control, or Route drift.

`phase2_final_gate.md` SHA-256 is
`22fd0376ad8e69e6816b3d005d88f4cde2cc5f4b243749c95aa2f19ab8164a3f`.
Its active tuple and six evidence hashes all match disk.  Its authorization is
correctly limited to the one-orbit Phase-3 program; packet LCH/completion,
packet same-map transport and packet-level `REFUTE` remain withheld, with
`NOT_TESTABLE` preserved absent those bridges.  A3, A4, and Route B remain
closed.  Final mechanical re-lock: **PASS**.
