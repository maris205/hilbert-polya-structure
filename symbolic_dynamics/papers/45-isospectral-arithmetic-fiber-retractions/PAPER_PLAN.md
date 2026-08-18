# Paper plan: Isospectral arithmetic fiber retractions

## Working identity

- Working title: **Isospectral Arithmetic Fiber Retractions with Distinct Nonnormal Phases**
- Format: anonymous mathematical article, self-contained main theorem and proofs.
- One-sentence contribution: For every integer `h >= 2`, the saturated and
  exponent-modulo arithmetic retractions define compact weighted operators
  with the same simple nonzero spectrum and every common legal determinant,
  yet they have different boundedness and normal-similarity domains; the
  discrepancy is quantified by exact primorial Riesz growth, explicit
  singular-value Weyl constants, and a sharp self-commutator Schatten wall.
- Claim boundary: the paper concerns only the two frozen maps on
  `ell^2(N)` with weights `n^{-s/2}`. It makes no priority claim, no general
  weighted-composition theorem, no rational-prime selectivity claim, and no
  inference from finite experiments to an infinite endpoint.

The claims--evidence matrix and all review/release gates below are internal
planning controls. They will not appear as manuscript section headings or be
presented as mathematical evidence.

## Reader contract

The reader should leave with one organizing distinction: cyclic data and
metric geometry decouple. The common `h`-free eigenlines determine the
nonzero spectrum, traces, and legal regularized determinants. Fiber mass and
fiber angle instead determine boundedness, singular values, Riesz
projections, similarity, and self-commutators.

Here a **negative control** is a construction deliberately retained because
it reproduces shared invariants while lacking the geometry or arithmetic
semantics under study. The **free-UFD negative control** replaces rational
primes by freely named atoms with the same multiplicative norms; reproducing
the formulas after this relabeling shows that those formulas alone do not
detect rational-prime semantics.

## Claims--evidence matrix

| Claim | Mathematical evidence | Canonical evaluated evidence | Failure condition |
|---|---|---|---|
| C1. Exact paired classification | Exact prime-exponent fibers; orthogonal rank-one blocks; positive Euler products; uniform Riesz-projection criterion | A and B each contain 21 finite records; comparator X covers seven finite case IDs with 0 exact and 0 interval mismatches; B and P close all 15 infinite cases | Any missing existence condition, endpoint made non-strict, trace outside trace class, or similarity inferred from spectrum |
| C2. Quantitative nonnormality laws | Exchange argument for exact primorial optimizer; PNT/Mertens/prime sums; positive generalized Dirichlet series and Wiener--Ikehara; rank-one commutator formula with separate `h=2` witness | Exact finite optimizer labels `(x,m)=(100,36),(1000,900),(10000,900)`; B/P certificates for primorial, Tauberian, crossover, Weyl, and commutator cases; 168 physical mutation outcomes with 0 survivors | Wrong `(h-1)^(sigma-1)` coefficient, missing `C_{h,1}=D_{h,1}=1`, ordering `C` and `D` away from one, or using the `h>=3` commutator witness at `h=2` |

The finite records verify implementations and local identities. Infinite
claims are proved analytically and independently certified; no finite
compression is used as proof of an endpoint or asymptotic.

## Main theorem ledger

### Operator and notation convention

Here `N={1,2,...}` and `n^{-s/2}=exp(-(s/2) log n)`, with the real logarithm
of the positive integer `n`. The displayed formulas first define algebraic
maps on `c_00(N)`. When a formula has a bounded extension to `ell^2(N)`, the
same symbol denotes that unique extension. Spectrum, singular values,
Schatten or quasi-Schatten membership, Riesz projections, similarity,
traces, determinants, and self-commutators are asserted only for these
bounded extensions. For `0<q<1`, `S_q` has its usual quasi-ideal meaning.

For an integer `r>=1`, a “legal order-`r` regularized determinant comparison”
means that both operators belong to `S_r`; in the present common domain this
is exactly `sigma>1/h` and `r sigma>2`.

