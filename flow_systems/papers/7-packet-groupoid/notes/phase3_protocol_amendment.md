# Paper 7 Phase-3 protocol amendment and M1--M4 crosswalk

Amendment ID: **`P7-PH3-AMEND-2026-08-14-v1`**  
Date: 2026-08-14  
Status: **APPLIED TO THE AUTHORIAL RECORD; M5 INDEPENDENT EXACT-BYTE RE-LOCK
PENDING**  
Trigger: `phase3_peer_review.md`, SHA-256
`8d9a246334ce4538d238050ffe85753ed6740c59c5347067983447b2cb7aea22`

## 1. Authority, scope, and historical record

This versioned amendment resolves Major findings M1--M4 without claiming the
independent M5 verdict.  Its normative scope is limited to:

- the zero-mode domain and determinant name in `research_protocol.md`;
- the corresponding `K0-M1` record in `candidate_lock.md`; and
- the FNS, relative-norm, and actual-base proofs in `proof_audit.md`.

It does not modify or adjudicate P7-9, source ownership, the T0--T7
same-object certificate, the composition blueprint, deterministic controls,
source files, or any manuscript.  In particular, no proxy-owned analytic
object is transferred to `DEN-WITT-Z-FIN`.

The exact pre-amendment records remain historically operative for their own
bytes:

| Record | Historical SHA-256 | Historical status |
|---|---|---|
| `research_protocol.md` | `0029ea437f9318ff4962830ed4d197cdad0d355968364a52bbeefc63a9db96c4` | Phase-1 frozen independent re-audit PASS |
| `candidate_lock.md` | `0a5712af3f1e9ad83db5191f588e43631510b066e2128cdf77b6b94802da62fa` | Phase-1 frozen independent re-audit PASS |
| `proof_audit.md` | `c51ca746a638fa624ee93f8160b0f7ffef9735c2c46cc22cb1f023026869d034` | pre-peer-review Phase-3 proof |

Those verdicts are not inherited by the amended bytes.  M5 requires a new
independent review on the superseding hashes in Section 4.

## 2. Normative M1 theorem amendment

The historical protocol target was

```text
K_s in L1(M,tau_m)
  iff sum_p m_p p^(-Re(s)) < infinity.
```

It is retained in the protocol as a visibly superseded target.  The corrected
theorem has two different domains:

```text
K_s in affiliated L^1(M,tau_m)
  iff sum_p m_p p^(-Re(s)) < infinity;

K_s in L^1_tau(M) := {X in M : tau_m(|X|)<infinity}
  iff Re(s)>=0 and sum_p m_p p^(-Re(s)) < infinity.
```

The branch-fixed complex scalar is now named only as

```text
D_tau^pr(s) = exp(tau_m(Log_0(I-K_s))),
Log_0(I-K_s) = -sum_(r>=1)K_s^r/r.
```

It is defined only on the open half-plane

```text
H_m={s:Re(s)>max(0,sigma_c(m))},
```

where the weighted sum converges and `||K_s||<1`.  No boundary definition is
asserted.  `D_tau^pr` means the principal trace-log scalar lift fixed at the
identity, not an unqualified complex semifinite determinant.  The conditional
unit-mass result remains exactly

```text
Re(s)>1.
```

Thus the amendment records a theorem correction but does not alter the
unit-mass half-plane.

## 3. Reviewer-finding crosswalk

| Finding | Severity | Required commitment | Applied change and evidence locator | Closure status |
|---|---|---|---|---|
| M1 | Major | Split affiliated and bounded `L1`; restrict the principal trace-log scalar to an open summability/`||K||<1` domain; use a precise candidate name; preserve the deviation. | `research_protocol.md`, status ledger, Sub-question 2, decomposable trace-domain definitions, Branch K, and P7-4--P7-5 targets; `candidate_lock.md`, `DEN-WITT-PACKET-DECOMP-K0-M1`; `proof_audit.md`, Sections 1, 6, and 7.1. | **CLOSED in authorial revision; M5 re-lock pending** |
| M2 | Major | Prove the concrete local and global faithful-normal-semifinite trace, including increasing nets and finite-weight approximants. | `proof_audit.md`, Section 2.1: direct-integral trace; `A_p^(1/2)(1 tensor Q_N)A_p^(1/2)` order calculation; finite-prime/finite-mode directed net; arbitrary-net normality identity (2.6); Section 8 points back to this proof. | **CLOSED mathematically** |
| M3 | Major | Prove `H_m` holomorphy and logarithm convergence in `||.||+||.||_1`, not trace norm alone. | `proof_audit.md`, Section 7.1: derivative trace bound (7.3), operator tail (7.4), double-norm power estimates (7.5)--(7.6), and locally uniform derivative estimate (7.7). | **CLOSED mathematically** |
| M4 | Major | Prove the actual frozen `B_p` is infinite and its Haar `L2` is infinite-dimensional before excluding the ordinary Fredholm determinant. | `proof_audit.md`, Sections 7.3--7.4: Paper-2-safe sign/procyclic quotient argument; singleton mass (7.13); arbitrarily large finite orthogonal families (7.14); ordinary-rank consequence.  No blanket nonatomicity claim is used. | **CLOSED mathematically** |
| M5 | Major | Independently inspect and lock the exact amended bytes, then update downstream references. | Not performed by this authorial amendment.  The superseding hashes are listed below for the independent reviewer. | **OPEN — MUST NOT BE SELF-CERTIFIED** |

## 4. Superseding exact-byte records for M5

| Record | Superseding SHA-256 | Role |
|---|---|---|
| `research_protocol.md` | `2f8dc9a802cfcf8b578db24419909de710563ece62cf026e9848fac437ba1581` | amended normative protocol |
| `candidate_lock.md` | `73314bb031f663e8532a922821e66b20f31bd6f20b06a801a25147d6e55a17a0` | amended candidate terminology/domain |
| `proof_audit.md` | `febcd43e5d23daf893816b815c81f19ee4da5bac42a554d553262784660f00b5` | amended M2--M4 mathematical proof |
| `operator_source_audit.md` | `69a76991c94cab24652c8d7d9f71c47a8eba70fcd7d1d4148689d47ff56e8b04` | unchanged source/domain authority |

The SHA-256 of this crosswalk is intentionally not embedded in itself; it must
be computed after the final byte and supplied alongside the table above to the
independent M5 reviewer.

## 5. Remaining boundary after M1--M4

No mathematical M1--M4 item is knowingly left open.  This is not a release or
same-object promotion: M5 remains mandatory, and P7-9 retains its independently
audited negative ownership boundary.  Unit masses remain
`MODELING_CHOICE`; target-conditioned coefficient uniqueness still cannot
supply mass provenance.
