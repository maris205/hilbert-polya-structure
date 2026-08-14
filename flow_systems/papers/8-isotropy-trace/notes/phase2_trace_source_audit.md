# Paper 8 Phase-2 primary trace/nonnormality source audit

Audit date: 2026-08-14  
Verdict: **PASS — adequate source chain, with the regular-completion and
finite-corner gates still open**  
Phase boundary: source retrieval, hypothesis matching, normalization ownership,
and proof-obligation classification only.  This audit proves no P8 theorem,
edits no Phase-1 lock, and supplies no manuscript prose.

## 1. Executive verdict

There is no hard source obstruction to the one-orbit trace experiment.
Authoritative full texts support all of the following ingredients:

1. an invariant measure on a compact `R^d`-space induces the
   identity-coefficient l.s.c. semifinite trace on the continuous crossed
   product and a trace on its von Neumann closure;
2. the Plancherel weight is faithful, semifinite, and sigma-weakly l.s.c., and
   dual Haar is uniquely normalized by Fourier `L2`-isometry;
3. l.s.c. traces are functorial under *-homomorphisms, and strong Morita
   equivalence induces l.s.c. traces while preserving faithfulness, dense
   definition, and semifiniteness;
4. `vN(Z)` is `L-infinity(T,Haar)`, its normal group trace is Haar integration,
   and normal states are precisely the ultraweakly continuous states; and
5. the locked Fourier sign convention, rapid decay of the transform of a
   smooth compactly supported function, and Poisson summation are sourced.

Those sources do **not** prove the locked theorem targets by themselves.  The
following four assertions remain conditional/new and must not be cited as
literature facts:

- the fixed regular representation has closure
  `M_reg ~= L-infinity(T,dtheta/(2pi)) bar-tensor B(L2(R/LZ))`;
- the locked convolution/character convention gives the `+theta` frequency
  and `exp(-ir theta)` return sign;
- `Tr o pi_theta` is densely defined/semifinite on the precise locked
  pullback domain; and
- its trivial-character member has no normal extension along the fixed
  `C* -> C*_r -> M_reg` map.

The most important domain correction is this:

> For the one-orbit algebra `A_L ~= C(T) tensor K(H)` with infinite-dimensional
> `H`, `Z(A_L)=0`.  `C(T)` is naturally the **multiplier centre** or a chosen
> rank-one corner, not a nonzero central subalgebra of `A_L`.  Moreover
> `delta_theta tensor Tr` is infinite on `f tensor 1` whenever
> `f(theta)>0`; it does not restrict to a finite point evaluation on the
> multiplier centre.  The point-evaluation obstruction must therefore be run
> in a trace-finite rank-one corner.

This is an exact-owner gate, not a negative verdict.  It makes P8-6 provable in
the intended model without conflating a semifinite weight with a bounded state.

### Mandatory Phase-2 amendment before Phase 3

Status: **MANDATORY**.  Before any Phase-3 proof attempt, amend the P8-6
preregistration language so that the point-evaluation obstruction is stated on
a trace-finite rank-one corner, not as the restriction of
`delta_theta tensor Tr` to a continuous central subalgebra.  Concretely, with
`p=1 tensor e` for a rank-one projection `e`, use
`p A_L p ~= C(T)` and
`(delta_theta tensor Tr)(p(f tensor 1)p)=f(theta)`.  The multiplier-centre
observation may be retained separately, but it is not itself the bounded
point-evaluation witness.  This amendment changes neither the proposed trace
family nor the regular/character comparison; it corrects the exact domain of
the no-normal-extension gate.

## 2. Evidence classes used below

| Label | Meaning in this audit |
|---|---|
| `SOURCE_THEOREM` | The retained source states the claim under explicit hypotheses. |
| `SOURCE_SPECIALIZATION` | A source theorem applies after a short, transparent specialization; Phase 3 must still write it with the locked conventions. |
| `CONDITIONAL_BRIDGE` | A source theorem becomes applicable only after another Paper-8 topology/representation gate closes. |
| `NEW_ELEMENTARY_LEMMA` | No retained source is being credited for the exact statement; Paper 8 must prove it. |
| `UNSOURCED/DO_NOT_CLAIM` | The present corpus does not license the assertion. |