For `s in C`, `sigma = Re(s)`, and `h >= 2`, define on `c_00(N)`

```
S_{h,s} e_n = n^{-s/2} e_{tau_h(n)},
M_{h,s} e_n = n^{-s/2} e_{omega_h(n)},
```

where the prime exponent is respectively capped at `h-1` or reduced
modulo `h`. The paper will prove, with all domains stated locally:

1. `S` is bounded and compact iff `sigma>0`; `M` is bounded and compact
   iff `sigma>1/h`.
2. For `k>=1` and `0<q<infinity`, `S^k in S_q` iff `k sigma q>2`, while
   `M^k in S_q` iff `sigma>1/h` and `k sigma q>2`.
3. Their simple nonzero eigenvalues are `m^{-s/2}`, indexed by `h`-free
   `m`, on each operator's bounded domain.
4. For every integer `k>=1`, if `sigma>1/h` and `k sigma>2`, then both
   `S^k` and `M^k` are trace class and
   `Tr(S^k)=Tr(M^k)=zeta(ks/2)/zeta(hks/2)`. No ordinary trace identity is
   asserted at or below `k sigma=2`.
5. For every integer `r>=1`, if `sigma>1/h` and `r sigma>2`, then
   `det_r(I-zS)=det_r(I-zM)` as entire functions of the determinant variable
   `z`. For `r=1` this is the ordinary Fredholm determinant and requires
   `sigma>2`.
6. `S` is boundedly similar to compact normal iff `sigma>1`; `M` is so
   similar throughout `sigma>1/h`. Hence `1/h<sigma<=1` is the exact
   isospectral-but-not-similar band.
7. Write `P_k=p_1...p_k`, take the largest `k=k(x)` with
   `P_k^(h-1)<=x`, and put `m_x=P_k^(h-1)`. Then the exact maximum of
   `||Pi_{S,m}||` over `h`-free `m<=x` is attained at `m_x`. As `x` tends
   to infinity:
   - if `sigma>1`, the maximum tends to `sqrt(zeta(sigma))`;
   - if `sigma=1`, it is asymptotic to
     `sqrt(exp(gamma) log log x)`;
   - if `0<sigma<1`, its logarithm is asymptotic to
     `(h-1)^(sigma-1)(log x)^(1-sigma)/
      (2(1-sigma) log log x)`.
8. For `sigma>0`, let
   `N_S(t)=#{n:s_n(S)>=t}`; then as `t` decreases to zero,
   `N_S(t)~C_{h,sigma} t^(-2/sigma)`, equivalently
   `s_n(S)~(C_{h,sigma}/n)^(sigma/2)`, where
   `C_{h,sigma}` is the explicit positive Euler product stated in Section 6.
   For `sigma>1/h`, let `N_M(t)=#{n:s_n(M)>=t}`. Then
   `N_M(t)~D_{h,sigma}t^(-2/sigma)` and
   `s_n(M)~(D_{h,sigma}/n)^(sigma/2)`, with
   `D_{h,sigma}=zeta(h sigma)^(1/sigma)/zeta(h)`.
   Let
   `N_lambda(t)=#{m in F_h:|m^{-s/2}|>=t}`; because the nonzero eigenvalues
   are simple, this is their count by modulus. It obeys
   `N_lambda(t)~zeta(h)^(-1)t^(-2/sigma)`, equivalently
   `|lambda_n|~((1/zeta(h))/n)^(sigma/2)`.
   At the exact crossover `C_{h,1}=D_{h,1}=1`; no ordering of the two
   constants is claimed away from one.
9. For `0<q<infinity`,
   `[S^*,S] in S_q` iff `sigma q>1`, and
   `[M^*,M] in S_q` iff `sigma>1/h` and `sigma q>1`.
   For `h=2` and `sigma>1/2`, the Hilbert--Schmidt norm is the exact
   difference of two separately convergent Euler products; no endpoint
   subtraction is asserted.

