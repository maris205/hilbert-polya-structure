# CSM01 — card-only independent derivation

Candidate: `ANG-AUDIT-20260923-CSM01`; Paper429; session2026-09-23.
Scope: the frozen full continuous-symmetry class and all three own controls.
Symmetry parameters s,t and physical height-translation parameter v are distinct.

## 1. Actual inputs, method and separation

- candidate-card.md original90-line prefix SHA256 79b08f0e6266d2d9d541f2175afd389ee9253bffb20a01fb544e24d62e039a9f.
- evidence/scope-review.md SHA256 d67348785f72cf4012ac38670c3041934cc171dad28a14f1ae6bba65bb941df9 — 92 frozen lines.
- Root fully read CP1 and separately released this raw stage. I reread
  precisely card1–90 and remeasured its prefix. No author paper/README/ledger,
  appended outcome, peer answer, sibling result or external source was read.
- Retained ARS/router/workflow/DA/runtime instructions and local scope apply.
  Informal design expectations and shared history are disclosed exposure;
  this is not blind or sealed preregistration. Same continuing AI reviewer,
  inherited settings, NOT_CALIBRATED; not human/external peer or cross-model
  verification. Effective served model identity/settings are not attested.
- Methods: density chain rule, exact iterate/arrow equations, closed-subgroup
  analysis on R and full symbolic control formulas. No scientific program,
  numerical search, auxiliary agent, Git/PDF or external action was used.
  Only this raw file is written; I have not edited the card or frozen CP1.

## 2. Every-Borel IMAGE and the all-point commuting correction

For a C1 diffeomorphism A, let j_A be its geometric positive density
Jacobian. Local change of variables and countably many charts give
mu(AE)=integral_E j_A dmu for EVERY Borel E, also when either side is infinite.
The smooth positive density on a second-countable manifold is sigma-finite
and has full support. The differential, not an a.e. modification, prescribes
these continuous positive finite values, including every periodic null point.
For two such maps the chain and inverse laws are

    j_AB(x)=j_A(Bx)j_B(x),       j_(A^-1)(Ax)=1/j_A(x).         (1)

In particular the actual inverse F^-1 has
q(w)=1/j_F(F^-1 w), mu(F^-1 E)=integral_E q dmu, and
kappa(x)=log j_F(x)=-log q(Fx). For each symmetry parameter t,

    mu(alpha_t E)=integral_E j_t dmu,
    mu(alpha_(-t) E)=integral_E j_(-t) dmu,
    rho_(s+t)(x)=rho_s(alpha_t x)+rho_t(x).                    (2)

Joint continuity of alpha and its spatial differential, with the smooth
density, gives joint continuity of j_t(x)>0 and rho_t(x). No time derivative,
infinitesimal generator, invariant density or preservation of mu is assumed.
Commutation F alpha_t=alpha_t F and (1) imply

    kappa(alpha_t x)=kappa(x)+rho_t(Fx)-rho_t(x).              (3)

For every integer k put D_k(x)=log j_(F^k)(x). It is the actual k-step
sum when k>=0; D_0=0 and D_(-k)(F^k x)=-D_k(x). The chain rule gives
D_(k+l)(x)=D_k(x)+D_l(F^k x), and the full all-integer correction is

    D_k(alpha_t x)=D_k(x)+rho_t(F^k x)-rho_t(x).               (4)

These are pointwise identities on the entire owner. They do not assert
that the clock itself is invariant away from isotropy.

## 3. Full actual source/extension ledger and symmetry action

Invertibility cancels F^n in F^m z=F^n w, giving w=F^(m-n)z. Thus

    G={(z,k,F^k z):z in M,k in Z},     c(z,k,F^k z)=D_k(z).    (5)

For any original meeting witnesses the identity
S_m(z)-S_n(w)=D_(m-n)(z) follows from the chain law. It proves descent;
the same law proves additive composition. All actual lags remain even
when several have identical endpoints. Inverse arrows negate c. Forward
arrival z->Fz is (Fz,-1,z), with clock -kappa(z), not +kappa(z).

