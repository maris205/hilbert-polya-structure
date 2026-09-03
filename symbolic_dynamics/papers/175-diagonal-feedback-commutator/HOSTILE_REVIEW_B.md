# Hostile Review B — P175

**Reviewer:** independent non-author / non-Review-A rederivation  
**Round reviewed:** byte-frozen author Round 1 (identical to Round 0)  
**Verdict:** `PROVABLE AS STATED / OWNER REFRAME REQUIRED`  
**Findings:** 0 Critical, 1 Major, 0 Minor  
**Lifecycle:** `HOLD_EXTERNAL` (unchanged)

## Frozen intake and independence

The reviewed inputs were frozen before this review:

```text
main.tex                    ba1436720a49b0667e168afd5f5e352efc657b82907af3a402ca36fd1cfa5eff
main.pdf                    32f296a1519fd598f0ef4c88bdbd0d655ff930b94e97eec42bd6f2b9ba1d1eba
main_round0_original.pdf    32f296a1519fd598f0ef4c88bdbd0d655ff930b94e97eec42bd6f2b9ba1d1eba
main_round1.pdf             32f296a1519fd598f0ef4c88bdbd0d655ff930b94e97eec42bd6f2b9ba1d1eba
references.bib              d134944049dac7f06c2f757292dd550df7fd03b529dc87862b14f6b2728f8bcf
verify_p175.py              9a9ff255e36262034d1012a1cb38f5ef7018a4579a80a8ee1153c10f00741b2a
verification_output.txt     f9169bb2d6ccfb304dee28409c3ed07e86ba597cc1862524bcc7f29d5a34eb25
P119 main.tex               b705827c4db387b7148a0fa2cad92e8b7166194137875fba8812dc4765c64017
```

The Review-B verifier imports no author, Review-A, or scouting code.  It
uses canonical sparse matrices decoded from integers and polynomial-quotient
finite fields, whereas the author and Review A use dense flat tuples.  The
proof below was rederived before comparison with their transcripts.

## Uniform theorem audit

### B-T1 — Square-zero feedback

For `D=Delta(A)`, direct multiplication gives

\[
 [D,A]_{ij}=(a_{ii}-a_{jj})a_{ij}.
\]

The diagonal of `Phi(A)` is therefore zero.  Consequently
`Delta(Phi(A))=0` and `Phi^2(A)=[0,Phi(A)]=0`.  This is a literal identity
over every field; it uses neither characteristic, diagonalizability, nor
the cyclic structure of the multiplicative group.

**Result:** theorem and boundary are correct.

### B-T2 — Every-target fibre and occupation mark

Freeze the prospective source diagonal `c=(c_1,...,c_n)`.  Each ordered
off-diagonal coordinate is governed independently by

\[
                 (c_i-c_j)a_{ij}=b_{ij}.
\]

It has one solution if `c_i != c_j`, `q` solutions if `c_i=c_j` and
`b_ij=0`, and no solution if `c_i=c_j` and `b_ij != 0`.  Thus `c` is
admissible exactly when it is a proper colouring of the undirected union
support `G_B`.  An admissible `c` leaves precisely

\[
 m(c)=\sum_{\alpha\in\mathbb F_q}n_\alpha(c)(n_\alpha(c)-1)
\]

ordered entries free and contributes `q^{m(c)}` sources.  Retaining the
monomial in the labelled occupation vector proves the marked coefficient
claim, not merely the aggregate fibre formula.

**Result:** complete and correct for every target.

### B-T3 — Image criterion, image count, kernel count, and maximum

All fibre summands are positive integers, so a zero-diagonal target is
reachable exactly when `G_B` has a proper `q`-colouring.  A chosen support
edge carries any nonzero ordered pair in `F_q^2`, independently giving
`q^2-1` labels, hence the image graph sum.  For `B=0`, grouping all
colourings by the labelled weak composition `(r_alpha)` gives the stated
kernel formula.

For every nonzero zero-diagonal `B`, `G_B` has an edge and its proper
colourings are a strict subset of all colourings contributing positively
to the zero fibre.  Nonzero-diagonal targets have empty fibre.  Therefore
zero is the unique global maximizer, including `n=1`.

**Result:** all four claims are correct.

### B-T4 — Complete rooted graph, all-time fibres, and zeta

