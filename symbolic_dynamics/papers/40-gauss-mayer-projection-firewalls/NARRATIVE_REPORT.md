# Paper 40 narrative report — SD-C42

## Central story

The two-digit/even-iterate Gauss--Mayer system already has substantial
positive structure: an intrinsic ordered-pair ledger, exact positive
$\mathrm{SL}_2(\mathbb Z)$ monodromies, the derivative clock, and a
same-space nuclear Fredholm determinant. Its unmarked specialization is tied
to the modular Selberg zeta function by Mayer's theorem. None of these facts
alone identifies rational primes.

Paper 40 asks one deliberately narrow question. Can any of exactly three
source-canonical scalar projections---trace, trace/order discriminant, or
geodesic norm---convert the full intrinsic pair ledger into the
rational-prime reciprocal Euler ledger while preserving label support,
one-to-one multiplicity, temporal powers, clock, digit marker, orbit weight,
sign, orientation, phase, and operator ownership?

The answer is an exact contract-relative STOP. The intrinsic pair ledger and
its Fredholm determinant retain positive modular credit, but none of the
three projections satisfies the complete rational-prime conjunction. This is
an audit closure, not a new Gauss--Mayer mechanism. Paper 1 already owns the
qualitative mismatch, the pre-existing next-test request, and a much larger
finite collision census. The present work contributes a typed theorem,
all-order identities, explicit contract falsifiers, an intrinsic pair
Fredholm regrouping, and an executable projection-by-projection coverage
audit. It claims no collision priority or witness-size optimality.

## Claims--evidence matrix

| Claim | Evidence | Status | Manuscript location |
|---|---|---|---|
| C1. The pair return, marker, branch, clock, and determinant form one typed construction. | $X$, $X_2$, $\iota$, $\rho\iota=\iota\sigma^2$; raw-index reversal; $K_s=\mathcal L_s^2$; local/formal Fredholm regrouping. | Immutable/proved | Sections 3 and 5; Appendix A |
| C2. None of exactly three scalar projections supplies the complete rational-prime ledger. | Order-discriminant factorization, nonsquare norm, clock inequality, Cayley--Hamilton recurrence, three collision classes, composite species, amplitude mismatch. | Immutable/proved | Section 4; Appendix A |
| C3. Scalar prime filtering does not inherit Fredholm ownership from the untwisted $K_s$. | Typed object--marker--operator ledger and absence of a declared reducing projector/selected trace owner. | Immutable/contract-relative proof | Section 5 |
| C4. The conclusion is scoped rather than universal. | Three primitivity types, twists and changed-operator boundaries, and five explicit out-of-contract countermodels. | Immutable/proved scope | Sections 2, 5, and 7; Appendix B |
| C5. The bounded implementation checks exact obligations but does not define the theorem. | FINAL block: main 210/210, independent 208/208, integrity 83/83, ledger 102/102, all declared packet/Route mutations rejected, cold-copy second-run delta zero. | Integrator-verified | Section 6 |

## Typed source object

Let $X=\mathbb N^{\mathbb N}$ carry the one-digit shift $\sigma$. Let
$X_2=(\mathbb N^2)^{\mathbb N}$ carry the one-pair shift $\rho$, and group
adjacent digits by

$$
\iota(a_1,a_2,a_3,a_4,\ldots)
=((a_1,a_2),(a_3,a_4),\ldots).
$$

Then

$$
\rho\circ\iota=\iota\circ\sigma^2.
$$

This equality is typed: $\sigma^2$ acts on digit space and $\rho$ acts on
pair space. A least-period-$n$ digit orbit produces $\gcd(n,2)$ cycles under
$\sigma^2$, each of length $n/\gcd(n,2)$. Odd periods remain one cycle;
even periods split into two. Thus

$$
N_{D^2}(k)=2N_D(2k)+\mathbf1_{k\text{ odd}}N_D(k).
$$

For a pair word with flattened digits $(a_1,\ldots,a_{2k})$, define

