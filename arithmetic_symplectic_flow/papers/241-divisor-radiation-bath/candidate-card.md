# Frozen divisor-channel oscillator / radiation bath

**Candidate ID:** `ANG-20260918-DRB01`  
**Paper ID:** `241-divisor-radiation-bath`  
**Version:** 1; frozen 2026-09-18 before the mathematical audit.  
**Initial status:** `PROPOSAL — FULL OWNER AND PERIODIC SELECTION OPEN`.  
**Formal coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

This is a separately admitted conservative-mechanism control of
[SCJ01](../240-source-clock-joint-frontier/candidate-card.md), not a claim
that its source-naturalness question has been solved. It replaces static
force-based exclusion by full conservative field coupling. The integer
label and divisor incidence remain static. No sequential source update is
claimed. The carrier is an infinite-dimensional real Hilbert flow and its
transformation groupoid, not a classical finite-dimensional ASFS map.

## Exact carrier, arithmetic input and Hamiltonian

For every integer \(n\ge2\), retain \((q,p)\in\mathbb R^2\) and all
\(n-1\) complex field channels \(z_d\in\mathfrak h\), including inactive
ones, where

\[
\mathfrak h=L^2((0,\infty),(1+\omega)\,d\omega;\mathbb C),\qquad
X_n=\mathbb R^2\times\mathfrak h^{n-1},\qquad X=\coprod_{n\ge2}X_n.
\]

Write \(\varepsilon_{n,1}=0\) and
\(\varepsilon_{n,d}=\mathbf1_{\{d\mid n\}}\) for \(2\le d<n\).
The only coefficients are

\[
c_n=1+n^{-2},\quad W(q)=\frac{4q^2}{(1+q^2)^2},\quad
f(\omega)=e^{-\omega},\quad g(\omega)=\omega e^{-\omega}.
\]

The real weak symplectic form is the sum of \(dq\wedge dp\) and the
channel forms \(\Omega_d(u,v)=2\operatorname{Im}\int_0^\infty\bar u v\,d\omega\).
Freeze

\[
H_n(q,p,z)=\frac{p^2}{2}+c_nW(q)
 +\sum_{d=1}^{n-1}\int_0^\infty
 \omega\left|z_d(\omega)+\varepsilon_{n,d}qf(\omega)\right|^2d\omega.
\tag{1}
\]

The completed square, including its quadratic counterterm, is the actual
definition; no later subtraction or renormalization is allowed. The full
candidate carrier is \(M=\coprod_{n\ge2}\{H_n=1\}\), fixed before proof.
No initial state on this level is removed.

## Exact action and domain obligation

Use \(\iota_{X_H}\Omega=dH\), actual time \(t\), and equations

\[
\dot q=p,\qquad
\dot p=-c_nW'(q)-2\sum_d\varepsilon_{n,d}\operatorname{Re}
 \int_0^\infty g(\omega)
  \bigl(\bar z_d(\omega)+\varepsilon_{n,d}qf(\omega)\bigr)d\omega,
\tag{2}
\]
\[
i\dot z_d(\omega)=\omega z_d(\omega)+\varepsilon_{n,d}qg(\omega).
\tag{3}
\]

Let \(U_tz(\omega)=e^{-i\omega t}z(\omega)\). The action must be
constructed for every \(X_n\) initial state by the scalar integral equations
and

\[
z_d(t)=U_tz_d(0)-i\varepsilon_{n,d}
 \int_0^tU_{t-s}q(s)g\,ds.
\tag{4}
\]

Global existence, uniqueness, energy preservation and a continuous
two-sided group action are OPEN audit obligations, not assumed. The
strong generator domain is
\(D(M_\omega)=\{z\in\mathfrak h:\omega z\in\mathfrak h\}\);
it must not replace the full mild carrier. If the action exists, its
transformation groupoid is \(M\rtimes\mathbb R\).

## Lineage, packets and prohibited substitutions

The precise lineage arrow is prime/composite proper-divisor symbols
\(\longrightarrow\) all proper-factor channel incidence
\(\longrightarrow\) reciprocal conservative oscillator/field coupling.
The witness changes the evolution of real field coordinates, rather than
specifying a prime-only carrier. This is a conservative deformation of a
symbolic exclusion rule, not a conjugacy to a historical Logistic/Henon
map, and not a proof of a naturally forced sieve evolution.

Count every nonconstant periodic full-state orbit, modulo time translation
only, as a primitive packet at its least positive physical period. Keep
orientation, all field phases, all channels and any stationary states;
classify multiplicity and repetitions from full-state equality. No
outgoing-wave condition, dissipative reduction, generalized monochromatic
state, phase quotient, selected oscillator section, or field projection is
permitted. Closed field response cannot be presumed absent.

