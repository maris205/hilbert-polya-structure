# Primary-source and collision audit

Date: 2026-08-06  
Scope: HCS-C12A WP0 and the period-five C12B reframe

## Paper-5 anchor

The local source `../docs/prior_work/papers/5-An Area-Preserving
Henon-Map Model.pdf` uses the conservative recurrence

\[
x_{k+1}=1-a x_k^2-x_{k-1}.
\]

The present project retains this map exactly.  It does not use Paper 5's
continuum approximation, quartic regularization, time-dependent parameter
schedule, or zero-calibrated spectral comparison.  The integer value \(a=6\)
is used only to obtain an integral arithmetic fiber and to reproduce earlier
C03 controls.

## Fixed points and multiplicity

Friedland and Milnor, *Dynamical properties of plane polynomial
automorphisms*, Theorem 3.1, prove that a cyclically reduced complex polynomial
automorphism of degree \(d\) has total fixed-point multiplicity \(d\), and
that the \(n\)-th iterate has total multiplicity \(d^n\).  Lemma 3.2 gives
distinctness only generically, followed by examples where points collide.

- Primary PDF: <https://deserti.perso.math.cnrs.fr/biblio/FriedlandMilnor_dynamicalpropertiesofplanepolynomialautomorphisms.pdf>
- DOI: <https://doi.org/10.1017/S014338570000482X>
- Used here for: complex precedent and the warning that multiplicity one is
  not automatic.
- Not used for: the finite-flat theorem over
  \(\mathbb Z[A,A^{-1}]\), which is proved directly by a monic Gröbner basis.

## Frobenius trace and zero-dimensional zeta

Grothendieck's Bourbaki exposé defines the closed-point Euler product and
Frobenius trace/determinant formula and proves rationality for finite-type
schemes.

- A. Grothendieck, *Formule de Lefschetz et rationalité des fonctions
  \(L\)*, Séminaire Bourbaki, Exp. 279:
  <https://www.numdam.org/article/SB_1964-1966__9__41_0.pdf>
- Relevant locations: §§1--2 for point counts and trace/determinant; Theorem
  5.1 and Corollary 5.2 for rationality.
- Applied boundary: our scheme is zero-dimensional, so the formula reduces to
  a finite permutation on \(H_c^0\).  The resulting local factor is
  cyclotomic and nilpotent-blind.

Milne's notes give an accessible independent account of Frobenius fixed points
and the Lefschetz formula:
<https://jmilne.org/math/CourseNotes/LEC210.pdf>.  They are explanatory
support, not the novelty source.

## Dynatomic multiplicity boundary

Hutz develops effective dynatomic cycles for morphisms of nonsingular
projective varieties, including the distinction between formal and primitive
period and failures when the characteristic divides the period.

- B. Hutz, *Dynatomic cycles for morphisms of projective varieties*, New York
  J. Math. 16 (2010), 125--159:
  <https://nyjm.albany.edu/j/2010/16-8p.pdf>
- arXiv: <https://arxiv.org/abs/0801.3643>
- Used here for: the multiplicity/formal-period warning.
- Applicability limit: a Hénon map extends birationally to \(\mathbb P^2\),
  not as the projective morphism assumed by Hutz.  The present affine scheme
  arguments are therefore independent.

## Compactification boundary

Diller and Favre characterize algebraic stability and birational surface
dynamics.  Their results explain why one must not treat the naive
\(\mathbb P^2\) extension as a regular compact surface automorphism.

- J. Diller and C. Favre, *Dynamics of bimeromorphic maps of surfaces*:
  <https://deserti.perso.math.cnrs.fr/biblio/DillerFavre_dynamicsofbimeromorphicmapsofsurfaces.pdf>
- Used here for: source boundary and compactification caution.
- Not used for: finite-field trace claims.

## Reversibility controls

Roberts and Vivaldi prove exact combinatorial restrictions for reversible
polynomial automorphisms over finite fields.  Their involution-fixed-set
identities explain the dominant C03 cycle signal.

- J. A. G. Roberts and F. Vivaldi, *Signature of time-reversal symmetry in
  polynomial automorphisms over finite fields*:
  <https://web.maths.unsw.edu.au/~jagr/RV05p.pdf>
- DOI: <https://doi.org/10.1088/0951-7715/18/5/015>
- Used here for: mandatory matched reversible controls.
- Not used for: their experimental limiting laws as theorems.

For the present family the reversor is direct:

\[
R(q,p)=(p,q),\qquad RH_aR=H_a^{-1}.
\]

## Higher-rank zeta boundary

Lind defines a zeta function for \(\mathbb Z^d\)-actions by summing common
fixed counts over every finite-index subgroup.

- D. A. Lind, *A zeta function for \(\mathbb Z^d\)-actions*:
  <https://sites.math.washington.edu/~lind/Papers/ZetaFunction.pdf>
- DOI: <https://doi.org/10.1017/CBO9780511662812.019>

