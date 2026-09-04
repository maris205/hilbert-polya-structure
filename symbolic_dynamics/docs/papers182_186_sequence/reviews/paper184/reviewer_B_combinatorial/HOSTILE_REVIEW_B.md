# Hostile Review B — P184, co-gcd translation on prime powers

**Reviewer lane:** combinatorial; process-separated from the author and Review A  
**Reviewed object:** immutable Round 1  
**Review date:** 2026-09-03  
**Decision:** `ACCEPT_ROUND1_FOR_COORDINATOR_GATE`  
**External lifecycle:** `HOLD_EXTERNAL`

## Bottom line

The frozen P184 Round-1 package survives Review B with **zero Critical, zero
Major, and zero Minor findings**.  The pointwise tail and eventual-period
formulas, cycle and depth populations, sharp tail extrema, every-target
predecessor atlas, empty/double target parametrizations, fibre cap, and image
defect all survive a line-by-line proof attack and a digit-level exact audit.
No paper-directory file was edited and no repair is requested.

This is a process-separated review, not a claim that its possible errors are
independent of the author's or Review A's errors.  The three processes share
the frozen theorem specification and standard number-theoretic identities.
Review B changes the state representation, transition implementation,
functional-graph classification, and inverse construction.

## Exact Round-1 binding

| Object | SHA-256 | Result |
|---|---|---|
| `main.tex` | `6f11630dfbb68ff3ac30e652130497b3c473a45869c968fb0679136ba2b8b44a` | exact required binding |
| `main_round1.pdf` | `991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab` | exact required binding |
| `main.pdf` | `991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab` | byte-identical |
| `main_round0_original.pdf` | `991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab` | byte-identical |
| `references.bib` | `3c1b98b55d0e6a6215f88e3182173254974b158ba34a0f744be3bf0c12769b66` | frozen and resolved |
| author verifier | `7636127ed7eb4693aa5adb1dd7d68406b21d776299da7b7a64b71b866dbbe653` | bound, not executed by Review B |
| author canonical | `616f48c16bc1d335c658bcfded8b0b004b5dafdec79b77cb17a333ce3067acda` | bound and parsed |

The 19-row author manifest validates and excludes itself.  The Round-1 PDF is
a byte-identical promotion of the author baseline, so the control documents'
Round-0 labels are not a conflicting content claim.  Review B directly binds
the later `main_round1.pdf`.  The PDF is four pages, 353,576 bytes,
unencrypted, and its extracted text contains the same prime/exponent scope,
109,478-author-assertion receipt, disclosures, and `HOLD_EXTERNAL` status as
the source.

Terminal re-signing note: the original `main.tex`, Round-1 PDF, and
mathematical attack are unchanged; this re-signing only rebinds the terminal
19-row paper manifest.  Its four added lifecycle rows (`IMPROVEMENT_LOG.md`,
`FINAL_QA.md`, `main_round1.pdf`, and `main_round2.pdf`) remain hard-fail
checks but are excluded from the original scientific assertion census.

## Representation and algorithm separation

| Process | State representation | Graph/fibre method |
|---|---|---|
| author | canonical integer residue; transition evaluated with `gcd` | forward orbit tracing and accumulated reverse lists |
| Review A | canonical integer residue split by candidate valuation | modular predecessor congruence solver plus orbit signatures/canonical cycles |
| **Review B** | least-significant-first base-\(p\) digit word | one-position carry update, indegree peeling and reverse BFS, union-find cycle components, and a low/middle/high digit inverse grammar |

Review B does not import or run either earlier verifier.  If the first nonzero
digit of \(x\) is in position \(v\), then
\(N/\gcd(x,N)=p^{a-v}\); the reviewer implements the map by adding one at
digit position \(a-v\) with carry, treating position \(a\) as zero modulo
\(p^a\).  It then checks this digit update against the literal gcd formula at
every state.  Recurrent nodes are obtained by indegree-zero peeling, tails by
reverse breadth-first distance, and cycle multiplicities by union-find on the
peeled recurrent permutation.

## Hostile theorem audit

### 1. Literal map and valuation trichotomy

For nonzero \(x=p^vu\), with \(u\) a unit,

\[
T(x)=p^vu+p^{a-v}\pmod {p^a}.
\]

