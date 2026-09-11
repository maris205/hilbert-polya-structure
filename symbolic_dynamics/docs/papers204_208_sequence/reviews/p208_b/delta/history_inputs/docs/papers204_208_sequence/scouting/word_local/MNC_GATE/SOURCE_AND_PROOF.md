# MNC nonauthor proof audit and complete mechanism deductions

2026-09-06 UTC. This is an internal candidate gate, not a manuscript review,
external expert opinion, or author proof contribution. The frozen author
inputs are in [INPUT_PINS.sha256](INPUT_PINS.sha256). The full
[author proof](../CONTRAST_PROOF_WORK/PROOF_PACKAGE.md), source boundary,
handoff, root distance proof, and root source note were read. Author code
and canonical content were not used to construct the independent checker;
their hashes are pinned for artifact identity, not imported as evidence.

**Mathematics: valid as stated. Value: the proposed temporal axis is an
ECA36 singleton-deletion tail with frozen color labels and a bounded
two-step front end. The sharp 2/3 boundary does not restore a materially
separate temporal mechanism. The all-target fibre comparison is not falsely
declared an old theorem; it remains a valid extremal residual, insufficient
by itself for this batch's two-axis admission standard.**

## 1. Literal scope and proof attack

Throughout, the positions of a ternary cycle are labeled, $n\ge3$, and
$$F(x)_i=\min(|x_i-x_{i-1}|,|x_i-x_{i+1}|).$$
The metric is the usual integer distance, updates are synchronous, and
neither a rotation quotient nor a larger alphabet is introduced.

The following local truth-table description is equivalent to the literal:
the output is zero if either neighboring source equals its center; it is
two exactly on $020,202$; all other triples give one. The independent
checker compares these descriptions on all 27 triples and on every source
in the declared full boxes. This also fixes the ternary rule code
112796998038 with exponent $9a+3b+c$.

### 1.1 Full temporal adapter, not merely a binary restriction

Let $G$ be binary ECA36,
$$G(p)_i=(p_{i-1}\mathbin\oplus p_i)(p_i\mathbin\oplus p_{i+1}).$$
The only one-producing triples are $010,101$. Define
$$\begin{split}
\mathcal P_n&=\{p\in\{0,1\}^n:\text{each zero has a zero neighbor}\},\\
I(p)_i&=\mathbf1\{p_i=1,\ p_{i-1}=p_{i+1}=0\}.
\end{split}$$
For $p\in\mathcal P_n$, a zero cannot be the center of $101$.
Consequently $G(p)=I(p)$: all nonsingleton one-runs disappear, while
singleton ones remain. Distinct surviving ones have at least two zeros
between them, so $G(I(p))=I(p)$. The constant words, including $1^n$,
are covered: $I(1^n)=0^n$. Also $G$ sends every binary word into
$\mathcal P_n$, since a zero output comes from an equal edge and both
endpoints of that edge output zero. Hence $G^3=G^2$ on all binary cycles.
This is the elementary pulse-erasure mechanism underlying the published
second-level identity emulation of rule 36; the displayed argument is our
explicit application/rederivation, not an attribution of new ternary
content to the binary source.

Now define the *colored tail class*
$$\mathcal C_n=\{u\in\{0,1,2\}^n:
\text{every zero is paired, and every 2 has two zero neighbors}\}.$$
Every $u\in\mathcal C_n$ has a unique encoding
$$p_i=\mathbf1\{u_i>0\},\qquad D=\{i:u_i=2\},\qquad u=p+\mathbf1_D.$$
It satisfies $p\in\mathcal P_n$ and $D\subseteq\operatorname{supp}I(p)$.
Conversely every such $(p,D)$ gives a member of $\mathcal C_n$.
This is a labeled bijection, not a many-to-one support projection.

Directly from the local rule,
$$F(p+\mathbf1_D)=G(p)+\mathbf1_D.\tag{T1}$$
At a site of $D$ both zero neighbors give output two. At every zero site
an equal zero neighbor keeps the output zero, irrespective of a possible
adjacent two. At the remaining positive sites the relevant update is
binary; a two cannot be adjacent to one. Since $D\subseteq
\operatorname{supp}G(p)$, the encoding remains admissible after updating.
Thus $F|_{\mathcal C_n}$ is exactly the map
$(p,D)\mapsto(G(p),D)$. All magnitudes beyond binary are frozen labels.
In particular $F^2(u)=F(u)$ for every $u\in\mathcal C_n$.

