# Paper 22 — Cofactor Holonomy Fredholm Trilemma

**Candidate:** SD-C24  
**Primary family:** Symbolic Dynamics only  
**Title:** *Cofactor Holonomy on the Successor–Divisor Shift: Exact Class
Resolution and a Fredholm Trilemma*  
**Status:** positive same-object class-resolution theorem plus a sharp scoped
Route-A rejection  
**Target-zero data:** none  
**Route B:** locked

## One-paragraph result

On the successor–divisor graph

\[
 n\longrightarrow d
 \quad\Longleftrightarrow\quad
 d\ge2,\qquad d\mid n+1,
\]

the exposed factor witness

\[
 q(n,d)=\frac{n+1}{d}
\]

is a source-intrinsic multiplicative cocycle.  Every closed path has positive
integer holonomy

\[
 Q(\gamma)=\prod q(n_j,n_{j+1})
           =\prod_j\left(1+\frac1{n_j}\right)\ge2,
\]

so the neutral group-trace sector contains no recurrence.  The first
non-neutral class is exactly solvable:

\[
 Q(\gamma)=2
 \quad\Longleftrightarrow\quad
 \gamma=C_k=(k,k+1,\ldots,2k-1),\quad k\ge2,
\]

up to rotation.  Hence the connected holonomy-two Fredholm coefficient is

\[
 \mathcal H_2(s,z)
 =\sum_{k\ge2}z^k
   \left(\frac{(2k-1)!}{(k-1)!}\right)^{-2s}.
\]

For the two-parameter adjacency

\[
 L_{s,u}e_n
 =\sum_{d\mid n+1,\ d\ge2}
   (nd)^{-s}q(n,d)^{-u}e_d,
\]

the analytic domain is sharp:

\[
 L_{s,u}\in\mathcal S_1
 \quad\Longleftrightarrow\quad
 \Re s>\frac12
 \quad\text{and}\quad
 \Re(s+u)>\frac12.
\]

This yields a trilemma.  The pure cofactor roof keeps the desired
\(Q^{-u}\) label weight but is noncompact whenever bounded; endpoint
regularization produces an honest Fredholm determinant but factorially damps
the canonical spine; unitary characters change phases only and retain every
\(C_k\).  The construction is mathematically exact but does not reproduce the
Riemann prime Euler ledger.

## Strongest advances

1. **Intrinsic cocycle:** the cofactor comes from the same successor–tensor
   factorization that defines the graph.
2. **Exact class resolution:** Haar extraction on the character family gives
   every multiplicative holonomy coefficient of the connected trace ledger.
3. **Closed first-class formula:** \(Q=2\) is exactly one primitive orbit at
   every length \(k\ge2\), with no repetition contamination.
4. **Sharp analytic phase diagram:** two independent boundary mechanisms
   give the exact \(\mathcal S_1\) domain.
5. **Scoped no-go:** every function of the abelian product \(Q\) is constant
   on all \(C_k\), and arbitrary positive inventories preserve this support.

## Fredholm trilemma

| Choice | Analytic outcome | Arithmetic outcome |
|---|---|---|
| pure cofactor roof \(s=0\) | never trace class; noncompact whenever bounded | \(Q^{-u}\), but infinitely many canonical representatives |
| endpoint regularization | honest Fredholm determinant in the sharp two-half-plane domain | factorial weights indexed by \(k\) |
| unitary character twist | same \(\Re s>1/2\) threshold as the base operator | phases only; all \(C_k\) survive |

The ordinary regular group lift is not compact because the infinite deck
coordinate supplies infinite multiplicity.  In the separate semifinite
algebra \((B(\ell^2(V))\bar\otimes L(\Gamma),\Phi)\), it is \(L^1\) exactly
for \(\Re s>1/2\); its neutral \(\Phi\)-determinant is locally equal to one
because no periodic path has identity holonomy.  This is trace blindness,
not target success.

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

Stop labels:

- STOP_NEUTRAL_SECTOR;
- STOP_PRIME_ORBIT_LEDGER;
- CYCLE_FLOOD;
- GAUGE_REDUCIBLE_TO_SOURCE_POTENTIAL;
- PROVES_TOO_MUCH;
- ROUTE_B_LOCKED.

## Claim boundary

This project proves the cocycle, holonomy classifications, connected
coefficient formulas, sharp trace-class domain, regular-lift distinction,
trilemma, and inventory controls.  It does not prove an identity with
\(1/\zeta(s)\), analytic continuation to the critical line, a functional
equation, an explicit formula, RH, or a Hilbert–Pólya operator.

## Shareable paper

The shareable artifact is [main.pdf](main.pdf).  Its modular sources are
[main.tex](main.tex), [math_commands.tex](math_commands.tex),
[sections/](sections/), [figures/](figures/), and
[references.bib](references.bib).  The source, proof, derivation, literature,
and build contracts are recorded in the top-level Markdown packages; the
final mechanical audit is [COMPILATION_REPORT.md](COMPILATION_REPORT.md).

## Next smallest symbolic obligation

Any successor must leave the abelian product-holonomy branch.  The minimum
new object is the ordered free word

\[
 W(C_k)=1^{k-1}2,
\]

with the numerical label \(1\) deliberately retained as a letter.  A later
project would first have to prove the finite-fiber eventual-periodicity
barrier and then justify any infinite-memory extension without compiling a
primality decider into the grammar.  No such successor is started here.
