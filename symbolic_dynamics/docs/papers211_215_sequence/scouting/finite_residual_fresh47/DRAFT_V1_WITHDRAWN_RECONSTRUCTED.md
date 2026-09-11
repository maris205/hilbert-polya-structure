# Preservation notice: reconstructed withdrawn V1

This is a reconstruction of the first fresh47 draft from its recorded author edit and subsequent exact corrections. It preserves the erroneous inverse generating function and unexecuted erroneous coefficient-source proposal for review history. It is NOT an immutable original-byte capture, and no raw-byte identity to the first on-disk version is claimed. The inverse formula is withdrawn; use DESK.md for the corrected author proposal. No code in this file has been executed by the author.

---

# Fresh47: exact parallel run-parity cancellation — author proof proposal

Author: `current_round_two_seats_scout`. Scope: follow-up only to fresh45C. **AUTHOR PROOF PROPOSAL / NOT REVIEWED / NOT ADMITTED.** No pilot has run, no count or central-state change is made, and no external release is authorized. Root requested the complete proof and an unexecuted bounded pressure-test source proposal; root has not contributed a proof.

## 1. Literal map, claims, and boundaries

Fix an integer $q\ge1$ and an alphabet $\Sigma$ of $q$ letters. For any fixed $N\ge0$, the carrier is $\Sigma^{\le N}$. Define $R$ simultaneously on the maximal constant runs of a word: replace $a^r$ by $a$ if $r$ is odd and by the empty word $\epsilon$ if $r$ is even, and concatenate the replacements. Do not reduce newly adjacent letters until the next update. This is a finite autonomous deterministic map.

Let $\operatorname{red}(u)$ be the adjacent-equal-pair normal form, obtained by the stack rule: read each letter, remove the top if equal, otherwise push it. Set $h(w)=\min\{t\ge0:R^{t+1}(w)=R^t(w)\}$. For $w=w_1\cdots w_n$, define

$$A_i=|\operatorname{red}(w_1\cdots w_i)|,\qquad C_j=|\operatorname{red}(w_{j+1}\cdots w_n)|\qquad(0\le i,j\le n),$$

$$m=|\operatorname{red}(w)|,\qquad M(w)=\max_{0\le i\le j\le n}(A_i+C_j).$$

**Temporal claim:**

$$\boxed{h(w)=\left\lceil\frac{M(w)-m}{2}\right\rceil.}$$

This is a finite maximum of explicitly evaluated prefix/suffix lengths, not an iteration of $R$, a shortest-reduction optimization, or greedy cancellation-tree depth. The clock's proof below depends on the actual maximal-run parallel schedule.

**Inverse claim:** for every target $y$, Section 3 gives an explicit binomial sum counting its one-step predecessors of every exact length, hence also in $\Sigma^{\le N}$. The generating function depends only on $|y|$ and its number of equal adjacent pairs, not on its particular letters.

Proof status: **PROVABLE AS STATED — author argument pending independent scrutiny.** This label is a proof-writer feasibility assessment, not an accepted mathematical review or a novelty verdict. The two delicate temporal inequalities are isolated below. Source subtraction remains bounded and incomplete; see Section 4.

Boundary cases:

- $w=\epsilon$: $n=m=M=0$ and $h=0$.
- Already reduced words have no equal adjacent letters, are fixed by $R$, and have $M=m$, hence $h=0$.
- $q=1$: the carrier consists of $a^n$. For $n=0,1$, $h=0$; for $n\ge2$, $h=1$. If $n\ge2$ is even, $m=0,M=2$; if $n\ge3$ is odd, $m=1,M=2$. Thus the formula includes this degenerate alphabet without a hidden $q\ge2$ assumption.

## 2. Complete temporal proof

### 2.1 Tree model and proof dependencies

Construct a graph whose vertices are reduced words. A letter $a$ takes a reduced word $u$ to the word obtained by deleting its last letter when that letter is $a$, and otherwise to $ua$. These moves are involutions. Each nonempty vertex has exactly one neighbour of smaller length, obtained by deleting its last letter; its other neighbours have larger length. This graph is a tree: a hypothetical cycle has a vertex of maximal length, whose two neighbours on the cycle would both have smaller length, contrary to uniqueness. It is connected by repeatedly deleting last letters. For $q=1$ it is the two-vertex tree.