$$
A(a)=\begin{pmatrix}a&1\\1&0\end{pmatrix},\qquad
M(w)=A(a_1)\cdots A(a_{2k}).
$$

Every pair product lies in $\mathrm{SL}_2(\mathbb Z)$ and has trace
$t\ge3$. Write

$$
\Delta(w)=\Delta_{\mathbb Z[M]}(w)=t(w)^2-4,
\quad
\lambda(w)=\frac{t(w)+\sqrt{\Delta(w)}}2,
\quad
T(w)=2\log\lambda(w).
$$

Here $\Delta_{\mathbb Z[M]}$ is the order/characteristic-polynomial
discriminant, not a field fundamental discriminant or a larger multiplier-
ring discriminant.

The types `RhoPrimitivePair`, `SigmaPrimitiveDigit`, and
`GeodesicPrimitiveClass` remain distinct. The $u=1$
Selberg-zeta/Fredholm-determinant equality is a functional identity, not an
objectwise primitive-orbit dictionary.

## Same-object operator and pair ledger

For $\phi_a(z)=(a+z)^{-1}$, the digit matrices
$B(a)=\left(\begin{smallmatrix}0&1\\1&a\end{smallmatrix}\right)$ and
$J=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ satisfy
$A(a)=JB(a)J$. Raw nested indices in $\mathcal L_s^{2k}$ occur in the reverse
of stored composition order. Global reversal is a dummy-index bijection that
preserves cyclic pair classes; it does not quotient a word with its reverse.

In Mayer's nuclear domain and coefficientwise/formally in $u^2$ (or
analytically for sufficiently small $|u|$), the local Fredholm logarithm
regroups as

$$
-\log\det(I-u^2K_s)
=\sum_{n\ge1}\frac{u^{2n}}n\operatorname{Tr}(K_s^n)
=\sum_{[v]\ \rho\text{-primitive}}\sum_{r\ge1}
  \frac{u^{2k(v)r}d_v^{rs}}{r(1-d_v^r)},
$$

where $K_s=\mathcal L_s^2$ and
$d_v=|\Phi_v'(x_v)|=\lambda(v)^{-2}$ at the positive real fixed point.
The complex weight itself is defined through Mayer's fixed holomorphic
logarithm branch. Cyclic multiplicity cancels the word-length denominator,
so this derivation owns the intrinsic pair ledger without importing a
pair-to-geodesic bijection. The source stability denominator and Selberg
tower remain visible.

## Exact projection firewalls

For every source word,

$$
\Delta=(t-2)(t+2),
$$

so the order discriminant is prime exactly at $(t,\Delta)=(3,5)$. The strict
interval

$$
(t-1)^2<\Delta<t^2
$$

shows that $\lambda^2$ is irrational. It also yields
$\lambda^2>t$, hence the derivative clock is not $\log t$. The realized
one-pair family $w_t=((1,t-2))$ for every $t\ge3$, together with the
large-$t$ limit, rules out one common constant rescaling. Cayley--Hamilton
gives

$$
q_r=tq_{r-1}-q_{r-2},\qquad q_0=2,\quad q_1=t,
$$

so $q_2=t^2-2\ne t^2$; similarly
$\Delta(M^2)=t^2\Delta(M)\ne\Delta(M)^2$.

Three exact collision classes make the multiplicity failure explicit:

| Class | Pair words | Common trace | Role |
|---|---|---:|---|
| reversal-phase | `((1,2))`, `((2,1))` | 4 | distinct pair factors because reversal is metadata only |
| one-pair non-reversal | `((1,4))`, `((2,2))` | 6 | duplicate species without a reversal relation |
| cross-pair-length non-reversal | `((2,4))`, `((1,1),(1,2))` | 10 | duplicate species at pair lengths one and two |

All three scalar projections collide on each row because $P_\Delta$ and
$P_N$ are functions of $t$. The full ledger also contains the composite
trace species `((1,2))`.

The exact reciprocal-determinant comparison exposes a further amplitude
failure. A source repetition contributes

$$
\frac{u^{2kr}d_w^{rs}}{r(1-d_w^r)},
$$

