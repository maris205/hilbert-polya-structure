# Matrix remainder feedback: owned volume and a rational-square period obstruction

Candidate ID: `ANG-20260922-MRF01`. Paper401, version1, 2026-09-22.
Outcome: `OWNED MATRIX IMAGE CLOCK; RATIONAL-SQUARE PERIOD OBSTRUCTION — STOP / FORK`.
Batch: `NONLINEAR-RETURN-20260922-K`, round2/5.
Type: piecewise-linear partial Borel action with nonlinear digit readout.
Classical symplectic/suspension fields NOT APPLICABLE; T3 NOT AUDITED.
Formal Route coordinates UNASSIGNED; Route B NOT INVOKED.
Authority: the complete [88-line frozen card](candidate-card.md), after CP1 release.
This is source-author work, not an independent review or a novelty claim.

## Abstract

Two current matrix quotients supply integer digits and a common-content permission,
which then governs simultaneous matrix residuals. The entire eight-dimensional
Lebesgue owner has explicit, exhaustive inverse domains and an all-point IMAGE clock.
All four frozen owners have empty fixed sets, but this is not a successful prime ledger.
For every actual MAIN cycle, its full primitive multiplier, if nonzero in time,
is a square of a positive rational number and cannot be an ordinary integer prime.
This necessary obstruction requires neither cycle existence nor a higher-period census.
All kernels, incoming histories, source/extension isotropy and phases are retained,
including zero-clock source cycles. The exact frozen owner stops.

## 1. Whole source and separately owned controls

Write \(z=(X,Y)\in\mathcal Y=M_2(\mathbb R)^2\), with usual Borel structure
and \(\mu=\operatorname{Leb}_8\). Whenever \(X,Y\) are invertible, set
\[
A=XY^{-1},\quad Q=\lfloor A\rfloor,\quad P=\lfloor A^{-1}\rfloor,\quad
d=\gcd(\text{absolute values of all eight entries of }Q,P).
\]
Floors are entrywise, with half-open integer cells, and all-zero content is \(d=0\).
Let \(W=[X;Y]\), a \(4\times2\) stacked matrix, and set
\[
B=B_{Q,P}=\begin{pmatrix}I&-Q\\-P&I\end{pmatrix},\qquad
C_Q=\begin{pmatrix}I&-Q\\0&I\end{pmatrix},\qquad
\Delta=\det B.
\]
MAIN has domain \(D=\{X,Y\text{ invertible},\ d\ge2,\ \Delta\ne0\}\)
and action \(W\mapsto BW/d\), namely \(((X-QY)/d,(Y-PX)/d)\).
Both residuals use the same OLD matrices. Every next step recomputes both quotients.
There is no separate integer root, frozen fibre or external arithmetic input.

Each owner uses the full \(\mathcal Y,\mu\), with the following own branch matrix \(L\):

| Owner | Actual source permission | \(T(W)=LW\) |
| --- | --- | --- |
| MAIN | \(D\) | \(L=B/d\) |
| G: GATE-OFF | \(X,Y,B\) invertible; \(e=\max(1,d)\) | \(L=B/e\) |
| N: NORMALIZATION-OFF | \(D\) | \(L=B\) |
| R: REVERSE-RESIDUAL-OFF | \(D\), including both floors and \(\Delta\ne0\) | \(L=C_Q/d\) |

Every domain complement is retained as terminals with \(T^0\), identities and all
actual incoming, but no absorbing loop. All singular/zero matrices, signs, units,
integer cuts and null fibres remain. No similarity or right-basis quotient is taken.
The branch selection is nonlinear; a fixed digit branch is linear, not a claimed smooth conservative flow.

## 2. Lineage admission is an actual source check

