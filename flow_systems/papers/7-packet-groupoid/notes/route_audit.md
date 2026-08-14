# Paper 7 object-specific Route-A v0.2.0 audit

Audit date: **2026-08-14 (Asia/Shanghai)**  
Audit status: **COMPLETE — FOUR OBJECTS EVALUATED; ROUTE B NOT INVOKED**  
Evaluator boundary: independent read-only evaluation of the accepted Phase-3
snapshot; this file and the four new YAML records are the only outputs

## 1. Evidence lock and method

The audit applies `route-a-evaluator` v0.2.0 separately to four frozen
candidate IDs. It also applies the Route-B same-object entry rule solely to
decide that Route B must remain closed; no Route-B YAML was created.

The load-bearing evidence snapshot is:

| Record | SHA-256 | Use |
|---|---|---|
| `research_protocol.md` | `2f8dc9a802cfcf8b578db24419909de710563ece62cf026e9848fac437ba1581` | normative object/domain/data freeze |
| `candidate_lock.md` | `73314bb031f663e8532a922821e66b20f31bd6f20b06a801a25147d6e55a17a0` | four-candidate ownership lock |
| `proof_audit.md` | `febcd43e5d23daf893816b815c81f19ee4da5bac42a554d553262784660f00b5` | P7-1--P7-8 proofs and controls theorem |
| `phase3_protocol_amendment.md` | `b8c55c5a2ebd4f22f6990671d03b2e1d997ce180e7638ed933b20471374eb03c` | affiliated/bounded/determinant crosswalk |
| `source_audit.md` | `a6a0e75aa2a5f38e8c60a5ce34ffb536438f93828501e282a2d0ecb530847d53` | source ownership and P7-9 |
| `operator_source_audit.md` | `69a76991c94cab24652c8d7d9f71c47a8eba70fcd7d1d4148689d47ff56e8b04` | trace/determinant terminology |
| `phase3_postfix_review.md` | `8527d940ccac52279ac857a9db7739e8a4d4849035d6a6a371aeaac7beacb475` | independent ACCEPT and exact-byte re-lock |
| `phase3_lock_ef_review.md` | `913f901d2afe648c10bddfbfd41f9a3d7356c2b5f99c87d459547810d596581b` | repaired `E_f`, strict non-surjectivity, and M5 closure addenda |
| `composition_blueprint.md` | `ec916a47cc77b7d6e731614d2f258f7c61ecb3317b405ad5fc0b094324a6cc7b` | typed-owner ceilings and no-splice rule |
| `packet_trace_manifest.json` | `fe12ec4c6b0a950d35d267c830119945652acafb9a5ddae2aa6b86db92943b26` | nine deterministic artifacts and implementation hashes |

The complete control suite was independently rerun during this audit:

```text
21/21 unit tests: PASS
manifest verification: PASS
generated artifacts: 9 CSV files, 407 data rows
max_prime: 5000 (669 primes)
two fresh regenerations: byte-identical
manifest SHA-256: fe12ec4c6b0a950d35d267c830119945652acafb9a5ddae2aa6b86db92943b26
```

These controls are `NUMERICALLY_CERTIFIED` only as finite implementation and
convention witnesses. The mathematical claims used below are `PROVED` by the
symbolic audit and independently accepted review, not by the finite tables.

## 2. Final object-level verdicts

