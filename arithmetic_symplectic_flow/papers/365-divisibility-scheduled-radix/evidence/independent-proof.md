# Independent proof — divisibility schedule with full retained phase

Candidate: `ANG-20260921-DSR01`.
Standing: full variable-branch IMAGE owned; every MAIN physical return group
is zero because the retained phase forbids source isotropy — **STOP / FORK**.
Internal proof: `NOT_CALIBRATED`, not external peer review.

## 1. Input, exposure and scope

I personally read candidate-card.md lines 1–106 through EOF and measured
SHA-256 `a97872251dc4605ea0e60fd65c2ebfee83fedddf221c6200c3517cc4c3d000e8`.
This was the sole new scientific input. No author manuscript, peer, scout,
old scientific file, external source, numerical experiment or auxiliary was
used. ARS router/DA/runtime/workflow guidance remains retained from its
prior complete reads. Same model/shared history and the card's disclosed
phase-obstruction expectation prevent blindness or error-independence claims.
All findings were sent to root before writing. This is an independent proof
and adverse check, not a review of an unread author manuscript.

## 2. Full arithmetic schedule, path space and probability kernel

The intersection of all dK, d>=2, is {0}, since every finite residue must
then vanish. Thus b(q) exists and is finite for EVERY nonzero q. Its level
set is (intersection_{2<=m<d} mK) minus dK, a clopen set. The infinity
level is the singleton zero, so b is Borel. On embedded nonzero integers,
membership in dK is exactly ordinary integer divisibility, proving the interface.
The embedding of the integers in K is injective. Therefore N(q)=n exactly
at q=-n, n>=0, and otherwise N(q)=infinity. This is a Borel function.

Over q=-n the fibre is the finite product of its n prescribed digit sets,
followed by dagger forever. Their countable union is Borel in the ambient
product. Over phases outside {-n:n>=0}, infinite-path admissibility
is the countable intersection of a_i in N_0 and a_i<b(q+i). Hence the full
X, with all finite words and all infinite paths, is Borel.
For each q construct its conditional probability by recursively partitioning
[0,1) into b(q+i) equal half-open subintervals for the next digit, stopping
at N(q) and thereafter emitting dagger. Each finite coordinate of this coding
is Borel in (q,t). Interval lengths give precisely the independent uniform
finite-cylinder probabilities, including finite fibres and the empty word.
The pushforward of dt defines nu_q for EVERY q. For every Borel E subset X,
nu_q(E_q) is measurable by integration of the joint Borel coding indicator.
Integrating against Haar h gives the specified probability mu on the full X.
Zero-mass phases have not been removed: their conditional kernels are defined
by this same construction. No uniform distribution on an infinite alphabet
is introduced at q=0. The full carrier is not replaced by the coding's image.

## 3. Complete source, inverses and every-Borel IMAGE

For q!=0, N(q+1)=N(q)-1 when finite, and remains infinite otherwise.
Thus the shift gives the stated Borel map T on exactly X minus (0,empty).
If r!=1, every j<b(r-1) gives the legal predecessor (r-1,jw), and these
are all predecessors. If r=1 there is none; the target nevertheless has
its ordinary forward step. Direct removal/insertion of the first digit
proves both inverse identities and the exact E_j. In particular terminal
(0,empty) has two immediate predecessors at q=-1, since b(-1)=2.

For every allowed q,j and every Borel tail set B in X_(q+1), the complete
conditional product law gives nu_q(jB)=nu_(q+1)(B)/b(q).
Apply this to the sections of any Borel E subset E_j and substitute r=q+1
in Haar integration. One obtains exactly
mu(theta_j E)=integral_E [1/b(r-1)] dmu(r,w).
This is an EVERY-Borel statement, not a ratio of whole fibre masses, which
would be zero over a singleton phase. The all-point prescribed version is
finite and positive on E_j, including its null targets. Its justification
uses the frozen conditional laws at every q, not a.e. uniqueness of a density.
For an admissible length-m prefix starting at q, put
P_m(q)=product_{0<=i<m} b(q+i), P_0=1. Iterating the same argument gives
the inverse-history density 1/P_m(q), on its entire actual target domain.

## 4. Actual arrows, all kernels and complete incoming phase

A triple (z,m-n,w) with equal legal tails satisfies
q_z+m=q_w+n. Hence its lag k=m-n is the UNIQUE integer q_w-q_z.
The proposed c=S_m(z)-S_n(w) is witness independent: extending both
witnesses adds identical common-tail terms. Aligning the middle histories
proves additivity, with only legal continuations. Equivalently, if k>0,
c=S_k(z)>0; if k<0, c=-S_(-k)(w)<0; and k=0 gives c=0. The common-tail
witness supplies the required legal shorter segment. Positivity uses b>=2.
On a pair of inverse-history charts I_u,I_v over a common tail t, their
densities are j_u=1/P_m and j_v=1/P_n. Thus the replacement's IMAGE is
j_u/j_v=exp(-c). Change of variables through I_v proves the EVERY-Borel
history law, not an undefined quotient of two null-set masses.

The groupoid is Borel as a countable union of legal-iterate equality relations.
It retains equal triples only once. Its full clock
kernel equals its lag kernel:
{(z,0,w):q_z=q_w and T^m z=T^m w for some legal m}.
This can contain distinct words; it is not just identities. But isotropy
forces q_z+m=q_z+n, so m=n. ENTIRE source isotropy, extension isotropy
and H_z are zero at EVERY object, including all terminating histories.
No loop can be recovered from a periodic digit projection with moving phase.
The extension on all real heights is a Borel groupoid; height translations
commute with all its arrows. Only its orbit set is used, with no assertion
of a coarse manifold or an invariant physical-flow measure.

