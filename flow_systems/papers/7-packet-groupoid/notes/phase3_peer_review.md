# Paper 7 Phase-3 independent mathematical and reproducibility peer review

Review date: **2026-08-14**  
Decision: **MAJOR REVISION — no Critical counterexample found, but the current
proof/release package is not yet manuscript-ready**  
Scope: active proof, source/operator audits, protocol/candidate locks, and the
deterministic controls; no manuscript or Route-YAML judgment  
Reviewer position: the reviewer implemented the deterministic controls but did
not author `proof_audit.md`; numerical controls are therefore treated as
potentially self-confirming and are never used to close a proof obligation

## 1. Executive assessment

The component Fourier/Poisson calculation, the global trace-norm asymptotic,
the positive-time Radon ledger, the corrected zero-mode summability theorem,
the reciprocal-prime argument, the target-conditioned coefficient uniqueness,
and the source-ownership negative certificate all survive adversarial checking.
No sign error was found in

```text
-Z_m'(s)/Z_m(s)
  = sum_p sum_(r>=1) m_p (log p) p^(-rs).
```

The proof package nevertheless overstates its present closure.  Three
operator-theoretic dependencies are asserted rather than completed: the
concrete faithful-normal-semifinite trace lemma, holomorphy in the **relative
Banach-algebra norm** required by the cited determinant framework, and
infinite-dimensionality of the actual frozen `L2(B_p,mu_p)`.  In addition, the
P7-4 theorem proved in `proof_audit.md` is not the theorem still printed in the
active protocol, so the protocol requires its own versioned amendment and a new
independent hash lock.

The strongest counter-argument to any positive promotion is already visible in
the project's own controls: the exact scalar is a probability-base-blind,
arbitrary-clock compiler built in a selected proxy, and unit masses are forced
only after one conditions on the desired logarithmic derivative.  Consequently
the exact right-half-plane product does not answer the primary ownership
question affirmatively.  The source audit instead supports a scoped negative
result: no audited theorem transports measure, algebra, trace, zero mode, or
determinant from `DEN-WITT-Z-FIN` to the proxy.

## 2. Active-input and hash audit

The following bytes were independently re-hashed for this review.

| Record | Observed SHA-256 | Review use |
|---|---|---|
| `notes/proof_audit.md` | `c51ca746a638fa624ee93f8160b0f7ffef9735c2c46cc22cb1f023026869d034` | active Phase-3 proof |
| `notes/research_protocol.md` | `0029ea437f9318ff4962830ed4d197cdad0d355968364a52bbeefc63a9db96c4` | active protocol input |
| `notes/candidate_lock.md` | `0a5712af3f1e9ad83db5191f588e43631510b066e2128cdf77b6b94802da62fa` | active candidate input |
| `notes/source_audit.md` | `a6a0e75aa2a5f38e8c60a5ce34ffb536438f93828501e282a2d0ecb530847d53` | P7-9 ownership input |
| `notes/operator_source_audit.md` | `69a76991c94cab24652c8d7d9f71c47a8eba70fcd7d1d4148689d47ff56e8b04` | determinant/domain source input |
| `notes/composition_blueprint.md` | `8071cb4d710ddd25ffae975fbd898c2373bb7f298989d170bb12ad141404ee44` | lock-drift record only |
| `code/packet_trace_controls.py` | `5374eb4c16c6789a71da69eae2495befd20b9646242d63d57320a3245ae58405` | deterministic controls |
| `code/test_packet_trace_controls.py` | `a2ab0da2f55f332538ce7b6d913feee63f654ab9db3063e58c77675325e42ac4` | regression tests |
| `results/packet_trace_manifest.json` | `5788a29b9bdd20c8c1748112e5a9c7a906644f51c2a1598ef6741aae7fbddd95` | artifact manifest |

The old protocol/candidate hashes
`5a0c77b637e8e744356f8a65726c04789837f7588ded710e6eb28090c2655d49`
and
`6b70f75917f929918cb2eade1734ce90feb32167b5bfae624290cefd49f915ef`
are correctly typed in `composition_blueprint.md` as **historical Phase-1
mechanical locks**, not current inputs.  `proof_audit.md`, `source_audit.md`,
and `operator_source_audit.md` consistently use the active `0029.../0a57...`
pair.  Thus there is no accidental stale-hash substitution inside those three
audits.  There is, however, no valid inheritance of the old independent PASS:
the current active pair must be amended and independently re-locked as stated
in Major findings M1 and M5.