All physical-page locators below are licensed by same-stem `PASS` ARS
preflights.  The exact bibliography, endpoints, hashes, and locator details are
in `sources/trace_source_manifest.md`.

## 3. Invariant-measure/FNS trace: exact hypotheses and owner

### 3.1 Direct sourced result

`TR-BR18`, Lemma 7.4 (physical p. 36), treats a compact configuration space
`Omega`, a continuous `R^d` action, and an invariant full-support probability
`P`.  On the continuous crossed product it defines, on the stated positive
core,

```text
T(f) = integral_Omega f(0;omega) dP(omega).
```

The source states that this is faithful, semifinite, and norm-l.s.c., contains
its dense test algebra in the domain, and extends to the displayed von Neumann
closure.  Proposition 3.2 (physical pp. 8--9) gives the underlying module-trace
construction, and the paper's Appendix uses a faithful normal semifinite trace
on the generated von Neumann algebra.

This provides `SOURCE_THEOREM` coverage for the continuous crossed-product
trace template.  Its exact hypotheses must be carried into Paper 8:

- the unit space is compact Hausdorff and the action is continuous;
- the unit measure is invariant;
- the acting group is `R^d`, hence unimodular;
- full support is required for faithfulness on the represented coefficient
  algebra; and
- the von Neumann algebra is the closure in the representation generated by
  that trace construction.

For a finite invariant measure of total mass `c`, scalar rescaling gives
`T(f)=integral f(0;omega)dmu(omega)` and total coefficient `c f(0)`.  Thus, if
the Paper-8 section-free lift from `nu_p in Prob(Q_p)` is proved to be the
length-scale invariant measure of mass `L_p`, the time-only target is

```text
T_reg(a_f) = L_p f(0).
```

The scalar rescaling is a `SOURCE_SPECIALIZATION`; the existence and
regularity of the packet measure are not supplied by `TR-BR18`.

### 3.2 What still has to match

The following are `CONDITIONAL_BRIDGE` obligations:

1. identify the locked transformation-groupoid algebra, with its frozen
   convolution convention, with the crossed product to which `TR-BR18`
   applies;
2. show that `M_(p,nu)^reg` is the same represented closure as the sourced
   trace construction, not merely an abstract isomorphic von Neumann algebra;
3. state what happens when `nu_p` lacks full support: the trace may descend to
   a faithful trace on its support representation but is not faithful on an
   unreduced coefficient algebra; and
4. prove that a general complex time kernel `a_f` belongs to the **linear
   `L1`/trace ideal**, not merely to `C_c(G)`.  A trace is initially an
   extended-positive map; writing `T(a_f)` requires this domain statement.

Calling the result an FNS trace is safe only after the represented von Neumann
algebra, positive cone, normality, faithfulness relative to support, and
semifiniteness are all named.

### 3.3 Plancherel normalization

`TR-REN21`, physical pp. 3--4, states that the canonical left-Hilbert-algebra
weight is faithful, semifinite, and sigma-weakly l.s.c. and identifies the
group case as the Plancherel weight.  It also fixes the dual Haar measure as
the unique Haar measure making Fourier transform an `L2` isometry.

For `H=L Z` with counting Haar, this convention selects

```text
hat H ~= T,             d hat h = dtheta/(2pi).
```

This is not an arbitrary probability choice.  It is the dual of the frozen
counting Haar.  It does not, however, select a packet transverse measure or a
cross-prime mass.

The sibling groupoid audit retains Williams's quotient integral formula
(4.63), printed p. 138.  With Lebesgue Haar on `R`, counting Haar on `L Z`, and
unimodularity, its specialization is

```text
integral_R g(t)dt
  = integral_(R/LZ) sum_(r in Z) g(u+rL) du,
```

where `du` is quotient **length Haar** of total mass `L`.  Writing
`dubar=du/L` gives the probability-scale version.  The source template is
sourced; the exact locked specialization is a `SOURCE_SPECIALIZATION` to be
shown in Phase 3.

## 4. The character-fibre l.s.c. trace and its true domain

### 4.1 C*-level source chain

The independent groupoid audit sources, on one transitive orbit only,

```text
A_L = C*((R/LZ) rtimes R) ~= C*(LZ) tensor K(H)
    ~= C(T) tensor K(H),       H=L2(R/LZ,du).
```

