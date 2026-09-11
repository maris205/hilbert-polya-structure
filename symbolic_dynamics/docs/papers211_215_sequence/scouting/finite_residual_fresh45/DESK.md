# Fresh45: constrained combinatorial restrictions

Author: `current_round_two_seats_scout`. **NO NOMINATION / zero count change.** Three desk attempts, no scientific code or pilot, no independent review, no central edits, no Git. The strongest restriction below has evaluated temporal and inverse formulas, but its mechanism subtraction does not justify a paper-sized advance. Literal ownership alone is not the reason for closing it.

## Screening several finite maps

| Attempt | Literal finite carrier and update | Desk result and disposition |
|---|---|---|
| A: restricted pop-stack | The $321$-avoiding permutations $\operatorname{Av}_n(321)$; simultaneously reverse every maximal decreasing run. | Developed below: exact pointwise sorting time, all-target Fibonacci-product fibre formula, unique maximum. Source subtraction reaches threshold shadows and inverse run cuts, not just the literal rule. No material residual advance established. |
| B: diagonal Ferrers deletion | All partitions in an $m\times m$ box; delete first row and first column: $Q(\lambda)_i=\max(\lambda_{i+1}-1,0)$. | Both axes evaluate immediately from diagonal translation and two independent border choices; proof below. Too elementary to nominate. |
| C: parallel equal-letter cancellation | All words of length at most $N$ on $q\ge2$ letters; replace each maximal constant run by one copy if odd and by the empty word if even, then concatenate. | A genuinely length-changing finite rewrite, but the available sharp worst clock and empty-target count are elementary. No evaluated arbitrary-target/pointwise temporal package established; do not upgrade a special fibre into the missing axis. |

These are three desk attempts, not three independently reviewed candidates. B and C stop on their explicit proof-value/missing-theorem limitations, without a claim of exhaustive source subtraction.

## A. Claim, assumptions, and proof status

Fix $n\ge1$. Write permutations in one-line notation. Avoidance is classical: there are no indices $i<j<k$ with $w_i>w_j>w_k$. Let $P$ reverse maximal decreasing runs simultaneously. Define $h(w)=\min\{t\ge0:P^t(w)=12\cdots n\}$.

**PROVABLE AS STATED (author derivation, not independently reviewed):** the temporal and inverse formulas below. **NOT CURRENTLY JUSTIFIED:** that they constitute a materially new two-axis research contribution after subtraction.

Strategy/dependency map: avoidance gives disjoint adjacent swaps and invariance; threshold projection gives binary exclusion; crossing dependencies give a closed time formula. For inversion, avoidance gives eligible swaps, maximality gives descent coverage, and inclusion–exclusion over a path gives an evaluated fibre count. These proof dependencies do not invoke a pilot.

### A1. Closure and exact temporal formula

For each $1\le k<n$, let $p_{k,1}<\cdots<p_{k,k}$ be the positions in $w$ occupied by values at most $k$. Then

$$h(w)=\max\left(\{0\}\cup\{p_{k,j}+k-2j:1\le k<n,\ 1\le j\le k,\ p_{k,j}>j\}\right).$$

Consequently $\max h=n-1$, attained by $23\cdots n1$ for $n\ge2$; for $n=1$ the maximum is zero. The identity is the only recurrent state.

**Proof.**

1. A $321$-avoider has no decreasing run of length three, so $P$ swaps precisely its disjoint adjacent descents. A swap of an adjacent inverted pair removes the inversion of that pair and changes no other pair's relative order. A decreasing triple in the result would therefore already have existed before the swap. Disjoint swaps preserve avoidance, proving that the carrier is invariant.

2. Replace values at most $k$ by $0$ and larger values by $1$. Every adjacent $10$ is an adjacent descent of the permutation. It cannot overlap another descent because there is no decreasing triple. All other swaps exchange equal projected bits. Therefore projection commutes exactly with simultaneous binary $10\mapsto01$. This is equality on the restricted carrier, not an asserted equality for unrestricted pop-stack.

3. In a binary word with $k$ zeros, number zeros from left to right. The $j$th zero has $a_j=p_{k,j}-j$ ones initially to its left, with $a_1\le\cdots\le a_k$. Number the ones from left to right. For $1\le r\le a_j$, zero $j$ must cross one $r$. That crossing waits for zero $j$ to cross one $r+1$, when present, and for zero $j-1$ to cross one $r$, when present. Once those crossings have occurred, this one and zero are adjacent: all intervening zeros or ones have crossed by their preserved internal orders. They cross on the next update. Thus the crossing time is one plus the maximum of the existing two predecessor times, taking the maximum of no predecessors as zero.

4. Induction on these dependencies gives

