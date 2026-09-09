# E8 full nonauthor review: the excluded unicritical congruence

2026-09-10 UTC. Current-team independent mathematical review under the
proof-writer and research-review skills, with the repository's selected-model
and no-external-upload boundary. No mathematical program was run. The
accepted R4 result and all earlier files were treated as read-only inputs.

## Decision and reviewed versions

**PROVABLE AS STATED.** The complete author proof and report pass within
their stated scope. Open mathematical must-fixes: **0**. Open imported-source
applicability must-fixes: **0**. Required textual/minor repairs: **0**.

This decision covers the new all-$c$ excluded-congruence theorem and its
two-return Hasse certificate, not merely the report's monomial subfamily.
It is an extension within the same PC424-L paper question. No extra paper
count, worldwide priority, human review, or target-arithmetic grade is claimed.

Both actual files were read completely, including the proof's full Sections
5–9 and the report's conditional multiplicity alternative:

- [Proof package](../../a2_excluded_congruence/PROOF_PACKAGE.md): 517 lines;
  SHA256 `b703fde520e5405b6ab28833a40dcce324925bebbbeaefea6b9ca22de57445e3`.
- [Author report](../../a2_excluded_congruence/REPORT.md): 203 lines;
  SHA256 `2d99b82dc75d50d18b8e74eb20a12a97d9a1117e50a13f950c5dfb087b7f99a5`.

The author confirmed these versions are frozen and have no pending edits.
The reviewer independently checked both hashes. The applicable normal-form,
digit-basis and leading-digit passages of the
[R4 proof](../../../continuation_round4/a2_unicritical_carry_extension/PROOF_PACKAGE.md)
were read again; its unchanged SHA256 is
`766f8d95f3297fdfe2b803965bc217ed28ccc7934090c07c68f42c9624f0cd01`.

## Exact mathematical scope

Let $p$ be any odd prime, $k=\overline{\mathbf F}_p$, and let $d\ge2$
be any integer with $d\equiv1\pmod p$. For every $c\in k$ and
$f(x)=x^d+c$, the reviewed equality is

$$
K_f=\left\{h\in k[x]:\sum_{a\in O}h(a)=0
\text{ for every ordinary primitive }f\text{-orbit }O\right\}
=B_f=\{Q\circ f-Q:Q\in k[x]\}.
$$

Each distinct point is counted once, including primitive periods divisible
by $p$. The native map is not replaced by an iterate or a Frobenius clock.
There is no restriction to $c=0$, low degree, simple periodic roots, or
one finite field.

Put $P=p^{v_p(d-1)}$, $A=(d-1)/P$, and $\alpha=[A]\in k^\times$.
For any integer $M\ge1$ and any $h$ of degree at most $M$, including
zero, set $m=\lfloor\log_d(PM)\rfloor$ and $n=7m+22$.
The reviewed finite statement equates polynomial coboundary membership,
ordinary-root return-sum vanishing, and

$$
F_j\mid D^{[P]}F_j\,\widetilde H_j(h)^P
\qquad(j=n,n+1).
$$

It gives a detecting primitive period at most $7m+23$ and bounds the
degrees of the two iterate polynomials by $d^{23}(PM)^7$.
These are not bounds on every intermediate expression or an optimized
running-time estimate.

## 1. Normalization, Frobenius, and the periodic algebra: PASS

The imported normal space is

$$
V_d=k\oplus\bigoplus_{r\ge1,\ d\nmid r}kx^r.
$$

The degree argument for $k[x]=B_f\oplus V_d$ is independent of the
congruence class of $d$. Eliminating exponents divisible by $d$ does
not increase degree. A nonconstant coboundary has positive leading degree
divisible by $d$, so the normal representative is unique. For zero input
one may take $Q=v=0$, and no logarithm of degree zero is needed.

