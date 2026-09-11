# Algebra / finite-field / number-theory scout and kill ledger

**Status:** `SCOUT_COMPLETE / HOLD_EXTERNAL`.

## Outcome

The lane executed eleven raw deterministic finite maps.  The historical
firewall then identified two exact rediscoveries; they remain executable
sentinels but receive no breadth credit.  The resulting ledger contains
**nine genuinely fresh literal systems**, exceeding the requested minimum of
eight:

- one internal promotion: `C01/SFD`;
- one strong but mechanism-colliding reserve: `C02/SST`;
- seven kills; and
- two excluded rediscovery sentinels.

There is deliberately only one recommendation.  The reserve is not a second
paper allocation.

## Exact evidence contract

[`verify_algebra_lane.py`](verify_algebra_lane.py) is a fresh Python
standard-library implementation.  It imports no author, earlier scout, or
paper code and uses no randomness, floating point, CAS black box, or network.
Every displayed finite carrier is completely enumerated.  Reproduce the
canonical transcript with

```bash
cd docs/papers177_181_sequence/scouting/algebra_lane
cmp -s CANONICAL.txt <(PYTHONDONTWRITEBYTECODE=1 python3 verify_algebra_lane.py)
```

The frozen run covers 104 raw parameter boxes, of which 92 belong to the nine
fresh systems.  It evaluates 900,976 labelled transitions in total, 884,933
of them fresh, and makes 1,375,295 exact assertions.  Its transition digest
is

```text
30db71534328fcb0a43b8d0a2ce7acda3fc271808e057b851a5c5adfa6038cc9
```

Enumeration is falsification evidence, not proof and not ownership evidence.

## Permanent ledger