$$T(j,r)=\max_{1\le i\le j:\ a_i\ge r}(a_i-r+1+j-i).$$

Indeed the predecessor in the same row supplies the terms with $a_i\ge r+1$, and the preceding-zero predecessor supplies the terms with $i<j$ and $a_i\ge r$; the initial boundary term is the remaining $i=j$, $a_j=r$ case. When $a_i=r$ but $a_j>r$, its term is dominated by the term with $i=j$ or by the preceding-zero contribution, so the displayed maximum satisfies the recurrence at every boundary. Equivalently it is the longest directed path through the existing crossing cells. Zeros with $a_j=0$ never move. If there is any inversion, the last zero has $a_k>0$, and its final crossing occurs at

$$T(k,1)=\max_{i:a_i>0}(a_i+k-i)=\max_{i:p_{k,i}>i}(p_{k,i}+k-2i).$$

Every earlier zero finishes no later, as the formula with $j<k$ only decreases the corresponding terms and restricts their index set. This is the exact binary sorting time.

5. A permutation is the identity exactly when every threshold word is sorted. Taking the maximum of the binary times proves the stated formula. Since $p_{k,j}\le n-k+j$, each term is at most $n-j\le n-1$. For $23\cdots n1$, use $k=j=1$ and $p_{1,1}=n$. Finally each nonidentity has a descent, so inversion number strictly decreases at every nonfixed update; no other recurrent state exists. ∎

### A2. All-target inverse formula and sharp fibre

Fix $y\in\operatorname{Av}_n(321)$. Let $D=\{d:y_d>y_{d+1}\}$ and define eligible ascent indices

$$E=\{i:y_i<y_{i+1},\quad y_{i+1}>\max_{r<i}y_r,\quad y_i<\min_{r>i+1}y_r\},$$

where an empty exterior imposes no condition. View $E$ as vertices in the path of indices $1,\ldots,n-1$, with consecutive indices adjacent. For $J\subseteq D$, put

$$E_J=E\setminus\bigcup_{d\in J}\{d-1,d+1\}.$$

Let $\mathcal L(E_J)$ list the lengths of maximal consecutive strings of indices in $E_J$. With Fibonacci numbers $F_0=0,F_1=1$, the complete restricted fibre is

$$|P^{-1}(y)\cap\operatorname{Av}_n(321)|=\sum_{J\subseteq D}(-1)^{|J|}\prod_{\ell\in\mathcal L(E_J)}F_{\ell+2}.$$

Empty products equal one. This gives zero fibres as well as positive fibres without an unevaluated transfer matrix. Moreover the unique maximum over targets is $F_{n+1}$, attained at the identity (also valid for $n=1$).

**Proof.**

1. Every predecessor is obtained by swapping a set $M$ of nonconsecutive ascents of $y$, because forward decreasing runs have length at most two. Consider such a swapped ascent $a<b$. It creates the inverted pair $b,a$. A new decreasing triple must contain a newly inverted pair. A triple cannot contain two disjoint newly inverted pairs, so it contains one swapped pair and one exterior value. It exists exactly when some earlier value is greater than $b$ or some later value is smaller than $a$. The other disjoint swaps do not change which values lie outside this pair. Thus the reconstructed permutation avoids $321$ exactly when $M\subseteq E$.

2. The selected edges are descents in the reconstructed permutation. An unselected ascent of $y$ remains an ascent: a neighbouring selected swap can only decrease its left endpoint or increase its right endpoint. A descent $d$ of $y$ remains an unwanted descent if neither neighbouring edge is selected. If $d-1$ is selected, its new left endpoint is a suffix minimum and hence is below the right endpoint; if $d+1$ is selected, its new right endpoint is a prefix maximum and hence exceeds the left endpoint. These conclusions also hold when both neighbours are selected. Therefore $P(x)=y$ exactly when the independent set $M\subseteq E$ meets $\{d-1,d+1\}$ for every $d\in D$.

3. Apply inclusion–exclusion to uncovered descents. Requiring each $d\in J$ to be uncovered forbids precisely its eligible neighbours, leaving the path-induced set $E_J$. Independent sets on a path of $\ell$ vertices are counted by $F_{\ell+2}$: splitting on its last vertex gives $I_\ell=I_{\ell-1}+I_{\ell-2}$, with $I_0=1,I_1=2$. Components are independent. This proves the formula and the predecessor bijection.

4. Every fibre injects into all independent sets on the full path with $n-1$ vertices, giving the bound $F_{n+1}$. At the identity all indices are eligible and there are no descent constraints, so equality holds. Any nonidentity has a descent index outside $E$, and the singleton containing that index is a full-path independent set absent from its fibre encoding. Its count is strictly smaller. ∎

