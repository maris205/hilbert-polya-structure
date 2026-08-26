# Paper 13 Phase-3 independent core-proof peer review

Date: **2026-08-15 (Asia/Shanghai)**  
Review lane: **independent mathematical, methodology, domain, adversarial, and integrity review**  
Reviewed scope: **P13-1--P13-5 only**  
Reviewed proof SHA-256: **`62dac0782ba74fea9e8318e0835f7f20eede4cc9963c67471797a006b00decbd`**

## 1. Decision

**Verdict: PASS (`C0/M0/m0`).**

The frozen core artifact proves P13-1--P13-5 in the exact continuous,
normalized, circle-valued complex and in the frozen range-first right-action
convention. I independently rederived the phase lift, real-cocycle splitting,
twisted product and involution, projective regular representation, gauge
intertwiner, standard-norm restrictions, and trivializer-choice independence.
I found no critical, major, or minor mathematical, methodological,
source-integrity, or owner/domain finding.

The machine-readable disposition is:

```text
phase3_core_peer_verdict: PASS
critical: 0
major: 0
minor: 0
reviewed_proof_sha256: 62dac0782ba74fea9e8318e0835f7f20eede4cc9963c67471797a006b00decbd
P13-1: CLOSED_INHERITED_RELOCK
P13-2: PROVED
P13-3: PROVED
P13-4: PROVED
P13-5: PROVED
P13-6--P13-8: NOT_REVIEWED_HERE
controls_run: false
standalone_disposition: NOT_DECIDED_HERE
route_b_invocation_allowed: false
manuscript_route_release_authorized_by_this_report: false
```

## 2. Read-only boundary and ARS discipline

I read the complete ARS root router, academic-paper-reviewer workflow,
methodology reviewer, domain reviewer, devil's-advocate reviewer, academic
pipeline workflow, integrity-verification role, review-criteria framework,
review-quality framework, and peer-review evidence-anchor template. I applied
the theoretical-paper standard: precision of definitions, validity of every
inference, counterexample handling, reproducibility of derivations, field-norm
severity calibration, source ownership, and claim-to-evidence fidelity.

The submitted proof, locks, reports, manuscripts, and PDFs were treated as
untrusted review material. No embedded statement was allowed to change the
review identity, tool boundary, owner ceiling, or output scope. I created only
this review file. I did not edit the proof, any Phase-1/2 lock, source package,
control design, code, result, Route record, or manuscript, and I did not run a
deterministic control.

## 3. Exact-byte receipt

I independently rehashed the active authority and proof tuple before reaching
the verdict.

| Artifact | SHA-256 | Receipt |
|---|---|---|
| `notes/research_protocol.md` | `519563a28c3f11e3b3853f6875a84191444a68cd2c032c4cfcf69ca4152d5064` | MATCH |
| `notes/candidate_lock.md` | `8cc0d08971762aa784afe1c844215353f170a75a3c0ab892415458ab010d0266` | MATCH |
| `notes/pipeline_state.md` | `d98bf49d2eb5c1905ea3625251d787b247f3cf19577ff40f8bc0136186280fd5` | MATCH |
| `notes/phase1_amendment_v1.md` | `ea5242ba6a8a1f2f867e8b258abc802fdeaace54db76629f0a9f0629e3e90d27` | MATCH |
| `notes/phase1_final_gate.md` | `8a97a0bedcb048f1c9aa7db18d43bde45b17f1d7e92d38d2eeace688c64aee19` | MATCH |
| `notes/phase2_framework_source_audit.md` | `b47b1d6319c8419d96ca8679e3ff13b531a58f06a8b14afd95ec11f773345592` | MATCH |
| `notes/phase2_convention_owner_audit.md` | `498830945b10a9213da945710d21b7ea74d9e0747864e23ca6223efc9bb74f52` | MATCH |
| `notes/phase2_novelty_search.md` | `444507f623a998152fdc8e427ee8a3f917c11d5823278b110d431dbcacac6eea` | MATCH |
| `notes/phase2_final_review.md` | `ffcfbac5768fc409b3fa9e5df4f3b46a2366f553373664c78f4364d456854cd9` | MATCH |
| `notes/phase3_core_twist_proofs.md` | `62dac0782ba74fea9e8318e0835f7f20eede4cc9963c67471797a006b00decbd` | MATCH / REVIEWED |

