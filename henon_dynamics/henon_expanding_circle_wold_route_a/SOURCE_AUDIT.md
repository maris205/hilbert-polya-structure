# C177 source audit

## Frozen source

- Candidate: `HCS-C177`.
- Source commit: `100e5f601a0196710d53784bdeef40d2bff89fa8`.
- Evaluator: `flow_systems/skills/route-a-evaluator.md`, v0.2.0, SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Family: every integer \(b\ge2\).
- Map: \(T_b(x)=bx\pmod1\) on \(\mathbb R/\mathbb Z\).
- Clock: one application of \(T_b\).
- Measure: normalized Haar measure.
- Koopman convention: \(U_bf=f\circ T_b\), \(e_m(x)=e^{2\pi imx}\).
- Zeta convention: ordinary Artin--Mazur zeta from finite fixed sets.

The only admissible data are this map, its Haar measure, integer Fourier indices, and exact source-derived identities. No parameter is fitted.

## Evidence and ownership boundary

The paper is a source-locked theorem certificate with citation and reference populations both zero. It makes no novelty or priority claim. The classical object is used as an exact Route-A stress test. Finite evidence covers \(2\le b\le12\), \(1\le n\le12\), \(|m|\le72\), and sharp correlation sentinels through \(n=8\), \(s=4\). These rows test code; written proofs carry all quantifiers.

The inverse-limit natural extension gives a unitary dilation only after changing phase space. It is not relabeled as a physical quantization, as the original Koopman operator, or as a Hilbert--Pólya construction.

## Scope firewall

`NO_BAD_EULER_OR_ROOT_NUMBER` is literal. No target zero table, prime table, arithmetic local data, Euler factor, root number, automorphy input, Route-B input, target divisor, target functional equation, target counting law, or Hilbert--Pólya operator is used or claimed.

## Mandatory seven-mode integrity audit

Stage 2.5 and stage 4.5 use the same seven mandatory failure modes:

| Failure mode | Verdict | Reason |
|---|---|---|
| Implementation bug | CLEAR | independent reconstruction checks all rows, schema and payload hash |
| Hallucinated citation | N/A/CLEAR | citation and reference populations are zero |
| Hallucinated experimental result | CLEAR | all finite metrics are regenerated; no physical experiment is claimed |
| Shortcut reliance | CLEAR | group, Fourier and Cauchy--Schwarz proofs carry the infinite claims |
| Bug-as-insight | CLEAR | rejected mutations are tests, never mathematical evidence |
| Methodology fabrication | CLEAR | producer, checker, SymPy, replay, mutation and release commands are executable |
| Frame-lock | CLEAR | the evaluator is allowed to reject the model and does so at A0 |

At stage 4.5 the audit remains CLEAR after 3,980 independent assertions, 3,927 SymPy checks, exact byte replay, and 19/19 mutation rejections. Internal drafting audits are not external peer review or an independent error process.
