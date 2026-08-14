# Paper 7 Phase-3 post-fix independent mathematical and reproducibility review

Review date: **2026-08-14 (Asia/Shanghai)**  
Review status: **COMPLETE — ACCEPT; M1--M4, m1--m2, AND THE EXACT-BYTE M5
RE-LOCK PASS**  
Scope: the amended Phase-3 protocol/candidate/proof snapshot, deterministic
controls, P7-1--P7-9 status, source ownership, and the frozen Route boundary  
Write boundary: this report only; all submitted protocol, candidate, proof,
source, code, result, roadmap, and Route files were treated as read-only  
Reviewer independence: a separate post-fix reviewer; no authorship of the
submitted amendments or controls; same model family, with no cross-model claim

## 1. Executive decision

The repaired snapshot closes every blocking item in
`phase3_peer_review.md`.  In particular:

- the amended protocol now distinguishes affiliated noncommutative `L1` from
  the bounded relative trace ideal and names only the branch-fixed scalar
  `D_tau^pr`;
- the proof supplies a concrete local and global faithful normal semifinite
  trace argument for arbitrary increasing nets;
- `s -> K_s` and `Log_0(I-K_s)` are proved holomorphic/convergent in the
  combined norm `||.||+||.||_1`, not merely in trace norm;
- the actual frozen quotient `B_p` is proved infinite, and its Haar `L2` is
  proved infinite-dimensional without relying on a generic control base;
- every determinant-side table now makes
  `log_Z=-tau_Log_D`, `D=exp(tau_Log_D)`, and `Z=D^(-1)` explicit; and
- `verify()` now locks the exact implementation-file set and hashes, with
  positive tamper, missing-entry, and extra-entry rejection tests.

No new counterexample or open proof dependency was found.  The result remains
strictly a proxy theorem: P7-9 closes as a negative source-ownership
certificate, unit masses remain a modeling choice, coordinatewise Route
credit remains forbidden, A4 is not invoked, and Route B remains closed.

```text
Critical findings: 0
Major findings:    0
Minor findings:    0
Decision:          ACCEPT
M5 exact-byte lock: PASS
Phase-3 gate:      CLOSED
```

Two downstream propagation actions follow from, rather than qualify, this
decision: `composition_blueprint.md` must cite the superseding hashes and this
report, and manuscript prose must use the strict restricted-Morishita wording
already frozen in `phase3_lock_ef_review.md`.  Neither action changes the
mathematics reviewed here.

## 2. Frozen inputs and exact-byte integrity

All requested hashes matched before review and again after the full
reproduction run.

| Record | Independently observed SHA-256 | Role |
|---|---|---|
| `notes/research_protocol.md` | `2f8dc9a802cfcf8b578db24419909de710563ece62cf026e9848fac437ba1581` | amended normative protocol |
| `notes/candidate_lock.md` | `73314bb031f663e8532a922821e66b20f31bd6f20b06a801a25147d6e55a17a0` | amended candidate/domain lock |
| `notes/proof_audit.md` | `febcd43e5d23daf893816b815c81f19ee4da5bac42a554d553262784660f00b5` | repaired P7-1--P7-8 proof |
| `notes/phase3_protocol_amendment.md` | `b8c55c5a2ebd4f22f6990671d03b2e1d997ce180e7638ed933b20471374eb03c` | versioned M1--M4 crosswalk |
| `notes/phase3_peer_review.md` | `8d9a246334ce4538d238050ffe85753ed6740c59c5347067983447b2cb7aea22` | findings being re-reviewed |
| `notes/source_audit.md` | `a6a0e75aa2a5f38e8c60a5ce34ffb536438f93828501e282a2d0ecb530847d53` | P7-9 ownership authority |
| `notes/operator_source_audit.md` | `69a76991c94cab24652c8d7d9f71c47a8eba70fcd7d1d4148689d47ff56e8b04` | trace/determinant terminology authority |
| `notes/phase3_lock_ef_review.md` | `4c525e269d256bd5ccfb6e18d114de00f8a13d31987965d7f0c6e77d1e1c8beb` | prior `E_f`/strict-nonsurjectivity audit and historical-lock record |
| `code/packet_trace_controls.py` | `2bfce3c29964d780e464e869cffa65ba578acdfd23d174c5ccba2d7b253245f0` | control implementation |
| `code/test_packet_trace_controls.py` | `9d2078c59050b1d685a1d0f43cb8e104d80f48c185abd5c7095a3681b6122fd8` | regression and tamper tests |
| `experiments/reproduce.sh` | `efbdddf269cd5393214430e77088d52120ae64ffd8611877a9a1906d128982d1` | complete reproduction entry point |
| `results/packet_trace_manifest.json` | `fe12ec4c6b0a950d35d267c830119945652acafb9a5ddae2aa6b86db92943b26` | artifact and implementation manifest |

