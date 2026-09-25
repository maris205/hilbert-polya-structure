# Unavoidable periodic power sectors in bounded symmetric multiplicative flows

**Paper ID:** `234-multiplicative-sector-obstruction`  
**Audit ID:** `ANG-AUDIT-20260918-MSO01`  
**Date / status:** 2026-09-18; `CLASS OBSTRUCTION ESTABLISHED — STOP COEFFICIENT TUNING / FORK`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

We audit every fixed bounded real symmetric coefficient array in the
factor-interaction class frozen for this paper. Each array defines its own
flow on the entire all-integer charge shell, rather than a common flow
assembled from favorable sectors. Uniform weighted tensor estimates and
charge conservation give a unique global mild action. For every integer
\(q\ge2\), the complete power sector \(E_q\) is invariant and contains an
actual nonconstant periodic orbit of that full action. If the cubic
interaction is nonzero on the sector, odd homogeneity and weak compactness
produce a positive maximizer; its Euler equation proves generator-domain
regularity and a rotating strong solution. If the cubic vanishes identically,
the restricted nonlinear vector field vanishes too and a pure-mode linear
orbit gives the return. Thus no bounded real symmetric coefficient choice,
including zero or sign-changing arrays, removes the mixed-prime periodic
packet in \(E_6\). This is a scoped obstruction to coefficient tuning within
the frozen class, not a theorem against all arithmetic nonlinear flows.
No periodic-packet count, trace, determinant, natural arithmetic clock or
Route result is supplied.

## 1. Frozen class and same-object ledger

The [version-1 audit card](candidate-card.md) predates this proof and is
unchanged. This is a universal theorem about a specified class, not a new
single candidate or a revision of
[233, ANG-20260918-MRF01](../233-multiplicative-resonant-flow/paper.md).
An arbitrary coefficient array is fixed before proving its action and
periodic orbit. The quantifiers are

\[
\text{for every admissible }\theta\text{ and every }q\ge2,
\quad\text{there exists a periodic point of that same }\Phi^\theta.
\]

They do not mean that one point or one period works for all arrays.

| Item | Frozen owner for a fixed array \(\theta\) | Result / boundary |
| --- | --- | --- |
| Carrier | Full norm-topological shell \(\mathcal M=\{Q=1\}\subset E\) | Never restricted to a selected sector |
| Action | Mild equation (2) with that array and all integer modes | Global action proved below |
| Arithmetic mechanism | Ordered factor triples \((a,b,ab)\) with coefficients \(\theta_{a,b}/(ab)\) | Retains the factor relation; feedback may vanish for a degenerate array |
| Clock | Physical time in (2), with \(S_tz=(n^{-it}z_n)\) | Not replaced by a roof or a phase quotient |
| Packets | All nonconstant primitive point orbits modulo actual time translation | Existence and least period for a witness, not a complete count |
| Repetitions | Repeated traversal of the same primitive point orbit | Times \(rT\), \(r\in\mathbb N\) |
| Classical base map / suspension | NOT APPLICABLE to this infinite-dimensional class | No finite-dimensional symplectic claim |
| Trace / zeta / determinant / quantum object | NOT SUPPLIED | No owner transferred from another paper |

The preserved prior-work arrow is proper-divisor symbolic data to the full
network of factor triples, then to autonomous coherent factor/product
interaction. It is the explicitly declared replacement of symbolic
admissibility in 233, not a conjugacy to a chronological sieve, Logistic
map or Hénon map. The connection is to the prime/composite factor observable
in the [prior-work lineage](../../docs/prior_work/README.md). Naturalness
of the logarithmic dispersion and coefficient design remains `OPEN`.

## 2. Question, definitions and claim boundary

The question is whether replacing the coefficients in 233 can remove its
mixed-prime return while retaining every mode, the charge shell and the
physical clock. The answer is negative for the complete frozen class.

Let \(w_n=\log n\), and let \(\theta=(\theta_{a,b})_{a,b\ge2}\) be any
fixed real symmetric array with \(|\theta_{a,b}|\le1\). Write

\[
E=\ell^2(w_n),\quad Q(z)=\|z\|_E^2=\sum_{n\ge2}w_n|z_n|^2,
\quad \mathcal M=Q^{-1}(1),
\]

