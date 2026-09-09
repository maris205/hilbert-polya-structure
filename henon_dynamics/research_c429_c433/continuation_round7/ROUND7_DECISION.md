# Round 7 — finite interfaces and exact remaining bridges

Coordinator checkpoint, 2026-09-09 18:24 UTC. All four allocated R7
nonauthor mathematical reviews are fully read and closed at their stated
auxiliary scopes, with zero open must-fixes. This is a research decision,
not a completed-paper release or an R7 synchronization receipt.
The actual local baseline is
`9e39585284d854195faebeb5072f43041672fb21`, following the frozen R6
research commit `a9793f56636e3471356408a5304b646fd08a7766`.

**Four contracts remain admitted; zero papers are complete.** PC424-L,
UL4, OM4 and RLG5 keep their previously reviewed scopes. No result below
is admitted as a fifth contract. Five complete papers is a checkpoint,
not the continuous-run stopping rule. No mathematical execution was
allocated or performed in R7 at this checkpoint.

## 1. Actual mathematical decisions

| Artifact and exact scope | Coordinator disposition | Unresolved boundary |
| --- | --- | --- |
| [C2 finite reflection interface](c2_nine_reflection_lifting/REPORT.md), with [E6 review](reviews/e6_nine_reflection_lifting/REVIEW.md) | Accept the complete finite restriction, gcd and polynomial-evaluation statements; zero open must-fixes | Ordinary integral-polynomial interpolation is not a global tame lift |
| [C4 specified candidate](c4_specific_nine_lift/REPORT.md), with [E4 review](reviews/e4_specific_nine_lift/REVIEW.md) | Accept the all-degree two-alternating-shear obstruction; zero open must-fixes | Other conjugator words and the full integer-nine problem remain open |
| [A2 divisor criterion](a2_multiplicative_existence/REPORT.md), with [E5 review](reviews/e5_multiplicative_divisor/REVIEW.md) | Accept the complete criterion, normalization, pure-Frobenius subtype and controls; zero open must-fixes | General norm-one plus cofinite products has not been proved to force the function to be one |
| [X2 native fiber source audit](x2_pointwise_periodic_fibers/REPORT.md) | Accept the elementary controls, first-integral equivalence and bounded source disposition at auxiliary scope | No exact-native-period existence bridge was obtained |
| [A1 smallest balanced atom](a1_balanced_divisor_detection/REPORT.md), with [E8 review](reviews/e8_balanced_divisor_detection/REVIEW.md) | Accept the complete parameter reduction, all-parameter non-torsion and stated residual interface; zero open must-fixes | The exact residual $f=x^2-1$, $a=\pm1$, for all odd primes is unproved |

Root actually read all 245 lines of C2, all 301 lines of E6, all
342 lines of C4, all 143 lines of E4, all 434 lines of A2, all
428 final lines of E5, all 240 lines of X2, all 379 final lines
of A1, and all 296 final lines of E8. E5's final four wording clarifications were read in the full
428-line version, and its actual final hash matches the freeze notice.
A1's stated reduction and the complete E8 review have been checked
by root and accepted; its full all-parameter sublemma remains unproved.
The four final mathematical reviews total 1,168 lines. X2's source
audit and the subsequent integration audit are not additional proof reviews.
The author date labels follow the environment date, while this record
uses the actual UTC clock. Hashes bind bytes, not mathematical truth.

## 2. What the nine-point work proves

Use C2's labels $1,\ldots,9$ on the same R6 integral nine-point set
$C$, with the actual maps $A,I$ and restrictions $a,i$ retained.
For an integral tame conjugate of a triangular reflection preserving
$C$, the restriction belongs to the explicitly listed 27 candidates.
The argument uses normalization of the fixed curve modulo four:
three independent fixed lifts in one mod-two fiber cannot occur.
The bijection $C\to\mathbb F_3^2$ gives exactly three fixed labels.
These restrictions, not just a finite-field permutation count, give
the 27-candidate upper bound.