The full cyclic algebra has dimension $d^n$ and the digit monomials
with exponents in $[0,d-1]$ as a basis. Total-degree-lowering reduction
proves spanning even at wraparound; dimension proves independence.
No reducedness hypothesis enters this input or coefficient extraction.
Telescoping gives $H_n(\Delta Q)=0$ in this same full algebra.

Since $\gcd(d,P)=1$, every normal positive exponent remains normal
after multiplication by $P$. In characteristic $p$, the identity
$H_n(v)^P=H_n(v^P)$ is valid. Thus subtracting a coboundary preserves
the two Hasse divisibilities exactly, rather than only their ordinary
values at periodic points.

## 2. Multiplicity-safe Hasse implication: PASS

For a nonzero polynomial $G$ and a polynomial $H$ vanishing at every
ordinary root of $G$, the claimed implication

$$
G\mid D^{[E]}G\,H^E \qquad(E\ge1)
$$

is valid. At a root of multiplicity $e$, the Hasse product rule gives
order at least $\max(e-E,0)$ for the derivative, and $H^E$ supplies
order at least $E$. This covers $e<E$, vanishing Hasse coefficients,
and a derivative that is identically zero. It does not require a bound
on $e$ or division by a factorial.

For a root of $F_n$ with primitive period $r\mid n$, the complete
return sum is $(n/r)S_h(O)$. Vanishing of every ordinary primitive sum
therefore implies the Hasse certificate at every level. The proof never
uses a converse of this implication at one level.

## 3. Exact marked-background formula: PASS

The parameter range gives $3\le P<d$ and $d\ge4$. Expanding
$(x+z)(x^P+z^P)^A+c$ gives no Taylor terms of degrees
$2,\ldots,P-1$, linear coefficient $x^{d-1}$, and coefficient
$\alpha x^{d-P}$ at degree $P$.

The absence of intermediate orders is preserved by composition. The
order-$P$ coefficient of a composite has exactly the two authored terms:
the outer first derivative times the inner order-$P$ coefficient, and
the outer order-$P$ coefficient times the $P$th power of the inner
linear coefficient. Higher orders cannot contribute to order $P$.

Consequently, with mark $j$, the exact background exponents are
$P(d-1)$ before $j$, $d-P$ at $j$, and $d-1$ after $j$.
Their sum over all marks, multiplied by $\alpha$, represents
$D^{[P]}F_n$. The term $-x$ contributes nothing because $P>1$.
No factor of $d$ has been lost: $d=1$ as a scalar in the stated field.

This is a polynomial identity for arbitrary $c$, not a pure-power
identity after setting $c=0$. All subsequent reduction of its high
background exponents is explicitly retained.

## 4. Target digits and weighted paths: PASS

For a normal leading degree $D\le M$, put $L=m+2$ and choose
$s\ge4L+4$, $n\ge s+3L+4$. The target has digit $d-P+1$
at zero, digit $d-1$ at sites $1,\ldots,s-1$, the padded digits
of $PD-1$ at sites $s,\ldots,s+m$, and zero afterwards.

All digits are legal because $P\ge3$ and $PD\le PM<d^{m+1}$.
The first digit at $s$ is at most $d-2$, since $d\nmid PD$.
The stated integer digit value $PDd^s-P+1$ is correct, but is not
used as a claim that the corresponding basis element is the same pure
power in the univariate quotient for $c\ne0$.

The local quotient, retained digit, carry, and weight are precisely the
binomial expansion of $X_a^d=X_{a+1}-c$. Defining
$\kappa_a=q_a-t_{a+1}\ge0$ gives the exact integer identity

$$
e_a=b_a+t_a+Pr\mathbf1_{a=i}-dt_{a+1}-d\kappa_a.
$$

Carry bounds and the later weighted sum are integer arguments before
reduction modulo $p$. Zero binomial weights and every positive power
of $c$ are retained; the reasoning does not assume cancellation is absent.

## 5. Adaptive cuts and overflowing branches: PASS

