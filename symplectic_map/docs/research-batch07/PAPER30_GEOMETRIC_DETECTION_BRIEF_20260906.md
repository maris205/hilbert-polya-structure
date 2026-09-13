# Paper30 candidate brief: geometric periodic detection of polynomial coboundaries

Date: 2026-09-06. Status: SAME_COMPLETE_INPUT_FOR_BLIND_CANDIDATE_REVIEWS.
This selection-stage brief is now frozen for two fresh candidate reviewers.
It is not a formal Paper30 project, a manuscript, a capacity exception or an
accepted paper. Batch07 remains 3/5. The quantum and wild-cover results are
separate, unselected problems and contribute no claims or pages here.

## 1. Decision requested and unchanged conjunctive gates

Two fresh, mutually blind independent reviewers are to receive the same
completed package. Each must independently give novelty at least 7.5/10,
research value at least 7.5/10, proof confidence at least 9/10, and credible
support for **22–30 substantive body pages**. Both reports must pass every
condition. Do not combine the better dimensions from different reports.
An independent proof check is not a candidate or page-capacity PASS.

The format assumption is an anonymous English single-column `article`,
11pt, letterpaper, one-inch margins, ordinary spacing and normal theorem/
display layout. References start on a separate page and are excluded from
the body count. Exposition should make the new arguments independently
readable, but inherited results and standard tools must not be expanded to
fill the minimum. Do not duplicate the scalar and multiphase theories,
reprove long Paper29 arguments, or count conditional corollaries repeatedly.
Paper29's special one-time natural-draft permission does not extend here.

This is one candidate about replacing infinitesimal periodic information by
actual point values in the polynomial cohomological equation. The positive
rank mechanism, the parameter-family certificate and the local obstructions
are to be assessed for genuine cohesion, not assumed to form a long paper
merely because they appear together in a dossier.

## 2. Inputs and reading responsibilities

All files below are in this directory. The author proofs and their existing
checks are frozen; their earlier status headings describe their dates of
creation and are not revised retrospectively. Root has fully read them.

| Author input | Lines | SHA256 |
| --- | --- | --- |
| `PAPER30_GEOMETRIC_TEST_PROBE_20260906.md` | 356 | `c2520f2651270b0fddc24a53ace06dca8c5486b9ab1180d7554f58670ce58f73` |
| `PAPER30_GEOMETRIC_TEST_ERRATUM_20260906.md` | 103 | `376504c6085b2e2d9abd1d599fd1913bd07ad23443073504dbdc8afcac052a05` |
| `PAPER30_GEOMETRIC_RANK_DETECTION_PROOF_V1_20260906.md` | 320 | `9544b15fcef634697e21a33e85d55f0a656728ba01f225b47e57148d6009e79d` |
| `PAPER30_GEOMETRIC_UNIFORM_PERIOD_ADDENDUM_20260906.md` | 251 | `3a61b858489516689e33f709aaf1572e37754f2cc5840f412df1b403d9772839` |

Read these four inputs and this brief completely, together with:

- `PAPER30_GEOMETRIC_INDEPENDENT_CHECK_20260906.md`, 329 lines, SHA256
  `55e74b146e1d53d2a0103bc1886bdc129fe83f6f85195a85b750c5d51c0674f3`;
- `PAPER30_GEOMETRIC_ERRATUM_CHECK_20260906.md`, 63 lines, SHA256
  `ddde8026f532237fd95abd352b3216dad27e71b930ce1bcb30c46542d29d1f48`;
- `PAPER30_GEOMETRIC_RANK_INDEPENDENT_CHECK_20260906.md`, 291 lines, SHA256
  `14a0f35e87eac526def0869fc32e85e55474f3825be275a484be00f5b6eb0442`;
- `PAPER30_GEOMETRIC_UNIFORM_INDEPENDENT_CHECK_20260906.md`, 347 lines, SHA256
  `a1d4ded856db07b14da6178844dde6d212287652336869a9c0628a53ce6591f1`;
- `PAPER30_GEOMETRIC_SADDLE_COUNT_PRIOR_20260906.md`, 84 lines, SHA256
  `4b9b2348241449f652bcbf9f86997344940df276418302cafcab81b35dcaa160`;
- `PAPER30_GEOMETRIC_DETECTION_NOVELTY_20260906.md`, 113 lines, SHA256
  `39133ec0bc091a09438bc70741ec6d1c615b82e1148330ee6759e7329eec9018`.

All mathematical reports and the dedicated novelty report have completed,
and root has fully read them. G1–G5 are independently PROVABLE AS STATED;
there is no additional theorem-level correction to those two newer proofs.
Directly relevant accepted Paper29 source sections may be inspected
to resolve a concrete inherited dependency; do not reopen its build or PDF.
The portfolio's occupied-scope list may be consulted for local noncollision.

