# X2: four obstruction-transfer tests for live interfaces

2026-09-09 UTC. First-wave adversarial synthesis, not a formal evaluation
or review of uncreated papers. All old artifacts are read-only. No
mathematical program, PDF build, Git write, external model, API upload,
or shared-index mutation was performed.

## Exact question and source subtraction

For the fourteen investigations in `SCOUT_PLAN.md`, which proposed
joins preserve the existing obstruction's actual hypotheses, domain,
native time, and observable? Success here is an equation proving
preservation, an explicit falsifier, or a precise missing hypothesis
that a named consumer can test. Failure of that join is not failure of
its original full family question.

Imported source theorems remain proved and are not re-admitted:
C12A finite periodic schemes/Frobenius collapse; C426/GR5 all-affine
good models; WM6 multiplier-norm platform; the PC424-L trace and
algebraic-descent auxiliaries; LG4's profinite closure and bounded-degree
branch. The new substantive derivation is the prescribed-order jet
counterexample in [the supplement](PERIODIC_JET_COUNTEREXAMPLE.md).

All source paths below are relative to `henon_dynamics/` unless an
external URL is given. Locators identify original proof passages,
not just registry summaries.

Directory abbreviations: C12A = `henon_frobenius_scheme_obstruction/`;
C426 = `research_c424_c428/papers/C426_affine_good_models/`;
C413 = `continuation_c409_c413_round2/papers/C413_integral_trace/`.

| Test | Named consumers | Reject the join when… | What remains live |
| --- | --- | --- | --- |
| 1: reduced points versus local lengths | A1, A2, A3, A4; D2 | data factor through reduction, or through the proved trace-zero block, but the conclusion needs nilpotents/length | local algebras, integral lifts with extra data, characteristic polynomials, genuinely constructed finite transfer |
| 2: completed time versus integer time | B1, B2; C2 | compactness, finite local zeros, or factorwise linearization is used as the missing integer-time theorem | a quantitative height/precision bridge or a different full separation argument |
| 3: local jets versus global good chart | B3, B4; C1 | raw coefficients are called invariant, or bounded-order local jet integrality is called potential good reduction | a canonical lattice/gauge, degree-dependent cutoff, exact jet invariant, cross-periodic-point compatibility |
| 4: Frobenius versus native cycle owner | D1, D2, C4; A3 | commutation or rectangular counts are used to identify actions/clocks/prime owners | joint action, rotation holonomy, actual monodromy, a separately proved native arithmetic correspondence |

## 1. Ordinary cycles do not determine nonreduced lengths

### 1a. Reduction blindness survives genuine recoding and field extension

For every finite field extension $K/k$ and every finite $k$-scheme $X$,

$$X(K)=X_{\rm red}(K). \tag{1}$$

Every map from a field kills nilpotents. For example
$X_e=\operatorname{Spec}k[t]/(t^e)$ has one geometric point for every
$e\ge1$, while its geometric local length is $e$. Base extension does
not restore that length from ordinary points. A bijective recoding of
the point dynamics preserves its cycles, not its missing local algebra.
An algebraic conjugacy that actually identifies local algebras does
preserve length; these are different premises.

