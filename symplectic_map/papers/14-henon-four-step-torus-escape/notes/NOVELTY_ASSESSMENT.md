# Novelty Assessment

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_INDEPENDENT_REVIEW / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

## Proposed result

For

\[
H(x,y)=(b x^d+a y+c,x)
\]

over an arbitrary characteristic-zero field, and an arbitrary finite-rank
subgroup \(\Gamma\le K^\ast\), the proposal gives an explicit uniform bound
for the four-step survival set \(T_4(H,\Gamma)\), proves that three-step
survival may be infinite already in rank one, and derives a weighted bound
for periodic orbits wholly contained in \(\Gamma^2\).

## Conservative verdict

**GO to independent source review.**

The novelty is concentrated in the combined statement:

1. coefficient-free uniformity in \(a,b,c,K\);
2. an explicit \(d,r\)-only bound for all initial states surviving through
   four forward iterates;
3. a complete degeneracy automaton with a sharp four-versus-three threshold;
4. a rank-one construction showing \(T_3\) can be infinite;
5. the orbit-contained weighted periodic corollary.

The proof method itself is only moderately novel. Its nondegenerate input is
the classical Evertse--Schlickewei--Schmidt theorem. The residual mathematical
work is the exact fixed-coefficient reduction, the nine-transition table,
closure of the \(BA\) and \(CB\) free chains, and the sharp example.

## Two independent source-stage assessments

The two proof-first audits were performed independently and are preserved
separately; they are not averaged and do not constitute cross-model
validation.

### Independent assessment A

- result novelty: **7.0/10**
- standalone size: **6.0--6.5/10**
- proof confidence after formal repairs: **9.5/10**
- disposition: **GO after minor formal repair**
- principal repair: promote \(T_4\) finite and \(T_3\) infinite to the
  headline; define full-orbit containment in the periodic corollary.

### Independent assessment B

- result novelty: **7.0/10**
- standalone size: **6.0--6.3/10**
- proof confidence: **9.7/10**
- disposition: **GO with source-package corrections**
- principal repair: use the full \(b x^d\) family and fixed ESS coefficients,
  thereby removing all coefficient-membership assumptions without changing
  the rank \(3r\).

## Core-claim novelty map

| Component | Novelty level | Closest source boundary | Residual delta |
|---|---:|---|---|
| Explicit nondegenerate count | low | Evertse--Schlickewei--Schmidt | dynamical local-state pullback and the factor \(d\) |
| Four-step finite survival | medium-high | general \(S\)-unit and group-intersection dynamics | an unconditional initial-state bound over arbitrary characteristic-zero fields |
| Full \(b\)-version without coefficient membership | medium | ESS with fixed coefficients | recognition that rank remains \(3r\), uniformly in \(a,b,c\) |
| Degenerate-word closure | medium-high | no direct collision located | complete \(A/B/C\) automaton and \(BA/CB\) free-chain closure |
| Rank-one infinite \(T_3\) | high as part of threshold | no direct collision located | sharp failure of the immediately shorter window |
| Weighted periodic corollary | medium-low alone | arithmetic Hénon periodic-point literature | follows from the stronger survival theorem and exact orbit-containment semantics |

## Closest prior work and collision strength

### Direct arithmetic input

Evertse, Schlickewei, and Schmidt prove the finite-rank multiplicative-group
linear-equation bound used in the proof. This is a direct method input, not a
collision with the Hénon survival theorem.

### One-dimensional \(S\)-unit dynamics

Krieger--Levin--Scherr--Tucker--Yasufuku--Zieve study uniform boundedness of
\(S\)-units in images of one-variable rational functions. Canci and
coauthors obtain explicit periodic or preperiodic bounds for rational maps on
\(\mathbb P^1\) in terms of good or bad reduction data. These works are
adjacent in arithmetic technique but do not treat all initial states of a
two-dimensional Hénon recurrence in a finite-rank torus.

### Finitely generated groups and orbit intersections

Ostafe--Sha--Shparlinski--Zannier and
Bérczes--Ostafe--Shparlinski--Silverman treat multiplicative dependence of
univariate iterated values. Bell--Chen--Hossain Theorem 1.1 treats a fixed
orbit through one rational observable, while Bell--Ghioca Theorem 1.1 treats
return times of one fixed orbit of a rational self-map of a semiabelian
variety to a finitely generated subgroup. Both are qualitative return-time
structure results; neither bounds all initial states surviving a prescribed
four-transition Hénon window, and neither yields a rank-only cardinality
bound.

