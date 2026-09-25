# Current divisor inertial secant: owned clock and the entire fixed-point gate

Candidate ID: `ANG-20260925-DIS01`.
Outcome: OWNED SECANT CLOCK; PRIME-2 FIXED PACKET — BOUNDED OPEN / FORK
Paper468; batch `ADMISSION-CORE-20260925-X`, round4/5; 2026-09-25.
Status: exact global fixed-point classification for four separately owned maps.
Classical NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

The full real plane carries a rational two-state update whose content, remainder and inertial coefficient are recomputed from the current coordinates.
All regular inverse roots, including roots at floor faces, own their geometric every-Borel IMAGE and clock.
The complete MAIN fixed set is one point \((\sqrt[3]2,\sqrt[3]2)\), with primitive \(\log2\) and no incoming states other than itself.
The remainder-OFF owner independently reproduces that fixed packet.
The content-OFF owner has one actual zero-clock fixed point; the memory-OFF owner's sole formal fixed point is critical and terminal, not an actual periodic state.
All four inverse atlases and full-history clock laws are derived without a root or depth cutoff.
These fixed-only results do not establish global prime-only support, global prime uniqueness, all-prime coverage or an endogenous prime-generating mechanism.

## 1. Frozen owners and lineage

| Item | Exact owner / boundary |
| --- | --- |
| Carrier | Each owner has its OWN full \(X=\mathbb R^2\), ordinary Borel structure and original Lebesgue area |
| Readouts | \(A=1+\lfloor\lvert x\rvert\rfloor,\ B=1+\lfloor\lvert y\rvert\rfloor,\ g=\gcd(A,B),\ r=A-B\lfloor A/B\rfloor\), recomputed each step |
| MAIN | \((G,R,H)=(g,r,g)\) |
| C: content-OFF | \((G,R,H)=(1,r,1)\) |
| R: remainder-OFF | \((G,R,H)=(g,0,g)\) |
| I: inertial-memory-OFF | \((G,R,H)=(g,r,0)\) |
| Legal domain | Own denominator and own assigned analytic-germ determinant both nonzero; everything else remains terminal |
| Clock and packet owner | All-point geometric inverse IMAGE, actual lag-clock extension, entire isotropy-clock image and all real phases |
| Classical / analytic fields | No positive roof, symplectic suspension, Hamiltonian lift, operator, trace or zeta |

On each assigned arithmetic cell put
\[
 D=x^2+xy+y^2-R,\quad N=xy(x+y)+G,\qquad
 F(x,y)=\left(y,\frac ND+H(x-y)\right).
\]
The constants \(G,R,H\) are frozen only when taking the cell's analytic germ; the actual map rereads them after each step.
For integers \(N_0,d\) with \(1<d<N_0\), the proper-divisor interface \((x,y)=(N_0-1,d-1)\) has readouts \(A=N_0,B=d\), and \(d\mid N_0\) exactly when \(r=0\).
This changes the actual denominator; MAIN content also changes numerator and memory feedback.
The arithmetic identity does not guarantee the separate geometric guard at that seed.
The lineage is divisor/content symbols → current rational divided differences and memory → regenerated geometric readouts, with no passive integer register.
This is neither a prime predicate nor an autonomous owner replaced by a time-dependent fitting schedule.

## 2. Question, frozen input and stop boundary

The [121-line card](candidate-card.md) has SHA256
`fc36a5a9d68b245feb00f6da52a9d568122bfb9352cbe0f27e6ca0e7fb6bd10e`.
The gate is the ENTIRE actual fixed set of MAIN/C/R/I, with full incoming and clock data for every found core.
No period-two or higher search is performed.
An owned MAIN nonprime primitive, duplicate prime packet or ownership failure would stop/fork; absent such a witness, this short gate ends bounded OPEN/FORK.
Control results neither transfer to MAIN nor automatically condemn it.
Full inverse recursion and actual-history predicates are exact global descriptions, not a claim that every higher-period core has been enumerated.
Strong naturalness and arbitrary-encoding / PROVES_TOO_MUCH remain OPEN.

