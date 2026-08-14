# Source Lock — Paper27 / SD-C29

## Immutable research source

The sole mathematical and literature authority for this manuscript is:

~~~text
/tmp/paper27_research_package.md
SHA-256 216415568c467d5640b2cbb7e9d1114a625d2854188845296b250338f754b083
~~~

The package was frozen on 2026-08-14 after its primary-source novelty audit.
The manuscript may improve exposition and prove stated intermediate lemmas,
but it may not expand the theorem class, replace the source family, import a
new repair, or promote any finite computation into an analytic theorem.

## Frozen title and candidate

**Candidate:** SD-C29
**Title:** *Möbius-Compiled Atom Loops in Integer Symbolic Dynamics: Exact
Necklace Selection and Oblique-Projector Collapse*

## Frozen source family

The arithmetic source is the locally finite divisibility poset

\[
P=(\mathbb N_{\ge 1},\mid),
\qquad P_N=\{1,\ldots,N\}.
\]

Paper25's source-fixed Elias-gamma code, affine renewal branches, and
holomorphic de Rham grading are inherited without modification. The only new
object is the incidence fiber derived from this integer grammar.

Allowed inputs are source objects, divisibility, incidence convolution,
\(\zeta\), its inverse \(\mu\), the cover relation, the fixed gamma duration,
and honest ordinary or graded Fredholm determinants on a proved trace-class
domain.

Forbidden inputs include a supplied prime/color list, prime mask, von
Mangoldt or prime-zeta coefficient table, target zeros, fitted spectra,
cross-family repairs, Route B assertions, and removal of the digit-duration
marker.

## Frozen definitions

The atom predicate is source internal:

\[
\operatorname{At}(P)
=\{n>1:(1,n)=\varnothing\}
=\{n>1:((\zeta-\delta)*(\zeta-\delta))(1,n)=0\}.
\]

For all source coordinates,

\[
\varepsilon_n(a,b)=\mathbf 1_{a=b=n},\qquad
q_n=\zeta*\varepsilon_n*\mu,\qquad
q_n(a,b)=\mathbf 1_{a\mid n\mid b}\mu_{\rm arith}(b/n).
\]

The letter action and marked weight are

\[
A_n=\mathbf 1_{\operatorname{At}(P)}(n)q_n,\qquad
a_n(s,u)=u^{\ell(n)}n^{-s},\qquad
\ell(n)=2\lfloor\log_2 n\rfloor+1.
\]

Here \(z\) counts completed returns and \(u\) counts original binary digit
steps. At repetition order \(r\), the marker is \(u^{r\ell(n)}\).

## Frozen theorem boundary

The manuscript proves:

1. \(q_nq_m=\delta_{nm}q_n\) and \(\sum_nq_n=\delta\), intervalwise in the
   countable incidence algebra, with every \(q_n\) primitive.
2. Every nonempty word has trace one exactly when it is a monochromatic
   temporal repetition of a source atom; mixed words and composite source
   letters vanish.
3. Every finite complete primitive lift with the same diagonal labels is
   conjugate to the coordinate family by a unit in \(1+J_N\).
4. On \(H_\eta\), each atom \(q_p\) is rank one and trace class for
   \(\eta>1/2\), with the exact trace norm frozen in the research package.
5. The global zeta/Möbius similarity is bounded for \(\eta>1\).
6. The marked atom transfer is holomorphic and trace class exactly on the
   stated absolute-convergence domain; all power traces and the Fredholm atom
   product follow.
7. Tensoring with the inherited Paper25 de Rham sector gives two honest
   degreewise Fredholm determinants whose graded ratio equals the atom
   product.

The manuscript does **not** claim a new Möbius idempotent theory, a new
representation of \(1/\zeta\) in isolation, continuation across
\(\operatorname{Re}s=1\) at \(u=1\), a critical-line carrier, or an RH
mechanism.

## Mandatory firewalls

- Source label \(p^r\) is not the temporal repetition \(p,p,\ldots,p\).
- Incidence inversion alone creates one oblique coordinate for every integer;
  atom selection is owned by the cover predicate.
- Scalar Möbius or von Mangoldt inversion is not a necklace-resolved
  projector.
- Ordinary determinants are not the even/odd graded ratio.
- Oblique/radical geometry is invisible to ordinary cyclic traces.
- A bounded global similarity is asserted only for \(\eta>1\); individual
  trace-class rank-one projectors exist already for \(\eta>1/2\).
- At \(u=1\), the trace-class barrier \(\operatorname{Re}s>1\) is not analytic
  continuation.
- The digit marker \(u^{r\ell(p)}\) must remain visible.
- Mutated-poset selection is a PROVES_TOO_MUCH control, not evidence of an
  independent notion of rational primality.

## Frozen route record

~~~text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
GO_SOURCE_DERIVED_ATOM_ORBITS
STOP_INCIDENCE_SIMILARITY_COLLAPSE
STOP_CRITICAL_STRIP_CONTINUATION
~~~

The positive A1 upgrade and the overall rejection must be reported together.

## Paper28 minimum obligation

Paper28 may inspect only the remaining trace-invisible datum: the mixed Gram
geometry of \(q_p^*q_q\) in a canonical adjoint/chiral completion. It must
compare diagonal and mutated-poset controls, retain the gamma marker, prove a
common Schatten domain, and reject any fitted or reference-dependent
regularization. Failure to obtain a source-specific invariant triggers
STOP_ADJOINT_GRAM_COLLAPSE and STOP_INCIDENCE_ROUTE.

## Ownership and review policy

The authority writer owns only top-level manuscript documentation,
sections/, figures/, main.tex, math_commands.tex, references.bib, main.pdf,
and COMPILATION_REPORT.md. Code, generated results, experiments, evaluations,
manifest files, the root README, and Git are excluded. All manuscript review
loops are skipped by standing instruction.