The concrete isomorphism is noncanonical and does not yet identify the locked
regular von Neumann representation.  Conditional on this one-orbit bridge,
the character trace is the expected extended-positive map

```text
tau_theta(a) = Tr(a(theta)),
Dom(tau_theta)_+ = {a in A_L,+ : Tr(a(theta)) < infinity}.
```

There are two rigorous source routes to its l.s.c. status:

- `TR-CZ83`, Proposition 2.2 (physical pp. 7--8), induces l.s.c. traces across
  the Green/Morita equivalence and preserves dense definition and
  semifiniteness; or
- once the exact representation `pi_theta:A_L->K(H)` is proved,
  `TR-ERS11`, Theorem 3.11 (physical p. 12), makes
  `Tr o pi_theta` the functorial pullback of the ordinary l.s.c. trace on
  `K(H)`.

Neither route licenses an algebra isomorphism or normal extension.  The second
route also does not supply dense definition automatically.

### 4.2 Semifiniteness gate

Paper 8 must separately prove all of the following:

- `pi_theta(A_L)` is contained in `K(H)` (and record whether it is onto);
- `pi_theta` factors through the reduced algebra along the locked diagram;
- the finite-positive domain is norm dense; and
- the trace identity holds on the extended-positive pullback domain.

The intended `NEW_ELEMENTARY_LEMMA` uses compactness of every positive image:
for `a>=0`, the spectral cutoff `(pi_theta(a)-epsilon)_+` has finite rank, and
functional calculus identifies it with `pi_theta((a-epsilon)_+)`.  That is a
proof route, not a result credited by this source audit.  If the compact-image
gate fails, no semifiniteness conclusion survives.

The character trace is generally nonfaithful on `A_L`: its kernel contains the
ideal of fields vanishing at `theta`.  This is expected and must not be hidden
by the word “semifinite.”

### 4.3 Trace-class time-smearing

`HA-LAU17`, Definition 14.1 (physical p. 79), fixes
`fhat(xi)=integral f(t)e^{-itxi}dt`; Theorems 14.10--14.11 (physical
pp. 84--85) give the decay needed to infer rapid decay for
`f in C_c^infinity(R)`.  Once the induced representation has actually been
diagonalized with frequencies `(2pi n +/- theta)/L`, rapid decay makes the
diagonal eigenvalue sequence absolutely summable.  Ordinary trace class is
defined in `OP-JON09`, physical p. 50.

Thus the analytic estimate is well sourced, but

```text
pi_theta(a_f) is trace class
```

is a `NEW_ELEMENTARY_LEMMA` conditional on the representation/sign derivation.
It cannot be inferred merely from `a_f in C_c(G)` or from Morita equivalence.

## 5. Trace disintegration/classification: what is and is not available

For the one-orbit algebra, `TR-CZ83` gives a bijection between the relevant
l.s.c. trace cones of `C(T)` and `C(T) tensor K`.  Combining this with the
ordinary Riesz representation theorem on `C(T)` yields the expected
measure-labelled family, schematically

```text
tau_mu(a) = integral_T Tr(a(theta)) dmu(theta).
```

This receives only `CONDITIONAL_BRIDGE` status here because Phase 3 must:

- fix the actual imprimitivity module or concrete trivialization;
- state the trace class being classified (all l.s.c., densely defined,
  semifinite, faithful, finite, or normalized);
- verify the extended integral and its domain; and
- avoid calling the resulting parametrization canonical when the
  C*-isomorphism is choice-dependent.

The useful conceptual consequences are nevertheless clear:

- dual Haar corresponds to the regular/Plancherel member;
- `delta_theta` corresponds to a character-fibre member;
- algebraic distinction of `theta=0` does not choose a transverse packet
  measure; and
- none of this classifies traces on the full packet unless the field/twist
  over `Q_p` is first proved.

No retained source supports a packet formula
`C(Q_p) tensor C(T) tensor K`, exhaustion of packet invariant measures, or a
canonical global trace.  Those remain `UNSOURCED/DO_NOT_CLAIM` at this stage.

## 6. Point evaluation and no normal extension: corrected fixed-map lemma

### 6.1 Sourced background