## 3. Target-by-target verdict

| Target | Peer-review verdict | Basis and exact boundary |
|---|---|---|
| **P7-1** | **MATHEMATICS PASS; formal release conditional on M2** | The Fourier eigenvalue, absolute trace-class lattice sum, measure-one base factor, and Poisson scaling are correct.  Calling the resulting weight a faithful normal semifinite trace still depends on the missing concrete trace lemma. |
| **P7-2** | **PASS** | For `g=|fhat|`, the whole-line Riemann sum has mesh `2pi/L`; nonzero `f` gives a positive limit constant, yielding eventual two-sided comparison with `log p` and therefore the stated weighted-series iff.  The Gaussian CSV is only a convention witness. |
| **P7-3** | **PASS** | Compact positive-time support bounds both `p` and `r`, so the positive atomic ledger is locally finite.  The distinction from `tau_m(C_f)` outside global `L1` is correctly enforced; zero time is separately exposed. |
| **P7-4** | **PASS FOR THE CORRECTED THEOREM; active protocol FAILS TO MATCH** | In the bounded product, membership requires `Re(s)>=0` **and** the weighted Dirichlet sum.  The sum alone is the affiliated-operator `L1` criterion.  Unit masses give exactly `Re(s)>1`.  M1 is mandatory. |
| **P7-5** | **MAJOR REVISION** | The scalar trace-log identities and determinant taxonomy are substantively correct, but relative-norm holomorphy is not proved in the norm required by the cited Banach-algebra pair, and the ordinary-Hilbert exclusion assumes the unproved actual-`B_p` dimension claim.  See M3--M4. |
| **P7-6** | **MAJOR REVISION** | The central-scalar mass classification, positivity, copying, and the disclaimer that this is not all traces are correct.  The claimed faithful-normal-semifinite trace foundation is not concretely proved.  See M2. |
| **P7-7** | **PASS** | Dirichlet-series uniqueness is correctly applied at the primitive indices `n=p`; the sign of `-Z'/Z` is correct and the argument is explicitly target-conditioned rather than provenance-producing. |
| **P7-8** | **PASS, MATHEMATICAL PART; controls are finite witnesses only** | Constant fibers depend only on total probability.  Local finiteness of clocks suffices for Branch F, while Branch K separately requires weighted exponential convergence, boundedness, and `||K_s||<1`.  The actual ordinary-Hilbert control remains conditional on M4. |
| **P7-9** | **PASS AS A SCOPED NEGATIVE OWNERSHIP CERTIFICATE** | The source audit closes every T0--T7 field without importing proxy results.  Morishita's `E_f`-restricted map receives only continuity/time-reversal/packetwise-onto credit and collapses every transverse circle to the same `C_p`; no analytic transport follows. |

The aggregate decision is not obtained by averaging this table.  M2 and M3 are
shared foundations for several rows, while P7-9 is a negative source verdict,
not a promotion.

## 4. Findings by severity

### Critical

**None.**  No single false assertion was found that destroys the corrected
proxy theorem beyond repair.  The defects below block manuscript release but
have precise, claim-preserving repairs.

### Major M1 — the bounded/affiliated correction is absent from the active protocol

**Problem.**  The protocol states only
`K_s in L1(M,tau_m) iff sum_p m_p exp(-sigma L_p)<infinity`, while its
determinant branch uses the bounded algebra/relative trace ideal.  The proof
correctly discovers that these are two different statements.  The same frozen
protocol and candidate lock also use the unqualified name `Det_tau`, after the
operator audit restricted the permitted complex name to a branch-fixed
principal trace-log determinant.

