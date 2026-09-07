# Independent source and all-quantifier reduction review

2026-09-07. Reviewer: current-team `scout_charp_c414`, not the coordinator
who proposed or is writing this candidate. This file is the reviewer's
only write in `function_field/`. The coordinator owns the proof, atlas,
code, overall substance adjudication and all global records.

**Final mathematical verdict: PASS.** The reviewer independently checked
the full 486-line [PROOF_PACKAGE.md](PROOF_PACKAGE.md), including its
all-quantifier reduction, seven-type field-uniform atlas, sign lifts,
sharp 14-point characteristic-three case and finite ordinary zeta.
Sections 1–2 below record the independent reduction developed before
reading that full proof; Section 6 records the subsequent comparison and
additional atlas checks. No mathematical blocker was found. This
certifies the mathematical arguments specified here, not the unexecuted
producer script, publication priority or an admission decision.

## 1. Exact reviewed object and conventions

Let $k$ be any field with $\operatorname{char}k\ne2$, let $a\in k^*$,
and let $c\in k[t]\setminus k$. On $k(t)^2$ consider

$$H(x,y)=(y,y^2+c-a x).$$

The time is ordinary positive iteration, and points/cycles are counted
without scheme multiplicity. A periodic point gives a cyclic coordinate
word satisfying

$$y_i^2+c=y_{i+1}+a y_{i-1}. \tag{1}$$

No period bound, finite constant field, algebraic closure, perfectness,
local compactness, separability of $k$, or completed-field descent is
assumed in the arguments below. Indices are cyclic even for periods one
and two, so repeated neighbors must retain their coefficients.

## 2. Independent proof audit of the reduction

### 2.1 Finite poles and the common degree

At an irreducible polynomial prime of $k[t]$, suppose that one coordinate
has a pole. Let $M>0$ be the maximum pole order within its finite periodic
word and take an index attaining it. The left side of (1) has pole order
$2M$, since $c$ is integral there. The right side has pole order at most
$M$, since $a$ is a nonzero constant. This contradiction shows that all
coordinates are in $k[t]$.

Let $d=\deg c>0$ and let $m$ be the largest degree in one periodic word.
The word cannot consist entirely of constants. At a coordinate of degree
$m\ge1$, the right side of (1) has degree at most $m$. Therefore the
degree-$2m$ term in $y_i^2$ must cancel that of $c$, and $d=2m$. For any
other index, degree strictly below $m$ would leave the degree-$2m$ term
of $c$ uncancelled. Consequently every coordinate has degree $m=d/2$.
This also proves that words in different cycles have the same degree;
no maximum over a possibly infinite set of cycles was used.

### 2.2 All coordinates lie on two polynomial translates

Choose one coordinate $Y$ from one periodic word. For any coordinate $Z$
from any periodic word, subtract the two instances of (1). Their right
sides have degree at most $m$, so

$$\deg(Z^2-Y^2)\le m.$$

Their leading coefficients have equal squares. Since the characteristic
is not two, choose the unique $\sigma\in\{1,-1\}$ that cancels the
degree-$m$ term of $Z-\sigma Y$. Then $Z+\sigma Y$ has degree exactly
$m$. Unless $Z-\sigma Y=0$, the product degree identity forces
$\deg(Z-\sigma Y)\le0$. Thus

$$Z=\sigma Y+b,\qquad b\in k. \tag{2}$$

This is valid across all cycles, not just inside the initially selected
one. The choice of sign is unique because $Y$ is nonconstant and
$2\ne0$ in $k$.

### 2.3 Square completion, uniqueness and coefficient comparison

Apply (1) at the chosen coordinate $Y$. Its two neighbors are of form
(2), so $c=-Y^2+LY+C_0$ for constants $L,C_0\in k$. Put

$$P=Y-L/2,\qquad C=C_0+L^2/4.$$

Then $P\in k[t]\setminus k$ and

$$c=-P^2+C. \tag{3}$$

No square root outside $k$ has been chosen. If also $c=-Q^2+D$ with
$Q$ nonconstant and $D\in k$, then
$(P-Q)(P+Q)=C-D$. If $C-D\ne0$, both factors must be constants,
contradicting the nonconstancy of $P$ and $2\ne0$. If $C-D=0$, the
integral domain $k[t]$ gives $Q=\pm P$. Thus $C$ is unique and $P$ is
unique up to sign.

