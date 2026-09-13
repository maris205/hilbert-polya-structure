# Paper31 complete candidate brief: initial contacts and fixed-scheme thickness in a fixed Tate pencil

Date: 2026-09-12 UTC. Prepared by `/root`.
Status: `COMPLETE_SCIENTIFIC_CANDIDATE / V1–V3_UNDIVIDED / ADMISSION_OPEN`.
route_applicability: NOT_APPLICABLE.
This is a scientific brief, not a manuscript, section plan, source/publication lock, or admission vote.

## 1. The decision and the strongest objection

The candidate determines initial intersection multiplicities of one specified section on the original fixed-time autonomous qPI pencil.
It gives exact initialization at every prime-field good parameter and every finite nodal parameter in the stated characteristics, then supplies the exponents in the original fixed schemes.
The question is whether this unified, proved finding has sufficient novelty, independent scientific value, proof confidence, and natural substance for the unchanged standalone-paper contract.
The need for a fifth paper, accumulated effort, and the number of formulas are not evidence for any gate.

The [preflight disposition][PRE] preserves the independent [C/D assessment][CD]: **novelty 6.8/10, PROCEED_WITH_CAUTION**.
All three claims have LOW method novelty and MEDIUM finding novelty. The strongest objection is that the result remains a precise specialization of classical tools to a classical marked normal form.
The node's unique second-order exception is the most distinctive concrete phenomenon; it is not a new general Tate or deformation method.
Neither this brief nor the proof map changes that assessment. The two formal reviewers must receive its full reasoning and source gaps, not just the positive statement that unknown initial intersections have now been evaluated.

The earlier mathematical input genuinely changed: the [previous package][OLD] retained unknown initial intersections in its fixed-ideal formula, whereas [MATH] now accepts their exact values in the stated ranges.
This is the first complete-candidate review of this V1–V3 fingerprint, not a new vote on the unchanged earlier interface or the unrelated nonunit-time candidate.
The manuscript, Paper31 project, source/publication locks, and PDF do not yet exist. No trial prose layout or page measurement has been performed.

## 2. The original object and the necessary existing interfaces

Fix a nonzero time $T$ and the autonomous map and energy

$$
F_T(x,y)=\left(\frac{T}{x-y},\frac{x}{y}\right),\qquad
h=-x+y+\frac{x}{y}-\frac{T}{x}.
$$

The original surface $S_T$ is obtained from $\mathbf P^1\times\mathbf P^1$ by the four ordered clusters of $1+2+3+2$ blowups.
They are the original unit-time construction with map multiplier $1$, not a new compactification chosen from an elliptic equation:

1. Blow up $(x^{-1},y-1)=(0,0)$.
2. Blow up $(x,y^{-1})=(0,0)$, then the point $xy=T$ on its exceptional curve.
3. Blow up $(x,y)=(0,0)$, then the intersection of its exceptional curve with $y=0$, then the point $x^2/y=T$ on the next exceptional curve.
4. Blow up $(x^{-1},y^{-1})=(0,0)$, then the point $y/x=1$ on its exceptional curve.

Remove only the original anticanonical eight-cycle $D$, and write $\mathcal U=S_T\setminus D$.
Its four terminal charts, with local coordinates $a,b$, are

$$
\begin{array}{c|cc}
1&x=a^{-1}&y=1+ab\\
2&x=a(T+ab)&y=a^{-1}\\
3&x=a(T+ab)&y=a^2(T+ab)\\
4&x=[a(1+ab)]^{-1}&y=a^{-1}.
\end{array}
$$

The complete terminal lines $a=0$ belong to $\mathcal U$. The map extends over every legitimate state; it is not restricted to the denominator-free torus.
The existing geometric proofs supply $(h)_\infty=D$, the base-point-free pencil, properness and flatness over the finite base, and integral reduced finite fibers of arithmetic genus one.
The actual Picard pullback and integer degree growth prove that the generic return has infinite order in every relevant characteristic.
These are necessary original-object proofs, not new contributions of this candidate and not consequences of finite-field sampling.

The marked cubic, short coordinates, and local parameters are

$$
W_h:v^2+huv-Tv=u^3-Tu^2,\qquad O=[0:1:0],\quad P=(0,T),\quad t_O=-u/v,
$$

