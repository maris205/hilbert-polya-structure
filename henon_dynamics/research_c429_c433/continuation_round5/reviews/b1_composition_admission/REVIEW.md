# R5 B1 — CGR5 independent-contract admission audit

2026-09-09 UTC. NONAUTHOR closest-source/substantiality review.
Assigned scope: the original frozen CGR5 contract and B3 proof, conditional
on E1's separate mathematical audit. No mathematical program was run.

## 1. Decision

**Recommendation: retain CGR5 as a useful extension of GR5, but do not
admit it as a fourth independent paper contract on the current evidence.**

This is a substance/collision decision, not a mathematical rejection.
The arbitrary-word theorem is genuinely stronger than the *statement* of
single-factor GR5. It is not a direct invocation of that statement outside
its domain. Nevertheless, after subtracting the *proof* of GR5, the
remaining work consists of verifying the same pure-leading-form interface,
retaining its two independent scales, duplicating the centre search, and
applying the same determinant-module obstruction. The examples instantiate
the resulting extra freedom; they do not supply a distinct classification
mechanism or a separately established substantial question.

Status separation:

- Complete stated family and model classification: retained, not weakened.
- Mathematical correctness: E1's independent audit is the controlling gate;
  this review does not duplicate a full mathematical PASS.
- Closest external source: bounded subtraction adequate; no checked exact
  external collision established.
- Repository independence from GR5/C426: insufficient for a separate paper.
- Admission recommendation: AUXILIARY EXTENSION / NOT AN INDEPENDENT CONTRACT.
- Actual admission, evaluator grades and publication decisions: coordinator only.

No result is being promoted because a fourth seat is vacant. Conversely,
this conclusion does not say that short proofs or generalizations can never
be substantial. Section 6 evaluates the strongest affirmative case before
explaining why the present package does not clear this batch's independence
gate. A mathematically passing E1 review would certify the extension, not
erase the separate admission finding.

The C2 exact-spectrum supplement is expressly outside this review. The
coordinator confirmed that it is not part of CGR5 and that there is no
contract expansion. Its volume, partial results and conjectures are not
counted toward CGR5 substance.

## 2. Exact question audited

Let $K$ be any number field, $R=\mathcal O_K$, and
$$
F=H_r\circ\cdots\circ H_1,
\qquad H_i(x,y)=(y,f_i(y)-a_i x),
$$
with every finite $r\ge1$, $a_i\in K^\times$, and every
$f_i\in K[Y]$ of degree $d_i\ge2$. Set $D=\prod_i d_i$,
$\delta=\prod_i a_i$, and, writing $b_i=\operatorname{LC}(f_i)$,
$$
B=\prod_i b_i^{\prod_{j>i}d_j},\qquad
C=\prod_i(b_i/a_i)^{\prod_{j<i}d_j}.
$$
The clock is one full application of $F$, not a factor clock. At each
finite place, every affine map over the original $K_v$ is allowed; globally,
one affine map over the original $K$ must work at every finite place.
No extension field, restriction to diagonal charts, factorwise-good
assumption, or individual-unit-Jacobian assumption is permitted.

Regular-good means integral forward and inverse models, preservation of
both degrees $D$, and disjoint geometric indeterminacy sets of their
reductions in the specified projective compactification. This is stronger
than integral coefficients or a unit total Jacobian alone.

The full requested output is:

1. Necessary and sufficient local existence, all failure branches, and all
   affine charts. If $k_x=-v(C)/(D-1)$ and $k_y=-v(B)/(D-1)$ are integral
   and $v(\delta)=0$, choose scales of these valuations. The two pure
   subleading coefficients give base centres
   $c_x^0=-\eta_x/(DC)$ and $c_y^0=-\eta_y/(DB)$; testing the
   $q_v^{2v(D)}$ pairs represented by
   $(c_x^0+(s/D)\alpha,c_y^0+(t/D)\beta)$ is exhaustive. Each test checks
   every coefficient of both full maps, including wild residue cases.
2. When a local chart exists, a unique rectangle is the two-sided bounded
   set, and all charts are its one left coset $S\operatorname{Aff}_2(O_v)$.
3. If every place passes, patch the centres and form the canonical module
   $I_x\oplus I_y$ with exponents $-v(C)/(D-1)$ and $-v(B)/(D-1)$.
   A global chart exists exactly when $I_xI_y$ is principal. Describe
   every global chart and its one integral-affine left coset.

This is a complete classification, not merely a sufficient criterion or
a list of examples. The negative admission recommendation leaves these
quantifiers intact. It does not replace CGR5 by a weaker positive contract.

## 3. Evidence read and binding pins