## Planned section architecture

### 1. Introduction

- Lead with the isospectral/non-similar band, not with generic weighted
  composition.
- State the paired theorem informally and list three concrete contributions:
  the exact phase classification, the primorial/Weyl metric laws, and the
  commutator wall.
- Explain that equal determinants are a negative control, not a determinant
  construction.
- State the result firewall and the role of canonical evaluation.

### 2. Arithmetic fibers and rank-one blocks

- Define `F_h`, `tau_h`, `omega_h`, and the algebraic basis maps.
- Derive both fibers directly from valuations.
- Decompose `ell^2(N)` into orthogonal target fibers.
- Compute the unique block singular values and `T_m^k=lambda_m^(k-1)T_m`.
- Distinguish algebraic prescription, eigenvalue, singular value, and Riesz
  norm at first use.

### 3. Existence, Schatten powers, and the common cyclic ledger

- Prove exact boundedness/compactness domains.
- Derive positive Euler products for power-Schatten membership and retain
  strict endpoints.
- Prove simplicity of the common nonzero spectrum.
- State trace and determinant identities only on their legal common domains.
- Include a compact comparison table separating shared cyclic data from
  different metric data.

### 4. Isospectrality without bounded similarity

- Express every Riesz idempotent norm as block norm divided by eigenvalue
  modulus.
- Prove the uniform-projection necessity and the block graph-transform
  sufficiency for bounded similarity to a compact normal diagonal.
- Identify the normal model explicitly as the orthogonal direct sum of the
  scalar eigenvalues `m^{-s/2}` on the eigenlines and zero on the transformed
  block kernels.
- Display the exact phase diagram and emphasize the band
  `1/h<sigma<=1`.

### 5. Primorial growth of saturated spectral projections

- Prove the exact optimizer by cardinality and prime-exchange arguments.
- Apply PNT, Mertens, and prime-sum asymptotics.
- Record the mandatory subcritical coefficient
  `(h-1)^(sigma-1)/(2(1-sigma))`.
- Pair the theorem with the three canonical finite optimizer checks, clearly
  labelled in Appendix C as implementation checks rather than asymptotic
  evidence. Section 5 itself will not use them.

### 6. Singular-value Weyl laws and the crossover

- Introduce the generalized weight `w_{h,sigma}`.
- Factor `F=zeta*G`, prove the local cancellation and holomorphic strip,
  identify the positive residue, and state the exact Wiener--Ikehara
  hypothesis.
- Invert the count for `S`; use `h`-free density for `M` and for eigenvalues.
- Prove `C_{h,1}=D_{h,1}=1`; explicitly decline an ordering away from one.
- State explicitly that no asymptotic or endpoint conclusion in the section
  depends on finite records.

### 7. Self-commutator ideals

- Derive the two singular values of a rank-one self-commutator.
- Prove sufficiency from the squared block scale.
- Give separate necessity families for `h>=3` and `h=2`.
- State the exact `h=2` Hilbert--Schmidt Euler identity and prohibit endpoint
  subtraction of divergent products.
- State explicitly that no ideal endpoint is inferred from a finite block.

### 8. Independent evaluation and limitations

- Give one short, anonymous summary of independent map-to-matrix,
  exponent-to-Euler, proof-audit, and finite-comparison routes.
- Keep exact hashes, route inventories, mutation counts, and case rows out of
  the main text; bind them only in Appendix D as reproducibility metadata.
- State what the evaluation does and does not establish.
- Close with the free-UFD negative control and the precise theorem boundary.

### Appendices

- A. Graph-transform similarity lemma.
- B. Regularized determinant legality.
- C. Tauberian local-uniform convergence details.
- D. Canonical case inventory and hash-bound reproducibility ledger.

### Dependency note