The entire lag and clock kernels, including nonisotropy arrows, are

    M_lag = units,
    K_clock = {(z,k,F^k z):D_k(z)=0},
    M_lag intersect K_clock = units.                         (6)

Source orbits are exactly F^Z z with all inverse histories. A least-source-
period-p point has source isotropy pZ. Let C=D_p(z), which is independent
of the reference point on that cycle. Then, for every n in Z,

    c(z,np,z)=nC,     ENTIRE H_z=CZ,
    extension isotropy at (z,h)={np:nC=0}.                    (7)

For C!=0 the positive physical primitive is |C| and repeats are n|C| for
positive integers n; extension isotropy is zero. For C=0 source/extension
isotropy pZ remains, H=0, and there is no positive primitive. At aperiodic
points all three isotropy/return groups are zero. If F^N z is periodic,
its return transported by F^-N shows that z already lies on the cycle;
there are no outside strictly preperiodic incoming points.

All real heights remain. With reference b and z=F^n b, the arrow (b,n,z)
is FROM z TO b, so the complete extension-orbit phase is

    [h+D_n(b)] in R/H_b.                                    (8)

Changing n by mp on a period-p orbit changes the value by mC. Conversely,
equality modulo H_b supplies a reference isotropy arrow, so this classifies
all extension orbits. Every value occurs. Physical translation adds v to
the phase; its full stabilizer is H_b, distinct from extension isotropy.
H=0 gives a free real phase even with ineffective source isotropy. No
global regular quotient or measurable orbit selector is asserted.

For symmetry parameter t, the exact arrow action and corrected object lift are

    Phi_t(z,k,w)=(alpha_t z,k,alpha_t w),
    c(Phi_t g)=c(g)+rho_t(w)-rho_t(z),
    U_t(z,h)=(alpha_t z,h-rho_t(z)).                          (9)

Commutation proves these are actual arrows with unchanged integer lag.
The new target/source heights differ by c(g)+rho_t(w)-rho_t(z), proving
compatibility. Formula (2) proves U_s U_t=U_(s+t), including inverses.
It is a jointly continuous action on the full object space M times R,
commutes with physical height translation and induces an action on its
SET of extension orbits. No quotient by alpha or groupoid enlargement occurs.

Lag and joint kernels are invariant, but the full clock kernel need not be.
Its exact transport tests, for g=(z,k,w), are

    Phi_t^-1(K_clock)={g:c(g)+rho_t(w)-rho_t(z)=0},
    Phi_t(K_clock)={g:c(g)+rho_(-t)(w)-rho_(-t)(z)=0}.         (10)

The second follows by applying the first correction to Phi_(-t)g. In
contrast, on every isotropy arrow w=z the endpoint correction is ZERO.
Consequently Phi_t preserves its numeric clock, full source isotropy and
the entire H while taking the extension isotropy to that at U_t(z,h).
Measure preservation is sufficient for whole-clock preservation but is not
necessary; a rho_t constant along F-orbits also cancels the correction.

## 4. Complete finite-core multiplicity law and fixed-locus boundary

Let O be a nonempty finite F-cycle of least source period p. Its image
alpha_t O is again a least-p cycle: any shorter return would pull back by
alpha_(-t). On its lag-p isotropy arrow (9) gives the SAME signed cycle
sum C, not its negative. Entire H, primitive when nonzero, repetitions
and zero-clock ineffective isotropy are therefore the same on every image.

Set K_O={t in R:alpha_t O=O}. It is a subgroup. It is CLOSED, because
O is finite and closed and

    K_O = intersection_(x in O) {t:alpha_t x belongs to O}.    (11)

Each factor is closed by continuity. Inclusion into O is equality since
alpha_t is injective on the finite set. Closed subgroups of R here are
exactly {0}, aZ for a>0, or R. For completeness: if a subgroup has positive
elements arbitrarily close to0, integer multiples approximate every real
number and closedness gives R. Otherwise the positive infimum is attained
by closedness and positive; subtracting integer multiples shows that every
element is a multiple of this minimum. A subgroup with no positive element
is {0}. No properness or freeness of the action is needed.

