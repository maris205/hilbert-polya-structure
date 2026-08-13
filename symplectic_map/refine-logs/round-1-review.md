# Round 1: Independent Pre-Implementation Technical Review

## Review provenance and limitation

- Review type: independent model-based technical review, not human peer review.
- Reviewer configuration reported by the orchestration log: GPT-5.4, xhigh reasoning.
- Review timing: after the repository/literature audit and before the final
  confirmatory design.
- Date recorded: 2026-08-12.
- Text status: **structured transcription from the review scores and adjudication
  delivered to the research agent; not a verbatim transcript.** No unavailable quote
  has been reconstructed.

## Scores delivered

| Dimension | Score / 10 |
|---|---:|
| Theory | 6 |
| Method | 5 |
| Contribution | 5 |
| Novelty | 4 |
| Feasibility | 6 |
| Validation | 4 |
| Readiness | 3 |
| **Reported weighted score** | **5.0** |

## Verdict delivered

```text
Overall proposal: REVISE
Arithmetic multiplier candidate: RETHINK
Narrowed nonlinear-dynamics/diagnostic paper: REVISE
```

The review did not recommend proceeding from the current proposal directly to a
Riemann-targeted zeta function, quantization, or paper claim.

## Package ranking delivered

The reviewer ranked the candidate packages:

1. **Obstruction plus \(\rho\)-survival experiment** -- strongest and most
   defensible.
2. **High-\(a\) anti-integrable/full-shift positive control** -- necessary for method
   validation but not a novelty claim.
3. **Multiplier-to-prime Euler product** -- substantially weaker and to be deferred or
   rethought.

## Main positive assessment

The review found several sound components:

- the Hénon family gives an exact conservative/dissipative control through
  \(\det DH=\rho\);
- the generating function at \(\rho=1\) and monodromy determinant identity are exact;
- freezing \(u_c\) before inspecting prime labels or multipliers is methodologically
  correct;
- the critical-fiber rank argument supplies a clear conceptual boundary;
- a negative survival result could be useful if controls, censoring, and completeness
  are handled rigorously;
- the high-\(a\) symbolic regime offers a credible positive control for the orbit
  finder.

## Main criticisms

### 1. The arithmetic source was overstated

The upstream work appeared to support only a parity/mod-2 shadow, not intrinsic
rational-prime coding. The proposal could not treat "Logistic arithmetic seed" as an
established premise. It needed to distinguish upstream failure from failure caused by
the symplectic passage.

### 2. The obstruction was useful but not sufficiently novel alone

The chain-rule rank lemma is elementary and consistent with the direct literature on
singular canonical extensions. It should anchor scope, not be marketed as a new
Hilbert--Pólya obstruction theorem.

### 3. The broad Hénon ledger/zeta program duplicated mature techniques

Periodic-orbit enumeration, symbolic coding, monodromy ledgers, and dynamical
determinants in hyperbolic Hénon regimes are established. The paper needed a new
question beyond "compute a Hénon ledger."

### 4. The \(\rho=0\) endpoint was being treated too casually

Because the endpoint is singular, the experiment should not begin with an unqualified
smooth continuation from \(\rho=0\). A branch identity must be defined, singular
values and bifurcations recorded, and the phrase "the same orbit survives" withdrawn
when a collision or branch ambiguity occurs.

### 5. The arithmetic test was not yet predeclared

The review required one primary transport statistic that can be defined before seeing
prime labels, together with a fixed trajectory ensemble, data split, censoring rule,
exposure gate, uncertainty calculation, neighboring-parameter controls, and explicit
stopping rules.

### 6. Completeness uncertainty blocked zeta interpretation

Certification should be restricted to a low-period range. A high-\(a\) full-shift
control should validate the enumeration software. An incomplete mixed-regime ledger
at \(u_c\) cannot support a dynamical determinant as though complete.

### 7. The multiplier-prime idea lacked a blind assignment rule

No orbit-to-prime assignment had been defined before labels. A single multiplier near
an integer, or an exact prime multiplier obtained by parameter tuning, would be
post-hoc and non-specific. Any enrichment test would need prime, composite, shuffled,
matched-density, neighboring-parameter, and cat-map controls.

### 8. The semiclassical and Ruelle-style weights were being conflated

For a two-dimensional symplectic hyperbolic orbit,

\[
|\det(M^r-I)|^{-1/2}
=\frac{|\Lambda|^{-r/2}}{|1-\Lambda^{-r}|}.
\]

This is not exactly the monomial weight in the provisional unstable-multiplier Euler
product. The two objects must remain separate.

## Mandatory revisions extracted from the review

1. Reframe Stage 1 as a nonlinear-dynamics diagnostic/negative-result paper.
2. Cite Fogedby--Jensen (2005) and Demaeyer--Gaspard (2009) as direct priors.
3. Describe the obstruction as elementary and scope it to smooth-submersion factors.
4. Freeze one parent symbolic feature, rather than retroactively using prime labels.
5. Add development, validation, and single-use confirmatory splits.
6. Add an exposure gate so rare-survivor conditioning cannot pass.
7. Use the singular reference separately from regular positive \(\rho\)-values.
8. Restrict the primary certification target to periods \(n\leq6\), with periods 7--8
   exploratory at \(u_c\).
9. Validate periods through 10 in a high-\(a\) positive control.
10. Report all branch collisions, period collapses, and missed-orbit risk.
11. Stop before zeta or quantization if A0 fails, exposure collapses, completeness is
    unavailable, or controls reproduce the signal.
12. Defer the multiplier-prime hypothesis until a robust weak-shadow result exists.

## Claims adjudication

| Claim package | Round-1 adjudication |
|---|---|
| Conformal-symplectic identity and monodromy determinant | Exact and usable |
| Generating function/action at \(\rho=1\) | Exact and usable |
| Critical-fiber smooth-factor obstruction | Correct but elementary/known boundary |
| Generic Hénon UPO ledger | Low novelty; method/control only |
| Complete \(u_c\) ledger | Not established |
| Arithmetic shadow survival | Open, selected as primary test |
| Prime-valued multipliers | Unsupported and vulnerable to tuning |
| Unstable-multiplier Euler product | Formal/conditional only |
| Riemann determinant or natural quantization | Stop-scoped |

## Revision implemented after review

The proposal was narrowed to source-lock v2:

- singular reference \(\rho=0\);
- regular test grid \(0.02,0.05,0.1,0.2,0.5,1\);
- primary polarity
  \(P=(N_{\rm even}-N_{\rm odd})/(N_{\rm even}+N_{\rm odd})\);
- 2048 trajectories, burn-in 4096, horizon 1024, escape bound 100;
- trajectory-cluster bootstrap with 2000 replicates;
- endpoint availability of at least 0.80 and at least 10,000 gaps;
- endpoint lower 95% confidence bound at least 0.98;
- specificity against every clean neighbor after Holm correction;
- high-\(a\) positive-control certification and explicit \(u_c\) incompleteness;
- no Stage-1 determinant evaluation.

## Round-1 disposition

The arithmetic multiplier candidate remains `RETHINK`. The narrowed Stage-1 paper is
`REVISE` pending confirmatory results and a second independent review. A positive
software calibration does not by itself change the reported 5.0/10 proposal score.
