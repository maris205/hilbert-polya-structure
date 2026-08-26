# C175 source audit

## Frozen source

- Candidate: `HCS-C175`.
- Source commit: `100e5f601a0196710d53784bdeef40d2bff89fa8`.
- Family: every `N>=1` and every `0<=k<=N`.
- Map: cyclic synchronous Rule 184, `F(x)_i=x_(i-1)(1-x_i)+x_i x_(i+1)`.
- Clock: one simultaneous update.
- Normalization: labelled sites and right rotation `(rho x)_i=x_(i-1)`.
- Zeta convention: finite-sector Artin--Mazur zeta from labelled fixed points.

No parameter is fitted. Admissible inputs are the local rule, cyclic adjacency, `N`, `k`, and exact combinatorial identities derived from them.

## Evidence population

The manuscript is a source-locked theorem note with no external citations. Citation and reference registry populations are zero. It makes no external novelty or priority claim. The finite ledger exhausts `1<=N<=12`, all 8,190 words, all 90 sectors, and `1<=n<=2N+2`; it is a regression sentinel, not evidence by extrapolation.

## Scope firewall

`NO_BAD_EULER_OR_ROOT_NUMBER` is literal. The package uses no target zero table, prime table, arithmetic local data, Euler factor, root number, automorphy input, or Route-B input. It does not claim a target divisor, target functional equation, target counting law, Weil compression, Hilbert--Pólya operator, external peer review, or independent error process.

## Mandatory seven-mode integrity audit

Stage 2.5, after theorem/evidence design:

| Mandatory mode | Verdict | Evidence |
|---|---|---|
| Implementation bug | CLEAR | independent particle-move checker does not import the producer and recomputes every finite row |
| Hallucinated citation | N/A/CLEAR | citation and reference populations are both zero; no literature attribution appears |
| Hallucinated experimental result | CLEAR | every finite count is regenerated exactly; no physical or statistical experiment is claimed |
| Shortcut reliance | CLEAR | finite rows are sentinels; gap and rotation proofs carry all infinite quantifiers |
| Bug-as-insight | CLEAR | no failed run is promoted; mutations are rejection tests only |
| Methodology fabrication | CLEAR | producer, checker, SymPy, replay, mutation and release commands are package-local and executable |
| Frame-lock | CLEAR | the hostile audit preserves A0 failure, weak A1, full-system nonunitarity, and overall rejection |

Stage 4.5 repeats the same seven modes after manuscript and release assembly. Implementation bug remains CLEAR after 34,545 independent assertions, 25,563 SymPy checks, exact byte replay, and 17/17 mutation rejections. Citation remains N/A/CLEAR at zero population. Experimental-result hallucination, shortcut reliance, bug-as-insight and methodology fabrication remain CLEAR because every released finite metric is reproduced and the proof owns the all-parameter statements. Frame-lock remains CLEAR because the final paper retains `ROUTE_A_REJECTED`, `A4_FORMAL_HINT`, and the no-arithmetic boundary.