| ID | Literal carrier and update | Exact early signal | Owner/collision pressure | Decision |
|---|---|---|---|---|
| `C01/SFD` | All functions \(f:\mathbb F_p\to\mathbb F_p\); \(T(f)(x)=f(x+f(0))-f(x)\). | For \(p=2,3,5,7\), image towers are \(p^p,p^{p-1},\ldots,1\). Every nonzero target in the time-\(t\) image has \((p-1)^t\) sources, the zero fibre has the complementary mass, height is sharply \(p\), and the computed Jordan inventory has \(p-1\) top \(J_p(0)\)-blocks. | Fixed finite differences and augmentation-ideal nilpotence are classical/A05/P164 zero credit. The current anchor selects every direction and makes each reverse integration unique. | **`PROMOTE_INTERNAL / HOLD_EXTERNAL`.** Sole recommendation; full proof in `THEOREM_SPIKES.md`. |
| `C02/SST` | \(M_n(\mathbb F_q)\); \(A\mapsto A+I\) if \(A\) is invertible and \(A\mapsto A\) if singular. | Eight prime-field boxes verify periods \(1,p\), sharp height \(p-1\), fibres \(0/1/2\), every-time target formula, exact prescribed-root cycle-index coefficients, and all zero-Jordan gap multiplicities. At \((p,n)=(5,2)\): \(625\) states, image \(510\), \(145\) fixed, gaps \(b_1,b_2,b_3,b_4=30,30,30,25\). | Forward reduction is a P166-style statistic-gated central translation; prescribed-eigenvalue counting is Kung--Stong--Morrison territory. | **`RESERVE_STRONG / KILL_IF_MECHANISM_NOVELTY_REQUIRED`.** Not recommended ahead of SFD. |
| `C03/UCT` | \(\mathbb F_{p^2}\), \(p\) odd; zero fixed and \(x\ne0\mapsto x^{p-1}+x^{1-p}\). | Always lands in \(\mathbb F_p\), has exactly fixed points \(0,2\), and height two. A base target \(a\) has \(\mathbf1_{a=0}+(p-1)\nu(a)\) sources, where \(\nu(a)=1\) for \(a^2=4\), \(2\) for nonsquare \(a^2-4\), and \(0\) otherwise. Ten primes through \(31\) pass. | A norm-one quotient followed by trace/discriminant counting is the previous QTS/generalized-cyclotomic region; after it there is no clock. | **`KILL_OWNER_DENSE_QTS`.** |
| `C04/VTM` | \(\mathbb F_p^2\); \((x,y)\mapsto(x+y,xy)\). | Discriminant gives every fibre \(0/1/2\); periods and heights vary with \(p\). | Exact earlier `F01` literal in the P170 replacement lane. | **`REDISCOVERY_SENTINEL / EXCLUDED`.** |
| `C05/ZMI` | Full \(M_n(\mathbb F_p)\); singular matrices go to zero, invertible matrices to \(A^{-1}\). | Image is \(\operatorname {GL}_n\cup\{0\}\), height one, periods \(1,2\), zero fibre equals the number of singular matrices, and every invertible target has one source. Six boxes through \(3\times3\) pass. | Classical inversion plus P150 zero totalization and P103/P168 matrix singular strata. | **`KILL_SHALLOW_CLASSICAL`.** |
| `C06/PCM` | \(S_n^2\); \((x,y)\mapsto(xy,[x,y])\). | Exact graphs through \(S_5^2\) show nontrivial periods and large fibres. | Same word map as prior `NL02/PCW`; changing Heisenberg groups to symmetric groups is a repaint. | **`REDISCOVERY_SENTINEL / EXCLUDED`.** |
| `C07/SPR` | Canonical residues \(0,\ldots,p-1\); zero fixed and \(x\ne0\mapsto x^x\bmod p\). | Fourteen primes through \(43\) have changing fixed counts, periods, heights, and fibre histograms; nontrivial cycles first appear in the pilot at \(p=23\). | Kurlberg--Luca--Shparlinski and Holden--Richardson--Robinson study this literal self-power map and its closed walks. | **`KILL_DIRECT_OWNER`.** |
| `C08/APD` | \(\mathbb Z/p^2\mathbb Z\), returned to the embedded prime field; \(x\mapsto(x-x^p)/p\bmod p\). | Writing \(x=a+pb\), the image is \(b+(a-a^p)/p\bmod p\), so each base target has exactly \(p\) first sources. The induced base dynamics nevertheless has periods \(7\) at \(p=17\) and \(5\) at \(p=31\), with strongly varying heights. | The Fermat-quotient operator is directly owned by arithmetic differential-operator theory; local lifting also meets P157. | **`KILL_DIRECT_OWNER_AND_IRREGULAR`.** |
| `C09/FRD` | \(\mathbb F_{p^2}\); zero fixed and \(x\ne0\mapsto x^p-x^{-1}\). | If \(n=N(x)\ne1\), then \(N(Tx)=(n-1)^2/n\) and the unit coordinate inverts. Zero has \(p+2\) sources; a nonzero target \(y\) has \(0,1,2\) sources according to the roots of \(r^2-(N(y)+2)r+1\). Seven primes through \(19\) pass, but periods and height vary. | Totalized reciprocal and one-dimensional rational quotient sit in P150/QTS/generalized finite-field dynamics. | **`KILL_QUOTIENT_OWNER_DENSE`.** |
| `C10/MOR` | Canonical residues modulo \(p\); \(0\mapsto0\), \(x\ne0\mapsto\operatorname {ord}_p(x)\). | The first fibre of a divisor \(d\mid p-1\) is exactly \(\varphi(d)\); after one step the graph lies on the divisors of \(p-1\). Fifteen primes show periods from \(1\) through \(7\) and heights from \(0\) through \(6\). | The only uniform axis is the classical cyclic-group order census; the residual divisor values have irregular order modulo \(p\). | **`KILL_ARITHMETIC_IRREGULAR`.** |
| `C11/FAC` | Canonical residues modulo \(p\); zero is fixed by convention and \(x\ge1\mapsto x!\bmod p\). | Fifteen primes through \(97\) show height as large as \(20\) and periods \(1,2,3,7\); Wilson gives the fixed endpoint \(p-1\), but no stable census emerges. | P153 already occupies factorial-controlled translation dynamics; the present iteration is weaker and prime-sensitive. | **`KILL_INTERNAL_P153_AND_IRREGULAR`.** |

## Why only SFD is recommended

SFD closes both axes without importing the missing part from an owner:

1. the forward map has a sharp all-\(p\) clock, complete image tower, depth
   census, and full transition Jordan form; and
2. every target at every time has an exact fibre, with a nonuniform zero
   exception explained by state-selected direction words and unique anchored
   lifts.

SST also closes formally, but its forward engine transfers from P166 and its
enumerative engine transfers from the full-matrix cycle index.  Keeping it as
a reserve documents the useful formula without pretending that a second
mechanism survived.
