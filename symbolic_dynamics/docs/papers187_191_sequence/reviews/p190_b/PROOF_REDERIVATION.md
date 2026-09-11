# P190 Review B — proof rederivation

## Status

`PROVABLE AS STATED / C=0 M=0 m=0 / OWNER_AMBER / HOLD_EXTERNAL`

Review B rederived the mathematical package directly from the literal Brandt
update and used the finite verifier only as a separate regression receipt.

## 1. Local filter and all-time form

Let `u=(a,b)` and `v=(c,d)` in `B_n`. The product `uvu` is nonzero exactly
when `b=c` and `d=a`, i.e. exactly when `v=u*`; in that case the value is
`u`. If `u=0` or either equality fails, the output is `0`. Therefore the
literal one-step rule is a filter:

`uvu = u` iff `u != 0` and `v = u*`; otherwise `uvu = 0`.

For a cyclic word `x`, define `g_i(x)=1[x_i != 0 and x_(i+1)=x_i*]`. The
time-`t` formula

`(T^t x)_i = x_i` iff every edge `g_i,...,g_(i+t-1)` is good

follows by induction on `t`. The induction step uses two adjacent survival
windows of length `t`; their union is the length-`t+1` window, and the first
edge of that union supplies the needed inverse relation. This remains valid
after any number of cyclic wraps.

## 2. Recurrence, fixed states, and sharp tails

The all-time formula only retains original letters or sends them to zero, so
support is monotone decreasing. Any recurrent orbit is therefore fixed.
Nonzero fixed words must alternate `u,u*,u,u*,...` around the cycle.

- If `m` is odd, closure forces `u=u*`, so only diagonal units occur: `1+n`
  fixed states including zero.
- If `m` is even, any nonzero unit may start the alternating word: `1+n^2`
  fixed states including zero.

For a non-all-good, nonzero word, let `L` be the longest cyclic run of good
edges. The all-time formula leaves some site nonzero through time `L` and no
site nonzero at time `L+1`, so the tail is exactly `L+1`.

- For `n>=2` and odd `m`, an off-diagonal alternating run with one bad closing
  edge gives `L=m-1`, hence maximal tail `m`.
- For `n>=2` and even `m`, exactly one bad edge is impossible because the
  remaining inverse equalities force the omitted one; two adjacent bad edges
  are attainable, giving maximal tail `m-1`.
- For `n=1`, the only good edge is `ee`; a mixed cyclic binary word has at
  most `m-2` consecutive good edges, so the maximal tail is `max(0,m-1)`.

The short carriers `m=1,2` match these formulas exactly.

## 3. Every-target fibres

For each output letter `y`, define `M_y(u,v)=1[uvu=y]`. Expanding
`tr(M_(y_0)...M_(y_(m-1)))` sums over cyclic source-letter paths
`u_0,...,u_(m-1)` and counts exactly the words whose sitewise outputs equal
the target. That gives the labelled trace formula.

For nonzero `y`, the matrix `M_y` has exactly one nonzero entry, namely at
ordered pair `(y,y*)`. Hence every nonzero target site pins the adjacent
source pair. Between consecutive pinned anchors, only zero targets remain,
and their contribution is the number of literal zero-producing paths across
the gap. Multiplying those independent gap counts yields the complete
anchor-gap fibre product. With no anchor, the fibre is the cyclic zero-path
count `tr(A^m)` for `A=M_0`.

## 4. Zero-target recurrence and image

Write `r=n^2`. Among unit coordinates, the zero-output matrix acts as `-P` on
the coefficient-sum-zero subspace, where `P` is inversion `u -> u*`. Inversion
has `n` fixed diagonal units and `(r-n)/2` transposed two-cycles, so the
`+1/-1` multiplicities of `P` and therefore the `-1/+1` multiplicities of `A`
follow immediately.

On the span of the zero coordinate `e_0` and the all-unit sum `w`,

`A e_0 = e_0 + w`, `A w = r e_0 + (r-1) w`.

That `2 x 2` block has characteristic polynomial `z^2-rz-1`, so its power
sum obeys `s_0=2`, `s_1=r`, `s_k=r s_(k-1)+s_(k-2)`. Adding the remaining
eigenvalue powers yields the all-zero fibre formula in the paper.

Image membership is then read from positivity of the gap counts:

- gap `0`: the next anchor must be the inverse of the previous one;
- gap `1`: the next anchor may be any letter except the same letter;
- gap `>=2`: every entry is positive because paths may go through zero.

## 5. Fibre mass and review boundary

Every ordered source pair has exactly one local output, so `sum_y M_y` is the
all-ones matrix. Summing labelled fibres over all targets gives the entire
carrier size `(n^2+1)^m`.

The review verifier separately checks 26 finite boxes and `1,438,171` exact
assertions. Those computations support regression and boundary pressure only;
they do not replace the proof, and they do not upgrade the bounded owner
search into novelty or release clearance.
