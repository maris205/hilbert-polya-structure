# Hostile gate — G03 quadratic-state shear

**Role:** independent nonauthor proof/value/owner gate  
**Candidate:** G03 in the replacement scout  
**Decision:** **GO** to internal paper allocation, subject to the mandatory
repairs in Section 11  
**External status:** **HOLD**; no novelty, priority, posting, or submission
claim is authorized

I did not author the candidate, and I made no change to `SCOUT.md`,
`QUADRATIC_STATE_SHEAR_REPORT.md`, the verifier, or its canonical output. This
gate reconstructs the mathematics rather than treating the 20-million-assertion
run as a proof. The result is positive: I found no false all-size formula or
missing functional-component shape. The exact map remains owner-sensitive
because it is so short, but a fresh primary-source search found no literal or
conjugate-map owner. The full fibre/image/layer/component package is large
enough for a short paper after a few precise evidence and attribution repairs.

## 1. Literal map, boundaries, and claim ceiling

Let \((V,Q)\) be a nonsingular quadratic space of dimension \(2m\) over
\(\mathbb F_2\), with polar form
\[
B(x,y)=Q(x+y)+Q(x)+Q(y).
\]
The state space is \(V^2\), and
\[
\Phi(x,y)=(y,x+Q(x)y).                                      \tag{1}
\]
Write
\[
N=|V|=2^{2m},\qquad
S=\sum_x(-1)^{Q(x)}=\varepsilon 2^m,qquad
\varepsilon\in\{+1,-1\}.                                  \tag{2}
\]
Only the plus convention exists at \(m=0\). Both Witt signs occur for
\(m\ge1\).

The defensible contribution is not the static quadratic-space census, the
Arf/Witt classification, transvection theory, or the formal conversion from
cycle counts to zeta. It is the exact functional graph of the literal
nonbijective, \(O(V,Q)\)-equivariant map (1): pointwise fates, fibres, images,
Witt-sensitive layers, all decorated components, and the resulting cycle
census. Any eventual paper must keep that ceiling.

Equivariance is immediate and worth stating accurately: for
\(g\in O(V,Q)\),
\[
\Phi(gx,gy)=(gy,gx+Q(gx)gy)=g\Phi(x,y).
\]
This gives the map a basis-free finite-geometry meaning. It does not make the
map an orthogonal-group action or make its eight type classes full
\(O(V,Q)\)-orbits.

## 2. Three-bit quotient and pointwise dynamics

For
\[
a=Q(x),\qquad b=Q(y),\qquad c=B(x,y),
\]
put \((u,v)=\Phi(x,y)\). Polarization gives
\[
Q(u)=b,
\qquad
Q(v)=Q(x+ay)=a+ab+ac=a(1+b+c),
\]
and alternation gives
\[
B(u,v)=B(y,x+ay)=B(y,x)=c.
\]
Thus
\[
(a,b,c)\longmapsto (b,a(1+b+c),c).                         \tag{3}
\]
The polar bit really is invariant. Exhausting the four \((a,b)\)-states for
each \(c\) produces exactly the dossier's quotient table:

| \(c\) | quotient motion |
|---:|---|
| 0 | \(00\to00\), \(01\leftrightarrow10\), \(11\to10\) |
| 1 | \(00\to00\), \(01\to10\to00\), \(10\to00\), \(11\to11\) |

The quotient alone does not determine the shorter pointwise periods, so I
also solved the matrix equalities. If the departing first vector is singular,
the pair matrix is the swap
\[
S_0=\begin{pmatrix}0&1\\1&0\end{pmatrix};
\]
if it is nonsingular, it is
\[
S_1=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\]
The resulting classification is correct:

* \(c=0,00\): period one precisely when \(x=y\), otherwise period two;
* \(c=0,01\): period two precisely when \(x=0\), otherwise period four;
* \(c=0,10\): period two precisely when \(y=0\), otherwise period four;
* \(c=0,11\): depth one, then period two precisely when \(x=y\), otherwise
  period four;
* \(c=1,00\): exact period two, since \(B(x,x)=0\) rules out \(x=y\);
* \(c=1,01\): exact depth two followed by period two;
* \(c=1,10\): exact depth one followed by period two;
* \(c=1,11\): exact period three; the order-three matrix has no admissible
  fixed pair.

