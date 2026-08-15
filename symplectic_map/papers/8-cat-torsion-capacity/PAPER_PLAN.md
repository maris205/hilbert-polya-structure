# Paper Plan

## Frozen identity and release state

**Title:** *A Primitive-Divisor Audit of Prime-Order Torsion Periods for
Hyperbolic Toral Automorphisms*

**Article type:** scoped mathematical technical note / exact audit.

**One-sentence thesis:** primitive divisors give prime-additive-order carriers
of every prescribed dynamical period above the sharp uniform threshold
$12$, while the standard cat map has the exact carrier exception set
$\{1,6,12\}$; nevertheless, the intrinsic torsion-order label is far too
nonspecific and irregular to supply the later Route-A structure by itself.

**Required conclusion label:**
`INTRINSIC_TORSION_CAPACITY_CERTIFIED / A0_FAIL_PROVES_TOO_MUCH`.

> **Release gate:** `FINAL RESULT MANIFEST / POST-RUN ANALYZER CLOSURE:
> PASS`. The read-only V2 closure passed with manifest SHA-256
> `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f`.
> Manifest closure authorizes figure and manuscript production under the
> frozen scope; it does not authorize a candidate rerun or any new scientific
> result.

### Frozen inputs

| Role | Path | SHA-256 / state |
|---|---|---|
| proof source | `notes/PROOF_PACKAGE.md` | `ee02fe72071c0bbea26f5f34c28130374fe1a919195cfbe154f6f5a39ab420af` |
| novelty source | `notes/NOVELTY_AUDIT.md` | `dcc30076f31099db5fb960284374819c39fdbf5f9a5c9348c19bf5ed92a22212` |
| source lock | `experiments/source_lock.json` | `87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce` |
| raw exact result | `results/EXPERIMENT_RESULTS.json` | `0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0` |
| current post-run review | `results/POSTRUN_ANALYZER_REVIEW.md` | `POSTRUN_ANALYZER_PASS`; `42e4e2010be2d5cbb51a2ceb1fd9a1f8048bcec17daa2767c9f38cebaaa6fdcd` |
| final result manifest | `results/result_manifest.json` | **PASS**; `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f` |
| official experiment report | `experiments/OFFICIAL_EXPERIMENT_RESULTS.md` | `4cf1645505a835a9d0aa62d84e7b6b47fc708b1347a954eeac26eb9710b9187d` |
| official validation report | `experiments/OFFICIAL_VALIDATION_REPORT.md` | `ac9ac741cffd89dc8ab32db654ae59dc901b823a4b496be0607c7ce05fd403c3` |

The paper must not silently substitute later versions of these inputs. The
final manifest closure is complete; any changed proof, result, review, or
manifest requires a fresh claim/evidence review and a new binding record.

## Scope and positioning

### In scope

1. A prime-order carrier theorem for every hyperbolic
   $M\in\mathrm{SL}_2(\mathbb Z)$ and every $n>12$.
2. The elementary bridge from a primitive rational prime divisor of
   $\det(M^n-I)$ to a nonzero $p$-torsion point of exact period $n$,
   including the exact cycle count from the kernel dimension.
3. The separate negative-trace parity reduction through $B=-M$.
4. The exact standard-cat classification, including the ramified
   modulo-five Jordan repair at $n=10$ and exclusions at $1,6,12$.
5. The capacity-versus-specificity audit for
   $L(x)=\log\operatorname{ord}(x)$ on torus torsion.
6. A small exact, registered, no-external-data audit used as corroboration
   and falsification control, never as evidence for the infinite tail.

### Out of scope and explicit nonclaims

- No Riemann Euler product, explicit formula, prime/zero matching, or
  prime-orbit correspondence.
- No transfer-operator, Fredholm-determinant, or dynamical-zeta novelty.
- No quantization, quantum operator, Hilbert--Pólya, or quantum-cat novelty.
- No amplitudes, signs, repetitions, or trace-formula reconstruction.
- No Route-A claims beyond A0 and no claims on A1--A4 or Route B.
- No claim that primitive divisors are necessary for carriers: $n=10$ is
  an explicit counterexample to that converse.
