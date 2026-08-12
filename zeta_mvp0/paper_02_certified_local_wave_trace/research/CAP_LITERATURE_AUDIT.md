# Computer-Assisted Proof Literature Audit

**Scope:** Paper 02's parameterized Krawczyk certificates, validated
\(C^1\) ODE integration, periodic-orbit continuation, and arithmetic/
reproducibility protocol.  
**Audit date:** 2026-08-06.  
**Evidence policy:** original articles and books, publisher or institutional
records, and the official CAPD repository are preferred.  This is a
source-and-claim audit, not an independent rerun of the certificates.

## Bottom line

The literature supports the individual numerical-analysis ingredients used
by A4.12 and A4.13, but it does not certify this project's implementation or
promote its local-box result to global uniqueness.

1. Under the cited theorem's regularity hypotheses and the separately
   verified uniqueness/contraction condition, a strict Krawczyk inclusion
   built from valid enclosures of the complete residual and its Jacobian is
   an appropriate existence-and-local-uniqueness certificate.  Its
   conclusion is local to the stated root box.
2. The \(C^1\)-Lohner literature and the CAPD::DynSys paper support rigorous
   simultaneous enclosures of a flow and its first variational equations.
   State-only \(C^0\) integration would not supply the derivative and
   monodromy data required by this certificate.
3. There is direct prior art for combining validated flows/Poincaré maps
   with parameter-uniform interval Newton tests to continue locally unique
   periodic-orbit branches.  The method class must not be presented as
   novel.
4. The project's guarded bridge boxes, full-return recovery, primitive-
   period argument, quotient determinant identity, and complement boundary
   are separate proof layers.  They are not consequences of citing CAPD,
   Lohner, or Krawczyk.
5. IEEE arithmetic standards, MPFR, and reproducible-research guidance
   support directed/correct rounding and artifact disclosure.  No located
   primary or normative source mandates the project's precise protocol of
   printing decimal interval endpoints, parsing them as exact rationals,
   and independently replaying the inequalities.  That is a defensible,
   project-specific proof-object design, not a standard compliance claim.

The software provenance should be described exactly as **CAPD pinned at
commit `731079217a9254ea2948d742df2b170895effe7f`, whose
`CAPDVersion.txt` reports 6.1.0**.  The official repository does not expose a
`v6.1.0` tag or release; its release list currently stops at `v6.0.0`.
Therefore “the CAPD 6.1.0 release” is not supported wording.

## Project method being audited

A4.12 encodes a four-variable return system \(F(x,\epsilon)=0\), encloses
the residual and \(D_xF\) over parameter slabs, and applies a parameterized
Krawczyk operator.  Fifty-one primary slabs and fifty guarded bridge hulls
cover \(\epsilon\in[0,0.101]\); all 101 jobs are run at both 128- and
256-bit MPFR precision.  Strict inclusion and a contraction gate give one
root in the displayed \(x\)-box for each fixed \(\epsilon\) in its slab.
The bridge certificates identify adjacent local roots as one connected
branch.  Energy conservation and a positive phase slope recover the omitted
full-return coordinate; a separate argument establishes primitivity.

The accepted CAPD jobs also propagate the first variational equations and
enclose the monodromy matrix.  A4.13 consumes those enclosures and combines
them with an analytic invariant-quotient identity; its determinant
conclusion is therefore not produced by CAPD alone.  The independent
checkers reconstruct the printed decimal endpoints as exact rational
numbers and replay the finite-dimensional Krawczyk and determinant
inequalities.  They do **not** independently integrate the ODE or regenerate
CAPD's flow/variational enclosures.

This division of labor should remain explicit in the manuscript:

| Proof layer | Literature supports | Project must establish |
|---|---|---|
| Flow enclosure | Validated IVP algorithms enclose all solutions from an input set over the integration interval | Correct vector field, parameter embedding, initial set, time range, build, and successful run |
| First variations | \(C^1\)-Lohner methods enclose derivatives with respect to initial data | Correct variational equations and extraction of the shooting Jacobian/monodromy |
| Local shooting root | Krawczyk/interval Newton gives existence and uniqueness in a stated box under its hypotheses | Complete residual, valid interval Jacobian, nonsingular preconditioner, and strict inclusion for every slab |
| Connected branch | Parameter-uniform local roots can form a validated branch | Overlap or guarded bridge logic identifying neighboring roots; analytic regularity if claimed |
| Periodic orbit | A root of a correctly gauge-fixed return system can encode a periodic orbit | Full-state recovery, section/transversality conditions, and exclusion of a shorter return |
| Stability gap | Validated monodromy data can feed a rigorous stability calculation | The quotient identity, directed endpoint calculation, and exact meaning of the Poincaré derivative |
| Global uniqueness | Exhaustive interval search can exclude all other roots on a declared domain | A complete complement/global cover; local boxes alone do not do this |
| Independent replay | Exact arithmetic can audit finite inequalities derived from stored endpoints | Provenance of those endpoints and a clear statement that the checker does not rerun the validated integrator |

## Interval Newton and Krawczyk methods

### Krawczyk (1969)