**Evidence Anchor:** equation: `research_protocol.md` lines 236--255 versus `proof_audit.md` equations (6.2), (7.3)--(7.4)  
**Why it matters.**  For sufficiently decaying masses and `Re(s)<0`, the sum can
converge while `K_s` is an unbounded affiliated operator.  It is then outside
the bounded relative determinant domain.  Leaving the protocol unchanged
makes the proof look like it proved the preregistered theorem verbatim when it
actually proved a necessary correction.

**Required fix.**  Append and version a protocol amendment, as required by
protocol lines 387--388, with three separate statements:

```text
K_s in affiliated L1(M,tau_m)
  iff sum_p m_p p^(-Re(s)) < infinity;

K_s in L1_tau(M) := {x in M: tau_m(|x|)<infinity}
  iff Re(s)>=0 and sum_p m_p p^(-Re(s)) < infinity;

D_tau^pr(s)=exp(tau_m(Log_0(I-K_s)))
  only on the open subdomain where the sum converges and ||K_s||<1.
```

Update the candidate record to use `D_tau^pr` / “principal trace-log
determinant,” retain `Z_m=(D_tau^pr)^(-1)`, and state that the unit-mass
half-plane `Re(s)>1` is unchanged.

**Severity:** Major  
**Confidence:** 5/5 — direct bounded-versus-affiliated domain check

### Major M2 — the concrete `tau_p` and global `tau_m` FNS proof is incomplete

**Problem.**  Section 2 explicitly says its block-domain lemma is separate from
existence, normality, and semifiniteness.  Section 8 later assumes local
faithfulness/normality/semifiniteness and says that selecting one nonzero
central component proves global semifiniteness.  That does not exhibit the
finite-weight approximants required for an arbitrary positive element, and it
does not discharge `operator_source_audit.md` residual obligation 1.

**Evidence Anchor:** absence: `proof_audit.md` Sections 2 and 8 — expected concrete local `tau_p` FNS proof and a global finite-weight approximation net; checked lines 94--119 and 527--536  
**Why it matters.**  `tau_m` being a normal semifinite trace is the foundation
for the `L1` terminology used in P7-1--P7-6.  The source audit authorizes the
framework only **after** concrete fiber verification.

**Required fix.**  Add a lemma that:

1. derives traciality, faithfulness, and normality of
   `tau_p(A)=integral Tr(A(b))dmu_p(b)` from the ordinary fiber trace and the
   direct-integral theorem;
2. lets `Q_N` project onto circle modes `|n|<=N` and, for `A_p>=0`, uses
   `A_p^(1/2)(1 tensor Q_N)A_p^(1/2) <= A_p` as finite-trace approximants;
3. for the global product, combines those cutdowns with finite prime sets
   `F`, proves the directed net increases strongly to `A`, and invokes
   normality to obtain the full semifinite supremum property; and
4. proves normality for increasing **nets**, not only sequences, by finite
   prime partial sums followed by the countable supremum.

The existing mass recovery and copy-additivity arguments may then remain.

**Severity:** Major  
**Confidence:** 5/5 — direct audit of the positive-cone trace proof

### Major M3 — `H_m` holomorphy is shown in trace norm, not the relative Banach norm

**Problem.**  The proof establishes local uniform convergence in
`tau_m(|.|)` norm.  The cited relative determinant framework instead uses the
bounded ideal with norm `||x|| + tau_m(|x|)`.  The bounded ideal is not complete
under the `L1` norm alone, so the sentence “holomorphic as an
`L1_tau(M)`-valued map” does not by itself verify the relative Banach-algebra
hypothesis.

**Evidence Anchor:** equation: `proof_audit.md` lines 397--427 and `operator_source_audit.md` lines 81--88, 143--152  
**Why it matters.**  P7-5 calls the scalar a local lift in the relative
de la Harpe--Skandalis setting.  That terminology needs a path and logarithm in
the actual relative Banach-algebra pair, not merely convergence in the
affiliated `L1` completion.

**Required fix.**  On a compact set with `Re(s)>=a>0`, add the operator-tail
estimate

```text
sup_(p>P) (log p)^k p^(-a) -> 0
```

for every derivative, and combine it with the existing weighted `L1` bound.
For the logarithm add both

```text
sum_(r>=1) ||K_s^r||/r < infinity,
sum_(r>=1) ||K_s^r||_(1,tau_m)/r < infinity
```

