# Hostile Review B — round 1

**Role and independence.** This is an independent non-author review of
`main_round1.pdf` and the current source/support package. I did not open or use
Reviewer A's report. I made no changes to the manuscript, verifier, canonical
output, or PDF.

**Provisional verdict:** **REVISE, THEN GO INTERNAL; EXTERNAL HOLD.** The core
theorem package survives independent reconstruction, including all fibre,
recurrence, product, zeta, and basin formulas. There is no theorem-threatening
defect. There is, however, one literally false converse sentence in the passage
that transfers quotient recurrence back to graph colourings. It has a two-line
repair and does not change any count or theorem. That repair is required before
signoff.

## 1. Required repair

### MAJOR (mathematical statement, local and non-theorem-threatening): the stated converse is false

**Location:** `main.tex:358–360`, round-1 PDF p. 4.

The manuscript says:

> Every periodic graph colouring belongs to the image of \(\Phi_G\), hence is
> part-monochromatic. The converse is immediate from the quotient.

The literal converse—every part-monochromatic colouring is periodic—is false.
For the canonical phase on \(K_{1,2}\), where \(q=3\), the
part-monochromatic vector \((2,2)\) has orbit
\[
 (2,2)\longmapsto(0,0)\longmapsto(1,1)\longmapsto(0,0).
\]
Thus it is part-monochromatic but transient.

The intended conclusion and the displayed value
\(R_k=k!+2b_k\) are nevertheless correct. The exact repair is:

> Every periodic graph colouring lies in \(\operatorname{im}\Phi_G\) and hence
> is part-monochromatic. On the part-monochromatic subspace, coordinate
> identification intertwines \(\Phi_G\) with \(T\). Therefore the periodic
> graph states are exactly the lifts of \(\operatorname{Rec}_k\), so their
> number is \(R_k=k!+2b_k\).

With that replacement, Corollary 4.5 and the zeta product follow unchanged.

## 2. Independent mathematical reconstruction

### 2.1 Phase closure and the first-image quotient

For \(G=K_{a_1,\ldots,a_k}\), every open neighbourhood has size at most
\(\Delta=n-\min_i a_i<q\), so its mex lies in \(\{0,\ldots,q-1\}\). Equal
open neighbourhoods inside a part make the first image part-monochromatic,
with
\[
 y_i(c)=\operatorname{mex}c(V\setminus V_i),\qquad
 T(y)_i=\operatorname{mex}\{y_j:j\ne i\}.
\]
Also \(\Delta\ge k-1\), hence the standing condition implies \(q\ge k\);
all displayed recurrent coordinates therefore belong to the palette. For
\(k=1\), the graph is edgeless and every state maps in one round to the unique
part vector \((0)\).

### 2.2 Both exact fibre formulas

The inclusion–exclusion formula is exact. After imposing the absence of each
target colour \(y_i\) outside \(V_i\), the bad event indexed by \((i,r)\),
\(r<y_i\), is precisely the failure of colour \(r\) to occur outside
\(V_i\). Under a selected event set \(J\), a vertex of \(V_h\) has exactly
\(q-|B_h(y,J)|\) available colours. Indexed bad events remain distinct even
when their forbidden colour sets coincide, while the union in \(B_h\) removes
only duplicate forbidden colours. This yields the sign and product in (3.1),
including impossible targets and all \(k=1\) cases.

The support/EGF formula is independently correct. For a named colour \(r\),
the two conditions
\[
 y_i=r\Rightarrow P_r\subseteq\{i\},\qquad
 y_i>r\Rightarrow P_r\nsubseteq\{i\}
\]
are exactly the target absence and lower-colour presence conditions. Once all
supports are fixed, the restriction to \(V_i\) is an onto map onto its
\(d_i\) named colours, contributing \(d_i!S(a_i,d_i)\). This gives both the
onto sum and the labelled coefficient extraction. For \(r>\max y_i\), all
supports are allowed, and their factor is \(e^{x_1+\cdots+x_k}\), so the
surplus-colour exponential is also correct. These are genuinely different
counting routes, not two rewritings of the same inclusion–exclusion.

### 2.3 Quotient recurrence, including all boundary branches

Let \(g=\operatorname{mex}\{y_1,\ldots,y_k\}\). Direct deletion of coordinate
\(i\) gives
\[
 T(y)_i=
 \begin{cases}
 y_i,&y_i<g\text{ and }y_i\text{ is unique in }y,\\
 g,&\text{otherwise}.
 \end{cases}
\]
Let \(m\) be the mex of the retained unique values below \(g\).

- If \(m<g\), then \(m\) occurs in \(y\) but was not retained, so it occurs
  at least twice. Consequently at least two coordinates remain outside the
  injected low segment. The second quotient image is necessarily
  \(x^-_{\iota,m}\); the “one remaining coordinate” alternative mentioned in
  the present proof cannot occur in this branch.

