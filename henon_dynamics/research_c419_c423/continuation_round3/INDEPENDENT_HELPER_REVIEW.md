# Non-author review of the two round-three helper packages

2026-09-07 UTC. Reviewer: current-team `scout_nonlinear_return`.
Only this review document was written for this task.

## 1. Independence, exact scope and verdict

I did not author either new `rational_trace` or `spectral_recursion`
proof package or the new spectral program. I **was an author of the
earlier IR1 work** and already knew its accepted scope and the
coordinator's intended companion-only disposition. This review is
therefore non-author for these two helpers, but neither blind nor
independent of IR1's prior development. IR1 is an accepted dependency,
not a theorem re-reviewed or rerun here.

I read all six specified local documents in full: each lane's frozen
contract, proof package and source audit. I also read all of
`spectral_recursion/exact_denominators.py` and the imported
`continuation_round2/solenoid_boundary/semigroup_probe.py`, checking in
particular the pure successor/graph/component functions and the guarded
old entry point. I compared the existing author-run stdout with the
new proof package and checked the two executable-source SHA-256 values
read-only. Primary papers listed inside the source audits were **not**
independently re-read for this bounded helper review; no new source
priority certificate is claimed.

No mathematical program was executed or imported; no finite-field
graph, moment sequence, matrix characteristic polynomial, BM fit,
denominator factorization, rational orbit census or old IR1 check was
recomputed. Even the optional AST/in-memory compile was not needed.
The polynomial manipulations below are direct written reasoning, not a
new computational run. The review uses the current team and the
proof-writer/research-review rigor checks; the task's current-team
instruction supersedes the old skill's external-model defaults.
No paid/external model, human review or GPU is implied.

| Claim | Review status | Permitted conclusion |
|---|---|---|
| RT3 exact denominator $\operatorname{den}(k)=q^2$ | `PROVABLE AS STATED` | Correct elementary lemma for integer $a$ and rational periodic points |
| Integral-level rational locus equals IR1 integer locus | `PROVABLE AS STATED`, conditional on accepted IR1 for its explicit classification | Same points and native periods; short corollary, not a new classification contract |
| Every denominator $q\ge2$ occurs in the displayed $a=0$ family | `PROVABLE AS STATED` | Genuine least-two cycles with exact level denominator $q^2$ |
| AS1-R3 finite-state observable and infinite-moment certificate | `STATIC LOGIC CHECK SATISFIED` | A successful exact run of the reviewed program certifies each fixed finite layer, including every later moment |
| Six reported minimal denominators and multiplicity discussion | `AUTHOR-RECEIPT TRANSCRIPTION MATCHES` | Existing exact output is faithfully recorded; this is not independent numerical reproduction |
| All-rational RT3 classification / full AS1 secondary-circle continuation | `NOT CURRENTLY JUSTIFIED` | Both original contracts remain unclosed and unadmitted |

No blocking mathematical or transcription error was found in the
reviewed versions. No coordinator correction is requested before
retaining these limited helper statements. The result adds **zero
admissions** and does not change the original three admitted contracts.

## 2. RT3: independent check of the denominator lemma

### Claim, assumptions and dependency map

The map is
$$T_a(x,y,z)=(y,z,yz+a-x),\qquad a\in\mathbb Z,$$
and the whole ordinary rational periodic orbit is in scope, including
zero coordinates, fixed points and points on singular levels. Let
$q$ be the least common multiple of all reduced coordinate denominators
in this finite orbit. Its symmetric invariant is
$$K_a=x^2+y^2+z^2-xyz-a(x+y+z).$$
The claim is that the reduced positive denominator of its constant
value $k$ is $q^2$, with denominator one for $k=0$.

The proof uses only: the cyclic scalar recurrence, an attained maximum
at each prime, integer $a$, the ultrametric inequality and the invariant
identity. It uses no integral finite-core theorem, surface smoothness,
source height theorem or period lower bound. Preservation of $K_a$
also follows directly: as a polynomial in the replaced coordinate
$x$, its quadratic part is $x^2-(yz+a)x$, invariant under
$x\mapsto yz+a-x$; the remaining cyclic rotation preserves the
symmetric expression.

### Direct proof and edge cases

1. Fix a prime $p$, and let $h=\max_i|x_i|_p$ for the finite scalar
   cycle. If $h\le1$, every summand of $K_a$ is $p$-integral, hence
   $k$ has no denominator factor $p$.
2. If $h>1$, choose $|x_j|_p=h$. The two scalar recurrence identities
   $$x_{j-1}x_j=x_{j-2}+x_{j+1}-a,\qquad
     x_jx_{j+1}=x_{j-1}+x_{j+2}-a$$
   have right sides of norm at most $h$. Dividing by the nonzero
   $x_j$ shows that **both** neighboring norms are at most one.
3. Evaluate $K_a$ on that three-coordinate window. The middle square
   has norm $h^2$. The two other squares have norm at most one; the
   triple product and each parameter-linear term have norm at most
   $h<h^2$. Hence there is exactly one largest-norm summand, and
   cancellation at that order is impossible: $|k|_p=h^2$.
