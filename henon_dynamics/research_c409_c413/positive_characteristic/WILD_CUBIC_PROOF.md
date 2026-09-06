# Wild cubic inverse-image towers in characteristic three

2026-09-06. Scout theorem package, not an admitted C-number or manuscript.
The group below is the classical signature-constrained ternary group `E`
of Benedetto et al./Bouw–Ejder–Karemaker/Ejder. The proposed increment is
its uniform realization by a wild characteristic-three family, including
the geometric ramification and genera. No priority claim is made before
the source audit and independent mathematical review are complete.

## 1. Exact scope and statements

Let `k` be any field of characteristic three, let `a in k*`, and let `t`
be transcendental over `k`. Put

    f(X) = X^3 + a X^2,
    L_n = splitting field of f^n(X)-t over k(t),
    G_n = Gal(L_n/k(t)).

The tree is the genuine inverse-image tree of the generic point `t`.
Height `n` is an inverse-image depth, not a forward periodic-point clock
and not a finite-field extension degree. All covers and all roots in this
document are separable. In particular, neither a purely inseparable
polynomial nor a group endomorphism is substituted for `f`.

Write `W_n=Aut(T_n)` for the full rooted ternary tree automorphism group.
For `g=(g_1,g_2,g_3)sigma` with `n>=2`, define

    sgn_2(g) = sgn(sigma) product_i sgn(g_i|T_1).

Define the already known groups

    E_1 = S_3,
    E_n = (E_(n-1)^3 semidirect S_3) intersect ker(sgn_2).

Equivalently, at every vertex with at least two levels below it, the sign
of the local permutation equals the product of the three children's
local signs. These are constraints on the actual tree action, not only
on the sign of the permutation of all leaves.

### Proposed theorem T1: complete generic tower

For every `k,a,n` as above there is a compatible labelling of the entire
inverse-image tree such that

    G_n = E_n,
    |G_n| = 2^(3^(n-1)) 3^((3^n-1)/2).

Every `L_n/k(t)` is geometrically connected and has constant field `k`.
Consequently, the arithmetic and geometric inverse limits both equal
the classical closed group `E=lim E_n` in this compatible labelling.

The equality is a generic-function-field theorem. It makes no assertion
that every specialized polynomial `f^n(X)-t_0` has group `E_n`.

### Proposed theorem T2: complete geometric branch data and genera

After extending constants to an algebraic closure, the only branch
points of `L_n/k(t)` are `0` and infinity. At every place over zero,

    e_0 = 2^n,    d_0 = 2^n-1.

At every place over infinity,

    e_infinity = 2*3^n,    d_infinity = 3^(n+1)-2.

Here `d` is the different exponent in the normalized valuation upstairs.
The smooth projective curve with function field `L_n` has geometric genus

    g_n = 1 + |E_n|/2 * (1/2 - 1/2^n - 1/3^n).

The first two genera are `g_1=0` and `g_2=46`. Residue degrees over a
non-algebraically-closed constant field are not asserted to be one.

### Proposed theorem T3: exact one-step Kummer and Artin–Schreier ranks

Over algebraically closed constants, let `A_n` be the set of the `3^n`
roots at level `n`, and define

    M_n = L_n( beta_alpha : alpha in A_n ),
    beta_alpha^2 = alpha/a^3.

Then

    [M_n:L_n] = 2^(2*3^(n-1)),
    [L_(n+1):M_n] = 3^(3^n).

The only F_2-relations among the square classes `alpha/a^3` are generated
by the three-element sibling sets. The `3^n` classes `beta_alpha` are
linearly independent in `M_n/{u^3-u : u in M_n}` over F_3. Nevertheless,
at each geometric completion over infinity they span precisely a
one-dimensional Artin–Schreier class space. This global/local distinction
is essential to the induction.

## 2. Elementary cubic normal form

In characteristic three the identity

    f(a(z^2-1)) = a^3(z^3-z)^2                                      (2.1)

holds. If `z^3-z=beta` and `beta^2=alpha/a^3`, the three roots of
`f(X)-alpha` are

    a(z^2-1),    a(z^2+z),    a(z^2-z).                             (2.2)

Indeed, translating `z` by `1` and `-1` permutes these three expressions.
Conversely, their differences recover `z` up to the harmless choices of
ordering and sign. The splitting field of the cubic is thus obtained
by adjoining `beta` and then a root of the Artin–Schreier equation
`z^3-z=beta`. Replacing `beta` by `-beta` gives the same splitting field.

