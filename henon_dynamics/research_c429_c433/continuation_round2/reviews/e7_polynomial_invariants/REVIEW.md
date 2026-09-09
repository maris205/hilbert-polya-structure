# E7 Round 2 — polynomial invariant separators

2026-09-09 UTC. Independent current-session nonauthor internal review by
`c429_e7_congruence_review`. This is a bounded proof/source audit, not human
peer review, formal evaluation, admission, or a full manuscript panel.

## Verdict and actual coverage

**AUXILIARY_PROOFS_PASS; ZERO_SUBSTANTIVE_MUST_FIX;
LG4_UNCLOSED; PAPER_COUNT_CONTRIBUTION_ZERO.**

I read both actual files completely and independently checked every proof
step, including the infinite-quantifier arguments and explicit controls:

| Reviewed file | Lines | SHA-256 |
| --- | --- | --- |
| [REPORT](../../b1_global_orbit_separation/REPORT.md) | 203 | `644d8be77e68cd6b48b0ba717c8ffcb2597478cfb63346d30c3ca6e9df3b2c2e` |
| [PROOF_PACKAGE](../../b1_global_orbit_separation/PROOF_PACKAGE.md) | 534 | `36531ac17486e5b4e358dbaa7764fd8423bf8e395beb1248fe1221f51ffc83c8` |

Both hashes match the coordinator's frozen inputs. Root/Hénon/batch
instructions, `CONTINUOUS_RUN.md`, and the batch skill/workflow were read.
Previously accepted first-pass results were not reopened or counted again.
This round's proofs are self-contained apart from standard algebra and
curve facts; their nearest-source ownership was checked separately below.

No substantive counterexample to BDQ, UPI, or the finite control was found.
The scope distinctions in the report are correct: bounded-degree failure
is not unrestricted-degree failure; unrestricted invariant values recover
separate prime-power incidence, not a proved common mixed-modulus time.

## 1. BDQ: pointwise invariance, exact grid, and all denominators

Proof lines 119–151 establish a function-zero test, not a formal
polynomial-zero test. For an integer polynomial of partial degrees at most
L, its Newton coefficients are integer linear combinations of values on
\(\{0,\ldots,L\}^2\). If all these values are divisible by m, all Newton
coefficients are divisible by m. Binomial polynomials have integer values
at every integer, including negative integers, so the expansion proves
divisibility on all of \(\mathbb Z^2\).

There is no inversion of \(i!j!\) in \(\mathbb Z/m\mathbb Z\), no field
assumption, and no problem when distinct grid integers have equal residues.
The conclusion is only that the polynomial represents the zero function
modulo m. Nonzero formal null polynomials are correctly retained.

For the matrix in lines 155–186, \(dD=L\) bounds the total, hence both
partial, degrees of each \(b_j\circ F-b_j\). Over Q, vanishing on the grid
does imply formal zero by ordinary interpolation. A kernel vector gives
an invariant polynomial with constant coefficient zero. Under
\(\mathbb Q[x,y]^F=\mathbb Q\), it is zero, so the matrix has full column
rank. This use of rational interpolation is separate from the finite-ring
function argument; the proof does not interchange them.

The specified first nonzero maximal row minor therefore exists. Its
absolute determinant defines a positive, effectively specified integer
\(\Delta(F,D)\). An exhaustive finite determinant search is a definition
of a terminating method here, not a claim that it has been executed.

For every coefficient lift of h, the grid lemma makes pointwise invariance
equivalent to \(Ma=0\pmod m\). The constant coefficient cancels. The
adjugate then proves \(m\mid\Delta a_j\), without cancelling a nonunit.
Writing \(g=\gcd(m,\Delta)\) yields \(m/g\mid a_j\). If
\(P\equiv Q\pmod\Delta\), every monomial difference is divisible by g;
its product with the corresponding coefficient is divisible by m.

This covers every prime power and mixed modulus simultaneously. In
valuation language, the coefficient contributes at least
\(\max(0,v_p(m)-v_p(\Delta))\), while the monomial difference contributes
at least \(v_p(\Delta)\). Their sum is at least \(v_p(m)\) for every p.
There is no hidden restriction to primes coprime to the minor.

The no-invariant hypothesis is genuine. For example, if F is the identity,
h=x is invariant at every modulus; no positive Delta makes all pairs
\(P\equiv Q\pmod\Delta\) indistinguishable at every modulus. The proof
correctly confines the hypothesis to BDQ and not UPI.

## 2. The no-invariant Hénon proof and the cutoff-dependent family

Proof lines 239–282 are valid for a single generalized Hénon map
\(H(x,y)=(y,p(y)-ax)\), \(\deg p=e\ge2\), \(a\ne0\), over C.

