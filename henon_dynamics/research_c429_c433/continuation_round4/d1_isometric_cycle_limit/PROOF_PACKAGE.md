# Isometric finite-cycle limits: the measure bridge

## Claim

Let $(X,d)$ be a complete ultrametric space and let $T:X\to X$ be an isometry. Let $C_e$ be a nonempty finite single $T$-cycle, for every integer $e\geq1$, and let $\mu_e$ be its uniform probability measure. Put

$$
a_{d,e}:=\min\{d(x,y):x\in C_d,\ y\in C_e\},\qquad
\varepsilon_d:=\sup_{e>d}a_{d,e}.
$$

The sufficient contact criterion is

$$
\tag{CC}\varepsilon_d\longrightarrow0\qquad(d\longrightarrow\infty).
$$

Under (CC), the closure $B=\overline{\bigcup_e C_e}^{\,X}$ is compact. The sets $C_e$ converge in Hausdorff distance to a nonempty compact invariant set $A\subset B$, and $\mu_e$ converge weakly to a probability measure $\mu$ supported exactly on $A$. The restriction $T|_A$ is minimal and uniquely ergodic, with unique invariant probability $\mu$.

If, in addition, $\#C_e=p^e$ for one prime $p$, then $T|_A$ is conjugate either to addition by $1$ on a finite group $\mathbb Z/p^k\mathbb Z$, including the one-point case $k=0$, or to addition by $1$ on $\mathbb Z_p$. Its invariant probability is the corresponding Haar probability.

Condition (CC) is equivalent to Hausdorff-Cauchyness of the cycle sets. This is an exact criterion for this stronger, classical compact-limit mechanism; it is not asserted to be necessary for weak convergence in a larger compactification.

## Status

**PROVABLE AS STATED.** The proof below is independent of the proposed polynomial contact formula in the companion A1 lane. The application to the full Lindahl–Rivera-Letelier question is explicitly conditional on that separate input until its proof has been checked.

## Assumptions and notation

- An isometry means $d(Tx,Ty)=d(x,y)$ for all $x,y\in X$. Surjectivity on $X$ is not assumed.
- A single cycle is the orbit of one point under $T$, with its exact finite period. Different indices need not have different periods in the general theorem.
- $d_H$ is the Hausdorff distance on nonempty compact subsets of a metric space.
- For probability measures of finite first moment, $W_1$ is the infimum of $\int d(x,y)\,d\pi(x,y)$ over couplings $\pi$; $W_\infty$ is the infimum of the essential supremum of $d(x,y)$ over couplings.
- Weak convergence on a compact space means convergence against every real-valued continuous function. For a continuous function $f$ on a compact metric space, let $\omega_f(t)=\sup_{d(x,y)\leq t}|f(x)-f(y)|$.

## Proof strategy

A nearest pair of points from two cycles gives an orbit coupling whose every pair has the same distance. Thus one cross-cycle contact controls both entire supports and entire uniform measures. The resulting total boundedness, together with the stated completeness of $X$, proves the compactness needed for limiting arguments. Finite ultrametric partitions then prove the minimality, unique ergodicity and odometer description.

## Dependency map

1. Exact cycle coupling uses only the isometry and finite transitivity.
2. Compactness uses (CC), the finite cycle sets and completeness, not local compactness of $X$.
3. Measure convergence uses the coupling and the Riesz representation theorem on the proved compact metric space $B$.
4. Minimality uses the isometry and Hausdorff convergence of single cycles.
5. The inverse-limit description uses finite ultrametric partitions of $A$. The $p$-adic specialization uses only the exact cardinalities $p^e$.
6. Berkovich convergence uses continuity of the inclusion of a compact classical set. No metrizability of the whole Berkovich projective line is used.

## Proof

### 1. One pair controls both cycles

Let $C,D$ be finite single cycles of lengths $m,n$, respectively, and choose $x\in C$, $y\in D$ realizing $a=\min_{u\in C,v\in D}d(u,v)$. Set $L=\operatorname{lcm}(m,n)$. The measure

$$
\pi=\frac1L\sum_{j=0}^{L-1}\delta_{(T^jx,T^jy)}
$$

is a coupling of the two uniform cycle measures: each point of $C$ occurs exactly $L/m$ times in the first coordinate, and each point of $D$ exactly $L/n$ times in the second. Every pair in its support has distance $a$, since $T$ is an isometry. Every pair in $C\times D$ has distance at least $a$, by the definition of $a$. Therefore