The reviewer read the complete frozen B3 theorem/proof and report, the
complete X2 scout, the original GR5 frozen contract, full GR5 proof and
independent review, and the actual C426 source sections on classification,
local rigidity, the finite local test, global models, examples and scope.
This comparison is not based only on abstracts or author summaries.

The active batch rules, selected research-review and research-lit skills,
and the Hénon batch skill/workflow were read. Current-team review is used
under the batch's explicit authority; no named external-model review was
performed or implied. The governing independence criterion is §2 of
[the Hénon workflow](../../../../../.agents/skills/henon-route-a-batch/references/WORKFLOW.md).

Inputs, repository-relative:

| Input | SHA-256 |
| --- | --- |
| continuation_round5/b3_composition_good_models/PROOF_PACKAGE.md | 3f810fa619ee61805ffd236514300844372d1dc5fca5215d8ff0049db31fcc4c |
| continuation_round5/b3_composition_good_models/REPORT.md | 9508495d93d76839777efb2ac028afbb1557588d98db0b18df91653586870b92 |
| continuation_round5/x2_arithmetic_replacement/REPORT.md | 94d22d60b0def90a36fec3141915802009eda1418c8033b75b41242d0b9db471 |
| research_c424_c428/continuation_round5/arithmetic/PROOF_PACKAGE.md | 165f262916ae4cebaee51202fabbb9292c942942573c969de40b3bbbe58b46cb |

The first three paths are under `henon_dynamics/research_c429_c433/`;
the last is under `henon_dynamics/`. B3's final report incorporates only
the disclosed rendering cleanup relative to the earlier report pin.
Hash agreement is integrity evidence, not an additional proof check.

## 4. Exact internal subtraction: proof, not just theorem

Single-factor GR5 already classifies all local and global affine good
models over every number field, in every residue characteristic, with the
same regular-good definition. Its conclusion has a common scale and
centre, hence $I\oplus I$ and the square class $[I]^2$.

The crucial comparison is the intermediate stage of its proof. Before
using a single factor's linear coordinates, GR5 already obtains
$$
A=\operatorname{diag}(s,t)U,\qquad U\in\mathrm{GL}_2(O),
$$
from primitive rows of $A$, the two pure-power top forms, retained degrees,
and disjoint reduced indeterminacy points. Only *after* this step do the
single-factor linear coordinates force the two scales and centres to agree.
Thus CGR5 does not newly discover the two-row lattice mechanism.

| CGR5 component | Earlier owner and precise increment |
| --- | --- |
| Full-word degrees and $F_D=(0,By^D)$, $(F^{-1})_D=(Cx^D,0)$ | The new word-interface verification is elementary induction. It makes GR5's existing top-form argument applicable with two independent constants. |
| All-affine rectangle rigidity, §2 | The primitive-row argument is the GR5 argument before its additional single-factor identification. Keeping $s,t$ independent removes that identification; it does not replace a failed rigidity proof with a new one. |
| Two finite centre searches, §3 | The pure subleading Taylor coefficient bounds each centre in exactly the direction already used for the old scalar centre. Two copies and the full expanded coefficient tests cover the extra freedom. |
| Unique two-sided bounded rectangle, §4 | Good-reduction escape/filled-ball structure is classical; CGR5 uses the full forward/inverse top forms to apply it to the normalized word. |
| Centre patching, §5 | Apply the old additive approximation argument independently to the two coordinates. No new simultaneous obstruction remains for translation. |
| Product obstruction and all global charts, §6 | The same rank-two module problem is now $I_x\oplus I_y$ instead of $I\oplus I$. Steinitz gives $[I_xI_y]$ in place of $[I]^2$; the explicit two-generator matrix is the standard constructive sufficiency argument. |
| Arithmetic and boundary examples, §7 | They are genuine discriminators of the broader statement, but instantiate the expected independent-scale freedom and factor-presentation caveat. They do not alter the classification proof. |

One can formulate the shared interface without a Hénon factorization:
an automorphism and inverse of common degree $D\ge2$ whose degree-$D$
parts are $(0,By^D)$ and $(Cx^D,0)$. After B3 §1, §§2–6 use this interface,
the two selected subleading coefficients, and the classical lattice facts;
they do not use a new interaction between word factors. This is a concrete
mechanical-merger argument, not merely a complaint about related titles.

In particular, the product ideal is not a new *type* of global obstruction.
It is the determinant class of the same rank-two model lattice, already
identified in GR5. The old square rule reflects equality of its two summands,
not a distinct global principle that the new result overturns.

## 5. Closest external sources and bounded ownership check

The following passages were checked in primary sources. This audit does
not claim that an entire unexamined literature has been excluded.

