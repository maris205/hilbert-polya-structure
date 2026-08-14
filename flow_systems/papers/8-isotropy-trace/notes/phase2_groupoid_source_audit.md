# Paper 8 Phase-2 groupoid/imprimitivity source audit

**Audit date:** 2026-08-14  
**Verdict:** **PASS — source coverage for the one-orbit completion, with packet/global scope explicitly withheld**  
**Phase boundary:** source and theorem-hypothesis audit only.  This file does not prove
P8-1--P8-9, select a trace, identify `Q_p` with `B_p`, or enter manuscript drafting.

## 1. Exact object audited

Put

```text
G = R,
H = L Z  (L>0),
K = G/H = R/(L Z),
A_L = C*(K rtimes G) = C(K) rtimes_lt G.
```

Here `A_L` is the full algebra of the **single transitive orbit** record
`DEN-EF-ORBIT-ACTION-GRPD`.  It is not the full packet algebra
`C*(Gamma_p rtimes R)`, and no claim below transports through a packet product
chart.

The lock writes an arrow `(x,t)` from `x` to `phi^t(x)`.  The conventional
range-first transformation groupoid used in the retained sources writes an arrow
`(y,t)` from `phi^{-t}(y)` to `y`.  The convention change is the groupoid
isomorphism

```text
(x,t)_lock |-> (phi^t(x),t)_range-first.
```

Thus the source results apply without changing the locked groupoid.  On an
`r`-fibre over `y`, the proposed Haar system is

```text
lambda^y(f) = integral_R f(phi^{-t}(y),t) dt.
```

Lebesgue translation invariance gives left invariance, and the defining
continuity condition follows for `f in C_c(K x R)` from continuity of the action
and compact support.  This is a convention/assumption check against the standard
Haar-system definition, not a new packet-level topology theorem.

For the one-orbit object all relevant hypotheses hold:

- `G=R` is locally compact, Hausdorff, second countable, unimodular, and
  amenable;
- `H=L Z` is a closed, discrete, second-countable subgroup;
- `K=R/(L Z)` is compact, Hausdorff, and second countable;
- the `R`-action on `K` is continuous and transitive, with isotropy exactly
  `H`; and
- the above continuous Haar system is available.

These facts do **not** discharge the separate source-topology gates for an actual
packet `Gamma_p`.

## 2. Source-verified findings

### G1. Amenability and full versus reduced

Anantharaman-Delaroche defines amenability for a locally compact transformation
group in Definition 2.1 and proves in Examples 2.7(2) that every action of an
amenable locally compact group is amenable.  No separability assumption on the
locally compact transformation space is needed in that survey.  Her Theorem 5.3
states that an amenable transformation group `(X,G)` has

```text
C*_r(G,D) = C*(G,D)
```

for every `G-C_0(X)`-algebra `D`; taking `D=C_0(X)` gives equality for the
transformation-group algebra.  Independently, Williams, Theorem 7.13, proves
full/reduced equality for every action of an amenable locally compact group.

Therefore, for this one-orbit action,

```text
C*(K rtimes R) = C*_r(K rtimes R).
```

This conclusion uses amenability of `R`, not transitivity alone and not merely
weak containment of the isotropy group.

### G2. Green/Mackey imprimitivity and induced isotropy characters

Green's original Proposition 3 constructs the relevant imprimitivity bimodule.
Williams, Theorem 4.22, gives the modern precise form: for a locally compact
group `G`, closed subgroup `H`, and the left translation action on `G/H`, the
Green module is a

```text
C_0(G/H) rtimes G  --  C*(H)
```

imprimitivity bimodule (the general theorem includes coefficients).  MRW,
Theorem 2.8, gives the parallel groupoid statement for second-countable locally
compact groupoids with Haar systems and a groupoid equivalence.

Williams, Theorem 5.12, identifies Rieffel induction through the Green module
with ordinary group induction.  Specializing its coefficient algebra to `C`, a
character

```text
chi_theta(rL) = exp(i r theta),  theta in [0,2pi),
```

of `H=L Z` induces a representation `pi_theta` of `A_L`, and the underlying
unitary `R`-representation is `Ind_H^G chi_theta`.  Under the concrete
isomorphism in G3, `pi_theta` is the point representation at `chi_theta` on
the `C(hat H)` factor, tensored with the defining representation of the compact
operators.  This labels fibres; it does not source-select `theta=0`, a
transverse measure, or a normal extension.