$$
\tag{1}W_1(\mu_C,\mu_D)=W_\infty(\mu_C,\mu_D)=a.
$$

For each point $T^jx\in C$, the point $T^jy\in D$ has distance $a$; the same argument covers each point of $D$. Both directed Hausdorff distances are at most $a$ and at least the global minimum $a$. Hence

$$
\tag{2}d_H(C,D)=a.
$$

This step works in any metric space; the ultrametric hypothesis is not needed here. In particular, (CC) is equivalent to the usual Cauchy criterion for the sequence $(C_e)$ in Hausdorff distance.

### 2. Compact classical support is a conclusion

Fix $\eta>0$. Choose $d$ so large that $\varepsilon_d<\eta$. For every $e>d$, equation (2) implies that every point of $C_e$ is within distance $\eta$ of some point of the finite set $C_d$. Thus the tail $\bigcup_{e>d}C_e$ is covered by finitely many balls of radius $\eta$. The union of the finitely many earlier cycle sets is finite and has a finite such cover as well. The full union $\bigcup_e C_e$ is totally bounded.

Its closure $B$ is totally bounded and is complete because it is closed in the complete space $X$. A complete totally bounded metric space is compact: every sequence admits, by successively choosing one ball from finite covers with radii tending to zero, a Cauchy subsequence, which converges by completeness. This proves the required compactness without assuming that any ball in $X$ is locally compact.

The map $T$ maps the union of cycle sets onto itself. By continuity, $T(B)\subset B$. Since $B$ is compact, $T(B)$ is compact and therefore closed; it contains the union of the cycle sets. Consequently $T(B)=B$.

### 3. Existence of the Hausdorff limit and tail description

The space of nonempty compact subsets of a compact metric space is complete for $d_H$. Here is the needed construction. For a Hausdorff-Cauchy sequence, choose a subsequence $C_{e_j}$ such that $d_H(C_{e_j},C_{e_{j+1}})<2^{-j}$. Starting from any point in $C_{e_1}$, choose successive points in these sets with distances less than $2^{-j}$. They form a Cauchy sequence and have a limit in $B$. Let $A$ be the set of all subsequential limits of points $x_j\in C_{e_j}$ with $e_j\to\infty$. Compactness of $B$ makes $A$ nonempty and closed. The Hausdorff-Cauchy property implies $d_H(C_e,A)\to0$: first bound the distances from $C_e$ to points of a sufficiently late cycle uniformly, and then pass to convergent subsequences in $B$ in each directed distance. In particular,

$$
\tag{3}A=\bigcap_{N\geq1}\overline{\bigcup_{e\geq N}C_e}^{\,B},
\qquad d_H(C_d,A)\leq\varepsilon_d.
$$

The second assertion follows by fixing $d$, using $d_H(C_d,C_e)\leq\varepsilon_d$ for every $e>d$, and passing to the Hausdorff limit. Continuity and $T(C_e)=C_e$ imply $T(A)=A$. For the reverse inclusion, if $y_j\in C_{e_j}$ converges to $y\in A$, choose its predecessor $x_j\in C_{e_j}$. A subsequence of $(x_j)$ converges in $B$ to some $x\in A$, and $T(x)=y$.

### 4. Uniform cycle measures converge

Let $f\in C(B,\mathbb R)$. From the coupling in Step 1,

$$
\tag{4}\left|\int f\,d\mu_d-\int f\,d\mu_e\right|
\leq\omega_f(a_{d,e})\leq\omega_f(\varepsilon_d)
\qquad(e>d).
$$

Uniform continuity gives $\omega_f(t)\to0$ as $t\to0$. Hence $L(f):=\lim_e\int f\,d\mu_e$ exists for every $f\in C(B,\mathbb R)$. The functional $L$ is linear, positive, has norm $1$, and satisfies $L(1)=1$. The Riesz representation theorem for positive functionals on continuous functions on a compact Hausdorff space gives a unique regular Borel probability $\mu$ with $L(f)=\int f\,d\mu$. This proves weak convergence. No subsequence of the original sequence has been selected for the final limit.

Since each $\mu_e$ is $T$-invariant and $f\circ T$ is continuous on $B$, passing to the limit proves $T_*\mu=\mu$. The Hausdorff convergence implies $\operatorname{supp}(\mu)\subset A$: a compact subset of $B\setminus A$ has positive distance from $A$ and eventually misses all $C_e$; testing with continuous functions supported outside $A$ gives zero measure there.

