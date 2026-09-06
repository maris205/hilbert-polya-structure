# Independent coordinator review: the all-odd-degree rational cycle graph

Scope: nonauthor mathematical and closest-source review of
`nonlinear_geometry/PROOF_PACKAGE.md`, its four symbolic-certificate modules,
and `nonlinear_geometry/SOURCE_AUDIT.md`. This is internal model review, not
external or human peer review. The coordinator did not author this theorem.
The producer's initial numerical scout is not the proof of the universal claim.

## Final decision

**Mathematical argument: PASS at the stated all-odd-degree scope.** The three
source/parametrization precision requests and final independent certificate
receipt are closed. The coordinator admits one bounded substantive contract;
this does not itself assign a paper number or complete the five-contract gate.

The claim is for the exact central-factorial polynomial printed in the proof,
the map `(y,-x+s_d(y))`, all of `Q^2`, and ordinary positive iteration. Opposite
cycles are counted separately unless joined by actual iteration. The degree
range is every odd `d>=3`, with no eventual-degree qualification. These choices
are necessary: changing the phase, sign, shift or quotient would change the
central and boundary cycle tables.

## Proof dependency review

### 1. Rational integrality and an integer escape box

For a nonintegral rational coordinate at a fixed prime, each factor
`y^2-i^2` has the same norm as `y^2`. The factorial summand norms strictly
increase with the summation index, including when the prime divides a
factorial. Thus the leading summand is unique; at a maximal-norm orbit
coordinate its norm exceeds both adjacent coordinates. This proves integrality
without a missing `(p,d)=(2,3)` exception.

The coefficient generating series `z/(1-z+z^2)` produces exactly the declared
six-periodic sequence. The one- and two-term omitted tails give the two
boundary values with the printed degree-dependent phase. I checked the
central second-difference identity and its induction base `s_3(n)`.
For the induction step, the preceding degree's threshold is `R+2`, so its use
at `R+2` and subsequently is within range. The lower bounds for the first
increment and `s_d(R+3)` suffice at the smallest allowed `R=3`.

The resulting `|s_d(n)|>=3|n|` for `|n|>=R+3` contradicts a maximal-coordinate
periodic recurrence. Only integer escape is needed after integrality; no
unverified real-variable derivative bound or finite exceptional rational
search is being used. This proves the required box, not a statement about all
complex or rational nonperiodic orbits escaping in both directions.

### 2. Full bulk table and exact clipped multiplicities

The two-variable affine recurrence remains valid throughout an entire residue
cell. The returned identity gives a generic period, and the full itinerary
intersects to the printed rectangle because every coordinate is one signed
free variable plus a constant. Proper periods need only be tested at proper
divisors. The linear-system routine explicitly rejects a consistent rank-one
family; it does not silently lose a possible infinite exceptional set.

The 17 exceptional points are precisely one fixed point, two 5-cycles and
one 6-cycle. They and their intermediate points lie in the smallest core.
Subtracting these points before dividing by generic period is consequently
valid in every radius progression. Formula (5) counts exact integers of one
residue between two inclusive affine bounds; the floor/ceiling signs and the
`2m` coefficient are correct. The code verifies nonnegative coordinate counts
already at each smallest permitted `m`, preventing a missing positive-part
term. Summation and division give the displayed quadratic polynomials.

This is a symbolic clipped-orbit calculation, not polynomial interpolation
of degree samples. The core residue-period classification itself is already
in the primary source and is deducted in the substance decision below.

### 3. Negative phase and the ordinary clock

Direct substitution verifies `Sg=gS` and `g_-=C(Sg)C`. Both coordinate
symmetries preserve the core. For a generic period divisible by four, an odd
return under `Sg` would imply `ell | 2n` with `n` odd, which is impossible;
an even return has the original period. Thus generic periods and counts are
unchanged, although the actual orbits must be transformed as stated in Step 3.

Negation exchanges the two 5-cycles, yielding one 10-cycle for `Sg`; on the
6-cycle it equals `g^3`, so `Sg=g^4` gives two 3-cycles. This accounts for
all 17 central points in the other phase and does not replace the ordinary
clock by a quotient clock.