Our \(N(r,n)\) records only rectangular subgroups of the commuting
Frobenius--Hénon action.  A full Lind object would also require twisted
nonrectangular data.  Moreover,
\(\mathbb A^2(\overline{\mathbb F}_p)\) is not the compact metric phase space
assumed in Lind's analytic theory.  Lind is therefore a structural precedent,
not a theorem that supplies analytic continuation here.

Walton's periodic zeta construction over finite fields is also relevant:

- L. Walton, *Counting periodic points on quotient varieties over
  \(\mathbb F_q\)*, J. Number Theory 192 (2018), 386--405:
  <https://arxiv.org/abs/1705.09034>
- DOI: <https://doi.org/10.1016/j.jnt.2018.03.023>

For a polynomial automorphism every point of each finite set
\(\mathbb A^2(\mathbb F_{q^r})\) is periodic, so the zeta of *all* periodic
points collapses to \((1-q^2u)^{-1}\).  This is why the present project keeps
fixed or exact chronological period.  More directly, Walton's Definition 4.6
counts fixed points of \(g\sigma_q^r\) on the periodic set and forms
character-averaged periodic \(L\)-functions from those twisted counts.  On a
reduced finite periodic fiber \(S\), take \(\varphi=H_a|_S\),
\(G=\langle H_a|_S\rangle\), and \(g=H_a^{-s}\).  Her fixed count is then

\[
\#\operatorname{Fix}(H_a^{-s}\sigma_q^r|S)
=T_{a,p,n}(r,s),
\]

since Frobenius and \(H_a\) commute.  Thus the joint trace is a sound
information-preserving refinement, but its twisted-count construction has
direct prior art in Walton rather than being a new zeta formalism.

## Exact period-five collision

The exact producer's \(a=6\) reversor-line marker is

\[
G_6(q)=46656q^6+15552q^5-20736q^4-4752q^3
       +3060q^2+360q-151.
\]

With \(x=6q\), this is \(G_6(q)=Z(6q)\), where

\[
Z(x)=x^6+2x^5-16x^4-22x^3+85x^2+60x-151.
\]

Endler and Gallas are the decisive original source for this collision.  They
start from \(y_{t+1}=1-a y_t^2-y_{t-1}\), explicitly change variables by
\(x=ay\), and at \(a=6\) publish the same \(Z(x)\) for the diagonal
coordinates of the six period-five cycles.  They also give
\(\operatorname{Disc}(Z)=2^6\cdot31\cdot241\cdot389\) and state that the
three sextics \(X,Y,Z\), in particular \(Z\), have full symmetric Galois
group \(S_6\).

- A. Endler and J. A. C. Gallas, *Reductions and simplifications of orbital
  sums in a Hamiltonian repeller*, Phys. Lett. A 352 (2006), 124--128:
  <https://inaesp.org/PublicJG/endler_gallas_orbital_sums_PLA2006.pdf>
- DOI: <https://doi.org/10.1016/j.physleta.2006.01.031>

The producer uses the scaled, nonmonic polynomial \(Z(6q)\).  Since \(Z\) has
degree six, the discriminants are related exactly by

\[
\operatorname{Disc}(Z(6q))
=6^{6(6-1)}\operatorname{Disc}(Z)
=6^{30}\operatorname{Disc}(Z)
=2^{36}3^{30}\cdot31\cdot241\cdot389.
\]

Brison and Gallas later publish the same polynomial as one member of the
period-five Hénon Hamiltonian-repeller cluster, together with companion
sextics, their discriminants, explicit polynomial bridges, and the symmetric
Galois-group statement.

- O. J. Brison and J. A. C. Gallas, *Polynomial interpolation as detector of
  orbital equation equivalence*, Int. J. Mod. Phys. C 29(8) (2018), 1850096:
  <https://inaesp.org/PublicJG/brison_gallas_interpolation_as_detector_orbital_equivalence_IJMPC2018.pdf>
- DOI: <https://doi.org/10.1142/S0129183118500961>

The collision is exact in all seven coefficients.  The producer's modular
factor-type certificate independently reproduces the \(S_6\) conclusion, but
neither the sextic, its discriminant, nor its Galois group is new.

Endler and Gallas had already performed an analogous exact arithmetic analysis
for period four:

- A. Endler and J. A. C. Gallas, *Arithmetical signatures of the dynamics of
  the Hénon map*, Phys. Rev. E 65 (2002), 036231:
  <https://inaesp.org/PublicJG/pre_EG02.pdf>

Thus low-period elimination, discriminants, or Galois tables alone cannot
promote C12B.

## Source-lock decision

\[
\boxed{
\text{C12A: NO-GO by zero-dimensional Frobenius collapse;}\qquad
\text{C12B at }n=5:\text{ prior-work collision.}
}
\]

The residual source-locked question is narrower: can a higher-period or
parameter-varying exact-period scheme produce a genuinely new theorem about
the dihedral centralizer or a positive-dimensional cohomology group?  No such
claim is made in this project.
