# C406 independent review of the frozen manuscript

Date: 2026-09-06.

Verdict: **PASS — no mathematical blocker and no mandatory theorem,
citation, or scope correction identified in the reviewed manuscript.**
This is clearance of the mathematical manuscript for the coordinator's
final production checks, not a claim that final production is complete.

## 1. Independence, object, and method

The reviewed article is *The critical second Weyl coefficient of a
harmonic delta chain*, under `critical_delta/paper/`. The reviewer is
the separately assigned nonlinear-return agent, not the author of
the C406 proof package or of this article. The agent that reviewed
the earlier proof package subsequently drafted the article. Its
earlier proof review was read as a prerequisite but is not treated
as an independent review of its own later manuscript.

This review began binding the actual article only after its author
announced that the TeX, bibliography, and initial PDF were frozen.
The reviewer independently reconstructed the arguments, then checked
them against all eight actual section files, the master, macros,
bibliography, and the actual PDF's extracted text. The article inputs
contain 1,132 lines: 1,025 section lines, 32 master lines, 24 macro
lines, and 51 bibliography lines. All 730 extracted PDF-text lines
were read; this is text inspection, not page-image visual inspection.
The source plan, proof package, source audit, and full earlier
cross-review including its ownership addendum were also read.

The `research-review` and `proof-writer` skills supplied the critical
review and proof-audit structure. The assigned pure-mathematics scope
overrides their legacy external-model and empirical-scoring defaults.
No external model was queried, no numerical experiment was run, and
no empirical score or referee acceptance was inferred.

Only this review file was created. The reviewer did not edit author
inputs, alter project state or evaluation files, run a new LaTeX build,
or perform any Git operation. The coordinator retains ownership of
two fresh final builds, all-page visual QA, and final sealing.

## 2. Frozen snapshot and evidence binding

All hashes below are SHA-256. Both author-supplied manifests were
checked with `sha256sum -c` against the actual files; every entry
passed. The proof-package and other prerequisite hashes also match
the announced freeze.

| Bound object | SHA-256 |
|---|---|
| `critical_delta/paper/main.pdf` | `43f04734234a9e21e41ad0eaff5e199c642935228475c4207e7a4cee14bec1a9` |
| `critical_delta/paper/initial_build/main.pdf` | `43f04734234a9e21e41ad0eaff5e199c642935228475c4207e7a4cee14bec1a9` |
| `critical_delta/paper/SOURCE_INPUTS.sha256` | `3a73cdaf29b5c608d05e272723b15b065f3b9559f53d4bf7e5dd4288ac542687` |
| `critical_delta/paper/INITIAL_ARTIFACTS.sha256` | `dee757d89adf86ad79a3a9f82ef0b329ca77b7355038c6aebefc3ab55773297a` |
| `critical_delta/INITIAL_COMPILE_RECEIPT.md` | `b9c22da289c6abddb3de925852d17c2ce79d0d34cb1142c0a2984107741c81c6` |
| `critical_delta/PROOF_PACKAGE.md` | `5ae8f666d9fe091ce40ff4317aa7acc6a0f6c3735049d016bfdfff5192feb3ca` |
| `critical_delta/SOURCE_AUDIT.md` | `2b87777ac7ae2a2ed57d156710b60ea82d5e631f953adc9491e07f37082daecd` |
| `critical_delta/PAPER_PLAN.md` | `a9a6391e23b05b76368b7699b4c5caa2027521cbada51ce240bc47d701a02dac` |
| `wild_dynamics/CROSS_REVIEW_CRITICAL_DELTA.md` | `85eb51dcf8ef48c839392ea7d4c676357d84a1d0f5b1044c2bbe0d27dcef0f27` |

The following complete source-input binding is copied from the verified
manifest. Paths in this block are relative to `critical_delta/paper/`.