For every integer \(n\ge2,\ 1<q<n\), take the declared interface
\[
X=\operatorname{diag}(n,1/q),\qquad Y=I.
\]
Both are invertible; their quotient floors are exactly
\(Q=\operatorname{diag}(n,0)\), \(P=\operatorname{diag}(0,q)\).
Thus \(d=\gcd(n,q)\), and the proper-divisor witness \(q\mid n\) is exactly \(d=q\).
Here \(QP=PQ=0\), so
\[
B^{-1}=\begin{pmatrix}I&Q\\P&I\end{pmatrix},\qquad \Delta=1.
\]
MAIN therefore admits precisely those displayed seeds with \(\gcd(n,q)\ge2\);
in particular EVERY proper-divisor seed is admitted, rather than assumed admissible.
The permission is a common-factor deformation, not the identical proper-divisor test.
For an admitted seed the image is
\[
\left(\operatorname{diag}(0,1/q)/d,\ \operatorname{diag}(1,0)/d\right).
\]
Both matrices are singular: this is a retained terminal with a genuine incoming arrow,
not a periodic packet. The interface slice never replaces the whole carrier.
The preserved arrow is divisor witness, two current quotient digits, common content,
simultaneous residual transport, then newly read geometry. Named entries, floor,
threshold and measure are declared choices; no GL-invariance or strong naturalness is proved.

## 3. Complete inverses and every-Borel IMAGE

