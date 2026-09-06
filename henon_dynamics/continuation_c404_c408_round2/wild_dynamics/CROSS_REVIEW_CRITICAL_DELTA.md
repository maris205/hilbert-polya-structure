# Independent internal review: critical harmonic delta-chain theorem

Status: `MATH_PASS_PENDING_SOURCE_OWNERSHIP_GATE`.

Blocking mathematical defects found: **0**. Required mathematical fixes: **0**.

This is an independent internal proof review, not an external-referee report,
a publication-priority certificate, or formal admission of a numbered result.
The research-review skill was used as a critical-review framework. No external
review API, numerical eigenvalue run, or large census was used. The reviewer
has not edited any file in the candidate author's `critical_delta` directory.

## 1. Reviewed artifact and claim

The complete 402-line `critical_delta/PROOF_PACKAGE.md` was read and checked.
Its SHA-256 at review is

    5ae8f666d9fe091ce40ff4317aa7acc6a0f6c3735049d016bfdfff5192feb3ca

The author's source audit and any computational receipts were not yet present
when this review was written. The mathematical verdict is bound to the above
proof version; any later source-audit review should be identified separately.

For nodes `x_n=pi H_n`, positive couplings `b_n` with `n b_n -> infinity`,
and inclusive eigenvalue counts, the main assertion is

    b_n/n -> kappa in (0,infinity)
      => N_b(k^2)=k log k+C(kappa)k+o(k),

where `C` is a convergent regularized integral of the periodic, per-cell
Kronig--Penney IDS `J_kappa`. It is continuous, strictly decreasing, and
has range `(2 gamma-1,infinity)`. The package also proves the hard-coupling
endpoint when `b_n/n -> infinity` and divergence of the centered second
coefficient, not a general leading-order law, when `b_n/n ->0`.

## 2. Form realization and bracketing

The domain and hypotheses in sections 1--2 suffice. Cauchy convergence for
the form norm gives convergence in `H^1_0` and in the weighted sampled
`ell^2` space. Continuity of each individual point trace identifies these
two limits. There is no reliance on a uniform positive lower bound for
the shrinking edge lengths. Compactly supported smooth test functions
give density, because only finitely many vertices meet a compact set.

The endpoint estimate gives exactly

    ||f||^2_{L^2(x_M,infinity)}
      <= [2pi sup_{n>M} 1/(n b_n)+2pi^2/(M+1)^2] q_b[f].

The bracket tends to zero under the stated hypothesis. Local Rellich
compactness plus this uniform tail estimate proves compact form embedding.
Positivity of the first eigenvalue follows after compactness: zero energy
would force a constant function with the zero left trace, hence zero.

Every finite set of zero-trace cuts imposes at most that many bounded
linear constraints on the form domain. Min--max therefore gives the
claimed inclusive count error. The package correctly does not assign
finite rank to an infinite collection of cuts. At every cut, its delta
form term vanishes, so the direct-sum block forms really agree with the
restricted original form.

## 3. Periodic normalization and the uniform chain estimate

The fiber form has one delta term `kappa |u(0)|^2` per cell of length `pi`.
The Dirichlet interval is a codimension-one restriction. This proves

    floor(z) <= nu_kappa(z,theta) <= floor(z)+1.

The free fiber frequencies `|2j+theta/pi|` integrate to `z`, not `pi z`
or `z/pi`, under normalized phase measure. Positive form ordering then
gives `floor(z) <= J_kappa(z) <= z` with the correct normalization.

The diamagnetic comparison puts the lowest band edge in the periodic
fiber. The positive symmetric cosine solves its derivative jump precisely
when

    r tan(pi r/2)=kappa/2,  0<r<1.

This equation has a unique continuous strictly increasing root. The
positive eigenfunction is the ground state. Consequently the IDS vanishes
below `r` and is positive above it: the ground eigenvalue is then strictly
below the test energy on an open set of phases.

The transfer half-trace

    cos(pi z)+(kappa/(2z)) sin(pi z)

and the equation equating it to `cos(theta)` have the stated sign and
factor. At a positive integer `z`, the nonzero delta shear prevents an
unaccounted-for free double eigenspace. For fixed positive `z`, there
are at most two exceptional phases. Continuous dependence follows by
gauging to a fixed periodic form domain. Off the exceptional phases the
integer count is locally constant; subtracting `floor(z)` leaves a
zero-one function with at most two boundary phases. Its uniform phase-mesh
sum has a bounded discrepancy, and the loose constant 4 is adequate,
including exceptional mesh points.