Source: `henon_frobenius_scheme_obstruction/paper/sections/3_periodic_schemes.tex`,
Theorem `thm:flat` and its final reduced-fibre distinction; and
`sections/4_frobenius_obstruction.tex`, Theorem `thm:collapse`, complete proof.
The stronger étale-cohomology invariance under nilpotent thickenings is
the explicit hypothesis/conclusion of
[Stacks, Proposition 59.45.4](https://stacks.math.columbia.edu/tag/03SI)
(statement and proof accessed). Therefore replacing ordinary counts
by their standard étale trace does not make nilpotent length intrinsic
to those already reduced data.

**A3/A4 check:** specify the actual local algebra and a scheme comparison,
not just its support or a formally similar recurrence. The older
`continuation_c407_c408_round3/ROOT_CLUSTER_REVIEW.md`, “Scope clarification”,
provides a second early test: the unsaturated alternating-zero relation
algebra has embedding dimension $m$, so for $m>2$ it cannot be a fixed
local scheme of an endomorphism of a smooth surface, whose quotient
local ring has embedding dimension at most two. This invariant survives
local algebra isomorphism and field extension. Saturation or changing
the ambient model changes the object and needs its own comparison.

### 1b. Trace blindness survives the proposed trace-only combinations

In characteristic $p$, on an exact-$n$ orbit block
$A_O=\prod_{a\in O}k[t_a]/(t_a^e)$ of a fixed-point algebra, with native
substitution $\sigma^n=1$, the source proves

$$
 \operatorname{tr}(m_U\sigma^j)=
 \begin{cases}0,&n\nmid j,\\ e\sum_{a\in O}U(a),&n\mid j.
 \end{cases}
 \tag{2}
$$

Source: `research_c424_c428/continuation_round4/positive_characteristic/PROOF_PACKAGE.md`,
Steps 2–4, auxiliary propositions 1–3. Its proof explicitly uses the
factor-permuting block matrix and the multiplication trace
$\operatorname{tr}(m_W)=\sum_a e_aW(a)$. If $p\mid e$, all of (2) vanish,
even when $p\nmid n$ and Reynolds averaging by $1/n$ is allowed.

Conjugation preserves trace; scalar extension carries the same zero
to the new field; traces add on direct sums and multiply on tensor
products. Thus a finite word/sum/tensor construction from those
multiplication/shift operators does not repair that zero block merely
by taking another ordinary trace. This statement requires that the
construction continue to factor through that operator algebra—new
operators probing jets are not silently included.

The abstract example $k[t]/t^p$ already has
$\operatorname{tr}(I^j)=0$ for every $j\ge1$, but
$\det(TI-I)=(T-1)^p=T^p-1$ still records degree $p$. Exterior-power or
characteristic-polynomial data are therefore **not** covered by the
trace-only exclusion. Nor is a Witt/integral lift of the entire local
algebra. A lift applied only to a scalar trace that is already zero
cannot distinguish the original local lengths. No assertion is made
here that such a $p$-divisible length occurs at every needed quadratic
primitive period: that would be an extra global theorem.

**A1/A2 check:** the auxiliary descent theorem requires an actual finite
extension $E/k(x)$ and compatible embedding with $\sigma u-u=h$.
`research_c424_c428/continuation_round6/positive_characteristic/PROOF_AND_GAPS.md`, §§1–7
proves descent, while §9 explicitly leaves $K_c\subseteq A_c$ missing.
Independent finite-field interpolants do not provide this object.
An exact escape direction remains: construct that finite stable object,
with a uniform finite algebraic relation and compatible embedding.
The descent hypothesis $p\nmid\deg f$ is essential: §8's genuine
counterexample uses $x=t^q-t$, $\sigma(t)=t^q$, $f=x^q$, $h=x$.
It has a finite algebraic transfer but no polynomial transfer by degree.

**Contract warning for A3:** the sealed original PC424-D question is
the full geometric component classification of the **reduced**
$\Phi_{p^e}(x,c)$ for all odd $p,e$, not just local lengths. See
`research_c424_c428/positive_characteristic/FROZEN_CONTRACTS.md`,
“PC424-D”, and the R5 `PROOF_AND_GAPS.md`, §1. A local multiplicity
tower may be a bridge, but cannot silently become the original answer.

## 2. Profinite completion is not integer-time rigidity

For $F\in\operatorname{Aut}_{\mathbb Z}(\mathbb A^2)$ and nonperiodic
$P\in\mathbb Z^2$, let $r_m$ be the native period modulo $m$. The
proved map

$$
 \theta_P:\widehat{\mathbb Z}\overset\sim\longrightarrow
 \overline{\{F^nP:n\in\mathbb Z\}},\qquad
 (\theta_P(t))_m=F^{t\bmod r_m}P\pmod m
 \tag{3}
$$

is a homeomorphism. LG4's remaining assertion is exactly

$$\theta_P^{-1}(\mathbb Z^2)=\mathbb Z. \tag{4}$$

Source: `research_c424_c428/continuation_round4/arithmetic/PROOF_PACKAGE.md`,
§§2–3 (valuation growth and full mixed-modulus construction), §5 (R).
Thus mixed-modulus compatibility is already handled; independently
gluing arbitrary local interpolation parameters is not that theorem.
Conjugacy by an integral polynomial automorphism transports (3) and
(4), so it cannot remove the remaining logical step.

Three cheap falsifiers for B1/B2:

- A finite analytic zero set does not place its elements in $\mathbb Z$:
  $t^2-2$ has simple roots in $\mathbb Z_7$ (the root $3$ modulo $7$
  lifts), but none in $\mathbb Z$. This refutes the local-zero inference,
  not LG4. [Poonen, Theorem 1 and its Mahler-series proof](https://arxiv.org/pdf/1307.5887)
  give analytic interpolation when coefficient congruence has exponent
  $c>1/(p-1)$; no integer-time conclusion is part of that theorem.
- Clearing denominators and omitting their primes changes the question:
  $F(x,y)=(x+2,y)$, $P=(0,0)$, $Q=(1,0)$ admits hits modulo every odd
  modulus, but no hit modulo $2$ and no integer orbit hit. A rational
  coordinate change must transport the whole lattice and all congruences.
- A useful sufficient height/precision interface is an actual hit
  $F^{n_m}P\equiv Q\pmod m$ with
  $\|F^{n_m}P-Q\|_\infty<m$. Every coordinate difference is then zero.
  Escape alone supplies no bound of this kind for the chosen $n_m$;
  allowing time/height to grow with the modulus gives no contradiction.

### Factor combinations do not preserve the finite-rank hypothesis

The proved Segal branch assumes $\sup_{n\in\mathbb Z}\deg F^n<\infty$;
then the span of all iterated coordinate polynomials sits in one
finite-rank saturated integer lattice. Source: same LG4 proof, §4.2;
[Segal, Theorem 7.2.3(i), printed p.232, PDF p.10](https://www.math.auckland.ac.nz/~obrien/segal-survey.pdf)
requires both the module group and acting subgroup to be virtually
polycyclic. Statement and adjacent proof reduction were accessed.

For a concrete failed transfer take
$S(x,y)=(y,-x)$ and $U(x,y)=(x,y+x^2)$. Each has uniformly bounded
iterate degree, but

$$US(x,y)=(y,y^2-x),\qquad \deg(US)^n=2^n\quad(n\ge1). \tag{5}$$

The last identity follows inductively from the unique highest-degree
term in the recurrence. Factorwise linearization therefore does not
yield the needed common finite-rank module. This is not a counterexample
to orbit separation for $US$.

**C2 clock check:** if replacing $F$ by $F^a$, a native $n$-cycle
splits into $\gcd(n,a)$ cycles of length $n/\gcd(n,a)$. A fixed
composition is its own native map; primitive cycles of individual
factors are not composable period ledgers. The finite-phase lift of
an ordered length-$a$ word returns to a marked phase after $a$ steps;
an orbit of native word-period $n$ has phase-lift period $an$.
These elementary identities state the exact clock conversion, not
an authorization to change the frozen C2 clock.

## 3. Coordinate jets and intrinsic affine good reduction

### 3a. Raw jet coefficient integrality is not affine invariant

For the good map $F=(y,y^2-x)$ and $S_s(x,y)=(sx,sy)$,

$$S_s^{-1}FS_s=(y,sy^2-x). \tag{6}$$

Taking $|s|>1$ makes the second-jet coefficient at the fixed origin
nonintegral, while potential affine good reduction is unchanged.
For a general affine $T(z)=Az+c$ and periodic return $F^n$,

$$D(T^{-1}F^nT)=A^{-1}D(F^n)A,$$
$$D^j(T^{-1}F^nT)=A^{-1}D^j(F^n)[A\cdot,\ldots,A\cdot]. \tag{7}$$

First-order eigenvalues survive, but higher coefficient norms require
a transported lattice/tensor norm. Source: C426 `sections/03_local_rigidity.tex`,
top-homogeneous identity and integral-affine coset invariance; WM6
`research_c424_c428/continuation_round6/arithmetic_spectral/PROOF_PACKAGE.md`, assumptions
and §§3–5. “Intrinsic” must specify the lattice or quotient gauge, and
whether base extension and native repetition preserve the observable.

### 3b. Even all periodic low-order integral jets are insufficient

For each fixed $N$, [the complete supplement](PERIODIC_JET_COUNTEREXAMPLE.md)
constructs, over $\mathbb Q_p$,

$$F=(y,y^{p^{r+1}}+p^{-1}y^{p^r}-x),\qquad
r=\lfloor\log_pN\rfloor+3. \tag{8}$$

At every actual periodic point all centered forward/inverse return
$N$-jets are integral with unit linear determinant, but no finite
extension admits any good affine model. The decisive bound is

$$|[u^j](f(z+u)-f(z))|
 \le p^{-r+v_p(j)}R^{d-j}<1\quad(1\le j\le N),
\quad R=p^{1/(d-p^r)}. \tag{9}$$

The proof uses all native periods, not a census or a fixed-point guess.
The obstruction is that separate integral local charts do not patch
to the unique good radius-one disc: two scalar fixed points are
distance $R>1$ apart. **B4:** reject a degree-independent jet-integrality
criterion immediately; retain exact coefficient invariants,
degree-dependent cutoffs and cross-point compatibility as distinct
possibilities. WM6 remains a norm-spectrum failure, not an assertion
that exact multiplier spectra agree or all spectral data are blind.

### 3c. Base change does not preserve every original-field obstruction

C426's scale condition is $-v(b)/(d-1)\in\mathbb Z$. A ramified
extension of index $e$ multiplies $v(b)$ by $e$, so this failure can
disappear. If all local models already exist over a number field $K$,
the global obstruction is $[I]^2\ne1$; after an extension $L/K$ it
must be retested as $[I\mathcal O_L]^2$, which can vanish by
principalization. In contrast $|a|\ne1$ and the explicit WM6
distance obstruction survive every finite extension.

Source: C426 `sections/02_classification.tex`, Theorem `thm:main`,
and `sections/05_global.tex`, determinant identity $I^2=(\det A)$
and final coordinate-invariance paragraph. **B3:** original-field
global no-model does not mean no potential model and does not mean
no periodic points. Combining two modules can cancel determinant
classes: for example $\det(I\oplus I)=I^2$ can be principal even
when $I$ is not. Conversely unrelated local model modules do not
assemble one native periodic observable without an additional map.

**C1/C3 domain seam:** an affine rational conjugacy preserves rational
cycles, but preserves an integral atlas only on the transported
lattice $T^{-1}\mathbb Z^d$, not automatically on $\mathbb Z^d$.
C424/HEN-O408 and C428/HEN-O412 explicitly exclude replacing
$\mathbb Z[t]$ by arbitrary $\operatorname{Int}(\mathbb Z)$ or
$\mathbb Q[t]$. For a direct rational-period witness in the Vieta
return source, C413 `sections/5_scope.tex`, equation
`eq:rational-example`, has
$T(3,3/2,3)=(3/2,3,3/2)$ and its reverse, an actual nonintegral
two-cycle. Denominator strata require their own recurrence argument;
the old integer-neighbour finite alphabet is not transported intact.

## 4. Frobenius/prime labels are not native primitive orbits

### 4a. Actual Hénon witness and the necessary holonomy interface

Over $\mathbb F_3$, $H(x,y)=(y,y^2-x)$ has the ordinary cycle

$$
(1,1)\to(1,0)\to(0,2)\to(2,1)\to(1,2)\to(2,0)
\to(0,1)\to(1,1). \tag{10}
$$

Each arrow is direct substitution and the seven points are distinct,
so its native least period is $7$. Arithmetic Frobenius fixes every
point. This hand calculation is a concrete member of the generalized
Hénon class, not a hypothetical arbitrary permutation model.

More generally let $H$ and $\Phi$ commute on a finite set, and let
$P$ have native $H$-period $n$. If the $\Phi$-orbit of its native
cycle has length $e$, write uniquely

$$\Phi^e P=H^aP,\qquad a\in\mathbb Z/n\mathbb Z.$$

Then the Frobenius point-period is exactly

$$D=\frac{en}{\gcd(n,a)}. \tag{11}$$

Proof: a return to $P$ must first return to its native cycle, hence
has time $eh$; commutation gives $\Phi^{eh}P=H^{ah}P$, which returns
exactly when $n\mid ah$. Thus both cycle permutation and within-cycle
rotation are needed. Under base extension $\mathbb F_q\subset
\mathbb F_{q^b}$, Frobenius becomes $\Phi^b$, so $D$ changes to
$D/\gcd(D,b)$, whereas geometric native period $n$ does not change.

### 4b. Counts and commutation do not supply the missing phase

C12A `paper/sections/4_frobenius_obstruction.tex`, “What the rectangular
table forgets”, proves that on $\{\pm1\}\times\mathbb Z/5$,

$$H(\epsilon,i)=(\epsilon,i+1),\quad
\Phi_c(\epsilon,i)=(\epsilon,i+\epsilon c)$$

with $c=1,2$ gives identical untwisted Frobenius traces for every
power but
$\operatorname{tr}(\Phi_1H^{-1})=5\ne0=
\operatorname{tr}(\Phi_2H^{-1})$. Both also commute with the stated
reversor. Recoding the joint action preserves this difference; keeping
only the Frobenius marginal loses it. The legitimate interface is

$$T(r,s)=\operatorname{tr}(\Phi^rH^{-s})
=\#\{P:\Phi^rP=H^sP\}, \tag{12}$$

with its two axes still distinguished. A diagonal restriction needs
its own theorem; substituting $u=p^{-s}$ is not one.

**A3/C4:** native commutation with Galois does not put the native
rotation inside the Galois group. R5 positive-characteristic
`PROOF_AND_GAPS.md`, §4, derives
$\#\operatorname{Irr}\Phi_{p^e}=\sum_jp^{e-h_j}$, where
$p^{h_j}$ is the rotation image of a native-cycle stabilizer. A
transitive cycle quotient still requires full rotation image for
point transitivity. The finite étale algebra $K^n$ with cyclic native
permutation has one cycle but trivial Galois action and $n$ components.
It is an inference counterexample, not a quadratic dynatomic one.

**D1/D2:** a non-tautological bridge must supply the phase data in
(11)/(12), its compatibility under base extension and repetition,
and a native reason for any prime labels. Finite zero-dimensional
Frobenius factors are still permutation-Artin factors. C12A §4
explicitly allows their global Dedekind products to have nontrivial
zeros; the obstruction is lack of a distinguished Hénon target
divisor, not a claim that those products have no zeros. Ordinary
cycle products and a local good-model valuation ideal do not become
target Euler factors by combining their labels.

## Handoff and limitations

All four actionable groups were sent to the coordinator before this
report. The jet supplement is the only new extended proof and should
receive a bounded nonauthor check if B4 uses it. The other conclusions
are exact source-hypothesis transfers and small explicit derivations,
not proposed extra papers. B1/B2's LG4, A1/A2's PC424-L, and the full
PC424-D component question are not settled by these method failures.

The proof-writer skill enforced explicit hypotheses/status and the
separation of original questions from failed methods; local-first
research-lit and the Hénon batch workflow kept source ownership and
execution boundaries explicit. Primary browsing was limited to the
Stacks proposition, Poonen's theorem/proof and Segal's specified
theorem passage; no global novelty or exhaustive search is claimed.
`NO_BAD_EULER_OR_ROOT_NUMBER`; Route B remains closed.
