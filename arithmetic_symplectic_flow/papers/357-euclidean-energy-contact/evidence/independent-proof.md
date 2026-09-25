# Independent Euclidean energy-cover and packet audit

**Candidate:** `ANG-20260921-EEC01`.
**Finding:** MAIN owns the stated cover/action and a primitive time strictly
between0 and log2. R fails its own Reeb/descent tests; D/U are distinct controls.
**Standing:** Internal inherited-model/shared-history; `NOT_CALIBRATED`.

## 1. Input and scope

After explicit release I personally read original357 card lines1–115 through
EOF and measured SHA-256
`435fa4906a0790fdb64cdd4141268e9290bde67eda576128fe83f0ad7e021333`.
This was the only scientific file read. I derived MAIN, R, the entire
ell1 stabilizer and D/U, then sent the parent the findings before writing.
No root paper, scout/peer answer, external source, scientific computation
or auxiliary agent was used. Only this assigned file was written.
The already-read ARS instructions apply; the card's quadratic-scaling
expectation and inherited context preclude blind/independent-error claims.
This is not external peer review. No ell2 or broader cycle census is made.

## 2. Full smooth cover, Reeb field and physical volume

For H=q dot p, dH=(p,q) is nonzero on H=1, so M is a smooth3-manifold.
Both q and p are nonzero there. With omega=d alpha=sum dp_i wedge dq_i,
the vertical field Y=sum p_i partial_(p_i) satisfies i_Y omega=alpha and
dH(Y)=1. Since omega^2 is a nonzero4-volume,
alpha wedge d alpha=(i_Y omega^2)/2 restricts nonvanishingly to M.
This proves contactness on ALL signs, axes and fibers without a chart deletion.

R=(q,-p) satisfies alpha(R)=1 and i_R d alpha=-dH, zero on TM.
Thus the frozen Phi is its actual Reeb flow, complete for all real t,
with inverse Phi^(-t). Its pullback fixes alpha and d alpha, preserving
mu=|alpha wedge d alpha| for every Borel set. This is a cover result,
not an assertion that the coarse orbit set is a smooth contact manifold.

## 3. Half-open branches, complete inverses and IMAGE

The forward base map is Q=(y,x-ell|y|); its second coordinate is in
[0,|y|). The matrix is symmetric, has determinant-1, and its inverse is
[[ell sigma,1],[1,0]]. Therefore its exact image is V_sigma in the card.
For Q there the inverse has y=Q_1 and
x/|y|=ell+Q_2/|Q_1|, including the lower cut and excluding the upper cut.
This proves both inverse identities and the full half-open domains.

Every target in V_sigma has exactly one incoming branch for EVERY integer
ell, with sigma determined by Q_1; all targets outside the union have none.
In particular every terminal target(Q_1,0), Q_1!=0, has all these incoming
branches, not just identity. Target zero remainder is never discarded.
Cotangent momentum is restored as A^T P on each entire stated inverse domain.

The ambient cotangent linear map preserves H and alpha exactly. Its smooth
restriction to M preserves contact volume, hence mu(I_(ell,sigma)(E))=mu(E)
for EVERY Borel E inside V_sigma. The all-point IMAGE version is1, including
all cuts and terminal targets. Derivatives mean the indicated ambient
linear branch. S as a whole is Borel/piecewise smooth, not claimed continuous,
differentiable at cuts or étale. Branch preservation is not global measure
invariance of a map with countably many incoming branches.

## 4. Actual Borel groupoid and full Phi descent

Legal iterate domains are Borel, so the union of the actual equality
relations at all(m,n) gives the stated Borel subset of M x Z x M.
To compose common-tail arrows, align their two middle iterate depths at
the larger one. The requisite extension is legal because the corresponding
middle history exists; equality forces the other history to extend too.
This proves closure, inverses and identities even at terminals. Identical
triples are not duplicated as formal histories. Branch IMAGE characters
are zero on all actual arrows, independently of physical time.

Positive dilation preserves sign(y), x/|y|, every half-open cut and every
terminal. On each legal branch S Phi^t=Phi^t S exactly, including momenta.
Thus Phi preserves every legal history and maps(a,k,b) to
(Phi^t a,k,Phi^t b), an actual arrow with the same lag. It gives a complete
real SET action on M/G; each fixed-time induced map is measurable for the
quotient sigma-algebra. The cover action is jointly smooth/Borel. No standard
Borel, Hausdorff, smooth or stronger product-topological coarse owner is inferred.

In fact all MAIN source isotropy is trivial. After two nonterminating steps,
the base coordinates satisfy0<y<x; subsequent first coordinates strictly
decrease, since the next pair is(y,r), 0<=r<y. A periodic source history
would contradict this, while terminal histories cannot repeat. This is an
elementary source statement, NOT absence of physical quotient returns.
Distinct terminal targets can be common-tail equivalent only if identical;
their Phi dilates q nontrivially, so axis-terminal orbit classes have H={0}.

## 5. R: group, measure, Reeb and descent tested independently

On M, rho is smooth, positive and homogeneous of degree0 in nonzero q.
Therefore rho is unchanged along Psi, proving the group law and completeness.
The form alpha_rho is contact, with volume mu_rho=rho^(-2)mu.
For its proposed generator rho R one has

```text
alpha_rho(rho R)=1,
i_(rho R) d alpha_rho=d rho/rho.                          (1)
```

