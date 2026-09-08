# Arithmetic continuation scout: no additional admission

Date: 2026-09-07 UTC. This report closes the arithmetic lane's two-candidate
screen in the same C419–C423 batch. It does not change the two previously
admitted contracts, assign C-numbers, or evaluate a paper.

## Decision

| Frozen candidate | Result | Reason for no admission |
|---|---|---|
| ED1: full-image duplication Lattès prime distribution | Short exact joint Haar calculation obtained; bounded residue diagnostic passed | After Bell, finite-layer Chebotarev, open-image methods and the existing local CM work are deducted, the remaining calculation is too small for the required independent paper |
| ED2: all-prime quantitative decay for `x^2-1` | Not closed; neither a proof nor a counterexample obtained | Geometric fixed-point proportion and prime liminf theorems do not supply a uniform quantitative estimate in every arithmetic Frobenius coset |

The lane contributes **0 new admissible papers**. ED1 is not rejected as
false; ED2 is not declared false, novel, or an established open problem.
There is no third candidate. The exact family, native clock, domain,
observable and pre-computation falsifiers are in
[FROZEN_CONTRACTS.md](FROZEN_CONTRACTS.md). Primary-source applicability
and the fresh query record are in [SOURCE_AUDIT.md](SOURCE_AUDIT.md).

## ED1: the residual really is short

For a fixed `E/Q` with image `GL_2(Z_2)`, set

`A(g)=v_2 det(I-g)`, `B(g)=v_2 det(I+g)`,

with `v_2(0)=infinity`. Here `g` is Haar-uniform in `GL_2(Z_2)`.
The screen produced the following rational generating function for finite
valuations, with the exceptional infinite-valuation sets of measure zero:

```text
H(z) = z/(2-z),
D(z) = (3/8)/((1-z/2)(1-z/4)),

J(s,t) = 1/8 + (3/16)(H(s)+H(t))
         + (1/16)(s^2 D(s)+t^2 D(t)) + (3/8)H(s)H(t),

P(s,t) = E[s^A t^B]
       = 1/3 + st/4
         + s^2 t^2/(16(1-s/2)(1-t/2))
         + s^2 t^2 J(s,t)/6.
```

Thus the coefficient of `s^a t^b` specifies the joint mass. No
independence between `A` and `B` is assumed. The following hand derivation
is retained as a screening result, not packaged as an independent paper.

### The three `GL_2(F_2)` types

Two of its six elements have order three. Their lifts have both
determinants odd, contributing `1/3` at `(A,B)=(0,0)`.

Three elements are nonidentity unipotents. Conjugate a representative to
`[[1,1],[0,1]]`. Write a lift as `[[a,b],[c,d]]`, with `a,b,d` odd and
`c` even. Replacing the coordinates `c,d` by trace `tau` and determinant
`delta` has unit Jacobian because `b` is odd. Hence `tau=2T` and
`1+delta=2D_0` give independent uniform `T,D_0` in `Z_2`. The two
determinants are `2(D_0-T)` and `2(D_0+T)`.

With probability `1/2`, `D_0,T` have opposite parity, giving `(1,1)`.
Conditioned on equal parity,

`U=(D_0-T)/2`, `V=(D_0+T)/2`

are independent uniform `Z_2` variables: their inverse is
`D_0=U+V`, `T=V-U`, an isomorphism onto the equal-parity subgroup.
Consequently this branch has `(A,B)=(2+v_2 U,2+v_2 V)`. Multiplying by
the total unipotent weight `1/2` gives the middle two terms of `P`.

The final element is the identity, of weight `1/6`. Its lifts are
`g=I+2M` for uniform `M` in `Mat_2(Z_2)`, so

`(A,B)=(2+v_2 det M, 2+v_2 det(I+M))`.

### The sixteen `Mat_2(F_2)` classes

The following masses are conditional on uniform `M`, not on uniform
invertible `g`:

| Residue type of `M` | Number | Contribution to `J` |
|---|---:|---|
| Characteristic polynomial irreducible over `F_2` | 2 | `1/8` |
| Nonzero nilpotent | 3 | `(3/16)H(s)` |
| Identity plus a nonzero nilpotent | 3 | `(3/16)H(t)` |
| Zero | 1 | `(1/16)s^2 D(s)` |
| Identity | 1 | `(1/16)t^2 D(t)` |
| Rank-one, trace-one idempotent | 6 | `(3/8)H(s)H(t)` |