The word $w$ traces a unit-edge walk $v_0,\ldots,v_n$ from the empty vertex $s=v_0$ to $t=v_n$. Immediate backtracking occurs exactly at adjacent equal letters. A path in a tree with no immediate backtracking is the unique geodesic between its endpoints: otherwise deleting the common initial segment with that geodesic would produce a nontrivial closed walk without a backtrack, impossible by taking a vertex furthest from its starting vertex. Thus the stack word is the label of the unique endpoint geodesic; deleting equal adjacent pairs preserves the endpoint and this normal form.

Write $a(v)=d(s,v)$ and $c(v)=d(v,t)$. Then $a(v_i)=A_i$, $c(v_j)=C_j$, and $d(s,t)=m$. For the suffix identity, the suffix labels trace the path from $v_j$ to $t$; their reduced labels describe its geodesic and therefore have length $d(v_j,t)$.

All following distances are graph distances in this tree. The dependency chain is:

1. Ordered distance maximum detects a non-geodesic walk.
2. One run-parity update has an order-preserving correspondence moving vertices at most one edge.
3. A peak exposed in the output requires an erased even run in the input, supplying an extra outward edge.
4. These facts force the rounded distance excess to decrease by exactly one until the walk is geodesic.

### 2.2 Detection lemma

For every walk from $s$ to $t$, $M\ge m$, and $M=m$ if and only if the walk is the geodesic from $s$ to $t$.

**Proof.** Taking $i=j=0$ gives $M\ge m$. On the geodesic, $A_i=i$ and $C_j=m-j$, so $A_i+C_j\le m$ for $i\le j$.

Conversely, if any visited vertex $v_i$ lies outside the endpoint geodesic, then $d(s,v_i)+d(v_i,t)>m$, and choosing $i=j$ gives $M>m$. If every vertex lies on that geodesic but the walk is not the geodesic traversal, there is a backwards step, from coordinate $r$ to $r-1$, when the endpoint geodesic is numbered $0,\ldots,m$. Taking $i$ before and $j=i+1$ after that step gives $A_i+C_j=r+(m-r+1)=m+1$. Thus again $M>m$. ∎

### 2.3 First schedule inequality: $M(R(w))\ge M(w)-2$

Let $w'=R(w)$, with output walk $u_0,\ldots,u_k$. Its endpoints are still $s,t$.

Within an input maximal run of one letter, the walk alternates across one fixed edge. If its length is even, its two boundary vertices coincide; the output has no edge there. Map every input vertex of that run to that output boundary vertex. If its length is odd, the output has one edge with the same two endpoints; map all vertices of the run except its final vertex to the output edge's initial vertex, and map the final vertex to its final vertex. Each mapped point is at distance at most one from the original point.

The maps agree at shared run boundaries and concatenate into a nondecreasing map from input vertex indices to output vertex indices. Empty output pieces cause no problem: their boundary indices coincide. Thus for any $i\le j$, their images have indices $p\le r$ and satisfy

$$a(u_p)\ge a(v_i)-1,\qquad c(u_r)\ge c(v_j)-1.$$

Taking a maximizing input pair proves