The latter is nonzero when xy!=0, so Psi is NOT its Reeb flow.
More exactly Psi^(t)*alpha_rho=alpha_rho+t d(log rho). Nevertheless its
contact volume IS preserved: d rho is R-horizontal, and
d(log rho) wedge d alpha_rho=0 in horizontal dimension2.
This positive measure fact does not repair the failed Reeb identity.
For an inverse S branch the own IMAGE density is
[rho(Q)/rho(A^(-1)Q)]^2, valid for every Borel set, not MAIN's constant1.

There is also an independent failure of ACTUAL quotient descent. Take
a=((1,1),(1,0)) and b=S a=((1,0),(1,1)), both on M. The latter is terminal.
Here rho(a)=3/2 and rho(b)=2. After applying Psi^t, the unique terminal tail
of Psi^t a is(e^(3t/2)(1,0),e^(-3t/2)(1,1)), whereas Psi^t b is
(e^(2t)(1,0),e^(-2t)(1,1)). They differ for t!=0. Terminal tails cannot
be joined through some alternative incoming history, so these two states
have NO actual common-tail arrow. Psi does not induce an action on M/G.
This excludes R alone, not every state-dependent time change.

## 6. Entire ell1 stabilizer and decisive primitive

Let phi=(1+sqrt5)/2, lambda=1/phi, q_0=(phi,1), and
p_0=q_0/(q_0 dot q_0). This is a full point a_0 of M, not a selected owner.
For A=A_(1,+), A q_0=lambda q_0 and A^(-T)p_0=lambda^(-1)p_0.
Every positive dilation stays strictly inside the same ell1 branch. With
L=log phi, all m>=0 and every real t satisfy

```text
S^m Phi^t a_0=Phi^(t-mL) a_0.                             (2)
```

The cover dilation is free on M since q!=0. Thus any actual common tail
S^m Phi^t a_0=S^n a_0 holds EXACTLY when t=(m-n)L. Consequently
H_[a_0]=LZ, with least L>0, and source isotropy is0. All positive repetitions
are kL in that same packet. There is no extra smaller time supplied by
inverse histories: groupoid equivalence is exactly the tested common-tail
condition, already allowing every m,n. All incoming states in this orbit
have this same quotient stabilizer; they do not define a shorter primitive.

All cotangent fibers remain. Along the same positive q ray, decompose p
into the q_0 eigenline and the other eigenline of A, whose eigenvalue is
-phi. Energy1 fixes the first coefficient. If the second coefficient is
nonzero, the same return calculation additionally requires
(-lambda^2)^(m-n)=1; hence m=n and t=0. Only the aligned fiber gives(2).
Its positive-ray points are one physical orbit, not separately chosen packets.

Since1<phi<2, 0<L<log2: this is not log of any prime. Its ENTIRE group makes
it a genuine wrong primitive, not merely a tested return. The frozen time
normalization cannot be rescaled after this result. The short gate decides
STOP / FORK; ell2 and all larger periodic censuses are not pursued.

## 7. D: full swap source with no physical quotient periods

D has one inverse(JQ,JP), defined exactly Q_1!=0. It preserves H, alpha
and every-Borel contact volume; all-point IMAGE is1. If x,y are both nonzero,
its source orbit has one or two points: least1 exactly when x=y and
p_x=p_y=1/(2x), otherwise least2. Corresponding source isotropies are Z
or2Z. At an axis, a point(0,y) maps once to terminal(y,0), with its swapped
momentum; there are no further ancestors of the x=0 state. Axis source
isotropy is0. Thus every state and all terminal incoming are accounted for.

Phi preserves the domain and commutes with J, so it descends. If a physical
return uses the swap, e^t q=Jq implies e^(2t)q=q, hence t=0; a return using
identity also has t=0. Therefore ALL D physical stabilizers are zero despite
its nontrivial source isotropy. The zero IMAGE character retains that entire
source-isotropy kernel. No physical primitive is supplied by the two-cycle.

## 8. U: full R4 owner and its own witnesses

The same inverse matrices/domains apply without an H constraint. They
preserve alpha, d alpha, H and Lebesgue symplectic volume, so every-Borel
branch IMAGE is1. The full Phi is a complete symplectic/Liouville action,
not a Reeb flow on an even-dimensional space. Its branch domains and
actual arrows are invariant exactly as in section4, including q=0 terminals.

Every q=0 point has no incoming S branch and only its identity source orbit.
At(q,p)=(0,0), physical H is ALL R. At q=0,p!=0 it is{0}. Neither can be
erased or replaced by the energy1 ledger. For every E in R, take q=q_0 and
p=E p_0. The OWN calculation gives(2) and H=LZ, even at E=0. H=q dot p
is invariant under both actual source arrows and Phi, so different E give
inequivalent packets: already a continuum within this frozen ell1 family.
All source isotropy is0 by the nonzero-q descent argument or terminality.
No full U periodic census is claimed after these complete witnesses.

## 9. Adverse disposition

The main cover, piecewise forms, full Borel source and actual physical
quotient SET action are owned; zero branch IMAGE time does not negate its
physical returns. The decisive negative is instead the entire wrong-time
primitive in the fixed H=1 normalization. R's independent failures do not
invalidate MAIN. D separates source lag from physical return; U shows why
the frozen energy restriction cannot be omitted silently. No alternate
energy, clock, section, smooth coarse quotient, T3 or quantum result is claimed.
Strong naturalness remains OPEN and formal Route B is not invoked.

EOF — MAIN/R/ell1/D/U bounded independent audit complete.