The cut is a nonsource long-block site whose forward cyclic distance
from the source is at least $L$. Before reaching the source, the incoming
carry is at most $P-1$, because all backgrounds are at most $P(d-1)$.
At the source and after $h\ge1$ steps, the exact upper bound is

$$
t\le P+\frac{Pr-1}{d^h}.
$$

Since $d^{L-1}=d^{m+1}>PM-1$, the carry has dropped to at most
$P$ after $L-1$ steps. Thus the incoming carry at the cut is at
most $P$, and the incoming carry at its predecessor is also at most
$P$. The predecessor is not the source, because $L\ge2$.

The cut initially retains digit $d-P$ for a prefix or mark, and
$d-1$ for a suffix. In the suffix case its predecessor is a suffix
or the mark, so that predecessor's outgoing carry is at most one.
This establishes the stated maximum final cut exponent $d$ in all
cases, including a wrapped source.

If the exponent is below $d$, the first circuit is already a digit
monomial. If it equals $d$, reducing the cut leaves digit zero and
sends at most one unit to the next site. Such a unit can continue only
through a retained digit $d-1$. It either stops, or makes one further
circuit and raises the cut's zero digit to one. It cannot cause another
overflow at the cut. Every resulting branch has cut digit at most one,
whereas the target requires $d-1\ge3$. Thus no overflow branch can
contribute to the target, regardless of its weight.

For every contributing branch, adding the final carry to the retained
cut digit does not change its first quotient. The closed-circuit weight
therefore equals the actual one-circuit expansion weight. This verifies
the cut rather than presuming a cyclic recurrence is already an exact
normal-form algorithm.

## 6. Excess-carry localization and source-free terms: PASS

The baseline $\ell_a=P-1$ for $a\le j$ and $\ell_a=0$ for
$a>j$ satisfies the stated background identity at every $a<n-1$.
With $u_a=t_a-\ell_a$, a nonsource transition obeys

$$
du_{a+1}=d-1+u_a-e_a-d\kappa_a.
$$

If $u_a\le0$, the right side is at most $d-1$, so integrality
forces $u_{a+1}\le0$. This implication does not need a continuing
upper bound on the carries. A zero target digit is impossible under
nonpositive excess: then $0\le t_a\le\ell_a\le P-1$, while
direct reduction of each background requires $t_a=\ell_a+1$.

At any nonsource long-block site with incoming carry in $[0,P]$,
digit $d-1$ forces $t_a=\ell_a$. This statement concerns a digit
exponent, not the value of the scalar $d-1$ in the field.

Writing $b=s+m+1=s+L-1$, the two exclusion cases are complete:

- If $i\le s-L-1$, the cut $a=i+L$ is in $[1,s-1]$ and is
  exactly $L$ forward steps from the source. Its excess is zero,
  and there is no source in $[a,b]$.
- If $i\ge b+1$, the cut $a=L$ has forward distance
  $n-i+L\ge L+1$ from the source, and again $[a,b]$ has no source.

In each case nonpositive excess reaches the zero target site $b$,
a contradiction. The propagation interval does not cross $n-1$,
where the baseline identity was not claimed. Therefore the coefficient
of every monomial with a source outside $I_{n,s}=[s-L,b]$ is zero.
The same cut and propagation argument gives zero target coefficient
for every source-free marked background. Constants in $H_n(v^P)$
therefore contribute zero, independently of the scalar $n$.

There is no need to identify branch sets arising from different adaptive
cuts. The argument proves zero coefficient separately for each excluded
source monomial; those terms may then be omitted before adopting one
common expansion for all remaining sources.

## 7. The common cut and all-mark insertion bijection: PASS

For $i\in I_{n,s}$, the exact bound is
$n-i\ge n-b\ge2L+5$. In the fixed order $0,\ldots,n-1$,
site zero is not a source and initially retains digit $d-P$.
The last site is a suffix or the mark, with sufficiently decayed
incoming carry, so its outgoing carry is at most one. Thus there is
no overflow at zero. The target forces final carry one, giving the
closed convention $t_0=t_n=1$.

