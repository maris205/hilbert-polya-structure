# Owner-first search log — algebraic scout

**Search date:** 2026-09-02 UTC.  
**External status:** `HOLD_EXTERNAL`.  
**Purpose:** find reasons to kill candidates before drafting.  This is a
bounded search log, not a systematic-review claim and not novelty clearance.

## Search protocol

The search started from literal update formulas, then expanded to polynomial
aliases and the nearest established source families.  Search-result snippets
were treated only as discovery aids.  Scope statements below were checked
against arXiv primary records/full text, publisher records, or the local
frozen papers themselves.  No unpublished manuscript or local result was sent
to an external model or person.

### QTS literal and alias queries

The following query strings were executed through the web search interface:

```text
"Tr(x)^2" "finite field" rational map
"trace" "x^{-1}" finite field map permutation polynomial
site:arxiv.org finite fields trace reciprocal map
finite field rational function trace quotient quadratic extension
"x+2x^q+x^{2q-1}" finite field
"x + 2x^q + x^{2q-1}" permutation polynomial
"x^{2q-1}" "2x^q" finite field
"(x+x^q)^2/x" finite field
"x^{2q-1}+2x^q+x" finite field
"Tr(x)^2/x" finite fields
"trace-square" reciprocal finite field
"x(1+x^{q-1})^2" finite field
"x(1+x^(q-1))^2" finite field
"X(1+X^{q-1})^2" permutation polynomial
"(1+x^{q-1})^2" "F_{q^2}"
"functional graph" "x^{2q-1}" finite field
dynamics "a x+b x^q+x^{2q-1}"
iteration "x+2x^q+x^{2q-1}" finite field
cycle structure "x(1+x^{q-1})^2"
functional graph polynomial "x h(x^{q-1})" finite fields
"functional graph" "x^r h(x^{q-1})"
site:arxiv.org functional graph x h x q-1 finite field quadratic extension
```

The initial trace/reciprocal and expanded-exponent queries did not display the
literal package.  Rewriting the same function as

```text
x(1+x^(q-1))^2=x+2x^q+x^(2q-1)
```

then produced a **direct polynomial-family owner hit**.  Consequently QTS is
not a literal non-hit.  Only the complete iterative functional-graph
conjunction remained absent from the bounded results.  Equivalent graph
formulations, unindexed papers, books, non-English sources, or material
outside snippets/full text can still defeat that residual non-hit.

## Verified adjacent primary sources

### Hou, direct trinomial-family owner

- Xiang-dong Hou, *Determination of a Type of Permutation Trinomials over
  Finite Fields*, arXiv:1309.3530 (2013), Acta Arithmetica 166 (2014), DOI
  `10.4064/aa166-3-3`.
- Primary record: <https://arxiv.org/abs/1309.3530>.
- Xiang-dong Hou, *Determination of a Type of Permutation Trinomials over
  Finite Fields, II*, arXiv:1404.1822 (2014), Finite Fields and Their
  Applications 35 (2015), DOI `10.1016/j.ffa.2015.03.002`.
- Primary record: <https://arxiv.org/abs/1404.1822>.
- Checked scope: the first work determines the permutation members of
  `a x+b x^q+x^(2q-1)` for `a,b in F_q`; the second completes the coefficient
  range `a,b in F_{q^2}`.  The second paper explicitly rewrites the family as
  `x h(x^(q-1))` and states a complete permutation classification.
- Direct implication for QTS: its polynomial form is the member `(a,b)=(1,2)`.
  The construction, family reduction, and whole-field nonpermutation status
  are therefore zero credit.  The retrieved source treats the equation
  `f(x)=y` for permutation classification; it does not display QTS's complete
  nonpermutation functional graph, trace-kernel star, norm-order cycle census,
  or fixed-iterate/zeta package.
- Verdict after the hit: `SELECT_INTERNAL_OWNER_THIN_PENDING`.  Only that
  residual graph conjunction may be evaluated, and a direct graph owner kills
  it.

### Chen--Mesnager, permutation rational functions

- Ruikai Chen and Sihem Mesnager, *Permutation Rational Functions over
  Quadratic Extensions of Finite Fields*, arXiv:2309.04121v2 (2024), linked
  journal DOI `10.1016/j.ffa.2024.102365`.
- Primary record: <https://arxiv.org/abs/2309.04121>.
- Checked scope: rational functions on `F_{q^2}`, `q`-quadratic numerators,
  exact zero counts, and criteria for inducing permutations.
- Owner subtraction: general quadratic-extension rational-function and
  permutation-testing techniques receive zero credit.  Searches within the
  retrieved text for `2q-1` and `Tr(x)^2` returned no match, but this does not
  prove absence from every equivalent formulation.

### Zheng--Zhang--Ding--Zha--Wang, trace diagrams for many-to-one maps

- Yanbin Zheng, Meiying Zhang, Yanjin Ding, Zhengbang Zha, and Qiang Wang,
  *Large class of many-to-one mappings over quadratic extension of finite
  fields*, arXiv:2503.06640v1 (2025).
- Primary record: <https://arxiv.org/abs/2503.06640>.
- Checked scope: many-to-one polynomials of the form
  `h(ax^q+bx+c)+ux^q+vx`, commutative diagrams built from trace maps, inverse
  formulae for the permutation cases, and involutions derived from two-to-one
  maps.
- Owner subtraction: trace-based fibre diagrams and general many-to-one
  language receive zero credit.  The retrieved source did not display QTS's
  literal exponent `2q-1` or its functional-graph package.

