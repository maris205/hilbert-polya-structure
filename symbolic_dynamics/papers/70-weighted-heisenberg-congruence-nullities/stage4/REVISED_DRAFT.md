<!--block:B0001-->
# Introduction

<!--block:B0002-->
Periodic configurations convert an infinite symbolic constraint into a finite linear problem. For shifts over an abelian lattice, Fourier characters then diagonalize convolution, and nullity becomes a count of torsion points on the zero set of the symbol. This positive-characteristic viewpoint is developed systematically by \[@Zaidenberg2008\]. The discrete Heisenberg group is a basic nonabelian nilpotent setting in which that character calculation is incomplete: most of the finite regular representation lies in nonlinear blocks.

<!--block:B0003-->
For unit coefficients, the character resultant is Wendt’s determinant, whose relation to finite-field points on Fermat curves is classical \[@FordJha1993\]. We therefore do not present the cyclotomic gcd itself as a new number-theoretic invariant. Its role is to isolate the abelian stratum before the nonlinear Heisenberg jump is restored.

<!--block:B0004-->
We study the finite-field group shift defined by the weighted rule \[\label{eq:local-rule-intro}
 \alpha x_g+\beta x_{ga}+\gamma x_{gb}=0.\] The underlying Heisenberg principal-action framework is established. In particular, \[@GollSchmidtVerbitskiy2014\] develop expansiveness and homoclinic methods for principal actions, and the survey of \[@LindSchmidt2015\] treats the exact integer element \(1+a+b\) as a mixing example. Our object is its zero-dimensional coefficient reduction, not a claim that the group, action framework, or three-term element is new. The question here is narrower and arithmetic: what is the exact kernel dimension after imposing a prime congruence period?