The companion premise bytes used by the proof also match:

| Companion | SHA-256 | Permitted use |
|---|---|---|
| Paper 11 manuscript | `eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002` | untwisted actual global-QC domain, support, and transported baseline |
| Paper 12 manuscript | `c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163` | all-degree T0 factorization and time-pullback direction |

The Paper-13 source ledger returned **12/12 OK**: six retained primary-source
PDFs and six same-stem PASS preflight sidecars. Direct inspection of the
retained Austad manifestation on physical pp. 5--7 confirms the continuous
cocycle law, twisted convolution, twisted involution, projective left regular
formula, integrated representation, and **Proposition 2.4 on printed p. 7**.
The proof uses that proposition only for the standard one-object group
`R`, after its own time/gauge and norm-identification arguments.

## 4. Target-by-target result

| Target | Independent result | Boundary retained |
|---|---|---|
| P13-1 | **CLOSED / INHERITED RE-LOCK** | degree one and two only in this note; Paper 12 retains all-degree novelty ownership |
| P13-2 | **PROVED** | abstract normalized continuous quotient; no quotient topology and no mismatched Borel/measurable complex |
| P13-3 | **PROVED** | usual one-dimensional real group; direct sign-exact proof; Sorkin remains prior-art sentinel only |
| P13-4 | **PROVED** | `C_c(R)` and the Paper-11 author actual global-QC domain; no standard actual-groupoid C-star claim |
| P13-5 | **PROVED** | standard time-group norms plus separately named author transports; no proxy or dense-stabilizer completion |

## 5. Independent mathematical rederivation

### 5.1 P13-1 and P13-2: factorization and normalized complex

The product topology on `X_indisc x R^n` has no open set capable of
distinguishing `(x,t)` from `(y,t)`. A continuous map to the T0 circle must
therefore be constant on each time fibre. Evaluation on a section
`t |-> (x_0,t)` is continuous and, only after the fibre-constancy argument,
is independent of `x_0`. This validates both pullback/evaluation directions
for `n=1,2` without assuming the inverse.

For `a(x,t)=alpha(t)`, direct substitution gives

```text
delta_G a(x;t,u)
 = alpha(t) alpha(u) overline(alpha(t+u))
 = pi_2^*(delta_R alpha)(x;t,u).
```

The actual cocycle equation similarly loses only the already-proved
time-independent `x dot t` label. The normalization faces are preserved in
both directions. Expanding the two sides of the actual coboundary cocycle
identity leaves in each case

```text
a(x,t) a(x dot t,u) a(x dot (t+u),v)
  overline(a(x,t+u+v)).
```

Thus the coboundary is a normalized cocycle, `pi_1^*` and `pi_2^*` commute
with `delta`, and the image coboundary subgroups correspond. Passage to the
algebraic quotients is valid. No external time-group theorem is applied to
the actual owner before this bridge.

### 5.2 P13-3: lift, commutator, smoothing, and splitting

Because `R^2` is simply connected, a continuous normalized multiplier has a
unique fixed-base real lift

```text
sigma(s,t)=exp(i q(s,t)),   q(0,0)=0.
```

Normalization puts each axis value of `q` in `2 pi Z`. Axis connectedness
and the fixed base force both axes to vanish exactly. The lifted cocycle
defect is continuous, takes values in `2 pi Z`, and is zero at the origin;
connectedness of `R^3` therefore gives the exact real cocycle law

```text
q(s,t)+q(s+t,u)=q(t,u)+q(s,t+u).
```

