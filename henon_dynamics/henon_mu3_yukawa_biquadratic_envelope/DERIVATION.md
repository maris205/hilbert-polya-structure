# HCS-C60 derivation ledger

Status: **PREFREEZE_CODE_RESULTS_PASS / POSTREFRESH_PASS;
FORMAL_DOCS_PASS; PAPER_PENDING; NOT_RELEASED.**

This ledger records deterministic mathematical consequences of the locked
C60-EXACT premises. The official independently checked machine tuple now
certifies all eight premises at the prefreeze code/results layer. This edited
post-machine ledger and the complete 13-root package have now passed their
independent hostile audit; the live Route binds the externally computed
post-machine aggregate, so the current formal status is `FORMAL_DOCS_PASS`.

## Post-refresh machine handoff

The machine-bound facts are exact:

```text
status: PREFREEZE_CODE_RESULTS_PASS / POSTREFRESH_PASS
inventories code/results/live/scoped: 13 / 8 / 21 / 20
tests per refresh cycle: 53
official test cycles: 2
payload scalar leaves: 9310
value/type/structural mutations: 9339 / 9339 / 14
group/resolver/evidence/artifact hostile rebounds: 6 / 4 / 10 / 2
actual evidence-and-artifact hostile total: 12
snapshot rebind checks: 39
payload: dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead
certificate: d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518
schema: c7ddb4ff8fa890f9f801d615158c9038299487affa3808f25fe5d73c987791a5
independent check: 25bc9c1c656da742359814054b66c05e18a304ca85741776c055152a30a98e44
scoped manifest: f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7
group evidence: dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2
resolver evidence: f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da
source contract: 4c484b3532c4604b028f45fc157c261149a7a49ca9631bbcf83f8d1efd1cdb90
G0: 0512db556004edde7c19176bbb35375beaeba89301da53902d5c5d98001cb8a8
official refresh log: 5f5d788a1493c16a8eec86ec0cb40bfed2dea72fa2257bddf50eed1be2c43239
```

Every C60-EXACT-0--7 machine gate is `PREFREEZE_CODE_RESULTS_PASS`.
The historical machine-bound formal aggregate is
`fd76237963d385b79b10b7ea13477173b2cf17261fc47d5b43697379d9b012ca`,
and its historical machine-time Batch input is
`bd2a4881e636e18efd0d9917b99ba84b01c7507d6dcff0cefe28f5e5a3661cc3`.
Neither identifies these changed post-machine formal bytes; their replacement
aggregate is bound externally in the live Route following the independent
`FORMAL_DOCS_PASS` verdict.
Release promotion remains unauthorized; implementation/provenance commits,
the full-project manifest, Route archive, paper sources, and paper PDF remain
null or pending.

## 1. Orders, indices, and lattice

The target orders give

$$
[G:N]=160,\qquad [G:H_i]=320,\qquad [G:J]=640.
$$

Because $J\subset H_i\subset N$ and $N/J\cong V_4$, the reverse fixed-field
lattice is

$$
M=K^N\subset F_i=K^{H_i}\subset L=K^J,
$$

with degrees $[F_i:M]=2$, $[L:F_i]=2$, and $[L:M]=4$.

## 2. Normalizer and core formulas

For $H\le G$,

$$
\operatorname{Aut}_{\mathbf Q}(K^H)=N_G(H)/H,
$$

and the normal closure inside $K$ is fixed by $\operatorname{Core}_G(H)$.
The target normalizers and trivial cores therefore yield the automorphism and
normal-closure claims. Self-normality of $N$ gives
$\operatorname{Aut}_{\mathbf Q}(M)=1$.

## 3. Primitive-element calculation

If an integral carrier $\theta$ is fixed by $H$ and has $[G:H]$ distinct
reductions among its full $G$-orbit at one common good prime, then it has
exactly $[G:H]$ characteristic-zero conjugates. Hence

$$
\operatorname{Stab}_G(\theta)=H,\qquad \mathbf Q(\theta)=K^H.
$$

This is the only route from the design carriers to the fixed-field
identities. A support stabilizer without modular noncollision does not pass.

## 4. Formal degree-two fixed space

