# Theorem package

## Frozen conventions

Let `Phi` be a finite reduced crystallographic root system in a real vector
space, with simple roots `alpha_i`, simple coroots `alpha_i^vee`, Weyl group
`W=<s_i>`, positive roots `Phi^+`, and Cartan convention

```text
A_ij = <alpha_j,alpha_i^vee>.
```

For a dominant weight `lambda`, put
`x_i=<lambda,alpha_i^vee> >= 0`.  Node `i` is legal exactly when `x_i>0`.
Firing it replaces `lambda` by `s_i lambda`, hence

```text
x'_j = x_j - A_{j i} x_i.
```

A word `(i_1,...,i_m)` accumulates on the left as
`w_m=s_{i_m}...s_{i_1}`.  Let `J={i:x_i=0}`, let `W_J` be the standard
parabolic, let `Phi_J^+=Phi^+ intersect span{alpha_j:j in J}`, and let `w_0`
and `w_J` be the longest elements of `W` and `W_J`.

## Main theorem

For every such `Phi` and `lambda`, every legal firing sequence is finite and
every complete sequence has all of the following properties.

1. Its terminal position is the unique anti-dominant member `w_0 lambda` of
   the orbit `W lambda`.
2. Its cumulative element is `w_0w_J`.  This is the unique shortest element
   of the terminal right coset `w_0W_J`; equivalently it is the unique
   maximum-length element among the minimal right-coset representatives
   `W^J`.
3. Its number of moves is
   `ell(w_0w_J)=|Phi^+|-|Phi_J^+|`.

Thus all legal choices strongly converge: endpoint, cumulative element, and
length are independent of the choices.

## Proof

For `w in W`, the coordinate at node `i` of `w lambda` is
`<lambda,w^{-1}alpha_i^vee>`.  A positive coroot is a nonnegative integral
combination of simple coroots.  Therefore its pairing with `lambda` is zero
exactly when its root lies in `Phi_J`.  It follows that firing `i` from
`w lambda` is legal exactly when `w^{-1}alpha_i` is positive and does not lie
in `Phi_J`.  The positivity gives
`ell(s_iw)=ell(w)+1`.

Let

```text
W^J={w in W : w(alpha_j) is positive for every j in J}.
```

This is the set of unique minimum-length representatives of the right cosets
`W/W_J`.  Starting at the identity, the preceding root criterion and the
standard parabolic exchange lemma say exactly that a legal edge
`w -> s_iw` is a length-increasing left weak-order edge that remains in
`W^J`; conversely every such edge is a legal firing edge.  In particular the
accumulated word is reduced and its length is the number of moves.

The finite poset `W^J` has the unique maximum `w_0w_J`.  Equivalently,
`w_0w_J` is the unique minimum-length representative of the coset `w_0W_J`.
A vertex of the quotient game has no legal edge precisely when its weight is
anti-dominant.  Every Weyl orbit meets the closed anti-dominant chamber once,
so the only terminal quotient vertex is `w_0w_J`.  Since each move strictly
increases length in the finite set `W^J`, every play terminates there.

Finally, inversion sets give `ell(w_0)=|Phi^+|` and
`ell(w_J)=|Phi_J^+|`.  Because `w_0w_J` is the minimal representative of
`w_0W_J`,

```text
ell(w_0w_J)=ell(w_0)-ell(w_J)=|Phi^+|-|Phi_J^+|.
```

Also `w_J lambda=lambda`, so the terminal position is
`w_0w_J lambda=w_0lambda`.  This proves all three choice-independent claims.

## Complete boundary atlas

- **Strictly dominant:** `J` is empty, so the cumulative element is `w_0`
  and the length is `|Phi^+|`.
- **Wall position:** arbitrary simultaneous zero coordinates are retained;
  they remove exactly `|Phi_J^+|` moves.  No generic perturbation is used.
- **Zero vector:** `J` is all nodes, `w_0w_J=e`, the terminal is zero, and
  there are no moves.
- **Disconnected system:** `W` and `Phi^+` factor over components.  Component
  games interleave freely, their lengths add, and their terminal positions
  form the product anti-dominant point.
- **Rank-one positive:** in `A1`, `x>0` fires once to `-x`.
- **Rank-one zero:** in `A1`, `x=0` has no legal firing.
- **Strict rule:** a zero coordinate is not legal.  Replacing `>0` by `>=0`
  defines a different and partly vacuous move relation.
- **Scope stop:** the proof uses finiteness, longest elements, and a finite
  quotient.  No affine, indefinite, Kac--Moody, noncrystallographic, or
  arbitrary generalized-Cartan conclusion is claimed.

## Evidence boundary

The exact small-type branch ledger is an independent regression test for
sign, transpose, word-order, wall, product, and rank-one conventions.  The
all-system proof is the weak-order/parabolic argument above; it does not rest
on finite enumeration.
