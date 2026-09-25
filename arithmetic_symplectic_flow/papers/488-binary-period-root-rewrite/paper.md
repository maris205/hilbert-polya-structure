# Binary periodic-root rewriting has owned nonprime fixed packets

Candidate ID: ANG-20260925-BPR01
Outcome: OWNED MARKOV CLOCK; NONPRIME FIXED PACKETS — STOP / FORK

Paper: 488-binary-period-root-rewrite. Batch PRE-P0-STRUCTURE-20260925-AB, round 4/5.
Date: 2026-09-25. Type: measured Borel arithmetic-history groupoid (ANG).
Scope: the frozen seven-cylinder fixed gate, with unrestricted inverse histories.
Formal Route coordinates: UNASSIGNED. Route B: NOT INVOKED.

## Abstract

The full one-sided binary source is parsed into a unary length header, a finite word and an unrestricted tail. MAIN replaces the finite word by its shortest periodic root and parses the result afresh. We construct the original two-state Markov probability, prove the prescribed inverse IMAGE density on every Borel restriction, and retain every actual integer-lag history, terminal incoming branch and physical phase. The seven frozen source cylinders contain exactly three MAIN fixed words. Their entire clock images have positive generators \(\log(3/2)\), \(\log 9\) and \(\log(81/4)\), none an ordinary-prime logarithm. Each whole fixed-core basin supplies one physical packet, not a collection of selected tails. Three independently owned controls are solved on the same seven full cylinders. The common \(0^\infty\) packet already disproves prime-only purity, while the other fixed words distinguish root compression from its removal. No higher-period classification, canonical arithmetic measure, geometric lift or operator is claimed.

## 1. Frozen object, lineage and question

Let \(X=\{0,1\}^{\mathbb N_0}\) have its Cantor topology and Borel structure; write \([v]\) for a finite-word cylinder and \([\epsilon]=X\). The point \(\mathbf1=1^\infty\) is terminal, with no added forward loop. Every \(x\ne\mathbf1\) has a unique decomposition
\[
x=A_{n,w}\eta,\qquad A_{n,w}=1^n0w,\quad n\in\mathbb N_0,\quad |w|=n,\quad\eta\in X.
\tag{1}
\]
The first zero determines \(n\); the next \(n\) bits determine \(w\). Thus there is no overflow, missing finite word or unspecified tail.