Fix either choice of $P$. Every periodic coordinate is uniquely
$y_i=\sigma_iP+b_i$, where $\sigma_i\in\{1,-1\}$ and $b_i\in k$.
The coefficients of $P$ and of $1$ in (1) give exactly

$$b_i=\frac{\sigma_i(\sigma_{i+1}+a\sigma_{i-1})}{2},\qquad
b_i^2+C=b_{i+1}+a b_{i-1}. \tag{4}$$

Conversely, any periodic sign word satisfying both equations in (4)
reconstructs an actual periodic word for (1). These are polynomial
identities, not a leading-order approximation. The existence of (3) by
itself is necessary, not sufficient: its sign graph may contain no cycle.

### 2.4 Exact four-sign graph and ordinary-point injection

For a state $(r,s,u,v)\in\{1,-1\}^4$, define

$$B_0=\frac{s(u+a r)}2,\qquad
B_1=\frac{u(v+a s)}2,$$

and label the state by

$$\mathcal L(r,s,u,v)=(sP+B_0,\;uP+B_1). \tag{5}$$

This map from all 16 states to $k[t]^2$ is injective, including when
$a=\pm1$ or the characteristic is three. Indeed the nonconstant
coefficients of the point recover $s,u$, the constant terms recover
$B_0,B_1$, and

$$r=(2sB_0-u)/a,\qquad v=2uB_1-a s.$$

There is an arrow $(r,s,u,v)\to(s,u,v,w)$ precisely when

$$B_1^2+C=\frac{v(w+a u)}2+a B_0. \tag{6}$$

For that arrow, the coefficient-of-$P$ identity in (4) is automatic,
and (6) is exactly the remaining condition
$H(\mathcal L(r,s,u,v))=\mathcal L(s,u,v,w)$.

Injection of $\mathcal L$ gives at most one outgoing arrow per state.
Injection of the automorphism $H$ additionally gives at most one incoming
arrow. Thus the graph is a partial permutation, not a branching shift.
Every graph cycle reconstructs an actual ordinary orbit, and every
rational periodic point has the unique four-sign state supplied by its
own neighbors. Exact periods are preserved by the injective labels.
Hence there are at most 16 ordinary rational periodic points in total,
and every period is at most 16. This is a genuine finite reduction over
every allowed $k$, not a finite-field sample.

Changing $P$ to $-P$ and all four signs to their negatives leaves the
same actual label after this simultaneous change. With $P$ fixed,
however, complementary states are not identified: injection (5) applies.
A later quotient to transition bits must account for the lifts back to
these two global sign choices.

### 2.5 Essential exclusions and avoided shortcuts

- If $a$ were nonconstant, its finite valuations and degree would enter
  the estimates. If $a=0$, both inverse dynamics and predecessor
  reconstruction fail. Neither extension is certified here.
- In characteristic two, the two leading signs merge, division by two
  fails and the degree-of-sum argument changes. No positive-characteristic
  extrapolation across that exclusion is made.
- For constant $c$, $m$ need not be positive; the two-term independence
  and uniqueness steps do not apply. The accepted constant-coefficient
  height contract remains a different source problem.
- Point labels, not Jacobian nonvanishing of fixed equations, justify
  the ordinary-point count. No assertion of reduced fixed schemes has
  been made, and no prime-to-characteristic period assumption was used.

## 3. Primary ownership: exact convention and read scope

### 3.1 Ingram: existing bad-place bounds, not the present atlas

