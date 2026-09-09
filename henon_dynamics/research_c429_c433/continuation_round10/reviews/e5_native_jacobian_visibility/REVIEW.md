# R10 full nonauthor review: native Jacobian visibility

2026-09-10 UTC. Reviewer: E5. Current-team internal mathematical review.
This is not an admission, external peer review, or full MS6 conclusion.

## 1. Frozen version, exact question, and verdict

The entire actual author report was read:

- `continuation_round10/a2_native_jacobian_visibility/REPORT.md`;
- 411 lines;
- SHA256: `46a8d605900a3145134a0074371ea170c6ed8d2ba54aa8c046ed6e59c7c2dd0b`.

The accepted R9 A1 report at
`continuation_round9/a1_general_quadratic_normone/REPORT.md` was
also read in full to check the normalization and the exact interface
with $U_n$. Its accepted all-word theorem was not rerun or re-audited
as a new R10 claim.

Fix any odd prime $p$, $k=\overline{\mathbf F}_p$, arbitrary
$c\in k$, $f=x^2+c$, and a rational function $w\ne0$ with
$w(x)w(-x)=1$. The original question is whether

$$\exists S\in k[x]\setminus\{0\}\ \forall n\ge1:
F_n\mid S F_n'C_n$$

implies the ordinary cofinite native-cycle product condition (CP).
The exponent, denominator, and multiple-atom content of the entire
$w$ are retained; no factorwise (CP) assumption is introduced.

**Auxiliary verdict: PROVABLE AS STATED.** Lemma 4.1, Corollary 4.2,
Theorem 5.1, and both infinite families of permanently native-blind
cycles have valid proofs. There are **zero unresolved mathematical
or source-applicability must-fixes** in the frozen report. No author
repair was requested.

**Original all-$U_n$ converse: NOT CURRENTLY JUSTIFIED.** The report
correctly stops at visible CP. Neither the monomial nor the Chebyshev
control supplies a rational norm-one observable satisfying all the
identities while failing ordinary CP. Infinite blind cycles are not
by themselves such a counterexample. The reported four contracts and
zero completed papers are not changed by this review.

## 2. Normalization, native products, and the derivative criterion

The accepted normalization is applicable, including constants:

$$w=\eta A/B,\qquad B(X)=(-1)^mA(-X),\qquad \eta\in\{1,-1\},$$

where $A,B$ are coprime monic polynomials of equal degree $m$ and
$A(0)B(0)\ne0$. Indeed the norm-one identity pairs opposite divisor
orders at $a,-a$, and forces zero order at both $0$ and infinity.
Monicity fixes $B$; the value at infinity gives $\eta^2=1$.
Arbitrary positive root multiplicities in $A,B$ remain integer
multiplicities, not their residues modulo $p$.

For $n\ge1$, write

$$F_n=f^{\circ n}(x)-x,\qquad
C_n=\eta^n\prod_{i=0}^{n-1}A(f^{\circ i}(x))
-\prod_{i=0}^{n-1}B(f^{\circ i}(x)).$$

Under the accepted isomorphism
$\mathcal A_n\simeq k[x]/(f^{\circ n}(x)-x)$, the Jacobian factor
$2^n\prod_iX_i-1$ is exactly $F_n'$. Thus the R10 condition is
the actual R9 identity $U_n(S)=0$, for every $n\ge1$, with no
change of clock or of quotient scheme.

For a nonzero polynomial $F=(x-a)^eV$, $V(a)\ne0$, direct
differentiation gives

$$\operatorname{ord}_aF'=e-1\quad(p\nmid e),\qquad
\operatorname{ord}_aF'\ge e\quad(p\mid e).$$

In the second case the first derivative summand has coefficient zero
in the field; $F'=(x-a)^eV'$, possibly zero. Since a polynomial
$H$ has nonnegative order at $a$, local divisibility of $F'H$ by
$F$ is automatic in this case. In the first case it is equivalent
to $H(a)=0$. Checking every distinct root proves author (3.1).
In particular, the derivative requires only one additional zero at a
visible root, regardless of how large its multiplicity is.

Let an admissible primitive cycle $O$ have least native period $r$,
and put $n=rk$. Each of its $r$ distinct points occurs exactly $k$
times in the $n$-step numerator and denominator products. Hence

