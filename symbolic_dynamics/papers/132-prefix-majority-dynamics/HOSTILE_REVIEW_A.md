# Round-A hostile review: synchronous prefix-majority dynamics

**Review date:** 2026-08-31  
**Reviewer posture:** independent internal reviewer; not an author of this manuscript  
**External status:** `HOLD_EXTERNAL`

## Verdict

**`GO_INTERNAL_AFTER_MINOR_REPAIR`**

The all-length mathematical spine survives adversarial reconstruction.  In
particular, I found no counterexample or missing implication in the fixed-word
classification, the sharp stabilization clock, the target-wise fibre formula,
the Fibonacci image count, or the unique maximum-fibre theorem.  The finite
computation is appropriately presented as falsification rather than proof.

The present source is nevertheless not mechanically release-ready.  Two
displayed formulas are visibly malformed, and the abstract's claim to
"complete finite dynamics" is broader than the atlas actually proved.  These
are mandatory but local repairs; they do not require a new theorem.

**Severity count:** critical 0; major mathematical 0; major scope 0; mandatory
minor 4.

## Frozen evidence and reproducibility check

I audited the manuscript, bibliography, support documents, verifier, frozen
stdout, current PDF, and frozen round-0 PDF.

- `main.tex`: `b328469ecce4adeea2dc894a47716562f3122a1985decc496e913575619b4e6f`
- `references.bib`: `37af8e3aec5558199966d428bcd4a136dc3612da82318c9d7221c57df280313a`
- `code/verify.py`: `50ff5f13d47c01b679a9158f79ce5aa20333f43c374d133c31ff46712882604d`
- frozen stdout: `f52d769cd0831772458e700db189722bf745b8e74c4aca2c3539dcfea8a0f442`
- current `main.pdf`: `73e9721a3c25e206838f4031cb75d04c9e5d2eb935ed90664b386f6438e48d65`
- `main_round0_original.pdf`: `f6329905059f20811380dcfe1163d9cd908a592e428a358ec1f9461d55140679`

A fresh replay of the paper-local verifier reproduced the frozen stdout byte
for byte (`cmp=0`).  It reports 131,070 exhausted states, 131,070 target cells,
ten larger witnesses through length 511, 524,452 exact-integer assertions, and
`STATUS=PASS`.

The current PDF is not byte-identical to round 0.  Text extraction and a
linewise comparison locate the only visible change in the bibliography:
round 0 misparsed the second cited author's name, while the current PDF prints
"Gilbert Agnew Hunt, Jr." correctly.  The mathematical body, including the
three source defects listed below, is unchanged.  This distinction should be
recorded rather than silently treating the two PDFs as one frozen artifact.

## Mathematical attack

### 1. Closure, fixed language, and recurrence

The update is a genuine self-map of `\{0,1\}^n`.  Rewriting letters as
increments `x_i=2w_i-1` correctly makes each output coordinate the weak sign
of the corresponding prefix sum.

The fixed-word proof closes.  At balances at least one, a zero cannot be a
fixed next report; at balances at most minus two, a one cannot be.  The only
nonconstant continuation is the two-step return
`0 -> -1 -> 0`, yielding the two alternating--constant families.  Their
stated parameter ranges are disjoint and contain exactly `n+1` words.  Once
the typographical commas in the exponents are removed, the theorem statement
matches its proof.

Since the later clock proof forces every orbit into this language, the
conclusion that all recurrent points are fixed, and hence that the dynamical
zeta function is `(1-z)^{-(n+1)}`, follows without relying on enumeration.

### 2. Sharp clock

The fixed-prefix amplifier is sufficient for the claimed upper bound.  If the
maximal fixed prefix ends in a one-tail of length `ell`, one update protects
at least another `ell` positions.  On the zero branch a one-letter tail cannot
be maximal, so `ell>=2`, and one update protects at least another `ell-1`
positions.  Thus the recurrences

```text
one branch:  ell_t >= 2^t ell_0,
zero branch: ell_t - 1 >= 2^t(ell_0 - 1)
```

force stabilization by `ceil(log_2 n)` updates.  The source family
`W_a=1^a0^{n-a}` satisfies the exact all-length identity
`P_n(W_a)=W_{min(2a,n)}`.  Starting at `W_1` therefore realizes the upper
bound, including the `n=1` boundary.  The clock is sharp as stated; the
verifier merely checks examples of this proof-level identity.