- No priority claim. The work is positioned as a low-to-moderate-novelty
  synthesis and exact audit built from a classical arithmetic engine.

Use the verbs **derive**, **record**, **audit**, and **synthesize**. Avoid
“first,” “discover,” “prime-generating cat map,” “Riemann dynamics,” and
“natural quantization of the order clock.”

## Reader, format, and length

The primary reader is a researcher in arithmetic dynamics, smooth dynamics,
or mathematical physics who knows toral automorphisms but may not know the
primitive-divisor literature. The target is a self-contained journal-style
technical note; a venue is not frozen.

Planned length: approximately 12 pages of main text plus 4--6 pages of
appendices. The full negative-trace conversion and the modulo-five Jordan
argument remain in the main text because both prevent plausible but false
shortcuts. Mechanical ledger details and provenance checks may move to
appendices.

## Claims--evidence matrix

| ID | Manuscript-level claim | Mathematical support | Exact audit support | Literature boundary | Release status |
|---|---|---|---|---|---|
| C1 | If $M\in\mathrm{SL}_2(\mathbb Z)$, $\lvert\operatorname{tr}M\rvert>2$, then every $n>12$ has a prime-additive-order point of exact $M$-period $n$. | Norm--determinant identity; Flatters' norm-one theorem; primitive-kernel lemma; Paper 8's separate three-case proof for negative trace. | `general_theorem_contract`; explicitly no period above 12 computed. | Flatters is the imported arithmetic engine; do not attribute the negative-trace extension to Flatters. | Proof frozen; manifest-bound result released. |
| C2 | A primitive divisor $p\mid\det(M^n-I)$ makes every nonzero vector in the mod-$p$ kernel an order-$p$, exact-period-$n$ carrier; a kernel of dimension $r$ gives $(p^r-1)/n$ cycles. | Elementary finite-field kernel proof and orbit partition. | `general_theorem_contract.primitive_kernel`. | Classical finite-lattice work supplies context, not this proof's novelty. | Proof frozen; manifest-bound result released. |
| C3 | For $A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)$, a prime-order exact-period carrier exists iff $n\notin\{1,6,12\}$. | Exact determinant ledger; primitive-kernel lemma; direct reductions mod $2,3,5$; Flatters for $n>12$. | `boundary_summary`, `ledger_records`, `finite_field_records`. | Gaspari is especially close for prime lattices; Flatters supplies the small Lehmer--Pierce table and tail. | Proof frozen; manifest-bound result released. |
| C4 | The threshold $12$ is sharp, and $n=10$ shows primitive divisibility is sufficient but not necessary. | Failure at $n=12$; modulo-five nilpotent/Jordan calculation gives 20 points and two period-10 cycles. | `boundary_summary.exception_set`, `jordan_period_ten_points`, `jordan_period_ten_cycles`. | State as an exact synthesis, not a priority result. | Proof frozen; manifest-bound result released. |
| C5 | $\operatorname{Per}(T_A)=\operatorname{Tor}(\mathbb T^2)$; $L=\log\operatorname{ord}$ is invariant, realizes all positive integers after exponentiation, and is unbounded and discontinuous in every torsion neighborhood. | Integer-matrix invertibility; rational inverse of $A^n-I$; coprime perturbation proof. | `clock_specificity.range`, `regularity`, `all_order_witnesses`, `discontinuity_witnesses`. | The order label itself has essentially no novelty. | Proof frozen; manifest-bound result released. |
| C6 | On an order-$p$, period-$n$ orbit, $S_nL=n\log p$ and an $r$-fold traversal gives $rn\log p$, while $D(T_A^n)=A^n$ is period-dependent and torsion-order-blind. | Invariance of order and linearity of the map. | `clock_specificity.orbit_sum_monodromy`. | Ruelle/Parry--Pollicott are context only; no zeta or transfer theorem follows. | Proof frozen; manifest-bound result released. |
| C7 | The correct Route-A decision is capacity certified but A0 rejected as nonspecific: `A0_FAIL_PROVES_TOO_MUCH`. | C1--C6 together, with prime and composite orders produced by the same mechanism. | Frozen `classification`; zero candidate numerical runs and no external tables. | No transfer or quantization novelty is claimed. | Scientific interpretation and provenance released. |