```text
6c82f1f0323f93ba5eaf2942c9e9384d4c39597f985bc4d6dc8281ca49a900c0  main.tex
22d3347af65e8745e5b932c21e0ad61c6dd7b55ea5194457f1e1218e30d6fff7  math_commands.tex
234d735b2d4c865369b57609960fface2f6d0bbf61cdc403249c891ca9a514a6  references.bib
f87ef40afad84b407ef6860d040418bcc349a12e976e9e655e0041fabbc04281  sections/0_abstract.tex
3ee35c83bb3296b038e3b9127b62172be491070ad4ff262f25dff39671200b6c  sections/1_introduction.tex
d0c716973badad558cc6abd7657cd50943598f884c932a131ddfe69a49976d14  sections/2_forms.tex
32f522184d08cd085d58c3ea1a4eb3017f16811d84fa16aae2536c5750cdd700  sections/3_periodic.tex
ad4f86e83f1f75da87c6e0b32c00588a4b3a682521cce57fccf49dab0d16710c  sections/4_reduction.tex
7fdbe6d3ca7cedd5d59a7dff149013c38057de056174219c271544403a2330d1  sections/5_coefficient.tex
1f91a56289c2ef2efc95ea517fd8ec651b76ae6f8c85bfb5fd55a362e397f21c  sections/6_general.tex
eef6680f56415aa1ce5a22cda7742d318a7c4695703075347c78ac41363930cf  sections/7_scope.tex
29f387656ad6944057802d6fddca81b8da4724c0b9c8b786d24b0c7a842c4bd6  build_initial.sh
42dfd2cccea50cd25d9d925548cc96941ad249513d7dcdc9c0a76924ba34edce  CITATION_AUDIT.md
```

The initial artifact is a 13-page, 403,808-byte A4 PDF. The main
mathematics and disclosure occupy pages 1–12, and references page 13.
The two initial PDF copies are identical. The artifact manifest binds
the actual final LaTeX/BibTeX logs, bibliography, auxiliary/recorder
files, build stdout, extracted text, metadata, and font listing. A
read-only scan of the final `main.log` and `main.blg` found no warning,
undefined-reference/citation, overfull/underfull-box, or TeX-error
diagnostic. The resolved auxiliary file has five citation occurrences
using exactly four keys, all represented in the actual bibliography.
The font listing has 24 embedded Type 1 records and no Type 3 record.

The initial receipt correctly distinguishes one completed build from
the still-pending two-fresh-build equality test, and its limited
first/last-page previews from all-page QA. No visual-clearance claim
is added by this review.

## 3. Theorem contract and source operator

Locators: `sections/1_introduction.tex:36` and `:97`; Proposition 2.1
and Lemma 2.2 in `sections/2_forms.tex:4` and `:57`; PDF pages 2–4.

The statements consistently fix a positive coupling sequence before
taking the real-frequency limit. The geometry is exactly
`x_n = pi H_n`, with cell length `pi/n`; no altered spectral weights
or parameter-dependent source operator is introduced. The form domain
is explicitly the global `H^1` space with zero left trace and finite
weighted sample sum, not a smaller unspecified boundary space at
infinity. The resulting dynamics remains `exp(-it H_b)`.

Closedness follows from simultaneous convergence in `H^1` and the
weighted sample `ell^2` space: each fixed trace identifies the limit
coordinate. Density follows because compactly supported smooth
functions meet finitely many vertices. The tail estimate is correctly
indexed at the right endpoint of each cell:

```text
integral_{I_n} |f|^2
 <= (2 pi/n)|f(x_n)|^2 + (2 pi^2/n^2) integral_{I_n}|f'|^2.
```

Summation gives the stated `a_M`, and `n b_n -> infinity` makes it
tend to zero. Local Rellich compactness plus this uniform tail bound
gives compact resolvent. Vanishing energy forces `f'=0` and then
`f=0`, so compact resolvent excludes zero from the spectrum and gives
a strictly positive first eigenvalue. There is no inference that
injectivity alone would imply a gap without compactness.

For `r` cuts the trace kernel has codimension at most `r`; intersecting
the original spectral subspace with that kernel proves the inclusive
count error even at thresholds. The direct-sum identification is valid
because the cut delta penalties vanish. The manuscript explicitly
does not apply this finite error estimate to infinitely many cuts.

## 4. Per-cell normalization and finite-chain estimate

Locators: `sections/3_periodic.tex:9`, `:97`, and `:145`; equations
(3.1)–(3.8); PDF pages 4–6.

The normalization in (1.6) is per cell of length `pi`. Restriction
to `H^1_0(0,pi)` is codimension one in every quasiperiodic fiber,
giving `floor(z) <= nu <= floor(z)+1` with inclusive counts. At zero
coupling, the frequencies are `|2j+theta/pi|`; their normalized phase
integral is exactly `z`. Thus `floor(z) <= J_kappa(z) <= z` has no
missing factor of `pi` or two.

