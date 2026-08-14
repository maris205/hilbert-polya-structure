# LITERATURE AUDIT — SD-C21

**Audit date:** 2026-08-14
**Primary family:** Symbolic Dynamics
**Technical-source policy:** primary papers, publisher records, author-hosted
papers, and official repositories
**Cross-family policy:** clues only in `ROUND2_CLUES.md`

## 1. Search object

The audit targeted the closest collisions to a full-shift-semiring
trial-division countable Markov graph:

- product/sum operations on symbolic systems and finite dynamics;
- direct-prime full shifts and prime-indexed subshifts;
- automata or counter machines recognizing primes;
- Turing computations represented as dynamical systems;
- countable Markov, renewal, coded, and formal-language zeta functions;
- trace-class determinants of infinite weighted graphs;
- graph-prime and trace-monoid Euler products;
- invariance of periodic-orbit zeta data under transient pruning.

Search strings included combinations of `full shift semiring product sum`,
`prime language automaton`, `Turing machine symbolic dynamics`, `renewal
shift zeta arbitrary function`, `countable Markov Fredholm determinant`,
`trace monoid prime walks zeta`, and `transient graph zeta`.  DOI and
bibliographic fields were checked against publisher or official repository
records.  The search cannot establish absence of every equivalent
presentation.

## 2. Source ledger