Enumerate ALL \((Q,P)\in M_2(\mathbb Z)^2\) satisfying the owner-specific digit
content/block restrictions. On each branch the four-dimensional matrix \(L\) is invertible.
For arbitrary target \(W'=[U;V]\), reconstruct \(W=L^{-1}W'\) and retain exactly
the targets for which \(X,Y\) are invertible, BOTH reconstructed floors equal
\(Q,P\), the full own source permission holds, and the own forward equation returns \(W'\).
For MAIN/G/N these are respectively \(B^{-1}[dU;dV]\),
\(B^{-1}[eU;eV]\), \(B^{-1}[U;V]\). For R they are exactly
\[
Y=dV,\qquad X=dU+QdV.
\]
R still checks its own \(P\), \(d\) and \(\Delta\), even though its residual formula omits \(PX\).

These actual inverse domains are Borel: inversion on \(GL_2(\mathbb R)\) is continuous,
floors are Borel and all other tests are explicit equalities/inequalities.
Each branch source set maps by an invertible linear homeomorphism to precisely this domain.
The reconstruction and forward formula are mutual inverses there. Every predecessor
has exactly one pair of current floors and thus appears in the enumeration.
No target-forward permission, finite digit cutoff or duplicate naming is inserted.
In particular, the singular targets of Section2 remain present.

Stacking by columns, \(W\mapsto LW\) acts by two identical \(4\times4\) blocks.
Its real eight-dimensional determinant is \((\det L)^2\). Moreover block elimination gives
\[
\begin{pmatrix}I&0\\P&I\end{pmatrix}B
=\begin{pmatrix}I&-Q\\0&I-PQ\end{pmatrix},
\qquad \Delta=\det(I-PQ)\in\mathbb Z\setminus\{0\}.             \tag{1}
\]
Consequently, with \(b=|\det L|>0\), the full-point inverse density is
\[
J=b^{-2},\qquad
\begin{array}{c|cccc}
\text{owner}&\text{MAIN}&\text{G}&\text{N}&\text{R}\\ \hline
b&|\Delta|/d^4&|\Delta|/e^4&|\Delta|&1/d^4 .
\end{array}                                                  \tag{2}
\]
All values are positive finite rationals at EVERY actual inverse-domain point.
For every Borel subset \(E\) of that domain, linear change of variables proves
\(\mu(\Theta E)=J\mu(E)=\int_EJ\,d\mu\), including null subsets.
This is exactly the frozen derivative of the displayed full linear inverse.
Measure alone does not choose values on null branches; the specified linear extension
does. There is no separate boundary patch or claim of continuity across different digit branches.

## 4. Full groupoids, cocycle and exact kernels

For each owner let \(T^0=\mathrm{id}_{\mathcal Y}\); all longer iterates require
their actual finite source histories. Its groupoid is the actual set of triples
\[
G=\{(z,\ell,w):T^mz=T^nw,\ \ell=m-n,\ m,n\ge0
       \text{ and both histories legal}\}.
\]
Source is \(w\), range \(z\); all integer lags remain and equal triples are one arrow.
This set is Borel by a countable union of legal-iterate equality sets.
Each source/range fibre is countable by the untruncated inverse enumeration.
Inversion swaps endpoints and changes the lag sign. To compose two arrows, extend
their meetings along the middle history to the larger of its two already-valid times.
This gives the sum of lags without trying to continue a terminal past its lifetime.

For a legal history define the positive rational product
\[
\beta_0(z)=1,\qquad \beta_m(z)=\prod_{j=0}^{m-1}b(T^jz).
\]
The owned one-step clock and its sums are
\[
\kappa(z)=-\log J(Tz)=2\log b(z),\qquad
S_m(z)=2\log\beta_m(z),\qquad
c(z,\ell,w)=2\log{\beta_m(z)\over\beta_n(w)}.                  \tag{3}
\]
Two presentations of the same triple have \((m',n')=(m+t,n+t)\).
Taking the longer presentation multiplies both products by the SAME legal
continuation product from the common meeting point. Thus (3) is well-defined;
the same alignment proof establishes additivity under composition.
Finite inverse words have density \(\beta_m^{-2}\). For two actual inverse words
\(\Theta_m(v)=z,\Theta_n(v)=w\), the branch-pair map \(w\mapsto z\) has IMAGE density
\(\beta_m(z)^{-2}/\beta_n(w)^{-2}=e^{-c}\) for every Borel subset.
Countably many finite inverse-word restrictions cover every actual arrow.

The lag kernel is exactly \(K_\ell=\{(z,0,w)\in G\}\), the same-time meeting relation.
For either presenting history write
\(A_m(z)=\prod_{j<m}|\Delta(T^jz)|\),
\(D_m(z)=\prod_{j<m}d(T^jz)\), and for G use \(E_m=\prod_{j<m}e(T^jz)\).
Only the products appropriate to that owner's legal domain are used; all empty products are one.
The COMPLETE clock-kernel tests are

| Owner | Exact condition for an ACTUAL arrow to belong to \(K_c\) |
| --- | --- |
| MAIN | \(A_m(z)D_n(w)^4=A_n(w)D_m(z)^4\) |
| G | \(A_m(z)E_n(w)^4=A_n(w)E_m(z)^4\) |
| N | \(A_m(z)=A_n(w)\) |
| R | \(D_m(z)=D_n(w)\) |

For \(K_\ell\cap K_c\), add \(\ell=0\) to the appropriate displayed test.
These integer equalities are independent of the chosen presentation by (3);
they do not enlarge \(G\) into a free branch graph or quotient away its zero-clock arrows.

## 5. Every source group, extension, incoming history and phase

The extension retains every \((z,h)\in\mathcal Y\times\mathbb R\) and
\((w,h)\to(z,h+c(z,\ell,w))\). Its lag/clock kernels and their intersection
are the lifts of the preceding kernels with all \(h\).
The actual forward step \((Tz,-1,z)\) has clock \(-\kappa(z)\);
its inverse \((z,1,Tz)\) has \(+\kappa(z)\).
Height translation acts on the full orbit SET; no smooth or Hausdorff quotient is asserted.

For any partial deterministic owner, nonzero lag isotropy is equivalent to an
eventual legal cycle. Indeed \(T^mz=T^nz\), \(m>n\), supplies a repeatable segment;
conversely a cycle supplies such equalities. If its least source period is \(r\),
all isotropy lags are exactly \(r\mathbb Z\): moving both meeting times into the
cycle proves divisibility by \(r\), and every multiple is obtained.
For an actual cycle put
\[
q_{\rm cyc}=\prod_{j=0}^{r-1}b(T^ju)>0,\qquad
C=2\log q_{\rm cyc}.                                         \tag{4}
\]
Preperiodic products cancel in (3), so at every point in its full source class
\[
G_z^z\simeq r\mathbb Z,\qquad H_z=c(G_z^z)=C\mathbb Z,\qquad
\operatorname{Iso}_{G^c}(z,h)=\{kr:kC=0\}.                    \tag{5}
\]
Thus \(C\ne0\) gives trivial extension isotropy and primitive time \(|C|\).
If \(C=0\), BOTH source and extension retain the full \(r\mathbb Z\), while
\(H_z=0\); a zero-clock source cycle is not a positive packet.
At terminals and non-eventually-periodic points both isotropy groups are trivial and \(H_z=0\).

For an arbitrary source class, transport each height to any one reference object.
Two choices of arrow differ exactly by its full \(H_z\). Hence its phase set is
\(\mathbb R/H_z\): a circle for \(C\ne0\), a free translation line for \(H_z=0\).
This identifies phases, not different source classes having equal clock.
Repetitions are integer multiples of the same primitive \(|C|\), not a relabelled smaller roof.

All incoming histories are precisely all finite compositions of Section3's
actual inverse domains, without depth/digit cutoff or infinite-history completion.
For a cycle with point set \(\mathcal O\), its full basin is
\(\bigcup_{N\ge0}T^{-N}\mathcal O\). A terminal's full class is
\(\bigcup_{N\ge0}T^{-N}\{t\}\); the latter has no source cycle.
All these points and all heights remain. Transport from \(z\) to \(T^Nz\)
changes phase by \(-S_N(z)\), with any further cycle movement accounted for by (5).
Every actual fixed core would be the special case \(r=1\); none is silently discarded below.

## 6. Complete fixed sets of all four owners

MAIN fixedness requires \(QY=(1-d)X\), hence \(Q=(1-d)A\).
For \(d\ge2\), every entry \(a\) would satisfy
\(\lfloor a\rfloor=-(d-1)a\). If \(a>0\), its floor is nonnegative while
the right side is negative; if \(a<0\), its floor is negative while the right
side is positive. Therefore every entry is zero, contradicting invertibility of \(A\).
Thus MAIN has NO fixed point, on any cell, sign or boundary.

For G the same argument excludes \(e>1\). When \(e=1\), fixedness and
invertibility imply \(Q=P=0\). It would require BOTH \(A\) and \(A^{-1}\)
to have all entries in \([0,1)\). This cannot happen for an invertible \(2\times2\) matrix:
write \(A=\begin{pmatrix}a&b\\c&f\end{pmatrix}\), with all four entries in \([0,1)\).
If \(\det A>0\), nonnegativity of \(A^{-1}\) forces \(b=c=0\), after which
its entry \(1/a>1\). If \(\det A<0\), nonnegativity forces \(a=f=0\),
after which an inverse entry \(1/c>1\). Invertibility guarantees the stated denominators
are positive; both cases contradict the upper bound. G therefore has NO fixed point.

For N, fixedness gives \(QY=PX=0\), hence \(Q=P=0\), contradicting \(d\ge2\).
For R, its second equation \(Y/d=Y\) contradicts invertible \(Y\) and \(d\ge2\).
Consequently
\[
\operatorname{Fix}(T)=\operatorname{Fix}(T_G)
=\operatorname{Fix}(T_N)=\operatorname{Fix}(T_R)=\varnothing.  \tag{6}
\]
Retained terminal identities are not fixed points of an undefined forward step.
This is a complete fixed-set result, not a truncated search and not positive-ledger success.

R also has no eventual cycle: along a legal cycle its second matrix would satisfy
\(Y_r=Y_0/\prod_{j<r}d_j=Y_0\), impossible with invertible \(Y_0\) and every \(d_j\ge2\).
Thus R has trivial source/extension isotropy and \(H_z=0\) everywhere; all its phase sets
are free lines. This monotone-scale argument does not assert finite-time termination.
For MAIN/G/N, higher-cycle existence is not classified; (4)–(5) give their full conditional ledger.

## 7. Algebraic cycle filter and decisive stop

For EVERY MAIN branch, \(b=|\Delta|/d^4\) is a positive rational.
For any actual least source cycle, \(q_{\rm cyc}\) in (4) is therefore a positive rational.
If \(C\ne0\), its full positive primitive multiplier is
\[
\exp(|C|)=\max(q_{\rm cyc}^2,q_{\rm cyc}^{-2})>1,              \tag{7}
\]
a rational square. It cannot equal any ordinary integer prime \(p\):
if coprime positive integers \(a,b\) satisfied \(a^2=p b^2\), then \(p\mid a\)
would imply \(p\mid b\), a contradiction. Prime factorization is a proof tool here,
not a prime table or parameter supplied to the dynamics.

Equation (5) is essential: incoming histories cannot divide this primitive time
by two, and zero-clock cycles cannot be promoted to positive ones.
Thus MAIN has NO ordinary-prime-log primitive packet. This is a necessary
obstruction whether its full positive ledger is empty or contains nonprime times.
The frozen NONEMPTY/all-prime-coverage target fails in either case; uniqueness at
prime times cannot rescue absent prime times. No cycle-existence assertion is needed.

G owns the same rational-square restriction using its own \(e\), without a cycle-existence claim.
For N, \(q_{\rm cyc}\) is a positive INTEGER product of \(|\Delta|\); a nonzero
cycle has a nontrivial integer-square multiplier, while product one retains zero-clock isotropy.
R has no cycles by its own second-coordinate law. These are separate control conclusions.
The repeated two-column volume factor explains this scoped `PROVES_TOO_MUCH` obstruction;
selecting one column or halving the clock would change the frozen owner.

## 8. Evidence, boundaries and handoff

T0 and the specified same-transport Borel clock are established. T2's necessary
ordinary-prime target is obstructed for this whole owner. Strong naturalness remains OPEN;
T3 NOT AUDITED, classical fields NOT APPLICABLE, formal coordinates UNASSIGNED, B NOT INVOKED.
The decision is STOP / FORK, not a global theorem against arithmetic-geometric feedback.
No higher-period census, fitting, science code, numerical experiment, external lookup,
operator, PDF, Git write or publication was used.

The author read the frozen 401 card 1–88, SHA-256
`97c81980e34b430191329cd1ef63965239c57cf0ab707a6fdcc6b587a404a4e5`,
and no reviewer evidence or peer result. Definition-stage access was
[395 batch summary](../395-simultaneous-content-return/batch-summary.md) 1–87 (EOF),
[395 original card](../395-simultaneous-content-return/candidate-card.md) 1–55 (non-EOF),
and [336 original card](../336-divisibility-lu-reassembly/candidate-card.md) 1–57 (non-EOF);
heading discovery exposed appended outcome titles, not their bodies. Prior 336-source
and 397-author participation and shared history are disclosed: NOT_CALIBRATED, not blind review.
No nonconjugacy or literature-priority claim follows from these limited comparisons.
All proofs are exact and contained here; no finite check supplies an infinite claim.

See the [claim ledger](claim-ledger.md), [overview](README.md) and
[prior-work lineage](../../docs/prior_work/README.md).
Data availability: the frozen card and displayed proofs are the complete scientific inputs.
AI assistance: AI agents supplied the mathematical derivation and manuscript drafting;
the separate internal-review workflow also uses AI agents. This record certifies no
human or external mathematical verification. The source author did not read reviewer evidence.
Human-subject ethics is not applicable. Funding/conflict information was not supplied;
no human-authorship or external-review attestation is made.
