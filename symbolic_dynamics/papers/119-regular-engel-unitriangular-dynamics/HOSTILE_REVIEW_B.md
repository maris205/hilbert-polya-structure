# Hostile Review B — P119 round one

Date of audit: 2026-08-30.

## Role, scope, and provisional verdict

I acted as an independent nonauthor reviewer of the current round-one
source, the stored round-one PDF, the canonical verifier, and all support
documents.  I did **not** read Hostile Review A.  I reconstructed the claims
from the map itself and checked Bier's primary text rather than relying on
the manuscript's account of that paper.

**Verdict: MINOR REPAIR, THEN GO INTERNAL.  External release remains HOLD.**

There is no critical issue and no major mathematical defect.  The exact
fibre, iterated-fibre, layer, typed-indegree, and \(U_4\) formulas are
correct, including in characteristic two.  Bier is now identified as the
direct owner of the same fixed-\(J\) restricted and iterated images, and the
manuscript repeatedly assigns those statements zero contribution credit.
The remaining contribution is narrow and highly derivative, but its ceiling
is stated honestly as an exact finite-field conjunction rather than a
priority claim.

Four minor repairs are required before the next internal freeze:

1. qualify the abstract's fibre sentence by \(Y\in\gamma_{k+1}\);
2. restrict the abstract's deepest-layer formula to \(n\ge2\); and
3. point to the proof, rather than only the statement, of Bier's Theorem 1;
   and
4. keep Table 1 after the theorem that defines its entries.

## Reconstruction of the system

Let
\[
 N=\sum_{i=1}^{n-1}E_{i,i+1},\qquad J=I+N,\qquad
 E(X)=X^{-1}J^{-1}XJ
\]
on \(U_n(\mathbb F_q)\).  The subgroup
\(\gamma_k=I+\mathfrak n_k\) has order
\[
 |\gamma_k|=q^{(n-k)(n-k+1)/2},
\]
and the ideal product gives \(E(\gamma_k)\subseteq\gamma_{k+1}\).

Put \(\phi(X)=J^{-1}XJ\).  If \(E(X_1)=E(X_2)\), then
\[
 \phi(X_2X_1^{-1})=X_2X_1^{-1}.
\]
Conversely, left multiplication by a fixed point of \(\phi\) preserves
\(E(X)\).  Thus every nonempty fibre in \(\gamma_k\) is the **left** coset
\[
 C_{\gamma_k}(J)X.
\]
Commuting with \(J\) is the same as commuting with \(N\).  The equations
\(MN=NM\) force upper-triangular Toeplitz form, hence
\[
 C_{\gamma_k}(J)
 =\{I+a_kN^k+\cdots+a_{n-1}N^{n-1}\},
 \qquad |C_{\gamma_k}(J)|=q^{n-k}.
\]
It follows that
\[
 |E(\gamma_k)|
 =|\gamma_k|/q^{n-k}
 =|\gamma_{k+1}|.
\]
Together with the filtration inclusion, this proves both the image equality
and the stated one-step fibre formula.

The coordinate route is also sound.  Writing \(X=I+A\) and \(Y=I+B\),
the equation \(E(X)=Y\) is exactly
\[
 AN-NA=B+NB+AB+NAB.
\]
On superdiagonal \(r+1\), the new source diagonal enters through
\[
 \Delta_r(x_1,\ldots,x_{n-r})
 =(x_1-x_2,\ldots,x_{n-r-1}-x_{n-r}).
\]
This map is onto and has a one-dimensional constant-vector kernel.  Every
term involving \(A\) on the right uses only a source diagonal
\(u\le r-k<r\).  The \(r=n-1\) stage is the free central coordinate with
zero-dimensional codomain.  There are therefore \(n-k\) independent field
choices and exactly \(q^{n-k}\) solutions.

For
\[
 S_{k,t}=\sum_{j=k}^{k+t-1}(n-j)
         =t(n-k)-\binom t2,
\]
composition gives fibre size \(q^{S_{k,t}}\) over
\(\gamma_{k+t}\).  Since \(I\) is fixed,
\(\tau(X)\le t\) is equivalent to \(E^t(X)=I\).  Consecutive differences
therefore give
\[
 L_{k,t}
 =q^{S_{k,t}}-q^{S_{k,t-1}}
 =(q^{n-k-t+1}-1)q^{S_{k,t-1}},
\]
and at \(k=1,t=n-1\),
\[
 L_{1,n-1}=(q-1)q^{\binom n2-1}.
\]
All endpoint conventions agree: \(t=0\) gives singleton fibres,
\(t=n-k\) gives all of \(\gamma_k\) over \(I\), and later iterates remain
constant.