### 4. First-return section, signs and complete endpoint domain

Any remaining periodic orbit must meet the section because it has an outside-
core coordinate. The section has no fixed point of negation. A first-return
cycle with positive sign therefore gives two distinct ordinary cycles of
its total time; negative sign gives one of twice that time. An earlier
ordinary return would repeat a normalized section state earlier, contradicting
first return and primitive normalized cycling. This justifies both periods
and multiplicities, rather than only a count of signed states.

For each free strip the intermediate bulk inequalities are recorded before
the first boundary coordinate; the affine identity alone would not suffice.
The four-symbol tuple convention and normalized translation signs in the
compressed table agree with the generator. A targeted read-only diagnostic
confirmed that the auxiliary strip lower-radius bound is exactly two in all
36 `(R mod 6,x mod 6)` cases, so the prose's all-`R>=2` assertion is literal.

The outer-layer inequality is `x>=R+s-2`; its complement escapes in one step.
The inner endpoint set is the exact complement of the six residue strips
inside `[-R-2,R+2]`, not a guessed corner cutoff. The strengthened endpoint
generator derives those complementary intervals. The smallest radii are
`6,7,2,3,4,5`, not six arbitrarily selected samples: each checks an affine
inequality on its whole increasing progression. The affine-alias checks
ensure two named endpoint states do not coincide at a small admissible radius.

### 5. Exhaustive boundary routing, including the unbounded chain

For `s=0`, the `2q+1` stationary multiple-of-three strips and the one
endpoint 4-cycle are disjoint; the four-node signed endpoint circuit has
total time 14 and positive sign, yielding two 14-cycles. The unused strips
either go to the outer layer below threshold or to the explicitly listed
escaping endpoint chains. No unassigned residue or endpoint remains.

For `s=1`, the stationary progression has `q-1` points and is empty at
`q=1`. The long normalized circuit consists of its initial time-one edge,
`q+1` time-two edges and `q` time-six edges. The decreasing coordinates
`a_j=R+1-6j` have two interleaved, distinct residues; the terminal value is
`a_q=-R+3`, whose next target is the starting endpoint. Thus the circuit is
primitive and has time `8q+3` with negative sign. The two strip progression
counts prove that this circuit uses every generic state of those residues,
not merely that one long cycle exists. The remaining residues and endpoints
are stationary cycles, the listed finite endpoint cycles, or escape paths.

For `s=2`, the paired residues give exactly `q` normalized two-node circuits;
each has time eight and positive sign, hence two ordinary 8-cycles. The list
is empty at `q=0`. The two endpoint circuits give the claimed 4- and 6-cycle
counts. All other strips feed below the outer threshold or into the stated
escaping endpoint paths. The endpoint complement and the residue partition
make this exhaustive.

The executable certificate checks the affine identities, complementary
domains, specified constant cycles and progression counts. The exhaustive
escape-routing argument and the long-chain connectivity above remain explicit
proof obligations in Steps 5–7; a code PASS must not be described as an
independent automatic classification of an infinite graph.

### 6. Disjoint assembly, small degrees, and zeta convention

Core-contained and boundary-meeting cycles are disjoint. At radii 2, 3 and 4,
the uniform formulas give 31, 69 and 115 points with nonnegative
multiplicities and the claimed empty families. These are substitutions into
proved all-radius formulas, not additional finite-degree evidence.
The growing period is at least 22 and cannot equal 36 for integer `q>=1`;
there is no hidden collision with a constant period. Repeated periods four
or six from distinct additive tables must and do have added multiplicities.

Adding period times multiplicity gives the three printed total polynomials.
The divisor formula for fixed points and finite source-zeta product then
follow from ordinary cycle counting. They supply no target arithmetic
determinant, Euler factors, root number or zero correspondence.

## Closest-source ownership and substantive increment

