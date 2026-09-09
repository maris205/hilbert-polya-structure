# E1 independent internal denominator and source review

Date: 2026-09-09 UTC. Reviewer: current-session nonauthor E1. Scope: C1
integer-valued cubic feasibility/normalization and C3 rational Vieta
period-two arithmetic. This is internal mathematical review, not human peer
review, a literature-priority certificate, or paper admission.

## Verdict and required changes

**Mathematical must-fixes: 0.** The C1 auxiliary theorems and C3 main
counterexample, denominator tower, invariant calculation, and added genus
and rational-function-chart statements have been independently checked.
The original questions have different outcomes:

- **C1-UB3 remains open.** Neither an absolute rational least-period bound
  nor a family with unbounded least periods has been proved.
- **C3's frozen finite rational affine-polyhedral atlas claim is refuted.**
  This is an actual counterexample to the specified output contract, not
  merely a failure of C427's proof method.
- **Admission recommendation: retain both as complete auxiliary modules,
  with C1's original contract unresolved.** In C3 the bare negative atlas
  answer is already an elementary consequence of C421/C427's native
  three-dimensional two-period hyperbola. The positive-genus and valuation
  supplements are correct, useful, and stronger, but do not by themselves
  establish a substantial independent all-rational classification. They
  must not be promoted merely to fill a paper quota. Admission belongs to
  the coordinator.

Numbered must-fix list: **none on the inspected mathematical statements**.
The source subtraction and claim boundaries below are conditions on any
later promotion; they are not requests to enlarge the frozen question.

## Actual artifacts and source passages read

All paths in this paragraph are relative to `henon_dynamics/`.

1. `research_c429_c433/lanes/c1_integer_valued_cubic/REPORT.md` and
   `PROOF_PACKAGE.md`, in full: Theorems F/O, Steps 1–5, the ten-cycle
   supplement, and the surviving uniform-period gap.
2. `research_c429_c433/lanes/c3_rational_vieta/FROZEN_QUESTION.md` in full,
   `PROOF_PACKAGE.md` through the final 438-line version, and the final
   175-line `REPORT.md` in full: Steps 1–7, the explicit free-rational-chart
   definition and restriction compatibility, rational-function
   strengthening, genus ladder, source subtraction, and final disposition.
   The final report preserves the native clock, exact-period exclusion,
   cross-level quantifier, classical ownership, and no-admission boundary.
   Section and equation locators below remain primary if author line
   numbers move.
3. C424 actual manuscript `research_c424_c428/papers/
   C424_integer_valued_quadratic/sections/{1_introduction,2_normalization,
   3_integrality}.tex`: full degree-two rational domain, both Newton
   branches, and the half-integral normal form's local integrality proof.
4. C427 actual manuscript `research_c424_c428/papers/
   C427_vieta_semilinear/sections/{01_statement,02_blocks,03_classical,
   04_atlas,05_completion}.tex`: integral semilinear contract, actual
   nonzero-block proof, classical integral period bound, finite tagging,
   and the inherited three-dimensional hyperbola.
5. C421 actual `research_c419_c423/papers/C421_integral_return/
   sections/02_classification.tex` and `figures/TABLE_classification.tex`,
   especially the native period-two row at table line 21.
6. C417 actual `continuation_c414_c418_round2/papers/C417_integral_cubic/
   sections/{1_introduction,3_global_secant}.tex`; C428 actual
   `research_c424_c428/papers/C428_integer_period_spectrum/
   sections/01_theorem_sources.tex`; GR5 actual
   `research_c424_c428/continuation_round5/arithmetic/PROOF_PACKAGE.md`,
   theorem and local affine-rigidity proof through the common-square-lattice
   reduction. These were targeted dependency/subtraction checks, not
   reopening their sealed proofs or certificates.

No mathematical program, finite census, certificate rerun, build, Git
operation, evaluator mutation, external model call, or new agent was used.
Only this assigned review directory was written. The research-review
skill's external-model default was replaced by the explicitly authorized
current-session internal review; the proof-writer discipline was used to
separate established conclusions from the original unmet claim.

