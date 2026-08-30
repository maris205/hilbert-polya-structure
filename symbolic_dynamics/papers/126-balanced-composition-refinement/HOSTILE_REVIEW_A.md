# P126 hostile Review A — independent nonauthor, round 0

## Decision

**STOP / REWRITE. External release remains HOLD.**

The mathematical core survives independent reconstruction: the terminal
codeword marker, complete kernel equivalence, right-to-left decoder,
one-run fibre product, maximum-fibre inequality, image bijection, rational
OGF, and recurrence are correct, including the cases \(t=0\), \(n=0\), and
\(K=1\). The fresh verifier and an independent ephemeral implementation
also pass.

The package nevertheless does **not** yet satisfy the cited phase-one gate.
Two mandatory owner/scope repairs are absent from the manuscript:

1. the external owner subtraction omits the gate's primary parallel-morphism
   and binary-fragmentation sources and does not itemize those zero-credit
   interfaces; and
2. the required internal firewall against P094, P108, P113, P115, P122,
   P123, and P125 is absent.

The README's statement that the GO_IF_REPAIRED gate is satisfied is therefore
premature. These are value/ownership MAJOR issues, not defects in the main
formulas. Once they are repaired, a narrow re-entry review should be
sufficient.

Severity count:

- **CRITICAL: 0**
- **MAJOR: 2**
- **MINOR: 4**

## Independence, scope, and frozen artifacts

I did not author P126. I read the entire current manuscript, bibliography,
support package, verifier, canonical transcript, PDF, frozen round-zero PDF,
and the full pre-paper gate
HOSTILE_GATE_BALANCED_COMPOSITION_REFINEMENT.md. I reconstructed the
mathematics directly rather than treating the verifier or gate as a proof.
I did not edit any manuscript, code, PDF, bibliography, or support document.

The reviewed hashes are:

- main.tex:
  fe8d5a382a1f659f5146cb87bb8f1e45dd8fef11eec8d813a666c6d956261e6f
- references.bib:
  c31b2d54985e9503ac51df206f6980afdf4dd7956bd5f011945218f65dad0cbc
- code/verify.py:
  5f58da9c3418502d64cd2fc7e3918c9a8bb464c456bc936539bb2afc7ee83ef0
- code/verification_output.txt:
  978191ccbc9a120ca34a298ab79f828175a069b7574388823885fb5712bd2090
- main.pdf and main_round0_original.pdf:
  d48125fc509fc972b2b705226c33d7915a529523917fd786a5eda2190106ca1e

The two PDF hashes are identical, so the live artifact is exactly the frozen
round-zero artifact.

## 1. Literal dynamics and exact clock

For a part \(m>1\), the map replaces \(m\) by
\((\lfloor m/2\rfloor,\lceil m/2\rceil)\), and it fixes \(1\). Extension by
concatenation makes the update a synchronous monoid morphism. Weight is
preserved. Every nonfixed word contains a part greater than one, and every
such part increases the word length by one; hence word length is a strict
Lyapunov function away from \(1^n\). Since a composition of weight \(n\) has
length at most \(n\), every orbit terminates at \(1^n\), the unique recurrent
state at that weight. The empty composition is fixed at weight zero.

Let \(W_t(m)=\Phi^t((m))\) and \(K=2^t\). At level \(j\), the descendants
have sizes \(\lfloor m/2^j\rfloor\) or
\(\lceil m/2^j\rceil\), up to the harmless persistence of a descendant that
has already reached one. The rightmost path obeys

\[
 r_{j+1}=\left\lceil\frac{r_j}{2}\right\rceil,\qquad r_0=m,
\]

so the nested-ceiling identity gives

\[
 r_j=\left\lceil\frac{m}{2^j}\right\rceil.
\]

It is both the rightmost and the largest descendant. If \(m>K\), then before
level \(t\) every descendant is at least two, so the full binary tree has
\(K\) leaves. If \(m\le K\), all descendants are one at time \(t\), and
weight preservation gives \(m\) leaves. Thus

\[
 |W_t(m)|=\min(m,K),\qquad
 \operatorname{last}(W_t(m))
 =\max W_t(m)=\left\lceil\frac mK\right\rceil,
\]

