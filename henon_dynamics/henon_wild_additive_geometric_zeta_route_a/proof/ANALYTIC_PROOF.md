# Wild additive dynamics: proof package

## Claim, assumptions and status

Status: **PROVABLE AS STATED**. Fix any prime $p$, including $2$, and the autonomous map $f(x)=x+x^p$ on $\mathbb A^1(\overline{\mathbb F}_p)$. Iteration number $n\ge1$ is the dynamical clock; extension degree $r\ge1$ is a separate arithmetic clock. No finite-field cutoff appears in the theorem. All complex generating functions count geometric points unless explicitly labelled scheme-theoretic.

Write $v=v_p(n)$, $e=p^v$, $n=em$ with $p\nmid m$. Then the fixed scheme has length $p^n$, every geometric point has multiplicity $p^e$, and there are exactly $N_n=p^{n-e}$ geometric fixed points. For every extension degree,

$$N_{n,r}=\#\{x\in\mathbb F_{p^r}:f^n(x)=x\}=p^{\deg\gcd((1+T)^n-1,T^r-1)}.$$

These counts determine all primitive periods and exact residue degrees. The geometric Artin--Mazur zeta has a meromorphic natural boundary at $|z|=1/p$, whereas the length-counting series is the rational function $(1-pz)^{-1}$. The latter cannot replace the former's primitive-orbit determinant. This is a complete source theorem, not a target Riemann determinant or a literature-priority claim.

## Notation and dependency map

For $Q(T)=\sum q_jT^j\in\mathbb F_p[T]$, put $L_Q(X)=\sum q_jX^{p^j}$ and write $F(X)=X^p$. Composition satisfies $L_{AB}=L_A\circ L_B$ and addition satisfies $L_{A+B}=L_A+L_B$. The symbol $p^e$ means $p^{p^{v_p(n)}}$, not $p^{v_p(n)}$.

1. Binomial arithmetic in $\mathbb F_p[T]$ gives the inseparable exponent and geometric count.
2. Euclidean division under the linearized-polynomial correspondence gives the complete extension-field gcd formula; no semisimplicity or normal-basis assumption is needed.
3. Finite permutation cycles give both Möbius inversions and the primitive Euler product.
4. A telescoping valuation expansion gives a normally convergent Lambert series and controlled tail.
5. Radial limits at every nontrivial $p$-power root of unity give noninteger logarithmic-derivative residues. Local meromorphicity would force integer orders; density then proves the natural boundary for the zeta itself.

## 1. Iteration, scheme length and reduced counts

The identity $f=1+F$ in the commutative ring of additive endomorphisms gives $f^n-\mathrm{id}=L_{Q_n}$ with $Q_n(T)=(1+T)^n-1$. In characteristic $p$,

$$Q_n(T)=((1+T)^m-1)^e=T^eH_m(T)^e,\qquad H_m(T)=\frac{(1+T)^m-1}{T}.$$

The polynomial $H_m$ has degree $m-1$ and constant coefficient $m\ne0$. Consequently $L_{H_m^e}$ has nonzero derivative $m^e$ and degree $p^{e(m-1)}=p^{n-e}$. Moreover,

$$L_{Q_n}(X)=L_{H_m^e}(X)^{p^e}.$$

Over the algebraic closure, $L_{H_m^e}$ has exactly its degree many distinct roots. Its $p^e$-th power has those same roots, each with multiplicity $p^e$. This proves all three counts, including $m=1$: then $H_1=1$, the unique fixed point is $0$, and $f^{p^v}-\mathrm{id}=X^{p^{p^v}}$. In particular there are no nonzero points of pure $p$-power dynamical period. The differential of $f$ is $1$ at every point, so every periodic multiplier is $1$; multiplicity is a wild algebraic effect, not positive real Lyapunov stability.

## 2. Every extension, without an implicit semisimplicity assumption

Let $A=BQ+R$ be Euclidean division in $\mathbb F_p[T]$. At every common root of $L_A$ and $L_B$, the identity $L_A=L_Q\circ L_B+L_R$ shows that $L_R$ also vanishes; the converse follows from the same identity. Iterating Euclid proves that the common roots of $L_A,L_B$ are exactly the roots of $L_{\gcd(A,B)}$, where the gcd is monic. Apply this to $A=Q_n$ and $B=T^r-1$. The latter linearized polynomial is $X^{p^r}-X$, whose roots are precisely $\mathbb F_{p^r}$.

If $g=\gcd(Q_n,T^r-1)$, then $g(0)\ne0$ because $T\nmid T^r-1$. Thus $L_g$ is separable of degree $p^{\deg g}$, proving the claimed extension count even when $p\mid r$ or $p\mid n$. The unreduced polynomial $T^r-1$ must not be replaced by its radical: its repeated factors contain genuine extension information in these cases.