All depth-m predecessors of (r,w) are (r-m,uw), where u has the prescribed
digits and r-j!=0 for 1<=j<=m. All incoming source-orbit objects are
union_{legal n,m} T^{-m}(T^n(r,w)), with those complete inverse lists.
This retains arbitrary off-window prefixes, but does not equate unrelated
infinite words merely because their phases differ by an integer.
For an orbit anchor a and any arrow (z,k,a), the complete real phase is
h-c(z,k,a); uniqueness of lag and zero isotropy make it independent of choice.
The terminal orbit is precisely all fibres at q=-n, n>=0. Its entrance
clock is A_n=sum_{s=1}^n log b(-s), and its phase is h-A_n for EVERY word
in that finite fibre. Distinct terminal-bound words of the same length have
zero-lag arrows; none has positive-time isotropy. This closes the MAIN gate.

## 5. DIGIT-OFF: its own complete partial translation

Q has domain K minus {0}, inverse r->r-1 on K minus {1}. Haar translation
gives its own EVERY-Borel inverse IMAGE 1 and the prescribed all-point c=0.
The same phase equation proves source isotropy and extension isotropy zero,
and every H is zero. Its FULL clock kernel is now the entire groupoid,
whereas its lag kernel contains only identities: there are no digit choices.
Noninteger q has the full orbit q+Z. The embedded integer orbit is split
by the missing edge 0->1 into Z_{<=0} and Z_{>=1}, not one merged orbit.
All inverse depths obey r-j!=0 as above. Zero is terminal; 1 has no
predecessor but is not terminal. Every incoming orbit has unchanged real
height as phase. MAIN's variable clock is not assigned to this control.

## 6. PHASE-OFF: full binary primitive/incoming ledger

Each prefix inverse has EVERY-Borel IMAGE 1/2 by the fair product law.
Replacement v eta->u eta has density 2^{|v|-|u|} at every tail-cylinder
depth and on every Borel subset; c=(|u|-|v|)log 2 descends to actual lag.
The full clock/lag kernel is synchronized tail equivalence at equal depth,
not merely identities. Eventual least-tail-period q gives entire source
isotropy q Z and H=q log 2 Z; noneventual points have both groups zero.
Extension isotropy is always zero because c is injective on isotropy.
For a primitive periodic eta of length q, ALL incoming are u sigma^j eta,
0<=j<q, with phase h-(|u|-j)log 2 modulo q log 2. Different primitive
necklaces cannot share a forward tail, and never merge by height translation.
Noneventual orbits are all prefixes of all forward tails of an anchor;
their unique lag k gives the real phase h-k log 2. Repetitions of a positive
packet have times n q log 2. If P_q(2) counts primitive length-q words,
2^q=sum_{d|q}P_d(2), so the EXACT number of packets is P_q(2)/q.
These formulas cover all states and ancestors, not only the two constants.
This changed owner does not inherit MAIN's divisor permissions or no-return result.

## 7. FINITE-PHASE: entire alternating-path ledger

Its own two phase weights are equal. Conditional prefixing and the phase
permutation therefore give EVERY-Borel inverse IMAGE 1/b_C(r-1), including
every null path; T_C is total, with all its stated inverse branches.
For m>=0, S_m(r)=floor(m/2)log 6+(m mod 2)log b_C(r).
Equal-tail witnesses give c=S_m(r_z)-S_n(r_w), independent of presentation.
Its sign is the sign of lag by the signed-interval argument. Thus its full
clock kernel again equals lag-zero synchronized tails, with the phase retained.

At phase 0, group successive digits into pairs in {0,1} times {0,1,2}.
Then T_C^2 is EXACTLY the full one-sided shift on six letters. Every cycle
must have even length; a primitive q-letter paired word gives least full
source period 2q, entire isotropy 2q Z and H=q log 6 Z. Conversely every
eventually periodic full state reaches such a paired core; noneventual
states have isotropy and H zero. Extension isotropy is zero everywhere.
Each eventual-periodic orbit crosses phase 0; its paired necklace identifies its core
uniquely. Hence the EXACT packet count at q log 6 is P_q(6)/q, where
6^q=sum_{d|q}P_d(6). In particular there are SIX least-log-6 packets,
even when a digit projection is constant; the full source period is still 2.
All incoming consist of every alternating-admissible finite prefix of every
phase-labelled forward tail. With core eta at phase 0, a prefix of length m
attached to T_C^j eta starts at r=j-m mod 2 and has phase
h-[S_m(r)-S_j(0)] modulo q log 6. Repetitions have times n q log 6.
Noneventual orbits have real phase h-c_C(z,k,a), using their own orbit anchor a.
These statements use this control's own phase, measure and entire H, not MAIN's.

## 8. Adverse conclusion and remaining obligations

The arithmetic schedule, all-point variable IMAGE and full-state ownership
are established. Nevertheless the retained K phase eliminates all MAIN
positive primitives. Dropping it or replacing it by a finite phase changes
the owner; the control returns cannot rescue MAIN. No technical obligation
in this frozen owner/control gate remains unresolved. Strong naturalness is
still OPEN, T3 is not audited, classical A0/A1/A2 are not applicable, formal
Route unassigned and B not invoked. Stop/fork without deleting null fibres,
repairing the schedule, adding a roof or continuing a digit-only period search.

EOF — full retained-phase gate and all three own controls; report frozen.
