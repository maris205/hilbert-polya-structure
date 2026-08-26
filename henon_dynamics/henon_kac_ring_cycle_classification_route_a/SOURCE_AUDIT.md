# C170 source audit

## Frozen source

- Candidate: `HCS-C170`.
- Source commit: `ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f`.
- Family: every \(N\ge1\) and every marker word \(\varepsilon\in\{\pm1\}^N\).
- Phase space: \(\mathbb Z/N\mathbb Z\times\{\pm1\}\).
- Map: \(T(j,s)=(j+1,\varepsilon_j s)\).
- Clock: one site advance using the marker at the departed site.
- Normalization: labelled states, then exact periods and geometric cycles.
- Determinant convention: finite Artin--Mazur zeta and the same-clock Koopman determinant.

The only family invariant used is \(\eta=\prod_j\varepsilon_j\), derived from the frozen marker word. No parameter is fitted.

## Evidence population

This source-locked theorem note has no external citation and makes no novelty or priority claim. Citation and reference registries therefore both have population zero. The producer exhausts all 2,046 marker words for \(N\le10\) and records class formulas through \(N=24\); those rows are regression sentinels, while the theorem covers every \(N\) and marker word by proof.

## Scope firewall

`NO_BAD_EULER_OR_ROOT_NUMBER` is literal. No target zero/prime table, arithmetic local datum, Euler factor, root number, automorphy input, Hilbert--Pólya construction, or Route-B input is used. The finite kinetic system is not promoted to a target determinant.

## Mandatory seven-mode integrity audit

Stage 2.5 (after theorem/evidence design):

| Mandatory mode | Verdict | Evidence |
|---|---|---|
| Implementation bug | CLEAR | independent enumeration recomputes cycles, fixed counts, configuration digests and both reversal identities |
| Hallucinated citation | N/A/CLEAR | citation and reference populations are both zero; no literature attribution appears |
| Hallucinated experimental result | CLEAR | all finite metrics come from deterministic exhaustive enumeration; no physical/statistical experiment is claimed |
| Shortcut reliance | CLEAR | the all-size/all-marker result follows from the \(N\)-step law and gauge proof, not the \(N\le10\) sentinel |
| Bug-as-insight | CLEAR | no failed classification is promoted; mutations are rejection tests only |
| Methodology fabrication | CLEAR | producer, independent checker, SymPy, replay, mutation and build commands are released and executable |
| Frame-lock | CLEAR | the finite reducible model is permitted to fail A0 and the overall primary-candidate gate |

Stage 4.5 (after manuscript and release assembly) repeated the same seven modes. Implementation bug remains CLEAR after 114,056 independent assertions, 221 SymPy checks, exact byte replay and 17/17 mutation rejections. Citation remains N/A/CLEAR at zero population. Experimental-result hallucination, shortcut reliance, bug-as-insight and methodology fabrication remain CLEAR because released artifacts regenerate every finite metric and the circuit/gauge proofs carry the infinite quantifiers. Frame-lock remains CLEAR because the final paper keeps `A0_FAIL` and `ROUTE_A_REJECTED` while preserving the exact cycle theorem only as scoped progress.
