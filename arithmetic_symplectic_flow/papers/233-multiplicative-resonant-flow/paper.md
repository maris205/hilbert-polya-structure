# A global multiplicative resonant flow with an intrinsic mixed-prime periodic packet

**Paper ID:** `233-multiplicative-resonant-flow`  
**Candidate ID:** `ANG-20260918-MRF01`  
**Date / status:** 2026-09-18; `T0 ESTABLISHED; MIXED-PRIME PERIODIC PACKET — STOP / FORK`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

We audit the frozen coherent-mode equation indexed by all integers
\(n\ge2\), with dispersion \(\log n\) and quadratic fusion/fission along
\((a,b,ab)\). Weighted Hilbert–Schmidt estimates and an exact resonance
identity reduce the mild equation to a locally Lipschitz ordinary
differential equation on its charge space. Charge conservation proves a
global action on the entire unit shell, without restricting to finite
support. The nonlinear terms genuinely generate a product mode and feed
back into its factors. However, the full action also has a nonconstant
periodic orbit supported on powers of 6. Existence follows from the positive
maximum of a weakly continuous cubic on a Hilbert ball; the Euler equation
also supplies the generator-domain regularity needed for an actual strong
relative equilibrium. We derive its least physical period from the gcd of
the active exponents. This exact mixed-prime packet triggers the frozen
stop condition. Naturalness of the all-integer dispersion remains open; no
full orbit classification, trace, determinant or Route result is claimed.

## 1. Identity, question and lineage

The [version-1 card](candidate-card.md) was frozen before this audit. No
coefficient, carrier, charge, clock or packet convention is changed here.

| Item | Same-object owner | Evidence state |
| --- | --- | --- |
| Carrier | Full complex Hilbert shell \(\mathcal M=\{z:Q(z)=1\}\) below, with norm topology | Retained in full |
| Action | Exact mild equation (1), with every integer mode \(n\ge2\) | Global action proved in Section 4 |
| Arithmetic mechanism | All ordered factor triples \((a,b,ab)\), coefficient \(1/(ab)\) | Genuine feedback proved; design naturalness OPEN |
| Clock | Physical real time of (1), dispersion \(\log n\) | Unchanged; no suspension roof |
| Packets | All nonconstant primitive point orbits, modulo actual time translation only | One composite-source packet proved; full ledger NOT CLASSIFIED |
| Classical symplectic map / mapping torus | NOT APPLICABLE to this infinite-dimensional carrier | Not supplied |
| Trace / zeta / determinant / spectral owner | NOT SUPPLIED | No analytic promotion |

The lineage link is the precise replacement of a proper-divisor witness
\(d\mid n\), \(2\le d<n\), by the full network of factor triples
\((d,n/d,n)\), then by coherent fusion/fission in one autonomous mode
equation. This preserves the prime/composite factor observable from the
[prior-work lineage](../../docs/prior_work/README.md), but replaces its
symbolic admissibility implementation. It is not an asserted conjugacy to a
chronological sieve, a Logistic map or a Hénon map. The broadened ANG track
is used explicitly.

The bounded question is: does the frozen equation define a full action, and
does it exclude a periodic source supported on mixed-prime powers? The
strongest supported answer is a global-owner theorem followed by an exact
counterexample to that exclusion. We stop there.

## 2. Frozen definitions and provenance

Write \(w_n=\log n\) and

\[
E=\ell^2(w_n),\qquad Q(z)=\|z\|_E^2=\sum_{n\ge2}w_n|z_n|^2,
\qquad \mathcal M=Q^{-1}(1).
\]

The diagonal group and its generator domain are

\[
(S_tz)_n=n^{-it}z_n,\quad (Lz)_n=w_nz_n,\quad
D(L)=\left\{z:\sum_{n\ge2}w_n^3|z_n|^2<\infty\right\}.
\]

Define the ordered-pair cubic and the two quadratic terms by