At a rank-one singular residue, a determinant has a nonzero derivative,
so its lift is uniform in `2Z_2` and its valuation has generating
function `H`. For a trace-one idempotent, the two determinant gradients
are independent modulo 2. For example at `diag(1,0)`, the Jacobian of
`(det M,det(I+M))` in the two diagonal entries has determinant `d-a`,
which is odd. Hensel lifting on that residue ball gives independent
uniform values in `2Z_2`; conjugacy handles the other five residues.

For uniform `N` in `Mat_2(Z_2)`, the common valuation `r` of its first
column has probability `(3/4)4^(-r)`. After factoring `2^r`, an integral
invertible row operation sends the primitive column to `(1,0)`. The
transverse entry of the independent second column remains uniform in
`Z_2`. Therefore

`v_2 det N = r + v_2 W`,

with independent `W` uniform in `Z_2`, giving `D`. In particular,

`[z^j]D(z)=(3/4)(2^(-j)-2^(-2j-1))`, for `j>=0`.

The zero and identity residue branches respectively reduce to `N` and
`I+N`, both uniform. This proves the displayed mixture by these elementary
residue calculations. It also shows directly that the zero-determinant
sets have Haar measure zero. The generating functions normalize at
`H(1)=D(1)=J(1,1)=P(1,1)=1`.

### Why passing to primes does not restore paper-scale content

Write `a_p=p+1-#E(F_p)`. Bell et al., Theorem 1.2, already give the exact
periodic proportion of the degree-four quotient of `[2]`. In particular
it differs from

`(2^(-v_2(p+1-a_p))+2^(-v_2(p+1+a_p)))/2`