The `M`-cell ring decomposes into exactly the `M` fibers of phases
`2pi j/M`; neither the energy nor the coupling acquires an extra factor
of `M`. One zero-trace condition turns the ring into a Dirichlet-ended
chain and removes its endpoint delta term. Thus

    |N^D_{M,kappa}(z^2)-M J_kappa(z)| <=5

is valid uniformly in `M`, positive `kappa`, and real `z>=0`. Zero energy
is covered by the positive gap. This proof also covers inclusive counting
at band edges. The phase exceptional-set argument proves the continuity
of the IDS used later; differentiability at band edges is not assumed.

## 4. Critical local-periodic reduction

For exact `b_n=kappa n`, the tail coefficient is bounded by
`(2pi/kappa+2pi^2)/(M+1)^2`. Taking `M=ceil(Rk)` with the strict stated
inequality on `R` excludes all tail eigenvalues at or below `k^2`.
This establishes the spectral cutoff rather than guessing it.

The first `m=floor(sqrt(k))` cells form a finite interval of length
`pi H_m`. Both its free and its delta-coupled forms have the same
restriction to the fully Dirichlet cells, at codimension at most `m-1`.
This yields `N_head=k H_m+O(m)` independently of the varying head
couplings.

The geometric blocks with `epsilon=(log k)^(-2)` have at most
`O_kappa(log^3 k)` members. Integer rounding does not create empty
blocks once `epsilon m>2`, and the final shortened block obeys the same
upper relative-length estimate.

On `a<n<=b`, comparison with cells of length `pi/a` gives original
squared norm between `rho^(-1)` and 1 times the reference norm, and
original energy between 1 and `rho` times the reference energy,
where `rho=b/a`. All internal node indices lie in the required range;
the endpoint values are zero. Therefore the Rayleigh quotients lie
between the reference quotient and `rho^2` times it. Rescaling that
reference problem gives energy factor `a^2` and delta strength
`kappa`, yielding exactly

    (b-a)J_kappa(k/b)-5 <= N_block(k^2)
                        <= (b-a)J_kappa(k/a)+5.

The cumulative freezing error is the main potential vulnerability, and
the package addresses it. If `j_i=J_kappa(k/a_i)`, summation by parts gives

    sum (a_{i+1}-a_i)(j_i-j_{i+1})
      <= epsilon k [1+log(M/m)].

Here `j_i<=k/a_i` and
`(a_i-a_{i-1})/a_i <= log(a_i/a_{i-1})`; the final omitted term has the
correct nonpositive sign. No unjustified smoothness or fixed-parameter
Riemann approximation is substituted for this bound. Together with the
cuts and the head, all errors are

    O_kappa(sqrt(k)+log^3 k+k/log k)=o(k).

The head can be replaced by its IDS sum at cost at most `m`; all IDS
terms beyond `M` vanish by the band gap. This proves the central identity

    N_{kappa n}(k^2)=sum_{n>=1} J_kappa(k/n)+o(k).

## 5. Second coefficient and its range

The function `G(x)=J_kappa(1/x)-x^(-1) 1_{x<=1}` is bounded near zero,
has compact support away from infinity, and has the required continuity
elsewhere apart from the one cutoff. Removing `(0,delta)` bounds both
the normalized mesh sum and the integral error by `O(delta+1/k)`.
The subsequent Riemann-sum limit is therefore justified even though
`G` need not have a limit at zero.

Separating `k H_floor(k)` gives the asserted second coefficient with
Euler's constant, including for noninteger real `k`. The substitution
`z=1/x` gives the displayed integral without a sign or endpoint error.

Continuity in `kappa` follows from fiber form continuity outside finitely
many phases, the uniform positive band gap on compact positive coupling
ranges, and the integrable `1/z^2` tail bound. Strict decrease follows
on the nonempty interval between two strictly ordered band bottoms,
not just from weak form monotonicity.