Hence the universal depth ceiling is two and the only periods are
\(1,2,3,4\). The small-form exceptions are also correct. Depth two has size
\(A=N(N+S-2)/8\): it is nonzero for the plus plane at \(m=1\), zero for the
minus plane at \(m=1\), and nonzero for both signs when \(m\ge2\). At \(m=0\)
the unique state is fixed.

I found no omitted equality case and no hidden period divisor.

## 3. Reverse formula and fibre distribution

For a target \((u,v)\), an unknown preimage has the form \((x,u)\) and must
satisfy
\[
v=x+Q(x)u.
\]
Splitting by \(Q(x)\) yields exactly two possible sources:
\[
\Phi^{-1}(u,v)
=\{(v,u):Q(v)=0\}\ \cup\
 \{(u+v,u):Q(u+v)=1\}.                                  \tag{4}
\]
Both candidates satisfy (1). If the two displayed ordered pairs were equal,
then \(u=0\), but the two membership conditions would demand both
\(Q(v)=0\) and \(Q(v)=1\). Thus they are distinct whenever both occur, and
\[
|\Phi^{-1}(u,v)|
=\mathbf1_{Q(v)=0}+\mathbf1_{Q(u+v)=1}\in\{0,1,2\}.       \tag{5}
\]

The global fibre histogram has an especially short independent derivation.
The change of variables \((u,v)\leftrightarrow(v,w=u+v)\) is a bijection on
\(V^2\). A missing target has \(Q(v)=1,Q(w)=0\); a double target has
\(Q(v)=0,Q(w)=1\). Since
\[
N_0=\frac{N+S}{2},\qquad N_1=\frac{N-S}{2},
\]
both numbers equal
\[
N_0N_1=\frac{N^2-S^2}{4}=\frac{N(N-1)}4.
\]
The remaining targets have fibre one. Therefore
\[
d_0=d_2=\frac{N(N-1)}4,
\qquad d_1=\frac{N(N+1)}2.                                \tag{6}
\]
This part of the dossier is exact and does not depend on the eight-type
Walsh census.

## 4. Images and temporal layers

Evaluating (5) on the eight types gives

| \(c\) | 00 | 01 | 10 | 11 |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 2 | 0 |
| 1 | 2 | 0 | 1 | 1 |

Combining this with the pointwise table gives a setwise statement, not merely
a cardinality statement:

* the missing types are transient \((c=0,11)\) and depth-two
  \((c=1,01)\);
* the first image is the recurrent set together with the depth-one type
  \((c=1,10)\);
* that extra type maps into recurrent \((c=1,00)\);
* every recurrent point has predecessors of every iterate along its cycle.

Consequently
\[
\operatorname{im}\Phi^2=\operatorname{Rec}(\Phi),
\qquad
\operatorname{im}\Phi^t=\operatorname{Rec}(\Phi)\quad(t\ge2). \tag{7}
\]
The sizes in the report follow once the type counts are inserted:
\[
|\operatorname{im}\Phi|=\frac{N(3N+1)}4,
\qquad
|\operatorname{im}\Phi^t|=rac{N(5N-S+4)}8\quad(t\ge2). \tag{8}
\]

The exact depth layers are also correct:
\[
L_0=\frac{N(5N-S+4)}8,
\qquad
L_1=\frac{N(N-1)}4,
\qquad
L_2=\frac{N(N+S-2)}8.                                    \tag{9}
\]
Here \(L_1=C_{110}+C_{101}=M+A\), while \(L_2=C_{011}=A\).

As an extra gate control, independent of the canonical script, I constructed
the literal first and second image sets for both signs through \(m=4\) and
compared the second image point-for-point with the set of states of preperiod
zero. Equality held in every lane, including the \(m=0\) boundary.

## 5. Witt-sensitive pair census

For
\[
C_{abc}=\#\{(x,y):Q(x)=a,Q(y)=b,B(x,y)=c\},
\]
the character expansion is
\[
\begin{aligned}
C_{abc}=\frac18[&N^2+(-1)^aNS+(-1)^bNS+(-1)^{a+b}S^2\\
&+(-1)^cN\{1+(-1)^a+(-1)^b+(-1)^{a+b}S\}].              \tag{10}
\end{aligned}
\]
Every transform term checks out:

* the zero-\(B\) character gives \(N^2,NS,NS,S^2\);
* nondegeneracy gives
  \(\sum_{x,y}(-1)^{B(x,y)}=N\);
* the two one-quadratic mixed sums are each \(N\);
* polarization gives
  \(Q(x)+Q(y)+B(x,y)=Q(x+y)\), so the final mixed sum is
  \(NS\).

Since \(S^2=N\), this reduces to
\[
\begin{aligned}
H=C_{000}&=\frac{N(N+3S+4)}8,\\
M=C_{010}=C_{100}=C_{110}&=\frac{N(N-S)}8,\\
A=C_{001}=C_{011}=C_{101}&=\frac{N(N+S-2)}8,\\
Z=C_{111}&=\frac{N(N-3S+2)}8.                            \tag{11}
\end{aligned}
\]

The alternative hyperplane count is also correct for nonzero \(x\):
\[
\#\{y:Q(y)=b,B(x,y)=c\}
=\frac14\left[N+(-1)^bS+(-1)^{a+b+c}S\right].            \tag{12}
\]
It follows by expanding the two indicators; the pure nontrivial linear
character sums to zero, while completing the quadratic character by the
linear form contributes \((-1)^aS\). The \(x=0\) case must, and in the
dossier does, remain separate.

The two census routes are genuinely different calculations. The static
identities themselves must receive zero contribution credit and precise
finite-quadratic-geometry citations.

## 6. Decorated components and zeta

The reverse table does force exactly the six claimed component shapes.

* In \(c=0,00\), swap gives \(N_0\) fixed points; all other states lie in
  bare 2-cycles.
* In \(c=0,01/10\), a type-10 cycle vertex has its cycle predecessor of type
  01 and one additional type-11 leaf. If a coordinate is zero, this is a
  2-cycle with one leaf; otherwise it is a 4-cycle with leaves on the two
  alternating type-10 vertices.
* In \(c=1,00\), every 2-cycle vertex has one type-10 predecessor, and that
  predecessor has one type-01 predecessor. Thus there is one length-two tail
  at each cycle vertex.
* In \(c=1,11\), all components are bare 3-cycles.

No deeper tree is possible because types 11 and 01 in the relevant lanes
have fibre zero, and the fibre ceiling is two. The component counts therefore
are
\[
N_0,\quad \frac{H-N_0}{2},\quad N_1,\quad \frac A2,
\quad \frac Z3,\quad \frac{M-N_1}{2},                    \tag{13}
\]
in the order listed in the dossier.

I independently traversed the literal undirected functional components for
both signs through \(m=3\), canonically recording each cycle together with
the reverse rooted tree at every cycle vertex. Every component had one of
the six shapes, the two leaves on a 4-cycle were alternating, and the literal
counts agreed with (13). Some shape counts vanish in the small planes; this
is already handled by the formulas.

The cycle counts obtained from (13) are
\[
\begin{aligned}
c_1&=\frac{N+S}{2},\\
c_2&=\frac{N^2+2NS+3N-6S}{8},\\
c_3&=\frac{N(N-3S+2)}{24},\\
c_4&=\frac{N^2-NS-4N+4S}{16}.                            \tag{14}
\end{aligned}
\]
They match the pointwise periodic census. Hence the finite-map zeta is the
routine cycle product
\[
\zeta_\Phi(t)=
(1-t)^{-c_1}(1-t^2)^{-c_2}(1-t^3)^{-c_3}(1-t^4)^{-c_4}.  \tag{15}
\]
The zeta conversion is zero-credit bookkeeping; the nonroutine result is the
component classification that supplies the exponents.

One narrative overclaim needs repair. Section 5 calls the reverse proof
“logically independent” of the forward period proof, but its prose already
uses the cycle types and exceptional shorter periods established in Section
2. The fibre engine independently determines the attached trees and checks
the component mass; as currently written it is **complementary**, not a
self-contained second proof of the entire period/component theorem. Either
weaken “logically independent” to “complementary,” or actually rederive all
cycle periods in the reverse section.