\[
\mathcal B(z)=\sum_{a,b\ge2}\frac{\bar z_{ab}z_az_b}{ab},
\qquad C(z)=\operatorname{Re}\mathcal B(z),
\]

\[
A_n(z,y)=\frac1{2n}\sum_{\substack{a,b\ge2\\ab=n}}z_ay_b,
\qquad
D_n(z,y)=\sum_{b\ge2}\frac{z_{nb}\bar y_b}{nb},
\qquad N(z)=A(z,z)+D(z,z).
\]

Here \(D(z,y)\) denotes a sesquilinear term, whereas \(D(L)\) denotes the
generator domain. Both ordered pairs \((a,b)\) and \((b,a)\) occur, and the
case \(a=b\) occurs once as an ordered pair. The candidate equation is

\[
z(t)=S_tz_0-i\int_0^t S_{t-s}N(z(s))\,ds.\tag{1}
\]

The formal ambient two-form and Hamiltonian are
\(\Omega=i\sum dz_n\wedge d\bar z_n\) and \(H=Q+C\).
This does not make the charge shell a symplectic manifold. The audit defines
the action by (1), rather than assuming a globally defined strong vector
field \(-i(Lz+N(z))\) at every point of \(E\).

The coefficient \(1/(ab)\), charge 1 and all-integer dispersion \(\log n\)
are declared design inputs. No prime table, prime-specific parameter, von
Mangoldt weight, zero data or fitted spectrum enters the proofs. In
particular, a frequency \(\log n\) is not a period \(\log n\).

## 3. Full-space estimates and exact resonance

### Lemma 1 — Bounded quadratic terms and a differentiable cubic

Let

\[
U=\sum_{n\ge2}\frac1{n^2},\qquad
V=\sum_{n\ge2}\frac1{n^2\log n}.
\]

Both are finite, and

\[
\|A(z,y)\|_E\le\sqrt{UV/2}\,\|z\|_E\|y\|_E,
\qquad
\|D(z,y)\|_E\le\sqrt{UV}\,\|z\|_E\|y\|_E.\tag{2}
\]

Consequently \(N:E\to E\) is a real-smooth quadratic map, with

\[
\|N(z)-N(y)\|_E
\le K(\|z\|_E+\|y\|_E)\|z-y\|_E,
\quad K=(1+2^{-1/2})\sqrt{UV}.\tag{3}
\]

The cubic is absolutely convergent and real-smooth on \(E\), and

\[
DC(z)[h]=2\operatorname{Re}\sum_{n\ge2}\bar h_nN_n(z).\tag{4}
\]

**Proof.** In normalized coordinates \(x_n=\sqrt{w_n}z_n\), the squared
coefficient norm of the fusion tensor is

\[
\sum_{a,b\ge2}\frac{w_{ab}}{4a^2b^2w_aw_b}
=\frac14\sum_{a,b\ge2}\frac{1/w_a+1/w_b}{a^2b^2}
=\frac{UV}{2}.
\]

The squared coefficient norm of the fission tensor is

\[
\sum_{n,b\ge2}\frac{w_n}{n^2b^2w_{nb}w_b}\le UV.
\]

Viewing these square-summable tensors as Hilbert–Schmidt maps from the
Hilbert tensor product to \(\ell^2\), or applying Cauchy–Schwarz to their
coefficient arrays, proves (2). The input rank-one tensor has norm
\(\|z\|_E\|y\|_E\); complex conjugation in the second term does not change
this norm. Expanding differences gives (3).

For absolute convergence, the same estimates apply to the componentwise
absolute values. Since \(E\) embeds continuously into ordinary \(\ell^2\),
the identity
\(\mathcal B(z)=2\sum_n\bar z_nA_n(z,z)\)
gives an absolutely convergent cubic. Continuous multilinear expansion
therefore differentiates it legitimately. Differentiating both halves of
\(C=(\mathcal B+\overline{\mathcal B})/2\), with the ordered-pair convention,
gives (4). In particular the factor \(1/2\) in fusion and the coefficient 1
in fission are both required. ∎

