# A Descent Obstruction to Verschiebung Lifts on fppf and Finite-Flat Sites

## 1. Introduction and main results

Deninger associates to a commutative ring \(A\) a reduced integral monoid algebra \(\underline{\mathbf Z}(A)\) and a natural map from it to the rational big-Witt vectors \(W_{\mathrm{rat}}(A)\). After passage to sheaves, this map is an epimorphism on the sites considered below. The resulting quotient presentation raises a natural lifting question: does the additive Verschiebung \(V_N\) of rational Witt vectors lift to an additive endomorphism of the sheafified reduced monoid algebra? The question is posed for the finite-flat and fppf topologies in Deninger, *Rational Witt vectors and associated sheaves*, arXiv:2508.05329v1, p. 25.<!--ref:Deninger2025Rational--><!--anchor:page:25-->
<!--PDF-INTEGRITY-WARNING: The p. 25 locator is inherited from the frozen source screen. No PDF-preflight sidecar was supplied to this drafting call.-->
The distinction between an epimorphism of sheaves and a surjection on sections is decisive: the former supplies local preimages, whereas a sheaf endomorphism must assign compatible global preimages functorially.

The quotient description alone does not answer the problem, because it controls local existence rather than compatibility on overlaps. To our knowledge, based on targeted searches of official arXiv records and full text, publisher pages, Crossref, and the Stacks Project completed on 2026-08-24, no direct post-source solution to this lifting question was found. The nearest different-owner result identified in that search is Deninger and Mellit, *ZR and rings of Witt vectors \(W_S(R)\)*, Rend. Sem. Mat. Univ. Padova **142** (2019), 93–102, Theorem 1.1, DOI 10.4171/RSMUP/32.<!--CITATION-MARKER-CAVEAT: The frozen bibliography supplied no citation_key for this verified Deninger–Mellit record. Downstream finalization must assign its ref slug.--> Their theorem computes a kernel for a related monoid-algebra map to truncated Witt vectors, but it does not concern the present sheafification or its descent problem. The contribution here is therefore framed as an answer to Deninger’s specified question, rather than as an unrestricted priority claim.

Fix a universe-small version \(\mathcal C\) of \(\mathrm{NoethAffSch}\) containing the affine schemes and fiber products used below. On either the absolute fppf site or, separately, the finite-flat site, put
\[
  Z=\underline{\mathbf Z}(\mathcal O)^{\sharp},\qquad
  W=W_{\mathrm{rat}}(\mathcal O)^{\sharp},\qquad
  \omega:Z\twoheadrightarrow W.
\]
For \(N\geq 1\), Verschiebung is the additive endomorphism determined in the power-series model by
\[
  V_N(f)(T)=f(T^N).
\]
Here and throughout, a lift means a morphism of additive sheaves. No multiplicative compatibility or system of Frobenius–Verschiebung identities is included in the assertion.

**Theorem A (nonexistence of additive Verschiebung lifts).** *Let \(N>1\). On the absolute fppf site there is no additive sheaf endomorphism \(\widetilde V_N:Z\to Z\) such that*
\[
  \omega\circ\widetilde V_N=V_N\circ\omega.
\]
*The same nonexistence statement holds on the finite-flat site, by a separate finite-flat descent argument. For \(N=1\), the identity of \(Z\) is a lift of \(V_1=\mathrm{id}_W\).* 

The obstruction is explicit. Choose a prime divisor \(q\mid N\), write \(N=q^a d\) with \((q,d)=1\), and take a finite extension \(k/\mathbf F_q\) containing the \(d\)-th roots of unity. The finite-free cover
\[
  k[x]\longrightarrow k[s],\qquad x\longmapsto s^N,
\]
forces any putative image of the section \((x)^{\sharp}\) to restrict to
\[
  c(s)^{\sharp},\qquad
  c(s)=q^a\sum_{\zeta\in\mu_d(k)}(\zeta s).
\]
Indeed, \(\omega(c(s))=1-s^N T^N\), and the relevant map \(\omega\) is injective over the principal ideal domain \(k[s]\). On the double overlap, the two restrictions of \(c(s)^{\sharp}\) would have to agree. Specializing one root to \(\epsilon\) and the other to zero in \(k[\epsilon]/(\epsilon^N)\) yields a section whose inner factor has Witt image \(1-\epsilon^dT^d\neq 1\). Torsion-freeness of \(Z\) then preserves its nonzero multiple by \(q^a\). Thus the forced local preimage does not descend.

The failed descent also has an extension-theoretic formulation. Let \(K=\ker(\omega)\) and let
\[
  e:\quad 0\longrightarrow K\longrightarrow Z\xrightarrow{\omega}W\longrightarrow 0
\]
denote the resulting extension in the abelian category of sheaves on the chosen site.