If an irreducible curve is preserved by \(H^r\), the induced automorphism
extends to its smooth projective normalization and permutes the finite
boundary set S. At least one coordinate has a pole at some boundary point:
otherwise both extend as regular functions on the complete curve and are
constant. Set their pole orders to u and w, with negative orders and an
identically zero coordinate treated as in the proof.

If \(w\ge u\), then \(w>0\) and \(ew>u\); the leading pole of p(y)
cannot cancel with ax. Forward pole orders grow by powers of e. If
\(u>w\), inverse iteration gives the corresponding growth from the pole
of x. In either direction the growth persists along multiples of r.
On those iterates, however, the functions are pullbacks of the fixed x,y
under a permutation of S, and hence their pole orders belong to a finite
set. This is the required contradiction.

The argument does not assume H itself fixes the curve when only \(H^r\)
does: intermediate coordinate pullbacks are still rational functions on
the original curve, and only the multiples of r are compared with the
boundary permutation. Reducible curves reduce to a component and a
further iterate. A nonconstant invariant polynomial has a nonempty curve
fibre whose components are permuted, so none exists.

For \(F_0=(y,y^3-x)\), the family
\(P=(1,2)\), \(Q_D=(1+10\Delta(F_0,D),2)\) therefore satisfies BDQ.
Its integer-orbit separation is also proved, not inferred from sampling:
the positive recurrence strictly increases, and the two backward base
cases give \(a_{-r}=-a_{r-1}\) for every \(r\ge1\). Thus the second
coordinate is 2 only at native time zero. Since \(Q_D\ne P\), it is not
on the two-sided orbit. P has an unbounded forward orbit; Q has an
unbounded backward orbit in the positive cone \(x>y\), so both are
nonperiodic.

This establishes \(\forall D\,\exists Q_D\) for the bounded-degree test.
It does not establish \(\exists Q\,\forall D\), and it does not establish
all-modulus orbit incidence for any of these pairs. The report preserves
both distinctions explicitly.

## 3. UPI: interpolation and clearing at the correct modulus

Proof lines 323–357 correctly treat \(L_a\) as a rational polynomial
evaluated first in Q. Its Newton coefficients are
\((-1)^{j-a}\binom ja\) for \(a\le j<q\), so its values are integers.
For \(q=p^r\) and \(j<q\), all intermediate coefficients
\(\binom qi\), \(0<i\le j\), are divisible by p. Vandermonde's
identity therefore makes \(\binom tj\) q-periodic modulo p. This also
holds at negative t by the polynomial identity and backward iteration.

Consequently \(L_a\) is the indicator of the residue a modulo q when
its *values* are reduced modulo p. Tensor products and summation over the
full cycle give an integer-valued f of total degree at most \(2(q-1)\).
Because F is a permutation modulo q, it preserves both the cycle and its
complement. Hence \(f\circ F-f\) takes values in \(p\mathbb Z\), while
\(f(P)-f(Q)\) is a p-adic unit. Invertibility is used at this step; the
argument is not silently generalized to arbitrary noninvertible maps.

The denominator of \(L_a\) is, up to sign,
\(a!(q-1-a)!\), a divisor of \((q-1)!\). Thus
\(A_q=((q-1)!)^2\) clears all coefficients of f. For
\(s=v_p(A_q)\), the ordinary integer polynomial \(H=A_qf\) satisfies

\[
p^{s+1}\mid H(F(z))-H(z)\quad(z\in\mathbb Z^2),\qquad
v_p(H(P)-H(Q))=s.
\]

This proves invariant function separation modulo \(p^{s+1}\), retaining
the displayed degree bound. Even when the clearing factor is a nonunit,
the difference survives at precisely the stated modulus. No rational
coefficient is reduced illegally, and formal polynomial invariance is
not asserted. For r=1, K=1; the modulus can remain unchanged rather than
strictly increase. That harmless edge case does not affect the proof.

Conversely, if Q lies in the orbit of P modulo every separate prime
power, reducing any invariant h modulo each exact prime-power divisor
of m gives equal values there. CRT gives equality modulo m. This
argument does not require a common hitting time. These two implications
prove UPI with exactly the stated quantifiers and without the BDQ
no-invariant hypothesis.

## 4. Mixed phases and the exact nonlinear control

The time coset at q is \(a_q+t_q\mathbb Z\). For a mixed modulus,
membership requires intersection of these cosets, equivalent to their
pairwise compatibility modulo \(\gcd(t_{q_i},t_{q_j})\). The proof of
generalized CRT in lines 427–431 is valid. CRT on scalar polynomial
values does not provide this time compatibility.

For \(F=(y,x+6y^2)\), the displayed inverse is correct. Modulo 6, F is
the swap, with P-cycle \((0,1),(1,0)\); Q reduces to \((4,3)\) and is
absent. Modulo 2, Q=P and only even times hit. Modulo 3, Q is the swapped
point and only odd times hit. Every invariant polynomial modulo 6 has
equal P,Q values modulo 2 and modulo 3, hence modulo 6.

