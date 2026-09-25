# Proper-divisor Euclidean return: full fixed packets and a nonprime primitive

Candidate ID: `ANG-20260925-DJP01`.
Outcome: OWNED EUCLIDEAN CLOCK; NONPRIME FIXED PRIMITIVE — STOP / FORK
Paper473; batch `SYMBOLIC-RETURN-20260925-Y`, round4/5; 2026-09-25.
Status: exact global fixed-point classification and decisive MAIN counterexample.
Classical NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

A two-dimensional quotient/remainder return rereads its shared-denominator digits and applies a current proper-divisor permission.
Each of four separate owners retains the closed unit square with its original area measure.
The complete inverse domains, every-point IMAGE and full-history clock are explicit.
Every admissible fixed digit pair gives exactly one actual fixed point, with its whole incoming packet and primitive time.
All these fixed multipliers are algebraic irrational numbers, and distinct fixed digit pairs have distinct primitive times.
After this global classification, the lexicographically first MAIN pair \((4,2)\) supplies an owned primitive not equal to the logarithm of any ordinary prime.
This stops the stated prime-only target without a digit cutoff, higher-period search, measure change or borrowed symbolic clock.

## 1. One object per owner and the lineage interface

| Item | Frozen definition / boundary |
| --- | --- |
| Carrier and measure | Each owner has its OWN full \(X=[0,1]^2\), usual Borel structure and original Lebesgue area |
| Current digits | For \(x>0\), \(a=\lfloor1/x\rfloor,\ b=\lfloor y/x\rfloor\) |
| Actual formula | \(F(x,y)=(y/x-b,\ 1/x-a)\) on that owner's permitted sources |
| MAIN M | \(1<b<a\) and \(b\mid a\) |
| P: permission-OFF | \(1<b<a\), with no divisibility test |
| C: complementary | \(1<b<a\) and \(b\nmid a\) |
| E: digit-range-OFF | Every \(x>0\), including its actual \(b=0,b=a\) digits |
| Terminals | Every \(x=0\) and illegal source stays an object with units and actual incoming, never an absorbing loop |
| Physical owner | Own inverse IMAGE, actual retained-lag groupoid and full height extension; no separate roof |
| Classical / operator fields | No symplectic suspension, Hamiltonian lift, operator, trace or zeta |

For integers \(N,d\) with \(1<d<N\) and real \(\rho,\eta\in[0,1)\), the source
\[
 (x,y)=\left(\frac1{N+\rho},\frac{d+\eta}{N+\rho}\right)
\]
lies in \(X\) and has actual digits \((a,b)=(N,d)\).
MAIN permission is therefore exactly the proper-divisor test at this interface.
The returned coordinates determine the next digits; no external integer register, prime list or fitted time schedule supplies them.
This is the divisor-symbol → shared-denominator quotient/remainder → actual return-permission arrow.
It is a declared deformation, not a proved Logistic/Hénon/symplectic lift or a prime-generation theorem.

## 2. Frozen question and evidence limit

The [93-line card](candidate-card.md) has SHA256
`3d20f511c63b244d324f87c20e7cf9bc4f68d541d3bca291ca65df64d6b6b7f0`.
The only location gate is the ENTIRE actual fixed set of M/P/C/E, followed by the lexicographically first actual MAIN fixed digit pair if one exists.
All other fixed packets and their unrestricted incoming remain part of the result.
No period-two or higher census, new parameter, density or formula is introduced.
The full-history formulas below specify all actual arrows and phases without claiming that higher-period locations have been enumerated.
The target tested is nonempty positive data with every primitive \(\log p\), at most one full packet per ordinary prime; all-prime coverage would be additional.
An actual MAIN nonprime primitive is sufficient for STOP/FORK.

## 3. Complete inverse domains and owned all-point IMAGE