`OP-JON09`, physical p. 15, identifies `vN(Z)` with
`L-infinity(T,dtheta/(2pi))`; physical p. 16 identifies the canonical normal
group trace with Haar integration.  Definition 7.1.2 and Theorem 7.1.3,
physical pp. 43--44, state the exact normality criterion: for a state on a von
Neumann algebra, normality is equivalent to ultraweak continuity and complete
additivity.

These facts are `SOURCE_THEOREM`.  The statement

```text
delta_theta:C(T)->C has no normal positive extension to
L-infinity(T,Haar)
```

is not quoted from Jones; it is a `NEW_ELEMENTARY_LEMMA`.  A suitable Phase-3
witness is a decreasing family of continuous peaks equal to one at `theta`
whose infimum in `L-infinity(T,Haar)` is zero.  The audit records the proof
route but gives no theorem credit.

### 6.2 The centre/corner distinction

Let `H` be infinite dimensional and `A=C(T) tensor K(H)`.  Then

```text
Z(A)=0,
ZM(A)=C(T) tensor 1,
```

while a rank-one projection `e in K(H)` gives

```text
p=1 tensor e in A,       pAp ~= C(T).
```

For the character weight `tau_theta=delta_theta tensor Tr`,

```text
tau_theta(p(f tensor 1)p)=f(theta),
```

but its multiplier-centre value is infinite for positive `f` with
`f(theta)>0`.  Therefore the bounded point evaluation belongs to the finite
corner, not to the multiplier-centre restriction of the full semifinite
weight.

The correctly typed P8-6 proof target is consequently:

1. prove the fixed regular closure and map
   `A -> M_reg ~= L-infinity(T,Haar) bar-tensor B(H)`;
2. choose or intrinsically identify a projection `p in A` with
   `tau_theta(p)=1` whose regular compression is the expected
   `L-infinity(T,Haar)` corner;
3. assume a normal extension of the **same** extended-positive trace along
   that fixed map;
4. compress by `p`, obtaining a normal finite positive functional on
   `pM_reg p`; and
5. use the new point-evaluation lemma for the contradiction.

This is a `NEW_ELEMENTARY_LEMMA` with a `CONDITIONAL_BRIDGE` premise.  Until
Step 1 is proved, abstract C*-isomorphism to `C(T) tensor K` does not prove
nonnormality in the locked `M_reg`.

The existence and nonuniqueness of singular state extensions from `C(T)` to
`L-infinity(T,Haar)` are separate claims.  They are not needed for the
no-normal-extension direction and receive no source credit in this audit.

## 7. Floquet/Poisson sign and normalization ledger

| Link | Evidence status | Exact downstream duty |
|---|---|---|
| `dt` on `R`, counting on `LZ`, quotient length `du` | Williams (4.63) plus specialization | Prove total mass `du(R/LZ)=L`; name probability `dubar=du/L` separately. |
| counting Haar on `LZ` -> dual `dtheta/(2pi)` | `TR-REN21`, Fourier-isometric dual Haar | Write the chosen Fourier transform on `LZ` and verify Parseval. |
| `fhat(xi)=integral f(t)e^{-itxi}dt` | `HA-LAU17`, Definition 14.1 | Use without changing sign. |
| decay and trace-class summability | `HA-LAU17`, pp. 84--85 | After diagonalization, prove the eigenvalue sequence is in `ell1`. |
| unshifted Poisson formula | `HA-LAU17`, Theorem 23.5, p. 137 | Scale from `2pi Z` to `LZ`. |
| shifted formula and phase | `NEW_ELEMENTARY_LEMMA` | Derive by modulation; do not quote the locked sign from the source. |
| character frequencies | groupoid audit + `NEW_ELEMENTARY_LEMMA` | Derive from the frozen arrow, convolution, representation, and `chi_theta(rL)=e^{irtheta}` conventions. |
| dual-Haar cancellation | `NEW_ELEMENTARY_LEMMA` | Justify sum/integral interchange on the trace domain and show only `r=0` remains. |

The preregistered target

```text
sum_n fhat((2pi n+theta)/L)
  = L sum_r f(rL) exp(-irtheta)
```

is consistent with modulation under the locked Fourier transform, but that
observation is not a substitute for the representation sign calculation.  If
the representation produces `-theta`, every phase-sensitive record must be
amended together; the Haar average and `theta=0` value are unchanged.

At the common length scale, the intended Phase-3 chain is