### Lemma 2 — Resonance and the charge identity

For every \(z\in E\) and \(t\in\mathbb R\),

\[
N(S_tz)=S_tN(z),\qquad
\operatorname{Im}\sum_{n\ge2}w_n\bar z_nN_n(z)=0.\tag{5}
\]

**Proof.** Fusion phases multiply to \((ab)^{-it}\); fission phases obey
\((nb)^{-it}\overline{b^{-it}}=n^{-it}\). This proves equivariance. For the
second identity set \(T_{a,b}=\bar z_{ab}z_az_b\). The weighted pairing is

\[
\frac12\sum_{a,b\ge2}\frac{w_a+w_b}{ab}T_{a,b}
+\sum_{a,b\ge2}\frac{w_a}{ab}\overline{T_{a,b}}
=\frac12\sum_{a,b\ge2}\frac{w_a+w_b}{ab}
       (T_{a,b}+\overline{T_{a,b}}),
\]

which is real. All rearrangements are absolutely convergent: for example
the absolute weighted fusion sum is bounded by
\(\||z|\|_E\|A(|z|,|z|)\|_E\), and the fission sum has the analogous bound.
No assumption \(z\in D(L)\) is used. ∎

## 4. Global ownership on the whole shell

### Theorem 3 — Global mild action

Equation (1) defines a unique global mild solution for every \(z_0\in E\),
in both time directions. The maps \(\Phi_tz_0=z(t)\) form a jointly
continuous action of \(\mathbb R\), preserve \(Q\), and therefore restrict
to a full action on \(\mathcal M\).

**Proof.** The diagonal maps \(S_t\) form a strongly continuous isometric
group on \(E\): strong continuity follows first on finite sequences, then
on all of \(E\) by isometry and norm approximation. Set
\(u(t)=S_{-t}z(t)\). Multiplying (1) by \(S_{-t}\) and using (5) gives the
equivalent integral equation

\[
u(t)=z_0-i\int_0^tN(u(s))\,ds,
\qquad \dot u=-iN(u).\tag{6}
\]

The right-hand side is locally Lipschitz in \(E\) by (3). Picard iteration
is a contraction on a sufficiently short interval in any fixed norm ball,
so (6) has a unique local \(E\)-valued \(C^1\) solution. The continuation
criterion is norm boundedness: on a fixed ball the vector field is bounded
and Lipschitz, hence a solution approaching a finite endpoint is Cauchy in
\(E\), has a limit there, and the same local construction extends it.

Differentiating the continuous quadratic form \(Q\) along (6), not along
an unproved strong solution of (1), gives

\[
\frac{d}{dt}Q(u(t))
=2\operatorname{Re}\sum_nw_n\bar u_n(-iN_n(u))=0
\]

by Lemma 2. Thus \(\|u(t)\|_E=\|z_0\|_E\), which gives global continuation
forward and backward. The transformations between (1) and (6) prove
existence and uniqueness of the global mild solution, and isometry of
\(S_t\) proves charge conservation for it.

Let \(\Psi_t\) be the global action from (6). Equivariance and uniqueness
give \(\Psi_tS_s=S_s\Psi_t\), so
\(\Phi_t=S_t\Psi_t\) obeys
\(\Phi_t\Phi_s=\Phi_{t+s}\). The norm estimates for the local ODE imply
continuous dependence on data on bounded time intervals; together with
strong continuity of \(S_t\), they prove joint continuity. ∎

This constructs the transformation groupoid with objects \(\mathcal M\)
and arrows \((z,t):z\to\Phi_tz\); composition adds times along matching
source/range pairs. No local compactness or groupoid operator algebra is
asserted. Generic \(E\) trajectories are only claimed to be mild for (1).
The strong equation is justified for the explicit domain-valued orbit in
Section 6, not presumed for every point of the shell.

## 5. A genuine source interaction, and its boundary

For a pure-mode state \(z=a e_n\), \(a\ne0\),

\[
N_{n^2}(z)=\frac{a^2}{2n^2}\ne0.
\]