Since `Phi^2=0`, `im Phi` lies in the set-theoretic zero fibre.  The root is
zero; the remaining `kappa_{n,q}-1` kernel states are exactly depth one; and
all `q^{n^2}-kappa_{n,q}` remaining states have nonzero first image and
depth two.  A nonzero depth-one state branches precisely when it belongs to
`im Phi`, giving `I_{n,q}-1` branch vertices and
`kappa_{n,q}-I_{n,q}` depth-one leaves.  Every source above a nonzero branch
is outside the kernel and hence a depth-two leaf.  This proves the
support-indexed branches and total mass identity.

For `n=1`, `Phi` is constant zero and the height is one under the paper's
root-at-depth-zero convention.  For every `n>=2`, two distinct diagonal
values and one suitable nonzero off-diagonal entry produce a nonzero image,
so height two is sharp.  Every iterate `Phi^r`, `r>=1`, has only zero fixed,
and therefore the Artin--Mazur series is `(1-z)^{-1}`.

**Result:** tree, all-time, and zeta package is complete and correct.

### B-T5 — The nonprime prime-power boundary

The proof needs only the following field facts: `c_i-c_j` is zero exactly
when the colours agree, and every nonzero difference is invertible.  It
does not identify `F_q` with integers modulo `q`.  The independent control
constructs `GF(4)`, `GF(8)`, `GF(9)`, and `GF(16)` as polynomial quotients,
checks their field operations, and then exhausts all matrices in the
feasible boxes.  In particular, the characteristic-two sign collapse does
not alter the scalar trichotomy or any exponent.

**Result:** the stated prime-power range is justified.

## Ownership and internal subtraction

### P119 is not a transferable-engine collision

P119 iterates the fixed-second-entry group commutator
`X -> X^{-1}J^{-1}XJ` on `U_n(q)`.  Its nonempty restricted fibres are
uniform centralizer cosets, and its temporal mechanism is lower-central
filtration descent of sharp height `n-1`.  P175 instead applies an additive
commutator on the full matrix space with a diagonal extracted anew from
each source.  Its fibres are nonuniform support-colouring sums and its
height is at most two.  The contrast is already made explicit and assigned
zero credit in P175.  No parameter or coefficient substitution carries the
P119 theorem into P175, so no P119 repair is required.

### The aggregate polynomial is an exact Potts specialization

The present text says only that `P_{G,q}` is “Potts-type” with a global
occupation interaction.  There is a stronger exact identity.  In the
standard `q`-state spin representation of the multivariate Potts partition
function on the complete graph `K_n`, set

\[
 v_{ij}=\begin{cases}
 -1,&\{i,j\}\in E(G),\\
 X^2-1,&\{i,j\}\notin E(G).
 \end{cases}
\]

Then

\[
 Z^{\rm Potts}_{K_n}\!\left(q,\{v_{ij}\}\right)
 =\sum_{c:[n]\to\mathbb F_q}
   \prod_{i<j}\bigl(1+v_{ij}{\bf1}_{c_i=c_j}\bigr)
 =\mathcal P_{G,q}(X;\mathbf1).
\]

Indeed, a monochromatic support edge receives factor zero, while each
monochromatic nonedge receives `X^2`; under properness all equal-colour
pairs are nonedges and their number is `m(c)/2`.  At `X=q` this is exactly
the unmarked P175 fibre, not merely an analogy.  Sokal's multivariate
Potts/Tutte spin formula is therefore a direct formal owner for the
partition-function side of the reduction.

The unweighted labelled occupation enumerator is also the truncation to
`q` variables of Stanley's chromatic symmetric function

\[
 X_G(z_1,\ldots,z_q,0,\ldots)
 =\sum_{c\in\operatorname{Col}_q(G)}\prod_i z_{c_i}.
\]

P175's marked polynomial is obtained coefficientwise by multiplying the
monomial of occupation `r` by `X^{sum r_alpha(r_alpha-1)}`.  This does not
invalidate any fibre theorem, but it means that the occupation inventory
itself also has a precise prior owner rather than only a generic
“colouring” owner region.  Primary records checked for this decision are:

- Alan D. Sokal, “The Multivariate Tutte Polynomial (Alias Potts Model) for
  Graphs and Matroids,” *Surveys in Combinatorics 2005*, 173–226,
  <https://arxiv.org/abs/math/0503607>;