Section 3 uses only the exact fibers and block identities of Section 2.
Section 4 uses the block Riesz formulas, compactness, simplicity of the
nonzero eigenvalues, and the explicit diagonal model; necessity follows by
conjugating orthogonal spectral projections, while sufficiency uses a
uniform direct sum of block graph transforms. Section 5 uses only the exact
saturated Riesz product from Section 4 and classical prime asymptotics.
Section 6 uses the block masses from Section 2 plus positive generalized
Dirichlet-series analysis. Section 7 uses the rank-one block angle and mass
formulas, not any Weyl result or finite evaluation.

## Figure and table plan

1. **Fiber schematic** (vector TikZ): the same `h`-free fixed points with
   saturated rays versus modulo-`h` power fibers. Purpose: make the source of
   common eigenvalues and different masses visible.
2. **Phase diagram** (vector TikZ): boundedness, similarity, operator
   Schatten, and commutator walls as exact inequalities. Purpose: compare
   four thresholds without hiding the modulo existence condition.
3. **Primorial evidence panel** (Appendix D only; generated TeX from a
   hash-bound canonical extract): the three exact finite optimizer rows.
   Purpose: display implementation checks without suggesting a numerical
   proof.
4. **Shared-versus-distinct ledger table**: spectrum/traces/determinants
   versus fiber masses/Riesz norms/similarity.

All generated figures and tables will read a candidate-local canonical
summary extracted from the sealed result JSON. The source script will verify
the input hashes before reading data; no expected numerical table will be
hardcoded into a plotting script.

## Related-work and citation plan

Primary records to cite and the narrow ownership assigned to each:

- Luan--Khoi (2015), DOI `10.1090/conm/645/12907`: generic boundedness,
  compactness, closed range, and essential norm for weighted composition on
  weighted Hilbert sequence spaces.
- Carlson (1990), DOI `10.1090/S0002-9947-1990-0979958-6`: spectrum and
  commutant context for weighted composition on discrete `L^2` spaces.
- Abanin--Mannanikov (2023), DOI `10.46698/x5057-2500-3053-t`: the broader
  quasi-Banach weighted-sequence setting and its topological criteria.
- de Weger--van de Woestijne (1999), DOI
  `10.4064/aa-90-4-387-395`: power-free-part terminology and arithmetic
  context.
- Classical tools will be named and used without novelty credit: Euler
  products, `h`-free density, PNT, Mertens, Wiener--Ikehara, compact spectral
  theory, Schatten ideals, and regularized determinants.

Proof/citation allocation is fixed as follows. Prime-exponent fibers,
rank-one blocks, endpoint witnesses, the graph transform, Euler products,
the `h`-free density calculation, local Tauberian cancellation, residue,
positivity, and asymptotic inversion will be proved in the paper. The exact
Wiener--Ikehara theorem invoked, PNT/Mertens/prime-sum asymptotics, standard
quasi-Schatten terminology, and existence theory for regularized
determinants will be cited precisely, with all hypotheses checked locally.

No citation is used as evidence for the new paired arithmetic theorem. A
bounded source search failing to find an exact collision is not turned into a
priority assertion.

## Reverse-outline and review gates

Before final sealing, every paragraph must serve one of: definition,
theorem, proof step, evidence boundary, related-work subtraction, or
limitation. Generic tutorial material that does not support a claim will be
deleted.

Required gates:

1. GPT-5.4 xhigh review of this plan; repair every mathematical or narrative
   issue before LaTeX drafting.
2. Complete modular LaTeX draft and fresh deterministic compile at fixed
   epoch A.
3. Two full-paper GPT-5.4 xhigh improvement rounds, each preserving the
   incoming PDF and raw review.
4. Fresh fixed-epoch B rebuild; citation/reference scan; font embedding,
   text extraction, bounding-box/C0, and per-page visual audit.
5. Replay the protected50 snapshot byte-for-byte and metadata-for-metadata.
6. Write a self-excluding manifest, writer report, and handoff seal. Final
   candidate status is `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`, never a self-
   assigned clean verdict.