and \(W_t(m)=1^m\) exactly when \(m\le K\). This validates the codeword
terminal marker on which the decoder depends.

For a nonempty composition \(a\), all parts have become one by time \(t\)
exactly when \(\max_i a_i\le2^t\). Therefore

\[
 \operatorname{depth}(a)=\left\lceil\log_2\max_i a_i\right\rceil,
\qquad
 \max_{a\in\mathcal C_n}\operatorname{depth}(a)
 =\lceil\log_2 n\rceil,
\]

with witness \((n)\). The empty and \(n=1\) boundaries are correct.

## 2. Complete kernel and suffix decoder

For \(K=2^t\), let \(\mathcal N_K\) replace a source part \(m\le K\) by
\(1^m\) and retain a part \(m>K\). The codeword identity above immediately
gives

\[
 \Phi^t=\Phi^t\circ\mathcal N_K.
\]

The canonical alphabet is

\[
 A_K=\{1\}\cup\{K+1,K+2,\ldots\}.
\]

On this alphabet, \(W_t(1)=1\), while each \(W_t(m)\) with \(m>K\) has the
same length \(K\) and final symbol \(\lceil m/K\rceil>1\). Two long
codewords with different source letters have different total weights, hence
are distinct. Consequently:

- the one-symbol word \(1\) is not a suffix of any long codeword;
- no long codeword is a suffix of \(1\); and
- two distinct long codewords, having equal length, cannot be suffixes of
  one another.

The set is therefore a suffix code. If a target ends in \(1\), its final
canonical letter must be \(1\). Otherwise, its last \(K\) symbols must be a
long codeword; their weight identifies the sole candidate source letter,
and literal equality with \(W_t(m)\) accepts or rejects the block. Repetition
decodes uniquely from right to left.

This proves injectivity of \(\Phi^t\) on \(A_K^*\), and hence

\[
 \Phi^t(a)=\Phi^t(b)
 \quad\Longleftrightarrow\quad
 \mathcal N_K(a)=\mathcal N_K(b).
\]

The theorem's same-weight hypothesis is redundant but harmless: equality of
images already forces equal weights. At \(t=0\), \(K=1\), every codeword is
a single source letter, \(\mathcal N_1\) is the identity, and the decoder
reduces to literal one-symbol decoding. Thus the claimed complete kernel
does not hide a \(t=0\) exception.

The manuscript's example is also correct:

\[
 W_2(3)=111,\qquad W_2(5)=1112,\qquad W_2(2)=11,
\]

so \((3,5,2)\) has canonical form \((1,1,1,5,1,1)\) and image
\(111\,1112\,11\). The advertised suffix decoding recovers that canonical
form.

## 3. Every fibre and the maximum inequality

Write a decoded canonical form as

\[
 z=1^{r_0}m_1 1^{r_1}\cdots m_s1^{r_s},
 \qquad m_i>K,\quad r_i\ge0.
\]

In a source normalizing to \(z\), every \(m_i\) is forced. Each unit run
\(1^{r_j}\), independently of the others, can be regrouped into an arbitrary
composition of weight \(r_j\) with parts at most \(K\). If \(R_K(r)\) denotes
the number of these restricted compositions and \(R_K(0)=1\), then

\[
 |(\Phi^t)^{-1}(y)|=\prod_{j=0}^{s}R_K(r_j)
\]

for an accepted target, and the fibre is empty for a rejected target. No
source grouping can cross a retained large letter, so there is no missing
coupling between runs.

For fixed run weights \(r_0,\ldots,r_s\), concatenation is an injection from
the tuple of restricted compositions into the restricted compositions of
weight \(\sum_jr_j\): the prescribed cumulative weights recover the tuple
boundaries. Appending \(n-\sum_jr_j\) ones is then an injection into the
restricted compositions of \(n\). Therefore

\[
 \prod_j R_K(r_j)
 \le R_K\!\left(\sum_jr_j\right)
 \le R_K(n).
\]

The all-one target has canonical form \(1^n\) and fibre \(R_K(n)\), so the
maximum formula is exact. This also equals the number of states of depth at
most \(t\), since those are exactly the compositions with all parts at most
\(K\).

