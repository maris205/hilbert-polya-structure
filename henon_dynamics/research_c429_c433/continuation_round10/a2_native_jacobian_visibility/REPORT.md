# R10: native Jacobian visibility at every return level

2026-09-10 UTC. One bounded local-iteration mechanism.

## 1. Exact question and initial status

Let $p$ be any odd prime, $k=\overline{\mathbf F}_p$,
$f=x^2+c$ with arbitrary $c\in k$, and let
$w\in k(x)^\times$ satisfy $w(x)w(-x)=1$. Use the accepted R9
normalization

$$w=\eta A/B,\qquad \eta\in\{1,-1\},\qquad
B(X)=(-1)^mA(-X),$$

where $A,B$ are coprime monic polynomials of degree $m$, neither
vanishing at zero. Let $F_n=f^{\circ n}(x)-x$ and

$$C_n(x)=\eta^n\prod_{i=0}^{n-1}A(f^{\circ i}(x))
             -\prod_{i=0}^{n-1}B(f^{\circ i}(x)).$$

The R9 condition $U_n(S)=0$ is precisely

$$F_n\mid S F_n'C_n\qquad(n\ge1). \tag{1.1}$$

**Frozen question.** If one nonzero polynomial $S\in k[x]$
satisfies (1.1) for every $n\ge1$, must $w$ satisfy the ordinary
cofinite native-cycle product condition (CP)? All odd primes,
all constants, and all rational norm-one functions remain in scope.

**Initial status: NOT CURRENTLY JUSTIFIED.** The requested success
is either a full converse or an actual rational norm-one $w$, fixed
$S$, and cofinite failure satisfying all the identities. A point
masked at one higher return or an abstract formal germ is not that
counterexample.

## 2. The single decisive mechanism, frozen before proof

For a primitive cycle $O$ of least native period $r$ and $a\in O$,
put

$$e_O(k)=\operatorname{ord}_a(f^{\circ rk}(x)-x),\qquad
W_O=\prod_{a\in O}w(a)$$

when the cycle avoids the zeros and poles of $w$.
The exact proposed detector is: outside the finite roots of $S$
and the support of $w$, all the identities (1.1) constrain $W_O^k$
only at those multiples for which $p\nmid e_O(k)$.

The local proof must determine whether native multiplicity divisible
by $p$ remains invisible at every multiple, using actual iteration.
If such cycles exist, the missing global obligation remains whether
a rational norm-one observable can fail on infinitely many of them
while satisfying the tested products everywhere else. That implication
is not assumed from the local criterion.

The accepted R9 A1 report was actually read, including Sections 2--4
and 8; its all-word certificate is not rerun here. This task does not
duplicate A1's annihilator-ideal or degree-bound investigation.
Only this new report is writable. At most two new targeted source
batches are allowed; no mathematical program, census, nested agent,
external model/API, GPU, Git, old/shared-file, or PDF edit is allocated.

## 3. Exactly what the derivative detects

