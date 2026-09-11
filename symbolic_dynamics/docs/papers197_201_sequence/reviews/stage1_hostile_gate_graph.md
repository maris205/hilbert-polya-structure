# Second Stage-1 hostile gate — GBE, SDD, TCSD, and SCT

**Gate date:** 2026-09-05 UTC  
**Reviewer:** process-separated from the four scouts  
**Scope:** internal theorem/value/collision gate only  
**External status:** `OWNER_AMBER / HOLD_EXTERNAL`  
**Novelty or priority conclusion:** none

## Outcome first

Only TCSD clears this gate as a paper candidate.  SDD is mathematically
sound within its deliberately narrow contract, but that contract does not
solve the dynamics on its advertised full carrier.  GBE is standard Bellman
closure with a generic inverse inclusion--exclusion attached.  SCT is a real
nonmonotone map, not a conjugate of P188, but it reuses P188's exact carrier,
feedback statistic, and endogenous prefix while supplying a substantially
less complete temporal atlas.

| rank | candidate | correctness result | decisive subtraction | verdict |
|---:|---|---|---|---|
| 1 | ternary cyclic sign derivative (`TCSD`) | the frozen core, clock, trace, recurrence, and fibre claims survived the independent attacks below | generic CA/SFT, de Bruijn traces, comparison words, and the exact P164 equality shadow are zero credit; the oriented ternary core/clock/Lucas-fibre conjunction remains | **`SELECT / OWNER_AMBER / HOLD_EXTERNAL`** |
| 2 | self-displacement difference (`SDD`) | Theorems A--C are correct on their stated scopes | the affine atlas is an ordinary power-map cocycle on only `p^2` of `p^p` states; P178 owns the adjacent all-function/state-selected-difference surface; the full carrier has only its fixed locus classified | **`RESERVE_BOUNDED_CONTRACT / OWNER_AMBER / HOLD_EXTERNAL`** |
| 3 | self-cardinality toggle (`SCT`) | the image, one-step fibre, indegree distribution, and two-cycle census are correct | exact P188 carrier/statistic/prefix reuse; no sharp all-`n` tail, recurrent-locus classification, or complete period theorem replaces what is subtracted | **`KILL_CURRENT_CONTRACT_P188_COLLISION`** |
| 4 | graph Bellman envelope (`GBE`) | the displayed iterate, fixed locus, sharp height, and inclusion--exclusion are correct for nonempty finite graphs | the entire forward theorem is the standard min-plus Bellman/distance closure; P90 removes min-plus propagation as a residual, and the inverse is generic witness inclusion--exclusion | **`KILL_STANDARD_BELLMAN_CLOSURE`** |

`SELECT` here means eligible for a proof/manuscript stage, not externally
cleared.  `RESERVE` does not allocate a paper number.  The two `KILL`
decisions apply to the submitted contracts; the revival conditions below are
intentionally stronger than adding more finite data.

## Frozen audit surface

The gate read the following candidate inputs without changing them:

```text
b4e093c44b41a7a8a09c00d202c2bc9d45bc3f05f177d54958e65546552cedd4  scouting/root_graph_bellman/THEOREM_SPIKE.md
b11cb1f13d84ac3bf9892449ebb3e238382643dab4e160781f6521aca074fd83  scouting/root_graph_bellman/verify_scout.py
09e36343f7fe8e1f4887c775f971f93397006793261eaef5470c328f63e80278  scouting/algebra_lane/SDD_THEOREM_CONTRACT.md
cc258a92b1ddac56eb15ec1869993d265a7e98d239132fbac328c6a8521b8a14  scouting/algebra_lane/COLLISION_MEMO.md
904628b6c2e52af1f88460e4f1879a2b8610b5499c0c9e4c11569437b4af85ad  scouting/word_poset_lane/TCSD_THEOREM_CONTRACT.md
f63c0cc9a5f69321f6f63666aef7374d61125ee8df9ec8bb833fe048c948395e  scouting/word_poset_lane/TCSD_LOCAL_CERTIFICATE.md
3cdafac7c0e18aaab4d69fdc40dc04196ac4dd75bfc4fa71a5cbdbe68171c04f  scouting/word_poset_lane/COLLISION_FIREWALL.md
736fe6a1df12bee26f47d846a47e78319f7b41fdcfd37ad15415c21ca8ec0ff0  scouting/root_self_cardinality_toggle/THEOREM_SPIKE.md
71d4d7072961fc0b1675f332d766514b76baac1c231cbbc41580ece64ff0a594  scouting/root_self_cardinality_toggle/verify_scout.py
```

