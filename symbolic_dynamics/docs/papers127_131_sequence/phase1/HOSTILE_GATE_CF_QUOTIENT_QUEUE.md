# Hostile gate: X18 continued-fraction quotient queue

**Role:** independent nonauthor theorem/owner/collision gate.  **Audit date:**
2026-08-31.  **External status:** **HOLD_EXTERNAL**.  **Hard verdict:**
**REWRITE / GO_IF_REPAIRED**.

The proposed finite map and every enumerated formula survive independent
reconstruction.  The current statement does not, however, define its
rational carrier correctly: canonical words with every displayed digit
positive represent only one half of the positive rationals under the standard
continued-fraction convention.  More importantly, all current proofs live
literally on integer compositions, immediately after P126.  Continued-fraction
terminology cannot cure that internal collision by itself.  X18 may survive as
a reserve only if the rewrite makes the Euclidean/Stern--Brocot carrier honest,
adds a second path/run-word derivation, and restricts value to the exact
quotient-queue conjunction.  If it remains merely P126's carrier with a
different local rule and classical necklace output, it should be killed for
portfolio value even though the mathematics is correct.

## 1. Evidence, hashes, and fresh execution

| reviewed file | SHA-256 |
|---|---|
| proof_spikes/CF_ROTATION_NORMALIZATION_REPORT.md | b49e8a945a6f1ce3cacf0f754f1cfdda13220ce67d99f5d853d926070cb8f8b3 |
| proof_spikes/verify_cf_rotation_normalization.py | 7721ece86e9b9d5d95147ff95eb523c6ca46056e757ac89e6c63fc6a7fd51000 |
| proof_spikes/CF_ROTATION_NORMALIZATION_CANONICAL.txt | bcf11f8629001e4ac78ce2090f47464cbecc7908a3ed0a92493174cae165f7ab |
| phase1/SYSTEM_COLLISION_FIREWALL.md | 84ed6ed93d308bc9565ba7d7d3629469358ad29287b0dc5fbe69f41eec6e55fc |

I ran

    python3 docs/papers127_131_sequence/proof_spikes/verify_cf_rotation_normalization.py > TMP
    cmp -s TMP docs/papers127_131_sequence/proof_spikes/CF_ROTATION_NORMALIZATION_CANONICAL.txt
    sha256sum TMP

from a fresh temporary file.  The byte comparison passed; fresh stdout has
SHA-256
bcf11f8629001e4ac78ce2090f47464cbecc7908a3ed0a92493174cae165f7ab.
The run reports **4,006,803 assertions** and exhausts every canonical word for
\(2\le N\le18\).  It checks each orbit normal form, every depth bin, every
one-step fibre, image/fixed counts, and the Burnside cycle formula.  The
evidence is deterministic and strong, but finite exhaustion is not the
all-\(N\) proof.

## 2. Literal carrier: a mandatory correction

Under the standard regular continued-fraction convention,

\[
q=[a_0;a_1,\ldots,a_k],\qquad
a_0\in\mathbb Z,\quad a_i\ge1\ (i\ge1),\quad a_k\ge2,
\]

is the unique canonical finite expansion of a nonintegral rational.  The
spike instead writes

\[
[a_1;a_2,\ldots,a_k],\qquad a_i\ge1,\quad a_k\ge2,
\]

and calls the resulting set “the positive rationals” of cost \(N\).  In the
standard notation these values are \(>1\); \(0<q<1\) and \(q=1\) are absent.
Thus the current carrier sentence is false.

There are two clean repairs, but the manuscript must choose exactly one.

1. Use
   \[
   \mathcal R_N=\{q\in\mathbb Q:0<q<1,\ 
   q=[0;a_1,\ldots,a_k],\ \sum_i a_i=N\}.
   \]
   Then the digit word is exactly the spike's positive composition ending in
   a part at least two.
2. Use the reciprocal half-line \(q>1\), with
   \(q=[a_1;\ldots,a_k]\), and say explicitly that this is one half of
   \(\mathbb Q_{>0}\), not all positive rationals.

For either repair, \(N\ge2\) and

\[
|\mathcal R_N|=2^{N-2},
\]

because subtracting one from the final part identifies the state words with
all positive compositions of \(N-1\).  The strata \(N=0,1\) are empty under
this convention and must be stated rather than silently omitted.

“Subtractive-Euclidean cost” also needs a convention.  If the subtractive
algorithm continues until one coordinate is zero, its step count is the sum
of canonical partial quotients; if it stops when the coordinates first
agree, an offset appears.  Minelli--Sourmelidis--Technau give the former
convention explicitly.  The safest title-level invariant is “canonical digit
sum \(N\), equivalently the stated subtractive-Euclidean cost,” followed by
the algorithm definition.