\[
(S_tz)_n=e^{-itw_n}z_n,\quad (Lz)_n=w_nz_n,\quad
D(L)=\left\{z:\sum_{n\ge2}w_n^3|z_n|^2<\infty\right\}.
\]

Define the continuous bilinear and sesquilinear terms, justified below, by

\[
(A_\theta(z,y))_n=\frac1{2n}\sum_{ab=n}\theta_{a,b}z_ay_b,
\quad
(D_\theta(z,y))_n=\sum_{b\ge2}\frac{\theta_{n,b}}{nb}z_{nb}\bar y_b,
\]

\[
N_\theta(z)=A_\theta(z,z)+D_\theta(z,z),\quad
B_\theta(z)=\sum_{a,b\ge2}\frac{\theta_{a,b}}{ab}\bar z_{ab}z_az_b,
\quad C_\theta=\operatorname{Re}B_\theta. \tag{1}
\]

Both \((a,b)\) and \((b,a)\) occur in the ordered sums; the diagonal
pair occurs once. The full equation is

\[
z(t)=S_tz_0-i\int_0^t S_{t-s}N_\theta(z(s))\,ds. \tag{2}
\]

Its action is denoted \(\Phi^\theta_t\). The formal ambient weak two-form
\(i\sum dz_n\wedge d\bar z_n\) and Hamiltonian \(Q+C_\theta\) motivate
(2), but no symplectic structure on the charge shell or strong equation at
every point of \(E\) is assumed. The mild equation owns the flow.

The allowed inputs are exactly the all-integer factor relation, \(\log n\),
charge normalization 1 and the fixed bounded symmetric array. No prime
table, von Mangoldt weight, Riemann-zero data, time-dependent schedule or
per-prime fitted parameter is used. The prime-support criterion is the
one frozen in the card: a packet should have support contained in
\(\{p^k:k\ge1\}\) for one ordinary prime \(p\). This audit disproves
that exclusion of mixed-prime packets throughout the class; it does not
assert that this criterion follows from a general trace formula.

## 3. Layer 1: uniform full-space control

### Lemma 1 — Quadratic bounds and the cubic differential

Set

\[
U=\sum_{n\ge2}n^{-2},\qquad
V=\sum_{n\ge2}(n^2w_n)^{-1},\qquad
K=(1+2^{-1/2})\sqrt{UV}.
\]

These constants are finite and independent of \(\theta\). For all
\(z,y\in E\),

\[
\|A_\theta(z,y)\|_E\le\sqrt{UV/2}\,\|z\|_E\|y\|_E,
\quad
\|D_\theta(z,y)\|_E\le\sqrt{UV}\,\|z\|_E\|y\|_E, \tag{3}
\]

\[
\|N_\theta(z)-N_\theta(y)\|_E
\le K(\|z\|_E+\|y\|_E)\|z-y\|_E. \tag{4}
\]

The cubic is absolutely convergent and real-smooth on \(E\), and

\[
DC_\theta(z)[h]=2\operatorname{Re}\sum_{n\ge2}\bar h_nN_{\theta,n}(z).
\tag{5}
\]

**Proof.** In coordinates \(x_n=\sqrt{w_n}z_n\), the sum of squared
fusion tensor coefficients is at most

\[
\sum_{a,b\ge2}\frac{w_{ab}}{4a^2b^2w_aw_b}
=\frac14\sum_{a,b\ge2}\frac{1/w_a+1/w_b}{a^2b^2}
=UV/2.
\]

The corresponding fission sum is at most

\[
\sum_{n,b\ge2}\frac{w_n}{n^2b^2w_{nb}w_b}\le UV.
\]

Cauchy–Schwarz on the tensor coefficients and the rank-one input tensor
proves (3); complex conjugation does not change the input norm. Bilinear
and sesquilinear difference expansions prove (4). The same majorants
applied to componentwise absolute values show absolute convergence of
\(B_\theta(z)=2\sum_n\bar z_n A_{\theta,n}(z,z)\), since
\(E\hookrightarrow\ell^2\). Continuous multilinear expansion therefore
permits differentiation. Real symmetry of \(\theta\), the two ordered
factor positions and \(C_\theta=(B_\theta+\bar B_\theta)/2\) yield
(5). These facts also prove real smoothness. ∎

### Lemma 2 — Resonance and charge conservation identity

For every \(z\in E\) and \(t\in\mathbb R\),

