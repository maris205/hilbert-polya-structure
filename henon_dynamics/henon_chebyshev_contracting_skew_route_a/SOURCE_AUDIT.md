# Source audit — HCS-C126

## Frozen source

The sole mathematical source is the explicitly declared skew product

\[
F(x,y)=\bigl(T_3(x),\tfrac14y+x\bigr)
      =\bigl(4x^3-3x,\tfrac14y+x\bigr)
\]

on \(\mathbb R^2\).  One application of \(F\) is one clock unit.  The
normalization is the unweighted count of isolated fixed points, and the zeta
convention is

\[
\zeta_F(z)=\exp\!\left(\sum_{n\ge1}\#\operatorname{Fix}(F^n)\frac{z^n}{n}\right).
\]

No parameter was fitted.  The theorem has no orbit cutoff; period twelve is
only the finite evidence-replay horizon.  All calculations use exact integer,
rational, trigonometric, or symbolic identities.

## Allowed and forbidden inputs

Allowed:

- the displayed polynomial map;
- the standard polynomial identity \(T_a\circ T_b=T_{ab}\), reproved through
  the cosine definition in the theorem package;
- elementary Möbius inversion and exact differentiation.

Forbidden and unused:

- prime or Riemann-zero tables;
- target-spectrum fitting or post-hoc scaling;
- arithmetic local factors, Euler factors, root numbers, or automorphy data;
- an imported transfer operator, quantum operator, or target divisor.

The literal scope firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Evidence classification

The all-period iterate, root, fiber-lift, primitive-count, Artin–Mazur zeta,
stability, orientation, and repetition statements are `PROVED`.  The period
1–12 JSON rows are deterministic theorem illustrations, not the basis for the
all-period inference.  The two controls are also exact theorems.

No external literature review, novelty search, peer review, reviewer score, or
venue assessment was performed.  Consequently no such conclusion is claimed.

## Integrity boundary

The producer establishes the receipt from one implementation.  A checker that
imports none of that code independently reconstructs the same mathematical
objects.  A separate SymPy script checks 73 exact predicates.  Canonical
replay requires byte identity, and eighteen hostile field changes must all be
rejected.  These checks support reproducibility; they do not convert the
source zeta into a target-facing Fredholm determinant.