At any legal source, \(a\ge1\), \(b\ge0\), and \(b\le a\), because \(0\le y\le1\).
Both outputs of \(F\) lie in \(U=[0,1)^2\), including zero coordinates.
For each integer pair \(a\ge1,b\ge0\), the candidate inverse at \((u,v)\in X\) is
\[
 \theta_{ab}(u,v)=\left(\frac1{a+v},\frac{b+u}{a+v}\right).
\]
Its actual floors equal \(a,b\) exactly when \(v<1,u<1\), respectively.
The source belongs to \(X\) exactly when additionally \(b+u\le a+v\); all other source inequalities are automatic.
Consequently no pair with \(b>a\) is possible, and the EXACT inverse domains are
\[
 Y_{ab}=
 \begin{cases}
 U,&0\le b<a,\\
 U\cap\{u\le v\},&b=a.
 \end{cases}
\]
Retain only that owner's allowed digit pairs.
M/P/C use \(b<a\), so each of their allowed branches has the entire domain \(U\).
E also retains the indicated triangular \(b=a\) domains, with their diagonal boundary.
These statements follow by direct substitution into both floor equations and \(F\theta_{ab}=(u,v)\), and conversely every source reconstructs by its unique actual digits.
Different actual digit pairs cannot duplicate one predecessor, because its floors are unique.
The domains and images are Borel: these explicit rational inverses are homeomorphisms on surrounding open sets and are restricted to the displayed Borel sets.

There is no incoming into a target with \(u=1\) or \(v=1\), but such objects are not removed and may still have outgoing E-steps.
A target with \(u=0\) may have incoming even though its own first coordinate makes it terminal.
For E, \(y=0,y=1,x=1\) remain subject to exactly the source and triangular checks above.
No next-step permission is imposed at a target.

For the fixed smooth-cell germ,
\[
 DF(x,y)=
 \begin{pmatrix}-y/x^2&1/x\\-1/x^2&0\end{pmatrix},
 \qquad \det DF=x^{-3}>0 .
\]
Thus every permitted source is regular, including its assigned null faces.
The actual inverse derivative gives, at EVERY point of \(Y_{ab}\),
\[
 J_{ab}(u,v)=|\det D\theta_{ab}(u,v)|=(a+v)^{-3}>0 .
\]
It is finite, and its analytic formula agrees on every overlap through the same assigned source.
Change of variables on the surrounding diffeomorphism, restricted to any Borel \(B\subset Y_{ab}\), proves
\[
 \mu(\theta_{ab}B)=\int_B (a+v)^{-3}\,d\mu(u,v).
\]
Here source and target both use the original area restricted to \(X\); no invariant-density hypothesis is used.
This proves the four owners' own every-Borel IMAGE, including all cuts and boundary points.
Only then their legal-step clock is
\[
 \kappa(x,y)=-\log J_{\rm actual}(F(x,y))=-3\log x .
\]
It is nonnegative, with zero possible only at \(x=1\) in E.
No outgoing clock is assigned at a terminal; the exponent3 comes from the actual two-dimensional inverse, not an imposed symbolic normalization.

## 4. Every history, actual history-pair IMAGE and full kernels

All definitions here apply separately to each owner's actual branch domains.
For a legal \(n\)-step history \(z_j=F^jz=(x_j,y_j)\), put
\[
 V_0=1,\qquad V_n(z)=\prod_{j=0}^{n-1}x_j^{-3},\qquad S_n(z)=\log V_n(z).
\]
A legal inverse word \(\Theta\) of length \(n\) has all-point IMAGE \(J_\Theta(w)=V_n(\Theta w)^{-1}\).
The one-step IMAGE implies weighted substitution by indicators, simple functions and monotone limits; successive substitution proves this product identity on EVERY Borel part of the actual word domain.
At each stage retain all branches whose reconstructed source is legal, even if the final target is terminal.

