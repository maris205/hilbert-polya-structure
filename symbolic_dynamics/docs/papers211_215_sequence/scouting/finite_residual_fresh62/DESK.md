# Fresh 62 — parallel abc erasure, author negative

2026-09-11. **NO NOMINATION.** One bounded word-rewriting literal was inspected. Only this file is created; no scientific execution, import, pilot, build, child agent, paper number, central edit or Git operation. This is author work, not a manuscript review.

## Literal and time boundary

Fix an alphabet containing three distinct letters $a,b,c$ and a length ceiling $N$. On all words of length at most $N$, simultaneously delete every occurrence of $abc$; call this $T$. Distinct occurrences cannot overlap because no nonempty proper prefix of $abc$ is a suffix. The finite carrier is invariant. Words avoiding $abc$, including the empty word, are fixed.

Every nonfixed round deletes at least three letters, so $h(w)\le\lfloor|w|/3\rfloor$. Equality occurs for $w=a^k(bc)^k$, which has exactly one occurrence per round and maps to $a^{k-1}(bc)^{k-1}$. This is just the sharp deletion budget. No all-input pointwise clock independent of executing the deletion process was proved here. An informal nesting-tree description is not presented as a proved, uniquely defined normal form or height formula.

## Evaluated one-step inverse, with explicit limits

For a target $y=y_1\cdots y_m$, let $r$ be its number of occurrences of $abc$. Let $f_t(y)$ count sources of length $m+3t$ mapping to $y$. Then

$$\sum_{t\ge0}f_t(y)z^t=\frac{z^r(2-z)^r}{(1-z)^{m+1}}.$$

Equivalently, $f_t(y)=0$ if $t<r$, and otherwise

$$f_t(y)=\sum_{j=0}^{\min(r,t-r)}(-1)^j\binom rj2^{r-j}\binom{m+t-r-j}{m}.$$

The fibre on the prescribed carrier is

$$|T^{-1}(y)|=\sum_{t=0}^{\lfloor(N-m)/3\rfloor}f_t(y).$$

**Proof.** Any source is obtained by inserting $(abc)^{k_i}$ in each of the $m+1$ gaps around the surviving letters, with $k_i\ge0$. These are the blocks actually erased. An occurrence of $abc$ cannot overlap an inserted full $abc$ block; such an overlap would give a border of $abc$. Thus the only possible unwanted occurrences consist of three consecutive surviving letters. Each occurrence of $abc$ in $y$ must therefore have at least one positive insertion count in its two internal gaps. This is also sufficient. The erased source occurrences determine the surviving letters and all gap counts uniquely, so valid choices are counted without multiplicity.

The $r$ occurrences in $y$ are disjoint, hence their pairs of internal gaps are disjoint. An unconstrained gap contributes $(1-z)^{-1}$, while each constrained pair contributes $(1-z)^{-2}-1$. The product is

$$((1-z)^{-2}-1)^r(1-z)^{-(m+1-2r)}=\frac{z^r(2-z)^r}{(1-z)^{m+1}}.$$

Binomial expansion gives the displayed coefficient. For $m=r=0$ this says $f_t(\epsilon)=1$, corresponding to $(abc)^t$. The term $t=0$ gives the self-preimage exactly for avoiding targets. No empirical check is claimed.

This is an elementary gap-allocation inverse mechanism. It does not supply the missing substantive pointwise temporal axis or by itself justify a paper.

## Early literal and primary subtraction

The complete current Fresh53 desk and the original ZR proof at `docs/papers204_208_sequence/scouting/combinatorial_second/PROOF_NOTES.md`, lines 24–75, were read. ZR preserves length and replaces cyclic $001$ by $110$; its inverse uses constrained target-block choices. It is **not** the present linear-word erasure map. The shared unbordered-occurrence argument is only a known primitive. A further targeted Markdown search in the P82–P91 and P147 scout paths returned no match; that limited no-hit is not novelty evidence.

The decisive actual primary PDF is [Cui, Kari and Seki, *On the Reversibility of Parallel Insertion, and Its Relation to Comma Codes*](https://cs.uwaterloo.ca/~lila/pdfs/On%20the%20reversibility%20of%20parallel%20insertion,%20and%20its%20relation%20to%20comma%20codes.pdf), CAI 2009, pp. 204–219. Printed p. 206 defines maximal parallel deletion, and p. 208, Proposition 1, states its single-valuedness for an unbordered deleted word. These passages were actually read. Specializing to $abc$ deletes all its disjoint occurrences, exactly our nonfixed update. The source returns an empty result set when no occurrence exists; our self-loop convention only makes those states fixed. Neither our coefficient formula nor an all-input clock is attributed to that paper without inspection.

The earlier [Kari et al., *On parallel deletions applied to a word*](https://www.numdam.org/item/ITA_1995__29_2_129_0.pdf) PDF was also opened, but no new substantive theorem from it is used here. Unlike overlapping $aa$ deletion, no scheduler ambiguity remains for $abc$.

## Disposition

**AUTHOR NEGATIVE: known update; no complete two-axis residual contract.** The explicit gap-count formula is preserved as a deduction, not declared globally novel. The only established time theorem is the excluded elementary sharp deletion budget. No larger word box, new scheduler, second literal or extra layer is requested. The project and proof-writer skills kept source subtraction, author deductions and missing obligations separate; native calls are evidence of reading, not an immutable verification package or independent PASS.