$$C_n(a)=\left(\prod_{i=0}^{n-1}B(f^{\circ i}(a))\right)
(W_O^k-1),\qquad W_O=\prod_{a\in O}w(a).$$

The prefactor is nonzero, and $\eta^n=(\eta^r)^k$ is retained.
Thus the visible local condition is exactly
$S(a)(W_O^k-1)=0$. There is no evaluation of a transfer quotient
at a cancelled zero, and no scheme weighting of $W_O$.
At cycles meeting the support of $w$, the proof uses the polynomial
$C_n$ and the exceptional factor $S$, not an undefined product.

## 3. Independent reconstruction of the weak Sen argument

The formal lemma is the most substantial new proof obligation in
this review. Its assumptions are a field $K$ of characteristic $p$
and a tangent-to-identity series $\phi(z)=z+O(z^2)$ of infinite
compositional order. All statements below concern formal $z$-adic
Laurent series, not analytic convergence or a characteristic-zero lift.

### 3.1. Finite indices and integer iterates

Let $\theta$ be any infinite-order tangent-to-identity series. Every
nonzero integer iterate is different from the identity, so every index
$i(\theta^{\circ u})=\operatorname{ord}(\theta^{\circ u}-z)-1$
used below is finite. An inverse exists because the linear coefficient
is one. If $\theta=z+bz^{d+1}+O(z^{d+2})$, $b\ne0$, its inverse
has leading nonlinear coefficient $-b$. Positive and negative
composition therefore give coefficient $ub$ when $p\nmid u$,
and cannot create a smaller-degree nonlinear term for any $u\ne0$.
This proves

$$i(\theta^{\circ u})=i(\theta)\ (p\nmid u),\qquad
i(\theta^{\circ u})\ge i(\theta)\ (u\ne0).$$

For $i=i(\phi)$ and $j=i(\phi^{\circ p})$, the leading coefficient
cancels on $p$-fold composition, so $j>i$. Infinite order is what
ensures that $j$ is nevertheless finite.

### 3.2. The Laurent basis, including negative indices

For $m>0$, define $E_m^\theta=\prod_{v=0}^{m-1}\theta^{\circ v}(z)$;
for $m<0$, define
$E_m^\theta=(\prod_{v=m}^{-1}\theta^{\circ v}(z))^{-1}$; set
$E_0^\theta=1$. Negative $v$ here denote compositional inverses,
and the outer inverse for $m<0$ is the multiplicative Laurent inverse.

Each factor has leading term $z$, and direct cancellation of the
shifted index sets gives

$$E_m^\theta=z^m(1+O(z)),\qquad
\frac{E_m^\theta\circ\theta}{E_m^\theta}
=\frac{\theta^{\circ m}(z)}{z}.$$

For example, at $m=-1$ the ratio is
$(1/z)/(1/\theta^{\circ(-1)}(z))=\theta^{\circ(-1)}(z)/z$,
so the sign and negative-index convention really agree. For every
$m\ne0$ it follows that

$$\operatorname{ord}(E_m^\theta\circ\theta-E_m^\theta)
=m+i(\theta^{\circ m}).$$

The leading coefficient one and strictly increasing leading exponents
make $\{E_m^\theta\}$ a triangular topological basis: recursively
remove the lowest Laurent coefficient to express any series uniquely
as $\sum_{m\ge m_0}b_mE_m^\theta$. The lower bound $m_0$ is
finite. Substitution by a series with leading term $z$ preserves
valuation and is continuous, so differences may be taken termwise.
More explicitly their valuations are at least $m+i(\theta)$ and
tend to infinity with $m$, ruling out a hidden low-order tail term.

### 3.3. The trace contradiction

Suppose $s=i-j$ is not divisible by $p$. It is a negative integer.
Set $\psi=\phi^{\circ p}$ and $Z=E_s^\psi$. The prime-to-$p$
iterate formula, including negative $s$, gives

$$\operatorname{ord}(Z\circ\psi-Z)=s+j=i.$$

Let $H=\sum_{v=0}^{p-1}Z\circ\phi^{\circ v}$. Every summand
has leading term $z^s$, so the coefficient at that power is zero
in characteristic $p$. Thus either $H=0$ or $\operatorname{ord}H>s$.
The finite sum telescopes to

$$H\circ\phi-H=Z\circ\psi-Z,$$

