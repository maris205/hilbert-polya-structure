# Nonadditive positive-characteristic scout: no new admission

2026-09-07 UTC. Bounded continuation of the same C419–C423 batch.
The two [frozen contracts](FROZEN_CONTRACTS.md) are the entire candidate
set for this lane. M1 and AS2 are not re-evaluated or changed.

## Outcome

| Contract | Exact obstruction or deducted owner | Disposition |
|---|---|---|
| NC1: all native ordinary counts for every odd-characteristic map `lambda*x*(1+x)^p` | Already inside the earlier general `x*H(x)^p` first-return problem. A new symbolic two-cycle certificate also disproves the tempting multiplicity-`p` shortcut for every odd prime. | `REJECT_AS_NEW_LANE; COMPLETE_OBSERVABLE_UNCLOSED` |
| NC2: all finite-extension cycles of `(x,y) -> (x^p,y+x^(p+1)+a*x^2)` | The full answer is an elementary skew-return identity followed by the classical zero count of a trace quadratic form. Both the rank-zero case and the characteristic-divisible time case are retained. | `REJECT_CLASSICAL_RECONSTRUCTION` |

**New admissible contracts: 0.** There is no new manuscript, C-number,
formal Route-A evaluation, or claimed target arithmetic bridge. The
symbolic certificates below are screening evidence, not additional papers.
No polynomial census, finite-field experiment, old check, GPU job or paid
model call was run. Source retrieval and read-only file inspection are not
reported as mathematical experiments.

The research-lit / idea-creator source-first screen and the batch skill's
substantial-question gate determined these dispositions. The proof-writer
discipline is used for the two short collision certificates, not to
mislabel a rejected candidate as a complete research proof package.

## NC1: the apparent subtype change does not survive collision checking

The frozen family is

$$
f_\lambda(x)=\lambda x(1+x)^p,
\qquad p\text{ odd},\quad \lambda\in\overline{\mathbb F}_p^\times.
$$

All counts refer to distinct affine geometric points under ordinary
composition. Scheme degree, a weighted first-return count, a finite-field
restriction or an inverse clock cannot replace this observable.

Since