R. Krawczyk, “Newton-Algorithmen zur Bestimmung von Nullstellen mit
Fehlerschranken,” *Computing* **4**, 187–201 (1969).
[DOI](https://doi.org/10.1007/BF02234767) ·
[publisher record](https://link.springer.com/article/10.1007/BF02234767).

**Supports:** the foundational Krawczyk construction within interval Newton
methods for verified zeros with error bounds, including systems of
equations.

**Does not support:** any residual or Jacobian enclosure in this repository;
parameter continuation, bridge gluing, primitivity, or global uniqueness
without the additional hypotheses and proof layers actually checked here.

### Moore, Kearfott, and Cloud (2009)

R. E. Moore, R. B. Kearfott, and M. J. Cloud, *Introduction to Interval
Analysis*, Society for Industrial and Applied Mathematics, Philadelphia,
2009. ISBN 978-0-89871-669-6.
[DOI](https://doi.org/10.1137/1.9780898717716) ·
[publisher record](https://epubs.siam.org/doi/book/10.1137/1.9780898717716).

**Supports:** a modern statement of interval Newton/Krawczyk existence and
uniqueness tests, interval extensions, and outward/directed enclosures.
For the paper, this is the clean reference for the theorem instantiated by
each frozen Krawczyk record.

**Does not support:** treating a point Jacobian or midpoint energy gradient
as an enclosure over the whole root box.  The invalidated predecessor of
A4.12 is a useful internal example of why this hypothesis matters.

### Neumaier (1990)

A. Neumaier, *Interval Methods for Systems of Equations*, Encyclopedia of
Mathematics and its Applications 37, Cambridge University Press, Cambridge,
1990.
[DOI](https://doi.org/10.1017/CBO9780511526473) ·
[publisher record](https://www.cambridge.org/core/books/interval-methods-for-systems-of-equations/1BC3BDF16A2F4EC44EAFAD75051733DA).

**Supports:** precise enclosure, exclusion, existence, uniqueness, and
regularity formulations for interval Newton and Krawczyk operators.  It is
the safest detailed source for matching the manuscript's hypotheses to the
exact theorem variant used.

**Does not support:** historical priority for the Krawczyk operator or any
claim beyond the finite-dimensional system and box to which the theorem is
correctly applied.

### Kearfott (1996)

R. B. Kearfott, *Rigorous Global Search: Continuous Problems*, Kluwer
Academic Publishers, Dordrecht, 1996.
[DOI](https://doi.org/10.1007/978-1-4757-2495-0) ·
[publisher record](https://link.springer.com/book/10.1007/978-1-4757-2495-0).

**Supports:** exhaustive subdivision/branch-and-bound methods for global
root search and all-roots claims over a specified domain.

**Project boundary:** this source makes the local/global distinction sharp.
Strict inclusion proves one root in a certified box; a global uniqueness
claim requires a complete domain and a validated exclusion or accounting of
its complement.  A4.12 explicitly does not provide that complement proof.

### Rump (2010)

S. M. Rump, “Verification methods: Rigorous results using floating-point
arithmetic,” *Acta Numerica* **19**, 287–449 (2010).
[DOI](https://doi.org/10.1017/S096249291000005X) ·
[publisher record](https://www.cambridge.org/core/journals/acta-numerica/article/verification-methods-rigorous-results-using-floatingpoint-arithmetic/770FE58E5293985CCAB770AF09C4F3FF).

**Supports:** the broader discipline of producing rigorous numerical
conclusions with floating-point arithmetic, including verified linear and
nonlinear computations and careful rounding.

**Does not support:** the validity of arbitrary printed decimal intervals or
the project-specific exact-rational replay protocol.  Those endpoints must
first be shown to be outward enclosures of the quantities claimed.

## Validated ODE integration and first variations

### Lohner (1987)

R. J. Lohner, “Enclosing the Solutions of Ordinary Initial and Boundary
Value Problems,” in E. W. Kaucher, U. W. Kulisch, and C. Ullrich, eds.,
*Computerarithmetic: Scientific Computation and Programming Languages*,
B. G. Teubner, Stuttgart, 1987.
[stable catalog record](https://cir.nii.ac.jp/crid/1572261550533637504).

**Supports:** the foundational validated-enclosure and wrapping-control
lineage conventionally called Lohner's method.

**Metadata note:** no DOI or publisher-hosted chapter page was located.  The
linked catalog directly confirms the chapter title, author, containing book,
and year.  Pagination and ISBN are omitted here because that record does not
display them.  Accordingly, the DOI-backed \(C^1\) article below should be
the principal algorithmic citation.

### Zgliczyński (2002)

P. Zgliczyński, “\(C^1\)-Lohner algorithm,” *Foundations of Computational
Mathematics* **2**(4), 429–465 (2002).
[DOI](https://doi.org/10.1007/s102080010025) ·
[publisher record](https://link.springer.com/article/10.1007/s102080010025) ·
[author manuscript](https://ww2.ii.uj.edu.pl/~zgliczyn/papers/ks/c1lohner.pdf).

**Supports:** rigorous joint enclosure of an ODE flow and derivatives with
respect to initial conditions, wrapping control for the first variational
equations, and applications to derivatives of Poincaré maps and periodic
orbits.

**Does not support:** identifying every modern CAPD class with the exact
2002 implementation, or concluding existence/uniqueness of a shooting root
from a flow enclosure alone.  The Krawczyk step remains indispensable.

### Nedialkov, Jackson, and Corliss (1999)

N. S. Nedialkov, K. R. Jackson, and G. F. Corliss, “Validated solutions of
initial value problems for ordinary differential equations,” *Applied
Mathematics and Computation* **105**(1), 21–68 (1999).
[DOI](https://doi.org/10.1016/S0096-3003%2898%2910083-8) ·
[publisher record](https://www.sciencedirect.com/science/article/pii/S0096300398100838).

**Supports:** the general meaning and structure of successful validated IVP
computations: existence of the IVP solution over the requested interval and
a guaranteed enclosure of it.

**Does not support:** CAPD specifically.  IVP uniqueness is uniqueness of
the trajectory for fixed initial data, not uniqueness of a periodic orbit or
of a root of the shooting equations.

### CAPD::DynSys (2021)

T. Kapela, M. Mrozek, D. Wilczak, and P. Zgliczyński, “CAPD::DynSys: A
flexible C++ toolbox for rigorous numerical analysis of dynamical systems,”
*Communications in Nonlinear Science and Numerical Simulation* **101**,
105578 (2021).
[DOI](https://doi.org/10.1016/j.cnsns.2020.105578) ·
[publisher record](https://www.sciencedirect.com/science/article/pii/S1007570420304081) ·
[author preprint](https://arxiv.org/abs/2010.07097).

**Supports:** CAPD's validated integration of sets of initial conditions,
interval parameters, first and higher variational equations, and rigorous
flows/Poincaré maps.  It is the primary software-method citation for the
project's use of `OdeSolver` with a multiprecision \(C^1\) set.

**Does not support:** correctness of the project's vector field, shooting
formulation, gauge/energy equation, tolerances, compiler flags, MPFR build,
or stored outputs.  Nor does an ODE enclosure alone establish a periodic
orbit, its principal period, or uniqueness outside a root box.

The DOI contains 2020 because of online-publication metadata; the cited
journal volume is 101 (2021).

### Poincaré-map refinement (2022)

T. Kapela, D. Wilczak, and P. Zgliczyński, “Recent advances in a rigorous
computation of Poincaré maps,” *Communications in Nonlinear Science and
Numerical Simulation* **110**, 106366 (2022).
[DOI](https://doi.org/10.1016/j.cnsns.2022.106366) ·
[author preprint](https://arxiv.org/abs/2104.08046).

**Supports:** rigorous enclosures of crossing times, Poincaré maps, and
their derivatives, including the importance of the section and coordinate
choice.

**Project boundary:** cite this source only for genuinely event-defined
Poincaré-map parts.  If a certificate uses a fixed-time map plus separate
phase/energy equations, its semantics must be described as such.  In either
case, transversality and a fixed-point inclusion are separate checks.

## Rigorous continuation and uniqueness of periodic orbits

### Wilczak and Barrio (2017)

D. Wilczak and R. Barrio, “Systematic Computer-Assisted Proof of Branches of
Stable Elliptic Periodic Orbits and Surrounding Invariant Tori,” *SIAM
Journal on Applied Dynamical Systems* **16**(3), 1618–1649 (2017).
[DOI](https://doi.org/10.1137/17M1113254) ·
[author manuscript](https://ww2.ii.uj.edu.pl/~wilczak/papers/invtori/bw_siads_2017.pdf).

**Supports:** the closest direct precedent located for the continuation
logic: rigorous Poincaré maps and \(C^r\)-Lohner derivatives combined with a
parameter-uniform interval Newton test to obtain one locally unique fixed
point for every parameter in a box and a validated \(C^1\) branch.

**Does not support:** global uniqueness outside those boxes, primitivity,
automatic identification of independently validated cells, or real
analyticity.  In the project, guarded bridges identify adjacent cells, the
analytic implicit-function theorem gives analytic regularity, and the
separate short-period exclusion gives primitivity.  A4.12 still makes no
global uniqueness claim outside its boxes.

### Wilczak and Zgliczyński (2009)

D. Wilczak and P. Zgliczyński, “Period Doubling in the Rössler System—A
Computer Assisted Proof,” *Foundations of Computational Mathematics*
**9**(5), 611–649 (2009).
[DOI](https://doi.org/10.1007/s10208-009-9040-x) ·
[author preprint](https://arxiv.org/abs/0712.1123).

**Supports:** an early full-scale precedent for validated derivatives,
Poincaré maps, and interval techniques in a rigorous periodic-orbit/
bifurcation proof.

**Does not support:** transfer of the Rössler-specific bifurcation theorem to
this Hamiltonian system or the claim that CAPD output alone proves the
project's connected branch.

### Barrio and Rodríguez (2014)

R. Barrio and M. Rodríguez, “Systematic Computer Assisted Proofs of
periodic orbits of Hamiltonian systems,” *Communications in Nonlinear
Science and Numerical Simulation* **19**(8), 2660–2675 (2014).
[DOI](https://doi.org/10.1016/j.cnsns.2013.12.025) ·
[publisher record](https://www.sciencedirect.com/science/article/pii/S1007570413006060).

**Supports:** a close Hamiltonian precedent using CAPD and interval Newton
to validate periodic orbits, their stability, continuous families, and
local one-and-only-one-family statements in the authors' setting.

**Novelty boundary:** CAPD plus interval Newton for Hamiltonian periodic-
orbit families is prior art.  The potentially new content here is the
model-specific Hénon-warped return system, its exact analytic anchor and
full-return recovery, the guarded bridge cover, and the paired
branch/determinant certificate—not the generic method combination.

## Arithmetic and reproducibility

### Correctly rounded multiprecision arithmetic

L. Fousse, G. Hanrot, V. Lefèvre, P. Pélissier, and P. Zimmermann, “MPFR: A
Multiple-Precision Binary Floating-Point Library With Correct Rounding,”
*ACM Transactions on Mathematical Software* **33**(2), article 13, 15 pages
(2007).
[DOI](https://doi.org/10.1145/1236463.1236468) ·
[official MPFR citation page](https://www.mpfr.org/algo.html).

**Supports:** the correctly rounded multiple-precision primitive used by the
CAPD build and the importance of an explicit rounding mode.

**Does not support:** that compiler flags, all intermediate conversions, or
all application-level interval endpoints are outward rounded.  Those are
build- and code-level obligations.

### Relevant IEEE standards

- *IEEE Standard for Floating-Point Arithmetic*, IEEE Std 754-2019 (2019).
  [DOI](https://doi.org/10.1109/IEEESTD.2019.8766229) ·
  [official record](https://standards.ieee.org/ieee/754/6210/).
- *IEEE Standard for Interval Arithmetic*, IEEE Std 1788-2015 (2015).
  [DOI](https://doi.org/10.1109/IEEESTD.2015.7140721) ·
  [official record](https://standards.ieee.org/ieee/1788/4431/).

**Supports:** normative definitions for floating-point operations,
rounding/conversion, and interval arithmetic.

**Does not support:** a claim that CAPD or this archive conforms to either
standard unless conformance is separately established.  Neither standard
specifies the project's exact-decimal transcript/replay workflow.

### Reproducible computational methods

V. Stodden, M. McNutt, D. H. Bailey, E. Deelman, Y. Gil, B. Hanson,
M. A. Heroux, J. P. A. Ioannidis, and M. Taufer, “Enhancing
reproducibility for computational methods,” *Science* **354**(6317),
1240–1241 (2016).
[DOI](https://doi.org/10.1126/science.aah6168) ·
[PubMed record](https://pubmed.ncbi.nlm.nih.gov/27940837/).

**Supports:** publishing code, data, workflows, environmental/version
information, licenses, persistent links, and tests so computations can be
inspected and repeated.

**Does not support:** mathematical validation of a numerical result or any
particular decimal serialization.  Reproducibility and proof validity are
related but distinct gates.

### Exact-decimal replay: scoped finding

No primary paper or normative standard located in this audit requires the
following exact protocol as a general norm:

1. serialize every outward interval endpoint as a decimal string;
2. interpret the string as an exact rational number rather than converting
   it back to binary floating point;
3. replay the Krawczyk and determinant inequalities in exact rational
   arithmetic; and
4. require componentwise cross-precision overlap of every archived root box
   and printed Krawczyk image from the 128- and 256-bit MPFR runs.

The protocol is nevertheless mathematically useful.  Steps 1–3 remove a
second layer of floating-point ambiguity from the finite proof-object audit,
provided the producer has already guaranteed that the serialized endpoints
are outward enclosures.  Step 4 is a strong implementation-consistency gate,
but replication at two precisions is not a substitute for the strict
inclusion theorem.  The manuscript should call this an **independent exact-
rational replay of the stored interval proof objects**, not an independent
validated ODE computation.

## Claim-to-source map

| Intended manuscript statement | Best source(s) | Safe scope |
|---|---|---|
| A strict Krawczyk inclusion plus verified uniqueness hypotheses proves a unique zero | Krawczyk (1969); Neumaier (1990); Moore–Kearfott–Cloud (2009) | One zero in the stated box, assuming valid residual/Jacobian enclosures and the selected theorem's regularity/contraction hypotheses |
| Local uniqueness is not global uniqueness | Kearfott (1996) | Global claims require exhaustive treatment of a declared complement |
| Validated integration encloses an IVP solution | Nedialkov–Jackson–Corliss (1999) | IVP enclosure, not a periodic shooting root |
| \(C^1\)-Lohner encloses flow derivatives | Zgliczyński (2002) | First variations/Poincaré derivatives, not root existence by itself |
| CAPD supports rigorous flows, variational equations, parameters, and Poincaré maps | Kapela–Mrozek–Wilczak–Zgliczyński (2021) | Software capability, not validation of this encoding or run |
| Parameter-uniform interval Newton can validate a locally unique periodic-orbit branch | Wilczak–Barrio (2017) | Local \(C^1\) branch in prescribed boxes; not global uniqueness or automatic analyticity |
| CAPD + interval Newton has Hamiltonian periodic-family precedents | Barrio–Rodríguez (2014) | Generic method combination is prior art |
| Correctly rounded multiprecision arithmetic is provided by MPFR | Fousse et al. (2007) | Arithmetic primitive; application-level outwardness still must be audited |
| Reproducibility calls for code/data/environment disclosure | Stodden et al. (2016) | Artifact practice, not a proof theorem |
| Exact-decimal rational replay is a recognized mandatory standard | None located | Describe as a project-specific verification design, with no standards claim |

## Consequences for Paper 02

The computer-assisted theorem can be stated defensibly if its hypotheses and
scope remain visible:

> For every parameter value in each certified slab, validated \(C^1\) flow
> and variational enclosures produce interval residual and Jacobian data for
> the complete reduced return system.  A strict parameterized Krawczyk
> inclusion then proves one root in the displayed box.  Guarded bridge
> certificates identify adjacent local roots as one connected branch.  The
> result is unique only within the union of the certified boxes and bridge
> hulls; it does not exclude roots in their complement.

The software sentence should read:

> The validated integrations use the official CAPD repository pinned at
> commit `731079217a9254ea2948d742df2b170895effe7f`, whose
> `CAPDVersion.txt` reports version 6.1.0, with the separately recorded
> MPFR/GMP build and compiler configuration.

The replay sentence should read:

> Separate independent checkers parse the stored decimal endpoints as exact
> rationals.  One replays the finite-dimensional Krawczyk and contraction
> inequalities; the other replays the phase and determinant inequalities.
> They audit stored proof objects but do not rerun CAPD or independently
> regenerate the ODE enclosures.

Avoid the following formulations:

- “CAPD proves the periodic orbit.”  CAPD supplies validated flow and
  derivative enclosures; the return formulation, Krawczyk inclusion, and
  analytic recovery arguments prove the orbit statement.
- “The interval Newton test proves the unique periodic orbit.”  It proves a
  unique root in a declared box; primitivity, equivalence to a full return,
  and complement exclusion are additional questions.
- “Two precisions independently prove the theorem.”  They are two producer
  runs and a robustness gate; the exact-rational checkers are independent
  only at the stored finite-inequality layer.
- “CAPD 6.1.0 release.”  The pinned source tree reports 6.1.0, but no such
  tag/release is present in the official repository.
- “Our CAPD/interval-Newton continuation method is novel.”  The 2014 and
  2017 periodic-orbit papers are direct precedents.

## Official CAPD provenance links

- [Pinned commit](https://github.com/CAPDGroup/CAPD/commit/731079217a9254ea2948d742df2b170895effe7f)
- [`CAPDVersion.txt` at the pinned commit](https://github.com/CAPDGroup/CAPD/blob/731079217a9254ea2948d742df2b170895effe7f/CAPDVersion.txt)
- [`OdeSolver.hpp` at the pinned commit](https://github.com/CAPDGroup/CAPD/blob/731079217a9254ea2948d742df2b170895effe7f/capdDynSys/include/capd/dynsys/OdeSolver.hpp)
- [`mplib.h`, defining the `MpC1Rect2Set` alias used by the producer](https://github.com/CAPDGroup/CAPD/blob/731079217a9254ea2948d742df2b170895effe7f/capdDynSys/include/capd/dynset/mplib.h)
- [Official tags](https://github.com/CAPDGroup/CAPD/tags) and
  [official releases](https://github.com/CAPDGroup/CAPD/releases)

The legacy generated CAPD documentation identifies itself as version 5.2.0,
so it is useful for general API explanations but should not substitute for
commit-pinned source provenance.  The relevant official pages are the
[validated ODE/time-map overview](https://capd.sourceforge.net/capdDynSys/docs/html/a05233.html),
[Poincaré-map overview](https://capd.sourceforge.net/capdDynSys/docs/html/a05238.html),
and [complete Rössler periodic-orbit example](https://capd.sourceforge.net/capdDynSys/docs/html/a05240.html).
The last page is also a useful scope check: it combines a rigorous Poincaré
map with interval Newton to prove a unique fixed point in a box, while
explicitly saying that the program does not check the asserted principal
periods.

## Final audit judgment

The source chain is sufficient to position the method as an orthodox but
carefully audited composition of validated \(C^1\) integration and
interval-operator root certification.  The publishable distinction lies in
the model-specific proof architecture and the transparent proof archive.
The literature does not close the project's remaining complement/global-
cover gates, does not make the exact-decimal replay a formal standard, and
does not license an unqualified novelty claim for periodic-orbit
continuation by CAPD plus interval Newton.
