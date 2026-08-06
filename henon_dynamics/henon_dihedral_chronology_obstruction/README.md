# Dihedral quotients of the area-preserving Hénon family

## Outcome

This project closes candidate **HCS-C12C** in its registered form.

The exact Paper-5 recurrence

\[
q_{t+1}=1-Aq_t^2-q_{t-1}
\]

is conjugate, away from \(A=0\), to the Hamiltonian Hénon recurrence

\[
x_{t+1}=A-x_t^2-x_{t-1},\qquad x_t=Aq_t.
\]

The proposed parameter-varying exact-period quotient therefore collides
directly with the orbital-polynomial and reversor-class program of
Endler--Gallas (2002--2006) and Gallas (2007).  The coarse quotient also
retains only the trivial dihedral representation sector.  It remembers an
unlabelled, unoriented orbit, but not a marked phase, reversal orientation, or
the non-trivial joint Hénon--Frobenius representation data.

Quotienting cyclic phase is standard for an autonomous scalar dynamical zeta;
the invariant-sector identity is therefore not, by itself, a no-go for every
orbit zeta.  It is a precise limit on claims that the coarse curve preserves a
non-trivial chronological action or its isotypic arithmetic information.

The first chiral case, period six, also fails the proposed cohomological gate:
all three components of the squarefree dihedral orbit-marker curve have
genus zero, so their smooth projective normalizations have no weight-one
\(H^1\).

The formal decision is

```text
HCS-C12C: STOP_SCOPED_PRIOR_MARKER_COLLISION_NO_GLOBAL_DETERMINANT
```

This is a scoped decision.  It does not rule out an equivariant tower of
exact-period covers with non-trivial \(D_n\)-isotypic coefficient systems, or
an ordinary autonomous zeta that intentionally sums unmarked cycles.  The
registered reframe was not promoted: at fixed \(n\) it is still a
finite-monodromy Artin system, with no canonical prime clock, cross-period
tower maps, or target divisor.

## Main exact statements

On a discriminant-free parameter open set, let \(\mathcal P_n\) be the exact
period-\(n\) cover.  Its generic degree is

\[
\nu(n)=\sum_{d\mid n}\mu(n/d)2^d.
\]

The Hénon map \(H\) acts freely and the reversor \(R\) satisfies

\[
R^2=1,\qquad RHR=H^{-1}.
\]

Writing \(M_n=\nu(n)/n\), define

\[
A_n=\sum_{d\mid n}\mu(n/d)2^{\lfloor(d+1)/2\rfloor},\qquad
Q_n=\sum_{d\mid n}\mu(n/d)2^{\lfloor(d+2)/2\rfloor}.
\]

The numbers of diagonal, non-diagonal, and chiral cyclic orbits are

\[
D_n=\begin{cases}A_n,&n\text{ odd},\\A_n/2,&n\text{ even},\end{cases}
\quad
N_n=\begin{cases}0,&n\text{ odd},\\Q_n/2,&n\text{ even},\end{cases}
\quad
C_n=M_n-D_n-N_n.
\]

Here \(C_n\) counts cyclic orbits, so the number of chiral doublets is
\(C_n/2\).  The coarse dihedral quotient has generic degree

\[
\deg(\mathcal P_n/D_n)=D_n+N_n+C_n/2
=\frac{M_n+D_n+N_n}{2}.
\]

These formulas are prior work, not a novelty claim.  The executable audit
also catches an internal arithmetic typo in the published period-14 table:
the displayed inputs imply 493 chiral doublets, not 500.

## Reproduce

Requires Python 3 and SymPy.

```bash
python code/c12c_audit.py --max-period 35 --out-dir results
python code/test_c12c_audit.py
```

The first command writes a machine-readable certificate and the full counting
table.  The test suite checks the identities against frozen low-period values
and integrality constraints.

All orbit counts are generic algebraic/complex counts in the complete
two-symbol regime.  They are not counts of bounded real trajectories near the
Paper-5 numerical value \(A\approx1.02\).

## Directory map

- `DERIVATION_PACKAGE.md`: precise mathematical argument and scope.
- `SOURCE_AUDIT.md`: primary-source equivalence and novelty boundary.
- `code/`: exact symbolic and combinatorial audit.
- `results/`: generated certificate and decision record.
- `paper/`: short paper draft for the negative result.
- `evaluations/route_a/`: Route-A assessment.
- `REPOSITORY_UPDATE.md`: append-only repository handoff.