The four-source ownership checksum manifest was also rerun: all four PDFs and
all four ARS preflight sidecars returned `OK`.  The unchanged source/operator
audits deliberately retain their historical protocol/candidate input hashes;
the versioned amendment and this review, rather than silent edits to frozen
source audits, provide the superseding crosswalk.

## 3. Re-review of the five former Major findings

### M1 — bounded versus affiliated domains and determinant naming: PASS

The historical ambiguous statement remains quoted as superseded, so the
preregistration deviation is visible rather than retroactively erased.  The
normative theorem now states separately

```text
K_s in affiliated L^1(M,tau_m)
  iff sum_p m_p p^(-Re(s)) < infinity;

K_s in L^1_tau(M)=M intersect L^1(M,tau_m)
  iff Re(s)>=0 and sum_p m_p p^(-Re(s)) < infinity.
```

The second condition contains the necessary boundedness test because
`||K_s||=sup_p p^(-Re(s))` is finite exactly for `Re(s)>=0`.  The determinant
domain is the open set

```text
H_m={s:Re(s)>max(0,sigma_c(m))},
```

so both summability and `||K_s||<1` hold locally.  If
`sigma_c(m)=+infinity`, the domain is honestly empty; if it is `-infinity`,
the strict positive-real-part norm gate remains.  For unit masses all three
conditions coincide exactly on `Re(s)>1`.

The only complex name used normatively is

```text
D_tau^pr(s)=exp(tau_m(Log_0(I-K_s))),
Z_m(s)=(D_tau^pr(s))^(-1).
```

The files explicitly exclude an ordinary Fredholm determinant, a complex
Fuglede--Kadison determinant, a “Breuer determinant,” a global scalar
de la Harpe--Skandalis determinant, and a Ruelle determinant.  M1 is closed.

### M2 — concrete local/global faithful normal semifinite trace: PASS

The local proof uses the direct-integral algebra

```text
M_p=integral_(B_p)^direct-sum B(Kappa_(L_p))dmu_p(b)
```

and integrates the ordinary fiber trace.  Fiber traciality and faithfulness
pass under integration, and the stated direct-integral theorem supplies
normality for arbitrary increasing nets.

Semifiniteness is not inferred from a single central summand.  For
`A_p>=0`, the proof takes the circle-mode projections `Q_(p,N)` and the
congruence cutdowns

```text
A_p^(N)=A_p^(1/2)(1 tensor Q_(p,N))A_p^(1/2).
```

These cutdowns are ordered, satisfy `0<=A_p^(N)<=A_p`, converge strongly to
`A_p`, and have finite trace bounded by `||A_p||(2N+1)`.  The congruence form
is essential and is used correctly.

Globally, finite-prime/finite-mode pairs `(F,mathbf N)` form a directed net
increasing strongly to any bounded positive `A`.  Every term has finite
weight because `F` is finite and every frozen `m_p` is positive and finite.
For an arbitrary increasing net `A_i up A`, the proof establishes