The degree-at-most-two part of
$\mathbf Q[X_1,\ldots,X_{27}]$ is spanned by point-indexed linear and square
monomials and unordered-pair-indexed mixed monomials. Therefore equality of
the $H_0$ and $N$ point and pair partitions implies

$$
\mathbf Q[X_1,\ldots,X_{27}]_{\le2}^{H_0}
=\mathbf Q[X_1,\ldots,X_{27}]_{\le2}^{N}.
$$

The selected cubic orbit is a separate exact stabilizer certificate. No
claim is made for the quotient by all algebraic relations among the roots.

## 5. Rational $V_4$ relation

For $V=V_4$ and its three order-two subgroups $A_i$,

$$
[V/1]+2[V/V]=[V/A_1]+[V/A_2]+[V/A_3]
$$

as rational characters. Inflating along $N\to N/J$ and inducing to $G$ gives

$$
[G/J]+2[G/N]=[G/H_+]+[G/H_0]+[G/H_3].
$$

Artin formalism gives the corresponding product of Dedekind zeta functions.
This is not a $G$-set isomorphism.

## 6. Signature derivation

For a degree-$n$ coset carrier with $o_c$ complex-conjugation orbits,

$$
r_1+2r_2=n,\qquad r_1+r_2=o_c,
$$

so $r_1=2o_c-n$ and $r_2=n-o_c$. The target pairs $(n,o_c)$ are
$(160,88)$, $(320,168)$, $(320,160)$, and $(640,320)$, yielding
$(16,72)$, $(16,152)$, $(0,160)$, and $(0,320)$.

## 7. Conductor-discriminant derivation

For orbit counts ordered as
$(I_3,P_3,Q_3,I_5,P_5,C_3,C_2)$, use

$$
v_3=(n-o_{I_3})+\frac{n-o_{P_3}}2+(n-o_{Q_3}),
$$

$$
v_5=(n-o_{I_5})+\frac34(n-o_{P_5}),\quad
v_A=n-o_{C_3},\quad v_B=n-o_{C_2}.
$$

The target vectors and results are:

| field | orbit counts | $(v_3,v_5,v_A,v_B)$ |
|---|---|---|
| $M$ | $(22,28,56,8,32,64,80)$ | $(308,248,96,80)$ |
| $F_+,F_3$ | $(36,56,112,16,64,128,160)$ | $(624,496,192,160)$ |
| $F_0$ | $(28,56,112,16,64,128,160)$ | $(632,496,192,160)$ |
| $L$ | $(56,112,224,32,128,256,320)$ | $(1264,992,384,320)$ |

The inherited exact support and even $r_2$ values give the signed absolute
formulas in the theorem package.

## 8. Relative discriminant derivation

The tower identity

$$
\operatorname{Disc}(E/\mathbf Q)
=\operatorname{Disc}(M/\mathbf Q)^{[E:M]}
N_{M/\mathbf Q}(\mathfrak d_{E/M})
$$

gives exponent differences

```text
F+/M: (624,496,192,160) - 2(308,248,96,80) = (8,0,0,0)
F0/M: (632,496,192,160) - 2(308,248,96,80) = (16,0,0,0)
F3/M: (624,496,192,160) - 2(308,248,96,80) = (8,0,0,0)
L/M:  (1264,992,384,320) - 4(308,248,96,80) = (32,0,0,0).
```

Thus the target relative norms are $3^8,3^{16},3^8,3^{32}$.

## 9. Relative local identities

Each target table must satisfy, prime by prime:

- sum of relative factor degrees equals $[E:M]$ over each base factor;
- global factor totals are $(36,28,36,56)$ for ToM $140$ and
  $(18,14,18,28)$ for ToM $206$;
- the relative different contributions sum to exponents $8,16,8,32$; and
- every ramified relative row is $(g,2,1,1)$ with $g=1$ or $2$ as displayed.

The tables are data obligations for C60-EXACT-6. This derivation cannot
replace their exhaustive enumeration.

## 10. Scope firewall

`NO_BAD_EULER_OR_ROOT_NUMBER`. The conductor and local calculations above
authorize discriminants and relative local rows only. They do not authorize
decomposition Frobenius, bad Euler factors, epsilon factors, root numbers,
holomorphy, automorphy, or a selected decomposition branch.