## 1. C1: denominator control is valid for the complete cubic class

Locator: C1 proof, Theorem F(1), Step 2, equations (2)–(4).
Write $6P(t)=At^3+\beta t^2+\gamma t+\delta$, with all four coefficients
integral and $A\ne0$. At any prime, select a periodic coordinate with
minimum valuation $-e<0$. If $e>v_p(A)$, the leading term has valuation
$v_p(A)-3e<-2e$, whereas every lower polynomial term has valuation at least
$-2e$. The recurrence multiplied by $6$ has valuation at least
$v_p(6)-e\ge-e$, a contradiction. This proves $Ax_i\in\mathbb Z$ for
every coordinate and every rational periodic orbit.

This uses neither a nonzero constant coefficient nor distinct neighboring
coordinates. Zero coordinates have valuation $+\infty$ and cannot be the
chosen negative minimum. Periods one and two, both Jacobian signs, negative
$A$, and the primes $2,3$ are covered. In particular no unmentioned
odd-prime exception is needed.

The refinement $E_p(P)$ is correct: exceeding each of the four displayed
thresholds makes the leading term strictly lower than every competitor
and than the recurrence bound. Entries with zero coefficients are omitted
as prescribed. The resulting exponent satisfies $0\le E_p(P)\le v_p(A)$;
individual candidate entries inside the maximum may be negative. Thus
$L(P)\mid|A|$ is a necessary bound, not a sufficiency criterion for realizing
every divisor. For $p>3$, $q=p^e$ in Theorem O has Newton coefficient
$A=6q$ and fixed coordinate $1/q$, proving exactly the stated sharpness of
the simpler exponent across free coefficients.

The real maximum inequality in Step 3 is also correct. Together with this
lattice it yields a finite rational state graph for each input. All actual
cycles lie entirely in it; every graph cycle is an actual cycle; injectivity
prevents spurious multiple predecessors. The procedure terminates without
any assumed period cutoff. Its coefficient dependence is essential, and
does not furnish the uniform integer $N$ sought by C1-UB3.

## 2. C1: the normalization obstruction has the claimed strength

Locator: C1 proof, Step 4 and Theorem O/Step 5, especially equation (7).
Comparing first components of an arbitrary affine conjugacy between the
two standard single-factor forms forces the off-diagonal entries to
vanish, the diagonal entries to agree, and the translations to agree.
The remaining equation preserves the Jacobian sign and sends a cubic
leading coefficient $a$ to $a/\lambda^2$. This verifies the squareclass
claim for exactly the stated source/target forms. It does not classify
arbitrary integral targets; that is why the separate trace argument matters.

For $P_{q,\epsilon}=qt^3-t^2+(1+\epsilon)t$,
$P_{q,\epsilon}(1/q)=(1+\epsilon)/q$, and
$P'_{q,\epsilon}(1/q)=1+\epsilon+1/q$.
At the fixed point, differentiating $T F=H T$ with $DT$ invertible makes
$DF$ and $DH$ similar. An integral-coefficient map at an integral point
has integral derivative entries and integral trace. The displayed rational
noninteger trace therefore excludes every such marked-point transport,
including nonlinear maps regular with invertible derivative there. Over
any number field, the same trace would have to be an algebraic integer;
$\mathbb Q\cap\overline{\mathbb Z}=\mathbb Z$ gives the same contradiction.

The original map already has integral coefficients: the obstruction is to
making its marked rational point integral *as well*. Singular changes,
ramified semiconjugacies, or changes undefined at the point are not excluded
and are not advertised as excluded. The obstructing point has native least
period one, so this is not an unbounded-period result.

The $s_3$ ten-cycle and the scaled words $w/q$ were checked directly from
the five displayed values and ten distinct adjacent pairs. They have least
period exactly ten; unbounded denominators under scaling do not change it.
The source-owned $s_3$ family is appropriately not counted as a new spectrum.

