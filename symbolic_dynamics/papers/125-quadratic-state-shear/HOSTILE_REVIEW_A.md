# P125 hostile review A (independent, nonauthor, round 0)

## Decision

**Formal gate: GO (GO_INTERNAL). External release remains HOLD.**

I found no critical or major mathematical error in the round-zero package. The quotient dynamics, Witt pair counts, fibre formula, image filtration, six functional-digraph components, cycle census, zeta function, and the two displayed failures of braid/Yang--Baxter relations all survive independent reconstruction and fresh exhaustive verification. The paper's novelty language is appropriately bounded: the classical quadratic-form, transvection, finite-dynamical, and Yang--Baxter regions are treated as background, and no priority claim is made.

Severity summary:

- **CRITICAL:** none.
- **MAJOR:** none.
- **MINOR A1:** the component checker canonicalizes a directed cycle decoration under reflection as well as rotation. Reflection is not generally an isomorphism of a directed functional cycle. This does not change the present verdict: every admitted component signature is reflection-symmetric, and the only potentially confusable four-cycle placements (adjacent versus alternating attachments) remain distinct. A future checker revision should use rotations only, or document why an undirected decoration convention is sufficient.
- **MINOR A2:** the pointwise classification proof compresses several finite matrix-word calculations into “multiplying the matrix words” and a shortening argument. I independently checked those products and found them correct. A compact transition/product table would improve auditability, but this is not a correctness blocker.

The permitted claim ceiling is the exact analysis of this literal map and the residual synthesis formed by its quotient, fibres, finite transient layers, component census, and zeta data. A claim of general novelty for quadratic transvections, functional-graph enumeration, or set-theoretic Yang--Baxter methods would exceed the evidence. The existing manuscript stays below that ceiling.

## Material reviewed and independence

I reviewed the current `main.tex`, `references.bib`, all support documents, the paper-local verifier and canonical output, `main.pdf`, and frozen `main_round0_original.pdf`. I reconstructed the main calculations without adopting an earlier reviewer conclusion. I did not participate in G03/P125 authorship and did not modify the manuscript, support documents, code, bibliography, or PDFs.

The audited artifact hashes are:

- `main.tex`: `cf8ff8440e506302dfa8d02aaf8abbd24539a72b8293b6c35a336b572fe11872`
- `references.bib`: `138ccfc9deec2c31fc8fad76c7046b2f3ce6c3b34e2dba3f60f8cd64a39c3017`
- `code/verify.py`: `82df023b5e43e9dda5e53df20ef2a7373bf76ea58afb904f18398e50f952f02c`
- `code/verification_output.txt`: `19c1589b9e9e92eac6258047fdc739b9cc1e04c3fdf7aa6efc96853bee9740fe`
- `main.pdf` and `main_round0_original.pdf`: `e9f190aed3d2ac1ec337c7d9133f77d2e17c64f8b18070e74587c6c8397d4368`

The identical PDF hashes confirm that the live artifact is exactly the frozen round-zero artifact.

## Independent reconstruction of the literal map and quotient

Let $V$ be a nonsingular quadratic space over $\mathbb F_2$, let $B$ be the polar form of $Q$, and consider

\[
\Phi(x,y)=(y,x+Q(x)y).
\]

Put $a=Q(x)$, $b=Q(y)$, and $c=B(x,y)$. Since

\[
Q(x+ay)=Q(x)+aQ(y)+aB(x,y)=a+ab+ac=a(1+b+c),
\]

and $B(y,x+ay)=B(y,x)=c$, the quotient update is exactly

\[
(a,b,c)\longmapsto (b,a(1+b+c),c).
\]

Thus $c$ is invariant. This derivation uses the literal state-dependent coefficient $Q(x)$, not a fixed transvection disguised by notation.

For $c=0$, the four quotient states have fates

- $00$: recurrent; period 1 precisely when $x=y$, otherwise period 2;
- $01$: recurrent; period 2 precisely when $x=0$, otherwise period 4;
- $10$: recurrent; period 2 precisely when $y=0$, otherwise period 4;
- $11$: depth 1, landing in the mixed cycle; its eventual period is 2 precisely when $x=y$, otherwise 4.

For $c=1$, the fates are

- $00$: recurrent of exact period 2;
- $01$: depth 2 and eventual period 2;
- $10$: depth 1 and eventual period 2;
- $11$: recurrent of exact period 3.

On the relevant two-dimensional span, the recurrent linear words reduce to

\[
A_0=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
A_1=\begin{pmatrix}0&1\\1&1\end{pmatrix},
\]

with orders 2 and 3. Direct multiplication, together with the exceptional vector equalities above, gives exactly the manuscript's pointwise periods. This closes the main risk that a quotient period might have been mistaken for a point period.

## Witt counts

Write $N=|V|=2^{2m}$, $S=\sum_x(-1)^{Q(x)}=\epsilon 2^m$, so $S^2=N$, and let

\[
C_{abc}=\#\{(x,y):Q(x)=a,Q(y)=b,B(x,y)=c\}.
\]

Expanding the three indicator functions gives