locally uniformly.  Then state holomorphy and logarithm convergence in
`||.||+||.||_1`; the scalar trace-log calculation itself does not otherwise
change.

**Severity:** Major  
**Confidence:** 5/5 — direct norm comparison against the audited theorem domain

### Major M4 — infinite ordinary Hilbert multiplicity of the actual `B_p` is asserted, not proved

**Problem.**  The proof says the frozen packet base has
`dim L2(B_p,mu_p)=infinity`, then uses this to rule out the ordinary Fredholm
determinant.  Neither the proof nor the controls prove that fact for the actual
quotient `B_p`; the CSV only contains generic finite atomic and symbolic
nonatomic comparison bases.

**Evidence Anchor:** absence: `proof_audit.md` determinant taxonomy and P7-8 control — expected a proof that the frozen quotient `B_p` is infinite and has infinite-dimensional Haar `L2`; checked lines 504--515, 638--671  
**Why it matters.**  Without this lemma, the intended-representation statement
“every nonzero block fails ordinary Hilbert trace class” is unsupported, even
though the semifinite determinant calculation remains valid.

**Required fix.**  Insert a self-contained group lemma.  One available route is
to place the coordinatewise sign subgroup

```text
E = product_(ell odd, ell != p) {+1,-1}
    subset Zhat_(p)^x.
```

The subgroup `p^Zhat` is procyclic and has at most two elements of exponent
dividing two, whereas `E` is infinite (indeed uncountable).  Hence the image of
`E` in `B_p=Zhat_(p)^x/p^Zhat` is infinite.  An infinite compact group has
nonatomic Haar probability; equivalently, its Haar `L2` admits arbitrarily
large finite orthogonal families.  Therefore `L2(B_p,mu_p)` is
infinite-dimensional and `I tensor P_0` has infinite ordinary rank.  The proof
should check the notation against the exact quotient definition before using
this route.

**Severity:** Major  
**Confidence:** 4/5 — operator consequence is certain; the proposed group proof must be written against the source's exact notation

### Major M5 — the active hashes have not received an inheritable independent re-lock

**Problem.**  The `5a.../6b...` PASS belongs to historical bytes.  The active
`0029.../0a57...` files are consistently identified, but
`composition_blueprint.md` correctly records that the prior PASS cannot be
inherited.  This review cannot re-lock them because M1 requires a substantive
amendment, which will create new hashes.

**Evidence Anchor:** dataset: `composition_blueprint.md` Section 1.1 hash table and lines 23--33  
**Why it matters.**  Treating a content inspection or a downstream source audit
as a byte-level Phase-1 re-lock would erase the provenance of the domain
correction.

**Required fix.**  After M1--M4 are repaired, record the superseding
protocol/candidate/proof hashes, provide an explicit old-to-new amendment
crosswalk, and obtain an independent lock verdict on those exact bytes.  Update
the blueprint and every downstream hash reference.  Keep `5a.../6b...` labeled
historical rather than deleting or silently repointing them.

**Severity:** Major  
**Confidence:** 5/5 — direct hash and authority-chain audit

### Minor m1 — control names conceal that the computed quantity is `log Z`, not `tau Log(I-K)`

**Problem.**  The function named `trace_log_exact` returns

```text
-sum_j m_j log(1-exp(-sigma L_j)) = log Z_m(sigma),
```

and `compiled_inverse_product` returns `Z_m`, while the proof's determinant-side
trace-log is

```text
tau(Log_0(I-K_s))
  = sum_j m_j log(1-exp(-sL_j)) = -log Z_m(s).
```

The numerics are correct, but the generic CSV fields `trace_log_exact` and
`zero_mode_trace_log_term` can be read as determinant-side quantities.

**Evidence Anchor:** equation: `packet_trace_controls.py` lines 160--199, 344--374, 409--455, and 487--505  
**Required fix.**  Rename the computed fields/functions to `log_Z_*` or
`inverse_determinant_log_*`, or add an explicit `quantity_owner` column.  The
clearest table would contain both
`tau_Log_D=-log_Z` and `log_Z`, both `D=exp(tau_Log_D)` and `Z=1/D`, and a test
of their reciprocal/sign relations.  Qualify the README and manifest phrase as
“inverse-determinant trace-log (`log Z`) versus inverse product.”