The original geometric probe's OPEN global question has subsequently been
addressed by the rank proof and addendum. Its genuine finite-period/lcm
wording error is superseded only by the explicit, independently closed
erratum. Neither that correction nor the new proof silently changes the
short-period counterexample or other checked local results.

## 3. Precise object and inherited input

Fix an ordered tuple of degrees d=(d_0,...,d_{k-1}), each d_i at least two,
and arbitrary complex polynomials p_i of exactly those degrees, with nonzero
leading coefficients. Put

\[
H_i(x,y)=(p_i(x)-y,x),\quad F=H_{k-1}\circ\cdots\circ H_0,\quad
\sigma=F^*,\quad A=\mathbb C[x,y],\quad \delta=\prod_i d_i.
\]

The actual orbit coordinates obey X_0=x, X_{-1}=y,
X_{i+1}+X_{i-1}=p_i(X_i), and sigma X_i=X_{i+k}. Write
S_n g=sum_{j=0}^{n-1} sigma^j g and N=kn. The complete cyclic periodic
ring A_N has dimension delta^n for N at least three, including multiplicity.
Its geometric points are all of Fix(F^n), not only least-period-n points.

Paper29, building on Bousch's quadratic orbit algebras, supplies the standard
words M_e=product X_i^{e_i}, 0<=e_i<d_i, finite support; their mixed-radix
ordinary degrees; the orbit-coefficient criterion for g in (sigma-1)A;
and no-alias scheme detection when N>2L(g). L(g) is the largest diameter of
an **individual** nonconstant word in the normal form, not its total span.

The degree bound D is a nonnegative integer. One may take the inherited exact bound

\[
L_D=\max\bigl(\{b-a:a<b,\ w_a+w_b\le D\}\cup\{0\}\bigr),\quad
w_0=w_{-1}=1,
\]

where w_i is the outward product of the appropriate phase degrees.
It bounds L(g) for every polynomial of ordinary degree at most D and is
coefficient-independent. The proof of this bound, Paper29's Hilbert series,
degree-preserving primitives, rational-pole rigidity, sharp scheme threshold
and symplectic-extension application are inherited or excluded, not new
headlines in the present package.

## 4. Positive results to assess as one chain

Set C_D=floor((D+2)^2/4) and eta_D=1/C_D. All following bounds use D>=0;
there is no division by D in the constant case.

**Finite rank and zero-count certificate (G1, strengthened by G4).** For
deg(g)<=D, g not in (sigma-1)A, N>=3 and N>2L_D,

\[
\operatorname{rank}(m_{[S_ng]}:A_N\to A_N)\ge\delta^n/C_D,
\qquad
\#\{z\in\operatorname{Fix}(F^n):S_ng(z)=0\}
\le(1-1/C_D)\delta^n.
\]

A sufficient finite detection certificate is therefore
r_n(F)>(1-1/C_D)delta^n, where r_n counts distinct geometric points.
More than this number of distinct tested points also suffices. This is a
zero-count consequence, not a separate coding or statistical theory.

The rank proof uses the normal-form leading monomial z^e: multiplication
images indexed by 0<=u_i<d_i-e_i retain distinct standard leading monomials.
The degree improvement applies the elementary digit inequality
product b_j/(b_j-e_j)<=a+1 to each of the two mixed-radix coordinate tails.
A representative occurring in g has leading coordinate monomial x^a y^b,
so its reciprocal rank fraction is at most (a+1)(b+1)<=C_D. Macro shifts
and nonoverlapping wrapping preserve this product even though the ordinary
degree of a far translated word need not remain at most D.

The digit product inequality is sharp across the allowed degree families
and on a binary subsequence. This is **not** a proof that actual periodic
orbit sums attain the rank bound, zero-count bound or a best detecting period.

**Fixed-map eventual geometric/saddle detection (G2).** For every fixed F,D,
there is n_0(F,D) such that every integer n>=n_0 and every deg(g)<=D satisfy

\[
S_ng(z)=0\text{ on all saddle points of least period }n
\quad\Longleftrightarrow\quad g\in(\sigma-1)A.
\]

The same holds on all geometric fixed points. Each non-coboundary has
nonzero orbit sum at more than delta^n/(2C_D) exact-period saddle points
for all sufficiently large n, uniformly over g in that degree range.
The only dynamical count input is the existing BLS theorem
#SPer_n(F)/delta^n -> 1 for each fixed complex polynomial automorphism of
dynamical degree greater than one, along all integers. No global
hyperbolicity, genericity or dissipativity is imposed here or inferred.

**Exact adaptive certificate for one map (G3).** For coefficients in a given
number field, form the full periodic trace pairing