The same coupling estimate has a limiting form. Fix $d$ and take the couplings between $\mu_d$ and $\mu_e$ given in Step 1. Compactness of the probability measures on the compact metric space $B\times B$ gives a convergent subsequence. Its limit has marginals $\mu_d,\mu$ and is supported on the closed set $\{(x,y):d(x,y)\leq\varepsilon_d\}$. Consequently

$$
\tag{5}W_1(\mu_d,\mu)\leq W_\infty(\mu_d,\mu)\leq\varepsilon_d,
\qquad
\left|\int f\,d\mu_d-\int f\,d\mu\right|\leq\omega_f(\varepsilon_d).
$$

Here sequential compactness of probabilities is applied only to a proved compact metric space, not to an arbitrary nonmetrizable compactification.

### 5. Minimality of the limit system

Fix $x,y\in A$ and $\eta>0$. Choose $e$ with $d_H(C_e,A)<\eta$, and choose $u,v\in C_e$ with $d(u,x)<\eta$ and $d(v,y)<\eta$. Some nonnegative integer $j$ satisfies $T^ju=v$, because $C_e$ is a single cycle. The isometry and the ultrametric inequality give

$$
d(T^jx,y)\leq\max\{d(T^jx,T^ju),d(v,y)\}<\eta.
$$

Every forward orbit in $A$ is dense. In particular, the support of the invariant probability $\mu$, a nonempty closed invariant subset of $A$, equals $A$.

### 6. Finite clopen quotients and unique ergodicity

Choose positive radii $\eta_j\downarrow0$. On $A$ let $x\sim_jy$ mean $d(x,y)<\eta_j$. The ultrametric inequality makes this an equivalence relation; its classes are open and closed. Compactness makes the quotient set $Q_j=A/{\sim_j}$ finite. The isometry induces a permutation of $Q_j$. Minimality implies that this permutation is one cycle: otherwise the union of the classes in one quotient orbit would be a proper nonempty clopen invariant subset of $A$.

Every invariant probability on $A$ therefore gives each member of $Q_j$ mass $1/q_j$, where $q_j=\#Q_j$. The partitions refine as $j$ increases, and their diameters tend to zero. Their clopen sets form a basis of the topology. A continuous function can be uniformly approximated by functions constant on their cells, so these cell masses uniquely determine the integral of every continuous function and hence the probability measure. This proves unique ergodicity independently of any named odometer theorem.

### 7. Prime-power cycle lengths force a $p$-odometer or a finite cycle

Assume now $\#C_e=p^e$. Fix $j$ and take $e$ with $d_H(C_e,A)<\eta_j$. To each $u\in C_e$ associate the class in $Q_j$ of any $x\in A$ with $d(u,x)<\eta_j$. The association is well-defined: two choices of $x$ have distance less than $\eta_j$. It is onto, using the other directed Hausdorff bound, and it commutes with $T$, using the isometry. It maps a cycle of length $p^e$ onto a cycle of length $q_j$, so $q_j\mid p^e$. Thus $q_j=p^{k_j}$ for a nonnegative integer $k_j$.

Choose a basepoint $a\in A$. Label the cell of $T^ma$ in $Q_j$ by $m\bmod q_j$. Minimality guarantees that this labels all cells; cyclic transitivity makes the label well-defined. Refinement gives the reduction maps

$$
\mathbb Z/q_{j+1}\mathbb Z\longrightarrow\mathbb Z/q_j\mathbb Z,
\qquad q_j\mid q_{j+1}.
$$

The map from $A$ to the inverse limit of these finite cyclic groups is continuous and injective because the partition diameters tend to zero. It is surjective because every compatible nested sequence of nonempty compact cells has nonempty intersection, and that intersection is a singleton. The map is a homeomorphism, by compactness of $A$ and Hausdorffness of the inverse limit. It conjugates $T$ to addition by $1$ in every coordinate.

If the integers $k_j$ are bounded, they are eventually constant, and $A$ is one finite cycle of cardinality $p^k$. If they are unbounded, the moduli $p^{k_j}$ are cofinal among all powers of $p$, so the inverse limit is $\mathbb Z_p$. The invariant measure is Haar probability because its image on each finite quotient is uniform. This proves the claim. $\square$

## Berkovich implementation and the ambient-topology issue