- Kawaguchi, *Local and global canonical height functions for affine space
  regular automorphisms*, Definition 4.1 and Propositions 4.2–4.3, own the
  regular-good convention and good-reduction Green/norm mechanism.
  Their hypotheses cover general regular automorphisms, so the filled-ball
  argument cannot be advertised as new merely because the map is a word.
  Those checked results do not themselves give this all-affine finite
  coefficient/ideal classification.
  [Primary publisher PDF](https://msp.org/ant/2013/7-5/ant-v7-n5-p08-s.pdf).
- Bruin–Molnar, *Minimal models for rational functions in a dynamical
  setting*, Propositions 2.10/2.12, §3 including Algorithm 3.8, and
  Proposition 6.3/Example 6.4, are antecedents for affine-versus-projective
  model distinctions, finite valuation/translation searches and ideal
  obstructions. Their rational maps are on $\mathbf P^1$; their
  $\mathrm{Aff}_2$ notation is not the affine automorphism group of
  $\mathbf A^2$. This is ownership of ingredients, not an exact Hénon-word
  theorem collision.
  [Primary author text](https://arxiv.org/html/1204.4967).
- Petsche–Stout, *Global minimal models for endomorphisms of projective
  space*, Theorem 1, Proposition 6, Lemma 7 and the final patching proof,
  own the relevant integral-stabilizer/lattice-patching template. Their
  PID and projective-morphism hypotheses do not directly settle arbitrary
  $\mathcal O_K$ or a Hénon compactification with indeterminacy. This scope
  difference does not make lattice patching a new CGR5 mechanism.
  [Primary author text](https://arxiv.org/html/1303.5783v1).
- Allen–DeMark–Petsche, §1.1 and Theorem 11 with proof, classify the
  unit-ball regime for their normalized quadratic family over complete
  locally compact fields of odd residue characteristic. This is a
  narrower antecedent to filled-set rigidity, not the all-word model
  criterion. [Primary author text](https://arxiv.org/html/1610.04271v3).
- Lamy, *Tame polynomial automorphisms*, §4.1–4.2, considers valuations
  vanishing on nonzero field constants. Those weighted-degree valuation
  statements are not finite-place valuations extending a nontrivial
  valuation of $K$, and the checked stabilizer statements do not supply
  CGR5. [Primary author text](https://arxiv.org/html/2609.05655v1).

The main reviewer personally checked the listed statements and decisive
proof passages; for Kawaguchi Proposition 4.2 the actual read covered its
statement and relevant proof portions, not a claimed new independent
verification of every line. The complete source ledger and additional
Lee–Silverman/open-problems boundaries were read in X2's report. Those
additional sources are not falsely recorded as this reviewer's full-text
primary reads.

Three targeted searches concerned Hénon compositions and affine good
models, Hénon good reduction with ideal/composition terms, and polynomial
automorphism good-reduction lattices. They produced no additional checked
exact theorem collision. Local-library inspection did not identify a
relevant accessible specialist collection; primary web retrieval was used.
No private manuscript was uploaded. X2's broader search ledger is separate
evidence, not a query count reproduced as this reviewer's work.

The source conclusion is deliberately limited: the displayed arbitrary-word
classification was not found verbatim in the checked external sources.
That does not establish worldwide priority, nor does it defeat the closer
internal proof-template collision in §4.

## 6. Strongest affirmative case, then adjudication

The strongest argument **for** separate admission is not a superficial
increase in parameters:

1. The family is every finite word, with arbitrary coefficients and all
   affine charts over the original fields. Factors can individually have
   bad Jacobian valuations while the whole word is good.
2. The classification is exhaustive, including wild places, all charts
   and a global existence obstruction. It is not a fixed-length census.
3. The two local directions need not define the same ideal class. The
   order-three example has nonprincipal classes $[P]$ and $[P]^2$ whose
   product is principal; a mixed global model exists although a diagonal
   global model does not. Another example produces a genuine rectangular
   obstruction. The first example is not affine-conjugate to a single
   generalized Hénon factor, so it cannot be dismissed as merely an old
   map written twice.
4. A complete theorem can be substantial even when its proof is short or
   reuses known methods. No artificial demand for a wholly new technique
   is appropriate under workflow §2.

These points establish genuine mathematical value and a proper enlargement
of the domain. They do not, on the present package, establish a sufficiently
independent paper-sized advance beyond C426:

- The new family reaches the already-proved intermediate two-scale
  normal form by the same argument. The additional single-factor equality
  is simply no longer imposed. This is precisely the natural generality
  of the existing local proof, not an unrelated hard case resolved by a
  new bridge.
- Full coefficient expansion is a legitimate exhaustive test, but it
  absorbs all factor cancellations without producing a new structural
  classification of those cancellations. The word length does not
  introduce another theorem-level mechanism after the leading forms.
- Independent coordinate ideals make inverse ideal-class cancellation
  inevitable once freeness is tested by the determinant. The order-three
  mixed example confirms that the extension is proper, but its arithmetic
  conclusion is the expected specialization of the old module principle.
- The telescoping example disproves factorwise Jacobian testing. It is
  important for guarding the correct contract, but a factor presentation
  of a good full map is not itself an additional good-model classification
  result. Likewise, wild centre representatives validate exhaustiveness,
  not an independent paper question.
- The package closes the same affine good-model classification program
  in the natural pure-leading-form scope of its previous proof. It does
  not by itself close LG4, WM6, a new target-arithmetic bridge, or a distinct
  composition interaction problem. This is not a requirement that every
  admissible paper solve those other problems; it identifies what this
  package actually adds after the existing result has been deducted.

On balance, the new theorem is best retained as a generalization/supplement
to the GR5 line, rather than counted again as an independent fourth paper.
This is a reasoned admission judgment, not a claim that there is a formal
mathematical test that forbids all other editorial judgments.

## 7. Findings, required disposition, and boundaries

**S1 — Independent-substantiality gate not met.** This is the one admission
finding. The exact repair is a classification decision: preserve the
original CGR5 proof and its eventual E1 certification as an auxiliary
extension, and do not increment the independent-paper count on this basis.
No cosmetic wording change, larger table, longer word example or additional
repeat review can repair this finding. This audit does not request a new
candidate or authorize an expansion of the theorem contract.

**Mathematical must-fixes from this scoped audit: none asserted.** That is
not a full independent mathematical PASS; E1 owns that separate question.
The reviewer found no reason to weaken the advertised family in order to
make the admission judgment. Any E1 correction must be evaluated on its
actual affected theorem, not assumed resolved by this report.

**Source must-fixes: no additional missing primary citation identified.**
The explicit credit to the GR5 primitive-row argument, classical escape,
finite-search antecedents, CRT and Steinitz must be retained in any later
presentation. Exact external non-collision is not a positive substance
certificate.

The original GR5/C426 package is sealed and remains unchanged. Calling the
new work an extension does not authorize editing that sealed paper: keep
the new proof in its present continuation directory, with the outcome
recorded by the coordinator. No manuscript, numbering, evaluator, index,
Git or release file was changed by this reviewer.

CGR5 is source arithmetic. It establishes no target Euler factor, root
number, automorphy, Hilbert–Pólya realization or Route-B entry.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force. LG4 and WM6 remain open at
their original quantifiers, independently of the useful good-model result.

## 8. Mathematical-review readback

Pending E1's final report at the time of this initial writing. The present
negative independent-contract recommendation does not depend on whether
E1 ultimately certifies the current proof or requires a mathematical repair.
The eventual readback must pin the actual E1 report and the reviewed proof,
and distinguish that gate from this report's admission recommendation.

### Final readback — mathematical gate closed, admission unchanged

The initial pending status immediately above is superseded by this readback.
I checked the actual E1 report's verdict, frozen scope, author-file pins,
antecedent/applicability statement and final disposition. This was a bounded
readback of the separate review, not another full mathematical review.

Bound input: [E1 REVIEW.md](../e1_composition_good_models/REVIEW.md),
SHA-256 `3e24744c7650931ed2348d5f2871258355027ca95e6dce0ce1bae8fe6e479f5f`.
The actual file has **370 lines** according to the read-only line count;
this receipt records the file rather than a conflicting handoff count.
The B3 proof and final report hashes were also rechecked and remain exactly
the two pins in §3.

E1's verdict is **PROVABLE AS STATED, with zero mathematical or
source-applicability must-fixes**. Its audited scope is the full original
all-number-field, arbitrary-finite-word, all-affine local/global contract,
including wild places, possibly bad individual factors, all charts, the
unique local rectangle, patched translations and the product-ideal
criterion. No author hypothesis or proof change was required. E1 explicitly
separates this correctness verdict from independent substantiality and
does not assign admission or a paper count.

Accordingly, the final combined status is: **mathematically proved and
independently checked auxiliary extension; NOT recommended as a fourth
independent contract**. E1 closes the previously pending mathematical gate.
It does not close or contradict finding S1, which concerns the already
deducted GR5 proof mechanism. The coordinator has separately communicated
agreement with the auxiliary disposition; this file does not itself change
the batch's admission record. No source/proof expansion or author edit was
performed for this readback.