\[
N_\theta(S_tz)=S_tN_\theta(z),\qquad
\operatorname{Im}\sum_nw_n\bar z_nN_{\theta,n}(z)=0. \tag{6}
\]

**Proof.** The fusion phase is \((ab)^{-it}\), and the fission phase
is \((nb)^{-it}b^{it}=n^{-it}\). For the second identity put
\(T_{a,b}=\bar z_{ab}z_az_b\). The weighted pairing is

\[
\frac12\sum_{a,b}\frac{\theta_{a,b}(w_a+w_b)}{ab}T_{a,b}
+\sum_{a,b}\frac{\theta_{a,b}w_a}{ab}\overline{T_{a,b}}
=\frac12\sum_{a,b}\frac{\theta_{a,b}(w_a+w_b)}{ab}
 (T_{a,b}+\overline{T_{a,b}}),
\]

which is real. The second equality uses real symmetry. Absolute
convergence follows from the weighted Cauchy–Schwarz pairing with the
absolute-value versions of (3), so no generator-domain assumption is
needed to rearrange these sums. ∎

## 4. Layer 2: global ownership, without a cutoff

### Theorem 3 — Global full-shell action for every array

For every admissible \(\theta\), equation (2) has a unique global mild
solution through every \(z_0\in E\), in both time directions. It gives
a jointly continuous action \(\Phi^\theta\) preserving \(Q\), and
hence an action on the entire shell \(\mathcal M\).

**Proof.** The diagonal maps \(S_t\) form a strongly continuous
isometric group on \(E\). Strong continuity first holds on finite
sequences and extends by norm approximation and isometry. The interaction
variable \(u(t)=S_{-t}z(t)\) transforms (2), using (6), exactly into

\[
u(t)=z_0-i\int_0^tN_\theta(u(s))\,ds,\qquad
\dot u=-iN_\theta(u). \tag{7}
\]

By (4), Picard iteration gives a unique local \(C^1\), \(E\)-valued
solution. On a bounded norm ball the vector field is bounded and
Lipschitz. Thus a solution at a finite maximal endpoint would be Cauchy
in \(E\) if its norm stayed bounded; its limit could be used as new
initial data, extending the solution.

Differentiation of the continuous quadratic form \(Q\) along (7) is
legitimate and gives, by (6),

\[
\frac{d}{dt}Q(u)=2\operatorname{Re}\sum_nw_n\bar u_n(-iN_{\theta,n}(u))=0.
\]

The norm is constant, so the continuation argument works forward and
backward for all time. The equivalence of (7) and (2), together with
isometry of \(S_t\), proves the claimed mild well-posedness and charge
conservation. If \(\Psi^\theta_t\) is the ODE action, uniqueness and
equivariance imply \(\Psi^\theta_tS_s=S_s\Psi^\theta_t\). Consequently
\(\Phi^\theta_t=S_t\Psi^\theta_t\) is an action. The local Lipschitz
bound gives continuous dependence on bounded time intervals; strong
continuity of \(S_t\) then gives joint continuity. ∎

For each array this proves its transformation-groupoid owner, with arrows
\((z,t):z\to\Phi^\theta_tz\). No local compactness, Haar system or
groupoid operator algebra is inferred. This layer is a positive ownership
result even for arrays whose arithmetic interaction is degenerate.

## 5. Layer 3: invariant power sectors and an attained extremum

For a fixed integer \(q\ge2\), define the closed subspace

\[
E_q=\{z\in E:z_n=0\text{ unless }n=q^k,\ k\ge1\},
\quad
m_q(\theta)=\max_{\substack{v\in E_q\\Q(v)\le1}}C_\theta(v). \tag{8}
\]

This is a probe inside the full carrier, not its replacement.

### Lemma 4 — Sector invariance, weak continuity and the zero dichotomy

The subspace \(E_q\) is invariant under the full action. The maximum
in (8) exists, \(m_q(\theta)\ge0\), and precisely one of these cases holds:

1. \(C_\theta|_{E_q}\not\equiv0\), in which case \(m_q(\theta)>0\).
2. \(C_\theta|_{E_q}\equiv0\), in which case
   \(N_\theta|_{E_q}\equiv0\) and \(m_q(\theta)=0\).

**Proof.** Fusion of powers of \(q\) is a power of \(q\). For a
nonzero fission term at a state in \(E_q\), both \(b=q^j\) and
\(nb=q^k\), whence \(n=q^{k-j}\) with \(k>j\) because \(n\ge2\).
Thus \(N_\theta(E_q)\subset E_q\); \(S_t\) preserves \(E_q\) too.
Uniqueness for (7) proves full-flow invariance.