## 3. Literal update and exact temporal normal form

On a canonical word \(w=(a_1,\ldots,a_k)\), define

\[
\Phi(w)=
\begin{cases}
(a_1),&k=1,\\
(a_2,\ldots,a_k,a_1),&k>1,\ a_1>1,\\
(a_2,\ldots,a_{k-1},a_k+1),&k>1,\ a_1=1.
\end{cases}
\]

The last branch is rotation followed by the canonical identity
\([\ldots,b,1]=[\ldots,b+1]\).  It preserves the digit sum and again ends in
a part at least two, so this is a well-defined self-map on every
\(\mathcal R_N\).  “Trailing-one normalization” should not be described as a
second optional operation: it is part of the definition of the rational
self-map.

Let

\[
\delta(w)=\max\{i:a_i=1\},
\]

with \(\delta(w)=0\) when there is no one.  During one update, the marked last
one moves one place toward the front whether the first digit is rotated or
deleted.  No operation creates a new one.  On the \(\delta(w)\)-th update
that marked digit is deleted; all original ones have then disappeared.
Hence

\[
\operatorname{depth}(w)=\delta(w).
\]

The maximum on weight \(N\) is \(N-2\), and
\((1^{N-2},2)\) is a witness.  This includes \(N=2\), where the maximum is
zero.

To identify the terminal word, regard the indices cyclically.  Add the length
of every run of ones to the non-one digit immediately preceding that run,
delete the ones, and cut the resulting cyclic word immediately after the
last original one.  Call this ordered word \(\kappa(w)\).  The preceding
argument proves

\[
\Phi^{\delta(w)}(w)=\kappa(w).
\]

All parts of \(\kappa(w)\) are at least two.  On such a word \(\Phi\) is
ordinary left rotation.  Therefore:

- the recurrent set is exactly the words with all parts at least two;
- the eventual period of \(w\) is the primitive rotation period of
  \(\kappa(w)\);
- there are no additional transient states hidden inside the no-one set.

The spike has the right normal form, but a paper must prove the marked-position
invariant and the cut location, not merely state “absorb each run.”

## 4. Exact depth layers

Let \(D_t(x)\) count states of total digit sum \(N\) and exact depth \(t\).
A recurrent state is a nonempty sequence of parts from
\(\{2,3,\ldots\}\), so

\[
D_0(x)=\frac{x^2}{1-x-x^2}.
\]

For \(t\ge1\), the first \(t-1\) parts are arbitrary positive parts, part
\(t\) equals one, and the suffix is a nonempty sequence of parts at least
two.  Hence

\[
D_t(x)=
\left(\frac{x}{1-x}\right)^{t-1}x
\frac{x^2}{1-x-x^2}
=\frac{x^{t+2}}
{(1-x)^{t-1}(1-x-x^2)}.
\]

These are formal ordinary generating functions.  Coefficient extraction
must be included if the paper claims exact layer numbers, with the separate
\(t=0,1\) conventions made explicit.  Summing all coefficients at fixed
\(N\) must recover \(2^{N-2}\).  The verifier checks this but the report does
not show the algebraic identity.

This layer theorem is one of the two plausible residual engines.  It is also
elementary regular-language enumeration and cannot by itself distinguish the
project from P126.

## 5. Complete one-step fibres and image

For a target \(y=(b_1,\ldots,b_\ell)\), the only possible predecessors are:

\[
\rho(y)=
\begin{cases}
y,&\ell=1,\\
(b_\ell,b_1,\ldots,b_{\ell-1}),
&\ell>1\text{ and }b_{\ell-1}\ge2,
\end{cases}
\]

from an unnormalized rotation, and

\[
\eta(y)=(1,b_1,\ldots,b_{\ell-1},b_\ell-1)
\quad\text{when }b_\ell\ge3,
\]

from deletion of a leading one.  They are distinct whenever both exist, and
there are no other first-step branches.  Thus every fibre has size
\(0,1,\) or \(2\).

The no-preimage targets for \(N\ge4\) are exactly the words of length at
least two ending in \((1,2)\).  Deleting that suffix leaves a nonempty
composition of \(N-3\), so their number is \(2^{N-4}\).  Consequently

\[
|\operatorname{im}\Phi|=
\begin{cases}
1,&N=2,3,\\
3\cdot2^{N-4},&N\ge4.
\end{cases}
\]