Patrick Ingram, *Canonical heights for Hénon maps*, Proc. London Math.
Soc. 108 (2014), no. 3, 780–808, DOI 10.1112/plms/pdt026. Identity:
[primary publisher metadata](https://academic.oup.com/plms/article-abstract/108/3/780/1571741).
Actual proof-source access: [arXiv:1111.3609v1](https://arxiv.org/pdf/1111.3609v1),
32 pages; Introduction Theorems 1.2/1.4, relevant §3 root-disc and
product-formula arguments, and §4 local bounds/proof closure were read
as text excerpts, not as a claim to reread every page.

The source writes $\varphi_\alpha=(\alpha y,x+f(y))$. Theorems 1.2/1.4
fix $\alpha=1$ and provide function-field finiteness or bounded periods
controlled by bad places, together with height assertions. Its §3
degree-at-least-three argument routes the quadratic case to §4. Those
accessed results do not state the complete square-completion/reconstruction
or the unrestricted-determinant parameter atlas. The source's finiteness,
local escape and clustering mechanisms must nonetheless be credited.

The convention conversion is checked directly:

$$L(x,y)=(-a x,y),\qquad
L H_{a,c}L^{-1}(x,y)=(-a y,x+y^2+c).$$

Thus $\alpha=1$ corresponds to our $a=-1$, not $a=1$. A reference to
the source's special determinant must preserve this sign.

### 3.2 Allen–DeMark–Petsche: completion horseshoes

Kenneth Allen, David DeMark and Clayton Petsche, *Non-Archimedean Hénon
maps, attractors, and horseshoes*, [official arXiv record](https://arxiv.org/abs/1610.04271),
v3 dated 6 February 2018. Actual [primary PDF](https://arxiv.org/pdf/1610.04271)
access: Introduction §1.1, parameter regions and Theorem 1(a),(e);
targeted §5 horseshoe statements. No full 31-page proof reread is claimed.

The stated base field is complete, locally compact, non-Archimedean,
with odd residue characteristic. For
$\varphi_{A,B}(X,Y)=(A+B Y-X^2,X)$, the relevant region is
$|A|>\max(1,|B|^2)$; when $A$ is a square, the filled Julia dynamics is
the full two-symbol bilateral shift. With $J(x,y)=(-y,-x)$, direct
composition gives $JHJ^{-1}=\varphi_{-c,-a}$.

This completion theorem does not determine which itineraries come from
$k(t)$, and $k((1/t))$ is not generally locally compact for arbitrary
$k$. Our rationality restriction (4)–(6) is therefore not a restatement
of that accessed theorem. Binary itinerary coding and local escape are
classical inputs, not novelty claims here.

## 4. Repository collision and remaining substance question

The earlier [C412 integer-Hénon proof](../../research_c409_c413/nonlinear_geometry/PROOF_INTEGER_HENON.md),
especially §§1 and 3–4, was read directly. Its conservative $a=1$
integer-parameter setting obtains $x_i=\varepsilon_i r+\delta_i$ with
six coordinate symbols and then the same sign/offset equations as (4)
at $a=1$. Its large-integer separation and finite small-parameter
completion are not repeated here. The current degree comparison is a
clean algebraic analogue of that same mechanism; the conservative
subcase and the mere use of finitely many symbols cannot be presented
as independent inventions.

The already admitted [constant-coefficient height proof](../../research_c414_c418/spectral/HEIGHT_PROOF_PACKAGE.md),
assumptions and Step 1, was also read. It fixes coefficients in a finite
constant field and treats the distribution of heights on polynomial
points; every nonconstant orbit escapes there. It neither includes a
nonconstant $c(t)$ nor classifies the present rational periodic locus.
The shared elementary degree-escape argument is still deducted.

The remaining candidate increment is consequently specific: exact
global rationality/reconstruction for **every** nonconstant polynomial
parameter and **every** nonzero constant determinant, followed by the
complete all-field parameter atlas and its actual exceptional cycle
lifts. It is not general Hénon arithmetic boundedness, a local horseshoe,
an integral conservative six-symbol theorem or a height distribution.
The reduction alone is short and uses nearby classical/repository ideas;
its correctness alone does not establish independent-paper substance.
The now-verified atlas also resolves the unrestricted constant
determinant and characteristic-dependent branches, rather than stopping
at that short reduction. No nearest accessed theorem was found that
already supplies this whole atlas, but that bounded finding is not a
global novelty guarantee. The coordinator retains the substance verdict.

## 5. Review method and source-search receipt

The reviewer performed symbolic reasoning and read-only primary-source
and repository checks. No new numerical experiment, parameter census,
root atlas enumeration, old certificate, PDF build or frozen test was
run. Formula-heavy primary searches for function-field quadratic-Hénon
rational periodic classifications, polynomial parameters, squares and
the proposed finite bound mostly returned Ingram, the 2024 open-problem
survey and unrelated material. Search absence is not a theorem or a
systematic literature conclusion. Secondary results were not used to
claim mathematical ownership.

The review uses `proof-writer`'s quantifier/assumption discipline and the
research-review structure with current-team independent reading. The
repository's current-team review policy replaces the older skill's
external-model example; all current concurrency slots are occupied by
the coordinator and independent lanes, and no extra reviewer/API was
invented. ARS source-verification is limited to the source records and
scope distinctions above; it supplies no proof or admission verdict.

After the coordinator delivered the stable proof, the reviewer accepted
the additional invitation to check its minimum-state classification,
sign lifts and field-dependent overlaps by hand. No producer code was
run, and the number 19 of unrestricted graph cycles was not needed or
independently asserted as a computational result by this reviewer.

## 6. Full-proof comparison and independently checked atlas

### 6.1 Read object and precise certification boundary

The entire proof was read, from Theorem 1 through the final scope
paragraph. The first fully reviewed version had SHA256

```text
1a6d092e4a50b6d2556d373f50709309324e38224d0c2c50a652b5c20e79c991
```

The certified mathematical scope is Steps 1–9 and Theorems 1–2 /
Corollary 3: rational-to-polynomial exhaustion; common degree across all
cycles; unique square completion; exact sign/bit equations; injective
point reconstruction and partial permutation; all graph cycles; actual
ordinary least periods; all parameter overlaps and sharp point totals;
and the resulting finite-cycle zeta identity. Certification of the
producer script's execution, implementation, outputs and historical
timing is explicitly excluded.

Steps 1–3 agree with the independent proof in §§2.1–2.3, including the
across-cycles quantifier. Step 4 was checked by expanding

$$b_i=(a+1)/2-\delta_i-a\delta_{i-1}.$$

Using only $\delta_i^2=\delta_i$ gives

$$K_a-C=a^2\delta_{i-2}
       +2a\delta_{i-1}\delta_i+\delta_{i+1},$$

which is the author's equation (8) after shifting indices. Its validity
requires no division by three or restriction on the constant field.

For the signed-state label $E(\varepsilon;u,v,w)$, the injection follows
from its two leading coefficients, then its two constants. In the
converse direction, if $H(E)$ is another signed label, its two leading
coefficients give $\varepsilon'=\varepsilon(-1)^v$ and $v'=w$;
the first constant offset then gives $u'=v$ since $a\ne0$. The remaining
constant equation gives the new bit and the edge condition. The reviewer
suggested spelling out this order as a clarity improvement: a lone
constant offset need not determine two bits when $a=1$. This is not a
counterexample to the actual formula or a missing hypothesis.

### 6.2 Exhaustion without an enumeration program

The reviewer followed each possible least state in the author's eight
vertex graph, retaining characteristic-dependent equations. The
independent implications were:

| Least state / branch | Forced continuation and algebra | Result |
|---|---|---|
| $000$, loop | $\Lambda=0$ | Word $0$ |
| $000$, nonloop | $000\to001\to011\to110\to100\to000$; alternatives force $a=0$; $2a=1$ and $a^2=1$ | Exactly characteristic three, $a=-1$; word $00011$, $\Lambda=1$ |
| $001$ | A label-one path enters $000$; otherwise $001\to010\to100\to001$ and $a^2+1=0$ | Word $001$, $\Lambda=0$ |
| $010$ | The label-zero branch reaches a smaller successor; $010\to101\to010$ forces $a^2=1$ | Word $01$, $\Lambda=1$ |
| $011\to110$ | The branch through $100$ must reach a smaller state; $110\to101\to011$ forces $(a-1)^2=0$ | Since $k$ is a field, $a=1$; word $011$, $\Lambda=2$ |
| $011\to111$ | The loop forces $a=0$; the path $111\to110\to101\to011$ forces $a^2=1$ and $2a=1$ | Exactly characteristic three, $a=-1$; word $0111$, $\Lambda=2$ |
| $100,101,110$ or $111$ | The first three have only smaller successors; $111$ must loop | Only word $1$, $\Lambda=(a+1)^2$ |

This handles every possible least state of a nonempty finite directed
cycle. The inference $(a-1)^2=0\Rightarrow a=1$ is valid for a field,
including imperfect fields, and is not silently applied to a ring with
nilpotents. The exceptional inference uses $4a^2=1$ and $a^2=1$ to
give $3=0$; it does not discard small-characteristic solutions using a
characteristic-zero gcd. Thus the seven rows are an all-field theorem,
not a parameter sample.

### 6.3 Sign lifts, least periods and noncollision of rows

On one traversal of a bit cycle, the signed-state phase is multiplied
by $(-1)^{\text{number of ones}}$. Even parity therefore gives two
cycles of the bit period; odd parity gives one cycle of twice that
period. Injection of the signed labels rules out any shorter actual
point period. If two even-parity lifts were cyclic rotations of one
another, the rotation would already return the same bit state and
preserve its sign, which is impossible for opposite initial signs.

The reviewer checked the seven lengths/parities explicitly:

| Word | Length | Ones | Ordinary contribution |
|---|---:|---:|---|
| $0$ | 1 | 0 | Two fixed points |
| $1$ | 1 | 1 | One two-cycle |
| $01$ | 2 | 1 | One four-cycle |
| $001$ | 3 | 1 | One six-cycle |
| $011$ | 3 | 2 | Two three-cycles |
| $00011$ | 5 | 2 | Two five-cycles |
| $0111$ | 4 | 3 | One eight-cycle |

At fixed parameters, different bit cycles have disjoint states, and
the injective signed labels give disjoint point sets. Therefore rows
that meet in parameter space must be added, not merged or discarded.
The transformation $P\mapsto-P$ changes the phase labels only and
does not alter the actual point inventory.

### 6.4 Every overlap and the sharp total

For $a\notin\{1,-1\}$, the fixed and two-cycle loci are distinct
because equality would force $(a+1)^2=0$. The only extra possible row
is the six-cycle at $a^2=-1$, where it joins the two fixed points and
gives exactly eight. This determinant cannot also equal $\pm1$ in
an allowed characteristic.

For $a=1$, the four $(C,\text{point count})$ entries are
$(1,2),(-3,2),(0,4),(-1,6)$. Pairwise differences are among
$\{\pm1,\pm2,\pm3,\pm4\}$; with characteristic two excluded,
the only possible equality is $-3=0$ in characteristic three.
It combines two and four points, while the six-point three-cycle
locus stays separate. The maximum is six.

For $a=-1$, the fixed and two-cycle rows meet at $C=0$ and total four.
The four-cycle lies at $C=-1$. In characteristic three only, the two
five-cycles lie at that same $C=-1$ and contribute ten additional,
distinct points. The eight-cycle is at $C=1$, disjoint from both
other parameter values. Thus the maximum is exactly fourteen, with
precisely the stated characteristic-three, $a=-1$, $c=-P^2-1$ locus.

Outside characteristics two and three the maximum is eight exactly
when the field admits a square root of $-1$; otherwise the conservative
three-cycle pair attains six. Choosing $P=t$ realizes the bounds over
the stated field, without adjoining constants. The period-greater-than-two
determinant restriction follows from the atlas's $a=\pm1$ or $a^2=-1$.
Finally, counting points of each finite cycle at times divisible by its
least period gives Corollary 3 directly. These checks complete the
reviewer's mathematical PASS; they do not elevate the corollary to a
separate research contract.

## 7. Affected-revision closure

The coordinator adopted the optional Step 5 converse clarification.
The reviewer read only the affected paragraph in the revised proof:
the two leading coefficients first determine
$\varepsilon'=\varepsilon(-1)^v$ and $v'=w$; the first constant offset
then determines $u'=v$ using $a\ne0$; finally $z=w'$ gives the remaining
edge equation. This is exactly the valid recovery order identified in
§6.1 and removes the possible ambiguity of using a lone constant offset.
The affected revision is **PASS / CLOSED**, with no outstanding required
mathematical repair.

Final proof SHA256 at this affected-revision check:

```text
a5f10ff4354adb0fa86ffdf6868b9f7c7658e2e95116a62d20142c0308be6ccb
```

The previous full-proof verdict carries forward with this checked
clarification. No new full review, enumeration, mathematical test, old
certificate or PDF build was performed. Source-audit completion,
admission records and all other files remain coordinator-owned.
