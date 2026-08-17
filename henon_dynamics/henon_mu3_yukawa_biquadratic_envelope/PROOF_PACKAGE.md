# HCS-C60 proof package

## Claim

The official project-local machine tuple now certifies C60-EXACT-0 through
C60-EXACT-7 at the prefreeze code/results layer. The independent
formal-documents audit has confirmed the written bridges below without drift;
together these establish the subgroup lattice, primitive generators,
invariant-degree gap, Brauer/zeta identity, absolute and relative
discriminants, and both relative local tables stated in `THEOREM_PACKAGE.md`.

The machine PASS does not by itself authorize a formal theorem claim. The
separate formal PASS now authorizes that claim, but it does not authorize a
paper or C60 release.

Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Status

**`PREFREEZE_CODE_RESULTS_PASS`; `POSTREFRESH_PASS`;
`FORMAL_DOCS_PASS`; `PAPER_PENDING`; `NOT_RELEASED`.**

The machine assumption is discharged by the official independent C60 tuple
and the authorized refresh plus mandatory nonmutating replay. The independent
formal audit has also accepted this proof's mapping from the frozen machine
premises to the written conclusions. The earlier `TARGET_LOCK_FORMAL_INPUT`
layer and target-selection pilots remain historical design input and do not
discharge any theorem premise.

## Official machine-premise binding

The handoff binds the exact `code13 / results8 / live21 / scoped20`
inventories. The refresh transcript records two identical complete cycles of
$53/53$ tests; both execute all eight gates with $9{,}310$ payload scalar
leaves. The checker rejects $9{,}339$ value mutations, $9{,}339$ type
mutations, and $14$ structural mutations ($18{,}692$ certificate mutations
in total). Its actual hostile group/resolver/self-consistent
evidence/additional artifact/total counts are $6/4/10/2/12$, and it performs
$39$ child snapshot rebind checks.

| bound object | SHA-256 |
|---|---|
| canonical payload | `dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead` |
| `results/c60_certificate.json` | `d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518` |
| `results/c60_schema.json` | `c7ddb4ff8fa890f9f801d615158c9038299487affa3808f25fe5d73c987791a5` |
| `results/c60_check_report.json` | `25bc9c1c656da742359814054b66c05e18a304ca85741776c055152a30a98e44` |
| `results/scoped_hash_manifest.json` | `f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7` |
| `results/c60_group_evidence.json` | `dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2` |
| `results/c60_resolvent_evidence.json` | `f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da` |
| official refresh log | `5f5d788a1493c16a8eec86ec0cb40bfed2dea72fa2257bddf50eed1be2c43239` |

This table binds machine premises only. It is not a formal-audit, paper, or
release manifest.

## Assumptions

1. C60-EXACT-0 binds the final released C59 extension, labelled carrier,
   exact subgroups, local filtrations, manifests, Route/archive pair, Batch,
   and guard.
2. C60-EXACT-1 certifies the exact arrays and all finite-group assertions for
   $H_+,H_0,H_3,N,J$, including the exhaustive eleven-bucket uniqueness
   statement.
3. C60-EXACT-2 certifies the three integral carriers, exact stabilizers,
   orbit sizes, and distinct reductions at $p=692717$.
4. C60-EXACT-3 certifies equality of the point and unordered-pair orbit
   partitions of $H_0$ and $N$, and the exact cubic carrier.
5. C60-EXACT-4 certifies the full rational permutation characters and the
   fixed-field input.
6. C60-EXACT-5 certifies the complete orbit-count vectors and exact inherited
   support.
7. C60-EXACT-6 certifies every row and total in both relative local tables.
8. C60-EXACT-7 certifies independence, schemas, mutations, source/scope
   controls, deterministic replay, and promotion discipline.

## Notation

- $K/\mathbf Q$ is the released C59 normal extension and
  $G=\operatorname{Gal}(K/\mathbf Q)=W(E_6)$.
- Left label-map transport is used:
  $H_3=xH_-x^{-1}$ and $\eta_3=x\cdot\eta_-$.
- $N=N_G(H_+)=N_G(H_3)$, $H_0$ is the third index-two subgroup of $N$, and
  $J=H_+\cap H_3=[N,N]$.