The discriminant and product identities are

    disc_X(f(X)-alpha) = a^3 alpha,
    product_{f(gamma)=alpha} gamma = alpha.                         (2.3)

For example, the resultant computation uses `f'(X)=-aX` and the
degree-three sign in the discriminant. These identities have their exact
constants retained; no square root of `a` is required over the original
field `k`.

For `alpha=t`, (2.1) shows directly that `L_1=k(z)` with
`t=a^3(z^3-z)^2`. The six maps `z -> +/-z+b`, `b in F_3`, give the full
group `S_3`. This proves the starting case, including regularity.

## 3. A genuine all-level signature upper bound

For a vertex `v` with value `x_v`, let `Delta_v` be the Vandermonde of an
ordered list of its three children. Equation (2.3) gives

    Delta_v^2 = a^3 x_v,
    (product_{w child of v} Delta_w)^2 = a^9 x_v.

Therefore the ratio of the product on the second line to `a^3 Delta_v`
is `+1` or `-1`. Choose the ordering of the first-level children once.
Having chosen the orderings through one level, choose the orderings at
the next level so that, for every parent `v`,

    product_{w child of v} Delta_w = a^3 Delta_v.                   (3.1)

This is possible independently for each parent: an odd relabelling of
the children of one of its children changes exactly the required sign.
It does not change any already fixed relation higher in the tree.
Induction gives a single compatible labelling of the infinite tree.

For a Galois automorphism `g`, write `s_v(g)` for its local sign at `v`.
Apply `g` to (3.1) and compare it with (3.1) at `g(v)`. Since `a` is
fixed, this gives

    s_v(g) = product_{w child of v} s_w(g).

Thus `G_n <= E_n` over the original field `k`, for every `n`. This is
stronger than the alternating-leaf discriminant at height two. Nothing
in this argument asserts equality of the groups.

The defining product-sign map is onto: the root transposition with
identity sections has sign `-1`. Consequently

    |E_n| = 3 |E_(n-1)|^3,
    |E_(n+1)|/|E_n| = 2^(2*3^(n-1)) 3^(3^n).                       (3.2)

Also, `E_n` contains the independent copies of `A_3` acting at each
bottom-level parent, trivially elsewhere. All their local signs are
positive, so they satisfy every defining relation.

## 4. Geometric branch support and the zero-place valuations

For Sections 4–7 assume `k` is algebraically closed. The derivative

    (f^n)'(X) = (-a)^n product_{j=0}^{n-1} f^j(X)

shows that every finite branch value of `f^n` is zero, because `f(0)=0`.
The root cover `k(X)/k(t)`, `t=f^n(X)`, is unramified outside zero and
infinity. The same holds for its Galois closure `L_n`.

At zero, `f` has local degree two at `0`, and its other preimage `-a`
has local degree one. A point above zero under `f^n` has ramification
index `2^j`, where `j` is its number of visits to zero before time `n`.
In particular, `X=0` has index `2^n`. All these indices are prime to
three. Local extensions over the algebraically closed residue field
are therefore tame. Their Galois closure has ramification index the
least common multiple of these indices, namely `2^n`.

Fix a normalized place `P` of `L_n` above `t=0`. Thus `v_P(t)=2^n`.
All level-`n` roots are integral at `P`. Exactly `2^n` specialize to zero,
since zero has multiplicity `2^n` in `f^n(X)`. For each such root `alpha`,

    v_P(alpha)=1;                                                 (4.1)

the remaining roots have valuation zero. The vertices specializing to
zero form an embedded binary subtree: each zero vertex has two zero
children and one child specializing to `-a`. In particular, within each
bottom sibling triple the parity vector of (4.1) is either `000` or one
of `110,101,011`.

These facts depend only on the local degrees of the polynomial map and
the already defined Galois closure. They do not use the desired equality
`G_n=E_n`.

## 5. Exact square-class rank using only the previous induction level

Assume the already proved induction hypothesis `G_n=E_n`. Let
`r_n=3^(n-1)` be the number of bottom sibling triples. Define

    V_n = direct sum over sibling triples of
          {(u_1,u_2,u_3) in F_2^3 : u_1+u_2+u_3=0}.

Thus `dim(V_n)=2r_n`. All parity valuation vectors at places over zero
lie in `V_n` by Section 4. In fact, they span `V_n`.

