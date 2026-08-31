# Hostile Review A — rootward active-pile coalescence

Review date: 2026-08-31 UTC  
Role: independent nonauthor, round-zero review  
External status: **HOLD**

## Provisional verdict

**GO_IF_REPAIRED for another internal review; HOLD_EXTERNAL.**

I found no counterexample to the finite-law recursion, the interval-support
theorem, the interface-additive mean, the adjacent closed form, the
full-start asymptotic, or the minimum-time mass.  Fresh exact control and a
separate labelled-flow state search also passed.  The present draft is not
yet ready to advance, however, for two substantive reasons:

1. the only displayed justification of the central finite ballot sum is the
   assertion that Pascal's identity gives the recurrence in (15); the
   necessary boundary/telescoping algebra is absent; and
2. the owner boundary omits three close primary neighbors, including a 2026
   paper on exact coalescence patterns.  The generic graphical-flow,
   interval-label, and active-count/jump-current machinery must be credited
   explicitly and assigned zero contribution credit.

Severity count: **CRITICAL 0; MAJOR (mathematics) 1; MAJOR
(owner/scope) 1; MINOR 4.**

## Independent reconstruction of the theorem package

### 1. Literal chain, absorption, and complete-law recursion

For a finite rooted state $S\subseteq\mathbb N_0$, $0\in S$, an effective
step chooses $v\in S\setminus\{0\}$ uniformly and replaces $v$ by
$v-1$, with set union implementing coalescence.  If

\[
  \Phi(S)=\sum_{v\in S}v,
\]

then an unblocked move lowers \(\Phi\) by one, while a collision at $v-1$
removes $v$ and lowers it by $v$.  Thus every step lowers a nonnegative
integer potential, and conditioning on the first selected pile gives

\[
 G_{\{0\}}(z)=1,\qquad
 G_S(z)=\frac{z}{|S|-1}\sum_{v\in S\setminus\{0\}}G_{C_v(S)}(z).
\]

This is an acyclic exact recursion.  I found no missing state or boundary
case here; $S=\{0\}$ is explicitly absorbing.

### 2. Support is one complete interval

The deterministic bounds are correct: a move lowers the current maximum by
at most one, whereas it lowers \(\Phi\) by at least one, so

\[
 \max S\le T_S\le \Phi(S).
\]

The induction also closes for arbitrary sparse $S$.  Writing $m=\max S$:

- if $m-1\notin S$, moving $m$ first reduces both the maximum and
  potential by one and supplies all of $[m,\Phi(S)]$;
- if $m-1\in S$, moving $m$ first supplies
  $[m,\Phi(S)-m+1]$; moving the bottom $a$ of the occupied run ending at
  $m$ supplies $[m+1,\Phi(S)]$.  This second move lowers the potential by
  exactly one whether $a=1$ (collision with the root) or $a>1$
  (unoccupied predecessor), and it leaves the maximum at $m$.  Since
  $m,m-1\in S$ implies \(\Phi(S)\ge 2m-1\), the two integer intervals touch.

The separate $m=1$ boundary is present.  Every prescribed finite schedule
has positive probability, so the constructive support argument is valid,
not merely a reachability statement with zero-probability paths.

### 3. Site-Poisson embedding and the active-pile scheduler

The continuous-time construction is the correct embedding of the literal
discrete chain.  At a state with $k$ positive occupied sites, the residual
times at precisely those sites are independent rate-one exponentials.  The
next effective site is therefore uniform and its holding time has rate $k$.
Rings at empty sites are lazy events and do not enter the embedded chain.

There is one precision issue, listed below as MINOR-1: because the prose puts
clocks at every positive integer, it should explicitly restrict the relevant
clock vector to the finite accessible set

\[
 \{1,\ldots,\max S\},
\]

and invoke the strong Markov/memoryless property at each effective stopping
time.  This matters especially when a pile newly occupies a site whose clock
has rung previously while empty.  The claim is correct after that sentence;
the current informal minimum-of-$k$-exponentials statement is not by itself
the full stopping-time argument.