whose right side is nonzero and has order $i$. In particular $H$
is a nonzero Laurent series of finite order and can be expanded as
$H=\sum_{m>s}b_mE_m^\phi$.

The cancellation analysis of this expansion is complete:

- If $s<m<0$ and $p\nmid m$, the corresponding nonzero difference
  has order $m+i<i$. These orders are pairwise distinct, and there
  are only finitely many such negative integers.
- If $m>0$ and $p\nmid m$, its order is $m+i>i$.
- If $p\mid m$, $m\ne0$, then
  $\phi^{\circ m}=\psi^{\circ(m/p)}$, so the order is at least
  $m+j>s+j=i$. This also covers negative $m$ divisible by $p$.
- The $m=0$ term has zero difference.

If a negative prime-to-$p$ term occurs, the smallest order below $i$
has exactly one contributor and cannot cancel. If no such term occurs,
the difference has order strictly above $i$, or is zero. Continuity
and the growing valuations exclude cancellation involving an infinite
tail. Neither possibility gives order exactly $i$, contradicting
the telescoping identity. Therefore $j\equiv i\pmod p$.

Applying this result successively to $\phi^{\circ p^v}$, which
remain infinite-order tangent series, gives the congruence for all
$p$-power iterates. Writing $k=p^vu$ with $p\nmid u$ and using
the leading-term formula gives author (4.1) for every $k\ge1$.
The proof works over any coefficient field of characteristic $p$;
no perfectness, finite coefficient field, or divided trace is used.

## 4. Native return multiplicities and the multiplier cases

At a periodic point $a$ of native period $r$, the return germ is
$\phi(z)=f^{\circ r}(a+z)-a$. Write
$\lambda_O=\phi'(0)$, $e_O(k)=\operatorname{ord}_aF_{rk}$, and $e_O=e_O(1)$.
If its multiplier is one, this germ
has infinite compositional order: an identity $\phi^{\circ k}=z$
would make the entire polynomial $f^{\circ rk}(x)-x$ zero, whereas
its degree is $2^{rk}>1$. Its orders are therefore finite, and
$e_O(k)=i(\phi^{\circ k})+1$ gives

$$e_O(k)\equiv e_O(1)\pmod p\qquad(\lambda_O=1).$$

The three cases are genuinely different:

| Native multiplier | Native multiplicity | What holds at multiples |
| --- | --- | --- |
| $\lambda_O=0$ | $e_O=1$ | Every multiple has multiplier zero and multiplicity one. |
| $\lambda_O\ne0,1$ | $e_O=1$ | The native layer detects the cycle; if $\lambda_O^k\ne1$, that multiple is simple, but a resonant multiple can be blind. |
| $\lambda_O=1$ | $e_O\ge2$ | All $e_O(k)$ have the same residue modulo $p$ as $e_O$. |

The multiplier is the cyclic product of the derivatives and is the
same at every point of $O$. When it is zero, simplicity at every
multiple settles phase-independence without using invertible local
maps. When it is nonzero, every derivative along the cycle is nonzero;
the local maps between phases are formal coordinate changes that
conjugate the return germs and all their multiples. Thus $e_O(k)$
is independent of the selected phase in all cases.

If $p\mid e_O$, then $e_O>1$, so $\lambda_O=1$ and the
congruence makes every multiple blind. If $p\nmid e_O$, the native
layer itself is a detector. The report does not extend the congruence
to $\lambda_O\ne1$ or assume that all later multiples of a
native-visible cycle remain visible.

## 5. The all-level quantifiers are exactly visible CP

Theorem 5.1 preserves one fixed polynomial $S$ for every $n$.
In the forward direction, take the native layer $n=r$ of an
admissible native-visible cycle. If any point on it is not a root
of $S$, the local criterion forces $W_O=1$. A bad such cycle would
have all its points among the finite roots of $S$, so only finitely
many bad admissible native-visible cycles are possible.

Conversely, visible CP gives finitely many bad admissible
native-visible cycles. Only finitely many cycles meet the finite
zero/pole support of $w$. Let $T$ be the finite union of all points
of these two collections, and put $S=\prod_{a\in T}(x-a)$,
or $S=1$ when $T$ is empty. This polynomial is chosen once.

For a root $a$ of any $F_n$, its native period $r$ divides $n$.
There are exactly the cases used by the author:

1. If its cycle is native-blind, permanent blindness makes the
   divisibility condition automatic at this multiple.