The nearest live definitions checked directly were P90, P164, P178, P187,
P188, and P196.  Hashes above are workspace-root-relative after the common
prefix `docs/papers197_201_sequence/`; they are audit identifiers, not a
release manifest.

## 1. TCSD — select, with a narrower collision statement

### Cold temporal derivation

Let

```text
D(x)_i = sgn(x_(i+1)-x_i),   x_i in {-1,0,1}.
```

A zero run of length `q` in `D(x)` needs an equal-letter run of length
`q+1` in `x`.  A run of equal nonzero signs in `D(x)` is a strict monotone
chain in a three-element alphabet and consequently has length at most two.
For a nonconstant cyclic word this independently gives

```text
R(Dx) <= max(R(x)-1,2).
```

The finite identities in the local certificate then have exactly the
required index orientation:

```text
delta^5(w_0...w_5)_0 = delta(w_2w_3)_0                 when R=1,
delta^6(w_0...w_6)_0 = delta^2(w_2w_3w_4)_0            when R<=2.
```

Applied around the cycle, the second identity is
`D^6(x)=rho^2 D^2(x)`.  Thus after run contraction every state enters

```text
K_n={x:D^4x=rho^2x}.
```

On `K_n`, `rho^(-2)D^3` is a two-sided inverse to `D`: commutation with
`rho` gives both compositions.  Hence `K_n` is recurrent, while eventual
entry prevents recurrence outside it.  This also proves the pointwise clock
as the first time the local equality holds; it is not merely a stopping rule
inserted into the definition.

For the one-exception word, direct differentiation gives

```text
a^(n-1)b -> 0^(n-2) s (-s)
0^r Alt_l(s) -> 0^(r-1) Alt_(l+1)(s).
```

The last zero disappears when `n` is even and one zero remains when `n` is
odd.  This yields the stated sharp heights `n-1` and `n-2`.  A manuscript
proof must explicitly show that the displayed intermediate words are not in
`K_n`; saying only that they “reach” the exhibited recurrent word does not
by itself prove first-entry sharpness.  This check is elementary from the
same local identity, and the exhaustive boxes support it, but it must be on
the proof page.  The separate `n=1,2,3` conventions must remain visible.

### Depth, periods, and inverse axis

The matrices `A_t` correctly encode the local condition

```text
D^(t+4)x = rho^2 D^t x
```

by length-`t+5` windows, so `tr(A_t^n)` counts depth at most `t`, including
small cycles whose windows repeat coordinates.  An independent exact
construction of `A_0` produced 165 allowed length-five blocks and

```text
det(zI-A_0)
 = z^74 (z-1)(z^3-z^2-2z-1)(z^3+z^2+2z+1),
```

which rederives the displayed order-seven recurrence.  Likewise `C_p`
does exactly count `D^p x=x`, and Möbius inversion gives least periods.
These are correct exact enumerators, but they are de Bruijn/trace machinery,
not a closed classification of which divisors of the period bound occur.

For a labelled target `y`, a predecessor is precisely a closed walk on the
three ordered levels whose successive relation is `<`, `=`, or `>` according
to `y_i`.  This proves

```text
|D^(-1)(y)| = tr(M_(y_0)...M_(y_(n-1))).
```

Removing equality letters leaves the strict-sign skeleton.  Nilpotence of
three consecutive strict rises or falls gives the stated image criterion.
For alternating strict signs,

```text
tr((M_+ M_-)^m)=tr([[2,1],[1,1]]^m)=L_(2m).
```

The strict-skeleton normal form then gives the global maximum and its exact
equality cases.  The small ties are essential: at `n=2`, `00` and the two
alternating targets tie; at `n=3`, `000` and the six one-zero alternating
targets tie.  This labelled maximum/equality theorem is a materially
stronger inverse result than merely printing a generic transfer trace.