## 3. Own regularity, complete inverse roots and every-Borel IMAGE

Write
\[
 U_y=y^3-Ry-G,\quad U_x=x^3-Rx-G,\quad
 L=H+\frac{(2x+y)U_y}{D^2},\quad
 M=-H+\frac{(x+2y)U_x}{D^2}.
\]
The quotient rule gives
\[
 DF=\begin{pmatrix}0&1\\L&M\end{pmatrix},\qquad \det DF=-L .
\]
For example \(yD-N=y^3-Ry-G\), which proves the formula for the \(x\)-derivative; the other formula follows from \(xD-N\).
Thus each actual domain is exactly \(D\ne0,L\ne0\) with its OWN coefficient law.
All signed, critical, pole and floor-face states remain in \(X\), whether or not they can depart.

At target \((u,v)\), a predecessor has the form \((x,u)\).
For every source cell its complete algebraic test is
\[
 P(x;u,v)=(v-H(x-u))(x^2+xu+u^2-R)-xu(x+u)-G=0 .
\]
After taking ALL real roots, require the reconstructed source's actual \(A,B\), its recalculated coefficients, \(D\ne0,L\ne0\), and forward equality.
Necessity is multiplication by a nonzero actual denominator; conversely the equation with \(D\ne0\) gives the displayed forward map exactly.
No target next-step condition occurs.
On an actual root,
\[
 P_x=-D\,L\ne0,
\]
because \(P=D(v-F_2(x,u))\) and its second factor vanishes there.
Hence every admitted root is simple. If a polynomial is identically zero, none of its roots with \(D\ne0\) can pass the regularity test.
Degree drops are therefore handled without dividing by a possibly zero coefficient.
For MAIN/C/R the leading coefficient is \(-H\ne0\); I has degree at most two, including its constant and identically-zero cases.
There are at most finitely many admitted roots per cell and countably many source cells, not a uniform finite bound on the whole predecessor set.

For atlas construction the cells
\[
 C_{AB}=\{A-1\le |x|<A,\ B-1\le |y|<B\},\qquad A,B\ge1,
\]
with a disjoint sign refinement if needed, partition every actual point.
Each assigned rational germ is analytic on the open set \(D\ne0,L\ne0\).
The inverse function theorem supplies local analytic diffeomorphisms there.
The fixed rational-ball enumeration covers this locus by balls on which that cell germ is injective; intersect with the actual cell and subtract earlier eligible pieces.
These countably many disjoint Borel source pieces cover the full legal domain.
Their images are Borel because each surrounding chart is a homeomorphism onto an open image; restricting its inverse gives the actual branch.
The all-root test above and the chart coverage prove both algebraic and atlas completeness, including every null face.

For an actual inverse \(\theta\) and source \(z=\theta w=(x,y)\), the frozen geometric version is
\[
 J_\theta(w)=|\det D\theta(w)|
           =\frac1{|L(\theta w)|}
           =\frac{D(z)^2}{|H D(z)^2+(2x+y)U_y(z)|}>0 .
\]
It is finite at every actual point.
Overlapping charts through the same assigned source have the same inverse derivative, the inverse of its unique cell-germ \(DF\); first-eligible disjointization changes no value.
The ordinary change-of-variables formula on a chart, restricted to an arbitrary Borel subset \(B\) of the actual inverse domain, gives
\[
 \mu(\theta B)=\int_B J_\theta\,d\mu .
\]
This proves each owner's every-Borel IMAGE, not merely a formula outside a null set.
Only then its own legal-step clock is
\[
 \kappa(z)=-\log J_{\rm actual}(Fz)=\log|L(z)|.
\]
Signed and zero values remain. There is no outgoing clock at a terminal and no density or roof substitution.

## 4. Entire histories, history-pair IMAGE and all kernels