```text
sup_i sum_p m_p tau_p(A_(i,p))
  = sum_p m_p sup_i tau_p(A_(i,p))
```

by first choosing a common upper index on each finite prime set, then taking
the supremum over finite sets.  This closes both normality and semifiniteness
at the global level and supports every later bounded-`L1` use.  M2 is closed.

### M3 — relative-norm holomorphy and logarithm series: PASS

On a compact `C subset H_m`, the proof chooses
`sigma_c(m)<sigma_0<a=min_(s in C)Re(s)`.  For every derivative order `k`,
the trace-norm estimate absorbs `(log p)^k` into the gap `a-sigma_0`, while
the independent operator tail satisfies

```text
sup_(p>P)(log p)^k p^(-a) -> 0.
```

Thus finite-prime entire truncations converge locally uniformly in both
operator norm and trace norm, proving Banach-valued holomorphy in

```text
||X||_rel=||X||+||X||_(1,tau_m).
```

For the logarithm, with `q=2^(-a)<1`, the two required estimates are

```text
||K_s^r|| <= q^r,
||K_s^r||_(1,tau_m) <= S_m(a)q^(r-1).
```

They give locally uniform convergence of
`sum_r K_s^r/r` in the combined norm.  The commuting diagonal blocks also
give a locally uniformly convergent derivative series.  Continuity of the
trace on the relative ideal then yields the holomorphic, nonvanishing scalar
and licenses the locally absolutely convergent trace-log/product
calculation.  No `L1`-only completeness shortcut remains.  M3 is closed.

### M4 — infinitude of the actual frozen base and ordinary multiplicity: PASS

The repaired proof works with the actual quotient

```text
G_p=product_(ell!=p)Z_ell^x,
H_p=p^Zhat,
B_p=G_p/H_p.
```

The coordinate sign subgroup
`S_p isomorphic to product_(ell odd,ell!=p)C_2` is infinite, while a
procyclic profinite group has at most one nonidentity involution.  Hence
`|S_p intersect H_p|<=2`, so the image of `S_p` in `B_p` is infinite.  This
argument does not require injectivity of the exponent map defining `H_p`.

For every `N`, compact Hausdorff separation gives `N` pairwise disjoint
nonempty open subsets of the infinite compact group.  Each has positive Haar
measure, so their indicator functions are nonzero and pairwise orthogonal.
Therefore `L2(B_p,mu_p)` is infinite-dimensional.  It follows that
`I_(L2(B_p)) tensor |e_0><e_0|` has infinite ordinary Hilbert rank, although
its semifinite trace is one.  The ordinary Fredholm determinant is therefore
unavailable in the intended representation for every nonzero block.  M4 is
closed.

### M5 — independent exact-byte re-lock: PASS

This review attaches a new content verdict directly to the hashes in Section
2.  It does not inherit either the historical Phase-1 lock or the earlier
old-hash Gate-A review.  The amended protocol and candidate satisfy all eight
original closure conditions:

| Gate | Post-fix verdict |
|---|---|
| component trace / global `L1` / positive-time distribution separation | **PASS** |
| separate `K_s` analytic owner and branch-fixed determinant convention | **PASS** |
| four disjoint candidate IDs | **PASS** |
| no groupoid or flow-generation overclaim | **PASS** |
| target-free unit-mass provenance obligation retained | **PASS** |
| complete same-object transport field list retained | **PASS** |
| proxy restarts A0; no A3/A4/Route-B promotion | **PASS** |
| no global-smearing trace outside the global `L1` domain | **PASS** |

The old-to-new amendment crosswalk is complete, and the exact amendment hash
is independently supplied in Section 2.  M5 is closed for this snapshot.

## 4. Re-review of the two former Minor findings

### m1 — `log Z` versus `tau Log D`: PASS

The primary functions and every determinant-related CSV now distinguish

