# Classical candidate card — ASFS-20260918-SPK01

**Version:** 1, 2026-09-18; frozen before the proof audit.  
**Initial status:** `P0 FROZEN; A0/A1 PROOF OBLIGATIONS OPEN; A2 NOT EVALUATED`.

## Frozen object

Let

\[
a_n=\sum_{d=2}^{\lfloor\sqrt n\rfloor}{\bf1}_{d\mid n},\qquad n\ge2,
\]
and let \(\rho(t)=e^{-1/t^2}\) for \(t>0\), with \(\rho(t)=0\) for
\(t\le0\).  The explicitly fixed bump is

\[
\eta(t)=
\begin{cases}
\exp\!\left(1-\dfrac1{1-16t^2}\right),& |t|<1/4,\\
0,& |t|\ge1/4.
\end{cases}
\]

**v1 specification clarification, before results:** the first card text named
an arbitrary fixed smooth bump supported in \((-1/3,1/3)\); the displayed
formula now fixes that datum explicitly.  It has support \([-1/4,1/4]\),
is nonnegative, and is normalized by \(\eta(0)=1\).  This clarification
does not alter the roof, divisor amplitudes, carrier, or kick/shear architecture.
The potential is

\[
f(x)=\sin^2(\pi x)+\rho(2-x)+\sum_{n=2}^{\infty}a_n\eta(x-n).
\tag{1}
\]

The sum is part of the frozen definition, not a finite numerical fit.  The
phase space is the connected plane \(M=\mathbb R^2_{(x,p)}\), with
\(\omega=dx\wedge dp\), and the one exact kick/shear is

\[
F(x,p)=\bigl(x+p,\ p-f(x+p)\bigr).
\tag{2}
\]

The roof is the unit roof \(\tau\equiv1\), and the owned suspension is

\[
M_\tau=(M\times[0,1])/{((z,1)\sim(Fz,0))},
\]

with translation flow \(\varphi^t\).  All real \((x,p)\) are retained; no
prime fibre, centre slice, or momentum crop is allowed.

## P0 ownership ledger

| P0 field | Frozen definition / obligation |
| --- | --- |
| Candidate relation | Fresh connected-carrier candidate; no result or credit is inherited from 228/229 or any other package. |
| Symplectic phase space | \((\mathbb R^2,dx\wedge dp)\), connected and boundaryless. |
| Base map | The single map (2), with the potential (1); no parameter is selected after an arithmetic or spectral comparison. |
| Arithmetic mechanism | The divisor-count amplitudes \(a_n\) are internal coefficients of the same potential.  Zeros at integer sites are intended to distinguish primes from composites. |
| Lineage arrow | Prime/composite divisor observable \(\to\) divisor-admissibility scan \(\to\) smooth kick potential \(\to\) connected exact symplectic shear.  This is a deformation/lift of the project's prime-symbolic source, not a claim of a Markov conjugacy. |
| Roof / flow | \(\tau=1\), endpoint-glued mapping torus above this exact \(F\); completeness is immediate. |
| Orbit convention | Every least-period state of the full map is included; oriented suspension orbits are identified only by cyclic time shift. |
| Repetition law | The \(r\)-fold traversal of a primitive unit-roof circle has time \(r\); no relabelling creates a new primitive orbit. |
| Analytic owner | None frozen beyond this flow.  Transfer operator, determinant, and trace are `OPEN`; no borrowed analytic object is allowed. |
| Controls | \(a_n=0\) / base-potential control, shifted-divisor amplitudes, same-density randomized or shuffled amplitudes, and static-potential / `PROVES_TOO_MUCH` checks. |
| Future lift owner | Hamiltonian/contact/quantum owner `DEFERRED`. |
| Route state | Formal Route-A coordinates `UNASSIGNED`; Route B `NOT INVOKED`. |

## Immediate boundaries and stop rules

The construction is connected and genuinely two-dimensional, but the arithmetic
pattern is spatially frozen in a static potential.  Any scoped A0 positive
owner result still leaves source naturalness `OPEN`; the
paper must not call the divisor amplitudes a dynamically generated prime list.
The static zero set is also a `PROVES_TOO_MUCH` risk: replacing the amplitudes
by zero or by a shuffled sequence changes the fixed-point labels while leaving
the kick/shear and its symplectic proof intact.

The unit roof gives one period for every prime fixed point, not \(\log p\).
Any target-clock repair, non-unit roof, alternate potential, symbolic coding,
or analytic owner creates a new candidate ID.  An ordinary Euler product over
the countably many unit-period prime circles is not asserted.  No prime table,
manually inserted \(\log p\), von Mangoldt weight, Riemann-zero data, or
per-prime parameter enters the frozen object.

## Appended audit outcome — specification unchanged

**Audited status:** `SCOPED ENGINEERING POSITIVE — CONNECTED EXACT SYMPLECTIC
OWNER; COMPLETE PRIME-ONLY LEDGER; A0 NATURALNESS OPEN; UNIT-ROOF TARGET CLOCK
SCOPED FAIL`.

The [paper](paper.md) proves the global inverse and exact symplecticity, the
complete periodic set \(\{(\ell,0):\ell\text{ prime}\}\), suspension
completeness, unit primitive times, and repetition times \(r\).  Every
prime fixed point has monodromy
\(\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\), so all
repetitions are degenerate.  The ordinary primitive product has no
absolute-convergence half-plane.  A0 remains only a scoped engineering
positive because arbitrary nonnegative bump amplitudes realize arbitrary
integer zero patterns.  The target prime-log clock is a proved scoped FAIL,
not an OPEN quantity for this unit-roof object.

**Portfolio:** stop / fork at the target-clock failure; retain the connected
owner and complete ledger as a control.  A2 NOT EVALUATED; formal Route-A
coordinates UNASSIGNED; Route B NOT INVOKED.  See the
[claim ledger](claim-ledger.md), [summary](README.md), and
[evidence record](evidence/README.md).  No roof or potential was changed
during this audit.