### 8. Compact classical support is enough over every allowed ground field

Let $K$ be complete and algebraically closed with an ultrametric absolute value. Suppose the sets $C_e$ lie in a closed classical disk $X=\{z:|z|\leq R\}$ on which a polynomial $T$ is an isometry, and suppose (CC). The disk is complete, even when it is not locally compact. Steps 1–7 apply with $d(x,y)=|x-y|$.

The map sending $a\in K$ to its evaluation seminorm in the Berkovich affine line is continuous: for every polynomial $f\in K[z]$, the function $a\mapsto|f(a)|$ is continuous. Its restriction to the compact set $B$ is an embedding into a Hausdorff space. For each continuous real-valued function $F$ on the Berkovich projective line, its restriction to $B$ is continuous. Hence

$$
\int F\,d\mu_e\longrightarrow\int F\,d\mu.
$$

This is precisely the requested weak* convergence on the Berkovich projective line. The measure $\mu$ is a Radon probability there, obtained by pushing forward a probability on the compact metric space $B$. All its support consists of type-I points. Nothing in the proof asserts metrizability of the whole Berkovich line or compactness of the ambient classical disk.

### 9. An optional compact metrizable closure without (CC)

There is also a separate, weaker ambient fact. Let $D$ be a countable subset of a bounded classical disk, and let $\mathcal C$ be its closure in the corresponding closed Berkovich disk. Then $\mathcal C$ is compact metrizable, even if the full Berkovich line over $K$ is not metrizable.

To prove metrizability, the countable family of continuous functions

$$
\phi_a(x)=|z-a|_x,\qquad a\in D,
$$

separates points of $\mathcal C$. Indeed, let $x\ne y$ in $\mathcal C$. Since $K$ is algebraically closed, factorization of polynomials into linear factors shows that some $b\in K$ satisfies $|z-b|_x\ne|z-b|_y$. Interchange $x,y$ if necessary and choose a positive real number $t$ strictly between these values. The relatively open set $\{u\in\mathcal C:|z-b|_u<t\}$ contains $x$ and meets the dense set $D$. Choose $a$ in this intersection, so $|a-b|<t$. The ultrametric inequalities for seminorms imply

$$
|z-a|_x<t<|z-a|_y.
$$

For the second inequality, $|z-b|_y>t>|a-b|$ forces $|z-a|_y=|z-b|_y$. Thus the map given by the functions $\phi_a$ is a continuous injection from compact $\mathcal C$ to a countable product of bounded real intervals. It is a homeomorphism onto its image, proving metrizability.

Apply this to $D=\bigcup_eC_e$ when all cycles lie in one invariant bounded disk. On $\mathcal C$, every subsequential measure limit exists along a subsequence after further extraction and is invariant. It is supported on

$$
\mathcal Y=\bigcap_{N\geq1}\overline{\bigcup_{e\geq N}C_e}^{\,\mathcal C}.
$$

If $T|_{\mathcal Y}$ is known independently to be uniquely ergodic, then $\mu_e$ converge. This last implication alone does not prove unique ergodicity; top-level cluster matching is not such a proof.

## Exact interface to the quadratic arithmetic lane

Fix an odd prime $p$, an algebraically closed complete ultrametric field $K$ of characteristic $p$, and $s=\lambda-1\in K$ with $0<|s|<1$. Write

$$
r=\frac{p-1}{p},\qquad P(z)=(1+s)z+z^2,\qquad
v(x)=\frac{\log|x|}{\log|s|},\qquad R=|s|^r.
$$

Let $S_e$ denote the single cycle of period $p^e$ in the open unit disk. The source theorem supplies its existence, uniqueness and containment in $|z|=R$. On the complete disk $|z|\leq R<1$,

$$
P(x)-P(y)=(x-y)(1+s+x+y),\qquad |1+s+x+y|=1,
$$

so $P$ is an isometry.

The following arithmetic condition suffices; it is not an assumption of the general theorem:

$$
\tag{AC}
\text{For each }d\geq1\text{ there is }c_d\to+\infty
\text{ such that, for every }e>d,\text{ some }\beta\in S_d,\alpha\in S_e
\text{ satisfy }v(\beta-\alpha)\geq c_d.
$$

Then $a_{d,e}\leq|s|^{c_d}$ uniformly in $e>d$, and (CC) follows. Every assertion of Steps 1–8 follows for the full sequence of quadratic cycle measures. In particular,