In normalized coordinates, the cubic tensor has entries

\[
c_{a,b}=\frac{\theta_{a,b}}{ab\sqrt{w_{ab}w_aw_b}}
\quad\text{at positions }(ab,a,b),
\qquad
\sum_{a,b}|c_{a,b}|^2\le\frac{U^2}{2(\log2)^3}<\infty. \tag{9}
\]

Truncating \(a,b\le R\) yields a polynomial in finitely many
coordinates, which is weakly continuous. On \(\|z\|_E\le M\), the
tail is at most \(M^3\|c-c^{(R)}\|_{\ell^2}\), by Cauchy–Schwarz
against the threefold tensor of normalized coordinates. This tends
uniformly to zero. Hence \(C_\theta\) is weakly continuous on bounded
subsets of \(E\), including the unit ball of \(E_q\).

For completeness, a maximizing sequence in this ball has a coordinatewise
convergent subsequence by a diagonal selection. Its limit belongs to the
ball by the finite partial-sum bound. The subsequence converges weakly:
pair against a finite-coordinate approximation to any \(E_q\) test
vector and bound both tails by the uniform norm bound. The established
weak continuity therefore gives an attained maximum.

The cubic is odd under real negation:
\(C_\theta(-v)=-C_\theta(v)\). If it is not identically zero on
\(E_q\), change the sign of a nonzero test value and dilate to the
unit ball to obtain a positive value. Thus \(m_q>0\). Conversely,
\(m_q=0\) forces the cubic to vanish on the ball by oddness and then
on all of \(E_q\) by real homogeneity.

Finally, if this restriction vanishes, its derivative in every direction
\(h\in E_q\) is zero. Invariance puts \(N_\theta(v)\) in \(E_q\).
Taking \(h=N_\theta(v)\) in (5) gives
\(0=2\sum_n|N_{\theta,n}(v)|^2\). This sum is finite since
\(N_\theta(v)\in E\hookrightarrow\ell^2\). Hence the entire
nonlinear vector at every sector state vanishes, including its components
outside the sector. ∎

No sign condition on the array was used to get \(m_q>0\). In particular,
negative or sign-changing coefficients do not invalidate the argument.
No claim that \(m_q\) is bounded below uniformly over all arrays is made;
the zero array is explicitly part of the second branch.

## 6. Layer 4: actual strong periodic orbits in both branches

### Theorem 5 — A periodic witness in every power sector

For every admissible \(\theta\) and every integer \(q\ge2\), there
are \(u\in E_q\cap\mathcal M\cap D(L)\) and \(\kappa\ge0\) such that

\[
N_\theta(u)=\kappa Lu,\qquad
\Phi^\theta_tu=S_{(1+\kappa)t}u. \tag{10}
\]

This is a nonconstant actual periodic point orbit, not a phase-quotient
return. If \(J=\{k\ge1:u_{q^k}\ne0\}\) and \(d=\gcd J\), its least
physical period is

\[
T=\frac{2\pi}{(1+\kappa)d\log q}. \tag{11}
\]

When \(m_q(\theta)>0\), one may take any positive maximizer of (8) and
\(\kappa=3m_q(\theta)/2>0\). When \(m_q(\theta)=0\), one may take
\(u=e_q/\sqrt{\log q}\), \(\kappa=0\), \(d=1\), so
\(T=2\pi/\log q\).

**Proof, nonzero branch.** Let \(u\) maximize (8) at \(m_q>0\).
It lies on \(Q=1\): the zero vector cannot maximize, and a positive
real dilation from a point with \(0<Q(u)<1\) to the sphere increases
the positive cubic by the factor \(Q(u)^{-3/2}>1\).

We justify the multiplier directly on the real Hilbert space \(E_q\).
For every tangent vector \(h\) with
\(\operatorname{Re}\langle u,h\rangle_E=0\), differentiate the
sphere curve \((u+sh)/\|u+sh\|_E\) at zero. Maximality gives
\(DC_\theta(u)[h]=0\). Every direction splits into such a tangent
vector and a real multiple of \(u\); radial differentiation gives
\(DC_\theta(u)[u]=3m_q\) and \(DQ(u)[u]=2\). Therefore