- If \(m=g\), the first image retains \(0,\ldots,g-1\). With at least two
  remaining coordinates it is \(x^-_{\iota,g}\). With one remaining
  coordinate, \(g=k-1\), and with zero remaining coordinates, \(g=k\); both
  boundary cases are permutations of \(0,\ldots,k-1\).

Direct substitution swaps each \(x^-_{\iota,m}\) with
\(x^+_{\iota,m}\) and fixes each permutation. The fill value and positions of
the lower unique values recover \((m,\iota)\), so the cycles are disjoint.
This proves the stated complete list and
\[
 b_k=\sum_{m=0}^{k-2}\frac{k!}{(k-m)!}.
\]
For \(k=1\), the sum is empty and \((0)\) is the sole fixed state.

### 2.4 Why the labelled graph needs only two rounds

If two coordinates of a first-image vector agree at \(r\), the two target
conditions together make \(r\) globally absent. No larger target can then
occur, so only the maximum first-image value can repeat. Write
\(M=\max_i y_i(c)\) and \(g=\operatorname{mex}y(c)\). Necessarily either
\(g\le M\) or \(g=M+1\).

- For \(g\le M\), every value below \(g\) is unique, and \(T(y(c))\) is a
  fixed permutation or an \(x^-\) state.
- For \(g=M+1\), all values through \(M\) occur and all values below \(M\)
  are unique. A unique \(M\) gives a fixed permutation; a repeated \(M\)
  gives an \(x^+\) state.

Thus \(T(y(c))\in\operatorname{Rec}_k\), equivalently every labelled state
has preperiod at most two. This argument is correct and is stronger than the
generic quotient bound.

### 2.5 Closed recurrent fibres

All three products in Proposition 5.1 survived direct reconstruction.

- At a fixed permutation, colour \(r<k-1\) is confined to and required in
  its designated part; colour \(k-1\) is confined but optional; the \(q-k\)
  larger colours are free. This gives (5.1), including \(k=1\).
- At \(x^-_{\iota,m}\), each lower colour is confined to and required in its
  injected part, colour \(m\) is globally absent, and the \(q-m-1\) larger
  colours are free. This gives (5.2).
- At \(x^+_{\iota,m}\), colour \(m+1\) is globally absent. If colour \(m\)
  appears in a low injected part, it automatically satisfies every remaining
  part; this is \((L_1-L_0)Q\). Otherwise it must occur in at least two
  remaining parts; subtracting the absent and exactly-one-part cases gives
  \(L_0Q_{\ge2}\). This proves (5.3), including \(m=0\), \(u=0\), empty
  products, and the stated combinatorial \(0^0\) convention.

### 2.6 Exact quotient preimages and every basin

Equations (6.1)–(6.3) are exact. A fixed permutation output forces the lower
\(k-1\) values to occur uniquely in their prescribed coordinates, while the
last input can be any value at least \(k-1\). An \(x^-\) output forces its
prescribed low values and inputs strictly above \(m\) elsewhere. An \(x^+\)
output forces global mex \(m+1\), hence at least two occurrences of \(m\) in
the remaining coordinates and excludes \(m+1\).

Consequently, if \(S_{\mathbf a,q}\) is the total fibre mass over recurrent
first images, then
\[
 D_0=R_k,\qquad D_1=S_{\mathbf a,q}-R_k,\qquad
 D_2=q^n-S_{\mathbf a,q}.
\]
For one recurrent orbit \(\mathcal O\), summing
\(H_x=\sum_{T(y)=x}N_{\mathbf a,q}(y)\) over \(x\in\mathcal O\) counts its
entire basin, and successive subtraction yields (6.6)–(6.8). For \(k=1\),
these specialize to \(D_0=1\), \(D_1=q^{a_1}-1\), and \(D_2=0\), as they
must.

## 3. Minor repairs and control-scope corrections

1. **Make the impossible \(m<g\) subcase explicit** (`main.tex:294–305`).
   Replace the generic “when one remains” language in this branch by the
   observation that \(m\) is present but nonunique in the input. Hence
   \(k-m\ge2\). In the \(m=g\) branch, explicitly identify zero remaining
   with \(g=k\) and one remaining with \(g=k-1\). The current classification
   is correct; this repairs only the branch proof.

2. **State palette capacity once** (`main.tex:115–126`). Add
   \(\Delta\ge k-1\), hence \(q\ge k\). The implication is already true and
   all formulas use it correctly.

3. **Reintroduce local notation** (`main.tex:436–452`). Proposition 6.1 uses
   \(R\) and \(i_r\) in (6.2)–(6.3) without defining them inside that
   proposition. Add
   \(R=[k]\setminus\operatorname{im}\iota\) and \(i_r=\iota(r)\).

