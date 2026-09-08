# Seventh characteristic-p scout: three questions, zero admissions

2026-09-08 UTC. The three bounded mechanisms are genuinely different, but
none supplies a fourth or fifth paper contract in this pass. The strongest
arithmetic lead remains an already-owned finite-field Painlevé conjecture;
it is not proved here. The only complete new hand calculation is an
elementary negative certificate for Nagata return data.

| Entry | Mechanism and full question | Outcome |
| --- | --- | --- |
| P7 | Root-of-unity q-Painlevé I: all-parameter uniform native-period bound | `PARK_SOURCE_OWNED_CONJECTURE`; fibration/exceptional-fibre proof absent |
| N7 | Nagata finite additive action: can all finite-extension ordinary return data detect wildness? | Complete negative hand answer; `REJECT_SHORT_CLASSICAL_RECONSTRUCTION` |
| R7 | Reversible characteristic-two soliton scattering: exact temporal fixed counts on every finite ring | `NO_NEW_FULL_COUNT_PROOF / WEAK_ROUTE_A_ARITHMETIC`; no admission |

These are three source-first screens, not three deep all-parameter proof
attempts. N7 alone received a short complete hand certificate after freezing;
P7 and R7 received source/feasibility checks, not large proofs or censuses.
The early Markoff locator is excluded as a repository duplicate, not a
fourth frozen candidate. M1/AS2/IR1 and every earlier decision are unchanged.

## 1. P7: the most relevant surviving question is still unclosed

**Exact object.** For every prime power $q$, $s,t_0\in\mathbb F_q^*$ and
$r=\operatorname{ord}(s)$, the torus formula is

$$
S_s(x,y,t)=\left(\frac{t}{x-s^{-1}y},\frac{sx}{y},st\right).
$$

