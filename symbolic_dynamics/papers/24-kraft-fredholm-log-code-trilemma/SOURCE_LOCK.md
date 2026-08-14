# Source Lock — SD-C26

**Freeze date:** 2026-08-14  
**Primary family:** Symbolic Dynamics  
**Authority object:** positive scalar stationary graph grammars with a finite
orbit-separating local code and an intrinsic additive roof  
**Target-zero data:** forbidden and unused  
**Route-B invocation:** forbidden  
**Review loop:** excluded by instruction

## 1. Source skeleton

For an (n)-letter alphabet (A_n), let (F_n=A_n^{\mathbb Z}), up to
topological conjugacy.  Freeze

\[
 F_m\boxtimes F_n:=F_{A_m\times A_n}\cong F_{mn},\qquad
 F_m\boxplus F_n:=F_{A_m\sqcup A_n}\cong F_{m+n},
\]

\[
 S(F_n)=F_n\boxplus F_1\cong F_{n+1},\qquad h(F_n)=\log n.
\]

Here (\boxplus) means alphabet disjoint union followed by the full-shift
functor; it is not a categorical-coproduct claim.  Rational primes are the
multiplicative atoms of this frozen positive-integer skeleton.  No prime
table, target Euler coefficient, or Riemann-zero table is admissible in a
graph, code, roof, or weight.

## 2. Stationary graph and finite local code

Let (G=(V,E)) be a fixed countable simple directed graph and (X_G^+) its
one-sided edge shift.  A primitive orbit is a directed closed edge word,
modulo cyclic rotation, which is not a positive temporal power of a shorter
closed word.  Reflections are not identified.

Fix a finite alphabet (\mathcal A), (b=|\mathcal A|\ge2), and a one-edge
code

\[
        \lambda:E\longrightarrow\mathcal A.
\]

A finite-radius local code is included by passing to its finite higher-block
alphabet.  For (\gamma=e_0\cdots e_{\ell-1}), put

\[
 \Lambda(\gamma)
 =[\lambda(e_0)\cdots\lambda(e_{\ell-1})]_{\rm cyc}.
\]

The code is **prime-orbit separating** when

\[
        \Lambda(\gamma_p)=\Lambda(\gamma_q)\Longrightarrow p=q.
\]

If this condition is dropped, a hidden countable vertex label can store an
arbitrary atom inventory.  Such a model belongs to the arbitrary-inventory
control, not to the finite local arithmetic-code class.

## 3. Positive one-step operator

Let (\tau:E\to[0,\infty)) be fixed.  For real (\sigma>0), define on the
natural counting space (\ell^2(V))

\[
 L_\sigma e_u
 =\sum_{e:u\to v}e^{-\sigma\tau(e)}e_v.
\]

The graph is simple and the coefficients are positive.  If this rule is not
bounded, the compactness/Fredholm gate has already failed.  If it is bounded,
compactness is tested on this same vertex space.  The theorem also applies to
positive edge weights (a_\sigma(e)) when the orbit product, rather than a
roof decomposition, is frozen.

## 4. Literal connected prime ledger

The invariant is the connected primitive ledger

\[
 -\log D_G(s,z)
 =\sum_{[\gamma]\ {\mathrm{primitive}}}\sum_{r\ge1}
   \frac{z^{r|\gamma|}}{r}e^{-srT(\gamma)}.
\]

The strongest positive scalar A1 hypothesis is frozen for a no-go test:

1. every rational prime (p) labels exactly one primitive orbit
   (\gamma_p);
2. these are all primitive directed orbits of (G); and
3. the additive roof is intrinsic and obeys
   (T(\gamma_p)=\sum_{e\in\gamma_p}\tau(e)=\log p).

Thus repetition gives (T(\gamma_p^r)=r\log p=\log p^r).  This is a
best-case compatibility hypothesis, not an assertion that the graph exists.
Where a trace-class determinant exists, it would give

\[
 -\log D_G(s,z)
 =\sum_p\sum_{r\ge1}\frac{z^{r\ell(p)}}r p^{-rs},
 \qquad \ell(p)=|\gamma_p|.
\]

The graph-step marker is deliberately retained.  This differs from the
standard marked target

\[
 -\log D_{\mathbb P}(s,z)
 =\sum_p\sum_{r\ge1}\frac{z^r}{r}p^{-rs}.
\]

## 5. Frozen candidate families

Three families must be audited before the positive branch may close.

1. **Binary/Euclidean tableau:** binary digits plus local
   equality/addition/multiplication/remainder witnesses, closed into
   recurrent computations.
2. **Factorization/renewal grammar:** source-derived relations (n=ab),
   with temporal concatenation proposed as multiplicative composition.
3. **S-adic stationarization:** a finite-alphabet directive system made
   stationary by adjoining explicit level/directive states.

For each family the first gates are: primitive-orbit ledger, arbitrary-
inventory controls, graph-step marker, and whole-operator compactness or
nuclearity.  Analytic continuation is inadmissible until those gates pass.

## 6. Allowed information and forbidden repairs

Allowed source information consists of the full-shift semiring relation,
finite binary digits, local equality/addition/multiplication witnesses,
Euclidean or factorization relations expanded into states, and stationary
edge rules fixed independently of a cutoff.

Forbidden repairs are a prime table; prime-aware allowed-word list; target-
aware terminal return; target coefficient placed in the roof; target-zero
data; a dimension or alphabet silently growing with cutoff; or an induced
return marker presented as the original graph-step marker.

Mandatory controls are primes, squares, Fibonacci membership, matched-
density seeded random and hash inventories, and arbitrary decidable
inventories under any countable-state compiler.

## 7. Theorem scope

SD-C26 freezes the following class and no larger one:

- stationary simple countable directed graphs;
- positive scalar one-step weights;
- an additive edge roof with total (\log p) on each intended prime orbit;
- a finite local code which visibly separates the prime orbits;
- the natural counting-measure vertex adjacency.

Signed or matrix-valued cancellation, genuinely infinite local alphabets,
nonlocal completed-orbit weights, quotient operators, and anisotropic
function spaces are outside the theorem.  They are explicit escape
obligations, not conclusions silently ruled out by positivity.

## 8. Route lock

The frozen evaluation tuple is

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)
```

The candidate is evaluated `ROUTE_A_REJECTED`; Route B remains locked.  No
functional equation, critical-line mechanism, RH implication, or
Hilbert--Pólya operator is claimed.
