# C411 paper plan

Working title: **Joint meromorphic boundaries of two-clock common returns**.

One-sentence contribution: for every integer pair a,b>=2, the independently
marked common-return series has an exact open convergence domain, a complete
dependent-branch polar divisor, and the whole bidisc as its joint meromorphic
natural-boundary domain.

Format: anonymous English mathematical article, 11pt, one-inch margins;
no selected venue or fixed page budget. This refines the parent BATCH_PLAN,
which has been frozen after independent outline review. The R3 refinement
is binding: the theorem distinguishes the initial open absolute-convergence
domain from meromorphic continuation to D² and the terminal joint boundary
∂D². It does not make every curved convergence-boundary point singular.

## Fixed inputs

All paths here refer to ../../../research_c409_c413/ relative to this directory.

- arithmetic/RECTANGULAR_RETURN_PROOF.md: all-base classification and full proof.
- arithmetic/RECTANGULAR_SOURCE_AUDIT.md: precise rectangular, volume,
  subgroup-index, synchronization and diagonal ownership distinctions.
- arithmetic/RECTANGULAR_EXACT_CHECK_REPORT.md: existing finite diagnostic
  receipt, not a basis for the analytic theorem and not to be re-run.
- REVIEW_RECTANGULAR_ROOT.md and
  positive_characteristic/REVIEW_HARTOGS_PROPAGATION.md:
  independent full checks and the explicit regularized-tail-envelope proof.

Only the new paper directory is written. Frozen source/review bytes and
mathematical receipts remain unchanged.

## Claims–evidence matrix

| Paper claim | Frozen evidence | Prior content deducted | Location |
| --- | --- | --- | --- |
| For independent bases the exact open absolute domain is D² | Proof §3.2 and the actual two-exponent CZ input | No new gcd bound; no unjustified replacement by the diagonal BCZ estimate | §3 |
| For a=c^r,b=c^s,(r,s)=1 the exact domain is D² intersect c^(rs)|x|^s|y|^r<1 | Proof §3.1/3.3, sufficient geometric bound and divergent distinguished ray | Common-base and gcd identities are classical | §3 |
| The dependent series continues meromorphically to D² with all primitive-ray polar components genuine and simple | Proof §4, bounded ray exponents, normal tails and signed residue formula | Ray decomposition itself is classical; actual polar geometry and noncancellation are part of this family's classification | §4 |
| No boundary point of D² admits joint meromorphic continuation in either branch | Proof §§5–8 and full independent Hartogs review | Positive Cauchy-measure and subharmonic tools are classical; the full parameter/threshold application is proved | §§5–6 |
| This joint conclusion does not assert all slices have natural boundaries | Axis example and cap definition; dependent strip/pole threshold split | No independent novelty for merely keeping two clocks or for known diagonal non-D-finiteness | §§1–2, 6–7 |

## Structure

Abstract plus seven numbered sections, each in an actual section file.
Every required proof appears in the manuscript body. No numerical experiment
section or external proof-link substitution.

### Abstract

Define the ordinary double gcd series and give both branches of the domain
classification. State the primitive-ray meromorphic continuation and genuine
poles in the dependent branch, followed by the joint boundary conclusion.
Explicitly say this is joint continuation, not a claim about every individual
slice. Around 170–220 words; no citations or undefined specialized abbreviations.

### 1. Introduction: what two independent clocks retain

Start with common fixed points of the two circle multiplication maps.
State the problem and preview the complete theorem.
Deduct Ward's native rectangular counts and earlier volume-weighted zeta,
Miles's one-time synchronization and full-subgroup-index zeta, and the current
diagonal recurrence classification. A compact object/clock/series table makes
these exact differences visible without claiming the objects were newly defined.

Use a=b=2 to show that a rational diagonal does not recover the two-variable
interior poles or joint bidisc boundary. Do not label a diagonal or
non-D-finiteness consequence as an extra theorem.

### 2. Common returns and the joint continuation theorem