Thus even a pure prime mode immediately generates its square mode. In the
interaction picture the first two derivatives at this state satisfy

\[
\dot u_{n^2}(0)=-\frac{ia^2}{2n^2},\qquad
\dot u_n(0)=0,\qquad
\ddot u_n(0)=-\frac{a|a|^2}{2n^4}.\tag{7}
\]

The last identity follows from the actual fission summand
\(u_{n^2}\bar u_n/n^2\) in \(N_n\). Other first-order terms at the initial
pure mode vanish. The smooth ODE (6) justifies these derivatives. Equation
(7) is a feedback calculation inside the frozen equation, not an external
source schedule; finite support has not been asserted invariant.

Primes have no proper factorization input in the fusion sum, but they still
couple to product modes through fission. That arithmetic distinction alone
does not show prime-exclusive periodicity. The logarithmic dispersion was
chosen to make multiplication resonant, and the decay was chosen as part of
the full equation. Neither choice is a proof that a natural prime-length
flow emerges. Source/scale naturalness remains `OPEN`.

## 6. The exact mixed-prime return discriminator

Let

\[
E_6=\{z\in E:z_n=0\text{ unless }n=6^k,\ k\ge1\}.
\]

This is the precommitted probe subspace, not a replacement carrier.

### Lemma 4 — Invariance and compactness of the cubic test

The full flow preserves \(E_6\). The functional \(C\) is weakly continuous
on every norm-bounded subset of \(E\), hence also of \(E_6\).

**Proof.** Fusion of two powers of 6 is a power of 6. In a nonzero fission
term both \(b=6^j\) and \(nb=6^k\), so \(n=6^{k-j}\) with \(k>j\), because
\(n\ge2\). Thus \(N(E_6)\subset E_6\). The group \(S_t\) preserves it too,
and uniqueness of (6) proves invariance.

In normalized coordinates the cubic tensor has nonzero entries only at
\((ab,a,b)\), of value

\[
c_{a,b}=\frac1{ab\sqrt{w_{ab}w_aw_b}}.
\]

Its squared coefficient sum is bounded by
\(U^2/(2(\log2)^3)<\infty\). Truncate to \(a,b\le R\); the resulting
cubic uses finitely many coordinates (including products up to \(R^2\)),
so is weakly continuous. On \(\|z\|_E\le M\), the error is at most
\(M^3\|c-c^{(R)}\|_{\ell^2}\) by Cauchy–Schwarz on the triple tensor.
It tends uniformly to zero, so \(C\) is weakly continuous there. ∎

### Theorem 5 — A full-model periodic mixed-prime packet

There exists \(u\in E_6\cap\mathcal M\cap D(L)\) and \(\kappa>0\) with

\[
N(u)=\kappa Lu,\qquad
\Phi_tu=S_{(1+\kappa)t}u.\tag{8}
\]

This is a nonconstant periodic point orbit of the full candidate. If

\[
m=\max_{\substack{v\in E_6\\Q(v)\le1}} C(v),\quad
J=\{k\ge1:u_{6^k}\ne0\},\quad d=\gcd J,
\]

then \(m>0\), \(\kappa=3m/2\), and its least physical period is

\[
T=\frac{2\pi}{(1+3m/2)\,d\log6}.\tag{9}
\]

**Proof.** The charge-unit ball of \(E_6\) is weakly compact. Equivalently,
for this separable Hilbert space one can take a coordinatewise convergent
subsequence of a bounded maximizing sequence; the coordinate limit is in
the ball by the sum-of-squares bound, and boundedness plus finite-coordinate
approximation of test vectors gives weak convergence. Lemma 4 makes \(C\)
continuous under that convergence, so it attains its maximum \(m\).

Positivity is explicit. The state

\[
v_6=\frac1{\sqrt{2\log6}},\qquad
v_{36}=\frac1{2\sqrt{\log6}},\qquad v_n=0\ (n\ne6,36)
\]