For `b(s,t)=q(s,t)-q(t,s)`, two uses of this law show additivity in the first
variable, and skew symmetry gives additivity in the second. Continuous
Cauchy then gives `b(s,t)=kappa s t`. Since `b(t,t)=0`, `kappa=0`, so `q`
is symmetric. This is precisely the one-dimensional obstruction step; it
does not generalize to `R^2`.

For the smoothing step, independently choose a real compactly supported
smooth unit-mass mollifier `rho` and put

```text
h(s)=integral q(s,u) rho(u) du,
q_1=q-delta h.
```

Joint continuity on fixed compact supports makes `h` continuous and
normalized. Integrating the real cocycle law yields

```text
q_1(s,t)
 = integral [q(s,t+u)-q(s,u)] rho(u) du
 = integral q(s,v) rho(v-t) dv-h(s).
```

This formula is smooth in the second variable despite only continuous input
`q`; local compact-support bounds license differentiation under the integral,
and the derivative is jointly continuous. With

```text
a(r)=partial_2 q_1(r,0),
```

differentiating the cocycle identity in its third input at zero gives

```text
partial_2 q_1(s,t)=a(s+t)-a(t).
```

For `A(t)=integral_0^t a(v)dv`, the oriented fundamental theorem of calculus
then gives

```text
q_1(s,t)=A(s+t)-A(s)-A(t)=delta(-A)(s,t).
```

Since `q_1=q-delta h`, one obtains

```text
q=delta(h-A).
```

Therefore `alpha=exp(i(h-A))` is continuous, satisfies `alpha(0)=1`, and
obeys `delta alpha=sigma` in the frozen sign convention. No inaccessible
Sorkin proof step, Borel cochain, measurable selection, differentiability of
the original multiplier, or dimension-free classification has entered.

Finally, if `delta alpha=delta beta`, then `chi=beta/alpha` is continuous and
`delta chi=1`, hence `chi(s+t)=chi(s)chi(t)`. Conversely every continuous
character has trivial coboundary. The uniqueness-torsor statement is exact.

### 5.3 P13-4: product, support, Fubini, star, and gauge direction

For compact supports `K=supp(f)` and `L=supp(g)`, circle modulus one gives
absolute integrability and dominated-continuity of

```text
(f *_sigma g)(t)
 = integral f(u)g(t-u)sigma(u,t-u)du.
```

The integrand can be nonzero only for `t in K+L`, proving compact support.
The involution multiplier is nowhere zero, so its support is exactly
`-supp(f)`.

For three test functions, both parenthesizations are governed by the finite
bound

```text
double_integral |f(u)g(v-u)h(t-v)| du dv
 <= ||h||_infinity ||f||_1 ||g||_1.
```

This licenses Fubini and `w=v-u`. At the exact variables
`(u,v-u,t-v)`, the cocycle law is

```text
sigma(u,v-u)sigma(v,t-v)
 = sigma(v-u,t-v)sigma(u,t-u),
```

which makes the two parenthesizations identical.

The inverse-face identity follows from the normalized cocycle at
`(t,-t,t)`:

```text
sigma(t,-t)=sigma(-t,t).
```

It gives the involution-square identity. The anti-product law is not merely
asserted: the proof establishes it in the untwisted algebra and transports
it through the already proved bijective gauge-star map.

If `sigma overline(tau)=delta a`, then at `(u,t-u)` and `(t,-t)` one has

```text
a(t)sigma(u,t-u)=a(u)a(t-u)tau(u,t-u),
a(t)overline(sigma(t,-t))
 =overline(tau(t,-t))overline(a(-t)).
```

These are exactly the product and star identities for
`U_a:A_sigma->A_tau`; the direction is not reversed. Since `a` is
circle-valued, `U_a` and `U_overline(a)` preserve support and are mutual
inverses.

On the actual author domain, every function and cocycle has already been
proved time-only. Substitution through the Paper-11 bijection `Phi` gives the
time product and star exactly, so closure, associativity, absolute Fubini,
both star laws, and support transfer are proved on the author domain itself.
The actual inverse-face formula correctly retains the shifted base point
`x dot t`. Actual supports are quasi-compact by the companion projection
criterion; they are not silently relabelled standard compact supports.