The least field containing all geometric fixed points can also be characterized exactly. For $m>1$, $H_m$ is squarefree because $(1+T)^m-1$ has derivative $m(1+T)^{m-1}$ and shares no root with that derivative. Let $o_m$ be the multiplicative order of the unit $T$ in the finite reduced algebra $\mathbb F_p[T]/(H_m)$. This order is prime to $p$. All $N_n$ roots belong to $\mathbb F_{p^r}$ exactly when $H_m^e\mid T^r-1$: the gcd formula has degree at most $n-e$, with equality precisely in that case. Factoring $T^r-1=(T^{r/p^{v_p(r)}}-1)^{p^{v_p(r)}}$ shows that this holds exactly when $eo_m\mid r$. Hence the least splitting degree is $eo_m$. For $m=1$ the root set is $\{0\}$ and the least field is $\mathbb F_p$, not a fictitious degree-$e$ extension.

## 3. Primitive cycles and the two clocks

Every $\operatorname{Fix}(f^n)$ is finite and $f$ acts there as a permutation because $f^n=\mathrm{id}$ on that set. If $P_n$ counts forward-oriented primitive cycles of least period $n$, retaining reversal as distinct when it is distinct, then

$$N_n=\sum_{d\mid n}dP_d,\qquad P_n=\frac1n\sum_{d\mid n}\mu(n/d)N_d\in\mathbb Z_{\ge0}.$$

There is no independent geometric reversal involution being imposed. All geometric orbit weights are $1$, and repetitions have exactly the displayed divisor multiplicities. Let $E_{n,r}$ count points of exact dynamical period $n$ and exact degree $r$ over $\mathbb F_p$. Since $f$ is defined over $\mathbb F_p$, it never increases residue degree. Along a periodic cycle the inclusions return to the original field, so every point in the cycle has the same residue field. Double Möbius inversion therefore gives

$$E_{n,r}=\sum_{a\mid n}\sum_{b\mid r}\mu(n/a)\mu(r/b)N_{a,b},\qquad E_{n,r}/n\in\mathbb Z_{\ge0}.$$

This counts $f$-cycles whose points have exact residue degree $r$. It is not the count of orbits of the joint $\mathbb Z^2$-action generated by $f$ and $F$, which could identify several $f$-cycles. Extension degree, dynamical least period and rational prime are not interchangeable labels.

Because $0\le N_n\le p^n$, the series $\sum N_nz^n/n$ converges absolutely for $|z|<1/p$. Since $N_n=p^{n-1}$ for $p\nmid n$, its radius is exactly $1/p$. The primitive product is consequently valid there:

$$\zeta_p(z)=\exp\left(\sum_{n\ge1}N_n\frac{z^n}{n}\right)=\prod_{n\ge1}(1-z^n)^{-P_n}.$$

Absolute convergence follows from $nP_n\le N_n$ and $|z|<1/p<1$. Exchanging sums yields $\sum_dP_d\sum_{k\ge1}z^{dk}/k=\sum_nN_nz^n/n$. The reciprocal $D_p=1/\zeta_p$ is the native primitive determinant germ; it is not assumed to be an operator Fredholm determinant.

## 4. Lambert expansion and a quantitative interior tail

Set $w=pz$, $\mathcal Z_p(w)=\zeta_p(w/p)$ and

