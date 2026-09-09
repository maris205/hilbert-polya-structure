# R4 A1: convergence of optimal-cycle measures

2026-09-09 UTC. New bounded proof investigation. All admitted PC424-L,
Round-3 author files and their reviews remain read-only. No mathematical
run, manuscript, evaluation, Git, shared-index or external-model action
is allocated.

## Original public question

The target is Lindahl–Rivera-Letelier,
[Optimal cycles in ultrametric dynamics and minimally ramified power series, Problem 1.3](https://arxiv.org/html/1311.4478v3#S1.SS3),
in the 26 May 2015 arXiv version, subsequently published in
Compositio Mathematica 152 (2016), 187–222.

Let $p$ be any odd prime, let $(K,|\cdot|)$ be any complete
algebraically closed ultrametric field of characteristic $p$, and fix
$\lambda\in K$ with $0<|\lambda-1|<1$. Write
$P(z)=\lambda z+z^2$. For $e\ge1$, let $\Pi_e$ be its unique cycle
of $p^e$ distinct points in the open unit disk with ordinary least
period $p^e$. Does the sequence of real probability measures

$$\mu_e=p^{-e}\sum_{z\in\Pi_e}\delta_z$$

converge weakly on the Berkovich projective line $\mathbb P^{1,\mathrm{an}}_K$?
The normalization is a real mass, not division by $p$ in $K$.
The source's Theorem C and its $q=1$ discussion supply existence,
uniqueness and the common absolute value
$|\lambda-1|^{(p-1)/p}$. The question here retains every allowed
field and multiplier, not only the formal-parameter base.

## Status

**PROVABLE AS STATED: author proof, pending independent review.** The
original field, multiplier and prime quantifiers are unchanged. The
proof below also shows that the measures are all carried by one compact
subset of the classical field $K$, and gives a uniform orbit-coupling
estimate. Source-priority clearance and paper admission are separate
questions and are not asserted here.

## Exact new estimate

Put $s=\lambda-1$, normalize
$v(x)=\log|x|/\log|s|$ for $x\ne0$, and set $r=(p-1)/p$.
For $\beta\in\Pi_d$ and $0\le j<d$, let

$$\delta_j(\beta)=v(P^{\circ p^j}(\beta)-\beta),\qquad
A_d=v((P^{\circ p^d})'(\beta)-1).$$

The identities and bound proved below are

$$A_d=\delta_{d-1}(\beta)
 +\sum_{j=0}^{d-1}(p-1)p^{d-j-1}\delta_j(\beta), \tag{MC1}$$

and, for every $e>d$,

$$\frac1{p^e}\sum_{\alpha\in\Pi_e}v(\beta-\alpha)
=c_d:=\frac{p-1}{p^{d+1}}A_d
\ge d r^3+r^2(1+1/p). \tag{MC2}$$

All quantities are finite real valuation numbers. The right side
tends to infinity with $d$, uniformly over $e>d$ after normalization.
In particular (MC2) supplies a pair with
$v(\alpha-\beta)\ge c_d$ for every pair of levels $e>d$.

Since $P$ is an isometry on these cycles, iterating one such pair
couples $\mu_e$ and $\mu_d$ with every paired absolute distance at most
$|s|^{c_d}$. This is stronger than the accepted top-$p$ cluster matching
and does not require guessing exact deeper displacement values.

## Assumptions and source subtraction

- The exact public question, common sphere, and $q=1$ case of Theorem C
  were read in the primary arXiv HTML. Bounded searches for the problem,
  title and measure/equidistribution terminology returned the source and
  related literature, but no checked primary solution. This is not a
  claim that no subsequent solution exists.
- The accepted canonical small-factor identity is
  $Q_e=M_eV_e$, with $\deg M_e=p^e$, its roots the small cycle,
  and $V_e(0,0)$ a unit. It is part of the prior LRL/Hensel interface.
- The accepted [B4 displacement proof, Section 1](../../continuation_round2/b4_local_period_degree/PROOF_SUPPLEMENT.md)
  gives $\delta_j(\beta)\ge(p^j+1)r$, by the weighted Gauss valuation
  and $(U-I)^{p^j}=U^{p^j}-I$. The weaker linear-in-$j$ displacement
  estimate would not give the divergent lower bound in (MC2).
- The [R3 interlevel contact proof](../../continuation_round3/a3_interlevel_contacts/PROOF_SUPPLEMENT.md)
  and [full-local-inertia proof](../../continuation_round3/a3_interlevel_contacts/FULL_LOCAL_INERTIA.md)
  already use derivative-ratio identities at low anchor levels.
  Their complete statements and proofs were read. This investigation
  seeks the all-anchor-level average and its measure consequence.
- The accepted top-$p$ matching and
  [oriented first quotient](../../continuation_round3/a3_interlevel_contacts/ORIENTED_QUOTIENT_STABILIZATION.md)
  are not being promoted to higher-depth matching by assumption.
  Full local inertia is unnecessary for (MC1)–(MC2);
  only actual single-cycle sets and their factors are required. The
  Hensel interface and the displacement bound are re-established below
  to expose their applicability to the full public question.

## Assumptions and notation

The assumptions are exactly those in the original question: $p$ is odd,
$K$ is algebraically closed and complete of characteristic $p$, and
$s=\lambda-1$ satisfies $0<|s|<1$. Thus $|\lambda|=1$. The valuation
$v$ above has $v(s)=1$; set $v(0)=+\infty$. It is real-valued away from
zero. Write $N_e=p^e$ and

$$F_e(z)=P^{\circ N_e}(z)-z \quad(e\ge0),\qquad
Q_e(z)=F_e(z)/F_{e-1}(z) \quad(e\ge1).$$

The superscript $\circ$ always denotes an ordinary iterate. Integer
weights in real sums of valuations and in probability measures are
ordinary real numbers. Integer coefficients inside $K$ are reduced
modulo its characteristic. A multiplier is denoted by $m_d$ below to
distinguish it from the measure $\mu_d$.

The only dynamical source input is the stated odd-characteristic,
$q=1$ optimal-cycle theorem, including minimal ramification of
$g(z)=z+z^2$. In particular

$$\operatorname{ord}_z(g^{\circ p^e}(z)-z)
=1+\frac{p^{e+1}-1}{p-1} \quad(e\ge0). \tag{1}$$

Existence and distinctness of the $p^e$ points of $\Pi_e$ are part of
that input, not conclusions of an irreducibility calculation.

## Proof strategy

Differentiate a dynatomic factorization at a periodic anchor. First
this expresses the anchor multiplier through all within-cycle
distances. Then differentiating higher quotients at the same anchor
expresses its average distance to every higher cycle. The elementary
characteristic-$p$ displacement bound makes that average diverge with
the anchor level. One close pair then yields an entire close coupling,
because the native dynamics is isometric.

## Dependency map

1. Embed a coefficient copy of $\overline{\mathbb F}_p((t))$
   isometrically into $K$ by $t\mapsto s$. Prove Laurent-series
   evaluation, leading-term norm, injectivity and compatibility of the
   canonical small factors with all of $\Pi_e$.
2. Use the exact difference identity for $P$ to identify a native
   displacement of index $a$ with $\delta_{v_p(a)}$ and to prove
   that the multiplier in (MC1) is not one.
3. Differentiate the accepted factorization at an anchor of level $d$
   to obtain (MC1). Differentiate the level-$e$ quotient at that same
   anchor to obtain (MC2), with a nonzero denominator checked first.
4. Apply the accepted exponential displacement lower bound and sum
   all terms, rather than extrapolating a guessed contact pattern.
5. Pass from a single close pair to aligned native orbit couplings,
   total boundedness of the union of cycles, and a unique weak limit.
   This final argument is included here; it does not depend on the
   complementary D1 investigation or on an odometer assertion.

## Proof

### 1. Coefficient-field specialization for every allowed multiplier

Let $k_0$ be the set of elements of $K$ algebraic over its prime field
$\mathbb F_p$. Because $K$ is algebraically closed, $k_0$ is an
algebraic closure of $\mathbb F_p$. Every nonzero element of $k_0$
belongs to a finite field and hence is a root of unity, so its absolute
value is $1$. In particular $s\notin k_0$ and is transcendental over
$k_0$: an element algebraic over $k_0$ would belong to this algebraically
closed subfield.

Equip $k_0((t))$ with the absolute value $|s|^{\operatorname{ord}_t}$.
For a Laurent series $a(t)=\sum_{n\ge n_0}a_nt^n$, define

$$\iota(a)=\sum_{n\ge n_0}a_ns^n\in K. \tag{2}$$

The series converges because $K$ is complete and its terms tend to
zero. If $n_*$ is the first nonzero coefficient index, the leading
term has norm $|s|^{n_*}$ and the entire remaining tail has norm at
most $|s|^{n_*+1}$. The strong triangle inequality therefore gives

$$|\iota(a)|=|s|^{n_*}\quad(a\ne0). \tag{3}$$

Finite Laurent polynomials are dense in $k_0((t))$. Addition and
multiplication are continuous in both valued fields. Applying them
first to finite truncations and then taking limits proves that
$\iota$ is a ring homomorphism; (3) makes it injective. It preserves
$1$, so the relation $\iota(a)\iota(a^{-1})=1$ proves that it is a
field homomorphism. It is an isometric embedding, with $t\mapsto s$.
No assertion that the residue field of $K$ equals $k_0$ is needed.

Over $R=k_0[[t]]$, put $P_t(z)=(1+t)z+z^2$ and define $F_{e,t}$,
$Q_{e,t}$ by the same iterate formulas. The quotient $Q_{e,t}$ is
a monic polynomial in $R[z]$: for any polynomial $h$, the polynomial
$h^{\circ p}(z)-z$ is divisible by $h(z)-z$, as is seen in the quotient
ring where $h(z)=z$; here take $h=P_t^{\circ p^{e-1}}$. Monic
polynomial division shows that the quotient belongs to $R[z]$ and
that its reduction is the quotient of the reductions. Equation (1)
gives

$$\overline{Q}_{e,t}(z)=z^{p^e}\overline V_e(z),
\qquad \overline V_e(0)\ne0. \tag{4}$$

The two monic factors in (4) are relatively prime. Coprime Hensel
factorization applies because $R$ is a complete discrete valuation
ring. It produces monic polynomials $M_{e,t},V_{e,t}\in R[z]$ with

$$Q_{e,t}=M_{e,t}V_{e,t},\qquad
\deg M_{e,t}=p^e,\qquad
\overline M_{e,t}=z^{p^e},\qquad
\overline V_{e,t}(0)\ne0. \tag{5}$$

Apply $\iota$ coefficientwise and denote the resulting polynomials
by $M_e,V_e$. The exact identity over $K$ is

$$F_e=F_{e-1}M_eV_e. \tag{6}$$

Their coefficients have nonnegative $v$-valuation, and $V_e(0)$ has
valuation zero. For any $x\in K$ of positive valuation, every
positive-degree term of $V_e(x)$ has positive valuation. Hence

$$v(V_e(x))=0 \quad\text{whenever }v(x)>0. \tag{7}$$

For every $\alpha\in\Pi_e$, the value $F_{e-1}(\alpha)$ is nonzero,
because its ordinary least period is $p^e$. Equations (6) and (7)
then imply $M_e(\alpha)=0$. There are $p^e$ distinct such points and
$M_e$ is monic of degree $p^e$, so

$$M_e(z)=\prod_{\alpha\in\Pi_e}(z-\alpha). \tag{8}$$

In particular the transported factor is separable and contains exactly
the required cycle in $K$. No irreducibility, full local inertia,
choice of extension tower, or additional assumption on $\lambda$ has
entered the argument.

### 2. Isometry and index-dependent displacements

Let $D=\{x\in K:v(x)\ge r\}$. Since $|\lambda|=1$ and
$|x|\le|s|^r<1$, $P(D)\subseteq D$. For $x,y\in D$,

$$P(x)-P(y)=(x-y)(1+s+x+y). \tag{9}$$

For $x\ne y$, the second factor belongs to
$1+\{u\in K:v(u)\ge r\}$, so it is a unit. Products of elements in
that set stay in the set. Thus, for every integer $a\ge0$,

$$v(P^{\circ a}(x)-P^{\circ a}(y))=v(x-y),\qquad
\frac{P^{\circ a}(x)-P^{\circ a}(y)}{x-y}
\in1+\{u:v(u)\ge r\}. \tag{10}$$

All cycles lie in $D$. Fix $\beta\in\Pi_d$, with $d\ge1$.
For $0\le j<d$, the quantity
$\delta_j=v(P^{\circ p^j}(\beta)-\beta)$ is finite. If
$1\le a<p^d$, write $a=kp^j$, where $j=v_p(a)$ and $p\nmid k$.
Set $G=P^{\circ p^j}$. In the telescoping sum

$$G^{\circ k}(\beta)-\beta
=\sum_{i=0}^{k-1}\bigl(G^{\circ(i+1)}(\beta)-G^{\circ i}(\beta)\bigr),$$

divide by $G(\beta)-\beta\ne0$. Each summand after division is
congruent to $1$ modulo the maximal ideal, by (10) applied to
$G^{\circ i}$. Their sum has residue $k\ne0$, and therefore valuation
zero. We have proved

$$v(P^{\circ a}(\beta)-\beta)=\delta_{v_p(a)}
\quad(1\le a<p^d). \tag{11}$$

In particular, there are exactly $(p-1)p^{d-j-1}$ points of
$\Pi_d\setminus\{\beta\}$ whose difference from $\beta$ has the
valuation indexed by $j$. This statement counts rotation indices;
it does not assert that different $j$ necessarily give distinct
valuation values.

### 3. Exponential displacement bound

For a polynomial $H(z)=\sum_i h_i z^i\in K[z]$, define its weighted
Gauss valuation by

$$w_r(H)=\min_{h_i\ne0}\{v(h_i)+ir\},\qquad
w_r(0)=+\infty.$$ 

Let $U$ be the $K$-linear operator $UH=H\circ P$, and set
$\Delta=U-I$. For every integer $i\ge1$,

$$\Delta(z^i)=z^i\bigl((1+s+z)^i-1\bigr).$$

The constant term in the bracket has valuation at least $1$ if it is
nonzero. Every positive-degree term has weighted valuation at least
$r$, because its coefficient is integral and its degree is positive.
Since $1>r$, the bracket has weighted valuation at least $r$.
Constants have zero $\Delta$-image. The nonarchimedean inequality for
the finite sum of monomial images consequently gives

$$w_r(\Delta H)\ge w_r(H)+r. \tag{12}$$

By iteration, $w_r(\Delta^N z)\ge(N+1)r$ for every positive
integer $N$. The commuting operators $U$ and $I$ act in
characteristic $p$, so the binomial identity gives

$$\Delta^{p^j}=U^{p^j}-I \quad(j\ge0).$$

Evaluation at $\beta$, where $v(\beta)=r$, cannot decrease the
weighted Gauss lower bound. It follows that

$$\delta_j\ge(p^j+1)r \quad(0\le j<d). \tag{13}$$

This proves the needed version of the earlier B4 displacement lemma
directly over the arbitrary field $K$ of the question.

### 4. The multiplier identity and nonzero denominators

Put $m_d=(P^{\circ p^d})'(\beta)$. Differentiate (6) with $e=d$
and evaluate at $\beta$. Since $M_d(\beta)=0$, one obtains

$$m_d-1=F_{d-1}(\beta)M_d'(\beta)V_d(\beta). \tag{14}$$

Each factor on the right is nonzero: the first by the least-period
condition, the second by (8) and distinctness, and the third by (7).
Thus $m_d\ne1$ and $A_d=v(m_d-1)$ is finite. Equations (8), (11)
and (14) yield

$$\begin{aligned}
A_d
&=v(F_{d-1}(\beta))+
  \sum_{\gamma\in\Pi_d\setminus\{\beta\}}v(\beta-\gamma)\\
&=\delta_{d-1}+
  \sum_{j=0}^{d-1}(p-1)p^{d-j-1}\delta_j.
\end{aligned} \tag{15}$$

This is (MC1). The multiplier $m_d$ is independent of the choice of
$\beta$ in the cycle: its chain-rule expression is the product of
$P'$ over all $p^d$ orbit points, and starting elsewhere just
permutes these scalar factors. Hence $A_d$ is also independent of
the anchor point.

Now fix any $e>d$. Both $F_e(\beta)$ and $F_{e-1}(\beta)$ vanish.
Differentiating $F_e=F_{e-1}Q_e$ at $\beta$ gives

$$F_e'(\beta)=F_{e-1}'(\beta)Q_e(\beta). \tag{16}$$

By the chain rule at the fixed point of $P^{\circ p^d}$,

$$F_e'(\beta)=m_d^{p^{e-d}}-1
=(m_d-1)^{p^{e-d}},$$

and the corresponding identity holds with $e-1$. In particular
$F_{e-1}'(\beta)\ne0$, including the boundary case $e=d+1$.
Division in (16) is therefore legitimate and gives

$$Q_e(\beta)=(m_d-1)^{(p-1)p^{e-d-1}}. \tag{17}$$

The cycles $\Pi_d$ and $\Pi_e$ are disjoint, because their least
periods differ. Taking valuations in (17), using $Q_e=M_eV_e$,
(7), and (8), gives the exact all-higher-level identity

$$\sum_{\alpha\in\Pi_e}v(\beta-\alpha)
=(p-1)p^{e-d-1}A_d \quad(e>d). \tag{18}$$

Every summand is finite. Dividing by the real number $p^e$ proves
the equality in (MC2), uniformly over every $e>d$.

### 5. Divergent contact and aligned orbit couplings

Apply (13) term by term in (15). Summing the finite geometric series
gives

$$\begin{aligned}
\frac{A_d}{p^d}
&\ge \frac{r(p^{d-1}+1)}{p^d}
 +\frac{r}{p^d}\sum_{j=0}^{d-1}
 (p-1)p^{d-j-1}(p^j+1)\\
&=r\left(1+\frac1p+d\frac{p-1}{p}\right).
\end{aligned} \tag{19}$$

Since $(p-1)/p=r$, (18) and (19) imply

$$c_d:=\frac{p-1}{p^{d+1}}A_d
\ge b_d:=d r^3+r^2(1+1/p)\longrightarrow+\infty. \tag{20}$$

Fix $e>d$ and any $\beta\in\Pi_d$. At least one
$\alpha\in\Pi_e$ has $v(\beta-\alpha)\ge c_d$, because the
maximum of the finitely many real numbers in (18) is at least their
average. For this pair, (10) gives

$$|P^{\circ i}(\alpha)-P^{\circ i}(\beta)|
=|\alpha-\beta|\le|s|^{c_d}\le\varepsilon_d:=|s|^{b_d}
\quad(i\ge0). \tag{21}$$

Define the real probability measure on $K\times K$

$$\pi_{e,d}:=p^{-e}\sum_{i=0}^{p^e-1}
\delta_{(P^{\circ i}(\alpha),P^{\circ i}(\beta))}. \tag{22}$$

Its first marginal is $\mu_e$. Its second marginal is $\mu_d$,
because every point of $\Pi_d$ occurs exactly $p^{e-d}$ times.
Every pair in its support has distance at most $\varepsilon_d$.
Thus it is a coupling of the actual native-cycle measures, not just
of an auxiliary cluster quotient. The deterministic bound
$\varepsilon_d\to0$ is valid for every $e>d$.

### 6. Classical compactness and the weak probability limit

Let $S=\bigcup_{e\ge1}\Pi_e\subset K$. For any real $\eta>0$,
choose $d$ so large that $\varepsilon_d<\eta$. For every $e>d$,
(21) shows that all of $\Pi_e$ lies within distance
$\varepsilon_d$ of the finite set $\Pi_d$. The finitely many earlier
cycles are finite sets as well. Consequently $S$ is totally bounded
in the metric $|x-y|$. Because $K$ is complete, its closure
$C=\overline S\subset K$ is a compact metric space. All its points
still have absolute value $|s|^r$, by continuity of the norm.

For a real continuous function $\varphi$ on $C$, define

$$\omega_\varphi(a)=
\sup\{|\varphi(x)-\varphi(y)|:x,y\in C,\ |x-y|\le a\}
\quad(a\ge0).$$

Compactness makes $\varphi$ uniformly continuous, so
$\omega_\varphi(a)\to0$ as $a\downarrow0$. Using the coupling
(22) yields

$$\left|\int_C\varphi\,d\mu_e-
\int_C\varphi\,d\mu_d\right|
\le\omega_\varphi(\varepsilon_d) \quad(e>d). \tag{23}$$

The sequence of integrals is therefore Cauchy for every
$\varphi\in C(C,\mathbb R)$. Its limit $L(\varphi)$ is a positive
linear functional, satisfies $L(1)=1$, and has norm one. The
Riesz representation theorem for positive linear functionals on a
compact Hausdorff space applies to $C$ and gives a unique regular
Borel probability measure $\nu_C$ with
$L(\varphi)=\int_C\varphi\,d\nu_C$. This proves weak convergence
on the classical compact space $C$.

The map $a\mapsto$ evaluation at $a$ embeds $K$ continuously into
$\mathbb P^{1,\mathrm{an}}_K$: on the affine line the defining
seminorm coordinates are $a\mapsto|H(a)|$ for polynomials $H$,
and each is continuous. Restricting to $C$, this is a continuous
injection of a compact space into the Hausdorff Berkovich projective
line, hence a homeomorphism onto a closed compact image. Push
$\nu_C$ forward under this inclusion and call the result $\nu$.
Every continuous real function on the Berkovich projective line
restricts to a continuous function on $C$. Equation (23) therefore
proves

$$\mu_e\ \xrightarrow[e\to\infty]{\mathrm{weak}}\ \nu
\quad\text{on }\mathbb P^{1,\mathrm{an}}_K. \tag{24}$$

Moreover, by first fixing $d$ in (23) and then taking $e\to\infty$,
the same upper bound compares $\mu_d$ with $\nu_C$ for every
$\varphi\in C(C,\mathbb R)$. The limit is $P$-invariant: each
$\mu_e$ is $P$-invariant, $P(C)\subseteq C$ by continuity, and weak
convergence applied to $\varphi\circ P$ passes that identity to the
limit. This proves the original convergence claim for every field,
multiplier and odd prime in its statement. $\square$

## Corrections or missing assumptions

None are introduced. In particular no assumption of discrete valuation
on $K$, residue field $\overline{\mathbb F}_p$, nested root fields,
full inertia, exact deeper contact pattern, separability premise beyond
the source's actual distinct cycle, or restriction to a formal
multiplier is required. The discrete valued field in Step 1 is only a
coefficient-field proof device that embeds into every allowed $K$.

## Open risks and source status

- This is an author proof pending independent actual-file review.
  The finite-denominator check, the average-versus-maximum inequality,
  and the quantifier $e>d$ have been exposed for that review.
- The bounded initial primary-source search did not identify a
  checked subsequent solution of Problem 1.3. This is not a current-open
  assertion or a proof of priority. The coordinator has allocated a
  separate bounded source-status check.
- The proof answers the measure question. It does not by itself claim
  an explicit odometer identification, a global Galois/inertia theorem,
  a new paper admission, or a Hilbert–Pólya construction.