## 7. Fresh verifier audit

I freshly ran

```text
python3 docs/papers122_126_sequence/scouting/replacement/replacement_quadratic_shear_verify.py
```

The output ended with

```text
ASSERTIONS 20133012
PASS
```

and was byte-identical to the canonical transcript. At gate time:

```text
replacement_quadratic_shear_verify.py
  SHA-256 c1a8e7ac9ded27cac60e9d1c30ef0f8e02a81374b9efd6c35c43aa18107744d0
replacement_quadratic_shear_verify.out
  SHA-256 7f991759606813d04a97c313e9c0097b5b04f61d5848b277a13db96f605432bb
```

The literal orbit, quotient, pair-type, pointwise-fibre, histogram, layer,
image-size, and cycle assertions are strong. Two statements in the dossier
overdescribe what the code literally checks:

1. `len(image2) == recurrent` checks only the **size** of the second image,
   not equality of the second-image set with the recurrent set;
2. `expected_component_counts` calculates the six formulas and verifies
   cycle/state mass identities, but the script never traverses components or
   compares their literal rooted shapes.

The mathematical proofs cover both facts, and my independent scratch controls
confirmed them. This is therefore not a theorem failure. Before paper freeze,
however, the canonical verifier should assert pointwise second-image equality
and perform literal component traversal, or its coverage description must be
narrowed. Given how heavily the candidate advertises two independent engines,
strengthening the verifier is preferable.

## 8. Primary-source owner search

I ran fresh exact and equivalent-map searches using the current network,
including the strings

```text
(x,y) (Q(x)) (x+Q(x)y)
x + Q(x) y characteristic 2
quadratic-state shear finite field
conditional shear quadratic form F_2
quadratic form state-dependent transvection
quadratic set / nonbijective Yang--Baxter / finite-order pair map
```

and variants with `swap`, `Nielsen`, `switch`, `orthogonal`, `symplectic`,
`functional graph`, and `ordered pair`. I also searched recent arXiv records
through 2026 for finite quadratic-space functional graphs and conditional
transvections. No located primary source states (1), a conjugate of (1), its
fibre formula, or its six component shapes. This remains a bounded non-hit,
not a priority certificate.

### 8.1 Static quadratic counts

