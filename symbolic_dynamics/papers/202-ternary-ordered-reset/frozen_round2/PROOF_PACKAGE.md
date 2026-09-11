# P202 author proof package

Status: PROVABLE AS STATED, with the explicit scope below. This is an
author companion, adapted from the writer's prior Stage1 reconstruction;
it is not an independent manuscript review. The main manuscript contains
the entire proof without needing this file.

## Claims, assumptions and dependencies

The carrier is the full set of length-n cyclic labelled words over
0<1<2, for every integer n>=1. Updates are synchronous, with the right
neighbor, including the self-neighbor at n=1. The local output rows,
indexed by the current letter and columns 0,1,2, are 111,022,000.
No random initialization, quotient by rotation, or larger alphabet is assumed.

The inverse theorem depends only on these nine local entries. The temporal
theorem uses the image theorem to obtain the run factor, then elementary
finite parking and original-coordinate action checks. Counting uses the
proved languages and finite adjacency matrices. The numeric controls are
falsification tests, not a premise of any all-length theorem.

## 1. Complete inverse, including zero fibres

At target 0 the allowed source edges are 10,20,21,22; at target 1 they
are 00,01,02; at target 2 they are 11,12. Thus target 21 is impossible:
the common source letter would have to be simultaneously nonzero and zero.
Conversely, if target y avoids cyclic 21, set
$x_i=y_i-1\pmod3$. Each source 1 then sees a nonzero neighbor, so this
is a source. The only alternative to source 2 at a target 0 is source 1
followed by source 0, exactly a target edge 01. Choosing this alternative
independently at any subset of target 01 edges gives every source.
Different 01 edges share no vertex and the choices are readable from x;
there is neither incompatibility nor duplicate output in the decoder.
Consequently the fibre is zero off the image and $2^{e_{01}(y)}$ on it.

The disjoint edges give $e_{01}\le\lfloor n/2\rfloor$. At even n,
equality forces alternation, yielding exactly two targets. For odd
$n=2m+1\ge3$, the paired edges leave one vertex. Cutting there produces
$001(01)^{m-1}$, $011(01)^{m-1}$, or $012(01)^{m-1}$ according to its
letter. All avoid 21. Their unique doubled-zero, doubled-one or sole-two
feature gives n different rotations per type and separates the types.
There are exactly 3n maximizing targets. At n=1, the map is a three-cycle
and all three fibres are one. Constants have unique constant sources at
every length, so a nonconstant orbit cannot become constant.

## 2. Run factor with spatial-phase limitation

A nonconstant image word contains zero; otherwise a nonconstant cyclic
binary word on 1,2 would contain 21. Its zero runs define cyclic blocks
$0^{c_i}1^{a_i}2^{b_i}$, where $c_i\ge1$, $a_i,b_i\ge0$ and
$a_i+b_i\ge1$. Track the order of these blocks. The old zero run becomes
a one run of length $c_i$. When $b_i>0$, all old ones become twos and
all old twos become zeros. When $b_i=0$, the final one resets to zero.
The resulting positive one runs prevent mergers and give

$$c_i'=\max(b_{i-1},1),\qquad a_i'=c_i,\qquad
b_i'=a_i-\mathbf1_{\{b_i=0\}}.$$

This includes an initially absent one run. The number k of blocks stays
fixed. After the second original update both c and a are positive.
Subtract their compulsory ones, setting
$z_{c_i}=c_i-1$, $z_{a_i}=a_i-1$, $z_{b_i}=b_i$. Their mass is
$M=n-2k$, and, with $u_+=\max(u,0)$,

$$z_{c_i}'=(z_{b_{i-1}}-1)_+,\quad
z_{a_i}'=z_{c_i},\quad z_{b_i}'=z_{a_i}+\min(z_{b_i},1).$$

Thus particles move through the 3k cyclic bins c,a,b, with each b bin
retaining one particle permanently. Give particles distinct labels and
choose any arriving label when an empty slot is filled. The labels do not
affect counts. These coordinates retain cyclic order but discard an
absolute spatial origin: they are not a claimed full labelled-word
conjugacy. Entry criteria are rotation invariant; periods will be checked
on the original coordinates.

## 3. Finite parking calculation (prior mechanism, zero novelty credit)

Define clearance as the first time all particles are parked or all k
slots are occupied. If M=0 it is zero. For $1\le M\le k$, a mobile
particle cannot complete a circuit before parking: all k visited slots
would have to hold distinct other particles, requiring at least k+1
particles. Its passed slots are therefore distinct and each consumes
another particle. A transit-bin start meets a first slot within two
steps, so it parks by $2+3(M-1)=3M-1$. Starting at an occupied slot
already consumes another particle, giving at most $3+3(M-2)$ when that
case occurs. This bounds the final parking time.

For $M\ge k$, suppose a slot remains empty at time $3k-1$. Fewer than
k particles have parked, so a particle remains mobile. It never parked
earlier and thus moved at every step. Its destinations visited every bin
except possibly its starting bin. It could not miss the empty slot
unless it started there, but then a particle would have parked there at
time zero. This contradiction proves clearance by $3k-1$.