All statements in this section apply separately with each owner's actual \(D,L,F\).
For a legal \(n\)-step history set
\[
 V_0(z)=1,\quad V_n(z)=\prod_{j=0}^{n-1}|L(F^jz)|,\qquad S_n(z)=\log V_n(z).
\]
Every factor is positive and finite. A complete inverse word \(\Theta\) of depth \(n\), with source \(z=\Theta y\), has all-point IMAGE \(J_\Theta(y)=V_n(z)^{-1}\).
The one-step IMAGE gives the weighted substitution identity first for indicators, then nonnegative simple functions and monotone limits.
Applying it repeatedly proves the product identity for EVERY Borel subset of the actual word domain, including all intermediate permission restrictions.

For a target \(p\), let \(\mathcal B_0(p)=\{p\}\) and
\[
 \mathcal B_{n+1}(p)=\bigcup_{w\in\mathcal B_n(p)}\operatorname{Inv}(w),
\]
where \(\operatorname{Inv}\) uses all cells and all admitted polynomial roots from §3.
Induction proves \(\mathcal B_n(p)=\{z:F^nz=p\text{ legally}\}\) for every \(n\).
All compatible inverse sequences are retained; no branch or depth cutoff is used.
This describes actual predecessors, not points which merely converge to \(p\) without ever reaching it.

Use all actual triples
\[
 \mathcal G=\{(z,m-n,w):F^mz=F^nw\text{ legally},\ m,n\ge0\},
 \qquad c(z,m-n,w)=S_m(z)-S_n(w).
\]
Source is \(w\), range is \(z\); equal triples are identified and the integer lag is retained.
Two witnesses for the same triple differ by an equal shift in both depths, adding the same common-tail sum, so \(c\) descends.
Composition aligns middle-state depths by a legal common-tail extension, after which the middle sums cancel; hence \(c\) is additive.
The forward arrow \((Fz,-1,z)\) has clock \(-\kappa(z)\).

For the promised actual history-pair IMAGE, take inverse words \(\Theta_a,\Theta_b\) of lengths \(m,n\) on a common actual target domain.
The map \(\chi=\Theta_a\circ\Theta_b^{-1}\) sends \(w=\Theta_b y\) to \(z=\Theta_a y\).
For every Borel subset of its actual domain, weighted substitution proves its image density
\[
 J_\chi(w)=\frac{J_{\Theta_a}(y)}{J_{\Theta_b}(y)}
          =\frac{V_n(w)}{V_m(z)}=e^{-c(z,m-n,w)} .
\]
All versions are pointwise fixed products; duplicate witnesses agree by the descent proof.
Every arrow is covered by such history pieces, including length0 identities at terminals.

The COMPLETE kernels, on the entire source, are the actual meeting triples satisfying
\[
 K_{\rm lag}:\ m=n,\qquad
 K_c:\ V_m(z)=V_n(w),\qquad
 K_{\rm joint}:\ m=n\text{ and }V_m(z)=V_m(w).
\]
These are exact unrestricted tests, not assertions that the kernels are units globally.
All terminal and infinite source classes are exactly the actual common-tail equivalence classes specified by \(\mathcal G\).
A finite-forward class can equivalently be identified by its terminal endpoint: two finite histories meet exactly when those endpoints agree.
For terminal \(t\), depths \(d_z\) and sums \(\beta_z=S_{d_z}(z)\), its arrows are exactly \((z,d_z-d_w,w)\), with clock \(\beta_z-\beta_w\).
This includes all terminal incoming, without adding absorbing loops.

## 5. Isotropy, physical phases and complete core convention