For \(n=0\), take \(s=0,r_0=0\); the unique factor is \(R_K(0)=1\), giving
the correct singleton empty-word fibre. For \(t=0\), \(R_1(r)=1\) for every
\(r\), as required by the identity map.

## 4. Image OGF, recurrence, and boundaries

Every source has the same image as its canonical form, and distinct
canonical forms have distinct images. Thus \(\Phi^t\) restricts to a
weight-preserving bijection from \(A_K^*\) onto its image. The weight series
of one canonical letter is

\[
 L_K(x)=x+\frac{x^{K+1}}{1-x}.
\]

Taking arbitrary finite sequences, including the empty one, gives

\[
 I_t(x)=\frac1{1-L_K(x)}
 =\frac{1-x}{1-2x+x^2-x^{K+1}}.
\]

Coefficient extraction yields

\[
 I_{0,t}=I_{1,t}=1,\qquad
 I_{n,t}=2I_{n-1,t}-I_{n-2,t}
 +\mathbf1_{n\ge K+1}I_{n-K-1,t}\quad(n\ge2).
\]

All highlighted boundaries check:

- \(n=0\): the empty sequence contributes \(I_{0,t}=1\);
- \(n=1\): only \((1)\) occurs, so \(I_{1,t}=1\);
- \(t=0\): \(K=1\), the OGF becomes
  \((1-x)/(1-2x)\), giving all ordinary compositions,
  \(I_{0,0}=1\) and \(I_{n,0}=2^{n-1}\) for \(n\ge1\);
- \(t=1\): canonical parts are all positive parts except \(2\), giving the
  stated no-part-\(2\) sequence; and
- \(2^t\ge n\): only \(1^n\) is canonical, so \(I_{n,t}=1\).

The Garden formula \(2^{n-1}-I_{n,t}\) is correctly restricted to \(n\ge1\).

## 5. Gate compliance audit

The mathematical repairs demanded by the pre-paper gate are substantially
present:

| Gate item | Review result |
|---|---|
| all-\(t\) normal form and complete kernel iff | PASS |
| final-letter marker and suffix decoder | PASS |
| exact pointwise run-product fibre | PASS |
| maximum fibre via an explicit injection | PASS |
| all-\(t\) image bijection, OGF, recurrence | PASS |
| \(t=0\), \(n=0\), \(K=1\) mathematical boundaries | PASS, with minor exposition repairs below |
| one-step no-part-\(2\) enumeration zero-credit | PASS |
| general restricted-composition enumeration zero-credit | PASS |
| primary parallel-morphism and fragmentation subtraction | **NOT CLOSED — MAJOR A1** |
| required P094/P108/P113/P115/P122/P123/P125 firewall | **NOT CLOSED — MAJOR A2** |
| three proof-spike hashes in the later evidence ledger | **NOT CLOSED — MINOR A4** |

Therefore the package does not fully satisfy
HOSTILE_GATE_BALANCED_COMPOSITION_REFINEMENT.md despite the README status
line.

## 6. Owner subtraction

The current four references correctly cover a general code text, the
Chinn--Heubach no-part-\(2\) class, parts-in-a-set enumeration, and
bounded-part composition counts. The manuscript also uses appropriately
bounded non-hit language and makes no priority claim.

However, the gate expressly required primary-source subtraction of the
other mechanism interfaces. Those sources are absent from both the
bibliography and the itemized prose:

- Lindenmayer and Rozenberg's synchronous developmental-system formulation
  explicitly applies rewriting functions simultaneously to all cells:
  [Developmental systems and languages, STOC 1972,
  DOI 10.1145/800152.804917](https://doi.org/10.1145/800152.804917).
- Matsoukas treats an integer mass splitting into two integer fragments as
  discrete binary fragmentation:
  [Stochastic Theory of Discrete Binary Fragmentation, Entropy 24 (2022),
  229](https://doi.org/10.3390/e24020229).
- Chinn and Heubach directly own the compositions-without-\(2\) class and
  its enumeration:
  [Journal of Integer Sequences 6 (2003), Article
  03.2.3](https://cs.uwaterloo.ca/journals/JIS/VOL6/Heubach/heubach5.html).
- The gate additionally identified Banderier--Hitczenko for the surrounding
  restricted-composition analytic toolkit
  ([DOI 10.1016/j.dam.2011.12.011](https://doi.org/10.1016/j.dam.2011.12.011))
  and Honkala plus Freydenberger--Reidenbach for morphism/code ambiguity
  ([DOI 10.1080/00207168708803578](https://doi.org/10.1080/00207168708803578);
  [DOI 10.1016/j.dam.2009.06.009](https://doi.org/10.1016/j.dam.2009.06.009)).

A fresh bounded search using the literal floor/ceiling rule, balanced
composition split, suffix decoding, morphism kernel, and iterated-image
phrases did not locate a direct owner of the exact P126 conjunction. That is
only a bounded non-hit. Generic literature on morphisms and their kernel
congruences further confirms that the vocabulary itself is mature and must
receive zero credit.

### MAJOR A1 — required repair

Add the gate's primary parallel-rewriting and binary-fragmentation sources,
or equally direct primary substitutes, and state item by item that the
following receive zero contribution credit:

1. simultaneous/parallel application of a monoid morphism;
2. binary integer fragmentation and balanced splitting;
3. generic suffix codes, unique decoding, and morphism ambiguity;
4. bounded-part Fibonacci counts and parts-in-a-set OGFs;
5. the \(t=1\) no-part-\(2\) class and sequence.

Keep the residual claim limited to the exact temporal
kernel--fibre--image conjunction. This repair does not require changing a
formula.

## 7. Internal collision audit

The internal corpus confirms the gate's listed package collisions:

- **P094** already uses morphisms, explicit terminal/boundary markers, and
  unique desubstitution/recognizability.
- **P108** already occupies Fibonacci terminology together with a sharp
  clock and image/fibre geometry.
- **P113** uses an integer-sum carrier, absorption, a sharp depth, and an
  owned product-fibre transport.
- **P115** already packages every iterate, every image and fibre, and a
  logarithmic threshold.
- **P122** already combines target-local fibre factorization/DP with an
  aggregate image and Garden census.
- **P123** already uses refinement as a central dynamics word.
- **P125** already packages pointwise fibres, iterated images, and exact
  temporal layers.

None is a literal collision with P126's ordered-composition map or its
normal form. Nevertheless, the required firewall is wholly absent from
main.tex; neither a table nor a paragraph names these neighbors. The
package therefore risks selling an occupied architecture rather than its
residual.

The current NARRATIVE_REPORT.md and CONTROL_RESULTS.md do contain a different
firewall for P101, P110, P117, and P121. Those are useful additional controls,
but they do not replace the seven collisions expressly required by the
phase-one gate, and they are not carried into the manuscript's claim boundary.

### MAJOR A2 — required repair

Add an explicit internal firewall covering all seven items. It should say
that P126 claims only the all-iterate canonical kernel, exact run-product
fibres, and temporal image bijection for this infinite-alphabet balanced
morphism. Refinement, recognizability, Fibonacci naming, logarithmic clocks,
target-local DP, image/Garden enumeration, and the generic
depth--fibre--image package are not claimed as new internal value.

After this change, correct the README/support status from “gate satisfied”
only if the external-owner repair is also present.

## 8. Minor findings

### MINOR A1 — weight versus word length

The maximum-fibre proof says “restricted compositions of lengths
\(r_0,\ldots,r_s\)” and “their total length.” A composition of \(r_j\)
has integer **weight** \(r_j\); its number of parts is its word length.
This is exactly the terminology ambiguity flagged by the gate. Replace both
uses by “weights.” The injection is then unambiguous.

### MINOR A2 — make empty and \(t=0\) conventions explicit

The formulas already handle the boundaries, but the theorem text should
state:

- the empty decoded word is represented by \(s=0,r_0=0\);
- its fibre product is \(R_K(0)=1\);
- \(R_1(r)=1\) for all \(r\ge0\); and
- at \(t=0\), the image OGF is \((1-x)/(1-2x)\), with
  \(I_{0,0}=1\) and \(I_{n,0}=2^{n-1}\) for \(n\ge1\).

This closes the gate's boundary convention literally rather than only by
inference.

### MINOR A3 — expose the codeword induction identity

Lemma 2.1 is correct, but its crucial terminal-marker proof is compressed to
“induction therefore gives.” Add the recurrence

\[
\operatorname{last}(W_{t+1}(m))
=\operatorname{last}\!\left(
 W_t(\lceil m/2\rceil)\right)
=\left\lceil\frac{\lceil m/2\rceil}{2^t}\right\rceil
=\left\lceil\frac{m}{2^{t+1}}\right\rceil
\]

and one sentence justifying that \(m>2^t\) prevents early leaves before
level \(t\). This is an auditability repair, not a mathematical correction.

### MINOR A4 — restore the proof-spike provenance ledger

The gate required its three pinned proof-spike hashes and a fresh stdout
comparison in any future evidence ledger. The paper package records the
paper-local hashes and fresh canonical match, but not the three gate-input
hashes. Add them to BUILD.md or CONTROL_RESULTS.md, explicitly labelled as
pre-paper provenance rather than current paper hashes.

## 9. Mechanical verification

I reran

    PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py

from the P126 directory, redirecting stdout to a fresh temporary file. The
run completed with

    balanced composition refinement exact control: PASS
    assertions=8756710

The fresh transcript SHA-256 is
978191ccbc9a120ca34a298ab79f828175a069b7574388823885fb5712bd2090,
byte-for-byte identical to the canonical transcript.

The paper-local verifier checks:

- literal dynamics through weight 18;
- all kernel classes, sources, targets, and fibres through weight 15 for
  \(0\le t\le5\);
- both normal-to-image and image-to-normal implications;
- the suffix decoder on every tested image and target;
- the literal fibre against both the run product and a separately coded
  factorization DP;
- codewords through \(m=256,t=8\); and
- image recurrence coefficients through weight 90 for \(t\le8\).

I also ran a separate ephemeral standard-library implementation that did
not import code/verify.py. It reconstructed the step map, codewords, normal
form, decoder, fibre product, maximum, and recurrence and made 179,674
additional exact assertions, including exhaustive small boundary cases.
It passed.

Finite enumeration remains falsification evidence, not proof or ownership
evidence.

## 10. Isolated build, visual inspection, fonts, and metadata

I copied only main.tex and references.bib into a fresh temporary directory
and ran:

1. pdflatex,
2. bibtex,
3. pdflatex,
4. pdflatex.

All four stages exited zero. The final log has no errors, warnings,
undefined citations/references, rerun requests, or overfull/underfull boxes.
The isolated PDF SHA-256 is
d48125fc509fc972b2b705226c33d7915a529523917fd786a5eda2190106ca1e,
exactly matching both packaged PDFs.

The artifact has 4 A4 pages and 314,921 bytes. I rendered and inspected all
four pages. There is no clipping, overlap, malformed formula, missing glyph,
broken citation, unresolved marker, or orphaned heading. Page 4 contains only
the four references and substantial blank lower-page space; this is
cosmetic, not a defect.

All listed fonts are embedded, subsetted, and Unicode-mapped. Author, Title,
Subject, and Keywords metadata fields are blank; there is no metadata stream,
form, JavaScript, encryption, or author leakage. The PDF is anonymous.

## 11. Claim ceiling and re-entry condition

After the two MAJOR repairs, the admissible internal claim remains:

\[
\boxed{\text{literal balanced-composition dynamics}
+\text{ all-time canonical kernel}
+\text{ exact run-product fibres}
+\text{ temporal image bijection}.}
\]

The logarithmic clock, parallel morphism, binary fragmentation, suffix-code
principle, restricted-composition counts, no-part-\(2\) sequence, and generic
image/Garden bookkeeping remain zero-credit. No asymptotic, priority,
minimality, general D0L, or external-readiness claim is supported.

**Final verdict: STOP / REWRITE, not KILL.** Resolve MAJOR A1 and A2, make
the four minor clarifications, rebuild, and return for a narrow Review-A
re-entry. **External release remains HOLD.**
