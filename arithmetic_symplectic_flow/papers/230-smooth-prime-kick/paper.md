# Prime-only fixed points of a smooth kick on the connected symplectic plane

**Paper ID:** `230-smooth-prime-kick`  
**Candidate ID:** `ASFS-20260918-SPK01`  
**Date / status:** `2026-09-18; SCOPED ENGINEERING POSITIVE — CONNECTED EXACT
SYMPLECTIC OWNER AND COMPLETE PRIME-ONLY LEDGER; A0 NATURALNESS OPEN;
UNIT-ROOF TARGET CLOCK SCOPED FAIL`  
**Route state:** owner-level construction only; formal Route-A coordinates
`UNASSIGNED`; Route B `NOT INVOKED`.

## Abstract

One connected symplectic plane is equipped with a smooth nonnegative kick
whose integer-site amplitudes count divisors up to the square root.  The kick
vanishes exactly at the prime integers.  Its composition with a horizontal
shear is a global exact symplectomorphism.  Along every trajectory momentum
is nonincreasing; on a periodic trajectory it is constant, forcing zero
momentum and a prime fixed point.  Thus the full intrinsic periodic ledger has
one fixed point per prime and no omitted composite or continuous periodic
families.  The unit-roof suspension is complete and gives one oriented
primitive circle per prime, all of period one, with repetition times equal to
the repetition number.  This is a connected-carrier engineering result, not a
natural arithmetic-clock construction.  The source remains a static
divisor-coded potential, the target logarithmic clock fails, all fixed points
are parabolic, and the ordinary product over infinitely many unit circles has
no absolute-convergence half-plane.  No transfer operator, determinant, trace
formula, Route coordinate, or quantum owner is supplied.

## 1. Candidate identity and lineage

The [candidate card](candidate-card.md) fixes the entire plane, one explicit
bump, one map, and the unit roof before the proof audit.  This is candidate
`ASFS-20260918-SPK01`, not a parameter change in another package.

The project [prior-work guide](../../docs/prior_work/README.md) motivates the
arrow from a prime/composite symbolic observable and its admissibility
constraints to a positive-dimensional area-preserving realization.  Here the
precise retained observable is

\[
a_n=\sum_{d=2}^{\lfloor\sqrt n\rfloor}{\bf1}_{d\mid n},\qquad n\ge2.
\tag{1}
\]

It is the zero/nonzero output of the finite local divisor-admissibility scan.
The deformation statically compresses/replaces the scan's zero/nonzero
admissibility constraint by a smooth spatial bump amplitude in a connected
potential; it does not preserve the scanner's time order.  The lift places that potential
inside one exact symplectic kick/shear.  This gives a concrete source-to-map
relation; it does not supply a Markov partition, a conjugacy to the Logistic
prototype, or a theorem inherited from the Hénon stream.  The finite scan is
used to define coefficients, not dynamically executed in a time register.

The closest local controls include the
[witness-kicked cylinder 150](../150-witness-kicked-cylinder/README.md), whose
prime-supported periodic fibres still contain continuum-many packets at
rational momenta, and the
[convex witness Hénon sieve 145](../145-convex-witness-henon-sieve/README.md),
whose nonnegative cycle-sum already proves a prime-only ledger.  This paper
does not claim a new positivity device.  Its specific difference is the one
connected plane with arithmetic zero sites in a single spatial potential,
and its full periodic classification has no rational-momentum continuum.

| Ledger item | Owner and definition | Scope |
| --- | --- | --- |
| Base carrier | \(M=\mathbb R^2_{(x,p)}\), \(\omega=dx\wedge dp\) | Full connected plane, no selected section of a larger map |
| Map | Equation (4) below | One explicit global exact symplectomorphism |
| Arithmetic input | Equation (1), all integers \(n\ge2\) | Divisibility rule, not a supplied prime table |
| Symbolic relation | Zero-divisor admissibility is preserved as the potential's integer zero set | No claim of a full symbolic coding |
| Roof and flow | \(\tau=1\), endpoint-glued suspension of the same \(F\) | Complete, with no logarithmic rescaling |
| Primitive ledger | Every intrinsic periodic point of the full map | One prime fixed point each; proof below |
| Repetitions | Same oriented circle traversed \(r\) times | Time \(r\), not a new primitive |
| Analytic owner | No operator, trace, or Fredholm determinant constructed | Ordinary unweighted-product obstruction only |
| Later lift | Hamiltonian/contact/quantum | `DEFERRED` |

The three-dimensional mapping torus is not called a symplectic manifold or a
Hamiltonian flow.  Only its two-dimensional base has the asserted symplectic
structure.

## 2. Definitions, question, and claim boundary

Define

