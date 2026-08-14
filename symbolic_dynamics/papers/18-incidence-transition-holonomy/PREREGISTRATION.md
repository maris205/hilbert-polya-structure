# PREREGISTRATION — SD-C20

**Freeze date:** 2026-08-14
**Project:** `18-incidence-transition-holonomy`
**Primary system family:** Symbolic Dynamics
**Forbidden data:** Riemann-zero tables, zero-derived fitting, prime-indexed
fiber labels, and post-hoc arithmetic phases

## Research question

Can a relabeling-natural transition cocycle generated only by the incidence
of two tensor subsets escape the cyclic one-letter obstruction, produce a
genuine noncommutative Artin factor on the same symbolic extension, and remain
free of mixed holonomy leakage?  If not, does the failure distinguish primes
from matched nonprime inventories?

## Frozen object

For finite \(P\), use the full shift on
\(\mathcal E_P=2^P\setminus\{\varnothing\}\), with scalar arrival weight

\[
w(T)=(-1)^{|T|+1}x_T,\qquad x_T=\prod_{p\in T}x_p.
\]

For a finite-group cocycle
\(\alpha_P:\mathcal E_P\times\mathcal E_P\to G\) and irreducible
representation \(\rho\), freeze

\[
B_{\rho,P}(S,T)=w(T)\rho(\alpha_P(S,T)),
\qquad D_{\rho,P}=\det(I-B_{\rho,P}).
\]

The main candidate takes \(G=S_3\), \(r=(12)\), \(t=(23)\), and

\[
\alpha(S,T)=r\mathbf1_{S\subsetneq T}
+t\mathbf1_{T\subsetneq S}
\]

in piecewise group notation: \(r\) for strict refinement, \(t\) for strict
coarsening, and \(e\) otherwise.

## Frozen claims

### C1 — natural incidence classification

Under relabeling naturality, restriction compatibility, fixed target group,
and one-step incidence locality,

\[
\alpha_P(S,T)=g_{|S\setminus T|,|S\cap T|,|T\setminus S|}.
\]

The number of stable types on \(n\) atoms is

\[
N(n)=\binom{n+3}{3}-(2n+1),
\]

giving (1,5,13,26) for \(n=1,2,3,4\).

### C2 — exact natural counting gauge class

Natural gauges are \(b_P(S)=q_{|S|}\).  The natural gauge orbit of
\(\alpha_a(S,T)=a^{|T|}\) is

\[
g_{u,v,w}=q_{u+v}^{-1}a^{v+w}q_{v+w},
\]

and every irreducible block factors atomwise:

\[
D_{\rho,P}=\prod_{p\in P}\det(I-x_p\rho(a)).
\]

### C3 — genuine noncommutative transition holonomy

The frozen \(S_3\) refinement/coarsening cocycle is not gauge equivalent to
any one-letter reference.  The primitive four-cycle
\([p,pq,q,pq]\) has commutator holonomy
\((rt)^2=[r,t]\ne e\).

### C4 — exact abelian-clean/nonabelian-leaking blocks

On two atoms,

\[
D_{\mathbf1}=D_{\mathrm{sgn}}=(1-x)(1-y),
\]

but

\[
D_{\mathrm{std}}
=(1-x)^2(1-y)^2
+3xy(x+y)(xy+1)(x+y-1).
\]

The first unmarked trace-log differences are

\[
[x^2y]=-3,\quad [xy^2]=-3,\quad [x^2y^2]=-6.
\]

The edge-separated commutator cycle has character gap (3).

### C5 — cycle-separated leakage

If a cycle-separated primitive word has holonomy not conjugate to its
reference holonomy, some irreducible character coefficient differs.  This is
a marked-cycle theorem.  It is not a claim that unmarked determinants
classify cocycles.

### C6 — exact finite evidence, scoped

Exhaustive two-atom enumeration gives:

- \(S_3\): (7{,}776) tables, (972) sign-clean, (36) all-irrep-clean,
  all (36) in the count/gauge class;
- \(D_4\): (32{,}768) tables, (64) all-irrep-clean, all (64) in the
  count/gauge class;
