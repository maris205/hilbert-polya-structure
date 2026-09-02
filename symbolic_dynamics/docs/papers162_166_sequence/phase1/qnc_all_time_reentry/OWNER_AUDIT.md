# Fresh specialist owner audit — QNC all-time re-entry

**Search date:** 2026-09-03 UTC  
**Gate:** `KILL` after owner subtraction  
**External status:** `HOLD_EXTERNAL`

## 1. Search method and limitation

The search began from four aliases of the literal map:

```text
x -> x(x+p) on pZ/p^eZ
u -> p u(u+1) on Z/p^(e-1)Z
y -> y^2 + p(2-p)/4 on p/2+pZ_p
z -> 1+(p/2)(z^2-1)
```

It then expanded to mechanism queries for critical residue-class fibres,
iterated quadratic congruences modulo prime powers, attracting fixed-point
linearization, Schroeder equations, iterative logarithms, and finite
reductions of p-adic conjugacies.  Primary arXiv records, author manuscripts,
publisher/institutional records, and full text were preferred.  Search-result
snippets were discovery aids, not evidence.

Representative queries included:

```text
"x(x+p)" iteration modulo "p^n"
"x^2+px" dynamics p-adic
iterated polynomial congruence modulo prime powers preimages
critical residue class second derivative fibre polynomial mod p^n
p-adic attracting fixed point linearization iterative logarithm
"On hyperbolic fixed points in ultrametric dynamics"
quadratic polynomial local field conjugacy
```

No source was found that prints the exact `B_t` target permutation for this
literal finite system.  That is a bounded, English-heavy non-hit, not a
novelty, priority, ownership, or freedom-to-operate claim.  It does not rescue
the candidate because the two surrounding theorem axes have direct general
owners.

## 2. Decisive source: critical-residue fibre spectrum

