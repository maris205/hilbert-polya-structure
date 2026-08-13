# Narrative Report

Paper09 asks whether Paper08's positive-cone recurrent transfer can acquire
the functional reflection `s <-> 1-s` without invoking an adjoint. SD-C11
uses the most economical symbolic extension: two alternating channels,
carrying `T_s^+` and `T_(1-s)^-`, with independent positive cocycle alphabets.

The construction succeeds analytically at first. It has a nonempty common
Schatten strip, exact holomorphic reflection, recurrent base grammar, and an
all-order identity-word trace rule. It also avoids the immediate
`g g^{-1}` backtracking term that obstructed the adjoint double in Paper08.

The success is too rigid. Every identity-visible pure atom orbit must cross
both layers equally often, so its mass contains matched factors
`p^{-s}p^{-(1-s)}=p^{-1}`. The vertical parameter disappears from every
retained trace and from the regularized determinant. This is not merely a
two-channel accident: a finite-channel reflection-balance theorem proves the
same sterility for all finite monomial channel decorations, including
constant signs and virtual representations.

There is one elementary way to restore motion: identify a reflected edge
label with an inverse. It creates identity-visible two-step words with
frequency `log(p/q)`. But motion occurs only for `p!=q`, precisely when the
word mixes two atoms and violates the prime-power ledger. Thus, inside the
frozen model class, reflection, pure arithmetic visibility, and vertical
motion cannot coexist.

This is a productive scoped failure. SD-C11 gives an exact analytic
determinant and a new no-go theorem, but no moving Euler divisor and no
Route-B object. The next Symbolic-Dynamics-only branch must leave finite
monomial channels, most economically through a source-derived infinite-memory
renewal potential. Before any zero test it must prove nuclearity and exhibit
a nonzero critical-line frequency in a pure-prime coefficient.