| source | primary result used | boundary for SD-C21 |
|---|---|---|
| Bowen--Lanford (1970), [DOI](https://doi.org/10.1090/pspum/014/9985) | finite shift zeta/determinant framework | trace-to-determinant conversion is classical |
| Lind (1984), [DOI](https://doi.org/10.1017/S0143385700002443) | entropy realization for topological Markov shifts | full-shift entropy and prime-cardinality examples are not new |
| Kopra (2023), [DOI](https://doi.org/10.1017/etds.2022.33) | direct-prime subshifts and canonical covers | direct primeness under product is an established symbolic notion |
| Salo--Törmä (2015), [DOI](https://doi.org/10.1016/j.tcs.2014.10.023) | categories of subshifts and block maps | alphabet-sum must not be mislabeled a categorical coproduct |
| Hartmanis--Shank (1968), [DOI](https://doi.org/10.1145/321466.321470) | recognition complexity of prime representations | prime recognition by machines is classical; the novelty cannot be “an automaton tests primes” |
| Shepherdson--Sturgis (1963), [DOI](https://doi.org/10.1145/321160.321170) | register/counter-style computability of recursive functions | successor/multiplication programs inherit classical universality risks |
| Kůrka (1997), [DOI](https://doi.org/10.1016/S0304-3975(96)00025-4) | Turing machines treated as topological dynamical systems | embedding computation into dynamics is established machinery |
| Gurevich--Savchenko (1998), [DOI](https://doi.org/10.1070/RM1998v053n02ABEH000017) | thermodynamic formalism for countable symbolic Markov chains | infinite-state zeta questions require explicit recurrence/summability hypotheses |
| Sarig (1999), [DOI](https://doi.org/10.1017/S0143385799146820) | thermodynamic formalism for countable Markov shifts | SD-C21 deliberately claims only a weighted vertex adjacency on (\ell^2), not a Ruelle theorem |
| Sarig (2004), [official repository](https://repository.kulib.kyoto-u.ac.jp/dspace/handle/2433/249526) | one renewal shift with two-coordinate weights can realize arbitrary local zeta germs | flexible countable grammars can encode targets and therefore demand a `PROVES_TOO_MUCH` control |
| Simon (1977), [DOI](https://doi.org/10.1016/0001-8708(77)90057-3) | infinite Fredholm determinants for trace-class operators | the determinant needs a genuine (\mathcal S_1) proof |
| Deitmar (2015), [DOI](https://doi.org/10.1137/140957925) | Fredholm determinant formulas for infinite weighted graphs of finite total weight | infinite weighted graph determinants are established; the model-specific content is the semiring verifier and pruning theorem |
| Berstel--Reutenauer (1990), [DOI](https://doi.org/10.1090/S0002-9947-1990-0998123-X) | zeta functions of formal languages | language-to-zeta encodings are classical and can be highly expressive |
| Giscard--Rochet (2017), [DOI](https://doi.org/10.1137/15M1054535) | prime hikes and number-theoretic identities on trace monoids | “prime” graph walks are not automatically rational primes |
| Naquin--Gadouleau (2024), [DOI](https://doi.org/10.1016/j.tcs.2024.114509) | factorization in the semiring of finite dynamical systems | semiring language for dynamical objects has close precedents, though the present full-shift skeleton and sieve graph differ |

## 3. Closest collisions

### 3.1 Prime support already built into symbolic objects

Lind's entropy setting and Kopra's direct-prime subshifts make clear that
prime-cardinality full shifts and product indecomposability are established
objects.  SD-C21 therefore does not claim discovery of primes inside full
shifts.  Its narrower positive contribution is an explicit local quotient
search and one trace-class whole-graph determinant.

### 3.2 Machine computation as dynamics

Hartmanis--Shank analyze recognition of primes, register-machine work gives
general recursive computation, and Kůrka treats Turing machines as dynamical
systems.  These sources collide with any broad novelty claim that “dynamics
computes primality.”  The defensible statement is more specific: the
instructions are expressed by the two full-shift semiring operations and the
quotient witness is exposed state by state.

### 3.3 Flexible countable zeta encodings

The renewal-shift example is the strongest conceptual collision.  A fixed
countable Markov shift with suitable local weights can realize arbitrary
holomorphic germs near zero.  SD-C21 differs in using positive entropy roofs,
a deterministic source program, and an exact Euler orbit ledger, but Sarig's
example reinforces rather than weakens the compiler no-go: expressive
countable grammars need a selectivity test.

### 3.4 Infinite weighted graph determinants

Simon supplies the operator-theoretic determinant and Deitmar treats
infinite weighted graph zetas under finite-total-weight hypotheses.  The
(\mathcal S_1) proof and Euler conversion are therefore applications of
classical technology.  The source-specific theorem is that the expanded
semiring verifier meets those hypotheses on (\operatorname{Re}s>1).

### 3.5 Language and trace-monoid primes

Formal-language zetas and trace-monoid hikes show that primitive words and
graph-prime factorizations support Euler-like identities in broad settings.
They do not identify rational primes without an arithmetic selector.  This
is precisely the distinction formalized by the universal-decider theorem.

## 4. Defensible novelty

The literature search did not locate the exact conjunction of:

1. the finite-full-shift positive-integer semiring skeleton;
2. an explicitly unrolled (Q_{n,d,q}) quotient search with no factor guard;
3. an entropy-weighted whole adjacency that is trace class on
   (\operatorname{Re}s>1);
4. the exact two-variable Fredholm product
   (\prod_p(1-zp^{-s})) on that same operator;
5. a theorem proving that all verifier computation prunes from periodic data;
6. the universal total-decider and factorial-monoid compiler controls.

This conjunction is the defensible model-specific contribution.  Items
(1)--(4) are a constructive result; items (5)--(6) supply the more important
negative interpretation.

## 5. Dangerous formulations and replacements

| dangerous formulation | required replacement |
|---|---|
| “the categorical coproduct of full shifts” | “alphabet-sum, or alphabet coproduct followed by the full-shift functor” |
| “a Ruelle operator” | “weighted vertex-adjacency on (\ell^2(V(G)))” |
| “primes emerge dynamically” | “the source program accepts primes before their loops are entered” |
| “the construction is circular” | “algorithmically non-oracular but dynamically selector-tautological” |
| “the verifier causes the determinant” | “the same operator contains the verifier, but pruning proves determinant invisibility” |
| “all exact verifiers are diagonal” | scoped positive formal-ledger pruning theorem only |
| “the zeta function is continued by the graph” | equality only on (\operatorname{Re}s>1) |
| “graph primes are rational primes” | graph primitives require a separate arithmetic selectivity theorem |

## 6. Novelty verdict

**Construction novelty:** medium and defensible in the exact frozen
combination.
**Analytic machinery novelty:** low.
**Obstruction novelty:** medium-to-high as a scoped theorem tied to the same
object.
**RH consequence:** none.
**Overclaim risk:** high if transient pruning or the universal compiler is
omitted.

The paper should be presented as an exact construction-and-no-go result in
Symbolic Dynamics, not as an RH proof and not as a general theory of
computational dynamical systems.
