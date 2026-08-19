# C74 theorem package

## Theorem 1: finite affine group

Put `P=Z/9+Z/3`. Every endomorphism of `P` has the form

\[
(x,y)\longmapsto (ax+3by\bmod 9,\;cx+dy\bmod 3),
\]

with `a` in `Z/9` and `b,c,d` in `Z/3`. There are 243 such odd-part matrices;
the two endomorphisms of the `Z/2` factor give 486 endomorphisms of `Q`. A
full endomorphism is an automorphism exactly when its dyadic component is the
identity and `a` and `d` are nonzero modulo 3. Hence

\[
|\operatorname{Aut}(Q)|=6\cdot3\cdot3\cdot2=108,
\qquad |\operatorname{Aff}(Q)|=54\cdot108=5832.
\]

## Theorem 2: named-coordinate rigidity

Let `M` be the 16-occurrence C72 named multiset and `X` its 10-point support.
The affine stabilizers are both trivial:

\[
\operatorname{Stab}_{\operatorname{Aff}(Q)}(M)=1,
\qquad
\operatorname{Stab}_{\operatorname{Aff}(Q)}(X)=1.
\]

The linear stabilizers are also trivial. Consequently the affine orbit of
either named object has size 5832, while its linear orbit has size 108.

For `M`, the unique multiplicity-five point is zero, so a stabilizing
translation vanishes. The unique nonzero point in `M\cap3P` is `(6,0,0)`,
which gives `a=1 mod 3`. The multiplicity-two pair `(0,1,0),(3,1,0)` first
gives `d=1` and `b in {0,1}`; `b=1` sends the second point to first
coordinate 6, outside the pair, so `b=0`. The remaining order-nine points
force `a=1,c=0`.

For `X`, the unique point with nonzero dyadic coordinate first forces the
dyadic translation to vanish. Write the affine map as `phi(q)=Aq+t`. The sum
of its ten distinct points is `(0,0,1)`. Every automorphism fixes the unique
order-two element, so preservation of the set gives the explicit affine sum
identity

```text
(0,0,1) = sum_{q in X} phi(q)
         = A(sum_{q in X} q) + 10 t
         = A(0,0,1) + 10 t
         = (0,0,1) + 10 t.
```

Hence `10t=0` in the odd factors (the dyadic component was already shown to
vanish). Because `10` is one modulo both 9 and 3, the odd translation
vanishes as well. The order-nine reductions
`T={(1,0),(1,2),(2,1),(2,2)}` modulo 3 force `c=0,d=1`, and the remaining
representatives force `a=1,b=0`.

## Theorem 3: exact rigidity margin

With

\[
O(\varphi)=\sum_{q\in Q}\min(m_M(q),m_{\varphi(M)}(q)),
\]

the complete affine overlap histogram is recorded in the evidence. Its unique
value 16 is the identity; the largest nonidentity value is 14, attained by

\[
(x,y,z)\mapsto(4x,2x+y,z),
\qquad
(x,y,z)\mapsto(7x,x+y,z).
\]

Their distinct-point overlap is 8. The underlying-set histogram is recorded
separately and must not be substituted for `O`.

## Symmetry boundary

C73's abstract 16-vertex generation hypergraph has automorphism order
`345600`, but C74 proves that no nonidentity affine map of the actual named
core realization permutes its named points. The duplicate-label fiber
`5!*2!*2!=480` is bookkeeping after the point map is fixed, not an affine
stabilizer. No full Burnside ring, arithmetic or local result, Euler factor,
root number, automorphy, or Hilbert--Polya claim is made.