- \(Q_8\): (32{,}768) tables, (512) one-dimensional-clean, (64)
  all-irrep-clean, all (64) in the count/gauge class.

The zero nongauge-clean count is finite evidence only.

### C7 — Fredholm half-plane

The symmetric realization on
\(\ell^2(\mathcal E_\infty)\otimes V_\rho\) is trace class for
\(\operatorname{Re}s>2\).  The trivial rank-one block is trace class for
\(\operatorname{Re}s>1\).  No stronger half-plane or continuation is
preregistered.

### C8 — exact nonselectivity

Every algebraic identity depends only on incidence and formal atom variables.
Prime, shuffled-prime, composite, random-integer, random-rational, and free-
commutative inventories therefore reproduce the mechanism with zero symbolic
margin.  This triggers

```text
STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH
```

## Primitive and repetition freeze

Closed words are identified by rotation only.  Reflection is not an orbit
equivalence.  A primitive word \(\gamma\) has scalar weight \(w(\gamma)\)
and ordered holonomy \(H(\gamma)\); its \(m\)-fold traversal uses
\(w(\gamma)^m\) and \(H(\gamma)^m\).  Edge-separated coefficients are kept
distinct from coefficients aggregated only by atom multidegree.

## Finite evidence protocol

- exact group tables and exact irreducible matrices;
- modular evaluation only as a rejection screen;
- every survivor certified symbolically over the integer polynomial ring;
- no floating equality;
- no general theorem inferred from \(S_3,D_4,Q_8\);
- squarefree atom multidegree at most four and temporal power at most four
  for the frozen low-degree audit;
- commuting edge markers used only when the connected cyclic traversal is
  unique, otherwise a phase-lift or cyclic-word marker is required.

## Controls

1. identity cocycle;
2. one-letter degree cocycle;
3. exact gauge-generated incidence tables;
4. random natural incidence tables;
5. one-dimensional/abelianization-only audit;
6. forbidden prime-indexed labels as a negative naturality control;
7. prime, shuffled, composite-only, matched random, rational, and formal atom
   inventories.

Random-control seeds, if the finite audit is rerun, are

```text
18001, 18002, 18003, 18004, 18005
```

## Refutation and stop rules

- A natural cocycle not determined by \((u,v,w)\) under the stated
  assumptions refutes C1.
- A natural gauge depending on more than \(|S|\) refutes the gauge part of C2.
- A gauge solving the frozen \(S_3\) candidate against a one-letter reference
  refutes C3.
- Any failure of the exact determinant formula refutes C4.
- A cycle-separated nonidentity holonomy invisible to every irreducible
  character refutes C5.
- Any nongauge-clean survivor refutes the finite rigidity observation but not
  C1--C5.
- Trace-class failure in \(\operatorname{Re}s>2\) refutes C7.
- A symbolic separation between prime and matched formal inventories refutes
  C8 and reopens Route A.

## Frozen anti-claims

- No claim that finite-group Artin factors, voltage graphs, gain graphs, or
  Livšic cohomology are new.
- No universal theorem that all clean transition cocycles are
  count+coboundary.
- No claim that character determinants determine the gauge class.
- No claim that all nonabelian holonomy leaks in an unmarked determinant.
- No continuation, Gamma factor, functional equation, zero-counting law,
  Weil compression, self-adjoint operator, or RH conclusion.

## Frozen verdict

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

GO_GENUINE_TRANSITION_HOLONOMY
GO_SAME_OBJECT_ARTIN_BLOCKS
GO_TRIVIAL_EULER_FACTOR
GO_TRACE_CLASS_RE_GT_2
STOP_NONABELIAN_CLEAN_FACTOR
STOP_DETERMINANT_IMPLIES_COHOMOLOGY
STOP_ONE_DIMENSIONAL_CHARACTER_AUDIT
STOP_ROBUST_NO_LEAK
STOP_ARITHMETIC_SELECTIVITY
PROVES_TOO_MUCH
ROUTE_A_REJECTED
ROUTE_B_LOCKED
```