\[
\Gamma(a,b)=\operatorname{Tr}(m_{ab})
 =\sum_z\ell_z a(z)b(z).
\]

Its rank equals r_n, and its radical is the nilradical. Enumerating the
admissible n until rank Gamma>(1-1/C_D)delta^n is an exact terminating
algorithm. After certification, the entire vector Gamma([S_n g],b), over
the standard basis b, detects the degree-bounded coboundaries. This computes
on the full scheme ring, but uses weighted geometric values and annihilates
nilpotent directions. It is not one scalar trace or an algorithm avoiding
the periodic algebra. No a priori n_0 or complexity bound is supplied.

**One period for the whole coefficient family (G5).** A terminating exact
symbolic algorithm depending only on d,D outputs an integer M(d,D) such
that for every allowed complex coefficient choice and every deg(g)<=D,

\[
S_Mg(z)=0\quad\forall z\in\operatorname{Fix}(F^M)(\mathbb C)
\quad\Longleftrightarrow\quad g\in(F^*-1)\mathbb C[x,y].
\]

All positive multiples of M work for all the same coefficient choices.
The universal coefficient ring is a finite-type Q-algebra adjoining inverses
of the leading coefficients. Each cyclic ring is finite free over it by
monic reduction. The relevant minors of the universal trace matrix define
rank-certificate opens. BLS covers every complex parameter by at least one
such open. Nullstellensatz and faithful-flat descent give a finite rational
Bézout ideal identity 1=sum h_nu Delta_nu. Exact cumulative
ideal membership therefore terminates. The least common multiple of its
finitely many periods gives M, since on Fix(F^{n_i}), S_M=(M/n_i)S_{n_i}.

The output M itself need not satisfy the same rank-count threshold; its
detection property follows by divisibility from a period appropriate to
each parameter. The proof gives neither a uniform all-large-integer threshold
nor a uniform BLS convergence rate. It reports no computed M and no useful
runtime or elementary a priori upper bound. The standard algebraic tools
are explicitly deducted, not presented as a new general effective
Nullstellensatz or a new compactness principle.

## 5. Local obstruction and separation results within the same problem

The checked original probe supplies the following boundaries, not unrelated
extra pages:

- **A1:** H=(x^2-x-y,x), F=H^3, k=3, n=1, N=3 and
  g=X_0X_1-X_1X_2-X_0+X_2 have deg(g)=6 and L(g)=1. The orbit sum
  vanishes at all five geometric points while g is not a coboundary.
  Its cyclic class is nonzero, its square is nonzero and its cube is zero.
  The maximum local Loewy length is exactly three. Thus the inherited
  no-alias scheme threshold cannot just be reused for point values.
- **A2:** For every scalar quadratic H_p, all coefficients including the
  collision parameters, the actual n=3 geometric test detects every
  g with L(g)<=1. This is a short contrasting proposition, not a separate
  scalar theory or an assertion that all quadratic periods work.
- **B1:** With q=ceil((2L(g)+1)/k), n>=Bq and kn>=3,
  [S_n g]^B=0 in A_N iff g is a coboundary. The new B>1 argument places
  separated short-word blocks and isolates the nonzero coefficient B!c^B.
- **B2:** A local Loewy bound lambda_n<=B plus n>=Bq gives another
  single-period geometric certificate. A false positive at an admissible
  period forces lambda_n>=floor(n/q)+1. The earlier hypothetical all-period
  false positive is ruled out by G2; do not present it as an open possibility.
- **C1:** A bounded-coefficient quadratic family H_m, varying with m>=3,
  has a fixed point whose local Loewy length in Fix(H_m^m) is at least m-1.
  The proof uses only a finite formal normal form and a quotient onto
  C[u]/(u^{m-1}). It excludes degree-only uniform Loewy bounds and uniform
  sublinear-in-period bounds across maps, not geometric detection bounds.

G5 is compatible with C1 because a large worst local nilpotence depth does
not imply a positive proportion of the entire periodic algebra is defective.
The rank mechanism bypasses, and does not solve, worst-local Loewy control.
The scalar/macro distinction in A1 and A2 must remain explicit.

## 6. Closest prior and deductions

The dedicated novelty report records six core primary sources, exact actual-
read locations, per-claim searches and a March–September 2026 screen.
Its conclusion is NO_DIRECT_PRIOR_LOCATED_IN_BOUNDED_SEARCH, with moderate
confidence, not proof of world priority. Read its complete prior/delta matrix.