For any target \(p\), define \(\mathcal B_0(p)=\{p\}\) and
\[
 \mathcal B_{n+1}(p)=\bigcup_{w\in\mathcal B_n(p)}
             \{\theta_{ab}(w):w\in Y_{ab},\ (a,b)\text{ allowed}\}.
\]
Induction proves that this is exactly the full set of actual depth-\((n+1)\) predecessors.
All compatible infinite inverse sequences remain; no branch or depth cutoff is present.
Coincident states are identified rather than counted as additional word-labelled sources.

Use every actual triple
\[
 \mathcal G=\{(z,m-n,w):F^mz=F^nw\text{ legally},\ m,n\ge0\},
 \qquad c=S_m(z)-S_n(w).
\]
Source is \(w\), range is \(z\), and equal triples, not integer lags, are identified.
Changing a witness for one triple shifts both depths equally and adds the same common-tail sum, proving descent.
Composition aligns the two middle depths by legal extension; the middle sums cancel, proving additivity.
The forward arrow \((Fz,-1,z)\) has clock \(-\kappa(z)\).

For inverse words \(\Theta_a,\Theta_b\) of lengths \(m,n\) over a common actual target domain, the history-pair map
\(\chi=\Theta_a\circ\Theta_b^{-1}\) sends \(w=\Theta_b y\) to \(z=\Theta_a y\).
Weighted substitution on an arbitrary Borel part of its actual domain proves
\[
 J_\chi(w)=\frac{J_{\Theta_a}(y)}{J_{\Theta_b}(y)}
          =\frac{V_n(w)}{V_m(z)}=e^{-c(z,m-n,w)} .
\]
These are fixed pointwise versions; descent gives agreement for duplicate actual witnesses.
Every arrow is covered, including length0 identities at terminals.

The complete kernels are the actual meeting triples satisfying
\[
 K_{\rm lag}:m=n,\qquad K_c:V_m(z)=V_n(w),\qquad
 K_{\rm joint}:m=n,\ V_m(z)=V_m(w).
\]
They are not presumed to be units.
For example in MAIN, \(\theta_{6,2}(u,v)\) and \(\theta_{6,3}(u,v)\), for any \((u,v)\in U\), are distinct one-step predecessors with the same first coordinate and clock.
Their equal-depth meeting gives a nonunit joint-kernel arrow, retained by the full ledger.

Every source packet is exactly an actual common-tail equivalence class.
Finite-forward packets are equivalently fibres of the actual terminal endpoint; if \(d_z\) steps reach terminal \(t\), their arrows are \((z,d_z-d_w,w)\) with clock \(S_{d_z}(z)-S_{d_w}(w)\).
Infinite non-eventually-periodic packets use the same unrestricted legal-meeting test.
Neither description pads a terminal or deletes incoming histories.

## 5. Entire isotropy-clock images and all real phases

A nonzero-lag source loop is equivalent to eventual periodicity.
For any actual least-\(q\) core with cycle sum \(C\), every incoming source has source isotropy \(q\mathbb Z\) and loop character \(nq\mapsto nC\).
Existence is witnessed after arrival at the core; the converse follows from its least source period.
Thus the ENTIRE clock image is \(\mathcal H_z=C\mathbb Z\).
For all four owners, every actual cycle lies in the image \(U\) and has legal \(x>0\), so each cycle phase has \(0<x<1\) and contributes a strictly positive clock.
Consequently \(C>0\) whenever a cycle exists; no zero-clock source cycle has been discarded.
Source isotropy is zero at terminal and non-eventual sources, and height-extension isotropy is trivial everywhere.
These structural statements do not search for any higher-period location.