K_O=R iff every point of O is fixed by every alpha_t: for the forward
direction, t->alpha_t x is continuous from connected R into the finite
discrete set O, hence constant. The converse is immediate. If K_O is proper,
the distinct image cores are in exact bijection with R/K_O, since equality
of two images is precisely a difference in K_O. Both R and R/aZ have
continuum cardinality. Distinct F-cycles are disjoint and cannot be joined
by an actual source arrow, so these are continuum-many DISTINCT packets,
not merely different representatives of one source or height orbit.

If C!=0 this family consists of continuum-many positive packets of the
same primitive |C|. If that primitive is not log an ordinary prime, prime
support fails. If it is log p, at-most-one fails. Hence existence of ONE
nonzero-clock core with nontrivial symmetry orbit is a decisive conditional
obstruction. No positive-core existence or global nontrivial action on
every core is assumed. If C=0 the same family consists of zero-clock source
cycles with free real phase; it alone supplies no positive packet. If K_O=R
the family has one core and this multiplicity argument does not apply.
The closed-subgroup argument is for FINITE cores; no such classification
is asserted for stabilizers of arbitrary infinite source orbits.

Fixed core does NOT imply fixed height. More generally, for t in K_O and
reference x in O, write alpha_t x=F^(j(t))x, with j(t) defined modulo p.
The induced action on the one packet's phase u is

    u -> u + D_(j(t))(x) - rho_t(x) modulo H.                (12)

The choice of j changes this only by H. Thus the stabilizer of a PHASE
under symmetry is exactly those t in K_O for which this shift belongs
to H, and is not generally K_O itself. This is still not an alpha quotient.

For a pointwise-fixed core, rho_(s+t)(x)=rho_s(x)+rho_t(x) by (2), and
continuity gives rho_t(x)=lambda t for some real lambda. Equation (3),
with all core points fixed, gives the same lambda along the whole F-cycle.
Now (12) is u->u-lambda t. If lambda=0 the phase is fixed for all t;
if lambda!=0 its symmetry stabilizer is {t:lambda t in H}, equal to
(|C|/|lambda|)Z when C!=0 and {0} when C=0. The source core can therefore
be fixed while its single physical phase circle is rotated. No extra
source packet or physical primitive is manufactured by that rotation.

## 5. Control A — whole translating line of positive cores

Write L=log2. For own Lebesgue area, F(x,y)=(2x,y) has inverse(x/2,y),
forward Jacobian2 and inverse IMAGE density1/2 at EVERY point. Translation
alpha_t(x,y)=(x,y+t) has j_t=1, rho_t=0; inverse translation has density1.
Change of variables gives all these identities for every Borel set.

    G_A={((x,y),k,(2^k x,y)):k in Z},     c_A=kL.              (13)

All three lag/clock/joint kernels are units. For k!=0, 2^k x=x forces x=0.
Thus ALL periodic cores are the separate fixed singletons O_y={(0,y)},
y in R. Each has source isotropy Z, extension isotropy0, ENTIRE H=LZ,
positive primitive log2 and every repetition n log2. No outside point
enters such a core. These are continuum-many distinct positive packets.

Every x!=0 point is aperiodic, with source orbit {(2^n x,y):n in Z},
source/extension isotropy0 and H=0. Its unique inverse histories and every
sign of x are retained. For any starting (z,h), including a fixed core,
its complete extended orbit is {(F^n z,h-nL):n in Z}.
For x!=0 set n=floor(log_2|x|), u=2^(-n)x, 1<=|u|<2. The reference
(u,y) gives the free real phase h+nL. At O_y the phase is h modulo L.