Fulton's primary paper,
[*Representations by Quadratic Forms in a Finite Field of Characteristic
Two*](https://doi.org/10.1002/mana.19770770117), is a legitimate owner-region
source for characteristic-two quadratic representation counts. Hall and
Shpectorov's primary paper,
[*The spectra of finite 3-transposition
groups*](https://arxiv.org/abs/1809.03696), uses the relevant orthogonal
\(\mathbb F_2\) geometry and Witt-sign vector classes in a different problem.
Neither source located in this pass defines the state shear (1). A paper must
cite a precise proposition or standard source for \(N_0,N_1\) and any pair
orbit/census fact it treats as classical; citing a broad owner region is not
enough.

### 8.2 Orthogonal and symplectic transvections

The direct modern primary comparison is Sjöstrand,
[*Orbits under Dual Symplectic
Transvections*](https://arxiv.org/abs/2312.03933), published in *Linear Algebra
and its Applications* 710 (2025), 507--530. There the elementary map has the
form
\[
z\longmapsto z+k\,\omega(z,s)s
\]
for a fixed centre \(s\); it is an invertible linear map, and the paper studies
orbits of the generated group and its dual action. In characteristic two, an
orthogonal transvection similarly uses a nonsingular fixed root and the polar
coefficient \(B(z,s)\).

G03 instead updates an ordered pair, uses the scalar \(Q(x)\) of the moving
state, changes which vector supplies the shear at every step, and is
noninjective with \(N(N-1)/4\) missing targets. It is neither a transvection
nor an action of a transvection group. Transvection orbit theory should be
fully credited as neighboring machinery but does not own the literal
functional graph.

### 8.3 Yang--Baxter and quadratic-set maps

Etingof--Schedler--Soloviev,
[*Set-theoretical solutions to the quantum Yang--Baxter
equation*](https://arxiv.org/abs/math/9801047), studies bijections of
\(X\times X\). That alone separates its main setting from G03, but it is not
enough owner subtraction: nonbijective finite-order solutions are also a real
literature. For example, Catino--Colazzo--Stefanelli,
[*Set-theoretic solutions to the Yang--Baxter equation and generalized
semi-braces*](https://arxiv.org/abs/2004.01606), explicitly treats
nonbijective solutions and their index/period.

I therefore tested the defining equations rather than relying on
nonbijectivity. G03 is **not** a Yang--Baxter solution. In the plus hyperbolic
plane choose \(e,f\) with \(Q(e)=Q(f)=0\), \(B(e,f)=1\). For the braid form,
on \((e+f,e,f)\),
\[
\Phi_{12}\Phi_{23}\Phi_{12}(e+f,e,f)=(f,e,f),
\]
whereas
\[
\Phi_{23}\Phi_{12}\Phi_{23}(e+f,e,f)=(f,e,e).
\]
It also fails the quantum \(R_{12}R_{13}R_{23}=R_{23}R_{13}R_{12}\)
convention: on \((e+f,e+f,e)\), with products acting right-to-left, the two
sides give \((e,f,e)\) and \((e,f,0)\). Thus ordinary bijective and
nonbijective Yang--Baxter classifications are neighbor firewalls, not direct
owners.

The current dossier should add the nonbijective primary source and an explicit
failure witness. Describing the entire neighbor only as “generic bijective
pair maps” is too narrow.

### 8.4 Owner verdict

**No direct owner found; risk remains medium-high.** The non-hit is meaningful
enough for internal allocation because searches covered the literal formula,
equivalent state-dependent shears, transvection formulations, and both
bijective and nonbijective Yang--Baxter lanes. The formula is short enough
that a specialist finite-geometry search must continue during drafting. A
same-map result, or a conjugacy transporting an already-classified functional
graph, remains an immediate KILL condition. External status stays HOLD.

## 9. P1--P121 internal collision audit

No P1--P121 paper located by literal and semantic search uses a nonsingular
quadratic \(\mathbb F_2\)-space, the update (1), or its three-bit quotient.
The relevant collisions are package or vocabulary collisions, not theorem
identity.

| Internal paper | Overlap | Required subtraction |
|---|---|---|
| **P99 — unipotent shear on fixed-index sublattices** | “Shear,” complete cycle inventory, and zeta. | P99 is a bijective action of one fixed integer matrix on HNF layers, with arbitrarily long valuation-controlled cycles. G03 is a nonlinear, nonbijective state-gated map on \(V^2\), with depth at most two and periods at most four. Do not market “shear + zeta” as new. |
| **P103 — double-adjugate matrix dynamics** | Nonlinear finite-field dynamics, image tower, recurrent core, cycle/zeta census. | P103 reduces via Jacobi to scalar power maps on matrix-rank strata. G03's residue is the quadratic/polar three-bit quotient plus nonuniform 0/1/2 fibres and six component shapes. |
| **P106 — synchronous MIS polarity dynamics** | Very shallow universal functional graph, short periods, complete periodic census and zeta. This is the closest temporal silhouette. | P106 is the order-reversing Boolean polarity \(F^3=F\), so preperiod is at most one and periods at most two. G03 has two Witt signs, a genuine depth-two layer, periods 3 and 4, nonuniform fibres, and decorated tails. |
| **P109 — nilpotent image subspace dynamics** | Finite linear-algebra carrier, exact fibres, image/absorption layers, functional graph. | P109 is the monotone nilpotent image map on the full subspace lattice and has a unique periodic point. G03 acts on vector pairs, is not monotone or nilpotent, and has a Witt-sensitive recurrent core with four possible periods. |
| **P118 — synchronous mex multipartite dynamics** | Full finite functional graph from a small quotient, exact fibres, basin layers and zeta. | P118 is graph-colouring dynamics with labelled-EGF fibres. G03 has pointwise quadratic-space fibres and character-sum/Witt enumeration. The reusable “quotient + fibres + zeta” architecture earns no novelty credit. |

P102's nonlinear finite group-algebra norm map and other finite-field papers
add a generic “full functional graph over a finite algebraic carrier”
portfolio silhouette, but no closer mechanism. The internal paper must lead
with the \(O(Q)\)-equivariant conditional pair update, the exact reverse
formula, and the six Witt-sensitive decorated components. Generic claims of
having a finite-field shear, exact fibres, image layers, or a zeta function
are already spent internally.

## 10. Paper-scale value

After zero-credit subtraction, the quotient table or period ceiling alone
would be too thin. The conjunction is paper-scale:

1. a basis-free nonbijective pair update with a complete pointwise temporal
   classification;
2. a two-candidate inverse formula giving every fibre and the full image
   tower;
3. exact formulas for all temporal layers in both Witt signs;
4. a complete six-shape functional graph, not only fixed/cycle counts; and
5. two compatible enumerative engines, character/hyperplane counts and
   reverse-tree reconstruction.

The formulas are compact, the boundaries are nontrivial (especially the
minus plane's vanished depth-two layer), and the component shapes expose more
than a routine finite-map zeta. This is sufficient for a focused short paper.
It is not sufficient for broad claims about quadratic dynamics,
transvection orbits, Yang--Baxter maps, or new finite-geometry enumeration.

The best narrative is: “a minimal \(O(Q)\)-equivariant conditional shear has
a completely solvable but nonuniform functional graph.” The worst narrative
is: “a new quadratic/transvection/Yang--Baxter system with an exact zeta.”

## 11. Findings and mandatory repairs

### CRITICAL

None.

### MAJOR

**M1 — canonical-control coverage is overstated.** Add a literal assertion
that \(\operatorname{im}\Phi^2\) equals, rather than merely has the size of,
the recurrent set. Traverse and classify actual functional components rather
than checking only the six expected formulas and their mass identities. If
the code is not strengthened, narrow the coverage claims.

**M2 — the claimed independence of the reverse proof is overstated.** As
written, the reverse component proof uses the forward cycle classification.
Call the routes complementary or add a self-contained reverse derivation of
all cycle types and periods.

**M3 — the Yang--Baxter owner firewall is incomplete.** Add a primary source
for nonbijective finite-order set-theoretic solutions and explicitly record
that (1) fails both the braid and quantum Yang--Baxter equations. A reference
only to bijective Etingof--Schedler--Soloviev maps is not enough.

**M4 — exact classical-source anchors are needed.** Identify a precise
primary/standard theorem for the singular/nonsingular vector counts and any
orthogonal pair census credited as known. Keep the character-sum derivation
self-contained even after citation.

### MINOR

**m1.** State explicitly that the eight types are a quotient sufficient for
dynamics, not necessarily the complete orthogonal orbit partition.

**m2.** Keep the \(m=0\), plus-plane \(m=1\), and minus-plane \(m=1\)
boundaries adjacent to every depth/component theorem, not only in the pilot.

**m3.** Use `nonsingular vector` for \(Q(x)=1\) and reserve `nonzero` for
\(x\ne0\); those notions differ in characteristic two.

**m4.** Present the short product-code argument for (6). It is clearer and
more independent than deriving the global histogram only from the eight
Walsh counts.

**m5.** State that the zeta is standard cycle bookkeeping and that the value
lies in the component census.

### Required pre-freeze actions

1. implement or accurately disclaim the two missing verifier lanes in M1;
2. repair the independence language in M2;
3. expand the owner ledger as in M3--M4, retaining exact query/date notes;
4. include an explicit comparison against P99, P103, P106, and P109, with
   P106 identified as the closest temporal silhouette;
5. preserve all small-Witt boundaries and the zero-credit ceiling;
6. rerun an independent hostile review after a manuscript exists;
7. keep external circulation and all priority language on HOLD.

## 12. Final verdict

**GO** to internal paper allocation. The algebraic theorem package survives
hostile reconstruction, the fresh 20,133,012-assertion run is canonical, the
extra pointwise image/component controls pass, and no direct owner or internal
literal collision was found. The residual full-functional-graph result is
paper-scale.

This is not an unconditional release decision. The exact-control overclaim,
reverse-proof independence wording, nonbijective Yang--Baxter firewall, and
classical-source anchors must be repaired before freeze. **External HOLD
remains absolute.**
