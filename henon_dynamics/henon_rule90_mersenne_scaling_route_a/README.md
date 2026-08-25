# HCS-C150: Mersenne scaling family for Rule 90

For every `r>=1`, this package studies Rule 90 on the cyclic binary ring of
length `L=2^r-1`.  It proves `a^(L+1)=a` for `a=x+x^(-1)`, identifies the
periodic set with the codimension-one image, proves every state enters that
image in one update, and resolves primitive cycle counts by polynomial gcd
and Möbius inversion.  Exactly half the states are periodic and every cycle
period divides `L`.

The matched length `2^s` family is nilpotent and has only zero periodic.  The
strict verdict is `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_EXPLORATORY`; `route_b_invocation_allowed=false`.  Scope:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