The full extension acts by \((w,h)\mapsto(z,h+c(g))\).
For a reference \(p\) in one source packet and any actual \(g_z:p\to z\), put \(a_z=c(g_z)\).
All phases are exactly \([h-a_z]\in\mathbb R/\mathcal H_p\): changing \(g_z\) changes \(a_z\) by a loop clock, and equality modulo that group supplies the required adjusted arrow.
Changing reference translates the coordinate; no global selector or nice quotient is presumed.
Height translation has stabilizer precisely the ENTIRE \(\mathcal H_p\).
If a core is present its primitive is \(C\), with all returns \(nC\); when \(\mathcal H_p=0\), every real phase remains and there is no positive return.

## 6. Global classification of ALL fixed digit pairs

The entire digit sets relevant to fixed points are
\[
 \mathcal D_E=\{(a,b):a\ge1,\ 0\le b\le a\},\qquad
 \mathcal D_P=\{(a,b):1<b<a\},
\]
\[
 \mathcal D_M=\{(a,b)\in\mathcal D_P:b\mid a\},\qquad
 \mathcal D_C=\{(a,b)\in\mathcal D_P:b\nmid a\},
\]
with integer digits in every case.
A fixed point must be legal and in the image \(U\); its first coordinate is positive.
The first fixed equation gives \(y=x^2+bx>0\), and the second gives
\[
 p_{ab}(x)=x^3+bx^2+ax-1=0 .
\]
For every \((a,b)\in\mathcal D_E\), this polynomial is strictly increasing on \(x\ge0\), since \(p'_{ab}(x)=3x^2+2bx+a>0\).
Moreover,
\[
 p_{ab}(1/a)=a^{-3}+ba^{-2}>0,\qquad
 p_{ab}(1/(a+1))
 =\frac{1+b(a+1)-(a+1)^2}{(a+1)^3}
 \le\frac{-a}{(a+1)^3}<0 .
\]
There is exactly one positive root \(\rho_{ab}\), and
\[
 \frac1{a+1}<\rho_{ab}<\frac1a,\qquad
 p_{ab}^{\,*}=(\rho_{ab},\rho_{ab}^2+b\rho_{ab}).
\]
The cubic identity also gives \(y=1/\rho_{ab}-a\in(0,1)\).
Since \(y/\rho_{ab}=b+\rho_{ab}\in(b,b+1)\), both actual floors are exactly the proposed digits.
Thus \(p_{ab}^{\,*}\) is admitted by precisely the owners whose digit sets contain \((a,b)\), and is their actual fixed point.
Conversely the fixed equations and actual floors force this unique root, proving global completeness.
No fixed point lies on an axis, \(x=1\), \(y=1\), or an integer inverse cut; terminal units are not fixed action steps.
This handles E's \(b=0,b=a\) as well as all unbounded proper-divisor and complementary digits.
M contains \((2m,2)\) for every \(m\ge2\), and C contains \((2m+1,2)\) for every \(m\ge1\); P and E contain these families.
Thus every displayed digit set is infinite and nonempty; no finite census is being substituted for this classification.

## 7. Full fixed incoming, kernels, multiplicity and primitive times

Fix an allowed pair \(d_0=(a,b)\), its point \(p=p_{ab}^{\,*}\), and
\[
 C_{ab}=-3\log\rho_{ab}>0 .
\]
Its complete incoming set is \(\mathcal B(p)=\bigcup_{n\ge0}\mathcal B_n(p)\) from §4.
For M/P/C, each allowed inverse maps \(U\) into the open square and into its own legal cell.
Therefore ALL finite words in that owner's entire digit alphabet can be applied to \(p\), and every compatible infinite inverse word remains.
For E, the exact \(Y_{ab}\) test is applied at every stage, in particular the triangular condition when \(b=a\); no full-shift claim is substituted for this condition.
In all cases the recursion proves every-depth coverage and includes every possible all-cell predecessor.

There is a unique canonical finite word for any noncore incoming state: its actual digit itinerary up to first arrival at \(p\).
Its last letter is not \(d_0\), since \(\theta_{d_0}(p)=p\) is the unique predecessor of \(p\) with that digit.
Conversely an admissible inverse word not ending in \(d_0\) cannot have arrived at \(p\) earlier, since all digits after that arrival would be \(d_0\).
Equal-length words giving the same source agree by deterministic forward digits; different-length repetitions merely append the constant core tail.
Thus state multiplicity is not word-label multiplicity, while all actual integer lag loops are retained.
Different fixed cores have disjoint full incoming packets: a meeting of two eventual fixed histories would force the two cores to coincide.

For \(z\in\mathcal B(p)\), choose its first arrival depth \(d_z\) and put
\[
 \beta_z=S_{d_z}(z)-d_z C_{ab}.
\]
Any later arrival gives the same \(\beta_z\).
The COMPLETE restricted groupoid and clock are
\[
 \mathcal G|_{\mathcal B(p)}
 =\{(z,k,w):z,w\in\mathcal B(p),\ k\in\mathbb Z\},\qquad
 c(z,k,w)=kC_{ab}+\beta_z-\beta_w .
\]
Indeed sufficiently large arrival depths with any prescribed difference witness every \(k\); every other meeting can be extended to the fixed core and gives the same formula.
Hence the lag kernel is all \((z,0,w)\); the clock kernel imposes \(kC_{ab}+\beta_z-\beta_w=0\); the joint kernel imposes \(k=0,\beta_z=\beta_w\).
At every incoming source, source isotropy is \(\mathbb Z\), extension isotropy0 and ENTIRE \(\mathcal H_z=C_{ab}\mathbb Z\).
Every phase is \([h-\beta_z]\in\mathbb R/C_{ab}\mathbb Z\).
The least positive return is \(C_{ab}\), and all repeats are \(nC_{ab}\).
In particular its factor3 cannot be divided away: the source core is already least period1, and no actual loop supplies \(C_{ab}/3\).

Let \(\xi_{ab}=1/\rho_{ab}>1\), distinct from the inverse-map notation \(\theta_{ab}\), so
\[
 Q_{ab}(\xi_{ab})=0,\qquad Q_{ab}(t)=t^3-at^2-bt-1,\qquad
 \exp(C_{ab})=\xi_{ab}^3 .
\]
The monic integer cubic has no rational root: any such root is \(1\) or \(-1\), while \(Q_{ab}(1)=-a-b<0\) and \(Q_{ab}(-1)=b-a-2<0\).
A reducible rational cubic would have a rational linear factor, so \(Q_{ab}\) is irreducible and is the degree3 minimal polynomial of \(\xi_{ab}\).
If \(\xi_{ab}^3\) were rational \(r\), the monic degree3 polynomial \(t^3-r\) would be the same minimal polynomial, contradicting \(a\ge1\).
Thus EVERY fixed multiplier is irrational, not an ordinary prime.

The fixed primitive times are also pairwise distinct.
If two roots \(\rho\) agreed, subtracting their cubics gives \((b-b')\rho+(a-a')=0\).
A difference in \(b\) would make \(\rho\) rational, contradicting the degree3 result; otherwise \(a=a'\) too.
Since \(-3\log\rho\) is injective, distinct fixed digit pairs give distinct times.
Each owner therefore has one full fixed packet per allowed pair, with no duplicate fixed primitive; this is not a uniqueness theorem for higher-period packets.

## 8. Precommitted MAIN witness, controls and decision

The global classification precedes selection of the witness.
No pair exists for \(a<3\); at \(a=3\) the only proper digit \(b=2\) does not divide \(a\).
At \(a=4\), \(b=2\) is allowed and is lexicographically first.
Its actual point has \(\rho\) the unique root in \((1/5,1/4)\) of
\[
 \rho^3+2\rho^2+4\rho-1=0,
 \qquad p=(\rho,\rho^2+2\rho).
\]
The complete incoming packet has primitive \(C=3\log\xi\), where \(\xi=1/\rho\in(4,5)\) and \(\xi^3-4\xi^2-2\xi-1=0\).
Its multiplier \(\exp C=\xi^3\) is irrational by §7, so \(C\) cannot equal the logarithm of ANY ordinary prime.
This is an actual MAIN primitive, not a control time or a selected repeat.

P, C and E separately own the same inverse/clock derivation on their own full domains and the complete fixed classifications above.
Their fixed multipliers are likewise irrational; control observations are not pooled into MAIN multiplicity or used to supply MAIN evidence.
E's extra digits and boundary branches remain explicitly in its history tests.
Removing or complementing permission does not turn this fixed return mechanism into a prime multiplier source.
The decisive failure is already MAIN's intrinsic primitive; naturalness and PROVES_TOO_MUCH need not be resolved to record it.

| Gate | Result for this frozen owner | Boundary |
| --- | --- | --- |
| T0 | Complete actual inverse domains, all-point every-Borel IMAGE and history-pair IMAGE established | Broadened measured carrier, not a symplectic suspension |
| T1 clock COMPONENT | Own \(-3\log x\) clock established | Arithmetic T1 NOT PASSED |
| T2 fixed gate | All four global fixed sets, full incoming, entire clock images, kernels, phases and repeats established | MAIN nonprime primitive violates the necessary target |
| T3 | NOT AUDITED | No operator, trace or zeta |
| Classical / formal / B | NOT APPLICABLE / UNASSIGNED / NOT INVOKED | No formal evaluator invoked |

Decision: STOP / FORK.
Same-object ownership remains intact; the existing counterexample is not repaired by any unsearched higher period.
No extra period window, selected subsystem, new measure, formula retuning or paper475 follows from this result.

## Reproducibility and AI/access disclosure

Data/proof availability: exact records are the [card](candidate-card.md), this paper, [claim ledger](claim-ledger.md) and [overview](README.md), following the [paper template](../paper-template.md).
Author read all93 card lines through EOF with `sed -n '1,110p'`; `wc -l` and `sha256sum` bind the frozen bytes in §2.
The template107, ARS skill488, academic-paper workflow544, runtime policy113 and local AGENTS/plan were personally read and retained.
Methods are exact inverse substitution, change of variables, polynomial monotonicity/irreducibility and unrestricted inverse induction; there is no numerical cutoff or approximation.
Mechanical checks are full author-file self-read, ID/Outcome agreement, local links, table columns and unchanged frozen-card hash.
No scientific code/numerics, network, old edits, Git mutation, PDF, target-zero data, operator or external publication was used.

AI author `/root/batch_clock_scope_review` supplied derivation, drafting and internal checking; root owns card/integration.
No proof-stage helper, current CP1 text, raw, reviewer, peer proof or old paper/proof was used.
Design-only reads were455card1–66/105, prefixSHA `14266b22d349baf0e1a7b07b4868364a12f276962107a3f06b4323f8a405994e`;
014card1–11 EOF, SHA `e9109900a510099f67a73c4e68638f325be025abb49aa35d1e812004bd273519`;
358card1–80/136, prefixSHA `13f9a57c2fb21f977c056fbc394837edd48930a9f0f9ea66499be3de138702b9`.
The abandoned profinite proposal exposed014's no-return conclusion; no Outcome appendix or old proof was read for the accepted design.
Shared history and scout/root fixed-elimination/cubic feasibility thoughts influenced design, not blind or sealed preregistration; no old clock or theorem transfers.
The comparison with455 is definitional, not a novelty or nonconjugacy certificate.
Same-model/shared-history AI assistance is `NOT_CALIBRATED`, not independent-error, cross-model, blind, human or external validation.
No human or external mathematical verification is certified. Human contributions, funding and competing interests are unspecified; no human-participant or sensitive personal data are involved.
ARS supplied bounded scope, drafting and integrity/disclosure discipline, not a publication pipeline; `criteria_binding_unavailable`, with no venue-readiness claim.