### G3. Morita, stable isomorphism, and actual isomorphism are three different claims

The sources support the following strict evidence ladder.

| Level | Exact result | What it licenses here |
|---|---|---|
| Strong Morita equivalence | Green, Proposition 3; Williams, Theorem 4.22; MRW, Theorem 2.8 | `A_L ~_M C*(H)` |
| Stable isomorphism | Brown--Green--Rieffel, Theorem 1.2, for algebras with strictly positive elements (in particular separable algebras) | `A_L tensor K ~= C*(H) tensor K` |
| Unstabilized concrete isomorphism | Williams, Theorem 4.30; independently MRW, Theorem 3.1 for a second-countable transitive groupoid | `A_L ~= C*(H) tensor K(L^2(K,mu))` |

The last line is **not** obtained by cancelling `K` from the BGR result or by
silently upgrading Morita equivalence.  It is licensed by its own stronger
theorem.  Williams's theorem assumes only that `H` is a closed subgroup of the
locally compact group `G` and uses a quasi-invariant measure `mu` on `G/H`
satisfying his equation (4.63).  In the present unimodular quotient, normalized
or length Haar is admissible; changing between them gives unitarily equivalent
`L^2` spaces but does not by itself fix a trace normalization.

Since `H=L Z` is discrete abelian,

```text
C*(H) ~= C(hat H) ~= C(T),
```

where the last coordinate uses the positive generator `L`.  Since
`L^2(K,mu)` is infinite-dimensional and separable,

```text
A_L ~= C(T) tensor K(L^2(K,mu)) ~= C(T,K).
```

Consequently the one-orbit algebra is not merely known to be Morita equivalent
or stably isomorphic: it is a **trivial continuous field of compact operators
over the isotropy dual `hat H ~= T`**, hence a continuous-trace algebra.  The
displayed isomorphism is not asserted to be canonical or trace-preserving;
Williams's proof uses a measurable cross-section, and MRW explicitly notes the
choice dependence of the concrete isomorphism.

### G4. What the C*-completion results do not decide

The preceding sources do not, on their own, identify the locked regular von
Neumann representation, its multiplicity, or its transverse measure.  A
separate Fourier/Plancherel argument is required before one may write a normal
closure such as

```text
L-infinity(hat H,m_hatH) bar-tensor B(L^2(K,mu)).
```

That display is therefore only the expected conditional form, not a conclusion
of this audit.  In particular:

- a point character `chi_theta`, including the trivial character, is a valid
  `C*`-fibre representation;
- full/reduced equality does not make point evaluation normal in a particular
  regular von Neumann completion;
- Morita equivalence and even the concrete `C*`-isomorphism do not transport a
  chosen FNS trace without specifying the representation and measures; and
- no regular/trivial-character trace formula, Poisson formula, or
  non-normal-extension result receives proof credit from this file.

## 3. Scope barriers for `Gamma_p` and `Q_p`

1. The exact tensor-product theorem above applies to one transitive orbit
   `R/(L_p Z)`, whose orbit quotient is a point.  It does not identify the full
   packet groupoid with a product over `Q_p`.
2. Even if the source-topology audit proves that
   `K_p=R/(L_p Z)` acts freely and compactly on `Gamma_p`, the intrinsic quotient
   remains `Q_p=Gamma_p/K_p`.  None of the retained operator-algebra sources
   identifies `Q_p` with the abstract `B_p`.
3. A principal `K_p`-bundle over `Q_p` need not be globally trivial.  Fibrewise
   copies of `C(T) tensor K` do not by themselves yield
   `C(Q_p) tensor C(T) tensor K`; a packet-level equivalence/twist and its
   Dixmier--Douady or bundle data would have to be audited separately.
4. No topological coproduct over primes, inherited all-prime topology, packet
   probability, or cross-prime mass is supplied by Green/MRW imprimitivity.

These barriers preserve the active `Q_p != B_p` and same-object rules.

## 4. Primary locators and assumption ledger

### Philip Green (primary)

Philip Green, “The local structure of twisted covariance algebras,” *Acta
Mathematica* **140** (1978), 191--250,
doi:10.1007/BF02392308.

