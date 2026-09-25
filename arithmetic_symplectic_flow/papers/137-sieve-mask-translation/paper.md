# A sieve-derived involution carries the prime word but has an undifferentiated orbit spectrum

**Paper ID:** 137-sieve-mask-translation.  
**Candidate ID:** ANG-20260914-SBT01.  
**Date / status:** 2026-09-14; STOP — UNIFORM TWO-CYCLES; ORDINARY PRODUCT DIVERGES.  
**Evidence:** exact elementary proofs, including positive arithmetic and return controls.  
**Route state:** broadened T0--T3 scoped audit; no classical Route coordinates;
Route B NOT INVOKED.

## Abstract

Evaluate the causal binary sieve on the constant-one word, and use its output
as a fixed translation of the compact binary product. The displacement is
exactly the full prime indicator, derived from divisibility without a supplied
prime table. The same continuous invertible action has only primitive
two-cycles. This is a genuine positive control for coexistence of an exact
prime-side observable and closed orbits in one broadened owner. It does not
give prime-selective periodic data: every orbit has the same displacement and
unit-roof length, there are continuum many primitive packets, and the frozen
ordinary unweighted product fails its elementary convergence test. A conjugacy
to a two-point flip times an identity isolates the dynamical degeneracy, but
does not erase the arithmetic observable, since that conjugacy itself uses
the sieve output. The candidate stops without changing its roof or quotient.

## 1. Frozen identity and lineage

The [version-1 card](candidate-card.md) was frozen before the audit. Let

\[
X=\{0,1\}^{\{2,3,\ldots\}},\qquad
c_n=\prod_{\substack{2\leq d\leq\lfloor\sqrt n\rfloor\\d\mid n}}(1-1),
\qquad T(x)=x\mathbin{\mathrm{XOR}}c.
\]

The empty product is one, and X has its product topology. This is exactly
the evaluation c=G(1) of the formula in
[050](../050-causal-binary-sieve-fixed-point-screen/paper.md), but T is a new
map, not an iterate or a claimed reversible realization of G.

The precise early [prior-work arrow](../../docs/prior_work/README.md) is:
prime/composite symbolic exclusion by divisibility, followed by evaluation
at the constant-one candidate word, followed by reversible translation with
the source as a spatial displacement.

This is a stated deformation from state-dependent arithmetic feedback to a
fixed arithmetic forcing. The loss of feedback is part of the audit, not
hidden inside a claim of conjugacy to the sieve. No Logistic, Hénon, or
finite-dimensional symplectic realization is supplied.

| Owner field | Frozen object | Result |
| --- | --- | --- |
| Carrier / action | Compact binary product X and T | Homeomorphism |
| Broadened carrier | Transformation groupoid X crossed with Z | Same T action, with its full isotropy retained |
| Arithmetic inputs | Integer divisibility and constant-one seed evaluation | No prime table, selected prime parameter, or zero input |
| Distinguished observable | D(x)=x XOR T(x), with integer labels retained | Exactly the prime indicator at every state |
| Roof and flow | Unit roof; (x,1) identified with (Tx,0) | Complete suspension; no clock substitution |
| Packets | All primitive T-orbits modulo cyclic phase | Continuum many; every one has two states |
| Repetition law | Same unit clock on the same suspension | Primitive length 2; r-fold length 2r |
| Analytic proposal | Ordinary unweighted primitive product | Diverges for every positive real s |
| Operator / quantum owner | Not supplied | OPEN / NOT SUPPLIED; none borrowed |
| Classical symplectic fields | NOT APPLICABLE | No classical gate claimed |

The Z action is not faithful: T squared is the identity, so every point has
isotropy 2Z. It is not silently replaced by a Z/2 action, an effective
groupoid, or a single chosen orbit.

## 2. Question and claim boundary

Can a spatial, sieve-generated observable avoid the temporal nonreturn
obstruction while remaining visible in the same object's closed-orbit data?

The answer separates three claims. Exact arithmetic displacement is
established; closed orbits of the same object are established; a
prime-selective orbit spectrum and the frozen ordinary product are not
obtained. The last conclusion does not negate either positive result.