\[
DC_\theta(u)=\kappa DQ(u)\text{ on }E_q,
\qquad \kappa=3m_q/2>0. \tag{12}
\]

Testing (12) on the real and imaginary coordinate directions, using (5),
yields \(N_{\theta,q^k}(u)=\kappa w_{q^k}u_{q^k}\). Outside the
sector both sides vanish by Lemma 4. This proves the full coordinate
equation in (10), without having assumed that \(Lu\in E\).
The latter now follows from that equation and Lemma 1:

\[
\sum_nw_n^3|u_n|^2=\kappa^{-2}\|N_\theta(u)\|_E^2<\infty. \tag{13}
\]

Thus \(u\in D(L)\). The curve \(z(t)=S_{(1+\kappa)t}u\) is strongly
differentiable in \(E\), since its generator-domain norm is finite.
Equivariance gives
\(N_\theta(z(t))=\kappa Lz(t)\), and hence
\(i\dot z=(1+\kappa)Lz=Lz+N_\theta(z)\). Variation of constants
shows that it solves (2); uniqueness in Theorem 3 identifies it with
\(\Phi^\theta_tu\).

**Proof, zero branch.** Lemma 4 gives \(N_\theta(v)=0\) for every
\(v\in E_q\). Set \(u=e_q/\sqrt{\log q}\). This finite-support
state belongs to \(D(L)\) and has \(Q(u)=1\). The curve \(S_tu\)
stays in \(E_q\), solves the full strong and mild equations, and is
the actual full-flow orbit by uniqueness. This proves (10) with
\(\kappa=0\), without dividing by a zero multiplier.

**Least period in both branches.** The support set \(J\) is nonempty
because \(Q(u)=1\). At least one active coordinate rotates with
nonzero frequency \((1+\kappa)k\log q\), so the orbit is nonconstant.
A time \(t\) returns exactly when

\[
\frac{(1+\kappa)t\log q}{2\pi}\,k\in\mathbb Z
\quad\text{for every }k\in J. \tag{14}
\]

The gcd of a nonempty, possibly infinite subset of positive integers is
the gcd of a finite subset: along an enumeration, successive positive
gcds eventually stabilize. Bézout's identity for that finite subset
shows that (14) implies
\((1+\kappa)t\log q\,d/(2\pi)\in\mathbb Z\). Conversely this
condition implies (14), since \(d\) divides every active exponent.
The exact return group is \(T\mathbb Z\), with \(T\) in (11).
In the zero branch \(J=\{1\}\). Thus (11) is a least positive
period in both cases. ∎

### Corollary 6 — Coefficient tuning cannot remove mixed-prime packets

Every fixed array in the frozen class has a nonconstant primitive periodic
packet whose support is contained in \(\{6^k:k\ge1\}\). None of its
active mode labels is a power of a single prime: each is divisible by both
2 and 3. Consequently the prime-support target fails for every array.

**Proof.** Apply Theorem 5 with \(q=6\). Its least-period orbit is one
primitive point orbit in the full shell, and every active integer is
\(6^k=2^k3^k\). No state selection or phase identification is made. ∎

This corollary needs only one witness, not a full classification. In
particular, the existence theorem for every \(q\) does not count one
distinct packet per integer. Sectors can be nested:
\(E_{q^r}\subset E_q\), and one orbit can lie in several named
sectors. Relabeling that orbit by \(q^r\) does not create a new packet
or a repeated traversal. The primitive orbit in (11) is defined by actual
time translation; its \(r\)-fold traversal has time \(rT\).

## 7. Controls, adverse findings and exact limits