\[
C_{abc}=\frac18\left[N^2+(-1)^aNS+(-1)^bNS+(-1)^{a+b}S^2
+(-1)^cN\{1+(-1)^a+(-1)^b+(-1)^{a+b}S\}\right].
\]

The mixed Walsh sums are $N,N,N,NS$, respectively; this is the place where a sign or Witt-type error would propagate through every later count. Substitution yields exactly the four quantities used in the manuscript:

\[
H=C_{000}=\frac{N(N+3S+4)}8,
\]

\[
M=C_{010}=C_{100}=C_{110}=\frac{N(N-S)}8,
\]

\[
A=C_{001}=C_{011}=C_{101}=\frac{N(N+S-2)}8,
\]

and

\[
Z=C_{111}=\frac{N(N-3S+2)}8.
\]

The boundary cases, including the zero-dimensional plus space and the two-dimensional minus space, are consistent; zero component counts in these cases are genuine rather than a hidden division failure.

## Fibres, image, and transient layers

Solving $\Phi(x,y)=(u,v)$ gives the exact disjoint description

\[
\Phi^{-1}(u,v)
=\{(v,u):Q(v)=0\}\ \sqcup\
\{(u+v,u):Q(u+v)=1\}.
\]

If both candidates existed and coincided, then $u=0$ and the same vector would have to be simultaneously singular and nonsingular; hence the union is disjoint. With the bijective change of variables $(u,v)\leftrightarrow(v,w=u+v)$, the indegree census is

\[
d_0=d_2=\frac{N(N-1)}4,\qquad
d_1=\frac{N(N+1)}2.
\]

The fibre-count table by target quotient type, with columns $ab=00,01,10,11$, is

\[
\begin{array}{c|cccc}
c=0&1&1&2&0\\
c=1&2&0&1&1.
\end{array}
\]

It follows that the first image consists of the recurrent set together with the $c=1,ab=10$ stratum. That extra stratum maps to recurrent $c=1,ab=00$. Every recurrent point has predecessors at all times along its cycle, so the equality is pointwise and setwise:

\[
\operatorname{im}\Phi^2=\operatorname{Rec}(\Phi).
\]

Consequently

\[
|\operatorname{im}\Phi|=\frac{N(3N+1)}4,
\qquad
|\operatorname{im}\Phi^t|=\frac{N(5N-S+4)}8\quad(t\ge2),
\]

and the exact depth layers are

\[
L_0=\frac{N(5N-S+4)}8,\qquad
L_1=\frac{N(N-1)}4=M+A,\qquad
L_2=\frac{N(N+S-2)}8=A.
\]

This independently confirms both the maximum depth two statement and the distinction between first-image and recurrent counts.

## Six literal functional components

Tracing the quotient transitions backward through the fibre table, and then applying the pointwise exceptional conditions, gives exactly six component types:

1. A bare fixed point, count $N_0=(N+S)/2$.
2. A bare $c=0,ab=00$ two-cycle, count $(H-N_0)/2$.
3. A $c=0$ mixed exceptional two-cycle with one leaf at one cycle vertex, count $N_1=(N-S)/2$.
4. A $c=1,ab=00$ two-cycle with a length-two tail at each cycle vertex, count $A/2$.
5. A bare $c=1,ab=11$ three-cycle, count $Z/3$.
6. A $c=0$ mixed four-cycle with one leaf at each of two alternating cycle vertices, count $(M-N_1)/2$.

The zero-fibre entries rule out extra branches, and the global indegree ceiling two rules out additional hidden attachments. The reverse type chains also force the advertised placement of leaves and length-two tails. This is a genuine literal component census, not merely an orbit-period list.

As noted in MINOR A1, the verifier's component signature routine considers reflections as well as rotations. I explicitly checked that this does not merge an actual component with an unlisted directed component here: the six admitted signatures are reflection-symmetric, while adjacent and alternating attachments on a four-cycle remain inequivalent even under the larger relation.

## Cycle census and zeta function

Summing the cycles in the six components and simplifying gives

\[
c_1=\frac{N+S}{2},
\]

\[
c_2=\frac{N^2+2NS+3N-6S}{8},
\]

\[
c_3=\frac{N(N-3S+2)}{24},
\qquad
c_4=\frac{N^2-NS-4N+4S}{16}.
\]

The functional graph has no other recurrent periods, so the Artin--Mazur product is exactly

\[
\zeta_\Phi(t)=
(1-t)^{-c_1}(1-t^2)^{-c_2}(1-t^3)^{-c_3}(1-t^4)^{-c_4}.
\]

I also checked the zero-dimensional specialization; the formulas do not silently assume $m\ge1$.

## Braid and Yang--Baxter failures

The two counterexamples were checked directly in a hyperbolic plane. Choose singular $e,f$ with $B(e,f)=1$, and put $g=e+f$, so $Q(g)=1$.

For the braid relation at $(g,e,f)$, literal composition gives

\[
\Phi_{12}\Phi_{23}\Phi_{12}(g,e,f)=(f,e,f),
\]

whereas