$$
\frac{f_\lambda'(x)}{f_\lambda(x)}=\frac1x,
$$

the nonzero periodic multipliers telescope to one. If
`alpha^p=lambda`, then `f_lambda=x H(x)^p` with
`H(x)=alpha(1+x)`. The unique p-th root exists in the algebraic closure.

This is an exact local collision with the general hypotheses of
[the previous first-return package](../../../continuation_c407_c408_round3/wild_ordinary/PROOF_PACKAGE.md).
That package permits arbitrary nonconstant `H`; it does **not** require
`H(0)=1`. Its completed result is a Frobenius-degree-lifting statement for
fixed finite fields, not a uniform ordinary count over the algebraic
closure. Its original universal multiplicity assertion was already
disproved at `p=3`, `lambda=1`, least period `12`.

The separate
[weighted-observable package](../../../continuation_c404_c408_round2/wild_dynamics/PROOF_PACKAGE.md)
does assume `H(0)=1` and supplies a weighted count, not the NC1 observable.
It is an exact overlap at `lambda=1`, not a license to extend its formula
unchanged to every `lambda` or to call its weights distinct points.

Thus adding a displayed scalar does not create a new independent problem.
The initial suggestion that this was the most promising new contract is
withdrawn after checking the actual old hypotheses.

### Exact cheap falsifier: a two-cycle of multiplicity 2p for every odd p

Fix an odd prime `p`. Choose

$$
u^{p+2}=1,\quad u\ne1,
\qquad b_0=\frac{u-1}{2},\quad b_1=\frac{u^{-1}-1}{2},
\qquad
\lambda=-\frac{1}{u(1+b_0)^p}.
$$

Such a `u` exists because `p` does not divide `p+2`. Since `p+2` is odd,
`u` is neither `-1` nor an element of order two. Consequently `b_0,b_1`
are distinct and nonzero, and the denominator defining `lambda` is
nonzero. Moreover,

$$
b_1=-b_0/u,\qquad 1+b_1=(1+b_0)/u,\qquad u^p=u^{-2}.
$$

Substitution gives

$$
f_\lambda(b_0)=b_1,\qquad
f_\lambda(b_1)=-b_1u^{-p-1}=-b_1u=b_0.
$$

This is a genuine least-period-two orbit, defined over a finite extension.
Let `alpha^p=lambda`, set `c=alpha^2`, and write

$$
G(x)=c(1+x)\bigl(1+\lambda x(1+x)^p\bigr).
$$

Direct composition in characteristic `p` gives

$$
f_\lambda^2(x)-x=x\bigl(G(x)-1\bigr)^p,
$$

and

$$
G'(x)=c\bigl(1+\lambda(1+x)^p(1+2x)\bigr),
\qquad G''(x)=2c\lambda(1+x)^p.
$$

The two-cycle identity and `b_0 != 0` imply `G(b_0)^p=1`, hence
`G(b_0)=1`. The selected parameter gives `G'(b_0)=0`, while
`G''(b_0) != 0`. Since `p` is odd, the quadratic Taylor coefficient is
nonzero, so

$$
\operatorname{ord}_{b_0}(G-1)=2,
\qquad
\operatorname{ord}_{b_0}(f_\lambda^2-x)=2p.
$$

This proves the frozen cheap hypothesis false symbolically, without a
finite search. It does **not** disprove the possibility of a more involved
all-period classification. It does show why replacing all first-return
weights by one cannot close NC1. No all-parameter, all-period multiplicity
classification is proved here; no claim of global literature absence is
made. This lane stops at its recorded collision/replacement boundary.

## NC2: complete classical reduction, including all degenerate cases

Fix any odd prime `p`, `a in F_p`, and `r,n >= 1`. Write

$$
h_a(x)=x^{p+1}+a x^2,\qquad
S(x,y)=(x^p,y+h_a(x)),\qquad X_r=\mathbb F_{p^r}^2.
$$

The inverse on `X_r` is obtained by inverse Frobenius in the first
coordinate and subtraction of the corresponding forcing in the second;
thus this is a finite permutation. Induction gives

$$
S^n(x,y)=\left(x^{p^n},\ y+\sum_{j=0}^{n-1}h_a(x)^{p^j}\right).
$$

Put `d=gcd(n,r)` and `m=n/d`. The first-coordinate fixed points are
exactly `F_{p^d}`. On that subfield the sum consists of `m` complete
Frobenius-trace blocks. Define

$$
Q_{d,a}(x)=\operatorname{Tr}_{\mathbb F_{p^d}/\mathbb F_p}
              (x^{p+1}+a x^2),\qquad
Z_{d,a}=\#\{x\in\mathbb F_{p^d}:Q_{d,a}(x)=0\}.
$$

Every allowed first coordinate leaves all `p^r` choices of `y` fixed.
The full return formula is therefore

$$
F_{p,a,r}(n):=\#\operatorname{Fix}(S^n|X_r)
=\begin{cases}
p^{r+d},&p\mid m,\\
p^r Z_{d,a},&p\nmid m.
\end{cases} \tag{1}
$$

No assumption such as `p` not dividing `d`, `r` or `n` has been introduced.
Extension degree `r` is not identified with native time `n`.

### Uniform evaluation of the remaining standard quadratic form

Choose any `F_p`-basis `e_1,...,e_d` of `F_{p^d}` and form the symmetric
matrix

$$
A_{ij}=\frac12\operatorname{Tr}
 (e_i e_j^p+e_i^p e_j+2a e_i e_j).
$$

Then `Q_{d,a}(sum v_i e_i)=v^T A v`. Diagonalize `A` by congruence over
`F_p`. Let `k` be its rank, and, if `k>0`, let `Delta` be the product of
the nonzero diagonal entries, considered modulo squares. Both the rank
and this square class are independent of the selected basis and
diagonalization. With `chi` the quadratic character of `F_p^*`, the
classical finite-field quadratic-form formula is

$$
Z_{d,a}=\begin{cases}
p^d,&k=0,\\
p^{d-1},&k\text{ odd},\\
p^{d-1}+(p-1)\chi((-1)^{k/2}\Delta)\,
             p^{d-k/2-1},&k>0\text{ even}.
\end{cases} \tag{2}
$$

For completeness, the radical has `p^{d-k}` elements, and every zero of
the induced nondegenerate form has precisely that many lifts. Multiplying
the nondegenerate zero formula by this factor gives (2). For `k=0` the
form is identically zero, which explains the separate first case. These
are explicit finite linear-algebra instructions for every displayed
parameter, with no factorization of a growing iterate and no unspecified
sign: the sign is the displayed Gram determinant square class.

The primary source [Bouw et al., Section 0.2](https://arxiv.org/html/1410.7031v2#Ch0.S2)
uses precisely the trace form associated with `Y^p-Y=X R(X)` and records
the quadratic zero formula as Theorem 0.2.1, attributed there to Joly.
Here `R(X)=X^p+aX` is additive. Its Proposition 3 also gives the curve
connection `#C_a(F_{p^d})=p Z_{d,a}+1`. These are deducted classical
inputs, not claimed new arithmetic. The source's later Theorem 0.8.1 is
restricted to extensions containing a specified splitting field; it is
**not** used to assert that its special numerator formula holds over
every `F_{p^d}`.

Finally `S^{pr}=id`: after `r` steps the fibre displacement is a member
of `F_p`, killed by `p` repetitions. Hence every cycle length divides
`pr`. For all positive integers `ell`, the exact number of cycles is

$$
c_\ell=\frac1\ell\sum_{j\mid\ell}\mu(\ell/j)F_{p,a,r}(j),
$$

and is zero when `ell` does not divide `pr`. This is ordinary finite
permutation inversion; its rational Euler product is not an additional
result. Equations (1)–(2) close the frozen count task by classical
reconstruction. No substantial residual or new target dictionary remains
in this exact candidate.

## Handoff boundary

The [source audit](SOURCE_AUDIT.md) records twelve actual fresh search
formulations, actual primary reading scopes, failed theorem matches and
nearby local contracts. No global novelty claim follows from this bounded
screen. Earlier closed-chain, skew inverse and mixed-clock candidates are
not silently treated as the same mathematical problem; the exact NC1
collision and the explicit NC2 classical reduction are the reasons for
rejection.

Only this directory was written. No accepted proof, global state, Git
object, old artifact or manuscript was edited. This result leaves the
coordinator's existing two admitted contracts intact and contributes zero
toward the remaining three. Any further candidate requires a new bounded
assignment, not a hidden third candidate in this lane.