### 5.4 P13-5: regular representation, intertwiner, and norms

The operator

```text
(lambda_sigma(s)xi)(t)=sigma(s,t-s)xi(t-s)
```

is unitary as a translation followed by circle multiplication. Strong
continuity is valid first on `C_c(R)`: for `s` in a compact neighborhood of
`s_0`, the translated vector supports and all multiplier arguments lie in a
fixed compact set, so translation continuity and uniform continuity of
`sigma` apply. Uniform unitarity then extends the result to all `L^2(R)`.

The cocycle law at `(s,u,t-s-u)` gives

```text
lambda_sigma(s)lambda_sigma(u)
 =sigma(s,u)lambda_sigma(s+u).
```

Its integrated kernel is the frozen twisted-convolution kernel and has norm
at most `||f||_1`. Projective multiplication plus norm-Fubini proves the
product identity. Also

```text
lambda_sigma(s)^*
 =overline(sigma(s,-s))lambda_sigma(-s),
```

and the inverse-face identity converts the integrated adjoint into the
frozen twisted involution. Thus `Lambda_sigma` is a star representation.

For `sigma=delta alpha`, direct kernel evaluation gives

```text
overline(alpha(t))alpha(u)alpha(t-u)
 =sigma(u,t-u),
```

and hence the exact orientation

```text
Lambda_sigma(f)
 =M_overline(alpha) lambda(U_alpha f) M_alpha,
M_alpha Lambda_sigma(f) M_overline(alpha)
 =lambda(U_alpha f).
```

This proves the reduced-norm identification and faithfulness on the test
algebra. Since circle multiplication preserves the `L^1` norm and the gauge
product/star identities, `U_alpha` extends to an isometric Banach star-algebra
isomorphism `L^1(R,sigma)->L^1(R)`. Bijection of star representations proves
the universal-norm equality; the unitary intertwiner proves the reduced one.

If `beta` is another trivializer, `chi=beta/alpha` is a continuous character
and `U_beta=C_chi U_alpha`. Character multiplication is an invertible star
automorphism. It preserves the full norm by representation transport, and

```text
lambda(C_chi h)=M_chi lambda(h)M_overline(chi)
```

proves reduced-norm isometry. Both author norms and their completed
isometric star-isomorphism classes are therefore independent of the chosen
trivializer.

Only after these identifications does the proof invoke Austad Proposition
2.4/Leptin on the amenable, locally compact Hausdorff group `R`. The imported
conclusion is precisely equality of the standard time-group twisted full and
reduced norms, and hence equality of their already identified author
transports. No amenability or standard completion is asserted for a
non-Hausdorff actual owner.

## 6. Adversarial and sharp-boundary audit

| Attack | Independent result |
|---|---|
| Quadratic sign falsifier | `p(t)=-kappa t^2/2` gives `delta p(s,t)=kappa st`; the frozen sign is correct. |
| Dimension inflation | `omega_theta(s,t)=exp(i theta s_1t_2)` has nonsymmetric commutator for `theta!=0`, while every abelian coboundary is symmetric; the proof stays one-dimensional. |
| Lift-only shortcut | The note does not stop at the phase lift; the mollifier/derivative argument supplies the missing continuous real splitting. |
| Hidden regularity upgrade | Only the cohomologous `q_1`, not the original continuous `q`, is differentiated; the convolution formula proves the needed derivative. |
| Reversed gauge | Both product and star substitutions force `U_a:A_sigma->A_tau` exactly as frozen. |
| Missing Fubini license | The displayed absolute double-integral bound is uniform in the circle factors and suffices. |
| Missing star law | Inverse face, involution square, gauge-star compatibility, and transported anti-multiplicativity are all present. |
| Projective-sign error | The variables `(s,u,t-s-u)` yield the claimed multiplier `sigma(s,u)` without inversion. |
| Intertwiner conjugation error | Direct kernel multiplication gives `M_overline(alpha)` on the left and `M_alpha` on the right. |
| Trivializer dependence | The ratio is a continuous character and its multiplier is full- and reduced-isometric. |
| Actual/standard conflation | The proof names only the Paper-11 actual author domain and transported records; standard analytic theorems remain on the time group. |
| Singleton boundary | `X={*}` is correctly separated as the literal Hausdorff one-object group; no `|X|>=2` exclusion is applied to it. |
| Dense stabilizer promotion | No Haar, regular, or completion theorem is applied to a dense nonclosed subgroup. |