| Candidate ID | Route-A tuple `(A0,A1,A2,A3,A4)` | Overall |
|---|---|---|
| `DEN-WITT-Z-FIN` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-WITT-PACKET-DECOMP-MASS-FAM` | `(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-WITT-PACKET-DECOMP-RETURN-DIST-M` | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |
| `DEN-WITT-PACKET-DECOMP-K0-M1` | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)` | `ROUTE_A_EXPLORATORY` |

Every candidate has `route_b_invocation_allowed: false`. The common overall
label does not mean the objects have interchangeable coordinates; it records
that none passes the complete arithmetic-orbit-determinant-global-analytic
chain.

## 3. Candidate-by-candidate rationale

### `DEN-WITT-Z-FIN`

The source retains `A0_ANALYTIC_ARITHMETIC_ORIGIN`: closed points `(p)`,
packets, `p^Z`, and `log p` are source theorems. It remains `A1_WEAK` because
the source packet contains an infinite transverse family of equal-period
circles without individual stability, phase, multiplicity weight, or trace
coefficient. The repaired `E_f` morphism is real progress but maps every
circle in `Gamma_p` onto the same adelic `C_p`, is strictly not globally
onto, and transports no measured/operator data.

The ordinary individual-orbit product is refuted, so A2 fails. Selected proxy
traces and the zero-mode scalar cannot repair that coordinate. With no
source-owned determinant, A3 and A4 remain untestable failures.

### `DEN-WITT-PACKET-DECOMP-MASS-FAM`

This is a rigorous operator-algebra host, but it restarts A0. Its relation to
the source is only choice-dependent at the set/clock level; product topology,
Haar disintegration, algebra, representation, and all central masses are
selected proxy data. That warrants `A0_WEAK_ARITHMETIC_RELATION` with
`MODELING_CHOICE`, not inherited analytic-origin credit.

The selected circle flow has an exact repeated-circle ledger but does not
derive arithmetic labels or isolated-orbit amplitudes, hence `A1_WEAK`. The
record deliberately defines neither the return distribution nor a
determinant. Its concrete faithful normal semifinite trace therefore gives no
A2 or A3 coordinate. The Hilbert representation is an algebra representation,
not a natural quantization, so A4 fails.

### `DEN-WITT-PACKET-DECOMP-RETURN-DIST-M`

P7-1--P7-3 prove the complete positive repetition measure

```text
Theta_m = sum_(p,r>=1) m_p log(p) delta_(r log(p)).
```

This is an analytic primitive/repetition ledger and receives
`A1_PASS_ANALYTIC`, with the caveat that amplitudes aggregate the selected
transverse probability measure and free masses. It does not receive a new A0
promotion beyond the parent proxy's weak relation.

That `A1_PASS_ANALYTIC` is strictly a theorem about the typed
`DEN-WITT-PACKET-DECOMP-RETURN-DIST-M` proxy ledger. It is not a theorem that
Deninger's individual source orbits own these amplitudes, not a transport of
the source packet's transverse multiplicity, and not credit for
`DEN-WITT-Z-FIN`. The original source therefore remains `A1_WEAK`.

The type boundary is decisive at A2: `Theta_m` is a locally finite Radon
measure, not `tau_m(C_f)` outside the global `L1` ideal and not any form of
zeta or determinant. Therefore A2 fails with `STOP_SCOPED`; the separate K0
scalar cannot be borrowed. There is consequently no A3 or A4 promotion.

### `DEN-WITT-PACKET-DECOMP-K0-M1`

P7-4--P7-5 prove a genuine relative-norm holomorphic scalar on `Re(s)>1`:

```text
D_tau^pr(s) = exp(tau(Log_0(I-K_s))) = product_p (1-p^(-s)),
Z(s) = D_tau^pr(s)^(-1).
```

This earns the object-specific verdict `A2_ANALYTIC_DETERMINANT`. The verdict
is about the branch-fixed proxy scalar only; it is not ordinary Fredholm,
Ruelle, a global complex Fuglede--Kadison determinant, or a completed divisor.

The other coordinates do not come along. Unit central mass remains
`MODELING_CHOICE`, so A0 is only weak. The projection `P_0` discards all
nonzero circle modes and the determinant is expressly not primitive-orbit
owned, so A1 fails. Right-half-plane exactness supplies none of the A3 global
obligations. The same formula survives singleton/arbitrary probability bases,
arbitrary locally finite clocks, and composite-augmented clocks; it therefore
triggers `STOP_SCOPED / PROVES_TOO_MUCH` for geometry, arithmetic, and Riemann
promotion. No natural quantization exists, so A4 fails.

#### Why this is `ROUTE_A_EXPLORATORY`, not `ROUTE_A_REJECTED`

The distinction from `SPECZ-TAUT-NORM-CIRCLES` is substantive rather than a
reward for having an exact product. `SPECZ-TAUT-NORM-CIRCLES` has `A0_FAIL`:
its entire phase space, one-circle-per-prime multiplicity, and `log p` roofs
are direct encodings of the target table; the exact orbit product is its only
positive role, arbitrary prescribed products behave identically, and its
frozen evaluation has no next test other than retaining it as a negative
control.

`K0-M1`, by contrast, has only `A0_WEAK_ARITHMETIC_RELATION`, not an A0 pass:
its host uses the independently arithmetic groups `B_p` and a
source-derived, choice-dependent packet/clock parametrization, and Paper 7
proves non-tautological operator facts on the actual infinite-base
representation (the affiliated/bounded domain split, faithful normal
semifinite trace, relative-norm holomorphy, and ordinary-Hilbert multiplicity
obstruction). Those facts remain true and research-useful even when the Euler
identity is denied any arithmetic or geometric evidential force. Two
falsifiable within-family questions remain open: target-free transport of
closed-point counting to the central trace masses, and construction of a
coefficient sensitive to actual `B_p` geometry. A positive or negative answer
could change the proxy program rather than merely recompile a prescribed
product.

Accordingly, `A1_FAIL` plus `STOP_SCOPED / PROVES_TOO_MUCH` blocks every
promotion of the present scalar and keeps the candidate outside primary
HP-Dynamics status, but it does not erase the independently arithmetic host
or the unresolved transport test. `ROUTE_A_EXPLORATORY` means only “retain
for those bounded tests.” It does not mean that the current determinant is a
credible Riemann dynamical determinant. If the arithmetic-host relation were
reduced to direct target encoding, or if the candidate were retained solely
as a universal compiler, the consistent verdict would be
`ROUTE_A_REJECTED`, as for `SPECZ-TAUT-NORM-CIRCLES`.

## 4. The cross-object anti-splice boundary

The four rows cannot be combined coordinatewise:

| Credit | Sole typed owner in this audit | Why it cannot travel |
|---|---|---|
| analytic arithmetic origin | `DEN-WITT-Z-FIN` | no measure/algebra/trace/determinant transport to the proxy |
| analytic positive-time repetition ledger | return-distribution record | it is a componentwise Radon distribution, not the K0 trace-log owner |
| principal trace-log analytic determinant | `K0-M1` | it uses a selected zero mode and modeled unit masses, not source packets or Branch-F smearings |
| source `E_f` intertwiner | `DEN-WITT-Z-FIN` to a separate adelic target | target is not `Y_p`; transverse labels collapse and analytic data do not travel |

In particular, the tempting coordinatewise maximum

```text
source A0/A1 + return A1 + K0 A2
```

is not a candidate and is not a Route-A certificate. Shared notation, clocks,
or a parent algebra does not satisfy the same-object condition.

## 5. Adversarial gate and Route-B status

The strongest counter-argument survives every positive theorem: the only
exact determinant is a normalized zero-mode ledger compiler that ignores the
actual transverse geometry and works for arbitrary clocks. Conversely, the
geometry-bearing source supplies no measured analytic owner. The four YAMLs
therefore record `STOP_SCOPED` wherever a result would otherwise be promoted
beyond its typed object.

Route B is not invoked because no record reaches `A4_ROUTE_B_READY`, and no
single object supplies the arithmetic origin, orbit layer, global analytic
determinant, natural Hilbert-space lift, operator domain, self-adjointness,
spectral type, exact trace formula, and completed-divisor identity. No
Route-B YAML has been created.
