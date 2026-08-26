<!--block:B0001-->
# Introduction

<!--block:B0002-->
A zip shift records future symbols in one alphabet and past symbols in a quotient alphabet. When a future symbol crosses the origin, a surjection forgets which element of its fibre was present. This gives a compact symbolic model of a finite-to-one noninvertible map. The formal zip-shift space, its sliding block codes, local homeomorphism structure, and periodic points are developed by \[@LameiMehdipour2025\]. The same system appears under the name *extended shift*; \[@MartinsMattosVarao2026\] compute metric and folding entropies for its Bernoulli measures. Those results are owner-subtracted here.

<!--block:B0003-->
For a uniform \(n\)-to-one zip shift the local degree is constant, so its logarithm carries no fluctuations. Uniform systems are treated through square entropy and intrinsic ergodicity by \[@MehdipourJangjooye2025\]. A nonuniform fibre profile changes the question: the orbit sees a sequence of local degrees, and the exponential growth of their products depends on how frequently the future visits each fibre. The intrinsic potential \[\phi_\tau(x)=\log |F_\tau^{-1}(x)|\] turns that loss of information into an additive observable.

<!--block:B0004-->
This paper gives one closed theorem package for that observable. The component-level comparison in \cref{tab:component-comparison} separates documented overlap, documented differences, and a same-family project whose theorem text is unavailable. Accordingly, the list below states the residual components supported by the frozen local source ledger; it is not a priority claim, and the pressure component retains high collision risk.

<!--block:B0005-->
1.  For the nonuniform full one-block model, the pressure and its unique equilibrium states satisfy \[P_\tau(t)=\log\sum_{z\in Z}k_z^{t+1},\qquad
    p_t(s)\propto k_{\tau(s)}^t.\] The derivative is the equilibrium average of \(\log d_\tau\), and the second derivative detects whether the profile is nonuniform. This is the high-collision component identified in the comparison table.

2.  For the same model, the degree-exponent level sets have an exact Bowen-entropy spectrum, both as a constrained Shannon maximum and as the Legendre transform of \(P_\tau\).

3.  The entire pressure curve recovers the fibre-size multiset. Combined with an explicit one-block construction, this yields the equivalence among topological conjugacy, equal fibre profiles, and equal degree-pressure curves inside the full one-block family.

4.  In that family, weighted periodic points satisfy \[\sum_{x\in\Fix(F_\tau^n)}
     \exp\!\left(t\sum_{j=0}^{n-1}\phi_\tau(F_\tau^j x)\right)
     =\left(\sum_z k_z^{t+1}\right)^n.\]

