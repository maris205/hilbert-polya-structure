# Proof package: nullity-feedback Jordan powers

Status: mathematical claims pass; paper gate fails.  
Decision: `KILL_INTERNAL_P137_PLUS_ROOT_OWNER`.  
External lifecycle: `HOLD_EXTERNAL`.

## Proposition 1: literal type map and iterate transport

Let `lambda=(lambda_i)` be the Jordan type of a nilpotent matrix `A`.  For
`r>=1`, write `lambda_i=q_i r+s_i`, `0<=s_i<r`.  Then the type of `A^r` is
the union, over `i`, of `s_i` parts `q_i+1` and `r-s_i` parts `q_i`, with
zeros omitted.  Moreover `dim ker A^r=sum_i min(r,lambda_i)`.

**Proof.**  In a basis `e_1,...,e_m` for one block, `J_m^r` sends `e_j` to
`e_(j-r)` when that index is positive and to zero otherwise.  Its chains are
the nonempty congruence classes of indices modulo `r`.  Exactly `s` classes
have length `q+1`, and the others have length `q`.  Kernel dimensions add
over direct sums.  If `K_t` is the accumulated exponent, the next literal
step is `(A^K_t)^(1+dim ker A^K_t)`, proving the exponent recurrence and
`F^t([A])=[A^K_t]` by induction.  QED.

## Proposition 2: recurrence and exact point clock

For `n>=1`, `(1^n)` is the only recurrent state, and

`tau(lambda)=min{t:K_t>=lambda_1}`.

**Proof.**  If a nilpotent `A` is nonzero, it has a block of size at least two.
For every `r>=2`, the image of `A^r` is properly contained in the image of
`A`; hence rank strictly falls.  The literal exponent is always at least two,
so no nonzero state is periodic.  A power `A^K` is zero precisely when `K` is
at least the largest Jordan block.  This proves both statements.  QED.

## Proposition 3: sharp Sylvester clock

Let `s_0=1`, `s_(t+1)=s_t(s_t+1)`.  Then

`max_(lambda|-n) tau(lambda)=min{t:s_t>=n}`,

and the cyclic type `(n)` attains the maximum.

**Proof.**  Before absorption `K_t<lambda_1`.  The largest block alone
contributes `K_t` to `dim ker A^K_t`; therefore
`K_(t+1)>=K_t(K_t+1)`.  Induction gives `K_t>=s_t`, hence the universal
bound.  For `(n)`, while `K_t<n`, the nullity is exactly `K_t`, so equality
holds throughout.  QED.

## Proposition 4: all deepest types and uniqueness boundary

Write `lambda=(L,mu)` with `L>=mu_1`, and define `q_t(mu)` as in the
derivation package.  Then `tau(lambda)>t` exactly when `L>q_t(mu)`.  If
`D=D(n)>=1`, the cyclic type is uniquely deepest exactly for
`n<=2^(2^(D-1))`.

**Proof.**  As long as the orbit is not absorbed by time `j`, the accumulated
exponent is below `L`.  The contribution of the leading block to the nullity
is then the exponent itself, while the tail contributes
`sum_(u in mu) min(q_j,u)`.  This is precisely the recurrence defining
`q_j(mu)`, giving the equivalence by induction.

For a nonempty tail, monotonicity in every tail part shows the smallest value
of `|mu|+q_t(mu)` occurs at `mu=(1)`.  There,
`q_(j+1)=q_j(q_j+2)`, so `q_j+1=(q_(j-1)+1)^2` and
`q_j=2^(2^j)-1`.  A noncyclic deepest type exists exactly when
`n>|mu|+q_(D-1)(mu)` for some nonempty `mu`, equivalently when
`n>2^(2^(D-1))`.  The first witness is `(n-1,1)`.  QED.

## Proposition 5: fixed-exponent image and fibre flow

Fix `r>=2` and restrict to sources with `r-1` blocks.  A target with block
multiplicities `c_j` lies in this image exactly when the finite integer system
(5.1)--(5.4) in `DERIVATION_PACKAGE.md` has a solution.  Its fibre size is
(5.5).

**Proof.**  Separate source blocks below `r` from those written `jr+s` with
`j>=1` and `0<=s<r`.  A small source block contributes only that many singleton
target blocks.  A large block contributes `r-s` copies of `j` and `s` copies
of `j+1`.  Counting the contributions into levels `j` gives (5.1) and (5.2),
and counting/summing small blocks gives (5.3) and (5.4).

Conversely, every feasible solution can be realized by an unordered multiset
of residues at each quotient level and an unordered multiset of small block
sizes.  Replacing a quotient/residue pair by `jr+s` reconstructs one and only
one source partition.  The two multiset generating functions count those
independent choices, proving (5.5).  QED.

## Proposition 6: zero fibre and maximum

The one-step zero fibre has size

`Z_n=[q^n] sum_(ell>=1) q^ell [2ell choose ell]_q`,

and no other target has a larger fibre.

**Proof.**  A source of length `ell` maps to zero iff its largest part is at
most `ell+1`.  Removing one cell from every row gives a partition in an
`ell x ell` rectangle, proving the coefficient formula.  Conjugation sends
every nonterminal source injectively into the terminal set because its new
largest part is `ell` and its new length is the old largest part.  A nonzero
target can receive only nonterminal sources.  Therefore each such fibre has
size at most the number of nonterminal sources, which is at most `Z_n`.  QED.

## Boundary audit

- `n=0`: optional empty class, fixed by convention; excluded from all sums.
- `n=1`: the only type is `(1)`, already zero; depth zero and fibre one.
- `r>lambda_1`: every block powers to singletons; formulas retain no zero
  blocks and still give `(1^n)`.
- `t=0`: `K_0=1`, so the map is the identity and all fibres are singletons.
- `n=5`: `(5)` and `(4,1)` are both deepest, refuting any blanket uniqueness
  claim beyond the boundary in Proposition 4.
- The dynamics and partition formulas are field-independent; literal matrix
  controls over two characteristics guard against an accidental
  characteristic-specific implementation.

## Gate conclusion

These propositions are internally complete, but Propositions 1 and 5 are
fixed-power nilpotent-root theory, and Propositions 2--6 reproduce almost the
same theorem architecture as P137 on the same partition carrier with the same
current-length feedback statistic.  The conditional all-time inverse remains
coefficient extraction.  Thus there is no paper-sized residual after the
required subtraction.

