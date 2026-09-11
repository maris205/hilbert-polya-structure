# P203 Section 2: bounded coauthor compression check

Date: 2026-09-05 UTC. **AUTHOR_SIDE_PROOF_CHECK / NOT_REVIEW_A_OR_B.**
The checker contributed the original temporal theorem and is therefore a
mathematical coauthor. This is not blind, external, cross-model, or independent
manuscript review. Only this file is written; the manuscript is not edited.

## Claim, assumptions and status

For the full carrier of simple loopless labelled graphs on
$\{0,\ldots,n-1\}$, complement the lexicographically least monochromatic
triple, or hold if no such triple exists. Section 2 claims that every strict
selector change introduces a globally new vertex and consequently
$H(n)=\max\{0,n-3\}$ for every $n\ge0$.

**PROVABLE AS STATED.** The compressed text retains the load-bearing steps
of the original proof. No mathematical repair is requested within this
bounded Section 2 check. This statement does not review the inverse/equality
sections, bibliography, paper value, PDF, code, or final gate disposition.

## Exact inspected text

- Working `main.tex` SHA-256 at inspection:
  `a08983002caf08109c6a6406183149343aaa5ecd9a6d08af7f521f8ca85480b0`.
- Section 2 SHA-256:
  `289a8d5dbb1504c38fb5636f010032d2fd57cd78feab81e9ce5475a10139747c`.
  This hashes the 6,207 UTF-8 bytes beginning with the Section 2 command and
  ending immediately before the Section 3 command, including intervening
  whitespace. It isolates the reviewed proof if unrelated draft text changes.
- Original frozen `reviews/mct_temporal_pressure_20260905/PROOF_PACKAGE.md`:
  `25ba4d29400ee7047fac588c3e8ba64cd55bf3782368a96bf4fb88dcbd5b85f8`.

The exact map/notation in Section 1 and the entirety of Section 2 were read,
then compared with the full original temporal proof. The optional later
vertex-zero lemma is not used. The proof-writer skill supplies the explicit
assumptions, dependency and boundary checks here; it does not turn coauthor
checking into independent review.

## Dependency and compression audit

### 1. Selector descent and the two-step obstruction

A flipped triple remains monochromatic. Thus the selector cannot increase;
an equal selector reverses the preceding move, and any moving orbit reaches
a two-cycle. Distinct triangle edge masks cannot cancel in two successive
flips, so entrance time equals the number of strict changes. This is generic
scheduling background, not claimed new credit.

In the forbidden $abc,abd,abe$ pattern, strict replacement gives $e<d<c$;
in particular $e$ is not an earlier triangle vertex. The untouched $ae,be$
and restored $ab$ therefore really produce an earlier initial monochromatic
triple. For the later-minimum argument, $e<\min T_1$ and $d<c$ imply that
$e$ precedes every vertex of $T_0$. The initial constraints on $eab,eac$
force $eb=ec=1-q$, and flipping $T_0$ makes $ebc$ an earlier competitor
to $T_1$. No hidden assumption about sorted names $a,b,c$ is used.

### 2. Fixed-anchor parity

The shared-edge obstruction forces the sliding form
$T_t=\{a,v_t,v_{t+1}\}$ and $v_{t+2}<v_t$. A first repeated vertex has
opposite-parity indices. Interior vertices receive exactly two anchor-edge
flips before retirement, restoring their entry colour; the initial retired
vertex receives one. The manuscript distinguishes these cases and obtains
the required opposite colour at re-entry in each. Zero strict changes are
vacuous; a single strict change needs only the initial pair orientation.

### 3. Initial retired vertex: the previously fragile case

The compressed text does not omit this case or wrongly apply the fixed-anchor
argument to $T_0$. If the minimum first drops from $T_0=\{r,u,v\}$ to
$T_1=\{a,u,v\}$, then no initial monochromatic triple can contain $a$.
Every initial anchor-colour class therefore induces the opposite edge colour.

For $ar=\gamma$, minimality of $T_1$ against $aru$ and $arv$ separately
forces $r>v$ and $r>u$. Both decreasing subsequences remain below this label.
For $ar=q$, a putative return has odd relative time $k$, even incoming
position $k+1$, and odd partner $w=v_k\le v$. The old partners $u,v$ are
handled separately by their already-flipped edge to $r$.

For a new partner, $w<v$ and its first entry occurs at even relative time
$k-1$. Its initial anchor edge is therefore $\gamma$, not $q$. Together
with $u,v$ in the same initial class this forces $wu=wv=q$. An edge
$rw=q$ would make $ruw$ initially monochromatic and earlier than $ruv$;
otherwise the unchanged edge $rw=\gamma$ blocks the return. The orientation
of $u,v$ is the sliding-pair orientation, not an unmentioned inequality
between those two labels. This closes the global, rather than merely
fixed-anchor, no-return conclusion.

### 4. Uniform sharp family and small sizes

The displayed edge formula is the original explicit family, with descending
non-anchor labels and the exceptional $s_0=s_1=0$ correctly retained.
Initially only $0v_0v_1$ is monochromatic among anchor triples. At time
$t\ge1$, the manuscript retains all three needed classes: restored retired
vertices, the once-flipped carry, and untouched future vertices, with the
special retired $v_0$ treated separately.

Equal-colour future/future and retired/future pairs cannot be eligible;
the latter have unchanged mutual edges. Descending labels make any eligible
retired/retired or carry/retired pair lexicographically later than the
carry/next-future pair. Among matching future anchor colours, precisely
$j=t+1$ has the correct pair edge, while $j\ge t+3$ has the opposite
colour. Non-anchor triples start later. Hence the selected trace and its
$n-3$ strict changes follow inductively. The last triple is $012$ and is
immediately selected again after flipping.

At $n=3$, the construction has two non-anchor vertices, one selected triple
and zero strict changes; no induction step is required. At $n=0,1,2$ there
is no triple and every state is fixed. No larger-size witness assumption is
smuggled into these cases.

## Scope of the result

The original claim survives unchanged and Section 2 is self-contained at
the inspected digest. No finite verifier was rerun or counted for this
textual author check, and no new independent review is claimed. Subsequent
changes to Section 2 require a fresh digest and renewed checking; the whole
paper still requires its genuine independent A/B process and terminal QA.
