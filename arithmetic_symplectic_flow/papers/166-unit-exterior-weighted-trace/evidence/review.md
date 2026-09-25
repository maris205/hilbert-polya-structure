# Bounded mathematical review — unit-exterior weighted trace

**Candidate ID:** ANG-20260915-UEW01  
**Date:** 2026-09-15  
**Candidate status:** STOP — LOCAL RANK-ONE SURVIVAL; FULL DEGREE-WEIGHTED ORDINARY TRACE UNDEFINED.  
**Review result:** Main arguments verified within the frozen scope; minor M1 ADDRESSED.  
**Calibration:** NOT_CALIBRATED.  
**Formal Route coordinates:** UNASSIGNED; Route B NOT INVOKED.

## Scope and actual review provenance

The reviewer read the complete frozen [candidate card](../candidate-card.md)
before the manuscript existed and independently derived the finite rank
selector, the infinite fixed-channel obstruction, and the fixed-smoothing
cutoff obstruction. The completed [paper](../paper.md), [package README](../README.md),
[claim ledger](../claim-ledger.md), and [evidence index](README.md) were then
read in full. This receipt reviews the actual manuscript, not only its
abstract or an author's reported outcome.

Relevant instructions, plan, current project entry, the
[168 scope](../../168-source-return-breadth-frontier/candidate-card.md),
and the complete mathematical arguments in
[146](../../146-localization-scaling-groupoid/paper.md) and
[158](../../158-localization-koszul-packet-audit/paper.md) were read.
The latter two serve as ownership and collision controls; their results
were not silently transferred to the new analytic contract.

The reviewer invocation is
/root/research_controller/unit_degree_weighted_trace/unit_exterior_trace_review.
It is separate from the author invocation but inherits the project context
and session model. The assignment exposed the proposed positive and negative
hypotheses; this was not manuscript-blind or hypothesis-blind review.
Pre-manuscript feedback about cutoff order and the meaning of closedness
was sent to the author. The final manuscript was reviewed after that feedback.

A further same-model, inherited-context, read-only invocation,
maximal_domain_readonly_check, separately checked only the maximal domain,
degree-one noncompactness, and all-rank unboundedness against the card and
actual Propositions 1--3. It wrote no files. Its domain observation was
independently checked by this reviewer and is disclosed as M1 below.
The main reviewer remains responsible for the full receipt.

This is model-assisted mathematical review, not human peer review, blind
review, a calibrated panel, a formal proof certificate, or evidence of
independent error processes. No external-model API, computation, external
dataset or source-dependent theorem lookup was used. ARS was used only for
bounded claim/evidence/counterargument separation, not a publication workflow.
No venue criteria were supplied: criteria_binding_unavailable.

## Criterion-bound findings

| Criterion from the frozen contract | Judgment | Actual manuscript anchor | Reason and scope |
| --- | --- | --- | --- |
| All-localization ownership and original time | MEETS | Sections 1--2; Proposition 1; equation (7) | Actual ring equality and all positive units remain; no rank-one sector is substituted for the carrier |
| Integer-unit atom basis and metric | MEETS | Proposition 1, first two proof paragraphs | Unique factorization derives the finite unit basis from the integer monoid rather than selecting a prime-indexed input |
| Full-unit coefficient Koszul model | MEETS | Proposition 1, final proof paragraph | The finite free Laurent augmentation resolution gives the displayed zero cochain differential with trivial coefficients |
| Mean norm and Hilbert completion | MEETS | Proposition 1, coefficient-space paragraph | Rank-one periodic mean and higher-rank constants yield positive-definite coefficient norms on every actual component |
| Owned smoothing and fixed-component trace | MEETS | Proposition 2; equation (8) | The actual translation Fourier multipliers, Gaussian transform, and periodization agree in the same clock and normalization |
| Finite exterior rank selector | MEETS | Proposition 2; equations (9)--(10) | The finite degree-weighted trace is minus the rank-one coefficient trace and zero at higher rank |
| Dense closed full operator | MEETS | Proposition 3, first proof paragraph; equation (6) | Finite block support is dense; the coordinate-limit argument proves the graph is closed on the frozen maximal domain |
| Ordinary full-trace failure | MEETS | Proposition 3; equation (11); arbitrary-rank paragraph | Degree one is bounded but noncompact; the full operator is additionally unbounded |
| Fixed-smoothing component exhaustion | MEETS | Proposition 4; equation (12) | The positive zero-lattice Gaussian term gives divergence at every fixed positive smoothing and real time |
| Same-object and nonclaim discipline | MEETS | Sections 5--8; ledger UEW-11--12 | Local cancellation is not full return faithfulness, ordinary trace existence, torsion, a determinant, or Route credit |