\[
\rho(t)=\begin{cases}e^{-1/t^2},&t>0,\\0,&t\le0,\end{cases}
\qquad
\eta(t)=\begin{cases}
\exp\!\left(1-\dfrac1{1-16t^2}\right),& |t|<1/4,\\
0,&|t|\ge1/4.
\end{cases}
\tag{2}
\]

The fixed smooth nonnegative potential and map are

\[
f(x)=\sin^2(\pi x)+\rho(2-x)+\sum_{n=2}^{\infty}a_n\eta(x-n),
\tag{3}
\]
\[
F(x,p)=\bigl(x+p,\ p-f(x+p)\bigr).
\tag{4}
\]

The question is whether (4), on all of \(\mathbb R^2\), has a complete
prime-only intrinsic periodic ledger while preserving an honest connected
positive-dimensional carrier.  The answer below is positive in this exact
engineering sense.  It does not answer whether arithmetic naturally selects
(3), and it does not produce a prime-dependent clock.

There is no numerical parameter fitting, prime list, zero data, von Mangoldt
weight, or per-prime scale choice.  All coefficients are specified by (1),
and no finite cutoff defines the map.  The potential is nevertheless a static
encoding of the divisor test; absence of a supplied prime table is not a
proof of source naturalness.

## 3. Smooth potential and exact symplectic owner

### Proposition 1 — Smoothness and exact zero set

The series in (3) is locally finite, \(f\in C^\infty(\mathbb R)\),
\(f\ge0\), and

\[
f^{-1}(0)=\{\ell:\ell\text{ is a prime integer}\}.
\tag{5}
\]

**Proof.** Every coefficient \(a_n\) is a finite nonnegative integer.  The
support of \(\eta(x-n)\) is contained in \([n-1/4,n+1/4]\).  A compact
interval meets only finitely many such supports; indeed distinct supports do
not overlap.  Thus every derivative of (3) is locally a finite sum.  At the
boundary of the bump support all derivatives vanish, because any reciprocal
power of the distance to that boundary multiplied by the exponential in (2)
tends to zero.  The same flat-extension argument at zero proves smoothness of
\(\rho\).  All terms are nonnegative.

If \(x<2\), then \(\rho(2-x)>0\), so \(f(x)>0\).  If \(x\ge2\)
is not an integer, then \(\sin^2(\pi x)>0\).  At an integer \(n\ge2\)
the sine and cutoff terms vanish, every bump except the one centred at \(n\)
vanishes, and \(f(n)=a_n\eta(0)=a_n\).  A prime has no divisor in the
range of (1), so \(a_n=0\).  Conversely, if \(n\ge2\) is composite,
writing \(n=uv\) with \(2\le u\le v\) gives
\(u\le\sqrt n\), hence \(a_n\ge1\).  This proves (5), including the
empty sums at \(n=2,3\).  QED.

The coefficients need not be bounded for this argument: local finiteness,
not uniform convergence of a global series, is the asserted regularity
mechanism.

### Proposition 2 — Global inverse and exact symplecticity

The map (4) is a global smooth exact symplectomorphism of the connected plane.
Its inverse is

\[
F^{-1}(X,P)=\bigl(X-P-f(X),\ P+f(X)\bigr).
\tag{6}
\]

**Proof.** Writing \(X=x+p\) and \(P=p-f(X)\) immediately gives
\(p=P+f(X)\) and then the first coordinate of (6).  Both maps are smooth
everywhere by Proposition 1.  Moreover,

