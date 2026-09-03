# Hostile Review A — P180 bilinear radial scaling

**Role:** independent algebra reviewer; author package read-only  
**Frozen author baseline:** `main.tex` SHA-256
`7f43974b3a3885545f5a2bc6910a79359c6f039e41819fa2085f2c9b29c24712`  
**Original Round-0 decision:** `MAJOR_REPAIR / DO_NOT_KILL / HOLD_EXTERNAL`  
**Round-1 delta disposition:** `ACCEPTED / HOLD_EXTERNAL`  
**Current open findings:** `0 Critical / 0 Major / 0 Minor`

## 1. Scope and independent method

I re-derived the literal map, iterate, pointwise tails and periods, every
target fibre, tail populations, image, and maximum-fibre claim.  I also read
the manuscript, bibliography/source ledger, plan/narrative/claims/self-QA,
build record, author verifier/canonical, and the P1–P176 collision surfaces.
No paper file was edited or compiled.

The independent verifier is deliberately outside the author's model.  It
implements polynomial-basis fields `F4`, `F8`, and `F9` in addition to prime
fields, and uses invertible nonsymmetric Gram matrices such as
`[[1,alpha],[0,1]]`.  It checks two-sided nondegeneracy literally, traverses
the full functional graph, and constructs every time-`t` fibre as a target
histogram.  Thus it pressures the two theorem axes absent from the author
enumeration—extension fields and nonsymmetric forms—as well as
characteristic two, `A=0`, `A>=2`, and `t=0`.  No author/scout module or code
organization is reused.  Two fresh processes match `CANONICAL.txt` byte for
byte.

## 2. Independent re-derivation

Write `c=B(u,v)` and `a_t=(3^t-1)/2`.  Bilinearity alone—not symmetry—gives

```text
B(lambda u,lambda v)=lambda^2 B(u,v).
```

Consequently the bilinear value cubes at each step and the accumulated
radial exponent obeys `a_(t+1)=a_t+3^t`, proving
`Phi^t(u,v)=c^a_t (u,v)` and `B(Phi^t(u,v))=c^(3^t)` in every characteristic.
Here `/2` is ordinary integer division in the exponent; no inverse of two is
used in the field.

For `c!=0` of order `r=3^a s`, equality of epochs `t` and `t+l` is
equivalent to

```text
r divides 3^t (3^l-1)/2.
```

Since `3` never divides `3^l-1`, the exact entry time is `a`.  At that time
the least positive `l` satisfies `s | (3^l-1)/2`, equivalently
`2s | 3^l-1`; the period is therefore `ord_(2s)(3)`.  A nonzero null pair
maps directly to zero, while zero is fixed.  Full orbit traversal in the
review boxes, including `q=19` where `A=2`, confirms the exact tails and
periods.

For a positive-time target `(x,y)` with nonzero value `d`, a source with
initial value `c` must equal `c^(-a_t)(x,y)`.  Its bilinear value is `c`
exactly when `c^(3^t)=d`.  Hence the fibre size is the cyclic-group root
count `g_t=gcd(3^t,q-1)` on the corresponding power subgroup.  A nonzero
null target is unreachable, and all `Z` points of the null cone map to zero
at every positive time.  This reasoning is unchanged for nonsymmetric
forms.

Every nonzero bilinear level has
`Q=q^(m-1)(q^m-1)` points and the null cone has
`Z=q^(2m-1)+q^m-q^(m-1)`: for each nonzero `u`, the functional
`v -> B(u,v)` is onto.  If `q-1=3^A h`, the scalar values with exact
3-primary order `3^a` number `phi(3^a)h`; multiplying by `Q` and adjoining
the null cone gives the displayed tail census, including `A=0` and
characteristic two.  At one step the image consists of zero and the `Q`
pair targets above each cube value.  Since `Z>q-1>=g`, zero is the unique
maximum-fibre target.  The reviewer additionally confirms the same strict
maximum for every tested positive time.

## 3. Findings

### Critical

None.

### P180-A-M01 — “Every-time” fibre contract omits time zero

**Severity:** Major.  **Locations:** abstract; section title at line 135;
Theorem 3.1, lines 137–149; frozen theorem contract item 3.

The abstract and frozen contract promise every-time fibres, but the theorem
starts at `t>=1`.  This is not merely implicit in the displayed cases: at
`t=0` every target has exactly one predecessor, whereas the first case of
the positive-time display would assign `Z` to zero.  Therefore the existing
formula cannot be read at time zero.

**Mandatory repair:** add an explicit `t=0` identity-fibre clause immediately
before or inside Theorem 3.1, and state that the four-case `Z/0/g_t/0`
display is for `t>=1`.  Synchronize the abstract, narrative, plan,
claims/evidence, and self-QA so “every-time” has a literal meaning.  Add a
`t=0` target sweep to the author control.  Failure to close the frozen
all-time contract is a theorem-contract kill switch.

### P180-A-m01 — The positive-dimension hypothesis is unstated

**Severity:** Minor.  **Location:** opening definition, lines 52–57.

The manuscript never states `m>=1`, although `Q` contains `q^(m-1)` and the
strict maximum argument relies on the existence of nonzero null states.  The
zero-dimensional space is a legitimate nondegenerate bilinear space under a
common convention, so it should not be left to implication.

