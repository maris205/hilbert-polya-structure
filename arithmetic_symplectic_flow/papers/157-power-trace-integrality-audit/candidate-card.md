# Analytic-owner card — ASFS-20260915-PTI01

Version 1, 2026-09-15. Frozen before the asymptotic and spectral audit.
Initial status: OPEN — EXACT POWER-TRACE REALIZATION QUESTION.

This is a new analytic contract, not a new geometric construction or a
retroactive change to 153. Its sole question is whether the exact full-map
flat traces below can be ordinary traces of all positive powers of a
single Hilbert trace-class operator.

For all integers n>=2 and phases 1<=k<=K_n, freeze
\[
K_n=\max(1,\lfloor\log_2(n-1)\rfloor),\qquad
b(n,k)=\sum_{\substack{2^k\le d<2^{k+1}\\d<n}}1_{\{d\mid n\}},
\]
\[
f_{n,k}(q)=q+\tfrac12\tanh q+K_n b(n,k),\qquad
F(n,k,q,p)=(n,k^+,f_{n,k}(q),p/f'_{n,k}(q)).
\]
The full symplectic base is M=coproduct_{n,k} R^2 with omega=dq wedge dp.
The roof is tau=1, the suspension is (M times [0,1]) with (x,1)~(Fx,0),
and its flow uses the unit translation clock. No component, phase, or
real state is removed.

| Field | Frozen owner / question |
| --- | --- |
| Lineage | Proper-divisor symbolic exclusion -> local witness drift -> cotangent conservative geometry -> full-map flat-trace audit |
| Arithmetic input | All integer divisibility tests; no selected prime tables, prime-log roofs, zero data or fitted weights |
| Full geometric comparator | [153](../153-saturated-sieve-flat-trace/paper.md); restate and check the exact return-count formulas before using them |
| Primitive/repetition target | One least-period K_p cycle per prime, full K_p section multiplicity; repeat r has time rK_p |
| Existing test-section operators | U_j=F* on C_c^infinity(M;Lambda^j T*M), j=0,1,2; U_{j,s}=e^{-s}U_j |
| Exact scalar target | T_0(m)=N_m/B_m, B_m=(3/2)^m+(2/3)^m-2, N_m=sum_{p:K_p divides m}K_p, every integer m>=1 |
| Optional natural-form targets | T_2(m)=T_0(m), T_1(m)=N_m+2T_0(m); no alteration of weights |
| Existential analytic owner | A complex Hilbert space H and bounded trace-class A on H, with tr(A^m)=T_0(m) for every m>=1; H and A OPEN at freeze |
| Strength of question | Abstract exact sequence realization is necessary for any trace-class completion realizing these same traces, but is not by itself sufficient for geometric ownership |
| Central normalization | d_0(z)=exp(-sum_{m>=1} T_0(m) z^m/m), the germ from 153 with z=e^{-s}; test ordinary det(I-zA), not a regularized determinant |
| Permitted audit | Exact dyadic prime counts, proper-divisor remainder estimate, prime number theorem, compact/trace-class spectral obstruction |
| Controls | Exact small m and dyadic endpoints; finite-rank integer-multiplicity model; oscillatory peripheral eigenvalues; damping and other-owner boundaries |
| Stop condition | Prove a contradiction for all trace-class A, or report OPEN/refuted hypothesis promptly; no changed roof, state restriction, damping or matrix fitting to rescue this contract |
| Other analytic frameworks | Distributional/local traces, non-trace-class operators, other regularized determinants and local meromorphic frameworks are outside the existential trace-class claim |
| Later owner | Hamiltonian/contact/quantum owner NOT SUPPLIED |
| Route | Limited owner-level analytic audit; formal Route coordinates UNASSIGNED; Route B NOT INVOKED |

The leading-asymptotic/integral-multiplicity obstruction is a hypothesis at
freeze, not a theorem. The source clocks remain the rounded K_p clocks,
and the generic constraint-engineering limitation remains unchanged.

## Appended outcome — version-1 tuple unchanged

**Status:** STOP — EXACT FULL FLAT-TRACE SEQUENCES HAVE NO HILBERT TRACE-CLASS POWER REALIZATION.

The [paper](paper.md) proves N_m/2^m -> 1/log 2 and the corresponding
scalar/two-form (4/3)^m and one-form 2^m normalized trace limits.
A finite positive leading coefficient of ordinary trace-class powers
must be an integer algebraic multiplicity. Since 1<1/log 2<2, no
Hilbert trace-class operator can realize any one of these exact
all-powers sequences. The ordinary fixed-operator determinant germ is
also excluded. The proposed H and A therefore do not exist under
the frozen exact-trace requirement.

This is an analytic stop, not a change of geometry or a negation of
153's distributional flat trace and graded identity. More general
regularized/local frameworks remain outside this theorem. Formal
coordinates remain UNASSIGNED; Route B NOT INVOKED. Portfolio: stop
this contract and retain the obstruction as a control.
