# Claims–evidence map — P109

Status: **cross-hostile A/B mathematical closure / final mechanical QA PASS /
internal freeze / external HOLD**.

`q` is a prime power, `d>=1`, `V=F_q^d`, and `N` is regular nilpotent.
Invalid Gaussian binomials are interpreted as zero.

| claim | theorem/proof evidence | independent evidence |
|---|---|---|
| exact iterates | Proposition 2.1: images respect composition, hence `T^t(U)=N^t(U)` | every literal subspace satisfies `image(image(U,t),1)=image(U,t+1)` in the verifier |
| rank loss | rank–nullity for `N^t|_U`, with kernel `U intersect ker N^t` | every enumerated `(t,U)` image dimension is computed from its materialized vector set |
| uniform fibre | Theorem 3.1: choose `R=U intersect ker N^t`, then parameterize lifts as graphs `W -> ker N^t/R` | verifier groups literal preimages by the exact target subspace `W` and input rank `r` |
| joint rank transition | Corollary 3.2 multiplies a uniform fibre by the number `[d-t choose s]_q` of targets in `im N^t` | all `(t,r,s)` cells are compared to the closed formula |
| second proof route | Proposition 6.1 slices by a hyperplane containing a fixed kernel and solves the recurrence with Gaussian Pascal | RREF enumeration is coordinate-level and does not call the quotient-fibre proof |
| iterated indegree | Corollary 3.3 sums the fibre formula over `r`; at one step the two terms are `q^s` and `1` | every target in the literal first image is checked for indegree `q^s+1` |
| absorption CDF | `T^t(U)=0` iff `U <= ker N^t`, whose dimension is `min(t,d)` | exact orbit depths are computed for all subspaces in every lane |
| exact depth layers | successive differences of the CDF give `G_t-G_{t-1}` | stored profiles include every layer, not samples |
| unique periodic point | if `T^n(U)=U`, then `N^(mn)U=U`; choosing `mn>=d` forces `U=0` | periods `1,...,d+1` are checked for every enumerated subspace |
| zeta | every positive-period fixed count is one, so the Artin–Mazur exponential is `(1-z)^(-1)` | periodic-point checks certify the finite lanes |
| sharp maximum depth | `ker N^(d-1)` is proper; a cyclic top vector has depth `d` | every tested profile has nonempty last layer and no deeper point |
| rigidity | conjugacy preserves the unique fixed point and all absorption layers; max depth gives `d`, and `B_2=q+3` gives `q` for `d>=2` | pairwise signature comparison permits only identical `(q,d)` or the stated `d=1` collision |

## Quantifier and endpoint ledger

- The fibre and transition formulas are stated for `0<=t<=d`; outside this
  range the map is already zero and the absorption theorem uses `min(t,d)`.
- At `t=0`, the fibre formula reduces to the identity map.
- At `t=d`, the only target is zero and the formula counts all `r`-subspaces.
- At `r<s` or `r-s>t`, the invalid Gaussian coefficient makes the count zero.
- At `d=1`, the system does **not** recover `q`; all such systems are
  explicitly classified as conjugate.
- The control covers prime powers `2,3,4,5,8,9,16`; the proof covers every
  prime power.

## Ownership subtraction

The paper cites and subtracts:

- Goldman–Rota and Prasad for Gaussian finite-subspace enumeration;
- Brickman–Fillmore and Fripertinger for invariant-subspace lattices and
  finite-field enumeration;
- Bender–Coley–Robbins–Rumsey for dimension-sequence enumeration and its
  regular-nilpotent product formula, and Ram for the 2026 general
  finite-field subspace-profile solution; and
- Artin–Mazur for the zeta definition.

The profile owners count global dimension-sequence data, whereas the residual
statement here is limited to pointed fibres `N^t U=W`, the resulting
functional graph, absorption, and rigidity.  A bounded search is not a
novelty certificate, so public release stays **HOLD**.

Internally, P73 acts on symbolic substitution patterns, P99 permutes
fixed-index integer sublattices by an invertible shear, and P103 acts on full
matrix space by double adjugation.  The present map instead absorbs the full
finite-field subspace lattice by a noninvertible image operation; these are
update-rule-level separations, not merely parameter changes.