The modulus comparison lowers each fiber ground energy to the
periodic one. The positive function `cos(r(x-pi/2))` satisfies the
periodic derivative jump precisely when
`r tan(pi r/2)=kappa/2`. The solution in `(0,1)` is unique and is the
ground state. It increases continuously with `kappa`. Phase continuity
then makes `J_kappa(z)>0` at every `z>r(kappa)`, which is stronger than
the mere absence of a spectrum below the gap and is needed later for
strict monotonicity of the coefficient.

The manuscript's state-vector convention `(u,u')` gives the stated
propagation and delta matrices. Their half-trace is
`cos(pi z)+(kappa/(2z))sin(pi z)`. At every fixed positive test
frequency there are at most two exceptional phases. At integer
frequencies the nontrivial shear has a one-dimensional eigenspace,
so the proof does not import a spurious double free eigenvalue. The
zero-frequency half-trace is greater than one. Dominated phase
integration establishes continuity of `J` without continuity of each
inclusive fiber count at a threshold.

Away from at most two exceptional phases,
`nu-floor(z)` is a constant or an arc indicator on the phase circle.
The uniform mesh discrepancy is at most two for the arc, plus at most
two endpoint corrections. The ring decomposes into exactly the `M`
phase fibers, with both norm and energy multiplied by `M`; the coupling
is not multiplied or divided by `M`. One zero trace turns the ring
into the prescribed Dirichlet chain at count cost at most one.
This proves the displayed error `<=5`, uniformly for all `M>=1`,
`kappa>0`, and `z>=0`, including band edges and `M=1`.

## 5. Growing-region reduction and cumulative error

Locator: Proposition 4.1, `sections/4_reduction.tex:7`; equations
(4.2)–(4.11); PDF pages 7–8.

The tail choice fixes `R` for a fixed `kappa` and uses
`R^2 > 2pi/kappa+2pi^2`, not a non-strict inequality. For
`M=ceil(Rk)`, the tail Rayleigh lower bound is strictly greater
than `k^2`. Zero extension justifies use of the global tail inequality
on the Dirichlet-ended tail. Thus even a threshold eigenvalue cannot
be inadvertently discarded.

The head shares its fully cut restriction with the free interval of
length `pi H_m`; the codimension is `m-1` in both forms. Its count is
therefore `k H_m+O(m)`, regardless of individual head coupling sizes.
With `m=floor(sqrt(k))` and `epsilon=(log k)^(-2)`, eventually
`epsilon m>2`; the integer geometric blocks are nonempty and have
`B=O_kappa(log^3 k)`.

For a block `a<n<=b`, the affine common-domain transformation has
`s_n=a/n` in `[1/rho,1]`, `rho=b/a`. The norm has factors `s_n`,
the derivative energy has factors `1/s_n`, and internal strengths
lie between `kappa a` and `rho kappa a`. This gives

```text
norm_ref^2/rho <= norm_orig^2 <= norm_ref^2,
q_ref <= q_orig <= rho q_ref,
R_ref <= R_orig <= rho^2 R_ref.
```

In the length-`pi` coordinate, `norm_ref^2=a^(-1) norm_cell^2`
and `q_ref=a q_cell` with cell strength `kappa`. The eigenvalue
factor is thus `a^2`. Min–max consequently gives the stated block
bounds with arguments `k/b` and `k/a`, not their squares or an
incorrect single-power dilation.

The accumulated freezing error is not bounded separately by an
order-one error on each of order-`k` cells. Setting
`j_i=J_kappa(k/a_i)`, summation by parts yields

```text
sum Delta_i (j_i-j_{i+1})
 <= epsilon [m j_0 + sum_{i=1}^{B-1}(a_i-a_{i-1})j_i
                         - a_{B-1}j_B]
 <= epsilon k [1+log(M/m)].