It remains essential to check that this adapter covers every initial
ternary source, not just a favored invariant subfamily. Put $y=F(x)$.
Every zero of $y$ is paired and hence permanent. If $y$ has a zero,
each positive block of length at least two uses only values 1 and 2.
Every site in that block has an inside positive neighbor at distance at
most one, so after one more update the entire block is binary. A
singleton two is fixed and retains its two permanent zero neighbors.
No other site can output two. If $y$ is zero-free, all its letters are
1 or 2 and *every* adjacent distance is at most one, so $F(y)$ is
entirely binary. In both cases $F(y)$ is an image and its zeros are
paired. We have proved the complete inclusion
$$F^2(\{0,1,2\}^n)\subseteq\mathcal C_n.\tag{T2}$$
Combining (T1), (T2), and binary singleton deletion proves $F^4=F^3$.
The fixed set is exactly $0^n$ and isolated positive pulses, independently
labeled 1 or 2, separated by at least two zeros. Indeed a fixed point
belongs to $F^2$'s image, and in (T1) being fixed is precisely $G(p)=p$.
This also excludes every nonfixed recurrent cycle.

The adapter is **not** claimed to be a conjugacy on the original full
ternary carrier, a global equation $pF=Gp$, or a theorem stated in the
binary paper. Those stronger statements are unnecessary and the global
projection statement is false (the triples $121$ and $111$ suffice).
It is an exact covering of the claimed eventual dynamics after two
updates, with the whole entrance observation proved above.

### 1.2 What remains of the sharp clock

The author's small-case deductions are correct. At $n=3$, the first
image is $\{000,111\}\cup\operatorname{Rot}(001)\cup
\operatorname{Rot}(002)$; only $111$ is not fixed. At $n=4$, images
with a length-two zero block have a complementary $11$ block; the
zero-free images are $1111,2222$, and rotations of $2111$. Their next
images are fixed. Thus height two is a complete boundary classification,
not a finite guess. The sources $012$ and $0012$ attain two.

The orbit $01102\to10012\to10011\to00000$ attains three at length
five. At $n\ge6$, padding the fixed local pattern gives
$$0^{n-4}1102\to0^{n-2}12\to0^{n-2}11\to0^n.$$
The author correctly separates $n=5$, where the boundary wraps differently.

These witnesses show the one additional magnitude-collapse round can
really occur; they do not supply a new temporal engine after (T1)–(T2).
There is no long-time interaction among colors, new sharp length-dependent
transport law, nontrivial recurrent action, or additional all-size image
atlas in this submitted contract. The exact 2/3 distinction is a bounded
local front-end/sharpness patch to the occupied pulse-erasure mechanism.
This is the specific value deduction behind MNC-V1, not a claim that a
short proof is automatically worthless or that every use of a known tool
invalidates a theorem.

### 1.3 Arbitrary-target inverse: complete generic deduction

For target $b$, use nine overlap states $(a,c)\in\{0,1,2\}^2$ and an
edge $(a,c)\to(c,d)$ when $\min(|c-a|,|c-d|)=b_i$. A length-$n$
closed labeled path recovers exactly one source word from its centers;
every source recovers exactly that path. Remembering the initial pair
enforces the wraparound equations. This instantiates the general cyclic
preimage network, including source listing, not just counting.

The author's edge-distance representation gives the same source set
partitioned by $d_i=|x_i-x_{i+1}|$. The indicator
$\min(d_{i-1},d_i)=b_i$ is both necessary and sufficient after choosing
a closed color walk. Its weight formula is correct: zeros contract, an
odd number of unit edges is impossible, pure unit edges give
$2^{u/2+1}$, pure two-edges give $1+(-1)^v$, and a mixed word gives
$2^{u/2}$ precisely when each gap of unit edges between successive
two-edges is even. The invariant $2\times2$ block and complementary
reflection line in the submitted proof justify every case, including
empty and single-edge contractions. No division by cyclic rotations is
allowed or performed. All this is zero-credit static decoding.

### 1.4 Complete extremal audit: no missing target class

For the zero fibre, record the set $E$ of unequal source edges. A source
has no singleton precisely when $E$ is a matching. For a prescribed
edge mask of weight $k$, the number of colorings is
$2^k+2(-1)^k$; $k=0$ means three constants and $k=1$ means no source.
This gives $Z_n=I(C_n;2)+2I(C_n;-1)$ and hence
$$Z_n=2^n+(-1)^n+4\cos(n\pi/3).$$
The matching/proper-coloring calculation is classical and already occupied
internally by equality-mask work; no credit is restored to this slice.