$$A_p(w)=w\frac{\mathcal Z_p'(w)}{\mathcal Z_p(w)}=\sum_{n\ge1}p^{-p^{v_p(n)}}w^n.$$

Define $c_0=p^{-1}$ and, for $k\ge1$, $c_k=p^{-p^k}-p^{-p^{k-1}}<0$. The coefficient identity $p^{-p^{v_p(n)}}=\sum_{k=0}^{v_p(n)}c_k$ gives

$$A_p(w)=\sum_{k\ge0}c_k\frac{w^{p^k}}{1-w^{p^k}}\qquad(|w|<1).$$

For $0<\rho<1$, $|w|\le\rho$, and integer $K\ge0$, the tail obeys

$$\left|\sum_{k>K}c_k\frac{w^{p^k}}{1-w^{p^k}}\right|\le p^{-p^K}\frac{\rho^{p^{K+1}}}{1-\rho^{p^{K+1}}}.$$

Indeed $\sum_{k>K}|c_k|=p^{-p^K}$, and $\rho^h/(1-\rho^h)$ decreases with $h$. This proves normal convergence on compact subdisks and justifies the coefficient rearrangement independently of formal power-series arithmetic.

Using the branch of $\log(1-w^{p^k})$ vanishing at $0$, integration also gives the normally convergent local expression

$$\log\mathcal Z_p(w)=-\sum_{k\ge0}\frac{c_k}{p^k}\log(1-w^{p^k}).$$

No global branch is chosen across $|w|=1$.

## 5. Meromorphic natural boundary for the zeta, not only its derivative

Let $\omega$ have exact order $p^K$ with $K\ge1$. For real $0<r<1$, terms $k<K$ satisfy $\omega^{p^k}\ne1$ and therefore tend to zero after multiplication by $1-r$. For $k\ge K$, $\omega^{p^k}=1$ and

$$0\le(1-r)\frac{r^{p^k}}{1-r^{p^k}}\le1,\qquad\lim_{r\uparrow1}(1-r)\frac{r^{p^k}}{1-r^{p^k}}=p^{-k}.$$

The dominating sequence $|c_k|$ is summable, so dominated convergence proves

$$\lim_{r\uparrow1}(1-r)A_p(r\omega)=S_K:=\sum_{k\ge K}\frac{c_k}{p^k}<0.$$

The strict bounds

$$0<-S_K\le p^{-K}\sum_{k\ge K}|c_k|=p^{-K-p^{K-1}}<1$$

are valid also for $p=2,K=1$. Suppose $\mathcal Z_p$ admitted a meromorphic continuation to a neighborhood of $\omega$. It is not identically zero because it agrees with the exponential germ inside the disk. The local order $j=\operatorname{ord}_{\omega}\mathcal Z_p$ is an integer, and its logarithmic derivative has residue $j$. On the radial path,

$$\lim_{r\uparrow1}(r\omega-\omega)\frac{\mathcal Z_p'(r\omega)}{\mathcal Z_p(r\omega)}=-S_K\in(0,1),$$

contradicting integrality of $j$. This excludes meromorphic continuation at every such $\omega$, not just a particular branch of a fractional product. Nontrivial roots of $p$-power order are dense on the unit circle. A meromorphic continuation through any other boundary point would exist in a disk intersecting one of these roots and agree with the original germ on the connected inner overlap, giving the forbidden continuation there. Hence the entire circle is a meromorphic natural boundary. The reciprocal has the same obstruction, since the reciprocal of a nonzero meromorphic germ is meromorphic.

## 6. Length counting, controls and the scoped obstruction

Counting fixed-scheme lengths gives

$$\zeta^{\mathrm{len}}_p(z)=\exp\left(\sum_{n\ge1}p^n\frac{z^n}{n}\right)=\frac1{1-pz}.$$

It has the scalar determinant $1-pz$; this length-counting identity does not supply a geometric-orbit trace formula. At the first iterate the discrepancy is already $p$ versus $1$. In HEN-O368, no entire or meromorphic continuation in the same $z$-variable can equal $\zeta_p$ or $D_p$ on the initial disk. Multiplication by an entire zero-free function cannot cure the obstruction because division by that function would provide a forbidden continuation. An operator holomorphic only on the original disk is not excluded. No blanket obstruction to unrelated variables, renormalizations, nonholomorphic boundary values or genuinely different objects is asserted.

For the simpler parent $g_0(x)=x^p$, $g_0^n-x$ has derivative $-1$ and exactly $p^n$ roots, so geometric and length zeta coincide. For the neighboring family $g_a(x)=ax+x^p$ with $a\in\mathbb F_p^\times$ of order $d$, the same binomial calculation gives $p^n$ roots if $d\nmid n$, and $p^{n-p^{v_p(n)}}$ roots if $d\mid n$. Thus the derivative/unit-order gate, not a fitted zero pattern, determines the repeated-point correction. A field has prime characteristic; mixed composite labels are not admissible characteristics. Prime powers describe extension sizes over a fixed prime, not new time owners.

These three controls do not establish a rational-prime/primitive-orbit correspondence or complete the evaluator's six A1 controls. The strict tuple remains $(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},\mathrm{A4\_FAIL})$. All target claim flags and Route B remain false.

## Attribution, corrections and open risks

Bridy's 2012 theorem treats transcendence for $x^{p^m}+ax$ in odd characteristic; his 2016 Theorem 1.3 covers separable additive polynomials in every positive characteristic. Those results predate this package. The present proof uses direct valuation/Lambert residues for this frozen family and makes no priority claim for irrationality, transcendence or natural boundaries. Repository C204 already treats a single finite-dimensional finite-field linear system, C14 treats a chronological $S$-integer solenoid, C159 treats a Thue--Morse renewal natural boundary, and C382 treats reduced elliptic Frobenius fixed points. None supplies the geometric-versus-length and all-extension theorem for this wild additive owner; none is denied its prior contribution.

All theorem steps above are proved without numerical data or conditional external theorems. Finite computations are regression evidence only. Classical source selection and the absence of a rational-prime target bridge are acknowledged limitations. No current proof gap is hidden behind a numerical certificate.