The set-theoretic cycle indicator separates them, so it cannot be an
ordinary polynomial function over \(\mathbb Z/6\mathbb Z\). This is a
valid distinction between a finite orbit quotient and a polynomial-value
quotient, not a failure of finite orbit quotients themselves.

Modulo 4, direct substitutions give
\((0,1)\to(1,2)\to(2,1)\to(1,0)\to(0,1)\).
Q is \((0,3)\), absent. Thus the control fails UPI's all-level
prime-power premise and is not an LG4 false positive. Nothing here proves
strict separation between *all-level* prime-power incidence and all-mixed
incidence for integral triples; the report explicitly leaves that question
unresolved.

## 5. Primary-source audit and subtraction

The following source passages were actually read on 2026-09-09:

- [Schauz, arXiv:1212.5522v3](https://arxiv.org/pdf/1212.5522v3): definitions
  distinguishing ordinary polynomials and polyfracts; Theorem 2.5 with
  proof; Corollary 3.7 and Theorem 3.8 with its interpolation proof;
  Theorems 3.14–3.17 with their primary-decomposition and variable-splitting
  arguments. The adjacent Theorem 3.6 statement/proof and Corollary 3.13
  proof were also read to check the interfaces. These passages concern
  integer-valued/binomial representations, not arbitrary ordinary
  coefficient polynomials at the same modulus. They support the declared
  ownership of interpolation and primary decomposition. They do not give
  the missing arithmetic orbit-separation theorem.
- The [arXiv metadata](https://arxiv.org/abs/1212.5522) confirms the author,
  title, *Journal of Number Theory* 139 (2014), 1–28, and related DOI
  `10.1016/j.jnt.2013.12.010`. Direct DOI opening returned a retrieval error;
  this is not recorded as successful publisher access. The theorem
  numbering audited is explicitly the author's v3 preprint.
- [AKNTVV, author-hosted published article](https://www.imo.universite-paris-saclay.fr/~ekaterina.amerik/articles/DBM.pdf):
  Theorems 4.2–4.4 statements on printed page 60, and Proposition 4.9 with
  proof on page 63. The target invariance/preperiodicity conditions and
  forward-time predecessor obstruction remain as reported. These
  statements do not settle the arbitrary wandering two-sided target.

This is a source-application/ownership check, not a full reproof of Schauz's
entire paper or an exhaustive novelty survey. The local proof independently
establishes the elementary statements used. The author correctly subtracts
the source-owned interpolation and decomposition. The adjugate obstruction,
pole argument, dynamical specialization and explicit clearing factor remain
auxiliary contributions at the stated batch threshold; they are not grounds
for counting a new paper or claiming global novelty.

## Must-fixes and final allowed-claim matrix

**Substantive mathematical/source must-fixes: none.** No author-file
revision is required for the displayed auxiliary claims. Optional wording
only: “possibly increased modulus” is more literal than “increase” at
REPORT line 130 / Proof line 54, since r=1 gives K=1. No strict-increase
claim is used anywhere in the argument.

| Claim | Verdict | Necessary retained boundary |
| --- | --- | --- |
| BDQ for every fixed degree and every modulus | Allowed, proved | Requires the stated rational no-invariant hypothesis; invariance is pointwise. |
| Explicit Delta from a finite integer minor | Allowed, effective definition | No determinant run, numerical value, optimality or practical complexity is certified. |
| No periodic algebraic curve for the displayed generalized Hénon map | Allowed, proved | Single-factor map with degree at least two and nonzero a, as proved. |
| Nonperiodic off-orbit witnesses passing fixed-degree tests at all moduli | Allowed, proved | The witness depends on D; not an unrestricted-degree or LG4 false positive. |
| UPI equivalence and explicit prime-power separator bound | Allowed, proved | All moduli on the polynomial side; separate prime powers on the orbit side; clearing may change the modulus. |
| Mod-6 polynomial blindness despite incompatible local time phases | Allowed, proved | Single-modulus control, explicitly failing modulo 4. |
| All-level prime-power hits automatically give mixed-time compatibility | Unresolved | Neither proved nor refuted by the control. |
| Every off-orbit integral target has a prime-power separator | Unresolved | This is the stronger required separation input for the scalar-invariant strategy. |
| Full LG4, a general quotient-route no-go, or a new admitted paper | Not established | Preserve original mixed-modulus contract and auxiliary-only disposition. |

Only this assigned review file was created. Zero mathematical programs,
reruns, author edits, shared-index/Git changes, builds, evaluations, external
model/API uploads, or extra agents were used. The research-review and batch
skills supplied claim/source discipline under current-session internal
review rules; no external or full-panel review is claimed.
`NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