$$
\tag{6}d_H(S_d,A)\leq|s|^{c_d},\qquad
W_\infty(\mu_d,\mu)\leq|s|^{c_d}.
$$

The A1 lane proposes the stronger average-contact identity

$$
\tag{AC$'$}
\frac1{p^e}\sum_{\alpha\in S_e}v(\beta-\alpha)
=\frac{p-1}{p^{d+1}}A_d=:c_d
\geq d r^3+r^2\left(1+\frac1p\right),
\qquad \beta\in S_d,\quad e>d,
$$

where $A_d=v((P^{p^d})'(\beta)-1)$. If (AC$'$) is valid with finite valuations for every stated parameter, one summand is at least its average, so it implies (AC). No relation between higher Galois splitting fields, exact pairwise contacts or previously chosen orbit orientations is needed for this implication. The all-$e>d$ quantifier is essential; closeness for one selected pair of consecutive levels would need a separate summability or ultrametric chaining argument.

### Aperiodicity directly from the finite average-contact identity

The full identity (AC$'$), if established, excludes periodic points from the limit without an additional isolation theorem. Fix $d\geq1$, $\beta\in S_d$, $e>d$ and $\alpha\in S_e$, and write $h=v(\beta-\alpha)$. The $p^{e-d}$ distinct points $P^{j p^d}(\alpha)$, for $0\leq j<p^{e-d}$, all have distance $|\beta-\alpha|$ from $\beta$, since $P^{j p^d}(\beta)=\beta$ and $P$ is an isometry. All other points of $S_e$ have distance at most $R$ from $\beta$ and therefore valuation at least $r$. Consequently (AC$'$) gives

$$
c_d\geq p^{-d}h+(1-p^{-d})r,
\qquad
\tag{7}h\leq U_d:=p^dc_d-(p^d-1)r<+\infty.
$$

Thus $|\beta-\alpha|\geq|s|^{U_d}>0$, uniformly over every $e>d$, every $\alpha\in S_e$ and every $\beta\in S_d$. Passing to the Hausdorff limit shows $A\cap S_d=\varnothing$ for each fixed $d\geq1$.

If the finite-cycle alternative in Step 7 held, its period would be $p^k$. For $k\geq1$, uniqueness of the quadratic cycle of period $p^k$ in the open unit disk would give $A=S_k$, contradicting this separation. For $k=0$, a point of $A$ would be fixed by $P$. Its two fixed points are $0$ and $-s$, neither on $|z|=R$, since $0<|s|<|s|^r$. All of $A$ is on this sphere, being the Hausdorff limit of sets on the sphere. Thus the one-point alternative is excluded as well.

It follows that, under (AC$'$), $A$ is conjugate to $\mathbb Z_p$ with addition by $1$ and $\mu$ is nonatomic Haar probability. Minimality then excludes every periodic point of $A$: any such point would have a finite closed invariant orbit equal to $A$. This direct argument was suggested by the coordinator and checked here from the exact fraction $p^{-d}$ of aligned higher-cycle points.

### Alternative refinement from periodic-point isolation

Suppose, in addition to (AC), that every periodic point of $P$ on $|z|=R$ is isolated within the set of all periodic points. Then $A$ contains no periodic point. To see this, a point $a\in A$ is approached by points of $S_e$ with $e\to\infty$, by Hausdorff convergence. If $a$ were periodic, all sufficiently high $S_e$ would omit $a$ because their exact periods differ, contradicting its isolation. The finite-cycle alternative in Step 7 is therefore excluded, and $P|_A$ is a $p$-adic adding machine with nonatomic Haar probability.

For the actual polynomial, it would suffice to verify that every periodic point on this sphere has multiplier $m$ with $|m|=1$ and $m$ not a root of unity, and then use Lindahl–Rivera-Letelier Corollary 1.1. In characteristic $p$, a root of unity congruent to $1$ modulo the maximal ideal must equal $1$: remove any $p$-power from its order using $(u-1)^{p^j}=u^{p^j}-1$, and use the unit linear term of $(1+w)^n-1$ when $p\nmid n$ and $|w|<1$. Thus, for these cycle multipliers, the finite nonzero quantity $A_d=v(m-1)$ proposed in (AC$'$) would also provide the required non-root-of-unity check. This extra refinement is not needed for convergence itself.

## Why the earlier generic inputs alone do not establish convergence

The following abstract counterexample separates the missing cross-level condition from internal ramification bounds. It is not claimed to arise from the quadratic polynomial.

Fix $q\in(0,1)$ and put $r=(p-1)/p$ and $\rho_j=q^{(p^j+1)r}$ for $j\geq0$. Let $\Omega$ consist of all words of finite positive length over $\{0,\ldots,p-1\}$ and all infinite words. Regard the first digit as the least significant digit. Distinct words at distance $\rho_j$ have exactly $j$ initial digits in common; termination of a finite word counts as the first difference when one word is a prefix of the other. This is a compact ultrametric space. At each fixed prefix length there are finitely many cylinders and finitely many shorter terminated words, giving total boundedness. A Cauchy sequence either eventually stays at one terminated word or determines a consistent infinite word, giving completeness.

Let $T$ add $1$, modulo $p^e$ on a word of finite length $e$, and with carries on infinite words. Common-prefix length is preserved, including a termination boundary, so $T$ is an isometry. Choose $\eta$ with $\rho_1<\eta<\rho_0$, equip $\Omega\times\{0,1\}$ with the maximum of this word metric and $\eta$ times the discrete bit metric, and leave the bit invariant under $T$. Restrict to the closed invariant subspace

$$
X=\{(w,e\bmod2):w\text{ has finite length }e\geq1\}
\ \cup\ \{(w,b):w\text{ is infinite},\ b\in\{0,1\}\}.
$$

There is exactly one finite cycle $C_e$ of each period $p^e$ and no other periodic points. Every $C_e$ has the same $p$ top-level clusters given by its first digit. These top clusters match canonically for all levels. For every $x\in C_e$ and $0\leq j<e$,

$$
d(T^{p^j}x,x)=\rho_j=q^{(p^j+1)r};
$$

thus the same form of internal displacement lower valuation bounds holds, uniformly in the cycle level. Nevertheless, the even cycle measures converge to Haar probability on the infinite-word boundary with bit $0$, and the odd cycle measures converge to Haar probability on the boundary with bit $1$. The continuous bit-coordinate function has integrals alternating between $0$ and $1$. Hence the full sequence does not converge.

For the asserted subsequence limits, each cylinder of length $j$ has mass $p^{-j}$ in every cycle of length $e\geq j$, and the distance from each finite word of length $e$ to any infinite extension with the same bit is $\rho_e\to0$. These statements prove the two Haar limits directly. The example demonstrates that uniqueness of each finite cycle, stable top-$p$ matching and arbitrarily strong internal return estimates do not, as abstract dynamical facts, replace (AC) or another genuine cross-level distribution theorem.

## Source subtraction and open risks

- The finite-cycle coupling, compactness, finite-partition proof and Haar/odometer description are elementary/general dynamical machinery, not a new target-arithmetic mechanism. They are written out to make the exact interface auditable.
- The external target is Problem 1.3 of Lindahl–Rivera-Letelier, *Optimal cycles in ultrametric dynamics and minimally ramified power series*, arXiv:1311.4478v3, dated 26 May 2015. The source also supplies Theorem C, its $q=1$ discussion, and the periodic-point isolation result in Corollary 1.1. [Primary full text](https://arxiv.org/html/1311.4478v3).
- Compactness/Hausdorffness and the seminorm definition of the Berkovich line are established background; see Matthew Baker, *An introduction to Berkovich analytic spaces and non-archimedean potential theory on curves*, Section 1. [Author lecture notes](https://swc-math.github.io/aws/2007/BakerNotesMarch21.pdf).
- The odometer/unique-invariant-probability mechanism is classical. For a broader equicontinuous Cantor-action formulation, see Hurder and Lukina, *Essential holonomy of Cantor actions*, Sections 2.2–2.3. [Author manuscript](https://homepages.math.uic.edu/~hurder/papers/93manuscript.pdf). The proof in Steps 5–7 does not depend on importing its more general theory.
- The general theorem has no remaining mathematical hypothesis gap. The actual quadratic application must not be marked established from this file alone: the polynomial average-contact identity, its finite multiplier valuation and its uniform validity over all allowed $K,\lambda,p$ are the companion A1 obligation.
- Even if that obligation closes, the result concerns the stated source-system cycle distributions only. It supplies no target Euler factors, root numbers, automorphy or Hilbert–Pólya realization.

No mathematical computation, external model call, manuscript edit or Git action was performed for this proof package.