**Mandatory repair:** state `m>=1` and that `q` is a prime power at the
literal definition.  No formula then changes.

### P180-A-m02 — Paper-local internal subtraction omits the closest occupied mechanisms

**Severity:** Minor.  **Locations:** `main.tex`, lines 59–69;
`SOURCE_VERIFICATION.md`, lines 1–18.

The sequence-level firewall contains the needed audit, but the paper package
does not record it.  At minimum it should subtract P102/P103's scalar power-
map/rank-stratum engine and compare P125's formed-space state-gated pair map.
P171 is a Gram-word warning but not a literal collision.  The distinctions
are real: P180 freezes projective direction and has a multiplicative scalar
cube clock plus a null-cone fibre, whereas P125 uses a three-bit
quadratic/polar quotient with nonuniform `0/1/2` fibres and periods up to
four.  Still, scalar power clocks and formed-space counting cannot be counted
again as separation credit.

**Mandatory repair:** add a compact internal-collision table/paragraph to
the paper-local owner ledger and synchronize the contribution ceiling in the
manuscript/support files.  Preserve `OWNER_AMBER`; a noncollision is not a
novelty finding.

## 4. Accepted hostile checks requiring no theorem change

- **Nonsymmetric forms:** every proof step uses only bilinearity and
  nondegeneracy.  Literal nonsymmetric invertible Gram matrices over prime and
  extension fields reproduce all formulas.
- **`ord_(2s)(3)`:** the factor two is necessary at pair level.  Replacing it
  by `ord_s(3)` would already fail for a value of order two over `F3`.
- **Null cone:** zero has exactly `Z` positive-time predecessors and every
  other null target has none.
- **Characteristic two:** `a_t` is an integer exponent, so no division by two
  occurs in the field.  `F2`, `F4`, and `F8` checks pass.
- **`A=0`:** all nonzero-value states are recurrent; the nonzero null cone
  still supplies tail one, so the sharp maximum is one.
- **Unique maximum:** `Z>q-1>=g` is strict for every `q>=2,m>=1`.

The author claims ledger transparently says its own finite control is only
over prime fields and symmetric dot products.  That is an evidence-coverage
limitation, not a proof defect; the present independent control supplies
direct pressure on the omitted axes.

## 5. Primary-source and owner audit

The primary records confirm that Colón-Reyes et al. treat monomial finite
dynamical systems, Konyagin et al. treat functional graphs of univariate
polynomials, and Qureshi–Reis treat power maps over finite groups.  The last
source directly owns the scalar power-map functional graph after reduction;
none of these sources was found to state the literal bilinear radial pair map
with the null-cone lift.  The Konyagin citation should continue to be
described only as broad univariate polynomial-functional-graph context, not
as ownership of multivariate polynomial maps.

The reopened literal searches produced no direct owner.  This remains a
bounded non-hit, not novelty or freedom-to-operate evidence.  Because almost
the entire nonzero-value clock reduces to the classical power map, the
residual remains owner-thin and `OWNER_AMBER / HOLD_EXTERNAL` is mandatory.

## 6. LaTeX, anonymity, artifacts, and status

- The settled PDF is three A4 pages, visibly Anonymous, with blank
  title/author/creator/producer metadata.  No compile was performed here.
- `main.pdf` and `main_round0_original.pdf` are byte-identical with SHA-256
  `3051dc087aa5c26bb2bcc69e363af75918fe51797dd509161979656fb8ecb248`.
- The settled pass is free of unresolved references/citations; first-pass
  warnings in archived logs are expected.
- The paper directory has no `SHA256SUMS`; adding a non-self-referential
  manifest is recommended during repair if required by the round contract.
- No wording authorizes posting, submission, or external circulation.

## 7. Kill switches and disposition

Kill or withdraw if the `t=0` contract is left inconsistent, if a direct or
conjugate owner is found, or if the retained contribution is described as a
new power-map theory rather than the literal pair-level lift.  The positive-
time mathematics survives the hostile re-derivation.  Close M01 and the two
minor scope/ownership items, then proceed to delta review under
`HOLD_EXTERNAL`.

**Reviewer assertions:** 243,393.  **Canonical replay:** byte-identical twice.

## Round-1 delta disposition — accepted

The superseding repaired source at SHA-256
`529bd4c0c091d3932c35de0b1ac8a6d347b3c65a838738bccfc1167207929991`
and PDF at
`d0b08ddc5de6a91a120282d6c31dcc56ca67c1bfdc5202d68b24a22335c80b59`
close P180-A-M01, P180-A-m01, and P180-A-m02. The time-zero identity fibre,
positive-time case split, prime-power/positive-dimension hypotheses,
P102/P103/P125/P171 subtraction, owner ceiling, characteristic-two wording,
Round-1 receipts, anonymity, and `17/17` paper manifest all pass. Two new
fresh-process Reviewer-A replays again matched the canonical at 243,393
assertions each; the author control matched at 770,697 assertions.

**Delta decision:** `ROUND1_DELTA_ACCEPT / THEOREM_ACCEPT / HOLD_EXTERNAL`.  
**Post-delta open findings:** `0 Critical / 0 Major / 0 Minor`.

The original verdict above is retained as the historical Round-0 review;
the formal evidence ledger is `DELTA_ACCEPTANCE_TEMPLATE.md`.