The domain is not the torus alone. It is the disjoint union of phase spaces
$X_{t,s}(\mathbb F_q)$ for $t\in t_0\langle s\rangle$, each represented by
one copy of $(\mathbb F_q^*)^2$ and four separately tagged copies of
$\mathbb F_q$. The exact, everywhere-defined seven-branch update, including
every exceptional-line state, is fixed in
[P7's frozen definition](FROZEN_CONTRACTS.md). One update is the native
clock. Ordinary fixed states, if counted, are
$N(n)=\#\operatorname{Fix}(S_s^n)$; neither scheme multiplicities nor
Frobenius point counts are the observable.

**Single full question.** Does every native least period $\ell$ satisfy
$\ell/r\le q+1+2\sqrt q$ for every allowed field and parameter?
No restriction to generic invariant fibres or bounded phase order is part
of this question. The ratio is bookkeeping for the phase clock, not a
replacement for native time.

**Ownership and decisive check.** The map, resolved domain, invariant and
bound conjecture belong to Joshi–Roffelsen. The accessed v2 body explicitly
separates Theorem 3.1 from Conjectures 1.2 and 3.6. The abstract's stronger
wording is not accepted as a substitute proof. Relevant source sections,
publication-access limits and the later-paper check are in
[the P7 source receipt](SOURCE_AUDIT.md).

**Residual mathematical increment.** A proof must control actual invariant
dynamical fibres and all exceptional orbits uniformly. A spectral equation
whose quotient looks elliptic does not, by itself, give a birational
identification with those fibres. Generic smooth-fibre point bounds alone
do not account for every singular or reducible fibre and any component
permutation. No such bridge is proved here. In particular, the existence of
a monodromy invariant does not itself close the full period question.

This remains the best candidate by intrinsic finite-field arithmetic and
native nonlinear dynamics, not by demonstrated tractability. Replacement
boundary: without a new all-parameter geometric mechanism, stop; do not
turn an invariant, a low-order genus calculation, or a few small fields into
a smaller paper. No new P7 mathematical execution occurred.

## 2. N7: complete ordinary data are blind to this proposed distinction

**Exact object and question.** For every prime $p$, $e\ge1$, $Q=p^e$, put
$\Delta=xz+y^2$ and use

$$
\mathcal N(x,y,z)=(x-2y\Delta-z\Delta^2,y+z\Delta,z)
\quad\text{on }\mathbb F_Q^3.
$$

One application is the native clock; all distinct ordinary fixed points of
$\mathcal N^n$, every $n\ge1$, and their cycle multiplicities are the
observable. The question is whether this full all-extension return data
can distinguish Nagata from tame polynomial automorphisms, not whether the
characteristic-zero Nagata automorphism is tame.

**Cheap decisive hand result.** The frozen family $\mathcal N_a$ preserves
$\Delta$ and obeys $\mathcal N_b\mathcal N_a=\mathcal N_{a+b}$, hence
$\mathcal N^p=\mathrm{id}$. The complete result is

$$
f_p(Q)=\begin{cases}Q^2,&p\ne2,\\2Q^2-Q,&p=2,\end{cases}
\qquad
\#\operatorname{Fix}(\mathcal N^n)=
\begin{cases}Q^3,&p\mid n,\\f_p(Q),&p\nmid n.\end{cases}
$$

There are $f_p(Q)$ fixed points and $(Q^3-f_p(Q))/p$ cycles of length $p$,
with no other lengths. For odd $p$, the tame shear $(x+y,y,z)$ has identical
data over every extension. For $p=2$, the tame shear $(x+yz,y,z)$ does too.
Each comparator is fixed independently of $e$ and $n$.
The proof, including both characteristics and the full zeta, is in
[the author proof package](PROOF_PACKAGE.md).

**Ownership and residual increment.** Maubach–Willems already own exact
finite-field tame mimicking of Nagata, allowing the mimicking map to depend
on the extension. That is not literally the same quantifier as one
comparator matching cycle types over all extensions; the hand proof
addresses the latter precisely. Nevertheless, its dependency is just the
classical additive action plus a quadratic fixed-locus count. This is a
short rejection certificate, not an independent substantial paper.

Ordinary finite-field data are finite. The ambient geometric fixed scheme
can have positive-dimensional components, so its scheme length is not a
substitute observable. Replacement boundary: no pivot to a new
scheme-theoretic wildness problem under the same contract. N7 is rejected.

## 3. R7: exact nonlinear model, but no new all-size count theorem

**Exact object.** Fix characteristic two. For every $L\ge2$, let
$X_L=\mathbb F_2^{2L}$ with indices modulo $2L$ and
$\chi(a,b,c)=a+b+c+ac$. Let $E_L$ simultaneously replace each even site
by $\chi(x_{i-1},x_i,x_{i+1})$, leaving odd sites unchanged. Define $O_L$
by exchanging even and odd. The map is

$$U_L=O_L\circ E_L.$$

Each half-step is an involution because its neighbours are unchanged and
the centre is toggled by the same quantity twice. Thus $U_L$ is a
permutation. Its native time is a full even-then-odd sweep. It is not the
synchronous elementary rule numbered 54 and not a spatial translation.
The ordinary observable is $A_L(n)=\#\operatorname{Fix}(U_L^n)$ for every
$n\ge1$. If expressed as a scheme, the domain includes $x_i^2=x_i$ and
is reduced; ambient affine fixed-scheme multiplicities are irrelevant.

**Single full question.** Prove an exact structural formula for every
$A_L(n)$ by a complete soliton/scattering parametrization, including mixed
species, collisions, symmetries and shorter-period stabilizers. The
tautological identity $A_L(n)=\operatorname{tr}(P_L^n)$ for the full
$2^{2L}$-state permutation matrix does not satisfy the substantial target.

**Ownership and decisive source check.** Existing sources own RCA54,
soliton scattering and proposed finite-size Bethe quantization. The 2019
main text's completeness language must be read with the supplement's
small-sector extrapolation and numerical-validation statements. That
source discrepancy is documented, not repaired by assumption. The 2021
stochastic-boundary spectrum and the 2026 protected translation sector
answer different questions. See [the R7 source receipts](SOURCE_AUDIT.md).

**Residual increment and replacement boundary.** Any worthwhile count
result would need a rigorous, complete finite-ring parametrization with
multiplicities after deducting the known formulas. None is proved here.
Even such a theorem has a weaker present Route-A case than P7: this screen
has only characteristic-two Boolean arithmetic, with no variable-prime,
number-field or target-Euler mechanism. The entry is not admitted. We do
not replace all configurations by a one-way soliton sector, or lift the
same Boolean polynomial to other primes merely to manufacture arithmetic.

## 4. What was done and what remains

The [frozen objects](FROZEN_CONTRACTS.md) precede the hand checks;
the [proof package](PROOF_PACKAGE.md) contains exactly the complete N7
negative answer and honest P7/R7 gap reports;
the [source audit](SOURCE_AUDIT.md) records actual accessed sections,
access failures, collision scope, 36 distinct query formulations and
39 submissions, including one repeated three-query block.

`henon-route-a-batch` set the substantive admission threshold;
`research-lit`, `idea-creator` and bounded ARS source verification led to
the explicit conjecture/proof and boundary/periodic distinctions.
`proof-writer` kept the sole hand result complete across characteristic
two and all finite extensions. Internal authorship is not external peer
review. The coordinator retains all global admission authority.

This lane executed zero mathematical programs, old reruns, GPU jobs or
paid model API calls; it performed no Git mutation or manuscript build.
It wrote only four Markdown files in this assigned directory. No new
paper, PDF, formal evaluation or A2 evidence was created. Maintain
`NO_BAD_EULER_OR_ROOT_NUMBER`.

The safe next research move, if continued by the coordinator, is a
separately bounded all-parameter geometry check for P7, with the already
owned conjecture and the actual missing fibre argument frozen unchanged.
This report does not authorize or claim that continuation has happened.