- Richard P. Stanley, “A Symmetric Function Generalization of the Chromatic
  Polynomial of a Graph,” *Advances in Mathematics* 111 (1995), 166–194,
  <https://doi.org/10.1006/aima.1995.1020> and the
  [author PDF](https://math.mit.edu/~rstan/pubs/pubfiles/100.pdf).

External-field Potts formulations provide further nearby language, but are
not needed to establish the exact unmarked identity or the Stanley
occupation owner.  No bounded-search miss is used as novelty evidence.

## Finding and mandatory repair

### P175-B-M01 — exact Potts / chromatic-symmetric ownership is under-subtracted

**Severity: Major.**  This is a claim-boundary and provenance defect, not a
mathematical error.  The fibre formula, image criterion, and functional
graph all remain valid.  However, calling the aggregate sum merely
“Potts-type” obscures an exact standard specialization, while the current
residual language can be read as retaining contribution credit for the
occupation-weighted partition object.

Before any circulation, the author must:

1. display the complete-graph Potts specialization above and assign the
   partition-function identity itself zero standalone contribution credit;
2. cite and subtract Stanley's chromatic symmetric function for the
   proper-colouring occupation enumerator, explaining the deterministic
   coefficientwise `X^{sum r_alpha(r_alpha-1)}` transform;
3. update `main.tex`, `references.bib`, `SOURCE_VERIFICATION.md`, and
   `CLAIMS_EVIDENCE.md` consistently; and
4. narrow the residual claim to the literal matrix-to-support reduction,
   its use for every target of this feedback map, and the consequent rooted
   functional-graph census.  Do not claim the Potts or occupation
   polynomial as a new combinatorial object.

The repair must leave `HOLD_EXTERNAL` in force.  A direct-owner search for
the literal feedback self-map remains incomplete, so this review neither
certifies novelty nor authorizes external circulation.

## Independent executable receipt

The independent verifier at
`docs/papers172_176_sequence/reviews/p175_review_b/verify_review_b.py`
reports:

```text
ASSERTIONS 2559272
RESULT PASS_MATHEMATICS_OWNER_REFRAME_REQUIRED
```

It exhausts twelve matrix boxes and every target therein, including four
genuine nonprime fields, and separately checks the exact Potts identity and
the occupation-profile transform.  Two fresh deterministic processes were
byte-identical to `CANONICAL.txt`.  Finite enumeration is only a falsifier;
the all-parameter conclusions above rest on the uniform scalar-equation
derivation.

## Final verdict

`PROVABLE AS STATED / OWNER REFRAME REQUIRED`: 0 Critical, 1 Major,
0 Minor.  No manuscript or PDF byte was changed during Review B.

## Author-response delta ledger — Round 2 candidate

**Delta checked:** 2026-09-03 UTC  
**Mode:** read-only acceptance; no manuscript or PDF edit by Reviewer B  
**Delta verdict:** `MATHEMATICAL_TEXT_CLOSED / PACKAGE_SURFACES_STILL_OPEN`  
**Lifecycle:** `HOLD_EXTERNAL` (unchanged)

The inspected Round-2 candidate is frozen at:

```text
main.tex                    d660c01649ba648ab2cd915ab6bceacfef695789eb7856c1c7823dbce95cceb5
references.bib              26aad95c02247ec87c979060293edd457590af4cceecbc40b30d4a23640f8f78
main.pdf / main_round2.pdf   321d59b8b66cc2aef22296f214ee0d0072652c86d53293714599b0e07ee4b703
main_round0_original.pdf    32f296a1519fd598f0ef4c88bdbd0d655ff930b94e97eec42bd6f2b9ba1d1eba
main_round1.pdf             32f296a1519fd598f0ef4c88bdbd0d655ff930b94e97eec42bd6f2b9ba1d1eba
```

The new PDF is four A4 pages, byte-identical to `main_round2.pdf`, with
blank author, creator, and producer metadata.  The final Round-2 LaTeX and
BibTeX logs contain no warning, undefined citation/reference, bad box, rerun
request, or fatal error.  The unchanged author verifier freshly matches its
canonical transcript (`2,111,465` assertions), and the Review-B control
remains canonical (`2,559,272` assertions).

| `P175-B-M01` acceptance item | Status | Evidence / remaining repair |
|---|---|---|
| Display the exact Potts specialization and zero-credit it | **CLOSED in manuscript** | Equation `eq:potts-owner` now evaluates the standard `q`-state Potts spin sum on `K_n` with activity `-1` on `E(G)` and `X^2-1` on its complement.  The following text correctly explains the zero factor and the `m(c)/2` monochromatic nonedges, and assigns the identity no standalone credit. |
| Cite/subtract Stanley for occupations | **CLOSED in manuscript and bibliography** | The DOI-verified Stanley 1995 record is present and cited.  The manuscript displays the `q`-variable chromatic-symmetric truncation and the coefficientwise multiplier `X^{sum r_alpha(r_alpha-1)}`. |
| Narrow the residual | **CLOSED in the theorem text; OPEN on package surfaces** | The introduction and concluding limitations now retain only the every-target matrix-to-support reduction and consequent rooted tree.  However, the current package-level `README.md`, `SOURCE_VERIFICATION.md`, and `CLAIMS_EVIDENCE.md` still carry their pre-review “exact conjunction” / “Potts-type” residual wording. |
| Update all named support files consistently | **OPEN** | `SOURCE_VERIFICATION.md` still says only “Potts-type” and explicitly says no identity is claimed; it has no Stanley record.  `CLAIMS_EVIDENCE.md` still lacks the exact specialization/occupation-owner subtraction and retains the old residual.  `README.md` and `SELF_QA.md` are likewise stale.  These files must be synchronized with Round 2 before the Major finding can be fully closed. |

Accordingly, the mathematical/source changes in `main.tex` and
`references.bib` satisfy the substance of the finding, and no new theorem
defect is present.  Nevertheless `P175-B-M01` remains **OPEN for package
consistency** at this checkpoint.  Once the supporting ledgers explicitly
record the exact Potts identity, Stanley occupation owner, zero-credit
assignment, and narrowed residual, a final read-only delta can mark it
`CLOSED`.  This open bookkeeping item does not justify any value upgrade;
`HOLD_EXTERNAL` remains mandatory.

### Final package recheck — `P175-B-M01 CLOSED`

The author subsequently synchronized every named claim surface and repaired
the exact package inconsistencies identified at the first checkpoint.  A
second read-only delta therefore changes the finding status to **CLOSED**.
The accepted additional locks are:

```text
SOURCE_VERIFICATION.md      807bdd8b3a20caf88bc62fd5a3aec712b5fced048b7084bf634e8579da712877
CLAIMS_EVIDENCE.md          1ea252a0a319c0bbd256b55d9a2990ba96d71c4584ce836a1d9935664a2e35d2
README.md                   11c8a91f3252566d91c3f4838a01ba3967bc7ca38b619aca9d76ad2c98cb145d
SELF_QA.md                  4fca4840d1356b57cdc4e7cfe3f2f4923304537818ba6f9d90c8f08af330bd67
NARRATIVE_REPORT.md         a8f90104851157390d7c35d1085f9e486a45354723c9c87a6f3505837c0b7b80
PAPER_PLAN.md               91560d101df8156dda151903bcffa1b5d9b347cfa91bcb662551baef7e08cace
IMPROVEMENT_LOG.md          1ac81211b5364251a2bb5c19cdcfc7f51d9db6ac767d3e137703382e61215eec
BUILD.md                    d0ec5bb9012c1ec5cb04972d4b919712b00d1a4b08bd5c95a370c734cf4c6d62
paper SHA256SUMS            9078b42fc87e1a76876132860f3837c270807263b9e365dee210ebd6f7c9fbde
```

In particular:

- `SOURCE_VERIFICATION.md` now labels its scope through Round 2, gives the
  exact Sokal specialization and Stanley occupation role, assigns both zero
  credit, and states the narrow matrix-to-support/tree residual;
- `CLAIMS_EVIDENCE.md`, `README.md`, `SELF_QA.md`, the narrative, and the
  plan now use the same owner subtraction and residual boundary;
- `README.md` correctly compares live `main.pdf` with `main_round2.pdf`, not
  the frozen Round-0 PDF;
- `BUILD.md` now labels the old three-page/source-hash block explicitly as
  the frozen author Round-0 receipt and separately records the four-page
  Round-2 candidate; and
- the live paper-local `SHA256SUMS` covers current Round-2 source/PDF,
  preserved Round 0/1 PDFs, verifier, and canonical output, with all eight
  entries passing.

There are now **0 open Critical, 0 open Major, and 0 open Minor** Review-B
findings.  No omitted repair or new mathematical inconsistency was found.
This closure accepts only the response to Review B: it neither upgrades the
scientific value assessment nor establishes novelty, priority, or freedom to
operate.  `HOLD_EXTERNAL` remains unchanged.