- Proposition 3, printed p.203: the dense Green bimodule is an
  imprimitivity bimodule for the homogeneous-space imprimitivity algebra and
  the subgroup crossed product.
- Retained as the primary historical source for the Morita/imprimitivity step;
  the clearer exact specialization used above is Williams, Theorem 4.22.

### Muhly--Renault--Williams (primary)

Paul S. Muhly, Jean N. Renault, and Dana P. Williams, “Equivalence and
isomorphism for groupoid C*-algebras,” *Journal of Operator Theory* **17**(1)
(1987), 3--22.

- Theorem 2.8, printed p.10: for second-countable locally compact groupoids
  with Haar systems and a `(G,H)`-equivalence, `C_c(Z)` completes to a
  `C*(G)`--`C*(H)` imprimitivity bimodule.
- Theorem 3.1, printed p.16: for a second-countable transitive groupoid `G`,
  a unit `u`, and isotropy `H=G_u^u`, there is a positive measure `mu` on the
  unit space such that
  `C*(G) ~= C*(H) tensor K(L^2(G^(0),mu))`.
- The theorem concerns the full groupoid algebra; reduced equality is supplied
  separately by amenability.

### Brown--Green--Rieffel (primary)

Lawrence G. Brown, Philip Green, and Marc A. Rieffel, “Stable isomorphism and
strong Morita equivalence of C*-algebras,” *Pacific Journal of Mathematics*
**71**(2) (1977), 349--363, doi:10.2140/pjm.1977.71.349.

- Theorem 1.2, printed p.351: strong Morita equivalence plus strictly positive
  elements implies stable isomorphism; stable isomorphism implies strong
  Morita equivalence.
- The example on printed pp.351--352 applies this specifically to
  `C*(G,G/H)` and `C*(H)` when separable, and explicitly mentions `G=R`,
  `H=Z`.
- This source is a fallback/stable statement, not the authority for the
  stronger unstabilized model.

### Anantharaman-Delaroche (primary, author-hosted)

Claire Anantharaman-Delaroche, “Amenability and exactness for dynamical systems
and their C*-algebras,” *Transactions of the American Mathematical Society*
**354**(10) (2002), 4153--4178,
doi:10.1090/S0002-9947-02-02978-1.

- Definition 2.1 and Proposition 2.2, manuscript pp.3--4 (published
  pp.4155--4156): transformation-group amenability and equivalent tests.
- Examples 2.7(2), manuscript p.6 (published p.4158): every action of an
  amenable locally compact group is amenable.
- Theorem 5.3, manuscript p.14 (published p.4166): amenability implies
  full/reduced equality for every `G-C_0(X)`-algebra.
- The paper states that this transformation-group treatment does not require a
  separability assumption on the locally compact spaces.

### Dana P. Williams (authoritative author draft, with published metadata)

Dana P. Williams, *Crossed Products of C*-Algebras*, author manuscript,
Version 3.1, 6 September 2006; published as Mathematical Surveys and
Monographs **134**, American Mathematical Society, 2007,
ISBN 978-0-8218-4242-3.

- Theorem 4.22, printed p.132: Green's imprimitivity theorem with exact module
  and closed-subgroup hypotheses.
- Theorem 4.30, printed p.138: actual isomorphism
  `C_0(G/H) rtimes G ~= C*(H) tensor K(L^2(G/H,mu_G/H))`, with `mu_G/H`
  satisfying (4.63).
- Theorem 5.12, printed p.161: compatibility of Green/Rieffel induction with
  ordinary induced representations.
- Theorem 7.13, printed p.199: for amenable `G`, universal and reduced norms
  coincide for every dynamical system.

## 5. Retained-source manifest and checksums

All URLs were accessed on 2026-08-14.  Only load-bearing primary or
authoritative full texts were retained.  The `grp-*` namespace was reserved in
advance to prevent collision with the topology (`topo-*`) and trace/harmonic
audits.