These two additional papers establish a **high and active owner-risk
neighbourhood** beyond Hou's direct family ownership.  QTS is not
owner-cleared.  A later source owning the functional-graph conjunction kills
it even if all formulae are correct.

### Oliveira--Brochero Martínez, general functional-graph framework

- José Alves Oliveira and Fabio Enrique Brochero Martínez, *Dynamics of
  polynomial maps over finite fields*, arXiv:2201.00954, Designs, Codes and
  Cryptography 92 (2024), DOI `10.1007/s10623-023-01332-3`.
- Primary record: <https://arxiv.org/abs/2201.00954>.
- Discovery boundary: the primary record advertises functional graphs for
  maps `x^n h(x^((Q-1)/m))` under stated regularity hypotheses.  Over
  `Q=q^2`, QTS is syntactically in that ambient form with `n=1`, `m=q+1`, and
  `h(X)=(1+X)^2`.  However, `h(-1)=0` is exactly the trace-zero collapse, and
  this Stage-1 pass did **not** verify whether the paper's regularity
  hypotheses admit that singular cyclotomic value or whether its conclusions
  specialize to the full QTS graph conjunction.
- Consequence: this is a mandatory focused-audit source, not evidence of a
  non-hit and not yet a direct-owner kill.  Until its hypotheses and theorem
  output are compared line by line, QTS remains
  `SELECT_INTERNAL_OWNER_THIN_PENDING` and `HOLD_EXTERNAL`.

## PDG direct owner and compression

The literal PDG update is

```text
f -> gcd(f,f')
```

on monic polynomials of degree at most `N` in characteristic greater than
`N`.  Searches used:

```text
square-free factorization repeated gcd f f' multiplicities original paper
Yun algorithm square-free decomposition gcd derivative paper PDF
Musser square-free polynomial decomposition finite fields original
site:doi.org square-free factorization polynomial gcd derivative Yun
10.1145/800205.806320 Yun On square-free decomposition algorithms
```

The search found a direct primary owner:

- David Y. Y. Yun, *On square-free decomposition algorithms*, SYMSAC '76,
  pp. 26--35, DOI `10.1145/800205.806320`, published 10 August 1976.
- Publisher record: <https://doi.org/10.1145/800205.806320>.
- Independent author-affiliation record:
  <https://research.ibm.com/publications/on-square-free-decomposition-algorithms>.

The publisher abstract explicitly places the work in square-free
decomposition and revamped Horowitz/Musser algorithms.  Standard
square-free-decomposition proofs identify `gcd(f,f')` with the polynomial
whose irreducible multiplicities are all reduced by one under the scout's
characteristic bound.  That identity is the entire forward clock engine of
PDG.  Its bounded-carrier temporal polynomial and inverse generating function
are mathematically correct residual bookkeeping, but they do not rescue an
independent system claim.  Verdict: `RESERVE_OWNER_COMPRESSED`; it must not be
used merely to fill a five-paper quota.

## Internal owner/collision checks

The local frozen artifacts were read directly:

- `papers/102-cyclic-group-algebra-involution-norm-dynamics/README.md` and
  `CLAIMS_EVIDENCE.md`;
- `papers/125-quadratic-state-shear/README.md` and `CLAIMS_EVIDENCE.md`;
- `papers/150-zero-totalized-lyness-finite-fields/README.md` and
  `CLAIMS_EVIDENCE.md`;
- `docs/papers147_151_sequence/phase1/HISTORICAL_OCCUPANCY.md` and
  `SYSTEM_COLLISION_FIREWALL.md`.

The literal/proof comparison is frozen in `QTS_FREEZE_CONTRACT.md`.  The most
dangerous superficial collision is P150: both carriers have `q^2` points and
both display a `q/1/0` fibre law.  The decisive difference is that QTS is the
global polynomial `x+2x^q+x^(2q-1)` and is bijective off one linear
trace-kernel, whereas P150's zero-totalized denominator creates three
exceptional layers and a depth-three in-tree around a Lyness two-cycle.

The breadth controls were killed mainly by direct internal reductions:

| handles | direct boundary |
|---|---|
| `TQI`, `NTF` | same trace-normalization root as QTS, with only an involutive image and no independent temporal axis |
| `MBI`, `QRM` | literal Möbius/projective iterations; generic finite-group orbit machinery owns the result |
| `DDE` | prime-exponent tent/doubling mechanism collides with P142 |
| `RDF` | simultaneous prime-multiplicity decrement; direct factorization bookkeeping and theorem-thin |
| `EGD` | support peeling along a prime-divisibility/Pratt DAG collides with P133 |
| `FPD` | fixed-point deletion is idempotent after one standardization |
| `DSP` | state-dependent symmetric-group powering hits the permanent generic group-power exclusion |
| `MCH` | Cayley--Hamilton collapses immediately to a scalar power map; P103/P102 neighbourhood |
| `CRH` | code-hull intersection is an idempotent lattice closure |
| `DUA` | a rank-one Artin--Schreier linear image with an involutive core; P109/P115 neighbourhood |

## Bounded-search conclusion

- `QTS`: a direct owner of its full polynomial family was found.  Polynomial
  construction, `x h(x^(q-1))` reduction, and permutation classification are
  fully subtracted.  Only the complete nonpermutation functional-graph
  conjunction survives for a citation-chained audit.  Status
  `SELECT_INTERNAL_OWNER_THIN_PENDING`.
- `PDG`: direct algorithmic ownership found.  Status
  `RESERVE_OWNER_COMPRESSED`, never a quota filler.
- all other controls: killed before paper drafting.

Nothing in this log authorizes novelty language, public posting, specialist
contact, submission, or release.  External status remains `HOLD_EXTERNAL`.