$$
\begin{gathered}
s=h^2-4T,\quad q=8h-9,\quad H=32T+3h,\quad b=2h^2-3h-8T,\\
\delta=h^4-h^3-8Th^2+36Th+16T^2-27T,\\
c_4=s^2+24hT,\quad c_6=-s^3-36hTs-216T^2,\\
X=u+s/12,\quad Y=v+(hu-T)/2,\quad a_4=-c_4/48,\quad a_6=-c_6/864.
\end{gathered}
$$

Thus $Y^2=f(X)=X^3+a_4X+a_6$, $P=(s/12,T/2)$ in short coordinates, and $\Delta=T^3\delta$.
Here $q$ is only the displayed linear polynomial; it is neither the original map multiplier nor a Tate smoothing parameter.
The complete fixed-scheme conclusions below are in characteristic $p>3$.
The characteristic-zero claims are the actual-contact conclusion in V1 and the finite-order nodal boundary in V3; they do not assert a characteristic-zero global exceptional spectrum.

The [existing fixed-scheme interface][FIX] proves, in its stated positive-characteristic range, the specified same-base isomorphism on the entire finite base

$$
\phi:\mathcal U\xrightarrow{\sim}W,\qquad
\phi(x,y)=\left(\frac{T}{y},\frac{Tx(y-1)}{y^2}\right),\qquad
\phi F_T=\tau_P\phi.
$$

Its extension uses actual regular minimal proper models, not a gluing of finite point-set bijections.
Let $C^{\rm ss}=\mathbf A^1_h$ unless $T=-27/256$, in which case omit only $h=9/8$ from the domain of the semistable ideal statement.
The omitted fiber is a cusp; it is not removed from the definition of the original surface.
On $C^{\rm ss}$ the smooth locus of $W$ has its generalized elliptic action. The generic non-torsion of $P$ makes

$$
D_n=(nP)^{-1}(O),\qquad i_n=(nP.O)_{h_*},\qquad z=h-h_*
$$

a finite effective Cartier divisor and its finite local intersection exponent, with $i_n=0$ when the sections do not meet.
Write $f_{\mathcal U}:\mathcal U\to C^{\rm ss}$ for the restricted energy morphism. The same [FIX] already proves

$$
\mathcal I_{\operatorname{Fix}(F_T^n)}
=f_{\mathcal U}^{*}\mathcal I_{D_n}\,\operatorname{Fitt}_1\Omega^1_{\mathcal U/C^{\rm ss}}.
\tag{B0}
$$

Formula (B0), including its node structure, is baseline. The contribution being evaluated is the exact input exponent, not another claim to have constructed the complete ideal.

## 3. V1: exact original forcing and low-order good contacts

For each prime $p>3$, define the actual coefficients by the unique polynomial decomposition

$$
f(Z)^{(p-1)/2}=Z^pM(Z)+AZ^{p-1}+L(Z),\qquad\deg L<p-1.
$$

The [old Manin interface][M] already gives $j\notin k(h)^p$, the specified nonzero value

$$
\lambda=-\frac q\delta\,dh,\qquad
\mu(P)=\frac T2M(s/12)+\left(\frac b{2q}\right)^p-A\frac b{2q},
$$

and the same nonzero polynomial

$$
N_p=q^p\mu(P)=\frac12\{Tq^pM(s/12)+b^p-Abq^{p-1}\}\in k[h],\qquad\deg N_p\le2p.
$$

These formulas, their nonvanishing at every allowed $T$, and the necessary prime-to-$p$ tangency support are old input.
In particular the positive-characteristic exclusion of prime-to-$p$ tangency at a good point $q=0$ was already proved in [M]; it is not counted again.

The new [forcing proof][G] gives, in characteristic zero on $q\delta\ne0$,