has \(Q(v)=1\) and
\(C(v)=1/[144(\log6)^{3/2}]>0\), from the pair \((6,6)\).
Thus \(m>0\). A maximizing state \(u\) must lie on \(Q=1\): if
\(0<Q(u)<1\), positive real dilation to the sphere increases the positive
cubic by \(Q(u)^{-3/2}>1\); the zero state cannot maximize.

The real Hilbert sphere is a smooth constraint with nonzero derivative
\(DQ(u)\). The Lagrange multiplier rule gives a real \(\kappa\) satisfying
\(DC(u)=\kappa DQ(u)\) on \(E_6\). Pairing with the radial direction \(u\)
and using cubic homogeneity yields
\(3m=2\kappa\). Applying the derivative equality to real and imaginary
coordinate test directions gives
\(N_{6^k}(u)=\kappa w_{6^k}u_{6^k}\). Both sides are zero off the subspace,
by its invariance, so this is the full coordinate equation in (8).

There is no unresolved domain inference here: Lemma 1 gives \(N(u)\in E\),
and \(\kappa>0\), hence

\[
\sum_nw_n^3|u_n|^2
=\kappa^{-2}\|N(u)\|_E^2<\infty.
\]

Thus \(u\in D(L)\). The curve \(z(t)=S_{(1+\kappa)t}u\) is strongly
differentiable in \(E\). Equivariance and (8) show
\(i\dot z=(1+\kappa)Lz=Lz+N(z)\), so it solves the full strong equation,
hence (1). Theorem 3 supplies uniqueness and identifies it with \(\Phi_tu\).

Because \(Q(u)=1\), its active exponent set \(J\) is nonempty. Every active
coordinate rotates with the positive frequency
\((1+\kappa)k\log6\), so the orbit is nonconstant. A time \(t\) returns
exactly when

\[
\frac{(1+\kappa)t\log6}{2\pi}\,k\in\mathbb Z
\quad\hbox{for every }k\in J.\tag{10}
\]

The gcd \(d\) of a nonempty possibly infinite subset of positive integers
is the gcd of a finite subset: the successive positive gcds eventually
stabilize. Bézout's identity for that finite subset shows that (10) implies
\((1+\kappa)t\log6\,d/(2\pi)\in\mathbb Z\). Conversely this last condition
implies (10), since \(d\mid k\) for every \(k\in J\). The return-time group
is therefore exactly \(T\mathbb Z\), with \(T\) as in (9); (9) is the least
positive period, not just an upper bound. ∎

The symbols \(m,u,d\) are specified by an infinite-dimensional existence
proof, not a claimed numerically evaluated maximum or unique maximizer.
For any chosen maximizing state the displayed formula is its exact least
period. No value of \(d\), uniqueness or full support description is needed
or claimed. The positivity of \(C(u)\) ensures that nonzero interaction
triples are present; this is not a one-mode orbit of the zero-coupling model.

Every active integer \(6^k=2^k3^k\) has both prime factors 2 and 3. Hence
this orbit is contained in no single-prime power source sector, under the
observable fixed in the candidate card. Since the main carrier was never
restricted to \(E_6\), it is an actual packet in that carrier. Calling the
solution a relative equilibrium describes its construction through the
symmetry \(S_t\); its return is an equality of states in \(\mathcal M\),
without any phase quotient.

Traversing this same primitive orbit \(r\) times has time \(rT\). A higher
mode label \(6^{k+r}\), a maximizing state with another support, and an
\(r\)-fold traversal are not interchangeable. All other packet families,
their multiplicities and stability remain `OPEN / NOT CLASSIFIED`.

## 7. Controls and adverse findings