These judgments concern mathematical truth conditions of the specified
contract, not a numerical score, novelty assessment or publication recommendation.

## Independent derivation checks

### 1. Arithmetic basis, coefficients and Koszul differential

For A=Z[1/n], a reduced positive rational q satisfies qA=A exactly
when both q and its inverse belong to A. Its numerator and denominator
therefore use only the finite prime support S of n. Thus
U_A is free abelian on S, and the irreducibles of
U_A intersect the positive integers are precisely S. Equality of actual rings
is equality of S, so prime powers do not add duplicate components.

At rank one, the invariant smooth functions are exactly the smooth
functions of period L=log p. Their mean norm is
L inverse times the integral over one period. At higher rank,
irrationality of log p/log q yields a dense logarithmic translation
subgroup; continuity forces invariant functions to be constant.
Both norm formulas are definite and produce the Hilbert spaces claimed.
No component disappears when its coefficient space becomes C.

In one Laurent variable, multiplication by z-1 is injective and its
cokernel is evaluation at 1. The division of f(z)-f(1) by z-1 stays
inside the Laurent ring. Its augmented two-term resolution is split as
a complex of complex vector spaces. Tensoring the finitely many copies
over C preserves the augmented exactness and gives the displayed finite
free resolution of the trivial augmentation module. Applying Hom into
B_A kills every z_i-1 because the coefficient action is trivial.
This justifies the zero differential and exterior powers of
Hom_Z(U_A,C), rather than merely declaring a convenient dimension count.
It does not identify this model with full groupoid cohomology or 158's
basic de Rham complex.

### 2. Smoothing, genuine local return comb and finite rank selection

In a rank-one component the normalized Fourier functions
exp(2 pi i m u/L) are orthonormal. The coefficient eigenvalues are

\[
e^{-\epsilon(2\pi m/L)^2}e^{2\pi i mt/L}.
\]

Their absolute sum is finite for fixed L and epsilon>0. Periodizing the
normalized Gaussian gives exactly
Theta=L sum_k g_epsilon(t-kL), with the factor L required by the
Fourier coefficient normalization. For this fixed L, Gaussian
approximation gives L sum_k delta_(kL) in distributions on R.
The paper does not interchange this limit with an infinite component sum.

The coefficient action is the identity on every higher-rank constant
space. In each fixed component there are only finitely many exterior
degrees, with dimensions binom(r,j). Differentiating (1-z)^r and
evaluating z times that derivative at z=1 gives

\[
\sum_{j=0}^r(-1)^j j\binom rj=-1\quad(r=1),\qquad
\sum_{j=0}^r(-1)^j j\binom rj=0\quad(r\ge2).
\]

Hence the finite trace calculation is legitimate. The rank-two control
has signed trace -2+2=0 but trace norm 2+2=4, confirming that cancellation
does not remove the channels. This is an exterior-rank identity; its
arithmetic interpretation additionally uses the independently derived
classification of rank-one actual localizations.

### 3. Maximal domain, noncompact compression and unboundedness

Write i=(A,j) and T_i=(-1)^j j(R_A tensor I). Each block is bounded.
Finite-block vectors lie in the frozen maximal domain and are dense.
If eta_n tends to eta and W eta_n tends to zeta in H, boundedness
of each block gives T_i eta_i=zeta_i. The square sum of those images
is finite because zeta belongs to H. Thus eta belongs to the maximal
domain and W eta=zeta. This establishes closedness of the graph,
not H-closedness of the domain as a subset.

