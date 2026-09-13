# Paper 25 — Fresh Independent Source-Design Review

## Verdict and independence

I am the fresh source-design reviewer for Paper 25. I authored none of the
ten frozen source-design files, neither candidate review, and no source-design
claim under review. I treated the two root ledgers, both candidate reviews,
all ten project files, every formula, every inventory assertion, every
citation statement, and every scope statement as unproved.

I read through the complete current BATCH_06_STATUS.md and
BATCH_06_IDEA_REPORT.md, both complete Paper-25 candidate reviews, and all ten
frozen project files. I then repeated the inventory and mathematical audits
independently. I used research-review and proof-writer discipline: explicit
assumptions, dependency order, literal algebra, boundary cases, adversarial
claim subtraction, and a finding ledger. I did not use a CAS, numerical
experiment, parameter scan, scientific program, generated certificate, or
empirical result. The only local computation was a new read-only no-follow
inventory and hashing implementation. Public network use was limited to the
eight required primary or authoritative source records listed below.

The complete scientific, evidence, citation, portfolio, inventory, and
permission conjunction passes. There is no hard blocker and no major or
minor mathematical defect.

## Controlling records and gate

The controlling gate immediately before this conditional write was
PAPER25_SOURCE_DESIGN_REVIEW_OPEN. The four root records remeasured as:

| Record | SHA-256 | Bytes | LF | Mode / links |
|---|---|---:|---:|---|
| BATCH_06_STATUS.md | fa0b10f522b8801f3556a42c0bd49964d658d36a930f4f84be3e235e8b5e979a | 175,824 | 2,548 | 0644 / 1 |
| BATCH_06_IDEA_REPORT.md | 164b1f3ce4bd60959e217cae8e30fb9c8e23e640a786bdb62a540174ec90325a | 297,321 | 5,769 | 0644 / 1 |
| BATCH_06_PAPER25_CANDIDATE_REVIEW_R1.md | c8044d3d41573df7d1cd356acaa1e78414e18b3608e76a50553157c556495d0f | 21,097 | 603 | 0644 / 1 |
| BATCH_06_PAPER25_CANDIDATE_REVIEW_R2.md | 46724d7d3c764d95f8235e6ffc40b40d78c6130ccf9c85a5832bbc4b5ca6b408 | 17,460 | 663 | 0644 / 1 |

The R1 terminal occurs uniquely at line 603 and the R2 terminal occurs
uniquely at line 663. The reviews are custody and comparison records, not
substitutes for the derivations below.

## Independent T10 evidence

I walked the project without following links, classified every descendant
node, sorted relative POSIX path bytes, opened every regular file as raw
bytes, and independently computed SHA-256, byte and LF counts, UTF-8
validity, newline properties, modes, links, and the aggregate framing.

| Frozen relative path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| experiments/EXPERIMENT_PLAN.md | ab2291ddf6bff7aae632e2b261c58895a9367dc110f15d2c22920cec685a7cc9 | 11,033 | 359 |
| experiments/EXPERIMENT_TRACKER.md | 9527dada16fa76c0434e94de028a1635fcab3942cf9bee5a38d5cb577f1a89fb | 5,405 | 92 |
| notes/CITATION_VERIFICATION.md | 9538e423e5ba9fedf9e9cac3fd8060800d683a935ffba48b8ada69b3b51697af | 9,001 | 126 |
| notes/CLAIMS_EVIDENCE_MATRIX.md | abb0b13c83fc32c5dbbecd0de6ce18c6a154177f41955deddcfba3bc308b6e7d | 8,618 | 87 |
| notes/NOVELTY_ASSESSMENT.md | ecc57ca4ba68375270b04d5be2eff9884d31f81d3fa1acc36d0bc5cd49f2683d | 8,496 | 136 |
| notes/PROOF_PACKAGE.md | 0b957e5519dff5460d819de335782b9ac2b669f42089e0699d03cf0349f5ab93 | 29,750 | 1,240 |
| notes/RESEARCH_QUESTION.md | 8641c4160fe74ee3925bc2803c90ef139261f48c844c78856b53989e9a8d7098 | 5,839 | 139 |
| refine-logs/FINAL_PROPOSAL.md | 13bf8d9bc21a1841b24b9d9308558d6807cba5e218685a03795dfd65d75d4f6d | 7,426 | 220 |
| refine-logs/INITIAL_PROPOSAL.md | 06caba1425c68ac387d3ae618bc1ce1edea02cbf4db547adfb3dea136070f6ba | 5,788 | 126 |
| refine-logs/REVIEW_SUMMARY.md | 69408011fd514f8a5ab54fe81253b960e527c58c0da46090f346e076de931fb7 | 6,190 | 122 |