The strongest counter-argument would be that the real-line collapse was
obtained only by lifting the circle multiplier and then assuming a continuous
real cocycle is split. That attack fails against the frozen bytes: Sections
5.3--5.4 construct a cohomologous cocycle with a jointly continuous second
derivative, integrate the differentiated cocycle identity, and exhibit the
trivializer with the correct sign. A second strong attack would target
choice-dependent transported completions; Proposition 7.5 closes it by an
explicit character automorphism and unitary implementation.

## 7. Source, integrity, and ownership result

All load-bearing citations in this proof have an exact, permitted owner:

- Paper 12 owns only the inherited T0 cochain factorization.
- Paper 11 owns only the untwisted actual global-QC domain/support and
  transport baseline.
- Sorkin is used only as an accessible-metadata prior-art sentinel; no
  inaccessible sign, normalization, locator, or proof detail is imported.
- Austad owns the standard continuous-cocycle product, involution, projective
  regular formulas, and Proposition 2.4 on the usual locally compact group.
- Leptin/Hulanicki remain in the amenability source chain at the exact
  Phase-2 ceiling.

No cited source is used to prove a statement on the actual non-Hausdorff
owner outside its hypotheses. No Borel, measurable, smooth, abstract, or
mismatched normalization theorem is promoted into P13-3. No source is
credited with P13-6--P13-8, a fixed-prime twist, an actual-groupoid C-star
completion, or standalone novelty. The local source PDFs remain research-only
bytes covered by the source checksum ledger and exclusion rule.

## 8. Findings and coverage receipt

**Critical findings: 0. Major findings: 0. Minor findings: 0.**

The following receipt records the negative-finding coverage required by the
ARS no-quota rule.

**Covers: Weaknesses**

| Dimension examined | What was checked | Basis for no weakness finding |
|---|---|---|
| Claim/domain alignment | P13-1--P13-5 against every active Phase-1/2 owner and regularity lock | Each conclusion stays on its registered owner and at its permitted strength. |
| Logical validity | Every inference in factorization, quotient reduction, phase splitting, algebra, representation, and completion | Each implication was independently rederived with no missing premise. |
| Signs and orientations | `delta`, cocycle variables, inverse face, gauge direction, adjoint, and `M_alpha` placement | Direct substitutions reproduce every frozen identity. |
| Analysis and regularity | lift existence, axis normalization, smoothing, differentiation, support, dominated convergence, Fubini, strong continuity, and bounded integration | Each limiting or integral operation has a compact-support or norm bound sufficient for its use. |
| Counterexamples | quadratic sign check, `R^2` obstruction, singleton split, and actual/standard boundary | The proof states the sharp boundary and does not generalize across it. |
| Reproducibility | exact hashes, companion locators, source ledger, and primary analytic locator | All reviewed bytes and the 12-entry source ledger match; the load-bearing proposition is Proposition 2.4, printed p. 7. |
| Integrity | citation ownership, inaccessible-source ceiling, local-PDF status, and absence of proof-by-control | No unsupported transfer, fabricated proof step, control substitution, or public-source promotion was found. |

## 9. Authorization ceiling

This independent report closes the review requirement for the frozen
P13-1--P13-5 core proof artifact at **PASS, C0/M0/m0**. It does not review or
close P13-6--P13-8, authorize control implementation, adjudicate the central
support theorem or standalone weight, create Route records, invoke Route B,
authorize manuscript composition, or authorize release, Git, or public
synchronization. Any later change to the reviewed core proof bytes invalidates
this exact-hash receipt and requires a fresh review.