## Core notation and theorem order

Introduce only the notation needed for the proofs:

\[
T_M(x)=Mx\pmod{\mathbb Z^2},\qquad
\Delta_n(M)=\det(M^n-I),\qquad
V_p=(\mathbb Z/p\mathbb Z)^2.
\]

A nonzero $v\in V_p$ represents $x_v=v/p\in\mathbb T^2$, which has
exact additive order $p$. “Period” always means least positive dynamical
return time. “Prime-order” always means additive group order, not primitive
orbit length. These two uses of “order” must never be conflated.

Recommended logical order in the paper:

1. primitive determinant divisor \(\Rightarrow\) exact prime-order carrier;
2. positive-trace norm identity and Flatters corollary;
3. negative-trace three-case conversion;
4. standard-cat exact boundary and sharpness;
5. torsion-order clock and specificity obstruction;
6. exact audit and limitations.

## Section-by-section outline

### Abstract (150--180 words)

State C1, C3, and the capacity/specificity conclusion. Say explicitly that
the positive-trace tail is a Flatters corollary and the negative-trace case
uses a separate parity argument. Mention the sharp standard-cat exception
set and the $n=10$ Jordan repair. End with the obstruction: the intrinsic
order clock realizes primes and composites indiscriminately, is nowhere
regular on torsion, and its Birkhoff/derivative data do not isolate
\(\log p\). Do not cite papers or mention unfinished provenance in the
abstract; provenance belongs in the reproducibility statement.

### 1. Introduction and bounded question (1.25 pages)

Open with the precise question: for a prescribed dynamical period $n$,
does a hyperbolic toral automorphism possess a periodic point whose additive
order is a rational prime? Separate this cross-prime prescribed-period
question from fixed-modulus orbit classification and aggregate periodic-point
counting. Summarize C1--C7 in one numbered contribution paragraph.

Position the result beside arithmetic cat-map studies
\cite{PercivalVivaldi1987Arithmetic,Gaspari1994Arnold,DysonFalk1992Period,
BaakeRobertsWeiss2008Periodic,BaakeNeumaerkerRoberts2013Orbit} and identify
Flatters \cite{Flatters2009Primitive} as the direct arithmetic engine.
Mention recent fixed-residue-ring and spectral-landscape work only to bound
novelty \cite{TanLi2025Graph,Chandra2026Arithmetic}. State that classical
dynamical-zeta and quantum-cat literatures are context, not contributions of
this note \cite{Ruelle1976Zeta,ParryPollicott1990Zeta,
HannayBerry1980Quantization,KurlbergRudnick2000Hecke}.

End with a roadmap and the exact scope exclusions.

### 2. Arithmetic and dynamical preliminaries (1.5 pages)

Define torsion order, exact period, primitive rational prime divisor, and
the Lehmer--Pierce sequence. Record the fixed-point count identity
$\lvert\det(M^n-I)\rvert$ only as background; do not mistake aggregate counts for
prime-order carrier counts.

Organize related work into four nonoverlapping lanes:

1. arithmetic classification of cat-map orbits and prime lattices;
2. matrix periods and local/global rational-lattice orbit counts;
3. primitive divisors of quadratic norm sequences;
4. dynamical-zeta and quantum-cat context that is explicitly outside the
   novelty claim.

Close with a boxed attribution rule: Flatters proves the positive norm-one
primitive-divisor statements; all conversion from a negative-trace matrix
$M$ through $B=-M$ is Paper 8's elementary argument.

### 3. Prime-order carriers above the uniform threshold (2.75 pages)

#### 3.1 Primitive-kernel lemma

Prove that primitive $p\mid\Delta_n(M)$ gives a nonzero kernel and excludes
every smaller return. Include the cycle-count corollary
$(p^r-1)/n$, where
$r=\dim_{\mathbb F_p}\ker(M^n-I)\in\{1,2\}$.

#### 3.2 Positive trace