For a mixed target, prescribe only its source-singleton mask. A singleton
zero block is impossible. Otherwise let $K$ be its number of positive
sites and $\ell_1,\ldots,\ell_r\ge2$ its zero-block lengths. Every
positive block forces unequal source edges; a zero block has forced equal
first/last internal edges and a path matching of optional unequal edges.
This gives endpoint matrices $B_2=B_3=I$, $B_\ell=B_{\ell-1}+QB_{\ell-2}$
with $Q=J-I$. Their common eigenvalues are
$$a_\ell=\frac{2^{\ell-1}+(-1)^\ell}{3},\qquad
e_2,e_3,e_4,\ldots=1,1,0,-1,-1,0,\ldots.$$
Taking the cyclic trace gives the exact relaxed count
$$2^{K+r}\prod_j a_{\ell_j}
 +2(-1)^{K+r}\prod_j e_{\ell_j}.$$
This counts every labeled endpoint-color choice, including $r=1$.
The bounds $a_\ell\le2^{\ell-2}$ and $|e_\ell|\le1$ imply the
uniform upper bound $2^{n-r}+2\le2^{n-1}+2$. At every $n\ge4$,
$2^{n-1}+2<2^n-5\le Z_n$. The relaxation is allowed to forget
magnitudes because it is used only as an upper bound. This is a valid
strict comparison for *every* mixed target.

If an all-positive target contains two, a prescribed site forces source
triple $020$ or $202$, leaving at most $2^{n-2}$ proper colorings.
This is strictly below $Z_n$ for $n\ge4$. For target $1^n$, sources
are proper colorings avoiding $020,202$. They necessarily contain 1,
and consecutive occurrences of 1 are separated by one extreme or two
distinct extremes. The two tile lengths are 2 and 3, each with two color
choices. The unique five-state lift in the author proof therefore counts
the sources without a root/rotation factor. Its trace recurrence is
$$t_0=3,\ t_1=0,\ t_2=4,\quad t_n=2t_{n-2}+2t_{n-3}.$$
The values $t_4=8,t_5=20,t_6=28$ start the induction
$t_n\le(3/4)2^n$. Direct comparison at four and
$(3/4)2^n<2^n-5$ for $n\ge5$ finish strictness.

This exhausts all target classes and proves the unique maximizer $0^n$
for $n\ge4$. At length three the complete fibre census is
$3+3\cdot4+3\cdot2+6=27$; the six permutations of $012$ form the
unique largest fibre over $111$. No exception, equality target, or
zero-fibre convention has been omitted.

## 2. Actual primary-source reading and limits