**Corollary B (extension obstruction).** *For every \(N>1\) and every endomorphism \(u:K\to K\), one has*
\[
  u_*e\neq V_N^*e\qquad\text{in }\operatorname{Ext}^1(W,K).
\]
*Moreover, \(e\) is nonsplit and \(V_N^*e\) is nonzero.*

The equality excluded in Corollary B is the exact formal condition for a morphism between the pushout of \(e\) along \(u\) and the pullback of \(e\) along \(V_N\). Such a morphism has a middle arrow \(Z\to Z\) inducing \(u\) on \(K\) and \(V_N\) on \(W\), hence gives the prohibited lift. This uses only the functoriality of extensions described in the Stacks Project, Tags [010I](https://stacks.math.columbia.edu/tag/010I)<!--ref:StacksProject--><!--anchor:section:010I--> and [06XP](https://stacks.math.columbia.edu/tag/06XP)<!--ref:StacksProject--><!--anchor:section:06XP-->. The overlap calculation is a necessary descent test and is not asserted to compute the full sheaf \(\operatorname{Ext}^1\) group.

The finite-flat instance also produces a section over a Dedekind domain that is locally, but not globally, in the image of \(\omega\). Consequently, the sectionwise equality in Deninger’s Corollary 4.6, as stated in v1 on p. 23, requires correction.<!--ref:Deninger2025Rational--><!--anchor:section:Corollary%204.6--> This conclusion does not affect the independent inputs used here, namely Proposition 4.3, Example 4.4, and Proposition 4.5. Section 6 isolates that source-sensitive point. The present argument first develops the sheaves and the injectivity lemmas on which the obstruction rests.

The proof is organized around this distinction. Section 2 fixes the two sites, the rational Witt sheaf, and the actual kernel extension. Section 3 proves the torsion, detection, and Dedekind-injectivity lemmas. Section 4 calculates the failed descent datum for all \(N>1\). Sections 5 and 6 then give the extension and finite-flat formulations separately.

## 2. Rational Witt sheaves and the extension

Let \(\tau\) denote either the fppf topology or the finite-flat topology on the fixed small affine site \(\mathcal C\). The two cases will be kept distinct whenever a covering argument is used. We write “finite-flat” rather than the source notation “fp” to avoid confusion with finite presentation. Both topologies are subcanonical, and the cover \(k[x]\to k[s]\), \(x\mapsto s^N\), belongs to both. Their subcanonicity will also be used in Lemma 3.3.

For a commutative unital ring \(A\), let \(\mathbf Z[A,\cdot]\) be the integral monoid algebra of the multiplicative monoid of \(A\), and write
\[
  \underline{\mathbf Z}(A)=\mathbf Z[A,\cdot]/\mathbf Z(0).
\]
This is Deninger’s reduced monoid algebra (equation (4), p. 3).<!--ref:Deninger2025Rational--><!--anchor:section:Equation%20(4)--> We write \((a)\) for the class of the monoid element \(a\). Let \(W_{\mathrm{rat}}(A)\) be the rational big-Witt group inside \(1+TA[[T]]\), with its additive law represented by multiplication of power series, as in Deninger’s equation (20), p. 14.<!--ref:Deninger2025Rational--><!--anchor:section:Equation%20(20)--> The Teichmüller element associated with \(a\) is \([a]=1-aT\), and the induced additive map is
\[
  \omega_A:\underline{\mathbf Z}(A)\longrightarrow W_{\mathrm{rat}}(A),
  \qquad
  \omega_A\!\left(\sum_i n_i(a_i)\right)
    =\prod_i(1-a_iT)^{n_i}.
\]

Thus \(\omega_A((a))=[a]\), while Verschiebung sends this element to
\[
  V_N([a])=1-aT^N.
\]
The local factorization used later is compatible with these formulas. If \(N=q^ad\) in characteristic \(q\) and \(a=s^N\), then the product over the \(d\)-th roots of unity rewrites \(1-s^NT^N\) as the image under \(\omega\) of \(q^a\sum_{\zeta\in\mu_d(k)}(\zeta s)\). The quotient presentation therefore supplies the relevant preimage on the root cover. The issue is whether that preimage descends.

Apply these functors to the structure sheaf and sheafify for \(\tau\). Deninger’s Theorem 3.4 identifies \(W_{\mathrm{rat}}(\mathcal O)\) as an fpqc sheaf, so it is already a sheaf for either topology used here.<!--ref:Deninger2025Rational--><!--anchor:section:Theorem%203.4--> Proposition 4.3, p. 21,<!--ref:Deninger2025Rational--><!--anchor:section:Proposition%204.3--> gives the epimorphism
\[
  \omega:Z=\underline{\mathbf Z}(\mathcal O)^{\sharp}_{\tau}
       \twoheadrightarrow W=W_{\mathrm{rat}}(\mathcal O).
\]
The operation \(V_N\) is additive because substitution \(T\mapsto T^N\) respects multiplication of power series. A lift is therefore a dotted arrow in the diagram of additive sheaves
\[
\begin{CD}
Z @>{\widetilde V_N}>> Z\\
@V{\omega}VV @VV{\omega}V\\
W @>{V_N}>> W.
\end{CD}
\]
The adjective “additive” is essential: the theorem concerns this diagram and makes no assertion about a lift in the category of sheaves of rings.

Evaluation on an affine object will be denoted by \(Z(A)\) and \(W(A)\), but this notation refers to sections of the sheaves. It should not be confused with the presheaf groups \(\underline{\mathbf Z}(A)\) and \(W_{\mathrm{rat}}(A)\) before sheafification. Proposition 4.3<!--ref:Deninger2025Rational--><!--anchor:section:Proposition%204.3--> says that for \(w\in W(A)\), there is a \(\tau\)-cover \(\{A\to A_i\}\) and local sections \(z_i\in Z(A_i)\) mapping to \(w|_{A_i}\). It neither chooses the \(z_i\) naturally nor says that they agree after pullback to \(A_i\otimes_A A_j\). A lift \(\widetilde V_N\), in contrast, would produce a global section before any cover is selected. This difference turns a formal quotient question into a descent calculation.

Before sheafification, define
\[
  K_0(A)=\ker\!\left(\underline{\mathbf Z}(A)
             \xrightarrow{\omega_A}W_{\mathrm{rat}}(A)\right).
\]
Equivalently,
\[
  K_0(A)=\left\{\sum_i n_i(a_i):
       \prod_i(1-a_iT)^{n_i}=1\text{ in }W_{\mathrm{rat}}(A)\right\}.
\]
Exactness of abelian sheafification, recalled in Lemma 3.2, identifies the actual kernel sheaf with \(K=K_0^{\sharp}_{\tau}\) and yields the extension \(e\) displayed above.

This construction must not be read objectwise. An epimorphism of abelian sheaves means that a target section acquires a preimage after passage to a covering family. It need not have a preimage over the original object. This local characterization is the content used from the Stacks Project, Tag [03CN](https://stacks.math.columbia.edu/tag/03CN).<!--ref:StacksProject--><!--anchor:section:03CN--> Theorem A exploits precisely the additional compatibility demanded of a global section: the local preimage supplied over the root cover has unequal pullbacks on the double overlap.

## 3. Detection and injectivity lemmas

The obstruction proof uses four elementary facts. They are stated for either topology when the proof is site-independent. The final injectivity statement treats the fppf and finite-flat refinements separately.

**Lemma 3.1 (torsion-freeness).** *For every positive integer \(m\), multiplication by \(m\) on \(Z\) is a monomorphism.*

**Proof.** Objectwise, \(\underline{\mathbf Z}(A)\) is the free abelian group on the nonzero elements of the multiplicative monoid of \(A\): quotienting \(\mathbf Z[A,\cdot]\) by \(\mathbf Z(0)\) removes a free direct summand. It is therefore torsion-free, so multiplication by \(m\) is injective on every section of the presheaf. Abelian sheafification is exact (Stacks Project, Tag [03CN](https://stacks.math.columbia.edu/tag/03CN)),<!--ref:StacksProject--><!--anchor:section:03CN--> hence it preserves this monomorphism. \(\square\)

The sheaf statement is stronger than torsion-freeness at a selected ring. Once a section survives sheafification, no nonzero integer multiple of it can disappear after a further covering refinement. Section 4 applies this observation with \(m=q^a\).

**Lemma 3.2 (the kernel after sheafification).** *The natural morphism \(K_0^{\sharp}_{\tau}\to Z\) identifies \(K_0^{\sharp}_{\tau}\) with \(\ker(\omega)\). In particular,*
\[
  0\longrightarrow K_0^{\sharp}_{\tau}\longrightarrow Z
   \xrightarrow{\omega}W\longrightarrow 0
\]
*is exact.*

**Proof.** The defining presheaf sequence is exact at \(K_0\) and \(\underline{\mathbf Z}(\mathcal O)\). Exact abelian sheafification preserves its kernel, while Deninger’s Theorem 3.4 identifies the sheafification of the target with \(W\).<!--ref:Deninger2025Rational--><!--anchor:section:Theorem%203.4--> Surjectivity in the sheaf category is Proposition 4.3.<!--ref:Deninger2025Rational--><!--anchor:section:Proposition%204.3--> Thus the displayed sequence is the actual extension, without any assertion that \(K_0(A)\) controls global surjectivity object by object. \(\square\)

In particular, the notation \(K=K_0^{\sharp}_{\tau}\) records a sheaf-theoretic identity, not an objectwise formula \(K(A)=K_0(A)\) for every \(A\). Sections of \(K\) may be represented only after refinement. This is why a nonzero specialized overlap section, rather than a calculation of one presheaf kernel alone, is needed in the main proof.

**Lemma 3.3 (big-Witt detection).** *Assume \(\tau\) is subcanonical. If \(z\in Z(Y)\) has \(\omega(z)\neq 1\) in the big-Witt sheaf, then \(z\neq 0\). In particular, let \(k\) have characteristic \(q\), let \(d<N\) satisfy \((q,d)=1\), and assume that \(k\) contains \(\mu_d\). For \(D=k[\epsilon]/(\epsilon^N)\), the section represented by*
\[
  y=\sum_{\zeta\in\mu_d(k)}(\zeta\epsilon)
\]
*is nonzero, since \(\omega(y)=1-\epsilon^dT^d\neq 1\).* 

**Proof.** The first assertion is immediate from functoriality: a zero section must map to the identity element of the additive big-Witt group. For the displayed element,
\[
  \omega(y)=\prod_{\zeta\in\mu_d(k)}(1-\zeta\epsilon T)
           =1-\epsilon^dT^d.
\]
The product identity holds because \((q,d)=1\) and \(k\) contains all \(d\)-th roots of unity. Because \(d<N\), the coefficient \(\epsilon^d\) is nonzero in \(D\). This is the detector used in Deninger’s Example 4.4, p. 22, with that example giving the case \(N=2\).<!--ref:Deninger2025Rational--><!--anchor:section:Example%204.4--> The detector is applied before multiplication by \(q^a\). Lemma 3.1 then shows that the multiple remains nonzero even though its rational-Witt image will vanish. \(\square\)

**Lemma 3.4 (Dedekind injectivity on the two sites).** *Let \(B\) be a Dedekind domain. Then*
\[
  \omega_B:Z(B)\longrightarrow W_{\mathrm{rat}}(B)
\]
*is injective after sheafification for the fppf topology and, separately, for the finite-flat topology.*

**Proof.** Consider first an fppf covering \(\{\operatorname{Spec}C_i\to\operatorname{Spec}B\}\). Quasi-compactness permits a finite subcover. Each \(C_i\) is a finitely presented flat \(B\)-algebra and is Noetherian. Replace \(C_i\) by the quotients \(C_i/P\) over its finitely many minimal primes. Flat going-down gives \(P\cap B=(0)\) (Stacks Project, Tag [00HS](https://stacks.math.columbia.edu/tag/00HS)),<!--ref:StacksProject--><!--anchor:section:00HS--> so each \(C_i/P\) is a domain and is torsion-free as a \(B\)-module. A torsion-free module over a Dedekind domain is flat (Stacks Project, Tag [0AUW](https://stacks.math.columbia.edu/tag/0AUW)).<!--ref:StacksProject--><!--anchor:section:0AUW--> These quotients are still finitely presented over \(B\), and their spectra remain jointly surjective. They therefore form an fppf refinement by domains.

For a finite-flat covering, the same construction remains within the finite-flat site. Each quotient \(C_i/P\) is finite over \(B\), and torsion-freeness over the Dedekind domain makes it finite flat. The minimal-prime quotients again form a jointly surjective family. Thus every cover relevant to either site admits a refinement by integral domains. Deninger’s Proposition 4.5, pp. 22–23, then gives the asserted injectivity.<!--ref:Deninger2025Rational--><!--anchor:section:Proposition%204.5--> In particular, the conclusion applies to \(B=k[s]\), a principal ideal domain. Hence the local section \(c(s)^{\sharp}\) occurring in Theorem A is not one choice among several: it is the unique possible restriction of a putative lift. \(\square\)

The first three lemmas ensure that the overlap specialization detects a genuine nonzero section of the kernel sheaf, while Lemma 3.4 removes the possibility of repairing descent by choosing another local preimage. Section 4 applies these facts to the finite-free root cover for every \(N>1\).

<!--protected-hedges: To our knowledge, based on targeted searches of official arXiv records and full text, publisher pages, Crossref, and the Stacks Project completed on 2026-08-24-->