### Higher-dimensional integrality and Hénon results

Grieve--Noytaptim Theorem 1.2 and Corollary 1.5 prove non-Zariski-density
results for integral points in fixed forward orbits under projective divisor
hypotheses. Noytaptim--Zhong Theorem 1.2 treats a common-iterate locus for
compositionally independent Hénon-type maps. Mello--Yasufuku Theorems
1.1--1.2 and Corollary 1.3 treat projective endomorphism semigroups over
number fields and finitely generated subgroups conditional on
\(\mathrm{Hyp}_\epsilon\), with \(\epsilon\ge(1+c)/2\). Their Theorem 4.2,
under additional divisor hypotheses and Vojta's Main Conjecture, reaches
only sufficiently small \(\epsilon\) and therefore does not establish the
general main hypothesis. None supplies the present unconditional
four-transition cardinality bound.

Ji--Xie--Zhang Theorem 1.8 and Corollary 1.9 prove that periodic points over
a maximal cyclotomic extension for Hénon-type automorphisms are not Zariski
dense. Their conclusion is not finiteness and their set is not an arbitrary
fixed finite-rank subgroup.

Kim--Krieger--Postolache--Szeto Theorem A constructs, for every odd \(d>2\),
a rational polynomial \(s_d\) of degree at most \(d\) such that
\(h_d(x,y)=(y,-x+s_d(y))\) has at least \((d-4)^2\) rational periodic
points; Theorem B gives, for \(d\equiv1\pmod6\), an integer cycle of length
\((8d+10)/3\). After a coordinate swap this is still a general-polynomial
Hénon family, not the present monomial-plus-constant family. These are
degree-dependent lower bounds, not fixed-rank \(T_4\) finiteness or the
rank-one \(T_3\) sharpness construction.

The residual novelty axes are consequently precise: all initial states, a
fixed four-transition window, an explicit rank-and-degree-only cardinality,
finite-rank rather than finitely generated groups, and the exact \(T_4/T_3\)
threshold.

## Novelty statement permitted after review

The strongest currently safe positioning is:

> A targeted primary-source search through 2026-08-16 located no theorem
> combining this three-coefficient Hénon family, arbitrary finite-rank
> multiplicative groups, a coefficient-uniform four-transition cardinality
> bound, and a rank-one sharp three-transition failure.

This is a search report, not an absolute global-priority claim.

## Standalone-size assessment

A periodic-point-only note would be too thin. The source package becomes a
credible focused short paper only if it keeps the following order:

1. \(T_4\) as the main theorem;
2. the coefficient-free fixed-ESS formulation;
3. the complete degeneracy automaton;
4. the sharp rank-one \(T_3\) family;
5. the weighted periodic-orbit corollary;
6. exact literature and nonclaim boundaries.

Optional \(T_2/T_3\) strata may be considered only after separate proof and
review. They are not needed to support the current theorem.

## Risks

- A referee may view the ESS application as classical and ask whether the
  degeneracy automaton alone provides enough depth.
- The ESS constant is enormous and is not presented as practical.
- The \(81d^2\) bound is a union bound, not an optimized count.
- Recent higher-dimensional multiplicative-dependence literature makes
  precise boundary writing essential.
- The two source-stage audits may share correlated blind spots; a new
  independent reviewer remains mandatory.

## Paper 15 reserve

The quartic sharp-cutoff candidate remains reserved for Paper 15. It is not a
supporting theorem, comparison experiment, or extension of Paper 14. Its
score and proof package must remain independent.

## Nonclaims

No novelty credit or theorem scope is claimed for:

- the ESS theorem itself;
- \(S\)-unit equations as a method;
- general Hénon arithmetic;
- all rational or integral periodic points;
- one-point intersections \(\operatorname{Per}(H)\cap\Gamma^2\);
- arbitrary polynomial \(p(x)\);
- positive characteristic or \(d=1\);
- optimal constants;
- algorithms, height bounds, or effective listings;
- a complete \(T_2/T_3\) classification;
- numerical evidence or parameter scans;
- the Paper 15 quartic reserve.
