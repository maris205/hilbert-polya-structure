# P117 claims–evidence map

Status: internal proof package; external release, novelty, and priority HOLD.

| Claim | Proof anchor | Independent exact control | Boundary |
|---|---|---|---|
| Boundary survival iff adjacent run parities agree | Lemma 2.2, direct comparison of the two updated endpoint bits | Literal one-step boundary sets for every word through \(n=16\) | Constant words are handled separately |
| Recurrent iff all run lengths have one parity; eventual period at most two | Theorem 2.3, monotone boundary set and direct converse | Every finite orbit through \(n=16\) | For odd \(n\), constants form a two-cycle |
| Exact fixed and two-periodic state counts | Theorem 3.1, even boundary subsets and odd cyclic compositions | Exact census through \(n=16\) | Counts labelled states, not necklaces |
| Odd maximum preperiod \((n-1)/2\) | Theorem 4.1, two-boundary loss and one-even-run family | Exhaustive maxima and witness checks | Includes \(n=1\) |
| Even maximum preperiod \(\lfloor(n-2)/4\rfloor\) | Theorem 5.4, parity eroder, cost-drop lemma, minimal realization | All even-length parity words through length 18 plus exhaustive word orbits through \(n=16\) | Includes \(n=2,4\); mixed patterns start at cost six |
| Zeta formula | Corollary 3.2, routine finite-cycle product | Direct fixed/period-two census | Artin–Mazur bookkeeping is zero-credit |

The two analytic routes are materially different after the common survival
lemma: the odd route counts disappearing run boundaries, while the even
route follows a new cyclic parity word and proves a sharp metric cost drop.
The labelled census is recorded as an enumerative corollary of the temporal
classification, not as an independent run-enumeration contribution.