The exact author universe is 10 regular files, 3 directories, 0 symbolic
links, and 0 other nodes. The only directories are experiments, notes, and
refine-logs. Every regular file is mode 0644 with link count one; every
directory is mode 0755 with link count two. All files decode as UTF-8, end
with a terminal LF, and contain no CR byte. Totals are 97,546 content bytes
and 2,647 LF. Relative path bytes total 288.

For each byte-sorted record I independently hashed

$$
\operatorname{u64be}(|p|)\,\|\,p\,\|\,
\operatorname{u64be}(|x|)\,\|\,x.
$$

The framed length is

$$
16(10)+288+97{,}546=97{,}994
$$

bytes, and its SHA-256 is

e92a6133694e5868e47525981f07e7335617a8f7e5bf84fd8b205743be3e2902.

The author stop phrase occurs exactly once, at
refine-logs/REVIEW_SUMMARY.md line 122. Immediately before the conditional
review write, experiments/source_lock.json, this review path, paper/,
paper/PAPER_PLAN.md, paper/main.tex, and paper/references.bib were all absent.

## Part I: selected-row factorization

Let

$$
A=-I_n+\mathsf P\mathsf Q,\qquad
B=-I_n+\mathsf R\mathsf S,\qquad C=BA,
$$

and let

$$
Y=\begin{bmatrix}\mathsf Q\\ \mathsf S\end{bmatrix},
\qquad r=\operatorname{rank}Y.
$$

Direct multiplication, with no kernel inference hidden inside it, gives

$$
C-I_n=-\mathsf P\mathsf Q-\mathsf R\mathsf S
       +\mathsf R\mathsf S\mathsf P\mathsf Q
=
\begin{bmatrix}
\mathsf R\mathsf S\mathsf P-\mathsf P&-\mathsf R
\end{bmatrix}
\begin{bmatrix}\mathsf Q\\ \mathsf S\end{bmatrix}.
$$

Choose a full-row-rank matrix $T_0\in K^{r\times n}$ whose rows form a basis
of the row space of $Y$. There is an $L$ with $Y=LT_0$. If

$$
U=\begin{bmatrix}
\mathsf R\mathsf S\mathsf P-\mathsf P&-\mathsf R
\end{bmatrix},
\qquad X=UL,
$$

then $C=I_n+XT_0$. With $z=t-1$, the rectangular Sylvester identity over
$K(z)$ yields

$$
\begin{aligned}
\det(zI_n-XT_0)
&=z^n\det(I_n-z^{-1}XT_0)\\
&=z^n\det(I_r-z^{-1}T_0X)\\
&=z^{n-r}\det(zI_r-T_0X).
\end{aligned}
$$

Both sides are polynomials, so the identity also holds at $z=0$:

$$
\chi_C(t)=(t-1)^{n-r}
\det\bigl((t-1)I_r-T_0X\bigr).
$$

The reduced determinant is monic of degree $r$. Therefore the nonunit
characteristic degree is at most $r$, while the algebraic multiplicity of
the unit eigenvalue is at least $n-r$. This is only a lower bound:
$\det((t-1)I_r-T_0X)$ may itself vanish at $t=1$. The kernel check agrees:
$\ker T_0=\ker\mathsf Q\cap\ker\mathsf S$, and every vector in it is fixed
by $C$.

All requested boundaries are consistent:

- If $r=0$, then $\mathsf Q=\mathsf S=0$, $A=B=-I_n$, $C=I_n$, and the
  empty reduced determinant is one.
- If $r=n$, the forced exponent is zero and no unit factor is forced.
- If $n=0$, necessarily $r=0$; both characteristic and reduced empty
  determinants are one, and the formula remains valid.

No exact-unit-multiplicity or complete support-profile classification follows.

## Part II: every-d parameter construction

Fix an integer $d\ge2$ before making any other choice.

Dirichlet's theorem gives a prime $p\equiv1\pmod d$. Choose a generator
$c\in\mathbb F_p^\times$, so $\operatorname{ord}(c)=p-1$. The $d$ solutions
of $x^d=1$ have least positive representatives
$r_1<\cdots<r_d$. For one sufficiently large common integer shift $N$, set

$$
a_i=Np+r_i.
$$

Then $a_1<\cdots<a_d$, the residues are exactly all $d$-th roots of unity,
and $a_1+1>4d$. Freeze these lifts and put

$$
S_a=\sum_i a_i,\qquad M=a_d.
$$

Since $p\nmid d$, there is one residue class satisfying

$$
bd\equiv1-(-1)^dc\pmod p.
$$

It is nonzero: equality to zero would force a primitive $c$ to be $1$ in
the even-$d$ case or $-1$ in the odd-$d$ case, incompatible with the
available order when $d\ge2$. Choose $b$ arbitrarily large and positive in
this fixed class, with $b\ge2$, and define

$$
R=1+\frac{2M}{bS_a}.
$$

As $b$ tends to infinity in the class, $R\downarrow1$. Hence one choice
simultaneously gives

$$
R^2<2
$$

and, for the finite set $i>1$,

$$
b(a_i-a_1)S_a>a_i^2R-a_1^2.
$$

The left side of each last inequality grows linearly in $b$ while the right
side has a finite limit. The quantifier order is therefore exactly

$$
d\longrightarrow p,c\longrightarrow(a_i)_{i=1}^d
\longrightarrow b,R,
$$

with no later choice changing an earlier residue.

## Literal gradients and symplecticity

Define

$$
V(q)=\prod_{j=1}^d q_j^2+\sum_{i=1}^d q_i^{a_i+1},
\qquad
W(p)=\prod_{j=1}^d p_j^b,
$$

and

$$
S_V(q,p)=(q,p+\nabla V(q)),\qquad
T_W(q,p)=(q+\nabla W(p),p),\qquad F=T_W\circ S_V.
$$

The literal derivative rows are

$$
\frac{\partial V}{\partial q_i}
=2q_i\prod_{j\ne i}q_j^2+(a_i+1)q_i^{a_i},
$$

and

$$
\frac{\partial W}{\partial p_i}
=b\,p_i^{b-1}\prod_{j\ne i}p_j^b.
$$

Thus a $q$-degree vector $u$ presents the two $V$ competitors
$2\sum_j u_j-u_i$ and $a_i u_i$. Once spikes are selected, their row
matrix is

$$
D=\operatorname{diag}(a_1,\ldots,a_d).
$$

The sole $W$ row in component $i$ has degree
$b\sum_jv_j-v_i$, so

$$
B_0=bJ-I_d,\qquad
C=B_0D=b\mathbf1a^{\mathsf T}-D.
$$

Every entry of $C$ is positive:
$C_{ii}=(b-1)a_i>0$ and $C_{ij}=ba_j>0$ for $i\ne j$.

For the standard form $\omega=\sum_i dq_i\wedge dp_i$, the extra term in
$S_V^*\omega$ is the alternating contraction of the symmetric Hessian of
$V$, hence zero. The identical argument with the Hessian of $W$ proves
$T_W^*\omega=\omega$. Their polynomial inverses subtract the same gradients.
This proves symplecticity and invertibility directly, without transferring a
claim from the literature.

## Broad ratio cone

Let

$$
\mathcal K_{\mathrm{ratio}}(R)
=\{u>0:\max_i u_i\le R\min_i u_i\}.
$$

