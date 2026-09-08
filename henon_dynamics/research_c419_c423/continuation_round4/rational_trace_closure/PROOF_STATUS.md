# RT3-R4 proof status: full contract remains open

2026-09-08 UTC. Status: `STOP_FULL_CONTRACT_UNCLOSED`.
The calculations below prove failures of two proposed bridges. They do
not disprove the possible exhaustiveness of known rational short-period
families, and they are not a new paper-level theorem.

## 1. Normalization and native clock

Write

\[
\begin{aligned}
s_x(x,y,z)&=(yz+a-x,y,z),\\
s_y(x,y,z)&=(x,xz+a-y,z),\\
s_z(x,y,z)&=(x,y,xy+a-z),\\
R(x,y,z)&=(y,z,x).
\end{aligned}
\]

Then `T_a=R s_x` and, with rightmost map applied first,

\[
T_a^3=s_zs_ys_x.
\]

Indeed the three newly computed coordinates are successively
`x'=yz+a-x`, `y'=zx'+a-y`, `z'=x'y'+a-z`. This also fixes the ordered
word when comparing a group-action theorem. A native period `n` becomes
`n/gcd(n,3)` for the three-step map; they are not interchangeable clocks.

Negating all three coordinates, `(X,Y,Z)=(-x,-y,-z)`, sends the invariant
surface to Jang's normalization

\[
X^2+Y^2+Z^2+XYZ=AX+BY+CZ+D,
\quad A=B=C=-a,\quad D=K_a.
\]

Signs do not change the non-Archimedean valuations. The accepted input
`den(K_a)=q^2`, for full-cycle least common denominator `q`, implies
that at every `p|q` the parameter `D` has negative valuation. No proof or
computational rerun of that input is performed here.

## 2. The exact domain required by the tropical comparison

For a valuation vector `w=(w_1,w_2,w_3)`, Jang's skeleton is characterized
by

\[
w_1+w_2+w_3=\min(2w_1,2w_2,2w_3,
\alpha+w_1,\beta+w_2,\gamma+w_3,d),
\]

