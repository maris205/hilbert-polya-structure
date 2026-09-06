# A period-five boundary counterexample, not an all-period paper contract

Work throughout over C. Let

`f_i=x_i^6+1-x_{i-1}x_{i+1}`, indices modulo 5,

and `A=C[x_0,...,x_4]/(f_0,...,f_4)`. The admissible observable is the length
of `A[(x_0 x_1 x_2 x_3 x_4)^(-1)]`. The calculation below proves that length
is **6666**, refuting the fitted value **6726**. It does not give all periods.

## 1. Whole algebra and possible zero patterns

The leading monomials of the f_i in a degree order are x_i^6, pairwise coprime.
Thus the f_i form a Gröbner basis and `length A=6^5=7776`.

No two adjacent coordinates can vanish, since their shared equation would
force `1=0`. A zero pattern on a five-cycle has at most two zeros. There are
five possible two-zero sets, all nonadjacent.

At x_0=0, put `x_1=t`, so `t^6=-1`. Then `x_4=1/t`. Put `x_2=u` and
`x_3=v`. The remaining equations are

`t v=1+u^6`,  `u/t=1+v^6`.

Eliminating v gives the monic degree-36 equation

`h_t(u)=(1+u^6)^6-1+u/t=0`.

Since t has six distinct nonzero choices, the quotient `A/(x_0)` has length
216. This assertion includes algebraic multiplicities; h_t is not assumed
squarefree. Cyclic symmetry gives `length A/(x_i)=216` for each i.

For the pattern x_0=x_2=0, all points are

`(0,t,0,1/t,1/t)`,  `t^6=-1`.

The full five-by-five Jacobian determinant there is `-6/t`, hence nonzero.
Consequently every two-zero point is reduced in A. There are six for each of
five nonadjacent zero pairs, hence thirty distinct such points. There are no
three-zero points.

## 2. Where can imposing one zero lose local length?

Fix a boundary point with only x_0=0, and write nearby coordinates
`(a,b,u,v,e)=(x_0,x_1,x_2,x_3,x_4)`.
The defining equations imply

`b^6=a u-1`,  `e^6=a v-1`,  `be=1+a^6`.

Multiplying the first two equations and comparing with the sixth power of
the third gives the exact relation

`a[-(u+v)+a u v-((1+a^6)^6-1)/a]=0`.

The displayed quotient is a polynomial divisible by a^5. If `u+v != 0` at
the boundary point, the bracket is a unit in its local Artin algebra. It
follows that a=0 in that algebra, so imposing x_0=0 changes no local length.
This argument does not require the point or h_t to be reduced.

It remains to study `u+v=0`. Both u and v are nonzero here, since otherwise
adjacent coordinates would vanish. Using v=-u and even degree six in the two
equations from Section 1 gives

`-t u=1+u^6=u/t`.

Hence `t^2=-1`, so t=i or t=-i. For t=i the point has the form

`P_u=(0,i,u,-u,-i)`,  `g(u)=u^6+i u+1=0`.

The t=-i points are its global sign-conjugates, with u replaced by -u.
The polynomial g has six simple nonzero roots; exact gcd with g' is 1.
There are twelve resonance points at the specified zero position and sixty
after cyclic shifts. Each has exactly one zero, so none of these sixty points
is duplicated by this counting.

## 3. Every resonance point has local length two

At P_u the four-by-four Jacobian of `(f_1,f_2,f_3,f_4)` with respect to
`(b,u,v,e)` has determinant

`-36(36u^10+1)`.

It is nonzero at every root of g, as its gcd with g is 1. Thus the formal
implicit-function theorem solves these four coordinates as power series in
a=x_0. Substitute them into f_0 and call the resulting one-variable power
series G(a). Its constant term vanishes, and implicit differentiation gives

`G'(0)=0`,

`G''(0)=2u^2(9u^5-i)/(9(6u^5-i))`.

Neither numerator nor denominator vanishes at a root of g, as certified by
exact gcd arithmetic in Q(i)[u]. Therefore `ord_a G=2`; the completed local
algebra is `C[[a]]/(G)` and has length two. Its quotient by a has length one.
Global negation gives the same result at t=-i.

The accompanying Python certificate independently derives G' and G'' using
the Jacobian/Hessians of the five original polynomial equations, then checks
the displayed expression modulo g. It does not merely assert the formula or
substitute a numerical approximation to a root.

## 4. Total boundary length and the localized count

Summing the five lengths `length A/(x_i)` counts a two-zero reduced point
twice, and a one-zero point once with its imposed-zero local length. Subtract
the thirty two-zero points. By Section 2 this equals the actual boundary
length except at the sixty resonance points. Section 3 adds one at each.
Thus

`boundary length = 5*216 - 30 + 60 = 1110`,

and

`admissible torus length = 7776 - 1110 = 6666`.

For comparison, the recurrence `T_0=2,T_1=k,T_n=k*T_{n-1}-T_{n-2}` gives
`T_5=k^5-5k^3+5k`, hence 6726 at k=6. The small-data parity/period-four
correction vanishes at n=5, so it cannot account for the sixty extra boundary
units of length. This is a counterexample to that proposed all-period fit,
not a claim that all other possible corrections have been classified.

## 5. Explicit limits

All numbers above are scheme lengths. No assertion that the admissible
points are all reduced has been made. No ordinary Artin–Mazur zeta function
or primitive-cycle count is inferred from these lengths. No claim about
periods other than five, or about all k, follows from the resonance check.
The full confinement-stratum classification remains unfinished.
