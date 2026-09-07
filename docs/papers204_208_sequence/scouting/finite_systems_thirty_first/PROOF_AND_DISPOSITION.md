# TCF: complete temporal subtraction, not a candidate gate

Author: `/root/thirty_first_finite_scout`; `HOLD_EXTERNAL`.
Status of the identities and finite deduction below: **PROVABLE AS STATED**.
Research disposition: **KILL_VALUE_TEMPORAL_CAPTIVE_BALLISTIC_WRAPPER**.

## Claim, assumptions and dependency map

Use exactly the TCF map on $X_n$, $n\ge1$, in `INTAKE.md`.
No experiment is a premise. The proof dependencies are:

1. The three local colour cases identify a commuting global-colour rotation
   times a one-sided captive rule.
2. Signed differences give an exact two-speed annihilation factor; an anchor
   colour makes this a bijective representation of the entire original carrier.
3. An even-site embedding and moving spatial frame identify that particle
   rule with the previously rejected BA literal, not merely its terminology.
4. The old survivor argument supplies recurrence and the finite clock;
   the remaining colour motion is an explicit commuting permutation.

The primary comparison is Hellouin de Menibus–Sablik, §2.6.3, local
one-sided captive update and its speed-$(-1,0)$ interface representation.
Its measure-theoretic Proposition 4 is NOT invoked as a finite-ring sharp
clock theorem. The finite deduction is written out below and is deducted
through the actual older BA proof at
`docs/papers204_208_sequence/scouting/combinatorial_second/PROOF_NOTES.md`,
BA subsection. This is source/mechanism subtraction, not a new temporal
contribution or a claim of global prior ownership of every possible fibre law.

## 1. Exact co-rotating rule

Let $R(x)_i=x_i+1\pmod3$ be global colour rotation, and let

$$C(x)_i=x_i+\mathbf1\{x_{i+1}=x_i+1\pmod3\}\pmod3.$$

If $b=a$, then $RC(a,b)=a+1$. If $b=a+1$, the missing colour is
$a+2=RC(a,b)$. If $b=a-1$, the missing colour is $a+1=RC(a,b)$.
These three cases exhaust the ordered pairs. Thus

$$T=RC=CR,\qquad T^t=R^tC^t\quad(t\ge0).$$

The equality test defining $C$ is unchanged by a simultaneous colour
rotation, proving the commutation. In particular $C(a,b)$ is either
$a$ or $b$: it is exactly a one-sided captive rule with neighbourhood
$\{0,1\}$. This is an autonomous commuting-frame identity, not a claim
that an arbitrary time-dependent change of colours gives a conjugacy.

## 2. Whole-carrier signed differences and anchor

Let $d_i$ be the unique member of $\{-1,0,1\}$ congruent to
$x_{i+1}-x_i$ modulo three; put $e_i=\mathbf1\{d_i=1\}$.
The map

$$x\longleftrightarrow(a,d),\qquad a=x_0,\qquad
\sum_{i=0}^{n-1}d_i\equiv0\pmod3$$

is bijective, with inverse
$x_i=a+\sum_{j=0}^{i-1}d_j\pmod3$. The congruence is exactly the cyclic
closing condition. Hence no source-label information is silently discarded.
The update becomes

$$a'=a+1+e_0\pmod3,\qquad d_i'=d_i+e_{i+1}-e_i.$$

The right-hand difference already lies in $\{-1,0,1\}$ as an integer:
for $d_i=-1,0,1$ it is respectively $-1+e_{i+1}$,
$e_{i+1}$, $e_{i+1}$. Call this difference update $P$.
It conserves the integer sum of the differences and therefore its required
modulo-three constraint. In particle terms:

- a $+1$ particle moves one site to the left;
- a $-1$ particle stays at its site;
- an incoming $+1$ and a stationary $-1$ annihilate together.

No other creation, collision or waiting is present. The displayed integer
formula verifies every local case, including adjacent equal signs.

## 3. Literal adapter to the old BA rule

