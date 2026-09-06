# Wild ordinary-count continuation: outcome

2026-09-06. No C-number assigned; no paper draft or old-check rerun.

## Original target

**Refuted.** For $f=x+x^4$ in characteristic $3$, a root $a$ of
$h=x^4+2x^3+2$ has least period $12$ and

$$
f^{12}(a+u)-a-u=(a^2+a)u^{12}+O(u^{13}),\qquad a^2+a\ne0.
$$

The independent polynomial certificate is

$$
f^{12}-x\equiv h^{12}(x^3+2x^2+x+1)\pmod {h^{13}}.
$$

The local calculation uses degree-$52$ modular arithmetic, not the
degree-$4^{12}$ full iterate. The twelve points contribute a deficit
of at least $36$ between the established first-return weighted formula
and the ordinary nonzero count at every time divisible by $12$. No exact
global ordinary count is inferred from this lower bound.

## Closed replacement result

`PROOF_PACKAGE.md` proves a general Frobenius-degree transfer theorem for
$f_q=xH(x)^q$:

$$
1+G_C(v)\equiv(1+v)\left[
\prod_{a\in C}\frac{H(a(1+T))}{H(a)}
\right]^{[q]}_{T=v^q}\pmod {v^{q^2}}.
$$

If the first nonconstant product coefficient has index $\nu<q$, the
first-return multiplicity is exactly $q\nu$, with an explicit leading
coefficient. The precision is sharp already on genuine two-cycles.

For fixed $K=\mathbb F_{p^d}$, $H\in K[x]$, and a residue class $r$,
all nonzero $K$-cycles of $xH(x)^{p^{r+jd}}$ have one fixed finite
ramification profile once $p^{r+jd}>\deg H(|K|-1)$. In odd
characteristic, established local theorems then give every later return
multiplicity. This is an all-cycle result in one fixed finite field,
not an all-geometric-cycle result for one fixed polynomial.

It produces the explicit infinite family
$F_j=x+x^{3^{4j+1}+1}$: each map has the displayed least-$12$ cycle
with first-return multiplicity $4\cdot3^{4j+1}$. The low-exponent
case is separately certified. The maps have distinct degrees and are
not dynamically affine.

## Assessment

The original ordinary-count contract remains unavailable. The transfer
theorem is a mathematically complete possible technical note, not another
weighted-zeta note. Its generality, explicit precision, and infinite
exceptional family are real; its core argument is elementary and short.
`SOURCE_AUDIT.md` recommends non-author source/substance review, not
automatic paper admission. The two strongest independently complete
remaining routes should take priority over a quota-driven selection.

## Artifacts and exact-check scope

- `PROOF_PACKAGE.md`: complete proofs and the original-target rejection.
- `SOURCE_AUDIT.md`: primary reading scope, attribution, and self-assessment.
- `EXACT_CERTIFICATE.json`: the passing bounded $h$-adic certificate.
- `verify_h_adic.py`: exact polynomial verification, stdout only.
- `verify_period12.py`: separate translated-jet verification, stdout only.
- `targeted_orbit_probe.py`: the new bounded discovery probe; it stopped
  after fields of orders $9$, $27$, and $81$.

No old round2 file was changed or checked by executing its scripts. The
coordinator additionally reported a standard-library independent
verification in its own new file. No Git mutation, external model upload,
Route-A evaluation, arithmetic Euler factor, or root-number claim was
performed in this lane.