### Collision subtraction

The TCSD firewall needs one wording correction at manuscript stage.  On
P164's `q=3` slice there is an exact first-front factor:

```text
P164_(q=3),equal(x)_i = 1{x_i=x_(i+1)} = 1{D(x)_i=0}.
```

Therefore TCSD must not say without qualification that no factor exists.
What does **not** exist in the audited material is a dynamical semiconjugacy
that recovers TCSD's theorem package from this zero/nonzero projection.
P164 discards the sign, then follows an affine binary Rule-102 tail; TCSD
retains both orientations, stays ternary and nonlinear, and has a
fourth-root-of-shift recurrent core with linear parity-sensitive attraction.

P187 owns positive cyclic difference, frozen-peak/run arguments, and local
relation traces; P196 owns an adjacent operation on finite-chain cyclic
words, a constrained recurrent language, and transfer/cycle/fibre methods;
P90 owns generic cyclic-CA and min-plus temporal language.  All of those
surfaces receive zero credit.  After that subtraction, the surviving
internal conjunction is:

1. the literal oriented three-valued sign derivative;
2. the finite local certificate yielding `D^4=rho^2` exactly on the
   recurrent core;
3. the parity-sharp global clock; and
4. the labelled relation-walk fibre theorem with its Lucas maximum and all
   equality cases.

No one item alone clears the gate.  Their conjunction does.

### Mandatory TCSD claim boundary

Any promoted contract must satisfy all of the following.

- Keep `OWNER_AMBER / HOLD_EXTERNAL`; no internal non-hit is novelty,
  priority, or freedom-to-operate evidence.
- Assign zero contribution credit to cellular-automaton, SFT, de Bruijn
  trace, transfer-matrix, comparison-word, and Möbius-inversion machinery.
- State the exact P164 zero-symbol projection above.  Claim only failure of
  theorem-preserving semiconjugacy, not absence of every factor relation.
- Call (3.2)--(3.3) exact finite matrix enumerators, not fixed-size closed
  forms or efficient formulae: the matrix size grows with `t`.
- Call (4.3) a complete matrix census, not a simple classification of the
  period set; the bound in (4.1) does not assert that every divisor occurs.
- Call (5.2) a one-step every-target fibre theorem.  No all-time
  every-target fibre atlas is presently proved.
- Print the no-early-entry step for the sharp witnesses and all `n=1,2,3`
  fibre/tail exceptions.
- Retain the full local certificate in a human-auditable form; finite carrier
  exhaustion cannot replace the all-size radius-six identity.

Subject to these boundaries, the verdict is **SELECT**.

## 2. SDD — correct partial theorem, reserve only

### Cold algebraic derivation

For `f_(a,b)(x)=ax+b`, direct substitution into

```text
(D_pf)(x)=f(x+f(x))-f(x)
```

gives `(a,b)->(a^2,ab)`, and induction gives
`(a^(2^t),b a^(2^t-1))`.  This proves the affine tail/period law, the
iterate-fixed formula, and every-time affine fibre sizes exactly as stated.
The clause `A=0,B=0` has `p` sources because all `(0,b)` collapse there;
when `A!=0`, each `2^t`-power root determines `b` uniquely.

For the full-carrier fixed equation,

```text
f(x+f(x))=2f(x),
```

the graph of `f` is invariant under the bijection
`L(x,c)=(x+c,2c)`.  Nonzero `L`-orbits project to labelled sets
`b+a<2>`; selecting a union that is still a function graph is exactly a
matching of the labelled projected-orbit hypergraph.  Uncovered arguments
receive their zero singleton.  This proves Theorem C.  It also explains why
coincident projected sets must retain their orbit labels and cannot both be
selected.

The primitive-root corollary is valid only when `2` generates
`F_p^*`.  The `p=7` value 22, rather than 8, is the necessary visible
counterexample to an unconditional `p+1` formula.

### Why it is not selected

The scope separation in the frozen document is honest, but it is decisive:

- the full temporal and all-time inverse atlas applies only to the affine
  stratum of size `p^2` inside a carrier of size `p^p`;
- on the full carrier, only fixed points are classified;
- the verified nonfixed recurrent populations and tails at `p=5,7` are
  explicitly pilot data and have no all-parameter theorem.