### 3. Every-target fibres and image

The fibre proof is a genuine inverse bijection, not a count suggested by a
census.  At every sign change, the simple walk must traverse the edge between
zero and minus one.  Cutting at those forced edges gives:

- an even nonnegative first excursion when the first target run is positive;
- an odd reflected first excursion when it is negative;
- an odd crossing-plus-excursion for every interior run; and
- a terminal meander of length one less than the last run.

These pieces concatenate uniquely, so the Catalan/meander product applies to
every target, with the constant targets treated separately.  The resulting
run language has ordinary generating function
`(2z+z^2)/(1-z-z^2)`, hence image size `F_{n+2}`.

For the extremal fibre, taking the absolute value of the source walk is an
injection into nonnegative meanders because the target signs recover the
original signed walk.  A nonconstant target forces a positive-time return to
zero, excluding at least the all-up meander.  The all-zero fibre has
`M_{n-1}<M_n` for `n>=2`; therefore the all-one target is uniquely maximal.
This also handles the `n=1` tie explicitly.

## Mandatory repairs

### A132-1 — malformed exponents in the fixed theorem (`MINOR`, mandatory)

Source lines 101 and 103 contain

```tex
(01)^r0^{,n-2r}
(01)^r1^{,n-2r}
```

The comma is rendered inside each exponent, so the published theorem does not
literally state the intended words.  Replace these by `0^{n-2r}` and
`1^{n-2r}`.  Reinspect the rebuilt PDF rather than relying only on source
grep.

### A132-2 — literal `qquad` in the constant-fibre display (`MINOR`, mandatory)

Source line 189 has

```tex
|P_n^{-1}(1^n)|=M_n,qquad |P_n^{-1}(0^n)|=M_{n-1}.
```

The PDF visibly prints the letters `qquad`.  Restore the missing backslash:
`,\qquad`.

### A132-3 — abstract overstates the delivered atlas (`MINOR-SCOPE`, mandatory)

"We determine the complete finite dynamics" normally promises the full
functional graph, or at least a state-wise decoder for terminal fixed point
and exact depth/basin data.  This paper proves the recurrent set, global and
sharp maximum stabilization, and exact one-step inverse geometry, but it does
not give a terminal-state/depth decoder for every source or basin sizes for
every fixed word.  The body itself is careful; the abstract should be made
equally exact.  A safe replacement is, for example,

> We determine its recurrent set and sharp global stabilization time, and give
> an exact target-wise atlas of its one-step fibres.

Alternatively, retain "complete" only after adding the missing state-wise
functional-graph contract and proof.

### A132-4 — record the post-round-0 artifact divergence (`MINOR-PROVENANCE`)

The corrected bibliography makes the current PDF differ from the frozen
round-0 PDF, while the existing build record does not identify both hashes or
explain the delta.  After A132-1--A132-3, rebuild in the normal isolated
four-stage sequence, freeze the new reviewed artifact under the appropriate
round name, and record source/PDF/stdout hashes plus fresh `cmp=0`.  Do not
overwrite `main_round0_original.pdf`.

## Ownership and claim boundary

The subtraction paragraph correctly assigns zero contribution credit to the
prefix-majority predicate itself, batched partial-sum evaluation, Catalan and
ballot enumeration, Fibonacci run languages, persistence terminology, and
generic majority-network dynamics.  Husfeldt--Rauhe is a direct owner for the
dynamic prefix-majority query predicate, not for feeding the whole answer
vector back into itself.  The residual internal claim is therefore narrow and
coherent: repeated full-vector feedback, its fixed language and sharp clock,
and its target-wise inverse atlas.

The reported owner search is bounded and cannot establish novelty by a
non-hit.  Accordingly, `HOLD_EXTERNAL` must remain in force pending specialist
owner review and explicit release authorization.

## Round-A exit condition

Round A passes once A132-1--A132-4 are implemented, the mathematical text is
otherwise unchanged or re-reviewed, the verifier again reproduces frozen
stdout, and the rebuilt PDF is visually checked at the three repaired
locations.  No new all-length computation is needed for these repairs.