Write \(\mathcal H_z=c(\mathcal G_z^z)\) for the isotropy-clock image, distinct from the inertial coefficient \(H\).
A source has a nonzero-lag loop if and only if its actual forward history is eventually periodic.
At a least-\(q\) core with signed cycle sum \(C\), and at every actual incoming source reaching that core, source isotropy is \(q\mathbb Z\).
Every loop clock is \(nC\) at lag \(nq\): witness after arrival for existence, and use least period for the converse.
Thus the ENTIRE \(\mathcal H_z=C\mathbb Z\); extension isotropy is \(q\mathbb Z\) if \(C=0\), and zero otherwise.
Terminal and non-eventually-periodic sources have zero source isotropy and \(\mathcal H_z\).
These laws classify isotropy whenever such a core occurs; they do not assert that higher-period cores have been searched.

The full height extension acts by \((w,h)\mapsto(z,h+c(g))\).
For a packet reference \(p\), choose an actual arrow \(g_z:p\to z\), put \(a_z=c(g_z)\), and retain every phase \([h-a_z]\in\mathbb R/\mathcal H_p\).
Two choices differ by an isotropy clock, and equality modulo \(\mathcal H_p\) supplies an adjusted arrow, proving completeness of this phase test.
Changing reference only translates the coordinate; no global measurable selector or nice quotient is presumed.
Height translation on this orbit SET has stabilizer exactly \(\mathcal H_p\).
When \(C\ne0\), its primitive is \(|C|\), with all positive integer repetitions; \(\mathcal H_p=0\) has all real phases and no positive return.
Zero-clock source isotropy remains visible instead of being confused with a positive periodic flow.

For any eventual core, choose one phase \(p\), arrival depths \(d_z\) to \(p\), and \(\beta_z=S_{d_z}(z)\).
The entire incoming packet has the exact formulas
\[
 (z,k,w)\in\mathcal G\iff k-d_z+d_w\in q\mathbb Z,\qquad
 c=\beta_z-\beta_w+\frac{k-d_z+d_w}{q}C .
\]
Extending a meeting to the core proves necessity; sufficiently large arrival depths give sufficiency.
These formulas also give every incoming kernel and phase, and are independent of the chosen arrival depths.

## 6. Global fixed-point classification for all four owners

A fixed point must be \((t,t)\).
Its readouts satisfy \(A=B=n=1+\lfloor|t|\rfloor\), \(g=n,r=0\).
The denominator is \(3t^2\), so \(t=0\) is forbidden for every owner.
Since the inertial term vanishes on the diagonal, the fixed equation is exactly
\[
 t^3=G .
\]
All \(G\)'s are positive, so every formal fixed point has \(t>0\).
For MAIN/R/I, \(G=n\).
If \(0<t<1\), the equation would require \(t=1\), outside that cell.
If \(1\le t<2\), it has the unique solution \(\alpha=\sqrt[3]2\in(1,2)\).
For \(t\ge2\), \(t^3\ge4t>t+1\ge1+\lfloor t\rfloor=n\), so no solution remains.
This covers all real cells, including every integer boundary, without an arithmetic cutoff.
For C, \(G=1\), giving only \(t=1\), assigned to the actual floor-face cell \(A=B=2\).

At any such formal fixed point, \(U_y=t^3-G=0\), so \(L=H\).
The own regularity tests and clocks are therefore:

| Owner | Entire actual fixed set | Own determinant / clock | Status of formal exceptions |
| --- | --- | --- | --- |
| MAIN | \(p=(\alpha,\alpha)\) | \(\det DF=-2,\ J=1/2,\ \kappa=\log2\) | No other formal root |
| R | \(p=(\alpha,\alpha)\) | \(\det DF=-2,\ J=1/2,\ \kappa=\log2\) | Independently owned control |
| C | \(p_C=(1,1)\) | \(\det DF=-1,\ J=1,\ \kappa=0\) | Actual null floor-face point |
| I | Empty | No fixed-source clock | Formal \(p\) has \(L=0\), hence is terminal |

In C the all-point geometric prescription fixes the clock at the integer face; an almost-everywhere version would not settle this point.
In I, the unit at \(p\) is not an actual lag1 periodic arrow.