Thus the two advertised axes do not jointly resolve the same phase space.
The affine first coordinate is ordinary squaring, whose 2-primary tail and
root counts receive zero credit.  P178 also uses the identical all-function
carrier and a state-selected finite difference
`f(x+f(0))-f(x)`; its literal map is different, but it makes carrier and
finite-difference rhetoric owner-sensitive.

The result is worth retaining as a bounded proof spike, but not allocating as
a “complete dynamics” paper.  Promotion would require either a genuine
full-carrier temporal theorem beyond fixed points, or a deliberately
retitled fixed-point/affine-slice note that passes a separate portfolio value
gate.

### Mandatory SDD claim boundary

- Quantify Theorems A and B with `D_p|A_p` every time; never abbreviate their
  fixed counts, tails, periods, or fibres as full-carrier results.
- Do not claim a full-carrier tail bound, recurrent classification,
  all-target fibre law, image formula, or cycle census from the `p<=7`
  pilots.
- Keep `p` odd in the theorem: invertibility of the factor `2` is used by
  `L`.  A computed `p=2` control is not part of the contract.
- Treat the hypergraph as a labelled multi-hypergraph and define matching by
  disjoint projected vertex sets.
- State `|Fix(D_p)|=p+1` only under the primitive-root hypothesis; retain the
  `p=7` counterexample.
- Give ordinary finite-field power maps and their root/period calculus zero
  contribution credit, and name P178's exact neighboring literal.
- Keep all full-box numbers labelled finite counterexample pressure.

The verdict is **RESERVE**, with no paper number at this gate.

## 3. SCT — correct one-step theory, killed against P188

Let `P_k=[k]`.  If `|A|=k`, then

```text
F(A)=A triangle P_k,
|F(A)|=2(k-|A intersect P_k|),
```

so the image lies in the even layer.  Conversely, for a target `B` of size
`2r`, the only possible source of cardinality `k` is
`A=B triangle P_k`, and it has cardinality `k` exactly when
`|B intersect P_k|=r`.  If
`B={b_1<...<b_(2r)}`, the admissible values are
`b_r<=k<b_(r+1)`, proving fibre `b_(r+1)-b_r`; the empty target has the
`n+1` prefix sources.  This also proves the parity image and the stated
indegree distribution.

For an even nonzero state of size `k`, a return in two steps is equivalent to
`|A intersect [k]|=k/2`, which gives the displayed binomial two-cycle-state
census.  Coordinate 1 changes at every step of a nontrivial cycle, so odd
periods are excluded.  Zero extension and pair doubling genuinely embed
functional graphs and supply the stated period-existence results.

These facts do **not** remove the P188 collision:

| feature | P188 | SCT |
|---|---|---|
| carrier | all `A subseteq [n]` | identical |
| feedback statistic | `k=|A|` | identical |
| endogenous object | prefix `[k]` | identical |
| Boolean operation | `A intersect [k]` | `A triangle [k]` |
| inverse sufficient data | target size/order statistics and admissible source `k` | the same reconstruction shell |
| temporal strength | pointwise all-time rank recursion, endpoint/basins, unique sharp state, all-time fibres | complete one-step atlas and two-cycle census, but no full recurrent locus, period set, or sharp all-`n` tail |

Symmetric difference creates genuinely different nonmonotone behavior, so
this is not a literal equality or relabelling conjugacy.  Nevertheless, once
the common carrier/cardinality/prefix and rank-reconstruction inverse engine
are subtracted, the remaining theorem is incomplete exactly where it needs
to be strongest: the long cycles are witnessed but not classified, and even
the observed maximum-tail sequence is not frozen as an all-parameter
theorem.  More exhaustive period examples would not repair this deficit.

### Mandatory SCT claim boundary

If the map is retained in a kill ledger or later reopened:

- describe the fibre law as one-step only;
- distinguish the number of states on two-cycles from the number of
  two-cycles (divide the former by two);
- do not claim that all periods are powers of two, that the displayed powers
  exhaust the period set, or that the pilot maximum tails have a proved
  formula;
- do not call the functional graph or recurrent locus classified;
- give the P188 carrier/statistic/prefix and rank-reconstruction shell zero
  contribution credit;