At site zero this convention has the same quotient and binomial weight
as the literal expansion that initially has no incoming carry. After
site zero and before the source, every carry is at most $P-1$.
Hence the common path expansion is justified for all retained terms.

Insert a new site at $a=2L$ and replace $(n,s)$ by $(n+1,s+1)$.
The entire source interval lies above $a+1$ and is relabeled exactly
to the new interval. The target inserts one digit $d-1$ and retains
all other digits, including the special digit at zero.

For every old mark, the inserted site is unmarked. Its incoming and
outgoing baseline is $P-1$ if the mark is ahead and zero if the mark
is behind. In the first case the quotient is $P-1$; in the second
it is zero. Taking the outgoing carry equal to this quotient has weight
one. All old backgrounds, transitions, source coefficients, and final
carry are unchanged.

Conversely, in any retained longer path whose mark is not the inserted
site, that site and its successor are nonsources with target digit
$d-1$. Their incoming carries equal their low baselines. Those baselines
are equal precisely because the mark is not the inserted site. The
inserted transition has weight one and can be deleted. This explicitly
includes a mark immediately before or immediately after the insertion.

The operations are inverse on the complete retained source/mark/path
sets. Excluded sources and source-free terms already have coefficient
zero at both levels. Therefore the coefficient difference consists
exactly of paths with the newly inserted mark, with no lost source or
unpaired old mark.

## 8. The new mark and every high-$c$ branch: PASS

Let $N=n+1$, $S=s+1$, with the mark at $a=2L$. Every possible
source is after $a+1$. At the mark, incoming carry $P-1$ combines
with background $d-P$ to give exponent $d-1$ and quotient zero.
Its outgoing carry is zero, with weight one.

The subsequent nonsource suffix sites necessarily retain $d-1$ with
carry zero. Since the target digit at $S$ is smaller, the source
must satisfy $i\le S$. Summing the exact carry identity with weights
$d^{u-i}$ over $i\le u<N$, using initial carry zero and final
carry one, gives

$$
\sum_{u=i}^{N-1}e_ud^{u-i}
=Pr-1-\sum_{u=i}^{N-1}\kappa_ud^{u-i+1}.
$$

The target makes the left side $PDd^{S-i}-1$. Hence

$$
Pr=PDd^{S-i}+\sum_{u=i}^{N-1}\kappa_ud^{u-i+1}.
$$

All terms in the last sum are nonnegative integers. Together with
$r\le D$ and $i\le S$, this forces $i=S$, $r=D$, and
$\kappa_u=0$ at every suffix site. The earlier prefix sites have
their forced baseline transitions, including the transition at zero;
the mark and remaining presource suffix sites also have weight one.
Thus no earlier positive power of $c$ remains unexamined.

The unique suffix path exists. More explicitly, after the source its
carry at $S+h$, for $h\ge1$, is

$$
1+\left\lfloor\frac{PD-1}{d^h}\right\rfloor.
$$

This produces exactly the padded base-$d$ digits of $PD-1$ and then
the final string of zero digits with carry one. Every outgoing carry
equals its quotient, so every binomial weight is one, even in small
characteristic. The resulting coefficient is exactly
$\alpha a_D^P\ne0$.

Consequently the stated identity
$C(n+1,s+1)-C(n,s)=\alpha a_D^P$ holds for every allowed $c$.
The proof has not discarded terms containing $c$, assumed their
cancellation, or replaced a digit target by a pure-power monomial.

## 9. Constants, zero input, wild periods, and the finite bound: PASS

The selected values $L=m+2$, $s=4L+4$, and $n=s+3L+4$
give exactly $n=7m+22$. If the two Hasse certificates hold, normalization
preserves them, and both target coefficients are zero. The nonzero
coefficient difference excludes every positive-degree normal part.

