# Source and duplication audit

> Priority note (2026-08-05): source conclusions remain relevant; former
> N+1/N+2 scheduling conclusions are superseded by the breadth-first search.

Date: 2026-08-05

This audit controls what the next paper may inherit from
`docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`.
When the legacy README, manuscript language, stored code, and later audit
disagree, the code-level audit is treated as authoritative evidence about what
was actually computed.

## Executive verdict

Paper 5 correctly selects an exact, reversible, area-preserving Hénon family as
a potentially relevant classical system. Its later spectral construction is
not a quantization determined by that map. Future work should preserve the map
and replace the spectral surrogate, not tune the surrogate further.

The strongest immediate negative result is analytic: a one-dimensional
quartic confining Hamiltonian has counting exponent \(3/4\), not the
Riemann--von Mangoldt \(T\log T\) law. The strongest immediate constructive
route is the certified Ruelle-operator limit for the already validated local
\(H_6\) instability suspension. A later quantum route may use one known
natural Hénon quantization and connect its localized traces to the certified
periodic orbits only after its novelty, gauge, cutoff, and trace-class gates
pass.

## Exact checks on the classical baseline

### Area preservation and reversibility

For

\[
H_a(q,p)=(1-aq^2-p,q),
\qquad
DH_a(q,p)=\begin{pmatrix}-2aq&-1\\1&0\end{pmatrix},
\]

one has \(\det DH_a=1\). The coordinate-swap involution
\(R(q,p)=(p,q)\) satisfies \(RH_aR=H_a^{-1}\).

These are exact structural facts. They do not, by themselves, specify a
Hilbert space, a quantum operator, a domain, a discrete spectrum, or an
arithmetic trace identity.

### Exact match to the standard parameter convention

For \(a\ne0\), the linear conjugacy

\[
C_a(q,p)=(-aq,ap)
\]

gives

\[
C_aH_aC_a^{-1}(X,Y)=(X^2+Y-a,-X).
\]

Thus the parameter in Paper 5 is the same \(k=a\) used by
Sterling--Dullin--Meiss for the conservative \(b=1\) family. Their homoclinic
bifurcation and horseshoe-closing computations are mandatory prior work.

Since \(\det C_a=-a^2\), this is a classical conjugacy, not a
symplectic/metaplectic equivalence. It cannot be used to transfer a quantum
spectrum between conventions without a separate operator construction.

### An exact obstruction to “only a chaotic saddle remains” at \(a=1.02\)

The positive fixed point is

\[
q_+(a)=\frac{\sqrt{1+a}-1}{a},
\]

and

\[
\operatorname{tr}DH_a(q_+,q_+)
=2(1-\sqrt{1+a}).
\]

It is linearly elliptic for \(-1<a<3\). In particular, at \(a=1.02\) its trace
is approximately \(-0.842\), strictly between \(-2\) and \(2\). Therefore the
claim that only a chaotic saddle remains is false. Linear ellipticity alone is
not asserted here to prove surviving KAM curves or to rule out the breakup of
a particular global transport barrier; those stronger statements require
nonresonance/twist analysis.

## Claim-by-claim legacy audit

| Legacy item | Evidence status | Decision for next paper |
|---|---|---|
| \(H_a(q,p)=(1-aq^2-p,q)\), \(\det DH_a=1\) | Exact | Retain |
| Reversibility | Exact | Retain, and test the induced antiunitary symmetry of any quantization |
| LL/same-side statistic vanishes near \(1.02\) | Finite-sample, seed/box/transient dependent; not a topological invariant | Do not use as a parameter-selection principle |
| “First homoclinic tangency” near \(1.00561\) | Notebook minimizes sampled distance to \(y=x\); it does not solve the tangency derivative, quadratic nondegeneracy, generic unfolding, or firstness conditions | Treat as unproved; reproduce only as a legacy negative control |
| \(\Delta W=35.5499(a-a_c)^{3/2}\) | Coefficient stored, not derived | Retire unless independently derived from a normal form |
| Match \(\Delta W\) to \(\hbar_{\rm eff}\) | \(\hbar_{\rm eff}\) fitted to target zeros | Not an independent prediction; retire |
| Cubic continuum potential | A formal second-difference approximation, not the exact discrete action | Historical motivation only |
| Added \(0.05q^4\) term | Chosen confinement; changes the operator and its asymptotic counting law | Subject of the Weyl no-go theorem, not inherited physics |
| Static/logarithmic \(a(t)\) schedules | Modeling/fitted choices, no canonical skew product or cocycle | Exclude from this autonomous paper |
| Best 100-zero quantum MAPE \(2.3\%\) | Stored run optimized against all 100 targets, then anchored; sharp and grid/regularization sensitive | Not blind validation; no reuse as evidence |
| Robust 10--20% fits | Require retuning \(\hbar\); do not identify a natural operator | No reuse |
| Markov/Fokker--Planck spectrum | One evolving occupancy rather than source-row assembly; escape reset; incorrect CSR normalization; target anchoring | Invalid as a standard Ulam operator; exclude |
| Floquet GUE-like phases | Generic diagnostic; different spectral object from unwrapped fitted energies | Not a main claim |
| Phase-to-energy reconstruction | Branch selected using a base-Hamiltonian expectation, thereby relabeling levels | Exclude |
| Hardware downturn analogy | Qualitative and mechanistically unmatched | Exclude |

## The homoclinic-value issue

The original notebook's small distance to the symmetry line is not a tangency
certificate. A proper tangency experiment must solve, for a parameterized
unstable manifold and symmetry-line function \(g\),

\[
g(a,t)=0,\qquad \partial_tg(a,t)=0,
\]