## 7. Complete all-cell incoming for the fixed gate

The inverse recursion can be closed exactly for these targets.
For target \((t,t)\), its second-source readout is \(B=2\) in every case.
Thus even \(A\) gives \(g=2,r=0\), and odd \(A\) gives \(g=1,r=1\).
Substitution into the COMPLETE inverse polynomial yields:

| Target / owner | Even \(A\): polynomial in \(x\) | Odd \(A\): polynomial in \(x\) |
| --- | --- | --- |
| MAIN, \(t=\alpha\) | \(-2x^3+4\) | \(-x^3+x+3-2\alpha\) |
| R, \(t=\alpha\) | \(-2x^3+4\) | \(-x^3+3\) |
| C, \(t=1\) | \(-x^3+1\) | \(-x^3+x-1\) |
| I, formal \(t=\alpha\) | Identically0 | \(1-\alpha\ne0\) |

The even-A roots for MAIN/R and C are respectively \(x=\alpha\) and \(x=1\), both with actual \(A=2\), and they are regular as proved above.
R's odd-A polynomial has only \(x=\sqrt[3]3\in(1,2)\), whose actual \(A=2\) rejects that odd-cell root.
For MAIN's odd case write \(f_0(x)=x^3-x\) and \(k=3-2\alpha\).
Since \(1<\alpha<13/10\), proved by cubing the endpoints, \(2/5<k<1\).
An odd source cell has either \(|x|<1\) or \(|x|\ge2\).
For \(|x|<1\), elementary differentiation gives \(|f_0(x)|\le2/(3\sqrt3)<2/5\); the last inequality is equivalent to \(25<27\).
For \(x\ge2\), \(f_0(x)\ge6\), and for \(x\le-2\), \(f_0(x)\le-6\).
None can equal \(k\), so MAIN has no admitted odd-A predecessor.
The same bounds exclude C's odd equation \(f_0(x)=-1\).
These arguments exclude ALL odd cells, not merely nearby ones.

For I's even case, \(H=0\) and \(U_y=\alpha^3-2=0\), making \(L=0\) at every nonpole root; no point of the identically-zero inverse polynomial is admitted.
Its odd case has no root at all.
Consequently
\[
 \operatorname{Inv}_{\rm M}(p)=\operatorname{Inv}_{\rm R}(p)=\{p\},\qquad
 \operatorname{Inv}_{\rm C}(p_C)=\{p_C\},\qquad
 \operatorname{Inv}_{\rm I}(p)=\varnothing .
\]
Induction in the unrestricted inverse recursion proves that each actual fixed core has full incoming equal to its singleton, at EVERY depth.
All its backward and forward histories are the constant actual fixed history; there are no additional transient sources in that packet.
The formal I point is an isolated terminal singleton, with only its unit and no incoming.

For MAIN and R separately the fixed packet's entire groupoid is \(\{(p,k,p):k\in\mathbb Z\}\), \(c=k\log2\).
Its lag, clock and joint kernels are units; source isotropy is \(\mathbb Z\), extension isotropy0, ENTIRE \(\mathcal H_p=\log2\,\mathbb Z\), phases \(h\bmod\log2\).
The primitive is \(\log2\), and every repeat is \(n\log2\).
For C, its fixed groupoid has the same integer lags but all clocks vanish.
The lag and joint kernels are units, the clock kernel and extension isotropy are the whole \(\mathbb Z\), \(\mathcal H_{p_C}=0\), and phases are all \(h\in\mathbb R\); there is no positive primitive.
At I's isolated terminal point all kernels consist only of its unit, source/extension isotropy and \(\mathcal H_p\) vanish, and all real phases remain.
These are complete fixed-packet ledgers; global kernels elsewhere remain the exact unrestricted tests of §4, not a claim that every global kernel is trivial.

## 8. Controls, assessment and decision