As `kappa -> infinity`, the fiber form limit imposes both Dirichlet
endpoint values. The limiting eigenvalues are `j^2`, so the IDS tends
to `floor(z)` away from integer energies. Dominated convergence applies,
and the elementary integral evaluates to `gamma-1`, giving
`C(infinity)=2 gamma-1`. As `kappa ->0+`, the free IDS limit is `z`.
Its contribution on `(delta,1)` diverges as `log(1/delta)`, while the
upper-energy negative contribution is bounded and the remaining
lower-energy contribution is nonnegative. This proves the claimed
infinite limit and, with strict continuity, the exact range.

## 6. Full asymptotic-coupling theorem and endpoint regimes

For a positive finite limiting ratio, eventual comparison by
`(kappa-eta)n` and `(kappa+eta)n` also makes their form domains equivalent:
the finitely many initial point penalties are finite on `H^1` functions.
Imposing zero traces at those exceptional vertices gives the common
ordered forms and the fixed count error `r_eta`. Taking `k -> infinity`
before `eta ->0` proves stability without a convergence rate or any
monotonicity assumption on `b_n`.

For the hard regime the domains need not coincide, but the needed
inclusion does hold: the `b`-form domain is contained in the `Kn`-form
domain, apart from harmless finite terms. Thus the min--max comparison
has the stated direction. The fully Dirichlet form is a subdomain of
the `b`-form with exactly the same derivative energy. This yields the
lower count bound. The hyperbola formula supplies its classical
`(2 gamma-1)k` term and `O(sqrt(k))` error.

For the soft regime the domain inclusion reverses and gives the lower
bound by each fixed `Kn` model. Letting `K ->0+` proves precisely
divergence of the centered coefficient. The separate condition
`n b_n -> infinity` remains essential for the compactness assertion;
the proof never applies it to the zero-coupling free half-line. It
correctly makes no general `k log k` leading-order assertion here.

## 7. Bounded independent source-ownership check

