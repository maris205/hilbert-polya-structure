# Independent hostile review A — P147

**Manuscript:** *Adjacent-Run Consolidation of Integer Compositions: A Sharp
Logarithmic Clock and Divisor-Path Fibres*  
**Reviewer role:** independent; the reviewer did not author this package.  
**External status:** `HOLD_EXTERNAL`.  
**Verdict:** **REVISE** — 0 Critical, 1 Major, 3 Minor findings.

The theorem package appears mathematically correct after independent
re-derivation, and no direct primary owner was found in the bounded hostile
search.  The revision verdict is driven by the proof standard for the central
clock lemma, not by a detected counterexample.  The current PDF and exact
transcript are reproducible.

## 1. Theorem-interface audit

| interface | independent conclusion | evidence / edge cases attacked |
|---|---|---|
| self-map, weight, fixed set, termination | **PASS** | Every output part is the sum of one maximal constant run, so total weight is preserved.  Off the adjacent-unequal set, at least one run has length at least two and the number of parts decreases strictly.  This also excludes nontrivial cycles.  The cases \(n=1\) and a one-part composition are consistent. |
| pointwise upper bound \(\tau(\alpha)\le\lfloor\log_2n\rfloor\) | **PASS MATHEMATICALLY / PROOF REPAIR REQUIRED** | A state-indexed backward selector does exist: from a run collapsed at level \(j+1\), two equal adjacent inputs cannot both be unchanged singleton outputs of level \(j-1\); hence one is a nontrivial level-\(j\) output.  Recursing yields a weight-doubling chain.  Lines 117--130 only state this recursion informally and do not actually define the selector across all levels. |
| sharp every-\(n\) witness | **PASS** | \(C_t=(1,1,2,\ldots,2^{t-1})\) has depth \(t\).  Appending \(r\ne2^{t-1}\) cannot meet the unchanged right boundary before the last cascade; prepending \(r=2^{t-1}\) creates the final triple.  Direct checks covered \(n=1,2,3\), powers of two, both remainder branches, and every \(1\le n\le10{,}000\). |
| length-refined one-step fibre | **PASS, SUBJECT TO TYPE REPAIR** | A predecessor run producing \(b_i\) is uniquely \(s_i^{b_i/s_i}\) with positive \(s_i\mid b_i\); maximality is exactly \(s_i\ne s_{i+1}\).  Expansion is the inverse construction, and the exponent is the source length.  Tests such as \(\Phi_{(2)}=u+u^2\), \(\Phi_{(1,1)}=0\), and \(\Phi_{(2,2)}=2u^3\) agree with the literal map. |
| Carlitz generating function | **PASS / ZERO CREDIT** | The last-part equations \(C_j=x^j(C-C_j)\) give the displayed OGF when the empty composition is included.  The manuscript correctly assigns this fixed-class result no contribution credit. |

## 2. Findings and required repairs

### A1 — Major: the doubling-ancestry selector is asserted rather than formally constructed

The entire upper bound rests on Lemma 2.  Lines 117--122 establish the local
fact that, among two equal adjacent inputs to a later collapse, at least one
must have been created by a nontrivial preceding collapse.  Lines 124--130
then say “apply the same observation backwards” and introduce
\(w_{j-1}\), but they never define the orbit states, the generation indices,
or the recursive choice that guarantees one selected part at every earlier
level.  The proof also does not separately dispatch \(t=0\), for which there
is no “last update.”  The intended argument is sound, but this compression is
too large for the lemma carrying the main sharp upper bound.

**Required repair.**  Write \(\alpha^{(j)}=A_n^j(\alpha)\),
\(0\le j\le t\), handle \(t=0\) explicitly, and prove a one-step ancestry
claim: if a nontrivial run of \(\alpha^{(j)}\) is collapsed, then one of a
chosen adjacent equal pair in that run is the output of a nontrivial run of
\(\alpha^{(j-1)}\).  Recursively select parts
\(w_1,\ldots,w_t\) and state precisely that the run producing \(w_j\) has at
least two inputs, each equal to \(w_{j-1}\), so
\(w_j\ge2w_{j-1}\), with \(w_1\ge2\).  Conclude
\(2^t\le w_t\le n\).  A genealogical contiguous-block formulation is an
equally acceptable repair.

### A2 — Minor: the target domain is implicit, and the unrestricted reading is false

Theorem 1 begins with fixed \(n\), then states “for every target \(\beta\)”
at line 87 without writing \(\beta\in\operatorname{Comp}(n)\).  The intended
codomain reading is evident, but the displayed identity is false if “target”
means an arbitrary positive tuple: for fixed \(n=2\) and \(\beta=(1)\),
\(\Phi_\beta(u)=u\), whereas \(A_2^{-1}(\beta)=\varnothing\).