The content-OFF and memory-OFF controls remove the MAIN positive fixed clock in different ways: zero-clock actual isotropy versus failure of actual fixed admission.
Remainder-OFF reproduces the MAIN positive fixed packet.
Thus this fixed gate cannot show that proper-divisor remainder displacement is necessary for the observed \(\log2\).
The R packet is not a second MAIN packet: multiplicity never pools distinct owners.
Nor does its existence automatically refute MAIN; the frozen conclusion is bounded OPEN/FORK.
All regularity, inverse and boundary controls use their own coefficients and original measure.
No prime table, fitted logarithmic roof, per-prime parameter, precision cutoff or numerical census is used.

| Gate | Evidence for this exact owner | Boundary |
| --- | --- | --- |
| T0 | Complete actual inverse atlas, all-point every-Borel IMAGE and full-history IMAGE established | Piecewise measured owner, not a classical symplectic map |
| T1 clock COMPONENT | Own \(\log\lvert L\rvert\) clock; MAIN fixed primitive \(\log2\) established | Arithmetic T1 NOT PASSED; R reproduces the fixed packet |
| T2 fixed gate | All four entire fixed sets, complete incoming, kernels, \(H\), phases and repeats established | Higher periods, global purity/uniqueness and all-prime coverage OPEN |
| T3 | NOT AUDITED | No operator, trace or zeta |
| Classical / formal / B | NOT APPLICABLE / UNASSIGNED / NOT INVOKED | No Route evaluator invoked |

Decision: BOUNDED OPEN / FORK after the frozen fixed-only gate.
The same-object ledger remains intact; none of the controls repairs or replaces MAIN.
No extra period window, parameter tuning, formula change, later operator claim or paper470 is authorized by this result.

## Reproducibility and AI/access disclosure

Data/proof availability: exact inputs and results are in the [card](candidate-card.md), this paper, [claim ledger](claim-ledger.md) and [overview](README.md), using the [paper template](../paper-template.md).
Author read the entire121-line card with `sed -n '1,145p'`; `wc -l` and `sha256sum` identify the frozen bytes in §2.
The template107, ARS skill488, academic-paper workflow544, runtime policy113 and local AGENTS/plan were personally read and retained from the preceding authorized work.
Proof methods are exact differentiation, polynomial identities, global cell inequalities, change of variables and unrestricted inverse induction.
Mechanical checks are full author-file self-read, matching ID/Outcome, local links, Markdown table columns and unchanged frozen-card hash.
No scientific code/numerics, network, old edits, Git mutation, PDF, target-zero data or external publication was used.

AI author `/root/batch_clock_scope_review` supplied the derivation, drafting and internal checking; root owns card/integration.
No helper was used for this proof stage, and no current CP1 text, raw, reviewer, peer, helper proof or old paper/proof was read.
The rejected parameter-continuation design duplicated443, whose original1–99 prefix was read, SHA `f9d2dac20d66d35e7a36ef63c53ca350827bd28a69dd98f36df5547df2ac9f2d`; prior authorship already exposed historical results.
For the secant design, the actual435card read was1–105/109, prefixSHA `510e309579f3c39a5153707f9d9a669c04d21825fedc02ce0757ddfae92dcc79`, inadvertently including Outcome and partial result prose beyond the original96 lines.
That exposure, root's historical reads and informal fixed-equation/clock feasibility are disclosed in the card, not called blind preregistration; no old theorem is transferred.
Definition comparison distinguishes the old complex quadratic Newton owner from this real two-state cubic secant with content-weighted inertia, without a novelty or nonconjugacy certificate.
Same-model/shared-history AI assistance is `NOT_CALIBRATED`, not independent-error, cross-model, blind, human or external validation.
No human or external mathematical verification is certified. Human contributions, funding and competing interests are unspecified; no human-participant or sensitive personal data are involved.
ARS supplied bounded scope, drafting and integrity/disclosure discipline, not a publication pipeline; `criteria_binding_unavailable`, with no venue-readiness claim.