| Source and locator actually read | What is deducted; what is not asserted |
|---|---|
| Fukś, *Sequences of Preimages in Elementary Cellular Automata* (Complex Systems 14, 2003), introduction/definitions, Section 3 equation (9), Figure 1 caption and adjacent identity-emulator statement; [primary journal PDF](https://content.wolfram.com/sites/13/2023/02/14-1-2.pdf) | Rule 36's binary second-level identity emulation is explicitly prior. The paper distinguishes guessed multi-step preimage recurrences from proved results; those guesses are unused. The reference to Rogers–Want is read in this source, not passed off as reading that earlier paper's body. |
| Jen, *Enumeration of Preimages in Cellular Automata* (1989), introduction, Section 2 through equation (2.1), complete Sections 5.4–5.5, Appendix A conventions and rule-36 entry; [primary journal PDF](https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf) | Arbitrary-alphabet endpoint recurrences, binary run optimization, and forbidden-block modifications are occupied. Section 5.4 is a real optimization precedent, but its prose is not an exact theorem establishing MNC's labeled ternary strict maximum. The binary open-word rule-36 Fibonacci product is not silently substituted for the cyclic three-color count. |
| Jeras–Dobnikar, *Algorithms for computing preimages of cellular automata configurations* (2007), introduction, Section 4.2.2 including Theorem 6 and proof sketch, Sections 4.3–4.4, and complete Section 5.2/5.2.1; [author preprint](https://rattus.info/al/files/preimages.pdf) | The stated scope includes arbitrary alphabet/neighborhood and cyclic boundaries. The matrix product, cyclic diagonal, and remembered-start listing algorithm cover the complete generic decoder. Section 1.3 above gives the exact MNC substitution. No theorem of global fibre maximization is attributed to this algorithm. |
| Jen, *Scaling of Preimages in Cellular Automata* (1987), Section 2 matrix construction and Section 3 definitions (3.1)–(3.2), explanation preceding Lemma 1; [primary journal PDF](https://wpmedia.wolfram.com/sites/13/2018/02/01-6-2.pdf) | Its maximum first fixes an open binary word and varies its four end extensions, then sums over fixed words. That is not the maximum one cyclic ternary fibre. No false direct extremal adapter is declared from its title. |
| Fukś, *Ternary cellular automata induced by semigroups of order 3 are solvable*, arXiv:2601.00486v1, abstract and Sections 1–2 definitions; [primary HTML](https://arxiv.org/html/2601.00486v1) | The class has two essential inputs. MNC has three, as the literal triple table demonstrates. This excludes only a direct sitewise relabeling/reflection into that class, not arbitrary block/time encodings. It provides no clearance for MNC. |

The local extraction sidecars for the first three sources are honestly
`UNAVAILABLE`: `pypdf` is absent. Their exit zero means a verdict was
produced, **not** that structural verification passed. No local numerical
page anchor is certified. The source locators above are section, equation,
theorem, and appendix identifiers; relevant contexts were also actually
read through the primary web PDFs/HTML. Equation (2.1), missing from the
plain extraction, was additionally rendered and actually viewed in
[Jen1989_eq21.png](sources/Jen1989_eq21.png). This is an actual equation
inspection, not a claim of whole-PDF visual review or validated pagination.
The full extracted files are archival retrieval bytes, not declarations
that every paragraph was read. The originals remain in the frozen author
package and are explicitly pinned here.

The attempted Rogers–Want DOI open returned an internal retrieval error;
its body was not obtained. No unseen result from it is required: the binary
identity is reported in the retrieved Fukś primary article and directly
rederived in Section 1.1. No source HOLD is invented or silently closed by
the present value rejection.

## 3. Internal collision boundary

Literal/mechanism searches were run on manuscript TeX and selected scout,
proof, gate, and contract originals. The following exact contexts were
then read and pinned, rather than treating old summaries as proofs.

- P164, cyclic equality feedback: the literal $E(x)_i=\mathbf1\{x_i=x_{i+1}\}$,
  theorem atlas, change-mask multiplicity and affine-tail proof. There is
  the exact first-step relation $\mathbf1\{F(x)_i>0\}=(1-E(x)_{i-1})(1-E(x)_i)$.
  Proper cycle-coloring weights and equality-mask enumeration are occupied.
  Its subsequent affine Rule-102 evolution is not identified with MNC.
- P197, ternary cyclic sign difference: literal $D(x)_i=\operatorname{sgn}(x_{i+1}-x_i)$,
  core, local certificate, sharp-tail theorem and run-bound mechanism.
  Signed forward differences have a nontrivial shift-type core, unlike MNC.
  Edge traces/finite-language methods remain zero-credit primitives.
- P117, odd-run reversal: literal definition and boundary-cost drop lemma.
  It flips complete odd-length runs, is not fixed radius, and has a
  shrinking parity-boundary mechanism. It is not a direct MNC duplicate;
  generic run deletion gives no new credit to either comparison.
- P196, cyclic Gödel implication: the two-input literal, constrained image
  language, one-step shift theorem and proof. A generic finite-language
  tail is occupied, but its actual implication/shift is not MNC's rule.
- The full current contrast intake and root source note were read. MDE and
  MNC share the binary contrast core and count as at most one family; the
  present rejection does not authorize promoting the same axis under MDE.

No bounded search is a proof excluding all possible nonlocal encodings.
The rejection below does not rely on any of these failed direct matches:
its operative temporal transfer is the complete one in Section 1.1.

## 4. Search provenance, value disposition and scope

Three actual query groups are preserved in [sources/](sources/): literal
minimum/absolute contrast, decimal ternary rule code, ternary identity
emulation, maximum ternary preimages, cyclic singleton runs, and recent
2024–2026/index-specific variants. Direct Scholar/Semantic Scholar provider
tools were unavailable; web queries restricted to their domains were tried.
The arXiv query requested a 183-day recency window but returned older
records too. This is a bounded attempt, not a six-month census. Unrelated
results were not used as scientific evidence; nonhits add no novelty credit.

The exact generic decoder, zero count, and all-one language are deducted.
The mixed-target relaxation and all-positive exclusions establish a correct
global strict maximum. I did **not** find a primary statement that already
asserts that complete ternary maximum, and I do not manufacture one from
Jen's general optimization discussion. Nevertheless the batch requires a
separate substantive temporal/recurrent axis. After (T1)–(T2), the latter
consists only of a local magnitude-collapse front and bounded sharpness
exceptions wrapped around ECA36's pulse deletion with frozen labels.

Under the inherited prohibition on parameter wrappers and occupied proof
mechanisms, this fails the conjunction threshold: **MATH_VALID /
KILL_VALUE_TEMPORAL_BINARY_WRAPPER / NO_ADMISSION**. This is an evidence-
anchored internal value judgment, not proof of global nonnovelty, an attack
on the correctness of the extremal theorem, or a numerical quality score.
Preserve the author theorem and failed candidate evidence. No larger
cutoff, additional finite table, generic inverse rewrite, or promotion under
a same-family alias resolves MNC-V1. A genuinely different theorem contract
would require separate authorization and a fresh gate; none is requested
or authored here. HOLD_EXTERNAL remains unchanged.
