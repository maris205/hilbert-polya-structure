# P47 paper plan

This writer-side plan is bound to the protected Stage0 and canonical State-A
authority tree.  It is not a publication verdict or an authorization to
write authority, Git, README, or mirror paths.  Infinite-operator statements
remain analytic-proof-owned; exact computation is finite implementation
replay.

## Working identity

- Working title: **The Harmonic-Quotient Graph Operator: Sharp Ideal
  Thresholds and a Mordell--Tornheim Trace**.
- Alternate title: **An Egyptian-Fraction Graph Operator with Zeta and
  Mordell--Tornheim Traces**.  The first is preferred because it names the
  frozen edge invariant without implying priority for Egyptian fractions.
- Format: anonymous, self-contained mathematical article; 11pt A4 article,
  not forced into an ICLR/NeurIPS/ICML template.
- Type: theorem paper with exact finite implementation replay.
- Structure: an unnumbered abstract, eight main sections, and four
  appendices.
- One-sentence contribution: For the Dirichlet-weighted adjacency of the
  looped graph `m+n | mn`, we prove sharp bounded/compact,
  Hilbert--Schmidt, and trace-class walls at `0`, `1/2`, and `1`, and identify
  its first two legal traces as `2^{-s} zeta(s)` and `zeta(2s)P(s)`, where
  `P(s)=sum_{(a,b)=1} a^{-s}b^{-s}(a+b)^{-2s}`, equivalently
  `zeta(2s) zeta_MT(s,s;2s)/zeta(4s)`.
- Claim boundary: one frozen graph, loops retained, real-logarithm complex
  powers, one-edge clock, and standard-basis adjacency on `ell^2(N)`; no
  all-`S_p` theorem, priority claim, rational-prime primitive ledger,
  completed target divisor, functional equation, or fixed Hilbert--Pólya
  operator.

## Reader and evidence contract

The article tells one story.  The divisibility relation has two exact edge
coordinates: a coprime-scale coordinate that makes global ideal and trace
sums transparent, and a divisor-row coordinate that makes boundedness and
compactness transparent.  The same looped graph then owns both the
`zeta(s)` first trace and the coprime Mordell--Tornheim second trace.  The
mixed triangle shows that this is not a disjoint collection of rank-one
scale fibers.

Three evidence types are separated at first use:

1. analytic proof establishes every infinite theorem, endpoint, and trace
   identity;
2. canonical finite replay checks independent direct and parameter
   implementations;
3. integrity and mutation audits establish reproducibility, not mathematics
   or novelty.

## Main theorem ledger

Let `s=sigma+i tau` and define the coefficient array

```text
e_s(m,n) = 1_{m+n divides mn} (mn)^(-s/2),  m,n>=1,
```

using the real logarithm.  We write `E_s` only when this array gives a
bounded operator on `ell^2(N)`.  The paper proves the following, with every
domain repeated locally.

1. **Two edge coordinates.**  Every ordered edge has a unique representation
   `m=t a(a+b)`, `n=t b(a+b)` with `t>=1` and `(a,b)=1`; its harmonic quotient
   is `k=t a b`.  For fixed `m`, neighbors are independently parametrized by
   `d|m^2`, `d<m`, through `n=m^2/d-m`.
2. **Boundedness and compactness.**  The array defines a bounded operator,
   which is then compact, exactly for `sigma>0`.  For `sigma<0`, even loops
   have unbounded modulus.  At zero, squarefree vertices have unbounded row
   support `(3^omega(m)-1)/2`.
3. **Sharp ideals.**  `E_s in S_2` exactly for `sigma>1/2`, and `E_s in S_1`
   exactly for `sigma>1`.
4. **First trace.**  The loops are exactly `m=n=2t`; hence, only in the
   trace-class domain,

   ```text
   Tr(E_s) = 2^(-s) zeta(s).
   ```

5. **Second trace and the realization theorem.**  On `sigma>1/2`,

   ```text
   Tr(E_s^2)
     = zeta(2s) sum_{(a,b)=1} a^(-s)b^(-s)(a+b)^(-2s)
     = zeta(2s)/zeta(4s) * zeta_MT(s,s;2s).
   ```

   Ordered edges are used, so no extra factor two appears.  The adjective
   “coprime” or “primitive” refers only to gcd-one edge coordinates, never
   to least temporal period.