$$
\mathcal L\int_O^P\frac{dX}{2Y}=-\frac H{q\delta},\qquad
\mathcal L=\partial_h^2+\left(\frac{\delta'}\delta-\frac8q\right)\partial_h
+\frac{8h^3-18h^2+9h-12T}{q\delta}.
\tag{V1a}
$$

The entire moving-endpoint calculation is included, with cancellation of the combined primitive's pole at $O$.
A separate positive-characteristic coefficient proof gives, for all $p>3,T\ne0$,

$$
\mu(P)'=-\frac{AH}{q^2},\qquad N_p'=-q^{p-2}AH.
\tag{V1b}
$$

It is not justified by simply reducing an analytic integral equation modulo $p$.
The [good-contact proof][C] then proves the following exact statements.

- Over any algebraically closed field of characteristic zero, or of characteristic $p>3$ with $p\nmid n$, every actual finite good tangency $i_n>1$ satisfies $q_*\ne0$ and $i_n=2+\mathbf1_{H_*=0}$.
- Its original parameter has leading term $-nH_*z^2/(2q_*\delta_*)$ if $H_*\ne0$, and $-nz^3/(2q_*\delta_*)$ if $H_*=0$.
- In characteristic $p>3$, every good Hasse zero has $\operatorname{ord}_{h_*}A=1+\mathbf1_{q_*=0}$.
- At every root of $N_p$ in $q\delta\ne0$, $\operatorname{ord}_{h_*}N_p=1+\operatorname{ord}_{h_*}A+\mathbf1_{H_*=0}\le3$.

The ordinary and supersingular local Manin expansions have different lowest terms. The proof first bounds the actual intersection below $p$ and only then reads its coefficient; invisible $p$th-power terms cannot be discarded in advance.
The Hasse argument includes the original good point $q=0$ and proves its double-zero case, not just simplicity away from it.
These conclusions give exact conditional contact orders, not all contact locations or an existence theorem for third-order good tangencies.
Over general algebraically closed positive-characteristic constants, a root of $N_p$ has not been proved sufficient for actual prime-to-$p$ tangency.

## 4. V2: every prime-field good initialization and every iterate

Let $p>3$, $T\in\mathbf F_p^\times$, $h_*\in\mathbf F_p$, and $\delta(h_*)\ne0$.
Keep the point order $d=\operatorname{ord}P(h_*)$ in the actual closed-fiber group as a finite algebraic input. Define

$$
e_*=
\begin{cases}0,&A_\ast\ne0,\\1+\mathbf1_{q_*=0},&A_\ast=0,\end{cases}
\qquad
c_*=
\begin{cases}
1+\mathbf1_{q_*=0},&p\mid d,\\
1,&p\nmid d,\ N_p(h_*)\ne0,\\
2+\mathbf1_{H_*=0},&p\nmid d,\ N_p(h_*)=0.
\end{cases}
\tag{V2a}
$$

Then $e_*=\operatorname{ord}_{h_*}A$ and $c_*=i_d$.
The prime-to-$p$ branches use the [old prime-field equivalence][PF] and V1.
The [new $p$-primary proof][PP] supplies the complementary branch using an actual finite étale Igusa lift, compatible generator and model normalization, the horizontal logarithmic derivative on the Frobenius twist, and low-order integration.
It does not pull a relative differential along a section as though it were a base differential. The moving translation is treated correctly.
The case $p=5,d=10$ is retained by taking $2P$; no small-prime exception is suppressed.

For every $n\ge1$, the accepted [synthesis][SYN] yields

$$
i_n=
\begin{cases}
0,&d\nmid n,\\[2pt]
p^a c_*+e_*\dfrac{p^a-1}{p-1},&d\mid n,\quad a=v_p(n/d).
\end{cases}
\tag{V2b}
$$

It identifies the original Hasse coefficient with the $t^p$ coefficient of the formal $[p]$-series and uses $e_*\le2<p$ to exclude cancellation of its lowest term.
This is the standard low-Hasse-order propagation already given by Naskręcki Lemma8.2, not a new all-multiples theorem.
Closed supersingular fibers are allowed; generic ordinarity is not replaced by an assumption that every closed fiber is ordinary.

On the formal neighborhood of the entire original good fiber,

$$
\mathcal I_{\operatorname{Fix}(F_T^n)}=(z^{i_n}).
\tag{V2c}
$$

The exponent is now evaluated by (V2a)–(V2b); $i_n=0$ means the unit ideal and an empty fixed scheme there.
The group input $d$ is not an unknown intersection or an unevaluated division-polynomial order.
No uniform closed formula for $d$ over all primes is claimed, and this result is not extended to all finite extensions or all geometric good parameters.

## 5. V3: every finite node and the unique second-order exception

Let $k$ be any algebraically closed field of characteristic $p>3$, let $T\in k^\times$, and let $h_*$ be any finite nodal parameter.
The [nodal proof][NODE] extracts $w$ from the original unique singular point and gives

$$
T=w^3(w-1),\qquad h_*=w(3-2w),\qquad w\ne0,1,3/4.
$$

Take either root $\zeta$ of

$$
(w-1)\zeta^2+(2w-1)\zeta+(w-1)=0.
$$

The roots are reciprocal and represent the original marked point's multiplicative coordinate or its inverse; their order is the same.
For $n=p^a m$, $p\nmid m$, the exact intersection is

$$
i_n=
\begin{cases}
0,&\zeta^m\ne1,\\
2p^a,&\zeta^m=1,\ p>5,\ (T,h_*)=(3/16,-2),\\
p^a,&\zeta^m=1,\ (T,h_*)\ne(3/16,-2).
\end{cases}
\tag{V3a}
$$

If $\zeta$ has finite order $d$, the initial original-parameter terms are

$$
t_O(dP)=\frac{d(2w+1)}{w(4w-3)^3}z+O(z^2)
\quad\text{at a nonexceptional node},
$$

$$
t_O(dP)=-\frac{3d}{3125}z^2+O(z^3)
\quad\text{at }(T,h_*)=(3/16,-2),\ p>5.
\tag{V3b}
$$

The proof constructs the marked model from integer Tate series, keeps $T$ fixed by an explicit formal implicit function, and proves that its energy parameter is unramified over the original $z$.
The Tate point used in that construction is $-P$, so the original sign is accounted for in (V3b).
The first derivative vanishes only at the displayed exception, where the second coefficient is proved nonzero. The conclusion is not based on an unproved genericity assertion.
Multiplicative $p$-power propagation is standard and receives no separate novelty credit.

In characteristic five the displayed exceptional parameter is a cusp, not a node; the nodal quantifier has not omitted an allowed node.
For a general algebraically closed $k$, $\zeta$ need not be a root of unity, and then every $i_n$ is zero.
At the exceptional parameter in characteristic $p>5$, its algebraic constant lies in $\overline{\mathbf F}_p$, so a finite-order return actually realizes the double contact.
This is distinct from the unresolved existence of a third-order good contact.
The same nodal calculation in characteristic zero shows that every finite-order nodal return is transverse: its sole double-contact candidate would require $\zeta+\zeta^{-1}=-4/3$, impossible for a root of unity.

At the original node, choose completed coordinates $z=\xi\eta$. The old ideal (B0) and the new exponent give

$$
\widehat{\mathcal I}_{\operatorname{Fix}(F_T^n)}
=z^{i_n}(\xi,\eta)\subset k[[\xi,\eta]].
\tag{V3c}
$$

The other smooth points of that nodal fiber have ideal $(z^{i_n})$.
For $i_n=0$ the fixed scheme is just the reduced isolated node; for $i_n>0$ it is a fiber of thickness $i_n$ with a length-one embedded part at the node.
This precise distinction is already part of [FIX]; (V3c) is its evaluated consumer, not an independent fourth structural innovation.
The identity $H=w(2w+1)(4w-3)^2$ relates the nodal exception to the same forcing factor and explains cohesion. It is not a new general degeneration theorem.

## 6. Full proof responsibilities and accepted status

The [mathematical disposition][MATH] accepts G/C, PP, NODE, and the new SYN consumer through their actual non-author checks.
The earlier [Manin acceptance][MA] and [prime-field/fixed-scheme acceptance][OLD] supply M, PF, FIX and their named original-model interfaces.
Frozen author files retain their then-current “awaiting review” wording; later dispositions provide their current accepted status without rewriting those files.
This brief does not use one conditional consumer check as a second certification of all its upstream mathematics.

| Necessary output | Actual full proof responsibility |
|---|---|
| Original complete surface, energy, finite fibers and non-torsion | Accepted original charts/pole/no-base-point proof; full integer orthogonal-lattice and finite-fiber argument; actual return-map completion and Picard pullback/degree growth. The current proof map specifies the precise consumed source segments. |
| The specified finite-base action and complete fixed ideals | FIX: direct $+P$ identity, regular minimal-model extension, good torsor equalizer, generalized elliptic action, both inclusions in the completed nodal ideal, and descent/gluing. A tangent representation alone is insufficient. |
| The original nonzero Manin polynomial | M: marked short coordinates, non-$p$th-power $j$, source normalization, nonvanishing at ordinary and exceptional time, and the full good-local necessary implication. |
| Prime-field sufficiency | PF: actual residue and Frobenius calculations, Hasse/finite-group branches, and both directions of the stated equivalence, without an extension-field extrapolation. |
| V1 | G: both Gauss–Manin identities, the full moving-endpoint forcing, independent positive-characteristic coefficient identity, and Hasse auxiliary lemma; C: local Manin expansion, noncircular low-order bound, exact coefficients, characteristic-zero and $q=0$ boundaries. |
| V2 initialization | C plus PP's actual étale Igusa lifting, compatible marking, model weights, horizontal logarithmic derivative, low-order integration and Verschiebung comparison, including $p=5,d=10$. |
| V3 initialization | NODE: all denominators, marked Tate change, fixed-T implicit function, first and second coefficients, original-parameter invertibility, local identity-section comparison, and characteristic-five exclusion. |
| All-iterate and fixed-ideal consumers | SYN: original Cartier/formal-Hasse normalization, integral $[p]$ series, strict lowest-order comparison, all divisibility branches and full ideal substitution. |

The proof map is an index to existing proofs, not permission to omit topic-specific necessary proofs from a future body.
Using the $r=1$ instance of the old finite-fiber argument does not require its empty $0<\ell<r$ branch or the general normal-bundle-order calculation.
Nor does the direct autonomous FIX construction consume the general-r spectral Jacobian, Weil point selection, finite-set autonomous conjugacy or cycle-counting chain.
These exclusions follow actual proof consumption, not a target page estimate. The original full model, all four terminal lines, finite-fiber integrity and non-torsion remain required.
No new short replacement proof is silently substituted for an accepted necessary argument.

The old F5 certificate is not a proof dependency of the uniform theorems and is not an extra contribution to fill pages.
If a future manuscript elects to state an optional example, its exact scope and verification must be retained; it cannot replace any of the above proofs.
No new sampling, CAS run, formal proof assistant, or actual PDF acceptance is asserted by this brief.

## 7. Prior-art deductions and portfolio delta

The [Phase B report][B], [C/D][CD], [portfolio comparison][PORT], and [preflight][PRE] record bounded primary-source reading and remaining gaps.
They do not certify an exhaustive search or absence of prior art.

| Existing work or baseline | Deduction and residual object-specific work |
|---|---|
| Voloch1990 Theorem6.1, Broumas and Ulmer/UV descent | A generic cross-characteristic derivative relation and compatible descent mechanisms already exist. Voloch gives a nonzero function-field multiplier, not the exact original normalization at every closed parameter. The present evaluated factor and local orders are the residual finding. |
| UV Proposition4.7, Proposition4.11 and §4.12 | Exact complex-Betti read-off, all moving endpoints, and a third-order complex-Betti example are prior. At an actual tangent torsion leaf one cannot evade this overlap by renaming “maximal contact” as “designated contact”. |
| Naskręcki Lemma8.2 | The all-multiples formula is standard once $c_*,e_*$ are known; “every n” cannot create a separate novelty item. |
| Gasull–Mañosa–Xarles and CCRS | The candidate is the same marked Tate normal form $E(b,c)$ with $b=T,c=1-h,(0,0)=-P$. Fixed-order torsion conditions already have an algorithm. On the common charts fixed T moves both Lyness parameters, so a fixed-Lyness-parameter statement is not automatically the same slice. |
| Tate integer series, formal implicit functions and multiplication | These are tools, not a new deformation method. The evaluated fixed-T coefficients and unique exception remain the specific calculation to assess. |
| Old qPI Manin/support/fixed-scheme work | The actual model, marked point, $N_p$, prime-field support equivalence and the complete ideal shape are all deducted, as is the old positive-characteristic good $q=0$ exclusion. |
| Papers18 and29 | Both already retain genuine complete fixed schemes and nilpotents. Their read theorems do not supply the qPI section's evaluated base-direction intersections; “scheme rather than point set” is nevertheless not an original method here. |
| Paper30 and Paper11 | P30's vertical critical ideal is a different object, with Hasse root multiplicity formerly an input; its geometry remains baseline. P11 already supplies the ordinary finite-group cycle consumers, which are not added as a new application chapter. |

The [portfolio report][PORT] finds a cohesive local delta in the actual compared material; that is not a global novelty score or a natural-body-capacity approval.
The old characteristic-zero I03 proposed the intersection problem but did not solve these values. Its full exceptional-location/order spectrum remains unresolved; this brief neither claims to close it nor adds it as a new compulsory joint contract.
The main external risk is direct containment in unread Duistermaat or other fixed-Tate-slice work, or a judgment that the surviving calculations are routine despite their completeness.
Duistermaat's relevant full text and Scholar/Semantic Scholar access gaps remain exactly as reported. Failed access is not positive novelty evidence.
Source reports' reading identities are not inherited as a formal reviewer's own full reading; the common manifest specifies what that reviewer must actually inspect.

## 8. Nonclaims and unchanged admission contract

There is no claim of all geometric good parameters, every finite extension, all characteristic-zero exceptional locations, a third-order good-contact existence theorem, a closed point-order formula, cusp or infinity fixed ideals, $T=0$, or the entire nonautonomous relative torsor action.
The nodal statement is not narrowed to prime fields to match V2. Different constant-field quantifiers describe complementary parts of one original construction, not selected best results from different systems.
There is no Riemann determinant or Hilbert–Pólya operator claim; Route A/B scoring is not applicable.

Each of two fresh non-author reviewers must personally assess all four gates on the same complete scientific input, even if an earlier gate fails:
novelty at least 7.5/10, independent scientific value at least 7.5/10, complete proof confidence at least 9/10, and a credible natural-body-capacity PASS.
Capacity means anonymous English, single column, 11pt article, letter paper, one-inch margins, ordinary spacing, and **22–30 pages of complete substantive body**, with references separate.
Each reviewer must give low/central/high estimates by actual necessary proof modules, explaining both under-window and over-window risks. These are predictions, not measurements or rigorous bounds.
There is no added requirement that the central estimate itself lie within the window. Paper30's later 40-page exception does not apply.

Do not use source line counts, file counts, accumulated effort, padding, smaller typography, shortened claims, necessary proofs moved to appendices, split papers or trial layouts to satisfy capacity.
Each reviewer gives their own conjunction, and admission requires both complete conjunctions. Scores are not averaged, calibrated, rounded into a pass, or combined by selecting different reviewers' best gates.
The two reports remain mutually unseen until submission. Earlier mathematical/source contacts are disclosed; these formal seats are not the authors or earlier bounded reviewers of this candidate.
Submission freezes each vote. A factual clarification cannot silently become a new favorable vote.
The specified GPT-5.4 MCP is unavailable; use of an available Codex xhigh reviewer must be disclosed and is not cross-model or human certification.

The shared manifest and proof map must be frozen before dispatch. Two complete passing votes are required before project creation, source/publication locks, manuscript writing or PDF construction.
All work remains local. Papers27–30 retain their accepted artifacts; Paper31 and the final cross-paper audit remain unfinished.

[PRE]: PAPER31_QPI_EXACT_THICKNESS_PREFLIGHT_DISPOSITION_V1_20260912.md
[CD]: PAPER31_QPI_EXACT_THICKNESS_NOVELTY_PHASE_CD_V1_20260912.md
[B]: PAPER31_QPI_EXACT_THICKNESS_NOVELTY_PHASE_B_V1_20260912.md
[PORT]: PAPER31_QPI_EXACT_THICKNESS_PORTFOLIO_DELTA_V1_20260912.md
[MATH]: PAPER31_QPI_EXACT_LOCAL_THICKNESS_DISPOSITION_V1_20260912.md
[OLD]: PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md
[MA]: PAPER31_QPI_NEW_INPUT_MANIN_DISPOSITION_V1_20260912.md
[M]: PAPER31_QPI_NEW_INPUT_MANIN_INTERFACE_V1_20260912.md
[PF]: PAPER31_QPI_MANIN_PRIMEFIELD_EXACTNESS_V1_20260912.md
[FIX]: PAPER31_QPI_MANIN_FIXED_SCHEME_INTERFACE_PROBE_V1_20260912.md
[G]: PAPER31_QPI_PICARD_FUCHS_FORCING_PROBE_V1_20260912.md
[C]: PAPER31_QPI_GOOD_CONTACT_MULTIPLICITY_V1_20260912.md
[PP]: PAPER31_QPI_PRIMEFIELD_PPRIMARY_GOOD_PROBE_V1_20260912.md
[NODE]: PAPER31_QPI_MANIN_NODAL_SCALAR_PROBE_V1_20260912.md
[SYN]: PAPER31_QPI_EXACT_LOCAL_THICKNESS_SYNTHESIS_V1_20260912.md