Write a nonzero polynomial locally as
$F=(x-a)^eV$ with $V(a)\ne0$. If $p\nmid e$, then
$\operatorname{ord}_aF'=e-1$. If $p\mid e$, then
$F'=(x-a)^eV'$, so $\operatorname{ord}_aF'\ge e$
(including $F'=0$). Consequently, for every polynomial $H$,

$$F\mid F'H\quad\Longleftrightarrow\quad
 H(a)=0\ \text{at every root }a\text{ whose multiplicity is prime to }p.
 \tag{3.1}$$

This follows by checking the order at each distinct root in the
algebraically closed field; no squarefreeness is assumed.
For an admissible primitive cycle $O$ of period $r$, and $n=rk$,

$$C_n(a)=\left(\prod_{i=0}^{n-1}B(f^{\circ i}(a))\right)
                    (W_O^k-1),\qquad a\in O. \tag{3.2}$$

The prefactor is nonzero. Thus the local condition at $a$ for
(1.1) is automatic if $p\mid e_O(k)$, and otherwise is exactly
$S(a)(W_O^k-1)=0$. This statement alone does not say which
multiples have prime-to-$p$ multiplicity.

## 4. The local iteration input, with a complete mod-p proof

The ramification congruence used below is classical, not a new claim.
Sen's theorem gives the stronger successive congruences modulo
$p^j$. The present argument only needs their mod-$p$ consequence.
The following proof spells out that consequence without an appeal
to an unproved intuition about $p$-fold iteration.

**Lemma 4.1 (the needed weak Sen congruence).** Let $K$ have
characteristic $p$, and let $\phi(z)=z+O(z^2)\in K[[z]]$ have
infinite compositional order. Set
$i(\phi)=\operatorname{ord}_z(\phi(z)-z)-1$. Then

$$i(\phi^{\circ k})\equiv i(\phi)\pmod p
                  \qquad\text{for every integer }k\ge1. \tag{4.1}$$

**Proof.** All the numbers in question are finite. A leading-term
induction, and the corresponding calculation for the inverse, give

$$i(\theta^{\circ u})=i(\theta)\quad(p\nmid u),\qquad
  i(\theta^{\circ u})\ge i(\theta)\quad(u\ne0) \tag{4.2}$$

for any infinite-order tangent-to-identity series $\theta$ and any
integer $u$ to which the displayed condition applies. Explicitly,
if $\theta=z+bz^{d+1}+O(z^{d+2})$, composition adds the coefficient
$b$, and inversion changes it to $-b$. Iteration cannot introduce
a term of smaller degree. In particular,
$j=i(\phi^{\circ p})>i=i(\phi)$.

For every integer $m$ define a Laurent series

$$E_m^{\theta}(z)=
\begin{cases}
 \prod_{v=0}^{m-1}\theta^{\circ v}(z),&m>0,\\
 1,&m=0,\\
 \left(\prod_{v=m}^{-1}\theta^{\circ v}(z)\right)^{-1},&m<0.
\end{cases} \tag{4.3}$$

Negative iterates exist because the linear coefficient is one.
These choices, including the negative-index convention, give

$$E_m^{\theta}=z^m(1+O(z)),\qquad
 \frac{E_m^{\theta}\circ\theta}{E_m^{\theta}}
       =\frac{\theta^{\circ m}(z)}{z}. \tag{4.4}$$

For $m\ne0$ it follows that

$$\operatorname{ord}_z(E_m^{\theta}\circ\theta-E_m^{\theta})
      =m+i(\theta^{\circ m}). \tag{4.5}$$

Every Laurent series has a unique convergent expansion
$\sum_{m\ge m_0}b_mE_m^{\theta}$: subtract its leading monomial
coefficient times $E_{m_0}^{\theta}$ and repeat in increasing order.
Composition and subtraction commute with this expansion because
they are continuous in the $z$-adic topology.

Suppose, for a contradiction, that $s=i-j$ is not divisible by $p$.
Put $\psi=\phi^{\circ p}$ and $Z=E_s^{\psi}$. By (4.2) and
(4.5),

$$\operatorname{ord}_z(Z\circ\psi-Z)=s+j=i. \tag{4.6}$$

Let $H=\sum_{v=0}^{p-1}Z\circ\phi^{\circ v}$. Each summand
has leading term $z^s$, so $\operatorname{ord}_zH>s$, unless
$H=0$. But the telescoping identity

$$H\circ\phi-H=Z\circ\psi-Z \tag{4.7}$$

and (4.6) show that $H\ne0$. Expand
$H=\sum_{m>s}b_mE_m^{\phi}$. If $p\nmid m$, the difference
of its $m$th basis term under $\phi$ has order $m+i$ by (4.2).
If $p\mid m$ and $m\ne0$, write
$\phi^{\circ m}=\psi^{\circ(m/p)}$; its order in (4.5) is
at least $m+j>s+j=i$. The $m=0$ term has zero difference.

Thus any nonzero term with $s<m<0$ and $p\nmid m$ has order
below $i$, distinct from those of all the other such terms.
If at least one occurs, the smallest of these finitely many orders
cannot cancel. If none occurs, every nonzero term has order above
$i$. In neither case can $H\circ\phi-H$ have order exactly $i$,
contradicting (4.6)--(4.7). Therefore $j\equiv i\pmod p$.

Apply this result successively to $\phi^{\circ p^v}$. For
$k=p^vu$ with $p\nmid u$, (4.2) then proves (4.1). $\square$

The orbit-product/trace proof structure is classical. Its
negative-index definition and cancellation argument have been
explicitly supplied here; neither the full modulo-$p^j$ theorem
nor a characteristic-zero lifting theorem is needed for the
application below.

**Corollary 4.2 (permanent native blindness).** Let $a$ have native
period $r$ for $f=x^2+c$. Write
$\lambda_O=(f^{\circ r})'(a)$ and $e_O=e_O(1)$.

If $\lambda_O\ne1$, then $e_O=1$. If $\lambda_O=1$, then

$$e_O(k)\equiv e_O\pmod p\qquad(k\ge1). \tag{4.8}$$

Indeed $\phi(z)=f^{\circ r}(a+z)-a$ is tangent to the identity
in the second case. It has infinite compositional order: any
identity $\phi^{\circ k}=z$ of formal series would make the
polynomial $f^{\circ rk}(x)-x$ identically zero, contrary to its
degree $2^{rk}>1$. Apply Lemma 4.1 and add one.

The multiplier is the same at every point of the cycle. If it is
zero, every multiple-return multiplier is zero and every $e_O(k)$
is one. If it is nonzero, every derivative along the cycle is
nonzero; the local maps between consecutive points are formal
changes of coordinate and conjugate the return germs. Their
multiplicities, including those at every multiple, therefore agree.
This justifies the cycle notation $e_O(k)$ in every case.

In particular, $p\mid e_O$ implies $\lambda_O=1$ and
$p\mid e_O(k)$ for all $k$. Conversely, $p\nmid e_O$ makes
the native layer itself a detector. Formula (4.8) is **not**
asserted when $\lambda_O\ne1$; later resonances can hide a
cycle that its native layer detects.

## 5. An exact all-level statement, with the quantifiers retained

Call a primitive affine cycle **native-visible** if $p\nmid e_O$,
and **native-blind** if $p\mid e_O$. An admissible cycle avoids
the zeros and poles of $w$. Define visible CP to mean that
$W_O=1$ on all but finitely many admissible native-visible cycles.

**Theorem 5.1 (exact scope of the all-Jacobian certificate).**
For every odd $p$, every $c\in k$, and every rational norm-one
$w$ in Section 1,

$$\bigl[\exists\,0\ne S\in k[x]\ \forall n\ge1:
           U_n(S)=0\bigr]
\quad\Longleftrightarrow\quad
\bigl[\text{visible CP for }w\bigr]. \tag{5.1}$$

**Proof, forward.** At a native-visible admissible cycle use
$n=r$ in (3.1)--(3.2). If $S(a)\ne0$ at any point of the
cycle, its ordinary native product is one. Only finitely many
cycles can meet the finite root set of $S$. This proves visible
CP. No assertion about higher-return multiplicities is needed
in this direction.

**Proof, reverse.** There are finitely many exceptional admissible
native-visible cycles. There are also finitely many periodic
cycles meeting the finite zero/pole support of $w$. Let $T$ be
the union of all the points of these cycles, and take
$S=\prod_{a\in T}(x-a)$, with $S=1$ if $T$ is empty.
This is one fixed polynomial, independent of $n$.

Take any root $a$ of any $F_n$, and let $O$ be its native
cycle, of period $r\mid n$. If $O$ is native-blind,
Corollary 4.2 makes its local condition automatic at this level.
If $O\subseteq T$, then $S(a)=0$, which also suffices by (3.1).
In all remaining cases $O$ is admissible and native-visible
with $W_O=1$. Equation (3.2), for $k=n/r$, gives $C_n(a)=0$.
Thus every root satisfies (3.1), proving (1.1) for every $n$.
$\square$

The reverse proof keeps ordinary products even when $p\mid r$
or $p\mid k$. A good native product gives $W_O^k=1$ directly;
no prime-to-$p$ period restriction and no weighted orbit
convention have been introduced.

**Consequences with no overclaim.** Ordinary CP implies (5.1).
If a given quadratic has only finitely many native-blind cycles,
then (5.1) implies ordinary CP as well. In general the exact
remaining question is whether a rational norm-one $w$ with
visible CP must also have product one on all but finitely many
native-blind cycles. Theorem 5.1 does not answer it.

## 6. Actual quadratic controls: infinitely many permanently blind cycles

### 6.1 Monomial control; the one-level warning is repaired

Work in characteristic three with $f=x^2$. For a nonzero point
of native period $r$, and every multiple $n=rk$,

$$f^{\circ n}(x)-x=x(x^{2^n-1}-1),\qquad
 e_O(k)=3^{v_3(2^n-1)}. \tag{6.1}$$

To see the exact multiplicity, write $2^n-1=3^vM$ with
$3\nmid M$ and factor $x^{2^n-1}-1=(x^M-1)^{3^v}$;
the nonzero roots of $x^M-1$ are simple. It follows that
nonzero cycles of odd native period are visible, while those
of even native period are blind at every multiple.

For each $t\ge1$, choose a primitive $5^t$th root $a_t$.
Squaring permutes this finite root group, so $a_t$ is periodic.
Its native period $r_t$ satisfies $2^{r_t}\equiv1\pmod5$,
hence $4\mid r_t$. Equation (6.1) proves permanent blindness
at its native period and at every multiple. Iteration preserves
the exact root order, so different $t$ yield distinct cycles.
This gives infinitely many actual native-blind cycles in the
unchanged quadratic family, not merely an abstract formal germ.

For comparison, $a=1$ has native period one, multiplier $2\ne1$,
and native multiplicity one. Its multiplicity at level two is
three. This is why a masked higher return alone does not prove
permanent native blindness or an all-level failure.

### 6.2 Odd native periods can also be permanently blind

The root agent supplied the Chebyshev control; the following
argument verifies it without a period census. In characteristic
three take $f=x^2-2=x^2+1$ and
$\pi(u)=u+u^{-1}$, so $f\circ\pi(u)=\pi(u^2)$.
For each $t\ge1$ let $u_t$ be a primitive $11^t$th root.

Put $N_t=5\cdot11^{t-1}$. The elementary binomial induction
$(1+11b)^{11^j}\equiv1\pmod{11^{j+1}}$, applied to
$-32=1-33$, gives $2^{N_t}\equiv-1\pmod{11^t}$.
Thus $a_t=\pi(u_t)$ is periodic with native period $r_t\mid N_t$,
in particular $r_t$ is odd. The equality
$\pi(v)=\pi(u)$ is equivalent to $v\in\{u,u^{-1}\}$.
At the native return one must have $u_t^{2^{r_t}}=u_t^{-1}$:
the other possibility would, on iteration, contradict
$u_t^{2^{N_t}}=u_t^{-1}\ne u_t$.

For $n=r_tk$, therefore, $u_t^{2^n}=u_t^{(-1)^k}$. The identity

$$\pi(z^{2^n})-\pi(z)
  =\frac{(z^{2^n}-z)(z^{2^n}-z^{-1})}{z^{2^n}} \tag{6.2}$$

has exactly one vanishing numerator factor at $z=u_t$.
As $\pi'(u_t)=1-u_t^{-2}\ne0$, the multiplicity at $a_t$
equals its multiplicity in this coordinate, namely

$$e_{O_t}(k)=3^{v_3(2^n-(-1)^k)}. \tag{6.3}$$

Since $r_t$ is odd, $2^n\equiv(-1)^k\pmod3$, so this
multiplicity is divisible by three at every $k$, including
the native one. Distinct $t$ give distinct cycles, because
iteration and the identification $u\sim u^{-1}$ preserve
the exact order $11^t$. Thus blindness is not an even-native-
period phenomenon for all quadratics.

Neither control supplies a rational norm-one observable with
bad products on these cycles while satisfying visible CP.
They disprove a universal finite-blind-cycle repair, not the
all-$U_n$ converse for rational norm-one observables.

## 7. The unclosed rational-observable step

The bounded mechanism now gives an exact auxiliary equivalence,
not a disguised proof of the original converse. To refute that
converse one still needs an actual rational norm-one $w$ that
is good on all but finitely many native-visible cycles and bad
on infinitely many native-blind cycles. One fixed $S$ would
then follow from Theorem 5.1. No such $w$ is constructed here.

Conversely, a proof would have to show that rationality and the
norm-one condition force the missing blind products from visible
CP. Local iteration does not link the values of $w$ on distinct
cycles, and hence supplies no such implication by itself.
Assigning arbitrary products on the blind cycles is not a
rational-function construction. Infinite blindness, even at odd
native periods, is not an all-level counterexample.

## 8. Sources, subtraction, and execution boundary

The accepted R9 A1 report was read in full, with particular
attention to Sections 2--4 and 8. Its normalization, Jacobian
certificate, one-level warning, and finite all-word theorem are
inputs, not new claims. No all-word proof or annihilator-ideal
degree-bound argument was repeated.

The proof-writer skill was read and used to separate hypotheses,
the local lemma, the exact auxiliary theorem, controls, and the
remaining gap. The research-lit skill was read before the
source search and used for local-first retrieval and primary-
source applicability checks. The first local check found no
callable Zotero/Obsidian tools and no relevant local paper;
no unavailable knowledge base is represented as searched.

Exactly two targeted query batches were used, both on the new
precise ramification-congruence hypothesis: the first asked for
Sen congruences for iterated formal series, and the second for
the exact original theorem/title and primary proof sources.
No third query batch was run. Subsequent direct opens only
resolved sources returned by these batches.

The following are source distinctions, not novelty claims:

- [Berger--Rozensztajn, *Composition of power series*, Section 5](https://perso.ens-lyon.fr/sandra.rozensztajn/documents/WildPromys.pdf):
  the actual returned text through the ramification section was
  read. Its exercises provide a classical orbit-product/trace
  route. Lemma 4.1 fills in the weaker mod-$p$ argument, including
  the negative-index convention; the worksheet was not described
  as a fully written-out proof. A later direct reopen errored.
- [Sen, *On automorphisms of local fields*, Annals 90 (1969), 33--46](https://annals.math.princeton.edu/1969/90-1/p04):
  the primary journal page verifies title, author, pages, and DOI
  10.2307/1970680. Only that metadata page was opened; the original
  article proof was not read and is not claimed to have been read.
- [Berger, *The Weierstrass preparation theorem and resultants of p-adic power series*, Section 3](https://perso.ens-lyon.fr/laurent.berger/articles/article33.pdf):
  the actual section statement and proof were read. It attributes
  the congruence to Sen and discusses Lubin's lifting argument.
  It confirms the classical status and tangent-to-identity
  hypotheses. No lifting construction is imported into our
  quadratic proof; Lemma 4.1 is supplied directly.

The precise contribution of this lane is the application to the
native/multiple Jacobian detector with both directions of (5.1)
and actual all-multiple controls. The classical ramification
congruence, monomial/Chebyshev identities, and existence of
prime-power roots of unity are not represented as new theory.

No mathematical program, enumeration, nested worker, external
model/API, GPU, Git operation, old/shared-file edit, or PDF write
was performed. Shell use was limited to text/source inspection,
the authorized report edit, and final readback/checksum.

## 9. Final author status

Lemma 4.1, Corollary 4.2, Theorem 5.1, and the two infinite
native-blind controls have complete proofs above, subject to
independent review. The original all-parameter implication

$$\exists S\ne0\ \forall n:\ U_n(S)=0
                 \quad\Longrightarrow\quad \mathrm{CP}$$

remains **NOT CURRENTLY JUSTIFIED**. This report neither proves
it nor supplies the requested rational norm-one counterexample.
No admission, manuscript claim, or full bridge is inferred from
the auxiliary equivalence. The one-mechanism/two-batch budget
is exhausted and this lane stops at that honest boundary.