<!--block:B0006-->
The natural extension of a full zip shift is the ordinary full two-sided \(|S|\)-shift. We prove the explicit identification because it is the shortest route to pressure, but we use it only as infrastructure. Likewise, the metric- and folding-entropy formulae themselves remain those of \[@MartinsMattosVarao2026\]; our statement substitutes the equilibrium weights and connects the resulting quantities to \(P_\tau'\).

<!--block:B0007-->
Bowen’s entropy for noncompact sets provides the level-set notion \[@Bowen1973\]; digit-frequency multifractal arguments give adjacent context \[@BarreiraSaussolSchmeling2002\]. Here the proof reduces directly to types on the future alphabet and keeps the multiplicity of every fibre.

<!--block:B0008-->
defines the map and its extension. Pressure and entropy identities are proved in [3](#sec:pressure). Periodic data and conjugacy rigidity appear in [4](#sec:rigidity), the multifractal spectrum in [5](#sec:multi), and source boundaries in [7](#sec:scope).

<!--block:B0009-->
# The full zip shift and its natural extension

<!--block:B0010-->
Let \(S\) and \(Z\) be nonempty finite sets, and let \(\tau:S\to Z\) be surjective. Set \[X_\tau=Z^{\Z_{<0}}\times S^{\Z_{\geq0}}.\] We write a point as \(x=(\ldots,x_{-2},x_{-1};x_0,x_1,\ldots)\) and define \[F_\tau x=(\ldots,x_{-2},x_{-1},\tau(x_0);x_1,x_2,\ldots).
 \tag{2.1}\label{eq:zip-map}\] This is the full one-block zip shift of \[@LameiMehdipour2025\], and the same formula defines the extended shift of \[@MartinsMattosVarao2026\]. For \(z\in Z\), put \[k_z=|\tau^{-1}(z)|,
 \qquad m_k=|\{z\in Z:k_z=k\}|.\] The multiset \(\{k_z:z\in Z\}\) is the *fibre profile*.

<!--block:B0011-->
\[lem:degree\] The map \(F_\tau\) is a local homeomorphism and \[d_\tau(x):=|F_\tau^{-1}(x)|=k_{x_{-1}}.
 \tag{2.2}\label{eq:degree}\] Thus \(\phi_\tau=\log d_\tau\) is a locally constant intrinsic potential.

<!--block:B0012-->
For a preimage \(y\) of \(x\), all coordinates except \(y_0\) are forced by [\[eq:zip-map\]](#eq:zip-map): \(y_j=x_{j-1}\) for \(j\neq0\). The remaining condition is \(\tau(y_0)=x_{-1}\), giving exactly \(k_{x_{-1}}\) choices. On the cylinder where \(x_{-1}=z\), the inverse branches obtained by choosing \(s\in\tau^{-1}(z)\) are continuous.

<!--block:B0013-->
Let \(\sigma:S^\Z\to S^\Z\) be the ordinary left shift. Define \[\pi:S^\Z\longrightarrow X_\tau,
 \qquad
 \pi(t)_i=
 \begin{cases}
 \tau(t_i),&i<0,\\
 t_i,&i\geq0.
 \end{cases}
 \tag{2.3}\label{eq:factor}\] Then \(F_\tau\pi=\pi\sigma\).

<!--block:B0014-->
\[prop:natural\] The inverse-limit natural extension of \((X_\tau,F_\tau)\) is conjugate to \((S^\Z,\sigma)\), with current-coordinate factor [\[eq:factor\]](#eq:factor). Under this identification, \[\phi_\tau\circ\pi(t)=\log k_{\tau(t_{-1})}.
 \tag{2.4}\label{eq:lift-potential}\] Invariant probabilities correspond affinely, and corresponding measures have equal metric entropy.

<!--block:B0015-->
An inverse history is a sequence \((x^{(0)},x^{(-1)},\ldots)\) satisfying \(F_\tau x^{(-j)}=x^{(-j+1)}\). Recover \(t_i=x^{(0)}_i\) for \(i\geq0\) and \(t_{-j}=x^{(-j)}_0\) for \(j\geq1\). Conversely, a two-sided word \(t\) gives the history whose \(j\)th predecessor has future beginning at \(t_{-j}\) and whose past is the corresponding \(\tau\)-image. These coordinate formulae are continuous and inverse to one another, and advancing the history is the left shift. Formula [\[eq:lift-potential\]](#eq:lift-potential) follows from \(\pi(t)_{-1}=\tau(t_{-1})\).

<!--block:B0016-->
For completeness, let \(p_{-j}\) denote projection from the inverse limit to its \(j\)th predecessor. If \(\mu\) is \(F_\tau\)-invariant, its only possible invariant lift is determined on finite-coordinate cylinders by \[\widehat\mu\!\left(\bigcap_{j=0}^r p_{-j}^{-1}A_j\right)
 =\mu\!\left(\bigcap_{j=0}^r
       F_\tau^{-(r-j)}A_j\right).
 \tag{2.5}\label{eq:natural-measure}\] Invariance makes these finite-dimensional distributions consistent, so they define the lift; the formula also proves uniqueness and affinity. Conversely the current-coordinate projection sends every invariant inverse-limit measure to an invariant base measure. Finally, for every finite measurable partition \(\mathcal P\) of \(X_\tau\), the entropy rate of \(p_0^{-1}\mathcal P\) under the invertible natural-extension map equals the entropy rate of \(\mathcal P\) under \(F_\tau\). Finite joins of such pullback partitions generate the inverse-limit sigma-algebra, so the usual increasing- partition argument gives \(h_{\widehat\mu}(\widehat F_\tau)=h_\mu(F_\tau)\).

<!--block:B0017-->
In particular, the topological entropy is \(\log|S|\). This ordinary fact is not the invariant used below: different fibre profiles can have the same \(|S|\) and hence the same entropy.

<!--block:B0018-->
# Degree pressure and equilibrium states

<!--block:B0019-->
For \(t\in\R\), let \(P_\tau(t)\) denote the topological pressure of \(t\phi_\tau\) for \(F_\tau\). Define \[Q_\tau(t)=\sum_{z\in Z}k_z^{t+1}
 =\sum_{s\in S}k_{\tau(s)}^t.
 \tag{3.1}\label{eq:q}\]

<!--block:B0020-->
\[thm:pressure\] For every \(t\in\R\), \[P_\tau(t)=\log Q_\tau(t).
 \tag{3.2}\label{eq:pressure}\] There is a unique equilibrium state \(\mu_t\). Its natural extension is the Bernoulli measure on \(S^\Z\) with one-symbol probabilities \[p_t(s)=\frac{k_{\tau(s)}^t}{Q_\tau(t)}.
 \tag{3.3}\label{eq:pt}\] If \[r_t(z)=\sum_{s\in\tau^{-1}(z)}p_t(s)
 =\frac{k_z^{t+1}}{Q_\tau(t)},
 \tag{3.4}\label{eq:rt}\] then \[P_\tau'(t)=\sum_z r_t(z)\log k_z,
 \qquad
 P_\tau''(t)=\Var_{r_t}(\log k_z).
 \tag{3.5}\label{eq:derivatives}\] Hence \(P_\tau\) is strictly convex exactly when the fibre profile is nonuniform.

<!--block:B0021-->
By [\[prop:natural\]](#prop:natural), the variational functional for \(F_\tau\) equals that for the full shift on \(S^\Z\) with the one-coordinate potential \(t\log k_{\tau(s)}\). For any shift-invariant measure \(\nu\), its entropy rate is bounded by the Shannon entropy \(H(p)\) of its one-symbol marginal \(p\). The finite-alphabet Gibbs inequality gives \[H(p)+t\sum_{s\in S}p(s)\log k_{\tau(s)}
 \leq\log\sum_{s\in S}k_{\tau(s)}^t,
 \tag{3.6}\label{eq:gibbs}\] with equality only at [\[eq:pt\]](#eq:pt); entropy-rate equality then forces the Bernoulli process. This proves [\[eq:pressure\]](#eq:pressure) and uniqueness.

<!--block:B0022-->
Summing [\[eq:pt\]](#eq:pt) over a fibre gives [\[eq:rt\]](#eq:rt). Differentiating the finite exponential sum yields [\[eq:derivatives\]](#eq:derivatives). Its variance vanishes for one, hence every, \(t\) exactly when all values \(\log k_z\) coincide.

<!--block:B0023-->
Two parameter values have immediate meanings: \[P_\tau(0)=\log|S|,
 \qquad
 P_\tau(-1)=\log|Z|.
 \tag{3.7}\label{eq:end-alphabets}\] Thus the curve contains both alphabet sizes, while its curvature records the nonuniform distribution of information loss.

<!--block:B0024-->
The next corollary explicitly uses the main entropy formulae of \[@MartinsMattosVarao2026\]; it is not a reattribution of those formulae.

<!--block:B0025-->
\[cor:folding\] For the equilibrium state \(\mu_t\), \[h_{\mu_t}(F_\tau)=P_\tau(t)-tP_\tau'(t),
 \qquad
 \cF_{\mu_t}(F_\tau)=P_\tau'(t).
 \tag{3.8}\label{eq:entropy-bridge}\]

<!--block:B0026-->
Theorem A of \[@MartinsMattosVarao2026\] identifies metric entropy with \(H(p_t)\). From [\[eq:pt\]](#eq:pt), \(-\log p_t(s)=P_\tau(t)-t\log k_{\tau(s)}\), so averaging gives the first identity. Their Theorem B writes folding entropy as the average conditional entropy inside the fibres. Equation [\[eq:pt\]](#eq:pt) is uniform within each fibre, so the conditional entropy over \(z\) is \(\log k_z\). Averaging with \(r_t\) and using [\[eq:derivatives\]](#eq:derivatives) gives the second identity.

<!--block:B0027-->
# Weighted periodic data and profile rigidity

<!--block:B0028-->
The same exponential sum in [\[eq:q\]](#eq:q) appears without a variational argument when periodic points are weighted by their local degrees.

<!--block:B0029-->
\[prop:periodic\] For every \(n\geq1\) and \(t\in\R\), \[\sum_{x\in\Fix(F_\tau^n)}
 \exp\!\left(t\sum_{j=0}^{n-1}\phi_\tau(F_\tau^j x)\right)
 =Q_\tau(t)^n.
 \tag{4.1}\label{eq:periodic}\] In particular \(|\Fix(F_\tau^n)|=|S|^n\).

<!--block:B0030-->
Each word \((s_0,\ldots,s_{n-1})\in S^n\) determines one fixed point of \(F_\tau^n\) by the unambiguous coordinate formula \[x_i=s_{i\bmod n}\quad(i\geq0),
 \qquad
 x_{-j}=\tau(s_{(-j)\bmod n})\quad(j\geq1),
 \tag{4.2}\label{eq:periodic-coordinates}\] where residues lie in \(\{0,\ldots,n-1\}\). Every fixed point arises uniquely in this way. Its local degrees at times \(0,\ldots,n-1\) are \(k_{\tau(s_{n-1})},k_{\tau(s_0)},\ldots,k_{\tau(s_{n-2})}\), a cyclic permutation of the advertised list. Summing the product of their \(t\)th powers over \(S^n\) factorizes as \((\sum_s k_{\tau(s)}^t)^n=Q_\tau(t)^n\).

<!--block:B0031-->
The weighted orbit sums also give a closed zeta function. For \(|u|<Q_\tau(t)^{-1}\), set \[\zeta_\tau(t,u)=\exp\!\left(
 \sum_{n\geq1}\frac{u^n}{n}
 \sum_{x\in\Fix(F_\tau^n)}e^{tS_n\phi_\tau(x)}
 \right).\]

<!--block:B0032-->
\[cor:zeta\] For every real \(t\), \[\zeta_\tau(t,u)=\frac{1}{1-uQ_\tau(t)}.
 \tag{4.3}\label{eq:zeta}\] Its smallest positive pole is \(e^{-P_\tau(t)}\).

<!--block:B0033-->
Insert [\[eq:periodic\]](#eq:periodic) and use \(\sum_{n\geq1}(uQ)^n/n=-\log(1-uQ)\).

<!--block:B0034-->
We now compare two surjections \(\tau:S\to Z\) and \(\kappa:T\to W\). A topological conjugacy means a homeomorphism \(H:X_\tau\to X_\kappa\) satisfying \(HF_\tau=F_\kappa H\).

<!--block:B0035-->
\[thm:rigidity\] The following are equivalent.

<!--block:B0036-->
1.  \((X_\tau,F_\tau)\) and \((X_\kappa,F_\kappa)\) are topologically conjugate.

2.  The fibre-size multisets \(\{k_z:z\in Z\}\) and \(\{|\kappa^{-1}(w)|:w\in W\}\) agree.

3.  \(P_\tau(t)=P_\kappa(t)\) for every \(t\in\R\).

<!--block:B0037-->
Equal profiles admit a one-block conjugacy on the negative and nonnegative coordinates separately.

<!--block:B0038-->
Conjugacy preserves local degree pointwise because it bijects the preimage sets of corresponding points. It also bijects fixed points. There is one fixed point for each \(s\in S\), and that point has degree \(k_{\tau(s)}\). Consequently the number of fixed points of degree \(k\) is \[N_k=k\,m_k.
 \tag{4.4}\label{eq:degree-hist}\] The conjugacy-invariant histogram \(N_k\) recovers every multiplicity \(m_k=N_k/k\), proving \((1)\Rightarrow(2)\).

<!--block:B0039-->
If the profiles agree, choose a bijection \(\beta:Z\to W\) matching equal-size fibres and, for each \(z\), a bijection \(\alpha_z:\tau^{-1}(z)\to\kappa^{-1}(\beta z)\). Put \(\alpha(s)=\alpha_{\tau(s)}(s)\) and define \[H(x)_i=
 \begin{cases}
 \beta(x_i),&i<0,\\
 \alpha(x_i),&i\geq0.
 \end{cases}
 \tag{4.5}\label{eq:one-block-conj}\] The relation \(\kappa\alpha=\beta\tau\) shows directly from [\[eq:zip-map\]](#eq:zip-map) that \(HF_\tau=F_\kappa H\). Coordinatewise inverse bijections make \(H\) a conjugacy, proving \((2)\Rightarrow(1)\).

<!--block:B0040-->
Equal profiles give equal sums in [\[eq:q\]](#eq:q), hence \((2)\Rightarrow(3)\). Conversely suppose the pressure curves agree and set \[R_\tau(u)=\exp P_\tau(u-1)=\sum_{k\geq1}m_k k^u.
 \tag{4.6}\label{eq:dirichlet}\] The largest fibre size is \(K=\lim_{u\to\infty}R_\tau(u)^{1/u}\), and its multiplicity is \(m_K=\lim_{u\to\infty}R_\tau(u)/K^u\). Subtract \(m_KK^u\) and repeat on the finite remaining sum. This recovers the whole profile from the curve and proves \((3)\Rightarrow(2)\).

<!--block:B0041-->
The fixed-point argument already proves profile necessity. The pressure formulation is stronger as a thermodynamic representation: one convex function simultaneously carries the profile, equilibrium degree averages, and the spectrum proved next.

<!--block:B0042-->
# The degree-exponent spectrum

<!--block:B0043-->
For \(x\in X_\tau\), define the forward degree exponent when the limit exists: \[\lambda(x)=\lim_{n\to\infty}\frac1n
 \log\prod_{j=0}^{n-1}d_\tau(F_\tau^j x),
 \qquad
 E_\tau(\alpha)=\{x:\lambda(x)=\alpha\}.
 \tag{5.1}\label{eq:level}\] We use Bowen’s topological entropy \(h_B\) for a possibly noncompact level set \[@Bowen1973\].

<!--block:B0044-->
Equip \(X_\tau\) with the compatible product metric \[\rho(x,y)=2^{-N(x,y)},\qquad
 N(x,y)=\min\{|i|:x_i\ne y_i\},\] with \(N(x,x)=\infty\) and the convention \(2^{-\infty}=0\). Write \(B_n(x,\epsilon)=\{y:\rho(F_\tau^j x,F_\tau^j y)<\epsilon
\text{ for }0\leq j<n\}\).

<!--block:B0045-->
\[lem:boundary\] For every \(x\) and \(n\geq2\), \[\sum_{j=0}^{n-1}\phi_\tau(F_\tau^j x)
 =\log k_{x_{-1}}+
 \sum_{i=0}^{n-2}\log k_{\tau(x_i)}.
 \tag{5.2}\label{eq:boundary}\] The first term is uniformly bounded. Moreover, for every \(M\geq1\), \[B_n(x,2^{-M})=
 \left\{y:\begin{array}{ll}
 y_i=x_i&\text{for }-M\leq i\leq-1,\\
 y_i=x_i&\text{for }0\leq i\leq n+M-1
 \end{array}\right\}.\] Consequently the negative coordinates and the \(M\) terminal future symbols contribute only factors \(|Z|^M\) and \(|S|^M\) to Bowen covers. The Bowen entropy of \(E_\tau(\alpha)\) therefore equals the digit-average level-set entropy in the one-sided full shift on \(S\) for the weights \(a_s=\log k_{\tau(s)}\).

<!--block:B0046-->
The degree at time zero is \(k_{x_{-1}}\). For \(j\geq1\), the symbol at coordinate \(-1\) of \(F_\tau^j x\) is \(\tau(x_{j-1})\), giving [\[eq:boundary\]](#eq:boundary). Since the alphabet is finite, the boundary term divided by \(n\) tends uniformly to zero.

<!--block:B0047-->
For the displayed Bowen-cylinder identity, the inequality \(\rho(F_\tau^j x,F_\tau^j y)<2^{-M}\) means agreement in the coordinate window \([-M,M]\) at time \(j\). The nonnegative part of that window reads the initial future coordinates \(j,\ldots,j+M\); as \(0\leq j<n\), their union is \([0,n+M-1]\). At time zero the negative part reads exactly the initial block \([-M,-1]\). At later times its surviving old-past coordinates remain inside that block, while every future coordinate that has crossed the zipper is seen only through \(\tau\) and is already fixed by agreement of the future symbols. This proves both inclusions.

<!--block:B0048-->
Thus, relative to a length-\(n\) future cylinder, passage to an \((n,2^{-M})\) Bowen ball requires at most \(|Z|^M|S|^M\) refinements, a factor independent of \(n\). Together with the uniform boundary term, this proves the asserted entropy reduction.

<!--block:B0049-->
Let \(\Delta(S)\) and \(\Delta(Z)\) denote the corresponding probability simplices, and write \(H\) for Shannon entropy with natural logarithms.

<!--block:B0050-->
\[thm:spectrum\] Put \(k_{\min}=\min_z k_z\) and \(k_{\max}=\max_z k_z\). If \(\alpha\notin[\log k_{\min},\log k_{\max}]\), then \(E_\tau(\alpha)=\varnothing\). For every \(\alpha\) in this interval, \[\begin{aligned}
 h_B(E_\tau(\alpha))
 &=\max_{p\in\Delta(S):\,\sum_s p_s\log k_{\tau(s)}=\alpha}H(p)
 \tag{5.3}\label{eq:spectrum-s}\\
 &=\max_{r\in\Delta(Z):\,\sum_z r_z\log k_z=\alpha}
 \bigl(H(r)+\alpha\bigr)
 \tag{5.4}\label{eq:spectrum-z}\\
 &=\inf_{t\in\R}\bigl(P_\tau(t)-t\alpha\bigr).
 \tag{5.5}\label{eq:legendre}\end{aligned}\] For an interior \(\alpha\) and a nonuniform profile, the infimum is attained at the unique \(t\) satisfying \(P_\tau'(t)=\alpha\).

<!--block:B0051-->
By [\[lem:boundary\]](#lem:boundary), it suffices to work with future words and the digit weights \(a_s\). We spell out the Carathéodory step because fixed-length type counts alone would give only capacity entropy. Put \[H_\alpha=\max\{H(p):p\in\Delta(S),\ \textstyle\sum_s p_sa_s=\alpha\}\] when the constraint is feasible. For \(\eta>0\), let \(H_{\alpha,\eta}\) be the same maximum with the equality replaced by \(|\sum_s p_sa_s-\alpha|\leq\eta\). Compactness and continuity give \(H_{\alpha,\eta}\downarrow H_\alpha\) as \(\eta\downarrow0\).

<!--block:B0052-->
For \(N\geq1\), let \(Y_{N,\eta}\) be the set of future sequences whose length-\(n\) digit average lies in that \(\eta\)-window for every \(n\geq N\). The exact average level set is contained in \(\bigcup_NY_{N,\eta}\). The number of length-\(n\) words in the window is at most \[(n+1)^{|S|}\exp(nH_{\alpha,\eta}),\] by the method of types. Fixing the metric scale \(2^{-M}\) adds at most the factor \(|Z|^M|S|^M\) from [\[lem:boundary\]](#lem:boundary). Hence, for every \(s>H_{\alpha,\eta}\), a fixed-length cover with arbitrarily large \(n\geq N\) has Bowen–Carathéodory sum bounded by \[|Z|^M|S|^M(n+1)^{|S|}
 \exp\bigl(-n(s-H_{\alpha,\eta})\bigr),\] which tends to zero. Countable stability of Bowen entropy gives the upper bound \(h_B(E_\tau(\alpha))\leq H_{\alpha,\eta}\); now let \(\eta\downarrow0\).

<!--block:B0053-->
For the reverse bound, fix a feasible \(p\) and denote by \(\nu_p\) the probability law obtained by putting a Bernoulli-\(p\) law on the future coordinates while fixing one arbitrary past. Almost every future is \(p\)-generic and hence belongs to \(E_\tau(\alpha)\). For every fixed \(M\), the Bowen-cylinder identity and the Shannon law of large numbers give, at almost every such point, \[\lim_{n\to\infty}-\frac1n
 \log\nu_p\bigl(B_n(x,2^{-M})\bigr)=H(p).\] The entropy distribution principle therefore yields \(h_B(E_\tau(\alpha))\geq H(p)\). Maximizing over feasible \(p\) proves [\[eq:spectrum-s\]](#eq:spectrum-s). If the constraint is infeasible, no digit average can converge to \(\alpha\); its feasible interval is the convex hull of the weights, namely \([\log k_{\min},\log k_{\max}]\).

<!--block:B0054-->
Given \(p\), group it by fibres: \(r_z=\sum_{s\in\tau^{-1}(z)}p_s\). The entropy chain rule gives \[H(p)=H(r)+\sum_z r_z H(p(\,\cdot\mid z))
 \leq H(r)+\sum_z r_z\log k_z=H(r)+\alpha.
 \tag{5.6}\label{eq:conditional-max}\] Equality holds by distributing mass uniformly within each fibre. This proves [\[eq:spectrum-z\]](#eq:spectrum-z).

<!--block:B0055-->
For any \(t\) and any feasible \(p\), the Gibbs variational inequality [\[eq:gibbs\]](#eq:gibbs) rearranges to \(H(p)\leq P_\tau(t)-t\alpha\). Hence the maximum is at most the infimum in [\[eq:legendre\]](#eq:legendre). If \(\alpha\) is interior, continuity and strict monotonicity of \(P_\tau'\) give a parameter \(t\) with \(P_\tau'(t)=\alpha\); the distribution \(p_t\) is feasible and equality in [\[eq:gibbs\]](#eq:gibbs) proves the reverse inequality. At the endpoints, take \(t\to-\infty\) or \(t\to+\infty\) and use continuity of the constrained maximum.

<!--block:B0056-->
At either endpoint \(k\in\{k_{\min},k_{\max}\}\), the formula retains every fibre of that extremal size: \[h_B(E_\tau(\log k))=\log(km_k)\] (with the two endpoint statements coinciding in the uniform case). The spectrum reaches the full entropy \(\log|S|\) at \[\alpha=P_\tau'(0)=\sum_z\frac{k_z}{|S|}\log k_z.\] Together with [\[cor:folding\]](#cor:folding), the tangent parameter describes both the folding entropy of \(\mu_t\) and the degree exponent of its generic points.

<!--block:B0057-->
# Two four-symbol controls

<!--block:B0058-->
The ordinary topological entropy cannot distinguish fibre profiles with the same forward alphabet size. Consider two surjections with \(|S|=4\): \[\mathbf k=(1,3),
 \qquad
 \widetilde{\mathbf k}=(2,2).\] Both full zip shifts have topological entropy \(\log4\), but \[P_{(1,3)}(t)=\log(1+3^{t+1}),
 \qquad
 P_{(2,2)}(t)=(t+2)\log2.
 \tag{6.1}\label{eq:example-pressure}\] The first curve is strictly convex, while the second is affine. Theorem [\[thm:rigidity\]](#thm:rigidity) therefore separates the systems even though their natural extensions are both the full four-shift.

<!--block:B0059-->
For the nonuniform profile \((1,3)\), write \(\theta=\alpha/\log3\). Formula [\[eq:spectrum-z\]](#eq:spectrum-z) becomes \[h_B(E(\alpha))
 =-\theta\log\theta-(1-\theta)\log(1-\theta)+\alpha,
 \qquad 0\leq\alpha\leq\log3.
 \tag{6.2}\label{eq:binary-spectrum}\] At \(\alpha=0\) the level set uses the single symbol over the one-element fibre and has entropy zero. At \(\alpha=\log3\) it uses the three symbols over the three-element fibre and has entropy \(\log3\). The maximum \(\log4\) occurs at \(\theta=3/4\), the fibre frequency induced by the uniform distribution on the four future symbols.

<!--block:B0060-->
For the uniform profile \((2,2)\), every point has degree exponent \(\log2\). The spectrum consists of one level set of entropy \(\log4\), matching the affine pressure and zero curvature. This is the degenerate case adjacent to the uniform \(n\)-to-one theory of \[@MehdipourJangjooye2025\].

<!--block:B0061-->
@lYY@ Quantity & profile \((1,3)\) & profile \((2,2)\)  
Natural extension & full four-shift & full four-shift  
\(h_{\rm top}\) & \(\log4\) & \(\log4\)  
degree range & \(\{1,3\}\) & \(\{2\}\)  
\(P(t)\) & \(\log(1+3^{t+1})\) & \((t+2)\log2\)  
\(P''(t)\) & positive & zero  
degree-exponent interval & \([0,\log3]\) & \(\{\log2\}\)  

<!--block:B0062-->
# Source boundary and limitations

<!--block:B0063-->
The formal zip-shift definitions, local homeomorphism results, sliding block codes, and periodic-point setting belong to \[@LameiMehdipour2025\]. Uniform \(n\)-to-one intrinsic ergodicity and square-entropy classification are treated by \[@MehdipourJangjooye2025\]. Most directly, \[@MartinsMattosVarao2026\] study exactly the map [\[eq:zip-map\]](#eq:zip-map) under the name extended shift and prove the Bernoulli metric- and folding-entropy formulae used in [\[cor:folding\]](#cor:folding). We do not present the natural extension, ordinary entropy, local degree, or their Theorems A–B as isolated paper claims.

<!--block:B0064-->
Recent adjacent directions include zip cellular automata \[@MehdipourSalarinoghabiGibrim2026\] and symbolic encodings of finite-to-one local homeomorphisms \[@MehdipourLamei2026\]. In another exact-family neighbour, \[@LameiMehdipourVargas2025\] introduce S-expansiveness for local homeomorphisms, prove S-expansiveness and shadowing for the full zip shifts considered there, and establish a factor theorem for S-expansive local homeomorphisms under their stated hypotheses. Those S-expansiveness, shadowing, and factor results belong to them and are not claimed here. These works motivate the system class but do not alter the scope of the proofs here.

<!--block:B0065-->
The official UFV researcher profile for Pouya Mehdipour lists a 2024–present project entitled *Formalismo Termodinâmico para Mapas Zip Shift* \[@MehdipourUFVProject2024\]. Its public description says that the project aims to study and formulate thermodynamic formalism for zip-shift maps, with the principal objective of showing that these maps represent systems with phase transitions. This is a project objective, not theorem text: the public page supplies no theorem-level statement that can be compared with the formulae here. It nevertheless creates a high collision risk for the pressure portion, so a specialist exact-neighbour gate remains required.

<!--block:B0072-->
Theorem-component comparison from the frozen local source ledger (cutoff 26 August 2026). *Not located* is search-bounded and is not a priority or clearance claim.

<!--block:B0073-->
| Component and nearest record | Documented overlap | Documented difference | Status in this manuscript |
|---|---|---|---|
| Zip-shift setup; [@LameiMehdipour2025] | Definitions, local-homeomorphism structure, sliding-block framework, and periodic setting | Used as infrastructure rather than restated as an isolated result | Owner-subtracted |
| Uniform theory; [@MehdipourJangjooye2025] | Full uniform \(n\)-to-one systems, square entropy, and intrinsic ergodicity | Nonuniform fibre profiles and the varying local-degree observable | Adjacent owner-subtracted case |
| Bernoulli entropies; [@MartinsMattosVarao2026] | Metric- and folding-entropy formulae for the same map under the name extended shift | Equilibrium weights are substituted and related to \(P_\tau'\); the prior entropy formulae themselves are not reclaimed | Prior theorem used explicitly |
| S-expansive topology; [@LameiMehdipourVargas2025] | Full-zip-shift topology, shadowing, S-expansiveness, and a factor theorem | No S-expansiveness, shadowing, or factor result is asserted here | Documented distinct theorem surface |
| Pressure, equilibrium, and curvature; [@MehdipourUFVProject2024] | The public project objective names thermodynamic formalism and phase transitions for zip shifts | No public theorem text is available for formula-by-formula comparison | **HIGH collision risk**; specialist gate and external HOLD |
| Weighted periodic/profile rigidity | The formal periodic setting is prior; no exact weighted profile-recovery theorem was located in the bounded ledger | Fixed-point degree histograms and the finite exponential sum recover the fibre profile inside the stated family | Difference documented only against located sources; not priority-cleared |
| Degree-exponent spectrum; [@Bowen1973; @BarreiraSaussolSchmeling2002] | Bowen entropy and digit-frequency multifractal methods are prior | The stated local-degree spectrum is specialized to the full zip-shift model; no exact zip-shift theorem was located in the bounded ledger | Search-bounded difference; not priority-cleared |

<!--block:B0074-->
: Theorem-component comparison from the frozen local source ledger. {#tab:component-comparison}

<!--block:B0066-->
Within that owner subtraction, the manuscript’s residual mathematical package is the intrinsic degree pressure, its equilibrium and curvature, the full degree-exponent spectrum, and the equivalence between pressure-profile recovery and topological conjugacy.

<!--block:B0067-->
Three restrictions are important. First, the space is full: future symbols have no transition constraints. For a proper zip subshift, pressure is controlled by a weighted transition operator rather than the scalar sum \(Q_\tau(t)\). Second, the conjugacy classification is internal to full one-block zip shifts; it does not classify arbitrary finite-to-one local homeomorphisms. Third, the bounded source search through 26 August 2026 found no primary article stating the exact pressure/spectrum/profile package, but such a search is not a priority certificate and cannot resolve the public UFV project at theorem level. External release therefore remains on hold for the specialist exact-neighbour audit of current zip-shift thermodynamic work.

<!--block:B0068-->
The companion script exhausts periodic words through length five for several integer weights, checks profile recovery on finite examples, differentiates the displayed pressure numerically against its exact mean/variance formulae, and verifies the binary spectrum's entropy maximum. It also checks the profile \((1,1,2,4,4)\), whose minimal and maximal fibre sizes both repeat: the endpoint symbol masses are exactly \(1\cdot2=2\) and \(4\cdot2=8\), and the stable shifted pressure limits give the corresponding Legendre values \(\log2\) and \(\log8\). These are regression checks only; all formulae are proved symbolically in the manuscript.

<!--block:B0069-->
# Conclusion

<!--block:B0070-->
For a nonuniform full zip shift, local degree is not merely a pointwise topological invariant. Its logarithm generates a pressure curve that simultaneously determines equilibrium measures, folding averages, degree fluctuations, weighted periodic data, and the Bowen-entropy spectrum of orbit exponents. The finite exponential sum behind that curve also recovers every fibre multiplicity, yielding a complete conjugacy invariant within the full one-block family.

<!--block:B0071-->
The full-system assumption makes the pressure scalar and the spectrum a finite-dimensional entropy maximization. A next step is to replace the full future shift by a mixing SFT and determine which parts of profile recovery survive when the degree potential interacts with transition constraints. That extension is outside the present theorem contract.