The primary source [Egger ne Endres and Steiner, arXiv:1104.1364v1](https://arxiv.org/pdf/1104.1364)
was inspected in its introduction and the relevant parts of sections
2--4, not claimed to have been read in full. Equation (4) specifies
constant coupling at `x_n=pi H_n`; Theorem 2.2 proves compactness and
strictly positive discrete spectrum. The end of section 2, printed
page 10, explicitly leaves finite-constant-coupling high-energy
asymptotics to future work. Equations (35)--(39) establish the
fully Dirichlet divisor counting law and its two leading terms.
Accordingly those facts belong to the source, not to this candidate.
The inspected passages do not contain the present asymptotic-linear-
coupling IDS reduction. This is a limited source comparison, not an
assertion about every theorem or later paper.

Additional bounded searches on harmonic delta-chain Weyl asymptotics,
shrinking-cell Kronig--Penney couplings, and linear-coupling infinite
quantum graphs did not supply a directly matching primary theorem.
Those negative search returns are not evidence of global priority.
No secondary snippet was used as a theorem or verified publication
metadata.

The distinction from the prior C400 constant-coupling result is also
mathematically substantive at the level of the claimed mechanism:
in the critical transition `n` of order `k`, the rescaled delta strength
has a nonzero finite limit. The periodic-cell IDS must be retained there.
The resulting second coefficient is not obtained by substituting a
number into a fixed constant-coupling asymptotic. This observation does
not by itself settle paper-level significance or independence from the
broader existing slowly varying periodic-operator literature.

## 8. Disposition and remaining gate

The complete proof passes this independent mathematical review. No
counterexample, missing limiting argument, count-normalization defect,
or unproved claim essential to the stated theorem was found.

The remaining admission gate is bibliographic/source ownership and
paper-level significance. The author's final primary-source audit has
not yet been reviewed here. Standard form theory, Floquet dispersion,
finite-codimension bracketing, and the Dirichlet divisor law must remain
explicitly credited; the proposed increment is the proved critical
local-periodic reduction and its full second-coefficient stability.

The package appropriately denies any deduction of target Euler factors,
root numbers, individual zero correspondence, or a Hilbert--Polya
realization. An `o(k)` counting remainder alone supplies no meromorphic
continuation of a spectral zeta function. No numerical validation is
needed for the logical proof, and none was performed or inferred in
this review.

## 9. SOURCE_OWNERSHIP_ADDENDUM

Date: 2026-09-06. This addendum supersedes the pending source gate in
the original review; it leaves that historical review unchanged.

Final independent-review disposition:

    MATH_PASS_SOURCE_GATE_PASS_ADMIT_ONE_FOCUSED_PAPER

Explicit admission recommendation: **admit one substantial, focused
critical-regime research paper**. Do not admit separate papers for
coefficient monotonicity, stability, compactness, or endpoint corollaries.
This is an internal admission judgment, not a guarantee of journal
acceptance, comprehensive priority clearance, or a new general method
of semiclassical analysis.

### 9.1. Frozen versions and access

The complete 144-line author `critical_delta/SOURCE_AUDIT.md` was
independently read. Its SHA-256 is

    2b87777ac7ae2a2ed57d156710b60ea82d5e631f953adc9491e07f37082daecd

The proof remains unchanged from the mathematical review, with SHA-256

    5ae8f666d9fe091ce40ff4317aa7acc6a0f6c3735049d016bfdfff5192feb3ca

The pre-addendum cross-review SHA-256 was

    daa29dd8be6b12e2ea7407bf8c2a1ab08da12dba1e5a97869471a895ea1a5ab1

Both author-file hashes were rechecked immediately before this addition.
No mathematical rerun or numerical probe was necessary, because the
proof was unchanged and the source check raised no new mathematical
concern. Only this owned review file was edited. Primary-source PDF
retrieval and text extraction were read-only and were not experiments.

The named external Codex review endpoint is unavailable in this session;
as in the original review, the research-review framework is applied
internally. No external-model report or panel approval is represented.

### 9.2. Independent checks of the author's source split

S1 agrees with the primary-body comparison already recorded in section
7 of this review. Its ownership of the harmonic-chain model and the
Dirichlet benchmark is correctly acknowledged.

For S2, the [Kostenko--Malamud author PDF](https://arxiv.org/pdf/0908.3542)
was checked at Example 5.12 and section 5.4, in particular Theorem 5.17
and Propositions 5.18, 5.21, and 5.23. These address realization and
discreteness through Jacobi-operator criteria. In the critical positive
case, `d_n=pi/n`, `b_n~kappa n` give `b_n/d_n -> infinity` and
`1/(d_n b_n) ->1/(pi kappa)>-1/4`, consistently with Proposition 5.18
once self-adjointness is supplied. They do not supply the asserted
second counting coefficient in the inspected statements. The
[TU Dublin institutional record](https://researchprofiles.tudublin.ie/en/publications/1-d-schr%C3%B6dinger-operators-with-local-point-interactions-on-a-disc-3/)
independently confirms JDE 249(2), 253--304 (2010), and the stated DOI.
The audit correctly avoids claiming a new compactness theory.

For S3, [Drabkin--Kirsch--Schulz-Baldes, sections 2.1--2.3](https://arxiv.org/html/1207.0295v1)
were inspected at the jump condition (7), propagation matrix (11),
one-step matrix (12), and the positive periodic specialization. Their
unit-cell trace is `2cos(k)+(v/k)sin(k)`. Rescaling to length `pi`
gives exactly the package's half-trace. The audit properly treats
this as classical periodic machinery and does not borrow a theorem
about random transport to justify the growing nonperiodic chain.

For S4, [Bifulco--Kerner's arXiv v1, section 5](https://arxiv.org/html/2308.16869v1)
was read through Theorem 11 and its proof. The Hamiltonian has constant
coupling, and that local Weyl theorem explicitly sets it to infinity.
The other variable-coupling comparison statements in the inspected
preprint concern graphs of finite total length. Thus neither statement
is the present global two-term law on an infinite-length critical chain.
The arXiv abstract record confirms that v1 is the posted version and
links the 2024 journal publication; the automated HTML display date
must not be used as its publication date.

There is one useful citation-precision caution: the published S4 is
longer and reorganized compared with arXiv v1. The audit explicitly
identifies its access as the v1 HTML, so this is not a blocking defect.
In a manuscript, cite "arXiv v1, section 5, Theorem 11" when using
that locator, rather than silently calling it the journal's Theorem 11.

### 9.3. Bounded follow-up beyond the audit

To check whether the later S4 material changed the above conclusion,
selected passages of [Patrizio Bifulco's 2025 dissertation](https://d-nb.info/1388406829/34)
were retrieved from the German National Library. The title pages give
the author, FernUniversitaet in Hagen, and submission date 25 June 2025.
The harmonic-chain model and Theorem 6.3.14 in section 6.3.3 still use
fully Dirichlet vertices, also allowing a bounded ordinary potential.
Section 6.3.5 and Theorem 6.3.19 compare an integrable bounded potential
with zero, again at fully Dirichlet coupling; that section identifies
the journal result as S4 Theorem 18. These inspected later statements
do not supply the critical finite-transmission coefficient. Only the
identified passages were checked, not the entire dissertation or
the complete journal article.

A bounded search of the broader adiabatic literature also led to
[Magali Marx, arXiv:math-ph/0503031](https://arxiv.org/pdf/math-ph/0503031).
Its introduction and initial hypotheses concern a fixed locally
square-integrable periodic potential plus a decaying slowly varying
perturbation, with impurity levels in spectral gaps in an adiabatic
limit. Those hypotheses are not an off-the-shelf theorem for the
present shrinking-cell delta form and its high-energy global count.
This small comparison is not a survey of all slowly varying operator
results. Broader specialist review remains useful before submission.

No inspected primary theorem was found to own the proposed critical
IDS reduction. This bounded conclusion, rather than negative search
results alone, closes the present internal source-ownership gate.

### 9.4. Substantial paper versus short classical extension

The strongest case against separate admission is real: every basic
tool is classical, the geometry is one specific harmonic chain, and
several attractive conclusions are short corollaries once the exact
critical law is known. The elementary finite-ring estimate, form
closedness, monotonicity of fibers, and divisor summation should not
be advertised as independent breakthroughs. The asymptotic-coupling
extension is a min--max sandwich, not a second major theorem-paper.
The present proof also gives only `o(k)`, not a sharp oscillatory
remainder, a spectral determinant, or a general variable-microstructure
calculus.

Nevertheless, the central theorem survives those deductions from the
novelty budget. It identifies the order-`k` effect of finite microscopic
transmission in a critical regime where an order-`k` population of
shrinking cells contributes. The reduction

    N_{kappa n}(k^2)=sum_{n>=1} J_kappa(k/n)+o(k)

is a genuine additional analytic assertion, not a formula already
available from compactness, ordinary Weyl bracketing, or the endpoint
divisor law. Establishing it requires a coupled control of three
different regions: an increasingly long high-frequency head, a
growing transition region with band edges, and a spectrally excluded
tail. In particular, a bounded error per cell would accumulate to
order `k` and would destroy the requested second coefficient. The
geometric blocks and their telescoping IDS error are what remove
that obstruction in the actual proof.

The resulting coefficient is not just a renamed constant. Its full
dependence on the limiting coupling is proved through a convergent
regularized IDS integral; strict monotonicity and the exact range
show that distinct finite-transmission limits have genuinely distinct
second-order laws while sharing the same leading term. The arbitrary
positive `o(n)` perturbations make this a full asymptotic class, not
one solvable sequence or a finite collection of parameter examples.

The old fixed-constant-coupling result cannot deliver this coefficient
by substitution or by exchanging the high-energy and hard-coupling
limits. At `n` of order `k`, the product of coupling and cell length
stays of order one for `b_n~kappa n`; neither the free-cell nor the
Dirichlet-cell IDS can replace it without changing the order-`k`
contribution. This is a different asymptotic balance, although the
overall model lineage is shared and must be made explicit.

My judgment is therefore **one focused spectral-asymptotics paper**,
not a short restatement of a cited theorem and not several papers.
Its significance is moderate and specialized: a complete critical
regime and a rigorously determined second coefficient on a classical
infinite graph. I would not describe it as a broadly new method,
claim top-venue sufficiency, or inflate its importance through the
Hilbert--Polya motivation. Admission is justified by the proved
critical mechanism, not by the number of subsidiary statements or
the size of the source list.

### 9.5. Manuscript boundaries and final recommendation

The admissible manuscript should center its title, abstract, and main
theorem on the critical two-term counting law and the local-periodic
reduction. Put coefficient behavior, rate-free stability, and hard/soft
consequences in the same paper. Credit the source model and periodic
inputs prominently, and distinguish preprint and journal locators.
No numerical plot is required to repair the proof or to earn admission.

No new blocking mathematical or source-attribution issue was found.
The original mathematical verdict remains 0 blocking defects and
0 required proof fixes. The source audit passes at its explicitly
bounded scope. The independent admission recommendation is **one**
paper with the above restricted claims; formal project admission and
numbering remain the root agent's responsibility.