Define the circle maps, independent times n,m, count and ordinary R(x,y).
Prove the cyclic-kernel gcd identity and state the optional solenoid
realization only briefly. Define open absolute convergence as an interior,
and define a local joint meromorphic cap by agreement on the interior overlap.

State the complete all-base theorem: exact domains, primitive-ray expansion,
full polar divisor, one-variable residue formula, and all of the bidisc boundary.
Include axes outside the open domain as pointwise zero-sum exceptions and
the entire y=0 slice as a warning against a stronger slice claim.

### 3. Arithmetic input and exact convergence domains

Prove unique coprime-exponent common-base form without requiring the base
c to be power-free. Prove the elementary gcd identity for same-base powers.
Quote the exact two-exponent Corvaja–Zannier consequence from the inspected
v2 Corollary 1/(1.3), absorb finite exceptions uniformly, and derive normal
convergence on every compact sub-bidisc.

For dependent bases, give the exponent-slack sufficient estimate and the
distinguished-ray necessity. Treat fixed-row divergence and zero axes separately.
Do not call every curved convergence-boundary point a singularity.

### 4. Primitive rays and the full polar divisor

Derive the geometric sum along (n,m)=k(i,j). Prove
gcd(ri,sj)=gcd(r,j)gcd(s,i) divides rs. Establish locally normal meromorphic
tails on the whole bidisc, with only finitely many local exceptional terms.
Prove each primitive monomial level is smooth and irreducible in the torus,
distinct and nonempty in D². Give the generic simple-pole argument and
the exact residue -x0 sum(1/i), which rules out coincident-pole cancellation.

### 5. A dense atomic boundary on positive real slices

For 0<t<1/b, derive the totient/order expansion, construct the positive finite
atomic measure and bound its total mass. Use powers of one prime not dividing
ab to obtain unbounded orders and full dense root grids. Prove the radial
mass limit by dominated convergence and rule out meromorphic continuation.
No Diophantine approximation bound is needed in this part.

### 6. Propagation to every joint boundary point

State and prove the classical-tool cap lemma on D times a connected parameter
domain. Prefer the independently checked regularized tail envelopes
V_N=(sup_{n>=N} n^{-1}log|a_n|)^* and their decreasing limit: this avoids
any unsupported identification of raw limsups with subharmonic functions.
Give all Cauchy bounds, the maximum principle and the denominator reduction.

Apply it to the independent bidisc. For the dependent branch apply it only
on D times D_(1/b), where joint holomorphy is known. For |y|>1/b use the
actual primitive-ray pole grids (sk,r), for every neighboring parameter;
show a joint denominator would vanish identically. Finish the threshold,
opposite face and corner arguments. Do not apply a holomorphic-product lemma
to the dependent function on a bidisc containing genuine poles.

### 7. Consequences and limits

Explain the dependent example a=b=2 and the distinction between convergence
domain and meromorphic domain. Recap which classical ingredients were used.
State that no uniform exceptional-slice natural-boundary claim, effective
CZ threshold, Euler-prime identification or Hilbert–Pólya conclusion is supplied.
No additional contract or unrun experiment.

## Figures, citations and provenance

Use one object/clock/function table in §1. No synthetic figure is needed:
the exact domain formula and primitive-ray divisors communicate the geometry.
No mandatory page-length padding, diagram, or new numerical pole plot.

Seven intended citations: Ward 1989, Ward 1992, Miles 2013, Miles 2015,
Corvaja–Zannier, Nguyen-Dang v2, and Korevaar–Wiegerinck 2017 notes.
Theorem locators refer to the inspected versions; publisher metadata alone
does not certify equality of manuscript and typeset numbering.
CITATION_METADATA.md records verification and references.bib contains
only these planned citations.

## Review and build gate

Root has confirmed outline freeze and authorized body drafting. A new non-author full
manuscript review must check all statements, proof coverage and citations.
Existing proof reviews remain evidence, not draft-review substitutes.

Author LaTeX checks/builds concern new paper sources only. The old 784-kernel,
24,624-coefficient and four-pole checks are not rerun or described as proof.
Root owns formal evaluation, final deterministic rebuilds, PDF inspection,
global state, exact ledgers and Git.