```text
tau_Log_D = sum_j m_j log(1-exp(-sigma L_j)) < 0,
log_Z     = -tau_Log_D > 0,
D         = exp(tau_Log_D),
Z         = exp(log_Z)=D^(-1).
```

The legacy `trace_log_*` and `compiled_inverse_product` function names remain
only as documented compatibility wrappers whose docstrings identify their
outputs as `log_Z`/`Z`.  The new regression test checks sign, reciprocal, and
compiled-product identities.  Across the 72-row finite-prime ledger, the
maximum sign and reciprocal residuals are exactly zero; the maximum
finite-product residuals are `4.4408920985006262e-16` for `D` and
`2.6645352591003757e-15` for `Z`.  m1 is closed.

### m2 — implementation-hash verification and tamper rejection: PASS

The manifest freezes six reproduction files relative to the Paper-7 root.
`verify()` now requires the manifest key set to equal the frozen set exactly,
rejects missing or extra entries, and verifies each required file and recorded
hash.  The unit suite independently:

- tampers with a generated CSV and observes verification failure;
- copies the complete code/experiments/results tree, tampers with an
  implementation README, and observes an implementation-hash failure;
- removes one implementation entry and observes a set-mismatch failure; and
- adds one implementation entry and observes a set-mismatch failure.

The full reproduction invokes `--verify-only` after regeneration, so the
stored artifact and implementation hashes are checked in the release path.
m2 is closed.

## 5. Independent reproduction receipt

The following release entry point was rerun from the Paper-7 directory:

```text
./experiments/reproduce.sh
```

Observed results:

```text
unit tests:                     21/21 PASS
generated CSV artifacts:       9
total CSV data rows:            407
max_prime:                      5000
prime_count:                    669
current-tree manifest verify:   PASS
temporary regeneration one:    PASS
temporary regeneration two:    PASS
current vs temporary bytes:     identical
temporary one vs two bytes:     identical
manifest SHA-256:               fe12ec4c6b0a950d35d267c830119945652acafb9a5ddae2aa6b86db92943b26
```

The controls remain finite regression witnesses.  They use no network,
randomness, external datasets, fits, Riemann zeros, or target-selected
parameters, and they do not prove an infinite sum, a source transport, an
analytic continuation, or a Route verdict.

## 6. P7-1--P7-9 post-fix disposition

| Target | Post-fix verdict | Exact surviving boundary |
|---|---|---|
| **P7-1** | **PASS** | Component Fourier eigenvalues, trace-class lattice sum, probability-base normalization, and Poisson factor are correct; M2 now supplies the FNS foundation. |
| **P7-2** | **PASS** | The global block is bounded; for nonzero `f`, global bounded-`L1` membership is equivalent to `sum_p m_p log p<infinity`; unit masses fail. |
| **P7-3** | **PASS** | The positive-time ledger is a locally finite Radon measure; outside global `L1` it is not written as `tau_m(C_f)`, and no zero-time regularization is claimed. |
| **P7-4** | **PASS, VERSIONED CORRECTION** | Affiliated summability and bounded-relative membership are distinct; unit masses still give exactly `Re(s)>1`. |
| **P7-5** | **PASS** | Relative-norm holomorphy, local principal trace-log scalar, product identity, actual-base ordinary multiplicity, and determinant taxonomy are all closed. |
| **P7-6** | **PASS, SCOPED** | Positive finite sequences classify only the frozen central-scalar trace family, not every FNS trace; copying remains additive. |
| **P7-7** | **PASS** | Target logarithmic-derivative equality forces `m_p=1`, but this target-conditioned uniqueness supplies no provenance. |
| **P7-8** | **PASS** | Both branches are probability-base blind; locally finite clocks compile the positive-time ledger, while the determinant branch separately requires summability, boundedness, and strict norm control. |
| **P7-9** | **PASS AS A SCOPED NEGATIVE OWNERSHIP CERTIFICATE** | The source owns packets, repetitions, and clocks, but no audited theorem transports measure, algebra, trace, zero mode, analytic family, or determinant to the proxy. |

