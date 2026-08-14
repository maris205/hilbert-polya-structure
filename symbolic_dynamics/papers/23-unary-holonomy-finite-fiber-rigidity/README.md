# Paper 23 — Unary Holonomy Finite-Fiber Rigidity

**Candidate:** SD-C25  
**Primary family:** Symbolic Dynamics only  
**Title:** *Finite-Fiber Rigidity of the Ordered Cofactor Spine: Unary
Periodicity, Recurrence Supports, and Compiler Collapse*  
**Status:** exact same-object no-go theorem and Route-A branch closure  
**Target-zero data:** none  
**Route B:** locked  
**Compiled artifact:** [main.pdf](main.pdf), 21 A4 pages, SHA-256
38cc9ee9bbd76fedee168caa969d076510ed22416d0c00ac8132a23c3247a765

## One-paragraph result

Paper22 classifies the holonomy-two primitive cycles of the
successor–divisor shift as

\[
 C_k=(k,k+1,\ldots,2k-1),\qquad k\ge2.
\]

Marking the unique minimum exposes the source-derived quotient word

\[
 W(C_k)=1^{k-1}2.
\]

Every fixed finite group, semigroup, DFA, or NFA reads this unary family
eventually periodically, so it cannot accept an infinite prime-only set of
lengths.  Every fixed characteristic-zero finite-dimensional response

\[
 u^{\mathsf T}A^{k-1}Bv
 \quad\text{or}\quad
 \operatorname{tr}(A^{k-1}B)
\]

is a linear recurrence sequence.  Skolem–Mahler–Lech makes its exact nonzero
support ultimately periodic, again excluding infinite prime-only support.
Growing nilpotent fibers can memorize every finite prefix, including a prime
indicator, but they fit arbitrary bit strings equally well and are therefore
a PROVES_TOO_MUCH control.  The two licensed countable total-decider
wrappers return to the Paper19 transient-pruning or Paper20 clock-dilution
alternatives.  Finally, even a separately assumed one-dimensional oracle
deletion control leaves the same canonical factor

\[
 z^p
 \left(\frac{(2p-1)!}{(p-1)!}\right)^{-2s},
\]

not \(zp^{-s}\).  The ordered cofactor spine is therefore closed as a
Route-A branch.

## Main theorem chain

1. **Canonical word.**  The exact cofactor word is \(1^{k-1}2\), with no
   prime predicate in the source.
2. **Finite-fiber rigidity.**  Powers in a fixed finite semigroup are
   eventually periodic; finite automata and finite group characters inherit
   that periodicity.
3. **Linear-recurrence rigidity.**  Cayley–Hamilton gives a fixed recurrence
   for every bilinear or trace response, and Skolem–Mahler–Lech controls its
   exact support.
4. **Finite-fit control.**  An \(N\)-dimensional nilpotent shift memorizes
   any \(N\)-term response.  Finite prime fits have no selectivity evidence.
5. **Countable-wrapper boundary.**  In the licensed Paper19/Paper20
   architectures, transient computation is invisible to traces; recurrent
   long computation under total roof \(\log n\) is noncompact; inducing
   changes \(z^{\ell(n)}\) to \(z\).
6. **Factorial-roof persistence.**  A genuine block fiber has local factor
   \(\det_{\mathbb C^d}(I-w_kBA^{k-1})\), not
   \(1-w_k\operatorname{tr}(BA^{k-1})\).  Its trace-log terms, and a
   separately assumed scalar deletion control, retain graph length and the
   endpoint roof \(2\log((2k-1)!/(k-1)!)\).

For the complete block factor, every exterior-power coefficient
\(\operatorname{tr}((\wedge^jB)(\wedge^jA)^{k-1})\) is an LRS.  Thus the
set of nontrivial block factors is ultimately periodic; this is the
full-factor statement, not an inference from the first trace term alone.

## Closest literature collision

The broad statement “Skolem–Mahler–Lech forbids prime period support in
Symbolic Dynamics” is not novel.  De Jong's 2026 work applies
Skolem–Mahler–Lech to rational logarithmic derivatives of Artin–Mazur zeta
functions and classifies period sets, while also classifying least-period
sets for finitely presented systems.  Paper23 claims only the model-specific
closure chain on the ordered successor–divisor cofactor family.
The present countable Markov shift is not asserted to satisfy de Jong's
compact/finitely-presented or rational-logarithmic-derivative hypotheses;
the citation bounds novelty and is not an application theorem for SD-C25.

The source ledger also locks Chrobak's 1986 unary-automata paper together
with its 2003 erratum and To's 2009 correction, Schützenberger's
multiplicity-automata paper, Hartmanis–Shank on prime recognition,
Lech/Bell for Skolem–Mahler–Lech, and current unary weighted-automata
context.

## Exact audit status

The exact experiment protocol was frozen before execution.  It covers:

- source/no-oracle and word certificates;
- exhaustive small finite-state periodicity;
- exact Cayley–Hamilton residuals;
- bilinear and trace nilpotent memorizers on matched target families;
- finite block traces and determinants;
- inherited trace-class diagnostics;
- transient and recurrent countable-wrapper controls;
- exact factorial-roof and marker mismatch;
- deterministic double-run and SHA-256 integrity.

The integrated suite passed 32/32 tests.  It certified 4,095 canonical
cycles and 8,390,655 edges; exhausted 1,054,474 finite-state
terminal/acceptance configurations with 8,067,400 periodicity comparisons;
and reproduced the two-dimensional firewall
\(\operatorname{tr}(P)=0\), \(\operatorname{tr}(P^2)=2\),
\(\det(I-wP)=1-w^2\).  Thirty-one generated artifacts were byte-identical
across two runs, with combined SHA-256
`25d1dc42431693a0b380741531238b5b52bbbb62f5c9602afe13845a67ebd336`;
the integrity audit passed.  Finite computation remains an implementation
audit, not proof.

## Strict route decision

\[
(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
 \mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_FAIL},
 \mathrm{A4\_FAIL}).
\]

Overall:

\[
        \mathrm{ROUTE\_A\_REJECTED}.
\]

Machine-readable tuple:

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_WEAK,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

Route B is locked.

## Claim boundary

This project does not prove that every finite-dimensional nonlinear
observable, every sign/cutpoint language of a recurrence, or every
countable symbolic extension fails to recognize primes.  Its exact
finite-dimensional theorem concerns zero/nonzero and fixed-level supports
of the displayed linear responses.  Its countable theorem concerns the two
licensed total-decider wrappers already analyzed in Papers19–20.

The project does not claim an identity with \(1/\zeta(s)\), analytic
continuation, a functional equation, a critical-line mechanism, RH, or a
Hilbert–Pólya operator.

## Shareable paper

The shareable artifact is [main.pdf](main.pdf).  Modular sources are
[main.tex](main.tex), [math_commands.tex](math_commands.tex),
[sections/](sections/), [figures/](figures/), and
[references.bib](references.bib).  Source, proof, derivation, literature,
narrative, preregistration, figure, and compilation contracts are recorded
in the top-level Markdown files.

## Paper24 obligation

No successor may test another finite character, DFA, or fixed matrix fiber
on \(1^{k-1}2\).  A viable next object must be a source-derived recurrent
grammar with \(O(\log n)\) symbolic length, intrinsic total roof \(\log n\),
prime/composite separation in primitive-orbit algebra rather than at a
terminal selector, and a compact or trace-class whole operator.  If such a
grammar cannot be defined without target-dependent computation, this branch
should stop.