2. If its cycle lies in $T$, the factor $S(a)=0$ suffices even
   if $C_n(a)$ is not zero.
3. Otherwise the cycle is admissible, native-visible, and good;
   $W_O=1$ gives $C_n(a)=0$ at every multiple.

This verifies the local criterion at all roots and proves all the
identities simultaneously. A simple zero of $S$ suffices by Section 2;
no unbounded root multiplicity needs to be built into $S$.
The argument remains valid when $p$ divides $r$ or $n/r$, since a
good native product gives $W_O^{n/r}=1$ directly.

Ordinary CP implies visible CP. Conversely, finitely many native-blind
cycles would allow visible CP to imply ordinary CP. The two explicit
families below disprove the assertion that every quadratic parameter
has only finitely many blind cycles, not the desired converse for a
rational norm-one observable. Infinity, if one includes it, adds at
most one exceptional cycle and does not change this cofinite statement.

## 6. Monomial control: infinitely many all-multiple blind cycles

In characteristic three with $f=x^2$, write $n=rk$ for the native
period $r$ of a nonzero point. The factorization

$$F_n=x(x^{2^n-1}-1),\qquad
x^{2^n-1}-1=(x^M-1)^{3^v},\quad
2^n-1=3^vM,\quad 3\nmid M$$

shows that the exact multiplicity is $3^v$, because $x^M-1$ has
simple nonzero roots. Thus
$e_O(k)=3^{v_3(2^n-1)}$ as stated.
Odd native period gives multiplicity one at the native layer;
even native period makes every multiple even, hence gives
multiplicity divisible by three at every multiple.

Primitive $5^t$th roots exist for every $t\ge1$ and have a finite
squaring orbit. Their native periods satisfy $2^r\equiv1\pmod5$,
so $4\mid r$. They are permanently blind by the preceding exact
formula. Squaring preserves the exact odd root order $5^t$;
cycles from different $t$ are disjoint, so there are infinitely many.
No finite period census or assertion of an exact order modulo $5^t$
is needed.

The comparison point $a=1$ really has native multiplier $2\ne1$
and native multiplicity one, but at level two
$F_2=x(x-1)^3$ and its multiplicity is three. It is detected at
its native layer, not permanently blind. This correctly repairs the
possible overinterpretation of the already recorded one-level warning.

## 7. Chebyshev control: odd native periods and exact multiplicities

The coordinator supplied this example and the author disclosed that
origin. This review independently checks its mathematics; it is not
represented as a blind-discovery experiment.

In characteristic three, take $f=x^2-2=x^2+1$ and
$\pi(u)=u+u^{-1}$. Direct expansion gives
$f\circ\pi(u)=\pi(u^2)$. Let $u_t$ have exact order $11^t$ and
let $N_t=5\cdot11^{t-1}$. Since $-32=1-33$, the binomial
congruence $(1+11b)^{11^j}\equiv1\pmod{11^{j+1}}$ gives

$$2^{N_t}\equiv-1\pmod{11^t}.$$

Indeed $11^{t-1}$ is odd, so raising $-32$ to this power gives
$-2^{N_t}$. The point $a_t=\pi(u_t)$ is therefore periodic with
native period $r_t\mid N_t$. In particular its native period is
odd (and is also prime to three).

For nonzero $u,v$, $\pi(v)=\pi(u)$ is equivalent to
$(v-u)(v-u^{-1})=0$. Thus a native return of $a_t$ lifts either to
$u_t$ or $u_t^{-1}$. It must lift to $u_t^{-1}$: a return to
$u_t$ would also return it at the multiple $N_t$, contradicting
the displayed congruence and $u_t\ne u_t^{-1}$.
Consequently, for $n=r_tk$,

$$u_t^{2^n}=u_t^{(-1)^k}.$$

The identity

$$\pi(z^{2^n})-\pi(z)
=\frac{(z^{2^n}-z)(z^{2^n}-z^{-1})}{z^{2^n}}$$

is verified by multiplying out. Its denominator is a unit at $u_t$,
and exactly one numerator factor vanishes there, since $u_t$ has
odd order greater than two. Also $\pi'(u_t)=1-u_t^{-2}\ne0$,
so $z-u_t$ and $x-a_t$ are equivalent formal local parameters.
Pullback by $\pi$ preserves the vanishing order in question.