- $M=K^N$, $F_i=K^{H_i}$ for $i\in\{+,0,3\}$, and $L=K^J$.
- The line-root scale is denoted $L_0$ when needed, to avoid confusing it
  with the field $L=K^J$; $\alpha_i=L_0d_i$.
- $o_U(H)$ denotes the number of $U$-orbits on $G/H$.

## Proof Strategy

Use Galois correspondence and normalizer/core formulas for the field lattice;
use integral orbit products and a split-prime noncollision witness for
primitivity; use equality of coefficient-orbit partitions for the formal
degree obstruction; inflate the elementary $V_4$ permutation-character
identity and induce it from $N$ to $G$; then apply Artin
conductor-discriminant, signature, discriminant-tower, and double-coset local
formulas.

## Dependency Map

1. The field lattice and automorphism groups depend on C60-EXACT-0/1.
2. The explicit field generators depend on C60-EXACT-0/2 and the integrality
   lemma below.
3. The invariant-degree gap depends on C60-EXACT-3 and is deliberately a
   formal-polynomial statement.
4. The zeta identity depends on C60-EXACT-1/4 and classical Artin formalism.
5. The global arithmetic depends on C60-EXACT-0/5 and the released C58/C59
   filtration formulas.
6. Relative discriminants depend on the absolute discriminants and the
   tower formula.
7. The relative local theorem depends on C60-EXACT-6 and the double-coset
   interpretation; no converse local classification is used.
8. Every theorem-level conclusion additionally depends on C60-EXACT-7's
   authority and scope envelope.

## Proof

### Step 1. Subgroup lattice and field degrees

C60-EXACT-1 gives

$$
|G|=51840,\quad |N|=324,\quad |H_i|=162,\quad |J|=81,
$$

so Galois correspondence gives

$$
[M:\mathbf Q]=160,\quad [F_i:\mathbf Q]=320,\quad [L:\mathbf Q]=640.
$$

Since $J\subset H_i\subset N$, inclusions reverse:

$$
M\subset F_i\subset L.
$$

C60-EXACT-1 also gives $J\triangleleft N$ and $N/J\cong V_4$. Therefore
$L/M$ is Galois with group $V_4$. The three distinct subgroups
$H_i/J\le N/J$ have order $2$, so their fixed fields are exactly the three
quadratic subfields $F_+,F_0,F_3$ of $L/M$.

### Step 2. Normal closures and automorphisms

For a subgroup $H\le G$, the normal closure of $K^H/\mathbf Q$ inside $K$ is
fixed by $\operatorname{Core}_G(H)$. All five relevant cores are trivial by
C60-EXACT-1, so their normal closures are $K$.

For a finite Galois extension, restriction identifies

$$
\operatorname{Aut}_{\mathbf Q}(K^H)\cong N_G(H)/H.
$$

The certified normalizers therefore give

$$
\operatorname{Aut}_{\mathbf Q}(M)=N_G(N)/N=1,
$$

$$
\operatorname{Aut}_{\mathbf Q}(F_i)=N/H_i\cong C_2,
\qquad
\operatorname{Aut}_{\mathbf Q}(L)=N/J\cong V_4.
$$

The element $x\in G$ fixes $\mathbf Q$ and sends $K^{H_-}$ to
$K^{xH_-x^{-1}}=F_3$. Thus $F_3=x(F_-)$ is a $\mathbf Q$-conjugate of the
original C59 minus field. This does not place the original embedded $F_-$
inside this particular $L$.

### Step 3. Integrality and primitivity

Write the released eliminant as

$$
g(t)=L_0t^{27}+b_{26}t^{26}+\cdots+b_0\in\mathbf Z[t].
$$

If $d_i$ is a root and $\alpha_i=L_0d_i$, substituting $t=y/L_0$ and
multiplying by $L_0^{26}$ gives a monic integer polynomial for $y$. Hence
every $\alpha_i$ is integral. The carriers $\mu,\xi_0,\lambda$ are integer
polynomials in the $\alpha_i$, so they are algebraic integers.

