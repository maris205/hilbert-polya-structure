# Independent internal review — ordinary scalar orbit zeta

Audit ID: ASFS-AUDIT-20260920-APZ01.
Candidate ID: ANG-20260920-APR01, unchanged from 288/289.
Date: 2026-09-20.
Status: ORDINARY ORBIT ZETA ESTABLISHED; TRACE/FREDHOLM OWNER OPEN — SCOPED ADVANCE / FORK.

## 1. Scope, bindings and review provenance

This review uses the ARS raw-card, manuscript-comparison and final
adverse checkpoints. Its subject is the frozen ordinary unit-weight
orbit function and derived time-counting measure, not an operator,
determinant, trace formula, quantum construction or formal Route audit.
Only this report is reviewer-authored; all earlier packages are read-only.

Exact SHA-256 bindings:

- 291 original candidate-card.md:
  76830495c7e32a08de4dc270d620e6144ce307da3d8360b67954e5332464f413.
- 288 candidate-card.md:
  cb48100913138d23d66b89e91c0502e5920337cc0c9969f31d33d9cf441fdc78.
- 288 paper.md:
  b20fa7e047eabcb036e95b60a6a2255f60bb11419ef9d588df7c5d86d86c78b8.
- 289 candidate-card.md:
  a7bcac69bc0552bc91f137dfe4739a58c8056140aa6dc3cda4e2c9640206015b.
- 289 paper.md:
  857e2a8b5ec91aaddfe759a9a068c0e1de616a37eb763efc692d8b9180181826.
- Initial 291 manuscript, fully read, 284 lines:
  044d83beb21fd8b616b2a021f55ad36e9d9253523f3aa213344026199f9a73d3.
- Final 291 manuscript, after targeted Section 5 readback, 295 lines:
  7dd25c66e30d80a454f0a375c29caacf993280fa85231e82ec5358054ad3f366.

The entire new card was read before any 291 manuscript. The unchanged
288/289 papers had previously been fully reviewed; their hashes and all
four source locks were checked again, and the ledger, null-set, controls
and full-circle passages were reread before this manuscript. Raw analytic
conclusions were sent to the root author before manuscript access.
The card binding is the original freeze, not a later outcome appendix.

A bounded auxiliary read only the raw card and its stated control
dependencies to check coefficients and Haar/counting scope. Its conclusions
arrived after the main reviewer's raw findings and before manuscript
access. It supplied no convergence proof, external citation or manuscript
judgment. The agents inherit the same model and substantial shared context.
This is not external peer review, cross-model verification, formal
verification, or an independent-error guarantee.