## 3. C3: the two-period reduction and all denominator edges are exact

Locator: C3 proof, Steps 1–2, equations (1)–(6).
For odd $n=2m+1$, native period dividing two is equivalent to an alternating
scalar word and the single equation
$u+v=(uv)^m+a$. Exact period two requires $u\ne v$.
No factor count, order of return, or change of native clock is missing.

For a nonzero pair with a denominator at $p$, order its valuations
$\alpha\le\beta$, $\alpha<0$. Equality would give
$v_p(u+v-a)\ge\alpha>2m\alpha$, contradicting the product side.
With $\alpha<\beta$, $u$ is the unique least term of $u+v-a$, so
$\alpha=m(\alpha+\beta)$. Coprimality of $m,m-1$ gives exactly
$\{\alpha,\beta\}=\{-me,(m-1)e\}$ for integral $e\ge1$.

The normal form using positive coprime $B,D$ and nonzero $r,t$ is both
necessary and sufficient *with the residual integer equation (6)*.
Reduced denominators determine $B,D$ uniquely; the opposite coordinate's
forced numerator exponents give $\gcd(rt,BD)=1$. Clearing denominators
gives precisely $rD^{2m-1}+tB^{2m-1}=(rt)^m+a(BD)^m$.
This is an exact stratification, not a solution of that nonlinear equation.

Important boundary cases:

- For $m=1$ the valuation pair is $\{-e,0\}$, not two nonzero exponents.
  The curve is $(u-1)(v-1)=1-a$. At $a=1$ it splits into the lines
  $u=1$ and $v=1$; it must not be included in the positive-genus assertions.
- Zero-containing solutions are exactly $(0,a)$ and $(a,0)$, with possible
  coincidence. They have exact period two when $a\ne0$ and are the single
  all-zero fixed point when $a=0$. Thus excluding zero pairs in Step 2 loses
  no nonintegral denominator case.
- Diagonal pairs are fixed, not primitive two-cycles. For $m=2,a=-1$,
  $u=v$ would solve $u^4-2u-1=0$. The rational-root theorem reduces to
  $u=\pm1$, neither of which works. Hence all rational points of the
  displayed quartic, including its two zero-containing points, really have
  exact native period two.

## 4. C3: the elliptic infinitude is proved, not inferred from examples

Locator: C3 proof, Steps 3–4, equations (7)–(11).
The substitution $X=u$, $Y=u^2v$ yields
$Y^2-Y=X^3-aX^2$. The inverse $v=Y/X^2$ on $X\ne0$ and
$v=(X-a)/(Y-1)$ near $(0,0)$ cover the affine curve after removing $O$
and $(0,1)$ from its projective cubic. The singularity equations force
$16a^3=27$; this is impossible for integer $a$, and $O$ is smooth.
Thus the elliptic terminology is justified, including the zero-coordinate
extension of the inverse.