### 4. Labels, indirect mergers, and the interface identity

The pathwise identity survives indirect coalescences.  In the site-arrow
picture, assign initial labels $0,1,\ldots,r$ in spatial order.  The
invariant that needs to be stated explicitly is:

> every current pile carries a nonempty interval of initial labels, and the
> left-to-right pile order is the order of those intervals.

Initially this is immediate.  Moving a pile to an empty predecessor
preserves the invariant.  If the predecessor is occupied, nearest-neighbor
order implies that the two merging label intervals are consecutive, so their
union is again an interval.  Hence this remains true even after either member
of a designated adjacent pair has already merged with labels outside that
pair.  It follows that the interface between labels $i-1$ and $i$ is open
exactly until their two graphical paths meet, and therefore

\[
 N_t=\sum_{i=1}^{r}{\bf1}_{\{\tau_i>t\}}.
\]

No independence among the \(\tau_i\) is needed or claimed.  I independently
enumerated all reachable labelled configurations from every rooted initial
set through ambient size eight.  The interval-label invariant, label order,
the displayed interface count, and potential descent passed on 26,232
labelled states and 70,056 labelled transitions (149,254 reviewer-side
assertions).  This is strong falsification evidence, not a replacement for
the two-line induction requested in MINOR-2.

### 5. Compensator, Tonelli, and discrete update count

Let $J_t$ be the number of effective rings by time $t$.  Its predictable
intensity is $N_{t-}$, so for finite $t$,

\[
 \mathbb E J_t=\mathbb E\int_0^tN_{u-}\,du.
\]

The manuscript writes $N_u$.  The two integrals agree because jump times
are Lebesgue-null, but the martingale statement should use the predictable
version.  Since $J_\infty\le\Phi(S)$, monotone convergence can be applied on
both sides after first proving the finite-time identity.  Nonnegativity then
justifies Tonelli, giving

\[
 \mathbb E T_S
 =\sum_i\mathbb E\tau_i.
\]

Absorption in continuous time is also harmless: at most \(\Phi(S)\)
effective waits occur and every nonabsorbed effective rate is at least one.
Thus the compensator route is mathematically sound after the predictable-
intensity repair in MINOR-3.

For one adjacent interface at $0<a<b$, its two distinct paths read
independent site clocks until meeting.  The next relevant event has mean
$1/2$ and chooses either path with probability $1/2$.  At $a=0$, only
the upper path moves.  First-event conditioning therefore gives exactly

\[
 h(a,a)=0,\qquad h(0,b)=b,\qquad
 h(a,b)=\frac12+\frac{h(a-1,b)+h(a,b-1)}2,
\]

and the arbitrary-state formula

\[
 \mathbb E T_S=\sum_i h(s_{i-1},s_i).
\]

The presence of a third path does not change this marginal: a graphical path
follows the same future site arrows after an outside label joins its pile.

### 6. Adjacent ballot formula and full-start asymptotic

The stopped event-word decomposition is correctly indexed.  With
$p=m-1$, meeting after $j$ lower moves and $j+1$ upper moves has Catalan
multiplicity

\[
 A_j=\frac1{j+1}\binom{2j}{j},\qquad 0\le j<p,
\]

while the lower path making its $p$-th move after $q<p$ upper moves has
ballot multiplicity

\[
 B_{p,q}=\binom{p+q-1}{q}-\binom{p+q-1}{q-1}.
\]

The probability denominators, mean $1/2$ per two-clock event, and residual
upper-path distance $p+1-q$ in (14) are all correct.  Exact rational checks
through $m=80$ agree with the claimed double-factorial ratio.

What is not yet a proof is the next sentence: substituting the ballot form
and saying that Pascal's identity gives

\[
 R_1=1,\qquad 2mR_{m+1}=(2m+1)R_m
\]