| Control | Result for the frozen class | Interpretation |
| --- | --- | --- |
| \(\theta_{a,b}=1\) | Nonzero branch; recovers the variational mechanism of 233 for \(q=6\) | A scoped extension, not inherited proof credit |
| \(\theta_{a,b}=0\) | Nonlinear term vanishes globally; pure mode \(q\) has least period \(2\pi/\log q\) | Zero coupling still has mixed-prime periodic modes |
| Sign-changing or wholly negative coefficients | Either branch of Lemma 4 applies; oddness supplies a positive value whenever the cubic is nonzero | Positivity of individual coefficients is unnecessary |
| Vanishing within-sector coefficients \(\theta_{q^j,q^k}=0\) | Cubic and nonlinear vector vanish throughout \(E_q\), even if other coefficients are nonzero | Off-sector coupling cannot drive a state out of this invariant sector |
| Nonzero cubic with arbitrarily small norm | Positive maximizer exists, with possibly arbitrarily small \(\kappa>0\) | No quantitative lower bound or uniform maximizer asserted |
| Full ownership | Same array, shell, mode set, physical clock and equation in Theorems 3 and 5 | Sector used as a probe, not a replacement main object |
| Cutoff / precision | No numerical experiment, finite orbit census or truncation eigenvector | Uniform tensor tails justify the infinite-dimensional proof |
| \(q\) versus \(q^r\) | Sectors overlap; packet counts are not inferred from labels | No overcounting or false repetition law |
| `PROVES_TOO_MUCH` | Every integer power sector, including mixed-prime sectors, contains a periodic witness | This resonance-plus-compact-cubic architecture is not a prime selector |

The theorem assumes all frozen ingredients: real symmetric bounded
coefficients, the specified factor-only quadratic structure, its fixed
decay, the charge shell, and logarithmic resonant dispersion. It does not
exclude nonsymmetric or time-dependent systems, other interactions,
different carriers, noncompact variational problems or any model obtained
by changing these assumptions. Such changes are outside this audit and
need new candidate cards; leaving the class is not evidence of success.
No different model is constructed or authorized here.

The full periodic set, multiplicities, maximizer uniqueness, active gcd,
stability, nondegeneracy and monodromy remain unclassified. Naturalness and
an endogenous prime-length theorem remain open. The displayed \(m_q,u,d\)
are exact variational quantities, not claimed numerical values.

## 8. Gate assessment and decision

| Gate | Result for `ANG-AUDIT-20260918-MSO01` | Boundary |
| --- | --- | --- |
| T0 | Global full-shell owner ESTABLISHED for each fixed class member | No classical finite-dimensional symplectic claim |
| T1 | Factor structure and resonance fixed; naturalness OPEN | Genuine feedback is not universal: the zero array is allowed |
| T2 | Actual primitive witness and repetition law ESTABLISHED; prime-support target SCOPED FAIL for every member | Complete packet classification NOT SUPPLIED |
| T3 | NOT SUPPLIED / NOT EVALUATED | No analytic or quantum object introduced |
| Classical A0–A2 | NOT APPLICABLE to this broadened audit | Formal coordinates UNASSIGNED |
| Formal Route A / Route B | UNASSIGNED / NOT INVOKED | No formal evaluation performed |

**Decision: `stop coefficient tuning / fork`.** The decisive gate reason
is not insufficient estimates or failure to solve the infinite-dimensional
equation. Those layers are established. It is the unavoidable mixed-prime
periodic packet, including the degenerate zero-interaction case. Within
this class, changing bounded symmetric coefficients cannot fix the target.

The next missing structural layer is a mechanism that can exclude mixed
returns in the full carrier while retaining an independently justified
physical arithmetic clock. A possible future architecture must break at
least one stated hypothesis of this theorem and explain why the change
still follows the prime-symbolic lineage. That is a requirement for a new
screen, not a claim that a successful fork already exists.

## 9. Evidence, provenance and disclosure

The primary evidence is the complete derivation above, with exact inputs
in the [frozen card](candidate-card.md), claims separated in the
[claim ledger](claim-ledger.md), and reproducibility details in the
[evidence index](evidence/README.md). Paper 233 is a source of the narrower
construction and an exact \(\theta=1\) control; this proof explicitly
rechecks the changed coefficient class and its additional zero branch.
No external literature priority or novelty claim is made.

Data availability: there are no empirical data, external datasets or
numerical outputs; all definitions, proofs and limitations are in this
Markdown package. No PDF, LaTeX, publication artifact or external upload
is produced. This is an AI-assisted internal mathematical record, not a
venue submission or a full journal workflow. Any separately dispatched
technical review has its observed outcome recorded separately; review by
another model execution is not external peer review. Venue-specific
criteria were not supplied (`criteria_binding_unavailable`), and no
submission-readiness claim is made.

Ethics: no human-subject, personal-data or animal research is involved.
The AI workflow contributed mathematical analysis, drafting and local
verification. Human authorship and CRediT allocations were not supplied
and are not invented. Funding acknowledgments and conflict-of-interest
declarations for human authors were not supplied; both remain undeclared,
not certified absent.