For $a=-1$, the seed $Q_0=(-3/4,-1/8)$ satisfies both sides of the cubic
as $9/64$. The derived tangent/reflection formulas give
$X'=(X^4-2X-1)/(4X^3+4X^2+1)$.
If $v_2(X)=-2e$ with $e\ge1$, the cubic forces $v_2(Y)=-3e$.
The tangent denominator has valuation $1-3e$, so it is never zero.
The numerator and denominator of $X'$ have unique least valuations
$-8e$ and $2-6e$, respectively. Consequently $v_2(X')=-2(e+1)$.
Induction proves the infinite tower and
$v_2(u_k)=-2(k+1)$, $v_2(v_k)=k+1$.

Every pair is zero-free and has unequal coordinates. Different indices
give different orbits, not only different labels: exchanging the phases
would put a positive valuation into the negative-valuation slot. No rank
claim, Lutz--Nagell theorem, group generator assertion, computed list, or
finite-test extrapolation is used. This is a complete exact proof.

The no-one-time-affine-normalization claim also follows: the inverse image
of $\mathbb Z_2^5$ under any fixed invertible affine map over $\mathbb Q_2$
has coordinate valuations bounded below by finitely many matrix/translation
valuations. It cannot contain this tower. This is distinct from C1's
stronger marked-point nonlinear trace obstruction.

## 5. C3: atlas obstruction, rational charts, genus, and levels

Locator: C3 proof, Step 5; Step 7; additional genus consequence (14).
A nonconstant affine line cannot lie in $u^2v^2-u-v-1=0$: its degree-four
coefficient forces one direction to vanish, and the degree-two and degree-one
coefficients then force the other to vanish. Two different image points
of an allowed affine-polyhedral chart would supply their entire rational
segment. The curve polynomial would vanish on infinitely many points of
the corresponding line and therefore on the whole line, a contradiction.
Each chart has at most one point. The infinite native period-two stratum
therefore refutes the frozen finite labelled atlas.

The added rational-function version is also correct. A nonconstant rational
map from a rational affine parameter space to this projective elliptic
curve restricts to a suitable rational line as a nonconstant rational map.
It extends to a morphism from $\mathbb P^1$; in characteristic zero
Riemann–Hurwitz would give $-2=\deg R\ge0$. Linear parameter restrictions
do not evade the result: use the rational affine hull and its Zariski-dense
relative interior. This excludes fixed rational-function charts with free
rational parameters, not Mordell–Weil descriptions indexed by integer
multiplication. It is a supplement, not a replacement frozen contract.

For $m\ge2$, the polynomial changes $s=uv$, $w=u-v$ identify the full
period-dividing-two curve with $w^2=(s^m+a)^2-4s$. A repeated root would
force $m^{2m}a^{2m-1}=(2m-1)^{2m-1}$. A prime dividing $m$ contradicts
this for integer $a$. The degree-$2m$ polynomial is therefore squarefree,
and the two unramified points at infinity give genus $m-1$. This verifies
the exact integer-parameter range of the genus claim, not arbitrary rational
$a$ at possible singular parameters.

The invariant on the alternating locus is
$K=m s^{2m}+ma s^m-(2m+1)s$. For the elliptic tower this gives
$v_2(K)=1-4(k+1)$, so infinitely many **different levels** occur.
For any one fixed rational $a,D$, this nonconstant degree-$2m$ equation
permits at most $2m$ products $s$, and each gives at most two ordered
pairs. The stated bound of $4m$ period-dividing-two states on one level
is valid, including $m=1$ and zero pairs. It does not control other periods.

## 6. Source subtraction and substantive recommendation

The actual C424 theorem is not a universal reduction to an
integer-coefficient map on integer points. Its odd Newton branch remains
half-integral-coefficient, although its rational periodic coordinates are
integral. C1 does not falsify C424: it extends the coefficient feasibility
discussion to degree three and refutes a stronger proposed normalization.
C417 owns the monic conservative cubic branch and its integer-secant
method; C428 owns its full integral-coefficient/integer-point period spectra.
GR5 owns the complete affine regular-good-model classification. The C1
report correctly preserves these distinctions and does not paper-admit
its elementary local escape/derivative consequences.

C427's block argument explicitly uses nonzero integer factors having
absolute value at least one, and a nonzero integer product of magnitude
less than two being a unit. Those implications fail over $\mathbb Q$;
the verified pair $(21,-2/9)$ is a concrete zero-free violation of the
five-dimensional bound $|a|+4$. None of this contradicts C427's actual
integer-domain theorem.

More decisively for source ownership, C421's period-two table and C427
`05_completion.tex` lines 18–24 already display
$(u-1)(v-1)=1-a$. At fixed $(n,a)=(3,0)$, set
$u_k=1+2^k$, $v_k=1+2^{-k}$ for $k\ge1$. These are zero-free,
unequal native two-period pairs with $v_2(v_k)=-k$. The hyperbola contains
no line, so the same convex-segment proof already refutes the bare affine
atlas; the same local-boundedness argument already refutes one fixed
affine denominator normalization. These deductions require no old finite
certificate. The C3 proof's final source-subtraction note now acknowledges
this; it must remain in every later narrative.

The remaining distinct content is the fixed five-dimensional positive-genus
period-two obstruction, its self-contained exact denominator growth, and
the all-odd-dimensional valuation/genus structure. This is a coherent and
useful module. Nevertheless, it is obtained by the immediate alternating
recurrence, elementary valuations, a classical cubic doubling identity,
and classical curve theory. The nonlinear denominator equation is not
solved for all data; higher-genus rational points, all rational periods,
and a complete nonlinear rational atlas are not determined. My independent
recommendation is **COMPLETE_AUXILIARY**, not a substantial paper admission
on the frozen negative affine-atlas answer alone. Adding a correct classical
positive-genus corollary must not conceal that the original yes/no question
had an inherited elementary obstruction.

Primary-source browsing was bounded and used only public formulas and
identifiers, not manuscript uploads. The established elliptic curve is
indeed $43.a1$ with equation $y^2+y=x^3+x^2$ and discriminant $-43$;
database rank information was not used as proof. See
[LMFDB's original curve record](https://www.lmfdb.org/EllipticCurve/Q/43/a/1).
The discrete-sine cubic and local escape mechanism are source-owned;
the proved long-cycle theorem in the accessed version varies the degree
and its displayed Theorem 5.1 is restricted to $d\equiv1\pmod6$, with
shifted tables explicitly experimental. See
[Kim–Krieger–Postolache–Szeto, Sections 3–5](https://arxiv.org/html/2412.01668v2).
Ingram's affine normalization permits algebraic coefficients and supplies
the classical local-height context, not rational integral normalization
or a uniform all-coefficient cubic period bound. See
[Ingram, Section 2 and Lemma 2.2](https://arxiv.org/html/1111.3609).
The classical distinction between a given-point periodicity decision and
an all-points atlas is verified in
[Whang, Theorems 1.1–1.4 and Section 2.3](https://arxiv.org/html/2305.13529v3):
the finitely generated model ring used to decide a supplied rational point
may depend on that point. This is not a uniform all-denominator chart
construction. The characteristic-zero curve formula used by the C3
supplement is the ordinary
[Riemann–Hurwitz formula](https://stacks.math.columbia.edu/tag/0C1B).
The full unforced Markoff–Hurwitz automorphism group in
[Hu–Tan–Zhang's introduction](https://arxiv.org/html/1501.06955v2)
has a different scope from the forced ordered native return; no complete
proof audit of that paper is claimed here.
These accesses verify the named dependencies and boundaries, not exhaustive
worldwide novelty.

## Precise allowed claims and remaining gap

Allowed: C1's complete denominator lattice/refinement, input-dependent
finite graph, standard-form affine squareclass invariant, and regular
marked-fixed-point obstruction; C3's exact odd-dimensional two-period
equation and valuation stratification, explicit elliptic denominator tower,
finite labelled affine/rational-function chart obstruction at $(5,-1)$,
and the stated genus and fixed-level period-two bounds.

Not allowed: resolving C1-UB3; claiming C3 has classified all rational
periodic points or proved/refuted all-period decidability; calling the
bare rational-affine atlas obstruction a new discovery beyond C421/C427;
claiming the genus computation solves its rational-point equations;
claiming admission, worldwide priority, target Euler factors, root numbers,
automorphy, or a Hilbert–Pólya result.

C1 still needs a coefficient-independent restriction on primitive rational
cyclic words, or a rigorously unbounded-period family. C3 has no proof gap
in its frozen negative atlas answer; a broader nonlinear/all-period
classification is a different, unresolved question, not an omitted step
of that counterexample. The paper-level substantive gate remains separate
from both mathematical statuses.