suppresses the nontrivial cancellation of two finite sums with moving upper
limits and their $q=0,q=p-1$ boundary terms.  Since this is the only
all-$m$ evaluation underlying the displayed closed form, the omission is a
MAJOR mathematical gap, not a stylistic request.  A repair may either show
the summand-level telescoping and both boundary cancellations explicitly, or
replace it with a complete independent derivation of
$h(m-1,m)=\mathbb E|W_{2m}|$.  A finite verifier cannot promote the current
one-sentence reduction to a theorem.

Conditional on that repair, the rest is correct:

\[
 h(m-1,m)=\frac{(2m-1)!!}{(2m-2)!!}
          =\frac{2m}{4^m}\binom{2m}{m},
\]

and summing consecutive interfaces from the full state gives the stated
mean.  The central-binomial estimate makes the $m$-th term
$2\sqrt{m/\pi}+O(m^{-1/2})$, whence

\[
 \mathbb E T_n=\frac{4}{3\sqrt\pi}n^{3/2}+O(n^{1/2}).
\]

### 7. Minimum-time mass

For full occupancy, $n-1$ effective steps are possible only if every step
reduces the number of nonroot piles, hence only if every step collides.
Removing a site before its right neighbor creates a hole and prevents that
neighbor's next move from colliding.  Thus the unique minimum schedule is
$n-1,n-2,\ldots,1$.  Its successive selection probabilities multiply to

\[
 \frac1{n-1}\frac1{n-2}\cdots\frac11=\frac1{(n-1)!}.
\]

This includes $n=2$; $n=1$ is separately absorbed and is not included in
the corollary.

### 8. PILOT_ONLY containment

The maximum-endpoint experiment has not leaked into the theorem contract.
Its formula occurs only in the verifier; canonical stdout calls it
`PILOT_ONLY ... MANUSCRIPT_CLAIM=NO`.  The manuscript merely records that an
unnamed pattern was excluded, and neither the abstract nor the contribution
paragraph states the formula.  This control passes.  The segregation must be
preserved in any repair.

## Severity-ranked issues

### CRITICAL

None found.

### MAJOR (mathematics)

**MATH-1 — Equation (14) does not presently imply (15) on the page.**
Supply the complete all-$m$ finite-sum calculation, including the moving
upper limit and the $q=0,p-1$ boundary terms, or a genuinely complete
alternative proof of the adjacent formula.  Retaining “Pascal's identity
gives” without the algebra is not sufficient for re-entry.

### MAJOR (owner/scope)

**OWNER-1 — The subtraction boundary omits direct modern neighbors and is
currently too broad.**  The following primary sources must be read, cited,
and assigned explicit zero credit:

- Theodoros Assiotis, *Random surface growth and Karlin--McGregor
  polynomials* (2018), [DOI 10.1214/18-EJP236](https://doi.org/10.1214/18-EJP236),
  especially its graphical construction of a discrete coalescing flow for
  birth-and-death chains.  This owns the general site-arrow/coalescing-flow
  technology used in the manuscript.
- Paweł Hitczenko and Jacek Wesołowski, *Expected Number of Jumps and the
  Number of Active Particles in TASEP* (2025),
  [DOI 10.1007/s10955-025-03483-0](https://doi.org/10.1007/s10955-025-03483-0).
  Their Theorem 3 formalizes, in TASEP, the expected jump-current/active-count
  derivative.  The model differs, but the generic active-count-to-jump
  bridge cannot be presented as residual contribution.
- Piotr Śniady and Ákos Urbán, *Exact determinant formulas for coalescing
  particle systems*, [arXiv:2602.10782v3](https://arxiv.org/abs/2602.10782)
  (2026).  This treats exact coalescence patterns for nearest-neighbor
  systems, including birth-death chains, with active interval labels and
  explicit coalescing constructions.  Coalescence-pattern, ordered-interval,
  and survivor-position machinery are therefore zero-credit background.

After subtraction, the admissible residual is narrower than “general
interface-additive jump count”: it is the exact arbitrary-initial-state
expected **embedded update count for this specified deterministic rootward,
uniform-active-pile finite chain**, together with the support and full-start
consequences proved from that identity.  The sources above do not state that
conjunction in the bounded search I performed, but the non-hit is only
bounded evidence and is not a novelty or priority claim.

The internal firewall also needs a literal correction.  P117 is the
odd-run-reversal map on labelled cyclic binary words, not a paper whose
carrier is “pointer doubling.”  State the actual P117 carrier and its
boundary-parity eroder, then explain the absence of overlap.  For P121,
record the decisive distinctions rather than only naming “adjacent
coalescence”: P121 selects a current adjacent separator and follows a
BST/Yule history, whereas P129 selects a current pile, permits noncoalescing
rootward moves, and counts its embedded effective updates.  P114 synchronous
forest-leaf peeling and P126 synchronous length-increasing composition
refinement are genuinely different, but their root/peeling and
split/coalescence backgrounds remain zero credit.

### MINOR

**MINOR-1 — Site-clock stopping-time precision.**  Restrict the graphical
construction to the finite accessible sites $1,\ldots,\max S$, and invoke
the vector-Poisson strong Markov property at each effective jump.  This
closes the newly-occupied-site case.

**MINOR-2 — The indirect-merge invariant is asserted rather than proved.**
Insert the short induction that every pile carries a consecutive interval of
initial labels, that a collision merges adjacent intervals, and that this
gives the “if and only if” between a closed initial interface and common
current pile.  Also state explicitly that adding an outside label does not
alter either graphical path's future arrows.

**MINOR-3 — Use the predictable intensity.**  Write $N_{u-}$ in the
compensated martingale, establish the expectation identity first on finite
time intervals, and then take $t\to\infty$ by monotone convergence.  It is
fine to replace $N_{u-}$ by $N_u$ only after observing equality of their
Lebesgue integrals.

**MINOR-4 — Evidence ranges disagree.**  `CLAIMS_EVIDENCE.md` says that the
Bellman/interface comparison was made through `n=16`, and `PAPER_PLAN.md`
still advertises rooted checks through `n=12` and transition/mean checks
through `n=16`.  The actual verifier, canonical transcript,
`CONTROL_RESULTS.md`, and manuscript say rooted mean/interface through
`n=14` and complete distributions through `n=11`.  Make every support file
state the executed ranges exactly.

## Owner search log and subtraction result

Search date: 2026-08-31.  I used multiple literal formulations, including
`coalescing birth death chain graphical construction site Poisson arrows`,
`expected number jumps active particles interacting particle process`,
`coalescing particle interval labels exact determinant birth-death 2026`,
`deterministic left coalescing walks total jumps interface sum`, `rootward
pure-death coalescing embedded jump count arbitrary initial set`, and
`uniform active pile coalescence support hitting-time law`.  I followed
primary journal, DOI, and arXiv pages rather than aggregator summaries.

The three direct neighbors above are real subtraction obligations.  The
existing Cox, Cooper--Elsässer--Ono--Radzik, Benjamini et al.,
Kanade--Mallmann-Trenn--Sauerwald, and Ermakov citations remain useful broad
background, but they do not replace the more literal flow/current/2026
pattern sources.  I found no primary source in this bounded search stating
the P129 arbitrary-rooted embedded-update formula, its complete support
interval, and its full-start double-factorial mean as one literal theorem
package.  This is **not** a novelty certificate; external release remains
HOLD.

## Fresh exact control

The paper-local verifier was rerun without bytecode output:

```bash
fresh=$(mktemp /tmp/p129-reviewA-verify-XXXXXX)
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py > "$fresh"
cmp "$fresh" code/verification_output.txt
sha256sum "$fresh" code/verification_output.txt
```

Result: byte-for-byte match and PASS, with **506,663 assertions**.  The
transcript records 16,383 rooted states and 98,305 transitions through
`n=14`, complete laws for 2,047 rooted states through `n=11`, the pair
triangle through 80, the independent adjacent ballot sum through 80, and
full-start laws through `n=11`.  Fresh and canonical stdout both have SHA-256
`3e40359274ae4bb033db5efe16d463b28af3fcd7464f9589bc5b136626acd080`.

As an independent control, a temporary standard-library enumeration (no
repository artifact) reconstructed labelled graphical states and all
reachable transitions through ambient size eight.  It passed 149,254
assertions on 26,232 labelled states and 70,056 transitions, including the
indirect-merge/interface invariant.  These controls did not participate in
the proof verdict.

## Isolated build and visual audit

I copied only `main.tex`, `math_commands.tex`, `references.bib`, and
`sections/` into `/tmp/p129-reviewA-build-8Wisdn` and ran:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The isolated PDF is byte-identical to both `main.pdf` and
`main_round0_original.pdf`.  It has 5 pages, 330,389 bytes, and SHA-256
`404b21a8beb9f9691326262544fc797cd1b62bf69b36ad2b5b65f693495dc05d`.
The settled log and BLG contain no warning, undefined citation/reference,
multiply-defined label, or over/underfull-box report; all 5 cited entries are
present in the BBL.  `pdfinfo` reports A4, rotation zero, no encryption,
forms, JavaScript, custom metadata, author, title, subject, or keywords.
Every reported font is embedded, subset Type 1 with Unicode mapping.

All five pages were rendered and inspected.  Equations (1)--(17), theorem
heads, page breaks, bibliography, and the code/control paragraph are legible;
there is no clipping, collision, orphan heading, or visibly bad spacing.  A
PDF text scan finds the word `PILOT_ONLY` only in the explicit exclusion on
page 4 and finds no pilot formula.

## Reviewed hashes

```text
main.tex                  6f187199a00764f23faf40cf8efec56dfb989cdf4771ee5a3316f7b631d111dd
math_commands.tex         4994d5e68b4c06585fe2fc358808303a02621b6ee6ffae1af0e609cbb9632b6d
references.bib            0685bf33c6f6541b8c87a3cf334b851a79a52cbbfff779b9be94a0ac8f1b09dd
sections/0_abstract.tex   e0f736febc69ac58028c69be0a9abdae2f4041fd5f949022fc77eb9bcc36b2f6
sections/1_model.tex      d39a52443ebc30593ec9ce1cd20a37a3a85fa94590711136e2a38e6c31efdcad
sections/2_finite_law.tex f92e80a450164d4903f8c512e1d8d7d303e86cb2801793e9c1c13882e0f3fdd4
sections/3_interfaces.tex 261664cd792fdeb2877faf1cb484638c3ae7f8cb8ad0eddfb563b46beaeb1ff7
sections/4_ballot.tex      14758b82dca16b25d9d1c247fe28a8a55e699a56c6fd0248cdfdf203a2e7655e
sections/5_control.tex     7f5098942961c3bc4c33bb4ae148607ce935f29d359c2a7a90413d5c01d97ce9
sections/6_conclusion.tex  f7c4d27247bec422cc7c8d5ee2a09707ab51e941ae57e4452e598d2c5b9ffc77
code/verify.py            fe79e8e3dfa1d15b16d04138d39ef653ac45bbd6addea50d3b53adf34f5aa272
canonical stdout          3e40359274ae4bb033db5efe16d463b28af3fcd7464f9589bc5b136626acd080
main.pdf                  404b21a8beb9f9691326262544fc797cd1b62bf69b36ad2b5b65f693495dc05d
```

## Re-entry conditions

Re-entry requires all of the following:

1. close MATH-1 with visible all-size algebra or a complete alternate proof;
2. add and zero-credit Assiotis (2018), Hitczenko--Wesołowski (2025), and
   Śniady--Urbán (2026), and narrow the residual wording accordingly;
3. formalize the consecutive-label-block invariant and its persistence under
   indirect merges;
4. repair the clock and compensator precision with finite accessible sites,
   strong Markov at effective times, $N_{t-}$, and finite-time-to-limit
   justification;
5. correct all support-document control ranges and the literal P117/P121
   firewall; and
6. preserve the current `PILOT_ONLY / MANUSCRIPT_CLAIM=NO` boundary, then
   rerun the canonical verifier, isolated four-stage build, warning scan, and
   visual audit.

Until those repairs are present, the manuscript remains **HOLD_EXTERNAL**.