If an integral tame map $T$ induced a nine-cycle on $C$, the nine
restrictions of $T^jIT^{-j}$ for $0\le j<9$ would be distinct.
Consequently at least six additional candidates beyond the three
known reflections would need genuine lifts. This is a necessary
condition, not the existence of those lifts.

All 27 candidates pass the pair-difference gcd condition. The report
also determines the exact evaluation image of $\mathbb Z[x,y]$ on
$C$, using unimodular three-point interpolation in each mod-two fiber
and integral CRT selectors. Hence all candidates have ordinary
integral-polynomial coordinate interpolants. Neither interpolants
in both directions on $C$ nor correct gcd data give a polynomial
inverse or a unit Jacobian on the entire plane.

The specific desired reflection is

$$\kappa=(5\ 9)(3\ 8)(6\ 7).$$

Its restriction would give

$$\kappa ia=(1\ 2\ 3\ 9\ 7\ 8\ 5\ 6\ 4).$$

C4 proves that no conjugate $M^{-1}\rho_RM$ induces this $\kappa$
when $M=L\circ V_Q\circ H_P$, $P,Q,R\in\mathbb Z[t]$, and $L$
is any integral unimodular affine map. There is no degree, coefficient
or intermediate-set-preservation restriction. The proof already
excludes the necessary first coordinate, before choosing $R$ or
checking the three fixed points.

After legitimate integer normalizations the three exchanged pairs
force

$$P(0)=0,\quad P(-2)=2,\quad P(2)=-2,\quad
P(1)=-4,\quad P(-1)=-2.$$

The remaining integer polynomial $S$ must satisfy

$$S(0)=S(-2),\qquad S(-1)-S(-3)=2,\qquad S(1)-S(-1)=2.$$

Since integer polynomials preserve congruences modulo three, these
three equalities contradict one another modulo three. All sign
branches, affine complements and arbitrary-degree divisions are
covered by the complete E4 review. This does not classify general
tame conjugators, a different integral point set, or all native
integer periods. The missing lengths $9,12,18,24$ remain unresolved.

## 3. Exact multiplicative interface

The unchanged MS6 family is $k=\overline{\mathbb F}_p$, every prime
$p$, every $d\ge2$, every $c\in k$, $f=x^d+c$, and every
$g\in k(x)^\times$. Condition (CP) keeps all ordinary primitive
native periods and allows only finitely many exceptional cycles.
The proposed conclusion is $g^{p^e}=h\circ f/h$ for some $e\ge0$
and rational $h\ne0$. R6 already proves saturation conditional on
the existence of an integer-power rational transfer; it does not
provide that existence.

For $D=\operatorname{div}(g)$, write $P=f_*$ and $A=f^*$ on
finite rational divisors. The support's forward closure is finite
over this constant field. The canonical rational divisor

$$E_D=\sum_{n\ge1}d^{-n}P^nD$$

satisfies $(dI-P)E_D=PD$. Here coefficients and $d^{-1}$ are rational
numbers, not scalars reduced modulo $p$. The identities $PA=dI$
and $\|PU\|_1\le\|U\|_1$ include inseparable degrees and show
uniqueness even among potential solutions with unrestricted finite
support. The residual

$$\mathcal R_f(D)=AE_D-E_D-D$$

lies in $\ker P$. Its vanishing is equivalent to torsion of $[g]$:
an integer multiple of $E_D$ is principal on $\mathbb P^1$, and the
remaining nonzero constant has finite order. The constant is killed
explicitly, not silently discarded. The finite functional graph gives
the denominator $M=d^T\prod_i(d^{r_i}-1)$ and the reported transfer
degree bound before any additional constant-killing power.

Using the full determinant norm, including inseparability, a power
of $g$ divided by a genuine rational coboundary can be normalized to
$w$ with

$$N_f(w)=1,\qquad
\operatorname{div}(w)=-M\nu\mathcal R_f(D).$$

This preserves (CP) after excluding only finitely many actual support
cycles. The full missing implication is now precisely