For $t=\operatorname{tr}M>2$, let
$\alpha=(t+\sqrt{t^2-4})/2$. Display

\[
N_{\mathbb Q(\alpha)/\mathbb Q}(\alpha^n-1)
=2-\alpha^n-\alpha^{-n}=\det(M^n-I).
\]

Invoke Flatters, Theorem 1.4, with its positive quadratic norm-one hypotheses
visible at the citation point. Do not rebrand the imported theorem as new.

#### 3.3 Negative trace

Set $B=-M$ and give the full parity table:

| requested $M$-period | primitive index for $B$ | reason |
|---|---:|---|
| $n$ odd | $2n$ | exact $B$-period $2n$ forces $B^nv=-v$ |
| $4\mid n$ | $n$ | parity excludes a smaller $M$-return |
| $n=2k$, $k$ odd | $k=n/2$ | $p\ne2$ and $M^kv=-v$; $k=7,9,11$ use Flatters Theorem 3.1 |

Explicitly reject the tempting use of index $n$ in the
$n\equiv2\pmod4$ branch. Conclude C1 without any computed period above
12. Figure 1 supports this section.

### 4. The standard cat: exact boundary and a nonprimitive repair (2.5 pages)

Set $A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)$,
$s_{n+2}=3s_{n+1}-s_n$, and $\Delta_n=2-s_n$. Present the $n\le12$
ledger in a compact table, distinguishing “new determinant divisor” from
“carrier exists.” Apply the primitive-kernel lemma at
\(n=2,3,4,5,7,8,9,11\).

Give the modulo-five calculation in full:

\[
N=A+I,\qquad N^2=0,\qquad \operatorname{rank}N=1,\qquad
A^k=(-1)^kI+k(-1)^{k-1}N.
\]

Count four nonzero kernel points of period two and twenty points outside the
kernel of exact period ten, hence two period-ten cycles. This is the key
warning that primitive divisibility is not a necessary criterion.

For exclusions, use only the determinant supports and complete period
profiles modulo $2,3,5$: periods $3$, $4$, and $2/10$, respectively.
Conclude the iff classification and sharpness at $n=12$. Figure 2 is the
main visual evidence summary.

### 5. Capacity is not specificity (1.75 pages)

First prove
\(\operatorname{Per}(T_A)=\operatorname{Tor}(\mathbb T^2)\). Define
\(L(x)=\log\operatorname{ord}(x)\) only on torsion. Prove invariance under
unimodular maps and exhibit $x_m=(1/m,0)$ for every $m\ge1$.

Use the coprime perturbation
\(y_k=x+(1/N_k,0)\), \(\gcd(N_k,m)=1\), to obtain
\(\operatorname{ord}(y_k)=mN_k\) and show local unboundedness and
discontinuity. Then contrast

\[
S_nL(x)=n\log p,\qquad S_{rn}L(x)=rn\log p,
\]

with the raw orbit label \(\log p\), and with
\(D(T_A^n)_x=A^n\), for which the logarithm of the modulus of the unstable
multiplier is $n\log\rho(A)$ and is independent of $p$. Explain why division
by $n$ imports the global least period rather than producing a fixed local
continuous observable. Figure 3 supports this section.

Close with the exact interpretation: the map has abundant intrinsic torsion
capacity, but the order clock proves too much because it realizes prime and
composite orders by the same construction.

### 6. Exact audit and falsification controls (1.0 page)

Describe the audit as an exact consistency check of already frozen
mathematics, not a numerical discovery experiment. Report only values bound
to the closed raw result after final manifest approval:

- one registered exact audit and periods $1,\ldots,12$;
- zero candidate numerical runs;
- no generated prime-target arrays, external prime tables, zero data, or
  floating/approximate matching;
- no computed period above 12;
- exact agreement of recurrence and matrix-power determinant engines;
- exact finite-field profiles for $p=2,3,5,7,11,19,29,199$;
- the frozen exception set and clock witnesses.

The final V2 manifest and independent Round-2 analyzer review now pass. When
manuscript drafting is separately authorized, this section may use the exact
manifest-bound values and must retain the theorem/computation firewall.