For completeness, the Garden count is \(0,1,2^{N-4}\) for
\(N=2,N=3,N\ge4\), respectively.  The present report's fibre wording is
correct, but the manuscript should display these actual predecessor words
and handle the one-part target explicitly.

## 6. Recurrent cycles and the exact zero-credit boundary

For recurrent words of total weight \(N\) and length \(k\), rotation orbits
are cyclic compositions with every part at least two.  Burnside's lemma gives

\[
\mathcal C_{N,k}=
\frac1k
\sum_{d\mid\gcd(N,k)}
\varphi(d)
\binom{N/d-k/d-1}{k/d-1},
\qquad 1\le k\le\lfloor N/2\rfloor.
\]

The binomial convention is valid because \(N\ge2k\); it should be stated,
not called “evident.”  This formula counts rotation orbits grouped by digit
length, not primitive cycles grouped by dynamical period.  The pointwise
primitive-period theorem is valid, but an Artin--Mazur zeta or full
period-\(p\) census requires an additional Möbius inversion and is outside
the current contract.

Fixed words are constant digit words.  There is one for each divisor
\(d\mid N\) with \(d\ge2\), so

\[
|\operatorname{Fix}\Phi|=d(N)-1,
\]

where \(d(N)\) is the divisor-counting function.  The spike writes
\(\tau(N)-1\) without defining \(\tau\), while also discussing entrance
times; use \(d(N)\) or define the notation unambiguously.

All necklace, Burnside, totient, restricted-part, and divisor-counting
machinery is classical and receives zero contribution credit.  The only
possible value here is that this exact cycle set is coupled to the same
quotient-queue transient and fibre theorem.

## 7. Severity-ranked hostile findings

### CRITICAL

None in the corrected word-level map.  The current rational-carrier sentence
is false, but it has a non-destructive repair.

### MAJOR (mathematics and definitions)

1. **Repair the phase space.**  Choose \(0<q<1\) with a displayed initial
   zero, or choose \(q>1\).  Do not claim all positive rationals.
2. **Define Euclidean cost exactly.**  State the subtractive algorithm's
   stopping convention and prove that its cost is the chosen digit sum.
3. **Prove the terminal decoder.**  The paper needs a marker argument showing
   exact depth, the cyclic run absorption, and the cut immediately after the
   last original one.
4. **Close the depth-series offsets.**  Derive \(D_0,D_t\), state their
   coefficient ranges, and verify that the layers sum to \(2^{N-2}\).
5. **State the fibre inverse, not just its conditions.**  Include
   \(\rho(y),\eta(y)\), the one-part boundary, and the Garden count.
6. **Do not upgrade Burnside orbit counts to a period enumerator or zeta.**
   The current formula is by word length.  A zeta claim needs a separate
   primitive-period inversion.

### MAJOR (owner scope)