\[
\Phi_{23}\Phi_{12}\Phi_{23}(g,e,f)=(f,e,e).
\]

For the quantum Yang--Baxter convention used in the manuscript, at $(g,g,e)$ one obtains

\[
R_{12}R_{13}R_{23}(g,g,e)=(e,f,e),
\]

but

\[
R_{23}R_{13}R_{12}(g,g,e)=(e,f,0).
\]

Thus both failures are literal and convention-specific; neither is inferred only from nonbijectivity.

## Owner subtraction and novelty boundary

I checked the bibliography and the paper's subtraction language against the following primary or publisher-hosted records:

- Fulton, “Representations by Quadratic Forms in a Finite Field of Characteristic Two,” *Mathematische Nachrichten* 77 (1977), 237--243, DOI `10.1002/mana.19770770117`.
- Hall and Shpectorov, “The spectra of finite 3-transposition groups,” including its orthogonal-$\mathbb F_2$ and transvection background; publisher/arXiv versions agree on the relevant setup.
- Sjöstrand, “Orbits under transvection groups,” *Linear Algebra and its Applications* 710 (2025), 507--530, DOI `10.1016/j.laa.2025.02.010`, for fixed-center linear transvections and their generated groups.
- Etingof--Schedler--Soloviev for the standard bijective set-theoretic quantum Yang--Baxter setting.
- Catino--Colazzo--Stefanelli, “Set-theoretic solutions to the Yang--Baxter equation and generalized semi-braces,” *Forum Mathematicum*, DOI `10.1515/forum-2020-0082`, as a nonbijective/finite-order YBE boundary.
- Artin--Mazur for the dynamical zeta background.

Exact literal searches for the formula $(y,x+Q(x)y)$, its state-dependent shear $x+Q(x)y$, and close Yang--Baxter variants did not locate a direct owner. This is only a bounded non-hit, not proof of novelty. The manuscript and support documents correctly say so, assign zero credit to the classical owner regions, retain substantial owner risk, and keep external release on HOLD. The residual paper-scale value is the complete exact synthesis for this literal nonbijective state-dependent shear.

## Internal collision audit

The internal firewall was checked against the cited corpus items rather than accepted by title alone:

- P99 studies a fixed unipotent shear on integer sublattices and is bijective; it does not contain the quadratic state-dependent coefficient or the present fibres.
- P103 studies double-adjugate rank/scalar-power dynamics; its mechanism and invariants differ.
- P106 has the closest shallow-transient silhouette through polarity dynamics, but depth, periods, fibres, and state rule are different.
- P109 concerns a nilpotent subspace-image mechanism with a unique recurrent part, not this six-component finite quadratic graph.
- P118 shares a quotient/fibre/basin/zeta presentation architecture for a mex multipartite system, not the literal map or formulas here.

A broader corpus search also found finite algebra dynamics such as P102, but no material collision with the quadratic state-dependent shear, Witt pair census, or six-component result. Architectural resemblance is explicitly not claimed as new mathematics.

## Fresh mechanical verification

I reran the paper-local verifier from the P125 directory with bytecode writing disabled and redirected stdout to a fresh temporary file. The run completed with

    ASSERTIONS 27405886
    PASS

The fresh stdout hash was `19c1589b9e9e92eac6258047fdc739b9cc1e04c3fdf7aa6efc96853bee9740fe`, byte-for-byte identical to the frozen canonical output.

The verifier exhausts the zero-dimensional plus case and both Witt signs for $m=1,\ldots,5$, reaching $|V|=1024$ and $1,048,576$ state pairs. It checks the literal update, quotient, orbit classification, fibre counts, all $C_{abc}$, image layers, pointwise `image^2 = recurrent`, cycle counts, and actual connected-component signatures. The computation is integer, deterministic, local, and uses no network, random sampling, floating point, or external CAS.

## Isolated four-stage build, visual audit, and metadata

I copied only `main.tex` and `references.bib` into a fresh temporary directory and ran

1. `pdflatex`,
2. `bibtex`,
3. `pdflatex`,
4. `pdflatex`.

All four stages returned exit status zero. The final log had zero warning hits. The isolated PDF hash was `e9f190aed3d2ac1ec337c7d9133f77d2e17c64f8b18070e74587c6c8397d4368`, exactly matching both packaged PDFs.

The artifact is 5 A4 pages and 363,856 bytes. I rendered and inspected every page. I found no clipping, overlap, missing glyph, broken reference, malformed equation, or displaced float. Page 5 contains the concluding references with unused lower-page space, which is harmless. Fonts are embedded/subsetted and Unicode mapping is present.

PDF metadata inspection found blank Author, Title, Subject, and Keywords fields, with no custom metadata stream, form, JavaScript, encryption, or identifying author leakage. The manuscript remains anonymous.

## Required disposition

No round-one repair is required for internal circulation. MINOR A1 and A2 are recommended auditability improvements only; neither changes a theorem, formula, count, verifier outcome, or PDF integrity.

**Final verdict: GO / GO_INTERNAL. External release: HOLD pending a dedicated direct-owner/novelty search and the project's release gate.**