To see this, choose a bottom triple where the parity vector at one place
is a nonzero even vector. Conjugate that place by an independent bottom
`A_3` element, whose existence follows from `G_n=E_n` and Section 3.
Adding the two valuation vectors in F_2 cancels every other triple and
leaves a nonzero even vector on the chosen triple. Its cyclic translates
span the two-dimensional even subspace on that triple. Finally,
`G_n` acts transitively on bottom parents (also immediate from the
irreducibility of `f^(n-1)(X)-t`), so this conclusion holds on each triple.

A relation among the square classes `alpha/a^3` must have even valuation
at every place over zero. Its exponent vector therefore lies in
`V_n^perp`, the span of the all-one vector on each sibling triple.
Every one of these candidate relations really holds: if the parent
value is `eta`, then

    product_{f(alpha)=eta} (alpha/a^3) = eta/a^9
                                    = (beta_eta/a^3)^2.            (5.1)

Here `beta_eta^2=eta/a^3` belongs to `L_n` by the discriminant of the
already split polynomial `f(X)-eta`. This also applies when `n=1` and
`eta=t`. Equation (5.1) retains the constants over the original field.

Thus the relations are exactly the sibling relations, and

    [M_n:L_n]=2^(2r_n).                                           (5.2)

No class is zero, and no two distinct level-`n` roots have the same
class: vectors of weight one or two cannot lie in the span of disjoint
three-element sibling vectors. This distinctness will be needed in the
Artin–Schreier argument.

The use of `E_n` here is not circular. We prove `E_(n+1)` from `E_n`;
we never use an unproved bottom action in the next level.

## 6. Infinity: simultaneous local and global induction

Carry the following additional induction hypothesis:

    e_infinity(L_n/k(t)) = 2*3^n.                                 (6.1)

It holds for `n=1` because the parameterization in Section 2 has a pole
of order six at `z=infinity`.

At a normalized place `Q` of `L_n` over infinity, every level-`n` root
has valuation `-2`. Indeed, `f^n` is monic of degree `3^n`, and comparison
of leading valuations in `f^n(alpha)=t` gives

    3^n v_Q(alpha) = v_Q(t) = -2*3^n.

Each element `alpha/a^3` is therefore a unit times an even power of a
uniformizer. A unit has a square root in the completion, since the
residue field is algebraically closed and the derivative of `X^2-u`
is nonzero at a nonzero residue root. It follows that `M_n/L_n`
**splits completely at every place over infinity**. In particular no
new ramification rescales this normalized valuation.

At a normalized place of `M_n` over infinity we consequently have

    v(beta_alpha)=-1                                             (6.2)

for every `alpha`. Such an element cannot equal `u^3-u` in `M_n`: if
`u` has a pole, the pole order of `u^3-u` is divisible by three, and if
`u` is integral it has no pole. Hence every individual `beta_alpha`
has a nonzero Artin–Schreier class.

### 6.1 Global Artin–Schreier independence

Let `H=Gal(M_n/L_n)`, the elementary abelian two-group determined by
Section 5. For each `alpha`, its square-root line is a character line

    h(beta_alpha)=chi_alpha(h) beta_alpha,    chi_alpha in {+1,-1}.

All these characters are nontrivial and pairwise distinct, by the last
paragraph of Section 5. They remain character lines in the F_3-vector
space `M_n/(Frob-1)M_n`. The order of `H` is invertible in F_3, so the
character projections in `F_3[H]` isolate these lines. Since each
`[beta_alpha]` is nonzero by (6.2), no F_3-linear relation between these
`3^n` classes is possible.

Artin–Schreier theory and the cubic normal form now give

    L_(n+1) = M_n(z_alpha : z_alpha^3-z_alpha=beta_alpha),
    [L_(n+1):M_n] = 3^(3^n).                                    (6.3)

The equality of fields follows both ways from (2.2) and its differences,
not merely from an inclusion of polynomials in a larger splitting field.

### 6.2 Local Artin–Schreier rank at infinity is only one

Fix one completion of `M_n` at infinity. For any two roots `alpha,gamma`,
the leading coefficient of `alpha/gamma` is one: the equations
`f^n(alpha)=f^n(gamma)=t` force its `3^n`-th power to be one in the
residue field, and in characteristic three that equation has the unique
root one. Therefore the leading coefficient of
`beta_alpha/beta_gamma` is `+1` or `-1`.