Let $B$ be the old BA map on the ring $\mathbb Z/(2n)$: signs
$\{-1,+1\}$ move at their signed velocities, and opposite continuous
paths annihilate on crossing or common landing, as in the original BA
definition. Let $S$ translate every particle one site to the right.
Embed a difference state using only even sites:

$$E(d)_{2i}=-d_i,\qquad E(d)_{2i+1}=0.$$

Then, for every admissible difference state,

$$B E(d)=S E(P(d)),\qquad B^tE(d)=S^t E(P^t(d)).$$

To verify the first identity, an embedded original $+1$ has BA sign $-1$
and moves from $2i$ to $2i-1$. This is the translation by one of the
new even site $2(i-1)$. An embedded original $-1$ has BA sign $+1$ and
moves from $2i$ to $2i+1$, the translation by one of its unchanged even
site. Opposite meeting paths arrive at $2i-1$ exactly when original
sites $i-1,i$ contain $-1,+1$, the annihilation case of $P$. All occupied
sites have the same parity, so no other half-step crossing occurs.
The second identity follows inductively because $B$ commutes with $S$.

This is an exact moving-frame restriction on even-site inputs, not a
static conjugacy from all ternary words to all BA states. Section 2's
anchor supplies the omitted three-valued coordinate explicitly. Neither
restriction, spatial frame, nor anchor creates a new particle mechanism.

## 4. Finite recurrent set and clock — fully deducted

A difference state with both signs is not recurrent. Its particle count
never increases and must eventually strictly decrease. More strongly,
opposite particles cannot both survive $n-1$ steps: their initial directed
distance along the moving $+1$ trajectory is an integer between one and
$n-1$, so their trajectories would have met by that time. If another
collision killed either one earlier, it was not a surviving particle.
It follows that $P^{n-1}(d)$ has at most one sign.

If every difference is nonpositive, then every $e_i=0$ and $T(x)=R(x)$.
If every difference is nonnegative, then
$C(x)_i=x_i+d_i=x_{i+1}$ modulo three, so $T(x)=R\rho(x)$, where
$\rho(x)_i=x_{i+1}$ is spatial left rotation. Each of these languages
is invariant and its displayed action is a permutation. Consequently

$$\operatorname{Rec}(T)=
\{x:d_i\le0\ \forall i\}\ \cup\
\{x:d_i\ge0\ \forall i\}.$$

The entrance time is exactly the first epoch with at most one particle
sign. If both signs remained at an earlier epoch, a later loss would
contradict periodicity. Thus $H(n)\le n-1$. For $n\ge2$, the state
with $d_0=1$, $d_1=-1$ and all other differences zero is admissible.
The single moving particle first meets its sole trap after exactly
$n-1$ steps. With anchor zero it is the word
$(0,1,0,\ldots,0)$. Hence $H(n)=n-1$ for $n\ge2$.
At $n=1$ every difference is zero, every colour belongs to a three-cycle,
and $H(1)=0$.

On the nonpositive language the exact labelled period is three. On the
nonnegative language it is the least $t\ge1$ such that
$\rho^t x=R^{-t}x$, and therefore divides $\operatorname{lcm}(n,3)$.
This is merely the period of the explicitly displayed commuting spatial/
colour action; no new period-counting or group-action result is claimed.

## 5. Inverse boundary and disposition

Every target satisfies the exact set identity

$$T^{-1}(y)=C^{-1}(R^{-1}y).$$

This is a target relabelling, since $R$ is bijective. It does not claim
that the primary source already evaluates all finite-ring fibres or a
sharp inverse maximum. No such source assertion is made here. A new
inverse calculation, even if correct, could not restore a materially
fresh temporal axis after the complete deductions above. Therefore no
independent inverse/extremum development, numerical pilot or gate
request follows this check.

All asserted mathematical statements above are deductive. The conclusion
is a bounded negative for this one literal, not a universal exclusion of
multistate cellular automata or a certificate that the research area is
exhausted. The scout is a proof contributor and, separately, has the
disclosed P209 scope familiarity. No independent review is claimed.