**Required repair.**  Declare \(\beta\in\operatorname{Comp}(n)\) both when
\(\Phi_\beta\) is introduced and in Theorem 1(3).  Alternatively formulate
the inverse globally as a statement about \(A_{|\beta|}\).  State that all
divisors \(s_i\) are positive.  Align the verifier documentation with that
typing decision.

### A3 — Minor: the every-size witness deserves an explicit orbit formula

Lines 155--159 give correct separation observations, but the all-\(n\) lower
bound is closed by prose rather than an indexed orbit.  In particular, the
phrase about a prepended remainder “remaining separate” needs a distinct
\(t=1\) interpretation because \(W_3=(1,1,1)\) begins as one triple run.

**Required repair.**  Display the states of \(A_n^j(W_n)\) for
\(0\le j<t\) in the appended branch, and the corresponding prepended states
ending in \((r,r,r)\) in the half-remainder branch.  Give \(n=1\) and
\(t=1\) as explicit base cases.  This is a short presentation repair; the
construction itself survived exhaustive and extended testing.

### A4 — Minor: the owner ledger is directionally correct but not current or source-precise enough

The existing subtraction correctly removes Carlitz enumeration, equal-run
statistics, locally restricted compositions, and ordinary run-length
encoding.  No screened primary source states the residual clock-plus-fibre
conjunction.  However:

1. `SOURCE_VERIFICATION.md` calls the UCSD `~ebender` copy of Knopfmacher--
   Prodinger “author-hosted,” although neither named author is the host.  The
   direct publisher record and missing DOI are available:
   [10.1006/eujc.1998.0216](https://doi.org/10.1006/eujc.1998.0216).
2. The dated 2026-09-01 audit omits David Bevan and Dan Threlfall,
   [*On the evolution of random integer compositions*](https://doi.org/10.37236/13010),
   EJC 32(1) (2025), P1.21.  That paper studies a different random weak-
   composition growth process, but it explicitly treats equal runs and the
   disappearance of adjacent equality; it is the nearest recent
   “evolution” terminology collision and must be subtracted.
3. It also omits the then-available primary preprint by Brian Hopkins and
   Aram Tangboonduangjit,
   [*Arndt and Carlitz Compositions*](https://arxiv.org/abs/2512.12354)
   (subsequently DOI 10.1016/j.tcs.2026.116156).  This is static and does not
   own ARC, but it is a current adjacent-restriction neighbour.
4. Literal web queries also expose non-archival coding-problem formulations
   of repeatedly summing consecutive equal entries.  They are not acceptable
   primary owners and their digit semantics may differ, but they reinforce
   that the literal rule alone should be treated as folklore-risk.  The
   paper-sized residual should be scored on the proved clock-plus-inverse
   package.

**Required repair.**  Correct the host description, add the 1998 DOI, screen
and record the two recent primary neighbours with explicit different-object
subtraction, and keep the conclusion at “bounded non-hit,” not novelty or
priority.  No direct-owner kill is warranted on the inspected evidence.

## 3. Exact verifier and artifact audit

- Cold command:
  `PYTHONDONTWRITEBYTECODE=1 python3 verify_p147.py`.
- Frozen-output comparison: byte-identical; exit status 0.
- Reported coverage: all 262,143 positive compositions of totals 1 through
  18, all targets in each corresponding layer, and 2,690,869 assertions.
- Arithmetic: integer-only standard-library computation; no seed, tolerance,
  network, or external dependency.
- Literal carrier, map, orbit, and incoming-fibre enumeration are separate
  from the Carlitz DP and divisor-path DP to a reasonable falsification
  standard.  Enumeration is correctly described as pressure rather than
  proof.
- Extended witness replay for every \(1\le n\le10{,}000\) found no failure.
- An isolated source-only `pdflatex -> bibtex -> pdflatex -> pdflatex` build
  reproduced the frozen PDF byte for byte.
- Current and round-0 PDF SHA-256:
  `c21bc9029f7dd697a623f489d446fcfa9329bd96f1bb6ea34e9c363a545a6aa3`.
- PDF: 3 A4 pages, 330,830 bytes, blank identifying metadata, embedded fonts;
  no unresolved citation/reference or bad-box warning.  All pages were
  independently rasterized and visually inspected without clipping or glyph
  corruption.

No verifier or artifact repair is required beyond documenting the target
typing change in A2.

## 4. Decision gate

There is no Critical defect: the literal theorem interfaces survived
re-derivation and exact pressure, the build is reproducible, and no direct
primary owner was found.  P147 should remain internal and under
`HOLD_EXTERNAL`, but it should not advance to review B until A1 is formalized
and A2--A4 are closed.  The permitted residual remains exactly the
simultaneous weight-preserving iteration together with the sharp all-size
clock and complete length-refined divisor-path inverse; all static Carlitz
and run-statistic material remains zero credit.