P7-1--P7-8 therefore close only on their typed proxy owners.  P7-9 is not a
positive bridge theorem and cannot be merged coordinatewise with those proxy
results.

## 7. Source ownership and Route-boundary drift audit

The source audit bytes and ownership source manifestations are unchanged.
The post-fix protocol/candidate amendment changes only the Branch-K operator
domain and determinant name.  It does not change the following ownership
classification:

```text
prime packet / repetitions / log p clock        SOURCE_THEOREM
abstract normalized Haar on B_p                 DERIVABLE_NEW_LEMMA
prime closed-point counting measure             DERIVABLE_NEW_DEFINITION
proxy product/Borel/measure/algebra/trace        MODELING_CHOICE
central m_p=1 trace weights                      MODELING_CHOICE
P_0 / K_s / D_tau^pr                            PROXY-OWNED THEOREM TARGETS
source-to-proxy analytic transport               NOT FOUND / NOT TESTABLE
```

The repaired Morishita statement also remains unchanged: on Deninger's
`E_f` subsystem there is a continuous flow-anti-equivariant intertwiner;
every source circle in `Gamma_p` maps onto the same target circle `C_p`, so
transverse labels collapse.  It is strictly not globally onto the whole
adelic target because every source image has at most one finite zero
coordinate, whereas target classes with two finite zero coordinates exist.
No measure, Haar disintegration, algebra, trace, representation, zero mode,
or determinant is transported.

Against the Route roadmaps, the amended files preserve every cap:

- the original and the three proxy records remain different candidates;
- the proxy restarts A0 and cannot inherit the original packet's A0/A1
  credit;
- source A0/A1 and proxy A2-like exactness cannot be combined by coordinatewise
  maxima;
- a right-half-plane reciprocal Euler product supplies no continuation,
  functional equation, Gamma factor, completed divisor, counting law, or
  Weil-compression credit at A3;
- probability-base and arbitrary-clock controls retain the explicit
  `STOP_SCOPED / PROVES_TOO_MUCH` warning;
- A4 is not invoked; and
- Route B has neither the required Route-A-ready entry verdict nor a
  same-object operator/domain/self-adjointness chain, so it remains closed.

This is a no-drift audit, not a fresh Route-YAML verdict.

## 8. Final release block

```text
[P7-PHASE3-POSTFIX-RELOCK]
protocol_sha256: 2f8dc9a802cfcf8b578db24419909de710563ece62cf026e9848fac437ba1581
candidate_sha256: 73314bb031f663e8532a922821e66b20f31bd6f20b06a801a25147d6e55a17a0
proof_sha256: febcd43e5d23daf893816b815c81f19ee4da5bac42a554d553262784660f00b5
amendment_sha256: b8c55c5a2ebd4f22f6990671d03b2e1d997ce180e7638ed933b20471374eb03c
manifest_sha256: fe12ec4c6b0a950d35d267c830119945652acafb9a5ddae2aa6b86db92943b26
source_audit_sha256: a6a0e75aa2a5f38e8c60a5ce34ffb536438f93828501e282a2d0ecb530847d53
operator_source_audit_sha256: 69a76991c94cab24652c8d7d9f71c47a8eba70fcd7d1d4148689d47ff56e8b04
closure_conditions: 8/8 PASS
historical_pass_inherited_without_review: false
M1_M4: CLOSED
m1_m2: CLOSED
P7_1_P7_8: PASS_ON_TYPED_PROXY_OWNERS
P7_9: PASS_SCOPED_NEGATIVE_OWNERSHIP
source_route_boundary_drift: NONE
decision: ACCEPT
```

The report's own SHA-256 is intentionally not embedded in itself.  It must be
computed after the final byte and propagated with this release block.