It contains $\mathbf1$. For $u$ in this cone, set
$m=\min_i u_i$ and $H=a^{\mathsf T}u$. Since $u_j\le Rm$ and
$u_i\ge m$,

$$
2\sum_j u_j-u_i\le(2dR-1)m.
$$

Meanwhile $a_i u_i\ge a_1m$. The assumptions give

$$
a_1>4d-1>2dR-1,
$$

because $R<\sqrt2<2$. Therefore every spike wins strictly throughout the
broad cone.

Write $z=Cu$, so $z_i=bH-a_i u_i$. Positivity is already literal from the
entries of $C$. Also $H\ge S_am$ and $a_i u_i\le MRm$. Hence

$$
\frac{\max_i z_i}{\min_i z_i}
\le\frac{bH}{bH-MRm}
\le\frac{bS_a}{bS_a-MR}
=\frac{1}{1-\frac{MR}{bS_a}}.
$$

The middle direction is correct because $x/(x-k)$ decreases for $x>k>0$.
Since $M/(bS_a)=(R-1)/2$, the denominator is positive:

$$
R(R-1)=R^2-R<2-R<1.
$$

Finally,

$$
\frac{1}{1-\frac{R(R-1)}2}<R
$$

is equivalent, after multiplication by that positive denominator, to

$$
(R-1)\left(1-\frac{R^2}{2}\right)>0.
$$

Both factors are strict. Thus $C$ maps the broad cone into its interior.

## Fine visibility chamber

Use

$$
\mathcal K_{\mathrm{vis}}(R)=
\{u>0:u_i\le u_1<Ru_i,\ 
a_1u_1<a_i u_i\text{ for every }i>1\}.
$$

The ordinary seed lies on the permitted walls $u_i=u_1$, while
$u_1<Ru_i$ and $a_1u_1<a_i u_i$ are strict. The chamber is contained
strictly in the broad ratio cone away from the first coordinate.

For $u$ in the fine chamber put $s=u_1$, $H=a^{\mathsf T}u$, and
$w=Cu$. Then $u_j\le s$, every $u_j>s/R$, and

$$
H>\frac{S_a}{R}s.
$$

For $i>1$,

$$
w_1-w_i=a_i u_i-a_1s>0,
$$

so the first coordinate becomes strictly largest. The ratio wall has the
strict lower bound

$$
\begin{aligned}
Rw_i-w_1
&=(R-1)bH-Ra_i u_i+a_1s\\
&>
\left(\frac{(R-1)bS_a}{R}-RM+a_1\right)s\\
&=\left(\frac{M(2-R^2)}R+a_1\right)s>0.
\end{aligned}
$$

For the weighted wall,

$$
\begin{aligned}
a_iw_i-a_1w_1
&=b(a_i-a_1)H-a_i^2u_i+a_1^2s\\
&>
\left(\frac{b(a_i-a_1)S_a}{R}-a_i^2+a_1^2\right)s.
\end{aligned}
$$

The chosen parameter inequality implies

$$
\frac{b(a_i-a_1)S_a}{R}>
a_i^2-\frac{a_1^2}{R},
$$

so the last display is greater than

$$
a_1^2\left(1-\frac1R\right)s>0.
$$

All denominators are positive because $R>1$. Every defining wall is
preserved in the required direction, and $q_1$ is strictly visible after
the first complete step.

## Temporal carries, noncancellation, and exact ordinary degree

For $u$ in the broad cone,

$$
(Cu)_i\ge(bS_a-MR)m,\qquad
\max_j a_j u_j\le MRm.
$$

The identity $bS_a=2M/(R-1)$ and $R(R-1)<1$ give

$$
bS_a>2MR,
$$

and therefore the strict cross-block domination

$$
(Cu)_i>\max_j a_j u_j
$$

for every $i$. It also implies $Cu>u$ componentwise because all $a_j>1$.