This issue does **not** require changing the sign in proof equation (9.1): that
sign is correct.

**Severity:** Minor  
**Confidence:** 5/5 — direct symbolic differentiation and code inspection

### Minor m2 — `verify-only` does not verify the implementation hashes stored in the manifest

**Problem.**  `verify()` checks CSV size, row count, and SHA-256, but ignores the
`implementation_files` mapping.  A changed implementation with old generated
tables could therefore pass `--verify-only`.  The full reproduction script is
stronger because it regenerates first, so current reproducibility is not
invalidated.

**Evidence Anchor:** absence: `packet_trace_controls.py` function `verify` — expected comparison of current implementation files with `manifest[implementation_files]`; checked lines 796--818  
**Required fix.**  Resolve each manifest implementation path against the Paper-7
directory, compare its current SHA-256, fail on missing/extra expected entries,
and add a temporary-copy tamper test for an implementation file.  Regenerate
the manifest after any code/README rename from m1.

**Severity:** Minor  
**Confidence:** 5/5 — direct verifier control-flow inspection

## 5. Requested hostile checks: explicit determinations

| Attack surface | Determination |
|---|---|
| **Bounded versus affiliated `L1`** | The proof's correction is mathematically necessary and correct.  It is not merely notation if determinant eligibility is claimed; protocol amendment M1 is mandatory. |
| **`tau_m` normality/semifiniteness** | The result is standard and strongly supported by OA-1/OA-2, but the concrete proof required by the operator audit is missing.  “Choose a nonzero component” is not an explicit approximation proof for arbitrary positive `A`. |
| **Riemann-sum iff** | Correct.  With `h=2pi/L`, `h sum_n g(nh)->integral g`; `g=|fhat|` is continuous and rapidly decreasing.  For nonzero `f`, Fourier injectivity gives a positive constant, hence eventual two-sided comparison and the weighted-series iff. |
| **Reciprocal-prime proof** | Correct and target-free.  The finite Euler product expands over integers whose prime divisors are at most `x`, dominates the harmonic partial sum, and `-log(1-1/p)<=2/p` contradicts bounded products if `sum_p1/p` converged. |
| **`H_m` holomorphy** | The abscissa and derivative domination are correct.  The missing step is convergence in the combined relative norm, not the scalar analysis; repair M3 closes it. |
| **Principal trace-log / FK / dHS / Breuer / ordinary taxonomy** | Correctly separated in substance: `D_tau^pr` is a local branch-fixed scalar; FK is positive and equals only its modulus for nonreal `s`; dHS is quotient-valued before choosing the local lift; invertibility gives Breuer--Fredholm index zero, not a determinant.  Ordinary Fredholm exclusion awaits M4. |
| **Actual `L2(B_p)` dimension** | Not established in the active proof.  Generic control bases cannot substitute for a lemma about the frozen quotient. |
| **Sign of `-Z'/Z`** | Correct in the proof.  Since `log Z=sum m_p sum_r p^(-rs)/r`, differentiating gives `Z'/Z=-sum m_p(log p)p^(-rs)`.  Only the code naming is ambiguous. |
| **Arbitrary-clock conditions** | Correctly separated: local finiteness of positive lengths proves only the positive-time ledger; Branch K additionally needs weighted exponential summability, boundedness, and a strict norm bound for the logarithm.  The convergence half-plane can be empty. |
| **Finite controls** | They are regression witnesses, not theorem evidence.  The Gaussian is Schwartz rather than `C_c^infinity`; clock tables have three finite ledgers; Hilbert rows are model bases; zero-time rows are finite positive partial sums and assign no regularized limit. |
| **Lock drift** | No current proof/source audit confuses old and active hashes.  Formal inheritance nevertheless fails, and the next valid lock must attach to post-amendment bytes. |

## 6. Reproducibility review

The following read-only checks were rerun with bytecode writing disabled:

```text
python3 -m unittest -v test_packet_trace_controls.py
python3 packet_trace_controls.py --output-dir ../results --verify-only
```