Subtracting the corresponding signed `beta_gamma` from `beta_alpha`
cancels their only pole. Every resulting difference is integral. In a
complete discretely valued field with algebraically closed residue
field of characteristic three, every integral element is an
Artin–Schreier image: solve its residue equation and apply Hensel's
lemma, whose derivative is `-1`.

Hence the local classes of all the `beta_alpha` are the same up to
sign. They are nonzero by their pole order one. Their local class space
has dimension exactly one, the local extension in (6.3) is totally
ramified of degree three, and

    e_infinity(L_(n+1)/k(t))=3 e_infinity(L_n/k(t))=2*3^(n+1).

This proves (6.1) at the next level. Global independence was not used to
infer local independence; the two ranks are explicitly different.

## 7. Completion of the group induction and descent

Equations (5.2) and (6.3) yield

    [L_(n+1):L_n] = 2^(2*3^(n-1)) 3^(3^n).

This is exactly the order ratio in (3.2). Together with `G_n=E_n` and
the genuine upper bound `G_(n+1)<=E_(n+1)` from Section 3, it proves
`G_(n+1)=E_(n+1)`. Sections 5 and 6 simultaneously establish the next
geometric group and infinity-ramification induction steps. The base
case was proved explicitly, so the result holds at every height.

Now let `k` again be an arbitrary characteristic-three field. The upper
bound of Section 3 was proved over `k` itself, without adjoining any
new constants. After extending to an algebraic closure of `k`, the
degree has just been proved to be `|E_n|`. Geometric degree is at most
arithmetic degree, which is at most `|E_n|`. Thus both are equal.
The base extension does not lower the degree, so the splitting field
is geometrically connected and regular over `k`. Arithmetic and
geometric groups both equal `E_n`, proving T1 and T3.

## 8. Different exponents and genera

The tame zero-place index from Section 4 immediately gives
`d_0=2^n-1`. For infinity, first work in the non-Galois root field
`k(X)`, and put `u=1/X`. The local map is

    h(u)=1/f(1/u)=u^3/(1+au),
    h'(u)=-a u^3/(1+au)^2.

Thus the order of `h'(u)` is three. By the chain rule,

    ord_u((h^n)'(u)) = 3 sum_{j=0}^{n-1} 3^j
                     = 3(3^n-1)/2.                              (8.1)

This is the different exponent of the separable totally ramified
root-field completion over the base completion. The geometric Galois
closure completion has ramification index `2*3^n`, whereas the root
completion has index `3^n`; hence the former has degree two over the
latter. It is tame, with different exponent one. Transitivity of the
different now gives

    d_infinity = 1 + 2*3(3^n-1)/2 = 3^(n+1)-2.

There are no other branch places by Section 4. Riemann–Hurwitz for the
Galois cover of degree `|E_n|` therefore reads

    2g_n-2 = |E_n|[-2+(1-2^(-n))+(3/2-3^(-n))],

which is exactly the genus formula in T2. This proves the proposed
theorem package, subject to independent review of the arguments above.

## 9. Dependency audit and boundaries

The induction is ordered as follows:

1. A field-independent, coherently labelled signature upper bound.
2. The direct height-one parameterization and infinity index six.
3. Local tame zero-place data, available without the next group theorem.
4. Previous-level `E_n` bottom `A_3` actions force the next square rank.
5. Previous-level infinity index makes root valuations `-2`; Kummer
   splitting at infinity then makes square-root valuations `-1`.
6. Distinct Kummer characters imply global AS independence; comparison
   of leading coefficients separately gives local AS rank one.
7. Degree comparison proves the next group, and local rank proves its
   next infinity index. No forward-period census is involved.

Classical inputs are Kummer and Artin–Schreier theory, tame extensions
of geometric discrete valuation fields, Hensel's lemma, the different
chain rule, and Riemann–Hurwitz. The abstract `E_n` groups and their
order formula are already known. The claims to be screened as the
source increment are the characteristic-three realization for every
`a!=0`, the explicit mixed Kummer/AS induction, and its wild geometric
ramification/genus package.

No theorem for characteristic `p>3` is claimed. No finite specialization
surjectivity, forward periodic-point formula, target-prime clock,
Riemann-target divisor, Hilbert–Pólya operator, target Euler product,
functional equation, or root number is constructed. In particular,
`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
