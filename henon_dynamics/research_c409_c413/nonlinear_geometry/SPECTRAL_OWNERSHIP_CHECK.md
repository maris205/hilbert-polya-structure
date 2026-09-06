# Bounded source-ownership check: logarithmic Dirichlet germs and Gram spectra

Date: 2026-09-06. Independent source check by the nonlinear-geometry reviewer.
This report is not an admission, manuscript, new C-number, or novelty certificate.
Only this report was written; the author's spectral draft was not edited.

## 1. Decision

**NO EXACT DIRECT OWNER CONFIRMED IN THIS BOUNDED CHECK; GENERAL METHOD
OWNERSHIP IS SUBSTANTIAL; KEEP THE COMPLETE TRANSFER STATEMENT AS A CANDIDATE,
NOT AS AN ADMITTED NEW PAPER.**

The four primary sources below do not, in the statements actually read,
assert the proposed implication

`D(rho+u) = -c Log u + holomorphic germ`

`=> N(exp(-L); G) ~ L^2/(2 pi^2)`

for the unrestricted positive, locally finite Dirichlet data in the draft.
That is a bounded negative search result, not a proof that no such result exists.

Conversely, the following are already established mathematical infrastructure:
Gram/Laplace factorization, unitary equivalence modulo kernels, comparison to a
model operator, analytic-kernel low-rank approximation, and variational
stability after a sufficiently small singular-value error. The current
construction should not be described as a new general approximation method.
Webb's June 2026 revision is particularly relevant and must not be omitted.

My earlier mathematical review remains valid conditionally on external input W.
This check narrows the possible contribution to the **assembled, precisely
quantified logarithmic-germ-to-Gram transfer theorem**, if a further editorial
assessment considers that a sufficiently independent question. It does not
support separate papers for the analytic lemma, prime/AP application, density
independence, or determinant corollary.

## 2. Exact target and comparison scale

The inspected target is `spectral/PROOF_DRAFT.md`, Sections 1–5, as present on
2026-09-06. Its important quantitative step is the following lemma:

- R is holomorphic on `{Re u>0} union {|u|<r}`.
- For every eta>0, `|R(u)| <= C_eta exp(-d Re u)` on `Re u>=eta`, with fixed d>0.
- The integral Hankel operator with kernel `R(x+y)` satisfies
  `N_s(exp(-L); H_R) = O(L log L)`.

Only `o(L^2)` is needed for the leading spectral transfer. Thus a source proving
only membership in every Schatten class does not directly finish the argument;
neither does a fixed upper bound `s_n <= C exp(-c sqrt(n))`, which gives only
`N_s(exp(-L)) = O(L^2)`. A uniform or improvable constant could change that
assessment, but it must actually be established rather than assumed.

The relevant distinction is between a logarithmic singularity of an **integral
kernel near time zero** and a logarithmic singularity of a **Hardy-space
symbol on the unit circle**. Their displayed spectral scales need not coincide.

## 3. Four closest primary owners actually inspected

| Primary source | Statements/sections actually read | Direct ownership of target? |
| --- | --- | --- |
| Miheisi–Pushnitski, *A Helson matrix with explicit eigenvalue asymptotics*, JFA (2018), arXiv:1709.06326 | Sections 1.4–1.7; Theorem 2.1; Lemmas 2.2–2.4 and their proofs; final use in Section 4 | Owns the closely related Gram/Dirichlet-kernel reduction, with an all-Schatten error. Not the claimed logarithmic scale. |
| Pushnitski–Yafaev, *Localization principle for compact Hankel operators*, JFA 270 (2016), 3591–3621, arXiv:1508.04279v2 | Introduction; Theorem 1.1; Lemma 2.1; Theorem 2.2 and proof; continuous version Theorem 2.6 | Owns localization and perturbation in the power scale. Its remainder class does not directly settle this scale. |
| Blower, *Hankel operators that commute with second-order differential operators*, JMAA (2008), arXiv:0712.1013 | Introduction; Section 6, especially Theorem 6.1, its proof, and Proposition 6.3 | Owns analytic-half-plane rapid-decay results. The stated conclusions do not supply this lemma or transfer. |
| Webb, *Low-rank approximation of analytic kernels*, arXiv:2509.14017v4, revised 2026-06-17 | Setup and Theorem 1.1; Cauchy–Zolotarev definitions; Theorem 3.3; Section 6.2 log-Cauchy example | Strong general owner of analytic-kernel low-rank approximation. The target still requires the unbounded-domain/germ/tail assembly. |