| Local artifact | Pages | SHA-256 | Source URL |
|---|---:|---|---|
| `sources/grp-green-local-structure-1978.pdf` | 60 | `bca0701f16e965424563004c5e6d9eec2a9310e05b860857f23d97b2f8819b3d` | `https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6237-11511_2006_Article_BF02392308.pdf` |
| `sources/grp-muhly-renault-williams-equivalence-1987.pdf` | 20 | `16723f6b3b3d90f220a4bc0814ed8374817ae2025c8eef9822f520a8da7b6629` | `https://jot.theta.ro/jot/archive/1987-017-001/1987-017-001-001.pdf` |
| `sources/grp-brown-green-rieffel-stable-isomorphism-1977.pdf` | 19 | `d2b64846c0dd59668f261782ae832df1bb7dad15479d5bb5c2e7aeec37fd19c8` | `https://msp.org/pjm/1977/71-2/pjm-v71-n2-p06-s.pdf` |
| `sources/grp-anantharaman-delaroche-amenability-exactness-2002.pdf` | 28 | `a5e908a4c310e5ce162c3a8ab090d491b1cb024a3c5cb36bbb7ac2b9135739ab` | `https://idpoisson.fr/anantharaman/publications/Exactness02.pdf` |
| `sources/grp-williams-crossed-products-draft3.1.pdf` | 540 | `3dbc1fb9e96191a278e0d59feb4981d3bbea4faa4df609d1886c81125bffe9c2` | `https://math.dartmouth.edu/~dana/cpcsa/draft3.1.pdf` |

Each PDF has a same-stem `.preflight.json` sidecar generated once with the ARS
`pdf_read_preflight/1.0.0` script.  Sidecar checksums are:

| Preflight sidecar | Verdict | SHA-256 |
|---|---|---|
| `sources/grp-green-local-structure-1978.preflight.json` | `UNAVAILABLE` | `5bd1d5e010721ba5546cd92a67df783f083ebdc0e29ad9264da7b38177fb7c65` |
| `sources/grp-muhly-renault-williams-equivalence-1987.preflight.json` | `UNAVAILABLE` | `29604fed0515d7626a34045279adbf80cad84a3832f1949fb3d8db03558391a6` |
| `sources/grp-brown-green-rieffel-stable-isomorphism-1977.preflight.json` | `UNAVAILABLE` | `74f410fe5618946780b11200cca58fdcd91c91b95d7fbcf0b60300474887b761` |
| `sources/grp-anantharaman-delaroche-amenability-exactness-2002.preflight.json` | `UNAVAILABLE` | `4bb6fc7c8c75b6167c4fc7433c504e0b410ba1ca953e378cc7ee5e361ca19991` |
| `sources/grp-williams-crossed-products-draft3.1.preflight.json` | `UNAVAILABLE` | `745284c93aa2e2934f2714bb846cc2d8b3897001b538803e09dff072d0377fda` |

The uniform `UNAVAILABLE` reason is environmental, not a damaged-PDF finding:
`pypdf` is not installed.  As the required fallback, `pdfinfo` independently
returned the page counts above; `pdftotext` yielded 69,702, 39,815, 156,700,
and 1,229,539 bytes for the Anantharaman-Delaroche, BGR, Green, and Williams
files respectively.  The MRW artifact is an image-only scan (`pdftotext`: 20
bytes), so printed pp.10 and 16 were independently inspected as rendered page
images before recording Theorems 2.8 and 3.1.  Page locators in this audit use
the printed pagination, not an unverified PDF page offset.

## 6. Safe downstream claim language

Safe:

> For the one-orbit action groupoid
> `(R/(L Z)) rtimes R`, Lebesgue time defines the standard Haar system; the
> action is amenable, so full and reduced algebras agree.  Green's homogeneous-
> space theorem, equivalently the transitive-groupoid isomorphism theorem of
> Muhly--Renault--Williams, gives
> `C*((R/(L Z)) rtimes R) ~= C(T) tensor K(L^2(R/(L Z)))`.

Unsafe without further work:

- “Morita equivalence alone proves `C(T) tensor K`.”
- “The isomorphism canonically transports the regular trace.”
- “The same tensor product describes the entire packet `Gamma_p`.”
- “`Q_p` is `B_p`, or the packet bundle is trivial.”
- “Full equals reduced, therefore the trivial-character fibre is normal.”
- “The groupoid C*-algebra result already proves the locked FNS/Poisson return
  formula.”

**Final gate:** the original/authoritative source chain is adequate for the
one-orbit Haar, amenability, full/reduced, imprimitivity, induced-character, and
exact C*-completion claims.  Packet topology, packet fields/twists, regular
von Neumann decomposition, trace normality, and all cross-prime ownership
remain separate Phase-2 gates.