$$N_f(w)=1\quad\text{and (CP)}\quad\Longrightarrow\quad w=1.$$

For $d=p^r$ the pushforward is injective and all classes are torsion.
Root supplied the stronger finite-field Frobenius construction:
translate a fixed point to zero, choose a finite field containing
all coefficients, and telescope a finite product of substitutions
to give exponent $p^{rs}-1$. It is prime to $p$, so the accepted
R6 saturation theorem gives $g=h\circ f/h$ under (CP), with no
remaining $p$-power. All $c,g$ in this pure-Frobenius subtype survive.
Mixed inseparable and general separable degrees are not settled.

The explicit sibling Hilbert 90 factorization uses $x\mapsto\zeta x$,
not native $x\mapsto f(x)$, so cannot telescope along native cycles.
The characteristic-five norm-one atom has infinitely many bad prime
periods and is not an MS6 counterexample. The characteristic-three
two-cycle control shows that a merged product of one can conceal
two nontrivial individual cycle products; it asserts no cofinite
counterexample.

## 4. First integrals and actual source boundaries

X2 proves that for $T(x,y)=(f(x),g(x)y)$, existence of a nonconstant
rational first integral is equivalent to torsion of $[g]$. A nonzero
Laurent coefficient index gives the integer-power relation; a base-only
invariant is constant by degree. This includes negative indices,
inseparability and a rational domain not containing $y=0$.

A pointwise return of each periodic vertical fiber under some later
iterate is automatic for every $g$: every nonzero multiplier belongs
to a finite field. Only a pointwise return under the exact base-period
iterate contains the intended information. The elementary non-torsion
control therefore defeats a loose fiber-return bridge, not MS6.

Root read the actual Bell--Moosa--Topaz Theorem 8.1 and its printed
proof sketch. It requires a fixed map pair and full inverse-image
invariance of hypersurfaces; the geometric reducedness condition also
matters in positive characteristic. The available vertical periodic
fibers fail full inverse-image invariance, and the purely inseparable
base fails geometric reducedness. This theorem is not an existence
bridge for the present problem.