and separate both \(\partial_t^2g\) and \(\partial_ag\) from zero. It must also
establish which symbolic branch is being continued and, if “first” is claimed,
exclude all earlier competitors.

The standard conservative literature locates the complete-horseshoe closing
branch near \(a\simeq5.699310787\), not \(1.0056\). The present paper will not
attempt to re-prove that global threshold. If a full certification is later
pursued, it belongs in a separate computer-assisted dynamics paper.

## Existing repository work that must not be duplicated

### `docs/related_programs/henon_weighted_zeta`

Already completed:

- a code-level audit of Paper 5;
- parameter continuation from the mixed low-\(a\) regime toward \(a=6\);
- a certified four-state local survivor at \(a=6\);
- exact covering relations, cone bounds, and symbolic conjugacy;
- a local periodic-orbit catalogue and finite cycle/operator experiments.

Open seams:

- the continuous Ruelle-operator/finite-memory limit is a certified fallback
  seam;
- a specified quantum map and controlled classical--quantum trace bridge is
  HCS-C09 in the breadth-first pool.

### `henon_instability_roof_zeta`

Already completed:

- a positive Hölder instability roof
  \(T_p=\log|\Lambda_{u,p}|\) on the certified local survivor;
- a non-lattice proof;
- 2,170 primitive local cycles through period 20;
- negative results for unit clock and action as positive suspension roofs;
- finite-section root studies with an A3 convergence failure.

The 2,170 cycles are complete only for the local four-state survivor
\(\Lambda_*\). Its unweighted determinant is \(1-z-z^3-z^4\); it must never be
described as the full binary Hénon horseshoe with determinant \(1-2z\).

New use permitted in this paper:

- use \(T_p\) in the exact stability amplitude of the quantum trace;
- use the local orbit coordinates to evaluate discrete actions and Maslov
  data;
- do not reinterpret \(T_p\) or \(S_p\) as candidate zero ordinates.

## Prior work that changes the novelty claim

Tabor's area-preserving-map trace framework predates this project. Fornæss and
Weickert constructed a unitary quantized Hénon map on
\(L^2(\mathbb R)\) in 2000, and Weickert later studied its spectral type,
including a purely continuous-spectrum regime. Earlier numerical quantization
and later horseshoe-regime WKB/Stokes analyses also exist. Consequently:

- “we discover/canonically quantize the Hénon map” is not a novel claim;
- rederiving the generating function in the present coordinates is necessary
  for correctness but is not the paper's contribution;
- novelty must come from the Paper-5 Weyl obstruction, localization to the
  certified survivor, the explicit action/stability/Maslov orbit formula, and
  a controlled determinant or trace computation.

Standard semiclassical trace formulas and open-quantum-map theory are also
prior art. The project therefore needs at least one of:

1. an explicit, rigorous remainder uniform over a useful period range;
2. a computer-assisted trace bound using the certified orbit geometry;
3. a fixed-contour determinant comparison with a certified error;
4. a precise microlocal cutoff-independence result for the reported trace
   coefficients.

A collection of finite matrix eigenvalue plots is not sufficient.

The hard G0 source set now includes Helleman (1988), Fornæss--Weickert (2000),
Weickert (2004), Shudo--Ikeda (2008), and Shudo--Ikeda (2016). Unless a full
comparison shows that certified localized **traces with explicit error/contour
bounds** are absent, this quantum route is too close to prior art for the next
paper.

## Duplication firewall

The new paper must not be built around:

- another low-resolution scan near \(1.0056\) or \(1.02\);
- more Riemann-zero optimization or a larger zero table;
- another finite Ulam grid without a continuous-operator theorem;
- a longer cycle catalogue without a new analytic bound;
- GUE spacing alone;
- non-autonomous schedules replaced by averaged transition matrices;
- the assertion that area preservation alone supplies a Hilbert--Pólya
  operator.

## Source ledger

Internal controlling sources:

- `../docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`
- `../docs/prior_work/legacy/5-riemann_henon/paper/manuscript.tex`
- `../docs/related_programs/henon_weighted_zeta/research/LEGACY_HENON_AUDIT.md`
- `../docs/related_programs/henon_weighted_zeta/R058_COVERING_PROOF.md`
- `../docs/related_programs/henon_weighted_zeta/research/refine-logs/R059_SYMBOLIC_CONTRACTION_PROOF.md`
- `../henon_instability_roof_zeta/README.md`

External primary sources:

- Hénon (1969), *Numerical study of quadratic area-preserving mappings*.
- Tabor (1983), semiclassical quantization of area-preserving maps,
  <https://doi.org/10.1016/0167-2789(83)90005-2>.
- Sterling, Dullin, and Meiss (1999),
  <https://arxiv.org/abs/chao-dyn/9904019>.
- Fornæss and Weickert (2000),
  <https://doi.org/10.3934/dcds.2000.6.723>.
- Weickert (2004),
  <https://doi.org/10.1090/S0002-9947-04-03475-0>.
- Helleman (1988),
  <https://doi.org/10.1016/S0167-2789(98)90014-8>.
- Shudo and Ikeda (2008),
  <https://doi.org/10.1088/0951-7715/21/8/007>.
- Shudo and Ikeda (2016),
  <https://doi.org/10.1088/0951-7715/29/2/375>.
- Wilczak and Zgliczyński (2009), computer-assisted homoclinic-tangency
  methodology, <https://arxiv.org/abs/0905.3924>.
- Faure (2007), semiclassical map trace formula,
  <https://eudml.org/doc/10305>.
- Nonnenmacher, Sjöstrand, and Zworski (2011), open quantum maps,
  <https://arxiv.org/abs/1105.3128>.