6. **Legal determinants.**  `det_2(I-zE_s)` is an entire function of `z` on
   `sigma>1/2`; the ordinary Fredholm determinant is legal only on
   `sigma>1`.  On a sufficient disk `|z| ||E_s||<1`, with the logarithm
   normalized to zero at `z=0`,

   ```text
   log det_2(I-zE_s) = -sum_{r>=2} z^r Tr(E_s^r)/r.
   ```

   Consequently the quadratic coefficient of the local logarithm is
   `-Tr(E_s^2)/2`, namely minus one half of the displayed
   Mordell--Tornheim trace.  In the trace-class overlap,
   `det_2(I-zE_s)=det(I-zE_s) exp(z Tr(E_s))`.  No global logarithm or
   determinant outside its ideal domain is asserted.
7. **Mixed cycles and sign.**  `15 -> 30 -> 60 -> 15` is a triangle with
   harmonic quotients `10,20,12`.  For real `s>1`, the `{3,6}` principal
   block has determinant `-18^{-s}`.  Thus the graph is not a collection of
   isolated scale fibers and symmetry does not imply positivity.

## Complex-parameter firewall

Entrywise, and equivalently for every finite coefficient compression,

```text
e_s^(N) = U_tau^(N) e_sigma^(N) U_tau^(N),
U_tau e_n = n^(-i tau/2)e_n.
```

On `sigma>0`, where the infinite arrays are bounded operators, this passes
to the left--right factorization `E_s=U_tau E_sigma U_tau`.  It is not
unitary conjugacy.  It transfers boundedness, compactness, singular values,
ideal membership, and corresponding norms only.  It does not transfer
spectra, powers, traces, positivity, or determinants.  The trace and
determinant identities retain complex `s` and are proved directly from the
actual matrix and trace ideals.

## Protected and canonical bindings

- Protected authority manifest: 91 nodes, 67 regular files, 24 directories;
  SHA-256
  `30a79c4be4bc9b9333cb2a9f809d2039430cebc86686a054765734a782eea473`.
- Protected replay JSON SHA-256:
  `bd172e5a1f7523211f8784a4384c6e885f33d681b6bc8dc728bbd96ea378f4c3`.
- State-A output tree SHA-256:
  `328527680d533e34ce3aabc17f2cf5688759b0674b7fc8740d0c2df332b64c42`.
- State-A result-ledger SHA-256:
  `dba161719ef85dee433a13aa14505ab6b0f5ff0fef8c627ea39ddb4bf81bfe47`.
- Writer canonical summary SHA-256:
  `45185ea8750dec4557b055f0381137076df5d1615c51c482fa96e623f8ed1d7f`.
- Canonical finite support counts `(N, ordered edges, loops)`:
  `(16,16,8)`, `(32,40,16)`, `(64,96,32)`, `(128,228,64)`.
- X comparison checks: 12 exact PASS fields.  All reported finite numbers
  are implementation controls, never endpoint evidence.

## Claims--evidence backbone

The detailed matrix is `CLAIMS_EVIDENCE.md`.  Its high-level allocation is:

| Claim | Analytic proof owner | Finite replay owner | Writing status |
|---|---|---|---|
| unique coprime-scale and divisor-row coordinates | gcd and divisor algebra | D/P/X full support and rows | theorem plus constructive lemmas |
| bounded/compact iff `sigma>0` | row Schur decay, finite-rank approximation, loop/degree obstructions | proof-contract fields only | no finite inference |
| `S_2` iff `sigma>1/2` | scale sum and coprime majorant | exact second-trace controls | strict endpoint |
| `S_1` iff `sigma>1` | entrywise sum and even diagonal | domain/type audits | strict endpoint |
| zeta and coprime-MT first two traces | loop ledger, ordered-edge sum, gcd extraction | four exact finite projections | central theorem |
| mixed triangle and negative minor | exact arithmetic witnesses | D/P/X and exact rational minors | anti-fiber/sign control |

## Executable page budget

No conference-template main-page limit is imposed.  The target is about
16.3 A4 pages inclusive: 11.2 pages through Section 8, 1.1 pages of
references, and 4.0 pages of appendices.  The following allocations include
three vector TikZ figures and three compact tables.

### Abstract — 0.35 page, 170--210 words

- Start with the exact graph and three strict walls.
- State both traces in their legal domains and identify the coprime
  Mordell--Tornheim factor without priority language.
