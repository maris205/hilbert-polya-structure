# Paper 05 Preregistration — Intrinsic Symbolic Grading and Duality

Frozen on 2026-08-13 before computation.  No candidate ID is assigned yet.

## Research target

Starting only from the Paper-04 full-shift tensor/entropy source, determine
whether a canonical graded symbolic transfer object can do more than restate
the Euler product.  The live A3 target is a same-object mechanism for at
least one of:

1. a non-arbitrary determinant orientation;
2. cancellation of mixed symbolic traces;
3. a genuine \(s\leftrightarrow1-s\) duality on a nonempty analytic domain;
4. an internally controlled continuation beyond the Euler half-plane.

The immediate output may be a candidate or a scoped obstruction.  It is not
required to be an RH proof.

## Shared arithmetic source

Let \(F_n\) be the finite full \(n\)-shift and let

\[
 [F_m]\boxtimes[F_n]=[F_{mn}],\qquad
 h(F_n)=\log n.
\]

The tensor atoms are \(F_p\).  This source may be reused because every branch
below is a functorial construction on the same monoidal symbolic skeleton.
No branch may import a clock, sign, parity, Gamma factor, or determinant from
another candidate.

## Three frozen branches

### K — factorization/Koszul grading

- For each \(F_n\), form the open tensor-divisor interval
  \(P_n=(F_1,F_n)\).
- Use its order complex and the standard reduced simplicial chain degree.
- The only allowed parity is chain degree modulo two; a global parity flip is
  reported as a control, not a second candidate.
- Weight the \(F_n\) summand by \(e^{-s h(F_n)}=n^{-s}\).
- Test whether the reduced Euler characteristic recovers \(\mu(n)\), whether
  the differential squares to zero, and whether a trace-class graded
  compression exists.

### S — stable/unstable symbolic duality

- Replace an atom inventory by the internally normalized full \(p\)-shift
  transfer block.
- Normalization must be derived from entropy/Parry normalization.
- Stable and unstable sectors must be related by the canonical time-reversal
  of the two-sided shift; parity cannot be declared after seeing a target.
- Record separately ordinary traces, Lefschetz/supertraces, and any temporal
  primitive-orbit interpretation.

### G — tensor group completion and centered inversion

- Use the Grothendieck group of the tensor monoid, canonically
  \(\bigoplus_p\mathbb Z\), with inversion \(q\mapsto q^{-1}\).
- Center the spectral parameter as \(u=s-\tfrac12\) only if the half-density
  normalization is derived from the same entropy norm.
- The finite atom-cutoff dual ratio is
  \[
  R_P(s)=\prod_{p\leq P}
  \frac{1-p^{-(1-s)}}{1-p^{-s}}.
  \]
- Finite-cutoff symmetry and unit modulus on the critical line are algebraic
  diagnostics only.  They receive no continuation credit.

## Gates

### G0 — definition and source lock

For a branch to remain live it must define its phase/category, grading,
differential or duality map, transfer action, function space, determinant
convention, and analytic domain without prime/zero tables or fitted signs.

### G1 — intrinsic parity

The grading must be invariant under relabeling tensor atoms and functorial
under full-shift tensor isomorphisms.  If a global parity reversal changes the
claimed conclusion and the source has no rule selecting one orientation, the
orientation claim is `MODELING_CHOICE`.

### G2 — exact trace ledger

All finite coefficients and chain identities are computed exactly.  A branch
must distinguish:

- categorical tensor atoms;
- temporal primitive orbits;
- chain-level supertrace;
- homology-level supertrace;
- ordinary or relative Fredholm determinant.

### G3 — analytic-domain gate

Every determinant or superdeterminant must have a nonempty domain on which
the relevant operators are trace class, or a separately proved relative
determinant theorem.  An alternating difference of two divergent traces is
not a supertrace.

### G4 — A3 progress gate

A formal identity earns no A3 advance.  GO requires at least one of:

- a nonempty new controlled domain beyond \(\Re s>1\);
- a canonical relative determinant on an open set intersecting the critical
  strip;
- an internally derived functional-equation factor;
- a same-object finite Weil/Lefschetz compression with a proved trace identity.

If none occurs, the paper records the strongest exact grading theorem and
the obstruction that prevents promotion.

## Forbidden moves

- prime or Riemann-zero tables in any candidate definition;
- choosing parity, signs, or chain shifts to obtain the desired orientation;
- fitting Gamma factors or counterterms to the completed zeta function;
- calling a finite-cutoff phase a limiting determinant;
- subtracting divergent sector traces without a relative trace theorem;
- importing analytic continuation of \(\zeta\) as operator continuation;
- combining branch K's sign, branch S's dynamics, and branch G's duality
  coordinatewise unless a single functorial object is explicitly built;
- Route B.

## Frozen controls

1. global parity reversal;
2. deterministic random atom parity;
3. factor-count parity with multiplicity versus squarefree exterior degree;
4. shifted multiplication with intrinsic full-shift entropy;
5. additive monoid;
6. positive free-mixing grammar;
7. \(s\) and \(1-s\) sectors evaluated separately before any quotient;
8. finite-cutoff symmetry versus genuine infinite-domain convergence.

## GO / STOP / NOT-TESTABLE

- **GO:** one branch passes G0–G4 on the same frozen object.  Only then assign
  `SD-C08`.
- **SCOPED THEOREM STOP:** intrinsic grading is exact but every admissible
  determinant remains confined to the Paper-04 domain, or the dual sectors
  have no common/relative nuclear domain.
- **NOT_TESTABLE:** grading, differential, duality, function space, or
  determinant convention is missing; controls are incomplete; or a
  regularization is chosen after inspecting the target.

Route B remains locked in all three outcomes.
