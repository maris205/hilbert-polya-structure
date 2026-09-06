# Bounded primary-source and repository audit

Date: 2026-09-05. This is an admission-level search, not a systematic review,
an exhaustive current-literature certificate, or global novelty clearance.
Only public bibliographic/mathematical search terms were sent to browsing;
no private manuscript or repository payload was uploaded to another model.

## Primary materials actually accessed

1. Andrew Bridy, *The Artin-Mazur Zeta Function of a Dynamically Affine
   Rational Map in Positive Characteristic*, JTNB 28 (2016), 301–324.
   Publisher metadata and full publisher PDF were opened; the introduction,
   Theorems 1.2–1.3, Conjecture 1.4, definition, Lemma 2.1, and the
   one-dimensional group-quotient classification were inspected.
   This directly owns the zeta classification after the proved $f_2$
   Lattès reduction. It does not supply the missing non-affine theorem for
   $f_1$ or $f_3$.
   [Publisher PDF](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.941.pdf),
   [publisher metadata](https://www.numdam.org/item/JTNB_2016__28_2_301_0/).
2. Jakub Byszewski, Gunther Cornelissen, Marc Houben, *Dynamically affine
   maps in positive characteristic*, author preprint 1904.04942v1.
   The full author-hosted arXiv HTML was opened, and introduction §1.4,
   Theorem A and its non-affine limitation were inspected. Its dynamically
   affine non-holonomicity and tame-zeta results reinforce the ownership
   collision; the stated non-affine limitation is historical evidence,
   not proof of current global openness.
   [Author preprint](https://arxiv.org/html/1904.04942v1).
3. Andrew Bridy, *Transcendence of the Artin-Mazur Zeta Function for
   Polynomial Maps of A^1(Fbar_p)*, author preprint 1202.0362.
   The arXiv abstract was accessed via search. Its listed monomial/additive
   families are background only; no uninspected claim from the body is used.
   [Author abstract](https://arxiv.org/abs/1202.0362).

For the elementary elliptic-curve dependency, the official MIT course notes
were also accessed via indexed full-text results: the identity-preserving
morphism/isogeny equivalence is stated in Lecture 4 §4.2, while the 18.782
Lecture 24 Theorem 24.2 gives the group-homomorphism statement. These are
supporting authoritative exposition, not the claimed research owner.
[18.783 notes](https://math.mit.edu/classes/18.783/2025/LectureNotes4.pdf),
[18.782 theorem](https://math.mit.edu/classes/18.782/2013fa/LectureNotes24.pdf).

Vélu's original isogeny article was searched but not accessed in full. The
explicit lift in the proof note is verified by substitution, not attributed
to an uninspected statement of that article. Search returns concerning
$x+x^{-1}$ were not silently substituted for the different map
$x+x^{-2}$.

## Directed queries actually run

The bounded search used, among others, the following formulations:

- `Bridy dynamical zeta functions positive characteristic rational maps derivative constant one`
- `polynomial x+x^6 characteristic 3 periodic points zeta function`
- `dynamical zeta function separable rational map positive characteristic transcendental PCF`
- `"dynamical zeta" "constant derivative"`
- `"rational maps" "derivative one" "characteristic"`
- `"x+1/x^2" "Lattes"`
- `"x+x^{-2}" "Lattès"`
- `"x+x^6" "periodic"`
- `"x^3+x^2" finite field dynamics periodic`
- `"x^3+x^2" "zeta" "characteristic"`
- `"Bridy" "Conjecture 1.4" zeta`
- `"dynamical zeta functions" "finite fields" 2025 2026`

Several literal searches returned irrelevant algebra, finite-field
arithmetic, or polynomial irreducibility material. They were discarded,
not counted as papers addressing the proposed all-period invariant.
The search did not locate a directly applicable all-period theorem for
$f_1$ or $f_3$. This negative retrieval statement has no global novelty or
openness implication.

## Repository checks actually made

- Read `henon_dynamics/SCOUT_C399_C403.md`, specifically section D and the
  previous rejection table. The existing $\mathbb F_7$ five-cycle obstruction
  and all-tower gap are not being relabelled as a result of this lane.
- Read `research_c399_c403/arithmetic_scout/CONTINUATION_CLOSEOUT.md`.
  Its matrix/Hessian group-quotient rejections and target-arithmetic boundary
  remain in force. The $f_2$ elliptic reduction is the same excluded class,
  although not the same literal Hessian map.
- Searched Hénon markdown/TeX for literal candidate expressions, derivative
  one, unicritical, Bridy, and subadditive. The clear nearest mechanism is
  C384, `henon_wild_additive_geometric_zeta_route_a`, whose source audit and
  analytic proof already credit additive-map ownership. A polynomial merely
  written as $x+g^p$ is not necessarily additive, but derivative one alone
  does not extend that completed theorem.
- The root `literature/` directory is absent. The local root `papers/`
  inventory is from the separate symbolic stream; no relevant candidate
  source PDF was identified or read there. Unrelated material was not used
  as a surrogate literature library.

## Genuinely non-affine versus merely nonlinear

The proved lift makes $f_2$ dynamically affine despite its nonlinear
rational formula. The other two probes do not have that elementary
classification escape:

- Additive and subadditive polynomial quotients have degree a power of
  the characteristic, excluding degree six in characteristic three and
  degree three in characteristic two.
- A degree-six power or Chebyshev map in characteristic three is
  inseparable, excluding $f_1$, whose derivative is one.
- The power map of degree three has two totally invariant exceptional
  points; $f_3$ has only infinity. A finite totally invariant $a$ would
  require $x^3+x^2-a=(x-a)^3$; coefficient comparison forces both $a=1$
  from $x^2$ and $a=0$ from $x$, a contradiction.
- In characteristic two the normalised degree-three Chebyshev polynomial
  is $T_3=x^3+x$. Its only finite critical point is one and is not fixed,
  whereas $f_3$ has its finite critical point zero fixed. Both have a
  unique exceptional point at infinity, so a conjugacy between them would
  preserve infinity and hence preserve this finite critical portrait.
- A separable Lattès map of degree greater than one cannot have an
  exceptional point. Indeed, lifting a finite total backward orbit through
  the finite elliptic quotient would give a finite nonempty set whose
  inverse images under all powers of a separable isogeny remain finite and
  bounded. An isogeny is an unramified covering and these inverse images
  have cardinality multiplied by its degree at every step. This contradicts
  boundedness. Every polynomial has the exceptional point infinity.

These arguments use the existing classification as a diagnostic. They do
not solve the zeta functions of $f_1$ and $f_3$.

## Admission outcome

Exactly three candidates examined; **zero retained substantial contracts**.
The all-period route for $f_2$ is classically owned and excluded. The two
genuinely non-affine candidates defeat their simplest global-multiplicity
ansätze, and no replacement all-period mechanism was found. Further local
jets or a larger finite census would not by themselves repair that deficit.