I directly inspected the [primary arXiv v2 HTML](https://arxiv.org/html/2412.01668v2),
including the introduction, central-factorial definition and Lemma 2.1,
the exact escape statements around Corollary 4.3, Theorem 4.4 and its count
remark, Theorem 5.1 with its long-cycle proof, and Proposition 5.2 with its
full residue table and central exceptions. The source header says 8 July
2025; the served document's internal date says 24 August 2026. These are
separate observed fields, not grounds to invent a publication update.

The following are explicitly deducted: the polynomial family, rational
integrality/escape box, many-point construction, the entire positive-phase
bulk period classification and 17 exceptions, and existence of the growing
cycle. The new escape rederivation is a self-contained proof convenience,
not an additional independent paper result.

The surviving increment is the full radius-clipped multiplicity calculation,
the complete signed boundary permutation with all escape alternatives, and
hence the complete rational cycle graph in every odd degree. The natural
target of the source's numerical count conjecture is fully decided for its
exactly printed map, not just for sampled degrees or one congruence class.
This is a substantive family classification after those deductions.

The v2 Theorem 4.4 gives at least 225 points at `d=13`; its count remark
gives 153, while the present proven formula gives 271. This is a bounded,
version-specific discrepancy, not a claim about an unseen journal final
text, the authors' intent, or worldwide priority. The shifted family printed
in that article is not silently identified with the frozen map here.

Final adjudicated recommendation after precision/check closure:
**ADMITTED_BOUNDED_SUBSTANTIVE_CONTRACT**, as one family theorem only.
Formal Route A evaluation, manuscript review and reproducible PDF release
are separate unperformed gates. No target A1/A2 success is inferred.

## Requested precision closure and final receipts

1. Split the source's arXiv-header and internal-document dates in its audit.
2. Explicitly credit Proposition 5.2's entire core period table and 17
   exceptions, and Theorem 5.1's growing-cycle existence, rather than say
   only that the source studies the bulk map.
3. Clarify in the claim's graph-parametrization sentence that negative-phase
   actual points use the Step 3 coordinate conversion.

These requests do not alter the stated theorem or require a new degree
census. The coordinator reread all three affected portions of the final
proof/source files: dates are now separated in both records, the named
classical results are explicitly deducted, and the claim's actual graph
labels point to the negative-phase conversion. All three requests are closed.

Actual final-input hashes verified by the coordinator with `sha256sum`:

- `PROOF_PACKAGE.md`:
  `a1a0c8fbd2ff8b1fbd3bc73606c8dd435c727fe914cbf907d9e55d7f8c9891e0`.
- `SOURCE_AUDIT.md`:
  `3b89e0e5bf4586b55f270bfe3391bb8607e9eddd30e748e2b670d6a151deb3e9`.
- `symbolic_bulk.py`:
  `7a99667d25790a65cdbce9b429577350c65e7038c5aac00e663a5e7ab3789691`.
- `symbolic_boundary.py`:
  `af7491291cb6292c044bad6ddceaa7f76ba0146110ceca6fd473347308350fea`.
- `symbolic_corners.py`:
  `8d878ed3f4b639b63f5d674ca11b85818bce5ef9b9317626f23f9fbde6f6010d`.
- `verify_symbolic_certificate.py`:
  `0377f99976173cf0e4d177e0793de49ce8bbecf0565cb4fa47b49aef697b98fb`.

The coordinator subsequently read the entire 347-line
[independent certificate review](positive_characteristic/REVIEW_GEOMETRY_CERTIFICATE.md),
SHA256 `45761e4d9da58b56642946d2d1370696b760a6e52fda0ff4b30e9e6723735d06`.
It binds the same four code inputs and proof digest, records the one final
producer-certificate reproduction with assertions enabled, and supplies a
distinct check of both central phases, 128 affine alias equations and weighted
cycle-polynomial arithmetic. The reviewer's first one-off command failed at
parse time; its corrected command passed. That failure did not execute a
mathematical check or change an input, and was not hidden as a successful run.

The concrete endpoint-complement and derived-count repairs are adequate.
I retain the report's exact scope: it does not automatically classify all
escape trajectories or the long chain. Those steps were separately checked
in the complete mathematical review above. No required proof/source/
certificate repair remains for research admission. Final decision:
**ADMITTED_BOUNDED_SUBSTANTIVE_CONTRACT**, one contract only, not a completed
paper and not a target Route A success.