- **Bousch, 1992, Algèbres de Hénon:** the entire 13-page author manuscript
  was read by the novelty reviewer. Sections 5.1–5.2 supply orbit bases,
  wrapping and stabilization of full-period averages; Section 7 concerns
  holomorphic mixing. No geometric-point polynomial coboundary criterion
  was located there. Section 8.1's limiting-form nondegeneracy lemma is
  explicitly unproved in that manuscript. This does not erase Bousch's
  foundational contribution or Paper29's already accepted extension.
  [Author manuscript](https://www.imo.universite-paris-saclay.fr/~thierry.bousch/preprints/alghenon.pdf).
- **Bedford–Lyubich–Smillie, 1993:** Corollary 1 in the author version is
  exactly the least-period saddle point asymptotic used here. It is a major
  external dynamical input, fully deducted. G2's final subtraction once G1
  is known is short, not a new periodic-count theory.
  [Original author version](https://arxiv.org/pdf/math/9301220v1).
- **Geil–Høholdt, 2000:** the footprint/leading-ideal control of a geometric
  zero set is a classical method. The actual-read Theorem II.16.4 and the
  following page of the author collection concern just this type of bound.
  The staircase rank calculation is not a new general algebraic principle.
  [Author collection](https://people.math.aau.dk/~olav/footorgenBez.pdf).
- **Dilsavor–Marshall Reber, 2024, A positive proportion Livshits theorem:**
  Theorem 1.1 and the Axiom A remark are strong direct neighbors. In their
  hyperbolic/Hölder category, positive asymptotic upper density of zero
  periodic sums forces a Hölder coboundary. Their fixed-observable density
  conclusion is stronger than a fixed positive nonzero fraction in that
  category. It does not provide the present all-parameter polynomial
  transfer function or degree-uniform single-period theorem. Do not claim
  to invent positive-proportion periodic detection.
  [Author version](https://arxiv.org/html/2304.01372v2).
- **Bianchi–He, June 2026 preprint:** its thermodynamic path metric treats
  hyperbolic components and complex unstable derivative cocycles. Section
  2.6, Lemma 2.7, uses the Hölder Livšic covariance criterion on a symbolic
  model. It is recent Hénon-specific prior, not a theorem for arbitrary
  polynomial observables and every complex coefficient choice.
  [Version 1](https://arxiv.org/html/2606.29363v1).
- **Janovitz-Freireich–Szántó–Mourrain–Rónyai, 2008:** trace/moment matrices
  and recovery of the radical algebra are mature exact algebraic tools.
  G3's delta is the periodic search and its dynamical termination argument,
  not a new trace form, radical algorithm or root-counting method.
  [Author version](https://arxiv.org/html/0812.0088v1).

The finite-cover/Nullstellensatz/faithful-flat descent, exact ideal-membership
and lcm steps in G5 are standard as well. Its possible standalone interest
is the concrete all-coefficient geometric detection property that these
certificates actually establish, not the introduction of a new Noetherian
principle. G4 is an elementary degree-constant strengthening within that
argument. Reviewers must decide how much remains after those deductions.

The 2026 finite-Livšic seminar announcement in the dedicated report is
SCREEN_ONLY, not a read full theorem; its approximate Anosov/Hölder result
must not be described as completely ruled out. Older Markov-system
regularity and recent Hénon multiplier-rigidity literature are also compared
there at their actual reading levels. Unindexed polynomial cohomology work
remains a real literature uncertainty. No broad priority claim is justified.

Locally, Paper29 treats complete-scheme detection and polynomial filtration,
not this all-parameter geometric criterion. The explicit A1 example makes
the logical difference real. Nonetheless a new object boundary alone does
not automatically establish sufficient standalone value or 22-page capacity.

## 7. Natural organization and reviewer obligations

A possible dependency order is: precise problem and strongest prior; compact
orbit-basis preliminaries; finite-period collision and scalar contrast;
separated-block nilpotence and the resonant Loewy family; multiplication rank
and ordinary-degree control; eventual saddle/geometric detection; trace-form
certification; the universal family and one-period algorithm; limitations.
This is not a page allocation or an assertion that all deserve separate
sections. Reviewers must identify overlap and compress short corollaries.

Supply independent low/central/high natural body estimates by substantive
section, a candid standalone-value assessment, all four individual gates,
and the conjunctive outcome. Do not invent unproved optimality, explicit M,
parameter-uniform asymptotics, practical complexity, quantum/wild material,
arithmetic spectra or numerical experiments to make the package pass.
Suggestions for later results are unproved and do not count as present
capacity. No manuscript measurement is requested or authorized by this brief.

Reviewer provenance is the actual fresh secondary agent under the available
research-review workflow with xhigh reasoning, not an external human referee
or an unavailable specified GPT-5.4/Codex-MCP endpoint. Route A/B applicability
is NOT_APPLICABLE. All effects are local, with no mutations of accepted
Papers27–29 and no upload, submission or paid computation.