Results:

- **18/18 tests PASS**;
- manifest verification reports **9 artifacts, PASS**;
- the nine CSV files contain **407 data rows** in total;
- the unit suite itself generates two independent temporary output trees and
  compares every generated byte;
- no network, randomness, fit, external dataset, or Riemann-zero data is used;
- manifest SHA-256 is
  `5788a29b9bdd20c8c1748112e5a9c7a906644f51c2a1598ef6741aae7fbddd95`.

The numerical residuals are consistent with their intended finite roles:
Poisson convention error is at floating-point scale, the finite trace-log and
inverse-product agree at floating-point scale, and the Gaussian scaled Riemann
sum tends to its exact `2pi` value.  None of these residuals can establish the
general `C_c^infinity` theorem, an infinite prime sum, analytic continuation,
or source ownership.  The existing README and manifest interpretation boundary
mostly state this correctly; m1 is the remaining sign/owner naming repair.

## 7. P7-9 ownership and Morishita boundary

The P7-9 matrix in `source_audit.md` is internally consistent with the proof
and controls:

| Gate | Peer-review status |
|---|---|
| T0 object identity | **FAIL** for source-to-proxy transport; Morishita targets a third, adelic object. |
| T1 classical ledger | **PARTIAL**: packet, prime label, repetitions, and absolute clock are sourced; amplitude is not. |
| T2 trace definition | **NOT_TESTABLE** in the audited source. |
| T3 analytic ledger | **NOT_TESTABLE** in the audited source. |
| T4 theorem extent | **SCOPED ONLY**: the repaired map is continuous, time-reversing, and packetwise onto. |
| T5 coefficient provenance | **FAIL** for central masses and analytic weights. |
| T6 clock/normalization | **PARTIAL**: `p^Z` and `log p` survive; trace/Fourier/determinant normalization does not. |
| T7 arithmetic promotion | **PARTIAL; no determinant promotion**. |

The `E_f` repair has the right type.  Equation (35) supplies nonzero away-from-
`p` coordinates; rational scaling and an away-coordinate unit normalize the
image into `C_p`; flow anti-equivariance makes the circle image onto.  This is
a `DERIVABLE_NEW_LEMMA`, not a corrected theorem attributed back to Morishita,
and it transports no transverse labels.  The bounded-search statement “no such
analytic transport was found through 2026-08-14” is appropriate; a universal
nonexistence claim would not be.

Thus P7-9 closes negatively even if the proxy mathematics is repaired.  It
does not permit a coordinatewise maximum of source A0/A1 credit and proxy A2
credit, and it supplies no Route-B premise.

## 8. Mandatory repair order and release gate

The smallest safe revision sequence is:

1. append the M1 protocol amendment and update the candidate determinant name;
2. add the M2 concrete local/global FNS trace lemma;
3. strengthen P7-5 with the M3 combined-norm estimates;
4. prove the M4 actual-`B_p` infinite-dimensionality lemma;
5. repair the m1 `log Z`/determinant sign naming and the m2 implementation-hash
   verifier, then regenerate all CSVs and the manifest;
6. rerun tests and full byte-for-byte reproduction;
7. issue an updated proof-status table without silently calling the original
   protocol theorem proved verbatim; and
8. independently re-lock the exact new protocol, candidate, proof, source
   crosswalk, code, and manifest hashes.

No manuscript drafting or Route-YAML release should precede this sequence.
After these repairs, the likely mathematical disposition is P7-1--P7-8 PASS on
the proxy and P7-9 closed negatively for source ownership.  This review does
not itself award a Route verdict.

## 9. Final decision

```text
Critical findings: 0
Major findings:    5
Minor findings:    2
Decision:          MAJOR REVISION
Draft release:     BLOCKED pending M1--M5 and independent post-fix re-lock
Route verdict:     NOT ISSUED
```

The central proxy theorem appears repairable rather than refuted.  Its strongest
publishable conclusion remains deliberately two-sided: an exact, mathematically
valid trace-log compiler exists in the selected proxy, while the base/clock
controls and P7-9 certificate prevent that exactness from being mistaken for a
source-owned packet trace or determinant.