Put all M particles into a single c bin. Slots fill at times
2,5,8,..., and the last necessary filling is
$3\min(k,M)-1$. Hence the bound is sharp for every positive k,M.
The calculation specializes already owned particle parking; it is not a
new general method or a separately credited contribution axis.

## 4. Exhaustive recurrence and exact point clock

Let $\mathcal A_n$ allow the six edges with cyclic difference 0 or 1.
Directly on those edges, F is global colour addition by one. This action
preserves the language and every point has exact period three. Let
$\mathcal B_n$ allow 01,10,12,20, equivalently circular concatenations
of 01 and 012. On those four edges F copies the right neighbor, so its
action is left rotation and periods are the ordinary spatial periods.
Their common edge list is 01,12,20. Therefore their intersection has the
three rotations of a repeated 012 if 3 divides n, and is empty otherwise.

In the twice-image run domain, all slots filled means all $b_i\ge1$,
exactly membership in $\mathcal A_n$. All particles parked means
$c_i=a_i=1$ and $b_i\in\{0,1\}$, exactly $\mathcal B_n$.
Finite clearance sends every nonconstant state into this union, while
constants are already in the first language. Both languages are periodic,
so the union is precisely the full recurrent set. Before clearance there
are a mobile particle and an empty slot, excluding both languages.
Thus clearance is exactly, not merely an upper bound for, remaining
entrance time in this domain. Original-coordinate actions close the
spatial-phase issue without relying on quotient recurrence.

## 5. Global sharp tails, boundaries and witness prehistory

For a nonconstant twice-image, k>=1 and $M=n-2k\ge0$. If M>0, the
original tail is at most
$2+3\min(k,n-2k)-1\le3\lfloor n/3\rfloor+1$. If M=0, the tail is
at most two. Constants need no tail. At n=1 every point is recurrent;
at n=2 the witness $12\to20\to01\leftrightarrow10$ has tail two.

For $n=3k+r\ge3$ with $0\le r\le2$, choose
$x=1^{k+r+1}2(12)^{k-1}$. Direct updates give
$F(x)=2^{k+r+1}0(20)^{k-1}$ and
$F^2(x)=0^{k+r+1}1(01)^{k-1}$. The latter has k blocks, M=k+r particles
in one c bin, and all slots empty. Its remaining tail is exactly 3k-1
by the parking equality case. No earlier point can have been recurrent,
since recurrence is forward invariant. Thus $h(x)=3k+1$, proving
$H(1)=0$, $H(2)=2$, and $H(n)=3\lfloor n/3\rfloor+1$ for n>=3.
No classification of all maximum-tail source words is asserted.

## 6. Target and periodic census

Let V(u) have rows (1,u,1), (1,1,1), (1,0,1). A closed walk with labelled
initial coordinate is a cyclic labelled word, not a rotation class.
Thus $\operatorname{tr}V(u)^n$ counts image words weighted by
$u^{e_{01}}$. The characteristic polynomial of V(1) is
$\lambda(\lambda^2-3\lambda+1)$: trace three, principal two-minor sum
one, and determinant zero. The nonzero roots are squares of the two
roots of $z^2-z-1$, yielding image count $L_{2n}$.

The first recurrent language has adjacency $I+P_3$, with eigenvalues
$2,1+\omega,1+\omega^2$, where $\omega^3=1\ne\omega$.
Hence $a_n=2^n+\epsilon_n$, with six-periodic epsilon
(2,1,-1,-2,-1,1). The second has matrix Q with rows (0,1,0), (1,0,1),
(1,0,0). Its characteristic polynomial is $\lambda^3-\lambda-1$,
so traces satisfy $b_0=3,b_1=0,b_2=2$ and $b_n=b_{n-2}+b_{n-3}$.
The zero-index trace is a matrix convention, not an empty-word carrier.
Inclusion-exclusion gives recurrent count $a_n+b_n-3\mathbf1_{3\mid n}$.

For t>=1, the colour action contributes all $a_n$ exactly when 3 divides t.
Writing $d=\gcd(n,t)$, the rotation-fixed words repeat a closed word of
length d and contribute $b_d$. The overlap contributes three precisely
when 3 divides d. Therefore
$|\operatorname{Fix}(F^t)|=\mathbf1_{3\mid t}a_n+b_d-3\mathbf1_{3\mid d}$.

## Exact controls and open risks

The standalone code checks all 797,160 states and all target source sets
at n=1,...,12. It uses bitplane updates, actual orbit-cycle discovery and
local source-edge walks rather than assuming the closed formulae.
Run equations, complete weighted coefficient vectors, fixed counts for
1<=t<=6n, 7,280 complete labelled-token parking configurations, and sharp
witnesses n=3,...,150 are also checked. Two new paper-author processes
each pass 3,962,690 assertions with byte-identical stdout. Code reuse is
explicit: these are author checks, not new independent reviews.

There is no unresolved deductive lemma in the printed scope. The open
risks concern external ownership, missing P51--P56 history, arbitrary
block encodings or powers, and possible exact joint owner transfers.
All generic parking, moving-frame and transfer methods are deducted.
The manuscript remains OWNER_AMBER / HOLD_EXTERNAL, pending independent
paper Review A and B and eventual further source work.