```

All signs and indices in (4.10) are correct. The last term is
nonpositive, `j_i<=k/a_i`, and the remaining endpoint ratios are
bounded by their logarithms. The total error, including finite-chain
and cut errors, is
`O_kappa(sqrt(k)+log^3(k)+k/log(k))=o(k)`. No differentiability or
Lipschitz bound at band edges is assumed. Replacing the head by its
IDS sum costs at most `m`; the positive periodic gap kills every
remaining term beyond `M`. This proves the full reduction claimed
in the introduction, not only a fixed compact-region approximation.

## 6. Riemann limit and coefficient range

Locators: Propositions 5.1–5.2, `sections/5_coefficient.tex:6` and
`:70`; PDF pages 9–10.

The regularized summand `G(x)=J_kappa(1/x)-x^(-1)1_(0,1](x)`
is bounded by one near zero and is compactly supported. Its possible
failure to have a limit at zero is explicitly handled: both the
integral and normalized mesh mass in `(0,delta)` have bound
`delta+O(1/k)`, while ordinary Riemann convergence applies on the
remaining compact interval with one cutoff discontinuity. The limits
are taken in the correct order. The exact separation uses
`H_floor(k)`, so it holds for real `k`, including integer thresholds.
The substitution `z=1/x` produces the correct sign, regularizer,
Jacobian `z^(-2)`, and additive `gamma`.

For continuity in positive coupling, the fixed-domain fiber
eigenvalues converge and exceptional phases have measure zero.
A uniform gap on compact positive coupling intervals and the
uniform `z^(-2)` tail bound justify the coefficient's dominated
limit. Strict monotonicity does not rely on strict motion of every
band: the interval between the two distinct band bottoms has
positive first IDS and zero second IDS, making the integral
difference strictly positive.

In the hard cell limit, bounded-energy normalized eigenspaces are
compact and their endpoint values tend to zero. The limiting dense
form domain is precisely Dirichlet, giving indexed eigenvalue limits
`j^2`. Noninteger-frequency IDS convergence and domination suffice
for the coefficient integral. Its remaining integral is
`sum_{j>=1}[1/(j+1)-log((j+1)/j)]=gamma-1`, hence the endpoint is
`2gamma-1`.

In the soft cell limit, the free phase average tends to `z` at fixed
positive frequency. The integral over `[delta,1]` tends to
`log(1/delta)`, the high-frequency part is bounded below by `-1`,
and the omitted low-frequency part is nonnegative. Taking the
coupling to zero before `delta` proves divergence to positive
infinity. Together with continuity and strict decrease this gives
exactly the open range `(2gamma-1,infinity)`, not its closed hull.

## 7. Rate-free, hard, and soft domain comparisons

Locator: `sections/6_general.tex:12`, `:55`, `:94`, and `:127`;
equations (6.1)–(6.8); PDF pages 10–12.

For fixed `eta`, eventual two-sided comparability makes the three
critical form domains equal. Zeroing the finite exceptional set
orders the forms on a common domain. The count sandwich requires
only `|F_eta|` on each side, as stated. The frequency limit is taken
before `eta` tends to zero, so no convergence rate or monotonicity
of `b_n/n` has been smuggled in.

The fully Dirichlet domain is an infinite restriction contained in
every positive-coupling domain. Its direct-sum identification follows
from zero endpoints and finite global derivative energy, and its
count is a lower bound with no finite-rank assertion. The hyperbola
identity with `h=floor(sqrt(k))` gives the classical
`k log k+(2gamma-1)k+O(sqrt(k))` for real `k`.

The hard and soft domain directions are explicit and correct:

| Regime, outside a finite exceptional set | Form-domain inclusion | Count bound after finite cuts |
|---|---|---|
| `b_n>=Kn` | `D_b subset D_(Kn)` | `N_b<=N_(Kn)+|F_K|` |
| `b_n<=Kn` | `D_(Kn) subset D_b` | `N_b>=N_(Kn)-|F_K|` |

For hard couplings the Dirichlet lower count and the critical upper
count squeeze the centered coefficient as `K` tends to infinity.
For soft couplings the lower count gives a lower limit at least
`C(K)` for every fixed `K>0`; letting `K` decrease to zero proves
only the asserted centered divergence. The separate assumption
`n b_n -> infinity` is retained in the soft theorem and proof.
Neither compactness for zero coupling nor a universal soft-regime
leading asymptotic is asserted.

## 8. Actual citation and attribution audit

All five citation occurrences were mapped to their claims. Relevant
primary-text passages were accessed afresh for this review. This is
a targeted verification of the four works used by the manuscript,
not a new exhaustive literature search or a re-audit of entire books
and dissertations.

- **Egger né Endres–Steiner:** the introduction/model definition,
  Theorem 2.2, the fully Dirichlet discussion, and equations
  (35)–(39) support the classical model, positive constant-coupling
  discreteness, and divisor benchmark. The source explicitly leaves
  its finite positive-coupling high-energy asymptotics for later work.
  The manuscript does not attribute its critical coefficient theorem
  or a constant-coupling counting theorem to this source.
  [Primary text](https://arxiv.org/pdf/1104.1364).
- **Kostenko–Malamud:** Example 5.12 and Section 5.4, specifically
  Theorem 5.17 and Proposition 5.18, support the stated realization
  and shrinking-gap discreteness background. The positive harmonic
  example is a realization comparison, not an imported second-term
  theorem. The article proves its quantitative compactness estimate
  directly, so no unverified Jacobi-operator hypothesis is used as
  a black box. [Primary text](https://arxiv.org/pdf/0908.3542).
- **Drabkin–Kirsch–Schulz-Baldes:** Sections 2.1–2.3, including
  equations (7), (11), (12), and the positive periodic specialization,
  support precisely the classical jump, propagation, and discriminant
  background. The source uses the reversed state-vector order and
  unit cells; the manuscript correctly derives its own length-`pi`
  convention. No random-transport theorem or uniform finite-chain
  error is falsely imported.
  [Primary text](https://arxiv.org/html/1207.0295v1).
- **Bifulco–Kerner:** arXiv v1 Section 5 defines the harmonic model
  in (11); Theorem 11 explicitly imposes fully Dirichlet coupling and
  concerns a local eigenfunction average. Its statement and proof
  do not provide the manuscript's global critical second term.
  Both the introduction and bibliography identify the locator as
  belonging to arXiv v1, not silently to the reorganized journal
  text. [Inspected version](https://arxiv.org/html/2308.16869v1).

DOI content negotiation was independently repeated for all four
entries. The Drabkin request had one transient TLS failure and
succeeded on retry; no failed request is counted as verification.
Titles, authors, years, journals, volumes, issues, and available page
or article data agree with the actual BibTeX. The first author's
displayed name in the Egger source is consistent with the normalized
BibTeX and rendered reference, despite the DOI record's surname
parsing. For Drabkin, article number 122109 is also confirmed by
the [author-posted arXiv record](https://arxiv.org/abs/1207.0295)
and [institutional record](https://cris.fau.de/publications/112746744/).
For Bifulco, the independently fetched DOI CSL-JSON explicitly gives
`article-number: 073502`, although its BibTeX response omits that
field; full names and the linked journal DOI agree with the
[author-posted record](https://arxiv.org/abs/2308.16869).

There is no unsupported priority claim over all adiabatic periodic
asymptotics. Classical compactness, periodic formulas, and the
Dirichlet divisor law are credited; the critical reduction and its
consequences are proved in the manuscript. The background search
does not become a proof of exhaustive novelty.

## 9. Scope, findings, and handoff

The abstract, main statements, proofs, and Section 7 agree on the
admitted scope. Fixed constant couplings are placed on the zero-ratio
side and not confused with `b_n~kappa n`. The periodic object is only
a local comparison, not a global conjugate or a scalar-potential
replacement. The paper obtains no target Euler factors, root numbers,
individual Riemann-zero correspondence, or Hilbert–Pólya realization.
It explicitly does not infer meromorphic spectral-zeta continuation
from an `o(k)` counting remainder.

The AI disclosure accurately separates the earlier proof check from
the present manuscript review. It does not claim external referee
approval. This new review is internal non-author checking, not a
machine-verified proof or a novelty/acceptance guarantee.

Findings:

- Mathematical blockers: **0**.
- Mandatory theorem/proof corrections: **0**.
- Mandatory citation or scope corrections: **0**.
- Unresolved mathematical dependencies in the stated proof chain: **0**.
- Final-production clearance: **not supplied by this review**.

No author revision is required by the findings above. The reviewed
snapshot may proceed to the coordinator's two fresh deterministic
builds and all-page visual QA. If a substantive theorem, proof,
normalization, domain, citation, or scope change is made afterward,
this verdict must not be represented as covering that altered text
without a corresponding recheck and updated hash binding.