Let $\theta$ be one of these carriers and let $H$ be its certified formal
stabilizer. C60-EXACT-2 gives $[G:H]$ pairwise distinct reductions of its
formal conjugates at a common good prime. Equality of two characteristic-zero
integral conjugates would force equality of their reductions, contradicting
that certificate. Thus $\theta$ has at least $[G:H]$ distinct conjugates.
Because $H$ fixes $\theta$, it has at most $[G:H]$ conjugates. Hence

$$
\operatorname{Stab}_G(\theta)=H,
\qquad \mathbf Q(\theta)=K^H.
$$

Applying this to $(\mu,N)$, $(\xi_0,H_0)$, and $(\lambda,J)$ proves

$$
M=\mathbf Q(\mu),\quad F_0=\mathbf Q(\xi_0),\quad
L=\mathbf Q(\lambda).
$$

Each full orbit product is therefore a monic, integral, irreducible,
separable minimal polynomial of degree $160,320,640$, respectively. This is
product-form exactness, not an expanded characteristic-zero coefficient list.

### Step 4. Formal invariant-degree obstruction

Let $R=\mathbf Q[X_1,\ldots,X_{27}]$ with its ordinary commutative
permutation action. A polynomial of degree at most two has a unique expansion
in the basis

$$
1,\quad X_i,\quad X_i^2,\quad X_iX_j\ (i<j).
$$

It is $H_0$-fixed exactly when its linear and square coefficients are constant
on the $H_0$-orbits of points and its mixed coefficients are constant on the
$H_0$-orbits of unordered pairs. C60-EXACT-3 states that these two orbit
partitions equal the corresponding $N$ partitions. Therefore every such
$H_0$-fixed polynomial is $N$-fixed, so no degree-at-most-two formal
polynomial can have stabilizer exactly $H_0$.

The displayed $27$-term cubic orbit sum is $H_0$-fixed, and
C60-EXACT-2/3 certifies that its stabilizer is exactly $H_0$. This proves the
formal quadratic/cubic gap. Evaluation at the actual roots may introduce
relations, so no stronger quotient-ring statement follows.

### Step 5. Exhaustive uniqueness

C60-EXACT-1 replays all $350$ subgroup classes and all eleven collision
buckets. Its exhaustive predicate selects exactly $[301,303]$ among buckets
whose two normalizers are conjugate and have index $2$ over both members.
Therefore the stated index-two common-normalizer property is unique in that
finite table. This does not assert that no other bucket has any generated
$V_4$ quotient; in particular it makes no broader uniqueness claim about
$[112,120]$.

### Step 6. Brauer relation and zeta identity

Write $V=N/J\cong V_4$. Its regular rational character is the sum of the
trivial character and its three nontrivial one-dimensional characters. Each
two-point permutation representation $\mathbf Q[V/(H_i/J)]$ is the sum of
the trivial character and the unique nontrivial character with kernel
$H_i/J$. Consequently, in the rational representation ring of $V$,

$$
[V/1]+2[V/V]=\sum_{i\in\{+,0,3\}}[V/(H_i/J)].
$$

Inflating to $N$ and inducing to $G$ gives

$$
[G/J]+2[G/N]=[G/H_+]+[G/H_0]+[G/H_3].
$$

Artin formalism identifies $\zeta_{K^H}(s)$ with the Artin $L$-function of
$\operatorname{Ind}_H^G\mathbf 1$. Multiplicativity on character sums gives

$$
\zeta_L(s)\zeta_M(s)^2
=\zeta_{F_+}(s)\zeta_{F_0}(s)\zeta_{F_3}(s).
$$

C59 proves that $H_+$ and $H_-$ have equal full permutation characters;
conjugation preserves that character, so $H_+$ and $H_3$ do also. Hence
$\zeta_{F_3}=\zeta_{F_+}$ and the second displayed zeta equality follows.
No bad Euler or root-number computation is used.

### Step 7. Signatures and absolute discriminants

C60-EXACT-5 gives the orbit-count vectors, ordered as
$(I_3,P_3,Q_3,I_5,P_5,C_3,C_2,c_\infty)$:

```text
M:       22,  28,  56,  8,  32,  64,  80,  88
F+,F3:   36,  56, 112, 16,  64, 128, 160, 168
F0:      28,  56, 112, 16,  64, 128, 160, 160
L:       56, 112, 224, 32, 128, 256, 320, 320
```