In particular, no theorem here says that a labelled observable ceases to be
arithmetic under a topological conjugacy. No theorem excludes all weighted,
measured, regularized, or operator-valued constructions on another frozen
owner. No such construction is supplied for this card.

## 3. Exact proofs

### Proposition 1 — Arithmetic displacement and topological ownership

For every integer n>=2, c_n is one exactly when n is prime. The map T is a
fixed-point-free homeomorphism with T squared equal to the identity, and
D(x)=c for every x in X.

**Proof.** If n is prime there is no divisor in the product, so c_n=1.
If n is composite, write n=ab with 2<=a<=b; then a<=sqrt(n), and the
product contains a zero factor. Thus c_n=0. This is the elementary
divisibility proof, not an imported prime indicator.

Each output coordinate of T depends only on the corresponding input
coordinate and its fixed c_n, so T is continuous in the product topology.
Binary addition of c twice cancels, giving a continuous inverse equal to T.
Because c_2=1, no x can satisfy T(x)=x. The identity D(x)=c follows directly
by coordinatewise cancellation. QED.

The transformation groupoid has arrows (x,k) from x to T^k x, with topology
X times discrete Z. Each k slice is a source and range chart, making it a
locally compact Hausdorff étale groupoid. Nontrivial isotropy is allowed in
this category and has not been removed to improve the packet count.

### Proposition 2 — Full packet ledger and the clock

Every T-orbit has least period two. Its unit-roof suspension is complete,
every primitive flow orbit has length two, and its r-fold traversal has
length 2r. There are continuum many primitive orbits.

**Proof.** Proposition 1 gives T squared equal to the identity and excludes
fixed points, proving exact primitivity. For a representative (x,u),
0<=u<1, time t is represented by

\[
\bigl(T^k x,u+t-k\bigr),\qquad k=\lfloor u+t\rfloor.
\]

This exists for every real t. A return at the same height requires integer
elapsed time; its least positive value is the least positive period of x,
namely two. Repeated traversals add the same roof lengths.

Every two-cycle has exactly one point whose coordinate at 2 is zero.
Consequently the packet set is in bijection with
\(\{x\in X:x_2=0\}\), a full binary product over n>=3, of cardinality
continuum. This section is used to count all packets, not to retain only one
of them or discard their multiplicity. QED.

### Proposition 3 — Generic flip dynamics, with the observable tracked

Define

\[
H(x)=(b,z),\qquad b=x_2,\qquad
z_n=x_n\mathbin{\mathrm{XOR}}(c_n b)\quad(n\geq3).
\]

This is a homeomorphism from X to
\(\{0,1\}\times\{0,1\}^{\{3,4,\ldots\}}\), and

\[
H T H^{-1}(b,z)=(b\mathbin{\mathrm{XOR}}1,z).
\]

**Proof.** The inverse is x_2=b and
x_n=z_n XOR (c_n b). Both directions are continuous coordinate maps.
Under T, b changes to b XOR 1 and

\[
(x_n\mathbin{\mathrm{XOR}}c_n)
\mathbin{\mathrm{XOR}}\bigl(c_n(b\mathbin{\mathrm{XOR}}1)\bigr)
=x_n\mathbin{\mathrm{XOR}}(c_n b)
\]

in the binary field, so z remains fixed. QED.

Exactly the same construction works for any fixed binary mask d with d_2=1.
It follows that period data alone cannot distinguish the sieve mask from
these controls. It does NOT follow that the integer-labelled arithmetic
system with observable D is identical to an arbitrary mask system with its
observable retained: H contains c, and D transported through H remains c.
The arithmetic content survives as a static, identical readout on all
packets. The card supplies no rule partitioning those packets into a
distinguished prime-specific family, and the frozen lengths offer no such
partition.

### Proposition 4 — Failure of the ordinary primitive product

For the complete primitive-packet set P, consider the frozen proposal

\[
Z(s)=\prod_{\gamma\in P}(1-e^{-sT_\gamma})^{-1}.
\]

It does not converge to a finite value at any real s>0.

