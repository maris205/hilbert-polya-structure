# C166 narrative report

C166 replaces a weak standalone two-dimensional shear proposal with the full
dyadic Pascal skew tower.  Its headline progress is a uniform theorem: the
dimension contributes an exact clock jump `2^floor(log_2 d)`, every fixed set
is either empty or the whole state space, and every point has the same least
period.  This closes the primitive census, Artin--Mazur zeta, and finite
Koopman determinant at all parameters.

The proof is not a table extrapolation.  It identifies the affine tower with
multiplication by `1+t` in a truncated polynomial ring, reduces fixed points
to divisibility of Pascal coefficients, and uses one explicit
`k=2^(b+1)` coefficient to prove necessity.  The same ring supplies the
involutive substitution `t -> -t/(1+t)`, hence a source-derived antiunitary
time reversal.

Exact finite computations serve only as regression, replay, and mutation
sentinels.  The result is a finite Route-A source theorem with natural
quantization, not a complexity theorem, target determinant match, arithmetic
local construction, or Hilbert--Polya operator.