The exact symmetry is Phi_t from (9) and U_t(x,y,h)=(x,y+t,h).
It preserves the whole clock kernel. Every source orbit, periodic or not,
is moved to the distinct y+t orbit when t!=0. In particular K_(O_y)={0}.
Using transported references, the phase value is unchanged while the packet
changes. The primitive family log2 violates uniqueness, not prime support.
No line, null core, nonperiodic orbit or height has been selected away.

## 6. Control B — a fixed positive core despite nontrivial symmetry

Put B0=log3. On own Lebesgue area the inverse of F(x,y)=(2x,3y/2) is
(x/2,2y/3), with every-point inverse density1/3 and forward Jacobian3.
Thus kappa=B0. The radial alpha_t=e^t id has j_t=e^(2t), rho_t=2t,
and inverse IMAGE density e^(-2t). These follow by their own changes of
variables on EVERY Borel set. Alpha is not measure preserving, but rho_t
is constant in the source point, so the entire clock is preserved.

    G_B={((x,y),k,(2^k x,(3/2)^k y)):k in Z},   c_B=kB0.      (14)

All three kernels are units. A nonzero return requires both x=y=0, since
2^k and (3/2)^k differ from1 for k!=0. The origin is therefore the ONLY
periodic core, fixed, with source isotropy Z, extension isotropy0, H=B0 Z
and ONE physical primitive log3, with repetitions n log3. Every other
point is aperiodic, with source/extension isotropy0,H=0 and complete source
orbit {(2^n x,(3/2)^n y):n in Z}. There is no finite entrance to the origin.
Full extended orbits are {(F^n z,h-nB0):n in Z} at all points.

For x!=0 choose n=floor(log_2|x|) and b=(2^(-n)x,(3/2)^(-n)y),
with 1<=|b_x|<2. For x=0,y!=0 choose n=floor(log_(3/2)|y|) and
b=(0,(3/2)^(-n)y), with 1<=|b_y|<3/2. These unique orbit references
give every nonperiodic real phase h+nB0. The origin phase is h modulo B0.

The full lift is U_t(z,h)=(e^t z,h-2t). At the origin the finite core
is pointwise fixed, K_O=R, but its phase changes by -2t. The symmetry
stabilizer of a physical phase there is (B0/2)Z, whereas the lifted OBJECT
is fixed only for t=0. Physical height-translation stabilizer remains B0 Z;
these are different notions, and none adds a second source packet.

For completeness, source-packet stabilizers on the aperiodic remainder
follow from e^t x=2^k x and e^t y=(3/2)^k y. If xy!=0 then k=t=0.
On the nonzero x-axis they are (log2)Z; on the nonzero y-axis they are
log(3/2)Z. At such an axis packet return, the real phase shift is
kB0-2t, respectively k log(3/4) or k log(4/3), zero only for k=0.
Thus no aperiodic physical phase has a nonzero symmetry stabilizer.
For general t, transported references e^t b give the phase change -2t.

This full owner meets the necessary nonempty/prime-only/unique benchmark
at prime3, but NOT all-prime coverage. It proves that a globally nontrivial
continuous symmetry alone is not a class-wide no-go. Its only positive core
lies in the fixed locus. It is an EXTERNAL CONTROL, not a prime mechanism.

## 7. Control C — new full density and a genuinely moving clock kernel

Here the OWN measure is mu_C=e^(xy) dx dy on ALL R2. It is smooth, positive
and sigma-finite, with no restriction at large xy or at a null stratum.
F(x,y)=(2x,y) has own inverse(u,v)->(u/2,v), giving

    j_F(x,y)=2 exp(xy),        kappa(x,y)=L+xy,
    q(u,v)=(1/2)exp(-uv/2),
    j_t(x,y)=exp(tx),          rho_t(x,y)=tx.                 (15)

The inverse symmetry alpha_(-t) has density exp(-tx). These are ratios
of the actual densities times the coordinate Jacobians, so they prove
every-Borel IMAGE identities, not just a.e. formulas. They are C's own
pointwise versions; A's constant clock and kernel cannot be transferred.
For EVERY integer k, including negative k,

    F^k(x,y)=(2^k x,y),
    D_k(x,y)=kL+(2^k-1)xy,
    G_C={((x,y),k,(2^k x,y)):k in Z},     c_C=D_k(x,y).        (16)