4. If $p^e\Vert q$, then $h=p^e$ when $e>0$, so
   $v_p(k)=-2e$. For $e=0$ there is no negative valuation. Combining
   these exact statements over all primes gives
   $\operatorname{den}(k)=q^2$.

The maximum chosen in step 2 is necessarily nonzero; other coordinates
may be zero without affecting the estimate. Small periods merely
identify some indices, and do not invalidate either recurrence
identity. At $k=0$, step 3 would be impossible for any $h>1$, so
$q=1$ as claimed. This verifies the precise lemma in
[RT3's proof package](rational_trace/PROOF_PACKAGE.md), not a generic
or nonsingular weakening.

Integer $a$ is essential and is already correctly stated. As an
outside-hypothesis check, $a=3/4$ has the fixed point
$(1/2,1/2,1/2)$, with $q=2$ but $k=-1/2$. Its level denominator is
two, not four. The package does not claim the lemma for this case.

### Corollary and unrestricted-denominator family

At integral $a,k$, the lemma forces $q=1$. Conversely, an ordinary
integral periodic point is of course a rational one and has integral
invariant. Thus the two periodic loci on that level are literally
equal under the identity inclusion, not just conjugate or in bijection
after quotienting. The same displayed map and same one-step clock
preserve every native least period. Importing the accepted IR1
classification therefore gives exactly the stated corollary. This
review does not reopen IR1's explicit integer atlas or counts.

For $q\ge2$, let $u=(q+1)/q$ and $v=q+1$. Directly
$uv=u+v$, and hence
$$T_0(u,v,u)=(v,u,v),\qquad T_0(v,u,v)=(u,v,u).$$
The two points are distinct since $u\ne v$; they are ordinary affine
points, with exact least period two and exact common denominator $q$.
Using $uv=u+v$ in the invariant gives
$$K_0(u,v,u)=uv(uv-3)
 =\frac{(q+1)^2(q^2-q+1)}{q^2}.$$
Both numerator factors are coprime to $q$, so the displayed denominator
is reduced. The arbitrary-$q$ claim is correct and excludes any
parameter-uniform denominator bound even at the fixed parameter $a=0$.

The proof package also correctly refuses the converse “square level
denominator implies a periodic point.” A prescribed level with
denominator $q^2$ determines the possible coordinate denominator, but
does not classify all coordinates or periods on it. The real
maximum-difference condition gives centers in $[-3,1]$; its intersection
with $q^{-1}\mathbb Z$ contains $4q+1$ values, not the five integral
centers. Thus the stated remaining all-denominator gap is genuine.

## 3. AS1-R3: static observable and certificate review

### Initial vector, transition direction and cyclic words

The imported constructor starts state index zero at
$(I,\mathrm{sentinel})=(1,0,0,1,2)$. Its two update formulas are exactly
left multiplication by
$$A=\begin{pmatrix}3&1\\1&3\end{pmatrix},\qquad
  B=\begin{pmatrix}3&2\\2&4\end{pmatrix}$$
modulo $2^k$. The last-letter flag suppresses $A$ only when the
previous letter was $A$. Merging states does not merge path counts:
the adjacency rows retain the outgoing edges and the transfer action
sums them with multiplicity.

At [program lines 83--88](spectral_recursion/exact_denominators.py),
the terminal vector is $f(M)=1_{\operatorname{tr}M\equiv1}$.
Starting from that column and repeatedly summing successor entries
computes $S^nf$; reading coordinate zero is exactly $eS^nf$.
There is no transposition, accidental terminal/initial reversal,
primitive-cycle division or time-reversal quotient. The last-letter
sentinel exists only at time zero, and its trace two fails the terminal
test at every $k\ge1$.

The lack of an explicit stored first letter is not a defect for this
observable. Modulo two, $A^2=0$. For a word of length at least two
whose two endpoints are $A$, cyclic invariance of the trace moves
the endpoint factors together; the trace is then zero modulo two.
Such a word cannot pass any trace-one test modulo $2^k$. The single
letter $A$ also fails because its trace is six. Thus an accepted
internally admissible path is exactly a cyclically active based word
with the prescribed trace congruence.

Both matrices have determinant eight, so
$$\det(I-M)=1-\operatorname{tr}M+8^n.$$
For $3n\ge k$, the two stated congruences coincide. For the six
reported layers the only positive-length exceptional case is $n=1$
at $k=4,5,6$; the sole active word is $B$, with trace seven and
$\det(I-B)=2$, and it fails both tests. This verifies the initial
correction claim exactly in the claimed range, not at arbitrary $k$.
As a hand check of the endpoint convention, the three length-two
words $AB,BA,BB$ have traces $25,25,33$, giving the reported
length-two values $3,3,3,1,1,0$ across $k=1,\ldots,6$.

### BM is a proposal; Cayley--Hamilton makes it a certificate

Let $N$ be the finite graph dimension. The code constructs the exact
integer sequence $c_n=eS^nf$ for $0\le n\le3N$. The BM routine uses
`Fraction`, not modular or floating approximations, and proposes an
order $L$ and coefficients $q_0=1,\ldots,q_L$ from the first $2N+1$
values. Its update signs and discrepancy convention agree with
$\sum_{j=0}^Lq_jc_{n-j}=0$. More importantly, the certificate does
not depend on trusting BM's claimed minimality: the code rejects
$L>N$ or bad normalization and checks every exact residual from
$n=L$ onward, requiring at least $N$ consecutive zero residuals.

For an independently transparent propagation argument, put
$$v=\sum_{j=0}^Lq_jS^{L-j}f,\qquad r_m=eS^mv.$$
The checked residual at index $L+m$ is exactly $r_m$.
If $\chi_S(X)=X^N+\sum_{j<N}\alpha_jX^j$, Cayley--Hamilton gives
$$r_{m+N}=-\sum_{j<N}\alpha_jr_{m+j}\quad(m\ge0).$$
The first $N$ zero values therefore imply all $r_m=0$ by induction.
The check starts at $n=L$, so those first $N$ values are indeed
among the checked residuals; this is not a validation block at the
wrong shifted index. The proof works for singular matrices and
transient states as well as invertible recurrent blocks.

Consequently the initial convolution polynomial $P$ used at program
lines 101--102 satisfies $Q(t)C(t)=P(t)$ as an identity of infinite
formal series. Exact gcd reduction in $\mathbb Q[t]$, followed by
$Q(0)=1$ normalization, gives the true reduced scalar denominator.
There is no omitted minimality hypothesis: a coprime representation
of a rational function has its unique minimal denominator up to a
constant. Trailing zero recurrence coefficients can make $L$ exceed
$\deg Q$; a polynomial/transient contribution can require the
recurrence to start later. The observed one-degree difference is
therefore not itself an error.

The SCC routine is the two-pass finish-order/reverse-graph algorithm;
its groups partition the reachable states. The product of all SCC
block characteristic polynomials is the full characteristic
polynomial because the condensation graph is acyclic and a block
triangular ordering exists. Closed-component detection checks every
outgoing target's label. These full-matrix factors are separate from,
and need not survive in, the scalar reduced denominator.

### Existing output versus the written formulas

The existing author-run stdout reports the same $(N,L,\deg Q)$ and
residual counts as the proof package:

| $k$ | $(N,L,\deg Q)$ | zero residuals $3N+1-L$ | normalized denominator transcription |
|---|---|---:|---|
| 1 | $(5,3,2)$ | 13 | $1-t-t^2$ matches |
| 2 | $(9,5,4)$ | 23 | $D$ matches |
| 3 | $(9,5,4)$ | 23 | $D$ matches |
| 4 | $(39,11,10)$ | 107 | $DE$ matches |
| 5 | $(75,19,18)$ | 207 | $DEF$ matches |
| 6 | $(147,43,42)$ | 399 | $DEFR_+R_-$ matches |

Here $D,E,F,R_\pm$ mean precisely the polynomials in the
[spectral proof package](spectral_recursion/PROOF_PACKAGE.md).
I checked the constant signs, the reciprocal orientation of the
degree-twelve factors, and each $t^3,t^5,t^9,t^{11}$ sign in
$R_\pm$. No transcription discrepancy was found. The $k=5$ output
also has the stated squared quartic in each closed block, whereas
the scalar denominator has one copy. Repeated factors across the
three blocks are not incorrectly tripled in the scalar denominator.

The current script digest is
`0e3f71a4b18a1db39617a6dcce37c32295da750df7743fe38b9963db8e48c255`,
and the imported graph source digest is
`96a8ddbde573c95ad70f99e5a0fccab7ed9775e825da0733e74b274804660357`.
Both match the existing author receipt and proof package. This is a
source-integrity and transcription check, not another successful
mathematical run or an independent certificate of SymPy internals.

## 4. Corrections, remaining risks and admission boundary

No correction is required for the two helpers as presently scoped.
The source audits correctly avoid claiming that an ambient
whole-group, non-Archimedean-valued or differently weighted transfer
theorem automatically proves the present single-map/complex-valued
question. This review checks that their limited use is consistent with
the proofs; it does not replace an independent audit of every cited
primary theorem or establish novelty.

The critical boundaries remain unchanged:

- RT3 has a correct square-denominator obstruction and an integral-
  level IR1 corollary, but no complete rational periodic atlas over
  all unbounded denominators. The short inherited two-cycle family
  cannot be counted as a new independent theorem package.
- AS1-R3 has a logically sound exact finite-layer certification
  method and faithfully recorded six-layer output. Certifying all
  moments at one fixed $k$ does **not** certify all $k$. No all-depth
  factor recursion, annular weighted-tower estimate, survival of
  layer poles after summation, or noncancellation after integration
  and exponentiation has been proved here.
- The whole-secondary-circle contract cannot be replaced by the
  already retained two-real-point obstruction, these finitely many
  denominator factors, or a fresh numerical PASS label.

Final recommendation: retain the stated helpers and exact gaps;
**do not admit RT3 or AS1-R3**. There is no requested author revision
to await and thus no local correction recheck is needed in this round.
This review creates no manuscript, formal evaluation, C-number,
target Euler factor, root number or zero-correspondence claim.