The degree-one restriction has norm at most one. On every distinct
rank-one component its normalized constant exterior vector e_p obeys
W e_p=-e_p. The images of this infinite orthonormal family have no
convergent subsequence, so that bounded restriction is not compact.
Any bounded trace-class full realization preserving this action would
have a compact degree-one compression, which is impossible.

Actual components of arbitrary finite rank r exist. A normalized
constant vector in top degree has image norm r. Hence the frozen
full operator is unbounded as well, independently excluding ordinary
Hilbert trace class. For general t, this is not a claim that the
undefined ordinary trace itself equals negative infinity; the latter
statement belongs only to the finite-cutoff numerical traces below.

### 4. Full component exhaustion at fixed smoothing

For each finite set F, finite-dimensional exterior summation and
finite component addition give equation (12). At fixed epsilon>0,t,

\[
\Theta_{\log p,\epsilon}(t)
\ge(\log p)g_\epsilon(t)
\ge(\log2)g_\epsilon(t)>0.
\]

Every increasing exhaustion contains arbitrarily many distinct
rank-one components. Its finite traces therefore tend to negative
infinity. This proof needs neither a prime counting asymptotic nor
a numerical cutoff.

The actual manuscript claims only the fixed-component comb limit and
this fixed-positive-smoothing exhaustion result. It explicitly leaves
different limit orders, zero-time subtraction and relative distributions
unexecuted. There is consequently no illicit passage to a full
prime-return distribution in the reviewed result.

## Strongest counterargument and its disposition

The most serious apparent objection to the STOP is that the finite
exterior calculation has already done what the earlier complex failed
to do: it cancels every mixed-support component while leaving exactly
the rank-one circles. One might therefore argue that the full answer is
obtained by doing the finite degree cancellation first, then summing
the surviving circle traces, and finally removing the Gaussian. Since
all mixed components were present before cancellation, this looks
stronger than an explicit rank-one projection and may resemble the
beginning of a torsion or relative-trace construction.

That observation is a genuine local positive result, but it does not
refute the particular negative theorem under review. The frozen
target is the ordinary Hilbert trace of the actual full weighted
operator, or ordinary separate degree traces before any signed
summation. That operator has the infinite degree-one obstruction and
is unbounded across ranks. Moreover, even the finite-component signed
trace prescription diverges at every fixed positive smoothing.
An alternative order of limits would need a declared distributional
domain and a treatment of zero-time mass; it is not the ordinary
trace required by this card. The manuscript keeps these alternatives
open and does not infer that all torsions, relative traces or
arithmetic analytic frameworks fail. Thus the counterargument
supports preserving Proposition 2 as a local result and exploring
a genuinely different future contract, not promoting this contract's
undefined ordinary trace to an existing one.

## Issue list and actual adjudication

No CRITICAL or MAJOR mathematical issue was found in the reviewed scope.

| ID | Severity | Typed evidence anchor | Finding and minimum remedy | Confidence | Disposition |
| --- | --- | --- | --- | --- | --- |
| M1 | MINOR | text: Proposition 3, original first proof paragraph, “without incorrectly restricting the domain to that of the degree operator N” | This wording could imply D(N) is an incorrect smaller domain. In this model D(W)=D(N): every j>=2 block is higher rank with R_A=I, and the j=0,1 domain sums are finite for every vector in H. Delete the misleading comparison; no change to the main proof is needed. | 5/5, direct blockwise domain calculation | ADDRESSED |

The author accepted M1 and replaced the sentence with:
“This proves that W is closed on the displayed maximal domain.”
The reviewer reread that actual replacement in Proposition 3 before
finalizing this receipt. The frozen card, main results and stop condition
were not changed. No manuscript file was edited by the reviewer.

## Final bounded disposition

The candidate remains STOP at the full ordinary-trace requirement.
Propositions 1--2 establish a well-defined owned coefficient complex
and a genuine finite-component rank-one return trace; Propositions 3--4
establish the scoped global failures. The same-object ledger remains
intact, all mixed components remain in scope, and no formal Route
coordinate or Route-B claim was evaluated.

There is no unresolved mathematical blocker to recording these scoped
results after M1's verified correction. Other limiting, relative or
torsion prescriptions remain OPEN, not refuted and not executed.