For a degree-$n$ carrier, the released filtration formulas are

$$
v_3=(n-o_{I_3})+\frac{n-o_{P_3}}2+(n-o_{Q_3}),
$$

$$
v_5=(n-o_{I_5})+\frac34(n-o_{P_5}),\qquad
v_A=n-o_{C_3},\qquad v_B=n-o_{C_2}.
$$

Substitution gives exponents

```text
M       (308,248, 96, 80)
F+,F3   (624,496,192,160)
F0      (632,496,192,160)
L       (1264,992,384,320).
```

If $o_c$ is the number of complex-conjugation orbits, then
$r_1=2o_c-n$ and $r_2=n-o_c$. This yields $(16,72)$, $(16,152)$,
$(0,160)$, and $(0,320)$. Each $r_2$ is even, so every discriminant sign is
positive. C60-EXACT-0/5 binds the inherited exact eight-prime support, giving
the signed formulas in `THEOREM_PACKAGE.md`.

### Step 8. Relative discriminants

For a finite extension $E/M$,

$$
\operatorname{Disc}(E/\mathbf Q)
=\operatorname{Disc}(M/\mathbf Q)^{[E:M]}
N_{M/\mathbf Q}(\mathfrak d_{E/M}).
$$

Subtracting twice the exponent vector of $M$ from those of
$F_+,F_0,F_3$ gives $(8,0,0,0)$, $(16,0,0,0)$, and $(8,0,0,0)$.
Subtracting four times the $M$ vector from that of $L$ gives
$(32,0,0,0)$. Therefore the four relative norms are
$3^8,3^{16},3^8,3^{32}$, and all relative extensions are unramified away
from primes of $M$ above $3$.

### Step 9. Relative local tables

C60-EXACT-6 enumerates the relevant double cosets. For $F=K^H$ and a prime
of $K$ with decomposition group $D$, the primes of $F$ are indexed by
$D\backslash G/H$. Intersections with the decomposition and ramification
filtrations compute the displayed local degrees, ramification indices,
residue degrees, and different exponents. Grouping those factors over the
corresponding primes of $M$ produces exactly the two tables in
`THEOREM_PACKAGE.md`.

All degree, factor, and different totals are certified in both branches. Each
relative ramified row has $e=2,d=1$ over a residue-character-$3$ base, so it
is tame. The proof retains both branches and uses no converse assertion that
$(n,e,f,d)$ classifies an individual high-degree local field.

### Step 10. Authority and scope conclusion

C60-EXACT-7 makes the preceding finite premises project-local, independently
checked, mutation-tested, and manifest-bound. Those machine premises have now
passed. The independent formal-documents audit has confirmed this written
bridge, so Steps 1--9 prove the integrated theorem at the formal-document
layer. The scope leaves and written argument contain no forbidden
Euler/root-number or wider claim.
$\square$

## Corrections or Missing Assumptions

- The wording “C60 proves” is justified at the formal-document layer by the
  combined machine and formal passes; it does not imply paper completion or
  release.
- Pilot hashes remain historical expected values only. The official
  project-local producer and independently implemented checker have now
  reproduced the bound facts without promoting the pilots to authority.
- $F_3$, not the original embedded $F_-$, is the third quadratic subfield of
  this particular $L/M$.
- The uniqueness claim is restricted to the index-two common-normalizer
  predicate; it is not a claim that no other collision yields any $V_4$
  configuration.

## Open Risks

- The official durable transport and carrier serialization agree on the
  inversion and label-action convention; the formal audit confirmed that no
  written formula reverses that convention.
- Formal carrier stabilizers do not by themselves prove stabilizers after
  evaluation; the complete split-prime noncollision certificate is required.
- The formal degree-two argument must cover constants, linear monomials,
  squares, and unordered mixed pairs; an orbit-size list alone is insufficient.
- Both local branches and all tower totals must pass independently.
- Formal proof status is now `FORMAL_DOCS_PASS` after the independent hostile
  audit. Paper and release status remain `PAPER_PENDING / NOT_RELEASED`.
