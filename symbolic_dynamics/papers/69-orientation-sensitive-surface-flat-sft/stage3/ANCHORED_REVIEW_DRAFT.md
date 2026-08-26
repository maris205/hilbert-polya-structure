<!--block:B0001-->
# Introduction

<!--block:B0002-->
For a shift action of a finitely generated group, periodic data are indexed by finite-index subgroups rather than by one integer. This makes the topology of the corresponding finite covers available to symbolic dynamics. The purpose of this paper is to exhibit a finite-type system for which orientable and nonorientable cover directions read genuinely different parts of finite-group representation theory.

<!--block:B0003-->
The acting group is \[\LambdaSurf
 =\left\langle x_1,x_2,x_3
   \mathrel{\big|}x_1^2x_2^2x_3^2=1\right\rangle,
 \label{eq:surface-presentation}\] the fundamental group of the closed nonorientable surface \(N_3\). For a finite group \(\K\), we place a \(\K\)-label on each positively oriented generator edge of the Cayley \(2\)-complex and require the ordered product around every lift of the relator to be the identity. This is a subshift of finite type, denoted \(X_{\K}\). When a finite-index subgroup \(H\leq\LambdaSurf\) fixes a configuration, that configuration descends to a flat \(\K\)-connection on the finite surface cover associated with \(H\).

<!--block:B0004-->
Periodic points of group shifts and their finite-index organization have been studied in a general setting by Carroll and Penland \[@CarrollPenland2015\]. Surface groups also support rich finite-type symbolic systems; see, for example, Cohen and Goodman-Strauss \[@CohenGoodmanStrauss2017\]. Our count uses a different, elementary flat-connection model.

<!--block:B0005-->
Periodic data already recover a finite-group parameter in a distinct family of higher-dimensional Markov shifts. Ward obtained an almost-classification, and Roettger completed the classification, for Ledrappier-type algebraic \(\ZZ^2\)-shifts parameterized by finite abelian groups \[@Ward1998; @Roettger2005\]. Those works own the periodic-data recovery/classification principle in that family. They do not contain the present surface-group construction: their acting group is \(\ZZ^2\), their model is an abelian group shift, and their recovered object is the finite abelian parameter itself. Here the acting group is \(\pi_1(N_3)\), the configurations are nonabelian edge labels, and the selected spectra recover character degrees and Frobenius–Schur types.

<!--block:B0006-->
The representation-theoretic inputs are the classical surface-group homomorphism formulas of Mednykh and Frobenius–Schur. Snyder gave a lattice-TQFT proof of the orientable and nonorientable formulas \[@Snyder2007\], so neither the lattice surface-counting viewpoint nor those formulas are contributions of this paper. We choose Klug’s modern account as the normalization source \[@Klug2025\]; this bibliographic choice does not alter historical ownership.

<!--block:B0007-->
Define a homomorphism \(f\colon\LambdaSurf\to\ZZ\) and the orientation character \(\omega\colon\LambdaSurf\to\ZZ/2\ZZ\) by \[\begin{aligned}
 &f(x_1)=1,\qquad f(x_2)=-1,\qquad f(x_3)=0,\\
 &\omega(x_1)=\omega(x_2)=\omega(x_3)=1.
 \end{aligned}
 \label{eq:f-and-omega}\] The two divisibility-directed subgroup families used throughout are \[H_n=\ker(\LambdaSurf\xrightarrow{f}\ZZ\to\ZZ/n\ZZ),
 \qquad
 L_m=\ker(\ker\omega\xrightarrow{f}\ZZ\to\ZZ/m\ZZ).
 \label{eq:two-families}\] They are explicit kernels of cyclic quotients. The \(H_n\)-cover is nonorientable of genus \(n+2\), whereas the \(L_m\)-cover is orientable of genus \(m+1\).

<!--block:B0008-->
For \(\chi\in\Irr(\K)\), write \[d_\chi=\chi(1),\qquad
 \nu_\chi=\frac{1}{|\K|}\sum_{g\in\K}\chi(g^2)
 \in\{-1,0,1\}.\] Our main result is the following.

<!--block:B0009-->
\[thm:main\] For every finite group \(\K\), the flat-connection SFT \(X_{\K}\) satisfies \[\begin{aligned}
 O_{\K}(m)
  :=|\Fix_{L_m}(X_{\K})|
  &=|\K|^{4m}\sum_{\chi\in\Irr(\K)}d_\chi^{-2m},
  &&m\geq1,
 \label{eq:intro-orientable}\\
 N_{\K}(n)
  :=|\Fix_{H_n}(X_{\K})|
  &=|\K|^{2n}\sum_{\chi\in\Irr(\K)}
       \nu_\chi^{n+2}d_\chi^{-n},
  &&n\geq1.
 \label{eq:intro-nonorientable}\end{aligned}\] The joint sequences \((O_{\K}(m))_{m\geq1}\) and \((N_{\K}(n))_{n\geq1}\) determine \(|\K|\) and the multiset \[\bigl\{(d_\chi,\nu_\chi):\chi\in\Irr(\K)\bigr\}.\] Conversely, these character-theoretic data determine both sequences.