- Mention the two parameterizations and mixed triangle.
- End with one sentence labeling the four finite cutoffs as independent
  implementation replay rather than proof.

### 1. Introduction — 1.35 pages, includes Figure 1

- Open with the same-object tension: a simple Egyptian reciprocal relation
  creates both operator-ideal walls and a classical multiple Dirichlet
  series inside the trace ledger.
- State the gap narrowly: classical MT theory does not identify this
  operator, while a phase diagram alone would repeat shared infrastructure.
- Give the coprime-scale/divisor-row strategy before technical detail.
- Provide three falsifiable contribution bullets: exact coordinates and
  walls; first/second trace realization; mixed-cycle and determinant
  consequences.
- State proof/computation/provenance separation and no-priority boundary.

### 2. Related work and ownership boundaries — 0.90 page

- Synthesize Tornheim and Mordell as classical ownership of the double sums.
- Position Bradley--Zhou and Tsumura as identity/functional-relation
  background, not operator ownership.
- Contrast the distinct `(s,s;s)` tropical boundary realization of
  Kalinin--Lupercio--Shkolnikov with the present `(s,s;2s)` graph trace.
- Use Simon only for standard trace-ideal and determinant definitions.
- End with the bounded-search disposition and explicitly avoid priority.

### 3. Harmonic graph and two exact edge coordinates — 1.50 pages,
includes Figure 1 continuation

- Define the looped graph, one-sided edge shift, one-edge clock, based closed
  vertex words, temporal primitive type, marker `z`, and coefficient array.
- Derive `1/m+1/n=1/k`, the unique `(t,a,b)` coordinate, and `k=tab`.
- Independently derive `d=m-k`, `d|m^2`, `n=m^2/d-m`.
- Classify loops and state the complex left--right firewall.
- Include a typed-object table distinguishing vertices, harmonic quotients,
  edge coordinates, temporal cycles, and the marker.

### 4. Boundedness and compactness — 1.30 pages

- Write the exact row sum
  `R_m=m^{-sigma} sum_{d|m^2,d<m} (d/(m-d))^(sigma/2)`.
- Split at `d=m/2`; for the upper half put `e=m-d`, use `d|e^2`, and obtain
  `R_m << tau(m^2)(m^{-sigma}+m^{-3sigma/4}) -> 0`.
- Apply the symmetric Schur test and prove
  `||E_s-P_N E_s P_N|| -> 0` by tail Schur bounds plus finite-rank cross
  terms.
- Treat `sigma<0` with even loops and `sigma=0` with squarefree row support.

### 5. Sharp Hilbert--Schmidt and trace-class thresholds — 1.60 pages,
includes Figure 2 and Table 1

- Derive the exact Hilbert--Schmidt norm square as the scale sum times the
  coprime double sum.
- Use loops for necessity at `1/2`, and `(a+b)^2>=4ab` for sufficiency.
- Prove trace-class sufficiency from absolute entry summability bounded by
  `2^{-sigma} zeta(sigma)^3`.
- Prove necessity from the absolute standard-basis even diagonal.
- Display all strict endpoints and determinant permissions in the phase
  figure/table.

### 6. Zeta and Mordell--Tornheim traces — 2.25 pages

- Prove the loop trace only after trace-class legality.
- Prove `E_s^2` trace class from `E_s in S_2`, then compute its trace as the
  ordered-edge sum with no factor two.
- Extract `zeta(2s)` from the infinite scale and derive
  `zeta_MT(s,s;2s)=zeta(4s)P(s)` by gcd decomposition.
- Separate absolute convergence of the series from every possible analytic
  continuation.
- State the determinant corollary, the local logarithmic series, and the
  exact first two coefficients; include a proof sketch and put standard
  determinant details in Appendix C.

### 7. Mixed cycles, temporal typing, and sign — 1.05 pages,
includes Figure 3

- Verify the triangle and its three harmonic quotients.
- Explain why edge-coordinate primitivity is different from least temporal
  period and why division by walk length in a determinant logarithm only
  removes a base point.
- Verify the negative `{3,6}` principal minor in the real trace-class
  domain.  Do not call nonreal `E_s` Hermitian.

### 8. Canonical replay, limitations, and conclusion — 0.90 page,
includes Table 2

- Report the four cutoff counts and a compact second panel listing all twelve
  exact comparison PASS key names from the mechanically generated
  candidate-local summary.
- State the finite termwise cutoff distinction explicitly.
- Compress mutation and hash information to one sentence; move details to
  Appendix D.