\[
dX\wedge dP=(dx+dp)\wedge\bigl(dp-f'(X)(dx+dp)\bigr)
=dx\wedge dp.
\]

For exactness use the global primitive \(\lambda=-p\,dx\), so that
\(d\lambda=\omega\), and set \(V(u)=\int_0^u f(v)\,dv\).  Then

\[
F^*\lambda-\lambda
=-(p-f(X))(dx+dp)+p\,dx
=f(X)\,dX-p\,dp
=d\!\left(V(x+p)-\frac{p^2}{2}\right).
\tag{7}
\]

No restriction on \((x,p)\) entered the inverse or the exactness identity.
QED.

## 4. Full periodic ledger, repetitions, and monodromy

### Theorem 3 — All intrinsic periodic points are prime fixed points

For every positive integer \(m\),

\[
\operatorname{Fix}(F^m)=\{(\ell,0):\ell\text{ is prime}\}.
\tag{8}
\]

Each point in (8) has least map period one; no other least periods, continuous
periodic families, or composite periodic states occur.

**Proof.** Let \((x_j,p_j)=F^j(x_0,p_0)\), where the orbit is \(m\)-periodic.
Its exact recurrence is

\[
x_{j+1}=x_j+p_j,\qquad p_{j+1}=p_j-f(x_{j+1}).
\tag{9}
\]

Since \(f\ge0\), momentum is nonincreasing.  Summing the second equation
over a period gives

\[
0=p_m-p_0=-\sum_{j=0}^{m-1}f(x_{j+1}).
\tag{10}
\]

All summands are nonnegative, so every one is zero.  Hence every \(p_j\)
equals a constant \(c\), and summing the first equation gives
\(0=x_m-x_0=mc\).  Thus \(c=0\), all \(x_j=x_0\), and
\(f(x_0)=0\).  Proposition 1 gives \(x_0=\ell\) prime.  Conversely,
each \((\ell,0)\) is fixed by (4).  The argument starts from an arbitrary
periodic point on the full real plane, so it proves coverage, not merely
existence at selected centres.  QED.

### Proposition 4 — Complete unit-roof suspension ledger

Let

\[
M_\tau=(\mathbb R^2\times[0,1])/((z,1)\sim(Fz,0)),\qquad\tau=1.
\tag{11}
\]

Translation in the second coordinate induces a smooth flow defined for all
real times.  Its oriented primitive closed orbits are exactly
\(\gamma_\ell\), one for each prime fixed point \((\ell,0)\), with

\[
T_{\gamma_\ell}=1,\qquad T_{\gamma_\ell^r}=r\quad(r\ge1).
\tag{12}
\]

**Proof.** The global diffeomorphism (6) permits all positive and negative
section crossings.  A bounded real time interval contains only finitely many
crossings because every roof equals one; hence there is no Zeno accumulation
in either direction.  The height modulo one defines a circle-valued function
on the quotient.  A closed trajectory must therefore have a positive integer
return time, and its section state must be fixed by the corresponding iterate
of \(F\).  Theorem 3 classifies those states.  Above each fixed point the
quotient is one circle with least positive period one.  Cyclic starting
positions on it do not create extra primitives; traversing it \(r\) times
gives (12).  QED.

This unit clock is not \(\log\ell\).  It also cannot be converted to all
prime logarithms by one global change of time units, since \(\log2\ne\log3\).
The target-clock discrepancy is a scoped negative theorem, not an unknown
quantity.  Whether a different natural mechanism could provide an appropriate
clock is `OPEN`, but it would belong to a fresh candidate.

### Proposition 5 — Degenerate parabolic monodromy

At every surviving prime fixed point,

\[
DF(\ell,0)=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
DF^r(\ell,0)=\begin{pmatrix}1&r\\0&1\end{pmatrix},\qquad
\det(I-DF^r(\ell,0))=0.
\tag{13}
\]

**Proof.** A smooth nonnegative function vanishing at an interior point has
zero first derivative there, so \(f'(\ell)=0\).  Differentiating (4) gives

\[
DF(x,p)=\begin{pmatrix}1&1\\-f'(x+p)&1-f'(x+p)\end{pmatrix}.
\]

At a prime fixed point this is the first matrix in (13).  Its nilpotent
off-diagonal part squares to zero, which gives the stated powers and zero
determinant.  QED.

Thus the full periodic set is discrete, but its periodic points are
nonhyperbolic and degenerate.  Discreteness does not license a standard
nondegenerate periodic-orbit trace denominator.

## 5. Adversarial controls and the static-potential risk

These controls are exact comparison objects, not silent changes to the frozen
candidate.  For any nonnegative sequence \((b_n)_{n\ge2}\), replace only
\(a_n\) in (3) by \(b_n\) and call the result \(f_b\).  The proofs above
give

\[
\operatorname{Fix}(F_b^m)=\{(n,0):n\ge2,\ b_n=0\}
\quad\text{for every }m\ge1.
\tag{14}
\]

Equation (14) is a general encoding statement and the decisive
`PROVES_TOO_MUCH` warning.  The connected kick/shear realizes the prescribed
zero locations of a nonnegative coefficient sequence; the symplectic and
periodicity arguments themselves do not distinguish primes.
More explicitly, for any subset \(A\subseteq\{2,3,\ldots\}\), the control
choice \(b_n=0\) on \(A\) and \(b_n=1\) off \(A\) realizes exactly
\(\{(n,0):n\in A\}\) as its entire periodic set.  This is a control family,
not a replacement of the frozen divisor amplitudes.

| Control | Exact definition and result | Meaning |
| --- | --- | --- |
| Bump-free base / zero amplitudes | \(b_n=0\) for all \(n\ge2\); only \(\sin^2(\pi x)+\rho(2-x)\) remains, and every integer \(n\ge2\) gives a fixed point. | The generic smooth geometry does not select primes. |
| Shifted divisors | \(b_n=a_{n+1}\); the fixed points are exactly integers \(n\ge2\) with \(n+1\) prime.  For example \(n=4\) survives and \(n=3\) does not. | Arithmetic selectivity is tied to the specific spatial placement of divisor amplitudes. |
| Finite shuffled block | Choose \(N\ge4\) and a permutation \(\sigma\) of \(\{2,\ldots,N\}\); set \(b_n=a_{\sigma(n)}\) inside the block and \(b_n=a_n\) outside. | The number of zeros in the block is exactly preserved, while their labels are permuted; connectedness and all proofs remain unchanged. |
| Same-density randomized bumps | Choose \(\sigma\) uniformly among those finite-block permutations and freeze its realized permutation as control data. | Every realization preserves the finite-block zero density exactly; the output labels merely follow the random zero locations.  This is an exact conditional theorem, not a reported simulation. |
| Base-potential ablation | Remove both cutoff and bumps, leaving \(f(x)=\sin^2(\pi x)\). | Every integer in \(\mathbb Z\), including nonpositive ones, is a fixed point.  The cutoff excludes the unwanted spatial half-line by design. |

No random experiment was run, and no stochastic or asymptotic density claim is
made.  The permutation statement is stronger than a finite observed example
for the stated finite-block control.  In particular a swap of the amplitudes
at 3 and 4 removes the prime point 3 and inserts the composite point 4 without
altering the form of the map.

The source-level result is therefore `A0 SCOPED POSITIVE / NATURALNESS OPEN`:
the fixed map does own the divisor test's prime-only zero set, with no
post-hoc prime slice, but it does not explain why this static arithmetic
potential is privileged.  The connected carrier solves a geometric ownership
problem, not the source-naturalness problem.

## 6. Analytic boundary

No transfer operator or Fredholm determinant is constructed.  Even the
ordinary unweighted primitive product has an immediate obstruction.  With
the actual roof (12), its prospective absolute log expansion would require

\[
\sum_{\ell\text{ prime}}\sum_{r\ge1}\frac{|e^{-sr}|}{r}<\infty.
\tag{15}
\]

For any finite real part \(\sigma=\Re s\), the \(r=1\) subseries is
\(\sum_{\ell\text{ prime}}e^{-\sigma}\), which diverges.  Thus there is
no half-plane of ordinary absolute convergence.  Infinite primes are enough
for this conclusion: if there were only a finite list, a prime divisor of
one plus their product would lie outside it.  This is a same-object negative
control, not a construction of any regularized determinant.

Together with (13), this excludes importing the ordinary prime Euler product
or a standard nondegenerate flat-trace formula.  It does not prove that every
possible analytic realization is impossible.  Changing the roof, inserting
weights, or adding an operator would require a separately frozen owner and
would not inherit A2 credit from this paper.

## 7. Gate assessment, limitations, and decision

| Gate | Evidence for ASFS-20260918-SPK01 | Status and boundary |
| --- | --- | --- |
| P0 geometry and ownership | Propositions 1–2 and the explicit card | Established on the full connected plane; no omitted ambient periodic states |
| A0 arithmetic selector | Equation (5) and Theorem 3 | `SCOPED POSITIVE / NATURALNESS OPEN`; static divisor potential and control (14) remain adverse findings |
| A1 full primitive ledger | Theorem 3 and Proposition 4 | `OWNER-LEVEL ESTABLISHED`; one prime circle each, unit repetitions, all states covered |
| A1 target logarithmic clock | Equation (12) | `SCOPED FAIL`; all prime periods equal one, not \(\log\ell\) |
| A2 | No operator; (13) and (15) are negative entry controls | `NOT EVALUATED`; no formal coordinate or determinant claim |
| Formal Route A / Route B | No formal evaluator run | `UNASSIGNED` / `NOT INVOKED` |

**Portfolio decision: stop / fork.**  Preserve the connected two-dimensional
exact symplectic realization and its complete prime-only ledger as an
engineering control.  Stop promotion of this candidate because the unit roof
provably collapses every prime to the same primitive time; source naturalness
also remains unresolved.  A different arithmetic clock, potential or analytic
owner requires a new card, not local retuning under this ID.

The same-object ledger stayed intact throughout: the source coefficients,
smooth map, full periodic set, suspension clock, repetitions and negative
analytic controls all refer to (1)–(4) and (11).  No theorem, clock,
determinant, Route credit or quantum owner is transferred from another
candidate.  The statement is a scoped constructive theorem, not a natural A0
pass, formal Route-A result, or Route-B entry.

## Reproducibility and disclosures

- [Frozen candidate card and pre-result specification clarification](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence methods and verification record](evidence/README.md)
- [Package summary](README.md)

The arguments are exact; no orbit cutoff, numerical precision, floating-point
test, unbounded computation, PDF or publication artifact is used.  Data
availability: every definition and proof input is in this package, with no
external dataset.  Ethics: no human subjects or private data are involved.
Author contributions: automated candidate formalization, proof drafting and
local consistency checking; human scholarly authorship is not assigned by
this record.  Funding and conflicts of interest: not supplied, so no external
funding or conflict-free status is asserted.  AI use: this is an AI-assisted
internal research record, not externally peer-reviewed work.