<!--block:B0010-->
The proof has two independent layers. A spanning-tree gauge argument first gives, for every finite-index \(H\), \[|\Fix_H(X_{\K})|
 =|\K|^{[\LambdaSurf:H]-1}|\Hom(H,\K)|.
 \label{eq:intro-gauge}\] The topology of the two covers and the classical surface formulas then give [\[eq:intro-orientable\]](#eq:intro-orientable)–[\[eq:intro-nonorientable\]](#eq:intro-nonorientable). The inverse step is a finite exponential-moment problem. The orientable moments recover all degree multiplicities. Even nonorientable moments retain precisely the self-dual irreducibles. Odd nonorientable moments first recover the difference between the \(+1\) and \(-1\) indicator multiplicities divided by the already recovered degree; multiplying by that known degree gives the signed multiplicity difference at each degree.

<!--block:B0011-->
The orientation sensitivity is visible in a small control pair.

<!--block:B0012-->
\[cor:d8q8-intro\] Let \(D_8\) be the order-eight dihedral group and let \(Q_8\) be the quaternion group. Then \[O_{D_8}(m)=O_{Q_8}(m)
 =8^{4m}\bigl(4+2^{-2m}\bigr)\] for every \(m\geq1\), while \[\begin{aligned}
 N_{D_8}(n)&=8^{2n}\bigl(4+2^{-n}\bigr),\\
 N_{Q_8}(n)&=8^{2n}\bigl(4+(-1)^n2^{-n}\bigr).
 \end{aligned}\] Thus the nonorientable spectra agree for even \(n\) and differ for odd \(n\).

<!--block:B0013-->
The argument does not classify finite groups. Different groups may have the same order and the same multiset of degree–indicator pairs; the theorem says exactly that the selected periodic spectra recover this signature, no more. It is also distinct from a finite-Heisenberg modular-nullity calculation: the present system is nonabelian and surface-topological, its counts are flat connections, and its inverse engine is complex-character moment inversion. We return to these scope boundaries in [7](#sec:scope).

<!--block:B0014-->
The paper is organized as follows. fixes conventions and records the classical surface formulas. constructs the SFT and proves [\[eq:intro-gauge\]](#eq:intro-gauge). identifies the two covers and derives the fixed spectra. proves the inverse theorem. treats \(D_8\) and \(Q_8\), and [7](#sec:scope) records the control and ownership boundaries.

<!--block:B0015-->
# Conventions and surface formulas

<!--block:B0016-->
## The surface complex and its covers

<!--block:B0017-->
Let \(N_3\) be represented by the standard one-vertex CW complex with three oriented \(1\)-cells \(x_1,x_2,x_3\) and one \(2\)-cell attached along \(x_1^2x_2^2x_3^2\). Its fundamental group is [\[eq:surface-presentation\]](#eq:surface-presentation). The universal cover \(\widetilde N_3\) has vertices indexed by \(\LambdaSurf\), with the positive \(x_i\)-edge starting at \(g\) and ending at \(gx_i\).

<!--block:B0018-->
For a subgroup \(H\leq\LambdaSurf\), we use left cosets. The corresponding cover \(H\backslash\widetilde N_3\) has vertex set \(H\backslash\LambdaSurf\) and an \(x_i\)-edge \[Hg\longrightarrow Hgx_i.\] If \(H\) has finite index \(V\), the lifted CW structure has \(V\) vertices, \(3V\) edges, and \(V\) faces. In particular, its Euler characteristic is \(-V\).

<!--block:B0019-->
The orientation character is the epimorphism \(\omega\colon\LambdaSurf\to\ZZ/2\ZZ\) in [\[eq:f-and-omega\]](#eq:f-and-omega). A connected cover associated with \(H\) is orientable if and only if \(H\leq\ker\omega\). This criterion will be important because it is the same finite-type shift, rather than two different systems, that is probed in both topological directions.

<!--block:B0020-->
## Shift convention

<!--block:B0021-->
For a finite alphabet \(A\), the left shift of \(\LambdaSurf\) on \(A^{\LambdaSurf}\) is \[(h\cdot z)(g)=z(h^{-1}g).\] Therefore \(z\) is fixed by \(H\) exactly when it is constant on every left coset \(Hg\). This convention matches the quotient cellulation above. For a \(\LambdaSurf\)-subshift \(X\), write \[\Fix_H(X)=\{z\in X:h\cdot z=z\text{ for all }h\in H\}.\]

<!--block:B0022-->
## Characters and Frobenius–Schur indicators

<!--block:B0023-->
Let \(\K\) be a finite group and \(\Irr(\K)\) its irreducible complex characters. For \(\chi\in\Irr(\K)\), set \[d_\chi=\chi(1),\qquad
 \nu_\chi=\frac1{|\K|}\sum_{g\in\K}\chi(g^2).
 \label{eq:fs-definition}\] The indicator \(\nu_\chi\) is \(+1\) for an irreducible admitting a nonzero invariant symmetric bilinear form, \(-1\) for an invariant skew-symmetric form, and \(0\) for a non-self-dual irreducible. In particular, \(\nu_\chi\in\{-1,0,1\}\). As our chosen modern normalization source, we use Klug’s account . Snyder’s lattice-TQFT argument gives a separate topological and combinatorial derivation of both formulas \[@Snyder2007\]. Historical ownership remains with Mednykh and Frobenius–Schur.

<!--block:B0024-->
\[prop:surface-hom\] Let \(\Sigma_g\) be the closed orientable surface of genus \(g\) and \(N_\ell\) the closed nonorientable surface of genus \(\ell\). Then \[\begin{aligned}
<!--block:B0025-->
 |\Hom(\pi_1(\Sigma_g),\K)|
<!--block:B0026-->
 &=|\K|^{2g-1}\sum_{\chi\in\Irr(\K)}d_\chi^{2-2g},
 \label{eq:orientable-hom}\\
<!--block:B0027-->
 |\Hom(\pi_1(N_\ell),\K)|
<!--block:B0028-->
 &=|\K|^{\ell-1}\sum_{\chi\in\Irr(\K)}
      \nu_\chi^{\ell}d_\chi^{2-\ell}.
 \label{eq:nonorientable-hom}\end{aligned}\]

<!--block:B0029-->
For completeness, the exponents can be read directly from the usual presentations. The orientable relation is a product of \(g\) commutators; the nonorientable relation is a product of \(\ell\) squares. Convolution of the corresponding class functions diagonalizes in irreducible characters, giving [\[eq:orientable-hom\]](#eq:orientable-hom) and [\[eq:nonorientable-hom\]](#eq:nonorientable-hom). We do not reprove this character calculation, and we make no new claim about it.

<!--block:B0030-->
The factors \(\nu_\chi^\ell\) explain the orientation effect. On orientable surfaces, only the degree survives. On nonorientable surfaces, a non-self-dual character contributes zero, whereas an orthogonal or symplectic character contributes with sign determined by the parity of \(\ell\).

<!--block:B0031-->
# The flat-connection subshift

<!--block:B0032-->
## A local holonomy rule

<!--block:B0033-->
Fix a finite group \(\K\). A point \(A\in(\K^3)^{\LambdaSurf}\) is written \[A(g)=(A_1(g),A_2(g),A_3(g)).\] Interpret \(A_i(g)\) as the parallel transport on the positive oriented edge \(g\to gx_i\); the reverse edge has transport \(A_i(g)^{-1}\). Starting at \(g\), the lift of \(x_1^2x_2^2x_3^2\) traverses six positive edges. Define its holonomy by \[\begin{aligned}
 \mathcal H_A(g)={}&A_1(g)A_1(gx_1)
 A_2(gx_1^2)A_2(gx_1^2x_2)\notag\\
 &\quad\cdot A_3(gx_1^2x_2^2)
 A_3(gx_1^2x_2^2x_3).
 \label{eq:local-holonomy}\end{aligned}\]

<!--block:B0034-->
\[def:flat-shift\] The *\(\K\)-flat surface shift* is \[X_{\K}=\{A\in(\K^3)^{\LambdaSurf}:
              \mathcal H_A(g)=\eK\text{ for every }g\in\LambdaSurf\}.\]

<!--block:B0035-->
\[prop:sft\] \(X_{\K}\) is a \(\LambdaSurf\)-subshift of finite type.

<!--block:B0036-->
The condition at the identity reads only the coordinates in the fixed finite set \[\{1,x_1,x_1^2,x_1^2x_2,x_1^2x_2^2,
   x_1^2x_2^2x_3\}.\] There are finitely many forbidden patterns on this set, namely those for which the ordered product in [\[eq:local-holonomy\]](#eq:local-holonomy) is not \(\eK\). Its translates are exactly the conditions at all \(g\). The resulting set is closed and shift invariant, and it is defined by this finite forbidden list.

<!--block:B0037-->
## Fixed configurations as flat connections

<!--block:B0038-->
Let \(H\leq\LambdaSurf\) have finite index \(V\). By the left-shift convention, an \(H\)-fixed \(A\) descends to one label on each positively oriented edge of \(H\backslash\widetilde N_3\). Equation [\[eq:local-holonomy\]](#eq:local-holonomy) says precisely that every lifted face has trivial holonomy. Thus \(\Fix_H(X_{\K})\) is the set of flat \(\K\)-connections on this finite cellulation.

<!--block:B0039-->
We count these connections without quotienting by gauge. If \(u\colon H\backslash\LambdaSurf\to\K\) is a vertex gauge, use the convention \[(u\cdot A)(v\to w)=u(v)A(v\to w)u(w)^{-1}.
 \label{eq:gauge-action}\] Face holonomy is conjugated by the value of \(u\) at its initial vertex, so flatness is preserved.

<!--block:B0040-->
\[prop:gauge-count\] For every finite-index subgroup \(H\leq\LambdaSurf\), \[|\Fix_H(X_{\K})|
 =|\K|^{[\LambdaSurf:H]-1}|\Hom(H,\K)|.
 \label{eq:gauge-count}\]

<!--block:B0041-->
Write \(Y=H\backslash\widetilde N_3\) and choose a root vertex \(v_0\) and a spanning tree \(T\) in its \(1\)-skeleton. A based gauge is a vertex map \(u\) with \(u(v_0)=\eK\). There are \(|\K|^{V-1}\) based gauges, where \(V=[\LambdaSurf:H]\).

<!--block:B0042-->
The based gauge action on edge labellings is free. Indeed, if \(u\cdot A=A\), then along an oriented tree edge \(v\to w\), \[u(w)=A(v\to w)^{-1}u(v)A(v\to w).\] Starting from \(u(v_0)=\eK\) and moving along the unique tree paths gives \(u(v)=\eK\) at every vertex.

<!--block:B0043-->
Every connection has a unique based gauge transform whose labels on all tree edges are \(\eK\). Existence follows recursively: once \(u(v)\) is fixed and \(v\to w\) is the next outward tree edge, set \(u(w)=u(v)A(v\to w)\). With the convention [\[eq:gauge-action\]](#eq:gauge-action), the transformed edge label is the identity. Uniqueness follows by the same tree recursion.

<!--block:B0044-->
It remains to identify the tree-trivial flat connections. For such a connection, multiply edge labels along a based cellular loop, using inverses on reversed edges. Flatness makes this holonomy invariant under insertion or deletion of a lifted face boundary, and tree triviality fixes the chosen based representatives. Consequently holonomy defines a homomorphism \[\pi_1(Y,v_0)\cong H\longrightarrow\K.\] Conversely, collapse \(T\) to the root. A homomorphism \(H\to\K\) assigns labels to the remaining oriented \(1\)-cells, and the relators given by the \(2\)-cells are sent to \(\eK\); expanding the tree with identity labels gives a tree-trivial flat connection. The two constructions are inverse.

<!--block:B0045-->
Hence the set of flat connections is the Cartesian product of the \(|\K|^{V-1}\) based gauges with \(\Hom(H,\K)\), proving [\[eq:gauge-count\]](#eq:gauge-count).

<!--block:B0046-->
\[rem:unbased-gauge\] The based condition is essential for this clean count. The full gauge group can have stabilizers governed by centralizers of holonomy images. No orbit count is taken here: \(X_{\K}\) contains raw edge labellings, so [\[eq:gauge-count\]](#eq:gauge-count) is the required cardinality.

<!--block:B0047-->
# Two explicit cover families and their spectra

<!--block:B0048-->
The relation \(x_1^2x_2^2x_3^2\) has \(f\)-value \(2-2+0=0\), so the first line of [\[eq:f-and-omega\]](#eq:f-and-omega) defines a homomorphism \(f\colon\LambdaSurf\to\ZZ\). It is onto because \(f(x_1)=1\). The resulting families are directed by divisibility: if \(a\mid b\), then \(H_b\leq H_a\) and \(L_b\leq L_a\). We retain all positive moduli because both parities of the nonorientable genus carry information.

<!--block:B0049-->
\[lem:family-topology\] For every \(n,m\geq1\):

<!--block:B0050-->
1.  \([\LambdaSurf:H_n]=n\), and \(H_n\) is the fundamental group of a closed nonorientable surface of genus \(n+2\);

2.  \([\LambdaSurf:L_m]=2m\), and \(L_m\) is the fundamental group of a closed orientable surface of genus \(m+1\).

<!--block:B0051-->
The reduction of \(f\) modulo \(n\) is onto, so \(H_n\) has index \(n\). Moreover, \(x_3\in H_n\) and \(\omega(x_3)=1\). Thus \(H_n\) is not contained in the orientation kernel, and the corresponding cover is nonorientable. Euler characteristic multiplies under a finite cover, so its Euler characteristic is \[n\chi(N_3)=-n.\] If its nonorientable genus is \(\ell\), then \(2-\ell=-n\), hence \(\ell=n+2\).

<!--block:B0052-->
Let \(\LambdaSurf^+=\ker\omega\). It has index two and is the fundamental group of the orientation double cover. Since \(2\chi(N_3)=-2=2-2\cdot2\), that cover is \(\Sigma_2\). The restriction \(f|_{\LambdaSurf^+}\) is onto: the element \(x_1x_3^{-1}\) has even orientation parity and \(f\)-value \(1\). Consequently \(L_m\) has index \(m\) in \(\LambdaSurf^+\) and index \(2m\) in \(\LambdaSurf\). It lies inside the orientation kernel, so its cover is orientable. Its Euler characteristic is \(-2m\); writing this as \(2-2g\) gives \(g=m+1\).

<!--block:B0053-->
The same integer-valued homomorphism therefore yields both families; only its domain changes. This prevents the orientation comparison from being hidden in unrelated quotient choices.

<!--block:B0054-->
\[thm:fixed-laws\] For every finite group \(\K\) and every \(m,n\geq1\), \[\begin{aligned}
<!--block:B0055-->
 |\Fix_{L_m}(X_{\K})|
<!--block:B0056-->
 &=|\K|^{4m}\sum_{\chi\in\Irr(\K)}d_\chi^{-2m},
 \label{eq:orientable-spectrum}\\
<!--block:B0057-->
 |\Fix_{H_n}(X_{\K})|
<!--block:B0058-->
 &=|\K|^{2n}\sum_{\chi\in\Irr(\K)}
       \nu_\chi^{n+2}d_\chi^{-n}.
 \label{eq:nonorientable-spectrum}\end{aligned}\]

<!--block:B0059-->
For \(L_m\), [\[lem:family-topology\]](#lem:family-topology) gives index \(V=2m\) and orientable genus \(g=m+1\). The gauge factor in [\[eq:gauge-count\]](#eq:gauge-count) is \(|\K|^{2m-1}\), while [\[eq:orientable-hom\]](#eq:orientable-hom) gives \[|\Hom(L_m,\K)|
 =|\K|^{2m+1}\sum_{\chi\in\Irr(\K)}d_\chi^{-2m}.\] Multiplication gives [\[eq:orientable-spectrum\]](#eq:orientable-spectrum).

<!--block:B0060-->
For \(H_n\), the index is \(V=n\) and the nonorientable genus is \(\ell=n+2\). The gauge factor is \(|\K|^{n-1}\), and [\[eq:nonorientable-hom\]](#eq:nonorientable-hom) becomes \[|\Hom(H_n,\K)|
 =|\K|^{n+1}\sum_{\chi\in\Irr(\K)}
       \nu_\chi^{n+2}d_\chi^{-n}.\] This proves [\[eq:nonorientable-spectrum\]](#eq:nonorientable-spectrum).

<!--block:B0061-->
@l l l l Y@ Family & Index & Cover & Genus & Normalized moment  
\(H_n\) & \(n\) & nonorientable & \(n+2\) & \(N_{\K}(n)/|\K|^{2n}=\sum_\chi\nu_\chi^{n+2}d_\chi^{-n}\)  
\(L_m\) & \(2m\) & orientable & \(m+1\) & \(O_{\K}(m)/|\K|^{4m}=\sum_\chi d_\chi^{-2m}\)  

<!--block:B0062-->
Two features of [\[tab:families\]](#tab:families) will drive the inverse theorem. First, every irreducible contributes positively to the orientable moment. Second, the nonorientable parity separates self-duality from its sign: even \(n\) replaces every nonzero indicator by \(1\), while odd \(n\) retains the sign.

<!--block:B0063-->
# Finite moment inversion and recovery

<!--block:B0064-->
We isolate the elementary inverse principle used below. It is stated over \(\CC\), although all applications have positive rational bases.

<!--block:B0065-->
\[lem:finite-moments\] Let \(z_1,\ldots,z_r\) be distinct nonzero complex numbers and \[u_m=\sum_{i=1}^r a_i z_i^m\qquad(m\geq1),\] where \(a_i\neq0\). The sequence \((u_m)_{m\geq1}\) determines the unordered collection \(\{(z_i,a_i):1\leq i\leq r\}\). If the bases \(z_i\) are already known and \(u_m=\sum_i a_i z_i^m\) is available at any \(r\) consecutive nonnegative indices \(m=m_0,\ldots,m_0+r-1\), then those moments determine all coefficients, allowing \(m_0=0\) and allowing some coefficients to be zero.

<!--block:B0066-->
As a formal power series at the origin, \[\sum_{m\geq1}u_m t^{m-1}
 =\sum_{i=1}^r\frac{a_i z_i}{1-z_i t}.
 \label{eq:moment-generating}\] The reduced rational function on the right has simple poles \(z_i^{-1}\). Their positions recover the bases, and their residues recover the coefficients. Hence equality of all moments forces equality of the unordered collections.

<!--block:B0067-->
When the bases are known, moments with nonnegative indices \(m_0,\ldots,m_0+r-1\) give a linear system with matrix \((z_i^{m_0+j})_{0\leq j<r,1\leq i\leq r}\). Its determinant is a nonzero monomial times the Vandermonde product \(\prod_{i<j}(z_j-z_i)\), so all coefficients are uniquely determined.

<!--block:B0068-->
For each degree \(d\) occurring in \(\Irr(\K)\), introduce the multiplicities \[\begin{aligned}
 c_d^+&=\#\{\chi:d_\chi=d,\ \nu_\chi=+1\},\\
 c_d^-&=\#\{\chi:d_\chi=d,\ \nu_\chi=-1\},\\
 c_d^0&=\#\{\chi:d_\chi=d,\ \nu_\chi=0\},\\
 t_d&=c_d^++c_d^-+c_d^0.\end{aligned}\]

<!--block:B0069-->
\[thm:reconstruction\] The joint sequences \[(O_{\K}(m))_{m\geq1},\qquad (N_{\K}(n))_{n\geq1}\] determine \(|\K|\) and every multiplicity \(c_d^+,c_d^-,c_d^0\). Equivalently, they determine the multiset \(\{(d_\chi,\nu_\chi):\chi\in\Irr(\K)\}\).

<!--block:B0070-->
We proceed in four steps.

<!--block:B0071-->
*Step 1: the group order.* By [\[eq:orientable-spectrum\]](#eq:orientable-spectrum), \[O_{\K}(m)^{1/(4m)}
 =|\K|\left(\sum_{\chi\in\Irr(\K)}d_\chi^{-2m}\right)^{1/(4m)}.\] There is at least one degree-one character, namely the trivial character. The sum in parentheses is bounded below by \(1\) and above by \(|\Irr(\K)|\), independently of \(m\). Therefore \[|\K|=\lim_{m\to\infty}O_{\K}(m)^{1/(4m)}.
 \label{eq:recover-order}\]

<!--block:B0072-->
*Step 2: all degree multiplicities.* After recovering \(|\K|\), normalize the orientable moments as \[P_m=\frac{O_{\K}(m)}{|\K|^{4m}}
     =\sum_d t_d(d^{-2})^m.
 \label{eq:P-moments}\] Inverse-degree sums \(\sum_{\chi}\chi(1)^{-t}\) are standard character-degree zeta values; see, for example, Liebeck and Shalev \[@LiebeckShalev2005\]. We use this standard finite-group expression at positive even integers, not a new zeta function. Distinct degrees give distinct nonzero bases \(d^{-2}\), and every coefficient \(t_d\) is positive. By [\[lem:finite-moments\]](#lem:finite-moments), \((P_m)\) recovers the bases and coefficients, hence every occurring degree \(d\) and its total multiplicity \(t_d\).

<!--block:B0073-->
*Step 3: the self-dual multiplicities.* At even nonorientable indices, indicator-zero characters vanish and both nonzero indicators have even power. Thus \[Q_m=\frac{N_{\K}(2m)}{|\K|^{4m}}
 =\sum_d(c_d^++c_d^-)(d^{-2})^m,
 \qquad m\geq1.
 \label{eq:Q-moments}\] The bases are already known from [\[eq:P-moments\]](#eq:P-moments). The Vandermonde part of [\[lem:finite-moments\]](#lem:finite-moments), with zero coefficients allowed, recovers \[s_d:=c_d^++c_d^-\] for every occurring \(d\).

<!--block:B0074-->
*Step 4: the indicator signs.* At odd index \(n=2m+1\), where \(m\geq0\), \[\begin{aligned}
 R_m&=\frac{N_{\K}(2m+1)}{|\K|^{4m+2}}\notag\\
 &=\sum_d(c_d^+-c_d^-)d^{-(2m+1)}
  =\sum_d\frac{c_d^+-c_d^-}{d}(d^{-2})^m.
 \label{eq:R-moments}\end{aligned}\] Again the bases are known. If \(r\) distinct degrees occur, the known-base clause of [\[lem:finite-moments\]](#lem:finite-moments), now with \(m_0=0\), shows that \(R_0,\ldots,R_{r-1}\) recover the coefficients \[b_d:=\frac{c_d^+-c_d^-}{d}.\] Since each degree \(d\) is already known from [\[eq:P-moments\]](#eq:P-moments), multiplying by \(d\) gives \(\delta_d:=d b_d=c_d^+-c_d^-\) for every degree. Finally, \[c_d^+=\frac{s_d+\delta_d}{2},\qquad
 c_d^-=\frac{s_d-\delta_d}{2},\qquad
 c_d^0=t_d-s_d.
 \label{eq:multiplicity-recovery}\] This reconstructs the claimed multiset.

<!--block:B0075-->
\[cor:spectral-equivalence\] For finite groups \(\K\) and \(\K'\), the two identities \[O_{\K}(m)=O_{\K'}(m)\quad(m\geq1),\qquad
 N_{\K}(n)=N_{\K'}(n)\quad(n\geq1)\] hold if and only if \[|\K|=|\K'|
 \quad\text{and}\quad
 \{(d_\chi,\nu_\chi):\chi\in\Irr(\K)\}
 =\{(d_\psi,\nu_\psi):\psi\in\Irr(\K')\}\] as multisets.

<!--block:B0076-->
The forward implication is [\[thm:reconstruction\]](#thm:reconstruction). For the reverse implication, substitute the common order and pair multiset into [\[eq:orientable-spectrum\]](#eq:orientable-spectrum) and [\[eq:nonorientable-spectrum\]](#eq:nonorientable-spectrum).

<!--block:B0077-->
\[rem:finite-recovery\] Once \(|\K|\) is known and there are \(r\) distinct degrees, the remaining reconstruction is finite. The rational function [\[eq:moment-generating\]](#eq:moment-generating) for \((P_m)\) has denominator degree \(r\); standard finite recurrence recovery determines it from finitely many exact moments. After its \(r\) bases are known, \(r\) even nonorientable moments and \(r\) odd nonorientable moments solve two Vandermonde systems. The infinite sequences in [\[thm:reconstruction\]](#thm:reconstruction) are used to state the invariant without assuming \(r\) or \(|\K|\) in advance.

<!--block:B0078-->
The parity split is essential. The orientable moments alone cannot distinguish characters of equal degree with different indicators. The even nonorientable moments detect self-duality but cannot distinguish \(+1\) from \(-1\). The odd nonorientable moments supply exactly the missing signed data.

<!--block:B0079-->
# The dihedral–quaternion separation

<!--block:B0080-->
Let \[D_8=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle\] and let \(Q_8=\{\pm1,\pm i,\pm j,\pm k\}\). Both groups have four one-dimensional irreducible characters and one two-dimensional irreducible character. Hence both have degree multiset \[\{1,1,1,1,2\}.\] Every one-dimensional character of either group is real and has indicator \(+1\).

<!--block:B0081-->
The two-dimensional indicators have opposite signs. This can be checked directly from [\[eq:fs-definition\]](#eq:fs-definition). For the standard two-dimensional character \(\chi_D\) of \(D_8\), \[\chi_D(1)=2,\quad \chi_D(r^2)=-2,
 \quad \chi_D(g)=0\ \text{otherwise}.\] The squares of \(1,r^2\) and the four reflections are \(1\), while \(r\) and \(r^3\) square to \(r^2\). Therefore \[\sum_{g\in D_8}\chi_D(g^2)=8,
 \qquad \nu_{\chi_D}=1.\] For the faithful two-dimensional character \(\chi_Q\) of \(Q_8\), \[\chi_Q(1)=2,\quad \chi_Q(-1)=-2,
 \quad \chi_Q(\pm i)=\chi_Q(\pm j)=\chi_Q(\pm k)=0.\] The elements \(\pm1\) square to \(1\), and the other six elements square to \(-1\). Hence \[\sum_{g\in Q_8}\chi_Q(g^2)=2\cdot2+6\cdot(-2)=-8,
 \qquad \nu_{\chi_Q}=-1.\]

<!--block:B0082-->
Substitution in [\[thm:fixed-laws\]](#thm:fixed-laws) proves \[\begin{aligned}
 O_{D_8}(m)=O_{Q_8}(m)
 &=8^{4m}\bigl(4+2^{-2m}\bigr),
 \label{eq:d8q8-O}\\
 N_{D_8}(n)&=8^{2n}\bigl(4+2^{-n}\bigr),
 \label{eq:d8-N}\\
 N_{Q_8}(n)&=8^{2n}\bigl(4+(-1)^n2^{-n}\bigr).
 \label{eq:q8-N}\end{aligned}\]


<!--block:B0083-->
| Group   |   \((d,\nu)\) signature    | \(O(1)\)  | \(N(1)\) | \(N(2)\)  |
| :------ | :------------------------: | :-------: | :------: | :-------: |
| \(D_8\) | \(4\times(1,+1),\ (2,+1)\) | \(17408\) | \(288\)  | \(17408\) |
| \(Q_8\) | \(4\times(1,+1),\ (2,-1)\) | \(17408\) | \(224\)  | \(17408\) |

<!--block:B0084-->
Orientation-sensitive periodic data for \(D_8\) and \(Q_8\). The orientable family cannot see the sign of the unique two-dimensional indicator; the odd nonorientable levels can.


<!--block:B0085-->
At even \(n\), the exponent \(n+2\) is even and the sign disappears. At odd \(n\), the two-dimensional contributions differ by \[2\cdot8^{2n}2^{-n}=2^{5n+1},\] so separation holds at every odd level, not only at the first one. This example also shows why the orientable and nonorientable families must be used jointly in [\[thm:reconstruction\]](#thm:reconstruction).

<!--block:B0086-->
# Scope, ownership, and finite controls

<!--block:B0087-->
## What is and is not being recovered

<!--block:B0088-->
The output of [\[thm:reconstruction\]](#thm:reconstruction) is the order of \(\K\) and the multiset of pairs \((d_\chi,\nu_\chi)\). The theorem does not assert that this signature determines the multiplication table of \(\K\), its full character table, or its isomorphism class. Likewise, [\[cor:spectral-equivalence\]](#cor:spectral-equivalence) is an exact classification of the two selected periodic sequences, not a classification of finite groups.

<!--block:B0089-->
The classical input must also be kept separate from the residual result. Equations [\[eq:orientable-hom\]](#eq:orientable-hom) and [\[eq:nonorientable-hom\]](#eq:nonorientable-hom) are the Mednykh and Frobenius–Schur formulas, respectively. Klug’s account \[@Klug2025\] is our chosen modern normalization source, not a reassignment of historical ownership. Snyder’s lattice-TQFT proof \[@Snyder2007\] already supplies a topological/combinatorial surface-state-sum route to both formulas. Likewise, the inverse-degree sums used here belong to the standard character-degree zeta-function setting \[@LiebeckShalev2005\], and the Vandermonde inversion is elementary. The residual proof sequence in this manuscript begins with the finite-type flat model and rooted gauge identity, specializes the owned formulas to the two explicit families, and inverts their joint output. No priority claim is made for this combination.

<!--block:B0090-->
Periodic-data recovery also has a prior symbolic-dynamics line. Ward and Roettger use periodic points to recover the finite abelian parameter of a Ledrappier-type algebraic \(\ZZ^2\) Markov shift \[@Ward1998; @Roettger2005\]. Their acting group, configuration law, and recovered invariant differ from the surface-group and Frobenius–Schur setting here, so they are conceptual nearest neighbors rather than a collision with [\[thm:reconstruction\]](#thm:reconstruction). This distinction does not turn the bounded search for the present combination into a priority certificate.

<!--block:B0091-->
## Separation from the finite-Heisenberg nullity engine

<!--block:B0092-->
This paper’s moment argument and the finite-Heisenberg modular-nullity engine used in the neighboring P70 project address different systems and invariants. The distinctions are structural:

<!--block:B0093-->
@lYY@ Feature & Present paper (P69) & Finite-Heisenberg project (P70)  
Acting group & nonorientable surface group \(\pi_1(N_3)\) & discrete Heisenberg group  
Alphabet/model & nonabelian finite-group edge labels with flat holonomy & additive finite-field principal linear kernel  
Finite-index datum & number of flat connections on surface covers & nullity on finite Heisenberg quotients  
Representation input & complex character degrees and FS indicators & modular Maschke/Schrödinger blocks  
Inverse engine & finite exponential moments and Vandermonde inversion & blockwise linear algebra and modular rank jumps  

<!--block:B0094-->
Thus neither the characteristic-three phenomenon nor the modular-nullity calculation of P70 is reused here. The two projects share only the broad practice of probing a group shift by finite-index fixed data.

<!--block:B0095-->
## Exact finite regression controls

<!--block:B0096-->
The script `verify_surface_flat_sft.py` implements the groups \(D_8\), \(Q_8\), and \(C_3\) from their multiplication laws and performs the following checks using exact integers and rational arithmetic:

<!--block:B0097-->
1.  it checks identity, inverses, and associativity;

2.  it enumerates the distribution of one commutator and convolves it to count homomorphisms from orientable surface groups;

3.  it enumerates the distribution of one square and convolves it to count homomorphisms from nonorientable surface groups;

4.  it multiplies by the rooted gauge factors and compares with [\[eq:d8q8-O\]](#eq:d8q8-O)–[\[eq:q8-N\]](#eq:q8-N) for \(m=1,\ldots,4\) and \(n=1,\ldots,5\);

5.  for \(C_3\), it derives the exact one-dimensional indicator signature \((1,0,0)\), checks both surface formulas, and reconstructs all three multiplicities \((c_1^+,c_1^-,c_1^0)=(1,0,2)\) from normalized moments;

6.  it checks the orientable surface formula for \(S_3\) at genera one through three as a separate non-order-eight control.

<!--block:B0098-->
For the \(C_3\) control, the degree multiset is \(\{1,1,1\}\), while only the trivial character is self-dual. Hence the two non-real characters disappear from every nonorientable moment, and the predicted fixed counts reduce to \[O_{C_3}(m)=3^{4m+1},\qquad N_{C_3}(n)=3^{2n}.
 \label{eq:c3-controls}\] The direct commutator and square-product enumerations agree with [\[eq:c3-controls\]](#eq:c3-controls). Their normalized moments are \(P_m=3\), \(Q_m=1\), and \(R_m=1\), which recover \(t_1=3\), \(s_1=1\), \(\delta_1=1\), and therefore the stated \((+,-,0)\) multiplicities. This is an exact exercise of the \(\nu=0\) branch, not numerical approximation.

<!--block:B0099-->
The stored run ends in `ALL CHECKS PASS`. This finite enumeration can detect normalization or parity regressions. It cannot prove the gauge bijection, the all-genus character formulas, or the infinite moment inversion; those statements rest on the proofs above.

<!--block:B0100-->
## Release posture

<!--block:B0101-->
The package is an anonymous internal Stage-2 draft. A bounded search did not locate an exact collision involving this flat SFT, these two explicit families, and the same joint reconstruction. That negative search is not a priority result. Specialist review of the symbolic-dynamics, surface-topology, and finite-group literature remains mandatory before any external release.

<!--block:B0102-->
# Conclusion

<!--block:B0103-->
The flat-connection SFT converts finite-index fixed points into raw flat connections on finite surface covers. Rooted gauge fixing separates this count into an elementary power of \(|\K|\) and a surface-group homomorphism count. The two explicit cyclic-cover families then expose complementary character moments: orientable covers see degrees, while nonorientable covers see self-duality and its Frobenius–Schur sign. Their joint Vandermonde inversion proves the recovery theorem, and the order-eight \(D_8/Q_8\) pair makes the orientation effect exact in a small explicit example.

<!--block:B0104-->
Several boundaries are deliberate. The recovered signature is not a group classification invariant, the classical surface formulas remain fully credited inputs, and the argument does not use modular nullity or finite-Heisenberg block theory. Within those boundaries, the result gives a concrete mechanism by which the topology of subgroup covers enriches the periodic spectrum of one finite-type group action.

<!--block:B0105-->
# Declarations

<!--block:B0106-->
#### Data and code availability.

<!--block:B0107-->
No external dataset is used. The source package includes an exact finite regression script and its frozen output. Numerical enumeration is not a proof premise.

<!--block:B0108-->
#### Author contributions.

<!--block:B0109-->
The manuscript is an anonymous internal draft. Authorship and contribution statements must be supplied by the responsible researchers before release.

<!--block:B0110-->
#### Funding and competing interests.

<!--block:B0111-->
No funding or competing-interest statement has been supplied for this internal draft. Both declarations require author confirmation before release.

<!--block:B0112-->
#### Ethics.

<!--block:B0113-->
The work is purely mathematical and uses no human participants, animals, or personal data.

<!--block:B0114-->
#### AI-use disclosure.

<!--block:B0115-->
AI-assisted tools were used in the internal drafting, algebraic checking, and compilation workflow. Every theorem, proof, computation, citation, and priority-sensitive statement requires verification and approval by the human authors before any external dissemination.