1. Minelli--Sourmelidis--Technau's
   [Euclidean-cost paper](https://doi.org/10.1007/s00208-022-02452-2)
   explicitly identifies the subtractive step count with the sum of regular
   continued-fraction digits.  Digit-sum cost, Euclidean terminology, and the
   convention are zero-credit.
2. Reutenauer's
   [Stern--Brocot expansion paper](https://doi.org/10.5802/jtnb.1104)
   owns the run-word coding, its continued-fraction relation, periodic
   binary words, cyclic/Lyndon representatives, and the modular-cycle
   interface.  Stern--Brocot level size and binary path coordinates are
   zero-credit.
3. Kan's 2026
   [finite-continuant paper](https://doi.org/10.4213/sm10170e)
   is a current primary source for finite continued-fraction words,
   uniqueness, matrices, prefixes/endings, and continuants.  Jones's 2026
   [extended-continuant paper](https://math.colgate.edu/~integers/aa73/aa73.pdf)
   directly discusses periodic partial-quotient words under reversal and
   cyclic permutation.  Neither paper located in this audit states the
   finite rational self-map, but all continuant and cyclic-CF infrastructure
   is zero-credit.
4. Gibson--Just--Wang's
   [restricted cyclic-composition paper](https://math.colgate.edu/~integers/s19/s19.pdf)
   and Hadjicostas's
   [cyclic-composition enumeration](https://cs.uwaterloo.ca/journals/JIS/VOL19/Hadjicostas/hadji2.html)
   own cyclic compositions with part restrictions and their cycle-index
   enumeration.  The Burnside formula is background, not a result attributable
   to the new map.
5. Searches on 2026-08-31 for exact rotation/trailing-one normalization,
   quotient-sequence cycling, cyclic Euclidean quotients, Stern--Brocot
   queue maps, and 2025--2026 variants found no primary source stating the
   literal map together with depth layers and fibres.  This is a bounded
   non-hit only, not novelty or priority.

### MAJOR (internal portfolio value)

1. **P126 is the hard collision.**  In canonical digits, X18's state space is
   literally a subset of integer compositions, not merely analogous to one.
   Both projects package all-depth information, image membership/counts,
   and pointwise fibres.  The nonconjugacy is real—P126 is a synchronous
   balanced morphism with logarithmic absorption to one fixed point and a
   suffix-code kernel, whereas X18 is a one-place queue with linear depth,
   fibres at most two, and many rotation cycles—but different formulas on
   the same carrier are not automatically portfolio value.
2. **P117 owns cyclic run reduction and recurrent classification.**  It acts
   on labelled binary words by simultaneous odd-run flips and has periods at
   most two; X18 deletes leading quotient-ones sequentially and then rotates.
   Run language, cyclic-composition coordinates, sharp depth, and cycle/zeta
   bookkeeping are zero-credit.
3. **P122 owns the reversal/depth/fibre/image-Garden package.**  Its carrier is
   permutations with recomputed record blocks and a finite automaton; X18 has
   neither records nor reversal.  Still, the presentation silhouette
   “sharp linear clock + exact target fibres + image/Garden count” is already
   occupied and cannot be sold as value.
4. The rational name is not a firewall.  If every proof is transported
   verbatim through the composition bijection, the candidate violates the
   sequence's carrier-relabeling guard.

### MINOR

1. Reserve \(\tau\) for either depth or the divisor function, not both.
2. State whether rotations are left rotations and whether period means the
   number of map applications.
3. Use “canonical normalization” only for the final-one identity; do not
   suggest an iterative normalization beyond one local rewrite.
4. Record \(N=2,3\) everywhere a power \(2^{N-4}\) occurs.
5. Keep “formal OGF,” “weighted necklace,” and “primitive period” distinct.

## 8. Bounded owner-search log

Representative queries included:

- finite continued fraction cyclic shift partial quotients rotation;
- trailing one normalization cyclic continued fraction;
- Euclidean quotient sequence cyclic permutation;
- Stern--Brocot continued fraction word rotation necklace;
- integer composition rotate first part delete one add to last;
- cyclic compositions parts at least two Burnside;
- 2025 2026 continuant cyclic partial quotient word.

The audit read the primary sources linked above and also checked the current
2026 continued-fraction/continuant neighborhood.  Generic Gauss/Farey shift
maps remove a leading digit; they are not this operation, which appends it
and then canonicalizes.  No literal temporal owner was found within these
bounded formulations.

## 9. Allowed claim ceiling and freeze conditions

The maximum admissible claim package is:

1. the literal canonical-CF quotient-queue map on one precisely defined
   rational half-level \(\mathcal R_N\);
2. exact entrance time, sharp \(N-2\) witness, and the terminal-core decoder;
3. the formal exact-depth OGFs and coefficient layers;
4. the complete \(0/1/2\) one-step fibre law, image, and Garden counts;
5. the recurrent rotation classification, pointwise primitive period,
   weighted-necklace orbit count, and fixed count.

No claim is allowed for canonical CF uniqueness, the trailing-one identity,
Euclidean cost, Stern--Brocot coding, continuants, restricted compositions,
Burnside/necklaces, priority, asymptotics, all positive rationals, or a
general family of continued-fraction maps.

**Freeze requires all of the following.**

1. Correct the rational carrier and Euclidean-cost convention.
2. Give complete proofs of the marker/core, layer, fibre, and cycle statements
   with \(N=2,3\) controlled.
3. Add the direct owners above and the explicit P117/P122/P126 subtraction.
4. Supply a genuinely second derivation in Stern--Brocot binary path/run
   coordinates that independently recovers at least the terminal decoder and
   one of the layer or fibre formulas.  A sentence translating compositions
   into rationals is not enough.
5. Keep the residual headline as the literal
   **Euclidean quotient queue + terminal decoder + depth layers + small fibres**;
   necklace and divisor formulas must be corollaries with zero credit.

If these conditions close, X18 is defensible as a compact internal reserve
despite the P126 carrier collision: **GO_INTERNAL_AFTER_REPAIR**, external
**HOLD**.  If no genuinely rational/Stern--Brocot second engine is supplied,
or if a direct owner of the quotient queue is found, the correct outcome is
**KILL/RESERVE**, not paper freeze.