Let $u_n$ be the position-degree vector at the beginning of step $n+1$.
At the first $V$ half-step, $a_i>1$ beats the carried degree-one momentum
coordinate. At every later $V$ half-step the fresh degree
$a_i u_{n,i}$ beats the carried $a_i u_{n-1,i}$ because
$u_n>u_{n-1}$. Thus the exact momentum vector is $Du_n$. At the $W$
half-step, the new degree vector is $B_0Du_n=Cu_n$, and the cross-block
inequality beats every entry of $Du_n$ and every carried position entry.
Consequently

$$
u_{n+1}=Cu_n,\qquad u_n=C^n\mathbf1.
$$

There is no cancellation gap. The original coordinates have coefficient
one, both shears use addition, multiplication, and positive integer
coefficients, and composition stays in the nonnegative integer coefficient
semiring. Strict selectors isolate the highest-degree source where additions
compete. Powers and products of nonzero top forms remain nonzero in a
polynomial domain. Characteristic zero makes the map
$\mathbb Z\to K$ injective, so no selected positive coefficient vanishes.

For $n\ge1$, the fine chamber makes $q_1$ uniquely maximal within the
position block, and the cross-block comparison makes every new position
degree larger than every retained momentum degree. At $n=0$, all $2d$
coordinate degrees tie at one. Thus the exact ordinary, rather than merely
weighted or upper-bound, identity is

$$
\deg(F^n)=e_1^{\mathsf T}C^n\mathbf1\qquad(n\ge0),
$$

with unique $q_1$ visibility asserted only for $n\ge1$.

## Characteristic polynomial and irreducibility

The matrix determinant lemma applied over $\mathbb Q(t)$ gives

$$
\begin{aligned}
\chi_C(t)
&=\det(tI_d+D-b\mathbf1a^{\mathsf T})\\
&=\prod_i(t+a_i)
-b\sum_i a_i\prod_{j\ne i}(t+a_j).
\end{aligned}
$$

A squarefree product of $k$ distinct $a_i$ occurs $k$ times in the second
sum. Therefore

$$
\chi_C(t)=t^d+
\sum_{k=1}^d(1-bk)e_k(a_1,\ldots,a_d)t^{d-k}.
$$

Modulo $p$, the residue multiset of the $a_i$ is exactly the root set of
$x^d-1$. Hence

$$
e_k(a)\equiv0\pmod p\quad(1\le k<d),\qquad
e_d(a)\equiv(-1)^{d+1}\pmod p.
$$

Since $1-bd\equiv(-1)^dc\pmod p$,

$$
\chi_C(t)\equiv t^d-c\pmod p.
$$

The exact finite-field binomial criterion is satisfied:

1. every prime divisor of $d$ divides $\operatorname{ord}(c)=p-1$;
2. $\gcd(d,(p-1)/\operatorname{ord}(c))=\gcd(d,1)=1$; and
3. if $4\mid d$, then $p\equiv1\pmod d$ implies $p\equiv1\pmod4$.

For $d=2$, $p$ is odd and a generator is outside the index-two square
subgroup, so $t^2-c$ is irreducible. This separately audits the smallest
allowed dimension.

As an independent cross-check, if $\alpha^d=c$, then
$\operatorname{ord}(\alpha)=d(p-1)$. Indeed
$\operatorname{ord}(\alpha^d)=p-1$, while $d\mid p-1$ forces the relevant
greatest common divisor to be $d$. Also

$$
p^k\equiv1+k(p-1)\pmod{d(p-1)},
$$

because all higher binomial terms contain $(p-1)^2$, which is divisible by
$d(p-1)$. The Frobenius orbit of $\alpha$ therefore has least length $d$.
This again proves $t^d-c$ irreducible.

The integral polynomial $\chi_C$ is monic and its reduction remains monic of
degree $d$. Any rational factorization would, by Gauss's lemma, reduce to a
nontrivial factorization modulo $p$. Hence $\chi_C$ is irreducible over
$\mathbb Q$.

## Perron degree and exact scalar recurrence order

