# PAPER PLAN — SD-C21

## Title

*A Semiring Sieve Shift: Exact Euler Determinant, Recurrent-Core Collapse,
and a Factorial-Monoid Compiler No-Go*

## Central thesis

Finite full shifts contain a literal positive-integer semiring skeleton, and
an expanded countable Markov verifier can use that skeleton to compute
primality without a factor oracle and to realize (1/\zeta(s)) as the
Fredholm determinant of one trace-class adjacency.  The same theorem also
shows why this does not advance the recurrent arithmetic program: the
computation prunes away, and an arbitrary total decider compiles its support
into the same determinant form.

## Claim--evidence matrix

| ID | claim | status | decisive support |
|---|---|---|---|
| C1 | alphabet product/sum recover multiplication/addition | structural identity | alphabet cardinalities and entropy |
| C2 | explicit (Q_{n,d,q}) graph decides primality | theorem | terminating quotient successor search |
| C3 | whole adjacency is (\mathcal S_1)-holomorphic for (\Re s>1) | theorem | rank-one edge majorant |
| C4 | primitive loops and repetitions are exact | theorem | complete cycle census |
| C5 | (D_{\rm SV}(s,z)=\prod_p(1-zp^{-s})) | theorem | trace-class determinant expansion |
| C6 | verifier computation is determinant-invisible | theorem | transient block has zero power traces |
| C7 | positive exact ledgers prune to simple cycles | scoped theorem | SCC connector argument |
| C8 | every total decidable support is compilable | theorem | time-damped configuration chains |
| C9 | factorial monoids reproduce the mechanism | theorem/control | atom verifier plus summable norm |
| C10 | finite implementation matches C2--C9 | exact evidence | 13/13 tests, no-oracle certificate, and rational matrix audits |
| C11 | candidate advances strict Route A | refuted | A3/A4 failures and `PROVES_TOO_MUCH` |

## Section architecture

1. **Introduction.** State the exact construction and its no-go together.
2. **Classical boundary.** Locate full-shift entropy, countable Markov zeta,
   automata computation, renewal flexibility, and Fredholm machinery.
3. **Full-shift semiring.** Freeze (\boxtimes), alphabet-sum (\boxplus),
   order, successor, entropy, and categorical language.
4. **Expanded sieve graph.** Define (I,T,Q,A,R) and prove local primality
   correctness without an existential edge.
5. **Weighted adjacency.** Define the one-sided CMS, vertex Hilbert space,
   roofs, (L_s), and the complete trace-class majorant.
6. **Euler determinant.** Prove the cycle ledger, power traces, and the
   two-variable Fredholm--Euler identity.
7. **Recurrent-core collapse.** Give block pruning, the positive exact-ledger
   theorem, deterministic-verifier corollary, and graph-length caveat.
8. **Universal compilers.** Prove the total-decider and factorial-monoid
   theorems; give the (\mathbb F_q[t]) control.
9. **Finite certificate.** Report exact support, SCC, trace, determinant,
   relabeling, bounded-depth, shifted, polynomial, and arbitrary-support
   audits behind an evidence firewall.
10. **Route evaluation.** Apply the exact tuple and anti-claims.
11. **Conclusion.** State the no-accept-loop obligation for Paper 20.
12. **Appendices.** Collect expanded estimates/proofs and the claim ledger.

## Figure plan

One native TikZ figure has three layers:

```text
full-shift semiring skeleton
        |
I_n -> T_{n,d} -> Q_{n,d,q}
        | accept          | equality
     A_p loop          cemetery ray
        \                 /
     whole S1 weighted adjacency
              |
     traces/determinant retain only A_p
       /                         \
exact 1/zeta               universal decider
       \                         /
 selector-tautological / pruning-equivalent
```

Blue denotes frozen structure, green an exact analytic pass, amber an
invisibility boundary, and red a Route-A stop.  Text duplicates color.

## Citation plan

- Bowen--Lanford for classical shift determinants;
- Lind and Kopra for entropy/direct-prime symbolic context;
- Salo--Törmä for categorical discipline;
- Hartmanis--Shank and Shepherdson--Sturgis for primality languages and
  counter/register computation;
- Kůrka for Turing computation viewed dynamically;
- Gurevich--Savchenko and Sarig for countable Markov/renewal zeta boundaries;
- Simon and Deitmar for trace-class/Fredholm and infinite weighted graphs;
- Berstel--Reutenauer and Giscard--Rochet for language/trace-monoid zetas;
- Naquin--Gadouleau for semirings of finite dynamical systems.

## Writing controls

- Use “alphabet-sum,” never categorical coproduct.
- Use “weighted vertex-adjacency,” never Ruelle operator.
- Define (Q_{n,d,q}) before any divisibility macro.
- State the one-sided phase space explicitly.
- Separate canonical accept roofs from transient modeling choices.
- Keep graph-step (z^\ell) markers under cycle contraction.
- Call the construction “algorithmically non-oracular but dynamically
  selector-tautological.”
- Do not describe pruning as topological conjugacy.
- Keep cross-family speculation only in `ROUND2_CLUES.md`.

## Venue and length

This is an internal research authority manuscript with no external venue
page limit.  Target length is 14--18 A4 pages including appendices.  No
review round is run by instruction; the final quality gate is four clean
LaTeX passes plus citation, font, page, link, and intermediate-file audits.
