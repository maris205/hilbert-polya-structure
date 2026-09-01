# Hostile review A — round 1

**Verdict: ACCEPT WITH MINOR REPAIRS.**  I found no counterexample, missing
component, or all-parameter gap in the stated theorem for odd prime powers.
The partition, sharp tails, cycle census, zeta function, every-target fibre
law, and distinguished exceptional component all survive independent
rederivation, including the boundary fields `q=3`, `q=5`, and nonprime
fields.  The current source, PDF, frozen transcript, and verifier are mutually
consistent.  The two requested repairs below harden exposition and the
bounded source audit; neither changes the theorem.

## Severity summary

- **Critical:** none.
- **Major:** none.
- **Minor:** two items, both with local repairs.

## Severity-ranked findings

### M1. MINOR — the owner-search record is too aggregate to be replayable

`SOURCE_VERIFICATION.md` gives a responsible non-clearance statement and
subtracts the classical rational map, five-periodicity, cluster/QRT context,
finite-field birational methods, and generic zeta algebra.  I found no direct
owner of the paper's residual conjunction: the literal affine self-map with
`inv0(0)=0`, its five-stratum atlas, sharp clock, complete functional graph,
and every-target inverse law.  In particular, searches combining the Lyness
formula/name with `finite field`, `division by zero`, `inverse-or-zero`,
`zero-totalized`, `totalized field`, `functional graph`, and `singularity`
did not produce the same scheduler.

The ledger nevertheless records only a prose summary of this search.  It
does not list the actual query families and candidate-by-candidate exclusions,
and it omits two primary adjacent sources that make the subtraction boundary
more auditable:

- R. C. Lyness, “1581. Cycles,” *The Mathematical Gazette* 26(268), p. 62
  (1942), DOI [`10.2307/3606036`](https://doi.org/10.2307/3606036), is the
  historical source identified by the publisher for the recurrence's cycle;
- M. Kanki, “Integrability of Discrete Equations Modulo a Prime,” *SIGMA* 9,
  056 (2013), DOI
  [`10.3842/SIGMA.2013.056`](https://doi.org/10.3842/SIGMA.2013.056), treats
  division-by-zero/indeterminacy in finite-field discrete dynamics through a
  different extension/reduction convention.

Neither source is a direct hit on `inv0(0)=0`, and neither subtracts the
residual graph theorem.  Their omission therefore does not defeat the paper,
but the current non-hit is harder to audit than it needs to be.

**Required repair.**  Add a compact query/candidate/exclusion table to
`SOURCE_VERIFICATION.md`, record access dates, and add the two primary sources
above as zero-credit historical/adjacent-convention entries.  For Kanki,
state explicitly that extension of the space or almost-good reduction is not
the paper's inverse-to-zero affine totalization.  Retain `HOLD_EXTERNAL` and
the present statement that a bounded non-hit is not clearance, novelty, or
priority evidence.

### M2. MINOR — make the five-cycle exponent's integrality and the two smallest
field boundaries explicit in the manuscript

The displayed count

`((q-2)(q-3)-r_q)/5`

is an integer for the reason already present implicitly in the proof: after
removing the `r_q` fixed points, the generic locus is partitioned by the
literal map into exact orbits of prime length five.  Thus no independent
quadratic-character congruence is needed.  The argument is correct, but the
sentence “Dividing by five gives their cycle count” makes the integrality
interface easy to mistake for an unproved arithmetic assertion.  The
small-field behavior is also only distributed across the proof and own-author
QA: at `q=3` the generic locus and the 4/5-cycle families are empty while the
depth-three layer is nonempty; in characteristic five the fixed polynomial
has one double root (so `r_q=1`), including `q=5` and its extensions.

**Required repair.**  Replace the division sentence by an explicit orbit-
partition sentence: the nonfixed generic points are a disjoint union of
five-element `L`-orbits, which simultaneously proves divisibility and the
cycle count.  Add one short boundary remark recording the `q=3` degeneration
and the characteristic-five double-root case.  This is explanatory hardening,
not a correction to the formula.

## Independent theorem rederivation

### Whole-plane partition

After removing the axes, `x` and `y` are nonzero.  The mutually exclusive
ordered tests

1. `y=-1`;
2. `y!=-1` and `x=-1`;
3. `x,y!=-1` and `1+x+y=0`;
4. none of the above

give `E1`, `E3`, `E2`, and `G`, respectively.  The parameter exclusions in
the three exceptional sets are exactly those needed to keep both coordinates
nonzero.  Their sizes are `q-1,q-2,q-2`; the axis union has size `2q-1`; hence
the residual generic size is `(q-2)(q-3)`.  This proves actual pointwise
coverage and disjointness rather than inferring them from a cardinality sum.

### Generic recurrence and all sharp tails

On `G`, direct substitution gives

```text
(x,y)
 -> (y,(1+y)/x)
 -> ((1+y)/x,(1+x+y)/(xy))
 -> ((1+x+y)/(xy),(1+x)/y)
 -> ((1+x)/y,x)
 -> (x,y).
```

Every denominator is certified nonzero by the five defining factors of `G`.
On the complement, direct evaluation gives the invariant axis dynamics and

```text
E3: (-1,-1-a) -> E2: (-1-a,a)
    -> E1: (a,-1) -> (-1,0),
(-1,-1) -> (-1,0) <-> (0,-1).
```

Since the five strata are disjoint and the axes are invariant, these entry
times are exactly `1,2,3`, not merely upper bounds.  The recurrent population
is `(q-2)(q-3)+(2q-1)=q^2-3q+5`, yielding the stated temporal polynomial.  As
`|E3|=q-2>0` even at `q=3`, the maximum tail three is genuinely sharp for
every allowed field.

### Complete cycle census, integrality, and zeta

A fixed point has `x=y`.  Besides `(0,0)`, the equation is
`a^2-a-1=0`.  Such a root is neither `0` nor `-1`; moreover `1+2a` cannot
vanish because substitution of `a=-1/2` gives `-1/4`, nonzero in odd
characteristic.  Hence all `r_q` nonzero fixed points lie in `G`.

On the axes, inversion fixes exactly `a=1,-1`, producing the two stated
2-cycles.  The remaining `q-3` nonzero labels pair under inversion, giving
`(q-3)/2` 4-cycles.  On `G`, `L^5=id`; because five is prime, every generic
nonfixed point has exact period five.  Those points therefore partition into
five-element orbits, proving both the count and its integrality.  The
exceptional layers cannot contain cycles because they enter the invariant
axis set.  This exhausts all states.

For a finite self-map, each cycle of length `d` contributes
`(1-z^d)^(-1)` to the Artin--Mazur zeta product.  Substitution of the four
cycle counts gives exactly the manuscript's formula; transient vertices do
not contribute to any fixed iterate.

### Every-target fibres and the whole exceptional component

For target `(u,v)`, the first coordinate forces the source to be `(x,u)` and
the second coordinate becomes

`(1+u) inv0(x)=v`.

If `u=-1`, all `q` choices of `x` hit `v=0` and none hits nonzero `v`.  If
`u!=-1`, `v=0` forces the unique solution `x=0`, while `v!=0` has the unique
nonzero solution `x=(1+u)/v`.  This proves the `q/0/1` law and image size
`q(q-1)+1`.

Iterating this inverse law resolves every predecessor of the distinguished
2-cycle.  The fibre of `(-1,0)` consists exactly of all `(x,-1)`.  Its
noncycle members are the lone leaf `(-1,-1)` and the `q-2` endpoints
`(a,-1)` of the displayed length-three chains.  Each chain then has one
predecessor at the next two levels, and its top vertex has empty fibre;
`(-1,-1)` also has empty fibre.  Thus no omitted vertex or incoming branch
can enter the component.

### Boundary-field checks

- `q=3`: `|G|=0`; the recurrent set has size five; there is one fixed point
  and two 2-cycles, with no 4- or 5-cycle; the exceptional sizes are `2,1,1`,
  so depth three remains attained.
- `q=5`: `|G|=6`; the fixed polynomial has one double root; the cycle census
  is two fixed points, two 2-cycles, one 4-cycle, and one 5-cycle.
- Nonprime fields: every symbolic step uses only field axioms, odd
  characteristic, and finiteness.  In particular, `a^2=1` still has only the
  two roots `+/-1`, and the argument does not assume a prime field or an
  ordering of field elements.

## Executable, transcript, and artifact audit

I cold-ran

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p150.py | cmp - verification_output.txt
```

and obtained a byte-for-byte match.  The run covers all odd prime fields
through `F101` and the declared extension fields
`F9,F25,F27,F49,F121,F125`: 31 fields, 110,095 state/target cells, and
2,144,131 assertions.  It uses literal forward orbits, independently extracts
cycles, checks all five displayed generic iterates, checks exact tail/period
pairs, asserts divisibility by five, tests fixed-iterate shadows through
iterate 20, enumerates every target fibre, and compares the full predecessor
sets in the exceptional component.  Its extension polynomials pass the
degree-two/three irreducibility test and its arithmetic checks Frobenius and
nonzero inverses.  Enumeration remains falsification only; the manuscript's
all-field proof does not depend on it.

Before adding this review, `sha256sum -c SHA256SUMS` passed for every listed
artifact.  The frozen transcript hash is
`f95db125148f156dd5ea4a75e2acbf22a68ed565e4c5df6c1399e018acf8f460`.
Both `main.pdf` and `main_round0_original.pdf` have SHA-256
`d94b53e9a1e496c766e8770e88f588053b7333e702b08177f0647578f90d274d`.
An isolated source-only LaTeX/BibTeX build produced the same five-page text,
file size, and clean warning profile as the checked PDF.  All five rendered
pages were inspected: no clipping, overlap, broken formula, unresolved
reference, identifying author metadata, or illegible bibliography entry was
found.  The PDF is A4, unencrypted, and has blank title/author metadata.

The three existing bibliography records agree with their DOI/publisher
metadata, including the Hone--Kouloukas online-2022 versus issue-2023 date
distinction.  The source audit repair in M1 is therefore about coverage and
replayability, not a detected metadata error or an owner hit.

External status must remain **`HOLD_EXTERNAL`**.  This review authorizes no
posting, contact, submission, Git action, or release.
