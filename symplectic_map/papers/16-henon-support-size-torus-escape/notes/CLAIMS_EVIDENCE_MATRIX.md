# Claims--Evidence Matrix

## Reading key

The matrix separates proved mathematical claims, literature-supported context,
explicit examples, lifecycle statements, and nonclaims.  “Complete proof” means
that the argument is written in `notes/PROOF_PACKAGE.md`; it does not mean that
the source package has passed its still-required independent source review.

| ID | Exact claim | Evidence in this package | External dependency | Assumptions that must travel with the claim | Source-stage status |
|---|---|---|---|---|---|
| D1 | The map is `H(x,y)=(P(x)+ay,x)` with `P(X)=c+sum b_j X^(e_j)` and actual collected support `1<=e_1<...<e_s=d`. | Definitions and inverse formula in `RESEARCH_QUESTION.md` and `PROOF_PACKAGE.md`. | None. | `char K=0`; every `a,c,b_j` is nonzero. | Fixed. |
| D2 | `T_m` consists of initial torus states whose first `m` transitions, hence `m+1` states, remain in `Gamma^2`. | Definition plus scalar-coordinate convention in the proof package. | None. | `Gamma <= K*` has finite rank `r`; finite generation is not assumed. | Fixed. |
| U1 | A nondegenerate `q`-term linear equation in a rank-`R` subgroup has at most `A(q,R)=(8q)^(4q^4(q+R+1))` solutions. | Exact input statement and arbitrary-field bridge in the proof package. | Amoroso--Viada, Theorem 6.2. | Published theorem is over an algebraically closed characteristic-zero field; base extension is explicit. | Verified external input. |
| L1 | If a degree-at-most-`d` polynomial has exactly `q>=2` nonzero terms, then `#{(t,u) in Gamma^2: lambda u=F(t)} <= S_q=d(A(q,2r)+2^q-q-2)`. | Full sparse-image proof: rank-`2r` tuple, power fiber, and all proper zero subsums. | U1 only. | Distinct exponents; nonzero coefficients and `lambda`; characteristic zero. | Complete proof. |
| L2 | Torsion, including infinite torsion, causes no missing fiber in L1. | Rank convention and torsion audit in the proof package. | U1 only. | Finite rank, not finite generation. | Complete proof. |
| L3 | The nondegenerate part of the first local Hénon equation contributes at most `d A(s+2,3r)`. | Rank-`3r` variable tuple and degree-`d` power-fiber argument. | U1. | Coefficients are fixed scalars and need not lie in `Gamma`. | Complete proof. |
| L4 | Every first-local degeneracy belongs to one of four incidence types according to membership of `Z` and `U`: GZ, GU, R0, R1. | Explicit fixed convention `Z=z/c`, `U=-au/c`, `M_j=-b_jv^(e_j)/c`; four-case derivation. | None beyond algebra. | The chosen zero subsum is nonempty and proper. | Complete proof. |
| L5 | Each GZ or GU graph label has at most `S_*` torus points. | The two polynomial term counts sum to `s+1`; the endpoint cases `J=[s]` and `|J|=1` are checked explicitly; apply L1. | L1. | `s>=2`; `c,a,b_j` nonzero. | Complete proof. |
| L6 | R0 has at most `e_maxJ-e_minJ` possible nonzero `v`; R1 has at most `e_maxJ` possible `v`. | Factoring the lowest power in R0 and ordinary degree in R1. | None. | Distinct positive exponents; characteristic zero is more than sufficient here. | Complete proof. |
| L7 | Every fixed root fiber from R0 or R1 contributes at most `S_*` points after the second recurrence. | `w=(c+a rho)+sum b_j z^(e_j)` has `s+1` terms unless its constant cancels, and still has `s>=2` terms when it cancels. | L1. | `s>=2`; all `b_j` nonzero. | Complete proof. |
| L8 | Simultaneous vanishing subsums do not create an omission. | The proof assigns any available zero subset and takes a union over all labels; overlap is intentional overcount. | None. | No disjointness assertion. | Complete proof. |
| C1 / PC1 | For `s>=2`, `#T_2 <= d A(s+2,3r)+M(e)S_*`, where `M(e)` is defined by the two explicit subset sums. | L3 plus L4--L8, followed by the exact label/root sum. | U1 through L1 and L3. | Full D1--D2 assumptions. | Complete author proof; independent review still required. |
| C2 | `M(e)=2^(s+1)-2+sum_k(2^k-2^(s-k))e_k` is a checksum, not its definition. | Max/min subset counting in the proof package. | None. | Ordered distinct exponents. | Complete proof. |
| C3 | `M(e) <= 2(2^s-1)+d(2^(s+1)-s-2)`. | Count of subsets of size at least two and nonempty subsets. | None. | `e_s=d`. | Complete proof. |
| C4 / PC2 | For every prescribed support with `s>=2`, rational nonzero coefficients and a rank-one group give infinite `T_1`. | Direct family `a=b_j=1`, `c=-s`, `Gamma=<2>`, `(1,2^n)->(2^n,1)`. | None. | `n>=0`. | Directly verified example. |
| C5 | The coefficient-uniform finite threshold for `s>=2` is exactly two transitions. | C1 gives finiteness at `T_2`; C4 gives failure at `T_1`. | U1 through C1. | Same class of maps and groups in both statements. | Complete author proof. |
| C6 / PC3 upper | For support one, `#T_4 <= 4d A(3,3r)+81d^2`. | Four possible nondegenerate local indices plus the complete A/B/C automaton for four degenerate labels. | U1. | `P=c+bX^d`, `d>=2`, `a,b,c` nonzero. | Complete reproduced proof. |
| C7 | In the support-one automaton, only `BA` and `CB` are free after two labels; only `CBA` can remain free after three, under `a=-1` and `bc^(d-1)=-1`; every fourth label closes it. | Nine-transition table and the BA, CB, CBA continuation equations. | None beyond algebra. | Same as C6. | Complete reproduced proof. |
| C8 / PC3 sharpness | For every `d>=2`, a number-field rank-one group gives infinite `T_3`. | `c^(d-1)=-1`, `a=-1`, `b=1`, `Gamma=<2,c,-1>`, and scalar chain `t^d,t,c,-t,(-t)^d`. | None. | `t=2^n`; `c` and `-1` are torsion, so the group rank is one. | Directly verified example. |
| C9 | The coefficient-uniform finite threshold for support one is exactly four transitions. | C6 and C8. | U1 through C6. | Support exactly one. | Complete absorbed theorem. |
| B1 | The hypothesis `c!=0` is essential for PC1. | Direct counterexample `P=X^d+X`, `a=-1`, `(t,t^d)->(t,t)->(t^d,t)`. | None. | Infinite `Gamma`; `d>=2`. | Directly verified. |
| B2 | The hypothesis `a!=0` is essential for PC1. | Direct counterexample `P=-1+X+X^2`, `a=0`, `(1,t)->(1,1)->(1,1)`. | None. | Infinite `Gamma`. | Directly verified. |
| N1 | No direct published or posted collision was found for the exact support-size dichotomy and PC1 bound in the bounded search through 2026-08-17. | `CITATION_VERIFICATION.md` and `NOVELTY_ASSESSMENT.md`. | Primary-source search only. | This is a bounded-search report, not a global priority claim. | Provisional novelty GO. |
| P1 | The support-one predecessor is absorbed and must not be submitted in parallel. | Hash-identified provenance in every lifecycle document; full proof C6--C8 is reproduced here. | Local predecessor only. | Later manuscript must disclose provenance appropriately. | Locked lifecycle constraint. |

## Claim combinations that are forbidden

The source package must not silently strengthen the matrix in any of these
ways:

- replacing finite rank by a statement about arbitrary subgroups;
- allowing `a=0`, `c=0`, or a zero displayed `b_j`;
- treating a repeated-exponent presentation as support size `s` before
  collection;
- claiming the constants are optimal or the surviving points effectively
  enumerable;
- turning the bounded novelty search into a priority assertion;
- presenting PC3 as an external citation instead of an absorbed, fully
  reproduced proof;
- claiming a periodic-point classification, affine-conjugacy invariance, or
  positive-characteristic analogue.

## Evidence balance

PC1 is the dominant contribution.  PC2 is the shortest-window obstruction
needed to interpret PC1.  PC3 supplies the fully proved support-one comparison
and absorbs the local predecessor.  All other cited arithmetic-dynamics papers
locate the boundary; none is used to fill a proof step.