whereas a hypothetical rational-prime factor contributes
$u^{2kr}p^{-rs}/r$. Even the formal assignment $p=d_w^{-1}=\lambda^2$
leaves the nonunit stability factor $(1-d_w^r)^{-1}$.

## Analytic boundary

On the disk algebra
$A_\infty(D)$, $D=\{z:|z-1|<3/2\}$, Mayer's Gauss operator is nuclear of
order zero for $\operatorname{Re}s>1/2$. Proposition 3 gives the holomorphic
identity on that same half-plane:

$$
Z_{\mathrm{PSL}_2(\mathbb Z)}(s)
=\det(I-\mathcal L_s^2)
=\det(I-\mathcal L_s)\det(I+\mathcal L_s).
$$

The Selberg Euler product is initially absolutely convergent for
$\operatorname{Re}s>1$, while Corollary 3 supplies the qualified meromorphic
continuation to $\mathbb C$. The free variable $u$ counts original Gauss
digits and does not define a new two-variable Selberg mechanism. The local
Fredholm logarithm/product is not continued across determinant zeros, and no
arbitrary-$u$ Selberg interpretation is asserted.

## Priority and novelty boundary

The independent replacement literature audit scores the scoped closure 4/10
and recommends `PROCEED_WITH_CAUTION_AS_SCOPED_CLOSURE_ONLY`. Foundational
work owns the Gauss transfer operator, modular coding, and Selberg-zeta
identity. Prior work also owns two-variable Gauss/Farey determinants,
geodesic trace and discriminant arithmetic, length multiplicities, primitive
geodesic analyses, and strict or twisted transfer families. Paper 40 therefore
foregrounds only its contract-specific synthesis and closure, and concedes
mechanism-level prior art immediately.

The selection audit is independent of P39. P39 supplies terminal-clean
provenance and existence only; it neither ranks nor authorizes SD-C42. The
correction chronology is retrospective: v1 and in-flight corrective outputs
were known, the exact final M1--M20 input set preceded the canonical
replacement run, and the M21--M25 proof/source/literature renderings are
post-run.

## Route disposition

The retained positive codes are

```text
GO_MODULAR_PRIMITIVE_LEDGER
GO_SAME_OBJECT_MAYER_DETERMINANT
```

and the rational-prime branch terminates with

```text
STOP_CANONICAL_INTEGER_PROJECTION
STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION
STOP_OPERATOR_VISIBLE_SELECTOR_NOT_OWNED
ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

The clock/repetition STOP is intentionally narrow. $P_t$ and $P_\Delta$ are
integer-valued but fail exact clock and temporal powers; $P_N$ passes clock
and powers but is not integer-valued. The GO ledger code is pair-shift typed
and carries no digit-primitive, geodesic-primitive, or rational-prime credit.

## Evidence-integration boundary

The designated integrator released one `FINAL / POST-OUTPUT CLEAN` block.
The main and independent evaluators passed 210/210 and 208/208 checks,
respectively; the canonical scientific projection has SHA-256
`340aff6f08e7cf9360d57d34ff9c66e99f9322343b3069fe37e5acc2f55aa7c5`.
The integrity audit passed 83/83 checks (SHA-256
`61ff8805dd5bcc44dec3ea8a960786ccb72f211bf7c8d30d013eb749a536110c`),
and the 102/102-entry results ledger has SHA-256
`ddcda6a450c662be8432f14510569a4097f6f3909ea17a68f499d21e47edeb31`.
The exact package contains 54 result files, two evaluation files, and one
experiment report. Both evaluators rejected all 164 packet mutations
(164 x 2); Route testing rejected all 422 executions (24 explicit plus 398
exhaustive recursive mutations over 409 distinct payloads), and the strict
Route schema passed 18/18 checks. A hidden cold-copy second full run changed
zero paths.

These are bounded checker and reproducibility outcomes. They may check exact
fixtures, finite censuses, mutations, and schema integrity; they cannot by
themselves prove nuclearity, meromorphic continuation, the all-orders
algebra, novelty, or a universal no-go theorem.