where `(alpha,beta,gamma,d)=(v(A),v(B),v(C),v(D))`. His Proposition 3.1
requires membership in `dom(s_i)`, not merely in the skeleton, for
valuation and the tropical Vieta map to commute. Outside that domain
equation (3.5) supplies only a coordinatewise inequality. Theorem A's
conjugacy is consequently not a comparison theorem for every ordinary
point of the surface. These are the actual restrictions in
[Jang v2, §3, Proposition 3.1 and Definition 3.2](https://arxiv.org/pdf/2306.11357v2).

### S challenge: a smooth nonzero rational two-cycle

Use the already-known family

\[
u=1+r,\quad v=1+r^{-1},\quad uv=u+v,
\quad (u,v,u)\ \longleftrightarrow\ (v,u,v)
\]

for `a=0`. It has native period two when `r!=1,-1`. Now set `r=1/q`,
`q>=2`, and let `e=v_p(q)>0`. The two phase valuations are

\[
\eta=(-e,0,-e),\qquad \theta=(0,-e,0).
\]

Here `d=-2e` by the retained square-denominator input. The vector `eta`
belongs to the skeleton: its coordinate sum and the minimum are both
`-2e`. The vector `theta` does not: its sum is `-e`, while the minimum
is `-2e`.

Even at the skeletal phase, the first comparison fails. For `a=0` the
tropical version of `R s_x` gives

\[
\begin{aligned}
\operatorname{trop}(R s_x)(\eta)
 &=R\big(\min(2w_2,2w_3,d)-w_1,w_2,w_3\big)\\
 &=(0,-e,-e)\ne(0,-e,0)
   =v_p\big(T_0(u,v,u)\big).
\end{aligned}
\]

The failure is the actual cancellation `uv-u=u(v-1)=v`: both terms
`uv` and `u` have valuation `-e`, while their difference has valuation
zero. Equivalently, the constant-term formula in the quadratic Vieta
equation has a tie between `z^2` and `D`; the required unique tropical
minimum is absent. The example has no zero coordinates. It is also
smooth: at `(u,v,u)`, the invariant's `x` derivative is
`u(2-v)=u(1-q)!=0`.

Thus the following implication is false:

> A rational periodic point whose valuation is on the skeleton can be
> iterated by the tropical Vieta formula throughout its native orbit.

Shifting the start cannot fix this example: every complete traversal
contains both phases. The source theorem is not contradicted; its domain
condition is violated. Deducting the known two-cycle only removes this
example. It supplies no theorem that all other cancellation-channel
cycles lie in known curves. That is exactly the missing part of route S.

## 3. Primewise good phases need not synchronize

Use the frozen challenge `r=2/3` in the same known family:

\[
P=(5/3,5/2,5/3),\qquad Q=(5/2,5/3,5/2).
\]

The identity `uv=u+v` proves `T_0(P)=Q` and `T_0(Q)=P`, and `P!=Q`
proves native period two. Their valuations at the denominator primes are

| Prime | `v_p(P)` | `v_p(Q)` | Phase with integral first and third coordinates |
|---|---|---|---|
| `2` | `(0,-1,0)` | `(-1,0,-1)` | `P` |
| `3` | `(-1,0,-1)` | `(0,-1,0)` | `Q` |

At every other prime both scalar coordinates are locally integral.
Hence at each prime there is a phase with two integral neighbours around
the middle coordinate. Nevertheless **no phase has even one rational
integer coordinate**. In symbols, this example separates

\[
\forall p\ \exists i:\ x_i,x_{i+2}\in\mathbb Z_p
\quad\text{from}\quad
\exists i\ \forall p:\ x_i,x_{i+2}\in\mathbb Z_p.
\]

The phenomenon is not specific to small primes: if positive coprime
integers `s,t>1` are used in `r=s/t`, then `u=(s+t)/t` and `v=(s+t)/s`
have respective reduced denominators `t` and `s`. The two denominator
supports control opposite phases. This is a parametrization of a known
curve, not a new periodic family or a new classification theorem.

Route D therefore needs an actual simultaneous residue/denominator
relation. Primewise maximum bounds alone do not justify a global
integer pivot or a denominator-independent central alphabet. We have
not proved such a relation after deducting the known short curves.

## 4. Other current non-Archimedean theorems do not supply the bridge

[Cantat--Jang, Theorem A and §8](https://arxiv.org/html/2410.08579v1)
concern group orbit closures, and the Markov application assumes all
four surface parameters are in the valuation ring. At a denominator
prime of the remaining RT3 problem, `D=K_a` is nonintegral. Moreover the
cyclic group generated by one loxodromic map does not satisfy Theorem A's
requirement of an infinite-order non-loxodromic element. Enlarging the
group changes the periodicity question.

[Jang's residual-transitivity Theorem 1](https://arxiv.org/pdf/2502.18976v1)
assumes `p>3`, `D in Z_p` with specific congruence conditions, and a
transitive full automorphism-group action on the nonsingular reduction.
It establishes full-group minimality on the corresponding integral
locus, not rational ordinary native periods at nonintegral levels.

## 5. What remains unproved and why this round stops

No all-denominator exceptional-channel classification has been proved.
No finite complete list of nonintegral rational native periods or loci
has been obtained. We have not shown that such a list cannot exist.
Neither local counterexample lies outside the known short families;
therefore neither is evidence against their possible global completeness.

The new diagnostic content is precise: even *skeletal membership* does
not authorize the valuation comparison, and even primewise phases with
integral neighbours do not give a common global phase. The next genuine
lemma would have to control the missing cancellation residues across
the whole cyclic word and all denominator primes. Naming this lemma is
not proving it.

No mathematical CPU run was performed: no rational-height box, no
denominator/period table, no periodic-ideal enumeration, and no old
IR1 or RT3 validation was rerun. Recommendation: retain these bridge
failures in the continuation record, with **zero new admissions**.