For a constant normal part $a_0$, its return sum raised to $P$ is
$(ja_0)^P=ja_0^P$, since the integer scalar $j$ lies in the prime
field. Choose one of $n,n+1$ not divisible by $p$. Each marked
univariate term has degree $d^j-P$ and leading coefficient one:
its exponent sum is

$$
P(d^t-1)+(d-P)d^t+(d^j-d^{t+1})=d^j-P
$$

for mark $t$. Therefore $D^{[P]}F_j$ has leading coefficient
$j\alpha\ne0$ and degree strictly below $\deg F_j$. The constant
divisibility forces $a_0=0$. The case $h=0$ is already included.

Coboundaries telescope, and ordinary-root vanishing gives the necessary
Hasse certificate. These implications establish all three finite
conditions as equivalent and then prove the full ordinary-cycle theorem.
If a root test fails at primitive period $r\mid j$, the nonzero
quantity $(j/r)S_h(O)$ implies $S_h(O)\ne0$ without division in
$k$. No wild primitive period is excluded. The tests concern complete
return sums at every ordinary root, not only exact periods $n,n+1$.

The degree calculation
$d^{n+1}=d^{7m+23}\le d^{23}(PM)^7$ follows from $d^m\le PM$.
For the smallest cap $M=1$, $P<d$ gives $m=0$, $L=2$, $s=12$,
$n=22$. All cut distances, source intervals, and insertion inequalities
used above still hold. No positive-degree lower bound on $h$ is silently
imposed by this boundary check.

## 10. Report, source applicability, and remaining boundaries

The report's separate $c=0$ proof is valid. For $p\nmid n$, the
binomial congruence $(d^n-1)/P\equiv nA\pmod p$ makes
$R=(d^n-1)/P$ prime to $p$. Hence
$F_n=x(x^R-1)^P$, with ordinary multiplicities one and $P$.
Ordinary-root vanishing implies divisibility after taking the $P$th
power, and the applicable R4 leading-digit detector excludes a positive
normal part at sufficiently large prime-to-$p$ levels. A constant is
detected at zero. This proves the monomial subfamily only; the full
all-$c$ theorem is supplied by the different Hasse-carry proof above.

The report's multiplicity-growth route is also correctly conditional.
An unbounded sequence with $n-2\log_dE_n\to+\infty$ would suffice
by applying the normal digit detector to $v^{E_n}$, but no such
all-$c$ estimate is established or imported. The displayed derivative
power identity is valid under the report's retained excluded-congruence
parameters and does not supply a bound on root multiplicities.
Nothing in the completed proof relies on that conditional route.

The R4 imported statements are valid in this congruence class even
though its ordinary-Jacobian theorem excluded the class. Their roles
are separated correctly. Hasse differentiation itself, polynomial
normal forms, the digit basis, and the earlier adjacent-level carry
idea are not newly owned mechanisms. No unseen external theorem is
being used outside its characteristic or multiplicity hypotheses.

The report expressly limits its discovery searches and does not claim
an exhaustive priority check. This review assesses mathematical source
applicability, not independent verification of every search receipt or
worldwide novelty. No additional citation is required to fill a missing
mathematical premise: the new proof is self-contained. The coordinator
retains the separate source-priority and integration decisions.

The result remains inside the same PC424-L question. The R4 and R5
ranges together cover all $d\ge2$ in odd characteristic, but no
change to older frozen statements, an additional contract count, or
conclusion in characteristic two is made by this review.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unchanged.

## Verification receipt

Verification consisted of complete actual-file reading, checking the
applicable R4 proof passages, independent symbolic reasoning through
every marked-path case, and read-only hashes. There were no mathematical
executions, external model/API calls, new agents, Git operations, old-file
or shared-state edits, manuscript edits, or PDF builds. The only new
workspace write by E8 is this allocated review file.