| Control | Exact result or boundary | Consequence |
| --- | --- | --- |
| Zero coupling, a different equation | Pure integer modes would rotate with period \(2\pi/\log n\) | Frequency is not logarithmic orbit length; no linear result is substituted for the nonlinear orbit |
| Pure-mode source in the actual equation | Product generation and factor feedback in (7) | Static-label interpretation refuted; finite support not presumed invariant |
| Prime-power versus mixed-prime support | The \(E_6\) test is invariant and contains the actual periodic packet of Theorem 5 | Exact prime-exclusive source interpretation fails |
| Ownership | Same full shell, coefficient, charge and physical time in Theorems 3 and 5 | No packet selection, changed roof or borrowed flow |
| Cutoff / precision | No orbit integration, truncation stationary point, finite orbit census or precision-dependent claim | Infinite existence follows from uniform tensor tails, not finite evidence |
| `PROVES_TOO_MUCH` | The factor-resonance mechanism also admits the specifically tested composite source | Arithmetic feedback alone is insufficient as a prime selector |

Shuffled-prime or density-matched numerical tests are not run: no prime table
or numerical fit enters the candidate, and the exact composite-sector
counterexample already triggers the precommitted first stop. There is no
attempt to tune away this packet, replace \(\log n\), delete composite
modes, quotient out phases, or construct a trace after that stop.

## 8. Gate assessment, limitations and decision

| Gate | Evidence for `ANG-20260918-MRF01` | Status |
| --- | --- | --- |
| T0 | Full global mild action and its transformation groupoid, norm topology and charge shell | ESTABLISHED at owner level |
| T1 | All-integer factor feedback and exact resonance; no external prime selector | Mechanism ESTABLISHED; source/scale naturalness OPEN; no endogenous prime-length theorem |
| T2 | One actual mixed-prime primitive packet and its exact repetition law | Prime-exclusive target SCOPED FAIL; full ledger NOT CLASSIFIED |
| T3 | No transfer space, trace, zeta or determinant constructed | NOT SUPPLIED / NOT EVALUATED |
| Classical A0–A2 | No finite-dimensional symplectic suspension supplied | NOT APPLICABLE to this carrier; no formal coordinates assigned |
| Formal Route A / Route B | No formal evaluation invoked | UNASSIGNED / NOT INVOKED |

**Decision: `stop / fork`.** The decisive reason is the intrinsic periodic
packet supported on powers of 6, not failure of global well-posedness. The
global-owner and feedback theorems remain positive engineering results, but
they do not accumulate Route credit or repair the failed prime-exclusive
interpretation. A different source interaction or clock would require a new
candidate card; this package authorizes no such repair.

No claim is made about the complete periodic set, enumeration, packet
uniqueness, monodromy, nondegeneracy, invariant measure, locally compact
groupoid framework, trace, quantization, self-adjoint target operator,
completed determinant, zero match or RH. The Hilbert space here is a
classical mode space, not a Hilbert–Pólya spectral realization.

## 9. Evidence, provenance and disclosure

The proofs above are the primary mathematical evidence; all exact inputs are
in the [candidate card](candidate-card.md). The [claim ledger](claim-ledger.md)
maps claims to proofs and limits, and the [evidence index](evidence/README.md)
records the bounded reproducibility/checking contract. Neighboring
[186](../186-multiplicative-bar-clock/README.md),
[193](../193-indecomposable-radial-quotient/README.md) and
[182](../182-nonlinear-two-pair-hamiltonian/README.md) are separate collision
controls identified at freeze, not theorem or operator dependencies.

No empirical data, external dataset or numerical output is used. These
Markdown records make the definitions, proof method and limitations
available in full. No external literature novelty claim is made; source
review here is limited to the repository's frozen contract and lineage.

This is an AI-assisted internal mathematical research record. A separately
dispatched technical check may assess these proofs; it is not external
peer review, and its observed outcome must be recorded separately rather
than inferred from package completion. No venue-specific acceptance criteria
were supplied (`criteria_binding_unavailable`); no submission-readiness
claim is made. No human-subject, personal-data or animal research is involved.
The AI workflow contributed mathematical analysis, drafting and local
verification; it does not assert human authorship or assign CRediT roles to
unidentified people. Human funding and conflict-of-interest declarations
were not supplied and are not fabricated. No publication artifact or
external circulation is produced.

