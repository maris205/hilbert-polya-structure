# Proof spike: product-exchange dynamics on odd class-two groups

**Status:** all-size theorem proved; independent owner/value gate required.  
**External status:** `HOLD_EXTERNAL`.

## 1. Literal system and historical ceiling

Let (G) be a finite group and define

\[
                  \Phi:G^2\longrightarrow G^2,
                  \qquad \Phi(x,y)=(xy,yx).                 \tag{1}
\]

The two coordinates of \(\Phi^t(x,y)\) are the evaluations in \(G\) of the
two length-\(2^t\) Thue--Morse blocks.  This is not a new observation.
Boffa and Point, *Identites de Thue--Morse dans les groupes*, C. R. Acad.
Sci. Paris Ser. I 312 (1991), 667--670, define recursively the identities
\(I_0(x,y):x=y\) and \(I_{t+1}(x,y):I_t(xy,yx)\), and characterize finite
groups satisfying one of them.  The Thue--Morse substitution, these word
identities, and the fact that class-two groups satisfy \(I_2\) receive zero
contribution credit.

The candidate residual is deliberately narrower: the complete pointwise
one-step fibre theorem for every finite group, followed by a full functional
graph, depth, cycle, and *all-iterate fibre* census for every finite
class-two group of odd order.

## 2. One-step image and fibres for an arbitrary finite group

### Theorem 1 (conjugacy fibre theorem)

For \(a,b\in G\),

\[
 |\Phi^{-1}(a,b)|=
 \begin{cases}
 |C_G(a)|,&a\text{ and }b\text{ are conjugate},\\
 0,&\text{otherwise}.
 \end{cases}                                                \tag{2}
\]

Consequently

\[
 \operatorname{im}\Phi
   =\{(a,b):a\sim_G b\},\qquad
 |\operatorname{im}\Phi|=\sum_{K\in\operatorname{Cl}(G)}|K|^2, \tag{3}
\]

where the sum is over conjugacy classes.

**Proof.**  If \(xy=a\), then \(y=x^{-1}a\), and the second equation
\(yx=b\) becomes

\[
                         x^{-1}ax=b.                       \tag{4}
\]

Thus a preimage is uniquely specified by a conjugator \(x\) from \(a\) to
\(b\).  Such conjugators form either the empty set or a coset of
\(C_G(a)\).  This proves (2), and summing the conjugate pairs proves (3).
\(\square\)

This elementary theorem is retained because it is an independent fibre
engine; ordinary conjugacy-class and centralizer facts receive zero credit.

## 3. Uniform two-step collapse in odd class two

Assume from now on that \(G\) has odd order and nilpotency class at most two.
Then every commutator is central.  Put \(a=xy\) and \(b=yx\).  The elements
\(a\) and \(b\) differ by a central commutator, hence commute, and therefore

\[
              \Phi^2(x,y)=(ab,ba)=(r,r),
              \qquad r=(xy)(yx)=xy^2x.                    \tag{5}
\]

The squaring map on a finite odd-order group is a bijection.  Indeed, choose
\(h\) with \(2h\equiv1\pmod{\exp(G)}\); then \(z\mapsto z^h\) is its
two-sided inverse.  Fix \(r\in G\).  For every choice of \(x\), equation
\(xy^2x=r\) has the unique solution whose square is

\[
                         y^2=x^{-1}rx^{-1}.                \tag{6}
\]

Hence every diagonal point has exactly \(|G|\) preimages under \(\Phi^2\).
After (5), the map is simply

\[
                         (g,g)\longmapsto(g^2,g^2).        \tag{7}
\]

Since (7) is a permutation, the same uniform fibre statement persists for
every later iterate.

### Theorem 2 (all iterated fibres)

For every integer \(t\ge2\) and \(a,b\in G\),

\[
 |(\Phi^t)^{-1}(a,b)|=
 \begin{cases}
 |G|,&a=b,\\
 0,&a\ne b.
 \end{cases}                                               \tag{8}
\]

Equations (2) and (8) give every fibre of every positive iterate.  In
particular, the first-iterate centralizer variation disappears completely at
the second iterate.

## 4. Complete transient and recurrent census

The recurrent set is exactly the diagonal

\[
                         \Delta_G=\{(g,g):g\in G\}.        \tag{9}
\]

Indeed every point reaches the diagonal by (5), while (7) permutes it.  A
non-diagonal pair enters the diagonal after one update exactly when
\(xy=yx\).  If \(k(G)\) is the number of conjugacy classes, the classical
commuting-pair identity gives \(|G|k(G)\) ordered commuting pairs.  Thus the
exact depth layers are

\[
\begin{array}{c|c}
\text{depth}&\text{number of states}\\ \hline
0&|G|,\\
1&|G|k(G)-|G|,\\
2&|G|^2-|G|k(G).
\end{array}                                                \tag{10}
\]

The maximum depth is zero for the trivial group, one for a nontrivial
abelian odd group, and two for a nonabelian class-two odd group.  Formula
(10) is a complete all-group layer theorem, not a finite-field fit.

For a recurrent point, its exact period is

\[
                 \operatorname{per}(g,g)
                 =\operatorname{ord}_{\operatorname{ord}(g)}(2). \tag{11}
\]

Consequently, for every \(m\ge1\),

\[
 |\operatorname{Fix}(\Phi^m)|
   =|\{g\in G:g^{,2^m-1}=1\}|,                           \tag{12}
\]

and the Artin--Mazur zeta function is determined exactly by (12).  When
\(G\) has exponent an odd prime \(p\), put \(o=\operatorname{ord}_p(2)\).
Then the cycle Euler product closes to

\[
                   \zeta_\Phi(t)
                   =(1-t)^{-1}(1-t^o)^{-(|G|-1)/o}.        \tag{13}
\]

Power-map orbit facts, multiplicative orders, the commuting-pair identity,
and zeta conversion are zero-credit background.  The residual conjunction is
(2), (8), and (10) for the literal map (1).

## 5. Exact controls and falsification boundary

The standard-library verifier checks the group laws, (2), the literal
two-step collapse, the uniform fibres (8) through the seventh iterate, all
three depth layers, and (12) through the eighth iterate.  It covers

- the nonnilpotent even control \(S_3\) for Theorem 1 only;
- \(C_3\) and \(C_9\);
- Heisenberg groups of orders \(3^3\) and \(5^3\); and
- \(H_3\times C_3\).

It makes **320,848 exact assertions** and stores byte-stable stdout in
`verify_group_product_exchange.out`.  The \(S_3\) control is important:
Theorem 1 survives, while the class-two/odd conclusions are not asserted.
Finite checks do not prove the group-theoretic theorems or ownership.

## 6. Internal collision and owner verdict before hostile review

This map appeared only as the undeveloped matrix-pair reserve C12 in the
current algebraic scout.  It is not the Nielsen map \((x,y)\mapsto(y,xy)\),
the Hurwitz map, P111's positive Heisenberg word-area cocycle, or P119's
fixed-regular commutator map.  Nevertheless, Boffa--Point directly own the
Thue--Morse identity engine, so no manuscript may advertise the word blocks
or two-step equality itself as new.

**Author-side verdict:** `PROVED / SEND TO HOSTILE OWNER-VALUE GATE`.
Promotion requires an independent judgment that the exact all-iterate fibre
collapse and full class-two functional graph remain paper-scale after the
1991 identity theory is assigned zero credit.  Novelty, priority, and
external release remain `HOLD_EXTERNAL`.
