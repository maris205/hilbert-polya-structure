# Paper Plan — P119

Status: frozen internal author draft; external novelty, priority, specialist
clearance, and circulation **HOLD**.

## One-sentence contribution

For the fixed regular element `J=I+N` in `U_n(F_q)`, refine Bier's owned
lower-central image theorem by counting every finite-field fibre, then derive
all iterated fibre, depth, and filtration-typed predecessor counts, with
centralizer–coset and triangular-superdiagonal counting routes.

## Contract-to-section map

| Contract | Main-text anchor | Proof mechanism |
|---|---|---|
| Literal system and filtration | Section 2 | Matrix-ideal filtration `n_r n_s subset n_(r+s)` |
| Owned image plus fibre `q^(n-k)` | Theorem 3.1 | Bier supplies the image equality; left centralizer cosets give the finite-field count |
| Second substantive counting route | Proposition 4.1 | Solve `XJ=JXY` by a difference equation with one free field coordinate per superdiagonal |
| All restricted iterated fibres | Theorem 5.1(i) | Compose the uniform one-step surjections |
| CDF, exact layers, sharp height and deepest shell | Theorem 5.1(ii–iii) | Root-fibre counts and consecutive differences |
| Full and filtration-stratified indegrees | Corollary 6.1 | One-step fibres and subtraction of nested source levels |
| Unique recurrence and zeta | Corollary 6.1 | Strict filtration descent and zero-credit finite-map bookkeeping |
| Regularity firewall | Proposition 7.1 | Direct centralizer calculation for `J'=I+E12+E34` in `U_4` |
| Exact computation | Section 8 and `code/` | Literal finite fields and matrices; canonical deterministic stdout |

## Narrative order

1. State the exact finite-dynamical question before giving group-theory
   background.
2. Subtract Bier's literal fixed-`J` image theorem, Lang-map terminology,
   Engel sinks, lower-central descent, regular centralizers, and zeta
   conversion before presenting the residual.
3. Define the fixed regular map and all small-parameter conventions.
4. Count every one-step fibre by left centralizer cosets.
5. Recount it by triangular superdiagonal solving; do not reclaim existence.
6. Multiply the one-step fibres to expose every temporal layer and local
   predecessor type.
7. Put the near-regular counterexample before the conclusion so the claim
   ceiling cannot be missed.

## Proof-route firewall

- **Route I — group action/cosets:** Write `E(X)=X^(-1)phi(X)`, identify
  equal fibres with left cosets of `Fix(phi)`, and calculate the regular
  Toeplitz centralizer.
- **Route II — triangular coordinates:** Expand `E(X)=Y` as
  `AN-NA=B+NB+AB+NAB`; on source diagonal `r`, solve one discrete-difference
  equation with one free constant. Products use only earlier source
  diagonals.

The routes are independent counts of the finite-field fibre size.  Bier
already owns existence and the image equality.  Later iterated-fibre and
layer formulas intentionally share the count and are not represented as
separately rederived.

## Claim ceiling

- Fixed `J=I+N`, one regular upper shift, only.
- No claim for arbitrary unipotent `J`, another Engel word, conjugacy-class
  dynamics, or a general Lang map; the displayed `U_4` case disproves only a
  universal extension.
- Bier's restricted/iterated image theorem, the Lang fibre idea, left Engel
  sequence, regular centralizer, lower-central filtration, unique nilpotent
  sink, and Artin–Mazur conversion receive zero contribution credit.
- A bounded no-hit is not a novelty or priority certificate.

## Boundary checklist

- `n=1`: singleton system, handled separately.
- `n=2`: one root plus `q-1` depth-one vertices.
- `t=0`: identity iterate, empty exponent sum, singleton fibres.
- `t=n-k`: image `gamma_n={I}` and fibre all of `gamma_k`.
- `t>n-k`: the same constant image persists.
- Target outside `gamma_(k+t)`: fibre zero.
- Characteristic two and nonprime finite fields: included in literal controls.
- The `U_4` near-regular counterexample is checked over four fields.