- Conclude by restating the same-object realization in different words.
- Give exact limitations: no intermediate all-`S_p` classification, no
  priority, no completed divisor or target functional equation, and no fixed
  self-adjoint spectral lift.
- Name one concrete next question: determine intermediate Schatten behavior
  of this same frozen harmonic graph without extrapolating from `p=1,2`.

### Appendices — 4.0 pages total

- **A (1.0):** divisor-row bijection, row decay, compactness tail estimate,
  and the squarefree endpoint.
- **B (1.0):** exact ideal sums, diagonal trace-norm obstruction, and complex
  phase/singular-value details.
- **C (1.2):** trace-ideal justification, MT convergence/gcd extraction,
  and local Fredholm/`det_2` logarithms.
- **D (0.8):** mechanically extracted State-A ledger, a compact checklist of
  all twelve PASS key names, canonical hashes, mutation counts, Route
  rejection, and evidence firewall.

## Figure and table plan

No numerical trend plot is justified: the evaluated evidence is exact and
discrete.  All mathematical figures are vector TikZ, and all evaluated
tables are generated mechanically from `canonical_summary.json`.

| ID | Type | Content and comparison | Source | Priority |
|---|---|---|---|---|
| Figure 1 | hero flow diagram | one direct relation feeds the coprime-scale and divisor-row coordinates; the former exposes ideal/trace sums while the latter exposes row decay; both return to the same `E_s` | analytic theorem, manual TikZ | high |
| Figure 2 | phase diagram | strict walls at `0,1/2,1`, with bounded/compact, `S_2`/`det_2`, and `S_1`/ordinary determinant bands; endpoint markers are open | analytic theorem, manual TikZ | high |
| Figure 3 | arithmetic graph witness | triangle `15,30,60`, edge quotient labels `10,20,12`, and the `{3,6}` negative-minor inset | exact witness ledger, manual TikZ | medium |
| Table 1 | theorem phase table | properties, exact domains, decisive boundary witnesses | generated from frozen theorem constants | high |
| Table 2 | canonical replay table | first panel: cutoff, ordered-edge count, loop count; second panel: all twelve exact PASS key names; caption states finite implementation replay | canonical summary, generated | high |
| Table 3 | ownership/type table | mathematical object, owner, and forbidden identification | source/type contracts | medium |

Figure 1 caption draft: “Two independent coordinates of the same looped
harmonic graph divide the proof labor.  Gcd reduction produces the unique
coprime-scale edge coordinate and therefore the global ideal and trace sums;
row elimination produces the divisor coordinate and therefore vanishing
Schur rows.  Neither coordinate changes the temporal edge clock.”

## Citation plan

- Introduction: Tornheim, Mordell, and Simon only after the frozen operator
  is stated.
- Related work: all six verified records, organized by mathematical role.
- Ideal and determinant sections: Simon for standard definitions and
  inequalities; specialized estimates reproduced.
- Trace section: Tornheim/Mordell for historical ownership;
  Bradley--Zhou/Tsumura for classical MT context.
- Ownership boundary: Kalinin--Lupercio--Shkolnikov only for the distinct
  tropical `(s,s;s)` primitive realization.
- Bibliography entries come only from `evidence/SOURCE_VERIFICATION.md` and
  remain filtered to cited keys.

## Formal plan-review gate

An independent GPT-5.4 xhigh reviewer must score logical flow,
claim--evidence alignment, mathematical domains, source positioning, page
feasibility, and front-matter strength.  `paper-figure` and `paper-write`
begin only after the same reviewer returns `PLAN_READY` with zero critical
and zero major issue.  Raw reviews are preserved in `reviews/`.

## Hard writing gates

1. `POST-OUTPUT CLEAN` received for the 47-static + 20-State-A authority
   tree before writer creation.
2. Protected 91-node capture and State-A replay PASS.
3. Plan review reaches `PLAN_READY` before figures or manuscript prose.
4. Every figure is vector and every canonical table regenerates exactly.
5. Baseline compilation succeeds before the two-round improvement loop.
6. GPT-5.4 xhigh reviews two rounds; each fix is global and followed by a
   clean fixed-epoch rebuild.
7. Final PDF passes fonts, text, bbox, and page-by-page visual QA.
8. Protected replay is unchanged immediately before self-excluding writer
   manifest, report, handoff, and seal closure.