**Proof.** By Proposition 2, every factor is the same number
a(s)=(1-e^{-2s})^{-1}>1. A finite subset of L distinct packets gives exactly
a(s)^L. The packet set contains arbitrarily large finite subsets, and these
products are unbounded as L grows. Thus the directed net of finite products
diverges; choosing only a countably infinite subfamily already gives the
same obstruction. QED.

This is an exact failure of the ordinary unweighted orbit product and its
usual right-half-plane starting construction, not a no-go theorem for every
notion of noncommutative or measured trace. Operators, a transverse measure,
weights, and a regularization are not part of the frozen proposal.

## 4. Controls and argument audit

| Claim and evidence | Strongest objection | Scoped resolution |
| --- | --- | --- |
| Proposition 1 derives the full prime displacement | The mask is fixed rather than recomputed through feedback | Correct: source-derived arithmetic is real, but dynamic generation and selective clock credit remain unresolved |
| Proposition 2 gives actual closed packets | A generic flip also has two-cycles | Correct: packet existence is positive, prime-selective period data are not established |
| Proposition 3 displays a generic flip form | The conjugacy uses the arithmetic mask | Correct: only the unlabelled dynamics are trivialized, not the retained arithmetic observable |
| Proposition 4 refutes the ordinary product | A different measure or regularization could be proposed | Such an object needs a fresh card; it is not evaluated or ruled out here |

Further controls are exact. A single-coordinate mask and the all-one mask
with d_2=1 have the identical period and full-multiplicity ledger. The zero
mask instead has only fixed points and is explicitly excluded from the
nonzero-mask comparison. A hypothetical roof chosen from a packet's
arithmetic label would change this card; none is inserted. No finite cutoff,
floating-point calculation, statistical fit, or Riemann-zero data is used.

The argument table applies the ARS claim-evidence-reasoning and
counterargument discipline to this bounded research note. It is not a full
ARS paper pipeline, a venue review, or a correctness certificate.

## 5. Gate assessment

| Gate | Evidence for ANG-20260914-SBT01 | Status and limitation |
| --- | --- | --- |
| T0 | Full continuous action, groupoid, roof and flow owned together | ESTABLISHED at the broadened type |
| T1 | Exact source-derived prime displacement; fixed unit clock | PARTIAL: labelled arithmetic established; fixed forcing is not a demonstrated prime-selective endogenous clock/packet mechanism |
| T2 | Complete primitive-packet classification and repetitions | ESTABLISHED, including continuum multiplicity and uniform lengths |
| T3 | Ordinary unweighted primitive product | Scoped FAIL by Proposition 4; operator NOT SUPPLIED |
| Classical A0/A1/A2 | No finite-dimensional symplectic base | NOT APPLICABLE |
| Formal Route coordinates | No formal evaluation performed | UNASSIGNED |
| Route B | Not evaluated | NOT INVOKED |

## 6. Decision and limitations

**Decision: stop this candidate; portfolio fork.** The planned packet audit
finds uniform two-cycles of continuum multiplicity, and the ordinary product
fails immediately. The positive coexistence result is retained: arithmetic
observation plus recurrence is possible here. It is insufficient for the
proposed analytic architecture.

No topology, mask, roof, packet quotient, operator, or normalization changed
during this audit. In particular, reducing the continuum of packets to a
chosen prime-indexed subset is not an admissible continuation of this card.
The broader question of an arithmetic feedback rule selecting a nondegenerate
packet structure remains OPEN. Neither this elementary example nor its
controls settle that question.

## Reproducibility and evidence

The [candidate card](candidate-card.md), [claim ledger](claim-ledger.md), and
[evidence record](evidence/README.md) carry all definitions and controls.
Propositions 1--4 are full proofs on the infinite carrier. They require no
numerical evidence or external analytic theorem.

Data availability: no acquired dataset; all mathematical inputs and proofs
are in this package. Ethics: no human or animal study or personal data.
Contributions: candidate construction, proof drafting and checking were
AI-assisted under the user's research direction; no human proof verification
is attested. Conflicts and funding: no declaration supplied by the user;
unknown rather than assumed absent. This is a local research record, not a
submission-ready manuscript.