The lag and joint kernels are units. The ENTIRE clock kernel is units
together with, for each nonzero integer k, exactly the arrows satisfying

    xy = -kL/(2^k-1).                                       (17)

All these products are negative, hence x,y are nonzero and the endpoints
are distinct. They do NOT create isotropy. Inverse-arrow consistency is
included by the negative-k formula. No branch of any hyperbola is discarded.

The full periodic set remains x=0, each point (0,y) a fixed core. Its
clock on lag k is kL, source isotropy Z, extension isotropy0 and entire
H=LZ; all these distinct packets have primitive log2 and repetitions nL.
All x!=0 points are aperiodic with source/extension isotropy0,H=0 and full
source orbit {(2^n x,y):n in Z}, including y=0 and both signs of x.
No nonzero point enters a core. Complete extended orbits are

    {((2^n x,y), h-nL-(2^n-1)xy):n in Z}.                    (18)

For x!=0, normalize x=2^n u with 1<=|u|<2. The complete free real phase
relative to (u,y) is h+nL+(x-u)y. At every fixed core it is h modulo L.
These formulas retain all heights even when the local kappa is zero or
negative away from the fixed line. A zero step clock is not a periodic core.

The full symmetry lift and arrow-clock change are

    U_t(x,y,h)=(x,y+t,h-tx),
    c(Phi_t g)=c(g)+(2^k-1)xt.                               (19)

This matches rho_t(w)-rho_t(z) exactly. Every nonunit clock-kernel arrow
in (17) leaves that kernel for every t!=0, because x!=0 and k!=0. For
an explicit exact check, k=1,x=1,y=-L gives c=0, while its translated
arrow has c=t. Units remain. Nevertheless on every isotropy arrow x=0
the correction vanishes, so the whole H and repetition law are unchanged.
Formula (19) is a group action, not an asserted preservation of A's clock.

The symmetry sends each fixed core (0,y) to (0,y+t) and leaves its phase
h modulo L unchanged. On a nonperiodic orbit with normalized reference
(u,y), the new reference is (u,y+t) and the phase changes by -tu:
h-tx+nL+(x-u)(y+t) equals the old phase minus tu. All source packets
have trivial symmetry setwise stabilizer because y is constant along F
and is shifted by t. In particular the positive-core family has K_O={0},
and continuum-many primitive-log2 packets violate uniqueness. Nonunit
zero-clock arrows elsewhere do not change this count or create extra H.

## 8. Bounded conclusion and freeze hold

The exact density correction, action law, full source/extension isotropy,
kernels, all inverse histories and real phases are established on the
frozen owner. A finite core is either pointwise fixed by the symmetry or
has continuum-many distinct symmetry-related core packets; only in the
nonzero-clock case does that force the stated positive multiplicity failure.
Zero cycles and fixed cores remain; B supplies the full fixed-core boundary,
while C verifies why whole clock-kernel invariance is not automatic.

This is a CONDITIONAL multiplicity filter for a proposed full realization,
not a universal class no-go, a quotient rescue or an admitted prime source.
No quotient by alpha, representative selection, new density, positive roof,
operator, partial-map or discrete-symmetry extension was introduced. Each
control owns its own measure and clock. All-prime coverage and endogenous
arithmetic/naturalness remain unestablished; arithmetic T1 NOT PASSED,
classical NOT APPLICABLE, T3 NOT AUDITED, formal UNASSIGNED, B NOT INVOKED.
No numerical, literature-priority, RH or external verification claim is made.

Freeze after complete readback and HOLD for root's full raw read followed
by separate PAPER UNLOCK. Preserve CP1 and the scientific prefix. Stop at
this bounded result; no430 or additional research is authorized here.

EOF — card-only derivation; shared-history internal NOT_CALIBRATED.