If \(2v<a\), division by \(p^v\) produces translation by
\(p^{a-2v}\) on unit coordinates modulo \(p^{a-v}\).  This preserves unit
status; for the boundary \(v=0\), the increment is zero modulo \(p^a\).
The additive order is exactly \(p^v\), so every low state is recurrent with
the claimed exact period, not merely a period dividing that number.

If \(2v>a\), factoring yields

\[
p^{a-v}\bigl(1+p^{2v-a}u\bigr).
\]

The parenthesis is congruent to one modulo \(p\), eliminating cancellation;
the image valuation is exactly \(a-v<a/2\).  Low strata are invariant, so the
old high state cannot lie on the reached low cycle and its tail is exactly
one.  The zero state is handled separately: \(0\mapsto1\mapsto1\), agreeing
with the convention \(\nu_p(0)=a\) without applying the nonzero factorization
to zero.

**Result:** all strict low/high cases survive.

### 2. Even-exponent equality conveyor

For \(a=2h\) and \(x=p^hu\), the middle coordinate advances by
\(u\mapsto u+1\pmod {p^h}\).  Since \(u\bmod p\in\{1,\ldots,p-1\}\),
\(r=p-(u\bmod p)\) lies in \(1,\ldots,p-1\) and is the first positive step
at which divisibility by \(p\) occurs.  The landing has valuation \(h+s\),
where \(s=\nu_p(u+r)\), and one further high-to-low step reaches valuation
\(h-s\) with period \(p^{h-s}\).  The middle states, high landing, and low
cycle lie in distinct valuation regimes, proving the exact tail \(r+1\).

The endpoint \(u+r=p^h\) is sound: it lands at zero, sets \(s=h\), and the
next step reaches fixed state one.  For \(p=2\), every middle unit has
\(r=1\), so every middle state has tail two.  The digit audit checks both
boundaries on every applicable carrier.

**Result:** survives, including all advertised binary and zero-landing cases.

### 3. Cycle census, recurrent population, and tail ladder

The exact-valuation-\(v\) stratum contains
\((p-1)p^{a-v-1}\) states.  In a low stratum every cycle has length \(p^v\),
so division gives \((p-1)p^{a-2v-1}\) cycles.  Low states are precisely the
residues not divisible by \(p^{\lceil a/2\rceil}\), leaving recurrent
population \(p^a-p^{\lfloor a/2\rfloor}\).

For \(a=2h+1\), the \(p^h\) high states all have tail one.  For \(a=2h\),
the strict-high region has \(p^{h-1}\) states at depth one; in the middle
stratum each nonzero residue of \(u\bmod p\) occurs \(p^{h-1}\) times, so
every depth \(2,\ldots,p\) has the same population.  The populations exhaust
the carrier and make the maximum tail exactly one for odd \(a\), exactly
\(p\) for even \(a\).

Indegree peeling, reverse distances, and union-find cycle components agree
with these formulas pointwise and in aggregate on every reviewed carrier.

**Result:** survives.

### 4. Every-target fibres, explicit sets, and defect

Every low restriction is a bijection, yielding one low predecessor for every
low target.  A strict-high source of valuation \(a-w\) maps to

\[
p^w\bigl(1+p^{a-2w}u\bigr),
\qquad 1\le u<p^w,\quad p\nmid u.
\]

The target valuation recovers \(w\), and the remaining high digits recover
\(u\), so the high-source map is injective.  Zero supplies the separate
second predecessor of target one.  In digit language, every nontrivial double
target has \(w\) initial zero digits, digit \(w\) equal to one, a forced zero
gap, and a top \(w\)-digit coefficient whose first digit is nonzero.  This is
exactly the manuscript's displayed parametrization, not a looser congruence.

For odd \(a\), only low targets are hit, so the empty set is exactly the high
region.  For even \(a=2h\), a target coordinate \(z\) has a middle predecessor
precisely when \(z-1\) is a unit; failure is exactly \(z\equiv1\pmod p\),
giving the displayed middle-layer empty set.

The geometric count

\[
1+\sum_{1\le w<a/2}(p-1)p^{w-1}
=p^{\lfloor(a-1)/2\rfloor}
\]