For \(w\ne\epsilon\), let \(r(w)\) be the shortest prefix \(v\ne\epsilon\) with \(w=v^{|w|/|v|}\); the exponent must be an integer. Set \(r(\epsilon)=\epsilon\). Define four distinct owners on the same full source and common domain \(D=X\setminus\{\mathbf1\}\):
\[
T_U(A_{n,w}\eta)=B^U_{n,w}\eta,\qquad
\begin{array}{c|cccc}
U&M&F&C&O\\ \hline
B^U_{n,w}&r(w)&w&\epsilon&r(\operatorname{sort}(w))
\end{array}
\tag{2}
\]
Here \(M\) is MAIN, \(F\) is root-OFF, \(C\) is payload-OFF, and \(O\) is order-OFF; \(\operatorname{sort}(w)=0^{\#0(w)}1^{\#1(w)}\). All unsorted input words remain in \(O\). Each owner has \(T_U(0\eta)=\eta\), including when the output is terminal.

The lineage is current integer length and proper-divisor admissibility \(\to\) tests \(w=v^{n/d}\), \(d\mid n\) \(\to\) actual output compression \(\to\) changed next parsing. A primitive finite word is not an ordinary prime: \(0001\) has composite length and no shorter repeating root, while a constant word of any prime length has a one-letter root. Neither fact deletes those sources. This is a symbolic admissibility deformation, not an arithmetic prime generator or a Logistic/Hénon geometric realization.

| Owner field | This frozen object |
| --- | --- |
| Carrier and original measure | Full \(X\), Markov probability of §2 |
| Evolution and actual inverses | (2) and every chart of (3) |
| Clock and histories | Prescribed IMAGE version; actual lag groupoid of §3 |
| Packets and repetitions | Entire stabilizer of height translation, not word-root length |
| Classical symplectic map, roof, suspension | NOT APPLICABLE |
| Trace, determinant, Hilbert-space operator | NOT CONSTRUCTED; T3 NOT AUDITED |

The question is whether the complete positive primitive ledger has exactly one packet of length \(\log p\) for every ordinary prime \(p\), and no extra packets. A single positive nonprime packet refutes this conjunction. The fixed-word window is not a cutoff on the source, inverses or history.

## 2. Probability, every inverse and the all-point IMAGE proof

Put \(\pi_0=\pi_1=1/2\), \(P_{00}=P_{11}=2/3\), \(P_{01}=P_{10}=1/3\). These are frozen design inputs, not a canonical arithmetic density or an inserted meaning for prime \(3\). Set
\[
\mu([s_0\cdots s_{\ell-1}])=\pi_{s_0}\prod_{i=0}^{\ell-2}P_{s_i,s_{i+1}}
\quad(\ell\ge1),\qquad\mu(X)=1.
\]
The row sums give consistent cylinder probabilities. They extend to a Borel probability: on the finite-cylinder algebra consistency gives finite additivity; compactness reduces any cylinder-algebra cover of a compact member to a finite cover, giving the premeasure continuity needed for extension. Cylinders generate the Borel structure, so the extension is unique. Every nonempty cylinder has positive mass, and a length-\(\ell\) cylinder has mass at most \((1/2)(2/3)^{\ell-1}\); hence every singleton is null. All such points remain in \(X\).

For each owner and every \(n,w\), the complete inverse chart is
\[
\theta^U_{n,w}:[B^U_{n,w}]\longrightarrow[A_{n,w}],
\qquad B^U_{n,w}\eta\longmapsto A_{n,w}\eta.
\tag{3}
\]
This is a homeomorphism between the displayed cylinders, and (2) verifies its forward inverse. The source cylinders \([A_{n,w}]\) partition \(D\), so every preimage has exactly one such source label. Target cylinders may overlap; all their branches are retained. There is no target-outgoing guard. In particular \(\theta_{0,\epsilon}(y)=0y\) is available for every \(y\in X\), so \(T_U:D\to X\) is onto for all four owners. Each \(T_U\) is a local homeomorphism on its open domain, not a total homeomorphism of \(X\).

For a finite word \(s\) and bit \(t\), define
\[
K(\epsilon,t)=1,\qquad
K(s,t)=
\frac{\pi_{s_0}\bigl(\prod_{i=0}^{|s|-2}P_{s_i,s_{i+1}}\bigr)P_{s_{|s|-1},t}}{\pi_t}
\quad(s\ne\epsilon).
\]
For every Borel \(E\subseteq X\),
\[
\mu(sE)=\int_E K(s,\eta_0)\,d\mu(\eta).
\tag{4}
\]
Indeed (4) follows by cancellation of finite products when \(E\) is a cylinder; equality of the resulting finite measures then extends it to the generated Borel sigma-algebra. This proof also covers \(s=\epsilon\).

Fix a chart (3), abbreviate its prefixes by \(A,B\), and take any Borel \(E\subseteq[B]\). Write \(E=\{B\eta:\eta\in E'\}\) and partition \(E'\) by \(\eta_0=t\). On each piece (4) gives masses \(K(B,t)\mu(E'_t)\) and \(K(A,t)\mu(E'_t)\). Consequently
\[
\mu(\theta E)=\int_E J_\theta(y)\,d\mu(y),\qquad
J_\theta(B\eta)=\frac{K(A,\eta_0)}{K(B,\eta_0)}\in(0,\infty).
\tag{5}
\]
No division by \(\mu(E'_t)\) is used: (5) holds for arbitrary Borel restrictions, including null ones. Its finite-cylinder formula is the prescribed version at EVERY tail, terminal target included. It is not asserted to be the only measurable a.e.-equivalent version. The actual branch at \(x=A\eta\) defines
\[
\kappa_U(x)=-\log J_{\theta^U_{n,w}}(T_Ux).
\tag{6}
\]
No positive step-clock or invariant measure is assumed. On the forward branch at \(x\), IMAGE has density \(J_\theta(T_Ux)^{-1}\), not \(J_\theta(T_Ux)\).

## 3. All legal histories, clock kernels and physical packets

Fix any one owner \(U\), without identifying it with another. An iterate is legal only while each required forward step is defined. Zero steps are always allowed. Write
\[
S_0(z)=0,\quad S_r(z)=\sum_{j=0}^{r-1}\kappa_U(T_U^jz),\qquad
G_U=\{(z,r-s,y):T_U^rz=T_U^sy,\ r,s\ge0\text{ legal}\}.
\tag{7}
\]
The source is \(y\), the range is \(z\); equal triples, and only equal triples, are identified. Finite inverse paths furnish actual charts, not a free-label groupoid with extra isotropy. Legal domains and iterates are Borel; (7) is a countable union of Borel equality relations in \(X\times\mathbb Z\times X\). Every source and range fibre is countable by the countable inverse atlas. Composition is addition of lags and inversion reverses endpoints and lag.

These operations remain legal with terminals. To compose two represented arrows, extend the shorter of their two middle-orbit segments to the longer one. That extension exists because the longer segment is already legal; propagate it through the common meeting point. This proves closure without continuing a terminal. The same extension argument shows that
\[
c_U(z,r-s,y)=S_r(z)-S_s(y)
\tag{8}
\]
is independent of the representation: two pairs with the same lag differ by a common integer increment, and the added sums along their common forward image cancel. It also proves additivity under composition.

On an injective branch of \(T_U^r\), let \(\theta_\alpha\) be its inverse and \(u=T_U^rz\). Repeated application of (5), refining by finitely many bits when necessary, gives the all-point inverse density
\[
J_\alpha(u)=\prod_{j=0}^{r-1}J_{\mathrm{actual},j}(T_U^{j+1}z)=e^{-S_r(z)}.
\]
For a history-pair chart \(y\mapsto z=\theta_\alpha(T_U^sy)\), first follow the \(s\) forward steps and then the \(r\) inverse steps. Its actual IMAGE density is \(J_\alpha(u)/J_\beta(u)=e^{-c_U(z,r-s,y)}\). The every-Borel identity follows by composition of (5), not by taking a limit of densities. Thus the lag kernel is the arrows with \(r=s\), the clock kernel is the arrows with \(S_r(z)=S_s(y)\), and the joint kernel is their intersection. These conditions include all charts and all null points.

Use all of \(X\times\mathbb R\), with an arrow \(y\to z\) lifting
\[
(y,h)\longmapsto(z,h+c_U(z,r-s,y)).
\tag{9}
\]
Let height translation act on its orbit SET; no Hausdorff quotient, positive roof, smooth flow or conservative measure is inferred. Define
\[
I_z=\{k:(z,k,z)\in G_U\},\qquad H_z=\{c_U(z,k,z):k\in I_z\}.
\]
If the forward orbit has no repeated state, including an orbit that terminates, then \(I_z=\{0\}\). Otherwise its eventual cycle has an actual least step period \(q\ge1\), and \(I_z=q\mathbb Z\). To see this, any unequal meeting times force a cycle; on its least cycle every subsequent equality has time difference divisible by \(q\), and sufficiently late meetings realize every multiple. For \(\ell\) the sum of (6) once around that cycle,
\[
c_U(z,kq,z)=k\ell,\qquad H_z=\ell\mathbb Z,\qquad
I_{(z,h)}^{\mathrm{extension}}=\{kq:k\ell=0\}.
\tag{10}
\]
Cyclic shifts of the core give the same \(\ell\), since it is the sum of the same terms. If there is no cycle, \(H_z=\{0\}\) and extension isotropy is trivial; if \(\ell=0\), source isotropy is retained but there is no positive physical primitive.

The stabilizer of the height action at \([(z,h)]\) is exactly \(H_z\): an equality after height translation must be witnessed by an arrow with both base endpoints \(z\), and every such arrow supplies the corresponding equality. Thus a nonzero \(\ell\) gives one positive primitive \(|\ell|\) and repetitions \(j|\ell|\), \(j\ge1\). Source step period, ordinary bit period and finite-word-root length are different notions. One actual base orbit gives one physical time orbit; its real phases are not additional packets. Distinct base orbits are not identified by equal periods, bit shifts or ordinary tail equivalence.

### 3.1 Complete incoming prescription and terminal basin

For any target \(v\in X\), every immediate predecessor is obtained by enumerating ALL \(n\ge0,w\in\{0,1\}^n\), checking whether \(v\) starts with \(B^U_{n,w}\), and then returning
\[
A_{n,w}\,\sigma^{|B^U_{n,w}|}v,
\tag{11}
\]
where \(\sigma\) deletes bits. Empty \(B\) always matches. Unique parsing proves (11) is exhaustive and source-checked. Iterating this rule at every node enumerates all finite incoming paths; compatible infinite choices give all infinite incoming histories. There is no \(n\le2\) restriction here. For a fixed range \(z\), all incoming groupoid arrows are obtained by taking any legal \(r\), applying (11) backwards \(s\) times to \(T_U^rz\) to obtain \(y\), and forming \((z,r-s,y)\).

For the terminal basin, let \(N_z\) be the number of steps to \(\mathbf1\). Any two meeting histories extend to their terminal, forcing lag \(N_z-N_y\) and clock \(S_{N_z}(z)-S_{N_y}(y)\). It follows that the terminal core itself has only its identity isotropy, and the entire basin has \(H=\{0\}\), though it has all its incoming paths. Its height time orbit is a line, not a closed packet. In particular the kernel of the height-translation action on the entire orbit set is \(\bigcap_zH_z=\{0\}\). No terminal or incoming null point was removed to reach this conclusion.

### 3.2 Full basin of a fixed core

Let \(p=T_Up\), \(L=\kappa_U(p)>0\), and
\[
\mathcal B_p=\bigcup_{N\ge0}T_U^{-N}\{p\},\qquad
\beta(z)=S_N(z)-NL\quad(T_U^Nz=p).
\]
The definition of \(\beta\) is independent of the chosen legal hitting time because each extra step at \(p\) adds \(L\). All integers occur as lags between any \(z,y\in\mathcal B_p\): extend their hitting times independently while they remain at the fixed core. Conversely any arrow meeting this basin ends in it. Therefore
\[
G_U|_{\mathcal B_p}=\mathcal B_p\times\mathbb Z\times\mathcal B_p,\qquad
c_U(z,k,y)=\beta(z)-\beta(y)+kL.
\tag{12}
\]
In particular the entire clock image at EVERY point of the basin is exactly \(L\mathbb Z\), not merely a subgroup containing one displayed loop. The phase coordinate is
\[
h-\beta(z)\pmod{L\mathbb Z}.
\tag{13}
\]
This identifies its quotient time orbit with one circle \(\mathbb R/L\mathbb Z\); translation is transitive on that circle. The lag, clock and joint kernels in this basin are respectively \(k=0\), \(\beta(z)-\beta(y)+kL=0\), and their intersection; extension isotropy is trivial. Two distinct fixed cores cannot belong to one base orbit, because their every forward iterate remains their distinct core. Their basins and packets are therefore distinct even if their \(L\)'s coincide.

## 4. Exhaustive fixed words in the seven full cylinders

The following elementary word equation solves the whole tail, not a selected subset. Let \(A,B\) be finite words with \(|A|>|B|\). Then
\[
A\eta=B\eta
\quad\Longleftrightarrow\quad
A=BD\text{ for a nonempty }D,\ \eta=D^\infty.
\tag{14}
\]
Indeed equality first forces \(B\) to be the corresponding prefix of \(A\); cancellation gives \(D\eta=\eta\), which fixes each successive block of the entire tail to \(D\). Conversely that tail satisfies the equation. Every owner has \(|A|=2n+1>|B|\), so (14) applies to every frozen cell.

At such a fixed word, \(\eta_0=D_0\). If \(B\ne\epsilon\), cancellation of the common \(B\) factors and of the edge from its last bit to \(D_0\) in (5) yields the closed-word weight
\[
J_{\mathrm{fixed}}=
\prod_{i=0}^{|D|-1}P_{D_i,D_{(i+1)\bmod |D|}}
=\frac{2^{e(D)}}{3^{|D|}},
\tag{15}
\]
where \(e(D)\) counts equal adjacent pairs around the cyclic word. For \(B=\epsilon\), (14) gives \(D=A\), and the factor \(\pi_{A_0}/\pi_{\eta_0}=1\), giving the same formula. This is the actual inverse IMAGE; the positive length is its negative logarithm.

The table lists every fixed word, with its \(J_{\mathrm{fixed}}\) in parentheses. A dash means the full cylinder has none. The coincidences of \(M\) and \(O\) below are limited to this table.

| Source cylinder | MAIN \(M\) | Root-OFF \(F\) | Payload-OFF \(C\) | Order-OFF \(O\) |
| --- | --- | --- | --- | --- |
| \([0]\) | \(0^\infty\;(2/3)\) | \(0^\infty\;(2/3)\) | \(0^\infty\;(2/3)\) | \(0^\infty\;(2/3)\) |
| \([100]\) | — | — | \((100)^\infty\;(2/27)\) | — |
| \([101]\) | \((10)^\infty\;(1/9)\) | \((10)^\infty\;(1/9)\) | \((101)^\infty\;(2/27)\) | \((10)^\infty\;(1/9)\) |
| \([11000]\) | — | — | \((11000)^\infty\;(8/243)\) | — |
| \([11001]\) | — | — | \((11001)^\infty\;(8/243)\) | — |
| \([11010]\) | — | — | \((11010)^\infty\;(2/243)\) | — |
| \([11011]\) | \((1101)^\infty\;(4/81)\) | \((110)^\infty\;(2/27)\) | \((11011)^\infty\;(8/243)\) | \((1101)^\infty\;(4/81)\) |

Here is an explicit exhaustion check. At \(n=0\), \(A=0,B=\epsilon,D=0\) for every owner. At \(n=1\), the nondeleting owners have \(B=w\): \(w=0\) mismatches the initial \(1\) of \(A\), whereas \(w=1\) gives \(D=01\) and \(1(01)^\infty=(10)^\infty\). At \(n=2\), MAIN roots for \(w=00,01,10,11\) are \(0,01,10,1\); only the last is a prefix of its \(A\), giving \(D=1011\). For \(F\), only \(w=11\) matches, with \(D=011\). For \(O\), the four outputs are \(0,01,01,1\); again only the last matches. Finally \(C\) has \(B=\epsilon,D=A\) in every cell, giving exactly the displayed \(A^\infty\)'s.

For (15), the removed words \(0,01,1011,011\) have respectively lengths \(1,2,4,3\) and equal-edge counts \(1,0,2,1\). The two three-letter \(C\) words each have one equal edge. Among its five-letter words, \(11000,11001,11011\) each have three equal edges, while \(11010\) has one. These counts prove all table densities exactly, without numerical enumeration. Every displayed \(J\) lies in \((0,1)\).

The actual terminal \(\mathbf1\) is not a fixed point of an artificially completed map; its identity and full basin are as in §3.1. Equations (11)–(13) apply separately to every displayed fixed core and every owner. Thus the table has three distinct packets for each of \(M,F,O\), and seven for \(C\), within the frozen window. In particular the two \(C\) cores of length \(\log(27/2)\) and the three of length \(\log(243/8)\) remain distinct packets, not repetitions or phases of one packet.

## 5. Decisive failure, controls and limitations

MAIN's \(p=0^\infty\) lies in the full retained source and has
\[
I_p=\mathbb Z,\qquad H_p=\log(3/2)\mathbb Z.
\tag{16}
\]
Equation (12), not just the existence of a one-step loop, proves (16) for its entire basin. The primitive length is \(\log(3/2)>0\), which cannot equal \(\log p\) for an ordinary prime integer \(p\). This already falsifies the complete target.

The other two MAIN fixed packets have primitive lengths \(\log9\) and \(\log(81/4)\). In particular \(\log9=2\log3\) does NOT make this an allowed repetition of an underlying prime-\(3\) packet: its own entire stabilizer is \(\log9\,\mathbb Z\), which excludes \(\log3\). Relabelling its combinatorial word or ordinary bit period changes neither the stabilizer nor packet identity. All MAIN fixed packets in the tested window are nonprime; no claim about existence or uniqueness of prime packets outside the window is needed or made.

Each control owns (2)–(13) independently. Root-OFF \(F\) changes the \(n=2,w=11\) fixed word and its length from \(\log(81/4)\) to \(\log(27/2)\), showing that the compression affects an actual core rather than only a readout. Payload-OFF \(C\) supplies a fixed word in every tested source cylinder and repeated packet lengths with distinct cores. Order-OFF \(O\) happens to match MAIN's tested cores and lengths, but the equations outside this window and their full inverse basins have not been identified. No control's history groupoid is substituted for MAIN.

The common nonprime \(0^\infty\) obstruction uses the empty-payload branch before any proper-divisor test. It is a retained unit/boundary obstruction, not evidence that the periodic-root operation cannot affect other returns. It also displays a PROVES_TOO_MUCH risk: a finite-cylinder Markov clock can create positive periodic packets without the factor test doing the arithmetic work. The declared Markov law and parser remain design choices; strong naturalness is OPEN. No density change, removal of a null word, selection of a prime packet, or prime-fitted roof repairs this frozen owner.

| Gate | Established evidence | Boundary |
| --- | --- | --- |
| T0 | Full measured Borel source, complete inverse charts, all-point every-Borel IMAGE and history owner | Not a classical symplectic suspension |
| T1 | Same-owner clock exists; prime-only purity fails by (16) | Prime generation/canonical arithmetic law not established |
| T2 | Entire stabilizers, primitive/repetition and packet phases proved for the full source conditionally on its actual cycles, and explicitly for all frozen fixed cores | No higher-period or global packet census |
| T3 | NOT AUDITED | No trace/zeta/operator constructed |
| Formal Routes | Coordinates UNASSIGNED; Route B NOT INVOKED | No Route credit transferred |

The decision is STOP / FORK. The seven full cylinders and all three controls complete the frozen gate; the short test's failure does not authorize extending the census. Full source basins and all incoming paths remain in the stopped object.

## 6. Provenance, reproducibility and research disclosures

The proof input was the complete [candidate card](candidate-card.md), original lines 1–84 through EOF, measured 84 lines, SHA256 fe59e005a560c186b3c666509318e1043bcc5ab16b8a19348d7acbe8e15b28ee. The author independently derived this manuscript after root reported CP1 PASS and separately released mathematics. No scope-review text, reviewer raw proof, peer manuscript or current peer result was read; no author helper was used. A claim-intent ledger was written before the manuscript and then finalized with proof locations in the [claim ledger](claim-ledger.md).

Design-stage input was narrowly bounded. The author read 372-arithmetic-mixture-version/candidate-card.md lines 1–51, not EOF, after heading-only inspection within lines 1–70; the file's measured total was 109 lines and the read prefix SHA256 was 787b60f65c7aa2ad2f21259af5f842f1e3e5844097c3e0ff9e397342cfcb41f2. That prefix contained definitions and OPEN obligations, no appended outcome or proof. No mixture version was borrowed. Filename-only discovery exposed historical names, not their scientific bodies. Prior shared context included a previous read of card 471 lines 1–49/116, not reread for this design, and earlier author work including 483; none supplies proof credit here. Root reported that 481 already uses a Markov-clock block-replication architecture; no 481 file was read. Markov IMAGE is expressly NOT the novelty claim. The actual changed mechanism is periodic-root compression followed by reparsing; no global novelty or nonconjugacy claim is made.

Informal finite-word design algebra occurred before freeze. This is disclosed design exposure, not blind or outcome-sealed preregistration. The current author refreshed the ARS router, academic-paper workflow and runtime policy; retained local guidance, paper-template and writing-role instructions were used for the bounded author stage. ARS supplied claim separation and disclosure discipline, not a mathematical result or expanded research authority.

Methods were exact word cancellation, finite products and measure identities in §§2–4. Shell reads, line counts, SHA256 receipts and final text/link checks are documentary checks only; no scientific code, numerical search, external literature/API, Git operation, PDF or higher-period census was used. Only this package's paper.md, README.md and claim-ledger.md were authored. Root owns card outcomes and integration. The [package README](README.md) is the compact handoff; any later internal review is separate from this author proof.

AI assistance: AI agents supplied candidate design, mathematical derivation, drafting and the project's internal review workflow. This author is the prior definition scout, with inherited shared history and unchanged runtime settings; internal assessment is NOT_CALIBRATED, not blind external peer review. No human or external mathematical verification is certified.

Data availability: all definitions and exact derivations are in this Markdown package; there are no empirical data. Ethics: no human participants, personal data or external uploads were used. Contributions: source design, formal analysis and drafting were performed in the disclosed AI-assisted workflow; root handles research selection/integration and separately assigned agents handle internal review. Funding: no funding information was supplied. Conflicts: no conflict information was supplied; this is not an independently verified absence statement.
