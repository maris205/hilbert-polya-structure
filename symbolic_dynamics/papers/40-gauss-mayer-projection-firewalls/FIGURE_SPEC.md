# Paper 40 figure specification — SD-C42

All three figures are writer-owned pure TikZ. They contain no raster image,
external artwork, opacity-dependent distinction, or provisional experiment
value. Color, border style, node shape, and line style jointly encode meaning
so the figures remain legible in grayscale. Mathematical labels follow the
immutable source and type firewalls exactly.

## Figure 1 — typed return, same-object ledger, and projection gate

File: `figures/object_projection_gate.tex`.

- Far left: digit space
  $X=\mathbb N^{\mathbb N}$ with one-digit shift $\sigma$ and one marker
  factor $u$ per digit.
- Left center: grouping map
  $\iota(a_1,a_2,a_3,a_4,\ldots)=((a_1,a_2),(a_3,a_4),\ldots)$ into pair
  space $X_2=(\mathbb N^2)^{\mathbb N}$ with one-pair shift $\rho$.
- The commuting label is the typed identity
  $\rho\circ\iota=\iota\circ\sigma^2$; the artwork must not place
  $\sigma^2$ directly on $X_2$.
- A pair-return badge states `one pair = two digits = marker $u^2$` and names
  `RhoPrimitivePair`.
- Center upper: ordered monodromy
  $M=A(a_1)\cdots A(a_{2k})\in\mathrm{SL}_2(\mathbb Z)$ and the
  branch/matrix bridge, carrying the roof $T=2\log\lambda$.
- Center lower: same-space analytic path
  $K_s=\mathcal L_s^2$ to
  $D_{42}(s,u)=\det(I-u^2K_s)$, labeled `intrinsic pair ledger`.
- Right upper: exactly three projection boxes:
  $P_t=t$, $P_\Delta=\Delta_{\mathbb Z[M]}=t^2-4$, and
  $P_N=\lambda^2$.
- Right lower: a barred gate labeled `rational-prime reciprocal-Euler-ledger
  conjunction`, with failure tags for support/multiplicity,
  clock/repetition, amplitude, and owner.
- Bottom positive bar:
  `intrinsic pair ledger + same-space Fredholm determinant: GO`.

Caption requirement: state that the typed pair object and determinant retain
positive modular credit, while none of the three scalar maps preserves the
full rational-prime support/multiplicity/clock/repetition/amplitude/ownership
conjunction. The functional $u=1$ identity supplies no objectwise
pair/geodesic bridge.

## Figure 2 — exact algebra and explicit collision classes

File: `figures/algebraic_firewalls.tex`.

- Three top panels:
  1. order discriminant:
     $(t-2)(t+2)$, prime exactly at $(t,\Delta)=(3,5)$;
  2. norm and clock:
     $(t-1)^2<\Delta<t^2$, $\lambda^2\notin\mathbb Q$,
     $\lambda^2>t$;
  3. repetition and amplitude:
     $q_r=tq_{r-1}-q_{r-2}$,
     $q_2=t^2-2\ne t^2$, and the surviving source factor
     $(1-d_w^r)^{-1}$.
- Lower row, three exact collision-class panels:
  1. trace $4$: `((1,2))` versus `((2,1))`, labeled
     `reversal phases; distinct because reversal is not quotiented`;
  2. trace $6$: `((1,4))` versus `((2,2))`, labeled
     `one-pair non-reversal`;
  3. trace $10$: `((2,4))` versus `((1,1),(1,2))`, labeled
     `non-reversal; pair lengths 1 and 2`.
- Each collision panel contains its two frozen ordered matrices and common
  order discriminant: $12$, $32$, and $96$, respectively.
- The trace-$4$ panel also carries a `composite full-ledger species` badge.
- No finite collision census appears; the figure communicates exact contract
  falsifiers and gives no discovery, priority, or size-optimality signal.

Caption requirement: distinguish the prime order-discriminant boundary,
irrational norm, wrong trace clock/powers, source amplitude, duplicate source
species, and the composite trace in the full ledger. State that all three
projections collide because $P_\Delta$ and $P_N$ factor through $t$.

## Figure 3 — primitivity, analytic domains, and selector ownership

File: `figures/type_source_ownership.tex`.

- Left column: three separately shaped boxes:
  `RhoPrimitivePair`, `SigmaPrimitiveDigit`, and
  `GeodesicPrimitiveClass`.
- The digit/pair relation is the splitting law, not a type equality:
  `odd sigma period: one cycle; even sigma period: two cycles`, with
  $N_{D^2}(k)=2N_D(2k)+\mathbf1_{k\text{ odd}}N_D(k)$.
- Barred arrows from `RhoPrimitivePair` to the other two types say
  `no bridge lemma / no coercion`.
- Center: Mayer's disk algebra with three nested but distinct domain claims:
  1. nuclearity and holomorphic Fredholm identity for
     $\operatorname{Re}s>1/2$;
  2. initial absolute convergence of the Selberg Euler product for
     $\operatorname{Re}s>1$;
  3. source-qualified meromorphic continuation to $\mathbb C$.
- A local-$u$ badge states:
  `Fredholm log/product: formal in $u^2$ or small $|u|$ near 0`.
- The equality at $u=1$ is labeled `functional identity`, not `orbit
  bijection`; no arbitrary-$u$ Selberg label appears.
- Right: the three scalar labels feed a dashed postselection box, followed by
  a barred arrow to the untwisted $K_s$ owner labeled
  `no declared reducing projector / selected Fredholm owner`.
- A scope badge states `twists, changed spaces, direct sums, and changed
  roofs: outside contract`.

Caption requirement: say that the three primitive types remain separate,
even and odd digit periods obey the displayed splitting law, the analytic
claims use exactly the source-supported domains, and the selector STOP is an
absence-of-declared-owner statement for the frozen untwisted operator only.

## Shared visual language

- `formalblue`: frozen object, equation, or source theorem;
- `deepgreen`: retained positive ownership/GO statement;
- `warningamber`: boundary, distinct type, or outside-contract item;
- `stopred`: failed conjunction or barred credit transfer;
- `governancepurple`: Route/contract scope;
- `softgray`: metadata and neutral grouping.

Solid arrows denote declared same-object maps. Dashed arrows denote scalar
postprocessing or outside-contract associations. Dotted arrows denote
functional/source relationships without objectwise coercion. A barred line
denotes forbidden credit transfer.

## Quality checklist

- pure vector TikZ;
- no title inside the artwork;
- no provisional integrator value;
- no red/green-only distinction;
- minimum text remains legible in the compiled A4 manuscript;
- no arrow crosses or hides an endpoint;
- captions are self-contained;
- every figure is introduced before or at first placement;
- matrix order and theorem equations match the immutable proof package;
- return-map typing, even/odd splitting, and Mayer domains match the
  immutable firewalls;
- no wording implies a new two-variable zeta mechanism or collision priority.