For even $k$, the vanishing factor is
$z(z^{2^n-1}-1)$; for odd $k$, it is
$z^{-1}(z^{2^n+1}-1)$. Factoring out the integer power of three
in these exponents gives simple remaining roots. This proves the
exact formula

$$e_{O_t}(k)=3^{v_3(2^n-(-1)^k)}.$$

Because $r_t$ is odd, $2^n\equiv(-1)^k\pmod3$, so every
one of these multiplicities, including the native one, is divisible
by three.
As an independent consistency check, differentiating the semiconjugacy
at a native inverse return gives multiplier $-2^{r_t}=1$ in
characteristic three. This agrees with the tangent-to-identity case;
the exact factorization, not the multiplier alone, proves divisibility
of the multiplicity by three.

Iteration by squaring and the identification $u\sim u^{-1}$ both
preserve exact root order. If cycles from different $t$ overlapped,
that identity would equate roots of different exact orders, impossible.
Thus these are infinitely many permanently blind cycles of odd native
period, not merely higher-level repetitions of finitely many cycles.

## 8. Primary-source scope and classical subtraction

The [Sen journal page](https://annals.math.princeton.edu/1969/90-1/p04)
was directly read: Shankar Sen, *On automorphisms of local fields*,
Annals of Mathematics 90 (1969), 33--46, DOI 10.2307/1970680.
This verifies metadata, not the contents of Sen's original proof.
I did not read that original article and do not claim otherwise.

I directly read Section 3 of [Laurent Berger's author manuscript](https://perso.ens-lyon.fr/laurent.berger/articles/article33.pdf),
including its statement of the ramification congruences, explanation
of Lubin's characteristic-zero lifting argument, and Theorem 3.1
with its displayed proof through the end of the section. It explicitly
attributes the congruences to Sen and presents the lifting approach
as classical. This supports the author's ownership subtraction.
R10 does not import that lift or its analytic hypotheses: the required
weaker congruence is proved directly in the formal Laurent argument
checked above. No full audit of Berger's other sections is claimed.

Two direct attempts to open the cited Berger--Rozensztajn worksheet
`WildPromys.pdf` failed. I therefore do not independently certify its
exercise text or represent it as a complete proof that I accessed.
This is not a missing hypothesis in R10: the actual Laurent proof
is self-contained, and the classical status of the congruence is
independently documented by Berger. The author's record of previously
reading the worksheet remains a separate access record.

The ramification theorem, monomial and Chebyshev semiconjugacies,
and roots-of-unity constructions are not assessed as new theory.
The accepted R9 whole-function normalization and annihilation interface
are also subtracted. No conclusion about global novelty or absence
of other applicable literature is made from these bounded checks.

## 9. Remaining global obligation and final handoff

The exact proved boundary is

$$\exists S\ne0\ \forall n\ge1:\ U_n(S)=0
\quad\Longleftrightarrow\quad
W_O=1\text{ on all but finitely many admissible native-visible cycles}.$$

To disprove the original converse one still needs an actual rational
norm-one $w$ with this property and bad products on infinitely many
native-blind cycles. To prove it one must show that rationality and
the whole norm-one constraint force cofinite goodness also on the
blind cycles. Neither local iteration nor an arbitrary assignment
of values on disjoint cycles establishes that implication.
The report constructs neither such a rational counterexample nor
such a global rigidity theorem.

No author repair was required. The proof-writer and research-review
requirements led to the split verdict: the auxiliary statements pass,
while the original implication remains NOT CURRENTLY JUSTIFIED.
The research-lit check retained the precise source-access and ownership
limits. Current-session internal review, not an external model call,
is the applicable repository workflow here.

Only this allocated new review file was written. No mathematical
program, certificate execution, parameter census, nested agent,
external model/API, GPU job, Git operation, manuscript/PDF, or
author/old/shared-file edit was performed. Primary-source access was
limited to the cited pages and within-document navigation, with no
new search-query batch and no local PDF download. The local relevant-
filename check found no matching paper; no exposed Zotero/Obsidian
tool was available. Hash checks establish provenance, not mathematics.

Final status: **PROVABLE AS STATED for all reviewed auxiliary claims;
NOT CURRENTLY JUSTIFIED for the original all-$U_n$-to-(CP) converse.
Zero unresolved mathematical/source-applicability must-fixes.
No rational norm-one counterexample or contract admission is claimed.**
