# Actual bounded relative-heat-trace review

**Paper ID:** 213-relative-periodic-heat-trace  
**Candidate ID:** AQC-20260916-RHT01  
**Research date:** 2026-09-16  
**Actual final-input review clock:** 2026-09-16 13:45:04 UTC.  
**Reviewer invocation:** `/root/carrier_boundary_audit`.  
**Disposition:** ACCEPT THE EXACT PERIODIC-CHANNEL CONTROL; NO AUTHOR-FILE CHANGE REQUESTED.  
**Candidate status:** CONTROL ADVANCE — RELATIVE PERIODIC-CHANNEL TRACE RECOVERS THE POSITIVE-TIME ORBIT COMB; FULL-STATE TRACE NOT SUPPLIED; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Actual process and final bindings

This is a separately invoked bounded mathematical model review using
the selected model and inherited shared context. It is nonblind, not
human peer review, cross-model replication or an independent-error
certificate. Root's initial assignment supplied a provisional
Hilbert--Schmidt factorization and proposed tail estimates. The reviewer
read the frozen card and recomputed those claims, the normalization,
forward-time convention and limit controls before receiving the author
manuscript. Preliminary feedback included the normalized-measure factor,
the distinction between winding and Fourier indices, and the need for
Gaussian summability in a generic long-circle control. This was visible
author-reviewer exchange, not blind discovery of the construction.

ARS was used only for bounded claim/evidence/reasoning and adverse
controls. The reviewer read its router and argument-builder instructions,
restored the stream guidance and current entry, and read the relevant
205 measure and lost-observation proof at the card stage. No helper
reviewer, full publication pipeline, external model, new candidate,
formal Route or integrated batch check was invoked.

After the final-text-ready notice, the reviewer read the entire 401-line
[paper](../paper.md), [README](../README.md),
[card including appended outcome](../candidate-card.md),
[claim ledger](../claim-ledger.md) and [evidence index](README.md).
The two author-reported pre-notice typographical corrections were
already present in the reviewed text; they are not reviewer revisions.
No final-read mathematical or scope correction was required. An actual
`sha256sum` command then produced these bindings:

| Reviewed core | SHA-256 |
| --- | --- |
| README.md | `91a58294481ea2db7af2a1fe48e18f51af90bd9b651c760b508b0fd66f4845b8` |
| candidate-card.md | `429958df61ff15658bbf943afde4acd713ca84d27cdd0792f326d37536678f1e` |
| paper.md | `5601e2a1a2b5dc47e36f455352c83a42afd618ca118970a1cb67c450d2c692d9` |
| claim-ledger.md | `04553a769987fbbf8fcef73d6e5612d37c9fe6e9f7f93e6971da92f7249ca56b` |

The evidence index is read but remains unbound for root's actual
completion receipt. Its arXiv source is disclosed metadata/abstract
context, not a theorem premise. This review does not certify a full
external-paper read, Anosov hypotheses, novelty or literature coverage.
Only this assigned review file is written by the reviewer.

## Recomputed mathematical obligations

### Frozen geometry, time and normalization

The lengths L_a are the established physical periods of 194's actual
singleton circles, not new roof inputs. The chosen invariant measure
is the explicit 205 circle mixture. Its positive block weights and
normalized circle measures change Hilbert normalization, not the actual
translation or the trace of an intertwined operator. Multiplication by
sqrt(w_a/L_a) gives the stated unitary identification with L2(dr).

The paper correctly uses the periodized kernel relative to ds and
explicitly multiplies it by L when instead integrating against ds/L.
This is the source of the physical-period factor in the trace. It is
not an inserted sampling or prime-power weight.

The Gaussian periodization converges uniformly on a period. Unfolding
the nonnegative convolution and completing the real square prove the
periodic heat composition law. The supplementary Fourier calculation
has the right sign: V_t gives exp(2 pi i k t/L), and the Gaussian
transform satisfies F'=-2 epsilon omega F, F(0)=1. Thus the frozen
multiplier description is verified without using a Poisson theorem
as an unchecked premise.

### Genuine trace-class operators on both specified blocks

On a finite circle, the half-heat kernel is square integrable. Factoring
the heat-translation operator into half heat and translated half heat
gives two Hilbert--Schmidt factors. Their product-trace integral is

    integral_0^L integral_0^L
        K_(epsilon/2,L)(r-u) K_(epsilon/2,L)(u+t-r) du dr.

The proven periodic convolution identity makes the inner integral
K_(epsilon,L)(t), so the trace is L times the full winding sum.
The product is trace class before any diagonal is evaluated.