### 7. Limitations, novelty boundary, and conclusion (1.0 page)

Reiterate that the tail theorem is a corollary plus parity conversion, the
standard-cat statement is an exact synthesis, and the order clock is an
obstruction rather than a new observable theory. State the bounded-search
qualification: no source was located that packaged both main conclusions,
but absence was not proved.

Separate the result from dynamical-zeta/transfer and quantization literatures.
Do not speculate that later mechanisms exist. End with the required
classification label and the concrete unresolved requirement: additional
structure would have to distinguish primes from composites and supply the
missing orbit weights/repetitions, none of which is furnished here.

### Appendices (4--6 pages)

- **Appendix A:** complete proof audit, including the $p\ne2$ argument in
  the half-index negative-trace branch.
- **Appendix B:** full $n\le12$ determinant/factor ledger and direct
  modulo-$2,3,5$ calculations.
- **Appendix C:** exact JSON field map, source-lock hashes, and the passed
  final post-run manifest statement.

## Planned vector figures

Exactly three figures are planned. They must be produced as vector PDF/SVG
with embedded/selectable text, a color-blind-safe palette, and a legible
grayscale fallback. No raster screenshots, decorative cat imagery, external
datasets, or values absent from the theorem/raw JSON are permitted.

### Figure 1 (hero): From a determinant divisor to every period above 12

**Message:** the general theorem is a short exact chain, with a genuinely
separate negative-trace conversion.

**Layout:** a three-panel horizontal vector diagram.

- **A, arithmetic bridge:** norm identity \(\to\) primitive $p$ \(\to\)
  nonzero mod-$p$ kernel \(\to\) order-$p$, exact-period-$n$ carrier,
  with \((p^r-1)/n\) cycles under the final node.
- **B, sign/parity routing:** positive trace goes directly to Flatters;
  negative trace passes through $B=-M$ and branches into odd $n$,
  $4\mid n$, and $n=2k$ with $k$ odd, labeled by primitive indices
  $2n,n,k$.
- **C, theorem range:** a number-line boundary at $12$, with every
  $n>12$ certified and no suggestion of computation in the tail.

**Sources:** `notes/PROOF_PACKAGE.md`, especially Steps 1--3, and
`results/EXPERIMENT_RESULTS.json/general_theorem_contract` for assertion
flags only. **Validation:** every arrow corresponds to a proved implication;
the caption must say Flatters supplies the positive norm-one primitive
divisor and Paper 8 supplies the negative-trace conversion.

### Figure 2: The standard-cat carrier boundary at periods 1--12

**Message:** primitive divisors settle most small periods, the ramified
$p=5$ Jordan structure repairs period 10, and exactly $1,6,12$ fail.

**Layout:** a two-tier categorical strip for $n=1,\ldots,12$.

- Top tier: each $n$ labeled with \(\Delta_n\) and either its selected new
  divisor or “none.”
- Bottom tier: carrier status and carrier prime; $n=10$ receives a distinct
  “Jordan repair” glyph labeled “20 points / 2 cycles,” while $1,6,12$
  receive exclusion marks.
- A small inset shows the exact profiles
  $p=2:\{3:3\}$, $p=3:\{4:8\}$,
  $p=5:\{2:4,10:20\}$.

**Sources:** `ledger_records` and `boundary_summary` in the raw JSON, checked
against Steps 4--6 of the proof. **Encoding:** categorical shapes in addition
to color; no log-scale bar chart, since magnitude of \(|\Delta_n|\) is not
the claim. **Validation:** the exception set must be parsed from JSON, not
typed independently; all twelve determinant values must agree with both
exact engines. Generation is authorized from the manifest-bound raw result.

### Figure 3: Capacity versus specificity of the torsion-order clock

**Message:** the same intrinsic label that reaches all orders is invariant
and orbit-readable, but it is locally unbounded and does not match the native
period-only derivative clock.

**Layout:** a three-panel vector diagnostic.

- **A, range:** the single construction $x_m=(1/m,0)$ feeds both prime and
  composite $m$, visually emphasizing the lack of prime specificity.