4. **Define depth formally** (`main.tex:473–505`). Before Theorem 6.2, define
   \(\operatorname{depth}(c)=\min\{t\ge0:\Phi_G^t(c)\in
   \operatorname{Rec}_k\}\), with recurrent quotient vectors identified with
   their part-monochromatic lifts. The layer formulas themselves are correct.

5. **Soften or extend the verifier description**
   (`CLAIMS_EVIDENCE.md:8`). The phrase “Complete quotient graphs in every
   lane” is stronger than the current script: the script enumerates quotient
   states for exact preimage comparisons, but it does not directly assert for
   every arbitrary quotient state that \(T^2(y)\in\operatorname{Rec}_k\) or
   independently extract the quotient cycle set. Either say exactly what is
   checked, or add those two direct assertions. This is a control-coverage
   issue, not a gap in the proof.

6. **Repeat the 2018 subtraction in the closing owner ledger**
   (`main.tex:520–527`). Faghih et al. are correctly cited and subtracted in
   the abstract and Introduction, but Section 7 names only the 2003 work as
   the closest rule-level owner. Repeating the 2018 protocol-synthesis
   subtraction there would make the final claim ceiling self-contained.

## 4. Owner subtraction and claim ceiling

The added Faghih citation is bibliographically exact: F. Faghih,
B. Bonakdarpour, S. Tixeuil, and S. Kulkarni, “Automated Synthesis of
Distributed Self-Stabilizing Protocols,” *Logical Methods in Computer
Science* 14(1:12), 1–25 (2018), DOI
`10.23638/LMCS-14(1:12)2018`. The [official LMCS article
page](https://lmcs.episciences.org/4241) and [official
PDF](https://lmcs.episciences.org/4241/pdf) confirm the metadata, explicit
timing-model framework, and inclusion of distributed Grundy colouring. That
paper studies synthesis of guarded self-stabilizing protocols; it does not
supply the unconditional simultaneous mex functional graph on complete
multipartite graphs or the present exact temporal census. The manuscript's
zero-credit subtraction is therefore accurate.

The 2003 Hedetniemi–Jacobs–Srimani paper owns the local Grundy/mex correction
and scheduler-dependent self-stabilizing setting; the DOI metadata in the
bibliography also closes. Generic labelled-EGF and finite-map zeta machinery
are appropriately assigned zero contribution credit. No arbitrary-graph,
asynchronous, complexity, novelty, or priority claim is made. The residual
claim ceiling—this synchronous complete-multipartite conjunction of exact
fibres, image shape, two-round recurrence, recurrent products, and basin
layers—is respected. The bounded search non-hit is correctly not presented as
novelty evidence.

## 5. Fresh computational, citation, and PDF controls

- **Canonical verifier:** fresh run passed **201,922 assertions**. Its stdout
  byte-compared equal to `code/verification_output.txt`, whose SHA-256 is
  `6130da8d004126ee51151e3f40f8af9692d087fec0a921a504f95f3b3aba668e`.
  The lanes include \(k=1\), enlarged palettes, \(K_{1,2,3}\) with 46,656
  labelled states, and \(K_{2,2,2}\) with 15,625 states.

- **Independent audit:** a separate enumeration, without importing the
  author's recurrence classifier, passed **199,832 checks** over 47,303
  quotient states and 1,043 labelled graph states. It checked fibres,
  preimages, products, actual cycle sets, depths, and basins. In particular it
  exercised 9,882 \(m<g\) cases and 37,421 \(m=g\) cases, including 1,071
  zero/one-remaining boundary cases.

- **Fresh isolated build:** `pdflatex`–`bibtex`–`pdflatex`–`pdflatex` produced
  a settled seven-page A4 PDF with no errors, undefined references/citations,
  warning, overfull/underfull box, or rerun request. All **6/6** bibliography
  entries are cited and rendered, including the Faghih DOI.

- **Delivered PDF:** `main_round1.pdf` and current `main.pdf` are byte-identical,
  **379,370 bytes**, SHA-256
  `ea59b099e61c0f6f32cf03b2290dcb68507027c91dd348e2710c03976e813156`.
  All seven pages were rendered and visually inspected. Layout, equations,
  table, and references are clean, with no clipping or collision.

- **PDF hygiene:** all **27/27** font instances are embedded, subset, and
  Unicode-mapped. Author metadata is empty; the file is date-free, unencrypted,
  unrotated, and has no form or JavaScript. The visible manuscript remains
  anonymous.

## 6. Final disposition

**CRITICAL:** none.

**MAJOR (math):** the false converse at `main.tex:358–360`; repair is mandatory
and specified above.

**MAJOR (owner/scope):** none.

**MINOR:** the six proof, notation, control-description, and owner-ledger items
in Section 3.

**Theorem-threatening issue:** **none.** The counterexample defeats only an
overbroad transition sentence, not the recurrent-state census or any ensuing
formula. After that sentence is replaced and the local minor items are
cleaned, the round-1 package is suitable for the next internal gate. External
dissemination remains **HOLD**.