The integer matrix $C$ is strictly positive. Perron--Frobenius supplies a
simple positive spectral radius $\rho$, positive left and right eigenvectors,
and $|\mu|<\rho$ for every other eigenvalue. Moreover $C\mathbf1>\mathbf1$,
so $\rho>1$. For

$$
s_n=e_1^{\mathsf T}C^n\mathbf1,
$$

the Perron projection has a strictly positive coefficient:

$$
s_n=\gamma\rho^n+O(\theta^n),\qquad
\gamma=\frac{(e_1^{\mathsf T}r)(\ell^{\mathsf T}\mathbf1)}
{\ell^{\mathsf T}r}>0,\quad \theta<\rho.
$$

Together with exact visibility this proves

$$
\lambda_1(F)=\lim_n\deg(F^n)^{1/n}=\rho.
$$

Since the irreducible monic integral characteristic polynomial has degree
$d$, it is the minimal polynomial of $\rho$. Thus $\rho$ is a Perron
algebraic integer of degree exactly $d$; all its other conjugates are the
other roots and have strictly smaller modulus.

Cayley--Hamilton supplies a rational constant-coefficient recurrence of
order at most $d$ for $s_n$. For the lower bound, irreducibility implies
that every nonzero state is cyclic. If a polynomial $f$ of degree below $d$
satisfied $f(C)\mathbf1=0$, Bézout with the irreducible $\chi_C$ would give
$\mathbf1=0$. Therefore

$$
\mathcal R=
\begin{bmatrix}\mathbf1&C\mathbf1&\cdots&C^{d-1}\mathbf1\end{bmatrix}
$$

is invertible. Applying the same argument to $C^{\mathsf T}$ and $e_1$
shows that

$$
\mathcal O=
\begin{bmatrix}
e_1^{\mathsf T}\\e_1^{\mathsf T}C\\\vdots\\
e_1^{\mathsf T}C^{d-1}
\end{bmatrix}
$$

is invertible. Hence the Hankel matrix

$$
\mathcal H_d=\mathcal O\mathcal R
=(s_{i+j})_{0\le i,j<d}
$$

has rank $d$. A from-start recurrence of order $k<d$ would force its Hankel
rank to be at most $k$, a contradiction.

The same order is minimal even for an eventual recurrence. If
$f(t)=\sum_{j=0}^k f_jt^j$ with $k<d$ annihilated all sufficiently late
windows, then division of

$$
\sum_j f_js_{n+j}
=\gamma\rho^n f(\rho)+O(\theta^n)
$$

by $\rho^n$ and passage to the limit would give $f(\rho)=0$. That is
impossible below the degree of the minimal polynomial. Thus the global and
eventual minimal rational scalar recurrence orders are both exactly $d$.

## Support-rank sharpness

For the family,

$$
D=-I_d+I_d(D+I_d),\qquad
B_0=-I_d+(b\mathbf1)\mathbf1^{\mathsf T}.
$$

The diagonal matrix $D+I_d$ is invertible, so

$$
\operatorname{rank}
\begin{bmatrix}D+I_d\\\mathbf1^{\mathsf T}\end{bmatrix}=d.
$$

Thus the selected support-row rank is $r=d$. Irreducibility of the
degree-$d$ characteristic polynomial for $d\ge2$ excludes the factor
$t-1$, so all $d$ characteristic degrees are nonunit and the Part-I bound is
attained. This is existential sharpness for every constructed nontrivial
rank $r=d\ge2$, not a claim about every presentation and not a rank-one
construction.

## Portfolio subtraction, anti-claims, and standalone mass

The internal lineage audit subtracts the following occupied ground:

- Paper 22 owns the arbitrary-mode endpoint-spiked family, the common
  identity sector, and the cubic quotient/cubic recurrence mechanism.
- Paper 23 owns the fixed positive four-mode family and irreducible quartic
  subfamily. A $d=4$ instance or isolated $d=5$ continuation is insufficient.
- Paper 24 owns forced period-two selector exchange, parity monodromy, and
  stride-two recurrence. Paper 25 is stationary and uses a strict invariant
  visibility chamber, not a selector-period or automaton mechanism.