### 3.1 Miheisi–Pushnitski: Dirichlet kernel and Gram mechanism

Theorem 2.1 assumes a bounded, nonnegative, compactly supported weight w and
`a(t)=integral t^(-1/2-lambda) w(lambda) dlambda`. It identifies the associated
discrete and integral Helson operators, modulo kernels, with self-adjoint
operators whose difference lies in `S_0 = intersection_(p>0) S_p`.
Lemma 2.2 passes through the weighted kernel
`sqrt(w(x)) zeta(1+x+y) sqrt(w(y))`; Lemma 2.3 subtracts a weighted Carleman
kernel; Lemma 2.4 uses the standard `T*T` / `TT*` equivalence.
[Primary preprint](https://arxiv.org/pdf/1709.06326).

**Delta:** the draft's unrestricted positive Dirichlet sequence and logarithmic
germ are different hypotheses. More importantly, this source's declared
negligibility is super-polynomial, not `o(L^2)` on the inverse-log counting
scale. Its phrase about agreement to all orders must be read in that setting,
not promoted to arbitrary stretched-exponential spectral equivalence.
The elementary Gram maneuver is not a novel ingredient here.

### 3.2 Pushnitski–Yafaev: localization at a different spectral scale

Theorem 1.1 treats bounded symbols on the unit circle with mutually disjoint
singular supports. For each fixed p>0 it compares the limits of
`n s_n(H(omega))^p` to the individual contributions. Theorem 2.2 is the abstract
operator version, with cross-products negligible in weak Schatten classes;
Theorem 2.6 transports the principle to the real-line Hardy representation.
The introduction expressly identifies the power scale.
[Primary preprint, v2](https://arxiv.org/pdf/1508.04279v2).

**Delta:** substituting a square-root-exponential sequence makes these
power-normalized limits zero. Consequently these statements give no nonzero
coefficient for `N(exp(-L))/L^2`, and their smooth-error hypothesis alone
does not justify the proposed transfer. Nevertheless, the conceptual
localize–compare–perturb organization has a clear prior owner.

### 3.3 Blower: analytic half-plane decay, not the claimed counting estimate

Theorem 6.1 assumes analyticity throughout a shifted half-plane
`Re z > -delta` and a global bound on `phi(z) exp(epsilon z)` there.
Its conclusion is `j^p s_j -> 0` for every positive integer p, together with
an order-zero determinant statement. Proposition 6.3 instead assumes a
two-sided strip with exponential decay and states an upper bound
`s_N <= C exp(-kappa N^(1/3))`.
[Primary preprint, Section 6](https://arxiv.org/pdf/0712.1013).

**Delta:** the draft does not require continuation across the entire imaginary
axis: only a disk at zero is added to the right half-plane. More importantly,
the source's stated conclusions do not yield `N_s(exp(-L))=O(L log L)` or
even the required little-o estimate. I have not silently optimized its
fixed-order intermediate inequalities or asserted a stronger theorem than
the source states. Its analytic-Cauchy/Laguerre approximation technique is
relevant prior art, not a direct exact owner found here.

### 3.4 Webb: strongest general approximation owner in the search

Theorem 1.1 works with compact D and E, Radon measures, and kernels continuous
on `D x E` that continue analytically in one variable outside a closed
singular set F. It bounds a rank-n approximation in operator norm using a
Cauchy–Zolotarev number and a dual-operator norm. Theorem 3.3 recalls the
separated-interval bound `4 exp[-pi^2 n/log(16 gamma)]`. Section 6.2 applies
the framework to `log(x+y)` on `[c,d]`, with `0<c<d<infinity`.
[Primary preprint, v4](https://arxiv.org/pdf/2509.14017v4).

**Delta:** the actual theorem is not confined to finite matrices, but its stated
setup is compact; do not dismiss it merely as numerical linear algebra.
It does not itself assert the infinite-half-line logarithmic-germ transfer.
To apply it here one must control the analytic approximation constants across
growing truncations and the tail. The draft does that through elementary
dyadic Taylor pieces. This is a legitimate proof step, but not persuasive
evidence of a new general low-rank principle. The risk of a short corollary
of general approximation theory is real.

## 4. Rational approximation and other screened leads

Pushnitski–Yafaev's *Best rational approximation of functions with logarithmic
singularities* was also checked at its actual statements: Proposition 2.7
records the AAK singular-value/approximation-distance connection; Theorems
3.3 and 3.5 give power-law asymptotics; Theorem 3.8 treats analytic functions
with boundary logarithmic powers. These are not the same object as an
integral kernel `-log(t+s)` near `(0,0)`. AAK is a bridge, not an automatic
root-exponential asymptotic theorem.
[Primary preprint](https://arxiv.org/pdf/1601.00882).

Two further safeguards against overclaiming search coverage:

- Opmeer's 2010 analytic-control-system result states all-Schatten membership.
  His 2015 ECC result announces square-root-exponential upper bounds for
  Gramians and Hankel singular values. The latter's full theorem pages were
  not retrieved in this check; I used its institutional abstract only as a
  lead, not as a fully audited exclusion or direct theorem dependency.
  [2010 publisher page](https://www.sciencedirect.com/science/article/abs/pii/S0167691110000964),
  [2015 institutional record](https://researchportal.bath.ac.uk/en/publications/decay-of-singular-values-of-the-gramians-of-infinite-dimensional-/).
- Guiver's 2024-online/2025-volume *Regularity and Compactness Properties of
  Integral Hankel Operators and Their Singular Vectors*, Theorem 2.3, was
  inspected. It concerns compactness on function spaces and regularity of
  singular vectors, not the target eigenvalue asymptotic.
  [Primary article](https://link.springer.com/article/10.1007/s11785-024-01627-w).

Searches included general analytic-Hankel decay, rational approximation of
logarithmic singularities, unbounded analytic kernels, and 2025–2026
low-rank/spectral variants. Search failures and abstract-only access are not
treated as evidence of nonexistence. No PDFs were saved locally.

## 5. What remains defensible, and what does not

The strongest defensible description is provisional:

> A logarithmic Dirichlet-germ criterion transfers a classical Hankel
> eigenvalue law to a class of positive discrete Gram operators; an explicit
> analytic remainder estimate verifies the perturbation scale.

This should be accompanied by the close Gram/Helson and analytic-approximation
sources, and by a clearly external Widom model law. It should not say that
the Gram factorization, the logarithmic model law, analytic low-rank
approximation, or spectral stability is newly discovered.

The full spectral asymptotic still differs from a bare application of positivity:
the needed remainder estimate has actually been proved in the draft. But
that observation alone does not establish enough originality or substance for
an independent paper. A decision to proceed must be about the whole theorem
and the mathematical question it answers, not the existence of an elementary
technical lemma missing verbatim from a few searched papers.

**Bounded handoff:** no source found here compels immediate rejection as an
exact already-stated theorem. Equally, this report does not clear a broad
novelty/admission gate. Preserve the proof candidate, record substantial
method ownership, and let the root's nonauthor gate decide its standalone
value. The original Widom text/coefficient check is deliberately outside this
report; the root is handling that dependency, including the accessible
Tantalakis report and the conflicting public PY coefficient.