- **B, regularity:** an order-18 base point with the exact frozen
  perturbations $N=19,55,127$ and resulting orders $342,990,2286$,
  illustrating divergence as displacement tends to zero.
- **C, orbit/native comparison:** for the order-5, period-10 carrier, show
  \(L=\log5\), \(S_{10}L=10\log5\),
  \(S_{10r}L=10r\log5\), beside
  \(A^{10}=\left(\begin{smallmatrix}10946&6765\\6765&4181\end{smallmatrix}\right)\)
  and characteristic coefficients \([1,-15127,1]\), labeled
  “period-dependent / torsion-order-blind.”

**Sources:** `clock_specificity` in the raw JSON and Steps 7--9 of the proof.
**Validation:** use exact strings/rationals from JSON; do not numerically
approximate logarithms or eigenvalues. The caption must state that the three
perturbations illustrate the general coprime-sequence proof rather than
establishing discontinuity by sampling.

## Planned tables

1. **Table 1:** claims, provenance, and attribution map (condensed from the
   matrix above).
2. **Table 2:** negative-trace parity cases and primitive indices.
3. **Table 3:** full standard-cat determinant/factor/carrier ledger.
4. **Table 4 (appendix):** frozen finite-field period profiles and their
   evidentiary role.

Tables 3--4 must be rendered only from the now-closed, manifest-bound JSON.
The theorem tables may be typeset from the frozen proof and independently
cross-checked against JSON.

## Citation plan

- Cite Flatters at every imported primitive-divisor theorem/table use.
- Cite Percival--Vivaldi and Gaspari for classical arithmetic orbit and prime
  lattice context.
- Cite Dyson--Falk and both Baake et al. papers for global/local rational
  lattice periods, orbit structure, and zeta-counting context.
- Cite Kannan et al. for the ordinary hyperbolic two-torus period-set
  baseline and Seibt for rational-lattice period formulae; neither source is
  evidence for a prime-additive-order carrier theorem.
- Cite Tan--Li and Chandra as recent neighboring work, explicitly preserving
  their preprint status and not importing broader novelty claims.
- Cite Ruelle and Parry--Pollicott only when distinguishing this audit from
  classical dynamical-zeta/transfer formalism.
- Cite Hannay--Berry and Kurlberg--Rudnick only to delimit quantum-cat work.

All metadata and allowed citation roles are frozen in
`notes/CITATION_VERIFICATION.md`; BibTeX keys are frozen in
`paper/references.bib`.

## Writing and review invariants

1. Always write “additive order $p$” when first introducing a carrier.
2. Keep point counts and primitive-cycle counts separate.
3. Keep primitive-divisor exceptions and carrier exceptions separate;
   $n=10$ differs between them.
4. Never say Flatters proves the negative-trace matrix theorem.
5. Never use the finite $n\le12$ audit to support the infinite tail.
6. Never present the clock's all-integer range as prime selectivity.
7. Never call $L/n$ a fixed local potential; $n$ is the global least
   return time.
8. Keep classical derivative monodromy separate from torsion order.
9. Treat Chandra (2026) and Tan--Li (2025) as preprints at the search cutoff.
10. Bind figures and manuscript provenance to the passed V2 manifest and
    Round-2 independent analyzer authority.

## Pre-writing gates

- [x] Final result manifest exists and passes a fresh independent post-run
      analyzer review, including read-only validation of its post-write
      inventory.
- [x] The final manifest hash is added to the frozen-input table.
- [ ] A proof reviewer rechecks all three negative-trace branches, the
      $p\ne2$ sublemma, the modulo-five Jordan count, and the exclusions.
- [ ] Every Figure 2/3 value is generated from the manifest-bound raw JSON.
- [ ] All BibTeX entries compile and all DOI/arXiv links resolve.
- [ ] The abstract, introduction, and conclusion contain none of the
      forbidden novelty or transfer/quantization claims.
- [ ] The artifact statement reports zero candidate numerical runs, no
      external prime/zero data, and no tail computations exactly as recorded.

The release gate has passed; the remaining unchecked items govern later
manuscript review and compilation.