by less than `1/(sqrt(p)+1/sqrt(p))` at good odd primes. This input counts
ordinary periodic points on the entire projective line, including
infinity. [Bell et al., arXiv v1, Theorem 1.2](https://arxiv.org/html/2103.00074v1)

For full image, finite-level Chebotarev gives the Haar distribution of
each conjugacy-invariant pair of censored valuations. There is an even
shorter way to control the infinite layer than an additional tail lemma:

`F(g)=(|det(I-g)|_2+|det(I+g)|_2)/2`

is continuous on the compact group, including determinant-zero matrices.
Replacing each valuation by its minimum with `k` approximates `F`
uniformly to within `2^(-k)`. Applying uniform continuity to any continuous
test function on `[0,1]`, followed by fixed-level Chebotarev and then
`k -> infinity`, gives the weak limit `F_*Haar`. Bell's vanishing error
does not change it. These are imported standard steps, not a new
equidistribution theorem or an effective prime-error estimate.

The limit is purely atomic. If `c_ab=[s^a t^b]P`, its mass at a value
`r` is the sum of `c_ab` over all pairs with
`r=(2^(-a)+2^(-b))/2`. In particular:

| Value of the limiting proportion | Mass |
|---|---:|
| `1` | `1/3` |
| `1/2` | `1/4` |
| `1/4` | `1/12` |
| Values strictly between `0` and `1/4`, combined | `1/3` |
| `0` | `0` |

This full distribution is stronger than a mean constant, but the residual
calculation remains only the two small residue decompositions above.
No exact prior occurrence of this particular two-variable expression is
asserted. Its possible absence from a search is not enough for admission.
Lombardo–Perucca already supply general open-image one-eigenspace Haar
algorithms; switching to a list of proper 2-adic images would not fix the
independence problem. See the applicability audit below and
[their Theorems 1–2](https://arpi.unipi.it/retrieve/e0d6c92e-36b5-fcf8-e053-d805fe0aa794/1Eigenspace-second-ArXiv.pdf).

### Single bounded diagnostic receipt

Only [check_joint_mod16.py](check_joint_mod16.py) was executed for new
arithmetic mathematics in this lane. It was run once after the ED1
contract was frozen, using `python3 -B`, on 2026-09-07 at approximately
09:17 UTC. Python reported version 3.12.3 and the process exited 0:

```text
k=1; modulus=2; matrices=6; bins=2; PASS
k=2; modulus=4; matrices=96; bins=3; PASS
k=3; modulus=8; matrices=1536; bins=6; PASS
k=4; modulus=16; matrices=24576; bins=11; PASS
Bounded censored distributions only; no prime limit or novelty certified.
```

SHA-256 of the checked script:

`aeea1f16e1f110e3d94f884d380a11a3e3bb44fd3eba93c5862e74f0c59e797d`.

The direct side enumerates matrix entries and determinant formulas; the
proposed side builds the residue mixture with exact rational arithmetic.
The value `k` means valuation at least `k`, including zero modulo `2^k`.
The checker uses explicit exceptions rather than removable `assert`
statements and writes no files. It is author-side bounded diagnostics,
not an independent review, an infinite-law proof, or a novelty test.
No old CM, C382, M1 or AS2 computation was rerun.

## ED2: the precise missing theorem

The frozen target concerns `b(x)=x^2-1` over `Q` and every sufficiently
large odd prime:

`#Per(b,P^1(F_p))/(p+1) <= C/log(log(p))`,

for absolute effective `C,p0`. Its critical orbit `0 -> -1 -> 0` and
the fixed point at infinity are part of the native system.

For each `n`, let `L_n/Q(t)` be the splitting field of `b^n(x)-t`, set
`A_n=Gal(L_n/Q(t))`, and let `B_n` be the geometric subgroup. For an
arithmetic coset `c B_n`, define `FPP_n(c B_n)` as its fraction of
elements fixing at least one of the `2^n` inverse-tree vertices. A
sufficient missing group estimate for the proposed route is

`sup_(c in A_n/B_n) FPP_n(c B_n) <= C_0/(n+1)`.

That estimate has not been proved here or located with its exact
hypotheses in the inspected sources. It is a proposed sufficient lemma,
not a claimed necessary condition for the target itself. A further
missing step is an explicit Chebotarev/reduction error uniform at a level
`n` comparable to `log log p`, with constants and bad-prime control.
These two gaps must not be compressed into the phrase “by Chebotarev.”

The native forward/inverse connection itself is elementary: every
periodic point belongs to `b^n(P^1(F_p))` for every `n`, by moving
backwards along its finite cycle. Hence the periodic count is at most
the image size. An inverse-tree fixed-point estimate can bound that
image size through a correctly specified arithmetic Frobenius coset;
it is not the same statistic as counting forward periodic points.

The source audit identifies three decisive boundaries:

1. Garton’s effective all-prime theorem requires a critical subset with
   noncolliding iterates and at most one omitted critical point. For
   `b`, both critical points `0` and infinity are periodic. The relevant
   disjointness hypothesis therefore fails; a generic wreath-product
   bound cannot be specialized to this map.
2. The arithmetic Basilica tower has infinite cyclotomic constants.
   Pink identifies the periodic-critical arithmetic quotient via the
   2-adic cyclotomic character. Thus the arithmetic cosets cannot be
   replaced by the geometric subgroup. This obstruction to a proposed
   shortcut is not a counterexample to ED2.
3. Recent geometric fixed-point and prime-liminf conclusions do not
   supply the required all-coset rate. In particular the finite-constant
   hypothesis of Radi’s August 2026 arithmetic corollary is not available.

Exact primary theorem locators and links for these three statements are
in [SOURCE_AUDIT.md](SOURCE_AUDIT.md), entries G1, B1–B2 and F1–F3.

There was no ED2 forward-prime census, inverse-tree computation, or
unfrozen recurrence test. A finite sample cannot decide a bound with
unspecified `C,p0`. The result is **admission rejected for unclosed
substantial proof obligations**, not an invented obstruction theorem and
not a silent weakening to a density-one or liminf statement.

## Scope and handoff

The research-lit / idea-creator source-first process and the local
Route-A substantial-contract gate caused the explicit ED1 replacement
and the ED2 stop at its frozen proof obligations. The ARS source-audit
guidance was used for primary-versus-lead distinctions. This was an
internal team scout, not an external-model review or peer review.

Only this `elliptic_dynamics/` directory was written. No manuscript,
formal evaluation, C-number, global state, old sealed artifact, Git
object, paid API or GPU task was changed or created by this lane.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force: none of this supplies
target Euler factors, root numbers, automorphy, zero correspondence, a
Hilbert–Pólya realization, or Route-B entry authority.