For the line block, set A=chi_L H_(epsilon/2) and
B=V_t H_(epsilon/2) chi_L. The factors multiply to exactly the
frozen windowed operator because heat and translation commute. Direct
integration gives both squared Hilbert--Schmidt norms equal to
L G_epsilon(0). Their product-trace integral has inner factor

    integral_R G_(epsilon/2)(r-u) G_(epsilon/2)(u+t-r) du
        = G_epsilon(t).

Hence the line trace is L G_epsilon(t), with the actual forward
translation and the stated window. Absolute integrability follows
from the Hilbert--Schmidt Cauchy--Schwarz estimate, not from a formal
diagonal rule for a general bounded operator.

The finite paired subtraction therefore gives precisely the nonzero
winding terms. Removing m=0 winding is not removing Fourier k=0:
their contributions are respectively L G_epsilon(t) and the constant
1. The manuscript keeps that distinction intact.

### Infinite-atom and heat-tail controls

For abs(t)<=T and L>=2T+1, the inequality
abs(t-mL)>=abs(m)L/2 holds for every nonzero integer m. Summing the
resulting Gaussian terms using m^2>=m yields exactly equation (9),
including its prefactor L/sqrt(pi epsilon).

At fixed epsilon the denominator has a strictly positive lower bound.
For 0<epsilon<=1 and L>=1 it is uniformly bounded below by
1-exp(-1/16). Splitting the exponent and using
sup_(x>=1) sqrt(x)exp(-x/32)<4 proves the stated estimate

    epsilon^(-1/2) exp(-L^2/(16 epsilon))
        <= 4 exp(-L^2/32).

Thus the uniform heat-range bound is valid with one constant. The
all-integer comparison converges because for sufficiently large n,
(log n) exp(-c(log n)^2) is at most (log n)/n^3. No prime-counting
asymptotic, finite census or empirical cutoff enters the argument.
These bounds prove local uniform convergence of the paired atom sum
for every fixed positive heat parameter.

For the distribution limit, extending a test function compactly
supported in (0,infinity) by zero gives a smooth compactly supported
function on the line. The Gaussian approximate identity applies at
each fixed winding center. There are only finitely many centers with
abs(m)L<=2T+1 on any fixed circle. For the other windings, the same
split-exponent bound retains m^2 L^2 and yields a summable dominating
sequence uniformly for epsilon<=1. This justifies the full winding
limit, rather than only termwise limits at finitely many repeats.

The remaining atom tail is bounded by a constant times
norm(h)_1 L_a exp(-L_a^2/32), summable independently of epsilon.
Dominated convergence then removes that tail. Negative windings give
no mass on positive test support, and the remaining positive centers
are locally finite. Consequently the ordered limit in equations
(13)--(14) is established. No claim at t=0 or about arbitrary joint
cutoff limits is needed or made.

### Divergent sectors and representation controls

For every fixed epsilon>0 and finite real t, G_epsilon(t)>0 and
sum_a L_a diverges. The covering traces sum to infinity; the circle
traces are at least those same positive zero-winding terms. Separately,
circle constants give an infinite orthonormal sequence preserved by
the direct-sum heat-translation operator. Thus its noncompactness and
the failure of ordinary infinite-sector trace class are genuine.
Convergence of the paired scalar difference does not license an
ordinary infinite graded trace or unpaired infinity subtraction.

Window translation leaves the line integral unchanged, and positive
circle-measure rescaling leaves the circle operator unitarily
equivalent. The generic-circle control supplies the necessary Gaussian
summability hypothesis, with all integer logarithms as a concrete
comparison. It does not infer convergence merely from L_j tending
to infinity, or infer prime specificity from a universal circle-cover
heat mechanism.

## Final scope verdict

All final summary surfaces agree with the proved result: CONTROL
ADVANCE for an exact relative periodic-channel distribution, not a
new full-state trace candidate. The circle-channel representation
already loses a nonzero continuous mixed-state observation. Neither
the successful trace calculation nor hypothetical algebraic padding
repairs that defect, supplies heat in mixed directions or constructs
a trace on exact 204 H. The underlying full geometry itself is not
altered or stripped of mixed states.

The period coefficient and repetitions are genuinely operator-derived
from the declared circle-cover construction, while the arithmetic
period ledger remains an inherited geometric input. Naturalness is
OPEN. No determinant, continuation, target divisor, quantum owner or
formal Route credit follows. Further full-state localization requires
a fresh explicit contract rather than promotion of this control.

The bounded mathematical review is complete for the four hashes above.
Root retains the sole integrated mechanical verification and actual
completion-receipt responsibility.
