# Hostile Review A — principal-hook partition dynamics

**Role and scope.** Independent non-author review, dated 2026-08-29. I
reconstructed the map and proofs from the definitions, ran a separate literal-cell
audit, inspected the cited primary sources, reran the supplied verifier, and made a
fresh build in a temporary directory. I did not consult any Review B artifact. No
existing P113 file was edited, no Git operation was performed, no hash was made,
and this is not final QA.

**Provisional verdict: MAJOR REVISION; external dissemination remains HOLD.** I
found no counterexample to the stated formulas or finite-dynamical conclusions.
The mathematical core is short and apparently correct. Release is nevertheless
premature for two reasons: the central word “attractor” is undefined and
convention-sensitive, and the ownership subtraction stops too early. In
particular, the principal-hook partition and the first-hook identity were already
explicit in Gutschwager, while most claims other than the exact gap/depth theorem
are immediate corollaries or a tautological fibre transport. A bounded search did
not locate an exact owner for iteration of this map, but that negative search is
not novelty evidence.

## 1. Independent mathematical reconstruction

### 1.1 The literal map and its orientation

Let \(\lambda=(\lambda_1,\ldots,\lambda_\ell)\vdash n\), let
\(\lambda'\) be its conjugate, and let
\(d=\max\{i:\lambda_i\ge i\}\). For \(1\le i\le d\), the arm and leg
lengths at the diagonal cell \((i,i)\) are

\[
\alpha_i=\lambda_i-i,\qquad \beta_i=\lambda'_i-i.
\]

Thus the principal-hook length is

\[
h_i=\alpha_i+\beta_i+1=\lambda_i+\lambda'_i-2i+1.
\]

The hooks are ordered from the outer/top-left diagonal cell to the inner one.
Every Ferrers cell \((r,c)\) is assigned to the diagonal hook indexed by
\(\min(r,c)\); a cell with both coordinates greater than \(d\) cannot exist by
maximality of the Durfee square. Hence the hooks are disjoint, cover the diagram,
and have total size \(n\). Strict decrease of both Frobenius sequences gives

\[
h_i-h_{i+1}=(\alpha_i-\alpha_{i+1})
             +(\beta_i-\beta_{i+1})\ge2.
\]

Therefore \(H(\lambda)=(h_1,\ldots,h_d)\) is indeed a partition of the
same weight. The formula is invariant under changing Ferrers drawing convention
and under conjugation, so there is no hidden orientation reversal.

### 1.2 Image and Frobenius fibre

Conversely, fix \(h=(h_1,\ldots,h_r)\) with adjacent gaps at least two.
At the innermost hook there are exactly \(h_r\) choices
\(\alpha_r\in\{0,\ldots,h_r-1\}\), after which
\(\beta_r=h_r-1-\alpha_r\). For each \(i<r\), write

\[
x_i=\alpha_i-\alpha_{i+1}-1,\qquad
y_i=\beta_i-\beta_{i+1}-1.
\]

The nonnegative pair \((x_i,y_i)\) must sum to
\(h_i-h_{i+1}-2\), so it has exactly
\(h_i-h_{i+1}-1\) choices. These choices reconstruct unique strict
nonnegative Frobenius coordinates. Thus

\[
\#H^{-1}(h)=h_r\prod_{i<r}(h_i-h_{i+1}-1).
\]

The proof in Proposition 2.1 is correct, including the one-part/empty-product
case. It is, as the manuscript says, owned material; Section 4 below refines the
owner attribution.

### 1.3 First part, exact gap increments, and depth

The outer hook contains the first row and first column with the corner counted
once, so

\[
(H\lambda)_1=\lambda_1+\ell(\lambda)-1.
\]

Off \((n)\), the length is at least two, hence the first part strictly grows.
Because \(\mathcal P(n)\) is finite and the first part is at most \(n\), every
orbit reaches \((n)\); no other periodic orbit is possible.

For \(g(\lambda)=\lambda_1-\lambda_2\), with \(\lambda_2=0\) for a
one-row partition, the two Durfee cases are exactly as follows.

- If \(d\ge2\), then
  \(h_1=\lambda_1+\ell-1\) and
  \(h_2=\lambda_2+\lambda'_2-3\). Therefore

  \[
  g(H\lambda)-g(\lambda)=\ell-\lambda'_2+2
  =2+m_1(\lambda),
  \]

  since \(\lambda'_2\) counts the parts at least two.

- If \(d=1\) and the state is nonterminal, then
  \(\lambda=(a,1^b)\) with \(b\ge1\). Its only principal hook is the
  whole diagram, so \(H\lambda=(n)\) and the gap rises from \(a-1\) to
  \(a+b\), an increment of \(b+1\).

Every nonterminal step therefore raises the gap by at least two. Telescoping to
the terminal gap \(g((n))=n\) gives

\[
\tau(\lambda)\le \left\lfloor\frac{n-g(\lambda)}2\right\rfloor
\le\left\lfloor\frac n2\right\rfloor.
\]

For \(a\ge b\ge2\), direct hook calculation gives
\(H(a,b)=(a+1,b-1)\), while \(H(a,1)=(a+1)\). Starting at the balanced
two-row partition takes \(b=\lfloor n/2\rfloor\) steps, so the global bound
is attained. The theorem is correct; there is only a small wording error about
which formula handles the last step, recorded under MINOR.

### 1.4 Layer timing

The time offset in Theorem 4.1 is correct. The only depth-zero state is
\((n)\). Its fibre consists of the \(n\) hook partitions of \(n\), including
\((n)\) itself, so \(A_1(n)=n-1\). For \(t\ge2\), a state has depth \(t\)
exactly when its first image \(h\) has depth \(t-1\). Since then
\(\tau(h)\ge1\), there is no fixed-state subtraction, and disjoint fibres give

\[
A_t(n)=\sum_{\substack{h\in\operatorname{im}H\\\tau(h)=t-1}}
       \#H^{-1}(h).
\]

The restriction \(t\ge2\) is essential: using the same unadjusted sum at
\(t=1\) would give \(n\), not \(n-1\). The manuscript gets this boundary and
the \(t-1\) shift right.

### 1.5 Conjugation, periodic data, and the two smallest weights

Conjugation swaps \(\alpha_i\) and \(\beta_i\), hence
\(H(\lambda)=H(\lambda')\). Positive-time orbits coincide. If neither
conjugate is terminal, both entrance times equal \(1+\tau(H\lambda)\). The
only unordered conjugate pair with exactly one terminal member is
\(\{(n),(1^n)\}\) for \(n>1\), with depths zero and one. This proves the
claimed unique depth exception.

The strict first-part increase leaves \((n)\) as the only periodic point, so
\(\#\operatorname{Fix}(H^m)=1\) for every \(m\ge1\), and the formal
Artin--Mazur zeta calculation

\[
\exp\!\left(\sum_{m\ge1}\frac{z^m}{m}\right)=(1-z)^{-1}
\]

is correct.

At \(n=1\), the sole state \((1)\) has depth zero, \(A_0=1\), and
\(A_1=0\). At \(n=2\), \((2)\) and \((1,1)\) have depths zero and one,
respectively; they are also the first conjugate-depth exception. The pointwise
bound, balanced witness, layer initialization, and zeta statement all survive
these endpoints.

## 2. Counterexample attack and exact controls

I did not merely replay the submitted implementation. I separately enumerated
Ferrers cells and assigned each cell to the hook indexed by \(\min(r,c)\), then
rebuilt fibres and literal orbits without importing `code/verify.py`. Through
\(n=30\), this covered 28,628 states and 172,944 checks. It found no
counterexample to any stated theorem and independently reproduced the first
three killed overclaims:

- projection/idempotence already fails at
  \((2,2)\mapsto(3,1)\mapsto(4)\);
- unconditional depth invariance under conjugation fails at
  \((2)\leftrightarrow(1,1)\), with depths zero and one;
- “rectangular implies deepest” fails first at
  \((4,4,4,4)\vdash16\), whose depth is seven rather than eight.

The exact-increment split was also attacked directly. For example,
\((3,2,1)\mapsto(5,1)\) has increment three because one part equals one,
while \((2,1,1)\mapsto(4)\) is the Durfee-one case with increment three.
These rule out the tempting stronger assertion that every step has increment
exactly two.

The supplied verifier was then fresh-run with bytecode writes disabled and its
stdout sent to the temporary audit directory. Results:

- `PASS: 10,110,035 exact assertions`;
- 45 output lines and 6,053 bytes;
- byte-for-byte `cmp` against `code/verification_output.txt`: **MATCH**;
- the reported first counterexamples and every lane through \(n=40\) were
  reproduced.

This byte comparison used no hash. The exhaustive computation is strong
regression evidence, not ownership or novelty evidence.

## 3. Graded findings

### CRITICAL

**None found.** I found no false displayed formula, missing endpoint, cycle, or
time-index error that invalidates a theorem. This does not clear the paper for
release because the owner-scope findings below remain unresolved.

### MAJOR (math)

#### M-MATH-1 — “unique attractor” is undefined and convention-sensitive

**Location:** abstract, lines 39--40; Lemma 3.1, lines 163--165; README and
narrative summary.

**Evidence:** the proof establishes the precise and stronger usable facts that
every orbit reaches \((n)\), that \((n)\) is fixed, and that no other periodic
point exists. It never defines “attractor.” In finite/discrete dynamics that word
can mean an attracting periodic class, a minimal global attractor, a trapping
invariant set, or a set satisfying a metric/neighbourhood definition. “Unique
attractor” is therefore not a theorem until a convention is fixed, even though
the intended global-absorption claim is correct.

**Executable fix:** replace every unqualified “unique attractor” by “globally
absorbing fixed point” (recommended), or define an attractor explicitly and prove
that the adopted definition makes \(\{(n)\}\) unique. State the concrete orbit
claim in the abstract: “every orbit reaches \((n)\).” No change to the algebraic
proof is needed.

### MAJOR (owner-scope)

#### M-OWN-1 — the subtraction boundary omits the standard principal-hook map and first-hook identity

**Location:** Introduction lines 51--68 and Lemma 3.1 lines 156--173.

**Evidence:** the manuscript subtracts only the image and fibre product, then
says “the contribution begins after this subtraction.” However,
[Gutschwager, Definition 2.2](https://arxiv.org/abs/0802.0417) explicitly defines
the principal hook length partition \(hl(\lambda)\) and writes
\(hl_1(\lambda)=\lambda_1+\ell(\lambda)-1\). This predates Goupil and is the
literal map/identity used as the Lyapunov input here. The dynamical deduction
from strict growth may still be residual, but equation (2) itself is not.
[Pak--Panova--Vallejo, Section 3.1](https://arxiv.org/abs/1304.0738) also uses
the same “principal hook partition” as standard representation-theoretic
notation.

**Executable fix:** add Gutschwager to the bibliography and owner table; label
the definition of \(H\), conjugation invariance of hook lengths, and the
first-hook formula as standard/zero-credit inputs. Rephrase Lemma 3.1 so that
the residual statement begins with the dynamical consequence (“strict growth
implies global absorption and excludes cycles”), not with ownership of the
identity.

#### M-OWN-2 — contribution density is overstated by listing immediate corollaries as co-equal results

**Location:** abstract lines 38--43, Introduction lines 61--68, and the theorem
architecture.

**Evidence:** after complete subtraction, the substantive mathematical item is
the exact gap increment and its sharp transient-depth consequence. The remaining
headline items have much lower independent content:

- absorption and the periodic census are immediate from the standard first-hook
  identity;
- the zeta formula is an automatic one-line consequence of that census;
- \(H(\lambda)=H(\lambda')\) is immediate from swapping Frobenius arms and
  legs, and the sole entrance-time exception is then one line;
- the layer “recurrence” is the general identity
  \(A_t=\sum_{\tau(h)=t-1}\#H^{-1}(h)\) with the owned fibre weight inserted;
  it is exact but does not independently evaluate the layers.

The clean four-page format magnifies this issue: page 4 is largely blank after
the short corollary discussion and three references. This is not a typesetting
fault, but it is a contribution-density signal.

**Executable fix:** position the manuscript as a short note with one main theorem
(exact gap growth plus sharp depth) and label attraction, layer transport,
conjugation, periodic census, and zeta explicitly as corollaries. Alternatively,
for a full-paper claim, add a non-tautological result such as an evaluated layer
generating function, a structural recurrence that eliminates \(\tau(h)\), or an
equality/deepest-state classification. Do not count the owned fibre product, the
standard first-hook identity, elementary conjugation symmetry, or formal zeta
algebra toward novelty.

#### M-OWN-3 — bounded search found no iterative owner, but the current three-reference audit cannot clear novelty

**Location:** global positioning and the current `references.bib`.

**Evidence:** exact-phrase and synonym searches for “principal hook partition,”
“principal/diagonal hook lengths,” “iterate,” “orbit,” “fixed point,” and
“dynamics” were checked against the primary sources listed in Section 4. No
source in that bounded corpus studied repeated application
\(\lambda\mapsto hl(\lambda)\). Gutschwager's uses of “iterate” concern recursive
northwest-ribbon constructions, and Chern--Yee's \(\phi\) is a different
involution that preserves diagonal hooks. This is useful collision screening,
not proof that an iterated owner does not exist.

**Executable fix:** retain external HOLD and conduct a database-level owner audit
before any novelty or priority language: MathSciNet/zbMATH, Zentralblatt citation
chains from Goupil and Gutschwager, forward citations using “principal hook
partition,” and searches in partition-dynamics terminology. Record databases,
dates, exact queries, screened result counts, and inclusion decisions. A failed
search must remain phrased “no exact owner located in the bounded search.”

### MINOR

#### MIN-1 — the balanced-path proof attributes the last step to the wrong displayed formula

**Location:** lines 240--249.

Equation (7), \(H(a,b)=(a+1,b-1)\), is stated only for \(b\ge2\). The proof then
says that “equation (7) takes exactly \(b\) steps,” but only the first \(b-1\)
steps use (7); the last uses the separately stated \(H(a,1)=(a+1)\). At
\(n=2\), equation (7) is used zero times.

**Executable fix:** write: “Apply (7) \(b-1\) times (zero times if \(b=1\)),
then apply \(H(n-1,1)=(n)\); hence the total is \(b\) steps.”

#### MIN-2 — make the dependence on the fixed weight explicit in the zeta notation

**Location:** Theorem 4.3, lines 327--340.

The same symbol \(H\) is used for the maps on all \(\mathcal P(n)\), while the
Artin--Mazur zeta function is attached to one finite system at a fixed \(n\).
The result is correct because it is identical for every \(n\ge1\), but the
quantification is easy to misread.

**Executable fix:** say “For each fixed \(n\ge1\), let \(H_n\) denote the
restriction to \(\mathcal P(n)\)” in the zeta theorem, or add one sentence that
\(n\) is fixed and suppressed from the notation.

#### MIN-3 — distinguish “recorded by Goupil” from the broader word “classical”

**Location:** abstract lines 36--38, Introduction lines 55--59, Proposition 2.1,
and its proof.

Goupil's 2009 preprint gives the exact hook-type product as Corollary 1 and
records the adjacent-gap condition. That is a direct owner. The manuscript has
not documented enough history to establish that every part of the packaged
image/fibre proposition should be called “classical.”

**Executable fix:** use “previously recorded/owned” unless a pre-Goupil source is
identified. Keep the zero-credit designation regardless.

#### MIN-4 — say explicitly that the layer formula is a transport identity

**Location:** Theorem 4.1 and the abstract phrase “recurrence for every depth
layer.”

The right side still requires knowing \(\tau(h)\), so “recurrence” may suggest
more computational closure than is present.

**Executable fix:** title it “fibre-weighted layer transport identity,” or add a
sentence that it is recursive in time over the much smaller one-step image but is
not a closed recurrence in \((n,t)\) alone.

## 4. Bounded primary-source owner audit

| Primary source | What it actually contains | Ownership decision for P113 |
|---|---|---|
| [Alain Goupil, *A product of integer partitions* (2009)](https://arxiv.org/abs/0906.3004) | Defines central-hook type, records the adjacent-gap admissibility condition, and gives in Corollary 1 the exact product \(k_r\prod_{i<r}(k_i-k_{i+1}-1)\). | Direct owner for the one-step image/fibre layer; manuscript subtraction is correct here. No repeated-map dynamics was located in the full text. |
| [Christian Gutschwager, *On principal hook length partitions and Durfee sizes in skew characters*](https://arxiv.org/abs/0802.0417), published with [DOI 10.1007/s00026-011-0084-7](https://doi.org/10.1007/s00026-011-0084-7) | Definition 2.2 defines \(hl(\lambda)\) as the principal hook length partition and explicitly states \(hl_1(\lambda)=\lambda_1+\ell(\lambda)-1\). | Missing direct owner for the map terminology and first-hook identity. Its “iteration” language concerns northwest-ribbon constructions, not \(hl^{\circ t}\). |
| [Shane Chern and Ae Ja Yee, *Diagonal Hooks and a Schmidt-Type Partition Identity* (2022)](https://doi.org/10.37236/10803) | Defines all diagonal hook lengths, proves a Schmidt-type identity, and constructs an involution preserving Durfee size and every diagonal hook length. | Relevant context and evidence that diagonal-hook fibres are active prior art, but not an owner for P113's iterated map, gap law, or transient depth. |
| [Igor Pak, Greta Panova, and Ernesto Vallejo, *Kronecker products, characters, partitions, and the tensor square conjectures*](https://arxiv.org/abs/1304.0738) | Uses \(\widehat\lambda\) for the principal hook partition as standard notation in representation theory. | Further evidence that the map object itself is standard; no repeated-map dynamics was located. |

The search was deliberately bounded: four direct primary texts plus several exact
phrase/synonym web queries and their relevant primary hits. Within that scope I
located no paper claiming the exact iteration, gap increment, sharp
\(\lfloor n/2\rfloor\) transient depth, or depth-layer transport. **This sentence
is a search report, not a novelty or priority conclusion.** Chern--Yee should not
be inflated into a dynamics owner, and the absence of a hit should not be used to
clear external release.

## 5. Fresh build and presentation audit

Only `main.tex` and `references.bib` were copied to the temporary audit
directory; no review artifact was included in the compilation. A fresh
`pdflatex`/`bibtex`/`pdflatex`/`pdflatex` sequence completed successfully.

- PDF: 4 pages, A4, 256,893 bytes, PDF 1.5.
- LaTeX/package warnings: 0.
- Overfull boxes: 0; underfull boxes: 0.
- Undefined references/citations: 0; multiply defined labels: 0.
- BibTeX-emitted warnings (`Warning--...`): 0. (The `.blg` identifier
  `warning$ -- 0` is an internal function statistic, not a warning.)
- Fonts: 20/20 embedded, 20/20 subsetted, and 20/20 with Unicode maps.
- Visual inspection: all four pages were rasterized and inspected. Page 1
  (title through setup), page 2 (owner proposition and gap theorem), page 3
  (layers, conjugation, zeta), and page 4 (proof-route discussion and references)
  have no clipping, collision, broken glyph, margin escape, or unreadable formula.
  Page 4 has substantial unused lower-page space, but this is a density issue,
  not a rendering defect.

The submitted build record is therefore reproducible in this environment.

## 6. Required revision checklist and release decision

Before any external circulation:

1. Replace or define “unique attractor” and lead with the proved global-absorption
   statement.
2. Add Gutschwager and move the map definition/first-hook formula into explicit
   zero-credit background.
3. Recast the paper around the exact gap increment and sharp depth; label the
   layer, conjugation, periodic, and zeta statements as transport/corollary
   consequences, or add a genuinely non-tautological layer/deepest-state result.
4. Fix the \(b-1\) plus final-step wording and clarify the fixed-\(n\) zeta
   notation.
5. Complete and document a broader owner audit. Preserve the sentence that a
   missing search hit does not establish novelty.

**Mathematical disposition after the listed local fixes:** likely sound as a
compact note; no theorem-level counterexample found.

**Ownership/novelty disposition:** not cleared.

**External dissemination, novelty, and priority:** **HOLD**.