Exactly one external page was opened: [NIST DLMF §25.2](https://dlmf.nist.gov/25.2).
Only Equation 25.2.1 and the continuation paragraph in §25.2(i) are used:
the usual Dirichlet definition for Re s>1 and classical meromorphic
continuation, with its sole pole at 1, simple and of residue one.
No external Euler-product proof or zero-location input replaces the
independent derivation below. No broader source campaign was performed.

## 2. Checkpoint 1 — independent raw-card findings

**Owner and counting.** The complete same-candidate ledger gives precisely
one primitive oriented time orbit gamma_p for each prime, least log p.
Finite preimages and all phases stay in that packet, not additional
Euler factors. Unit weights and the denominator 1/r are an expressly
declared ordinary counting convention, not derived stability weights.
Counting closed orbits does not remove other states from the owner.

**Local finiteness.** If r log p<=R, then p<=exp R and
r<=R/log 2. Only finitely many pairs occur. Hence the positive measure
sum_(p,r) log p delta_(r log p) is locally finite, with minimum support
time log 2. It is a measure on positive time, not a joint-Haar density.

**Convergence.** On every compact subset with Re s>=sigma_0>1,
the logarithmic double series is dominated by
(1-2^(-sigma_0))^(-1) sum_(n>=2) n^(-sigma_0).
The differentiated series has the same majorant with a factor log n.
Both are normally absolutely convergent. Thus exp L_C is holomorphic,
nonzero and equals the ordinary product of (1-p^(-s))^(-1).

Finite prime products expand by unique factorization with coefficient
one on integers supported on those primes. The missing terms are
bounded by the tail of sum n^(-sigma_0). This proves, before naming
the function, Z_C(s)=sum_(n>=1)n^(-s) on Re s>1.
At real s=1 finite reciprocal products dominate the harmonic partial
sums; their logarithms are unbounded. Termwise comparison gives
absolute divergence for 0<Re s<=1, and a single prime's repetition
sum suffices for Re s<=0. The differentiated series has the same
sharp absolute boundary. This is not a claim about all conditional
summation prescriptions or the continued function outside the half-plane.

**Differentiation and continuation.** Differentiating exp(-srT)/r
cancels r and yields primitive length T, not repeated length rT.
Consequently -Z_C'/Z_C is the Laplace transform of the stated measure,
with log p at log(p^r). These coefficients are outputs, not weights
inserted into the source or evolution. The established half-plane
identity permits the classical scalar continuation cited above.
It supplies neither a global single-valued logarithm nor new information
about zero locations, spectra, traces or Hilbert–Pólya realizations.

**Controls.** OFF uses every n>=2; ON has the empty product 1;
SHIFTED uses n>=2 with n+1 prime, never n=1. All products and
their differentiated series converge absolutely on Re s>1.
At log 4, OFF and SHIFTED have mass log 2+log 4, while the main
owner has log 2. SHIFTED is missing the log 3 atom; ON has none.
Distinct packets at coincident times are added, not identified.

The scalar Z coefficient at 6^(-s) need not represent a single
closed orbit: in the main owner it comes from the independent 2 and
3 factors, while its logarithmic series has no 6^(-s) term.
Thus the Dirichlet comparison does not invent a primitive log 6 packet.

## 3. Checkpoint 2 — manuscript comparison and small correction

The full initial manuscript matches these conclusions and correctly
derives the sharp boundary without a finite prime sample. Its control
and Haar-null comparisons preserve the separate owners and measures.
No missing operator is silently supplied by naming the scalar zeta.

One minor proof-explication request concerned Section 5: differing
positive measures should not alone be asserted to have different analytic
functions without a uniqueness argument. The initial first-term statement
was valid; the author added the recommended explicit bound. If m_0 is
the first nonzero coefficient of an absolutely convergent Dirichlet
difference A, then for real sigma>=sigma_0,

    |m_0^sigma A(sigma)-a_(m_0)|
      <= m_0^sigma_0 [m_0/(m_0+1)]^(sigma-sigma_0)
         sum_(m>m_0)|a_m|m^(-sigma_0) -> 0.

Targeted readback confirms this estimate and the first differences
4, 3 and 2 for OFF, SHIFTED and ON versus the main logarithmic
derivative. Their Z functions cannot coincide if their -Z'/Z differ.
The request is closed at the final bound hash. No extra control
continuation or sharp-boundary theorem was required or added.

## 4. Checkpoint 3 — strongest adverse interpretation and verdict

An engineered complete prime-period ledger makes this Euler identity an
expected scalar consequence. It does not make witness selection,
completion or Haar measure uniquely natural, or explain zeta zeros.
The final paper states that limitation while retaining the exact result.

The returning source set is Haar-null, so its indicator gives the zero
multiplication operator on full Haar L². Positive orbit-counting mass
is consistent because it is a different measure. Neither that observation
nor non-Hausdorffness proves a universal obstruction to distributional,
transverse or other properly specified analytic constructions.

**Verdict: no outstanding blocking issue or requested correction.**
Advance only the ordinary scalar T3 layer of unchanged APR01. Naturalness
remains OPEN; operator/domain/Fredholm/trace data are NOT SUPPLIED.
No RH, zero-location, classical A0/A1/A2 or formal Route result follows.
Coordinates remain UNASSIGNED; Route B NOT INVOKED. No numerical run,
owner repair, deleted locus, new architecture or old-file edit occurred.