<!--block:B0005-->
Finite-Heisenberg convolution itself also has a direct computational literature. Deundyak and Leonov define left and right convolution on finite Heisenberg groups, construct the corresponding noncommutative Fourier transform, and solve convolution equations through the irreducible blocks \[@DeundyakLeonov2016\]. That algorithmic framework and its representation ledger are prior. It does not calculate the cross-characteristic singular kernel dimensions of the weighted family in [\[eq:local-rule-intro\]](#eq:local-rule-intro).

<!--block:B0006-->
The answer has two qualitatively different pieces. The one-dimensional representations behave as in abelian harmonic analysis and contribute a polynomial gcd degree. The degree-\(\ell\) representations see the clock–shift matrix \[\alpha I+\beta U+\gamma V.\] Its determinant is independent of the nontrivial central character and equals \(\alpha^\ell+\beta^\ell+\gamma^\ell\). Thus all nonlinear types become singular together. Each singular block has nullity one, but its regular multiplicity is \(\ell\); summing over the \(\ell-1\) nontrivial central characters creates a jump of size \(\ell(\ell-1)\).

<!--block:B0007-->
Against the component-by-component owner comparison below, the paper makes three bounded contributions.

<!--block:B0008-->
1. For the stated cross-characteristic family, we give an exact fixed-dimension formula for every nondegenerate weight triple and every pair of distinct primes \(p,\ell\), with \(\ell\) odd.

2. We separate the character contribution from a nonlinear Fermat-locus jump and prove the latter with an exact corank-one statement, not only a determinant test.

3. As finite regression evidence, we audit right versus left convolution and verify the formula against full \(\ell^3\)-dimensional matrices in ten independent cases.

<!--block:B0009-->
Finite Heisenberg representation theory, including the Stone–von Neumann description behind the nonlinear blocks, is standard; we use the formulation of \[@GurevichHadani2010\] and the direct finite-group classification of \[@GrassbergerHormann2001\]. The progress here is the resulting symbolic fixed-space phase diagram for the weighted cross-characteristic family. No priority language is intended: the literature search supporting this internal draft is bounded.

<!--block:B0010-->
# The shift, the quotient, and the formula

<!--block:B0011-->
Write the discrete Heisenberg group in coordinates as \(\GammaH=\mathbb Z^3\) with multiplication \[\label{eq:heis-product}
 (r,s,t)(u,v,w)=(r+u,s+v,t+w+rv).\] Set \(a=(1,0,0)\), \(b=(0,1,0)\), and \(c=(0,0,1)\), so that \([a,b]=c\) and \(c\) is central. For an odd prime \(\ell\), reduction of all three coordinates modulo \(\ell\) gives \[\pi_\ell:\GammaH\longrightarrow
 \Ql:=\Heis(\Fell),
 \qquad N_\ell:=\ker\pi_\ell.\]

<!--block:B0012-->
Let \(p\ne\ell\) be prime, and fix \(\alpha,\beta,\gamma\in\Fp^\times\). On \(\Fp^{\GammaH}\) use the left shift \((h\cdot x)_g=x_{h^{-1}g}\) and define \[\label{eq:shift-definition}
 X_{p;\alpha,\beta,\gamma}
 =\{x:\alpha x_g+\beta x_{ga}+\gamma x_{gb}=0
       \text{ for every }g\in\GammaH\}.\] This is a closed shift-invariant linear group shift.

<!--block:B0013-->
An \(N_\ell\)-fixed configuration is constant on left cosets. Normality of \(N_\ell\) identifies those cosets with \(\Ql\), and [\[eq:shift-definition\]](#eq:shift-definition) becomes the right-convolution kernel \[\label{eq:finite-operator}
 (T_{\alpha,\beta,\gamma}f)(q)
  =\alpha f(q)+\beta f(qa)+\gamma f(qb),
 \qquad f\in\Fp^{\Ql}.\]

<!--block:B0014-->
Define \[\label{eq:D-definition}
 \Dcycl(\alpha,\beta,\gamma)
 :=\deg\gcd_{\Fp[t]}
 \bigl(t^\ell-1,(\alpha+\beta t)^\ell+\gamma^\ell\bigr)\] and \[\label{eq:Fermat-delta}
 \Delta_\ell(\alpha,\beta,\gamma)
 :=\alpha^\ell+\beta^\ell+\gamma^\ell\in\Fp.\]

<!--block:B0015-->
\[thm:main\] Under the assumptions above, \[\label{eq:main-formula}
 \dim_{\Fp}\Fix_{N_\ell}
 X_{p;\alpha,\beta,\gamma}
 =\Dcycl(\alpha,\beta,\gamma)
  +\ell(\ell-1)\one_{\{\Delta_\ell(\alpha,\beta,\gamma)=0\}}.\] Equivalently, the number of \(N_\ell\)-fixed configurations is \(p\) raised to the right-hand side of [\[eq:main-formula\]](#eq:main-formula).

<!--block:B0016-->
The two terms in [\[eq:main-formula\]](#eq:main-formula) are summarized in [\[tab:block-ledger\]](#tab:block-ledger). Their different scales are essential: the character term is at most \(\ell\), whereas the nonlinear term is either zero or \(\ell(\ell-1)\).

<!--block:B0017-->
@YcccY@ Stratum & Types & Degree & Multiplicity & Singular contribution  
Characters & \(\ell^2\) & \(1\) & \(1\) & \(\Dcycl(\alpha,\beta,\gamma)\)  
Nontrivial central character & \(\ell-1\) & \(\ell\) & \(\ell\) & \(\ell(\ell-1)\one_{\{\Delta_\ell=0\}}\)  

<!--block:B0018-->
# Finite Heisenberg regular decomposition

<!--block:B0019-->
Let \(k\) be an algebraic closure of \(\Fp\). We first remove a possible field splitting ambiguity.

<!--block:B0020-->
\[lem:base-change\] For a matrix \(A\) over \(\Fp\), its nullity over \(\Fp\) equals the nullity of \(A\otimes_{\Fp}k\) over \(k\).

<!--block:B0021-->
Field extension is flat, so tensoring the exact sequence \(0\to\ker A\to\Fp^n\to\Fp^m\) with \(k\) remains exact. Equivalently, the nonzero minors determining the rank remain nonzero after embedding \(\Fp\hookrightarrow k\).

<!--block:B0022-->
The complex Stone–von Neumann theorem supplies a standard model for finite Heisenberg representations \[@GurevichHadani2010\]. Grassberger and Hörmann give an elementary construction of all irreducible representations of \(H(\mathbb{Z}_n)\) \[@GrassbergerHormann2001\]; at prime \(n=\ell\), their classification owns the character/nontrivial-central-character type ledger used below. Since our splitting field has characteristic \(p\), we still record the cross-characteristic classification directly rather than silently transferring a complex representation statement.

<!--block:B0023-->
\[lem:irreducibles\] Over \(k\), the irreducibles of \(\Ql\) are the following:

<!--block:B0024-->
1.  for every \((u,v)\in\mu_\ell(k)^2\), the character \[\chi_{u,v}(a)=u,\qquad \chi_{u,v}(b)=v,\qquad \chi_{u,v}(c)=1;\]

2.  for every nontrivial \(\zeta\in\mu_\ell(k)\), one degree-\(\ell\) module \(\pi_\zeta\) on the basis \(e_0,\ldots,e_{\ell-1}\), given by \[\pi_\zeta(a)e_j=\zeta^j e_j,
     \qquad
     \pi_\zeta(b)e_j=e_{j+1\bmod\ell},
     \qquad
     \pi_\zeta(c)=\zeta I.\] The modules in this list are pairwise inequivalent and the list is complete.

<!--block:B0025-->
Because \(p\ne\ell\), the polynomial \(t^\ell-1\) has \(\ell\) distinct roots in \(k\). The characters in (1) are therefore distinct and exhaust the characters of the abelianization \(\Ql/[\Ql,\Ql]\cong\Fell^2\).

<!--block:B0026-->
For (2), the displayed clock and shift matrices satisfy \(\pi_\zeta(a)\pi_\zeta(b)=
\zeta\pi_\zeta(b)\pi_\zeta(a)\), matching \([a,b]=c\). The clock matrix has \(\ell\) distinct one-dimensional eigenspaces. Any invariant subspace is a sum of some of them, because their spectral projectors are polynomials in the clock matrix. The shift matrix cyclically permutes all eigenspaces, so a nonzero invariant subspace contains all of them. Thus \(\pi_\zeta\) is irreducible. Distinct values of \(\zeta\) give inequivalent modules because the center acts by different scalars.

<!--block:B0027-->
Maschke’s theorem applies over \(k\), and the sum of the squared degrees of the displayed pairwise inequivalent irreducibles is \[\ell^2+(\ell-1)\ell^2=\ell^3=|\Ql|.\] For a split semisimple group algebra this is the full dimension ledger, so there are no further irreducibles.

<!--block:B0028-->
\[prop:regular-ledger\] Over \(k\), the right regular module of \(\Ql\) decomposes into the \(\ell^2\) characters, each once, and the \(\ell-1\) modules \(\pi_\zeta\), each with multiplicity \(\ell\). Consequently, \[\begin{aligned}
\label{eq:nullity-ledger}
 \Null(T_{\alpha,\beta,\gamma})
 &=\#\{(u,v)\in\mu_\ell(k)^2:
             \alpha+\beta u+\gamma v=0\}\notag\\
 &\quad+\ell\sum_{\substack{\zeta^\ell=1\\\zeta\ne1}}
  \Null\bigl(\alpha I+\beta\pi_\zeta(a)
                         +\gamma\pi_\zeta(b)\bigr).\end{aligned}\]

<!--block:B0029-->
Maschke’s theorem applies because \(p\nmid|\Ql|\), and [\[lem:irreducibles\]](#lem:irreducibles) gives the complete split list. To freeze the right-translation convention, set \((R_hf)(q)=f(qh)\). For a representation \(\pi\) on \(V\), identify its matrix- coefficient space with \(V^*\otimes V\) by \[\varphi_{\lambda,v}(q)=\lambda(\pi(q)v).\] Then \[R_h\varphi_{\lambda,v}(q)
 =\lambda(\pi(q)\pi(h)v)
 =\varphi_{\lambda,\pi(h)v}(q).\] Thus \(R_h\) acts as \(I_{V^*}\otimes\pi(h)\): the right regular module contains \(\dim V\) copies of \(V\), and the finite operator acts on each copy by \(\alpha I+\beta\pi(a)+\gamma\pi(b)\). Inserting the degrees from [\[lem:irreducibles\]](#lem:irreducibles) proves [\[eq:nullity-ledger\]](#eq:nullity-ledger).

<!--block:B0030-->
\[rem:left-right\] Our finite operator is right translation because the local rule reads \(q,qa,qb\), and the matrix-coefficient calculation above gives the displayed \(\pi(a),\pi(b)\) blocks without a transpose or inverse. Under the common dual convention the blocks are contragredient. On characters this replaces \((u,v)\) by \((u^{-1},v^{-1})\), a permutation of \(\mu_\ell(k)^2\). On nonlinear modules it replaces the central scalar \(\zeta\) by \(\zeta^{-1}\), a permutation of the nontrivial central characters. Hence the summed nullities in [\[eq:nullity-ledger\]](#eq:nullity-ledger) are unchanged even though individual matrices need not be identical.

<!--block:B0031-->
# The character contribution

<!--block:B0032-->
The first line of [\[eq:nullity-ledger\]](#eq:nullity-ledger) is a commutative torsion-point count. The following calculation identifies it over the ground field and also fixes the sign in [\[eq:D-definition\]](#eq:D-definition).

<!--block:B0033-->
\[prop:character-count\] The number of singular character blocks is \(\Dcycl(\alpha,\beta,\gamma)\).

<!--block:B0034-->
For \(u,v\in\mu_\ell(k)\), singularity means \[\label{eq:character-equation}
 \alpha+\beta u+\gamma v=0.\] Because \(\gamma\ne0\), a choice of \(u\) determines the only possible value \[v=-\frac{\alpha+\beta u}{\gamma}.\] Since \(\ell\) is odd, the condition \(v^\ell=1\) becomes \[-\frac{(\alpha+\beta u)^\ell}{\gamma^\ell}=1,
 \qquad\text{or equivalently}\qquad
 (\alpha+\beta u)^\ell+\gamma^\ell=0.\] Thus singular characters are in bijection with the common roots of the two polynomials in [\[eq:D-definition\]](#eq:D-definition). The polynomial \(t^\ell-1\) is separable in characteristic \(p\) because \(p\ne\ell\). Hence the degree of the gcd counts those common roots once each.

<!--block:B0035-->
\[rem:arithmetic-content\] The term \(\Dcycl\) is an intersection of the \(\ell\)-torsion torus with the affine curve \(\alpha+\beta u+\gamma v=0\). It satisfies \(0\le\Dcycl\le\ell\) and can vary with both primes and the coefficient point. This is the part of the answer analogous to lattice Fourier analysis in positive characteristic \[@Zaidenberg2008\]. The next section accounts for the nonabelian mass absent from that calculation. For \((\alpha,\beta,\gamma)=(1,1,1)\), the corresponding resultant is the classical Wendt determinant \[@FordJha1993\]; we use the gcd only as a block count and claim no new resultant theory.

<!--block:B0036-->
# Clock–shift blocks and the Fermat jump

<!--block:B0037-->
Fix a nontrivial central character. Use the explicit module \(\pi_\zeta\) from [\[lem:irreducibles\]](#lem:irreducibles); writing its two generators again, \[\label{eq:clock-shift}
 U=\operatorname{diag}(1,\zeta,\ldots,\zeta^{\ell-1}),
 \qquad Ve_j=e_{j+1\bmod\ell}.\] Changing the central character only replaces \(\zeta\) by another primitive root, which will not change the calculation below.

<!--block:B0038-->
\[lem:clock-shift-det\] For nonzero \(\alpha,\beta,\gamma\in k\), \[\label{eq:clock-shift-det}
 \det(\alpha I+\beta U+\gamma V)
 =\alpha^\ell+\beta^\ell+\gamma^\ell.\]

<!--block:B0039-->
Put \(d_j=\alpha+\beta\zeta^j\). In the determinant of \(\operatorname{diag}(d_0,\ldots,d_{\ell-1})+\gamma V\), a nonzero permutation term can use only the full diagonal or the unique full \(\ell\)-cycle. The cycle sign is \((-1)^{\ell-1}=1\) because \(\ell\) is odd. Therefore \[\det(\alpha I+\beta U+\gamma V)
 =\prod_{j=0}^{\ell-1}(\alpha+\beta\zeta^j)+\gamma^\ell.\] The factorization of \(X^\ell-Y^\ell\), evaluated at \(X=\alpha\) and \(Y=-\beta\), gives \(\prod_j(\alpha+\beta\zeta^j)=\alpha^\ell+\beta^\ell\). This proves [\[eq:clock-shift-det\]](#eq:clock-shift-det).

<!--block:B0040-->
A determinant alone would not determine the fixed-space dimension. The special cyclic sparsity gives the required corank statement.

<!--block:B0041-->
\[lem:nonlinear-nullity\] Every nonlinear block is invertible when \(\Delta_\ell\ne0\) and has nullity exactly one when \(\Delta_\ell=0\).

<!--block:B0042-->
Since \((Vx)_j=x_{j-1}\), in the basis of [\[eq:clock-shift\]](#eq:clock-shift) the equation \((\alpha I+\beta U+\gamma V)x=0\) is exactly \[\label{eq:cyclic-recurrence}
 (\alpha+\beta\zeta^j)x_j+\gamma x_{j-1}=0
 \qquad(j\bmod\ell).\] Since \(\gamma\ne0\), a single coordinate determines all other coordinates by successive use of [\[eq:cyclic-recurrence\]](#eq:cyclic-recurrence). The kernel therefore has dimension at most one. By [\[lem:clock-shift-det\]](#lem:clock-shift-det), it is nonzero exactly when \(\Delta_\ell=0\), in which case its dimension is one.

<!--block:B0043-->
By [\[prop:character-count\]](#prop:character-count), the characters contribute \(\Dcycl\). By [\[lem:nonlinear-nullity\]](#lem:nonlinear-nullity), either none or all of the \(\ell-1\) nonlinear types are singular. Each singular type has block nullity one and multiplicity \(\ell\) in the regular representation, so its total contribution is \(\ell(\ell-1)\). Insert these terms into [\[eq:nullity-ledger\]](#eq:nullity-ledger), then use [\[lem:base-change\]](#lem:base-change) to descend the nullity from \(k\) to \(\Fp\).

<!--block:B0044-->
# Coefficient phase diagram and finite controls

<!--block:B0045-->
Multiplying \((\alpha,\beta,\gamma)\) by a nonzero scalar multiplies the finite operator by that scalar and does not change its kernel. The family therefore lives naturally in the projective coefficient plane.

<!--block:B0046-->
\[cor:phase-diagram\] On \(\mathbb P^2(\Fp)\) away from the coordinate axes, the nonlinear part of the fixed dimension is zero off the Fermat curve \[\alpha^\ell+\beta^\ell+\gamma^\ell=0\] and equals \(\ell(\ell-1)\) on that curve. The remaining variation is the bounded term \(\Dcycl\le\ell\).

<!--block:B0047-->
The Fermat equation is homogeneous, and scaling both polynomials in [\[eq:D-definition\]](#eq:D-definition) by a nonzero \(\ell\)th power does not change their common roots. The claim now follows from [\[thm:main\]](#thm:main).

<!--block:B0072-->
**Bounded coding/spectral transfer.** On the quotient \(\Ql\), the kernel of \(T_{\alpha,\beta,\gamma}\) is a linear code of length \(n_{\rm code}=|\Ql|=\ell^3\) and dimension \[k_{\rm code}=\Dcycl(\alpha,\beta,\gamma)+\ell(\ell-1)\one_{\{\Delta_\ell=0\}}.\] Thus the theorem determines the rate-like normalized dimension \(k_{\rm code}/\ell^3\). Spectrally, the same number is the geometric multiplicity of the zero eigenvalue of the displayed finite convolution matrix. The argument does not determine the code's minimum distance, weight enumerator, or decoding performance, nor the nonzero eigenvalues, their algebraic multiplicities, or a spectral gap.

<!--block:B0048-->
\[cor:unit\] For the rule \(x_g+x_{ga}+x_{gb}=0\), \[\dim_{\Fp}\Fix_{N_\ell}X_{p;1,1,1}
 =\deg\gcd_{\Fp[t]}(t^\ell-1,(-1-t)^\ell-1)
  +\ell(\ell-1)\one_{\{p=3\}}.\]

<!--block:B0049-->
For odd \(\ell\), \((-1-t)^\ell-1=-((1+t)^\ell+1)\), so the two gcd expressions agree up to a unit. The nonlinear determinant is \(1+1+1=3\), which vanishes in a prime field exactly in characteristic three.

<!--block:B0050-->
We checked the formula by constructing the full matrix of [\[eq:finite-operator\]](#eq:finite-operator) in the coordinate model [\[eq:heis-product\]](#eq:heis-product). Gaussian elimination was performed over the indicated prime field. A selection of the frozen results appears in [1](#tab:controls); the complete receipt and code accompany the paper. The control also constructs four clock–shift blocks directly over fields containing the required roots of unity: two singular and two nonsingular cases verify both [\[lem:clock-shift-det\]](#lem:clock-shift-det) and the zero/one nullity dichotomy in [\[lem:nonlinear-nullity\]](#lem:nonlinear-nullity).


<!--block:B0051-->
| \(\ell\) | \(p\) | \((\alpha,\beta,\gamma)\) | Fermat stratum | Nullity |
| :------: | :---: | :-----------------------: | :------------- | :-----: |
|    3     |   2   |        \((1,1,1)\)        | nonsingular    |    2    |
|    3     |   5   |        \((1,1,2)\)        | singular       |    6    |
|    3     |   5   |        \((1,2,3)\)        | nonsingular    |    0    |
|    3     |   7   |        \((2,3,4)\)        | nonsingular    |    1    |
|    5     |   3   |        \((1,1,1)\)        | singular       |   21    |
|    5     |  11   |        \((1,1,1)\)        | nonsingular    |    3    |
|    5     |  11   |        \((2,3,5)\)        | nonsingular    |    2    |

<!--block:B0052-->
Independent full-matrix controls. In every row the observed nullity equals [\[eq:main-formula\]](#eq:main-formula).


<!--block:B0053-->
The full quotient matrices verify the implementation of the displayed group law, the selected finite operator, and the final nullity formula on the sample tuples. They can expose many transcription or implementation mistakes, including an omitted regular multiplicity. Nullity comparison alone does not distinguish the selected right-translation convention from the dual left convention, because [\[rem:left-right\]](#rem:left-right) shows that the total nullity is invariant under that change. All computations remain finite regression evidence and are not used to infer the all-prime theorem.

<!--block:B0073-->
An additional non-split fixture takes \((\ell,p)=(3,2)\), so the nontrivial cube roots lie in \(\mathbb F_4\) rather than \(\mathbb F_2\). Writing them as \(a\) and \(1+a\), with \(a^2+a+1=0\), exact enumeration of \(1+u+v=0\) gives precisely \((u,v)=(a,1+a),(1+a,a)\). The count two agrees with \[\deg\gcd_{\mathbb F_2[t]}(t^3-1,(1+t)^3+1)=2.\] This independently checks that the ground-field gcd degree counts geometric character solutions even when the roots do not split over the prime field.

<!--block:B0054-->
# Scope, limitations, and declarations

<!--block:B0055-->
#### Ownership and scope.

<!--block:B0056-->
Principal algebraic actions of the discrete Heisenberg group and the exact integer element \(1+a+b\) precede this paper [@GollSchmidtVerbitskiy2014; @LindSchmidt2015]. Finite Heisenberg Stone–von Neumann theory and the explicit finite-group irreducible ledger are also standard [@GurevichHadani2010; @GrassbergerHormann2001]. Deundyak and Leonov already supply left/right convolution, noncommutative Fourier blocks, and a blockwise equation-solving algorithm on finite Heisenberg groups [@DeundyakLeonov2016]. We therefore claim none of those frameworks. The verified local ledger and bibliography support the following theorem-component comparison; absence of a P70 output from this table means only that none of the locally verified sources states it, not that no such source exists.

<!--block:B0074-->
| Component | Closest verified owner/source | P70 difference: coefficient field; operator; output invariant |
| :-- | :-- | :-- |
| Weighted fixed-space formula | Principal Heisenberg actions and \(1+a+b\) [@GollSchmidtVerbitskiy2014; @LindSchmidt2015]; finite-Heisenberg convolution solver [@DeundyakLeonov2016] | \(\mathbb F_p\) with quotient order \(\ell\ne p\); weighted right convolution; exact congruence-kernel dimension. |
| Character term | Positive-characteristic lattice torsion analysis [@Zaidenberg2008] and the unit Wendt resultant [@FordJha1993] | \(\mathbb F_p\), with roots allowed over a splitting extension; weighted Heisenberg character blocks; the gcd degree \(\Dcycl\). |
| Central-character-independent determinant | Standard finite-Heisenberg modules [@GurevichHadani2010; @GrassbergerHormann2001] and the unit resultant [@FordJha1993] | Cross-characteristic splitting field; \(\alpha I+\beta U+\gamma V\); \(\alpha^\ell+\beta^\ell+\gamma^\ell\) for every nonlinear type. |
| Corank-one singular block | Standard blocks and blockwise convolution solving [@GurevichHadani2010; @DeundyakLeonov2016] | Cross-characteristic splitting field; cyclic clock–shift recurrence; exact nullity one on the Fermat locus. |
| Regular-multiplicity jump | Finite-Heisenberg irreducible ledger [@GrassbergerHormann2001; @GurevichHadani2010] | \(\mathbb F_p\) after base-change descent; regular representation of the weighted operator; total jump \(\ell(\ell-1)\). |

<!--block:B0075-->
After that owner subtraction, the residual P70 claim is the conjunction of the weighted cross-characteristic congruence-nullity formula, its character gcd term, the central-character-independent Fermat determinant, exact corank-one singular blocks, and the resulting \(\ell(\ell-1)\) regular-representation jump. A bounded search through 26 August 2026 found no exact match for that conjunction. This is not a worldwide novelty or priority certificate, and specialist exact-neighbour clearance remains unresolved; external release remains on hold.

<!--block:B0057-->
#### Limitations.

<!--block:B0058-->
The assumption \(p\ne\ell\) is structural: at \(p=\ell\), the finite regular module need not be semisimple, and nilpotent extensions can change the nullity. We also require all three coefficients to be nonzero. Degenerate two-term rules admit separate elementary case splits but are outside the selected theorem. Finally, congruence-fixed dimensions do not by themselves settle expansiveness, entropy, density of periodic points, or generator questions for the infinite action.

<!--block:B0059-->
#### Data and code availability.

<!--block:B0060-->
No external data are used. The finite-control source and its frozen text receipt are included in the manuscript directory. They generate every reported matrix nullity from the displayed group law and coefficient tuple.

<!--block:B0061-->
#### Ethics declaration.

<!--block:B0062-->
The work is purely mathematical, uses no human participants, animals, or sensitive data, and requires no ethics approval.

<!--block:B0063-->
#### Author contributions.

<!--block:B0064-->
Conceptualization, formal analysis, software, verification, writing—original draft, and writing—review and editing were performed by the anonymous author or authors. Attribution must be replaced by the final CRediT record before external submission.

<!--block:B0065-->
#### Conflicts of interest and funding.

<!--block:B0066-->
No conflict of interest or external funding is declared in this internal draft.

<!--block:B0067-->
#### Tool-use disclosure.

<!--block:B0068-->
Automated tools assisted with finite regression checks, source discovery, LaTeX compilation, and language editing. The formal arguments and all bibliographic metadata require author verification before external use.

<!--block:B0069-->
# Conclusion

<!--block:B0070-->
Weighted three-term Heisenberg shifts have an exact finite-quotient phase diagram. Character blocks contribute the cyclotomic intersection degree \(\Dcycl\), while every nonlinear block is controlled by the same Fermat polynomial \(\alpha^\ell+\beta^\ell+\gamma^\ell\). The regular multiplicities turn its vanishing into a jump of \(\ell(\ell-1)\). The unit-coefficient characteristic-three phenomenon is therefore one specialization of a coefficient-space theorem rather than an isolated determinant coincidence.

<!--block:B0071-->
The excluded modular case \(p=\ell\) is the next concrete problem. There the failure of semisimplicity should replace the two-stratum ledger by a radical filtration, so the present formula identifies both the baseline and the exact point at which new representation-theoretic behavior must enter.