handles both parities and the empty-sum boundaries.  The double targets lie
in low strata while empty targets lie in high or middle strata, so the sets
are disjoint.  All other fibres are singletons; consequently the image size
is \(p^a-d\) and the full `0/1/2` histogram is
\((d,p^a-2d,d)\).

Review B constructs the predicted predecessor **set** of every target from
the digit grammar and compares it with reverse adjacency.  Thus it checks
source identities, not only fibre sizes.  It also checks the full histogram,
mass conservation, exact image complement, set disjointness, and both set
cardinalities.

**Result:** survives target by target.

## Quantifier and boundary table

| Scope | Attack | Outcome |
|---|---|---|
| every prime \(p\) | proof uses only prime-power valuation; controls use eight primes through 19 | pass |
| every exponent \(a\ge1\) | parity-complete symbolic argument; 48 carriers with all \(p^a\le30{,}000\) for tested primes | pass |
| \(a=1\) | units fixed, `0 -> 1`, exactly one empty and one double target | pass |
| \(a=2\) | nonempty equality stratum; maximum tail exactly \(p\) | pass |
| \(p=2\) | exponents 1 through 14; every even middle layer has tail two | pass |
| \(x=0\) | separate digit transition to fixed one | pass |
| \(u+r=p^h\) | explicit middle-to-zero-to-one boundary in every even exponent | pass |
| empty double-set sum | \(a=1,2\) yield only special double target one | pass |
| all targets | exact predecessor-set equality on 160,928 targets | pass |

The finite controls include primes 17 and 19, absent from both earlier
control sets, but remain falsification evidence only.  The unrestricted
prime/exponent quantifiers rest on the valuation proof.

## Artifact, source, and owner wording audit

- `main.tex`, Round-1 PDF, proof package, claims ledger, README, build receipt,
  self-QA, author canonical, and author manifest agree on the map, hypotheses,
  boundary conventions, theorem formulas, 109,478 author assertions, and
  `HOLD_EXTERNAL`.
- Every bibliography entry is cited and all three citation keys resolve.
  Xu--Zou studies linear systems over finite rings
  ([primary preprint](https://arxiv.org/abs/0810.3164)); Anashin--Khrennikov is
  broad algebraic and \(p\)-adic dynamics background
  ([publisher record](https://www.degruyterbrill.com/document/doi/10.1515/9783110203011/html));
  Konyagin et al. studies polynomial functional graphs over finite fields
  ([publisher record](https://www.sciencedirect.com/science/article/pii/S0095895615000878)).
  Their metadata and the manuscript's limited background attribution agree;
  none is presented as an owner of the nonlinear co-gcd map.
- The manuscript explicitly limits itself to prime-power moduli and does not
  imply a Chinese-remainder extension.  Generic cyclic arithmetic, valuation
  stratification, and functional-graph bookkeeping receive zero contribution
  credit.
- Internal comparisons with P128/P142/P166 are labelled proof-transfer
  subtraction, not external priority evidence.  The owner search is expressly
  bounded, its non-hit is denied novelty-certificate status, and a future
  literal/equivalent owner is a withdrawal trigger.

**Result:** no source, owner-language, or artifact inconsistency found.

## Exact Review-B receipt

```text
carriers=48
primes=2,3,5,7,11,13,17,19
new_prime_controls=17,19
states=160928
targets=160928
exact_assertions=3987801
review_transition_digest=58f3fe63ee9a7396fdf269909dcbc564ca0854681860d931ec84f574e893b229
```

## Findings ledger

### Critical findings (0)

None.

### Major findings (0)

None.

### Minor findings (0)

None.

## Residual risks, not findings

1. Exact enumeration is bounded at 48 carriers and does not replace the
   all-prime/all-exponent proof.
2. Different representations and algorithms do not make reviewer errors
   independent of author errors.
3. The exact-owner search is still bounded.  Correctness acceptance does not
   upgrade `OWNER_AMBER` or release `HOLD_EXTERNAL`.

## Reproduction

From the repository root:

```bash
python3 docs/papers182_186_sequence/reviews/paper184/reviewer_B_combinatorial/verify_review_b.py
```

Acceptance requires exit code zero and stdout byte-identical to
`CANONICAL.txt`.  Two fresh processes satisfied this condition before sealing.