$$\boxed{M(w')\ge M(w)-2.}$$

### 2.4 Exposed-peak lemma

Consider an interior output vertex $u_p$ which is a strict local maximum of distance to a fixed root $z$ in the same tree. Both neighbouring output vertices are its unique neighbour toward $z$. Hence the incoming and outgoing output edges traverse the same tree edge in opposite directions and have the same letter label $a$.

Each surviving output letter came from an odd maximal run in the input. The two consecutive equal output letters cannot have come from adjacent input runs, since adjacent maximal input runs have different labels. Between the two odd runs there is therefore at least one erased even run. Every such intervening run begins and ends at $u_p$. The first one has label different from $a$, by maximality of the input runs. Its first edge is consequently not the unique edge toward $z$. Its next vertex $x$ has

$$d(z,x)=d(z,u_p)+1.$$

This witness occurs strictly between the input odd runs producing the incoming and outgoing output edges. Witness intervals for distinct output vertex indices occur in their index order. If $u_p$ lies outside the geodesic from $s$ to $t$, its edges toward $s$ and toward $t$ coincide, so such a witness increases both endpoint distances by one whenever $u_p$ is a peak toward both endpoints. ∎

### 2.5 Second schedule inequality: if $M(w')>m$, then $M(w)\ge M(w')+2$

Choose a maximizing output pair $0\le p\le r\le k$, so

$$a(u_p)+c(u_r)=M(w')>m.$$

First suppose $p<r$. The index $p$ cannot be zero: if $p=0$, then $c(u_r)>m$, and replacing $p$ by $r$ adds the positive quantity $a(u_r)$, contradicting maximality. The neighbour $p+1$ is admissible as the first index because $p+1\le r$. Neither neighbour of $u_p$ can have larger $a$-value, since using that neighbour with the same second index would increase the objective. Distances to a root differ by exactly one across a tree edge. Therefore both neighbours have smaller $a$-value, and $u_p$ is a strict local maximum of distance to $s$.

The index $r$ cannot be $k$: if it were, $a(u_p)>m$, and replacing $r$ by $p$ would add the positive quantity $c(u_p)$. Both neighbours of $r$ are admissible as second indices ($r-1\ge p$). Maximality forces their $c$-values to be smaller. Thus $u_r$ is a strict local maximum of distance to $t$.

Apply the exposed-peak lemma at $u_p$ with root $s$ and at $u_r$ with root $t$. It provides input vertices $x$ and $y$ in this order, with

$$a(x)=a(u_p)+1,\qquad c(y)=c(u_r)+1.$$

Therefore $M(w)\ge a(x)+c(y)=M(w')+2$.

Now suppose $p=r$. The strict excess $a(u_p)+c(u_p)>m$ means $u_p$ is off the endpoint geodesic, hence is not an endpoint of the output walk. Replacing the first index by $p-1$ shows $a(u_{p-1})<a(u_p)$; replacing the second by $p+1$ shows $c(u_{p+1})<c(u_p)$. The unique edges from $u_p$ toward $s$ and $t$ are the same, so these two neighbours coincide with that unique parent. The output vertex is a peak toward both endpoints. Its single exposed-peak witness $x$ increases both distances, and choosing the same input index twice gives

$$M(w)\ge a(x)+c(x)=M(w')+2.$$

In both cases,

$$\boxed{M(w')>m\ \Longrightarrow\ M(w)\ge M(w')+2.}$$

### 2.6 Clock conclusion and checks

Set $H(w)=\lceil(M(w)-m)/2\rceil$. If $w$ is reduced, the detection lemma gives $H=0$ and $R(w)=w$.

If $w$ is not reduced and $w'$ is also not reduced, the detection lemma and the two inequalities give $M(w')=M(w)-2$, hence $H(w')=H(w)-1$. If $w$ is not reduced but $w'$ is reduced, then $M(w')=m$; the first inequality gives $M(w)-m\le2$, while detection gives $M(w)-m>0$. Thus $H(w)=1$ and $H(w')=0$.

Every nonfixed run-parity update removes at least two letters, so the process reaches a reduced word. Along that process $H$ drops by exactly one at every nonfixed step and vanishes exactly at the fixed word. Therefore $h(w)=H(w)$, proving the claim. ∎

The usual $\lfloor n/2\rfloor$ bound follows from length decrease. For $q\ge2$ it is sharp on the carrier of length at most $N$: choose an alternating word $u$ of length $\lfloor N/2\rfloor$ and take $u u^{\rm rev}$. The literal schedule removes only its central pair at each round. For $q=1$ the sharp bound is instead zero when $N\le1$ and one when $N\ge2$.

**Hand countercheck against the wrong clock.** The word `abaabaa` evolves as `abaabaa` → `abb` → `a`, so its parallel clock is two. Left-greedy stack matching cancels its first six letters with nesting depth three and leaves the last `a`; that depth is not the clock. For this word the proposed formula gives $m=1,M=5$, hence two. This protects the exact schedule from a normal-form-only substitution.

## 3. Arbitrary-target one-step inverse counts

Let $f_L(y)$ count words of exact length $L$ with $R(w)=y$. The bounded-carrier count is $\sum_{L=0}^N f_L(y)$.

For $y=\epsilon$,

$$f_{2t}(\epsilon)=q^t\quad(t\ge0),\qquad f_{2t+1}(\epsilon)=0.$$

Indeed every maximal run must have even length. Compress each pair within each run; this bijects exact length-$2t$ predecessors with arbitrary words of length $t$. The empty source is included at $t=0$.

For a nonempty target $y=y_1\cdots y_m$, write

$$a=|\{i<m:y_i=y_{i+1}\}|,\qquad b=m-1-a.$$

Then

$$\boxed{\sum_{L\ge0} f_L(y)z^L=\frac{(q-1)^a z^{m+2a}(1-z^2)(1-(q-1)z^2)^b}{(1-qz^2)^{m+1}}.}$$

This rational expression is a formal series, so no analytic convergence assumption is used. Its fully explicit coefficient form is zero unless $L=m+2a+2t$ for some integer $t\ge0$, and otherwise is

$$f_L(y)=(q-1)^a\bigl(B_t-B_{t-1}\bigr),$$

$$B_t=\sum_{r=0}^{\min(b,t)}(-1)^r\binom br(q-1)^r q^{t-r}\binom{m+t-r}{m},\qquad B_{-1}=0.$$

Use $0^0=1$ in this combinatorial formula. For $q=1$, it gives one predecessor at every odd length for target $a$, and zero predecessors for all targets of length greater than one, agreeing with the literal map.

**Proof by canonical run/gap decomposition.** Every target letter comes from one odd maximal input run; its length contributes

$$o(z)=z+z^3+\cdots=\frac z{1-z^2}.$$

Every deleted run has positive even length, contributing $e(z)=z^2/(1-z^2)$. The odd runs appear in the exact order of the target letters. Before them, after them, and between each consecutive pair lie sequences of deleted even runs. Consecutive run labels must differ. This decomposition is unique for each source, and every legal decomposition produces that source and target.

Let $K$ be the $q\times q$ matrix with zero diagonal and one off diagonal. A prefix of $r$ even runs before a specified surviving letter has $(q-1)^r$ labelings, as does a suffix. Thus each exterior gap contributes

$$U=\frac1{1-(q-1)e}.$$

An internal gap between surviving letters $c,d$ with $r$ erased runs has $(K^{r+1})_{cd}$ legal labelings. Hence its series is $[K(I-eK)^{-1}]_{cd}$. Resolving the constant-vector direction (eigenvalue $q-1$) and its complement (eigenvalue $-1$) gives

$$G_=\frac{(q-1)e}{(1-(q-1)e)(1+e)},\qquad G_{\ne}=\frac{1-(q-2)e}{(1-(q-1)e)(1+e)}.$$

For $q=1$, only the equal case is relevant and equals zero; the formula follows directly from $K=0$. For $q\ge2$ the displayed two eigenspaces give both entries. Substitution yields

$$U=\frac{1-z^2}{1-qz^2},\quad G_=\frac{(q-1)z^2(1-z^2)}{1-qz^2},\quad G_{\ne}=\frac{(1-(q-1)z^2)(1-z^2)}{1-qz^2}.$$

Multiplying $o^mU^2G_=^aG_{\ne}^b$ gives the boxed generating function because $a+b=m-1$. Expanding its polynomial numerator and the negative-binomial denominator gives the stated $B_t-B_{t-1}$ coefficient sum. ∎

This is a one-step fibre theorem for arbitrary, possibly nonreduced targets. It is not the standard count of all words with a specified eventual reduced endpoint.

## 4. Current subtraction record and limitations

Primary source actually read: Kari, Mateescu, Păun and Salomaa, *On parallel deletions applied to a word*, RAIRO 29(2) (1995), 129–144, [primary PDF](https://www.numdam.org/item/ITA_1995__29_2_129_0.pdf). The selected reading covers the definition of a set-valued parallel deletion operation on printed page 130 and the unary $L=\{a^2\}$ discussion on printed pages 135–136. That operation admits different maximal deletion choices; it is not automatically our deterministic maximum-pair-per-run schedule. For example, on $a^4$ one may delete the middle $aa$ and leave $aa$ with undeletable separate gaps, whereas our map returns $\epsilon$. Thus this source is relevant background, not an exact-clock subtraction. No claim is made about unread sections proving or excluding our formula.

Local search located older serial adjacent-equal cancellation and free-group parallel-pair rules. Their exact originals still require the narrow follow-up read before any candidate nomination; search snippets are not proofs. The mathematical normal-form and Cayley-tree primitives receive no novelty credit here. The residual temporal claim is the schedule-specific ordered two-endpoint maximum and its exposed-peak decrement. The residual inverse claim is the evaluated one-step run/gap fibre, distinct from eventual-normal-form cogrowth.

Searches concerning parallel reduction, cancellation depth and tree walks did not yet establish a direct owner of these two exact statements. That is not an exhaustive novelty finding. Fréchet-distance search hits were navigation only; no equivalence to a Fréchet theorem is asserted or used.

## 5. Proposed bounded pressure-test source — NOT EXECUTED

Root requested source preparation for independent scrutiny. The following is a **proposal only**, embedded here without creating a runnable file or executing it. Scope: $q=1,n\le8$; $q=2,n\le8$; $q=3,n\le7$, totaling $9+511+3280=3800$ source words. No randomization, filesystem access, network, third-party dependencies, external observer, or enlarged sweep. It directly iterates maximal-run parity for the temporal ground truth; separately computes prefix/suffix stack lengths; counts literal one-step fibres; and checks both temporal inequalities and the explicit inverse coefficient formula. Any discrepancy must be preserved and returned, not patched around or used to expand the cutoff automatically.

```python
# PROPOSAL ONLY: has not been executed.
from itertools import product
from math import comb

def parity_step(w):
    out = []
    i = 0
    while i < len(w):
        j = i + 1
        while j < len(w) and w[j] == w[i]:
            j += 1
        if (j - i) % 2:
            out.append(w[i])
        i = j
    return tuple(out)

def reduced(w):
    stack = []
    for letter in w:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)

def distance_stat(w):
    n = len(w)
    left = [len(reduced(w[:i])) for i in range(n + 1)]
    right = [len(reduced(w[j:])) for j in range(n + 1)]
    maximum = max(left[i] + right[j]
                  for i in range(n + 1) for j in range(i, n + 1))
    return maximum, len(reduced(w))

def literal_time(w):
    current = w
    for t in range(len(w) // 2 + 1):
        following = parity_step(current)
        if following == current:
            return t, current
        assert len(following) <= len(current) - 2, (w, current, following)
        current = following
    raise AssertionError(('failed length bound', w))

def fibre_formula(q, length, target):
    if not target:
        return 0 if length % 2 else q ** (length // 2)
    m = len(target)
    a = sum(target[i] == target[i + 1] for i in range(m - 1))
    b = m - 1 - a
    remainder = length - m - 2 * a
    if remainder < 0 or remainder % 2:
        return 0
    t = remainder // 2
    def coefficient(s):
        if s < 0:
            return 0
        return sum((-1) ** r * comb(b, r) * (q - 1) ** r
                   * q ** (s - r) * comb(m + s - r, m)
                   for r in range(min(b, s) + 1))
    return (q - 1) ** a * (coefficient(t) - coefficient(t - 1))

def check_box(q, cutoff):
    words = [w for n in range(cutoff + 1)
             for w in product(range(q), repeat=n)]
    fibres = {}
    for w in words:
        following = parity_step(w)
        fibres[(len(w), following)] = fibres.get((len(w), following), 0) + 1
        maximum, endpoint_length = distance_stat(w)
        next_maximum, next_endpoint_length = distance_stat(following)
        time, endpoint = literal_time(w)
        assert endpoint == reduced(w), ('endpoint', q, w, endpoint)
        assert endpoint_length == next_endpoint_length, ('length', q, w)
        assert next_maximum >= maximum - 2, ('first inequality', q, w)
        if next_maximum > endpoint_length:
            assert maximum >= next_maximum + 2, ('second inequality', q, w)
        predicted = (maximum - endpoint_length + 1) // 2
        assert time == predicted, ('clock', q, w, time, predicted)
    comparisons = 0
    for target in words:
        for length in range(cutoff + 1):
            observed = fibres.get((length, target), 0)
            predicted = fibre_formula(q, length, target)
            assert observed == predicted, ('fibre', q, length, target,
                                           observed, predicted)
            comparisons += 1
    return {'q': q, 'cutoff': cutoff, 'sources': len(words),
            'fibre_comparisons': comparisons}

def main():
    reports = [check_box(q, cutoff) for q, cutoff in [(1, 8), (2, 8), (3, 7)]]
    witness = tuple('abaabaa')
    assert literal_time(witness)[0] == 2
    assert distance_stat(witness) == (5, 1)
    for report in reports:
        print(report)

if __name__ == '__main__':
    main()
```

Expected scope counts are arithmetic planning, not observed output. No PASS, canonical output, independent review, or execution provenance exists for this proposal. Execution requires a separate explicit scope approval from root. If independent review finds a proof gap that this box cannot resolve, return the gap rather than treating finite agreement as proof.