Sanity example by hand only: for $y=1324$, $E=\{1,3\}$ and $D=\{2\}$. The three allowable nonempty subsets give predecessors $3124,1342,3142$; the formula is $4-1=3$. This is not an enumeration run.

### A3. Actual subtraction and remaining value boundary

Local original read: `docs/papers157_161_sequence/scouting/combinatorial/SCOUT.md`, PPS section, lines 216–230. It already identifies unrestricted descending-run reversal and the worst-clock/image directions. The present avoidance restriction was not dismissed merely because PPS exists.

Primary paper: Asinowski, Banderier and Hackl, *Flip-sort and combinatorial aspects of pop-stack sorting*, DMTCS 22:2 (2021), [journal](https://dmtcs.episciences.org/7411), [primary PDF](https://arxiv.org/pdf/2003.04912). Selected actual PDF text was read: definition and prior bounds on printed pages 2–3; image-definition passage on page 6; inverse run-cut construction on pages 19–20; threshold shadows, binary swaps and comparison framework on pages 25–28. The paper supplies both relevant proof primitives. Its Theorem 14 concerns layered targets, not arbitrary $321$-avoiding targets, so it is not cited as the exact fibre theorem above. Its threshold framework is likewise not cited as the exact equality formula for this restriction.

Residual content is the exact equality of threshold dynamics under avoidance and the eligibility test combined with path counting. Those are proved here, but their mechanisms are short specializations plus elementary inclusion–exclusion. The worst $n-1$ bound and identity's layered small-block fibre provide no separate novelty credit. The desk has not established a sufficiently material advance beyond those owned routes; **do not nominate**. This is a value/source-boundary conclusion, not a claim that the precise displayed formulas were found verbatim in a source or that no publishable theorem could ever exist on this restriction.

Source limitations: the journal PDF initially opened, but later journal find/open requests failed (including timeouts); direct arXiv PDF opens supplied the selected text. Failed text-find queries do not establish absence of a topic. An initial broad local search truncated and served only as navigation; only the stated original passage is used here. No immutable web capture or full literature audit is claimed. Related bypass-stack search hits concern a different map and do not subtract this theorem.

## B. Short complete calculation: Ferrers diagonal deletion

For a partition $\lambda$ in an $m\times m$ box, induction gives $Q^t(\lambda)_i=\max(\lambda_{i+t}-t,0)$, taking missing parts as zero. Hence the first time at the empty partition is the Durfee size $\max\{d:\lambda_d\ge d\}$, with value zero for the empty partition. This reaches $m$ on the full square. All nonempty states lose cells and the empty partition is the sole recurrent state.

For a nonempty target $\mu$ of length $r$ and largest part $c$, a predecessor exists only if $r,c\le m-1$. Every predecessor is uniquely

$$\lambda=(a,\mu_1+1,\ldots,\mu_r+1,1^b),\qquad c+1\le a\le m,\quad0\le b\le m-r-1.$$

Thus its fibre has $(m-c)(m-r)$ members. The empty target has the empty predecessor plus the $m^2$ hooks $(a,1^b)$ with $1\le a\le m$ and $0\le b\le m-1$. For $m=0$ only the empty state exists. These claims are **PROVABLE AS STATED**, but diagonal translation and two free border parameters exhaust the content; there is no material residual mechanism to nominate.

## C. Short partial calculation: equal-letter cancellation

Every nonfixed update removes at least two letters. Therefore every word of length at most $N$ stabilizes in at most $\lfloor N/2\rfloor$ updates. For $N=2m$, take a length-$m$ alternating word $u$ and concatenate its reversal: $u u^{\rm rev}$. Only the central pair cancels on each update, so exactly $m$ updates occur. The same word lies in the carrier for $N=2m+1$. For $N\le1$ the bound is zero. Fixed words have no equal adjacent letters; no nonfixed cycle exists because length decreases.

Among words of exact length $2m>0$, the one-step empty fibre comprises precisely words whose maximal run lengths are all even. Compress every pair inside each run. This is a bijection with arbitrary length-$m$ words on the same alphabet, giving $q^m$ predecessors. No odd-length word maps directly to empty. These special claims are **PROVABLE AS STATED**. A pointwise sharp clock and evaluated all-target inverse formula have not been supplied. The length potential and pair-compression fibre alone do not meet the two-axis bar, so this attempt stops without pilot.

## Final verification and open risks

All mathematical claims here are author proofs with boundary cases; no empirical all-size inference is made. A's inclusion–exclusion is a closed finite formula, but calling it evaluated does not by itself establish research significance. B's two-axis calculation is deliberately retained as a negative control for that distinction. C does not claim the missing general theorem. No accepted-review status, additional seat, or permission for external release follows. HOLD_EXTERNAL remains in force.
