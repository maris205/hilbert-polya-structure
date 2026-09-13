# Paper27 first local build: preserved failure

Status: FAIL_PRESERVED_NO_RETRY

The hash-bound, independently reviewed script was executed once. The tool returned live session 7599, then that same session returned exit 1. There is no live build handle to poll and no restart of this attempt.

- Root r0 completed exactly TeX → BibTeX → TeX → TeX; final R050.status is 0.
- Its PDF is 336,903 bytes / 29 total pages. The unique reference sentinel is 28, giving 27 proof-content pages, within 24–28.
- Final log contains 13 overfull hboxes: 10.99185pt at source line 738; six 17.59975pt and six 33.8701pt boxes in target/reflected-target table rows at source lines 1462–1550. Underfull warnings also remain for later disposition.
- Actual PDF metadata reports Custom Metadata: yes. Read-only inspection identifies `/PTEX.Fullbanner` in Info object 207; creator/producer and epoch dates otherwise match. This is an additional unmet output criterion, not a parser implementation failure.
- r1 was never started. No deterministic two-root PASS or release-grade completion is claimed.

Exact new failure artifacts (relative to project): `build/local-20260905-evidence/failure.json`, `build/local-20260905-evidence/r0/`, and `build/local-20260905-r0/`. They are preserved, not reused or edited. This recorded diagnostic access applies only to this newly created attempt; all older successor/postfail/recovery/build namespaces remain untouched.

PDF SHA256: `c1a9a21e675dc92cc5164a92a2bb855e47f2e832f61e27a2dd0dd57b11469a2b`.
Unchanged original manuscript SHA256: `d60ec6611683cafdf822b4cb493040258dc1dd29502363d493f52c3e2deeed3e`.

Next work is a separately reviewed, semantics-preserving layout copy, not another invocation of this script or reuse of either reserved root. All factual build acceptance criteria stay in force.