The first joint test is full mild ownership, then the periodic field
equations, then the oscillator clock on any genuinely derived surviving
packets. This order must decide whether prime returns survive and unwanted
returns disappear; deleting all returns is a failure, not a positive sieve.

## Scope and controls

| Field | Frozen owner / obligation |
| --- | --- |
| Allowed data | All integer labels, ordinary divisibility, the uniform rational barrier, fixed all-channel functions f and g, energy 1 |
| Forbidden input | Prime table, per-prime choices, supplied log-p roof, von Mangoldt weights, zero data |
| Clock | Actual equations (2)--(4), no time rescaling; logarithmic size is an audit question |
| Classical map / roof / mapping torus | NOT APPLICABLE; none constructed or borrowed |
| Prime / prime-power / mixed-composite controls | Full field equations for labels 2, 4, 6 and all labels; include inactive fields and constant-q states |
| Conservative ownership | Full energy preserved; apparent oscillator radiation must not become an assumed loss of total energy |
| Comparator controls | Set all incidence to zero; replace incidence by arbitrary Boolean channel data; constant barrier; remove barrier excess; change energy as a separate comparison |
| Nearest objects | 171 rational physical well; 182 finite-dimensional coupling; 237 discrete bound-state control; 239 full bilateral no-return control; all are different owners |
| Naturalness | OPEN; static incidence, barrier, energy and bath profile are engineered; arbitrary zero-channel sets are a PROVES_TOO_MUCH test |
| Analytic owner | Transfer operator, trace, zeta, determinant and continuation NOT SUPPLIED by this card |
| Later geometry | Contact, quantum, finite-dimensional section and quantization NOT SUPPLIED |
| Gate labels | Broadened T0--T3 only; no classical A0--A2 coordinate or formal Route inference |
| Stop / fork | Stop at nonexistence of the complete owner, hidden unwanted packets, loss of desired returns or failure of controlled physical-time growth; changing any generator, carrier or clock requires a new card |

The rational well matches a formula in
[171](../171-separatrix-witness-hamiltonian-clock/candidate-card.md), but
the full object does not. All packet and clock statements must be derived
for (1)--(4); no stability, return-map, analytic or Route credit transfers.
This bounded audit uses exact proofs, not numerical sweeps, and produces
only Markdown records under the [project standard](../paper-template.md).

## Version-one audit result — unchanged full owner and physical time

**Candidate ID:** `ANG-20260918-DRB01`  
**Status:** `ADVANCE — PRIME-ONLY FULL-FIELD PACKETS; PHYSICAL LOGARITHMIC CLOCK; NATURALNESS OPEN`.  
**Gates:** `T0 ESTABLISHED; T1 ENGINEERING POSITIVE / NATURALNESS OPEN; T2 ESTABLISHED; T3 NOT SUPPLIED`.  
**Independent mathematical review:** Separate model-assisted readback completed; [record](evidence/review.md).

The [full proof](paper.md) establishes a unique continuous global mild
action on every complete \(X_n\), preservation of the displayed energy
for all mild states, and the invariant regular full level \(H_n=1\).
The weak-form Hamiltonian identity is established on the strong domain;
that domain never replaces the full mild carrier. No everywhere defined
smooth Hilbert-valued vector field or unproved mild symplecticity result
is claimed.

Bounded frequency projections justify Bochner temporal harmonic equations
for any periodic mild state. An active divisor channel excludes every
nonzero harmonic of the real oscillator. All constant-oscillator periodic
configurations then have \(q=0,\pm1\), \(p=0\) and
\(z_d=-\varepsilon_{n,d}qf\), with energy 0 or \(c_n>1\).
They do not lie on the frozen carrier. Every inactive periodic field
vanishes by its atomless continuous frequency measure.

The complete ledger is one primitive oriented packet per prime and none
on composites, with no stationary state at energy one. Its actual period
is the derived scalar integral and satisfies
\(T_p=2\sqrt2\log p+O(1)\) uniformly in the original time units;
every repetition has time \(rT_p\). The rational-well integral is
rederived for this owner; no 171 return, stability or analytic theorem
is transferred.

The static incidence and conserved integer label remain unchanged, as do
the engineered barrier, energy and bath profile. Arbitrary Boolean channel
rows would select arbitrary zero-row labels. Source-naturalness therefore
remains OPEN, and this result is a conservative-mechanism control rather
than a new arithmetic source law. No scattering/decay, stability, trace,
zeta, determinant or quantum result is supplied. Formal coordinates remain
UNASSIGNED; Route B remains NOT INVOKED.

**Decision:** advance this bounded control; fork before claiming a natural
source-law solution. All channels, all energy-one states and actual time
are retained. See the [claim ledger](claim-ledger.md) and
[evidence/review state](evidence/README.md).