David L. desJardins and Michael E. Zieve,
[*On the Structure of Polynomial Mappings Modulo an Odd Prime Power*
(`Polynomial Mappings mod p^n`)](https://arxiv.org/abs/math/0103046),
arXiv:math/0103046 (manuscript dated 1994, arXiv posting 2001).

Section 6.4, “Tails,” was checked in full text.  For a polynomial on a
residue class above a mod-`p` cycle, with derivative zero and second
derivative nonzero modulo odd `p`, it states that positive fibres have sizes
`p^j` or `2p^j`; more precisely, for `1<=j<n/2`, there are

```text
(p-1)p^(n-2j-1)/2
```

fibres of size `2p^j`, plus one fibre of size `p^floor(n/2)`.

For every fixed QNC time `t`, the normalized polynomial on the remaining
precision is

```text
P_t(u)=B_t(u(u+1)) mod p^k,       k=e-t-1.
```

Modulo `p`, every factor of `B_t` is the identity.  Thus `P_t mod p` is
`u(u+1)`, with one critical source class of unit second derivative; all other
source classes are nonsingular and are bijective onto their lifted target
classes by the preceding argument in the same section.  More transparently,
compare with one-step QNC at precision `p^(k+2)`.  Its fibre formula is
`p rho_{p^k}(1+4a)`, while the time-`t` formula is
`p^t rho_{p^k}(1+4a)` after the target relabelling `a=B_t^(-1)(b)`.  Hence the
latter spectrum is exactly the cited, already-owned one-step spectrum with
each source repeated `p^(t-1)` times.  It becomes:

```text
fibre 2p^(t+r), multiplicity (p-1)p^(k-2r-1)/2,
one fibre p^(t+floor(k/2)).
```

Therefore the proposed **coordinate-free all-time positive-fibre spectrum is
directly compressed at every time**, even though the source does not name
`B_t` or label which QNC target carries which fibre.  Image size, maximum
fibre, and zero-fibre count are immediate consequences and receive zero
credit.

## 3. Decisive source: attracting Koenigs conjugacy

Karl-Olof Lindahl and Michael Zieve,
[*On Hyperbolic Fixed Points in Ultrametric
Dynamics*](https://arxiv.org/abs/1111.2000), *p-Adic Numbers, Ultrametric
Analysis and Applications* 2 (2010), 232--240,
[DOI 10.1134/S2070046610030052](https://doi.org/10.1134/S2070046610030052).

Theorem 3.1 treats a power series

```text
f(x)=lambda x + higher terms,       0<|lambda|<1,
```

and gives a normalized `g` satisfying `g o f=lambda g`; full conjugacy holds
on `|x|<|lambda|rho`.  The paper explicitly notes for
`f(x)=lambda x+a_2x^2` that the full-conjugacy radius is
`|lambda|/|a_2|`.

For QNC over `Q_p`, `lambda=p`, `a_2=1`, and `rho=1`.  The theorem's full
conjugacy disc is therefore

```text
|x|_p<|p|_p  <=>  x in p^2 Z_p,
```

exactly the proposed inner ball.  The other root `-p` lies on the boundary,
so this radius is also sharp for full conjugacy.

The paper's Remark 2 identifies the standard attracting construction as the
iterative logarithm `g=lim_n f^n/lambda^n`, citing prior p-adic work.  For
this literal polynomial,

```text
F^n(x)/p^n = x product_{j=0}^{n-1}(1+F^j(x)/p),
```

so the proposed product is precisely that construction.  Reducing the
conjugacy modulo `p^e` yields the finite chart; the image balls and uniform
fibres are the elementary fibres of multiplication by `p^t`.  The explicit
valuation proof of isometry is valid but does not create a new independent
axis.

Earlier primary records confirming that this is established machinery are:

* Jonathan Lubin,
  [*Nonarchimedean Dynamical Systems*](https://www.numdam.org/item/CM_1994__94_3_321_0/),
  *Compositio Mathematica* 94 (1994), 321--346;
* Juan Rivera-Letelier,
  [*Dynamique des fonctions rationnelles sur des corps
  locaux*](https://numdam.org/item/AST_2003__287__147_0/),
  *Astérisque* 287 (2003), 147--230.

Lindahl--Zieve is the decisive source because it states the needed full-disc
bound and directly specializes to the QNC inner ball.

## 4. Direct arithmetic input

Steve Wright,
[*On the Quadratic Formula Modulo N*](https://arxiv.org/abs/1507.07513),
arXiv:1507.07513; *Journal of Algebra, Number Theory and Applications* 7
(2007), 33--68.

This is direct background for completing a quadratic congruence to its
discriminant and for the prime-power square-root census.  It owns the
arithmetic labels `rho_{p^k}(Delta)`.  The new calculation correctly inserts
the transported coordinate `Delta=1+4B_t^(-1)(b)`, but the root-count engine
itself is zero credit.

## 5. Nearest and false-positive sources

* Ashish Dwivedi, Rajat Mittal, and Nitin Saxena,
  [*Counting Basic-Irreducible Factors mod p^k in Deterministic Poly-time and
  p-adic Applications*](https://arxiv.org/abs/1902.07785), explicitly uses
  `x^2+px mod p^2` as an example.  Its subject is factor/root counting, not
  iteration.  This is an exact-polynomial string hit but **not** the
  dynamical owner.
* Robert Benedetto, Jean-Yves Briend, and Herve Perdry,
  [*Dynamique des polynomes quadratiques sur les corps
  locaux*](https://doi.org/10.5802/jtnb.589), *Journal de Theorie des Nombres
  de Bordeaux* 19 (2007), 325--336, classifies broad local-field quadratic
  dynamics.  It is contextual, not the source of the finite target atlas.
* Aihua Fan and Lingmin Liao,
  [*On Minimal Decomposition of p-adic Polynomial Dynamical
  Systems*](https://arxiv.org/abs/1010.5583), supplies broader cycle-lifting
  and growing-tail context and points back to desJardins--Zieve for the
  odd-prime finite-level mechanism.  It is reinforcing background, not a
  rescue axis.

## 6. Mandatory subtraction and residual

| claimed material | source disposition | credit |
|---|---|---:|
| derivative-zero attracting tail on the lifted zero class | desJardins--Zieve | zero |
| positive fibre sizes and multiplicities of every normalized `P_t` | desJardins--Zieve direct specialization | zero |
| image size, maximum fibre, zero-target complement count | corollaries of the owned spectrum | zero |
| discriminant completion and `rho_{p^k}` census | Wright / classical arithmetic | zero |
| existence and full-conjugacy radius on `p^2 Z_p` | Lindahl--Zieve Theorem 3.1 | zero |
| iterative-logarithm/product construction | standard construction recorded by Lindahl--Zieve; literal factorization | zero |
| finite uniform inner-ball fibres | reduction of conjugacy to multiplication by `p^t` | zero |
| explicit all-time target transport `B_t^(-1)` | no verbatim owner located in bounded search | residual |

The last line is useful but is one elementary finite-coordinate refinement,
not a second paper-scale theorem.  It cannot satisfy the P162--P166 progress
threshold on its own.

**Owner-gate verdict: `KILL`.**  Formula correctness is preserved in the
internal theorem record; no external novelty claim follows, and the status
remains `HOLD_EXTERNAL`.