Root also read the actual characteristic-zero setup and relevant
Proposition 3.22/Algorithm 9 proof passages in
[Chyzak--Dreyfus--Dumas--Mezzarobba](https://arxiv.org/pdf/1612.05518v2),
and the complete Theorem 1 statement in
[Faverjon--Poulet](https://arxiv.org/pdf/2511.18877v1).
The former solves a given monomial-base Mahler equation; the latter
works in a larger formal extension over an effective characteristic-zero
field. Neither supplies a finite algebraic transfer from (CP).
Root did not claim to read the first algorithm's final cost line or
either entire paper; E5 records its own slightly broader passage read.
Unsuccessful bounded searches establish neither novelty nor nonexistence
of an applicable theorem.

## 5. Smallest balanced atom: independently accepted reduction

For every odd prime, $f=x^2+c$ and
$g_a=(x-a)/(x+a)$ with $a\ne0$, A1 proves that (CP) implies
$c=-1$ and $a=\pm1$. All other parameters therefore have infinitely
many distinct bad ordinary primitive cycles. This is a reduction of
the unchanged all-parameter question, not its replacement or closure.

The divisor $[a]-[-a]$ is nonzero and has zero pushforward, so the
$\ell^1$ argument rules out any integer-power rational transfer for
every parameter. It does not by itself establish or refute (CP).

Under (CP), the weighted full-fixed-point product at every sufficiently
large prime $\ell$ equals the fixed-point product at time one whenever
neither signed support point is fixed. The exact resultant ratio
$F_\ell(a)/F_\ell(-a)$ then forces
$f^{\ell}(a)=f(a)$. The latter point's period divides $\ell-1$
for every sufficiently large prime, so an elementary Euclid argument
bounds its period by two. A periodic predecessor is $a$ or $-a$.
One selected congruence progression would not justify this argument.

For a noncritical signed support cycle, choose $N$ killing its return
multiplier. Its first nonidentity local coefficient at time $N\ell$
is $\ell$ times that at time $N$, for $\ell\ne p$. Delete the
support root from the weighted product. All finite exceptional cycles
and their multiplicities stay unchanged for sufficiently large primes,
whereas this local coefficient scales the product by $\ell$. The
resulting requirement $\ell\equiv1\pmod p$ for all large primes is
impossible for odd $p$. Constancy of multiplicity along every new
cycle, including critical cycles, is proved separately.

A signed nonzero support point must therefore lie on a critical cycle
of length two. This forces $0\mapsto-1\mapsto0$, giving exactly the
remaining parameter family. For its good cycles $O$ the product is
$(\prod_{x\in O}x)^{-3}$. A uniform finite multiplier group is a
necessary condition under (CP), not a rigidity theorem.

Root actually read the relevant statements in
[Levy, arXiv:1304.2834v2](https://arxiv.org/html/1304.2834v2),
including Theorems 1.1, 1.10 and 1.12 and Corollary 1.14 with its
proof. They concern spectra of map families; Theorem 1.12 additionally
excludes spectra contained in the algebraic closure of the prime field.
They do not supply the required finite-multiplier-set theorem for this
single map. No external theorem is needed for A1's reduction proof.

## 6. Byte bindings and next gate

The original seven bindings were actually read on 2026-09-09 at
18:15 UTC; A1's final and E5's revised final bindings were subsequently
read from the actual files after full final-text reads. E8's final
binding was actually checked after its complete 296-line read.

| Relative file | SHA256 |
| --- | --- |
| `a1_balanced_divisor_detection/REPORT.md` | `59f79d718d85e0c2b4bbaea2e8d78416b5cb48e52927fe044605fb5847bc6e8f` |
| `a2_multiplicative_existence/REPORT.md` | `2cd5f0765f382180badde4ffe9f3ec20f77649be5e461a41dfe81cb8731d88b2` |
| `c2_nine_reflection_lifting/REPORT.md` | `98fc3d0ed9b30c38c6050fe41ae60392e7cb720c84cb6c0b1399dcf2346f78f3` |
| `c4_specific_nine_lift/REPORT.md` | `1dfc67f4171979139817231b6f95bf667cff58d87ea169e681f019370acc274f` |
| `x2_pointwise_periodic_fibers/REPORT.md` | `0a9cb0a92df6151d974184a1672c3f1ef42b84a29057aa23e57fb14e8661e703` |
| `reviews/e4_specific_nine_lift/REVIEW.md` | `48df50abc00541bc495950342754590b31c638e76a0dc06755d8ccdadedf796d` |
| `reviews/e5_multiplicative_divisor/REVIEW.md` | `69dcce664646b4555d5f98d4460aef90ab82e08535b6d285faff6df4b379dd7f` |
| `reviews/e6_nine_reflection_lifting/REVIEW.md` | `b89444ad0070cc85b4fe75941ce03a701b8b78badbe2f96fb08ba332b0003450` |
| `reviews/e8_balanced_divisor_detection/REVIEW.md` | `3c60b9996a18c3f46a3711d6a5533316a6e21cb9c0a6bfda5f622b70d6b84cd3` |

Next: perform the independent integration audit of the exact final R7
payload and synchronize authorized paths only. No R7 push is claimed here.
Two bounded R8 follow-ups already reuse A2 and X2 in exclusive new
directories for the critical atom and its precise finite-multiplier
source interface. Their live work is separate from this R7 checkpoint.
An additional bounded D1 R8 scout now tests at most two genuinely
independent full questions after subtracting all four admitted contracts
and the rejected R6 candidates. It has at most three source batches and
no mathematical execution. No fifth contract is promised by that scout.
Old rounds, admission decisions and eight inherited untracked directories
remain unchanged. No mathematical census, new agent, external model/API,
GPU, credential/configuration, manuscript/PDF or formal-evaluation work
is authorized by this checkpoint. `NO_BAD_EULER_OR_ROOT_NUMBER` remains.
