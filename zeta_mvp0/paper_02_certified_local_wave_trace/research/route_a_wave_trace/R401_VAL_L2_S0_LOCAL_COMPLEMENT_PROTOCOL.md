# R401-VAL-L2-S0 — representative local-complement protocol

Status: prospective implementation-smoke protocol, frozen before execution.

## Purpose and non-claiming boundary

R401-VAL-L1-V2 proves one periodic return in each small root box but does not
exclude zeros elsewhere in the preregistered local Poincare root domain.  L2
tests a proof-producing complement engine before an all-slab production run.
It uses the already frozen normalized Hamiltonian, section, coordinates, and
return equations; it changes no scientific threshold.

The smoke covers only the three representative parameter slabs `S000`,
`S025`, and `S050`, at both 128 and 256 MPFR bits.  A pass is therefore
`PASS_IMPLEMENTATION_SMOKE`, never `PASS_LOCAL_COMPLEMENT`, `PASS_ENDPOINT`,
or `PASS_FULL`.  It cannot promote \(\delta_{\rm tr}\), \(P_0\), a
Hilbert--Polya statement, zeta zeros, or RH.

## Frozen domain

For each representative epsilon slab \(E_i\), let

\[
 B_{\rm loc}=[-0.02,0.02]\times[0.12,0.17]
 \times[-0.08,0.08]\times[0.64,0.69]
\]

in coordinates \((Q_-,Q_+,P_-,T)\).  Let \(X_i\Subset B_{\rm loc}\) be
the exact decimal plan box for the corresponding accepted L1-V2 primary job.
The driver and checker must pin the accepted L1 release provenance, summary,
manifest, independent checker, and postcheck.  At both precisions they must
verify that the requested plan box is contained in the actual outward MPFR
root enclosure and that the full Krawczyk image lies strictly inside the
requested plan box.  The latter locates the accepted L1 root inside the exact
decimal box routed below.  The driver must form an
exact rectangular decomposition

\[
 B_{\rm loc}=X_i\cup\bigcup_{j=1}^{8} C_{ij},
\]

where the eight closed complement boxes are the standard coordinatewise
lower/upper shells.  Boundary overlap is allowed; a gap is not.  The root box
is routed to A4.12 without reevaluation.  Every complement box is resolved by
the validated tree below.

## Energy contraction

Every node first applies interval Newton in the \(Q_+\) coordinate to

\[
 K_\epsilon(Q_-,Q_+,P_-,0)-1=0
\]

inside its own \(Q_+\) interval.  The already required gate

\[
 \partial_{Q_+}K_\epsilon>0
\]

must hold on every Newton enclosure.  An empty Newton intersection licenses
`ENERGY_EXCLUDED`.  Otherwise the contracted interval is an over-cover of all
energy-section candidates and is passed to the flow evaluator.  The archive
must store the pre-contraction interval, point midpoint, energy residual,
derivative enclosure, and Newton image used by any energy exclusion.  Before
intersection, the evaluator adds the prospectively frozen symmetric
construction guard \(10^{-40}\) at 128 bits and \(10^{-75}\) at 256 bits.
This guard is not an acceptance tolerance: it ensures that a checker using
the separately printed decimal enclosures can recompute a conservative
\(m-F/D\) image without losing a terminal formatting unit.

## Validated return exclusion

For a surviving node, CAPD C1 Taylor/Lohner integration encloses the reduced
necessary-return residual

\[
 F=(K_\epsilon-1,\ Q_-(T)-Q_-(0),\
       P_-(T)-P_-(0),\ P_+(T)).
\]

The implementation stores three enclosures:

1. direct interval evaluation \([F]_{\rm dir}\);
2. the mean-value form
   \([F]_{\rm mv}=F(\bar x,E)+[D_xF](X,E)(X-\bar x)\);
3. \(C[F]_{\rm mv}\), where \(C\) is a fixed point matrix computed from
   the midpoint Jacobian.

A node is `RETURN_EXCLUDED` only if a displayed component of at least one of
these enclosures omits zero by more than the frozen logical margin
\(10^{-30}\) at 128 bits or \(10^{-60}\) at 256 bits.  An empty energy-Newton
intersection is accepted only with the same strictly positive gap guard.
Because the center evaluation retains the full
epsilon interval, the mean-value expression covers root-variable dependence
while the parameter dependence remains enclosed in \(F(\bar x,E)\) and
\([D_xF](X,E)\).

`ROOT_CANDIDATE` in a complement node is not silently accepted: it is
archived and makes the smoke fail pending a separate existence/full-return
identity audit.  A zero of the reduced system does not by itself recover the
omitted terminal \(Q_+\) equation.  `UNKNOWN`, `FLOW_FAIL`, depth exhaustion,
and node
budget exhaustion are inconclusive, not evidence for another orbit.

## Tree and hard gates

Unknown nodes are bisected at exact decimal midpoints along the coordinate
with largest width relative to the frozen parent-domain width.  A
non-claiming 128-bit development run on `S000` left two root-boundary boxes
at depth 24, so the prospectively frozen production limits are depth 40 and
20,000 evaluated nodes per `(slab, precision)` tree; the
driver uses no sampled residual as a logical gate.

`PASS_IMPLEMENTATION_SMOKE` requires:

1. all three representative slab trees terminate at 128 and 256 bits;
2. every non-root leaf is `ENERGY_EXCLUDED` or `RETURN_EXCLUDED`;
3. every parent is exactly the union of its two children;
4. the eight initial complement boxes plus the protected L1 box cover the
   complete frozen local root domain in each slab;
5. the producer records only `PASS_S0_PRODUCER`; the milestone remains null
   until the independent checker replays all exact-decimal coverage,
   protected-L1-box, interval-Newton, and displayed separation decisions
   without importing the production driver and writes a passing postcheck;
6. source, protocol, plan, result, and checker hashes agree;
7. both precisions independently cover the same three exact decimal domains
   and reach the same domain-level verdict “every complement leaf excluded”;
   their adaptive leaf partitions and separating components need not agree.

No success fraction below one is rounded into a pass.  Failure to terminate
is `INCONCLUSIVE_S0` and triggers a redesign using the archived bottleneck
statistics before an all-51-slab L2 production is frozen.