- Papers 20 and 21 already supply the stationary quadratic and cubic
  selector-to-degree-matrix grammar.

The surviving conjunction is the full support-row-rank upper law, a literal
positive Hamiltonian realization attaining it for every $d\ge2$, exact
$q_1$-visible ordinary degrees, unbounded Perron algebraic degree, and exact
unbounded scalar recurrence order.

The package correctly makes no claim of arbitrary signs, arbitrary supports,
arbitrary exponent profiles or coefficients, arbitrary shear words, every
weak Perron realization, minimal ambient dimension, optimal sparsity,
inverse-degree behavior, higher dynamical degrees, compactification, entropy
equality, integrability, selector periodicity, finite automata, genericity,
classification, nonconjugacy, positive-characteristic validity, exact unit
multiplicity, novelty of a $d=5$ case, or absolute priority.

There are fifteen natural lemma/proof units. A credible standalone
proof-first allocation, excluding references, is:

| Material | Pages |
|---|---:|
| abstract, introduction, and bounded related work | 3.5 |
| support-rank factorization and boundary cases | 2.5 |
| family, parameters, gradients, and symplecticity | 3.5 |
| broad and fine cones | 4.0 |
| carries, noncancellation, and exact visibility | 4.0 |
| characteristic arithmetic and irreducibility | 3.0 |
| Perron degree and scalar minimality | 3.0 |
| sharpness, limitations, and conclusion | 2.5 |
| **Total** | **26.0** |

This lies inside the 22--30-page band and remains credible after Papers
22--24 are subtracted. No appendix or computational certificate is needed to
carry a theorem-critical step.

## Primary-source verification through 2026-08-26 UTC

The source screen was closed after the eight required records. The following
metadata and claim boundaries were checked from direct public primary or
authoritative records:

1. Jérémy Blanc and Immanuel van Santen,
   [Dynamical degrees of affine-triangular automorphisms of affine spaces](https://arxiv.org/abs/1912.01324),
   submitted 2019-12-03 and revised through v2 on 2021-03-13. The official
   [version of record](https://doi.org/10.1017/etds.2021.90) is in
   Ergodic Theory and Dynamical Systems 42(12), 3551--3592 (2022), published
   online 2021-10-01. Its abstract states weak-Perron realization by
   affine-triangular automorphisms in some dimension. It therefore blocks a
   general or first realization claim but does not prove the present
   Hamiltonian support-rank conjunction.

2. Enbo Shao and Xiaosong Sun,
   [Dynamical degrees of affine-triangular automorphisms in dimension four](https://arxiv.org/abs/2509.14584),
   v1 submitted 2025-09-18. Its Theorem 1.4 bounds the algebraic degree in
   the four-dimensional affine-triangular setting and motivates higher
   dimensions. It does not state an arbitrary-$d$ positive Hamiltonian
   support-rank family.

3. Nguyen-Bac Dang and Charles Favre,
   [Spectral interpretations of dynamical degrees and applications](https://annals.math.princeton.edu/2021/194-1/p05),
   Annals of Mathematics 194(1), 299--359 (2021),
   DOI 10.4007/annals.2021.194.1.5. It supplies broad spectral and
   algebraicity context, not the selected-gradient visibility or scalar
   minimality theorem here.

4. Pierre Berger and Dmitry Turaev,
   [arXiv:2210.14710](https://arxiv.org/abs/2210.14710), supplies
   position/momentum shear generation and approximation context. The arXiv
   metadata literally misspells the title word as “Hamitonian”; the
   authoritative [version of record](https://link.springer.com/article/10.1007/s11856-024-2709-7)
   uses “Hamiltonian,” Israel Journal of Mathematics 267, 237--252 (2025),
   published online 2024-12-18. A later bibliography must preserve the
   source-specific metadata rather than silently treating the two title
   strings as identical. Neither version proves polynomial iterate-degree
   rank sharpness.

5. Hans Koch and Héctor E. Lomelí,
   [On Hamiltonian flows whose orbits are straight lines](https://arxiv.org/abs/1304.3377),
   submitted 2013-04-11. It develops affine-integrable Hamiltonian flows and
   shear factorization context. It does not supply this cone, recurrence, or
   support-rank theorem.

6. Julie Déserti,
   [Degree growth of polynomial automorphisms and birational maps: some examples](https://arxiv.org/abs/1602.04642),
   revised through v4 on 2016-07-14 and published in European Journal of
   Mathematics 4, 200--211 (2018). Its higher-dimensional degree-growth
   examples are object-distinct from the frozen conjunction.

7. Marc Abboud and Junyi Xie,
   [Dynamical degrees of twisted rational maps](https://arxiv.org/abs/2608.09275),
   v1 submitted 2026-08-10. It concerns twisted rational maps, relative
   dynamics, limits, birational invariance, and conditional algebraicity,
   not polynomial Hamiltonian product shears.

8. Randell Heyman and Igor E. Shparlinski,
   [Counting irreducible binomials over finite fields](https://arxiv.org/abs/1504.01172),
   Finite Fields and Their Applications 38, 1--12 (2016). Lemma 6 states
   the three-part irreducible-binomial criterion used above, including the
   separate clause when $4$ divides the exponent. The project still checks
   every hypothesis and does not claim novelty for that criterion.

No direct collision with the complete support-rank, sharp positive
Hamiltonian, exact-visibility, and scalar-minimality package was found in
this bounded eight-record primary-source screen through the cutoff. This is
only bounded noncollision. It is not exhaustive and supports no first,
only, unprecedented, or absolute-priority language.

The standard Sylvester identity, determinant lemma, Dirichlet theorem,
cyclicity of finite-field multiplicative groups, Gauss lemma,
Perron--Frobenius theorem, and Cayley--Hamilton theorem are expanded or have
their hypotheses checked in the proof package, but final bibliography
sources for them are not yet assigned. That is a downstream bibliographic
task, not permission to invent metadata and not a source-design blocker.

## Finding ledger and scores

| Class | Count | Disposition |
|---|---:|---|
| Hard blocker | 0 | PASS |
| Major mathematical defect | 0 | PASS |
| Minor mathematical defect | 0 | PASS |
| Evidence or inventory defect | 0 | PASS |
| Citation-boundary defect | 0 | PASS |
| Authority expansion | 0 | PASS |
| Nonblocking control notes | 2 | recorded below |

The two nonblocking notes are:

1. The final sentence of experiments/EXPERIMENT_PLAN.md uses the phrase
   “written blocker.” It is nonoperative. The controlling ledger requires
   zero filesystem writes on any review blocker, and that rule governed this
   review.
2. The Berger--Turaev arXiv title typo and corrected version-of-record title
   must be represented accurately in any later bibliography. Bibliographic
   metadata is not locked at this stage.

Review scores are:

| Dimension | Score / 10 | Basis |
|---|---:|---|
| Proof correctness and boundary control | 9.7 | complete independent rederivation; no open mathematical gap |
| T10 evidence and reproducibility | 10.0 | exact independent no-follow inventory and framed aggregate |
| Citation accuracy and positioning | 9.2 | all eight required primary records checked; standard-theorem bibliography remains downstream |
| Portfolio differentiation | 8.5 | meaningful bounded conjunction after predecessor subtraction, without a priority claim |
| Standalone paper potential | 8.6 | credible 26-page proof-first mass |

## Permission and sole-write discipline

The nonoperative “written blocker” wording in the scientific plan did not
control this review. Had any blocker survived, I would have made zero
filesystem writes. Because every required conjunct passed, the only
authorized write is this independent review file, created by apply_patch.

This review does not create or authorize a source lock, paper plan,
publication scope or lock, manuscript, bibliography, figure, code, run,
scientific experiment, build, PDF, release, registry change, successor-paper
work, submission, upload, hosting, repository push, external message, or
other external effect. It does not mutate or correct any frozen T10 byte.
Only a separate parent ledger transition may consume the terminal verdict.

SOURCE_DESIGN_PASS