The filtration-stratum indegree is the difference between the
\(\gamma_k\)-restricted and \(\gamma_{k+1}\)-restricted fibres:
\[
 q^{n-k}\mathbf 1_{\gamma_{k+1}}(Y)
 -q^{n-k-1}\mathbf 1_{\gamma_{k+2}}(Y).
\]
At the last stratum it reduces to \(q-1\) predecessors of \(I\).  The
global indegree, root-child convention, unique recurrence, and
\((1-z)^{-1}\) zeta function follow correctly.

Finally, for \(J'=I+E_{12}+E_{34}\) in \(U_4(q)\), direct multiplication
gives exactly
\[
 a_{23}=0,\qquad a_{24}=a_{13}.
\]
Four of the six strict upper coordinates are free.  Hence the centralizer
has \(q^4\) points, every nonempty fibre has \(q^4\) points, and the image
has \(q^{6-4}=q^2<q^3=|\gamma_2|\).  This proves precisely one failure of a
universal arbitrary-unipotent extension; it does not classify nonregular
second entries, and the paper does not claim that it does.

## Characteristic-two and boundary audit

No proof step divides by two or uses a sign distinction.  In characteristic
two the difference \(x_i-x_{i+1}\) becomes a sum, but its kernel is still
the constant vectors and the map remains onto.  The \(U_4\) equations above
are unchanged as equalities.  A separate throwaway enumeration passed
through \(U_5(\mathbb F_2)\) and \(U_4(\mathbb F_3)\).  In the smallest
characteristic-two guard it found centralizer size \(16\), image size \(4\),
uniform fibre size \(16\), and \(|\gamma_2|=8\), exactly as predicted.

The body handles \(n=1\), \(n=2\), \(k=n-1\), \(t=0\),
\(t=n-k\), \(t>n-k\), targets outside the image, prime fields, and
nonprime finite fields correctly.  The only boundary leaks are in the
abstract and are listed under minor issues.

## Primary-owner audit

The bibliographic record is correct: Agnieszka Bier, *Linear Algebra and
its Applications* **438** (2013), no. 5, 2320--2330,
[DOI 10.1016/j.laa.2012.10.009](https://doi.org/10.1016/j.laa.2012.10.009).
I checked both the
[publisher record](https://www.sciencedirect.com/science/article/pii/S0024379512007197)
and the
[institutional full text](https://delibra.bg.polsl.pl/Content/31969/REPO_35897_-_On-Solvability-of-En_0000.pdf).

Bier defines the same convention
\([x,y]=x^{-1}y^{-1}xy\) and fixes
\[
 B=I+\sum_{i=1}^{n-1}E_{i,i+1}=J.
\]
Her notation satisfies \(UT_n^m=\gamma_{m+1}\).  Lemma 1 says that every
\(C\in UT_n^m\) has a solution \(A\in UT_n^{m-1}\) to
\([A,B]=C\).  After translating the index, this is exactly the restricted
surjectivity
\[
 E(\gamma_k)=\gamma_{k+1}.
\]
The statement of her Theorem 1 is phrased as two-variable Engel
solvability, but its proof keeps this same \(B\) fixed through the induction.
It therefore supplies the fixed-\(J\) iterated images
\[
 E^t(U_n)=\gamma_{t+1},
\]
not merely generic Engel-word image existence.

The round-one manuscript recognizes all of that direct ownership in the
abstract, introduction, theorem proof, conclusion, README, plan,
narrative, claims-evidence map, and control report.  It gives the image and
existence statements zero credit.  That subtraction is substantively
accurate.

The residual must nevertheless remain narrow.  Once Bier supplies
nonempty fibres, the general fixed-coset observation and the classical
regular centralizer make the one-step cardinality nearly immediate.  The
iterated fibres, depth layers, and typed indegrees then follow by products
and differences.  The triangular count is a genuinely different coordinate
derivation of multiplicity, but not a second ownership claim for existence.
The manuscript says exactly this.  A bounded search through 2026 with
fixed-commutator, regular-unitriangular, Engel-fibre, and iterated-image
formulations found no primary source stating the complete finite-field
fibre/layer/type conjunction.  That no-hit is not a novelty certificate,
and the manuscript correctly says so.

## Severity-ranked issues

### CRITICAL

None.

### MAJOR (mathematics)

None.  I found no counterexample to a formally stated theorem.

### MAJOR (owner scope)

None at the present claim ceiling.  External novelty and priority are not
cleared: the residual is close to an immediate corollary of Bier's owned
surjectivity plus an owned regular-centralizer computation.  This would be
a major external-positioning objection if the HOLD language were removed.
With the present repeated zero-credit statements and external HOLD, it is a
controlled limitation rather than a manuscript overclaim.

### MINOR

1. **The abstract's target quantifier is literally false.**  It says every
   target has \(q^{n-k}\) predecessors in \(\gamma_k\), whereas targets
   outside \(\gamma_{k+1}\) have none.  The smallest counterexample is
   \(n=2,k=1\) and \(Y=I+aE_{12}\) with \(a\ne0\): here
   \(\gamma_2=\{I\}\), the map is constant at \(I\), and the fibre over
   \(Y\) is empty.  Theorem 3.1 is correct.  Replace the abstract phrase by
   “every target in \(\gamma_{k+1}\).”
2. **The abstract needs \(n\ge2\) for the deepest-layer formula.**  At
   \(n=1\), the displayed expression becomes
   \((q-1)q^{-1}\), while the singleton phase has deepest layer \(1\).
   The setup and Remark 2.1 already handle this correctly.  Add \(n\ge2\)
   before the abstract's height/deepest-layer assertion.
3. **Make the Bier citation pointer exact.**  Bier's Lemma 1 literally
   fixes \(B=J\).  Her Theorem 1 statement quantifies both variables, while
   the *proof* keeps that same \(B\) fixed.  References to the iterated
   fixed-\(J\) result should therefore say “the proof of Theorem 1,” not
   only “Theorem 1.”  This is citation precision, not an ownership defect.
4. **Table 1 appears before its definition.**  In the rendered PDF the
   table floats to the top of page 4, above Section 5 and before
   \(L_{k,t}\) is introduced.  Keep it after Theorem 5.1 and its proof
   (or otherwise prevent that float).  The numbers themselves are correct.

## Fresh verifier audit

From the paper directory I ran

    PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py

and compared fresh stdout byte-for-byte with
code/verification_output.txt.  The comparison returned zero.  The fresh
result is nine lines and 287 bytes:

    regular Engel exact control: PASS
    assertions=1,491,877
    fields=F_2,F_3,F_4,F_5,F_8,F_9
    exhaustive_phase_states=55,808
    restricted_surjections=39
    iterated_fibre_profiles=112
    nonregular_counterexample_states=20,514
    exact_layer_table_rows=43
    claim_ceiling=fixed_J_equals_I_plus_regular_shift

Inspection of the code confirms that the controls are literal rather than
formula-only: matrix inverses, the update, restricted images, targetwise
fibres, left-coset orientation, difference maps, iterated fibres, root CDFs,
exact layers, typed indegrees, periodic points, nonprime fields, and the
near-regular \(U_4\) guard are all checked.  The 43-row TSV is rebuilt and
byte-compared.  The assertion count is an execution count, not a count of
independent theorems, and the support documents state that limitation.

## Fresh build and PDF audit

In a new temporary directory containing only main.tex and references.bib, I
ran

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

The fresh PDF is byte-for-byte equal to both main_round1.pdf and main.pdf.
It has six A4 pages, PDF version 1.5, and 409,880 bytes.  The settled log and
BLG contain no LaTeX/BibTeX warning, error, undefined citation/reference,
box warning, or rerun request.  All seven cited bibliography entries resolve.
All 32 font rows are embedded, subsetted, and Unicode mapped.  Author
metadata is empty; there is no form, JavaScript, encryption, or page
rotation.  Text extraction found no placeholder, draft marker, unresolved
token, or anonymous-author leak.

I rendered and inspected all six pages.  There is no clipping, collision,
blank page, missing glyph, or broken formula.  The only visual objection is
the premature Table 1 float recorded above.

## Required repair contract and final recommendation

Before the next internal freeze:

1. insert “in \(\gamma_{k+1}\)” into the abstract's fibre claim;
2. insert \(n\ge2\) into the abstract's deepest-layer claim;
3. point to the proof of Bier's Theorem 1 for the fixed-\(J\) iteration; and
4. keep Table 1 after the theorem that defines its entries.

No theorem formula, verifier result, or support-document claim requires
substantive revision.  After these minor changes, my recommendation is
**GO INTERNAL**.  External circulation, novelty, priority, and specialist
clearance remain **HOLD**.