```text
(1/(2pi)) integral_0^(2pi) T_theta(f)dtheta = L f(0),
T_0(f) = L sum_r f(rL).
```

At probability scale **both** values are divided by `L`.  No retained source
licenses rescaling only one side.

## 8. P8 theorem-target source map

| Target | Source status after this audit |
|---|---|
| `P8-2` orbit imprimitivity/Floquet | C*-imprimitivity and induced-character labels are sourced by the sibling audit; the concrete frequency/sign computation remains new. |
| `P8-3` character-fibre Poisson trace | Fourier/decay/Poisson ingredients sourced; diagonalization, trace-class membership, scaling, and phase are new lemmas. |
| `P8-4` regular isotropy cancellation | invariant crossed-product trace and dual-Haar normalization sourced; fixed `M_reg` decomposition, `L1` domain, Weil specialization, and cancellation are new/conditional. |
| `P8-5` trivial-character l.s.c. trace | l.s.c. trace induction/pullback sourced; compact-image factorization, dense finite domain, and exact time value remain new. |
| `P8-6` singularity/no normal extension | `vN(Z)=L-infinity(T)` and normality criterion sourced; fixed completion, finite-corner compression, and no-normal-extension contradiction remain new. |
| `P8-7` packet measure/domain boundary | No trace source proves the packet quotient field, invariant-measure exhaustion, trace variation with `nu_p`, or global assembly. |
| `P8-8/P8-9` controls/ownership | Source corpus supplies definitions and limits only; controls, T0--T7, and Route evaluation remain Paper-8 work. |

## 9. Mandatory claim-language guards

Safe after the listed hypotheses are proved:

> An invariant finite unit measure on the compact continuous `R`-space gives
> the standard identity-time l.s.c. semifinite crossed-product trace.  On one
> transitive orbit, the C*-algebra is a continuous field of compacts over the
> isotropy dual.  Character evaluation induces l.s.c. C*-traces, while the
> dual-Haar member is the regular Plancherel trace.

Unsafe at Phase 2:

- “The Haar system itself is the invariant unit measure or trace.”
- “Bourne--Rennie proves the locked packet regular representation.”
- “Morita equivalence identifies the full and reduced algebras or preserves a
  preselected trace without an induction theorem.”
- “`C(T)` is the centre of `C(T) tensor K`.”
- “The character weight restricts to point evaluation on the multiplier
  centre.”
- “Point evaluation is a normal functional on `L-infinity(T,Haar)`.”
- “Full equals reduced, therefore the character fibre is normal.”
- “Agreement on time-only kernels makes the full packet traces equal.”
- “A one-orbit trace classification supplies a packet probability or
  cross-prime mass.”

## 10. Retained artifacts and reproducibility

The retained trace/harmonic corpus consists of six PDFs and six same-stem
preflight sidecars under `notes/sources/`.  All preflights are `PASS` with page
counts `62/62/62`, `17/17/17`, `33/33/33`, `6/6/6`, `127/127/127`, and
`176/176/176`, respectively.  The canonical artifact ledgers are:

- `sources/trace_source_manifest.md`; and
- `sources/trace_source_checksums.sha256`.

From `notes/sources/`, exact-byte verification is:

```bash
sha256sum -c trace_source_checksums.sha256
```

The search retained only sources that changed a load-bearing theorem or
normalization decision.  Hahn's official AMS full text was inaccessible in
this environment and unauthorized mirrors were rejected.  Etale-groupoid
trace results were excluded because their hypotheses do not match the
continuous `R` action.  The screened-source log and redistribution boundary
are recorded in the manifest.

## 11. Final source verdict

**PASS for Phase-2 source coverage; no Phase-3 theorem is proved.**

The strongest sourced progress is the exact normalization chain:

```text
Lebesgue dt + counting on LZ
  -> quotient length Haar du (mass L)
  -> dual probability Haar dtheta/(2pi)
  -> regular identity coefficient L f(0).
```

The strongest remaining obstacle is not bibliographic.  It is the fixed-map
representation theorem: Paper 8 must identify its actual regular closure and
trace domain, then run the nonnormality argument in a trace-finite corner.
Once that closes, the character trace can be correctly described as an l.s.c.
semifinite C*-trace that is singular relative to the regular Haar completion,
without treating point evaluation as a normal `L-infinity` functional or as a
finite multiplier-centre restriction.
