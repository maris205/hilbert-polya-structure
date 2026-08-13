# Literature Review: Critical One-Dimensional Maps, Hénon Lifts, and Arithmetic Orbit Claims

## Review status

- Date: 2026-08-12
- Scope: literature relevant to Stage 1 of the symplectic-map program.
- Selected family: \(H_{a,\rho}(x,y)=(1-a x^2-\rho y,x)\).
- Frozen parameter of interest: \(a=u_c=1.5436890126920763\).
- Central question: whether the only defensible arithmetic shadow inherited from the
  quadratic parent survives when \(\rho>0\), and especially at the symplectic endpoint
  \(\rho=1\).
- Evidence status: this document is a literature and novelty audit. It reports no new
  numerical result.

The bibliographic records below were collected during the initial audit. Links are
provided to DOI or arXiv records. Full-text claims should be checked again when the
manuscript bibliography is finalized.

## Executive conclusion

Three negative boundaries are already clear.

1. A critical one-dimensional map cannot be an everywhere regular smooth-submersion
   factor of a local diffeomorphism across the critical fiber. This is an elementary
   chain-rule/rank obstruction, not a new theorem.
2. Canonical two-dimensional extensions of noisy one-dimensional maps, including the
   Logistic map, have already been studied. Their singular behavior at \(f'=0\) is
   directly relevant prior art.
3. Periodic-orbit enumeration, symbolic dynamics, stability ledgers, and dynamical
   determinants for Hénon maps are mature topics. A generic Hénon ledger or zeta
   product is therefore not a novelty claim.

The remaining research gap is narrower and higher risk:

> With \(u_c\) fixed before examining symplectic-orbit multipliers or arithmetic
> labels, does the parent's weak mod-2 symbolic shadow remain observable along the
> conformally symplectic Hénon family, or does it become singular, branch-dependent,
> or disappear before \(\rho=1\)?

This is a controlled survival/failure question, not a claim that the Logistic map has
already generated the rational primes. The multiplier-to-prime Euler-product idea is
deferred until this entry question passes.

## 1. The exact geometric boundary

Let \(f:N\to N\) be a \(C^1\) map of a one-dimensional manifold, let
\(\pi:M\to N\) be a \(C^1\) submersion, and let \(F:M\to M\) be a local
diffeomorphism satisfying \(\pi\circ F=f\circ\pi\). Differentiation gives

\[
D\pi_{F(z)}DF_z=Df_{\pi(z)}D\pi_z.
\]

At a critical point of \(f\), the right side has rank zero, whereas the left side is
surjective. Thus the identity cannot hold over the critical fiber. In coordinates, a
triangular lift \(F(q,p)=(f(q),P(q,p))\) would require
\(\det DF=f'(q)P_p(q,p)\); it cannot have nonzero symplectic or conformally
symplectic determinant where \(f'(q)=0\) with finite \(P_p\).

This argument is elementary. Its value here is diagnostic: it forces any proposed
"Logistic-to-symplectic lift" to state which regularity, projection, branch, or memory
assumption it gives up. It does not rule out singular projections, canonical
relations, inverse limits, branch extensions, or topological realizations.

The general categorical background is compatible with this boundary. A smooth map
has a canonical cotangent relation, while an honest cotangent symplectomorphism is
available only under stronger invertibility assumptions; see Cattaneo, Dherin, and
Weinstein, [arXiv:0905.3574](https://arxiv.org/abs/0905.3574), and Weinstein's
[symplectic-categories article](https://doi.org/10.4171/PM/1866).

Inverse-limit and topological realizations occupy a different category and therefore
do not contradict the rank obstruction; relevant examples include the work of Barge
and Diamond ([DOI](https://doi.org/10.1017/S0143385799126622)) and Berger and Rovella
([DOI](https://doi.org/10.1016/j.anihpc.2012.10.001)).

## 2. The closest direct prior: canonical noisy-map extensions

Fogedby and Jensen constructed a two-dimensional area-preserving canonical map in a
weak-noise treatment of the Logistic map, with the noiseless dynamics recovered on a
special axis and with period-doubling, hyperbolic inherited cycles, elliptic off-axis
cycles, and KAM structure. This is the closest direct prior to the broad idea of
placing Logistic dynamics in a canonical planar setting:

- H. C. Fogedby and J. H. Jensen, "Weak noise approach to the logistic map,"
  *Journal of Statistical Physics* 121 (2005), 759--778,
  [arXiv:nlin/0411035](https://arxiv.org/abs/nlin/0411035),
  [DOI](https://doi.org/10.1007/s10955-005-5457-z).

Demaeyer and Gaspard studied the corresponding canonical weak-noise construction in
detail and explicitly analyzed focal/prefocal singularities and nonunique inverse
behavior where the parent derivative vanishes:

- J. Demaeyer and P. Gaspard, *Physical Review E* 80, 031147 (2009),
  [arXiv:0908.0465](https://arxiv.org/abs/0908.0465),
  [DOI](https://doi.org/10.1103/PhysRevE.80.031147).

Consequences for novelty are decisive:

- "A canonical extension of the Logistic map" is not a new contribution by itself.
- Singularity at \(f'=0\) is known behavior in the direct-prior construction.
- The present elementary rank lemma should be cited as a clean formulation of a known
  boundary, not promoted as a deep or unprecedented impossibility theorem.
- A contribution must instead come from the frozen-parameter survival experiment,
  a precise branch/completeness analysis, or a rigorously scoped negative result.

## 3. Conservative--dissipative Hénon homotopies are established

The family

\[
H_{a,\rho}(x,y)=(1-a x^2-\rho y,x)
\]

has \(\det DH=\rho\). It gives a useful matched comparison, but the existence of a
single family interpolating among one-dimensional, dissipative, and conservative
regimes is not itself novel.

- Heagy used a kicked-oscillator interpretation connecting conservative,
  dissipative, and Logistic limits, *Physica D* 57 (1992),
  [DOI](https://doi.org/10.1016/0167-2789(92)90012-C).
- Sterling and Meiss developed periodic-orbit computation through the anti-integrable
  limit across Hénon-type conservative and dissipative regimes, "Computing periodic
  orbits using the anti-integrable limit,"
  [arXiv:chao-dyn/9802014](https://arxiv.org/abs/chao-dyn/9802014),
  [DOI](https://doi.org/10.1016/S0375-9601(98)00094-2).
- Falcolini, Tedeschini-Lalli, and collaborators studied matched continuation between
  conservative and dissipative Hénon regimes,
  [DOI](https://doi.org/10.3934/dcds.2018263).
- Arai and Chen recently examined generalized parameter paths and hyperbolic
  quadratic limits, *Journal of Mathematical Physics* 66, 102706 (2025),
  [arXiv:2505.15346](https://arxiv.org/abs/2505.15346),
  [DOI](https://doi.org/10.1063/5.0280115).
- The older conservative/dissipative period-doubling crossover literature includes
  Bountis and collaborators, *Physica A* 137 (1986),
  [DOI](https://doi.org/10.1016/0378-4371(86)90062-2).

Reversibility must not be conflated with symplecticity. Reversible non-conservative
Hénon maps can exhibit structures unavailable to a purely dissipative description,
but their determinant need not equal one; see Gonchenko and collaborators,
[arXiv:2006.02542](https://arxiv.org/abs/2006.02542) and
[DOI](https://doi.org/10.3934/dcds.2020343).

For the present project, \(\rho\) is therefore a control coordinate rather than a
novel family. The potentially new object is the pre-registered response of a frozen
symbolic/arithmetic shadow to this control.

## 4. Hénon orbit ledgers and zeta constructions are mature

Several parts of the original proposal are technically useful but have low standalone
novelty.

- Sattari and Mitchell developed homotopic-lobe symbolic dynamics for an
  area-preserving Hénon map, enumerated all prime periodic orbits through substantial
  period cutoffs, computed monodromy information, and used periodic-orbit data in a
  Perron--Frobenius spectral determinant and escape-rate calculation,
  *Chaos* 27, 113104 (2017),
  [DOI](https://doi.org/10.1063/1.4998219).
- Gallas gave exact conjugacy-class/orbit-counting formulas for Hénon maps and located
  the full-horseshoe threshold near the strongly hyperbolic regime,
  *Physics Letters A* 360 (2007),
  [DOI](https://doi.org/10.1016/j.physleta.2006.08.065).
- Rugh's generalized Fredholm/Selberg-zeta framework already supplies the standard
  functional-analytic setting for Axiom-A maps,
  *Ergodic Theory and Dynamical Systems* 16 (1996),
  [DOI](https://doi.org/10.1017/S0143385700009111).
- Multiplier data can be rigid rather than arbitrary. A recent complex-Hénon result by
  Cantat and Dujardin makes this motivation explicit,
  [arXiv:2603.09445](https://arxiv.org/abs/2603.09445). This strengthens the case for
  recording a multiplier ledger, but does not make prime-valued multipliers natural.

Accordingly, the following are methods or calibration artifacts, not headline claims:

- enumerating low-period Hénon cycles;
- distinguishing primitive cycles from repetitions;
- computing monodromy eigenvalues and actions;
- forming a conventional hyperbolic dynamical zeta function;
- reproducing binary-necklace counts in an anti-integrable/full-horseshoe control.

The high-\(a\) Hénon calculation remains important as a positive control for the orbit
finder and completeness logic. It cannot establish arithmetic relevance at the frozen
\(u_c\) parameter.

## 5. Logistic-to-Hénon inheritance is broad prior art, but the exact lock is not settled

Rank-one and small-Jacobian Hénon theory has long used one-dimensional maps,
including Misiurewicz-type quadratic dynamics, as singular limits. The audit located
the classical Benedicks--Carleson and Mora--Viana lineage and later Wang--Young and
Ott--Wang developments. These works make a generic claim of "lifting Logistic chaos
to Hénon chaos" untenable as a novelty statement.

They do not, from the literature located in this audit, answer the narrower question
posed here: whether a *specific parameter fixed by the earlier project* carries a
specific, predeclared mod-2 symbolic statistic through the entire path to
\(\rho=1\), with branch identity and censoring controlled. That is the remaining gap.

This gap may have a negative answer. Because \(\rho=0\) is a singular endpoint rather
than an ordinary diffeomorphic member, immediate branch loss or nonunique continuation
would itself be informative.

## 6. Arithmetic dynamics sets a much higher bar than generic prime-orbit asymptotics

The dynamical "prime orbit theorem" counts primitive periodic orbits; it does not
identify those orbits with rational primes. Existing arithmetic-dynamics programs
make the additional structure explicit.

- Deninger's arithmetic-dynamical program organizes closed points/orbit packets with
  lengths related to logarithms of arithmetic norms,
  [arXiv:1807.06400](https://arxiv.org/abs/1807.06400), with a later formal account in
  *Indagationes Mathematicae* (2024),
  [DOI](https://doi.org/10.1016/j.indag.2024.05.007).
- Connes and Consani construct prime-labelled periodic-orbit structures in the scaling
  site/adelic setting; see [arXiv:2401.08401](https://arxiv.org/abs/2401.08401) and
  [arXiv:2501.06560](https://arxiv.org/abs/2501.06560).
- Berry and Keating emphasize that a Riemann trace interpretation would require
  classical periods tied to \(\log p\), rather than merely chaotic level statistics,
  *SIAM Review* 41 (1999),
  [DOI](https://doi.org/10.1137/S0036144598347497).
- Models that insert primes directly, such as Sierra's prime-mirror construction,
  illustrate a different design class and cannot validate an intrinsic Hénon
  mechanism; see [arXiv:1404.4252](https://arxiv.org/abs/1404.4252).

The project must therefore separate three statements:

1. Hyperbolic systems have primitive periodic orbits. This is generic dynamics.
2. A conventional Euler product can be written from orbit weights. This is standard
   formalism, subject to convergence and completeness.
3. Primitive Hénon multipliers intrinsically encode rational primes with correct
   multiplicity and repetitions. This is the unproved arithmetic hypothesis.

Only the third statement would cross the Route-A arithmetic gate, and it is currently
deferred.

The title "arithmetical signatures" is also occupied in the Hénon literature; see
Endler and Gallas, *Physical Review E* 65, 036231 (2002),
[DOI](https://doi.org/10.1103/PhysRevE.65.036231). Broad title-level claims about
"arithmetic signatures in Hénon maps" should be avoided.

## 7. Cat maps and quantization are controls, not rescue routes

Cat maps provide exact symplectic and quantum-map baselines. Their arithmetic over
finite rings and their quantum spectral statistics are well developed, beginning with
Hannay and Berry, [DOI](https://doi.org/10.1016/0167-2789(80)90026-3), and the later
Kurlberg--Rudnick program.

A recent discrete-cat-map paper obtains exact arithmetic orbit-zeta/Green-function
structure over finite rings using CRT and Pisano-type periods:

- Chandra, "Arithmetic Landscape Functions of a Discrete Cat Map,"
  [arXiv:2607.24857](https://arxiv.org/abs/2607.24857).

This is genuine arithmetic structure, but it is not a rational-prime Euler
correspondence of the type demanded here. It is a valuable "right arithmetic, wrong
target" control.

There is also an elementary exact negative control at the linear level. If
\(A\in SL(2,\mathbb Z)\) is hyperbolic and its unstable eigenvalue were a rational
prime \(p\), then the integer trace would equal \(p+p^{-1}\), which is not an integer.
Thus a two-dimensional integer cat map cannot realize a rational prime as its unstable
multiplier. Cat-map quantization should not be used to rescue a failed Hénon A0 gate.

## 8. Higher dimension is intentionally postponed

Coupled and higher-dimensional symplectic Hénon constructions are already active
research areas. For example, Fujioka and collaborators study hyperbolicity in coupled
four-dimensional Hénon maps, *Physica D* 481 (2025),
[arXiv:2303.05769](https://arxiv.org/abs/2303.05769),
[DOI](https://doi.org/10.1016/j.physd.2025.134722).

Adding dimensions before the two-dimensional A0 question is resolved would add orbit
complexity without a defined arithmetic mechanism. It is recorded as a later clue,
not a current work package.

## 9. Novelty map

| Candidate contribution | Prior-art saturation | Current novelty assessment |
|---|---:|---|
| Smooth critical-map lift obstruction | High | Elementary boundary; cite, do not headline as a new theorem |
| Logistic canonical/noisy symplectic extension | High | Directly covered by Fogedby--Jensen and Demaeyer--Gaspard |
| Conservative/dissipative Hénon homotopy | High | Useful experimental control, not new family |
| Generic Hénon UPO ledger | High | Calibration/reproducibility contribution only |
| Generic Hénon zeta or Fredholm determinant | High | Low novelty without new arithmetic source |
| Frozen \(u_c\) mod-2-shadow survival to \(\rho=1\) | Not located directly | Selected, high-risk, falsifiable gap |
| Exact prime-valued multiplier correspondence | Not established | High-impact if intrinsic, but currently unsupported and deferred |
| Hénon quantization toward Riemann zeros | Unsupported | Stop-scoped until A0 and A1 pass |

## 10. Resulting research position

The defensible Stage-1 paper is a nonlinear-dynamics and methodology paper with a
sharp negative/diagnostic possibility:

1. state the regular-lift obstruction with correct historical scope;
2. use \(H_{a,\rho}\) as a matched conformally symplectic family;
3. freeze \(u_c\) and one symbolic transport statistic before confirmatory data;
4. validate orbit-finding logic in a high-\(a\) anti-integrable control;
5. report branch loss, exposure loss, or parity-shadow loss without attempting a
   Riemann-zeta or quantum rescue;
6. open the multiplier-prime Euler product only if the arithmetic-shadow gate passes
   under controls.

This positioning is deliberately narrower than the original proposal. It is also more
scientifically identifiable: a clean failure discriminates between geometric richness
and arithmetic inheritance rather than treating generic Hamiltonian chaos as evidence
for primes.