- keep period embeddings as existence lower bounds only.

A legitimate revival needs a complete all-`n` recurrent/period theorem plus
a sharp tail classification, or an equally strong all-time inverse theory
that is not another P188 rank-chain calculation.  The present verdict is
**KILL**.

## 4. GBE — correct Bellman closure, no surviving paper residual

Put `A_(v,v)=0`, `A_(v,u)=1` on edges, and infinity elsewhere in the
min-plus semiring.  Then GBE is simply

```text
T(x)=A tensor x.
```

Min-plus matrix powers give

```text
T^t(x)_v=min_(d(v,u)<=t)(x_u+d(v,u)).
```

After component diameter many steps this is the ordinary metric minorant
envelope.  Its fixed points are exactly the integer 1-Lipschitz functions.
The first time a vertex attains its final value is the distance to its
nearest minimizing source, and the sharp global tail is

```text
min(maximum component diameter, max(0,h-1)).
```

For a target `y`, the lower bounds

```text
ell_u=max(0,max_(d(v,u)<=t)(y_v-d(v,u)))
```

force every candidate source above every target cone.  Requiring each target
coordinate to have at least one attaining source and applying
inclusion--exclusion over the failed-attainment events gives exactly the
displayed all-time fibre formula.  The formula is therefore correct.

It is also the reason for the kill.  The forward dynamics is standard
synchronous Bellman--Ford/min-plus distance closure, not merely analogous to
it.  Fixed-function enumeration as homomorphisms to a reflexive path is
standard transfer counting.  The inverse sum is the generic
inclusion--exclusion for witnesses attaining a family of minima; it does not
expose a graph-specific second statistic, factorization, or nontransferable
fibre engine.

P90 is not a literal collision: it evolves binary traffic configurations and
has conserved density and translating recurrent phases.  It does, however,
already consume a closed min-plus propagation formula and sharp entry clock,
so “min-plus finite dynamics” cannot be used to separate GBE from the
classical Bellman closure.  P90's different carrier does not restore a
residual after the standard algorithm itself is subtracted.

### Mandatory GBE claim boundary

- Treat the Bellman recurrence, shortest-path iterate, metric envelope,
  1-Lipschitz fixed locus, and path/cycle transfer counts as standard and
  zero credit.
- Describe the target formula as a generic exact inclusion--exclusion, not a
  compact or efficient inverse classification.
- Require `V` nonempty, or explicitly define the maximum component diameter
  and empty products for the empty graph; the frozen verifier begins at one
  vertex.
- Do not use the P90 comparison as evidence of novelty: it is only an
  internal method subtraction.
- Do not claim a nontrivial recurrent spectrum; every orbit is absorbed at a
  fixed metric envelope.

The verdict is **KILL**.  A revival would require a new graph-dependent
inverse factorization or enumerative theorem that is not implied by generic
min-plus inequalities; restating the inclusion--exclusion in matrix notation
is not enough.

## Verification record and final gate

The author/scout programs were run read-only as counterexample pressure:

| candidate | replay result |
|---|---|
| GBE | `232,448` assertions; all labelled simple graphs through four vertices and heights through three; PASS |
| SCT | `1,650,635` assertions; all subsets through `n=18`; PASS |
| SDD lane | `198,297` assertions; frozen canonical transcript byte-match; PASS |
| TCSD lane | two fresh processes, `3,238,990` assertions each; outputs byte-identical with SHA-256 `2b47662aaeab35569a9720896846537c58e040a4b82b9197c4a8b698e7479132`; PASS |

Enumeration supports implementation correctness but proves none of the
unbounded statements.  The independent exact `A_0` characteristic-polynomial
calculation and the cold derivations above provide separate pressure on the
main formulas.

Final Stage-1 disposition:

```text
TCSD = SELECT / OWNER_AMBER / HOLD_EXTERNAL
SDD  = RESERVE_BOUNDED_CONTRACT / OWNER_AMBER / HOLD_EXTERNAL
SCT  = KILL_CURRENT_CONTRACT_P188_COLLISION
GBE  = KILL_STANDARD_BELLMAN_CLOSURE
```

No verdict in this file is an external novelty, ownership, or release claim.
